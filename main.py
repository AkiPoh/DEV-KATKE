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



cursors_color_inverted_status = False
cursor_color_inverted_since_last_change_time_ms = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_surface.fill((255, 255, 255))  # COLOR: "white"

    # Test original single character rendering
    characters.render_character_bitmap(
        screen_surface, character_bitmap_number_sign_inverted, 50, 50
    )

    # Test 0D grid (single character)
    characters.render_character_grid_bitmap(
        screen_surface,
        grid_bitmap_0d,
        spacing_between_characters_horizontal,
        spacing_between_characters_vertical,
        50,
        100,
    )

    # Test 1D grid (single row)
    characters.render_character_grid_bitmap(
        screen_surface,
        grid_bitmap_1d,
        spacing_between_characters_horizontal,
        spacing_between_characters_vertical,
        50,
        150,
    )

    # Test 2D grid (multiple rows)
    characters.render_character_grid_bitmap(
        screen_surface,
        grid_bitmap_2d,
        spacing_between_characters_horizontal,
        spacing_between_characters_vertical,
        50,
        200,
    )

    pygame.display.flip()  # update the display
    clock.tick(60)  # limits FPS to 60

pygame.quit()
