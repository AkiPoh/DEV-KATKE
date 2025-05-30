import pygame

import json

import characters

with open("storage.json") as storage_json_file:
    storage_json_data = json.load(storage_json_file)

character_bitmap_number_sign = storage_json_data["character_bitmap_number_sign"]

# 5 total rendered characters
row_bitmap_test = [True, False, True, True, False, True, False, False, True]
character_row_spacing = 4  # in pixels

pygame.init()

screen_surface = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_surface.fill((255, 255, 255))  # COLOR: "white"

    characters.render_character_bitmap(
        screen_surface, character_bitmap_number_sign, 100, 100
    )

    characters.render_character_row_bitmap(
        screen_surface,
        character_bitmap_number_sign,
        row_bitmap_test,
        character_row_spacing,
        150,
        150,
    )

    pygame.display.flip()  # Update the display
    clock.tick(60)  # 60 FPS

pygame.quit()
