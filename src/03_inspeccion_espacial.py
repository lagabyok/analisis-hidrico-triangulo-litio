
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr


RAIZ = Path(__file__).resolve().parent.parent

ARCHIVO = (
    RAIZ
    / "data"
    / "raw"
    / "grace"
    / "GRCTellus.JPL.200204_202607.GLO.RL06.3M.MSCNv04CRI.nc"
)

SALIDA = RAIZ / "outputs" / "eda_grace"
SALIDA.mkdir(parents=True, exist_ok=True)


def resumen_variable(var):
    valores = np.asarray(var.values)
    finitos = valores[np.isfinite(valores)]

    if finitos.size == 0:
        return {
            "valores_validos": 0,
            "valores_faltantes": valores.size,
            "minimo": np.nan,
            "maximo": np.nan,
        }

    return {
        "valores_validos": int(finitos.size),
        "valores_faltantes": int(valores.size - finitos.size),
        "minimo": float(finitos.min()),
        "maximo": float(finitos.max()),
    }


def main():
    if not ARCHIVO.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ARCHIVO}"
        )

    with xr.open_dataset(ARCHIVO) as original:
        # Trabajar con una copia en memoria; no modificar el archivo.
        ds = original.assign_coords(
            lon=((original.lon + 180) % 360) - 180
        ).sortby("lon")

        print("=" * 70)
        print("INSPECCIÓN ESPACIAL PRELIMINAR DE GRACE")
        print("=" * 70)

        # Ventana amplia de exploración en el noroeste de Sudamérica.
        # No representa límites provinciales ni cuencas hidrogeológicas.
        region = ds.sel(
            lon=slice(-75, -60),
            lat=slice(-40, -15),
        )

        print("\nTamaño de la ventana exploratoria:")
        print(dict(region.sizes))

        print("\nRango de coordenadas:")
        print(
            "Longitud:",
            float(region.lon.min()),
            "a",
            float(region.lon.max()),
        )
        print(
            "Latitud:",
            float(region.lat.min()),
            "a",
            float(region.lat.max()),
        )

        resultados = []

        for nombre in [
            "land_mask",
            "scale_factor",
            "mascon_ID",
        ]:
            var = region[nombre]
            resumen = resumen_variable(var)

            resultados.append({
                "variable": nombre,
                **resumen,
            })

            print(f"\n{nombre}:")
            print("  Valores válidos:", resumen["valores_validos"])
            print("  Valores faltantes:", resumen["valores_faltantes"])
            print("  Mínimo:", resumen["minimo"])
            print("  Máximo:", resumen["maximo"])

            if nombre in ["land_mask", "mascon_ID"]:
                valores = np.asarray(var.values)
                valores = valores[np.isfinite(valores)]

                unicos, conteos = np.unique(
                    valores,
                    return_counts=True,
                )

                print("  Valores únicos:", len(unicos))
                print("  Primeras 20 frecuencias:")

                for valor, cantidad in zip(
                    unicos[:20],
                    conteos[:20],
                ):
                    print(f"    {valor}: {cantidad:,}")

        # Cobertura temporal de la variable principal en la ventana.
        agua = region["lwe_thickness"]
        celdas_validas_por_mes = (
            np.isfinite(agua)
            .sum(dim=("lat", "lon"))
            .values
        )

        tabla_tiempo = pd.DataFrame({
            "fecha": pd.to_datetime(region.time.values),
            "celdas_validas": celdas_validas_por_mes,
        })

        tabla_tiempo["celdas_validas"] = (
            tabla_tiempo["celdas_validas"].astype(int)
        )

        tabla_tiempo.to_csv(
            SALIDA / "cobertura_temporal_ventana.csv",
            index=False,
        )

        pd.DataFrame(resultados).to_csv(
            SALIDA / "resumen_espacial_ventana.csv",
            index=False,
        )

        print("\nCobertura temporal de lwe_thickness:")
        print(
            "Mínimo de celdas válidas por mes:",
            int(tabla_tiempo["celdas_validas"].min()),
        )
        print(
            "Máximo de celdas válidas por mes:",
            int(tabla_tiempo["celdas_validas"].max()),
        )
        print(
            "Meses con cero celdas válidas:",
            int((tabla_tiempo["celdas_validas"] == 0).sum()),
        )

        print("\nArchivos guardados en:", SALIDA)
        print("- resumen_espacial_ventana.csv")
        print("- cobertura_temporal_ventana.csv")


if __name__ == "__main__":
    main()
