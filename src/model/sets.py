import yaml
import re
from pyomo.environ import Set


class SetEngine:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        self.cfg = cfg.get("sets", {})
        self.relations = cfg.get("relations", {})
        self.subsets_cfg = cfg.get("subsets", {})
        self.variables = cfg.get("variables", {})

        self.sets = {}

    # =========================================================
    # PUBLIC
    # =========================================================
    def build(self):
        self._build_base()
        self._build_subsets()
        self._build_relations()
        self._build_variables()

        self._validate_full_coverage()

        return self.sets, self.relations

    # =========================================================
    # BASE SETS
    # =========================================================
    def _build_base(self):
        for name, spec in self.cfg.items():
            if name in ["relations", "subsets", "variables"]:
                continue

            t = spec["type"]

            if t == "range":
                self.sets[name] = self._range(spec)

            elif t == "list":
                self.sets[name] = self._list(spec)

            elif t == "include":
                self.sets[name] = self._include(spec["file"])

    # =========================================================
    # SUBSETS (DSL ENGINE)
    # =========================================================
    def _build_subsets(self):
        for name, spec in self.subsets_cfg.items():
            base = spec["base"]
            expr = spec.get("expr", "identity")

            if expr == "identity":
                self.sets[name] = self.sets[base]

            elif expr == "union":
                out = set()
                for s in spec["sets"]:
                    out |= self.sets.get(s, {s})
                self.sets[name] = out

            elif expr == "exclude":
                base_set = set(self.sets[base])
                for e in spec["exclude"]:
                    base_set.discard(e)
                self.sets[name] = base_set

            elif "values" in spec:
                self.sets[name] = set(spec["values"])

            else:
                raise ValueError(f"Expr non supportée: {name}")

    # =========================================================
    # RELATIONS
    # =========================================================
    def _build_relations(self):
        for name, spec in self.relations.items():
            self.relations[name] = {
                "dims": spec["dims"],
                "data": self._relation(spec["file"]),
            }

    # =========================================================
    # VARIABLES
    # =========================================================
    def _build_variables(self):
        self.variables_data = {}
        for name, spec in self.variables.items():
            self.variables_data[name] = self._include(spec["file"])

    # =========================================================
    # VALIDATION (GARANTIE DE COUVERTURE)
    # =========================================================
    def _validate_full_coverage(self):
        declared = set(self.sets.keys())

        expected = set(self.cfg.keys())
        expected.discard("relations")
        expected.discard("subsets")
        expected.discard("variables")

        missing = expected - declared

        if missing:
            raise ValueError(f"SETS NON TRAITES: {missing}")

    # =========================================================
    # PARSERS
    # =========================================================
    def _range(self, spec):
        start = spec["start"]
        end = spec["end"]

        prefix = re.match(r"[A-Za-z]+", start).group()
        i0 = int(re.findall(r"\d+", start)[0])
        i1 = int(re.findall(r"\d+", end)[0])

        return {f"{prefix}{i}" for i in range(i0, i1 + 1)}

    def _list(self, spec):
        return set(spec["values"])

    def _include(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return {l.strip() for l in f if l.strip()}
        except:
            return set()

    def _relation(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return [tuple(l.split()) for l in f if l.strip()]
        except:
            return []


def to_pyomo(sets_dict):
    return {k: Set(initialize=v) for k, v in sets_dict.items()}
