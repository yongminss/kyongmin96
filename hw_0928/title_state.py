from pico2d import *
import game_framework
import boys_state

class Title:
    def __init__(self):
        self.image = load_image('../image/title.png')
    def draw(self):
        self.image.draw(400, 300)

def handle_events():
    global title
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.pop_state()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
               game_framework.pop_state()
            elif e.key == SDLK_SPACE:
               game_framework.push_state(boys_state)

def enter():

    global title

    open_canvas()
    title = Title()

def draw():

    global title

    clear_canvas()
    title.draw()
    update_canvas()

def update():
    pass

def resume():
    pass

def exit():
    close_canvas()
