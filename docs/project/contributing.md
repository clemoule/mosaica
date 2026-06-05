# Contributing to MOSAICA

Merci de contribuer au projet MOSAICA. Ce guide présente les bonnes pratiques de développement.

## Code of Conduct

Soyez respectueux, inclusif et professionnel.

## Démarrage

### 1. Setup de l'environnement

```bash
git clone https://github.com/your-repo/mosaica.git
cd mosaica
python -m venv venv
```

#### Activation

- macOS / Linux :

```bash
source venv/bin/activate
```

- Windows PowerShell :

```powershell
venv\Scripts\Activate.ps1
```

- Windows CMD :

```cmd
venv\Scripts\activate.bat
```

### 2. Installation en mode développement

```bash
pip install -e " .[dev] "
pre-commit install
```

## Workflow de développement

- Branches de fonctionnalité : `feature/description`
- Corrections de bug : `bugfix/description`
- Documentation : `docs/description`
- Refactorisation : `refactor/description`

### Commit messages

Utilisez le format :

```
[COMPONENT] Short description

Long description if needed
```

## Standards de code

- `black` pour le formatage
- `isort` pour les imports
- `pylint` pour le lint
- `mypy` pour le typage

### Commandes utiles

```bash
black src
isort src
pylint src
mypy src
```

## Tests

- Écrire des tests unitaires pour toute nouvelle fonctionnalité
- Viser ≥80% de couverture

### Commandes de test

```bash
pytest tests/
pytest --cov=src tests/
```

## Structure de modules

| Module           | Responsabilité                                                       |
| ---------------- | -------------------------------------------------------------------- |
| `preprocessing`  | Chargement de données SIG, jointures spatiales, nettoyage de données |
| `optimization`   | Optimisation multi-objectif et solveur                               |
| `gama_interface` | Couplage avec GAMA / MAELIA                                          |
| `orchestration`  | Orchestration des pipelines et exécutions                            |
| `analysis`       | Post-traitement, métriques, scoring                                  |
| `visualization`  | Graphiques, cartes, tableaux de bord                                 |

## Pull Requests

1. Mettez à jour `docs/project/todo.md` avec votre progression
2. Ajoutez des tests
3. Exécutez le jeu de tests complet
4. Créez une PR avec une description claire
5. Demandez une relecture

## Documentation

- Architecture : `docs/architecture/`
- Tutoriels : `docs/tutorials/`
- API : `docs/api/`
- Documentation de projet : `docs/project/`
