import pyautogui as pg
import time
import turtle

starttime = time.time()


def doHeroes():
    pg.leftClick(210, 178, interval=1, duration=1)
    pg.leftClick(1166, 174, interval=1, duration=1)

    pg.leftClick(736, 480, interval=1, duration=1)
    pg.leftClick(1700, 493, interval=1, duration=1)

    # all rest
    pg.leftClick(466, 254, interval=1, duration=1)
    pg.leftClick(1406, 253, interval=1, duration=1)
    print("all resting for 120s")
    waitTime(120.0)
    # all work
    pg.leftClick(424, 248, interval=1, duration=1)
    pg.leftClick(1390, 254, interval=1, duration=1)
    print("all working")

    pg.leftClick(517, 222, interval=1, duration=1)
    pg.leftClick(1472, 229, interval=1, duration=1)

    pg.leftClick(492, 301, interval=1, duration=1)
    pg.leftClick(1444, 317, interval=1, duration=1)


def keepSessionActive():
    pg.leftClick(212, 169, interval=1, duration=1)
    pg.leftClick(505, 343, interval=1, duration=1)
    pg.leftClick(1170, 171, interval=1, duration=1)
    pg.leftClick(1445, 337, interval=1, duration=1)
    waitTime(120.0)
    print("keeping sessions active for 120s")


def printPosition():
    pos = pg.position()
    # for x pos
    print(pos[0])
    # for y pos
    print(pos[1])


def waitTime(timeInMiliseconds):
    time.sleep(timeInMiliseconds - ((time.time() - starttime) % timeInMiliseconds))


# while True:
#    waitTime(5.0)
#    doHeroes()
# printPosition()
#    waitTime(120.0)

counter = 0

while True:
    waitTime(5.0)
    if counter < 150:
        keepSessionActive()
        counter += 1
print("keep session...")
else:
doHeroes()
waitTime(1.0)
keepSessionActive()
waitTime(1.0)
doHeroes()
waitTime(1.0)
counter = 0
