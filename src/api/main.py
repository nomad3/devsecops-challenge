from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.data_processing.process import process_data

app = FastAPI(title="LATAM Airlines Data API", version="1.0.0")

class DataRequest(BaseModel):
    input_path: str
    output_path: str

@app.post("/process-data", summary="Procesa datos y almacena el resultado.")
def handle_data(request: DataRequest):
    try:
        process_data(request.input_path, request.output_path)
        return {"message": "Datos procesados exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data", summary="Obtiene datos procesados.")
def get_data():
    # Implementar lógica para obtener datos
    return {"message": "Datos obtenidos exitosamente"}
