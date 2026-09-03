def GuardarPersonas():

    nombre= input("Como te llamas? ")
    edad= int(input("Que edad tienes? "))
    while  edad <18 or edad > 120:
        if edad > 120 :
            print (" Debes estar vivo para registrarte")
            edad=int(input("Por favor coloque una edad permitida: ") )
        else:
            print("Debe ser mayor de edad para poder registrarte")
            edad=int(input("Por favor coloque una edad permitida: ") )
        
    ciudad= input("De donde eres? ")
    genero= input("Cual es tu genero? ")
    gbusca= input("Que genero busca? ")
    edadmin =int (input("Cual es la edad minima que buscas para tu futura cita? "))
    while edadmin < 18 or edadmin > 120:
        if edadmin < 18:
            print("El furuto prospecto debe ser mayor de edad por politicas del gobierno")
            edadmin =int(input("Por favor coloque una edad permitida: "))
        else:
            print ("tu futura pareja minimo debe estar viva")
            edadmin=int(input("Por favor coloque una edad permitida: ") )
            
    edadmax =int(input("Cual es la edad maxima que buscas para tu futura cita? "))
    while edadmax < 18 or edadmax > 120:
        if edadmax < 18:
            print("El furuto prospecto debe ser mayor de edad por politicas del gobierno")
            edadmax =int(input("Por favor coloque una edad permitida: "))
        elif edadmax < edadmin:
            print("La edad maxima de tu pareja debe ser mayor a la edad minima")
            edadmax =int(input("Por favor coloque una edad mayor a la edad minima de tu pareja: "))
            
        elif edadmax > 120:
            print ("tu futura pareja debe estar viva")
            edadmax=int(input("Por favor coloque una edad permitida: ") )
    
        

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
