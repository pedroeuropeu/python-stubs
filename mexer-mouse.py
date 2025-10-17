#!/usr/bin/env python3
"""
human_mouse_esc_pynput.py
Movimenta o mouse devagar e aleatoriamente de forma "humana".
Pressione ESC para parar.
"""

import pyautogui
import random
import time
import math
from pynput import keyboard

pyautogui.FAILSAFE = True

stop_flag = False  # controla parada

def on_press(key):
    global stop_flag
    if key == keyboard.Key.esc:
        stop_flag = True
        print("\n🛑 ESC pressionado. Encerrando...")

listener = keyboard.Listener(on_press=on_press)
listener.start()

def cubic_bezier(p0, p1, p2, p3, t):
    u = 1 - t
    tt = t * t
    uu = u * u
    uuu = uu * u
    ttt = tt * t
    x = uuu * p0[0] + 3 * uu * t * p1[0] + 3 * u * tt * p2[0] + ttt * p3[0]
    y = uuu * p0[1] + 3 * uu * t * p1[1] + 3 * u * tt * p2[1] + ttt * p3[1]
    return (x, y)

def human_move_to(x, y, duration=2.0, steps=None):
    global stop_flag
    start = pyautogui.position()
    dx = x - start.x
    dy = y - start.y
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(12, int(dist / 5) + int(duration * 10))

    spread = max(30, dist * 0.3)
    p0 = (start.x, start.y)
    p3 = (x, y)
    p1 = (start.x + dx * 0.25 + random.uniform(-spread, spread),
          start.y + dy * 0.25 + random.uniform(-spread, spread))
    p2 = (start.x + dx * 0.75 + random.uniform(-spread, spread),
          start.y + dy * 0.75 + random.uniform(-spread, spread))

    base_sleep = duration / steps
    for i in range(1, steps + 1):
        if stop_flag:
            return
        t = i / steps
        nx, ny = cubic_bezier(p0, p1, p2, p3, t)
        jitter_x = random.uniform(-1.0, 1.0)
        jitter_y = random.uniform(-1.0, 1.0)
        pyautogui.moveTo(int(nx + jitter_x), int(ny + jitter_y), _pause=False)
        time.sleep(base_sleep * random.uniform(0.85, 1.25))

def random_small_move(max_offset=50, duration_range=(1.0, 4.0)):
    w, h = pyautogui.size()
    cur = pyautogui.position()
    tx = int(min(max(0, cur.x + random.uniform(-max_offset, max_offset)), w - 1))
    ty = int(min(max(0, cur.y + random.uniform(-max_offset, max_offset)), h - 1))
    dur = random.uniform(duration_range[0], duration_range[1])
    human_move_to(tx, ty, duration=dur)

def random_walk_periodic(long_move_chance=0.1):
    global stop_flag
    print("🖱️ Movendo o mouse de forma humana. Pressione ESC para parar.")
    while not stop_flag:
        for _ in range(random.randint(1, 5)):
            if stop_flag:
                break
            random_small_move(max_offset=random.uniform(8, 60),
                              duration_range=(0.6, 3.0))
            time.sleep(random.uniform(0.6, 3.2))
        if stop_flag:
            break

        if random.random() < long_move_chance:
            w, h = pyautogui.size()
            targets = [
                (w * 0.5 + random.uniform(-200, 200), h * 0.5 + random.uniform(-150, 150)),
                (w * 0.08 + random.uniform(-50, 50), h * 0.9 + random.uniform(-50, 50)),
                (w * 0.92 + random.uniform(-50, 50), h * 0.9 + random.uniform(-50, 50)),
                (w * 0.5 + random.uniform(-300, 300), h * 0.15 + random.uniform(-100, 100)),
            ]
            tx, ty = random.choice(targets)
            dur = random.uniform(2.0, 6.0)  # ✅ aqui estava o erro
            human_move_to(int(tx), int(ty), duration=dur)

        time.sleep(random.uniform(5.0, 30.0))

    print("✅ Execução encerrada.")

if __name__ == "__main__":
    random_walk_periodic(long_move_chance=0.18)
