import pygame
import random

pygame.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pong')

# Cores do jogo

verde = (0,205,0)
preto = (0,0,0)
branco = (255,255,255)

#pontuação
fonte_pontos = pygame.font.Font(None, 90)

pontos1 = 0
pontos2 = 0

#raquete
largura_raquete = 10
altura_raquete = 90
#bloco de codigo - classe 

class Raquete:

#função - o que vai acontecer quando for criado a raquete
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, largura_raquete, altura_raquete)

    def desenhar(self, tela):
        pygame.draw.rect(tela, verde, self.rect)

 #funcao de movimento
    def mover (self, tecla_cima, tecla_baixo):
        teclas = pygame.key.get_pressed()
        if teclas[tecla_cima] and self.rect.top > 0:
            self.rect.y -=10 
        elif teclas[tecla_baixo] and self.rect.bottom < 600:
            self.rect.y +=10    



raquete1 = Raquete(10, 300)
raquete2 = Raquete(780,300)

raio_bola = 10
velocidade_bola_x = 6
velocidade_bola_y = 6

class Bola:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - raio_bola, y - raio_bola, raio_bola*2, raio_bola*2)

        self.vel_x = velocidade_bola_x
        self.vel_y = velocidade_bola_y

    def desenhar(self, tela):
        pygame.draw.ellipse(tela,branco, self.rect)

    def mover (self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def verificar_colisao(self, raquete1, raquete2):

     #batida de bola na parede   
        if self.rect.top <=0 or self.rect.bottom >= altura_tela:
            self.vel_y *= -1
     #batida de bola na raquete
        if self.rect.colliderect(raquete1) or self.rect.colliderect(raquete2):
            self.vel_x *=-1    

         

    def resetar(self):
        self.rect.x = largura_tela/2 - raio_bola
        self.rect.y = altura_tela/2 - raio_bola

        pygame.time.delay(1000)


bola = Bola(400,300)        



relogio = pygame.time.Clock()

rodando = True

while rodando:
    #eventos
    for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
         rodando = False

    tela.fill(preto)

    raquete1.desenhar(tela)
    raquete2.desenhar(tela)
    bola.desenhar(tela)

    pygame.draw.aaline(tela, branco, (largura_tela/2, 0), (largura_tela/2, altura_tela))

    texto_p1 = fonte_pontos.render(str(pontos1), True, branco)
    tela.blit(texto_p1, (largura_tela/4, 20))

    # Placar Jogador 2 (direita)
    texto_p2 = fonte_pontos.render(str(pontos2), True, branco)
    tela.blit(texto_p2, (largura_tela * 3/4 - texto_p2.get_width(), 20))

    raquete1.mover(pygame.K_w, pygame.K_s)

    raquete2.mover(pygame.K_UP, pygame.K_DOWN)
    bola.mover()
    bola.verificar_colisao(raquete1.rect, raquete2.rect)

    if bola.rect.left < 0:
            pontos2 +=1
            bola.resetar()  

    if bola.rect.right> largura_tela:
            pontos1 +=1
            bola.resetar()    

    pygame.display.flip()

    relogio.tick(60)              
 
pygame.quit()   