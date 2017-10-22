import time, ssd1306

for i in range(10):
    oled.fil(0)
    oled.text(str(i), 0, 0)
    oled.show()
    time.sleep(1)