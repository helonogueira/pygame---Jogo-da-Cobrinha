import pygame
import random
import time

vel = 10
preto = pygame.Color(0, 0, 0)
branco = pygame.Color(255, 255, 255)
vermelho = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
azul = pygame.Color(0, 0, 255)

img_inicial = pygame.image.load('pygame\pygame---Jogo-da-Cobrinha\imagem inicial.png').convert()

pygame.init()
pygame.mixer.init()

eat_sound = pygame.mixer.Sound('pygame\pygame---Jogo-da-Cobrinha\som mordida.wav')
game_over_sound = pygame.mixer.Sound('pygame\pygame---Jogo-da-Cobrinha\game over sound.wav')
window = pygame.display.set_mode((720, 480))

def tela_inicial():
    pygame.display.set_caption('Tela inicial')

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'sair'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'jogando' 

        window.fill((preto))
        window.blit(img_inicial,(-120,-20))
        cor = (255,255,255)


        pygame.display.update()

def tela_jogo():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'sair'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'jogando'
                
        window.fill((preto))
        window.blit(img_inicial, (-120, -20))
        fps = pygame.time.Clock()
        posicao_cobra = [100, 50]

        cobra = [[100, 50], [90, 50], [80, 50], [70, 50]]

        posicao_fruta = [random.randrange(1, (720//10)) * 10, random.randrange(1, (480//10)) * 10]

        spawn_fruta = True
        direcao = 'direita'
        mudanca = direcao
        pontuacao = 0 

        def placar (choice, color, font, size):
            score_font = pygame.font.SysFont(font, size)
            score_surface = score_font.render('Placar : ' + str(pontuacao), True, branco)
            score_rect = score_surface.get_rect()
            window.blit(score_surface, score_rect)

        def game_over():
            fonte = pygame.font.SysFont('times new roman', 50)
            final_jogo = fonte.render('Your Score is : ' + str(pontuacao), True, vermelho)
            final_jogo_rect = final_jogo.get_rect()
            final_jogo_rect.midtop = (720/2, 480/4)
            window.blit(final_jogo, final_jogo_rect)
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mudanca = 'cima'
                    if event.key == pygame.K_DOWN:
                        mudanca = 'baixo'
                    if event.key == pygame.K_LEFT:
                        mudanca = 'esquerda'
                    if event.key == pygame.K_RIGHT:
                        mudanca = 'direita'

            if mudanca == 'cima' and direcao != 'baixo':
                direcao = 'cima'
            if mudanca == 'baixo' and direcao != 'cima':
                direcao = 'baixo'
            if mudanca == 'esquerda' and direcao != 'direita':
                direcao = 'esquerda'
            if mudanca == 'direita' and direcao != 'esquerda':
                direcao = 'direita'

            if direcao == 'cima':
                posicao_cobra[1] -= 10
            if direcao == 'baixo':
                posicao_cobra[1] += 10
            if direcao == 'esquerda':
                posicao_cobra[0] -= 10
            if direcao == 'direita':
                posicao_cobra[0] += 10

            cobra.insert(0, list(posicao_cobra))
