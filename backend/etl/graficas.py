import pandas as pd
import time
import matplotlib.pyplot as plt


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

    tamaños = [100, 500, 1000, 2000, 5000, 10000]

    tiempos_lineal = []
    tiempos_binaria = []

    for n in tamaños:
        subset = fechas[:n]
        objetivo = subset[-1]

        # Lineal
        inicio = time.time()
        busqueda_lineal(subset, objetivo)
        fin = time.time()
        tiempos_lineal.append(fin - inicio)

        # Binaria
        inicio = time.time()
        busqueda_binaria(subset, objetivo)
        fin = time.time()
        tiempos_binaria.append(fin - inicio)

    plt.plot(tamaños, tiempos_lineal, label="Búsqueda Lineal")
    plt.plot(tamaños, tiempos_binaria, label="Búsqueda Binaria")

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de complejidad temporal")
    plt.legend()
    plt.show()