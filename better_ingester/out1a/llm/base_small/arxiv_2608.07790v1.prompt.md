Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Permutation theory governs long-term dynamics of critical Boolean networks
Venkata Sai Narayana Bavisettya, Matthew Wheelerb, Julian Vignesc, Matthew Stephen Jones
Jr.d, Ruodan Liue, Sean Campbelle, Claus Kadelkae,∗
aDepartment of Integrative Biology and Physiology, University of California, Los Angeles, CA, 90095, United States
bDepartment of Medicine, University of Florida, Gainesville, FL, 32611, United States
cPonte Vedra High School, Ponte Vedra Beach, FL, 32081, United States
dWatchung Hills Regional High School, Warren, NJ, 07059, United States
eDepartment of Mathematics, Iowa State University, Ames, IA 50011, United States
Abstract
Boolean networks are widely used to model gene regulatory dynamics, where long-term behavior is
organized by attractors — by both their number and their lengths. The number of attractors was
resolved recently, but the distribution of attractor lengths and its dependence on network archi-
tecture remain poorly understood. We address this for critical Boolean networks with connectivity
K = 1. Weshowthattheattractorstructureofthesenetworksisencodedbyapermutationinduced
by the network’s feedback loops, thereby recasting questions about attractor lengths as questions
about permutations and their arithmetic properties. In particular, the maximum attractor length
is determined by the order of the induced permutation. Using results of Erdős and Turán together
with a classical theorem of Landau, we show that almost all networks have attractors of length
√
at most exp[1 ln2N], while some networks support attractors as long as exp[ N lnN]. The mean
2
attractor length scales as exp[N1/3], reflecting the influence of rare networks whose exceptionally
long attractors dominate the expectation value. These results establish a direct connection between
Boolean network dynamics, combinatorics, and number theory, and identify the permutation in-
duced by the feedback loops as a central dynamical invariant governing attractor lengths in critical
Boolean networks.
Introduction
Gene regulatory networks govern fundamental cellular processes such as differentiation, develop-
ment, and signaling. Boolean network models, originally introduced by Kauffman [1], are discrete
dynamical systems that provide a simplified yet powerful framework for studying these networks. A
Booleannetworkcomprisesadirectedgraphwhosenodesrepresentgenesandwhoseedgesrepresent
regulatory interactions. Each node takes a binary state (on or off) and is updated in discrete time
steps according to an update rule. Starting from any initial state, the network eventually reaches a
periodic attractor: either a fixed point (period one) or a limit cycle (period greater than one). The
numberandlengths(periods)ofattractorsarekeyquantitiescharacterizingthelong-termdynamics
of the network. Attractors correspond to stable or recurring patterns of gene expression and are
commonly interpreted as distinct cell types or phenotypes. Despite their simplicity, Boolean net-
workshavesuccessfullyreproducedqualitativefeaturesofcellcycling, signaling, anddifferentiation,
attracting substantial interest in both biology and physics [2].
∗Corresponding author
Email address: ckadelka@iastate.edu (Claus Kadelka)
6202
guA
7
]NM.oib-q[
1v09770.8062:viXra

The most widely studied class of Boolean networks is the Kauffman NK model, in which each
of the N nodes receives input from exactly K regulators and updates according to a Boolean
function drawn independently at random [1]. Mathematical understanding of these networks differs
sharply across connectivity regimes. In the high-connectivity limit K = N, the dynamics are well
understood: the update rule corresponds to a random map on 2N states, the expected number of
attractorsgrowslinearlyinN,andmanydynamicalpropertiesincludingbasinsizedistributionshave
beencharacterizedanalytically[3]. Bycontrast,thelow-connectivityregimeK = 1,2hasprovenfar
more elusive: while several theoretical studies have characterized the number of attractors exactly
for K = 1 and derived lower bounds for K = 2 [4, 5, 6, 7, 8, 9], the distribution of attractor lengths
remains poorly understood.
Critical low-connectivity networks are of particular interest due to their connection to the criticality
hypothesis [10, 1], which posits that biological regulatory networks operate at the phase boundary
betweenorderedandchaoticdynamics, enablingabalancebetweenrobustnessandadaptability[11,
12, 13, 14]. Among critical networks, the K = 1 case is particularly tractable: its sparse, loop-
dominated structure admits exact analysis while still exhibiting nontrivial dynamics. It also has
broader relevance: in critical networks with connectivity K = 2, the majority of nodes freeze under
iteration, and the dynamically active core reduces effectively to a K = 1 structure [15]. Therefore,
understanding critical K = 1 networks is a necessary first step toward a principled theory of low-
connectivity Boolean dynamics.
A critical K = 1 Boolean network consists of N nodes, each receiving input from exactly one other
node and updating via either the identity or negation function. These K = 1 networks have been
studied extensively for decades [4, 15, 5, 16, 17]. Despite their simple structure, key dynamical
quantities have proven surprisingly difficult to resolve. The number of attractors was only recently
√
settled: Fink [7] showed that the expected number grows as (2/ e)N. Drossel [5] showed that the
√
meanattractorlengthgrowsatmostasexp(0.4 N), andFink[8]derivedanimprovedupperbound
in terms of the number of relevant nodes, but neither bound is tight, leaving the true asymptotic
scaling unresolved.
In this article, we resolve the asymptotic scaling of attractor lengths in critical K = 1 Boolean
networks. The central insight is that the loop structure induces a permutation on the relevant
nodes whose order governs all attractor lengths, recasting the problem in terms of the arithmetic
properties of permutations. Using results of Erdős and Turán together with a classical theorem
of Landau, we show that asymptotically almost surely, the longest attractor in a random critical
K = 1 network has length at most exp[1 ln2N], while the longest attainable attractor across all
√ 2
such networks grows as exp[ N lnN]. Thus, typical and extremal networks exhibit very different
scalingofthemaximumattractorlength: almostallnetworkshavesub-exponentiallengths,whereas
rare networks attain exponentially larger ones. We further prove that the mean attractor length
is bounded above and below by constant multiples of the permutation order, implying that the
expected mean attractor length over all critical K = 1 networks scales as exp[N1/3].
Permutation determines long-term dynamics
The underlying graph of a critical K = 1 network decomposes naturally into directed loops with
trees rooted at the loop nodes (Fig. 1a). Each edge is either activating or inhibitory, and a loop is
positive if it contains an even number of inhibitory edges and negative otherwise. The long-term
dynamicsaregovernedentirelybytheloopnodes, calledtherelevant nodes, whilenodesonthetrees
affect only transient behavior [4, 15]. In particular, the number and lengths of attractors depend
only on the lengths and signs of the loops [17, 18].
2

(a)
|     | 8   | 11 12 |     | 16  |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- |
15
|     | 1   | 2   | 5   | 6   | (b) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
17 18
|     | 10 9 |     |     |     |     |     |       |     |
| --- | ---- | --- | --- | --- | --- | --- | ----- | --- |
|     |      |     |     |     |     | 1 2 | 3 4 5 | 6 7 |
σ:
|     | 4   | 3   | 19 7 |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
13
|     |     |     | 20  |     |     | 2 3 | 4 1 6 | 7 5 |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
14
Figure1: (a)TwodisjointK =1Booleannetworkcomponents,eachconsistingofaloopofrelevantnodes(numbered
1–4 and 5–7) with trees of non-relevant nodes branching out. (b) The corresponding permutation σ on the relevant
nodes, consisting of loops (1234) and (567): the top row lists each node and the arrow indicates its image under
σ.
Let m denote the number of relevant nodes. Within the subnetwork induced by these nodes, every
node has exactly one incoming and one outgoing edge. Thus, this subnetwork is naturally identified
with a permutation σ ∈ S . For example, the relevant subnetwork in Fig. 1a consists of a 4-loop
m
anda3-loop, correspondingtothepermutation(1 2 3 4)(5 6 7) ∈ S . Theorderofthispermutation
7
is the least common multiple of its cycle lengths, namely ord(σ) = lcm(4,3) = 12.
It is known that every attractor length divides twice the least common multiple of the loop lengths,
and,inparticularcases(e.g.,whenallloopsarepositive),dividestheleastcommonmultipleitself[5,
4]. Sincethelooplengthsareexactlythecyclelengthsoftheinducedpermutation, theseresultscan
be restated entirely in permutation-theoretic language: every attractor length in a critical K = 1
| network | divides 2ord(σ). |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
The order of the induced permutation also determines the mean attractor length and the number of
attractors. In a critical K = 1 network, the attractor states are in one-to-one correspondence with
the configurations of the m relevant nodes; there are therefore exactly 2m of them, and the mean
| attractor | length is |     |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
2m
A¯=
, (1)
c
where c is the total number of attractors. Since every attractor has length at most 2ord(σ),
A¯≤
2ord(σ), (2)
| and in | Theorem 1 in | the appendix | we establish | the | lower bound |     |     |     |
| ------ | ------------ | ------------ | ------------ | --- | ----------- | --- | --- | --- |
ord(σ)
≤ A¯. (3)
4
| A¯  |     |     |     |     |     |     |     | A¯  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thus and ord(σ) differ by at most a constant factor, so the asymptotic scaling of is set by that
| of ord(σ). | Equivalently, | the number | of attractors | satisfies |        |     |     |     |
| ---------- | ------------- | ---------- | ------------- | --------- | ------ | --- | --- | --- |
|            |               |            | 2m−1          |           | 2m+2   |     |     |     |
|            |               |            |               | ≤ c ≤     | ,      |     |     | (4) |
|            |               |            | ord(σ)        |           | ord(σ) |     |     |     |
2m/ord(σ).
so up to a constant factor c ∼ Therefore, questions about the long-term dynamics are
| naturally | reformulated | as questions | about | the induced | permutation. |     |     |     |
| --------- | ------------ | ------------ | ----- | ----------- | ------------ | --- | --- | --- |
This reformulation is the central conceptual advance underlying our analysis. Rather than study-
ing long-term dynamics directly as a property of Boolean networks, we instead study the induced
permutation. Different aspects of the dynamics are thereby recast as questions about different
permutation-theoretic invariants. More generally, this viewpoint establishes a bridge between
3

Boolean-networkdynamicsandpermutationtheory,openingthepossibilityofcharacterizingabroad
range of dynamical properties using the rich algebraic, combinatorial, and probabilistic theory of
permutations.
| Typical | versus | extremal |     | maximum | attractor |     | lengths |     |     |     |
| ------- | ------ | -------- | --- | ------- | --------- | --- | ------- | --- | --- | --- |
Since attractor lengths are governed by permutation order, classical results on the order of random
permutations immediately yield asymptotic bounds for attractor lengths in random Boolean net-
works. In a celebrated series of papers, Erdős and Turán [19, 20, 21, 22] studied the distribution of
the order of a uniformly random permutation σ ∈ S . In particular, they showed that σ satisfies
m
|     |     |     |     | (cid:18) |     | (cid:18) |     | (cid:19)(cid:19) |     |     |
| --- | --- | --- | --- | -------- | --- | -------- | --- | ---------------- | --- | --- |
1+ϵ
ln2m
|     |     |     |     | P ord(σ) | ≤   | exp |     | > 1−δ |     | (5) |
| --- | --- | --- | --- | -------- | --- | --- | --- | ----- | --- | --- |
2
for any ϵ,δ > 0 and all sufficiently large m [19]. In other words, a typical random permutation has
sub-exponential order. Since the attractor lengths are bounded by 2ord(σ), and since the number
of relevant nodes satisfies m ≤ N, the maximum attractor length ℓ satisfies
max
|     |     |     |     | (cid:18) |     | (cid:18) |     | (cid:19)(cid:19) |     |     |
| --- | --- | --- | --- | -------- | --- | -------- | --- | ---------------- | --- | --- |
1+ϵ
ln2N
|     |     |     |     | P ℓ max | ≤ 2exp |     |     | > 1−δ |     | (6) |
| --- | --- | --- | --- | ------- | ------ | --- | --- | ----- | --- | --- |
2
for sufficiently large N. Thus, Erdős and Turán’s theorem immediately implies that almost all
critical K = 1 Boolean networks have sub-exponential maximum attractor lengths. By contrast,
| Landau | [23] showed | that |     |     |               |     | √   |       |     |     |
| ------ | ----------- | ---- | --- | --- | ------------- | --- | --- | ----- | --- | --- |
|        |             |      |     |     | max logord(σ) |     | ∼   | mlnm, |     | (7) |
σ∈Sm
√
so there exist networks whose maximum attractor length grows as Θ(exp[ N lnN]). Thus, the
permutation formulation reveals a striking dichotomy: typical critical K = 1 networks have sub-
exponential maximum attractor lengths, whereas extremal networks attain exponentially larger
ones.
| Scaling | of mean | attractor |        | length. |     |     |     |     |     |     |
| ------- | ------- | --------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
| Goh and | Schmutz | [24]      | proved | that    |     |     |     |     |     |     |
(cid:114)
m
|     |     |     |     | logE[ord(σ)] |     | =   | c   | (1+o(1)), |     | (8) |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --------- | --- | --- |
lnm
where c ≈ 2.99047. Since ln(m) grows slower than any polynomial power,
|     |     |     |     |     | logE[ord(σ)] |     | m1/2+o(1). |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | --- | --- |
|     |     |     |     |     |              |     | =          |     |     | (9) |
Therefore, the mean attractor length of networks with m relevant nodes scales as exp[m1/2+o(1)].
To obtain the expected mean attractor length over all critical K = 1 networks with N nodes, it
remains only to average over the distribution of the number of relevant nodes. By [7, 15],
|     |     |     |     |     |     |     | (cid:18) | m2(cid:19) |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --- |
m
|     |     |     |     |     | P(m) | ∼   | exp − | ,   |     | (10) |
| --- | --- | --- | --- | --- | ---- | --- | ----- | --- | --- | ---- |
|     |     |     |     |     |      | N   |       | 2N  |     |      |
so
∞
|     |     |     |       | (cid:88) | m   |                |     | (cid:16)          | (cid:17) |      |
| --- | --- | --- | ----- | -------- | --- | -------------- | --- | ----------------- | -------- | ---- |
|     |     |     | E[A¯] |          |     | (cid:0) −m2/2N |     | (cid:1) m1/2+o(1) |          |      |
|     |     |     |       | ∼        | exp |                |     | exp               | .        | (11) |
N
m=0
4

√
Setting m = N x and applying Laplace’s method (see Lemma 4) yields
(cid:16) (cid:17)
E[A¯] = exp N1/3+o(1) . (12)
Thus, although a typical critical K = 1 network possesses sub-exponential maximum attractor
length, the expected mean attractor length is dominated by rare networks whose exceptionally
large permutation order gives rise to much longer attractors.
Discussion.
We have shown that the scaling of attractor lengths in critical K = 1 Boolean networks is funda-
mentally governed by the order of the permutation induced by the network’s feedback loops. More
broadly, we identified the induced permutation as the natural mathematical object underlying long-
term network dynamics and reduces questions about these dynamics, such as attractor lengths, to
questionsinthetheoryofrandompermutations. CombiningclassicalresultsofErdősandTurán[19],
Landau’stheorem[23],andGohandSchmutz’sasymptoticsfortheexpectedpermutationorder[24],
we obtain a complete asymptotic picture: almost all networks have sub-exponential maximum at-
tractor lengths of order exp[O(ln2N)], whereas rare extremal networks attain lengths as large as
√
exp[Θ( N lnN)]. Averaging over all network realizations then yields an expected mean attractor
length of exp[N1/3+o(1)], demonstrating that expectation values are dominated by rare networks
with exceptionally large permutation order. Beyond these leading-order asymptotics, our approach
also provides exact, albeit algebraically involved, finite-N expressions for the mean attractor length
(see Eq. 21 in the appendix).
This distinction between typical and average behavior has important practical consequences. Be-
cause the distribution of attractor lengths is highly right-skewed, simulations that sample typical
trajectories systematically underestimate the mean attractor length and therefore cannot reliably
estimateexpecteddynamicalquantities[7]. Understandingthefulldistributionofattractorlengths,
rather than only its extreme and average behavior, therefore remains an important open problem.
Our analysis uses only the first layer of a much richer theory of random permutations. More
recent results on the distribution of permutation order, refined asymptotics for logord(σ) [25],
suggest that much more precise descriptions of attractor-length distributions should be obtainable.
More broadly, the induced permutation provides a unifying framework extending beyond attractor
lengths. Differentdynamicalquantities,includingthenumberofattractors,basin-sizestatistics,and
measures of dynamical entropy, depend on different arithmetic invariants of the same permutation,
making them natural targets for the methods of algebraic combinatorics and probabilistic number
theory.
Finally, the permutation-theoretic viewpoint may extend beyond the K = 1 setting considered
here. In critical K = 2 Boolean networks, the dynamically relevant core reduces asymptotically to
an effective K = 1 structure [15], suggesting that permutation-based methods may provide a route
toward resolving the long-standing problem of attractor statistics in critical Boolean networks with
higher connectivity.
Acknowledgments
The authors thank Maria Siskaki for useful comments and suggestions.
5

Appendix
This appendix contains a theorem together with its proof. The proof makes use of two lemmas that
we state and prove after the theorem. Additionally, there is a lemma that details the computation
| of the | asymptotic | for | the mean | attractor |     | length. |     |     |     |     |     |
| ------ | ---------- | --- | -------- | --------- | --- | ------- | --- | --- | --- | --- | --- |
A¯
Theorem 1. Suppose a critical K = 1 network has mean attractor length and permutation σ,
then
A¯
1
|     |     |     |     |     |     |        | ≥   | .   |     |     | (13) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | ord(σ) |     | 4   |     |     |      |
Proof. We proceed by a sequence of reductions. We first show that for any Boolean network F with
at least one negative feedback loop, the network F obtained by replacing all inhibitory edges with
+
activatingedgessatisfiesA¯(F ) ≤ A¯(F). SinceF andF sharethesameunderlyingdirectedgraph,
|     |     |     |     | +   |     |     |      | +   |               |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------------- | --- | --- |
|     |     |     |     |     |     |     | A¯(F |     | A¯(F)/ord(σ), |     |     |
they induce the same permutation σ, and therefore )/ord(σ) ≤ so it suffices to
+
prove the lower bound for networks consisting entirely of positive feedback loops. Within this class,
we then show that A¯/ord(σ) is minimized when every non-trivial (length > 1) feedback loop has a
prime-power length, so it suffices to consider networks of this form. Finally, we show that for any
A¯/ord(σ)
| such network |     |     | ≥ 1/4, | which | establishes |     | the | theorem. |     |     |     |
| ------------ | --- | --- | ------ | ----- | ----------- | --- | --- | -------- | --- | --- | --- |
Step 1: Reduction to positive loops. Let F be a critical K = 1 Boolean network containing at least
one component whose long-term dynamics are governed by a negative feedback loop of length n;
|     |     |     | C¯  |     | F′  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
we denote this component . Let be the network obtained from F by replacing all inhibitory
n
edges in C¯ with activating edges, leaving all other update functions unchanged. We now show that
n
A¯(F′) ≤ A¯(F). Applying this iteratively yields a network F consisting entirely of components
+
|     |     |     |     |     |     | A¯(F | A¯(F) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- | --- |
with positive feedback loops, satisfying ) ≤ and ord(σ ) = ord(σ ), so it suffices to
|           |       |       |       |     |     | +   |     |     | F+  | F   |     |
| --------- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| prove the | lower | bound | for F | + . |     |     |     |     |     |     |     |
Recall from Eq. (1) that A¯ = 2m/c, where m is the total number of relevant nodes across all
components and c is the number of attractors. It therefore suffices to show that c(F′) ≥ c(F).
G∪C¯
Writing F = , where G is the remainder of the network, the total number of attractors of F
n
is
|     |     |     |     |      |     | (cid:88) | (cid:88) |           |     |     |      |
| --- | --- | --- | --- | ---- | --- | -------- | -------- | --------- | --- | --- | ---- |
|     |     |     |     | c(F) | =   | g(P)     | c¯(ℓ)    | gcd(ℓ,P), |     |     | (14) |
|     |     |     |     |      |     | P        | ℓ        |           |     |     |      |
where g(P) is the number of attractors of length P in G, and c¯(ℓ) is the number of limit cycles of
C¯
length ℓ determined by the negative feedback loop of length n in [17, 18]:
n
|     |     |     |     |         |    |          |              |          | ℓ    |     |      |
| --- | --- | --- | --- | ------- | --- | -------- | ------------ | -------- | ---- | --- | ---- |
|     |     |     |     |         | 1   | (cid:88) |              | ifℓeven, | |n,  |     |      |
|     |     |     |     |         |   |          | µ(d)·2ℓ/(2d) |          | 2    |     |      |
|     |     |     |     |         |    |          |              |          | 2n   |     |      |
|     |     |     |     |         | ℓ  |          |              | and      | odd, |     |      |
|     |     |     |     | c¯(ℓ) = |     | d|ℓ/2    |              |          | ℓ    |     | (15) |
n/dodd
 

|     |     |     |     |     | 0  |     |     | otherwise. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
| F′  | G∪C |     |     |     |     |     |     |            | C¯  |     |     |
Since = differs from F only in that all inhibitory edges within have been replaced by
|     |     | n   |     |     |     |     |     |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F′
| activating | edges, | the | number | of attractors |     | of       | is       |     |     |     |     |
| ---------- | ------ | --- | ------ | ------------- | --- | -------- | -------- | --- | --- | --- | --- |
|            |        |     |        |               |     | (cid:88) | (cid:88) |     |     |     |     |
c(F′)
|     |     |     |     |     | =   | g(P) |     | c(ℓ) gcd(ℓ,P), |     |     | (16) |
| --- | --- | --- | --- | --- | --- | ---- | --- | -------------- | --- | --- | ---- |
|     |     |     |     |     |     | P    | ℓ   |                |     |     |      |
6

where c(ℓ) is the number of limit cycles of length ℓ determined by the positive feedback loop of
C
| length n | in  | n [17, 18]: |     |     |          |                   |           |     |
| -------- | --- | ----------- | --- | --- | -------- | ----------------- | --------- | --- |
|          |     |             |     |     | 1       | (cid:18) (cid:19) |           |     |
|          |     |             |     |     | (cid:88) | ℓ                 |           |     |
|          |     |             |     |     |         | µ 2d              | if ℓ | n, |     |

|     |     |     |     |      | ℓ   | d   |     |      |
| --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
|     |     |     |     | c(ℓ) | =   |     |     | (17) |
d|ℓ

|     |     |     |     |     | 0  |     | otherwise. |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
Note that when c(ℓ) and c¯(ℓ) are nonzero, their values depend only on ℓ and not on the loop length
n. Since g(P) ≥ 0, it suffices to show that for all positive integers n and P,
|     |     |     |     | (cid:88) |          | (cid:88) |                |      |
| --- | --- | --- | --- | -------- | -------- | -------- | -------------- | ---- |
|     |     |     |     | c¯(ℓ)    | gcd(ℓ,P) | ≤        | c(ℓ) gcd(ℓ,P). | (18) |
|     |     |     |     | ℓ        |          | ℓ        |                |      |
Restricting the sums to the support of c(ℓ) and c¯(ℓ) — namely divisors of n — and substituting the
| explicit | formulas | (17) | and (15), | Eq.      | (18) reduces              | to showing |            |      |
| -------- | -------- | ---- | --------- | -------- | ------------------------- | ---------- | ---------- | ---- |
|          |          |      |           | (cid:88) | (cid:16) (cid:17)(cid:16) | (cid:17)   | (cid:88)   |      |
|          |          |      |           |          | c¯ 2n 2n,P                | ≤          | c(d)(d,P). | (19) |
|          |          |      |           |          | q q                       |            |            |      |
|          |          |      |           | q|n      |                           |            | d|n        |      |
q odd
| This follows | from | Lemma | 2   | below, | which concludes | Step | 1.  |     |
| ------------ | ---- | ----- | --- | ------ | --------------- | ---- | --- | --- |
Step 2: Reduction to prime-power loop lengths. By Step 1, it suffices to consider networks in which
all feedback loops are positive, with non-trivial loop lengths l ,...,l . For such networks, the mean
1 k
A¯
attractor length depends only on the loop lengths l 1 ,...,l k and not on the tree structure of the
components, since the long-term dynamics are entirely determined by the relevant core. Therefore
A¯/Lisafunctionofthelooplengthsalone, anditismeaningfultominimizeoverallpossiblechoices
A¯≥
of loop lengths. Since ord(σ) = L = lcm(l ,...,l ), the lower bound ord(σ)/4 is equivalent to
|     |     |     |     |     | 1   | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
A¯/L ≥ 1/4. Applying Burnside’s lemma, the total number of attractors is
|     |     |     |     |     |     | L−1 k |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- |
1 (cid:88)(cid:89)
|     |     |     |     |     | c = | 2gcd(j,li), |     | (20) |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ---- |
L
j=0i=1
(cid:80)
| and since | A¯= | 2 li/c, | we have |     |     |     |     |     |
| --------- | --- | ------- | ------- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     | A¯  | (cid:80) |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- |
2 i li
|     |     |     |     |     | =                      |         | .          | (21) |
| --- | --- | --- | --- | --- | ---------------------- | ------- | ---------- | ---- |
|     |     |     |     |     | L (cid:80)L−1(cid:81)k |         | 2gcd(j,li) |      |
|     |     |     |     |     |                        | j=0 i=1 |            |      |
Note that loops of length 1 contribute equally to the numerator and denominator of Eq. (21) and
A¯/L,
therefore do not affect so it suffices to consider non-trivial loops only. We now show via two
observations thattheminimumofA¯/Loverall choicesof non-trivial looplengths occurswhen these
| lengths | are distinct | prime | powers. |     |     |     |     |     |
| ------- | ------------ | ----- | ------- | --- | --- | --- | --- | --- |
First, suppose one loop has length l = ab with gcd(a,b) = 1. Consider a new network F′ whose
1
relevant core consists of two components with loops of lengths a and b respectively, together with
theremainingloopsl ,...,l unchanged. Sincethelong-termdynamicsdependonlyontherelevant
|     |     | 2   | k   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
core,thetreestructureofthenewcomponentscanbearbitrary. Thenodesthatwereontheoriginal
F′, A¯/L
loop of length ab are accounted for by trivial loops of length 1 in which do not affect as
established above. Since gcd(a,b) = 1, we have lcm(a,b,l ,...,l ) = lcm(ab,l ,...,l ) = L, so the
2 k 2 k
| denominator |     | L is unchanged. |     | We  | claim that |       |     |      |
| ----------- | --- | --------------- | --- | --- | ---------- | ----- | --- | ---- |
|             |     |                 |     |     | A¯(F′)     | A¯(F) |     |      |
|             |     |                 |     |     |            | ≤     | ,   | (22) |
|             |     |                 |     |     | L          |       | L   |      |
7

A¯/L.
i.e. splitting a composite-length loop into coprime parts does not increase This follows from
| the pointwise |                  | inequality |                                |     |                               |     |     |       |     |      |
| ------------- | ---------------- | ---------- | ------------------------------ | --- | ----------------------------- | --- | --- | ----- | --- | ---- |
|               |                  |            | gcd(j,ab)                      |     | ≤ gcd(j,a)+gcd(j,b)+ab−a−b−1, |     |     |       |     | (23) |
| which         | gives 2gcd(j,ab) |            | ≤ 2gcd(j,a)·2gcd(j,b)·2ab−a−b, |     |                               |     | and | hence |     |      |
|               |                  |            | L−1                            | k   |                               |     |     |       |     |      |
|               |                  |            | (cid:88)(cid:89)               |     | 2gcd(j,li)·2gcd(j,ab)         |     |     |       |     |      |
j=0i=2
L−1 k
|     |     |     |     | 2ab−a−b |     | (cid:88)(cid:89) | 2gcd(j,li)·2gcd(j,a)·2gcd(j,b). |     |     |      |
| --- | --- | --- | --- | ------- | --- | ---------------- | ------------------------------- | --- | --- | ---- |
|     |     |     |     | ≤       |     |                  |                                 |     |     | (24) |
j=0i=2
Eq. (22) follows from simple alebraic manifpulation. Repeated application reduces to networks
| where | every non-trivial |     | loop | length | is a | prime | power. |     |     |     |
| ----- | ----------------- | --- | ---- | ------ | ---- | ----- | ------ | --- | --- | --- |
Second, suppose the relevant core contains a loop of length d such that d divides lcm(l ,...,l ),
2 k
F′′
so that L is unchanged by removing it. Consider the network obtained by removing this loop
from the relevant core (replacing it with trivial loops of length 1). The numerator of Eq. (21) loses
(cid:80)L−12gcd(j,d)
a factor of 2d, while the denominator loses a factor of 1 ≤ 2d, since gcd(j,d) ≤ d for
L j=0
A¯/L,
all j. Hence removing such a loop does not decrease so the minimum is achieved for networks
| whose | non-trivial | loop | lengths | are | distinct | prime | powers. |     |     |     |
| ----- | ----------- | ---- | ------- | --- | -------- | ----- | ------- | --- | --- | --- |
Combining these two observations, it suffices to prove A¯/L ≥ 1/4 for networks whose relevant core
consists of loops of distinct prime-power lengths pa 1,...,pa r with distinct primes p .
|     |     |     |     |     |     |     | 1   | r   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Step 3: Lower bound for prime-power loop lengths. For networks with distinct prime-power loop
lengthspa1,...,par, thelooplengthsarepairwisecoprime, sogcd(j,pai)dependsonlyonj mod pai.
|     | 1   | r   |     |     |     |     |     |     | i   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Applying the Chinese Remainder Theorem to Eq. (20) therefore gives the factorization
|     |     |     |     |     | A¯(pa1,...,par) |     |     | r A¯(pai) |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --------- | --- | --- |
(cid:89)
|     |     |     |     |     | 1   |     | r = | i . |     | (25) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
pai
L
|     |     |     |     |     |     |     | i=1 | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For a single positive loop of prime-power length pa, evaluating Eq. (21) explicitly gives
|     |     |     |     | A¯(pa) |     |     | 2pa |     |     |      |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |        | =   |     |     |     | ,   | (26) |
(cid:80)a
|     |     |     |     | pa  | 2pa | +   | pj−1(p−1)·2pa−j |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
j=1
| which | at a = 1 | reduces | to        |     |         |     |           |     |     |      |
| ----- | -------- | ------- | --------- | --- | ------- | --- | --------- | --- | --- | ---- |
|       |          |         |           |     | A¯(p)   |     | 2p        |     |     |      |
|       |          |         |           |     |         | =   |           | .   |     | (27) |
|       |          |         |           |     |         | p   | 2p+2(p−1) |     |     |      |
|       |          |         | A¯(pa)/pa |     | A¯(p)/p |     |           |     |     |      |
By Lemma 3 below, ≥ for all a ≥ 1, so combining with the factorization gives
|     |     |     |     | A¯  | r        | A¯(pa i) | r        | A¯(p ) |     |      |
| --- | --- | --- | --- | --- | -------- | -------- | -------- | ------ | --- | ---- |
|     |     |     |     |     | (cid:89) |          | (cid:89) | i      |     |      |
|     |     |     |     |     | =        | i        | ≥        |        |     | (28) |
|     |     |     |     | L   |          | pai      |          | p      |     |      |
i
|     |     |     |     |     | i=1      | i   | i=1 |          |     |      |
| --- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- | ---- |
|     |     |     |     |     | (cid:89) |     | 2p  |          |     |      |
|     |     |     |     |     | ≥        |     |     | =: R min | ,   | (29) |
2p+2(p−1)
pprime
where the last inequality holds since each factor is less than one, so extending the finite product to
all primes can only decrease it. The infinite product R converges, and a numerical computation
min
|     |     |     |     |     |     |     | A¯/L |     | A¯≥ |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
gives R min ∼ 0.32 > 1/4, from which we conclude ≥ 1/4, i.e. ord(σ)/4.
8

We now proveLemma 2, Lemma 3 thatwererequired in the proofof Theorem 1. Thesetwo lemmas
| were formally | verified | using | the | Aristotle | API | [26]. |     |     |     |     |
| ------------- | -------- | ----- | --- | --------- | --- | ----- | --- | --- | --- | --- |
Lemma 2. With c(ℓ) and c¯(ℓ) as in Eqs. (17) and (15), the following identity holds for all positive
| integers | k:  |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|     |     |     |     | c¯(2k)·2k | =   |     |     | d·c(d). |     | (30) |
| --- | --- | --- | --- | --------- | --- | --- | --- | ------- | --- | ---- |
d|k
|     |     |     |     |     |     | k/d a power | of  | 2   |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
Proof. Sinceeverystateofapositiveloopoflengthnliesonanattractor, thetotalnumberofstates
| in limit | cycles satisfies | [17] |     |     |          |         |     |     |     |      |
| -------- | ---------------- | ---- | --- | --- | -------- | ------- | --- | --- | --- | ---- |
|          |                  |      |     |     | (cid:88) | c(d′)d′ | 2n. |     |     |      |
|          |                  |      |     |     |          |         | =   |     |     | (31) |
d′|n
Substituting n = k/d into Eq. (31) and inserting into the formula for c¯(2k) from Eq. (15) gives
|     |     |     |           |     | (cid:88) |       | (cid:88) |          |     |      |
| --- | --- | --- | --------- | --- | -------- | ----- | -------- | -------- | --- | ---- |
|     |     |     | c¯(2k)·2k |     | =        | µ(d)· |          | c(d′)d′. |     | (32) |
|     |     |     |           |     | d|k      |       | d′|(k/d) |          |     |      |
k/dodd
(cid:80)
Exchangingtheorderofsummation,thecoefficientofc(d′)d′ becomes µ(e),whichequals
e|(k/d′)
k/(ed′)odd
| 1 if k/d′ | is a power | of 2 | and 0 otherwise. |     | This | yields |     |     |     |     |
| --------- | ---------- | ---- | ---------------- | --- | ---- | ------ | --- | --- | --- | --- |
(cid:88)
|     |     |     |     | c¯(2k)·2k | =   |     |     | d′·c(d′), |     | (33) |
| --- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- | ---- |
d′|k
k/d′ apowerof2
| which is | the required | equality. |     |     |     |     |     |     |     |     |
| -------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
A¯(pa)/pa
Lemma 3. The ratio is minimized at a = 1, i.e. for any prime p and positive integer a,
|     |     |     | 2p  |     |     |     | 2pa |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | ≤   |     |     |     | .   | (34) |
(cid:80)a
|     |     |     | 2p+2(p−1) |     | 2pa | +   | pj−1(p−1)·2pa−j |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --------------- | --- | --- | --- |
j=1
Proof. Since all quantities are positive, both sides have the form X/(X +Y) and cross-multiplying
| reduces | the inequality | to  |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a
(cid:88)
|     |     |     | 2p· | pj−1(p−1)·2pa−j |     |     | ≤ 2(p−1)·2pa |     | .   | (35) |
| --- | --- | --- | --- | --------------- | --- | --- | ------------ | --- | --- | ---- |
j=1
| Factoring | out p−1 | > 0 | reduces | this to |     |     |     |     |     |     |
| --------- | ------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
a
(cid:88)
|     |     |     |     | 2p· | pj−1·2pa−j |     | ≤ 2pa+1, |     |     | (36) |
| --- | --- | --- | --- | --- | ---------- | --- | -------- | --- | --- | ---- |
j=1
2p,
which we prove by induction on a. For a = 1 both sides equal so equality holds. Assuming
| Eq. (36) | at level a, | the left-hand |                       | side | at level | a+1      | is  |                     |     |     |
| -------- | ----------- | ------------- | --------------------- | ---- | -------- | -------- | --- | ------------------- | --- | --- |
|          |             |               |                       |      |          |         |     |                     |    |     |
|          |             |               | a+1                   |      |          |          |     | a                   |     |     |
|          |             |               | (cid:88) pj−1·2pa+1−j |      |          | 2p·2pa  |     | (cid:88) pj−1·2pa−j |     |     |
|          |             | 2p            |                       |      | =        |          | +p· |                     |    |     |
|          |             |               | j=1                   |      |          |          |     | j=1                 |     |     |
|          |             |               |                       |      |          | (cid:18) |     | 2pa+1(cid:19)       |     |     |
|          |             |               |                       |      |          | 2p·      | 2pa |                     |     |     |
|          |             |               |                       |      | ≤        |          | +p· |                     |     |     |
2p
|     |     |     |     |     | =   | 2pa ·(2p+2p), |     |     |     | (37) |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ---- |
9

where we used the inductive hypothesis in the second line. It therefore suffices to show that
|       |         |     |         |     |        | 2pa+1−pa | 2p−1+p.       |                |          |           |      |
| ----- | ------- | --- | ------- | --- | ------ | -------- | ------------- | -------------- | -------- | --------- | ---- |
|       |         |     |         |     |        |          | ≥             |                |          |           | (38) |
|       | pa+1−pa |     | pa(p−1) |     |        |          |               |                | 2pa+1−pa | 2p 2·2p−1 |      |
| Since |         | =   |         | ≥   | p(p−1) | ≥ p      | for p ≥ 2 and | a ≥ 1, we have |          | ≥ ≥       | ≥    |
2p−1+p, where the last step uses 2p−1 ≥ p, which holds for all primes p.
Finally, we prove the Lemma 4 required to compute the asymptotics of the mean attractor length.
| Lemma | 4.  | The integral |     |     |     |     |     |     |     |     |     |
| ----- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:90) ∞
|     |     |     |     |     |     | I = | xeϕN(x)dx, |     |     |     | (39) |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ---- |
0
where
x2
|     |     |     |     |     | ϕ   | (x) = | − + (cid:0) Nx2(cid:1)1/4+o(1) | ,   |     |     | (40) |
| --- | --- | --- | --- | --- | --- | ----- | ------------------------------ | --- | --- | --- | ---- |
N
2
satisfies
N1/3+o(1).
|     |     |     |     |     |     | logI | =   |     |     |     | (41) |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ---- |
Proof. Since ϕ (x) → −∞ as x → ∞, the integral is dominated by the unique maximum of ϕ .
|         |       | N   |         |     |            |     |                   |     |     |     | N    |
| ------- | ----- | --- | ------- | --- | ---------- | --- | ----------------- | --- | --- | --- | ---- |
| Setting | ϕ′ (x | ) = | 0 gives | x = | N1/6+o(1), |     | at which          |     |     |     |      |
|         | N     | ∗   |         | ∗   |            |     |                   |     |     |     |      |
|         |       |     |         |     |            | ϕ   | (x ) = N1/3+o(1). |     |     |     | (42) |
|         |       |     |         |     |            | N   | ∗                 |     |     |     |      |
Applying Laplace’s method [27] and absorbing sub-exponential prefactors into the o(1) exponent,
we conclude
|     |     |     |     |     |     | logI | = N1/3+o(1). |     |     |     | (43) |
| --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | --- | --- | ---- |
References
[1] Stuart A Kauffman. Metabolic stability and epigenesis in randomly constructed genetic nets.
|     | Journal | of theoretical |     | biology, |     | 22(3):437–467, | 1969. |     |     |     |     |
| --- | ------- | -------------- | --- | -------- | --- | -------------- | ----- | --- | --- | --- | --- |
[2] Rui-Sheng Wang, Assieh Saadatpour, and Reka Albert. Boolean modeling in systems biology:
an overview of methodology and applications. Physical biology, 9(5):055001, 2012.
[3] Bernard Derrida and H Flyvbjerg. The random map model: a disordered model with deter-
|     | ministic | dynamics. |     | Journal | de  | Physique, | 48(6):971–978, | 1987. |     |     |     |
| --- | -------- | --------- | --- | ------- | --- | --------- | -------------- | ----- | --- | --- | --- |
[4] Henrik Flyvbjerg and NJ Kjr. Exact solution of kauffman’s model with connectivity one.
Journal of Physics A: Mathematical and General, 21(7):1695–1718, 1988.
[5] Barbara Drossel, Tamara Mihaljev, and Florian Greil. Number and length of attractors in a
critical kauffman model with connectivity one. Physical review letters, 94(8):088701, 2005.
[6] Barbara Drossel. Number of attractors in random boolean networks. Physical Review
E—Statistical, Nonlinear, and Soft Matter Physics, 72(1):016110, 2005.
[7] TMAFinkandFCSheldon. Numberofattractorsinthecriticalkauffmanmodelisexponential.
|     | Physical | Review | Letters, |     | 131(26):267402, |     | 2023. |     |     |     |     |
| --- | -------- | ------ | -------- | --- | --------------- | --- | ----- | --- | --- | --- | --- |
10

[8] FCSheldonandTMAFink. Insightsfromnumbertheoryintothecriticalkauffmanmodelwith
connectivity one. Journal of Physics A: Mathematical and Theoretical, 57(27):275003, 2024.
[9] Björn Samuelsson and Carl Troein. Superpolynomial growth in the number of attractors in
| kauffman | networks. |     | Physical | Review | Letters, | 90(9):098701, |     | 2003. |
| -------- | --------- | --- | -------- | ------ | -------- | ------------- | --- | ----- |
[10] Stuart A Kauffman. The origins of order: Self-organization and selection in evolution. In Spin
| glasses | and biology, |     | pages | 61–100. | World | Scientific, | 1992. |     |
| ------- | ------------ | --- | ----- | ------- | ----- | ----------- | ----- | --- |
[11] Maximino Aldana, Enrique Balleza, Stuart Kauffman, and Osbaldo Resendiz. Robustness and
evolvabilityingeneticregulatorynetworks. Journal of theoretical biology,245(3):433–448,2007.
[12] Enrique Balleza, Elena R Alvarez-Buylla, Alvaro Chaos, Stuart Kauffman, Ilya Shmulevich,
and Maximino Aldana. Critical dynamics in genetic regulatory networks: examples from four
| kingdoms. | PLoS | One, | 3(6):e2456, |     | 2008. |     |     |     |
| --------- | ---- | ---- | ----------- | --- | ----- | --- | --- | --- |
[13] Bryan C Daniels, Hyunju Kim, Douglas Moore, Siyu Zhou, Harrison B Smith, Bradley Karas,
Stuart A Kauffman, and Sara I Walker. Criticality distinguishes the ensemble of biological
| regulatory | networks. |     | Physical | review | letters, | 121(13):138102, |     | 2018. |
| ---------- | --------- | --- | -------- | ------ | -------- | --------------- | --- | ----- |
[14] Claus Kadelka, Taras-Michael Butrie, Evan Hilton, Jack Kinseth, Addison Schmidt, and Haris
Serdarevic. A meta-analysis of Boolean network models reveals design principles of gene regu-
| latory networks. |     | Science | advances, |     | 10(2):eadj0822, |     | 2024. |     |
| ---------------- | --- | ------- | --------- | --- | --------------- | --- | ----- | --- |
[15] Barbara Drossel. Random boolean networks. Reviews of nonlinear dynamics and complexity,
| pages 69–110, |     | 2008. |     |     |     |     |     |     |
| ------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
[16] Shan-Tarng Chen, Hsen-Che Tseng, Shu-Chin Wang, and Ping-Cheng Li. Investigation of the
dynamics of critical k= 2 kauffman networks using second-order loops. Journal of the Physical
| Society | of Japan, | 77(9):094002, |     | 2008. |     |     |     |     |
| ------- | --------- | ------------- | --- | ----- | --- | --- | --- | --- |
[17] Jacques Demongeot, Mathilde Noual, and Sylvain Sené. On the number of attractors of posi-
tive and negative boolean automata circuits. In 2010 IEEE 24th International Conference on
Advanced Information Networking and Applications Workshops, pages 782–789. IEEE, 2010.
[18] Solomon W Golomb. Shift register sequences: secure and limited-access code generators, effi-
ciency code generators, prescribed property generators, mathematical models. World Scientific,
2017.
[19] Paul Erdos and Pál Turán. On some problems of a statistical group-theory. i. Z. Wahrschein-
| lichkeitstheorie |     | verw. | Geb, | 4:175–186, | 1965. |     |     |     |
| ---------------- | --- | ----- | ---- | ---------- | ----- | --- | --- | --- |
[20] Pál Erdős and P Turán. On some problems of a statistical group-theory. ii. Acta Math. Acad.
| Sci. Hungar., |     | 18:151–163, |     | 1967. |     |     |     |     |
| ------------- | --- | ----------- | --- | ----- | --- | --- | --- | --- |
[21] Paul Erdős and Paul Turán. On some problems of a statistical group-theory. iii. Acta Math.
| Acad. Sci. | Hungar, |     | 18:309–320, |     | 1967. |     |     |     |
| ---------- | ------- | --- | ----------- | --- | ----- | --- | --- | --- |
[22] Paul Erdős and Paul Turán. On some problems of a statistical group-theory. iv. Acta Mathe-
| matica | Hungarica, |     | 19(3-4):413–435, |     | 1968. |     |     |     |
| ------ | ---------- | --- | ---------------- | --- | ----- | --- | --- | --- |
[23] Edmund Landau. Über die maximalordnung der permutationen gegebenen grades. Archiv der
| Math. und | Phys, | 3:92–103, |     | 1903. |     |     |     |     |
| --------- | ----- | --------- | --- | ----- | --- | --- | --- | --- |
11

[24] William MY Goh and Eric Schmutz. The expected order of a random permutation. Bulletin
of the London Mathematical Society, 23(1):34–42, 1991.
[25] Kevin Ford. Cycle type of random permutations: a toolkit. arXiv preprint arXiv:2104.12019,
2021.
[26] Tudor Achim, Alex Best, Alberto Bietti, Kevin Der, Mathïs Fédérico, Sergei Gukov,
Daniel Halpern-Leistner, Kirsten Henningsgard, Yury Kudryashov, Alexander Meiburg, Mar-
tin Michelsen, Riley Patterson, Eric Rodriguez, Laura Scharff, Vikram Shanker, Vladmir
Sicca, Hari Sowrirajan, Aidan Swope, Matyas Tamas, Vlad Tenev, Jonathan Thomm, Harold
Williams, and Lawrence Wu. Aristotle: Imo-level automated theorem proving, 2025.
[27] Nicolaas Govert De Bruijn. Asymptotic methods in analysis, volume 4. Courier Corporation,
1981.
12
---- END DOCUMENT ----
