
from pathlib import Path

import numpy as np
import xarray as xr


# Localizar la raíz del proyecto a partir de este archivo Python.
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent

ARCHIVO = (
    RAIZ_PROYECTO
    / "data"
    / "raw"
    / "grace"
    / "GRCTellus.JPL.200204_202607.GLO.RL06.3M.MSCNv04CRI.nc"
)


def mostrar_variable(ds, nombre):
    var = ds[nombre]

    print("\n" + "=" * 70)
    print(f"VARIABLE: {nombre}")
    print("Dimensiones:", var.dims)
    print("Forma:", var.shape)
    print("Tipo de dato:", var.dtype)
    print("Unidades:", var.attrs.get("units", "No especificadas"))
    print(
        "Descripción:",
        var.attrs.get("long_name", "No especificada"),
    )
    print("Atributos completos:")

    for clave, valor in var.attrs.items():
        print(f"  {clave}: {valor}")

    if nombre in ("land_mask", "mascon_ID"):
        valores = np.asarray(var.values)
        valores = valores[np.isfinite(valores)]

        unicos, conteos = np.unique(
            valores,
            return_counts=True,
        )

        print("Cantidad de valores únicos:", len(unicos))
        print("Primeras 15 categorías y frecuencias:")

        for valor, cantidad in zip(unicos[:15], conteos[:15]):
            print(f"  {valor}: {cantidad:,}")


def main():
    print("INSPECCIÓN DEL ARCHIVO GRACE")
    print("=" * 70)
    print("Raíz del proyecto:", RAIZ_PROYECTO)
    print("Archivo:", ARCHIVO)

    if not ARCHIVO.exists():
        print("\nERROR: no se encontró el archivo NetCDF.")
        print("Verificá que exista en data/raw/grace.")
        return

    with xr.open_dataset(ARCHIVO) as ds:
        print("\nDIMENSIONES DEL DATASET")
        for nombre, cantidad in ds.sizes.items():
            print(f"  {nombre}: {cantidad:,}")

        print("\nVARIABLES Y COORDENADAS")
        print("Variables:", list(ds.data_vars))
        print("Coordenadas:", list(ds.coords))

        for nombre in [
            "land_mask",
            "mascon_ID",
            "scale_factor",
            "lwe_thickness",
            "uncertainty",
        ]:
            if nombre in ds:
                mostrar_variable(ds, nombre)

        print("\nRANGO DE COORDENADAS")

        for nombre in ("lat", "lon", "time"):
            if nombre in ds.coords:
                coord = ds[nombre]
                print(
                    f"  {nombre}: "
                    f"{coord.min().values} a {coord.max().values}"
                )

        print("\nMETADATOS GLOBALES RELEVANTES")

        for clave in [
            "title",
            "summary",
            "time_coverage_start",
            "time_coverage_end",
            "months_missing",
            "time_mean_removed",
        ]:
            if clave in ds.attrs:
                print(f"  {clave}: {ds.attrs[clave]}")

    print("\nInspección finalizada.")


if __name__ == "__main__":
    main()
