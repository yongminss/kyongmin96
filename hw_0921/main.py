from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.frame = random.randint(0, 7)
        self.speed = random.uniform(1.0, 3.0)
        self.image = load_image('run_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed

def handle_events():

    global running
    global x, y

    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            tx = e.x
            ty = 600 - e.y

def character_move():
    if self.x > tx:
        self.x -= speed
        if self.x <= tx:
            self.x = tx
    elif self.x < tx:
        self.x += speed
        if self.x >= tx:
            self.x = tx
    elif self.y > ty:
        self.y -= speed
        if self.y <= ty:
            self.y = ty
    elif self.y < ty:
        self.y += speed
        if self.y >= ty:
            self.y = ty
            
open_canvas()

g = Grass()
b = Boy()
boys = [ Boy() for i in range(20)]

running = True

while running:
    handle_events()
    
    for b in boys:
        b.update()

    clear_canvas()

    g.draw()
    for b in boys:
        b.draw()
    character_move()
    update_canvas()

    delay(0.01)
    get_events()

close_canvas()
