from pico2d import *
import game_framework
import title_state

class Logo:
    def __init__(self):
        self.image = load_image('../image/kpu_credit.png')
        self.time = 0
    def draw(self):
        self.image.draw(400, 300)


def handle_events():
    global logo

    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()

def enter():

    global logo

    open_canvas()
    logo = Logo()


def draw():

    global logo

    clear_canvas()
    logo.draw()
    update_canvas()

def update():
    logo.time += 0.01
    if logo.time >= 1:
        game_framework.change_state(title_state)


def exit():
    close_canvas()
