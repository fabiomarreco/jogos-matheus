import os
import random
import time
import keyboard

def tela(largura, altura, posicao_barra, posicao_c):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(altura):
        for x in range(largura):
            if y == altura - 1 and posicao_barra <= x < posicao_barra + 3:
                print('=', end='')
            elif y == posicao_c[1] and x == posicao_c[0]:
                print('C', end='')
            else:
                print(' ', end='')
        print()

def jogar():
    largura, altura = 50, 10
    numero_jogadas = 0
    while numero_jogadas < 4: 
      posicao_barra = largura // 2 - 1
      posicao_c = [random.randint(0, largura - 1), 0]
      velocidade_c = 0.1
      

      print("Bem-vindo ao jogo de pegar a letra 'C'!")
      print("Use as teclas 'a' e 's' para mover a barra para a esquerda e direita.")
      print("Pressione Enter para começar.")
      input()
      

      while True:
          if keyboard.is_pressed('a') and posicao_barra > 0:
              posicao_barra = posicao_barra - 1
          if keyboard.is_pressed('s') and posicao_barra < largura - 3:
              posicao_barra = posicao_barra + 1
          if posicao_c[1] < altura - 1:
              posicao_c[1] += 1
          else:
              if posicao_barra <= posicao_c[0] < posicao_barra + 3:
                  print("Parabéns! Você pegou a letra 'C'!")
                  break
              else:
                  print("Você perdeu! A letra 'C' caiu.")
                  break

          tela(largura, altura, posicao_barra, posicao_c)
          time.sleep(velocidade_c)
          
      numero_jogadas += 1
if __name__ == "__main__":
    jogar()
