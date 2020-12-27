def conversor(tipo_peso, peso_1, valor):
    peso = float(input("Cuantos  "+ tipo_peso + "? : "))
    peso_1 = peso*peso_1
    peso_1 = round(peso_1, 2 )
    peso_1 = str(peso_1)
    libra = 220
    kilo = 100 
    print("usted tiene " + peso_1 + valor)

menu = """--CONVERSOR PESO--
1 - KILOGRAMOS A LIBRAS
2 - LIBRAS A KILOGRAMOS

Ingrese su opcion porfavor:  """

opcion = int(input(menu))
if opcion == 1:
    conversor("Kilogramos", 2.20462, " Libras")
    while peso_1 < libra :
        print ("estas sobre peso")
    
else:
        print ("no estas sobre peso")
    
    
if opcion == 2:
    conversor("Libras", 0.453592," Kilogramos")
    while peso_1 < kilo :
        print ("estas sobre peso")

    else:
        print ("no estas sobre peso")

else:
    print ("eliga una opcion correcta porfavor : ")