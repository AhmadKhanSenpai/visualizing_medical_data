import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

# 3
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)


# 4
def draw_cat_plot():
    # 5
    # 6
    df_cat = df.melt(
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
        var_name="feature",
        value_name="value",
    )
    # 7
    df_grouped = (
        df_cat.groupby(["cardio", "feature", "value"]).size().reset_index(name="total")
    )
    # 8
    fig = sns.catplot(
        data=df_grouped,
        x="feature",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    )

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None

    # 14
    fig, ax = None

    # 15

    # 16
    fig.savefig("heatmap.png")
    return fig
