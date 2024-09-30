from src.data_processing.process import process_data
import os
import pandas as pd

def test_process_data(tmpdir):
    input_file = os.path.join(tmpdir, "data.csv")
    output_file = os.path.join(tmpdir, "data_processed.csv")
    
    # Crear datos de prueba
    df = pd.DataFrame({
        "col1": [1, 2, None],
        "col2": ["a", "b", "c"]
    })
    df.to_csv(input_file, index=False)
    
    # Ejecutar procesamiento
    process_data(input_file, output_file)
    
    # Verificar resultados
    df_processed = pd.read_csv(output_file)
    assert df_processed.shape[0] == 2  # Una fila eliminada por NaN
