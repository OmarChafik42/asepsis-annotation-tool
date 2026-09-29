Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Self-Normalizing Denominators
in Rational Causal Estimation
Shu Tamano1,2,∗
1
Department of Multidisciplinary Sciences, Graduate School of Arts and Sciences, The
University of Tokyo, 3-8-1 Komaba, Meguro-ku, Tokyo 153-8902, Japan
2 Department of Epidemiology, National Institute of Infectious Diseases, Japan Institute for
Health Security, 1-23-1 Toyama, Shinjuku-ku, Tokyo 162-0052, Japan
∗Email: tamano-shu212@g.ecc.u-tokyo.ac.jp
Abstract
Rational causal estimators in linear structural equation models take the form
of one covariance polynomial divided by another, and a small denominator is com-
monly interpreted as weak identification. We show that, under Gaussian sampling,
some denominators cannot enter this regime at first order. Their sampling varia-
tion is exactly proportional to their magnitude, so the standardized denominator
is constant in every sample. Products of powers of nested covariance minors have
this property in every dimension and admit an exact Wishart pivot. The converse
is complete in dimension two. In dimension three, one mixed family remains open,
while a factor-and-rank criterion classifies all denominators with linear or quadratic
determinant-free factors and covers instrumental-variable, front-door and proximal
formulas. For linear front-door adjustment, Wald inference remains asymptotically
valid even as the mediator residual variance vanishes at an arbitrary rate, pro-
vided the treatment–mediator coefficient is nonzero. In simulations, proximal Wald
coverage fell as a naive treatment–proxy diagnostic strengthened, while front-door
coverage stayed nominal, and right-heart-catheterization data distinguished naive
from denominator-relevant diagnostics.
Keywords: Bartlett decomposition; Fieller’s theorem; Fisher–Rao geometry; Proximal
causal inference; Symmetric cone; Weak instrument.
1 Introduction
1.1 Motivation and scope
Graphical identification in linear structural equation models often yields a causal coeffi-
cient of the form N(Σ)/D(Σ). Here Σ ∈ Sd is the observational covariance matrix of d
++
observed coordinates, and N and D are polynomial functions on the space Sym of sym-
d
metric matrices of order d. Instrumental variables, conditional instruments, front-door
adjustment, half-trek identification and proximal formulas all produce such expressions
(Pearl, 1995; Brito and Pearl, 2002; Foygel et al., 2012; Kuroki and Pearl, 2014; van der
Zander et al., 2015; Miao et al., 2018; Tchetgen Tchetgen et al., 2024; Henckel et al.,
1
6202
guA
02
]TS.htam[
1v32202.8062:viXra

2024). At regular distributions, substituting the sample covariance matrix into such a
formula is routine. However, when D is small, weak-instrument theory suggests a ratio-
of-normals limit, distorted Wald inference and confidence sets that must sometimes be
unbounded (Gleser and Hwang, 1987; Dufour, 1997; Staiger and Stock, 1997; Stock and
Wright, 2000; Andrews and Cheng, 2012; Andrews et al., 2019). The standard safeguard
compares the estimated denominator with its estimated standard error, as in first-stage
relevance screening.
Two of these strategies display the contrast that motivates this paper. Throughout this
preview, the observed vector is centred Gaussian with covariance matrix Σ ∈ Sd . The
++
ˆ
scalar σ = cov(U,V) denotes the covariance of two observed variables U and V, and Σ
UV
denotes the sample covariance matrix from n independent observations. Section 2 gives
the remaining conventions. For the front-door strategy, the observed vector is (X,M,Y)⊤
and
D (Σ) = σ (σ σ −σ2 ).
fd XX XX MM XM
At every such Σ, the asymptotic variance of n1/2{D (Σ ˆ )−D (Σ)} is 10D (Σ)2. Con-
fd fd fd
sequently, the statistic that divides nD (Σ ˆ )2 by the plug-in value of this variance equals
fd
n/10 for every positive-definite sample covariance. Screening this denominator reveals
nothing about the underlying distribution, although the precision of the plug-in estima-
tor may deteriorate without bound. By contrast, consider a linear proximal strategy
with observed coordinates (A,Z,W)⊤, comprising a treatment, a treatment proxy and an
outcome proxy. Its denominator is
D (Σ) = σ σ −σ σ ,
prox AA ZW AZ AW
which equals σ times the partial covariance of Z and W given A. This denominator
AA
vanishes at interior covariance matrices at which its asymptotic variance does not. There
are therefore sequences of covariance matrices along which the plug-in ratio can have the
ratio-of-normals limit of weak-instrument theory. The relevant screening direction is the
partial covariance, not the marginal treatment–proxy association.
These examples motivate the question of which denominators make the first-order ratio
regime impossible along every sequence of underlying covariance matrices. Under cen-
tred Gaussian sampling, the first-order variance of a covariance polynomial is a classical
quadraticforminitssymmetricgradient. Weshowthat, foraspecialclassofpolynomials,
this quadratic form is exactly proportional to the square of the polynomial. Denominator
noise then contracts at the same rate as the denominator itself, and the standardized
denominator is a samplewise constant rather than a relevance statistic. We call such
denominators exactly self-normalizing.
Two neighbouring phenomena are excluded from this notion. A polynomial whose first-
order variance merely vanishes on its zero set can still generate a nondegenerate second-
order local limit when that variance is not proportional to the square of the polynomial.
Section 5 gives an example. Numerator singularities are also distinct. The mediation null
remains nonregular even though the front-door denominator is exactly self-normalizing
(Drton and Xiao, 2016). Therefore, the classification below concerns denominators, not
universal regularity of the associated estimators.
2

1.2 Contributions
The first contribution is an all-dimensional sufficient class. Products of powers of covari-
ance determinants along a nested flag of subspaces are exactly self-normalizing. Their
relative gradients have a fixed spectrum, and their sample-to-population ratios factor
into independent chi-squared variables. In recursive coordinates, these polynomials are
monomials in successive conditional variances, which links the algebra directly to variance
information.
The second contribution is a low-dimensional converse. The converse is complete in
dimension two. In dimension three, determinant stripping reduces every solution to a
rank-one branch, a pure plane-minor branch or a mixed branch with constant relative
spectrum and a polynomial kernel line. The first two branches are flag powers, while
rigidity of the mixed kernel line remains open. For the practically important class whose
determinant-free irreducible factors have degree at most two, only one rank-one variance
factor and one nested plane-minor factor can occur. This gives a coefficient-level factor-
and-rank diagnostic and classifies every reducible self-normalizing cubic.
The statistical results connect this algebra to weak-denominator inference. A local result
recovers the classical ratio-of-normals limit under a drift condition that no exactly self-
normalizing denominator can satisfy. The standardized denominator is the noncentrality
diagnostic of this limit and also determines whether Fieller inversion is bounded. For
marginal and partial covariance denominators, it is an explicit increasing function of
the corresponding first-stage statistic. For linear front-door adjustment, the Gaussian
delta Wald statistic remains asymptotically standard normal when the mediator residual
variance tends to zero at any rate, provided the treatment–mediator coefficient is nonzero.
Together, the results give a diagnostic pathway for graph-derived rational formulas. One
factors the symbolic denominator, checks whether its factors form a nested variance flag,
and then chooses between conventional studentization and weak-identification-robust in-
version. Simulations and a diagnostic audit of right-heart-catheterization data from the
SUPPORT study illustrate the two branches of this pathway.
1.3 Related work
Graphicalcriteriaforinstrumentalsets, front-dooradjustmentandproximalidentification
determine whether a causal effect can be expressed from the observational law. The
half-trek criterion and computer-algebra methods provide rational certificates for linear
structuralequationmodels(Pearl,1995;BritoandPearl,2002;García-Puenteetal.,2010;
Foygel et al., 2012; Kuroki and Pearl, 2014; van der Zander et al., 2015; Miao et al., 2018;
Henckel et al., 2024; Tchetgen Tchetgen et al., 2024). Generic and rational identifiability
are distinct algebraic notions, and a parameter may be generically unique without being
represented by the particular rational formula under study (Drton and Weihs, 2016).
Recent semiparametric work derives regular influence functions for half-trek estimators
at fixed interior distributions (Mareis et al., 2026). Our analysis starts after a rational
certificate has been selected. It classifies the denominator as a polynomial on the ambient
covariance space and determines which first-order boundary regime that certificate can
generate.
Fieller and Anderson–Rubin inversion provide the classical ratio-based confidence con-
structions (Anderson and Rubin, 1949; Fieller, 1954). The impossibility of uniformly
3

bounded confidence sets and the local theory of weak instruments and weak moments ex-
plain why a noisy denominator near zero produces non-Gaussian ratio limits (Gleser and
Hwang, 1987; Dufour, 1997; Staiger and Stock, 1997; Stock and Wright, 2000; Andrews
and Cheng, 2012). Modern work develops first-stage-dependent corrections and robust
procedures, including settings with many weak moments and weakly identified nuisance
functions (Andrews et al., 2019; Lee et al., 2022; Wang et al., 2025; Bennett et al., 2026).
The local result in Section 5 is a covariance-polynomial specialization of this literature.
The new point is structural and precedes the limit calculation. The self-normalization
identity decides when the first-order ratio regime is algebraically impossible.
Condition-number analyses quantify sensitivity of an identified functional or structural
parameter to perturbations of the observational law (Schulman and Srivastava, 2016; Gor-
don et al., 2021; Sankararaman et al., 2022). Exact self-normalization instead compares
the gradient noise of one denominator with the denominator itself through a global poly-
nomialidentity. Thetwonotionsneednotagree. Inthefront-doorboundarysequence,the
standard error diverges and the formula becomes badly conditioned, yet the denominator
cannot enter the first-order Fieller regime. Conversely, a well-scaled slope denominator
may have an interior zero with nondegenerate first-order noise.
Products of nested covariance minors are generalized power functions of a symmetric
cone (Faraut and Korányi, 1994), and their exact sampling factorization follows from the
BartlettdecompositionofaWishartmatrix(Muirhead,1982). Theaffine-invariantmetric
on the positive-definite cone, which agrees up to scale with the Fisher–Rao metric of the
centred Gaussian family, gives the geometric form of the logarithmic gradient flow used
in the converse proofs (Bhatia, 2007). The separation between Gaussian and elliptical
covariance operators is familiar in covariance-structure analysis (Shapiro and Browne,
1987; Iwashita and Siotani, 1994). Here it identifies which part of the classification is
distributional and which part is algebraic.
The dimension-two converse uses the Gordan–Noether theorem for forms with vanishing
Hessian (Gordan and Noether, 1876; Lossen, 2004). That route fails for the six variables
of a symmetric matrix of order three because noncone forms with vanishing Hessian exist
in this dimension (Perazzo, 1900; Ciliberto et al., 2008; Gondim and Russo, 2015). Sup-
plementary Section I.1 explains why Hessian degeneracy does not force a cone on the six-
dimensional space Sym , while Supplementary Section I.2 identifies the information lost
3
when the relevant tensor relation is passed through polynomial multiplication. These two
obstructions explain why neither route presently closes the mixed branch (Lichtenstein,
1982). This distinction explains the complete dimension-two result and the mixed-kernel
problem left in dimension three.
2 Preliminaries
2.1 Basic notation
We use R and C for the real and complex fields. Vectors are columns, A⊤ denotes matrix
transpose, I is the identity matrix of order m, and e is the jth standard basis vector.
m j
The subscript on I is omitted when the order is clear. The symbols tr(A), det(A),
m
rank(A) and spec(A) denote trace, determinant, rank and the multiset of eigenvalues of
A. Expectations, variances, covariances and probabilities under a probability measure Q
4

E
are denoted by , var , cov and pr . The subscript is suppressed once the probability
|     |     | Q   | Q   | Q   |     | Q   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
measure is fixed. Convergence in probability and in distribution are denoted by −→ and
p
⇝, and limits are as n → ∞ unless stated otherwise. The indicator of a statement A is
| 1(A), | and sgn(x) | is the | sign | of  | x ∈ R. |     |     |     |     |     |     |     |     |
| ----- | ---------- | ------ | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
For a positive integer d, let [d] = {1,...,d}, p = d(d+1)/2 and I = {(i,j) : 1 ≤ i ≤ j ≤
|     |     |     |     |      |     |     | d   |     |     | d   |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | Rd×d |     | A⊤} |     |     |     |     |     |     |     |
d}. We write Sym = {A ∈ : A = and denote its positive-definite and positive-
d
semidefinite cones by Sd and Sd. The notation A ≻ 0 and A ⪰ 0 means A ∈ Sd and
|     |     |     | ++  |     | +   |     |     |     |     |     |     | ++  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A ∈ Sd, respectively. For Σ ∈ Sym , its entries are σ = σ . For I,J ⊆ [d], A is the
|     |     |     |     |     |     |     |     | ij  | ji  |     |     | I,J |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | +   |     |     |     | d   |     |     |     |     |     |     |     |     |
submatrix with rows in I and columns in J, A = A , and A = A .
|          |                      |     |     |     |          |       | I    | I,I   |         | 1:r | {1,...,r},{1,...,r} |     |     |
| -------- | -------------------- | --- | --- | --- | -------- | ----- | ---- | ----- | ------- | --- | ------------------- | --- | --- |
| We order | I lexicographically, |     |     |     | first by | i and | then | by j, | and set |     |                     |     |     |
d
)⊤ Rp
|     |     | vech(A) |     | = (a | ,a    | ,...,a | ,a    | ,a ,...,a |     | ∈   | d.  |     |     |
| --- | --- | ------- | --- | ---- | ----- | ------ | ----- | --------- | --- | --- | --- | --- | --- |
|     |     |         |     |      | 11 12 |        | 1d 22 | 23        | dd  |     |     |     |     |
Vectors and matrices indexed by I follow this ordering. We identify R[Sym ] = R[σ :
|     |     |     |     |     | d   |     |     |     |     |     | d   |     | ij  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
R.
(i,j) ∈ I ] with the ring of polynomial maps from Sym to The notation P ≡ 0 means
|     | d   |     |     |     |     |     |     | d   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that P is the zero polynomial in this ring. A polynomial P is homogeneous of degree K
|     |     | tKP(Σ) |     |     |     | R.  |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
when P(tΣ) = for every t ∈ Its total degree is deg(P), and two polynomials
are coprime when their only common divisors are nonzero constants.
|     | R[Sym |     |     |     |     |     |     | Rp  |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For P ∈ ], the coordinate gradient ∇P(Σ) ∈ d consists of the partial derivatives
d
in the preceding vech order. The Fréchet differential of P at Σ in the direction H is
(cid:12)
|     |     |     |     |     | d   |                 |     | (cid:12) |       |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ----- | --- | --- | --- | --- |
|     |     |     | dP  | (H) | =   | P(Σ+tH)(cid:12) |     | , H      | ∈ Sym | .   |     |     |     |
Σ
|     |     |     |     |     | dt  |     |     | (cid:12) |     | d   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
(cid:12)
t=0
The symmetric gradient G (Σ) ∈ Sym is the unique matrix satisfying dP (H) =
|     |     |     |     | P   |     |     |     |     |     |     |     | Σ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
d
tr{G (Σ)H} for every H ∈ Sym . Thus, (G ) = ∂P/∂σ and (G ) = 2−1∂P/∂σ
| P   |     |     |     |     | d   |     | P   | ii  | ii  |     | P ij |     | ij  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
for i < j, with all quantities evaluated at Σ. For P(Σ) ̸= 0, the relative gradient is
| R (Σ) | = G (Σ)Σ/P(Σ). |        |     |     |     |     |     |     |     |     |     |     |     |
| ----- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P     | P              |        |     |     |     |     |     |     |     |     |     |     |     |
| 2.2   | Problem        | set-up |     |     |     |     |     |     |     |     |     |     |     |
We formulate the statistical problem in the ambient covariance space. Fix d ≥ 1 and
Σ ∈ Sd . The notation N (µ,Ω) denotes the Gaussian law on Rm with mean µ ∈ Rm
|     | ++  |     |     | m   |     |     |     |     |      |      |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- |
|     |     |     |     | Sm. |     |     |     |     | P(n) | P⊗n. |     |     |     |
and covariance matrix Ω ∈ Write P = N (0,Σ) and = Let X ,...,X be
|     |     |     |     | +   |     | Σ   | d   |     | Σ   | Σ   | 1   |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P(n).
independent observations with joint law We use the known-mean sample covariance
Σ
matrix
n
|     |     |     |     |     | ˆ n−1X |     | X⊤, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | Σ =    |     | X   | n > | d.  |     |     |     | (1) |
i i
i=1
|     |     |     |     | Sm, |     |     |     |     |     | Pν  | Z⊤  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For an integer ν ≥ 1 and Ω ∈ W (ν,Ω) denotes the law of Z for independent
|     |     |     |     |     | + m |     |     |     |     | ℓ=1 | ℓ ℓ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
Z ∼ N (0,Ω). Its scalar specialization with Ω = 1 is χ2. Consequently, nΣ ∼ W (n,Σ)
| ℓ   | m   |     |     |     |     |     |     |     | ν   |     |     | d   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
| and Σ | ≻ 0 almost | surely. |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The identification equality is required only on a covariance model, whereas the polyno-
mial pair representing it governs off-model sampling behaviour. The following definition
| separates | these | two | objects. |     |     |     |     |     |     |     |     |     |     |
| --------- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition 1 (Identification strategy). Let M ⊆ Sd be a nonempty covariance model
++
and let τ : M → R be a scalar target. An identification strategy for τ is an ordered pair
5

R[Sym
(N,D) of coprime elements of ] such that D is not identically zero on M and
d
|     |     |     |     |     | N(Σ) | =   | τ(Σ)D(Σ) |     | (Σ ∈ M). |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | -------- | --- | -------- | --- | --- | --- |
Thus, τ = N/D at every point of M at which D is nonzero. The covariance plug-in
estimator is τˆ = N(Σ)/D(Σ) ˆ ˆ on the event {D(Σ) ˆ ̸= 0}. The target is scale-invariant
| when | τ(tΣ) | =   | τ(Σ) | whenever | Σ,tΣ | ∈   | M and | t > | 0.  |     |     |     |
| ---- | ----- | --- | ---- | -------- | ---- | --- | ----- | --- | --- | --- | --- | --- |
ˆ
Thisdistinctionisnecessaryfortworeasons. First,Σneednotsatisfythemodelequations,
so the sampling behaviour of τˆ depends on N and D as polynomials on the whole of
Sym . Second, multiplying both N and D by a nonconstant common factor leaves the
d
identified ratio unchanged wherever both representations are defined, yet alters the off-
model sampling behaviour of the denominator. Coprimality removes this ambiguity. Two
coprime pairs representing the same rational function coincide up to a common nonzero
scalar, while distinct rational certificates for the same target remain distinct strategies.
| 2.3 | Exact |     | self-normalization |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We now introduce the central property of the paper. Define the polynomial matrix map
| Γ : Sym |     | → Sym | by  |     |     |     |     |     |     |     |     |     |
| ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|         | d   |       | p   |     |     |     |     |     |     |     |     |     |
d
|     |       |     |     | Γ         | (Σ) | = σ | σ +σ | σ ,   | (i,j),(k,l) |     | ∈ I . | (2) |
| --- | ----- | --- | --- | --------- | --- | --- | ---- | ----- | ----------- | --- | ----- | --- |
|     |       |     |     | (ij),(kl) |     | ik  | jl   | il jk |             |     | d     |     |
|     | P(n), |     |     |           |     |     |      |       |             |     | ˆ     |     |
Under the matrix Γ(Σ) is the covariance matrix of n1/2vech(Σ − Σ). For D ∈
Σ
R[Sym
|     | ],  | define | its Gaussian |     | first-order |     | variance | functional |     | by  |     |     |
| --- | --- | ------ | ------------ | --- | ----------- | --- | -------- | ---------- | --- | --- | --- | --- |
d
|     |     |     | s2  | (Σ) | = ∇D(Σ)⊤Γ(Σ)∇D(Σ) |     |     |     | = 2tr{(G | (Σ)Σ)2}. |     | (3) |
| --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | -------- | -------- | --- | --- |
|     |     |     |     | D   |                   |     |     |     |          | D        |     |     |
The second equality is the Gaussian quadratic-form variance identity, verified in Sup-
plementary Lemma B.1. Both sides are polynomial in Σ, so the equality extends from
Sd to all of Sym . For Σ ∈ Sd the matrix Γ(Σ) is positive semidefinite, and we write
| ++  |     |     | d   |     | +   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s (Σ) = {s2 (Σ)}1/2 there. The standardized denominator is Fb = nD(Σ ˆ )2/s2 (Σ ˆ ), de-
| D     |        |       |     |        |       |     |     |     |     |     | D   |     |
| ----- | ------ | ----- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
|       |        | D     |     |        |       |     |     |     |     |     | D   |     |
| fined | on the | event | {s2 | (Σ ˆ ) | > 0}. |     |     |     |     |     |     |     |
D
Definition 2 (Exact self-normalization). A nonconstant homogeneous polynomial D ∈
R[Sym
] is exactly self-normalizing when there is a constant c ∈ (0,∞) such that
d
|     |     |     |     | 2tr{(G |     | (Σ)Σ)2} | =   | cD(Σ)2 | (Σ  | ∈ Sym | ).  | (4) |
| --- | --- | --- | --- | ------ | --- | ------- | --- | ------ | --- | ----- | --- | --- |
|     |     |     |     |        | D   |         |     |        |     |       | d   |     |
For a strategy (N,D), exact self-normalization refers only to the denominator D.
The constant c is unique because D is not the zero polynomial. Below, self-normalizing
always means exactly self-normalizing. Equation (4) states that the Gaussian first-order
noise of D contracts in exact proportion to |D| throughout the ambient covariance space.
In particular, evaluating (4) at Σ ˆ gives Fb = n/c whenever s2 (Σ ˆ ) > 0. Thus, the stan-
D
D
dardized denominator of a self-normalizing polynomial D is constant over samples rather
than a relevance statistic. Exact self-normalization is invariant under congruence trans-
formations. Every rational strategy for a scale-invariant coefficient in a linear structural
equation model has a homogeneous representative, and a nonzero self-normalizing polyno-
Sd
mial has no zero in . Supplementary Lemmas B.1–B.3 prove these facts. If D depends
++
on Σ only through its compression to an r-dimensional subspace, its self-normalization
status and constant are unchanged in every ambient dimension d ≥ r by Supplementary
Lemma B.4. The dimension-three classification below therefore applies to any denomina-
tor supported on at most three directions, whatever the number of observed coordinates.
6

Remark 1 (Scope of exactness). Equation (4) is an identity in the ambient polynomial
ring for the coprime denominator fixed by Definition 1. It is not merely an equality on
a structural model. The word “exact” also refers to the Gaussian covariance operator in
(3). A sandwich studentizer under a general law targets a different quadratic form and
need not be constant sample by sample. Under elliptical sampling, the same algebraic
class persists after a kurtosis adjustment, although the product-of-chi-squares pivot is
generally lost. With an unknown Gaussian mean, the corresponding centred covariance
formulas replace n by n − 1. Supplementary Proposition B.1 and Remark B.1 give the
precise statements.
| 3   | Flag |        | powers |            | and | an     | exact | pivot |     |     |     |
| --- | ---- | ------ | ------ | ---------- | --- | ------ | ----- | ----- | --- | --- | --- |
| 3.1 |      | Nested |        | covariance |     | minors |       |       |     |     |     |
We construct self-normalizing denominators in every dimension. The building blocks are
covariance volumes of subspaces. For an r-dimensional subspace V ⊆ Rd, let M be
V
any full-row-rank matrix whose row space is V, and write ∆ (Σ) = det(M ΣM⊤). If a
|     |     |     |     |     |     |     |     |     |     | V V V |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
random vector X has covariance matrix Σ, then ∆ (Σ) is the generalized variance of the
V
reduced vector M X. A different choice of M multiplies ∆ by a positive constant and
|         |     |              |     | V      |     |     |     | V   |     | V   |     |
| ------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| affects |     | no statement |     | below. |     |     |     |     |     |     |     |
Rd.
A flag is a strictly increasing chain V ⊂ ··· ⊂ V of nonzero subspaces of Let
|     |     |     |     |     |     |     | 1   |     | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a = dim(V ), so that 1 ≤ a < ··· < a ≤ d, and let e ,...,e be positive integers. The
| j          |     | j    |       |      |     | 1              | k      |     | 1   | k         |     |
| ---------- | --- | ---- | ----- | ---- | --- | -------------- | ------ | --- | --- | --------- | --- |
| associated |     | flag | power | and  | its | multiplicities |        | are |     |           |     |
|            |     |      |       |      |     | k              |        |     | k   |           |     |
|            |     |      |       | D(Σ) |     | = Y ∆          | (Σ)ej, | m = | X e | 1(a ≥ i). | (5) |
|            |     |      |       |      |     |                | Vj     | i   | j   | j         |     |
|            |     |      |       |      |     | j=1            |        |     | j=1 |           |     |
Thus, m is the total exponent carried by factors whose subspaces have dimension at least
i
i, and m ≥ ··· ≥ m ≥ 1. The following theorem shows that every flag power is exactly
|     |     | 1   |     | a   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
| self-normalizing |     |     | and | gives | its | exact | sampling | law. |     |     |     |
| ---------------- | --- | --- | --- | ----- | --- | ----- | -------- | ---- | --- | --- | --- |
Theorem 1 (Flag powers). Let D and m ,...,m be given by (5). The following state-
|     |     |     |     |     |     |     |     | 1 a | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ments hold.
(i) ForeveryΣ ≻ 0, thespectrumoftherelativegradientR (Σ)is(m ,...,m ,0,...,0),
|     |       |     |                |     |      |     |              |     |     | D 1 a k |     |
| --- | ----- | --- | -------------- | --- | ---- | --- | ------------ | --- | --- | ------- | --- |
|     | where |     | the eigenvalue |     | zero | has | multiplicity | d−a | .   |         |     |
k
2Pa
| (ii) | Equation |     | (4) | holds | with | c = | k m2. |     |     |     |     |
| ---- | -------- | --- | --- | ----- | ---- | --- | ----- | --- | --- | --- | --- |
|      |          |     |     |       |      |     | i=1   | i   |     |     |     |
ˆ
| (iii) | If  | n ≥ | a , then | D(Σ)/D(Σ) |     | is  | distributed | as  |     |     |     |
| ----- | --- | --- | -------- | --------- | --- | --- | ----------- | --- | --- | --- | --- |
k
|     |     |     |     |     |     |     |     |    | mi |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a k χ2
Y n−i+1
|     |     |     |     |     |     |     |     |    |  , |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
i=1
|     | where |     | the chi-squared |     |     | variables | are independent. |     |     |     |     |
| --- | ----- | --- | --------------- | --- | --- | --------- | ---------------- | --- | --- | --- | --- |
(iv) In particular, the identity Fb = n/c holds almost surely, and no sequence Σ ∈ Sd
|     |     |         |     |              |     | D   |          |      |       | n    | ++  |
| --- | --- | ------- | --- | ------------ | --- | --- | -------- | ---- | ----- | ---- | --- |
|     | can | satisfy |     | both n1/2D(Σ |     | ) = | O(1) and | s (Σ | ) → s | > 0. |     |
|     |     |         |     |              |     | n   |          | D n  |       |      |     |
Remark 2 (Algebraic and sampling content). Parts (i) and (ii) are polynomial identities
anddonotdependonasamplinglaw. Thesamplewiseidentityinpart(iv)thereforeholds
7

at every sample covariance matrix at which D is nonzero, whatever the data-generating
law. Only the factorization in part (iii) uses Gaussian sampling. With an unknown Gaus-
sian mean, parts (iii) and (iv) hold for the centred sample covariance with n replaced by
n−1. Underellipticalsampling, flagpowersremainproportionallyself-normalizingaftera
kurtosis adjustment, but the product-of-chi-squares law is generally lost. Supplementary
| Proposition | B.1 | and | Remark | B.1 | give | these variants. |     |     |     |
| ----------- | --- | --- | ------ | --- | ---- | --------------- | --- | --- | --- |
Thenestinghypothesiscannotbeweakened. IfneitheroftwosubspacesV andW contains
the other, then no product ∆p ∆q with positive integer exponents p and q is exactly
V W
self-normalizing. Supplementary Section C proves both this two-subspace criterion and
| Theorem       | 1.  |     |          |     |                |     |     |     |     |
| ------------- | --- | --- | -------- | --- | -------------- | --- | --- | --- | --- |
| 3.2 Recursive |     |     | variance |     | interpretation |     |     |     |     |
Flag powers aggregate conditional-variance information. Let X = (X(1),...,X(d))⊤ have
the sampling law P , and write v (Σ) = var {X(i) | X(1),...,X(i−1)} for the successive
|             |            |     | Σ    |       | i   | Σ           |     |        |     |
| ----------- | ---------- | --- | ---- | ----- | --- | ----------- | --- | ------ | --- |
| conditional | variances, |     | with | v (Σ) | = σ | . For every | r   | ∈ [d], |     |
|             |            |     |      | 1     |     | 11          |     |        |     |
r
Y
|     |     |     |     |     | det(Σ | ) = | v (Σ). |     | (7) |
| --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- |
|     |     |     |     |     |       | 1:r | i      |     |     |
i=1
Consider the coordinate flag, whose jth subspace is spanned by the first a coordinate
j
By(7),theflagpower(5)isthenthemonomialQa
| directions. |     |     |     |     |     |     |     | k v (Σ)mi,sothemultiplicity |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- |
i=1 i
m is the exponent attached to the ith conditional variance. A general flag reduces to
i
this case, up to a positive constant, after one fixed nonsingular linear transformation of
the observation vector. For the front-door strategy of Section 1, the first two conditional
variances are the treatment variance and the mediator residual variance. Its denominator
is the monomial v (Σ)2v (Σ), and part (ii) of Theorem 1 returns the constant c = 2(22+
|          |        |     | 1     | 2     |     |     |     |     |     |
| -------- | ------ | --- | ----- | ----- | --- | --- | --- | --- | --- |
| 12) = 10 | behind | the | value | n/10. |     |     |     |     |     |
P(n),
The same representation explains the exact sampling law. Under the sample con-
Σ
ˆ
ditional variances computed from Σ along the coordinate flag are mutually independent.
The ith is distributed as v (Σ) times a χ2 /n variable. This is the Bartlett decompo-
|     |     |     |     | i   |     | n−i+1 |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
ˆ
sition of the Wishart matrix nΣ (Muirhead, 1982, Ch. 3), and evaluating the monomial
at these independent factors gives the law in (6). To first order, the relative variance of
every sample conditional variance is 2/n, whatever the value of Σ. By independence, the
2Pa
relative first-order variance of the sample flag power is k m2/n, which equals c/n.
i=1 i
This constancy in Σ is the sampling mechanism behind exact self-normalization. The
ˆ
sample flag power depends on Σ only through these conditional variances. The regression
coefficients of each coordinate on its predecessors, which complete the recursive decom-
position of Σ, ˆ do not enter. This contrast between conditional variances and regression
coefficients is the sample form of the distinction between variance information and slope
| information   | that | organizes |         | the | converse | results   | of Section | 4.  |     |
| ------------- | ---- | --------- | ------- | --- | -------- | --------- | ---------- | --- | --- |
| 4 Converse    |      |           | results |     | and      | diagnosis |            |     |     |
| 4.1 Dimension |      |           |         | two |          |           |            |     |     |
We first obtain a complete converse for covariance matrices of order two. Through face
| restriction, | this | result | also | drives | the | three-variable |     | analysis. |     |
| ------------ | ---- | ------ | ---- | ------ | --- | -------------- | --- | --------- | --- |
8

R[Sym
Theorem 2 (Complete converse in dimension two). Let D ∈ ] be homogeneous,
2
| nonconstant | and exactly | self-normalizing. |     | Then |     |     |     |
| ----------- | ----------- | ----------------- | --- | ---- | --- | --- | --- |
γ(v⊤Σv)a(detΣ)b,
|     |     |     | D(Σ) = |     |     |     | (8) |
| --- | --- | --- | ------ | --- | --- | --- | --- |
R2,
for a nonzero constant γ, a nonzero vector v ∈ and nonnegative integers a,b with
(a,b) ̸= (0,0). The self-normalization constant is c = 2{(a+b)2 +b2}.
Thus, a two-variable denominator can self-normalize only by combining one variance
| direction | with the full | covariance | volume. |     |     |     |     |
| --------- | ------------- | ---------- | ------- | --- | --- | --- | --- |
Remark 3 (What the converse excludes). The permitted irreducible factors are one
rank-one variance v⊤Σv and the determinant. Every linear form tr(BΣ) whose coefficient
matrix B has rank two, such as the off-diagonal covariance σ , is excluded even though
12
it has the same degree as the permitted variance forms. Thus, the theorem distinguishes
variance information from slope information within the same polynomial degree.
We summarize the proof mechanism, which explains the rigidity. Euler’s identity and
(4) fix the first two power sums of the eigenvalues of R (Σ). The elementary symmetric
D
identity converts them into a determinant identity with an explicit constant coefficient.
When that coefficient is nonzero, the determinant divides D, the factor can be stripped,
and induction on the degree applies. When it vanishes, the gradient map takes values
in the rank-one quadric, and the Hessian determinant of D vanishes identically. The
Gordan–Noether theorem reduces D to a power of one linear form, which symmetry
and reality identify with a variance direction (Gordan and Noether, 1876; Lossen, 2004).
| Supplementary | Section   | D.2 gives | the full | proof. |     |     |     |
| ------------- | --------- | --------- | -------- | ------ | --- | --- | --- |
| 4.2           | Dimension | three     |          |        |     |     |     |
We now reduce the three-variable converse to a single mixed branch. Put δ = detΣ and
call D ∈ R[Sym ] determinant-free when δ ∤ D. For homogeneous D of degree K, define
3
the rank-one restriction p : R3 → R by p (u) = D(uu⊤). For a plane V ⊆ R3 with basis
|     |     | D   |     | D   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
matrix P ∈ R3×2, define the face restriction D : Sym → R by D (S) = D(PSP⊤).
|     |     |     |     | V   | 2   | V   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
The plane V is called D-good when D ̸≡ 0, and simply good when the polynomial is
V
clear from context. A polynomial vector is primitive when its entries have no nonconstant
| common | divisor. |     |     |     |     |     |     |
| ------ | -------- | --- | --- | --- | --- | --- | --- |
A nonzero plane restriction of a self-normalizing polynomial is again self-normalizing
with the same constant. Supplementary Lemma D.3 provides this restriction principle,
and Theorem 2 then determines the form of every such restriction.
Definition 3 (Face type). Let D be a determinant-free self-normalizing polynomial on
Sym , of degree K and with self-normalization constant c. For a,b ∈ Z , we say that D
| 3   |     |     |     |     |     | ≥0  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
has face type (a,b) if, for every D-good plane V, there exist γ ∈ R\{0} and w ∈ R2\{0}
|            |                 |          |     |       | V   | V   |     |
| ---------- | --------------- | -------- | --- | ----- | --- | --- | --- |
| such that, | as a polynomial | identity | on  | Sym , |     |     |     |
2
|     | D (S) = | γ (w⊤Sw | )a(detS)b, | a+2b = K, | (a+b)2 +b2 | = c/2. | (9) |
| --- | ------- | ------- | ---------- | --------- | ---------- | ------ | --- |
|     | V       | V V     | V          |           |            |        |     |
A determinant-free solution has at least one good plane, and its degree and constant
admit at most one pair satisfying (9), so the face type exists and is common to all good
planes. Removing a factor of δ preserves exact self-normalization with a shifted constant,
so the residue in the next theorem is itself self-normalizing. Supplementary Lemmas D.4
| and D.6 | provide both | facts. |     |     |     |     |     |
| ------- | ------------ | ------ | --- | --- | --- | --- | --- |
9

Theorem 3 (Three-variable reduction). Let D ∈ R[Sym ] be homogeneous, nonconstant
3
and exactly self-normalizing, and let E be the determinant-free residue obtained by remov-
ing from D the largest power of δ. Exactly one of the following cases occurs.
(i) If p ̸≡ 0, then E = γ(v⊤Σv)deg(E) for a nonzero constant γ and a nonzero vector
E
v ∈ R3.
(ii) If p ≡ 0 and the face type of E is (0,b), then E = γ∆b for a nonzero constant γ
E W
and a plane W ⊆ R3.
(iii) If p ≡ 0 and the face type of E is (a,b) with a,b ≥ 1, then
E
spec{R (Σ)} = {a+b,b,0} (Σ ≻ 0), (10)
E
detG ≡ 0, and a primitive polynomial vector ν satisfies G ν ≡ 0, so that ν(Σ)
E E
spans the kernel of G (Σ) at every point where G (Σ) has rank two and ν(Σ) ̸= 0.
E E
The polynomials in cases (i) and (ii) are flag powers built on a single subspace. A mixed
type has degree a+2b ≥ 3, so every solution of degree at most two falls under the first
two cases and is a flag power. Therefore, the unresolved solutions lie in case (iii) and
carry one possibly moving null direction together with the fixed spectrum in (10).
Remark 4 (The mixed-kernel problem). The unrestricted three-variable converse is
equivalent to the constancy of the kernel line in Theorem 3 (iii). For a nonzero vec-
tor w, write [w] for the line that it spans. If [ν(Σ)] is constant on one nonempty open
set, then a fixed vector u satisfies G (Σ)u ≡ 0, and the two-variable converse yields
0 E 0
E(Σ) = γ(v⊤Σv)adet(MΣM⊤)b, v ∈ u⊥,
0
where u⊥ = {x ∈ R3 : u⊤x = 0} and the rows of M span u⊥. The equivalence between
0 0 0
constancy of the kernel line and the displayed mixed flag form is established in Supple-
mentary Lemma D.11. Supplementary Proposition D.3 gives the cofactor syzygy that
couples a moving kernel line to the determinant boundary. Vanishing of the six-variable
Hessian alone is insufficient because noncone forms with vanishing Hessian exist in this
dimension (Perazzo, 1900; Ciliberto et al., 2008; Gondim and Russo, 2015).
Supplementary Section D also gives an independent closure of the mixed branch that does
not presuppose a constant kernel line. If the restrictions of the determinant-free mixed
residue to rank-two faces agree with those of one fixed flag power built from a nested
line and plane, the residue is that flag power whenever its mixed type has degree at most
eight. For higher-degree types, the same conclusion holds under this boundary agreement
condition outside an explicit arithmetic resonance set. Therefore, the unresolved diffi-
culty is the geometric gluing of the face directions rather than an uncontrolled interior
perturbation.
4.3 Higher-dimensional scope
The constancy of the relative spectrum that drives the three-variable reduction is special
to dimension three. Euler’s identity fixes the trace of R (Σ) at the degree of D, and
D
(4) fixes the trace of its square, so in dimension three the eigenvalues are confined to
a circle. The polynomial character of D forces at least one further linear relation with
integer coefficients among the eigenvalues. A line meets a circle in at most two points,
10

so only finitely many spectra are possible, and continuity on the connected cone makes
the spectrum constant. This finiteness underlies the fixed spectrum displayed in (10). In
dimension d ≥ 4 the same two traces leave a sphere of dimension d−2, a linear relation
cuts out a set of dimension d−3, and no finiteness follows.
A conditional converse nevertheless holds in every dimension. If the relative gradients
R (Σ) preserve one fixed complete flag for every Σ ≻ 0 and induce constant weights on
D
the successive one-dimensional quotients, then D is the corresponding flag power. This
is an intrinsic condition on the gradient rather than an assumed factorization, and the
precisestatementisSupplementaryPropositionD.5. Exactself-normalizationaloneisnot
claimed to create such an invariant flag when d ≥ 4. The obstruction in higher dimensions
is thus the emergence of one common invariant recursive ordering, not the integration step
oncethatorderingispresent, anddimensionthreeisasharplow-dimensionaltargetrather
than an arbitrary truncation.
4.4 A factor-and-rank diagnostic
Although the mixed branch obstructs an unconditional converse, the denominators pro-
ducedbygraphicalidentificationtypicallyhaveasimplefactorstructure. Thetwodenom-
inators of Section 1 factor into linear and quadratic pieces after determinant stripping,
and the same holds for the formulas revisited in Section 6. We now show that this class is
classifiedcompletelyandthatmembershipcanbedecidedbyexactsymboliccomputation.
Definition 4 (Low-degree-factorcondition). A homogeneous polynomial on Sym satisfies
3
the low-degree-factor condition if, after removing the largest power of detΣ, every real
irreducible factor has degree at most two.
Under this condition the mixed branch disappears and the classification closes.
Theorem 4 (Low-degree-factor converse). Let D ∈ R[Sym ] be homogeneous, noncon-
3
stant and exactly self-normalizing, and suppose that D satisfies the low-degree-factor con-
dition. Then there exist a nested line and plane V ⊂ V , a nonzero constant γ, and
1 2
nonnegative integers a,b,e such that
D(Σ) = γ∆ (Σ)a∆ (Σ)b(detΣ)e. (11)
V1 V2
Therefore, linear and quadratic factors cannot assemble into any self-normalizing config-
uration other than a nested flag.
For a square matrix A, adj(A) denotes its classical adjugate, characterized by Aadj(A) =
adj(A)A = det(A)I. Writing the plane minor through the adjugate turns Theorem 4 into
a normal form whose ingredients can be tested one by one.
Corollary 1 (Factor-and-rank diagnostic). Let D ∈ R[Sym ] be homogeneous and non-
3
constant, and suppose that D satisfies the low-degree-factor condition. Then D is exactly
self-normalizing if and only if, up to a nonzero constant,
D(Σ) = (v⊤Σv)a{u⊤adj(Σ)u}b(detΣ)e, u⊤v = 0,
for nonzero vectors u,v ∈ R3 and nonnegative integers a,b,e. In that case the self-
normalization constant is
c = 2{(a+b+e)2 +(b+e)2 +e2}.
11

Consequently, every reducible exactly self-normalizing cubic is one of γ∆3 , γ∆ ∆ with
V1 V1 V2
V ⊂ V , or γdetΣ.
1 2
This corollary reduces the audit of a candidate denominator to a finite procedure. One
factors the polynomial symbolically, tests the ranks of the coefficient matrices of the
linear and adjugate-linear factors, and checks orthogonality and nesting of the resulting
directions. The globalization of the generic face factors and the resulting coefficient-level
characterization are proved in Supplementary Section D.8.
The two formulas of Section 1 illustrate the procedure.
Example 1 (From a graph formula to a rank check). For the coordinate order (X,M,Y),
let e ,e ,e denote the corresponding standard basis vectors. The front-door denomina-
X M Y
tor factors as
D = σ (σ σ −σ2 ) = tr(e e⊤Σ)e⊤adj(Σ)e .
fd XX XX MM XM X X Y Y
Both coefficient matrices have rank one and e⊤e = 0, so Corollary 1 applies with
Y X
(a,b,e) = (1,1,0) and certifies exact self-normalization with c = 10, in agreement with
Section 3. For the coordinate order (A,Z,W), define e ,e ,e analogously. The proxi-
A Z W
mal denominator is
D = σ σ −σ σ = tr{Cadj(Σ)}, C = −{e e⊤ +e e⊤}/2,
prox AA ZW AZ AW Z W W Z
where rank(C) = 2, so the quadratic factor fails the rank-one test. Indeed, D vanishes
prox
atthe identitymatrix, so exactself-normalization alreadyfailsby theinteriornonvanishing
property recorded in Section 2.
Thus, the audit separates the two formulas before any data are collected.
Remark 5 (How the diagnostic should be used). For a denominator with rational or al-
gebraic coefficients, the factorization and the rank checks are exact symbolic operations,
and the diagnostic is complete on the stated class. A near-factorization obtained numer-
ically does not certify self-normalization. An irreducible factor of degree at least three
renders the criterion inconclusive rather than negative. One may then test (4) directly
by comparing coefficients or apply the kernel and boundary criteria of Supplementary
Section D.
5 Weak-denominator inference
5.1 Local ratio experiment
We formulate the first-order regime of a weak denominator whose sampling noise does not
degenerate with it. Throughout this section, (N,D) is a fixed identification strategy in
ˆ ˆ
the sense of Definition 1, and τˆ = N(Σ)/D(Σ) is its plug-in estimator. For a deterministic
sequence Σ ∈ Sd with D(Σ ) ̸= 0, define
n ++ n
N(Σ )
n
τ = , g = ∇N(Σ )−τ ∇D(Σ ),
n n n n n
D(Σ )
n
and put s = s (Σ ) and s = {g⊤Γ(Σ )g }1/2. Whenever s s > 0, define
D,n D n g,n n n n D,n g,n
n1/2D(Σ ) g⊤Γ(Σ )∇D(Σ ) s
µ = n , r = n n n , ω = g,n .
n n n
s s s s
D,n g,n D,n D,n
12

These three quantities are the standardized drift of the denominator, the correlation
between the moment direction and the denominator gradient, and their scale ratio.
|     |     |     |     |     |     |     |     |     |     | R,  | Sd  | R   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Assumption 1 (First-order weak denominator). There are τ ∈ Σ ∈ and δ ∈
|     |     |     |     |     |     |     |     |     |     | ∗   | ∗ + | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
such that
n1/2D(Σ
|     |     |     | τ   | → τ | , Σ | → Σ | ,   |     | ) → | δ . |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | n   | ∗   |     | n   | ∗   |     | n   | 0   |     |     |
Define
|            |          |     |       |      |     |     |     |       |     | {g⊤Γ(Σ | }1/2, |     |
| ---------- | -------- | --- | ----- | ---- | --- | --- | --- | ----- | --- | ------ | ----- | --- |
|            | g = ∇N(Σ |     | )−τ   | ∇D(Σ | ),  | s   | = s | (Σ ), | s   | =      | )g    |     |
|            | ∗        |     | ∗     | ∗    | ∗   | D,∗ | D   | ∗     | g,∗ | ∗      | ∗ ∗   |     |
| and assume | s        | > 0 | and s | >    | 0.  |     |     |       |     |        |       |     |
|            | D,∗      |     |       | g,∗  |     |     |     |       |     |        |       |     |
By continuity of the polynomial gradients and of Γ, Assumption 1 implies s → s ,
|     |       |     |     |     |     |       |       |     |     |     | D,n   | D,∗ |
| --- | ----- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | ----- | --- |
| s → | s and |     |     |     |     |       |       |     |     |     |       |     |
| g,n | g,∗   |     |     |     |     |       |       |     |     |     |       |     |
|     |       |     | δ   |     |     | g⊤Γ(Σ | )∇D(Σ |     | )   |     | s     |     |
|     |       |     | 0   |     |     |       | ∗ ∗   |     | ∗   |     | g,∗   |     |
|     | µ →   | µ = |     | , r | → r | =     |       |     | ,   | ω → | ω = . |     |
|     | n     | ∗   | s   | n   |     | ∗     | s     | s   |     | n   | ∗ s   |     |
|     |       |     | D,∗ |     |     |       | g,∗   | D,∗ |     |     | D,∗   |     |
Assumption 1 describes a denominator that drifts to zero at exactly the rate of its non-
degenerate first-order noise. Continuity gives D(Σ ) → D(Σ ), and the finite limit of
|     |     |     |     |     |     |     |     | n   |     | ∗   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n1/2D(Σ ) then forces D(Σ ) = 0, so the sequence approaches a zero of the denominator,
|     | n   |     |     | ∗   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which may lie in the interior of the cone or on its boundary. The condition s > 0
D,∗
makes this zero first-order nondegenerate, and the condition s > 0 excludes a simul-
g,∗
taneous first-order degeneracy of the moment function itself. The limit µ records how
∗
many first-order standard errors separate the drifting denominator from zero, and it acts
| as the | noncentrality |     | parameter |     | of the | limit | experiment. |     |     |     |     |     |
| ------ | ------------- | --- | --------- | --- | ------ | ----- | ----------- | --- | --- | --- | --- | --- |
The associated Wald procedure studentizes the plug-in estimator along the estimated
ˆ
moment direction. On the event where D(Σ) ̸= 0 and the quadratic form below is
| positive, | define |     |     |     |     |     |         |     |         |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- |
|           |        |     |     |     |     |     | {gˆ⊤Γ(Σ | ˆ   | )gˆ}1/2 |     |     |     |
τˆ−τ
|     | gˆ = | ∇N(Σ)−τˆ∇D(Σ), | ˆ   |     | ˆ   | se(τˆ) | =        |     |      | , T | = n .  | (12) |
| --- | ---- | -------------- | --- | --- | --- | ------ | -------- | --- | ---- | --- | ------ | ---- |
|     |      |                |     |     |     | b      |          |     |      | n   |        |      |
|     |      |                |     |     |     |        | n1/2|D(Σ |     | ˆ )| |     | se(τˆ) |      |
b
| The next | proposition |     | identifies |     | the joint | limits. |     |     |     |     |     |     |
| -------- | ----------- | --- | ---------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
Proposition 1 (Local ratio experiment). Suppose that Assumption 1 holds. Let Z and
0
Z be independent standard normal variables and put Z ˜ = r Z +(1−r2)1/2Z . Then
| 2              |     |     |         |     |     |       |      |     | ∗   | 2   | ∗ 0 |      |
| -------------- | --- | --- | ------- | --- | --- | ----- | ---- | --- | --- | --- | --- | ---- |
|                |     |     |         |     |     | ω Z ˜ |      |     |     |     |     |      |
|                |     |     |         |     | ⇝   | ∗     |      | ⇝   |     |     |     |      |
|                |     |     | τˆ−τ    |     |     |       | , Fb | (µ  | +Z  | )2. |     | (13) |
|                |     |     |         | n   |     |       | D    |     | ∗   | 2   |     |      |
|                |     |     |         |     | µ   | +Z    |      |     |     |     |     |      |
|                |     |     |         |     |     | ∗ 2   |      |     |     |     |     |      |
| If in addition | |r  | | < | 1, then |     |     |       |      |     |     |     |     |      |
∗
|     |     |     |     |     | Z ˜ sgn(µ | +Z  | )   |     | Z ˜ |     |     |      |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |           | ∗   | 2   |     |     |     |     |      |
|     |     |     | T   | ⇝   |           |     | ,   | q = |     | .   |     | (14) |
n
|     |     |     |     | {1−2r |     | q +q2}1/2 |     |     | µ +Z |     |     |     |
| --- | --- | --- | --- | ----- | --- | --------- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |       |     | ∗         |     |     | ∗    | 2   |     |     |
Thus, a first-order nondegenerate small denominator produces the classical Fieller ratio
)2
limit. The limiting standardized denominator (µ +Z is a noncentral chi-squared vari-
∗ 2
able with one degree of freedom and noncentrality µ2, so Fb measures the local strength
|     |     |     |     |     |     |     |     | ∗   | D   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of identification. The Wald statistic converges to a non-Gaussian law governed by µ and
∗
| r . Supplementary |     | Section |     | E proves |     | Proposition |     | 1.  |     |     |     |     |
| ----------------- | --- | ------- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
∗
13

Remark 6 (Role of the local experiment). Proposition 1 is not offered as a new general
theory of weak identification. Its role is to place every covariance-polynomial strategy
in a common three-parameter local experiment and to make the algebraic classification
operational. Once D is known not to self-normalize, the limits µ , r and ω determine
∗ ∗ ∗
the leading ratio geometry. When D is a flag power, the assumptions of this experiment
cannot hold on the denominator side.
5.2 Robust inversion and the boundary of the classification
We connect the ratio experiment to robust inference. For α ∈ (0,1), inverting the single
moment N −tD gives the confidence set
(cid:26) (cid:27)
C = t : n{N(Σ ˆ )−tD(Σ ˆ )}2 ≤ q h⊤Γ(Σ ˆ )h , h = ∇N(Σ ˆ )−t∇D(Σ ˆ ), (15)
1−α 1−α t t t
where
q = inf{x ∈ R : pr(U ≤ x) ≥ 1−α}, U ∼ χ2,
1−α 1
is the (1−α) quantile of the χ2 law.
1
Proposition 2 (Fieller confidence set). Suppose that Assumption 1 holds. Then pr{τ ∈
n
C } → 1−α. Moreover, for every fixed n, with probability one the set C is nonempty
1−α 1−α
and is an interval, the complement of a bounded open interval, or the whole real line, and
it is bounded exactly when Fb > q .
D 1−α
SupplementarySectionEprovesProposition2. ThisistheclassicalFiellerandAnderson–
Rubin analysis specialized to covariance polynomials (Anderson and Rubin, 1949; Fieller,
1954). It gives the standardized denominator a second role. Proposition 1 identifies Fb as
D
the noncentrality diagnostic of the local experiment, and Proposition 2 makes the same
statistic decide whether the inverted set is bounded. Combining the two results, the
probability that C is bounded converges to pr{(µ +Z )2 > q }, so unbounded sets
1−α ∗ 2 1−α
retain a positive limiting frequency under weak drift, in accordance with the impossibility
results for uniformly bounded confidence sets (Gleser and Hwang, 1987; Dufour, 1997).
We now delimit what exact self-normalization removes. As noted after Assumption 1,
the drift forces D(Σ ) = 0 while requiring s (Σ ) = s > 0. For a self-normalizing
∗ D ∗ D,∗
denominator, evaluating (4) at Σ gives s (Σ ) = c1/2|D(Σ )| = 0, so the two require-
∗ D ∗ ∗
ments are incompatible and no drifting sequence satisfies Assumption 1. Therefore, exact
self-normalization excludes the first-order ratio experiment, not every nonregular limit.
The exclusion concerns the first order only. On Sym , the polynomial D = σ2 has
2 12
s2 = 4σ2 (σ σ + σ2 ), so its first-order variance vanishes on the entire zero set and
D 12 11 22 12
Assumption 1 cannot hold, although the ratio s2 /D2 is not constant. Under the drift
D
σ = ζn−1/2 with σ = σ = 1, the standardized denominator converges in distri-
12,n 11,n 22,n
bution to (ζ+Z)2/4 for a standard normal variable Z, a nondegenerate limit generated at
second order. Supplementary Section E verifies this example. Hence, the self-normalizing
and the first-order nondegenerate regimes are two extremes of a broader classification
rather than an exhaustive dichotomy.
14

| 6   | Causal      | applications |            |     |          |     |     |     |     |
| --- | ----------- | ------------ | ---------- | --- | -------- | --- | --- | --- | --- |
| 6.1 | Diagnostics |              | for common |     | formulas |     |     |     |     |
Wetranslatethealgebraintofamiliarcovariancediagnostics. Fordistinctindicesa,b ∈ [d],
ˆ
put ρ = σ /(σ σ )1/2 and let ρˆ be the same function evaluated at Σ . For the
|     | ab ab | aa  | bb  | ab  |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
marginal covariance D = σ , the Gaussian first-order variance is s2 = σ σ + D2,
|     |     |     | ab  |     |     |     |     | D   | aa bb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
so every zero of D in the open cone is first-order nondegenerate and the denominator
conditions of Assumption 1 can hold along suitable drifting sequences. The standardized
|     |     |     | nρˆ2 | ρˆ2 |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
denominator is Fb = /(1 + ), an increasing function of the familiar first-stage
|     |     | D   | ab  | ab  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nρˆ2 /(1−ρˆ2
| statistic |     |     | ).  |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|           | ab  |     | ab  |     |     |     |     |     |     |
For indices e,a,b ∈ [d] with e ̸= a and e ̸= b, allowing a = b, define ρ as the correlation
ab·e
oftheresidualsfromthepopulationlinearprojectionsofcoordinatesaandboncoordinate
e, and let ρˆ be its sample-covariance analogue. For the partial minor D = σ σ −
|     | ab·e |     |     |     |     |     |     |     | ee ab |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | ----- |
σ σ ,
ea eb
|     |     |     | s2 = | detΣ  | detΣ | +3D2. |     |     | (16) |
| --- | --- | --- | ---- | ----- | ---- | ----- | --- | --- | ---- |
|     |     |     |      | {e,a} |      | {e,b} |     |     |      |
D
|     |     |     |     |     |     |     |     | s2  | 4D2, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
When a = b the minor is a principal 2×2 minor, the identity reduces to = and
D
| Fb  | = n/4 in agreement |     | with Theorem | 1.  | When | a ̸= b, define |     |     |     |
| --- | ------------------ | --- | ------------ | --- | ---- | -------------- | --- | --- | --- |
D
nρˆ2
nF
|     |     |     | F = | ab·e  | , Fb | = par | ,   |     |     |
| --- | --- | --- | --- | ----- | ---- | ----- | --- | --- | --- |
|     |     |     | par |       |      | D     |     |     |     |
|     |     |     |     | 1−ρˆ2 |      | n+4F  |     |     |     |
|     |     |     |     | ab·e  |      |       | par |     |     |
so the standardized denominator is again an increasing transform of the familiar partial
first-stageindex F . Inboth casesthestandardized denominatorreproducesthe relevant
par
marginal or partial screening direction without any modelling input. Supplementary
Proposition F.1 gives the calculation and the exact partial-correlation formula.
We compare four representative strategies in Table 1. The table separates variance-type
flag powers from slope-type marginal or nonprincipal minors. The structural parame-
terizations and substitutions yielding the third column are given in Supplementary Sec-
tion F.1, so that each displayed pullback can be checked directly from the stated linear
reduced form. The three slope-type rows can realize the denominator conditions of As-
sumption 1, whereas the front-door row is a flag power. The next subsection develops the
| front-door | strategy   | in  | detail.    |     |                 |     |     |           |     |
| ---------- | ---------- | --- | ---------- | --- | --------------- | --- | --- | --------- | --- |
| 6.2        | Front-door |     | adjustment | and | boundary-robust |     |     | inference |     |
We now show that the front-door studentized statistic survives arbitrary collinearity drift
when the treatment–mediator coefficient is nonzero. The exact regression decomposition
and the proof of the boundary result are given in Supplementary Section F.3. Consider
| the | Gaussian reduced |     | form   |     |       |        |     |     |      |
| --- | ---------------- | --- | ------ | --- | ----- | ------ | --- | --- | ---- |
|     |                  |     | M = aX | +ε  | , Y = | bM +γX | +ε, |     | (17) |
M
in which X, ε and ε are independent centred Gaussian variables with var(X) = ν > 0
|     | M   |     |     |     |     |     |     |     | X   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(X,M,Y)⊤.
and var(ε) > 0, and the observed vector is The coefficients a, b and γ are
fixed, while the mediator residual variance v = var(ε ) may change with n and takes
|     |     |     |     |     | M,n | M   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
values in a fixed interval (0,v¯]. Observations are n independent copies of the observed
vector, and Σ ˆ is the known-mean sample covariance (1). Substituting the reduced form
15

Table 1: Denominator structure of four linear causal strategies. Each structural pullback eval-
uates the denominator in a linear reduced form for that row, detailed in Supplementary Sec-
tion F.1, and symbols are defined separately within each row. In the two instrument rows, π
is the coefficient of the instrument Z in the equation for the treatment X, ν and ν are the
|     |     |     |     |     |     |     |     |     |     | Z   | W   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
variancesofZ andoftheconditioningcovariateW,andv istheresidualvarianceofZ givenW.
Z
In the front-door row, ν is the treatment variance and v is the mediator residual variance.
|     |     |     | X   |     |     |     |     |     | M   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In the proximal row, a and c are the coefficients of the latent variable U in the equations for
the proxies Z and W, ν is the variance of U, and v is the treatment residual variance. A
|     |     |     | U   |     |     |     |     | A   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
flag power is a denominator of the form (5). Marginal slope and partial slope denote a marginal
covariance and a nonprincipal two-by-two minor, and together they constitute the slope type.
|     | Strategy     |            |          | Denominator |       |      |     | Structural | pullback | Classification |     |
| --- | ------------ | ---------- | -------- | ----------- | ----- | ---- | --- | ---------- | -------- | -------------- | --- |
|     | Instrumental |            | variable | σ           |       |      |     | πν         |          | Marginal slope |     |
|     |              |            |          | ZX          |       |      |     |            | Z        |                |     |
|     | Conditional  | instrument |          | σ           | σ     | −σ   | σ   | πv         | ν        | Partial slope  |     |
|     |              |            |          | WW          | ZX    | ZW   | WX  |            | Z W      |                |     |
|     |              |            |          |             |       |      | −σ2 | ν2v        |          |                |     |
|     | Front-door   |            |          | σ XX        | (σ XX | σ MM |     | )          | M        | Flag power     |     |
|     |              |            |          |             |       |      | XM  | X          |          |                |     |
|     | Linear       | proximal   |          | σ           | σ     | −σ   | σ   | acν        | v        | Partial slope  |     |
|     |              |            |          | ZW          | AA    | ZA   | AW  |            | U A      |                |     |
ν2
gives σ = ν and detΣ = ν v , so the population denominator equals v ,
|     | XX  | X   |     | {X,M} | X   | M,n |     |     |     |     | X M,n |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- |
which is the pullback recorded in Table 1 and which tends to zero whenever v does.
M,n
| The | front-door | covariance |     | functional |     | is  |     |     |       |     |     |
| --- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | ----- | --- | --- |
|     |            |            |     |            | σ   | (σ  | σ   | −σ  | σ )   |     |     |
|     |            |            |     |            |     | XM  | XX  | MY  | XM XY |     |     |
|     |            |            |     | τ (Σ)      | =   |     |     |     | ,     |     |     |
|     |            |            |     | fd         |     | σ   | (σ  | σ   | −σ2 ) |     |     |
|     |            |            |     |            |     | XX  | XX  | MM  |       |     |     |
XM
on the set where its denominator is nonzero. Direct substitution shows that τ (Σ ) = ab
fd n
for every value of γ, so the functional isolates the product ab and removes the association
| carried | by γ. |     |     |     |     |     |     |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Example 2 (Exact front-door denominator). In the front-door causal model, the coef-
ficient γ is generated by an unobserved confounder of X and Y rather than by a direct
effect, so the total effect of X on Y equals ab and is identified by τ . The denominator
fd
| is the | flag power | identified |      | in Section |      | 3, and | Theorem |     | 1 gives   |              |      |
| ------ | ---------- | ---------- | ---- | ---------- | ---- | ------ | ------- | --- | --------- | ------------ | ---- |
|        | D          | = σ        | detΣ |            | = σ2 | var(M  | |       | X), | s2 = 10D2 | , Fb = n/10. | (18) |
|        | fd         | XX         |      |            |      |        |         |     |           | D            |      |
|        |            |            |      | {X,M}      | XX   |        |         |     | D fd      |              |      |
The last equality holds for every positive-definite sample covariance when the Gaussian
| studentizer | is  | used, whatever |     | the | data-generating |     |     | law. |     |     |     |
| ----------- | --- | -------------- | --- | --- | --------------- | --- | --- | ---- | --- | --- | --- |
Thus a relevance test based on the front-door denominator is exactly uninformative even
| though | the | precision | of τˆ | can deteriorate |     |     | without | bound. |     |     |     |
| ------ | --- | --------- | ----- | --------------- | --- | --- | ------- | ------ | --- | --- | --- |
Because D is exactly self-normalizing, no drifting sequence satisfies Assumption 1 for
fd
this strategy, and the ratio experiment of Section 5 is unavailable as a description of the
boundary v → 0. That exclusion is negative information only. The following result
M,n
provides the positive counterpart for the studentized estimator. The plug-in estimator is
ˆ
| τˆ = | τ (Σ), | and its Gaussian |     | delta | standard |     | error | is  |     |     |     |
| ---- | ------ | ---------------- | --- | ----- | -------- | --- | ----- | --- | --- | --- | --- |
fd
1
|     |     |     |     |     |     |     | ˆ        | ˆ   | ˆ     |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | --- | ---- |
|     |     |     |     | se2 | =   | ∇τ  | (Σ )⊤Γ(Σ | )∇τ | (Σ ). |     | (19) |
|     |     |     |     | b   |     | fd  |          |     | fd    |     |      |
n
|     |     |     |     |     |     |     |     | ˆ   |     | ˆ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Both quantities are defined almost surely because Σ ≻ 0 implies D (Σ) > 0.
fd
16

Proposition 3 (Boundary-robust front-door Wald inference). Under the reduced form
(17) with a ̸= 0,
τˆ−ab
⇝ N (0,1),
1
se
b
along every sequence v ∈ (0,v¯], including sequences with nv → C for any C ∈
M,n M,n
[0,∞].
Thus, arbitrarily poor mediator residual variation inflates uncertainty but does not inval-
idate the studentized Gaussian limit on the stated parameter region.
Remark 7 (Why studentization survives). The covariance estimator factors exactly as
the product of the slope in the regression of M on X and the coefficient of M in the
regression of Y on (X,M). Conditional on the second regression design, the latter co-
efficient has an exact Student statistic. As v decreases, the first slope is estimated
M,n
more accurately while the second standard error grows at the reciprocal rate. The Gaus-
sian delta studentizer reproduces this balance exactly, so the exploding variance affects
precision but not the limiting studentized law.
Therestrictiona ̸= 0inProposition3isdeliberate. Thepropositioncoversb = 0whena ̸=
0, but it makes no claim on the stratum a = 0, whether or not b vanishes. At the doubly
singular point a = b = 0 the numerator gradient vanishes, the estimator has a product-of-
normals limit at rate n, and the nonregularity is a singular-hypothesis phenomenon of the
numerator rather than a weak-denominator phenomenon (Drton and Xiao, 2016). The
exact denominator identity in (18) remains true throughout these parameter regions.
7 Numerical experiments
7.1 Design
Two Monte Carlo experiments isolate the two denominator mechanisms of Table 1, one
flag power and one partial slope. The front-door design sets X = ε , M = 0.8X + ε
X M
and Y = M +ε , where (ε ,ε ) is centred Gaussian with unit marginal variances and
Y X Y
covariance 0.5, and ε is an independent Gaussian variable with variance v ; the target
M M
is the total effect 0.8. The proximal design sets Z = 0.8U + ε , A = 0.8U + ε , W =
Z A
0.8U +ε and Y = A+0.8U +ε , with mutually independent centred Gaussian shocks
W Y
of unit variance except var(ε ) = v ; the target is the coefficient of A, equal to one. By
A A
the structural pullbacks in Table 1, the population denominators are v and 0.64v , so
M A
the grids v ∈ {1,0.1,0.01,0.001} and v ∈ {1,0.3,0.1,0.03,0.01} trace the approach to
M A
the two denominator boundaries. The population value of nD(Σ)2/s2 (Σ) equals n/10
D
identically in the front-door design and falls from 63.7 to 0.1 across the proximal grid
(Supplementary Table G.1).
ˆ
For each cell, we draw the known-mean sample covariance directly from nΣ ∼ W (n,Σ),
d
with d = 3 and d = 4 respectively, which is distributionally equivalent to simulating n
centred Gaussian observations. The converse classification of Section 4 is not invoked
at d = 4: Theorem 1, Proposition 1 and the calibrations of Section 6 hold in every
dimension, and the proximal denominator depends only on the (A,Z,W) block, so its
slope-type status is unchanged by the ambient dimension (Supplementary Lemma B.4).
We use n = 1000 and 100000 replications per cell. Each replication yields the plug-in
estimator τˆ, the standardized denominator Fb , and, in the proximal design, the partial
D
17

statistic F of Section 6 with (e,a,b) = (A,Z,W) together with the deliberately naive
par
marginal statistic nρˆ2 /(1−ρˆ2 ), which measures only the treatment–proxy association.
AZ AZ
Cells are summarized by medians and by the interquartile range of τˆ divided by 1.349,
because the ratio estimator need not possess moments in the weak cells, and by the
empirical coverage of nominal 95% Wald intervals based on the delta standard error in
(12) and of the inversion (15). The estimator, both intervals and all diagnostics were
well defined in every replication. The Python scripts reproducing both the numerical
experiments and the real data experiments in Section 8 are available at https://github.
com/shutech2001/self-normalizing-denominators-experiments.
The theory yields three predictions. First, Theorem 1 (iv) and Example 2 imply that
Fb = n/10 = 100 in every front-door replication, and Proposition 3 implies nominal
D
Wald coverage along the whole grid, whose smallest cell has nv = 1 and so lies inside
M
the boundary regime nv → C ∈ [0,∞]. Secondly, the weak proximal cells have
M,n
populationvaluesofnD(Σ)2/s2 (Σ)belowone,matchingthedriftregimeofAssumption1,
D
so Proposition 1 predicts the noncentral limit for Fb in (13) and distorted Wald inference.
D
Thirdly, Proposition 2 predicts near-nominal coverage for the inversion (15) in every cell,
with sets that are bounded exactly when Fb exceeds the 0.95 quantile 3.84 of the χ2 law.
D 1
7.2 Results
Table2reportstheresults. Inthefront-doordesignthemedianstandardizeddenominator
equals the theoretical constant 100.0 in every cell; by Theorem 1 (iv) the statistic equals
n/10 in every replication, so it carries no information about v . Precision, by contrast,
M
deteriorates by a factor of eighteen: the robust standard deviation of τˆ rises from 0.038
to 0.696 as v falls from 1 to 0.001, and the median delta standard error tracks it closely,
M
rising from 0.038 to 0.693. Wald coverage lies between 0.949 and 0.950 in all four cells,
including the boundary cell with nv = 1, and inversion coverage lies between 0.953 and
M
0.955, slightly above the nominal level. This confirms the first prediction: the studentized
statistic remains accurate while the denominator diagnostic is exactly uninformative.
In the proximal design the naive marginal statistic rises from 179.7 to 624.6 as v de-
A
creases, while the partial statistic falls from 85.6 to 0.5 and the median Fb falls from 63.8
D
to 0.5; the latter two columns accord with the identity between Fb and F stated after
D par
(16). At v = 0.03 and 0.01 the median bias reaches 0.44 and 0.88 and Wald coverage
A
falls to 0.930 and 0.931, although the naive diagnostic is largest exactly there. In those
two cells the median standard error exceeds the robust standard deviation, so the Wald
failure is one of centring and distributional shape rather than of scale, as the ratio limit
in (13) predicts. Inversion coverage remains between 0.951 and 0.953 throughout, but the
protection has a price: in the two weakest cells the median Fb lies below 3.84, so more
D
than half of the inverted sets are unbounded.
The two designs estimate different targets in different models, so the experiment com-
pares diagnostics rather than estimators. Its message is the dissociation predicted by the
classification: front-door adjustment loses precision without entering the first-order ratio
regime, whereas the proximal estimator fails in the partial-covariance direction that the
marginal treatment–proxy statistic does not measure. Supplementary Section G gives
complete cell summaries.
18

Table 2: Gaussian simulation results based on 100000 replications per cell. Med., median across
replications; s.e., Gaussian delta standard error; robust s.d., interquartile range of τˆ divided by
1.349; cov., empirical coverage, the two entries giving the nominal 95% Wald interval and the
inversion (15). Dashes indicate diagnostics defined only for the proximal design. Bias entries
of 0.00 are zero to the precision shown. The largest Monte Carlo standard error for a coverage
entry is 0.0008.
Parameter Med. FbD Med. partial F Med. naive F Robust s.d. Med. s.e. Med. bias Wald/inv. cov.
| Front-door: |     | parameter | v   |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
M
|           | 1.00      | 100.0 |     |     | –   | –   | 0.038 | 0.038 | 0.00 0.949/0.954 |
| --------- | --------- | ----- | --- | --- | --- | --- | ----- | ----- | ---------------- |
|           | 0.10      | 100.0 |     |     | –   | –   | 0.070 | 0.070 | 0.00 0.950/0.955 |
|           | 0.01      | 100.0 |     |     | –   | –   | 0.217 | 0.219 | 0.00 0.949/0.954 |
|           | 0.001     | 100.0 |     |     | –   | –   | 0.696 | 0.693 | 0.00 0.950/0.953 |
| Proximal: | parameter |       | v   |     |     |     |       |       |                  |
A
|     | 1.00 | 63.8 |             | 85.6 |        | 179.7 | 0.064 | 0.063 | 0.00 0.952/0.953 |
| --- | ---- | ---- | ----------- | ---- | ------ | ----- | ----- | ----- | ---------------- |
|     | 0.30 | 26.5 |             | 29.6 |        | 362.0 | 0.173 | 0.170 | 0.00 0.952/0.952 |
|     | 0.10 | 6.2  |             | 6.4  |        | 510.2 | 0.491 | 0.468 | 0.01 0.935/0.953 |
|     | 0.03 | 0.9  |             | 0.9  |        | 595.2 | 1.187 | 1.433 | 0.44 0.930/0.952 |
|     | 0.01 | 0.5  |             | 0.5  |        | 624.6 | 1.460 | 2.037 | 0.88 0.931/0.951 |
| 8   | Real | data | experiments |      |        |       |       |       |                  |
| 8.1 | Data | and  | diagnostic  |      | design |       |       |       |                  |
We audit the public SUPPORT right-heart-catheterization data (Connors et al., 1996),
which contain 5735 critically ill patients, an indicator of right-heart catheterization on
the first study day, survival time in days truncated at 30, and baseline physiological
measurements. Following proximal analyses of these data (Liu et al., 2025; Tchetgen Tch-
etgen et al., 2024), we consider treatment proxies pafi1 and paco21 and outcome proxies
ph1 and hema1. The analysis is the diagnostic pathway described in the introduction
rather than a new clinical causal analysis: the symbolic factor-and-rank step has already
classified the proximal denominator as a nonprincipal slope minor (Example 1), and the
data-level step measures the implied partial direction for each candidate proxy pair.
Treatment, outcome and the four proxies are residualized by least squares on age, sex,
primary and secondary disease categories, do-not-resuscitate status, the SUPPORT two-
monthsurvivalestimateandtheAPACHEscore; missingcontinuouscovariatesaremedian-
imputed, and missing categorical covariates are mode-imputed and coded by indicator
variables with one level omitted. The resulting design has rank r = 19, and all diagnos-
tics use the residual degrees of freedom ν = n−r = 5716 in place of n. For residualized
treatment A, treatment proxy Z and outcome proxy W, we report the naive marginal
statistic νρˆ2 /(1 − ρˆ2 ), the partial statistic νρˆ2 /(1 − ρˆ2 ) and two versions of
|     |     | AZ  | AZ  |     |     |     | ZW·A | ZW·A |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
the standardized denominator: the Gaussian version of Section 6, and a sandwich version
ˆ
in which Γ(Σ) in (3) is replaced by the empirical covariance matrix of the six second-
moment scores. Because the original treatment is binary, the residualized treatment is
non-Gaussian. The Gaussian fourth-moment formula therefore serves only as a reference
value. The sandwich version is the appropriate studentization under the empirical law
(Remark 1). Sampling variability of the proximal estimates and of the sandwich statistic
is assessed by 2000 nonparametric percentile bootstrap replications over patients, each of
which repeats the imputation, coding and residualization. The audit is descriptive: proxy
strength in the denominator direction is measurable, but proxy validity is not testable
19

Table3: DenominatorauditfortheSUPPORTdata. CI,percentilebootstrapconfidenceinterval
based on 2000 replications. All statistics are scaled by the residual degrees of freedom ν = 5716.
The naive and partial statistics are the indices νρˆ2/(1−ρˆ2) defined in the text, not finite-sample
F tests, and the naive statistic depends only on the treatment proxy. The sandwich statistic
uses the empirical covariance matrix of the six second-moment scores.
Treatment proxy Outcome proxy Naive F Partial F Gaussian FbD Sandwich FbD (95% CI)
pafi1 ph1 173.4 3.2 3.2 2.3 (0.0, 12.7)
pafi1 hema1 173.4 32.3 31.6 25.7 (9.2, 51.3)
paco21 ph1 16.4 1980.0 830.0 315.2 (218.2, 461.9)
paco21 hema1 16.4 69.3 66.1 51.3 (30.3, 78.4)
from these diagnostics.
Full variable definitions and preprocessing details are given in Supplementary Section H.1,
and the second-moment score construction and bootstrap implementation are given in
Supplementary Section H.2.
8.2 Results
Table 3 reports the audit, and the two pairs involving ph1 reverse their ordering across
diagnostics. The pair pafi1/ph1 appears strong in the treatment–proxy direction, with
naive statistic 173.4, but is weak in the direction that enters the denominator. Its partial
statistic is 3.2 and its sandwich statistic is 2.3, with a bootstrap interval reaching essen-
tially zero. The pair paco21/ph1 shows the reverse pattern, with naive statistic 16.4 but
partial statistic 1980.0 and sandwich statistic 315.2, bounded well away from zero. The
Gaussian version is the monotone transform of the partial statistic given after (16) with
ν in place of n, which explains why those two columns nearly coincide when the partial
statistic is small relative to ν. The sandwich column carries the additional distributional
information. It is smaller than the Gaussian value for every pair, by factors of 0.72 to
0.81 for three pairs and 0.38 for paco21/ph1. Thus, the Gaussian formula overstates de-
nominator strength under the empirical fourth moments, most severely for the strongest
pair.
The plug-in proximal estimates for the four pairs, in the order of Table 3, are −1.25,
−1.41, −1.33 and −1.14 days, with percentile intervals (−2.25,0.14), (−2.04,−0.81),
(−1.84,−0.81) and (−1.69,−0.56). Only the interval for the weak pair pafi1/ph1 cov-
ers zero. For that pair, however, the bootstrap interval inherits the nonstandard ratio
behaviour described in Section 5 and is reported for completeness only; the inversion
(15) is the appropriate construction in that regime. None of these intervals validates the
proximal bridge assumptions, which the audit cannot test.
The audit illustrates the practical content of the classification. A strong association
between treatment and a proposed treatment proxy neither implies nor precludes strength
of the nonprincipal minor that identifies the proximal bridge; the symbolic step locates
the relevant covariance direction before any estimation, and the partial and sandwich
statistics then measure it for each candidate allocation.
20

9 Discussion
The classification turns the choice among rational identification formulas into a design de-
cision. When several certificates identify the same target, their denominators can belong
to different algebraic classes even though the ratios agree on the model. The classes are
complementary rather than ordered, because a flag denominator removes first-order de-
nominator nonregularity while a slope-type formula may be more precise at strongly iden-
tified distributions. Therefore, we recommend reporting the symbolic denominator class
alongside any covariance plug-in estimate. When a denominator is not self-normalizing
and its relevant standardized diagnostic is weak, inference should also include a robust
inversion.
The main open algebraic problem is the rigidity of the mixed kernel line. A proof that the
kernel line in Theorem 3 (iii) is constant would complete the unconditional three-variable
converse, while a counterexample would produce a self-normalizing denominator outside
the flag class. Either resolution must exploit the integrability of the relative gradient
beyond its vanishing Hessian. In dimension at least four, a converse would additionally
require invariants beyond the first two power sums of the relative gradient.
Theprincipaldistributionalquestionisself-normalizationbeyondtheGaussiancovariance
operator. Ellipticity only rescales the constant, so the first open case is a semiparametric
familywithunrestrictedfourthcumulants. Acharacterizationofpolynomialswhosesand-
wich variance is proportional to their square over such a family would determine when the
standardized denominator remains a samplewise constant under a matched studentizer.
This, in turn, would establish how far the exact screening interpretation extends.
The principal methodological question concerns selection among many candidate strate-
gies. Choosing a certificate because its observed denominator diagnostic is largest rein-
troduces a data-adaptive weak-direction problem. Therefore, applications with many
proxies or graph-derived formulas call for selection-adjusted denominator diagnostics and
simultaneous robust inversions (Wang et al., 2025; Bennett et al., 2026). Because the
factor-and-rank audit is symbolic, it could also be attached to computer-algebra iden-
tification pipelines, so that every certificate is generated together with its denominator
class.
Declaration of the use of generative AI and AI-assisted
technologies
During the preparation of this work the author used ChatGPT and Claude in order to
assist with writing and refactoring the simulation code. After using these tools the author
reviewed and edited the content as necessary and takes full responsibility for the content
of the publication.
Acknowledgement
Shu Tamano was supported by JSPS KAKENHI Grant Numbers 25K24203.
21

Supplementary material
The Supplementary Material includes a notation table, all omitted proofs, the elliptical
and unknown-mean extensions, the recursive-flag and boundary-rigidity converses, the
Fieller and minor-calibration results, detailed simulation and SUPPORT analyses, and
the algebraic obstructions to an unrestricted three-variable converse.
References
Anderson, T. W. and Rubin, H. (1949). Estimation of the parameters of a single equation
in a complete system of stochastic equations. The Annals of Mathematical Statistics,
20(1):46–63.
Andrews, D. W. K. and Cheng, X. (2012). Estimation and inference with weak, semi-
strong, and strong identification. Econometrica, 80(5):2153–2211.
Andrews, I., Stock, J. H., and Sun, L. (2019). Weak instruments in instrumental variables
regression: Theory and practice. Annual Review of Economics, 11:727–753.
Bennett, A., Kallus, N., Mao, X., Newey, W. K., Syrgkanis, V., and Uehara, M. (2026).
Inference on strongly identified functionals of weakly identified functions. Journal of
the Royal Statistical Society Series B: Statistical Methodology, 88(3):998–1028.
Bhatia, R. (2007). Positive Definite Matrices. Princeton University Press.
Brito, C. and Pearl, J. (2002). Generalized instrumental variables. In Proceedings of the
18th Conference on Uncertainty in Artificial Intelligence, pages 85–93.
Ciliberto, C., Russo, F., and Simis, A. (2008). Homaloidal hypersurfaces and hypersur-
faces with vanishing hessian. Advances in Mathematics, 218(6):1759–1805.
Connors, A. F., Speroff, T., Dawson, N. V., Thomas, C., Harrell, F. E., Wagner, D.,
Desbiens, N., Goldman, L., Wu, A. W., Califf, R. M., Fulkerson, W. J., Vidaillet, H.,
Broste, S., Bellamy, P., Lynn, J., and Knaus, W. A. (1996). The effectiveness of right
heart catheterization in the initial care of critically ill patients. The Journal of the
American Medical Association, 276(11):889–897.
Drton, M. and Weihs, L. (2016). Generic identifiability of linear structural equation
models by ancestor decomposition. Scandinavian Journal of Statistics, 43(4):1035–
1045.
Drton, M. and Xiao, H. (2016). Wald tests of singular hypotheses. Bernoulli, 22(1):38–59.
Dufour, J.-M. (1997). Some impossibility theorems in econometrics with applications to
structural and dynamic models. Econometrica, 65(6):1365–1387.
Faraut, J. and Korányi, A. (1994). Analysis on Symmetric Cones. Oxford University
Press.
Fieller,E.C.(1954). Someproblemsinintervalestimation. Journal of the Royal Statistical
Society Series B: Statistical Methodology, 16(2):175–185.
Foygel, R., Draisma, J., andDrton, M.(2012). Half-trekcriterionforgenericidentifiability
of linear structural equation models. The Annals of Statistics, 40(3):1682–1713.
22

García-Puente, L. D., Spielvogel, S., and Sullivant, S. (2010). Identifying causal effects
with computer algebra. In Proceedings of the 26th Conference on Uncertainty in Arti-
ficial Intelligence, pages 193–200.
Gleser, L. J. and Hwang, J. T. (1987). The nonexistence of 100(1−α)% confidence sets
of finite expected diameter in errors-in-variables and related models. The Annals of
Statistics, 15(4):1351–1362.
Gondim, R. and Russo, F. (2015). On cubic hypersurfaces with vanishing hessian. Journal
of Pure and Applied Algebra, 219(4):779–806.
Gordan, P. and Noether, M. (1876). Ueber die algebraischen formen, deren hesse’sche
determinante identisch verschwindet. Mathematische Annalen, 10:547–568.
Gordon, S. L., Kumar, V. M., Schulman, L. J., and Srivastava, P. (2021). Condition num-
berboundsforcausalinference. InProceedings of the 37th Conference on Uncertainty in
Artificial Intelligence, volume 161 of Proceedings of Machine Learning Research, pages
1948–1957.
Harris, J. (1992). Algebraic Geometry: A First Course, volume 133 of Graduate Texts in
Mathematics. Springer.
Henckel, L., Buttenschoen, M., and Maathuis, M. H. (2024). Graphical tools for selecting
conditional instrumental sets. Biometrika, 111(3):771–788.
Iwashita, T. and Siotani, M. (1994). Asymptotic distributions of functions of a sample
covariance matrix under the elliptical distribution. The Canadian Journal of Statistics,
22(2):273–283.
Kuroki, M. and Pearl, J. (2014). Measurement bias and effect restoration in causal
inference. Biometrika, 101(2):423–437.
Lee, D. S., McCrary, J., Moreira, M. J., and Porter, J. (2022). Valid t-ratio inference for
IV. American Economic Review, 112(10):3260–3290.
Lichtenstein, W. (1982). A system of quadrics describing the orbit of the highest weight
vector. Proceedings of the American Mathematical Society, 84(4):605–608.
Liu, J., Park, C., Li, K., and Tchetgen Tchetgen, E. J. (2025). Regression-based proximal
causal inference. American Journal of Epidemiology, 194(7):2030–2036.
Lossen, C. (2004). When does the hessian determinant vanish identically? on gordan and
noether’s proof of hesse’s claim. Bulletin of the Brazilian Mathematical Society, New
Series, 35:71–82.
Mareis, L., Sturma, N., and Drton, M. (2026). Semiparametric inference for half-trek
estimators in linear structural equation models. arXiv preprint arXiv:2606.26931.
Miao, W., Geng, Z., and Tchetgen Tchetgen, E. J. (2018). Identifying causal effects with
proxy variables of an unmeasured confounder. Biometrika, 105(4):987–993.
Muirhead, R. J. (1982). Aspects of Multivariate Statistical Theory. Wiley, New York.
Pearl, J. (1995). Causal diagrams for empirical research. Biometrika, 82(4):669–688.
Perazzo, U. (1900). Sulle varietà cubiche la cui hessiana svanisce identicamente. Giornale
Di Matematiche Di Battaglini, 38:337–354.
23

Sankararaman, K. A., Louis, A., and Goyal, N. (2022). Robust identifiability in linear
structural equation models of causal inference. In Proceedings of the 38th Conference on
Uncertainty in Artificial Intelligence, volume 180 of Proceedings of Machine Learning
| Research, | pages 1728–1737. |     |     |
| --------- | ---------------- | --- | --- |
Schulman, L. J. and Srivastava, P. (2016). Stability of causal inference. In Proceedings of
the 32nd Conference on Uncertainty in Artificial Intelligence, pages 666–675.
Shapiro, A. and Browne, M. W. (1987). Analysis of covariance structures under elliptical
distributions. Journal of the American Statistical Association, 82(400):1092–1097.
Staiger, D. and Stock, J. H. (1997). Instrumental variables regression with weak instru-
| ments. | Econometrica, 65(3):557–586. |     |     |
| ------ | ---------------------------- | --- | --- |
Stock, J. H. and Wright, J. H. (2000). GMM with weak identification. Econometrica,
68(5):1055–1096.
TchetgenTchetgen,E.J.,Ying,A.,Cui,Y.,Shi,X.,andMiao,W.(2024). Anintroduction
| to proximal | causal inference. | Statistical | Science, 39(3):375–390. |
| ----------- | ----------------- | ----------- | ----------------------- |
van der Zander, B., Textor, J., and Liśkiewicz, M. (2015). Efficiently finding conditional
instruments for causal inference. In Proceedings of the 24th International Joint Con-
| ference | on Artificial Intelligence, | pages | 3243–3249. |
| ------- | --------------------------- | ----- | ---------- |
Wang, R., Chan, K. C. G., and Ye, T. (2025). GMM with many weak moment conditions
and nuisance parameters: General theory and applications to causal inference. arXiv
| preprint | arXiv:2505.07295. |     |     |
| -------- | ----------------- | --- | --- |
24

Supplementary Material for
“Self-normalizing denominators in rational causal
estimation”
A Notation
A.1 Linear-algebraic, algebraic and geometric conventions
WecollecttheconventionsneededtoreadtheSupplementaryMaterialindependently. Fix
d ≥ 1, write [d] = {1,...,d}, put p = d(d+1)/2 and I = {(i,j) : 1 ≤ i ≤ j ≤ d}, and
d d
use the lexicographic order (1,1),(1,2),...,(1,d),(2,2),...,(d,d). Vectors are columns,
A⊤ is transpose, A−⊤ = (A−1)⊤ for nonsingular A, I is the identity matrix and e is the
m j
jth standard basis vector. The symbols tr, det, rank and spec denote trace, determinant,
rank and the eigenvalue multiset. For I,J ⊆ [d], A is the corresponding submatrix,
I,J
A = A and A = A .
I I,I 1:r {1,...,r},{1,...,r}
The space Sym = {A ∈ Rd×d : A = A⊤} has positive-definite and positive-semidefinite
d
cones Sd and Sd. For A ∈ Sym , vech(A) ∈ Rp d stacks the upper-triangular entries in
++ + d
the stated order. The coordinate ring R[Sym ] = R[σ : (i,j) ∈ I ] is identified with the
d ij d
polynomial maps Sym → R; P ≡ 0 means equality in this ring, deg(P) is total degree,
d
and homogeneity, divisibility and coprimality are understood in the indicated coordinate
ring. For P ∈ R[Sym ], ∇P is the coordinate gradient in the vech order, and
d
(cid:12)
d (cid:12)
dP (H) = P(Σ+tH)(cid:12) , dP (H) = tr{G (Σ)H},
Σ dt (cid:12) Σ P
(cid:12)
t=0
define the Fréchet differential and symmetric gradient. The relative gradient is R (Σ) =
P
G (Σ)Σ/P(Σ) on {P ̸= 0}.
P
Throughout the remaining algebraic conventions, k denotes either R or C. For a real
vector space V, its complexification is V = V ⊗ C. The notation GL (k) denotes the
C R m
group of nonsingular m×m matrices over k, span (S) is the linear span of S, and ker(A),
k
range(A)androwspace(A)arethekernel, rangeandrowspaceofamatrix. Whenthefield
is clear, the subscript on span is omitted. For a real subspace V ⊆ Rd, V⊥ = {x ∈ Rd :
x⊤v = 0 for every v ∈ V}, and diag(a ,...,a ) is the diagonal matrix with the displayed
1 m
entries. The matrix unit E ∈ km×m has a one in position (i,j) and zeros elsewhere.
ij
For an integral domain R, Frac(R) is its field of fractions. If R is a unique factorization
domain, abbreviated UFD, then gcd(f ,...,f ) denotes a greatest common divisor, de-
1 s
fined up to multiplication by a unit. A vector with entries in R is primitive when the
greatest common divisor of its entries is a unit. For a finite-dimensional k-vector space V
and K ≥ 0, SymK(V) is the Kth symmetric tensor power,
SymK(V) = V⊗K/⟨v ⊗···⊗v −v ⊗···⊗v : v ,...,v ∈ V, π ∈ S ⟩,
1 K π(1) π(K) 1 K K
where the angle brackets denote linear span, S is the symmetric group on {1,...,K},
K
and Sym0(V) = k. Its dual is naturally the space of homogeneous polynomial functions
of degree K on V. After choosing the standard basis, Sym2(km) is identified with the
space of symmetric m×m matrices over k.
25

|     |     |     |     |     |     | P(V) |     | {0})/k× |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------- | --- | --- | --- |
For a finite-dimensional k-vector space V, = (V \ is its projective space,
|     |     |     |     |     |     |     |     | Pm P(Cm+1) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
and [v] is the point represented by v ̸= 0. We write C = and Gr(r,V) for the
Grassmannian of r-dimensional linear subspaces of V; thus Gr(r,d) = Gr(r,Cd). More
C
generally, a subscript C on a real algebraic variety or construction denotes extension of
scalars from R to C, equivalently the complex variety defined by the same real polynomial
equations. A dashed arrow f : X (cid:57)(cid:57)(cid:75) Y denotes a rational map: it is represented by a
morphism on a Zariski-dense open subset of X, and two representatives are identified
when they agree on a Zariski-dense open subset. When X is irreducible, every nonempty
Zariski-open subset is dense. For a homogeneous polynomial p, the notation {p = 0}
red
q
denotes the reduced projective hypersurface defined by the radical ideal (p); it has the
same underlying zero set as {p = 0} but carries no multiplicities. Terms such as Zariski
open, closed, dense and irreducible refer to this algebraic topology over the field stated in
the argument.
For a differentiable map F : Sym → W into a finite-dimensional vector space and
d
| H ∈ Sym | , its directional |     | derivative |     | is  |     |     |     |     |     |     |
| ------- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
d
(cid:12)
d
(cid:12)
|     |     |     |     | ∂ F(Σ) | =   | F(Σ+tH)(cid:12) |     | .        |     |     |     |
| --- | --- | --- | --- | ------ | --- | --------------- | --- | -------- | --- | --- | --- |
|     |     |     |     | H      |     |                 |     | (cid:12) |     |     |     |
|     |     |     |     |        |     | dt              |     | (cid:12) |     |     |     |
t=0
For scalar F, this equals dF (H); for matrix-valued F it is taken entrywise. Ordinary
Σ
symbols such as ∂ and ∂ denote coordinate derivatives. The symbol HessF means the
q ri
coordinate Hessian of a scalar function on the affine space Sym . When a Riemannian
d
metric g is explicitly fixed, grad f, ∇g and Hess f denote its gradient, Levi–Civita
g
g
connection and Riemannian Hessian, and ∥·∥ is the induced norm.
g
For a square matrix A, adj(A) is its classical adjugate, so Aadj(A) = adj(A)A = det(A)I,
where I has the same order as A. For a polynomial F on Sym , the adjugate transform is
3
F† = F ◦adj. If V ⊆ Rd has dimension r, M is any full-row-rank matrix with row space
V
V and ∆ (Σ) = det(M ΣM⊤). If P ∈ Rd×r has range V, then F (S) = F(P SP⊤)
|     | V   |     | V   |     | V   |     |     |     |     | V   | V   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | V   |     |     |     |     |     |     | V   |
is the face restriction and S (V) = {A ∈ Sd : range(A) ⊆ V}. For a polynomial F on
+
+
Sym , a plane V is called F-good when F ̸≡ 0; when F is clear, such a plane is called
| 3   |     |     |     |     |     | V   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
good. If finitely many polynomials are under discussion, a generic good plane means
a plane in a common nonempty Zariski-open set on which all indicated restrictions are
nonzero and retain their generic factorization type. On Sym we use δ(Σ) = det(Σ) and
3
F(uu⊤).
p (u) =
F
For later representation-theoretic notation, let gl (k) be the vector space of all m × m
m
matrices. Its derived congruence action on polynomial functions F on Sym is
m
(cid:12)
|     |     |     |     |     | d   |     | (cid:12) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
F(etAΣetA⊤)(cid:12)
|     |     | (ρ(A)F)(Σ) |     | =   |     |     |          | , A ∈ | gl (k). |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | -------- | ----- | ------- | --- | --- |
|     |     |            |     |     | dt  |     | (cid:12) |       | m       |     |     |
(cid:12)
t=0
| With | the preceding | matrix | units, |            | ρ(E )F | = 2{G | (Σ)Σ}       | .   |     |     |     |
| ---- | ------------- | ------ | ------ | ---------- | ------ | ----- | ----------- | --- | --- | --- | --- |
|      |               |        |        |            | ij     |       | F           | ij  |     |     |     |
| A.2  | Probability   |        | and    | asymptotic |        |       | conventions |     |     |     |     |
E
For a probability law Q, , var , cov , corr and pr denote expectation, variance,
|     |     |     | Q   |     | Q   | Q   | Q   | Q   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
covariance, correlation and probability whenever the relevant moments exist. Conditional
26

versions are under the same governing law. For centred Y ,...,Y , the fourth joint cumu-
1 4
lant is
cum (Y ,Y ,Y ,Y ) = E (Y Y Y Y )−cov (Y ,Y )cov (Y ,Y )
Q 1 2 3 4 Q 1 2 3 4 Q 1 2 Q 3 4
−cov (Y ,Y )cov (Y ,Y )−cov (Y ,Y )cov (Y ,Y ).
Q 1 3 Q 2 4 Q 1 4 Q 2 3
For random elements Y ,...,Y , σ(Y ,...,Y ) is the smallest σ-algebra with respect to
1 m 1 m
which all Y are measurable. It is not automatically completed; as usual, conditional
j
expectations are defined up to Q-null sets.
The law N (µ,Ω) is Gaussian with mean µ ∈ Rm and covariance Ω ∈ Sm. For integer
m +
ν ≥ 1, W (ν,Ω) is the law of Pν Z Z⊤ for independent Z ∼ N (0,Ω); χ2 = W (ν,1),
m ℓ=1 ℓ ℓ ℓ m ν 1
andt isStudent’stlawwithν degreesoffreedom. ForGaussiansampling, P = N (0,Σ)
ν Σ d
and P(n) = P⊗n, with
Σ Σ
n
Σ ˆ = n−1X X X⊤, σˆ = e⊤Σ ˆ e .
i i ij i j
i=1
The Gaussian covariance map and the associated first-order variance are
Γ (Σ) = σ σ +σ σ , s2(Σ) = ∇F(Σ)⊤Γ(Σ)∇F(Σ),
(ij),(kl) ik jl il jk F
and s is the nonnegative square root. Under a general law Q for a centred vector X,
F
Γ (Σ) = cov {vech(XX⊤)} whenever the fourth moments exist. In a triangular array
Q Q
with row covariance Σ , the row law is P = P(n), and we abbreviate E = E and
n n Σn n Pn
pr = pr .
n Pn
ˆ ˆ
For an identification strategy (N,D), the plug-in estimator is τˆ = N(Σ)/D(Σ) whenever
ˆ
D(Σ) ̸= 0. Along a deterministic sequence Σ with D(Σ ) ̸= 0, put
n n
N(Σ )
n
τ = , g = ∇N(Σ )−τ ∇D(Σ ),
n n n n n
D(Σ )
n
s = s (Σ ) and s = {g⊤Γ(Σ )g }1/2. Whenever s s > 0,
D,n D n g,n n n n D,n g,n
n1/2D(Σ ) g⊤Γ(Σ )∇D(Σ ) s
µ = n , r = n n n , ω = g,n .
n n n
s s s s
D,n g,n D,n D,n
d
Equality in distribution is =, convergence in probability is −→ , and convergence in
p
distributionis⇝or⇒. Thefunctionsgn(x)isthesignofx ∈ R. Forpositivedeterministic
a , Y = O (a ) means that Y /a is bounded in probability, and Y = o (a ) means
n n p n n n n p n
Y /a −→ 0. Unlessstatedotherwise,allasymptoticstatementsusethecurrentsequence
n n p
of laws and let n → ∞.
A.3 Paper-specific symbols
The remaining notation is summarized in Table A.1. An omitted matrix argument means
evaluation at the current base point Σ.
27

Table A.1: Paper-specific notation used in the Supplementary Material.
|     | Symbol |     |     | Meaning    |     |            |             |         |                   |     |
| --- | ------ | --- | --- | ---------- | --- | ---------- | ----------- | ------- | ----------------- | --- |
|     | Γ, Γ   | Q   |     | Gaussian   |     | covariance | map         | and     | the corresponding |     |
|     |        |     |     | covariance |     | map        | under a     | general | law Q             |     |
|     | s2, s  |     |     | ∇F⊤Γ∇F     |     | and its    | nonnegative |         | square root       |     |
F F
|     | R F    |     |     | Relative   | gradient |        | G F (Σ)Σ/F(Σ) |     | on {F ̸=0}      |     |
| --- | ------ | --- | --- | ---------- | -------- | ------ | ------------- | --- | --------------- | --- |
|     | Σˆ, σˆ |     |     | Known-mean |          | sample | covariance    |     | and its entries |     |
ij
|     |     |     |     | nD(Σˆ)2/s2 |     | (Σˆ) | {s2 (Σˆ)>0} |     |     |     |
| --- | --- | --- | --- | ---------- | --- | ---- | ----------- | --- | --- | --- |
|     | FbD |     |     |            |     | on   |             |     |     |     |
|     |     |     |     |            |     | D    | D           |     |     |     |
(a,b), ν Three-variable face type and primitive polynomial kernel
vector
|          | µ n , r   | n , ω n   |         | Local       | denominator |               | mean,     | numerator–denominator |                |     |
| -------- | --------- | --------- | ------- | ----------- | ----------- | ------------- | --------- | --------------------- | -------------- | --- |
|          |           |           |         | correlation |             | and scale     | ratio     |                       |                |     |
|          | Hat,      | subscript | n,      | Sample      | or          | plug-in       | quantity, | row                   | of a sequence, | and |
|          | subscript | ∗         |         | limiting    | value       |               |           |                       |                |     |
| B Proofs |           | of        | Section |             | 2:          | Preliminaries |           |                       |                |     |
This section proves the facts about exact self-normalization that the main text invokes
without proof. Lemma B.1 identifies the Gaussian first-order variance with the trace form
in (3) and shows that the property is preserved under congruence transformations. Propo-
sition B.1 and Remark B.1 then delimit its distributional scope under elliptical sampling
and unknown means. Lemma B.2 reduces every converse question to one homogeneous
degree, Lemma B.3 establishes interior nonvanishing, and Lemma B.4 shows that neither
the property nor its constant depends on the ambient dimension.
The first lemma converts the statistical definition of s2 into the intrinsic trace form used
D
| throughout | the | paper. |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma B.1 (Trace form and congruence invariance). For every D ∈ R[Sym ] and every
d
| Σ ∈ Sd | ,   |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
++
|     |     |     | ∇D(Σ)⊤Γ(Σ)∇D(Σ) |     |     |     | = 2tr{(G |     | (Σ)Σ)2}. |     |
| --- | --- | --- | --------------- | --- | --- | --- | -------- | --- | -------- | --- |
D
If D is exactly self-normalizing with constant c and A is nonsingular, then D (Σ) =
A
| D(AΣA⊤) | is exactly |     | self-normalizing |     | with | the | same | constant. |     |     |
| ------- | ---------- | --- | ---------------- | --- | ---- | --- | ---- | --------- | --- | --- |
Both sides of the display are polynomial in Σ, which yields the extension to all of Sym
d
recorded after (3). The congruence part makes the property coordinate-free, and it is used
silently whenever a flag or a kernel direction is normalized by a linear change of variables.
Proof of Lemma B.1. Let X ∼ N (0,Σ) and write G = G (Σ). Under the symmetric
|     |     |     |     |     | d   |     |     |     | D   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
perturbation convention, the coordinate gradient of D has entries G on diagonal coor-
ii
| dinates | and 2G | on  | off-diagonal |     | coordinates. |     | Therefore, |     |     |     |
| ------- | ------ | --- | ------------ | --- | ------------ | --- | ---------- | --- | --- | --- |
ij
|     |     | ∇D(Σ)⊤Γ(Σ)∇D(Σ) |     |     |     | = var(X⊤GX) |     |     | = 2tr{(GΣ)2}, |     |
| --- | --- | --------------- | --- | --- | --- | ----------- | --- | --- | ------------- | --- |
by the Gaussian quadratic-form variance formula. If D (Σ) = D(AΣA⊤), the chain rule
A
gives
|     |     |     |     | G   | (Σ) | = A⊤G | (AΣA⊤)A. |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- |
|     |     |     |     |     | DA  |       | D        |     |     |     |
Consequently, G (Σ)Σ is similar to G (AΣA⊤)AΣA⊤, so traces of powers agree. Since
|     |     | DA  |     |     |     | D   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Σ 7→ AΣA⊤ is a bijection of Sym , the identity (4) for D transfers to D with the same
|     |     |     |     |     | d   |     |     |     |     | A   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
constant.
28

We next determine how the sampling law enters. Throughout the following discussion, P
|     |     |     |     | Rd  |     |     |     |     | (X(1),...,X(d))⊤ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
is a probability law on under which the vector X = is centred with
covariance matrix Σ and finite fourth moments, and Γ (Σ) = cov {vech(XX⊤)} is the
|     |     |     |     |     |     |     |     |     | P   | P   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
associated covariance operator. Directly from the definition of the fourth joint cumulant
| in Section |     | A,  |             |     |       |       |      |                        |     |     |     |
| ---------- | --- | --- | ----------- | --- | ----- | ----- | ---- | ---------------------- | --- | --- | --- |
|            |     |     | Γ           | =   | σ σ   | +σ σ  | +cum | (X(i),X(j),X(k),X(l)), |     |     |     |
|            |     |     | P,(ij),(kl) |     | ik jl | il jk |      | P                      |     |     |     |
so the departure of Γ from the Gaussian operator (2) consists exactly of the fourth
P
cumulants. Suppose now that Σ ≻ 0 and that P is elliptical, meaning that X has the
stochastic representation X = RAU, where AA⊤ = Σ, the vector U is uniform on the unit
sphere in Rd, and the radius R ≥ 0 is independent of U. The covariance normalization
E
| forces | (R2) | =   | d. Define | the | kurtosis | parameter |     | κ of | P by |     |     |
| ------ | ---- | --- | --------- | --- | -------- | --------- | --- | ---- | ---- | --- | --- |
P
|     |     |     |     | E   | {(X⊤Σ−1X)2} |     | =   | d(d+2)(1+κ), |     |     | (B.1) |
| --- | --- | --- | --- | --- | ----------- | --- | --- | ------------ | --- | --- | ----- |
P
sothatκ = 0underGaussiansampling,andJensen’sinequalitygives1+κ ≥ d/(d+2) > 0.
| Write | Γ = | Γ and | s2  | (Σ) | = ∇D(Σ)⊤Γ |     | (Σ)∇D(Σ). |     |     |     |     |
| ----- | --- | ----- | --- | --- | --------- | --- | --------- | --- | --- | --- | --- |
|       | κ   | P     | D,κ |     |           |     | κ         |     |     |     |     |
Proposition B.1 (Elliptical fourth moments). Let P be elliptical with covariance matrix
| Σ ≻ | 0 and | kurtosis | parameter |     | κ, and | let | D ∈ R[Sym | ].  | Then |     |     |
| --- | ----- | -------- | --------- | --- | ------ | --- | --------- | --- | ---- | --- | --- |
d
|     |     |     | Γ           |     | = (1+κ)(σ     |     | σ +σ  | σ )+κσ      |     | σ ,   | (B.2) |
| --- | --- | --- | ----------- | --- | ------------- | --- | ----- | ----------- | --- | ----- | ----- |
|     |     |     | κ,(ij),(kl) |     |               |     | ik jl | il jk       |     | ij kl |       |
|     |     |     | s2          |     |               |     |       | Σ)2}+κ{tr(G |     | Σ)}2. |       |
|     |     |     |             | (Σ) | = 2(1+κ)tr{(G |     |       |             |     |       | (B.3) |
|     |     |     |             | D,κ |               |     | D     |             |     | D     |       |
If D is homogeneous of degree K, then D satisfies (4) with constant c if and only if
s2 = c D2 identically, where c = (1+κ)c+κK2, and in that case
| D,κ | κ   |     |     |     | κ      |     |        |      |     |     |       |
| --- | --- | --- | --- | --- | ------ | --- | ------ | ---- | --- | --- | ----- |
|     |     |     |     |     | nD(Σ ˆ | )2  | n nD(Σ | ˆ )2 | n   |     |       |
|     |     |     |     |     |        | =   | ,      |      | =   |     | (B.4) |
|     |     |     |     |     | ˆ      |     |        | ˆ    |     |     |       |
|     |     |     |     |     | s2 (Σ  | )   | c s2   | (Σ ) | c   |     |       |
|     |     |     |     |     | D      |     |        | D,κ  | κ   |     |       |
at every sample covariance matrix at which the displayed denominators are positive.
Both sides of (B.3) are polynomial in Σ, so the proportionality in the proposition is an
identity in the polynomial ring, exactly as in the Gaussian case. The proposition sepa-
rates two conclusions. Ellipticity rescales the proportionality constant of a homogeneous
polynomial but does not change the algebraic class, so the classification developed in the
main text is unaffected. At the same time, only the second ratio in (B.4) carries the
correct fourth-moment scaling when κ governs the sampling law, so samplewise algebraic
constancy is distinct from correct variance calibration, which is the distinction drawn in
| the | main text. |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof of Proposition B.1. All expectations are under P. Since Σ ≻ 0, the matrix A is
E
nonsingular, so X⊤Σ−1X = R2 and (B.1) states that (R4) = d(d + 2)(1 + κ). Put
P
H = A⊤G A, so that tr(H) = tr(G Σ) and tr(H2) = tr{(G Σ)2}. The spherical fourth-
|        | D        |     |     |     |     | D   |     |     |     | D   |     |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| moment | identity |     | is  |     |     |     |     |     |     |     |     |
2tr(H2)+(trH)2
E
|     |     |     |     |     | {(U⊤HU)2} |     | =   |     |     | ,   |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
P
d(d+2)
| and | independence |     | of R  | and | U gives |              |     |            |     |        |     |
| --- | ------------ | --- | ----- | --- | ------- | ------------ | --- | ---------- | --- | ------ | --- |
|     |              | E   | {(X⊤G |     | X)2} =  | (1+κ)[2tr{(G |     | Σ)2}+{tr(G |     | Σ)}2]. |     |
|     |              |     | P     | D   |         |              |     | D          |     | D      |     |
29

Since E (X⊤G X) = tr(G Σ), subtraction of the squared mean proves (B.3), and coef-
P D D
ficient comparison over G yields (B.2).
D
If D is homogeneous of degree K, Euler’s identity gives tr(G Σ) = KD(Σ). Substituting
D
(4) into (B.3) gives s2 = {(1+κ)c+κK2}D2, which is the stated proportionality, and
D,κ
evaluating the two polynomial identities at Σ ˆ gives (B.4). Conversely, if s2 = c D2
D,κ κ
identically, then 1 + κ > 0 permits solving (B.3) for 2tr{(G Σ)2}, and Euler’s identity
D
recovers (4) with constant c.
Remark B.1 (Ellipticalsamplingandunknownmeans). Theproduct-of-chi-squarespivot
in Theorem 1 is generally unavailable under elliptical sampling, because the sample co-
variance matrix is Wishart only when the radial law is Gaussian. Under P(n) with an
Σ
unknown mean, let X ¯ = n−1Pn X and
i=1 i
n
Σ ˜ = (n−1)−1X (X −X ¯ )(X −X ¯ )⊤.
i i
i=1
˜
Then (n−1)Σ ∼ W (n−1,Σ), every exact Gaussian pivot holds with n replaced by n−1,
d
˜
and the standardized denominator of a flag power computed from Σ equals (n−1)/c. For
non-Gaussianellipticalsamplingwithanestimatedmean, thedistinctionin(B.4)persists.
Algebraic constancy survives, correct calibration requires the kurtosis-adjusted operator,
and a Wishart factorization is unavailable in general. In the front-door regressions of the
main text fitted with intercepts, the residual degrees of freedom become n−2 and n−3.
Two structural reductions underlie every converse argument. The first confines every
question about exact self-normalization to a single homogeneous degree, and the second
supplies the interior positivity on which the logarithmic and geodesic arguments rely.
Lemma B.2 (Homogeneous reduction). Every rational strategy for a scale-invariant co-
efficient in a linear structural equation model admits a representative whose numerator
and denominator are homogeneous of the same degree. If a nonhomogeneous polynomial
satisfies exact self-normalization, then its highest- and lowest-degree nonzero homogeneous
parts satisfy the same identity with the same constant.
Lemma B.2 permits all converse arguments to be conducted within one homogeneous
degree, which is the standing convention of Sections 3 and 4 of the main text.
Proof of Lemma B.2. For a linear structural equation model, multiplying every error co-
variance by t > 0 multiplies Σ by t but leaves the scale-invariant causal coefficient under
study unchanged. Expanding N(tΣ) = τD(tΣ) in powers of t shows that each pair of
homogeneous components of the same degree satisfies the identification identity, and at
least one denominator component is nonzero on the model. For the second assertion,
substitute tΣ into (4) and compare the highest and lowest powers of t.
Lemma B.3(Interiornonvanishing). Anonzeropolynomialsatisfyingexactself-normalization
has no zero in Sd . It therefore has a constant sign on that cone.
++
Lemma B.3 makes the logarithm of a self-normalizing polynomial globally available on
the positive cone, which the geodesic arguments of Supplementary Sections C and D use
throughout. Itsfailureattheidentitymatrixisalsowhatrejectstheproximaldenominator
in the factor-and-rank example of the main text.
30

BecauseDisanonzeropolynomialandSd
| Proof | of Lemma | B.3. |     |     |     |     |     |     | isanonemptyEuclidean- |     |
| ----- | -------- | ---- | --- | --- | --- | --- | --- | --- | --------------------- | --- |
++
open set, there is Σ ≻ 0 with D(Σ ) ̸= 0. Let U be the connected component of
|     |     |     | 0   |     |     | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{Σ ≻ 0 : D(Σ) ̸= 0} containing Σ , and define f = log|D| only on U, so that no global
0
nonvanishing conclusion is used at this stage. Equip Sd with the affine-invariant metric
++
|     |     |     |     |     |       | tr(Σ−1H | Σ−1H |     |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | ---- | --- | --- | --- |
|     |     |     |     | g   | (H ,H | ) =     |      | ).  |     |     |
|     |     |     |     | Σ   | 1     | 2       | 1    | 2   |     |     |
Its gradient on U is grad f = Σ(G /D)Σ, and (4) gives ∥grad f∥2 = α with α = c/2.
|     |     |     |     | g   | D   |     |     |     | g g |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Suppose that D(Σ ) = 0 for some Σ ≻ 0. Let γ : [0,1] → Sd be the affine-invariant
|     |     |     | 1   |     |     | 1   |     |     | ++  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
geodesicsegmentfromΣ toΣ ,whichhasfinitelength. Lett = inf{t ∈ (0,1] : D(γ(t)) =
|          |        |     | 0            | 1       |         |     |         |               | ∗   |     |
| -------- | ------ | --- | ------------ | ------- | ------- | --- | ------- | ------------- | --- | --- |
| 0}. Then | γ([0,t | ))  | ⊂ U,         | and for | t < t   | ,   |         |               |     |     |
|          |        | ∗   |              |         |         | ∗   |         |               |     |     |
|          |        |     | |(f ◦γ)′(t)| |         | ≤ ∥grad | f∥  | ∥γ˙(t)∥ | = α1/2∥γ˙(t)∥ | .   |     |
|          |        |     |              |         |         | g   | g g     |               | g   |     |
Integration over the finite-length segment shows that f(γ(t)) is bounded below as t ↑ t .
∗
ContinuityofthepolynomialD andD(γ(t )) = 0insteadimplyf(γ(t)) = log|D(γ(t))| →
∗
−∞, a contradiction. Hence, D has no zero in Sd . Since the cone is connected, its sign
++
is constant.
The final lemma shows that exact self-normalization is a property of the smallest coordi-
| nate block | on  | which | the | polynomial | depends. |     |     |     |     |     |
| ---------- | --- | ----- | --- | ---------- | -------- | --- | --- | --- | --- | --- |
¯ R[Sym
Lemma B.4 (Invariance under ambient extension). Let r ≤ d, let D ∈ ], and
r
|     | R[Sym |     |     |     | ¯   |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
define D ∈ ] by D(Σ) = D (Σ ). Then s2 (Σ) = s2 (Σ ) for every Σ ∈ Sym .
|     |     |     | d   |     |     | 1:r | D   |     | D¯ 1:r | d   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
¯
Consequently, D is exactly self-normalizing on Sym if and only if D is exactly self-
d
| normalizing | on  | Sym | , with | the | same | constant. |     |     |     |     |
| ----------- | --- | --- | ------ | --- | ---- | --------- | --- | --- | --- | --- |
r
Lemma B.4 justifies the dimension reductions invoked in Section 2 of the main text and
in the simulation design. Combined with the congruence invariance of Lemma B.1, it
applies to a polynomial depending on Σ only through its compression to an arbitrary
r-dimensional subspace, because one nonsingular linear change of the observation vector
| moves | that subspace |     | to the | leading | coordinate |     | block. |     |     |     |
| ----- | ------------- | --- | ------ | ------- | ---------- | --- | ------ | --- | --- | --- |
Proof of Lemma B.4. Since ∂D/∂σ = 0 whenever max(i,j) > r, the symmetric gradient
ij
has the block form G (Σ) = diag{G (Σ ),0}. Writing Σ in the corresponding blocks,
|     |     |     | D   |     |     | D¯ 1:r |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
G (Σ)Σ has zero second block row, and the trace of its square equals tr[{G (Σ )Σ }2],
| D   |     |     |     |     |     |     |     |     | D¯ 1:r | 1:r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
which proves the identity. The equivalence follows because Σ ranges over all of Sym
|             |      |     |     |     |     |     |     |     | 1:r | r   |
| ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| as Σ ranges | over | Sym | .   |     |     |     |     |     |     |     |
d
| C   | Proofs | of  | Section |     | 3:  | Flag | powers |     |     |     |
| --- | ------ | --- | ------- | --- | --- | ---- | ------ | --- | --- | --- |
This section proves Theorem 1 and the two-subspace criterion stated after it in Section 3
of the main text. The theorem combines an upper-triangular calculation of the relative
gradient with the Bartlett decomposition of the Wishart matrix. The final lemma shows
thatthenestingconditionisalsonecessaryforaproductoftwocovariance-volumefactors.
Proof of Theorem 1. By congruence invariance of Lemma B.1, it suffices to treat the
coordinate flag, and the constants arising from the chosen basis matrices cancel from the
31

logarithmic gradient. Put A = {1,...,a }. For Σ ≻ 0 every leading block is invertible
|     |     |     | j   |     |     | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and
|     |     |     |     |       |     |         | !     |     |     |
| --- | --- | --- | --- | ----- | --- | ------- | ----- | --- | --- |
|     |     |     | G   | (Σ)Σ  |     | I Σ− 1Σ |       |     |     |
|     |     |     |     | ∆Aj   |     | aj Aj   | Aj,Ac |     |     |
|     |     |     |     |       | =   |         | j .   |     |     |
|     |     |     |     | ∆ (Σ) |     | 0 0     |       |     |     |
Aj
Weighting the jth term by the exponent e and summing over j shows that R (Σ) is
|     |     |     |     |     |     | j   |     |     | D   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
upper triangular with diagonal (m ,...,m ,0,...,0), which proves (i).
|     |     |     |     | 1   |     | a k |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore, the trace of the square of R (Σ) is Pa k m2, so (4) holds with c = 2Pa k m2
|     |     |     |     |     | D   | i=1 | i   |     | i=1 i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
on the cone. Both sides of (4) are polynomial, so the identity extends to all of Sym ,
d
| proving | (ii). |     |     |     |     |     |     |       |     |
| ------- | ----- | --- | --- | --- | --- | --- | --- | ----- | --- |
|         |       |     | LL⊤ |     |     |     | ˆ   | LWL⊤, |     |
For part (iii), write Σ = with L lower triangular and nΣ = where W ∼
W (n,I). Since L is lower triangular, (LWL⊤) = L W L⊤ , so leading determinants
| d   |     |     |     |     |     | 1:r | 1:r 1:r |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
1:r
factorblockwise, andtheBartlettdecomposition(Muirhead,1982, Ch.3)givesdetW =
1:r
Qr B2 with independent B2 ∼ χ2 . Collecting exponents gives (iii).
| i=1 | ii  |     | ii  | n−i+1 |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
ˆ
For part (iv), a flag power is positive at every positive-definite matrix, so D(Σ) > 0 and
| ˆ   | ˆ   |     |     |     |     |     | ˆ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s2 (Σ ) = cD(Σ )2 > 0 almost surely, and evaluating (4) at Σ gives Fb = n/c. The same
| D   |     |     |     |     |     |     |     | D   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
identity gives s (Σ ) = c1/2|D(Σ )| for every n. If n1/2D(Σ ) = O(1), then D(Σ ) → 0,
|         |        | D n   |                 | n   |      |          | n      |     | n   |
| ------- | ------ | ----- | --------------- | --- | ---- | -------- | ------ | --- | --- |
| so s (Σ | ) → 0, | which | is incompatible |     | with | s (Σ ) → | s > 0. |     |     |
| D       | n      |       |                 |     |      | D n      |        |     |     |
The nesting assumption in Theorem 1 cannot be dropped even for a product of two
| covariance-volume |     | factors. |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Rd
Lemma C.1 (Two-subspace criterion). Let V,W ⊆ and let p,q be positive integers.
Then ∆p ∆q is exactly self-normalizing if and only if V ⊆ W or W ⊆ V.
V W
Proof of Lemma C.1. Thelogarithmicrelativegradientsof∆ and∆ aretheΣ-orthogonal
|             |     |         |         |         |            |            | V             | W   |     |
| ----------- | --- | ------- | ------- | ------- | ---------- | ---------- | ------------- | --- | --- |
| projections | PΣ  | and PΣ  | onto    | the two | subspaces. | Therefore, |               |     |     |
|             | V   |         | W       |         |            |            |               |     |     |
|             |     | tr{(pPΣ | +qPΣ)2} | =       | p2dimV     | +q2dimW    | +2pqtr(PΣPΣ). |     |     |
|             |     |         | V W     |         |            |            |               | V W |     |
Thefinaltraceisthesumofthesquaredcosinesoftheprincipalanglesintheinnerproduct
x⊤Σy. Under either containment, it equals the dimension of the smaller subspace and is
constant.
Suppose that neither containment holds. Write S = V ∩W, V = S⊕V′, and W = S⊕W′,
where V′ and W′ are nonzero. The sum S⊕V′⊕W′ is direct. Choose a positive-definite
inner product that makes these three subspaces mutually orthogonal. The final trace then
equals dimS. Perturb the inner product so that one nonzero vector in V′ has nonzero
inner product with one in W′, while retaining positive definiteness. At least one squared
principal-angle cosine becomes positive, so the trace changes. Exact self-normalization is
| therefore | impossible. |     |         |     |             |     |         |             |     |
| --------- | ----------- | --- | ------- | --- | ----------- | --- | ------- | ----------- | --- |
| D         | Proofs      | of  | Section |     | 4: Converse |     | results | and diagno- |     |
sis
| D.1 | Overview |     | and algebraic |     |     | preliminaries |     |     |     |
| --- | -------- | --- | ------------- | --- | --- | ------------- | --- | --- | --- |
This subsection proves the converse and diagnostic results in Section 4 of the main text.
The argument first reduces the problem to boundary faces and determinant-free residues.
32

It then proves the complete converse in dimension two and the three-variable reduction.
The remaining subsections study the mixed branch, the conditional higher-dimensional
| converse, | and the low-degree-factor |     | diagnostic. |     |     |     |     |
| --------- | ------------------------- | --- | ----------- | --- | --- | --- | --- |
The first two lemmas provide the divisibility tools used throughout the section.
Lemma D.1 (Irreducibility of the generic symmetric determinant). For every r ≥ 1, the
determinant of the generic symmetric matrix of order r is irreducible over R and over C.
R[Sym
Consequently, each leading principal minor ∆ = det(Σ ) is irreducible in ] for
|     |     |     |     | r   | 1:r |     | d   |
| --- | --- | --- | --- | --- | --- | --- | --- |
d ≥ r.
Irreducible elements are prime in the unique factorization domain R[Sym ]. Therefore,
d
Lemma D.1 justifies the determinant-divisibility and valuation arguments below.
R
Proof of Lemma D.1. We argue over a field k of characteristic zero, which covers k =
and k = C. The assertion is immediate for r = 1. Suppose it holds for r −1, and write
| the generic | symmetric | matrix as |     |     |     |     |     |
| ----------- | --------- | --------- | --- | --- | --- | --- | --- |
|             |           |           |     |   ! |     |     |     |
A y
|     |     |     | X = | ,    |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     | r   | y⊤ z |     |     |     |
where A is generic symmetric of order r−1. Expansion in z gives
|     |     | detX | = (detA)z | −y⊤adj(A)y. |     |     |     |
| --- | --- | ---- | --------- | ----------- | --- | --- | --- |
r
LetR = k[A,y], whichisauniquefactorizationdomain. Byinduction, detAisirreducible
inR. IfdetAdividedy⊤adj(A)y,itwoulddivideeverycoefficientofthispolynomialinthe
coordinates of y. In particular, it would divide the coefficient of y2 , which is a nonzero
r−1
principal minor of A of order r − 2 and has smaller degree. Thus, the two coefficients
of the displayed polynomial in z are coprime. The polynomial is primitive in R[z] and
irreducible over the fraction field of R. Gauss’ lemma gives irreducibility in R[z]. Passing
to a larger polynomial ring preserves irreducibility, which proves the final assertion.
The next lemma converts vanishing on a real part of the determinant boundary into
polynomial divisibility. This step is needed when two candidate solutions agree only on
| rank-deficient | covariance | matrices. |     |     |     |     |     |
| -------------- | ---------- | --------- | --- | --- | --- | --- | --- |
Lemma D.2 (Real determinant divisibility). If a polynomial F on Sym vanishes on a
d
nonempty Euclidean-open subset of the real symmetric matrices of rank d−1, then detΣ
divides F.
Proof of Lemma D.2. After a simultaneous permutation of rows and columns, work in a
chart in which the leading principal minor ∆ of order d−1 is nonzero at one point of the
given open set. Shrink the set so that ∆ ̸= 0 throughout it. The determinant is linear in
| σ , and | can be written | as  |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- |
dd
|     |     |     | δ := detΣ | = ∆σ +B, |     |     |     |
| --- | --- | --- | --------- | -------- | --- | --- | --- |
dd
where B does not involve σ . If N = deg F, pseudo-division in σ gives
|     |     | dd  | σ   |     |     | dd  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
dd
|     |     | ∆NF | = Qδ +R, | deg | R = 0. |     |     |
| --- | --- | --- | -------- | --- | ------ | --- | --- |
σ dd
On this chart, the equation δ = 0 is the graph σ = −B/∆. The projection of the given
dd
Euclidean-opensubsetofthisgraphtotheremainingcoordinatesisEuclideanopen. Since
33

∆NF.
R does not involve σ and vanishes on that projection, R ≡ 0. Thus, δ divides By
dd
R[Sym
Lemma D.1, δ is prime in ]. It does not divide ∆, because ∆ does not involve σ
d dd
| whereas | δ   | does. Hence, |     | δ divides | F.  |     |     |     |     |     |
| ------- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
The face-restriction principle transfers exact self-normalization to every nonzero covari-
ance face. Together with Theorem 2, it determines the form of each nonzero plane re-
| striction | in  | dimension |     | three. |     |     |     |     |     |     |
| --------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
Lemma D.3 (Face restriction). If D satisfies (4) on Sym and its restriction D to a
d V
S
face (V) is not identically zero, then D satisfies (4) with the same constant.
|     | +   |     |     |     |     | V   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof of Lemma D.3. ByLemmaB.1,acongruencereducestheargumenttoV = span(e ,...,e ).
1 r
Evaluate (4) at diag(S,0) for S ∈ Sym . In the corresponding block partition of the gra-
r
dient,
|     |     |     |     |     |     |     |     | !   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | G S | 0   |     |     |
11
|     |     |     |     |     | G diag(S,0) | =   |     | ,   |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | D           |     | G⊤S | 0   |     |     |
12
and the trace of its square is tr{(G S)2}. The block G , evaluated at diag(S,0), is the
|     |     |     |     |     | 11  |     |     | 11  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
symmetric gradient of D at S. This proves the identity for D .
|     |     |     |     | V   |     |     |     |     | V   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The stripping lemma removes one full determinant factor and records the resulting change
in the self-normalization constant. It is the degree-lowering step in the dimension-two
| proof | and | in the | three-variable |     | reduction. |     |     |     |     |     |
| ----- | --- | ------ | -------------- | --- | ---------- | --- | --- | --- | --- | --- |
Lemma D.4 (Determinant stripping). If D = (detΣ)E and E is homogeneous, then D
is exactly self-normalizing if and only if E is. Their constants satisfy
|     |     |     |     |     | c = c | +2d+4degE. |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     | D E   |            |     |     |     |     |
Proof of Lemma D.4. On the positive cone, write L = G /D and L = G /E. The
|         |       |       |     |         |                 |      | D         | D   |        | E E   |
| ------- | ----- | ----- | --- | ------- | --------------- | ---- | --------- | --- | ------ | ----- |
| product | rule  | gives | L   | = Σ−1   | +L . Therefore, |      |           |     |        |       |
|         |       |       | D   |         | E               |      |           |     |        |       |
|         |       | Σ)2}  |     |         |                 | Σ)2} |           |     |        | Σ)2}. |
|         | tr{(L |       | =   | d+2tr(L | Σ)+tr{(L        |      | = d+2degE |     | +tr{(L |       |
|         |       | D     |     |         | E               | E    |           |     |        | E     |
Exactself-normalizationisequivalentontheconetoconstancyofthefinaltrace. Hence, it
holds for D if and only if it holds for E. The displayed identity gives c /2 = d+2degE+
D
c /2. Both self-normalization identities then extend polynomially to all of Sym .
| E   |          |     |     |          |              |     |     |     |     | d   |
| --- | -------- | --- | --- | -------- | ------------ | --- | --- | --- | --- | --- |
| D.2 | Complete |     |     | converse | in dimension |     | two |     |     |     |
The proof separates solutions according to whether the determinant of the symmetric
gradient vanishes identically. A nonzero determinant coefficient produces a removable
determinant factor. The zero coefficient leads to a rank-one gradient and then to a power
| of one | variance | direction. |     |     |     |     |     |     |     |     |
| ------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof of Theorem 2. Let K = degD and let µ ,µ be the eigenvalues of G (Σ)Σ. On
|     |     |     |     |     |     | 1   | 2   |     |     | D   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the positive cone they are real because this matrix is similar to Σ1/2G (Σ)Σ1/2. Euler’s
D
| identity | and | (4) give |     |     |          |        |     |          |     |     |
| -------- | --- | -------- | --- | --- | -------- | ------ | --- | -------- | --- | --- |
|          |     |          |     | µ   | +µ = KD, | µ2 +µ2 | =   | (c/2)D2. |     |     |
|          |     |          |     | 1   | 2        | 1      | 2   |          |     |     |
34

| Hence, | as a | polynomial |     | identity, |     |     |     |     |     |
| ------ | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
1
|     |     |     |      |         |     | qD(Σ)2, |     | (K2    |     |
| --- | --- | --- | ---- | ------- | --- | ------- | --- | ------ | --- |
|     |     |     | detG | (Σ)detΣ |     | =       | q = | −c/2). |     |
|     |     |     |      | D       |     |         |     | 2      |     |
If q ̸= 0, Lemma D.1 gives detΣ | D. Lemma D.4 removes this factor, and induction on
K applies.
Suppose that q = 0. Then detG ≡ 0. The polynomial gradient map takes values in
D
∼ R3.
the rank-one quadric cone in Sym = At every nonzero smooth image point, the
2
differential of the gradient, which is the Hessian of D, maps into the two-dimensional
tangent plane. Thus, detHessD ≡ 0. The Gordan–Noether theorem for forms in at
most four variables implies over C that D is a cone. The reduction may be taken over
R. A complex constant direction annihilating D brings its conjugate with it. If the two
directions are proportional, rescaling gives a real direction. If they are independent, D
depends on one linear form, which reality makes real up to a scalar. Thus, after a real
| linear | change, | D   | = P(ℓ | ,ℓ ). |     |     |     |     |     |
| ------ | ------- | --- | ----- | ----- | --- | --- | --- | --- | --- |
1 2
Write G = P A + P A for fixed independent matrices A ,A ∈ Sym . The binary
|     | D   | 1   | 1   | 2 2 |     |     |     | 1 2 | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
quadratic Q(x,y) = det(xA +yA ) is nonzero because the determinant cone contains no
|     |     |     |     | 1   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two-dimensional linear subspace. The identity Q(P ,P ) = 0 either forces P = P = 0
|     |     |     |     |     |     |     | 1   | 2   | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
when Q is definite, or forces one real linear factor of Q to vanish identically. Thus, P
| depends | on  | one linear | form | and |     |           |        |     |     |
| ------- | --- | ---------- | ---- | --- | --- | --------- | ------ | --- | --- |
|         |     |            |      |     | D = | γtr(AΣ)K, | detA = | 0.  |     |
A nonzero real symmetric rank-one matrix A is a nonzero scalar multiple of vv⊤. This
| gives | the form | in  | (8). The | value | of  | c follows from | Theorem | 1.  |     |
| ----- | -------- | --- | -------- | ----- | --- | -------------- | ------- | --- | --- |
The two branches of the proof correspond exactly to the determinant factor and the rank-
one variance factor in Theorem 2. No other irreducible factor can occur in dimension
two.
| D.3 | Adjugate |     | duality |     | and | three-variable |     | face types |     |
| --- | -------- | --- | ------- | --- | --- | -------------- | --- | ---------- | --- |
We next turn to determinant-free solutions on Sym . Adjugate duality exchanges rank-
3
one and rank-two boundary data. The face-type lemma then shows that every nonzero
| plane | restriction |     | has one | common |     | pair of multiplicities. |     |     |     |
| ----- | ----------- | --- | ------- | ------ | --- | ----------------------- | --- | --- | --- |
Lemma D.5 (Adjugate duality). If D is homogeneous of degree K and satisfies (4) on
D†
Sym with constant c, then = D◦adj is homogeneous of degree (d−1)K and satisfies
d
(4) with
|           |     |         |                |     |     | c† = c+2(d−2)K2. |     |     |     |
| --------- | --- | ------- | -------------- | --- | --- | ---------------- | --- | --- | --- |
| Moreover, |     | (D†)† = | (detΣ)(d−2)KD. |     |     |                  |     |     |     |
Proof of Lemma D.5. On the positive cone, adjΣ = (detΣ)Σ−1, so
|      |     |                     |     | log|D†(Σ)| |        | = KlogdetΣ+log|D(Σ−1)|. |        |     |     |
| ---- | --- | ------------------- | --- | ---------- | ------ | ----------------------- | ------ | --- | --- |
| If L | = G | /D, differentiation |     |            | gives  |                         |        |     |     |
| D    | D   |                     |     |            |        |                         |        |     |     |
|      |     |                     |     |            | L (Σ)Σ | = KI −Σ−1L              | (Σ−1). |     |     |
|      |     |                     |     |            | D†     |                         | D      |     |     |
35

Σ−1.
The second term is similar to the relative gradient of D at If its eigenvalues are
|     |     |     |     | P   |     | P λ2 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
λ ,...,λ , Euler’s identity and (4) give λ = K and = c/2. Hence,
| 1   | d   |     |       | i i          |     | i i   |     |
| --- | --- | --- | ----- | ------------ | --- | ----- | --- |
|     |     |     |       | Σ)2} (d−2)K2 |     |       |     |
|     |     |     | tr{(L | =            |     | +c/2. |     |
D†
Clearing denominators proves the polynomial identity for D†. The involution formula
| follows | from adj(adjΣ) | =   | (detΣ)d−2Σ. |     |     |     |     |
| ------- | -------------- | --- | ----------- | --- | --- | --- | --- |
For the next lemma, write K = degD. The result makes the face type in Definition 3
well defined and gives the bounds used in the three-variable reduction.
Lemma D.6 (Face type in dimension three). Let D be determinant-free, homogeneous
and exactly self-normalizing on Sym . At least one D-good plane exists, and every D-good
3
K2 2K2,
restriction has the form (9) with one common pair (a,b). Moreover, ≤ c ≤ with
| c = 2K2 | if and only | if b | = 0. |     |     |     |     |
| ------- | ----------- | ---- | ---- | --- | --- | --- | --- |
Proof of Lemma D.6. If every plane restriction vanished, D would vanish on every sin-
gular positive-semidefinite matrix. Lemma D.2 would then give δ | D, contrary to
determinant-freeness. A D-good face restriction satisfies (4) by Lemma D.3. Theorem 2
gives its form. Substituting a = K − 2b into the equation for the self-normalization
| constant | gives |     |              |       |     |      |     |
| -------- | ----- | --- | ------------ | ----- | --- | ---- | --- |
|          |       |     | 2b2 −2Kb+(K2 | −c/2) |     | = 0. |     |
Its two roots b and b satisfy b + b = K. Admissibility requires 0 ≤ b ≤ K/2. If
|     | +   | −   | +   | −   |     |     | ±   |
| --- | --- | --- | --- | --- | --- | --- | --- |
both roots were admissible, their sum could equal K only when b = b = K/2. Hence,
+ −
there is at most one admissible root, and the face type is common to all good planes. The
| bounds | on c follow | from | the same | two equations. |     |     |     |
| ------ | ----------- | ---- | -------- | -------------- | --- | --- | --- |
Theadjugatemapsarank-twocovariancefacetotherank-onecone. Thefollowingformula
| makes | that action explicit. |     |     |     |     |     |     |
| ----- | --------------------- | --- | --- | --- | --- | --- | --- |
Lemma D.7 (Boundary strata under the adjugate). If P ∈ R3×2 and m(P) is the cross
| product | of its columns, | then, | for every | S ∈ Sym | ,   |     |     |
| ------- | --------------- | ----- | --------- | ------- | --- | --- | --- |
2
|     |     |     | adj(PSP⊤) | = (detS)m(P)m(P)⊤. |     |     |     |
| --- | --- | --- | --------- | ------------------ | --- | --- | --- |
PSP⊤
Proof of Lemma D.7. The (i,j) cofactor of is the product of the corresponding
2×2 row minors of P and detS. Those signed minors are the coordinates of m(P).
The next dichotomy separates solutions that survive on the rank-one cone from those
that vanish there. The surviving branch must have the largest possible self-normalization
| constant | and a pure | rank-one | face | type. |     |     |     |
| -------- | ---------- | -------- | ---- | ----- | --- | --- | --- |
Lemma D.8 (Rank-one dichotomy). Let D be homogeneous of degree K and exactly self-
normalizing on Sym . Either p ≡ 0, or D is determinant-free, c = 2K2, and its face
|     |     | 3   | D   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
type is (K,0).
∤
Proof of Lemma D.8. If p ̸≡ 0, then δ D. For a plane represented by P, Lemma D.7
D
gives
|     |     |     | (D†) (S) | = (detS)Kp | {m(P)}. |     |     |
| --- | --- | --- | -------- | ---------- | ------- | --- | --- |
|     |     |     | V        |            | D       |     |     |
36

On every plane for which p {m(P)} ̸= 0, this is a pure determinant power of type (0,K).
D
|              |           | c†/2   | 2K2.   |     |           |       | c†/2 K2+c/2, |           | 2K2. |
| ------------ | --------- | ------ | ------ | --- | --------- | ----- | ------------ | --------- | ---- |
| Its constant | satisfies |        | =      |     | Lemma D.5 | gives | =            | and hence | c =  |
| Lemma        | D.6 then  | forces | b = 0. |     |           |       |              |           |      |
The dichotomy leaves a rigidity question on the rank-one cone. The next proposition
closes that branch and shows that it contains only powers of one variance direction.
Proposition D.1 (Rank-one rigidity). Let D be homogeneous of degree K and exactly
self-normalizing on Sym . If p ̸≡ 0, then D = γ(v⊤Σv)K for a nonzero constant γ and
|     |     |     | 3   | D   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
R3.
| a nonzero | vector | v ∈ |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Proof of Proposition D.1. By Lemma D.8, every D-good plane restriction is a Kth power
of one linear covariance form. Thus, on a Zariski-open family of projective lines in P2,
C
the form p restricts to a polynomial whose zero set has one support point. If the
D
reduced projective curve {p = 0} had degree at least two, a general line would meet
|     |     |     | D   |     | red |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
it transversally in at least two points by Bezout’s theorem (Harris, 1992). Hence, the
| reduced | curve is | one line | and |     |     |     |     |     |     |
| ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
γ(v⊤u)2K
|     |     |     |     |     | p (u) = |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
D
| with v | and γ real | after | rescaling. |     |     |     |     |     |     |
| ------ | ---------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
Let D = γ(v⊤Σv)K. On every D-good plane, both face restrictions are Kth powers of
0
linear covariance forms and agree on all rank-one matrices in that face. Unique factoriza-
tion of the resulting binary powers makes the linear forms proportional with the matching
constant. Hence, the two face polynomials agree identically. Therefore, D and D agree
0
on a nonempty open set of rank-two matrices, and Lemma D.2 gives δ | D−D .
0
If the difference is nonzero, write D = D +δjR with j ≥ 1, δ ∤ R, and degR = K −3j.
0
After a congruence, take v = e and put Q = σ . Expanding (4) and dividing by δj gives
|                  |                   |     |     | 1   |          | 11   |           |     |       |
| ---------------- | ----------------- | --- | --- | --- | -------- | ---- | --------- | --- | ----- |
|                  |                   |     | (Σe | )⊤G | (Σ)(Σe ) | = (K | −j)QR+δjS |     | (D.1) |
|                  |                   |     | 1   | R   | 1        |      |           |     |       |
| for a polynomial |                   | S.  |     |     |          |      |           |     |       |
| Use the          | Schur coordinates |     |     |     |          |      |           |     |       |
|                  |                   |     |     |     |          | qu⊤  | !         |     |       |
q
|     |     |     | Σ(q,u,C) | =   |     |     | , δ = qdetC. |     |     |
| --- | --- | --- | -------- | --- | --- | --- | ------------ | --- | --- |
+quu⊤
|     |     |     |     |     | qu C |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
The line Σ+t(Σe )(Σe )⊤ changes only q to q+tq2. Therefore, the left-hand side of (D.1)
|     |     | 1   | 1   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
¯
| is q2∂ | R . On detC | =   | 0,  |     |     |     |     |     |     |
| ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
q
|     |     |     |     |     | ¯       |          | ¯   |     |     |
| --- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- |
|     |     |     |     |     | q2∂ R = | (K −j)qR | .   |     |     |
q
¯
The polynomial R has q-degree at most K −3j < K −j. Coefficient comparison forces
¯
R = 0 on detC = 0. Thus, R vanishes on a nonempty open set of rank-two matrices and
| is divisible | by δ, | which | contradicts |     | its definition. |     |     |     |     |
| ------------ | ----- | ----- | ----------- | --- | --------------- | --- | --- | --- | --- |
PropositionD.1provesTheorem3(i)afterdeterminantstripping. Theremainingdeterminant-
| free solutions | vanish | on  | the rank-one |     | cone. |     |     |     |     |
| -------------- | ------ | --- | ------------ | --- | ----- | --- | --- | --- | --- |
37

| D.4 | Relative |     | spectral |     | constancy |     | in  | dimension | three |     |     |
| --- | -------- | --- | -------- | --- | --------- | --- | --- | --------- | ----- | --- | --- |
Euler’s identity fixes the trace of the relative gradient, while exact self-normalization fixes
its squared Frobenius norm. The next proposition uses the polynomial character of D to
obtain the additional discrete constraint that makes the spectrum constant in dimension
three.
Proposition D.2 (Spectral constancy). Let D be homogeneous of degree K and exactly
self-normalizing on Sym , and put α = c/2. There is a fixed multiset {λ ,λ ,λ } such
|     |     |     |     | 3   |     |     |     |     |     | 1 2 | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that
|          |       |     |     | specR | (Σ) | = {λ | ,λ ,λ | } (Σ ≻ 0). |     |     |     |
| -------- | ----- | --- | --- | ----- | --- | ---- | ----- | ---------- | --- | --- | --- |
|          |       |     |     |       | D   |      | 1 2   | 3          |     |     |     |
| In every | case, |     |     |       |     |      |       |            |     |     |     |
D(Σ)3.
|        |       |      |       | detG  | (Σ)detΣ       |     | = λ | λ λ |     |     |     |
| ------ | ----- | ---- | ----- | ----- | ------------- | --- | --- | --- | --- | --- | --- |
|        |       |      |       |       | D             |     | 1   | 2 3 |     |     |     |
| If α = | K2/3, | then | 3 | K | and D | = γ(detΣ)K/3. |     |     |     |     |     |     |
S3
Proof of Proposition D.2. By Lemma B.3, D has constant sign on . Multiply it by
++
| −1 if necessary |     | so  | that D | > 0 | there. | Fix Σ | ≻ 0 | and define |     |     |     |
| --------------- | --- | --- | ------ | --- | ------ | ----- | --- | ---------- | --- | --- | --- |
0
|     |     |     |     |     | ˜     | D(Σ1/2XΣ1/2). |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | ------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | D (X) | =             |     |     |     |     |     |
|     |     |     |     |     |       |               | 0   | 0   |     |     |     |
˜
By Lemma B.1, D satisfies (4) with the same constant. At I, put
|     |     |     |     |     |      |     | Σ1/2G | )Σ1/2   |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ----- | ------- | --- | --- | --- |
|     |     |     |     |     | G D˜ | (I) |       | (Σ      |     |     |     |
|     |     |     |     | B   | =    | =   | 0     | D 0 0 . |     |     |     |
˜
|     |     |     |     |     | D (I) |     | D(Σ | )   |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
0
The matrix B is symmetric and is similar to R (Σ ). In particular, trB = K and
D 0
| trB2 = | α.  |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
By Cauchy–Schwarz, α ≥ K2/3. If α = K2/3, equality forces all three eigenvalues of
R (Σ )toequalK/3. SinceΣ wasarbitraryandR (Σ )isdiagonalizable, R = (K/3)I
| D 0 |     |     |     |     | 0   |     |     | D 0 |     | D   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
throughout the cone. Hence, dlog|D| = (K/3)dlogdetΣ. On a nonempty open set
this gives D3 = γ (detΣ)K. Polynomial continuation and unique factorization using
0
Lemma D.1 yield 3 | K and D = γ(detΣ)K/3. The determinant identity follows with
K2/3.
| λ = λ | = λ | = K/3. | Henceforth, |     | assume | α   | >   |     |     |     |     |
| ----- | --- | ------ | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
| 1 2   | 3   |        |             |     |        |     |     |     |     |     |     |
˜
Let f = logD and equip S3 with the affine-invariant metric. Equation (4) gives
++
∥grad f∥2 = α. For every vector field Y, symmetry of the Riemannian Hessian gives
| g   | g   |      |      |      |        |        |     |      |     |     |     |
| --- | --- | ---- | ---- | ---- | ------ | ------ | --- | ---- | --- | --- | --- |
|     |     | g(∇g | grad | f,Y) | = Hess | f(grad |     | f,Y) |     |     |     |
g
|     |     | grad | g f | g   |     |     |     | g   |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
f∥2
|     |     |     |     |     | = Hess | f(Y,grad |     | f) = Y∥grad |     | = 0. |     |
| --- | --- | --- | --- | --- | ------ | -------- | --- | ----------- | --- | ---- | --- |
|     |     |     |     |     |        | g        |     | g 2         | g   | g    |     |
Thus, the integral curves of grad f are geodesics. The geodesic through I with initial
g
velocity B is t 7→ etB. Uniqueness of geodesics and integral curves makes the two curves
| agree near | t   | = 0. Along |     | that interval, |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
d
|     |     |     |     |     | f(etB) |         |     | f∥2  |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------- | --- | ---- | --- | --- | --- |
|     |     |     |     |     |        | = ∥grad |     | = α. |     |     |     |
|     |     |     |     |     | dt     |         | g   | g    |     |     |     |
Therefore,
|     |     |     |     |     | D ˜ | (etB) = | D ˜ (I)eαt. |     |     |     | (D.2) |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- | ----- |
38

R.
| Both sides | are | entire | functions | of t, | so (D.2) | holds | for every | t ∈ |
| ---------- | --- | ------ | --------- | ----- | -------- | ----- | --------- | --- |
Choose an orthogonal matrix O such that B = Odiag(λ ,λ ,λ )O⊤. Define
|     |     |     |     |     |     |     | 1   | 2 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
X
|     | Q(x | ,x  | ,x ) = | D ˜ {Odiag(x |     | ,x ,x )O⊤} | =   | a xn1xn2xn3. |
| --- | --- | --- | ------ | ------------ | --- | ---------- | --- | ------------ |
|     |     | 1   | 2 3    |              |     | 1 2 3      |     | n 1 2 3      |
n∈Z3
≥0
|n|=K
Since Q(1,1,1) = D(I) ˜ ̸= 0, at least one coefficient group is nonzero. Substitution in
(D.2) gives
X
|     |     |     |     |     | a e(n·λ)t | = D ˜ (I)eαt. |     |     |
| --- | --- | --- | --- | --- | --------- | ------------- | --- | --- |
n
|n|=K
Z3
Linear independence of real exponentials implies n·λ = α for at least one n ∈ with
≥0
|n| = K.
The equations P λ = K and P λ2 = α define a circle in the trace plane. If n is
|     |     | i   | i   |     | i i |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
proportional to (1,1,1), then n = (K/3)(1,1,1) and n · λ = K2/3 ̸= α. Thus, this
exceptional resonance contains no admissible point. For every other n, the equation
n·λ = α cuts the trace plane in a proper affine line and meets the circle in at most two
points. There are only finitely many such n. Hence, the ordered spectrum belongs to a
finite set. The ordered eigenvalues vary continuously with Σ because R (Σ) is similar to
D
| the symmetric |     | matrix |     |     |       |         |     |     |
| ------------- | --- | ------ | --- | --- | ----- | ------- | --- | --- |
|               |     |        |     |     | Σ1/2G | (Σ)Σ1/2 |     |     |
D
.
D(Σ)
Since S3 is connected, the ordered spectrum is constant. Taking the product of the fixed
++
eigenvalues and clearing denominators gives the determinant identity.
For a determinant-free solution, the determinant identity forces one relative eigenvalue to
| vanish. | The face | type | determines | the | other | two. |     |     |
| ------- | -------- | ---- | ---------- | --- | ----- | ---- | --- | --- |
∤
Corollary D.1. If δ D, then one relative eigenvalue is zero and detG ≡ 0. If D has
D
| face type | (a,b), | then |       |     |     |           |     |       |
| --------- | ------ | ---- | ----- | --- | --- | --------- | --- | ----- |
|           |        |      | specR | (Σ) | =   | {a+b,b,0} | (Σ  | ≻ 0). |
D
Proof of Corollary D.1. The left-hand side of the determinant identity in Proposition D.2
is divisible by the prime δ. If the eigenvalue product were nonzero, then δ | D3, contrary
to the hypothesis. The remaining two eigenvalues have sum K = a + 2b and product
| b(a+b). | They | are therefore |     | a+b | and b. |     |     |     |
| ------- | ---- | ------------- | --- | --- | ------ | --- | --- | --- |
Spectralconstancysuppliesthesingular-gradientstructureofeverydeterminant-freethree-
variable solution. It is the step that reduces the unresolved case to a polynomial kernel
line.
| D.5 | Pure | plane-minor |     | and | mixed | branches |     |     |
| --- | ---- | ----------- | --- | --- | ----- | -------- | --- | --- |
Wefirstidentifythebranchwhosenonzeroplanerestrictionsarepuredeterminantpowers.
| This proves | Theorem |     | 3 (ii). |     |     |     |     |     |
| ----------- | ------- | --- | ------- | --- | --- | --- | --- | --- |
Proof of the pure plane-minor branch in Theorem 3. Suppose that the face type is (0,b),
so K = 2b and the spectrum is (b,b,0). The adjugate transform has spectrum (b,b,2b).
39

Since p ≡ 0, the polynomial D† vanishes on every singular positive-semidefinite matrix.
D
Lemma D.2 gives δ | D†. Write D† = δsE with exact s ≥ 1. The adjugate involution gives
2s ≤ K, and determinant stripping shifts every relative eigenvalue down by s. Hence,
specR = {b−s,b−s,2b−s}.
E
Because δ ∤ E, Corollary D.1 forces a zero eigenvalue. The bound s ≤ b leaves only
s = b. Thus, degE = b and specR = (b,0,0). The pair (b,0) satisfies the equations
E
that determine the face type of E. Lemma D.6 therefore gives face type (b,0). A nonzero
restrictionofthistypeisnonzeroatasuitablerank-onematrix,sop ̸≡ 0. PropositionD.1
E
gives E = γ(u⊤Σu)b. Applying the adjugate again yields D = γ′∆b .
u⊥
Mixed face types are paired by adjugate duality. This symmetry is used in both the kernel
analysis and the boundary-rigidity argument.
Lemma D.9 (Mixed duality). If D is determinant-free of mixed type (a,b), then E =
D†/δb is determinant-free of type (b,a) and E† = δaD.
Proof of Lemma D.9. ThespectrumofD is(a+b,b,0), sothatofD† is(a+2b,a+b,b). As
in the pure branch, δ | D†. Let s be its exact multiplicity. After stripping, the spectrum is
(a+2b−s,a+b−s,b−s). The adjugate involution gives 2s ≤ K = a+2b. Corollary D.1
requires a zero eigenvalue, so s ∈ {b,a+b,a+2b}. Since a ≥ 1, a+b > (a+2b)/2 = K/2.
The involution bound therefore excludes s = a + b and s = a + 2b. Hence, s = b. The
stripped spectrum is (a + b,a,0) and the degree is 2a + b. The pair (b,a) satisfies the
two equations that determine the face type. Lemma D.6 gives the stated type, and the
involution identity gives the final formula.
The next algebraic lemma turns a rank-one factorization over the fraction field into a
polynomial factorization. It is applied to the adjugate of the singular symmetric gradient.
Lemma D.10 (Primitive rank-one factorization over a UFD). Let R be a unique factor-
ization domain and let U ∈ R3×3 be a nonzero matrix whose 2×2 minors all vanish. Then
U = vr⊤ for vectors v,r ∈ R3, where v is primitive. If U is symmetric, then U = ψvv⊤
for some ψ ∈ R. If the entries of U are homogeneous of one common degree, the factors
may be chosen homogeneous.
Proof of Lemma D.10. ChooseanonzerocolumnU . Letg beagreatestcommondivisor
·j0
of its entries and put v = U /g. Then v is primitive. Since all 2×2 minors vanish, every
·j0
other column is proportional to v over K = Frac(R). For each j, there is r ∈ K such
j
that U = r v. Write r = p/q in lowest terms. The identity qU = pv holds for every
·j j j ij i
i. If an irreducible element divided q, it would divide every v , contrary to primitivity.
i
Hence, q is a unit and r ∈ R. Thus, U = vr⊤ with r ∈ R3.
j
If U is symmetric, then vr⊤ = rv⊤. Hence, r = ψv for some ψ ∈ K. The same denomi-
nator argument shows that ψ ∈ R. When the entries of U are homogeneous, the greatest
common divisor may be chosen homogeneous. Degree comparison then makes v, r, and
ψ homogeneous.
For a mixed solution, the adjugate of the symmetric gradient has rank one. The factoriza-
tion lemma therefore produces the polynomial kernel vector in Theorem 3. It also shows
why a vanishing-Hessian argument arises naturally.
40

Proof of the kernel-field assertion in Theorem 3. For a mixed type, G has rank two on
D
the positive cone and detG ≡ 0. The identity adj(adjG ) = (detG )G = 0 shows
|     |     |     |     |     | D   |     |     |     | D   | D D |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that every 2 × 2 minor of adjG vanishes. The matrix adjG is not identically zero
|     |     |     |     |     | D   |     |     |     | D   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
because G has rank two on a nonempty open set. Apply Lemma D.10 in R = R[Sym ].
D
3
Since adjG is symmetric and homogeneous, there are a primitive homogeneous vector
D
| ν   | and a | nonzero | homogeneous |     | polynomial |      | ψ such  | that |     |     |     |
| --- | ----- | ------- | ----------- | --- | ---------- | ---- | ------- | ---- | --- | --- | --- |
|     |       |         |             |     |            | adjG | = ψνν⊤. |      |     |     |     |
D
The identity G adjG = 0 gives ψ(G ν)ν⊤ = 0. Choose an index j for which ν ̸≡ 0.
|     |     |     | D   | D   |     | D   |     |     |     |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Since R is an integral domain, every component of G ν vanishes. Hence, G ν ≡ 0.
|     |     |     |     |     |     |     |     | D   |     | D   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Differentiate this identity in a symmetric direction H and left multiply by ν⊤. This gives
ν⊤(∂ G )ν = 0. Thus, the rank-one direction νν⊤ lies in the radical of the coordinate
|         | H   | D        |     |          |             |          |     |      |     |     |     |
| ------- | --- | -------- | --- | -------- | ----------- | -------- | --- | ---- | --- | --- | --- |
| Hessian |     | wherever | ν   | ̸= 0. In | particular, | detHessD |     | ≡ 0. |     |     |     |
We can now assemble the three-variable reduction. The proof first strips full determinant
factors and then applies the rank-one, pure plane-minor, or mixed analysis according to
| the | boundary |     | restriction. |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Proof of Theorem 3. Apply Lemma D.4 repeatedly to write the original polynomial as
∤
D = δeE, where δ E. If p ̸≡ 0, Lemma D.8 and Proposition D.1 give case (i). Suppose
E
that p ≡ 0. Lemma D.6 supplies a common face type (a,b). Evaluating a nonzero face
E
restrictionatarank-onematrixshowsthatb ≥ 1. Ifa = 0,thepureplane-minorargument
above gives case (ii). If a ≥ 1, the type is mixed. Proposition D.2, Corollary D.1, and
the kernel-field argument give every assertion in case (iii). Since a mixed type has degree
| a+2b | ≥   | 3, no | mixed | case occurs | in  | degrees | at  | most two. |     |     |     |
| ---- | --- | ----- | ----- | ----------- | --- | ------- | --- | --------- | --- | --- | --- |
Theorem 3 leaves one geometric question. The next lemma shows that constancy of the
kernel line is exactly the missing condition for the mixed flag form.
Lemma D.11 (Constant kernel and the mixed flag form). Let E be determinant-free and
of mixed face type (a,b). The following statements are equivalent.
(i) The projective kernel line is constant on a nonempty open subset of S3 .
++
| (ii) | A   | fixed | nonzero | vector | u satisfies | G   | (Σ)u | ≡ 0. |     |     |     |
| ---- | --- | ----- | ------- | ------ | ----------- | --- | ---- | ---- | --- | --- | --- |
|      |     |       |         |        | 0           |     | E    | 0    |     |     |     |
(iii) There are a nonzero constant γ, a vector v ∈ u⊥, and a full-row-rank matrix M
0
|     | with | rowspace(M) |     | = u⊥ | such | that |     |     |     |     |     |
| --- | ---- | ----------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- |
0
|       |       |      |       |     | E(Σ)          | = γ(v⊤Σv)adet(MΣM⊤)b. |        |       |     |     |     |
| ----- | ----- | ---- | ----- | --- | ------------- | --------------------- | ------ | ----- | --- | --- | --- |
| Every | mixed | flag | power | has | this constant |                       | kernel | line. |     |     |     |
Proof of Lemma D.11. If the projective kernel line is constant on a nonempty open set,
choose a fixed representative u ̸= 0. Then G (Σ)u = 0 on that open set and hence
|     |     |     |     |     | 0   |     |     | E 0 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
identically, because its entries are polynomials. This proves (i)⇒(ii), and the reverse
| implication |     | is  | immediate. |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
41

Assume(ii). Afteranorthogonalcongruence, takeu = e . Underthesymmetric-gradient
|     |     |     |     |     |     |     |     |     | 0   | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
convention,
|     |     |     |       | 1   |     |      |     | 1   |     |        |        |     |
| --- | --- | --- | ----- | --- | --- | ---- | --- | --- | --- | ------ | ------ | --- |
|     |     | (G  | e ) = | ∂   | E,  | (G e | ) = | ∂   | E,  | (G e ) | = ∂ E. |     |
|     |     | E   | 3 1   | σ13 |     | E    | 3 2 | σ23 |     | E 3    | 3 σ33  |     |
|     |     |     |       | 2   |     |      |     | 2   |     |        |        |     |
These derivatives vanish identically, so E depends only on the leading 2 × 2 block S.
¯
| Write | E(Σ) = | E(S). | The | block | form | of  | G Σ | gives |     |     |     |     |
| ----- | ------ | ----- | --- | ----- | ---- | --- | --- | ----- | --- | --- | --- | --- |
E
|     |     |     |     |       |     | (Σ)Σ)2} |     |       | (S)S)2}. |     |     |     |
| --- | --- | --- | --- | ----- | --- | ------- | --- | ----- | -------- | --- | --- | --- |
|     |     |     |     | tr{(G |     |         | =   | tr{(G | E¯       |     |     |     |
E
¯
Thus, E is exactly self-normalizing on Sym with the same constant. Theorem 2 gives
2
| ¯   | γ(w⊤Sw)a′(detS)b′. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E (S) = Face-type uniqueness in Lemma D.6 gives (a′,b′) = (a,b).
| Lifting | w to | v ∈ e⊥ | proves | (iii). |     |     |     |     |     |     |     |     |
| ------- | ---- | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
3
Conversely, both gradient factors of a mixed flag power annihilate u . The product rule
0
therefore gives G (Σ)u = 0 identically. Since G has rank two on S3 , its kernel is
|         |        | E        |     | 0   |     |     |     |     | E   |     | ++  |     |
| ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exactly | span(u | ) there. |     |     |     |     |     |     |     |     |     |     |
0
The cofactor identity provides a second constraint on the moving kernel. It couples
the kernel vector to the determinant boundary without assuming that the kernel line is
constant.
Proposition D.3 (Cofactor syzygy). Let E be a determinant-free mixed solution of type
| (a,b), | and write | adj(G |     | ) = ψνν⊤. |     | Then |     |     |     |     |     |     |
| ------ | --------- | ----- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- |
E
|     |     |     |     | ψ(Σ)ν(Σ)⊤adj(Σ)ν(Σ) |     |     |     | = b(a+b)E(Σ)2. |     |     |     | (D.3) |
| --- | --- | --- | --- | ------------------- | --- | --- | --- | -------------- | --- | --- | --- | ----- |
Proof of Proposition D.3. LetA = G Σ. Itseigenvaluesare(a+b)E,bE,0,sotr{adj(A)} =
E
b(a+b)E2. For square matrices, adj(BC) = adj(C)adj(B). Therefore,
|     |     |     | adj(G |     | Σ) = | adj(Σ)adj(G |     | ) = | ψadj(Σ)νν⊤. |     |     |     |
| --- | --- | --- | ----- | --- | ---- | ----------- | --- | --- | ----------- | --- | --- | --- |
|     |     |     |       | E   |      |             |     | E   |             |     |     |     |
Taking the trace proves (D.3) on the positive cone and hence as a polynomial identity.
Lemma D.11 identifies the exact geometric obstruction. Proposition D.3 records an alge-
| braic relation |          | that | any nonconstant |     |     | kernel  | map   | must | satisfy. |     |     |     |
| -------------- | -------- | ---- | --------------- | --- | --- | ------- | ----- | ---- | -------- | --- | --- | --- |
| D.6            | Boundary |      | rigidity        |     |     | for the | mixed |      | branch   |     |     |     |
The constant-kernel criterion is geometric. The results in this subsection give a separate
algebraic closure when the rank-two boundary data already agree with one fixed flag. The
| argument | does | not | assume | the | desired | interior |     | factorization. |     |     |     |     |
| -------- | ---- | --- | ------ | --- | ------- | -------- | --- | -------------- | --- | --- | --- | --- |
Definition D.1 (Flag-coherent boundary). A determinant-free mixed polynomial D of
type (a,b) has a flag-coherent boundary if there are nested spaces V ⊂ V and a nonzero
|          |        |      |       |        |        |         |       |     |      |             | 1 2 |     |
| -------- | ------ | ---- | ----- | ------ | ------ | ------- | ----- | --- | ---- | ----------- | --- | --- |
| constant | γ such | that |       |        |        |         |       |     |      |             |     |     |
|          |        |      |       |        | det(Σ) | |       | D−γ∆a |     | ∆b . |             |     |     |
|          |        |      |       |        |        |         |       | V1  | V2   |             |     |     |
| For K    | = a+2b | and  | α =   | (a+b)2 | +b2,   | put     |       |     |      |             |     |     |
|          |        |      | q = K | −3j,   |        | W (a,b) | = {bq | +ap | :    | p = 0,...,q | }.  |     |
|          |        |      | j     |        |        | j       |       | j   |      |             | j   |     |
The set W (a,b) is the collection of weights available to a homogeneous correction of
j
| degree | q on | the determinant |     |     | boundary. |     |     |     |     |     |     |     |
| ------ | ---- | --------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
j
42

Definition D.2 (Boundary nonresonance). The type (a,b) is boundary-nonresonant if
|     |     |     | α−jK | ∈/  | W (a,b) |     | {j = 1,...,⌊K/3⌋}. |     |     |     |     |
| --- | --- | --- | ---- | --- | ------- | --- | ------------------ | --- | --- | --- | --- |
j
The next lemma gives two arithmetic forms of this condition. They are useful for locating
| the first | possible | resonance. |     |     |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma D.12 (Arithmetic characterization of boundary nonresonance). A type (a,b) is
resonant if and only if there is an integer j ∈ {1,...,⌊K/3⌋} such that
|               |     |               |     | a        | | jb, | j(2a+b)      |       | ≤ ab. |     |     | (D.4) |
| ------------- | --- | ------------- | --- | -------- | ----- | ------------ | ----- | ----- | --- | --- | ----- |
| Equivalently, | if  | g = gcd(a,b), |     | boundary |       | nonresonance |       | is    |     |     |       |
|               |     |               |     |          | b(g   | −1)          | < 2a. |       |     |     | (D.5) |
Proof of Lemma D.12. A resonance has the form α−jK = b(K−3j)+ap for an integer
| 0 ≤ p ≤ | K −3j. | Solving | for | p gives |     |     |     |     |     |     |     |
| ------- | ------ | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
jb
|     |     |     |     |     | p = | a+b−j | +   | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
a
For 1 ≤ j ≤ ⌊K/3⌋, this quantity is positive. It is an integer if and only if a | jb. The
upper bound p ≤ K −3j is equivalent to j(2a+b) ≤ ab. This proves (D.4).
Write a = ga and b = gb , where gcd(a ,b ) = 1. The divisibility condition a | jb is
|     | 0   |     |     | 0   |     | 0   | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
equivalent to a | j. Hence, the smallest positive admissible value is j = a/g. Since
|         | 0         |      |     |             |     |        |        |      |     | 0   |     |
| ------- | --------- | ---- | --- | ----------- | --- | ------ | ------ | ---- | --- | --- | --- |
| j(2a+b) | increases | with | j,  | a resonance |     | exists | if and | only | if  |     |     |
a
|     |     |     |     |     | (2a+b) |     | ≤ ab. |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ----- | --- | --- | --- | --- |
g
After division by a, this is b(g −1) ≥ 2a. If this inequality holds, then j ≤ ab/(2a+b)
0
and
3ab
|     |     |     |     | 3j  | ≤   | ≤   | a+2b | =   | K,  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
0
2a+b
because 3ab ≤ (a+2b)(2a+b). Thus, j ≤ ⌊K/3⌋ automatically. Negating the resonance
0
| criterion | gives (D.5). |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Boundarynonresonanceexcludeseverypolynomialcorrectioncompatiblewiththeweighted
Euler equation on a rank-two face. It therefore turns flag-coherent boundary data into a
| unique | interior | solution. |     |     |     |     |     |     |     |     |     |
| ------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proposition D.4(Boundary-coherentmixedconverse). Ifadeterminant-free exactlyself-
normalizing polynomial of mixed type (a,b) has a flag-coherent boundary and is boundary-
|              |                |      | γ∆a | ∆b          |       |       |       |     |     |     |     |
| ------------ | -------------- | ---- | --- | ----------- | ----- | ----- | ----- | --- | --- | --- | --- |
| nonresonant, | then           | D =  |     | .           |       |       |       |     |     |     |     |
|              |                |      |     | V1 V2       |       |       |       |     |     |     |     |
| Proof        | of Proposition | D.4. | By  | congruence, |       | take  |       |     |     |     |     |
|              |                |      |     | D           | = γσa | (σ    | σ −σ2 | )b. |     |     |     |
|              |                |      |     |             | 0     | 11 11 | 22    | 12  |     |     |     |
If D ̸= D , boundary coherence gives D = D +δjR for an exact j ≥ 1, where δ ∤ R and
|     | 0   |     |     |     |     |     | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
degR = q = K −3j. Put A = G Σ and B = jRI +G Σ. Then G Σ = A +δjB.
|     | j   |     |     | 0   | D0  |     |     |     | R   | D   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
43

Since D and D have the same constant α = c/2, expansion of (4), cancellation, and
0
| restriction | to  | δ = | 0 give |     |        |              |     |     |     |     |       |
| ----------- | --- | --- | ------ | --- | ------ | ------------ | --- | --- | --- | --- | ----- |
|             |     |     |        |     | tr(A G | Σ) = (α−jK)D |     | R.  |     |     | (D.6) |
|             |     |     |        |     | 0 R    |              |     | 0   |     |     |       |
Write J = G /D and Z = ΣJ Σ. The left-hand side of (D.6) is D dR (Z ). Hence,
|      | 0              | D0  | 0      | 0   | 0     |     |          |     |     | 0 Σ 0 |       |
| ---- | -------------- | --- | ------ | --- | ----- | --- | -------- | --- | --- | ----- | ----- |
| on a | dense boundary |     | chart, |     |       |     |          |     |     |       |       |
|      |                |     |        |     | dR (Z | ) = | (α−jK)R. |     |     |       | (D.7) |
Σ 0
| Use | the polynomial |     | LDL⊤ | parametrization |     |         |     |       |     |     |     |
| --- | -------------- | --- | ---- | --------------- | --- | ------- | --- | ----- | --- | --- | --- |
|     |                |     |      |                 |     |         |     |      |    |     |     |
|     |                |     |      |                 |     |         |     | 1 0   | 0   |     |     |
|     |                |     | Σ    | = T diag(r      | ,r  | ,r )T⊤, | T = | t 1  | 0. |     |     |
|     |                |     |      |                 | 1 2 | 3       |     |  21  |    |     |     |
|     |                |     |      |                 |     |         |     | t t   | 1   |     |     |
|     |                |     |      |                 |     |         |     | 31 32 |     |     |     |
Then ∆ = r , ∆ = r r , δ = r r r , and D = γra+brb. A direct logarithmic-gradient
|     | 1   | 1 2 | 1   | 2   | 1 2 3 |     | 0   | 1   |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
2
| calculation | gives       |     |       |     |                 |     |     |        |     |     |     |
| ----------- | ----------- | --- | ----- | --- | --------------- | --- | --- | ------ | --- | --- | --- |
|             |             |     |       | Z   | = T diag{(a+b)r |     | ,br | ,0}T⊤. |     |     |     |
|             |             |     |       |     | 0               |     | 1   | 2      |     |     |     |
| At fixed    | T, equation |     | (D.7) | on  | r = 0 becomes   |     |     |        |     |     |     |
3
|     |     |     |     |         |      |       | ¯             |     | ¯   |     |     |
| --- | --- | --- | --- | ------- | ---- | ----- | ------------- | --- | --- | --- | --- |
|     |     |     |     | {(a+b)r | ∂    | +br ∂ | }R = (α−jK)R. |     |     |     |     |
|     |     |     |     |         | 1 r1 | 2     | r2            |     |     |     |     |
Since R is homogeneous of degree q and Σ is linear in (r ,r ,r ), its restriction has the
|     |     |     |     |     | j   |     |     | 1 2 | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
expansion
qj
|     |     |     |     | ¯   |             |     | X        | qj−p |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | -------- | ---- | --- | --- | --- |
|     |     |     |     | R   | (r ,r ,0,T) | =   | c (T)rpr | .    |     |     |     |
|     |     |     |     |     | 1 2         |     | p        | 1 2  |     |     |     |
p=0
The monomial indexed by p has weight bq + ap. Boundary nonresonance forces every
j
c (T) to vanish. Thus, R vanishes on a nonempty open subset of the rank-two stratum.
p
Lemma D.2 gives δ | R, which contradicts the exact choice of j. Therefore, D = D .
0
The arithmetic condition is automatic in the lowest mixed degrees. The first normalized
| resonance | appears |     | only | in degree | nine. |     |     |     |     |     |     |
| --------- | ------- | --- | ---- | --------- | ----- | --- | --- | --- | --- | --- | --- |
Corollary D.2 (Low mixed degrees and the resonance locus). After mixed adjugate du-
ality, normalize the type by a ≥ b. A flag-coherent solution is a flag power when b ≤ 2,
and hence for every mixed degree at most eight. The first normalized resonance is (3,3)
in degree nine. More generally, resonance is equivalent to b{gcd(a,b)−1} ≥ 2a.
Proof of Corollary D.2. A resonance requires j(2a+b) ≤ ab. If b = 1 or b = 2, this fails
for j = 1 and therefore for every larger j. If a ≥ b ≥ 3, then K = a + 2b ≥ 9. At
(3,3), the choice j = 1 gives equality and satisfies a | jb. The greatest-common-divisor
| characterization |     | follows |     | from | Lemma | D.12. |     |     |     |     |     |
| ---------------- | --- | ------- | --- | ---- | ----- | ----- | --- | --- | --- | --- | --- |
The preceding proposition gives a conditional closure of the three-variable converse that
is independent of kernel-line constancy. It applies whenever the face factors glue to one
| fixed | flag and | the | resulting | type | is nonresonant. |     |     |     |     |     |     |
| ----- | -------- | --- | --------- | ---- | --------------- | --- | --- | --- | --- | --- | --- |
Theorem D.1 (Conditional characterization in dimension three). Suppose that every
determinant-free mixed residue can, after mixed adjugate duality if necessary, be chosen
with a flag-coherent boundary and a boundary-nonresonant type. On this class, the exactly
| self-normalizing |     | polynomials |     |     | are precisely | the | flag powers. |     |     |     |     |
| ---------------- | --- | ----------- | --- | --- | ------------- | --- | ------------ | --- | --- | --- | --- |
44

Proof of Theorem D.1. Strip determinant powers and apply Theorem 3 to the residue.
The rank-one and pure plane-minor cases are flag powers. In the mixed case, apply
the assumed adjugate normalization, boundary coherence, and Proposition D.4. Mixed
duality returns the flag form to the original residue. Restoring determinant powers adds
| the full | space to | the flag. |     |     |     |     |     |     |     |     |
| -------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
The conditional theorem isolates two separate issues in the mixed branch. The first is
geometric gluing of the face directions. The second is an explicit arithmetic resonance
| that begins | only          | at higher | degree.  |     |     |           |     |           |     |     |
| ----------- | ------------- | --------- | -------- | --- | --- | --------- | --- | --------- | --- | --- |
| D.7         | A conditional |           | converse |     | in  | arbitrary |     | dimension |     |     |
The three-variable spectral argument does not extend directly to higher dimensions. A
converse is nevertheless available once the relative gradients preserve one fixed recursive
ordering. The next proposition shows that this invariant flag determines the polynomial
uniquely.
Proposition D.5 (Recursive-flag converse). Let D be homogeneous, nonconstant and
exactly self-normalizing on Sym . Suppose that a complete flag 0 = F ⊂ F ⊂ ··· ⊂
|     |     |     |     | d   |     |     |     |     |     | 0 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rd
F = is preserved by R (Σ) for every Σ ≻ 0. Suppose also that the scalar induced on
| d     |               |     | D       |               |     |     |     |     |     |     |
| ----- | ------------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
| F /F  | is a constant | m   | . After | a congruence, |     |     |     |     |     |     |
| i i−1 |               |     | i       |               |     |     |     |     |     |     |
d
|     |      |     | Y     | )er, |     |        |     | Z   |     |      |
| --- | ---- | --- | ----- | ---- | --- | ------ | --- | --- | --- | ---- |
|     | D(Σ) | = γ | det(Σ |      | e   | = m −m |     | ∈   | , m | = 0. |
|     |      |     |       | 1:r  | r   | r      | r+1 |     | ≥0  | d+1  |
r=1
| Conversely, | every | flag | power | has such | a fixed | recursive |     | flag. |     |     |
| ----------- | ----- | ---- | ----- | -------- | ------- | --------- | --- | ----- | --- | --- |
Sd
Proof of Proposition D.5. By Lemma B.3, D has no zero on . Hence, log|D| is glob-
++
ally defined on the connected cone and on its connected Cholesky parametrization. Use
a congruence to take F = span(e ,...,e ). Then R (Σ) is upper triangular with diag-
|     |     |     | i   | 1   | i   |     | D   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LL⊤,
onal (m ,...,m ). Write the unique Cholesky factorization Σ = where L is lower
1 d
triangular with positive diagonal, and put J = G /D. The matrix
D
|     |     |     |     | L⊤JL |     | L⊤R | (Σ)L−⊤ |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     | C =  | =   |     |        |     |     |     |
D
is symmetric. It is also upper triangular because R (Σ) preserves the coordinate flag
D
and conjugation by L⊤ and L−⊤ preserves upper triangularity. Therefore, C is diagonal.
Triangular conjugation preserves diagonal entries, so C = diag(m ,...,m ).
|        |               |                  |     |     |              |     |     |       | 1   | d   |
| ------ | ------------- | ---------------- | --- | --- | ------------ | --- | --- | ----- | --- | --- |
| For an | infinitesimal | lower-triangular |     |     | perturbation |     | dL  | = LA, |     |     |
|        |               |                  |     | dΣ  | = L(A+A⊤)L⊤. |     |     |       |     |     |
Hence,
d
|     |     |     |         |               |     |     |     | X   | dL   |     |
| --- | --- | --- | ------- | ------------- | --- | --- | --- | --- | ---- | --- |
|     |     |     | dlog|D| | = tr{C(A+A⊤)} |     |     | = 2 | m   | ii . |     |
i
L
|             |        |           |     |          |        |       |     | i=1 | ii  |     |
| ----------- | ------ | --------- | --- | -------- | ------ | ----- | --- | --- | --- | --- |
| Integration | on the | connected |     | Cholesky | domain | gives |     |     |     |     |
d
Y
|     |     |     |     | D(LL⊤) |     | = γ | L2mi |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | ---- | --- | --- | --- |
ii
i=1
45

| for a | nonzero | constant | γ.  |     |     |     |     |
| ----- | ------- | -------- | --- | --- | --- | --- | --- |
Restrict to diagonal Cholesky factors and write x = L2 > 0. Then D{diag(x ,...,x )}
|     |     |     |     |     | i ii |     | 1 d |
| --- | --- | --- | --- | --- | ---- | --- | --- |
γQ xmi
is a polynomial in the x and equals on the positive orthant. Fixing all variables
|     |     |     | i   | i i |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Q
except x shows that each m is a nonnegative integer. Since ∆ = detΣ = L2, we
|        | i      |          |       | i   |     | r 1:r | i≤r ii |
| ------ | ------ | -------- | ----- | --- | --- | ----- | ------ |
| obtain | in the | fraction | field |     |     |       |        |
d
Y ∆mr−mr+1.
|     |     |     |     | D = γ |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
r
r=1
By Lemma D.1, the ∆ are pairwise nonassociate irreducible polynomials. The valuation
r
of the polynomial D at ∆ is m − m and must be nonnegative. This proves the
|     |     |     |     | r r r+1 |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |
factorization.
The converse is the upper-triangular calculation in the proof of Theorem 1. If only a
constant spectrum is assumed in addition to a common invariant flag, each quotient
weight is a continuous map from the connected cone to a finite multiset and is therefore
constant.
Proposition D.5 separates the higher-dimensional obstruction from the integration step.
Once one invariant recursive flag is present, no additional polynomial solutions occur.
| D.8 | Proof | of  | the | low-degree-factor | diagnostic |     |     |
| --- | ----- | --- | --- | ----------------- | ---------- | --- | --- |
The final part of Section 4 concerns denominators whose determinant-free irreducible fac-
tors have degree at most two. The proof identifies global linear and quadratic factors from
their generic plane restrictions. It then uses the two-subspace criterion in Supplementary
| Section | C to | force | nesting. |     |     |     |     |
| ------- | ---- | ----- | -------- | --- | --- | --- | --- |
Lemma D.13 (Generic linear factors). Let L (Σ) = tr(BΣ) with B ∈ Sym and B ̸= 0.
|     |     |     |     |     | B   |     | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- |
If the restriction of L to a Zariski-dense set of planes is a rank-one linear form on
B
Sym , then B has rank one. If two such forms are associates on a dense set of planes,
2
| their | rank-one | directions |     | are proportional. |     |     |     |
| ----- | -------- | ---------- | --- | ----------------- | --- | --- | --- |
Proof of Lemma D.13. If rankB ≥ 2, the symmetric bilinear form represented by B has a
nondegenerate two-dimensional compression. Rank at least two persists on a Zariski-open
neighbourhood of that plane, contrary to the hypothesis. Thus, B = ηvv⊤. For two rank-
one forms, association on a dense family of planes makes the wedge of the two projected
vectors vanish as a polynomial in the plane coordinates. It therefore vanishes on every
plane. The plane spanned by two nonproportional directions would give a contradiction,
| so the | directions | are | proportional. |     |     |     |     |
| ------ | ---------- | --- | ------------- | --- | --- | --- | --- |
The next lemma globalizes a pure-power restriction on generic projective lines. It is used
to exclude the square alternative for an irreducible quadratic factor.
Lemma D.14 (Single-support restriction). Let p be a nonzero homogeneous form of
degree m ≥ 2 on C3. If the restriction of p to a Zariski-dense set of projective lines is an
| mth | power | of a linear | form, | then p = γℓm | for a linear form | ℓ.  |     |
| --- | ----- | ----------- | ----- | ------------ | ----------------- | --- | --- |
Proof of Lemma D.14. On each line in the stated family, the zero set has one support
point. If the reduced plane curve {p = 0} had degree at least two, a general line would
red
46

meet it transversally in at least two points by Bezout’s theorem. Hence, the reduced curve
is a line, and unique factorization gives the claim.
An admissible irreducible quadratic must vanish on the rank-one cone. The next lemma
identifies it as a linear form in the adjugate matrix.
Lemma D.15 (Irreducible quadratic factors). Let Q be an irreducible real quadratic on
Sym . Suppose that, on a dense family of planes, every irreducible factor of Q is either
3 V
the unique rank-one linear face factor or detS. Then Q(Σ) = tr{Cadj(Σ)} for a nonzero
matrix C ∈ Sym .
3
Proof of Lemma D.15. WorkinanaffinechartofGr(2,3)inwhichabasismatrixP(t)de-
pendspolynomiallyonthechartcoordinatest. ThecoefficientsofQ (S) = Q{P(t)SP(t)⊤}
V(t)
are polynomial in t. Proportionality to detS is cut out by the 2×2 minors of the corre-
sponding coefficient vectors. Being a scalar multiple of a square of a linear form is cut out
by the 2 × 2 minors of the symmetric coefficient matrix of the ternary quadratic Q .
V(t)
TheseequationsarecompatibleonoverlapsanddefineintrinsicZariski-closedsubsetsZ
det
and Z of the complexified Grassmannian. The real Grassmannian is Zariski dense in
sq
its complexification. On a dense open set of good real planes, a degree-two restriction
is either proportional to detS or to the square of the unique linear face factor. Hence,
Gr(2,3) = Z ∪Z . Since the Grassmannian is irreducible, one of these closed subsets
C det sq
is the whole Grassmannian.
Consider first the determinant alternative. Proportionality to detS then holds for every
plane, includingazerorestriction. LetG = {V ∈ Gr(2,3) : Q ̸≡ 0}. Thisisanonempty
C V
Zariski-open set. It is nonempty because otherwise Q would vanish on the rank-two
determinant hypersurface and would be divisible by the cubic detΣ, which is impossible
for a nonzero quadratic. For V ∈ G, Q = η detS with η ̸= 0. Put B = Gr(2,3) \G.
V V V C
Identify Gr(2,3) with the dual projective plane. The planes containing a fixed point
C
[u] ∈ P2 form a projective line Π . If [u] lies on no plane in G, then Π ⊆ B. A proper
C u u
closed subset of the projective plane has only finitely many one-dimensional irreducible
components. Therefore, this can occur for at most finitely many pencils Π . For every
u
other [u], there is V ∈ G with u ∈ V, and Q(uu⊤) = Q (ξξ⊤) = 0. Thus, Q vanishes on
V
a Zariski-dense subset of the rank-one cone and hence on the whole cone.
The space of quadratics vanishing on {uu⊤ : u ∈ R3} is {tr(CadjΣ) : C ∈ Sym }.
3
QuadraticsonSym havedimension21,whilequarticsinuhavedimension15. Therestric-
3
tionmapissurjectivebecauseeveryquarticmonomialisaproductoftwoquadraticmono-
mials. The displayed family has dimension six and is injective. Indeed, if tr{Cadj(Σ)} ≡
0, then for every positive-definite T choose Σ = (detT)1/2T−1 so that adj(Σ) = T. Then
tr(CT) = 0 on an open set, which gives C = 0. The displayed family is therefore exactly
the kernel of the restriction map.
Suppose instead that Q is generically a square. Then p (u) = Q(uu⊤) restricts to a
V Q
fourth power on a dense set of lines. Lemma D.14 gives p (u) = γ(v⊤u)4. Consequently,
Q
Q = γ(v⊤Σv)2 + tr(CadjΣ) for some C. On a generic plane, the first two quadratic
expressions are squares of linear forms, while the last is (n⊤Cn)detS, where n is a normal
to the plane. A difference of two squares has matrix rank at most two as a quadratic
form on Sym . By contrast, detS = s s −s2 has rank three as a quadratic form on
2 11 22 12
(s ,s ,s ). Hence, n⊤Cn ̸= 0 is impossible. Since n⊤Cn = 0 for a Zariski-dense set
11 12 22
47

of normals, C = 0. Then Q is a square, contrary to irreducibility. Only the determinant
| alternative | remains. |     |     |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- | --- | --- |
The preceding lemmas show that all global linear factors are powers of one variance
direction and all irreducible quadratic factors are adjugate-linear. Adjugate duality then
| forces | the quadratic | directions | to  | coincide. |     |     |     |
| ------ | ------------- | ---------- | --- | --------- | --- | --- | --- |
Proof of Theorem 4. Strip the largest determinant power and call the determinant-free
| residue | E. Factor | it over | R as |       |     |       |     |
| ------- | --------- | ------- | ---- | ----- | --- | ----- | --- |
|         |           |         |      |       | r   | s     |     |
|         |           |         |      |       | Y   | Y     |     |
|         |           |         |      | E = γ | Lαi | Q βj, |     |
|         |           |         |      |       | i   | j     |     |
|         |           |         |      |       | i=1 | j=1   |     |
where the L are pairwise nonassociate linear forms and the Q are pairwise nonassociate
|     | i   |     |     |     |     |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- |
irreducible quadratics. Choose a generic good plane on which all indicated restrictions are
nonzero. The common face-type representation is E (S) = γ ℓ (S)a(detS)b. If a = 0,
|     |     |     |     |     |     | V   | V V |
| --- | --- | --- | --- | --- | --- | --- | --- |
unique factorization on a generic face forces r = 0. If a > 0, every L | is associated with
i V
the unique linear factor ℓ . Lemma D.13 shows that all L are rank-one and associate.
|       |            |           | V      |        |          | i          |     |
| ----- | ---------- | --------- | ------ | ------ | -------- | ---------- | --- |
| Their | product is | therefore | absent | or has | the form | γ (v⊤Σv)p. |     |
1
For each Q , its generic restriction is either a square of ℓ , when a > 0, or a multiple
|     | j   |     |     |     |     | V   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
of detS. Lemma D.15 gives Q (Σ) = tr{C adj(Σ)}. Put q = P β . If q > 0, adjugate
|     |     |     | j   |     | j   |     | j j |
| --- | --- | --- | --- | --- | --- | --- | --- |
duality yields
δq{v⊤adj(Σ)v}pY
|     |     |     | E† = γ |     |     | {tr(C Σ)}βj, |     |
| --- | --- | --- | ------ | --- | --- | ------------ | --- |
|     |     |     | 2      |     |     | j            |     |
j
wherethefactorinvolvingv isomittedwhenp = 0. Thedisplayedpoweroftheirreducible
cubic δ is exact. After stripping it, the residue is again determinant-free and exactly self-
normalizing. Its linear factors tr(C Σ) restrict on a generic face to the unique linear face
j
factor. Lemma D.13 shows that every C has rank one and that all are proportional.
j
| Hence, | C = η uu⊤ | and |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- |
j j
(v⊤Σv)p{u⊤adj(Σ)u}q,
|     |     |     | E(Σ) | = γ |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
3
with an absent factor interpreted as one. The second factor is the determinant of the
compression to u⊥. If p,q > 0, Lemma C.1 forces the line and plane to be nested. A
plane cannot be contained in a line, so span(v) ⊂ u⊥. Restoring the stripped determinant
| power | gives the flag | form | in (11). |     |     |     |     |
| ----- | -------------- | ---- | -------- | --- | --- | --- | --- |
The corollary converts the flag form into coefficient-level rank and orthogonality tests. It
| also identifies | every | reducible | self-normalizing |     |     | cubic. |     |
| --------------- | ----- | --------- | ---------------- | --- | --- | ------ | --- |
Proof of Corollary 1. Necessity is Theorem 4. Sufficiency and the value of c follow from
Theorem 1, whose multiplicities are (a+b+e,b+e,e). A cubic satisfying the low-degree-
factor condition is either a scalar multiple of δ, or its determinant-free part has only linear
and quadratic factors. The theorem gives the three possibilities in the corollary. Every
| reducible | cubic belongs |     | to the latter | class. |     |     |     |
| --------- | ------------- | --- | ------------- | ------ | --- | --- | --- |
The low-degree-factor converse is unconditional on its stated class. An irreducible factor
of degree at least three is the only factorization pattern not decided by this diagnostic.
48

E Proofs of Section 5: Weak-denominator inference
This section proves Propositions 1 and 2 and verifies the example that delimits the scope
of the classification in Section 5 of the main text. Both proofs rest on one triangular-array
central limit theorem for the sample covariance, which is established at the start of the
first proof and reused in the second.
The proof of Proposition 1 combines this central limit theorem with polynomial delta
expansions along the drifting sequence.
Proof of Proposition 1. For row n, write
n
Y = vech(X X⊤ −Σ ), ∆ = n−1/2X Y = n1/2 vech(Σ ˆ −Σ ).
ni ni ni n n ni n
i=1
Within each row the Y are independent and identically distributed, with covariance
ni
Γ(Σ ) → Γ(Σ ). Since Σ → Σ , Gaussian eighth-moment formulas for the quadratic
n ∗ n ∗
vector Y give
n1
supE ∥Y ∥4 < ∞.
n n1
n
Consequently, the Lyapunov quantity n−2Pn E ∥Y ∥4 is O(n−1). The multivariate
i=1 n ni
triangular-array Lyapunov theorem gives
∆ ⇝ N {0,Γ(Σ )}.
n p ∗
d
Because (N −τ D)(Σ ) = 0 and the polynomials are fixed, and their second derivatives
n n
ˆ
are bounded on a fixed neighbourhood of Σ , Taylor’s theorem together with Σ−Σ =
∗ n
O (n−1/2) yields
p
n1/2{N(Σ ˆ )−τ D(Σ ˆ )} = g⊤∆ +o (1), n1/2D(Σ ˆ ) = n1/2D(Σ )+∇D(Σ )⊤∆ +o (1).
n n n p n n n p
˜
Since g → g and ∇D(Σ ) → ∇D(Σ ), the pair converges jointly to (s Z,s (µ +Z ))
n ∗ n ∗ g,∗ D,∗ ∗ 2
with the stated correlation. The limiting denominator has a continuous distribution,
ˆ
so division gives the ratio limit in (13). The convergence s (Σ) − s −→ 0 and
D D,n p
s → s > 0 then give the limit of Fb .
D,n D,∗ D
For the Wald statistic, write W = τˆ− τ and use the direction gˆ defined in (12). The
n n
ratio limit gives W = O (1), so the polynomial-gradient expansion gives
n p
gˆ = g −W ∇D(Σ )+o (1).
n n n p
Substitutingtheratiolimitshowsthatgˆ⊤Γ(Σ ˆ )gˆ/s2 convergesindistributionto1−2r q+
g,∗ ∗
q2. Combining this with
n1/2|D(Σ ˆ )|W
n ⇝ Z ˜ sgn(µ +Z )
∗ 2
s
g,∗
gives (14). The limiting studentizer equals {(q−r )2+1−r2}1/2, which is positive almost
∗ ∗
surely when |r | < 1.
∗
49

The argument uses the drifting sequence only through the limits µ , r and ω , which is
|     |     |     |     |     |     |     |     |     | ∗   | ∗ ∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
why a single three-parameter experiment covers every covariance-polynomial strategy, as
| stated in | the main | text. |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
The proof of Proposition 2 treats coverage and sample geometry separately. Coverage
follows from the same central limit theorem applied to the moment at the local target,
and the trichotomy is the sign analysis of one quadratic polynomial in t.
Proof of Proposition 2. At t = τ , the moment N − τ D vanishes at Σ and has gra-
|     |     |     |     | n   |     |     |     | n   |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dient g . The central limit theorem from the proof of Proposition 1, together with
n
ˆ
h⊤Γ(Σ )h −→ s2 > 0, shows that the squared studentized moment converges in
| τn  | τn  | p g,∗ |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
χ2.
distribution to This proves the coverage statement without requiring a nonzero limit
1
of D.
| For the | sample geometry, |     | put | q = | q   | and |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1−α
|     |     |     | P (t) | = n{N(Σ | ˆ )−tD(Σ |     | ˆ )}2 | −qh⊤Γ(Σ | ˆ )h , |     |
| --- | --- | --- | ----- | ------- | -------- | --- | ----- | ------- | ------ | --- |
|     |     |     | Σˆ    |         |          |     |       |         | t      |     |
t
| a quadratic | polynomial |     | in t whose |      | leading | coefficient |        | is         |     |     |
| ----------- | ---------- | --- | ---------- | ---- | ------- | ----------- | ------ | ---------- | --- | --- |
|             |            |     | ˆ          |      | ˆ       |             | ˆ      | ˆ          |     |     |
|             |            |     | A(Σ ) =    | nD(Σ | )2 −qs2 |             | (Σ ) = | s2 (Σ ){Fb | −q} |     |
|             |            |     |            |      |         | D           |        | D          | D   |     |
|             | s2 ˆ       |     |            |      |         |             |        |            | ˆ   |     |
whenever (Σ ) > 0. Under n > d and Σ ≻ 0, the matrix nΣ has a Wishart density
|     | D   |     |     |     |     | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sd
on and is therefore absolutely continuous with respect to Lebesgue measure on Sym
++ d
(Muirhead, 1982, Ch. 3). The polynomial s2 is not identically zero because s2 (Σ ) > 0,
∗
|      |     |     |     |     |     | D   |     |     |     | D   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| s2 ˆ |     |     |     |     |     | ˆ   |     |     |     | ˆ ˆ |
so (Σ ) = 0 is a null event. Likewise D(Σ ) = 0 is a null event, so τˆ = N(Σ )/D(Σ ) is
D
| defined | almost surely. |     |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ˆ
The event A(Σ ) = 0 is also null. If the polynomial A(Σ) = nD(Σ)2 − qs2 (Σ) is not
D
identically zero, this follows from absolute continuity. If it were identically zero, then
s2 (n/q)D2
= and D would be exactly self-normalizing, whereas Assumption 1 gives
D
D(Σ ) = 0 and s (Σ ) > 0, and these two requirements are incompatible with (4).
| ∗   |     | D ∗ |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Finally,
|     |     |     |     |     |        | −qh⊤Γ(Σ | ˆ   |         |     |     |
| --- | --- | --- | --- | --- | ------ | ------- | --- | ------- | --- | --- |
|     |     |     |     | P   | (τˆ) = |         |     | )h ≤ 0, |     |     |
|     |     |     |     | Σˆ  |        | τˆ      |     | τˆ      |     |     |
ˆ
so the sublevel set {t : P (t) ≤ 0} is nonempty. On the probability-one event {A(Σ) ̸= 0},
Σˆ
elementary quadratic geometry shows that this set is an interval, possibly a singleton, the
R,
complement of a bounded open interval, or all of and that it is bounded exactly when
A(Σ) ˆ > 0, which is equivalent to Fb > q. This is the classical Fieller trichotomy (Fieller,
D
1954), and the inversion is also an Anderson–Rubin construction (Anderson and Rubin,
1949).
Thefinalitemverifiestheexamplethatthemaintextusestoseparateexactself-normalization
| from mere | first-order |     | degeneracy | on  | a zero | set. |     |     |     |     |
| --------- | ----------- | --- | ---------- | --- | ------ | ---- | --- | --- | --- | --- |
Example E.1 (First-order degeneracy without exact self-normalization). On Sym , let
2
| D(Σ) = | σ2 . Then |     |     |     |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
12
|     |     |     |     | s2  | 4σ2 |     |       | +σ2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     |     | =   | (σ  | σ     | ),  |     |     |
|     |     |     |     | D   |     | 12  | 11 22 | 12  |     |     |
so s = 0 vanishes on the entire zero set of D although s2 /D2 is not constant. For
D
D
| σ =  | σ = 1 | and  | σ =  | ζn−1/2, |      |     |      |     |              |     |
| ---- | ----- | ---- | ---- | ------- | ---- | --- | ---- | --- | ------------ | --- |
| 11,n | 22,n  |      | 12,n |         |      |     |      |     |              |     |
|      |       |      | )2   | ζ2      |      |     | +Z)2 |     |              |     |
|      |       | nD(Σ |      |         |      |     | (ζ   |     |              |     |
|      |       |      | n    | →       | , Fb | ⇝   |      | ,   | Z ∼ N (0,1). |     |
|      |       |      |      |         | D    |     |      |     | 1            |     |
|      |       | s2   | (Σ ) | 4       |      |     | 4    |     |              |     |
D n
50

The variance formula follows from (3), because the only nonzero coordinate of ∇D is
∂D/∂σ = 2σ and the corresponding diagonal entry of Γ is σ σ + σ2 . Cancelling
12 12 11 22 12
one factor of σ2 gives
12
nσˆ2
Fb = 12 ,
D 4(σˆ σˆ +σˆ2 )
11 22 12
wherever σˆ ̸= 0, and the same cancellation at Σ gives the population limit ζ2/4.
12 n
Under the displayed drift, n1/2σˆ ⇝ ζ +Z by the central limit theorem in the proof of
12
Proposition 1, while σˆ σˆ +σˆ2 −→ 1, which proves the limit of Fb . Assumption 1 fails
11 22 12 p D
along this sequence because s = 0, so the nondegenerate limit of Fb arises at second
D,∗ D
order, exactly as claimed in the main text.
F Proofs of Section 6: Causal applications
F.1 Structural pullbacks used in Table 1
This subsection verifies the third column of Table 1 in the main text. Each entry records
a direct substitution into a linear reduced form for that row and is not an additional
identification claim. All variables are centred, and symbols are local to the reduced form
in which they appear, as in the footnote to the table.
For the instrumental-variable row, let
X = πZ +ε , ν = var(Z), cov(Z,ε ) = 0.
X Z X
Then σ = πν .
ZX Z
For the conditional-instrument row, let
Z = λW +ε , X = πZ +ηW +ε , ν = var(W), v = var(ε ),
Z X W Z Z
where ε is uncorrelated with W and ε is uncorrelated with (Z,W). Substituting σ =
Z X ZX
πσ +ησ and σ = πσ +ησ cancels the terms in η and gives
ZZ ZW WX ZW WW
σ σ −σ σ = π(σ σ −σ2 ) = πν v .
WW ZX ZW WX WW ZZ ZW W Z
For the front-door row, let
M = aX +ε , ν = var(X), v = var(ε ), cov(X,ε ) = 0.
M X M M M
Then,
σ (σ σ −σ2 ) = ν2 v ,
XX XX MM XM X M
so the front-door denominator equals ν2 v .
X M
For the proximal row, let
A = λU +ε , Z = aU +ε , W = cU +ε , ν = var(U), v = var(ε ),
A Z W U A A
where U,ε ,ε ,ε are mutually uncorrelated. Then
A Z W
σ σ −σ σ = acν (λ2ν +v )−aλν λcν = acν v .
ZW AA ZA AW U U A U U U A
These four calculations define the symbols of the table and make every displayed pullback
verifiable.
51

| F.2 | Marginal |     | and | partial |     | minors |     |     |     |     |
| --- | -------- | --- | --- | ------- | --- | ------ | --- | --- | --- | --- |
This subsection proves the marginal and partial calibrations displayed in Section 6 of the
main text. Let a,b,e ∈ [d] with e ̸= a and e ̸= b, allowing a = b where indicated. As
in the main text, ρˆ is the sample correlation of coordinates a and b, the sample partial
ab
correlation ρˆ is the correlation of the residuals from the sample linear projections of
ab·e
nρˆ2
coordinates a and b on coordinate e, and the partial first-stage index is F = /(1−
par ab·e
ρˆ2
).
ab·e
The next proposition contains both variance identities and both closed forms for the
| standardized |     | denominator. |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Proposition F.1 (Marginal and partial minor calibration). For D = σ with a ̸= b,
ab
nρˆ2
|     |     |     |     | s2  |     | +D2,  |     |      | ab    |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ---- | ----- | --- |
|     |     |     |     |     | = σ | σ     |     | Fb = | .     |     |
|     |     |     |     |     | D   | aa bb |     | D    | 1+ρˆ2 |     |
ab
| For | D = | σ σ −σ | σ     | ,   |     |       |      |       |     |     |
| --- | --- | ------ | ----- | --- | --- | ----- | ---- | ----- | --- | --- |
|     |     | ee ab  | ea eb |     |     |       |      |       |     |     |
|     |     |        |       |     | s2  |       |      | +3D2. |     |     |
|     |     |        |       |     | =   | detΣ  | detΣ |       |     |     |
|     |     |        |       |     | D   | {e,a} |      | {e,b} |     |     |
When a = b the second identity reduces to s2 = 4D2. When a ̸= b, Fb = nF /(n +
|     |     |     |     |     |     |     |     | D   | D   | par |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4F ).
par
The case a = b recovers the constant c = 4 of Theorem 1 for a principal minor of order
two. In the two slope cases the standardized denominator is an increasing transform of
the familiar marginal or partial first-stage index, so the algebraic diagnostic automatically
| selects | the | screening | direction |     | relevant | to  | the | strategy. |     |     |
| ------- | --- | --------- | --------- | --- | -------- | --- | --- | --------- | --- | --- |
Proof of Proposition F.1. For D = σ with a ̸= b, the only nonzero coordinate of ∇D
ab
is ∂D/∂σ = 1, and the corresponding diagonal entry of Γ in (2) is σ σ +σ2 , which
|     |     | ab  |     |     |     |     |     |     | aa bb |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
ab
ˆ
proves the first identity. Evaluating at Σ and dividing the numerator and denominator of
| Fb  | by σˆ | σˆ gives | the | first closed |     | form. |     |     |     |     |
| --- | ----- | -------- | --- | ------------ | --- | ----- | --- | --- | --- | --- |
| D   | aa    | bb       |     |              |     |       |     |     |     |     |
For D = σ σ −σ σ , both sides of the asserted identity scale by the same factor under
|     |     | ee ab | ea eb |     |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Σ 7→ ΛΣΛ for positive diagonal Λ, so it suffices to verify it as σ = σ = σ = 1.
ee aa bb
Put x = σ , y = σ and ρ = σ . The nonzero coordinates of ∇D are ∂D/∂σ = ρ,
|     |     | ea  | eb  |     | ab  |     |     |     |     | ee  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂D/∂σ = 1, ∂D/∂σ = −y and ∂D/∂σ = −x, and expanding the quadratic form
|      | ab  |            | ea        |     |        |     | eb    |                        |     |     |
| ---- | --- | ---------- | --------- | --- | ------ | --- | ----- | ---------------------- | --- | --- |
| with | the | entries of | (2) gives |     |        |     |       |                        |     |     |
|      |     | s2 1+3ρ2   | −x2       | −y2 | +4x2y2 |     |       | (1−x2)(1−y2)+3(ρ−xy)2. |     |     |
|      |     | =          |           |     |        |     | −6ρxy | =                      |     |     |
D
| Undoing |     | the rescaling | gives |     | the determinant |     |     | identity. |     |     |
| ------- | --- | ------------- | ----- | --- | --------------- | --- | --- | --------- | --- | --- |
If a = b, then detΣ = detΣ = D, so s2 = 4D2. If a ̸= b, the sample partial
|             |     |           | {e,a} |     |     | {e,b} |     | D   |     |     |
| ----------- | --- | --------- | ----- | --- | --- | ----- | --- | --- | --- | --- |
| correlation |     | satisfies |       |     |     |       |     |     |     |     |
ˆ )2
D(Σ
|     |     |     |     |     | ρˆ2 | =   |     |     | ,   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ab·e
|     |     |     |     |     |     | detΣ | ˆ     | detΣ ˆ |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----- | ------ | --- | --- |
|     |     |     |     |     |     |      | {e,a} | {e,b}  |     |     |
so
nρˆ2
|     |     |     |     |     |     | Fb  | =   | ab·e , |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
D
1+3ρˆ2
ab·e
and substituting ρˆ2 = F /(n+F ) gives the second closed form.
|     |     |     | ab·e | par |     | par |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
52

F.3 Front-door boundary robustness
This subsection proves Proposition 3. The proof rests on three exact facts. The plug-in
estimatorfactorsasaproductoftworegressioncoefficients, theGaussiandeltastudentizer
is an exact combination of the two regression standard errors, and the second coefficient
has an exact Student statistic independent of the design. The boundary limit then fol-
lows by comparing the two terms of the combination uniformly in the mediator residual
variance, which makes quantitative the mechanism described after the proposition in the
main text.
Proof of Proposition 3. Write Z = (X ,M )⊤ and let W = σ(Z ,...,Z ). The covari-
i i i n 1 n
ˆ
ance formula factors exactly as τˆ = aˆb, where
P X M
aˆ = i i i
P X2
i i
istheknown-meanleast-squarescoefficientintheregressionofM onX, andthecoefficient
vector in the regression of Y on (X,M) is
(γˆ, ˆ b)⊤ = ( X Z Z⊤)−1X Z Y .
i i i i
i i
Put
1 n 1 n
vˆ = X (M −aˆX )2, σˆ2 = X (Y −γˆX − ˆ bM )2.
M n i i ε n i i i
i=1 i=1
The usual no-intercept regression standard errors are
vˆ σˆ2
se2 = M , se2 = ε . (F.1)
ba
(n−1)σˆ
bb
(n−2)vˆ
XX M
We first identify the Gaussian delta variance exactly. For a positive-definite covariance
matrix, let a(Σ) be the regression coefficient of M on X, let (γ(Σ),b(Σ)) be the coefficient
vector in the regression of Y on (X,M), and put
R = M −a(Σ)X, R = Y −γ(Σ)X −b(Σ)M,
M Y
and define σ = var (R ) and σ = var (R ). The influence functions of the
MM·X Σ M YY·XM Σ Y
two coefficient functionals under known-mean covariance sampling are
XR R R
M M Y
ϕ = , ϕ = .
a b
σ σ
XX MM·X
The first identity follows by differentiating a = σ /σ . The second follows by differ-
XM XX
entiating the normal equations (γ,b)⊤ = Σ−1 Σ and applying the Frisch–
(X,M),(X,M) (X,M),Y
Waugh residualization. Under a centred Gaussian law, X and R are independent, and
M
R is independent of (X,M). Hence,
Y
σ σ
∇a⊤Γ∇a = MM·X , ∇b⊤Γ∇b = YY·XM , ∇a⊤Γ∇b = 0. (F.2)
σ σ
XX MM·X
These are identities of rational functions on the positive cone and may therefore be eval-
ˆ
uated at Σ. Since ∇(ab) = b∇a+a∇b, the Gaussian delta standard error defined in (19)
53

| satisfies | the | exact | sample | identity |       |     |     |      |     |     |     |     |
| --------- | --- | ----- | ------ | -------- | ----- | --- | --- | ---- | --- | --- | --- | --- |
|           |     |       |        |          |       |    |     |      |    |     |     |     |
|           |     |       |        |          |       | 1  | vˆ  |      | σˆ2 |     |     |     |
|           |     |       |        |          |       | ˆ   | M   |      |    |     |     |     |
|           |     |       |        |          | se2 = | b2  |     | +aˆ2 | ε   |     |     |     |
b
|     |     |     |     |     |     | n  | σˆ  |     | vˆ M |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- |
|     |     |     |     |     |     |     | XX  |     |       |     |     | (F.3) |
|     |     |     |     |     |     | n−1 |     | n−2 |       |     |     |       |
ˆ
|       |     |        |          |     | =             |     | b2se2        | +   | aˆ2se2, |        |     |     |
| ----- | --- | ------ | -------- | --- | ------------- | --- | ------------ | --- | ------- | ------ | --- | --- |
|       |     |        |          |     |               | n   | ba           |     | n       | bb     |     |     |
| where | the | second | equality | is  | the algebraic |     | substitution |     | of      | (F.1). |     |     |
For completeness, the zero cross term in (F.2) also has an exact finite-sample regression
| justification. |     | ConditionalonW |     |     | ,   | thedifferenceb−bisalinearfunctionoftheindependent |     | ˆ   |     |     |     |     |
| -------------- | --- | -------------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
n
| mean-zero |     | errors ε | , so |     |     |     |     |     |     |     |     |     |
| --------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     |     | E(  | ˆ b | W | ) = | b,  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
n
whereas aˆ is W -measurable. Thus cov(aˆ,b) ˆ = 0 for every n and every interior covariance.
n
For a fixed interior covariance, Gaussian projection formulas give
|     |              |     |     |     | 3v2        | n2  |     |       |          |               | 3σ4n2 |     |
| --- | ------------ | --- | --- | --- | ---------- | --- | --- | ----- | -------- | ------------- | ----- | --- |
|     | E{n2(aˆ−a)4} |     |     |     |            | M   |     | E{n2( | ˆ b−b)4} |               | ε     |     |
|     |              |     |     | =   |            |     | ,   |       |          | =             |       |     |
|     |              |     |     | ν2  | (n−2)(n−4) |     |     |       |          | v2 (n−3)(n−5) |       |     |
|     |              |     |     | X   |            |     |     |       |          | M             |       |     |
ˆ
for all sufficiently large n. Hence, n(aˆ − a)(b − b) is uniformly integrable. The joint
delta limit therefore has zero covariance, in agreement with the direct influence-function
calculation.
Conditional on W , the usual Gaussian regression decomposition and Cochran’s theorem
n
ˆ
show that the statistic T = (b − b)/se has the t law. The conditional law does not
|        |     |        |      | b           |      | bb  |             |     | n−2       |           |     |     |
| ------ | --- | ------ | ---- | ----------- | ---- | --- | ----------- | --- | --------- | --------- | --- | --- |
| depend | on  | W , so | T is | independent |      | of  | the design. |     | Moreover, |           |     |     |
|        |     | n      | b    |             |      |     |             |     |           |           |     |     |
|        |     |        |      | nvˆ         |      |     | nσˆ2        |     |           |           |     |     |
|        |     |        |      | M           | ∼ χ2 | ,   | ε ∼         | χ2  | , σ2      | = var(ε), |     |     |
|        |     |        |      | v           | n−1  |     | σ2          | n−2 | ε         |           |     |     |
|        |     |        |      | M,n         |      |     | ε           |     |           |           |     |     |
with the second chi-squared variable independent of the design. These are the standard
Gaussian projection identities (Muirhead, 1982, Ch. 3). It follows that, uniformly over
| 0 < | v ≤ | v¯, |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M,n
|     |     |     |      |     |       |     | /n)1/2}, |     | se2   | σ2. |     |     |
| --- | --- | --- | ---- | --- | ----- | --- | -------- | --- | ----- | --- | --- | --- |
|     |     |     | aˆ−a | =   | O {(v |     |          | nv  |       | −→  |     |     |
|     |     |     |      |     | p     | M,n |          |     | M,nbb | p ε |     |     |
The first order also follows from the exact moment identity E(aˆ−a)2 = v /{ν (n−2)}.
|     |     |     |     |     |     |     |     |     |     |     | M,n | X   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
If a subsequence has v bounded away from zero, the ordinary joint central limit the-
M,n
orem and Slutsky’s theorem prove the result. Consider a subsequence with v → 0.
M,n
Decompose
|     |     |     | aˆb−ab ˆ |     | = a(b−b)+b(aˆ−a)+(aˆ−a)(b−b). | ˆ   |     |     |     | ˆ   |     |     |
| --- | --- | --- | -------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
After division by |aˆ|se , the first term is {a/|aˆ|}T , which converges in distribution to
|     |     |     | bb  |     |     |     |     |     | b   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sgn(a)Z with Z ∼ N (0,1), and this limit is standard normal by symmetry. Since
1
se−1 = O {(nv )1/2}, the second term is O (v ) = o (1), and the third equals
| bb             |     | p M,n |        |     |     |     |     | p   | M,n | p   |     |     |
| -------------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {(aˆ−a)/|aˆ|}T |     | =     | o (1). |     |     |     |     |     |     |     |     |     |
|                |     | b     | p      |     |     |     |     |     |     |     |     |     |
It remains to compare the delta studentizer with |aˆ|se . From (F.1), se2 = O (v /n),
|       |        |          |     |       |            |     |     |     | bb  |     | ba  | p M,n |
| ----- | ------ | -------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | ----- |
| while | ˆ b2 = | O {1+(nv |     | )−1}. | Therefore, |     |     |     |     |     |     |       |
|       |        | p        | M,n |       |            |     |     |     |     |     |     |       |
ˆ
|     |     |     |     | (n−1)       | b2se2 |     |       |     |     |          |     |     |
| --- | --- | --- | --- | ----------- | ----- | --- | ----- | --- | --- | -------- | --- | --- |
|     |     |     |     |             | ba    |     | {v2   |     |     |          |     |     |
|     |     |     |     |             |       | = O |       | +v  | /n} | = o (1). |     |     |
|     |     |     |     | (n−2)aˆ2se2 |       |     | p M,n |     | M,n | p        |     |     |
bb
Equation (F.3) now yields se/(|aˆ|se ) −→ 1. Every subsequence has the same limit,
|            |     |            |     |     | b   | bb  | p   |     |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| completing |     | the proof. |     |     |     |     |     |     |     |     |     |     |
54

Table G.1: Complete denominator summaries for the Gaussian simulations. The population
quantity is nD(Σ)2/s2 (Σ). Dashes denote diagnostics not used for the self-normalizing front-
D
door denominator.
Model Parameter Population F D Median FbD Median partial F Median naive F
|     | Front-door | v   | =1.000 |     | 100.000 | 100.000 |     | –   |     | –   |
| --- | ---------- | --- | ------ | --- | ------- | ------- | --- | --- | --- | --- |
M
|     | Front-door | v   | =0.100 |     | 100.000 | 100.000 |     | –   |     | –   |
| --- | ---------- | --- | ------ | --- | ------- | ------- | --- | --- | --- | --- |
M
|     | Front-door | v   | =0.010 |     | 100.000 | 100.000 |     | –   |     | –   |
| --- | ---------- | --- | ------ | --- | ------- | ------- | --- | --- | --- | --- |
M
|     | Front-door | v   | =0.001 |     | 100.000 | 100.000 |     | –   |     | –   |
| --- | ---------- | --- | ------ | --- | ------- | ------- | --- | --- | --- | --- |
M
|     | Proximal | v   | =1.00 |     | 63.729 | 63.792 |     | 85.647 | 179.670 |     |
| --- | -------- | --- | ----- | --- | ------ | ------ | --- | ------ | ------- | --- |
A
|     | Proximal | v   | =0.30 |     | 26.482 | 26.492 |     | 29.632 | 362.006 |     |
| --- | -------- | --- | ----- | --- | ------ | ------ | --- | ------ | ------- | --- |
A
|     | Proximal | v   | =0.10 |     | 6.218 | 6.234 |     | 6.393 | 510.227 |     |
| --- | -------- | --- | ----- | --- | ----- | ----- | --- | ----- | ------- | --- |
A
|     | Proximal | v   | =0.03 |     | 0.774 | 0.922 |     | 0.926 | 595.168 |     |
| --- | -------- | --- | ----- | --- | ----- | ----- | --- | ----- | ------- | --- |
A
|     | Proximal | v   | A =0.01 |     | 0.095 | 0.504 |     | 0.505 | 624.555 |     |
| --- | -------- | --- | ------- | --- | ----- | ----- | --- | ----- | ------- | --- |
The final display shows that the delta studentizer is asymptotically equivalent to the
dominant regression studentizer uniformly in v , which is the exact balance behind the
M,n
| boundary |                 | robustness. |           |            |             |     |            |            |     |     |
| -------- | --------------- | ----------- | --------- | ---------- | ----------- | --- | ---------- | ---------- | --- | --- |
| G        | Detailed        |             | numerical |            | experiments |     |            |            |     |     |
| G.1      | Data-generating |             |           | mechanisms |             |     | and target | parameters |     |     |
We give the complete specifications used for Table 2. The front-door covariance is gener-
ated by X = ε , M = 0.8X +ε and Y = M +ε , where (ε ,ε ) is centred Gaussian
|     |     | X   |     |     | M   |     | Y   | X Y |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with unit marginal variances and covariance 0.5, and ε is independent Gaussian with
M
variance v . The target is 0.8. The proximal covariance is generated by Z = 0.8U +ε ,
|     |     | M   |     |     |     |     |     |     |     | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A = 0.8U +ε , W = 0.8U +ε and Y = A+0.8U +ε . All shocks in the proximal de-
|     |     | A   |     | W   |     |     | Y   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sign are mutually independent centred Gaussian variables and have unit variance except
| var(ε | ) =         | v ; the | target is | one. |           |     |     |     |     |     |
| ----- | ----------- | ------- | --------- | ---- | --------- | --- | --- | --- | --- | --- |
|       | A           | A       |           |      |           |     |     |     |     |     |
| G.2   | Computation |         |           | and  | precision |     |     |     |     |     |
For each population covariance Σ, we draw the known-mean sample covariance directly
ˆ
from nΣ ∼ W (n,Σ). We compute the plug-in covariance ratio, its Gaussian delta stan-
d
darderror, thestandardizeddenominatorandtheindicatorthatthetruetargetbelongsto
the inverted set in (15). The robust standard deviation is the interquartile range divided
by 1.349. Each cell uses n = 1000 and 100000 replications. The Wald and inversion cal-
χ2
culations use the two-sided 95% standard-normal and critical values, respectively. The
1
{pˆ(1−pˆ)/(100000)}1/2;
Monte Carlo standard error attached to a coverage estimate pˆis
the largest value in the experiment is 0.00081. No replication fails the validity checks.
The front-door median standard errors closely track the empirical robust standard devi-
ations over the entire 1000-fold range of v . For the proximal design, agreement is good
M
when v is 1 or 0.3, but the Gaussian Wald approximation deteriorates once the popu-
A
lation denominator diagnostic falls below about 10. At v = 0.03 and 0.01, the sample
A
median Fb exceeds its population value because sampling noise is no longer small relative
D
to the denominator, while inversion retains near-nominal coverage.
55

Table G.2: Dispersion, standard errors and bias in the Gaussian simulations. Robust s.d.,
| interquartile | range | divided    | by  | 1.349.    |     |         |      |             |             |     |
| ------------- | ----- | ---------- | --- | --------- | --- | ------- | ---- | ----------- | ----------- | --- |
|               |       | Model      |     | Parameter |     | Robust  | s.d. | Median s.e. | Median bias |     |
|               |       | Front-door |     | v =1.000  |     | 0.03848 |      | 0.03848     | −0.00044    |     |
M
|     |     | Front-door |     | v M =0.100 |     | 0.06997 |     | 0.06996 | −0.00001 |     |
| --- | --- | ---------- | --- | ---------- | --- | ------- | --- | ------- | -------- | --- |
|     |     | Front-door |     | v =0.010   |     | 0.21745 |     | 0.21904 | 0.00086  |     |
M
|     |     | Front-door |     | v =0.001 |     | 0.69552 |     | 0.69252 | −0.00295 |     |
| --- | --- | ---------- | --- | -------- | --- | ------- | --- | ------- | -------- | --- |
M
|     |     | Proximal |     | v A =1.00 |     | 0.06415 |     | 0.06327 | −0.00002 |     |
| --- | --- | -------- | --- | --------- | --- | ------- | --- | ------- | -------- | --- |
|     |     | Proximal |     | v =0.30   |     | 0.17279 |     | 0.16975 | 0.00064  |     |
A
|     |     | Proximal |     | v =0.10 |     | 0.49080 |     | 0.46761 | 0.00878 |     |
| --- | --- | -------- | --- | ------- | --- | ------- | --- | ------- | ------- | --- |
A
|     |     | Proximal |     | v =0.03 |     | 1.18672 |     | 1.43329 | 0.43527 |     |
| --- | --- | -------- | --- | ------- | --- | ------- | --- | ------- | ------- | --- |
A
|     |     | Proximal |     | v =0.01 |     | 1.46031 |     | 2.03695 | 0.88490 |     |
| --- | --- | -------- | --- | ------- | --- | ------- | --- | ------- | ------- | --- |
A
Table G.3: Coverage and Monte Carlo standard errors in the Gaussian simulations. Cov.,
empirical 95% coverage; MCSE, Monte Carlo standard error; inversion, coverage of (15) at the
true target.
Model Parameter Wald cov. Wald MCSE Inversion cov. Inversion MCSE
|     | Front-door |     | v =1.000 |     | 0.94943 |     | 0.00069 |     | 0.95370 | 0.00066 |
| --- | ---------- | --- | -------- | --- | ------- | --- | ------- | --- | ------- | ------- |
M
|     | Front-door |     | v =0.100 |     | 0.94968 |     | 0.00069 |     | 0.95450 | 0.00066 |
| --- | ---------- | --- | -------- | --- | ------- | --- | ------- | --- | ------- | ------- |
M
|     | Front-door |     | v =0.010 |     | 0.94920 |     | 0.00069 |     | 0.95353 | 0.00067 |
| --- | ---------- | --- | -------- | --- | ------- | --- | ------- | --- | ------- | ------- |
M
|     | Front-door |     | v =0.001 |     | 0.94950 |     | 0.00069 |     | 0.95348 | 0.00067 |
| --- | ---------- | --- | -------- | --- | ------- | --- | ------- | --- | ------- | ------- |
M
|     | Proximal |     | v =1.00 |     | 0.95247 |     | 0.00067 |     | 0.95254 | 0.00067 |
| --- | -------- | --- | ------- | --- | ------- | --- | ------- | --- | ------- | ------- |
A
|     | Proximal |     | v A =0.30 |     | 0.95204 |     | 0.00068 |     | 0.95168 | 0.00068 |
| --- | -------- | --- | --------- | --- | ------- | --- | ------- | --- | ------- | ------- |
|     | Proximal |     | v =0.10   |     | 0.93531 |     | 0.00078 |     | 0.95262 | 0.00067 |
A
|     | Proximal |     | v =0.03 |     | 0.93042 |     | 0.00080 |     | 0.95150 | 0.00068 |
| --- | -------- | --- | ------- | --- | ------- | --- | ------- | --- | ------- | ------- |
A
|     | Proximal  |     | v A =0.01 |               | 0.93091     |     | 0.00080 |     | 0.95141 | 0.00068 |
| --- | --------- | --- | --------- | ------------- | ----------- | --- | ------- | --- | ------- | ------- |
| H   | Detailed  |     | real      | data          | experiments |     |         |     |         |         |
| H.1 | Variables |     | and       | preprocessing |             |     |         |     |         |         |
We use the public SUPPORT right-heart-catheterization data (Connors et al., 1996),
distributedathttps://hbiostat.org/data/repo/rhc.csvandcontaining5735patients
and 63 variables. Treatment is the indicator of right-heart catheterization on the first
study day, recorded in the variable swang1 and coded as one for the value RHC and zero
for No RHC. The descriptive outcome is survival time in days truncated at 30, recorded
in t3d30. The treatment proxies are pafi1 and paco21, and the outcome proxies are
ph1 and hema1. These six analysis variables are required to be observed and are not
imputed. The adjustment set contains age, sex, cat1, cat2, dnr1, surv2md1 and aps1,
correspondingtothecovariatesdescribedinSection8ofthemaintext. Missingcontinuous
adjustment covariates are median-imputed. Missing categorical adjustment covariates are
mode-imputed and coded by indicator variables with one level omitted. Nonconstant
design columns are standardized before an intercept is added, and the standardization
does not alter the projection space. The resulting design has rank 19 and leaves 5716
| residual | degrees    | of freedom. |          |     |     |           |     |     |     |     |
| -------- | ---------- | ----------- | -------- | --- | --- | --------- | --- | --- | --- | --- |
| H.2      | Diagnostic |             | formulas |     | and | bootstrap |     |     |     |     |
Let (A,Z,W,Y) denote the residualized treatment, treatment proxy, outcome proxy and
| outcome. | For | their empirical |     | second | moments, |     | put |       |       |     |
| -------- | --- | --------------- | --- | ------ | -------- | --- | --- | ----- | ----- | --- |
|          |     | D               | = σ | σ      | −σ σ     | ,   | N = | σ σ   | −σ σ  | ,   |
|          |     |                 | AA  | ZW     | AZ       | AW  |     | ZW AY | ZY AW |     |
56

Table H.1: Detailed point diagnostics for the SUPPORT analysis. Partial corr., sample partial
correlation between the treatment and outcome proxies given residualized treatment.
Treatment proxy Outcome proxy Partial corr. Estimate Gaussian FbD Sandwich FbD
|     | pafi1  |     |     | ph1   |     |     | 0.0236  | −1.245 |     |         | 3.179 | 2.306   |     |
| --- | ------ | --- | --- | ----- | --- | --- | ------- | ------ | --- | ------- | ----- | ------- | --- |
|     | pafi1  |     |     | hema1 |     |     | −0.0750 | −1.412 |     | 31.591  |       | 25.710  |     |
|     | paco21 |     |     | ph1   |     |     | −0.5072 | −1.328 |     | 829.990 |       | 315.190 |     |
|     | paco21 |     |     | hema1 |     |     | 0.1095  | −1.136 |     | 66.131  |       | 51.337  |     |
Table H.2: Percentile bootstrap intervals for the SUPPORT analysis. Intervals use 2000 row-
bootstrap replications. They reflect sampling variation under the prespecified preprocessing and
| proxy | allocation, |     | but not | uncertainty |     | about | proxy | validity. |     |     |     |     |     |
| ----- | ----------- | --- | ------- | ----------- | --- | ----- | ----- | --------- | --- | --- | --- | --- | --- |
Treatment proxy Outcome proxy Estimate 95% interval Sandwich-FbD 95% interval
|     | pafi1  |     |     | ph1   |     |     |          | (−2.249, | 0.139) |     | (0.011,   | 12.733)  |     |
| --- | ------ | --- | --- | ----- | --- | --- | -------- | -------- | ------ | --- | --------- | -------- | --- |
|     | pafi1  |     |     | hema1 |     |     | (−2.036, | −0.806)  |        |     | (9.166,   | 51.302)  |     |
|     | paco21 |     |     | ph1   |     |     | (−1.839, | −0.811)  |        |     | (218.242, | 461.934) |     |
|     | paco21 |     |     | hema1 |     |     | (−1.689, | −0.563)  |        |     | (30.317,  | 78.353)  |     |
so the reported proximal plug-in estimate is N/D. Put ν = n−r, where r is the realized
adjustment-design rank. Both denominator diagnostics have the form νD2/sˆ2 . Define
D
M = σ σ − σ2 and M = σ σ − σ2 . The Gaussian version uses sˆ2 =
| AZ  |     | AA ZZ |     |     | AW  |     | AA WW |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     |       | AZ  |     |     |     |       | AW  |     |     |     |     | D   |
M M +3D2, as in (16). The sandwich version uses the centred empirical covariance,
AZ AW
with divisor n, of the six second-moment scores (A2,Z2,W2,AZ,AW,ZW). The naive
| and | partial | indices | use | νρˆ2/(1−ρˆ2), |     |     | as stated | in the | main | text. |     |     |     |
| --- | ------- | ------- | --- | ------------- | --- | --- | --------- | ------ | ---- | ----- | --- | --- | --- |
We use 2000 nonparametric row-bootstrap replications. Each resample repeats the com-
plete preprocessing and residualization and uses the realized design rank to determine
ν. The resampled design rank is 19 in 1704 replications and 18 in 296 replications. The
| intervals | below |     | are percentile |     | intervals. |     |     |     |     |     |     |     |     |
| --------- | ----- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
The weak pafi1/ph1 pair is the only allocation for which the bootstrap estimate interval
containszeroandthelowerendpointofthesandwich-diagnosticintervalisessentiallyzero.
The other three allocations have diagnostic intervals bounded away from zero, although
the discrepancy between the Gaussian and sandwich versions remains substantial for
paco21/ph1. These comparisons are diagnostic and should not be interpreted as evidence
| for the | untestable |     | proximal |              | bridge | assumptions. |     |             |       |     |        |     |     |
| ------- | ---------- | --- | -------- | ------------ | ------ | ------------ | --- | ----------- | ----- | --- | ------ | --- | --- |
| I       | Algebraic  |     |          | obstructions |        |              |     | in the      | mixed |     | branch |     |     |
| I.1     | Kernel     |     | map      | and          | the    | Hessian      |     | obstruction |       |     |        |     |     |
For a determinant-free mixed solution E with self-normalization constant c, the kernel-
fieldargumentinSupplementarySectionDproducesaprimitivehomogeneouspolynomial
| vector | ν.  | It defines | the | complex-projective |       |     |                             | rational | map     |         |     |     |     |
| ------ | --- | ---------- | --- | ------------------ | ----- | --- | --------------------------- | -------- | ------- | ------- | --- | --- | --- |
|        |     |            |     | [ν] :              | P(Sym | ⊗   | C) (cid:57)(cid:57)(cid:75) | P2,      | [Σ] 7−→ | [ν(Σ)]. |     |     |     |
|        |     |            |     |                    |       | 3   | R                           | C        |         |         |     |     |     |
AteverypointwhereG (Σ)hasranktwoandν(Σ) ̸= 0, theimageistheprojectivekernel
E
line [kerG (Σ)]. Theorem 3 and Lemma D.11 show that the unrestricted three-variable
E
| converse | is  | equivalent |     | to proving |     | that | this map | is constant. |     |     |     |     |     |
| -------- | --- | ---------- | --- | ---------- | --- | ---- | -------- | ------------ | --- | --- | --- | --- | --- |
57

The identity detHessE ≡ 0 does not prove this constancy. The Gordan–Noether cone
conclusion holds for forms in at most four variables, but it fails in six variables, which is
the dimension of Sym (Lossen, 2004; Ciliberto et al., 2008). For example, the cubic in
3
| variables | x ,...,x |            | (Perazzo, | 1900;          | Gondim |     | and Russo,   | 2015)   |     |
| --------- | -------- | ---------- | --------- | -------------- | ------ | --- | ------------ | ------- | --- |
|           | 0        | 5          |           |                |        |     |              |         |     |
|           |          |            |           |                | x2     |     |              | x2 +x3, |     |
|           |          |            |           | P              | = x    | +2x | x x +x       |         |     |
|           |          |            |           |                | 0 4    | 1   | 4 5          | 2 5 3   |     |
| has the   | nonzero  | polynomial |           | Hessian-kernel |        |     | vector       |         |     |
|           |          |            |           |                | (x2,−x | x   | ,x2,0,0,0)⊤. |         |     |
|           |          |            |           |                | 5      | 4 5 | 4            |         |     |
Its first derivatives are linearly independent, so P is not a cone. This cubic is not claimed
to satisfy (4). It shows only that a polynomial Hessian-kernel field need not have a
constant direction. Consequently, the missing implication must use more than Hessian
degeneracy.
| I.2 | Representation-theoretic |     |     |     |     | lifting | obstruction |     |     |
| --- | ------------------------ | --- | --- | --- | --- | ------- | ----------- | --- | --- |
A second possible route uses the derived congruence action ρ. For the matrix units E ,
ij
|          |     |           |         |     | ρ(E            | )E = | 2(G Σ)   | .   |     |
| -------- | --- | --------- | ------- | --- | -------------- | ---- | -------- | --- | --- |
|          |     |           |         |     |                | ij   | E        | ij  |     |
| Equation | (4) | therefore | implies |     | the polynomial |      | identity |     |     |
3
X
|     |     |     |     |     | {ρ(E | )E}{ρ(E | )E} | = 2cE2. | (I.1) |
| --- | --- | --- | --- | --- | ---- | ------- | --- | ------- | ----- |
|     |     |     |     |     |      | ij      | ji  |         |       |
i,j=1
This is the image, under polynomial multiplication, of the tensor relation that one would
| seek from   | a highest-weight |                 |     | orbit  | characterization. |          |          |     |     |
| ----------- | ---------------- | --------------- | --- | ------ | ----------------- | -------- | -------- | --- | --- |
| The theorem |                  | of Lichtenstein |     | (1982) | is                | a tensor | identity | in  |     |
Sym2{SymK(Sym2C3)}.
By contrast, (I.1) lies only in the space of degree-2K polynomial functions. The mul-
tiplication map from the tensor space to degree-2K polynomials has a nontrivial kernel
for K ≥ 2. Hence, the scalar polynomial identity does not determine the required ten-
sor identity. A proof by this route would need an additional argument showing that the
| components | lost | under | multiplication |     |     | vanish | separately. |     |     |
| ---------- | ---- | ----- | -------------- | --- | --- | ------ | ----------- | --- | --- |
These two obstructions explain the scope of Theorem 3. They do not provide evidence for
a nonflag solution. They identify the remaining task more precisely. One must combine
the integrability of the symmetric gradient with the cofactor syzygy or with determinant-
boundary information to force the rational kernel map to be constant.
58
---- END DOCUMENT ----
