
import numpy as np

from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize


class MOSAICAProblem(ElementwiseProblem):

    def __init__(self):

        super().__init__(
            n_var=10,
            n_obj=2,
            n_ieq_constr=1,
            xl=0,
            xu=100
        )

    def _evaluate(self, x, out, *args, **kwargs):

        revenu = np.sum(x)
        impact = np.sum(x**2)

        out["F"] = [
            -revenu,
            impact
        ]

        out["G"] = [
            np.sum(x) - 1000
        ]


problem = MOSAICAProblem()

algorithm = NSGA2(pop_size=100)

result = minimize(
    problem,
    algorithm,
    ('n_gen', 100),
    verbose=True
)

print(result.F)
