from pico2d import *
import game_framework
import game_world
from stage import Stage
from ground import Ground
from hp import HP
from potion import Potion
from jelly import Jelly
from trap1 import jTrap
from trap2 import sTrap

class Cookie:
    RUN, JUMP, DOUBLE_JUMP, SLIDE = 0, 1, 2, 3
    
    def __init__(self):
        self.cookie = load_image('../term/cookierun_image/Cookie_Run_State.png')
        self.state = self.RUN   # 쿠키의 상태
        self.x = 250    # 쿠키 x좌표
        self.y = 215    # 쿠키 y좌표
        self.frame = 0

    def draw(self):
        if self.state == self.RUN:  # 달리기
            self.cookie.clip_draw(self.frame * 120, 382 - 135, 120, 135,
                                  self.x, self.y)
        elif self.state == self.JUMP:   # 1단 점프
            self.cookie.clip_draw(0, 382 - 135 - 165, 140, 165, self.x, self.y)
        elif self.state == self.DOUBLE_JUMP:    # 2단 점프
            self.cookie.clip_draw(self.frame * 140, 382 - 135 - 165, 140, 165,
                                  self.x, self.y)
        elif self.state == self.SLIDE:  # 슬라이딩
            self.cookie.clip_draw(self.frame * 170, 382 - 135 - 165 - 80, 170, 80,
                                  self.x, self.y)

    def update(self):
        if self.state == self.RUN:
            self.frame = (self.frame + 1) % 3
        elif self.state == self.JUMP:
            self.frame = (self.frame + 1) % 1
        elif self.state == self.DOUBLE_JUMP:
            self.frame = (self.frame + 1) % 6
        elif self.state == self.SLIDE:
            self.frame = (self.frame + 1) % 2
        
    def handle_events(self, e):
        pass

def handle_events():
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
             game_framework.quit()

def enter():

    global stage, ground, hp, potion, jelly

    stage = Stage()
    ground = Ground()
    hp = HP()
    potion = Potion()
    jelly = Jelly()
    jtrap = jTrap()
    strap = sTrap()
    
    game_world.add_object(stage, game_world.layer_bg)
    game_world.add_object(ground, game_world.layer_bg)
    game_world.add_object(hp, game_world.layer_bg)
    game_world.add_object(potion, game_world.layer_obstacle)
    game_world.add_object(jelly, game_world.layer_obstacle)
    game_world.add_object(jtrap, game_world.layer_obstacle)
    game_world.add_object(strap, game_world.layer_obstacle)
    

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def update():
    game_world.update()
    delay(0.06)

def exit():
    game_world.clear()

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
