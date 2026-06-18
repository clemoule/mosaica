import pandas as pd
import re

def parse_blocks(file_path):
    data = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    current_aide = None
    years = []

    for line in lines:

        # Header colonne
        if line.startswith("ident"):
            parts = line.split()
            years = [p for p in parts if p.isdigit()]
            continue

        # Données
        parts = line.split()
        ident = parts[0]
        init = float(parts[1])
        calib = float(parts[2])
        values = parts[3:]

        for i, y in enumerate(years):
            data.append({
                "aide": "garantie",
                "ident": ident,
                "annee": int(y),
                "init": init,
                "calib": calib,
                "valeur": float(values[i])
            })

    return pd.DataFrame(data)


df = parse_blocks("data\\1_raw\\Aide_Garantie_Prix_Cult.txt")
df.to_csv("output.csv", index=False)

print(df.head())