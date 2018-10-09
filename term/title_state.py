from pico2d import *
import game_framework

class Title:
    def __init__(self):
        self.image = load_image('../term/cookierun_image/cookierun_title.png')
    def draw(self):
        self.image.draw(400,300)

def handle_events():

    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
            
def enter():

    global title

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
    pass
