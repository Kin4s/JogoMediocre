import pygame, random, time
from pygame.locals import *


#config de logs + email e nome
#nomzin = input('diga seu nome: ')
#email = input('Diga seu Email: ')
#dados = {'nome':nomzin,'email':email}
#logs = open('logs.txt','a')
#logs.write(str(dados))

pygame.init()

#tela
pygame.display.set_caption("Jogo Mediocre")
icone = pygame.image.load("Jogo Medíocre/assets/boneco.png")
pygame.display.set_icon(icone)
background = pygame.image.load("Jogo Medíocre/assets/background.png")
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()

def text_objects(texto, font):  #recebe parâmetros da função abaixo
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()

def nomeDoJogo(texto):   #jeito "complexo" de escrever na tela
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = (700, 25)
    gameDisplay.blit(TextSurf, TextRect)

def placar(contador):   #jeito simples de escrever na tela
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Placar: " +str(contador), True, black)
    gameDisplay.blit(texto, (175, 15))

#cores
black = (0,0,0)
white = (255,255,255)

#movimentoBoneco

boneco = pygame.image.load("Jogo Medíocre/assets/boneco.png")
bonecoX = 0
bonecoY = 0
movimentoBonecoY = 0

def mexeBoneco(x, y):
    gameDisplay.blit(boneco, (x, y))

#movimentoInvaders
i1 = pygame.image.load("Jogo Medíocre/assets/eu1.png")
i2 = pygame.image.load("Jogo Medíocre/assets/eu2.png")
i3 = pygame.image.load("Jogo Medíocre/assets/eu3.png")
i4 = pygame.image.load("Jogo Medíocre/assets/eu4.png")
i5 = pygame.image.load("Jogo Medíocre/assets/eu5.png")
#invader = pygame.image.load("Jogo Medíocre/assets/eu1.png")
invaders = [i1, i2, i3, i4, i5]
invader = random.choice(invaders)
invaderX = 800
origemY = [0, 150, 300, 465]
invaderY = random.choice(origemY)

def mexeInvader(x, y):
    gameDisplay.blit(invader, (x, y))

#movimentoProjetil
shotEnabler = False
projetil = pygame.image.load("Jogo Medíocre/assets/blast.png")
projetilX = 0
projetilY = 0
movimentoProjetilX = 0

def mexeProjetil(x, y):
    gameDisplay.blit(projetil, (x, y))

#quadrantes
y1 = 0
y2 = 150
y3 = 300
y4 = 465

#lane do boneco

lane1 = y1
lane2 = y2
lane3 = y3
lane4 = y4

while True:
    #[ini] comandos
    acoes = pygame.event.get()
    for acao in acoes:
        if acao.type == pygame.QUIT:
            pygame.quit()
            quit()
        if acao.type == pygame.KEYDOWN:
            if acao.key == pygame.K_1:
                movimentoBonecoY = y1
                lane = y1
            if acao.key == pygame.K_2:
                movimentoBonecoY = y2
                lane = y2
            if acao.key == pygame.K_3:
                movimentoBonecoY = y3
                lane = y3
            if acao.key == pygame.K_4:
                movimentoBonecoY = y4
                lane = y4
            if acao.key == pygame.K_RIGHT:
                shotEnabler = True
                #projetilY = lane()
                movimentoProjetilX = +15
        #if acao.type == pygame.KEYUP:
        #    movimentoBonecoY = 0
    #[end] comandos

    bonecoY = movimentoBonecoY
    projetilX += movimentoProjetilX

    #if projetilX > 750:
    #    shotEnabler = False
    #    projetilX = -150

    #colisões
    if bonecoX + 100 == invaderX:
        bonecoY = 0

    if bonecoY < 0:
        bonecoY = 0
    if bonecoY > 500:
        bonecoY = 500

    if invaderX > 0:
        invaderX = invaderX - 3

    gameDisplay.fill(white)
    gameDisplay.blit(background, (0,0))
    mexeBoneco(bonecoX, bonecoY)
    mexeInvader(invaderX, invaderY)

    if shotEnabler == True:
        mexeProjetil(projetilX, projetilY)
    if projetilX < 800:
        projetilY = lane()
    if projetilX > 750:
        shotEnabler = False
        projetilX = -150
    if shotEnabler == False:
        projetilX = 0

    nomeDoJogo("Tobi Invaders")
    placar(0)

    pygame.display.update()
    clock.tick(60)