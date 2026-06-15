
from pyomo.environ import *

model = ConcreteModel()

# -----------------------------
# Sets
# -----------------------------

model.P = Set()
model.C = Set()

# -----------------------------
# Variables
# -----------------------------

model.X = Var(
    model.P,
    model.C,
    domain=NonNegativeReals
)

# -----------------------------
# Variables économiques
# -----------------------------

model.REV = Var()

# -----------------------------
# Exemple contrainte surface
# -----------------------------

def surface_rule(model, p):
    return sum(
        model.X[p, c]
        for c in model.C
    ) <= 1e6

model.surface_constraint = Constraint(
    model.P,
    rule=surface_rule
)

# -----------------------------
# Objectif
# -----------------------------

def objective_rule(model):

    return model.REV

model.objective = Objective(
    rule=objective_rule,
    sense=maximize
)
