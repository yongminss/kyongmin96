from pico2d import *
import game_framework
import game_world
from cookie import Cookie
from stage import Stage
from ground import Ground
from hp import HP
from potion import Potion
from jelly import Jelly
from trap1 import jTrap
from trap2 import sTrap

def handle_events():
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
             game_framework.quit()
        else:
            cookie.handle_events(e)

def collides(a, b):
    if not hasattr(a, 'get_bb'): return False
    if not hasattr(b, 'get_bb'): return False

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def enter():

    global stage, ground, hp, cookie, potion, jelly, jtrap, strap

    stage = Stage()         # 스테이지
    ground = Ground()       # 바닥
    hp = HP()               # 체력
    cookie = Cookie()       # 캐릭터
    potion = Potion()       # HP포션
    jelly = Jelly()         # 젤리
    jtrap = jTrap()         # 점프 함정
    strap = sTrap()         # 슬라이드 함정
    
    game_world.add_object(stage, game_world.layer_bg)
    game_world.add_object(ground, game_world.layer_bg)
    game_world.add_object(hp, game_world.layer_bg)
    game_world.add_object(cookie, game_world.layer_player)
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
    for jelly in game_world.objects_at_layer(game_world.layer_obstacle):
        if collides(cookie, jelly):
            print("충돌: ", jelly)
            game_world.remove_object(jelly)
    delay(0.06)

def exit():
    game_world.clear()

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
