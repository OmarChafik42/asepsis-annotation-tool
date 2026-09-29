Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
|     | LOCALLY |     | FINITE |          | FIXED | POINTS |     | OF BRANCHING |     |     |
| --- | ------- | --- | ------ | -------- | ----- | ------ | --- | ------------ | --- | --- |
|     |         |     |        | BROWNIAN |       | MOTION |     |              |     |     |
XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
Abstract.
WegiveafullcharacterizationofthefixedpointsofBranching
|     | Brownian |     | motion | with critical | and | supercritical | drifts | under | no additional |     |
| --- | -------- | --- | ------ | ------------- | --- | ------------- | ------ | ----- | ------------- | --- |
6202 guA 42  ]RP.htam[  1v20232.8062:viXra
|     | assumptionsbesidesitbeinglocallyfinitealmostsurely. |     |                                                          |     |                                    |     |     | Inparticular,wedo |          |     |
| --- | --------------------------------------------------- | --- | -------------------------------------------------------- | --- | ---------------------------------- | --- | --- | ----------------- | -------- | --- |
|     | notassumefiniteintensity(cf.                        |     |                                                          |     | [Kab12])orthefinitetopparticle(cf. |     |     |                   | [CGS23]) |     |
|     | conditions.                                         |     | Wealsogiveafullcharacterizationofthedomainofattractionof |     |                                    |     |     |                   |          |     |
thefixedpointsofBBM.
1. Introduction
1.1. The setup and the goal. A binary Branching Brownian motion (BBM) can
be described as follows: particles evolve independently of each other and according
to standard Brownian motion and split into two independent particles at rate 1.
If we start a BBM with a single particle at the origin, the locations of particles
at time t are denoted by {χ k (t)} 1≤k≤n(t) , where n(t) is the number of particles
alive at time t. A BBM with drift λ ≥ 0 is given by {χ (t)−λt} . The
|     |     |     |     |     |     |     |     | k   | 1≤k≤n(t) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
study of BBM seen as a Markov process and its invariant distributions was initiated
in [Kab12], [CGS23], [CGS24]. In this article we revisit the characterization of
invariant distributions of BBM, but under no additional assumptions besides the
| invariant |     | distribution | being | locally | finite | almost | surely. |     |     |     |
| --------- | --- | ------------ | ----- | ------- | ------ | ------ | ------- | --- | --- | --- |
Let N be the space of all locally finite point measures on R, see section 2.1. We
follow the standard terminology: a point process θ is a N-valued random variable,
| see | [Chapter | 2-[Bov17]]1. |     |     |     |     |     |     |     |     |
| --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
The BBM with drift λ≥0 started from a point process θ is informally defined as
follows. Given θ, for each atom x of θ, we run an independent BBM with drift λ
i
| starting | from | x . | The collection |     | of points | at  | time t is | given by |     |     |
| -------- | ---- | --- | -------------- | --- | --------- | --- | --------- | -------- | --- | --- |
i
ni(t)
|     |     |     |     |     | (cid:88) | (cid:88) |        |     |     |       |
| --- | --- | --- | --- | --- | -------- | -------- | ------ | --- | --- | ----- |
|     |     |     |     | θλ  | :=       | δ        |        | ,   |     | (1.1) |
|     |     |     |     | t   |          | xi+χi    | (t)−λt |     |     |       |
k
|     |     |     |     |     | i∈I | k=1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)
where θλ = θ = δ and {χi(t),1 ≤ k ≤ ni(t)} is a family of independent
|     | 0   |     | xi  |     | k   |     | i∈I |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i∈I
BBMs.
The Markov evolution θ (cid:55)→θλ is a priori interpreted only in an informal sense,
t
and it is not a well-defined Markov process on N. This is due to the fact which we
refer to as coming down from ∞: θλ may be locally infinite even if θ is locally finite.
t
e|x|3
For example, if θ has ≈ many particles in (x,x+1) as x → ±∞, since the
Browniantransitiondensityis≈e−x2/2t,
itcanbeeasilyshownusingBorel-Cantelli
arguments that θλ is locally infinite almost surely for all t>0. Since θλ may not
|     |     |     | t   |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1Althoughthisisastandardterminology,sincewewillalsoencounterrandompointmeasures
whicharepossiblylocallyinfinite,westressthatthetermpoint process willbeusedonlyfora
N-valuedrandomvariable. Wewilluse“randomcollectionofpoints"torefertorandompossibly
locallyinfinitepointmeasures.
1

| 2   | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- |
be a well-defined point process, the “law of θλ” is ill-defined. Hence, the question of
t
invariant distributions is not well-posed. A possible remedy to cure this issue is to
restrict the definition of this Markov process on a smaller state space than N. To
this end, we consider the subspace N ⊂N given by (2.2). It can be shown that
2
|     |     | θ ∈N | a.s. =⇒ θλ ∈N | a.s. | for all t>0, | (1.2) |
| --- | --- | ---- | ------------- | ---- | ------------ | ----- |
|     |     |      | 2 t           | 2    |              |       |
θλ θλ
see Lemma 2.1. In particular, for = θ ∈ N 2 almost surely, is almost surely
0 t
locally finite, and hence it is a well-defined point process. The Markov evolution
θ (cid:55)→θλ can be seen as a well-definedMarkov process on the state space N , andone
| t   |     |     |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- |
can henceforth study the invariant distributions of this Markov process. However,
in this approach, one only studies invariant distributions that are supported on
N 2 . It is possible to miss out on possibly exotic invariant distributions that are not
necessarily supported on N . Therefore, to be in a complete generality, we take
2
an alternative approach similar to that of Biskup and Louidor [BL16] which also
encounters an issue of coming down from ∞ in the context of extreme values of
Gaussianfreefield(GFF). However,itwillfollowfromtheresultsofthisarticlethat
the above mentioned approach based on the space N 2 and the following alternative
| approach | are consistent |     | with each other. |     |     |     |
| -------- | -------------- | --- | ---------------- | --- | --- | --- |
θλ
Let θ be a point process and be as given by (1.1) which is possibly locally
t
infinite. For f ∈C+(R) (the space of compactly supported non-negative continuous
c
| functions | on R),   | let      |             |                   |                 |       |
| --------- | -------- | -------- | ----------- | ----------------- | --------------- | ----- |
|           |          | (cid:90) |             | ni(t)             |                 |       |
|           |          |          | ∞           | (cid:88) (cid:88) |                 |       |
|           | ⟨f,θλ⟩:= |          | f(x)θλ(dx)= |                   | f(x +χi(t)−λt). | (1.3) |
|           |          | t        | t           |                   | i k             |       |
|           |          |          | −∞          | i∈I k=1           |                 |       |
Althoughitcanbepossiblyinfinite,⟨f,θλ⟩isawell-defined[0,∞]-valuedrandom
t
|     |     |     |     |     | λ⟩] λ⟩ |     |
| --- | --- | --- | --- | --- | ------ | --- |
variable. We can consider its Laplace transform E[e−⟨f,θ t where e−⟨f,θ t =0 on
| the event | {⟨f,θλ⟩=+∞}. |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- |
t
Definition 1.1. A point process Π is called a fixed point2 of BBM with drift λ if
∈C+(R)
| for all f |     | and for | all t≥0, |     |     |     |
| --------- | --- | ------- | -------- | --- | --- | --- |
c
|          |          |          | E[e−⟨f,θ λ⟩]=E[e−⟨f,θ |     | λ⟩], | (1.4) |
| -------- | -------- | -------- | --------------------- | --- | ---- | ----- |
|          |          |          | t                     |     | 0    |       |
| where θλ | is given | by (1.1) | with θλ =Π.           |     |      |       |
|          | t        |          | 0                     |     |      |       |
The benefit of the above definition is that it does not impose any additional
assumptions on the point process Π. Moreover, since Π is almost surely locally
finite, it can be easily seen that (1.4) implies that θλ, started from θλ = Π, is
|     |     |     |     |     | t 0 |     |
| --- | --- | --- | --- | --- | --- | --- |
locally finite almost surely (take f = αg, with α → 0+, g ∈ C+(R) and apply
c
θλ
Lévy continuity theorem for Laplace transforms). In particular, the law of
t
seen as a point process is well defined and (1.4) implies that these laws are in-
variant in t ≥ 0. As an intermediate step towards characterizing fixed points Π
we will in fact prove that fixed points Π ∈ N almost surely. Using (1.2), this
2
reconfirmsthatθλ startedfromΠisindeedlocallyfinitealmostsurely,anditalsore-
t
isanaturalstatespacefordefiningtheMarkovprocessθλ.
| assuresthatthespaceN |     |     | 2   |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- |
t
√
Itcanbeeasilyshownthatifλ∈[0, 2),thenontheeventθ ≠ 0,θλ([−K,K])→ d
t
+∞forallK >0(onewayofprovingthisisbyusing(2.8)andapplyingLemma2.7).
√
Thisimpliesthattherearenonon-trivialfixedpointsforBBMwithdriftλ∈[0, 2).
2Sincethisisanon-standarddefinition,wehereandhenceforthusethetermfixed points to
avoidanyconfusionwithinvariantdistributions.

|     | LOCALLY | FINITE | FIXED | POINTS | OF BRANCHING |     | BROWNIAN | MOTION | 3   |
| --- | ------- | ------ | ----- | ------ | ------------ | --- | -------- | ------ | --- |
√
The characterization of fixed points Π for the supercritical drift λ> 2 was given
in [Kab12] under an additional assumption that Π has locally finite intensity, i.e.
E[Π(K)] < ∞ for all compact sets K ⊂ R. It is proved √ in Section 6, Proposition
6.1 that if Π is a fixed point of BBM with drift λ> 2 with locally finite intensity,
then it also satisfies E[Π([0,∞))]<∞. In particular, Π([0,∞))<∞ almost surely,
which is equivalent to Π having a finite top particle almost surely. Hence, the
assumption of locally finite intensity is a stronger and more restrictive assumption
√
than the assumption of having a finite top particle. In the critical case λ= 2, the
assumption of locally finite intensity for fixed points Π is not appropriate since we a
posteriori know that fixed points in this case must have locally infinite intensity. In
√
[CGS23] a characterization of fixed points for λ= 2 was given under the weaker
and less restrictive assumption of finite top particle almost surely. In both critical
(resp. supercritical)cases,thefixedpointsaregivenbyrandomshiftsoftheso-called
critical (resp. supercritical) extremal point process of BBM; see section 2.5 for its
precise definition. In this article, we give a full characterization of fixed points Π
√
for both supercritical and critical cases λ≥ 2 without any additional assumption
on Π besides it being locally finite almost surely. The answer still turns out to be
random shifts of critical/ supercritical extremal point processes. Hence, there are
no exotic fixed points of BBM that violate the finite top particle condition.
|     |     |     |     | √   |     |     | √   | √   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.2. Main results. Let µ=λ+ λ2−2 for λ≥ 2. For λ> 2 it was proven
in [Kab12] that if θλ is PPP(√1 e−µxdx) (i.e. Poisson point process with intensity
0
2π
√1 e−µxdx ) then θλ given by (1.1) converges in distribution as point processes to
t
| 2π  |     |     |              |     | √   |     |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
|     |     |     | E(cid:101)λ. |     |     |     |     |     | θλ  |
a non-trivial point process For λ= 2, it was proven in [ABK13] that if is
|     | (cid:113) | √   | ∞   |     | √   |     |     |     | 0   |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 2(−x)e−   |     |     |     | 2   |     |     |     |     |
PPP( 2x1 dx), then θ converges in distribution as point processes
|     | π   |     | x<0 |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | √   |     | √   |     |     |
to another non-trivial point process E(cid:101) 2. The E(cid:101)λ (resp. E(cid:101) 2) are the supercritical
|     |     |     |     |     | ∞   | ∞   | ∞   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(resp. critical) extremal point processes of BBM, which are decorated Poisson point
processes; seesection2.5foramoredetaileddescription. Thecriticalextremalpoint
√
2
| process | E(cid:101) | will be simply | written |     | as E(cid:101)∞ . |     |     |     |     |
| ------- | ---------- | -------------- | ------- | --- | ---------------- | --- | --- | --- | --- |
∞
Our main result is as follows. For a point process θ = (cid:80) δ , we write θ(·−S)
i∈ I xi
(cid:80)
forthepointprocessobtainedbyshiftingatomsx byS,i.e. θ (·− S)= δ 3.
|     |     |     |     |     |     | i   |     | i∈I | xi+S |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
√
Theorem 1.2. Let λ ≥ 2 and Π be a point process. Then Π is a fixed point
of BBM with drift λ in the sense of Definition 1.1 if and only if there exists a
| [−∞,∞)-valued |     | random | variable | S   | independent | of  | E(cid:101)λ such | that |     |
| ------------- | --- | ------ | -------- | --- | ----------- | --- | ---------------- | ---- | --- |
∞
|     |     |     |     | Π=  | d E(cid:101) λ(·−S). |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
∞
Remark 1. It may seem awkward to see the random variable S to be [−∞,∞)
valued, i.e. it may take −∞ value with positive probability. On the event S =−∞,
thepointprocessE(cid:101)λ(·−S)isinterpretedasanemptypointprocesssinceE(cid:101)λ almost
|     |     | ∞   |     |     |     |     |     | ∞   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
surelyhasafinitetopparticleandallatomsofE(cid:101)λ
willbepushedto−∞bytheshift
∞
S =−∞. This is coherent with the fact that the fixed point Π can potentially be
an empty point process with positive probability: empty point process is obviously
fixedpoint. Also, notethatafixedpoint, conditionalonbeingnon-empty, remainsa
fixedpoint. One can hence, withoutlossofgenerality, assumethatthe fixedpointΠ
3IftheminussigninfrontofS onthelefthandsidecausesconfusiontoareader,notethatin
| thenotationθ(·),wetreatθ |     |     | asameasurewhichisevaluatedonBorelsubsetsofR. |     |     |     |     |     |     |
| ------------------------ | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |

| 4   |     | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |     |     |
| --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
is non-empty, i.e. Π(R)̸=0 almost surely. Under this condition, the corresponding
| random | variable | S   | will be | a proper | real-valued |     | random variable. |     |     |
| ------ | -------- | --- | ------- | -------- | ----------- | --- | ---------------- | --- | --- |
Theorem 1.2 will be derived as a consequence of addressing another related
problem of the domain of attraction of fixed points of BBM. For a point process Π,
| we  | define | its domain | of attraction |     | as follows: |     |     |     |     |
| --- | ------ | ---------- | ------------- | --- | ----------- | --- | --- | --- | --- |
Definition 1.3. For a point process Π, we say a point process θ is in the domain
of attraction of Π, written as θ ∈Dom (Π), if θλ given by (1.1) started from θλ =θ
|           |     |             |       |      | λ       |           | t   |     | 0   |
| --------- | --- | ----------- | ----- | ---- | ------- | --------- | --- | --- | --- |
| converges |     | to Π in the | sense | that | for all | f ∈C+(R), |     |     |     |
c
|     |     |     |     | E[e−⟨f,θ | λ⟩]−→E[e−⟨f,Π⟩] |     |     |     | (1.5) |
| --- | --- | --- | --- | -------- | --------------- | --- | --- | --- | ----- |
t
as t→∞.
Note that the above definition, similarly to Definition 1.1, bypasses the issue that
θλ can possibly be locally infinite. Nevertheless, as it turns out, if a point process
t
θλ
θ ∈Dom λ (Π) for a point process Π, then must be locally finite almost surely. It
t
is easy to heuristically support this claim: since the initial point process θ and the
limiting point process Π are locally finite, the intermediate collection of points θλ
t
must also be locally finite. We will, in fact, prove that for θ ∈Dom (Π), θ ∈N
λ 2
almost surely, which, using (1.2), implies that θλ is a well-defined point process.
t
Hence,Definition1.3impliesthatθλconvergesindistributiontoΠaspointprocesses.
t
It follows easily from the Markovian nature of the evolution θ (cid:55)→θλ that for a
t
point process Π, Dom (Π)̸=∅ if and only if Π is a fixed point of BBM with drift
λ
λ in the sense of Definition 1.1. Hence, without loss of generality, we assume in
Definition1.3thatΠisafixedpointofBBMwithdriftλ. TheproofofTheorem1.2
will run in parallel and will follow as a result of addressing the following problem of
characterizing Dom (Π) of fixed points Π. Let us first coin the following definition.
λ
| The | significance | of  | this definition |     | will be | addressed | in the next | section. |     |
| --- | ------------ | --- | --------------- | --- | ------- | --------- | ----------- | -------- | --- |
Definition 1.4. (1) A point process θ is called lacunary on (0,∞) if there
|     | exist | constants | c,d∈(0,∞), |     | c<d, | such | that |     |     |
| --- | ----- | --------- | ---------- | --- | ---- | ---- | ---- | --- | --- |
P
|     |     |     |     |     | θ([cx,dx])→0 |     |     |     | (1.6) |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ----- |
x→∞4.
as
(2) A point process θ is called exponentially-lacunary on (0,∞) if there exist
|     | constants | c,d∈(0,∞), |     |     | c<d, such | that |     |     |     |
| --- | --------- | ---------- | --- | --- | --------- | ---- | --- | --- | --- |
P
|     |     |      |     |     | θ([clogx,dx])→0 |     |     |     | (1.7) |
| --- | --- | ---- | --- | --- | --------------- | --- | --- | --- | ----- |
|     | as  | x→∞. |     |     |                 |     |     |     |       |
Letuslisttheconditionsappearinginthenextresult. Throughoutthispaper, we
willrefertoafamilyofrandomvariables{X } astight ifsup P(|X |≥K)→0
|     |     |     |     |     |     | t t>0 |     | t≥1 | t   |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
as K → +∞. In particular, √ we do not put any tightness assumption on X t for
| t∈(0,1). |     | For λ>      | 2, we | assume |       |           |     |     |     |
| -------- | --- | ----------- | ----- | ------ | ----- | --------- | --- | --- | --- |
| (H1):    | θ   | is lacunary | on    | (0,∞)  | and θ | ∈N 5 a.s. |     |     |     |
2
4The
|     | intuitive | meaning | of  | this | definition | is that atoms | of the point | process | θ in (0,∞) are |
| --- | --------- | ------- | --- | ---- | ---------- | ------------- | ------------ | ------- | -------------- |
extremelyspacedoutandhavelargegaps,hencethechoiceofthewordlacunary.
| 5Notethat,N2 |     | isdefinedin(2.2). |     |     |     |     |     |     |     |
| ------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |

|       | LOCALLY    |        | FINITE FIXED | POINTS OF BRANCHING | BROWNIAN |            | MOTION   | 5   |
| ----- | ---------- | ------ | ------------ | ------------------- | -------- | ---------- | -------- | --- |
| (H2): | For        | all K  | >0,          |                     |          |            |          |     |
|       | (cid:90) ∞ |        |              | (cid:90)            | 0 1      |            |          |     |
|       |            | P(|x+B | −λt|≤K)θ(dx) | and                 | √ e(1−λ  | 2 )teλxe−x | 2 tθ(dx) |     |
|       |            |        | t            |                     |          | 2          | 2        |     |
t
|       | −∞  |       |               |     | −∞  |     |     |     |
| ----- | --- | ----- | ------------- | --- | --- | --- | --- | --- |
|       | are | tight | in t≥1.       |     |     |     |     |     |
| (H3): | As  | t→∞   | and then L→∞, |     |     |     |     |     |
√
(cid:90)
|     |     |     | (λ−µ)t+L | t 1 2   | 2                |     |     |     |
| --- | --- | --- | -------- | ------- | ---------------- | --- | --- | --- |
|     |     | Z   | :=       | √ e(1−λ | )teλxe−x tθ(dx)→ | d   | Z,  |     |
|     |     | t,L |          | 2       | 2                |     |     |     |
√ t
|     |     |     | (λ−µ)t−L | t   |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- |
√
|     | where | µ=λ+ | λ2−2 | and Z is some | non-negative | random | variable. |     |
| --- | ----- | ---- | ---- | ------------- | ------------ | ------ | --------- | --- |
√
|       | For λ= | 2, we                  | assume |          |          |      |     |     |
| ----- | ------ | ---------------------- | ------ | -------- | -------- | ---- | --- | --- |
| (A1): | θ is   | exponentially-lacunary |        | on (0,∞) | and θ ∈N | a.s. |     |     |
2
| (A2):    | For    | all K | >0,           |                 |            |     |              |     |
| -------- | ------ | ----- | ------------- | --------------- | ---------- | --- | ------------ | --- |
| (cid:90) | ∞      |       | √             | (cid:90) 1 logt |            |     |              |     |
|          |        |       |               | 4               | 1          |     | √ 2          |     |
|          | P(|x+B |       | − 2t|≤K)θ(dx) | and             | (−x+logt)e |     | 2xe−x tθ(dx) |     |
|          |        | t     |               |                 |            |     | 2            |     |
t3 /2
|       | −∞  |       |            | −∞      |         |     |     |     |
| ----- | --- | ----- | ---------- | ------- | ------- | --- | --- | --- |
|       | are | tight | in t≥1.    |         |         |     |     |     |
| (A3): | As  | t→∞,  |            |         |         |     |     |     |
|       |     |       | (cid:90) 0 | √       |         |     |     |     |
|       |     |       | 1          | 2xe−x   | 2 d     |     |     |     |
|       |     |       |            | (−x)e 2 | tθ(dx)→ | Z,  |     |     |
t3/2
−∞
|     | where | Z is | some non-negative | random | variable. |     |     |     |
| --- | ----- | ---- | ----------------- | ------ | --------- | --- | --- | --- |
√
Theorem 1.5. Let Π be a fixed point of BBM with drift λ≥ 2 and θ be a point
process. Then,
√
(1) For λ> 2, θ ∈Dom (Π) if and only if θ satisfies (H1), (H2), (H3). In
λ
d
|     | that          | case, | Π= E(cid:101)λ(·−S) | with S =log(Z)/µ, | where | E(cid:101)λ | and Z are sampled |     |
| --- | ------------- | ----- | ------------------- | ----------------- | ----- | ----------- | ----------------- | --- |
|     |               |       | ∞                   |                   |       | ∞           |                   |     |
|     | independently |       | of each other       | 6.                |       |             |                   |     |
√
(2) For λ= 2, θ ∈Dom (Π) if and only if θ satisfies (A1), (A2), (A3). In
|     |     |     | λ   |     | √   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
d
|     | that          | case, | Π=E(cid:101)∞ (·−S) | with S =log(Z)/ | 2, where | E(cid:101)∞ | and Z are sampled |     |
| --- | ------------- | ----- | ------------------- | --------------- | -------- | ----------- | ----------------- | --- |
|     | independently |       | of each other7.     |                 |          |             |                   |     |
Remark 2. It can be easily seen that if (1.6) or (1.7) holds for some c,d∈(0,∞),
then it holds for all c,d ∈ (0,∞). Also, (1.6) is equivalent to θ([x,αx]) → P 0 as
x → ∞ for some α > 1 (and hence for all α > 1). As such, the condition (1.6) is
closely related to slowly varying functions, see [BGT87]. Indeed, if F(x)=eθ([0,x]),
P
| then | (1.6) | implies | F(αx)/F(x)→1 | as x→∞ | for some | α>1. |     |     |
| ---- | ----- | ------- | ------------ | ------ | -------- | ---- | --- | --- |
Remark 3. It is instructive to compare condition (1.6) with the finite top particle
condition θ([0,∞))<∞ almost surely. In combination with the fact that θ([0,x])
is integer valued, (1.6) is a rather stringent condition. In fact, if θ is a deterministic
locally finite integer-valued measure, (1.6) holds if and only if θ([cx,dx]) = 0 for
all x large enough. This holds if and only if θ([0,∞))<∞, i.e., θ has a finite top
6NotethattherandomvariableZ
|     |     |     |     | appearingherecanbe0withpositiveprobability. |     |     | Assuch, |     |
| --- | --- | --- | --- | ------------------------------------------- | --- | --- | ------- | --- |
comparingwithRemark1,S isa[−∞,∞)-valuedrandomvariableandΠ=E(cid:101)∞ λ(·−S)isanempty
pointprocessontheeventS=−∞.
√
7The critical case λ = 2 in this result was also addressed in [CGS24] although with an
additional assumption of θ having a finite top particle and with a slightly stronger notion of
convergenceascomparedtoDefinition1.3.

| 6   | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- |
particle. However, if we ignore the integer valued constraint on θ and view it as just
a positive measure, by utilizing the above mentioned connection to slowly varying
functions, one can easily come up with examples of positive measures satisfying
(1.6) and θ([0,∞))=∞, e.g. θ(dx)= 1 1 dx. Combining these observations,
xlogx x≥2
one can come up with examples of truly random point processes satisfying (1.6)
but not having a finite top particle, e.g. θ = PPP( 1 1 dx). Constructing
|     |     |     |     | xlogx | x≥2 |     |
| --- | --- | --- | --- | ----- | --- | --- |
an example of a point process satisfying (1.7) but not having a finite top particle
is only slightly more intricate. Let x be the sequence defined by x = e and
|     |     |     | n   |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- |
x = exn (it is the power tower sequence). Let G(x) = (cid:80)∞ 1 and m be
| n+1 |     |     |     |     | xn≤x |     |
| --- | --- | --- | --- | --- | ---- | --- |
n=1
the measure on (0,∞) defined by m(0,x]=logG(x). Note that (1.7) is equivalent
P
to θ([x,ex])→ 0 as x→∞. It can be easily checked that m is an infinite measure
satisfying m([x,ex])→0 as x→∞, which implies that θ =PPP(m(dx)) satisfies
| (1.7) and | θ([0,∞))=+∞ | almost | surely. |     |     |     |
| --------- | ----------- | ------ | ------- | --- | --- | --- |
Remark 4. AsitcanbeseenfromTheorem1.5,itisnotnecessarythatθ ∈Dom λ (Π)
has a finite top particle. However, if θ ∈Dom (Π) is deterministic, it then follows
λ
from Remark 3 that θ must have a top particle. Hence, for deterministic θ ∈
Dom (Π), conditions (A1),(A2) are redundant forpart-(2) of Theorem 1.5 and they
λ
can be replaced with the top particle assumption θ([0,∞))<∞. As such, it can be
| compared | to the results | of [CGS24]. |     |     |     |     |
| -------- | -------------- | ----------- | --- | --- | --- | --- |
1.3. Heuristic ideas and outline of the proof. Recall from Section 1.2 the
√
definition E(cid:101)λ as the limit of θλ starting from θ = PPP(√1 e−µxdx) for λ > 2
|              | ∞        | t         |     |         | 2π           |           |
| ------------ | -------- | --------- | --- | ------- | ------------ | --------- |
|              |          | (cid:113) | √   |         | √            |           |
|              |          | 2(−x)e−   | 2x1 |         |              |           |
| and starting | from θ = | PPP(      |     | dx) for | λ = 2. Since | we expect |
|              |          | π         |     | x<0     |              |           |
the fixed points Π to be random shifts of E(cid:101)λ, it is natural to expect that for
∞
θ ∈ Dom (Π), the number of particles of θ at a bounded distance from x should
λ
|     | √   |     | √   | √   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
be ≈e−µx for λ> 2 and ≈(−x)e− 2x for λ= 2 as x→−∞. The method to
make this guess mathematically √ precise was understood in [CGS23], [CGS24] √ for
the critical case λ= 2, and the similar arguments also apply to λ> 2. This is
reflected in the conditions (H3)/(A3) appearing in Theorem 1.5. However, for a
θ ∈Dom (Π), the structuralinformation aboutparticles ofθ ata boundeddistance
λ
fromxasx→+∞wasnotunderstoodin[CGS23],[CGS24]. Theresultsof[CGS23],
[CGS24] were hence proven under the additional assumption that θ has a finite top
particle almost surely. This assumption overlooked our above mentioned incomplete
understanding. The main new input in this article is to fill this gap since we do
not assume θ to have a finite top particle. This is given by the lacunary conditions
| appearing | in Theorem | 1.5 as per | Definition 1.4. |     |     |     |
| --------- | ---------- | ---------- | --------------- | --- | --- | --- |
WenowelaborateonthesignificanceoflacunaryconditionsappearinginTheorem
1.5. For a fixed point Π and θ ∈ Dom (Π), it is natural to look at the cloud of
λ
leading particles of θλ. More precisely, let M(θλ) be the thinned collection of points
|     | t   |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
given by
(cid:88)
|     |     | M(θλ):= | δ      | ,    |     | (1.8) |
| --- | --- | ------- | ------ | ---- | --- | ----- |
|     |     |         | t xi+M | i−λt |     |       |
t
xi∈θ
whereMi isthemaximumparticleofBBM{χi(t)} appearinginthedefinition
|     | t   |     |     | k k≤ni(t) |     |     |
| --- | --- | --- | --- | --------- | --- | --- |
(1.1) of θλ. While studying the large time behaviour of θλ, it is natural to first
|     | t   |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- |
study the large time behaviour of M(θλ). Note that M(θλ) is a (non-Markovian)
|     |     |     | t   |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- |
{Mi}
independent particle system since are i.i.d. over i ∈ I. For θ ∈ Dom λ (Π),
t
since θλ converges to the non-trivial limit Π, it is natural to anticipate that M(θλ)
| t   |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- |
converges to a non-trivial limit, and since it is an independent particle system, the
limit must be a Poisson point process. However, it is a priori not clear what would

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 7
be the intensity measure of this limiting Poisson point process.
Instead of picking the maximum particle Mi, it would also be beneficial to pick
t
a uniformly chosen particle from the collection {χi(t)} . One can choose
k k≤ni(t)
such a particle adaptively as follows. We attach a tag to the first particle of the
BBM {χi(t)} that starts from the origin. At each branching event, the tag is
k k≤ni(t)
transferred to one of the children uniformly at random. Let Bi denote the location
t
of the tagged particle at time t. Clearly, Bi is a standard Brownian motion. Instead
t
of choosing Mi, we can also choose Bi to obtain a thinned collection of points
t t
(cid:88)
U(θλ):= δ (1.9)
t xi+B
t
i−λt
xi∈θ
The advantage of picking a uniformly chosen particle is that the evolution
θ (cid:55)→ U(θλ) is Markovian. Such systems were introduced and studied by Liggett
t
[Lig78]. By the results of Liggett [Lig78], the limit of U(θλ) as t→∞ is a Poisson
t
point process, which is also an invariant distribution for the evolution θ (cid:55)→U(θλ).
t
Hence, the intensity measure of this limiting Poisson point process satisfies a
Choquet-Deny equation, see Section 1.5.1 of [CGS23] for details. Solving this
Choquet-Deny equation yields that the intensity measure has to be a linear com-
bination Z e−2λxdx+Y dx for some (possibly random) non-negative constants
∞ ∞
Z ,Y , see [CGS21] for an alternative direct approach. Note that on the event
∞ ∞
Y >0, the PPP(Z e−2λxdx+Y dx) does not have a finite top particle.
∞ ∞ ∞
For the thinning M(θλ), since it is non-Markovian, the limiting Poisson point
t
process obtained as the limit of M(θλ) as t → ∞ is not necessarily an invariant
t
distribution for the evolution θ (cid:55)→M(θλ). Hence, we do not have a Choquet-Deny
t
type equation at our disposal to determine the intensity measure of this limiting
PPP. However, resembling the case of U(θλ), we guess and conjecture that the
t
intensity measure in this case has to be of the form A e−µxdx+B dx, where
√ ∞ ∞
µ = λ+ λ2−2. We emphasize that B can be positive with positive prob-
∞
ability. For example, if θλ = θ = PPP(dx), then M(θλ) is also distributed as
0 t
PPP(dx) for all t > 0 (PPP(dx) is invariant for any independent particle sys-
tem, Markovian or non-Markovian). We again note that on the event B > 0,
∞
PPP(A e−µxdx+B dx) does not have a finite top particle.
∞ ∞
We infer from the discussion above that for a fixed point Π and θ ∈Dom (Π), it
λ
may be a priori possible that M(θλ) converges to a point process which does not
t
have a finite top particle. Nevertheless, we claim that the fixed point Π must have a
finite top particle almost surely. The heuristic but intuitive reason behind this is as
follows. To obtain back θλ from M(θλ), one has to recollect the cloud of particles
t t
within a bounded distance from Mi for each i ∈ I. Let us call these particles
t
decoration particles since, informally speaking, in the limit t→∞, conditional on
Mi being large, these particles form the decoration point process in the extremal
t
point process, see Section 2 for a more precise statement. The number of decoration
particles grows exponentially with time t>0. Hence, unless B appearing in the
∞
limit of M(θλ) is zero, the exponential contributions from these particles would
t
forcethelimitofθλ, whichisΠ, tobelocallyinfinite, whichisacontradiction. Also,
t
to counterbalance the exponential contribution from the decoration particles, the
atoms of the initial point process θλ = θ must be very sparse in (0,∞). This is
0
quantified using the lacunary point processes as in Definition 1.4.
The proof strategy is similar to the one used in [CGS23] along with some new
ideas. We make an educated guess and divide R into a certain number of pieces,

| 8   | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
see (4.1),(5.2), and track the contribution of atoms of θ in each piece to θλ for large
|     |     |     | √   |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
time t≫1. Forλ> 2, we showthatthe onlynon-trivialcontribution to θλ comes
|     |     |     | √   |     |     | √   |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
from atoms of θ in an O( t) neighbourhood of − λ2−2t. Furthermore, we show
that the contributions from the rest of the atoms of θ converge to zero in the limit
t→∞. For the contribution coming from the region {x>bt}, we use the Brownian
thinning U(θλ) given by (1.9) and prove a tightness estimate on θ, see Proposition
t
3.1. This is an essentialpiece ofnew argumentsince in the region {x>bt} we could
notrely on estimates forF-KPP solutions (note thatBramson’s ψ estimate given by
Proposition 2.8 does not hold in a neighbourhood of −∞). We get around this issue
byuseoftheBrownianthinningU(θλ).
Thecontributioncomingfromregion[at,bt]
t
for a,b > 0 is handled by proving the lacunary property of θ as explained in the
previous paragraph, see Proposition 3.2. The remaining contributions are handled
M(θλ).
by establishing tightness estimates on θ obtained via the thinning We can
t
here rely on the precise estimates on solutions to the F-KPP equation given by
Bramson’s ψ estimate; see section 2. The argument using these tightness estimates
to prove that the remaining contributions vanish in the limit t→∞ is similar to
that in [CGS23]: a non-zero contribution at time t would force an unusually large
contribution at a larger √ or smaller time u, which would contradict the tightness.
| The proof | for | λ=  | 2 follows using | similar | arguments. |     |     |     |
| --------- | --- | --- | --------------- | ------- | ---------- | --- | --- | --- |
1.4. Organization of the paper. The rest of the paper is organized as follows: In
Section 2, we recall some well-known results on BBM as well as some estimates used
in later sections. In Section 3, we list some properties of a point process when it
belongs to the domain of attraction of a fixed point. We prove Theorem 1.2 and 1.5
|     |     |     | √   |     | √   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
in Section 4 and 5 for λ> 2 and λ= 2 respectively. We include some relevant
discussions on supercritical fixed points and Tauberian conditions in Section 6. We
conclude this paper with Appendix 7, where we identify the explicit structure of
| supercritical |     | fixed points. |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
1.5. Notations. Wewritef ≲g,tomeanf ≤CgforafixedconstantC.Wealsouse
the usual Little-o and Big-O notation, that is, a(t)=o(b(t)) (Resp. a(t)=O(b(t)))
| implies | a(t) | →0 as t→∞ | (Resp. | |a(t)| | ≤C for | some | C >0). |     |
| ------- | ---- | --------- | ------ | ------ | ------ | ---- | ------ | --- |
|         | b(t) |           |        | |b(t)| |        |      |        |     |
1.6. Acknowledgments. S. Zhu would like to thank Professor Zenghu Li for a
helpful suggestion concerning the proof of Lemma 7.5 in Appendix 7. CA and SA
are supported through grant project no. RTI4014 of the Department of Atomic
| Energy, | Government |     | of India. |               |     |     |     |     |
| ------- | ---------- | --- | --------- | ------------- | --- | --- | --- | --- |
|         |            |     | 2.        | Preliminaries |     |     |     |     |
In this section, we introduce the state space of point processes that we work with
and review some classical results in probability theory. We then present some basic
facts on BBM and the associated F-KPP equation, and collect several estimates for
F-KPP solutions. Finally, we introduce the extremal point processes of BBM. The
results in this section are mainly extracted from [Bra78, Bra83, ABK13, ABBS13,
| Bov17, | CGS24] | and | will be used | in the | proof | of the main | theorems. |     |
| ------ | ------ | --- | ------------ | ------ | ----- | ----------- | --------- | --- |
2.1. State space and the Laplace functional. Let N be the space of all locally
| finite | point | measures | (i.e., they are | integer-valued) |     | on  | R,  |     |
| ------ | ----- | -------- | --------------- | --------------- | --- | --- | --- | --- |
(cid:88)
|     | N   | = (cid:8) η = | δ | η(K)<∞ |     | for | all compact | sets K | ⊂R (cid:9) . |
| --- | --- | ------------- | ---------- | --- | --- | ----------- | ------ | ------------ |
xi
i∈I
N isequippedwiththetopologyofvagueconvergence: forη ,η ∈N,wesayη →η v
|            |           |     |              |     |      |     | n   | n   |
| ---------- | --------- | --- | ------------ | --- | ---- | --- | --- | --- |
| if for all | f ∈C+(R), |     | ⟨f,η ⟩→⟨f,η⟩ | as  | n→∞. |     |     |     |
|            |           | c   | n            |     |      |     |     |     |

|     | LOCALLY | FINITE |     | FIXED | POINTS | OF BRANCHING |     | BROWNIAN | MOTION | 9   |
| --- | ------- | ------ | --- | ----- | ------ | ------------ | --- | -------- | ------ | --- |
A pointprocess θ is a N-valuedrandom variable. Itis wellknown thatthe lawof
d
θ is characterized by its Laplace functional, i.e., θ =θ 0 if and only if ψ θ (f)=ψ θ0 (f)
| for all | f ∈C+(R), |     | where | ψ (f) | is the             | Laplace | functional | of  | θ defined by |     |
| ------- | --------- | --- | ----- | ----- | ------------------ | ------- | ---------- | --- | ------------ | --- |
|         |           | c   |       | θ     |                    |         |            |     |              |     |
|         |           |     |       |       | ψ (f):=E[e−⟨f,θ⟩]. |         |            |     |              |     |
θ
In order to utilize the connection between the BBM and F-KPP equations, we
| will | often | be working | with | functions | of  | the following |     | form: |     |     |
| ---- | ----- | ---------- | ---- | --------- | --- | ------------- | --- | ----- | --- | --- |
n
(cid:88)
|     |     |     | f(x)= |     | a   | 1 ,a | >0,b | ∈R. |     | (2.1) |
| --- | --- | --- | ----- | --- | --- | ---- | ---- | --- | --- | ----- |
|     |     |     |       |     | k   | x≥bk | k k  |     |     |       |
k=1
We will use f of the form (2.1) instead of f ∈C+(R) as it is sufficient to consider
c
this class of test functions for weak convergence of point processes; see the remark
| on page  | 129 | in [Bov17].  |     |      |         |     |     |     |     |     |
| -------- | --- | ------------ | --- | ---- | ------- | --- | --- | --- | --- | --- |
| Consider |     | the subspace |     | N ⊂N | defined | by  |     |     |     |     |
2
|     |     |      | (cid:26) | (cid:12) | (cid:90) ∞ |         |     |         | (cid:27) |       |
| --- | --- | ---- | -------- | -------- | ---------- | ------- | --- | ------- | -------- | ----- |
|     |     |      |          | (cid:12) | e−αx2      |         |     |         |          |       |
|     |     | N := | η ∈N     | (cid:12) |            | η(dx)<∞ |     | for all | α>0 .    | (2.2) |
|     |     | 2    |          | (cid:12) |            |         |     |         |          |       |
−∞
| The | space | N 2 is | invariant | under | the | BBM: |     |     |     |     |
| --- | ----- | ------ | --------- | ----- | --- | ---- | --- | --- | --- | --- |
Lemma 2.1 (Easy adaptation of Lemma 3.7-[CGS24]). If θλ = θ ∈ N a.s.,
|     |     |     |     |     |     |     |     |     | 0   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | θλ  |     |     |     |     | θλ  | θλ  |     |
then for all t>0, ∈N a.s. In particular, for such =θ, is a well-defined
|     |     |     | t   | 2   |     |     |     | 0   | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
point process. Furthermore, if θ ∈N and θ([0,∞))<∞ a.s., then θλ([0,∞))<∞
|     |     |     |     |     | 2   |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a.s. for t>0.
2.2. Some classical results in probability theory. The following lemma is
classical, see [Theorem 2-Chapter13-[Fel71]]. However, notice the nuance that X t is
| allowed | to  | take +∞ | value. |     |     |     |     |     |     |     |
| ------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Lemma 2.2. Let X ,X be a family of [0,∞]-valued random variables such that
t
| P(X | <∞)=1. | Assume |                   | that for | all ρ>0, |     |         |     |     |       |
| --- | ------ | ------ | ----------------- | -------- | -------- | --- | ------- | --- | --- | ----- |
|     |        |        | E[e−ρXt]−→E[e−ρX] |          |          |     | as t→∞. |     |     | (2.3) |
Then,
|     |     |     |     | P(X t | =+∞)→0 |     | as t→∞, |     |     | (2.4) |
| --- | --- | --- | --- | ----- | ------ | --- | ------- | --- | --- | ----- |
andconditionedontheevent{X <∞},X convergesweaklytoX. Inparticular,for
|     |     |     |     |     | t   | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
all x∈[0,∞) which is a point of continuity for P(X ≤x), P(X ≤x)→P(X ≤x)
t
as t→∞.
Lemma 2.3 (Lemma 3.2 of [CGS23]). Let I be a countable set and {X } be
i i∈I
(cid:80)
independent Bernoulli random variables such that E[X i ]=p i . Let X I = X i .
i∈I
(cid:80)
| (a) | If  | E[X ]= |     | p is finite, | then | for | any ϵ∈(0,1), |     |     |     |
| --- | --- | ------ | --- | ------------ | ---- | --- | ------------ | --- | --- | --- |
|     |     | I      | i∈I | i            |      |     |              |     |     |     |
1
|     |     |     | P(|X | I −E[X | I ]|≥ϵE[X |     | I ])≤ | .   |     |     |
| --- | --- | --- | ---- | ------ | --------- | --- | ----- | --- | --- | --- |
ϵ2E[X ]
I
|     | (b) If | I is infinite | and | E[X | ]= (cid:80) | p =∞, | then | X =∞ | almost surely. |     |
| --- | ------ | ------------- | --- | --- | ----------- | ----- | ---- | ---- | -------------- | --- |
|     |        |               |     |     | I           | i∈I i |      | I    |                |     |
2.3. BBM and F-KPP equation. For the binary BBM, recall that the positions
of the particles alive at time t are denoted by {χ k (t),1≤k ≤n(t)}, where n(t) is
thenumberofparticlesaliveattimet. Thefollowinglemmacapturestheconnection
between the BBM and the F-KPP equation. This lemma is due to [McK75] but
| also | appeared | in [Sko64, |     | INW68a, | INW68b, | INW69]. |     |     |     |     |
| ---- | -------- | ---------- | --- | ------- | ------- | ------- | --- | --- | --- | --- |

| 10  | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma 2.4 (Lemma 5.5 of [Bov17]). For a measurable function ϕ:R→[0,1],
let
n(t)
(cid:89)
|     |     |     | u (t,x)=1−E[ |     |     | {1−ϕ(x−χ | (t))}]. |     | (2.5) |
| --- | --- | --- | ------------ | --- | --- | -------- | ------- | --- | ----- |
|     |     |     | ϕ            |     |     |          | k       |     |       |
k=1
| Then u=u | solves | the | following | F-KPP |     | equation |     |     |     |
| -------- | ------ | --- | --------- | ----- | --- | -------- | --- | --- | --- |
ϕ
1
|     |     |     |     | ∂ u= | ∂2u+u−u2 |     |     |     | (2.6) |
| --- | --- | --- | --- | ---- | -------- | --- | --- | --- | ----- |
|     |     |     |     | t    | x        |     |     |     |       |
2
| with the | initial | condition | u(0,x)=ϕ(x). |     |     |     |     |     |     |
| -------- | ------- | --------- | ------------ | --- | --- | --- | --- | --- | --- |
Ifϕ(x)=1 (x), we write the corresponding solution u as u . The relation
|     | (−∞,0] |     |     |     |     |     | ϕ   | M   |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
(2.5) gives, in particular, the distribution of the maximum particle M of BBM:
t
|      |            |     |                        | u M (t,x)=P(M |            | t ≥x).              |            |      | (2.7) |
| ---- | ---------- | --- | ---------------------- | ------------- | ---------- | ------------------- | ---------- | ---- | ----- |
| More | generally, | for | f :R→[0,∞),            |               | it follows | easily              | from (2.5) | that |       |
|      |            |     | (t,λt−x)=E[e−(cid:80)n |               |            | (t )f(x+χk(t)−λt)], |            |      |       |
|      |            | 1−u | ϕ                      |               |            | k= 1                |            |      | (2.8) |
1−e−f(−x).
where ϕ and f are related by ϕ(x) = This observation leads to the
following expression of the Laplace functional of BBM, and as the proof is quite
| straightforward, |     | it is | omitted. |     |     |     |     |     |     |
| ---------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
Lemma 2.5. Let θ be a point process and θλ as in (1.1). Then, for all f ∈C+(R)
|     |     |     |     |     |     | t   |     |     | c   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ϕ(x):=1−e−f(−x),
and
|     |          |     | (cid:20) | (cid:26)(cid:90) | ∞       |     |                | (cid:27)(cid:21) |       |
| --- | -------- | --- | -------- | ---------------- | ------- | --- | -------------- | ---------------- | ----- |
|     | E[e−⟨f,θ |     | λ⟩]=E    | exp              | log(1−u |     | (t,λt−x))θ(dx) | .                | (2.9) |
|     |          |     | t        |                  |         | ϕ   |                |                  |       |
−∞
Besides the connection of BBM to F-KPP, we will also use the following many-
| to-one | lemma, | see [HR17] | for | details. |     |     |     |     |     |
| ------ | ------ | ---------- | --- | -------- | --- | --- | --- | --- | --- |
Lemma 2.6 (The many-to-one lemma). LetF :R→R be a boundedmeasurable
| function. | Then, |     |     |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|     |     |     | E[  | F(χ | (t))]=etE[F(B |     | )], |     | (2.10) |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ------ |
|     |     |     |     |     | k             |     | t   |     |        |
k≤n(t)
| where B | is a standard |     | one dimensional |     | Brownian |     | motion. |     |     |
| ------- | ------------- | --- | --------------- | --- | -------- | --- | ------- | --- | --- |
2.4. Some estimates on solution to F-KPP equation. The following result is
| taken from | [Bra83]. |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma 2.7 (Proposition 3.4 of [Bra83]). 8 Let ϕ:R→[0,1] be a measurable
function such that ϕ(x) ≥ η for all x ∈ (a,b) with some a,b ∈ R and η > 0. Let
u (t,x) be the solution to F-KPP equation with initial condition ϕ. Then, for any
ϕ
| δ >0, as  | t→∞, |           |      |     |         |          |     |     |        |
| --------- | ---- | --------- | ---- | --- | ------- | -------- | --- | --- | ------ |
|           |      |           |      | u   | (t,x)→1 |          |     |     | (2.11) |
|           |      |           |      | √   | ϕ       |          |     |     |        |
|           |      |           |      |     | (cid:0) | (cid:1)  |     |     |        |
| uniformly | in x | such that | |x|≤ | 2t− | √3      | +δ logt. |     |     |        |
2 2
The above lemma gives the region of x where u converges to 1. On the other
ϕ
hand, it is well known (see e.g. Lemma 2.14) that for f either compactly supported
√
or of the type (2.1), u (t, 2t+x) → 0 uniformly over x ≥ −clog(t) as t → ∞,
ϕ
| 8ThisclaimcanalsobeverifiedinthemodernlanguageofextremalpointprocessesE(cid:101)∞ |     |     |     |     |     |     |     |     | λ.  |
| --------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Notably,
theunderlyingreasonfor(2.11)toholdisthatthenumber ofparticlesofE(cid:101)∞ λ atabounded distance
|     |     |     |     |     |     | √   | √   |     | √   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fromxblowsupasx→−∞: itgrowslikee−µx forλ> 2and≈(−x)e− 2x forλ= 2.

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 11
wherecisasmallenoughconstant. ThefollowingBramson’sψfunctionisapowerful
toolthatallowsustoobtainsharpestimatesonthesolutionsoftheF-KPPequation
in the region where u converges to zero.
ϕ
Proposition 2.8 (Proposition 8.3 of [Bra83], Proposition 4.3 of [ABK13]).
For a function f of type (2.1) and ϕ(x)=1−e−f(−x), let u be the solution to the
ϕ
F-KPP equation with initial condition ϕ. Define for z ∈R and t>r >0,
√
ψ(r,t,z+ √ 2t):= (cid:112) e− 2z (cid:90) ∞ u ϕ (r,y+ √ 2r)e √ 2ye−( 2 y ( − t− z r )2 ){1−e−2y z+ 2 t √3 − 2 r logt }dy.
2π(t−r)
0
(2.12)
Then, for all r large enough (depending only on the initial condition ϕ), t≥8r and
z ≥8r− √3 logt,
2 2
√ √ √
γ−1ψ(r,t,z+ 2t)≤u (t,z+ 2t)≤γ ψ(r,t,z+ 2t), (2.13)
r ϕ r
where γ ↓1 as r →∞.
r
The above proposition has several important consequences:
Lemma 2.9 (Proposition 3.1 of [BH14], Lemma 9.8 of [Bov17]). Let f,ϕ,u
ϕ
be as in Proposition 2.8. Then, for α>0 and z =αt+o(t),
C(f,α):= lim e √ 2zez 2 2 tt1 2u ϕ (t,z+ √ 2t) (2.14)
t→∞
exists, and is a strictly positive constant. The convergence in the right-hand side
above is uniform for α in compact subsets of (0,∞).
Lemma 2.10 (Lemma 9.10 of[Bov17]). Withf,ϕ,u ,C(f,α)givenasinLemma
ϕ
2.9, it holds that, as t→∞9,
1 (cid:90) ∞ √ √
√ u (t, 2t+z)e( 2+α)z−α2t/2dz →C(f,α). (2.15)
ϕ
2π
−∞
√ √ √
In particular, for λ > 2, µ = λ+ λ2−2, and α(λ) := µ− 2, by substituting
√
z =(λ− 2)t−x,
1 (cid:90) ∞
√ u (t,λt−x)e−µxdx→C(f,α(λ)). (2.16)
ϕ
2π
−∞
Also, for any fixed x∈R (see equation (9.50) of [Bov17]),
C(f(x+·),α(λ))=eµxC(f,α(λ)). (2.17)
Iff issuchthatϕ(x)=1−e−f(−x) =1 (x), motivatedbytherelation(2.7),
(−∞,0]
we write
C(f,α(λ))=C (α(λ)). (2.18)
M
The following quantitative upper and lower bounds hold as well.
Lemma 2.11. (a) Let f,ϕ,u be as in Proposition 2.8 and 0 < α < β < ∞.
ϕ
Then, there exist t ≥1,C ,C >0 such that for all t≥t and z ∈[αt,βt],
0 1 2 0
√ √
e− 2z √ e− 2z
C √ e−z2/2t ≤u (t,z+ 2t)≤C √ e−z2/2t. (2.19)
1 ϕ 2
t t
9Therangeofintegrationfor(2.15)in[Lemma9.10-[Bov17]]isgiventobe(0,∞). However,
√
sinceu (t, 2t+x)→0ast→∞pointwiseinx(seeLemma2.14),onecaneasilychangethe
ϕ
rangeofintegrationto(−∞,∞)byinvokingthedominatedconvergencetheorem.

12 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
The upper bound in the above holds for ϕ with f ∈C+(R) as well.
c
(b) Let 0 < α < β < ∞. Then, there exists t ≥ 1, K > 0 large enough and
0
constants C ,C >0 such that for all t≥t and z ∈[αt,βt],
1 2 0
√ √
e− 2z √ √ e− 2z
C √ e−z2/2t ≤u (t, 2t+z−K)−u (t, 2t+z+K)≤C √ e−z2/2t.
1 M M 2
t t
(2.20)
Proof. The proof of part-(a) follows easily by the same arguments as the proof
of [Proposition 3.1-[BH14]], which again is a direct consequence of Bramson’s ψ
estimate (2.8). We leave the details to the reader. The upper bound for ϕ with
f ∈C
c
+(R) follows easily by writing f(x)≤C1
[b,∞)
(x)=:f(cid:101)(x) for some b∈R and
applying comparison principle u
ϕ
≤u
ϕ(cid:101)
with ϕ(cid:101)(x)=1−e−f(cid:101)(−x).
For part-(b), the upper bound is immediate from (2.19). For the lower bound, we
claim that for K >0 and t>0 large enough,
√
u (t, 2t+z−K)
M √ ≥2 (2.21)
u (t, 2t+z+K)
M
for all z ∈[αt,βt]. Using (2.19), this implies that
√ √ √
u (t, 2t+z−K)−u (t, 2t+z+K)≥u (t, 2t+z+K)
M M M
√
e− 2z
≳ √ e−z2/2t.
t
It remains to verify (2.21). To this end, using (2.19) again, we obtain that
u M (t, √ √ 2t+z−K) ≳ e− √ 2(z−K)e−(z− 2 K t )2
u M (t, 2t+z+K) e− √ 2(z+K)e−(z+ 2 K t )2
√
≳e2 2K+2z
t
K
√
≳e2 2K.
Hence, (2.21) follows by choosing K large enough. □
√
Similarly as (2.16) which holds for λ > 2, we have the following lemma for
√
λ= 2:
Lemma 2.12 (Proposition 7.9 and Lemma 7.5 of [Bov17]). For f of the form
(2.1),
(cid:114) 2 (cid:90) ∞ √ √
u (t,x+ 2t)xe 2xdx→C(f) (2.22)
π ϕ
0
as t→∞, where C(f) is a positive constant. Furthermore, for any fixed x∈R,
√
C(f(x+·))=e 2xC(f). (2.23)
Iff issuchthatϕ(x)=1−e−f(−x) =1 (x), motivatedbytherelation(2.7),
(−∞,0]
we write
C(f)=C . (2.24)
M
Lemma 2.13 (Lemma 4.7 of [ABK13]). There exists a constant C > 0 such
1
that for all t large enough and z ≥−1logt,
2
u M (t,z+ √ 2t)≤C 1 t−3 2(z+logt)e− √ 2ze−z 2 2 t. (2.25)

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 13
The following lemma also allows us to estimate u from u using (2.25).
ϕ M
Lemma 2.14. Let f :R→[0,∞) be a non-negative measurable function supported
in [−K,∞) and ϕ(x)=1−e−f(−x). Then,
u (t,λt−x)≤etE[f(x+B −λt)], (2.26)
ϕ t
and
u (t,λt−x)≤u (t,λt−x−K). (2.27)
ϕ M
In particular, for f either compactly supported or of the type (2.1),
√
u (t, 2t−x)→0 (2.28)
ϕ
uniformly over x≤clogt as t→∞ for some small enough constant c>0.
Proof. Using (2.8), the many-to-one Lemma 2.6, and the fact that 1−e−y ≤y∧1
for y ≥0,
u ϕ
(t,λt−x)=E[1−e−(cid:80)n
k=
(t
1
)f(x+χk(t)−λt)]
=E[(1−e−(cid:80)n
k=
(t
1
)f(x+χk(t)−λt))1
x+Mt−λt≥−K ]
n(t)
(cid:8) (cid:88) (cid:9)
≤E[min 1, f(x+χ (t)−λt) 1 ]
k x+Mt−λt≥−K
k=1
≤min (cid:8) etE[f(x+B −λt)],P(x+M −λt≥−K) (cid:9) .
t t
The claim (2.28) follows easily using (2.27) and (2.25).
□
Lemma 2.15 (Lemma 2.8 of [CGS24]10). There exist constants r,C >0 such
2
that for all t large enough and z ≥−1logt,
2
u M (t,z+ √ 2t)≥C 2 t− 2 3(z+logt)e− √ 2ze− 2(t z − 2 r). (2.29)
As a consequence of the above bounds, the following variant of (2.20) holds as
well.
Lemma 2.16. Given b > 0, there exists K,C ,C > 011 such that for all t large
1 2
enough and z ∈[−1logt,bt],
4
C 1 t− 2 3(z+logt)e− √ 2ze−z 2 2 t ≤u M (t, √ 2t+z−K)−u M (t, √ 2t+z+K) (2.30)
≤C 2 t−3 2(z+logt)e− √ 2ze−z 2 2 t.
Proof. Theupperboundisimmediatefrom(2.25)bynotingthatforz ∈[−1logt,bt],
4
e−(z−K)2/2t =O(e−z2/2t).
10TheLemma2.8in[CGS24]isstatedsomewhatdifferentlyascomparedto(2.29)here. However,
theproofofLemma2.8in[CGS24]infactgivestheestimate(2.29). Weleavethedetailstothe
reader.
11Westressthatwearehereandin(2.20)writing“thereexistsaK>0"ratherthanwriting
“forallK>0". Weexpect(2.20),(2.30)toholdforallK>0ratherthanonlyforK largeenough.
Wewereabletoverify(2.20),(2.30)onlyforlargeenoughK>0,whichwillbesufficientforour
purposes.

| 14  |     | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |     |     |
| --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
For the lower bound, proceeding similarly to Lemma 2.11, using (2.25) and (2.29),
√
|     |     |       |         |     |                   |     | √ 2(z−K)e−( | z − K ) 2  |     |
| --- | --- | ----- | ------- | --- | ----------------- | --- | ----------- | ---------- | --- |
|     |     | u (t, | 2t+z−K) |     | t−3 2(z−K+logt)e− |     |             | 2 ( t− r ) |     |
|     |     | M √   |         |     | ≳                 |     |             |            |     |
√
|     |     | u (t, | 2t+z+K) |     | t−3 2(z+K+logt)e− |              | 2(z+K)e−(z+ | K )2 |     |
| --- | --- | ----- | ------- | --- | ----------------- | ------------ | ----------- | ---- | --- |
|     |     | M     |         |     |                   |              |             | 2 t  |     |
|     |     |       |         |     | √                 | )2           | 2           |      |     |
|     |     |       |         |     | ≳e2 2Ke           | (z+ K −( z − | K )         |      |     |
|     |     |       |         |     |                   | 2 t 2 (      | t− r )      |      |     |
√
|     |     |     |     |     | ≳e2 2K, |             |           |     |     |
| --- | --- | --- | --- | --- | ------- | ----------- | --------- | --- | --- |
|     |     |     |     |     |         | (z+ K )2 −( | z − K ) 2 |     |     |
where in the last line we have used that e 2 t 2 ( t− r ) ≳ 1 which holds clearly
| since | z ∈[−1logt,bt]. |     | Hence, | by  | choosing | K large | enough, | we obtain |     |
| ----- | --------------- | --- | ------ | --- | -------- | ------- | ------- | --------- | --- |
4
√
|     |     |     |     | u   | (t, 2t+z−K) |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
|     |     |     |     | M   | √           | ≥2, |     |     |     |
|     |     |     |     | u   | (t, 2t+z+K) |     |     |     |     |
M
| which | in turn | implies       |     |     |     |           |     |          |     |
| ----- | ------- | ------------- | --- | --- | --- | --------- | --- | -------- | --- |
|       |         | √             |     |     | √   |           |     | √        |     |
|       | u       | (t, 2t+z−K)−u |     |     | (t, | 2t+z+K)≥u | (t, | 2t+z+K). |     |
|       | M       |               |     |     | M   |           | M   |          |     |
□
Then,using(2.29)onceagaincompletestheproofofthelowerboundin(2.30).
Remark 5. The lower bounds in estimates (2.20) and (2.30) required a careful
verification, as presented above since Bramson’s ψ estimate (Proposition 2.8) is not
applicable forcompactlysupportedinitialconditions ϕ. Proposition 2.8 is validonly
for initial conditions ϕ satisfying certain conditions which are in particular satisfied
by ϕ(x)=1−e−f(−x) with f of the form (2.1), see [Chapter 6-[Bov17]] for details.
2.5. Extremal point processes of BBM. For a binary BBM ({χ (t);1≤k ≤
k
n(t)},t≥0) on the real line, recall that we denote the maximal position at time t
by
|     |     |     |     |     | M t := | max χ k (t). |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------------ | --- | --- | --- |
1≤k≤n(t)
Bramson [Bra78], [Bra83] proved that M −m(t) converges in law to some non-
t
| degenerate |     | random | variable | M   | , where |     |     |     |     |
| ---------- | --- | ------ | -------- | --- | ------- | --- | --- | --- | --- |
∞
|     |     |     |     |        | √   | 3     |      |     |        |
| --- | --- | --- | --- | ------ | --- | ----- | ---- | --- | ------ |
|     |     |     |     | m(t):= | 2t− | √ log | (t). |     | (2.31) |
+
|     |     |     |     |     |     | 2 2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Then, Lalley and Sellke showed in [LS87] that the limiting distribution function is a
| randomly |     | shifted Gumbel |     | distribution |     | given by |     |     |     |
| -------- | --- | -------------- | --- | ------------ | --- | -------- | --- | --- | --- |
√
|     |     |     |     |     | ≤x)=E[e−CMZ∞e− |     | 2x  |     |        |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | ------ |
|     |     |     |     | P(M |                |     | ]   |     | (2.32) |
∞
where C is as defined by (2.24) and Z is the positive random variable which is
|     | M          |        |           |            |         | ∞          |      |         |     |
| --- | ---------- | ------ | --------- | ---------- | ------- | ---------- | ---- | ------- | --- |
| the | a.s. limit | of the | so-called | derivative |         | martingale |      |         |     |
|     |            |        | n(t)      | √          |         | √          | √    |         |     |
|     |            |        | (cid:88)  |            |         | (cid:8)    |      | (cid:9) |     |
|     |            | Z      | :=        | ( 2t−χ     | (t))exp | − 2(       | 2t−χ | (t)) .  |     |
|     |            |        | t         |            | k       |            | k    |         |     |
k=1
Later, it was proven in [ABK13] and [ABBS13] that the point process defined by
n(t)
(cid:88)
|     |     |     |     |     | E := | δ          |     |     | (2.33) |
| --- | --- | --- | --- | --- | ---- | ---------- | --- | --- | ------ |
|     |     |     |     |     | t    | χk(t)−m(t) |     |     |        |
k=1
converges in law to a non-trivial point process E as t → ∞. The point process
∞
E is called the (limiting) extremal point process of BBM. The law of E can be
| ∞         |     |             |     |     |     |     |     |     | ∞   |
| --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| described |     | as follows. |     |     |     |     |     |     |     |
(cid:80)
Let P = δ be a Poisson point process independent of Z and with
|     | √   | i≥1√ | pi  |     |     |     |     | ∞   |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
intensity 2C e− 2xdx, where C is the same constant appearing in (2.32). For
|     |     | M   |     |     | M   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
each atom p of P, we attach a point process Di = (cid:80) δ where Di, i≥1 are
|     |     | i   |     |     |     |     |     | Di  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j≥1 j

|     | LOCALLY | FINITE | FIXED | POINTS | OF BRANCHING |     | BROWNIAN MOTION | 15  |
| --- | ------- | ------ | ----- | ------ | ------------ | --- | --------------- | --- |
i.i.d. copies of a certain point process D and independent of (P,Z ). In this way,
∞
we get
(cid:88)
|     |     |     | E   | =   | δ         |         | .   | (2.34) |
| --- | --- | --- | --- | --- | --------- | ------- | --- | ------ |
|     |     |     |     | ∞   | pi+D i+√1 | log(Z∞) |     |        |
j 2
i,j
ThepointprocessE isthuscalledadecoratedPoissonpointprocesswithdecoration
∞
process D. Moreover, the decoration process D is a point process supported on
(−∞,0]withanatomat0. Thepapers[ABK13],[ABBS13]alsodescribeditsprecise
law as
n(t)
|     |     |     |      |        | (cid:88)   |      | √        |        |
| --- | --- | --- | ---- | ------ | ---------- | ---- | -------- | ------ |
|     |     | P(D | ∈·)= | lim P( | δ χk(t)−Mt | ∈·|M | t ≥ 2t). | (2.35) |
t→∞
k=1
It is convenient to remove the randomness coming from the derivative martingale
| limit | Z . Define |     |     |     |     |     |     |     |
| ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
∞
|     |     |     |                 |     | 1       |     | (cid:88) |        |
| --- | --- | --- | --------------- | --- | ------- | --- | -------- | ------ |
|     |     |     | E(cid:101)∞ :=E | (·+ | √ log(Z | ))= | δ .      | (2.36) |
|     |     |     |                 | ∞   | ∞       |     | pi+D i   |        |
|     |     |     |                 |     | 2       |     | j        |        |
i,j
This process was proved in [ABBS13] (also in [ABK13], but it is not explicitly
| stated | there) | to be the | limit | in law | of  |     |     |     |
| ------ | ------ | --------- | ----- | ------ | --- | --- | --- | --- |
n(t)
(cid:88)
|     |     |     | E(cid:101)t | :=  | δ             |         | .   |     |
| --- | --- | --- | ----------- | --- | ------------- | ------- | --- | --- |
|     |     |     |             |     | χk(t)−m(t)−√1 | log(Zt) |     |     |
2
k=1
|     |     |     |     |     |     | √   | √   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Furthermore,itwasprovenin[ABK13]thatθ 2 givenby(1.1)forλ= 2started
t
|     |     | (cid:113) | √   |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- |
|     |     | 2(−x)e−   |     | 2x1 |     |     |     |     |
fromθ =PPP( x<0 dx)convergesindistributiontoE(cid:101)∞ . Then,using
π
the Laplace transform formula for PPP (see Proposition 2.12 of [Bov17]), formula
| (2.9), | and (2.22), | it follows | that | for                          | all f of type | (2.1), |     |        |
| ------ | ----------- | ---------- | ---- | ---------------------------- | ------------- | ------ | --- | ------ |
|        |             |            |      | E[e−⟨f,E(cid:101)∞⟩]=e−C(f). |               |        |     | (2.37) |
Also, if S is [−∞,∞)-valued random variable independent of E(cid:101)∞ , using (2.23),
| (2.37) | implies | that |     |     |     |     |     |     |
| ------ | ------- | ---- | --- | --- | --- | --- | --- | --- |
√
|     |     |     | E[e−⟨f,E(cid:101)∞(·−S)⟩]=E[e−e |     |     |     | 2SC(f)]. | (2.38) |
| --- | --- | --- | ------------------------------- | --- | --- | --- | -------- | ------ |
√
θλ,
For λ > 2, Kabluchko in [Kab12] proved that t given by (1.1) and started
from θ =PPP(√1 e−µxdx), converges in distribution to a non-trivial point process
2π
which we write as E(cid:101)λ. Again, using the Laplace transform formula for PPP (see
∞
Proposition 2.12 of [Bov17]), formula (2.9), and (2.16), it follows that for all f of
type (2.1),
|     |     |     |     | E[e−⟨f,E(cid:101)∞ | λ⟩]=e−C(f,α(λ)), |     |     | (2.39) |
| --- | --- | --- | --- | ------------------ | ---------------- | --- | --- | ------ |
where C(f,α(λ)) is given as in Lemma 2.9. Furthermore, if S is [−∞,∞)-valued
| random | variable | independent |     | of E(cid:101)λ, | using (2.17), |     | (2.39) implies that |     |
| ------ | -------- | ----------- | --- | --------------- | ------------- | --- | ------------------- | --- |
∞
|     |     |     | E[e−⟨f,E(cid:101)∞ | λ(·−S)⟩]=E[e−eµSC(f,α(λ))]. |     |     |     | (2.40) |
| --- | --- | --- | ------------------ | --------------------------- | --- | --- | --- | ------ |
The point process E(cid:101)λ is a form of extremal point process, namely it is the
∞
supercritical extremal point process of BBM. As an extension to (2.35), Bovier and
√
Hartung introduced in [BH14] a family of decoration point processes Dρ for ρ≥ 2
defined by

16 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
n(t)
(cid:88)
P(Dρ ∈·):= lim P( δ ∈·|M ≥ρt). (2.41)
t→∞
χk(t)−Mt t
k=1
These decoration point processes (Dρ) √ also appear in the extremal processes
ρ≥ 2
of variable speed branching Brownian motions [BH15] and multi-type branching
√
Brownian motions [BM21]. The special case of ρ = 2 gives the decoration
√
point process D 2 = D o
√
f the critical extremal point process E(cid:101)∞ appearing in
(2.36). The Dρ for ρ > 2 are called the supercritical decorations. The E(cid:101)λ
∞
is also a decorated Poisson point process with the decoration given by Dµ for
√ √
µ = λ+ λ2−2 > 2. More precisely, let Pµ = (cid:80) δ be a Poisson point
i≥1 pi
process with intensity µC (α(λ))e−µxdx, where C (α(λ)) is given by (2.18), and
M M
{Dµ,i} beani.i.d. collectionofpointprocessesdistributedasDµ. Then,similarly
i≥1
to (2.36),
(cid:88)
E(cid:101)
∞
λ = δ
pi+D
j
µ,i
. (2.42)
i,j
Since we could not find the above description of E(cid:101)λ explicitly stated in the
∞
literature, we include a proof of (2.42) in Appendix 7, see Proposition 7.1.
2.6. An excerpt from results in [CGS24].
Proposition 2.17 (Theorem 1.4, Remark 6, Proposition 4.1 of [CGS24]).
Let θ be a point process such that θ ∈ N and θ has a finite top particle almost
2
surely. Suppose
Y t := t3 1 /2 (cid:90) 0 (−x)e √ 2xe−x 2 2 tθ(dx)
−∞
is tight in t > 0. Then, given a sequence {t } and a non-negative random
n n≥1
d
variable Z such that Y →Z, it holds that
tn
√
⟨f,θ
tn
2⟩→ d ⟨f,E(cid:101)∞ (·−S)⟩, (2.43)
√ √ √
for all f of form (2.1), where θ 2 is given by (1.1) for λ= 2 started from θ 2 =θ
√ t 0
and S =logZ/ 2. In particular, (2.43) holds for all f ∈C+(R) as well.
c
3. Some Derived properties of θ ∈Dom (Π).
λ
In this section, we derive several structural properties of the point process θ ∈
Dom (Π). Although θ is assumed to be only locally finite, the condition θ ∈
λ
Dom (Π) forces θ to satisfy certain properties, including integrability, tightness
λ
estimates, and lacunarity. These properties and estimates will be key ingredients in
the proofs of the main theorems in the subsequent sections.
√
3.1. Integrability and tightness estimates for θ ∈Dom (Π), with λ≥ 2.
λ
√
Proposition 3.1. Let Π be a fixed point of BBM with drift λ ≥ 2 and let
θ ∈Dom (Π) be a point process. Then,
λ
(1) θ ∈N almost surely (recall the space N given by (2.2)).
2 2
(2) For each K >0, the family of random variables {Za} given by
t t>0
(cid:90) +∞
Za = P(|x+B −λt|≤K)θ(dx)
t t
−∞
is tight, where B is a standard Brownian motion.
t

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 17
(3) For each K >0, the family of random variables {Zb} given by
t t>0
(cid:90) +∞
Zb = P(|x+M −λt|≤K)θ(dx)
t t
−∞
is tight, where M is the maximum particle of BBM {χ (t)} .
t k k≤n(t)
Proof. In order to prove part-(1), we first claim that for all K >0,
(cid:18)(cid:90) ∞ (cid:19)
P P(|x+B −λt|≤K)θ(dx)=+∞ −→0 as t→∞. (3.1)
t
−∞
To this end, let f ∈C+(R) such that f(x)≡1 for x∈[−K,K] and f(x)=0 for
c
|x|≥2K. Since θ ∈ Dom (Π), we have, for all ρ>0, as t→∞,
λ
(cid:104) (cid:105) (cid:104) (cid:105)
E e−ρ⟨f,θ t λ⟩ −→E e−ρ⟨f,Π⟩ . (3.2)
Note that it is a priori possible that ⟨f,θλ⟩=+∞ with positive probability. But,
t
since Π is locally finite, we have ⟨f,Π⟩<∞ almost surely. Then, by Lemma 2.2,
P (cid:0) ⟨f,θλ⟩=+∞ (cid:1) −→0 as t→∞.
t
This, in turn, easily implies that
P (cid:0) θλ([−K,K])=+∞ (cid:1) →0 as t→∞,
t
and
P (cid:0) U(θλ)([−K,K])=+∞ (cid:1) −→0 as t→∞, (3.3)
t
where U(θλ) is the thinning of θλ given by (1.9). Note that
t t
(cid:90) ∞
E (cid:2) U(θ
t
λ)([−K,K]) (cid:12) (cid:12)θ (cid:3) = P(|x+B
t
−λt|≤K)θ(dx). (3.4)
−∞
Conditional on θ, U(θλ)([−K,K]) is a sum of independent Bernoulli random
t
(cid:82)∞
variables. Hence, by part (b) of Lemma 2.3, the event { P(|x+B −λt| ≤
−∞ t
K)θ(dx)=+∞} implies {U(θλ)([−K,K])=+∞}, that is,
t
(cid:18)(cid:90) ∞ (cid:19)
P P(|x+B −λt|≤K)θ(dx)=+∞ ≤P (cid:0) U(θλ)([−K,K])=+∞ (cid:1) . (3.5)
t t
−∞
The above implies (3.1) using (3.3).
Now in order to conclude that θ ∈N almost surely, we note that for a fixed t,
2
as |x|→∞,
ex t 2 P(|x+B t −λt|≤K)−→∞. (3.6)
Therefore, since θ is locally finite, (cid:82) − ∞ ∞ e−x t 2 θ(dx)=+∞ implies (cid:82) − ∞ ∞ P(|x+B t −
λt|≤K)θ(dx)=+∞, which means
(cid:18)(cid:90) ∞ (cid:19) (cid:18)(cid:90) ∞ (cid:19)
P e−x t 2 θ(dx)=+∞ ≤P P(|x+B t −λt|≤K)θ(dx)=+∞ . (3.7)
−∞ −∞
Hence, from (3.1),
(cid:18)(cid:90) ∞ (cid:19)
P e−x t 2 θ(dx)=+∞ −→0 as t→∞. (3.8)
−∞
Let A n := (cid:110) (cid:82) − ∞ ∞ e−x n 2 θ(dx)<∞ (cid:111) . As the events {A n } n∈N are decreasing, we
infer from (3.8) that P(A )→1 as n→∞. Hence
n
 
(cid:18)(cid:90) ∞ (cid:19)
P
e−αx2
θ(dx)<∞,∀α>0 =P
(cid:92)
A n= lim P(A
n
)=1, (3.9)
n→∞
−∞ n≥1

| 18    |          | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |          |           |      |        |         |     |     |     |
| ----- | -------- | --------------------------------------------- | -------- | --------- | ---- | ------ | ------- | --- | --- | --- |
| which | finishes | the                                           | proof of | the claim | θ ∈N | almost | surely. |     |     |     |
2
The proof of part-(2) uses similar arguments as in [CGS23], see section 3.4 in
[CGS23]. Inviewofbeingshortandself-contained,werepeatithereforthereader’s
convenience. Now θ ∈N a.s. implies that Za is almost surely finite and hence a
|     |     |     |     | 2   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
well-definedreal-valuedrandomvariable. Furthermore,itfollowseasilybycontinuity
of Za that for all T > 1, sup |Za| < ∞ almost surely. Hence, it suffices to
| t   |     |     |     | t∈[1,T] | t   |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Za
prove the tightness of for t > T with sufficiently large T. Also, from (1.2), it
t
follows that θλ is a well-defined point process. In particular, the thinning U(θλ)
|     |     | t   |     |     |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
given by (1.9) is a well-defined point process. Hence, for f ∈ C+(R) such that
c
f(x)=1 for x∈[−K,K] and f(x)=0 for |x|≥2K, ⟨f,θλ⟩ is finite almost surely.
t
Using (3.2) again, we conclude that ⟨f,θλ⟩ converges in distribution to ⟨f,Π⟩. In
t
|             |     | ⟨f,θλ⟩ |           |        | Za    | =U(θλ)([−K,K]). |     |          | Za    | ≤⟨f,θλ⟩, |
| ----------- | --- | ------ | --------- | ------ | ----- | --------------- | --- | -------- | ----- | -------- |
| particular, |     |        | is tight. | Let us | write |                 |     |          | Since |          |
|             |     | t      |           |        |       | t               | t   | (cid:12) | t     | t        |
it follows that Za is tight. Recall (3.4), i.e. Za =E[Za(cid:12)θ], and conditional on θ,
|     |     | t   |     |     |     | t   | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Za is a sum of independent Bernoulli random variables. The tightness of Za follows
| t   |     |     |     |     |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by noting
|     |      |       | (cid:18) |             |          | 1   | (cid:19) (cid:18) |          | 1   | (cid:19) |
| --- | ---- | ----- | -------- | ----------- | -------- | --- | ----------------- | -------- | --- | -------- |
|     | P(Za |       | Za       | ≥L;|Za−Za|≥ |          | Za  |                   | Za ≥L;Za |     | Za       |
|     |      | ≥L)≤P |          |             |          |     | +P                |          | ≥   |          |
|     | t    |       | t        | t           | t        | 2 t |                   | t        | t 2 | t        |
|     |      |       | (cid:20) | (cid:21)    | (cid:18) |     | (cid:19)          |          |     |          |
|     |      |       | 4        |             |          | 1   |                   |          |     |          |
|     |      | ≤E    |          | 1 +P        | Za       | ≥ L |                   |          |     |          |
|     |      |       | Za       | Z a≥L       |          | t   |                   |          |     |          |
|     |      |       |          | t           |          | 2   |                   |          |     |          |
t
|     |     |     |     | (cid:18) | (cid:19) |     |     |     |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- |
|     |     |     | 4   | 1        |          |     |     |     |     |     |
|     |     | ≤   | +P  | Za ≥     | L ,      |     |     |     |     |     |
|     |     |     | L   | t 2      |          |     |     |     |     |     |
where we applied part-(a) of Lemma 2.3 conditional on θ in first line to second line
intheabove. SinceZaistight,theabovecomputationimpliesthatZaistightaswell.
|     |     |     | t   |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The proof of the part-(3) is similar to the above: we apply the above arguments
| to the | thinning | M(θλ) | given | by (1.8) | instead | of  | U(θλ). |     |     | □   |
| ------ | -------- | ----- | ----- | -------- | ------- | --- | ------ | --- | --- | --- |
|        |          |       | t     |          |         |     | t      |     |     |     |
Remark 6. The tightness of Zb is deemed to be a better estimate than the tightness
t
of Za since we expect P(|x+M −λt|≤K)≈etP(|x+B −λt|≤K). However, in
| t   |     |     |     | t   |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
view √ of Proposition 2.8, we could only verify this for a certain range of x, e.g. for
λ> 2 and x∈[−bt,−at], a,b>0. In particular, we could not verify this for x in
a neighbourhood of +∞, e.g. for {x>bt}. As such, the tightness of Za will also be
t
| useful        | to us. |          |     |           |      |     |     |     |     |     |
| ------------- | ------ | -------- | --- | --------- | ---- | --- | --- | --- | --- | --- |
| 3.2. Lacunary |        | property |     | of θ ∈Dom | (Π). |     |     |     |     |     |
λ
√
Proposition 3.2. Let Π be a fixed point of BBM with drift λ ≥ 2 and let
| θ ∈Dom | (Π) | be a | point | process. Then, |     | (recall Definition |     | 1.4) |     |     |
| ------ | --- | ---- | ----- | -------------- | --- | ------------------ | --- | ---- | --- | --- |
λ
√
| (1) | For | λ>  | 2, θ is | lacunary. |     |     |     |     |     |     |
| --- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
√
| (2) | For | λ=  | 2, θ is | exponentially-lacunary. |     |     |     |     |     |     |
| --- | --- | --- | ------- | ----------------------- | --- | --- | --- | --- | --- | --- |
∈C+(R)
Proof. Let K >0 and f such that f(x)=1 for x∈[−K,K] and f(x)=0
c
| for |x|≥2K. |     | Then, | for ρ>0, | using                     | Lemma | 2.5, |     |     |                  |     |
| ----------- | --- | ----- | -------- | ------------------------- | ----- | ---- | --- | --- | ---------------- | --- |
|             |     |       |          | (cid:20) (cid:26)(cid:90) | ∞     |      |     |     | (cid:27)(cid:21) |     |
λ⟩]=E
|     |     | E[e−ρ⟨f,θ | t   | exp | log(1−u |     | (t,λt−x))θ(dx) |     | ,   | (3.10) |
| --- | --- | --------- | --- | --- | ------- | --- | -------------- | --- | --- | ------ |
ϕ
−∞
| where | ϕ(x)=1−e−ρf(−x). |     |        | For δ >0,       | let |     |         |           |     |        |
| ----- | ---------------- | --- | ------ | --------------- | --- | --- | ------- | --------- | --- | ------ |
|       |                  |     |        |                 |     | √   | 3       |           |     |        |
|       |                  | Qδ  |        | (cid:12)        |     |     | (cid:0) | (cid:1)   |     |        |
|       |                  |     | :={x∈R | (cid:12)|λt−x|≤ |     | 2t− | √       | +δ logt}. |     | (3.11) |
|       |                  |     | t      |                 |     |     | 2 2     |           |     |        |

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 19
Then, by using Lemma 2.7,
α := sup(1−u (t,λt−x))→0
t ϕ
x∈Qδ
t
as t→∞. Hence,
(cid:20) (cid:26)(cid:90) ∞ (cid:27)(cid:21)
E[e−ρ⟨f,θ t λ⟩]=E exp log(1−u ϕ (t,λt−x))θ(dx) (3.12)
−∞
(cid:20) (cid:26)(cid:90) (cid:27)(cid:21)
≤E exp log(1−u (t,λt−x))θ(dx)
ϕ
Qδ
t
(cid:20) (cid:26) (cid:27)(cid:21)
≤E exp logα ×θ(Qδ)
t t
(cid:20) (cid:26) (cid:27) (cid:21)
=E exp logα ×θ(Qδ) 1 +P(θ(Qδ)=0)
t t θ(Qδ)≥1 t
t
≤α +P(θ(Qδ)=0).
t t
Taking t→∞ in the above, since α →0 and θ ∈Dom (Π), we obtain
t λ
liminfP(θ(Qδ)=0)≥E[e−ρ⟨f,Π⟩],
t
t→∞
andsinceΠislocallyfinitealmostsurely,takingρ→0+,weconcludethatP(θ(Qδ)=
t
0)→1, which is equivalent to θ(Qδ)→ P 0 as t→∞. Finally, we note that for Qδ
√ t√ √ t
given by (3.11), if λ> 2, c>λ− 2 and d<λ+ 2, then [ct,dt]⊂Qδ for all t
√ √ t
large enough. For λ= 2, if c> √3 +δ and d<2 2, then [clogt,dt]⊂Qδ for all
2 2 √ t
P P
t large enough. Hence, θ([ct,dt]) → 0 (resp. θ([clogt,dt]) → 0) for λ > 2 (resp.
√
λ= 2).
□
√
4. Proof of Theorem 1.2 and Theorem 1.5 for λ> 2.
√
In this section, we prove Theorem 1.2 and Theorem 1.5 for the case λ > 2.
Following a strategy similar to that in [CGS23], we decompose the contribution
of the initial point process into several regions and show that only particles in an
√ √
O( t)-neighbourhood of the location − λ2−2t contribute to the limiting point
process.
Inparticular,thestructuralpropertiesestablishedinSection3allowustocontrol
thecontributionsfromdifferentregionswithoutimposingtheadditionalassumptions
on the initial point process required in [CGS23] and [CGS24].
√ √
Let a,b,L > 0 be fixed constants such that b > λ+ 2 and a < λ− 2. For
√ √
µ=λ+ λ2−2, write γ =µ−λ= λ2−2. We divide R into the following sets:
E1 =(−at,at),
t
E2 =(−∞,−bt)∪(bt,∞),
t
E3 =[at,bt], (4.1)
t
√
E4 =[−bt,−γt−L t],
t
√
E5 =[−γt+L t,−at],
t
√ √
E6 =(−γt−L t,−γt+L t).
t
For a fixed point Π and a point process θ ∈Dom (Π), for f ∈C+(R), Lemma
λ c
2.5 gives

| 20  | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |          |                    |     |     |     |                  |     |
| --- | --------------------------------------------- | --- | -------- | ------------------ | --- | --- | --- | ---------------- | --- |
|     |                                               |     | (cid:20) | (cid:26)(cid:90) ∞ |     |     |     | (cid:27)(cid:21) |     |
λ⟩]=E
|     | E[e−⟨f,θ | t   | exp |     | log(1−u | (t,λt−x))θ(dx) |     | ,   | (4.2) |
| --- | -------- | --- | --- | --- | ------- | -------------- | --- | --- | ----- |
ϕ
−∞
| where ϕ(x)=1−e−f(−x). |     |            | We  | write |     |     |            |     |     |
| --------------------- | --- | ---------- | --- | ----- | --- | --- | ---------- | --- | --- |
|                       |     | (cid:90) ∞ |     |       |     |     | (cid:88) 6 |     |     |
Ii,
|     |     |     | log(1−u | ϕ (t,λt−x))θ(dx)= |     |     |     |     | (4.3) |
| --- | --- | --- | ------- | ----------------- | --- | --- | --- | --- | ----- |
t
|     |     | −∞  |     |     |     |     | i=1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where
(cid:90)
Ii
|     |     |     | :=  | log(1−u | ϕ (t,λt−x))θ(dx). |     |     |     | (4.4) |
| --- | --- | --- | --- | ------- | ----------------- | --- | --- | --- | ----- |
t
Ei
t
We show that in the limit t→∞, I1,I2,I3 → P 0. Also, I4,I5 → P 0 as t→∞ and
|     |     |     |     |     | t t | t   | t t |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
then L→∞. Finally, we show that I6 will converge in distribution to a random
t
| variable | as t→∞ | and | then L→∞. |     |     |     |     |     |     |
| -------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- |
P
4.1. Proof of convergence I1,I2 → 0. Wefirstrecordthefollowinglemma,which
|              |        |        | t   | t   |     |     |     |     |     |
| ------------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| will be used | in the | proof. |     |     |     |     |     |     |     |
Lemma 4.1. Let K > 0 and E = E1 or E2. Then, there exists some u ≥ 0
|            |       |           |     | t   | t   | t   |     |     |     |
| ---------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
| (depending | on t) | such that |     |     |     |     |     |     |     |
etP(|x+B
−λt|≤K)
|         |                |     | sup          |     | t         | −→0 |     |     | (4.5) |
| ------- | -------------- | --- | ------------ | --- | --------- | --- | --- | --- | ----- |
|         |                |     | P(|x+B       |     | −λu|≤K)   |     |     |     |       |
|         |                |     | x∈Et         |     | u         |     |     |     |       |
| as t→∞. | In particular, |     |              |     |           |     |     |     |       |
|         |                |     | sup etP(|x+B |     | −λt|≤K)→0 |     |     |     | (4.6) |
t
x∈Et
√
as t → ∞. (4.5) and (4.6) hold for λ = 2 and E = E2 = {|x| > bt} for any
| √         |            |     |          |     |          | t      | t       |     |     |
| --------- | ---------- | --- | -------- | --- | -------- | ------ | ------- | --- | --- |
| b>2 2     | as well.   |     |          |     |          |        |         |     |     |
| Proof. By | definition |     |          |     |          |        |         |     |     |
|           |            |     |          |     | (cid:90) | K et   |         |     |     |
|           | etP(|x+B   |     |          |     |          | e−(y−x | + λt)2  |     |     |
|           |            |     | −λt|≤K)= |     |          | √      | 2 t dy, |     |     |
|           |            |     | t        |     |          | 2πt    |         |     |     |
−K
|     |        |     |          |     | (cid:90) | K 1    |         |     |     |
| --- | ------ | --- | -------- | --- | -------- | ------ | ------- | --- | --- |
|     |        |     |          |     |          | e−(y−x | + λu)2  |     |     |
|     | P(|x+B |     | −λu|≤K)= |     |          | √      | 2 u dy. |     |     |
|     |        |     | u        |     |          | 2πu    |         |     |     |
−K
Weshowthattheratioofthetwodensitiesabovegoestozerouniformlyoverx∈E ,
t
| y ∈[−K,K] | for | some choice | of  | u, i.e. |     |     |     |     |     |
| --------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
(cid:114)
|     |     |     |     | u   |        | λu)2    | λt)2 |     |       |
| --- | --- | --- | --- | --- | ------ | ------- | ---- | --- | ----- |
|     |     |     | sup | ete | (y−x + | −(y−x + | −→0  |     | (4.7) |
|     |     |     |     |     | 2      | u 2     | t    |     |       |
t
x∈Et,y∈[−K,K]
| as t→∞. | Note | that   |            |        |       |                 |         |     |     |
| ------- | ---- | ------ | ---------- | ------ | ----- | --------------- | ------- | --- | --- |
|         | ete  | (y−x + | λu)2 −(y−x | + λt)2 | =et+λ | 2 (u−t)+(y−x)2[ | 1 − 1   | ]   |     |
|         |      | 2      | u          | 2 t    |       | 2               | 2 u 2 t | .   |     |
For E =E 1, we pick u= L t where L := sup |y−x|. Note that u<t
|     | t t |     | λ   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x∈E1,y∈[−K,K]
t
and
|     |     | et+λ 2 (u−t)+(y−x)2[ |     | 1   | − 1 ] ≤et+λ | 2 (u−t)+L2 | [ 1 − 1   | ]   |     |
| --- | --- | -------------------- | --- | --- | ----------- | ---------- | --------- | --- | --- |
|     |     | 2                    |     | 2 u | 2 t         | 2          | t 2 u 2 t |     |     |
|     |     |                      |     |     | =et+λLt−L   | 2          | 2t        |     |     |
t−λ
|     |     |     |     |     |     | 2t  | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
≤e−δt,
for some δ > 0, where in the last inequality we have used the fact that for L =
|     |     |     | √   |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
at+K for some a < λ− 2. This implies (4.7). Similarly, for E = E2, we
t t

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 21
note that the above estimate continues to hold by taking u = L(cid:101)t > t where
√ λ
L(cid:101)t := inf |y −x| = bt−K for some b > λ+ 2. Also note that this
x∈E t 2,y∈[−K,K] √ √
estimate holds for λ= 2 and E =E2 ={|x|>bt} for any b>2 2 as well. □
t t
Now, let f ∈C+(R) and K >0 be such that f(x)=0 for |x|≥K. Using (2.26),
c
we obtain that
u (t,λt−x)≤etE[f(x+B −λt)]
ϕ t
≲etP(|x+B −λt|≤K). (4.8)
t
By (4.6), u (t,λt−x) → 0 as t → ∞ uniformly over x ∈ E1 and x ∈ E2. Hence,
ϕ t t
for i=1,2,
(cid:90) (cid:90)
Ii = log(1−u (t,λt−x))θ(dx)=−(1+o (1)) u (t,λt−x)θ(dx). (4.9)
t ϕ t ϕ
Ei Ei
t t
Furthermore, using (4.8),
(cid:90) (cid:90)
u (t,λt−x)θ(dx)≲ etP(|x+B −λt|≤K)θ(dx) (4.10)
ϕ t
Ei Ei
t t
etP(|x+B −λt|≤K)(cid:90)
≤ sup t P(|x+B −λu|≤K)θ(dx),
P(|x+B −λu|≤K) u
x∈Ei u Ei
t t
where we have picked u from Lemma 4.1. Then, from (4.5) and the tightness of
Za = (cid:82)+∞ P(|x+B −λt|≤K)θ(dx) given by Proposition 3.1, we conclude that
t −∞ t
(cid:90)
P
u (t,λt−x)θ(dx)→0,
ϕ
Ei
t
which in turn implies Ii → P 0 for i=1,2 as t→∞.
t
4.2. Proof of convergence I3 → P 0. The proof follows immediately from Proposi-
t
tion 3.2 as follows. Since θ is an integer-valued measure,
(cid:18)(cid:90) (cid:19)
P(I3 <0)=P log(1−u (t,λt−x))θ(dx)<0
t ϕ
[at,bt]
≤P(θ([at,bt])>0)
=P(θ([at,bt])≥1).
Then, since θ is lacunary, using Remark 2, P(θ([at,bt]) ≥ 1) → 0. Hence,
P(I3 >0)→0 as t→∞.
t
√
4.3. A reformulation of the tightness property of θ ∈Dom (Π) for λ> 2.
λ
Before proving I4,I5 → P 0, we record a consequence of the tightness property
t t
θ ∈Dom (Π) given by Proposition 3.1.
λ
√
Proposition 4.2. Let Π be a fixed point of BBM with drift λ > 2 and θ ∈
Dom (Π). Then, the family of random variables Z given by
λ t
Z t := (cid:90) 0 √ 1 e(1−λ 2 2 )teλxe−x 2 2 tθ(dx) (4.11)
t
−∞
is tight in t≥1.

22 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
√
Proof. Using (4.10), we have for b>λ+ 2,
(cid:90) −bt
etP(|x+B −λt|≤K)θ(dx)→ P 0
t
−∞
as t→∞. Also, uniformly over x<0,
etP(|x+B t −λt|≤K)= √ et (cid:90) K e−(y+λ 2 t t −x)2 dy (4.12)
2πt
−K
= √ 1 e(1−λ 2 2 )teλxe−x 2 2 t (cid:90) K e−y 2 2 t −yλ+x t y dy
2πt
−K
≥ √ 1 e(1−λ 2 2 )teλxe−x 2 2 t (cid:90) 0 e−y 2 2 t −yλdy
2πt
−K
≳ √ 1 e(1−λ 2 2 )teλxe−x 2 2 t.
t
This implies that
(cid:90) −bt √ 1 e(1−λ 2 2 )teλxe−x 2 2 tθ(dx)→ P 0. (4.13)
t
−∞
Since θ ∈N almost surely, clearly for all t >1,
2 0
sup (cid:90) −bt √ 1 e(1−λ 2 2 )teλxe−x 2 2 tθ(dx)<∞ almost surely.
1≤t≤t0 −∞ t
Hence, the convergence (4.13) implies the tightness of (cid:82)−bt √1 e(1−λ 2 2 )teλxe−x 2 2 tθ(dx)
−∞ t
in t≥1.
For the tightness of (cid:82)0 √1 e(1−λ 2 2 )teλxe−x 2 2 tθ(dx), we note using (2.7),
−bt t
√ √
P(|x+M −λt|≤K)=u (t,z+ 2t−K)−u (t,z+ 2t+K),
t M M
√ √ √
where z = (λ− 2)t−x. For x ∈ [−bt,0], z ∈ [(λ− 2)t,(λ− 2+b)t]. Hence,
using (2.20), for K large enough and t≥t ,
0
P(|x+M t −λt|≤K)≳ √ 1 e− √ 2ze−z 2 2 t. (4.14)
t
√
Note that for z =(λ− 2)t−x,
√ 1 e− √ 2ze−z 2 2 t = √ 1 e(1−λ 2 2 )teλxe−x 2 2 t. (4.15)
t t
Then, the tightness of Zb given by Proposition 3.1 completes the proof.
t
□
4.4. ProofofconvergenceI4,I5 → P 0. UsingLemma2.14,weknowthatu (t,λt−
t t ϕ
x)→0 uniformly over x≤0. Hence,
(cid:90) (cid:90)
log(1−u (t,λt−x))θ(dx)=−(1+o (1)) u (t,λt−x)θ(dx).
ϕ t ϕ
[−bt,−at] [−bt,−at]
(4.16)
Also, by Lemma 2.11-(a) and relation (4.15), we have that for x∈[−bt,−at],
u ϕ (t,λt−x)≲ √ 1 e(1−λ 2 2 )teλxe−x 2 2 t. (4.17)
t
Therefore, it suffices to prove that for i=4,5, as t→∞ and then L→∞,
(cid:90) √ 1 e(1−λ 2 2 )teλxe−x 2 2 tθ(dx)→ P 0. (4.18)
Ei t
t

|     | LOCALLY |     | FINITE | FIXED | POINTS | OF BRANCHING |     | BROWNIAN | MOTION | 23  |
| --- | ------- | --- | ------ | ----- | ------ | ------------ | --- | -------- | ------ | --- |
|     |         |     |        |       | √      |              |     |          | √      |     |
To this end, choose u = t+ √L t for i = 4 and u = t− √L t for i = 5.
|     |     |     |     |     | λ2−2 |     |     | √   | λ2−2 |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- |
For this choice of u, note that |x| = −x ≥ γt + L t = γu for x ∈ E4 and
|     |     |     | √   |     |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|x|=−x≤γt−L t=γu for x∈E5. Hence, uniformly over x∈E4 or x∈E5,
|            |     |            |       |            |     | t          |                |             | t       | t      |
| ---------- | --- | ---------- | ----- | ---------- | --- | ---------- | -------------- | ----------- | ------- | ------ |
|            |     | √1         | e(1−λ | 2 )teλxe−x | 2   | (cid:114)  |                |             |         |        |
|            |     |            |       | 2          | 2 t | u          | 2              | 2           |         |        |
|            |     |            | t     |            |     | =          | e(λ −1)(u−t)+x |             | ( 1−1 ) |        |
|            |     |            |       |            |     |            | 2              | 2           | u t     |        |
|            |     | √1         | e(1−λ | 2)ueλxe−x  | 2   | t          |                |             |         |        |
|            |     |            |       | 2          | 2u  |            |                |             |         |        |
|            |     |            | u     |            |     |            |                |             |         | (4.19) |
|            |     |            |       |            |     | ≲e(λ 2     | −1)(u−t)+(λ2−  | 2)u2t       | − u     |        |
|            |     |            |       |            |     | 2          |                | 2           | t u     |        |
|            |     |            |       |            |     | =e−L 2     |                |             |         |        |
|            |     |            |       |            |     | 2          | .              |             |         |        |
| Therefore, |     | for i=4,5, |       | recalling  | Z   | as defined | in             | Proposition | 4.2, we | have   |
t
| (cid:90) | 1       |            |              |     |     | (cid:90) 0 | 1     |            |             |         |
| -------- | ------- | ---------- | ------------ | --- | --- | ---------- | ----- | ---------- | ----------- | ------- |
|          | √ e(1−λ | 2 )teλxe−x | 2 tθ(dx)≲e−L |     |     | 2 √        | e(1−λ | 2 )ueλxe−x | 2 θ(dx)=e−L | 2       |
|          |         | 2          | 2            |     |     | 2          |       | 2          | 2u          | 2 Z u . |
|          | t       |            |              |     |     |            | u     |            |             |         |
| Ei       |         |            |              |     |     | − ∞        |       |            |             |         |
|          | t       |            |              |     |     |            |       |            |             | (4.20)  |
Since Z is tight by Proposition 4.2, by taking L→∞, this implies (4.18) which
u
| completes |     | the proof. |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
|           |     |            |     | I6. | Ii  | P   |     |     |     |     |
4.5. Convergence of Since → 0 for 1 ≤ i ≤ 5, it follows using (4.2) and
|        |      |             |                   | t        | t      |      |                  |           |     |     |
| ------ | ---- | ----------- | ----------------- | -------- | ------ | ---- | ---------------- | --------- | --- | --- |
| (4.16) | that | for a fixed | point             | Π,       | θ ∈Dom | (Π), | and              | f ∈C+(R), |     |     |
|        |      |             |                   |          |        | λ    |                  | c         |     |     |
|        |      |             | (cid:20) (cid:26) | (cid:90) |        |      | (cid:27)(cid:21) |           |     |     |
→E[e−⟨f,Π⟩]
|     |     | E   | exp | −   | u (t,λt−x)θ(dx) |     |     |     |     | (4.21) |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | ------ |
ϕ
E6
t
| as t→∞ |     | and then | L→∞. |     |     |     |     |     |     |     |
| ------ | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Now, define
(cid:90)
|     |     |     |     |     | 1    | 2              |     | 2       |     |        |
| --- | --- | --- | --- | --- | ---- | -------------- | --- | ------- | --- | ------ |
|     |     |     | Z   | :=  | √    | e(1−λ )teλxe−x |     | tθ(dx). |     | (4.22) |
|     |     |     |     | t,L |      | 2              |     | 2       |     |        |
|     |     |     |     |     | E6 t |                |     |         |     |        |
t
E6
For each fixed L>0, ⊂(−∞,0) for all sufficiently large t, and hence Z t,L ≤Z t .
t
Therefore, using Proposition 4.2, Z is tight in the regime under consideration.
t,L
The tightness implies subsequential convergence in distribution. Let τ =(t ,L )
n m
| be a | sequence | such | that | t →∞, | L   | →∞ and |     |     |     |        |
| ---- | -------- | ---- | ---- | ----- | --- | ------ | --- | --- | --- | ------ |
|      |          |      |      | n     | m   |        |     |     |     |        |
|      |          |      |      |       |     | d      | Zτ  |     |     |        |
|      |          |      |      |       | Z   | →      |     |     |     | (4.23) |
tn,Lm
as n→∞ and then m→∞, where Zτ is a non-negative random variable (the limit
| may  | a priori | depend    | on  | the sequence | √             | τ). |     |      |      |     |
| ---- | -------- | --------- | --- | ------------ | ------------- | --- | --- | ---- | ---- | --- |
| Note | that     | for x∈E6, |     | z =(λ−       | 2)t−x=α(λ)t+o |     |     | (1), | with |     |
|      |          |           | t   |              |               |     |     | t    |      |     |
|      |          |           |     |              |               |     | √   | √    |      |     |
(cid:112)
|        |       |             | α(λ)=λ+ |         |         | λ2−2− | 2=µ−     | 2.          |         |     |
| ------ | ----- | ----------- | ------- | ------- | ------- | ----- | -------- | ----------- | ------- | --- |
| Hence, | using | Proposition |         | 2.9 and | (4.15), | for   | f of the | type (2.1), | we have |     |
1
|     |     |     |                       |     |     |     | e(1−λ | 2 )teλxe−x | 2   |        |
| --- | --- | --- | --------------------- | --- | --- | --- | ----- | ---------- | --- | ------ |
|     |     |     | u (t,λt−x)∼C(f,α(λ))√ |     |     |     |       | 2          | 2 t | (4.24) |
|     |     |     | ϕ                     |     |     |     | t     |            |     |        |
d
uniformly over x∈E6. Since Z → Zτ, it follows that for all f of type (2.1),
|     |     |     | t   |     | tn,Ln |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
(cid:90)
|     |     |     |     | u (t,λt−x)θ(dx)→ |     |     | d ZτC(f,α(λ)) |     |     | (4.25) |
| --- | --- | --- | --- | ---------------- | --- | --- | ------------- | --- | --- | ------ |
ϕ
E6
t
| along | the       | subsequence | τ.        |     |           |     |     |     |     |     |
| ----- | --------- | ----------- | --------- | --- | --------- | --- | --- | --- | --- | --- |
| Now,  | similarly |             | to (1.1), | let | us define |     |     |     |     |     |
ni(t)
|     |     |     |     |       | (cid:88) | (cid:88) |       |        |     |        |
| --- | --- | --- | --- | ----- | -------- | -------- | ----- | ------ | --- | ------ |
|     |     |     |     | θλ := |          |          | δ     | .      |     | (4.26) |
|     |     |     |     | t,L   |          |          | xi+χi | (t)−λt |     |        |
k
|     |     |     |     |     | i∈I,xi∈E | 6 k=1 |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | ----- | --- | --- | --- | --- |
t

| 24  |     | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |     |
| --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
Note that since θλ is starting from θ| , which has a finite top particle, and
|     |     |     | t,L |     |     | E6 t |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
,Lemma2.1givesthatθλ
| θ ∈N | 2   |     |     |     | alsohasafinitetopparticlealmostsurely. |     |     | Hence, |
| ---- | --- | --- | --- | --- | -------------------------------------- | --- | --- | ------ |
t,L
⟨f,θλ ⟩<∞ a.s. forf of type (2.1). Then, it follows using (2.9), (2.28),(4.16), and
t,L
| (4.25) | that | for f of | the type | (2.1),   |                       |     |     |        |
| ------ | ---- | -------- | -------- | -------- | --------------------- | --- | --- | ------ |
|        |      |          |          | E[e−⟨f,θ | λ ⟩]→E[e−ZτC(f,α(λ))] |     |     |        |
|        |      |          |          |          | t ,L                  |     |     | (4.27) |
along subsequence τ. By (2.40), E[e−ZτC(f,α(λ))] is the Laplace transform of
| ⟨f,E(cid:101)λ(·−Sτ)⟩ |     |       | Sτ  | :=log(Zτ)/µ |     |                    |        | (Zτ      |
| --------------------- | --- | ----- | --- | ----------- | --- | ------------------ | ------ | -------- |
|                       |     | where |     |             |     | is a [−∞,∞)-valued | random | variable |
∞
| can | be zero | with positive |     | probability). |     | It hence follows | that |     |
| --- | ------- | ------------- | --- | ------------- | --- | ---------------- | ---- | --- |
d
|     |          |             |     | ⟨f,θλ | ⟩→  | ⟨f,E(cid:101) λ(·−Sτ)⟩ |     | (4.28) |
| --- | -------- | ----------- | --- | ----- | --- | ---------------------- | --- | ------ |
|     |          |             |     |       | t,L | ∞                      |     |        |
| for | all f of | type (2.1). |     |       |     |                        |     |        |
Observe that functions of the form 1 (x) for −∞<c<d<∞ can be written
[c,d)
as difference of functions of type (2.1). Therefore, (4.28) holds for functions f in
the span of {1 (x)|−∞<c<d<∞}. It then follows from standard arguments
[c,d)
that (4.28) holds for f ∈C+(R) as well. This in turn implies using (4.2) and (4.16)
c
∈C+(R),
| again | that | for f |     |     |     |     |     |     |
| ----- | ---- | ----- | --- | --- | --- | --- | --- | --- |
c
|     |     | (cid:20) | (cid:26) (cid:90) |                 |     | (cid:27)(cid:21)    |           |        |
| --- | --- | -------- | ----------------- | --------------- | --- | ------------------- | --------- | ------ |
|     |     | E exp    | −                 | u (t,λt−x)θ(dx) |     | →E[e−⟨f,E(cid:101)∞ | λ(·−Sτ)⟩] | (4.29) |
ϕ
E6
t
along the subsequence τ. Then, by comparing this to (4.21), we conclude that
|     |     |     |     |     | d λ(·−Sτ).    |     |     |        |
| --- | --- | --- | --- | --- | ------------- | --- | --- | ------ |
|     |     |     |     |     | Π= E(cid:101) |     |     | (4.30) |
∞
Sτ d
Since the law of Π does not depend on the subsequence τ, it follows that = S
for some [−∞,∞) valued random variable S for all subsequences τ. As a result, we
get
|     |     |     |     |     | d             | λ(·−S). |     |        |
| --- | --- | --- | --- | --- | ------------- | ------- | --- | ------ |
|     |     |     |     |     | Π= E(cid:101) |         |     | (4.31) |
∞
Zτ
Furthermore, this implies that all subsequential limits given by (4.23) have
the same law as Z :=eµS, which in turn implies that for Z given by (4.22),
t,L
d
|     |     |     |     |     | Z   | →Z  |     | (4.32) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ |
t,L
| as t→∞ |     | and then | L→∞. |     |     |     |     |     |
| ------ | --- | -------- | ---- | --- | --- | --- | --- | --- |
√
Proof of Theorem 1.2 and Theorem 1.5 for λ> 2. Theorem 1.2 has already been
proved by by (4.31). Also, for θ ∈ Dom λ (Π), it satisfies (H1), (H2), (H3) by
| Proposition |     | 3.2, Proposition |     | 3.1, | Proposition | 4.2, and | (4.32). |     |
| ----------- | --- | ---------------- | --- | ---- | ----------- | -------- | ------- | --- |
Conversely, if θ satisfies (H1), (H2), (H3), it can be seen from the proofs above
that Ii → P 0 for 1≤i≤5 still holds. Furthermore, since (H3) gives (4.32), it follows
t
as above that θ λ → d E(cid:101) λ(·−S) with S = logZ/µ. Hence, θ ∈ Dom (Π) with
|     |                   | t ,L | ∞   |     |     |     |     | λ   |
| --- | ----------------- | ---- | --- | --- | --- | --- | --- | --- |
| d   | E(cid:101)λ(·−S). |      |     |     |     |     |     | □   |
Π=
∞
√
|     | 5.  | Proof | of Theorem |     | 1.2 | and Theorem | 1.5 for λ= | 2.  |
| --- | --- | ----- | ---------- | --- | --- | ----------- | ---------- | --- |
√
The proof of Theorem 1.2 and Theorem 1.5 for λ= 2 again follows a strategy
similar to that in the previous section. Much of the groundwork in this case was al-
ready established in [CGS24], see Proposition 2.17, using which we can considerably
√
simplify the proof. Compared with the case λ > 2, the critical regime requires
different estimates for the F-KPP equation and relies on the exponentially-lacunary
property in part (2) of Proposition 3.2 to rule out the contribution from the inter-
mediate regions.

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 25
√
Let Π be a fixed point of BBM with drift λ= 2 and θ ∈Dom (Π). Then, for
λ
f ∈C+(R), Lemma 2.5 gives
c
√ (cid:20) (cid:26)(cid:90) ∞ √ (cid:27)(cid:21)
E[e−⟨f,θ t 2⟩]=E exp log(1−u ϕ (t, 2t−x))θ(dx) , (5.1)
−∞
where ϕ(x)=1−e−f(−x). We assume f is supported in [−K,K].
√
For constants a>0 small enough and b>2 2, we divide R into sets
F1 =(bt,∞),
t
F2 =[alogt,bt], (5.2)
t
F3 =[0,alogt),
t
F4 =(−∞,0),
t
and write
(cid:90) ∞ √ 4
(cid:88)
log(1−u (t, 2t−x))θ(dx)= Ji, (5.3)
ϕ t
−∞ i=1
where
(cid:90) √
Ji := log(1−u (t, 2t−x))θ(dx). (5.4)
t ϕ
Fi
t
Weshowthatinthelimitt→∞,J1,J2,J3 → P 0,andJ4 convergesindistribution
t t t t
to a random variable.
√
5.1. The proof of J1 → P 0. Wenote,using (2.26)andLemma4.1,thatu (t, 2t−
t √ ϕ
x)→0 uniformly over x∈(−∞,−bt)∪(bt,∞) for any b>2 2. Hence,
(cid:90) √ (cid:90) √
log(1−u (t, 2t−x))θ(dx)=−(1+o (1)) u (t, 2t−x)θ(dx). (5.5)
ϕ t ϕ
|x|>bt |x|>bt
Also, choosing u>0 as in Lemma 4.1,
(cid:90) √
etP(|x+B − 2t|≤K)θ(dx) (5.6)
t
|x|>bt
√
etP(|x+B − 2t|≤K)(cid:90) √
≤ sup t √ P(|x+B − 2u|≤K)θ(dx).
u
P(|x+B − 2u|≤K)
|x|>bt u |x|>bt
Then, Lemma 4.1 and Proposition 3.1 imply that
(cid:90) √
etP(|x+B − 2t|≤K)θ(dx)→ P 0, (5.7)
t
|x|>bt
which in turn, using (2.26), implies
(cid:90) √
P
u (t, 2t−x)θ(dx)→0. (5.8)
ϕ
|x|>bt
This in particular implies J1 → P 0.
t

26 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
5.2. The proof of J2 → P 0. The proof is immediate from Proposition 3.2 as follows.
t
Since θ is an integer-valued measure,
(cid:18)(cid:90) √ (cid:19)
P(J2 <0)=P log(1−u (t, 2t−x))θ(dx)<0
t ϕ
[alogt,bt]
≤P(θ([alogt,bt])>0)
=P(θ([alogt,bt])≥1).
Then,sinceθisexponentially-lacunary,usingRemark2,P(θ([alogt,bt])≥1)→0
for all b>a>0. Hence, P(J2 >0)→0 as t→∞.
t
√
5.3. A reformulation of the tightness property of θ ∈Dom (Π) for λ= 2.
√ λ
We note the corresponding variant of Proposition 4.2 for λ= 2.
√
Proposition 5.1. Let Π be a fixed point of BBM with drift λ = 2 and θ ∈
Dom
λ
(Π). Then, the random variables {Y(cid:101)
t
b}
t≥1
given by
Y(cid:101) t b := (cid:90) 1 4 logt t3 1 /2 (−x+logt)e √ 2xe−x 2 2 tθ(dx) (5.9)
−∞
is tight.
Proof. The tightness of
1 (cid:90) 1 4 logt (−x+logt)e √ 2xe−x 2 2 tθ(dx)
t3/2
−bt
is an immediate consequence of part-(3) of Proposition 3.1 and lower bound in
Lemma 2.16. On the other hand, using (5.7), we know that
(cid:90) −bt √
etP(|x+B − 2t|≤K)θ(dx)→ P 0, (5.10)
t
−∞
and, similarly to (4.12), for x≤−bt,
etP(|x+B t − √ 2t|≤K)= √ 1 e √ 2xe−x 2 2 t (cid:90) K e−y 2 2 t − √ 2y+x t y dy
2πt
−K
≳ √ 1 e √ 2xe−x 2 2 t (cid:90) 0 e x t y dy
t
−K
= √ 1 e √ 2xe−x 2 2 t t (1−e−Kx/t)
t x
≳ √ 1 e √ 2xe−x 2 2 t t x2 ≳ 1 (−x+logt)e √ 2xe−x 2 2 t,
t −x t2 t3/2
where in last line we have used er −1 ≳ r2 for r ≥ Kb, with r = −Kx for all
t
sufficiently large t. It hence follows that
1 (cid:90) −bt (−x+logt)e √ 2xe−x 2 2 tθ(dx)→ P 0.
t3/2
−∞
This, together with the fact that θ ∈N almost surely, implies the tightness of
2
1 (cid:90) −bt (−x+logt)e √ 2xe−x 2 2 tθ(dx),
t3/2
−∞
which completes the proof. □

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 27
√
5.4. The proof of J3 → P 0. UsingLemma2.14,fora>0smallenough,u (t, 2t−
t ϕ
x)→0 uniformly over x≤alogt, and
(cid:90) √ (cid:90) √
log(1−u (t, 2t−x))θ(dx)=−(1+o (1)) u (t, 2t−x)θ(dx). (5.11)
ϕ t ϕ
F3 F3
t t
Using (2.27) and (2.25), for x∈[0,alogt],
√ √ logt √
u (t, 2t−x)≤u (t, 2t−x−K)≲ e 2x.
ϕ M t3/2
Hence, it suffices to show that
(cid:90) alogt logt √
e 2xθ(dx)→ P 0. (5.12)
t3/2
0
To this end, note that for x∈[0,1logt],
4
logt e √ 2x ≲ 1 (−x+logt)e √ 2xe−x 2 2 t.
t3/2 t3/2
Thus, Proposition 5.1 implies that
(cid:90) 1 4 logt logt e √ 2xθ(dx) (5.13)
t3/2
0
√
is tight in t≥1. Then, by taking u= t, for a small enough,
(cid:90) alogt logt e √ 2xθ(dx)≲ 1 (cid:90) alogt logu e √ 2xθ(dx)≲ 1 (cid:90) 1 4 logu logu e √ 2xθ(dx).
t3/2 t3/4 u3/2 t3/4 u3/2
0 0 0
(5.14)
Therefore, the tightness in (5.13) implies (5.12), which completes the proof.
5.5. The convergence of J4. Proposition 5.1 implies that
t
Y t = t3 1 /2 (cid:90) 0 (−x)e √ 2xe−x 2 2 tθ(dx)
−∞
is tight in t≥1. Let τ ={t } be a sequence such that Y → d Zτ along τ to some
n n≥1 t
non-negative random variable Zτ.
Similarly as (1.1), let us define
ni(t)
(cid:88) (cid:88)
θ< := δ √ . (5.15)
t xi+χi
k
(t)− 2t
xi<0 k=1
Clearly, as in (5.1), we have
E[e−⟨f,θ t <⟩]=E[eJ t 4 ]. (5.16)
Now, using Proposition 2.17, along the sequence τ,
⟨f,θ
t
<⟩→ d ⟨f,E(cid:101)∞ (·−Sτ)⟩ (5.17)
√
for all f ∈C+(R), where Sτ =logZτ/ 2. Hence, along τ,
c
E[eJ
t
4 ]→E[e−⟨f,E(cid:101)∞(·−Sτ)⟩].
But, since θ ∈Dom (Π) and Ji → P 0 for i=1,2,3, along τ,
λ t
E[eJ
t
4 ]→E[e−⟨f,Π⟩].
This implies that
Π= d E(cid:101)∞ (·−Sτ). (5.18)

| 28  | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
d
Since the law of Π does not depend on the sequence τ, it follows that Sτ = S for
| some [−∞,∞)-valued |     |     | random | variable      | S   | for all sequences | τ,  | and |        |
| ------------------ | --- | --- | ------ | ------------- | --- | ----------------- | --- | --- | ------ |
|                    |     |     |        | Π=E(cid:101)∞ | d   | (·−S).            |     |     | (5.19) |
Furthermore, this implies that all subsequential limits Zτ of Y have the same
t
√
| law as Z | :=e | 2S, which | implies | that |     |     |     |     |     |
| -------- | --- | --------- | ------- | ---- | --- | --- | --- | --- | --- |
d
|     |     |     |     | Y t →Z |     | as t→∞. |     |     | (5.20) |
| --- | --- | --- | --- | ------ | --- | ------- | --- | --- | ------ |
√
Proof of Theorem 1.2 and Theorem 1.5 for λ= 2. Theorem 1.2 has already been
proved by by (5.19). Also, for θ ∈ Dom (Π), it satisfies (A1), (A2), (A3) by
λ
| Proposition | 3.2, | Proposition |     | 3.1, Proposition |     | 5.1, | and (5.20). |     |     |
| ----------- | ---- | ----------- | --- | ---------------- | --- | ---- | ----------- | --- | --- |
Conversely, if θ satisfies (A1), (A2), (A3), it can be seen from the proofs above
Ji P
that → 0 for 1 ≤ i ≤ 3 still holds. Furthermore, since (A3) gives (5.20), it
| t   |     |     |     |     |     |     |     | √   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
< d
follows from Proposition 2.17 that θ → E(cid:101)∞ (·−S) with S = logZ/ 2. Hence
t
|        |       |         | d                  |            |     |         |     |     | □   |
| ------ | ----- | ------- | ------------------ | ---------- | --- | ------- | --- | --- | --- |
| θ ∈Dom | λ (Π) | with Π= | E(cid:101)∞ (·−S). |            |     |         |     |     |     |
|        |       |         | Some               | Additional |     | Remarks |     |     |     |
6.
6.1. A remark on the finite intensity assumption in [Theorem 2.1-[Kab12]].
In the setting of fixed points of BBM, Theorem 2.1 of [Kab12] states that if Π
√
is a fixed point of BBM with drift λ > 2 having locally finite intensity, then
Π = d E(cid:101)λ(·−S) with a shift S satisfying E[eµS] < ∞. To validate our main result
∞
Theorem 1.2, we show in an a priori manner that the assumption of locally finite
| intensity | forces | Π to have | a   | finite top | particle | almost | surely. |     |     |
| --------- | ------ | --------- | --- | ---------- | -------- | ------ | ------- | --- | --- |
√
Proposition 6.1. Let Π be a fixed point of BBM with drift λ> 2 such that
|     |     | E[Π(K)]<∞ |     |     | for all | compact | sets K ⊂R. |     | (6.1) |
| --- | --- | --------- | --- | --- | ------- | ------- | ---------- | --- | ----- |
Then,
|                |     |            |     | E[Π([0,∞))]<∞. |         |     |     |     | (6.2) |
| -------------- | --- | ---------- | --- | -------------- | ------- | --- | --- | --- | ----- |
| In particular, |     | Π([0,∞))<∞ |     | almost         | surely. |     |     |     |       |
|                | θλ  |            |     |                |         | θλ  |     |     |       |
Proof. Let be given by (1.1) started from =Π. Then, since Π is a fixed point,
|     | t   |     |     |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
θλ(K) d
= Π(K) for all compact sets K and for all t > 0. Also, since Π satisfies
t
(6.1), E[θλ(K)]=E[Π(K)]. Byconditioning on Π andusing the many-to-one lemma
t
| (Lemma | 2.6), for | n≥1, |     |     |     |     |     |     |     |
| ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
(cid:90)
|     | λ[n,n+1] | (cid:12)    | etP(x+B |     |                     |     |     |     |     |
| --- | -------- | ----------- | ------- | --- | ------------------- | --- | --- | --- | --- |
| E[θ |          | (cid:12)Π]= |         |     | t −λt∈[n,n+1])Π(dx) |     |     |     |     |
t
R
(cid:90) (cid:90)
|     |     |     |     | n+1 | et                           |     |     |     |       |
| --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ----- |
|     |     |     | =   |     | √ exp{−(y+λt−x)2/2t}dyΠ(dx). |     |     |     | (6.3) |
2πt
|     |     |     | R   | n   |     |     |     | √   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
√
Let η = 1. Then, for sufficiently large t such that eη t−η/ t≥α>1, we can
λ
| write, for | all n≥0, |          |              |     |          |                         |     |     |     |
| ---------- | -------- | -------- | ------------ | --- | -------- | ----------------------- | --- | --- | --- |
|            |          | (cid:90) | (cid:90) n+1 | et  | (cid:26) | (y+1+λ(t−η)−x)2(cid:27) |     |     |     |
(cid:12)
| E[θλ[n,n+1] | (cid:12)Π]= |     |     | √   | exp − |     |     | dyΠ(dx) |     |
| ----------- | ----------- | --- | --- | --- | ----- | --- | --- | ------- | --- |
| t           |             |     |     |     |       |     | 2t  |         |     |
|             |             | R   | n   | 2πt |       |     |     |         |     |
√
|     |     |     |     | (cid:90) (cid:90) | n+2 | et−η | (cid:26) (y+λ(t−η)−x)2(cid:27) |     |     |
| --- | --- | --- | --- | ----------------- | --- | ---- | ------------------------------ | --- | --- |
t−η
|     |     | ≥eη    | √         |       |             |         | exp − |        | dyΠ(dx) |
| --- | --- | ------ | --------- | ----- | ----------- | ------- | ----- | ------ | ------- |
|     |     |        | t         |       | (cid:112)   |         |       | 2(t−η) |         |
|     |     |        |           | R n+1 |             | 2π(t−η) |       |        |         |
|     |     | ≥αE[θλ |           |       | (cid:12)    |         |       |        |         |
|     |     |        | [n+1,n+2] |       | (cid:12)Π], |         |       |        |         |
t−η

|     | LOCALLY | FINITE | FIXED | POINTS | OF BRANCHING |     | BROWNIAN | MOTION | 29  |
| --- | ------- | ------ | ----- | ------ | ------------ | --- | -------- | ------ | --- |
where we used (6.3) once again in the last line. Taking expectation on both sides
| above, | it follows | that |     |     |     |     |     |     |     |
| ------ | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     | E[Π([n+1,n+2])]≤ |     |     | E[Π([n,n+1])], |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | -------------- | --- | --- | --- |
α
| which | by  | iteration | implies |     |     |     |     |     |     |
| ----- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
E[Π([n,n+1])]≲α−nE[Π([0,1])].
| Since | α>1, | the right-hand |     | side | is summable, | which | implies | (6.2). |     |
| ----- | ---- | -------------- | --- | ---- | ------------ | ----- | ------- | ------ | --- |
□
6.2. A discussion on Tauberian theorems. The condition (A3) appearing in
√
Theorem 1.5 for λ = 2 was further simplified in [CGS24] using a probabilistic
versionoftheHardy-Littlewood-Karamata(HLK)Tauberiantheorem,see[Section5-
[CGS24]]fordetails, andalsosee[BW23]wheresuchaprobabilisticHLKTauberian
theorem appears as well in the context of Weyl’s law in Liouville quantum gravity.
It is then natural to ask if it is possible to simplify/convert the condition (H3)
√
appearing in Theorem 1.5 for λ> 2 into a simpler statement about θ. It can be
easily shown using the same arguments as in section 4.4 that in the presence of
|     |     | (cid:82) 0 |     | 2   | 2   |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
tightness of Z := √1 e(1−λ )teλxe−x tθ(dx), (H3) can be equivalently stated as
|     |     | t − | ∞ t | 2   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:90) 0 1
|     |     |     |     | e(1−λ | 2 )teλxe−x | 2         | d   |     |       |
| --- | --- | --- | --- | ----- | ---------- | --------- | --- | --- | ----- |
|     |     |     | Z = | √     | 2          | 2 tθ(dx)→ |     | Z.  | (6.4) |
|     |     |     | t   | t     |            |           |     |     |       |
−∞
√
|     |          | θˆ(A)=θ(−A), |     |       | (cid:82) x | e−λyθˆ(dy) |       |                      |     |
| --- | -------- | ------------ | --- | ----- | ---------- | ---------- | ----- | -------------------- | --- |
| By  | defining |              |     | G(x)= |            |            | and δ | =1/2t, the condition |     |
0
| (6.4) | can be | recast into | the | form     |            |     |     |     |       |
| ----- | ------ | ----------- | --- | -------- | ---------- | --- | --- | --- | ----- |
|       |        |             |     | (cid:90) | ∞          |     |     |     |       |
|       |        |             |     | δleb/δ   | e−δxdG(x)→ |     | d   |     |       |
|       |        |             |     |          |            |     | X,  |     | (6.5) |
0
as δ →0+, where G is a random monotonic increasing function, l=1/2, b is some
√
negativeconstant(sinceλ> 2)andX issomerandomvariable. Then, simplifying
condition (H3) is equivalent to converting (6.5) into an asymptotic statement about
function G(x) as x→+∞. This is a natural problem in Tauberian theory. In the
√
critical case λ= 2 (which gives b=0 in (6.5)), such an attempt falls exactly in
the framework of HLK Tauberian theorem. In this case, the decay of the Laplace
transform of G is of polynomial type rather than of exponential type in (6.5). One
can hence rely on the theory of regularly varying functions, which is the framework √
ofHLKTauberiantheorem,see[Section5-[CGS24]]fordetails. However,forλ> 2
(which gives b < 0 in (6.5)), without assuming any additional assumption on the
function G, (6.5) cannot be always converted into an asymptotic statement about
G(x) as x → ∞. A counterexample is provided below. However, there are some
related results in that direction, e.g. Kohlbecker’s, Cadena’s, Kosugi’s, Kasahara’s,
de Bruijn’s Tauberian theorems, see [Chapter 4.12-[BGT87]] and [Cad15, Kos99].
In particular, when G is deterministic, Kohlbecker’s Tauberian theorem can be used
√
| to conclude |     | from (6.5) | that | logG(x)∼2 | −bx. |     |     |     |     |
| ----------- | --- | ---------- | ---- | --------- | ---- | --- | --- | --- | --- |
12
| 6.2.1. | A counterexample |     | to  | exponential | type | Tauberian | equivalence. |     |     |
| ------ | ---------------- | --- | --- | ----------- | ---- | --------- | ------------ | --- | --- |
We consider a special case of (6.5) with b=−1 and any l∈R. Let G:[0,∞)→
| [0,∞) | be a | deterministic | monotonic |     | increasing | function | satisfying |     |     |
| ----- | ---- | ------------- | --------- | --- | ---------- | -------- | ---------- | --- | --- |
√
(cid:90) ∞
2 π
|     |     |     |     | e−δxdG(x)∼ |     | δ−le1/δ. |     |     | (6.6) |
| --- | --- | --- | --- | ---------- | --- | -------- | --- | --- | ----- |
3
0
12This counterexample was suggested in an interaction with ChatGPT (OpenAI), and the
calculationsweresubsequentlyverifiedbytheauthors.

30 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
√
There is a particular choice of function G=G given by G (x)= 1xl/2−1/4e2 x
0 0 3
which satisfies (6.6). Hence, if (6.6) is equivalent to an asymptotic statement about
function G, then any such G must satisfy G(x) ∼ G (x) as x → ∞. However,
0
following is an example ofG=G whichsatisfies (6.6), butG (x) is notasymptotic
1 1
to G (x).
0
For l∈R, let
∞
γ =
3l
−
1
, q
=mγe2m3/2
, µ=
(cid:88)
q δ , G (x)=µ[0,x].
2 4 m m m3 1
m=1
Then, G satisfies (6.6). However, note that since q /q →0 exponentially
1 m−1 m √
fast, G (m3) ∼ q . This in turn implies that G (m3)/G (m3) ∼ 3 m. On the
1 m 1 0
other hand, for y = (m+1)3−1, we again have G (y ) ∼ q . But, it can be
m 1 m m
easily seen that q /G (y )→0. We conclude that
m 0 m
G (x) G (x)
limsup 1 =+∞, and liminf 1 =0.
x→∞ G 0 (x) x→∞ G 0 (x)
Hence, G is not asymptotic to G .
1 0
7. Appendix
ForaPoissonpointprocessPPP(η(x)dx)andanotherindependentpointprocess
D, we will use the notation DPPP(η(x)dx,D) to denote the decorated Poisson
√
point process obtained from these. For ρ ≥ 2, let Eρ = DPPP(Ce−ρxdx,Dρ),
where C is a constant and Dρ is as in (2.41). A direct computation gives that
(cid:18) (cid:90) ∞ (cid:19)
E[e−⟨f,Eρ⟩]=exp
−C
E[1−e−(cid:82)f(y+z)Dρ(dz)]e−ρydy
, (7.1)
−∞
for every f ∈C+(R) or of the form (2.1).
c
√
7.1. Identification of the fixed point (for λ> 2).
√
Recall that E(cid:101)
∞
λ is the large
time limit of the BBM flow with supercritical drift λ> 2 starting from the initial
√
distribution PPP(√1 e−µxdx), with µ = λ+ λ2−2 (see Section 1.2). Now we
2π
determinetheexactstructureofE(cid:101)λ,andalsomotivatewhythisparticularchoiceofµ
∞
isessential. Theapproachisinspiredby[LS87]and[Kab12]. ConsidertheBBMflow
θλ with the initial distribution θ =PPP(η(x)dx) and we study the corresponding
t 0
θλ ast→∞. Oneimportantobservationisthatforsomeappropriatelychosenη(x),
t
the intensity of θλ is time invariant, that is for all f of the form (2.1) 13,
t
E[⟨f,θλ⟩]=E[⟨f,θ⟩], ∀t≥0. (7.2)
t
To find such a suitable intensity measure η(x)dx, setting v(t,x):=E [⟨f,θλ⟩], (7.2)
x t
implies
∂v
=0. (7.3)
∂t
Using the many to one formula (Lemma 2.6), we have
(cid:90)
v(t,x)= etE[f(x+B −λt)]η(x)dx. (7.4)
t
R
Moreover, ω(t,x):=E[f(x+B −λt)] satisfies
t
∂ω 1∂2ω ∂ω
= −λ . (7.5)
∂t 2∂x2 ∂x
13Itsufficestoconsideronlythisclassoftestfunctionsasaposteriori,therightchoiceofη
impliesPPP(η(x)dx)∈N2 (seeSection2.1).

|     | LOCALLY | FINITE |     | FIXED POINTS |     | OF BRANCHING | BROWNIAN | MOTION | 31  |
| --- | ------- | ------ | --- | ------------ | --- | ------------ | -------- | ------ | --- |
Combining these and using integration by parts, we get that η(x) satisfies the
| following | ODE: |     |     |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |     |     | η′′+λη′+η | =0. |     |     | (7.6) |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | ----- |
2
√
| For   | λ> 2, | the above | ODE | has          | the following | two          | fundamental | solutions: |     |
| ----- | ----- | --------- | --- | ------------ | ------------- | ------------ | ----------- | ---------- | --- |
|       |       |           |     | η (x)=e−µ1x, |               | η (x)=e−µ2x, |             |            |     |
|       |       |           |     | 1            |               | 2            |             |            |     |
|       |       | √         |     |              | √             |              |             |            |     |
| where | µ =λ− | λ2−2,     |     | µ =λ+        | λ2−2.         |              |             |            |     |
|       | 1     |           |     | 2            |               |              |             |            |     |
ensurethattheintensityofθλ
| Itturnsoutthatbothchoicesofη |     |     |     |     |     |     |     | istime-invariant. |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |
t
In [LS87], the authors showed that if we start from PPP(e−µ1xdx), θλ converges
t
in distribution to the empty point process, that is, the Laplace functional of θλ
t
converges to 1 as t→∞. They also conjectured that starting from PPP(e−µ2xdx),
θλ converges in distribution to a nontrivial limit. Kabluchko showed that this
t
conjectureistrueandthelimitingpointprocessisadecoratedPoissonpointprocess
[Kab12]. We now identify the exact structure of the limiting point process in the
| following | proposition. |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|           |              |     |     | √   |     | √   |     |     |     |
Proposition 7.1. For λ> 2, let µ=λ+ λ2−2, θ =PPP(√1 e−µxdx), then
0
2π
as t→∞,
|     |     |     |     |     | θλ  | ⇒E(cid:101) λ, |     |     | (7.7) |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ----- |
|     |     |     |     |     | t   | ∞              |     |     |       |
where the convergence is in the sense of vague convergence on the space of all point
| configurations. |     | Furthermore |            |          |     |                   |     |     |       |
| --------------- | --- | ----------- | ---------- | -------- | --- | ----------------- | --- | --- | ----- |
|                 |     |             | λ          |          |     | (α(λ))e−µxdx,Dµ), |     |     |       |
|                 |     |             | E(cid:101) | =DPPP(µC |     |                   |     |     | (7.8) |
|                 |     |             | ∞          |          |     | M                 |     |     |       |
Dµ(·)
where C M (·) is as in (2.18) and is a decoration point process with the law
n(t)
|     |     | P(Dµ |      |     | (cid:88) |              |      |         |       |
| --- | --- | ---- | ---- | --- | -------- | ------------ | ---- | ------- | ----- |
|     |     |      | ∈·)= | lim | P(       | δ {χk(t)−Mt} | ∈·|M | t ≥µt). | (7.9) |
t→∞
k=1
The rest of this section is devoted to proving this proposition. Recall that
| {χi} |     |     |     |     |     |     |     | ni(t) |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
i∈N is a family of i.i.d. BBMs starting from the origin, counts the number
of particles of the i-th BBM alive at time t, and {χi(t)} are their locations.
|     |     |     |     |     |     |     | k   | k≤ni(t) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
For f as in (2.1) and supp(f)⊂[−K ,∞), for some K >0, consider the Laplace
|           |     |         |     |     | f   |     | f   |     |     |
| --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| transform |     | of θλ : |     |     |     |     |     |     |     |
t
|     | E[e−⟨f,θ | λ⟩]=E[e−(cid:80)∞ |          | (cid:80)n | i( t)f(xi+χi     | (t)−λt)] |              |                 |          |
| --- | -------- | ----------------- | -------- | --------- | ---------------- | -------- | ------------ | --------------- | -------- |
|     |          | t                 |          | i=1 k=    | 1                | k        |              |                 |          |
|     |          |                   | (cid:18) |           | (cid:90)         |          |              |                 | (cid:19) |
|     |          |                   |          | 1         | (1−E[e−(cid:80)n |          | i( t)f(xi+χi |                 |          |
|     |          | =exp              |          | −√        |                  |          |              | (t)−λt)])e−µxdx |          |
|     |          |                   |          |           |                  | k=       | 1            | k               |          |
2π
|     |     |     | (cid:18) | 1   | (cid:90) ∞ |     |     | (cid:19) |     |
| --- | --- | --- | -------- | --- | ---------- | --- | --- | -------- | --- |
(t,λt−x)e−µxdx
|     |     | =exp |     | −√  | u   |     |     | ,   | (7.10) |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | ------ |
|     |     |      |     | 2π  |     | ϕ   |     |     |        |
−∞
whereu isthesolutionoftheF-KPPequationwithinitialdatau(0,x)=1−e−f(−x),
ϕ
and f is of the form (2.1). Thus, our objective is reduced to understanding the
(cid:82)∞
| limiting | behaviour |     | of  | u (t,λt−x)e−µxdx |     | as  | t tends | to ∞. |     |
| -------- | --------- | --- | --- | ---------------- | --- | --- | ------- | ----- | --- |
|          |           |     | −∞  | ϕ                |     |     |         |       |     |
Towards this goal, we prove the next lemma, which states that for the initial
PPP(√1
distribution θ = e−µxdx), only the BBMs starting from the region
|     |     | 0   |     | 2π  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
around −(µ−λ)t meaningfully contribute in large times. For brevity, we prove this
for the initial distribution PPP(e−µxdx), and it is straightforward to notice that
the statement of the following lemma does not change if one considers the initial
| distribution |     | PPP(Ce−µxdx), |     | for | any C | >0. |     |     |     |
| ------------ | --- | ------------- | --- | --- | ----- | --- | --- | --- | --- |

32 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
Lemma 7.2. Let (p ) be the atoms of a Poisson point process P with intensity
i i∈I
measure e−µxdx. For any choice of z ∈R and ϵ>0, there exist t >0,δ >0 such
0
that for all t>t ,
0
(cid:18) √ √ (cid:19)
P ∃i∈N,k ≤ni(t):p +χi(t)−λt≥z,p ∈/ [−(µ−λ)t−δ t,−(µ−λ)t+δ t] ≤ϵ.
i k i
(7.11)
√
Proof. We first consider the case when p >−(µ−λ)t+δ t. By union bounds and
i
Campbell’s formula, we have
(cid:18) √ (cid:19)
P ∃i∈N,k ≤ni(t):p +χi(t)−λt≥z,p >−(µ−λ)t+δ t
i k i
(cid:20) (cid:21)
(cid:88)
≤E P(p +M −λt≥z)
i t (7.12)
√
pi>−(µ−λ)t+δ t
(cid:90) ∞
= P(M ≥λt−x+z)e−µxdx.
√ t
−(µ−λ)t+δ t
We use the many to one lemma (Lemma 2.6) to bound the probability inside the
integral and split it into two parts:
(cid:90) ∞
P(M ≥λt−x+z)e−µxdx
√ t
−(µ−λ)t+δ t
(cid:90) ∞
≤ etP(B ≥λt−x+z)e−µxdx
√ t
−(µ−λ)t+δ t
(cid:90) 0 (cid:90) ∞
= etP(B ≥λt−x+z)e−µxdx+ etP(B ≥λt−x+z)e−µxdx
√ t t
−(µ−λ)t+δ t 0
=(I)+(II).
(7.13)
By standard Gaussian Mills ratio argument, we get
(cid:90) 0
(I)= etP(B ≥λt−x+z)e−µxdx
√ t
−(µ−λ)t+δ t
√ (7.14)
≲ (cid:90) (µ−λ)t−δ t √ et eµxe−(z+x 2 + t λt)2 dx.
2πt
0
√
where we do a change of variables x→−x. Observe that since µ= λ+ λ2−2,
we can find a constant c >0 depending on z such that for t large enough,
1
√
(cid:90) (µ−λ)t−δ t
√
et eµxe−(z+x
2
+
t
λt)2
dx
2πt
0
√
≤c 1 (cid:90) (µ−λ)t−δ t √ 1 e−(x−(µ 2 − t λ)t)2 dx (7.15)
2πt
0
=c 1 (cid:90) −δ √ √ 1 2π e−u 2 2 du.
−(µ−λ) t
As for the second term, direct calculation gives that
(II)= (cid:90) ∞ √ et e−µxdx (cid:90) ∞ e−[u+(z− 2 x t +λt)]2 du
2πt
0 0 (7.16)
=e(1−λ 2 2 )t (cid:90) ∞ e−(µ−λ)xdx (cid:90) ∞ √ 1 e−[u+(z 2 − t x)]2 e−λu−λzdu.
2πt
0 0

LOCALLY FINITE FIXED POINTS OF BRANCHING BROWNIAN MOTION 33
Notethat (cid:82)∞ e−(µ−λ)xdx (cid:82)∞ √1 e−[u+(z 2 − t x)]2 e−λu−λzduisfiniteasµ>λ;therefore,
0 0 2πt
one can find a constant c depending on z such that the above is bounded by
2
c 2 e(1−λ 2 2 )t. By a similar computation used to prove the bound on (I), we get
(cid:18) √ (cid:19) (cid:90) ∞
P ∃i∈I,k ≤ni(t):p i +χi k (t)−λt≥z,p i <−(µ−λ)t−δ t ≤c 3 e−u 2 2 du.
δ
(7.17)
Therefore
(cid:18) √ √ (cid:19)
P ∃i∈N,k ≤ni(t):p +χi(t)−λt≥z,p ∈/ [−(µ−λ)t−δ t,−(µ−λ)t+δ t]
i k i
≤c 1 (cid:90) −δ √ √ 1 2π e−u 2 2 du+c 2 e(1−λ 2 2 )t+c 3 (cid:90) ∞ e−u 2 2 du,
−(µ−λ) t δ
which concludes the proof of this lemma once we choose δ,t sufficiently large. □
0
Proof of Proposition 7.1. Lemma 7.2 suggests that we should focus on the region
√ √
[−(µ−λ)t−δ t,−(µ−λ)t+δ t]. Now we want to understand if we start from
the initial distribution PPP(√1 e−µxdx) restricted to the region [−(µ−λ)t−
√ √ 2π
δ t,−(µ−λ)t+δ t], where does θλ converge to. To this end, we require the
t
followinglemma,whichdescribestheasymptoticbehaviouroftheLaplacetransform
of the BBM with drift, conditioned on the event that the maximum is unusually
large. We use a similar approach as in [[BH14]-Corollary 7.6] to prove this.
Lemma 7.3. For any fixed δ >0 and f of the form 2.1 with supp(f)⊂[−K ,∞),
√ √ f
for some K >0, uniformly in x∈[−(µ−λ)t−δ t,−(µ−λ)t+δ t], we have
f
lim E[1−e−(cid:80)n i= (t 1 )f(xi+χi k (t)−λt)|x+M t −λt≥−K f ]
t→∞
(cid:90) ∞ (7.18)
=
µE[1−e−(cid:82)f(y+z)Dµ(dz)]e−µye−µKfdy.
−∞
We postpone the proof of this lemma until the end of this section. By Lemma
√ √
2.9, for every fixed δ >0, uniformly in x∈[−(µ−λ)t−δ t,−(µ−λ)t+δ t],
u M (t,λt+x)t2 1eλxex 2 2 te(λ 2 2 −1)t →C M (α(λ)), t→∞. (7.19)
By Lemma 7.3 and (7.19),
√
(cid:90) −(µ−λ)t+δ t
u (t,λt−x)e−µxdx
√ ϕ
−(µ−λ)t−δ t
√
(cid:90) −(µ−λ)t+δ t
= √ E[1−e−(cid:80)n i= (t 1 )f(xi+χi k (t)−λt)|x+M t −λt≥−K f ]
−(µ−λ)t−δ t
(7.20)
×P(x+M −λt≥−K )e−µxdx
t f
√
(cid:90) −(µ−λ)t+δ t
= √ E[1−e−(cid:80)n i= (t 1 )f(xi+χi k (t)−λt)|x+M t −λt≥−K f ]
−(µ−λ)t−δ t
×u (t,λt−x−K )e−µxdx.
M f

34 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
First taking t→∞ and then δ →∞, from (7.18) and (7.19), we get
√
1 (cid:90) −(µ−λ)t+δ t
lim lim √ u (t,λt−x)e−µxdx
δ→∞t→∞ 2π
−(µ−λ)t−δ
√
t
ϕ
(cid:90) ∞
=µC (α(λ))
E[1−e−(cid:82)f(y+z)Dµ(dz)]e−µydy
M
−∞ √ (7.21)
× lim lim
(cid:90) −(µ−λ)t+δ t
√
1 e−[x+(µ
2
−
t
λ)t]2
dx
δ→∞t→∞
−(µ−λ)t−δ
√
t
2πt
(cid:90) ∞
=µC (α(λ))
E[1−e−(cid:82)f(y+z)Dµ(dz)]e−µydy.
M
−∞
Our last step is to show that first letting t→∞, and then δ →∞,
(cid:90)
u (t,λt−x)e−µxdx→0.
√ √ ϕ
x∈[−(µ−λ)t−δ t,−(µ−λ)t+δ t]c
Observe that
(cid:90)
u (t,λt−x)e−µxdx
√ ϕ
x>−(µ−λ)t+δ t
(7.22)
(cid:90)
≤ P(x+M >λt−K )e−µxdx,
√ t f
x>−(µ−λ)t+δ t
which is what we have estimated in (7.12). Therefore
(cid:90)
lim lim u (t,λt−x)e−µxdx=0. (7.23)
δ→∞t→∞
x>−(µ−λ)t+δ
√
t
ϕ
Similarly, we get
(cid:90)
lim lim u (t,λt−x)e−µxdx=0. (7.24)
δ→∞t→∞
x<−(µ−λ)t−δ
√
t
ϕ
Putting these together, we have
lim √ 1 (cid:90) ∞ u (t,λt+x)eµxdx=µC (α(λ)) (cid:90) ∞ E[1−e−(cid:82)f(y+z)Dµ(dz)]e−µydy.
ϕ M
t→∞ 2π
−∞ −∞
(7.25)
√ √
By Lemma 7.3, uniformly in x∈[−(µ−λ)t−δ t,−(µ−λ)t+δ t],
E[1−e−(cid:80)n
i=
(t
1
)f(xi+χi
k
(t)−λt)]
lim
t→∞ P(x+M t −λt≥−K f )
= lim E[1−e−(cid:80)n i= (t 1 )f(xi+χi k (t)−λt)|x+M t −λt≥−K f ] (7.26)
t→∞
(cid:90) ∞
=
µE[1−e−(cid:82)f(y+z)Dµ(dz)]e−µye−µKfdy.
−∞
Rewriting this in terms of the solution of the F-KPP equation gives
lim u ϕ (t,λt−x) = (cid:90) ∞ µE[1−e−(cid:82)f(y+z)Dµ(dz)]e−µye−µKfdy. (7.27)
t→∞u
M
(t,λt−x−K
f
)
−∞
√ √
Applying Lemma 2.9 again, uniformly in x∈[−(µ−λ)t−δ t,−(µ−λ)t+δ t],
u (t,λt−x) C(f,α(λ))
lim ϕ = . (7.28)
t→∞u
M
(t,λt−x−K
f
) C
M
(α(λ))eµKf
Combining (7.27) and (7.28), we get
(cid:90) ∞
µC (α(λ))
E[1−e−(cid:82)f(y+z)Dµ(dz)]e−µydy
=C(f,α(λ)). (7.29)
M
−∞

|       | LOCALLY |        | FINITE | FIXED   | POINTS    | OF           | BRANCHING     | BROWNIAN | MOTION | 35     |
| ----- | ------- | ------ | ------ | ------- | --------- | ------------ | ------------- | -------- | ------ | ------ |
| Using | (7.10), | (7.25) | and    | (7.29), |           |              |               |          |        |        |
|       |         |        |        |         | (cid:104) | λ⟩ (cid:105) |               |          |        |        |
|       |         |        |        | lim     | E e−⟨f,θ  | t            | =e−C(f,α(λ)). |          |        | (7.30) |
t→∞
| On  | the other | hand, | from | (7.1) | we               | know             |     |     |     |        |
| --- | --------- | ----- | ---- | ----- | ---------------- | ---------------- | --- | --- | --- | ------ |
|     |           |       |      |       | (cid:104)        | (cid:105)        |     |     |     |        |
|     |           |       |      |       | e−⟨f,E(cid:101)∞ | λ⟩ =e−C(f,α(λ)). |     |     |     |        |
|     |           |       |      |       | E                |                  |     |     |     | (7.31) |
This means
|     |     |     |     |     | (cid:104) | λ⟩ (cid:105) | (cid:104)           | λ⟩ (cid:105) |     |        |
| --- | --- | --- | --- | --- | --------- | ------------ | ------------------- | ------------ | --- | ------ |
|     |     |     |     | lim | E e−⟨f,θ  | t            | =E e−⟨f,E(cid:101)∞ | ,            |     | (7.32) |
t→∞
□
| which | concludes |     | the proof. |     |     |     |     |     |     |     |
| ----- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Proof of Lemma 7.3. Let us denote D = (cid:80)n(t)δ . By Corollary 7.6 in
|     |     |     |     |     |     | t   | k=1√χk(t)−Mt |     | √   |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
[BH14],wegetthat,uniformlyinx∈[−(µ−λ)t−δ t,−(µ−λ)t+δ t],conditioned
ontheevent{x+M −λt≥−K },thepair(D ,x+M −λt+K )jointlyconverges
|     |     |     | t   |     | f   |     | t   | t   | f   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to an independent pair (D,e), where e=exp(µ) (exponential random variable with
| rate | µ), and | D   | is defined | as  |     |     |     |     |     |     |
| ---- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|      |         |     |            |    |     |     |     |     |    |     |
n(t)
(cid:88)
|     | P(D | ∈·):= | l   | im P | δ        |     | ∈·|x+M | −λt≥−K | f. | (7.33) |
| --- | --- | ----- | --- | ----- | -------- | --- | ------ | ------ | --- | ------ |
|     |     |       |     |       | χk(t)−Mt |     |        | t      |     |        |
t → ∞
k=1
Moreover, Proposition 7.5 in [BH14] tells that the above limit does not depend on
| the | particular | values |     | of δ and | K . | Therefore, | (7.33) | is the | same as |     |
| --- | ---------- | ------ | --- | -------- | --- | ---------- | ------ | ------ | ------- | --- |
f
|     |     |     |     |     |    |     |     |     |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n(t)
(cid:88)
|     |     | P(D | ∈·)= | l   | im P | δ        | ∈·|M | −µt≥0, |     | (7.34) |
| --- | --- | --- | ---- | --- | ----- | -------- | ---- | ------- | --- | ------ |
|     |     |     |      |     |       | χk(t)−Mt |      | t       |     |        |
t → ∞
k=1
d
| which | gives | D = | Dµ.             | Therefore |             |               |     |        |     |     |
| ----- | ----- | --- | --------------- | --------- | ----------- | ------------- | --- | ------ | --- | --- |
|       |       |     | E[1−e−(cid:80)n |           | (t )f(xi+χi |               |     |        |     |     |
|       |       |     | lim             |           | i= 1        | k (t)−λt)|x+M |     | −λt≥−K | ]   |     |
|       |       |     |                 |           |             |               |     | t      | f   |     |
t→∞
E[1−e−(cid:82)f(x+Mt−λt+z)Dt(dz)|x+M
|     |     | =   | lim |     |     |     |     | −λt≥−K | ]   | (7.35) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ |
|     |     |     |     |     |     |     |     | t      | f   |        |
t→∞
=E[1−e−(cid:82)f(e−Kf+z)D(dz)].
Since e and D are independent and D has the same distribution as Dµ, we get
|     |     |     | E[1−e−(cid:80)n |     | (t )f(xi+χi |     |             |        |     |     |
| --- | --- | --- | --------------- | --- | ----------- | --- | ----------- | ------ | --- | --- |
|     |     |     | lim             |     |             |     | (t)−λt)|x+M | −λt≥−K | ]   |     |
|     |     |     |                 |     | i= 1        | k   |             | t      | f   |     |
t→∞
(cid:90)
∞ µE[1−e−(cid:82)f(x−Kf+z)Dµ(dz)]e−µxdx
=
(7.36)
0
|     |     |     | (cid:90) ∞ |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
µE[1−e−(cid:82)f(y+z)Dµ(dz)]e−µye−µKfdy.
=
−Kf
Finally, the domain of the integration above can be extended to the whole real
line because f is supported on [−K ,∞) and Dµ is supported on (−∞,0]. This
f
□
| completes |     | the proof. |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
√
7.2. Intensity measure of E(cid:101)λ for λ> 2. It was proven in [CHL19] that for the
|          |          |     |       |         | ∞           |                  |     |           |                 | √   |
| -------- | -------- | --- | ----- | ------- | ----------- | ---------------- | --- | --------- | --------------- | --- |
|          |          |     |       |         |             |                  |     |           | E[D([x,0])]∼Ce− | 2x  |
| critical | extremal |     | point | process | E(cid:101)∞ | , the decoration | D   | satisfies |                 |     |
as x→−∞ for some constant C >0. Together with (2.36), this easily implies that
E(cid:101)∞ has infinite intensity, i.e. E[E(cid:101)∞ ([−K,K])] = +∞ for all K > 0. On the other
hand, the supercritical extremal point process E(cid:101)λ has a finite intensity given as
∞
follows.

| 36  | XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |                                               | √   |     |     | √   |     |     |     |
Proposition 7.4. Let λ> 2 and µ=λ+ λ2−2. Then, for every f ∈C+(R),
c
(cid:90)
|     |     | (cid:2)         | (cid:3) | 1   |             |     |     |        |
| --- | --- | --------------- | ------- | --- | ----------- | --- | --- | ------ |
|     |     | E ⟨f,E(cid:101) | λ⟩ =    | √   | f(x)e−µxdx. |     |     | (7.37) |
∞
2π R
To prove this proposition, we use the following lemma, which gives an alternate
E(cid:101)λ,
representation of the Laplace transform for that may also be of independent
∞
interest.
∈C+(R),
| Lemma | 7.5. For every | f   |     |     |     |     |     |     |
| ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
c
| (cid:2) e−⟨f,E(cid:101)∞ | λ⟩(cid:3) |     |     |     |     |     |     |     |
| ------------------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
E
|      | (cid:40) (cid:34) |                   |     |     |                    |                    |     | (cid:35)(cid:41) |
| ---- | ----------------- | ----------------- | --- | --- | ------------------ | ------------------ | --- | ---------------- |
|      | 1                 | (cid:90)          |     |     | (cid:90) ∞(cid:90) |                    |     |                  |
|      |                   | (1−e−f(x))e−µxdx− |     |     |                    | u2(s,λs−x)e−µxdxds |     |                  |
| =exp | − √               |                   |     |     |                    |                    |     | ,                |
|      | 2π                |                   |     |     |                    | ϕ                  |     |                  |
|      |                   | R                 |     |     | 0                  | R                  |     |                  |
(7.38)
| where u | is the solution | to the | F-KPP | equation | with | the initial | condition |     |
| ------- | --------------- | ------ | ----- | -------- | ---- | ----------- | --------- | --- |
ϕ
(0,x)=1−e−f(−x).
u
ϕ
|          |            | θλ     |           |       |         |      | √1        | e−µxdx, |
| -------- | ---------- | ------ | --------- | ----- | ------- | ---- | --------- | ------- |
| Proof of | Lemma 7.5. | Let be | a Poisson | point | process | with | intensity |         |
|          |            | 0      |           |       |         |      |           | 2π      |
|          | θλ         |        |           |       |         |      | θλ        |         |
and let be the corresponding BBM flow with drift λ started from (see (1.1)).
|        | t                  |         |          |         |       |          | 0        |     |
| ------ | ------------------ | ------- | -------- | ------- | ----- | -------- | -------- | --- |
| By the | Laplace functional | formula | of       | Poisson | point | process, | we have  |     |
|        |                    |         | (cid:26) |         |       |          | (cid:27) |     |
1 (cid:90)
|     | E (cid:2) e−⟨f,θ | λ⟩(cid:3) =exp | −√  |     | u (t,λt−x)e−µxdx |     | .   |     |
| --- | ---------------- | -------------- | --- | --- | ---------------- | --- | --- | --- |
|     |                  | t              |     |     | ϕ                |     |     |     |
2π
R
| Recall, | by Lemma 2.4, |                          |     |     |                     |     |     |     |
| ------- | ------------- | ------------------------ | --- | --- | ------------------- | --- | --- | --- |
|         |               | (t,λt−x)=1−E[e−(cid:80)n |     |     | (t )f(x+χk(t)−λt)]. |     |     |     |
|         |               | u                        |     |     | k= 1                |     |     |     |
ϕ
Define the family of maps {π } parametrized by t and acting on space of all
t t≥0
| bounded | measurable | functions           | as  |     |        |     |     |        |
| ------- | ---------- | ------------------- | --- | --- | ------ | --- | --- | ------ |
|         |            | (π g)(x):=etE[g(x+B |     |     | −λt)]. |     |     | (7.39) |
|         |            | t                   |     |     | t      |     |     |        |
Using the strong Markov property at the first branching time and the branching
| property, | we obtain |     |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
(cid:90)
|     |              |             |     |     | t   | (cid:0)    | (cid:1) |        |
| --- | ------------ | ----------- | --- | --- | --- | ---------- | ------- | ------ |
|     | u (t,λt−x)=π | (1−e−f(x))− |     |     | π   | u2(s,λs−x) | ds.     | (7.40) |
|     | ϕ            | t           |     |     | t−s | ϕ          |         |        |
0
| By (7.2), | for all g ∈C+(R), |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
c
|     |     | (cid:90)        |     | (cid:90) |             |     |     |        |
| --- | --- | --------------- | --- | -------- | ----------- | --- | --- | ------ |
|     |     | π (g(x))e−µxdx= |     |          | g(x)e−µxdx. |     |     | (7.41) |
t
|             |                   | R      |     |                  | R            |     |     |     |
| ----------- | ----------------- | ------ | --- | ---------------- | ------------ | --- | --- | --- |
| Integrating | (7.40) against    | e−µxdx | and | using            | (7.41) gives |     |     |     |
|             | (cid:90)          |        |     | (cid:90)         |              |     |     |     |
|             | u (t,λt−x)e−µxdx= |        |     | (1−e−f(x))e−µxdx |              |     |     |     |
ϕ
|     | R   |     |     | R   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(7.42)
(cid:90) t(cid:90)
u2(s,λs−x)e−µxdxds.
−
ϕ
|     |     |     |     | 0   | R   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Finally, by Proposition 7.1, θλ converges in distribution to E(cid:101)λ. Letting t→∞ in
|            |           | t              |     |     |     |     | ∞   |     |
| ---------- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
| both sides | of (7.42) | yields (7.38). |     |     |     |     |     | □   |
Proof of Proposition 7.4. By Fatou’s lemma and the invariance of the first moment
| for θλ (that | is (7.2)),      | for every                    | f ∈C+(R), |     |     |             |     |        |
| ------------ | --------------- | ---------------------------- | --------- | --- | --- | ----------- | --- | ------ |
| t            |                 |                              | c         |     |     |             |     |        |
|              |                 |                              |           |     | 1   | (cid:90)    |     |        |
|              | (cid:2)         | λ⟩ (cid:3) ≤liminfE[⟨f,θλ⟩]= |           |     |     | f(x)e−µxdx. |     |        |
|              | E ⟨f,E(cid:101) |                              |           |     | √   |             |     | (7.43) |
|              |                 | ∞ t→∞                        |           | t   | 2π  |             |     |        |
R

|     | LOCALLY |     | FINITE | FIXED | POINTS | OF  | BRANCHING | BROWNIAN MOTION | 37  |
| --- | ------- | --- | ------ | ----- | ------ | --- | --------- | --------------- | --- |
It remains to prove the reverse inequality. Applying Lemma 7.5 with εf in place of
| f and   | using            | Jensen’s | inequality       |           | gives |         |           |                    |          |
| ------- | ---------------- | -------- | ---------------- | --------- | ----- | ------- | --------- | ------------------ | -------- |
|         |                  |          | (cid:18)(cid:90) | 1−e−εf(x) |       |         | 1(cid:90) | ∞(cid:90)          | (cid:19) |
| (cid:2) |                  | (cid:3)  | 1                |           |       |         |           |                    |          |
| E       | ⟨f,E(cid:101) λ⟩ | ≥ √      |                  |           |       | e−µxdx− |           | u2(s,λs−x)e−µxdxds | .        |
|         | ∞                |          |                  |           | ε     |         | ε         | ε                  |          |
|         |                  |          | 2π               | R         |       |         | 0         | R                  |          |
Here we use u to denote the solution of the F-KPP equation with initial condition
ε
u (0,x)=1−e−εf(−x). ThefirstterminsidethebracketoftheRHSaboveconverges
ε (cid:82)
| to  | f(x)e−µxdx |     | by dominated |     | convergence |     | as ϵ↓0. | We claim that |     |
| --- | ---------- | --- | ------------ | --- | ----------- | --- | ------- | ------------- | --- |
R
1(cid:90) ∞(cid:90)
|     |     |     | lim |     | u2(s,λs−x)e−µxdxds=0. |     |     |     | (7.44) |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ------ |
|     |     |     |     | ε   |                       | ε   |     |     |        |
|     |     |     | ε↓0 | 0   | R                     |     |     |     |        |
Using the many to one lemma (Lemma 2.6) together with the simple inequality
| 1−e−x     | ≤x  | for x≥0, |      |     |                        |     |     |       |        |
| --------- | --- | -------- | ---- | --- | ---------------------- | --- | --- | ----- | ------ |
|           |     |          |      | u   | (s,λs−x)≤1∧επ          |     |     | f(x). | (7.45) |
|           |     |          |      |     | ε                      |     | s   |       |        |
| Moreover, |     | if suppf | ⊂[−K | ,K  | ], then                |     |     |       |        |
|           |     |          |      | f   | f                      |     |     |       |        |
|           |     |          |      |     | π f(x)≤Ce(1−λ2/2)seλx. |     |     |       |        |
s
√
| Since | λ>  | 2 and | 2λ>µ,     | we          | have |     |     |     |     |
| ----- | --- | ----- | --------- | ----------- | ---- | --- | --- | --- | --- |
|       |     |       | 1(cid:90) | ∞(cid:90) 0 |      |     |     |     |     |
u2(s,λs−x)e−µxdxds
|     |     |     | ε   |            | ε          |          |                 |     |        |
| --- | --- | --- | --- | ---------- | ---------- | -------- | --------------- | --- | ------ |
|     |     |     | 0   | −∞         |            |          |                 |     | (7.46) |
|     |     |     |     | (cid:90) ∞ |            | (cid:90) | 0               |     |        |
|     |     |     |     |            | e(2−λ2)sds |          | e(2λ−µ)xdx−−→0. |     |        |
≤Cε
ε↓0
|     |               |     |       | 0      |        |     | −∞        |     |     |
| --- | ------------- | --- | ----- | ------ | ------ | --- | --------- | --- | --- |
| For | the remaining |     | part, | we use | u2 ≤επ | f   | to obtain |     |     |
|     |               |     |       |        | ε      | s   |           |     |     |
1
|     |     |     |     | u2(s,λs−x)e−µx |     |     | ≤e(1−λ2/2)se−(µ−λ)x. |     |     |
| --- | --- | --- | --- | -------------- | --- | --- | -------------------- | --- | --- |
0≤
|     |     |     |     | ε ε |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
√
Thus, for all ε > 0, 1u2(s,λs−x)e−µx is integrable in R ×R as λ > 2 and
|     | √   |     | ε   | ε   |     |     |     | + + |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1u2(s,λs−x)e−µx
| µ−λ  | =          | λ2−2 | > 0.          | By (7.45), |             |     |         | converges pointwise | to 0 as |
| ---- | ---------- | ---- | ------------- | ---------- | ----------- | --- | ------- | ------------------- | ------- |
|      |            |      |               |            |             | ε ε |         |                     |         |
| ε↓0. | Therefore, |      | the dominated |            | convergence |     | theorem | gives               |         |
|      |            |      | 1(cid:90)     | ∞(cid:90)  | ∞           |     |         |                     |         |
u2(s,λs−x)e−µxdxds−−→0.
(7.47)
|           |     |        | ε    |                 | ε          |         |            | ε↓0 |     |
| --------- | --- | ------ | ---- | --------------- | ---------- | ------- | ---------- | --- | --- |
|           |     |        |      | 0               | 0          |         |            |     |     |
| Combining |     | (7.46) | with | (7.47),         | we get     | (7.44). | Therefore  |     |     |
|           |     |        |      |                 |            | 1       | (cid:90)   |     |     |
|           |     |        |      | (cid:2)         | λ⟩ (cid:3) |         | f(x)e−µxdx |     |     |
|           |     |        |      | E ⟨f,E(cid:101) |            | ≥ √     |            |     |     |
|           |     |        |      |                 | ∞          | 2π      |            |     |     |
R
| which | concludes |     | the proof. |     |     |     |     |     | □   |
| ----- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
References
[ABBS13] E.Aïdékon, J.Berestycki, É. Brunet, andZ.Shi. BranchingBrownianmotionseen
|     | fromitstip. |     | Probab. | Theory | Related |     | Fields,157(1-2):405–451,2013. |     |     |
| --- | ----------- | --- | ------- | ------ | ------- | --- | ----------------------------- | --- | --- |
[ABK13] Louis-Pierre Arguin, Anton Bovier, and Nicola Kistler. The extremal process of
|     | branchingBrownianmotion. |     |     |     | Probab. |     | Theory Related | Fields,157(3-4):535–574,2013. |     |
| --- | ------------------------ | --- | --- | --- | ------- | --- | -------------- | ----------------------------- | --- |
[BGT87] N. H. Bingham, C. M. Goldie, and J. L. Teugels. Regular variation, volume 27
|     | of  | Encyclopedia |     | of Mathematics |     | and | its Applications. | Cambridge University | Press, |
| --- | --- | ------------ | --- | -------------- | --- | --- | ----------------- | -------------------- | ------ |
Cambridge,1987.
[BH14] AntonBovierandLisaHartung. Theextremalprocessoftwo-speedbranchingbrownian
|     | motion. |     | Electron. | J. Probab,19(18):1–28,2014. |     |     |     |     |     |
| --- | ------- | --- | --------- | --------------------------- | --- | --- | --- | --- | --- |
[BH15] AntonBovierandLisaHartung. Variablespeedbranchingbrownianmotion1. extremal
|     | processesintheweakcorrelationregime. |     |     |     |     |     | ALEA,12(1):261–291,2015. |     |     |
| --- | ------------------------------------ | --- | --- | --- | --- | --- | ------------------------ | --- | --- |
[BL16] MarekBiskupandOrenLouidor. Extremelocalextremaoftwo-dimensionaldiscrete
|     | Gaussianfreefield. |     |     | Comm. | Math. | Phys.,345(1):271–304,2016. |     |     |     |
| --- | ------------------ | --- | --- | ----- | ----- | -------------------------- | --- | --- | --- |
[BM21] MohamedAliBelloumandBastienMallein. Anomalousspreadinginreduciblemultitype
|     | branchingbrownianmotion. |     |     |     | Electronic |     | Journal | of Probability,26(61):39–p,2021. |     |
| --- | ------------------------ | --- | --- | --- | ---------- | --- | ------- | -------------------------------- | --- |

38 XINXINCHEN,ARNABCHOWDHURY,ATULSHEKHAR,SHUOZHU
[Bov17] Anton Bovier. Gaussian processes on trees, volume 163 of Cambridge Studies in
| Advanced | Mathematics. |     | Cambridge | University | Press, | Cambridge, | 2017. From | spin |
| -------- | ------------ | --- | --------- | ---------- | ------ | ---------- | ---------- | ---- |
glassestobranchingBrownianmotion.
[Bra78] Maury D. Bramson. Maximaldisplacementofbranching Brownian motion. Comm.
| Pure | Appl. Math.,31(5):531–581,1978. |     |     |     |     |     |     |     |
| ---- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[Bra83] MauryBramson. ConvergenceofsolutionsoftheKolmogorovequationtotravelling
| waves. | Mem. | Amer. | Math. Soc.,44(285):iv+190,1983. |     |     |     |     |     |
| ------ | ---- | ----- | ------------------------------- | --- | --- | --- | --- | --- |
[BW23] Nathanaël Berestycki and Mo Dick Wong. Weyl’s law in liouville quantum gravity.
| arXiv | preprint | arXiv:2307.05407,2023. |     |     |     |     |     |     |
| ----- | -------- | ---------------------- | --- | --- | --- | --- | --- | --- |
[Cad15] MeitnerCadena. AnoteonTauberiantheoremsofexponentialtype. Int. J. Math.
Comput. Sci.,10(2):105–114,2015.
[CGS21] XinxinChen,ChristopheGarban,andAtulShekhar. AnewproofofLiggett’stheorem
| fornon-interactingBrownianmotions. |     |     |     |     | Electron. Commun. | Probab.,26:PaperNo. |     | 72, |
| ---------------------------------- | --- | --- | --- | --- | ----------------- | ------------------- | --- | --- |
12,2021.
[CGS23] Xinxin Chen, Christophe Garban, and Atul Shekhar. The fixed points of branching
| Brownianmotion. |     | Probab. | Theory | Related | Fields,185(3-4):839–884,2023. |     |     |     |
| --------------- | --- | ------- | ------ | ------- | ----------------------------- | --- | --- | --- |
[CGS24] XinxinChen,ChristopheGarban,andAtulShekhar. Domainofattractionofthefixed
| pointsofbranchingBrownianmotion. |     |     |     |     | Ann. Appl. | Probab.,34(6):5351–5387,2024. |     |     |
| -------------------------------- | --- | --- | --- | --- | ---------- | ----------------------------- | --- | --- |
[CHL19] AserCortines,LisaHartung,andOrenLouidor. Thestructureofextremelevelsetsin
| branchingBrownianmotion. |     |     | Ann. | Probab.,47(4):2257–2302,2019. |     |     |     |     |
| ------------------------ | --- | --- | ---- | ----------------------------- | --- | --- | --- | --- |
[Fel71] William Feller. An introduction to probability theory and its applications. Vol. II.
JohnWiley&Sons,Inc.,NewYork-London-Sydney,secondedition,1971.
[HR17] SimonC. HarrisandMatthewI. Roberts. Themany-to-fewlemmaandmultiplespines.
| Ann. | Inst. Henri | Poincaré | Probab. | Stat.,53(1):226–242,2017. |     |     |     |     |
| ---- | ----------- | -------- | ------- | ------------------------- | --- | --- | --- | --- |
[INW68a] NobuyukiIkeda,MasaoNagasawa,andShinzoWatanabe. BranchingMarkovprocesses.
| I.  | J. Math. | Kyoto Univ.,8:233–278,1968. |     |     |     |     |     |     |
| --- | -------- | --------------------------- | --- | --- | --- | --- | --- | --- |
[INW68b] NobuyukiIkeda,MasaoNagasawa,andShinzoWatanabe. BranchingMarkovprocesses.
| II. | J. Math. | Kyoto | Univ.,8:365–410,1968. |     |     |     |     |     |
| --- | -------- | ----- | --------------------- | --- | --- | --- | --- | --- |
[INW69] NobuyukiIkeda,MasaoNagasawa,andShinzoWatanabe. BranchingMarkovprocesses.
| III. | J. Math. | Kyoto | Univ.,9:95–160,1969. |     |     |     |     |     |
| ---- | -------- | ----- | -------------------- | --- | --- | --- | --- | --- |
[Kab12] ZakharKabluchko. Persistenceandequilibriaofbranchingpopulationswithexponential
| intensity. | J.  | Appl. Probab.,49(1):226–244,2012. |     |     |     |     |     |     |
| ---------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
[Kos99] Nobuko Kosugi. Tauberian theorem of exponential type on limits of oscillation. J.
| Math. | Kyoto | Univ.,39(4):783–792,1999. |     |     |     |     |     |     |
| ----- | ----- | ------------------------- | --- | --- | --- | --- | --- | --- |
[Lig78] ThomasM. Liggett. RandominvariantmeasuresforMarkovchains,andindependent
| particlesystems. |     | Z.  | Wahrsch. | Verw. | Gebiete,45(4):297–313,1978. |     |     |     |
| ---------------- | --- | --- | -------- | ----- | --------------------------- | --- | --- | --- |
[LS87] S.P. LalleyandT.Sellke. Aconditionallimittheoremforthefrontierofabranching
| Brownianmotion. |     | Ann. | Probab.,15(3):1052–1061,1987. |     |     |     |     |     |
| --------------- | --- | ---- | ----------------------------- | --- | --- | --- | --- | --- |
[McK75] H. P. McKean. Application of Brownian motion to the equation of Kolmogorov-
| Petrovskii-Piskunov. |     |     | Comm. Pure | Appl. | Math.,28(3):323–331,1975. |     |     |     |
| -------------------- | --- | --- | ---------- | ----- | ------------------------- | --- | --- | --- |
[Sko64] A. V. Skorohod. Branching diffusion processes. Teor. Verojatnost. i Primenen.,
9:492–497,1964.
|     | Beijing | Normal | University, |     | School | of Mathematical | Sciences, |     |
| --- | ------- | ------ | ----------- | --- | ------ | --------------- | --------- | --- |
(XinxinChen)
China
Email address: xinxin.chen@bnu.edu.cn
(ArnabChowdhury) Tata Institute of Fundamental Research-CAM, Bangalore,
India
Email address: arnab2020@tifrbng.res.in
(Atul Shekhar) Tata Institute of Fundamental Research-CAM, Bangalore,
India
Email address: atul@tifrbng.res.in
|     | Beijing | Normal | University, |     | School | of Mathematical | Sciences, |     |
| --- | ------- | ------ | ----------- | --- | ------ | --------------- | --------- | --- |
(Shuo Zhu)
China
Email address: zhushuo@mail.bnu.edu.cn
---- END DOCUMENT ----
