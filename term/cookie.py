from pico2d import *
import game_framework
import config

class Cookie:
    Image = None
    RUN, JUMP, DOUBLE_JUMP, SLIDE, COLLIDE = 0, 1, 2, 3, 4
    
    def __init__(self):
        if Cookie.Image == None:
            self.cookie = load_image('../term/cookierun_image/Cookie_Run_State.png')
            self.cookieCollide = load_image('../term/cookierun_image/cookie_run_collid.png')
        self.state = self.RUN   # 쿠키의 상태
        self.x = 250    # 쿠키 x좌표
        self.y = 265    # 쿠키 y좌표
        self.fps = 0
        self.frame = 0
        self.Jump_count = 0
        self.spaceClickCount = 0
        self.spaceClick = False
        # 함정 등장 카운트
        self.count = 0
        self.difficulty = 0
        # 점수
        self.score = 0
        # 사운드
        global jump_sound, slide_sound

        jump_sound = load_wav('jump.wav')
        jump_sound.set_volume(32)
        slide_sound = load_wav('slide.wav')
        slide_sound.set_volume(32)

    def get_bb(self):
        if self.state == self.RUN:
            return self.x - 30, self.y - 65, self.x + 55, self.y + 65
        elif self.state == self.JUMP:
            return self.x - 30, self.y - 40, self.x + 55, self.y + 70
        elif self.state == self.DOUBLE_JUMP:
            return self.x - 30, self.y - 40, self.x + 55, self.y + 70
        elif self.state == self.SLIDE:
            return self.x - 40, self.y - 30, self.x + 65, self.y + 40
        elif self.state == self.COLLIDE:
            return self.x - 40, self.y - 30, self.x + 65, self.y + 40

    def draw(self):
        if self.state == self.RUN:              # 달리기
            self.cookie.clip_draw(self.frame * 120, 382 - 135, 120, 135,
                                  self.x, self.y)
        elif self.state == self.JUMP:           # 1단 점프
            self.cookie.clip_draw(0, 382 - 135 - 165, 140, 165, self.x, self.y)
        elif self.state == self.DOUBLE_JUMP:    # 2단 점프
            self.cookie.clip_draw(self.frame * 140, 382 - 135 - 165, 140, 165,
                                  self.x, self.y)
        elif self.state == self.SLIDE:          # 슬라이딩
            self.cookie.clip_draw(self.frame * 170, 382 - 135 - 165 - 80, 170, 80,
                                  self.x, self.y)
        elif self.state == self.COLLIDE:
            self.cookieCollide.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.fps += 10 * game_framework.frame_time
        if self.state == self.RUN:
            if self.fps >= 3:
                self.fps = 0
        elif self.state == self.DOUBLE_JUMP:
            if self.fps >= 6:
                self.fps = 0
        elif self.state == self.SLIDE:
            if self.fps >= 2:
                self.fps = 0
        elif self.state == self.COLLIDE:
            if self.fps >= 3:
                self.y = 265
                self.spaceClickCount = 0
                self.spaceClick = False
                self.fps = 0
                self.state = self.RUN

        # 쿠키가 달릴 때 (기본 State)
        if self.state == self.RUN:
            for i in range(0, 3):
                if i <= self.fps and self.fps <= i + 1:
                    self.frame = i
        # 쿠키가 점프할 때 (1단 점프)
        elif self.state == self.JUMP:
            self.frame = 0
        # 쿠키가 점프를 한번 더 할 때 (2단 점프)
        elif self.state == self.DOUBLE_JUMP:
            for i in range(0, 6):
                if i <= self.fps and self.fps <= i + 1:
                    self.frame = i
        # 쿠키가 슬라이딩을 할 때 (슬라이드)
        elif self.state == self.SLIDE:
            if 0 <= self.fps and self.fps <= 1:
                self.frame = 0
            elif 1 <= self.fps and self.fps <= 2:
                self.frame = 1

        # 점프 이벤트를 수행 (SPACE바 눌렸을 때)
        if self.state == self.JUMP or self.state == self.DOUBLE_JUMP:
            self.spaceClick = True
            self.y += self.Jump_count * (50 * game_framework.frame_time)
            self.Jump_count -= 60 * game_framework.frame_time
            # 땅에 닿았을 때 (초기화)
            if self.y <= 265:
                self.y = 265
                self.Jump_count = 0
                self.state = self.RUN
                self.spaceClickCount = 0
                self.spaceClick = False
                self.frame = 0

        # 함정 등장 카운트
        self.count += (0.5 + self.difficulty) * game_framework.frame_time
        self.difficulty += 0.01 * game_framework.frame_time
        if self.difficulty >= 0.85:
            self.difficulty = 0.85

    def handle_events(self, e):
        # 슬라이딩
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state == self.RUN:
                self.state = self.SLIDE
                slide_sound.play()
                self.y = 230
        elif (e.type, e.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state == self.SLIDE:
                self.frame = 0
                self.state = self.RUN
                self.y = 265
        # 점프
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.spaceClickCount < 2:
                self.state = self.JUMP
                jump_sound.play()
                self.Jump_count = 13
                self.spaceClickCount += 1
                if self.spaceClick == True:
                    self.state = self.DOUBLE_JUMP
                    jump_sound.play()
                    self.Jump_count += 6

