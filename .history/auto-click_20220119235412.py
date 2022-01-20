import pyautogui as pg
import time
starttime = time.time()

def doHeroes():
    #pedroeuropeu-bomb1
    pg.leftClick(169, 158, interval=1, duration=1)
    pg.leftClick(874, 574, interval=1, duration=1)
    pg.leftClick(462, 265, interval=1, duration=1)
    pg.leftClick(580, 232, interval=1, duration=1)
    pg.leftClick(554, 347, interval=1, duration=1)
    #pedroeuropeu-bomb2
    pg.leftClick(1125, 183, interval=1, duration=1)
    pg.leftClick(1822, 592, interval=1, duration=1)
    pg.leftClick(1411, 288, interval=1, duration=1)
    pg.leftClick(1525, 246, interval=1, duration=1)
    pg.leftClick(1502, 389, interval=1, duration=1)

while True:
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
    doHeroes()
    time.sleep(240.0 - ((time.time() - starttime) % 240.0))




