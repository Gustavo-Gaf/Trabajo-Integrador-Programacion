import csv
#Funcion para cargar los datos del csv al codigo
def cargar_datos_csv(ruta_archivo):
  
    lista_paises = []   
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=',')
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                lista_paises.append(pais)
        print(f"Éxito: Se cargaron {len(lista_paises)} países desde {ruta_archivo}.")
    except (ValueError, KeyError):
        print("El formato interno del archivo CSV es incorrecto.")
    return lista_paises

#Guarda los cambios de la memoria de vuelta al archivo de Excel en formato plano cuando el usuario elije
#la opcion guardar y salir
def guardar_datos_csv(ruta_archivo, lista_paises):
    
    try:
        with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=',')
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
        print("Datos guardados de forma permanente en el archivo plano.")
    except Exception as e:
        print(f"No se pudieron guardar los cambios: {e}")