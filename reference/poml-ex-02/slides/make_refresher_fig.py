"""Figure for the refresher: pdf area up to t0 equals cdf height at t0."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

a, b, t0 = 2.5, 200.0, 150.0
t = np.linspace(0, 500, 1000)
f = a / b * (t / b) ** (a - 1) * np.exp(-(t / b) ** a)
F = 1 - np.exp(-(t / b) ** a)
F0 = 1 - np.exp(-(t0 / b) ** a)
print(f"F({t0:.0f}) = {F0:.4f}")

fig, (l, r) = plt.subplots(1, 2, figsize=(8, 2.8))
l.plot(t, f, color="#1F6FB2")
m = t <= t0
l.fill_between(t[m], f[m], color="#1F6FB2", alpha=.3)
l.text(95, f.max() * .25, f"area\n= {F0:.2f}", ha="center")
l.axvline(t0, color="gray", ls=":")
l.set(title=r"pdf $f(t)$", xlabel="t")
r.plot(t, F, color="#B26A00")
r.plot([t0], [F0], "o", color="#B26A00")
r.axvline(t0, color="gray", ls=":")
r.axhline(F0, color="gray", ls=":")
r.text(t0 + 15, F0 - .1, f"height = {F0:.2f}")
r.set(title=r"cdf $F(t)$", xlabel="t", ylim=(0, 1.05))
fig.suptitle(rf"Weibull $\alpha={a}$, $\beta={b:.0f}$, $t_0={t0:.0f}$", fontsize=10)
fig.tight_layout()
fig.savefig("figures/refresher_pdf_cdf.png", dpi=200)
