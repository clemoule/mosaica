# Projet de Couplage MOSAICA ↔ MAELIA ↔ Multi-Agent

## Vision globale du projet

Ce projet vise à construire une plateforme intégrée de simulation et d’optimisation territoriale agricole pour la Guadeloupe.

L’objectif est de coupler :

- un modèle d’optimisation multi-critère inspiré de MOSAICA (initialement développé en GAMS),
- le modèle MAELIA développé sous GAMA/GAML pour la simulation biophysique,
- et à terme des simulations multi-agents représentant les acteurs agricoles et institutionnels.

Le but scientifique est de dépasser une optimisation théorique statique pour évaluer :

- la faisabilité réelle des scénarios optimaux,
- leur robustesse,
- leur acceptabilité sociale,
- leur résilience face aux contraintes biophysiques et socio-économiques.

---

> Documentation de référence : `docs/project/getting_started.md`, `docs/project/roadmap.md`, `docs/project/contributing.md`.

---

# Contexte scientifique

Le modèle MOSAICA optimise l’allocation des cultures agricoles sur les parcelles de la Guadeloupe.

Le système doit déterminer :

- quelles cultures placer sur quelles parcelles,
- dans quelles proportions,
- sous quelles contraintes.

Les objectifs d’optimisation incluent notamment :

- maximisation du revenu agricole,
- augmentation de la production alimentaire locale,
- réduction de la dépendance aux cultures d’exportation,
- respect des contraintes environnementales,
- respect des contraintes sociales,
- respect des contraintes réglementaires.

Les données d’entrée incluent :

- données SIG,
- surfaces exploitables,
- rendements,
- temps d’itinéraire technique,
- temps de travail disponible,
- prix de vente,
- coûts,
- subventions,
- réglementations,
- contraintes hydriques,
- contraintes écologiques,
- etc.

Actuellement, certaines variables biophysiques sont simplifiées sous forme tabulée ou estimée.

L’objectif du couplage avec MAELIA est de remplacer ces simplifications par des simulations biophysiques explicites :

- croissance des cultures,
- dynamique hydrique,
- rendements simulés,
- stress environnementaux,
- interactions spatiales,
- temporalité des cultures,
- etc.

À plus long terme, une couche multi-agent permettra de simuler :

- les comportements des agriculteurs,
- l’acceptation des politiques agricoles,
- les inerties sociales,
- les stratégies individuelles,
- les interactions entre acteurs.

---

# Philosophie d’architecture du projet

Le projet ne doit PAS devenir un monolithe GAML.

Le principe fondamental est :

- Python = orchestration, optimisation, analyse, data science
- GAML = simulation spatiale, biophysique et multi-agent

GAMA/MAELIA doit être considéré comme un moteur de simulation spécialisé.

Python doit être considéré comme le cerveau principal du système.

---

# Répartition technologique recommandée

## PYTHON

Python est responsable de :

### 1. Préprocessing SIG et données

- import shapefiles
- traitement raster
- nettoyage géométrique
- harmonisation CRS
- jointures spatiales
- génération des tables d’entrée
- transformation Excel / CSV / GeoJSON
- feature engineering spatial

Librairies typiques :

- geopandas
- rasterio
- shapely
- pandas
- numpy
- xarray
- GDAL

---

### 2. Optimisation multi-critère

Le moteur principal d’optimisation doit être en Python.

Responsabilités :

- optimisation multi-objectif
- génération des fronts de Pareto
- calibration
- analyses de robustesse
- optimisation sous contraintes
- simulation-based optimization

Librairies potentielles :

- pymoo
- pyomo
- pulp
- nevergrad
- deap
- scipy.optimize

IMPORTANT :
L’optimisation NE doit PAS être codée directement dans GAML.

---

### 3. Orchestration globale du pipeline

Python pilote l’ensemble du workflow :

- génération des paramètres,
- lancement des simulations GAMA,
- récupération des résultats,
- évaluation des scénarios,
- comparaison des solutions,
- stockage des outputs,
- expérimentation batch.

Python agit comme chef d’orchestre.

---

### 4. Post-processing et analyses

Python gère :

- calcul des indicateurs,
- analyses statistiques,
- comparaison des scénarios,
- scoring,
- robustesse,
- analyses de sensibilité,
- Monte-Carlo,
- visualisation,
- dashboards.

---

### 5. Visualisation

Python est utilisé pour :

- graphiques,
- cartes,
- dashboards interactifs,
- Pareto fronts,
- indicateurs territoriaux.

---

# GAML / GAMA / MAELIA

GAML est responsable de la simulation.

Le rôle de GAMA est de représenter les dynamiques spatiales et temporelles complexes.

---

## 1. Simulation biophysique

MAELIA doit gérer :

- croissance des cultures,
- dynamique hydrique,
- rendements simulés,
- rotations,
- temporalité agricole,
- interactions environnementales,
- spatialisation des processus.

---

## 2. Simulation multi-agent

GAML sera également utilisé pour :

- agents agriculteurs,
- comportements économiques,
- adoption de pratiques,
- interactions sociales,
- diffusion spatiale,
- arbitrages individuels,
- décisions locales.

---

# Architecture cible

Le système doit être organisé comme suit :

Python :

- preprocessing
- optimisation
- orchestration
- analyses
- scoring
- post-processing

↓

GAMA / MAELIA :

- simulation biophysique
- simulation spatiale
- simulation multi-agent

↓

Retour des résultats vers Python

↓

Évaluation et optimisation itérative

---

# Workflow cible

Étape 1 :
Préprocessing des données SIG et génération des datasets.

Étape 2 :
Python génère une allocation agricole candidate.

Étape 3 :
Les paramètres sont envoyés à MAELIA/GAMA.

Étape 4 :
MAELIA simule les processus biophysiques.

Étape 5 :
Les résultats sont récupérés dans Python.

Étape 6 :
Python calcule les scores et objectifs.

Étape 7 :
L’optimiseur génère une nouvelle solution.

Boucle jusqu’à convergence.

---

# Vision scientifique à long terme

Le projet doit permettre de comparer :

1. optimum théorique multi-objectif
   VS
2. optimum réellement atteignable dans un système social complexe

L’objectif final est d’évaluer :

- robustesse,
- résilience,
- faisabilité,
- acceptabilité sociale,
- stabilité des politiques agricoles.

---

# Principes importants pour le développement

## Modularité

Chaque composant doit être indépendant :

- preprocessing,
- optimisation,
- simulation,
- analyse.

---

## Interopérabilité

Les échanges doivent passer par :

- CSV,
- JSON,
- GeoJSON,
- fichiers standardisés.

Éviter les dépendances internes complexes entre Python et GAML.

---

## Reproductibilité

Toutes les expériences doivent être :

- versionnées,
- traçables,
- configurables,
- relançables automatiquement.

---

## Scalabilité

Le système doit pouvoir évoluer vers :

- calcul parallèle,
- batch simulations,
- HPC,
- analyses massives de scénarios.

---

# Répartition finale recommandée

| Bloc                               | Technologie   |
| ---------------------------------- | ------------- |
| Préprocessing SIG                  | Python        |
| Nettoyage données                  | Python        |
| Construction datasets              | Python        |
| Optimisation multi-critère         | Python        |
| Couplage optimisation ↔ simulation | Python        |
| Simulation biophysique             | GAML / MAELIA |
| Simulation multi-agent             | GAML          |
| Orchestration expérimentale        | Python        |
| Analyse Pareto                     | Python        |
| Post-processing                    | Python        |
| Visualisation                      | Python        |
| Dashboards                         | Python        |

---

# Ce qu’il faut éviter

Ne PAS :

- transformer GAML en moteur principal d’optimisation,
- créer un énorme monolithe GAMA,
- mélanger optimisation et simulation dans le même bloc logique.

Le projet doit rester modulaire et scientifiquement maintenable.

---

# Rôle attendu de Copilot dans ce projet

Copilot doit :

- respecter strictement la séparation Python / GAML,
- proposer des architectures modulaires,
- privilégier Python pour optimisation et data science,
- privilégier GAML pour simulation spatiale et agents,
- générer du code maintenable et découplé,
- éviter les dépendances fortes entre composants,
- favoriser les pipelines reproductibles.

Lorsqu’un doute existe :

- optimisation / orchestration / analyse → Python
- simulation spatiale / biophysique / agents → GAML
