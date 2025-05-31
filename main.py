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

def EVENT_QUIT():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

def FILL(COLOR):
    global SURFACE
    SURFACE.fill(WHITE)

def UPDATE_DISPLAY():
    pygame.display.flip()

def TICK_CLOCK():
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

RUNNING = True
while RUNNING:
    EVENT_QUIT()
    FILL(WHITE)
    UPDATE_DISPLAY()
    TICK_CLOCK()
QUIT_PYGAME()
