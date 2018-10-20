from pico2d import *
import game_framework

class Cookie:
    RUN, JUMP, DEAD = 0, 1, 2
    
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
                
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
