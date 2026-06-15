import streamlit as st
import pandas as pd

from preprocessing.config_loader import load_config
from preprocessing.dataset_builder import build_datasets, export_parquet


# =========================
# CONFIG + DATA LOAD
# =========================
st.set_page_config(layout="wide")

cfg = load_config()
loaded, registry = build_datasets(cfg)


# =========================
# SIDEBAR GLOBAL INFO
# =========================
st.sidebar.title("📊 Mosaic Control Panel")

st.sidebar.metric("Nb datasets", len(loaded))
st.sidebar.write("Data dir:", cfg["data_dir"])

if st.sidebar.button("📦 Export Parquet"):
    export_parquet(loaded, cfg)
    st.sidebar.success("Export OK")


# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Registry",
    "👀 Preview",
    "📈 Stats",
    "🧪 Quality"
])


# =========================
# TAB 1 - REGISTRY
# =========================
with tab1:
    st.title("Registry global")

    st.dataframe(registry, width="stretch")

    st.download_button(
        "⬇️ Export registry CSV",
        registry.to_csv(index=False),
        file_name="registry.csv",
        mime="text/csv"
    )


# =========================
# TAB 2 - PREVIEW DATA
# =========================
with tab2:
    st.title("Preview datasets")

    selected = st.selectbox(
        "Choisir une variable",
        registry["variable"]
    )

    df = loaded[selected]

    st.subheader(selected)
    st.write("Shape:", df.shape)

    st.dataframe(df.head(100), width="stretch")


# =========================
# TAB 3 - STATS
# =========================
with tab3:
    st.title("Statistiques rapides")

    stats = []

    for k, df in loaded.items():
        stats.append({
            "variable": k,
            "rows": df.shape[0],
            "cols": df.shape[1],
            "missing_cells": int(df.isna().sum().sum()) if hasattr(df, "isna") else 0
        })

    stats_df = pd.DataFrame(stats)

    st.dataframe(stats_df, width="stretch")

    st.bar_chart(stats_df.set_index("variable")["rows"])


# =========================
# TAB 4 - QUALITY CHECK
# =========================
with tab4:
    st.title("Qualité des données")

    issues = []

    for k, df in loaded.items():

        # dataset vide
        if df.shape[0] == 0:
            issues.append((k, "EMPTY_DATASET"))

        # trop de valeurs manquantes
        if hasattr(df, "isna"):
            ratio = df.isna().sum().sum() / (df.shape[0] * max(df.shape[1], 1))
            if ratio > 0.3:
                issues.append((k, f"HIGH_MISSING_RATIO ({ratio:.2%})"))

        # colonnes bizarres
        if df.shape[1] == 1:
            issues.append((k, "ONLY_ONE_COLUMN"))

    issues_df = pd.DataFrame(issues, columns=["variable", "issue"])

    if issues_df.empty:
        st.success("Aucun problème détecté 🎉")
    else:
        st.warning("Problèmes détectés")
        st.dataframe(issues_df, width="stretch")