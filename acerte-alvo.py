#baixar e importar o pygame
import pygame
import random

#inicialização do jogo e arquivo de audio
pygame.init()
pygame.mixer.init()

#variaveis relevantes jogo

altura_tela = 600 
largura_tela = 800

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Acerte o Alvo!')

#cores
preto = (0,0,0)
branco =(255,255,255)
verde = (0,155,0)



#tempo de frames por segundo

relogio = pygame.time.Clock()
rodando = True


#largura e altura do alvo
tamanho_alvo = 10

# localização alvo, x,y
alvo_rect = pygame.Rect(375,275,tamanho_alvo, tamanho_alvo)

pontos = 0
fonte = pygame.font.SysFont("bahnsschrift",35)
som_acerto = pygame.mixer.Sound("acerto.wav")
som_erro = pygame.mixer.Sound("errou.wav")
while rodando:

    # 1. Eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
#clique randomico para alvo tanto acerto como erro
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if alvo_rect.collidepoint(evento.pos):
               alvo_rect.x = random.randrange(0,largura_tela - tamanho_alvo)
               alvo_rect.y = random.randrange(0,altura_tela - tamanho_alvo)
               pontos +=1
               som_acerto.play()
            else:
                pontos -=2
                som_erro.play()
                if pontos <0:
                    pontos = 0



    tela.fill(preto)

    pygame.draw.rect(tela, verde, alvo_rect)
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, branco)
    tela.blit(texto_pontos, (10,10))

    pygame.display.flip()

    relogio.tick(60)

pygame.quit()


