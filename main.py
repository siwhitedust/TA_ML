import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

datasets = pd.read_csv("Hasil_1.csv")
df = pd.DataFrame(datasets)
sb.set_theme(style="whitegrid")

# Pembuatan Histogram untuk data numerik
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# histogram umur
sb.histplot(df["Age"], kde=True, ax=axes[0])
axes[0].set_title("Histogram umur")

# histogram pengalaman kerja
sb.histplot(df["Work_Experience"], kde=True, ax=axes[1])
axes[1].set_title("Histogram Pengalaman Kerja")

# histogram jumlah keluarga
sb.histplot(df["Family_Size"], kde=True, ax=axes[2])
axes[2].set_title("Histogram Jumlah Keluarga")

# Pembuatan Bar Chart
prof_cols = [c for c in df.columns if c.startswith("Profession_")]
prof_counts = df[prof_cols].sum().sort_values(ascending=True)
prof_names = [c.replace("Profession_","") for c in prof_counts.index]

plt.figure(figsize=(10, 5))
bars = plt.barh(prof_names, prof_counts.values)
plt.title("Bar Chart Pelanggan Sesuai Profesi")
plt.xlabel("Jumlah Pelanggan")

plt.tight_layout()
plt.show()