import pygame
import sys

# Definindo os caminhos para as imagens
caminho_para_imagem_fundo = 'imagens/fundo.jpg'
caminho_para_imagem_barra = 'imagens/barra.png'
caminho_para_imagem_tiro = 'imagens/tiro.png'
caminho_para_imagem_nave = 'imagens/nave.png'
caminho_para_imagem_explosao = 'imagens/explosao.png'  # Adicione a imagem de explosão aqui

def jogar():
    largura, altura = 1024, 768  # Tamanho da tela em pixels
    tamanho_barra = 80, 80  # Tamanho da barra em pixels
    tamanho_nave = 80, 80  # Tamanho da nave em pixels
    tamanho_tiro = 30, 60  # Tamanho do tiro em pixels
    tamanho_explosao = 100, 100  # Tamanho da explosão em pixels
    posicao_barra = [largura // 2 - tamanho_barra[0] // 2, altura - tamanho_barra[1]]
    posicao_nave = [largura // 2, 0]
    posicao_tiro = [0, 0]
    tiro_ativo = False
    explosao_ativa = False
    posicao_explosao = [0, 0]
    velocidade_nave = 4
    velocidade_tiro = 10
    velocidade_barra = 11
    velocidade_queda_nave = 5  # A nave vai descer 1 pixel por frame
    maximo_de_naves = 10  # Número máximo de naves para ganhar/perder o jogo
    naves_destruidas = 0
    naves_escaparam = 0

    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    clock = pygame.time.Clock()

    fonte = pygame.font.Font(None, 36)  # Definir o tipo de fonte

    # Carregar imagens
    fundo = pygame.image.load(caminho_para_imagem_fundo)
    fundo = pygame.transform.scale(fundo, (largura, altura))
    imagem_barra = pygame.image.load(caminho_para_imagem_barra).convert_alpha()
    imagem_barra = pygame.transform.scale(imagem_barra, tamanho_barra)
    imagem_nave = pygame.image.load(caminho_para_imagem_nave).convert_alpha()
    imagem_nave = pygame.transform.scale(imagem_nave, tamanho_nave)
    imagem_tiro = pygame.image.load(caminho_para_imagem_tiro).convert_alpha()
    imagem_tiro = pygame.transform.scale(imagem_tiro, tamanho_tiro)
    imagem_explosao = pygame.image.load(caminho_para_imagem_explosao).convert_alpha()
    imagem_explosao = pygame.transform.scale(imagem_explosao, tamanho_explosao)

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
                explosao_ativa = True
                posicao_explosao = posicao_nave.copy()  # Coloca a explosão na posição da nave
                tiro_ativo = False  # Destrói o tiro
                naves_destruidas += 1
                posicao_nave = [largura // 2, 0]  # Reseta a posição da nave

        posicao_nave[0] += velocidade_nave
        posicao_nave[1] += velocidade_queda_nave  # Faz a nave descer
        if posicao_nave[0] <= 0 or posicao_nave[0] >= largura - tamanho_nave[0]:
            velocidade_nave = -velocidade_nave
        if posicao_nave[1] >= altura - tamanho_nave[1]:
            naves_escaparam += 1
            posicao_nave = [largura // 2, 0]  # Reseta a posição da nave

        if naves_destruidas == maximo_de_naves:
            texto = fonte.render("Parabéns! Você ganhou o jogo!", True, (0, 255, 0))
            tela.blit(texto, (largura//2 - texto.get_width()//2, altura//2 - texto.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            return
        if naves_escaparam == maximo_de_naves:
            texto = fonte.render("Você perdeu o jogo!", True, (255, 0, 0))
            tela.blit(texto, (largura//2 - texto.get_width()//2, altura//2 - texto.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        tela.blit(fundo, (0, 0))
        tela.blit(imagem_barra, tuple(posicao_barra))
        tela.blit(imagem_nave, tuple(posicao_nave))
        if tiro_ativo:
            tela.blit(imagem_tiro, tuple(posicao_tiro))
        if explosao_ativa:
            tela.blit(imagem_explosao, tuple(posicao_explosao))
            explosao_ativa = False  # A explosão deve aparecer apenas em um frame

        # Exibir contagem de naves destruídas e naves que escaparam
        texto = fonte.render(f"{naves_destruidas} x {naves_escaparam}", True, (50, 100, 0))
        tela.blit(texto, (largura - 100, 20))  # Posição do contador na tela

        pygame.display.flip()
        clock.tick(60)  # Limita o jogo a 60 frames por segundo

if __name__ == "__main__":
    jogar()
