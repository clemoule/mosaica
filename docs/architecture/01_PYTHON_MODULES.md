# Python Modules Architecture

## Module Dependency Graph

```
config (no dependencies)
  └── utils (depends on config)
  └── logging_config (depends on config)

preprocessing (depends on config, utils)
  ├── gis_loader
  ├── spatial_operations
  ├── data_cleaning
  ├── dataset_builder
  ├── agricultural_params
  ├── constraints
  └── export_handlers

optimization (depends on config, utils, preprocessing)
  ├── optimization_model
  ├── objectives
  ├── pymoo_solver
  ├── calibration
  └── solution_analysis

gama_interface (depends on config, utils)
  ├── gama_wrapper
  ├── communication
  └── simulation_runner

orchestration (depends on all modules)
  ├── pipeline
  ├── optimization_simulation_loop
  ├── experiment_manager
  └── checkpointing

analysis (depends on config, utils, preprocessing, optimization)
  ├── scoring
  ├── statistical_analysis
  ├── pareto_analysis
  └── scenario_comparison

visualization (depends on config, utils, analysis)
  ├── static_plots
  ├── gis_maps
  ├── dashboard
  └── reporting
```

---

## Module Details

### 1. `config` - Configuration Management

**Purpose**: Centralize all configuration loading and validation

**Key Classes**:

```python
class Config:
    - load(config_path: str) -> Config
    - get(key: str) -> Any
    - validate() -> bool
    - to_dict() -> dict
```

**Responsibilities**:

- Load YAML/JSON configs
- Validate required parameters
- Provide default values
- Manage environment variables

**Usage**:

```python
from shared.config.config import Config
config = Config.load('src/1_preprocessing/preprocessing_config.yaml')
data_path = config.get('inputs.raw_data_path')
```

---

### 2. `utils` - Shared Utilities

**Purpose**: Common utilities used across modules

**Submodules**:

#### `path_utils.py`

- Path resolution (absolute, relative)
- Path validation
- Directory creation helpers

#### `validators.py`

- Input type validation
- Range validation
- GeoDataFrame validation
- Data shape validation

#### `io_handlers.py`

- JSON read/write
- CSV read/write
- GeoJSON read/write
- File compression/decompression

#### `performance.py`

- Timing decorators
- Memory profiling
- Function profiling

**Usage**:

```python
from mosaica.utils import read_json, validate_geodataframe
data = read_json('file.json')
validate_geodataframe(gdf)
```

---

### 3. `preprocessing` - GIS & Data Preparation

**Purpose**: Transform raw data into unified dataset

**Key Classes**:

#### `SIGDataLoader`

```python
class SIGDataLoader:
    def load_parcels(self, path: str) -> GeoDataFrame
    def load_raster(self, path: str, bounds: Box) -> xarray.DataArray
    def harmonize_crs(self, gdf: GeoDataFrame, target_crs: str) -> GeoDataFrame
    def validate_geometries(self, gdf: GeoDataFrame) -> GeoDataFrame
```

#### `SpatialOperations`

```python
class SpatialOperations:
    def spatial_join(self, left: GeoDataFrame, right: GeoDataFrame) -> GeoDataFrame
    def raster_vector_intersect(self, gdf: GeoDataFrame, raster: DataArray) -> DataFrame
    def calculate_areas(self, gdf: GeoDataFrame) -> Series
    def detect_overlaps(self, gdf: GeoDataFrame) -> list[tuple[int, int]]
```

#### `DataCleaning`

```python
class DataCleaning:
    def handle_missing_values(self, df: DataFrame, strategy: str) -> DataFrame
    def remove_outliers(self, df: DataFrame, method: str) -> DataFrame
    def validate_ranges(self, df: DataFrame, ranges: dict) -> bool
    def harmonize_nomenclature(self, df: DataFrame, mapping: dict) -> DataFrame
```

#### `DatasetBuilder`

```python
class DatasetBuilder:
    def build(self, gdf_parcels, gdf_crops, constraints) -> DataFrame
    def add_agricultural_params(self, df: DataFrame) -> DataFrame
    def validate_completeness(self, df: DataFrame) -> bool
    def export_to_csv(self, df: DataFrame, path: str)
    def export_to_json(self, df: DataFrame, path: str)
    def export_to_geojson(self, gdf: GeoDataFrame, path: str)
```

#### `AgriculturalParams`

```python
class AgriculturalParams:
    def load_itineraries(self, path: str) -> DataFrame
    def get_water_requirements(self, crop: str) -> dict
    def get_crop_calendar(self, crop: str) -> dict
    def get_labor_requirements(self, crop: str) -> float
```

#### `ConstraintManager`

```python
class ConstraintManager:
    def add_regulatory_constraint(self, name: str, rule: callable)
    def add_water_constraint(self, threshold: float)
    def add_ecological_constraint(self, protected_areas: GeoDataFrame)
    def add_social_constraint(self, rule: callable)
    def validate_allocation(self, allocation: dict) -> bool
```

**Usage**:

```python
from mosaica.preprocessing import SIGDataLoader, DatasetBuilder

loader = SIGDataLoader(config)
gdf_parcels = loader.load_parcels('inputs/parcels.shp')
gdf_crops = loader.load_crop_data('inputs/crops.shp')

builder = DatasetBuilder(config)
df_dataset = builder.build(gdf_parcels, gdf_crops)
builder.export_to_csv(df_dataset, 'inputs/prepared/dataset.csv')
```

---

### 4. `optimization` - Multi-Objective Optimization

**Purpose**: Solve multi-objective agricultural optimization problem

**Key Classes**:

#### `OptimizationModel`

```python
class OptimizationModel:
    def setup_variables(self)
    def setup_objectives(self, objective_list: list[str])
    def setup_constraints(self, constraint_manager: ConstraintManager)
    def generate_candidate(self) -> dict
    def evaluate(self, scores: dict)
    def converged(self) -> bool
    def get_pareto_front(self) -> list[dict]
```

#### `ObjectiveFunction`

```python
class ObjectiveFunction:
    def evaluate(self, allocation: dict) -> float

class RevenueObjective(ObjectiveFunction):
    def evaluate(self, allocation: dict) -> float

class LocalFoodProductionObjective(ObjectiveFunction):
    def evaluate(self, allocation: dict) -> float
```

#### `PyMOOSolver`

```python
class PyMOOSolver:
    def solve(self, problem: OptimizationModel,
              algorithm: str = 'NSGA3',
              n_gen: int = 100,
              pop_size: int = 100) -> Solution
```

#### `SolutionAnalysis`

```python
class SolutionAnalysis:
    def extract_pareto_front(self, result: Solution) -> list[dict]
    def rank_solutions(self, solutions: list[dict],
                       weights: dict) -> list[dict]
    def calculate_trade_offs(self, pareto_front: list[dict]) -> dict
```

**Usage**:

```python
from mosaica.optimization import OptimizationModel, PyMOOSolver

model = OptimizationModel(df_dataset, config)
model.setup_variables()
model.setup_objectives(['revenue', 'food_security', 'sustainability'])
model.setup_constraints(constraint_manager)

solver = PyMOOSolver(model)
result = solver.solve(n_gen=100, pop_size=150)
pareto = result.pareto_front
```

---

### 5. `gama_interface` - GAMA Coupling

**Purpose**: Manage communication with GAMA simulations

**Key Classes**:

#### `GAMASimulator`

```python
class GAMASimulator:
    def launch(self, allocation: dict, config: dict) -> str  # Returns result_id
    def wait_for_result(self, result_id: str, timeout: int) -> dict
    def run_async(self, allocation: dict, config: dict) -> str
    def run_sync(self, allocation: dict, config: dict) -> dict
```

#### `ParameterIO`

```python
class ParameterIO:
    def allocation_to_gama_json(self, allocation: dict) -> str
    def allocation_to_gama_csv(self, allocation: dict) -> str
    def validate_allocation(self, allocation: dict) -> bool
```

#### `ResultsIO`

```python
class ResultsIO:
    def parse_gama_results(self, result_path: str) -> dict
    def validate_results(self, results: dict) -> bool
    def extract_yields(self, results: dict) -> dict
    def extract_water_stress(self, results: dict) -> dict
    def extract_production(self, results: dict) -> dict
```

#### `SimulationBatch`

```python
class SimulationBatch:
    def add_simulation(self, allocation: dict, simulation_id: str)
    def run_parallel(self, n_workers: int = 4)
    def wait_all(self, timeout: int)
    def collect_results(self) -> list[dict]
```

**Usage**:

```python
from mosaica.gama_interface import GAMASimulator, SimulationBatch

simulator = GAMASimulator(config)
result = simulator.run_sync(allocation, scenario_config)
yields = result['yields']
```

---

### 6. `orchestration` - Workflow Management

**Purpose**: Orchestrate entire MOSAICA workflow

**Key Classes**:

#### `MOSAICAOrchestrator`

```python
class MOSAICAOrchestrator:
    def run(self, config_path: str) -> Results
    def run_step(self, step: str) -> Results
    def load_checkpoint(self, checkpoint_id: str)
    def save_checkpoint(self, checkpoint_id: str)
    def get_status(self) -> dict
```

#### `OptimizationSimulationLoop`

```python
class OptimizationSimulationLoop:
    def run(self, max_generations: int = 100) -> ParetFront
    def check_convergence(self) -> bool
    def early_stop(self) -> bool
```

#### `ExperimentManager`

```python
class ExperimentManager:
    def create_experiment(self, name: str, config: dict) -> str
    def list_experiments(self) -> list[dict]
    def get_experiment(self, exp_id: str) -> dict
    def load_results(self, exp_id: str) -> dict
```

#### `Checkpointing`

```python
class Checkpointing:
    def save_state(self, state: dict, checkpoint_id: str)
    def load_state(self, checkpoint_id: str) -> dict
    def list_checkpoints(self) -> list[str]
    def cleanup_old_checkpoints(self, keep_n: int = 10)
```

**Usage**:

```python
from mosaica.orchestration import MOSAICAOrchestrator

orchestrator = MOSAICAOrchestrator()
results = orchestrator.run('src/4_orchestration/orchestration_config.yaml')
```

---

### 7. `analysis` - Post-Processing Analysis

**Purpose**: Analyze and score optimization results

**Key Classes**:

#### `Scoring`

```python
class Scoring:
    def calculate_territorial_indicators(self, results: dict) -> dict
    def score_robustness(self, results: dict) -> float
    def score_feasibility(self, results: dict) -> float
    def score_social_acceptance(self, results: dict) -> float
    def aggregate_scores(self, scores: dict, weights: dict) -> float
```

#### `StatisticalAnalysis`

```python
class StatisticalAnalysis:
    def descriptive_statistics(self, data: list[float]) -> dict
    def compare_scenarios(self, scenario1: dict, scenario2: dict) -> dict
    def sensitivity_analysis(self, base_solution: dict, param_ranges: dict) -> dict
    def monte_carlo(self, n_iterations: int = 1000) -> dict
```

#### `ParetoAnalysis`

```python
class ParetoAnalysis:
    def extract_pareto_front(self, population: list[dict]) -> list[dict]
    def dominance_analysis(self, solution1: dict, solution2: dict) -> bool
    def calculate_trade_offs(self, pareto_front: list[dict]) -> dict
    def rank_solutions(self, pareto_front: list[dict], weights: dict) -> list[dict]
```

#### `ScenarioComparison`

```python
class ScenarioComparison:
    def compare(self, scenario1: dict, scenario2: dict) -> dict
    def impact_analysis(self, baseline: dict, alternative: dict) -> dict
    def robustness_comparison(self, scenario1: dict, scenario2: dict) -> dict
    def resilience_metrics(self, scenario: dict) -> dict
```

**Usage**:

```python
from mosaica.analysis import Scoring, ParetoAnalysis

scorer = Scoring(config)
scores = scorer.calculate_territorial_indicators(gama_results)

pareto_analyzer = ParetoAnalysis()
pareto_front = pareto_analyzer.extract_pareto_front(population)
```

---

### 8. `visualization` - Results Presentation

**Purpose**: Generate visualizations and reports

**Key Classes**:

#### `StaticPlots`

```python
class StaticPlots:
    def plot_pareto_front(self, pareto_front: list[dict]) -> Figure
    def plot_objectives_distribution(self, population: list[dict]) -> Figure
    def plot_trade_offs(self, pareto_front: list[dict]) -> Figure
    def plot_convergence(self, history: list[dict]) -> Figure
```

#### `GISMaps`

```python
class GISMaps:
    def plot_allocation_map(self, allocation: dict, gdf_base: GeoDataFrame) -> Figure
    def plot_yield_map(self, yields: dict, gdf_base: GeoDataFrame) -> Figure
    def plot_water_stress_map(self, stress: dict, gdf_base: GeoDataFrame) -> Figure
    def plot_production_map(self, production: dict, gdf_base: GeoDataFrame) -> Figure
```

#### `Dashboard`

```python
class Dashboard:
    def create_dashboard(self, results: dict) -> DashApp
    def add_scenario_selector(self)
    def add_objective_charts(self)
    def add_map_viewer(self)
    def add_statistics_panel(self)
    def run(self, host: str = 'localhost', port: int = 8050)
```

#### `ReportGenerator`

```python
class ReportGenerator:
    def generate_pdf_report(self, results: dict, output_path: str)
    def generate_html_report(self, results: dict, output_path: str)
    def add_summary_section(self, summary: dict)
    def add_pareto_analysis_section(self, pareto_front: list[dict])
    def add_maps_section(self, maps: list[Figure])
```

**Usage**:

```python
from mosaica.visualization import Dashboard, ReportGenerator

dashboard = Dashboard(pareto_front, config)
dashboard.run()

reporter = ReportGenerator()
reporter.generate_pdf_report(results, 'reports/result_001.pdf')
```

---

## Inter-Module Communication

### Configuration Flow

```
config.yaml → Config class → All modules (dependency injection)
```

### Data Flow

```
Raw Data → preprocessing → CSV/JSON → optimization → GAMA → analysis → visualization
```

### Error Handling Flow

```
Any module → logging system → error tracking → checkpointing → recovery
```

---

## Testing Strategy

- **Unit Tests**: Each module has `tests/unit/test_<module>.py`
- **Integration Tests**: Cross-module tests in `tests/integration/`
- **Fixtures**: Shared test data in `tests/conftest.py`
- **Coverage Target**: ≥80% for critical modules

---

## Import Organization

**Recommended Import Style**:

```python
# Standard library
import logging
from pathlib import Path

# Third-party
import geopandas as gpd
import pandas as pd

# Local
from mosaica.config import Config
from mosaica.preprocessing import SIGDataLoader
```

---

## References

- Full architecture: `docs/architecture/00_ARCHITECTURE_OVERVIEW.md`
- Data flow: `docs/architecture/03_DATA_FLOW.md`
- API documentation: `docs/api/`
