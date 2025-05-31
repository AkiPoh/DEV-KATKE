import pygame

# EXAMPLE: 3x2 pixel screen with different colors
# rgb_bitmap = [
#     # Row 0: red, green, blue pixels  
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    
#     # Row 1: white, black, gray pixels
#     [[255, 255, 255], [0, 0, 0], [128, 128, 128]]
# ]
# 
# Access pattern:
# rgb_bitmap[0][0] = [255, 0, 0]     # Top-left pixel: red
# rgb_bitmap[0][1] = [0, 255, 0]     # Top-middle pixel: green  
# rgb_bitmap[1][2] = [128, 128, 128] # Bottom-right pixel: gray
def screen_surface_to_rgb_bitmap(screen_surface):
    screen_surface_rgb_numpy_bitmap = pygame.surfarray.array3d(screen_surface)

    screen_surface_rgb_bitmap = screen_surface_rgb_numpy_bitmap.tolist()
