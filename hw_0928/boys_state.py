from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')
        
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        tx, ty = self.x, self.y
        self.frame = random.randint(0, 7)
        self.speed = random.uniform(5.0, 10.0)
        self.image = load_image('../image/run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8

    def move(self):
        if self.x < tx:
            self.x += self.speed
            if self.x >= tx: self.x = tx
        elif self.x > tx:
            self.x -= self.speed
            if self.x <= tx: self.x = tx
        if self.y < ty:
            self.y += self.speed
            if self.y >= ty: self.y = ty
        elif self.y > ty:
            self.y -= self.speed
            if self.y <= ty: self.y = ty

    def handle_events(self):

        global running
        global tx, ty

        events = get_events()

        for e in events:
            if e.type == SDL_QUIT:
                if e.key == SDLK_ESCAPE:
                    running = False
            elif e.type == SDL_MOUSEMOTION:
                tx = e.x
                ty = 600 - e.y

tx, ty = 800 // 2, 600 // 2

open_canvas()

g = Grass()
b = Boy()
boys = [ Boy() for i in range(20)]


running = True

while running:
    for b in boys:
        b.update()

    clear_canvas()

    g.draw()
    b.handle_events()
    for b in boys:
        b.draw()
        b.move()
    
    update_canvas()

    delay(0.01)
    get_events()

close_canvas()

