from pico2d import *
import game_framework
import random
import json
from enum import Enum

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None
    wp = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
    
    def __init__(self):
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.state = self.RIGHT_STAND
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.waypoints = []
        if Boy.image == None:
            Boy.image = load_image('../image/animation_sheet.png')
        if Boy.wp == None:
            Boy.wp = load_image('../image/wp.png')
    def draw(self):
        for wp in self.waypoints:
            self.wp.draw(wp[0], wp[1])
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100,
                             self.x, self.y)
    def update(self):
        if self.state == self.LEFT_RUN:
            self.frame = (self.frame + 1) % 8
        elif self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1) % 8
        elif self.state == self.LEFT_STAND:
            self.frame = (self.frame + 1) % 8
        elif self.state == self.RIGHT_STAND:
            self.frame = (self.frame + 1) % 8
        if len(self.waypoints) > 0:
            tx, ty = self.waypoints[0]
            dx, dy = tx - self.x, ty - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist
                if dx > 0:
                    self.state = self.RIGHT_RUN
                elif dx < 0:
                    self.state = self.LEFT_RUN

                if dx < 0 and self.x < tx: self.x = tx
                if dx > 0 and self.x > tx: self.x = tx
                if dy < 0 and self.y < ty: self.y = ty
                if dy > 0 and self.y > ty: self.y = ty

                if (tx, ty) == (self.x, self.y):
                    del self.waypoints[0]
                    if self.state == self.RIGHT_RUN:
                        self.state = self.RIGHT_STAND
                    elif self.state == self.LEFT_RUN:
                        self.state = self.LEFT_STAND

span = 50
def handle_events():
    global boys
    global span
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif e.key in range(SDLK_1, SDLK_9 + 1):
                span = 20 * (e.key - SDLK_0)

        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                tx, ty = e.x, 600 - e.y
                for b in boys:
                    bx = tx + random.randint(-span, span)
                    by = ty + random.randint(-span, span)
                    b.waypoints += [ (bx, by) ]
            else:
                for b in boys:
                    b.waypoints = []

def enter():
    global boys, grass

    boys = [ Boy() for i in range(10) ]
    grass = Grass()


# def main():
#     global running
#     enter()
#     while running:
#         handle_events()
#         print(running)
#         update()
#         draw()
#     exit()

def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw()
    update_canvas()

def update():
    global boys
    for b in boys:
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
