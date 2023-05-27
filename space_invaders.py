import os
import time
import keyboard

def tela(largura, altura, posicao_barra, posicao_c, posicao_tiro):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(altura):
        for x in range(largura):
            if y == altura - 1 and posicao_barra <= x < posicao_barra + 3:
                print('=', end='')
            elif y == posicao_c[1] and x == posicao_c[0]:
                print('C', end='')
            elif y == posicao_tiro[1] and x == posicao_tiro[0]:
                print('|', end='')
            else:
                print(' ', end='')
        print()

def jogar():
    largura, altura = 30, 25
    posicao_barra = largura // 2 - 1
    posicao_c = [largura // 2, 2]
    posicao_tiro = [0, 0]
    tiro_ativo = False
    direcao_c = 1
    contador_movimento = 0

    print("Bem-vindo ao jogo Space Invaders simplificado!")
    print("Use as teclas 'a' e 's' para mover a nave e a barra de espaço para atirar.")
    print("Pressione Enter para começar.")
    input()

    while True:
        if keyboard.is_pressed('a') and posicao_barra > 0:
            posicao_barra -= 1
        if keyboard.is_pressed('s') and posicao_barra < largura - 3:
            posicao_barra += 1

        if not tiro_ativo and keyboard.is_pressed('space'):
            tiro_ativo = True
            posicao_tiro = [posicao_barra + 1, altura - 2]

        if tiro_ativo:
            posicao_tiro[1] -= 1
            if posicao_tiro[1] == 0:
                tiro_ativo = False
            elif posicao_tiro == posicao_c:
                print("Parabéns! Você destruiu a nave inimiga!")
                break

        posicao_c[0] += direcao_c
        contador_movimento += 1
        if contador_movimento == 5:
            posicao_c[1] += 1
            contador_movimento = 0

        if posicao_c[0] == 0 or posicao_c[0] == largura - 1:
            direcao_c = -direcao_c

        if posicao_c[1] == altura - 1:
            print("Você perdeu! A nave inimiga chegou à base.")
            break

        tela(largura, altura, posicao_barra, posicao_c, posicao_tiro)
        time.sleep(0.1)

if __name__ == "__main__":
    jogar()
