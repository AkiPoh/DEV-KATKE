import json
def GET_DEFAULTS():
    global DEFAULTS_PATH
    with open(DEFAULTS_PATH) as DEFAULTS_FILE:
        DEFAULTS = json.load(DEFAULTS_FILE)
    return DEFAULTS
DEFAULTS_PATH = "defaults_storage.json"
DEFAULTS = GET_DEFAULTS()

import pygame
def PYGAME_INIT():
    pygame.init()
PYGAME_INIT()

def GET_SURFACE():
    global WIDTH_PIXELS
    global HEIGHT_PIXELS
    return pygame.display.set_mode((WIDTH_PIXELS, HEIGHT_PIXELS))
WIDTH_PIXELS = 500
HEIGHT_PIXELS = 300
SURFACE = GET_SURFACE()

def CREATE_CLOCK():
    return pygame.time.Clock()
CLOCK = CREATE_CLOCK()



RUNNING = True
def EVENT_QUIT():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
while RUNNING:
    EVENT_QUIT()
    pygame.display.flip()  # update the display
    CLOCK.tick(60)  # limits FPS to 60

pygame.quit()
