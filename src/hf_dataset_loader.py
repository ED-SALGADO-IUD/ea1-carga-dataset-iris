"""Carga un dataset de Hugging Face Datasets y lo convierte a pandas."""
from pathlib import Path
from typing import Optional

import pandas as pd


class HFDatasetLoader:
    """Carga datasets de Hugging Face; admite un CSV local para modo sin conexión.

    Args:
        dataset_id: Identificador del dataset en Hugging Face (por ejemplo,
            ``scikit-learn/iris``).
        split: Partición que se cargará, normalmente ``train``.
        offline_fallback_path: CSV opcional para ejecutar la demostración sin
            conexión o sin el paquete ``datasets``. El intento de Hugging Face
            siempre se realiza primero.
    """

    def __init__(
        self,
        dataset_id: str,
        split: str = "train",
        offline_fallback_path: Optional[str] = None,
    ) -> None:
        if not dataset_id or not dataset_id.strip():
            raise ValueError("dataset_id no puede estar vacío.")
        if not split or not split.strip():
            raise ValueError("split no puede estar vacío.")
        self.dataset_id = dataset_id.strip()
        self.split = split.strip()
        self.offline_fallback_path = (
            Path(offline_fallback_path) if offline_fallback_path else None
        )
        self.last_source: Optional[str] = None

    def load(self) -> pd.DataFrame:
        """Carga la partición solicitada y la devuelve como DataFrame."""
        hf_error = None
        try:
            from datasets import load_dataset

            dataset = load_dataset(self.dataset_id, split=self.split)
            dataframe = dataset.to_pandas()
            if not isinstance(dataframe, pd.DataFrame):
                raise TypeError("Hugging Face no devolvió un DataFrame válido.")
            self.last_source = f"Hugging Face: {self.dataset_id} [{self.split}]"
            return dataframe
        except Exception as error:
            hf_error = error

        if self.offline_fallback_path is not None:
            if not self.offline_fallback_path.is_file():
                raise FileNotFoundError(
                    f"No existe el CSV local: {self.offline_fallback_path}"
                ) from hf_error
            self.last_source = (
                f"CSV local de respaldo: {self.offline_fallback_path} "
                f"(Hugging Face no estuvo disponible: {type(hf_error).__name__})"
            )
            return pd.read_csv(self.offline_fallback_path)

        raise RuntimeError(
            f"No fue posible cargar '{self.dataset_id}' (split='{self.split}') "
            "desde Hugging Face. Verifica la conexión, el identificador, el split "
            "y que esté instalado el paquete 'datasets'."
        ) from hf_error
