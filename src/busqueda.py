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

    try:
        # 1. Validamos si el país ya existe ANTES de pedir los demás datos
        # Usamos .lower() para que "Argentina" y "argentina" se consideren iguales
        for pais in lista_paises:
            if pais["nombre"].lower() == nombre.lower():
                # Levantamos manualmente un ValueError con un mensaje personalizado
                raise ValueError("El país ya se encuentra registrado.")

        # Se le pide al usuario que ingrese los datos y se capturan los datos inválidos
        poblacion = int(input("Población (entero): "))
        superficie = int(input("Superficie en km² (entero): "))
        
        if poblacion <= 0 or superficie <= 0:
            print("Error: Los valores deben ser mayores a cero.")
            return
            
    except ValueError as e:
        # Si el error es por el país duplicado, 'e' contendrá el texto que pusimos en el raise
        if str(e) == "El país ya se encuentra registrado.":
            print(f"Error: {e}")
        else:
            # Si el error fue porque ingresaron letras en población o superficie
            print("Error: Debe ingresar un número entero válido.")
        return

    continente = input("Continente: ").strip()
    if not continente:
        print("Error: No se permiten campos vacíos.")
        return

    lista_paises.append({
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

