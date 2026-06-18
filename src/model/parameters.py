import yaml
import pandas as pd
from pyomo.environ import Param, Set


class ParameterBuilder:

    def __init__(self, config_path: str):
        with open(config_path, "r") as f:
            self.cfg = yaml.safe_load(f)["parameters"]

    # ------------------------------------------------
    # ENTRY POINT
    # ------------------------------------------------
    def build(self, model):

        self._add_scalars(model)
        self._add_indexed_scalars(model)
        self._add_tables(model)

        return model

    # ------------------------------------------------
    # 1. SCALARS
    # ------------------------------------------------
    def _add_scalars(self, model):

        for name, value in self.cfg.get("scalars", {}).items():
            setattr(
                model,
                name,
                Param(initialize=value, mutable=True)
            )

    # ------------------------------------------------
    # 2. INDEXED SCALARS (ex: PART_PLUVIO(mois))
    # ------------------------------------------------
    def _add_indexed_scalars(self, model):

        for name, obj in self.cfg.get("indexed_scalars", {}).items():

            idx = obj["index"]
            values = obj["values"]

            setattr(model, f"{name}_SET", Set(initialize=idx))

            def rule(m, i, _vals=values):
                return _vals[i]

            setattr(
                model,
                name,
                Param(
                    getattr(model, f"{name}_SET"),
                    initialize=rule,
                    mutable=False
                )
            )

    # ------------------------------------------------
    # 3. TABLES (2D generic)
    # ------------------------------------------------
    def _add_tables(self, model):

        for name, obj in self.cfg.get("tables", {}).items():

            path = obj["file"]
            df = self._load_table(path)

            rows = df.index.tolist()
            cols = df.columns.tolist()

            setattr(model, f"{name}_R", Set(initialize=rows))
            setattr(model, f"{name}_C", Set(initialize=cols))

            def rule(m, i, j, _df=df):
                return _df.loc[i, j]

            setattr(
                model,
                name,
                Param(
                    getattr(model, f"{name}_R"),
                    getattr(model, f"{name}_C"),
                    initialize=rule,
                    mutable=False
                )
            )

    # ------------------------------------------------
    # UTILITY
    # ------------------------------------------------
    def _load_table(self, path):
        df = pd.read_csv(path, sep=None, engine="python")
        df = df.set_index(df.columns[0])
        return df