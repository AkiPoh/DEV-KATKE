import json

# EXAMPLE OUTPUT: 3x2 pixel screen with different colors
# rgb_bitmap = [
#     # Row 0: red, green, blue pixels
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],


#     # Row 1: white, black, gray pixels
#     [[255, 255, 255], [0, 0, 0], [128, 128, 128]]
# ]
#
# ACCESS PATTERN:
# rgb_bitmap[0][0] = [255, 0, 0]     # Top-left pixel: red
# rgb_bitmap[0][1] = [0, 255, 0]     # Top-middle pixel: green
# rgb_bitmap[1][2] = [128, 128, 128] # Bottom-right pixel: gray
def screen_surface_to_rgb_bitmap(screen_surface):
    screen_surface_rgb_bitmap = []

    screen_surface_bitmap_width = screen_surface.get_width()  # in pixels
    screen_surface_bitmap_height = screen_surface.get_height()  # in pixels
    for bitmap_row_index in range(
        screen_surface_bitmap_height
    ):  # starts at 0; stops a  n-1
        current_bitmap_rgb_row = []
        for bitmap_column_index in range(
            screen_surface_bitmap_width
        ):  # starts at 0; stops at  n-1
            current_pixel_rgb_color = screen_surface.get_at(
                (bitmap_column_index, bitmap_row_index)
            )
            current_pixel_rgb_color = [
                current_pixel_rgb_color.r,
                current_pixel_rgb_color.g,
                current_pixel_rgb_color.b,
            ]
            current_bitmap_rgb_row.append(current_pixel_rgb_color)
        screen_surface_rgb_bitmap.append(current_bitmap_rgb_row)
    return screen_surface_rgb_bitmap


# EXAMPLE OUTPUT JSON FILE:
# {
#     "metadata": {
#         "width": 3,
#         "height": 2,
#         "format": "rgb_bitmap",
#         "description": "Screen surface captured as RGB bitmap"
#     },
#     "bitmap": [
#         [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#         [[255, 255, 255], [0, 0, 0], [128, 128, 128]]
#     ]
# }
def screen_surface_to_json_bitmap_file(
    screen_surface, output_json_file_path="temp.json"
):
    screen_surface_rgb_bitmap = screen_surface_to_rgb_bitmap(screen_surface)

    screen_surface_rgb_bitmap_width = len(screen_surface_rgb_bitmap[0])
    screen_surface_rgb_bitmap_height = len(screen_surface_rgb_bitmap)

    output_json_data = {
        "screen_surface_rgb_bitmap": {
            "metadata": {
                "bitmap_width": screen_surface_rgb_bitmap_width,
                "bitmap_height": screen_surface_rgb_bitmap_height,
            },
            "bitmap": screen_surface_rgb_bitmap,
        }
    }

    with open(output_json_file_path, "w") as output_json_file:
        json.dump(output_json_data, output_json_file, indent=4, separators=(", ", ": "))
