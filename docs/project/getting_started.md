# Getting Started with MOSAICA

## Overview

Ce document rassemble les instructions d'installation, de configuration et de démarrage rapide pour le projet MOSAICA.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/mosaica.git
cd mosaica
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

#### Activate the virtual environment

- macOS / Linux:

```bash
source venv/bin/activate
```

- Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

- Windows CMD:

```cmd
venv\Scripts\activate.bat
```

### 3. Install dependencies

#### Development installation

```bash
pip install -e .[dev]
```

#### Production installation

```bash
pip install .
```

#### Verify installation

```bash
python -c "from mosaica import Config; print('Success!')"
```

## Configuration

### 1. Edit the module config files

Chaque dossier numéroté contient sa propre configuration :

- `src/1_preprocessing/preprocessing_config.yaml`
- `src/2_maelia_pipeline/maelia_pipeline_config.yaml`
- `src/3_optimisation/optimisation_config.yaml`
- `src/4_orchestration/orchestration_config.yaml`
- `src/5_analysis_visualization/analysis_visualization_config.yaml`
- `src/6_gama_multiagent/gama_multiagent_config.yaml`

### 2. Edit config files

Mettez à jour les fichiers YAML de chaque dossier avec vos chemins d'inputs, paramètres d'optimisation, et paramètres de simulation.

### 3. Set up environment variables

Ce projet n'utilise pas de fichier `.env.example` centralisé pour le moment. Configurez directement vos variables d'environnement locales selon vos besoins.

## Quickstart

### Run a smoke test

```bash
pytest tests/unit/test_config.py -v
```

### Run all unit tests

```bash
pytest tests/unit/ -v
```

### Run full test suite

```bash
pytest tests/
```

### Run with coverage

```bash
pytest --cov=src tests/
```

## Docker (optional)

### Build Docker images

```bash
docker-compose -f docker/docker-compose.yml build
```

### Run Docker stack

```bash
docker-compose -f docker/docker-compose.yml up
```

## Project structure

```
mosaica/
├── src/                      # Numbered Python and GAML modules
├── tests/                    # Unit and integration tests
├── docs/                     # Project documentation
├── inputs/                   # Data input and output
├── docker/                   # Docker compose containers
├── pyproject.toml            # Project metadata
```

## Troubleshooting

### GDAL / Rasterio issues

Si vous rencontrez des erreurs GDAL :

- Sous Ubuntu/Debian :

```bash
sudo apt-get install gdal-bin libgdal-dev
```

- Sous macOS :

```bash
brew install gdal
```

- Sous Windows :

Utilisez `conda install -c conda-forge gdal` ou installez OSGeo4W.

### GeoPandas issues

```bash
pip install --upgrade geopandas
```

### Dependencies manquantes

```bash
pip install . --upgrade
```
