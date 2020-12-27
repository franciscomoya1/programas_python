import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Escibe un numero del 1 al 100 : "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("elegiste un numero muy bajo, tiene que ser mayor")
        else:
            print("elegiste un numero muy alto, tiene que ser menor")
        numero_elegido = int(input("ingresa otro numero"))
    print("  ¡¡¡¡¡GANASTE !!!!!    ")    
            

if __name__ == "__main__":
    run()   