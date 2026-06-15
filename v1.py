import numpy as np

from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

# -----------------------------
# Données
# -----------------------------

cultures = [
    "ble_intensif",
    "ble_extensif",
    "mais_intensif",
    "mais_extensif",
    "tournesol_intensif",
    "tournesol_extensif"
]

# rendement t/ha
rendement = np.array([
    7,
    4,
    10,
    6,
    5,
    3
])

# prix €/t
prix = np.array([
    200,
    200,
    180,
    180,
    400,
    400
])

# coût €/ha
cout = np.array([
    600,
    250,
    800,
    350,
    500,
    200
])

# impact environnemental
impact = np.array([
    9,
    3,
    10,
    4,
    7,
    2
])

surface_totale = 100

# -----------------------------
# Définition du problème
# -----------------------------

class AgricultureProblem(ElementwiseProblem):

    def __init__(self):

        super().__init__(

            n_var=6,

            n_obj=2,

            n_ieq_constr=1,

            xl=np.zeros(6),

            xu=np.ones(6) * 100
        )

    def _evaluate(self, x, out, *args, **kwargs):

        # ---------------------------------
        # Revenu
        # ---------------------------------

        profit_par_ha = rendement * prix - cout

        revenu = np.sum(x * profit_par_ha)

        # ---------------------------------
        # Impact environnemental
        # ---------------------------------

        impact_total = np.sum(x * impact)

        # ---------------------------------
        # Contrainte surface
        # ---------------------------------

        surface = np.sum(x)

        contrainte_surface = surface - surface_totale

        # ---------------------------------
        # pymoo MINIMISE
        # donc on met -revenu
        # ---------------------------------

        out["F"] = [
            -revenu,
            impact_total
        ]

        out["G"] = [
            contrainte_surface
        ]

# -----------------------------
# Création problème
# -----------------------------

problem = AgricultureProblem()

# -----------------------------
# Algorithme
# -----------------------------

algorithm = NSGA2(
    pop_size=100
)

# -----------------------------
# Optimisation
# -----------------------------

result = minimize(

    problem,

    algorithm,

    ('n_gen', 200),

    seed=1,

    verbose=True
)

# -----------------------------
# Résultats
# -----------------------------

print("\n========== SOLUTIONS ==========\n")

for i in range(len(result.X)):

    print(f"\nSolution {i+1}")

    for j, culture in enumerate(cultures):

        print(f"{culture}: {result.X[i][j]:.2f} ha")

    revenu = -result.F[i][0]
    impact_env = result.F[i][1]

    print(f"Revenu = {revenu:.2f} €")
    print(f"Impact = {impact_env:.2f}")

import matplotlib.pyplot as plt

F = result.F

revenu = -F[:,0]
impact = F[:,1]

plt.scatter(impact, revenu)

plt.xlabel("Impact environnemental")
plt.ylabel("Revenu")

plt.title("Front de Pareto")

plt.show()