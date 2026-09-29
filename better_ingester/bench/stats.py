"""
bench/stats.py — the small statistics the report needs.

Deliberately minimal: per-condition means with spread, and paired
document-level differences with one significance test. Comparisons are paired
because the same documents go through every condition, which removes
document-to-document variation from the comparison — that is the only
statistical subtlety here and it is a property of the design, not of the test.

The Wilcoxon signed-rank test is used rather than a paired t-test because
per-document scores are bounded in [0, 1] and skewed, so a rank-based test is
the safer default. Nothing else is inferred.
"""

from __future__ import annotations

import math
import statistics


def describe(values: list[float]) -> dict | None:
    """mean, sd and n — what every reported cell is built from."""
    n = len(values)
    if not n:
        return None
    mean = statistics.mean(values)
    sd = statistics.stdev(values) if n > 1 else 0.0
    # Rounded to 6 places, not 3 or 4: every renderer rounds again to its own
    # precision, and rounding twice moved reported cells by 1 in the last
    # digit (BASE-big detection printed 0.875 in the main table while the
    # paired table, which rounds once from the raw mean, printed 0.876).
    return {"mean": round(mean, 6), "sd": round(sd, 6), "n": n}


def wilcoxon_one_sided(x: list[float], y: list[float],
                       alternative: str = "greater") -> float:
    """p-value that median(x - y) > 0 ('greater') or < 0 ('less').
    Zero differences are dropped, which is standard practice."""
    d = [a - b for a, b in zip(x, y) if a != b]
    if not d:
        return 1.0
    try:
        from scipy.stats import wilcoxon  # type: ignore[import-untyped]
        return float(wilcoxon([a - b for a, b in zip(x, y)],
                              alternative=alternative,
                              zero_method="wilcox").pvalue)
    except Exception:
        pass
    # normal approximation with tie correction, for environments without scipy
    ranked = sorted((abs(v), v > 0) for v in d)
    n = len(ranked)
    ranks: list[float] = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and ranked[j + 1][0] == ranked[i][0]:
            j += 1
        r = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[k] = r
        i = j + 1
    w_plus = sum(r for r, (_, pos) in zip(ranks, ranked) if pos)
    mu = n * (n + 1) / 4
    sigma = math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
    if sigma == 0:
        return 1.0
    z = (w_plus - mu) / sigma
    p_greater = 1 - 0.5 * (1 + math.erf(z / math.sqrt(2)))
    return p_greater if alternative == "greater" else 1 - p_greater


def paired_report(name: str, x: list[float], y: list[float],
                  alternative: str = "greater") -> dict:
    """One paired comparison: both means, their difference, and a p-value."""
    n = len(x)
    mx = statistics.mean(x) if n else None
    my = statistics.mean(y) if n else None
    diffs = [a - b for a, b in zip(x, y)]
    return {
        "comparison": name, "n": n,
        "mean_x": round(mx, 3) if mx is not None else None,
        "mean_y": round(my, 3) if my is not None else None,
        "mean_diff": round(statistics.mean(diffs), 3) if diffs else None,
        "sd_diff": round(statistics.stdev(diffs), 3) if len(diffs) > 1 else None,
        "p_wilcoxon": round(wilcoxon_one_sided(x, y, alternative), 5),
    }
