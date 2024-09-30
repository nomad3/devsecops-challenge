from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json() == {"message": "Datos obtenidos exitosamente"}

def test_process_data():
    payload = {
        "input_path": "data/raw/data.csv",
        "output_path": "data/processed/data_processed.csv"
    }
    response = client.post("/process-data", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Datos procesados exitosamente"}
