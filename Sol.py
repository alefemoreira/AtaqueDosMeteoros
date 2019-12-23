import pygame


class Sol():
    # relogio = pygame.time.Clock()
    imagem: pygame.Surface
    centerW = (1280 + 150) / 2
    size: int

    rectP: pygame.Rect

    def toque(self, rectM):
        return self.rectP.colliderect(rectM)

    def __init__(self, imagem: str, size: int):
        self.imagem = pygame.image.load(imagem)
        self.size = size
        self.imagem = pygame.transform.scale(self.imagem, (size, size))

    def rotacao(self, tela):
        self.imagem = pygame.transform.rotate(self.imagem, 90)

        self.rectP = pygame.draw.ellipse(tela, (0, 0, 0), [self.centerW - 200, -200, 400, 400])

        tela.blit(self.imagem, (self.centerW - self.size / 2, -self.size / 2))
