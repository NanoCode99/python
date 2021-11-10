import random

def run ():
    numero_aleatorio = random.randint(1,10)
    numero_elegido = int(input("Ingresa un numero cualquiera: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Ingresa un numero mas grande")
        else:
            print("Ingresa un numero mas pequeño")
        numero_elegido = int(input("Ingresa un numero cualquiera: "))
    print("Ganaste!")


if __name__ == '__main__':
    run()