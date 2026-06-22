from pymo.environ import *


def add_revenue_constraint(model, config):

    def rule(model):
        return model.REV == sum(
            model.X[p, c] * model.MB_HA[c] for p in model.PLOTS for c in model.CROPS
        )

    model.revenue_constraint = Constraint(rule=rule)


def add_markowitz_exploitation_constraint(model, config):

    def rule(model, e):

        base = sum(
            model.X[p, c] * model.MB_HA[c]
            for p in model.PLOTS
            for c in model.CROPS
            if model.EXP_PARC[e, p]
        )

        risk = sum(
            model.X[p, c] * model.MB_HA[c] * model.VAR_RDT[c, "init"]
            for p in model.PLOTS
            for c in model.CROPS
            if model.EXP_PARC[e, p]
        )

        return model.REV_MARKOVITZ[e] == base - model.AVERS[e] * risk

    model.markowitz_exploitation_constraint = Constraint(model.EXPLOITATIONS, rule=rule)


def add_markowitz_global_constraint(model, config):

    def rule(model):
        return model.REV_MARKOVITZ_GWAD == sum(
            model.REV_MARKOVITZ[e] for e in model.EXPLOITATIONS
        )

    model.markowitz_global_constraint = Constraint(rule=rule)
