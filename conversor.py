menu = """"
Bienvenidos 🌵🌴🌴🌵🌵
Cambio de Monedas 

1 - Dolares a pesos
2 - Pesos a Dolares   
3 - solo el saludo 

Selecciona ....

"""

def calcular(cambio):
    dolares = input("Cuantos dolares tienes?")
    dolares = float(dolares)
    valor_dolar = cambio
    pesos = dolares * valor_dolar
    pesos = round(pesos)
    pesos = str(pesos)
    print ("Tienes $" + pesos + " pesos")

opcion = int(input(menu))

if opcion == 1:
    calcular(3620)
    
elif opcion == 2:
   calcular(3830)
else:
    print("Aqui tu saludo, vuelve pronto")
