"""Genera un resumen legible de un DataFrame y lo guarda como archivo TXT."""
from pathlib import Path

import pandas as pd


class DatasetSummarizer:
    """Resume dimensiones, columnas, tipos, nulos y estadísticas descriptivas."""

    def __init__(self, dataframe: pd.DataFrame) -> None:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("dataframe debe ser una instancia de pandas.DataFrame.")
        self.dataframe = dataframe.copy()

    def build_summary(self) -> str:
        """Construye y devuelve el texto del resumen sin escribir archivos."""
        df = self.dataframe
        lines = [
            "RESUMEN DEL DATASET",
            "=" * 72,
            f"Filas: {len(df)}",
            f"Columnas: {len(df.columns)}",
            "",
            "COLUMNAS, TIPOS Y VALORES NULOS",
            "-" * 72,
        ]
        if df.empty and len(df.columns) == 0:
            lines.append("El DataFrame no contiene filas ni columnas.")
        else:
            for column in df.columns:
                lines.append(
                    f"- {column}: tipo={df[column].dtype}; "
                    f"nulos={int(df[column].isna().sum())}"
                )

        lines.extend(["", "ESTADÍSTICAS DESCRIPTIVAS", "-" * 72])
        if df.empty or len(df.columns) == 0:
            lines.append("No hay datos para calcular estadísticas.")
        else:
            try:
                lines.append(df.describe(include="all").to_string())
            except (TypeError, ValueError) as error:
                lines.append(f"No fue posible calcular estadísticas: {error}")
        lines.append("")
        return "\n".join(lines)

    def save(self, output_path: str) -> Path:
        """Guarda el resumen en UTF-8 y devuelve la ruta creada."""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.build_summary(), encoding="utf-8")
        return path
