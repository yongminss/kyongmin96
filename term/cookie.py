from pico2d import *
import game_world
import time

RUN, JUMP, DOUBLE_JUMP, SLIDE = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): JUMP,
    (SDL_KEYDOWN, SDLK_DOWN): SLIDE,
}

class RunState:
    @staticmethod
    def enter(cookie):
        pass
    
    @staticmethod
    def exit(cookie):
        pass

    @staticmethod
    def update(cookie):
        pass

    @staticmethod
    def draw(cookie):
        pass


class JumpState:
    @staticmethod
    def enter(cookie):
        pass
    
    @staticmethod
    def exit(cookie):
        pass

    @staticmethod
    def update(cookie):
        pass

    @staticmethod
    def draw(cookie):
        pass

class SlideState:
    @staticmethod
    def enter(cookie):
        pass
    
    @staticmethod
    def exit(cookie):
        pass

    @staticmethod
    def update(cookie):
        pass

    @staticmethod
    def draw(cookie):
        pass


class Cookie:
    image = None

    def __init__(self):
        if Cookie.image == None:
            Cookie.image = load_image('../term/cookierun_image/Cookie_Run_State.png')
            self.state = self.RUN
