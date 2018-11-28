from pico2d import *
import time
import game_world
from cookie import Cookie
from potion import Potion

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

class HP:
    MAX_HP = 500
    def __init__(self):
        global cookie, potion
        
        self.HP = load_image('../term/cookierun_image/HP.png')
        self.HP_count = 500
        self.x = 400
        self.y = 500
        cookie = Cookie()
        potion = Potion()

        game_world.add_object(potion, game_world.layer_obstacle)

    def draw(self):
        self.HP.clip_draw(0, 0, self.HP_count, 64, self.x, self.y)

    def update(self):
        self.HP_count -= 2
        # 체력 최대치
        if self.HP_count >= self.MAX_HP:
            self.HP_count = self.MAX_HP
        # 쿠키와 포션의 충돌 시
        for potion in game_world.objects_at_layer(game_world.layer_obstacle):
            if collides(cookie, potion):
                game_world.remove_object(potion)
                self.HP_count += 100
                
    def exit(self):
        pass
