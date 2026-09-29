Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
1
Exact Common Information and Exact
Channel Synthesis for Correlated Gaussian
Sources
Lei Yu
Abstract
In this paper, we resolve two conjectures posed by Yu and Tan in 2020 (in two separate
papers published in the IEEE Trans. Inf. Theory). Specifically, we establish that: 1) the exact
common information for a pair of ρ-correlated Gaussian sources is given by the conjectured
expression 1log 1+ρ+ ρ ;and2)theadmissibleregionforthesharedrandomnessrateandthe
2 1−ρ 1+ρ
communicationrateinexactchannelsynthesisisexactlytheconjecturedone.Theseresultsyield
twoimportantconsequences.First,foranyρ>0,theexactcommoninformationofacorrelated
Gaussian pair strictly exceeds Wyner’s common information. Second, for ρ > 0, the exact
channel synthesis of such a pair requires strictly higher rates than the total-variation version.
Theproofcombinesanexactoptimal-transportrepresentationoftheworst-caseGaussiancross-
entropy, Fathi’s Gaussian transport inequality, and a determinant inequality arising from the
covariance structure of the conditional means.
Index Terms
Gaussian sources, Exact common information, Exact channel synthesis, Communication
complexity, Transport inequality
I. INTRODUCTION
A. Common information
The common information problem asks for the minimum amount of common randomness
needed to generate two correlated random variables at two separate terminals. In Wyner’s
formulation [1], Wyner considered approximate generation in relative entropy and obtained the
common information
C (X;Y) = inf I(X,Y;W).
Wyner
W:X−W−Y
The exact common information problem, introduced by Kumar, Li, and El Gamal [2], is
different. Here the synthesized distribution must equal the target distribution exactly, rather
than merely approach it asymptotically in a weak metric. The common random variable is first
L. Yu is with the School of Statistics and Data Science, LPMC, KLMDASR, and LEBPS, Nankai University,
Tianjin 300071, China (e-mail: leiyu@nankai.edu.cn). This work was supported by the National Key Research and
Development Program of China under grant 2023YFA1009604 and the NSFC under grant 62101286.
6202
guA
62
]TI.sc[
1v21062.8062:viXra

2
generatedandthenindependentlyprocessedatthetwoterminals.Theexactcommoninformation
| is the minimum | asymptotic | rate | of this common | randomness. |     |     |     |     |
| -------------- | ---------- | ---- | -------------- | ----------- | --- | --- | --- | --- |
Let π be a probability distribution on a standard Borel product space. At blocklength n,
XY
an exact synthesis code consists of a discrete random variable W and conditional distributions
| P Xn|W ,P | Yn|W , such | that |     |     |     |     |     |     |
| --------- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
(cid:88)
|     |     | P =  | P (w)P |        | P      |     | = π⊗n, |     |
| --- | --- | ---- | ------ | ------ | ------ | --- | ------ | --- |
|     |     | XnYn | W      | Xn|W=w | Yn|W=w |     | XY     |     |
w
Xn−W −Yn
| where the | conditional | independence | relation |     |     | holds. |     |     |
| --------- | ----------- | ------------ | -------- | --- | --- | ------ | --- | --- |
The exact common information is the asymptotic normalized entropy of the smallest such
commonrandom variable.Thevariable-length formulation isequivalentbecause foraprefix-free
code,H(W) ≤ L(W) < H(W)+1,andthereforethedifferenceisnegligibleafternormalization
by n. Accordingly,
|     |       |            | 1 (cid:8) |     |      |        | −Yn(cid:9) |       |
| --- | ----- | ---------- | --------- | --- | ---- | ------ | ---------- | ----- |
|     | C     | (π ) = lim | inf H(W)  | : P |      | = π⊗n, | Xn−W       | . (1) |
|     | Exact | XY         |           |     | XnYn | XY     |            |       |
|     |       | n→∞        | n         |     |      |        |            |       |
A natural interpretation of exact common information can be described via the following
thought experiment. Consider a random particle (or planet) that, at a certain instant, decomposes
into multiple components. These components inherit shared common randomness and then
evolve independently, governed jointly by this common randomness as well as their respective
individual randomness. After some time has elapsed, given the observed joint distribution of
the components, one may wish to estimate the amount of common randomness they possess.
Or conversely, given the quantity of common randomness shared among them, we aim to
characterize the set of feasible joint distributions these components can attain. This is exactly
| the common | information | problem. |     |     |     |     |     |     |
| ---------- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
The exact common information is no smaller than Wyner’s common information. However,
unlike Wyner’s common information, the single-letter characterization of exact common infor-
mation is rarely known, except for doubly symmetric binary sources (DSBSes) [3] and a certain
class of sources satisfying C = C [2], [4], [3]. As for Gaussian sources, the exact
|        |             | Exact             | Wyner |     |     |     |     |     |
| ------ | ----------- | ----------------- | ----- | --- | --- | --- | --- | --- |
| common | information | is still unknown. |       |     |     |     |     |     |
In addition, Yu and Tan [5], [6], [3] introduced the notion of Re´nyi common information,
whichisdefinedastheminimum common ratewhenthetherelativeentropyisreplacedbymore
generaldivergences—thefamilyofRe´nyidivergences.ThefamilyofRe´nyicommoninformation
unifies Wyner’s common information and exact common information since it includes them as
| two special    | cases   | with the Re´nyi | order equal | to 1 | or ∞. |     |     |     |
| -------------- | ------- | --------------- | ----------- | ---- | ----- | --- | --- | --- |
| B. Distributed | channel | synthesis       |             |      |       |     |     |     |
Common information has natural applications in distributed channel synthesis [7], [8], [9],
[10], [11]. The latter problem, illustrated in Fig. 2, refers to the problem of determining the
|     |     |     |     |     |     |     | {(Xn,Yn)} | Xn  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- |
minimum communication rate required to generate a bivariate source with
n∈N
Yn
generated at the encoder and generated at the decoder such that the induced joint distribution
P approximately or exactly equals π⊗n for all n ∈ N. In this paper, we focus on the exact
| XnYn |     |     | XY  |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |

3
Xn (cid:45)
P
(cid:0)(cid:18) Xn|W
(cid:0)
|     |     |     |     | W   | (cid:0) |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
(cid:64)
(cid:64)
|     |     |     |     |     | (cid:64)(cid:82) |     | Yn (cid:45) |     |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --- | --- | --- |
P
Yn|W
| Fig. 1. Distributed | source | synthesis. |     |     |     |     |     |     |     |     |
| ------------------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
synthesis, equivalently, requiring P = π⊗n. When there is no shared randomness, the exact
|     |     |     |     | XnYn |     | XY  |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
channel synthesis problem reduces to the exact common information problem.
Consider the distributed source simulation setup depicted in Fig. 2. A sender and a receiver
share a uniformly distributed source of randomness1 K ∼ Unif(K),K := [enR 0]. The sender
π⊗n
has access to a memoryless source Xn ∼ that is independent of K , and wants to transmit
|     |     |     |     |     | X   |     |         |     | n   |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
|     |     |     |     |     |     |     | (Xn,Yn) |     | π⊗n |     |
information about the correlation between correlated sources ∼ to the receiver.
XY
Given the shared randomness and the correlation information from the sender, the receiver
π⊗n
generates a memoryless source Yn ∼ (·|Xn). Specifically, given Xn and K, the sender
Y|X
generates a “message” (i.e., a discrete random variable) M by a random mapping P M|XnK , and
then sends it to the receiver error free. Upon accessing to K and receiving M, the receiver
generates a source Yn by a random mapping P . The joint distribution induced by this
Yn|MK
code is
|     |     |     | P      |     | := P | P P  | P           | .   |     |     |
| --- | --- | --- | ------ | --- | ---- | ---- | ----------- | --- | --- | --- |
|     |     |     | XnKMYn |     |      | Xn K | M|XnK Yn|MK |     |     |     |
Now we would like to determine the minimum amount of communication such that P =
XnYn
| π⊗n               |     | P     |     | = π⊗n |     |     |     |     |     |     |
| ----------------- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- |
| (or equivalently, |     | Yn|Xn |     |       | ).  |     |     |     |     |     |
| XY                |     |       |     | Y|X   |     |     |     |     |     |     |
Definition 1. The admissible region of shared randomness rate and communication rate for the
| exact channel | synthesis |     | problem | is defined |     | as  |     |     |     |     |
| ------------- | --------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
|               |           | R   | (π      | )          |     |     |     |     |     |     |
Exact XY
|     |     |     |          |    |         |      |           |        |    |     |
| --- | --- | --- | -------- | --- | ------- | ---- | --------- | ------ | --- | --- |
|     |     |     |          | (R  | 0 ,R) : | ∃(P  | ,P        | ) s.t. |     |     |
|     |     |     | (cid:91) |    |         | M| X | n K Yn|MK |        |    |     |
|     |     |     |          |     | P       | = π  | ⊗ n ,     |        |     |     |
|     |     | =   | cl       |     | Yn|Xn   |      |           |        | .   | (2) |
Y|X
|     |     |     |     |    | R ≥ | 1H(M|K) |     |     |    |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
n≥1
n
Incontrasttoexactchannelsynthesis,totalvariation(TV)-approximatesynthesisonlyrequires
the TV distance between the empirical distribution P and the target distribution πn to
|     |     |     |     |     |     |     | XnYn |     |     | XY  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
vanish asymptotically. Early studies by Bennett et al. [7] and Winter [8] investigated exact and
TV-approximate channel synthesis under the assumption of unlimited shared encoder–decoder
randomness,provingthattheminimalasymptoticcommunicationrateforbothsynthesisschemes
equals the mutual information I(X;Y) of the target distribution (X,Y) ∼ π XY .
| 1For simplicity, | we  | assume | that enR0 | is integers. |     |     |     |     |     |     |
| ---------------- | --- | ------ | --------- | ------------ | --- | --- | --- | --- | --- | --- |

4
Unif[enR
|               |         | K ∼        | 0]       |          |     |          |          |     |            |
| ------------- | ------- | ---------- | -------- | -------- | --- | -------- | -------- | --- | ---------- |
|               |         |            |          | (cid:63) |     |          | (cid:63) |     |            |
|               |         | Xn π⊗n     |          |          |     |          |          | Yn  | π⊗n (·|Xn) |
|               |         | ∼          | (cid:45) |          | M   | (cid:45) |          |     | (cid:45) ∼ |
|               |         | X          | P        |          |     | P        |          |     | Y|X        |
|               |         |            | M|XnK    |          |     |          | Yn|MK    |     |            |
| Fig. 2. Exact | channel | synthesis. |          |          |     |          |          |     |            |
Subsequent research explored the fundamental tradeoff between communication rate and
shared randomness rate in TV-approximate synthesis. Cuff [9] and Bennett et al. [10] char-
acterized this rate tradeoff, while Harsha et al. [11] adopted a rejection sampling framework to
analyze one-shot exact synthesis for discrete sources, establishing a bounded shared randomness
cost with a mild increment in expected description length. Li and El Gamal [12] further refined
the finite shared randomness upper bound for discrete settings with a negligible communication
rate penalty.
Most prior work focused on TV-approximate synthesis or exact synthesis under extreme
randomness conditions, except for [13]. Yu and Tan [13] fully characterized the optimal tradeoff
between shared randomness rate and communication rate for exact synthesis of the doubly
symmetric binary source (DSBS), and verified that exact synthesis requires a strictly higher
communication rate than its TV-approximate counterpart. This is the first example for which the
| optimal rate    | tradeoff      | is explicitly      | known.   |     |              |          |     |     |     |
| --------------- | ------------- | ------------------ | -------- | --- | ------------ | -------- | --- | --- | --- |
| C. The Gaussian |               | setting            |          |     |              |          |     |     |     |
| Consider        | the           | standard bivariate | Gaussian |     | distribution |          |     |     |     |
|                 |               |                    |          | π   | = N(0,Σ      | ),       |     |     |     |
|                 |               |                    |          | ρ   |              | ρ        |     |     |     |
| where 0         | ≤ ρ <         | 1 and              |          |     |              |          |     |     |     |
|                 |               |                    |          |     | (cid:18)     | (cid:19) |     |     |     |
|                 |               |                    |          |     | 1            | ρ        |     |     |     |
|                 |               |                    |          | Σ   | ρ =          | .        |     |     |     |
|                 |               |                    |          |     | ρ            | 1        |     |     |     |
| For this        | distribution, | Wyner’s            | common   |     | information  | is       |     |     |     |
1 1+ρ
|     |     |     | C   |       | (π ) = | ln  | .   |     |     |
| --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- |
|     |     |     |     | Wyner | ρ      |     |     |     |     |
2 1−ρ
| Indeed, it | is achieved | by the      | Gaussian | decomposition |     |        |     |        |     |
| ---------- | ----------- | ----------- | -------- | ------------- | --- | ------ | --- | ------ | --- |
|            |             | W ∼ N(0,ρ), |          | X             | = W | +N X , | Y   | = W +N | Y , |
where
|     |     |     |     | N ,N | ∼ N(0,1−ρ) |     |     |     |     |
| --- | --- | --- | --- | ---- | ---------- | --- | --- | --- | --- |
|     |     |     |     | X    | Y          |     |     |     |     |
W.
| are independent |     | of each other | and | of  |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |

5
As already mentioned, the exact common information is always at least Wyner’s common
| information. | Yu and | Tan [3] | proved | the   | upper bound |     |     |     |     |     |
| ------------ | ------ | ------- | ------ | ----- | ----------- | --- | --- | --- | --- | --- |
|              |        |         |        |       | 1           | 1+ρ | ρ   |     |     |     |
|              |        |         | C      | (π    | ) ≤ ln      |     | +   | .   |     | (3) |
|              |        |         |        | Exact | ρ           |     |     |     |     |     |
|              |        |         |        |       | 2           | 1−ρ | 1+ρ |     |     |     |
They also proved that the exact common information equals the ∞-Re´nyi common information
| for this   | Gaussian source. | They      | conjectured |       | this   | upper | bound | is tight. |     |     |
| ---------- | ---------------- | --------- | ----------- | ----- | ------ | ----- | ----- | --------- | --- | --- |
| Conjecture | 1 ([3]).         | For every | 0           | ≤ ρ < | 1,     |       |       |           |     |     |
|            |                  |           |             |       | 1      | 1+ρ   | ρ     |           |     |     |
|            |                  |           | C           | (π    | ) = ln |       | +     | .         |     |     |
|            |                  |           |             | Exact | ρ 2    | 1−ρ   | 1+ρ   |           |     |     |
ρ
The importance of this question is that the second term is strictly positive whenever
1+ρ
ρ > 0. Hence the conjecture would show that exact synthesis requires strictly more common
| randomness | than Wyner’s |     | approximate |     | synthesis | in the | Gaussian | setting. |     |     |
| ---------- | ------------ | --- | ----------- | --- | --------- | ------ | -------- | -------- | --- | --- |
As for exact channel synthesis of Gaussian distributions, Yu and Tan [13] proved the inner
bound
|     |     |     |     | R     | (π  | ) ⊇ R(π | ),  |     |     | (4) |
| --- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- | --- |
|     |     |     |     | Exact | ρ   |         | ρ   |     |     |     |
where
|                  |         |       |       |           | [ρ2,1],αβ |                     | ρ2,       |              |    |     |
| ---------------- | ------- | ------ | ----- | --------- | --------- | ------------------- | --------- | ------------ | --- | --- |
|                  |         |        | (R,R  | ) :       | α ∈       |                     | =         |              |     |     |
|                  |         |       |       | 0         |           |                     |           |              |    |     |
|                  |         |      |       |           |           | (cid:104) (cid:105) |           |              |   |     |
|                  |         |        |       | R ≥       | 1 log     | 1                   | ,         |              |     |     |
|                  | R(π )   | :=     |       |           | 2         | 1−α                 |           |              | .   |     |
|                  | ρ       |        |       |           |           |                     |           | √            |     |     |
|                  |         |       |       |           |           | (cid:104)           | (cid:105) |              |    |     |
|                  |         |       | R+R   | ≥         | 1 log     | 1−ρ2                | +         | ρ (1−α)(1−β) |    |     |
|                  |         |       |       | 0         |           |                     |           |              |    |     |
|                  |         |        |       |           | 2         | (1−α)(1−β)          |           | 1−ρ2         |     |     |
| They conjectured | this    | inner  | bound | is tight. |           |                     |           |              |     |     |
| Conjecture       | 2 ([13] | ). For | every | 0 ≤ ρ     | < 1,      |                     |           |              |     |     |
|                  |         |        |       | R         | (π        | ) = R(π             | ).        |              |     |     |
|                  |         |        |       | Exact     | ρ         |                     | ρ         |              |     |     |
| D. Main          | results |        |       |           |           |                     |           |              |     |     |
OurfirstmaincontributionisthefollowinglowerboundonC (π ).Recallπ = N(0,Σ ).
|         |              |     |       |     |         |     |     | Exact ρ | ρ   | ρ   |
| ------- | ------------ | --- | ----- | --- | ------- | --- | --- | ------- | --- | --- |
| Theorem | 1. For every | 0 ≤ | ρ <   | 1,  |         |     |     |         |     |     |
|         |              |     |       |     | 1       | 1+ρ | ρ   |         |     |     |
|         |              |     | C     | (π  | ) ≥ log |     | +   | .       |     |     |
|         |              |     | Exact | ρ   |         |     |     |         |     |     |
|         |              |     |       |     | 2       | 1−ρ | 1+ρ |         |     |     |
CombiningthislowerboundwithYu–Tan’supperboundin(3)confirmConjecture1positively.
| Theorem | 2. For every | 0 ≤ | ρ < | 1,    |        |     |     |     |     |     |
| ------- | ------------ | --- | --- | ----- | ------ | --- | --- | --- | --- | --- |
|         |              |     |     |       | 1      | 1+ρ | ρ   |     |     |     |
|         |              |     | C   | (π    | ) = ln |     | +   | .   |     |     |
|         |              |     |     | Exact | ρ 2    | 1−ρ | 1+ρ |     |     |     |

6
Remark 1. If ρ < 0, replace Y by −Y. Since exact common information is invariant under
deterministic bijections applied separately to either terminal, C Exact (π ρ ) = C Exact (π ). Hence
|ρ|
| the general | scalar  | Gaussian | formula |     | is      |              |          |     |     |
| ----------- | ------- | -------- | ------- | --- | ------- | ------------ | -------- | --- | --- |
|             |         |          |         |     | 1 1+|ρ| | |ρ|          |          |     |     |
|             |         |          | C (π    | ) = | log     | +            | , |ρ| <  | 1.  |     |
|             |         |          | Exact   | ρ   |         |              |          |     |     |
|             |         |          |         |     | 2 1−|ρ| | 1+|ρ|        |          |     |     |
| This        | theorem | states   | that    |     |         |              |          |     |     |
|             |         |          |         |     | =       | CI+exactness | penalty, |     |     |
|             |         |          | exact   | CI  | Wyner   |              |          |     |     |
with
ρ
|     |     | exactness |     | penalty | = C   | (π )−C | (π ) =  | .   |     |
| --- | --- | --------- | --- | ------- | ----- | ------ | ------- | --- | --- |
|     |     |           |     |         | Exact | ρ      | Wyner ρ |     |     |
1+ρ
Thus the exact common information is strictly larger than Wyner’s common information for
| every | ρ > 0. The | gap | satisfies |     |     |     |     |     |     |
| ----- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
|       |            |     |           |     |     | ρ 1 |     |     |     |
|       |            |     |           |     | 0 < | < , |     |     |     |
|       |            |     |           |     | 1+ρ | 2   |     |     |     |
and
|         |            |         |     |     |         | ρ 1     |         |     |     |
| ------- | ---------- | ------- | --- | --- | ------- | ------- | ------- | --- | --- |
|         |            |         |     |     | lim     | = .     |         |     |     |
|         |            |         |     |     | ρ↑1 1+ρ | 2       |         |     |     |
| In bits | per source | symbol, | the | gap | is      |         |         |     |     |
|         |            |         |     | ρ   |         | 1       |         |     |     |
|         |            |         |     |     | log e ≤ | log e ≈ | 0.7213. |     |     |
|         |            |         |     | 1+ρ | 2       | 2 2     |         |     |     |
The proof idea of Theorem 1 can be applied to exact channel synthesis of Gaussian distribu-
| tions,  | leading | to our | second main | contribution. |            |           |      |     |     |
| ------- | ------- | ------ | ----------- | ------------- | ---------- | --------- | ---- | --- | --- |
| Theorem | 3. For  | every  | 0 ≤ ρ       | < 1,          |            |           |      |     |     |
|         |         |        |             |               | R Exact (π | ρ ) ⊆ R(π | ρ ). |     |     |
CombiningthisouterboundwithYu–Tan’sinnerboundin(4)confirmConjecture2positively.
| Theorem | 4. For | every | 0 ≤ ρ | < 1, |       |         |     |     |     |
| ------- | ------ | ----- | ----- | ---- | ----- | ------- | --- | --- | --- |
|         |        |       |       |      | R (π  | ) = R(π | ).  |     | (5) |
|         |        |       |       |      | Exact | ρ       | ρ   |     |     |
|         |        |       |       | II.  | PROOF | THEOREM | 1   |     |     |
OF
| In this | section, | we        | prove Theorem |             | 1 by using | the following | strategy:   |              |     |
| ------- | -------- | --------- | ------------- | ----------- | ---------- | ------------- | ----------- | ------------ | --- |
|         | exact    | synthesis | =⇒            | multiletter | bound      | =⇒ optimal    | transport   |              |     |
|         |          |           | =⇒            | Gaussian    | T          | =⇒ covariance | determinant | extremality. |     |
2
| The case | ρ = | 0 is trivial, | and | thus, | we only | consider ρ | ∈ (0,1). |     |     |
| -------- | --- | ------------- | --- | ----- | ------- | ---------- | -------- | --- | --- |

7
| A.  | A Multi-letter |     | Bound |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Define
|     |     |     |     |     |     | π⊗n | = N(0,Σ⊗n), |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
|     |     |     |     |     |     | ρ   |             | ρ   |     |     |     |
where
|     |     |     |     |     |     |       | (cid:18) | (cid:19) |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | -------- | -------- | --- | --- | --- |
|     |     |     |     |     |     |       | I        | ρI       |     |     |     |
|     |     |     |     |     |     | Σ⊗n = | n        | n        | .   |     |     |
ρ
|     |     |     |     |     |     |     | ρI n | I n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
E[Xn(Yn)T]
Equivalently, Xn ∼ N(0,I ), Yn ∼ N(0,I ),and = ρI . We also use π⊗n to
|        |     |               |     | n        |     |     | n   |     |     | n   | ρ   |
| ------ | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| denote | the | corresponding |     | density. |     |     |     |     |     |     |     |
For two probability measures µ,ν on Rn, let C(µ,ν) denote the set of all couplings of µ and
| ν.  | Define | the maximal |     | Gaussian | cross-entropy |     |          |     |     |     |     |
| --- | ------ | ----------- | --- | -------- | ------------- | --- | -------- | --- | --- | --- | --- |
|     |        |             |     |          |               |     | (cid:90) |     | 1   |     |     |
H(n)(µ,ν)
|     |        |           |        |                    | :=          | sup | Q(dx,dy)log |     |            | .         | (6) |
| --- | ------ | --------- | ------ | ------------------ | ----------- | --- | ----------- | --- | ---------- | --------- | --- |
|     |        |           |        | ρ                  |             |     |             |     | π⊗n(xn,yn) |           |     |
|     |        |           |        |                    | Q∈C(µ,ν)    |     |             |     | ρ          |           |     |
|     | We now | introduce | the    | n-letter           | functional: |     |             |     |            |           |     |
|     |        |           |        | (cid:110)          |             |     |             |     |            | (cid:111) |     |
|     |        | Γ (ρ)     | := inf | −h(Xn|W)−h(Yn|W)+E |             |     |             |     | H(n)(P     | ,P ) ,    |     |
|     |        | n         |        |                    |             |     |             |     | W Xn|W     | Yn|W      | (7) |
ρ
where the infimum is over all discrete W and conditional distributions satisfying P =
XnYn
| π⊗n, | Xn−W | −Yn. |     |     |     |     |     |     |     |     |     |
| ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ρ
|     | Because  | of conditional |                 | independence, |           |     |                  |     |     |     |     |
| --- | -------- | -------------- | --------------- | ------------- | --------- | --- | ---------------- | --- | --- | --- | --- |
|     |          |                |                 | h(Xn,Yn|W)    |           | =   | h(Xn|W)+h(Yn|W). |     |     |     |     |
|     | We first | prove          | the fundamental |               | converse. |     |                  |     |     |     |     |
π⊗n,
Proposition 1. For every exact n-letter synthesis code (W,P Xn|W ,P Yn|W ) for we have
ρ
| H(W) | ≥   | Γ (ρ). | As a | consequence, |     |     |     |     |     |     |     |
| ---- | --- | ------ | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
n
1
|     |        |       |      |       | C     | (π    | ) ≥ limsup |     | Γ (ρ). |     |     |
| --- | ------ | ----- | ---- | ----- | ----- | ----- | ---------- | --- | ------ | --- | --- |
|     |        |       |      |       | Exact | ρ     |            |     | n      |     |     |
|     |        |       |      |       |       |       | n→∞        | n   |        |     |     |
|     | Proof: | Fix w | with | P (w) | > 0.  | Since |            |     |        |     |     |
W
(cid:88)
|     |     |     |     | π⊗n(xn,yn) | =   |     | P (w′)p |       | (xn)p | (yn) |     |
| --- | --- | --- | --- | ---------- | --- | --- | ------- | ----- | ----- | ---- | --- |
|     |     |     |     |            |     |     | W       | Xn|w′ | Yn|w′ |      |     |
ρ
w′
| with | p     | ,p    | denote | the        | densities | of  | P       | ,P    | ,       | we have pointwise |     |
| ---- | ----- | ----- | ------ | ---------- | --------- | --- | ------- | ----- | ------- | ----------------- | --- |
|      | Xn|w′ | Yn|w′ |        |            |           |     | Xn|W=w′ |       | Yn|W=w′ |                   |     |
|      |       |       |        | π⊗n(xn,yn) |           | ≥ P | (w)p    | (xn)p | (yn).   |                   | (8) |
|      |       |       |        | ρ          |           |     | W Xn|w  |       | Yn|w    |                   |     |
Taking logarithms,
1
|     |     | log |     |     | ≤ −logP |     | (w)−logp |      | (xn)−logp | (yn). |     |
| --- | --- | --- | --- | --- | ------- | --- | -------- | ---- | --------- | ----- | --- |
|     |     |     |     |     |         | W   |          | Xn|w |           | Yn|w  |     |
π⊗n(xn,yn)
ρ

8
Let Q ∈ C(P ,P ) be arbitrary. Integrating with respect to Q gives
w Xn|w Yn|w w
(cid:90)
1
Q (dx,dy)log ≤ −logP (w)
w π⊗n(xn,yn) W
ρ
+h(Xn|W = w)+h(Yn|W = w).
Since the inequality holds for every coupling Q ,
w
H(n)(P ,P ) ≤ −logP (w)+h(Xn|w)+h(Yn|w).
ρ Xn|w Yn|w W
Therefore,
−h(Xn|w)−h(Yn|w)+H(n)(P ,P ) ≤ −logP (w).
ρ Xn|w Yn|w W
Averaging over W,
−h(Xn|W)−h(Yn|W)+EH(n)(P ,P ) ≤ H(W).
ρ Xn|W Yn|W
Taking the infimum over all exact decompositions proves H(W) ≥ Γ (ρ).
n
B. Evaluation of the Maximal Gaussian Cross-Entropy
We now evaluate the functional in (7). Fix w, and write
a = E[Xn|W = w], b = E[Yn|W = w],
w w
and
A = Cov(Xn|W = w), B = Cov(Yn|W = w).
w w
Let
µ0 = L(Xn−a |W = w), ν0 = L(Yn−b |W = w).
w w w w
The Gaussian density is
1 (cid:26) |xn|2+|yn|2−2ρ⟨xn,yn⟩ (cid:27)
π⊗n(xn,yn) = exp − ,
ρ (2π)n(1−ρ2)n/2 2(1−ρ2)
where |·| is the Euclidian norm. Hence,
(cid:112)
|xn|2+|yn|2−2ρ⟨xn,yn⟩
−logπ⊗n(xn,yn) = nlog(2π 1−ρ2)+ . (9)
ρ 2(1−ρ2)
Since the marginals of the coupling are fixed, maximizing the cross-entropy is equivalent, for
ρ ≥ 0, to minimizing E⟨Xn,Yn⟩.
Lemma 1 (Optimal transport representation). For every w,
Q∈C(P X i n n |w f ,P Yn|w ) E Q ⟨Xn,Yn⟩ = a w ·b w + 2 1 (cid:2) W 2 2(µ0 w ,−ν w 0)−trA w −trB w (cid:3) . (10)

9
Proof: Under any coupling,
E⟨Xn,Yn⟩ = a ·b +E⟨Xn−a ,Yn−b ⟩
w w w w
1 1 1
= a ·b + E|Xn−a +Yn−b |2− trA − trB .
w w w w w w
2 2 2
Minimizing E⟨Xn,Yn⟩ is therefore equivalent to minimizing E|Xn − a + Yn − b |2. But
w w
Xn−a has law µ0, while −(Yn−b ) has law −ν0. Hence the minimum of E|Xn−a +
w w w w w
Yn−b |2 is W2(µ0,−ν0).
w 2 w w
Combining the lemma with (9) gives the following exact expression.
Proposition 2. For every w,
(cid:112)
H(n)(P ,P ) = nlog(2π 1−ρ2)
ρ Xn|w Yn|w
|a |2+|b |2+(1+ρ)(trA +trB )−2ρa ·b −ρW2(µ0,−ν0)
+ w w w w w w 2 w w . (11)
2(1−ρ2)
C. Fathi’s Gaussian Transport Inequality
We next need to control the Wasserstein term in (11). We use Fathi’s Gaussian T inequality.
2
Lemma 2 (Fathi’s Gaussian transport inequality [14]). Let µ,ν be probability measures on Rn
with finite second moments, and let γ = N(0,I ). If µ is centered, then
n
W2(µ,ν) ≤ 2D(µ∥γ)+2D(ν∥γ).
2
√
More generally, applying the scaling transformation X (cid:55)→ tX to the underlying random
variables for all µ,ν,γ (and hence scaling their distributions accordingly), we obtain
W2(µ,ν) ≤ 2t (cid:2) D(µ∥γ )+D(ν∥γ ) (cid:3) , (12)
2 t t
where γ = N(0,tI ).
t n
This scaling is exactly what we need. We fix temporarily t ∈ (0, 1−ρ2) (and lastly, will choose
ρ
t = 1−ρ). Since µ0 and −ν0 are centered, applying (12) to them yields
w w
W2(µ0,−ν0) ≤ S −2tH +2ktlog(2πt), (13)
2 w w w w
where
S = trA +trB
w w w
and
H = h(Xn|w)+h(Yn|w).
w
Substituting (13) into (11) yields
H(n)(P ,P ) ≥nlog(2π (cid:112) 1−ρ2)+ |a w |2+|b w |2+S w −2ρa w ·b w
ρ Xn|w Yn|w 2(1−ρ2)
ρt ρkt
+ H − log(2πt). (14)
1−ρ2 w 1−ρ2

10
| Consequently, |     | the | contribution |     | of w | to Γ | (ρ), denoted |     | by g, | satisfies |     |     |
| ------------- | --- | --- | ------------ | --- | ---- | ---- | ------------ | --- | ----- | --------- | --- | --- |
n
|     |     |      |           |     |           |     |     | |2+|b | |2+S |      |     |     |
| --- | --- | ---- | --------- | --- | --------- | --- | --- | ----- | ---- | ---- | --- | --- |
|     |     |      |           |     | (cid:112) |     | |a  |       |      | −2ρa | ·b  |     |
|     |     | g(w) | ≥ nlog(2π |     | 1−ρ2)+    |     | w   |       | w    | w    | w w |     |
2(1−ρ2)
|     |     |     |     | (cid:18) |      | (cid:19) |     |      |           |     |     |      |
| --- | --- | --- | --- | -------- | ---- | -------- | --- | ---- | --------- | --- | --- | ---- |
|     |     |     |     |          | ρt   |          |     | ρkt  |           |     |     |      |
|     |     |     | +   | −1+      |      |          | H − |      | log(2πt). |     |     | (15) |
|     |     |     |     |          | 1−ρ2 |          | w   | 1−ρ2 |           |     |     |      |
Since (Xn,Yn) ∼ π⊗n, we have E|Xn|2 = E|Yn|2 = n, and E[Xn·Yn] = nρ. By the law
ρ
of total covariance,
E[A
|     |     |     |     |     | I = |     | ]+Cov(a |     | ),  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | n   |     | W       |     | W   |     |     |     |
and therefore
|     |     |     |     |     | E(cid:2) | trA | +|a | |2(cid:3) = | n.  |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | ----------- | --- | --- | --- | --- |
|     |     |     |     |     |          | W   | W   |             |     |     |     |     |
Similarly,
|     |     |     |     |     | E(cid:2) |     |     | |2(cid:3) |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --------- | --- | --- | --- | --- |
|     |     |     |     |     |          | trB | +|b | =         | n.  |     |     |     |
|     |     |     |     |     |          | W   | W   |           |     |     |     |     |
Finally, conditional independence gives Cov(Xn,Yn) = Cov(a ,b ), so E[a ·b ] = nρ.
|     |     |     |     |     |     |     |     |     |     | W W | W W |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hence,
|           |       |                | E(cid:2) |           |      |          |      |      | (cid:3)  |           |           |      |
| --------- | ----- | -------------- | -------- | --------- | ---- | -------- | ---- | ---- | -------- | --------- | --------- | ---- |
|           |       |                | |a       | |2+|b     | |2+S |          | −2ρa | ·b   | =        | 2k(1−ρ2). |           |      |
|           |       |                |          | W         | W    | W        |      | W    | W        |           |           |      |
| Averaging |       | (15) therefore |          | gives     |      |          |      |      |          |           |           |      |
|           |       |                |          |           |      | (cid:18) |      |      | (cid:19) |           |           |      |
|           |       |                |          | (cid:112) |      |          |      | ρt   |          | ρkt       |           |      |
|           | Γ (ρ) | ≥nlog(2π       |          | 1−ρ2)+n+  |      |          | −1+  |      | EH       | −         | log(2πt). | (16) |
|           | n     |                |          |           |      |          |      |      |          | W         |           |      |
|           |       |                |          |           |      |          |      | 1−ρ2 |          | 1−ρ2      |           |      |
At this point, all source-specific information has been reduced to an upper bound on the
| conditional | entropy |     | EH  | .   |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
W
| D. Entropy | Bound |     | from the | Conditional |     | Covariance |     |     |     |     |     |     |
| ---------- | ----- | --- | -------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Define
|     |     |     |     | U   | = Cov(E[Xn|W]) |     |     | = Cov(a |     | ),  |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | ------- | --- | --- | --- | --- |
W
and
Cov(E[Yn|W])
|     |     |     |     | V   | =   |     |     | = Cov(b |     | ).  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
W
Since Cov(Xn,Yn) = ρI and conditional independence gives Cov(Xn,Yn) = Cov(a ,b ),
|           |       |     |     | n    |       |          |          |     |     |     |     | W W |
| --------- | ----- | --- | --- | ---- | ----- | -------- | -------- | --- | --- | --- | --- | --- |
|           | Cov(a | ,b  | ) = | ρI . |       |          |          |     |     |     |     |     |
| we obtain |       | W   | W   | n    | Thus, |          |          |     |     |     |     |     |
|           |       |     |     |      |       | (cid:18) | (cid:19) |     |     |     |     |     |
|           |       |     |     |      |       | U        | ρI       |     |     |     |     |     |
n
|     |     |     |     |     |     |     |     | ⪰ 0. |     |     |     | (17) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
|     |     |     |     |     |     | ρI  | V   |      |     |     |     |      |
n
Moreover,
|     |     |     |     |     | I −U | = ECov(Xn|W) |     |     | ⪰ 0, |     |     |     |
| --- | --- | --- | --- | --- | ---- | ------------ | --- | --- | ---- | --- | --- | --- |
n
and similarly
|     |     |     |     |     |     | I   | −V ⪰ | 0.  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
n

11
| We    | now prove | the     | determinant | inequality |     | needed | for the    | entropy | estimate. |     |     |
| ----- | --------- | ------- | ----------- | ---------- | --- | ------ | ---------- | ------- | --------- | --- | --- |
| Lemma | 3.        | For 0 < | ρ < 1,      |            |     |        |            |         |           |     |     |
|       |           |         | det(I       | −U)det(I   |     | −V)    | ≤ (1−ρ)2k. |         |           |     |     |
|       |           |         |             | n          |     | n      |            |         |           |     |     |
Proof: For ρ > 0, the positive semidefiniteness in (17) implies that U is positive definite.
Taking the Schur complement of U, V −ρ2U−1 ⪰ 0. Hence V ⪰ ρ2U−1. Since V ⪯ I , we
n
ρ2U−1
| have |     | ⪯ I n . | Thus every | eigenvalue | u   | i of U satisfies |     |     |     |     |     |
| ---- | --- | ------- | ---------- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- |
ρ2
|      |          |        |                 |       |       | ≤ u i ≤ | 1.         |     |     |     | (18) |
| ---- | -------- | ------ | --------------- | ----- | ----- | ------- | ---------- | --- | --- | --- | ---- |
| From | V ⪰      | ρ2U−1, | we obtain       | I −V  | ⪯ I   | −ρ2U−1. | Therefore, |     |     |     |      |
|      |          |        |                 | n     |       | n       |            |     |     |     |      |
|      |          |        |                 | det(I | −V)   | ≤ det(I | −ρ2U−1).   |     |     |     |      |
|      |          |        |                 |       | n     | n       |            |     |     |     |      |
| Let  | u ,...,u | be     | the eigenvalues |       | of U. | Then,   |            |     |     |     |      |
|      | 1        | n      |                 |       |       |         |            |     |     |     |      |
n
|       |          |     |       |       |          |         |     |     |          | (cid:18) ρ2(cid:19) |        |
| ----- | -------- | --- | ----- | ----- | -------- | ------- | --- | --- | -------- | ------------------- | ------ |
|       |          |     |       |       |          | −ρ2U−1) |     |     | (cid:89) |                     |        |
| det(I | −U)det(I |     | −V) ≤ | det(I | −U)det(I |         |     | =   | (1−u     | ) 1−                | . (19) |
|       | n        |     | n     |       | n        | n       |     |     |          | i u                 |        |
i
i=1
| For | every | u ∈ [ρ2,1], |              |     |     |                     |        |     |      |     |     |
| --- | ----- | ----------- | ------------ | --- | --- | ------------------- | ------ | --- | ---- | --- | --- |
|     |       |             |              |     |     | (cid:18) ρ2(cid:19) | (u−ρ)2 |     |      |     |     |
|     |       |             | (1−ρ)2−(1−u) |     |     | 1−                  | =      |     | ≥ 0. |     |     |
|     |       |             |              |     |     | u                   |        | u   |      |     |     |
Consequently,
|     |     |     |     |      | (cid:18) | ρ2(cid:19) |          |     |     |     |     |
| --- | --- | --- | --- | ---- | -------- | ---------- | -------- | --- | --- | --- | --- |
|     |     |     |     | (1−u | ) 1−     |            | ≤ (1−ρ)2 |     |     |     |     |
i
u i
| for every | i,             | which    | gives       |          |             |             |            |         |       |     |     |
| --------- | -------------- | -------- | ----------- | -------- | ----------- | ----------- | ---------- | ------- | ----- | --- | --- |
|           |                |          | det(I       | −U)det(I |             | −V)         | ≤ (1−ρ)2k. |         |       |     |     |
|           |                |          |             | n        |             | n           |            |         |       |     |     |
| Lemma     | 4 (Conditional |          | entropy     | bound).  | For         | every exact | Gaussian   |         | code, |     |     |
|           |                |          |             | EH       |             | (cid:0)     |            | (cid:1) |       |     |     |
|           |                |          |             |          | W ≤ nlog    | 2πe(1−ρ)    |            | .       |       |     |     |
|           | Proof:         | For each | w, Gaussian | maximal  |             | entropy     | gives      |         |       |     |     |
|           |                |          |             |          | n           |             | 1          |         |       |     |     |
|           |                |          | h(Xn|w)     |          | ≤ log(2πe)+ |             | logdetA    |         | .     |     |     |
w
|           |     |           |           |     | 2         |     | 2         |     |      |     |     |
| --------- | --- | --------- | --------- | --- | --------- | --- | --------- | --- | ---- | --- | --- |
| Averaging |     | and using | concavity | of  | logdet,   |     |           |     |      |     |     |
|           |     |           |           |     | n         |     | 1         |     |      |     |     |
|           |     |           | h(Xn|W)   |     |           |     | logdetE[A |     |      |     |     |
|           |     |           |           | ≤   | log(2πe)+ |     |           |     | ]    |     |     |
|           |     |           |           |     | 2         |     | 2         |     | W    |     |     |
|           |     |           |           |     | n         |     | 1         |     |      |     |     |
|           |     |           |           | =   | log(2πe)+ |     | logdet(I  |     | −U). |     |     |
|           |     |           |           |     | 2         |     | 2         | n   |      |     |     |

12
Similarly,
|     |     |     |         |     | n         |     | 1        |     |      |     |     |
| --- | --- | --- | ------- | --- | --------- | --- | -------- | --- | ---- | --- | --- |
|     |     |     | h(Yn|W) | ≤   | log(2πe)+ |     | logdet(I |     | −V). |     |     |
n
|     |     |     |     |     | 2   |     | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore
1
EH
|     |     | W   | ≤ nlog(2πe)+ |     | log[det(I |     | n −U)det(I |     | n −V)]. |     | (20) |
| --- | --- | --- | ------------ | --- | --------- | --- | ---------- | --- | ------- | --- | ---- |
2
| Applying | the determinant |     | lemma,                |     |     |     |        |          |     |         |     |
| -------- | --------------- | --- | --------------------- | --- | --- | --- | ------ | -------- | --- | ------- | --- |
|          |                 |     |                       |     |     |     |        | (cid:0)  |     | (cid:1) |     |
|          |                 | EH  | ≤ nlog(2πe)+nlog(1−ρ) |     |     |     | = nlog | 2πe(1−ρ) |     | .       |     |
W
| E. Optimization |     | over the    | Transport | Parameter |       |            |     |        |     |     |     |
| --------------- | --- | ----------- | --------- | --------- | ----- | ---------- | --- | ------ | --- | --- | --- |
| Substituting    | the | conditional | entropy   |           | bound | into (16), | we  | obtain |     |     |     |
(cid:112)
|     | Γ   | (ρ) ≥ nlog(2πe |     | 1−ρ2) |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
n
|           |              |                | (cid:18) | ρt        | (cid:19)     |          |      |          | ρkt   |           |      |
| --------- | ------------ | -------------- | -------- | --------- | ------------ | -------- | ---- | -------- | ----- | --------- | ---- |
|           |              |                |          |           |              | (cid:0)  |      | (cid:1)  |       |           |      |
|           |              | +              | −1+      |           | nlog         | 2πe(1−ρ) |      | −        |       | log(2πt). | (21) |
|           |              |                |          | 1−ρ2      |              |          |      |          | 1−ρ2  |           |      |
| For 0 <   | ρ < 1,       | the derivative |          | of the    | right-hand   | side     | with | respect  | to    | t is      |      |
|           |              |                |          |           | ρn           |          | t    |          |       |           |      |
|           |              |                |          |           | −            | log      | .    |          |       |           |      |
|           |              |                |          |           | 1−ρ2         | 1−ρ      |      |          |       |           |      |
| Hence the | unique       | maximizer      | is       | t = 1−ρ.  | Substituting |          | t =  | 1−ρ      | gives |           |      |
|           |              |                |          |           | (cid:20)     |          |      | (cid:21) |       |           |      |
|           |              |                |          |           | 1            | 1+ρ      |      | ρ        |       |           |      |
|           |              |                | Γ        | n (ρ) ≥   | n log        |          | +    |          | .     |           | (22) |
|           |              |                |          |           | 2            | 1−ρ      | 1+ρ  |          |       |           |      |
| By the    | multi-letter | converse       |          | and (22), |              |          |      |          |       |           |      |
|           |              |                |          |           | Γ            | (ρ)      | 1    | 1+ρ      | ρ     |           |      |
n
|     |     | C     | (π ρ | ) ≥ limsup |     | ≥   | log |     | +   | .   |     |
| --- | --- | ----- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Exact |      |            | n   |     | 2   | 1−ρ | 1+ρ |     |     |
n→∞
|          |       |             |     | III.  | PROOF   | OF THEOREM |     | 3        |     |     |     |
| -------- | ----- | ----------- | --- | ----- | ------- | ---------- | --- | -------- | --- | --- | --- |
| The case | ρ = 0 | is trivial, | and | thus, | we only | consider   | ρ   | ∈ (0,1). |     |     |     |

13
A. A Multi-letter Bound
We now introduce the n-letter rate region:
 
(R ,R) : ∃P P P s.t.
 0 W Xn|W Yn|W 
  P = π⊗n,  
R (π ) := XnYn ρ , (23)
n ρ R ≥ 1I(W;Xn),
  n  
 R+R ≥ 1Γ (P ,P ,P ) 
0 n n W Xn|W Yn|W
where
Γ (P ,P ,P ) := −h(Xn|W)−h(Yn|W)+E H(n)(P ,P ), (24)
n W Xn|W Yn|W W ρ Xn|W Yn|W
which is the objective function in (7). We first prove the fundamental converse.
Proposition 3. For every exact n-letter channel synthesis code (R ,P ,P ) for
0 M|XnK Yn|MK
π⊗n and letting W = (M,K), we have Xn — W — Yn, R ≥ 1I(W;Xn), and R +R ≥
ρ n 0
1Γ (P ,P ,P ). As a consequence,
n n W Xn|W Yn|W
(cid:91)
R (π ) ⊆ cl R (π ).
Exact ρ n ρ
n≥1
Proof: By examining the proof of Proposition 1,
kR+kR ≥ H(W) ≥ −h(Xn|W)−h(Yn|W)+EH(n)(P ,P ).
0 ρ Xn|W Yn|W
Moreover,
kR ≥ H(M|K) ≥ I(Xn;M|K) = I(Xn;M,K) = I(Xn;W).
B. Evaluation of the Multi-letter Bound
Recall that
U = Cov(E[Xn|W]) = Cov(a ),
W
and
V = Cov(E[Yn|W]) = Cov(b ).
W
Let u ,1 ≤ i ≤ n be eigenvalues of U. From (18), we know ρ2 ≤ u ≤ 1.
i i
From (20) and (19), we get
1
EH ≤ nlog(2πe)+ log[det(I −U)det(I −V)]
W n n
2
1 (cid:88)
n (cid:20) (cid:18) ρ2(cid:19)(cid:21)
= nlog(2πe)+ log (1−u ) 1− . (25)
i
2 u
i
i=1

14
| Moreover, | we      | have |     |                      |     |                      |     |     |              |
| --------- | ------- | ---- | --- | -------------------- | --- | -------------------- | --- | --- | ------------ |
|           | I(Xn;W) |      | =   | h(Xn)−h(Xn|W)        |     |                      |     |     |              |
|           |         |      |     | n log(2πe)−E(cid:2)1 |     |                      |     |     | (cid:12)     |
|           |         |      | ≥   |                      |     | log{(2πe)ndet(Cov(Xn |     |     | W))} (cid:3) |
(cid:12)
|     |     |     |     | 2   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     | =   | − E(cid:2) | logdet(A | ) (cid:3) |     |     |     |
| --- | --- | --- | --- | ---------- | -------- | --------- | --- | --- | --- |
W
2
1
logdet(E[A
|     |     |     | ≥   | −   |     | W ]) |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
2
1
|     |     |     | =   | − logdet(I |     | n −U) |     |     |     |
| --- | --- | --- | --- | ---------- | --- | ----- | --- | --- | --- |
2
n
1 (cid:88)
|     |     |     | =   | −   | log(1−u | ),  |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
i
2
i=1
where the first inequality follows since Gaussian distributions maximize entropy, the second
inequality follows by the concavity of logdet, and the third equality follows by the law of total
covariance.
We next show that setting u ,1 ≤ i ≤ n to the same value will lead to a further bound.
i
| Lemma | 5. Assume | that | ρ2  | ≤ u ≤ | 1 for | all i. If |     |     |     |
| ----- | --------- | ---- | --- | ----- | ----- | --------- | --- | --- | --- |
i
n
1
(cid:88)
|     |     |     |     |     | log(1−u | ) = | log(1−α), |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --------- | --- | --- |
|     |     |     |     | n   |         | i   |           |     |     |
i=1
then
|     |     |     |     | n   | (cid:18) | ρ2(cid:19) | (cid:18) | ρ2(cid:19) |     |
| --- | --- | --- | --- | --- | -------- | ---------- | -------- | ---------- | --- |
1 (cid:88)
|        |        |     |           |     | log   | 1− ≤                | log 1− |               | .   |
| ------ | ------ | --- | --------- | --- | ----- | ------------------- | ------ | ------------- | --- |
|        |        |     |           | n   |       | u                   |        | α             |     |
|        |        |     |           | i=1 |       | i                   |        |               |     |
| Proof: | Define | x   | = log(1−u |     | ), so | that the assumption |        | is equivalent | to  |
|        |        | i   |           |     | i     |                     |        |               |     |
1 n
(cid:88)
|     |     |     |     |     |     | x = log(1−α). |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
|     |     |     |     |     | n   | i             |     |     |     |
i=1
| Consider | the | function |     |     |        |          |     |          |     |
| -------- | --- | -------- | --- | --- | ------ | -------- | --- | -------- | --- |
|          |     |          |     |     |        | (cid:18) | ρ2  | (cid:19) |     |
|          |     |          |     |     | f(x) = | log 1−   |     | ,        |     |
1−ex
| defined | for x ≤ | log(1−ρ2). |     | Since       | u = | 1−ex, we | have     |            |     |
| ------- | ------- | ---------- | --- | ----------- | --- | -------- | -------- | ---------- | --- |
|         |         |            |     |             |     |          | (cid:18) | ρ2(cid:19) |     |
|         |         |            |     | f(log(1−u)) |     | = log    | 1−       | .          |     |
u
| We first | show | that | h is concave. |     | A direct | calculation | gives |     |          |
| -------- | ---- | ---- | ------------- | --- | -------- | ----------- | ----- | --- | -------- |
|          |      |      |               |     | (cid:18) |             | 1−ρ2  |     | (cid:19) |
1
|     |     |     | f′′(x) | =   | ex      | −   |            |     | .   |
| --- | --- | --- | ------ | --- | ------- | --- | ---------- | --- | --- |
|     |     |     |        |     | (1−ex)2 |     | (1−ρ2−ex)2 |     |     |

15
Because u = 1−ex ≥ ρ2, we have ex ≤ 1−ρ2. Moreover,
(1−ρ2−ex)2 ≤ (1−ρ2)(1−ex)2,
which implies
1 1−ρ2
≤ .
(1−ex)2 (1−ρ2−ex)2
Hence f′′(x) ≤ 0, and therefore f is concave.
By Jensen’s inequality for concave functions,
(cid:32) (cid:33)
n n
1 (cid:88) 1 (cid:88)
f(x ) ≤ f x .
i i
n n
i=1 i=1
Using the definition of x and the constraint, we obtain
i
1 (cid:88)
n (cid:18) ρ2(cid:19) (cid:18) ρ2(cid:19)
log 1− ≤ log 1− .
n u α
i
i=1
Applying Lemma 5 yields that for some α such that ρ2 ≤ α ≤ 1, it holds that
1
I(Xn;W) ≥ − log(1−α),
2
and
EH 1 (cid:20) (cid:18) ρ2(cid:19)(cid:21)
W
≤ log(2πe)+ log (1−α) 1− . (26)
n 2 α
Analogously to (16), we have
R+R ≥log(2πe (cid:112) 1−ρ2)+ (cid:18) −1+ ρt (cid:19) EH W − ρt log(2πt).
0 1−ρ2 n 1−ρ2
Substituting (26) into this inequality yields
(cid:112) ρt
R+R ≥ log(2πe 1−ρ2)− log(2πt)
0 1−ρ2
(cid:18)
ρt
(cid:19)(cid:18)
1
(cid:20) (cid:18) ρ2(cid:19)(cid:21)(cid:19)
+ −1+ log(2πe)+ log (1−α) 1− . (27)
1−ρ2 2 α
The optimal parameter t is
(cid:115)
(cid:18) ρ2(cid:19)
t = (1−α) 1− .
α
Substituting it into (27) yields the desired bound
(cid:114)
(cid:16) (cid:17)
ρ (1−α) 1− ρ2
1 1−ρ2 α
R+R ≥ log + .
0 2 (1−α) (cid:16) 1− ρ2 (cid:17) 1−ρ2
α

16
Acknowledgements
Generative-AI use disclosure: During the preparation of this manuscript, the author used
ChatGPT (GPT-5.5-mini model, Think mode) as an auxiliary tool for exploring proof ideas,
checkingcalculations,andimprovingexposition.Allmathematicalcontent,includingstatements,
proofs, and references, was independently verified by the author, who assumes full responsibility
| for the final | manuscript. |     |     |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- | --- |
REFERENCES
[1] A.D.Wyner. Thecommoninformationoftwodependentrandomvariables. IEEETransactionsonInformation
| Theory, 21(2):163–179, |     | Mar 1975. |     |     |     |     |
| ---------------------- | --- | --------- | --- | --- | --- | --- |
IEEE International Symposium on
| [2] G. R. Kumar, | C.-T. Li,      | and A. | El Gamal. Exact    | common  | information. In |     |
| ---------------- | -------------- | ------ | ------------------ | ------- | --------------- | --- |
| Information      | Theory (ISIT), | pages  | 161–165, Honolulu, | Hawaii, | USA, 2014.      |     |
[3] L.YuandV.Y.F.Tan. Onexactand∞-Re´nyicommoninformation. IEEETransactionsonInformationTheory,
| 66(6):3366–3406, | Jun 2020. |     |     |     |     |     |
| ---------------- | --------- | --- | --- | --- | --- | --- |
[4] B. N. Vellambi and J. Kliewer. New results on the equality of exact and Wyner common information rates. In
IEEE International Symposium on Information Theory (ISIT), pages 151–155, Vail, Colorado, USA, Oct 2018.
[5] L. Yu and V. Y. F. Tan. Wyner’s common information under Re´nyi divergence measures. IEEE Transactions
| on Information | Theory, | 64(5):3616–3623, | May 2018. |     |     |     |
| -------------- | ------- | ---------------- | --------- | --- | --- | --- |
[6] L.YuandV.Y.F.Tan. Correctionsto“Wyner’scommoninformationunderRe´nyidivergencemeasures”. IEEE
| Transactions | on Information | Theory, | 66(4):2599–2608, | 2020. |     |     |
| ------------ | -------------- | ------- | ---------------- | ----- | --- | --- |
[7] C. H. Bennett, P. W. Shor, J. A. Smolin, and A. V. Thapliyal. Entanglement-assisted capacity of a quantum
|     |     |     | IEEE | Transactions | on Information | Theory, |
| --- | --- | --- | ---- | ------------ | -------------- | ------- |
channel and the reverse Shannon theorem. 48(10):2637–2655, Oct
2002.
[8] A.Winter. Compressionofsourcesofprobabilitydistributionsanddensityoperators. arXiv:quant-ph/0208131,
2002.
[9] P. Cuff. Distributed channel synthesis. IEEE Transactions on Information Theory, 59(11):7071–7096, 2013.
[10] C.H.Bennett,I.Devetak,A.W.Harrow,P.W.Shor,andA.Winter. ThequantumreverseShannontheoremand
resource tradeoffs for simulating quantum channels. IEEE Transactions on Information Theory, 60(3):2926–
| 2959, Oct | 2014. |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
[11] P. Harsha, R. Jain, D. McAllester, and J. Radhakrishnan. The communication complexity of correlation. IEEE
| Transactions | on Information | Theory, | 56(1):438–449, | Oct 2010. |     |     |
| ------------ | -------------- | ------- | -------------- | --------- | --- | --- |
[12] C.-T. Li and A. El Gamal. Strong functional representation lemma and applications to coding theorems. IEEE
| Transactions | on Information | Theory, | 64(11):6967–6978, | Oct | 2018. |     |
| ------------ | -------------- | ------- | ----------------- | --- | ----- | --- |
[13] L. Yu and V. Y. F. Tan. Exact channel synthesis. IEEE Transactions on Information Theory, 66(5):2299–2818,
May 2020.
[14] Max Fathi. A sharp symmetrized form of talagrand’s transport-entropy inequality for the gaussian measure.
| Electron. | Commun. Probab., | 23(81):1–9, | 2018. |     |     |     |
| --------- | ---------------- | ----------- | ----- | --- | --- | --- |
---- END DOCUMENT ----
