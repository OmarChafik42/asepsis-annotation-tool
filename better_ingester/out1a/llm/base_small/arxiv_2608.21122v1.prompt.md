Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
LABS: Extending the scope of binary segmentation
via a look-ahead device
∗
Piotr Fryzlewicz
Abstract
Binary segmentation is widely used for multiple change-point detection because
it is fast, simple to describe, and simple to implement. Its validity rests on the
requirement that, at each recursive stage, the procedure identifies one of the true
change-points when several are present in the current interval. This holds for de-
tectingchangesinmeanusingtheCUSUMstatistic, butfailsinsomeothersettings,
in particular in slope change detection for continuous piecewise-linear signals. We
propose Look-Ahead Binary Segmentation (LABS), a modification in which the
change-points returned by the two child recursions define a narrower interval on
which the parent estimate is re-evaluated. LABS inherits the computational speed
of standard binary segmentation, but achieves the near-optimal consistency rate of
O{(nlogn)1/2} in the slope-change signal setting when the LABS model is chosen
via either thresholding or a Schwarz-like information criterion. Simulations show
that LABS is fast and achieves state-of-the-art performance.
Keywords: Binary segmentation, change-point detection, piecewise-linear signal,
recursive algorithm, trend estimation.
1 Introduction
Binary segmentation is a frequently used method for segmenting ordered data, such as
time series, into multiple regions of perceived homogeneity. In its simplest form, it re-
cursively subdivides each current section of the data into two maximally contrasting
subsections, starting from the entire dataset, and stops on a given section when that
section is either too short to be divided further or considered homogeneous according to
∗Department of Statistics, London School of Economics and Political Science, London WC2A 2AE,
UK. Correspondence: p.fryzlewicz@lse.ac.uk. ORCID: 0000-0002-9676-902X.
1
6202
guA
12
]EM.tats[
1v22112.8062:viXra

a certain criterion. There is a 1-to-1 correspondence between the detected segments and
the estimated change-points that separate them.
In a time series setting, binary segmentation is often used to identify regions with ap-
proximately the same expectation, either of the time series itself or of a transformation
of it; see for example Vostrikova (1981), Venkatraman (1992), Bai (1997), Chen et al.
(2011), Cho and Fryzlewicz (2012) and Fryzlewicz and Subba Rao (2014), and Fryzlewicz
(2007) for the link with Unbalanced Haar wavelets. Killick et al. (2012) describe it as
“arguably the most widely used changepoint search method”. Brodsky and Darkhovsky
(1993) observe that many types of change, including distributional ones, can be seen as
changes in the mean of certain diagnostic sequences, which makes binary segmentation
applicable beyond mean shifts. Fryzlewicz (2014) proposes Wild Binary Segmentation,
which preserves the binary segmentation logic but evaluates the contrast on many deter-
ministically or randomly drawn sub-intervals, an idea also present in Kov´acs et al. (2023).
Both of these methods apply to the mean-shift model, but do not generalize beyond it.
Outside the classical time series setting, binary segmentation logic appears in Automated
Interaction Detection (Morgan and Sonquist, 1963) and Classification and Regression
Trees (CART; Breiman et al. (1984)), in which the best variable on which to subdivide is
chosen at each stage in a greedy way from the set of available predictive features, and is
inherited by modern descendants of CART offering improvements via bagging (random
forests; Breiman (2001)) or boosting (Friedman, 2001; Chen and Guestrin, 2016; Ke et al.,
2017). In these contexts the mechanism is alternatively referred to as recursive binary
partitioning. In contrast to regression trees, which typically use constant models in each
terminal node, Hothorn et al. (2006) introduce partitioned regression, in which terminal
nodes contain full regression models.
Binary segmentation is popular because it is fast (typically O(nlogn), where n is the data
length), easytoexplain, straightforwardtoimplement, andusablewitharangeofcontrast
functions across a range of stochastic models. Its success, however, relies on whether it
is capable, at each recursive stage, of identifying one of the change-points if multiple
are present in the current interval. When this condition holds, binary segmentation can
recursively isolate and estimate all change-points. When it fails, the algorithm may detect
spurious change-points far from any true locations. Venkatraman (1992) shows that, in
the piecewise-constant signal setting, binary segmentation used with the CUSUM statistic
(a maximum-likelihood-based contrast for additive i.i.d. Gaussian noise) does have this
property, which underpins the consistency of binary segmentation for detecting changes
in mean. By contrast, Baranowski et al. (2019) show that in the piecewise-linear signal
model the corresponding maximum-likelihood-based contrast can achieve its maximum
far from any of the true change-points when multiple are present in the current interval,
a point reiterated by Maidstone et al. (2019). This is the obstacle to extending binary
segmentation to this and similar settings.
2

Several methods address the limitations of classical binary segmentation in settings where
it fails; we review only those applicable to the piecewise-linear signal model. In the
Narrowest-Over-Threshold (NOT) method, Baranowski et al. (2019) sample many inter-
vals and select the narrowest one on which the contrast exceeds a threshold, the idea
being that sufficiently narrow intervals are likely to contain at most one change-point. A
related idea, based on interval expansion rather than sampling, appears in Isolate-Detect
(ID; Anastasiou and Fryzlewicz, 2022). Maidstone et al. (2019) introduce CPOP, a dy-
namic programming method for detecting changes in slope using an L penalty. This
0
approach is optimal for the criterion it minimizes, but the authors find empirically that
it has O(n2) computational cost when the number of change-points is fixed, making it or-
ders of magnitude slower in practice than the other techniques discussed here, a point we
illustrate later. Maeng and Fryzlewicz (2024) propose TrendSegment, a bottom-up adap-
tive wavelet-based approach that focuses on local features in the early stages of merging.
Kim et al. (2024a) propose a moving sum (MOSUM) procedure that scans for changes
using local parameter estimates from adjacent sliding windows, with O(n) cost for a fixed
collection of bandwidths.
We propose Look-Ahead Binary Segmentation (LABS), a modification of classical binary
segmentation that extends its scope to settings where the standard algorithm fails. It em-
ploys a look-ahead mechanism that uses information from the recursive calls on the child
intervals to refine the change-point estimate in the parent interval, at each recursive step.
This localizes the estimation problem adaptively, as the recursion proceeds. The modifi-
cation is confined to a single refinement step within the recursive flow, so the algorithm
remains straightforward to implement and to describe. It is naturally expressed through
recursion, and it has the same typical O(nlogn) cost as classical binary segmentation
under balanced recursive splits.
The basic version of LABS requires only the threshold parameter, which is also needed
by classical binary segmentation. We also describe a grid-based extension. It uses an
M-point grid for the proposal and an R-point grid for the re-test, providing additional
localization within each call at a fixed multiple of the cost. We prove consistency for
every fixed M,R ≥ 2, and for selection from a threshold solution path by a strengthened
Schwarz criterion. This mechanism differs from the one in NOT: LABS is consistent even
without grid refinement, corresponding to M = R = 2, whereas NOT requires the number
of sampled sub-intervals to grow with n.
The name look-ahead follows related uses in recursive search and decision-tree algorithms,
where tentative decisions are assessed through their child problems; Section S6 of the
supplement gives details.
The remainder of this paper is organized as follows. Section 2 presents the motivation
and problem statement, focusing on the piecewise-linear signal model, reviews classical
binary segmentation, and explains why it fails for detecting changes in slope. Section 3
3

introducestheLABSalgorithmanditsgrid-basedextension,andcomparesitwithexisting
methods. Section 4 establishes consistency for the piecewise-linear model. Section 5
reports a simulation study. Section 6 applies LABS to real data. Proofs and further
| discussion |            | are | in the | supplement |     | appended |     | to this   | preprint. |     |     |
| ---------- | ---------- | --- | ------ | ---------- | --- | -------- | --- | --------- | --------- | --- | --- |
| 2          | Motivation |     |        | and        |     | problem  |     | statement |           |     |     |
Although LABS applies to a variety of change-point models, including changes in mean,
changes in variance, and changes in higher-order polynomial structure, we present it in
the context of detecting changes in slope in a continuous piecewise-linear signal. This is
a canonical setting in which classical binary segmentation is known to fail (Baranowski
etal.,2019;Maidstoneetal.,2019). Thecontinuouspiecewise-linearmodelarisesinappli-
cations such as the analysis of tropospheric ozone trends (Chang et al., 2023), COVID-19
infection curves (Jiang et al., 2023), vehicle state estimation (Hosseinzadeh et al., 2025),
and intracellular transport (Do et al., 2025). Our application is to a global temperature
| time | series; | see | Section | 6.        |     |        |     |     |          |     |     |
| ---- | ------- | --- | ------- | --------- | --- | ------ | --- | --- | -------- | --- | --- |
| We   | observe | X   | ,...,X  | generated |     | by     |     |     |          |     |     |
|      |         |     | 1       | n         |     |        |     |     |          |     |     |
|      |         |     |         |           | X   | = f +ε | ,   | t = | 1,...,n, |     | (1) |
|      |         |     |         |           | t   | t      | t   |     |          |     |     |
where ε are zero-mean random variables with common variance σ2, and the signal f
|     |     | t   |     |     |     |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is continuous and piecewise-linear. Specifically, we assume there exist N change-points
1 < τ < ··· < τ < n and segment parameters (θ ,θ ) for j = 1,...,N+1, such that
|     | 1   |     | N   |     |     |     |     |     | j,1 j,2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
f = θ +θ t for t = τ +1,...,τ (with τ = 0, τ = n), subject to the continuity
| t   | j,1 | j,2 |     | j−1 |     | j   |     | 0   | N+1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
constraint
|     |     |     | θ   | +θ  | τ =   | θ     | +θ  | τ     | , j | = 1,...,N, | (2) |
| --- | --- | --- | --- | --- | ----- | ----- | --- | ----- | --- | ---------- | --- |
|     |     |     |     | j,1 | j,2 j | j+1,1 |     | j+1,2 | j   |            |     |
whichrequirestheleftandrightlinearpiecestoagreeateachchange-pointτ . Thechange-
j
points are the indices at which the slope changes, that is, θ ̸= θ , and our task is to
|     |     |     |     |     |     |     |     |     |     | j,2 j+1,2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
estimate N and the locations τ ,...,τ . The contrast functions below are derived under
|     |     |     |     |     | 1   |     | N   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
independent Gaussian errors, and the simulations of Section 5 use independent Gaussian
noise; the algorithm itself does not depend on this and only requires a contrast function
to be supplied.
We first review classical binary segmentation. Given a contrast function C (b) that
s,e
quantifies the evidence for a change-point at location b within the interval (s,e], binary
segmentation proceeds as follows. C (b) is taken to be non-negative, as is the case for the
s,e
CUSUM (3) and piecewise-linear GLR (6) contrasts used here, which are both defined as
absolute values; for a general signed contrast, replace C by |C| throughout.
4

| Algorithm | 1   | Classical       | Binary |     | Segmentation |     |     |     |     |     |     |     |
| --------- | --- | --------------- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| function  |     | BinSeg(X,s,e,λ) |        |     |              |     |     |     |     |     |     |     |
1:
ˆ
| 2:  | b ← argmax |         | C              | (b) |     |     |     |     |     |     |     |     |
| --- | ---------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |            |         | s<b<e          | s,e |     |     |     |     |     |     |     |     |
|     | if C       | (b) ˆ > | λ then         |     |     |     |     |     |     |     |     |     |
| 3:  | s,e        |         |                |     |     |     |     |     |     |     |     |     |
|     | Declare    |         | a change-point |     | at  | ˆ b |     |     |     |     |     |     |
4:
|     | BinSeg(X,s, |     | ˆ b,λ) |     |     |     |     |     |     |     | ▷ Recurse | on (s, ˆ b] |
| --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- |
5:
| 6:     | BinSeg(X, |     | ˆ b,e,λ) |     |     |     |     |     |     |     | ▷ Recurse | on ( ˆ b,e] |
| ------ | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- |
| 7:     | end if    |     |          |     |     |     |     |     |     |     |           |             |
| 8: end | function  |     |          |     |     |     |     |     |     |     |           |             |
The algorithm is launched by calling BinSeg(X,0,n,λ), where λ > 0 is a threshold
parameter. In the piecewise-constant signal model with additive Gaussian noise, the
| natural | contrast | is        | the CUSUM |            | statistic |     |             |          |     |          |           |     |
| ------- | -------- | --------- | --------- | ---------- | --------- | --- | ----------- | -------- | --- | -------- | --------- | --- |
|         |          |           |           |            |           |     | (cid:12)    |          |     |          | (cid:12)  |     |
|         |          |           |           | (cid:114)  |           |     |             | b        |     | e        |           |     |
|         |          |           |           | (e−b)(b−s) |           |     | (cid:12) 1  | (cid:88) | 1   | (cid:88) | (cid:12)  |     |
|         |          | CCUSUM(b) |           |            |           |     | (cid:12)    |          |     |          | (cid:12). |     |
|         |          |           | =         |            |           |     |             | X −      |     |          | X         | (3) |
|         |          | s,e       |           |            | e−s       |     | (cid:12)b−s | t        | e−b |          | t(cid:12) |     |
|         |          |           |           |            |           |     | (cid:12)    |          |     |          | (cid:12)  |     |
|         |          |           |           |            |           |     |             | t=s+1    |     | t=b+1    |           |     |
A result of Venkatraman (1992) establishes that the CUSUM achieves its maximum near
one of the true change-points even when multiple are present in (s,e], which underpins
the consistency of binary segmentation for detecting changes in mean.
In the continuous piecewise-linear model, the contrast derived from the generalized like-
lihood ratio (Baranowski et al., 2019) takes a different form. For each candidate location
b ∈ {s+2,...,e−1}, define ℓ = e−s and the normalizing quantities
|     |     |     | (cid:32) |     |     |     |     |     |     |     | (cid:33)1/2 |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
6
αb
|     |     |       | =       |     |         |     |     |     |     |         | ,   |     |
| --- | --- | ----- | ------- | --- | ------- | --- | --- | --- | --- | ------- | --- | --- |
|     |     | (s,e] | ℓ(ℓ2−1) |     | (cid:0) |     |     |     |     | (cid:1) |     |     |
1+(e−b+1)(b−s)+(e−b)(b−s−1)
(4)
|     |     |     | (cid:18) |     |     | (cid:19)1/2 |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
(e−b+1)(e−b)
|     |     | βb  | =   |     |     |     | .   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(s,e]
(b−s−1)(b−s)
| The contrast |     | vector | ϕb               | = (ϕb | (1),...,ϕb |         | (n))′   | has components |     |                  |     |     |
| ------------ | --- | ------ | ---------------- | ----- | ---------- | ------- | ------- | -------------- | --- | ---------------- | --- | --- |
|              |     |        | (s,e]            |       | (s,e]      |         | (s,e]   |                |     |                  |     |     |
|              |    |        | (cid:104)(cid:0) |       |            |         |         |                |     | (cid:1)(cid:105) |     |     |
|              |     | b b    |                  |       |            | (cid:1) | (cid:0) |                |     |                  |     |     |
 α β 3(b−s)+(e−b)− 1 t − b(ℓ−1)+2(s+1)(b − s) , t=s+1,...,b,
|     |     | ( s ,e ] ( | s , e] |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
α b
ϕb (t)= (cid:104) (cid:0) (cid:1) (cid:0) (cid:1) (cid:105) (5)
(s,e] − ( s ,e ] 3(e−b)+(b−s)+1 t − b(ℓ−1)+2e(e−b+1) , t=b+1,...,e,
b
0, β
( s,e]
otherwise,
| and the | contrast | function |     | is  |         |               |     |            |     |     |     |     |
| ------- | -------- | -------- | --- | --- | ------- | ------------- | --- | ---------- | --- | --- | --- | --- |
|         |          |          |     |     | Clin(b) | (cid:12)      | ϕb  | (cid:12)   |     |     |     |     |
|         |          |          |     |     |         | = (cid:12)⟨X, |     | ⟩(cid:12). |     |     |     | (6) |
|         |          |          |     |     | s,e     |               |     | (s,e]      |     |     |     |     |
The vector ϕb is the unit-norm continuous piecewise-linear function on (s,e] with a
(s,e]
single knot at b that is orthogonal to the constant and linear functions on that interval.
5

Two observations to the left of b and one to its right are needed for the knot to be
| identified, | which gives | the | candidate |     | set {s+2,...,e−1}. |     |     |     |     |     |
| ----------- | ----------- | --- | --------- | --- | ------------------ | --- | --- | --- | --- | --- |
When the interval (s,e] contains exactly one change-point, maximizing Clin(b) over b
s,e
yields a consistent estimator of its location with near-optimal guarantees (Baranowski
et al., 2019). When multiple change-points are present, however, the maximizer can be
far from all of them, unlike for CUSUM in the piecewise-constant model. To illustrate
| this, consider | the | “trap” | signal |     |     |     |     |     |     |     |
| -------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     | t/τ , |     |     | t = 1,...,τ    | ,   |     |     |
| --- | --- | --- | --- | ----- | --- | --- | -------------- | --- | --- | --- |
|     |     |     |   | 1     |     |     |                | 1   |     |     |
|     |     | f   | =   | 1,    |     |     | t = τ +1,...,τ | ,   |     | (7) |
|     |     |     | t   |       |     |     | 1              | 2   |     |     |
 (τ
|     |     |     |     | −t)/(τ | −τ  | ),  | t = τ +1,...,τ | ,   |     |     |
| --- | --- | --- | --- | ------ | --- | --- | -------------- | --- | --- | --- |
|     |     |     |     | 3      | 3   | 2   | 2              | 3   |     |     |
where0 < τ < τ < τ ,illustratedinFigure1withτ = 200,τ = 400,τ = 600,alongside
|     | 1 2 | 3   |     |     |     |     | 1   | 2   | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the contrast Clin(b) computed on the full interval. The contrast profile is unimodal, with
0,n
its maximum near b = 300, the midpoint between the two true change-points, rather than
near either τ or τ (neither τ nor τ is even a local maximum). Binary segmentation
|     | 1   | 2   |     | 1   | 2   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
would therefore detect a spurious change-point at the midpoint before recursing to the
left and to the right. This failure (Baranowski et al., 2019; Maidstone et al., 2019) is the
problem that LABS is designed to address. Its cause is that the contrast is evaluated on
an interval containing multiple change-points, so that localization to narrower intervals is
needed. As shown in the next section, LABS achieves the localization adaptively as the
recursion progresses, by passing change-point information from children to parents and
| using it     | to localize   | the estimation |        | for | the          | parent. |     |        |     |     |
| ------------ | ------------- | -------------- | ------ | --- | ------------ | ------- | --- | ------ | --- | --- |
| 3 Look-Ahead |               |                | Binary |     | Segmentation |         |     | (LABS) |     |     |
| 3.1          | The algorithm |                |        |     |              |         |     |        |     |     |
The failure of classical binary segmentation in the piecewise-linear setting stems from
estimating change-point locations on intervals that contain multiple change-points. The
methods reviewed in Section 2, most notably ID and NOT, address this by changing
which intervals are considered. LABS instead preserves the recursive structure of binary
segmentation: after detecting a candidate change-point and recursing into the left and
right child intervals, the change-points detected in those children are used to define a
narrower interval on which the parent change-point is re-evaluated. We refer to this
| device | as look-ahead. |     |     |     |     |     |     |     |     |     |
| ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
Suppose a candidate change-point b is detected in (s,e], and on recursing let L and R be
|     |     |     |     |     | ˆ   |     | ˆ   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the sets of change-points detected in (s,b] and (b,e]. When non-empty, max(L) provides
a refined left boundary and min(R) a refined right boundary. Under the assumptions of
6

Figure 1: Left: the trap signal (7) with τ = 200, τ = 400, τ = 600; dashed red lines
1 2 3
mark the true change-points. Right: the absolute kink contrast |⟨f,ϕb ⟩| computed
(0,n]
over the full interval; its maximum (dotted blue) is near b = 300, away from either true
change-point.
Section 4, the resulting interval contains at most one previously undetected change-point,
so re-evaluating the contrast on it gives a more accurate estimate.
Let C (b) denote a contrast function and λ > 0 a threshold. The algorithm is launched
s,e
by calling LABS(X,0,n,λ). Here B denotes the set of valid candidate locations for
s,e
the contrast on (s,e]: B = {s + 2,...,e − 1} for the piecewise-linear GLR (6), and
s,e
B = {s + 1,...,e − 1} for the CUSUM (3). The contrast is evaluable on (s,e] when
s,e
B ̸= ∅. Weadopttheleftmost-maximizerconventionthroughout: argmaxisinterpreted
s,e
as minargmax when the maximizer is not unique.
7

| Algorithm | 2 Look-Ahead | Binary Segmentation | (LABS) |     |     |
| --------- | ------------ | ------------------- | ------ | --- | --- |
1: functionLABS(X,s,e,λ)
2: if Bs,e=∅(intervaltooshort)then
3: return∅
4: endif
5: ˆb←argmax Cs,e(b)
b∈Bs,e
6: Cs,e(ˆb)>λthen
| if  |                  |     |     |     | ▷Proposalphase   |
| --- | ---------------- | --- | --- | --- | ---------------- |
| 7:  | L←LABS(X,s,ˆb,λ) |     |     |     | ▷Recurseon(s,ˆb] |
|     | R←LABS(X,ˆb,e,λ) |     |     |     | ▷Recurseon(ˆb,e] |
8:
9:
▷Look-aheadrefinementphase
10:
if L̸=∅orR̸=∅then
(cid:40)
|     | max(L) ifL̸=∅ |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- |
| 11: | s′←           |     |     |     |     |
|     | s otherwise   |     |     |     |     |
(cid:40)
|     | min(R) ifR̸=∅ |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- |
| 12: | e′←           |     |     |     |     |
|     | e otherwise   |     |     |     |     |
| 13: | if B ̸=∅then  |     |     |     |     |
s′,e′
| 14: | ˆb′←argmax |     |     |     | ▷Re-teston(s′,e′] |
| --- | ---------- | --- | --- | --- | ----------------- |
b∈Bs′,e′ C s′,e′(b)
| 15: | if C s′,e′(ˆb′)>λthen |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- |
| 16: | returnL∪{ˆb′}∪R       |     |     |     |     |
▷Acceptrefinedestimate
17:
endif
| 18: | endif          |     |     |                     |                       |
| --- | -------------- | --- | --- | ------------------- | --------------------- |
| 19: | returnL∪R      |     |     | ▷Re-testfailed:     | discardparentestimate |
| 20: | endif          |     |     |                     |                       |
| 21: | returnL∪{ˆb}∪R |     |     | ▷Bothchildrenempty: | keepparentestimate    |
22: else
| 23: | return∅ |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
24:
endif
25:
endfunction
There are two phases at each recursive level. The proposal phase is that of classical binary
segmentation: a candidate ˆ b is identified by maximizing the contrast over the current
interval, and if the contrast exceeds the threshold, the algorithm recurses into the two
subintervals. In the look-ahead refinement phase, the change-point sets returned by the
child recursions define a narrower interval (s′,e′] on which the contrast is re-evaluated,
and the parent change-point is discarded if the re-test does not exceed the threshold.
The difference from classical binary segmentation is that information flows not only from
parent to children, through the interval boundaries, but also from children back to parent,
| through | the detected change-points. |     |     |     |     |
| ------- | --------------------------- | --- | --- | --- | --- |
To see how this corrects the trap problem, consider the trap signal (7) with change-points
at τ = 200 and τ = 400. The initial contrast on (0,600] is maximized near the midpoint
| 1   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
ˆ b ≈ 300. Recursing, the left child (0,300] contains only τ and detects it; the right child
1
(300,600]containsonlyτ anddetectsit. Thelook-aheadrefinementthenre-evaluatesthe
2
contrastonthenarrowerinterval(τˆ ,τˆ ] ≈ (200,400], whichcorrespondstotheflatmiddle
1 2
section and contains no new change-points. The re-test does not exceed the threshold,
and the spurious midpoint change-point is discarded. We revisit this example with noisy
| data in | Section 5. |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- |
8

| 3.2 Grid-based |     | extension |     |     |     |     |     |
| -------------- | --- | --------- | --- | --- | --- | --- | --- |
The basic LABS algorithm evaluates the contrast on the single interval (s,e] at each
recursive call. A natural extension evaluates the contrast on multiple sub-intervals of
(s,e], providing additional localization within each call. We form a grid of M ≥ 2 equally
| spaced points | within | the interval | [s,e]:  |             |     |     |     |
| ------------- | ------ | ------------ | ------- | ----------- | --- | --- | --- |
|               |        |              | (cid:4) | e−s (cid:7) |     |     |     |
|               |        | g = s,       | g = s+  | , ...,      | g = | e,  |     |
|               |        | 1            | 2       | M−1         | M   |     |     |
where ⌊·⌉ denotes rounding to the nearest integer. For every pair (g ,g ) with i < j and
i j
g −g ≥ 3, wecomputeC (b)overeachcandidateb ∈ {g +2,...,g −1}. Thecandidate
| j i |     | gi,gj |     |     | i   | j   |     |
| --- | --- | ----- | --- | --- | --- | --- | --- |
change-point is the location achieving the global maximum across all such sub-intervals,
and a change-point is declared if this maximum exceeds λ. When M = 2, only the full
| interval (s,e] | is evaluated, | recovering | Algorithm | 2.  |     |     |     |
| -------------- | ------------- | ---------- | --------- | --- | --- | --- | --- |
The grid-based search complements the look-ahead mechanism. The look-ahead narrows
the re-test interval using information from child recursions, across levels of the recursion
tree. By contrast, the grid search identifies favorable sub-intervals within one recursive
call. In our implementation it is applied in both the proposal and re-test phases. We
use M points for the proposal grid and R points for the re-test grid. A single-interval
evaluation, R = 2, shouldusuallysufficeforthere-testbecausethelook-aheadhasalready
narrowed its interval, so the paper considers the case R > 2 for completeness rather than
| out of computational |     | necessity. |     |     |     |     |     |
| -------------------- | --- | ---------- | --- | --- | --- | --- | --- |
| GridSearch(X,s,e,K)  |     |            |     |     |     | ˆ   | ˆ   |
Write for the routine returning the pair ( b,W), where b gives
the maximum contrast across all sub-intervals formed by a K-point grid on [s,e], and
W is that maximum. LABS-Grid replaces the proposal maximization in Algorithm 2 by
GridSearch(X,s,e,M) and the re-test maximization by GridSearch(X,s′,e′,R). In
each case it compares W with λ. It also replaces the short-interval guard by the condition
that the relevant grid search can be evaluated. Algorithm S1 of the supplement gives the
full procedure. A proposal search costs O{M2(e−s)} and a re-test search costs O{R2(e′−
s′)}. The typical overall cost under balanced splits is therefore O{(M2+R2)nlogn}. For
fixed small grids, such as those with M ≤ 5 used below, these are fixed multiples of the
| corresponding | LABS | costs. |     |     |     |     |     |
| ------------- | ---- | ------ | --- | --- | --- | --- | --- |
The same threshold λ is used at the proposal and re-test stages. Because ϕb has unit
(s,e]
norm, contrasts on sub-intervals of different lengths are directly comparable. A larger
grid searches more sub-intervals, however, so its finite-sample null distribution changes.
In Section 5 an information criterion selects from a threshold path and accounts for this
change. For a fixed-threshold implementation, the constant in λ may need to depend on
M and R.
A distinction between the grid-based extension and NOT concerns the number of sub-
intervals required for consistency. NOT draws M random intervals from the entire sample
9

and requires M → ∞ as n → ∞ to guarantee that at least one interval isolates each
change-point. Under the assumptions of Theorem 4.1, LABS is consistent even without
grid refinement, the case M = R = 2, because localization is provided by the look-ahead
rather than by interval sampling. Increasing M can improve finite-sample performance
but is not needed for consistency. Section S4 of the supplement extends the consistency
result for LABS (Section 4) to every fixed M,R ≥ 2. Its population recursion and
its assumptions concern proposal windows, so they depend on M. A re-test window
contains either no undetected kink or one undetected kink. With one kink, the full re-test
interval has the unique largest population contrast for every fixed R, and with no kink
the population contrast is zero. Thus no extra signal assumption is needed for R, and
R = 2 suffices. The proof uses the same threshold order for every fixed M and R.
4 Consistency of LABS
We now establish the consistency of LABS in the continuous piecewise-linear model of
Section2, withthecontrast(6). ThealgorithmanalyzedisAlgorithm2asstated, without
grid refinement, so the result applies to the case M = R = 2. For an extension to
M,R ≥ 2, see Section S4 of the supplement.
We work in the fixed change-point regime, formulated as a triangular array. Fix N, fix
q < ··· < q in (0,1) and non-zero reals d ,...,d , and put q = 0, q = 1 and
1 N 1 N 0 N+1
¯
δ = min (q − q ). When N ≥ 1, also put d = min |d | and d = max |d |.
min 0≤i≤N i+1 i j j j j
When N = 0, the signal is affine, meaning that it is a straight line, with a constant signal
included as a special case. For each n, let f be as in (1), with change-points τ = ⌊q n⌋,
j j
slope jumps ∆ := θ − θ = d /n, and independent, mean-zero, σ-sub-Gaussian
j j+1,2 j,2 j
errors. Let g be the continuous piecewise-linear function on [0,1] with kinks q and slope
j
jumps d . The overall level and initial slope of f and g are arbitrary. Adding a straight
j
line to the signal does not change the contrast, which is orthogonal to constant and
linear functions. Apart from this arbitrary component, f differs uniformly from g(t/n)
t
by O(n−1).
We prescribe ∆ = d /n exactly. If instead one sets f = g(t/n), the second difference at
j j t
τ is d (1−{nq })/n. It then depends on the fractional part of nq and can be arbitrarily
j j j j
small. The exact prescription avoids this accidental weakening of a slope change. All
rates below use |∆ | ≍ n−1. The threshold is
j
λ = λ = Θσ(8logn)1/2, Θ > 1 fixed. (8)
n
The factor 8 is a convenient, non-sharp proof constant, not a finite-sample calibration.
The proof applies a union bound, equivalent here to a Bonferroni bound, to at most n3
triples (s,e,b). Any fixed constant greater than 6 can replace 8 inside the square root and
10

still make that probability tend to one. Model selection via the strengthened Schwarz
Information Criterion (sSIC), introduced in Section 5.2 and analyzed theoretically in S5
| of the | supplement, |          | removes | the need | to       | select | a threshold. |     |     |
| ------ | ----------- | -------- | ------- | -------- | -------- | ------ | ------------ | --- | --- |
| 4.1    | Signal      | strength |         | on       | a window |        |              |     |     |
On a window (s,e], let B be the valid candidate set defined in Section 3.1. The contrast
s,e
ˆ
vector (5) is the unit vector ψ = ψ /∥ψ ∥, where ψ is the projection of the hinge (t−b)
|     |     |     |     | b   | b   | b   | b   |     | +   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
onto the orthogonal complement of the constant and linear functions on the window. For
| a kink | τ ∈ B | , set |     |     |     |     |     |     |     |
| ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
j s,e
|     |     |     |     | x = | min(τ | −s,e+1−τ |     | ),  |     |
| --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- |
|     |     |     |     | j   |       | j        |     | j   |     |
its distance from the nearer edge, and set x = 0 otherwise. Define
j
|     |     |     |     |     | ℓ (s,e) | =   | |∆ |∥ψ | ∥   |     |
| --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- |
|     |     |     |     |     | j       |     | j τj   |     |     |
as the signal strength of the kink on that window, and set ℓ (s,e) = 0 when τ ∈/ B .
|     |     |     |     |     |     |     |     | j j | s,e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)
Then max |⟨f,ψ ˆ ⟩| ≤ ℓ (s,e), with equality when exactly one kink is present.
|     | b∈Bs,e |     | b   | j j |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Thus detectability is governed by the signal strength. Section S2 of the supplement shows
| that there | are | absolute | constants |     | 0 < c | ≤ C | < ∞ such | that |     |
| ---------- | --- | -------- | --------- | --- | ----- | --- | -------- | ---- | --- |
ℓ ℓ
|     |     |     |     | |d |x3/2 |     |         |     | |d |x3/2 |     |
| --- | --- | --- | --- | -------- | --- | ------- | --- | -------- | --- |
|     |     |     |     | j        |     |         |     | j        |     |
|     |     |     |     | c j      | ≤   | ℓ (s,e) | ≤ C | j .      | (9) |
|     |     |     |     | ℓ        |     | j       |     | ℓ        |     |
|     |     |     |     | n        |     |         |     | n        |     |
Up to universal constant factors, signal strength is therefore determined by the distance
from the kink to the nearer edge, and grows as x3/2; the exact norm depends on both
| distances, | but | only | its order | is controlled |     | by  | x.  |     |     |
| ---------- | --- | ---- | --------- | ------------- | --- | --- | --- | --- | --- |
Write r¯ = (nlogn)1/2. Two regimes follow from (9): a kink within O(r¯ ) of a window
n n
O{n−1/4(logn)3/4} σ(8logn)1/2,
| edge has | signal | strength |     |     |     | =   | o(1), below | the noise level | and |
| -------- | ------ | -------- | --- | --- | --- | --- | ----------- | --------------- | --- |
is not detected. However, a kink at distance at least κn from both edges, for a constant
κ > 0, has signal strength at least c dκ3/2n1/2, above that level, and is detected. The two
ℓ
| regimes | are separated |     | by  | a factor | of order | n3/4(logn)−3/4. |     |     |     |
| ------- | ------------- | --- | --- | -------- | -------- | --------------- | --- | --- | --- |
What has to be shown is that LABS produces no window in which a kink falls between
ˆ ˆ
the two regimes. The only window edge a recursive call creates is b, and b is either within
O(r¯ ) of a kink or, under Assumption 4.2 below, at distance of order n from every kink.
n
| 4.2 | The | population |     | recursion |     |     |     |     |     |
| --- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
The assumptions below are imposed on the finitely many windows the recursion visits,
rather than on all intervals. These windows are described by a deterministic object
11

depending on the signal alone. For 0 ≤ α < β ≤ 1, let Ψαβ denote the continuum
v
analogue of ψ on (α,β). Let V(α,β) = {j : α < q < β} be the set of live kinks,
|     |     |     | b   |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
meaning the true kinks still lying strictly inside the current population window. Define
| the | noiseless | profile | and      | its leftmost | maximizer |     |                     |
| --- | --------- | ------- | -------- | ------------ | --------- | --- | ------------------- |
|     |           |         | (cid:68) |              | (cid:69)  |     |                     |
|     | ¯         |         | (cid:88) |              | (cid:14)  |     | (cid:12) ¯ (cid:12) |
D (v) = d Ψαβ, Ψαβ ∥Ψαβ∥ , c(α,β) = minargmax (cid:12)D (v) (cid:12). (10)
|     | αβ  |     |     | j qj | v v |     | αβ  |
| --- | --- | --- | --- | ---- | --- | --- | --- |
v
j∈V(α,β)
Definition 4.1 (Population LABS, POP) POP(α,β) returns ∅ if V(α,β) = ∅. Oth-
erwise it sets c = c(α,β) and computes L = POP(α,c) and R = POP(c,β); if both are
empty it returns {c}, and otherwise, with α′ = maxL if L ̸= ∅ and α′ = α else, and
β′ defined symmetrically, it returns L ∪ {c(α′,β′)} ∪ R when V(α′,β′) ̸= ∅ and L ∪ R
otherwise. Write T (g) for the set of windows at which POP is invoked, starting from
POP(0,1).
This is Algorithm 2 with “the contrast exceeds λ” criterion replaced by “the window
| contains |     | a kink | in its | interior”. |     |     |     |
| -------- | --- | ------ | ------ | ---------- | --- | --- | --- |
Proposition 4.1 If T (g) is finite and c(α,β) is well defined at each of its nodes, then
POP(α,β) = {q : j ∈ V(α,β)} at every node. In particular POP(0,1) = {q ,...,q }.
|     |     |     | j   |     |     |     | 1 N |
| --- | --- | --- | --- | --- | --- | --- | --- |
Proposition 4.1, proved in Section S3 of the supplement, makes precise the argument of
Section 3.1. If the split lands away from every kink, each child returns its own kinks,
the re-test interval falls between two consecutive detected kinks and so is empty, and the
spurious parent estimate is discarded. If instead the split lands on a kink, that kink is
detected by neither child and is recovered by the re-test, on an interval where it is the
| only | live | kink.       |     |     |                 |         |     |
| ---- | ---- | ----------- | --- | --- | --------------- | ------- | --- |
| 4.3  |      | Assumptions |     | and | the consistency | theorem |     |
Assumption 4.1 (Termination) The population recursion started at (0,1) terminates,
| that | is, | T (g) is | finite. |     |     |     |     |
| ---- | --- | -------- | ------- | --- | --- | --- | --- |
Assumption 4.2 (Non-degeneracy) For every (α,β) ∈ T (g) with V(α,β) ̸= ∅, the
|     |     | ¯   |     |     |     | ¯   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
function |D | has a unique maximizer c(α,β) on (α,β), and ∂2|D |(c(α,β)) < 0.
|     |     | αβ  |     |     |     | v αβ |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
Assumption 4.2 is the standard requirement that a population criterion have a well-
separated optimum; without it the sample maximizer need not converge at any rate.
Assumption 4.1 holds in particular whenever c(α,β) lies strictly between the extreme live
kinks at every node. In that case the population recursion tree T (g) of Definition 4.1,
whose nodes are the windows visited by POP, has depth at most N+1. Both assumptions
concern g alone, and neither refers to n, to the noise, or to any class of intervals.
12

Noconditionseparatingc(α,β)fromthechange-pointsisassumed. BecauseT (g)isfinite,
the quantity min |c(α,β)−q |, which at each node is either zero or strictly positive, has
l l
a strictly positive minimum over the nodes at which it does not vanish.
Theorem 4.1 Let X ,...,X follow (1) in the regime described above, and suppose As-
1 n
ˆ
sumptions 4.1 and 4.2 hold for g. Let T be the set returned by Algorithm 2 with the
n
contrast (6) and threshold (8), written in increasing order as τˆ < ··· < τˆ , where
(1) (Nˆ)
ˆ ˆ
N = |T |, and let τ < ··· < τ be the true change-points. Then there is a constant
n 1 N
C < ∞, depending only on g and σ, such that as n → ∞:
• if N ≥ 1:
(cid:18) (cid:19)
P N ˆ = N and max |τˆ −τ | ≤ C(nlogn)1/2 → 1;
(j) j
j=1,...,N
• if N = 0: P(N ˆ = 0) → 1.
The proof, given in Section S3 of the supplement, shows that the sample recursion follows
the population recursion: on an event of probability tending to one, every window LABS
visits has both endpoints within O(r¯ ) of n times the endpoints of a node of T (g), and
n
the call on it returns exactly the kinks live at that node, each localized to within O(r¯ ).
n
Remark 4.1 (Rate) The rate (nlogn)1/2 agrees with the refined single-change-point
rate of Baranowski et al. (2019), obtained in their Section 3.4 under additional regularity
and a more restrictive threshold choice, rather than the O {n2/3(logn)1/3} of their gen-
p
eral theorem. Thus LABS attains for N change-points the rate that the contrast attains
for one. A coarse comparison of the deterministic gap, meaning the loss in the noise-
less contrast away from its population maximum, with a global noise bound gives only
n3/4(logn)1/4. At that distance a kink can remain strong enough for a child recursion to
detect it again. The proof instead controls noise increments between nearby contrast vec-
tors and obtains the sharper (nlogn)1/2 rate. At this distance the kink’s signal strength
on the child window is o(1), so the duplicate detection does not occur.
Remark 4.2 (Scope) Theorem 4.1 covers Algorithm 2, equivalently LABS-Grid with
M = R = 2. Section S4 of the supplement proves the same conclusion for arbitrary fixed
M,R ≥ 2, under conditions of the same form imposed on the M-grid proposal recursion.
As explained there, the re-test contains at most one live kink, so no additional node-level
condition is required for R. Section S5 proves consistency when the model is chosen from
a solution path by the strengthened Schwarz criterion, as in Section 5.
13

| 5 Numerical |            | illustrations |     |     |     |     |
| ----------- | ---------- | ------------- | --- | --- | --- | --- |
| 5.1         | Simulation | design        |     |     |     |     |
We compare sSIC-selected LABS with five existing procedures on twelve piecewise-linear
scenarios. The scenarios comprise two null signals and five non-null signal families, each
of the latter considered at two noise levels. Table 1 summarizes the design and Figure 2
shows one realization of each. The trapezoid is the noisy analogue of the trap signal in
Section 2. The bump contains three closely spaced changes, the teeth signal contains
nineteen regularly spaced changes, and the irregular signal combines unequal segment
lengths with heterogeneous slopes. Each noise-free signal is constructed by cumulatively
summing its segment-wise slopes, so its change-points occur exactly at the cumulative
| segment | lengths in Table | 1.  |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- |
The two null scenarios differ in the presence of a global linear trend and in the noise scale,
which is 1 in 1a and 200 in 1b. Every method considered here uses a statistic that is
invariant to the addition of a linear function of the index and equivariant under rescaling,
and the threshold is scaled by σˆ, so scenario 1b serves as a check on those two properties
rather than as an independent scenario; the differences between the two null columns
| below | are Monte Carlo | variation. |     |     |     |     |
| ----- | --------------- | ---------- | --- | --- | --- | --- |
For all methods except CPOP we use 500 Monte Carlo replications per scenario. CPOP
is substantially slower, so it is run for 50 replications per scenario. It is applied to the
first 50 realizations used by the other methods, making those comparisons paired, but its
| estimates    | have appreciably | larger Monte  | Carlo uncertainty. |                 |         |     |
| ------------ | ---------------- | ------------- | ------------------ | --------------- | ------- | --- |
| Scenario     | Labels           | n N σ         | Segment slopes     | Segment         | lengths |     |
| Null, flat   | 1a               | 500 0 1       | (0)                | (500)           |         |     |
| Null, linear | 1b               | 500 0 200     | (1)                | (500)           |         |     |
| Single       | kink 2a/2b       | 400 1 50/100  | (0,1)              | (200,200)       |         |     |
| Trapezoid    | 3a/3b            | 600 2 50/100  | (1,0,−1)           | (200,200,200)   |         |     |
| Short bump   | 4a/4b            | 420 3 2/3     | (0,1,−1,0)         | (200,10,10,200) |         |     |
| Teeth        | 5a/5b            | 2000 19 50/70 | rep{(1,−1),10}     | rep{100,20}     |         |     |
Irregular slopes 6a/6b 1000 5 200/250 (2,−1,3,−2.5,0.5,−1.5) (100,300,100,200,150,150)
(cid:80)t
Table 1: Simulation scenarios. The noise-free signal is f = b , where b takes
|     |     |     |     | t   | s   | s   |
| --- | --- | --- | --- | --- | --- | --- |
s=1
the listed segment slopes for the listed numbers of observations. The change-points are
therefore the cumulative segment lengths, excluding n. The notation rep{x,k} means
that x is repeated k times. The noise is independent Gaussian with standard deviation
σ. Each non-null row represents two scenarios, with the lower noise level labeled “a” and
| the higher | level labeled | “b”. |     |     |     |     |
| ---------- | ------------- | ---- | --- | --- | --- | --- |
14

Signal families used in LABS_comparisons.R
Grey: noisy observation  |  Blue: noise−free trend  |  Red dashed: true change−points
|     |     | 1a. Null flat (n=500) |     | 1b. Null with slope (n=500, sigma=200) |     |     | 2a. Single kink (n=400, sigma=50) |     |
| --- | --- | --------------------- | --- | -------------------------------------- | --- | --- | --------------------------------- | --- |
300
| 2   |     |     |     |     |     | 200 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
500
| 0   |     |     |     |     |     | 100 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 0   |     |     | 0   |     |
−2
−100
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400
|     | 2b. Single kink (n=400, sigma=100) |     |     | 3a. Trapezoid (n=600, sigma=50) |     |     | 3b. Trapezoid (n=600, sigma=100) |     |
| --- | ---------------------------------- | --- | --- | ------------------------------- | --- | --- | -------------------------------- | --- |
400
|     |     |     | 300 |     |     | 400 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 200 |     |     | 200 |     |     |     |     |     |
200
100
0
|      |     |     |      | 0   |     |     | 0   |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- | --- |
| −200 |     |     | −100 |     |     |     |     |     |
−200
| eulaV | 0 100                     | 200 300 | 400 | 0 200                     | 400 | 600 | 0 200                        | 400 600 |
| ----- | ------------------------- | ------- | --- | ------------------------- | --- | --- | ---------------------------- | ------- |
|       | 4a. Bump (n=420, sigma=2) |         |     | 4b. Bump (n=420, sigma=3) |     |     | 5a. Teeth (n=2000, sigma=50) |         |
12
| 8   |     |     | 10  |     |     | 200 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4   |     |     |     | 5   |     | 100 |     |     |
| 0   |     |     |     | 0   |     |     |     |     |
0
−5
| −4  |     |     |     |     |     | −100 |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
−10
|     | 0 100                        | 200 300 | 400 | 0 100                                    | 200 300 | 400 | 0 500                                    | 1000 1500 2000 |
| --- | ---------------------------- | ------- | --- | ---------------------------------------- | ------- | --- | ---------------------------------------- | -------------- |
|     | 5b. Teeth (n=2000, sigma=70) |         |     | 6a. Irregular slopes (n=1000, sigma=200) |         |     | 6b. Irregular slopes (n=1000, sigma=250) |                |
| 200 |                              |         | 500 |                                          |         |     |                                          |                |
500
100
|     |     |     |     | 0   |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
| −100 |     |     | −500 |     |     | −500 |     |     |
| ---- | --- | --- | ---- | --- | --- | ---- | --- | --- |
−200
−1000
|     | 0 500 | 1000 1500 | 2000 | 0 250 | 500 750 | 1000 | 0 250 | 500 750 1000 |
| --- | ----- | --------- | ---- | ----- | ------- | ---- | ----- | ------------ |
Time index
Figure 2: One realization of each of the twelve scenarios of Table 1. Grey: observed data.
Blue: noise-free signal. Red dashed: true change-points. Vertical scales differ between
panels.
15

| 5.2 | Methods |     | and | model | selection |     |     |     |     |
| --- | ------- | --- | --- | ----- | --------- | --- | --- | --- | --- |
For the piecewise-linear contrast (6), define the robust noise estimator
|     |     |     |     |     |          | (cid:18) ∆2X | (cid:19) |     |     |
| --- | --- | --- | --- | --- | -------- | ------------ | -------- | --- | --- |
|     |     |     |     |     | σˆ = MAD |              | √        | ,   |     |
6
∆2X
where = X −2X +X and the MAD includes its usual Gaussian consistency
|         | t    | t+1      | t        | t−1 |         |          |     |     |     |
| ------- | ---- | -------- | -------- | --- | ------- | -------- | --- | --- | --- |
| factor. | Each | SIC-LABS | solution |     | path is | computed | at  |     |     |
(cid:112)
|     |     |     | λ = | aσˆ | 2logn, | a = | 0.50,0.55,...,1.50. |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ------------------- | --- | --- |
a
For every distinct change-point set T on this path, we fit a continuous piecewise-linear
| signal | and minimize |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|+3)(logn)1.01,
|     |     |     | sSIC(T ) | = nlog{RSS(T |     | )/n}+(2|T |     |     |     |
| --- | --- | --- | -------- | ------------ | --- | --------- | --- | --- | --- |
where RSS(T ) is the residual sum of squares from the least-squares continuous piecewise-
linear fit with change-point set T . This is the strengthened Schwarz information criterion
with exponent 1.01. We use “SIC”, “sSIC” and “strengthened SIC” for this criterion
below; the shorter SIC form is retained in method labels. The same continuous piecewise-
linear convention is used for NOT and IDetect in the breakfast R package (Anastasiou
et al., 2026). Section S5 of the supplement shows that the selected model is consistent,
at the rate of Theorem 4.1, provided the grid of multipliers reaches into the range of
thresholds admitted by that theorem; the exponent being strictly greater than one is what
separates the correct model from models with superfluous change-points. Section S5 also
treats a variant in which the path is generated over the whole range of thresholds, indexed
| by the | number | of  | change-points |     | and truncated | at  | a cap. |     |     |
| ------ | ------ | --- | ------------- | --- | ------------- | --- | ------ | --- | --- |
We use sSIC selection because preliminary experiments, not reported here, showed that
fixed thresholds either lost power or did not control false positives uniformly across the
signal scales. This also agrees with the usual role of information criteria in change-point
analysis: the threshold produces a solution path and the criterion selects its model size.
| We consider |            | five LABS | configurations: |            |       |            |     |            |             |
| ----------- | ---------- | --------- | --------------- | ---------- | ----- | ---------- | --- | ---------- | ----------- |
|             | LABS(SIC,M |           | = 2),           | LABS(SIC,M |       | =          | 3), | LABS(SIC,M | = 3,R = 2), |
|             |            |           | LABS(SIC,M      |            | = 5), | LABS(SIC,M |     | = 5,R =    | 2).         |
Here M is the proposal grid size and R is the grid size used at the look-ahead re-test;
when R is omitted, R = M. Every configuration applies the threshold in the proposal
| phase | and again | at  | the re-test. |     |     |     |     |     |     |
| ----- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
The external competitors are IDetect (Anastasiou and Fryzlewicz, 2022) with SIC model
selection, NOT(Baranowskietal.,2019)withSICmodelselection, TrendSegment(Maeng
16

andFryzlewicz,2024)initscontinuousandindependent-noisesetting, multiscaleMOSUM
(Kim et al., 2024a) with BIC bandwidth merging, and CPOP (Maidstone et al., 2019)
with penalty 2logn. For CPOP the noise standard deviation is estimated by the same
second-difference MAD used above. MOSUM is run using the implementation of Kim
et al. (2024a) with the tuning those authors recommend: η = 0.3, θ = 0.8, significance
level 0.05, and BIC bandwidth merging. Its bandwidths follow a Fibonacci sequence
G ,2G ,3G ,5G ,..., truncated before n/log n, where G = max{10,10⌈n/1000⌉}.
1 1 1 1 10 1
The numerical work used R 4.5.2 (R Core Team, 2025). The competitor package versions
were 1.0.8 for cpop (Fearnhead and Grose, 2024), 2.6 for breakfast (Anastasiou et al.,
2026) (IDetect and NOT), and 1.3.2 for trendsegmentR (Maeng and Fryzlewicz, 2026).
The MOSUM implementation was obtained from the authors’ MovingSumLin repository
(Kim et al., 2024b).
Two features of the MOSUM comparison should be borne in mind. First, MOSUM tests
jointly for a jump and a slope change at each candidate location, and has no variant
that imposes continuity, so unlike the other methods considered here it does not use the
knowledge that the signal is continuous. Second, its theory requires the change-points to
be separated by more than twice the bandwidth. For the bump signal, whose changes
are ten observations apart, no bandwidth in the recommended set satisfies this, so that
scenario lies outside the conditions under which the method is designed to operate; for
the teeth and irregular signals only the smallest bandwidths satisfy it. We retain the full
recommended bandwidth set in all cases, as the authors do in their own study, since the
BIC merging step demotes poorly fitting bandwidths.
Foreachreplicationwerecordtheabsoluteerrorintheestimatednumberofchange-points,
the directed location errors in both directions, their maximum (the Hausdorff distance),
and computation time. The principal measure below is the probability of estimating the
exact number of change-points. On a null signal its complement is the false-positive rate
(FPR).
5.3 Results
Table 2 gives null control and performance averaged over the ten non-null scenarios. All
methods control the FPR below 0.05. Each SIC-LABS variant has FPR 0.008 on both
null signals, and SIC-NOT has maximum null FPR 0.008. Under the specified bandwidth
sequence, MOSUM also controls the null, with FPR 0.002 on the flat signal and 0.006 on
the linear signal. CPOP has no false positive in its 50 flat-null replications and one in its
50 linear-null replications, giving FPR 0.020 on the latter.
CPOP has the highest mean exact-count probability, 0.844, but this estimate is based
on only 50 replications per scenario. Among the methods run for 500 replications, the
M = 5,R = 2 SIC-LABS version is highest, while being around 40 times faster than
17

Method Reps FlatFPR LinearFPR Exactcount Counterror Hausdorff Time(ms) CPOP/time
CPOP 50 0.000 0.020 0.844 0.202 46.10 1142.25 1.0
LABS(SIC,M =5,R=2) 500 0.008 0.008 0.827 0.351 46.15 28.50 40.1
LABS(SIC,M =5) 500 0.008 0.008 0.827 0.350 45.79 33.00 34.6
LABS(SIC,M =3) 500 0.008 0.008 0.792 0.519 58.24 11.00 103.8
LABS(SIC,M =3,R=2) 500 0.008 0.008 0.791 0.518 59.37 10.50 108.8
NOT(SIC) 500 0.008 0.002 0.726 0.921 57.19 108.50 10.5
LABS(SIC,M =2) 500 0.008 0.008 0.704 1.386 104.35 4.50 253.8
IDetect 500 0.002 0.000 0.662 1.068 93.78 23.00 49.7
TrendSegment 500 0.000 0.000 0.355 2.951 211.85 214.00 5.3
MOSUM 500 0.002 0.006 0.236 1.953 117.33 3.00 380.8
Table 2: Null false-positive rates, averages over the ten non-null scenarios, and computa-
tion times, ranked by mean exact-count probability. “Reps” is the number of replications
per scenario, “Exact count” is the mean probability of estimating the correct number of
change-points, “Count error” is the mean absolute count error, and “Hausdorff” is the
mean finite Hausdorff distance. “Time” is the median of the ten scenario-specific me-
dian wall-clock times, so that each signal receives equal weight, and “CPOP/time” is the
CPOP median divided by the method median. The common LABS solution-path prepa-
ration time is apportioned equally among the five LABS variants. Timings compare the
implementations used in the simulation and should not be read as hardware-independent
complexity measurements. The CPOP estimates have greater Monte Carlo uncertainty
because CPOP uses only 50 replications per scenario, compared with 500 for every other
method.
CPOP (more on execution times below). Its mean exact-count probability 0.827, followed
almost exactly by M = 5, also 0.827 after rounding. The M = 3 versions attain 0.791
to 0.792, followed by SIC-NOT (0.726), M = 2 LABS (0.704), and IDetect (0.662). The
R = 2 re-test therefore retains the accuracy of the full M = 5 re-test while reducing
computation. The gap between M = 2 and M = 5 is substantial, and is largest on
the teeth and bump signals, where the noise is frequently large enough for both child
recursions to return empty sets; as noted in Section 3.1, the look-ahead does not correct
the proposal in that configuration, and the grid search is what provides the localization
instead.
CPOP requires 1.142 seconds for a typical replication, compared with 28.5 milliseconds
for the M = 5,R = 2 LABS variant, a factor of about 40; the unrestricted M = 5 re-
test is about 35 times faster than CPOP. The difference persists on the largest and most
structurally complex signals: the maximum scenario median is 7.016 seconds for CPOP
against 0.134 seconds for the M = 5,R = 2 LABS variant. NOT and TrendSegment are
also slower than the recommended LABS version. MOSUM is the fastest method and
controls the null false-positive rate, but its mean exact-count probability is substantially
lower.
Table 3 reports the exact-count probability scenario by scenario. The M = 5 variants are
18

particularly effective on the dense teeth signals: their exact-count probabilities are 0.994
at σ = 50 and approximately 0.75 at σ = 70. The M = 5,R = 2 variant also leads the
methods run for 500 replications on both irregular-slope signals. The unrestricted M = 5
version is highest on the bump at σ = 3, while the smaller M = 2 grid is preferable on
the high-noise trapezoid, so no single grid size dominates in every geometry.
| Method |     |     | 2a  | 2b  | 3a  | 3b  | 4a 4b | 5a  | 5b  | 6a 6b |
| ------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- |
LABS(SIC,M =2) .996 .982 .984 .744 .952 .640 .762 .102 .576 .302
LABS(SIC,M =3) .992 .982 .984 .734 .978 .888 .972 .532 .574 .282
LABS(SIC,M =3,R=2) .992 .982 .984 .732 .978 .884 .972 .534 .574 .282
LABS(SIC,M =5) .994 .982 .982 .714 .984 .894 .994 .746 .646 .330
LABS(SIC,M =5,R=2) .994 .982 .982 .714 .982 .888 .994 .748 .652 .332
| IDetect  |     |     | .996 | .956 | .984 | .696 | .964 .514 | .916 | .212 | .284 .096 |
| -------- | --- | --- | ---- | ---- | ---- | ---- | --------- | ---- | ---- | --------- |
| NOT(SIC) |     |     | .992 | .976 | .994 | .728 | .984 .732 | .960 | .354 | .368 .174 |
TrendSegment .998 .654 .994 .302 .518 .076 .004 .000 .008 .000
| MOSUM |     |     | .916 | .042 | .854 | .022 | .120 .014 | .392 | .002 | .000 .000 |
| ----- | --- | --- | ---- | ---- | ---- | ---- | --------- | ---- | ---- | --------- |
| CPOP  |     |     | .980 | .940 | .960 | .780 | .980 .980 | .980 | .900 | .640 .300 |
Table 3: Probability of estimating the exact number of change-points in each non-null
scenario. Scenario labels are defined in Table 1. CPOP uses 50 replications per scenario;
| all other | methods | use | 500. |     |     |     |     |     |     |     |
| --------- | ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Overall, SIC model selection gives LABS good power without loss of null control. Among
the LABS variants, the M = 5,R = 2 version has the highest aggregate exact-count
performance of the methods run for 500 replications, is faster than M = 5,R = 5, and
improves on SIC-NOT and IDetect in the dense- and irregular-change settings. CPOP
performs well but is much slower, and its 50-replication estimates remain less precise than
| the 500-replication |             | comparisons |     | for | the other | methods. |             |     |           |     |
| ------------------- | ----------- | ----------- | --- | --- | --------- | -------- | ----------- | --- | --------- | --- |
| 6 Data              | application |             |     | –   | global    |          | temperature |     | anomalies |     |
We analyze the HadCRUT5 annual land–sea surface-temperature anomalies made avail-
able by Our World in Data (Ritchie et al., 2024). The series measure differences in
degrees Celsius from the 1861–1890 mean. We consider the World, Northern Hemisphere
and Southern Hemisphere series separately. Although the downloaded data run from 1850
to 2026, the 2026 observation represents an incomplete year, so the primary analysis uses
the 176 annual observations from 1850 to 2025. The grey bands in the top row of Figure 3
are the pointwise 95% uncertainty intervals supplied with the data; they are displayed for
| context but | are | not used | as observation-specific |     |     |     | weights. |     |     |     |
| ----------- | --- | -------- | ----------------------- | --- | --- | --- | -------- | --- | --- | --- |
We use the best-performing LABS version among the methods run for 500 replications
in Section 5, LABS(SIC,M = 5,R = 2), and all five external competitors from that
study: IDetect, NOT(SIC), TrendSegment, MOSUM and CPOP. The implementations
19

and tuning are unchanged from the simulation study. A reported change year is the first
| year of the | segment | following | the fitted | slope change.       |          |            |
| ----------- | ------- | --------- | ---------- | ------------------- | -------- | ---------- |
| Method      |         | World     |            | Northern Hemisphere | Southern | Hemisphere |
LABS(SIC, 1913, 1942, 1972 1863, 1877, 1884, 1918, 1881, 1910, 1942, 1965
| M = 5,R | = 2) |       |            | 1941, 1975       |            |     |
| ------- | ---- | ----- | ---------- | ---------------- | ---------- | --- |
| IDetect |      | 1914, | 1945, 1977 | 1919, 1945, 1977 | 1912, 1967 |     |
NOT(SIC) 1910, 1943, 1972 1914, 1941, 1975 1880, 1912, 1945, 1965
| TrendSegment |     | 1974  |            | 1937, 1977       | 1912        |      |
| ------------ | --- | ----- | ---------- | ---------------- | ----------- | ---- |
| MOSUM        |     | 1861, | 1911, 1969 | 1909, 1946, 1974 | 1912, 1940, | 1969 |
CPOP 1876, 1877, 1884, 1862, 1876, 1878, 1879, 1876, 1877, 1885, 1911,
|     |     | 1911, | 1942, 1968, | 1912, 1941, 1974 | 1914, 1933, | 1945, 1946, |
| --- | --- | ----- | ----------- | ---------------- | ----------- | ----------- |
|     |     | 2012  |             |                  | 1964, 2022  |             |
Table4: Firstyearsfollowingtheslopechangesdetectedinthethreetemperature-anomaly
series. All methods use the configurations from the simulation study.
For the World series, LABS detects changes in 1913, 1942 and 1972 (right-hand column
of Figure 3). Its fitted slopes over 1850–1912, 1913–1941, 1942–1971 and 1972–2025 are,
respectively, −0.020, 0.142, −0.039 and 0.205 degrees Celsius per decade. IDetect and
NOT place each of these three principal transitions within five years of LABS, while
MOSUM places the latter two in 1911 and 1969 and additionally reports an early change
in 1861. TrendSegment returns only the onset of the most recent warming trend, in 1974.
CPOP gives a much finer segmentation, including adjacent changes in the late nineteenth
| century | and an additional |     | recent change | in 2012. |     |     |
| ------- | ----------------- | --- | ------------- | -------- | --- | --- |
FortheNorthernHemisphere,LABSdetectssixchanges: 1863,1877,1884,1918,1941and
1975 (left-hand column of Figure 3). The three short, early segments have fitted slopes
of −0.247, 0.206 and −0.258 degrees Celsius per decade; from 1884 to 1917 the fitted
trend is nearly flat. The more persistent twentieth-century segments have slopes 0.220
over 1918–1940, −0.081 over 1941–1974, and 0.287 over 1975–2025. The other methods
concentrate on the same broad transitions in the 1910s, 1940s and 1970s: IDetect, NOT
and MOSUM each return one change in each period, and TrendSegment returns changes
in 1937 and 1977. The additional early LABS changes are supported in broad location
by CPOP, although CPOP again resolves them into several adjacent changes.
FortheSouthernHemisphere, LABSdetectschangesin1881, 1910, 1942and1965(middle
column of Figure 3). Its corresponding segment slopes are 0.027, −0.076, 0.114, −0.010
and 0.133 degrees Celsius per decade. NOT gives a particularly close result, with changes
in1880, 1912, 1945and1965. IDetectretainsthe1912and1967changes, MOSUMreturns
1912, 1940 and 1969, and TrendSegment retains only 1912. CPOP places changes near
these common locations but also returns several adjacent changes and one near the end
| of the series, | for | a total | of ten. |     |     |     |
| -------------- | --- | ------- | ------- | --- | --- | --- |
20

2
1
0
)C°(
tfi
SBAL
Northern Hemisphere Southern Hemisphere World
2
1
0
)C°(
stfi
rotitepmoC
LABS
IDetect
NOT(SIC)
TrendSegment
MOSUM
CPOP
1860 1900 1940 1980 2020
Year
dohteM
1860 1900 1940 1980 2020 1860 1900 1940 1980 2020
Year Year
IDetect NOT(SIC) TrendSegment MOSUM CPOP
Figure 3: Temperature anomalies and detected slope changes, 1850–2025. The columns
show, fromlefttoright, theNorthernHemisphere, SouthernHemisphereandWorldseries,
all on common vertical and horizontal scales. The top row shows the annual anomaly, its
supplied 95% uncertainty interval, the LABS fit, and dotted lines at the LABS changes.
The middle row superimposes the five competitor fits; for comparability, each is the
continuous piecewise-linear least-squares refit at that method’s estimated change-points.
The bottom row shows the change-point locations for all six methods. CPOP’s automatic
0 and n−1 boundaries are omitted.
21

Taken together, the three analyses give a common chronology: early twentieth-century
warming, amid-centuryflatteningorreversal, andrenewedwarminginthelatertwentieth
century. The principal differences are in timing and magnitude. LABS places the onset
of the latest sustained warming in 1965 in the Southern Hemisphere, seven years before
the World change and ten years before the Northern Hemisphere change. The subsequent
Northern Hemisphere slope, 0.287 degrees Celsius per decade, is more than twice the
Southern Hemisphere slope of 0.133, with the World slope intermediate at 0.205. The
Northern series also has more short-lived nineteenth-century features, on which the meth-
ods agree less strongly. Across regions, LABS, IDetect, NOT and MOSUM broadly agree
on the major twentieth-century changes; TrendSegment favors fewer changes, whereas
CPOP systematically favors a finer segmentation. Including the incomplete 2026 value
in a sensitivity analysis leaves this principal twentieth-century comparison unchanged,
although it affects some fine early Northern Hemisphere changes and CPOP’s finer seg-
mentation.
Declarations
Funding. No funding was received. Competing interests. None. Generative AI
use. OpenAI Codex (gpt-5.6-sol) and Anthropic’s Opus 5 assisted with drafting and
checking prose and mathematical proofs, R implementation, and numerical studies, for
clarity and verification. The author reviewed, revised, and independently checked all AI
output and takes full responsibility. Data and code. HadCRUT5 data are from Our
World in Data (Ritchie et al., 2024); code, frozen data files, and simulation output are
available at https://github.com/pfryz/LABS.
22

Supplement to “LABS: Extending the scope of binary segmentation via a look-ahead de-
vice” Piotr FryzlewiczDepartment of Statistics, London School of Economics and Political
Science, London WC2A 2AE, UK. Correspondence: p.fryzlewicz@lse.ac.uk. ORCID:
0000-0002-9676-902X.
Abstract
This document supplements the main paper. Section S1 states the LABS-Grid
algorithm in full. Section S2 establishes the properties of the contrast used in the
consistency proof. Section S3 proves Proposition 4.1 and Theorem 4.1. Section S4
extends the consistency result to LABS-Grid. Section S5 treats selection from a
solution path by a strengthened Schwarz criterion. Section S6 describes related
uses of look-ahead in other algorithmic settings.
Keywords: Binary segmentation, change-point detection, piecewise-linear signal,
recursive algorithm, trend estimation.
Numbered items of the form “Assumption 4.1”, “Theorem 4.1” and “Algorithm 2” refer
to the main paper; items numbered with an S prefix refer to this document. Displayed
equations (4) and (5) of the main paper are the contrast vector and the contrast function.
S1 The LABS-Grid algorithm
Section 3.2 of the main paper describes LABS-Grid. It evaluates the proposal contrast on
all sub-intervals formed by an M-point equally spaced grid, and the re-test contrast on
those formed by an R-point grid. For completeness, the algorithm is stated in full below.
Here GridSearch(X,s,e,K) returns the pair ( ˆ b,W), where ˆ b is the location giving the
maximum contrast across all sub-intervals formed by the K-point grid and W is that
maximum. Setting M = R = 2 recovers Algorithm 2 of the main paper, which is the
algorithm analyzed in Theorem 4.1.
23

Algorithm S1 LABS with grid-based contrast evaluation (LABS-Grid)
| 1: function |     | LABS-Grid(X,s,e,λ,M,R) |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2: if the M-grid search cannot be evaluated on (s,e] (interval too short) then
| 3:                            | return | ∅    |     |     |     |     |     |     |     |            |            |          |
| ----------------------------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------- |
| 4: end                        | if     |      |     |     |     |     |     |     |     |            |            |          |
| 5: (ˆb,W)←GridSearch(X,s,e,M) |        |      |     |     |     |     |     |     |     | ▷ Proposal | search     | on (s,e] |
| 6: if                         | W >λ   | then |     |     |     |     |     |     |     |            | ▷ Proposal | phase    |
LABS-Grid(X,s,ˆb,λ,M,R)
| 7:  | L←  |                         |      |      |     |     |     |     |              |     |            |       |
| --- | --- | ----------------------- | ---- | ---- | --- | --- | --- | --- | ------------ | --- | ---------- | ----- |
| 8:  | R←  | LABS-Grid(X,ˆb,e,λ,M,R) |      |      |     |     |     |     |              |     |            |       |
| 9:  |     |                         |      |      |     |     |     |     | ▷ Look-ahead |     | refinement | phase |
| 10: | if  | L̸=∅ or                 | R̸=∅ | then |     |     |     |     |              |     |            |       |
(cid:40)
|     |     |      | max(L) | if L̸=∅   |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11: |     | s′ ← |        |           |     |     |     |     |     |     |     |     |
|     |     |      | s      | otherwise |     |     |     |     |     |     |     |     |
(cid:40)
|     |     |      | min(R) | if R̸=∅   |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12: |     | e′ ← |        |           |     |     |     |     |     |     |     |     |
|     |     |      | e      | otherwise |     |     |     |     |     |     |     |     |
(s′,e′]
| 13: |     | if the                         | R-grid search | can | be evaluated | on  | then |     |     |        |         |            |
| --- | --- | ------------------------------ | ------------- | --- | ------------ | --- | ---- | --- | --- | ------ | ------- | ---------- |
| 14: |     | (ˆb′,W′)←GridSearch(X,s′,e′,R) |               |     |              |     |      |     |     | ▷ Grid | re-test | on (s′,e′] |
W′
| 15: |     | if     | >λ then |           |     |     |     |           |         |          |         |          |
| --- | --- | ------ | ------- | --------- | --- | --- | --- | --------- | ------- | -------- | ------- | -------- |
| 16: |     |        | return  | L∪{ˆb′}∪R |     |     |     |           |         | ▷ Accept | refined | estimate |
| 17: |     | end    | if      |           |     |     |     |           |         |          |         |          |
| 18: |     | end if |         |           |     |     |     |           |         |          |         |          |
| 19: |     | return | L∪R     |           |     |     |     | ▷ Re-test | failed: | discard  | parent  | estimate |
| 20: | end | if     |         |           |     |     |     |           |         |          |         |          |
L∪{ˆb}∪R
| 21: | return |     |     |     |     |     | ▷ Both | children | empty: |     | keep parent | estimate |
| --- | ------ | --- | --- | --- | --- | --- | ------ | -------- | ------ | --- | ----------- | -------- |
22: else
| 23: | return | ∅   |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24: | end if |     |     |     |     |     |     |     |     |     |     |     |
25: end function
|     |     |     |     |     |     | O{M2(e |     |     | O{R2(e′ |     | s′)}, |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | ------- | --- | ----- | --- |
The proposal and re-test searches cost − s)} and − respectively.
Under balanced recursive splits the typical total cost is O{(M2 + R2)nlogn}, and the
worst-case cost is O{(M2 + R2)n2}. Ordinary binary segmentation also has worst-case
cost O(n2) when successive splits are maximally unbalanced. In the notation of the main
| paper, | an omitted |     | R means    | R = | M.  |     |     |          |     |     |     |     |
| ------ | ---------- | --- | ---------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
| S2     | Auxiliary  |     | properties |     |     | of  | the | contrast |     |     |     |     |
This section collects the four properties of the piecewise-linear GLR contrast (5) of the
main paper that are used in the proof. Throughout, (s,e] is a window, W = {s+1,...,e},
m = e − s, and B = {s + 2,...,e − 1}; Π⊥ is orthogonal projection in RW onto the
|            |     |            | s,e |            |       | W       |     |      |        |     |     |     |
| ---------- | --- | ---------- | --- | ---------- | ----- | ------- | --- | ---- | ------ | --- | --- | --- |
| orthogonal |     | complement | of  | span{1,t}; |       | and     |     |      |        |     |     |     |
|            |     |            |     | Π⊥ (cid:2) |       | (cid:3) | ˆ   |      |        |     |     |     |
|            |     |            | ψ   | :=         | (t−θ) | ,       | ψ   | := ψ | /∥ψ ∥. |     |     |     |
|            |     |            | θ   | W          |       | + t∈W   | θ   | θ    | θ      |     |     |     |
24

The contrast vector ϕb of the main paper equals −ψ ˆ , extended by zero off W; with
(s,e] b
ˆ
the opposite hinge convention it would equal +ψ . Either way it is the unit vector in
b
RW orthogonal to 1 and t that is continuous and piecewise linear with its only knot at
b, which is the defining property of the closed forms (4) and (5) there, and the sign is
ˆ
immaterial because the contrast takes an absolute value: C (b) = |⟨X,ψ ⟩|.
s,e b
For a kink τ , define its distance from the nearer end of W by
j
x (s,e) := min(τ −s,e+1−τ ) if τ ∈ B ,
j j j j s,e
and set x (s,e) := 0 otherwise. Its signal strength on (s,e] is ℓ (s,e) := |∆ |∥ψ ∥ when
j j j τj
τ ∈ B , and zero otherwise. As in Section 4.1 of the main paper, d := min |d | and
j s,e j j
¯
d := max |d | when N ≥ 1.
j j
S2.1 Which kinks the window sees
Lemma S2.1 (Representation) Let V(s,e) := {j : s+2 ≤ τ ≤ e−1}. Then:
j
(a) there are a,c ∈ R with f = a + ct + (cid:80) ∆ (t − τ ) for t ∈ W, and hence
t j∈V(s,e) j j +
ˆ (cid:80) ˆ
⟨f,ψ ⟩ = ∆ ⟨ψ ,ψ ⟩ for every b ∈ B ;
b j∈V(s,e) j τj b s,e
(b) max |⟨f,ψ ˆ ⟩| ≤ (cid:80) ℓ (s,e), and for any U and any b,b′ ∈ B ,
b b j j s,e
(cid:12)(cid:88) (cid:12) (cid:16)(cid:88) (cid:17)
(cid:12) ∆ ⟨ψ ,ψ ˆ −ψ ˆ ⟩(cid:12) ≤ ℓ (s,e) ∥ψ ˆ −ψ ˆ ∥;
(cid:12) j τj b b′ (cid:12) j b b′
j∈/U j∈/U
ˆ ˆ
(c) if V(s,e) = ∅ then ⟨f,ψ ⟩ = 0 for every b; and if V(s,e) = {j} then max |⟨f,ψ ⟩| =
b b b
ℓ (s,e), attained at b = τ and there only.
j j
Proof. Write ∇f = f −f , which is constant on each linear segment and changes value
t t t−1
between t = τ and t = τ +1. Such a change is visible within {∇f : t ∈ {s+2,...,e}}
i i t
precisely when s + 2 ≤ τ ≤ e − 1, that is, precisely when i ∈ V(s,e). The two sides
i
of the identity in (a) agree at t = s + 1 and have the same increments throughout W;
ˆ
since ψ ⊥ {1,t} the affine part, meaning the function a+ct, is annihilated, which gives
b
the displayed formula. Part (b) is Cauchy–Schwarz term by term. In (c), the first claim
ˆ
is immediate; for the second, Cauchy–Schwarz gives |⟨ψ ,ψ ⟩| ≤ ∥ψ ∥ with equality if
τj b τj
and only if ψ ∥ ψ , where ∥ means that the two non-zero vectors are scalar multiples of
b τj
one another. Distinct projected hinges ψ and ψ are not scalar multiples, because their
b τj
discrete second differences have knots at different locations. Equality therefore occurs
only at b = τ . □
j
25

The two sets have different types of elements, but their relevant locations coincide:
{τ : j ∈ V(s,e)} = {τ : τ ∈ B }.
j j j s,e
Here an admissible candidate location is an integer in B = {s + 2,...,e − 1}, the
s,e
range over which the contrast is maximized. Thus a kink contributes a hinge term to the
contrast representation precisely when its location belongs to the candidate range. Part
(c) also shows that the noiseless contrast vanishes identically when this set is empty.
S2.2 Signal strength
Lemma S2.2 (Norm and signal strength law) Let k = τ − s and k′ = e − τ, so
k+k′ = m, and put a = k, b = k′+1 and x = min(a,b), the distance from τ to the nearer
end of W; the asymmetry is that of the hinge. Then
ab(a−1)(b−1)(2ab−a−b+2)
∥ψ ∥2 = , (S1)
τ
6(a+b−2)(a+b−1)(a+b)
and consequently, for x ≥ 2,
|d |x3/2 |d |x3/2
c x3/2 ≤ ∥ψ ∥ ≤ C x3/2, c j j ≤ ℓ (s,e) ≤ C j j , (S2)
ℓ τ ℓ ℓ j ℓ
n n
with the absolute constants c = 192−1/2 and C = 3−1/2. In the rescaled continuum limit
ℓ ℓ
∥Ψ ∥2 = v3(1−v)3/3 on [0,1], so ∥Ψ ∥ ≍ {min(v,1−v)}3/2.
v v
Proof. In local coordinates {1,...,m} put S = m, S = (cid:80) t, S = (cid:80) t2, and let g ,g ,g
0 1 2 0 1 2
be the inner products of the hinge (t−k) with 1, t and itself. Then
+
S g2 −2S g g +S g2 m2(m2 −1)
∥ψ ∥2 = g − 2 0 1 0 1 0 1, S S −S2 = ,
τ 2 S S −S2 0 2 1 12
0 2 1
with g = k′(k′+1)/2, g = k′(k′+1)(2k′+1)/6 and g = kk′(k′+1)/2+g . Substituting
0 2 1 2
and simplifying gives (S1).
For (S2), write y = max(a,b) and note that a,b ≥ 2 when x ≥ 2, so that
(a−1)(b−1) ≥ 1ab, ab ≤ 2ab−a−b+2 ≤ 2ab,
4
y3 ≤ (a+b−2)(a+b−1)(a+b) ≤ 8y3.
The first holds because u − 1 ≥ u/2 for u ≥ 2; the second because ab − a − b + 2 =
(a−1)(b−1)+1 > 0 and a+b ≥ 2; the third because a+b−2 ≥ y, again by x ≥ 2, and
a+b ≤ 2y. Inserting these three in (S1) and using a3b3 = x3y3,
x3 ab· 1ab·ab ab·ab·2ab x3
= 4 ≤ ∥ψ ∥2 ≤ = .
192 48y3 τ 6y3 3
26

These constants are not sharp. The signal strength bounds follow from |∆ | = |d |/n. □
|       |       |             |     |     |     |     |     |     |     |     | j   | j   |
| ----- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Write | r¯ := | (nlogn)1/2. |     |     |     |     |     |     |     |     |     |     |
n
Corollary S2.1 (The two signal-strength regimes) Suppose N ≥ 1. Fix C > 0
⋆
(nlogn)1/2.
and κ > 0, and recall that r¯ = There is n such that for n ≥ n , every
|        |            |     |       | n      |          |     |     |     | 0   |     |     | 0   |
| ------ | ---------- | --- | ----- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| window | (s,e]      | and | every | kink j | satisfy: |     |     |     |     |     |     |     |
| (a)    | if x (s,e) | ≤   | C r¯  | , then |          |     |     |     |     |     |     |     |
|        | j          |     | ⋆ n   |        |          |     |     |     |     |     |     |     |
¯ C3/2n−1/4(logn)3/4
|     |            |     |          | ℓ (s,e) | ≤   | C d          |     |     |     | = o(1); |     |     |
| --- | ---------- | --- | -------- | ------- | --- | ------------ | --- | --- | --- | ------- | --- | --- |
|     |            |     |          | j       |     | ℓ            | ⋆   |     |     |         |     |     |
| (b) | if x (s,e) | ≥   | κn, then | ℓ (s,e) | ≥   | c dκ3/2n1/2. |     |     |     |         |     |     |
|     | j          |     |          | j       |     | ℓ            |     |     |     |         |     |     |
Proof. Both conclusions follow directly from the bounds for ℓ (s,e) in (S2). For (a),
j
|     |     |     | (nlogn)1/2 |     |     |     | ¯   |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
substitute x ≤ C and |d | ≤ d in the upper bound. For (b), substitute
|     |     | j   | ⋆   |     |     | j   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
□
| x ≥ κn | and       | |d | ≥   | d in | the lower        | bound.  |           |           |       |         |     |                |           |
| ------ | --------- | -------- | ---- | ---------------- | ------- | --------- | --------- | ----- | ------- | --- | -------------- | --------- |
| j      |           | j        |      |                  |         |           |           |       |         |     |                |           |
| S2.3   | Noise     |          |      |                  |         |           |           |       |         |     |                |           |
| Lemma  | S2.3      | (Uniform |      | noise            | bounds) |           | Let       |       |         |     |                |           |
|        |           |          |      |                  |         |           |           |       | ˆ       | ˆ   |                |           |
|        | (cid:110) |          |      |                  |         | (cid:111) | (cid:110) | |⟨ε,ψ | −ψ      | ⟩|  |                | (cid:111) |
| E      | :=        | max|⟨ε,ψ | ˆ    | ⟩| ≤ σ(8logn)1/2 |         | ∩         | max       |       | b       | b′  | ≤ σ(10logn)1/2 | ,         |
|        | n         |          | b    |                  |         |           |           |       |         |     |                |           |
|        |           | s,e,b    |      |                  |         |           | s,e,b̸=b′ |       | ∥ψ ˆ −ψ | ˆ ∥ |                |           |
|        |           |          |      |                  |         |           |           |       | b       | b′  |                |           |
the maxima being over all 0 ≤ s < e ≤ n and b,b′ ∈ B . Then P(E ) → 1. Write
|     |     |     |     |     |     |     |     |     | s,e |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Z := σ(8logn)1/2.
n
Eexp(tε
Proof. The assumption that each error is σ-sub-Gaussian means that ) ≤
i
exp(σ2t2/2)
for every real t. Independence then implies that a linear combination ⟨ε,v⟩ is
σ∥v∥-sub-Gaussian. In particular, each ψ ˆ is a unit vector, so ⟨ε,ψ ˆ ⟩ is σ-sub-Gaussian.
|     |     |     |     |     |     | b   |     |     |     |     | b   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
There are at most n3 triples, so the first event fails with probability at most 2n3e−4logn =
2/n. Likewise ⟨ε,ψ ˆ −ψ ˆ ⟩ is σ∥ψ ˆ −ψ ˆ ∥-sub-Gaussian and there are at most n4 quadru-
|     |     |     | b   | b′  | b   | b′  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ples, so the second fails with probability at most 2n4e−5logn = 2/n. □
The constant 8 in the first bound is not sharp. If it is replaced by a fixed constant
C > 6, the sub-Gaussian tail bound and the union bound give failure probability at most
2n3n−C/2 = 2n3−C/2, which tends to zero. The constant comes from this union bound over
all triples (s,e,b), not from the finite-sample threshold calibration used for the Narrowest-
Over-Threshold (NOT) method of Baranowski et al. (2019) or in the simulation study.
27

The second bound yields the rate r¯ in place of the weaker n3/4(logn)1/4 discussed in
n
Remark4.1ofthemainpaper. Therelevantindexsetconsistsofthequadruples(s,e,b,b′)
with b,b′ ∈ B , and has cardinality at most n4. A union bound over this finite set
s,e
therefore suffices. No chaining bound for the supremum of a stochastic process is needed;
see, for example, Section 2.2 of van der Vaart and Wellner (1996) for that concept.
S2.4 Separation
ˆ ˆ
Lemma S2.4 (Two-sided separation) Write ρ(θ,b) = |⟨ψ ,ψ ⟩|. There are absolute
θ b
constants c > 0 and C < ∞ such that for every window, every θ with x := min(θ −
0 0
s,e+1−θ) ≥ 2, and every b ∈ B ,
s,e
(cid:110)(cid:16)b−θ(cid:17)2 (cid:111) (cid:16)b−θ(cid:17)2
c min ,1 ≤ 1−ρ(θ,b) ≤ C .
0 0
x x
Proof. The lemma is proved in Section S2.6, from the exact identity of Lemma S2.5(b),
with the explicit constants c = 27/2048 and C = 576/7; Corollary S2.2 is the corre-
0 0
sponding continuum statement. The following indicates the shape of the argument in
the continuum. Rescale W to [0,1], u = (θ − s)/m, v = (b − s)/m. By Lemma S3.1
the discrete inner products agree with m3 times their continuum values up to relative
error O{1/(γm)} on u ∈ [γ,1 − γ]. The map θ (cid:55)→ Ψ is differentiable in L2 with
θ
∂ Ψ = −Π⊥1 , of norm bounded above and below on compact subsets of (0,1),
u u {·>u}
so 1 − ρ(u,v) = 1ς(u)(u − v)2 + O(|u − v|3) with ς bounded above and below, giving
2
both bounds for |u − v| small. For |u − v| bounded away from zero, ρ < 1 because Ψ
u
and Ψ are not parallel, meaning that they are not non-zero scalar multiples. This is the
v
strict case of the Cauchy–Schwarz inequality, and follows here because the two projected
hinges have different knots. The continuous positive function 1−ρ(u,v) attains a positive
minimum on the relevant compact set by the extreme-value theorem. If |u−v| ≥ δ > 0,
the upper bound follows from 1−ρ ≤ 1 ≤ δ−2(u−v)2. The scale-free form, with x rather
than m in the denominator, holds because near an edge Ψ depends on the window only
θ
through the distance to that edge, up to the same relative error. □
S2.5 Exact Gram identities
Lemma S2.2 gave the norm ∥ψ ∥ in closed form. The Gram matrix of vectors v ,...,v
τ 1 k
is the matrix with entries ⟨v ,v ⟩. Its off-diagonal entries are equally explicit here, as is
i j
the determinant of the 2×2 Gram matrix for a pair of contrast vectors; this determinant
controls ρ. This subsection records those identities and uses them to prove Lemma S2.4
in the continuum.
28

Lemma S2.5 (Gram determinants) (a) Continuum. For 0 < u ≤ v < 1, with Ψ
| formed |      | on [0,1], |     |      |            |     |            |     |        |     |            |     |
| ------ | ---- | --------- | --- | ---- | ---------- | --- | ---------- | --- | ------ | --- | ---------- | --- |
|        |      |           |     |      | u3(1−v)3(v |     | −u)2Q(u,v) |     |        |     |            |     |
|        | ∥2∥Ψ | ∥2        |     | ⟩2   |            |     |            |     |        |     |            |     |
|        | ∥Ψ   |           | −⟨Ψ | ,Ψ = |            |     |            | ,   | Q(u,v) | :=  | 4v −u−3uv, |     |
|        | u    | v         |     | u v  |            | 36  |            |     |        |     |            |     |
and consequently
−u)2Q(u,v)
(v
|     | 1−ρ(u,v)2 |     | =   |     |     | , with |     | 3u(1−u) | ≤ Q(u,v) |     | ≤ 4. | (S3) |
| --- | --------- | --- | --- | --- | --- | ------ | --- | ------- | -------- | --- | ---- | ---- |
4(1−u)3v3
(b) Discrete. Let 1 ≤ k < l ≤ m−1 and put a = k, c = l−k and b = m−l+1, so that
| a+b+c |     | = m+1. |     | Then |     |     |     |     |     |     |     |     |
| ----- | --- | ------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
abc(a−1)(b−1)P(a,b,c)
|     |     | ∥ψ ∥2∥ψ | ∥2  | −⟨ψ ,ψ | ⟩2 = |     |     |     |     |     | ,   |     |
| --- | --- | ------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     | k       | l   | k      | l    |     |     |     |     |     |     |     |
36(a+b+c)(a+b+c−1)2(a+b+c−2)
where
|     |     |          |     | 3a2b2c+4a2bc2 |             | −3a2bc+2a2b−2a2c2 |        |          | +3a2c−a2   |     |     |     |
| --- | --- | -------- | --- | ------------- | ----------- | ----------------- | ------ | -------- | ---------- | --- | --- | --- |
|     |     | P(a,b,c) |     | =             |             |                   |        |          |            |     |     |     |
|     |     |          |     | +4ab2c2       | −3ab2c+2ab2 |                   | +4abc3 | −8abc2   | +11abc−4ab |     |     |     |
|     |     |          |     | −2ac3         | +6ac2       | −7ac+3a−2b2c2     |        | +3b2c−b2 |            |     |     |     |
|     |     |          |     | −2bc3         | +6bc2       | −7bc+3b+c3        |        | −4c2     | +5c−2.     |     |     |     |
abc(3ab+4ac+4bc+4c2),
| Its | terms | of top     | degree | are      |     |                 |     | and     | with u = | a/m, | v = (a+c)/m |     |
| --- | ----- | ---------- | ------ | -------- | --- | --------------- | --- | ------- | -------- | ---- | ----------- | --- |
| and | m     | = a+b+c−1, |        |          |     |                 |     |         |          |      |             |     |
|     |       |            |        | m2Q(u,v) |     | 3ab+4ac+4bc+4c2 |     |         |          |      |             |     |
|     |       |            |        |          | =   |                 |     | −3a−4c, |          |      |             |     |
The determinant here is the left-hand side of part (b), namely the determinant of the
2×2 Gram matrix of ψ and ψ . Each squared norm and each inner product is of order
|     |     |     |     | k   | l   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m3, so every term in that determinant is of order m6. Equivalently, the numerator in
m6,
part (b) has total degree ten and the denominator has degree four. After division by
its highest-degree terms give the continuum determinant in part (a), with u = a/m and
v = (a+c)/m.
(c) Positivity. For 1 ≤ b ≤ b ≤ m−1, put a = b , c = b −b and d = m−b +1. Then
|     |     |       |     | 1            | 2   |                       |     | 1 2 | 1   |     | 2       |     |
| --- | --- | ----- | --- | ------------ | --- | --------------------- | --- | --- | --- | --- | ------- | --- |
|     |     |       |     |              |     | (cid:8)               |     |     |     |     | (cid:9) |     |
|     |     |       |     | ad(a−1)(d−1) |     | 2ad−a−d+2+3c(a+d+c−1) |     |     |     |     |         |     |
|     |     | ⟨ψ ,ψ | ⟩   | =            |     |                       |     |     |     |     | ,       |     |
|     |     | b1    | b2  |              |     |                       |     |     |     |     |         |     |
6(a+d+c−2)(a+d+c−1)(a+d+c)
which is strictly positive whenever a,d ≥ 2, that is whenever b ,b ∈ B . In particular
|     |      |      |       |         |          |       |         |     | 1 2 | s,e |     |     |
| --- | ---- | ---- | ----- | ------- | -------- | ----- | ------- | --- | --- | --- | --- | --- |
|     |      | ˆ    | ˆ     |         |          |       |         |     |     |     |     |     |
| ρ(b | ,b ) | = ⟨ψ | ,ψ ⟩, | with no | absolute | value | needed. |     |     |     |     |     |
|     | 1 2  | b1   | b2    |         |          |       |         |     |     |     |     |     |
29

Proof. (a) Substitute the closed forms of Lemma S3.1 for ∥Ψ ∥2 = u3(1−u)3/3 and for
u
⟨Ψ ,Ψ ⟩intotheleft-handsideandsimplify; thisisacomputationwithpolynomialsintwo
u v
variables. Dividing by ∥Ψ ∥2∥Ψ ∥2 = u3(1−u)3v3(1−v)3/9 gives (S3). For the bounds on
|     |     |     | u   | v   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Q, writeQ = v(4−3u)−u; sincev ≥ uand4−3u > 0wegetQ ≥ u(4−3u)−u = 3u(1−u),
and Q ≤ 4v ≤ 4. The case u > v follows from the reflection w (cid:55)→ 1 − w, under which
| Ψ (cid:55)→ | ±Ψ and | hence | ρ(u,v) | = ρ(1−u,1−v). |     |     |     |     |     |     |     |     |
| ----------- | ------ | ----- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| w           | 1−w    |       |        |               |     |     |     |     |     |     |     |     |
(b) The same computation with the explicit sums of the proof of Lemma S2.2 in place
of the integrals; it is a computation with polynomials in three variables. The identity for
m2Q follows by substituting m = a+b+c−1 into m2Q = 3a(m−a−c)+4cm.
(c) In local coordinates, let h = [(t−b) ]m , define g := ⟨h ,1⟩ and g := ⟨h ,t⟩, and
|     |           |     |     | b   | +   |     |     | 0,b | b   | 1,b | b   |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | (cid:80)m |     |     |     | t=1 |     |     |     |     |     |     |     |
retain S = tr for r = 0,1,2. Orthogonal projection away from span{1,t} gives
r
t=1
|     |         |      |       | S g    | g    | −S (g | g    | +g    | g )+S     | g   | g          |     |
| --- | ------- | ---- | ----- | ------ | ---- | ----- | ---- | ----- | --------- | --- | ---------- | --- |
|     |         |      |       | 2 0,b1 | 0,b2 | 1     | 0,b1 | 1,b2  | 1,b1 0,b2 | 0   | 1,b1 1,b2. |     |
|     | ⟨ψ ,ψ ⟩ | = ⟨h | ,h ⟩− |        |      |       |      |       |           |     |            |     |
|     | b1 b2   |      | b1 b2 |        |      |       | S    | S −S2 |           |     |            |     |
|     |         |      |       |        |      |       |      | 0 2   |           |     |            |     |
1
Substitution of the finite-sum formulae for these quantities and symbolic simplification
gives the expression in part (c), valid for every m. Setting c = 0, so that b = b ,
|     |     |     |     |     |     |     |     |     |     |     | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recovers the norm formula of Lemma S2.2. The identity was also verified in exact rational
arithmeticateveryadmissiblepairfor4 ≤ m < 30. Forpositivity, a−1 ≥ 1andd−1 ≥ 1;
2ad−a−d+2 = a(2d−1)−d+2 ≥ 3d > 0; 3c(a+d+c−1) ≥ 0; and a+d+c−2 ≥ 2,
| so the | denominator | is  | positive. |     |     |     |     |     |     |     |     | □   |
| ------ | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1].
Corollary S2.2 (Separation in the continuum) Let ϱ ∈ (0, For every u ∈ [ϱ,1−
2
| ϱ] and | every v ∈ | (0,1), |          |     |          |     |     |            |     |     |     |     |
| ------ | --------- | ------ | -------- | --- | -------- | --- | --- | ---------- | --- | --- | --- | --- |
|        |           |        | 3ϱ(u−v)2 |     |          |     |     | ϱ−6(u−v)2. |     |     |     |     |
|        |           |        |          | ≤   | 1−ρ(u,v) |     | ≤   |            |     |     |     |     |
8
Proof. By the reflection in Lemma S2.5(a) we may assume u ≤ v. From (S3) and
Q ≥ 3u(1−u),
|       |               |     |           |           | −u)2 |     |           | −u)2 |        |       |     |     |
| ----- | ------------- | --- | --------- | --------- | ---- | --- | --------- | ---- | ------ | ----- | --- | --- |
|       |               |     | 3u(1−u)(v |           |      |     | 3u(v      |      |        |       |     |     |
|       | 1−ρ2          | ≥   |           |           |      | =   |           |      | ≥ 3ϱ(v | −u)2, |     |     |
|       |               |     |           | 4(1−u)3v3 |      |     | 4(1−u)2v3 |      | 4      |       |     |     |
| using | u ≥ ϱ, (1−u)2 |     | ≤ 1 and   | v ≤ 1.    | From | Q ≤ | 4,        |      |        |       |     |     |
−u)2
(v
|     |     |     | 1−ρ2 | ≤   |     |     | ≤ ϱ−6(v | −u)2, |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- |
(1−u)3v3
□
using 1−u ≥ ϱ and v ≥ u ≥ ϱ. The claim follows from 1−ρ ≤ 1−ρ2 ≤ 2(1−ρ).
Corollary S2.2 is Lemma S2.4 in the continuum, with explicit constants, and it is the form
in which the lemma is used: in every application, in Lemma S3.5, in the case k = 1 of
30

Proposition S3.1 and in Lemma S5.1(b), the point θ lies at distance a fixed fraction of
the window from both of its ends, so ϱ may be taken to be a constant depending only on
g. The discrete statement is not deduced from the continuum one, and does not need to
be; it is proved directly in Section S2.6, in full rather than only in the interior regime.
That direct route uses Lemma S2.5(b) and avoids the continuum altogether: since ∥ψ ∥2,
k
| ∥2  |     |     |     |     |     | 1−ρ2 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
∥ψ and the determinant are all explicit, is an explicit function of (a,c,d), and
l
the two-sided bound is an elementary inequality on P, of the same kind as the one proved
| for the norm | in    | Lemma | S2.2.          |     |       |     |     |     |     |     |     |     |
| ------------ | ----- | ----- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| S2.6         | Proof | of    | the separation |     | lemma |     |     |     |     |     |     |     |
Lemma S2.4 follows from Lemma S2.5(b) once the polynomial P is compared with a
product of simple factors. That comparison is the content of the next lemma.
Lemma S2.6 (Polynomial comparison) For integers a,d ≥ 2 and c ≥ 1, with Q :=
d
| 3ad+4ac+4dc+4c2 |     |     | −3a−4c, |        |            |     |          |     |     |     |     |     |
| --------------- | --- | --- | ------- | ------ | ---------- | --- | -------- | --- | --- | --- | --- | --- |
|                 |     |     |         | 9 adcQ | ≤ P(a,d,c) |     | ≤ 9 adcQ | .   |     |     |     |     |
|                 |     |     |         | d      |            |     |          | d   |     |     |     |     |
|                 |     |     | 16      |        |            |     | 7        |     |     |     |     |     |
Proof. Substitute a = A+2, d = D +2, c = C +1 with A,D,C ≥ 0 and expand. Both
differences become polynomials in (A,D,C) with 29 terms and every coefficient strictly
| positive,  | so both | are | non-negative | on       | A,D,C    | ≥ 0. | Explicitly, |     |        |     |         |     |
| ---------- | ------- | --- | ------------ | -------- | -------- | ---- | ----------- | --- | ------ | --- | ------- | --- |
|            |         |     | 28ADC3       | +28AD2C2 | +28A2DC2 |      | +21A2D2C    |     | +24DC3 |     | +24D2C2 |     |
| 16P −9adcQ |         | =   |              |          |          |      |             |     |        |     |         |     |
d
|     |     |     | +24AC3  | +216ADC2 |         | +92AD2C | +24A2C2 |     | +119A2DC |         | +21A2D2 |     |
| --- | --- | --- | ------- | -------- | ------- | ------- | ------- | --- | -------- | ------- | ------- | --- |
|     |     |     | +192DC2 | +84D2C   | +192AC2 |         |         |     | +96AD2   | +138A2C |         |     |
+584ADC
|     |     |     | +123A2D+144C2 |     | +612DC |     | +108D2 | +720AC |     | +588AD |     |     |
| --- | --- | --- | ------------- | --- | ------ | --- | ------ | ------ | --- | ------ | --- | --- |
+162A2
|              |             |     |       | +792C   | +684D+792A+936, |     |         |        |     |         |     |     |
| ------------ | ----------- | --- | ----- | ------- | --------------- | --- | ------- | ------ | --- | ------- | --- | --- |
| the smallest | coefficient |     | being | 21, and |                 |     |         |        |     |         |     |     |
| 9adcQ        | −7P         | =   | 8ADC3 | +8AD2C2 | +8A2DC2         |     | +6A2D2C | +30DC3 |     | +30D2C2 |     |     |
d
|              |             |     | +30AC3     | +108ADC2     |               | +61AD2C | +30A2C2 |         | +34A2DC |        | +6A2D2 |     |
| ------------ | ----------- | --- | ---------- | ------------ | ------------- | ------- | ------- | ------- | ------- | ------ | ------ | --- |
|              |             |     | +81C3      | +240DC2      | +105D2C       |         | +240AC2 | +271ADC |         | +39AD2 |        |     |
|              |             |     | +51A2C     | +12A2D+423C2 |               |         |         | +54D2   |         |        |        |     |
|              |             |     |            |              |               | +441DC  |         |         | +333AC  |        |        |     |
|              |             |     | +87AD+504C |              | +126D+18A+36, |         |         |         |         |        |        |     |
| the smallest | coefficient |     | being      | 6.           |               |         |         |         |         |        |        | □   |
31

Proof of Lemma S2.4. Suppose first that the candidate lies to the right of θ, and put
|     | a = | θ−s, | c   | = b−θ | ≥ 1, |     | d = e+1−b, |     | r = d+c | =   | e+1−θ, |     |
| --- | --- | ---- | --- | ----- | ---- | --- | ---------- | --- | ------- | --- | ------ | --- |
so that m = a+r−1, a,d ≥ 2 because θ and b lie in B , and x = min(a,r) is the distance
s,e
from θ to the nearer end of W. Write L(p,q) := 2pq − p − q + 2, so that Lemma S2.2
reads ∥ψ ∥2 = ar(a−1)(r −1)L(a,r)/{6(m−1)m(m+1)} and similarly for ∥ψ ∥2 with
|     | θ   |     |     |     |     |     |     |     |     |     |     | b   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(a+c,d) in place of (a,r). Dividing the determinant of Lemma S2.5(b) by the product
of the two norms cancels the common factors a, d, a−1, d−1 and the common powers
| of m. | The factors |     | that | remain | give | exactly |                  |     |     |     |     |     |
| ----- | ----------- | --- | ---- | ------ | ---- | ------- | ---------------- | --- | --- | --- | --- | --- |
|       |             |     |      |        |      |         | c(m2 −1)P(a,d,c) |     |     |     |     |     |
1−ρ(θ,b)2
|     |     |     |     | =   |     |     |     |     |     |     | .   | (S4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
(a+c)(a+c−1)r(r−1)L(a,r)L(d,a+c)
We bound each factor. For p,q ≥ 2 one has pq ≤ L(p,q) ≤ 2pq, since L−pq = (p−1)(q−
1)+1 > 0 and 2pq −L = p+q −2 ≥ 0. Next, substituting d = r−c,
|     |     |     |     | Q   | = a{3(r−1)+c}+4c(r−1), |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
d
sothat, usingc ≤ r andr ≥ 3, Q ≤ a(3r+c)+4cr ≤ 4r(a+c)andQ ≥ (r−1)(3a+4c) ≥
|     |     |     |     |     | d   |     |     |     |     | d   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2r·3(a+c) = 2r(a+c). Finally m2 −1 ≥ 1m2, a+c−1 ≥ 1(a+c) and r−1 ≥ 2r for
| 3   |     |     |     |     |     |     | 2   |     | 2   |     |     | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m ≥ 2, a+c ≥ 2, r ≥ 3. Inserting these and Lemma S2.6 into (S4), and writing
c(a+r)
|     |     |     |     |     |     | E := | ,   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
(a+c)r
| simple     | algebra | gives   | 27  | E2 ≤   | 1−ρ2   | ≤ 144E2. |                     |     |     |     |     |     |
| ---------- | ------- | ------- | --- | ------ | ------ | -------- | ------------------- | --- | --- | --- | --- | --- |
|            |         |         | 256 |        |        | 7        |                     |     |     |     |     |     |
| It remains | to      | compare |     | E with | c/x.   | Since    | a+c ≥ a,            |     |     |     |     |     |
|            |         |         |     |        | c(a+r) |          | (cid:16)1 1(cid:17) |     | 2c  |     |     |     |
|            |         |         |     | E      | ≤      |          | = c +               | ≤   | .   |     |     |     |
|            |         |         |     |        |        | ar       | r a                 |     | x   |     |     |     |
For the lower bound there are two cases. If x = a, so a ≤ r, then E ≥ cr/{(a+c)r} =
|     |     |     |     |     |     | 1(c/x) |     |     |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
c/(a + c), which is at least c/(2a) = when c ≤ a and at least when c > a. If
|     |     |     |     |     |     | 2   |     |     |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1(c/x),
x = r, so r ≤ a and c ≤ r, then a+c ≤ 2a and E ≥ ca/{(a+c)r} ≥ c/(2r) =
2
1
| while | c/x ≤ | 1. In | both | cases | E ≥ | min{c/x, | 1}. |     |     |     |     |     |
| ----- | ----- | ----- | ---- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- |
2
| Since | 1(1−ρ2) | ≤   | 1−ρ | ≤ 1−ρ2, | we  | conclude |     |     |     |     |     |     |
| ----- | ------- | --- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
2
|     |     |     | 27   |     | (cid:110)(cid:16)c(cid:17)2 | (cid:111) |            |     | 576(cid:16)c(cid:17)2 |     |     |     |
| --- | --- | --- | ---- | --- | --------------------------- | --------- | ---------- | --- | --------------------- | --- | --- | --- |
|     |     |     |      | min |                             | ,1        | ≤ 1−ρ(θ,b) | ≤   |                       | ,   |     |     |
|     |     |     | 2048 |     | x                           |           |            |     | 7                     | x   |     |     |
The constants differ from 27/256 and 144/7 above because the lower bound uses both
|     | 1   |     |     |     | 1(1−ρ2), |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
E ≥ min{c/x,1} and 1−ρ ≥ whereas the upper bound uses E ≤ 2c/x. These
|     | 2   |     |     |     | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
32

factors give 27/(256 · 4 · 2) = 27/2048 and 4(144/7) = 576/7, respectively. This proves
the assertion with c = 27/2048 and C = 576/7. A candidate to the left of θ is handled
|     |     |     | 0   |     |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by the reflection t (cid:55)→ m+1−t, under which ψ (cid:55)→ ±ψ and x is unchanged. □
|     |     |     |     |     |     |     |     | k   | m+1−k |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
The constants are not sharp. Let m range over 4 ≤ m ≤ 150 together with 200, 300, 400
and 600, and let θ and b range over all admissible values. Then the two ratios
|     |     |     |     |     | 1−ρ |     |     |     | 1−ρ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and
|     |     |     |     | min{(c/x)2, |     |     | 1}  |     | (c/x)2 |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | ------ | --- | --- | --- |
had minimum 0.12798 and maximum 2.19664 respectively, against the proved bounds
27/2048 = 0.01318 and 576/7 = 82.29. The maximum is attained at m = 5, θ = 3, b = 2.
√
In that instance ∥ψ ∥2 = 7/10, ∥ψ ∥2 = 2/5 and ⟨ψ ,ψ ⟩ = 2/5, so ρ = 2/ 7 and the
|       |           |             | √ 3 |                    |     | 2     |     |          | 2 3    |             |     |     |
| ----- | --------- | ----------- | --- | ------------------ | --- | ----- | --- | -------- | ------ | ----------- | --- | --- |
| ratio | is 9(1−2/ |             | 7). |                    |     |       |     |          |        |             |     |     |
| S2.7  | Proof     |             | of  | the discretization |     |       |     | estimate |        |             |     |     |
| Work  | in local  | coordinates |     | 1,...,m            |     | and   | put |          |        |             |     |     |
|       |           |             | 1   |                    | k   |       | r   |          |        |             |     |     |
|       |           | h           | =   | , u                | =   | ,     | v = | ,        | w(v) = | min(v,1−v), |     |     |
|       |           |             | m   |                    | m   |       | m   |          |        |             |     |     |
|       |           |             |     |                    |     | ⟨ψ ,ψ | ⟩   |          | ∥ψ     | ∥2          |     |     |
|       |           |             |     |                    |     | k     | r   |          |        | r           |     |     |
|       |           |             |     | G (u,v)            | =   |       | ,   | N        | (v) =  | ,           |     |     |
|       |           |             |     | m                  |     | m3    |     |          | m      | m3          |     |     |
and let G(u,v) = ⟨Ψ ,Ψ ⟩ and N(v) = v3(1−v)3/3 be the continuum counterparts. Two
|     |     |     | u   | v   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
facts about G are used: for u ≤ v the closed form of Lemma S3.1 simplifies to
|     |     |     |     |        |     | u2(1−v)2(2uv |     |     | +u−3v) |     |     |      |
| --- | --- | --- | --- | ------ | --- | ------------ | --- | --- | ------ | --- | --- | ---- |
|     |     |     |     | G(u,v) | =   | −            |     |     |        | ,   |     | (S5) |
6
with the reflected expression for u ≥ v; and consequently, if u ∈ [γ,1−γ], then |G(u,v)| ≤
C w(v)2.
γ
Lemma S2.7 (Weighted discretization) Fix γ ∈ (0,1/2]. There are constants C and
| C such | that, | for | m ≥ | 4 and | admissible |     | k,r with | u   | ∈ [γ,1−γ], |     |     |     |
| ------ | ----- | --- | --- | ----- | ---------- | --- | -------- | --- | ---------- | --- | --- | --- |
γ
|     |              |     |     | Cm−1w(v)2, |                   |     |                |          |               |     | m−1w(v), |     |
| --- | ------------ | --- | --- | ---------- | ----------------- | --- | -------------- | -------- | ------------- | --- | -------- | --- |
| (a) | |N (v)−N(v)| |     |     | ≤          |                   |     | (b)            | |G       | (u,v)−G(u,v)| | ≤   | C        |     |
|     | m            |     |     |            |                   |     |                | m        |               |     | γ        |     |
|     |              |     |     |            | (cid:12)          |     |                | (cid:12) |               |     |          |     |
|     |              |     |     |            | (cid:12)G (u,v)   |     | G(u,v)(cid:12) |          | C             |     |          |     |
|     |              |     |     | (c)        | m                 | −   |                |          | ≤ γ           | .   |          |     |
|     |              |     |     |            | (cid:12)(cid:112) |     | (cid:112)      | (cid:12) | (cid:112)     |     |          |     |
|     |              |     |     |            | (cid:12) N        | (v) | N(v)(cid:12)   |          | m w(v)        |     |          |     |
m
33

Proof. (a) Both sides are explicit. Substituting a = vm and b = m(1 − v) + 1 in
| Lemma | S2.2 | and     | subtracting |     | N(v)     | gives, | after | factoring, |           |        |            |     |     |
| ----- | ---- | ------- | ----------- | --- | -------- | ------ | ----- | ---------- | --------- | ------ | ---------- | --- | --- |
|       |      |         |             |     |          |        | hv(v  | −1)        |           |        |            |     |     |
|       |      |         |             | N   | (v)−N(v) |        | =     |            | R         | (h,v), |            |     |     |
|       |      |         |             |     | m        |        |       |            | N         |        |            |     |     |
|       |      |         |             |     |          |        | 6(h2  | −1)        |           |        |            |     |     |
|       |      |         |             | −h3 | +h(2v4   | −4v3   | +7v2  |            |           |        |            |     |     |
|       |      | R (h,v) | =           |     |          |        |       | −5v        | +1)−3v(2v |        | −1)(v −1), |     |     |
N
from which, since the coefficients of the terms involving h have moduli summing to 20
and the remaining part is 3v(1−v)(2v −1), |R | ≤ 20h+3v(1−v) ≤ 20{h+v(1−v)}
N
1
for 0 < h ≤ and 0 ≤ v ≤ 1; the smallest admissible constant is 2.79. Since admissibility
2
gives x ≥ 2 and hence w(v) ≥ h, and v(1 − v) ≤ 2w(v). More precisely, the absolute
b
value of the factor hv(v−1)/{6(h2−1)} in the preceding factorization is at most Chw(v).
Also |R (h,v)| ≤ Cw(v) because h ≤ w(v). Their product is therefore at most Chw(v)2,
N
| as required |     | in (a). |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(b) The same computation with ⟨ψ ,ψ ⟩, whose exact form is that used in the proof of
|       |          |           |          |                |         | k     | r     |          |       |          |      |     |     |
| ----- | -------- | --------- | -------- | -------------- | ------- | ----- | ----- | -------- | ----- | -------- | ---- | --- | --- |
| Lemma | S2.5(b), |           | in place | of             | the     | norm. | For u | ≤ v it   | gives |          |      |     |     |
|       |          |           |          |                |         |       |       | hu(v     | −1)   |          |      |     |     |
|       |          |           |          | G (u,v)−G(u,v) |         |       | =     |          | R     | (h,u,v), |      |     |     |
|       |          |           |          | m              |         |       |       |          |       | ≤        |      |     |     |
|       |          |           |          |                |         |       |       | 6(h2 −1) |       |          |      |     |     |
|       |          |           |          | −h3            | +2hu2v2 |       | −hu2v | −3huv2   |       | +hv2     |      |     |     |
|       |          | R (h,u,v) |          | =              |         |       |       |          | +6huv |          | −5hv | +h  |     |
≤
|     |     |     |     | −3u2v | −3uv2 |     | +6uv | +3v2 | −3v, |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | ---- | ---- | ---- | --- | --- | --- | --- |
and for u ≥ v the same with u and v interchanged, that is with hv(u − 1)/{6(h2 − 1)}
1,
in front and R (h,u,v) = R (h,v,u). Both remainders are bounded on 0 < h ≤
|     |     | ≥   |     |     | ≤   |     |     |     |     |     |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 ≤ u,v ≤ 1 by the sum of the moduli of their coefficients, which is 38 in each case. For
h2)}.
u ≤ v, the absolute value of the factor preceding R is hu(1 − v)/{6(1 − It is at
≤
most Chv when v ≤ 1/2, because u ≤ v, and at most Ch(1−v) when v ≥ 1/2. Hence
it is at most Chw(v). For u ≥ v, the factor is hv(1−u)/{6(1−h2)}; it is at most Chv
when v ≤ 1/2 and at most Ch(1−v) when v ≥ 1/2, because then 1−u ≤ 1−v. Thus
| this | factor | is also | at most |     | Chw(v), | which | proves | (b). |     |     |     |     |     |
| ---- | ------ | ------- | ------- | --- | ------- | ----- | ------ | ---- | --- | --- | --- | --- | --- |
(c) By Lemma S2.2, N (v) ≍ w(v)3 and N(v) ≍ w(v)3. Writing the difference as
m
|     |     |     |     | G   | −G  |     |     | N −N    |     |         |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- |
|     |     |     |     |     | √m  |     |     |         | m   |         |     |     |     |
|     |     |     |     |     |     | +   | G √ | √       |     | √ ,     |     |     |     |
|     |     |     |     |     |     |     |     | (cid:0) |     | (cid:1) |     |     |     |
|     |     |     |     |     | N   |     | N   | N       | N + | N       |     |     |     |
|     |     |     |     |     | m   |     | m   |         | m   |         |     |     |     |
the first term is at most C m−1w·w−3/2 by (b), and the second at most C w2·Cm−1w2·
|     |     |     |     |     | γ   |     |     |     |     |     | γ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w−3 ·w−3/2 by (a) and the bound on |G|; both are C m−1w−1/2. □
γ
(cid:80)
Proof of (S12). By Lemma S2.1(a), D (b) = ∆ ⟨ψ ,ψ ˆ ⟩ with ∆ = d /n,
|     |     |     |     |     |     |     | V   |     |     | j   | τj b | j   | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
j∈V
|     |     | ˆ   |     |     |     | (cid:112) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
and ⟨ψ ,ψ ⟩ = m3/2G (u ,v)/ N (v) with u = (τ − s)/m and v = (b − s)/m;
|     | τj  | b   |     | m   | j   |     | m   | j   |     | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
34

and we first compare with the continuum expression formed from the same coordinates,
| (cid:80) |     |     |     | (cid:112) |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
(d /n)m3/2G(u ,v)/ N(v), which by the scaling relation of Lemma S3.1 is n1/2 times
|     | j j |     | j   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the profile on (α ,β ) with kinks at u . The replacement of u by the coordinate deter-
|     |     |     | n n |     | j   |     |     |     | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mined by q is a separate step, taken at the end. Each j ∈ V has u at a fixed fractional
|     |     | j   |     |     |     |     |     |     |     | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distance from both ends, by Lemma S3.3, so Lemma S2.7(c) applies with a γ depending
| only | on g,     | and       |     |          |                   |      |      |           |     |     |            |     |
| ---- | --------- | --------- | --- | -------- | ----------------- | ---- | ---- | --------- | --- | --- | ---------- | --- |
|      | (cid:12)  |           |     |          | (cid:12) (cid:88) | |d | |      | C         |     | m   |            |     |
|      | (cid:12)D | (b)−n1/2D | ¯   | [V](b/n) | ≤                 | j    | m3/2 | γ         | ≤   | C x | (s,e)−1/2, |     |
|      |           | V         |     | αnβn     | (cid:12)          |      |      | (cid:112) |     |     | b          |     |
|      |           |           |     |          |                   | n    | m    | w (v)     |     | n   |            |     |
j∈V
using mw(v) ≤ x (s,e) ≤ 2mw(v). The displacement of τ from nq , which is at most
|     |     |     | b   |     |     |     |     |     | j   | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112)
one, moves u by O(m−1) and, since ∂ {G(u,v)/ N(v)} is bounded uniformly for u at
|     |     | j   |     |     | u   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112)
a fixed distance from the ends, contributes a further O(m−1) to G(u ,v)/ N(v). This is
j
bounded by the right-hand side C m−1w(v)−1/2 of Lemma S2.7(c), because 0 < w(v) ≤ 1.
γ
□
| S3  | Proof |     | of  | Theorem | 4.1 |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
The proof shows that the sample recursion follows the population recursion of Defini-
tion 4.1: every window LABS visits has endpoints within O(r¯ ) of n times the endpoints
n
of a node of T (g), and returns the kinks live at that node. A kink is called live at (α,β)
when its rescaled location lies strictly inside the window, that is, when j ∈ V(α,β). Sec-
tion S3.1 develops the population objects and proves Proposition 4.1; Section S3.2 fixes
the constants; Section S3.3 proves the corresponding statement for the sample recursion;
| and  | Section | S3.4       | deduces | Theorem  | 4.1. |       |     |             |     |     |     |     |
| ---- | ------- | ---------- | ------- | -------- | ---- | ----- | --- | ----------- | --- | --- | --- | --- |
| S3.1 |         | Population |         | objects, | and  | proof | of  | Proposition |     |     | 4.1 |     |
For 0 ≤ α < β ≤ 1 let Π⊥ project L2(α,β) onto the orthogonal complement of span{1,u}
αβ
| and | put | Ψαβ := | Π⊥ [(u−v) | ].  |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+
|     |     | v   | αβ  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma S3.1 (Closed form) On [0,1], for p ≤ v, with a = 1−p and b = 1−v,
|     |     |      | ab2 | b3      | a2b3 | a3b2 | a3b3 |     |     | v3(1−v)3 |     |     |
| --- | --- | ---- | --- | ------- | ---- | ---- | ---- | --- | --- | -------- | --- | --- |
|     | ⟨Ψ  | ,Ψ ⟩ | =   | − −a2b2 | +    | +    | −    | ,   | ∥Ψ  | ∥2 =     |     | .   |
|     |     | p v  |     |         |      |      |      |     | v   |          |     |     |
|     |     |      | 2   | 6       | 2    | 2    |      | 3   |     |          | 3   |     |
For a general interval, ⟨Ψαβ,Ψαβ⟩ = (β − α)3⟨Ψ ,Ψ ⟩ with p′ = (p − α)/(β − α) and
|     |     |     |     |     |     |     | p′  | v′  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p v
| v′  | = (v −α)/(β |     | −α). |     |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
35

√
Proof. With the orthonormal basis {1, 12(u − 1)} of span{1,u} and h = (u − p) ,
|     |     |     |     | √   |     |     | √   |     |     |     | p   |     | +   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
one has ⟨h ,1⟩ = a2/2, 12⟨h ,u − 1⟩ = 12(a2/4 − a3/6) and, for p ≤ v, ⟨h ,h ⟩ =
|     | p   |     |     |     | p   |     |     |     |     |     |     | p   | v   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
ab2/2−b3/6. Subtracting the two projection terms and expanding gives the first formula;
setting p = v gives ∥Ψ ∥2 = a3(1−a)3/3 with a = 1−v, which is the second. The scaling
v
| relation | is the | change | of  | variables | u (cid:55)→ | α+(β | −α)u. |     |     |     |     |     | □   |
| -------- | ------ | ------ | --- | --------- | ----------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
|          |        |        |     | ¯         |             |      |       |     |     |     |     | ¯   |     |
ByLemmaS3.1theprofileD ofSection4.2ofthemainpaperiswelldefined,|D (v)| →
|     |     |     |     | αβ  |     |     |     |     |     |     |     | αβ  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 as v ↓ α or v ↑ β, so its maximum is attained in the interior, and
|     |     | Λ(α,β) |     | := max|D | ¯ (v)| | >   | 0   | whenever | V(α,β) |     | ̸= ∅, |     |     |
| --- | --- | ------ | --- | -------- | ------ | --- | --- | -------- | ------ | --- | ----- | --- | --- |
αβ
v
(cid:80)
since F := d Ψ ̸= 0 by linear independence of the Ψ , and F lies in the closed
|     |     | j∈V | j qj |     |     |     |     |     |     | q   |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
span of {Ψ }, so cannot be orthogonal to every Ψ . If V(α,β) = {j} then c(α,β) = q
|          | v      |           |     |      |          |     |          | v   |     |     |     |     | j   |
| -------- | ------ | --------- | --- | ---- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
| exactly, | by the | continuum |     | form | of Lemma |     | S2.1(c). |     |     |     |     |     |     |
Proof of Proposition 4.1. Induction on the height of the subtree rooted at (α,β). This
heightisfinitebythehypothesisofProposition4.1thatT (g)isfinite. WriteV := V(α,β)
| and k := | |V|. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
If k = 0 the call returns ∅. If k = 1, say V = {j}, then c = q exactly. The live-kink sets
j
of the children (α,q ) and (q ,β) are empty: q is an endpoint and is therefore excluded
|     |     |     | j   | j   |     |     | j   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by the strict inequalities in the definition of V, and no other kink lies in (α,β). Thus
| L = R | = ∅ and | the | call | returns | {q }. |     |     |     |     |     |     |     |     |
| ----- | ------- | --- | ---- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
j
| Let k ≥ | 2.  |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Case A: c ∈/ {q ,...,q }. Then V(α,c) =: V and V(c,β) =: V partition V, and by the
|     |     | 1   | N   |     |     |     | L   |     |     | R   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
induction hypothesis L = {q : j ∈ V }, R = {q : j ∈ V }, with |V | + |V | = k ≥ 2,
|     |     |     |     | j   |     | L   |     | j   | R   |     | L R |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
so the look-ahead branch is entered. If both are non-empty, α′ and β′ are consecutive
elements of {q : j ∈ V}; since V contains all kinks of (α,β) they are consecutive kinks
j
of g, so V(α′,β′) = ∅. The population re-test in Definition 4.1 therefore finds no kink in
its open interval and omits the parent candidate; the call returns L∪R. If L = ∅ then
α′ = α and β′ = min{q : j ∈ V}, so again V(α′,β′) = ∅ and the call returns R. The case
j
| R = ∅ | is symmetric. |     | In  | all three | the value |     | is {q | : j ∈ V}. |     |     |     |     |     |
| ----- | ------------- | --- | --- | --------- | --------- | --- | ----- | --------- | --- | --- | --- | --- | --- |
j
j∗
Case B: c = q . Necessarily ∈ V. The live-kink sets, meaning the indices of kinks
j∗
strictly inside the two child windows, are V = {j ∈ V : q < q j∗ } and V = {j ∈ V :
|     |     |     |     |     |     |     | L   |     | j   |     | R   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
q > q }, which exclude j∗, so |V | + |V | = k − 1 ≥ 1 and the look-ahead branch is
| j j∗ |     |     |     |     | L   | R   |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
entered. More precisely, α′ is the largest element of {q : j ∈ V, q < q }, or α if this set
|     |     |     |     |     |     |     |     | j   |     | j   | j∗  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is empty. Similarly, β′ is the smallest element of {q : j ∈ V, q > q }, or β if this set is
|     |     |     |     |     |     |     |     | j   |     | j   | j∗  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
empty. Thus way q is the unique kink in (α′,β′), so V(α′,β′) = {j∗} and, by the k = 1
j∗
computation, c(α′,β′) = q . The call returns L∪{q }∪R = {q : j ∈ V}. □
|     |     |     |     | j∗  |     |     |     | j∗  |     | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Case A is the trap configuration and Case B the configuration in which the split lands
on a kink. Proposition 4.1 shows that the look-ahead step handles both under its stated
36

well-posedness conditions: the population recursion tree is finite and c(α,β) is defined at
every node.
| S3.2 | Signal-dependent |     |     |     | constants |     | for | the | recursion |     | proof |     |     |
| ---- | ---------------- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- | ----- | --- | --- |
Assume Assumption 4.1 and Assumption 4.2, and assume throughout this subsection
that N ≥ 1; when N = 0 the extrema below are over empty sets, and that case is treated
separately in the proofs of the theorems. Since T (g) is finite, each of the following is a
minimum of a finite set of strictly positive numbers, hence strictly positive:
(cid:16)
|     |        |     | (cid:8) |       |      |         |     |      |            | (cid:9) |     |     |     |
| --- | ------ | --- | ------- | ----- | ---- | ------- | --- | ---- | ---------- | ------- | --- | --- | --- |
| κ   | := min | {δ  | }∪      | q −α, | β −q | : (α,β) | ∈ T | (g), | j ∈ V(α,β) |         |     |     |     |
|     |        | min |         | j     |      | j       |     |      |            |         |     |     |     |
(cid:17)
|     |               |     | (cid:8)     |     |               |     |        |        |               |     | (cid:9) |            |      |
| --- | ------------- | --- | ----------- | --- | ------------- | --- | ------ | ------ | ------------- | --- | ------- | ---------- | ---- |
|     |               |     | ∪ |c(α,β)−q |     | | : (α,β)     | ∈   | T (g), | 1 ≤    | l ≤ N, c(α,β) |     | ̸= q    | ,          | (S6) |
|     |               |     |             |     | l             |     |        |        |               |     | l       |            |      |
|     |               |     |             |     |               |     |        |        | min{c(α,β)−α, |     |         | β −c(α,β)} |      |
| Λ   | := minΛ(α,β), |     |             | Λ   | := maxΛ(α,β), |     | ϱ      | := min |               |     |         |            | ,    |
| min |               |     |             | max |               |     | 0      |        |               |     | β −α    |            |      |
|     | (α,β)         |     |             |     | (α,β)         |     |        | (α,β)  |               |     |         |            |      |
(S7)
the three extrema defining Λ , Λ and ϱ being over nodes with V(α,β) ̸= ∅. We also
|     |     |     |     |     | min max |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
require a lower bound for the noiseless contrast on every window whose sample contrast
must exceed the threshold. These are the proposal windows at non-empty nodes and the
| one-kink | re-test | windows   |         | in  | Case B: |     |     |     |                 |     |         |           |     |
| -------- | ------- | --------- | ------- | --- | ------- | --- | --- | --- | --------------- | --- | ------- | --------- | --- |
|          |         | (cid:104) |         |     |         |     |     |     |                 |     |         | (cid:105) |     |
|          |         |           | (cid:8) |     |         |     |     |     | (cid:9) (cid:8) |     | (cid:9) |           |     |
Λ := min Λ(α,β) : (α,β) ∈ T (g), V(α,β) ̸= ∅ ∪ |d |∥Ψα′β′∥ > 0, (S8)
| det |     |     |     |     |     |     |     |     | j∗  | q   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j∗
the second set running over the Case B re-test windows (α′,β′) of the proof of Proposi-
tion 4.1. On each such window, V(α′,β′) = {j∗}, so q is the only kink strictly inside
j∗
the window. Both sets are finite, so Λ > 0. Note Λ ≤ Λ , and the inequality can
|     |     |     |     |     |     | det |     |     | det min |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
be strict; see Remark S3.2. For LABS-Grid the corresponding constant is
|     |     | (cid:104) | (cid:8) |     |     |     |     |     | (cid:9) | (cid:8) |     | (cid:9) (cid:105) |     |
| --- | --- | --------- | ------- | --- | --- | --- | --- | --- | ------- | ------- | --- | ----------------- | --- |
ΛM,R := min Λ (α,β) : (α,β) ∈ T (g), V(α,β) ̸= ∅ ∪ |d |∥Ψα′β′∥ , (S9)
|     |     |     | M   |     |     | M,R |     |     |     | j∗  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| det |     |     |     |     |     |     |     |     |     |     | q   | j∗  |     |
thefirstsetnowformedfromthepooledamplitudesoverthegridtreeandthesecondfrom
the Case B re-tests of the R-grid. The two trees and the two families of re-test windows
ΛM,R
differ, so is not obtained from Λ by adjoining terms. No additional separation
|     |     | det |     |     |     | det |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assumption is required in (S6): its third set is finite because T (g) is finite, and each of
| its elements |     | is positive |     | by construction. |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma S3.2 (Consequences of Assumption 4.2) Fix a node (α,β). Suppose its
| live-kink | set | is non-empty, |     | so  | Assumption | 4.2       | applies, |       | and put |     |     |     |     |
| --------- | --- | ------------- | --- | --- | ---------- | --------- | -------- | ----- | ------- | --- | --- | --- | --- |
|           |     |               |     |     | V          | := V(α,β) |          | ̸= ∅. |         |     |     |     |     |
37

For a nearby window (α′,β′), write
(cid:42) (cid:43)
(cid:88)
Ψα′β′
D ¯ [V](v) := d Ψα′β′, v .
α′β′ j qj ∥Ψα′β′
∥
j∈V v
Thus this profile is formed from the fixed kinks q , j ∈ V, with their slope jumps d ; no
j j
kink is added or removed when the endpoints are perturbed. There are constants κ > 0,
ς > 0 and C < ∞, depending only on g, such that:
0 L
(a) Λ(α,β)−|D ¯ (v)| ≥ κ(v −c(α,β))2 for all v ∈ (α,β);
αβ
(b) for |α′ − α| + |β′ − β| < ς , the profile D ¯ [V] has a unique maximizer c′ of its
0 α′β′
modulus, with |c′ −c(α,β)| ≤ C (|α′ −α|+|β′ −β|), max |D ¯ [V]| ≥ 1Λ(α,β),
L v α′β′ 2
max (cid:12) (cid:12)D ¯ α′β′ [V] (cid:12) (cid:12)− (cid:12) (cid:12)D ¯ α′β′ [V](v) (cid:12) (cid:12) ≥ 2 1κ(v −c′)2 on (α′,β′),
v
and min{c′ −α′,β′ −c′} ≥ 1ϱ (β′ −α′).
2 0
Proof. (a) Write c = c(α,β) and Λ = Λ(α,β). Near c, Taylor expansion and Assump-
tion 4.2 give
Λ−|D ¯ (v)| ≥ 1|∂2|D ¯ |(c)|(v −c)2
αβ 3 v αβ
¯
on some (c − ϵ,c + ϵ). Moreover, |D (v)| → 0 at both endpoints. Consequently the
αβ
¯
function Λ − |D (v)| has a continuous extension to [α,β], obtained by assigning it the
αβ
value Λ at each endpoint. By uniqueness of c, this extension is strictly positive on
K := {v ∈ [α,β] : |v −c| ≥ ϵ}.
ϵ
It therefore has a positive minimum on K . Combining this minimum with the local
ϵ
Taylor bound proves (a) for the fixed node. Finally, take the smallest resulting positive
constant over the finitely many nodes (α,β) ∈ T (g) with V(α,β) ̸= ∅.
(b) Here Cp means that derivatives through order p exist and are continuous. With V
fixed, the map (α′,β′,v) (cid:55)→ D ¯ [V](v) is continuous, is C2 in v, and has a jointly con-
α′β′
tinuous second derivative in v, by Lemma S3.1 and continuity of Π⊥ g in the endpoints.
α′β′
¯
Since |D (c)| = Λ > 0, its sign is constant in a neighbourhood of (α,β,c), so the same
αβ
regularity holds for the absolute profile.
Apply the implicit function theorem to
H(α′,β′,v) := ∂ |D ¯ [V](v)|.
v α′β′
At (α,β,c), H = 0 and ∂ H = ∂2|D ¯ |(c) < 0. The theorem therefore provides neigh-
v v αβ
bourhoods of (α,β) and c, and a unique C1 function (α′,β′) (cid:55)→ c′(α′,β′) in those neigh-
bourhoods such that H(α′,β′,c′) = 0 and c′(α,β) = c. A C1 function on a sufficiently
38

small compact neighbourhood is Lipschitz, which gives the stated bound with a finite
| constant | C   | .   |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L
We now choose ς > 0 small enough that every endpoint pair satisfying |α′−α|+|β′−β| <
0
ς lies in this neighbourhood. If necessary, choosing a smaller positive value of ς ensures,
0 0
by the joint continuity just established, that the second derivative at c′ remains negative,
c′
the maximum value is at least Λ/2, and remains at least half the relative endpoint
| distance | attained |     | by c. | Part | (a) gives |     |      |        |      |
| -------- | -------- | --- | ----- | ---- | --------- | --- | ---- | ------ | ---- |
|          |          |     |       |      | ¯         | κϵ2 |      |        |      |
|          |          |     |       | Λ−|D | (v)|      | ≥   | when | |v −c| | ≥ ϵ. |
αβ
Uniform continuity of the absolute profile on the corresponding compact set of endpoint
and candidate triples preserves at least half this positive difference for all such (α′,β′).
Thus no point outside the local neighbourhood of c′ can maximize the perturbed profile.
Inside that neighbourhood, the uniform negative-curvature bound and Taylor’s theorem
κ
give the quadratic inequality in (b), after reducing the common constant if required.
c′
This also proves that is the unique global maximizer. Taking the smallest admissible ς
0
and the largest C over the finitely many non-empty nodes makes the constants depend
L
| only on | g.  |           |     |           |       |       |          |         | □   |
| ------- | --- | --------- | --- | --------- | ----- | ----- | -------- | ------- | --- |
| S3.3    | The | sample    |     | recursion |       | on    | tracking | windows |     |
| We work | on  | the event |     | E of      | Lemma | S2.3. |          |         |     |
n
Definition S3.1 (Tracking) A window (s,e] tracks a node (α,β) ∈ T (g) at scale C if
⋆
|s − nα| ≤ C r¯ , |e − nβ| ≤ C r¯ , and moreover s = 0 when α = 0 and e = n when
|     |     | ⋆ n |     |     | ⋆ n |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
β = 1. Thus the scale is the fixed constant multiplying the endpoint error r¯ . For example,
n
tracking at scale K means that both endpoint errors are at most Kr¯ , subject to the exact
n
| boundary | conditions |     | just | stated. |     |     |     |     |     |
| -------- | ---------- | --- | ---- | ------- | --- | --- | --- | --- | --- |
Lemma S3.3 (Tracking separates interior and exterior kinks) Fix C . There is
⋆
| n such | that | for n | ≥ n | , if (s,e] | tracks | (α,β) | at scale | C then |     |
| ------ | ---- | ----- | --- | ---------- | ------ | ----- | -------- | ------ | --- |
| 0      |      |       |     | 0          |        |       |          | ⋆      |     |
x (s,e) ≥ 1κn for j ∈ V(α,β), x (s,e) ≤ C r¯ +1 for j ∈/ V(α,β).
|     | j   |     |     |     |     |     | j   | ⋆   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
Hence the kinks in V(α,β) have signal strength, as defined in Section S2, at least
d(κ/2)3/2n1/2.
c
ℓ
Moreover,
(cid:88)
|     |     |     | ϱ   | :=  | ℓ (s,e) | =   | O{n−1/4(logn)3/4} |     | = o(1). |
| --- | --- | --- | --- | --- | ------- | --- | ----------------- | --- | ------- |
j
j∈/V(α,β)
39

Proof. If j ∈ V(α,β) then q −α ≥ κ and β−q ≥ κ by (S6), so τ −s ≥ κn−C r¯ −1 ≥
j j j ⋆ n
1κn for n large, and symmetrically on the right. If j ∈/ V(α,β) and q ∈ {α,β} then
2 j
x ≤ C r¯ + 1. Otherwise q < α or q > β strictly, and in the first case α − q ≥ κ,
j ⋆ n j j j
because α is 0, or one of the q , or a value c(·,·) at an ancestor node. The definition (S6)
l
or the minimum kink spacing δ then gives α−q ≥ κ; hence τ < s and x = 0. The
min j j j
case q > β is symmetric. The signal strength statements are Corollary S2.1. □
j
Lemma S3.4 (No detection) Fix C . There is n such that for n ≥ n , on E : if
⋆ 0 0 n
(s,e] is any window with x (s,e) ≤ C r¯ + 1 for every j, then max C (b) ≤ o(1) +
j ⋆ n b s,e
σ(8logn)1/2 < λ, and the call on (s,e] returns ∅.
Proof. By Lemma S2.1(b) and Corollary S2.1(a),
max (cid:12) (cid:12)⟨f,ψ ˆ ⟩ (cid:12) (cid:12) ≤ (cid:88) ℓ (s,e) = O (cid:8) n−1/4(logn)3/4 (cid:9) → 0.
b j
b
j
Adding Z and recalling that λ = Θσ(8logn)1/2 with Θ > 1 gives the strict inequality
n
for n large, since (Θ−1)σ(8logn)1/2 → ∞. If B = ∅ the call returns ∅ immediately. □
s,e
Lemma S3.5 (Detection and localization) Let (s,e] be a window and put
(cid:88) (cid:88)
ˆ
D (w) := ∆ ⟨ψ ,w⟩, D (b) := D (ψ ), ϱ := ℓ (s,e),
U j τj U U b j
j∈U j∈/U
for vectors w ∈ RW and some U ⊆ {1,...,N}. Suppose there are b∗ ∈ B and constants
s,e
a ,κ′,ϱ > 0 such that
0 1
(i) min(b∗ −s, e−b∗) ≥ ϱ n;
1
(ii) A := |D (b∗)| ≥ a n1/2, and |D (b∗)|−|D (b)| ≥ κ′A{(b−b∗)/n}2 for every b ∈ B
U 0 U U s,e
with |b−b∗| ≥ r , where r ≤ C n1/2;
0 0 r
(iii) ϱ ≤ σ(logn)1/2.
Then there are n and C , depending only on a ,κ′,ϱ ,C ,σ,c ,C , such that for n ≥ n
0 1 0 1 r 0 0 0
on E ,
n
maxC (b) ≥ 1A > λ, | ˆ b−b∗| ≤ C r¯ .
s,e 2 1 n
b
Proof. Define the linear functional
(cid:88)
R(w) := ∆ ⟨ψ ,w⟩.
j τj
j∈/U
40

Then ⟨f,w⟩ = D (w) + R(w), |R(w)| ≤ ϱ∥w∥, and |R(ψ ˆ ) − R(ψ ˆ )| ≤ ϱ∥ψ ˆ − ψ ˆ ∥ by
|     |     |     | U   |     |     |     |     |     |     | b   | b′  | b   | b′  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma S2.1(b). Since A ≥ a n1/2 and ϱ+Z = O{(logn)1/2} we get C(b∗) ≥ A−ϱ−Z ≥
|     |      |           |        |     | 0   |     |     | n   |     |     |     |     | n   |
| --- | ---- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1A  | > λ, | the first | claim. |     |     |     |     |     |     |     |     |     |     |
2
If | ˆ b − b∗| < r the second claim holds, since r ≤ C n1/2 ≤ C r¯ ; assume therefore
|     |     |     | 0   |     |     |     |     | 0   | r   |     | r n |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ˆ b − b∗| ≥ r , so that hypothesis (ii) may be used at b = ˆ b. Put ς∗ = signD (b∗),
|     |     | 0   |     |     |     |     |     |     |     |     |     |     | U   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ˆ   |     |     | ˆ   |     |     |     |     |     | ˆ   |     |     |     |
u∗ = ς∗ψ , and u = ςψ with ς chosen so that ⟨X,u⟩ = C( b) ≥ 0. From ⟨X,u⟩ ≥ ⟨X,u∗⟩
|     |       | b∗    |     | ˆb  |     |              |     |             |     |     |     |     |       |
| --- | ----- | ----- | --- | --- | --- | ------------ | --- | ----------- | --- | --- | --- | --- | ----- |
| and | Lemma | S2.3, |     |     |     |              |     |             |     |     |     |     |       |
|     |       |       |     |     |     | ⟨f,u∗⟩−⟨f,u⟩ |     | ≤ ⟨ε,u−u∗⟩. |     |     |     |     | (S10) |
ˆ
Since D (u∗) = |D (b∗)| by the choice of ς∗, and D (u) ≤ |D ( b)|,
|              | U   |     |     | U        |     |             |     | U    |      | U        |                |     |     |
| ------------ | --- | --- | --- | -------- | --- | ----------- | --- | ---- | ---- | -------- | -------------- | --- | --- |
| ⟨f,u∗⟩−⟨f,u⟩ |     |     |     | (b∗)|−|D |     | ˆ b)|−|R(u∗ |     |      |      | (b∗)|−|D | ˆ b)|−ϱ∥u−u∗∥. |     |     |
|              |     |     | ≥   | |D       |     | (           |     | −u)| | ≥ |D |          | (              |     |     |
|              |     |     |     | U        |     | U           |     |      | U    |          | U              |     |     |
Combining this inequality with (S10) and hypothesis (ii), and writing ∆ := | ˆ b−b∗|, gives
|     |     |     | κ′A(∆/n)2 |     |      |          |     | ˆ                         |     |     |     |     |       |
| --- | --- | --- | --------- | --- | ---- | -------- | --- | ------------------------- | --- | --- | --- | --- | ----- |
|     |     |     |           |     | ≤ |D | (b∗)|−|D |     | ( b)| ≤ ϱ∥u−u∗∥+⟨ε,u−u∗⟩. |     |     |     |     | (S11) |
|     |     |     |           |     |      | U        | U   |                           |     |     |     |     |       |
ς∗.
The noise term is treated differently before and after Step 2 proves that ς = The
ˆ ˆ
increment bound is the second event in the definition of E ; it controls ⟨ε,ψ − ψ b′ ⟩, a
|     |     |     |     |     |     |     |     |     |     | n   |     | b   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
difference of unsigned contrast vectors. If ς = −ς∗, then u−u∗ = ±(ψ ˆ +ψ ˆ ) is instead
|     |     |     |     |     |     |     |     |     |     |     | ˆb  | b∗  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a sum, so the second event does not apply. Before Step 2 excludes this case, we use the
pointwise part of E , namely its first event, separately at ˆ b and b∗:
n
|     |     |     |     | (cid:12)                 |     | (cid:12) | (cid:12)                                     | (cid:12) (cid:12) | (cid:12) |      |     |     |     |
| --- | --- | --- | --- | ------------------------ | --- | -------- | -------------------------------------------- | ----------------- | -------- | ---- | --- | --- | --- |
|     |     |     |     | (cid:12)⟨ε,u−u∗⟩(cid:12) |     | ≤        | (cid:12)⟨ε,u⟩(cid:12)+(cid:12)⟨ε,u∗⟩(cid:12) |                   |          | ≤ 2Z | ,   |     |     |
n
This inequality holds for either relation between the signs. After Step 2 has proved
ς = ς∗, u−u∗ = ±(ψ ˆ −ψ ˆ ), and the second event in E can be used. Lemma S2.4 then
|     |     |     |     | ˆb  | b∗  |     |     |     | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
makes both terms on the right of (S11) proportional to ∆/n, whereas its left-hand side
is proportional to (∆/n)2. For ∆ > 0, one factor ∆/n can then be canceled. The bound
|R(w)| ≤ ϱ∥w∥ holds for every w and does not depend on the relation between the signs.
Step 1 (preliminary bound). Using ∥u − u∗∥ ≤ 2, the pointwise bound just described,
κ′A(∆/n)2
and (iii), ≤ 2ϱ+2Z ≤ 2σ(logn)1/2+2σ(8logn)1/2 ≤ 8σ(logn)1/2, so ∆/n =
n
O{n−1/4(logn)1/4} → 0. The second, increment event in E is not used at this stage.
n
Step 2 (sign of the inner product). ByStep1andLemmaS2.4withx = min(b∗−s,e−b∗) ≥
|     |     |     | ρ(b∗, | ˆ   |     |     | ⟨u,u∗⟩ |     |     |     | u∗∥2 |     |     |
| --- | --- | --- | ----- | --- | --- | --- | ------ | --- | --- | --- | ---- | --- | --- |
ϱ n we get ρ := b) → 1. Suppose = −ρ. Then ∥u + = 2 − 2ρ → 0,
| 1     |     |     |          |     |         | √   |                |     |     |       | √    |         |       |
| ----- | --- | --- | -------- | --- | ------- | --- | -------------- | --- | --- | ----- | ---- | ------- | ----- |
|       | ∥Π⊥ |     | (cid:80) |     | ¯ n1/2/ |     | |⟨f,u⟩+⟨f,u∗⟩| |     |     | Cn1/2 |      |         |       |
| while |     | f∥  | ≤        | ℓ ≤ | Nd      | 2,  | so             |     | ≤   |       | 2−2ρ | = o(A). | Since |
|       |     | W   |          | j j |         |     |                |     |     |       |      |         |       |
ˆ
⟨f,u∗⟩ ≥ A−ϱ ≥ 3A, this forces ⟨f,u⟩ ≤ −1A < 0; but ⟨f,u⟩ ≥ C( b)−Z ≥ 1A−Z > 0,
|     |     |     |     |     |     |     |     |     |     |     | n   |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 4   |     |     |     |     | 2   |     |     |     | 2   |     |
a contradiction. Hence ⟨u,u∗⟩ = ρ > 0. This does not yet give ς = ς∗: a positive signed
correlation could equally arise from opposite multipliers applied to negatively correlated
|     |     |     |     |     |     |     |     |     |     |     | ˆ ˆ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vectors. What excludes that is Lemma S2.5(c), by which ⟨ψ ,ψ ⟩ > 0 for any two
ˆb b∗
ˆ ˆ
admissible candidates; since ⟨u,u∗⟩ = ςς∗⟨ψ ,ψ ⟩, it follows that ς = ς∗. Consequently
ˆb b∗
)1/2ϱ−1∆/n.
| ∥u−u∗∥ |     | = {2(1−ρ)}1/2 |     |     | ≤ (2C |     |     |     |     |     |     |     |     |
| ------ | --- | ------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |     |               |     |     |       | 0   | 1   |     |     |     |     |     |     |
41

Step 3 (conclusion). The signs now agree, so u − u∗ = ±(ψ ˆ − ψ ˆ ) and the increment
ˆb b∗
event in E gives ⟨ε,u−u∗⟩ ≤ σ(10logn)1/2∥u−u∗∥. Substituting this and the bound of
n
| Step  | 2 into | (S11)     | gives |                    |         |                |                |         |         |     |     |
| ----- | ------ | --------- | ----- | ------------------ | ------- | -------------- | -------------- | ------- | ------- | --- | --- |
|       |        |           |       | (cid:16)∆(cid:17)2 |         |                |                |         |         | ∆   |     |
|       |        |           |       |                    | (cid:8) |                |                | (cid:9) |         |     |     |
|       |        |           | κ′A   |                    | ≤       | ϱ+σ(10logn)1/2 |                | (2C     | )1/2ϱ−1 | .   |     |
|       |        |           |       |                    |         |                |                |         | 0 1     |     |     |
|       |        |           |       | n                  |         |                |                |         |         | n   |     |
| For ∆ | > 0,   | canceling | one   | factor             | of      | ∆/n gives      |                |         |         |     |     |
|       |        |           |       | ∆                  | (2C     | )1/2           |                |         |         |     |     |
|       |        |           |       |                    |         | 0 (cid:8)      |                |         | (cid:9) |     |     |
|       |        |           |       |                    | ≤       |                | ϱ+σ(10logn)1/2 |         | ;       |     |     |
κ′A
|     |     |     |     |     | n ϱ |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
the conclusion is immediate when ∆ = 0. By (iii), the quantity in braces is at most
| 5σ(logn)1/2, |     | and | A ≥ | a n1/2. | Therefore | ∆   | ≤ C | r¯ with |     |     |     |
| ------------ | --- | --- | --- | ------- | --------- | --- | --- | ------- | --- | --- | --- |
|              |     |     |     | 0       |           |     |     | 1 n     |     |     |     |
κ′a
|     |     |     |     | C   | = max{C | , 5(2C |     | )1/2σ/(ϱ | )}. |     |     |
| --- | --- | --- | --- | --- | ------- | ------ | --- | -------- | --- | --- | --- |
|     |     |     |     |     | 1       | r      | 0   | 1        | 0   |     |     |
The term C covers the case ∆ < r considered before (S10); the second term covers
|     |     | r   |     |     |     | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
□
∆ ≥ r .
0
Remark S3.1 Within Lemma S3.5, ϱ is fixed once the window (s,e] and the set U are
|     |     |     |     |     |     |     |     |     | ˆ b∗|. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
fixed; it does not depend on the localization error ∆ = | b − Consequently, the final
(cid:80)
bound on ∆ cannot be substituted into the definition ϱ = ℓ (s,e) to obtain a smaller
j∈/U j
value of ϱ. The rate r¯ follows directly because both R(u∗ − u) and the noise increment
n
⟨ε,u−u∗⟩ are bounded by a constant times ∥u−u∗∥, and hence by a constant times ∆/n.
By contrast, the noiseless contrast loss on the left of (S11) is bounded below by a constant
times (∆/n)2.
If |R(u∗) − R(u)| were instead bounded by 2ϱ, without its dependence on u∗ − u, the
resulting calculation would give only ∆ = O{n5/8(logn)3/8}. Corollary S2.1 then shows
that a kink at this distance from the child-window edge created by its own detection has
n−1/16,
signal strength of order apart from logarithmic factors. This does not tend to zero
| quickly | enough | for | the | induction | in  | Proposition |     | S3.1. |     |     |     |
| ------- | ------ | --- | --- | --------- | --- | ----------- | --- | ----- | --- | --- | --- |
Lemma S3.6 (Transfer to the sample window) Let (α,β) be a fixed rescaled win-
dow with β −α ≥ κ and V := V(α,β) ̸= ∅, at which the conclusions of Lemma S3.2 hold
with constants κ,ϱ and maximizer c. Let (s,e] track this window at scale C in the sense
|     |     |     | 0   |     |     |     |     |     |     |     | ⋆   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of Definition S3.1. There is n such that for n ≥ n , hypotheses (i)–(iii) of Lemma S3.5
|     |     |     |     |     | 0   |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hold with
|       | U        | = V, | ϱ =         | ϱ κ/4, | κ′     | = κ/(32Λ  |     | ), a =  | Λ /4, | r   | = C n1/2 |
| ----- | -------- | ---- | ----------- | ------ | ------ | --------- | --- | ------- | ----- | --- | -------- |
|       |          |      | 1           | 0      |        |           | max | 0       | min   | 0   | r        |
| for a | constant | C    | . Moreover, |        | b∗ may | be chosen |     | so that |       |     |          |
r
|     |     |     |     |     | |b∗  |     | (C′ +C′ |       |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------- | ----- | --- | --- | --- |
|     |     |     |     |     | −nc| | ≤   |         | C )r¯ | .   |     |     |
|     |     |     |     |     |      |     | 0       | L ⋆   | n   |     |     |
42

Here C′ does not depend on n or C , although it may depend on the signal and on the
|     | 0   |     |     |     |     | ⋆   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fixed window through the constants of Lemma S3.2. The additive term C′r¯ cannot in
0 n
general be omitted. At the root, C = 0 because (0,n] tracks (0,1) exactly, but b∗ is an
⋆
integer whereas nc need not be an integer. This conclusion applies to every node of T (g)
under Assumption 4.2. It also applies, in Section S4, to every grid sub-window for which
Assumption S4.2 states that the absolute population profile has a unique maximizer with
| a strictly | negative |     | second | derivative |     | there. |     |     |     |     |     |     |
| ---------- | -------- | --- | ------ | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
Proof. Write α = s/n, β = e/n, so |α −α|+|β −β| ≤ 2C r¯ /n → 0. This quantity
|     |     | n   |     | n   |     | n   |     | n   |     | ⋆ n |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is less than ς for all sufficiently large n, so Lemma S3.2(b) applies. By Lemma S2.1(a)
0
restricted to V, together with Lemma S3.1 and Lemma S2.7, proved in Section S2.7,
|     | (cid:12) |     |     |     | (cid:12) |     | m   |     |     |     |     |     |
| --- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
(cid:12)D (b)−n1/2D ¯ [V](b/n)(cid:12) ≤ C x (s,e)−1/2 for every b ∈ B , (S12)
|     | (cid:12) V |     | αnβn |     | (cid:12) |     | b   |     |     |     | s,e |     |
| --- | ---------- | --- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
n
where x (s,e) = min(b−s,e+1−b). Two consequences will be used. The error on the
b
left of (S12) is O(1) uniformly in b. For each fixed η > 0, it also satisfies the sharper
| interior | bound |     |     |          |     |     |     |     |          |     |     |     |
| -------- | ----- | --- | --- | -------- | --- | --- | --- | --- | -------- | --- | --- | --- |
|          |       |     |     | (cid:12) |     |     |     |     | (cid:12) |     |     |     |
¯
|     |     |     | sup | (cid:12)D | (b)−n1/2D |     |      | [V](b/n)(cid:12) | =        | O(n−1/2) |     | (S13) |
| --- | --- | --- | --- | --------- | --------- | --- | ---- | ---------------- | -------- | -------- | --- | ----- |
|     |     |     |     | (cid:12)  | V         |     | αnβn |                  | (cid:12) |          |     |       |
b:x b (s,e)≥ηm
| when | m ≍ | n.  |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The quantities in (S12) are algebraic functions of m and the integer locations: they are
formed from these arguments by finitely many arithmetic operations and square roots.
The square roots arise from the normalization by ∥ψ ∥. Section S2.7 proves the estimate
b
from Lemma S2.7. The error on the left of (S12) accounts for two differences: the dis-
crete Gram entries differ from m3 times the continuum entries G(u,v) and N(v) defined
in Section S2.7, and the integer location τ = ⌊nq ⌋ differs from nq by at most one.
|     |     |     |     |     |     |     | j   | j   |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
There is no additional error from the slope jumps, because the triangular-array regime
of Section 4.1 of the main paper, meaning the sequence of signal models indexed by n,
| prescribes | ∆   | = d | /n exactly. |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|            |     | j   | j           |     |     |     |     |     |     |     |     |     |
For a more general sequence of signal models, the limits τ /n → q and n∆ → d
|     |     |     |     |     |     |     |     |     |     | j   | j   | j j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alone do not imply an o(1) error in (S12). Moving a kink by h changes D by order
V
| hm1/2/n, |     |     |     |     |     |     |     |     | ϵn1/2. |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
and changing n∆ by ϵ changes it by order Thus an o(1) error requires
j
|τ − nq | = o(n1/2) and |n∆ − d | = o(n−1/2). A location error of order r¯ does not
| j   | j   |     |     | j   | j   |     |     |     |     |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
satisfy the first requirement and therefore does not ensure an o(1) discretization error.
The dependence on x in (S12) is necessary: the rate O(n−1/2) does not hold uniformly,
b
and fails at candidates within O(1) of an edge, where the discrete and continuum norms
differ by a constant factor rather than by a relative O(1/m). At b = s + 2, (S1) gives
∥ψ ∥2 = (m−1)(m−2)/{m(m+1)} → 1, whereas m3/2∥Ψ ∥ → 23/23−1/2. The form
| b   |     |     |     |     |     |     |     |     |     | 2/m |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
¯
(S12) is sharp. Let c maximize |D [V]| and b∗ maximize |D | over B . Note that
|     |     |     | n   |     |     | αnβn |     |     |     | V   | s,e |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
43

D ¯ is defined through the unnormalized inner product of L2(α,β), so it already includes
αβ
a factor (β − α)3/2 and the normalization in (S12) is the same for every window; this
is what makes contrasts computed on windows of different lengths directly comparable.
Then (S12) and Lemma S3.2(b) give |D (b∗)| ≥ 1Λ n1/2. Fix η := ϱ /4 and call b
V 4 min 0
interior if it is at distance at least ηm from both ends of the window; on interior b the
error is O(n1/2m−1) = O(n−1/2) by (S13), and on all b it is O(n1/2m−1/2) = O(1) by (S12).
The discrete maximizer is close to nc . Let b be the integer nearest nc , which is
n n n
¯
interior. By (S13) and the quadratic bound of Lemma S3.2(b) for the profile |D [V]|
αnβn
at its maximizer c ,
n
|D (b )| = n1/2max|D ¯ [V](w)|+o(1).
V n
w
αnβn
First, b∗ is interior. A non-interior b lies within η(β − α) of an endpoint, whereas c
n
is at least 1ϱ (β − α) from each endpoint by the final inequality in Lemma S3.2(b).
2 0
Hence |b/n − c | ≥ 1ϱ (β − α). Comparison must be with the perturbed maximum
n 4 0
¯
max |D [V](w)|, not with Λ(α,β): the rescaled endpoints move by O(r¯ /n), so the
w αnβn n
twomaximadifferbyO(r¯ /n). Aftermultiplicationbyn1/2,thisdifferenceisO{(logn)1/2}
n
rather than O(1).
For a non-interior b, the deficit
¯ ¯
max|D [V](w)|−|D [V](b/n)|
w
αnβn αnβn
is bounded below by a fixed constant δ > 0, uniformly for large n. This follows from
0
Lemma S3.2(b), the fixed lower bound on |b/n − c |, and continuity in the endpoints.
n
Equation (S12) therefore gives
|D (b)| ≤ n1/2{max|D ¯ [V](w)|−δ }+O(1),
V
w
αnβn 0
which is smaller than |D (b∗)| for large n. Second, compare b∗ with b . Both are interior,
V n
so the O(n−1/2) approximation error in (S13) applies at both points. Hence
1κn1/2 (cid:0) b∗/n−c (cid:1)2 ≤ |D (b )|−|D (b∗)|+O(n−1/2) ≤ O(n−1/2),
2 n V n V
since b∗ maximizes |D |. It follows that |b∗ −nc | ≤ C n1/2 for a constant C < ∞.
V n b b
Transfer of the profile deficit to b∗. Let r := 2C n1/2 =: C n1/2 and suppose |b−b∗| ≥ r .
0 b r 0
Then |b − nc | ≥ |b − b∗| − C n1/2 ≥ 1|b − b∗|, so (b/n − c )2 ≥ 1{(b − b∗)/n}2. For
n b 2 n 4
interior b, the continuum profile deficit provided by Lemma S3.2(b), after multiplication
by n1/2, is at least 1κn1/2(b/n − c )2. By choosing C large enough, this lower bound
2 n b
exceeds twice the two O(n−1/2) discretization errors from (S13). For non-interior b, the
continuum profile deficit is of order n1/2 and exceeds the O(1) error in (S12). Thus, in
both ranges,
|D (b∗)|−|D (b)| ≥ κ n1/2 (cid:8) (b−b∗)/n (cid:9)2 whenever |b−b∗| ≥ r ,
V V 16 0
44

which is hypothesis (ii) in the form required by Lemma S3.5 with κ′ = κ/(32Λ ).
max
The additional factor two absorbs the {1+o(1)} term in |D (b∗)| ≤ Λ n1/2{1+o(1)}.
|          |     |       |         |          |          |      |     |        | V         | max   |     |     |
| -------- | --- | ----- | ------- | -------- | -------- | ---- | --- | ------ | --------- | ----- | --- | --- |
| Finally, |     | Lemma | S3.2(b) | gives    | |c −c|   | ≤ 2C | C   | r¯ /n, | and hence |       |     |     |
|          |     |       |         |          | n        |      | L ⋆ | n      |           |       |     |     |
|          |     |       |         | |b∗ −nc| | ≤ C n1/2 | +2C  | C   | r¯ ≤   | (C′ +C′ C | )r¯ , |     |     |
|          |     |       |         |          | b        |      | L   | ⋆ n    | 0 L       | ⋆ n   |     |     |
withC′ := C andC′ := 2C . Hereweusedn1/2 ≤ r¯ . Also, |b∗−nc | = O(n1/2) = o(m),
|     | 0   |     | b   | L   | L   |     |     |     | n   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
while Lemma S3.2(b) places c at least 1ϱ (β − α ) from each endpoint. Therefore
|     |     |     |     |     | n   |     | 2 0 | n   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
min(b∗−s,e−b∗) ≥ 1ϱ m ≥ 1ϱ κn for large n, which verifies hypothesis (i). Hypothesis
|     |     |     |     | 4 0 | 4 0 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
□
| (iii) | follows | from | Lemma | S3.3. |     |     |     |     |     |     |     |     |
| ----- | ------- | ---- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition S3.2 (Node tracking constants) For v ∈ T (g), let C be the localization
1,v
constant provided by Lemma S3.5 at v. Let C′ and C′ be the largest of the corresponding
|     |     |     |     |     |     |     | 0   |     | L   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
constants in Lemma S3.6 over the finitely many non-empty nodes. Set K := 0 at the
v
v′
| root | and, | for    | each    | child | of v, set |         |     |     |      |           |     |           |
| ---- | ---- | ------ | ------- | ----- | --------- | ------- | --- | --- | ---- | --------- | --- | --------- |
|      |      |        | (cid:8) |       |           | (cid:9) |     |     |      | (cid:110) |     | (cid:111) |
|      | K    | := max | K       | , C   | +C′ +C′   | K       | ,   | and | C := | max max   | K , | C ,       |
|      | v′   |        |         | v 1,v |           | v       |     |     | ⋆    |           | v   | rt        |
0 L
v∈T(g)
where C is the largest localization constant provided by Lemma S3.5 at the finitely many
rt
Case B re-test windows in the proof of Proposition 4.1. On each such window, U is a
singleton, meaning that U = {j∗} contains only the unique kink strictly inside the re-test
window. The quantities K r¯ are called the node tracking radii because they bound the two
v n
endpoint errors of a sample window associated with node v. Thus K is the dimensionless
v
tracking constant and K r¯ is the corresponding radius. Both maxima are over finite sets,
|     |     |      |            | v n |      |     |     |     |     |     |     |     |
| --- | --- | ---- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| so  | C < | ∞ by | Assumption |     | 4.1. |     |     |     |     |     |     |     |
⋆
The re-test constant is included separately because a Case B re-test window is generally not
a node of T (g), so its localization constant is not among the C . Also K ≤ C for every
|     |     |     |     |     |     |     |     |     | 1,v |     | v ⋆ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
v, and C does not depend on a tracking constant K. Indeed, Lemma S3.6 shows that
1,v
the parameters a ,κ′,ϱ ,r used in Lemma S3.5 are determined by κ,κ,Λ ,Λ ,ϱ .
|     |     |     | 0   | 1   | 0   |     |     |     |     |     | min | max 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
The tracking constant enters only through the requirement 2Kr¯ /n < ς , which holds for
n 0
| all | large | n for | each | of the | finitely many | constants |     | K   | .   |     |     |     |
| --- | ----- | ----- | ---- | ------ | ------------- | --------- | --- | --- | --- | --- | --- | --- |
v
The constants are allowed to increase with depth. Suppose a sample window has endpoint
errors at most K r¯ relative to node v. By Lemma S3.6, the maximizer of its noiseless
|     |     |     | v   | n   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
discrete profile is at most (C′ +C′ K )r¯ from the population split nc(α,β). Lemma S3.5
|     |     |     |     |     |     | v n |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 0 L |     |     |     |     |     |     |     |
places the maximizer of the observed contrast at most a further C r¯ away. Each child
1,v n
window of the sample recursion retains one endpoint of its parent and uses this observed
maximizer as its other endpoint. Its two endpoint errors are therefore bounded by K r¯ ,
v′ n
with K as defined above. The constants K need not decrease from parent to child.
|     |     | v′  |     |     |     |     | v   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Finiteness of T (g) is enough: the recursively defined constants remain finite and their
| maximum |     | is  | C . |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
⋆
45

Proposition S3.1 (Recursion on tracking windows) Assume Assumption 4.1 and
Assumption 4.2. There is n such that for n ≥ n , on E , the following holds for every v =
|     |     |     |     | 0   |     |     | 0   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(α,β) ∈ T (g) and every window (s,e] tracking it at scale K : the call LABS(X,s,e,λ)
v
|     | ˆ   |     | ˆ   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
returns a set T with |T | = |V(α,β)| and, writing V(α,β) = {j < ··· < j } and the
|     |     |     |     |     |     |     |     |     | 1   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
| elements | of T in | increasing |        | order | as τˆ(1) < | ···  | < τˆ(k), |          |     |     |     |
| -------- | ------- | ---------- | ------ | ----- | ---------- | ---- | -------- | -------- | --- | --- | --- |
|          |         |            | |τˆ(i) | −τ    | | ≤ C      | r¯ , | i =      | 1,...,k. |     |     |     |
|          |         |            |        |       | ji         | ⋆ n  |          |          |     |     |     |
Proof. The radii of Definition S3.2 are fixed first and n afterwards. We induct on the
0
height of the subtree rooted at (α,β), finite by Assumption 4.1. Write V := V(α,β) and
k := |V|.
Case k = 0. By Lemma S3.3 every kink has x (s,e) ≤ C r¯ +1, so Lemma S3.4 returns
|     |     |     |     |     |     | j   |     | ⋆ n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∅.
Case k = 1, V = {j}. Here c(α,β) = q exactly, and it is simplest to apply Lemma S3.5
j
directly with U = {j} and b∗ = τ : (i) holds with ϱ = κ/2 by Lemma S3.3; (ii) holds
|     |     |               |     |     | j   |     |     | 1   |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | d(κ/2)3/2n1/2 |     |     | κ′  |     |     |     |     |     |     |
with A = ℓ ≥ c and = c , since by Lemma S2.1(c) and Lemma S2.4,
|     | j   | ℓ   |     |     | 0   |     |     |     |     |         |          |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- |
|     |     |     |     |     |     |     |     |     |     | (cid:0) | (cid:1)2 |
|D (τ )|−|D (b)| = ℓ {1−ρ(τ ,b)} ≥ ℓ c min{((b−τ )/x )2,1} ≥ ℓ c (b−τ )/n ,
| U j | U   |     | j   | j   |     | j 0 |     | j j |     | j 0 | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
using x ≤ n and |b − τ | ≤ n; and (iii) is Lemma S3.3. Lemma S3.5 now shows that
|     | j   |     | j   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the proposal statistic max C (b) exceeds λ, so the proposal test on (s,e] is accepted,
|     |     |     | b∈Bs,e | s,e |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
and |b−τ | ≤ C r¯ . For the left child, the endpoint s is unchanged from the parent and
|     | j   | 1,v n |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
still satisfies |s − nα| ≤ K r¯ , while its new right endpoint satisfies |b − nq | ≤ C r¯ .
|     |     |     | v   | n   |     |     |     |     |     | j   | 1,v n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     |     | ˆ   |     | ˆ   | ˆ     |
Similarly, the right child retains e and has new left endpoint b. Hence (s,b] and (b,e] track
(α,q ) and (q ,β) at scale max{K ,C } ≤ K . Neither population child contains a kink
| j   | j   |     |     |     | v 1,v | v′  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
strictly inside it, so both live-kink sets are empty and both recursive calls return ∅. The
|     |     |     |     |     |     |     |     |     | ˆ   | ˆ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
look-ahead branch is not entered, and the parent call returns {b}, with |b−τ | ≤ C r¯ .
|     |     |     |     |     |     |     |     |     |              | j   | ⋆ n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- |
|     |     |     |     |     |     |     |     | b∗  | |b∗−nc(α,β)| |     | (C′ |
Case k ≥ 2. Lemma S3.6, applied at scale K , provides a with ≤ +
|     |     |     |     |     |     | v   |     |     |     |         | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
| C′  |     |     |     |     |     |     |     |     |     | ˆ b−b∗| |     |
K )r¯ andverifieshypotheses(i)–(iii)ofLemmaS3.5, whichthengives| ≤ C r¯ .
| L v | n   |     |     |     |     |     |     |     |     |     | 1,v n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Hence
|     |     | (cid:12)    |     | (cid:12) | (cid:0) |      |      | (cid:1) |      |     |     |
| --- | --- | ----------- | --- | -------- | ------- | ---- | ---- | ------- | ---- | --- | --- |
|     |     | ˆ b−nc(α,β) |     |          | ≤ C     | +C ′ | +C ′ | K r¯ ≤  | K r¯ | ,   |     |
|     |     | (cid:12)    |     | (cid:12) | 1,v     |      |      | v n     | v′ n |     |     |
0 L
and since the other endpoint of each child is inherited unchanged, at scale K ≤ K v′ ,
v
the children (s,b] ˆ and (b,e] ˆ track (α,c) and (c,β) at scale K . The induction hypothesis
v′
applies to both, giving |L| = |V | and |R| = |V | with each returned point within C r¯ of
|           |           |     |     | L     |                | R   |      |     |     |     | ⋆ n |
| --------- | --------- | --- | --- | ----- | -------------- | --- | ---- | --- | --- | --- | --- |
| its kink. | We follow | the | two | cases | of Proposition |     | 4.1. |     |     |     |     |
Case A: c ∈/ {q }. Then |V |+|V | = k ≥ 2 and the look-ahead branch is entered. Every
|     | l   |     | L   | R   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
kink has x (s′,e′) ≤ C r¯ + 1: if both children are non-empty, s′ and e′ lie within C r¯
|     | j   |     | ⋆ n |     |     |     |     |     |     |     | ⋆ n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of τ and τ for consecutive kinks q < q of g, so no kink lies strictly between and all
| ja  | j   |     |     |     | ja  | j   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | b   |     |     |     |     | b   |     |     |     |     |     |
others are outside (s′,e′] by the κ-separation of (S6); if L = ∅ then s′ = s and e′ is within
46

C r¯ of τ , and no kink lies in (α,q ); the case R = ∅ is symmetric. By Lemma S3.4,
| ⋆ n | j1  |     |     |     |     | j1  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the maximum contrast in the re-test window is below λ. The re-test therefore rejects the
parent candidate and the call returns L∪R, of size k. Order preservation holds because
| τ −τ   | ≥ δ | n−1 | >   | 2C r¯ | for n large. |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| j b ja |     | min |     | ⋆ n   |              |     |     |     |     |     |     |     |
Case B: c = q , j∗ ∈ V. Then |V | + |V | = k − 1 ≥ 1 and the look-ahead branch is
|     |     | j∗  |     |     | L   | R   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
entered. Exactly as in Proposition 4.1, τ is the only kink at distance more than C r¯ +1
|     |     |     |     |     |     | j∗  |     |     |     |     | ⋆   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(s′,e′],
from both edges of its neighbors in {q : j ∈ V}∪{α,β} sitting at the edges, and
j
|     |     | min(τ | −s′, | e′  | −τ ) | ≥ nmin(κ,δ |     | )−C | r¯ −1 | ≥   | 1κn. |     |
| --- | --- | ----- | ---- | --- | ---- | ---------- | --- | --- | ----- | --- | ---- | --- |
|     |     |       | j∗   |     | j∗   |            |     | min | ⋆ n   |     | 2    |     |
In particular e′−s′ ≥ κn, so B ̸= ∅ and the re-test is performed; applying Lemma S3.5
s′,e′
to (s′,e′] as in the case k = 1, with U = {j∗} and b∗ = τ , the re-test statistic exceeds
j∗
λ and | ˆ b′ −τ | ≤ C r¯ . The call returns L∪{ ˆ b′}∪R, of size k, and order preservation
|         |       | j∗   | ⋆ n        |     |     |     |     |     |     |     |     |     |
| ------- | ----- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| follows | as in | Case | A.         |     |     |     |     |     |     |     |     | □   |
| S3.4    | Proof |      | of Theorem |     | 4.1 |     |     |     |     |     |     |     |
Work on E , which has probability tending to one by Lemma S2.3, and let n ≥ n with
|         | n           |     |      |     |         |            |     |       |     |     | 0   |     |
| ------- | ----------- | --- | ---- | --- | ------- | ---------- | --- | ----- | --- | --- | --- | --- |
| n as in | Proposition |     | S3.1 | and | C as in | Definition |     | S3.2. |     |     |     |     |
| 0       |             |     |      |     | ⋆       |            |     |       |     |     |     |     |
If N ≥ 1, the initial call is on (0,n], which tracks the root node (0,1) ∈ T (g) at scale
K = 0, both endpoints being exact, and V(0,1) = {1,...,N} since every kink is
(0,1)
ˆ
interior. Proposition S3.1 applied at the root gives N = N and |τˆ −τ | ≤ C r¯ for every
|          |        |           |     |      |       |     |     |     |     | (j) | j ⋆ n |     |
| -------- | ------ | --------- | --- | ---- | ----- | --- | --- | --- | --- | --- | ----- | --- |
| j, which | is the | assertion |     | with | C = C | .   |     |     |     |     |       |     |
⋆
If N = 0 then g is affine, meaning that it is a straight line, and no window contains a
kink. Lemma S3.4 applies to (0,n]: the maximum contrast is at most Z < λ, the root
n
| proposal | test | is rejected, |     | and | T ˆ = ∅. |     |     |     |     |     |     | □   |
| -------- | ---- | ------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
n
1Λ
Remark S3.2 (Uniformity in the threshold) Fix η > 0 and ς > 0 with ς < ,
2 det
1ΛM,R
or with ς < for LABS-Grid. Conditional on E , the argument above is deter-
|     |     | 2 det |     |     |     |     |     |     | n   |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ministic once λ is specified. The threshold enters only through two comparisons. On a
window with no visible kink, the maximum contrast is at most o(1)+Z and must be below
n
λ. On every non-empty population node used for a proposal, and on every Case B one-
kink re-test window, the corresponding maximum population contrast is at least 1Λ n1/2
det
2
and the sample statistic must exceed λ. Both comparisons hold simultaneously for every
λ ∈ [(1 + η)Z ,ςn1/2] once n is large. Hence, on E and for n ≥ n (η,ς), the con-
|     |     | n   |     |     |     |     |     | n   |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
clusion of Theorem 4.1 holds for all thresholds in this band simultaneously, including a
data-dependent threshold whose value lies in the band. The same statement holds for
ΛM,R
| Theorem | S4.1, | with |     | from | (S9) | in place | of Λ | .   |     |     |     |     |
| ------- | ----- | ---- | --- | ---- | ---- | -------- | ---- | --- | --- | --- | --- | --- |
|         |       |      | det |      |      |          |      | det |     |     |     |     |
47

It is Λ and not Λ that must appear here, because the Case B re-test window is
|     | det |     | min |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in general not a node of T (g) and its amplitude can be the smaller of the two. Take
q = 1 −δ, q = 1, q = 1 +δ with d = d = d = 1 and δ small. By symmetry the root
| 1 2 |     | 2   | 2 3 | 2   |     | 1   | 2   | 3   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
maximizer is q , so the root split is Case B; each child carries one live kink, of amplitude
2√
δ3/2(1−2δ)3/2/ 3, and this is Λ , the root amplitude being of order one. The re-test acts
|          |          |     |               |     | min |            | √   |       |          |                   |     |       |
| -------- | -------- | --- | ------------- | --- | --- | ---------- | --- | ----- | -------- | ----------------- | --- | ----- |
|          |          |     |               |     |     | δ3/2/(23/2 |     |       |          | {23/2(1−2δ)3/2}−1 |     | 2−3/2 |
| on (q ,q | ), where |     | the amplitude |     | is  |            |     | 3), a | fraction |                   |     | → <   |
| 1        | 3        |     |               |     |     |            |     |       |          |                   |     |       |
| 1        |          |     | cn1/2         |     |     |            |     |       |          |                   | 1Λ  |       |
of Λ . Any λ = with the re-test amplitude below c and c < therefore lies
| 2   | min |     |     |     |     |     |     |     |     |     | 2 min |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
in the band that Λ would permit, yet LABS recovers q and q and discards q .
|     |             |     | min |     |     |           |     |     |     | 1 3 |     | 2   |
| --- | ----------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
| S4  | Consistency |     |     |     | of  | LABS-Grid |     |     |     |     |     |     |
Theorem 4.1 concerns Algorithm 2, which is LABS-Grid with M = R = 2. This sec-
tion extends it to arbitrary fixed M ≥ 2 and R ≥ 2. The conclusion and the rate are
unchanged. The conditions required are the analogues of Assumption 4.1 and Assump-
tion 4.2 for the grid, and they constrain M only. The proposal grid size M determines
the proposed split and hence the population recursion tree. By Proposition S4.1, a re-test
window contains either no live kink or exactly one live kink; in the latter case its pooled
profile has a unique, non-degenerate maximizer for every fixed R. Therefore no analogous
| condition | is  | needed | for | the re-test |     | grid | size R. |     |     |     |     |     |
| --------- | --- | ------ | --- | ----------- | --- | ---- | ------- | --- | --- | --- | --- | --- |
Two points make the extension possible. The first is that the noise bound of Lemma S2.3
is already a maximum over all sub-intervals of {1,...,n}, so it covers every sub-interval
a grid of any size can produce, and the same threshold works for every M. The second is
that a grid sub-interval of the current window is contained in that window, so a kink close
to an edge of the window is close to an edge of, or outside, every sub-interval; the signal
strength dichotomy of Corollary S2.1 therefore transfers to the sub-intervals on which the
grid search evaluates the contrast. What the grid does change is the location of the split,
and hence the recursion tree, so the population objects have to be redefined for each M.
| S4.1 | The | grid |     | statistic |     | and | the | population |     | grid | recursion |     |
| ---- | --- | ---- | --- | --------- | --- | --- | --- | ---------- | --- | ---- | --------- | --- |
For a window (s,e] and M ≥ 2 let g = s < g < ··· < g = e be the M-point grid of
|         |     |        |      |        |         | 1     |       | 2       |     | M      |         |     |
| ------- | --- | ------ | ---- | ------ | ------- | ----- | ----- | ------- | --- | ------ | ------- | --- |
| Section | 3.2 | of the | main | paper, | and     | write |       |         |     |        |         |     |
|         |     |        |      |        | (cid:8) |       |       |         |     |        | (cid:9) |     |
|         |     |        | P    | (s,e)  | :=      | (i,j) | : 1 ≤ | i < j ≤ | M,  | g −g ≥ | 3       |     |
|         |     |        | M    |        |         |       |       |         |     | j i    |         |     |
for the admissible pairs. The grid statistic and its maximizer are
|     |     |         |     |        | (cid:8)(cid:12) |         | (cid:12) |         |     |            | (cid:9) |     |
| --- | --- | ------- | --- | ------ | --------------- | ------- | -------- | ------- | --- | ---------- | ------- | --- |
|     |     | C(M)(b) |     | := max | (cid:12)⟨X,ψ    | ˆgi,gj⟩ |          | : (i,j) | ∈ P | (s,e), b ∈ | B ,     |     |
|     |     | s,e     |     |        |                 |         | (cid:12) |         | M   |            | gi,gj   |     |
b
(S14)
|     |     |     | ˆ b | := minargmaxC(M)(b). |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
s,e
b
48

where ψ ˆgi,gj denotes the unit contrast vector of Section S2 formed on the sub-window
b
(g ,g ]. This is the routine GridSearch(X,s,e,M), and (S14) returns the pair ( ˆ b,W)
i j
C(M)( ˆ
| with W | = b). |     |     |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- | --- | --- |
s,e
At the population level, for a rescaled window (α,β) put γ = α+(i−1)(β−α)/(M−1),
i
i = 1,...,M, and define the pooled profile and its leftmost maximizer
|     |     |     | (cid:12) | (cid:12) |     |     |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- |
D ¯(M)(v) := max (cid:12)D ¯ (v) (cid:12), c (α,β) := minargmaxD ¯(M)(v), (S15)
|     |     |     | γiγj | M   |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     | αβ  |     |      |     |     | v   | αβ  |
i<j:γi<v<γj
with Λ (α,β) := max D ¯(M)(v). Here D ¯ is the profile of Section 4.2 of the main paper
|     | M   | v   |     | γγ′ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
αβ
formed on (γ,γ′), built from the kinks in V(γ,γ′) = {l : γ < q < γ′}. Because that profile
l
is defined through the unnormalized inner product of L2(γ,γ′), values on sub-windows
of different lengths are on a common scale, as required in (S15); this is the population
counterpart of the observation in Section 3.2 of the main paper that unit-norm contrast
vectors make sub-interval contrasts directly comparable. Since (γ ,γ ) = (α,β) is itself
1 M
an admissible pair, Λ (α,β) ≥ Λ(α,β) > 0 whenever V(α,β) ̸= ∅, and Λ (α,β) = 0
|     |     | M   |     |     |     |     | M   |
| --- | --- | --- | --- | --- | --- | --- | --- |
otherwise.
At a node with a non-empty live set, call a pair (i,j) attaining if the largest absolute
profile value on its sub-window equals the pooled maximum. Write
|     |         | (cid:110) |       |                |               |                    | (cid:111) |
| --- | ------- | --------- | ----- | -------------- | ------------- | ------------------ | --------- |
|     | P∗(α,β) |           |       |                | (cid:12) ¯    | (cid:12)           |           |
|     |         | := (i,j)  | : 1 ≤ | i < j ≤ M, max | (cid:12)D (v) | (cid:12) = Λ (α,β) |           |
|     |         |           |       |                | γiγj          | M                  |           |
v
| for the | set of all such | pairs. |     |     |     |     |     |
| ------- | --------------- | ------ | --- | --- | --- | --- | --- |
Definition S4.1 (Population LABS-Grid) Fix M,R ≥ 2. POP (α,β) is Defini-
M,R
tion 4.1 with c(α,β) replaced by c (α,β) in the proposal step and by c (α′,β′) in the
|     |     |     | M   |     |     |     | R   |
| --- | --- | --- | --- | --- | --- | --- | --- |
re-test step. Write T (g) for the set of windows at which POP is invoked, starting
|     |     | M,R |     |     |     | M,R |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
from (0,1), and G (g) for the set of grid points of all those windows together with the
M,R
| grid points | of the | associated | re-test windows. |     |     |     |     |
| ----------- | ------ | ---------- | ---------------- | --- | --- | --- | --- |
Proposition S4.1 (Population exactness) If T (g) is finite and c ,c are well de-
|     |     |     |     |     | M,R |     | M R |
| --- | --- | --- | --- | --- | --- | --- | --- |
fined at the relevant windows, then POP (α,β) = {q : j ∈ V(α,β)} at every node; in
|            |     |            |        | M,R | j   |     |     |
| ---------- | --- | ---------- | ------ | --- | --- | --- | --- |
| particular | POP | (0,1) = {q | ,...,q | }.  |     |     |     |
|            | M,R |            | 1 N    |     |     |     |     |
Proof. The proof of Proposition 4.1 uses the maximizer only through its position relative
| to the | kinks, and | applies verbatim | once | two facts | are checked. |     |     |
| ------ | ---------- | ---------------- | ---- | --------- | ------------ | --- | --- |
First, detection is unchanged: Λ (α,β) > 0 if and only if V(α,β) ̸= ∅, as noted above.
M
Second, if V(α,β) = {j} then c (α,β) = q . Indeed, a sub-window with q in its interior
|     |     |     | M   | j   |     |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- |
has q as its only live kink, so by Lemma S2.1(c) its profile attains its maximum at q
j j
and nowhere else; a sub-window without q in its interior has an identically zero profile.
j
The pooled profile is therefore maximized at q and nowhere else, whatever the relative
j
49

sizes of the individual maxima. The same argument applies to c on the re-test window,
R
which in Case B of the proof of Proposition 4.1 includes exactly one live kink. □
| S4.2 | Assumptions |     |     |     |     |     |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Assumption S4.1 (Termination, grid) POP started at (0,1) terminates, that is,
M,R
| T   | (g) is | finite. |     |     |     |     |     |     |     |     |     |
| --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M,R
| Assumption |     | S4.2 | (Non-degeneracy, |     |     | grid) |     |     |     |     |     |
| ---------- | --- | ---- | ---------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
At every node of T (g) with a non-empty live set, the pooled profile D ¯(M) has a unique
|           |     |         | M,R |            |     |       |       |            |     | αβ  |     |
| --------- | --- | ------- | --- | ---------- | --- | ----- | ----- | ---------- | --- | --- | --- |
| maximizer |     | c (α,β) | on  | (α,β), and | for | every | (i,j) | ∈ P∗(α,β), |     |     |     |
M
|     |     |     |     |     | (cid:12)       | (cid:12) (cid:0) |       | (cid:1) |     |     |     |
| --- | --- | --- | --- | --- | -------------- | ---------------- | ----- | ------- | --- | --- | --- |
|     |     |     |     |     | ∂2 (cid:12)D ¯ | c                | (α,β) | < 0.    |     |     |     |
γiγj (cid:12) M
v
Two remarks on the form of these conditions. First, no condition is imposed on R; the
reason is given in Remark S4.1 below. Second, when V(α,β) is a singleton, Assump-
tion S4.2 is automatic: the second step of the proof of Proposition S4.1 shows that the
maximizer is then unique and equal to the kink, and non-degeneracy at that point fol-
lows from Lemma S2.4, exactly as in the case k = 1 of Proposition S3.1. The condition
therefore has content only at nodes including two or more live kinks.
Under Assumptions S4.1 and S4.2, and again for N ≥ 1, the sets of nodes, grid points
and attaining pairs are finite. We now define the finite-set extrema used in the grid proof.
Let Q be the set of triples ((α,β),i,j) for which (α,β) ∈ T (g) has a non-empty live
M,R
P∗(α,β):
| set | and (i,j) | ∈/  |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:16)
|     |      |     |     | (cid:8) |       |       |      |     |               | (cid:9) |     |
| --- | ---- | --- | --- | ------- | ----- | ----- | ---- | --- | ------------- | ------- | --- |
|     | κ := | min | {δ  | }∪ |q   | −γ| : | γ ∈ G | (g), | 1 ≤ | l ≤ N, q ̸= γ |         |     |
|     | M    |     | min | l       |       |       | M,R  |     | l             |         |     |
(cid:17)
|     |     |     |           | (cid:8)    |     |           |     |          |           | (cid:9) |       |
| --- | --- | --- | --------- | ---------- | --- | --------- | --- | -------- | --------- | ------- | ----- |
|     |     |     | ∪         | |c (α,β)−q |     | | : (α,β) |     | ∈ T (g), | c (α,β)   | ̸= q ,  | (S16) |
|     |     |     |           | M          |     | l         |     | M,R      | M         | l       |       |
|     |     |     | (cid:110) |            |     |           |     |          | (cid:111) |         |       |
¯
|     | ι := | min | Λ (α,β)−max |     | |D  | (v)| | :   | ((α,β),i,j) | ∈ Q . |     | (S17) |
| --- | ---- | --- | ----------- | --- | --- | ---- | --- | ----------- | ----- | --- | ----- |
|     |      |     | M           |     | v   | γiγj |     |             |       |     |       |
The minimum defining ι is taken only over nodes with a non-empty live set and non-
| attaining | pairs. | If  | there | is no such | pair, | set | ι = 1. | Also set |     |     |     |
| --------- | ------ | --- | ----- | ---------- | ----- | --- | ------ | -------- | --- | --- | --- |
|           |        |     |       | Λ :=       |       | min |        | Λ (α,β). |     |     |     |
|           |        |     |       | min        |       |     |        | M        |     |     |     |
(α,β)∈TM,R(g):V(α,β)̸=∅
Then κ > 0 because every distance included in its definition is positive and there are
M
finitelymanyofthem. Similarly, Λ > 0by(S15), andι > 0becauseeverynon-attaining
min
| pair | has a | maximum | strictly | below | Λ   | (α,β). |     |     |     |     |     |
| ---- | ----- | ------- | -------- | ----- | --- | ------ | --- | --- | --- | --- | --- |
M
50

It remains to define the constants controlling curvature, interior margin and endpoint per-
turbations. These constants are not defined directly from the pooled profile. A maximum
of smooth individual profiles need not be differentiable at a point where two profiles have
the same value but different derivatives and the identity of the larger profile changes.
We instead work with each individual profile. For each node (α,β) with a non-empty
|     |     |     |     | P∗(α,β), |     |     |     |     |     | ¯   |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
live set and each (i,j) ∈ the individual absolute profile |D | has its unique
γiγj
maximum at c (α,β). Indeed, a second maximizer would also maximize the pooled pro-
M
file, contrary to Assumption S4.2. The same assumption gives a strictly negative second
derivative there. Apply the construction in Lemma S3.2 to each such individual profile
on (γ ,γ ). Define κ, ϱ and ς as, respectively, the minima of the resulting positive
|     | i   | j   |     | 0   | 0   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
curvature constants, positive relative interior margins and positive endpoint-perturbation
radii. DefineΛ andC as, respectively, themaximaoftheindividualprofileamplitudes
|     |     | max |     | L   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and the finite endpoint-Lipschitz constants. All five extrema are over the finitely many
node–pair combinations, so the three minima are strictly positive and the two maxima
are finite. These are the constants used when Lemma S3.2 is applied to an attaining pair
| in  | Lemma | S4.2. |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The grid points must be included in κ because they are endpoints of the sub-windows on
M
which the contrast is evaluated, even though they are not endpoints of recursion windows.
| S4.3 |     | Consistency |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Throughout, (s,e] tracks (α,β) ∈ T (g) at scale C in the sense of Definition S3.1, and
|     |     |     |     |     | M,R |     |     | ⋆   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
we work on the event E of Lemma S2.3. Note first that the sample and population grids
n
correspond: since |s−nα| ≤ C r¯ and |e−nβ| ≤ C r¯ , rounding gives
|     |     |     |     |        | ⋆ n |      |     | ⋆ n |          |     |     |       |
| --- | --- | --- | --- | ------ | --- | ---- | --- | --- | -------- | --- | --- | ----- |
|     |     |     |     | |g −nγ | | ≤ | C r¯ | +1, | i = | 1,...,M, |     |     | (S18) |
|     |     |     |     | i      | i   | ⋆ n  |     |     |          |     |     |       |
so that each sample sub-window (g ,g ] tracks the population sub-window (γ ,γ ) at scale
|     |     |     |     |     | i   | j   |     |     |     |     | i j |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C +1. LemmaS3.3, appliedwithκ inplaceofκ, thengivesthedichotomyoneverysub-
| ⋆   |     |     |     |     | M   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
window: for l ∈ V(γ ,γ ) one has x (g ,g ) ≥ 1κ n, and otherwise x (g ,g ) ≤ C r¯ +2.
|     |     |     | i   | j   | l   | i j | 2   | M   |     | l i | j   | ⋆ n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma S4.1 (No detection, grid) Fix C and M ≥ 2. There is n such that for n ≥
|     |     |     |     |     |     |     | ⋆   |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n , on E : if (s,e] is any window with x (s,e) ≤ C r¯ +1 for every j, then max C(M)(b) <
| 0   |     | n   |     |     |     | j   |     | ⋆ n |     |     | b   | s,e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
λ. Thus the value W returned by GridSearch(X,s,e,M) fails the proposal condition
W > λ in Algorithm S1, and the call returns ∅ without making a split.
Proof. Let (i,j) ∈ P (s,e) and let τ lie in the interior of (g ,g ]. Since g ≥ s and g ≤ e,
|      |      |     | M      |        |      | l       |       |        | i j | i   |     | j     |
| ---- | ---- | --- | ------ | ------ | ---- | ------- | ----- | ------ | --- | --- | --- | ----- |
| both | τ −g | ≤ τ | −s and | g +1−τ |      | ≤ e+1−τ |       | , so   |     |     |     |       |
|      | l    | i l |        | j      | l    |         |       | l      |     |     |     |       |
|      |      |     |        | x (g   | ,g ) | ≤ x     | (s,e) | ≤ C r¯ | +1. |     |     | (S19) |
|      |      |     |        | l      | i j  |         | l     | ⋆      | n   |     |     |       |
51

By Corollary S2.1(a), the signal strength of τ on (g ,g ] is O{n−1/4(logn)3/4}. By
|     |     |     |     |     |     | l   | i j |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma S2.1(b) the noiseless contrast on that sub-window is at most N times this, and
(cid:0)M(cid:1)
adding Z and maximizing over the at most admissible pairs gives max C(M)(b) ≤
|     | n   |     |     |     |     |     |     |     | b s,e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
2
o(1)+σ(8logn)1/2 < λ for n large, since M is fixed and Θ > 1. □
Formula(S19)isthestepthatextendstheno-detectionargumentfromtheoriginalwindow
to every grid sub-window: shrinking a window can only move an interior kink closer to an
endpoint. Thus a kink that has insufficient signal strength on (s,e] also has insufficient
signal strength on each sub-window on which the grid search evaluates the contrast.
| Lemma | S4.2 (Detection |     | and | localization, |     | grid) |     |     |     |
| ----- | --------------- | --- | --- | ------------- | --- | ----- | --- | --- | --- |
Let (α,β) be a node of T (g) with a non-empty live set, and let (s,e] track it at scale
M,R
C . Under Assumptions S4.1 and S4.2 there are n and C such that for n ≥ n , on E ,
| ⋆   |     |            |     |      |               | 0     | 1          |        | 0 n |
| --- | --- | ---------- | --- | ---- | ------------- | ----- | ---------- | ------ | --- |
|     |     |            |     |      | (cid:12) ˆ    |       | (cid:12)   |        |     |
|     |     | maxC(M)(b) |     | > λ, | (cid:12) b−nc | (α,β) | (cid:12) ≤ | C r¯ . |     |
|     |     |            | s,e |      |               | M     |            | 1 n    |     |
b
Proof. Detection does not require Assumption S4.2. Let (i,j) ∈ P∗(α,β). Its population
maximum is Λ (α,β) ≥ Λ by the definition of Λ . The maximum in (S14) is at least
|     | M   |     | min |     |     | min |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the maximum over this pair, which by (S12) applied on (g ,g ] is at least n1/2{Λ (α,β)−
|     |     |     |     |     |     |     | i j |     | M   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1Λ n1/2,
o(1)}−Z ≥ andthisexceedsλforlargen. Thefull-windowamplitudeΛ(α,β)
n 2 min
is no larger than the pooled amplitude at the same node and may be strictly smaller than
the minimum pooled amplitude across all nodes. It therefore cannot replace Λ (α,β)
M
in this lower bound while retaining the constant Λ . One could introduce a second,
min
possibly smaller, positive constant by taking the minimum of Λ(α,β) over the grid-tree
nodes, but it is unnecessary because the grid statistic searches the attaining pairs directly.
For localization, write Λ = Λ (α,β) and abbreviate P∗(α,β) to P∗. By (S18) and
|               |     |                  | M           | M         |            |                   |           |               |     |
| ------------- | --- | ---------------- | ----------- | --------- | ---------- | ----------------- | --------- | ------------- | --- |
| (S12) applied | on  | each             | sub-window, |           |            |                   |           |               |     |
|               |     |                  |             | (cid:110) |            |                   | (cid:111) |               |     |
|               |     | (cid:12) ˆgi,gj⟩ | (cid:12)    | n1/2      | (cid:12) ¯ | (cid:12)          |           | +O{(logn)1/2} |     |
|               | max | (cid:12)⟨X,ψ     | (cid:12) =  | max       | (cid:12)D  | (v) (cid:12)+o(1) |           |               |     |
|               |     |                  | b           |           |            | γiγj              |           |               |     |
|               | b   |                  |             |           | v          |                   |           |               |     |
uniformly over the finitely many pairs. Hence for (i,j) ∈/ P∗ the left side is at most
n1/2(Λ −ι+o(1)), while for (i,j) ∈ P∗ it is at least n1/2(Λ −o(1)). For n large the
| M   |     |     |     |     |     |     |     | M   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two ranges are disjoint, so the maximum in (S14) is attained at a pair in P∗.
Let (i,j) ∈ P∗ be that pair. If v maximizes |D ¯ | then D ¯(M)(v) = Λ , so v = c (α,β)
|     |     |     |     |     |     | γiγj |     | M   | M   |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
αβ
by the uniqueness in Assumption S4.2: every pair in P∗ attains its maximum at c (α,β)
M
and there only. Assumption S4.2 guarantees the negative second derivative at that point,
so Lemma S3.2 holds for the sub-window (γ ,γ ) with V(γ ,γ ) in place of V(α,β), and
|     |     |     |     |     | i   | j   | i   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LemmaS3.6, whichisstatedforanyfixedrescaledwindowatwhichthoseconclusionshold
and not only for nodes of T (g), applies to (g ,g ]. That the sample sub-window tracks
i j
the population one at scale C +1 is (S18), and the kink dichotomy on it is Lemma S3.3
⋆
52

with κ in place of κ. Since c (α,β) lies in the interior of (γ ,γ ) with margin at least
|     | M   |     |     |     | M   |     |     |     |     |     | i j |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ϱ (γ −γ ), Lemma S3.5 gives |b−nc ˆ (α,β)| ≤ C r¯ , with C the largest of the finitely
| 0    | j         | i   |              |     |     | M   |     |     | 1 n |     | 1   |     |     |
| ---- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| many | constants |     | so obtained. |     |     |     |     |     |     |     |     |     | □   |
Lemma S4.3 (Grid re-test on a one-kink window) Let (α′,β′) be one of the finitely
many Case B re-test windows arising in the proof of Proposition S4.1, so that V(α′,β′) =
{j∗}, and let (s′,e′] track it at some fixed scale K. There is a constant CM,R, not depending
rt
| on  | K, and | an n | = n | (K),    | such that | for    | n ≥ | n , | on E     | ,           |            |     |     |
| --- | ------ | ---- | --- | ------- | --------- | ------ | --- | --- | -------- | ----------- | ---------- | --- | --- |
|     |        |      | 0   | 0       |           |        |     | 0   |          | n           |            |     |     |
|     |        |      |     |         |           |        |     |     | (cid:12) | (cid:12)    |            |     |     |
|     |        | maxC | (   | R ) (b) | ≥ 1 ΛM    | ,Rn1/2 | >   | λ,  | ˆ b′     | −τ          | ≤ C M ,Rr¯ | .   |     |
|     |        |      |     |         |           |        |     |     | (cid:12) | j∗ (cid:12) |            | n   |     |
|     |        |      | s   | ′ ,e ′  | 2         | det    |     |     |          |             | r t        |     |     |
b
Proof. The population re-test window (α′,β′) contains the single live kink q . Hence, by
j∗
the second step of the proof of Proposition S4.1, its pooled R-grid profile is maximized at
q and nowhere else, whatever the relative sizes of the individual sub-window maxima.
j∗
The pooled maximum equals |d |∥Ψα′β′∥, which is at least ΛM,R by (S9). Detection
|     |     |     |     |     | j∗  | q   |     |     |     |     | det |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j∗
follows as in Lemma S4.2, from (S12) applied to a pair attaining this pooled maximum.
Forlocalizationapositivegapbetweenanattainingpairandtheotherpairsisneeded, and
the detection constant, being an amplitude rather than a difference, does not provide one.
Here the gap follows from monotonicity of the one-kink amplitude. Writing A = q −α′
j∗
| and | B = | β′ −q | , the | scaling | relation | of  | Lemma | S3.1 | gives |     |     |     |     |
| --- | --- | ----- | ----- | ------- | -------- | --- | ----- | ---- | ----- | --- | --- | --- | --- |
j∗
A3B3
|     |     | (cid:13) (cid:13)Ψα′β′(cid:13) | 2   |     |     |     |           |     |     |        | AB  |     |     |
| --- | --- | ------------------------------ | --- | --- | --- | --- | --------- | --- | --- | ------ | --- | --- | --- |
|     |     |                                |     | =   |     | =   | 1H(A,B)3, |     |     | H(A,B) | :=  | ,   |     |
q (cid:13)
|     |     |       | j∗  | 3(A+B)3 |        |     | 3     |     |     |          | A+B      |           |     |
| --- | --- | ----- | --- | ------- | ------ | --- | ----- | --- | --- | -------- | -------- | --------- | --- |
|     |     | B2/(A |     | B)2     |        |     | A2/(A |     | B)2 |          |          |           |     |
| and | ∂ H | =     | +   |         | > 0, ∂ | H = |       | +   |     | > 0. The | one-kink | amplitude | is  |
|     | A   |       |     |         |        | B   |       |     |     |          |          |           |     |
therefore strictly increasing under enlargement of the window at either end, so among
the R-grid sub-windows of (α′,β′) that contain q the full window (γ′,γ′ ) = (α′,β′) is
j∗
|     |     |     |     |     |     |     |     |     |     |     | 1   | R   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the unique maximizer, the others containing q being proper sub-windows and those not
j∗
| containing |     | it having | amplitude |     | zero.    | To               | state        | the        | gap, | set      |     |     |     |
| ---------- | --- | --------- | --------- | --- | -------- | ---------------- | ------------ | ---------- | ---- | -------- | --- | --- | --- |
|            |     |           |           |     | (cid:40) |                  | γ′γ′(cid:13) |            |      |          |     |     |     |
|            |     |           |           |     |          |                  | (cid:13)     |            | ′    |          | ′,  |     |     |
|            |     |           |           |     |          | |d j∗ |(cid:13)Ψ | i            | j(cid:13), | γ <  | q j∗ < γ |     |     |     |
|            |     |           |           | A   | :=       |                  | q j ∗        |            | i    | j        |     |     |     |
ij
|     |     |     |     |     |     | 0,  |     |     | otherwise, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
which is defined for every admissible pair, including those that do not contain the kink
and on which the profile vanishes identically. Since there are finitely many pairs and
| finitely | many | re-test | configurations, |     |           |     |     |     |           |     |     |     |     |
| -------- | ---- | ------- | --------------- | --- | --------- | --- | --- | --- | --------- | --- | --- | --- | --- |
|          |      |         |                 |     | (cid:110) |     |     |     | (cid:111) |     |     |     |     |
ιM,R
|     |     |     | :=  | min      | A   | −   | max          | A   | >   | 0,  | max∅ := | 0.  |     |
| --- | --- | --- | --- | -------- | --- | --- | ------------ | --- | --- | --- | ------- | --- | --- |
|     |     | rt  |     |          | 1R  |     |              | ij  |     |     |         |     |     |
|     |     |     |     | re-tests |     |     | (i,j)̸=(1,R) |     |     |     |         |     |     |
When R = 2 there is only the pair (1,2), the inner maximum is over the empty set,
ιM,2
and = minA > 0, which is the case R = 2 recommended in Remark S4.1. When
|     | rt  |     | 12  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
53

R > 2, strict monotonicity of H makes every proper sub-window containing the kink
strictly smaller, and the pairs not containing it contribute zero, so the minimum is again
positive. The gap argument of Lemma S4.2 then applies with ιM,R in place of ι: for n
rt
large the maximum in (S14) is attained on the full pair. On it q is interior with a fixed
j∗
κ′
margin, and Lemma S3.5 applies with U = {j∗}, b∗ = τ and = c , exactly as in
|     |     |     |     |     |     | j∗ 0 |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
the case k = 1 of Proposition S3.1. No node-level amplitude or curvature assumption is
used: a window with one live kink has a unique and non-degenerate pooled maximizer
for every grid size. The constant CM,R does not depend on the tracking scale K, because
rt
the parameters a , κ′ = c , ϱ and r fed into Lemma S3.5 are determined by ΛM,R, ιM,R,
|     | 0   |     | 0 1 0 |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
det rt
κ and the fixed margins alone; K enters only through the requirement that 2Kr¯ /n be
| M   |     |     |     |     |     |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
below ς and that the absorbed kinks have signal strength o(1), both of which hold for all
0
| large n | at each fixed | K.  |     |     |     |     |     | □   |
| ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Definition S4.2 (Grid tracking radii) The radii of Definition S3.2 cannot be used
unchanged, because the constant provided by Lemma S4.2 at a node depends on the
scale at which that node is tracked: its proof applies Lemma S3.6 on grid sub-windows
tracking population sub-windows at scale K + 1. The construction is instead recur-
v
sive in the same finite tree. Write G (K) for the constant that Lemma S4.2 provides
v
at v ∈ T (g) when its window tracks v at scale K. Set K := 0 and, for each child
|     | M,R |     |     |     |     | root |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
v′ of v, K := max{K , G (K )}; then C := max{max K , CM,R}, with CM,R as in
|     | v′  | v   | v v |     | ⋆   | v v rt | rt  |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- |
Lemma S4.3. The constants need not decrease from parent to child. Assumption S4.1
makes T (g) finite, so all recursively defined constants and their maximum are finite.
M,R
Proposition S4.2 (Recursion on tracking windows, grid) Assume S4.1 and S4.2.
There is n such that for n ≥ n , on E , the conclusion of Proposition S3.1 holds for
|     | 0   |     | 0   | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
LABS-Grid with parameters M and R, for every v ∈ T (g) and every (s,e] tracking it
M,R
| at scale | K , the radii | being | those of Definition |     | S4.2. |     |     |     |
| -------- | ------------- | ----- | ------------------- | --- | ----- | --- | --- | --- |
v
Proof. The induction is that of Proposition S3.1, on the height of the subtree of T (g),
M,R
with Lemma S4.1 in place of Lemma S3.4 and Lemma S4.2 in place of the combination of
Lemmas S3.6 and S3.5. The tracking radii are those of Definition S4.2 above. Only the
| three places | where | the grid | enters need | comment. |     |     |     |     |
| ------------ | ----- | -------- | ----------- | -------- | --- | --- | --- | --- |
Case k = 0. Lemma S3.3 gives x (s,e) ≤ C r¯ +1 for every j, and Lemma S4.1 returns
|     |     |     | j   |     | ⋆ n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
∅.
Case k = 1, V(α,β) = {j}. By Proposition S4.1, c (α,β) = q , and Lemma S4.2 gives
|     |     |     |     |     | M   | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
|b − τ | ≤ C r¯ without an additional non-degeneracy condition: with one live kink the
| j   | 1 n |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
pooled profile has its unique maximum at q by Proposition S4.1, and Lemma S2.4 gives
j
negative curvature there. The children track (α,q ) and (q ,β), both with empty live sets,
|     |     |     |     |     | j   | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
| so both | return ∅ by | the case | k = 0, and | the | call returns | {b}. |     |     |
| ------- | ----------- | -------- | ---------- | --- | ------------ | ---- | --- | --- |
54

ˆ
Case k ≥ 2. Lemma S4.2 gives |b − nc (α,β)| ≤ C r¯ , so the children track (α,c )
M 1 n M
and (c ,β) at their assigned scales from Definition S4.2. These child nodes have smaller
M
subtree height, so the induction hypothesis says that each recursive call returns exactly
one estimate for every live kink in that child, each within C r¯ of the corresponding kink.
⋆ n
The division into Cases A and B is by whether c (α,β) is a kink, as in Proposition S3.1.
M
Proposition S4.1 guarantees that the two population children contain all current live kinks
except, inCaseB,thekinkatthesplit. Italsoguaranteesthatthere-testwindowcontains
no live kink in Case A and exactly the omitted kink in Case B. In Case A the re-test
window therefore includes no live kink and every kink lies within C r¯ + 1 of one of its
⋆ n
edges, so Lemma S4.1, applied with R in place of M, shows that the re-test statistic is
below λ. In Case B the re-test window carries the single live kink τ at distance at least
j∗
1κ n from both edges. It is in general not a node of T (g), and its amplitude may
2 M M,R
be smaller than every node amplitude, which is why ΛM,R was introduced; Lemma S4.2,
det
which is stated at nodes, therefore cannot be applied to it. Lemma S4.3 is used instead;
it shows that the re-test statistic exceeds λ and that | ˆ b′ −τ | ≤ CM,Rr¯ ≤ C r¯ . Order
j∗ rt n ⋆ n
preservation is unchanged. □
Theorem S4.1 (Consistency of LABS-Grid) Fix M ≥ 2 and R ≥ 2. Let X ,...,X
1 n
follow the model of Section 4 of the main paper, and suppose Assumptions S4.1 and S4.2
ˆ
hold for g with these M and R. Let T be the set returned by LABS-Grid, Algorithm S1,
n
with the contrast of the main paper and threshold λ . Then the conclusion of Theorem 4.1
n
holds verbatim, with a constant C depending on g, σ, M and R.
Proof. As in Section S3.4: the initial call is on (0,n], which tracks the root (0,1) of
T (g) exactly and has V(0,1) = {1,...,N}, so Proposition S4.2 applies at the root. If
M,R
N = 0 then no window contains a kink and Lemma S4.1 gives T ˆ = ∅. □
n
S4.4 Remarks
Remark S4.1 (No condition on R) Assumptions S4.1 and S4.2 restrict M only, and
Theorem S4.1 holds for every R ≥ 2. The reason is that the re-test window is never
in the position that requires an assumption. In Case A it includes no live kink, and
Lemma S4.1 needs no hypothesis beyond the dichotomy; in Case B it includes exactly one,
and a window with one live kink has a unique and non-degenerate pooled maximizer, at
the kink, for every grid size. The look-ahead has already reduced the re-test to a single-
change-point problem, for which the conclusion holds at every grid size. In particular
R = 2 suffices, which is the formal counterpart of the observation in Section 3.2 of the
main paper that a single-interval evaluation should suffice at the re-test stage.
55

Remark S4.2 (The threshold does not depend on M) The same λ serves every
n
ˆ
M. This is because the event E of Lemma S2.3 controls |⟨ε,ψ ⟩| simultaneously over
n b
all O(n3) triples (s,e,b), which already includes every sub-interval any grid can produce;
enlarging the collection searched by a fixed factor
(cid:0)M(cid:1)
does not change the order of the
2
maximum. The observation in Section 3.2 of the main paper, that the null distribution of
the proposal statistic grows with M, concerns the sharpness of the constant in λ rather
n
than its order, and remains relevant in finite samples.
Remark S4.3 (What the grid changes) The grid does not weaken the conditions; it
changes the population recursion to which they are applied. A window carrying several
live kinks may have a sub-window that isolates one of them, and if the contrast on that
sub-window exceeds the contrast on every other, then c (α,β) is a kink where c(α,β)
M
was not. In the language of Proposition S4.1 this moves a node from Case A to Case B:
the split is made at a change-point rather than between change-points, and the look-ahead
recovers the change-point at the re-test rather than discarding a spurious estimate. This
may reduce the recursion depth. It also means that Assumptions S4.1 and S4.2 are specific
to M: they may hold for one M and fail for another, and neither implies Assumption 4.1
or Assumption 4.2.
Remark S4.4 (Recovering Theorem 4.1) When M = 2 the only admissible pair is
(1,2), so D
¯(2)
= |D
¯
|, c = c, T (g) = T (g) and G (g) consists of the window
αβ αβ 2 2,R 2,R
endpoints, so κ = κ and P∗ is a singleton with ι = 1. Assumptions S4.1 and S4.2 reduce
2
to Assumption 4.1 and Assumption 4.2, and Theorem S4.1 reduces to Theorem 4.1.
S5 Consistency under strengthened SIC selection
Theorem4.1andTheoremS4.1concernLABSrunatasinglethresholdinarangethatde-
pends on unknown quantities. The procedure used in Section 5 of the main paper instead
computes a solution path over a grid of thresholds and selects from it by a strengthened
Schwarz criterion. This section shows that the selected model is consistent, with the same
rate.
The argument has two parts. First, the path contains a candidate change-point set that
satisfiestheexact-countandlocalizationconclusionsofTheorem4.1. Second, thecriterion
does not prefer any other set on the path: a set that misplaces a change-point pays in
residual sum of squares, and a set with superfluous change-points pays in penalty. The
second comparison is what requires the exponent in the penalty to exceed one.
56

| S5.1 The             | procedure |     |     |         |           |     |         |         |     |     |
| -------------------- | --------- | --- | --- | ------- | --------- | --- | ------- | ------- | --- | --- |
| For T ⊂ {1,...,n−1}, |           | let |     |         |           |     |         |         |     |     |
|                      |           |     |     | (cid:8) |           |     |         | (cid:9) |     |     |
|                      |           | M(T | )   | := span | 1,t,(t−u) |     | : u ∈ T | .       |     |     |
+
This is the space of vectors obtained by restricting continuous piecewise-linear functions
with knots in T to the observation grid {1,...,n}. Here an affine function is one of
the form a + bt. The dimension is at most |T | + 2. If 1 ∈/ T , the displayed vectors
are linearly independent: their second differences identify the coefficients of the hinge
functions (t − u) separately, after which the constant and linear coefficients must also
+
vanish. If 1 ∈ T , then (t−1) = t−1 for every observed t, so this hinge vector already
+
lies in span{1,t} and does not add a dimension. For every u ≥ 2, by contrast, (t−u)
+
has a change of slope on the observation grid and is not affine on the whole grid. The
proof below uses only the upper bound dimM(T ) ≤ |T | + 2, in the union bound in
Lemma S5.2. Let P be orthogonal projection onto M(T ), and let
T
|     | (cid:13) |     | (cid:13)2 |     |     |     |     |     | (cid:0) | (cid:1) |
| --- | -------- | --- | --------- | --- | --- | --- | --- | --- | ------- | ------- |
RSS(T ) := (cid:13)(I −P )X(cid:13) , sSIC(T ) := nlog{RSS(T )/n}+ 2|T |+3 ξ ,
|     |     | T   |     |     |     |     |     |     |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with ξ := (logn)γ and γ > 1 fixed; Section 5 of the main paper takes γ = 1.01. Write
n
√
|     | (cid:0) |     | (cid:1) |     |     |     |     | (cid:8) |     | (cid:9) |
| --- | ------- | --- | ------- | --- | --- | --- | --- | ------- | --- | ------- |
σˆ := MAD ∆2X/ 6 , λ := aσˆ(2logn)1/2, Π := T ˆ (λ ) : a ∈ A ,
|     |     |     |     | a   |     |     | n   |     | a   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where T ˆ (λ) is the output of LABS, or of LABS-Grid, at threshold λ, and A is the grid
n
| of multipliers. | The selected |     | set | is           |     |        |     |     |     |     |
| --------------- | ------------ | --- | --- | ------------ | --- | ------ | --- | --- | --- | --- |
|                 |              |     | T   | ˆsSIC := arg | min | sSIC(T | ),  |     |     |     |
T∈Πn
ties being broken by taking the smallest |T | and then the smallest set in lexicographic
order.
| For a candidate | set write |     |           |     |     |         |     |     |     |         |
| --------------- | --------- | --- | --------- | --- | --- | ------- | --- | --- | --- | ------- |
|                 | (cid:13)  |     | (cid:13)2 |     |     | (cid:8) |     |     |     | (cid:9) |
b(T ) := (cid:13)(I −P )f(cid:13) , δ (T ) := min |τ −u| : u ∈ T ∪{0,n} ,
|     |     |     | T   | j   |     |     | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for the approximation error and the distance from the jth change-point to the nearest
knot.
| S5.2 Conditions |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In addition to Assumption 4.1 and Assumption 4.2, or to their grid counterparts, we
| require the | following. |     |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
57

Assumption S5.1 (Noise) ε ,...,ε are independent and identically distributed with
1 n
mean zero, variance σ2, and σ-sub-Gaussian, and σˆ/σ → 1 in probability. The two roles of
σ have to coincide here. Section 4 of the main paper assumes a sub-Gaussian parameter σ,
and the threshold band of Remark S3.2 is expressed in terms of that parameter, whereas σˆ
estimates the standard deviation; if the two differed by a factor K > 1, the band would have
(1+η)Kσ(8logn)1/2
to start at and the constants below would depend on K. Assuming
both equal to σ, which holds for Gaussian errors, avoids carrying K through the argument.
Assumption S5.2 (Threshold grid) Suppose first that N ≥ 1. There are fixed η > 0
|     | 1Λ  | 1ΛM,R) |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- |
and ς ∈ (0, ), or ς ∈ (0, in the grid case, such that, with probability tending
|         | 2 det      | 2         | det           |        |               |     |
| ------- | ---------- | --------- | ------------- | ------ | ------------- | --- |
|         |            |           | η)σ(8logn)1/2 | ςn1/2, |               |     |
| to one, | A contains | a value a | with (1 +     | ≤ λ ≤  | that is, with | λ   |
|         | n          |           |               | a      |               | a   |
in the band of Remark S3.2. If N = 0, in which case Λ is a minimum over an empty
det
set and is undefined, there is a fixed η > 0 such that, with probability tending to one,
A contains a value a with λ ≥ (1 +η)σ(8logn)1/2, at which LABS returns the empty
| n   |     | a   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
set. The upper restriction is important as a threshold of order Ln1/2 with L above the
population contrast at the root satisfies the lower bound but causes LABS to return the
empty set, so without it the path need not contain a consistent model at all. The factor
1+η gives a fixed multiplicative gap above the noise bound, meaning that η is positive and
does not depend on n. This gap is needed because λ is random through σˆ; by Remark S3.2
a
the conclusion of Theorem 4.1 then holds simultaneously for all thresholds in that band,
| so it may | be applied | at the random | λ . |     |     |     |
| --------- | ---------- | ------------- | --- | --- | --- | --- |
a
Assumption S5.3 (Bounded path) max |T | ≤ K for a sequence with K logn =
|     |     |     | T∈Πn | n   | n   |     |
| --- | --- | --- | ---- | --- | --- | --- |
o(n).
Assumption S5.1 strengthens the noise condition of Section 4 of the main paper from
independent to independent and identically distributed with a finite variance, which is
what makes σˆ and ∥ε∥2 well-behaved; the convergence of σˆ holds for the median absolute
deviation with the Gaussian consistency factor when the errors are Gaussian, the N
contaminated second differences at the kinks being of size O(n−1) and finite in number.
AssumptionS5.2isdiscussedinRemarkS5.2. AssumptionS5.3excludescandidatemodels
whose dimension is comparable to n, for which nlog{RSS(T )/n} is not informative. It
is satisfied by any implementation that caps the number of estimated change-points, and
it holds automatically for those λ that exceed σ(8logn)1/2, for which Theorem 4.1 gives
a
| |T ˆ (λ )| | = N. |     |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- | --- |
a
| S5.3 | Two lemmas |     |     |     |     |     |
| ---- | ---------- | --- | --- | --- | --- | --- |
Lemma S5.1 (Approximation error) Let T ⊂ {1,...,n − 1} and write δ = δ (T ).
|     |     |     |     |     | j   | j   |
| --- | --- | --- | --- | --- | --- | --- |
Then:
58

¯2n−1(cid:80)N
| (a) | b(T | ) ≤ Nd |     | δ2; |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
j=1
(b) if ϱ < δ /2, so that the interval I := (τ − ⌊ϱn⌋, τ + ⌊ϱn⌋], whose endpoints
|     |     | min |     |     |     | j   | j   |     | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
are integers, contains no change-point other than τ , and if I contains exactly one
|     |     |     |     |     |     |     |     | j   |     | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
d2ϱδ2/n,
point of T ∪{0,n} and δ ≤ ϱn/2, then b(T ) ≥ 1c2c with c and c the
|     |           |     |        |      | j         |     |     | 8 ℓ | 0   | j   | 0   | ℓ   |
| --- | --------- | --- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     | constants | of  | Lemmas | S2.4 | and S2.2; |     |     |     |     |     |     |     |
1c2d2ϱ3n.
(c) if ϱ < δ /2 and I contains no point of T ∪{0,n}, then b(T ) ≥
|     |     | min |     | j   |     |     |     |     |     |     | 8 ℓ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. (a) Let τˆ ∈ T ∪ {0,n} attain δ and take g ∈ M(T ) with the same affine
|     |     | j   |     |     |     | j   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
part as f and knot coefficients +∆ at τˆ, other coefficients zero. Then h := f − g =
|     |     |     |     |     | j   | j   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80) ∆ {(t − τ ) − (t − τˆ ) } up to an affine function, and each bracket is bounded in
|     | j   | j + |     | j + |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
|     |     |     |     |     | (cid:80) |     |     |     |     |     | ¯   |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
modulus by δ , so ∥h∥ ≤ |∆ |δ and, by Cauchy–Schwarz and |∆ | ≤ d/n from
|         |     | j             | ∞      |     | j j     | j   |          |     |               |     | j   |     |
| ------- | --- | ------------- | ------ | --- | ------- | --- | -------- | --- | ------------- | --- | --- | --- |
|         |     |               |        |     | ∥h∥2    |     | (cid:80) | )2  | ¯2n−1(cid:80) |     | δ2. |     |
| Section |     | 4 of the main | paper, |     | b(T ) ≤ | ≤   | n( |∆    | |δ  | ≤ Nd          |     |     |     |
|         |     |               |        |     |         |     | j        | j j |               |     | j j |     |
(b) Let τˆ be the unique point of T ∪ {0,n} in I . To lower-bound b(T ), restrict the
|     |     | j   |     |     |     |     | j   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
squared approximation error to the coordinates in I . The signal f has τ as its only
|     |     |     |     |     |     |     |     | j   |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
kink there because ϱ < δ /2. Every function in M(T ), when restricted to I , has
|     |     |     |     | min |     |     |     |     |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
τˆ as its only possible knot, since knots outside I contribute only an affine function
| j   |     |     |     |     |     |      |         | j   |      |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------- | --- | ---- | --- | --- | --- |
|     |     |     |     |     |     | |2∥ψ | I j∥2{1 |     | )2}, |     | ψIj |     |
on this interval. Therefore b(T ) ≥ |∆ τ − ρ(τ ,τˆ where and ρ are
|     |     |     |     |     |     | j   | j   |     | j j |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
formed on I . Writing L := ⌊ϱn⌋, so that τ is at distance L from each end of I ,
|       |     | j          |      |     |      |           | j    |     |      |     |            | j     |
| ----- | --- | ---------- | ---- | --- | ---- | --------- | ---- | --- | ---- | --- | ---------- | ----- |
|       |     |            | Ij∥2 |     | c2L3 | c2(ϱn)3/8 |      |     |      |     |            |       |
| Lemma |     | S2.2 gives | ∥ψ   | ≥   | ≥    |           | once | ϱn  | ≥ 2, | and | Lemma S2.4 | gives |
|       |     |            | τj   |     | ℓ    | ℓ         |      |     |      |     |            |       |
Ij∥2
1−ρ2 ≥ 1−ρ ≥ c {δ /(ϱn)}2. Multiplying the lower bounds for ∥ψ and 1−ρ2, and
|      |       |        | 0 j        |     |            |     |     |     |     | τj  |     |     |
| ---- | ----- | ------ | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| then | using | |∆ | ≥ | d/n, gives |     | the bound. |     |     |     |     |     |     |     |
j
(c) As in (b), but now f restricted to I is compared with affine functions only, so b(T ) ≥
j
Ij∥2
|∆ |2∥ψ ≥ c2d2n−2L3 ≥ c2d2ϱ3n/8. Here and in (b) the factors 1/8 and, in (b), 1/2
|     | j   | τj ℓ |     |     | ℓ   |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in the separation ratio δ /L ≤ 2δ /(ϱn) are the price of using integer endpoints; no rate
|     |     |     |     | j   | j   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
□
is affected.
Note the two-sided form of Lemma S5.1: part (a) says that a set localized to within η
has approximation error at most of order η2/n, so a set localized to within r¯ has error
n
O(logn); part(b)saysthatthisistherightorder, sothaterrorO(logn)forceslocalization
O(r¯ ).
n
Lemma S5.2 (Uniform control of projected noise) Under Assumption S5.1, ε /σ
t
is 1-sub-Gaussian. The Hanson–Wright inequality (Rudelson and Vershynin, 2013, The-
orem 1.1) therefore has an absolute positive constant that is independent of n, of the
projection and of the error distribution within this normalized sub-Gaussian class. Con-
sequently, there is a universal constant C and an event F with P(F ) → 1 on which
|     |     |           |            |     |             | P   |          |     | n       | n      |     |     |
| --- | --- | --------- | ---------- | --- | ----------- | --- | -------- | --- | ------- | ------ | --- | --- |
|     |     | (cid:13)  | (cid:13) 2 |     |             |     |          |     |         |        |     |     |
|     |     | (cid:13)P | ε (cid:13) | ≤ C | σ2(d+2)logn |     | whenever |     | |S| = d | ≤ n/2, |     |     |
|     |     |           | S          |     | P           |     |          |     |         |        |     |     |
59

and
|     |     |     |     | (cid:12)     |              | (cid:12) |     |     |     |
| --- | --- | --- | --- | ------------ | ------------ | -------- | --- | --- | --- |
|     |     |     |     | (cid:12)∥ε∥2 | −nσ2(cid:12) | ≤ 1nσ2.  |     |     |     |
|     |     |     |     | (cid:12)     |              | (cid:12) |     |     |     |
2
Proof. For fixed S, ∥P ε∥2 is a quadratic form in ε whose matrix has rank at most d+2
S
andoperatornormone, sotheHanson–WrightinequalitygivesP(∥P ε∥2 > σ2(d+2)+t) ≤
S
2exp[−cmin{t2/{σ4(d+2)}, t/σ2}]. Taking t = C σ2(d+2)logn with C large enough
|     |     |     |     |     |     | P   | P   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0)n(cid:1)
makes this at most 2exp{−3(d+2)logn}, and there are at most ≤ exp(dlogn) sets
(cid:80) d
of size d, so the first event fails with probability at most 2 exp{−(2d+6)logn} ≤
d≤n/2
4n−6. The second is the law of large numbers for ε2, whose mean is σ2 and whose variance
t
| is finite | under | Assumption |     | S5.1. |     |     |     |     | □   |
| --------- | ----- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
| S5.4      | The   | theorem    |     |       |     |     |     |     |     |
Theorem S5.1 (Consistency of sSIC-selected LABS) Let the model and assump-
tions of Theorem 4.1 hold, together with Assumptions S5.1 to S5.3, and let γ > 1. Write
N ˆ = |T ˆsSIC| and let τˆ < ··· < τˆ be the selected change-points. If N ≥ 1 there is
|     |              |          | (1) |          | (Nˆ)       |                           |          |     |     |
| --- | ------------ | -------- | --- | -------- | ---------- | ------------------------- | -------- | --- | --- |
| C < | ∞, depending | only     | on  | g, σ and | γ, such    | that                      |          |     |     |
|     |              | (cid:16) |     |          |            |                           | (cid:17) |     |     |
|     |              |          |     |          | (cid:12)   | (cid:12)                  |          |     |     |
|     |              | P N ˆ    | = N | and max  | (cid:12)τˆ | −τ (cid:12) ≤ C(nlogn)1/2 | −→ 1,    |     |     |
(j) j
1≤j≤N
ˆ
and if N = 0 then P(N = 0) → 1. The same holds for LABS-Grid with fixed M,R ≥ 2,
with Theorem 4.1 replaced by Theorem S4.1 and its assumptions in Assumption S5.2.
Proof. Let G be the intersection of three events. The first is the uniform contrast-noise
n
event E from Lemma S2.3. The second is the projected-noise event F from Lemma S5.2.
|     | n   |     |     |     |     |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The third is the threshold-grid event asserted in Assumption S5.2. Work on G , whose
n
probabilitytendstoone. WriteT = {τ ,...,τ },q = |T |andΦ2 := C σ2(q+N+2)logn,
|     |     |     |     | 0   | 1   | N   | q P |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and recall r¯ = (nlogn)1/2. Constants c ,c ,... depend only on g and σ.
|     |     | n   |     |     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Step 1: the path contains a good set. By Assumption S5.2 there is a ∈ A with λ
|     |     |     |     |     |     |     |     | n   | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
admissible, so Theorem 4.1 applies at that threshold and T ⋆ := T ˆ (λ ) ∈ Π satisfies
a n
¯2C2logn
|T ⋆| = N and δ (T ⋆) ≤ C r¯ for every j. Lemma S5.1(a) gives b(T ⋆) ≤ N2d =:
|     |     | j   | ⋆   | n   |     |     |     | ⋆   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c logn.
1
Step 2: an upper bound for RSS(T ⋆). Put A⋆ = T ⋆ ∪ T , so that f ∈ M(A⋆) and
0
(I − P )f ∈ M(A⋆). Hence |⟨(I − P )f,ε⟩| ≤ b(T ⋆)1/2∥P ε∥, and |A⋆| ≤ 2N, so
|       | T⋆   |          |     |           | T⋆       |           | A⋆  |     |     |
| ----- | ---- | -------- | --- | --------- | -------- | --------- | --- | --- | --- |
| Lemma | S5.2 | gives ∥P | ε∥2 | ≤ C σ2(2N | +2)logn. | Therefore |     |     |     |
|       |      |          | A⋆  | P         |          |           |     |     |     |
RSS(T ⋆) ≤ ∥ε∥2 +b(T ⋆)+2b(T ⋆)1/2∥P ε∥ ≤ ∥ε∥2 +c logn. (S20)
|     |     |     |     |     |     | A⋆  | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
60

Step 3: a lower bound for RSS(T ). Let T ∈ Π and A = T ∪T . Since M(T ) ⊆ M(A)
|     |       |     |     |     |     |     | n   |     |     | 0   |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| and | P f = | f,  |     |     |     |     |     |     |     |     |     |     |     |
A
|     |     |     |     | (cid:13) |     | (cid:13) |     |     |     | (cid:16) |     |     | (cid:17)2 |
| --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | -------- | --- | --- | --------- |
RSS(T ) = RSS(A)+ (cid:13)(P −P )X 2 ≥ ∥ε∥2 −∥P ε∥2 + b(T )1/2 −∥P ε∥ ,
|     |     |     |     | A   | T   | (cid:13) |     |     | A   |     |     | A   |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
+
using (P −P )X = (I−P )f+(P −P )ε and RSS(A) = ∥(I−P )ε∥2. By Lemma S5.2
|     | A          | T     |       | T   | A    | T    |     |              |         | A        |     |     |       |
| --- | ---------- | ----- | ----- | --- | ---- | ---- | --- | ------------ | ------- | -------- | --- | --- | ----- |
|     |            |       |       | ε∥2 | Φ2   | σ2(K |     |              |         |          |     |     |       |
| and | Assumption | S5.3, | ∥P    | ≤   | ≤    | C    |     | +N           | +2)logn | = o(n),  | so  |     |       |
|     |            |       |       | A   | q    | P    | n   |              |         |          |     |     |       |
|     |            |       |       |     | ∥ε∥2 | −Φ2  |     | (cid:0) )1/2 |         | (cid:1)2 |     |     |       |
|     |            |       | RSS(T | )   | ≥    |      | +   | b(T          | −Φ      | .        |     |     | (S21) |
|     |            |       |       |     |      |      | q   |              |         | q +      |     |     |       |
Step 4: sets with large approximation error. Suppose b(T ) ≥ ϵn for a fixed ϵ > 0. By
(S21) and Φ2 = o(n), RSS(T ) ≥ ∥ε∥2 + 1ϵn for n large, while (S20) bounds RSS(T ⋆) by
q
2
| ∥ε∥2 | +c logn. | Since | ∥ε∥2 | ≤ 3nσ2 | on       | F ,    |     |              |     |          |     |          |     |
| ---- | -------- | ----- | ---- | ------ | -------- | ------ | --- | ------------ | --- | -------- | --- | -------- | --- |
|      | 2        |       |      | 2      |          | n      |     |              |     |          |     |          |     |
|      |          | RSS(T | )    |        | (cid:16) | ϵn/2−c |     | logn(cid:17) |     | (cid:16) | ϵ   | (cid:17) |     |
2
|     |     | nlog  |     | ≥ nlog |     | 1+   |     |      | ≥   | nlog | 1+  |     |     |
| --- | --- | ----- | --- | ------ | --- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
|     |     | RSS(T | ⋆)  |        |     | ∥ε∥2 | +c  | logn |     |      | 5σ2 |     |     |
2
2nσ2
for n large, the denominator being at most on F , which exceeds 2Nξ for n large,
|     |     |     |     |     |     |     |     |     | n   |     |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
⋆)
and the penalty difference is at least −2Nξ . So sSIC(T ) > sSIC(T and T is not
n
selected.
In particular no T with q < N is selected: by the pigeonhole principle some τ has no
j
point of T ∪{0,n} within δ n/3, since the N +1 gaps between consecutive elements of
min
T ∪{0,n} have length at least δ n, so Lemma S5.1(c) gives b(T ) ≥ c n.
| 0   |     |     |     |     | min |     |     |     |     |     | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Step 5: sets with small approximation error. Suppose b(T ) < ϵn. Then by (S20), (S21)
and Lemma S5.2, both RSS(T ) and RSS(T ⋆) lie between 1nσ2 and 2nσ2 for n large and
3
ϵ small. Writing D := RSS(T )−RSS(T ⋆) and using logx ≥ 1−1/x,
|     |          | RSS(T      | )   |       | nD           | 3D  |          |     |          | D   |      |      |       |
| --- | -------- | ---------- | --- | ----- | ------------ | --- | -------- | --- | -------- | --- | ---- | ---- | ----- |
|     | nlog     |            |     | ≥     |              | ≥   | if       | D ≤ | 0,       | ≥   | if D | > 0, |       |
|     |          | RSS(T      | ⋆)  | RSS(T | )            |     | σ2       |     |          | 2σ2 |      |      |       |
| and | by (S20) | and (S21), |     |       |              |     |          |     |          |     |      |      |       |
|     |          |            |     |       | (cid:0) )1/2 |     | (cid:1)2 | −Φ2 |          |     |      |      |       |
|     |          |            | D   | ≥     | b(T          | −Φ  |          |     | −c logn. |     |      |      | (S22) |
|     |          |            |     |       |              |     | q +      | q   | 2        |     |      |      |       |
Step 6: no over-fitting. Supposeq > N andb(T ) < ϵn. IfD > 0thenthelogarithmicterm
is non-negative by the second branch of Step 5, while the penalty difference 2(q −N)ξ
n
is strictly positive, and T is not selected. Assume therefore D ≤ 0; dropping the non-
| negative | term   | in (S22) | and | using | the | first   | branch   | of Step | 5,   |        |      |     |     |
| -------- | ------ | -------- | --- | ----- | --- | ------- | -------- | ------- | ---- | ------ | ---- | --- | --- |
|          |        |          |     |       | 3   | (cid:0) |          | (cid:1) |      |        |      |     |     |
|          | sSIC(T | )−sSIC(T |     | ⋆) ≥  | −   | Φ2 +c   | logn     | +2(q    | −N)ξ |        |      |     |     |
|          |        |          |     |       |     |         | 2        |         |      | n      |      |     |     |
|          |        |          |     |       | σ2  | q       |          |         |      |        |      |     |     |
|          |        |          |     |       |     |         |          |         | 3c   | logn   |      |     |     |
|          |        |          |     | ≥     | −3C | (q +N   | +2)logn− |         |      | 2 +2(q | −N)ξ |     | .   |
|          |        |          |     |       |     | P       |          |         |      |        |      | n   |     |
σ2
61

Since q ≥ N + 1 gives q + N + 2 ≤ (2N + 3)(q − N), the right side is at least (q −
N){2ξ −3C (2N+3)logn−3c σ−2logn},whichispositivefornlargebecauseξ /logn =
|           | n   | P    |      | 2                |     |     |     |     |     |     | n   |
| --------- | --- | ---- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| (logn)γ−1 |     | → ∞. | So T | is not selected. |     |     |     |     |     |     |     |
Step 7: localization. By Steps 4 and 6 the selected set T ˆ := T ˆsSIC has |T ˆ | = N, which is
ˆ
the first assertion. Its penalty equals that of T ⋆, so sSIC(T ) ≤ sSIC(T ⋆) forces D ≤ 0 in
| Step | 5, and | (S22) | with      | q = N gives |          |         |          |     |           |     |     |
| ---- | ------ | ----- | --------- | ----------- | -------- | ------- | -------- | --- | --------- | --- | --- |
|      |        |       | (cid:0) ˆ | )1/2        | (cid:1)2 | Φ2      |          |     |           |     |     |
|      |        |       | b(T       | −Φ          | ≤        | +c      | logn,    |     |           |     |     |
|      |        |       |           |             | N +      | N       | 2        |     |           |     |     |
|      |        |       |           |             | ˆ        | (cid:0) | logn)1/2 |     | (cid:1)2  |     |     |
|      |        |       |           | b(T         | ) ≤      | 2Φ      | +(c      |     | ≤ c logn. |     |     |
|      |        |       |           |             |          | N       | 2        |     | 4         |     |     |
since Φ2 = C σ2(2N + 2)logn. Lemma S5.1(c), whose constant we write as c :=
|     | N   | P   |     |     |     |     |     |     |     |     | 5   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1c2d2, applied with any ϱ exceeding (c logn/(c n))1/3, then shows that every τ has a
| ℓ   |     |     |     |     |     | 4   | 5   |     |     |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8
point of T ˆ ∪{0,n} within Γ′ := C (n2logn)1/3 of it, where C > (c /c )1/3 is any fixed
|     |     |     |     |     | 6   |     |     |     | 6   | 4 5 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
constant. Since Γ′ = o(n) and the τ are δ n apart, the N points of T ˆ are in one-to-one
|     |     |     | n   |     | j   | min |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
correspondence with the τ , and each interval I = (τ −δ n/3, τ +δ n/3) contains
|         |     |          |       | j       |     |      | j     | j      | min j | min |     |
| ------- | --- | -------- | ----- | ------- | --- | ---- | ----- | ------ | ----- | --- | --- |
| exactly | one | of them. | Lemma | S5.1(b) |     | with | ϱ = δ | /3 now | gives |     |     |
min
|     |     |     |     | 1 c2c d2δ | δ   | (T ˆ )2/n | ≤ b(T | ˆ ) ≤ | c logn, |     |     |
| --- | --- | --- | --- | --------- | --- | --------- | ----- | ----- | ------- | --- | --- |
|     |     |     |     | 0         | min | j         |       |       | 4       |     |     |
24 ℓ
ˆ
so δ (T ) ≤ C(nlogn)1/2 for every j, which is the second assertion. If N = 0 then T ⋆ = ∅
j
by Theorem 4.1, b(T ) = 0 for every candidate, and Step 6 applies to every T with q ≥ 1,
so the empty set is selected. The statement for LABS-Grid is identical, Step 1 using
□
| Theorem |     | S4.1 in | place | of Theorem | 4.1. |     |     |     |     |     |     |
| ------- | --- | ------- | ----- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
| S5.5    |     | Remarks |       |            |      |     |     |     |     |     |     |
Remark S5.1 (Why the penalty exponent must exceed one) Step 6 is the only
place where γ > 1 is used, and it cannot be dispensed with there. Adding q −N superflu-
ous knots, chosen from n positions in a data-dependent way, reduces the residual sum of
squares by an amount that can be as large as a constant multiple of σ2(q −N)logn, the
(cid:0)n(cid:1)
logn arising from the possible choices in Lemma S5.2. The penalty must therefore
q
charge more than a constant multiple of logn for each knot. The ordinary Schwarz crite-
rion, with ξ = logn, charges exactly of that order and does not separate the two, whereas
n
|     | (logn)γ |     |     |     |     |     | (logn)γ−1 |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
ξ = with γ > 1 does, by the factor → ∞. This is the reason for the
n
| strengthened |     | form | used | in Section | 5   | of the | main paper. |     |     |     |     |
| ------------ | --- | ---- | ---- | ---------- | --- | ------ | ----------- | --- | --- | --- | --- |
Remark S5.2 (The range of the threshold grid) The lower restriction in Assump-
| tion | S5.2 | is  |     |     |               |     |                |     |     |     |     |
| ---- | ---- | --- | --- | --- | ------------- | --- | -------------- | --- | --- | --- | --- |
|      |      |     |     | λ = | aσˆ(2logn)1/2 |     | > σ(8logn)1/2. |     |     |     |     |
a
62

Since σˆ/σ → 1, this requires some a ∈ A with a > 2. The constant 8 comes from
n
the union bound over all O(n3) triples (s,e,b) in Lemma S2.3 and is not sharp: LABS
ˆ
evaluates the contrast on O(N) windows, not on all of them, as noted in Section 3.1 of
the main paper, so the maximum that λ must exceed is over a much smaller collection.
What Theorem S5.1 establishes is that the selection is consistent once the grid reaches
into the range in which the single-threshold theorem applies; identifying the smallest such
range for this contrast is a separate question, and the simulation evidence indicates that
the values used in practice are adequate.
Remark S5.3 (Rate and the required sample size) The rate is the same as in The-
orem 4.1: selection by the criterion does not alter its order. This is because the penalty
difference between two candidate sets of size N is zero, so the localization in Step 7 is
governed by the O(logn) terms alone and not by ξ . The value of n from which the proof
n
excludes over-fitting may nevertheless be large, because Step 6 requires (logn)γ−1 to exceed
a fixed multiple of 2N +3.
Remark S5.4 (What is not covered) Theorem S5.1 treats selection over a path gen-
erated by thresholding. It does not justify the use of σˆ inside the criterion itself, since
sSIC as defined does not involve σˆ; nor does it cover selection over a path generated in
any other way, or the choice of γ. Assumption S5.3 is a restriction on the path rather
than a property of the algorithm. A dimension bound of this order is needed in the proof of
Theorem S5.1 to keep the projected-noise term in Lemma S5.2 of order o(n). Section S5.6
imposes the bound by construction rather than assuming it, and in doing so also removes
Assumption S5.2.
S5.6 A solution path indexed by the number of change-points
Assumptions S5.2 and S5.3 are auxiliary: the first asks that the grid of multipliers reach
far enough, the second that the path not contain models whose dimension is comparable
to n. Both can be removed, without altering the algorithm, by generating the path over
thewholerangeofthresholdsratherthanoveragrid, indexingitbythenumberofchange-
points rather than by the threshold, and truncating it at a cap. This is the usual setting
for information criteria, which are ordinarily shown to be consistent over a finite collection
of candidate models of bounded size. The threshold then plays no role beyond that of an
internal device for generating candidates. Nothing in Sections S5.1 to S5.5 is changed;
what follows is an alternative route to the same conclusion.
63

Reduction to one candidate per model size
Lemma S5.3 (Reduction to one model per size) Let C be a finite collection of can-
didate sets and for each k let T ∈ argmin{RSS(T ) : T ∈ C,|T | = k} when that set is
k
non-empty. Then
minsSIC(T ) = minsSIC(T ),
k
T∈C k
and any minimizer of the right side is a minimizer of the left.
Proof. sSIC(T ) depends on T only through RSS(T ) and |T |, and is increasing in the
former for fixed |T |. □
Lemma S5.3 is elementary but it is what makes the reindexing legitimate: selecting by
sSIC over a collection of candidate sets is the same as retaining the best set of each size
and then choosing the size. No information is lost by presenting the path as a sequence
indexed by k.
The path
Definition S5.1 (Size-indexed path) Fix a cap K. Let
ΠK := (cid:8) T ˆ (λ) : λ ≥ 0 (cid:9) ∩ (cid:8) T : |T | ≤ K (cid:9) ,
n
ˆ
where T (λ) is the output of LABS, or of LABS-Grid with fixed M and R, at threshold λ.
Let K := {|T | : T ∈ ΠK}, let T be a minimum-RSS element of ΠK of size k, and set
n n k n
T
ˆK
:= arg min sSIC(T ).
k
k∈Kn
ˆ
Since T (λ) is piecewise constant in λ, with breakpoints among the finitely many contrast
values the algorithm computes, ΠK is a finite collection and T ˆK is well defined.
n
Computing the path
The proposal made at a node does not depend on the threshold. At a node with interval
ˆ
(s,e]theproposalbanditsvalueW aredeterminedbythedataonthatintervalalone, and
ˆ ˆ
the two children are (s,b] and (b,e]; the threshold decides only which nodes are reached
and what each returns. The intervals and proposals therefore form a single binary tree,
the proposal tree F, and the same tree serves every λ.
The look-ahead takes no part in building F. Were Algorithm 2 itself run at λ = 0,
every call would recurse to the shortest evaluable intervals, so each child would return
64

a point immediately adjacent to its parent’s proposal, each re-test interval would have
length O(1), and the re-test would carry no information; those of length less than three
would not admit the contrast at all. The construction below therefore separates the two,
building F from the proposals alone and applying the look-ahead afterwards, at each
threshold in turn, where the re-test intervals are the ones Algorithm 2 actually uses.
ˆ ˆ
1. Proposal tree. Starting from (0,n] and recursing on (s,b] and (b,e] whenever B ̸=
s,e
∅, record at each node its interval, its proposal and the proposal value. No threshold
is used and no re-test is performed. Nodes are expanded lazily, only as far as step 3
requires.
2. Output at a given λ. Evaluatebottom-uponF: out(v) = ∅ifW ≤ λ, andotherwise
v
the return of Algorithm 2 at v, formed from the children’s outputs L and R, with
s′, e′ and the re-test as there. This reproduces T ˆ (λ) exactly. The look-ahead enters
here and only here, and since (s′,e′] depends on λ through L and R, the re-test
contrasts are recomputed at each threshold.
3. Threshold sweep. Here a sweep means evaluating the output as λ decreases through
its breakpoints down to zero. Record the output after each pass and expand F as
deeper nodes become active. Early stopping is discussed below.
4. Selection. Retain, for each k ≤ K, the recorded set of size k with the smallest RSS,
and minimize sSIC over k.
ˆ
The breakpoints of λ (cid:55)→ T (λ) lie among the proposal values and the re-test values, and
may be assembled exactly, bottom-up: those at a node are the breakpoints of its two
children together with W and one re-test value for each of the resulting sub-intervals of
v
λ. In an implementation it is simpler to sweep a grid of thresholds, refining it until no
new set of size at most K appears.
Step 1 expands only the part of F reached by the smallest threshold used, so its cost is
that of one run of LABS at that threshold. Each pass in step 2 costs O(nlogn) under
balanced splits, the re-test intervals at a given depth being disjoint, so P passes cost
O(Pnlogn) typically and O(Pn2) in the worst case, matching the corresponding costs
for LABS itself. The tree must be expanded far enough for the thresholds being swept.
Truncating F by depth is not a substitute for truncating the path by size.
Stopping the sweep once the output size first exceeds K as λ decreases is a heuristic rule.
ˆ
It would be valid if the map λ (cid:55)→ |T (λ)| were non-increasing, equivalently if the output
size could only increase as the threshold is lowered. This monotonicity can fail when the
two children return sets of equal size but in different positions: the re-test interval can
then differ between two thresholds, and the parent estimate may be retained at the higher
threshold but discarded at the lower one. In that case early stopping can omit members of
65

ΠK occurring at smaller λ. Sweeping to λ = 0 is always valid and is what Definition S5.1
n
and Theorem S5.2 require. If the stated monotonicity does hold, once the output size
exceeds K it cannot later return to K or below, so early stopping omits no member of
ΠK.
n
Consistency
Theorem S5.2 (sSIC over the size-indexed path) Let the model and assumptions
of Theorem 4.1 hold, together with Assumption S5.1, and let γ > 1. Let K = K → ∞
n
with K logn = o(n). Then T
ˆKn
of Definition S5.1 satisfies the conclusion of Theo-
n
rem S5.1. No analogue of Assumption S5.2 or Assumption S5.3 is required. The same
holds for LABS-Grid with fixed M,R ≥ 2, with Theorem 4.1 replaced by Theorem S4.1.
Proof. Assumption S5.3 holds with the stated K by construction, since every element of
n
ΠKn has at most K points.
n n
For Step 1 of the proof of Theorem S5.1, let λ be any threshold in the range admitted by
Theorem 4.1, which is non-empty. Then T ⋆ := T ˆ (λ) has |T ⋆| = N and δ (T ⋆) ≤ C r¯ for
j ⋆ n
every j, on an event of probability tending to one. Since K → ∞ we have N ≤ K for
n n
n large, so T ⋆ ∈ ΠKn; no condition on a grid of multipliers is needed, because the path is
n
generated over all λ ≥ 0. By Lemma S5.3,
sSIC (cid:0) T ˆKn (cid:1) ≤ sSIC(T ) ≤ sSIC(T ⋆).
N
Steps 2 to 7 of the proof of Theorem S5.1 are unchanged: they compare an arbitrary
candidate with T ⋆, and use only that the selected set has sSIC no larger than that of T ⋆
and that every candidate has at most K points. □
n
Remarks
Remark S5.5 (Choice of the cap) The conditions K → ∞ and K logn = o(n)
n n
make the cap asymptotically non-binding while requiring K = o(n/logn). For example,
n
K = ⌈n/(logn)2⌉ is admissible. In practice a fixed K exceeding any plausible number of
n
change-points is what is used, and Theorem S5.2 then holds for every signal with N ≤ K.
This is the same convention under which the Schwarz criterion is ordinarily shown to be
consistent, namely over a finite collection of models of bounded size.
Remark S5.6 (What is gained, and what is lost) Relative to Theorem S5.1, both
auxiliary conditions are removed: Assumption S5.2 because the threshold sweep covers
every threshold, so the admissible range of Theorem 4.1 is reached by construction, and
Assumption S5.3 because the cap is imposed rather than assumed. What is not removed
66

is the requirement that the admissible range be non-empty, which is Assumption 4.1 and
Assumption 4.2 together with Lemma S2.3; the threshold sweep locates a suitable threshold
without knowing where it is, but it does not create one. Its computational cost is a factor
P on the running time, in place of the |A | runs of the procedure of Section S5.1.
n
S6 Connections with other look-ahead methods
ThissectionexpandsonthebriefdiscussionintheIntroductionofthemainpaper,givinga
fuller account of the connections between the look-ahead mechanism in LABS and related
ideas in other areas of algorithm design.
S6.1 Constraint satisfaction and SAT solvers
In constraint satisfaction problems (CSPs), a backtracking algorithm assigns values to
variables one at a time, recursing when an assignment is made and backtracking when a
dead-end is reached. Techniques for improving backtracking algorithms are traditionally
classified into two categories (Kondrak and van Beek, 1997; Dechter, 2003):
• Look-ahead schemes attempt to foresee the effects of the current assignment on
future, not yet assigned, variables. The simplest look-ahead technique is forward
checking, which removes from the domains of unassigned variables any values that
would be inconsistent with the current partial assignment. More sophisticated tech-
niques such as maintaining arc consistency propagate constraints more extensively,
potentially detecting dead-ends earlier. A prominent special case is the Boolean sat-
isfiability problem (SAT), where look-ahead solvers (Heule and van Maaren, 2009)
tentatively propagate the consequences of candidate variable assignments, detecting
unit propagations and failures, before committing to a branching decision.
• Look-backschemesanalyzedead-endswhentheyoccurtoextractusefulinformation.
The simplest look-back is chronological backtracking; more sophisticated techniques
such as conflict-directed backjumping identify the variables responsible for the fail-
ure and backtrack directly to them, skipping irrelevant intermediate variables.
The distinction drawn in this literature is that look-ahead uses information about future
parts of the search to improve current decisions, while look-back uses information about
pastfailurestoimprovebacktrackingdecisions. Empiricalstudieshavefoundthatstronger
look-ahead can reduce the benefit of look-back techniques (Kondrak and van Beek, 1997).
LABS employs a mechanism with features of both. Like look-ahead, it uses information
from child subproblems to refine decisions at the parent level: the child recursions can
67

be viewed as exploring future parts of the search tree, and the change-points they detect
provide information that improves the parent’s decision. Like look-back, it uses informa-
tion gathered after an initial decision, in the proposal phase, to revise that decision: the
refinement phase re-evaluates the parent change-point in the light of what was discovered
in the children.
There are also differences. In CSP and SAT look-ahead, information flows from the
current assignment to future variables through constraint propagation; the algorithm does
not actually recurse into future subproblems. In LABS, by contrast, we do recurse into
the child subproblems and use the actual results of those recursions, not just propagated
constraints, to refine the parent.
The connection to CSP also suggests a broader perspective: LABS can be viewed as a
form of intelligent backtracking for the change-point detection problem. Just as conflict-
directed backjumping in CSPs avoids exploring irrelevant parts of the search tree by iden-
tifying culprit variables, LABS avoids detecting spurious change-points by using child
information to identify narrower, more relevant intervals. The recursive structure han-
dles the bookkeeping automatically, much as the call stack in a recursive backtracking
algorithm handles the state management for backjumping.
S6.2 Decision tree induction
In the decision tree literature the connection to LABS is particularly direct. Standard
CART (Breiman et al., 1984) selects splits greedily: at each node, the best split is chosen
without considering what splits will follow in the child nodes. Murthy and Salzberg
(1995) study what happens when the algorithm instead looks one or more levels ahead,
tentatively making a split, building the child trees, and using the quality of the resulting
subtreetoevaluatetheparentsplit. Theyfindthatlook-aheadcandegradeperformancein
classification trees, a phenomenon they term pathology, and characterize conditions under
which it helps and under which it hurts. Esmeir and Markovitch (2007) develop this idea
further with anytime algorithms that invest varying amounts of look-ahead depending on
the available computation time.
The structural parallel with LABS is that in both settings a recursive partitioning algo-
rithm tentatively makes a split, or proposes a change-point, recurses into the children, and
uses the results to refine or validate the parent decision. A difference is that in tree look-
ahead the purpose is to choose a better split variable or threshold from scratch, whereas in
LABS the child recursions serve to narrow the interval on which the parent change-point
is re-evaluated, exploiting the specific geometry of the change-point detection problem.
68

S6.3 Numerical linear algebra
In numerical linear algebra, Parlett and Taylor (1985) propose a look-ahead modification
of the Lanczos algorithm for unsymmetric matrices, in which the procedure tentatively
explores further Krylov vectors before committing to a basis selection, thereby circum-
venting potential breakdowns. The look-ahead similarly involves tentative exploration
before commitment, but the structure being explored, namely Krylov subspaces, and the
purpose, namely avoiding numerical breakdown, are different from ours.
S6.4 Bayesian sequential analysis
In Bayesian sequential analysis, the term look-ahead refers to procedures that, at each
stage of sequential sampling, evaluate whether to stop collecting data or to continue by
examining the expected Bayes risk a fixed number of steps into the future; see Berger
(1985), Section 7.4.6. Our use of the term is unrelated to this sequential-sampling con-
text: in LABS, looking ahead refers to examining the results of deeper recursion before
confirming a candidate change-point, not to deciding when to stop gathering observations.
S6.5 Further research directions
Several questions remain open. First, one could seek sufficient conditions on the signal
for Assumption 4.1 and Assumption 4.2, or a formulation that does not require them.
The case in which N grows with n also requires separate analysis because the population
recursion is then no longer a fixed finite object. Second, LABS could be extended to other
signal models, including piecewise-polynomial signals of higher degree and signals with
both level and slope changes. Third, it would be useful to determine the smallest range
of thresholds for which a solution path computed on a fixed grid is guaranteed to contain
a consistent model, and to develop more efficient path-construction algorithms. Finally,
further work could establish conditions under which increasing M makes the assumptions
of Section S4.2 easier to satisfy and study how a suitable finite-sample threshold depends
on M. The present consistency result does not address either question.
S6.6 Summary
The strategy of full recursion followed by refinement is what distinguishes LABS among
these uses of look-ahead. Rather than propagating constraints or information forward, we
solve the child subproblems completely and then use the solutions to define a narrower
interval for re-evaluating the parent. This is possible because the child recursions are
computationally cheap, taking at most as long as the parent, and because the structure
69

of the change-point problem allows the child solutions to inform the parent refinement
directly.
References
A.AnastasiouandP.Fryzlewicz. Detectingmultiplegeneralizedchange-pointsbyisolating
| single ones. | Metrika, | 85:141–174, |     | 2022. |     |
| ------------ | -------- | ----------- | --- | ----- | --- |
A. Anastasiou, Y. Chen, H. Cho, and P. Fryzlewicz. breakfast: Methods for Fast
Multiple Change-Point/Break-Point Detection and Estimation, 2026. URL https:
//CRAN.R-project.org/package=breakfast. R package version 2.6.
J. Bai. Estimating multiple breaks one at a time. Econometric Theory, 13:315–352, 1997.
R. Baranowski, Y. Chen, and P. Fryzlewicz. Narrowest-over-threshold detection of mul-
tiple change-points and change-point-like features. Journal of the Royal Statistical
| Society, | Series B, | 81:649–672, |     | 2019. |     |
| -------- | --------- | ----------- | --- | ----- | --- |
J. O. Berger. Statistical Decision Theory and Bayesian Analysis. Springer, New York,
| 2nd edition, | 1985.  |          |         |           |                |
| ------------ | ------ | -------- | ------- | --------- | -------------- |
| L. Breiman.  | Random | forests. | Machine | Learning, | 45:5–32, 2001. |
L. Breiman, J. H. Friedman, C. J. Stone, and R. A. Olshen. Classification and Regression
| Trees. | Wadsworth, | Belmont, | CA, | 1984. |     |
| ------ | ---------- | -------- | --- | ----- | --- |
B. Brodsky and B. Darkhovsky. Nonparametric Methods in Change Point Problems, vol-
ume 243 of Mathematics and Its Applications. Kluwer Academic Publishers, Dordrecht,
1993.
K.-L. Chang, M. G. Schultz, G. Koren, and N. Selke. Guidance note on best statistical
practices for TOAR analyses. arXiv preprint arXiv:2304.14236, 2023.
K.-M. Chen, A. Cohen, and H. Sackrowitz. Consistent multiple testing for change points.
| Journal | of Multivariate |     | Analysis, | 102:1339–1343, | 2011. |
| ------- | --------------- | --- | --------- | -------------- | ----- |
T. Chen and C. Guestrin. XGBoost: A scalable tree boosting system. In Proceedings of
the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data
| Mining, | pages 785–794, |     | 2016. |     |     |
| ------- | -------------- | --- | ----- | --- | --- |
H.ChoandP.Fryzlewicz. Multiscaleandmultileveltechniqueforconsistentsegmentation
of nonstationary time series. Statistica Sinica, 22:207–229, 2012.
R. Dechter. Constraint Processing. Morgan Kaufmann, San Francisco, CA, 2003.
70

L. Do, D. Do, K. J. Cook, and S. A. McKinley. Change-in-velocity detection for multidi-
| mensional | data. arXiv | preprint arXiv:2510.27150, |     | 2025. |
| --------- | ----------- | -------------------------- | --- | ----- |
S. Esmeir and S. Markovitch. Anytime learning of decision trees. Journal of Machine
| Learning | Research, | 8:891–933, 2007. |     |     |
| -------- | --------- | ---------------- | --- | --- |
P. Fearnhead and D. Grose. cpop: Detecting changes in piecewise-linear signals. Journal
of Statistical Software, 109(7):1–30, 2024. doi: 10.18637/jss.v109.i07.
J. H. Friedman. Greedy function approximation: a gradient boosting machine. Annals of
| Statistics, | 29:1189–1232, | 2001. |     |     |
| ----------- | ------------- | ----- | --- | --- |
P.Fryzlewicz. UnbalancedHaartechniquefornonparametricfunctionestimation. Journal
| of the American | Statistical | Association, | 102:1318–1327, | 2007. |
| --------------- | ----------- | ------------ | -------------- | ----- |
P. Fryzlewicz. Wild binary segmentation for multiple change-point detection. Annals of
| Statistics, | 42:2243–2281, | 2014. |     |     |
| ----------- | ------------- | ----- | --- | --- |
P. Fryzlewicz and S. Subba Rao. Multiple-change-point detection for auto-regressive
conditional heteroscedastic processes. Journal of the Royal Statistical Society, Series
| B, 76:903–924, | 2014. |     |     |     |
| -------------- | ----- | --- | --- | --- |
M. J. H. Heule and H. van Maaren. Look-ahead based SAT solvers. In A. Biere, M. Heule,
H. van Maaren, and T. Walsh, editors, Handbook of Satisfiability, pages 155–184. IOS
| Press, | Amsterdam, | 2009. |     |     |
| ------ | ---------- | ----- | --- | --- |
A. Hosseinzadeh, L. Khoshnevisan, M. Pirani, S. Chenouri, and A. Khajepour. An ef-
ficient continual learning framework for multivariate time series prediction tasks with
application to vehicle state estimation. arXiv preprint arXiv:2503.01669, 2025.
T. Hothorn, K. Hornik, and A. Zeileis. Unbiased recursive partitioning: A conditional
inference framework. Journal of Computational and Graphical Statistics, 15:651–674,
2006.
F. Jiang, Z. Zhao, and X. Shao. Time series analysis of COVID-19 infection curve: A
change-point perspective. Journal of Econometrics, 232:1–17, 2023.
G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y. Liu. LightGBM:
A highly efficient gradient boosting decision tree. In Advances in Neural Information
| Processing | Systems, | volume 30, 2017. |     |     |
| ---------- | -------- | ---------------- | --- | --- |
R. Killick, P. Fearnhead, and I. A. Eckley. Optimal detection of changepoints with a
linear computational cost. Journal of the American Statistical Association, 107:1590–
1598, 2012.
71

J. Kim, H.-S. Oh, and H. Cho. Moving sum procedure for change point detection under
piecewise linearity. Technometrics, 66:358–367, 2024a.
J. Kim, H.-S. Oh, and H. Cho. Movingsumlin: Moving sum procedure for change-point
detection under piecewise linearity. GitHub repository, 2024b. URL https://github.
com/Joonpyo-Kim/MovingSumLin. Accessed 21 August 2026.
G.KondrakandP.vanBeek. Atheoreticalevaluationofselectedbacktrackingalgorithms.
Artificial Intelligence, 89:365–387, 1997.
S. Kova´cs, H. Li, P. Bu¨hlmann, and A. Munk. Seeded binary segmentation: a general
methodology for fast and optimal changepoint detection. Biometrika, 110:249–256,
2023.
H. Maeng and P. Fryzlewicz. Detecting linear trend changes in data sequences. Statistical
Papers, 65(3):1645–1675, 2024.
H. Maeng and P. Fryzlewicz. trendsegmentR: Linear Trend Segmentation, 2026. URL
https://CRAN.R-project.org/package=trendsegmentR. R package version 1.3.2.
R. Maidstone, P. Fearnhead, and A. Letchford. Detecting changes in slope with an L
0
penalty. Journal of Computational and Graphical Statistics, 28:265–275, 2019.
J. N. Morgan and J. A. Sonquist. Problems in the analysis of survey data, and a proposal.
Journal of the American Statistical Association, 58:415–434, 1963.
S. K. Murthy and S. Salzberg. Lookahead and pathology in decision tree induction. In
Proceedings of the 14th International Joint Conference on Artificial Intelligence (IJCAI-
95), pages 1025–1031. Morgan Kaufmann, 1995.
B.N.ParlettandD.R.Taylor. Alook-aheadLanczosalgorithmforunsymmetricmatrices.
Mathematics of Computation, 44(169):105–124, 1985.
R Core Team. R: A Language and Environment for Statistical Computing. R Foundation
forStatisticalComputing,Vienna,Austria,2025. URLhttps://www.R-project.org/.
H. Ritchie, P. Rosado, and V. Samborska. Climate change. Our World in Data, 2024.
URL https://ourworldindata.org/grapher/temperature-anomaly. Data adapted
from Met Office Hadley Centre–HadCRUT5; accessed 7 August 2026.
M. Rudelson and R. Vershynin. Hanson–Wright inequality and sub-Gaussian concentra-
tion. Electronic Communications in Probability, 18(82):1–9, 2013. doi: 10.1214/ECP.
v18-2865.
72

Aad W. van der Vaart and Jon A. Wellner. Weak Convergence and Empirical Processes:
| With Applications | to  | Statistics. Springer, | New York, | 1996. |
| ----------------- | --- | --------------------- | --------- | ----- |
E. S. Venkatraman. Consistency results in multiple change-point problems. PhD thesis,
Stanford University, 1992. Technical Report No. 24, Department of Statistics.
L. Vostrikova. Detection of the disorder in multidimensional random processes. Soviet
| Mathematics | – Doklady, | 259:270–274, | 1981. |     |
| ----------- | ---------- | ------------ | ----- | --- |
73
---- END DOCUMENT ----
