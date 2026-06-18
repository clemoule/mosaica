# solve.py
import pyomo.environ as pyo

def solve_model(model):
    solver = pyo.SolverFactory("glpk")  # ou cbc / gurobi

    result = solver.solve(model, tee=True)

    return result