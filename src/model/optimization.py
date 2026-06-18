# src/optimization/optimizer.py

import pyomo.environ as pyo
from model.variables import obj_rule
from src.model.constraints import one_crop_per_parcel
from model.variables import obj_rule

def build_model(features):
    m = pyo.ConcreteModel()

    parc = features["parc"]
    crops = features["matrice_parc_cult"].columns

    # --------------------------
    # SETS
    # --------------------------
    m.P = pyo.Set(initialize=parc["SP"].unique())
    m.C = pyo.Set(initialize=crops)

    # --------------------------
    # VARIABLES
    # --------------------------
    m.x = pyo.Var(m.P, m.C, domain=pyo.Binary)

    m.obj = pyo.Objective(rule=obj_rule, sense=pyo.maximize)

    m.cons = pyo.Constraint(m.P, rule=one_crop_per_parcel)


    return m