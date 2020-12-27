import random                      #hace un llamado a un acceso de python


def generador_contrasena():       # creas una funcion para hacer el generador de contraseñas
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    #crea las mayusculas 
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]   #y minusculas para 
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]     #hacer contraseñas con los parametros puestos

    caracteres = mayusculas + numeros + minusculas    #hace que los caracteres se sumen y se mezclen 

    contrasena = []               #aca se le agrega el parametro caracter_random

    for i in range(9):                                 #aca especificas cuantas letras quieres poner en el geneador de letras
        caracter_random = random.choice(caracteres)    #caracter random se le agrega el random.choice para que el computador eliga las letras por si sola giandose por la 
        contrasena.append(caracter_random)              #a la variable contrasena le agregas el parametro caracter_random              #cantidad que le pediste

    contrasena = "".join(contrasena)                #hace que todas los caracteres y numeros se vuelvan string de la variable contrasena
    return contrasena                                #aca vuelve a retomar la contrasena  y aparezca

def run():                                               #define a la variable run  para que arranque
    contrasena = generador_contrasena()                  #enlaza a la variable contrasena con la variable generador_contrasena
    print("tu nueva contraseña es : " + contrasena)     #imprime en pantalla la la nueva contrasena 


if __name__ == "__main__":
    run()