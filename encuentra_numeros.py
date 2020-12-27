import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Escibe un numero del 1 al 100 : "))
    vidas = 5

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("elegiste un numero muy bajo, tiene que ser mayor")
        else:
            print("elegiste un numero muy alto, tiene que ser menor")
        numero_elegido = int(input("te quedan " + str(vidas) + " vidas elige otro numero : " ))
        vidas -= 1
        if vidas == 0:
            print ("GAME OVER!!")
            break
    if numero_aleatorio == numero_elegido:
        print ("Excelente encontraste el numero correcto ..")
      

if __name__ == "__main__":
    run()   