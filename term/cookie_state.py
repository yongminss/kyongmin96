from pico2d import *
import game_framework

class Cookie:
    def __init__(self):
        self.cookie = load_image('../term/cookierun_image/cookie_run_1.png')
        self.x = 200
        self.y = 200

    def draw(self):
        self.cookie.draw(x,y)


def draw():
    clear_canvas()
    Cookie.draw()
    update_cavnas()
    delay(0.01)
