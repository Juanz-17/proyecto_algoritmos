import pandas as pd

def cargar_datos(ruta_csv: str):
    print("Cargando datos...")
    df = pd.read_csv(ruta_csv)
    print(f"Datos cargados: {len(df)} filas")
    return df


def limpiar_datos(df: pd.DataFrame):
    print("Limpiando datos...")

    # Convertir fecha a formato datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Ordenar por fecha
    df = df.sort_values("Date")

    # Eliminar valores nulos
    df = df.dropna()

    print("Datos limpios.")
    return df


if __name__ == "__main__":
    ruta = "../data/datos.csv"

    df = cargar_datos(ruta)
    df = limpiar_datos(df)

    print(df.head())