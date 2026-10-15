# EA1 — Carga y creación de dataset

Proyecto para la evidencia EA1: carga datos, los transforma y guarda un resumen en TXT.

## Estructura

- `src/hf_dataset_loader.py`: clase `HFDatasetLoader`, carga un split desde Hugging Face y lo convierte a pandas.
- `src/dataset_summarizer.py`: clase `DatasetSummarizer`, genera dimensiones, columnas, tipos, nulos y estadísticas en TXT.
- `EA1_Carga_y_Transformacion_Iris.ipynb`: flujo ejecutable con cuatro transformaciones visibles.
- `data/iris.csv`: copia local de respaldo para ejecutar el notebook sin conexión.
- `reports/dataset_summary.txt`: resumen generado por el notebook sobre el DataFrame transformado.

## Ejecutar

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook EA1_Carga_y_Transformacion_Iris.ipynb
```

Ejecuta las celdas en orden desde la carpeta raíz del proyecto. El cargador intenta Hugging Face primero. Si no hay conexión, usa `data/iris.csv` como respaldo para que la evidencia pueda reproducirse.

Dataset solicitado: [`scikit-learn/iris`](https://huggingface.co/datasets/scikit-learn/iris), split `train`.

## Publicar en GitHub

Crea un repositorio vacío en GitHub. Desde esta carpeta ejecuta:

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git branch -M main
git push -u origin main
```

Si el repositorio es privado, agrega al docente como colaborador. Entrega en la plataforma la URL del repositorio y confirma el envío.
