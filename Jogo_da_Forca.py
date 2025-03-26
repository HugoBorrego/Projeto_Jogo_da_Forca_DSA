# Criando o Jogo da Forca no projeto 1 do curso da DSA

import random
from os import system, name

def limpar_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def jogo():
    limpar_tela()
    print("""
---------------------------------
  Bem vindo(a) ao Jogo da Forca
---------------------------------
Advinhe a palavra abaixo(você terá 6 tentativas): 
             DICA: É uma fruta
""")
    palavras = ['banana', 'uva', 'laranja', 'limao', 'pera', 'morango', 'pessego', 'abacate', 'abacaxi', 'pitanga', 'manga', 'acerola']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print(f"Chances restantes: {chances}")
        print("Letras erradas: ", " ".join(letras_erradas))

        tentativas = input("\nDigite uma letra: ").lower()

        if tentativas in palavra:
            index = 0

            for letra in palavra:
                if tentativas == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativas)

        if "_" not in letras_descobertas:
            print(f"\nParabens, você acertou a palavra: {palavra}")
            break

    print(f"Você perdeu. A palavra era: {palavra}")

if __name__ == "__main__":
    jogo()
