import pygame, math
from random import randrange

# from AtaqueDosMeteoros import principal

pygame.init()


class Planetas():
    wCenter = (1280 + 150) / 2
    hCenter = 0

    angulo = 0

    sprite: pygame.Surface
    rectP: pygame.Rect

    fase: int

    pos_x: float
    pos_y: float
    wSize: int
    semiSize: int

    def __init__(self, sprite, resize):
        self.wSize = round(resize)

        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, (self.wSize, self.wSize))
        self.semiSize = self.wSize / 2

        self.fase = randrange(0, 360, 90) / 180 * math.pi

    def toque(self, rectM):
        return self.rectP.colliderect(rectM)

    def orbita(self, Tela, Velocidade, Raio):
        self.pos_x = self.wCenter + Raio * math.cos(Velocidade * -(self.fase + self.angulo / 180 * math.pi))
        self.pos_y = self.hCenter + Raio * math.sin(Velocidade * -(self.fase + self.angulo / 180 * math.pi))

        # self.rectP = pygame.draw.rect(Tela, (225, 225, 255), (self.pos_x, self.pos_y, self.wSize, self.wSize)) desenha retangulo

        self.rectP = pygame.draw.ellipse(Tela, (16, 16, 16), (  # termina na próxima linha
            self.pos_x, self.pos_y, self.wSize, self.wSize))  # desenha Circulo para detectar toque

        Tela.blit(self.sprite, (self.pos_x, self.pos_y))

        self.angulo += 1
