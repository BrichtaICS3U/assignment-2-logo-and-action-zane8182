import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (61, 237, 37)
RED = (255, 0, 0)
BLUE = (0, 86, 226)
class waves(pygame.sprite.Sprite):


    def __init__(self, colour, width, height, speed:


        super().__init__()

        self
                 .image = pyagem.Surface(width, height)
        self.image.fill(WHITE)
        self.image.set_colorkey(GREEN)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.ellipse(self.image,color,[0,0,self.width,self.height])

        self.rect = self.image.get_rect()

    def moveBackward(self, speed):
        self.rect.y += self.speed*speed / 20

    def changeSpeed(self, speed):
                 self.speed = speed
