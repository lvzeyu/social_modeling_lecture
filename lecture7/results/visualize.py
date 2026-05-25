import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

base = "Granovetter's_threshold_model_of_collective_behaviour "

def load_final(path, x_col):
    df = pd.read_csv(path, skiprows=6)
    df.columns = df.columns.str.strip().str.replace('"', '')
    final = df.loc[df.groupby("[run number]")["[step]"].idxmax()]
    agg = final.groupby(x_col)["final-proportion"].agg(
        cascade=lambda x: (x > 95).mean(),
        mean_fp="mean",
        std_fp="std"
    ).reset_index()
    return agg, final

# ── 実験1：平均値の影響 ─────────────────────────────────
agg1, final1 = load_final(base + "mean-effect-table.csv", "mean-threshold")
ax = axes[0]
ax.fill_between(agg1["mean-threshold"],
                agg1["cascade"] * 100 - agg1["std_fp"] * 0,
                color="steelblue", alpha=0.1)
ax.plot(agg1["mean-threshold"], agg1["cascade"] * 100,
        color="steelblue", linewidth=2.5, label="P(cascade)")
ax.plot(agg1["mean-threshold"], agg1["mean_fp"],
        color="steelblue", linewidth=1.5, linestyle="--",
        alpha=0.6, label="Mean final proportion")
ax.axvspan(28, 37, alpha=0.12, color="red", label="Transition zone")
ax.axvline(28, color="red", linestyle=":", linewidth=1)
ax.axvline(37, color="red", linestyle=":", linewidth=1)
ax.set_xlabel("Mean threshold  (sd = 20, fixed)", fontsize=12)
ax.set_ylabel("Cascade probability / Final proportion (%)", fontsize=11)
ax.set_title("Effect of Mean Threshold on Collective Action", fontsize=13)
ax.set_xlim(1, 60)
ax.set_ylim(-5, 110)
ax.legend(fontsize=10)
ax.grid(axis="y", alpha=0.3)

# ── 実験2：多様性の影響 ─────────────────────────────────
agg2, final2 = load_final(base + "diversity-effect-table.csv", "sd-threshold")
ax = axes[1]
ax.plot(agg2["sd-threshold"], agg2["cascade"] * 100,
        color="darkorange", linewidth=2.5, label="P(cascade)")
ax.plot(agg2["sd-threshold"], agg2["mean_fp"],
        color="darkorange", linewidth=1.5, linestyle="--",
        alpha=0.6, label="Mean final proportion")
ax.axvspan(11, 18, alpha=0.12, color="red", label="Transition zone")
ax.axvline(11, color="red", linestyle=":", linewidth=1)
ax.axvline(18, color="red", linestyle=":", linewidth=1)
ax.set_xlabel("SD threshold / Diversity  (mean = 25, fixed)", fontsize=12)
ax.set_title("Effect of Diversity (SD) on Collective Action", fontsize=13)
ax.set_xlim(1, 30)
ax.set_ylim(-5, 110)
ax.legend(fontsize=10)
ax.grid(axis="y", alpha=0.3)

plt.suptitle("Granovetter Threshold Model — Sensitivity Analysis\n"
             "(fully connected, normal distribution, N=100, 20–30 runs each)",
             fontsize=12)
plt.tight_layout()
plt.savefig("sensitivity_analysis.png", dpi=150, bbox_inches="tight")
print("Saved: sensitivity_analysis.png")

# ── 図2：臨界点付近の個別ラン分布（双稳态） ─────────────
fig2, axes2 = plt.subplots(1, 4, figsize=(14, 4), sharey=True)
for i, sd in enumerate([10, 12, 13, 17]):
    subset = final2[final2["sd-threshold"] == sd]["final-proportion"]
    axes2[i].hist(subset, bins=20, range=(0, 100),
                  color="darkorange", edgecolor="white", alpha=0.85)
    axes2[i].set_title(f"sd = {sd}", fontsize=12)
    axes2[i].set_xlabel("Final proportion (%)", fontsize=10)
    if i == 0:
        axes2[i].set_ylabel("Count", fontsize=10)
    axes2[i].grid(axis="y", alpha=0.3)

fig2.suptitle("Distribution of Final Participation — Bistability near the Critical Point\n"
              "(mean=25 fixed)", fontsize=12)
plt.tight_layout()
plt.savefig("bistability.png", dpi=150, bbox_inches="tight")
print("Saved: bistability.png")
plt.show()
