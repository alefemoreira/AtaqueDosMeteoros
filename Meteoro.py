import pygame, math


class Meteoro():
    wCenter = (1280 + 150) / 2
    hCenter = 0

    rectP: pygame.Rect

    raio = 215
    velocidade = 4

    fase: float
    angulo: int

    meteoro = pygame.image.load("images/meteoro2.png")
    meteoro = pygame.transform.scale(meteoro, (40, 102))

    pos_x: float
    pos_y: float

    def __init__(self):
        self.fase = 95 / 180 * math.pi  # math.pi / 2'''
        self.angulo = 0
        pass

    def toque(self, rectM):
        return self.rectP.colliderect(rectM)

    def meteoroSol(self, Tela):
        self.pos_x = self.wCenter + self.raio * math.cos(self.fase + self.velocidade * (self.angulo / 180 * math.pi))
        self.pos_y = self.hCenter + self.raio * math.sin(self.fase + self.velocidade * (self.angulo / 180 * math.pi))

        self.posicao = (self.pos_x, self.pos_y)

        self.rectP = pygame.draw.ellipse(Tela, (0, 0, 0), (  # termina na próxima linha
            self.pos_x + 10, self.pos_y + 10, 25, 25))  # desenha Circulo para detectar toque

        self.angulo += 1

        Tela.blit(self.meteoro, (self.pos_x, self.pos_y))
