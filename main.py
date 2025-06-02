import json
def GET_DEFAULTS():
    global DEFAULTS_PATH
    with open(DEFAULTS_PATH) as DEFAULTS_FILE:
        DEFAULTS = json.load(DEFAULTS_FILE)
    return DEFAULTS


import pygame
def INIT_PYGAME():
    pygame.init()

def GET_SURFACE():
    global WIDTH_PIXELS
    global HEIGHT_PIXELS
    return pygame.display.set_mode((WIDTH_PIXELS, HEIGHT_PIXELS))

def CREATE_CLOCK():
    return pygame.time.Clock()

def CHECK_EVENT(EVENT_TYPE):
    for EVENT in pygame.event.get():
        if EVENT.type == EVENT_TYPE:
            return True
    return False

def FILL(COLOR):
    global SURFACE
    SURFACE.fill(COLOR)

def UPDATE_DISPLAY():
    pygame.display.flip()

def LIMIT_FPS():
    global CLOCK
    CLOCK.tick(60)  # 60 FPS LIMITED

def QUIT_PYGAME():
    pygame.quit()


DEFAULTS_PATH = "defaults_storage.json"
DEFAULTS = GET_DEFAULTS()

INIT_PYGAME()
WIDTH_PIXELS = 500
HEIGHT_PIXELS = 300
SURFACE = GET_SURFACE()
CLOCK = CREATE_CLOCK()
WHITE = (255, 255, 255)
QUIT_EVENT = pygame.QUIT

RUNNING = True
while RUNNING:
    if CHECK_EVENT(QUIT_EVENT):
        RUNNING = False
    FILL(WHITE)
    UPDATE_DISPLAY()
    LIMIT_FPS()
QUIT_PYGAME()
