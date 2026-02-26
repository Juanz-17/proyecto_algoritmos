import requests
import os

def descargar_datos(simbolo: str):
    """
    Descarga datos históricos desde Stooq en formato CSV
    """
    url = f"https://stooq.com/q/d/l/?s={simbolo}&i=d"
    print(f"Descargando datos de: {simbolo}")

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error al descargar datos")

    return response.text


def guardar_csv(contenido: str, ruta: str):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)


if __name__ == "__main__":
    data = descargar_datos("aapl.us")

    ruta_salida = "../data/datos.csv"
    guardar_csv(data, ruta_salida)

    print("Archivo guardado correctamente en backend/data/datos.csv")