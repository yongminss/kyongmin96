from pico2d import *
import game_framework
import game_world
import random
# 백그라운드 및 UI
from stage import Stage
from ground import Ground
from hp import HP
import score
# 캐릭터
from cookie import Cookie
# 오브젝트
from jelly import Jelly
from potion import Potion
from jtrap import jTrap
from djtrap import djTrap
from strap import sTrap
# 점수판
import Score_state

def handle_events():
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
             game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        # 체력 회복 (시연용)
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_0):
            hp.HP_count += 500
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

    global stage, ground, hp, cookie, jelly, potion, jtrap, djtrap, strap
    global scoreLabel, Label
    global jelly_sound, item_sound, collide_sound

    stage = Stage()         # 스테이지
    ground = Ground()       # 바닥
    hp = HP()               # 체력
    cookie = Cookie()       # 캐릭터

    game_world.add_object(stage, game_world.layer_bg)
    game_world.add_object(ground, game_world.layer_bg)
    game_world.add_object(hp, game_world.layer_bg)
    game_world.add_object(cookie, game_world.layer_player)

    # 점수
    label = score.Label("Score: ", 50, get_canvas_height() - 50, 45, 0)
    label.color = (255, 255, 255)
    score.labels.append(label)
    scoreLabel = label

    # 사운드
    jelly_sound = load_wav('jelly.wav')
    jelly_sound.set_volume(32)
    item_sound = load_wav('item.wav')
    item_sound.set_volume(32)
    collide_sound = load_wav('collide.wav')
    collide_sound.set_volume(50)



def draw():
    clear_canvas()
    game_world.draw()
    score.draw()
    update_canvas()

def update():
    create = random.randint(0, 100)
    TrapPattern = random.randint(0, 3)


    # 오브젝트 생성
    if cookie.itemcount > 0.01:
        jelly = Jelly()  # 젤리 (점수)
        game_world.add_object(jelly, game_world.layer_obstacle)
        # 0.01초마다 5% 확률로 포션 생성
        if create < 5:
            potion = Potion()
            game_world.add_object(potion, game_world.layer_obstacle)
        cookie.itemcount = 0
 
    # 함정의 경우
    if cookie.count >= 1.0:
        if TrapPattern == 0:
            jtrap = jTrap()  # 1단 점프 함정
            game_world.add_object(jtrap, game_world.layer_obstacle)
            cookie.count = 0
        elif TrapPattern == 1:
            djtrap = djTrap()  # 2단 점프 함정
            game_world.add_object(djtrap, game_world.layer_obstacle)
            cookie.count = 0
        elif TrapPattern == 2:
            strap = sTrap()  # 슬라이드 함정
            game_world.add_object(strap, game_world.layer_obstacle)
            cookie.count = 0

    # 게임월드 업데이트
    game_world.update()
    # 충돌처리
    for obj in game_world.all_objects():
        if isinstance(obj, Jelly) and hp.HP_count >= 0:
            if collides(cookie, obj):
                cookie.score += 5
                jelly_sound.play()
                game_world.remove_object(obj)
        if isinstance(obj, Potion):
            if collides(cookie, obj) and hp.HP_count >= 0:
                hp.HP_count += 30
                item_sound.play()
                game_world.remove_object(obj)
        # 함정
        if isinstance(obj, jTrap):
            if collides(cookie, obj) and hp.HP_count >= 0:
                game_world.remove_object(obj)
                collide_sound.play()
                cookie.fps = 0
                cookie.state = cookie.COLLIDE
                hp.HP_count -= 50
        if isinstance(obj, djTrap):
            if collides(cookie, obj) and hp.HP_count >= 0:
                game_world.remove_object(obj)
                collide_sound.play()
                cookie.fps = 0
                cookie.state = cookie.COLLIDE
                hp.HP_count -= 50
        if isinstance(obj, sTrap):
            if collides(cookie, obj) and hp.HP_count >= 0:
                game_world.remove_object(obj)
                collide_sound.play()
                cookie.fps = 0
                cookie.state = cookie.COLLIDE
                hp.HP_count -= 50

        update_score()


        if hp.HP_count <= 0:
            cookie.x -= 10 * game_framework.frame_time
            if cookie.x <= -500:
                game_framework.change_state(Score_state)


def update_score():
    global scoreLabel
    str = "Score: {:0.0f}".format(cookie.score)
    scoreLabel.text = str

def puase():
    pass

def exit():
    game_world.clear()
    Score_state.scoretemp = cookie.score



if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
