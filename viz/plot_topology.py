import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_topology(df):
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(
        df["ZombieState"],
        df["RegulatoryDensity"],
        df["CapitalIntensity"],
        c=df["ReturnProfile"],
        cmap="viridis"
    )

    ax.set_xlabel("Zombie State")
    ax.set_ylabel("Regulatory Density")
    ax.set_zlabel("Capital Intensity")

    plt.show()
