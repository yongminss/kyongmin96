from pico2d import *
import game_framework
import game_world
import random
# 백그라운드 및 UI
from stage import Stage
from ground import Ground
from hp import HP
# 캐릭터
from cookie import Cookie
# 오브젝트
from jelly import Jelly
from potion import Potion
from jtrap import jTrap
from djtrap import djTrap
from strap import sTrap

def handle_events():
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
             game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
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

    global stage, ground, cookie, hp, jelly, potion, jtrap, djtrap, strap

    stage = Stage()         # 스테이지
    ground = Ground()       # 바닥
    hp = HP()               # 체력
    cookie = Cookie()       # 캐릭터

    game_world.add_object(stage, game_world.layer_bg)
    game_world.add_object(ground, game_world.layer_bg)
    game_world.add_object(hp, game_world.layer_bg)
    game_world.add_object(cookie, game_world.layer_player)

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def update():
    
    jelly = Jelly()     # 젤리 (점수)
    potion = Potion()
    
    Jcreate = random.randint(0, 100)
    Pcreate = random.randint(0, 100)
    
    # 오브젝트 생성
    if Jcreate <= 30:
        game_world.add_object(jelly, game_world.layer_obstacle)
    if Pcreate <= 1:
        game_world.add_object(potion, game_world.layer_obstacle)
    # 게임월드 업데이트
    game_world.update()
    # 충돌처리
    for obj in game_world.all_objects():
        if isinstance(obj, Jelly):
            if collides(cookie, obj):
                game_world.remove_object(obj)
        if isinstance(obj, Potion):
            if collides(cookie, obj):
                hp.HP_count += 50
                game_world.remove_object(obj)
    

def exit():
    game_world.clear()

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
