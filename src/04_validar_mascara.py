
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


def main():
    if not ARCHIVO.exists():
        raise FileNotFoundError(f"No existe el archivo: {ARCHIVO}")

    with xr.open_dataset(ARCHIVO) as ds:
        # Ventana exploratoria utilizada en el paso anterior.
        region = ds.sel(
            lon=slice(285.25, 299.75),
            lat=slice(-39.75, -15.25),
        )

        mascara = region["land_mask"]
        factor = region["scale_factor"]

        tierra = mascara == 1
        no_tierra = mascara == 0
        factor_faltante = ~np.isfinite(factor)

        print("=" * 70)
        print("VALIDACIÓN DE MÁSCARA Y FACTORES ESPACIALES")
        print("=" * 70)

        print("\nCantidad de celdas:")
        print("Total:", mascara.size)
        print("land_mask = 1:", int(tierra.sum().item()))
        print("land_mask = 0:", int(no_tierra.sum().item()))
        print(
            "scale_factor faltante:",
            int(factor_faltante.sum().item()),
        )

        # Tabla cruzada espacial entre máscara y faltantes.
        combinaciones = [
            ("Tierra (mask=1)", tierra),
            ("Fuera de máscara terrestre (mask=0)", no_tierra),
        ]

        filas = []

        for etiqueta, seleccion in combinaciones:
            total = int(seleccion.sum().item())
            faltantes = int(
                (seleccion & factor_faltante).sum().item()
            )
            disponibles = total - faltantes

            filas.append({
                "categoria_mascara": etiqueta,
                "total_celdas": total,
                "scale_factor_disponible": disponibles,
                "scale_factor_faltante": faltantes,
            })

            print(f"\n{etiqueta}:")
            print("  Total:", total)
            print("  Factor disponible:", disponibles)
            print("  Factor faltante:", faltantes)

        tabla = pd.DataFrame(filas)
        tabla.to_csv(
            SALIDA / "validacion_mascara_scale_factor.csv",
            index=False,
        )

        faltantes_en_tierra = int(
            (tierra & factor_faltante).sum().item()
        )
        faltantes_fuera = int(
            (no_tierra & factor_faltante).sum().item()
        )

        coincidencia_exacta = (
            faltantes_en_tierra == 0
            and faltantes_fuera == int(no_tierra.sum().item())
        )

        print("\n¿Los faltantes coinciden exactamente con mask=0?")
        print("Resultado:", coincidencia_exacta)

        # Identificar huecos en la secuencia mensual.
        fechas = pd.DatetimeIndex(
            pd.to_datetime(ds["time"].values)
        )

        meses_observados = set(fechas.to_period("M"))
        meses_esperados = pd.period_range(
            start=fechas.min().to_period("M"),
            end=fechas.max().to_period("M"),
            freq="M",
        )

        meses_faltantes = [
            str(mes)
            for mes in meses_esperados
            if mes not in meses_observados
        ]

        print("\nCobertura temporal:")
        print("Meses con registros:", len(meses_observados))
        print("Meses del calendario:", len(meses_esperados))
        print("Meses sin registro:", len(meses_faltantes))
        print(meses_faltantes)

        pd.DataFrame({
            "mes_faltante": meses_faltantes
        }).to_csv(
            SALIDA / "meses_sin_registro.csv",
            index=False,
        )

        print("\nResultados guardados en:")
        print(SALIDA)
        print("- validacion_mascara_scale_factor.csv")
        print("- meses_sin_registro.csv")


if __name__ == "__main__":
    main()
