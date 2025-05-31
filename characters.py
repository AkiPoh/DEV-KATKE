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


# GRID BITMAP EXAMPLES
# INSTRUCTIONS: Pass actual character bitmap arrays in 0D, 1D, or 2D format
#
# 0 DIMENSIONAL
# grid_bitmap = character_bitmap_number_sign
#
# 1 DIMENSIONAL
# grid_bitmap = [character_bitmap_number_sign, character_bitmap_space, character_bitmap_number_sign]
#
# 2 DIMENSIONAL
# grid_bitmap = [
#     [character_bitmap_number_sign, character_bitmap_space, character_bitmap_number_sign],
#     [character_bitmap_space, character_bitmap_number_sign, character_bitmap_space],
#     [character_bitmap_number_sign, character_bitmap_space, character_bitmap_number_sign]
# ]
def render_character_grid_bitmap(
    screen_surface,
    grid_bitmap,
    spacing_between_characters_horizontal,
    spacing_between_characters_vertical,
    begin_position_horizontal,
    begin_position_vertical,
):
    # If  0D bitmap, make into a 2D bitmap
    if isinstance(grid_bitmap[0][0], bool):
        grid_bitmap = [[grid_bitmap]]
    # If  1D bitmap, make into a 2D bitmap
    elif isinstance(grid_bitmap[0][0][0], bool):
        grid_bitmap = [grid_bitmap]
    # Check if 2D bitmap
    elif isinstance(grid_bitmap[0][0][0][0], bool):
        pass
    else:
        raise TypeError("render_character_grid_bitmap: Invalid grid_bitmap format")

    current_row_begin_position_vertical = begin_position_vertical

    for row_bitmap in grid_bitmap:
        if not row_bitmap:  # if empty
            raise ValueError(
                "render_character_grid_bitmap: Empty row found in grid_bitmap"
            )

        current_character_begin_position_horizontal = begin_position_horizontal

        for character_bitmap in row_bitmap:
            character_bitmap_width = len(character_bitmap[0])
            render_character_bitmap(
                screen_surface,
                character_bitmap,
                current_character_begin_position_horizontal,
                current_row_begin_position_vertical,
            )
            current_character_begin_position_horizontal += (
                character_bitmap_width + spacing_between_characters_horizontal
            )

        max_row_bitmap_height = max(
            len(character_bitmap) for character_bitmap in row_bitmap
        )
        current_row_begin_position_vertical += (
            max_row_bitmap_height + spacing_between_characters_vertical
        )


# "boolean_bitmap" can also be zero dimensional (just a simple "True" or "False")
# Recursive function
def invert_boolean_bitmap(boolean_bitmap):
    if isinstance(boolean_bitmap, bool):  # handles if 0D bitmap
        return not boolean_bitmap  # inverts boolean
    elif not isinstance(boolean_bitmap, list):
        raise TypeError("invert_boolean_bitmap: Invalid boolean_bitmap format")
    else:
        inverted_boolean_bitmap = []
        for current_boolean_bitmap in boolean_bitmap:
            inverted_boolean_bitmap.append(
                invert_boolean_bitmap(current_boolean_bitmap)
            )
        return inverted_boolean_bitmap


def manager_cursor_color_inverted_status(
    cursors_color_inverted_status: bool,
    cursor_blink_change_duration_ms: int,
    current_time_ms: int,
    when_last_change_time_ms: int
):
    time_since_last_change = (
        current_time_ms - when_last_change_time_ms
    )

    if time_since_last_change >= cursor_blink_change_duration_ms:
        return not cursors_color_inverted_status, current_time_ms

    return cursors_color_inverted_status, when_last_change_time_ms


# Implement `manager_character_row(screen_surface, character_dictionary, character_row_bitmap, cursor_position_index, cursor_blink_toggle_time_ms, spacingbetween_characters_horizontal, spacing_between_characters_vertical, begin_position_horizontal, begin_position_vertical)`
def manager_character_row(
    screen_surface,
    character_dictionary,
    character_row_bitmap,
    cursor_position_index,
    cursor_blink_toggle_time_ms,
    spacing_between_characters_horizontal,
    spacing_between_characters_vertical,
    begin_position_horizontal,
    begin_position_vertical,
):
    print("nothing")
