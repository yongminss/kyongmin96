from pico2d import *

def handle_events(speed):
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            if x <= event.x:
                x += speed
                if x >= event.x:
                    x = event.x
            elif x >= event.x:
                x -= speed
                if x <= event.x:
                    x = event.x
            if y <= 600 - 1 - event.y:
                y += speed
                if y >= event.y:
                    y = 600 - 1 - event.y
            elif y >= 600 - 1 - event.y:
                y -= speed
                if y <= event.y:
                    y = 600 - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = false
    
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')


x = 0
y = 90
frame = 0

while (1):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    handle_events(10)
    delay(0.01)
    get_events()
    
close_canvas()
