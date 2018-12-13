from pico2d import *
import game_framework
import cookie_state
title_sound = None

class Title:
    def __init__(self):
        self.image = load_image('../term/cookierun_image/Title.png')
        self.button = load_image('../term/cookierun_image/GameStart_button.png')
        self.keyset = load_image('../term/cookierun_image/key.png')

    def draw(self):
        self.image.draw(400, 300)
        self.button.draw(400, 40)
        self.keyset.draw(175, 540)

def handle_events():

    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()
            elif e.key == SDLK_SPACE:
                game_framework.change_state(cookie_state)

        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                tx, ty = e.x, 600 - e.y
                if e.x >= 275 and e.x <= 275 + 250 and e.y >= 530 and e.y <= 590:
                    game_framework.change_state(cookie_state)
            
def enter():
    global title, title_sound

    title = Title()

    # 사운드
    title_sound = load_music('Title.mp3')
    title_sound.set_volume(32)
    title_sound.repeat_play()

def draw():

    global title

    clear_canvas()
    title.draw()
    update_canvas()

def update():
    pass

def resume():
    pass

def exit():
    pass
