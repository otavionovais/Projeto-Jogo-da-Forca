import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")

    palavras = ["uva", "manga", "abacate", "melancia", "pera", "goiaba"]
    palavra = random.choice(palavras)
    
    letras_descobertas = ["_" for letra in palavras]
    letras_erradas = []
    chances = 6

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:".join(letras_erradas))
        tentativa = input("\nDigite uma letra:")


        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if letra == tentativa:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)


if __name__ == "__main__":
    game()
    print("Obrigado por jogar!")