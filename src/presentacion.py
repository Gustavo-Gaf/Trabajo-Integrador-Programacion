
#Funcion para mostrar los datos de los paises en una tabla
def mostrar_tabla(lista):
    if not lista:
        print("No hay registros para mostrar con ese criterio.")
        return
    print(f"\n{'NOMBRE':<20} | {'POBLACIÓN':<15} | {'SUPERFICIE (km²)':<18} | {'CONTINENTE':<15}")
    print("-" * 75)
    for p in lista:
        print(f"{p['nombre']:<20} | {p['poblacion']:<15,} | {p['superficie']:<18,} | {p['continente']:<15}")

#Funcion para mostrar todos los paises cargados con sus datos
def opcion_mostrar_todos(lista_paises):
    print("\n--- LISTADO DE TODOS LOS PAÍSES ---")
    mostrar_tabla(lista_paises)

