import pandas as pd
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(input_path: str, output_path: str) -> None:
    logger.info(f"Procesando datos desde {input_path}")
    try:
        df = pd.read_csv(input_path)
        # Procesamiento de datos (ejemplo: eliminar filas con valores nulos)
        df_processed = df.dropna()
        df_processed.to_csv(output_path, index=False)
        logger.info(f"Datos procesados y guardados en {output_path}")
    except Exception as e:
        logger.error(f"Error en el procesamiento de datos: {e}")
        raise
