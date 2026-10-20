
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt


# ============================================================
# 1. CONFIGURACIÓN
# ============================================================

RAIZ = Path(__file__).resolve().parents[1]

ARCHIVO = (
    RAIZ
    / "data"
    / "raw"
    / "grace"
    / "GRCTellus.JPL.200204_202607.GLO.RL06.3M.MSCNv04CRI.nc"
)

SALIDA = RAIZ / "outputs" / "eda_grace"
GRAFICOS = SALIDA / "graficos"

SALIDA.mkdir(parents=True, exist_ok=True)
GRAFICOS.mkdir(parents=True, exist_ok=True)

SEMILLA = 2026
MAX_MUESTRA = 200_000

rng = np.random.default_rng(SEMILLA)


# ============================================================
# 2. FUNCIONES AUXILIARES
# ============================================================

def guardar_csv(registros, nombre):
    """Guarda una lista de diccionarios en CSV."""
    pd.DataFrame(registros).to_csv(
        SALIDA / nombre,
        index=False,
        encoding="utf-8-sig"
    )


def muestra_valida(variable, max_valores=MAX_MUESTRA):
    """
    Obtiene una muestra reproducible de valores finitos.
    No carga intencionalmente toda la variable en memoria.
    """
    valores = np.asarray(variable.values).ravel()

    if valores.size == 0:
        return np.array([])

    paso = max(1, int(np.ceil(valores.size / max_valores)))
    candidatos = valores[::paso]
    candidatos = candidatos[np.isfinite(candidatos)]

    if candidatos.size > max_valores:
        indices = rng.choice(
            candidatos.size,
            size=max_valores,
            replace=False
        )
        candidatos = candidatos[indices]

    return candidatos


def estadisticas_muestra(valores):
    """Calcula estadísticas sobre la muestra finita disponible."""
    if len(valores) == 0:
        return {
            "n_muestra": 0,
            "media": np.nan,
            "mediana": np.nan,
            "desvio_std": np.nan,
            "varianza": np.nan,
            "minimo": np.nan,
            "q1": np.nan,
            "q2": np.nan,
            "q3": np.nan,
            "maximo": np.nan,
            "asimetria": np.nan,
            "curtosis": np.nan,
            "limite_inferior_iqr": np.nan,
            "limite_superior_iqr": np.nan,
            "outliers_iqr_muestra": np.nan,
        }

    s = pd.Series(valores, dtype="float64")
    q1 = s.quantile(0.25)
    q2 = s.quantile(0.50)
    q3 = s.quantile(0.75)
    iqr = q3 - q1

    inferior = q1 - 1.5 * iqr
    superior = q3 + 1.5 * iqr

    return {
        "n_muestra": len(s),
        "media": s.mean(),
        "mediana": s.median(),
        "desvio_std": s.std(),
        "varianza": s.var(),
        "minimo": s.min(),
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "maximo": s.max(),
        "asimetria": s.skew(),
        "curtosis": s.kurt(),
        "limite_inferior_iqr": inferior,
        "limite_superior_iqr": superior,
        "outliers_iqr_muestra": int(
            ((s < inferior) | (s > superior)).sum()
        ),
    }


# ============================================================
# 3. VALIDACIÓN INICIAL
# ============================================================

if not ARCHIVO.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo esperado: {ARCHIVO}"
    )

print("=" * 65)
print("EDA INICIAL — GRACE / GRACE-FO")
print("=" * 65)
print("Archivo:", ARCHIVO)
print("Tamaño MB:", round(ARCHIVO.stat().st_size / 1_000_000, 2))


# ============================================================
# 4. APERTURA Y ESTRUCTURA GENERAL
# ============================================================

lineas = []
reg_variables = []
reg_faltantes = []
reg_estadisticas = []
reg_cardinalidad = []
reg_muestras = []

with xr.open_dataset(ARCHIVO) as ds:

    # --------------------------------------------------------
    # 4.1 Dimensiones
    # --------------------------------------------------------

    print("\nDIMENSIONES")
    print(ds.sizes)

    lineas.append("EDA INICIAL DEL ARCHIVO GRACE")
    lineas.append(f"Archivo: {ARCHIVO.name}")
    lineas.append(
        f"Tamaño: {ARCHIVO.stat().st_size / 1_000_000:.2f} MB"
    )
    lineas.append("\nDIMENSIONES")

    for dimension, cantidad in ds.sizes.items():
        texto = f"{dimension}: {cantidad}"
        print(texto)
        lineas.append(texto)

    lineas.append("\nMETADATOS GLOBALES")
    for clave, valor in ds.attrs.items():
        lineas.append(f"{clave}: {valor}")

    # --------------------------------------------------------
    # 4.2 Variables, tipos y dimensiones
    # --------------------------------------------------------

    print("\nVARIABLES Y TIPOS")

    for nombre, var in ds.variables.items():

        if nombre in ds.coords:
            tipo_variable = "coordenada"
        else:
            tipo_variable = "variable de datos"

        registro = {
            "nombre": nombre,
            "tipo": tipo_variable,
            "dtype": str(var.dtype),
            "dimensiones": ", ".join(var.dims),
            "cantidad_elementos": var.size,
            "unidades": var.attrs.get("units", ""),
            "descripcion": var.attrs.get(
                "long_name",
                var.attrs.get("standard_name", "")
            ),
            "atributos": str(dict(var.attrs)),
        }

        reg_variables.append(registro)

        print(
            f"- {nombre}: {var.dtype}; "
            f"dimensiones={var.dims}; "
            f"unidades={var.attrs.get('units', 'no especificadas')}"
        )

    # --------------------------------------------------------
    # 4.3 Fechas y coordenadas repetidas
    # --------------------------------------------------------

    lineas.append("\nCOORDENADAS TEMPORALES Y ESPACIALES")

    for nombre in ("time", "lat", "lon"):

        if nombre not in ds.coords:
            continue

        coord = np.asarray(ds[nombre].values)
        repetidos = int(pd.Index(coord).duplicated().sum())

        registro = {
            "variable": nombre,
            "cantidad": coord.size,
            "duplicados": repetidos,
            "primer_valor": str(coord[0]) if coord.size else "",
            "ultimo_valor": str(coord[-1]) if coord.size else "",
        }

        reg_cardinalidad.append(registro)
        lineas.append(str(registro))

        print(registro)

    # --------------------------------------------------------
    # 4.4 Faltantes por variable
    # --------------------------------------------------------

    print("\nFALTANTES")

    for nombre, var in ds.variables.items():

        # Las variables de bounds se inspeccionan también,
        # pero no se confunden con mediciones científicas.
        cantidad = int(var.isnull().sum().compute().item())
        total = var.size
        porcentaje = 100 * cantidad / total if total else np.nan

        reg_faltantes.append({
            "variable": nombre,
            "elementos_totales": total,
            "faltantes": cantidad,
            "porcentaje_faltantes": porcentaje,
            "dtype": str(var.dtype),
            "dimensiones": ", ".join(var.dims),
        })

        print(
            f"{nombre}: {cantidad:,}/{total:,} "
            f"({porcentaje:.4f} %)"
        )

    # --------------------------------------------------------
    # 4.5 Cardinalidad y variables constantes
    # --------------------------------------------------------

    print("\nCARDINALIDAD Y VARIANZA CERO")

    for nombre, var in ds.variables.items():

        # Cardinalidad exacta en variables pequeñas y
        # categóricas/identificadoras.
        es_candidata = (
            nombre in ("land_mask", "mascon_ID")
            or nombre in ("time", "lat", "lon")
        )

        if not es_candidata:
            continue

        valores = np.asarray(var.values).ravel()
        unicos = np.unique(valores[~pd.isna(valores)])

        registro = {
            "variable": nombre,
            "elementos": valores.size,
            "valores_unicos": len(unicos),
            "constante": len(unicos) <= 1,
            "proporcion_unicos": (
                len(unicos) / valores.size
                if valores.size else np.nan
            ),
        }

        reg_cardinalidad.append(registro)
        print(registro)

    # --------------------------------------------------------
    # 4.6 Muestra cruda: primeros, últimos y aleatorios
    # --------------------------------------------------------

    print("\nMUESTRA DE VALORES")

    for nombre in ("lwe_thickness", "uncertainty", "GAD"):

        if nombre not in ds.data_vars:
            continue

        var = ds[nombre]
        valores = np.asarray(var.values).ravel()

        primeros = valores[:10]
        ultimos = valores[-10:]

        muestra = muestra_valida(var, max_valores=100)

        print(f"\n{nombre}")
        print("Primeros 10:", primeros)
        print("Últimos 10:", ultimos)
        print("Muestra aleatoria de hasta 100:", muestra[:100])

        for tipo_muestra, conjunto in (
            ("primeros", primeros),
            ("ultimos", ultimos),
            ("aleatorios", muestra[:100]),
        ):
            for posicion, valor in enumerate(conjunto):
                reg_muestras.append({
                    "variable": nombre,
                    "tipo_muestra": tipo_muestra,
                    "posicion_muestra": posicion,
                    "valor": valor.item()
                    if hasattr(valor, "item") else valor,
                })

    # --------------------------------------------------------
    # 4.7 Estadísticas univariadas de variables científicas
    # --------------------------------------------------------

    print("\nESTADÍSTICAS UNIVARIADAS")

    variables_cientificas = (
        "lwe_thickness",
        "uncertainty",
        "GAD",
    )

    for nombre in variables_cientificas:

        if nombre not in ds.data_vars:
            continue

        var = ds[nombre]
        valores = muestra_valida(var)
        estadisticas = estadisticas_muestra(valores)

        registro = {
            "variable": nombre,
            "unidades": var.attrs.get("units", ""),
            "metodo": (
                "muestra sistemática de la grilla "
                "con límite de tamaño"
            ),
            **estadisticas,
        }

        reg_estadisticas.append(registro)

        print(f"\n{nombre}")
        for clave, valor in estadisticas.items():
            print(f"  {clave}: {valor}")

        # ----------------------------------------------------
        # 4.8 Histogramas y boxplots
        # ----------------------------------------------------

        if len(valores) == 0:
            warnings.warn(f"{nombre}: no hay valores finitos.")
            continue

        unidades = var.attrs.get("units", "")

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.hist(valores, bins=60)
        ax.set_title(
            f"Distribución de {nombre} (muestra exploratoria)"
        )
        ax.set_xlabel(f"{nombre} ({unidades})")
        ax.set_ylabel("Frecuencia")
        ax.grid(axis="y", alpha=0.25)
        fig.tight_layout()
        fig.savefig(
            GRAFICOS / f"distribucion_{nombre}.png",
            dpi=150
        )
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(9, 3.5))
        ax.boxplot(valores, vert=False, showfliers=True)
        ax.set_title(
            f"Boxplot de {nombre} (muestra exploratoria)"
        )
        ax.set_xlabel(f"{nombre} ({unidades})")
        ax.grid(axis="x", alpha=0.25)
        fig.tight_layout()
        fig.savefig(
            GRAFICOS / f"boxplot_{nombre}.png",
            dpi=150
        )
        plt.close(fig)


# ============================================================
# 5. EXPORTACIÓN DE RESULTADOS
# ============================================================

guardar_csv(reg_variables, "dimensiones_variables.csv")
guardar_csv(reg_faltantes, "faltantes.csv")
guardar_csv(reg_estadisticas, "estadisticas_numericas.csv")
guardar_csv(reg_cardinalidad, "cardinalidad.csv")
guardar_csv(reg_muestras, "muestra_valores.csv")

with (SALIDA / "informe_eda.txt").open(
    "w",
    encoding="utf-8"
) as archivo_informe:
    archivo_informe.write("\n".join(lineas))
    archivo_informe.write("\n")

print("\n" + "=" * 65)
print("EDA FINALIZADO")
print("Resultados guardados en:", SALIDA)
print("=" * 65)

