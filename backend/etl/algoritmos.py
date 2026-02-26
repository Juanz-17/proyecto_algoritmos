import pandas as pd
import time

def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    return df


def busqueda_lineal(fechas, objetivo):
    for i in range(len(fechas)):
        if fechas[i] == objetivo:
            return i
    return -1


def busqueda_binaria(fechas, objetivo):
    izquierda = 0
    derecha = len(fechas) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if fechas[medio] == objetivo:
            return medio
        elif fechas[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


if __name__ == "__main__":
    ruta = "../data/datos.csv"
    df = cargar_datos(ruta)

    fechas = list(df["Date"])

    objetivo = fechas[len(fechas)//2]  # fecha en la mitad del dataset

    # Búsqueda lineal
    inicio = time.time()
    pos_lineal = busqueda_lineal(fechas, objetivo)
    fin = time.time()

    tiempo_lineal = fin - inicio

    # Búsqueda binaria
    inicio = time.time()
    pos_binaria = busqueda_binaria(fechas, objetivo)
    fin = time.time()

    tiempo_binaria = fin - inicio

    print("Resultado búsqueda:")
    print(f"Búsqueda lineal → Posición: {pos_lineal}, Tiempo: {tiempo_lineal:.8f} s")
    print(f"Búsqueda binaria → Posición: {pos_binaria}, Tiempo: {tiempo_binaria:.8f} s")