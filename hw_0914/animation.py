from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')
x = 0
y = 90
frame = 0
rect_move = 1
circle_move = 0
d = 0
angle = 0
count = 0
r = 320

while 1:
    while (rect_move == 1):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

        if (d == 0):
            x += 10
            if (x >= 800 - 20):
                d = 1

        elif (d == 1):
            if (count == 0):
                y += 10
                if (y >= 600 - 20):
                    d = 2
            elif (count == 1):
                y += 10
                if (y >= 300):
                    rect_move = 0
                    circle_move = 1

        elif (d == 2):
            x -= 10
            if (x <= 0 + 20):
                d = 3

        elif (d == 3):
            y -= 10
            if (y <= 90):
                d = 0
                count += 1

        delay(0.01)
        get_events()

    while (circle_move == 1):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

        x = 400 + r * math.cos(angle)
        y = 300 + r * math.sin(angle)
        angle = angle + 0.1

        if (angle > 6.5):
            rect_move = 1
            circle_move = 0
            count = 0
            d = 1
            angle = 0

        delay(0.01)
        get_events()

        
