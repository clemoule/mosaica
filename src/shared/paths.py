from pathlib import Path


# =========================================================
# ROOT DU PROJET
# =========================================================

def get_project_root(marker: str = ".git") -> Path:
    """
    Remonte l'arborescence jusqu'à trouver la racine du projet.
    Par défaut : détecte le dossier .git
    """
    path = Path(__file__).resolve()

    for parent in path.parents:
        if (parent / marker).exists():
            return parent

    # fallback si pas de .git
    return path.parents[-2]


PROJECT_ROOT = get_project_root()


# =========================================================
# DOSSIERS PRINCIPAUX
# =========================================================

SRC_DIR = PROJECT_ROOT / "src"
DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
CONFIG_DIR = PROJECT_ROOT / "config"
LOGS_DIR = PROJECT_ROOT / "logs"


# =========================================================
# MODULE PREPROCESSING
# =========================================================

PREPROCESSING_DIR = SRC_DIR / "1_preprocessing"
PIPELINE_DIR = PREPROCESSING_DIR / "preprocessing"