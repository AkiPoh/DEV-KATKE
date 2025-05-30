import pygame

character_number_sign = [
    [False, True, False, True, False],
    [True, True, True, True, True],
    [False,True, False, True, False],
    [True, True, True, True, True],
    [False,True, False, True, False],
]

pygame.init()
screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
