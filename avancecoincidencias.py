def GuardarPersonas():
    nombre = input("Cual es tu nombre completo? ")
    edad = int(input("Que edad tienes? "))
    while edad < 18 or edad > 120:
        if edad > 120:
            print("Debes estar vivo para registrarte")
        else:
            print("Debe ser mayor de edad para poder registrarte")
        edad = int(input("Por favor coloque una edad permitida: "))
    ciudad = input("De donde eres? ")
    opciones_genero = ["Masculino", "Femenino", "Otro"]
    while True:
        print("Opciones de genero:", opciones_genero)
        geningresado = input(
            "Cual es tu genero?: "
        ).strip().capitalize()
        if geningresado in opciones_genero:
            break
        print("Opcion no valida. Intenta de nuevo.")
    while True:
        print("Cual es el genero que buscas:", opciones_genero)
        geningresadobusca = input(
            "Cual es el genero que buscas?: "
        ).strip().capitalize()
        if geningresadobusca in opciones_genero:
            break
        print("Opcion no valida. Intenta de nuevo.")
    edadmin = int(input("Cual es la edad minima que buscas para tu futura cita?: "))
    while edadmin < 18 or edadmin > 120:
        if edadmin < 18:
            print("El futuro prospecto debe ser mayor de edad")
        else:
            print("La edad maxima permitida es 120")
        edadmin = int(input("Por favor coloque una edad permitida: "))
    edadmax = int(input("Cual es la edad maxima que buscas para tu futura cita?: "))
    while edadmax < edadmin or edadmax > 120:
        if edadmax < edadmin:
            print("La edad maxima debe ser mayor que la edad minima")
        else:
            print("La edad maxima permitida es 120")
        edadmax = int(input("Por favor coloque una edad permitida: "))
    gustos = input("Ingresa tus hobbies e intereses separados por coma: ")

    # Convertimos los gustos en una lista
    gustos = gustos.lower().split(",")

    # Quitamos los espacios
    gustos = [gusto.strip() for gusto in gustos]

    distancia = int(input("Que tan lejos estarias dispuesto a recorrer por el amor? (km):"))

    individuo = {
        "Nombre": nombre,
        "Edad": edad,
        "Ciudad": ciudad,
        "Genero": geningresado,
        "Genbusca": geningresadobusca,
        "Edadmin": edadmin,
        "Edadmax": edadmax,
        "Gustos": gustos,
        "Distancia": distancia
    }

    return individuo


# PUNTO 1
# REGISTRAR PERSONAS

def RegistrarPersonas(usuario):

    N = int(input("Cuantas personas vas a registrar?: "))
    for i in range(N):

        print("\nUsuario #", i + 1)
        persona = GuardarPersonas()
        usuario.append(persona)
        print("\nPersona registrada correctamente.")


# PUNTO 2
# MOSTRAR PERSONAS

def MostrarPersonas(usuario):

    if len(usuario) == 0:

        print("\nNo hay personas registradas.")

        return

    print("\n--------- PERSONAS REGISTRADAS ---------")

    for persona in usuario:

        print("\n--------------------------")

        print("Nombre:", persona["Nombre"])
        print("Edad:", persona["Edad"])
        print("Ciudad:", persona["Ciudad"])
        print("Genero:", persona["Genero"])
        print("Genero que busca:", persona["Genbusca"])
        print("Edad minima:", persona["Edadmin"])
        print("Edad maxima:", persona["Edadmax"])
        print("Gustos:", persona["Gustos"])
        print("Distancia:", persona["Distancia"], "km")


# PUNTO 3
# BUSCAR POSIBLES COINCIDENCIAS

def BuscarCoincidencias(usuario):

    if len(usuario) < 2:

        print("\nNecesitas registrar minimo 2 personas.")

        return

    print("\n--------- PERSONAS ---------")

    for i in range(len(usuario)):

        print(i + 1,"-",usuario[i]["Nombre"])

    numero = int(
        input("\nSelecciona la persona para buscar posibles coincidencias: "))

    if numero < 1 or numero > len(usuario):

        print("Persona no valida.")

        return

    persona = usuario[numero - 1]

    print("\nBuscando coincidencias para:",persona["Nombre"])

    encontro = False

    for otra in usuario:

        # No comparar una persona consigo misma
        if otra == persona:
            continue

       
        # 1. COMPROBAR EDAD

        edad_compatible = (
            otra["Edad"] >= persona["Edadmin"]
            and
            otra["Edad"] <= persona["Edadmax"]
        )

        # 2. COMPROBAR PREFERENCIA MUTUA

        genero_compatible = (
            persona["Genbusca"] == otra["Genero"]
            and
            otra["Genbusca"] == persona["Genero"]
        )

        # 3. COMPROBAR DISTANCIA

        distancia_compatible = (
            otra["Distancia"] <= persona["Distancia"]
        )

        # 4. BUSCAR INTERESES EN COMUN

        intereses_comunes = []

        for gusto in persona["Gustos"]:

            if gusto in otra["Gustos"]:

                intereses_comunes.append(gusto)

        # COMPROBAR SI ES COINCIDENCIA

        if (
            edad_compatible
            and
            genero_compatible
            and
            distancia_compatible
        ):

            encontro = True

            print("\n--------------------------")

            print(
                "Nombre:",
                otra["Nombre"]
            )

            print(
                "Edad:",
                otra["Edad"]
            )

            print(
                "Ciudad:",
                otra["Ciudad"]
            )

            print(
                "Intereses en comun:",
                intereses_comunes
            )

            print(
                "Edad compatible: Si"
            )

            print(
                "Preferencia compatible: Si"
            )

            print(
                "Distancia compatible: Si"
            )

    if encontro == False:

        print(
            "\nNo se encontraron posibles coincidencias."
        )

# MAIN

def main():

    usuario = []

    while True:

        print("\n---------------- TINDER CUN ----------------")
        print("\nLa mejor plataforma para encontrar el amor")
        print("\n-- MENU --")
        print("1. Para registrar un nuevo usuario")
        print("2. Mostrar personas registradas")
        print("3. Buscar posibles coincidencias")
        print("4. Mostrar el porcentaje de compatibilidad de cada coincidencia")
        print("5. Mostrar los intereses que tienen en común")
        print("6. Identificar cuál es la persona más compatible")
        print("7. Mostrar las personas que no cumplen los requisitos mínimos de compatibilidad")
        print("8. Consultar las coincidencias de cualquier persona")
        print("0. Salir")

        menu = input("\nPor favor selecciona una opcion: ")

        match menu:

            case "1":

                RegistrarPersonas(usuario)

            case "2":

                MostrarPersonas(usuario)

            case "3":

                BuscarCoincidencias(usuario)

            case "4":

                print("\nEsta opcion todavia esta en desarrollo.")

            case "5":

                print("\nEsta opcion todavia esta en desarrollo.")

            case "6":

                print("\nEsta opcion todavia esta en desarrollo.")

            case "7":

                print("\nEsta opcion todavia esta en desarrollo.")

            case "8":

                print("\nEsta opcion todavia esta en desarrollo.")

            case "0":

                print("\nGracias por utilizar Tinder CUN.")

                break

            case _:

                print("\nOpcion no valida. Intenta de nuevo.")


main()
