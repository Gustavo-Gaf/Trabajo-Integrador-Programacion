from presentacion import mostrar_tabla

#Funcion para buscar un pais en especifico mediante entrada del usuario
def opcion_busqueda_personalizada(lista_paises):
    print("\n--- BÚSQUEDA PERSONALIZADA ---")
    print("1. Buscar por Continente")
    print("2. Buscar por Población (Mayor/Menor)")
    print("3. Buscar por Superficie (Mayor/Menor)")
    
    opcion_filtro = input("Seleccione una opción: ").strip()
    #Opcion si desea buscar por continente
    if opcion_filtro == "1":
        continente_buscado = input("Ingrese continente: ").strip().lower()
        
        # Creamos una lista vacía para ir guardando los resultados
        resultados = []
        
        # Recorremos los países uno por uno
        for p in lista_paises:
            if p["continente"].lower() == continente_buscado:
                resultados.append(p)
                
        mostrar_tabla(resultados)
        
    elif opcion_filtro in ("2", "3"):
        clave = "poblacion" if opcion_filtro == "2" else "superficie"
        
        #Creamos un bucle para que el usuario decida como quiere hacer la busqueda
        while True: 
            print(f"\n¿Qué criterio desea aplicar para {clave}?")
            print("a. Mayor que un valor")
            print("b. Menor que un valor")
            criterio = input("Seleccione criterio (a/b): ").strip().lower()
            
            if criterio in ("a", "b"):
                break  # Rompe el bucle porque la opción es correcta
            else:
                print("Opción inválida. Por favor, ingrese únicamente 'a' o 'b'.")

        # Una vez validado el criterio, pedimos el número
        try:
            limite = int(input(f"Ingrese el valor entero de corte para {clave}: "))
            if criterio == "a":
                resultados = [p for p in lista_paises if p[clave] > limite]
            else:
                resultados = [p for p in lista_paises if p[clave] < limite]
            mostrar_tabla(resultados)
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            
    else:
        print("Opción de submenú inválida. Volviendo al menú principal.")