import Oled
import Random
import machine

SCREEENWIDTH = 128
SCREEENHEIGHT = 32
GROUND = SCREEENHEIGHT
oled = Oled.Oled(SCREEENWIDTH, SCREEENHEIGHT)
oled.erase()
robj = Random.Random()


class GameHandler:
    jumpButton = None
    gravity = 0.0
    player = None
    enemies = []
    score = 0

    def __init__(self):
        self.jumpButton = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

        global GROUND

        self.player = GameObject(5, GROUND - 15, 10, 15)

        self.gravity = GROUND / 30
        self.gravity = 3
        # SHould be last line of the constructor
        self.playGame()

    def playGame(self):
        while True:
            self.updateGame()
            self.drawObjects()

    def updateGame(self):
        if not self.jumpButton.value():
            self.player.jump()

        if len(self.enemies) >= 1 \
                and self.enemies[0].x + self.enemies[0].width <= 0:
            self.enemies.pop(0)
            self.score += 1

        if len(self.enemies) < 1:
            self.enemies.append(GameObject(SCREEENWIDTH - 10, GROUND - 15, 10, 15, -9))

        self.moveGameObjects()

    def moveGameObjects(self):
        global GROUND

        # player logic
        self.player.x += self.player.vx
        self.player.vy += self.gravity
        newPlayerY = self.player.y + self.player.vy
        if newPlayerY + self.player.height > GROUND:
            self.player.y = GROUND - self.player.height
            self.player.vy = 0
        else:
            self.player.y = newPlayerY

        # enemies
        for enemy in self.enemies:
            enemy.x += enemy.vx

    def drawObjects(self):
        global oled
        oled.erase(0)
        self.player.draw()

        for enemy in self.enemies:
            enemy.draw()

        oled.message('Score: ' + str(self.score), SCREEENWIDTH - (8*9))

        # oled.message(str(self.player.y) + " " + str(self.player.height))

        # keep this at the bottom
        oled.show()


# gameobject class for both enemies and the player
class GameObject:
    x = 0
    y = 0
    witdh = 0
    height = 0
    vx = 0
    vy = 0

    def __init__(self, x, y, width, height, vx=0, vy=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy

    def draw(self):
        oled.rectangle(int(self.x), int(self.y), int(self.width), int(self.height), show=0)

    def jump(self):
        global GROUND
        if self.y + self.height >= GROUND:
            self.vy -= 14


gameHandler = GameHandler()
