# CHARACTER BITMAP EXAMPLE
# INSTRUCTION: "False" means that the position is "transparent",
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
    display_surface,
    character_bitmap,
    begin_position_horizontal,
    begin_position_vertical,
):
    character_bitmap_height = len(character_bitmap)
    character_bitmap_width = len(character_bitmap[0])

    filled_pixel_color = (0, 0, 0)  # COLOR: black

    for character_bitmap_vertical_position in range(character_bitmap_height):
        for character_bitmap_horizontal_position in range(character_bitmap_width):
            bitmap_position_should_be_filled = character_bitmap[
                character_bitmap_vertical_position
            ][character_bitmap_horizontal_position]  # Either "True" or "False"

            if bitmap_position_should_be_filled:
                filled_display_surface_position_horizontal = (
                    begin_position_horizontal + character_bitmap_horizontal_position
                )
                filled_display_surface_position_vertical = (
                    begin_position_vertical + character_bitmap_vertical_position
                )
                display_surface.set_at(
                    (
                        filled_display_surface_position_horizontal,
                        filled_display_surface_position_vertical,
                    ),
                    filled_pixel_color,
                )
