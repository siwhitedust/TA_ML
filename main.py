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

plt.tight_layout()
plt.show()