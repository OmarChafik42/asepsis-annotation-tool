Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
The geometry of AI validation: Exact certification
limits for iid best-of-N search
Ricardo Fitas
Technical University of Darmstadt, Germany
rfitas99@gmail.com
Abstract theinferenceproducedbyadeploymentrule,nottoamodel
as an intrinsic scalar.
Abstract. AI systems increasingly generate alternatives, This paper begins from one geometric claim. Each valida-
inspectevidence,anddeployaselectedoutput. Validationis
tion intervention defines a kernel describing where it looks;
therefore target-relative: evidence certifies deployment only
deployment defines another kernel describing where it will
in directions resolved by the interventions that produced
place weight. The validated kernels span the directions re-
it. We represent validation and deployment rules as kernels
solved by evidence. If a deployment target lies outside that
over a reliability surface. Their span geometry separates
span,tworeliabilityworldscanagreeoneveryauditandstill
two resources: replication reduces sampling noise, whereas
disagreeafterselection. Thatresidualisstructural blindness.
new intervention directions reduce structural blindness. We
Moreobservationsinsidethesameinterventionsreducenoise
make this principle exact in the canonical iid best-of-N
but do not change the span; a new intervention can. If the
problem. For iid candidates, scalar ranking, randomized target is chosen after evidence is inspected, validity must
ties, maximum selection, bounded binary truth, and an
additionally protect the selectable family. Structural identi-
unchanged rank–truth relation, knowing best-of-n reliability
fication, post-selection inference, and evaluation design are
through n=m leaves exact width
thus consequences of the same target-relative geometry.
We make that geometry exact in a canonical deployment
m (cid:26) (cid:27)
B =1+2 X (−1)rcos2N rπ , problem. Suppose an evaluator knows, without sampling
m,N
r=1
2(m+1) error, iid best-of-n reliability for every n=1,...,m, under
a stable rank–truth law, scalar ranking, randomized ties,
Explicit bounded worlds attain the whole interval, and this
and maximum selection, but deployment searches N > m
prefix is information-maximal among reliability-mean au-
candidates. How far apart can two systems be at N while
dits confined to n ≤ m. The governing scale is m2/N: at
√ agreeing at every audited width? The answer is Eq. 14;
m ∼ N, ambiguity is about 0.83; in the iterated fixed- √
phasethensmall-εlimit,widthεrequiresm≍ p Nlog(1/ε). explicit worlds attain the whole interval. At m ∼ N,
its limiting width remains approximately 0.83, and small
Monotonicitygivesanexactuniform-approximationfrontier;
ambiguity ε requires m2/N ∼log(1/ε).
a Lipschitz bound gives an exact capped-tail dual and order-
The argument follows one idea through four consequences.
sharp L/m2 ambiguity. These results yield a two-gate audit
A target outside the validated span creates exact structural
rule: establish structural coverage, then add independent
ambiguity. Atargetselectedafterevaluationrequiresfamily-
tasks for precision. Retrospective CodeRM programs con-
level rather than unrelated pointwise validity. Audit design
struct compatible best-of-100 values spanning [0.186,0.992]
should therefore add feasible directions that expand the
and [0.305,0.996] as feasible witnesses, and a score-tail rule
span. In iid best-of-N search, the geometry becomes a
frozen after 82 discovery tasks reduced 500-label held-out
closed finite frontier, an information-maximality law for
95th-percentile error from 0.180 to 0.049 and from 0.076
low-width reliability means, and a finite audit-depth rule.
to 0.035. Beyond iid search, the geometry applies only to
Shape constraints test whether the phenomenon survives
known or independently estimated kernels. The empirical
monotonicity and smoothness; the finite-task planner and
analyses are illustrative, not prospective interventions.
two objective-domain studies test how structural breadth
Keywords: AI evaluation; inverse problems; post-selection interactswithtaskprecisionanddeployment-matchedlabels.
inference; optimal experimental design; inference-time
These are not separate warnings: they ask whether one
search.
selection direction is resolved by the interventions used to
Artificial-intelligence systems increasingly do more than validate it.
return a fixed output. They generate alternatives, compare Optimal recovery, truncated Hausdorff moments, post-
them,andactonaselectedanswer,program,prompt,agent, selection inference, and polynomial approximation supply
molecule, experiment, or scientific hypothesis [1–3]. The established ingredients [4–9]. The mathematical contribu-
act of selection changes the population whose truth matters. tion is the validation-specific package obtained after those
Validation is therefore target-relative: reliability belongs to ingredients are specialized: a full attainable bounded-binary
1
6202
guA
12
]GL.sc[
1v69412.8062:viXra

identified interval with explicit common-audit worlds; max- (ii) The largest separation between two validation-
imality of the complete prefix within the reliability-mean equivalent worlds is
query class and its finite theta phase law; and exact mono-
toneandcapped-Lipschitzresidualfrontierslinkedtoafinite sup |R k (f)−R k (g)|=b(k;V). (5)
f,g∈F
audit plan. We isolate the canonical L1 calculation as clas-
Kf=Kg
sical input C0. SI Appendix, Section S11 compares each
(iii) If all kernels integrate to one, the evidence Kf =
submittedobjectwiththeadjacentmoment,expected-order-
(1/2,...,1/2) has an exact identified interval of width
statistic, and best-of-N literatures; no broader theorem
b(k;V), centered at 1/2.
about moment spaces or optimal recovery is asserted.
The scope is equally explicit. The closed form B ap- The theorem formalizes the mental model. Validation-
m,N
plies only to iid candidates, scalar ranking, randomized ties, equivalent worlds can differ only in directions orthogonal
maximum selection, bounded truth, and a stable rank–truth to every v ; pairing the deployment kernel with the largest
j
law. The span theorem covers a different selection mecha- bounded such difference gives exactly its distance from the
nism only when its audit and deployment kernels act on a validated span. The quotient-duality and extremizer argu-
common stable state space and are known or independently ment appears in SI Appendix, Section S1. The equality is
estimated. Unmodeled adaptive generation receives no cer- important: Eq. 5 is the attainable ambiguity, not only an
tificatefromeitherresult. Heremmeasurescoverageoffixed upper bound.
search widths, not labels, tasks, generations, or monetary
cost. Generality at theorem level, not formula level. A
randomized shortlist, top-k draw, rejection sampler, beam-
Validation is a target-relative inverse prob-
search trace, or dependent candidate process induces a
lem
selected-state law different from NuN−1. If that law is
The geometry has three objects: f describes where the known on a common stable state space, Theorem 1 still
system is reliable; each v j describes where a validation pro- gives its exact structural ambiguity as a distance from the
cedure looks; and k describes where deployment will place audited span, without requiring iid candidates. It does not
weight. If k emphasizes a direction that no combination of givethatmechanismthebest-of-N valueB . Foranadap-
the v j observes, exact repetition inside the existing tests tive generator, the state must contain the m r ,N elevant history
cannot recover the missing target. The best-of-N result will
and the policy-induced kernel must be known or indepen-
make this general principle fully explicit for one important
dently estimated; if either is missing, neither the general
order statistic.
theorem nor the iid frontier supplies a certificate. When
Let (X,µ) describe latent deployment conditions—for
those kernels are estimated with L1 error bounds, SI Ap-
example, score ranks, prompts, task subpopulations, or
pendix, Section S7.2 gives an explicit perturbation penalty
workflow states. Let
weighted by the reconstruction coefficients. Thus the broad
result is a known- or estimated-kernel geometry, whereas
f(x)=P(T =1|X =x), 0≤f ≤1, (1)
the closed-form phase law is the exact iid specialization.
be the unknown reliability surface. A normalized validation
For a selectable family K={k
w
:w ∈W}, define
intervention v j ∈L1(µ) observes B(K;V)= sup b(k ;V). (6)
w
w∈W
Z Z
y j =⟨v j ,f⟩:= v j (x)f(x)dµ(x), v j dµ=1. (2) This is the structural half of validation capacity. If B =0,
every target in the family is reconstructible from the vali-
A deployment choice w induces another normalized kernel dated interventions. If B is near one for probability kernels,
k and target some selectable target is compatible with nearly opposite
w
R (f)=⟨k ,f⟩. (3) reliability under the same exact evidence. Importantly, in-
w w
creasing the number of observations inside any existing v
Kernels may be probability densities, signed contrasts, or j
does not change S and hence cannot change B.
known importance weights; normalization is used only to V
give the central evidence below the simple value 1/2. Selection after evidence requires family-level
Write S = span{v ,...,v } ⊂ L1(µ) and define the validity
V 1 p
blind residual
Pointwise identification and pointwise confidence are not
enough when deployment is chosen after evaluation. For a
b(k;V)=dist (k,S )= inf ∥k−s∥ . (4)
L1 V 1 finite target family, let C (Y) be an interval for R (f) and
s∈SV w w
let w(Y) be any measurable selector.
This distance has an exact inferential meaning. b
Proposition 1 (Arbitrary selection equals simultaneous
Theorem 1 (Span theorem and sharp ambiguity). For protection). A confidence system is valid at level 1−α after
F = {f ∈ L∞(µ) : 0 ≤ f ≤ 1} and validation operator every measurable target-selection rule if and only if it covers
Kf =(⟨v j ,f⟩)p j=1 : all targets simultaneously:
(i) R (f) is identified by Kf for every f ∈F if and only
k
if k ∈S V . f i ∈ n F f P f {R w (f)∈C w (Y) for every w ∈W}≥1−α. (7)
2

A Validation is target-relative
adaptively selected 1.0 target
deployment kernels
0.8 blind residual b(k,V)
0.6 0.4
validated span SV
0.2
0.0
100 101 102 103 104 105
Number of selectable targets, M
lavretni
%59
lanimon
fo egarevoC
B Pointwise validity is not selected validity
2.75
2.50
2.25
Coverage after selecting max 2.00 Fixed-target coverage Simultaneous width penalty 1.75
1.50
1.25
1.00
htdiw-flah
esiwtniop
/ htdiw-flah
deriuqeR
Making the geometry exact: the finite best-
of-N frontier
We now make the target-relative geometry fully explicit for
the canonical score-and-select workflow. Let (U ,T ) be iid i i candidates, where the randomized score percentile satisfies
U ∼Unif(0,1) and T ∈{0,1}. Define i i
f(u)=P(T =1|U =u). (9)
Figure 1: Target-relative and post-selection geometry. For a score S with atoms, the precise randomized percentile
is
(A)ValidationkernelsspanS . Adeploymentkerneldecomposes
V
intoarepresentedcomponentandablindresidualwhoseexactL1
norm is the structural ambiguity. Post-evaluation selection can U =F S (S−)+Z{F S (S)−F S (S−)}, Z ∼Unif(0,1)
(10)
choose a kernel with a large residual. The drawing is schematic;
the theorem uses L1/L∞ quotient duality. (B) For M indepen- withZ independent. ThenU isuniform,whileindependence
dent Gaussian target estimates, every fixed-target interval has of the tie jitter makes f constant almost everywhere on the
95% coverage, but the same interval around the largest estimate percentile interval occupied by each score atom. The unre-
rapidly loses coverage. Simultaneous protection widens only as strictedfrontierremainsexactoverthestatedmodelclassbe-
√
logM in this example, yet no amount of replication removes a causecontinuous-scorecandidatelawsattainit;conditioning
nonzero blind residual. on a fixed known atomic score law adds interval-constancy
restrictions and can only narrow the frontier. Best-of-n
selects the largest percentile. Its reliability is
Thenecessityfollowsbyselectingthefirsttargetwhosein-
tervalmisses,ifoneexists. Thisisthesamelogicalreduction
Z 1
used in universal post-selection inference [6]; it is included θ =n un−1f(u)du=⟨k ,f⟩, k (u)=nun−1.
n n n
to identify the correct unit of an AI validation claim, not 0
(11)
as a new abstract post-selection theorem. A fixed, stable,
Atn=1,k weightseverypercentileequally. Asngrows,k
or independently chosen selector can require less protection 1 n
moves its mass into an increasingly thin upper tail: search
[7, 10]. An unrestricted search system cannot be certified
has changed the population whose truth is being averaged.
by a collection of unrelated pointwise statements.
Exact audits at every n = 1,...,m span the polynomials
Figure 1B gives the elementary Gaussian illustration: or-
P . ThisisaboundedHausdorffmomentproblem[8,11];
dinary 95% intervals have correct fixed-target coverage, but m−1
the deployment target k is a more tail-concentrated order-
coveragecollapsesafterdeployingthetargetwiththelargest N
statistic kernel [12, 13].
estimate. This stochastic selection cost requires family-level
For a feasible audit vector y = (y ,...,y ), define the
protection. The blind residual is different: it survives even 1 m
deployment identified set and its worst-case width by
when sampling noise is exactly zero. Under Gaussian audit
noiseofordern−1/2,SIAppendix,SectionS3showsthatany I (y)={⟨k ,f⟩:0≤f ≤1, ⟨k ,f⟩=y (n≤m)},
m,N N n n
linear reconstruction s =P a v admits a bias-centered
w j wj j
estimator satisfying, simultaneously for every w and every (12)
f ∈F, W = sup diamI (y). (13)
m,N m,N
1 q (A,Σ)
y:Im,N(y)̸=∅
|Rbw −R w (f)|≤ 2 ∥k w −s w ∥ 1 + 1−α√ n . (8) Let U m denote the degree-m Chebyshev polynomial of the
second kind and define σ (u)=sgnU (2u−1), with arbi-
m m
The first term is structural and vanishes only when the trary values at its m roots.
deployment direction is represented. The second covers
the selectable family and shrinks with replication. Thus Classical input C0 (Canonical L1 distance (classical)).
replication changes sampling uncertainty, whereas a new For integers N >m≥1, canonical L1 interpolation at the
intervention direction is needed to change structural blind- shifted roots of U m gives
ness.
B :=dist (k ,P )
m,N L1 N m−1
m (cid:26) (cid:27)
Expanding the validated span. The span theorem sug- =1+2 X (−1)rcos2N rπ . (14)
gests choosing feasible new interventions—such as direct
2(m+1)
r=1
labels of selected winners or perturbed workflows—to mini-
mizethelargestblindresidualoverthedeploymentfamily. SI This approximation statement, including its nodes, error
Appendix, Section S3.3 states the formal constrained-width sign, and distance, is classical [14–18].
objective. Redundant evaluations may improve precision Theorem 2 (Finite-prefix certification theorem). For inte-
while adding no new direction; one deployment-matched gers N >m≥1, the worst-case bounded-reliability identified
intervention can remove a residual that thousands of ex-
width in Eq. 13 is exactly
changeable items cannot.
W =B . (15)
m,N m,N
3

Define two complete joint candidate laws P by Corollary 1 (Search–validation phase law). If m,N →∞
±
with m2/N →τ ∈(0,∞), then
U ∼Unif(0,1),
±
(cid:16) (cid:17)
T ± |U ± =u∼Bernoulli{f ± (u)}, (16) B m,N −→B(τ):=ϑ 4 0,e−π2/(4τ) . (21)
1±σ (u)
f ± (u)= 2 m , Define τ ε = inf{τ > 0 : B(τ) ≤ ε}. After first taking the
joint limit at fixed τ and then letting ε↓0,
and take candidate sequences iid under each law. These
worlds satisfy θ n + =θ n − =1/2 for every n≤m, but τ =log 1 + 1 loglog 1 +log√ 4 +o(1). (22)
ε ε 2 ε π
1±B
θ± = m,N. (17)
N 2 No uniform finite-(m,N) statement is asserted for an arbi-
trary sequence ε=ε .
At the common evidence (θ ,...,θ )=(1/2,...,1/2), the N
1 m
identified set is exactly The phase is sharper than the statement that m must be
√
of order N. At m2/N = 1, the exact limiting width is
(cid:20)1−B
m,N,
1+B
m,N
(cid:21)
; (18) approximately0.83: auditingthroughm≈
√
N stillpermits
2 2 reliabilitynearoppositeendsoftheunitinterval. Intuitively,
m polynomial moments resolve the endpoint only on a scale
every interior value is attained by the iid candidate law with
of order m−2, while best-of-N concentrates on a scale of
U ∼ Unif(0,1) and T | U = u ∼ Bernoulli{λf (u)+(1−
+ order N−1. Their ratio is m2/N. The transformed theta
λ)f (u)} for some λ ∈ [0,1]. Consequently Eq. 14 is the
− series,bothasymptoticregimes,andthederivationofEq.22
full worst-case identified width, not only a lower bound.
are in SI Appendix, Section S5 [19].
Classical input C0 computes a distance. Theorem 2 turns
Robustness: the degree-squared law survives
itintoanattainedcertificationstatement: admissibleworlds
shape constraints
(1±σ )/2shareonefeasibleauditvector,attainbothdeploy-
m The exact frontier above is distribution-free. Its principal
ment endpoints, and fill the interval by mixtures. The proof
scientificstresstestiswhetherblindnesssurvivesafterruling
is in SI Appendix, Section S4; the mathematical boundary
out oscillatory reliability. The Chebyshev worlds in Eq. 16
is documented separately in Section S11.
jump between zero and one; let F instead be the nonde-
↑
Proposition 2 (Information maximality of the complete creasing [0,1]-valued functions and, for 0<L<∞, let F
↑,L
low-width prefix). Consider any finite family of reliability- additionally have Lipschitz constant at most L. For realized
meanauditswhosekernelsarerandomizedmixturesofwidths feasible evidence y, define
at most m,
I (y)={θ (f):f ∈G, θ (f)=y , n≤m}. (23)
G N n n
m m
X X
a = q k , q ≥0, q =1, (19) Its exact endpoint programs are in SI Appendix, Section S6.
ℓ ℓn n ℓn ℓn
n=1 n=1 The design frontier is instead the largest compatible width
over feasible evidence:
and let S = span{a }. Its worst-case ambiguity at width
A ℓ
N >m is ∆G = sup diamI (y)
dist L1 (k N ,S A )≥B m,N . (20) m,N IG(y)̸=∅ G
Equality is attained by the complete prefix k 1 ,...,k m . The = sup (cid:12) (cid:12)θ N (f)−θ N (g)(cid:12) (cid:12). (24)
f,g∈G
samelowerboundholdsforasequentialschedulethatchooses
θn(f)=θn(g) (n≤m)
each such mean audit after earlier audit means are observed.
For a=(a ,...,a )∈Rm, put
1 m
EverykernelinEq.19liesinP ,whereasthecomplete
m−1
prefix spans that entire space. Sequential choice cannot m
X
distinguish the endpoint worlds because both return mean z a (t)=1−tN − a n (1−tn) (25)
1/2 for every admissible query. Thus the theorem is not n=1
merely about one convenient sweep of widths: among all
and define
exact population-mean schedules whose revealed kernels re-
main mixtures of fixed widths n≤m, the complete prefix is (cid:26) Z 1 (cid:27)
H (z)= sup cz(0)+ z(t)q(t)dt . (26)
alreadythestructurallystrongestpossibledesign. Theclaim L
c≥0, 0≤q≤L 0
excludes score-dependent stopping within a candidate run, R1
c+ q≤1
finite-sample outcome-adaptive coefficient selection, direct 0
width-N labels, and candidate-level rank–truth measure- Equivalently, with [x] =max(x,0),
+
ments; those can reveal a new direction or require uniform
finite-sample control. The proof is in SI Appendix, Section (cid:26) Z 1 (cid:27)
H (z)= inf λ+[z(0)−λ] +L [z(t)−λ] dt .
S4.6. L + +
λ≥0 0
The exact frontier has a nontrivial phase limit. (27)
4

1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Score percentile u
ytilibaborp
hturT
A Exact blind worlds
1.0
f+ f−
0.8
0.6
0.4
0.2
0.0
100 101 102 103 104 105
Candidates searched, n
etar
hturt
detceleS
B Exact agreement, maximal separation
audited
World +
World -
1.0
0.8
0.6
0.4
0.2
0.0
10−1 100 101
Audit ratio m2/N
htdiw
deifitnedi
esac-tsroW
C The search-validation frontier
101
100
10−1
m=16
m=32
m=64
m=128 10−2
exact phase limit
Legendre witness e−m2/N
10−3
10−1 100
Audit ratio m2/N
L/Δ2m
ytiugibma
dezilamroN
D Monotone smooth worlds remain blind
certified region (m=64)
explicit smooth pair
positive-kernel upper bound
lower limit e−m2/N
Figure 2: Exact and shape-restricted search–validation frontiers. (A) For m=6, complementary Chebyshev-sign reliability
surfaces produce the same first six audited reliabilities. (B) They agree throughout the audited range and then separate maximally.
(C) Finite exact widths collapse under m2/N to the Jacobi-theta frontier; the smooth Legendre witness alone understates unrestricted
ambiguity. (D) Under monotonicity and a Lipschitz bound L, an explicit smooth pair and a positive-polynomial recovery bound
bracket normalized ambiguity. Regularity changes its magnitude to order L/m2 but preserves the degree-squared endpoint-resolution
phase.
Theorem 3 (Exact shape-constrained frontiers). For inte- continuous component with density capped by L. Compact-
gers N >m≥1: measure separation gives Eqs. 28 and 29 without a duality
(i) For monotone reliability, gapandprovesattainment. Bounded-densitymomenttheory
supplies adjacent compact-set characterizations [20, Theo-
∆↑ =2 inf ∥uN −p(u)∥ . (28) rem 3(a–c), pp. 5–6]; the submitted object is the residual
m,N ∞
p∈Pm induced by this audit/deployment pair.
Thustheworstmonotoneworldsmaybechosenasstep
Corollary 2 (Constructive endpoint-resolution bounds).
functions, and the exact validation problem is uniform
Let d=⌊(m−1)/2⌋, let ξ be the largest zero on [0,1] of
monomial approximation rather than the unrestricted d+1
the shifted Legendre polynomial of degree d+1, and put
L1 problem.
(ii) For every 0<L<∞, monotone L-Lipschitz reliabil- (cid:26) 1 L (cid:27) Y m N −j
ity has the exact finite dual A =min , , D = .
m,L m+1 m(m+1) m,N N +j
j=1
∆↑,L = inf {H (z )+H (−z )}. (29) (30)
m,N a∈Rm L a L a
Then
Evaluationthereforereducestothemauditcoefficients
A D ≤∆↑,L ,
and the scalar threshold in Eq. 27. m,L m,N m,N
(cid:26) (cid:18) 1 (cid:19) (cid:27)
The proof represents a monotone law as the distribution ∆↑,L ≤min B ,L 1−ξ + ,1 .
m,N m,N d+1 N +1
function of a subprobability measure. With a Lipschitz
(31)
bound, this measure has a baseline atom and an absolutely
5

If L is fixed and m2/N →τ ∈(0,∞), then For N =100 and 95% confidence, full width 0.10 requires
atleastm=19beforesamplingerrorisconsidered. Ifdirect
m2∆↑,L m2∆↑,L deployment-winner labels are feasible, their structural term
e−τ ≤liminf L m,N ≤limsup L m,N ≤j 0 2 ,1 +τ, (32) iszeroandHoeffding’sinequalitygivestheseparatesufficient
count of 738 independent tasks. When audit and deploy-
where j 0,1 ≃2.4048 is the first positive zero of J 0 . mentkernelsareestimatedratherthanknown,SIAppendix,
Both bounds are constructive. The lower bound builds Section S7.2 adds the explicit penalty δ N +P n |a n |δ n . SI
Appendix, Section S3.3 gives the planning table. These
two smooth monotone worlds from a shifted Legendre poly-
calculations convert the frontier into a choice among three
nomial; the upper bound uses a nonnegative polynomial
noninterchangeable actions: widen the audited search range,
audit concentrated near the endpoint. Their constants do
increase independent task count, or collect labels in the
not match, so Eq. 32 is order-sharp rather than a closed
deployment direction.
form; the exact finite quantity is Eq. 29. This changes the
magnitude of ambiguity to order L/m2 while preserving Retrospective illustrations of the same ge-
the competition between m−2 endpoint resolution and N−1
ometry
deployment concentration (Fig. 2D).
The empirical analyses ask whether changing search width
The dual is numerically accessible rather than only for-
changes the truth target in objective data, whether rever-
mal. With 8,192 percentile bins, floating-point primal and
sals can coexist with favorable mean scaling, and whether
continuum-dual estimates are 0.046130661 and 0.046130667
a realistic audited prefix admits widely separated deploy-
at (m,N,L)=(4,16,1) and 0.020791486 and 0.020791501
ment values. They are mechanism demonstrations in fixed
at (8,64,1). These are agreement diagnostics, not interval-
public populations, not prevalence estimates or prospective
arithmetic-certified enclosures; the rigorous constructive
interventions; SI Appendix, Sections S8–S10, records the
brackets are [0.01409,0.27015] and [0.00449,0.08482]. SI
inferential boundary. The sampling idealization is condi-
Appendix, Section S6 reports convergence, optimizers, and
sensitivity. Because u is percentile rank, L is invariant to tional on task: task t has its own randomized percentile
monotone score transformations, but the audit prefix does and reliability law f t , with θ n,t = R k n f t . Equal-weight
notvalidateit. Adefensibleboundmustcomefromscientific macroaveraginggivesθ n =R k n f forf equaltotheaverage
task law, without treating candidates from different tasks
knowledgeorindependentcandidate-leveldatawithuniform
uncertainty; otherwise the frontier should be reported over
as exchangeable. Every reported best-of-n value is the ex-
act with-replacement maximum-score functional of a fixed
L.
task-specific empirical population. The two domains vary
From geometry to an audit decision output type, verifier construction, truth mechanism, and
The population frontier determines whether a finite audit search range while retaining this iid score-and-select esti-
is worth extending by replication. Let Z ∈ [0,1] be the mand. Treating problems rather than candidate outputs as
i,n
width-noutcomeontaski,withtasksindependentandiden- the independent units, the first analysis uses the two pinned
tically distributed and EZ =θ . For deterministic coeffi- Monkey Business files [21]. Each file contains exactly 127
i,n n
cientsa∈Rm chosenindependentlyoftheseauditoutcomes, GSM8K problem records with 10,000 independently gener-
put s
a
=Pm
n=1
a
n
k
n
and θbN (a)=1/2+P
n
a
n
(Z
n
−1/2).
1
a
2
te
7
d
re
s
c
o
o
lu
rd
ti
s
on
w
s
er
a
e
nd
inc
e
l
x
u
a
d
c
e
t
d
fi
f
n
o
a
r
l-
e
a
a
n
c
s
h
w
m
er
od
co
e
r
l,
re
w
c
i
t
t
n
h
es
n
s
o
la
o
b
u
e
tc
ls
o
;
m
a
e
ll
-
Corollary 3 (Finite-task audit planner). For every a and or completeness-based exclusion (2.54 million candidates in
0<α<1, with probability at least 1−α, total).
For each problem and model, a seeded 2,000-solution ref-
r
1 log(2/α) erencesplitestimatedthefrequencyofeachnormalizedfinal
|θbN (a)−θ
N
|≤
2
∥k
N
−s
a
∥
1
+∥a∥
1 2T
. (33)
answer. That frequency served as a simple consensus score.
A disjoint 8,000-solution deployment split supplied score
The smallest right side over a prespecified coefficient class
ranks and truth labels. We evaluated the empirical best-of-
is a computable bias–noise certificate. As T →∞, twice its
n law exactly for n=1,2,4,...,4096, averaging uniformly
infimum tends to B . Same-sample outcome-dependent
m,N acrosstiedwinningscores. Problem-bootstrapintervalsused
coefficient choice requires sample splitting or uniform con-
20,000 resamples. Ten independent reference/deployment
centration over the searched class.
splits assessed stability.
This yields a two-gate rule. The structural gate asks Consensus ranking was strong on average. Macro within-
whether B ≤ ε; if it fails, no number of additional in- problem AUC was 0.907 (95% bootstrap interval, 0.862–
m,N
dependent tasks and no randomized or sequential schedule 0.947) over the 125 of 127 mixed-label 8B deployment popu-
confined to widths at most m can achieve full width ε. The lations, and 0.962 (0.923–0.990) over the 107 of 127 mixed-
sampling gate is evaluated only after structural breadth is label 70B populations; AUC is undefined for a single-class
adequate; itaskswhetherthecoefficient-amplifiedtaskterm problem. Mean selected truth rose from 0.768 at n=1 to
in Eq. 33 is small enough. Failure there can be repaired by 0.882 at n=4096 for 8B, and from 0.931 to 0.968 for 70B
more independent tasks. A deployment-matched interven- (Fig. 3A). Yet 14 of 127 8B problems and three 70B prob-
tion changes the first gate by adding a new kernel direction lems lost more than one percentage point; worst losses were
rather than merely reducing noise. 0.480 and 0.360 (Fig. 3C). Across 10 splits, the 8B harm
6

count stayed between 13 and 15 and the same three 70B A retrospective masked-label acquisition replay. To
problems were harmed in every split (Fig. 3E). The data do examine the design consequence within the fixed CodeRM
not imply that the extremal Chebyshev worlds are typical. population,wetreatedeverycandidatetruthashiddenuntil
They establish that changing the search kernel changes a selectedbyascore-onlyauditrule. Eachdrawsampledatask
practically relevant reliability target even when aggregate uniformly and then a uniform candidate, a best-of-8 winner,
ranking looks favorable. a randomized top-5% score percentile, or a best-of-100 de-
The independent replication uses 164 HumanEval+ tasks ploymentwinner. Horvitz–Thompsonestimatestargetedthe
from the CodeRM release [22]. For each task and each macro best-of-100 truth. Across 5,000 replayed acquisitions
Llama-3 model, we analyzed 100 candidate programs. The at each budget, 500 uniform labels left 95th-percentile abso-
verifier score is the fraction of 100 CodeRM-8B-generated lute errorsof 0.184 and 0.110 for 8Band 70B; top-tail labels
unit tests passed; correctness is the separate HumanEval+ reduced them to 0.047 and 0.038, and deployment-winner
plus_status label. The task-level analysis therefore con- labels to 0.039 and 0.036 (Fig. 3F). The same top-5% rule,
tains 32,800 programs and 3.28 million candidate–unit-test budgets, and estimator were used for both models without
executions,butinferenceremainsacross164tasks. Exacttie- model-specific retuning. Its observed truncation biases were
averaged best-of-n curves and 20,000 task bootstraps used below 10−4; its distribution-free omitted-mass bound was
the same estimand as the math experiment. All 164 tasks 0.95100 = 0.0059. SI Appendix, Section S9, reports the
contained both truth classes for each model and therefore full budget curves, estimator, and the earlier asymptotic
entered the macro AUCs: 0.931 (0.898–0.959) for 8B and comparison. This is a within-pool estimator comparison on
0.881 (0.818–0.938) for 70B. Mean selected truth rose from public labels, not prospective evidence about intervention
0.536 to 0.715 and from 0.737 to 0.788 between n=1 and effectiveness or realized costs.
100(Fig.3B).Nevertheless,10andfourtaskslostmorethan
one point, with worst losses of 0.722 and 0.600 (Fig. 3D). A frozen-rule held-out test. We then separated design
Thereversalphenomenonthereforesurvivesachangeoftask, choice from evaluation. A seeded, label-blind split assigned
verifier, ground-truth mechanism, and search range. the 164 shared CodeRM tasks to 82 discovery and 82 held-
out tasks. Using discovery outcomes only, we chose among
A retrospective empirical compatibility construction. prespecified 5%, 10%, and 20% score-tail audits by mean
We next asked the same question of the CodeRM data 95th-percentile error across the two models; all three leave
that the theorem asks of an unknown system. Within each at most 0.95100 =0.0059 of target mass unsupported. The
task, tie-group truth was spread uniformly over its score- 5%rulewasselectedandfrozenbeforeeitherheld-outtarget
rank intervals; averaging the 164 task laws reproduces every or error was computed. At 500 labels and 5,000 replays, its
macro best-of-n mean exactly. We then concealed the best- held-out 95th-percentile errors were 0.049 rather than 0.180
of-100 value, retained only the plug-in audits θb1 ,...,θb8 , and under uniform labels for 8B, and 0.035 rather than 0.076 for
optimized θ within the subclass of bounded rank–truth 70B. Held-out absolute biases were below 8×10−5. This
100
laws that are constant on 1,000 percentile bins. result shows that the audit-design choice transferred across
For 8B, the observed best-of-100 truth was 0.715 (95% a task split within CodeRM; because candidates and labels
task-bootstrap interval, 0.650–0.778), while two such laws were already public, it is still retrospective and does not
matching all eight plug-in audits reached 0.186 and 0.992 estimate prospective effect or acquisition cost.
at deployment (SI Appendix, Fig. S1A,C). For 70B, the Table 1 makes the design implication concrete on one
observedvaluewas0.788(0.725–0.847),whilecompatiblewit- fixed target. Extending the prefix from m=8 to 20 sharply
nesses reached 0.305 and 0.996 (SI Appendix, Fig. S1B,D). narrowsthe1,000-binplug-inwitness,yetfinite-taskfeasible
Because every optimizer is a bounded continuum step func- spans remain wide because high-order moment estimation
tion, these separations are genuine feasible witnesses and amplifies noise. Holding the label budget at 500 and mov-
therefore lower bounds on the unrestricted continuum iden- ing acquisition toward the deployment tail instead reduces
tified width; the displayed endpoints are not claimed to held-out replay error by factors 3.67 and 2.15 relative to
solve that unrestricted problem exactly. Orthogonalizing uniform labels. The metrics are not interchangeable and
the same equality row space reduced raw audit residuals be- do not establish a causal ranking of audit programs; to-
low1.3×10−14,andchangingthegridfrom200to1,000bins gether they show why “collect more labels” is incomplete
moved every displayed endpoint by less than 0.007. Allow- without specifying audit breadth, independent units, and
ing 95% simultaneous max-t task-bootstrap bands produced the direction in which labels are collected.
1,000-bin feasible spans [0.003,1.000] and [0.016,1.000]. At Themasked-labelresultisnotatheoremaboutallmodels,
m=20, the corresponding plug-in spans narrowed to 0.047 and importance weighting need not be the preferred estima-
and 0.038, yet the finite-task band spans remained 0.897 tor. Within this fixed public population, it provides a finite,
and 0.803. This is the two-gate distinction in Corollary 3: unit-matched demonstration of the span-design principle:
broaderinterventionsnarrowthestructuralwitness,whereas collecting labels in the deployment direction can dominate
estimated high-order moments can still amplify task noise. replicating labels under a mismatched intervention. The
SI Appendix, Section S10, reports the construction and held-out split strengthens the inference from in-sample fea-
values for m=2 through 20. sibility to transfer across tasks within CodeRM; it does not
establish prospective effectiveness. The complete tables,
formulas, split assignments, CodeRM replication, and recon-
7

Table 1: What changes when the audit follows the best-of-100 target. Thefirsttworowsreportwidthsof1,000-binCodeRM
feasible constructions under simultaneous task bands; they are witnessed lower bounds on unrestricted continuum ambiguity. The last
two report held-out 95th-percentile absolute errors across 5,000 masked-label replays at 500 labels after the tail fraction was selected
on a separate 82-task discovery split. These are different metrics, shown together to separate structural breadth, task precision, and
label direction. The comparison is retrospective, not a prospective cost-effectiveness claim.
Evidencecollected Structuralorsamplingconsequence 8B 70B
Meanprefix,n≤8 B8,100=0.906;constructedtask-bandspan 0.997 0.984
Meanprefix,n≤20 B20,100=0.057;constructedtask-bandspan 0.897 0.803
500held-outuniformlabels Unbiasedimportanceweighting;highweightvariance 0.180 0.076
500held-outfrozentop-5%labels Tail-matched;omittedtargetmass≤0.0059 0.049 0.035
struction procedures are in SI Appendix, Sections S8–S10. data provide construct-level replication and retrospective
held-outmechanismevidenceonlywithiniidscore-and-select.
Discussion
A third domain could extend external validity but would
AI search changes the target that validation must certify.
not verify a distribution-free theorem. Universal guarantees
The span theorem expresses the resulting geometry as the
are intentionally conservative; fixed, independent, or stable
organizing separation
selection may permit narrower inference.
The framework is therefore not an argument against AI
certificate width=structural blindness
search. Searchimprovedmeanaccuracyinbothpublicexper-
+sampling uncertainty.
iments. It is an argument that search changes what must be
The finite best-of-N theorem makes the first term exact: validated. When AI expands the set of selectable decisions
reliability through width m cannot certify deployment be- faster than evaluation expands the span of interventions,
yond Eq. 14, and the same lower bound applies to every apparent precision can grow while scientific identification
randomized or sequential reliability-mean schedule confined deteriorates.
to widths at most m. This is an audit-complexity limit
Code and data availability
rather than a defect of one prefix protocol. Theorem 3
All manuscript source, analysis code, processed data, theo-
shows that the interpretation is not confined to oscillatory
rem checks, optimization outputs, and deterministic figure
Chebyshev worlds: regularity changes the magnitude, but
the competition between m−2 audit resolution and N−1 de- code are available at https://github.com/rfitas-lab/
ployment concentration remains. More data inside the same
geometry-of-ai-validation. Monkey Business genera-
span attack precision but cannot beat its structural floor. A
tionsandlabelsareavailableathttps://huggingface.co/
thousand evaluations produced inside one epistemic frame
datasets/ScalingIntelligence/monkey_business; Co-
deRM programs, annotations, and execution outputs
may therefore constitute one validation intervention.
This changes evaluation practice. The allowable prompts, are linked from https://github.com/RUCKBReasoning/
search budgets, tools, subpopulations, and workflows should
CodeRM. Raw generations, programs, and execution logs
are not redistributed because of their size.
be stated as a deployment family. Uncertainty should cover
that family simultaneously unless selection is demonstra-
bly restricted or stable. New tests should be chosen for Competing interests. Theauthordeclaresnocompeting
interest.
span expansion: ground-truthing winners, near-winners, or
perturbed workflows can be more informative than label-
References
ing more random candidates. In CodeRM, the discovery-
[1] Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster,
selected tail rule retained its advantage after it was frozen
Jeff Clune, and David Ha. The AI scientist: Towards fully
and moved to held-out tasks, a finite check that the design
automatedopen-endedscientificdiscovery.arXiv:2408.06292,
choice was not selected on the evaluation tasks themselves.
2024.
Any smoothness, exchangeability, or tail assumption doing
[2] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao
the extrapolation should be visible and stress-tested.
Tu, Petar Sirkovic, Artiom Myaskovsky, Grzegorz Glowaty,
The span theorem requires a stable reliability surface and
Felix Weissenberger, Alessio Orlandi, Dan Popovici, et al.
known or independently estimated kernels. The closed form
AcceleratingscientificdiscoverywithAIco-scientist. Nature,
further requires iid candidates, scalar ranking, randomized
655:487–496, 2026. doi: 10.1038/s41586-026-10644-y.
ties, maximum selection, and bounded truth; adaptive gen-
eration is outside k (u) = NuN−1 unless its history and [3] Marquita Ellis and Paul Castro. Don’t gamble, GAMBLe:
N
policyaremodeled. Theempiricalworkisequallydelimited: An analytical framework for AI-driven research systems.
arXiv:2606.02863, 2026.
its independent units are 127 problems and 164 tasks, not
millions of within-task outputs or test executions. The com- [4] David L. Donoho. Statistical estimation and optimal re-
patible worlds establish feasibility conditional on the prefix, covery. The Annals of Statistics, 22(1):238–270, 1994. doi:
not probability or prevalence. The held-out split blocks 10.1214/aos/1176325367.
outcome-guideddesignselectionontheevaluationtasks,but
[5] Charles F. Manski. Partial Identification of Probability
the replay still uses existing public candidates and labels
Distributions. Springer, New York, 2003. doi: 10.1007/
ratherthanaprospectiverandomizedintervention. Thusthe b97478.
8

|     |     |     | A  Math: 127 problems |     |     |     | B  Code: 164 tasks |     |     |     | C  Math reversals |     |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | ------------------ | --- | --- | --- | ----------------- | --- | --- | --- | --- |
1.00
|     |     |     |     |     |     | 0.85 |     |     |     |     | Llama-3-8B |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
0.8
|     |     |     |     |     |     | 0.80 |     |     |     |     | Llama-3-70B |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
0.95
0.6
|     | hturt renniw naeM |     |     |     |     | hturt renniw naeM 0.75 |     |     |     | 6904→1 ,hturt Δ |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
0.90
0.4
0.70
0.85
|     |     |     |     |     |     | 0.65 |     |     |     | 0.2 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.80
|     |     |     |     |     |     | 0.60 |     |     |     | 0.0 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.75
|     |     |      |                        |             |     | 0.55 |                      |             |     | −0.2 |                      |                  |         |     |     |
| --- | --- | ---- | ---------------------- | ----------- | --- | ---- | -------------------- | ----------- | --- | ---- | -------------------- | ---------------- | ------- | --- | --- |
|     |     | 0.70 |                        | Llama-3-8B  |     | 0.50 |                      | Llama-3-8B  |     |      |                      |                  |         |     |     |
|     |     |      |                        | Llama-3-70B |     |      |                      | Llama-3-70B |     | −0.4 |                      |                  |         |     |     |
|     |     | 0.65 |                        |             |     | 0.45 |                      |             |     |      |                      |                  |         |     |     |
|     |     | 100  | 101                    | 102         | 103 |      | 100                  | 101         | 102 |      | 0.0 0.2              | 0.4              | 0.6 0.8 | 1.0 |     |
|     |     |      | Candidates searched, n |             |     |      | Programs searched, n |             |     |      |                      | Problem quantile |         |     |     |
|     |     |      | D  Code reversals      |             |     |      | E  Split persistence |             |     |      | F  500 masked labels |                  |         |     |     |
0.200
|     |     |     | Llama-3-8B  |     |     | 16                    |     | Llama-3-8B  |     |                                |     |     | Llama-3-8B  |     |     |
| --- | --- | --- | ----------- | --- | --- | --------------------- | --- | ----------- | --- | ------------------------------ | --- | --- | ----------- | --- | --- |
|     |     | 0.8 |             |     |     | pp 1> demrah smelborP |     | Llama-3-70B |     |                                |     |     | Llama-3-70B |     |     |
|     |     |     | Llama-3-70B |     |     | 14                    |     |             |     | rorre etulosba .tcp-ht59 0.175 |     |     |             |     |     |
0.6
|     | 001→1 ,hturt Δ |     |     |     |     | 12  |     |     |     | 0.150 |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
0.4
|     |     |     |     |     |     | 10  |     |     |     | 0.125 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
0.2
0.100
|     |     | 0.0 |     |     |     | 8   |     |     |     |       |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 6   |     |     |     | 0.075 |     |     |     |     |     |
−0.2
|     |     | −0.4 |     |     |     | 4   |     |     |     | 0.050 |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     |     | −0.6 |     |     |     | 2   |     |     |     | 0.025 |     |     |     |     |     |
|     |     |      |     |     |     | 0   |     |     |     | 0.000 |     |     |     |     |     |
0.0 0.2 0.4 0.6 0.8 1.0 0 1 2 3 4 5 6 7 8 9 Uniform Bo8 Top 5% Bo100
|     |     |     | Task quantile |     |     |     |     | Split |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Figure 3: Search changes reliability in two objective domains. (A) Mean selected truth and 95% problem-bootstrap
intervals across 127 GSM8K problems (2.54 million solutions) under answer-consensus ranking. (B) Independent replication across
164 HumanEval+ tasks (32,800 programs; 3.28 million CodeRM unit-test executions). (C,D) Sorted task-level changes show severe
reversals despite favorable means and high macro AUC. (E) GSM8K harm counts persist across 10 disjoint reference/deployment
splits; macro AUC remains 0.90–0.96. (F) In 5,000 retrospective masked-label replays at a 500-label budget, score-matched CodeRM
auditsreducethe95thpercentileofabsolutebest-of-100estimationerrorrelativetouniformcandidatelabels. Truthisusedonlywhen
| a candidate |     | is sampled; | full | labels score | the emulation |     | afterward. |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | ---- | ------------ | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[6] Richard Berk, Lawrence Brown, Andreas Buja, Kai Zhang, [12] H.A.DavidandJ.Galambos. Theasymptotictheoryofcon-
and Linda Zhao. Valid post-selection inference. The Annals comitants of order statistics. Journal of Applied Probability,
ofStatistics,41(2):802–837,2013. doi: 10.1214/12-AOS1077. 11(4):762–770, 1974. doi: 10.2307/3212559.
|                                    |     |     |     |     |                         |     |     | [13] Nickos | Papadatos. |     | On sequences |     | of expected | maxima | and |
| ---------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | ----------- | ---------- | --- | ------------ | --- | ----------- | ------ | --- |
| [7] TijanaZrnicandMichaelI.Jordan. |     |     |     |     | Post-selectioninference |     |     |             |            |     |              |     |             |        |     |
via algorithmic stability. The Annals of Statistics, 51(4): expected ranges. Journal of Applied Probability, 54(4):1144–
1666–1691, 2023. doi: 10.1214/23-AOS2303. 1166, 2017. doi: 10.1017/jpr.2017.57.
|           |            |     |                    |     |     |               |     | [14] Serge | N.  | Bernstein. | Leçons | sur les | propriétés | extrémales | et  |
| --------- | ---------- | --- | ------------------ | --- | --- | ------------- | --- | ---------- | --- | ---------- | ------ | ------- | ---------- | ---------- | --- |
| [8] Felix | Hausdorff. |     | Summationsmethoden |     | und | momentfolgen. |     |            |     |            |        |         |            |            |     |
II. Mathematische Zeitschrift, 9:280–299, 1921. doi: 10. la meilleure approximation des fonctions analytiques d’une
1007/BF01279032. variable réelle. Gauthier–Villars, Paris, 1926.
[9] HolgerDetteandWilliamJ.Studden.TheTheoryofCanon- [15] Borislav D. Bojanov, Dietrich Braess, and Nira Dyn. Gen-
icalMomentswithApplicationsinStatistics,Probability,and eralized gaussian quadrature formulas. Journal of Ap-
Analysis. Wiley Series in Probability and Statistics. Wiley, proximation Theory, 48(4):335–353, 1986. doi: 10.1016/
0021-9045(86)90008-0.
| New | York, | 1997. | ISBN | 978-0-471-10991-4. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | ----- | ---- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[10] AlanE.Hubbard,SaraKherad-Pajouh,andMarkJ.vander [16] G. A. Watson. Approximation in normed linear spaces.
Laan. Statistical inference for data adaptive target parame- Journal of Computational and Applied Mathematics, 121
|       |     |               |     |            |                |             |     | (1–2):1–36, |     | 2000. doi: | 10.1016/S0377-0427(00)00333-2. |     |     |     |     |
| ----- | --- | ------------- | --- | ---------- | -------------- | ----------- | --- | ----------- | --- | ---------- | ------------------------------ | --- | --- | --- | --- |
| ters. | The | International |     | Journal of | Biostatistics, | 12(1):3–19, |     |             |     |            |                                |     |     |     |     |
2016. doi: 10.1515/ijb-2015-0013. L1-Approximation,volume93ofCam-
|             |        |            |              |                |                |       |             | [17] AllanM.Pinkus. |        | On              |      |                           |     |            |        |
| ----------- | ------ | ---------- | ------------ | -------------- | -------------- | ----- | ----------- | ------------------- | ------ | --------------- | ---- | ------------------------- | --- | ---------- | ------ |
|             |        |            |              |                |                |       |             | bridge              | Tracts | in Mathematics. |      | Cambridge                 |     | University | Press, |
| [11] Joseph |        | B. Kadane. | A            | moment problem | for            | order | statistics. |                     |        |                 |      |                           |     |            |        |
|             |        |            |              |                |                |       |             | Cambridge,          |        | UK, 1989.       | doi: | 10.1017/CBO9780511526497. |     |            |        |
| The         | Annals | of         | Mathematical | Statistics,    | 42(2):745–751, |       | 1971.       |                     |        |                 |      |                           |     |            |        |
doi: 10.1214/aoms/1177693423.
|     |     |     |     |     |     |     |     | [18] J.C.MasonandD.C.Handscomb. |     |               |     |      | Chebyshev  | Polynomials. |          |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | ------------- | --- | ---- | ---------- | ------------ | -------- |
|     |     |     |     |     |     |     |     | Chapman                         |     | and Hall/CRC, |     | Boca | Raton, FL, | 2003.        | doi: 10. |
1201/9781420036114.
9

| [19] E. T. | Whittaker | and | G. N. Watson. | A   | Course | of Modern | URL |     |     |     |     |
| ---------- | --------- | --- | ------------- | --- | ------ | --------- | --- | --- | --- | --- | --- |
https://link.springer.com/article/10.1007/
Analysis. Cambridge University Press, Cambridge, UK, 4 s13171-024-00343-z.
| edition, | 1927. |     |     |     |     |     |             |             |                |                 |     |
| -------- | ----- | --- | --- | --- | --- | --- | ----------- | ----------- | -------------- | --------------- | --- |
|          |       |     |     |     |     |     | [32] Audrey | Huang, Adam | Block, Qinghua | Liu, Nan Jiang, | Ak- |
[20] Jean B. Lasserre. The moment problem with bounded shay Krishnamurthy, and Dylan J. Foster. Is Best-of-N
density. arXiv:math/0607463v2 [math.FA], 2007. URL the best of them? coverage, scaling, and optimality in
https://arxiv.org/abs/math/0607463. inference-time alignment. In Proceedings of the 42nd In-
|     |     |     |     |     |     |     | ternational | Conference | on Machine | Learning, volume | 267 |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---------- | ---------------- | --- |
[21] Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald of Proceedings of Machine Learning Research, pages 25075–
| Clark, | Quoc     | V. Le, Christopher |         | Ré, and   | Azalia  | Mirhoseini. |             |                                        |     |     |     |
| ------ | -------- | ------------------ | ------- | --------- | ------- | ----------- | ----------- | -------------------------------------- | --- | --- | --- |
|        |          |                    |         |           |         |             | 25126,2025. | URLhttps://proceedings.mlr.press/v267/ |     |     |     |
| Large  | language | monkeys:           | Scaling | inference | compute | with        |             |                                        |     |     |     |
huang25c.html.
| repeated              | sampling.   | arXiv:2407.21787,                   |                               | 2024.        |            |           |     |     |     |     |     |
| --------------------- | ----------- | ----------------------------------- | ----------------------------- | ------------ | ---------- | --------- | --- | --- | --- | --- | --- |
| [22] Zeyao            | Ma,         | Xiaokang                            | Zhang,                        | Jing Zhang,  | Jifan      | Yu, Sijia |     |     |     |     |     |
| Luo,                  | and Jie     | Tang. Dynamic                       |                               | scaling of   | unit tests | for code  |     |     |     |     |     |
| rewardmodeling.       |             | InProceedingsofthe63rdAnnualMeeting |                               |              |            |           |     |     |     |     |     |
| of the                | Association | for                                 | Computational                 | Linguistics  |            | (Volume   |     |     |     |     |     |
| 1: Long               | Papers),    | pages                               | 6917–6935,                    | Vienna,      | Austria,   | 2025.     |     |     |     |     |     |
| Association           |             | for Computational                   |                               | Linguistics. | doi:       | 10.18653/ |     |     |     |     |     |
| v1/2025.acl-long.343. |             |                                     | URL https://aclanthology.org/ |              |            |           |     |     |     |     |     |
2025.acl-long.343/.
| [23] Allan       | Pinkus.       | n-Widths | in                              | Approximation | Theory,             | vol-     |     |     |     |     |     |
| ---------------- | ------------- | -------- | ------------------------------- | ------------- | ------------------- | -------- | --- | --- | --- | --- | --- |
| ume7ofErgebnisse |               | der      | Mathematik                      | und           | ihrer Grenzgebiete. |          |     |     |     |     |     |
| Springer,        | Berlin,       | 1985.    | doi: 10.1007/978-3-642-69894-1. |               |                     |          |     |     |     |     |     |
| [24] Donald      | J. Newman     | and      | Theodore                        | J. Rivlin.    | Approxima-          |          |     |     |     |     |     |
| tion             | of monomials  | by       | lower degree                    | polynomials.  |                     | Aequa-   |     |     |     |     |     |
| tiones           | Mathematicae, |          | 14(3):451–455,                  | 1976.         | doi:                | 10.1007/ |     |     |     |     |     |
BF01835995.
| [25] Gábor | Szegő.       | Orthogonal | Polynomials, |               | volume 23      | of Ameri- |     |     |     |     |     |
| ---------- | ------------ | ---------- | ------------ | ------------- | -------------- | --------- | --- | --- | --- | --- | --- |
| can        | Mathematical | Society    | Colloquium   | Publications. |                | Ameri-    |     |     |     |     |     |
| can        | Mathematical | Society,   | Providence,  |               | RI, 4 edition, | 1975.     |     |     |     |     |     |
doi: 10.1090/coll/023.
[26] MohsenHariri,WeicongChen,NahalShahini,VikashSingh,
KaiYe,AmirhosseinSamandar,DebarghaGanguly,Sreehari
| Sankar, | Yanyan | Zhang, | Shouren | Wang, | Jerry Peng, | Biyao |     |     |     |     |     |
| ------- | ------ | ------ | ------- | ----- | ----------- | ----- | --- | --- | --- | --- | --- |
Zhang,MichaelHinczewski,andVipinChaudhary.Test-time
| scaling | in reasoning     | LLMs: | Inference |                        | regimes, | evaluation, |     |     |     |     |     |
| ------- | ---------------- | ----- | --------- | ---------------------- | -------- | ----------- | --- | --- | --- | --- | --- |
| and     | reproducibility, | 2026. | URL       | https://arxiv.org/abs/ |          |             |     |     |     |     |     |
2608.04001.
| [27] Mahmood        | Ettehad                | and                                     | Simon                     | Foucart.        | Instances       | of compu-   |     |     |     |     |     |
| ------------------- | ---------------------- | --------------------------------------- | ------------------------- | --------------- | --------------- | ----------- | --- | --- | --- | --- | --- |
| tational            | optimal                | recovery:                               | Dealing                   | with            | observation     | errors.     |     |     |     |     |     |
| SIAM/ASA            |                        | Journal                                 | on Uncertainty            | Quantification, |                 | 9(4):       |     |     |     |     |     |
| 1438–1456,          |                        | 2021. doi:                              | 10.1137/20M1328476.       |                 |                 |             |     |     |     |     |     |
| [28] Florian        | E.                     | Dorner, Yatong                          | Chen,                     | Andre           | F.              | Cruz, and   |     |     |     |     |     |
| Fanny               | Yang.                  | ROC-n-Reroll:                           |                           | How verifier    | imperfection    |             |     |     |     |     |     |
| affects             | test-time              | scaling.                                | In International          |                 | Conference      | on          |     |     |     |     |     |
| Learning            | Representations,       |                                         | 2026.                     | doi:            | 10.48550/arXiv. |             |     |     |     |     |     |
| 2507.12399.         |                        | URL https://arxiv.org/abs/2507.12399v3. |                           |                 |                 |             |     |     |     |     |     |
| arXiv:2507.12399v3, |                        | revised                                 | 17                        | August          | 2026.           |             |     |     |     |     |     |
| [29] Jason          | Z. Wang.               | The                                     | evaluation                | blind           | spot: A         | stereologi- |     |     |     |     |     |
| cal                 | theory of              | benchmark                               | coverage                  | for large       | language        | mod-        |     |     |     |     |     |
| els.                | arXiv:2606.05169,2026. |                                         | URLhttps://arxiv.org/abs/ |                 |                 |             |     |     |     |     |     |
2606.05169.
| [30] C.L.Mallows.               |              | Boundsondistributionfunctionsintermsof |                                  |                   |                  |            |     |     |     |     |     |
| ------------------------------- | ------------ | -------------------------------------- | -------------------------------- | ----------------- | ---------------- | ---------- | --- | --- | --- | --- | --- |
| expectationsoforder-statistics. |              |                                        |                                  | The Annals        | of Probability,1 |            |     |     |     |     |     |
| (2):297–303,                    |              | 1973. doi:                             | 10.1214/aop/1176996981.          |                   |                  |            |     |     |     |     |     |
| [31] Andrzej                    | Okolewski    | and                                    | Nickos                           | Papadatos.        |                  | Finite se- |     |     |     |     |     |
| quences                         | representing |                                        | expected                         | order statistics. |                  | Sankhy¯a   |     |     |     |     |     |
| A,                              | 86:755–774,  | 2024.                                  | doi: 10.1007/s13171-024-00343-z. |                   |                  |            |     |     |     |     |     |
10

|     |     |     |     |     | Supporting |     |     | Information |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
The geometry of AI validation: Exact certification limits for iid best-of-N search
|     |     |     |     |     |     |     | Ricardo | Fitas |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
This appendix gives complete proofs of the span theorem, post-selection and noisy-capacity results, exact unrestricted
certification frontier, reliability-mean information-maximality result, evidence-specific shape programs, exact worst-evidence
shape duals, constructive endpoint bounds, finite-task planner, and kernel-perturbation result. It derives the scalar-threshold
capped-tail algorithm, Jacobi-theta and fixed-Lipschitz phase laws, reports numerical and Lipschitz-sensitivity checks, states
scope conditions, documents retrospective analyses across 127 mathematical-reasoning problems and 164 code tasks, and
| records     | a concise | contribution |          | boundary. |     |               |     |     |     |     |     |     |     |     |
| ----------- | --------- | ------------ | -------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1. Exact   |           | inverse      | geometry |           |     | of validation |     |     |     |     |     |     |     |     |
| S1.1. Setup |           | and notation |          |           |     |               |     |     |     |     |     |     |     |     |
Let (X,A,µ) be a σ-finite measure space. For ∈L1(µ) and ∈L∞(µ), write
|     |     |     |     |     |     | g   |     | f   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Z
|     |     |     |     |     |     |     | ⟨g,f⟩= | g(x)f(x)dµ(x). |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- |
X
| The admissible |     | reliability | surfaces |     | are |            |     |     |          |              |     |     |     |      |
| -------------- | --- | ----------- | -------- | --- | --- | ---------- | --- | --- | -------- | ------------ | --- | --- | --- | ---- |
|                |     |             |          |     | ={f | ∈L∞(µ):0≤f |     | ≤1  | µ-almost | everywhere}. |     |     |     | (S1) |
F
| Validation | kernels | v   | ,...,v | ∈L1(µ) | define | the | operator |            |       |     |     |     |     |      |
| ---------- | ------- | --- | ------ | ------ | ------ | --- | -------- | ---------- | ----- | --- | --- | --- | --- | ---- |
|            |         | 1   |        | p      |        |     |          |            |       |     |     |     |     |      |
|            |         |     |        |        |        |     | Kf =(⟨v  | ,f⟩,...,⟨v | ,f⟩). |     |     |     |     | (S2) |
|            |         |     |        |        |        |     |          | 1          | p     |     |     |     |     |      |
LetS =span{v }. BecauseS isfinite-dimensional,itisclosedinL1. Atargetkernelk definesR (f)=⟨k,f⟩.
|     |     | ,...,v |     |     |     |     |     |     |     |     |     | ∈L1 |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V   |     | 1      | p   |     | V   |     |     |     |     |     |     |     | k   |     |
The following elementary identity is what makes the unit interval constraint exact rather than merely convenient.
Lemma S1 (Difference set). The set of all differences of two reliability surfaces is the L∞ unit ball:
|     |     |     |     |     |     | {f −g :f,g | ∈F}={h∈L∞ |     | :∥h∥ | ≤1}. |     |     |     | (S3) |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ---- | ---- | --- | --- | --- | ---- |
∞
Every difference lies between −1 and 1. Conversely, for any in the unit ball, =(1+h)/2 and =(1−h)/2
| Proof.          |     |       | f −g    |          |     |     |     |     |     | h   |     | f   | g   |     |
| --------------- | --- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| both belong     | to  | F and | satisfy | f −g     | =h. |     |     |     |     |     |     |     |     | □   |
| S1.2. Proof     | of  | the   | span    | identity |     |     |     |     |     |     |     |     |     |     |
| The annihilator |     | of S  | is      |          |     |     |     |     |     |     |     |     |     |     |
V
|     |     |     |     |     |     | S⊥ ={h∈L∞ | :⟨s,h⟩=0 |     | for every | s∈S | }.  |     |     | (S4) |
| --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | V         |          |     |           |     | V   |     |     |      |
Standard quotient-space duality gives the following exact recovery identity; its statistical optimal-recovery antecedent is
| discussed | by Donoho |     | [4, Secs. | 2–3, | pp.  | 242–259]: |     |       |     |     |          |     |     |      |
| --------- | --------- | --- | --------- | ---- | ---- | --------- | --- | ----- | --- | --- | -------- | --- | --- | ---- |
|           |           |     |           |      | ∥k+S |           | =   | inf   | =   | sup |          |     |     | (S5) |
|           |           |     |           |      |      | V ∥ L1/SV |     | ∥k−s∥ | 1   |     | |⟨k,h⟩|. |     |     |      |
s∈SV
h∈S⊥
V
∥h∥∞≤1
The supremum is attained: apply Hahn–Banach to the one-dimensional span of the coset k+S in L1/S , and represent
|               |         |     |            |     |       |         |        |     |     |     |     | V   | V   |     |
| ------------- | ------- | --- | ---------- | --- | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| the resulting | bounded |     | functional |     | by an | element | of L∞. |     |     |     |     |     |     |     |
If f,g ∈F satisfy Kf =Kg, then h=f−g belongs to S⊥ and has ∥h∥ ≤1. Lemma S1 also shows that every such h is
|              |     |            |      |           |     |       |          | V     |      | ∞       |     |     |     |     |
| ------------ | --- | ---------- | ---- | --------- | --- | ----- | -------- | ----- | ---- | ------- | --- | --- | --- | --- |
| a difference | of  | admissible | f,g. | Therefore |     |       |          |       |      |         |     |     |     |     |
|              |     |            |      |           |     | sup   | |R (f)−R | (g)|= | sup  | |⟨k,h⟩| |     |     |     |     |
|              |     |            |      |           |     |       | k        | k     |      |         |     |     |     |     |
|              |     |            |      |           |     | f,g∈F |          |       | h∈S⊥ |         |     |     |     |     |
V
|     |     |     |     |     |     | Kf=Kg |     |     | ∥h∥∞  | ≤1    |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | ----- | --- | --- | --- | ---- |
|     |     |     |     |     |     |       |     |     | = inf |       |     |     |     | (S6) |
|     |     |     |     |     |     |       |     |     |       | ∥k−s∥ | .   |     |     |      |
1
s∈SV
| This proves | the | sharp-pair-ambiguity |     |     | statement. |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
11

If k ∈S , write k =P a v . Then R (f)=a⊤Kf, so the target is identified. Conversely, if k ∈/ S , the right side of
|     | V   |     | j   | j j | k   |     |     |     |     |     |     | V   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Eq. S6 is positive, and two validation-equivalent worlds have different target values. This proves the if-and-only-if statement.
Assume now that every v and k integrates to one. The constant reliability surface f =1/2 produces the central evidence
|     |     |     | j   |     |     |     |     |     |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Kf = (1/2,...,1/2). Every surface with that evidence can be written as f = (1+h)/2, where h ∈ S⊥ and ∥h∥ ≤ 1.
| 0     |     |     |     |     |     |     |     |     |     |     |     |     | ∞   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hence |     |     |     |     |     |     |     |     |     |     |     | V   |     |
1 1
|     |     |     |     |     |     |     | (f)= | +   |        |     |     |     | (S7) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------ | --- | --- | --- | ---- |
|     |     |     |     |     |     | R   | k    |     | ⟨k,h⟩. |     |     |     |      |
2 2
EquationS5showsthatthesupremumandinfimumare(1±b(k;V))/2. Convexscalingth,0≤t≤1,fillseveryintermediate
| value. | Thus the | central | identified | set | is exactly |                  |     |                  |     |     |     |     |     |
| ------ | -------- | ------- | ---------- | --- | ---------- | ---------------- | --- | ---------------- | --- | --- | --- | --- | --- |
|        |          |         |            |     |            | (cid:20)1−b(k;V) |     | 1+b(k;V)(cid:21) |     |     |     |     |     |
(S8)
|     |     |     |     |     |     |     |     | ,   | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | 2   |     | 2   |     |     |     |     |
This completes the proof of the span identity stated in the main text. □
| S1.3. | Interpretation |     | and | variants |     |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For noncentral evidence, the identified interval can be narrower because the box constraints 0 ≤ f ≤ 1 may bind
asymmetrically. Equation S6 is the largest width over all feasible evidence, and Eq. S8 exhibits evidence at which it is
attained. For an infinite collection of validation kernels, S is replaced by its L1 closure. Signed kernels are allowed; if
V
kernels are not normalized, the same proof holds with the appropriate baseline integrals in Eq. S7.
The metric is forced by the model class rather than selected for convenience: the reliability perturbation is bounded in
L1
L∞, whose dual pairing produces L1 distance. If the admissible surface were restricted by another norm or shape class, the
| corresponding |     | support | function | would | replace | Eq. S5. |     |     |     |     |     |     |     |
| ------------- | --- | ------- | -------- | ----- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
S2. Post-evaluation target selection and simultaneous protection
| S2.1. | Exact | equivalence |     | for a finite | family |     |     |     |     |     |     |     |     |
| ----- | ----- | ----------- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Let W = {1,...,M} and let C (Y) be measurable random confidence sets. Fix a reliability surface f. Define the
w
| simultaneous-coverage |     |     | event |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M
|     |     |     |     |     |     | (Y)= | \   | (f)∈C | (Y)}. |     |     |     | (S9) |
| --- | --- | --- | --- | --- | --- | ---- | --- | ----- | ----- | --- | --- | --- | ---- |
|     |     |     |     |     |     | A    |     | {R    |       |     |     |     |      |
|     |     |     |     |     |     | f    |     | w     | w     |     |     |     |      |
w=1
On Ac, let w (Y) be the smallest index whose confidence set misses R (f); on A , set w (Y)=1. Then
|     | f bf |     |     |     |     |     |       |        | w   | f   | bf  |     |       |
| --- | ---- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | ----- |
|     |      |     |     |     |     |     | (f)∈C | (Y)}=A |     |     |     |     | (S10) |
|     |      |     |     |     |     | {R  |       |        | f . |     |     |     |       |
|     |      |     |     |     |     | wbf |       | wbf    |     |     |     |     |       |
Consequently, if selected-target coverage is at least 1−α for every measurable selector, it is at least 1−α for w , which
bf
implies simultaneous coverage. The converse is immediate because simultaneous coverage implies coverage for any selected
coordinate.
The selector constructed for the proof depends on the fixed data-generating f. That is legitimate because a universal
guarantee quantifies over every selector and every f. It does not imply that an analyst knows f or can implement the
first-failure selector. It shows that no procedure can advertise validity under arbitrary unknown selection while avoiding
the simultaneous event. For countable families the same argument uses the first failing index. For uncountable families,
measurability and separability conditions are needed; one may work with a countable dense subclass when both target and
| confidence | processes |                 | are sample-continuous. |     |         |     |     |     |     |     |     |     |     |
| ---------- | --------- | --------------- | ---------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| S2.2.      | Gaussian  | selected-target |                        |     | example |     |     |     |     |     |     |     |     |
Let Y i ∼ id N(0,1) and z =Φ−1(0.975). Each interval [Y −z,Y +z] covers its fixed target zero with probability 0.95. If
| w       |     |            |          |     |        |      | w         | w   |       |     |     |     |     |
| ------- | --- | ---------- | -------- | --- | ------ | ---- | --------- | --- | ----- | --- | --- | --- | --- |
| =argmax |     | , selected | coverage |     | is     |      |           |     |       |     |     |     |     |
| w b     | w   | Y w        |          |     |        |      |           |     |       |     |     |     |     |
|         |     |            |          |     | P{0∈[Y | −z,Y | +z]}=P{−z |     | ≤maxY | ≤z} |     |     |     |
|         |     |            |          |     |        | wb   | wb        |     |       | w   |     |     |     |
w
|               |     |              |     |          |       |          |     | =Φ(z)M | −Φ(−z)M. |     |     |     | (S11) |
| ------------- | --- | ------------ | --- | -------- | ----- | -------- | --- | ------ | -------- | --- | --- | --- | ----- |
| The two-sided |     | simultaneous |     | critical | value | c solves |     |        |          |     |     |     |       |
M
(cid:20)1+0.951/M(cid:21)
|     |     |     |     | {2Φ(c | )−1}M | =0.95, |     | c   | =Φ−1 |     | .   |     | (S12) |
| --- | --- | --- | --- | ----- | ----- | ------ | --- | --- | ---- | --- | --- | --- | ----- |
|     |     |     |     |       | M     |        |     | M   |      | 2   |     |     |       |
The exact values in the machine-readable table are produced by code/reproduce_geometry_validation.py. The
example isolates stochastic post-selection. It has no structural blind residual because each coordinate is observed directly.
12

Table S1: Selection destroys pointwise Gaussian coverage. Coverage uses the ordinary 95% interval after selecting the largest
| of M independent |     | estimates. |     | Width | inflation | is c | /1.96. |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --- | ----- | --------- | ---- | ------ | --- | --- | --- | --- | --- | --- |
M
|           |              |            |            |          | M           | Selected   | coverage     |     | Simultaneous |     | width inflation |     |     |
| --------- | ------------ | ---------- | ---------- | -------- | ----------- | ---------- | ------------ | --- | ------------ | --- | --------------- | --- | --- |
|           |              |            |            |          | 1           |            | 0.950        |     |              |     | 1.000           |     |     |
|           |              |            |            |          | 5           |            | 0.881        |     |              |     | 1.311           |     |     |
|           |              |            |            |          | 10          |            | 0.776        |     |              |     | 1.428           |     |     |
|           |              |            |            |          | 20          |            | 0.603        |     |              |     | 1.539           |     |     |
|           |              |            |            |          | 50          |            | 0.282        |     |              |     | 1.675           |     |     |
|           |              |            |            |          | 100         |            | 0.080        |     |              |     | 1.772           |     |     |
|           |              |            |            |          | 1,000       | 1.01×10−11 |              |     |              |     | 2.066           |     |     |
|           |              |            |            | 100,000  |             |            | <10−300      |     |              |     | 2.562           |     |     |
| S3. Noisy |              | validation |            | capacity |             | and        | intervention |     | design       |     |                 |     |     |
| S3.1. A   | simultaneous |            | bias–noise |          | certificate |            |              |     |              |     |                 |     |     |
Suppose
|           |        |           |     |      |        | Y =⟨v | ,f⟩+n−1/2ξ |          | ,       | ξ ∼N(0,Σ). |     |     | (S13) |
| --------- | ------ | --------- | --- | ---- | ------ | ----- | ---------- | -------- | ------- | ---------- | --- | --- | ----- |
|           |        |           |     |      |        | j     | j          |          | j       |            |     |     |       |
| For every | target | w, choose |     | ∈Rp, | define |       | =P         | ,        | and set |            |     |     |       |
|           |        |           |     | a w  |        | s w   |            | a wj v j |         |            |     |     |       |
j
1Z
|     |     |     |     |     |     |     | =a⊤ | +   | (k  |     | )dµ. |     | (S14) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----- |
|     |     |     |     |     |     |     | Rbw | Y   |     | −s  |      |     |       |
|     |     |     |     |     |     |     |     | w   | 2   | w w |      |     |       |
Then
|              |     |            |       |     |     |                  |             |      |                   | (cid:28) | 1(cid:29) |     |       |
| ------------ | --- | ---------- | ----- | --- | --- | ---------------- | ----------- | ---- | ----------------- | -------- | --------- | --- | ----- |
|              |     |            |       |     | Rbw | −R               | (f)=n−1/2a⊤ |      | ξ−                | k −s     | ,f − ,    |     | (S15) |
|              |     |            |       |     |     |                  | w           |      | w                 | w        | w 2       |     |       |
| and Hölder’s |     | inequality | gives |     |     |                  |             |      |                   |          |           |     |       |
|              |     |            |       |     |     | (cid:12)(cid:28) |             |      | 1(cid:29)(cid:12) | 1        |           |     |       |
|              |     |            |       |     |     | (cid:12)         |             |      | (cid:12)          |          |           |     | (S16) |
|              |     |            |       |     |     | (cid:12)         | k −s        | ,f − | (cid:12) ≤        | ∥k       | −s ∥ .    |     |       |
|              |     |            |       |     |     | (cid:12)         | w           | w    | 2 (cid:12)        | 2 w      | w 1       |     |       |
Let
|     |     |     |     |     |     |           |     | (cid:26) | (cid:18)   |     | (cid:19) (cid:27) |     |       |
| --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ---------- | --- | ----------------- | --- | ----- |
|     |     |     |     |     | q   | (A,Σ)=inf |     | q :P     | sup|a⊤ξ|≤q |     | ≥1−α              | .   | (S17) |
|     |     |     |     |     | 1−α |           |     |          |            | w   |                   |     |       |
w
Combining Eqs. S15–S17 proves, simultaneously over all targets and all ∈F,
f
|                  |     |          |      |     |     |         |       | 1   |      |       | q (A,Σ) |     |       |
| ---------------- | --- | -------- | ---- | --- | --- | ------- | ----- | --- | ---- | ----- | ------- | --- | ----- |
|                  |     |          |      |     |     |         | (f)|≤ |     |      | +     | 1−α√    |     | (S18) |
|                  |     |          |      |     |     | |Rbw −R | w     | ∥k  | w −s | w ∥ 1 |         |     |       |
|                  |     |          |      |     |     |         |       | 2   |      |       | n       |     |       |
| with probability |     | at least | 1−α. |     |     |         |       |     |      |       |         |     |       |
For a finite family of M targets, if a⊤Σa ≤σ2 for every w, a union bound gives the explicit sufficient value
|     |     |     |     |     | w   | w   | A   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p
|               |     |     |     |     |     |     | q (A,Σ)≤σ        |     | 2log(2M/α). |     |     |     | (S19) |
| ------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --- | --- | --- | ----- |
|               |     |     |     |     |     |     | 1−α              |     | A           |     |     |     |       |
| More sharply, |     | let |     |     |     |     |                  |     |             |     |     |     |       |
|               |     |     |     |     |     |     | G(A,Σ)=Esup|a⊤ξ| |     |             |     |     |     | (S20) |
w
w
be the Gaussian width of the symmetrized coefficient image. Gaussian concentration implies
|     |     |     |     |     |     |       | (A,Σ)≤G(A,Σ)+σ |     |     | p 2log(1/α). |     |     | (S21) |
| --- | --- | --- | --- | --- | --- | ----- | -------------- | --- | --- | ------------ | --- | --- | ----- |
|     |     |     |     |     |     | q 1−α |                |     |     | A            |     |     |       |
The displayed bounds make the two geometries explicit: L1 approximation controls worst-case structural bias, while
| Euclidean/Gaussian |              |     | geometry   | controls |            | noise | amplification.   |               |         |      |                 |      |       |
| ------------------ | ------------ | --- | ---------- | -------- | ---------- | ----- | ---------------- | ------------- | ------- | ---- | --------------- | ---- | ----- |
| One                | may optimize |     | the common |          | half-width |       | over coefficient |               | fields: |      |                 |      |       |
|                    |              |     |            |          |            |       |                 | (cid:13)      |         |      | (cid:13)        |     |       |
|                    |              |     |            |          |            |       |                  | (cid:13)      |         |      | (cid:13)        |      |       |
|                    |              |     |            |          |            |       |                 | 1             | X       |      | q (A            | ,Σ) |       |
|                    |              |     |            |          | (K;V,Σ)=   |       | i n f            | su p (cid:13) |         |      | (cid:13) + 1−α√ |      | (S22) |
|                    |              |     |            | C n,α    |            |       |                  | (cid:13)      | k w −   | a wj | v j (cid:13)    | .    |       |
|                    |              |     |            |          |            |       | { a }            | 2 (cid:13)    |         |      | (cid:13) n      |      |       |
|                    |              |     |            |          |            |       | w               | w (cid:13)    |         | j    | (cid:13)        |     |       |
1
This is a constructive upper bound for universal confidence-band width. As n→∞, the stochastic term disappears and
the infimum of the first term is B(K;V)/2. Equation S6 shows that no honest central-evidence band can have a smaller
worst-case asymptotic half-width. At finite n, minimizing the structural and stochastic terms separately need not be optimal:
| coefficients | that | approximate |     | a target | closely |     | may amplify |     | noise. |     |     |     |     |
| ------------ | ---- | ----------- | --- | -------- | ------- | --- | ----------- | --- | ------ | --- | --- | --- | --- |
13

| S3.2. Adding |     | realizable | interventions |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let D ⊂L1(µ) be the set of feasible new intervention kernels. After choosing q of them, the smallest remaining structural
width is
|     |     |     |     | (K|V,D)= |     |     | inf | supdist | {k,span(S |     |     |        | )}. |     | (S23) |
| --- | --- | --- | --- | -------- | --- | --- | --- | ------- | --------- | --- | --- | ------ | --- | --- | ----- |
|     |     |     |     | d        |     |     |     |         |           |     | ,d  | ,...,d |     |     |       |
|     |     |     |     | q        |     |     |     |         | 1         |     | V   | 1      | q   |     |       |
d1,...,dq∈Dk∈K
Thesequenceisnonincreasinginq andequalszerowhentheaugmentedspancontainseverytargetkernel. IfD permitsevery
q-dimensional extension, Eq. S23 is a relative Kolmogorov-width problem [23]. Real validation design is more constrained: a
signed or oscillatory mathematical direction may not correspond to a population that can be sampled or a workflow that
| can be executed. |     | The dictionary |     | makes | that | constraint |     | explicit. |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | ----- | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Wheninterventionshavedifferentcostsornoisecovariance, Eq.S23shouldbereplacedbythefinite-nobjectiveinEq.S22.
The core qualitative distinction survives: replication changes the noise term, whereas a new kernel can change the closed
span.
| S3.3. A | distribution-free |     |     | finite-task | planner |     |     |     |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The Gaussian model above isolates covariance geometry. For the best-of-N application, a fully explicit task-level certificate
needs only bounded outcomes. Let Z =(Z ,...,Z )∈[0,1]m be independent and identically distributed audit vectors
|     |     |     |     |     | i   | i,1 | i,m |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
across T tasks, with EZ =θ . Dependence among widths within the same task is unrestricted. Fix coefficients a∈Rm
|               |           |              | i,n | n     |           |     |        |          |     |          |          |           |     |     |       |
| ------------- | --------- | ------------ | --- | ----- | --------- | --- | ------ | -------- | --- | -------- | -------- | --------- | --- | --- | ----- |
| independently | of        | the observed |     | audit | outcomes  | and | define |          |     |          |          |           |     |     |       |
|               |           |              |     |       | m         |     |        |          |     | m        | (cid:18) | 1(cid:19) |     |     |       |
|               |           |              |     |       | X         |     |        |          | 1   | X        |          |           |     |     |       |
|               |           |              |     |       | s =       | a k | ,      | θbN (a)= | +   | a        | Z        | −         | .   |     | (S24) |
|               |           |              |     |       | a         | n   | n      |          | 2   |          | n n      | 2         |     |     |       |
|               |           |              |     |       | n=1       |     |        |          |     | n=1      |          |           |     |     |       |
| The same      | centering | identity     | as  | Eq.   | S15 gives |     |        |          |     |          |          |           |     |     |       |
|               |           |              |     |       |           |     | m      |          |     | (cid:28) |          | 1(cid:29) |     |     |       |
|               |           |              |     |       | (a)−θ     | =   | X      | (Z       | )−  |          |          |           |     |     | (S25) |
|               |           |              |     |       | θbN       |     | a      | −θ       |     | k        | −s ,f    | −         | .   |     |       |
|               |           |              |     |       |           | N   | n      | n        | n   | N        | a        | 2         |     |     |       |
n=1
The deterministic term is at most ∥k −s ∥ /2. Across tasks, the scalar a⊤Z has range length at most ∥a∥ , regardless of
|            |       |                  |     |     | N a         | 1          |       |               |     |          | i   |     |     | 1   |       |
| ---------- | ----- | ---------------- | --- | --- | ----------- | ---------- | ----- | ------------- | --- | -------- | --- | --- | --- | --- | ----- |
| dependence | among | its coordinates. |     |     | Hoeffding’s | inequality |       | therefore     |     | gives    |     |     |     |     |       |
|            |       |                  |     |     | ((cid:12)   | m          |       | (cid:12)      | r   | log(2/α) | )   |     |     |     |       |
|            |       |                  |     |     | (cid:12)X   |            |       | (cid:12)      |     |          |     |     |     |     |       |
|            |       |                  |     |     | P (cid:12)  | a          | (Z −θ | )(cid:12)>∥a∥ |     |          |     | ≤α. |     |     | (S26) |
|            |       |                  |     |     | (cid:12)    | n          | n     | n (cid:12)    | 1   | 2T       |     |     |     |     |       |
|            |       |                  |     |     | (cid:12)    |            |       | (cid:12)      |     |          |     |     |     |     |       |
n=1
CombiningthetwotermsgivesthefollowingstandaloneSIfinite-taskcertificate. Thecomputabledistribution-freehalf-width
is
|     |     |     |     |        |      |     | (cid:13)    |     |             | (cid:13)      |     |          |     |     |       |
| --- | --- | --- | --- | ------ | ---- | --- | ----------- | --- | ----------- | ------------- | --- | -------- | --- | --- | ----- |
|     |     |     |     |        |      | (   | 1           | m   |             |               | r   | log(2/α) | )   |     |       |
|     |     |     |     |        |      |     | (cid:13)    | X   |             | (cid:13)      |     |          |     |     |       |
|     |     |     |     | C(m,N) | =    | inf | (cid:13)k   | −   | a k         | (cid:13) +∥a∥ |     |          | .   |     | (S27) |
|     |     |     |     | T,α    |      |     | 2(cid:13) N |     | n n(cid:13) |               | 1   | 2T       |     |     |       |
|     |     |     |     |        | a∈Rm |     | (cid:13)    |     |             | (cid:13)      |     |          |     |     |       |
|     |     |     |     |        |      |     |             | n=1 |             | 1             |     |          |     |     |       |
This is a convex bias–noise tradeoff over outcome-independent coefficients, which may be selected from the known kernels,
T, and α. Choosing the L1-best approximant at finite need not be optimal because its coefficients may amplify noise. If
|     |     |     |     |     |     |     | T   |     |     |     |     |     |     |     | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is chosen after inspecting the same outcomes, Eq. S26 does not by itself protect that choice; one needs sample splitting or
a uniform concentration bound over the searched coefficient class. As ∞, twice Eq. S27 decreases to . Hence
|     |     |     |     |     |     |     |     |     |     | T   | →   |     |     | B m,N |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
B ≤ε is a necessary infinite-task gate for any full-width target ε based only on the prefix.
m,N
If a new audit samples one best-of-N winner per independent task, set the new intervention equal to k . The structural
N
term is zero, the coefficient norm is one, and a full 1−α interval of width at most is guaranteed whenever
ε
2log(2/α)
|     |     |     |     |     |     |     | T   | ≥   |     | .   |     |     |     |     | (S28) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
ε2
Table S2 keeps this sufficient direct-audit calculation separate from the necessary prefix breadth. The prefix column does
not assert that its listed m is sufficient at finite T; remaining sampling error must still fit inside the width budget through
| Eq. S27    | or a covariance-adaptive |     |          | analogue. |        |         |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------------ | --- | -------- | --------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S4. Exact  | best-of-N                |     | frontier |           |        |         |     |     |     |     |     |     |     |     |     |
| S4.1. Rank | normalization            |     |          | and       | winner | kernels |     |     |     |     |     |     |     |     |     |
Let (S,T) be a candidate score and a bounded outcome T ∈ [0,1]. If S has a continuous distribution function F , then
S
U =F (S) is uniform on [0,1]. With score atoms, define the randomized percentile
S
|     |     |     |     | U   | =F (S−)+Z{F |     | (S)−F |     | (S−)}, |     | Z ∼Unif(0,1), |     |     |     | (S29) |
| --- | --- | --- | --- | --- | ----------- | --- | ----- | --- | ------ | --- | ------------- | --- | --- | --- | ----- |
|     |     |     |     |     | S           |     | S     |     | S      |     |               |     |     |     |       |
where is independent. Uniform tie breaking under the original score is equivalent to maximizing U. For an atom whose
Z
score mass occupies a percentile interval I, the independent jitter implies that E(T |U =u) is constant for almost every
14

Table S2: Finite certificate planning for N =100 and 95% confidence. Minimum m is necessary even with infinitely many
tasks. Thedirect-winnertaskcountisaseparatesufficientHoeffdingdesign. Exactvaluesareinresults/certificate_planning.csv.
|     |     |     | Desired |     | full width | Minimum |     | m B | Direct-winner |     | tasks |     |
| --- | --- | --- | ------- | --- | ---------- | ------- | --- | --- | ------------- | --- | ----- | --- |
m,100
|     |     |     |     |     | 0.50 |     |     | 13 0.446 |     |     | 30    |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | -------- | --- | --- | ----- | --- |
|     |     |     |     |     | 0.25 |     |     | 16 0.213 |     |     | 119   |     |
|     |     |     |     |     | 0.20 |     |     | 17 0.159 |     |     | 185   |     |
|     |     |     |     |     | 0.10 |     |     | 19 0.082 |     |     | 738   |     |
|     |     |     |     |     | 0.05 |     |     | 21 0.039 |     |     | 2,952 |     |
u∈I. Thus a known atomic score distribution adds interval-constancy restrictions to the reliability class. The unrestricted
frontier below ranges over the stated model class and remains exact because its extremal joint laws may use a continuous
score. Conditioning on a particular atomic score law can only narrow that frontier; the empirical programs in Sections
| S8–S10 | preserve | the observed | tie | intervals | explicitly. |     |     |     |     |     |     |     |
| ------ | -------- | ------------ | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
For iid candidates, the maximum percentile has distribution function and density
| n   |     |     |     |     |     |     |              |     | un  |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     | k (u)=nun−1. |     |     |     |     | (S30) |
n
| If f(u)=E(T |     | =u), | the selected |     | mean | is  |     |     |     |     |     |     |
| ----------- | --- | ---- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|U
Z
1
|     |     |     |     |     |     | θ   | = k | (u)f(u)du. |     |     |     | (S31) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ----- |
|     |     |     |     |     |     | n   |     | n          |     |     |     |       |
0
The first m kernels span P because nonzero scalar multiples do not change span.
m−1
| S4.2. A | Chebyshev-sign |              | annihilator |     |            |     |            |       |     |     |     |     |
| ------- | -------------- | ------------ | ----------- | --- | ---------- | --- | ---------- | ----- | --- | --- | --- | --- |
| Let U   | (x) be         | the degree-m | Chebyshev   |     | polynomial | of  | the second | kind, |     |     |     |     |
m
sin{(m+1)θ}
|     |     |     |     |     |     | U (cosθ)= |     |      | ,   |     |     | (S32) |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---- | --- | --- | --- | ----- |
|     |     |     |     |     |     | m         |     | sinθ |     |     |     |       |
and define
|     |     |     |     |     |     | (u)=sgnU |     | (2u−1). |     |     |     | (S33) |
| --- | --- | --- | --- | --- | --- | -------- | --- | ------- | --- | --- | --- | ----- |
σ
|           |     |     |     |     |     | m   |     | m   |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Its roots | are |     |     |     |     |     |     |     |     |     |     |     |
1+cos{jπ/(m+1)}
|       |           |                |     |     | u =   |            |      | ,   | j =1,...,m. |     |     | (S34) |
| ----- | --------- | -------------- | --- | --- | ----- | ---------- | ---- | --- | ----------- | --- | --- | ----- |
|       |           |                |     |     | j     |            | 2    |     |             |     |     |       |
| Lemma | S2 (Exact | annihilation). |     | For | every | polynomial | q ∈P | ,   |             |     |     |       |
m−1
Z 1
|     |     |     |     |     |     |     | q(u)σ | (u)du=0. |     |     |     | (S35) |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | ----- |
m
0
| Proof. Set | 2u−1=cosθ. |     | Up to | a constant |     | factor, the    | integral | is                |     |     |     |       |
| ---------- | ---------- | --- | ----- | ---------- | --- | -------------- | -------- | ----------------- | --- | --- | --- | ----- |
|            |            |     |       |            | Z π | (cid:18)1+cosθ | (cid:19) |                   |     |     |     |       |
|            |            |     |       |            |     |                | sinθ     | sgnsin{(m+1)θ}dθ. |     |     |     | (S36) |
q
2
0
The factor q((1+cosθ)/2)sinθ is a finite linear combination of sin(ℓθ) for 1 ≤ ℓ ≤ m. In L2(0,π), the square wave
sgnsin{(m+1)θ} has a sine series containing only frequencies (2r+1)(m+1), ≥0. Orthogonality of the sine basis makes
r
Eq. S36 zero. Values at the finitely many roots do not affect the integral. □
| S4.3. C0: | classical |     | L1 approximation |     |     | input |     |     |     |     |     |     |
| --------- | --------- | --- | ---------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
The canonical points for polynomial L1 approximation—the roots of the Chebyshev polynomial of the second kind—date
to Bernstein. The canonical-point, generalized-quadrature, and orthogonal-signature framework is treated explicitly by
Bojanov, Braess, and Dyn [15, pp. 335–353]; broader L1 characterizations are reviewed by Watson [16, pp. 1–15]. The
calculation below is therefore a direct specialization, not a claim to a new best-approximation theorem. This subsection
ends exactly where the classical input ends: with the best approximant, its error sign, and its distance.
Let N >m and let p be the unique polynomial of degree at most m−1 interpolating k (u)=NuN−1 at the nodes
|             |     |                    | m−1 |           |     |     |     |     |     |     | N   |     |
| ----------- | --- | ------------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| in Eq. S34. | The | divided-difference |     | remainder |     | is  |     |     |     |     |     |     |
m
Y
|     |     |     |     |     | k (u)−p | (u)=k |     | [u ,...,u | ,u] (u−u | ).  |     | (S37) |
| --- | --- | --- | --- | --- | ------- | ----- | --- | --------- | -------- | --- | --- | ----- |
|     |     |     |     |     | N       | m−1   | N   | 1 m       |          | j   |     |       |
j=1
15

Themthderivativeofk ispositiveon(0,1], sothedivideddifferenceispositivealmosteverywhere. TheproductinEq.S37
N
| is a positive | multiple | of  | (2u−1). |     | Therefore |     |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
U m
|         |      |         |     | sgn{k  | (u)−p           |     | (u)}=σ     | (u) | almost | everywhere. |     |     |     | (S38) |
| ------- | ---- | ------- | --- | ------ | --------------- | --- | ---------- | --- | ------ | ----------- | --- | --- | --- | ----- |
|         |      |         |     |        | N               | m−1 |            | m   |        |             |     |     |     |       |
| For any | q ∈P | , Lemma |     | S2 and | the subgradient |     | inequality |     | give   |             |     |     |     |       |
m−1
Z 1
|     |     |     |     |      | −(p +q)∥ |     |     | (u){k | (u)−p |     | (u)−q(u)}du |     |     |     |
| --- | --- | --- | --- | ---- | -------- | --- | --- | ----- | ----- | --- | ----------- | --- | --- | --- |
|     |     |     |     | ∥k N | m−1      | 1   | ≥ σ | m     | N     | m−1 |             |     |     |     |
0
Z
1
|     |     |     |     |     |     |     | = |k | (u)−p |     | (u)|du. |     |     |     | (S39) |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | ------- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     |      | N     | m−1 |         |     |     |     |       |
0
| Thus | is an | L1 best | approximant. |     | Moreover, |     |     |     |     |     |     |     |     |     |
| ---- | ----- | ------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p m−1
Z 1
|     |     |     |     |     | dist | (k ,P |     | )=  | k (u)σ | (u)du, |     |     |     | (S40) |
| --- | --- | --- | --- | --- | ---- | ----- | --- | --- | ------ | ------ | --- | --- | --- | ----- |
|     |     |     |     |     |      | 1 N   | m−1 |     | N      | m      |     |     |     |       |
0
because both p and every other lower-degree polynomial are annihilated by σ .
|     | m−1 |     |     |     |     |     |     |     |     |     | m   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To evaluate Eq. S40, integrate over the alternating intervals between roots. Because Ra (u)du=aN and the sign is
|     |     |     |     | k N |     |     |     |     |     |     |     | k N |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
| positive | next to | u=1, | telescoping |     | gives |     |         |                         |     |     |           |     |     |     |
| -------- | ------- | ---- | ----------- | --- | ----- | --- | ------- | ----------------------- | --- | --- | --------- | --- | --- | --- |
|          |         |      |             |     |       |     | m       | (cid:20)1+cos{rπ/(m+1)} |     |     | (cid:21)N |     |     |     |
|          |         |      |             |     | =1+2  |     | X (−1)r |                         |     |     |           |     |     |     |
B
|     |     |     |     |     | m,N |     |     |     |     | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r=1
|     |     |     |     |     |      |     | m          |     | (cid:26) | (cid:27) |     |     |     |       |
| --- | --- | --- | --- | --- | ---- | --- | ---------- | --- | -------- | -------- | --- | --- | --- | ----- |
|     |     |     |     |     |      |     | X          |     | rπ       |          |     |     |     |       |
|     |     |     |     |     | =1+2 |     | (−1)rcos2N |     |          |          | .   |     |     | (S41) |
2(m+1)
r=1
| This proves  | the | distance            | formula. |     |               |     |             |     |     |     |     |     |     |     |
| ------------ | --- | ------------------- | -------- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| S4.4. V1–V2: |     | bounded-reliability |          |     | certification |     | consequence |     |     |     |     |     |     |     |
The statistical object begins here. The approximation result in Section S4.3 does not by itself specify a feasible bounded
reliability model, a common audit vector, an identified set, or a minimax statement over such sets. Those are the additional
| claims proved | next. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Define complete binary joint laws P by U ∼Unif(0,1) and T |U =u∼Bernoulli{f (u)}, where f =(1±σ )/2,
|     |     |     |     |     | ±   | ±   |     |     | ± ± |     |     | ±   | ±   | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and take candidate sequences iid under each law. For every n≤m, , so Lemma S2 gives
|     |     |     |     |     |     |     |     |     | k n ∈P | m−1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
Z
|     |     |     |     |     |       |     | 1   |     |     |     | 1   |     |     |       |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |     | θ+−θ− | =   | k σ | =0, | θ+  | =θ− | = . |     |     | (S42) |
|     |     |     |     |     | n     | n   | n   | m   | n   | n   | 2   |     |     |       |
0
| At N, Eq. | S40 gives |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1±B
|     |     |     |     |     |     |     | θ± = |     | m,N. |     |     |     |     | (S43) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     | N    | 2   |      |     |     |     |     |       |
For every λ∈[0,1], the joint law with ∼Unif(0,1) and =u∼Bernoulli{λf (u)+(1−λ)f (u)} is again a valid
|     |     |     |     |     | U   |     |     | T |U |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |      |     |     | +   | −   |     |     |
iid candidate world, has every audited reliability equal to 1/2, and fills the entire interval between the two deployment
endpoints. The exact span identity says no validation-equivalent pair can be separated by more than the L1 distance. Thus
the central identified set is exactly [(1−B )/2,(1+B )/2], not merely a pair of separated witnesses. If N ≤m, k
|         |           |     |     |          | m,N      |     |     | m,N |     |     |     |     |     | N   |
| ------- | --------- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| already | lies in P | and | the | distance | is zero. |     |     |     |     |     |     |     |     | □   |
m−1
| S4.5. Why | Chebyshev |     | improves |     | the orthogonal-polynomial |     |     |     | witness |     |     |     |     |     |
| --------- | --------- | --- | -------- | --- | ------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
A shifted Legendre polynomial L also annihilates P and satisfies ∥L ∥ ≤1. It produces the valid gap
|     |     |     |     | m   |     |     | m−1   |        |     | m ∞ |     |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     | Z 1   |        |     | m   |     |     |     |       |
|     |     |     |     |     |     |     |       |        |     | Y N | −j  |     |     |       |
|     |     |     |     |     | D   | =N  | uN−1L | (u)du= |     |     | .   |     |     | (S44) |
|     |     |     |     |     | m,N |     |       | m      |     | N   | +j  |     |     |       |
0
j=1
Therefore D ≤ B . The Legendre construction is smooth and convenient, but it is not generally extremal for the
|     | m,N | m,N |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L1/L∞ geometry. The exact dual extremizer is the discontinuous sign of , and the exact primal solution interpolates at
U m
the roots of U . This distinction converts a lower-bound scale into a solved minimax frontier.
m
| S4.6. Optimality |     | among |     | low-width | reliability-mean |     |     | audits |     |     |     |     |     |     |
| ---------------- | --- | ----- | --- | --------- | ---------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Let an admissible audit kernel be any randomized mixture of best-of-n winner kernels with n≤m,
|     |     |     |     |     |        | m   |        |     |     | m   |     |     |     |       |
| --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |        | X   |        |     |     | X   |     |     |     |       |
|     |     |     |     |     | a (u)= | q   | k (u), | q   | ≥0, | q   | =1. |     |     | (S45) |
|     |     |     |     |     | ℓ      | ℓn  | n      |     | ℓn  |     | ℓn  |     |     |       |
|     |     |     |     |     |        | n=1 |        |     |     | n=1 |     |     |     |       |
16

If the budget realization is retained, the audit reveals a subset or linear combination of the individual θ ; if it is not retained,
n
it reveals the mixture mean ,f⟩. In either case every revealed kernel lies in . For a finite audit family A, put
|           |      |        |          | ⟨a ℓ |       |           |            |        |            | P     | m−1 |     |       |
| --------- | ---- | ------ | -------- | ---- | ----- | --------- | ---------- | ------ | ---------- | ----- | --- | --- | ----- |
| S =span{a |      | :ℓ∈A}. | Equation | S6   | gives | the exact | worst-case |        | separation |       |     |     |       |
| A         | ℓ    |        |          |      |       |           |            |        |            |       |     |     |       |
|           |      |        |          |      |       | ∆         | (k         | )=dist | (k         | ,S ). |     |     | (S46) |
|           |      |        |          |      |       |           | A N        |        | 1 N        | A     |     |     |       |
| Because   | S ⊆P | ,      |          |      |       |           |            |        |            |       |     |     |       |
A m−1
|              |        |     |                  |     |         | ∆ (k   | )≥dist | (k  |        | )=B   |     |     | (S47) |
| ------------ | ------ | --- | ---------------- | --- | ------- | ------ | ------ | --- | ------ | ----- | --- | --- | ----- |
|              |        |     |                  |     |         | A N    |        | 1 N | ,P m−1 | m,N . |     |     |       |
| The complete | prefix |     | attains equality |     | because | span{k | ,...,k |     | }=P    | .     |     |     |       |
|              |        |     |                  |     |         |        | 1      | m   | m−1    |       |     |     |       |
The same conclusion holds for an adaptive population-mean query rule that selects its next q after observing earlier
ℓ
reliability means, while every query remains in Eq. S45. Under the endpoint worlds , every such query returns
f
±
m
|     |     |     |     |     |     |       |      |       | X   | 1 1   |     |     |       |
| --- | --- | --- | --- | --- | --- | ----- | ---- | ----- | --- | ----- | --- | --- | ----- |
|     |     |     |     |     |     | ⟨a ,f | ⟩=⟨a | ,f ⟩= |     | q = . |     |     | (S48) |
|     |     |     |     |     |     | ℓ +   |      | ℓ −   |     | ℓn2 2 |     |     |       |
n=1
The two worlds therefore generate the same population transcript under any such rule while remaining separated by B
m,N
at deployment. This proves the low-width inclusion statement in the main text. The restriction is essential. Score-dependent
within-runstopping,finite-sampleoutcome-adaptivecoefficientchoice,anarbitraryselected-statekernelmerelyconstrainedto
generateatmostmcandidates,directwidth-N labels,candidate-levelrank–truthobservations,oranotherinterventionkernel
need not have the form in Eq. S45 and either needs separate protection or can enlarge the span. The mathematical step is
span inclusion; the validation consequence is that knowing the complete low-width prefix is a favorable, information-maximal
benchmark within this precisely stated mean-query class rather than a weak audit schedule. □
| S5. Jacobi-theta |     |     | phase | transition |     | and | audit | law |     |     |     |     |     |
| ---------------- | --- | --- | ----- | ---------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Set τ =m2/N and assume m,N →∞ with τ →τ ∈(0,∞). For each fixed r,
| m,N |     |     |     |       |          |        | m,N      |          |          |             |                  |     |     |
| --- | --- | --- | --- | ----- | -------- | ------ | -------- | -------- | -------- | ----------- | ---------------- | --- | --- |
|     |     |     |     |       | (cid:26) | rπ     | (cid:27) | (cid:20) |          | (cid:26) rπ | (cid:27)(cid:21) |     |     |
|     |     |     |     | cos2N |          |        |          | =exp     | 2Nlogcos |             |                  |     |     |
|     |     |     |     |       |          | 2(m+1) |          |          |          | 2(m+1)      |                  |     |     |
(cid:18) π2r2(cid:19)
|     |     |     |     |     |     |     |     | −→exp | −   | .   |     |     | (S49) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ----- |
4τ
To justify passage through the growing sum, define = m}cos2N{rπ/[2(m+1)]} for every 1. Because
|     |     |     |     |     |     |     | a   |     | 1{r ≤ |     |     | r ≥ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
m,N,r
N/(m+1)2 →1/τ, for all sufficiently large m, N/(m+1)2 ≥1/(2τ). The elementary inequality cosx≤e−x2/2 on [0,π/2]
| then gives, | uniformly |     | over every | ≥1, |     |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r
(cid:18) π2r2(cid:19)
|     |     |     |     |     |     | 0≤a |       | ≤exp | −   | .   |     |     | (S50) |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     | m,N,r |      |     | 8τ  |     |     |       |
The right side is summable on the positive integers, while Eq. S49 gives pointwise convergence for each fixed r. Dominated
| convergence | on  | counting | measure | therefore |       | yields |                    |     |     |                |          |     |       |
| ----------- | --- | -------- | ------- | --------- | ----- | ------ | ------------------ | --- | --- | -------------- | -------- | --- | ----- |
|             |     |          |         |           |       |        | ∞                  |     |     | (cid:16)       | (cid:17) |     |       |
|             |     |          |         |           | −→1+2 |        | X (−1)re−π2r2/(4τ) |     |     | =ϑ 0,e−π2/(4τ) |          |     | (S51) |
|             |     |          |         | B         |       |        |                    |     |     |                | .        |     |       |
|             |     |          |         | m,N       |       |        |                    |     |     | 4              |          |     |       |
r=1
| Jacobi’s        | imaginary |       | transformation |     | states            |                 |                |     |            |     |     |     |       |
| --------------- | --------- | ----- | -------------- | --- | ----------------- | --------------- | -------------- | --- | ---------- | --- | --- | --- | ----- |
|                 |           |       |                |     |                   | (0,e−πt)=t−1/2ϑ |                |     | (0,e−π/t). |     |     |     | (S52) |
|                 |           |       |                |     |                   | ϑ 4             |                |     | 2          |     |     |     |       |
| Taking t=π/(4τ) |           | gives | the positive,  |     | cancellation-free |                 | representation |     |            |     |     |     |       |
|                 |           |       |                |     |                   |                 |                | r   | ∞          |     |     |     |       |
τ X
|     |     |     |     |     |     | B(τ)=4 |     |     | e−τ(2j+1)2 | .   |     |     | (S53) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---------- | --- | --- | --- | ----- |
π
j=0
| The first    | representation |     | immediately |     | gives, | as τ ↓0,                     |     |     |     |     |     |     |       |
| ------------ | -------------- | --- | ----------- | --- | ------ | ---------------------------- | --- | --- | --- | --- | --- | --- | ----- |
|              |                |     |             |     |        | B(τ)=1−2e−π2/(4τ)+O(e−π2/τ). |     |     |     |     |     |     | (S54) |
| The positive | representation |     | gives,      | as  | →∞,    |                              |     |     |     |     |     |     |       |
τ
|               |     |        |        |          |     | B(τ)=4   | p         | τ/πe−τ{1+O(e−8τ)}. |     |     |     |     | (S55) |
| ------------- | --- | ------ | ------ | -------- | --- | -------- | --------- | ------------------ | --- | --- | --- | --- | ----- |
| The inversion |     | is now | stated | only for | the | limiting | frontier. | Define             |     |     |     |     |       |
|               |     |        |        |          |     | τ        | =inf{τ    | >0:B(τ)≤ε}.        |     |     |     |     | (S56) |
ε
17

Let L=log(1/ε). The large-τ expansion in Eq. S55 implies that inverting the leading relation
p
4 τ/πe−τ =ε (S57)
gives the asymptotics of τ . Taking logarithms yields
ε
1 4
τ =L+ logτ +log√ . (S58)
2 π
Since τ/L→1, one substitution yields
1 4
τ =L+ logL+log√ +o(1), (S59)
2 π
which proves the audit law in the main text. The order of limits is essential: for each fixed τ, first take m,N → ∞
with m2/N → τ to obtain B(τ); only then let ε ↓ 0 and invert that limiting frontier. The result does not assert that
B =B(m2/N)+o(1) uniformly over a diverging phase coordinate, and hence does not cover an arbitrary joint sequence
m,N
ε = ε without an additional uniform remainder theorem. If the desired worst-case absolute error is δ rather than full
N
interval width ε, use ε=2δ within the same iterated regime.
For comparison, Eq. S44 satisfies
m
X
logD = {log(1−j/N)−log(1+j/N)}=−m(m+1)/N +o(1), (S60)
m,N
j=1
so D →e−τ. It gets the exponential order in the well-audited regime but not the exact prefactor or the under-audited
m,N
frontier. For example, B(1)≈0.8305, whereas e−1 ≈0.3679.
S6. Shape-constrained validation frontier
This section removes the unrestricted Chebyshev construction from the critical path. We derive the exact ambiguity for
monotone reliability, an exact convex dual when monotonicity is combined with a Lipschitz bound, and matching-order lower
and upper bounds. The techniques are classical measure representation, linear-programming duality, orthogonal polynomials,
and Gauss quadrature; the resulting capped-tail validation dual and endpoint-resolution law are the contribution.
S6.1. Evidence-specific programs and the worst-evidence frontier
The main-text quantities ∆G are maxima over all feasible audit evidence. They are design guarantees, not the identified
m,N
width for every realized audit vector. Put b (t)=1−tn. For a feasible population audit vector y =(y ,...,y ), the exact
n 1 m
monotone identified set is
(cid:26)Z Z (cid:27)
I (y)= b dα:α≥0, α([0,1])≤1, b dα=y (n≤m) . (S61)
↑ N n n
For 0<L<∞, the exact monotone-Lipschitz identified set is
(cid:26) Z 1 Z 1
I (y)= c+ b (t)q(t)dt:c≥0, 0≤q ≤L, c+ q ≤1,
↑,L N
0 0
Z 1 (cid:27)
c+ b (t)q(t)dt=y (n≤m) . (S62)
n n
0
Both are compact intervals whenever feasible; minimizing and maximizing the displayed target gives their endpoints. Their
diameters are bounded above by the corresponding worst-evidence frontiers, with equality for at least one feasible y by
compactness of the pair program. If audit means are known only within simultaneous confidence bands, replacing each
equality by its band gives a valid finite-sample outer program. Sampling coverage is then a separate layer and is not supplied
by the population frontiers themselves.
Lemma S3 (No duality gap for the equality-constrained measure programs). Take a compact Hausdorff space X and
view the finite signed regular Borel measures as M(X)=C(X)∗ with the weak-star topology. Let K⊂M(X) be nonempty,
convex, and weak-star compact, and let b ,b ,...,b ∈C(X). Writing C =K−K and h (z)=sup R zdµ, one has
0 1 m K µ∈K
Z
sup b dν
0
ν∈C
R
bjdν=0, j=1,...,m
    
 X m X m 
= inf h Kb 0 − a j b j +h K−b 0 + a j b j . (S63)
a∈Rm 
j=1 j=1
Because C is symmetric, the left side also equals the largest absolute separation subject to the equality constraints.
18

Proof. The difference set C is convex, symmetric, and weak-star compact. Both
|     |     |     |     |     | (cid:18)Z |           | Z   | (cid:19) |         | Z   |      |     |     |
| --- | --- | --- | --- | --- | --------- | --------- | --- | -------- | ------- | --- | ---- | --- | --- |
|     |     |     |     | Aν  | =         | b dν,..., |     | b dν     | , c(ν)= |     | b dν |     |     |
|     |     |     |     |     |           | 1         |     | m        |         |     | 0    |     |     |
are weak-star continuous. Consequently G={(Aν,c(ν)):ν ∈C}⊂Rm+1 is compact and convex, and =AC is compact,
D
convex, and symmetric. Symmetry implies 0 ∈ riD, where relative interior is taken in affD; this also covers linearly
| dependent | moment | coordinates. |     |     |     |                 |     |     |         |     |     |     |     |
| --------- | ------ | ------------ | --- | --- | --- | --------------- | --- | --- | ------- | --- | --- | --- | --- |
| For       | x∈D,   | define       |     |     |     |                 |     |     |         |     |     |     |     |
|           |        |              |     |     |     | ϕ(x)=max{c(ν):ν |     | ∈C, | Aν =x}. |     |     |     |     |
The maximum exists because each fiber is compact. Compactness of makes upper semicontinuous, and convexity of
|     |     |     |     |     |     |     |     |     | G   | ϕ   |     |     | G   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
makes ϕ concave. A finite concave upper-semicontinuous function has a supergradient at every relative-interior point of its
| domain. | Thus | there is an | a on | affD (extended |     | arbitrarily    |     | to Rm) | such that |     |     |     |     |
| ------- | ---- | ----------- | ---- | -------------- | --- | -------------- | --- | ------ | --------- | --- | --- | --- | --- |
|         |      |             |      |                |     | ϕ(x)≤ϕ(0)+a⊤x, |     |        | x∈D.      |     |     |     |     |
Writing v =ϕ(0), this inequality says c(ν)−a⊤Aν ≤v for every ν ∈C. A maximizer in the fiber Aν =0 gives equality, so
|     |     |     |     |     |     | maxc(ν)= | inf     | sup{c(ν)−a⊤Aν}. |     |     |     |     | (S64) |
| --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     | ν∈C      | a∈Rmν∈C |                 |     |     |     |     |       |
Aν=0
There is therefore no duality gap and the primal maximum is attained. Finally, h (z)=h (z)+h (−z) gives Eq. S63;
|     |     |     |     |     |     |     |     |     |     |     | K−K | K K |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
symmetry of converts the one-sided maximum to the largest absolute separation. □
C
| S6.2. | Exact | worst-evidence |     | frontier | under | monotonicity |     |     |     |     |     |     |     |
| ----- | ----- | -------------- | --- | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Let be the nondecreasing measurable functions :[0,1]→[0,1], with changes on null sets ignored, and define
| F   | ↑   |     |     |     |      | f      |           |             |                    |     |            |     |       |
| --- | --- | --- | --- | --- | ---- | ------ | --------- | ----------- | ------------------ | --- | ---------- | --- | ----- |
|     |     |     |     |     |      |        |           | (cid:12)Z 1 |                    |     | (cid:12)   |     |       |
|     |     |     |     |     |      |        |           | (cid:12)    |                    |     | (cid:12)   |     |       |
|     |     |     |     | ∆↑  | =    | sup    |           | (cid:12)    | k (u){f(u)−g(u)}du |     | (cid:12) . |     | (S65) |
|     |     |     |     | m,N |      |        |           |             | N                  |     |            |     |       |
|     |     |     |     |     |      | f,g∈F↑ |           | (cid:12) 0  |                    |     | (cid:12)   |     |       |
|     |     |     |     |     | R    | R      |           |             |                    |     |            |     |       |
|     |     |     |     |     | knf= | kng,   | n=1,...,m |             |                    |     |            |     |       |
Every right-continuous representative of f ∈ F is the distribution function of a subprobability measure α on [0,1]:
↑
f(u)=α([0,u]). A jump at u=1 changes the function only on a null set. Equivalently, its atom at t=1 may be retained to
keep the subprobability set weak-star compact: every audit and target integrand 1−tn vanishes there, so the atom changes
| neither | constraints | nor objective. |     | Fubini’s | theorem |              | gives |     |              |     |     |     |       |
| ------- | ----------- | -------------- | --- | -------- | ------- | ------------ | ----- | --- | ------------ | --- | --- | --- | ----- |
|         |             |                |     |          |         | Z 1          |       |     | Z            |     |     |     |       |
|         |             |                |     |          | (f)=    | nun−1f(u)du= |       |     | (1−tn)α(dt). |     |     |     | (S66) |
θ n
|                  |     |             |     |        |     | 0   |     |     | [0,1] |     |     |     |     |
| ---------------- | --- | ----------- | --- | ------ | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
| For coefficients |     | a=(a ,...,a |     | ), set |     |     |     |     |       |     |     |     |     |
|                  |     | 1           | m   |        |     |     |     |     |       |     |     |     |     |
m
X
|     |     |     |     |     |     | z (t)=1−tN |     | −   | a (1−tn). |     |     |     | (S67) |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --------- | --- | --- | --- | ----- |
|     |     |     |     |     |     | a          |     |     | n         |     |     |     |       |
n=1
Let K ={α≥0:α([0,1])≤1}, a weak-star compact convex set. The equality-constrained primal program is explicitly
↑
Z
|     |     |     |     |     |     | sup |     | (1−tN)d(α−β). |     |     |     |     | (S68) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | ----- |
α,β∈K↑
R
|     |     |     |     |     | (1−tn)d(α−β)=0, |     |     | n≤m |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
For z in Eq. S67, the support of the unconstrained difference set in the residual direction is
a
Z
|     |     |     |     |     | sup |     | z d(α−β) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
a
α([0,1])≤1,β([0,1])≤1
|     |     |     |     | =max{0,supz |     |     | (t)}+max{0,−infz |     | (t)}=osc(z |     | ),  |     | (S69) |
| --- | --- | --- | --- | ----------- | --- | --- | ---------------- | --- | ---------- | --- | --- | --- | ----- |
|     |     |     |     |             |     |     | a                |     | t a        |     | a   |     |       |
t
where the last equality uses z (1)=0. Applying Lemma S3 to b (t)=1−tN and b (t)=1−tn gives, without a duality gap,
|     |     |     | a   |     |     |     |     | 0         |     |     | n   |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     | ∆↑  | =   | inf osc(z | ).  |     |     |     | (S70) |
|     |     |     |     |     |     |     | m,N |           | a   |     |     |     |       |
a∈Rm
Everyz isp(t)−tN forapolynomialp∈P satisfyingp(1)=1. Conversely, shiftinganyp∈P bytheconstant1−p(1)
|     | a   |     |     |     |     | m   |     |     |     |     |     | m   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
enforces that endpoint constraint without changing the oscillation of p−tN. Finally, for every continuous function r,
1
|     |     |     |     |     |     | inf | ∥r−c∥ | =   | osc(r). |     |     |     | (S71) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- | ----- |
∞ 2
c∈R
19

| Because | P contains |     | the constants, |     | Eqs. | S70 and | S71 | prove |     |     |     |     |     |
| ------- | ---------- | --- | -------------- | --- | ---- | ------- | --- | ----- | --- | --- | --- | --- | --- |
m
|     |     |     |     |     | ∆↑  | =2E | (uN;[0,1]):=2 |     |     | inf | ∥uN −p(u)∥ |     | (S72) |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ---------- | --- | ----- |
.
|     |     |     |     |     | m,N |     | m   |     |     |     |     | ∞   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p∈Pm
Extremal monotone worlds may be taken as step functions. Here is the finite argument. For any nonzero feasible measure
α with mass s, the vector of normalized integrals of (b ,...,b ,b ) lies in the convex hull of the continuous curve
|     |     |     |     |     |     |     |     |     | 1   | m N |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(b (t),...,b (t),b (t)) Rm+1. Carathéodory’s theorem represents that vector using at most m+2 curve points.
| t 7→ |     |     |     | ⊂   |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1    |     | m   | N   |     |     |     |     |     |     |     |     |     |     |
Multiplying their weights by s preserves the mass, all m audits, and the deployment objective. The zero measure is
already atomic. Applying this replacement separately to both measures in any optimal pair—whose existence follows from
weak-star compactness—gives two optimal atomic measures, hence two right-continuous distribution functions with at most
m+2 jumps each. Equation S72 is an exact validation consequence; best uniform approximation of monomials and its
| degree-squared |     | resolution | are | classical | [24, | main | result, | pp. | 451–455]. |     |     |     |     |
| -------------- | --- | ---------- | --- | --------- | ---- | ---- | ------- | --- | --------- | --- | --- | --- | --- |
S6.3. Exact capped-tail dual under monotonicity and Lipschitz regularity
For 0<L<∞, let contain the nondecreasing [0,1]-valued functions with Lipschitz constant at most L. Every member
F ↑,L
| has the unique |     | almost-everywhere |     |         | representation |         |     |      |     |     |     |          |       |
| -------------- | --- | ----------------- | --- | ------- | -------------- | ------- | --- | ---- | --- | --- | --- | -------- | ----- |
|                |     |                   |     |         |                | Z u     |     |      |     |     |     | Z 1      |       |
|                |     |                   |     | f(u)=c+ |                | q(t)dt, |     | c≥0, |     | 0≤q | ≤L, | c+ q ≤1. | (S73) |
|                |     |                   |     |         |                | 0       |     |      |     |     |     | 0        |       |
(t)=R1
| For any    | integrable  | residual | kernel  | r,         | write | Q             |     | r(u)du.  | Then   |     |            |          |       |
| ---------- | ----------- | -------- | ------- | ---------- | ----- | ------------- | --- | -------- | ------ | --- | ---------- | -------- | ----- |
|            |             |          |         |            |       | r             | t   |          |        |     |            |          |       |
|            |             |          |         |            | Z     | 1             |     |          |        | Z 1 |            |          |       |
|            |             |          |         |            |       | r(u)f(u)du=cQ |     |          | (0)+   |     | (t)q(t)dt. |          | (S74) |
|            |             |          |         |            |       |               |     |          | r      |     | Q r        |          |       |
|            |             |          |         |            |       | 0             |     |          |        | 0   |            |          |       |
| Define the | capped-tail |          | support | functional |       |               |     |          |        |     |            |          |       |
|            |             |          |         |            |       |               |     | (cid:26) |        | Z 1 |            | (cid:27) |       |
|            |             |          |         |            | H     | (z)=          | sup |          | cz(0)+ |     | z(t)q(t)dt | .        | (S75) |
L
|     |     |     |     |     |     |     | c≥0, 0≤q≤L |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
R
c+ q≤1
| It has the | explicit | scalar-threshold |     |     | representation |     |          |     |     |     |     |          |     |
| ---------- | -------- | ---------------- | --- | --- | -------------- | --- | -------- | --- | --- | --- | --- | -------- | --- |
|            |          |                  |     |     |                |     | (cid:26) |     |     | Z   |     | (cid:27) |     |
1
|     |     |     |     | H   | (z)= | inf | λ+[z(0)−λ] |     |     | +L  | [z(t)−λ] | dt . | (S76) |
| --- | --- | --- | --- | --- | ---- | --- | ---------- | --- | --- | --- | -------- | ---- | ----- |
|     |     |     |     |     | L    |     |            |     | +   |     |          | +    |       |
λ≥0
0
Toproveit, introduceanitemspace{⋆}∪[0,1]withcapacitymeasureµ =δ +Ldt, itemvaluev(⋆)=z(0)andv(t)=z(t),
|     |     |     |     |     |     |     |     |     | R   | L   | ⋆   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and allocation w(⋆)=c, w(t)=q(t)/L. Then 0≤w ≤1 and wdµ ≤1. For every λ≥0,
L
|     |     |     |     |     | Z    |     |             |     |     | Z   | 1        |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ----------- | --- | --- | --- | -------- | --- | --- |
|     |     |     |     |     | vwdµ |     | ≤λ+[v(⋆)−λ] |     |     | +L  | [v(t)−λ] | dt. |     |
|     |     |     |     |     |      | L   |             |     | +   |     |          | +   |     |
0
Conversely, allocate full capacity to values strictly above a threshold, none below it, and just enough of the threshold
level—including the atom when it ties—to fill at most one unit. If all positive capacity has mass at most one, the threshold
is zero. This continuous-knapsack rule attains the infimum and proves Eq. S76. It also supplies an algorithm: for the
polynomial residual z , find the roots of z (t) = λ, integrate its polynomial antiderivative on the positive intervals, and
|     |     |     | a   |     |     | a   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
minimize one convex scalar function. The baseline atom competes through the separate [z (0)−λ] term.
a +
Bounded-density moment problems have a substantial classical theory, including necessary-and-sufficient compact-set
conditions [20, Theorem 3(a–c), pp. 5–6]; here the functional arises as the exact dual norm of a validation residual.
| For completeness, |     | encode |     | Eq. S73 | by the | measure  |     |      |     |     |             |     |       |
| ----------------- | --- | ------ | --- | ------- | ------ | -------- | --- | ---- | --- | --- | ----------- | --- | ----- |
|                   |     |        |     | ν       | =cδ    | +q(t)dt, |     | c≥0, | 0≤q | ≤L, | ν([0,1])≤1. |     | (S77) |
0
The atom at the left endpoint represents the baseline c and has coefficient z(0); the absolutely continuous part represents
the derivative. The set of such measures is convex and weak-star compact: c∈[0,1], the order interval 0≤q is
|     |     |     | K L |     |     |     |     |     |     |     |     |     | ≤L  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
weak-star compact in L∞, and the mass inequality is closed. Its support function is exactly H (z). The equality-constrained
L
program over two copies of K reproduces the audit agreement and deployment separation for two members of F . Since
|     |     |         |     | L         |        |     |         |           |     |      |     |     | ↑,L |
| --- | --- | ------- | --- | --------- | ------ | --- | ------- | --------- | --- | ---- | --- | --- | --- |
|     | =z  | , Lemma | S3  | therefore | gives, |     | without | a duality |     | gap, |     |     |     |
| Q P |     | a       |     |           |        |     |         |           |     |      |     |     |     |
kN− ankn
|     |     |     |     |     |     | ∆↑,L | =   | inf {H | (z  | )+H | (−z )}. |     | (S78) |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------ | --- | --- | ------- | --- | ----- |
|     |     |     |     |     |     | m,N  |     |        | L a | L   | a       |     |       |
a∈Rm
Unlike a qualitative assertion that smoothness helps, Eq. S78 is a computable finite-dimensional convex optimization over
audit coefficients; evaluating only requires thresholding the values of a one-dimensional tail residual. As becomes
|     |     |     |     | H L |     |     |     |     |     |     |     | L   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
unbounded, the derivative mass may concentrate arbitrarily and the sum of supports tends to osc(z ), recovering Eq. S70.
a
20

| S6.4. Explicit | smooth | indistinguishable |          |     | worlds  |          |        |     |          |     |       |
| -------------- | ------ | ----------------- | -------- | --- | ------- | -------- | ------ | --- | -------- | --- | ----- |
| Let L (u)=P    | (2u−1) | be shifted        | Legendre |     | and set |          |        |     |          |     |       |
| m              | m      |                   |          |     |         |          |        |     |          |     |       |
|                |        |                   |          |     |         | (cid:26) |        |     | (cid:27) |     |       |
|                |        |                   |          |     |         |          | 1      | L   |          |     |       |
|                |        |                   |          | A   | =min    |          | ,      |     | .        |     | (S79) |
|                |        |                   |          | m,L |         | m+1      | m(m+1) |     |          |     |       |
Define
Z u
|     |     |     | (u)=A |     | [L    | (0)] | +A  | [L′ | (t)] |     |     |
| --- | --- | --- | ----- | --- | ----- | ---- | --- | --- | ---- | --- | --- |
|     |     |     | f m   |     | m,L m | +    | m,L |     | +    | dt, |     |
m
0
Z u
|     |     |     | g (u)=A |     | [−L | (0)] | +A  |     | [−L′ (t)] | dt. | (S80) |
| --- | --- | --- | ------- | --- | --- | ---- | --- | --- | --------- | --- | ----- |
|     |     |     | m       |     | m,L | m +  | m,L |     | m         | +   |       |
0
Then f −g =A L . Both functions are nonnegative and nondecreasing. The shifted derivative satisfies
| m   | m m,L | m   |     |     |     |          |     |     |     |     |       |
| --- | ----- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ----- |
|     |       |     |     |     | ∥L′ | =m(m+1), |     |     |     |     | (S81) |
∥ ∞
m
so each Lipschitz constant is at most L. To check the upper range constraint, note that has monotonicity intervals
L m
m
and |L |≤1, hence its total variation is at most 2m. Splitting positive and negative variation and accounting for the initial
m
value shows that each right side of Eq. S80 is at most (m+1)≤1. Thus .
|               |         |     |       |     |     | A m,L |     |     | f   | m ,g m ∈F ↑,L |     |
| ------------- | ------- | --- | ----- | --- | --- | ----- | --- | --- | --- | ------------- | --- |
| Orthogonality | of L to | P   | gives |     |     |       |     |     |     |               |     |
|               | m       | m−1 |       |     |     |       |     |     |     |               |     |
Z 1
|     |     |     | (f )−θ | (g  | )=A |     | (u)L | (u)du=0, |     |      | (S82) |
| --- | --- | --- | ------ | --- | --- | --- | ---- | -------- | --- | ---- | ----- |
|     |     | θ   | n m    | n m | m,L |     | k n  | m        |     | n≤m. |       |
0
| At deployment, | Eq. S44 | gives the | exact | separation |     |     |     |     |     |     |     |
| -------------- | ------- | --------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
m N −j
|     |     |     | (f     | )−θ | (g )|=A |       |       |     | = Y |     | (S83) |
| --- | --- | --- | ------ | --- | ------- | ----- | ----- | --- | --- | --- | ----- |
|     |     |     | |θ N m | N   | m       | m,L D | m,N , | D   | m,N | .   |       |
N +j
j=1
This proves the lower bound using smooth monotone worlds rather than a sign oscillation.
| S6.5. Positive-polynomial |     | recovery |     | and | the upper | bound |     |     |     |     |     |
| ------------------------- | --- | -------- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- |
Let agree on the first audits and put h=f−g. For x<y, both increments f(y)−f(x) and g(y)−g(x) lie in
| f,g ∈F |     |     | m   |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
↑,L
[0,L(y−x)]; their difference therefore lies in [−L(y−x),L(y−x)]. Thus h is L-Lipschitz, not merely 2L-Lipschitz. Audit
| agreement implies |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Z
1
|     |     |     |     | ujh(u)du=0, |     |     | j =0,...,m−1. |     |     |     | (S84) |
| --- | --- | --- | --- | ----------- | --- | --- | ------------- | --- | --- | --- | ----- |
0
Put d=⌊(m−1)/2⌋. Among nonzero p∈P , consider the Rayleigh quotient
d
R1(1−u)p(u)2du
|     |     |     |     |     | ρ =min | 0   |            |     | .   |     | (S85) |
| --- | --- | --- | --- | --- | ------ | --- | ---------- | --- | --- | --- | ----- |
|     |     |     |     |     | m      |     | R1 p(u)2du |     |     |     |       |
p̸=0
0
The eigenvalues of multiplication by compressed to are the shifted Gauss–Legendre nodes. Consequently
|     |     |     | u   |     |     | P   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
d
|     |     |     |     |     |     | ρ =1−ξ |     | ,   |     |     | (S86) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     | m      | d+1 |     |     |     |       |
where ξ is the largest shifted Legendre zero of degree d+1. Let p attain Eq. S85 and normalize q = p2/ R p2. Then
d+1
≥0, R =1, and degq ≤m−1. Equation S84 gives R qh=0, and Lipschitz continuity gives
q q
|     |     |     |     |     | (cid:12)Z |     |     |     | (cid:12) |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | -------- | --- | --- |
1
|     |     |     |     | |h(1)|=(cid:12) | q(u){h(1)−h(u)}du |     |     |     | (cid:12)    |     | (S87) |
| --- | --- | --- | --- | --------------- | ----------------- | --- | --- | --- | ----------- | --- | ----- |
|     |     |     |     |                 | (cid:12)          |     |     |     | (cid:12)≤Lρ | m . |       |
|     |     |     |     |                 | (cid:12)          |     |     |     | (cid:12)    |     |       |
0
| If U has density | k , then | E(1−U | )=1/(N |     | +1). Hence |     |     |     |     |     |     |
| ---------------- | -------- | ----- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
| N                | N        |       | N      |     |            |     |     |     |     |     |     |
Z 1
|     |     |     | (f)−θ |     | (g)|≤|h(1)|+ |     |     | (u)|h(u)−h(1)|du |     |     |     |
| --- | --- | --- | ----- | --- | ------------ | --- | --- | ---------------- | --- | --- | --- |
|     |     |     | |θ N  | N   |              |     | k   | N                |     |     |     |
0
|     |     |     |     |     |     | (cid:18) |     | 1   | (cid:19) |     |       |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- | ----- |
|     |     |     |     |     | ≤L  | 1−ξ      |     | +   | .        |     | (S88) |
|     |     |     |     |     |     |          | d+1 | +1  |          |     |       |
N
The unrestricted benchmark also gives (f)−θ (g)| , and bounded truth gives the trivial upper bound one.
|     |     |     |     | |θ N | N   | ≤   | B m,N |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ----- | --- | --- | --- | --- |
Combining Eqs. S83 and S88 proves the finite bounds in the shape-constrained corollary of the main text.
21

Finally, if 0 < L < ∞ is fixed and m2/N → τ, then A m2/L → 1 and Eq. S60 gives D → e−τ. The classical
|              |            |     |       |             |             |     |        | m,L            |        |         | m,N |       |
| ------------ | ---------- | --- | ----- | ----------- | ----------- | --- | ------ | -------------- | ------ | ------- | --- | ----- |
| extreme-zero | asymptotic |     | for   | Legendre    | polynomials |     | gives  |                |        |         |     |       |
|              |            |     |       |             |             |     | m2(1−ξ | )−→j2          | ,      |         |     | (S89) |
|              |            |     |       |             |             |     |        | d+1            | 0,1    |         |     |       |
| while m2/(N  | +1)→τ      |     | [25]. | Multiplying | the         | two | bounds | by m2/L proves |        |         |     |       |
|              |            |     |       |             |             |     | m2∆↑,L |                | m2∆↑,L |         |     |       |
|              |            |     |       |             | e−τ ≤liminf |     | m,N    | ≤limsup        | m,N    | ≤j2 +τ. |     | (S90) |
0,1
|     |     |     |     |     |     |     | L   |     | L   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The two sides differ by constants depending only on the fixed phase coordinate, so the rate L/m2 is sharp.
| S6.6. Numerical |     | evaluation |     | and | Lipschitz |     | sensitivity |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
The reproduction script independently checks: (i) the first m Legendre moments by adaptive quadrature; (ii) the derivative
bound m(m+1)≤L; (iii) the range of both Jordan worlds on a 200,001-point grid; and (iv) the lower and Gauss-node
A
m,L
upper bounds. Across 30 (m,N) cases with L=1, the maximum audited-moment residual was 6.356×10−17, the largest
constructed Lipschitz constant was one, and the largest constructed world value was 0.417.
Table S3: Shape-restricted bounds at m2/N = 1 and L = 1. Values are normalized by m2/L; they tend toward the lower
| constant | e−1 =0.3679 |     | and upper | constant | j2  | +1=6.7832. |     |     |     |     |     |     |
| -------- | ----------- | --- | --------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
0,1
|     |     |     |     |     | m   | m2A   | D   | m2{1−ξ | +1/(N | +1)} |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------ | ----- | ---- | --- | --- |
|     |     |     |     |     |     | m,1   | m,N |        | d+1   |      |     |     |
|     |     |     |     |     | 4   | 0.225 |     |        | 4.322 |      |     |     |
|     |     |     |     |     | 8   | 0.288 |     |        | 5.428 |      |     |     |
|     |     |     |     |     | 16  | 0.325 |     |        | 6.079 |      |     |     |
|     |     |     |     |     | 32  | 0.346 |     |        | 6.426 |      |     |     |
|     |     |     |     |     | 64  | 0.357 |     |        | 6.603 |      |     |     |
Toevaluatetheexactcapped-taildualitself,werestrictedeachderivativeq tobeconstantonnestedequal-widthpercentile
bins. ThisgivesafiniteprimalLPovertwoadmissiblepiecewise-linearreliabilitylawsandabin-averagedversionofEqs.S78
and S76. In exact arithmetic the two finite LP formulations are duals. The returned floating-point coefficient vector a was
then evaluated against the by root-finding for (t)=λ and analytic integration of the polynomial residual
|     |     |     | continuum |     | H   |     |     | z   |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |           |     | L   |     |     | a   |     |     |     |     |
between roots. Exact feasibility would make the bin construction a lower bound, and exact evaluation at any a would be
an upper bound. The stored solver vectors, roots, and integrals were not wrapped in interval arithmetic, however, so the
| following | pairs | are numerical |     | estimates | rather | than | certified | enclosures. |     |     |     |     |
| --------- | ----- | ------------- | --- | --------- | ------ | ---- | --------- | ----------- | --- | --- | --- | --- |
Table S4: Numerical primal–dual estimates for the exact capped-tail frontier. Theprimaluses8,192bins; “dual”evaluates
the continuum threshold functional at the returned audit coefficients. “Gap” is their floating-point difference, not an interval-certified
enclosure width. The final column is the rigorous but looser analytic bracket in the main corollary.
|     |     |     | (m,N,L)  |     | Primal      |     |             | Dual      | Gap | Constructive | bracket  |     |
| --- | --- | --- | -------- | --- | ----------- | --- | ----------- | --------- | --- | ------------ | -------- | --- |
|     |     |     | (2,8,1)  |     | 0.139322917 |     | 0.139322920 | 3.49×10−9 |     | [0.07778,    | 0.61111] |     |
|     |     |     | (4,16,1) |     | 0.046130661 |     | 0.046130667 | 6.41×10−9 |     | [0.01409,    | 0.27015] |     |
|     |     |     | (8,64,1) |     | 0.020791486 |     | 0.020791501 | 1.49×10−8 |     | [0.00449,    | 0.08482] |     |
|     |     |     | (8,64,4) |     | 0.072274153 |     | 0.072274347 | 1.94×10−7 |     | [0.01798,    | 0.33927] |     |
Across these rows the numerical finite-LP primal–dual gap is at most 2.1×10−12. Doubling from 4,096 to 8,192 bins
changes the primal by at most 2.84×10−7. For (m,N,L)=(4,16,1) one returned optimizer is
|     |     |     |     |     | a=(−0.931448, |     | 7.151953, | −15.935844, | 10.715339), |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --------- | ----------- | ----------- | --- | --- | --- |
with both thresholds zero. For (8,64,4) the positive-residual threshold is 0.0228384 and the negative threshold is zero,
illustrating the competition between derivative capacity and the baseline atom. Power-basis audit coefficients become
ill-conditioned at = 8 even though the objective is stable; all coefficients and nested-grid values are supplied in
m
results/capped_tail_dual_coefficients.csv and results/capped_tail_dual_checks.csv. The independent script
is code/solve_capped_tail_dual.py.
The percentile coordinate gives a direct scale interpretation: |f(u+h)−f(u)| Lh. A reliability change of one
|     |     |     |     |     | L   |     |     |     |     | ≤   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
therefore requires at least 1/L of the rank range; for L<1 it cannot occur anywhere on [0,1]. The audited moment prefix
does not validate this local assumption. It should be bounded using scientific knowledge or independent candidate-level
rank–truth data with uniform uncertainty, and otherwise varied as a sensitivity parameter.
22

Table S5: Sensitivity to the percentile-scale Lipschitz bound at (m,N) = (8,64). Values are converged floating-point
primal–dual estimates, not interval-certified enclosures; the last row is the separate monotone frontier 2E (u64).
8
|     |     |     |     |     | L   | Minimum | rank | span | 1/L | ∆↑,L |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ---- | ---- | --- | ---- | --- | --- | --- |
8,64
|     |     |     |     |     | 0.25 |     | 4.0000 |     |     | 0.005198 |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------ | --- | --- | -------- | --- | --- | --- |
|     |     |     |     |     | 0.50 |     | 2.0000 |     |     | 0.010396 |     |     |     |
|     |     |     |     |     | 1    |     | 1.0000 |     |     | 0.020791 |     |     |     |
|     |     |     |     |     | 2    |     | 0.5000 |     |     | 0.041509 |     |     |     |
|     |     |     |     |     | 4    |     | 0.2500 |     |     | 0.072274 |     |     |     |
|     |     |     |     |     | 8    |     | 0.1250 |     |     | 0.108038 |     |     |     |
|     |     |     |     |     | 16   |     | 0.0625 |     |     | 0.138346 |     |     |     |
|     |     |     |     |     |      |     |        | 0   |     | 0.162160 |     |     |     |
∞
The nearly linear regime through L=1 occurs because the total-mass constraint in is not yet active. At larger L, the
H L
optimal threshold becomes positive and the frontier bends toward the monotone limit. These values show why reporting
only the analytic brackets can be misleading and why conclusions should be accompanied by an L sensitivity curve.
| S7. Extensions |     | and         | scope |          |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S7.1. Bounded  | and | categorical |       | outcomes |     |     |     |     |     |     |     |     |     |
Nothing in the inverse theorem requires binary truth. For T ∈ [a,b], rescale to [0,1] and set f(x) = E(T | X = x). All
ambiguity results then rescale by b−a. For categories Y ∈ {1,...,C}, define f (x) = P(Y = c | X = x). The geometry
c
applies coordinatewise subject to P =1; joint identified sets may exploit that simplex constraint.
f
c c
| S7.2. Known-kernel |     | selection |     | laws | beyond | iid | search |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ---- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
Best-of-N is one kernel family. A recent test-time-scaling taxonomy distinguishes single-trajectory sequential scaling,
leaf-level terminal reduction, and prefix-level search [26]. The closed form in this paper covers the fixed-proposal iid special
case of leaf-level maximum-score reduction. A randomized shortlist, top-k draw, rejection sampler, beam-search trace, or
dependent candidate process induces another selected-state law . If that law is known or can be estimated independently
k
w
on the same stable state space, Eq. S6 applies without an iid assumption and returns dist (k ,S ); it does not return
|     |     |     |     |     |     |     |     |     |     |     |     | 1 w V |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
. Dependence among candidates changes the selected-rank kernel and may change effective search breadth in either
B m,N
direction. Adaptive generators create history-dependent kernels; the natural state x must then include the relevant history,
and validation must span the conditional deployment functionals. In particular, one must not substitute k (u)=NuN−1 for
N
an agent that updates its generator after observing intermediate scores. If the policy-induced law is unknown or candidate
generation changes the reliability surface, neither the exact best-of-N frontier nor the general known-kernel identity supplies
a certificate. The generality is therefore exact but conditional: it covers known kernels, not unspecified adaptive agents.
The boundary need not be binary when the policy law is estimable. Let v ,...,v ,k be modeled normalized kernels and
|          |                      |        |            |     |               |     |          |          |        | 1    | p   |     |       |
| -------- | -------------------- | ------ | ---------- | --- | ------------- | --- | -------- | -------- | ------ | ---- | --- | --- | ----- |
| let      | be the               | actual | normalized |     | kernels       | on  | the same | surface, |        | with |     |     |       |
| v ,...,v | ,ek                  |        |            |     |               |     |          |          |        |      |     |     |       |
| e1 ep    |                      |        |            |     |               |     |          |          |        |      |     |     |       |
|          |                      |        |            |     | ∥v            | −v  | ∥ ≤δ     | ,        | ∥ek−k∥ | ≤δ . |     |     | (S91) |
|          |                      |        |            |     | ej            | j   | 1 j      |          |        | 1 k  |     |     |       |
|          | (Kernel-perturbation |        |            |     | certificate). |     |          |          |        |      |     |     |       |
Proposition S1 If f,g ∈F agree under every actual audit kernel, then
|     |     |     |     |        |       |               | (cid:13)  |     | (cid:13)      |      |     |     |       |
| --- | --- | --- | --- | ------ | ----- | ------------- | ---------- | --- | ------------- | ---- | ---- | --- | ----- |
|     |     |     |     |        |       |               | (cid:13)  | p   | (cid:13)      | p    |      |     |       |
|     |     |     |     |        |       |               | (cid:13)   | X   | (cid:13)      | X    |     |     |       |
|     |     |     |     | |⟨ek,f | −g⟩|≤ | inf           | (cid:13)k− | a   | v (cid:13) +δ | + |a | |δ . |     | (S92) |
|     |     |     |     |        |       |               |            |     | j j           | k    | j j  |     |       |
|     |     |     |     |        |       | a∈Rp(cid:13) |            |     | (cid:13)      |      |     |     |       |
|     |     |     |     |        |       |               | (cid:13)   | j=1 | (cid:13)      | j=1  |      |     |       |
1
=⟨v
For one world, the centered reconstruction from the actual audit means y ,f⟩ satisfies, for every a,
|     |     |                  |     |     |      |      |              |            |     | ej ej            |      |          |       |
| --- | --- | ---------------- | --- | --- | ---- | ---- | ------------ | ---------- | --- | ---------------- | ---- | -------- | ----- |
|     |     | (cid:12)         |     |    |      |      | (cid:12)    | (cid:13)  |     | (cid:13)         |      |         |       |
|     |     | (cid:12)         |     |     | p    |      | (cid:12)     | (cid:13)   | p   | (cid:13)         | p    |          |       |
|     |     |                  |     |  1 | X    |      |             | 1         | X   |                  | X    |         |       |
|     |     | (cid:12)         |     | +   | (y   |      | 1 ) (cid:12) | (cid:13)   |     | (cid:13) +δ      | +    |          | (S93) |
|     |     | (cid:12) ⟨ek,f⟩− |     | 2   | a j  | ej − | (cid:12) ≤   | 2 (cid:13) | k−  | a j v j (cid:13) | k |a | j |δ j . |       |
|     |     | (cid:12)         |     |     |      |      | 2 (cid:12)   | (cid:13)   |     | (cid:13)         |      |          |       |
|     |     | (cid:12)         |     |    | j= 1 |      |  (cid:12)   |  (cid:13) | j=  | 1 (cid:13)       | j= 1 |         |       |
1
Proof. For h=f −g, actual audit agreement gives ⟨v ,h⟩=0 and ∥h∥ ≤1. For any a,
|     |     |     |     |     |     |     | ej        |     |          | ∞   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | (cid:13)  |     | (cid:13) |     |     |     |     |
|     |     |     |     |     |     |     | (cid:13)  |     | (cid:13) |     |     |     |     |
|     |     |     |     |     |     |     | +(cid:13) | X   | (cid:13) | X   |     |     |     |
|⟨ek,h⟩|≤∥ek−k∥ (cid:13)k− a v (cid:13) + |a |∥v −v ∥ , (S94)
|     |     |     |     |     |     | 1   | (cid:13) | j   | j (cid:13) | j j | ej 1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | --- | ---- | --- | --- |
|     |     |     |     |     |     |     | (cid:13) | j   | (cid:13)   | j   |      |     |     |
1
which proves Eq. S92 after taking the infimum. For Eq. S93, write both the actual target and audit means against −1/2,
f
whose L∞ norm is at most 1/2, and apply the same triangle inequality. □
23

Deterministic audit-mean errors |y −y |≤η add P |a |η to the right side of Eq. S93; the finite-task stochastic term
|     |     |     |     | bj ej | j   | j j j |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- |
in Eq. S27 is then added separately. Robust optimal recovery from inaccurate data is established more generally [27]; no
new abstract perturbation theorem is claimed. The validation-specific use is to turn an independently estimated policy law
into an auditable penalty. If a logged adaptive policy yields confidence bounds for its history-distribution kernel, Eq. S93
quantifies the remaining model risk. Without such bounds, describing the generator as adaptive supplies no certificate.
| S7.3. Structural |     | assumptions |     | can narrow | the | frontier |     |     |
| ---------------- | --- | ----------- | --- | ---------- | --- | -------- | --- | --- |
The Chebyshev worlds oscillate because the model class permits every measurable [0,1]. Monotonicity, Lipschitz
f ∈
bounds, bounded variation, analyticity, or a parametric tail law can sharply reduce ambiguity. Such assumptions should
be represented by replacing in Eq. S1 and recomputing its support function. They are scientifically meaningful only if
F
justified and stress-tested prospectively. Replication at the same interventions cannot manufacture them.
| S7.4. Unknown |     | kernels |     | and distribution | shift |     |     |     |
| ------------- | --- | ------- | --- | ---------------- | ----- | --- | --- | --- |
The span identity treats v and k as known and assumes that they act on a common reliability surface. Proposition S1
|     |     |     | j   | w   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
handles bounded kernel error on that surface; sample splitting or joint empirical-process bounds can supply the δ . If
j
deployment changes the underlying reliability surface from to , however, kernel geometry alone is insufficient. One then
|     |     |     |     |     |     | f f w |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- |
needs a transport or invariance model relating the surfaces. The present result should be read as a lower-level identification
limit, not a distribution-shift theorem: failure already occurs with known kernels and a common, stable f.
| S8. Mathematical-reasoning |     |     |     | search | experiment |     |     |     |
| -------------------------- | --- | --- | --- | ------ | ---------- | --- | --- | --- |
Empirical purpose and external-validity boundary. Theexperimentsareretrospective, contrastivedemonstrationsof
themodeledmechanism,notestimatesofitsprevalenceacrossAIsystemsandnotempiricalvalidationofthedistribution-free
extremizers. Within each model–task cell, the candidates are a fixed finite empirical population. The iid idealization is
=R
conditional on task: task t has its own randomized percentile and law f , so θ k f . Equal-weight macro averaging
t n,t n t
gives =R with =T−1P ; no exchangeability across tasks is assumed. Every reported best-of-n estimand is the
| θ n | k n | f   | f   | f t |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
exact with-replacement maximum-score functional of the corresponding task-specific population with randomized ties; it is
not an observed maximum among n distinct newly generated candidates. The analyses test four narrower claims: changing
that score-and-select functional changes the truth target; task-level reversals can coexist with favorable mean scaling; a
finite empirical audit prefix can leave a wide compatible deployment interval; and score-matched label acquisition can
reduce finite estimation error relative to uniform labels within one fixed pool. The GSM8K analysis uses natural-language
answers, consensus ranking, exact-answer truth, and widths through 4,096. The independent CodeRM analysis in Section
S10 uses programs, generated-unit-test ranking, separate HumanEval+ truth, and widths through 100. This variation
supports construct-level replication within the conditional-iid score-and-select setting. It does not make either task collection
representative of adaptive agents, new-candidate deployment, subjective evaluation, deployment frequency, or the probability
| of a near-worst-case |     | world. |         |     |     |     |     |     |
| -------------------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
| S8.1. Dataset        |     | and    | pinning |     |     |     |     |     |
The public Monkey Business dataset contains 10,000 generated GSM8K solutions per problem and model [21]. We used 127
| problems | for each | of  | two configurations: |     |     |     |     |     |
| -------- | -------- | --- | ------------------- | --- | --- | --- | --- | --- |
• GSM8K_Llama-3-8B-Instruct.json; SHA-256 0e334c7010a2eb39ab0aaf38cdd196da0b6219a95fd69f82d35b8f51e46e
d765;
• GSM8K_Llama-3-70B-Instruct.json; SHA-256 22ff8a363d5a5b8ea5a6c299285d8f615ec32b9c1fe08e8253cc1a6c9c7
c323f.
Both files are downloaded from revision a9f8f73bcd6948a57ed922cba4e48062ef95f553. The pinned release file, rather
than an outcome-dependent rule applied by us, fixes the inclusion set: each file contains exactly 127 problem records, and
we included every record in both files without excluding any eligible problem. Each record contains 10,000 generated texts
and exact final-answer correctness indicators. Total analyzed candidates were 127×10,000×2=2.54 million.
| S8.2. Consensus |     | score | and | disjoint deployment |     | population |     |     |
| --------------- | --- | ----- | --- | ------------------- | --- | ---------- | --- | --- |
Within every model–problem cell, a deterministic random permutation used 2,000 solutions as the reference set and 8,000 as
the deployment population. The split seed was 20,260,817 plus fixed model and problem offsets. The final answer following
the GSM8K delimiter was normalized by removing commas and whitespace. Its frequency in the reference set was the
consensus score for deployment candidates with that answer; unparsable answers received a score below every parsed answer.
For a discrete score group ℓ, let and be its lower and upper cumulative population masses and let be its mean
|     |     |     |     | F ℓ− | F ℓ |     | t ℓ |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- |
truth label. Under iid sampling with replacement from the empirical deployment population and uniform tie breaking, the
| exact selected | truth | at  | width | n is |     |         |     |       |
| -------------- | ----- | --- | ----- | ---- | --- | ------- | --- | ----- |
|                |       |     |       |      |     | = X n−F | n   | (S95) |
|                |       |     |       |      | θbn | t {F    | }.  |       |
|                |       |     |       |      |     | ℓ ℓ     | ℓ − |       |
ℓ
This avoids Monte Carlo simulation of search. We evaluated n∈{1,2,4,...,4096}.
24

|     |      | A  Math: 127 problems |     |     |     |      | B  Code: 164 tasks |     |     |     | C  Math reversals |     |     |
| --- | ---- | --------------------- | --- | --- | --- | ---- | ------------------ | --- | --- | --- | ----------------- | --- | --- |
|     | 1.00 |                       |     |     |     | 0.85 |                    |     |     |     |                   |     |     |
Llama-3-8B
0.8
|     | 0.95 |     |     |     |     | 0.80 |     |     |     |     | Llama-3-70B |     |     |
| --- | ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ----------- | --- | --- |
0.6
|     | hturt renniw naeM |     |     |     | hturt renniw naeM | 0.75 |     |     |     | 6904→1 ,hturt Δ |     |     |     |
| --- | ----------------- | --- | --- | --- | ----------------- | ---- | --- | --- | --- | --------------- | --- | --- | --- |
0.90
0.4
0.70
0.85
|     |     |     |     |     |     | 0.65 |     |     |     | 0.2 |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
0.80
|     |     |     |     |     |     | 0.60 |     |     |     | 0.0 |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
0.75
0.55
−0.2
|     | 0.70 |     | Llama-3-8B |     |     |     |     | Llama-3-8B |     |     |     |     |     |
| --- | ---- | --- | ---------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
0.50
|     |      |                        | Llama-3-70B |     |     |      |                      | Llama-3-70B |     | −0.4 |                      |         |     |
| --- | ---- | ---------------------- | ----------- | --- | --- | ---- | -------------------- | ----------- | --- | ---- | -------------------- | ------- | --- |
|     | 0.65 |                        |             |     |     | 0.45 |                      |             |     |      |                      |         |     |
|     |      | 100 101                | 102         | 103 |     | 100  |                      | 101         | 102 | 0.0  | 0.2 0.4              | 0.6 0.8 | 1.0 |
|     |      | Candidates searched, n |             |     |     |      | Programs searched, n |             |     |      | Problem quantile     |         |     |
|     |      | D  Code reversals      |             |     |     |      | E  Split persistence |             |     |      | F  500 masked labels |         |     |
0.200
|     |     | Llama-3-8B  |     |     |                       | 16  |     | Llama-3-8B  |     |                                |     | Llama-3-8B  |     |
| --- | --- | ----------- | --- | --- | --------------------- | --- | --- | ----------- | --- | ------------------------------ | --- | ----------- | --- |
|     | 0.8 |             |     |     |                       |     |     | Llama-3-70B |     |                                |     | Llama-3-70B |     |
|     |     | Llama-3-70B |     |     | pp 1> demrah smelborP |     |     |             |     | rorre etulosba .tcp-ht59 0.175 |     |             |     |
14
0.6
001→1 ,hturt Δ
|     |     |     |     |     |     | 12  |     |     |     | 0.150 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
0.4
|     |     |     |     |     |     | 10  |     |     |     | 0.125 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
0.2
|     |     |     |     |     |     | 8   |     |     |     | 0.100 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
0.0
|     |     |     |     |     |     | 6   |     |     |     | 0.075 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
−0.2
|     |     |     |     |     |     | 4   |     |     |     | 0.050 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
−0.4
|     |     |     |     |     |     | 2   |     |     |     | 0.025 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
−0.6
|     |     |     |     |     |     | 0   |     |     |     | 0.000 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
0.0 0.2 0.4 0.6 0.8 1.0 0 1 2 3 4 5 6 7 8 9 Uniform Bo8 Top 5% Bo100
|     |     | Task quantile |     |     |     |     |     | Split |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Figure S1: Retrospective construct checks in two fixed public candidate populations. (A) Mean selected truth and 95%
problem-bootstrap intervals across 127 GSM8K problems under answer-consensus ranking. (B) The corresponding functional across
164 HumanEval+ tasks under CodeRM ranking. (C,D) Task-level changes include reversals despite favorable aggregate scaling. (E)
GSM8K harm counts persist across 10 reference/deployment splits. (F) In masked-label replays at a 500-label budget, a score-tail rule
frozen after an 82-task design split reduces held-out best-of-100 estimation error relative to uniform candidate labels. All best-of-n
quantities are with-replacement functionals of fixed empirical populations. The panels are not prospective tests of audit effectiveness
| or    | prevalence  | estimates. |                |     |     |     |     |     |     |     |     |     |     |
| ----- | ----------- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S8.3. | Uncertainty |            | and robustness |     |     |     |     |     |     |     |     |     |     |
Allreportedaggregatestreattheproblemasthesamplingunit. Percentileintervalsuse20,000bootstrapresamplesofthe127
problem rows, with fixed seed 73,041 plus model offset. Macro AUC is the mean within-problem ROC AUC over deployment
populations containing both truth classes: 125problems for Llama-3-8Band 107 for Llama-3-70B.The remaining two and20
single-class populations remain in all search-reliability and harm summaries but do not have a defined AUC. Ten robustness
splits use distinct deterministic seeds and repeat reference scoring, deployment construction, exact winner integration, and
harm counting. This checks that reversals are not artifacts of a particular 2,000/8,000 partition; it does not make the 127
| GSM8K | problems | representative |     | of every | task | domain. |     |     |     |     |     |     |     |
| ----- | -------- | -------------- | --- | -------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
These data validate three premises, not the distribution-free worst case itself: the selection kernel changes materially with
search breadth; high average rank discrimination can coexist with problem-level reversals; and those reversals persist under
resplitting. The Chebyshev theorem is a mathematical identification result and does not require empirical frequency of its
extremizers.
S9. Finite and asymptotic efficiency of validation interventions
| S9.1. | Winner-distribution |     |     | importance |     | sampling |     |     |     |     |     |     |     |
| ----- | ------------------- | --- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| The   | target              | is  |     |            |     |          |     |     |     |     |     |     |     |
Z 1
|     |     |     |     |     | θ = | k   | (u)f(u)du, | k (u)=NuN−1. |     |     |     |     | (S96) |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --- | --- | --- | ----- |
|     |     |     |     |     | N   | N   |            | N            |     |     |     |     |       |
0
25

Table S6: Empirical search-scale summary. Intervals are 95% problem-bootstrap percentile intervals. Harm counts compare
| n=4096 | with n=1. |            |     |     |     |     |            |        |     |             |     |
| ------ | --------- | ---------- | --- | --- | --- | --- | ---------- | ------ | --- | ----------- | --- |
|        |           | Quantity   |     |     |     |     | Llama-3-8B |        |     | Llama-3-70B |     |
|        |           | Problems   |     |     |     |     |            | 127    |     | 127         |     |
|        |           | Candidates |     |     |     |     | 1,270,000  |        |     | 1,270,000   |     |
|        |           |            |     |     |     |     |            | 0.7684 |     | 0.9305      |     |
θb1
|     |     | θb4096   |          |          |           |     |          | 0.8819  |     | 0.9685           |     |
| --- | --- | -------- | -------- | -------- | --------- | --- | -------- | ------- | --- | ---------------- | --- |
|     |     | Mean     | change   |          |           |     |          | 0.1135  |     | 0.0380           |     |
|     |     | Change   | interval |          |           |     | [0.0748, | 0.1538] |     | [0.0195, 0.0576] |     |
|     |     | Problems |          | entering | macro     | AUC |          | 125     |     | 107              |     |
|     |     | Macro    | AUC      |          |           |     |          | 0.9070  |     | 0.9617           |     |
|     |     | AUC      | interval |          |           |     | [0.8616, | 0.9474] |     | [0.9230, 0.9901] |     |
|     |     | Problems |          | harmed   | >1 pp     |     |          | 14      |     | 3                |     |
|     |     | Problems |          | harmed   | >5 pp     |     |          | 12      |     | 3                |     |
|     |     | Worst    | problem  | change   |           |     |          | −0.4796 |     | −0.3598          |     |
|     |     | Best     | problem  | change   |           |     |          | 0.8803  |     | 0.4339           |     |
|     |     | Harm     | >1       | pp over  | 10 splits |     |          | 13–15   |     | 3 in every split |     |
Suppose an audit draws a labeled winner from width s, whose percentile density is (u)=sus−1. The Horvitz–Thompson
q
s
variable
(U)
k
|     |     |     | Z = | N   | T,  | U ∼q | , T | |U ∼Bernoulli{f(U)}, |     |     | (S97) |
| --- | --- | --- | --- | --- | --- | ---- | --- | -------------------- | --- | --- | ----- |
|     |     |     | s   | (U) |     |      | s   |                      |     |     |       |
q s
| is unbiased | because |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Z
k
|     |     |     |     |     | EZ  | =   | q Nf | =θ . |     |     | (S98) |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | ----- |
|     |     |     |     |     |     | s   | s    | N    |     |     |       |
q s
| Its second | moment is |     |     |     |     |     |          |              |     |     |     |
| ---------- | --------- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --- | --- |
|            |           |     |     |     | Z   | 1   | (cid:26) | (u)(cid:27)2 |     |     |     |
k
|     |     |     |     | EZ2 | =   | q (u) | N   | f(u)du |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | --- |
|     |     |     |     |     | s   | s     | (u) |        |     |     |     |
|     |     |     |     |     |     | 0     | q s |        |     |     |     |
N2 Z 1
|     |     |     |     |     | =   |     | u2N−s−1f(u)du |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
s
0
N2
|     |     |     |     |     | =   |     |        |     |     |     | (S99) |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ----- |
|     |     |     |     |     |     |     | θ 2N−s | ,   |     |     |       |
s(2N −s)
so
N2
|     |     |     |     | Var(Z | )=  |      |     | θ −θ2 | .   |     | (S100) |
| --- | --- | --- | --- | ----- | --- | ---- | --- | ----- | --- | --- | ------ |
|     |     |     |     |       | s   | s(2N | −s) | 2N−s  | N   |     |        |
For s=N, the weight is one and the variance is θ (1−θ ). We define the variance-equivalent label ratio
|     |     |     |     |     | N   | N   |       |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | Var(Z | )   |     |     |     |
s
|     |     |     |     |     |     | ρ = |      | .   |     |     | (S101) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------ |
|     |     |     |     |     |     | s θ | (1−θ | )   |     |     |        |
|     |     |     |     |     |     |     | N    | N   |     |     |        |
Under independent sampling and the same estimator class, labels from design have the same asymptotic variance as
|                       |        |        |     |     |     |     | ρ s |     |     | s   |     |
| --------------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| one deployment-winner |        | label. |     |     |     |     |     |     |     |     |     |
| S9.2. Top-tail        | design |        |     |     |     |     |     |     |     |     |     |
An audit uniform on the top fraction a of percentiles has density q (u) = a−11{u ≥ 1−a}. It targets the truncated
a
functional
Z 1
|     |     |     |     |     |       | =   | (u)f(u)du. |     |     |     | (S102) |
| --- | --- | --- | --- | --- | ----- | --- | ---------- | --- | --- | --- | ------ |
|     |     |     |     |     | θ N,a |     | k N        |     |     |     |        |
1−a
| The omitted | nonnegative | mass | satisfies |     |     |     |     |     |     |     |     |
| ----------- | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Z 1−a
|     |     |     |     | 0≤θ | −θ  | ≤   | k   | (u)du=(1−a)N. |     |     | (S103) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------ |
|     |     |     |     | N   | N,a |     | N   |               |     |     |        |
0
For a=0.05 and =4096, this is 0.954096 =5.70×10−92. Its importance-weighted second moment is
N
aN2
|     |     |     |     |     | EZ2 | =    |     | θ[1−a,1], |     |     | (S104) |
| --- | --- | --- | --- | --- | --- | ---- | --- | --------- | --- | --- | ------ |
|     |     |     |     |     |     | a 2N | −1  | 2N−1      |     |     |        |
where the superscript denotes the contribution of the top interval to the corresponding selected-mean integral.
26

| S9.3. Retrospective |     | masked-label |     |     | acquisition | replay |     |     |     |     |
| ------------------- | --- | ------------ | --- | --- | ----------- | ------ | --- | --- | --- | --- |
The variance calculation above predicts a design advantage but does not show its finite-sample size. We therefore used the
candidate-level CodeRM data in Section S10 as a label oracle. For every model–task cell, all truth values were treated as
masked at the allocation stage. Each acquisition draw first sampled one of the 164 tasks uniformly, then selected a candidate
using only its verifier score under one of four fixed rules: uniform candidate, best-of-8 winner, randomized top-5% score
percentile, or best-of-100 deployment winner. Full truth was used only after acquisition to score the estimator against the
| exact macro | best-of-100 |     | target. |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
For a tied score group occupying sorted candidate indices a+1,...,b among M =100 candidates, the probability assigned
| to each candidate |     | under | best-of-s | selection | is  |     |     |     |     |     |
| ----------------- | --- | ----- | --------- | --------- | --- | --- | --- | --- | --- | --- |
(b/M)s−(a/M)s
(i)= (S105)
|     |     |     |     |     |     | q   |     |     | .   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | s   |     | b−a |     |     |
This is exact for with-replacement search, maximum-score selection, and uniform randomization within the winning tie. Let
p =q (i) denote the target probability and let q denote the audit probability within the sampled task. The revealed-label
| i 100 |     |     |     |     |     | i   |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
variable
p iT
|     |     |     |     |     |     |     | Z = | ,   |     | (S106) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
|     |     |     |     |     |     |     | i q | i   |     |        |
i
is unbiased for the task-averaged best-of-100 target whenever 0 wherever 0. For the top-tail design, Eq. S106
|     |     |     |     |     |     |     |     | q i > | p i > |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- |
estimates the truncated target; the missing mass is at most 0.95100 =0.0059205. Randomized percentile sampling distributes
| a boundary-crossing |     | tie | uniformly | across | the entire | score | group. |     |     |     |
| ------------------- | --- | --- | --------- | ------ | ---------- | ----- | ------ | --- | --- | --- |
We ran 5,000 independent acquisition replicates for label budgets 25,50,100,250,500,1,000,2,000, and 5,000, using seed
131,071 plus fixed model and design offsets. Within a replicate, samples accumulate across budgets. The primary finite error
metric is the 95th percentile across replicates of |; root mean squared and median absolute errors are also written
|     |     |     |     |     |     | |θb100 −θ | 100 |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
to results/coderm_label_acquisition.csv.
Table S7: Finite masked-label error for best-of-100 CodeRM truth. Entries are the 95th percentile of absolute error across
5,000 retrospective replays. Allocation uses scores only; full labels score the emulation afterward.
|     |     |     | Model | Audit       | design     |        | 100   | 500   | 1,000 5,000 | labels |
| --- | --- | --- | ----- | ----------- | ---------- | ------ | ----- | ----- | ----------- | ------ |
|     |     |     | 8B    | Uniform     | candidate  |        | 0.444 | 0.184 | 0.131       | 0.060  |
|     |     |     | 8B    | Best-of-8   | winner     |        | 0.157 | 0.070 | 0.051       | 0.022  |
|     |     |     | 8B    | Top-5%      | percentile |        | 0.105 | 0.047 | 0.034       | 0.015  |
|     |     |     | 8B    | Best-of-100 |            | winner | 0.085 | 0.039 | 0.028       | 0.013  |
|     |     |     | 70B   | Uniform     | candidate  |        | 0.212 | 0.110 | 0.079       | 0.035  |
|     |     |     | 70B   | Best-of-8   | winner     |        | 0.109 | 0.047 | 0.033       | 0.015  |
|     |     |     | 70B   | Top-5%      | percentile |        | 0.085 | 0.038 | 0.027       | 0.012  |
|     |     |     | 70B   | Best-of-100 |            | winner | 0.082 | 0.036 | 0.025       | 0.011  |
At 500 labels, replacing uniform acquisition by the top-tail design reduced the 95th-percentile error by factors 3.89 and
2.89 for 8B and 70B. The same top-5% rule, budgets, and estimator were used for both models; no model-specific truth
information changes allocation. The actual top-tail truncation biases under the fully labeled empirical populations were
9.75×10−5 and 3.64×10−5, far below the distribution-free bound, but those empirical values are used only for retrospective
scoring. This is a finite label-acquisition emulation, not a prospective experiment with newly generated candidates or newly
collected truths. A genuinely prospective test would randomize the audit design before outcomes are produced and should
| additionally | account | for | per-design | generation | cost. |     |     |     |     |     |
| ------------ | ------- | --- | ---------- | ---------- | ----- | --- | --- | --- | --- | --- |
The replay errors and the 1,000-bin feasible spans in Section S10.2 are not one metric. The prefix programs construct
compatiblecontinuumstep-functionwitnessesunderexactorbandedmeanconstraints; thereplayaskshowafixedestimator
behaves when labels are acquired in different score directions. Their joint conclusion is narrower than a prospective
effectiveness claim: on the same best-of-100 functional, covered search widths, independent task count, and label direction
| address           | different | failure  | modes | and must   | be planned | separately. |     |     |     |     |
| ----------------- | --------- | -------- | ----- | ---------- | ---------- | ----------- | --- | --- | --- | --- |
| S9.4. Frozen-rule |           | held-out |       | audit test |            |             |     |     |     |     |
The full-pool replay above fixes the allocation rule in advance but evaluates it on the same task population used to
report the comparison. To test whether an audit rule selected from data transfers across tasks, we added a label-blind
discovery/held-out split before examining outcomes. With seed 260,821, the 164 task identifiers shared by both CodeRM
models were permuted once and divided into 82 discovery and 82 held-out tasks. The split is shared across models and is
| recorded | in results/coderm_heldout_task_split.csv. |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The candidate audit family was fixed at the top 5%, 10%, or 20% of score percentiles. All three designs leave at most
0.95100 =0.0059205 of the best-of-100 target mass unsupported. On discovery tasks only, we ran 5,000 masked-label replays
27

at a budget of 500 and selected the fraction minimizing the mean 95th-percentile absolute error across the two models.
Mean discovery errors were 0.0427, 0.0546, and 0.0751, respectively, so the 5% rule was selected. That rule was then frozen
before the held-out target and replay error were computed. Uniform acquisition served as the held-out comparator. The
estimator and exact tied-score candidate probabilities are those in Eqs. S105 and S106; independent replay streams use seed
| 262,147 plus | fixed | design | and | model offsets. |     |     |     |     |     |     |     |
| ------------ | ----- | ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Table S8: Frozen-rule performance on 82 held-out CodeRM tasks. Entries are based on 5,000 retrospective masked-label
replays at 500 labels. The top-tail fraction was chosen on a disjoint 82-task discovery split and frozen before held-out outcomes were
scored.
Model Held-out target Uniform q95 error Frozen top-5% q95 error Frozen absolute bias
|     | 8B  |     |     | 0.698 |     | 0.180 |     |     |     | 0.049 | 7.58×10−5 |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | ----- | --------- |
|     | 70B |     |     | 0.791 |     | 0.076 |     |     |     | 0.035 | 7.28×10−5 |
The frozen rule reduced the held-out q95 error by factors 3.67 and 2.15. This is stronger than selecting and evaluating
a design on the same task set: held-out outcomes did not choose the tail fraction. It is nevertheless not a prospective
intervention. Both splits come from one existing public dataset, all candidates and labels had already been generated, and
the replay does not measure collection cost, distribution shift, or a causal effect of assigning a real evaluation program.
Complete discovery and held-out metrics, including median error and RMSE, are in results/coderm_heldout_audit.csv.
| S9.5. Asymptotic |     | GSM8K |     | calculation |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Within each model, tie-averaged truth was aggregated into 20 equal-width percentile bins across problems. Treating the bin
meansasapiecewise-constantf,allmomentsinEqs.S100andS104areanalyticdifferencesofbin-edgepowers. Thisbinning
is deliberately coarse; at N =4096, essentially all target mass lies in the last bin, and the computation is a transparent
| design comparison |     | rather | than | a claim of | nonparametric |     | tail recovery. |     |     |     |     |
| ----------------- | --- | ------ | ---- | ---------- | ------------- | --- | -------------- | --- | --- | --- | --- |
Table S9: Variance-equivalent labels for a best-of-4096 target. Each entry is the number of labels under the row design
| needed to | match | the asymptotic |     | variance of  | one deployment-winner |      |            | label.   |             |          |     |
| --------- | ----- | -------------- | --- | ------------ | --------------------- | ---- | ---------- | -------- | ----------- | -------- | --- |
|           |       |                |     | Audit        | design                |      | Llama-3-8B |          | Llama-3-70B |          |     |
|           |       |                |     | Uniform      | candidate             |      |            | 17,333.7 |             | 64,993.0 |     |
|           |       |                |     | Best-of-8    | winner                |      |            | 2,162.0  |             | 8,104.2  |     |
|           |       |                |     | Best-of-64   | winner                |      |            | 265.6    |             | 993.1    |     |
|           |       |                |     | Uniform      | top 5%                | rank |            | 859.6    |             | 3,220.4  |     |
|           |       |                |     | Best-of-4096 | winner                |      |            | 1.0      |             | 1.0      |     |
The large ratios have a simple source. Under uniform candidate sampling, the importance weight near = 1 is
u
approximately N, so rare tail labels receive enormous leverage. The deployment-winner design samples directly from that
tail and uses unit weights. The ratios depend on f, N, the score law, and the estimator; they are not transferable constants.
In a real evaluation, cost per label, dependence among generated candidates, and the feasibility of producing deployment
| winners must      | also | be  | included.    |               |     |     |     |     |     |     |     |
| ----------------- | ---- | --- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
| S9.6. Prospective |      |     | intervention | specification |     |     |     |     |     |     |     |
The public-data experiment can be converted into a genuinely prospective test without changing its estimand. Before
generating or labeling new outcomes, register the target width N, task population, verifier, tie rule, label budget, top-tail
fraction, and the uniform-versus-score-matched allocation comparison. Randomize independent task–model cells to audit
designs before truth is observed; retain the task as the cluster; and collect a fully labeled evaluation subset only to score
estimator error, not to choose the allocation. The primary comparison should be finite-sample squared or absolute error at a
fixed total cost, with coverage and generation cost as secondary outcomes. If the objective is instead a distribution-free
direct-winner interval of full width 0.10 at 95% confidence, Eq. S28 requires 738 independent tasks; this is a conservative
certificate calculation, not a power analysis. The fixed replay design used here—N =100, top 5%, and the eight reported
budgets—is a ready specification, but this paragraph is a protocol, not additional prospective evidence.
| S10. Code-generation     |     |     |     | replication | and          | reproducibility |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ----------- | ------------ | --------------- | --- | --- | --- | --- | --- |
| S10.1. CodeRM/HumanEval+ |     |     |     | data        | and estimand |                 |     |     |     |     |     |
The independent domain is the public CodeRM release [22], pinned at Git commit aa4946e9245ed41e24d60ad29e965132b
5b84fe6. We used all 164 HumanEval+ tasks and the first 100 candidate programs per task from each of the Llama-3-8B
and Llama-3-70B annotated solution files. The annotation SHA-256 digests are, respectively,
• cae513c7578a52c6d3110a13bbf2514e44a0cd58f2a4a258b58e7337c2af0211;
28

• 6ddb4273e4d9a35f7bef6016f37ac2e9b99d6bd7aad05357f7ff9399b0d45850.
Objective truth is the HumanEval+ field, which evaluates the program against the benchmark’s expanded
plus_status
hidden tests.
The CodeRM output archive linked by the repository README has SHA-256
728780d642f465e91f8619de1bae0cb3
192519278e87014d546cee9921d4e6c5. Foreachmodelweusedthepublic100-solutionby100-generated-unit-testexecution
| matrix. | The extracted |     | JSONL member | digests | are |     |     |     |     |     |     |
| ------- | ------------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
• 8B: 8169be74c8144e0bad6b593093a02e4963144f66a6a5f6b84c10ff1dd6e316d1;
• 70B: 7edb5fc98033f5de748c5dfe2f740cdeffb02020ead8f49988ea822d2d8d2fdf.
For candidate i, the verifier score is the fraction of the 100 CodeRM-8B-generated unit tests for which the execution result
is pass. The data therefore contain 164×100×2 = 32,800 programs and 3.28 million candidate–test executions. The
generated tests determine ranking; the distinct HumanEval+ status determines truth.
Within each model–task cell, Eq. S95 was applied to the empirical verifier-score groups, with exact uniform tie breaking,
for n∈{1,2,4,8,16,32,64,100}. Intervals use 20,000 task bootstrap resamples, with seed 92,771 plus model offset. AUC
gives half credit to tied positive–negative pairs. All 164 tasks contain both truth classes for each model and therefore enter
both macro AUCs. The task is the independent unit; the 100 generated tests do not count as 100 independent benchmark
tasks.
Table S10: Independent CodeRM/HumanEval+ replication. Intervals are 95% task-bootstrap percentile intervals. Harm
| compares | best-of-100 | with | one random     | program.       |     |       |            |        |             |                |     |
| -------- | ----------- | ---- | -------------- | -------------- | --- | ----- | ---------- | ------ | ----------- | -------------- | --- |
|          |             |      | Quantity       |                |     |       | Llama-3-8B |        | Llama-3-70B |                |     |
|          |             |      | Tasks          |                |     |       | 164        |        |             | 164            |     |
|          |             |      | Candidate      | programs       |     |       | 16,400     |        |             | 16,400         |     |
|          |             |      | Candidate–test | executions     |     |       | 1,640,000  |        |             | 1,640,000      |     |
|          |             |      | Tasks          | entering macro | AUC |       | 164        |        |             | 164            |     |
|          |             |      | Macro          | AUC            |     | 0.931 | [0.898,    | 0.959] | 0.881       | [0.818, 0.938] |     |
|          |             |      | θb1            |                |     | 0.536 | [0.473,    | 0.597] | 0.737       | [0.675, 0.797] |     |
|          |             |      |                |                |     | 0.715 | [0.649,    | 0.780] | 0.788       | [0.726, 0.847] |     |
θb100
|     |     |     | Mean  | change      |       | 0.179 | [0.134, | 0.226] | 0.051 | [0.025, 0.080] |     |
| --- | --- | --- | ----- | ----------- | ----- | ----- | ------- | ------ | ----- | -------------- | --- |
|     |     |     | Tasks | harmed by   | >1 pp |       | 10      |        |       | 4              |     |
|     |     |     | Worst | task change |       |       | −0.722  |        |       | −0.600         |     |
TheCodeRMreplicationisnotasecondestimateoftheGSM8Kmechanism. Itdeliberatelychangesthedomain,generator
outputs, score construction, truth mechanism, and search range. Its role is to test the more basic prediction that a favorable
average verifier can induce a heterogeneous reliability spectrum with severe local reversals. The repository did not expose an
explicit license file at the pinned revision, so the package does not redistribute programs, generated unit tests, or execution
logs. It includes only derived numeric candidate scores and labels, plus a checksum-verifying reconstruction script.
| S10.2. Retrospective |     |     | compatibility | from | an  | audited | prefix |     |     |     |     |
| -------------------- | --- | --- | ------------- | ---- | --- | ------- | ------ | --- | --- | --- | --- |
The main-text certification exercise uses the same 32,800 derived CodeRM score–truth rows. Within task t, sort the 100
candidates by verifier score. If a score-tie group occupies percentile intervals and has mean truth ¯ , define the bounded
I tj T tj
step function
|     |     |     |     |     | fbt | (u)=T | ¯ , | u∈I . |     |     | (S107) |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | ------ |
|     |     |     |     |     |     |       | tj  | tj    |     |     |        |
Spreading a tie group’s mean over its occupied intervals is exactly equivalent to uniform tie breaking. Consequently the
| macro law | fb =164−1P |     | fbt satisfies |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     |     |     |     |     | Z 1     |        |     | 1 164 |     |     |        |
| --- | --- | --- | --- | --- | ------- | ------ | --- | ----- | --- | --- | ------ |
|     |     |     |     |     |         | (u)du= |     | X     |     |     | (S108) |
|     |     |     |     |     | nun−1fb |        |     | θbt,n |     |     |        |
164
0
t=1
| for every | integer | n, not | only for | the eight search | widths | previously |     | plotted. |     |     |     |
| --------- | ------- | ------ | -------- | ---------------- | ------ | ---------- | --- | -------- | --- | --- | --- |
To ask what the audited prefix alone certifies, refine the 100 empirical rank intervals to = 1,000 equal bins and let
J
| g ∈[0,1] | be a candidate |     | law on | bin j. Put |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
j
|          |        |         |                   |           |            | (cid:18) j | (cid:19)n (cid:18) | j−1(cid:19)n |            |     |        |
| -------- | ------ | ------- | ----------------- | --------- | ---------- | ---------- | ------------------ | ------------ | ---------- | --- | ------ |
|          |        |         |                   |           |            | =          |                    |              |            |     | (S109) |
|          |        |         |                   |           | w n,j      |            | −                  | .            |            |     |        |
|          |        |         |                   |           |            | J          |                    | J            |            |     |        |
| For each | m, the | plug-in | endpoints         | solve the | two linear | programs   |                    |              |            |     |        |
|          |        |         | minimize/maximize |           |            | ⊤g subject | to                 | ⊤g =θbn      | n=1,...,m. |     | (S110) |
|          |        |         |                   |           | w          |            |                    | w            | ,          |     |        |
|          |        |         |                   |           |            | N          |                    | n            |            |     |        |
0≤g≤1
29

Every optimizer defines a bounded piecewise-constant function on [0,1]. Thus the displayed separation is a constructive
lower bound on the unrestricted continuum identified width; it is not created by allowing infeasible grid vectors. Raw
power-momentrowsbecomenearlycollinearasmgrows. Forexactplug-inequalities,theimplementationthereforenormalizes
the rows and replaces them by an orthonormal basis obtained from a QR factorization of the transposed audit matrix. This
changes neither the row space nor the exact feasible set, but prevents a tiny raw-moment tolerance from becoming a large
extrapolated target error. At m=8, increasing J from 200 to 500 and 1,000 changed every endpoint by less than 0.007.
| The maximum | raw equality | residual at | =1,000 | was 1.3×10−14. |     |     |     |
| ----------- | ------------ | ----------- | ------ | -------------- | --- | --- | --- |
J
Finite task sampling uncertainty was propagated separately. We drew 20,000 multinomial bootstrap resamples of the 164
tasks. For each m, let s be the bootstrap standard error and let c be the 95th percentile of
|     |     | bn  |     |            | m        |     |     |
| --- | --- | --- | --- | ---------- | -------- | --- | --- |
|     |     |     |     | (cid:12)   | (cid:12) |     |     |
|     |     |     |     | (cid:12) ∗ | (cid:12) |     |     |
max θb n −θbn (S111)
|     |     |     |     | (cid:12)          | (cid:12). |     |     |
| --- | --- | --- | --- | ----------------- | --------- | --- | --- |
|     |     |     |     | (cid:12) s        | (cid:12)  |     |     |
|     |     |     |     | 1≤n≤m (cid:12) bn | (cid:12)  |     |     |
Replacing the equalities in Eq. S110 by the simultaneous inequalities θbn −c s ≤w ⊤g ≤θbn +c s , truncated to [0,1],
|     |     |     |     |     |     | m bn n | m bn |
| --- | --- | --- | --- | --- | --- | ------ | ---- |
gives the bootstrap-feasible ranges in Table S11. They condition on the empirical score/rank construction and use the task
| as the sampling | unit; | they are not a distribution-shift |     | guarantee. |     |     |     |
| --------------- | ----- | --------------------------------- | --- | ---------- | --- | --- | --- |
Table S11: CodeRM best-of-100 ranges from audits through m. Plug-in columns impose exact empirical means at every
integer n≤m. Bootstrap columns allow the simultaneous 95% task-bootstrap band. Observed best-of-100 truth is 0.715 for 8B and
0.788 for 70B.
|     |     | Model       | m Plug-in  | range Width  | Bootstrap-feasible |                | range |
| --- | --- | ----------- | ---------- | ------------ | ------------------ | -------------- | ----- |
|     |     | Llama-3-8B  | 4 [0.003,  | 1.000] 0.997 |                    | [0.000, 1.000] |       |
|     |     |             | 8 [0.186,  | 0.992] 0.806 |                    | [0.003, 1.000] |       |
|     |     |             | 12 [0.453, | 0.907] 0.453 |                    | [0.021, 1.000] |       |
|     |     |             | 16 [0.620, | 0.796] 0.176 |                    | [0.056, 1.000] |       |
|     |     |             | 20 [0.690, | 0.737] 0.047 |                    | [0.102, 0.999] |       |
|     |     | Llama-3-70B | 4 [0.018,  | 1.000] 0.982 |                    | [0.000, 1.000] |       |
|     |     |             | 8 [0.305,  | 0.996] 0.691 |                    | [0.016, 1.000] |       |
|     |     |             | 12 [0.569, | 0.937] 0.367 |                    | [0.065, 1.000] |       |
|     |     |             | 16 [0.711, | 0.852] 0.141 |                    | [0.130, 1.000] |       |
|     |     |             | 20 [0.769, | 0.806] 0.038 |                    | [0.197, 1.000] |       |
The m = 8 extremizers are plotted in Fig. S2. They are not fitted forecasts of best-of-100 truth; they are witnesses
to nonidentification. The observed target lies inside every reported range, as it must because the empirical rank–truth
law itself is feasible. Machine-readable endpoints, bootstrap critical values, grid checks, and all 1,000-bin extremiz-
ers are supplied in results/coderm_partial_identification.csv, results/coderm_partial_id_grid_check.csv, and
results/coderm_partial_id_worlds.csv.
| S10.3. Independent |     | theorem checks |     |     |     |     |     |
| ------------------ | --- | -------------- | --- | --- | --- | --- | --- |
For m=1,...,8 and four values of per m, the reproducibility script performed three independent computations:
N
| 1. evaluated | the closed | form in Eq. S41; |     |     |     |     |     |
| ------------ | ---------- | ---------------- | --- | --- | --- | --- | --- |
2. constructed the barycentric interpolant at the roots and integrated its absolute error by adaptive quadrature split at
U m
every root;
3. integrated ukσ (u) for k =0,...,m−1 to check audited-moment annihilation.
m
Across 32 cases, the largest absolute difference between items 1 and 2 was 1.887×10−15. The largest absolute residual in
| item 3 was | 3.331×10−16. |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- |
Table S12: Representative exact-frontier checks. The complete 32-row table is results/theorem_checks.csv.
|     |     | m N  | Closed form  | Quadrature   | Max | moment residual |     |
| --- | --- | ---- | ------------ | ------------ | --- | --------------- | --- |
|     |     | 1 16 | 0.9999694824 | 0.9999694824 |     |                 | 0   |
|     |     | 2 21 | 0.9952431821 | 0.9952431821 |     | 2.22×10−16      |     |
|     |     | 4 31 | 0.9109153208 | 0.9109153208 |     | 4.16×10−17      |     |
|     |     | 6 41 | 0.7510560990 | 0.7510560990 |     | 3.33×10−16      |     |
|     |     | 8 51 | 0.5838695161 | 0.5838695161 |     | 1.11×10−16      |     |
The numerical checks are not substitutes for the proof. They are designed to detect sign, indexing, interpolation-node,
| and phase-scaling | errors | in the implementation. |     |     |     |     |     |
| ----------------- | ------ | ---------------------- | --- | --- | --- | --- | --- |
30

A  Llama-3-8B: compatible rank--truth laws B  Llama-3-70B: compatible rank--truth laws
|     | 1.0 |     |     |     |     |     | 1.0 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0.8 |     |     |     |     |     | 0.8 |     |     |     |
ytilibaborp hturT
|     | 0.6 |                          |     |     |     |     | 0.6 |     |     |     |
| --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0.4 |                          |     |     |     |     | 0.4 |     |     |     |
|     | 0.2 | Lowest compatible target |     |     |     |     | 0.2 |     |     |     |
Highest compatible target
Empirical plug-in law
|     | 0.0 |     |                              |     |         |     | 0.0     |                              |     |         |
| --- | --- | --- | ---------------------------- | --- | ------- | --- | ------- | ---------------------------- | --- | ------- |
|     | 0.0 | 0.2 | 0.4                          |     | 0.6 0.8 | 1.0 | 0.0 0.2 | 0.4                          | 0.6 | 0.8 1.0 |
|     |     |     | Verifier-score percentile, u |     |         |     |         | Verifier-score percentile, u |     |         |
C  Agreement through m=8, divergence at N=100 D  Agreement through m=8, divergence at N=100
|     | 1.0 |     |     |     |     |       | 1.0 |     |     |       |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
|     |     |     |     |     |     | 0.992 |     |     |     | 0.996 |
|     | 0.8 |     |     |     |     |       | 0.8 |     |     |       |
hturt renniW
|     | 0.6 | Compatible lower curve |     |     |     |     | 0.6 |     |     |     |
| --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Compatible upper curve
Observed curve
|     | 0.4 |     |     |     |     |     | 0.4 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.305
0.186
|     | 0.2 |         |                      |     |       |        | 0.2     |                      |     |           |
| --- | --- | ------- | -------------------- | --- | ----- | ------ | ------- | -------------------- | --- | --------- |
|     |     | audited |                      |     |       |        | audited |                      |     |           |
|     | 0.0 |         |                      |     |       |        | 0.0     |                      |     |           |
|     | 1   | 2       | 4                    | 8   | 16 32 | 64 100 | 1 2     | 4 8                  | 16  | 32 64 100 |
|     |     |         | Programs searched, n |     |       |        |         | Programs searched, n |     |           |
Figure S2: An empirical audited prefix does not certify the deployment target. (A,B) For each CodeRM model, linear
programsconstructboundedpiecewise-constantrank–truthlawsthatmatchtheempiricalbest-of-nmeansforeveryn=1,...,8while
minimizing or maximizing best-of-100 truth; the black line is the empirical plug-in law. (C,D) The induced search curves coincide
throughout the shaded audited range and then separate. At N =100, the constructive plug-in ranges are [0.186,0.992] for 8B and
[0.305,0.996]for70B;observedvaluesare0.715and0.788. Thegridlawsarefeasiblecontinuumlaws,sotheirseparationisawitnessed
| lower       | bound on     | unrestricted | empirical | ambiguity. |     |     |     |     |     |     |
| ----------- | ------------ | ------------ | --------- | ---------- | --- | --- | --- | --- | --- | --- |
| S10.4.      | Reproduction |              | workflow  |            |     |     |     |     |     |     |
| The package |              | contains:    |           |            |     |     |     |     |     |     |
• code/reproduce_geometry_validation.py: unrestricted and shape-restricted theorem checks, phase and finite-
certificate planning tables, CodeRM reconstruction from derived numbers, QR-stabilized empirical partial-identification
programs, finite masked-label acquisition, the frozen-rule discovery/held-out audit, Gaussian selection, intervention
| efficiency, |     | and all deterministic |     | figures; |     |     |     |     |     |     |
| ----------- | --- | --------------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
• code/solve_capped_tail_dual.py: nested-bin primal–dual LPs, continuum scalar-threshold evaluation, optimizer
| coefficients, |     | and percentile-scale |     | L sensitivity; |     |     |     |     |     |     |
| ------------- | --- | -------------------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
• code/analyze_search_spectrum.py: pinned raw-data download, checksum verification, reference/deployment analysis,
| bootstrap,                          |     | and processed | tables; |     |              |            |           |     |     |     |
| ----------------------------------- | --- | ------------- | ------- | --- | ------------ | ---------- | --------- | --- | --- | --- |
| • code/analyze_split_robustness.py: |     |               |         |     | the 10-split | robustness | analysis; |     |     |     |
• code/analyze_coderm_search.py: CodeRMchecksumverification,streamingexecution-matrixaggregation,exactsearch
| curves, | task | bootstrap, | and | derived | candidate table; |     |     |     |     |     |
| ------- | ---- | ---------- | --- | ------- | ---------------- | --- | --- | --- | --- | --- |
• data/processed/: exact processed inputs, including 32,800 derived CodeRM score–truth rows, used by the lightweight
reproduction;
• results/: machine-readableunrestrictedandregularizedtheorembounds,capped-tailprimal–dualchecksandoptimizers,
phase,finitecertificateplans,Gaussian,CodeRM,partial-identificationextremizersandgridchecks,finitelabel-acquisition
errors, discovery/held-out task assignments and errors, and design-efficiency outputs.
The lightweight script requires Python 3.12, NumPy, SciPy, and Matplotlib and does not download data or call a model API.
The full GSM8K reconstruction additionally uses scikit-learn and downloads the two pinned raw files (approximately 18.5
GB combined). The CodeRM reconstruction reads the public 213-MB compressed output archive and the pinned annotation
files. Every figure is deterministic. Bootstrap seeds are stated above; analytic theorem figures do not rely on Monte Carlo
draws.
31

S11. Relation to adjacent literatures and contribution boundary
The mathematical ingredients have substantial precedents. The audit prefix is a truncated Hausdorff moment problem:
classical work characterizes feasible moment sequences, while canonical-moment and Tchebycheff-system theory studies
the geometry and extremal representations of the resulting moment spaces [8, 9]. Once k ,...,k are recognized to span
1 m
P , optimal-recovery duality and canonical L1 approximation give the unrestricted distance [4, 15]. Bounded-density
m−1
moment theory supplies feasibility characterizations for the Lipschitz derivative measure [20]. The submitted objects are
the diameters and residual support functionals induced by the stated best-of-N audit/deployment kernels after imposing
bounded reliability, monotonicity, or a density cap. No general theorem about moment spaces, canonical representations,
quotient duality, orthogonal polynomials, or moment representation is claimed as new.
Two close AI results mark the applied boundary. ROC-n-reroll gives verifiers with arbitrarily close finite best-of-N
behavior and opposite infinite-compute limits [28], whereas the present unrestricted benchmark requires exact prefix equality
and solves a specified finite target. Evaluation Blind Spot studies geometric recovery for static benchmark coverage [29]; the
object here is selected-output truth under an explicit deployment kernel. These distinctions delimit the submitted object.
Closer statistical neighbors are Mallows’s parent-distribution bounds from expected order statistics [30], Papadatos’s
expected-maximaandrangesequences[13],andOkolewskiandPapadatos’sfiniteexpected-order-statistic/truncated-moment
connection [31]. They clarify feasibility and recovery. To our knowledge, they do not state the bounded-binary exact interval
for a best-of-width reliability prefix, its low-width reliability-mean maximality, or the monotone and capped-Lipschitz
residuals stated here. Huang et al. instead study coverage and optimal alignment under imperfect rewards [32]. Accordingly,
the contribution claimed here is the exact validation object and its consequences, not a new characterization of expected
order statistics.
S11.1. Theorem-by-theorem provenance
Table S13 gives the theorem-level boundary. Classical moment, approximation, and bounded-density results supply the
mathematical ingredients [8, 9, 15, 20, 24]; finite expected-order-statistic work supplies the closest statistical representation
results [13, 30, 31]; and recent best-of-N theory supplies the closest AI decision setting [32]. The third column states the
remaining validation-specific contribution.
TableS13: Concisecontributionboundary. “Submittedobject”isvalidation-specific;thelistedmathematicaltoolsareestablished
inputs.
Result Classicalinput Submittedobject
Unrestrictedbenchmark Hausdorff/canonicalmomentspaces[8,9], Fullboundedbinaryidentifiedinterval,attainable
quotientrecovery[4],andcanonicalL1 endpointsandinteriorlaws,plusthefinitethetaphase
approximation[15] law
Monotonefrontier Measurerepresentationanduniformmonomial Exactreductionofcompatiblemonotonevalidation
approximation[24] worldsto2Em(uN)
MonotoneLipschitzfrontier Compactmeasuredualityandbounded-density Exactcapped-tailresidualdualforthestated
moments[20] validationkernels
Endpointbounds Legendreorthogonality,Gaussrecovery,and Explicitsmoothcompatibleworldsandorder-sharp
extreme-zeroasymptotics fixed-Lbounds
Scopeandsampling Spaninclusion,concentration,andperturbation Widthcoverageseparatedfromtaskprecision;nonew
inequalities[27] abstractrecoveryorconcentrationtheoremisclaimed
S11.2. Exact claim
The submitted claim is that the specified validation and deployment kernels produce the exact attainable identification
objects in Table S13, including the monotone and capped-Lipschitz duals, the reliability-mean audit law, and the finite
planning consequences. No general inverse-problem, moment, order-statistic, approximation, orthogonal-polynomial, or
theta-function theorem is claimed. Complete proofs are given in Sections S1–S7, with executable numerical checks for every
reported finite calculation.
The empirical role is narrower. Independent units are 127 problems and 164 tasks; candidate outputs repeat within them.
The analyses show target change, reversals, compatible witnesses, and a within-pool acquisition contrast, not prevalence,
extremal-world frequency, or prospective effectiveness. The 82/82 split protects held-out labels from rule selection but
remains a public-data replay.
32
---- END DOCUMENT ----
