import archivos 
import busqueda 
import estadistica 
import filtros 
import ordenamiento 
import presentacion 



#BLOQUE PRINCIPAL (MAIN) CON MENÚ INTERACTIVO
def menu_principal():
    # Llamamos al archivo csv
    ruta_csv = "data/PAISES.csv"
    
    # Cargamos el archivo plano directo en la lista de diccionarios
    dataset_paises = archivos.cargar_datos_csv(ruta_csv)
    #Utilizamos un bucle while para pedirle al usuario qe elija la opcion que desee
    #y que siempre lo retorne al menu
    while True:
        print("\n          SISTEMA GESTIÓN DE PAÍSES        ")
        print("1 - Mostrar todos los países")
        print("2 - Buscar por país")
        print("3 - Agregar país con sus datos")
        print("4 - Actualizar datos de país")
        print("5 - Búsqueda personalizada (Filtros)")
        print("6 - Mostrar estadísticas")
        print("7 - Ordenar países")  
        print("8 - Guardar cambios y Salir") 
        
        opcion = input("\nSeleccione una opción (1-8): ").strip()

        if opcion == "1":
            presentacion.opcion_mostrar_todos(dataset_paises)
        elif opcion == "2":
            busqueda.opcion_buscar_por_nombre(dataset_paises)
        elif opcion == "3":
            busqueda.opcion_agregar_pais(dataset_paises)
        elif opcion == "4":
            busqueda.opcion_actualizar_datos(dataset_paises)
        elif opcion == "5":
            filtros.opcion_busqueda_personalizada(dataset_paises)
        elif opcion == "6":
            estadistica.opcion_mostrar_estadisticas(dataset_paises)
        elif opcion == "7":
            ordenamiento.opcion_ordenar_paises(dataset_paises)
        elif opcion == "8":
            archivos.guardar_datos_csv(ruta_csv, dataset_paises)
            print("\nCambios guardados")
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 8.")

if __name__ == "__main__":
    menu_principal()