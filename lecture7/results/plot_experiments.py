import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from collections import defaultdict
from math import erf, sqrt
import scienceplots

plt.style.use(['science', 'nature', 'no-latex'])

BASE = "/home/lvzeyu/Lecture/social_modeling_lecture/lecture7/results/"

def norm_cdf(x, mean, sd):
    return 0.5 * (1 + erf((x - mean) / (sd * sqrt(2))))

# ═══════════════════════════════════════════════════════
# 実験1：平均閾値の影響（mean-effect-table.csv）
# ═══════════════════════════════════════════════════════
def load_table_final(path, x_col):
    runs = {}
    with open(path) as f:
        reader = csv.reader(f)
        for _ in range(6):
            next(reader)
        header = [c.strip().strip('"') for c in next(reader)]
        for row in reader:
            if len(row) < len(header):
                continue
            d = dict(zip(header, [v.strip().strip('"') for v in row]))
            rid = d['[run number]']
            step = int(d['[step]'])
            fp = float(d['final-proportion'])
            xv = int(float(d[x_col]))
            if rid not in runs or step > runs[rid]['step']:
                runs[rid] = {'x': xv, 'step': step, 'fp': fp}
    agg = defaultdict(list)
    for r in runs.values():
        agg[r['x']].append(r['fp'])
    xs = sorted(agg)
    cascade = [np.mean([v > 95 for v in agg[x]]) * 100 for x in xs]
    mean_fp = [np.mean(agg[x]) for x in xs]
    std_fp  = [np.std(agg[x])  for x in xs]
    return np.array(xs), np.array(cascade), np.array(mean_fp), np.array(std_fp)

# ═══════════════════════════════════════════════════════
# 実験2：多様性の影響（diversity-effect-stats.csv, sd=1-80）
# ═══════════════════════════════════════════════════════
def load_diversity_stats(path):
    sd_rows = defaultdict(list)
    with open(path) as f:
        reader = csv.reader(f)
        for _ in range(7):
            next(reader)
        for row in reader:
            if len(row) < 9:
                continue
            sd   = int(row[4])
            step = int(row[5])
            mfp  = float(row[6]) if row[6] not in ('N/A', '') else None
            if mfp is not None:
                sd_rows[sd].append((step, mfp))
    sds, last_means, step1_means = [], [], []
    for sd in sorted(sd_rows):
        steps = sorted(sd_rows[sd])
        last_means.append(steps[-1][1])
        s1 = next((m for s, m in steps if s == 1), 0.0)
        step1_means.append(s1)
        sds.append(sd)
    return np.array(sds), np.array(last_means), np.array(step1_means)

# ── データ読み込み ──────────────────────────────────────
xs1, casc1, mean1, std1 = load_table_final(
    BASE + "Granovetter's_threshold_model_of_collective_behaviour mean-effect-table.csv",
    'mean-threshold'
)
sds2, last2, step1_2 = load_diversity_stats(
    "/home/lvzeyu/Lecture/social_modeling_lecture/lecture7/"
    "Granovetter's_threshold_model_of_collective_behaviour diversity-effect-stats.csv"
)
p_clamp0   = np.array([norm_cdf(0.5,  25, sd) * 100 for sd in sds2])
p_clamp100 = np.array([(1 - norm_cdf(99.5, 25, sd)) * 100 for sd in sds2])

# ══════════════════════════════════════════════════════════════
# 図1：実験1 — 平均閾値の影響
# ══════════════════════════════════════════════════════════════
fig1, ax = plt.subplots(figsize=(6, 4))

ax.plot(xs1, casc1, color='#1f77b4', linewidth=1.8,
        label=r'$P(\mathrm{cascade})$')
ax.fill_between(xs1, np.clip(mean1 - std1, 0, 100),
                     np.clip(mean1 + std1, 0, 100),
                color='#1f77b4', alpha=0.12, label=r'Mean $\pm$ SD')
ax.plot(xs1, mean1, color='#1f77b4', linewidth=1.2,
        linestyle='--', alpha=0.7, label='Mean final proportion')

ax.axvspan(28, 37, alpha=0.10, color='#d62728', zorder=0)
ax.axvline(28, color='#d62728', linestyle=':', linewidth=1.0)
ax.axvline(37, color='#d62728', linestyle=':', linewidth=1.0)
ax.text(32.5, 55, 'Transition\nzone', ha='center', fontsize=7.5,
        color='#d62728')

ax.set_xlabel(r'Mean threshold $\mu$  ($\sigma = 20$, fixed)')
ax.set_ylabel('Cascade probability / Final proportion (%)')
ax.set_title('Experiment 1: Effect of Mean Threshold on Collective Action')
ax.set_xlim(1, 60)
ax.set_ylim(-5, 115)
ax.legend(fontsize=8, loc='lower left')
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%g%%'))

plt.tight_layout()
fig1.savefig(BASE + 'exp1_mean_effect.pdf', dpi=300, bbox_inches='tight')
fig1.savefig(BASE + 'exp1_mean_effect.png', dpi=200, bbox_inches='tight')
print("Saved: exp1_mean_effect.png / .pdf")

# ══════════════════════════════════════════════════════════════
# 図2：実験2 — 多様性（SD）の影響（非単調パターン）
# ══════════════════════════════════════════════════════════════
fig2, ax_top = plt.subplots(figsize=(6, 4))

w = 3
sm = np.convolve(last2, np.ones(w)/w, mode='same')

ax_top.plot(sds2, last2, color='#ff7f0e', alpha=0.30, linewidth=0.9)
ax_top.plot(sds2, sm,    color='#ff7f0e', linewidth=2.0,
            label='Final participation (3-pt moving avg)')

ax_top.axvspan(1,  9,  alpha=0.07, color='gray',    zorder=0)
ax_top.axvspan(10, 35, alpha=0.10, color='#2ca02c', zorder=0)
ax_top.axvspan(36, 80, alpha=0.08, color='#d62728', zorder=0)
ax_top.axvline(10, color='#2ca02c', linestyle='--', linewidth=1.0)
ax_top.axvline(35, color='#d62728', linestyle='--', linewidth=1.0)

ax_top.text(4.5,  8,  'No\ncascade',          ha='center', fontsize=7.5, color='gray')
ax_top.text(22,  50,  'Full cascade\n(100%)',  ha='center', fontsize=7.5, color='#2ca02c')
ax_top.text(58,  40,  'Partial cascade\n("too much diversity")',
            ha='center', fontsize=7.5, color='#d62728')

ax_top.set_xlabel('SD threshold  (mean = 25, fixed)')
ax_top.set_ylabel('Final participation (%)')
ax_top.set_title('Experiment 2: Effect of Diversity (SD) — Non-Monotonic Pattern\n'
                 '(mean = 25, fully connected, N = 100)')
ax_top.set_xlim(1, 80)
ax_top.set_ylim(-5, 115)
ax_top.yaxis.set_major_formatter(mticker.FormatStrFormatter('%g%%'))
ax_top.legend(fontsize=8, loc='lower right')

plt.tight_layout()
fig2.savefig(BASE + 'exp2_diversity_effect.pdf', dpi=300, bbox_inches='tight')
fig2.savefig(BASE + 'exp2_diversity_effect.png', dpi=200, bbox_inches='tight')
print("Saved: exp2_diversity_effect.png / .pdf")
plt.show()
