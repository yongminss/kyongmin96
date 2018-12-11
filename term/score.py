import os.path
from pico2d import *

buttons = []
labels = []

_FONT_FILES = [ \
    "../term/cookierun_image/origa_m_r.ttf" \
]
_fonts = {}

def getFont(idx, size):
    global _fonts
    key = str(idx) + '_' + str(size)
    if key in _fonts:
        print("Reuse font:", key)
        return _fonts[key]
    file = _FONT_FILES[idx]
    _fonts[key] = load_font(file, size)
    print("Font created for:", file, size)
    return _fonts[key]

def loadIfExists(file):
    if os.path.isfile(file):
        return load_image(file)
    return None

class Label:
    def __init__(self, text, x, y, size = 20, fontIndex = 0):
        self.text = text
        self.x, self.y = x, y
        self.color = (0, 0, 0)
        self.font = getFont(fontIndex, size)
    def draw(self):
        self.font.draw(self.x, self.y, self.text, self.color)

def update():
    pass

def draw():
    for b in buttons:
        b.draw()
    for l in labels:
        l.draw()
