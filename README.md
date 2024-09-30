# LATAM Airlines DevSecOps/SRE Challenge

## Descripción

Este proyecto implementa una API para procesar y exponer datos analíticos que agregan valor a diferentes áreas de LATAM Airlines. Se enfoca en la resiliencia, calidad y seguridad de los servicios.

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.10
- **Framework:** FastAPI
- **Procesamiento de Datos:** pandas
- **Testing:** pytest
- **CI/CD:** GitHub Actions
- **Contenerización:** Docker
- **Linters y Formateadores:** flake8, black, mypy
- **Seguridad:** Bandit, JWT para autenticación

## Instalación

1. **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/latam-challenge.git
    cd latam-challenge
    ```

2. **Crear y Activar el Entorno Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar la Aplicación

```bash
uvicorn src.api.main:app --reload
