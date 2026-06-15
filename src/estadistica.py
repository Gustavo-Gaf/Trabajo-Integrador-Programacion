from presentacion import mostrar_tabla


# Estas funciones reciben país y devuelven el valor para comparar

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]

#Funcion para mostrar las estadisticas de los paises
def opcion_mostrar_estadisticas(lista_paises):
    if not lista_paises:    # Verificamos que haya una lista cargada
        print("No hay datos cargados.")
        return
    
    print("\n                REPORTE DE ESTADÍSTICAS                \n")
    
    # Buscamos los minimos y maximos de poblacion y superficie
    max_pob = max(lista_paises, key=obtener_poblacion)
    min_pob = min(lista_paises, key=obtener_poblacion)
    max_sup = max(lista_paises, key=obtener_superficie)
    min_sup = min(lista_paises, key=obtener_superficie)

    print(f"• País con MAYOR Población:  {max_pob['nombre']} ({max_pob['poblacion']:,} hab.)")
    print(f"• País con MENOR Población:  {min_pob['nombre']} ({min_pob['poblacion']:,} hab.)")
    print(f"• País con MAYOR Superficie: {max_sup['nombre']} ({max_sup['superficie']:,} km²)")
    print(f"• País con MENOR Superficie: {min_sup['nombre']} ({min_sup['superficie']:,} km²)")

    # Promedios
    total_pob = sum(p["poblacion"] for p in lista_paises)
    total_sup = sum(p["superficie"] for p in lista_paises)
    cant = len(lista_paises)

    print(f"• Promedio de población general: {total_pob / cant:.2f} habitantes")
    print(f"• Promedio de población por superficie: {total_pob / total_sup:.4f} hab/km²")

    # Diccionario para contar por continente
    conteo = {}
    for p in lista_paises:
        conteo[p["continente"]] = conteo.get(p["continente"], 0) + 1

    print("\n• Cantidad de países por continente:")
    for continente, cantidad in conteo.items():
        print(f"  - {continente}: {cantidad} países")