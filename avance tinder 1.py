def GuardarPersonas():

    nombre= input("Como te llamas? ")
    edad= int(input("Que edad tienes? "))
    if edad < 18:
        print("Debe ser mayor de edad para poder registrarte")
        edadmin =int(input("Por favor coloque una edad permitida: "))
    ciudad= input("De donde eres? ")
    genero= input("Cual es tu genero? ")
    gbusca= input("Que genero busca? ")
    edadmin =int (input("Cual es la edad minima que buscas para tu futura cita? "))
    if edadmin < 18:
        print("El furuto prospecto debe ser mayor de edad por politicas del gobierno")
        edadmin =int(input("Por favor coloque una edad permitida: "))
    
    edadmax =int(input("Cual es la edad maxima que buscas para tu futura cita? "))
    if edadmax > 120:
        print("Estas buscando el ataud o que?")
        edadmax =int(input("Por favor coloque una edad permitida: "))

    distancia=int(input("Cuantos kilometros aceptas que este de distancia tu futura pareja? "))

    individuo={"nombre":nombre,"edad":edad,"ciudad":ciudad,"genero":genero,"gbusca":gbusca,"edadmin":edadmin,"edadmax":edadmax,"distancia":distancia}
    return individuo

def RegistrarPersonas(usuario):
    
    N=int(input("Cuantas personas vas a registrar? "))

    for i in range (0,N):
       print("Usuario # ",i)
       usuario.append(GuardarPersonas())
       
       print("\nPersonas registradas correctamente.")

    

def MostrarPersonas(usuario):

    for persona in usuario:
        print(persona)





def main ():
 usuario = []

 while True:
    print ("\n----------------BIENVENIDO A TINDER CUN--------------")
    print ("\nLa mejor plataforma para encontrar el amor")
    print ("\n--MENU--")
    print ("1. Para registrar un nuevo usuario")
    print ("2. Mostrar personas registradas")
    print ("3. Buscar posibles coincidencias")
    print ("4. Mostrar el porcentaje de compatibilidad de cada coincidencia")
    print ("5. Mostrar los intereses que tienen en común")
    print ("6. Identificar cuál es la persona más compatible")
    print ("7. Mostrar las personas que no cumplen los requisitos mínimos de compatibilidad")
    print ("8. Consultar las coincidencias de cualquier persona registrada")
    print("0. Salir")
    
    menu=input("Por favor selecciona una opción: ")
    match menu:
        
        case "1":
         RegistrarPersonas(usuario)

        case "2":
         MostrarPersonas(usuario)

        case "0":
         print("Gracias por utilizar Tinder CUN.")
         break


main()
