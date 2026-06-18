from pyomo.environ import *

from data.loader import load_yaml_config
from model.variables import create_variables
from model.constraint_registry import CONSTRAINT_REGISTRY


# ============================================================
# MODEL
# ============================================================

model = ConcreteModel()

config = load_yaml_config(
    "config/constraints.yaml"
)

# ============================================================
# SETS
# ============================================================

model.PLOTS = Set()
model.CROPS = Set()
model.FARMS = Set()

# ============================================================
# PARAMETERS
# ============================================================

model.plot_area_hectares = Param(model.PLOTS)

# etc...


# ============================================================
# VARIABLES
# ============================================================

create_variables(model)

# ============================================================
# CONSTRAINTS
# ============================================================

for _, constraint_builder in CONSTRAINT_REGISTRY.items():

    constraint_builder(
        model=model,
        config=config
    )

# ============================================================
# OBJECTIVE
# ============================================================

def objective_rule(model):

    return model.total_markowitz_revenue


model.objective = Objective(
    rule=objective_rule,
    sense=maximize
)