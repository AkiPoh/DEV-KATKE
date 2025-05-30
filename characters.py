# CHARACTER BITMAP EXAMPLE
# INSTRUCTIONS: "False" means that the position is "transparent",
# "True" means  that the position is "filled"
#
# character_bitmap_number_sign = [
#     [False, True, False, True, False],
#     [True, True, True, True, True],
#     [False, True, False, True, False],
#     [True, True, True, True, True],
#     [False, True, False, True, False],
# ]


def render_character_bitmap(
    screen_surface,
    character_bitmap,
    begin_position_horizontal,
    begin_position_vertical,
):
    character_bitmap_height = len(character_bitmap)
    character_bitmap_width = len(character_bitmap[0])

    filled_pixel_color = (0, 0, 0)  # COLOR: "black"

    for character_bitmap_vertical_position in range(character_bitmap_height):
        for character_bitmap_horizontal_position in range(character_bitmap_width):
            bitmap_position_should_be_filled = character_bitmap[
                character_bitmap_vertical_position
            ][character_bitmap_horizontal_position]  # Either "True" or "False"

            if bitmap_position_should_be_filled:
                filled_screen_surface_position_horizontal = (
                    begin_position_horizontal + character_bitmap_horizontal_position
                )
                filled_screen_surface_position_vertical = (
                    begin_position_vertical + character_bitmap_vertical_position
                )
                screen_surface.set_at(
                    (
                        filled_screen_surface_position_horizontal,
                        filled_screen_surface_position_vertical,
                    ),
                    filled_pixel_color,
                )


# ROW BITMAP EXAMPLE
# INSTRUCTIONS: True means render character, False means empty space
# row_bitmap = [True, False, True, True]


def render_character_row_bitmap(
    screen_surface,
    character_bitmap,
    row_bitmap,
    spacing_between_characters,
    begin_position_horizontal,
    begin_position_vertical,
):
    character_bitmap_width = len(character_bitmap[0])

    current_character_begin_position_horizontal = begin_position_horizontal

    for should_render_character in row_bitmap:
        if should_render_character:
            render_character_bitmap(
                screen_surface,
                character_bitmap,
                current_character_begin_position_horizontal,
                begin_position_vertical,
            )
        current_character_begin_position_horizontal += (
            character_bitmap_width + spacing_between_characters
        )


# GRID BITMAP EXAMPLE
# INSTRUCTIONS: True means render character, False means empty space
# grid_bitmap = [
#     [True, False, True],
#     [False, True, False],
#     [True, False, True]
# ]


def render_character_grid_bitmap(
    screen_surface,
    character_bitmap,
    grid_bitmap,
    spacing_between_characters_horizontal,
    spacing_between_characters_vertical,
    begin_position_horizontal,
    begin_position_vertical,
):
    character_bitmap_height = len(character_bitmap)

    current_row_begin_position_vertical = begin_position_vertical

    for row_bitmap in grid_bitmap:
        render_character_row_bitmap(
            screen_surface,
            character_bitmap,
            row_bitmap,
            spacing_between_characters_horizontal,
            begin_position_horizontal,
            current_row_begin_position_vertical,
        )
        current_row_begin_position_vertical += (
            character_bitmap_height + spacing_between_characters_vertical
        )


# "boolean_bitmap" can also be zero dimensional (just a simple "True" or "False")
# Recursive function
def invert_boolean_bitmap(boolean_bitmap):
    if isinstance(boolean_bitmap, bool):  # handles if 0D bitmap
        return not boolean_bitmap  # inverts boolean
    elif not isinstance(boolean_bitmap, list):
        raise TypeError("'invert_boolean_bitmap' did not like your input")
    else:
        inverted_boolean_bitmap = []
        for current_boolean_bitmap in boolean_bitmap:
            inverted_boolean_bitmap.append(invert_boolean_bitmap(current_boolean_bitmap))
        return inverted_boolean_bitmap
