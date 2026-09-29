Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
tSymPerturb converts longitudinal symptom networks into
time-indexed intervention strategies
Zheng Zhu1,4,*, Junwen Yu2,4, Tiantian Hu1,4, Zhongfang Yang3,4, Jiaqing Wang4
1School of Nursing, Fudan University, Shanghai, China
2NYU Shanghai, Shanghai, China
3School of Nursing, Soochow University, Suzhou, China
4Yulin AI-Enhanced HealthCare Lab, Shanghai, China
*Correspondence: zhengzhu@fudan.edu.cn
Abstract
Longitudinal symptom networks encode directed prediction across measurement occasions,
but outgoing connectivity does not by itself identify which symptom should be modified, how
strongly it should be changed, or how a perturbation would propagate to later symptoms. We
introduce tSymPerturb, a temporal extension of SymPerturb for cross-lagged panel networks
(CLPNs). The framework separates source-state operators (temporal virtual knockout and
knockdown), transition operators (directed edge and source-node communication blocking), and
strategy procedures (dosage perturbation, combination analysis and sequence optimisation). For
a two-wave linear CLPN, the central propagation identity is ∆µ =B(µ −µ∗), which makes
2 1 1
the source time, outcome time and transition operator explicit. The formulation also yields three
falsification constraints: dose response is exactly linear under a fixed linear transition model
and linear dose map; independent source-state perturbations are additive at the mean level; and
genuine treatment order is not identified from a single two-wave transition. In a known 22-node,
four-modulegeneratingsystem,analyticaltemporal-knockoutresponsesagreedwith250,000-draw
Monte Carlo estimates within 0.0057 standard deviations. Across 200 independently generated
datasets, median Spearman correlation with the population tVPPS ranking increased from 0.76
atn=250to0.88atn=500and0.93atn=1,000; mediantop-fiverecoverywas0.60,0.80and0.80,
respectively. Multi-wave simulations showed that target profiles can change across propagation
horizons despite high overall rank concordance. tSymPerturb therefore converts longitudinal
network structure into auditable, time-indexed intervention hypotheses while retaining the
distinction between prediction and causal treatment effects.
1 Introduction
Network models have changed how multivariate symptom systems are represented. Rather than
treating symptoms only as interchangeable indicators of a latent disorder, network models represent
symptoms as mutually related components whose structure can be studied at a single occasion or
across time [1–4]. Cross-lagged panel networks extend this logic to panel data by estimating how a
symptom at an earlier occasion predicts itself and other symptoms at a later occasion, conditional
on the remaining source variables [3,4]. This directional representation is appealing for symptom
management because it appears to provide a temporal basis for identifying candidate intervention
targets.
However, directional prediction and intervention value are not the same quantity. Outgoing
strength or expected influence describes the fitted transition structure; it does not quantify how
1
6202
guA
71
]MQ.oib-q[
1v66361.8062:viXra

much later symptom burden would change if a baseline symptom were modified, whether a feasible
partial change would preserve the same ranking, whether a target acts mainly through persistence
or cross-symptom spillover, or which directed pathways account for the predicted benefit. The
distinction becomes especially important when autoregressive paths are large, when the source
symptoms have different modifiable ranges, or when positive and negative cross-lagged paths coexist.
The original SymPerturb framework formalised virtual perturbation for cross-sectional symptom
networks by separating primitive perturbation operators from procedures that evaluate intensity,
combinations and target sequences. Its central limitation is also explicit: an undirected cross-
sectional graph does not contain temporal ordering, and a statistical perturbation of that graph
is not an identified causal intervention. Longitudinal networks provide a different mathematical
object. A fitted CLPN is a directed mapping from a source state at T1 to an outcome state at T2.
The virtual-perturbation question can therefore be written as a forward propagation query: what
does the fitted transition model predict at T2 after a prespecified modification of the T1 state or of
the T1→T2 transition process?
This temporal formulation does not automatically solve causal identification. Cross-lagged
coefficients remain regression parameters that can be affected by stable between-person differences,
measurement error, omitted causes and the selected time interval [5,6]. Wysocki and colleagues
explicitly recommend interpreting CLPN paths in predictive rather than causal terms [3]. tSym-
Perturb therefore uses intervention language only to define transparent model operations. The
output is a model-implied target hypothesis that requires longitudinal triangulation, measured
target engagement and experimental validation before it can be interpreted as a treatment effect.
Here we introduce tSymPerturb as a methods framework for longitudinal symptom networks.
We first define temporal state and transition operators, then derive their response functions in a
two-wave linear CLPN, distinguish total downstream benefit from cross-symptom spillover, formalise
seven non-redundant target-level utility outcomes, and extend the framework to combinations and
multi-wave sequences. We then use a known 22-node, four-module transition system to verify
the analytical equations, quantify finite-sample recovery and expose three conditions under which
seemingly attractive findings—nonlinear dosage curves, additive synergy and two-wave treatment-
order claims—are mathematically unsupported by the reference model.
2 The tSymPerturb architecture
tSymPerturb is organised into a source-state layer, a transition layer and a strategy layer (Fig. 1).
The source-state layer contains temporal virtual knockout (t-vKO), which anchors a T1 symptom to
a prespecified state, and temporal virtual knockdown (t-vKD), which produces a partial movement
toward that anchor. Temporal virtual dosage perturbation (t-vDP) evaluates a response curve
generated by a state operator. The transition layer contains directed edge-level communication
blocking and source-node-centred communication blocking, which attenuate one T1→T2 coefficient
or all outgoing coefficients from a selected source node. The strategy layer contains combination
perturbation and sequence optimisation. The latter has two distinct meanings: target-acquisition
order can be studied in a two-wave decision problem, whereas repeated temporal intervention order
requires at least a multi-step transition model or an explicit stationarity assumption.
Table 1. Components of tSymPerturb and the questions they answer.
Component Reference action Mathematical role and primary question
2

Temporal virtual Anchor source symptom i Primitive state operator: what is the predicted
knockout (t-vKO) at c downstream response to complete source-state
i
anchoring?
Temporal virtual Partially move source Primitive state operator: what response follows
knockdown (t-vKD) symptom i toward c i a feasible partial source change?
Temporal virtual Evaluate G (d) over Intensity-response procedure: is any apparent
i
dosage perturbation d ∈ [0,1] nonlinearity attributable to the specified model
| (t-vDP) |     |     |     |     |     |     | rather | than | the CLPN | alone? |     |
| ------- | --- | --- | --- | --- | --- | --- | ------ | ---- | -------- | ------ | --- |
Directed edge B∗ = (1−q)B Primitive transition operator: how dependent is
|               |     |     | ji  |     | ji  |     |            |            |     |                 |          |
| ------------- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --------------- | -------- |
| communication |     |     |     |     |     |     | a selected | prediction |     | on one directed | pathway? |
block
Source-node Attenuate the outgoing Primitive transition operator: how much
communication column B finite-horizon propagation depends on one
·i
| block |     |     |     |     |     |     | source | node? |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- |
Combination Apply a joint source-state Joint-target construction: what incremental
perturbation operator to S value does an additional target contribute
|     |     |     |     |     |     |     | beyond | the | better | single target? |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | -------------- | --- |
Sequence Optimise ordered target Decision procedure: which feasible order
optimisation acquisition or repeated maximises a prespecified temporal objective
|     |     | interventions |     |     |     |     | under | explicit | assumptions? |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | ----- | -------- | ------------ | --- | --- |
3 A temporal source-state intervention with virtual knockout as an
endpoint
|     | Rp  | Rp  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let X ∈ and X ∈ denote the symptom vectors at two consecutive occasions. The reference
| 1   |     | 2   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CLPN is
|     |     | X = | a+BX | +ε, |     | E(ε) | = 0, | Var(ε) | =   | Ψ. (1) |     |
| --- | --- | --- | ---- | --- | --- | ---- | ---- | ------ | --- | ------ | --- |
|     |     | 2   |      | 1   |     |      |      |        |     |        |     |
where B is the coefficient from source symptom i at T1 to outcome symptom j at T2. Diagonal
ji
elements represent autoregressive persistence and off-diagonal elements represent cross-symptom
prediction. The baseline mean is µ = a+Bµ . A state perturbation changes the source distribution
|     |     |     |     | 2   |     | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whilekeepingBfixed. ForatargetsetSwithclinicallymeaningfulanchorsc ,agenerallocation-scale
S
map is
|     |     | X (d) | = c | +D (d)(µ |     | −c )+D | (d)(X |     | −µ  | ). (2) |     |
| --- | --- | ----- | --- | -------- | --- | ------ | ----- | --- | --- | ------ | --- |
|     |     | 1,S   | S   | µ        | 1,S | S      | σ     | 1,S | 1,S |        |     |
with non-target source variables unchanged. The post-perturbation follow-up mean is µ (d) =
2
| a+Bµ (d), | so  | the model-implied |     | downstream |     | improvement |     | is  |     |     |     |
| --------- | --- | ----------------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- |
1
|     |     |     |     |       |      |       | h      | i   |       |     |     |
| --- | --- | --- | --- | ----- | ---- | ----- | ------ | --- | ----- | --- | --- |
|     |     |     | R   | (d) = | µ −µ | (d) = | B µ −µ | (d) | . (3) |     |     |
|     |     |     |     | S     | 2    |       | 1      |     |       |     |     |
|     |     |     |     |       |      | 2     |        | 1   |       |     |     |
Equation (3) is the central temporal propagation identity. It replaces the cross-sectional re-
equilibration query with an explicitly time-indexed forward mapping. For one target i anchored at
| c , the t-vKO | mean | response |     | is  |     |     |     |     |     |     |     |
| ------------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
RvKO
|     |     |     |     |     | =   | B ·i (µ | 1,i −c i ). | (4) |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- | --- |
i
3

Figure 1: The tSymPerturb workflow. Source-state operators alter the symptom state at the source
occasion; transition operators alter the fitted T1→T2 mapping; strategy procedures combine or
order candidate interventions. Seven target-level utility outcomes are used for within-analysis
prioritisation, while uncertainty is reported separately. All quantities are model-implied and do not
represent identified treatment effects.
4

This response depends jointly on the modifiable distance from the source state to the anchor
and on the outgoing transition profile. Unlike exact knockout in a cross-sectional covariance model,
t-vKO does not require re-estimating a covariance matrix containing a zero-variance column. The
fitted transition model is estimated once and then queried. Re-fitting a CLPN after replacing a
predictor by a constant would answer a different question and may create rank deficiency.
| 4 Seven  | components |     | and    | longitudinal-specific |     | constraints |     |
| -------- | ---------- | --- | ------ | --------------------- | --- | ----------- | --- |
| Temporal | knockdown  | and | dosage | perturbation          |     |             |     |
A partial knockdown uses d ∈ (0,1) to move the source state toward its anchor. Under the linked
reference map X∗ = c +(1−d)(X −c ), the mean source improvement is d(µ −c ), giving
|     | 1,i | i   | 1,i   | i             |     |     | 1,i i |
| --- | --- | --- | ----- | ------------- | --- | --- | ----- |
|     |     |     | R (d) | = dB (µ −c ). | (5) |     |       |
|     |     |     | i     | ·i 1,i i      |     |     |       |
Consequently, when B is fixed and the outcome functional is linear, G (d) = dG (1). Dose
i i
efficiency and low-dose responsiveness are then algebraically equivalent to efficacy. t-vDP is therefore
retained as an intensity-response procedure but these redundant summaries are not counted as
separatedimensionsoftheconfirmatorytVPPS.Thresholdsorsaturationrequireadditionalstructure,
such as bounded measurement, a nonlinear dose map, interactions, state-dependent coefficients or
| nonlinear | transition functions. |     |          |     |     |     |     |
| --------- | --------------------- | --- | -------- | --- | --- | --- | --- |
| Directed  | communication         |     | blocking |     |     |     |     |
State perturbation changes X ; communication blocking changes B. For a directed pathway i(T1) →
1
| j(T2), a | block fraction | q ∈ [0,1] | gives   |              |     |     |     |
| -------- | -------------- | --------- | ------- | ------------ | --- | --- | --- |
|          |                |           | B∗(i→j) | = B−qB e e⊤. | (6) |     |     |
ji j i
A source-node block attenuates the outgoing transition column B . In individual-level or
·i
clinically anchored predictions, this operator quantifies dependence of future symptom burden on
the selected predictive pathway. When predictors are centred, communication-block effects must
be evaluated at an explicit reference state; otherwise the average signed change can be zero by
construction. For target-level scoring, the reference implementation uses the relative loss of a
| finite-horizon | propagation  | functional | after | 80% source-node | blocking. |     |     |
| -------------- | ------------ | ---------- | ----- | --------------- | --------- | --- | --- |
| Combination    | perturbation |            |       |                 |           |     |     |
For two independently perturbed source symptoms i and k under the linear reference model, the
joint mean response is R = R i +R k . Thus the additive interaction contrast G −G i −G k
|     |     | {i,k} |     |     |     |     | {i,k} |
| --- | --- | ----- | --- | --- | --- | --- | ----- |
is exactly zero. A two-wave linear CLPN cannot generate statistical synergy merely because two
baseline states are modified together. tSymPerturb instead reports combination value relative to
the better single target and retains the additive contrast as a diagnostic. Non-zero non-additivity
must arise from an explicitly nonlinear element of the model, outcome function or state-update rule.
| Sequence | optimisation |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- |
Two-wave and multi-wave sequence questions are deliberately separated. A two-wave model can rank
the order in which candidate targets are added to a constrained intervention set, but it contains only
one observed transition and therefore does not identify a biological treatment sequence. Repeated
5

temporal sequencing requires additional observed waves or a stated stationarity assumption under
which the fitted transition operator is reused. This distinction prevents an optimisation algorithm
| from being | misreported | as evidence |     | of treatment | timing. |     |       |     |
| ---------- | ----------- | ----------- | --- | ------------ | ------- | --- | ----- | --- |
| 5 Seven    | utility     | outcomes,   |     | uncertainty  |         | and | tVPPS |     |
For target i, let ∆ (d) denote the standardised predicted improvement in outcome j after a
j←i
source-state perturbation. tSymPerturb distinguishes total downstream efficacy, which includes
the autoregressive outcome, from cross-symptom spillover, which excludes it. Seven non-redundant
utility outcomes are retained for the reference two-wave tVPPS (Table 2). Robustness is treated as
| uncertainty | rather | than utility | and is | reported | separately. |     |     |     |
| ----------- | ------ | ------------ | ------ | -------- | ----------- | --- | --- | --- |
Table 2. Seven target-level utility outcomes used in the reference tVPPS.
| Outcome |     | Reference | definition |     |     | Interpretation |     |     |
| ------- | --- | --------- | ---------- | --- | --- | -------------- | --- | --- |
Downstream Mean ∆ (1) over all T2 Overall predicted follow-up burden reduction,
j←i
efficacy outcomes including persistence of the target itself.
Cross-symptom Mean ∆ (1), j ̸= i Predicted benefit that propagates beyond the
j←i
| spillover |     |     |     |     |     | target symptom. |     |     |
| --------- | --- | --- | --- | --- | --- | --------------- | --- | --- |
Breadth Share of j ̸= i with Proportion of subsequent symptoms
|     |     | ∆ ≥ | 0.05 SD |     |     | exceeding | a prespecified | improvement |
| --- | --- | --- | ------- | --- | --- | --------- | -------------- | ----------- |
j←i
threshold.
Cross-module Share of other modules with Extent to which the predicted response
| reach |     | mean improvement |     | ≥   | 0.03 | reaches | other symptom | domains. |
| ----- | --- | ---------------- | --- | --- | ---- | ------- | ------------- | -------- |
SD
Communication- Relative loss of a Dependence of the directed transition system
block value finite-horizon |B|-propagation on the source node.
|     |     | functional | after | 80% source |     |     |     |     |
| --- | --- | ---------- | ----- | ---------- | --- | --- | --- | --- |
blocking
Combination value Mean incremental pair value Additional value beyond the better single
|     |     | over a prespecified |     | partner | set | target; | not causal synergy. |     |
| --- | --- | ------------------- | --- | ------- | --- | ------- | ------------------- | --- |
Spillover fraction Positive non-target response Fraction of beneficial response that is
divided by total positive distributed beyond autoregressive target
|     |     | response |     |     |     | persistence. |     |     |
| --- | --- | -------- | --- | --- | --- | ------------ | --- | --- |
Each raw outcome R is direction-aligned and min–max normalised across the prespecified
im
candidate set. If a dimension is constant it contributes a neutral score of 50. The reference temporal
| virtual | perturbation | priority score | is  |     |     |     |     |     |
| ------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- |
P
|     |     |       |     | ω   | score |     |          |     |
| --- | --- | ----- | --- | --- | ----- | --- | -------- | --- |
|     |     | tVPPS | =   | m m | im ,  | ω   | ≥ 0. (7) |     |
|     |     |       | i   | P   |       | m   |          |     |
ω
m m
Equal weights are used only for methodological verification. They are not patient utilities and do
not make tVPPS transportable across cohorts. Applied work should report the seven-dimensional
profile beside tVPPS and pre-specify any clinically informed weights. Because normalisation is
within the analysed candidate set, tVPPS is a relative prioritisation score rather than an absolute
| treatment-benefit |     | scale. |     |     |     |     |     |     |
| ----------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
6

6 Internal computational verification and finite-sample recovery
We generated a known 22-node transition system with four symptom modules. The matrix
contained 53 non-zero off-diagonal transitions, of which 47 were positive and 6 negative, together
with heterogeneous autoregressive coefficients ranging from 0.43 to 0.71. The spectral radius of B
was 0.827, allowing a stable stationary extension for the multi-wave stress test. Baseline means
ranged from 1.44 to 2.64, baseline standard deviations from 0.63 to 0.83, and residual standard
deviations from 0.38 to 0.52. Population outcomes were calculated from the known generating
| parameters | before | any data | were sampled. |     |     |     |     |
| ---------- | ------ | -------- | ------------- | --- | --- | --- | --- |
Analytical t-vKO responses closely matched direct simulation. Across 22 targets and 250,000
Monte Carlo draws per target, the maximum absolute discrepancy in any standardised T2 outcome
was 0.0057 SD. Target-level analytical and Monte Carlo efficacy values had Pearson r=0.99991,
with a maximum absolute efficacy discrepancy of 0.0013 SD (Fig. 2a). This verifies the forward
propagation implementation under model compatibility; it does not establish the clinical validity of
| the target | anchors | or the | transition model. |     |     |     |     |
| ---------- | ------- | ------ | ----------------- | --- | --- | --- | --- |
Finite-sample recovery improved monotonically with sample size. Across 200 independently
generated datasets at each n, the median Spearman correlation between estimated and population
tVPPS ranks was 0.76 at n=250, 0.88 at n=500 and 0.93 at n=1,000 (Fig. 2b and Table 3). The
corresponding 95% Monte Carlo intervals were 0.58–0.88, 0.74–0.95 and 0.85–0.98. Median top-five
recovery increased from 0.60 to 0.80 and 0.80, while tVPPS RMSE decreased from 13.94 to 9.47
| and 6.39 | points on | the 0–100 | scale (Fig. | 2c). |     |     |     |
| -------- | --------- | --------- | ----------- | ---- | --- | --- | --- |
Outcome-specific recovery was heterogeneous (Fig. 2d). Efficacy, cross-symptom spillover,
communication-block value, combination value and spillover fraction were recovered well by n=500,
with median rank correlations of 0.90 or higher for all except cross-module reach. Threshold-based
breadth was the least stable component, with median rank recovery of 0.41, 0.60 and 0.80 across
n=250, 500 and 1,000. This pattern supports reporting the raw utility profile and complete-pipeline
| uncertainty | rather | than treating | the | composite rank | as error-free. |     |     |
| ----------- | ------ | ------------- | --- | -------------- | -------------- | --- | --- |
Table 3. Finite-sample recovery of the seven-dimension tVPPS. Intervals are the 2.5th and 97.5th
| percentiles | across      | 200 independently |        | generated datasets. |          |                    |     |
| ----------- | ----------- | ----------------- | ------ | ------------------- | -------- | ------------------ | --- |
| Sample      | size Median | tVPPS             | ρ (95% | Median              | top-five | Median RMSE,       |     |
|             | MC          | interval)         |        | recovery            | (95% MC  | 0–100 (95%         | MC  |
|             |             |                   |        | interval)           |          | interval)          |     |
| 250         | 0.76        | (0.58–0.88)       |        | 0.60 (0.40–0.80)    |          | 13.94 (9.81–18.46) |     |
| 500         | 0.88        | (0.74–0.95)       |        | 0.80 (0.60–1.00)    |          | 9.47 (6.58–13.11)  |     |
| 1,000       | 0.93        | (0.85–0.98)       |        | 0.80 (0.60–1.00)    |          | 6.39 (4.10–9.25)   |     |
At the population level, Fatigue ranked first (tVPPS=100.0), followed by Rumination (84.6),
Anxiety(61.3),Pain(61.3)andAnhedonia(52.2). Therankingwasnotreducibletobaselinesymptom
burden: Pain had high total efficacy but a smaller spillover fraction than Fatigue or Rumination,
whereas Rumination combined broad cross-module reach with strong transition dependence. These
labels identify the intentionally constructed synthetic nodes and must not be interpreted as clinical
recommendations.
7

Figure 2: Internal verification and finite-sample recovery in model-compatible longitudinal networks.
a, Analytical versus Monte Carlo t-vKO efficacy for 22 targets. b, Distribution of tVPPS rank
correlation across 200 independently generated datasets at each sample size. c, Proportion of the
population top five recovered. d, Median outcome-specific rank recovery. Monte Carlo intervals
quantify simulation-to-simulation variability under the specified generating system and are not
patient-level confidence intervals.
8

7 Temporal validity, multi-wave propagation and benchmark con-
trasts
The reference linear model satisfied the two main algebraic falsification checks to numerical precision.
Across all 22 targets and six dose levels, the maximum deviation from G (d) = dG (1) was 2.78e-17.
i i
Across all 231 target pairs, the maximum absolute deviation from joint additivity was 2.78e-17.
Thus, any visibly nonlinear dosage curve or non-additive pair effect produced by the unbounded
two-wave reference implementation would indicate a coding error or the introduction of an additional
nonlinear operation rather than a property learned from the CLPN itself (Fig. 3a,b).
The multi-wave extension produced a distinct longitudinal result. Reusing the known stable
transition matrix over four waves changed the relative target profiles even though ranks remained
broadly concordant. The one-step and four-step efficacy ranks correlated at ρ=0.88; the correlation
between one-step efficacy and discounted four-wave cumulative efficacy was ρ=0.94. Fatigue was the
highest one-step target, whereas Rumination became the highest four-step target; Insomnia entered
the top five after the first transition (Fig. 3c). This illustrates why one-step outgoing influence and
persistent longitudinal leverage are not interchangeable.
Under an exploratory stationary repeated-intervention simulation restricted to the eight highest
populationtVPPScandidates,thehighestdiscountedtwo-steputilitywasobtainedforFatigue→Pain
(U=0.592), compared with U=0.527 for the reverse order. The order sensitivity for this pair was
0.065. Because the same transition matrix was reused beyond the observed two-wave interval, this
result is a strategy simulation under stationarity, not evidence that the sequence should be used
clinically. In the pure two-wave target-acquisition problem without state updating or constraints,
cumulative utility was order invariant as required.
tVPPS was associated with conventional longitudinal centrality but was not identical to it.
Population tVPPS rank correlated with absolute outgoing-strength rank at ρ=0.80 and signed
outgoing expected-influence rank at ρ=0.89; only 60% of the top five targets overlapped with either
outgoing-strength top five. Baseline burden alone had a much weaker association with tVPPS
(ρ=0.16; top-five overlap 40%). The contrast shows that tSymPerturb combines source modifiability,
directed response, module reach and strategy value rather than reproducing a single centrality
statistic (Fig. 3d).
8 Discussion
tSymPerturb extends virtual perturbation from contemporaneous symptom structure to explicitly
time-indexed prediction. Its central contribution is not another centrality statistic. The framework
specifies the object being perturbed, the temporal location of that perturbation, the rule by which
the fitted system is updated and the outcome functional used to judge the response. Source-state
operators ask what the fitted CLPN predicts after a change in the earlier symptom state. Transition
operators ask how much later prediction depends on a directed pathway. Combination and sequence
procedures then construct intervention strategies from those primitive operations.
The mathematical formulation clarifies several quantities that are easy to overinterpret in
applied longitudinal network studies. First, a T1 symptom with large outgoing coefficients is not
automatically the best intervention target because the model-implied response also depends on its
distance from a clinically meaningful anchor and on the outcomes reached by those coefficients.
Second, autoregressive persistence and cross-symptom propagation answer different questions. A
target can reduce its own future burden strongly while having little spillover, or it can have a smaller
total effect but a larger fraction of benefit distributed across other symptoms. Third, communication
9

Figure 3: Longitudinal-specific validity checks and contrasts. a, The unbounded linear reference
model lies on the analytical dose-response identity. b, Joint two-target state perturbations lie on
the additive identity. c, Model-implied target efficacy across four repeated transition horizons under
the stationary extension. d, Population tVPPS rank versus absolute outgoing-strength rank. The
multi-wave and sequence analyses are simulations under the specified transition model, not identified
treatment policies.
10

blocking is a transition-model operation. It should not be interpreted as evidence that symptoms
literally transmit a biological signal.
The simulation results support the internal coherence of the framework while also defining
sample-size limitations. Analytical and Monte Carlo responses agreed closely, and population
rankings were increasingly recovered as n increased. Nevertheless, at n=250 the 95% Monte Carlo
interval for tVPPS rank recovery extended from 0.58 to 0.88 and top-five recovery could be as low
as 0.40. Breadth was particularly unstable because a threshold converts small coefficient errors into
discrete changes in the count of affected symptoms. These findings argue against reporting only a
single target rank. Applied analyses should propagate uncertainty through estimation, perturbation,
normalisation and ranking, then report rank distributions and top-k selection probabilities beside
the point estimate.
Three null results are as important as the positive validation. In the reference linear CLPN,
dosage response is linear, independent source perturbations are additive and a two-wave model
contains no empirical information about repeated treatment order. These are not inconveniences
to be hidden by a more elaborate score. They are falsification constraints. A sigmoid dosage
curve, pairwise synergy or strong order sensitivity can be scientifically meaningful only when the
analysis explicitly introduces the mechanism that can generate it—for example bounded outcomes,
nonlinear transitions, interactions, state-dependent coefficients, intervention constraints or observed
multi-wave transitions.
The multi-wave extension illustrates the additional information that becomes available when a
transition process is iterated. In the synthetic system, one-step and four-step ranks were similar
but not identical; a target that was not among the strongest immediate candidates became more
prominent at later horizons. This distinction is important for chronic symptom management, where
an intervention may have modest immediate benefit yet alter a downstream cascade over several
assessment intervals. However, repeating one estimated B matrix assumes temporal stationarity.
When three or more empirical waves are available, wave-specific matrices B should be used unless
t
invariance is supported.
Several limitations define the scope of the present claims. The verification uses a continuous
Gaussian generating system with a sparse linear transition matrix and a fixed lasso penalty.
It does not establish performance for strongly ordinal or zero-inflated symptoms, non-random
dropout, measurement non-invariance, latent time-varying confounding, heterogeneous person-
specific dynamics or high-dimensional p/n regimes. The seven tVPPS dimensions are methodological
utilities rather than validated clinical preference weights. The target anchor, burden weights and
thresholdsforbreadthandmodulereachareanalysischoices. Mostimportantly,temporalprecedence
within a CLPN does not identify causal treatment effects [5,6,16].
A credible translational pathway should therefore proceed in stages. The first is expanded
computational validation across data types, estimators, missingness mechanisms, nonlinearity and
time-varying transition matrices. The second is longitudinal triangulation, asking whether naturally
occurring or treatment-induced changes in high-ranked source symptoms precede the downstream
pattern predicted by tSymPerturb. The third is experimental validation with measured target
engagement, followed by prospective decision studies that incorporate safety, feasibility, cost, equity
and patient preference. Used within these boundaries, tSymPerturb can narrow a target set and
make temporal intervention assumptions testable; it cannot replace a trial.
11

9 Methods
| 9.1 | Reference | two-wave |     | transition |     | model |     |     |     |     |     |
| --- | --------- | -------- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
|     |           |          | )⊤  |            |     |       |     | )⊤  |     |     |     |
Let X = (X ,...,X and X = (X ,...,X denote the same p symptoms measured at
|     | 1   | 1,1 | 1,p |     | 2   | 2,1 | 2,p |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two ordered occasions. The reference cross-lagged panel network (CLPN) is written as a multivariate
| transition |     | model    |     |      |     |     |        |      |       |          |     |
| ---------- | --- | -------- | --- | ---- | --- | --- | ------ | ---- | ----- | -------- | --- |
|            |     | X = a+BX | +ε, | E(ε) | =   | 0,  | Var(ε) | = Ψ, | Cov(X | ,ε) = 0. | (8) |
|            |     | 2        | 1   |      |     |     |        |      |       | 1        |     |
The coefficient B is the directed path from source symptom i at T1 to outcome symptom j
ji
at T2. The diagonal B contains autoregressive persistence and the off-diagonal elements contain
ii
cross-symptom prediction. If E(X ) = µ and Var(X ) = Σ , the first two moments at follow-up
|        |          |                |                  |              | 1     | 1    |          | 1   | 1    |     |     |
| ------ | -------- | -------------- | ---------------- | ------------ | ----- | ---- | -------- | --- | ---- | --- | --- |
| follow | directly | from           | linear           | propagation: |       |      |          |     |      |     |     |
|        |          |                |                  | µ            | = E(X | ) =  | a+Bµ     | ,   | (9)  |     |     |
|        |          |                |                  |              | 2     | 2    |          | 1   |      |     |     |
|        |          |                |                  | Σ =          | Var(X | ) =  | BΣ B⊤+Ψ. |     | (10) |     |     |
|        |          |                |                  | 2            |       | 2    | 1        |     |      |     |     |
|        | The      | source–outcome | cross-covariance |              |       | is   |          |     |      |     |     |
|        |          |                |                  | Cov(X        |       | ,X ) | = Σ B⊤.  |     | (11) |     |     |
|        |          |                |                  |              |       | 1 2  | 1        |     |      |     |     |
Equations (9)–(11) are important because tSymPerturb operates on an already fitted transition
operator. A state perturbation changes the distribution entering B; a communication-block pertur-
bation changes B itself. The two operations therefore answer different estimands and should not be
implemented by repeatedly refitting the CLPN after every hypothetical intervention.
| 9.2 | Clinical | anchors |     | and scale | transformation |     |     |     |     |     |     |
| --- | -------- | ------- | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
Every symptom was oriented so that larger values represented worse states. Let c i denote a clinically
interpretable source-state anchor for symptom i. The anchor is defined on the original measurement
| scale | before | standardisation. |     | If a fitted | CLPN |     | uses |     |     |     |     |
| ----- | ------ | ---------------- | --- | ----------- | ---- | --- | ---- | --- | --- | --- | --- |
X −µ
|     |     |     |     |     |     |     | 1,i | 1,i |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | Z   | =   |     | ,   |     |     |     |
|     |     |     |     |     |     | 1,i | σ   |     |     |     |     |
1,i
|     | then | the corresponding |     | anchor | on the | fitted | scale | is  |     |     |     |
| --- | ---- | ----------------- | --- | ------ | ------ | ------ | ----- | --- | --- | --- | --- |
c −µ
|     |     |     |     |     |       | i   | 1,i |      |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |     | c i,z | =   | .   | (12) |     |     |     |
σ
1,i
Thus, when symptom absence is coded as c = 0, a standardised value of zero is generally not a
i
knockout state; it is the sample mean. This transformation was repeated inside each finite-sample
replicate so that sampling variability in the estimated mean and standard deviation propagated
| into | the | perturbation | analysis. |     |     |     |     |     |     |     |     |
| ---- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
12

| 9.3 General |     | temporal |     | location–scale |     | state | intervention |     |     |     |     |
| ----------- | --- | -------- | --- | -------------- | --- | ----- | ------------ | --- | --- | --- | --- |
Let S be a target set and let K denote the complementary set of non-target source symptoms. A
general temporal intervention may alter the target mean and target scale separately. For target
| vector X | , define |     |     |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1,S
(d)
|     |     | X   | =   | c +D | (d)(µ | −c  | )+D | (d)(X | −µ ),   | (13) |     |
| --- | --- | --- | --- | ---- | ----- | --- | --- | ----- | ------- | ---- | --- |
|     |     |     | 1,S | S    | µ     | 1,S | S   | σ     | 1,S 1,S |      |     |
where D (d) and D (d) are diagonal intervention maps. Baseline recovery requires D (0) =
|     | µ   |     | σ   |     |     |     |     |     |     |     | µ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D (0) = I. An exact anchor intervention requires D (1) = D (1) = 0 in the reference implementa-
| σ              |     |      |         |     |                   |     | µ      |      | σ   |     |     |
| -------------- | --- | ---- | ------- | --- | ----------------- | --- | ------ | ---- | --- | --- | --- |
| tion. Equation |     | (13) | implies | the | post-perturbation |     | target | mean |     |     |     |
(d)
|     |     |     |     | µ   | = c S | +D µ (d)(µ | 1,S | −c S | ), (14) |     |     |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | ---- | ------- | --- | --- |
1,S
| and target |     | covariance |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(d)
|     |     |     |     | Σ   | =    | D (d)Σ | D    | (d)⊤. | (15) |     |     |
| --- | --- | --- | --- | --- | ---- | ------ | ---- | ----- | ---- | --- | --- |
|     |     |     |     |     | 1,SS | σ      | 1,SS | σ     |      |     |     |
Because non-target source symptoms are left unchanged, their covariance remains Σ , while
1,KK
target–non-target cross-covariances are attenuated only through the target scale map. Ordering the
| source vector |     | as (K,S) | gives |     |      |      |      |        |        |     |     |
| ------------- | --- | -------- | ----- | --- | ---- | ---- | ---- | ------ | ------ | --- | --- |
|               |     |          |       | "   |      |      |      |        | #      |     |     |
|               |     |          |       |     | Σ    |      | Σ    | D (d)⊤ |        |     |     |
|               |     |          | (d)   |     | 1,KK |      | 1,KS | σ      |        |     |     |
|               |     |          | Σ     | =   |      |      |      |        | . (16) |     |     |
|               |     |          | 1     | D   | (d)Σ | D    | (d)Σ | D      | (d)⊤   |     |     |
|               |     |          |       |     | σ    | 1,SK | σ    | 1,SS   | σ      |     |     |
Substituting the perturbed source moments into the longitudinal transition gives
|     |     |     |     |     | (d)   |          | (d)   |     |      |     |     |
| --- | --- | --- | --- | --- | ----- | -------- | ----- | --- | ---- | --- | --- |
|     |     |     |     |     | µ     | = a+Bµ   |       | ,   | (17) |     |     |
|     |     |     |     |     | 2     |          | 1     |     |      |     |     |
|     |     |     |     |     | Σ (d) | = BΣ (d) | B⊤+Ψ. |     | (18) |     |     |
|     |     |     |     |     | 2     | 1        |       |     |      |     |     |
The mean downstream improvement induced by perturbing S is therefore
|     |     |     |     |         |       |      | (cid:16) |      | (cid:17) |     |     |
| --- | --- | --- | --- | ------- | ----- | ---- | -------- | ---- | -------- | --- | --- |
|     |     |     |     |         |       | (d)  |          |      | (d)      |     |     |
|     |     |     |     | R S (d) | = µ 2 | −µ = | B µ      | 1 −µ | . (19)   |     |     |
|     |     |     |     |         |       | 2    |          |      | 1        |     |     |
Equation (19) is the central longitudinal propagation identity. It shows explicitly that the effect
is jointly determined by the amount of source-state change and by the fitted transition operator.
The corresponding covariance equation (18) is retained because a location-only intervention and a
linked location–scale intervention can have identical mean responses but different uncertainty and
| bounded-scale |     | behaviour. |     |          |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 9.4 Temporal  |     | virtual    |     | knockout |     |     |     |     |     |     |     |
For one target i, temporal virtual knockout (t-vKO) is the unit-dose endpoint of the state operator.
| In the reference |     | implementation, |     |               |          |     |               |     |           |     |     |
| ---------------- | --- | --------------- | --- | ------------- | -------- | --- | ------------- | --- | --------- | --- | --- |
|                  |     |                 |     | (cid:16) XvKO | (cid:17) |     | (cid:16) XvKO |     | (cid:17)  |     |     |
|                  |     |                 |     | E             | =        | c , | Var           |     | = 0. (20) |     |     |
|                  |     |                 |     | 1,i           |          | i   |               | 1,i |           |     |     |
Let δ = µ −c be the modifiable distance from the observed source mean to the anchor.
|     | i   | 1,i | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Because only coordinate i changes in the source mean, equation (19) reduces to
|     |     |     |     |     | RvKO | =   | B δ , | (21) |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ----- | ---- | --- | --- | --- |
|     |     |     |     |     |      | i   | ·i i  |      |     |     |     |
13

where B is column i of B. The outcome-specific standardised improvement is
·i
|     |     |     |     |     |     |      | B   | δ   |      |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |     |     | ∆vKO | ji  | i   |      |     |     |     |
|     |     |     |     |     |     |      | =   | ,   | (22) |     |     |     |
|     |     |     |     |     |     | j←i  | s   |     |      |     |     |     |
2,j
p
where s = Σ is the unperturbed follow-up standard deviation. Equation (22) makes the
|     |     | 2,j | 2,jj |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distinction from outgoing centrality explicit: a large |B ji | does not guarantee a large perturbation
effect when δ is small, and a large source burden does not guarantee leverage when the outgoing
i
| transition | profile |     | is weak | or sign-cancelling. |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
An exact t-vKO does not require re-estimation of B. The fixed source value is passed through
the already fitted transition equation. If a new CLPN were instead refitted after exact knockout,
the target predictor would have zero variance and the refitted design matrix could become rank
deficient; that procedure answers a different question and was not used here.
| 9.5 Temporal |     | virtual |     | knockdown |     | and | dosage |     | perturbation |     |     |     |
| ------------ | --- | ------- | --- | --------- | --- | --- | ------ | --- | ------------ | --- | --- | --- |
Temporal virtual knockdown (t-vKD) uses a partial dose d ∈ (0,1). The linked reference map moves
both the target location and residual dispersion toward the anchor by the same proportion:
(d)
|     |        |              |             | X        | =   | c +(1−d)(X |     | −c  | ). (23)               |          |     |      |
| --- | ------ | ------------ | ----------- | -------- | --- | ---------- | --- | --- | --------------------- | -------- | --- | ---- |
|     |        |              |             |          | 1,i | i          |     | 1,i | i                     |          |     |      |
| Its | mean   | and          | variance    | are      |     |            |     |     |                       |          |     |      |
|     |        | (cid:16) (d) | (cid:17)    |          |     |            |     |     | (cid:16) (d) (cid:17) |          |     |      |
|     |        | E X          | = c         | +(1−d)(µ |     | −c         | ),  | Var | X =                   | (1−d)2σ2 | .   | (24) |
|     |        | 1,i          |             | i        |     | 1,i        | i   |     | 1,i                   |          | 1,i |      |
| The | source | mean         | improvement |          | is  | dδ , hence |     |     |                       |          |     |      |
i
|     |     |     |     |     |     | R i (d) | = dB | ·i δ i . | (25) |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ---- | -------- | ---- | --- | --- | --- |
If the downstream utility is a linear weighted functional of the mean response,
P
|     |     |     |     |     |     |         |     | w ∆   | (d) |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |     |         | j   | j j←i |     |     |     |     |
|     |     |     |     |     |     | G i (d) | =   | P     | ,   |     |     |     |
w
j j
| then | equation |     | (25) implies | the | exact | linear | null | relation |      |     |     |     |
| ---- | -------- | --- | ------------ | --- | ----- | ------ | ---- | -------- | ---- | --- | --- | --- |
|      |          |     |              |     |       | G (d)  | = dG | (1).     | (26) |     |     |     |
|      |          |     |              |     |       | i      |      | i        |      |     |     |     |
Consequently,
(d)(cid:12)
|     |     |     |     | G i (d) |        |     | ∂G  | i (cid:12)   |          |      |     |     |
| --- | --- | --- | --- | ------- | ------ | --- | --- | ------------ | -------- | ---- | --- | --- |
|     |     |     |     | =       | G (1), |     |     | (cid:12)     | = G (1). | (27) |     |     |
|     |     |     |     |         | i      |     |     |              | i        |      |     |     |
|     |     |     |     | d       |        |     | ∂d  | (cid:12) d=0 |          |      |     |     |
Thus efficacy, benefit per unit dose and local responsiveness are mathematically redundant in an
unbounded linear CLPN with a linear dose map. A nonlinear dose-response curve is interpretable
| only when | an  | additional |     | nonlinear | element |     | is specified. |     |     |     |     |     |
| --------- | --- | ---------- | --- | --------- | ------- | --- | ------------- | --- | --- | --- | --- | --- |
For bounded symptom scales, one such source of nonlinearity is the measurement boundary.
(cid:0) m,s2(cid:1)
Let h(y) = min{U,max(L,y)} and Y ∼ N . With a = (L−m)/s and b = (U −m)/s, the
| bounded | expectation |     | is                                           |     |     |     |     |     |     |     |     |      |
| ------- | ----------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|         | E{h(Y)}     |     | = LΦ(a)+m{Φ(b)−Φ(a)}+s{ϕ(a)−ϕ(b)}+U{1−Φ(b)}. |     |     |     |     |     |     |     |     | (28) |
When s = 0, the expression reduces to h(m). Equation (28) provides an analytical way to
distinguish genuine boundary-induced curvature from coding artefacts in dosage analyses.
14

9.6 Directed edge and source-node communication blocking
Communicationblockingmodifiesthetransitionoperatorratherthanthesourcestate. Foradirected
path i(T1) → j(T2) and block fraction q ∈ [0,1], the edge-level operator is
B(i→j,q) = B−qB e e⊤. (29)
ji j i
For a prespecified source profile xref, the predicted follow-up difference between the unblocked
and blocked models is
(cid:16) (cid:17)
∆edge q;xref = {B−B(i→j,q)}xref = qB xrefe . (30)
i→j ji i j
Averaging over a source distribution gives
n o
E ∆edge(q;X ) = qB µ e . (31)
i→j 1 ji 1,i j
Equation (31) explains why communication blocking must specify a reference state. If predictors
are mean-centred, µ = 0 and the signed population-average prediction change is zero even when
1,i
B is large. The present framework therefore uses either clinically anchored profiles or individual-
ji
level predictions followed by aggregation rather than interpreting coefficient magnitude itself as
intervention impact.
A full source-node block attenuates all outgoing transitions from source i:
B(i,q) = B−qB e⊤. (32)
·i i
A cross-symptom-only version preserves autoregressive persistence and blocks only off-diagonal
outgoing paths:
B(i,q) = B−q(B −B e )e⊤. (33)
cross ·i ii i i
To quantify topology-level propagation independently of a single reference state, the reference
implementation uses a finite-horizon unsigned propagation functional
( H )
Q (B) = 1⊤ X (γ|B|)h 1, 0 < γ < 1. (34)
H
h=1
and the node-centred communication-block score is
(cid:16) (cid:17)
Q (B)−Q B(i,q)
H H
Rcomm = . (35)
i Q (B)
H
Because Q uses |B|, equation (35) measures route capacity rather than signed clinical benefit.
H
Signedreference-stateeffectsfromequation(30)shouldthereforebeinspectedalongsidethetopology
score when inhibitory paths are scientifically meaningful.
9.7 Combination perturbation and the additivity constraint
For targets i and k, let d δ e and d δ e denote their source mean improvements. The joint response
i i i k k k
is
R (d ,d ) = B(d δ e +d δ e ) = R (d )+R (d ). (36)
{i,k} i k i i i k k k i i k k
15

For any linear utility calculated on a common outcome set, equation (36) yields
|     | G     | (d  | ,d ) = | G (d | )+G | (d ), |     | NA = | G     | −G −G = 0. | (37) |
| --- | ----- | --- | ------ | ---- | --- | ----- | --- | ---- | ----- | ---------- | ---- |
|     | {i,k} | i   | k      | i i  |     | k k   |     | ik   | {i,k} | i k        |      |
Therefore, a standard linear two-wave CLPN cannot create statistical synergy from independent
state perturbations. tSymPerturb instead defines incremental combination value on a common
| comparison | set | that | excludes | targets |       | i and | k:  |       |         |      |     |
| ---------- | --- | ---- | -------- | ------- | ----- | ----- | --- | ----- | ------- | ---- | --- |
|            |     |      |          |         | (−ik) |       | n   | (−ik) | (−ik) o |      |     |
|            |     |      |          | I =     | G     | −max  | G   | ,G    | .       | (38) |     |
|            |     |      |          | ik      | ik    |       |     | i     | k       |      |     |
For a prespecified partner set T , the reference target-level combination score is
i
1 X
|     |     |     |     | Rcomb | =   |     | max(0,I |     | ).  | (39) |     |
| --- | --- | --- | --- | ----- | --- | --- | ------- | --- | --- | ---- | --- |
|     |     |     |     |       | i   |     |         |     | ik  |      |     |
|T i |
k∈Ti
The signed I values should also be retained so that antagonistic or harmful combinations are
ik
not hidden. A non-zero additive interaction contrast in equation (37) can arise only after introducing
a nonlinear outcome transform, interaction term, state-dependent coefficient, constraint or another
| non-additive | operation. |     |     |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
9.8 Multi-wave propagation and intervention sequence recursion
| For T | ≥ 3 occasions, |     | the | transition | model | generalises |        | to     |        |     |     |
| ----- | -------------- | --- | --- | ---------- | ----- | ----------- | ------ | ------ | ------ | --- | --- |
|       |                |     |     |            | X t+1 | = a t       | +B t X | t +ε t | . (40) |     |     |
−µ∗,
If a one-time source intervention at occasion t creates mean improvement δ t = µ t the
t
| one-step | response | is  | B δ | . After | h observed |     | transitions, |     |     |     |     |
| -------- | -------- | --- | --- | ------- | ---------- | --- | ------------ | --- | --- | --- | --- |
t t
|       |              |     |            | R   | =      | B     | B     | ···B | t δ t . | (41) |     |
| ----- | ------------ | --- | ---------- | --- | ------ | ----- | ----- | ---- | ------- | ---- | --- |
|       |              |     |            | t+h |        | t+h−1 | t+h−2 |      |         |      |     |
| Under | a stationary |     | transition |     | matrix | B t   | = B,  |      |         |      |     |
|       |              |     |            |     |        | R     | = Bhδ | .    | (42)    |      |     |
|       |              |     |            |     |        | t+h   |       | t    |         |      |     |
Equations (41) and (42) distinguish immediate leverage from persistent longitudinal leverage.
They also clarify that iterating a two-wave estimate beyond the observed interval requires a
stationarity assumption rather than additional information in the original data.
Repeated interventions can be represented by comparing an unperturbed mean trajectory µ0
t
|     |     |     |     |     |     |     | µ−. | ∆−  | µ0−µ− |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
with a perturbed pre-intervention trajectory Let = and let intervention u create an
|     |     |     |     |     |     |     | t   | t   | t   | t    | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
|     |     |     |     |     |     |     |     |     | ∆+  | ∆−+u |     |
additional improvement before the next transition, so that = t . The next-wave difference
|     |     |     |     |     |     |     |     |     | t   | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is then
|     |     |     |     |     |     |     | (cid:16) | (cid:17) |      |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | --- | --- |
|     |     |     |     |     | ∆−  |     | ∆−+u     |          |      |     |     |
|     |     |     |     |     |     | = B |          | .        | (43) |     |     |
|     |     |     |     |     | t+1 |     | t t      | t        |      |     |     |
This recursion is the appropriate object for genuine temporal sequence simulation. Order
dependence can arise when interventions occur at different observed occasions, when B changes
t
over time, when u depends on the current state, or when nonlinear constraints are imposed. A
t
two-wave CLPN contains only one observed transition and therefore cannot identify this repeated
| sequence         | without | additional |            | assumptions. |     |     |     |     |     |     |     |
| ---------------- | ------- | ---------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| A finite-horizon |         |            | discounted | utility      |     | is  |     |     |     |     |     |
16

U (H) = X
H
ηh−1
w⊤R
t+h,i , 0 < η ≤ 1. (44)
i P w
h=1 j j
For the separate two-wave target-acquisition problem, let π = (π ,...,π ) and S =
1 L m
{π ,...,π }. The decision objective is
1 m
L L
J(π) = X γm−1{U (S )−U (S )}− X λ . (45)
m m−1 πm
m=1 m=1
Equation(45)ordersadditionstoaninterventionsetunderexplicitcostanddiscountassumptions;
it should not be described as evidence for biological treatment order.
9.9 Longitudinal utility outcomes and tVPPS
For target i at dose d, the standardised outcome-specific improvement is
(i,d)
µ −µ
2,j 2,j
∆ (d) = . (46)
j←i
s
2,j
The total downstream efficacy includes the autoregressive destination:
Pp w ∆ (d)
Gall(d) = j=1 j j←i . (47)
i Pp w
j=1 j
The cross-symptom spillover estimand excludes the target’s own follow-up value:
P w ∆ (d)
Gcross(d) = j̸=i j j←i . (48)
i P w
j̸=i j
For threshold τ, breadth is
Rbreadth = 1 X 1{∆ (1) ≥ τ}. (49)
i p−1 j←i
j̸=i
LetM bethesetofsymptomsinmoduler,andletm(i)denotethetargetmodule. Cross-module
r
reach is
 
Rmodule = 1 X 1  1 X ∆ (1) ≥ τ  . (50)
i M −1 |M | j←i m
 r 
r̸=m(i) j∈Mr
Thepositivespilloverfractionseparatesdistributedbenefitfromautoregressivetargetpersistence:
P w max{∆ (1),0}
Rspill = j̸=i j j←i . (51)
i Pp w max{∆ (1),0}+10−12
j=1 j j←i
Together with communication-block value from equation (35) and combination value from
equation (39), these quantities define the seven reference utility dimensions: downstream efficacy,
cross-symptom spillover, breadth, cross-module reach, communication-block value, combination
value and spillover fraction. Dose efficiency and low-dose responsiveness are not included as
separate dimensions in the linear reference tVPPS because equations (26)–(27) show that they are
algebraically redundant with efficacy.
17

Each raw dimension R is direction-aligned and normalised only within the prespecified
im
candidate set:
|     |     |       |       | R   | −min R |        |
| --- | --- | ----- | ----- | --- | ------ | ------ |
|     |     | score | = 100 | im  | ℓ ℓm   | . (52) |
im
|     |     |     |     | max | R −min | R   |
| --- | --- | --- | --- | --- | ------ | --- |
|     |     |     |     | ℓ   | ℓm ℓ   | ℓm  |
If a dimension is constant, it is assigned the neutral value 50. The temporal virtual perturbation
| priority score is |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- |
P7
|     |     |       |       | ω score |      |             |
| --- | --- | ----- | ----- | ------- | ---- | ----------- |
|     |     | tVPPS | = m=1 | m       | im , | ω ≥ 0. (53) |
|     |     |       | i     | P7      |      | m           |
ω
|     |     |     |     | m=1 | m   |     |
| --- | --- | --- | --- | --- | --- | --- |
Equal weights were used only for internal methodological verification. Because normalisation is
candidate-set dependent, tVPPS is a relative within-analysis rank and is not directly transportable
across cohorts, networks or alternative candidate sets. Robustness and sampling uncertainty are
| reported separately | rather     | than | treated   | as intervention | utility. |     |
| ------------------- | ---------- | ---- | --------- | --------------- | -------- | --- |
| 9.10 Simulation     | generating |      | mechanism |                 |          |     |
The generating system contained 22 named synthetic symptoms organised into four modules.
Baseline X followed a multivariate normal distribution with heterogeneous means and stan-
1
dard deviations. Its correlation matrix was generated from one weak general factor and four
module factors so that within-module dependence was stronger than between-module depen-
dence. The transition matrix contained 22 autoregressive coefficients and 53 non-zero off-diagonal
paths; 47 cross-lagged paths were positive and 6 were negative. Strong prespecified bridge
transitions included Insomnia→Fatigue, Fatigue→Concentration difficulty, Rumination→Anxiety,
Rumination→Insomnia, Anxiety→Palpitations, Pain→Insomnia and Kinesiophobia→Activity avoid-
ance. Autoregressive coefficients ranged from 0.43 to 0.71 and the spectral radius of B was 0.827.
Residual errors were independent Gaussian variables with standard deviations from 0.38 to 0.52.
The intercept was selected so that the unperturbed follow-up mean equalled the baseline mean.
| From equation (9), | this | requires |     |           |        |     |
| ------------------ | ---- | -------- | --- | --------- | ------ | --- |
|                    |      |          | a   | = (I −B)µ | . (54) |     |
1
Baseline means ranged from 1.44 to 2.64 and baseline standard deviations from 0.63 to 0.83.
Population perturbation outcomes were calculated from the known µ , Σ , B and Ψ before any
1 1
| finite samples were | generated. |     |     |     |     |     |
| ------------------- | ---------- | --- | --- | --- | --- | --- |
At each sample size n ∈ {250,500,1000}, 200 independently generated datasets were created
from distinct child seeds of master seed 20260816. Within each dataset, T1 and T2 variables
were standardised and each T2 symptom was regressed on all T1 symptoms using lasso with
penalty α = 0.03 and no intercept on the standardised scale. The sample-specific zero anchor was
transformedusingequation(12). Networkestimation, perturbation, utilitycalculation, candidate-set
normalisation and ranking were rerun from the beginning for every independent dataset.
| 9.11 Analytical, | Monte | Carlo | and | algebraic | verification |     |
| ---------------- | ----- | ----- | --- | --------- | ------------ | --- |
For each of the 22 targets, 250,000 independent post-t-vKO draws were generated from the known
source distribution and residual distribution. The Monte Carlo estimate of the outcome response
was
|     |     |     | Rb MC = | X¯base−X¯vKO(i) | .   | (55) |
| --- | --- | --- | ------- | --------------- | --- | ---- |
|     |     |     | i,j     | 2,j             | 2,j |      |
18

It was compared with the analytical response in equation (21) after standardisation by s .
2,j
These Monte Carlo draws were used only to verify the analytical expectation and were not treated
| as independent | statistical | units. |     |     |
| -------------- | ----------- | ------ | --- | --- |
Two exact algebraic checks were applied to every implementation. First, the unbounded linear
reference model must satisfy equation (26) for every target and dose. Second, every two-target
state perturbation must satisfy equations (36)–(37). Numerically meaningful deviations from either
identity indicate an implementation error or the introduction of a nonlinear operation and should
| be diagnosed | before interpreting | target | rankings. |     |
| ------------ | ------------------- | ------ | --------- | --- |
The stationary multi-wave stress test reused the known B for four transitions and compared one-
step efficacy with B4δ and with the discounted cumulative utility in equation (44). The repeated-
i
intervention analysis applied equation (43) to the eight highest population tVPPS candidates.
Because the same transition matrix was reused beyond the observed two-wave interval, these
results were interpreted as strategy simulations under stationarity rather than identified treatment
sequences.
9.12 Finite-sample recovery, benchmark comparisons and uncertainty
Theindependentstatisticalunitforfinite-sampleverificationwasanindependentlygenerateddataset.
The primary recovery statistic was Spearman correlation between estimated and population tVPPS
ranks. We additionally calculated top-five recovery and RMSE on the 0–100 tVPPS scale. Medians
and 2.5th–97.5th percentile Monte Carlo intervals summarised the 200 replicate distributions at
| each sample | size. |     |     |     |
| ----------- | ----- | --- | --- | --- |
To determine whether tVPPS simply reproduced a standard longitudinal centrality measure,
| the population | ranking | was compared with | absolute outgoing | strength |
| -------------- | ------- | ----------------- | ----------------- | -------- |
p
Sout X
|     |     |     | = |B ji |, | (56) |
| --- | --- | --- | ---------- | ---- |
i
j=1
| signed | outgoing expected | influence |     |     |
| ------ | ----------------- | --------- | --- | --- |
p
X
|     |     | EIout | = B , | (57) |
| --- | --- | ----- | ----- | ---- |
i ji
j=1
and a baseline-burden-only rule based on µ . Rank correlation and top-five overlap were used
1,i
| as descriptive | benchmark | losses. |     |     |
| -------------- | --------- | ------- | --- | --- |
For applied data, uncertainty should be propagated through the complete pipeline. In bootstrap
(b)
replicateb,letr betheresultingrankoftargeti. Rankuncertaintyandtop-K selectionprobability
bi
| can be summarised | as  |     |           |          |
| ----------------- | --- | --- | --------- | -------- |
|                   |     | 1   | B Xboot n | o        |
|                   |     | (K) | (b)       |          |
|                   |     | P = | 1 r ≤     | K . (58) |
|                   |     | i B | bi        |          |
boot
b=1
The bootstrap should repeat participant resampling, standardisation, anchor transformation,
CLPN estimation, perturbation, utility calculation, normalisation and ranking. Robustness is
therefore treated as an uncertainty diagnostic rather than as an eighth utility component.
| 9.13 Required | validation | extensions |     |     |
| ------------- | ---------- | ---------- | --- | --- |
The current numerical experiment is an internal verification under a model-compatible continuous
Gaussian CLPN. A general methodological claim requires factorial stress tests that vary data type
19

(continuous, ordinal and zero-inflated), floor and ceiling effects, measurement error, latent common
causes, missingness and attrition, network density, edge-sign balance, p/n ratio, estimator and
penalty selection, time-varying coefficients, nonlinear transitions and participant-level heterogeneity.
These settings should distinguish failure caused by network estimation from failure caused by the
| perturbation  | operator | itself.         |     |
| ------------- | -------- | --------------- | --- |
| 9.14 Software | and      | reproducibility |     |
The validation was implemented in Python using NumPy, pandas, SciPy and scikit-learn; figures
were generated with Matplotlib. All data in the methodological verification are synthetic and use
masterseed20260816. Beforesubmission,thegeneratingparameters,validatedsourcecode,machine-
readable target scores and figure source data should be archived in a public version-controlled
repository with a persistent release identifier. An independent implementation in the intended
analysis environment should reproduce all analytical identities and source-data tables.
| Data | availability |     |     |
| ---- | ------------ | --- | --- |
All data used in the present methodological verification are synthetic. The generating parameters,
example datasets and source data underlying the validation figures should accompany the public
reproducibility bundle. No patient data were used in the simulation results reported here.
| Code | availability |     |     |
| ---- | ------------ | --- | --- |
ThecorecomputationalcodeunderlyingtheoriginalSymPerturbimplementationhasbeenpublished
previously in a related methodological article. The tSymPerturb implementation extends that frame-
work to directed transition matrices, temporal state operators, directed communication blocking,
longitudinal utility outcomes and multi-wave strategy simulation. The validated longitudinal code
and machine-readable outputs should be released in a version-controlled public repository upon
publication.
Acknowledgements
ThisworkwassupportedbytheNationalNaturalScienceFoundationofChina(GrantNo. 72574043),
the Shanghai Pujiang Program (Grant No. 24PJC014), and the China University Industry–Research
Innovation Fund–Digital Intelligence Innovation and Talent Program (Grant No. 2024LC007), all
awarded to Z.Z. The funders had no role in study design, data generation, analysis, interpretation,
| decision | to publish    | or preparation | of the manuscript. |
| -------- | ------------- | -------------- | ------------------ |
| Author   | contributions |                |                    |
Z.Z. conceived and developed the tSymPerturb framework, designed the methodological study and
drafted the manuscript. J.Y., T.H., Z.Y. and J.W. provided methodological and conceptual feedback
and critically reviewed the framework. All authors will review and approve the final version.
| Competing   | interests |              |            |
| ----------- | --------- | ------------ | ---------- |
| The authors | declare   | no competing | interests. |
20

References
[1] Borsboom, D. & Cramer, A. O. J. Network analysis: an integrative approach to the structure
of psychopathology. Annual Review of Clinical Psychology 9, 91–121 (2013).
[2] Borsboom, D. et al. Network analysis of multivariate data in psychological science. Nature
| Reviews Methods |     | Primers | 1,  | 58 (2021). |     |     |     |
| --------------- | --- | ------- | --- | ---------- | --- | --- | --- |
[3] Wysocki, A., McCarthy, I., van Bork, R. & Cramer, A. O. J. Cross-lagged panel networks.
| advances.in/psychology |     |     | 2, e739621 |     | (2025). | doi:10.56296/aip00037. |     |
| ---------------------- | --- | --- | ---------- | --- | ------- | ---------------------- | --- |
[4] Epskamp, S. Psychometric network models from time-series and panel data. Psychometrika 85,
| 206–231 (2020). | doi:10.1007/s11336-020-09697-3. |     |     |     |     |     |     |
| --------------- | ------------------------------- | --- | --- | --- | --- | --- | --- |
[5] Hamaker, E. L., Kuiper, R. M. & Grasman, R. P. P. P. A critique of the cross-lagged panel
| model. Psychological |     | Methods |     | 20, | 102–116 | (2015). |     |
| -------------------- | --- | ------- | --- | --- | ------- | ------- | --- |
[6] Sorjonen, K., Melin, B. & Nilsonne, G. Cross-lagged network models do not prove causality
and may be evaluated through triangulation. Acta Psychologica 260, 105562 (2025).
[7] Robinaugh, D. J., Millner, A. J. & McNally, R. J. Identifying highly influential nodes in the
complicated grief network. Journal of Abnormal Psychology 125, 747–755 (2016).
[8] Jones, P. J., Ma, R. & McNally, R. J. Bridge centrality: a network approach to understanding
| comorbidity. | Multivariate |     | Behavioral |     | Research |     | 56, 353–367 (2021). |
| ------------ | ------------ | --- | ---------- | --- | -------- | --- | ------------------- |
[9] Haslbeck, J. M. B. & Waldorp, L. J. How well do network models predict observations? On
the importance of predictability in network models. Behavior Research Methods 50, 853–861
(2018).
[10] Hallquist, M. N., Wright, A. G. C. & Molenaar, P. C. M. Problems with centrality measures in
psychopathology symptom networks: why network psychometrics cannot escape psychometric
| theory. Multivariate |     | Behavioral |     | Research |     | 56, 199–223 | (2021). |
| -------------------- | --- | ---------- | --- | -------- | --- | ----------- | ------- |
[11] Neal, Z. P. & Neal, J. W. Out of bounds? The boundary specification problem for centrality in
| psychological | networks. |     | Psychological |     | Methods |     | 28, 179–188 (2023). |
| ------------- | --------- | --- | ------------- | --- | ------- | --- | ------------------- |
[12] Neal, Z. P. et al. Critiques of network analysis of multivariate data in psychological science.
| Nature Reviews |     | Methods | Primers |     | 2, 90 (2022). |     |     |
| -------------- | --- | ------- | ------- | --- | ------------- | --- | --- |
[13] Lunansky, G. et al. Intervening on psychopathology networks: evaluating intervention targets
| through simulations. |     | Methods |     | 204, | 29–37 | (2022). |     |
| -------------------- | --- | ------- | --- | ---- | ----- | ------- | --- |
[14] Henry, T. R., Robinaugh, D. J. & Fried, E. I. On the control of psychological networks.
| Psychometrika | 87, | 188–213 | (2022). |     |     |     |     |
| ------------- | --- | ------- | ------- | --- | --- | --- | --- |
[15] Blanken, T. F. et al. Introducing network intervention analysis to investigate sequential,
symptom-specific treatment effects: a demonstration in co-occurring insomnia and depression.
| Psychotherapy | and | Psychosomatics |     |     | 88, 52–54 | (2019). |     |
| ------------- | --- | -------------- | --- | --- | --------- | ------- | --- |
[16] Pearl, J. Causal inference in statistics: an overview. Statistics Surveys 3, 96–146 (2009).
[17] Epskamp, S., Borsboom, D.&Fried, E.I.Estimatingpsychologicalnetworksandtheiraccuracy:
| a tutorial | paper. | Behavior | Research |     | Methods | 50, | 195–212 (2018). |
| ---------- | ------ | -------- | -------- | --- | ------- | --- | --------------- |
21

[18] Friedman, J., Hastie, T. & Tibshirani, R. Regularization paths for generalized linear models
via coordinate descent. Journal of Statistical Software 33, 1–22 (2010).
[19] Isvoranu, A.-M. & Epskamp, S. Which estimation method to choose in network psychometrics?
Deriving guidelines for applied researchers. Psychological Methods 28, 925–946 (2023).
22
---- END DOCUMENT ----
