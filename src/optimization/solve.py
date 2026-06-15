
from pyomo.environ import SolverFactory
from model.model import model

solver = SolverFactory("highs")

results = solver.solve(model)

print(results)
