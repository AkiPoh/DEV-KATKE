import pygame

from render_character_bitmap import render_character_bitmap

character_bitmap_number_sign = [
    [False, True, False, True, False],
    [True, True, True, True, True],
    [False, True, False, True, False],
    [True, True, True, True, True],
    [False, True, False, True, False],
]

pygame.init()

screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # COLOR: White

    render_character_bitmap(screen, character_bitmap_number_sign, 100, 100)

    pygame.display.flip()  # Update the display
    clock.tick(60)  # 60 FPS

pygame.quit()
