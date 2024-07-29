import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")

    palavras = ["uva", "manga", "abacate", "melancia", "pera", "goiaba"]
    palavra = random.choice(palavras)
    lista_letras_palavras = [letra for letra in palavra]

    tabuleiro = ["_"] * len(palavra)
    
    letras_tentativas = []
    chances = 6

    while chances > 0:
        print(display_hangman(chances))
        print("\nChances restantes:", chances)
        print("Palavra: ", tabuleiro)
        tentativa = input("\nDigite uma letra:")

        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        letras_tentativas.append(tentativa)

        if tentativa in lista_letras_palavras:
            
            print("Você acertou a letra!")
            
            # Loop
            for indice in range(len(lista_letras_palavras)):

                # Condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
            
            # Se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra))
                break
        else:
            print("Ops. Essa letra não está na palavra!")
            # Decremento
            chances -= 1
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}.".format(palavra))


if __name__ == "__main__":
    game()
    print("Obrigado por jogar!")