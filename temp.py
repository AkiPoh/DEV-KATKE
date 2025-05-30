def render_character_row_bitmap(screen_surface, character_bitmap, row_bitmap, spacing_between_characters, begin_position_horizontal, begin_position_vertical):
    character_bitmap_width = len(character_bitmap[0])
    current_position_horizontal = begin_position_horizontal
    
    for should_render_character in row_bitmap:
        if should_render_character:
            render_character_bitmap(
                screen_surface,
                character_bitmap,
                current_position_horizontal,
                begin_position_vertical
            )
        
        current_position_horizontal += character_bitmap_width + spacing_between_characters
