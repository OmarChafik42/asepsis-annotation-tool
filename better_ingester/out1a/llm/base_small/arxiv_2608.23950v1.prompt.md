Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
1
Receive Diversity for Differential Binary Noise
Modulation
Paulo V. B. Tome´, Andre´ A. dos Anjos, Hugerles S. Silva, Daniel C. Arau´jo,
Robson D. Vieira, and Ertugrul Basar
Abstract
Differential binary noise (DBN) modulation encodes information in the polarity transition of a
reused noise realization, dispensing channel state information and carrier-phase recovery. This letter
proposes single-input multiple-output (SIMO) reception for DBN via post-correlation decision-statistic
combining,followedbyonezero-thresholddecision.ThecombinedstatisticisaHermitianquadraticform
in complex Gaussian vectors, yielding an exact conditional bit error probability (BEP) with no Gaussian
approximation. Averaging it over κ-µ fading and the reused energy gives the exact BEP for arbitrary
weights. Because that energy is shared, its deep fades are common to every branch, and the observation
length caps the diversity order at min(Mµ,N). The deflection-optimal weights follow in closed form
and interpolate soft combining and power weighting. Measured 65GHz indoor non-line-of-sight (NLoS)
results quantify the trade-off between spatial resources and observation length.
Index Terms
DBN modulation, noncoherent detection, SIMO, receive diversity, decision-statistic combining,
diversity order, IoT.
I. INTRODUCTION
Internet of things (IoT) and machine-type communication systems must support many low-
power devices under tight energy and complexity constraints [1], which motivates keeping the
transmitter simple and shifting processing to the gateway, so as to avoid the circuit-power cost
of carrier synchronization, channel estimation, and coherent demodulation [2], [3]. Noise-based
modulation suits this regime by embedding information in the statistical behavior of random
waveforms rather than in deterministic constellation points. Representative schemes include
variance-switching noise modulation (NoiseMod) [4], on-off digital noise (OODN) [5], [6], and
6202
guA
52
]PS.ssee[
1v05932.8062:viXra

2
pilot-aided, multi-user, spreading-based, and Gaussian-mixture variants [7], [8], [9], [10]. Within
this family, differential binary noise (DBN) [11] reuses one noise realization across consecutive
symbols and encodes information in their polarity transition, so a receiver decides from the sign
of an inter-symbol correlation statistic, with no channel state information (CSI), noise variance
estimation, carrier phase recovery, or adaptive thresholding. Its reliability, however, is tied to the
number of samples per bit N, since a larger N buys processing gain but lengthens the observation
interval and raises the memory and correlation cost per bit.
This raises a natural question: can spatial diversity replace part of the temporal processing
gain while preserving the noncoherent receiver? The question matters for IoT, where devices
carry one transmit antenna whereas gateways carry M receive antennas. Rather than combining
complex received samples as in equal-gain combining (EGC) or maximal-ratio combining (MRC),
the receiver proposed here forms one DBN decision statistic per branch and combines these
real-valued statistics through a generalized weighting rule, recovering soft combining, single-input
single-output (SISO) operation, and arbitrary weighted combining as particular cases.
The answer is bounded in a way that a single-antenna analysis cannot reveal. Because the
transmitter reuses one realization for every branch, the energy of that realization is shared by all
antennas and cannot be averaged out by adding more of them, so the diversity order is capped
by the observation length rather than by the array size.
This paper contributes a generalized single-input multiple-output (SIMO)-DBN receiver based
on weighted noncoherent decision-statistic combining, which preserves the original transmitter
and zero-threshold detector. Recognizing the combined statistic as a Hermitian quadratic form
in complex Gaussian vectors [12] yields an exact conditional bit error probability (BEP), valid
for every N and free of any Gaussian approximation, from which the exact average BEP
over generalized κ-µ fading follows, evaluated under measured 65GHz indoor millimeter wave
(mmWave) non-line-of-sight (NLoS) conditions. An asymptotic analysis then establishes the
diversity order min(Mµ,N) with its exact leading constant, in which µ is the number of
multipath clusters of the fading model. Furthermore, the deflection-optimal combining weights
follow in closed form, interpolating soft combining and power weighting according to the branch
signal-to-noise ratio (SNR).

3
antenna1 down-converter y k∗,1 [n] N Zk,1 R ˆbk= (cid:26) 0 1 , , T T k k ≥< 0 0
andADC n=1 {·}
delayTb
P a1
sk − 1
delayTb yk
−
1,1[n]
generalized
bk di e f n fe c r o e d n e ti r al sk xk DAC con u v p e - rter xk(t) . . . . . . w d s e t e a c i t g i i s h s i t t o i e c n d 0 ˆbk
Tk
delayTb yk 1,M[n]
N u sa∼
n
m
o
p
i
C
s
le
e
Ns,
re
( o
a
0 n
li
, e
z
σ
a
p
t
u 2 e
io
r I
n
N fra ) me
antennaM
down-converter y k∗,M [n]
−
N Zk,M R
aM
andADC n=1 {·}
P Tk= M
ℓ=1
aℓR
{
Zk,ℓ}
P
Fig. 1. Proposed DBN transmitter and SIMO receiver architecture. A single noise realization u is generated once per frame and
reused by every receive branch.
II. SIMO-DBN SYSTEM MODEL
Fig. 1 illustrates the proposed SIMO-DBN system. The input bits are differentially encoded and
modulate a reused complex Gaussian noise realization, which propagates through M independent
fading branches, each corrupted by additive white Gaussian noise (AWGN). Consider a binary
sequence b ∈ {0,1} transmitted during the k-th bit interval [(k −1)T ,kT ), where T denotes
k b b b
the bit duration. As in DBN [11], the bits are differentially encoded into a bipolar sequence
s ∈ {+1,−1}, such that
k
s = s (1−2b ), d ≜ s s = 1−2b , (1)
k k−1 k k k k−1 k
with an arbitrary initial condition s ∈ {+1,−1}. Thus, the differential symbol is d = +1
0 k
for b = 0 and d = −1 for b = 1. Within a frame, a single realization u ∼ CN(0,σ2I )
k k k u N
is generated and reused across consecutive intervals, giving the transmitted vector x = s u,
k k
with I being the N ×N identity matrix and σ2 denoting the per-sample variance of the noise
N u
realization. Its instantaneous energy E ≜ ∥u∥2 follows a Gamma distribution with shape N and
u
scale σ2. Normalizing it as ε ≜ E /σ2 removes that scale from the analysis and gives
u u u
εN−1exp(−ε)
f (ε) = , ε ≥ 0, (2)
ε
Γ(N)
which is the form used throughout.
With a single transmit antenna and M receive antennas, the ℓ-th branch observes y =
k,ℓ
h x +w ,ℓ = 1,...,M,whereh isthecomplexfadingcoefficientandw ∼ CN(0,σ2I ),
k,ℓ k k,ℓ k,ℓ k,ℓ w N
with σ2 being the noise variance per complex sample, is an AWGN vector independent across
w
antennas, time, and symbols. Adopting the standard two-symbol block-fading assumption of
differential detection, h ≈ h ≜ h , valid when the symbol duration is shorter than the
k,ℓ k−1,ℓ ℓ

4
channel coherence time, the combining is carried out entirely at the decision-statistic level,
| keeping channel |     | and combining |             |     | independent. |          |     |          |           |     |     |
| --------------- | --- | ------------- | ----------- | --- | ------------ | -------- | --- | -------- | --------- | --- | --- |
|                 |     | III.          | GENERALIZED |     |              | WEIGHTED |     | DECISION | STATISTIC |     |     |
At the ℓ-th receive antenna, the DBN differential correlation statistic is
N
(cid:88)
|     |     |     |     | Z ≜ | yH  | y =   |     | y∗ [n]y   | [n], |     | (3) |
| --- | --- | --- | --- | --- | --- | ----- | --- | --------- | ---- | --- | --- |
|     |     |     |     | k,ℓ | k,ℓ | k−1,ℓ |     | k,ℓ k−1,ℓ |      |     |     |
n=1
| (·)H |     |     |     |     |     |     | (·)∗ |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
where denotes the Hermitian transpose and denotes the complex conjugate. The proposed
receiver combines these branch statistics according to an arbitrary weighting coefficient a ,
ℓ
| yielding the | decision |     | variable |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
M
(cid:88)
|     |     |     | T   | ≜   | a   | R{Z }, |     | a = [a ,...,a | ].  |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | ------------- | --- | --- | --- |
|     |     |     |     | k   | ℓ   | k,ℓ    |     | 1             | M   |     | (4) |
ℓ=1
|     |     |     |     |     |     |     |     | ˆ b = | 0 T ≥ 0 | ˆ b = 1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------- | --- |
The final decision follows the DBN zero-threshold rule, k for k and k otherwise.
Unlike EGC and MRC, which combine phase-aligned complex samples, the proposed receiver
operates entirely at the decision-statistic level, requiring no carrier-phase recovery, channel-
amplitude estimation, or noise-variance estimation, and thus preserving the noncoherent DBN
structure. Soft combining is the particular case a = 1 for all ℓ, while other weighting rules leave
ℓ
| the analytical | framework |     | unchanged. |     |      |       |          |           |       |     |     |
| -------------- | --------- | --- | ---------- | --- | ---- | ----- | -------- | --------- | ----- | --- | --- |
|                | x         | = s | u          | y   | = h  | x +w  |          |           |       |     |     |
| Substituting   |           | k   | k and      | k,ℓ |      | ℓ k   | k,ℓ into | (3) gives |       |     |     |
|                |           |     |            | Z   | = |h | |2d E | +h∗s     | uHw       |       |     |     |
|                |           |     |            | k,ℓ |      | ℓ k u | ℓ        | k k−1,ℓ   |       |     |     |
|                |           |     |            |     | +h   | s wH  | u+wH     | w         | ,     |     |     |
|                |           |     |            |     |      | ℓ k−1 |          |           | k−1,ℓ |     | (5) |
|                |           |     |            |     |      |       | k,ℓ      | k,ℓ       |       |     |     |
so that, taking the real part and summing over the M antennas as in (4),
|     |     |     |     |     |     | M        |     | M        |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- |
|     |     |     |     |     |     | (cid:88) |     | (cid:88) |     |     |     |
|2
|     |     |     |     | T   | = d | E a | |h  | + a | ξ ,   |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |     |     | k   | k   | u   | ℓ ℓ |     | ℓ k,ℓ |     |     |
|     |     |     |     |     |     | ℓ=1 |     | ℓ=1 |       |     |     |
where ξ collects the two signal-noise cross terms and the noise-noise term, and the combined
k,ℓ
(cid:80)M
instantaneous channel power gain is G ≜ a |h |2. The useful term depends on |h |2 and
|     |     |     |     |     |     | M   | ℓ=1 ℓ | ℓ   |     |     | ℓ   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
not on the channel phase, as a direct consequence of the product h∗h arising from differential
ℓ ℓ
correlation, so phase rotations common to two adjacent symbols do not affect the sign of the
useful decision component. The weighting vector is treated as deterministic throughout.

5
|     |     |     |     | IV. | PERFORMANCE |     |     | ANALYSIS |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | -------- | --- | --- | --- | --- |
The combined decision statistic T in (4) needs no distributional approximation. Grouping the
k
|     |     |     |     |     | v = | [y [n], | y   | [n]]T, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- | --- | --- |
two symbols of each sample into ℓ,n k,ℓ k−1,ℓ (4) becomes a Hermitian quadratic
|     |     |     |     |     |     |     |     |     |     |     | ≜ E[exp(ȷωT |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
form in complex Gaussian vectors, whose characteristic function ϕ (ω) )], in
|     |     |     |     |     |     |     |     |     |     | T   |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which ω is the transform variable, is classical. For a complex Gaussian vector of mean m
and covariance Σ, it reads exp[ȷωmH(I − ȷωΣF)−1Fm]/det(I − ȷωΣF) [12]. Here, F is a
√
Hermitian matrix with eigenvalues ±1 and eigenvectors [1,±1]T/ 2; under d = −1 the mean
k
2
lies entirely along the −1 one, so with soft combining the product over ℓ and n collapses to
2
| ϕ   | (ω) = | exp[−ȷωE    | G    | /(1+ȷωσ2/2)]/(1+ω2σ4/4)MN, |            |        |     |     |       |         |               |        |
| --- | ----- | ----------- | ---- | -------------------------- | ---------- | ------ | --- | --- | ----- | ------- | ------------- | ------ |
|     | T     |             | u    | M                          |            |        |     |     | which | depends | on the reused | energy |
|     |       |             |      |                            | w          |        | w   |     |       |         |               |        |
| and | on    | the channel | only | through                    | the single | scalar |     |     |       |         |               |        |
E G
|     |     |     |     |     |     | x ≜ | u M | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(7)
σ2
w
With equal weights every branch contributes the same factor, and the scale of ω is immaterial
because only the sign of T decides. Then ϕ is that of binary differential phase-shift keying
|     |     |      |     | k   |     | T   |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | L   | = MN |     |     |     |     | x.  |     | ϕ   |     |     |     |
with diversity branches and total SNR Inverting T yields the classical result [13,
Sec. 13.4],
|     |     |     |     | e−x   | L−1      |       |     |     | L −1−k(cid:18) |      | (cid:19) |     |
| --- | --- | --- | --- | ----- | -------- | ----- | --- | --- | -------------- | ---- | -------- | --- |
|     |     |     |     |       | (cid:88) |       |     | 1   | (cid:88)       | 2L−1 |          |     |
|     |     |     | P   | (x) = |          | β xk, | β   | =   |                |      | .        | (8) |
|     |     |     |     | e     |          | k     | k   |     |                |      |          |     |
|     |     |     |     | 22L−1 |          |       |     | k!  |                | n    |          |     |
|     |     |     |     |       | k=0      |       |     |     | n=0            |      |          |     |
Two physical remarks follow. First, x in (7) is the total energy collected by the MN correlator
taps, normalized by the noise variance, so the conditional error depends on M and N only
through their product, each antenna and each sample contributing one more tap to the same sum.
Second, the differential receiver correlates two noisy copies of the same waveform rather than
a waveform against a clean template, which is why L = MN appears both in the number of
branches and in the noise-noise floor of (8) instead of only in the useful term. Unequal weights
scale the factor that each receive branch contributes to ϕ by its own a , so the branches no longer
|     |     |     |     |     |     |     |     | T   |     | ℓ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
share a common scale in ω and (8) no longer applies. The conditional BEP then follows from
the same ϕ by the Gil-Pelaez inversion [14], which recovers Pr{T < 0} from a characteristic
|     |     | T   |     |     |     |     |     |     |     | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
function through a single real integral. Unequal weights leave the diversity order untouched,
(cid:80)
since the density of a |h |2 still vanishes as gMµ−1 for any strictly positive weights and only
|     |     |     |     | ℓ ℓ |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ℓ
its constant changes, so weighting buys array gain and not diversity. Unless otherwise stated,
a = 1
|     | ℓ in | what | follows, | and Section | IV-C | returns | to  | the general | case. |     |     |     |
| --- | ---- | ---- | -------- | ----------- | ---- | ------- | --- | ----------- | ----- | --- | --- | --- |

6
| A. Average | BEP |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let γ¯ ≜ σ2/σ2 denote the average per-sample SNR, so that x = γ¯εG , with ε distributed as
|     | u w |     |     |     |     |     |     |     | M   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in (2). Since the transmitted energy and the fading process are independent, the average BEP is
| the two-dimensional |     | integral |                    |     |         |      |          |     |     |     |
| ------------------- | --- | -------- | ------------------ | --- | ------- | ---- | -------- | --- | --- | --- |
|                     |     |          | (cid:90) ∞(cid:90) | ∞   |         |      |          |     |     |     |
|                     |     |          | P ¯ =              | P   | (γ¯εg)f | (ε)f | (g)dεdg. |     |     |     |
|                     |     |          | e                  |     | e       | ε    | GM       |     |     | (9) |
0 0
The inner average is available in closed form. Since (8) is a polynomial in x times e−x, and
x = γ¯εg is linear in ε, each term meets the Gamma density of (2) in a single integral,
|     |     | (cid:90) ∞ |                  |     |     | Γ(N +k) |     |          |     |     |
| --- | --- | ---------- | ---------------- | --- | --- | ------- | --- | -------- | --- | --- |
|     |     |            | εN−1+ke−(1+c)εdε |     | =   |         | ,   | c ≜ γ¯g, |     |     |
(1+c)N+k
0
| so that averaging | (8) | over | the reused | energy     | gives |         |          |     |     |      |
| ----------------- | --- | ---- | ---------- | ---------- | ----- | ------- | -------- | --- | --- | ---- |
|                   |     |      |            | L−1        |       |         |          | ck  |     |      |
|                   |     |      |            | 1 (cid:88) |       | Γ(N +k) |          |     |     |      |
|                   |     | P    | (g) =      |            | β     |         |          | .   |     | (10) |
|                   |     |      | e          |            | k     |         |          |     |     |      |
|                   |     |      | 22L−1      |            |       | Γ(N)    | (1+c)N+k |     |     |      |
k=0
Expression (10) is exact rather than a quadrature, and it reduces (9) to the single integral
¯ (cid:82)∞
P = P (g)f (g)dg. It returns 1/2 as c → 0, since only the k = 0 term survives and
| e 0 | e GM |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
β = 22L−2. As in (7), the branch gain enters only through c, the average post-correlation SNR
0
| per unit of | reused energy. |     |     |     |     |     |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For independent and identically distributed (i.i.d.) κ-µ branches with common average power
| Ω = E[|h |2], |     | E[·] |     |     |     |     |     |     | G   |     |
| ------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ℓ in which is the expectation operator, and for soft combining, M is the power
of an equivalent κ-µ random variable with κ = κ, µ = Mµ, and Ω = MΩ [15], whose
|              |             |       |                  |     | eq      |        | eq         |      | eq          |     |
| ------------ | ----------- | ----- | ---------------- | --- | ------- | ------ | ---------- | ---- | ----------- | --- |
| power-domain | probability |       | density function |     | (PDF)   | is     |            |      |             |     |
|              |             |       | µ (1+κ           | )   | µeq+1 g | µeq− 1 | (cid:18) µ | (1+κ | )g (cid:19) |     |
|              |             |       |                  |     | 2       | 2      |            |      |             |     |
|              |             | f (g) | = eq             | eq  |         | exp    | −          | eq   | eq          |     |
GM
|     |     |     | µ eq − | 1        | µ eq      | +1   |          | Ω        |     |      |
| --- | --- | --- | ------ | -------- | --------- | ---- | -------- | -------- | --- | ---- |
|     |     |     | κ 2    | eµ κ     | eqΩ       | 2    |          | eq       |     |      |
|     |     |     | e q    | eq       | e q       |      |          |          |     |      |
|     |     |     |        | (cid:32) | (cid:115) |      | (cid:33) |          |     |      |
|     |     |     |        |          | κ         | (1+κ | )g       |          |     |      |
|     |     |     | ×I     | 2µ       |           | eq   | eq       | , g ≥ 0, |     | (11) |
|     |     |     | µ −1   |          | eq        |      |          |          |     |      |
|     |     |     | eq     |          |           | Ω    |          |          |     |      |
eq
in which I (·) is the modified Bessel function of the first kind and order ν, κ is the power ratio
ν
between the dominant component and the scattered waves, and µ is associated with the number
of multipath clusters. Setting κ = 0 and µ = 1 recovers Rayleigh fading, µ = 1 with κ > 0 gives
| Rician fading, | and | κ → 0 | gives Nakagami-m |     | with | m = | µ.  |     |     |     |
| -------------- | --- | ----- | ---------------- | --- | ---- | --- | --- | --- | --- | --- |

7
|     |     | z = µ | (1+κ | )g/Ω |     |     |     |     |     | κ-µ |     |     |     |
| --- | --- | ----- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Applying eq eq eq to the remaining integral turns the density into a Laguerre
| weight | and | gives |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 µeq
|     |     |     |     | (κ  | µ )   | − n        | 1   | µeq 1  | √       |         |     |     |     |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | ------ | ------- | ------- | --- | --- | --- |
|     |     |     | ¯   |     | eq eq | 2 (cid:88) |     | −      | (cid:0) | (cid:1) |     |     |     |
|     |     |     | P   | ≈   |       |            | w z | 2 I    | 2 κ     | µ z     |     |     |     |
|     |     |     |     | e   | eµ κ  |            | i   | i µ eq | −1      | eq eq i |     |     |     |
|     |     |     |     |     | eq eq |            |     |        |         |         |     |     |     |
i=1
|     |     |     |     |     | (cid:18) |     | (cid:19) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
γ¯z Ω
|     |     |     |     | ×P  |     | i eq |     | ,   |     |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | e   |      |     |     |     |     |     |     | (12) |
|     |     |     |     |     | µ   | (1+κ | )   |     |     |     |     |     |      |
|     |     |     |     |     | eq  |      | eq  |     |     |     |     |     |      |
with z and w being the Laguerre roots and weights, respectively, and n being the number of
|     | i   | i   |     |     |     |     |     |     |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nodes. Expression (12) is accurate while the average is dominated by channel gains of the order
|     | E[G       | ],    |          |        |          |       |      |     |     |     |     |      |     |
| --- | --------- | ----- | -------- | ------ | -------- | ----- | ---- | --- | --- | --- | --- | ---- | --- |
| of  | M         | which | is where | the    | Laguerre | nodes | lie. |     |     |     |     |      |     |
| B.  | Diversity | Order |          |        |          |       |      |     |     |     |     |      |     |
|     | Y         | ≜ εG  | x        | = γ¯Y. |          |       |      |     |     |     |     | εN−1 |     |
Let M , so Near the origin the densities (2) and (11) behave as and
| gµ  | −1, | f (y) |     | Cyd−1, |     | d   |     |     |     |     |     | C   |     |
| --- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eq so Y behaves as with the smaller of the two exponents and a constant
| fixed | below, | giving |     |     |           |     |        |         |     |     |     |     |      |
| ----- | ------ | ------ | --- | --- | --------- | --- | ------ | ------- | --- | --- | --- | --- | ---- |
|       |        |        |     |     | d = min(µ |     | , N) = | min(Mµ, | N)  |     |     |     | (13) |
eq
| and, | after | rescaling | u = | γ¯y in | (9), |       |     |            |       |        |     |     |      |
| ---- | ----- | --------- | --- | ------ | ---- | ----- | --- | ---------- | ----- | ------ | --- | --- | ---- |
|      |       |           |     |        |      |       |     | (cid:90) ∞ |       |        |     |     |      |
|      |       |           |     | P ¯ →  | CK   | γ¯−d, | K   | =          | ud−1P | (u)du. |     |     |      |
|      |       |           |     | e      | d    |       |     | d          | e     |        |     |     | (14) |
0
The coefficient C follows the same comparison. For µ < N the fading sets the exponent and
eq
C = BΓ(N −µ )/Γ(N), with B being the small-argument coefficient of (11). For µ > N the
|        |        | eq   |        |     |              |     |      |        |     |          |        | eq  |        |
| ------ | ------ | ---- | ------ | --- | ------------ | --- | ---- | ------ | --- | -------- | ------ | --- | ------ |
|        |        |      |        | C = | E[G−N]/Γ(N), |     |      | E[G−N] |     | N-th     |        |     |        |
| reused | energy | sets | it and |     |              |     | with |        | the | negative | moment |     | of the |
|        |        |      |        |     | M            |     |      |        | M   |          |        |     |        |
combined gain under (11). Each form holds where its own factor converges, Γ(N −µ ) below
eq
E[G−N]
| the | crossing | and |     | above | it. |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M
At high SNR an error requires the useful term of (6) to collapse, and only two things can
make it collapse. The first is that all M branches fade together. They fade independently, so
Pr{G < t} falls as tµ for small t and every antenna added makes it rarer. The second is that
|     | M   |     |     | eq  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
u
the reused realization comes out weak, and here antennas do not help. The same multiplies
tN
every branch, so one small E wipes out all M of them at once and Pr{ε < t} falls as no
u
matter how large the array. Either event alone produces the error, so the more likely of the two
sets the slope, which is (13). Past Mµ = N the weak realization is the more likely one, and
| extra | antennas | only | raise | the | received | power. |     |     |     |     |     |     |     |
| ----- | -------- | ---- | ----- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |

8
| C. Combining |     | Weight | Design |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Write γ ≜ E |h |2/σ2 for the per-branch post-correlation SNR. Conditioned on E and on
|     | ℓ   | u ℓ | w   |     |            |     |     |     |               |        | u   |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ------------- | ------ | --- | --- |
|     |     |     |     |     | d (cid:80) | a γ |     |     | (cid:80) a2(γ | + N/2) |     | σ4, |
the branch gains, (6) has mean k ℓ ℓ and variance ℓ in units of in
|     |     |     |     |     |     | ℓ   |     |     | ℓ   | ℓ   |     | w   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wH
which γ comes from the two cross terms of (5) and N/2 from its noise-noise term w .
|     | ℓ   |     |     |     |     |     |     |     |     |     | k,ℓ | k−1,ℓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
aTp/(aTDa)1/2,
Maximizing the deflection Ψ(a) = with p = γ and D = diag(γ +N/2), is a
|     |     |     |     |     |     |     |     |     | ℓ ℓ | ℓ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
generalized Rayleigh quotient, solved by a⋆ ∝ D−1p with maximum Ψ⋆ = (pTD−1p)1/2, that is
|     |     |     |     |     |     |     |     | (cid:34) |     | (cid:35)1/2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | --- | --- |
M
|     |     |     |     |     | γ   |     |      | (cid:88) | γ2  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | --- | --- | --- |
|     |     |     | a⋆  | ∝   | ℓ   | ,   | Ψ⋆ = |          | ℓ   | .   |     |     |
(15)
|     |     |     | ℓ   | γ   | +N/2 |     |     | γ   | +N/2 |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     | ℓ   |      |     |     |     | ℓ    |     |     |     |
ℓ=1
The denominator of (15) is the variance contributed by a branch, a signal-noise term proportional
to γ plus a noise-noise term proportional to N/2, so a branch is down-weighted only while
ℓ
its own noise-noise floor dominates its useful energy. The rule gives a → 1 for γ ≫ N/2,
|     |     |     |     |     |     |     |     |     |     | ℓ   | ℓ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recovering soft combining, and a ∝ |h |2 for γ ≪ N/2, the square-law rule.
|     |     |     |     |     | ℓ   | ℓ   | ℓ   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Two properties make (15) practical. First, D is diagonal, so the weights decouple across
branches and no matrix inversion is needed. Second, u and h stay constant over a frame, and
ℓ
with them γ , so the weights are computed once and reused for the K decisions of that frame, at
ℓ
MN
| a cost | negligible | against | the |     | products |     | per bit. |     |     |     |     |     |
| ------ | ---------- | ------- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- |
The two implementations differ only in how γ is obtained. Evaluating (15) with the exact
ℓ
|2
γ requires E and |h separately, which no noncoherent receiver has, so that version is a
| ℓ   |     | u   | ℓ   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
benchmark rather than a receiver. A receiver instead needs γ only in absolute terms, and the
ℓ
| received | energy | already | carries  |     | it, since |      |         |      |         |     |     |      |
| -------- | ------ | ------- | -------- | --- | --------- | ---- | ------- | ---- | ------- | --- | --- | ---- |
|          |        |         | E(cid:2) |     | (cid:3)   |      |         |      |         |     |     |      |
|          |        |         |          | ∥y  | ∥2 =      | E |h | |2 +Nσ2 | = σ2 | (γ +N). |     |     |      |
|          |        |         |          | k,ℓ |           | u ℓ  |         |      | ℓ       |     |     | (16) |
|          |        |         |          |     |           |      |         | w    | w       |     |     |      |
|          |        |         |          |     |           |      |         | ˆ    |         |     |     | ∥2   |
Inverting (16) with the frame-averaged received energy E in place of the expectation of ∥y
|     |     |     |     |     |     |     |     | ℓ   |     |     |     | k,ℓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
gives
|     |     |     |          | (cid:32) | ˆ   | (cid:33) |     |     |     | K        |     |      |
| --- | --- | --- | -------- | -------- | --- | -------- | --- | --- | --- | -------- | --- | ---- |
|     |     |     |          |          | E   |          |     |     | 1   | (cid:88) |     |      |
|     |     |     |          |          | ℓ   |          |     | ˆ   |     | ∥2,      |     |      |
|     |     |     | γˆ = max |          | −N, | 0        | ,   | E = |     | ∥y       |     | (17) |
|     |     |     | ℓ        |          | σ2  |          |     | ℓ K | +1  | k,ℓ      |     |      |
|     |     |     |          |          | w   |          |     |     |     | k=0      |     |      |
which fed back into (15) yields a blind rule needing no CSI, no pilots and no phase reference,
at the cost of knowing the receiver noise floor. Both versions then combine exactly as in (4) and
decide on the same zero threshold, and Algorithm 1 collects the blind one end to end.
|     |     |     | V.  | NUMERICAL |     | RESULTS |     |     | DISCUSSION |     |     |     |
| --- | --- | --- | --- | --------- | --- | ------- | --- | --- | ---------- | --- | --- | --- |
AND
TableIliststhesimulationparameters.TheMonteCarlorunsthefulllinkwithnoapproximation
200
of the decision statistic. Each point accumulates at least bit errors, which keeps its relative

9
Algorithm 1 SIMO-DBN reception of one frame
Require: {y }, k =0,...,K, ℓ=1,...,M; noise floor σ2, window N
k,ℓ w
Ensure: decoded bits ˆb ,...,ˆb
1 K
1: for ℓ=1 to M do
2: Eˆ ℓ ← K 1 +1 (cid:80)K k=0 ∥y k,ℓ ∥2, γˆ ℓ ←max(Eˆ ℓ /σ w 2 −N, 0) ▷ (17)
3: a ℓ ←γˆ ℓ /(γˆ ℓ +N/2) ▷ (15), a ℓ ←1 is soft combining
4: for k =1 to K do
5: for ℓ=1 to M do
6: Z k,ℓ ←y k H ,ℓ y k 1,ℓ ▷ (3), no phase reference
−
7: T k ←
(cid:80)M
ℓ=1 a ℓ R{Z k,ℓ } ▷ (4)
8: ˆb k ←0 if T k ≥0 else 1 ▷ fixed zero threshold, ˆb k from (1)
100
10 2
−
10 4
−
10 0 10 20 30 40
−
γ¯ (dB)
PEB
exact, (9) with (8) simulation
asymptote (14) quadrature (12)
M = 1, N = 100, d = 0.84
M = 16, N = 6, d = 6
M = 128, N = 1, d = 1
Fig. 2. BEP versus γ¯ under measured 65GHz indoor NLoS fading, κ=1.08 and µ=0.84, at a fixed budget MN 100.
≈
uncertainty below 8%, and points below 10−5 are not simulated. Throughout, curves come from
the analysis and markers from simulation.
Fig. 2 shows the BEP of three configurations under soft combining at an approximately constant
budget MN ≈ 100. Four curve types appear. Solid lines with open markers are (9) evaluated
with the exact conditional BEP (8), and filled markers are the simulated link. Dashed lines are
the asymptote (14), and dotted lines are the quadrature (12).

10
|     | 102 |     | d = Mµ |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | N = 1  |     |     |     |     |     |     |     |
redro
|           |     |     | N = 4  |     |     |     |     |     |     |     |
| --------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|           |     |     | N = 12 |     |     |     |     |     |     |     |
| ytisrevid |     |     | N = 40 |     |     |     |     |     |     |     |
101
100
|     | 100 |     |     |         |     | 101      |     |     |     | 102 |
| --- | --- | --- | --- | ------- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     | receive |     | antennas |     |     | M   |     |
Fig. 3. High-SNR slope of (9) versus M under measured 65GHz indoor NLoS fading, κ=1.08 and µ=0.84. The slope
| tracks Mµ | and then saturates | at N, | confirming | (13). |       |     |     |     |     |     |
| --------- | ------------------ | ----- | ---------- | ----- | ----- | --- | --- | --- | --- | --- |
|           |                    |       |            |       | TABLE | I   |     |     |     |     |
SIMULATIONPARAMETERS
|     |     | Parameter |     |     | Value |              |        |              |           |     |
| --- | --- | --------- | --- | --- | ----- | ------------ | ------ | ------------ | --------- | --- |
|     |     | Signaling |     |     | DBN,  | differential |        | binary, zero | threshold |     |
|     |     | Combining |     |     | soft, | aℓ =1,       | except | in Fig.      | 4         |     |
|     |     | M, N      |     |     | 1 to  | 128 and      | 1 to   | 100, MN      | 100       |     |
≈
|     |     | Frame length |     |     | 100 | symbols | per noise | realization |     |     |
| --- | --- | ------------ | --- | --- | --- | ------- | --------- | ----------- | --- | --- |
κ-µ,
|     |     | Fading        |       |          |         | block    | fading | over two   | symbols |     |
| --- | --- | ------------- | ----- | -------- | ------- | -------- | ------ | ---------- | ------- | --- |
|     |     | 65GHz indoor  | NLoS  |          | κ=1.08, |          | µ=0.84 | [11], [16] |         |     |
|     |     |               |       |          |         | 2        |        | 2/σ        | 2       |     |
|     |     | Branch power, | noise | variance | Ωℓ      | =σ w     | =1, so | γ¯=σ u     | w       |     |
|     |     | SNR grid      |       |          | 10      | to 40dB, | step   | 2.5dB      |         |     |
−
|     |     | Stopping    | rule    |     | 200        | errors,         | floor 10−  | 5        |       |     |
| --- | --- | ----------- | ------- | --- | ---------- | --------------- | ---------- | -------- | ----- | --- |
|     |     | Integration | of (9)  |     | log-domain |                 | grid, step | 0.02     | in ln |     |
|     |     | Quadrature  | of (12) |     | n          | =64 generalized |            | Laguerre | nodes |     |
1
Three observations follow from Fig. 2. First, the analysis matches the simulation over the whole
range and for every configuration, which validates (8) and (9) together. Second, the configurations
differ in slope and not only in offset, and those slopes are the ones (13) predicts, six for M = 16
with N = 6 and one for M = 128 with N = 1. The latter is barely above the single-antenna
link, so 127 extra antennas move the curve sideways rather than tilting it. Third, the asymptote

11
|     |     |     | analysis |     | simulation |     |     |
| --- | --- | --- | -------- | --- | ---------- | --- | --- |
100
random
soft
power
blind
2
10
| PEB | −   |     |     |     |     | genie |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
4
10
−
|     | 10  | 8   | 6   | 4   | 2 0 | 2 4 | 6   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | −   | −   | −   | −   | −   |     |     |
γ¯ (dB)
Fig. 4. Weighting strategies under measured 65GHz indoor NLoS fading, M =4 and N =25.
(14) settles onto the analysis in both slope and constant, to within 1% beyond 24dB, so it can
size a link budget on its own, whereas the quadrature (12) follows the analysis only up to about
| 10dB, | for the reason | given in | Section IV-A. |     |     |     |     |
| ----- | -------------- | -------- | ------------- | --- | --- | --- | --- |
Fig. 3 plots the high-SNR slope of (9) against M for four observation lengths. Each curve
|     | Mµ  |     |     |     | N   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
climbs along and then flattens, and it flattens at the very that produced it, so the four
plateaus are the four observation lengths. That is (13) read off the figure. Antennas set the
diversity order only while Mµ < N, and past the crossing the reused realization sets it, so the
ceiling does not move over more than two decades in M. No array size buys diversity beyond that
point, which is what separates SIMO-DBN from a receiver whose branches carry independent
waveforms.
|     |     |     | M   | = 4 | N = 25, |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
Fig. 4 compares weighting rules for and all sharing the same statistic and
threshold and differing only in a . Soft combining uses a = 1, the square-law (power) rule
|     |     |     | ℓ   |     | ℓ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|2,
a ∝ |h and the random rule draws a from the uniform distribution on [0.05,1] once per
| ℓ   | ℓ   |     | ℓ   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
frame with no knowledge of the channel. The genie rule evaluates the deflection-optimal (15)
with the exact γ , making it a benchmark rather than a receiver, and the blind rule feeds that
ℓ
| same expression | with | the estimate | (17), as | in Algorithm | 1.  |     |     |
| --------------- | ---- | ------------ | -------- | ------------ | --- | --- | --- |
Weighting without knowing the branches is worse than not weighting at all. The random

12
choice falls 1.34dB below soft combining. The genie rule gains 0.70dB, and the square law is
indistinguishable from it, since the average is carried by deep fades, where γ ≪ N/2 and (15)
ℓ
degenerates into a ∝ |h |2. The gain thus comes from the noise floor rather than from the fading.
ℓ ℓ
The blind rule recovers nearly all of it without CSI, so (17) resolves γ finely. The gains are
ℓ
largely unchanged when the average branch powers differ, which suggests that weighting draws
mainly on the instantaneous imbalance within a frame rather than on any persistent asymmetry
between antennas.
VI. CONCLUSION
This paper proposes a receive-diversity scheme for DBN modulation based on generalized
noncoherent decision-statistic combining. Recognizing the combined statistic as a Hermitian
quadratic form in complex Gaussian vectors yields an exact conditional BEP for every observation
length. Averaging it over κ-µ fading and over the reused-energy law gives the exact BEP, validated
against Monte Carlo of the full link. The asymptotic analysis establishes the diversity order
min(Mµ,N). The deflection-optimal combining weights follow in closed form, interpolating
soft combining and power weighting, and a blind version of the same rule attains them without
CSI. Multiple-input single-output (MISO) and space-time extensions remain as future work.
REFERENCES
[1] C.-X. Wang et al., “On the Road to 6G: Visions, Requirements, Key Technologies, and Testbeds,” IEEE Commun. Surv.
Tutor., vol. 25, no. 2, pp. 905–974, Feb. 2023.
[2] Z. Kapetanovic, M. Morales, and J. R. Smith, “Communication by Means of Modulated Johnson Noise,” Proc. of the
National Academy of Sciences, vol. 119, no. 49, Nov. 2022.
[3] E. Basar, “Communication by Means of Thermal Noise: Toward Networks With Extremely Low Power Consumption,”
IEEE Trans. Commun., vol. 71, no. 2, pp. 688–699, Feb. 2023.
[4] ——, “Noise Modulation,” IEEE Wirel. Commun. Lett., vol. 13, no. 3, pp. 844–848, Mar. 2024.
[5] A. A. D. Anjos and H. S. Silva, “On–Off Digital Noise Modulation,” IEEE Wirel. Commun. Lett., vol. 14, no. 11, pp.
3595–3599, Nov. 2025.
[6] A. A. D. Anjos, V. H. F. Braga, H. S. Silva, and R. D. Vieira, “On-Off Digital Noise Modulation: Optimal Likelihood
Threshold and Exact BEP in AWGN and α-µ Fading,” IEEE Wirel. Commun. Lett., vol. 15, pp. 1474–1478, Jan. 2026.
[7] H. Shen, Z. Yang, and Y. Chen, “Channel Estimation via Thermal Noises,” IEEE Wireless Commun. Lett., vol. 14, no. 1,
pp. 178–182, Jan. 2025.
[8] E. Yapici, Y. Islam Tek, and E. Basar, “Noise-Domain Non-Orthogonal Multiple Access,” IEEE Open J. Commun. Soc.,
vol. 6, pp. 8410–8421, Sep. 2025.
[9] H. Zayyani, M. Salman, F. A. P. de Figueiredo, and R. A. A. de Souza, “Spread Spectrum Noise Modulation: Analysis and
Detection,” IEEE Commun. Lett., vol. 30, pp. 1106–1110, 2026.

13
[10] H.Zayyani,F.A.P.D.Figueiredo,M.Salman,andR.A.A.d.Souza,“3-D8-AryNoiseModulationUsingBayesian-and
| Kurtosis-Based | Detectors,” IEEE | Open J. Commun. | Soc., vol. 7, | pp. 3574–3584, 2026. |
| -------------- | ---------------- | --------------- | ------------- | -------------------- |
[11] A. A. d. Anjos, J. a. V. F. Borges, H. S. Silva, and R. D. Vieira, “Differential Binary Noise Modulation,” IEEE Wireless
| Commun. Lett., | vol. 15, pp. | 3746–3750, 2026. |     |     |
| -------------- | ------------ | ---------------- | --- | --- |
Biometrika,
[12] G. L. Turin, “The characteristic function of Hermitian quadratic forms in complex normal variables,” vol. 47,
| no. 1/2, pp. | 199–201, 1960. |     |     |     |
| ------------ | -------------- | --- | --- | --- |
[13] J. G. Proakis and M. Salehi, Digital Communications, 5th ed. New York, NY, USA: McGraw-Hill, 2008.
[14] J. Gil-Pelaez, “Note on the inversion theorem,” Biometrika, vol. 38, no. 3-4, pp. 481–482, 1951.
[15] M. D. Yacoub, “The κ-µ Distribution and the η-µ Distribution,” IEEE Antennas Propag. Mag., vol. 49, no. 1, pp. 68–81,
Feb. 2007.
[16] T. R. R. Marins et al, “Fading Evaluation in the mm-Wave Band,” IEEE Trans. Commun., vol. 67, no. 12, pp. 8725–8738,
Dec. 2019.
---- END DOCUMENT ----
