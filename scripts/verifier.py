import os
import pandas as pd

# Load the curated hero ledger relative to this script
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "..", "data", "hero_ledger.csv")
df = pd.read_csv(path)

# Observational association
p_y_given_x1 = df[df["X"] == 1]["Y"].mean()
p_y_given_x0 = df[df["X"] == 0]["Y"].mean()
print(f"P(Y=1|X=1) = {p_y_given_x1:.1%}")
print(f"P(Y=1|X=0) = {p_y_given_x0:.1%}\n")

# Backdoor adjustment function
p_z1 = (df["Z"] == 1).mean()
p_z0 = (df["Z"] == 0).mean()


def do_intervention(x_val):
    p_y_x_z1 = df[(df["X"] == x_val) & (df["Z"] == 1)]["Y"].mean()
    p_y_x_z0 = df[(df["X"] == x_val) & (df["Z"] == 0)]["Y"].mean()
    return p_y_x_z1 * p_z1 + p_y_x_z0 * p_z0

print(f"P(Y=1|do(X=1)) = {do_intervention(1):.1%}")
print(f"P(Y=1|do(X=0)) = {do_intervention(0):.1%}")
