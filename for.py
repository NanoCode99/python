from typing import Text


def run():
#    for contador in range (1,5):
#        print(contador)

    

    # frase = input("Escribe la frase a separar ")
    # for letras in frase:
    #     print(letras)    

    texto = input("Ingresa una palabra")
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()