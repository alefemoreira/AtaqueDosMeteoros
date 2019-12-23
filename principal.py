import pygame, os
from time import sleep, time
import Planetas, Sol, Meteoro

try:
    pygame.init()
except:
    print('Erro')

sol = Sol.Sol('images/Planetas/Sol.png', 450)

mercurio = Planetas.Planetas("images/Planetas/Mercurio.png", 44)
venus = Planetas.Planetas("images/Planetas/Venus.png", 104)
terra = Planetas.Planetas("images/Planetas/Terra.png", 120)
marte = Planetas.Planetas("images/Planetas/Marte.png", 61)
jupiter = Planetas.Planetas("images/Planetas/Jupiter.png", 50)
saturno = Planetas.Planetas("images/Planetas/Saturno.png", 50)
urano = Planetas.Planetas("images/Planetas/Urano.png", 50)
netuno = Planetas.Planetas("images/Planetas/Netuno.png", 50)

meteoros = list()

planetaObj = [mercurio, venus, terra, marte, jupiter, saturno, urano, mercurio]

pontuacaoTela = pygame.image.load("images/pontuacaoTela.png")
nomeJogo = pygame.image.load("images/nomeJogo.png")
meteoro = pygame.image.load("images/meteoro.png")
meteoro = pygame.transform.scale(meteoro, (40, 102))
os.environ['SDL_VIDEO_CENTERED'] = '1'

bgMusic = "musics/mastodon.mp3"
menuBg = pygame.image.load('images/bgMenu2.png')
planetaTeste = pygame.image.load("images/icone.png")

largura = 1280
altura = 720

Janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ataque Dos Meteoros")
pygame.display.set_icon(planetaTeste)

cor1 = (70, 137, 134)
cor2 = (103, 105, 71)
cor3 = (85, 90, 105)
cor4 = (12, 21, 48)
cor5 = (44, 6, 15)
cinza = (150, 150, 150)
branco = (255, 255, 255)

play = True
sair = True
menu = inicio = True
toque: bool
toqueM: bool
fimDeJogo = False
direita = esquerda = False

inicio1 = fim = time()

relogio = pygame.time.Clock()

velocidadeDaTerra = 2
velocidadeDoMeteoro = 30

pontuacao = 0

centroMeteoro = (largura + 150) / 2 - 20
alturaInicial = 720 - 19
pos = [centroMeteoro, alturaInicial]


def toqueSol():
    return sol.toque(rectM)


def toquePlanetas():
    for c in range(0, 4):
        if fase == 2:
            if planetaObj[c + 4].toque(rectM):
                pos[1] = alturaInicial
                return True
        else:
            if planetaObj[c].toque(rectM):
                pos[1] = alturaInicial
                return True


def toqueMeteoros():
    parcial = False
    for c in range(0, len(meteoros)):
        parcial = meteoros[c].toque(rectM)
        if parcial:
            return parcial

    return parcial


def verificaToque(posXmin, posXmax, posYmin, posYmax):
    """

    :param posXmin: posição do eixo X minima
    :param posXmax: posição eixo x máxima (largura)
    :param posYmin: posição eixo Y minima
    :param posYmax: posição eixo Y máxima (altura)
    :return: True: quando ou houver clique; False: Quando não houver

    author: Alefe Moreira
    """
    posXMouse = pygame.mouse.get_pos()[0]
    posYMouse = pygame.mouse.get_pos()[1]

    if posXMouse >= posXmin and posXMouse <= posXmax and posYMouse >= posYmin and posYMouse <= posYmax:

        return True
    else:
        return False


def criaTexto(msg, cor, tamFont, posicaoX, posicaoY, auto=False):  # Letras. Fonte Desse método não tem Numeros
    tam = 0
    fonte = pygame.font.SysFont('SPALA MARS', tamFont)
    texto1 = fonte.render(msg, True, cor)
    if auto:
        tam = pygame.Surface.get_width(texto1) / 2
    Janela.blit(texto1, [posicaoX - tam, posicaoY])


def criaTexto2(msg, cor, tamFont, posicaoX, posicaoY, auto=False):  # para ser usado com Numeros
    tam = 0
    fonte = pygame.font.SysFont(None, tamFont)
    texto1 = fonte.render(msg, True, cor)
    if auto:
        tam = pygame.Surface.get_width(texto1) / 2
    Janela.blit(texto1, [posicaoX - tam, posicaoY])


def screenPontuacao(pontuacao):
    criaTexto("Pontuação:", cor1, 35, 0, 0)
    criaTexto2(str(pontuacao), cor1, 30, 0, 40)


fase = 1
press = False

while sair:
    while menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = False
                menu = False
                quit()
            if evento.type == pygame.MOUSEBUTTONUP or evento.type == pygame.KEYUP:
                enter = False
                esc = False
                try:
                    if evento.key == pygame.K_KP_ENTER:
                        enter = True
                    if evento.key == pygame.K_ESCAPE:
                        esc = True
                except:
                    pass

                if enter or verificaToque(largura / 2 - 100, (largura / 2 - 100) + 200, 285,
                                          285 + 50):
                    pygame.draw.rect(Janela, cor1, [largura / 2 - 100, 285, 200, 50])
                    criaTexto("INICIAR", cor4, 50, largura / 2, 285, True)
                    pygame.display.update()

                    sleep(1)
                    menu = False
                    pygame.mixer.music.stop()

                if esc or verificaToque(largura / 2 - 62.5, (largura / 2 - 62.5) + 125, 385, 385 + 50):
                    pygame.draw.rect(Janela, cor1, [largura / 2 - 62.5, 385, 125, 50])
                    criaTexto("SAIR", cor4, 50, largura / 2, 385, True)
                    pygame.display.update()

                    sleep(1)
                    menu = False
                    sair = False
                    quit()
                    break

        if inicio:
            # pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.load("musics/Tony_Iggy_-_Astronomia__iCarroller_20110423060437.WAV")
            pygame.mixer.music.play(-1)

            inicio = False

        Janela.blit(menuBg, (0, 0))
        Janela.blit(nomeJogo, (1280 / 2 - 601 / 2, 125))  # imprime nome do jogo
        # criaTexto("MENU", cor1, 100, largura / 2 - 110, 100)

        pygame.draw.rect(Janela, cinza, [largura / 2 - 100, 285, 200, 50])
        criaTexto("INICIAR", cor4, 50, largura / 2, 285, True)

        pygame.draw.rect(Janela, cinza, [largura / 2 - 62.5, 385, 125, 50])
        criaTexto("SAIR", cor4, 50, largura / 2, 385, True)

        pygame.display.update()

    cont = 0

    while fimDeJogo:

        tempoDeExecucao = fim - inicio1

        # tempoDeExecucao = 3660

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                break

            if evento.type == pygame.MOUSEBUTTONUP or evento.type == pygame.KEYUP:
                enter = False
                esc = False
                try:
                    if evento.key == pygame.K_KP_ENTER:
                        enter = True
                    if evento.key == pygame.K_ESCAPE:
                        esc = True
                except:
                    pass

                if enter or verificaToque(largura / 2 - 125, (largura / 2 - 125) + 250, 285,
                                          285 + 50):
                    pygame.draw.rect(Janela, cor1, [largura / 2 - 125, 305, 250, 50])
                    criaTexto("VOLTAR", cor4, 50, largura / 2, 305, True)
                    pygame.display.update()

                    sleep(1)

                    menu = False
                    play = True
                    pontuacao = 0
                    velocidadeDaTerra = 2
                    velocidadeDoMeteoro = 30
                    fase = 1
                    meteoros = list()
                    fimDeJogo = False

                if esc or verificaToque(largura / 2 - 62.5, (largura / 2 - 62.5) + 125, 405, 405 + 50):
                    pygame.draw.rect(Janela, cor1, [largura / 2 - 62.5, 405, 125, 50])
                    criaTexto("SAIR", cor4, 50, largura / 2, 405, True)
                    pygame.display.update()

                    sleep(1)
                    menu = False
                    sair = False

                    quit()
                    break

        if inicio:
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.load("musics/Tony_Iggy_-_Astronomia__iCarroller_20110423060437.WAV")
            pygame.mixer.music.play(-1)

            inicio = False

        Janela.blit(menuBg, (0, 0))

        pygame.draw.rect(Janela, cinza, [largura / 2 - 125, 305, 250, 50])
        criaTexto("VOLTAR", cor4, 50, largura / 2, 305, True)

        pygame.draw.rect(Janela, cinza, [largura / 2 - 62.5, 405, 125, 50])
        criaTexto("SAIR", cor4, 50, largura / 2, 405, True)

        if tempoDeExecucao >= 3600:
            tempoString = str(round(tempoDeExecucao / 3600, 2))  # Arredonda e transforma em horas
            pontoFlutuante = tempoString.find(".")  # obtem posição do ponto que divide as casas fluruantes
            minuto = round((0 + float(tempoString[pontoFlutuante:])) * 60)  # faz o calculo dos minutos

            pygame.draw.rect(Janela, cinza, [0, 147.5, 1280, 100])  # desenha fundo
            criaTexto2(f'Tempo: {tempoString[:pontoFlutuante]}h {minuto}min', cor4, 50, largura / 2, 155, True)

            criaTexto2(f'Pontuação: {pontuacao}', cor4, 50, largura / 2, 205, True)

        elif tempoDeExecucao >= 60:
            tempoString = str(round(tempoDeExecucao / 60, 2))  # Arredonda e transforma em minutos
            pontoFlutuante = tempoString.find(".")  # obtem posição do ponto que divide as casas fluruantes
            segundo = round((0 + float(tempoString[pontoFlutuante:])) * 60)  # faz o calculo dos segundos

            pygame.draw.rect(Janela, cinza, [0, 147.5, 1280, 100])  # desenha fundo
            criaTexto2(f'Tempo: {tempoString[:pontoFlutuante]}min {segundo}seg', cor4, 50, largura / 2, 155, True)

            criaTexto2(f'Pontuação: {pontuacao}', cor4, 50, largura / 2, 205, True)

        elif tempoDeExecucao < 60:
            tempoString = str(round(tempoDeExecucao))

            pygame.draw.rect(Janela, cinza, [0, 147.5, 1280, 100])  # desenha fundo
            criaTexto2(f'Tempo: {tempoString}seg', cor4, 50, largura / 2, 155, True)

            criaTexto2(f'Pontuação: {pontuacao}', cor4, 50, largura / 2, 205, True)

        pygame.display.update()

    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:
            quit()

        if evento.type == pygame.KEYUP:
            try:
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                    press = True
                    toque = False
                    pos[1] -= 30

                if evento.key == pygame.K_LEFT:
                    esquerda = False
                    direita = False
                if evento.key == pygame.K_RIGHT:
                    direita = False
                    esquerda = False
            except:
                pass

        if evento.type == pygame.KEYDOWN:
            try:
                if evento.key == pygame.K_LEFT:
                    esquerda = True
                    direita = False
                if evento.key == pygame.K_RIGHT:
                    direita = True
                    esquerda = False
            except:
                pass

        if evento.type == pygame.MOUSEBUTTONUP:
            try:
                if verificaToque(50, 100, 720 - 50, 720 - 50 + 25):
                    pygame.draw.rect(Janela, cor1, [50, 720 - 50, 50, 25])
                    criaTexto("SAIR", cor4, 25, 75, 720 - 50, True)
                    pygame.display.update()

                    sleep(1)

                    # menu = True
                    fim = time()
                    fimDeJogo = True
                    inicio = True
                    # pontuacao = 0
                    fase = 1
                    meteoros = list()
                    velocidadeDaTerra = 2
                    velocidadeDoMeteoro = 30
                    pygame.mixer.music.stop()

            except:
                pass

    if play:
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load("musics/Mastodon_-_Blood_And_Thunder_(2).WAV")
        pygame.mixer.music.play(-1)

        play = False

    Janela.blit(menuBg, (0, 0))
    sol.rotacao(Janela)  # Gira Sol

    if fase == 1:
        mercurio.orbita(Janela, velocidadeDaTerra * 4.14, 300)
        venus.orbita(Janela, velocidadeDaTerra * 1.62, 400)
        terra.orbita(Janela, velocidadeDaTerra, 520)
        marte.orbita(Janela, velocidadeDaTerra * 0.53, 650)

        if pontuacao >= 800:
            meteoros = list()
            velocidadeDaTerra += 1.5
            velocidadeDoMeteoro += 10
            fase = 2

    elif fase == 2:
        jupiter.orbita(Janela, velocidadeDaTerra * 5, 300)
        saturno.orbita(Janela, velocidadeDaTerra * 2.8, 410)
        urano.orbita(Janela, velocidadeDaTerra, 520)
        netuno.orbita(Janela, velocidadeDaTerra * 0.5, 650)

        if pontuacao >= 1600:
            fase = 3
            fim = time()
            fimDeJogo = True
            inicio = True
            sleep(1)

    rectM = pygame.draw.ellipse(Janela, (255, 255, 255), (pos[0], pos[1], 40, 40))  # imprime retangulo base
    Janela.blit(meteoro, pos)  # imprime Meteoro na Tela

    # press = verificaSobreposicao()

    if press and not toque:  # move meteoro
        toque = toquePlanetas()
        if toque:
            if pontuacao >= 20:
                pontuacao -= 20  # subtrai pontuação ao bater em planetas

        if not toqueSol() and pos[1] >= 0:
            pos[1] -= velocidadeDoMeteoro

        else:
            if pos[0] >= 715 - 200 - 40 and pos[0] <= 715 + 200:  # verifica se a o meteoro esta no alcance Sol
                toqueM = toqueMeteoros()
                if not toqueM:
                    meteoros.append(Meteoro.Meteoro())  # adiciona meteoro nas lista
                    pontuacao += 50  # soma pontuação
                else:
                    if pontuacao >= 10:
                        pontuacao -= 10  # subtrai pontuação ao bater em meteoros
            pos[1] = alturaInicial  # reinicia a altura do meteoro
            press = False

    if direita:  # Faz o meteoro se mover para direita entre 150 e 1280 até que o usuario pare
        # if pos[0] <= 1280 - 40:
        for c in range(0, 5):
            pos[0] += 2
            if pos[0] > 1280:
                pos[0] = 150 - 40

    if esquerda:  # Faz o meteoro se mover para esquerda entre 150 e 1280 até que o usuario pare
        # if pos[0] >= 150:
        for c in range(0, 5):
            pos[0] -= 2
            if pos[0] < 150 - 40:
                pos[0] = 1280

    for c in range(0, len(meteoros)):
        meteoros[c].meteoroSol(Janela)

    Janela.blit(pontuacaoTela, (0, 0))  # Espaço de Pontuação
    screenPontuacao(pontuacao)  # Chama o método de manipular tela de pontuação
    pygame.draw.rect(Janela, cinza, [50, 720 - 50, 50, 25])
    criaTexto("SAIR", cor4, 25, 75, 720 - 50, True)

    relogio.tick(30)
    # pygame.draw.rect(Janela, (0, 0, 0), [715 - 0.5, 0, 1, 720]) # marca o meio
    pygame.display.update()

pygame.quit()
quit()
