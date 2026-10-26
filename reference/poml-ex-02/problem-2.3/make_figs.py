"""Figures for the Problem 2.3 reference slides (run with the shared .venv)."""
import sys, pathlib
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "poml-ex-02_solutions" / "code"))
from common import load_myspace_data, weibull_pdf

t, c = load_myspace_data()
C = c.sum()
g = weibull_pdf(t, 2, 200)
Astar = (c @ g) / (g @ g)

fig, ax = plt.subplots(figsize=(6, 3.4))
ax.plot(t, c, color="0.6", label="Google data")
ax.plot(t, 1000 * g, label=r"start: $A=1000,\ \alpha=2,\ \beta=200$")
ax.plot(t, Astar * g, "--", label=rf"best $A$ for this shape: $A^*={Astar:.0f}$")
ax.set_xlabel("week after onset"); ax.set_ylabel("search count"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig("figures/start_guess.png", dpi=160)

ls = (17459.41, 2.7310, 211.0244)
ml = (C, 2.8086, 215.43)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(6, 4.2), sharex=True,
                             gridspec_kw={"height_ratios": [2, 1]})
a1.plot(t, c, color="0.6", label="Google data")
a1.plot(t, ls[0] * weibull_pdf(t, *ls[1:]), label=r"2.3 least squares ($\alpha$=2.731, $\beta$=211.0)")
a1.plot(t, ml[0] * weibull_pdf(t, *ml[1:]), "--", label=r"2.2 MLE ($\alpha$=2.809, $\beta$=215.4)")
a1.set_ylabel("search count"); a1.legend(fontsize=7)
a2.axhline(0, color="0.6", lw=.8)
a2.plot(t, c - ls[0] * weibull_pdf(t, *ls[1:]), lw=.9)
a2.plot(t, c - ml[0] * weibull_pdf(t, *ml[1:]), "--", lw=.9)
a2.set_ylabel("residual"); a2.set_xlabel("week after onset")
fig.tight_layout(); fig.savefig("figures/ls_vs_mle.png", dpi=160)
print("A* =", Astar)
