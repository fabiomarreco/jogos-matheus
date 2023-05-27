caminho_para_imagem_fundo = 'imagens/fundo.jpg'
caminho_para_imagem_barra = 'imagens/barra.png'
caminho_para_imagem_tiro = 'imagens/tiro.png'
caminho_para_imagem_nave = 'imagens/nave.png'

import pygame
import sys

def jogar():
    largura, altura = 1024, 768  # Tamanho da tela em pixels
    tamanho_barra = 80, 80  # Tamanho da barra em pixels
    # tamanho_barra = 120, 20  # Tamanho da barra em pixels
    tamanho_nave = 80, 80  # Tamanho da nave em pixels
    tamanho_tiro = 30, 60  # Tamanho do tiro em pixels
    # tamanho_tiro = 10, 20  # Tamanho do tiro em pixels
    posicao_barra = [largura // 2 - tamanho_barra[0] // 2, altura - tamanho_barra[1]]
    posicao_nave = [largura // 2, 0]
    posicao_tiro = [0, 0]
    tiro_ativo = False
    velocidade_nave = 4
    velocidade_tiro = 10
    velocidade_barra = 10

    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    clock = pygame.time.Clock()

    # Carregar imagens
    fundo = pygame.image.load(caminho_para_imagem_fundo)
    fundo = pygame.transform.scale(fundo, (largura, altura))
    imagem_barra = pygame.image.load(caminho_para_imagem_barra).convert_alpha()
    imagem_barra = pygame.transform.scale(imagem_barra, tamanho_barra)
    imagem_nave = pygame.image.load(caminho_para_imagem_nave).convert_alpha()
    imagem_nave = pygame.transform.scale(imagem_nave, tamanho_nave)
    imagem_tiro = pygame.image.load(caminho_para_imagem_tiro).convert_alpha()
    imagem_tiro = pygame.transform.scale(imagem_tiro, tamanho_tiro)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_a] and posicao_barra[0] > 0:
            posicao_barra[0] -= velocidade_barra
        if tecla[pygame.K_s] and posicao_barra[0] < largura - tamanho_barra[0]:
            posicao_barra[0] += velocidade_barra
        if not tiro_ativo and tecla[pygame.K_SPACE]:
            tiro_ativo = True
            posicao_tiro = [posicao_barra[0] + tamanho_barra[0] // 2, altura - tamanho_barra[1]]

        if tiro_ativo:
            posicao_tiro[1] -= velocidade_tiro
            if posicao_tiro[1] <= 0:
                tiro_ativo = False
            elif pygame.Rect(posicao_tiro, tamanho_tiro).colliderect(pygame.Rect(posicao_nave, tamanho_nave)):
                print("Parabéns! Você destruiu a nave inimiga!")
                return

        posicao_nave[0] += velocidade_nave
        if posicao_nave[0] <= 0 or posicao_nave[0] >= largura - tamanho_nave[0]:
            velocidade_nave = -velocidade_nave
        if posicao_nave[1] >= altura - tamanho_nave[1]:
            print("Você perdeu! A nave inimiga chegou à base.")
            return

        tela.blit(fundo, (0, 0))
        tela


        if tiro_ativo:
            posicao_tiro[1] -= velocidade_tiro
            if posicao_tiro[1] <= 0:
                tiro_ativo = False
            elif pygame.Rect(posicao_tiro, tamanho_tiro).colliderect(pygame.Rect(posicao_nave, tamanho_nave)):
                print("Parabéns! Você destruiu a nave inimiga!")
                return

        posicao_nave[0] += velocidade_nave
        if posicao_nave[0] <= 0 or posicao_nave[0] >= largura - tamanho_nave[0]:
            velocidade_nave = -velocidade_nave
        if posicao_nave[1] >= altura - tamanho_nave[1]:
            print("Você perdeu! A nave inimiga chegou à base.")
            return

        tela.blit(fundo, (0, 0))
        tela.blit(imagem_barra, tuple(posicao_barra))
        tela.blit(imagem_nave, tuple(posicao_nave))
        if tiro_ativo:
            tela.blit(imagem_tiro, tuple(posicao_tiro))

        pygame.display.flip()
        clock.tick(60)  # Limita o jogo a 60 frames por segundo

if __name__ == "__main__":
    jogar()
