import pandas as pd

def load_topology_dataset(path="../data/zombie_topology.csv"):
    return pd.read_csv(path)
