from presentacion import mostrar_tabla

#Funcion que le permite al usuario buscar un pais por nombre
def opcion_buscar_por_nombre(lista_paises):
    print("\n--- BUSCAR POR PAÍS ---")
    busqueda = input("Ingrese el nombre del país a buscar: ").strip().lower()
    if not busqueda:
        print("Error: No se encuentra el pais.")
        return
    resultados = [p for p in lista_paises if busqueda in p["nombre"].lower()]
    mostrar_tabla(resultados)
    
#Funcion para agregar un pais a la lista,  se debe agregar con los datos de poblacion
#superficie y continente
def opcion_agregar_pais(lista_paises):
    print("\n--- AGREGAR PAÍS CON SUS DATOS ---")
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("Error: No se permiten campos vacíos.")
        return
    try:    #Se le pide al usuario que ingrese los datos y se capturan los datos invalidos y se imprime el error mediante except
        poblacion = int(input("Población (entero): "))
        superficie = int(input("Superficie en km² (entero): "))
        if poblacion <= 0 or superficie <= 0:
            print("Error: Los valores deben ser mayores a cero.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return
    continente = input("Continente: ").strip()
    if not continente:
        print("Error: No se permiten campos vacíos.")
        return

    lista_paises.append({   #Se agrega el pais ingresado por el usuario al final de la lista
        "nombre": nombre, "poblacion": poblacion, 
        "superficie": superficie, "continente": continente
    })
    print(f"{nombre} guardado temporalmente en memoria.")

#Funcion para modificar los datos de los paises
#Solo se permite actualizar Poblacion y Superficie
def opcion_actualizar_datos(lista_paises):
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")
    nombre_buscar = input("Ingrese el nombre exacto del país a modificar: ").strip().lower()
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar:
            try:
                nueva_pob = int(input(f"Nueva población (Actual: {pais['poblacion']}): "))
                nueva_sup = int(input(f"Nueva superficie (Actual: {pais['superficie']}): "))
                if nueva_pob <= 0 or nueva_sup <= 0: #Validamos que los ingresos sean mayores a cero
                    print("Error: Los números deben ser mayores a cero.")
                    return
                pais["poblacion"] = nueva_pob
                pais["superficie"] = nueva_sup
                print(f"Datos de {pais['nombre']} actualizados.")
                return
            except ValueError:
                print("Error: Entrada inválida.")
                return
    print("No se encontró el país.")

