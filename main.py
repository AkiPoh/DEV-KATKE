import pygame
import json
import characters

with open("defaults_storage.json") as defaults_storage_json_file:
    defaults_storage_json_data = json.load(defaults_storage_json_file)
character_bitmaps = defaults_storage_json_data["character_bitmaps"]

character_bitmap_number_sign = character_bitmaps["number_sign"]
character_bitmap_space = character_bitmaps["space"]
character_bitmap_number_sign_inverted = characters.invert_boolean_bitmap(
    character_bitmap_number_sign
)

grid_bitmap_0d = character_bitmap_number_sign
grid_bitmap_1d = [
    character_bitmap_number_sign,
    character_bitmap_space,
    character_bitmap_number_sign,
]
grid_bitmap_2d = [
    [
        character_bitmap_number_sign,
        character_bitmap_space,
        character_bitmap_number_sign,
    ],
    [character_bitmap_space, character_bitmap_number_sign, character_bitmap_space],
    [
        character_bitmap_number_sign,
        character_bitmap_space,
        character_bitmap_number_sign,
    ],
]

spacing_between_characters_horizontal = 4  # in pixels
spacing_between_characters_vertical = 6  # in pixels

pygame.init()
screen_surface = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
running = True

print(screen_surface.get_width())
print(screen_surface.get_height())

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
