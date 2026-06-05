# Architecture Overview - MOSAICA Project

## Executive Summary

This document describes the overall technical architecture of the MOSAICA ↔ MAELIA ↔ Multi-Agent coupling project for agricultural territorial optimization in Guadeloupe.

**Core Principle**: Python = brain (orchestration, optimization, analysis), GAML = specialist engines (simulation, spatial, agents)

---

## System Architecture Layers

### 1. **Data Layer** (Bottom)

- SIG/Raster data (shapefiles, GeoTIFFs)
- Crop parameters (agronomic, economic)
- Constraints (regulatory, environmental, social)
- GAMA simulation results

### 2. **Processing Layer** (Middle)

- **Python Preprocessing**: GIS operations, data cleaning, dataset generation
- **Python Optimization**: Multi-objective optimization with pymoo
- **GAMA Biophysics**: Crop growth, water dynamics via MAELIA
- **GAMA Multi-Agent**: Farmer behaviors, social interactions

### 3. **Orchestration Layer** (Middle-High)

- Python orchestrator pilots entire workflow
- Manages optimization-simulation loops
- Handles checkpointing and recovery
- Coordinates parallel simulations

### 4. **Analysis Layer** (Upper-Middle)

- Python post-processing
- Scoring and ranking
- Statistical analysis
- Pareto front analysis

### 5. **Presentation Layer** (Top)

- Python dashboards (Streamlit/Dash)
- Interactive maps (folium/geopandas)
- Report generation (PDF)
- Visualizations (matplotlib/seaborn)

---

## Technical Stack

### Python Ecosystem

| Component       | Technology                | Version |
| --------------- | ------------------------- | ------- |
| Preprocessing   | geopandas, rasterio, GDAL | Latest  |
| Optimization    | pymoo, pyomo, scipy       | Latest  |
| Data Processing | pandas, numpy, xarray     | Latest  |
| Testing         | pytest, pytest-cov        | Latest  |
| Documentation   | Sphinx, markdown          | Latest  |
| Dashboards      | Streamlit or Dash         | Latest  |
| Maps            | folium, geopandas         | Latest  |
| Visualization   | matplotlib, seaborn       | Latest  |

### GAML/GAMA Ecosystem

| Component   | Technology              |
| ----------- | ----------------------- |
| Biophysics  | MAELIA model (GAML)     |
| Multi-Agent | Custom GAML agents      |
| Container   | Docker + docker-compose |
| Runtime     | GAMA 1.9+               |

### Infrastructure

| Component        | Technology              |
| ---------------- | ----------------------- |
| Versioning       | Git + GitHub            |
| CI/CD            | GitHub Actions          |
| Environment      | Python venv / conda     |
| Containerization | Docker + docker-compose |
| Logging          | Python logging + files  |

---

## Module Organization

```
src/
├── 1_preprocessing/                 # Preprocessing pipeline
│   ├── main.py
│   ├── preprocessing/              # GIS & Data preparation
│   │   ├── __init__.py
│   │   ├── gis_loader.py           # Load shapefiles, rasters
│   │   ├── spatial_operations.py   # Spatial joins, intersections
│   │   ├── data_cleaning.py        # Data validation, cleaning
│   │   ├── dataset_builder.py      # Combine data into datasets
│   │   ├── agricultural_params.py  # Agronomic parameters
│   │   ├── constraints.py          # Constraint definitions
│   │   └── export_handlers.py      # CSV, JSON, GeoJSON export
│   └── preprocessing_config.yaml   # Preprocessing configuration
│
├── 2_maelia_pipeline/              # MAELIA / GAMA input pipeline
│   ├── main.py
│   ├── gama_interface/             # Interface with GAMA/MAELIA
│   │   ├── __init__.py
│   │   ├── gama_runner.py          # GAMA simulator wrapper
│   │   ├── io_adapter.py           # Parameter/result I/O
│   │   └── simulation_runner.py    # Batch simulation management
│   └── maelia_pipeline_config.yaml # MAELIA pipeline configuration
│
├── 3_optimisation/                 # Optimisation pipeline
│   ├── main.py
│   ├── optimization/               # Multi-objective optimisation
│   │   ├── __init__.py
│   │   ├── optimization_model.py   # Main model definition
│   │   ├── objectives.py           # Objective functions
│   │   ├── pymoo_solver.py         # Solver integration
│   │   ├── calibration.py          # Parameter tuning
│   │   └── solution_analysis.py    # Analysis of results
│   └── optimisation_config.yaml    # Optimisation configuration
│
├── 4_orchestration/                # Workflow orchestration
│   ├── main.py
│   ├── orchestration/              # Coordination and execution
│   │   ├── __init__.py
│   │   ├── workflow.py             # Main orchestrator
│   │   ├── experiment_manager.py   # Experiment workflows
│   │   └── checkpointing.py        # State persistence
│   └── orchestration_config.yaml   # Orchestration configuration
│
├── 5_analysis_visualization/       # Analysis and reporting
│   ├── main.py
│   ├── analysis/                   # Post-processing analysis
│   │   ├── __init__.py
│   │   ├── metrics.py              # Indicator scoring
│   │   ├── statistics.py           # Statistical analysis
│   │   ├── pareto_analysis.py      # Pareto front analysis
│   │   └── scenario_comparison.py  # Scenario benchmarking
│   ├── visualization/              # Graphs and maps
│   │   ├── __init__.py
│   │   ├── plots.py                # Plot generation
│   │   ├── maps.py                 # Spatial visualisations
│   │   └── reports.py              # Report export
│   └── analysis_visualization_config.yaml # Analysis/visualization config
│
└── 6_gama_multiagent/              # GAMA multi-agent model
    ├── main.py
    ├── gaml/                      # GAMA model assets
    │   ├── main.gaml
    │   ├── parameters/
    │   ├── experiments/
    │   ├── agents/
    │   ├── behaviors/
    │   ├── environment/
    │   └── visualizations/
    └── gama_multiagent_config.yaml # GAMA multi-agent configuration
```

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     GIS & Crop Data Sources                       │
│            (Shapefiles, Rasters, Excel, Databases)               │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │    Python: Preprocessing Module      │
        │  - Load SIG (geopandas, rasterio)   │
        │  - Spatial operations (joins, etc)  │
        │  - Data cleaning                    │
        │  - Build unified dataset            │
        │  - Export (CSV, JSON, GeoJSON)      │
        └────────────┬─────────────────────────┘
                     │
        ┌────────────▼─────────────────────────┐
        │    Python: Optimization Module       │
        │  - Load dataset                      │
        │  - Define objectives                │
        │  - Setup constraints                 │
        │  - Initialize pymoo solver           │
        └────────────┬─────────────────────────┘
                     │
                     │ (Iterative Loop)
                     │
      ┌──────────────▼──────────────────────────┐
      │  Python: Orchestrator                   │
      │  - Generate allocation candidate        │
      │  - Prepare parameters                   │
      └──────────────┬──────────────────────────┘
                     │
                     │ (JSON/CSV)
                     │
      ┌──────────────▼──────────────────────────┐
      │  GAMA/MAELIA: Biophysical Simulation    │
      │  - Load allocation                      │
      │  - Simulate crop growth                 │
      │  - Simulate water dynamics              │
      │  - Generate yield, stress results       │
      └──────────────┬──────────────────────────┘
                     │
                     │ (JSON/CSV results)
                     │
      ┌──────────────▼──────────────────────────┐
      │  Python: Analysis Module                │
      │  - Parse GAMA results                   │
      │  - Calculate objectives                 │
      │  - Score solution                       │
      │  - Return fitness to optimizer          │
      └──────────────┬──────────────────────────┘
                     │
                     │ (Loop to Optimization)
                     │
      ┌──────────────▼──────────────────────────┐
      │  Python: Pareto Analysis                │
      │  - Extract Pareto front                 │
      │  - Rank solutions                       │
      │  - Trade-off analysis                   │
      └──────────────┬──────────────────────────┘
                     │
      ┌──────────────▼──────────────────────────┐
      │  Python: Visualization                  │
      │  - Generate plots (Pareto, trade-offs)  │
      │  - Generate maps (allocation, yields)   │
      │  - Create dashboards                    │
      │  - Generate reports                     │
      └──────────────┬──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────────────────┐
        │    Final Results & Outputs            │
        │  - Interactive dashboards             │
        │  - PDF reports                        │
        │  - GIS layers                         │
        │  - Decision support                   │
        └──────────────────────────────────────┘
```

---

## Workflow Sequence

### Step 1: Data Preparation

```python
# Python preprocessing
preprocessor = SIGDataLoader(config)
gdf_parcels = preprocessor.load_parcels()
gdf_crops = preprocessor.load_crop_data()
gdf_constraints = preprocessor.load_constraints()
df_dataset = DatasetBuilder().build(gdf_parcels, gdf_crops, gdf_constraints)
df_dataset.to_csv('inputs/prepared/dataset.csv')
```

### Step 2: Initialize Optimization

```python
# Python optimization
optimizer = OptimizationModel(df_dataset, config)
optimizer.setup_variables()
optimizer.setup_objectives()
optimizer.setup_constraints()
```

### Step 3: Iterative Coupling Loop

```python
for generation in range(num_generations):
    # Get candidate allocation from optimizer
    allocation = optimizer.generate_candidate()

    # Send to GAMA
    gama_results = gama_simulator.run(allocation, config)

    # Evaluate
    scores = analyzer.score(gama_results)

    # Return to optimizer
    optimizer.evaluate(scores)

    # Check convergence
    if optimizer.converged():
        break
```

### Step 4: Analysis & Visualization

```python
# Python analysis
pareto_solutions = analyzer.extract_pareto_front()
dashboard = Dashboard(pareto_solutions)
dashboard.render()

reports = ReportGenerator(pareto_solutions)
reports.generate_pdf()
```

---

## Key Design Patterns

### 1. **Separation of Concerns**

- Preprocessing ≠ Optimization ≠ Simulation ≠ Analysis
- Each module has single responsibility
- Clear interfaces between modules

### 2. **Configuration-Driven**

- All parameters in YAML/JSON configs
- No hardcoded values in code
- Environment-specific configs

### 3. **Orchestrator Pattern**

- Central orchestrator manages workflow
- Modules don't know about each other
- Communication via files/APIs

### 4. **Factory & Builder Patterns**

- DatasetBuilder for complex object creation
- Factory methods for simulator creation
- Strategy pattern for different optimizers

### 5. **Observer Pattern**

- Logging system for monitoring
- Checkpointing for state tracking
- Event system for workflow milestones

---

## Data Format Standards

### Input Formats

- **SIG**: GeoJSON, Shapefile
- **Raster**: GeoTIFF
- **Tabular**: CSV, Excel
- **Config**: YAML, JSON

### Exchange Formats

- **Python ↔ GAMA**: JSON (preferred), CSV (fallback)
- **Results**: GeoJSON, CSV, JSON

### Output Formats

- **Results**: CSV, JSON, GeoJSON
- **Visualization**: HTML, PNG, PDF
- **Reports**: PDF, HTML

---

## Deployment Scenarios

### Development

```
Developer machine
├── Python venv
├── Local GAMA (if needed)
└── Local data
```

### Docker (Recommended)

```
docker-compose
├── Python container
├── GAMA container (optional)
└── Volumes for data
```

### HPC/Cluster

```
HPC environment
├── Python environment
├── GAMA module
└── Batch queue system
```

---

## Dependencies & Compatibility

- **Python**: 3.9+
- **GAMA**: 1.9+
- **GDAL**: 3.0+
- **PostgreSQL**: Optional (for large-scale data)

---

## Error Handling Strategy

1. **Input Validation**: Fail early at boundaries
2. **Graceful Degradation**: Use defaults when possible
3. **Logging**: Detailed logging at each step
4. **Recovery**: Checkpointing allows restart
5. **Reporting**: Clear error messages for users

---

## Performance Considerations

- Preprocessing: ~minutes (once per scenario)
- Optimization: ~hours (depends on population/generations)
- Single GAMA run: ~seconds to minutes
- Post-processing: ~minutes
- Total workflow: ~hours to days

---

## Scalability Roadmap

1. **Phase 1** (Current): Single-machine batch processing
2. **Phase 2**: Parallel GAMA simulations (local)
3. **Phase 3**: HPC cluster integration
4. **Phase 4**: Cloud batch processing (AWS/Azure)
5. **Phase 5**: Real-time streaming

---

## References

- README.md - Project overview
- PROJECT_ROADMAP.md - Implementation timeline
- TO_DO.md - Task tracking
- docs/architecture/01_PYTHON_MODULES.md - Python module details
- docs/architecture/02_GAML_STRUCTURE.md - GAML organization
