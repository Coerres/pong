import pygame
pygame.init()

screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Pong by @Coerres")

timer = pygame.time.Clock()
framerate = 60
black = (0,0,0)
white = (255, 255, 255)



running = True
while running:
    timer.tick(framerate)
    screen.fill((black))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.flip()

pygame.quit()