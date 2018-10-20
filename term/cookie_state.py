from pico2d import *
import game_framework

class Cookie:
    RUN, JUMP, SLIDE = 0, 1, 2
    
    def __init__(self):
        self.cookie = load_image('../term/cookierun_image/Cookie_Run_State.png')
        self.state = self.RUN   # 쿠키의 상태
        self.x = 200    # 쿠키 x좌표
        self.y = 200    # 쿠키 y좌표
        self.frame = 0

    def draw(self):
        self.cookie.clip_draw(self.frame * 120, 382 - 135, 120, 135, self.x, self.y)
        #self.cookie.clip_draw(0, 382 - 135 - 165, 140, 165, self.x, self.y)
        #self.cookie.clip_draw(0, 382 - 135 - 165 - 80, 170, 80, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 3
        
    def handle_events(self, e):
        pass
        

def handle_events():
    global state
        
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
             game_framework.quit()
        else:
            cookie.handle_events(e)
                    

def enter():
    global cookie

    cookie = Cookie()


def draw():
    clear_canvas()
    cookie.draw()
    update_canvas()

def update():
    cookie.update()
    delay(0.1)

def exit():
    pass

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
