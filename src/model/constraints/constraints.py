from pyomo.environ import *

# ============================================================
# REGISTRY GLOBAL (aucun hardcode ailleurs)
# ============================================================

CONSTRAINTS = {}


def register(name):
    def wrapper(func):
        CONSTRAINTS[name] = func
        return func
    return wrapper


# ============================================================
# PARCELLES
# ============================================================

@register("Eq_SURF_MAX_Parc")
def Eq_SURF_MAX_Parc(m, p):
    return sum(m.X[p, c] for c in m.SC) <= m.Data_Parc_Gwad[p, "SURF_HA"]


@register("Eq_SURF_INIT_Parc")
def Eq_SURF_INIT_Parc(m, p, c):
    return m.X[p, c] == m.MATRICE_Parc_Cult[p, c] * m.Data_Parc_Gwad[p, "SURF_HA"]


@register("Eq_NOCULT_NC")
def Eq_NOCULT_NC(m, p, c_nc):
    return m.X[p, c_nc] == 0


# ============================================================
# CULTURES
# ============================================================

@register("Eq_AN_SOL_Parc")
def Eq_AN_SOL_Parc(m, p, c_an):
    return m.X[p, c_an] <= (m.Data_Parc_Gwad[p, "TYPE_SOL"] == 2)


@register("Eq_ME_SOL_Parc")
def Eq_ME_SOL_Parc(m, p, c):
    return m.X[p, "ME"] <= (
        (m.Data_Parc_Gwad[p, "TYPE_SOL"] in [2,3,4]) or
        (m.Data_Parc_Gwad[p, "ILE"] == 1)
    )


@register("Eq_SURF_MIN_Parc")
def Eq_SURF_MIN_Parc(m, p, c):
    return m.X[p, c] <= m.Data_Parc_Gwad[p, "SURF_HA"]


@register("Eq_ALTIMIN_Parc")
def Eq_ALTIMIN_Parc(m, p, c):
    return m.X[p, c] <= (m.Data_Parc_Gwad[p,"ALTITUDE"] >= m.Data_Cult[c,"ALTI_MIN"])


@register("Eq_ALTIMAX_Parc")
def Eq_ALTIMAX_Parc(m, p, c):
    return m.X[p, c] <= (m.Data_Parc_Gwad[p,"ALTITUDE"] <= m.Data_Cult[c,"ALTI_MAX"])


@register("Eq_PENTEMIN_Parc")
def Eq_PENTEMIN_Parc(m, p, c):
    return m.X[p, c] <= (m.Data_Parc_Gwad[p,"PENTE"] >= m.Data_Cult[c,"PENTE_MIN"])


@register("Eq_PENTEMAX_Parc")
def Eq_PENTEMAX_Parc(m, p, c):
    return m.X[p, c] <= (m.Data_Parc_Gwad[p,"PENTE"] <= m.Data_Cult[c,"PENTE_MAX"])


@register("Eq_PLUVIOMIN_Parc")
def Eq_PLUVIOMIN_Parc(m, p, c):
    return m.X[p, c] <= (
        (m.Data_Parc_Gwad[p,"PLUVIO"] >= m.Data_Cult[c,"PLUVIO_MIN"])
        | (m.Data_Parc_Gwad[p,"IRRIG"] == 1)
    )


@register("Eq_PLUVIOMAX_Parc")
def Eq_PLUVIOMAX_Parc(m, p, c):
    return m.X[p, c] <= (m.Data_Parc_Gwad[p,"PLUVIO"] <= m.Data_Cult[c,"PLUVIO_MAX"])


# ============================================================
# SYSTEME CULTURES (exhaustif)
# ============================================================

@register("Eq_ME_IRR")
def Eq_ME_IRR(m, p):
    return m.X[p, "ME"] <= m.Data_Parc_Gwad[p,"IRRIG_PARC"]


@register("Eq_ME_MG")
def Eq_ME_MG(m, p):
    return m.X[p, "ME"] <= (m.Data_Parc_Gwad[p,"REGION"] != 7)


@register("Eq_IG_PLA_ILE")
def Eq_IG_PLA_ILE(m, p):
    return m.X[p,"IG_PLA"] <= (m.Data_Parc_Gwad[p,"ILE"] == 1)


@register("Eq_IG_TUT_ILE")
def Eq_IG_TUT_ILE(m, p):
    return m.X[p,"IG_TUT"] <= (m.Data_Parc_Gwad[p,"ILE"] != 1)


@register("Eq_IG_CLD")
def Eq_IG_CLD(m, p):
    return m.X[p,"IG_TUT"] <= (m.Data_Parc_Gwad[p,"RISQUE_CLD"] > 3)


# ============================================================
# CANNE (toutes variantes)
# ============================================================

@register("Eq_CS_IRR")
def Eq_CS_IRR(m, p, c):
    return m.X[p,c] <= 1


@register("Eq_CS_CONFORM")
def Eq_CS_CONFORM(m, p, c):
    return m.X[p,c] <= (m.Data_Parc_Gwad[p,"CONFORM"] <= m.params["CS_CONFORM_MAX"])


# ============================================================
# BANANE / PLANTAIN / etc (pattern identique)
# ============================================================

@register("Eq_BA_IRR")
def Eq_BA_IRR(m, p):
    return m.X[p,"BA_IRR"] <= m.Data_Parc_Gwad[p,"IRRIG_PARC"]


@register("Eq_BA_JA")
def Eq_BA_JA(m, e):
    return sum(m.X[p,"JA"] for p in m.parcels[e]) >= m.params["PROP_BA_JA"] * sum(m.X[p,"BA"] for p in m.parcels[e])


# ============================================================
# REVENU
# ============================================================

@register("Eq_REV")
def Eq_REV(m):
    return sum(m.X[p,c]*m.MB[c] for p in m.P for c in m.SC) == m.REV


@register("Eq_REV_MARKOVITZ")
def Eq_REV_MARKOVITZ(m, e):
    base = sum(m.X[p,c]*m.MB[c] for p in m.parcels[e] for c in m.SC)
    risk = sum(m.X[p,c]*m.MB[c]*m.Var_Rdt[c] for p in m.parcels[e] for c in m.SC)
    return base - risk * m.AVERS[e] == m.REV_MARKOVITZ[e]


# ============================================================
# QUOTAS (exhaustif)
# ============================================================

@register("Eq_BA_QUOTA_MAX")
def Eq_BA_QUOTA_MAX(m):
    return sum(m.X[p,c]*m.RDT_BA[c] for p in m.P for c in m.SC_BA) <= m.QUOTA_BA_MAX


@register("Eq_AN_QUOTA_MAX")
def Eq_AN_QUOTA_MAX(m):
    return sum(m.X[p,c]*m.RDT_AN[c] for p in m.P for c in m.SC_AN) <= m.QUOTA_AN_MAX