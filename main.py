import pandas as pd

datasets = pd.read_csv("Hasil_1.csv")
df = pd.DataFrame(datasets)

print(df.duplicated().sum())