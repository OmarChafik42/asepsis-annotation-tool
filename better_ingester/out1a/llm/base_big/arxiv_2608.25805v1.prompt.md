Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
1
| Beyond            |     | Minimum     |     | Distance: |       |     | The Optimal |
| ----------------- | --- | ----------- | --- | --------- | ----- | --- | ----------- |
| Leading           |     | Coefficient |     |           | in    | the | High-SNR    |
| Error-Probability |     |             |     | Expansion |       |     | for AWGN    |
|                   |     | Spherical   |     |           | Codes |     |             |
6202 guA 62  ]TI.sc[  1v50852.8062:viXra
|     |     |     | Nikola | Zlatanov |     |     |     |
| --- | --- | --- | ------ | -------- | --- | --- | --- |
Abstract
Packing-optimal(M,n)sphericalcodesattainthelargestachievableminimumdistanceandtherefore
achieve the optimal exponential decay rate of the error probability at high signal-to-noise ratio (SNR).
Among packing-optimal codebooks held fixed as the SNR grows, the smallest leading coefficient is
Kfix , equal to the smallest number of ordered closest pairs of codewords among packing-optimal
M,n
codebooks. We show that SNR-wise codebook optimization can achieve a smaller leading coefficient,
and thereby a smaller error probability, than any packing-optimal codebook held fixed. Let P∗(M,n;γ)
e
be the SNR-wise minimum exact maximum-likelihood (ML) error probability and let Pfix(M,n;γ) be
e
the minimum exact error over all packing-optimal codebooks. We prove that P∗ =B∗(K∗ +o(1))
e γ M,n
and Pfix =B∗(Kfix +o(1)), and that K∗ ≤Kfix , where B∗ is the common Gaussian-tail factor.
| e   | γ   | M,n      |     | M,n | M,n | γ   |     |
| --- | --- | -------- | --- | --- | --- | --- | --- |
|     |     | K∗ <Kfix |     |     |     |     |     |
Hence, whenever , the SNR-wise minimum exact error is strictly smaller than the best
|     |     | M,n M,n |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- |
packing-optimal benchmark at all sufficiently high SNRs, i.e., P∗ < Pfix. We also show that the
e e
| minimum | of the | Gaussian soft-packing | energy | converges | to K∗ | .   |     |
| ------- | ------ | --------------------- | ------ | --------- | ----- | --- | --- |
M,n
The orthoplex-bound construction reveals how K∗ <Kfix can occur. The construction splits
|     |     |     |     |     | M,n | M,n |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
the pairs that are closest in the limiting packing into two classes. At finite SNR, the pairs in the first
class are deliberately made slightly closer than the optimal packing distance. This change is too small
to affect either the optimal asymptotic error exponent or the selected pairs’ unit contributions to the
constructed family’s leading coefficient. However, this creates enough geometric freedom to move the
other pairs—those in the second class—farther apart on a larger but still vanishing scale, so that their
contributions to the constructed family’s leading coefficient vanish. By contrast, every closest pair
N. Zlatanov is with Innopolis University, Innopolis, 420500, Russia (e-mail: n.zlatanov@innopolis.ru).

2
of a packing-optimal codebook held fixed contributes one to that codebook’s fixed-codebook leading
coefficient.
Weapplythedevelopedtheoreticalframeworktothesimplexrange,2≤M ≤n+1,andtheorthoplex-
bound range, M = n+k, 2 ≤ k ≤ n. We obtain K∗ = Kfix = M(M −1) for 2 ≤ M ≤ n+1.
|     |     |     |     | M,n | M,n |
| --- | --- | --- | --- | --- | --- |
For M =n+k, 2≤k ≤n, we prove Kfix =4n(k−1) and K∗ ≤4k(k−1). For n≥3 and
|     |     |            | n+k,n |     | n+k,n |
| --- | --- | ---------- | ----- | --- | ----- |
|     | K∗  | =8<4n=Kfix |       |     |       |
M =n+2, , so the optimized error is asymptotically smaller by the factor
|     |     | n+2,n | n+2,n |     |     |
| --- | --- | ----- | ----- | --- | --- |
n/2 than the best packing-optimal error. At the terminal endpoint k =n, K∗ =Kfix =4n(n−1).
2n,n 2n,n
| For | 3≤k ≤n−1, | we conjecture | that K∗ | =4k(k−1). |     |
| --- | --------- | ------------- | ------- | --------- | --- |
n+k,n
|     |     |     |     | Index Terms |     |
| --- | --- | --- | --- | ----------- | --- |
AWGN channels, spherical codes, maximum-likelihood decoding, message error probability, high-
| SNR | asymptotics, | spherical packing, | codebook | optimization, | leading coefficients. |
| --- | ------------ | ------------------ | -------- | ------------- | --------------------- |
I. INTRODUCTION
At high average signal-to-noise ratio (SNR) per real channel use, finite spherical-code design
raises two nested questions. First, how rapidly can the minimum achievable average message
error probability under maximum-likelihood (ML) decoding decay? Second, after removing that
decay scale, how small can the remaining leading coefficient be? Optimal spherical packing,
through the largest achievable minimum distance, answers the first question. It need not answer
the second. Codebook families can have the same packing-determined exponential decay yet
| differ by | a nonvanishing | multiplicative | factor | in error | probability. |
| --------- | -------------- | -------------- | ------ | -------- | ------------ |
For a packing-optimal codebook held fixed as the SNR grows, classical high-SNR theory
shows that its number of ordered closest pairs of codewords determines the leading coefficient in
its high-SNR error-probability expansion [1], [2]. Dividing this count by M gives the codebook’s
average kissing number. Hence, among packing-optimal codebooks that are each held fixed as
the SNR grows, minimizing the leading coefficient is equivalent to choosing a codebook with the
smallest ordered closest-pair count, or, equivalently, the smallest average kissing number. The
optimization studied here is different: the codeword locations may be reoptimized at every SNR.
Because pairwise Gaussian error probabilities depend exponentially on the SNR and the pairwise
squared distances, vanishing changes in codeword distances can still change the error probability
by a nonvanishing factor. This allows an SNR-wise optimized codebook family to approach the
set of optimal packings while having a smaller leading coefficient than every packing-optimal
codebook held fixed. Its error probability is then smaller than the best fixed packing-optimal

3
benchmark at all sufficiently high SNRs. Consequently, optimizing the codebook at each SNR
and then taking the high-SNR limit can yield a smaller leading coefficient than first taking the
high-SNR limit for each fixed codebook and then optimizing over the packing-optimal class.
The explicit SNR-dependent construction developed in this paper for the orthoplex-bound range
M = n+k, 2 ≤ k < n, makes this phenomenon concrete. The construction splits the codeword
pairs that are closest in the limiting packing into two classes. At finite SNR, the pairs in the first
class are deliberately made slightly closer than the optimal packing distance. This deterioration
is too small to change either the optimal asymptotic error exponent or the selected pairs’ unit
contributions to the constructed family’s leading coefficient. However, it creates enough geometric
freedom to move the other pairs—those in the second class—farther apart on a larger but still
vanishing scale, so that their contributions to the constructed family’s leading coefficient vanish.
The constructed family retains the packing-optimal exponent and approaches an optimal packing
as the SNR grows, yet lies outside the set of optimal packings at every sufficiently large finite
SNR. Its leading coefficient is smaller than that of every packing-optimal codebook held fixed as
the SNR grows. This improvement cannot be obtained by holding any one codebook fixed. The
smaller coefficient is obtained only because the codebook continues to change with SNR.
Let P∗(M,n;γ) denote the exact average ML message error probability minimized over all
e
(M,n) spherical codebooks at SNR γ. For every fixed finite pair (M,n) considered here, we
| prove the general | expansion |           |     |         |         |
| ----------------- | --------- | --------- | --- | ------- | ------- |
|                   |           |           |     | (cid:0) | (cid:1) |
|                   |           | P∗(M,n;γ) |     | = B∗ K∗ | +o(1) , |
|                   |           | e         |     | γ       | M,n     |
where B∗ contains the packing-determined exponential decay and Gaussian prefactor, and K∗
γ M,n
| is a well-defined | optimal leading |     | coefficient. |     |     |
| ----------------- | --------------- | --- | ------------ | --- | --- |
For comparison, let Pfix(M,n;γ) denote the exact average ML message error probability
e
minimized over all spherical codebooks attaining the largest possible minimum distance. Then
|     |     |             |     | (cid:0)   | (cid:1) |
| --- | --- | ----------- | --- | --------- | ------- |
|     |     | Pfix(M,n;γ) |     | = B∗ Kfix | +o(1) , |
|     |     | e           |     | γ         | M,n     |
where Kfix is the smallest number of ordered closest-pair indices among packing-optimal
M,n
codebooks and Kfix /M is the smallest average kissing number. We show that K∗ ≤ Kfix . If
M,n M,n M,n
K∗ < Kfix , then P∗(M,n;γ) < Pfix(M,n;γ) for all sufficiently large γ, and
| M,n M,n | e   |             | e         |      |          |
| ------- | --- | ----------- | --------- | ---- | -------- |
|         |     |             | P∗(M,n;γ) | K∗   |          |
|         |     |             | e         | −→   | M,n < 1. |
|         |     | Pfix(M,n;γ) |           | Kfix |          |
|         |     |             | e         |      | M,n      |

4
Thus the improvement is a persistent multiplicative reduction in the minimum exact error
probability.
We call an SNR-dependent family packing-tail competitive if its normalized error remains
bounded on the packing-tail scale. We show that every such family approaches the set of optimal
packings. If such a family has a leading coefficient, then, along any convergent codebook
subsequence, only pairs that are closest in the packing-optimal limiting codebook can contribute
to that coefficient. The contribution of each such pair depends on the rate at which its correlation
approaches the optimal packing value and may be zero, fractional, one, or greater than one. For a
family attaining the optimal leading coefficient, these pairwise contributions sum to K∗ . Thus,
M,n
for a family attaining the optimal leading coefficient, the packing-optimal limiting codebook
identifies which pairs can contribute to K∗ , whereas the SNR-dependent codebook optimization
M,n
determines how much each such pair contributes to K∗ .
M,n
To analyze this geometry, we introduce a Gaussian soft-packing energy that continuously
accounts for all pairwise confusions. We prove that it uniformly represents the normalized exact
ML error for the SNR-dependent families relevant to optimized high-SNR design, and that its
minimum converges to K∗ . Consequently, every family whose Gaussian soft-packing energy is
M,n
within an additive o(1) of its global minimum is asymptotically ML-optimal.
A. Contributions
The contributions are as follows. The first three contributions apply to every fixed finite (M,n)
(with M ≥ 2) for which the best packing has nonzero minimum distance. The last two apply the
theory throughout the simplex and orthoplex-bound ranges.
1) Optimal leading-coefficient characterization and fixed-codebook benchmark. We introduce
a Gaussian soft-packing energy and prove that it uniformly represents the normalized
exact ML error on the bounded Gaussian soft-packing energy classes relevant to packing-
tail-competitive designs. Its minimum converges to a well-defined optimal leading coeffi-
cient K∗ , yielding the high-SNR expansion of the minimum average error probability,
M,n
P∗(M,n;γ) = B∗(K∗ +o(1)). We also prove Pfix(M,n;γ) = B∗(Kfix +o(1)) for the
e γ M,n e γ M,n
best packing-optimal benchmark. We show that K∗ ≤ Kfix . Hence, when K∗ < Kfix ,
M,n M,n M,n M,n
P∗(M,n;γ) < Pfix(M,n;γ) for all sufficiently large γ, and their ratio tends to K∗ /Kfix
e e M,n M,n
as the SNR grows.

5
2) Localization and SNR-dependent closest-pair contributions of packing-tail-competitive
| families. |          |      |                         | P   | (C ;γ)/B∗ | = O(1) |            |     |
| --------- | -------- | ---- | ----------------------- | --- | --------- | ------ | ---------- | --- |
|           | We prove | that | every family satisfying | e   | γ         |        | approaches | the |
γ
packing-optimal set. Along convergent subsequences, only pairs that are closest in the
packing-optimal limiting codebook can have nonvanishing normalized contributions, and
these contributions are determined by their scaled correlation offsets. Whenever the family’s
leading coefficient exists, these contributions sum to that coefficient; for a family attaining
the optimal leading coefficient, they sum to K∗ . This explains why neither an optimal
M,n
packing nor its ordinary closest-pair count alone determines the optimal leading coefficient
K∗
. Minimizing over all packing-optimal limiting codebooks and all jointly feasible
M,n
scaled closest-pair offsets yields an exact variational characterization of K∗ .
M,n
3) Attainment and matching-bound certification. We prove that codebook families whose
Gaussian soft-packing energy is within an additive o(1) of its global minimum are
asymptotically ML-optimal. We then give a matching-bounds criterion that certifies both
a proposed optimal leading coefficient and a full SNR-indexed construction attaining the
| optimal | leading coefficient. |     |     |     |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
4) Simplex code. For every 2 ≤ M ≤ n+1, we prove that an embedded regular (M −1)-
simplex minimizes the soft-packing objective exactly at every positive SNR and that
K∗ = Kfix = M(M − 1). The constant simplex family is therefore asymptotically
| M,n        | M,n   |          |                 |     |     |     |     |     |
| ---------- | ----- | -------- | --------------- | --- | --- | --- | --- | --- |
| ML-optimal | under | SNR-wise | reoptimization. |     |     |     |     |     |
5) Orthoplex-bound range. For the orthoplex-bound range M = n + k, 2 ≤ k ≤ n, we
Kfix
determine = 4n(k −1). For every 2 ≤ k < n, an explicit SNR-dependent family
n+k,n
K∗
has leading coefficient 4k(k −1), which proves ≤ 4k(k −1). Hence, the optimal
n+k,n
leading coefficient, K∗ , is strictly smaller than the fixed benchmark, Kfix , and
|     |     | n+k,n |             |     |     |     | n+k,n |     |
| --- | --- | ----- | ----------- | --- | --- | --- | ----- | --- |
|     |     |       | P∗(n+k,n;γ) | K∗  | k   |     |       |     |
n+k,n
|     |     | lim | e             | =     | ≤   | < 1. |     |     |
| --- | --- | --- | ------------- | ----- | --- | ---- | --- | --- |
|     |     |     | Pfix(n+k,n;γ) | Kfix  |     |      |     |     |
|     |     | γ→∞ |               |       | n   |      |     |     |
|     |     |     | e             | n+k,n |     |      |     |     |
At the left endpoint k = 2, a matching converse proves K∗ = 8, thereby showing
n+2,n
that P∗(n + 2,n;γ) is asymptotically smaller by the factor n/2 than Pfix(n + 2,n;γ).
|     | e   |     |     |     |     |     | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
At the terminal endpoint k = n, universal optimality of the full cross-polytope proves
K∗ = Kfix = 4n(n−1). For 3 ≤ k ≤ n−1, we conjecture that K∗ = 4k(k −1).
| 2n,n | 2n,n |     |     |     |     |     | n+k,n |     |
| ---- | ---- | --- | --- | --- | --- | --- | ----- | --- |

6
B. Relation to Existing Theory
For a fixed finite codebook over the AWGN channel, the pairwise error is a Gaussian tail, and
the closest-pair expansion is asymptotically equivalent to the exact ML message error probability
[1], [2]. Because these results hold the codebook fixed, they do not justify minimizing the
resulting formula over a different codebook at every SNR. At the exponential scale, equal-
energy codebook design is the classical spherical-packing problem [3]–[6], for which linear- and
semidefinite-programming methods provide powerful general bounds [7]–[10].
The simplex application uses the simplex bound [4] and the universal optimality of embedded
regular simplices [11]. The orthoplex-bound application uses the orthoplex bound [4] and its
equality-case classification [12, Thm. 3]; an equivalent characterization is given in [13, Thm. 2.2].
It also uses the universal optimality of the full cross-polytope [11]. The recent result in [14,
Cors. 2.5–2.6] proves the stronger finite-SNR coding statement that, for M equiprobable equal-
energy signals over the real AWGN channel, an embedded regular (M −1)-simplex maximizes
the average probability of correct ML decoding at every positive SNR whenever n ≥ M −1.
That result also characterizes the equality case: the embedded regular simplex is the unique
maximizer up to an orthogonal transformation and relabeling.
A closely related large-parameter phenomenon occurs for Riesz energies. In [15], the authors
proved that cluster points of fixed-cardinality Riesz-energy minimizers as the exponent tends
to infinity are best packings. For five points on S2, they identified, up to isometry, the unique
limiting square-pyramid configuration and proved that the normalized minimum Riesz energy
converges to 8; their upper bound uses an exponent-dependent square-pyramid deformation. This
is a close antecedent to the (M,n) = (5,3) specialization of the SNR-dependent construction in
our work. Their Riesz objective, however, neither gives the Gaussian construction for general
(n+k,n) nor transfers its asymptotics to exact AWGN ML error.
In a different positive-temperature cross-entropy problem motivated by neural collapse, [16]
show that, among packing-optimal codes in the orthoplex regime, sufficiently low temperature
selects a “low-entropy” geometry consisting of one regular simplex and an orthogonal cross-
polytope. For M = n+k, this is the same simplex-plus-antipodal-pairs geometry that attains the
best fixed-codebook leading coefficient here. Their feasible class and objective are different, and
their result does not address SNR-dependent paths outside the packing-optimal set.
The preceding works provide geometric, coding, and energy results that serve as technical inputs

7
or conceptual antecedents for particular simplex and orthoplex-bound applications considered
here. The theory developed in this paper is broader: it is not restricted to these special geometries
and characterizes the optimal high-SNR leading coefficient when a finite spherical codebook may
be reoptimized at each SNR. Its new ingredients are the uniform transfer from the soft-packing
energy to exact ML error, the existence and characterization of the optimal leading coefficient,
and the localization and closest-pair contribution results for competitive SNR-dependent families.
The simplex and orthoplex-bound results are concrete applications of this general framework.
C. Organization
Section II formulates the exact design problem and its fixed-codebook benchmark. Section III
develops the soft-packing characterization of the optimal leading coefficient and establishes
attainment by near-minimizers of the Gaussian soft-packing energy. Section IV establishes
localization, the SNR-dependent closest-pair structure of competitive families, and the global
variational characterization by jointly feasible scaled offsets. Section V develops the matching-
bounds criterion used in the applications. Sections VI and VII apply this theory to the simplex
and orthoplex-bound ranges, respectively. Section VIII concludes the paper, and the appendices
provide the technical proofs.
II. SIGNAL MODEL AND HIGH-SNR CODEBOOK DESIGN PROBLEM
This section introduces the exact AWGN error probability, the spherical-packing quantities
that determine its optimal exponential decay, and the classical high-SNR expansion for a fixed
codebook. It then defines the exact-error benchmark obtained by restricting the design to packing-
optimal codebooks and formulates the unrestricted optimization performed separately at each
SNR.
A. Signal Model and Exact Error Probability
Fix integers M ≥ 2 and n ≥ 1, write [M] = {1,...,M}, and let Sn−1 = {x ∈ Rn : ∥x∥ = 1}.
A labeled spherical codebook is
C = (c ,...,c ) ∈ M, M = (Sn−1)M,
1 M
where every codeword has unit norm. The product space M is compact.

8
| Let | W be uniform | on  | [M]. | The normalized |     | real | AWGN | channel | is  |     |
| --- | ------------ | --- | ---- | -------------- | --- | ---- | ---- | ------- | --- | --- |
√
|     |     |     | Y   | = nγc |     | +Z, | Z   | ∼ N(0,I | ).  | (1) |
| --- | --- | --- | --- | ----- | --- | --- | --- | ------- | --- | --- |
|     |     |     |     |       | W   |     |     |         | n   |     |
The noise variance is one per real channel use, and the transmitted vector has energy nγ; hence
γ is the average SNR per real channel use. Unless stated otherwise, every high-SNR limit keeps
| (M,n) | fixed and lets | γ → | ∞.    |                        |     |             |     |         |     |     |
| ----- | -------------- | --- | ----- | ---------------------- | --- | ----------- | --- | ------- | --- | --- |
| For   | an observation | y   | ∈ Rn, | the maximum-likelihood |     |             |     | decoder | is  |     |
|       |                |     |       | W(cid:99)(y)           |     | ∈ argmaxyTc |     | .       |     | (2) |
m
1≤m≤M
Because all codewords have the same norm, maximizing correlation is equivalent to minimizing
Euclidean distance. We use an arbitrary fixed measurable rule to break ties. With equiprobable
messages, the average error is independent of that choice, and ties have probability zero when
| no two | codewords     | coincide. |     |       |             |     |     |     |     |     |
| ------ | ------------- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- |
| The    | exact average | message   |     | error | probability | is  |     |     |     |     |
1 M
(cid:88)
|     |     |     | P (C;γ) | =   |     | P{W(cid:99)(Y | ) ̸= | m | | W = m}. | (3) |
| --- | --- | --- | ------- | --- | --- | ------------- | ---- | --- | ------- | --- |
e
M
m=1
| B. Pairwise | Geometry | and | the | Packing | Benchmark |     |     |     |     |     |
| ----------- | -------- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- |
Let
|     |     |     |     | E = | {(m,ℓ) | : m,ℓ | ∈ [M], | m   | ̸= ℓ} |     |
| --- | --- | --- | --- | --- | ------ | ----- | ------ | --- | ----- | --- |
M
be the ordered-pair index set. For e = (m,ℓ) ∈ E , define the pairwise correlation
M
|         |               |     |           |       | ρ   | (C) = | cTc .   |         |     | (4) |
| ------- | ------------- | --- | --------- | ----- | --- | ----- | ------- | ------- | --- | --- |
|         |               |     |           |       |     | e     | m ℓ     |         |     |     |
| Because | the codewords |     | have unit | norm, |     |       |         |         |     |     |
|         |               |     |           |       |     | ∥2    | (cid:0) | (cid:1) |     |     |
|         |               |     |           | ∥c    | −c  | =     | 2 1−ρ   | (C)     | .   | (5) |
|         |               |     |           |       | m   | ℓ     |         | e       |     |     |
Thus a larger correlation means a smaller Euclidean distance, and minimizing the largest pairwise
correlation is equivalent to solving the spherical-code, or spherical-cap-packing, problem [4]–[6].
The largest correlation of a particular codebook and the smallest such largest correlation
| attainable | over all | codebooks |     | are, respectively, |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
ρ∗
|     |     | ρ   | (C) | = maxρ |     | (C), |     | = minρ | (C). | (6) |
| --- | --- | --- | --- | ------ | --- | ---- | --- | ------ | ---- | --- |
|     |     |     | max |        | e   |      | M,n |        | max  |     |
|     |     |     |     | e∈EM   |     |      |     | C∈M    |      |     |

9
The minimum exists because M is compact and ρ is continuous. Thus ρ (C) is the worst
max max
C:
correlation within the particular codebook it identifies its closest pair or pairs. By contrast,
ρ∗
is the best worst correlation achievable among all (M,n) spherical codebooks. Equivalently,
M,n
| 2(1−ρ∗ | ) is the | largest | achievable |     | minimum |     | squared | distance. |     |     |
| ------ | -------- | ------- | ---------- | --- | ------- | --- | ------- | --------- | --- | --- |
M,n
| The | packing-optimal |     | codebook |     | set is |     |         |     |     |     |
| --- | --------------- | --- | -------- | --- | ------ | --- | ------- | --- | --- | --- |
|     |                 |     |          | P∗  |        |     |         | ρ∗  |     |     |
|     |                 |     |          |     | = {C   | ∈ M | : ρ (C) | =   | }.  | (7) |
|     |                 |     |          |     |        |     | max     | M,n |     |     |
Hence, P∗ is the collection of all codebooks whose worst correlation equals the best worst
ρ∗
correlation . It contains every solution of the spherical-packing problem, including rotated
M,n
and relabeled copies and, when they exist, geometrically noncongruent optimal packings.
The analysis in this paper concerns spherical codes for which ρ∗ < 1. Then every packing-
M,n
optimal codebook has pairwise-distinct codewords, and its optimal minimum squared distance is
2(1−ρ∗ ) > 0. The value ρ∗ determines the best high-SNR error exponent.
|     | M,n |     |     | M,n |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Anunorderedcodewordpair{m,ℓ}isaclosestpair ofC ifitattainstheminimumintercodeword
distance, or equivalently if ρ (C) = ρ (C). Collect the corresponding ordered closest-pair
|     |     |     |     | (m,ℓ) |     | max |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
indices in
|     |     |     |     | I (C) | = {e | ∈ E | : ρ (C) | = ρ | (C)}. | (8) |
| --- | --- | --- | --- | ----- | ---- | --- | ------- | --- | ----- | --- |
|     |     |     |     | max   |      |     | M e     | max |       |     |
For each unordered closest pair, this set contains both directed indices (m,ℓ) and (ℓ,m). If
| P∗,               |             |          |     |             |             |     | ρ∗  |     |     |     |
| ----------------- | ----------- | -------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- |
| C ∈               | every index | in       | I   | (C) has     | correlation |     | .   |     |     |     |
|                   |             |          | max |             |             |     | M,n |     |     |     |
| C. Fixed-Codebook |             | High-SNR |     | Asymptotics |             |     |     |     |     |     |
Assume a codebook C is pairwise distinct, i.e., ρ (C) < 1 holds. For such a codebook and
max
| distinct | m,ℓ, conditioned |     | on  | W =  | m, let |       |     |     |         |     |
| -------- | ---------------- | --- | --- | ---- | ------ | ----- | --- | --- | ------- | --- |
|          |                  |     |     | √    |        |       | √   |     |         |     |
|          |                  |     | A   | = {( | nγc    | +Z)Tc | ≥ ( | nγc | +Z)Tc } |     |
|          |                  |     | mℓ  |      | m      |       | ℓ   | m   | m       |     |
be the event that competitor ℓ scores at least as highly as the transmitted codeword. For e = (m,ℓ),
| write A | := A | . The | standard | pairwise |     | Gaussian          | calculation |      | gives    |     |
| ------- | ---- | ----- | -------- | -------- | --- | ----------------- | ----------- | ---- | -------- | --- |
|         | e mℓ |       |          |          |     |                   |             |      |          |     |
|         |      |       |          |          |     | (cid:32)(cid:114) |             |      | (cid:33) |     |
|         |      |       |          |          |     |                   | nγ[1−ρ      | (C)] |          |     |
(m,ℓ)
|     |     |     |     | P(A | ) = | Q   |     |     | ,   | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mℓ
2
|            | (2π)−1/2 |     | (cid:82)∞ | exp{−t2/2}dt |     |      |               |     |     |     |
| ---------- | -------- | --- | --------- | ------------ | --- | ---- | ------------- | --- | --- | --- |
| where Q(x) | =        |     |           |              |     | [1]. | Consequently, |     |     |     |
x
|     |     |     |     |     |     |     | (cid:32) | (cid:33) |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- |
M
|     |     |     |     |     |       | 1   | (cid:88) (cid:91) |     |     |      |
| --- | --- | --- | --- | --- | ----- | --- | ----------------- | --- | --- | ---- |
|     |     |     |     | P   | (C;γ) | =   | P                 | A   | .   | (10) |
|     |     |     |     | e   |       |     |                   | mℓ  |     |      |
M
|     |     |     |     |     |     |     | m=1 ℓ̸=m |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |

10
| For ρ | < 1, define |     | the single-ordered-pair |     |     | tail | scale |     |     |     |     |     |
| ----- | ----------- | --- | ----------------------- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- |
exp{−nγ(1−ρ)/4}
|     |     |     |     |     | b (ρ) = |     |             |        | .   |     |     | (11) |
| --- | --- | --- | --- | --- | ------- | --- | ----------- | ------ | --- | --- | --- | ---- |
|     |     |     |     |     | γ       |     | √ (cid:112) |        |     |     |     |      |
|     |     |     |     |     |         | M   | nγ          | π(1−ρ) |     |     |     |      |
The standard fixed-codebook high-SNR result then takes the following form.
Proposition 1 (Fixed-codebook high-SNR expansion). Let C be fixed with pairwise-distinct
| codewords, | equivalently |     | ρ   | (C) | < 1. Then |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
max
|     |     |     |       |     |      | (cid:32)(cid:114) |        |     | (cid:33) |         |         |     |
| --- | --- | --- | ----- | --- | ---- | ----------------- | ------ | --- | -------- | ------- | ------- | --- |
|     |     |     |       | |I  | (C)| |                   | nγ[1−ρ |     | (C)]     |         |         |     |
|     |     |     |       |     | max  |                   |        | max |          | (cid:0) | (cid:1) |     |
|     |     | P   | (C;γ) | =   |      | Q                 |        |     |          | 1+o     | (1)     |     |
|     |     | e   |       |     |      |                   |        |     |          | C       |         |     |
|     |     |     |       |     | M    |                   |        | 2   |          |         |         |     |
(12)
|     |     |     |     |     |         | (cid:0) |        |     | (cid:1) |     |     |     |
| --- | --- | --- | --- | --- | ------- | ------- | ------ | --- | ------- | --- | --- | --- |
|     |     |     |     | = b | (ρ (C)) | |I      | (C)|+o | (1) | .       |     |     |     |
|     |     |     |     | γ   | max     |         | max    | C   |         |     |     |     |
Consequently,
|     |     |     |     |     |          |       |     | n[1−ρ | (C)] |     |     |      |
| --- | --- | --- | --- | --- | -------- | ----- | --- | ----- | ---- | --- | --- | ---- |
|     |     |     |     |     | −γ−1logP |       |     |       | max  |     |     |      |
|     |     |     |     | lim |          | (C;γ) | =   |       |      | .   |     | (13) |
|     |     |     |     |     |          | e     |     |       | 4    |     |     |      |
γ→∞
| Here | and throughout, |     | log | denotes | the | natural | logarithm. |     |     |     |     |     |
| ---- | --------------- | --- | --- | ------- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
The proposition follows by specializing the standard fixed-constellation result [2, Th. 3] to
equal-prior spherical codebooks. It is the conventional nearest-neighbor principle stated directly
as an expansion of the exact error: after normalization by the tail scale associated with its own
worst correlation, a fixed codebook has leading coefficient |I (C)|. The remainder o (1) is
|     |     |     |     |     |     |     |     |     | max |     |     | C   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pointwise in C: it tends to zero for each fixed codebook, but its rate may vary with the codebook.
Evaluating (11) at the optimal packing correlation defines the single-ordered-pair packing-tail
scale
|     |     |     |     |     |     |     | exp{−nγ(1−ρ∗ |     |     | )/4} |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---- | --- | --- |
M,n
|     |     |     | B∗  | :=  | b (ρ∗ | ) = |     |           |     | .   |     | (14) |
| --- | --- | --- | --- | --- | ----- | --- | --- | --------- | --- | --- | --- | ---- |
|     |     |     |     | γ   | γ M,n |     | √   | (cid:113) |     |     |     |      |
π(1−ρ∗
|     |     |     |     |     |     |     | M nγ |     |     | )   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
M,n
It contains the optimal exponential decay, the Gaussian-tail prefactor, and the 1/M message
average, but no closest-pair multiplicity. Any fixed codebook outside P∗ has ρ (C) > ρ∗ ,
|     |     |     |     |     |     |     |     |     |     |     | max | M,n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and its exact error divided by B∗ therefore grows exponentially. Hence only packing-optimal
γ
codebooks can serve as fixed-codebook benchmarks at the optimal exponent, and every fixed
| C ∈ P∗ | satisfies |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     |     |     | P (C | ;γ) |       |       |     |     |     |      |
| --- | --- | --- | --- | --- | ---- | --- | ----- | ----- | --- | --- | --- | ---- |
|     |     |     |     |     | e    | 0   | −→ |I | (C    | )|. |     |     | (15) |
|     |     |     |     |     |      |     |       | max 0 |     |     |     |      |
B∗
γ
The best fixed-codebook leading coefficient attainable among packing-optimal codebooks is
therefore
|     |     |     |     |     | Kfix | :=  | min |I | (C    | )|. |     |     |      |
| --- | --- | --- | --- | --- | ---- | --- | ------ | ----- | --- | --- | --- | ---- |
|     |     |     |     |     |      |     |        | max 0 |     |     |     | (16) |
|     |     |     |     |     | M,n  |     | C0∈P∗  |       |     |     |     |      |

11
Equivalently, among all packing-optimal codebooks, one chooses a codebook with the fewest
ordered closest-pair indices and uses that same codebook as the SNR increases. Moreover,
Kfix
/M is the smallest average kissing number among packing-optimal codebooks.
M,n
To compare exact error probabilities, define the best packing-optimal benchmark at SNR γ by
Pfix(M,n;γ)
|     |     |     |     |     |     | := min | P (C ;γ). | (17) |
| --- | --- | --- | --- | --- | --- | ------ | --------- | ---- |
|     |     |     |     | e   |     |        | e 0       |      |
C0∈P∗
The minimum is attained because P∗ is compact and the exact average ML error is continuous
| on this | set. We | show | later, | cf. Corollary |     | 1, that   |         |      |
| ------- | ------- | ---- | ------ | ------------- | --- | --------- | ------- | ---- |
|         |         |      |        |               |     | (cid:0)   | (cid:1) |      |
|         |         |      |        | Pfix(M,n;γ)   |     | = B∗ Kfix | +o(1) . | (18) |
|         |         |      |        | e             |     | γ         | M,n     |      |
Accordingly, Kfix and Pfix(M,n;γ) are the best fixed-codebook leading-coefficient and exact-
|     |     | M,n | e   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
error benchmarks against which the SNR-wise optimized quantities are compared.
| D. Exact | High-SNR |     | Codebook | Design | Problem |     |     |     |
| -------- | -------- | --- | -------- | ------ | ------- | --- | --- | --- |
For fixed (M,n) and operating SNR γ, the exact SNR-wise optimal average error probability
is
|     |     |     |     | P∗(M,n;γ) |     | = minP | (C;γ). | (19) |
| --- | --- | --- | --- | --------- | --- | ------ | ------ | ---- |
e
e
C∈M
Thus the minimization ranges over all labeled M-tuples of unit vectors in Rn, and P∗(M,n;γ)
e
denotes the smallest exact average ML error probability among them. The minimum is attained
M
because is compact and the average ML error is continuous in the codeword tuple.
| An optimizing |     | codebook |     | may be | denoted | by      |        |     |
| ------------- | --- | -------- | --- | ------ | ------- | ------- | ------ | --- |
|               |     |          |     |        | C∗ ∈    | argminP | (C;γ). |     |
e
γ
C∈M
The subscript emphasizes that the optimizing codebook may change with SNR; there is no
| requirement | that | C∗  | = C∗ | .   |     |     |     |     |
| ----------- | ---- | --- | ---- | --- | --- | --- | --- | --- |
|             |      | γ1  | γ2   |     |     |     |     |     |
P∗
Because ⊆ M, the two exact design problems in (17) and (19) obey
|     |     |     | P∗(M,n;γ) |     | ≤   | Pfix(M,n;γ) | for every γ. | (20) |
| --- | --- | --- | --------- | --- | --- | ----------- | ------------ | ---- |
|     |     |     |           | e   |     | e           |              |      |
Every fixed C ∈ P∗ achieves the best error exponent. Among such fixed codebooks, however,
0
only a minimizer in (16) is guaranteed to have the smallest fixed-codebook leading coefficient.
Determining the unrestricted exact finite-SNR minimum P∗(M,n;γ) and its optimal leading
e
| coefficient | requires |     | optimization | over | the | full codebook | manifold. |     |
| ----------- | -------- | --- | ------------ | ---- | --- | ------------- | --------- | --- |

12
The central problem of this paper is therefore to determine whether the limit
P∗(M,n;γ)
|     |     | lim | e   |     |     | (21) |
| --- | --- | --- | --- | --- | --- | ---- |
γ→∞ B∗
γ
exists and is finite and, if so, to characterize it. Once existence is proved, the limit is denoted by
K∗ and is called the optimal leading coefficient. For any SNR-dependent family, if P (C ;γ)/B∗
| M,n |     |     |     |     | e γ | γ   |
| --- | --- | --- | --- | --- | --- | --- |
converges to a finite limit, we call that limit the leading coefficient of the family. For a general
SNR-dependent family on which no asymptotic optimality condition is imposed, this finite
limit need not exist: the normalized error may be unbounded, or it may remain bounded while
approaching different finite values along different SNR subsequences. This possible nonexistence
concerns the leading coefficient of such a family and does not arise for the optimal leading
coefficient. As shown later, cf. Theorem 2, P∗(M,n;γ)/B∗ converges to a finite limit and hence
|             |                     |            | e   | γ   |     |     |
| ----------- | ------------------- | ---------- | --- | --- | --- | --- |
| the optimal | leading coefficient | K∗ exists. |     |     |     |     |
M,n
An SNR-dependent family {C } attains the optimal leading coefficient if it satisfies
γ γ
P (C ;γ)
e γ K∗
|     |     |     | −→  | ,   |     |      |
| --- | --- | --- | --- | --- | --- | ---- |
|     |     | B∗  | M,n |     |     |      |
|     |     |     | γ   |     |     | (22) |
P (C ;γ)
e γ
−→ 1.
P∗(M,n;γ)
e
A second objective is to investigate whether K∗ < Kfix can occur and to characterize the
|     |     |     | M,n | M,n |     |     |
| --- | --- | --- | --- | --- | --- | --- |
associated geometric mechanism. A strict inequality means that SNR-dependent motion of the
codewords toward the packing-optimal set improves the optimal leading coefficient even though
both designs have the same optimal error exponent. Together with (18), the main optimized
| expansion | proved below | then gives |     |     |     |     |
| --------- | ------------ | ---------- | --- | --- | --- | --- |
P∗(M,n;γ) K∗
e M,n
|     |     |     | −→  | .   |     | (23) |
| --- | --- | --- | --- | --- | --- | ---- |
Pfix(M,n;γ) Kfix
e M,n
Hence K∗ < Kfix implies P∗(M,n;γ) < Pfix(M,n;γ) for all sufficiently large γ.
|        | M,n M,n | e         | e    |     |     |     |
| ------ | ------- | --------- | ---- | --- | --- | --- |
|        | K∗ Kfix |           |      |     |     |     |
| E. How | <       | Can Occur |      |     |     |     |
|        | M,n M,n |           |      |     |     |     |
|        |         |           | Kfix |     | K∗  |     |
The best fixed-codebook leading coefficient and the optimal leading coefficient
|     |     |     | M,n |     |     | M,n |
| --- | --- | --- | --- | --- | --- | --- |
Kfix
arise from different high-SNR procedures. The coefficient is obtained by holding a packing-
M,n
optimal codebook fixed as the SNR grows, identifying its number of ordered closest-pair indices,
and then minimizing this number over P∗. By contrast, K∗ is attained asymptotically by an
M,n
SNR-dependent family {C } . By definition, no codebook in P∗ has fewer than Kfix ordered
|     |     | γ γ |     |     | M,n |     |
| --- | --- | --- | --- | --- | --- | --- |
closest-pair indices. Hence, an attaining family under the strict inequality K∗ < Kfix , cf.
M,n M,n

13
Lemma 1, approaches P∗ while remaining outside it for all sufficiently large γ. Hence, the strict
inequality arises from the relative rates at which an SNR-dependent codebook family approaches
P∗.
| the | packing-optimal |     | set |     |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To make this more precise, along a convergent subsequence, reindexed by γ, write C →
γ
C ∈ P∗. For an ordered pair e ∈ I (C ), define its signed correlation offset from the optimal
| ∞       |       |             |     |                 | max | ∞    |       |          |     |     |     |     |
| ------- | ----- | ----------- | --- | --------------- | --- | ---- | ----- | -------- | --- | --- | --- | --- |
| packing | value | and compare |     | its single-pair |     | tail | scale | with B∗: |     |     |     |     |
γ
|     |     |     |     | ∆   | :=  | ρ (C | )−ρ∗ | ,   |     |     |     | (24) |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | e,γ | e    | γ    | M,n |     |     |     |      |
(cid:115)
|     |     |     |     |         |     | (cid:26) |     | (cid:27) |     |     |     |      |
| --- | --- | --- | --- | ------- | --- | -------- | --- | -------- | --- | --- | --- | ---- |
|     |     |     |     | b (ρ (C | ))  |          | nγ∆ | 1−ρ∗     |     |     |     |      |
|     |     |     |     | γ e     | γ   |          | e,γ |          | M,n |     |     |      |
|     |     |     |     |         | =   | exp      |     |          |     | .   |     | (25) |
|     |     |     |     | B∗      |     |          | 4   | 1−ρ      | (C  | )   |     |      |
e γ
γ
Because ρ (C ) → ρ∗ , the square-root factor tends to one. As the limiting-closest-pair result
|     | e   | γ   | M,n |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
below makes rigorous, for the family under discussion that attains the optimal leading coefficient,
if nγ∆ → λ ∈ R∪{−∞}, then the contribution of the ordered pair e to K∗ is exp{λ /4},
|     | e,γ | e   |     |     |     |     |     |     |     |     | M,n | e   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where exp{−∞} = 0. Thus a zero scaled offset gives a unit contribution to K∗ , whereas
M,n
divergence to −∞ suppresses the contribution even though the pair is closest in the packing-
| optimal | limit | C . |     |     |     |     |     |     |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∞
A revealing mechanism for achieving K∗ < Kfix , applied in the orthoplex-bound range, is
|     |     |     |     |     |     | M,n |     | M,n |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the following. Partition the closest-pair indices in I (C ) into two classes, denoting indices in
|     |     |     |     |     |     |     |     | max ∞ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
the selected class by e and those in the remaining class by f. At finite SNR γ, arrange their
| correlations |     | so that  |     |        |     |     |     |         |     |     |       |     |
| ------------ | --- | -------- | --- | ------ | --- | --- | --- | ------- | --- | --- | ----- | --- |
|              | ρ   | (C ) = ρ | (C  | ) = ρ∗ | +p  | ,   | p > | 0, p −→ | 0,  | nγp | −→ 0, |     |
|              |     | e γ      | max | γ      | M,n | γ   | γ   | γ       |     |     | γ     |     |
(26)
|     | ρ   | (C ) = ρ∗ | −q  | ,   |     | q   | >   | 0, q −→ | 0,  | nγq | −→ ∞. |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | ------- | --- | --- | ----- | --- |
|     |     | f γ       | M,n | f,γ |     |     | f,γ | f,γ     |     |     | f,γ   |     |
The first pairs are slightly closer than under an optimal packing, but their deterioration is too
small to change the optimal error exponent, and they make unit contributions to the family’s
leading coefficient. The second pairs are farther apart by a larger vanishing amount than under
an optimal packing, so their contributions to the family’s leading coefficient vanish, even though
they become closest pairs in C . Thus an asymptotically negligible worsening of selected pairs
∞
can create enough geometric freedom to suppress the contributions of other pairs to the family’s
leading coefficient. This description assumes that the family’s leading coefficient exists. More
general approach rates may produce fractional pair contributions, so the leading coefficient of an
SNR-dependent family, when it exists, need not be an integer-valued ordered closest-pair count.
If the family attains the optimal leading coefficient, its leading coefficient equals K∗ .
M,n

14
If C were instead held fixed, every one of its ordered closest-pair indices would contribute
∞
|     |     |     |     |     |     | |I  | (C  | )|, |     | Kfix |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
one to its fixed-codebook leading coefficient max ∞ which is at least . For an SNR-
M,n
K∗
dependent family that attains the optimal leading coefficient, the pairwise contributions to
M,n
therefore depend on the family’s approach to the limiting packing, not on the limiting packing
alone.
III. SOFT-PACKING CHARACTERIZATION OPTIMAL LEADING COEFFICIENT
OF THE
The design problem in Subsection II-D first asks whether the normalized SNR-wise optimal
ML error has a finite limit and how that limit can be characterized. This section resolves these
|     |     |     |     |     | (M,n) |     |     | M   | ≥ 2 | ρ∗ < 1. |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ------- | --- |
questions for every fixed finite pair satisfying and We introduce
M,n
a Gaussian soft-packing energy, prove that its minimum is asymptotically equivalent to the
normalized exact ML optimum, and show that this minimum converges to the optimal leading
coefficient K∗ . Comparison with fixed packing-optimal codebooks then gives K∗ ≤ Kfix .
|             | M,n          |     |        |     |     |     |     |     |     | M,n | M,n |
| ----------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| A. Gaussian | Soft-Packing |     | Energy |     |     |     |     |     |     |     |     |
For every codebook C ∈ M, define the Gaussian soft-packing energy as
|     |     |     |     |       | (cid:88) | (cid:110)nγ | (cid:0) |        | (cid:1) (cid:111) |     |      |
| --- | --- | --- | --- | ----- | -------- | ----------- | ------- | ------ | ----------------- | --- | ---- |
|     |     |     | G   | (C) = |          | exp         | ρ       | (C)−ρ∗ |                   | .   | (27) |
|     |     |     |     | γ     |          |             | e       |        |                   |     |      |
|     |     |     |     |       |          |             | 4       |        | M,n               |     |      |
e∈EM
Each exponential term in G (C) distinguishes correlation offsets on the 1/(nγ) scale: an offset
γ
λ/(nγ) produces the finite term exp{λ/4} in G . The Gaussian soft-packing energy also controls
γ
the hard packing objective. Indeed, an ordered pair attaining ρ (C) contributes
max
|     |     |     |     |     | (cid:110)nγ |         |        | (cid:111) |     |     |     |
| --- | --- | --- | --- | --- | ----------- | ------- | ------ | --------- | --- | --- | --- |
|     |     |     |     |     |             | (cid:0) |        | (cid:1)   |     |     |     |
|     |     |     |     | exp |             | ρ       | (C)−ρ∗ |           |     |     |     |
|     |     |     |     |     |             | max     |        | M,n       |     |     |     |
4
| to G (C). | Therefore, | if  | G (C) | ≤ L | for some | L   | ≥ 1, then |     |     |     |     |
| --------- | ---------- | --- | ----- | --- | -------- | --- | --------- | --- | --- | --- | --- |
| γ         |            |     | γ     |     |          |     |           |     |     |     |     |
4logL
(C)−ρ∗
|     |     |     |     | 0   | ≤ ρ |     |     | ≤   | .   |     | (28) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | max |     | M,n | nγ  |     |     |      |
Thus a bounded Gaussian soft-packing energy G (C) forces the worst correlation into the 1/(nγ)-
γ
ρ∗
| scale neighborhood |     | of  | the optimal |     | packing | value |     | .   |     |     |     |
| ------------------ | --- | --- | ----------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
M,n
P∗,
For a fixed packing-optimal codebook C ∈ every e ∈ I (C ) has zero correlation offset
|     |     |     |     |     |     | 0   |     |     | max | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
from ρ∗ and thereby contributes one to G (C ). Every remaining ordered pair has a fixed
| M,n |     |     |     |     |     | γ   | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
negative offset from ρ∗ ; hence its term decays exponentially to zero as γ → ∞. Consequently,
M,n
|     |     |     |     |     | lim G | (C ) | = |I | (C )|. |     |     | (29) |
| --- | --- | --- | --- | --- | ----- | ---- | ---- | ------ | --- | --- | ---- |
|     |     |     |     |     |       | γ 0  | max  | 0      |     |     |      |
γ→∞

15
Thus the limiting Gaussian soft-packing energy of a fixed packing-optimal codebook is exactly
its number of ordered closest-pair indices. We next compare the Gaussian soft-packing energy
with the normalized exact ML error while the codebook is allowed to vary with SNR.
| B. Uniform | Approximation |     |     | of the Exact | ML  | Error |     |     |
| ---------- | ------------- | --- | --- | ------------ | --- | ----- | --- | --- |
C ∈ M
The minimum of the Gaussian soft-packing energy over all codebooks at a fixed SNR
γ is
|     |     |     |     | V   | (M,n) | = minG | (C). | (30) |
| --- | --- | --- | --- | --- | ----- | ------ | ---- | ---- |
|     |     |     |     |     | γ     | γ      |      |      |
C∈M
For each fixed γ, the map C (cid:55)→ G (C) is continuous on the compact codebook space M; hence
γ
the minimum is attained. The quantity V (M,n) plays a crucial role in characterizing the optimal
γ
leading coefficient.
Theorem 1 (Uniform Gaussian soft-packing transfer). Fix finite (M,n) with M ≥ 2 and ρ∗ < 1.
M,n
For every fixed L ≥ 1, there are constants C < ∞ and γ < ∞ such that, for every γ ≥ γ
|           |     |                |     |     |     | L        | L   | L    |
| --------- | --- | -------------- | --- | --- | --- | -------- | --- | ---- |
| and every | C   | ∈ M satisfying |     |     |     |          |     |      |
|           |     |                |     |     | G   | (C) ≤ L, |     | (31) |
γ
we have
|     |     |     |     | (cid:12)  |       | (cid:12)         |     |      |
| --- | --- | --- | --- | --------- | ----- | ---------------- | --- | ---- |
|     |     |     |     | (cid:12)P | (C;γ) | (cid:12)         | C   |      |
|     |     |     |     |           | e     |                  | L   |      |
|     |     |     |     | (cid:12)  |       | −G (C)(cid:12) ≤ | .   | (32) |
|     |     |     |     | (cid:12)  | B∗    | γ (cid:12)       | nγ  |      |
γ
1−ρ∗
The constants may depend on (M,n), L, and the positive separation , but not on C or γ.
M,n
| Proof: | The | proof | is given | in Appendix |     | A.  |     |     |
| ------ | --- | ----- | -------- | ----------- | --- | --- | --- | --- |
Theorem 1 shows that, for every fixed L ≥ 1, the soft-packing energy G (C) uniformly
γ
approximates the normalized exact ML error Pe(C;γ) over all codebooks C ∈ M satisfying
B∗
γ
G (C) ≤ L. Equivalently, an SNR-dependent family is packing-tail competitive precisely when
γ
P (C ;γ)/B∗ = O(1). Later on, cf. Lemma 1, we show that every packing-tail-competitive family
e γ
γ
| eventually | satisfies | such | a fixed | soft-packing |     | energy bound. |     |     |
| ---------- | --------- | ---- | ------- | ------------ | --- | ------------- | --- | --- |
Corollary 1 (Best packing-optimal benchmark). For every fixed finite (M,n) with M ≥ 2 and
ρ∗ < 1,
M,n
Pfix(M,n;γ)
|     |     |     |     | e   | =   | Kfix +O((nγ)−1). |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
(33)
|     |     |     |     | B∗  |     | M,n |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ

16
Proof: For every C ∈ P∗, all correlation offsets from ρ∗ are nonpositive, and hence
0
M,n
| G (C | ) ≤ | M(M −1). |     |     |     |     |     |     | P∗  |     |     |     |
| ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ 0 Applying Theorem 1 uniformly over and then taking minima gives
Pfix(M,n;γ)
|     |     |     |     | e   |     | =   | min | G (C )+O((nγ)−1). |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
γ 0
|     |     |     |     |     | B ∗ |     | C0∈P∗ |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
γ
EveryC ∈ P∗ satisfiesG (C ) ≥ |I (C )| ≥ Kfix .ChooseCfix ∈ P∗ with|I (Cfix)| = Kfix
|     | 0   |     |     | γ 0 | max | 0   |     |     |     | max |     | .   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | M,n | 0   |     | 0   | M,n |
ρ∗
Its remaining ordered pairs, if any, lie a fixed positive correlation gap below . Therefore,
M,n
|     |     |     |     | G   | (Cfix) | = Kfix |     | +O(exp{−cnγ}) |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------ | --- | ------------- | --- | --- | --- | --- |
γ
|     |      |              |     |        | 0     |     | M,n   |     |     |     |     |     |
| --- | ---- | ------------ | --- | ------ | ----- | --- | ----- | --- | --- | --- | --- | --- |
| for | some | c > 0. These | two | bounds | prove |     | (33). |     |     |     |     |     |
Corollary 2 (Finite-SNR equivalence of the optimized exact ML error and Gaussian soft-packing
ρ∗
| energy). | For | every | fixed | finite (M,n) |     | with | M ≥ | 2 and | < 1, |     |     |     |
| -------- | --- | ----- | ----- | ------------ | --- | ---- | --- | ----- | ---- | --- | --- | --- |
M,n
P∗(M,n;γ)
|     |     |     |     | e   |     |     | (M,n)+O((nγ)−1). |     |     |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | =   | V                |     |     |     |     | (34) |
|     |     |     |     |     | B∗  |     | γ                |     |     |     |     |      |
γ
|     | Proof: | The proof | is  | given | in Appendix |     | A.  |     |     |     |     |     |
| --- | ------ | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
The corollary shows that minimizing the normalized exact ML error and minimizing the
soft-packing energy, see (30), produce asymptotically identical optimal normalized values. This
result compares the two optimized values, P∗(M,n;γ)/B∗ and V (M,n), at each sufficiently
γ
|     |     |     |     |     |     |     | e   |     | γ   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
large finite SNR. It does not yet establish the existence of an optimal leading coefficient, because
| it does | not | show that | V   | (M,n) | converges |     | as γ | → ∞. |     |     |     |     |
| ------- | --- | --------- | --- | ----- | --------- | --- | ---- | ---- | --- | --- | --- | --- |
γ
C. Existence and Characterization of the Optimal Leading Coefficient
It remains to prove that V (M,n) has a high-SNR limit. The next theorem establishes this
γ
convergence and transfers the resulting limit to the minimum error probability using Corollary 2.
Theorem 2 (Existence and Gaussian soft-packing energy characterization of the optimal leading
coefficient). For every fixed finite (M,n) with M ≥ 2 and ρ∗ < 1, the finite limits
M,n
|     |     |     |     |     | K∗  | :=  | lim | V (M,n) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
γ
M,n
γ→∞
(35)
P∗(M,n;γ)
e
|     |     |     |     |     |     | =   | lim |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
B∗
γ→∞
γ
K∗
| exist | and | agree. The | common | value, |     |     | , satisfies |     |     |     |     |     |
| ----- | --- | ---------- | ------ | ------ | --- | --- | ----------- | --- | --- | --- | --- | --- |
M,n
|     |     |     |     |     | 2   | ≤ K∗ | ≤   | M(M −1). |     |     |     | (36) |
| --- | --- | --- | --- | --- | --- | ---- | --- | -------- | --- | --- | --- | ---- |
M,n

17
| The globally |     | optimal ML  | error           | obeys     |          |     |            |     |     |      |
| ------------ | --- | ----------- | --------------- | --------- | -------- | --- | ---------- | --- | --- | ---- |
|              |     |             |                 | P∗(M,n;γ) | =        | K∗  | B∗ +o(B∗). |     |     | (37) |
|              |     |             |                 | e         |          | M,n | γ          | γ   |     |      |
| Moreover,    | for | every fixed | packing-optimal |           | codebook |     | C ∈        | P∗, |     |      |
0
K∗
|        |     |       |          |             | ≤   | |I  | (C )|. |     |     | (38) |
| ------ | --- | ----- | -------- | ----------- | --- | --- | ------ | --- | --- | ---- |
|        |     |       |          |             | M,n | max | 0      |     |     |      |
| Proof: | The | proof | is given | in Appendix |     | A.  |        |     |     |      |
The theorem shows that both P∗(M,n;γ)/B∗ and V (M,n) converge to K∗ , and that this
|     |     |     |     | e   |     | γ   | γ   |     | M,n |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
common limit is at most |I (C )| for every fixed packing-optimal codebook C . The scale B∗
|     |     |     |     | max 0 |     |     |     |     | 0   | γ   |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
contains the packing-determined exponential decay and its Gaussian prefactor, while K∗ is the
M,n
| remaining | optimal | leading | coefficient. |     |     |     |     |     |     |     |
| --------- | ------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
The theorem also proves existence of the optimized leading coefficient. Specifically, both
P∗(M,n;γ)/B∗ and V (M,n) converge to K∗ . Consequently, every selection of exact finite-
| e   |     | γ   | γ   |     |     | M,n |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SNR minimizers
|     |     |     |     | C∗  | ∈ argminP |     | (C;γ) |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ----- | --- | --- | --- |
|     |     |     |     | γ   |           |     | e     |     |     |     |
C∈M
has leading coefficient K∗ , even if the selected optimizing codebooks do not themselves
M,n
| converge | as a | family. | Indeed, |          |           |     |     |      |     |     |
| -------- | ---- | ------- | ------- | -------- | --------- | --- | --- | ---- | --- | --- |
|          |      |         |         | P (C∗;γ) | P∗(M,n;γ) |     |     |      |     |     |
|          |      |         |         | e γ      | e         |     |     |      |     |     |
|          |      |         |         |          | =         |     | −→  | K∗ . |     |     |
|          |      |         |         | B∗       |           | B∗  |     | M,n  |     |     |
|          |      |         |         | γ        |           | γ   |     |      |     |     |
The same characterization also identifies a broad class of families attaining the optimal leading
coefficient. Exact minimization of the Gaussian soft-packing energy at every SNR is unnecessary;
a globally vanishing additive objective gap is sufficient, as shown in the following.
Corollary 3 (Near-minimizers of the Gaussian soft-packing energy attain the optimal leading
coefficient). Let {C(cid:98) } ⊂ M and suppose that, for some ε ≥ 0 satisfying ε → 0,
|     |     | γ   |     |       |                |       |     | γ   | γ   |      |
| --- | --- | --- | --- | ----- | -------------- | ----- | --- | --- | --- | ---- |
|     |     |     |     | 0 ≤ G | (C(cid:98) )−V | (M,n) | ≤   | ε . |     | (39) |
|     |     |     |     |       | γ γ            | γ     |     | γ   |     |      |
Then
|     |     |     |     |     | G (C(cid:98) | ) −→ | K∗  | ,   |     |     |
| --- | --- | --- | --- | --- | ------------ | ---- | --- | --- | --- | --- |
|     |     |     |     |     | γ            | γ    | M,n |     |     |     |
(40)
|     |     |     |     | P   | (C(cid:98) ;γ) |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | e γ            |     |     |     |     |     |
|     |     |     |     |     |                | −→  | K∗  | ,   |     |     |
M,n
B∗
γ
and
P (C(cid:98) ;γ)
e γ
|     |     |     |     |     |     |     | −→ 1. |     |     | (41) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- |
P∗(M,n;γ)
e

18
| Proof: | The proof | is given | in  | Appendix | A.  |     |     |
| ------ | --------- | -------- | --- | -------- | --- | --- | --- |
{C(cid:98) } G (C(cid:98) )
Thus, any full SNR-indexed family γ γ whose Gaussian soft-packing energy γ γ is
within an additive o(1) of the global minimum V (M,n) as γ → ∞ attains the optimal leading
γ
coefficient K∗ , even if its codebooks do not minimize the exact ML error at any finite SNR.
M,n
| D. Comparison | With | the Best | Packing-Optimal |     | Benchmark |     |     |
| ------------- | ---- | -------- | --------------- | --- | --------- | --- | --- |
The fixed-codebook comparison can be written directly via the Gaussian soft-packing energy
| function | as  |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- |
K∗
|     |     |     |     | = lim | minG | (C) |     |
| --- | --- | --- | --- | ----- | ---- | --- | --- |
|     |     |     |     | M,n   |      | γ   |     |
γ→∞C∈M
(42)
Kfix
|     |     |     |     | ≤ min | lim | G (C ) = | .   |
| --- | --- | --- | --- | ----- | --- | -------- | --- |
|     |     |     |     |       |     | γ 0      | M,n |
C0∈P∗γ→∞
On the left, the codebook is optimized separately at every SNR before the high-SNR limit is
taken. On the right, a packing-optimal codebook is first held fixed, its limiting number of ordered
closest-pair indices is obtained, and that count is then minimized over P∗. The first procedure
retains the path-dependent pair contributions to the optimal leading coefficient that can arise
under SNR-wise codebook optimization; the second assigns one unit to the fixed codebook’s
leading coefficient for every ordered closest-pair index of that codebook.
| In fact, | (20) gives      |           |      |             |     |     |          |
| -------- | --------------- | --------- | ---- | ----------- | --- | --- | -------- |
|          |                 | P∗(M,n;γ) |      | Pfix(M,n;γ) |     |     |          |
|          |                 |           |      | ≤           |     | for | every γ. |
|          |                 |           | e    |             | e   |     |          |
| Theorem  | 2 and Corollary | 1         | then | give        |     |     |          |
|          |                 |           |      | P∗(M,n;γ)   |     | K∗  |          |
M,n
|     |     |     |     |             | e   | −→   | ,   |
| --- | --- | --- | --- | ----------- | --- | ---- | --- |
|     |     |     |     | Pfix(M,n;γ) |     | Kfix |     |
|     |     |     |     | e           |     |      | M,n |
(43)
Pfix(M,n;γ)−P∗(M,n;γ)
|     |     | e   |     |     | e   | −→ Kfix | −K∗ .   |
| --- | --- | --- | --- | --- | --- | ------- | ------- |
|     |     |     |     | B∗  |     |         | M,n M,n |
γ
Therefore, under the strict coefficient inequality, K∗ < Kfix , the packing-optimal restriction
|     |     |     |     |     |     | M,n | M,n |
| --- | --- | --- | --- | --- | --- | --- | --- |
retains a constant multiplicative disadvantage, and the exact SNR-wise optimal error is strictly
smaller for every sufficiently large SNR. If the coefficients are equal, K∗ = Kfix , the best
M,n M,n
fixed packing-optimal codebook is leading-order optimal, although lower-order differences may
remain.
The limit characterization determines the optimal leading coefficient but does not yet describe
the geometry of the codebook families that can approach it. The next section supplies that
structural description and derives a global variational characterization.

19
|     | IV. | LOCALIZATION |     | SNR-DEPENDENT |     |     | CLOSEST-PAIR |     | CONTRIBUTIONS |     |
| --- | --- | ------------ | --- | ------------- | --- | --- | ------------ | --- | ------------- | --- |
AND
The preceding section identifies the optimal leading coefficient as the high-SNR limit of the
minimum Gaussian soft-packing energy, K∗ = lim V (M,n). This section determines
|     |     |     |     |     |     |     | γ→∞ | γ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M,n
which ordered pairs can have nonvanishing normalized contributions along a family competitive
at the packing-tail scale and how those contributions are determined. The section concludes
by minimizing these contributions over all packing-optimal limiting codebooks and all jointly
| feasible        | scaled | closest-pair |              | offsets. |       |     |     |     |     |     |
| --------------- | ------ | ------------ | ------------ | -------- | ----- | --- | --- | --- | --- | --- |
| A. Localization |        | at the       | Packing-Tail |          | Scale |     |     |     |     |     |
Here and below, dist(C,P∗) is induced by the product Euclidean metric on the labeled tuples
in M.
Lemma 1 (Localization at the packing-tail scale). Let {C } ⊂ M satisfy
γ
|     |     |     |     |     | P (C ;γ) |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
e γ
|     |     |     |     |     |     | =   | O(1). |     |     | (44) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- |
B∗
γ
Then
|     |     |     |     | ρ   | (C )−ρ∗ | =   | O((nγ)−1), |     |     | (45) |
| --- | --- | --- | --- | --- | ------- | --- | ---------- | --- | --- | ---- |
|     |     |     |     | max | γ       | M,n |            |     |     |      |
,P∗)
|     |     |     |     | G (C ) = | O(1), | dist(C |     | −→  | 0.  | (46) |
| --- | --- | --- | --- | -------- | ----- | ------ | --- | --- | --- | ---- |
|     |     |     |     | γ γ      |       |        | γ   |     |     |      |
K∗
If the family additionally attains the optimal leading coefficient in the sense of (22) and <
M,n
Kfix
, then
M,n
|     |     |     |     | C ∈/ P∗ | for all | sufficiently |     | large γ. |     | (47) |
| --- | --- | --- | --- | ------- | ------- | ------------ | --- | -------- | --- | ---- |
γ
|     | Proof: | The proof | is given | in Appendix |     | B.  |     |     |     |     |
| --- | ------ | --------- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
Lemma 1 shows that any packing-tail-competitive codebook family must enter an increasingly
small neighborhood of the packing-optimal set. Indeed, define the excess maximal correlation as
|     |     | )−ρ∗ |     |     |     |     |     |     |     | B∗, |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
δ = ρ (C . If δ > 0, then the single-pair Gaussian-tail scale, normalized by grows
| γ   | max | γ M,n | γ   |     |     |     |     |     |     | γ   |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:110) (cid:111)
nγδγ
essentially as exp . Consequently, bounded normalized error is possible only if (45) holds.
4
Thus, the maximal correlation must be within O((nγ)−1) of ρ∗ , which is the critical correlation
M,n
scale governing pairwise contributions to a family’s leading coefficient, whenever that coefficient
exists. The lemma also establishes the geometric localization dist(C ,P∗) −→ 0. Hence, the
γ
family may continue to rotate, relabel its codewords, or move among different packing-optimal
P∗
configurations while its distance from tends to zero as the SNR grows.

20
The lemma also reveals the geometric mechanism by which the optimal leading coefficient
K∗ < Kfix
can be smaller than the best fixed-codebook leading coefficient. If , then a family
|     |     |     |     |     |     |     |     |     | M,n | M,n |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P∗
attaining the optimal leading coefficient must lie outside for every sufficiently large γ. Instead,
it approaches P∗ from outside. Such a family accepts a vanishing increase in its maximal
correlation, confined to the 1/(nγ) scale, in order to reduce or suppress the contributions to
K∗ made by other pairs that are closest in a packing-optimal subsequential limit. Therefore,
M,n
such a family may consist of codebooks that are slightly worse as packings at every sufficiently
large finite SNR and nevertheless have a strictly smaller leading coefficient than every fixed
| packing-optimal |     | codebook.  |     |          |            |         |     |     |     |         |     |
| --------------- | --- | ---------- | --- | -------- | ---------- | ------- | --- | --- | --- | ------- | --- |
| B. Reduction    |     | to Closest |     | Pairs of | a Limiting | Packing |     |     |     |         |     |
|                 |     |            |     |          |            |         |     | γ,  | C → | C ∈ P∗. | C   |
Consider a convergent subsequence, reindexed by for which γ ∞ Thus ∞
is a packing-optimal subsequential limit of the family. For each e ∈ I (C ), use the signed
max ∞
| correlation | offset | from | (24), |     |     |        |      |     |     |     |     |
| ----------- | ------ | ---- | ----- | --- | --- | ------ | ---- | --- | --- | --- | --- |
|             |        |      |       |     | ∆   | = ρ (C | )−ρ∗ | .   |     |     |     |
|             |        |      |       |     | e,γ | e      | γ    | M,n |     |     |     |
A positive offset worsens that ordered pair relative to the packing value, whereas a negative
| offset improves |     | it. |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theorem 3 (Reduction to closest pairs of a limiting packing). Let C → C ∈ P∗, and suppose
γ ∞
that, for some finite L ≥ 1, G (C ) ≤ L for all sufficiently large γ. Then, for all sufficiently large
|     |     |     |     | γ   | γ   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ,
4logL
)−ρ∗
|     |     |     | 0   | ≤ ρ | (C  | =   | max | ∆ ≤ | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | max | γ   | M,n |     | e,γ | nγ  |     |     |
e∈Imax(C∞)
| Moreover, | for | some | c > 0, |     |          |          |     |                |     |     |      |
| --------- | --- | ---- | ------ | --- | -------- | -------- | --- | -------------- | --- | --- | ---- |
|           |     |      |        |     |          | (cid:26) |     | (cid:27)       |     |     |      |
|           |     |      |        |     | (cid:88) | nγ∆      |     |                |     |     |      |
|           |     |      | G (C   | ) = |          | exp      | e,γ | +O(exp{−cnγ}), |     |     | (48) |
|           |     |      | γ      | γ   |          |          |     |                |     |     |      |
4
e∈Imax(C∞)
|     |     |     |     |      |     |            |     | (cid:26) | (cid:27) |     |      |
| --- | --- | --- | --- | ---- | --- | ---------- | --- | -------- | -------- | --- | ---- |
|     |     |     |     | P (C | ;γ) | (cid:88)   |     | nγ∆      |          |     |      |
|     |     |     |     | e    | γ   |            |     | e,γ      |          |     |      |
|     |     |     |     |      | =   |            | exp |          |          |     |      |
|     |     |     |     |      | B∗  |            |     | 4        |          |     |      |
|     |     |     |     |      | γ   | e∈Imax(C∞) |     |          |          |     | (49) |
+O((nγ)−1).
| Proof: | The | proof | is  | given in | Appendix | B.  |     |     |     |     |     |
| ------ | --- | ----- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
Theorem 3 shows that, for a packing-tail-competitive codebook family that converges to
an optimal packing, not all ordered codeword pairs can contribute to the normalized error

21
P (C ;γ)/B∗. The limiting packing restricts the ordered pairs that can contribute to the normalized
e γ
γ
e
error to those that are closest pairs in the limiting optimal packing. Indeed, if an ordered pair is
ρ∗
not in I (C ), then, for some fixed η > 0, ρ (C ) = −η . Because C → C , this pair
|     | max | ∞   |     |     | e   | e ∞ | M,n e | γ ∞ |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
retains a strict correlation gap for all sufficiently large γ. Therefore, its Gaussian soft-packing
energy term is bounded by an exponentially vanishing quantity of the form exp{−nγη /8}, and
e
its contribution to the normalized error vanishes. For an ordered pair that is closest in the limiting
packing, i.e., e ∈ I (C ), by contrast, ρ (C ) = ρ∗ , so there is no fixed correlation gap
|     |     | max | ∞   |     | e   | ∞   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M,n
that makes its contribution to the normalized error vanish. Instead, its finite-SNR displacement
)−ρ∗
∆ = ρ (C enters the normalized error through the term exp{nγ∆ /4}. Consequently,
| e,γ         | e   | γ M,n   |                |     |                |     |     | e,γ |     |
| ----------- | --- | ------- | -------------- | --- | -------------- | --- | --- | --- | --- |
| the theorem |     | reduces | the normalized |     | error to (49). |     |     |     |     |
Ordinary geometric convergence determines the set of potentially relevant closest pairs but
does not determine each contribution in this sum. It gives only ∆ → 0, whereas the limiting
e,γ
normalized error along a subsequence depends on the finer quantities nγ∆ . Thus, different
e,γ
SNR-dependent approaches to the same optimal packing can yield different subsequential limits of
the normalized error. The limiting codebook is the common destination, whereas the approach to
that destination on the 1/(nγ) correlation scale determines each limiting closest pair’s normalized
contribution along the selected subsequence. The following corollary makes these contributions
| explicit | when | the scaled | offsets | have | limits. |     |     |     |     |
| -------- | ---- | ---------- | ------- | ---- | ------- | --- | --- | --- | --- |
Corollary 4 (Subsequential closest-pair contribution formula). Under the assumptions of Theo-
rem 3, since I (C ) is finite and a bounded Gaussian soft-packing energy precludes any scaled
|     |     | max ∞ |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
offset from diverging to +∞, there exists a further subsequence, without changing notation, such
that
|     |     |     |     | nγ∆ | −→ λ , | e ∈ I | (C ), |     | (50) |
| --- | --- | --- | --- | --- | ------ | ----- | ----- | --- | ---- |
|     |     |     |     | e,γ | e      | max   | ∞     |     |      |
R∪{−∞},
simultaneously for some λ ∈ where exp{−∞} = 0. Along this subsequence,
e
(cid:88)
|     |     |     |     | G (C | ) −→ | exp{λ | /4}, |     |      |
| --- | --- | --- | --- | ---- | ---- | ----- | ---- | --- | ---- |
|     |     |     |     | γ    | γ    |       | e    |     | (51) |
e∈Imax(C∞)
|     |     |     |     | P (C ;γ) |     | (cid:88) |      |     |      |
| --- | --- | --- | --- | -------- | --- | -------- | ---- | --- | ---- |
|     |     |     |     | e γ      | −→  | exp{λ    | /4}. |     |      |
|     |     |     |     |          |     |          | e    |     | (52) |
B∗
γ
e∈Imax(C∞)
If the family attains the optimal leading coefficient in the sense of (22), then
(cid:88)
|     |     |     |     | K∗  | =   | exp{λ | /4}. |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- |
|     |     |     |     | M,n |     |       | e    |     |     |
e∈Imax(C∞)

22
For the constant family C ≡ C , every e ∈ I (C ) has ∆ = 0 and therefore contributes
γ ∞ max ∞ e,γ
one to both limiting sums. Hence,
lim G (C ) = lim P e (C ∞ ;γ) = (cid:12) (cid:12)I (C ) (cid:12) (cid:12) ≥ Kfix .
γ→∞ γ ∞ γ→∞ B∗ max ∞ M,n
γ
Thus, a fixed packing-optimal codebook has a leading coefficient equal to its number of ordered
closest-pair indices; this coefficient equals K∗ precisely when that constant family attains the
M,n
optimal leading coefficient.
Proof: Equations (48) and (49) give the two displayed limits. Bounded Gaussian soft-packing
energy gives nγ∆ ≤ 4logL for every e ∈ I (C ). The extended interval [−∞,4logL]
e,γ max ∞
is compact, and the set I (C ) is finite, so a common convergent subsequence exists. The
max ∞
attainment conclusion follows from (22). The constant-family conclusion follows from ∆ ≡ 0
e,γ
and (16).
Corollary4convertsthescaledcorrelationoffsetofeachlimitingclosestpairintoitscontribution
exp{λ /4} to the limiting normalized error along that subsequence. If the full family has a
e
leading coefficient, these contributions sum to that coefficient. If the family attains the optimal
leading coefficient, their sum is K∗ .
M,n
A fixed packing-optimal codebook provides the simplest special case. If C = C , then every
γ ∞
ordered closest-pair index has zero offset, so that λ = 0 and exp{λ /4} = 1. Its leading
e e
coefficient is therefore the number of ordered closest-pair indices. For an SNR-dependent family,
however, ordinary convergence still makes every such offset tend to zero, but multiplication by nγ
reveals differences that remain visible after normalization by B∗. In particular, if nγ∆ −→ λ ,
γ e,γ e
the limiting pair contribution has one of the following forms:
scaled-offset behavior limiting pair contribution
λ = −∞ exp{λ /4} = 0,
e e
−∞ < λ < 0 0 < exp{λ /4} < 1,
e e
λ = 0 exp{λ /4} = 1,
e e
λ > 0 exp{λ /4} > 1.
e e
For a family attaining the optimal leading coefficient, these are the corresponding contributions
to K∗ . Consequently, a pair that is closest in the limiting codebook may have a zero, fractional,
M,n
unit, or greater-than-unit contribution, depending on the 1/(nγ)-scale path by which the codebook
approaches the limiting packing.

23
C. Global Variational Characterization by Scaled Closest-Pair Offsets
Corollary 4 evaluates one specified SNR-dependent family. To characterize the global optimum,
the feasible subsequential scaled offsets must be considered jointly over every packing-optimal
limit.
P∗,
| For C | ∈ let | L(C | ) denote | the  | set | of all | vectors       |                 |     |     |     |
| ----- | ----- | --- | -------- | ---- | --- | ------ | ------------- | --------------- | --- | --- | --- |
|       | 0     |     | 0        |      |     |        |               |                 |     |     |     |
|       |       |     | λ =      | (λ ) |     | ∈      | (cid:0)R∪{−∞} | (cid:1)Imax(C0) |     |     |     |
e
e∈Imax(C0)
for which there exist SNRs γ → ∞ and codebooks C ∈ M satisfying
|     |     |     |         | j    |         |      | j      |      |      |       |      |
| --- | --- | --- | ------- | ---- | ------- | ---- | ------ | ---- | ---- | ----- | ---- |
|     |     |     |         |      | C       | −→ C | , supG | (C ) | < ∞, |       |      |
|     |     |     |         |      | j       |      | 0      | γj j |      |       |      |
|     |     |     |         |      |         |      | j      |      |      |       | (53) |
|     |     |     | (cid:0) |      | (cid:1) |      |        |      |      |       |      |
|     |     | nγ  | ρ (C    | )−ρ∗ |         | −→ λ | ,      | e    | ∈ I  | (C ). |      |
|     |     |     | j e     | j    | M,n     |      | e      |      | max  | 0     |      |
We call λ admissible scaled closest-pair-offset data at C . The bounded Gaussian soft-packing
0
energy condition excludes +∞ as a component limit, whereas −∞ is retained and gives the
limiting pair weight exp{−∞} = 0. The constant sequence C ≡ C shows that L(C ) is nonempty.
j 0 0
Proposition 2 (Global variational characterization by scaled closest-pair offsets). For every fixed
| finite (M,n) | with | M ≥ | 2 and | ρ∗  | < 1, |     |     |     |     |     |     |
| ------------ | ---- | --- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- |
M,n
(cid:88)
|     |     |     |     | K∗  | = min |     | exp{λ | /4}. |     |     | (54) |
| --- | --- | --- | --- | --- | ----- | --- | ----- | ---- | --- | --- | ---- |
|     |     |     |     | M,n |       |     |       | e    |     |     |      |
C0∈P∗
λ∈L(C0)e∈Imax(C0)
The minimum in (54) is attained. Moreover, every sequence witnessing a minimizing pair (C ,λ)
0
| satisfies, | along its | SNR  | sequence, |     |      |      |       |     |          |       |     |
| ---------- | --------- | ---- | --------- | --- | ---- | ---- | ----- | --- | -------- | ----- | --- |
|            |           |      |           |     | P (C | ;γ ) |       |     | P (C     | ;γ )  |     |
|            |           |      |           |     | e    | j j  |       |     | e        | j j   |     |
|            | G (C      | ) −→ | K∗        | ,   |      |      | −→ K∗ | ,   |          | −→ 1. |     |
|            | γj        | j    | M,n       |     |      |      | M,n   |     |          |       |     |
|            |           |      |           |     | B∗   |      |       |     | P∗(M,n;γ | )     |     |
|            |           |      |           |     |      | γj   |       |     | e        | j     |     |
Proof:
|     | The proof |     | is given | in Appendix |     | B.  |     |     |     |     |     |
| --- | --------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
The proposition minimizes over every packing-optimal limiting codebook and every jointly
feasible set of scaled offsets. The limiting packing fixes the ordered pairs in the sum, while the
offsets determine their limiting weights. A constant packing has λ = 0 at every ordered closest-
e
pair index and therefore recovers the ordinary closest-pair count. The joint-feasibility condition
is essential: the scaled offsets must arise simultaneously from one feasible codebook sequence
and therefore cannot be optimized independently. The characterization of K∗ is exact but
M,n
generally implicit because the admissible sets L(C ) need not admit tractable finite-dimensional
0
descriptions.

24
|     | V.  | LEADING-COEFFICIENT |     |     |     | EXTRACTION |     |     | MATCHING |     | BOUNDS |     |
| --- | --- | ------------------- | --- | --- | --- | ---------- | --- | --- | -------- | --- | ------ | --- |
BY
The preceding sections establish the existence of K∗ and characterize the closest-pair
M,n
contributions that can produce it. To determine K∗ in closed form, the applications below use
M,n
| a direct | matching-bounds |     | argument. |     | Specifically, |     |     | since    |     |     |     |     |
| -------- | --------------- | --- | --------- | --- | ------------- | --- | --- | -------- | --- | --- | --- | --- |
|          |                 |     |           |     | K∗            | =   | lim | V (M,n), |     |     |     |     |
γ
|     |     |     |     |     | M,n |     | γ→∞ |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
it is enough to identify a candidate value K, prove the global lower bound liminf V (M,n) ≥
|     |     |     |     |     |     |     |     |     |     |     | γ→∞ γ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
K, and construct a full SNR-indexed family whose Gaussian soft-packing energy has limiting
upper bound at most K. The following corollary then identifies K as the optimal leading
coefficient, transfers the equality to the exact SNR-wise optimized ML error, and certifies the
| constructed | family. |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Corollary 5 (Optimal leading-coefficient extraction by matching bounds). Fix a finite pair (M,n)
| with M | ≥ 2 and | ρ∗  | < 1, | and | let K | ∈ [2,M(M |     | −1)]. | Suppose | that |     |     |
| ------ | ------- | --- | ---- | --- | ----- | -------- | --- | ----- | ------- | ---- | --- | --- |
M,n
|     |     |     |     |     | liminfV |     | (M,n) | ≥ K, |     |     |     | (55) |
| --- | --- | --- | --- | --- | ------- | --- | ----- | ---- | --- | --- | --- | ---- |
γ
γ→∞
and that there is an SNR-indexed family, defined for every sufficiently large γ, {C } ⊂ M
γ
satisfying
|     |     |     |     |     | limsupG |     | (C  | ) ≤ K. |     |     |     | (56) |
| --- | --- | --- | --- | --- | ------- | --- | --- | ------ | --- | --- | --- | ---- |
γ γ
γ→∞
Then
|         |             |     |        |           |            |           |         |           | (cid:0) |       | (cid:1) |      |
| ------- | ----------- | --- | ------ | --------- | ---------- | --------- | ------- | --------- | ------- | ----- | ------- | ---- |
|         |             |     | K∗     | =         | K,         | P∗(M,n;γ) |         | = B∗      | K       | +o(1) | ,       | (57) |
|         |             |     | M,n    |           |            | e         |         |           | γ       |       |         |      |
| and the | constructed |     | family | satisfies |            |           |         |           |         |       |         |      |
|         |             |     |        |           |            |           |         |           | P (C    | ;γ)   |         |      |
|         |             |     |        |           | B∗ (cid:0) |           | (cid:1) |           | e γ     |       |         |      |
|         |             |     | P (C   | ;γ) =     |            | K +o(1)   | ,       |           |         | →     | 1.      | (58) |
|         |             |     | e      | γ         | γ          |           |         | P∗(M,n;γ) |         |       |         |      |
e
| Proof: | Since | V   | (M,n) | ≤ G | (C ), |           |     |       |     |     |     |     |
| ------ | ----- | --- | ----- | --- | ----- | --------- | --- | ----- | --- | --- | --- | --- |
|        |       | γ   |       | γ   | γ     |           |     |       |     |     |     |     |
|        |       |     |       |     | K     | ≤ liminfV |     | (M,n) |     |     |     |     |
γ
γ→∞
|     |     |     |     |     |     | ≤ limsupV |     | (M,n) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
γ
γ→∞
|     |     |     |     |     |     | ≤ limsupG |     | (C ) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---- | --- | --- | --- | --- |
γ γ
γ→∞
≤ K.

25
Thus V (M,n) → K, and Theorem 2 gives K∗ = K and the optimal leading-order expansion.
γ
M,n
|     | V (M,n) | ≤ G (C | )   | liminf | G (C | ) ≥ K, |
| --- | ------- | ------ | --- | ------ | ---- | ------ |
Moreover, γ γ γ gives γ→∞ γ γ while (56) gives the reverse upper
limit. Hence G (C ) → K. This convergence places the family in a fixed bounded-energy sublevel
γ γ
of G , so Theorem 1 yields P (C ;γ)/B∗ = K +o(1). Together with the optimal leading-order
|           | γ   |             | e          | γ γ                |     |                |
| --------- | --- | ----------- | ---------- | ------------------ | --- | -------------- |
| expansion | and | K ≥ 2, this | also gives | the relative-error |     | limit in (58). |
The lower bound in (55) is the converse: it controls every SNR-dependent codebook family
through the global minimum V (M,n). The upper bound in (56) is achievability: one feasible
γ
family reaches the same value. Once the two bounds match, Corollary 5 and the uniform transfer
in Theorem 1 give both the exact SNR-wise optimized ML expansion and attainment of the
| optimal | leading | coefficient. |     |     |     |     |
| ------- | ------- | ------------ | --- | --- | --- | --- |
Accordingly, determining the optimal leading coefficient K∗ by matching bounds consists
M,n
| of  | three steps: |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- |
ρ∗ B∗,
1) Determine the optimal packing correlation , which fixes the universal tail scale
M,n γ
|     | and identify | a candidate     | value | K.      |       |      |
| --- | ------------ | --------------- | ----- | ------- | ----- | ---- |
|     | 2) Prove the | global converse |       |         |       |      |
|     |              |                 |       | liminfV | (M,n) | ≥ K. |
γ
γ→∞
This may follow from a direct inequality valid for every feasible codebook or from
|     | localization | followed | by a | problem-specific | geometric | argument. |
| --- | ------------ | -------- | ---- | ---------------- | --------- | --------- |
3) Construct a feasible codebook family, defined for every sufficiently large γ, such that
|     |     |     |     | limsupG | (C  | ) ≤ K. |
| --- | --- | --- | --- | ------- | --- | ------ |
γ γ
γ→∞
Corollary 5 then proves K∗ = K, the exact SNR-wise optimized ML expansion, and
M,n
|     | relative-error | attainment | of  | the constructed | family. |     |
| --- | -------------- | ---------- | --- | --------------- | ------- | --- |
The next two sections apply this three-step matching-bounds framework to the simplex and
| orthoplex-bound |     | ranges. |     |     |     |     |
| --------------- | --- | ------- | --- | --- | --- | --- |
VI. APPLICATION TO THE SIMPLEX CODES: EXACT OPTIMAL LEADING COEFFICIENTS
This section applies the matching-bounds framework to 2 ≤ M ≤ n+1. The simplex bound
in [4] fixes the packing scale, and a global Jensen inequality solves the soft-packing energy
optimization at every positive SNR. The resulting optimal leading coefficient is determined exactly,
is attained by a fixed regular simplex, and cannot be improved by SNR-dependent motion.

26
Fix integers n ≥ 1 and 2 ≤ M ≤ n+1, and let C be an embedded regular (M−1)-simplex
simp
Sn−1.
| in  | This | bound gives |     |     |     |     |     |     |     |     |     |
| --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
ρ∗
|     |     |     |     |     |     | =   | −   | ,   |     |     | (59) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | M,n | M   | −1  |     |     |      |
with equality only for an embedded regular simplex, up to an orthogonal transformation and
| relabeling | [4]. | Substitution |     | in (14) | fixes         | the packing-tail |     | scale | as  |     |      |
| ---------- | ---- | ------------ | --- | ------- | ------------- | ---------------- | --- | ----- | --- | --- | ---- |
|            |      |              |     |         | exp{−nγM/[4(M |                  |     | −1)]} |     |     |      |
|            |      |              |     | B∗      | =             |                  |     |       | .   |     | (60) |
(cid:112)
|     |     |     |     |     | γ M | πnγM/(M |     | −1) |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Here the finite-SNR Gaussian soft-packing energy optimization can be solved exactly. The
following proposition gives the global minimum and identifies all minimizers.
Proposition 3 (Exact soft-packing energy minimum in the simplex range). For all integers n ≥ 1
| and 2 | ≤ M ≤ | n+1, and | every | γ       | > 0, |      |      |       |      |     |      |
| ----- | ----- | -------- | ----- | ------- | ---- | ---- | ---- | ----- | ---- | --- | ---- |
|       |       |          |       | V (M,n) | =    | G (C | )    | = M(M | −1). |     | (61) |
|       |       |          |       | γ       |      | γ    | simp |       |      |     |      |
Moreover, the minimizers are exactly the embedded regular (M −1)-simplices, up to orthogonal
| transformations |     | and relabeling. |          |     |          |     |     |     |     |     |     |
| --------------- | --- | --------------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
| Proof:          | The | proof           | is given | in  | Appendix | C.  |     |     |     |     |     |
The proposition is stronger than a high-SNR statement: an embedded regular simplex globally
minimizes the Gaussian soft-packing energy for every γ > 0. Consequently, no finite-SNR
deformation, including one that varies with γ, can lower the Gaussian soft-packing energy
| minimum | below | the simplex |     | value. |     |     |     |     |     |     |     |
| ------- | ----- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Corollary 6 (Optimal leading coefficient in the simplex range). For every fixed pair (M,n)
| satisfying | 2 ≤ | M ≤ n+1, |     |     |      |      |       |      |     |     |      |
| ---------- | --- | -------- | --- | --- | ---- | ---- | ----- | ---- | --- | --- | ---- |
|            |     |          |     |     | K∗ = | Kfix | = M(M | −1), |     |     | (62) |
|            |     |          |     |     | M,n  | M,n  |       |      |     |     |      |
and
|              |     |           |     |         | (cid:0) |          |           | (cid:1) |          |         |      |
| ------------ | --- | --------- | --- | ------- | ------- | -------- | --------- | ------- | -------- | ------- | ---- |
|              |     | P∗(M,n;γ) |     | =       | B∗ M(M  | −1)+o(1) |           |         |          |         |      |
|              |     | e         |     |         | γ       |          |           |         |          |         |      |
|              |     |           |     |         | −1)3/2  |          | (cid:26)  |         | (cid:27) |         | (63) |
|              |     |           |     |         | (M      |          |           | nγM     | (cid:0)  | (cid:1) |      |
|              |     |           |     | =       | √       |          | exp −     |         | 1+o(1)   | .       |      |
|              |     |           |     |         | πnγM    |          |           | 4(M −1) |          |         |      |
| The constant |     | family C  | ≡ C | attains | K∗      | and      | satisfies |         |          |         |      |
|              |     | γ         |     | simp    |         | M,n      |           |         |          |         |      |
|              |     |           |     |         | P       | (C       | ;γ)       |         |          |         |      |
e simp
|     |     |     |     |     |     |     | −→  | 1.  |     |     | (64) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
P∗(M,n;γ)
e

27
Proof: Proposition 3 gives the global lower bound (55) and, through the constant simplex
|     |     |     |     |     |     |     | K = M(M | −1). |     | K∗ = |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --- | ---- |
family, the matching upper bound (56), both with Corollary 5 gives
M,n
M(M − 1) and attainment of the optimal leading coefficient; substitution of (60) gives (63).
Packing uniqueness and the fact that every ordered pair of distinct simplex vertices is a closest-pair
index give Kfix = M(M −1), completing (62). The relative-error assertion then follows from
M,n
| attainment | of the | optimal | leading | coefficient. |     |     |     |     |     |     |
| ---------- | ------ | ------- | ------- | ------------ | --- | --- | --- | --- | --- | --- |
Corollary 6 completely resolves the SNR-wise optimized high-SNR problem in the simplex
range. The optimal and best fixed-codebook leading coefficients coincide, and the constant
simplex family attains the optimal leading coefficient; SNR-dependent motion therefore gives
no leading-order gain. Proposition 3 establishes exact finite-SNR optimality for the Gaussian
soft-packing energy, while the conclusion for the exact ML error follows asymptotically through
uniform transfer. Independently, the recent resolution of the Weak Simplex Conjecture in [14,
Cors. 2.5–2.6] proves the stronger statement that an embedded regular (M−1)-simplex minimizes
the exact average ML error at every positive SNR in this entire cardinality range. That external
result is consistent with, but is not needed for, the leading-coefficient derivation above.
|       |         | VII.         | APPLICATION |     | TO              | THE | ORTHOPLEX-BOUND |     | RANGE |      |
| ----- | ------- | ------------ | ----------- | --- | --------------- | --- | --------------- | --- | ----- | ---- |
| Fix n | ≥ 2 and | parameterize |             | the | orthoplex-bound |     | range by        |     |       |      |
|       |         |              |             | M   | = n+k,          |     | 2 ≤ k ≤         | n,  |       | (65) |
so that n + 2 ≤ M ≤ 2n. This section first determines the packing scale and the best fixed-
codebook leading coefficient Kfix . It then constructs a strictly improving SNR-dependent family
n+k,n
for every 2 ≤ k < n, obtains an achievability bound K∗ ≤ 4k(k −1), determines K∗
|     |     |     |     |     |     |     | n+k,n |     |     | n+k,n |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- |
exactly at k = 2 and k = n, and isolates the remaining intermediate equality as a conjecture.
| A. Packing | Scale | and | Best Fixed-Codebook |     |     | Leading | Coefficient |     |     |     |
| ---------- | ----- | --- | ------------------- | --- | --- | ------- | ----------- | --- | --- | --- |
Theorthoplexboundin[4]givesρ∗ ≥ 0wheneverM > n+1.Conversely,sinceM = n+k ≤
M,n
2n, any M vertices of the cross-polytope {±e ,...,±e } have all off-diagonal correlations in
|     |     |     |     |     |     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{−1,0}.
|     | Hence, | throughout | the | range, |     |     |     |     |     |     |
| --- | ------ | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
ρ∗
|     |     |     |     |     |     |     | = 0. |     |     | (66) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- |
n+k,n
| Substitution | in  | (14) gives | the | packing-tail |     | scale |     |     |     |     |
| ------------ | --- | ---------- | --- | ------------ | --- | ----- | --- | --- | --- | --- |
exp{−nγ/4}
|     |     |     |     |     | B∗ = |     | √ √ . |     |     | (67) |
| --- | --- | --- | --- | --- | ---- | --- | ----- | --- | --- | ---- |
γ
|     |     |     |     |     |     | (n+k) | nγ π |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- |

28
Proposition 4 (Best fixed-codebook leading coefficient in the orthoplex-bound range). For every
| fixed n ≥ | 2 and 2 ≤ | k ≤ n, |     |     |     |     |     |     |     |
| --------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Kfix
|     |     |     |     |     | = 4n(k | −1). |     |     | (68) |
| --- | --- | --- | --- | --- | ------ | ---- | --- | --- | ---- |
n+k,n
Equality is attained by the orthogonal union of k−1 antipodal pairs and a regular (n−k+1)-
simplex, the latter having n−k+2 vertices in the remaining (n−k+1)-dimensional subspace.
| Proof: | The proof | is given | in  | Appendix | C.  |     |     |     |     |
| ------ | --------- | -------- | --- | -------- | --- | --- | --- | --- | --- |
Proposition 4 determines the smallest leading coefficient obtainable by holding one packing-
optimal codebook fixed. The stated orthogonal union attains the minimum ordered closest-pair-
index count 4n(k −1). This is the benchmark for measuring the benefit of SNR-wise codebook
| optimization,       | developed | below.       |     |        |         |     |     |     |     |
| ------------------- | --------- | ------------ | --- | ------ | ------- | --- | --- | --- | --- |
| B. An SNR-Dependent |           | Construction |     | for    | 2 ≤ k < | n   |     |     |     |
| For every           | fixed n   | ≥ 3 and      | 2 ≤ | k < n, | put     |     |     |     |     |
log(nγ)
|     |     |     | d   | = n−k, |     | q = | .   |     | (69) |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | ---- |
γ
nγ
The closest-pair contribution formula in Corollary 4 suggests this choice because it separates the
two scales
|     |     |     |     | 1   |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | ≪ q | ≪ √ | .   |     |     |
γ
|     |     |     |     | nγ  |     | nγ  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
q
Thus correlations lowered by order γ produce zero limiting weights in the Gaussian soft-packing
q2
energy, whereas correlations worsened by order produce unit limiting weights.
γ
Rn,
For all sufficiently large γ, choose unit vectors a ,...,a in a d-dimensional subspace U ⊂
|              |      |         |             |     |          | 1      | d         |     |      |
| ------------ | ---- | ------- | ----------- | --- | -------- | ------ | --------- | --- | ---- |
| continuously | in q | from an | orthonormal |     | basis at | q = 0, | such that |     |      |
|              | γ    |         |             |     |          | γ      |           |     |      |
|              |      |         |             | aTa | = −q     | , i ̸= | j.        |     | (70) |
|              |      |         |             | j   | γ        |        |           |     |      |
i
Define
|     |     |     |     |       | q   |          | d   |     |     |
| --- | --- | --- | --- | ----- | --- | -------- | --- | --- | --- |
|     |     |     |     |       | γ   | (cid:88) |     |     |     |
|     |     |     |     | v = − |     |          | a , |     |     |
|     |     |     |     | γ     |     |          | j   |     |     |
1−(d−1)q
γ j=1
|     |     |     |     |        |      | dq2 |     |     | (71) |
| --- | --- | --- | --- | ------ | ---- | --- | --- | --- | ---- |
|     |     |     |     | p = ∥v | ∥2 = | γ   | ,   |     |      |
|     |     |     |     | γ      | γ    |     |     |     |      |
1−(d−1)q
γ
(cid:112)
|              |      |                   |      | r =   | 1−p .  |           |        |     |      |
| ------------ | ---- | ----------------- | ---- | ----- | ------ | --------- | ------ | --- | ---- |
|              |      |                   |      | γ     | γ      |           |        |     |      |
| Let f ,...,f | be a | fixed orthonormal |      | basis | of U⊥, | and       | set    |     |      |
| 1            | k    |                   |      |       |        |           |        |     |      |
|              |      | C                 | = {v | ±r f  | : 1 ≤  | i ≤ k}∪{a | ,...,a | }.  | (72) |
|              |      | γ                 |      | γ γ   | i      |           | 1      | d   |      |

29
Proposition 5 (Multiscale achievability in the nonterminal orthoplex-bound range). For every
fixed n ≥ 3 and 2 ≤ k < n, the vectors in and the codebook in exist for all sufficiently
|     |     |     |     |     | (70) |     |     | (72) |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- |
large γ. The codebook is feasible, has n+k points, and converges to a deleted cross-polytope
having both signs on k axes and one sign on each of the remaining d = n−k axes. Its maximal
| correlation | is p , and | its Gaussian |     | soft-packing |     | energy | is  |     |     |
| ----------- | ---------- | ------------ | --- | ------------ | --- | ------ | --- | --- | --- |
γ
|     |     |     | G (C | ) = 4k(k     | −1)exp{nγp |        | /4} |     |      |
| --- | --- | --- | ---- | ------------ | ---------- | ------ | --- | --- | ---- |
|     |     |     | γ    | γ            |            |        | γ   |     |      |
|     |     |     |      | +2kexp{nγ(2p |            | −1)/4} |     |     | (73) |
γ
|     |     |     |     | +d(d+4k |     | −1)exp{−nγq |     | /4}. |     |
| --- | --- | --- | --- | ------- | --- | ----------- | --- | ---- | --- |
γ
Moreover,
|     |     |     |     | nγq = | log(nγ) | −→ ∞, |     |     |     |
| --- | --- | --- | --- | ----- | ------- | ----- | --- | --- | --- |
γ
(74)
|     |     |     |     |       | (cid:18) | [log(nγ)]2(cid:19) |     |     |     |
| --- | --- | --- | --- | ----- | -------- | ------------------ | --- | --- | --- |
|     |     |     |     | nγp = | O        |                    | −→  | 0.  |     |
γ
nγ
Consequently,
|     |     |     |     | G   | (C ) −→ | 4k(k −1). |     |     | (75) |
| --- | --- | --- | --- | --- | ------- | --------- | --- | --- | ---- |
|     |     |     |     | γ   | γ       |           |     |     |      |
In particular,
K∗
|     |     |     |     |     |     | ≤ 4k(k −1). |     |     | (76) |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ---- |
n+k,n
| The family | in (72)   | satisfies |     |          |      |               |     |         |      |
| ---------- | --------- | --------- | --- | -------- | ---- | ------------- | --- | ------- | ---- |
|            |           |           |     |          |      | (cid:0)       |     | (cid:1) |      |
|            |           |           | P   | (C ;γ)   | = B∗ | 4k(k −1)+o(1) |     | .       | (77) |
|            |           |           |     | e γ      | γ    |               |     |         |      |
| Proof:     | The proof | is given  | in  | Appendix |      | C.            |     |         |      |
Proposition 5 gives an achievability family defined for every sufficiently large SNR, rather than
only along a subsequence. The construction lowers by order q the correlations of the d(d+4k−1)
γ
pairs involving an auxiliary point that are closest in the limiting deleted cross-polytope, so their
contributions to the constructed family’s leading coefficient vanish because nγq → ∞. The
γ
correlations of the 4k(k −1) pairs between shifted points on different axes increase only by
p = O(q2); since nγp → 0, these pairs have limiting weight one. The exact ML error of the
| γ   |     | γ   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
constructed family therefore has leading coefficient 4k(k−1). The improvement is obtained only
because the codebook continues to vary with SNR at the specified two rates.

30
C. Exact Optimal Leading Coefficients at the Orthoplex-Bound Endpoints
For the orthoplex-range endpoints, we first solve the terminal Gaussian soft-packing energy
problem exactly at every positive SNR, which determines the optimal leading coefficient for
| k = n, and | then provide |     | a matching | lower | bound | for | k = | 2.  |     |
| ---------- | ------------ | --- | ---------- | ----- | ----- | --- | --- | --- | --- |
Theorem 4 (Exact terminal endpoint k = n). For every fixed n ≥ 2 and every γ > 0, the full
cross-polytope
|             |           |     |              | C     | = {e ,−e              | ,...,e  | ,−e | }   |      |
| ----------- | --------- | --- | ------------ | ----- | --------------------- | ------- | --- | --- | ---- |
|             |           |     |              | cross | 1                     | 1       | n   | n   |      |
| is a global | minimizer | of  | the Gaussian |       | soft-packing          | energy, |     | and |      |
|             |           |     | V (2n,n)     | =     | 4n(n−1)+2nexp{−nγ/4}. |         |     |     | (78) |
γ
Consequently,
|     |     |     |     | K∗   | Kfix |            |     |     |      |
| --- | --- | --- | --- | ---- | ---- | ---------- | --- | --- | ---- |
|     |     |     |     |      | =    | = 4n(n−1), |     |     | (79) |
|     |     |     |     | 2n,n |      | 2n,n       |     |     |      |
and
2(n−1)
|           |                     | P∗(2n,n;γ) |              |          |                |            |             | (cid:0) (cid:1) |      |
| --------- | ------------------- | ---------- | ------------ | -------- | -------------- | ---------- | ----------- | --------------- | ---- |
|           |                     |            |              | =        | √              | exp{−nγ/4} |             | 1+o(1) .        | (80) |
|           |                     | e          |              |          | πnγ            |            |             |                 |      |
| The fixed | full cross-polytope |            | is therefore |          | asymptotically |            | ML-optimal. |                 |      |
| Proof:    | The proof           | is         | given in     | Appendix |                | C.         |             |                 |      |
The terminal endpoint behaves like the simplex range. Universal optimality makes the full
cross-polytope a soft-packing energy minimizer at every positive SNR. Its 4n(n−1) ordered
orthogonal pairs contribute one unit each to the limiting Gaussian soft-packing energy, whereas
the contributions of the 2n ordered antipodal pairs vanish exponentially. Hence Kfix and K∗
2n,n 2n,n
coincide, and SNR-dependent motion cannot improve the leading coefficient at k = n. The
result also covers the square n = k = 2, where the two orthoplex endpoints coincide. The
exact finite-SNR assertion concerns the Gaussian soft-packing energy; the exact ML conclusion
| established | here is | asymptotic. |     |     |     |     |     |     |     |
| ----------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
To determine the left endpoint of the orthoplex-bound range, the construction must be paired
with a global converse valid for every codebook, rather than only for a particular limiting packing.
Proposition 6 (Global signed-balance lower bound). For every C ∈ (Sn−1)n+2, put ϱ = ρ (C).
max
| Then, for | every γ > | 0,  |     |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
8
|     |     |     |     |     | G (C) | ≥      | .   |     | (81) |
| --- | --- | --- | --- | --- | ----- | ------ | --- | --- | ---- |
|     |     |     |     |     | γ     | (1+ϱ)2 |     |     |      |

31
Consequently,
|     |     |     |     |     | liminfV |     | (n+2,n) | ≥ 8. |     |     |      |
| --- | --- | --- | --- | --- | ------- | --- | ------- | ---- | --- | --- | ---- |
|     |     |     |     |     |         | γ   |         |      |     |     | (82) |
γ→∞
|     | Proof: The | proof | is  | given | in Appendix |     | C.  |     |     |     |     |
| --- | ---------- | ----- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
Unlike a bound based on a fixed closest-pair count, Proposition 6 applies globally to every
(n+2,n) codebook, including non-packing-optimal codebooks and codebooks selected from
SNR-dependent families. Every packing-tail-competitive family has ρ (C ) → 0, so the finite-
max γ
SNR inequality forces the liminf of its Gaussian soft-packing energy to be at least 8. It therefore
K∗
| supplies | exactly | the | converse |     | needed | to certify |     | .   |     |     |     |
| -------- | ------- | --- | -------- | --- | ------ | ---------- | --- | --- | --- | --- | --- |
n+2,n
Theorem 5 (Exact optimal leading coefficient at the left endpoint k = 2). For every fixed n ≥ 2,
| as γ | → ∞, |     |     |     |     |         |     |         |     |     |      |
| ---- | ---- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- | ---- |
|      |      |     |     |     | V   | (n+2,n) | =   | 8+o(1), |     |     | (83) |
γ
and
|     |     |     |     |     |     | K∗  | =   | 8.  |     |     | (84) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
n+2,n
| The | exact SNR-wise |     | optimized |     | ML error | satisfies |     |     |     |     |     |
| --- | -------------- | --- | --------- | --- | -------- | --------- | --- | --- | --- | --- | --- |
exp{−nγ/4}
|     |     |     |     | P∗(n+2,n;γ) |     | =   |     | √ (8+o(1)). |     |     | (85) |
| --- | --- | --- | --- | ----------- | --- | --- | --- | ----------- | --- | --- | ---- |
√
|     |     |     |     | e   |     | (n+2) |     | nγ π |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- |
Moreover, a family attaining the optimal leading coefficient is given by the fixed square when
n = 2 and by the SNR-dependent codebook in (72), specialized to k = 2, when n ≥ 3. In either
case,
|     |     |     |      |     |            |        |         | P (C ;γ)    |     |     |      |
| --- | --- | --- | ---- | --- | ---------- | ------ | ------- | ----------- | --- | --- | ---- |
|     |     |     |      |     | B∗ (cid:0) |        | (cid:1) | e γ         |     |     |      |
|     |     |     | P (C | ;γ) | =          | 8+o(1) | ,       |             | −→  | 1.  | (86) |
|     |     |     | e    | γ   | γ          |        |         | P∗(n+2,n;γ) |     |     |      |
e
Proof: Proposition 6 gives liminf V (n+2,n) ≥ 8. Let C be the fixed square when
|     |     |     |     |     |     | γ→∞ | γ   |     | γ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n = 2 and the family in (72), specialized to k = 2, when n ≥ 3. In the first case, Theorem 4
gives G (C ) = V (4,2) = 8 + 4e−γ/2. In the second case, (75) gives G (C ) → 8. Since
|     | γ γ |     | γ   |     |     |     |     |     |     | γ γ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
V (n+2,n) ≤ G (C ), both cases yield the matching limsup bound. Hence V (n+2,n) = 8+o(1),
| γ   |     | γ   | γ   |     |     |     |     |     |     | γ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
proving (83). Corollary 5, applied with K = 8, then gives (84) and (86). Substitution of (67),
| specialized | to  | k = | 2, gives | (85). |     |     |     |     |     |     |     |
| ----------- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Theorem 5 gives the strongest proved separation between fixed and SNR-dependent codebook
design in this paper. The optimal leading coefficient is K∗ = 8, independently of n, whereas
n+2,n
the best fixed-codebook leading coefficient is Kfix = 4n. For n ≥ 3, the moving family
n+2,n
genuinely attains the optimal leading coefficient, and its asymptotic ML error is smaller by the

32
factor n/2 than the best asymptotic ML error of any fixed packing-optimal codebook; no fixed
|     |     |     |     |     |     | K∗  |     | n = | 2,  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
packing-optimal codebook can attain . For the two endpoints coincide and the
n+2,n
| fixed | square  | is already | optimal.            |     |     |         |     |              |     |     |     |     |
| ----- | ------- | ---------- | ------------------- | --- | --- | ------- | --- | ------------ | --- | --- | --- | --- |
| D.    | Optimal | Versus     | Best Fixed-Codebook |     |     | Leading |     | Coefficients |     |     |     |     |
Combining Proposition 5 with the fixed benchmark in (68) gives, for every fixed n ≥ 3 and
| 2   | ≤ k < | n,  |     |       |        |     |     |          |        |       |     |      |
| --- | ----- | --- | --- | ----- | ------ | --- | --- | -------- | ------ | ----- | --- | ---- |
|     |       |     | K∗  |       | ≤ 4k(k | −1) | <   | 4n(k −1) | = Kfix | .     |     | (87) |
|     |       |     |     | n+k,n |        |     |     |          |        | n+k,n |     |      |
In particular,
|     |     |     |     |     |     | K∗  |     | k   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n+k,n
|     |     |     |     |     |     |      | ≤   | < 1. |     |     |     | (88) |
| --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | ---- |
|     |     |     |     |     |     | Kfix |     | n    |     |     |     |      |
n+k,n
Let Cfix be any fixed packing-optimal codebook attaining Kfix , and let C be the family in
|       | 0   |                |            |     |       |          |          |       | n+k,n |     | γ   |     |
| ----- | --- | -------------- | ---------- | --- | ----- | -------- | -------- | ----- | ----- | --- | --- | --- |
| (72). | The | fixed-codebook | expansion, |     | (77), |          | and (43) | yield |       |     |     |     |
|       |     |                |            |     | P     | (C ;γ)   |          | k     |       |     |     |     |
|       |     |                |            |     |       | e γ      | −→       | ,     |       |     |     |     |
|       |     |                |            |     | P     | (Cfix;γ) |          | n     |       |     |     |     |
|       |     |                |            |     | e     | 0        |          |       |       |     |     |     |
(89)
Kfix
|     |     |     |     |             | P (Cfix;γ) |     |     |       |     | n   |     |     |
| --- | --- | --- | --- | ----------- | ---------- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |             | e          | 0   | −→  | n+k,n | ≥   | .   |     |     |
|     |     |     |     | P∗(n+k,n;γ) |            |     |     | K∗    |     | k   |     |     |
|     |     |     |     |             | e          |     |     | n+k,n |     |     |     |     |
Thus, throughout the nonterminal orthoplex-bound range, the explicit moving family has a leading
coefficient equal to the fraction k/n of the best fixed-codebook leading coefficient. The exact
| SNR-wise |      | optimum      | is no larger |       | than | the error | of  | this family. |     |     |     |      |
| -------- | ---- | ------------ | ------------ | ----- | ---- | --------- | --- | ------------ | --- | --- | --- | ---- |
|          | At k | = 2, Theorem | 5 shows      | that  | the  | bound     | is  | sharp:       |     |     |     |      |
|          |      |              |              | K∗    |      | 2         | P   | (Cfix;γ)     |     | n   |     |      |
|          |      |              |              | n+2,n |      |           |     | e            |     |     |     |      |
|          |      |              |              |       | =    | ,         |     | 0            | −→  | .   |     | (90) |
Kfix
|     |     |     |     |       | n   |     | P∗(n+2,n;γ) |     |     | 2   |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|     |     |     |     | n+2,n |     |     | e           |     |     |     |     |     |
K∗
For 3 ≤ k ≤ n−1, only the one-sided upper bound on has been proved. At the terminal
n+k,n
| endpoint, |     | Theorem | 4 gives |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
K∗
2n,n
|     |     |     |     |     |     |     |     | = 1, |     |     |     | (91) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
Kfix
2n,n
so no leading-coefficient gain from an SNR-dependent codebook occurs. In particular, when
n = 2, the left and terminal endpoints coincide and the fixed square is already leading-order
optimal.
For 3 ≤ k ≤ n−1, we have not proved a global lower bound matching (76). We therefore
cannot exclude a different jointly feasible multiscale deformation with a still smaller value of
the sum in (54). Nevertheless, the two exact endpoint results and the structure of the explicit
construction suggest that its achieved value is sharp, motivating the following conjecture.

33
Conjecture 1 (Sharpness in the intermediate orthoplex-bound range). For every fixed n ≥ 4 and
| 3 ≤ k ≤ | n−1, |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- |
K∗
= 4k(k −1). (92)
n+k,n
The conjectured range is empty for n ≤ 3. If the conjecture holds, the moving family in (72)
attains the optimal leading coefficient throughout the intermediate range.
Table I separates the proved exact values, the proved upper bound, and the conjectured equality.
|     |     |     | TABLE I |     |     |
| --- | --- | --- | ------- | --- | --- |
STATUSOFTHELEADINGCOEFFICIENTSINTHESIMPLEXANDORTHOPLEX-BOUNDAPPLICATIONS.
Range Optimal leading coefficient Bestfixed-codebookleadingco-
efficient
| 2≤M ≤n+1 |     | M(M −1)   | (exact)              |     | M(M −1) |
| -------- | --- | --------- | -------------------- | --- | ------- |
| k =2     |     | 8 (exact) |                      |     | 4n      |
| 3≤k ≤n−1 |     | ≤4k(k−1); | equality conjectured |     | 4n(k−1) |
| k =n     |     | 4n(n−1)   | (exact)              |     | 4n(n−1) |
K∗
In the intermediate row, 4k(k−1) is the leading coefficient of the constructed family and hence an upper bound on ;
n+k,n
| equality is conjectured. |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- |
VIII. CONCLUSION
Optimal spherical packing fixes the best high-SNR error exponent, but it need not fix the
optimal leading coefficient when the codebook is reoptimized at each SNR. The nonterminal
orthoplex-bound construction exposes the reason. It slightly reduces the separations of selected
pairs by an amount negligible at the leading-coefficient scale, while using the resulting geometric
freedom to improve other pairs that become closest in the limiting packing on a larger, though still
vanishing, scale. The selected pairs make unit contributions to the constructed family’s leading
coefficient, whereas the improved pairs make vanishing contributions to that coefficient. The
codebooks therefore approach an optimal packing and retain its exponent, yet outperform every
packing-optimal codebook held fixed. The improvement results from the two SNR-dependent
| convergence | rates, not | from the | limiting packing alone. |     |     |
| ----------- | ---------- | -------- | ----------------------- | --- | --- |
ρ∗
| For every | fixed finite | (M,n) with | M ≥ 2 and | < 1, we proved |     |
| --------- | ------------ | ---------- | --------- | -------------- | --- |
M,n
(cid:0) (cid:1)
|     |     | P∗(M,n;γ) | = B∗ K∗ | +o(1) | .   |
| --- | --- | --------- | ------- | ----- | --- |
|     |     |           | e γ     | M,n   |     |

34
| The best packing-optimal |     | benchmark   | satisfies |                 |         |
| ------------------------ | --- | ----------- | --------- | --------------- | ------- |
|                          |     | Pfix(M,n;γ) |           | B∗ (cid:0) Kfix | (cid:1) |
|                          |     |             |           | = +o(1)         | .       |
|                          |     | e           |           | γ M,n           |         |
Moreover, K∗ ≤ Kfix . Thus, whenever K∗ < Kfix , the exact SNR-wise minimum error is
| M,n | M,n |     |     | M,n M,n |     |
| --- | --- | --- | --- | ------- | --- |
strictly smaller than the best packing-optimal benchmark for all sufficiently large γ, and their
K∗ /Kfix
ratio tends to . We showed that the minimum of the Gaussian soft-packing energy
M,n M,n
K∗
converges to . We also showed that only pairs that are closest in a limiting packing can
M,n
contribute to K∗ and that their contributions are determined by the pairs’ scaled correlation
M,n
offsets.
The simplex and orthoplex-bound ranges display both possible outcomes. For 2 ≤ M ≤ n+1,
the regular simplex gives K∗ = Kfix = M(M −1), so SNR-dependent motion provides no
M,n M,n
leading-order gain. For M = n + k, 2 ≤ k ≤ n, the best fixed-codebook leading coefficient
is 4n(k −1). When 2 ≤ k < n, the exact ML error of the explicit moving family has leading
coefficient 4k(k −1), exactly the fraction k/n of the best fixed-codebook leading coefficient;
hence
|     |     |     | K∗  | k   |     |
| --- | --- | --- | --- | --- | --- |
n+k,n
≤ < 1.
|     |     |     | Kfix | n   |     |
| --- | --- | --- | ---- | --- | --- |
n+k,n
K∗
A matching converse proves = 8 at k = 2. At the terminal endpoint k = n, the fixed
n+2,n
cross-polytope attains the optimal leading coefficient and K∗ = Kfix = 4n(n − 1). For
2n,n 2n,n
3 ≤ k ≤ n−1, equality in the constructive upper bound remains conjectural.
|     |     |     | APPENDIX | A   |     |
| --- | --- | --- | -------- | --- | --- |
UNIFORM TRANSFER, OPTIMAL LEADING-COEFFICIENT CHARACTERIZATION, AND
|     | GAUSSIAN | SOFT-PACKING |     | ENERGY ATTAINMENT | PROOFS |
| --- | -------- | ------------ | --- | ----------------- | ------ |
This appendix proves the uniform-transfer theorem, the O((nγ)−1) comparison between the
normalized optimized exact ML error and V (M,n), the existence and characterization of the
γ
optimal leading coefficient K∗ , and the Gaussian soft-packing energy near-minimizer attainment
M,n
criterion from Section III. The pointwise fixed-codebook expansion is the standard result cited
in Subsection II-C and is not rederived here. Instead, the first proof establishes the additional
uniformity needed when the codebook changes with SNR. It invokes standard Gaussian-tail and
Bonferroni estimates, while deriving only the codebook-uniform estimates specific to the present
| problem. Set |     |     |           |      |     |
| ------------ | --- | --- | --------- | ---- | --- |
|              |     |     | δ∗ = 1−ρ∗ | > 0, |     |
M,n

35
∆ (C) = ρ (C)−ρ∗ ,
e e M,n
d (C) = 1−ρ (C) = δ∗ −∆ (C).
e e e
For e = (m,ℓ), abbreviate d := d (C), and write
mℓ (m,ℓ)
w (C,γ) = exp{nγ∆ (C)/4},
e e
(cid:80)
so that G (C) = w (C,γ). Put N = M(M −1). Hidden constants in O (·) may depend
γ e∈EM e M L
on the fixed pair (M,n) and on L, but not on C or γ.
A. Uniform Transfer on Bounded-Energy Sublevels
Proof of Theorem 1: Fix L ≥ 1 and suppose G (C) ≤ L. The bounded-energy packing
γ
consequence (28) gives
4logL
0 ≤ ρ (C)−ρ∗ ≤ η , η = .
max M,n γ γ nγ
Hence, for all sufficiently large γ,
∥c −c ∥2 = 2d ≥ 2(δ∗ −η ) ≥ δ∗,
m ℓ mℓ γ
so the codewords are distinct. If M ≥ 3, consider the compact set of triples of unit vectors
√
with all mutual distances at least δ∗. On this set, the inner product of the two unit difference
directions from one point is strictly below one: equality would place the other two points on
the same ray, but that ray meets the unit sphere in only one further point. Let r denote the
maximum over this compact set; the preceding argument shows that r < 1. Put ϱ = max{0,r}.
Then, uniformly over this bounded-energy sublevel,
c −c
uT u ≤ ϱ, u = ℓ m ,
mℓ mk mℓ ∥c −c ∥
ℓ m
for every transmitted index m and distinct competitors ℓ,k ̸= m. For M = 2, this assertion is
vacuous.
Define the full ordered-pair tail sum
(cid:32)(cid:114) (cid:33)
1 (cid:88) nγd (C)
e
Q (C) = Q .
γ
M 2
e∈EM

36
The preceding correlation bound gives d (C) ∈ [δ∗/2,2] for all sufficiently large γ. The classical
e
two-sided Mills inequalities [17] imply, uniformly over all ordered pairs,
(cid:112)
|     |     |     |     | M−1Q( |     | nγd (C)/2) |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | ---------- | --- | --- | --- | --- |
e
B∗
γ
|     |     |     |     |     |     | (cid:18) | δ∗ (cid:19)1/2 |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | --- | --- |
|     |     |     |     |     | = w | (C,γ)    |                |     |     |     |
e
d (C)
e
|     |     |     |     |     |     | (cid:2)     |     | (cid:3) |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --- | --- |
|     |     |     |     |     | ×   | 1+O((nγ)−1) |     | .       |     |     |
On the stated interval, |(δ∗/d )1/2 −1| ≤ C|∆ |. For nonnegative offsets,
|     |     |     |     | e   |     | e   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|     |     |     |     | w   | |∆ | ≤ | η G (C) | = O | ((nγ)−1), |     |     |
| --- | --- | --- | --- | --- | ------ | ------- | --- | --------- | --- | --- |
|     |     |     |     | e   | e      | γ γ     | L   |           |     |     |
∆e≥0
(cid:80)
whereas, for ∆ = −x < 0, xexp{−nγx/4} ≤ 4/(enγ). Together with w ≤ L, these
e e e
| estimates | give |     |     |       |     |     |     |     |     |     |
| --------- | ---- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|           |      |     |     | Q (C) |     |     |     |     |     |     |
γ
|     |     |     |     |     | =   | G (C)+O | ((nγ)−1). |     |     | (93) |
| --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | ---- |
|     |     |     |     |     |     | γ       | L         |     |     |      |
B∗
γ
It remains to replace the sum of pairwise tails by the exact union. The union bound and the
| second Bonferroni |     | inequality |     | [18, Ch. | 1]      | give  |     |     |     |     |
| ----------------- | --- | ---------- | --- | -------- | ------- | ----- | --- | --- | --- | --- |
|                   |     |            |     | 0 ≤      | Q (C)−P | (C;γ) |     |     |     |     |
|                   |     |            |     |          | γ       | e     |     |     |     |     |
M
|     |     |     |     |     | 1 (cid:88) | (cid:88) |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | -------- | --- | --- | --- | --- |
P(A
|     |     |     |     | ≤   |     |     | ∩A  |     | ).  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | M   |     | mℓ  | mk  |     |     |
|     |     |     |     |     | m=1 | ℓ<k |     |     |     |     |
ℓ,k̸=m
| Each event | has | the form | A   | = {ZTu |     | ≥ x }, | where |     |     |     |
| ---------- | --- | -------- | --- | ------ | --- | ------ | ----- | --- | --- | --- |
|            |     |          | mℓ  |        | mℓ  | mℓ     |       |     |     |     |
(cid:114)
(cid:114)
|     |     |     |     |     | nγd |     | nγ(δ∗ |     | −η ) |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- |
|     |     |     | x   | =   | mℓ  | ≥ x | :=    |     | γ .  |     |
|     |     |     | mℓ  |     |     | min |       |     |      |     |
|     |     |     |     |     | 2   |     |       | 2   |      |     |
If the two normals are antipodal, the corresponding events are disjoint. Otherwise their intersection
implies ZT(u +u ) ≥ 2x , and the standard scalar Gaussian tail bound [1] gives
|     | mℓ  | mk  |     | min |     |          |       |     |            |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --- | ---------- | --- |
|     |     |     |     |     |     | (cid:26) | nγ(δ∗ | −η  | ) (cid:27) |     |
γ
|     |     |     | P(A | ∩A  | )   | ≤ exp | −   |     | .   |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     | mℓ  | mk  |       |     |     |     |     |
2(1+ϱ)
Because ϱ < 1, this exponent exceeds the exponent nγδ∗/4 in B∗ by a fixed positive multiple of
γ
nγ for all sufficiently large γ. The number of intersections is fixed, so, for some χ > 0,
L
|     |     |     | Q   | (C)−P | (C;γ) |     |         |       |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | ------- | ----- | --- | --- |
|     |     |     |     | γ     | e     |     |         |       |     |     |
|     |     |     |     |       |       | = O | (exp{−χ | nγ}). |     |     |
|     |     |     |     | B∗    |       |     | L       | L     |     |     |
γ
Combining this estimate with (93) proves the asymptotic form of (32). Enlarging its constant
| gives the | asserted | bound | for | every γ | ≥ γ | .   |     |     |     |     |
| --------- | -------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
L

37
B. Packing-Scale Error Implies Bounded Gaussian Soft-Packing Energy
Lemma 2 (Error-to-energy localization). If an SNR-indexed family {C } ⊂ M satisfies
γ
|     |     |     |     |     | P (C | ;γ) |         |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------- | --- | --- | --- | --- |
|     |     |     |     |     | e    | γ   |         |     |     |     |     |
|     |     |     |     |     |      |     | = O(1), |     |     |     |     |
B∗
γ
then its codewords are pairwise distinct for all sufficiently large γ, and
|     |     |     | )−ρ∗ |     | O((nγ)−1), |     |     |     |              |     |      |
| --- | --- | --- | ---- | --- | ---------- | --- | --- | --- | ------------ | --- | ---- |
|     |     | ρ   | (C   |     | =          |     |     | G   | (C ) = O(1). |     | (94) |
|     |     | max | γ    | M,n |            |     |     |     | γ γ          |     |      |
Proof: If two codewords coincide, then for every received vector a decoder can correctly
distinguish at most one of their two equiprobable message labels; equivalently, the two corre-
sponding conditional probabilities of correct decoding sum to at most one, independently of the
tie-breaking rule. Those two messages therefore contribute at least 1/M to the average error.
| B∗  | → 0, |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Since the assumed packing-scale error makes coincident codewords impossible for
γ
|     |     |     |     |     | )−ρ∗ |     |     |     | δ∗  |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
all sufficiently large γ. Put ξ = ρ (C ≥ 0 and d = −ξ . A pair attaining the
|            |             |               | γ   | max      | γ     | M,n |                   |     | γ        | γ   |     |
| ---------- | ----------- | ------------- | --- | -------- | ----- | --- | ----------------- | --- | -------- | --- | --- |
| maximal    | correlation | gives         |     |          |       |     |                   |     |          |     |     |
|            |             |               |     |          |       |     | (cid:32)(cid:114) |     | (cid:33) |     |     |
|            |             |               |     |          |       | 1   |                   | nγd |          |     |     |
|            |             |               |     | P (C     | ;γ) ≥ | Q   |                   | γ   | .        |     |     |
|            |             |               |     | e        | γ     |     |                   |     |          |     |     |
|            |             |               |     |          |       | M   |                   | 2   |          |     |     |
| The global | lower       | Gaussian-tail |     | estimate |       |     |                   |     |          |     |     |
exp{−x2/2}
|     |     |     | Q(x) | ≥   | c   |     | ,   | x   | ≥ 0, |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- | --- |
1+x
follows, for example, by combining monotonicity on 0 ≤ x ≤ 1 with the classical Mills
| inequalities | on x ≥ | 1 [17]. | Since | 0 ≤ | d ≤ | δ∗, it | gives |     |     |     |     |
| ------------ | ------ | ------- | ----- | --- | --- | ------ | ----- | --- | --- | --- | --- |
γ
√
nγ
|     |     |     |     | P (C | ;γ) |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | e    | γ ≥ | c′  |     |     |     |     |     |
(cid:112)
|     |     |     |     | B∗  |     | 1+       | nγd | /2  |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | γ   |          |     | γ   |     |     |     |
|     |     |     |     |     |     | ×exp{nγξ |     |     | /4} |     |     |
γ
|     |     |     |     |     | ≥   | c′′exp{nγξ |     | /4}. |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | --- | --- | --- |
γ
Bounded normalized error therefore implies nγξ = O(1). Since every offset ∆ (C ) ≤ ξ ,
|              |       |     |     |      |     |         | γ   |     |       | e γ | γ   |
| ------------ | ----- | --- | --- | ---- | --- | ------- | --- | --- | ----- | --- | --- |
|              |       |     | G   | (C ) | ≤ N | exp{nγξ | /4} | =   | O(1), |     |     |
|              |       |     |     | γ γ  | M   |         | γ   |     |       |     |     |
| which proves | (94). |     |     |      |     |         |     |     |       |     |     |

38
| C. Equivalence | of  | the Optimized |     | Values |     |     |     |     |
| -------------- | --- | ------------- | --- | ------ | --- | --- | --- | --- |
Proof of Corollary 2: Let CG minimize G . Evaluation at any fixed packing-optimal codebook
|         |         |        |         | γ   |        | γ   |     |     |
| ------- | ------- | ------ | ------- | --- | ------ | --- | --- | --- |
| gives V | (M,n) ≤ | N , so | Theorem | 1   | yields |     |     |     |
| γ       |         | M      |         |     |        |     |     |     |
(CG;γ)
|     |     | P∗(M,n;γ) |     |     | P   |                      |     |     |
| --- | --- | --------- | --- | --- | --- | -------------------- | --- | --- |
|     |     | e         |     | ≤   | e γ | = V (M,n)+O((nγ)−1). |     |     |
γ
|     |     |     | B∗  |     | B∗  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | γ   |     | γ   |     |     |     |
For the reverse inequality, choose an exact ML minimizer C∗ as in Subsection II-D. Comparison
γ
| with any | fixed C | ∈ P∗, | followed | by  | (15), gives |     |     |     |
| -------- | ------- | ----- | -------- | --- | ----------- | --- | --- | --- |
0
P (C∗;γ)
|     |     |     |     | e   |     | P (C ;γ) |       |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --- |
|     |     |     |     |     | γ ≤ | e 0 =    | O(1). |     |
|     |     |     |     | B∗  |     | B∗       |       |     |
|     |     |     |     |     | γ   | γ        |       |     |
Lemma 2 shows that G (C∗) is bounded. Uniform transfer can therefore be applied with one
γ γ
| fixed sublevel, | giving |     |     |     |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
P∗(M,n;γ)
|     |     |     |     | e   | =   | G (C∗)+O((nγ)−1) |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
γ γ
B∗
γ
(M,n)−O((nγ)−1).
|     |     |     |     |     | ≥   | V   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
| The two | bounds prove | (34). |     |     |     |     |     |     |
| ------- | ------------ | ----- | --- | --- | --- | --- | --- | --- |
D. Existence and Characterization of the Optimal Leading Coefficient
Proof of Theorem 2: The compact codebook space M is semialgebraic, and (γ,C) (cid:55)→ G (C)
γ
is definable, with real parameters, in the real exponential field R . Closure under quantification
exp
over M therefore makes the value function V (M,n) definable. O-minimality of R [19] and
|     |     |     |     |     |     | γ   |     | exp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
the one-variable monotonicity theorem [20, Ch. 3, Sec. 1] imply that this function is monotone
| or constant | on some | interval |     | (γ ,∞). |     |     |     |     |
| ----------- | ------- | -------- | --- | ------- | --- | --- | --- | --- |
0
For every codebook, ρ (C) ≥ ρ∗ . If the unordered pair {m,ℓ} attains ρ (C), then both
|     |     |     | max | M,n |     |     |     | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ordered terms (m,ℓ) and (ℓ,m) in G (C) are at least one. Thus V (M,n) ≥ 2. Conversely,
γ γ
evaluating the energy at a packing-optimal codebook gives V (M,n) ≤ N , because every
|     |     |     |     |     |     |     | γ   | M   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
packing gap is nonpositive. Eventual monotonicity and these uniform bounds prove existence
| and finiteness | of lim |     | V (M,n), | together |     | with (36). |     |     |
| -------------- | ------ | --- | -------- | -------- | --- | ---------- | --- | --- |
γ→∞ γ
P∗,
For a fixed C ∈ equation (29) and V ≤ G (C ) give (38). Finally, Corollary 2 gives
|     | 0   |     |     |     | γ   | γ 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
P∗(M,n;γ)
|     |     | e   |     | = V | (M,n)+O((nγ)−1) |     | = K∗ +o(1), |     |
| --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- |
γ
|     |     |     | B∗  |     |     |     | M,n |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
| which identifies | the | second | limit | in (35) | and | proves (37). |     |     |
| ---------------- | --- | ------ | ----- | ------- | --- | ------------ | --- | --- |

39
| E. Attainment | by Gaussian |     | Soft-Packing | Energy Near-Minimization |     |     |     |
| ------------- | ----------- | --- | ------------ | ------------------------ | --- | --- | --- |
Proof of Corollary 3: Equations (39) and (35) give G (C(cid:98) ) → K∗ ; the bound V (M,n) ≤
|     |     |     |     |     | γ γ | M,n | γ   |
| --- | --- | --- | --- | --- | --- | --- | --- |
N shows that this family has uniformly bounded Gaussian soft-packing energy. Uniform transfer
M
|     | ;γ)/B∗ | K∗  |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- |
then gives P (C(cid:98) → . Dividing by the optimized normalized-error limit in Theorem 2
|     | e γ | γ   | M,n |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
K∗
| is legitimate | because | ≥   | 2, and | proves (41). |     |     |     |
| ------------- | ------- | --- | ------ | ------------ | --- | --- | --- |
M,n
|     |     |     |     | APPENDIX | B   |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
PACKING-TAIL LOCALIZATION CLOSEST-PAIR CONTRIBUTION CHARACTERIZATION
AND
This appendix proves Lemma 1, Theorem 3, and Proposition 2 from Section IV. Appendix A
already supplies error-to-energy localization, uniform transfer, and convergence of the globally
minimized Gaussian soft-packing energy. The first two proofs use compactness and separation of
finitely many pair correlations; the final proof combines the limiting closest-pair reduction with
| the global | soft-packing | energy | limit. |     |     |     |     |
| ---------- | ------------ | ------ | ------ | --- | --- | --- | --- |
Atacoarserlevel,theknownRiesz-energyfactthatclusterpointsoffixed-cardinalityminimizers
are best packings is analogous to the first localization step [15, Prop. 2]. It does not provide the
1/(nγ) localization rate, the scaled closest-pair contribution formula, or the exact ML conclusions
proved here.
Proof of Lemma 1: Condition (44) and Lemma 2 give (45) and G (C ) = O(1), and hence
γ γ
ρ (C ) → ρ∗ . If the distance to P∗ did not tend to zero, compactness would give a convergent
| max | γ M,n |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- |
subsequence with fixed positive separation from P∗, whereas continuity of ρ would place its
max
| limit in | P∗. This proves | (46). |     |     |     |     |     |
| -------- | --------------- | ----- | --- | --- | --- | --- | --- |
Under the additional hypotheses, membership C ∈ P∗ along an unbounded subsequence
γj
would give
Kfix
|     |     |     | G (C | ) ≥ |I (C | )| ≥ . |     |     |
| --- | --- | --- | ---- | --------- | ------ | --- | --- |
|     |     |     | γj   | γj max    | γj M,n |     |     |
The first inequality follows directly from (27), because every ordered closest-pair index contributes
one to G (C ); the second is the fixed closest-pair-count characterization (16). Uniform transfer
γj γj
| would | then give |     |         |     |     |     |     |
| ----- | --------- | --- | ------- | --- | --- | --- | --- |
|       |           |     | P (C ;γ | )   |     |     |     |
e γj j
|     |     |     |     | ≥ Kfix −O((nγ | )−1), |     |     |
| --- | --- | --- | --- | ------------- | ----- | --- | --- |
|     |     |     | B∗  | M,n           | j     |     |     |
γj
while attainment of the optimal leading coefficient makes this ratio converge to K∗ < Kfix , a
M,n M,n
| contradiction. | This proves | (47). |     |     |     |     |     |
| -------------- | ----------- | ----- | --- | --- | --- | --- | --- |

40
Proof of Theorem 3: Finiteness and C → C give a > 0 such that, for all sufficiently large
γ ∞
γ, every e ∈/ I (C ) satisfies ρ (C )−ρ∗ ≤ −a (vacuously if there is no such index). Since
max ∞ e γ M,n
ρ (C ) ≥ ρ∗ , the largest correlation must therefore be attained within I (C ), and
max γ M,n max ∞
max ∆ = ρ (C )−ρ∗ ≥ 0.
e,γ max γ M,n
e∈Imax(C∞)
Equation (28) gives the stated upper bound. Separating the indices in I (C ) from the remaining
max ∞
pairs gives
(cid:88)
G (C ) = exp{nγ∆ /4}
γ γ e,γ
e∈Imax(C∞)
+O(exp{−anγ/4}).
The remainder is identically zero if every ordered pair belongs to I (C ). Thus (48) holds for
max ∞
some c > 0. Uniform transfer and absorption of the exponential remainder into O((nγ)−1) then
prove (49).
A. Global Variational Characterization by Scaled Closest-Pair Offsets
Proof of Proposition 2: Fix C ∈ P∗, λ ∈ L(C ), and a witnessing sequence from (53).
0 0
Theorem 3, specifically (48), gives
(cid:88)
G (C ) −→ exp{λ /4}.
γj j e
e∈Imax(C0)
Since V (M,n) ≤ G (C ) and Theorem 2 gives V (M,n) → K∗ , the sum in (54) is at least
γj γj j γj M,n
K∗ for every admissible pair.
M,n
For the reverse inequality, start with γ = j and select an exact soft-packing energy minimizer
(cid:101)j
C(cid:101)G at each γ . Its energy is
j (cid:101)j
G (C(cid:101) G) = V (M,n) ≤ M(M −1),
γ (cid:101)j j γ (cid:101)j
so compactness of M gives indices j → ∞ for which C(cid:101)G → C . Relabel this subsequence by
r jr 0
γ = γ = j and CG = C(cid:101)G. Equation (28) and continuity of ρ imply C ∈ P∗. Corollary 4
r (cid:101)jr r r jr max 0
then gives a further subsequence and λ ∈ L(C ) such that
0
(cid:88)
exp{λ /4} = lim V (M,n) = K∗ .
e
r→∞
γr M,n
e∈Imax(C0)
Thisprovesbothequalityandattainmentin(54).Finally,foranysequencewitnessingaminimizing
pair, G (C ) → K∗ , and the Gaussian soft-packing energy is uniformly bounded along that
γj j M,n

41
sequence. Theorem 1 then gives the limit of the normalized ML error. Dividing it by the
|     |     |     | P∗(M,n;γ)/B∗ |     |     |     |     |     |     | K∗ ≥ 2, |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | ------- |
corresponding limit of from Theorem 2, which is positive because
|           |                |     | e       |         | γ        |                 |     |              |     | M,n |
| --------- | -------------- | --- | ------- | ------- | -------- | --------------- | --- | ------------ | --- | --- |
| gives the | relative-error |     | limit.  |         |          |                 |     |              |     |     |
|           |                |     |         |         | APPENDIX |                 | C   |              |     |     |
|           | PROOFS         |     | FOR THE | SIMPLEX | AND      | ORTHOPLEX-BOUND |     | APPLICATIONS |     |     |
This appendix supplies the derivations specific to the simplex and orthoplex-bound applica-
tions. The simplex and terminal-endpoint arguments use the universal-optimality result in [11,
Thm. 1.2 and Table 1], while the orthoplex-bound fixed-codebook argument uses the equality-case
classification in [12, Thm. 3]; an equivalent characterization is given in [13, Thm. 2.2]. Only
the normalization and closest-pair-count consequences needed here are derived. The multiscale
moving-family and signed-balance proofs are paper-specific and are retained in full.
| A. Simplex | Gaussian |     | Soft-Packing |     | Energy Minimum |     |     |     |     |     |
| ---------- | -------- | --- | ------------ | --- | -------------- | --- | --- | --- | --- | --- |
Proof of Proposition 3: Put t = nγ/4 and f (s) = exp{−ts/2}. Since
t
|     |     |     |     |     | (cid:26) | (cid:27) |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
|     |     |     |     |     | tM       | (cid:88) |     |     |     |     |
∥2),
|     |     |     | G   | (C) = | exp |     | f (∥c −c |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | -------- | --- | --- | --- |
|     |     |     |     | γ     | M   | −1  | t m      | ℓ   |     |     |
m̸=ℓ
and f is strictly completely monotone, the universal-optimality result in [11, Thm. 1.2, Table 1,
t
and the simplex special case] makes the embedded regular simplex the unique minimizer among
distinct M-point configurations. For n ≥ 2, continuity extends the same lower bound to the full
| labeled | tuple space, | including |     | coincident | codewords. |     |     |     |     |     |
| ------- | ------------ | --------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- |
For completeness, the equality case on this enlarged space follows from the centroid identity
| and strict | Jensen | convexity: |     |     |          |           |     |     |     |     |
| ---------- | ------ | ---------- | --- | --- | -------- | --------- | --- | --- | --- | --- |
|            |        |            |     |     | (cid:13) | (cid:13)2 |     |     |     |     |
M
|            |     |       |      | (cid:88) | (cid:13)(cid:88) | (cid:13)   |          |     |     |     |
| ---------- | --- | ----- | ---- | -------- | ---------------- | ---------- | -------- | --- | --- | --- |
|            |     |       |      |          | cTc = (cid:13)   | c (cid:13) | −M ≥ −M. |     |     |     |
|            |     |       |      |          | ℓ                | m(cid:13)  |          |     |     |     |
|            |     |       |      |          | m (cid:13)       |            |          |     |     |     |
|            |     |       |      |          | (cid:13)         | (cid:13)   |          |     |     |     |
|            |     |       |      | m̸=ℓ     | m=1              |            |          |     |     |     |
| Thus, with | N   | = M(M | −1), |          |                  |            |          |     |     |     |
M
|     |     |     |       |       | (cid:40) (cid:32) |          |      | (cid:33)(cid:41) |     |     |
| --- | --- | --- | ----- | ----- | ----------------- | -------- | ---- | ---------------- | --- | --- |
|     |     |     |       |       | 1                 | (cid:88) | 1    |                  |     |     |
|     |     | G   | (C) ≥ | N exp | t                 | cTc      | +    | ≥                | N . |     |
|     |     | γ   |       | M     |                   |          | m ℓ  |                  | M   |     |
|     |     |     |       |       | N                 |          | M −1 |                  |     |     |
M
m̸=ℓ
Attaining the value M(M −1) forces zero centroid and equal off-diagonal correlations, hence
correlation −1/(M −1) for every ordered pair. Thus the minimizers are exactly the embedded
regular simplices, up to orthogonal transformation and relabeling. The case n = 1,M = 2 follows
| directly | by comparing |     | the | antipodal | and coincident |     | labeled pairs. |     |     |     |
| -------- | ------------ | --- | --- | --------- | -------------- | --- | -------------- | --- | --- | --- |

42
B. Best Fixed-Codebook Leading Coefficient in the Orthoplex-Bound Range
Proof of Proposition 4: Fix 2 ≤ k ≤ n, put M = n+k, and let C = {c ,...,c } ∈ P∗.
0 1 M
Since ρ∗ = 0, all off-diagonal correlations are nonpositive. Form the graph on [M] in which
M,n
cTc
m and ℓ are adjacent when < 0. Vectors belonging to different connected components are
m ℓ
orthogonal.
For a connected component of size s, let r be the rank of its Gram matrix G. The matrix
A = I − G is nonnegative and irreducible. Since G ⪰ 0, the largest eigenvalue of A is at
s
most one. If the component is linearly dependent, then one is an eigenvalue of A, and the
Perron–Frobenius theorem shows that it is simple. Thus every component has nullity either zero
or one. This is the connected-component form of the equality-case classification in [12, Thm. 3];
| see also | [13, Thm. 2.2]. |     |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- | --- |
Let ℓ be the number of dependent components. Since the full Gram matrix has rank at most n,
|     |     |     | ℓ ≥ M −n | = k. |     |     |
| --- | --- | --- | -------- | ---- | --- | --- |
Write the ranks of the dependent components as r ,...,r ≥ 1, so that their sizes are r +
1 ℓ 1
1,...,r +1. Let r ≥ 0 be the total size of the remaining, full-rank components. Then
| ℓ   | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
ℓ
(cid:88)
|     |     |     | r + (r | +1) = M. |     |     |
| --- | --- | --- | ------ | -------- | --- | --- |
|     |     |     | 0 i    |          |     |     |
i=1
If N denotes the number of ordered pairs having strictly negative correlation, then
−
ℓ
(cid:88)
|     |     | N   | ≤ r (r −1)+ | r (r +1). |     |     |
| --- | --- | --- | ----------- | --------- | --- | --- |
|     |     | −   | 0 0         | i i       |     |     |
i=1
Indeed, negative-correlation pairs can occur only within connected components, and the right-hand
| side bounds | all ordered | pairs within | those components. |     |     |     |
| ----------- | ----------- | ------------ | ----------------- | --- | --- | --- |
Merging r into any one of the r ’s can only increase the right-hand side, because
|     | 0     |              | i        |        |             |      |
| --- | ----- | ------------ | -------- | ------ | ----------- | ---- |
|     | (r +r | )(r +r +1)−r | (r −1)−r | (r +1) | = 2r (r +1) | ≥ 0. |
|     | 0     | i 0 i        | 0 0      | i i    | 0 i         |      |
For ℓ positive integers with sum n+k −ℓ, convexity then shows that the sum of r(r +1) is
maximized when one of them equals n+k −2ℓ+1 and the remaining ℓ−1 equal one. The
| resulting     | upper bound |                   |                   |               |      |     |
| ------------- | ----------- | ----------------- | ----------------- | ------------- | ---- | --- |
|               |             | (n+k −2ℓ+1)(n+k   |                   | −2ℓ+2)+2(ℓ−1) |      |     |
| is decreasing | over the    | feasible integers | ℓ ≥ k. Therefore, |               |      |     |
|               |             | N ≤               | (n−k +1)(n−k      | +2)+2(k       | −1). |     |
−

43
Every off-diagonal correlation is either negative or zero, and the ordered zero-correlation pairs
| are precisely | the ordered | closest-pair |           | indices. | Hence    |         |     |         |     |
| ------------- | ----------- | ------------ | --------- | -------- | -------- | ------- | --- | ------- | --- |
|               | |I (C       | )| =         | M(M −1)−N |          |          |         |     |         |     |
|               | max         | 0            |           |          | −        |         |     |         |     |
|               |             | ≥            | (n+k)(n+k |          | −1)−(n−k | +1)(n−k |     | +2)−2(k | −1) |
|               |             | =            | 4n(k −1). |          |          |         |     |         |     |
Conversely, take a regular (n−k+1)-simplex and k−1 antipodal pairs in mutually orthogonal
subspaces. All correlations within each block are strictly negative, all cross-block correlations are
zero, and the ordered zero-correlation count is exactly 4n(k−1). The codebook is packing-optimal,
| so minimizing | as in | (16) proves | (68). |     |     |     |     |     |     |
| ------------- | ----- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
C. Multiscale Construction in the Nonterminal Orthoplex-Bound Range
Proof of Proposition 5: Fix n ≥ 3 and 2 ≤ k < n, and put d = n−k. The Gram matrix
| specified | by (70) is |     |     |      |      |      |     |     |     |
| --------- | ---------- | --- | --- | ---- | ---- | ---- | --- | --- | --- |
|           |            |     |     | (1+q | )I−q | 11T. |     |     |     |
|           |            |     |     |      | γ    | γ    |     |     |     |
Its eigenvalues are 1+q , with multiplicity d−1, and 1−(d−1)q , with multiplicity one. It
|     |     | γ   |     |     |     |     |     | γ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is therefore positive definite for all sufficiently large γ. Taking its positive-definite square root
in a fixed basis of U produces the continuous realization specified in the body, and a ,...,a
1 d
| converge | to that basis. |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
j,
For each
d
(cid:88)
|     |     |     |     | aT  | a = 1−(d−1)q |     | .   |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
|     |     |     |     |     | i            |     | γ   |     |     |
j
i=1
| The definition | of v | therefore | gives |     |     |     |     |     |     |
| -------------- | ---- | --------- | ----- | --- | --- | --- | --- | --- | --- |
γ
dq2
|     |     | aTv |      |     | ∥2   |          | γ   |       |     |
| --- | --- | --- | ---- | --- | ---- | -------- | --- | ----- | --- |
|     |     |     | = −q | ,   | ∥v = |          |     | = p . |     |
|     |     | j   | γ    | γ   | γ    | 1−(d−1)q |     | γ     |     |
γ
|         | v ∈ U | f ∈ | U⊥, |     |          |     |      |     |     |
| ------- | ----- | --- | --- | --- | -------- | --- | ---- | --- | --- |
| Because | γ and | i   |     |     |          |     |      |     |     |
|         |       |     | ∥v  | ±r  | f ∥2 = p | +r2 | = 1. |     |     |
|         |       |     |     | γ   | γ i γ    | γ   |      |     |     |
For sufficiently large γ, p < 1/2, so the points in (72) are distinct and form a spherical codebook
γ
of size 2k + d = n + k. Since v → 0, r → 1, and the auxiliary vectors converge to an
|     |     |     |     | γ   | γ   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orthonormal basis of U, this codebook converges to the stated deleted cross-polytope.

44
Write a shifted point as x = v +sr f , where s ∈ {−1,1}. Its pair correlations are
|     |     |         |       |        | i,s γ        | γ   | i    |             |     |         |          |     |     |
| --- | --- | ------- | ----- | ------ | ------------ | --- | ---- | ----------- | --- | ------- | -------- | --- | --- |
|     |     | pair    | class |        |              |     |      | correlation |     | ordered | count    |     |     |
|     |     | shifted |       | points | on different |     | axes |             | p   |         | 4k(k −1) |     |     |
γ
|     |     | opposite |     | points | on one | shifted | axis |     | 2p −1 |     | 2k  |     |     |
| --- | --- | -------- | --- | ------ | ------ | ------- | ---- | --- | ----- | --- | --- | --- | --- |
γ
|     |     | pairs | involving |     | auxiliary | points |     |     | −q  | d(d+4k | −1). |     |     |
| --- | --- | ----- | --------- | --- | --------- | ------ | --- | --- | --- | ------ | ---- | --- | --- |
γ
Indeed, xT x = p for i ̸= j, xT x = 2p −1, and every off-diagonal pair containing an
|     |     | i,s j,t | γ   |     | i,1 | i,−1 | γ   |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
auxiliary point has correlation −q . The last count is the sum of d(d−1) ordered auxiliary–
γ
auxiliary pairs and 4kd ordered auxiliary–shifted pairs. The counts satisfy
|     |     |     | 4k(k | −1)+2k | +d(d+4k |     | −1) | =   | (n+k)(n+k |     | −1). |     | (95) |
| --- | --- | --- | ---- | ------ | ------- | --- | --- | --- | --------- | --- | ---- | --- | ---- |
For every sufficiently large finite γ, p > 0 > −q and 2p −1 < 0. Hence ρ (C ) = p ,
|     |     |     |     |     |     | γ   |     | γ   |     | γ   |     | max γ | γ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
attained by the 4k(k −1) ordered cross-axis pairs. Since (66) gives ρ∗ = 0, summing the
n+k,n
| three | pair       | classes | proves | (73). |       |          |       |     |     |     |     |     |     |
| ----- | ---------- | ------- | ------ | ----- | ----- | -------- | ----- | --- | --- | --- | --- | --- | --- |
| The   | definition |         | of q   | gives | nγq = | log(nγ), | while |     |     |     |     |     |     |
|       |            |         |        | γ     | γ     |          |       |     |     |     |     |     |     |
(cid:18) [log(nγ)]2(cid:19)
d[log(nγ)]2
|     |     |     |     | nγp | =             |     |     | = O |     |     | .   |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | γ nγ[1−(d−1)q |     |     | ]   |     | nγ  |     |     |     |
γ
This proves (74). In (73), the first term therefore tends to 4k(k −1), while the second and third
| terms | vanish. | Thus | (75) | holds. |     |     |     |     |     |     |     |     |     |
| ----- | ------- | ---- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Finally, V (n+k,n) ≤ G (C ). Taking limits and using Theorem 2 proves (76). The constructed
|     |     | γ   |     | γ   | γ   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
family has uniformly bounded Gaussian soft-packing energy, so Theorem 1 and (75) give (77).
| D.  | Terminal | Orthoplex  |     | Endpoint |           |       |     |     |     |     |     |     |     |
| --- | -------- | ---------- | --- | -------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     | Proof    | of Theorem |     | 4: Put   | t = nγ/4. | Since | ρ∗  | =   | 0,  |     |     |     |     |
2n,n
(cid:88)
exp{tcTc
|     |     |     |     |     | G   | (C) = |     |     | }.  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | γ   |       |     |     | m ℓ |     |     |     |     |
m̸=ℓ
|     |     |     |     |     | exp{txTy} |     |     | etf | (∥x−y∥2), |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- | --- | --- | --- |
With f (s) = exp{−ts/2}, one has = and f is strictly completely
|     | t   |     |     |     |     |     |     | t   |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
monotone. Universal optimality of the full cross-polytope therefore makes it a global soft-packing
energy minimizer [11, Thm. 1.2 and Table 1]; continuity extends the lower bound to the labeled
| tuple | space | allowing |     | coincidences. |     |     |     |     |     |     |     |     |     |
| ----- | ----- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The cross-polytope has 4n(n−1) ordered orthogonal pairs and 2n ordered antipodal pairs. Their
respective contributions to G (C ) are 1 and e−t, respectively, proving (78). Theorem 2 and
γ cross

45
Proposition 4, specialized to k = n, give (79). Corollary 2 together with (67), again specialized
k = n,
| to  | gives | (80). |     |     |     |     |     |     |     |
| --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Finally, the fixed cross-polytope is an exact soft-packing energy minimizer at every SNR.
| Corollary | 3, applied |     | with zero | objective |     | gap,    | gives |     |     |
| --------- | ---------- | --- | --------- | --------- | --- | ------- | ----- | --- | --- |
|           |            |     |           |           | P   | (C      | ;γ)   |     |     |
|           |            |     |           |           |     | e cross | −→    | 1,  |     |
P∗(2n,n;γ)
e
which proves relative-error optimality of this particular fixed codebook.
| E. Signed-Balance |     | Converse |     | at the | Left | Endpoint |     |     |     |
| ----------------- | --- | -------- | --- | ------ | ---- | -------- | --- | --- | --- |
Proof of Proposition 6: By (66), specialized to k = 2, the normalization in G has ρ∗ = 0.
γ n+2,n
Put t = nγ/4 and ϱ = ρ (C). If two codewords coincide, then ϱ = 1, and their two ordered
max
terms give
8
|     |     |     |     | G (C) | ≥ 2exp{t} |     | ≥ 2 | =   | .   |
| --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- |
γ
(1+ϱ)2
| We may | therefore | assume |     | that the | codewords |     | are distinct. |     |     |
| ------ | --------- | ------ | --- | -------- | --------- | --- | ------------- | --- | --- |
By Radon’s theorem [21], after discarding zero weights there are disjoint nonempty index sets
J and J , positive probability weights (α ) and (β ) , and µ ∈ Rn such that
| +         | −     |       |     |                |          | i   | i∈J+     | j j∈J−  |     |
| --------- | ----- | ----- | --- | -------------- | -------- | --- | -------- | ------- | --- |
|           |       |       |     |                | (cid:88) |     | (cid:88) |         |     |
|           |       |       |     |                | α        | c = | β        | c = µ.  |     |
|           |       |       |     |                |          | i i | j        | j       |     |
|           |       |       |     | i∈J+           |          |     | j∈J−     |         |     |
| For every | i ∈ J | , the | J   | representation |          | and | cTc ≥    | −1 give |     |
|           |       | +     | +   |                |          |     | i h      |         |     |
(cid:88)
|     |     |     | cTµ |     |     | cTc   |           |     |            |
| --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ---------- |
|     |     |     | =   | α + | α   |       | ≥ α −(1−α |     | ) = 2α −1. |
|     |     |     | i   | i   |     | h i h | i         |     | i i        |
h∈J+
h̸=i
| The J | representation |     | instead | gives |     |     |     |     |     |
| ----- | -------------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
−
(cid:88)
|     |     |     |     |     | cTµ | =   | β cTc | ≤ ϱ. |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- |
|     |     |     |     |     | i   |     | j i   | j    |     |
j∈J−
Interchanging the two sets gives the analogous bound for each β . Hence
j
1+ϱ
|     |     |     |     |     | ∥α∥ | , ∥β∥ | ≤   | .   |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     |     |     | ∞     | ∞   |     |     |
2
| Since | (cid:80) α | β = | 1, weighted | AM–GM |     | applied | to  |     |     |
| ----- | ---------- | --- | ----------- | ----- | --- | ------- | --- | --- | --- |
i j
i,j
exp{tcTc
}
|     |     |     |     |     | i   | j   | with weight | α   | β   |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
i j
α β
|     |     |     |     |     | i j |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
yields
(cid:88) (cid:88)
|     |     |     |     | S   | :=  |     | exp{tcTc | }   |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
i j
i∈J+j∈J−

46
exp{t∥µ∥2}
≥
|            |     |     |              |     | (cid:89) |      | (cid:89) |     |        |     |
| ---------- | --- | --- | ------------ | --- | -------- | ---- | -------- | --- | ------ | --- |
|            |     |     |              |     |          | ααi  | β βj     |     |        |     |
|            |     |     |              |     |          | i    | j        |     |        |     |
|            |     |     |              |     | i∈J+     | j∈J− |          |     |        |     |
|            |     |     |              |     |          | 1    |          | 4   |        |     |
|            |     |     |              |     | ≥        |      | ≥        |     | .      |     |
|            |     |     |              |     | ∥α∥      | ∥β∥  | (1+ϱ)2   |     |        |     |
|            |     |     |              |     |          | ∞    | ∞        |     |        |     |
| exp{t∥µ∥2} |     |     |              |     |          |      | (cid:80) |     |        |     |
| Here       |     | ≥   | 1. Moreover, |     | α ≤ ∥α∥  |      | and      | α = | 1 give |     |
|            |     |     |              |     | i        | ∞    |          | i i |        |     |
(cid:89)
|     |     |     |     |     |     | ααi | ≤ ∥α∥ | ,   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
∞
i
i
and the analogous inequality holds for β. The full energy contains both ordered orientations of
| every cross | pair, | so  | G (C) | ≥ 2S, | proving | (81). |     |     |     |     |
| ----------- | ----- | --- | ----- | ----- | ------- | ----- | --- | --- | --- | --- |
γ
For the asymptotic consequence, let CG minimize G and write ϱ = ρ (CG). Evaluation at
|     |     |     |     |     |     | γ   |     | γ   | γ max | γ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
any packing-optimal codebook gives V (n+2,n) ≤ (n+2)(n+1). Hence (28), with ρ∗ = 0,
|         |              |     |          |     | γ          |       |       |        |       | n+2,n |
| ------- | ------------ | --- | -------- | --- | ---------- | ----- | ----- | ------ | ----- | ----- |
| gives ϱ | = O((nγ)−1). |     | Applying |     | the finite | bound | to CG | proves | (82). |       |
γ
γ
REFERENCES
[1] J. G. Proakis, Digital Communications, 4th ed. New York, NY, USA: McGraw-Hill, 2001.
[2] A. Alvarado, E. Agrell, and F. Bra¨nnstro¨m, “Asymptotic comparison of ML and MAP detectors for multidimensional
constellations,” IEEE Transactions on Information Theory, vol. 64, no. 2, pp. 1231–1240, 2018.
[3] C. E. Shannon, “Probability of error for optimal codes in a Gaussian channel,” Bell System Technical Journal, vol. 38,
| no. 3, | pp. 611–656, |     | 1959. |     |     |     |     |     |     |     |
| ------ | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
[4] R. A. Rankin, “The closest packing of spherical caps in n dimensions,” Proceedings of the Glasgow Mathematical
| Association, |     | vol. 2, | no. 3, pp. | 139–144, | 1955. |     |     |     |     |     |
| ------------ | --- | ------- | ---------- | -------- | ----- | --- | --- | --- | --- | --- |
[5] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, 3rd ed., ser. Grundlehren der mathematischen
| Wissenschaften. |     | New | York, | NY, USA: | Springer-Verlag, |     | 1999, vol. | 290. |     |     |
| --------------- | --- | --- | ----- | -------- | ---------------- | --- | ---------- | ---- | --- | --- |
[6] T.EricsonandV.Zinoviev,Eds.,CodesonEuclideanSpheres,ser.North-HollandMathematicalLibrary. Amsterdam,The
| Netherlands: |     | Elsevier, | 2001, vol. | 63. |     |     |     |     |     |     |
| ------------ | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
[7] P.Delsarte,J.-M.Goethals,andJ.J.Seidel,“Sphericalcodesanddesigns,”GeometriaeDedicata,vol.6,no.3,pp.363–388,
1977.
[8] V.I.Levenshtein,“Universalboundsforcodesanddesigns,”inHandbookofCodingTheory,V.S.PlessandW.C.Huffman,
| Eds. | Amsterdam, |     | The Netherlands: |     | Elsevier, 1998, | vol. | 1, ch. 6, | pp. 499–648. |     |     |
| ---- | ---------- | --- | ---------------- | --- | --------------- | ---- | --------- | ------------ | --- | --- |
[9] C. Bachoc and F. Vallentin, “New upper bounds for kissing numbers from semidefinite programming,” Journal of the
| American | Mathematical |     | Society, | vol. | 21, no. 3, | pp. 909–924, | 2008. |     |     |     |
| -------- | ------------ | --- | -------- | ---- | ---------- | ------------ | ----- | --- | --- | --- |
[10] ——, “Semidefinite programming, multivariate orthogonal polynomials, and codes in spherical caps,” European Journal of
| Combinatorics, |     | vol. | 30, no. 3, | pp. 625–637, | 2009. |     |     |     |     |     |
| -------------- | --- | ---- | ---------- | ------------ | ----- | --- | --- | --- | --- | --- |
[11] H. Cohn and A. Kumar, “Universally optimal distribution of points on spheres,” Journal of the American Mathematical
| Society, | vol. | 20, no. | 1, pp. 99–148, |     | 2007. |     |     |     |     |     |
| -------- | ---- | ------- | -------------- | --- | ----- | --- | --- | --- | --- | --- |
[12] W. Kuperberg, “Optimal arrangements in packing congruent balls in a spherical container,” Discrete & Computational
| Geometry, | vol. | 37, | no. 2, pp. | 205–212, | Feb. 2007. |     |     |     |     |     |
| --------- | ---- | --- | ---------- | -------- | ---------- | --- | --- | --- | --- | --- |

47
[13] E.J.King,D.G.Mixon,H.Parshall,andC.Wells,“Uniquelyoptimalcodesoflowcomplexityaresymmetric,”Journalof
| Experimental | Mathematics, |     | vol. 2, | no. 1, | pp. 81–113, | Mar. 2026. |
| ------------ | ------------ | --- | ------- | ------ | ----------- | ---------- |
[14] A. Mulgund, “Stochastic domination of Gaussian maxima: A resolution of the Weak Simplex Conjecture,” Jul. 2026,
| arXiv:2607.14087v4. |     | [Online]. | Available: |     | https://arxiv.org/abs/2607.14087 |     |
| ------------------- | --- | --------- | ---------- | --- | -------------------------------- | --- |
[15] A.V.Bondarenko,D.P.Hardin,andE.B.Saff,“Meshratiosforbest-packingandlimitsofminimalenergyconfigurations,”
| Acta Mathematica |     | Hungarica, |      |          |                 |       |
| ---------------- | --- | ---------- | ---- | -------- | --------------- | ----- |
|                  |     |            | vol. | 142, no. | 1, pp. 118–131, | 2014. |
[16] J. Alcala, R. Andreeva, V. A. Kobzar, D. G. Mixon, S. Na, S. Sule, and Y. Xie, “Neural collapse in the orthoplex regime,”
| Mar. 2026, | arXiv:2603.20587v1. |     | [Online]. |     | Available: | https://arxiv.org/abs/2603.20587 |
| ---------- | ------------------- | --- | --------- | --- | ---------- | -------------------------------- |
[17] R. D. Gordon, “Values of Mills’ ratio of area to bounding ordinate and of the normal probability integral for large values
of the argument,” The Annals of Mathematical Statistics, vol. 12, no. 3, pp. 364–366, Sep. 1941.
[18] J. Galambos and I. Simonelli, Bonferroni-Type Inequalities with Applications, ser. Probability and Its Applications. New
| York, NY, | USA: | Springer-Verlag, | 1996. |     |     |     |
| --------- | ---- | ---------------- | ----- | --- | --- | --- |
[19] A.J.Wilkie,“ModelcompletenessresultsforexpansionsoftheorderedfieldofrealnumbersbyrestrictedPfaffianfunctions
and the exponential function,” Journal of the American Mathematical Society, vol. 9, no. 4, pp. 1051–1094, 1996.
[20] L. van den Dries, Tame Topology and O-Minimal Structures, ser. London Mathematical Society Lecture Note Series.
| Cambridge, | UK: | Cambridge | University | Press, | 1998, | vol. 248. |
| ---------- | --- | --------- | ---------- | ------ | ----- | --------- |
[21] J. Radon, “Mengen konvexer Ko¨rper, die einen gemeinsamen Punkt enthalten,” Mathematische Annalen, vol. 83, pp.
113–115, 1921.
---- END DOCUMENT ----
