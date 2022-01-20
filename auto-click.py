import pyautogui as pg
import time
import turtle
starttime = time.time()

def doHeroes():
    
    pg.leftClick(210, 178, interval=1, duration=1)
    pg.leftClick(1166, 174, interval=1, duration=1)
    waitTime(180.0)
    
    pg.leftClick(736, 480, interval=1, duration=1)
    pg.leftClick(1700, 493, interval=1, duration=1)
    waitTime(180.0)
    
    pg.leftClick(424, 248, interval=1, duration=1)
    pg.leftClick(1390, 254, interval=1, duration=1)
    waitTime(180.0)
    
    pg.leftClick(517, 222, interval=1, duration=1)
    pg.leftClick(1472, 229, interval=1, duration=1)
    waitTime(180.0)
    
    pg.leftClick(492, 301, interval=1, duration=1)
    pg.leftClick(1444, 317, interval=1, duration=1)
    waitTime(300.0)
    
    #normal direct process
    #bomb1
    #pg.leftClick(210, 178, interval=1, duration=1)
    #pg.leftClick(736, 480, interval=1, duration=1)
    #pg.leftClick(424, 248, interval=1, duration=1)
    #pg.leftClick(517, 222, interval=1, duration=1)
    #pg.leftClick(492, 301, interval=1, duration=1)
    #bomb2
    #pg.leftClick(1166, 174, interval=1, duration=1)
    #pg.leftClick(1700, 493, interval=1, duration=1)
    #pg.leftClick(1390, 254, interval=1, duration=1)
    #pg.leftClick(1472, 229, interval=1, duration=1)
    #pg.leftClick(1444, 317, interval=1, duration=1)

def printPosition():
    pos = pg.position()
    # for x pos
    print(pos[0])
    # for y pos
    print(pos[1])
    
def waitTime(timeInMiliseconds):
    time.sleep(timeInMiliseconds - ((time.time() - starttime) % timeInMiliseconds))
    
#while True:
#    time.sleep(3.0 - ((time.time() - starttime) % 3.0))
#    printPosition()
#    starttime = time.time()
#    time.sleep(7.0 - ((time.time() - starttime) % 7.0))
while True:
    waitTime(5.0)
    doHeroes()
    waitTime(300.0)




