"""
Visualize BehaviorSpace results from the Watts-Strogatz small-world model.

Supports both:
  - vary-rewiring-probability          (uniform step 0.025, stats CSV)
  - vary-rewiring-probability-finegrained  (3-range enumerated, table CSV)

Usage:
  python visualize_rewiring.py              # uses coarse stats CSV
  python visualize_rewiring.py --fine       # uses fine-grained table CSV
"""

import argparse
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

HERE    = pathlib.Path(__file__).parent
OUT_DIR = HERE.parent / "image"
OUT_DIR.mkdir(exist_ok=True)

# ── CLI ───────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument("--fine", action="store_true",
                    help="Use fine-grained table CSV instead of stats CSV")
args = parser.parse_args()

# ── load data ─────────────────────────────────────────────────────────────────
if args.fine:
    stats_path = HERE / "Small Worlds vary-rewiring-probability-step-stats.csv"
    table_path = HERE / "Small Worlds vary-rewiring-probability-step-table.csv"

    df = pd.read_csv(stats_path, skiprows=6)
    df.columns = ["p", "step", "apl_mean", "apl_std", "cc_mean", "cc_std"]
    df = df.sort_values("p").reset_index(drop=True)

    runs = pd.read_csv(table_path, skiprows=6)
    runs.columns = ["run", "p", "step", "apl", "cc"]
    runs = runs.sort_values("p").reset_index(drop=True)

    title_suffix = "fine-grained (3-range enumerated)"
    out_name = "WS-behaviorspace-fine.png"
else:
    csv_path = HERE / "Small Worlds vary-rewiring-probability-stats.csv"
    df = pd.read_csv(csv_path, skiprows=6)
    df.columns = ["p", "step", "apl_mean", "apl_std", "cc_mean", "cc_std"]
    df = df.sort_values("p").reset_index(drop=True)

    table_path = HERE / "Small Worlds vary-rewiring-probability-table.csv"
    runs = pd.read_csv(table_path, skiprows=6)
    runs.columns = ["run", "p", "step", "apl", "cc"]
    runs = runs.sort_values("p").reset_index(drop=True)
    title_suffix = "uniform step 0.025"
    out_name = "WS-behaviorspace.png"

# ── normalise by p=0 values ───────────────────────────────────────────────────
apl_0 = df.loc[df["p"] == 0, "apl_mean"].values[0]
cc_0  = df.loc[df["p"] == 0, "cc_mean"].values[0]

df["apl_norm"]     = df["apl_mean"] / apl_0
df["cc_norm"]      = df["cc_mean"]  / cc_0
df["apl_norm_std"] = df["apl_std"]  / apl_0
df["cc_norm_std"]  = df["cc_std"]   / cc_0

runs["apl_norm"] = runs["apl"] / apl_0
runs["cc_norm"]  = runs["cc"]  / cc_0

# ── figure ────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
fig.suptitle(
    f"Watts–Strogatz Small-World Model — BehaviorSpace ({title_suffix})\n"
    "N=31, k=4, 5 repetitions each",
    fontsize=11, y=1.02,
)

# ─── panel A: normalised C(p)/C(0) and L(p)/L(0), log x ─────────────────────
ax = axes[0]
p  = df["p"]

# drop p=0 for log-scale (plot separately as dashed reference lines)
mask = p > 0
p_pos = p[mask]

ax.fill_between(p_pos,
                (df["cc_norm"]  - df["cc_norm_std"] )[mask],
                (df["cc_norm"]  + df["cc_norm_std"] )[mask],
                alpha=0.15, color="#2196F3")
ax.fill_between(p_pos,
                (df["apl_norm"] - df["apl_norm_std"])[mask],
                (df["apl_norm"] + df["apl_norm_std"])[mask],
                alpha=0.15, color="#F44336")

ax.plot(p_pos, df["cc_norm"] [mask], "o-", color="#2196F3", ms=4, lw=1.8,
        label="$C(p)\\ /\\ C(0)$  clustering coeff.")
ax.plot(p_pos, df["apl_norm"][mask], "s-", color="#F44336", ms=4, lw=1.8,
        label="$L(p)\\ /\\ L(0)$  avg. path length")

# reference lines at p=0 (value = 1.0 after normalisation)
ax.axhline(1.0, ls=":", color="gray", lw=1, alpha=0.6, label="$p=0$ baseline")

ax.set_xscale("log")
ax.set_xlabel("Rewiring probability  $p$  (log scale)", fontsize=11)
ax.set_ylabel("Normalised value  (relative to $p=0$)", fontsize=11)
ax.set_title("(A) Normalised $C(p)$ and $L(p)$", fontsize=11)
ax.set_ylim(0, 1.15)
ax.legend(fontsize=9, loc="lower left")
ax.grid(True, which="both", ls=":", alpha=0.4)

# annotate small-world region
if p_pos.min() < 0.01:
    ax.axvspan(0.0001, 0.01, alpha=0.07, color="green")
    ax.text(0.0003, 1.08, "small-world\nregion", fontsize=8,
            color="green", ha="center")

# ─── panel B: raw values with individual runs ─────────────────────────────────
ax2  = axes[1]
ax2b = ax2.twinx()

# scatter individual runs (p > 0 for log)
run_mask = runs["p"] > 0
ax2.scatter(runs.loc[run_mask, "p"], runs.loc[run_mask, "cc"],
            alpha=0.25, s=16, color="#2196F3", zorder=2)
ax2b.scatter(runs.loc[run_mask, "p"], runs.loc[run_mask, "apl"],
             alpha=0.25, s=16, color="#F44336", marker="s", zorder=2)

ax2.plot(p_pos, df["cc_mean"] [mask], "o-", color="#2196F3", ms=5, lw=2,
         label="Clustering coeff. (left)")
ax2b.plot(p_pos, df["apl_mean"][mask], "s-", color="#F44336", ms=5, lw=2,
          label="Avg. path length (right)")

ax2.set_xscale("log")
ax2.set_xlabel("Rewiring probability  $p$  (log scale)", fontsize=11)
ax2.set_ylabel("Clustering coefficient  $C(p)$", color="#2196F3", fontsize=11)
ax2b.set_ylabel("Average path length  $L(p)$",   color="#F44336",  fontsize=11)
ax2.tick_params(axis="y", colors="#2196F3")
ax2b.tick_params(axis="y", colors="#F44336")
ax2.set_title("(B) Raw values  (dots = individual runs)", fontsize=11)
ax2.set_ylim(0, None)
ax2b.set_ylim(0, None)
ax2.grid(True, which="both", ls=":", alpha=0.4)

lines_a, labels_a = ax2.get_legend_handles_labels()
lines_b, labels_b = ax2b.get_legend_handles_labels()
ax2.legend(lines_a + lines_b, labels_a + labels_b, fontsize=9, loc="upper right")

plt.tight_layout()
out_path = OUT_DIR / out_name
fig.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Saved → {out_path}")
plt.show()
