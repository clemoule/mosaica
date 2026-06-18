import yaml
from pyomo.environ import ConcreteModel, ConstraintList

from constraints import CONSTRAINTS


def build_model(data, config_path):

    model = ConcreteModel()

    # attach data
    for k, v in data.items():
        setattr(model, k, v)

    with open(config_path) as f:
        config = yaml.safe_load(f)

    model.constraints = ConstraintList()

    for cname, cdef in config["constraints"].items():

        if not cdef.get("enable", False):
            continue

        func = CONSTRAINTS.get(cname)
        if func is None:
            raise ValueError(f"Unknown constraint: {cname}")

        args = cdef.get("args", {})

        # call generic builder
        _apply_constraint(model, func, args)

    return model


def _apply_constraint(model, func, args):

    # full generic expansion logic
    try:
        res = func(model, **args)

        # scalar constraint
        if res is not None:
            model.constraints.add(res)

    except TypeError:
        # indexed constraints (P, C, etc.)
        for r in model.P:
            for c in model.SC:
                try:
                    expr = func(model, r, c, **args)
                    model.constraints.add(expr)
                except Exception:
                    continue