Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Removal-Only Actuation in Age-Structured Branching Populations:
Fundamental Limits of Equilibrium Placement
Ouerdia Arezki1, Ali Zemouche2
Abstract—Asubcriticalage-structuredbranchingpopulation Thecontrolproblemisunusual:theplantneedsnostabili-
dies out almost surely. Conditioned on survival, it converges sation.Itcontractstoitsconditionedequilibriumonitsown,
to its Yaglom limit, a quasi-stationary equilibrium that we
so the command places the attractor rather than stabilising
take as the operating point for control. We model preventive
it. The state is a measure-valued population, observed only
removal (culling) as an age-dependent actuator that raises the
mortality rate and leaves the offspring law untouched, and through a Fleming–Viot particle estimator. The removal
we show that its authority over this equilibrium is bounded hazard u is the control input, the regulated output is the
for structural reasons. Two facts drive the result. First, the decay rate λ = ν (κ) of the conditioned equilibrium, and
0 Y
inputismatchedtothekillingratebutunmatchedwithrespect
a transmission barrier Λ bounds the reachable decay rate.
to the Foster–Lyapunov drift, so the transmission barrier Λ
Everything rests on one modelling hypothesis, which we
set by reproduction alone is invariant under such actuation.
Second, and this does not follow from invariance alone, the state at the outset because it limits the scope of every result
supremumofthereachabledecayratesisΛ+ν⋆,whereν⋆ ≤0 below: the actuator is childless, i.e. it raises the mortality
is the Malthusian parameter of the lineage conditioned never rate and does not alter the offspring law (p ). Removal ter-
n
to die childless; the gap |ν⋆| is given in closed form and
minates a lineage; it does not make transmission less likely.
vanishesexactlywhennoindividualhastwoormoreoffspring.
Under this hypothesis the barrier Λ, which is determined
Consequently no removal law of this class reaches the barrier,
andalongtheadmissibilityboundarytheachievabledecayrate by the uncontrolled lifetime and offspring laws, is invariant
isgovernedbytheshapeoftheactuatorratherthanbyitssize. (Lemma 1), so λ 0 (u) < Λ is immediate. What is not
We illustrate these results on a model calibrated to the 2001 immediate, and is the mathematical content of Theorem 2,
Cumbrian foot-and-mouth outbreak. is the exact value of the supremum, Λ+ν⋆, which is strictly
Keywords: Admissible controls, age-structured popula-
belowΛbyacomputablemargin.Actuatorsthatalsoreduce
tions,equilibriumplacement,fundamentallimitations,mono-
transmission act on Λ itself and are not covered here.
tone systems, reachable sets, stochastic systems.
This work draws on three lines of research. Fundamental
limitations of feedback, in the Bode–Freudenberg–Looze
I. INTRODUCTION
tradition [2]–[5], give the setting: a bound on achievable
Anage-structuredbranchingpopulationalmostsurelydies
performance that no control law in a given class can avoid,
outinthesubcriticalregime.Itslong-termobjectistherefore
because it is a property of the plant–actuator pair. Positive
notastationarydistributionbutthequasi-stationarydistribu-
and monotone systems [17]–[19] provide the ordering tools
tion (QSD), or Yaglom limit, namely the law of the popu-
behind the monotone input–output map established below.
lation conditioned on survival [6]–[10]. In applications such
Epidemic control over networks [20]–[22] and the optimal
as epidemic surveillance and invasive-species management,
controlofage-dependentpopulationPDEs[23]–[25]provide
this conditioned law provides the natural equilibrium for
the application context. What is different here is that the
control. In [1], we characterize this equilibrium by proving
operating point is a conditioned law, not a stationary one,
the existence and uniqueness of the QSD together with
and is available only through particle estimation.
the convergence of a Fleming–Viot particle approximation
Thecontributionsofthispaperarethefollowing.Weprove
for the uncontrolled plant. The present paper introduces
that the input is matched to the killing rate but unmatched
preventive removal as a control input and asks how far
with respect to the Foster–Lyapunov drift (Lemma 1); every
this actuator can displace the conditioned equilibrium. The
limitation below follows from this single mismatch. We
answer is a structural limitation of a specific actuator class,
derive a closed-form, state-independent input constraint set
in the sense of feedback theory [2], [4], [5], rather than a
(Theorem 1), necessary and independent of the control law,
new probabilistic estimate.
and sufficient for the proportional family. We show that the
input–outputmapismonotoneandcharacterisethereachable
The authors gratefully acknowledge the support of the IUT Henri
output set together with its supremum (Theorem 2), which
Poincare´deLongwy,Universite´deLorraine.Thisworkwasinitiatedwhile
O. Arezki was a visiting professor hosted by CRAN (CNRS UMR 7039) is strictly sharper than the elementary bound λ 0 (u) < Λ
andtheIUTHenriPoincare´ deLongwy. inherited from invariance: it identifies the supremum exactly
A short version of this paper, restricted to Sections III–IV, has been
andquantifiestheresidualgapinclosedform.Weshowthat,
submittedtotheIEEEControlSystemsLetters(L-CSS).
1Laboratoire de Mathe´matiques Blaise Pascal (LMBP), UMR CNRS along the admissibility boundary, achievable performance
6620, Universite´ Clermont Auvergne, F-63178 Aubie`re, France (email: is set by the input shape, not its magnitude (Corollary 1).
ouerdia.arezki@uca.fr)
For proportional actuation we give an exact certifiable gain
2Universite´ de Lorraine, CRAN CNRS UMR 7039, 54400 Cosnes et
Romain,France(e-mail:ali.zemouche@univ-lorraine.fr). interval (Theorem 3), show how fast the certified stability
6202
guA
11
]YS.ssee[
1v14601.8062:viXra

margin shrinks and what this costs in sensing near the con- the Malthusian parameter λ is the unique solution of the
0
straintboundary(Proposition2),andprovethatthecertainty- Euler–Lotka equation m (cid:82)∞ eλtdG(t) = 1. We use the
0
equivalence gain law driven by the particle estimator is ISS decay-rate sign convention throughout: λ > 0 in the
0
with respect to the estimation error (Proposition 3). subcritical regime, and −λ is the exponential growth rate.
0
II. PRELIMINARIESANDPROBLEMFORMULATION B. Standing assumptions and prior results
This section recalls the notation and results of [1] used We collect here the conditions used in the sequel. Each
throughout the paper and states the control problem. From statement below specifies the subset it requires.
a control perspective, the plant is an autonomous, open-loop (H1) G is absolutely continuous with continuous density g,
convergent conditioned process whose operating point is the G(0) = 0, supp(G) = [0,∞), and inf g > 0 for
[ℓ,L]
Yaglom limit. every 0<ℓ<L<∞;
(H2) m<1;
A. Measure-valued plant model
(H3) p >0;
LetGbealifetimedistributionon[0,∞)withcontinuous 1
density g and G(0)=0, and let h(s)= (cid:80) p sn denote (H4) 0<µ ∞ ≤µ∗ <∞;
n≥0 n (H5) p µ∗ <Λ;
the offspring generating function, where ξ ∼ (p ), m := 0
h′(1) < ∞, and p 0 := P(ξ = 0). Each individual n lives for (H6) (cid:80) n nαp n <∞ for some α>1 satisfying αλ 0 >Λ.
a random lifetime T ∼G and, upon death, is independently Conditions (H1)–(H5) are inherited from [1]: (H2) fixes
replaced by ξ offspring born at age zero. Write G¯ := 1− the subcritical regime, (H5) is the main structural require-
G, µ := g/G¯ for the hazard rate, µ∗ := sup µ(a), and ment, and (H1), (H3) and (H4) are regularity and non-
a
µ := liminf µ(a) ≤ µ∗. Because the death intensity degeneracy conditions on the lifetime and offspring laws.
∞ a→∞
(cid:80) µ(a (t)) depends on the age configuration rather than Assumption (H6) is what the controlled problem adds: it
i i
on the population size, the size process is not Markovian. strengthens the companion condition αλ 0 > p 0 µ∗ = ∥κ∥ ∞
The Markov property is recovered on the space M p (R + ) of to αλ 0 > Λ, so that a single exponent α serves for every
finitepointmeasures,equippedwiththenarrowtopology[8]. admissible input, the killing rate being allowed to rise up
Defining to Λ. It is not restrictive in the calibrated application, whose
offspringdistributionhasmomentsofeveryorder.Moreover,
(cid:88)
η := δ , Z :=⟨η ,1⟩, τ :=inf{t>0:η =0},
t ai(t) t t t (H5) implies p 0 <1/2, hence m>1/2.
i The certificates used throughout the paper are the follow-
andsettingE :=M (R )\{0},theextendedgenerator[14] ing.
p +
is, for F(η)=Φ(⟨η,f⟩),
Definition 1 (Admissible certificate). Let u ∈ L∞(R ).
+ +
LF(η)=Φ′(⟨η,f⟩)⟨η,f′⟩+ (cid:90) µ(a) (cid:88) p An admissible certificate for X u is a triple (V,λ 1 ,C) in
n which V : E → [0,∞) belongs to the extended domain of
R
+ n≥0 L , has relatively compact sublevel sets, satisfies B :=
(cid:104) Φ (cid:0) ⟨η,f⟩−f(a)+nf(0) (cid:1) −Φ (cid:0) ⟨η,f⟩ (cid:1)(cid:105) η(da), (1) (cid:80) Xu p V(nδ ) < ∞ and has W := V(δ) of clas V s C1
n≥1 n 0 ·
and eventually non-decreasing, and in which C < ∞ and
where individuals age at unit speed between jumps, and an
λ >∥κ ∥ satisfy
1 u ∞
individual of age a is replaced at rate µ(a) according to
η (cid:55)→η−δ a +ξδ 0 . For Φ=id, L Xu V ≤−λ 1 V +C on E.
L⟨η,f⟩=⟨η,Af⟩, (Af)(a)=f′(a)+µ(a) (cid:0) mf(0)−f(a) (cid:1) . We call λ 1 the certified drift rate.
Extinction occurs only when a singleton dies without off- Three results of [1] are used repeatedly below, and we
spring, so the killing rate is state them without proof.
κ(η)=p µ(a)1 , ∥κ∥ =p µ∗ <∞. (2) Fact 1 (Malthusian parameter and reproductive value [1,
0 {η=δa} ∞ 0
Lem. 2.2]). Under (H1), (H2), (H4) and (H5):
Absorption is a boundary that the size process cannot cross; (i) (cid:82) eθadG(a)<∞ for every θ <µ ;
∞
on the lifted state space it becomes a bounded killing
(ii) the Euler–Lotka equation has a unique solution 0 <
mechanism. Let X denote the process on E obtained by
λ <Λ;
0
removing the transition δ (cid:55)→ 0. Then η is X killed at
a (iii) the reproductive value v(a) = mE[eλ0(T−a) | T > a]
rate κ, with generator L F = LF +κ(F −F(0)). Under
X belongs to C1(R ), satisfies v(0)=1, m≤v ≤v ,
X, a singleton can leave the large-age region only through b + max
and Av =−λ v.
successfulreproduction,atrate(1−p )µ(a),sothemaximal 0
0
The stable-age profile and reproductive value coincide with
drift rate available in a Foster–Lyapunov argument is
the eigenelements of the associated renewal semigroup [12,
Λ:=(1−p )µ , (3) Thm. 3.8].
0 ∞
rather than µ . We call Λ the transmission barrier; it is Fact 2 (Necessity of the transmission barrier [1, Prop. 3.2]).
∞
determined solely by the reproduction mechanism. Finally, Assume (H2) and (H4). If the uncontrolled process X

admits an admissible certificate (V,λ ,C) in the sense of Nostabilisationisrequired,theflowconvergesonitsown,so
1
Definition 1 with u ≡ 0, then necessarily λ ≤ Λ, so that thedesignquestioniswhichequilibriumcanbeassigned,and
1
(H5) is necessary. It is also sufficient: under (H1)–(H6) the atwhatcertifiedcost.Thereachable-setanswerisalimitation
certificate underlying Fact 3 is admissible, so the class is of the plant–actuator pair, in the spirit of the fundamental
non-empty. limitations of feedback [2]–[4].
Fact3(Selection,contraction,andestimability[1,Thms.3.6,
conditionedflow
3
h
.
o
8
l
,
ds
C
f
o
o
r
r
. 3
X
.9 .
])
T
.
h
U
e
n
k
d
il
e
l
r
ed
(H
se
1
m
)–
i
(
g
H
ro
6
u
)
p
, A
a
s
d
s
m
um
its
pt
a
ion
un
H
iqu
o
e
f
Q
[1
S
1
D
] λ⋆ −
u
fee
=
dba
K
ck
(y(cid:98)
l
N
aw
) u
act
∈
uat
U
o
c
r cont
t
r
o
ac
ν
ts
Y
a
(
t
u
γ
)
(u)
ν =ν , with decay rate λ , and
QSD Y 0
∥P (η ∈·|τ >t)−ν ∥ ≤C ϱ(V)e−γt. Fleming–Viot
ϱ t Y TV 0 estimator,N ≥ 2
y(cid:98)N = XN(κu),
Moreover,thestationaryempiricalmeasureoftheN-particle errorO(dN−ϖ)
Fleming–Viot system [15] satisfies Fig. 1: Control structure. The removal input u enters the
E(cid:12) (cid:12)XN(φ)−ν
Y
(φ) (cid:12) (cid:12)≤dN−ϖ∥φ∥
∞
, ϖ =
2(∥κ∥
γ
+γ)
, c
o
o
u
n
tp
d
u
it
t
io
λ
ne
(
d
u
fl
)
ow
is
t
e
h
s
r
t
o
im
ug
a
h
ted
the
by
kill
t
i
h
n
e
g
F
ra
le
te
m
κ
in
u
g
;
–
t
V
h
i
e
ot
re
p
g
a
u
r
l
t
a
i
t
c
e
l
d
e
∞ 0
(4) system (N ≥2) and compared with the target λ⋆.
where d depends on the uniform moment estimate
sup E[XN(V)]≤C/(λ −∥κ∥ ). Finally,
N 1 ∞ III. MAINRESULTS:REACHABLEDECAYRATESAND
λ =ν (κ), (5) MAXIMALACTUATORAUTHORITY
0 Y
This section develops the control theory of childless ac-
a self-consistency identity showing that λ is an estimable
0 tuation. The following lemma isolates the single structural
output.
mismatch from which every limitation below is derived: the
Two consequences of (5) are used repeatedly: inputentersthekillingchannelonly,andthegeneratorofthe
unkilled dynamics, which carries the Foster–Lyapunov drift,
λ =ν (κ)≤∥κ∥ , (6)
0 Y ∞ is left invariant.
with strict inequality whenever P(ξ ≥2)>0, since ν then
Y Lemma 1. Let u≥0 be bounded and measurable. Then:
charges {Z ≥ 2}; and every quasi-stationary distribution ν
(i) the mortality rate of the controlled process is
satisfies ν(κ)≤∥κ∥ .
∞
(cid:2) (cid:3)
κ (η)= p µ(a)+u(a) 1 ,
C. Control problem u 0 {η=δa}
(cid:2) (cid:3)
∥κ ∥ =sup p µ(a)+u(a) ;
u ∞ 0
Preventive removal (culling) acts as an additional age-
a≥0
dependent hazard u(a)≥0: an individual removed this way
(ii) the generator of the unkilled dynamics is invariant on
terminates its lineage, whereas a natural death replaces it by
the singleton stratum:
ξ ∼(p ). Write X for the corresponding unkilled process,
n u
obtained by deleting the transition δ a (cid:55)→ 0, so that u enters L Xu F(δ a )=L X F(δ a ), a≥0,
only through the singleton killing rate κ = p µ+u. The
u 0
plant is the controlled conditioned flow Σ : ϱ˙ = L∗ϱ on for every F in the extended domain.
t u t
P(E), with input u∈L∞ + (R + ). It is autonomous and open- Proof. For a singleton η = δ a , the control input enters the
loop convergent: whenever an admissible Foster–Lyapunov extended generator (1) only through the additional removal
certificate exists (Fact 2), the flow contracts to a unique term u(a)[Φ(0)−Φ(f(a))], yielding
attractor ν (u) at rate γ(u). The regulated output is the
Y LuF(δ )=Φ′(f(a))f′(a)
decay rate of that attractor, y(u) = λ (u) = ν (u)(κ ), a
0 Y u
whichby(5)and(4)isreadfromtheparticlesystemthrough +µ(a) (cid:88) p (cid:2) Φ(nf(0))−Φ(f(a)) (cid:3)
n (7)
y =XN(κ ), with E|y −y|≤d∥κ ∥ N−ϖ. The input
(cid:98)N u (cid:98)N u ∞ n≥0
is constrained to the certifiable class (cid:2) (cid:3)
+u(a) Φ(0)−Φ(f(a)) .
U c :={u∈L∞ + (R + ):X u admits an admissible certificate} Absorption occurs only from singleton states, through either
the childless event, at rate p µ(a), or controlled removal, at
in the sense of Definition 1, for which Theorem 1 gives 0
rate u(a). Hence
an explicit outer bound. The control problem is equilibrium
placement under certifiability (Fig. 1): κ (δ )=p µ(a)+u(a),
u a 0
(i) bound the reachable output set R:={λ (u):u∈U }
0 c whereas κ vanishes outside the singleton stratum. This
and locate its supremum; u
proves(i).Removingtheabsorbingtransitionfrom(7)yields
(ii) foratargetλ⋆ intheinteriorofR,constructanoutput-
f
ν
ee
(
d
λ
b
⋆
a
)
c
,
k
an
la
d
w
bo
u
und
=
th
K
e
(
p
y (cid:98)
la
N
c
)
em
p
e
l
n
ac
t
i
e
n
r
g
ror
th
i
e
n N
att
.
ractor at L Xu F(δ a )=Φ′(f(a))f′(a)+µ(a) (cid:88) p n (cid:2) Φ(nf(0))−Φ(f(a)) (cid:3) ,
Y n≥1

which is independent of u. Therefore, Only proportional actuation u=cµ preserves the Bellman–
Harris structure. Establishing sufficiency for general control
L F(δ )=L F(δ ),
Xu a X a requires the controlled reproductive value satisfying
which proves (ii). □
A f =f′+mµf(0)−(µ+u)f =−λ (u)f, (11)
u 0
Lemma 1 shows that childless actuation can only increase
which we derive only for the proportional family in Sec-
the killing rate κ , thereby tightening the drift condition
u
tion IV. Lemma 1 also shows that the transmission barrier
λ > ∥κ ∥ without modifying the drift itself. The fol-
1 u ∞
is invariant under control and therefore cannot be reached.
lowing theorem translates this structural property into a
It remains to determine how closely the controlled decay
closed-form, control-law-independent characterization of the
rate λ (u) can approach this barrier. The controlled decay
admissible actuator class. 0
rate is characterized through the first-moment dynamics. An
Theorem 1. Assume (H2) and (H4), and let u ≥ 0 be individual born at age 0 produces offspring at age a at rate
bounded and measurable. If X u admits an admissible cer- mµ(a)G¯ u (a), where
tificate (V,λ ,C) in the sense of Definition 1, then
1 (cid:18) (cid:90) a (cid:19)
(cid:2) (cid:3) G¯ (a)=exp − (µ+u) ,
sup p µ(a)+u(a) <λ ≤Λ, (8) u
0 1
a≥0 0
in particular, so that the first-moment decay rate is the unique root of
(cid:90) ∞
u(a)<(1−p 0 )µ ∞ −p 0 µ(a), a≥0. (9) Ψ u (λ):=m eλaµ(a)G¯(a)e−(cid:82) 0 auda=1. (12)
0
Since u is arbitrary, U ⊆U, where
c
Foru=0,thisreducestotheEuler–Lotkaequation,whereas
U :={u≥0:∥κ u ∥ ∞ <Λ}. (10) for u=cµ it becomes
(cid:90)
Proof. ByLemma1(ii),thesingletondriftisindependentof
m eλagG¯cda=1.
the control:
L V(δ )=W′(a)−(1−p )µ(a)W(a)+µ(a)B . We write λ (u) for this root. It is the decay rate ν (u)(κ )
Xu a 0 V 0 Y u
of the conditioned equilibrium whenever Fact 3 applies,
As in Fact 2,
in particular on the proportional family of Section IV by
[λ −(1−p )µ(a)]W(a)≤C Theorem 3; otherwise Theorem 2 is a statement about the
1 0
first moment.
for sufficiently large a, whereas W(a) → ∞ because the
sublevel sets of V are relatively compact. If λ >Λ, choose Theorem 2. Assume (H1), (H2), (H4) and (H5). For every
1
measurable u≥0 with ∥κ ∥ ≤Λ, in particular for every
a →∞ such that µ(a )→µ . Then u ∞
k k ∞
u ∈ U, equation (12) has a unique root λ (u), and 0 <
0
λ 1 −(1−p 0 )µ(a k )−→λ 1 −Λ>0, λ 0 (u)≤Λ. Moreover:
soW(a k )remainsbounded,acontradiction.Henceλ 1 ≤Λ. (i) If u 1 ,u 2 ≥ 0 satisfy ∥κ ui ∥ ∞ ≤ Λ (i = 1,2) and
Together with λ 1 >∥κ u ∥ ∞ , this yields (8), from which (9) u 1 ≤ u 2 pointwise, then λ 0 (u 1 ) ≤ λ 0 (u 2 ), with strict
follows. □ inequality whenever u 1 < u 2 on a set of positive
Lebesgue measure.
Theorem 1 gives necessity only. The converse inclusion
(ii) Let u⋆(a):=Λ−p µ(a). Every u∈U satisfies u<u⋆
U ⊆U holdsonthehazard-proportionalfamily(Theorem3) 0
c pointwise, and u⋆ ∈/ U, yet
and is open in general, so every statement below bounds
certifiable performance from above. supλ (u)=λ (u⋆), (13)
0 0
OnecouldtrytoenlargeU byweakeningthedriftrequire- u∈U
ment λ 1 > ∥κ u ∥ ∞ to λ 1 > oscκ u := supκ u −infκ u , as a supremum that is not attained.
allowed by [11, Rem. 1]. This brings no improvement here: (iii) Let ν⋆ be the unique root of
absorption occurs only from singletons, so κ vanishes on
u (cid:90) ∞
{Z ≥2}, and therefore infκ u =0 and oscκ u =∥κ u ∥ ∞ for m eνaµ(a)G¯(a)1−p0da=1. (14)
every u, including u≡0. The envelope (9) is therefore not
0
caused by the particular norm used in the certificate.
Then λ (u⋆)=Λ+ν⋆, and ν⋆ ≤0 with ν⋆ =0 if and
0
The envelope tightens as the hazard increases, so the only if P(ξ ≥2)=0.
availableauthoritydecreaseswithageandissmallestatages
Combining (ii), (iii) and Theorem 1,
wherethenaturalchildlessratep µ(a)leavestheleastroom
0
below Λ. λ (u) < Λ+ν⋆ ≤ Λ for every u∈U :
0 c
Moreover, the controlled process generally no longer be-
longs to the Bellman–Harris class, since the effective off- certifiablechildlessactuationneverreachesthetransmission
spring mean mµ(a)/[µ(a)+u(a)] becomes age-dependent. barrier, and falls short of it by more than the deficit |ν⋆|.

Proof. Let u ≥ 0 be measurable with u ≤ u⋆. Since m ≥ and hence
1−p , assumption (H2) implies p >0, and therefore Λ= Ψ (λ)=Ψ (λ+ε).
0 0 u⋆ u⋆
ε
(1−p )µ <µ by (H4). Moreover,
0 ∞ ∞ Therefore,
Ψ (λ)≤Ψ (λ), Ψ (λ (u⋆)+ε)=1.
u 0 u⋆ 0 ε
soFact1(i)ensuresthatΨ u isfiniteandcontinuouson[0,Λ]. Since Ψ u⋆ is strictly increasing and admits the unique root
It is also strictly increasing: for λ<λ′ one has eλa <eλ′a λ 0 (u⋆), it follows that
at every a > 0, and by (H1) the measure mµG¯e−(cid:82) 0 ·uda λ (u⋆)=λ (u⋆)−ε.
charges (0,∞). Furthermore, 0 ε 0
(cid:90) ∞ Letting ε↓0 gives
Ψ u (0)=m
µ(a)G¯(a)e−(cid:82)
0
auda
supλ (u)=λ (u⋆),
0 0 0
(cid:90) ∞ u∈U
≤m µ(a)G¯(a) da=m<1.
and the supremum is not attained since u⋆ ∈/ U.
0 (cid:124) (cid:123)(cid:122) (cid:125)
g(a) (iii) By definition, λ 0 (u⋆) is the unique solution of
On the other hand, integrating u≤u⋆ :=Λ−p 0 µ(a) yields
m
(cid:90) ∞ eλaµ(a)G¯(a)e−(cid:82)
0
au⋆
da=1.
e−(cid:82)
0
au ≥e−aΛG¯(a)−p0, 0
Using the expression of u⋆ and the computations already
(cid:90) a
because µ(s)ds=−logG¯(a). Hence established in the proof of the preamble, this equation
0 reduces to
(cid:90) ∞ m (cid:90) ∞
Ψ u (Λ)≥m µ(a)G¯(a)1−p0da= 1−p ≥1. m e(λ0(u⋆)−Λ)aµ(a)G¯(a)1−p0da=1.
0 0 0
The intermediate value theorem therefore yields a unique Define ν⋆ := λ (u⋆)−Λ, then ν⋆ is the unique solution
0
root λ 0 (u)∈(0,Λ]. of (14), and hence λ 0 (u⋆)=Λ+ν⋆.
(i) Let u 1 ,u 2 ≥0 satisfy ∥κ ui ∥ ∞ ≤Λ (i=1,2) and u 1 ≤ Todeterminethesignofν⋆,weevaluateΨ u⋆ atthebarrier
u 2 . Then value λ=Λ:
e−(cid:82)
0
au1 ≥e−(cid:82)
0
au2,
m
Ψ (Λ)= =E[ξ |ξ ≥1]≥1,
u⋆
1−p
with strict inequality whenever u <u on a set of positive 0
1 2
Lebesgue measure. Hence, where the first equality follows from the normalization of
the probability density (1−p
0
)µ(a)G¯(a)1−p0. Since Ψ
u⋆
is
Ψ u1 (λ)≥Ψ u2 (λ) ,∀λ∈[0,Λ], strictlyincreasing,thenλ
0
(u⋆)≤Λ,thatis,ν⋆ ≤0.Finally,
with strict inequality under the same condition. Evaluating m
ν⋆ =0 ⇐⇒ Ψ (Λ)=1 ⇐⇒ =1.
at λ=λ (u ) gives
u⋆
1−p
0 1 0
(cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1) Since
Ψ u2 λ 0 (u 1 ) ≤Ψ u1 λ 0 (u 1 ) =1≡Ψ u2 λ 0 (u 2 ) .
m−(1−p )=
(cid:88)
(n−1)p ,
0 n
Since Ψ is strictly increasing,
u2 n≥2
λ 0 (u 1 )≤λ 0 (u 2 ), the latter equality holds if and only if p k =0 for all k ≥2,
namely P(ξ ≥2)=0. □
with strict inequality whenever u <u on a set of positive
1 2
Remark 1 (What is, and what is not, implied by invariance).
Lebesgue measure.
Lemma1immediatelyyieldsthequalitativebarrierλ (u)<
(ii) Every u∈U satisfies 0
Λ, so this part is indeed built into the modelling hypothesis.
u(a)<u⋆(a):=Λ−p 0 µ(a), The contribution of Theorem 2 is different: it identifies the
exact supremum sup λ (u) = Λ+ν⋆, where the deficit
where u⋆(a) > 0 by (H5). Since ∥κ ∥ = Λ, we have u∈U 0
u⋆ ∞ |ν⋆| is explicitly determined by the offspring law. Three
u⋆ ∈/ U. Moreover, part (i) yields λ (u) ≤ λ (u⋆), and
0 0 ingredientsareneededtoobtainthisresult,andnonefollows
therefore
from the invariance property alone. First, the optimisation
supλ (u)≤λ (u⋆).
0 0 over the infinite-dimensional class U is reduced, through
u∈U
the monotonicity established in Theorem 2(i), to the single
To show that this upper bound is sharp, let
extremal envelope u⋆(a)=Λ−p µ(a). Second, substituting
0
u⋆ :=u⋆−ε, 0<ε<Λ−p µ∗ = inf u⋆(a). (cid:82)a u⋆ =aΛ+p logG¯(a) transforms the controlled Euler–
ε 0 0 0
a≥0 Lotka equation into that of a different Bellman–Harris pro-
Thenu⋆ ≥0.Since∥κ ∥ =Λ−ε<Λ,wehaveu⋆ ∈U. cess, with hazard (1−p )µ and offspring law ξ | ξ ≥ 1.
ε u⋆ ε ∞ ε 0
Furthermore, This transformation is what turns the qualitative barrier Λ
e−(cid:82) 0 au⋆ ε =e−(cid:82) 0 au⋆ eεa, into the computable quantity Λ+ν⋆. Finally, the sign of ν⋆

follows from E[ξ | ξ ≥ 1] ≥ 1, with equality if and only if family falls short of it by ∥κ∥ −λ (0)+ν⋆ >0, and the
∞ 0
P(ξ ≥ 2) = 0, showing that the gap is entirely determined proportional family by more; only the envelope-saturating
by the offspring distribution. For the calibrated model of shapeu⋆ approachesit.Whatseparatesthethreeistheshape
Section VI, the invariance argument gives λ < 0.1400, of the actuator, not the certifiable authority it consumes.
0
whereas Theorem 2 sharpens this to λ ≤0.1050, reducing
0
IV. THEPROPORTIONALACTUATOR:CERTIFIABLE
the admissible range by approximately 25%.
RANGE,SENSITIVITY,ANDCOST
Thenextcorollarycomparesthetwofamiliesthatareused
Theorem1boundseveryadmissibleinput.Forthehazard-
in practice.
proportional actuator u = cµ we now show that this bound
Corollary 1 (Constant versus proportional actuation). As- is also sufficient, the controlled process remaining Bellman–
sume (H1)–(H6). Write λp(c) := λ (cµ) and λcst(c ) := Harrissothatthesufficiencyresultof[1]appliesunchanged.
0 0 0 0
λ (c 1) for c,c ≥ 0. Then cµ ∈ U if and only if Thisyieldsanexplicitcertifiablegaininterval,itssensitivity,
0 0 0
(p +c)µ∗ <Λ, and c 1∈U if and only if c <Λ−∥κ∥ . and the degradation of the certificate near the admissibility
0 0 0 ∞
On the constant family the output is an exact shift of the boundary.ThroughoutthissectionandSectionVIweabbre-
uncontrolled decay rate, viate λ 0 (c):=λp 0 (c)=λ 0 (cµ).
λcst(c )=λ (0)+c , (15) A. The certifiable gain interval
0 0 0 0
Here u = cµ gives total hazard (1+c)µ, survival G¯ =
and the two families are ordered: c
G¯1+c, and an offspring law keeping the natural offspring
sup λp(c) ≤ sup λcst(c ) = Λ− (cid:0) ∥κ∥ −λ (0) (cid:1) , with probability 1/(1+c):
0 0 0 ∞ 0
cµ∈U c01∈U
(16) m = m , p = p0+c,
with strict inequality whenever µ < µ∗ on a set of positive µ∗ c =( 1 1 + + c c)µ∗ 0 , ,c µ 1+c =(1+c)µ . (17)
measure. c ∞,c ∞
Hence ∥κ ∥ = (p + c)µ∗ increases with c, whereas
c ∞ 0
Proof. The proof is split into three steps.
(1 − p )µ = Λ remains constant, reflecting the can-
0,c ∞,c
Admissibility criteria. ∥κ ∥ = sup (p + c)µ(a) =
cµ ∞ a 0 cellation of (1+c) in Lemma 1. The admissibility criterion
(p 0 + c)µ∗ and ∥κ c01 ∥ ∞ = ∥κ∥ ∞ + c 0 , so both criteria of Corollary 1 for this family, (p
0
+c)µ∗ < Λ, therefore
are instances of ∥κ ∥ <Λ.
u ∞ reads c<c with
(cid:82)a max
Proof of (15). Let c ≥ 0. Since c ds = c a, the
0 0 0 0 Λ−p µ∗
definition (12) gives, for every λ, c := 0 , (18)
max µ∗
(cid:90) ∞
Ψ c01 (λ)=m eλaµ(a)G¯(a)e−c0ada which equals 1−2p 0 when µ∗ = µ ∞ . The next theorem
0 shows that this necessary condition is also sufficient.
(cid:90) ∞
=m e(λ−c0)aµ(a)G¯(a)da=Ψ (λ−c ).
0 0 Theorem 3 (Certifiable gain interval). Assume the uncon-
0
trolled process satisfies (H1)–(H6). Then under (17), the
Hence Ψ (λ) = 1 if and only if Ψ (λ−c ) = 1, that is,
c01 0 0 controlled process satisfies (H1)–(H5) and (H6) if and only
if and only if λ−c = λ (0) by uniqueness of the root of
0 0 if c∈[0,c ), with c as in (18). Hence
Ψ . This proves (15). max max
0
(a) for every c<c , all conclusions of Fact 3 hold: the
Consequently c (cid:55)→λcst(c ) is increasing and its supremum max
0 0 0 controlledprocessadmitsaYaglomlimitν (c),globally
over the admissible range c <Λ−∥κ∥ is Y
0 ∞ attractive and estimable at rate N−ϖ; and
sup λcst(c )=λ (0)+Λ−∥κ∥ =Λ− (cid:0) ∥κ∥ −λ (0) (cid:1) , (b) for c ≥ c , no admissible certificate exists, so no
0 0 0 ∞ ∞ 0 max
c01∈U quasi-stationary equilibrium can be certified.
which is the value stated in (16). It lies strictly below Λ
Proof. By (17), (H5) becomes ∥κ ∥ = (p +c)µ∗ < Λ,
whenever P(ξ ≥ 2) > 0, since λ (0) < ∥κ∥ by (6). The c ∞ 0
0 ∞ i.e., c < c by (18). The remaining assumptions hold
supremum is not attained, the admissibility constraint being max
on [0,c ): (H1) G¯1+c is absolutely continuous with full
strict. max
supportanddensity(1+c)µG¯1+cboundedbelowoncompact
Proofof (16).Ifcµ∈U then,foreverya,cµ(a)≤cµ∗ <
subsets of (0,∞); (H2) m ≤m<1; (H3) p =p /(1+
Λ−p µ∗ ≤ Λ−p µ(a), so cµ ≤ Λ−p µ∗ pointwise, i.e. c 1,c 1
0 0 0 c)>0; (H4) is immediate. For (H6), let α be the exponent
cµ ≤ c 1 for c := Λ − p µ∗ = sup{c : c 1 ∈ U}.
Theorem 0 2(i) giv 0 es λp 0 (c) ≤ 0 λc 0 st(c′ 0 ) for 0 every 0 c′ 0 < c 0 f f o o r r c ev = er 0 y . n Th ≥ em 1, o s m o e t n h t a c t o (cid:80) ndit n io α n p isin ≤ he (cid:80) rited n s α in p ce < p n ∞ ,c . ≤ T p h n e
close enough to c , which gives (16). If µ<µ∗ on a set of n n,c n n
0 controlled barrier is Λ =(1−p )µ =Λ by (17). The
positive measure, then cµ<c 0 1 there, and the strict part of controlled Malthusian c parameter 0 s ,c olve ∞ s ,c m (cid:82) eλadG = 1;
Theorem 2(i) applies. □ c c
since dG = (1+c)µG¯1+cda and m = m/(1+c), the
c c
Both families use up the same certifiable authority, in factors (1+c) cancel and this is exactly Ψ (λ)=1, whose
cµ
the sense that ∥κ ∥ ↑ Λ along each of them, yet neither uniquerootisλ (c).ThecontrolledMalthusianparameteris
u ∞ 0
approachesthesupremumΛ+ν⋆ofTheorem2.Theconstant therefore λ (c) itself. Monotonicity (Theorem 2(i)) applied
0

to 0≤cµ then gives αλ (c)≥αλ (0)>Λ=Λ , the strict which is exactly (19). Because ∂ Ψ>0 and ∂ Ψ<0, one
0 0 c λ c
inequality being (H6) for c=0; the same α therefore serves has λ′(c)>0, so λ is strictly increasing.
0 0
for all gains. Part (a) follows from Fact 3, the controlled The existence of
processbeingBellman–Harriswithparameters(17).For(b),
λmax = lim λ (c)
let c ≥ c max . Then ∥κ c ∥ ∞ = (p 0 + c)µ∗ ≥ Λ by (18), 0 c↑cmax 0
whereas any admissible certificate would give ∥κ ∥ <
c ∞ follows from monotonicity together with the uniform bound
λ ≤Λ by Theorem 1. As a conclusion, no such certificate
1 λ (c) ≤ Λ (Theorem 2). Since c µ ∈/ U, this limit is not
exists. □ 0 max
attained.
Remark 2 (Certificate versus existence). Theorem 3(b) con- Finally,
cerns loss of the certificate, not of the equilibrium. At the (cid:90) t
first-moment level the Malthusian parameter λ (c) is still
|logG¯(t)|= µ(s)ds≤µ∗t,
0
0
defined by (12) well beyond c : by renewal theory, or
max
so that
by [12, Thm. 3.8], and quantitatively up to c¯ of (21) by
lb λ′(c)≤µ∗.
Remark 3. What is lost beyond c are the contraction and 0
max
estimation guarantees of Fact 3, which rest on the measure- Integrating this differential inequality from 0 to c gives
valued lift. Whether the Yaglom limit ν Y (c) itself persists (cid:90) c
there remains open. λ (c)−λ (0)= λ′(s)ds≤µ∗c,
0 0 0
0
B. Sensitivity and reachable decay rates which proves (20). □
Proposition 1 (Sensitivity and reachable set). Assume (H1),
Remark 3 (Strict separation). Theorem 2(iii) already sep-
(H2), (H4), (H5). On [0,c ), the map c (cid:55)→ λ (c) is C1,
max 0 arates the reachable set from Λ; within this family the
with
separation can also be read off the gain axis. Only the
(cid:90) ∞
eλ0(c)tgG¯c|logG¯|dt intermediate-value step of Fact 1(ii) uses (H5), and for the
λ′(c)= 0 ∈(0,µ∗], (19) controlled process it requires
0 (cid:90) ∞
teλ0(c)tgG¯cdt Λ>(1−m )µ∗ =(1+c−m)µ∗
c c
0
by (17), that is, c<c¯ with
so λ is strictly increasing. Hence the reachable set within lb
0
the proportional family is [λ (0),λmax), where λmax := Λ (cid:88)
0 0 0 c¯ := −(1−m)=c + (n−1)p ≥ c , (21)
lim λ (c) exists by monotonicity and the bound λ ≤ lb µ∗ max n max
c↑cmax 0 0
n≥2
Λ, and is not attained. Moreover
since
λ 0 (c)≤λ 0 (0)+µ∗c. (20) m−(1−p 0 )= (cid:88) (n−1)p n ,
Proof. Let n≥2
(cid:90) ∞ withequalityifandonlyifξ ∈{0,1}almostsurely(theother
Ψ(c,λ):=m eλtg(t)G¯(t)cdt. requirement, Λ<µ , holds because 1−p <1≤1+c).
∞,c 0
0 Thus the ceiling λ (c)<Λ survives on [0,c¯ )⊇[0,c ):
0 lb max
Fix 0 ≤ c < c < c . Since λ (c) ∈ (0,Λ] for every c, the certificate is lost strictly before any gain in this family
1 2 max 0
it suffices to work on [c ,c ]×[0,Λ], a fixed compact set. could drive λ to the transmission barrier.
1 2 0
There the integrand and its partial derivatives in c and λ are
bounded in modulus by (1+t+µ∗t)eΛtg(t)G¯(t)c1, using C. The cost of certifiability
G¯c ≤ G¯c1 and |logG¯(t)| = (cid:82)t µ ≤ µ∗t; this majorant Reference [1] removes the particle-number threshold
0
is integrable because (1 + t + µ∗t)eΛt ≤ C eθt for any of [11, Thm. 2.3], so (4) holds for every N ≥ 2. What
θ
θ ∈ (Λ,µ ), and (cid:82) eθtdG < ∞ by Fact 1(i). Hence degrades, unboundedly, is the guaranteed constant.
∞
differentiation under the integral sign is justified, so that Ψ We first introduce and fix some constants. For a gain c,
is C1. let (V,λ 1 (c),C c ) be an admissible certificate for X cµ in the
(cid:90) ∞ senseofDefinition1;theassociateduniformmomentbound
∂ Ψ(c,λ)=m teλtg(t)G¯(t)cdt>0, of Fact 3 is B :=C /(λ (c)−∥κ ∥ ). We write γ(c) for
λ c c 1 c ∞
0 the contraction rate and ϖ := γ(c)/[2(∥κ ∥ +γ(c))] ∈
c c ∞
and (0,1)fortheexponentof(4)atgainc,andd ,C forthetwo
2 0 0
(cid:90) ∞ constants of [11, §4.3], which depend only on the particle
∂ Ψ(c,λ)=−m eλtg(t)G¯(t)c|logG¯(t)|dt<0.
c system and not on c.
0
Sinceλ (c)ischaracterizedbyΨ(c,λ (c))=1,theimplicit Proposition 2 (Divergence of the certified guarantee). Let
0 0
function theorem yields that c(cid:55)→λ 0 (c) is of class C1, with c∈[0,c max )andletλ 1 (c)bethedriftrateofanyadmissible
Lyapunov function for the controlled process. Then
∂ Ψ(c,λ (c))
λ′(c)=− c 0 ,
0 ∂ λ Ψ(c,λ 0 (c)) λ 1 (c)−∥κ c ∥ ∞ ≤ µ∗(c max −c), (22)

so no admissible certificate can guarantee, through Fact 3, A. The projected gain law
a moment bound smaller than C /[µ∗(c −c)]. Assume
c max Proposition 3 (ISS of the certainty-equivalence gain law).
in addition that the certificate constant and the contraction Fix c <c and let ℓ:=min λ′(c)>0, which ex-
rate do not degenerate on the gain range: inf [0,cmax) C c >0 istsa 1 ndisp m o a s x itivebyProposition c∈ 1 [0 . , L c1 e ] tλ 0 ⋆ ∈[λ
0
(0),λ
0
(c
1
)]
and 0 < γ − ≤ γ(c) ≤ γ + < ∞. Then the particle number andc⋆ :=λ−1(λ⋆).Supposetheestimatorerrorisuniformly
needed for a fixed accuracy ϵ obeys 0
bounded on the gain range,
N ϵ (c) ≥ K ϵ (c)(c max −c)−2∥κc∥∞/γ(c) −
c
−
↑c
−
m
−
a
→
x
∞, (23) (cid:12) (cid:12)λ(cid:98) N
0
(c)−λ
0
(c) (cid:12) (cid:12)≤e
N
for all c∈[0,c
1
], (25)
where and let c(·) solve the projected gain update
(cid:98)
K ϵ (c):= (cid:104)∥κ c ϵ ∥ ∥ ∞ κ + ∥ γ(c) d 0 2ϖc (cid:16)C µ 0 C ∗ c (cid:17)1−2ϖc (cid:105)1/ϖc . (24) (cid:98) c˙ =kΠ [0,c1] (cid:0) (cid:98) c, λ⋆−λ(cid:98) N 0 ( (cid:98) c) (cid:1) , k >0, (26)
c ∞
where Π zeroes the velocity component pointing out of
TheprefactorK
ϵ
(c)isboundedawayfromzerouniformlyin
[0,c ].Th
[0
e
,c
n
1]
[0,c ]isforwardinvariantand,foreveryc(0)∈
c, each factor in (24) being so, and the exponent in (23) lies 1 1 (cid:98)
[0,c ],
in the fixed interval [2∥κ∥ /γ , 2Λ/γ ]; the divergence is 1
∞ + −
therefore carried by the exponent alone. | (cid:98) c(t)−c⋆| ≤ | (cid:98) c(0)−c⋆|e−k 2 ℓt + 2ℓ−1e N , t≥0. (27)
Proof. By Theorem 1 applied to u = cµ, any admissible
Hence (26) is ISS with respect to the estimation error, with
λ (c) satisfies ∥κ ∥ < λ (c) ≤ Λ; with ∥κ ∥ = (p +
1 c ∞ 1 c ∞ 0 linear asymptotic gain 2ℓ−1, and any equilibrium of (26)
c)µ∗ from (17) and c of (18), Λ−∥κ ∥ =Λ−(p +
max c ∞ 0 in the interior of [0,c ] satisfies the sharper static bound
c)µ∗ =µ∗(c −c),whichis(22);themomentboundB is 1
max c |c−c⋆|≤ℓ−1e .
thereforeatleastC
c
/[µ∗(c
max
−c)].MinimisingAe∥κc∥∞t+ (cid:98) N
C B e−γ(c)t over t > 0, with A := d N−1/2, as in [11, Proof. Write e(t) := c(t)−c⋆, W := 1e2, and v := λ⋆−
0 c 0 (cid:98) 2
c § o 4 n .3 s ] t , an g t iv o e f s t ( h 4 e ) v s a a l t u is e fie ∥ s κc ∥ d ∥ κ ∞ c ∝ ∥ + ∞ γ B (c) c 1 A − 2 2 ϖ ϖ c c ( . C T 0 h B e c n )1 d − N 2ϖ − c ϖ , c so ≤ the ϵ λ r (cid:98) e N 0 ad ( s (cid:98) c) (cid:98) c˙ f = or k t Π he [0, u c n 1] p ( r (cid:98) c o , j v e ) c . ted velocity direction, so that (26)
gives N ≥ (d/ϵ)1/ϖc, and substituting the lower bound on Step1:theprojectionneverincreases|e|.Byconstruction
B yields (23)–(24), the exponent being (1−2ϖ )/ϖ = Π (c,v) = v unless c = 0 with v < 0, or c = c with
c c c [0,c1] (cid:98) (cid:98) (cid:98) 1
2∥κ ∥ /γ(c). Uniformity follows from ∥κ∥ ≤ ∥κ ∥ < v >0,inwhichcasesitvanishes.Inthefirstcasee=−c⋆ ≤
c ∞ ∞ c ∞
Λ and γ ≤γ(c)≤γ . □ 0 and v <0, so ev ≥0; in the second e=c −c⋆ ≥0 and
− + 1
v > 0, so again ev ≥ 0. In both cases eΠ (c,v) = 0 ≤
Thus c is not crossed at constant cost: by (23) the
[0,c1] (cid:98)
max ev. Therefore
certified accuracy degrades at an algebraic rate set by the
ratio ∥κ ∥ /γ(c), so the last part of the admissible range is W˙ =ec˙ =keΠ (c,v) ≤ kev, (28)
c ∞ (cid:98) [0,c1] (cid:98)
of little practical use, even though it is formally certifiable:
and [0,c ] is forward invariant, so c(t) stays in the range
the gain limit can be read as a loss of robustness margin. 1 (cid:98)
where (25) holds.
V. CERTAINTY-EQUIVALENCEFEEDBACK Step 2: decomposition of the velocity. Since λ⋆ =λ 0 (c⋆),
Sections III and IV answer question (i) of Section II-C: v =− (cid:2) λ
0
(
(cid:98)
c)−λ
0
(c⋆) (cid:3) + (cid:2) λ
0
(
(cid:98)
c)−λ(cid:98) N
0
(
(cid:98)
c) (cid:3) ,
they say which decay rates can be reached, and at what (cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
certified cost. We now turn to question (ii) and build a =:A =:δ
feedback law that places the conditioned equilibrium at a where|δ|≤e by(25).ByProposition1,λ isC1 on[0,c ]
N 0 1
chosen target. The problem differs from ordinary regulation with λ′ ≥ℓ, so the mean value theorem gives A=λ′(ξ)e
0 0
in two ways. The plant does not need to be stabilised, so for some ξ between c⋆ and c, so that
(cid:98)
the loop picks the attractor instead of creating it. And the
eA=λ′(ξ)e2 ≥ ℓe2.
regulatedoutputisnevermeasureddirectly:allwehaveisthe 0
particle estimate λ(cid:98)N
0
= XN(κ
cµ
), with the accuracy given
Step3:adecayinequalityoutsidearesidualset.Combin-
by Fact 3.
ing the two displays with eδ ≤|e|e ,
N
Thissuggestsacertainty-equivalencelaw:usetheestimate
in place of the unknown λ 0 (c), and integrate the output ev =−eA+eδ ≤ −ℓe2+|e|e N =−|e| (cid:0) ℓ|e|−e N (cid:1) .
error. One more ingredient is needed. The gain must stay in
a compact interval [0,c 1 ] with c 1 < c max , and the reason Assume |e|≥ 2e ℓ N. Then e N ≤ ℓ| 2 e|, so ℓ|e|−e N ≥ ℓ| 2 e| and
is not actuator saturation. By Theorem 3(b) there is no
ℓ
admissiblecertificateoncec≥c ,sotheestimatelosesits ev ≤ − e2 =−ℓW.
max 2
guaranteeexactlywheretheinputconstraintbecomesactive.
We therefore enforce the constraint of Theorem 1 inside the With (28) this yields
l t o h o e p s , e a n s si a ng pr a o c j c e u ct r i a o c n y . , T as he P m ro a p r o g s i i n tio c m n a 2 x − sh c o 1 w i s s . what pays for W˙ ≤ −kℓW whenever |e|≥ 2e N. (29)
ℓ

Step 4: invariance of the residual set and conclusion. Let Step 4: conclusion. Let S := {|y| ≤ 2e } and T :=
N
inf{t ≥ 0 : y(t) ∈ S}, with T = +∞ if y never enters
S :=
(cid:8)
|e|≤
2e N(cid:9)
and T :=inf{t≥0: e(t)∈S}, S. On [0,T) the comparison lemma applied to (32) gives
ℓ
V(t) ≤ V(0)e−kℓt, that is, |y(t)| ≤ |y(0)|e−k 2 ℓt. On the
with T = +∞ if the infimum is over an empty set. On boundary of S we have V˙ < 0 by (32), so S is forward
[0,T) the bound (29) applies, and the comparison lemma
invariant and |y(t)|≤2e for t≥T. In both regimes
gives W(t)≤W(0)e−kℓt, that is, N
(cid:110) (cid:111)
|e(t)| ≤ |e(0)|e−k 2 ℓt, t<T. |y(t)| ≤ max |y(0)|e−k 2 ℓt, 2e N ≤ |y(0)|e−k 2 ℓt +2e N ,
which is (30). □
On the boundary of S we have W˙ ≤ −kℓW < 0 by (29),
so S is forward invariant and |e(t)|≤ 2eN for all t≥T. In B. Tuning, and the role of the estimator
ℓ
either case Proposition 3 and Corollary 2 treat λ(cid:98)N as an external
0
|e(t)| ≤ max (cid:110) |e(0)|e−k 2 ℓt, 2e N (cid:111) ≤ |e(0)|e−k 2 ℓt+ 2e N, signalofknownaccuracy.Twoquestionsareleftopenbythat
ℓ ℓ reading: how fast the loop may be run before the estimator
which is (27). can no longer follow it, and how the bound (25) relates to
Step 5: interior equilibria. If c is an equilibrium in the what Fact 3 actually provides. We take them in turn.
(cid:98)
interior of [0,c ] then Π acts as the identity, so v = 0, Choice of k and timescale separation: The residual terms
1 [0,c1]
in (27) and (30) do not depend on k; the gain only fixes
i
|A
.e.
|=
λ(cid:98)N
0 |δ
(
(cid:98)
c
|
)
≤
=
e N
λ
,
⋆
t
.
h
H
at
e
i
n
s
c
,
e
|e
A
|≤
=
e ℓ N
−
.
δ and, by Steps 2, ℓ|e| ≤
□ t i h n e th r e ate an k a 2 ℓ lys a i t s w th h e i r c e h fo t r h e e p i r n e i v ti e a n l ts er t r a o k r in i g s f k or a g r o b t i t t e r n ar . il N y o l t a h r i g n e g ,
The regulated variable is not the gain but the decay rate which cannot be correct: the particle system needs a time of
it produces, and for that variable the sensitivity constant order 1 tosettle,and(25)describesitsstationaryempirical
γ(c)
disappears. measure, not its transient. The law (26) is thus meaningful
only when kℓ ≪ γ(c), so that the estimator can follow the
Corollary 2 (Placement error). Under the hypotheses of
current gain. Removing this separation would require the
Proposition 3,
singular-perturbation framework of [27] together with the
(cid:12) (cid:12)λ 0 ( (cid:98) c(t))−λ⋆(cid:12) (cid:12) ≤ (cid:12) (cid:12)λ 0 ( (cid:98) c(0))−λ⋆(cid:12) (cid:12)e−k 2 ℓt +2e N , t≥0. ISSsmall-gaintheoremof[26],andwouldalsoneedalower
(30) bound on γ(c), which is not available (Section VII).
Theasymptoticplacementerroristhereforeatmosttwicethe From the particle bound to (25): Hypothesis (25) holds
estimator error, however sensitive λ may be to the gain. pathwise and uniformly in c, whereas Fact 3 gives, for
0
Proof. Write y(t):=λ 0 ( (cid:98) c(t))−λ⋆, V := 1 2 y2, and let v :=
e
d
a
∥
c
κ
h
c ∥
fi
∞
xe
N
d
−
c
ϖ
, a
≤
bo
d
u
Λ
nd
N
i
−
n
ϖ
ex
b
p
y
ec
(
t
8
a
)
t
.
io
R
n
e
:
a
E
d
|λ(cid:98)
e N
N
0
(
a
c
s
)−
the
λ
0 ra
(c
n
)
d
|
om
≤
λ⋆ S − tep λ(cid:98)N 0 1 ( : (cid:98) c) a be sc a a s la i r n t e h q e ua p t r i o o o n f o fo f r Pr th o e pos o i u ti t o p n ut 3. error. Since i q n ua ( n 2 t 7 i ) ty an s d up (3 c∈ 0) [0, t c h 1 e ] n |λ(cid:98) g N 0 iv ( e c s ) − λ 0 (c)|. Taking expectations
λ⋆ =λ (c⋆), Step 2 of that proof gives v =−y+δ, where
δ :=λ 0 0 ( (cid:98) c)−λ(cid:98)N 0 ( (cid:98) c) and |δ|≤e N by (25). Differentiating y lim t→ s ∞ upE(cid:12) (cid:12)λ 0 ( (cid:98) c(t))−λ⋆(cid:12) (cid:12)≤2E[e N ], (33)
along (26),
y˙ =λ′ 0 ( (cid:98) c) (cid:98) c˙ =kλ′ 0 ( (cid:98) c)Π [0,c1] ( (cid:98) c,v).
lim
t→
s
∞
upE(cid:12) (cid:12)(cid:98) c(t)−c⋆(cid:12) (cid:12)≤ 2E[
ℓ
e N ] . (34)
Step2:theprojectionneverincreases|y|.Theprojectionis The gap is that Fact 3 controls sup c E|λ(cid:98)N 0 (c) − λ 0 (c)|,
inactiveexceptat (cid:98) c=0withv <0,orat (cid:98) c=c 1 withv >0. whereas (33)–(34) need
E(cid:2)
sup c | · |
(cid:3)
, a strictly stronger
Inthefirstcasey =λ (0)−λ⋆ ≤0,sinceλ⋆ ≥λ (0);inthe quantity.
0 0
second y =λ (c )−λ⋆ ≥0, since λ⋆ ≤λ (c ). Either way One hypothesis of the design is not covered by either
0 1 0 1
yv ≥0,whileyΠ (c,v)=0.HenceyΠ (c,v)≤yv remark. Placing the decay rate is only useful if it places
at all times, and λ
[
′
0,c
>
1]
0
(cid:98)
gives
[0,c1] (cid:98)
the equilibrium itself, and this requires c (cid:55)→ ν Y (c) to be
0
TV-Lipschitz on [0,c ]: with constant L , (34) gives
1 ν
V˙ =yy˙ ≤ kλ′(c)yv. (31)
Step 3: decay outside a residua 0 l (cid:98) set. From v = −y +δ limsupE(cid:13) (cid:13)ν Y ( (cid:98) c(t))−ν Y (c⋆) (cid:13) (cid:13) TV ≤ 2L ν E ℓ [e N ] .
t→∞
and yδ ≤|y|e ,
N NoquantitativeformofthisLipschitzpropertyisavailableat
yv =−y2+yδ ≤ −|y| (cid:0) |y|−e (cid:1) . present, and we state it as an assumption rather than derive
N
it.
Suppose |y| ≥ 2e . Then e ≤ |y|, so |y|−e ≥ |y| and
yv ≤ −y2 = −V
N
. Since λ
N
′ ≥
2
ℓ on [0,c ] a
N
nd yv
2
≤ 0,
VI. NUMERICALILLUSTRATION:FOOT-AND-MOUTH
2 0 1 SURVEILLANCE
inequality (31) yields
Weusethemodelcalibratedin[1]tothe2001northCum-
V˙ ≤ −kℓV whenever |y|≥2e . (32) brian foot-and-mouth outbreak. An individual is an infected
N

| TABLE | II: Reachable |     | decay | rates | by actuator |     | shape, cali- |     |     |     |     |     |     |     |
| ----- | ------------- | --- | ----- | ----- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
(A) certifiable envelope & actuator shapes
bratedFMDmodel.Allentriesbyquadratureon(12);barrier
| Λ=0.1400 | d−1. |     |     |     |     |     |     | )1  | barrier ¤ |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
¡ 0.14
d( )a(u drazah lavomer
|                          |     |     |     |        | (d−1) |      |          |      |     |     |     |     | envelope u⋆=¤      | p0¹ |
| ------------------------ | --- | --- | --- | ------ | ----- | ---- | -------- | ---- | --- | --- | --- | --- | ------------------ | --- |
| actuator                 |     |     |     | supλ0  |       | %ofΛ | 1/λ0 (d) | 0.12 |     |     |     |     |                    | ¡   |
| none,u≡0                 |     |     |     | 0.0235 |       | 16.8 | 42.6     |      |     |     |     |     | proportional cmax¹ |     |
| proportional,u=cµ,c→cmax |     |     |     | 0.0390 |       | 27.8 | 25.7     |      |     |     |     |     | constant ¤         | ∙   |
0.09
| constant,u≡c0→0.030      |     |     |     | 0.0535 |     | 38.2 | 18.7 |      |     |     |     |     | unused    | ¡k k1 |
| ------------------------ | --- | --- | --- | ------ | --- | ---- | ---- | ---- | --- | --- | --- | --- | --------- | ----- |
| envelope-saturating,u→u⋆ |     |     |     | 0.1050 |     | 75.0 | 9.5  | 0.06 |     |     |     |     | authority |       |
| barrier(unattainable)    |     |     |     | 0.1400 |     | 100  | 7.1  |      |     |     |     |     |           |       |
0.03
| premises, | its lifetime |     | the infectious |     | period, | its offspring | the | 0.00 |     |     |     |     |     |     |
| --------- | ------------ | --- | -------------- | --- | ------- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
premises it infects, so m = R . The infectious period is 0 5 10 15 20 25 30 35 40
eff
|            | E[T]       |     |       |       |        |         |           |     |     |     | age a (days) |     |     |     |
| ---------- | ---------- | --- | ----- | ----- | ------ | ------- | --------- | --- | --- | --- | ------------ | --- | --- | --- |
| Γ(2,θ)     | with       | =   | 8 d,  | hence | θ =    | 4 d and | µ(a) =    |     |     |     |              |     |     |     |
| a/[θ(θ+a)] | increasing |     | to µ∗ | = µ   | = 0.25 | d−1;    | offspring |     |     |     |              |     |     |     |
∞
e−m;
| are Poisson, | so  | p 0 = |     | the decline | of  | the | surveillance |     |     |     |     |     |     |     |
| ------------ | --- | ----- | --- | ----------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
(B) reachable decay rate by actuator shape
| recordgivesλ |     | =0.0235d−1 |     | and,byEuler–Lotkainversion |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
| m = (1 | − λ θ)2, | m   | = 0.8208   |     | and p   | = 0.4401. | Then       |         |     |     |     |                               |     |        |
| ------ | -------- | --- | ---------- | --- | ------- | --------- | ---------- | ------- | --- | --- | --- | ----------------------------- | --- | ------ |
|        | 0        |     |            |     | 0       |           |            |         |     |     |     | barrier ¤=0:14 (unattainable) |     |        |
| ∥κ∥ =  | 0.1100   | and | Λ = 0.1400 |     | d−1, so | (H5)      | holds with | )1 0.14 |     |     |     |                               |     |        |
| ∞      |          |     |            |     |         |           |            |         |     |     |     |                               |     | 0.1049 |
margin 0.0300 d−1; (H6) holds for every α > 5.96 (the ¡ 0.12 75%
|     |     |     |     |     |     |     |     | d(  |     |     |     | 2:69 by reshaping |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- |
£
| companion’s   | weaker     |     | form     | requires    | only | α >     | 4.68), the | ¸ elbahcaer 0 0.09 |        |     |        |        |     |     |
| ------------- | ---------- | --- | -------- | ----------- | ---- | ------- | ---------- | ------------------ | ------ | --- | ------ | ------ | --- | --- |
| Poisson       | law having | all | moments. |             |      |         |            |                    |        |     |        | 0.0535 |     |     |
|               |            |     |          |             |      |         |            |                    |        |     | 0.0390 | 38%    |     |     |
| The envelope. |            | By  | (9) the  | certifiable |      | removal | hazard is  | 0.06               |        |     |        |        |     |     |
|               |            |     |          |             |      |         |            |                    | 0.0235 |     | 28%    |        |     |     |
u⋆(a)
| bounded   | by     | =    | 0.1400   | − 0.4401µ(a), |          | falling | from      | 0.03 | 17% |     |     |     |     |     |
| --------- | ------ | ---- | -------- | ------------- | -------- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| 0.140 d−1 | at age | zero | to 0.030 | d−1           | at large | ages    | (Table I, |      |     |     |     |     |     |     |
0.00
Fig. 2A): a freshly infected premises may be culled preven- none prop. const. envelope
tivelyatupto0.14perday,along-standingoneatonly0.03, u 0 c c max c 0! ¤ ∙ u⋆
|         |          |      |             |           |     |         |        |         |         | ´           | !        |       | ¡k k1 |      |
| ------- | -------- | ---- | ----------- | --------- | --- | ------- | ------ | ------- | ------- | ----------- | -------- | ----- | ----- | ---- |
| because | at large | ages | the natural | childless |     | removal | p µ(a) |         |         |             |          |       |       |      |
|         |          |      |             |           |     |         | 0      | Fig. 2: | (A) The | certifiable | envelope | u⋆(a) | = Λ−p | µ(a) |
0
has already consumed almost all the margin. (shaded: admissible) and the three actuator shapes. The
| TABLEI:Certifiableremovalenvelopeu⋆(a)=Λ−p |     |     |     |     |     |     | µ(a), |                                                     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                            |     |     |     |     |     |     | 0     | proportionalcommandincreaseswithagewhiletheenvelope |     |     |     |     |     |     |
calibrated FMD model. decreases, so it saturates at large ages and leaves author-
|         |     |     |     |     |     |     |     | ity unused | at  | small ones. | (B) | The resulting |     | decay rates |
| ------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- | ------------- | --- | ----------- |
| agea(d) |     | 0   | 2   | 4   | 8   | 16  | ∞   |            |     |             |     |               |     |             |
µ(a)(d−1) 0 0.083 0.125 0.167 0.200 0.250 against the barrier Λ, invariant under childless actuation; the
u⋆(a)(d−1) 0.140 0.103 0.085 0.067 0.052 0.030 supremum over all certifiable actuators is Λ+ν⋆ (Thm. 2),
|           |     |       |         |         |      |     |            | approached, | but | not attained, | by  | saturating | the envelope. |     |
| --------- | --- | ----- | ------- | ------- | ---- | --- | ---------- | ----------- | --- | ------------- | --- | ---------- | ------------- | --- |
| Comparing | the | three | shapes. | Solving | (12) | by  | quadrature |             |     |               |     |            |               |     |
forthethreeshapesgivesTableII.Theproportionalactuator,
| admissible | up to | c max | = 1−2p | 0 = | 0.1199       | by (18), | attains  |           |      |     |         |         |             |        |
| ---------- | ----- | ----- | ------ | --- | ------------ | -------- | -------- | --------- | ---- | --- | ------- | ------- | ----------- | ------ |
| λ = 0.0390 | d−1,  | i.e.  | 27.8%  | of  | the barrier; | the      | constant |           |      |     |         |         |             |        |
| 0          |       |       |        |     |              |          |          | Feedback. | Take | c 1 | = 0.11, | leaving | a certified | margin |
actuator,admissibleupto0.0300d−1,attains0.0535exactly,
|     |     |     |     |     |     |     |     | µ∗(c | −c )=0.0025 |     | d−1 and | giving | ℓ=min | λ′ =     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ------- | ------ | ----- | -------- |
|     |     |     |     |     |     |     |     | max  | 1           |     |         |        |       | [0,c1] 0 |
in accordance with the shift identity (15) of Corollary 1; 0.128.ByCorollary2theasymptoticplacementerroronthe
| and the | envelope-saturating |        |     | value | Λ + | ν⋆ = | 0.1050 of |            |       |      |              |     |          |           |
| ------- | ------------------- | ------ | --- | ----- | --- | ---- | --------- | ---------- | ----- | ---- | ------------ | --- | -------- | --------- |
|         |                     |        |     |       |     |      |           | decay rate | is at | most | 2e , whereas | by  | (27) the | gain only |
|         |                     | 75.0%, |     |       |     |      |           |            |       |      | N            |     |          |           |
Theorem 2(iii), i.e. is approached but not attained, settles within 2e N = 15.6e of c⋆. The loop therefore in-
|         |           |     | E[ξ |       |      |        |           |     |     | ℓ   | N   |     |     |     |
| ------- | --------- | --- | --- | ----- | ---- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| with ν⋆ | = −0.0351 | and |     | | ξ ≥ | 1] = | 1.466. | Reshaping |     |     |     |     |     |     |     |
heritstheestimatoraccuracyontheregulatedoutputwithout
| the actuator | gives           | a factor |            | 2.69 in | decay | rate        | at the same |                                   |     |     |     |                      |     |     |
| ------------ | --------------- | -------- | ---------- | ------- | ----- | ----------- | ----------- | --------------------------------- | --- | --- | --- | -------------------- | --- | --- |
|              |                 |          |            |         |       |             |             | amplification,andpaysthefactorℓ−1 |     |     |     | onlyonthegainitself. |     |     |
| level of     | certifiability, |          | and brings | the     | mean  | persistence | of the      |                                   |     |     |     |                      |     |     |
conditioned outbreak from 25.7 down to 9.5 days. Scope. Under Poisson offspring with µ∗ = µ , (H5)
∞
The proportional family in detail. Here λ′(0) = 0.130 reads m > log2, so with (H2) the admissible range is
0
and λ′ ≈ 0.128 as c ↑ c , well below the rough bound R ∈ (log2,1) = (0.693,1): the weakly subcritical range,
| 0   |     |     | max |     |     |     |     | eff |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ∗ = 0.25 of Proposition 1, and λ (0)+µ∗c = 0.0535 where an outbreak lasts long enough for ν to be the right
|     |     |     |     |     | 0   | max |     |     |     |     |     |     | Y   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is exactly the constant-actuator supremum, as Corollary 1 reference, and where our calibration sits. Within that band
predicts. Numerically λ (c) meets the barrier only at c¯ = c = 1−2e−m is increasing in m, from 0 at m ↓ log2
|     |     |     | 0   |     |     |     |     | max |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.9353, about 7.8 times c and well past the separation to 1 − 2e−1 = 0.264 at m ↑ 1: certifiable authority is
max
bound c¯ = 0.3808 of Remark 3: within this family the smallest where the population is most strongly subcritical.
lb
actuator is stopped by certifiability, not by physics. By Therestrictionm>log2isapropertyofthemeasure-valued
µ∗(c
Proposition 2 the certified margin max −c) falls from lift [1, Rem. 3.10], not a statement about the epidemic. In
0.0300 at c = 0 to 0.0025 at c = 0.11 and 0.0012 at practice,removalgivesalimitedspeed-upandanequilibrium
c=0.115,sotheguaranteedmomentboundbecomestwelve that can be certified and monitored, whereas vaccination or
and twenty-five times larger. movement restrictions act on m and move the ceiling itself.

|         | VII.  | CONCLUSIONSANDPROSPECTS |                 |     |         |        |     |                |     | REFERENCES        |           |                |                |     |
| ------- | ----- | ----------------------- | --------------- | --- | ------- | ------ | --- | -------------- | --- | ----------------- | --------- | -------------- | -------------- | --- |
|         |       |                         |                 |     |         |        |     | [1] O. Arezki, |     | P.-M. Grollemund, | and       | A. Zemouche,   | “Fleming–Viot  |     |
| We have | shown |                         | that preventive |     | removal | acting | on  | a              |     |                   |           |                |                |     |
|         |       |                         |                 |     |         |        |     | selection      | of  | the Yaglom        | limit for | age-structured | Bellman–Harris |     |
subcriticalage-structuredbranchingpopulationhasalimited
processes,withapplicationtolivestockepidemicsurveillance,”2026.
arXiv:2607.29251;hal-05707769.
| authority | over | its conditioned |     | equilibrium, | and      | that | the limit |           |        |                   |     |                |     |             |
| --------- | ---- | --------------- | --- | ------------ | -------- | ---- | --------- | --------- | ------ | ----------------- | --- | -------------- | --- | ----------- |
|           |      |                 |     |              |          |      |           | [2] M. M. | Seron, | J. H. Braslavsky, | and | G. C. Goodwin, |     | Fundamental |
| comes     | from | the structure   |     | of the       | problem. | The  | input is  |           |        |                   |     |                |     |             |
LimitationsinFilteringandControl.London:Springer,1997.
matchedtothekillingratebutunmatchedwithrespecttothe [3] H.W.Bode,NetworkAnalysisandFeedbackAmplifierDesign.New
Foster–Lyapunov drift (Lemma 1), which yields a closed- York:VanNostrand,1945.
|                               |     |     |     |       |            |     |        | [4] J. S. | Freudenberg | and D. | P. Looze, | “Right | half plane | poles and |
| ----------------------------- | --- | --- | --- | ----- | ---------- | --- | ------ | --------- | ----------- | ------ | --------- | ------ | ---------- | --------- |
| form, control-law-independent |     |     |     | input | constraint | set | (Theo- |           |             |        |           |        |            |           |
zerosanddesigntradeoffsinfeedbacksystems,”IEEETrans.Autom.
rem 1) and, through the monotonicity of the input–output Control,vol.30,no.6,pp.555–565,1985.
map, the exact supremum Λ + ν⋆ of the reachable decay [5] G. Stein, “Respect the unstable,” IEEE Control Syst. Mag., vol. 23,
|     |     |     |     | |ν⋆| |     |     |     | no.4,pp.12–25,2003. |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
rates (Theorem 2). The deficit is explicit and is set by [6] R. Bellman and T. E. Harris, “On the theory of age-dependent
theoffspringlawalone.Alongtheadmissibilityboundarythe stochasticbranchingprocesses,”Proc.Natl.Acad.Sci.USA,vol.34,
achievabledecayrateissetbytheshapeoftheactuatorrather pp.601–604,1948.
|          |                 |     |       |           |      |        |            | [7] K. B. | Athreya | and P. E. | Ney, Branching | Processes. |     | New York: |
| -------- | --------------- | --- | ----- | --------- | ---- | ------ | ---------- | --------- | ------- | --------- | -------------- | ---------- | --- | --------- |
| than its | size (Corollary |     | 1), a | factor of | 2.69 | on the | calibrated |           |         |           |                |            |     |           |
Springer,1972.
foot-and-mouth model, and the certainty-equivalence law of [8] V.C.Tran,“Largepopulationlimitandtimebehaviourofastochas-
|         |          |     |             |      |          |              |     | tic particle | model | describing | an age-structured |     | population,” | ESAIM |
| ------- | -------- | --- | ----------- | ---- | -------- | ------------ | --- | ------------ | ----- | ---------- | ----------------- | --- | ------------ | ----- |
| Section | V places | the | equilibrium | with | an error | proportional |     |              |       |            |                   |     |              |       |
Probab.Stat.,vol.12,pp.345–386,2008.
| to that of | the          | particle | estimator. |              |        |     |         |           |             |                |          |        |          |              |
| ---------- | ------------ | -------- | ---------- | ------------ | ------ | --- | ------- | --------- | ----------- | -------------- | -------- | ------ | -------- | ------------ |
|            |              |          |            |              |        |     |         | [9] A. M. | Yaglom,     | “Certain limit | theorems | of the | theory   | of branching |
| Three      | restrictions |          | apply.     | (i) Actuator | class. | The | ceiling |           |             |                |          |        |          |              |
|            |              |          |            |              |        |     |         | random    | processes,” | Dokl. Akad.    | Nauk     | SSSR,  | vol. 56, | pp. 795–798, |
1947.
| is a limitation |             | of childless |              | actuation, | not          | of feedback | in   |                   |     |                     |                   |     |               |     |
| --------------- | ----------- | ------------ | ------------ | ---------- | ------------ | ----------- | ---- | ----------------- | --- | ------------------- | ----------------- | --- | ------------- | --- |
|                 |             |              |              |            |              |             |      | [10] S. Me´le´ard |     | and D. Villemonais, | “Quasi-stationary |     | distributions | and |
| general:        | an actuator |              | that reduces | onward     | transmission |             | acts |                   |     |                     |                   |     |               |     |
populationprocesses,”Probab.Surv.,vol.9,pp.340–410,2012.
on m, hence on Λ itself, and Theorem 2 does not apply to [11] N. Champagnat and D. Villemonais, “Convergence of the Fleming–
Viotprocesstowardtheminimalquasi-stationarydistribution,”ALEA
| it. (ii) Necessity |     | versus | sufficiency. | Theorem |     | 1is a | necessary |     |     |     |     |     |     |     |
| ------------------ | --- | ------ | ------------ | ------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
Lat.Am.J.Probab.Math.Stat.,vol.18,pp.1–15,2021.
| condition, | so U | is an | outer | bound on | U and | Theorem | 2 an |     |     |     |     |     |     |     |
| ---------- | ---- | ----- | ----- | -------- | ----- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
c [12] V. Bansaye, B. Cloez, and P. Gabriel, “Ergodic behavior of non-
upper bound on certifiable performance; a matching suffi- conservative semigroups via generalized Doeblin’s conditions,” Acta
ciency for a general u requires the age-dependent controlled Appl.Math.,vol.166,pp.29–72,2020.
|     |     |     |     |     |     |     |     | [13] V.Bansaye,B.Cloez,P.Gabriel,andA.Marguet,“Anon-conservative |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
reproductive value of (11), and the certified statements of Harris ergodic theorem,” J. Lond. Math. Soc., vol. 106, no. 3,
SectionIVareaccordinglylimitedtotheproportionalfamily. pp.2459–2510,2022.
(iii) Certificate versus equilibrium, as set out in Remark 2. [14] S.P.MeynandR.L.Tweedie,“StabilityofMarkovianprocessesIII:
Foster–Lyapunovcriteriaforcontinuous-timeprocesses,”Adv.inAppl.
The largest extension concerns the supercritical regime Probab.,vol.25,pp.518–548,1993.
m > 1, where (H2) fails, the population survives with [15] D. Villemonais, “General approximation method for the distribution
|          |              |     |     |        |       |              |     | of Markov | processes | conditioned | not | to be killed,” | ESAIM | Probab. |
| -------- | ------------ | --- | --- | ------ | ----- | ------------ | --- | --------- | --------- | ----------- | --- | -------------- | ----- | ------- |
| positive | probability, | and | the | Yaglom | limit | is no longer | the |           |           |             |     |                |       |         |
Stat.,vol.18,pp.441–467,2014.
relevantoperatingpoint.Therethecontrolproblembecomes
|     |     |     |     |     |     |     |     | [16] F. Ce´rou, | B.  | Delyon, A. Guyader, | and | M. Rousset, | “A  | central limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------------- | --- | ----------- | --- | ------------- |
theoremforFleming–Viotparticlesystems,”Ann.Inst.HenriPoincare´
| a different | one: | the plant | is  | unstable | and the | actuator | must |     |     |     |     |     |     |     |
| ----------- | ---- | --------- | --- | -------- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Probab.Stat.,vol.56,pp.637–666,2020.
| stabilise      | it rather | than           | place | an existing | attractor. |     | Propor-    |                                                                 |     |     |     |     |     |     |
| -------------- | --------- | -------------- | ----- | ----------- | ---------- | --- | ---------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                |           |                |       |             |            |     |            | [17] L.FarinaandS.Rinaldi,PositiveLinearSystems:TheoryandAppli- |     |     |     |     |     |     |
| tional removal |           | does stabilise |       | it, since   | by (17)    | the | controlled |                                                                 |     |     |     |     |     |     |
cations.NewYork:Wiley,2000.
offspringmeanism c =m/(1+c),sotheclosedloopissub- [18] D.AngeliandE.D.Sontag,“Monotonecontrolsystems,”IEEETrans.
Autom.Control,vol.48,no.10,pp.1684–1698,2003.
criticalassoonasc>m−1;combinedwiththecertifiability
|     |     |     |     |     |     |     |     | [19] A.Rantzer,“Scalablecontrolofpositivesystems,”EuropeanJ.Con- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
c < c
constraint max of Theorem 3, a certifiably stabilising trol,vol.24,pp.72–80,2015.
gain exists if and only if m−1 < c . When µ∗ = µ [20] V.M.Preciado,M.Zargham,C.Enyioha,A.Jadbabaie,andG.J.Pap-
|     |     |     |     |     | max |     | ∞   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
this reads m+2p < 2, which for Poisson offspring holds pas, “Optimal resource allocation for network protection against
0 spreadingprocesses,”IEEETrans.ControlNetw.Syst.,vol.1,no.1,
m⋆
up to ≃ 1.594; beyond that threshold childless removal pp.99–108,2014.
cannotcertifiablystabilisethepopulation,whateverthegain. [21] C.Nowzari,V.M.Preciado,andG.J.Pappas,“Analysisandcontrol
Turning this observation into a theorem requires replacing ofepidemics:asurveyofspreadingprocessesoncomplexnetworks,”
IEEEControlSyst.Mag.,vol.36,no.1,pp.26–46,2016.
the quasi-stationary framework by a full stability analysis [22] P. E. Pare´, C. L. Beck, and T. Bas¸ar, “Modeling, estimation, and
of the measure-valued flow, and the transient guarantees of analysisofepidemicsovernetworks:anoverview,”Annu.Rev.Control,
vol.50,pp.345–360,2020.
SectionVbyastabilisationcertificatevalidbeforetheclosed
|              |      |              |     |                 |     |           |     | [23] S.Ani¸ta,AnalysisandControlofAge-DependentPopulationDynam- |     |     |     |     |     |     |
| ------------ | ---- | ------------ | --- | --------------- | --- | --------- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| loop becomes |      | subcritical. |     |                 |     |           |     | ics.Dordrecht:Kluwer,2000.                                      |     |     |     |     |     |     |
|              |      |              |     |                 |     |           |     | [24] G.F.Webb,TheoryofNonlinearAge-DependentPopulationDynam-    |     |     |     |     |     |     |
| Further      | open | questions    | are | the sufficiency |     | direction | for | a                                                               |     |     |     |     |     |     |
ics.NewYork:Dekker,1985.
| general  | u; the | optimal-shape |     | problem,    | of which | Corollary |          | 1                                                              |     |     |     |     |     |     |
| -------- | ------ | ------------- | --- | ----------- | -------- | --------- | -------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |        |               |     |             |          |           |          | [25] S.LenhartandJ.T.Workman,OptimalControlAppliedtoBiological |     |     |     |     |     |     |
| compares | only   | two families  |     | and Theorem | 2        | solves    | only the |                                                                |     |     |     |     |     |     |
Models.BocaRaton,FL:Chapman&Hall/CRC,2007.
(cid:82) [26] Z.-P. Jiang, A. R. Teel, and L. Praly, “Small-gain theorem for ISS
| extreme | case, | when | u(s)ds | is bounded | instead | of  | u itself; |     |     |     |     |     |     |     |
| ------- | ----- | ---- | ------ | ---------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
systemsandapplications,”Math.ControlSignalsSyst.,vol.7,no.2,
| an explicit | bound | on  | γ(c), | for which | the | non-conservative |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ----- | --------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.95–120,1994.
Harris framework of [13] is the natural tool and which [27] P. Kokotovic´, H. K. Khalil, and J. O’Reilly, Singular Perturbation
would make Proposition 2 unconditional; and a central limit Methods in Control: Analysis and Design. Philadelphia, PA: SIAM,
1999.
| theorem | for the | estimator | [16] | in place | of  | the present | first- |     |     |     |     |     |     |     |
| ------- | ------- | --------- | ---- | -------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
moment rate.
---- END DOCUMENT ----
