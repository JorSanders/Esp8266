import machine

import Random
import Oled
import PotentioMeter

SCREEENWIDTH = 128
SCREEENHEIGHT = 32
oled = Oled.Oled(SCREEENWIDTH, SCREEENHEIGHT)
oled.erase()
robj = Random.Random()
PLAYERWIDTH = 5
PLAYERHEIGHT = 10
PLAYERSPEED = 2
PLAYER1BUTTONUPPIN = 13
PLAYER1BUTTONDOWNPIN = 2
PLAYER2BUTTONUPPIN = 12
PLAYER2BUTTONDOWNPIN = 14
PLAYER1LEDPIN = 0
PLAYER2LEDPIN = 15
BALLRADIUS = 6
BALLSTARTVX = -20
BALLSTARTVY = 6
SCORELIMIT = 2
PLAYER1NAME = 'Player 1'
PLAYER2NAME = 'Player 2'


class GameHandler:
    players = []
    ball = None
    potentioMeter = None
    player1Led = None
    player2Led = None

    def __init__(self):
        self.players = []
        self.players.append(
            Player(0, 0, PLAYERWIDTH, PLAYERHEIGHT, PLAYER1BUTTONUPPIN, PLAYER1BUTTONDOWNPIN, PLAYER1NAME,
                   PLAYER1LEDPIN, 'L'))
        self.players.append(
            Player(SCREEENWIDTH - PLAYERWIDTH, 0, PLAYERWIDTH, PLAYERHEIGHT, PLAYER2BUTTONUPPIN, PLAYER2BUTTONDOWNPIN,
                   PLAYER2NAME, PLAYER2LEDPIN, 'R'))

        self.ball = Ball(SCREEENWIDTH - BALLRADIUS * 2, SCREEENHEIGHT / 2, BALLRADIUS, BALLSTARTVX, BALLSTARTVY)
        self.potentioMeter = PotentioMeter.PotentioMeter()

        # Should be last line of the constructor
        self.playGame()

    def playGame(self):
        while True:
            self.updateGame()
            self.drawObjects()

    def updateGame(self):
        for player in self.players:
            if not player.buttonUp.value():
                player.up()
            elif not player.buttonDown.value():
                player.down()

        self.moveGameObjects()

    def moveGameObjects(self):
        # player logic
        for player in self.players:
            player.y += player.vy
            if player.y < 0:
                player.y = 0
            elif player.y + player.height > SCREEENHEIGHT:
                player.y = SCREEENHEIGHT - player.height

        # ball y logic
        self.ball.y += self.ball.vy * self.potentioMeter.getPercentage()
        if self.ball.y + self.ball.radius > SCREEENHEIGHT:
            self.ball.y = SCREEENHEIGHT - self.ball.radius
            self.ball.vy *= -1
        elif self.ball.y - self.ball.radius < 0:
            self.ball.y = self.ball.radius
            self.ball.vy *= -1

        self.ball.x += self.ball.vx * self.potentioMeter.getPercentage()

        for player in self.players:
            if Physics.circleRectangleCollision(self.ball.x, self.ball.y, self.ball.radius, player.x,
                                                player.y, player.width, player.height):
                self.ball.vx *= -1
                if player.side == 'L':
                    self.ball.x = player.x + player.width + self.ball.radius
                elif player.side == 'R':
                    self.ball.x = player.x + - self.ball.radius

        # ball on the right side
        if self.ball.x + self.ball.radius > SCREEENWIDTH - PLAYERWIDTH / 2:
            self.ball.x = SCREEENWIDTH - self.ball.radius - PLAYERWIDTH / 2
            self.ball.vx *= -1
            for player in self.players:
                if player.side == 'L':
                    player.goal()
                    if player.score >= SCORELIMIT:
                        self.endGame(player)

        # ball on the left side
        elif self.ball.x - self.ball.radius < 0 + PLAYERWIDTH / 2:
            self.ball.x = self.ball.radius + PLAYER2LEDPIN / 2
            self.ball.vx *= -1
            for player in self.players:
                if player.side == 'R':
                    player.goal()
                    if player.score >= SCORELIMIT:
                        self.endGame(player)

    def drawObjects(self):
        oled.erase(0)

        for player in self.players:
            player.draw()

        self.ball.draw()

        # keep this at the bottom
        oled.show()

    def endGame(self, winner):
        oled.erase(0)
        while True:
            oled.message(winner.name + ' wins', show=0)
            #oled.message(loser.name + ' loses', y=10, show=0)
            oled.show()


class Player:
    x = 0
    y = 0
    witdh = 0
    height = 0
    vy = 0
    buttonUp = None
    buttonDown = None
    score = 0
    name = ''
    side = ''

    def __init__(self, x, y, width, height, buttonUpPin, buttonDownPin, name, ledPin, side):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonUp = machine.Pin(buttonUpPin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.buttonDown = machine.Pin(buttonDownPin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.score = 0
        self.name = name
        self.led = machine.PWM(machine.Pin(ledPin))
        self.led.freq(60)
        self.led.duty(0)
        self.side = side

    def draw(self):
        oled.rectangle(int(self.x), int(self.y), int(self.width), int(self.height), show=0)

    def up(self):
        self.vy = -PLAYERSPEED

    def down(self):
        self.vy = PLAYERSPEED

    def goal(self):
        self.score += 1
        self.led.duty(int(1024 / SCORELIMIT * self.score))


class Ball:
    x = 0
    y = 0
    witdh = 0
    height = 0
    vx = 0
    vy = 0

    def __init__(self, x, y, radius, startVx, startVy):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = startVx
        self.vy = startVy

    def draw(self):
        oled.circle(self.x, self.y, self.radius, show=0)


class Physics:
    @staticmethod
    def rectangleCollision(x0, y0, width0, height0, x1, y1, width1, height1):
        if x0 + width0 > x1 and x0 < x1 + width1 \
                and y0 + height0 > y1 and y0 < y1 + height1:
            return True

    @staticmethod
    def circleRectangleCollision(circleX, circleY, circleR, rectX, rectY, rectWidth, rectHeight):
        for x in range(rectX, rectX + rectWidth + 1):
            for y in range(rectY, rectY + rectHeight + 1):
                distanceX = x - circleX
                distanceY = y - circleY
                if distanceX * distanceX + distanceY * distanceY <= circleR * circleR:
                    return True
        return False


gameHandler = GameHandler()
