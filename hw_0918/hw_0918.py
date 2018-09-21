from pico2d import *

def handle_events():
    global running
    global x, y
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            if x <= e.x:
                x += speed
                if x >= e.x:
                    x = e.x
            elif x >= e.x:
                x -= speed
                if x <= e.x:
                    x = e.x
            if y <= 600 - e.y:
                y += speed
                if y >= 600 - e.y:
                    y = 600 - e.y
            elif y >= 600 - e.y:
                y -= speed
                if y <= 600 - e.y:
                    y = 600 - e.y
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')


x = 0
y = 90
frame = 0
speed = 10
running = True

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    handle_events()
    delay(0.01)
    get_events()
    
close_canvas()
