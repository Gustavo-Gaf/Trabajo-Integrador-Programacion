from presentacion import mostrar_tabla

#Funcion para ordenar los paises por diferentes criterios y sentidos
def opcion_ordenar_paises(lista_paises):
    if not lista_paises: #Validamos que la lista no este vacia
        print("No hay datos cargados para ordenar.")
        return

    #Le preguntamos al usuario como desea ordenar la lista
    print("\n--- CRITERIOS DE ORDENAMIENTO ---")
    print("1. Ordenar por Nombre")
    print("2. Ordenar por Población")
    print("3. Ordenar por Superficie")
    
    opcion_criterio = input("Seleccione una opción de campo (1-3): ").strip()
    
    # Asignamos la clave del diccionario según lo elegido
    if opcion_criterio == "1":
        clave = "nombre"
    elif opcion_criterio == "2":
        clave = "poblacion"
    elif opcion_criterio == "3":
        clave = "superficie"
    else:
        print("Opción inválida. Volviendo al menú principal.")
        return

    # Validamos el sentido del orden con un bucle hasta que ponga una opción correcta
    while True:
        print("\n¿En qué sentido desea ordenar?")
        print("a. Ascendente (Menor a Mayor / A-Z)")
        print("b. Descendente (Mayor a Menor / Z-A)")
        sentido = input("Seleccione sentido (a/b): ").strip().lower()
        
        if sentido in ("a", "b"):
            break
        else:
            print("Opción inválida. Por favor, ingrese únicamente 'a' o 'b'.")

    # Definimos si es reverso (True para descendente, False para ascendente)
    orden_reverso = True if sentido == "b" else False

    # Si es texto (nombre) lo pasamos a minúsculas temporalmente al ordenar para que no interfieran las mayúsculas
    if clave == "nombre":
        lista_ordenada = sorted(lista_paises, key=lambda x: x["nombre"].lower(), reverse=orden_reverso)
    else:
        lista_ordenada = sorted(lista_paises, key=lambda x: x[clave], reverse=orden_reverso)

    # Mostramos el resultado final usando la función de tabla
    print(f"\n--- LISTADO ORDENADO POR {clave.upper()} ({'DESCENDENTE' if orden_reverso else 'ASCENDENTE'}) ---")
    mostrar_tabla(lista_ordenada)
