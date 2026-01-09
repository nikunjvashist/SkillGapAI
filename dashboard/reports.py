import pandas as pd

def generate_csv(matched, partial, missing):
    return pd.DataFrame({
        "Matched": matched,
        "Partial": partial + [""] * (len(matched) - len(partial)),
        "Missing": missing + [""] * (len(matched) - len(missing))
    })
