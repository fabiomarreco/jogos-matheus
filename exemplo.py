import random

def main():
    numero_secreto = random.randint(1, 10)
    numero_tentativas = 0

    print("Bem-vindo ao jogo de adivinhação de números!")
    print("Estou pensando em um número entre 1 e 10.")
    
    if numero_secreto % 2 == 0:
        print(f"o número é par.")
    else:
        print(f"o número é ímpar.")


    while True:
        tentativa = int(input("Digite o seu palpite: "))
        numero_tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número em {numero_tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("O número é maior. Tente novamente.")
        else:
            print("O número é menor. Tente novamente.")

if __name__ == "__main__":
    main()
