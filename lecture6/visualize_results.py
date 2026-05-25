import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.font_manager as fm
import seaborn as sns

# Use Noto Sans CJK JP for Japanese text support
plt.rcParams["font.family"] = "Noto Sans CJK JP"
sns.set_theme(style="whitegrid", palette="tab10")
plt.rcParams["font.family"] = "Noto Sans CJK JP"

# --- Load data ---
df = pd.read_csv(
    "results/Segregation experiment3-table.csv",
    skiprows=6,
    header=0,
    low_memory=False,
)
df.columns = ["run", "density", "similar_wanted", "step", "percent_similar", "percent_unhappy"]
df = df.apply(pd.to_numeric, errors="coerce").dropna()

# Average across runs for each (density, similar_wanted, step) combination
mean_df = (
    df.groupby(["density", "similar_wanted", "step"])[["percent_similar", "percent_unhappy"]]
    .mean()
    .reset_index()
)

DENSITY_FOCUS = 70
SIMILAR_FOCUS = 30

# --- Final step per run ---
final_df = df.loc[df.groupby(["run", "density", "similar_wanted"])["step"].idxmax()].copy()

# Mean and std across runs
final_mean = (
    final_df.groupby(["density", "similar_wanted"])[["percent_similar", "percent_unhappy"]]
    .mean()
    .reset_index()
)

COLOR_SIM  = "#2196F3"  # blue  for percent-similar
COLOR_UNHP = "#F44336"  # red   for percent-unhappy

def dual_axis_plot(ax_left, x_vals, sim_vals, unhp_vals, xlabel, title):
    ax_right = ax_left.twinx()

    l1, = ax_left.plot(x_vals, sim_vals,  color=COLOR_SIM,  marker="o", linewidth=2, label="percent-similar")
    l2, = ax_right.plot(x_vals, unhp_vals, color=COLOR_UNHP, marker="s", linewidth=2, linestyle="--", label="percent-unhappy")

    ax_left.set_xlabel(xlabel, fontsize=11)
    ax_left.set_ylabel("percent-similar (%)", color=COLOR_SIM, fontsize=10)
    ax_right.set_ylabel("percent-unhappy (%)", color=COLOR_UNHP, fontsize=10)
    ax_left.tick_params(axis="y", colors=COLOR_SIM)
    ax_right.tick_params(axis="y", colors=COLOR_UNHP)
    ax_left.set_title(title, fontsize=12, pad=10)
    ax_left.legend(handles=[l1, l2], loc="center right", fontsize=9)
    ax_left.set_xticks(x_vals)
    ax_left.grid(True, alpha=0.4)

# ---- Figure 1: density=70 固定、%-similar-wanted を変化 ----
sub1 = final_mean[final_mean["density"] == DENSITY_FOCUS].sort_values("similar_wanted")

fig1, ax1 = plt.subplots(figsize=(8, 5))
dual_axis_plot(
    ax1,
    x_vals  = sub1["similar_wanted"].values,
    sim_vals  = sub1["percent_similar"].values,
    unhp_vals = sub1["percent_unhappy"].values,
    xlabel = "%-similar-wanted (%)",
    title  = f"%-similar-wanted の効果（density = {DENSITY_FOCUS}%固定）",
)
fig1.tight_layout()
fig1.savefig("image/result_similar_wanted.png", dpi=150, bbox_inches="tight")
print("Saved: image/result_similar_wanted.png")
plt.close(fig1)

# ---- Figure 2: %-similar-wanted=30 固定、density を変化 ----
sub2 = final_mean[final_mean["similar_wanted"] == SIMILAR_FOCUS].sort_values("density")

fig2, ax2 = plt.subplots(figsize=(8, 5))
dual_axis_plot(
    ax2,
    x_vals  = sub2["density"].values,
    sim_vals  = sub2["percent_similar"].values,
    unhp_vals = sub2["percent_unhappy"].values,
    xlabel = "density (%)",
    title  = f"density の効果（%-similar-wanted = {SIMILAR_FOCUS}%固定）",
)
fig2.tight_layout()
fig2.savefig("image/result_density.png", dpi=150, bbox_inches="tight")
print("Saved: image/result_density.png")
plt.close(fig2)

# ---- Figure 3: 参考図スタイル ----
# x: %-similar-wanted (0〜70), y: average similarity (0〜1),
# lines per density, dots = individual runs
import numpy as np

plot_df = final_df.copy()
plot_df["similarity"] = plot_df["percent_similar"] / 100

mean3 = (
    plot_df.groupby(["density", "similar_wanted"])["similarity"]
    .mean()
    .reset_index()
)

densities_all = sorted(plot_df["density"].unique())
cmap   = plt.get_cmap("rainbow")
colors = [cmap(i / (len(densities_all) - 1)) for i in range(len(densities_all))]

fig3, ax3 = plt.subplots(figsize=(8, 6))
rng = np.random.default_rng(42)

for color, d in zip(colors, densities_all):
    sub_run  = plot_df[plot_df["density"] == d].copy()
    jitter   = sub_run["similar_wanted"] / 100 + rng.uniform(-0.008, 0.008, len(sub_run))
    ax3.scatter(jitter, sub_run["similarity"],
                color=color, alpha=0.2, s=10, zorder=2)
    sub_mean = mean3[mean3["density"] == d].sort_values("similar_wanted")
    ax3.plot(sub_mean["similar_wanted"] / 100, sub_mean["similarity"],
             color=color, linewidth=2, marker="o", markersize=5,
             label=str(int(d) / 100), zorder=3)

n_runs = int(plot_df.groupby(["density", "similar_wanted"])["run"].nunique().mean())
ax3.set_xlabel("similarity-threshold", fontsize=12)
ax3.set_ylabel("average similarity", fontsize=12)
ax3.set_title(f"{n_runs} runs per combo", fontsize=12)
ax3.set_xlim(-0.02, 0.75)
ax3.set_ylim(0.45, 1.02)
ax3.legend(title="density", fontsize=9, title_fontsize=10,
           loc="lower right", framealpha=0.9)
ax3.grid(True, alpha=0.3)

fig3.tight_layout()
fig3.savefig("image/result_overview.png", dpi=150, bbox_inches="tight")
print("Saved: image/result_overview.png")
plt.close(fig3)
