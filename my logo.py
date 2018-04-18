import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREENWIDTH = 400
SCREENHEIGHT = 400

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False



    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [55, 200, 100, 70], 0)
    pygame.draw.ellipse(screen, WHITE[20, 20, 250, 100], 2)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)


    pygame.diplay.flip()


    clock.tick

pygame.quit()
         
