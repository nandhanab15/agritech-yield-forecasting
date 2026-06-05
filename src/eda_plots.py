from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Create figures folder
Path("reports/figures").mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Numeric features
features = ["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]

# Correlation matrix
corr = df[features].corr()

# Plot heatmap
fig, ax = plt.subplots(figsize=(7, 6))

im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

# Axis labels
ax.set_xticks(range(len(features)))
ax.set_xticklabels(features, rotation=45, ha="right")

ax.set_yticks(range(len(features)))
ax.set_yticklabels(features)

# Correlation values inside cells
for i in range(len(features)):
    for j in range(len(features)):
        ax.text(
            j,
            i,
            f"{corr.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

# Color bar
fig.colorbar(im, ax=ax, label="Pearson Correlation (r)")

# Title
ax.set_title("Sensor and Yield Correlation Heatmap")

plt.tight_layout()

# Save figure
plt.savefig(
    "reports/figures/corr_heatmap.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("Heatmap saved -> reports/figures/corr_heatmap.png")
# Scatter Plot 1: Humidity vs Yield
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(df["humidity_pct"], df["yield_kg"], alpha=0.4, s=20)
ax.set_xlabel("Humidity (%)")
ax.set_ylabel("Yield (kg)")
ax.set_title("Humidity vs Yield")
plt.tight_layout()
plt.savefig("reports/figures/humidity_vs_yield.png", dpi=150)
plt.close()

# Scatter Plot 2: Temperature vs Yield
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(df["temperature_c"], df["yield_kg"], alpha=0.4, s=20)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Yield (kg)")
ax.set_title("Temperature vs Yield")
plt.tight_layout()
plt.savefig("reports/figures/temperature_vs_yield.png", dpi=150)
plt.close()

# Scatter Plot 3: CO₂ vs Yield
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(df["co2_ppm"], df["yield_kg"], alpha=0.4, s=20)
ax.set_xlabel("CO₂ (ppm)")
ax.set_ylabel("Yield (kg)")
ax.set_title("CO₂ vs Yield")
plt.tight_layout()
plt.savefig("reports/figures/co2_vs_yield.png", dpi=150)
plt.close()

print("Scatter plots saved successfully.")