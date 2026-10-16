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


Dataset solicitado: [`scikit-learn/iris`](https://huggingface.co/datasets/scikit-learn/iris), split `train`.

## Publicar en GitHub y registrar avances

Repositorio del proyecto: <https://github.com/ED-SALGADO-IUD/ea1-carga-dataset-iris>

Para actualizarlo con los archivos de esta carpeta, usa la copia local del repositorio y registra los cambios:

```bash
git add .gitignore requirements.txt data src
git commit -m "Add Hugging Face loader and dataset summarizer"
git add EA1_Carga_y_Transformacion_Iris.ipynb reports README.md
git commit -m "Add Iris transformations and generated summary"
git push origin main
```

Si el repositorio aún no está clonado, puedes descargarlo con:

```bash
git clone https://github.com/ED-SALGADO-IUD/ea1-carga-dataset-iris.git
```

Si el repositorio es privado, concede acceso al docente.
