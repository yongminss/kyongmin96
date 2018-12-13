from pico2d import *
import game_framework
import score
from cookie import Cookie

class ScoreBoard:
    def __init__(self):
        self.image = load_image('../term/cookierun_image/scoreBoard.png')

    def draw(self):
        self.image.draw(400, 300)

def handle_events():

    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                tx, ty = e.x, 600 - e.y
                if tx >= 320 and tx <= 520 and ty >= 25 and ty <= 110:
                    game_framework.quit()

def enter():
    global Board, scoreLabel, cookie, scoretemp
    Board = ScoreBoard()
    cookie = Cookie()

    # 스코어
    label = score.Label("Score: ", 60, 300, 80, 0)
    label.color = (0, 0, 0)
    score.labels.append(label)
    scoreLabel = label
    str = "Score: {:0.0f}".format(scoretemp)
    scoreLabel.text = str

def draw():
    clear_canvas()
    Board.draw()
    score.draw()
    update_canvas()

def update():
    pass

def exit():
    pass