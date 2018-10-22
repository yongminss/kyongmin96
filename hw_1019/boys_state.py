from pico2d import *
import game_framework
import random
from enum import Enum

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    IDLE, RUN, SLEEP = 0, 1, 2
    LEFT, RIGHT = 0, 1
    
    def __init__(self):
        self.image = load_image('../image/animation_sheet.png')
        self.x = 100
        self.y = 200
        self.state = self.IDLE
        self.dir = self.RIGHT
        self.frame = 0
        self.waypoints = []

    def enter_IDLE(self):
        self.frame = 0
        
    def update_IDLE(self):
        if self.state == self.IDLE:
            self.frame = (self.frame + 1) % 8

    def draw_IDLE(self):
        if self.state == self.IDLE:
            if self.dir == self.RIGHT:
                self.image.clip_draw(self.frame * 100, 300, 100, 100,
                                     self.x, self.y)
            elif self.dir == self.LEFT:
                self.image.clip_draw(self.frame * 100, 200, 100, 100,
                                     self.x, self.y)

    def exit_IDLE(self):
        pass

    def enter_RUN(self):
        self.frame = 0

    def update_RUN(self):
        if self.state == self.RUN:
            self.frame = (self.frame + 1) % 8

        if len(self.waypoints) > 0:
            tx, ty = self.waypoints[0]
            dx, dy = tx - self.x, ty - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                self.x += 10 * dx / dist
                self.y += 10 * dy / dist

            if dx < 0 and self.x < tx: self.x = tx
            if dx > 0 and self.x > tx: self.x = tx
            if dy < 0 and self.y < ty: self.y = ty
            if dy > 0 and self.y > ty: self.y = ty

            if (tx, ty) == (self.x, self.y):
                del self.waypoints[0]

    def draw_RUN(self):
        if self.state == self.RUN:
            if self.dir == self.RIGHT:
                self.image.clip_draw(self.frame * 100, 100, 100, 100,
                                     self.x, self.y)
            elif self.dir == self.LEFT:
                self.image.clip_draw(self.frame * 100, 0, 100, 100,
                                     self.x, self.y)

    def exit_RUN(self):
        pass

    def handle_events(self, e):
        pass

    def enter():
        enter_IDLE()
        enter_RUN()
        
    def draw():
        draw_IDLE()
        draw_RUN()

    def update():
        draw_IDLE()
        draw_RUN()

    def exit():
        pass

def handle_events():
    global tx, ty
    
    events = get_events()
    
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
        elif e.type == SDL_MOUSEBUTTONDOWN:
                if e.button == SDL_BUTTON_LEFT:
                    for b in B:
                        tx, ty = e.x, 600 - e.y
                        bx, by = tx, ty
                        b.waypoints += [ (bx, by) ]
                else:
                    for b in B:
                        b.waypoints = []
        else:
            B.handle_event(e)


def enter():
    global B, G

    B = [ Boy() for i in range(1) ]
    G = Grass()

def draw():
    global grass, boys
    
    clear_canvas()
    G.draw()
    for b in B:
        b.draw()
    update_canvas()

def update():
    global boys

    for b in B:
        b.update()
    delay(0.01)

# fill here

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
