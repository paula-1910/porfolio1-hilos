import threading
import time
import random

# Variable compartida para contar descargas completadas
total_descargas = 0

# Lock para evitar condiciones de carrera
lock = threading.Lock()


def descargar_archivo(nombre):
    """
    Simula la descarga de un archivo mostrando progreso en porcentaje.
    El tiempo de descarga es aleatorio.
    """
    global total_descargas

    tamaño = random.randint(3, 7)  # segundos simulados de descarga
    print(f"Iniciando descarga de {nombre}...")

    # Mostrar progreso en 10 pasos (10% cada uno)
    for i in range(1, 11):
        time.sleep(tamaño / 10)
        print(f"Descargando {nombre} [{i * 10}%]...")

    print(f"Descarga de {nombre} completada.")

    # Zona crítica protegida con Lock
    with lock:
        total_descargas += 1


def main():
    archivos = ["Archivo1.zip", "Archivo2.zip", "Archivo3.zip"]

    hilos = []

    # Crear e iniciar hilos
    for nombre in archivos:
        hilo = threading.Thread(target=descargar_archivo, args=(nombre,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print(f"\nTotal de descargas completadas: {total_descargas}")


if __name__ == "__main__":
    main()
