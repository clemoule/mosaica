from pyomo.environ import *


def create_variables(model):

    # ============================================================
    # DECISION VARIABLES
    # ============================================================

    model.optimized_area = Var(model.PLOTS, model.CROPS, domain=NonNegativeReals)

    # ============================================================
    # OBJECTIVE VARIABLES
    # ============================================================

    model.total_revenue = Var(domain=Reals)

    model.markowitz_revenue = Var(model.FARMS, domain=Reals)

    model.total_markowitz_revenue = Var(domain=Reals)
