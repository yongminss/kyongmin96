from pico2d import *
import game_framework

class Cookie:
    def __init__(self):
        self.cookierun_1 = load_image('../term/cookierun_image/cookie_run_1.png')
        self.cookierun_2 = load_image('../term/cookierun_image/cookie_run_2.png')
        self.x = 200
        self.y = 200
        self.state = 0

    def draw(self):
        if self.state == 1:
            self.cookierun_1.draw(self.x, self.y)
        elif self.state == 2:
            self.cookierun_2.draw(self.x, self.y)

    def update(self):
        self.state += 1
        if self.state > 2:
            self.state = 1


def handle_events():
    events = get_events()

def enter():
    global cookie
    
    cookie = Cookie()


def draw():
    clear_canvas()
    cookie.draw()
    update_canvas()

def update():
    cookie.update()
    delay(0.1)

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
