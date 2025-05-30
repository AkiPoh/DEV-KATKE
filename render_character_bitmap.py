def render_character_bitmap(screen, bitmap, begin_position_x, begin_position_y):
    bitmap_height = len(bitmap)
    bitmap_width = len(bitmap[0])

    for bitmap_y in range(bitmap_height):
        for bitmap_x in range(bitmap_width):
            pixel_is_filled = bitmap[bitmap_y][bitmap_x]

            if pixel_is_filled: 
                screen_x = begin_position_x + bitmap_x
                screen_y = begin_position_y + bitmap_y
                screen.set_at((screen_x, screen_y), (0, 0, 0))
