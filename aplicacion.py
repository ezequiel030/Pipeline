# Diccionario vacio para almacenar el nombre de los jugadores y sus goles 
goles = {}
# Lista de jugadores lesionados que no pueden marcar goles bajo ningun concepto
enfermeria = ["Rocha", "Batres", "Cupillar"]

# Menú repetitivo hasta que el usuario decida salir
while True:
    print("\n--- Menú ---")
    print("1. Anotar goles")
    print("2. Consultar jugador")
    print("3. Informe del equipo")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del jugador: ")

        # Verificar si el jugador está en la lista de lesionados
        if nombre in enfermeria:
            print(f"El jugador {nombre} está lesionado y no puede marcar goles.")
            continue

        try:
            cantidad_goles = int(input(f"Ingrese la cantidad de goles marcados por {nombre}: "))
            if cantidad_goles < 0:
                print("La cantidad de goles no puede ser negativa.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        # Registrar los goles en el diccionario
        if nombre in goles:
            goles[nombre] += cantidad_goles
        else:
            goles[nombre] = cantidad_goles
       	    print(f"Goles registrados para {nombre}. Total de goles: {goles[nombre]}")

    elif opcion == "2":
        if not goles:
            print("No hay goles registrados aún.")
        else:
            print("\n--- Goleadores ---")
            for nombre, total_goles in goles.items():
                print(f"{nombre}: {total_goles} goles")

    elif opcion == "3":
        total_goles_equipo = sum(goles.values())
        print(f"\nTotal de goles del equipo: {total_goles_equipo}")
        if goles:
            mejor_goleador = max(goles, key=goles.get)
            print(f"Mejor goleador: {mejor_goleador} con {goles[mejor_goleador]} goles")
        else:
            print("No hay goles registrados para determinar el mejor goleador.")

    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
