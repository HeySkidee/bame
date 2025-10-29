import pygame

pygame.init()
screen = pygame.display.set_mode((700,500))

running = True

while running:
    # to close the game on clicking X icon
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() # to show stuff on screen

pygame.quit() # clearing memory on closing the game