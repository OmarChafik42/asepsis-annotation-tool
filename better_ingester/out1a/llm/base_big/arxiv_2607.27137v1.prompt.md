Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
| Hybrid | SINDy-EnKF      | in Learning | Chikungunya  |            | Dynamics     | from |
| ------ | --------------- | ----------- | ------------ | ---------- | ------------ | ---- |
|        | Incomplete,     | Noisy,      | or Partially | Observed   | Data         |      |
|        | Bernard Asamoah | Afful1,     | Changhong    | Mou2, Luis | F. Gordillo3 |      |
Department of Mathematics and Statistics, Utah State University, Logan, UT 84322
Abstract
Current mechanistic models for the transmission dynamics of the Chikungunya virus (CHIKV) rely on
uncertainparametersorpartiallyobserveddata. Thislimitationchallengestheuseoftheoreticalmodels
for understanding and forecasting disease spread. Here we present a hybrid, data-driven model frame-
work that combines Sparse Identification of Nonlinear Dynamics (SINDy) with the Ensemble Kalman
Filter (EnKF) for sequential data assimilation. Our numerical experiments show that this approach im-
proves prediction accuracy and provides a good reconstruction of unobserved trajectories under partial
observability, a common constraint in real-world epidemiological surveillance. SINDy can be applied to
epidemic trajectories, recovering the underlying equations in noise-free conditions. However, standalone
SINDy is highly sensitive to noise, leading to spurious terms and poor performance. Hence, we embed
the identification procedure within an EnKF framework, which assimilates noisy observations to correct
6202 luJ 92  ]EP.oib-q[  1v73172.7062:viXra
forecast states from the SINDy-derived model and to infer unobserved state variables.
Keywords: Chikungunyavirus(CHIKV);SparseIdentificationofNonlinearDynamics(SINDy);Ensem-
bleKalmanFilter(EnKF);Dataassimilation;Infectiousdiseasedynamics;Computationalepidemiology.
| 1Correspondingauthor,e-mailaddress: |                          | bernard.afful@usu.edu |     |     |     |     |
| ----------------------------------- | ------------------------ | --------------------- | --- | --- | --- | --- |
| 2e-mailaddress:                     | a02483619@aggies.usu.edu |                       |     |     |     |     |
| 3e-mailaddress:                     | luis.gordillo@usu.edu    |                       |     |     |     |     |

1 Introduction
Chikungunyavirus(CHIKV)isamosquito-bornearbovirustransmittedprimarilybyAedesaegyptiandAedes
albopictus. ThespreadofCHIKVisconsideredasignificantpublichealthconcernintropicalandsubtropical
regions [20, 32, 31]. Compartmental epidemic models, usually formulated via nonlinear ordinary or partial
differential equations, have been used to provide insights into the host-vector interactions and intervention
strategiesforCHIKV.Thosemodels, whicharebasedonepidemiologicaltheory, mayallowthederivationof
key quantities such as the basic reproduction number or equilibrium states [8, 26, 28]. The effectiveness of
the models, however, depends on accurate parameter values, which are often diﬀicult to obtain in practice:
epidemiological data are frequently incomplete, noisy, or partially observed. This produces uncertainty in
model calibration and reduces the predictive power. A useful alternative is data-driven methods, which
enablelearningofdynamicalrelationshipsdirectlyfromobserveddatawithoutrequiringapriorimechanistic
knowledge. Inthispaper,weproposeaframeworkforlearningChikungunyatransmissiondynamicsthrough
sparse identification and sequential data assimilation. Specifically, we use Sparse Identification of Nonlinear
Dynamics(SINDy)todiscovergoverningequationsfromlimitedornoisydata,whileemployingtheEnsemble
Kalman Filter (EnKF) to filter noise and infer unobserved state variables.
Inrecentyears,scientistshavebeenusingSINDyasatoolfordiscoveringinterpretabledynamicalsystems
from time-series data [6]. Essentially, if snapshots of a dynamical system and their time derivatives are
provided, SINDy performs sparsity-promoting regression (e.g., LASSO or sparse Bayesian inference) on a
libraryofcandidatenonlinearfunctions. Thenitrecoversasetofgoverningequationsthatbalanceaccuracy
with parsimony. Due to its interpretability and ease of implementation, SINDy has been widely applied in
diverse scientific domains, such as fluid dynamics [2, 12], neuroscience [21, 25], chemical kinetics [13, 22],
stochastic modeling [19, 5], and epidemiology [3, 15]. On the downside, SINDy may perform poorly for
noisy data: the algorithm requires numerical estimation of time derivatives, a step where the effects of
noise are amplified before propagating into the sparse regression. Therefore, noise may potentially cause
true terms to be discarded or spurious terms to be retained [11, 16]. This is more notorious in low-data,
high-noise regimes, which are typical of real-world observations [10]. Also, performance depends on the
chosen candidate library and the sparsity threshold, both of which are problem-specific and diﬀicult to tune
without ground truth. This contributes to poor robustness across varying data conditions. Recent variants
of SINDy have been proposed: Ensemble-SINDy [10] uses bootstrap aggregation to improve robustness
to noise and provide uncertainty estimates, while SINDy-PI [17] reformulates the implicit problem as a
convexoptimizationproblem, makingtheidentificationofrationalandimplicitdynamicssubstantiallymore
noise-tolerant. Despite these remarkable efforts, reliably recovering dynamics from noisy epidemiological
observations remains an open problem.
Itisknownthat,fornonlinearsystems,theEnsembleKalmanFilter(EnKF)isacomputationallyeﬀicient
method for sequential state estimation [9]. By propagating an ensemble of model states and updating them
with observations via the Kalman gain, the EnKF optimally balances model errors and observational noise,
effectively filtering measurement uncertainty from observed state variables and inferring unobserved state
variables using the state covariance matrix estimated from the ensemble spread. This makes it particularly
well-suitedforepidemiologicalapplications,wheredataareoftensparse,noisy,orpartiallyobserved[1,4,18].
Hybrid frameworks that couple SINDy with Kalman-type estimation have largely been investigated out-
sideepidemiology,inengineeringandthephysicalsciences. (author?)[23]introducedEKF-SINDy,inwhich
a SINDy model serves as the forecast operator of an Extended Kalman Filter, and the two are coupled for
joint state–parameter estimation: by augmenting the state with the SINDy coeﬀicients, the filter corrects
modelerroronlineandstaysaccurateevenoutsidethelibrary’strainingregime. Theirtests,ashearbuilding
driven by recorded seismograms and a partially observed nonlinear resonator, share the noisy, incomplete
character of epidemiological surveillance, and a follow-up extended the coupling to bifurcating systems such
as the Lotka–Volterra and Selkov models [24]. Ensemble Kalman methods have likewise been used to learn
data-driven closures from indirect observations [30], relying on the same cross-covariance mechanism that
carries information from measured to unmeasured components. Comparatively less attention has been given
to pairing SINDy with the ensemble Kalman filter for partially observed compartmental models in epidemi-
ology,wherederivativedataforunobservedstatesareunavailableandcross-compartmentcouplingscanhelp
drive state reconstruction, a setting this study aims to explore.
Therefore, it is desirable to have robust, data-driven methodologies that model disease transmission
1

dynamics from limited, noisy surveillance data while maintaining model interpretability. In this paper, we
propose such a design for the spread of CHIKV. Here we formulate a detailed compartmental model for
CHIKV transmission that captures host–vector interactions, serving as both a mechanistic foundation and a
benchmark for data-driven discovery, followed by SINDy application to reconstruct the governing dynamics
with different levels of observational noise, thus providing a systematic assessment of its robustness to noise
inanepidemiologicalcontext. Finally, weintegratetheEnKF toimprovestateestimationforboth observed
and unobserved variables, enabling more reliable inference when surveillance data capture only a subset of
| epidemiological |     | states. |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The paper is organized as follows. Section 2.1 details the CHIKV compartmental model, followed by an
overviewoftheSINDyframeworkandnoisehandlinginSection2.2. InSection2.3,wedescribetheEnsemble
Kalman Filter for state estimation. We present our numerical results and evaluate the joint SINDy-EnKF
framework in Section 3, concluding with a summary of key findings and future directions in Section 4.
| 2 Learning |             | the | Chikungunya |         |     | Virus |       | Model |     |     |     |     |
| ---------- | ----------- | --- | ----------- | ------- | --- | ----- | ----- | ----- | --- | --- | --- | --- |
| 2.1 The    | chikungunya |     | virus       | (CHIKV) |     |       | model |       |     |     |     |     |
The transmission dynamics of the chikungunya virus (CHIKV) are influenced by the mobility of the host
and the vector, as well as by the host-vector interaction (human-mosquito) in space and time ([7, 14]). In
thiswork,wemodelthesedynamicsusingacompartmentalframeworkthatcapturesthekeyepidemiological
stages of both populations. All state variables are functions of time t, and time dependence is omitted for
notational convenience unless otherwise noted. A schematic overview of the model structure, including all
| compartments | and | transitions, | is          | shown | in Figure | 1.      |     |       |     |     |     |     |
| ------------ | --- | ------------ | ----------- | ----- | --------- | ------- | --- | ----- | --- | --- | --- | --- |
|              |     |              | Chikungunya |       | Virus     | (CHIKV) |     | Model |     |     |     |     |
Develop
Recovery
| HumanPopulation |     |     |     |     |     | symptoms | I           |     | Treatment | T       | aftertreatment |     |
| --------------- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --------- | ------- | -------------- | --- |
|                 |     |     |     |     |     |          |             | h   |           | h       |                |     |
|                 |     |     |     |     |     |          | Symptomatic |     | Natural   | Treated |                |     |
recovery
Mosquitobite
| Birth/immigration |     | S           | (infection)  | E       |                            |     | ×       |     |     | ×       |     | R         |
| ----------------- | --- | ----------- | ------------ | ------- | -------------------------- | --- | ------- | --- | --- | ------- | --- | --------- |
|                   |     | h           |              |         | h                          |     |         |     |     |         |     | h         |
|                   |     |             |              |         |                            |     | (µh+δh) |     |     | (µh+δh) |     |           |
|                   |     | Susceptible |              | Exposed |                            |     |         |     |     |         |     | Recovered |
|                   |     |             | Breakthrough |         | Mosquitobitesinfectedhuman |     |         |     |     |         |     |           |
Vaccination
|     |     | × µ      | infection |     | ×µh        |     |     |     | N a tu ra l  |     |     | ×µh |
| --- | --- | -------- | --------- | --- | ---------- | --- | --- | --- | ------------ | --- | --- | --- |
|     |     | W ahning |           |     |            |     | J   |     |              |     |     |     |
|     |     |          |           |     |            |     |     | h   | r ec o ve ry |     |     |     |
|     |     | immunity |           |     | Nosymptoms |     |     |     |              |     |     |     |
Asymptomatic
V
h
×
|     |     | Vaccinated |     |     |     |     | (µh+δh) |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Infectiousmosquitobitessusceptiblehuman
×µh
MosquitoPopulation
|     |     |               |     |             |     | Bitesinfected |         |     | Becomes    |            |     |     |
| --- | --- | ------------- | --- | ----------- | --- | ------------- | ------- | --- | ---------- | ---------- | --- | --- |
|     |     | Newmosquitoes |     | S           |     | human         | E       |     | infectious | I          |     |     |
|     |     |               |     |             | v   |               |         | v   |            | v          |     |     |
|     |     |               |     | Susceptible |     |               | Exposed |     |            | Infectious |     |     |
|     |     |               |     | ×µv         |     |               | ×µv     |     |            | ×µv        |     |     |
Legend:
|     | Transition |                          | Vector→Hosttransmission |     |     |                             | Host→Vectortransmission |       |                      |        |     |     |
| --- | ---------- | ------------------------ | ----------------------- | --- | --- | --------------------------- | ----------------------- | ----- | -------------------- | ------ | --- | --- |
|     | Deathexit  | µh=naturalhumandeathrate |                         |     |     | δh=disease-induceddeathrate |                         |       | µv=mosquitodeathrate |        |     |     |
|     |            | Figure                   | 1: Illustration         |     | of  | the Chikungunya             |                         | virus | (CHIKV)              | model. |     |     |
2

| 2.1.1 | Host | population |     |     |     |     |     |     |     |     |
| ----- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
The host population N h is subdivided into seven mutually exclusive compartments: susceptible hosts S h ,
vaccinated hosts V , exposed hosts E , symptomatically infectious hosts I , asymptomatically infectious
|       |             | h     |     |               | h     |        |       |       | h   |       |
| ----- | ----------- | ----- | --- | ------------- | ----- | ------ | ----- | ----- | --- | ----- |
| hosts | J , treated | hosts | T , | and recovered | hosts | R , so | that  |       |     |       |
|       | h           |       | h   |               |       | h      |       |       |     |       |
|       |             |       |     | N             | =S +V | +E     | +I +J | +T +R | .   | (2.1) |
|       |             |       |     |               | h h   | h h    | h     | h h   | h   |       |
Susceptible hosts are recruited at a constant rate Λ , and we assume no vertical transmission, meaning all
h
newborns enter the susceptible category. The natural mortality rate of the host population is µ h , and δ h
denotes the disease-induced death rate. Susceptible hosts are vaccinated at a rate θ, while vaccine-induced
immunity wanes at a rate ω, returning vaccinated individuals to the susceptible class. A susceptible host
acquires infection through the bite of an infectious mosquito at a rate governed by the force of infection
λ = β I /N , where β is the probability of transmission per bite from an infected mosquito to a host.
| h   | v v | v   | v   |     |     |     |     |        |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
|     |     |     |     |     |     |     |     | (1−η), | ∈   |     |
Vaccinated hosts may also become infected at a reduced rate λ h where η [0,1] represents vaccine
eﬀicacy, accounting for imperfect vaccine protection. Following an incubation period (typically 2–12 days),
exposed hosts transition to either the symptomatically infectious compartment at a rate ρσ or the asymp-
h
(1−ρ)σ
tomatically infectious compartment at a rate , where ρ is the probability of developing symptoms.
h
Symptomatically infectious hosts receive treatment at a rate τ. After the viremic period, hosts in the symp-
tomatically infectious, asymptomatically infectious, and treated compartments recover at rates γ s , γ a , and
γ , respectively.
T
| 2.1.2 | Vector | population |     |     |     |     |     |     |     |     |
| ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ThevectorpopulationN isfurtherdividedintothreemutuallyexclusivecompartments: susceptiblevectors
v
| S , | exposed vectors |     | E , and | infectious | vectors | I , so   | that    |     |     |       |
| --- | --------------- | --- | ------- | ---------- | ------- | -------- | ------- | --- | --- | ----- |
| v   |                 |     | v       |            |         | v        |         |     |     |       |
|     |                 |     |         |            |         | N v =S v | +E v +I | v . |     | (2.2) |
Susceptible vectors are recruited at a constant rate Λ and die naturally at a rate µ . A susceptible vector
|     |     |     |     |     |     |     | v   |     | v   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
acquires the virus through blood feeding on an infectious host at a rate governed by the force of infection
|     |     |     |     |     |     | β (ϵ I | +ϵ J | +ϵ T ) |     |       |
| --- | --- | --- | --- | --- | --- | ------ | ---- | ------ | --- | ----- |
|     |     |     |     |     |     | h 1 h  | 2 h  | 3 h    |     |       |
|     |     |     |     |     | λ = |        |      | ,      |     | (2.3) |
|     |     |     |     |     | v   |        | N    |        |     |       |
h
where β is the transmission probability per bite from an infectious host to a mosquito, and ϵ (i = 1,2,3)
|     | h   |     |     |     |     |     |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arereductionfactorsthataccountfordifferencesintransmissibilityfromsymptomaticallyinfectious,asymp-
tomatically infectious, and treated hosts, respectively. After an incubation period, exposed vectors become
| infectious | at  | a rate σ | .   |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
v
3

| 2.1.3 Governing | equations |     |     |     |     |     |     |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Applying the law of mass action and incorporating the assumptions described above [27], we obtain the
following system of ordinary differential equations governing the CHIKV transmission dynamics:
|     |     | dS  |      | β   | I S   |     |     |      |     |     |     |
| --- | --- | --- | ---- | --- | ----- | --- | --- | ---- | --- | --- | --- |
|     |     |     | h =Λ | −   | v v h | −θS | +ωV | −µ S |     |     |     |
|     |     |     |      | h   |       | h   |     | h h  | h   |     |     |
|     |     |     | dt   |     | N     |     |     |      |     |     |     |
v
|     |     | dV  |     |     | β (1−η)I | V   |       |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | ----- | --- | --- | --- | --- |
|     |     |     | h   | −   | v        | v   | h −ωV | −µ  |     |     |     |
|     |     |     | =θS | h   |          |     |       | h h | V h |     |     |
|     |     |     | dt  |     | N        |     |       |     |     |     |     |
v
(1−η)I
|     |     | dE  | h   | β v I v S h | β v |     | v V h |        |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | ----- | ------ | --- | --- | --- |
|     |     |     | =   |             | +   |     |       | −(σ +µ | )E  |     |     |
|     |     |     | dt  | N           |     | N   |       | h      | h h |     |     |
|     |     |     |     | v           |     | v   |       |        |     |     |     |
dI
|     |     |     | h =ρσ | E   | −(τ +γ | +µ  | +δ  | )I  |     |     |     |
| --- | --- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- |
|     |     |     |       | h h |        | s   | h   | h h |     |     |     |
dt
dJ
|     |     |     | h =(1−ρ)σ |     | E   | −(γ +µ | +δ  | )J  |     |     |     |
| --- | --- | --- | --------- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     | dt        |     | h h | a      | h   | h h |     |     |     |
(2.4)
dT h
|     |     |     | =τI  | −(γ  | +µ         | +δ       | )T     |           |     |     |     |
| --- | --- | --- | ---- | ---- | ---------- | -------- | ------ | --------- | --- | --- | --- |
|     |     |     | dt   | h    | T          | h h      | h      |           |     |     |     |
|     |     | dR  | h    |      |            |          | −µ     |           |     |     |     |
|     |     |     | =γ   | I +γ | J +γ       | T        | R      |           |     |     |     |
|     |     |     | dt   | s h  | a h        | T h      | h      | h         |     |     |     |
|     |     |     | dS v | − β  | h (ϵ 1 I h | +ϵ 2 J h | +ϵ 3 T | h )S v −µ |     |     |     |
|     |     |     | =Λ   |      |            |          |        |           | S   |     |     |
|     |     |     | dt   | v    |            | N        |        |           | v v |     |     |
h
|     |     | dE  |     | β (ϵ I | +ϵ J | +ϵ  | T )S |        |     |     |     |
| --- | --- | --- | --- | ------ | ---- | --- | ---- | ------ | --- | --- | --- |
|     |     |     | v = | h 1 h  | 2    | h 3 | h v  | −(σ +µ | )E  |     |     |
|     |     |     |     |        |      |     |      | v      | v v |     |     |
|     |     |     | dt  |        | N    | h   |      |        |     |     |     |
dI
|     |     |     | v =σ | E −µ | I   |     |     |     |     |     |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |      | v v  | v v |     |     |     |     |     |     |
dt
| with initial | conditions:    |     |     |           |     |           |       |         |           |     |       |
| ------------ | -------------- | --- | --- | --------- | --- | --------- | ----- | ------- | --------- | --- | ----- |
|              |                |     | ≥0, |           | ≥0, |           |       | ≥0,     |           |     |       |
|              | S h (0)=S      | h0  | V   | h (0)=V   | h0  | E h       | (0)=E | h0      |           |     |       |
|              |                |     | ≥0, |           | ≥0, |           |       | ≥0,     |           | ≥0, |       |
|              | I h (0)=I      | h0  | J   | h (0)=J   | h0  | T h (0)=T |       | h0      | R h (0)=R | h0  | (2.5) |
|              |                |     | ≥0, |           | ≥0, |           |       | ≥0.     |           |     |       |
|              | S v (0)=S      | v0  | E   | v (0)=E   | v0  | I v       | (0)=I | v0      |           |     |       |
| 2.2 Sparse   | identification |     | of  | nonlinear |     | dynamics  |       | (SINDy) |           |     |       |
WebrieflydescribeSINDy[6],adata-drivenmodeldiscoverymethodforidentifyingsparsenonlinearmodels
from measurement data. The goal is to recover or discover the governing equations of the CHIKV model
(2.4) from observed state data. To this end, we rewrite (2.4) in compact form as:
dx
|     |     |     |     |     |     | =f(x), |     |     |     |     | (2.6) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ----- |
dt
where x(t) = (S ,V ,E ,I ,J ,T ,R ,S ,E ,I )T ∈ RK is the state vector and K = 10 is the number of
|     | h h | h h | h h | h v | v v |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
compartments.
| 2.2.1 Model | discovery | from | clean | data |     |     |     |     |     |     |     |
| ----------- | --------- | ---- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
Supposewehaveaccesstotime-seriesmeasurementsofthestateatmtimepointst 1 ,t 2 ,...,t m . Weorganize
these into a state matrix X∈Rm×K and a corresponding derivative matrix X˙ ∈Rm×K:
|     |     |     |     | 2    | 3       |     | 2    |        | 3   |     |       |
| --- | --- | --- | --- | ---- | ------- | --- | ---- | ------ | --- | --- | ----- |
|     |     |     |     | xT(t |         |     | x˙   | T(t )  |     |     |       |
|     |     |     |     | 1    | 1 )     |     |      | 1 1    |     |     |       |
|     |     |     |     | 6    | 7       |     | 6    |        | 7   |     |       |
|     |     |     |     | 6 xT | ( t ) 7 |     | 6 x˙ | T (t ) | 7   |     |       |
|     |     |     |     | 6 2  | 2 7,    | X˙  | 6    | 2 2    | 7.  |     |       |
|     |     |     | X=  |      | .       |     | =    | .      |     |     | (2.7) |
|     |     |     |     | 4    | . 5     |     | 4    | .      | 5   |     |       |
|     |     |     |     |      | .       |     |      | .      |     |     |       |
|     |     |     |     | xT   | (t )    |     | x˙   | T(t )  |     |     |       |
|     |     |     |     | K    | m       |     | K    | m      |     |     |       |
4

Table 1: Definitions of the parameters and state variables used in the CHIKV model (2.4) subject to the
| initial conditions | (2.5).                |                |             |                 |         |     |     |
| ------------------ | --------------------- | -------------- | ----------- | --------------- | ------- | --- | --- |
| State              | variables Description |                |             |                 |         |     |     |
| N h , N            | v Total host          | and mosquito   | populations |                 |         |     |     |
| S , S              | Total number          | of susceptible | hosts       | and susceptible | vectors |     |     |
h v
| V   | Total number | of hosts | who receive | vaccinations |     |     |     |
| --- | ------------ | -------- | ----------- | ------------ | --- | --- | --- |
h
| E h , E | v Total number | of exposed | hosts and | vectors |     |     |     |
| ------- | -------------- | ---------- | --------- | ------- | --- | --- | --- |
I , J Total number of symptomatic and asymptomatic infected hosts
h h
| T   | Total number | of treated | hosts |     |     |     |     |
| --- | ------------ | ---------- | ----- | --- | --- | --- | --- |
h
| R   | Total number | of recovered | hosts |     |     |     |     |
| --- | ------------ | ------------ | ----- | --- | --- | --- | --- |
h
| I   | Total number | of infectious | vectors |     |     |     |     |
| --- | ------------ | ------------- | ------- | --- | --- | --- | --- |
v
| Parameter | Description |     |     |     |     | Units |     |
| --------- | ----------- | --- | --- | --- | --- | ----- | --- |
Λ , Λ Rates of recruiting susceptible hosts, and female vectors persons/day, mosquitoes/day
h v
| µ , µ | Natural | death rates of | hosts, and | vectors |     | day−1 |     |
| ----- | ------- | -------------- | ---------- | ------- | --- | ----- | --- |
h v
day−1
| δ   | Disease-induced | death | rate of hosts |     |     |     |     |
| --- | --------------- | ----- | ------------- | --- | --- | --- | --- |
h
β Transmission probability per bite (host → vector) dimensionless
h
→
β v Transmission probability per bite (vector host) dimensionless
ϵ , i=1,2,3 Transmission reduction factor, ϵ ≪1 dimensionless
| i   |        |               |                 | i   |             |       |     |
| --- | ------ | ------------- | --------------- | --- | ----------- | ----- | --- |
| ω   | Waning | immunity rate | from vaccinated | to  | susceptible | day−1 |     |
day−1
| θ   | Vaccination | rate                     |     |          |     |               |     |
| --- | ----------- | ------------------------ | --- | -------- | --- | ------------- | --- |
| η   | Vaccine     | eﬀicacy (0: ineffective, | 1:  | perfect) |     | dimensionless |     |
day−1
| σ h | Rate at | which exposed | hosts become | infectious |     |     |     |
| --- | ------- | ------------- | ------------ | ---------- | --- | --- | --- |
day−1
| σ   | Rate at | which exposed | vectors become | infectious |     |     |     |
| --- | ------- | ------------- | -------------- | ---------- | --- | --- | --- |
v
ρ Probability an exposed host becomes symptomatic dimensionless
day−1
| γ   | Recovery | rate of symptomatic | hosts |     |     |     |     |
| --- | -------- | ------------------- | ----- | --- | --- | --- | --- |
s
| γ   | Recovery | rate of asymptomatic |     | hosts |     | day−1 |     |
| --- | -------- | -------------------- | --- | ----- | --- | ----- | --- |
a
day−1
| γ T | Recovery | rate for treated | hosts |     |     |     |     |
| --- | -------- | ---------------- | ----- | --- | --- | --- | --- |
day−1
| τ   | Rate of         | treatment initiation | for        | symptomatic | hosts                        |     |     |
| --- | --------------- | -------------------- | ---------- | ----------- | ---------------------------- | --- | --- |
|     |                 | Table                | 2: Initial | conditions. |                              |     |     |
|     | State variables | Initial              | conditions | State       | variables Initial conditions |     |     |
|     | S (0)           | 1000                 |            | T (0)       | 0                            |     |     |
|     | h               |                      |            | h           |                              |     |     |
|     | V (0)           | 0                    |            | R (0)       | 0                            |     |     |
|     | h               |                      |            | h           |                              |     |     |
|     | E (0)           | 50                   |            | S (0)       | 2000                         |     |     |
|     | h               |                      |            | v           |                              |     |     |
|     | I h (0)         | 10                   |            | E v (0)     | 100                          |     |     |
|     | J (0)           | 5                    |            | I (0)       | 50                           |     |     |
|     | h               |                      |            | v           |                              |     |     |
The key assumption underlying SINDy is that f admits a sparse representation in a library of p nonlinear
| candidate | functions: |     |         |     |         |     |     |
| --------- | ---------- | --- | ------- | --- | ------- | --- | --- |
|           |            |     | (cid:2) |     | (cid:3) |     |     |
···
|     |     | Θ(x)= | 1 θ 1 (x) | θ 2 (x) | θ p (x) |     | (2.8) |
| --- | --- | ----- | --------- | ------- | ------- | --- | ----- |
whereeachcolumnθ (X)evaluatesacandidatefunction(e.g.,polynomialsorpairwiseproducts)ateachtime
j
instance. For the CHIKV model (2.4), the relevant candidates include constant, linear, and bilinear terms
arisingfrommass-actioninteractionsbetweencompartments. Thedynamics(2.6)canthenbeapproximated
| as a sparse | linear combination | of these candidates |     | :   |     |     |     |
| ----------- | ------------------ | ------------------- | --- | --- | --- | --- | --- |
dx(t)
≈Θ(x)Ξ,
(2.9)
dt
where Ξ is a sparse coeﬀicient matrix whose nonzero entries indicate the active terms in each governing
equation. Solving (2.9) as an unconstrained least-squares problem typically yields spurious nonzero entries.
5

|     |     |     |     |           | Table | 3: The | parameter |           | values. |       |     |
| --- | --- | --- | --- | --------- | ----- | ------ | --------- | --------- | ------- | ----- | --- |
|     |     |     |     | Parameter |       | Value  |           | Parameter |         | Value |     |
|     |     |     |     | Λ         |       | 10     |           | ϵ         |         | 0.2   |     |
h
|     |     |     |     | Λ v |     | 10000      |     | ρ   |     | 0.7 |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|     |     |     |     | µ   |     | 1/(80*365) |     | γ   |     | 1/7 |     |
|     |     |     |     | h   |     |            |     | s   |     |     |     |
|     |     |     |     | µ   |     | 1/14       |     | γ   |     | 1/5 |     |
|     |     |     |     | v   |     |            |     | a   |     |     |     |
|     |     |     |     | δ h |     | 0.001      |     | γ T |     | 1/6 |     |
|     |     |     |     | β   |     | 0.5        |     | τ   |     | 0.1 |     |
h
|     |     |     |     | β   |     | 0.4       |     | σ   |     | 0.33 |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ---- | --- |
|     |     |     |     | v   |     |           |     | v   |     |      |     |
|     |     |     |     | ω   |     | 1/(3*365) |     | σ   |     | 0.2  |     |
h
|            |           |     |         | θ           |                 | 0.4 |               | dt (days) |     | 0.0001 |        |
| ---------- | --------- | --- | ------- | ----------- | --------------- | --- | ------------- | --------- | --- | ------ | ------ |
|            |           |     |         | η           |                 | 0.7 |               |           |     |        |        |
| To enforce | sparsity, | we  | instead | solve       | the regularized |     | problem:      |           |     |        |        |
|            |           |     |         | Ξ=argmin∥X˙ |                 |     | −Θ(x)Ξ∥2+λ∥Ξ∥ |           |     | ,      | (2.10) |
|            |           |     |         |             |                 |     | k             |           | 2   | 0      |        |
Ξ
where λ>0 is a regularization parameter promoting sparsity. In practice, (2.10) is solved using the Sequen-
tiallyThresholdedLeastSquares(STLSQ)algorithm[29]: startingfromaleast-squaressolution, coeﬀicients
with magnitude below the threshold λ are set to zero, and the least-squares problem is re-solved over the
remaining terms. This procedure is repeated for a fixed number of iterations n.
| 2.2.2 | Model | discovery | from | noisy | data |     |     |     |     |     |     |
| ----- | ----- | --------- | ---- | ----- | ---- | --- | --- | --- | --- | --- | --- |
In practice, measurements are usually corrupted by noise. To model this, we define noisy observations as:
|     |     |     |     |     |     | Y   | =H(X)+ϵo |     |     |     | (2.11) |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ------ |
where H : RKs → RKo is an observation operator mapping the full state to K ≤ K observed components,
o
| ϵo  |     |     |     |     |     |     |     |     |     | Ro. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and is a zero-mean white noise process with covariance matrix The resulting noisy state matrix
∈Rm×K
| Y         | and       | its derivative |           | Y˙ take     | the | same tabular |      | form as | (2.7):   |         |        |
| --------- | --------- | -------------- | --------- | ----------- | --- | ------------ | ---- | ------- | -------- | ------- | ------ |
|           |           |                |           |             | 2   |              | 3    | 2       |          | 3       |        |
|           |           |                |           |             |     | yT(t         | )    |         | y˙T(t )  |         |        |
|           |           |                |           |             |     | 1            |      |         | 1        |         |        |
|           |           |                |           |             | 6   |              | 7    | 6       |          | 7       |        |
|           |           |                |           |             | 6   | yT( t        | ) 7  | 6       | y˙T( t ) | 7       |        |
|           |           |                |           |             | 6   | 2            | 7,   | Y˙ 6    | 2        | 7.      |        |
|           |           |                |           |             | Y = | .            |      | =       | .        |         | (2.12) |
|           |           |                |           |             | 4   | . .          | 5    | 4       | . .      | 5       |        |
|           |           |                |           |             |     | yT(t         | )    | y˙T(t   |          | )       |        |
|           |           |                |           |             |     | m            |      |         | m        |         |        |
| Analogous | to (2.8), | we             | construct | a candidate |     | library      | from | the     | noisy    | data:   |        |
|           |           |                |           |             |     | (cid:2)      |      |         |          | (cid:3) |        |
···
|                 |     |           |          | Φ(y)= |     | 1 ϕ 1 | (y) | ϕ 2 (y) | ϕ   | p (y) | (2.13) |
| --------------- | --- | --------- | -------- | ----- | --- | ----- | --- | ------- | --- | ----- | ------ |
| and approximate |     | the noisy | dynamics |       | as: |       |     |         |     |       |        |
dy(t)
≈Φ(y)Π,
(2.14)
dt
where Π is a sparse coeﬀicient matrix. The corresponding regularized regression problem is:
|     |     |     |     | Π=argmin∥Y˙ |     |     | −Φ(y)Π∥2+λ˜∥Π∥ |     |     | ,   | (2.15) |
| --- | --- | --- | --- | ----------- | --- | --- | -------------- | --- | --- | --- | ------ |
|     |     |     |     |             |     |     |                | 2   |     | 0   |        |
Π
λ˜
| where | >0 is the | regularization |     | parameter. |     |     |     |     |     |     |     |
| ----- | --------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
6

| 2.3 | Ensemble |     | Kalman | Filter |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Consider the ODE system (2.6) discretized in time, leading to the following state-space form:
|     |     |     |     |     |     | x   | =A (x | )+ζ      | ,   |     |     |     | (2.16) |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | ------ |
|     |     |     |     |     |     | n+1 | n     | n        | n   |     |     |     |        |
|     |     |     |     |     |     | z   | =H    | (x )+ζo, |     |     |     |     | (2.17) |
|     |     |     |     |     |     | n+1 | n+1   | n+1      | n   |     |     |     |        |
where A is a (possibly nonlinear) forward operator that advances the state from time t to t , and H
|     | n   |     |     |     |     |     |     |     |     |     |     | n n+1 | n+1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
is the observation operator introduced in (2.11). The term ζ is a K-dimensional Gaussian white noise with
n
zero mean and covariance Q , representing model error, while ζo is a K -dimensional Gaussian white noise
|     |     |     |     | n   |     |     |     |     | n   | o   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ro,
with zero mean and covariance representing observation noise consistent with (2.11).
Denotebyuk ,k =1,...,K,anensembleofJ forecaststatesattimet obtainedviaMonteCarlo
|     |     | m+1|m |     |     |     |     |     |     |     | n+1 |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A
| simulation | of  | the forward | model |     | n . The | forecast | (prior) | ensemble |     | mean is: |     |     |     |
| ---------- | --- | ----------- | ----- | --- | ------- | -------- | ------- | -------- | --- | -------- | --- | --- | --- |
XJ
|     |     |     |     |     |     |       |     | 1 x( | j )   |     |     |     |        |
| --- | --- | --- | --- | --- | --- | ----- | --- | ---- | ----- | --- | --- | --- | ------ |
|     |     |     |     |     |     | x¯    | =   |      | ,     |     |     |     | (2.18) |
|     |     |     |     |     |     | n+1|n |     | J n  | + 1|n |     |     |     |        |
j=1
where,fornotationalsimplicity,theapproximationiswrittenasanequality. Similarly,theanalysis(posterior)
| ensemble | mean | is: |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
XJ
1
|     |     |     |     |     |     |            |     | x(  | j )     |     |     |     |        |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ------- | --- | --- | --- | ------ |
|     |     |     |     |     |     | x¯ n+1|n+1 | =   |     |         | .   |     |     | (2.19) |
|     |     |     |     |     |     |            |     | J n | + 1|n+1 |     |     |     |        |
j=1
Thepriorandposteriorerrorcovariancematrices,P andP ,areestimatedfromtheensemble
|     |     |     |     |     |     |     |     | n+1|n |     | n+1|n+1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- |
as:
1
XT
|     |     |     |     |     | P n+1|n | =   |      | X n+1|n | n+1|n | ,   |     |     | (2.20) |
| --- | --- | --- | --- | --- | ------- | --- | ---- | ------- | ----- | --- | --- | --- | ------ |
|     |     |     |     |     |         |     | J −1 |         |       |     |     |     |        |
1
XT
|       |               |             |           |          | P n+1|n+1   | =           |            | X n+1|n+1 | n+1|n+1 | ,             |         |          | (2.21) |
| ----- | ------------- | ----------- | --------- | -------- | ----------- | ----------- | ---------- | --------- | ------- | ------------- | ------- | -------- | ------ |
|       |               |             |           |          |             |             | J −1       |           |         |               |         |          |        |
| where | the deviation |             | (anomaly) | matrices |             | are defined |            | as:       |         |               |         |          |        |
|       |               |             |           |          | (cid:2)     |             |            |           |         | (cid:3)       |         |          |        |
|       |               |             |           |          | x( 1 )      | −x¯         |            | x(        | J ) −x¯ |               |         |          |        |
|       |               |             | X n+1|n   | =        | 1|n         |             | n+1|n ,    | ...,      | 1|n     | n+1|n ,       |         |          | (2.22) |
|       |               |             |           |          | (cid:2) n + |             |            | n         | +       |               | (cid:3) |          |        |
|       |               |             | X         | =        | x( 1 )      | −x¯         |            | , ...,    | x( J )  | −x¯           | .       |          | (2.23) |
|       |               |             | n+1|n+1   |          | 1|n+1       |             | n+1|n+1    |           |         | 1|n+1 n+1|n+1 |         |          |        |
|       |               |             |           |          | n +         |             |            |           | n +     |               |         |          |        |
| When  | the           | observation | operator  |          | H is        | linear,     | the Kalman | gain      | takes   | the form:     |         |          |        |
|       |               |             |           | (cid:0)  |             |             |            | (cid:1)   |         |               |         |          |        |
|       |               |             |           | HT       |             | HT          | +Ro        | −1        |         |               |         |          |        |
|       |               | K =P        | n+1|n     | HP       | n+1|n       |             |            |           |         |               |         |          |        |
|       |               | n           |           |          |             |             | (cid:18)   |           |         |               |         | (cid:19) |        |
−1
|     |     |     | 1    |         |     |       |     | 1   |       |            |        |     |        |
| --- | --- | --- | ---- | ------- | --- | ----- | --- | --- | ----- | ---------- | ------ | --- | ------ |
|     |     |     |      |         |     |       | )T  |     |       |            | )T +Ro |     |        |
|     |     | =   |      | X n+1|n | (HX | n+1|n |     | (HX | n+1|n | )(HX n+1|n |        | .   | (2.24) |
|     |     |     | J −1 |         |     |       | J   | −1  |       |            |        |     |        |
where the observation operator G is assumed to be linear. For a nonlinear observation operator, the matrix
| product | HX  | is  | replaced | by the | ensemble |     | approximation: |     |     |     |     |     |     |
| ------- | --- | --- | -------- | ------ | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
n+1|n
|     |     |     |     | (cid:2) |       |     |        |       |      |             | (cid:3) |     |        |
| --- | --- | --- | --- | ------- | ----- | --- | ------ | ----- | ---- | ----------- | ------- | --- | ------ |
|     |     |     | Z=  | H(x(1)  | )−z¯, |     | H(x(2) | )−z¯, | ..., | H(x(J) )−z¯ | ,       |     | (2.25) |
|     |     |     |     |         | n+1|n |     | n+1|n  |       |      | n+1|n       |         |     |        |
P
|     | 1   | J   | H(x(j) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where z¯ = ). This avoids computing the Jacobian of H, as would be required in the
|          | J      | j=1     | n+1|n |           |        |       |         |          |          |         |     |     |        |
| -------- | ------ | ------- | ----- | --------- | ------ | ----- | ------- | -------- | -------- | ------- | --- | --- | ------ |
| extended | Kalman | filter. | The   | posterior | update |       | for the | ensemble | is then: |         |     |     |        |
|          |        |         |       |           |        |       |         | (cid:0)  |          | (cid:1) |     |     |        |
|          |        |         |       | x(j)      |        | =x(j) |         | z(j)     | −H(x(j)  |         |     |     |        |
|          |        |         |       |           |        |       | +K      |          |          | ) ,     |     |     | (2.26) |
|          |        |         |       | n+1|n+1   |        | n+1|n |         | n n+1    |          | n+1|n   |     |     |        |
where the observation is perturbed as z(j) = z +η(j) , with η(j) ∼ N(0,Ro). This stochastic per-
|     |     |     |     |     |     | n+1 | n+1 | n+1 |     | n+1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
turbation ensures an asymptotically correct estimate of the analysis error covariance for large ensembles.
7

However, for small ensemble sizes, this perturbation introduces additional sampling errors that affect the
covariance estimate.
8

|     |     |           | Sparse |     | Identification   |     | of     | Nonlinear | Dynamics     |     | (SINDy) |             |     |
| --- | --- | --------- | ------ | --- | ---------------- | --- | ------ | --------- | ------------ | --- | ------- | ----------- | --- |
|     |     | Snapshots |        |     | CandidateLibrary |     |        |           | Coefficients |     |         | Derivatives |     |
|     |     |           |        |     | 1 X              | X2  | X3 ··· |           |              |     |         |             |     |
x˙1(t1)
0
|     | x1  |     |     |     | · · | ·   | · · |     |     |     |     |         |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
|     |     |     |     |     |     |     |     |     | ξ2  |     |     | x˙1(t2) |     |
|     |     |     |     |     | · · | ·   | · · |     |     |     |     |         |     |
|     |     |     |     |     |     |     |     |     | 0   |     |     | .       |     |
. .
|     | x2  |     |     |     | · · | ·   | · · |     |     |         |     |         |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- |
|     |     |     |     |     |     |     |     | ×   | 0   |         | =   | . .     |     |
|     |     |     |     |     |     |     |     |     |     | sparse! |     | .       |     |
|     |     |     |     |     | · · | ·   | · · |     |     |         |     |         |     |
|     |     |     |     |     |     |     |     |     | ξ5  |         |     | x˙1(tm) |     |
|     |     |     |     |     | · · | ·   | · · |     |     |         |     | .       |     |
|     | x3  |     |     |     |     |     |     |     | 0   |         |     | .       |     |
|     |     |     |     |     | · · | ·   | · · |     |     |         |     | .       |     |
|     |     |     |     |     |     |     |     |     | 0   |         |     | x˙n(tm) |     |
|     |     |     |     |     | · · | ·   | · · |     |     |         |     |         |     |
x4
|     |     | X   |     |     |     | Θ(X) |     |            | Ξ     |     |     | X˙  |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ---------- | ----- | --- | --- | --- | --- |
|     |     | m×n |     |     |     | m×p  |     |            | p×n   |     |     | m×n |     |
|     |     |     |     |     |     |      |     | identified | model |     |     |     |     |
The SINDy model x˙ = Θ(x)Ξ is used as the forecast model in the Kalman filter:
|     |     |       |     |     | (cid:0) (cid:1) |     |         |     |       |     | (cid:0) |       | (cid:1) |
| --- | --- | ----- | --- | --- | --------------- | --- | ------- | --- | ----- | --- | ------- | ----- | ------- |
|     | xˆ  | = xˆ  | +∆t | Θ   | xˆ Ξ            |     | xˆ      |     | = xˆ  | +K  | y       | −Hxˆ  |         |
|     |     | k+1|k | k|k |     | k|k             |     | k+1|k+1 |     | k+1|k |     | k+1 k+1 | k+1|k |         |
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
|     |     | SINDyprediction |       |     |         |              |     |           | Kalmanupdatestep |     |          |     |     |
| --- | --- | --------------- | ----- | --- | ------- | ------------ | --- | --------- | ---------------- | --- | -------- | --- | --- |
|     |     |                 |       |     |         |              |     | filtering | & update         |     |          |     |     |
|     |     | From            | Noisy |     | Partial | Observations |     |           | Infer Unobserved |     | Variable |     |     |
(a)Truestatex(hidden) (b)Noisypartialobservationsy (c)Filteredstatexˆ
Kalman
filter
|     |     | x1  |     |     | x1  |     |     |     |     |     | xˆ1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
not
|     |     | x2  |     |     | x2  |     | ?   |     |     |     | xˆ2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observed
|     |     | x3  |     |     | x3  |     |     |     |     |     | xˆ3 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
not
observed
|     |     | x4               |                    |                        | x4  |                   | ?                            |           |            |           | xˆ4                          |     |     |
| --- | --- | ---------------- | ------------------ | ---------------------- | --- | ----------------- | ---------------------------- | --------- | ---------- | --------- | ---------------------------- | --- | --- |
|     |     | True(hidden)     |                    | Noisyobs.              |     | KFestimate        |                              |           | Unobserved |           |                              |     |     |
|     |     |                  |                    | −−K−al−m−a−n−fi−lt−e→r |     |                   |                              |           | SI N D y   |           |                              |     |     |
|     |     | y =Hx            | +v                 |                        |     |                   | xˆ ≈x                        |           | −− − − − → | x˙ =Θ(x)Ξ |                              |     |     |
|     |     | k                | k                  | k                      |     |                   | k                            | k         |            |           |                              |     |     |
|     |     | (cid:124)        | (cid:123)(cid:122) | (cid:125)              |     |                   | (cid:124) (cid:123)(cid:122) | (cid:125) |            | (cid:124) | (cid:123)(cid:122) (cid:125) |     |     |
|     |     | noisypartialobs. |                    |                        |     | fullstateestimate |                              |           |            |           |                              |     |     |
governingequations
Figure 2: Illustration of learning chikungunya transmission dynamics proposed in this paper: a sparse
| identification |     | and sequential |     | data | assimilation |     | approach. |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | ---- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
9

| 3 Numerical |     | Results |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Inthissection,weconductaseriesofnumericalexperimentstoassesstheperformanceoftheproposeddata-
driven framework for the CHIKV transmission model (2.4). Our objectives are threefold: (i) to verify that
SINDycanfaithfullyrecoverthegoverningequationsunderidealized,noise-freeconditions;(ii)tocharacterize
the degradation of SINDy-based identification as the level of observational noise increases, thereby exposing
the practical limitations of pure sparse regression; and (iii) to show that the EnKF, when coupled with the
SINDy-discovered surrogate, infers accurate state estimation and enables the reconstruction of unobserved
| state variables | under | realistic | partial | and noisy | observations. |     |     |     |     |
| --------------- | ----- | --------- | ------- | --------- | ------------- | --- | --- | --- | --- |
The reference (“true”) trajectories are obtained by integrating the CHIKV model (2.4) with the parame-
ters listed in Appendix 4, using the fourth-Order Runge-Kutta method (RK4) scheme with a fine time step.
xb(t)
Throughout, the accuracy of an estimated trajectory relativeto the true trajectory x(t) isquantified by
| the component-wise |     | root | mean square | error | (RMSE), |     |     |     |     |
| ------------------ | --- | ---- | ----------- | ----- | ------- | --- | --- | --- | --- |
v
u
|     |     |     |        | u   | Xm (cid:0) |     | (cid:1) |             |       |
| --- | --- | --- | ------ | --- | ---------- | --- | ------- | ----------- | ----- |
|     |     |     |        | t 1 |            |     | 2       |             |       |
|     |     |     | RMSE = |     | xb (t      | )−x | (t ) ,  | k =1,...,K, | (3.1) |
|     |     |     | k      | m   | k          | j   | k j     |             |       |
j=1
| and by | the corresponding |     | relative | RMSE, |     |     |     |     |     |
| ------ | ----------------- | --- | -------- | ----- | --- | --- | --- | --- | --- |
b
|     |     |     |     |     |     | ∥X  | −X∥ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F,
|     |     |     |     | rRMSE |     | =   |     |     | (3.2) |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | ----- |
∥X∥
F
where ∥·∥ denotes the Frobenius norm. For the data-assimilation experiments in Section 3.3, we addition-
F
ally report the normalized RMSE (NRMSE) and the temporal correlation between estimated and reference
trajectories.
| 3.1 Identification |     |     | of CHIKV | Dynamics |     | from | Clean | Observations |     |
| ------------------ | --- | --- | -------- | -------- | --- | ---- | ----- | ------------ | --- |
We first establish a baseline by applying SINDy to noise-free state trajectories. This idealized setting serves
as a sanity check, verifying that the chosen candidate library and sparsity-promoting regression can recover
| the structural | form | of (2.4) | when the | data | are uncorrupted. |     |     |     |     |
| -------------- | ---- | -------- | -------- | ---- | ---------------- | --- | --- | --- | --- |
Experimental setup The state matrix X and derivative matrix X˙ defined in (2.7) are constructed di-
rectly from the reference trajectories. The candidate library Θ(x) comprises a constant, all linear terms,
and all pairwise bilinear products of the ten compartments, consistent with the mass-action structure of
compartmental epidemic models. The sparse coeﬀicient matrix Ξ is then obtained by solving (2.10) with
10−10,
the STLSQ algorithm. In the noise-free case, we adopt a very small sparsity threshold λ = since
any nonzero coeﬀicient produced by the regression corresponds to a term in the underlying dynamics. The
discovered system is simulated by forward-integrating it with the same initial conditions and time horizon
| used to | generate | the reference | trajectories. |     |     |     |     |     |     |
| ------- | -------- | ------------- | ------------- | --- | --- | --- | --- | --- | --- |
Reconstruction accuracy Figures 3(a) and 3(b) compare the reference and SINDy-reconstructed trajec-
tories for the host and vector populations. The reconstructed dynamics are visually indistinguishable from
the truth across all compartments: the initial transient, the epidemic peak, and the long-term equilibrium
are accurately reproduced. The quantitative comparisons are reported in Tables 4 and 5. Component-wise
RMSE values remain below 1 for every host compartment and below 1 for the vector compartments relative
topopulationsoforder104,andtheglobalrelativeRMSEisessentiallyzero(rRMSE≈10−5). Theaggregate
RMSE of 0.2281 is several orders of magnitude smaller than the characteristic scale of the state variables.
Discussion Two observations are worth emphasizing. First, the equations identified by SINDy (reported
in Appendix B) reproduce both the structural form and the parameter values of the original model (2.4) to
within numerical precision, indicating that the bilinear candidate library is well adapted to the mass-action
transmission mechanism. Second, the parsimony of the discovered model is that only the terms genuinely
10

presentin(2.4)havesignificantcoeﬀicients,whichfurtherindicatesthattheSTLSQthresholdingsuccessfully
suppresses redundant nonlinear monomials despite the large dimensionality of the candidate space.
(a) True CHIKV dynamics
104
14
4500
4000
12
3500
10
| noitalupoP tsoH 3000 |     |     |     |     |     |     | noitalupoP rotceV |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
| 2500                 |     |     |     |     |     |     | 8                 |     |     |     |
2000
6
1500
4
1000
| 500 |     |     |     |     |     |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
| 0   | 50  | 100 | 150 | 200 250 | 300 | 350 | 0    |         |         |         |
| --- | --- | --- | --- | ------- | --- | --- | ---- | ------- | ------- | ------- |
|     |     |     |     |         |     |     | 0 50 | 100 150 | 200 250 | 300 350 |
Time [days]
Time [days]
(b) SINDy reconstruction using clean data
104
| 4500 |     |     |     |     |     |     | 14  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4000
12
3500
noitalupoP rotceV 10
noitalupoP tsoH 3000
| 2500 |     |     |     |     |     |     | 8   |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2000 |     |     |     |     |     |     | 6   |     |     |     |
1500
4
1000
| 500 |     |     |     |     |     |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
0
| 0   | 50  | 100 | 150         | 200 250 | 300 | 350 | 0 50 | 100 150     | 200 250 | 300 350 |
| --- | --- | --- | ----------- | ------- | --- | --- | ---- | ----------- | ------- | ------- |
|     |     |     | Time [days] |         |     |     |      | Time [days] |         |         |
Figure 3: Time evolution of the host and vector compartments obtained by numerically solving the original
CHIKV model. The left panel shows the host population dynamics, while the right panel shows the vector
| population | dynamics. |                |     |      |       |     |      |     |     |     |
| ---------- | --------- | -------------- | --- | ---- | ----- | --- | ---- | --- | --- | --- |
| 3.2 SINDy  |           | Reconstruction |     | from | Noisy |     | Data |     |     |     |
In practice, epidemiological time series are corrupted by observational noise, sampling fluctuations, and
underreporting. To investigate the sensitivity of SINDy to realistic data sets, we systematically add clean
| trajectories | with    | state-dependent |              | Gaussian | noise     | at  | different levels. |     |     |     |
| ------------ | ------- | --------------- | ------------ | -------- | --------- | --- | ----------------- | --- | --- | --- |
| 3.2.1        | Noise   | model and       | threshold    |          | selection |     |                   |     |     |     |
| Following    | (2.11), | noisy           | observations | are      | generated | as  |                   |     |     |     |
=X+εσ(X)N(0,I),
Y
whereε∈{5%,10%,20%,25%,30%,40%,50%}denotestherelativenoiseamplitudeandσ(X)istheempirical
λ˜
standard deviation of each state variable. The sparsity threshold in (2.15) is tuned for each noise level
11

Table4: Component-wiseRMSEbetweenthetrueCHIKVmodelandthediscoveredSINDymodels. Where
λ = 0.0000000001 for clean data, λ = 0.00002 for 5% noise, λ = 0.000028 for 10% noise, λ = 0.000001 for
20% noise, λ = 0.0006 for 25% noise, λ = 0.0006 for 30% noise, λ = 0.001 for 40% noise, and λ = 0.005 for
50% noise.
VAR Clean data 5% noise 10% noise 20% noise 25% noise 30% noise 40% noise 50% noise
S 0.0197 35.6759 96.3218 2.4341 80.0105 56.4741 54.4530 282.8390
h
| V   |     | 0.0001 |     | 0.0990 |     | 0.9548 |     | 0.0246 |     | 0.8502 |     | 0.9620 |     | 0.9561 | 2.0065 |
| --- | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | ------ |
h
E h 0.0019 5.3416 11.2494 0.6773 18.6239 13.5215 21.7616 50.0348
| I   |     | 0.0001 |     | 0.0401 |     | 0.0023 |     | 0.0010 |     | 0.0155 |     | 0.0159 |     | 0.0000 | 0.0000 |
| --- | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | ------ |
h
J h 0.0020 3.1800 10.3671 0.5330 17.1622 12.3184 20.4717 48.3326
| T   |     | 0.0001 |     | 0.0032 |     | 0.0016 |     | 0.0009 |     | 0.1170 |     | 0.0187 |     | 0.0181 | 0.1087 |
| --- | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------ | ------ |
h
R h 0.0214 27.9487 282.8673 2.3959 72.0374 78.7419 306.1954 778.6298
S 0.4893 1205.3428 2580.0147 116.5549 12409.5154 15878.6285 18115.5371 19219.8971
v
E v 0.1021 185.9490 973.8502 27.9961 983.1011 906.3452 1706.4929 2064.8223
I 0.5194 759.2170 3686.8817 94.1719 3344.0028 3238.3701 6343.3122 8083.9721
v
Table 5: Relative RMSE between the true CHIKV model and the discovered SINDy models. Where λ =
0.0000000001 for clean data, λ = 0.00002 for 5% noise, λ = 0.000028 for 10% noise, λ = 0.000001 for 20%
noise, λ = 0.0006 for 25% noise, λ = 0.0006 for 30% noise, λ = 0.001 for 40% noise, and λ = 0.005 for 50%
noise.
|     |       |     | Clean     | data  | 5%        | noise | 10%       | noise | 20%     | noise | 25%       | noise | 30%       | noise |     |
| --- | ----- | --- | --------- | ----- | --------- | ----- | --------- | ----- | ------- | ----- | --------- | ----- | --------- | ----- | --- |
|     | RMSE  |     | 0.2281    |       | 454.5252  |       | 1459.0231 |       | 48.2178 |       | 4076.2378 |       | 5132.7290 |       |     |
|     | rRMSE |     | 0.0000    |       | 0.0120    |       | 0.0385    |       | 0.0013  |       | 0.1076    |       | 0.1355    |       |     |
|     |       |     | 40%       | noise | 50%       | noise |           |       |         |       |           |       |           |       |     |
|     | RMSE  |     | 6094.4239 |       | 6631.0606 |       |           |       |         |       |           |       |           |       |     |
|     | rRMSE |     | 0.1609    |       | 0.1751    |       |           |       |         |       |           |       |           |       |     |
to balance two competing risks: thresholds that are too small admit noise-driven spurious terms, whereas
thresholds that are too large eliminate genuine physical terms. The values used are reported in the captions
| of    | Tables | 4 and | 5.           |     |         |     |     |     |     |     |     |     |     |     |     |
| ----- | ------ | ----- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.2.2 | Small  |       | noise regime |     | (ε≤10%) |     |     |     |     |     |     |     |     |     |     |
For small noise levels, the SINDy reconstruction retains qualitative agreement with the truth (Figs. 4(a)–
4(b)). The location of the epidemic peak, the relative ordering of compartmental amplitudes, and the
long-term decay are all preserved. Nevertheless, quantitative errors begin to accumulate, especially in the
vector compartments S , E , and I , which carry the largest absolute populations and are therefore most
|     |     |     |     | v v | v   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
exposedtoadditiveperturbations. Forinstance,theRMSEofS growsfrom0.4893(clean)to1205.34at5%
v
noise and to 2580.01 at 10% noise (Table 4). Although these errors remain small relative to the equilibrium
vector population, which yields a relative RMSE below 4%, they point to the derivative estimates, rather
than the states themselves, as the limiting factor. Numerical differentiation amplifies high-frequency noise
components, thereby contaminating the regression targets, even when the state observations appear visually
clean.
| 3.2.3 | Moderate-to-large |     |     |     | noise regime |     | (ε≥20%) |     |     |     |     |     |     |     |     |
| ----- | ----------------- | --- | --- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
At 20% noise (Fig. 4(c)), the reconstructed trajectories remain qualitatively consistent with the truth, yet
the RMSE is substantially higher than in the clean case. This behavior reflects the coupled effect of noise
λ˜
amplitude, sparsity threshold, and the conditioning of the regression matrix. The aggressive value of
required to suppress noise-induced terms also eliminates several small-magnitude coeﬀicients, yielding a
model that captures the correct qualitative structure but deviates quantitatively in compartments such as
12

| S and R | .   |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
| v h     |     |     |     |     |     |     |     |
For ε ≥ 25%, the reconstruction degrades consistently (Figs. 5(a)–5(c)). Three failure modes appear
concurrently: (i) the RMSE increases by three to four orders of magnitude relative to the clean case (Ta-
ble 5), reaching rRMSE ≈ 17% at 50% noise; (ii) the identified equations contain nonlinear interactions
absent from (2.4) (see Appendix B); and (iii) the resulting dynamics violate biological constraints, with
several compartments exhibiting non-physical oscillations or unbounded growth over the integration hori-
zon. The vector compartments are disproportionately affected because their larger absolute scale amplifies
| state-dependent |     | noise. |     |     |     |     |     |
| --------------- | --- | ------ | --- | --- | --- | --- | --- |
The degradation observed here is not specific to the CHIKV model but reflects a general limitation
of regression-based identification on time series. SINDy operates on numerically estimated derivatives Y˙ ,
and finite-difference or smoothing-based differentiation amplifies the noise present in Y. Once this noise
propagates into Y˙ , the least-squares problem (2.15) becomes ill-conditioned with respect to the bilinear
library, since several pairwise products are nearly collinear over the observed trajectories. The STLSQ
thresholding step then imposes a structural trade-off: a threshold large enough to suppress noise-driven
termsalsoeliminatesgenuinesmall-magnitudecouplings,whereasathresholdsmallenoughtoretainalltrue
couplings admits non-physical terms. The component-wise RMSE values in Table 4 quantify this trade-off:
compartmentswithsmallabsolutescale(I ,T )retainlowRMSEathighnoiselevelsbecausetheirdynamics
h h
are governed by a single dominant flow that persists under any admissible threshold, whereas compartments
| coupled to | multiple | flows (S | , R | , I ) accumulate | error | more rapidly. |     |
| ---------- | -------- | -------- | --- | ---------------- | ----- | ------------- | --- |
|            |          |          | v   | h v              |       |               |     |
Two implications follow. First, a single global sparsity threshold is inadequate for systems whose com-
partments span several orders of magnitude, motivating the development of compartment-wise or weighted-
regression variants of SINDy. Second, and central to the present study, an optimally tuned SINDy model
alone is insuﬀicient for trajectory reconstruction in the presence of realistic noise; it must instead be em-
ployed as a forecast operator within a data-assimilation framework that sequentially corrects the state using
observations. This is the role assigned to the EnKF in the experiments that follow.
| 3.3 State | Estimation |     | via | Ensemble | Kalman | Filtering |     |
| --------- | ---------- | --- | --- | -------- | ------ | --------- | --- |
We now examine the SINDy–DA approach, in which the SINDy-discovered model serves as the forecast
operator A in the state equation (2.16), and noisy observations are sequentially assimilated to update
n
the state estimate. This formulation addresses two limitations of pure SINDy identification: sensitivity to
observational noise, as documented in Section 3.2, and the requirement for full-state observations during
| training, a        | condition | rarely | satisfied | in epidemiological |     | surveillance. |     |
| ------------------ | --------- | ------ | --------- | ------------------ | --- | ------------- | --- |
| 3.3.1 Experimental |           | setup  |           |                    |     |               |     |
We consider a partially observed setting in which only the host compartments typically reported in surveil-
lance data—vaccinated (V ), infectious (I ), treated (J ), and recovered-under-treatment (T )—are accessi-
|     |     |     | h   | h   |     | h   | h   |
| --- | --- | --- | --- | --- | --- | --- | --- |
Theremainingsixcompartments{S }aretreatedasunobservedandinferredthrough
| ble. |     |     |     | ,E  | ,R ,S | ,E ,I |     |
| ---- | --- | --- | --- | --- | ----- | ----- | --- |
|      |     |     |     | h h | h     | v v v |     |
assimilation. Observations are perturbed by zero-mean Gaussian noise with covariance Ro calibrated to a
representative noise level. The EnKF is initialized with an ensemble of N e members drawn from a per-
turbation of the initial condition, and the forecast is propagated using the SINDy model identified from
noisy data. Sensitivity to the observation frequency is assessed by varying the time interval dt between
obs
| successive        | assimilation | cycles         | over | the range | [0.1,10]. |     |     |
| ----------------- | ------------ | -------------- | ---- | --------- | --------- | --- | --- |
| 3.3.2 Sensitivity |              | to observation |      | frequency |           |     |     |
Figure 7 reports the NRMSE and the temporal correlation between the EnKF estimate and the reference
trajectory for both observed and unobserved compartments as a function of dt . Three regimes are identi-
obs
fied.
≤1),theNRMSEremainsuniformlylow,andthecorrelationexceeds
Inthehigh-frequencyregime(dt
obs
0.95 across nearly all compartments. The assimilation interval is short relative to the characteristic time
scales of the host and vector dynamics, so that any drift introduced by the SINDy forecast is corrected
before it can amplify. The unobserved compartments are reconstructed with accuracy comparable to that of
13

(a) SINDy reconstruction from 5% noisy state data
104
| 4500 |     |     |     | 14  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
4000
12
3500
10
noitalupoP rotceV
noitalupoP tsoH 3000
| 2500 |     |     |     | 8   |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
2000
6
1500
4
1000
| 500  |             |         |         | 2    |             |         |         |
| ---- | ----------- | ------- | ------- | ---- | ----------- | ------- | ------- |
| 0    |             |         |         | 0    |             |         |         |
| 0 50 | 100 150     | 200 250 | 300 350 | 0 50 | 100 150     | 200 250 | 300 350 |
|      | Time [days] |         |         |      | Time [days] |         |         |
(b) SINDy reconstruction from 10% noisy state data
104
| 4500 |     |     |     | 14  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
4000
12
3500
10
| noitalupoP tsoH 3000 |     |     |     | noitalupoP rotceV |     |     |     |
| -------------------- | --- | --- | --- | ----------------- | --- | --- | --- |
2500
8
2000
6
1500
4
1000
| 500 |     |     |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0
| 0 50 | 100 150     | 200 250 | 300 350 | 0    |             |         |         |
| ---- | ----------- | ------- | ------- | ---- | ----------- | ------- | ------- |
|      |             |         |         | 0 50 | 100 150     | 200 250 | 300 350 |
|      | Time [days] |         |         |      | Time [days] |         |         |
(c) SINDy reconstruction from 20% noisy state data
104
14
4500
4000
12
3500
10
| 3000 |     |     |     | noitalupoP rotceV |     |     |     |
| ---- | --- | --- | --- | ----------------- | --- | --- | --- |
noitalupoP tsoH
| 2500 |     |     |     | 8   |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
2000
6
1500
4
1000
| 500 |     |     |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0
0
| 0 50 | 100 150 | 200 250 | 300 350 | 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- | ---- | ------- | ------- | ------- |
Time [days]
Time [days]
Figure4: NumericalsimulationoftheSINDy-identifiedCHIKVmodelusingnoisystatemeasurements. The
left panel shows the host compartments, and the right panel shows the vector compartments.
14

(a) SINDy reconstruction from 25% noisy state data
104
| 4500 |     |     |     | 16  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
4000
14
3500
12
| 3000            |     |     |     | noitalupoP rotceV |     |     |     |
| --------------- | --- | --- | --- | ----------------- | --- | --- | --- |
| noitalupoP tsoH |     |     |     | 10                |     |     |     |
2500
8
2000
6
1500
4
1000
2
500
0
0
| 0 50 | 100 150 | 200 250 | 300 350 | 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- | ---- | ------- | ------- | ------- |
Time [days]
Time [days]
(b) SINDy reconstruction from 30% noisy state data
104
| 4500 |     |     |     | 20  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
4000
3500
15
| noitalupoP tsoH 3000 |     |     |     | noitalupoP rotceV |     |     |     |
| -------------------- | --- | --- | --- | ----------------- | --- | --- | --- |
2500
10
2000
1500
| 1000 |     |     |     | 5   |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
500
0
| 0 50 | 100 150     | 200 250 | 300 350 | 0    |             |         |         |
| ---- | ----------- | ------- | ------- | ---- | ----------- | ------- | ------- |
|      |             |         |         | 0 50 | 100 150     | 200 250 | 300 350 |
|      | Time [days] |         |         |      | Time [days] |         |         |
(c) SINDy reconstruction from 40% noisy state data
104
| 4500 |     |     |     | 20  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
4000
15
3500
3000
| noitalupoP tsoH |     |     |     | noitalupoP rotceV |     |     |     |
| --------------- | --- | --- | --- | ----------------- | --- | --- | --- |
| 2500            |     |     |     | 10                |     |     |     |
2000
5
1500
1000
0
500
| 0    |             |         |         | -5   |             |         |         |
| ---- | ----------- | ------- | ------- | ---- | ----------- | ------- | ------- |
| 0 50 | 100 150     | 200 250 | 300 350 |      |             |         |         |
|      |             |         |         | 0 50 | 100 150     | 200 250 | 300 350 |
|      | Time [days] |         |         |      | Time [days] |         |         |
Figure5: NumericalsimulationoftheSINDy-identifiedCHIKVmodelusingnoisystatemeasurements. The
left panel shows the host compartments, and the right panel shows the vector compartments.
15

SINDy reconstruction from 50% noisy state data
104
| 4500 |     |     |     | 16  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
| 4000 |     |     |     | 14  |     |     |     |
3500
12
| 3000            |     |     |     | noitalupoP rotceV |     |     |     |
| --------------- | --- | --- | --- | ----------------- | --- | --- | --- |
| noitalupoP tsoH |     |     |     | 10                |     |     |     |
2500
8
2000
6
1500
4
1000
2
| 500  |             |         |     | 0    |             |         |         |
| ---- | ----------- | ------- | --- | ---- | ----------- | ------- | ------- |
| 0    |             |         |     | -2   |             |         |         |
| 0 50 | 100 150     | 200 250 | 300 | 350  |             |         |         |
|      |             |         |     | 0 50 | 100 150     | 200 250 | 300 350 |
|      | Time [days] |         |     |      | Time [days] |         |         |
Figure6: NumericalsimulationoftheSINDy-identifiedCHIKVmodelusingnoisystatemeasurements. The
left panel shows the host compartments, and the right panel shows the vector compartments.
the observed ones, indicating that the cross-compartment correlations encoded in the ensemble covariance
effectively propagate information from the observed subset to the unobserved states.
|     |     | ≤   | ≤   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
In the intermediate regime (1 dt obs 5), the NRMSE increases moderately, and the correlation
decreasesforunobservedcompartments,particularlythoseweaklycoupledtotheobservedsubset. Thefilter
remains stable, but its skill becomes increasingly dependent on the accuracy of the SINDy forecast between
| assimilation steps. |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
In the low-frequency regime (dt ≥ 5), the estimation error grows substantially. The interval between
obs
updates is long enough for the SINDy-driven forecast to accumulate model error, and a single observation
is insuﬀicient to reproject the full ten-dimensional state onto the true trajectory. This regime delineates a
structural limit of the framework: data assimilation can correct, but does not replace, model accuracy.
Table 6: RMSE comparison between the noisy SINDy trajectory and the SINDy–EnKF posterior estimate.
|     | State | RMSE SINDy | RMSE | SINDy–EnKF | Reduction | (%) |     |
| --- | ----- | ---------- | ---- | ---------- | --------- | --- | --- |
|     | S     | 79.3176    |      | 0.3347     | 99.58     |     |     |
h
|     | V h | 0.8690  |     | 0.1254 | 85.56 |     |     |
| --- | --- | ------- | --- | ------ | ----- | --- | --- |
|     | E   | 18.3900 |     | 0.1678 | 99.09 |     |     |
h
|     | I   | 0.0122 |     | 0.0462 | -279.02 |     |     |
| --- | --- | ------ | --- | ------ | ------- | --- | --- |
h
|     | J   | 16.9518 |     | 0.1291 | 99.24 |     |     |
| --- | --- | ------- | --- | ------ | ----- | --- | --- |
h
|     | T   | 0.1155 |     | 0.0718 | 37.87 |     |     |
| --- | --- | ------ | --- | ------ | ----- | --- | --- |
h
|     | R h | 71.1182    |     | 0.9163  | 98.71 |     |     |
| --- | --- | ---------- | --- | ------- | ----- | --- | --- |
|     | S   | 12605.0025 |     | 33.3287 | 99.74 |     |     |
v
|     | E   | 977.5464 |     | 7.6687 | 99.22 |     |     |
| --- | --- | -------- | --- | ------ | ----- | --- | --- |
v
|     | I   | 3335.5796 |     | 27.8186 | 99.17 |     |     |
| --- | --- | --------- | --- | ------- | ----- | --- | --- |
v
| 3.3.3 Recovery | of unobserved | state | variables |     |     |     |     |
| -------------- | ------------- | ----- | --------- | --- | --- | --- | --- |
The framework also recovers compartments that are never directly measured—a setting in which SINDy
alone is not applicable, since no derivative data are available for those states. The EnKF achieves this
by accumulating cross-compartment covariances across the ensemble: information from the infectious host
population I , for example, is propagated through model-induced couplings to update the susceptible vector
h
population S , even though the latter is not directly observed. Figure 7 confirms that this indirect inference
v
is reliable for suﬀiciently frequent observations and degrades smoothly as the observation interval increases.
16

4
1
3.5
0.9
0.8
3
0.7
2.5
0.6
| ESMRN |     |     | noitalerroC |     |     |
| ----- | --- | --- | ----------- | --- | --- |
2
0.5
0.4
1.5
0.3
1
0.2
0.5
0.1
| 0    |     |     | 0    |            |     |
| ---- | --- | --- | ---- | ---------- | --- |
| 10-1 | 100 | 101 | 10-1 | 100        | 101 |
|      | dt  |     |      | dt  (days) |     |
|      | obs |     |      | obs        |     |
Figure 7: Sensitivity of Ensemble Kalman Filter to the observational time interval dt for the CHIKV
obs
model (2.4). The left panel shows the Normalized Root Mean Square Error, while the right panel shows the
correlation between the host and vector compartments. Data points represent intervals ranging from 0.1 to
10. Observed variables: V , I , J , and T . Unobserved variables: S , E , R , S , E , and I .
|     | h h h | h   | h h | h v v | v   |
| --- | ----- | --- | --- | ----- | --- |
17

4
2
0
|     | 0   | 50 100 | 150 | 200 250 | 300 350 |
| --- | --- | ------ | --- | ------- | ------- |
10
5
0
|     | 0   | 50 100 | 150 | 200 250 | 300 350 |
| --- | --- | ------ | --- | ------- | ------- |
200
100
0
|     | 0   | 50 100 | 150 | 200 250 | 300 350 |
| --- | --- | ------ | --- | ------- | ------- |
2
1
0
|     | 0   | 50 100 | 150 | 200 250 | 300 350 |
| --- | --- | ------ | --- | ------- | ------- |
Figure 8: EnKF reconstruction of observed host compartments. Comparison of the 25% noisy
SINDy trajectory, forecast prior mean, true clean trajectory, filtered posterior mean, and observations for
| the observed | compartments | V , I , J , | and T . |     |     |
| ------------ | ------------ | ----------- | ------- | --- | --- |
|              |              | h h h       | h       |     |     |
18

1000
500
0
| 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- |
4
2
0
| 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- |
200
100
0
| 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- |
10
5
0
| 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- |
200
100
0
| 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- |
2
1
0
| 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- |
5000
0
| 0 50 | 100 150 | 200 250 | 300 350 |
| ---- | ------- | ------- | ------- |
Figure9: EnKFreconstructionofhostcompartments. Comparisonofthe25%noisySINDytrajectory,
forecastpriormean, truecleantrajectory, andfilteredposteriormeanforallhostcompartments. TheEnKF
corrects the noisy SINDy forecast and closely tracks the clean reference dynamics.
19

104
15
10
5
0
0 50 100 150 200 250 300 350
15000
10000
5000
0
0 50 100 150 200 250 300 350
104
6
4
2
0
0 50 100 150 200 250 300 350
Figure 10: EnKF reconstruction of vector compartments. Comparison of the 25% noisy SINDy
trajectory,forecastpriormean,truecleantrajectory,andfilteredposteriormeanforthevectorcompartments
S , E , and I . The filtered estimates remain close to the true clean trajectories despite noise-induced
v v v
deviations in the SINDy forecast.
20

The robustness of the integrated framework arises from the complementarity of its two components.
SINDy provides an interpretable, parsimonious forecast model whose structure encodes the dominant mass-
action interactions of the CHIKV system; without such a model, the EnKF would lack a propagator and
couldnotinferunobservedstatevariables. WhenSINDyisidentifiedfromnoisydata,however,thediscovered
systemcarriesnon-negligiblemodelerror,whilethemeasurementsthemselvesaresubjecttoobservationerror.
The EnKF reconciles these two sources of uncertainty by producing a statistically optimal state estimate
that weights the SINDy forecast and the observations according to their respective error covariances Q
n
and Ro (see (2.16)–(2.17)). Neither component alone yields reliable trajectory reconstruction under realistic
conditions: SINDy degrades under moderate-to-high noise, and the EnKF cannot be deployed without a
forecast model. Their combination yields accurate estimates of both observed and unobserved states with
quantifiable uncertainty.
Figures 8–10 illustrate the performance of the EnKF when applied to the 25% noisy SINDy-generated
trajectories. The noisy SINDy trajectory exhibits visible deviations from the true clean dynamics, especially
during the transient phase and near the epidemic peaks. This is most evident in the exposed and infectious
vector compartments, where the noisy SINDy trajectory underestimates the peak magnitude and shows
noticeable long-time bias.
For the observed host compartments V , I , J , and T , the filtered posterior mean closely follows the
h h h h
true clean trajectory and substantially improves upon the noisy SINDy trajectory. The observation points
coincide with the noisy SINDy trajectory at the assimilation times, but the posterior estimate does not
simply interpolate these noisy values. Instead, the EnKF balances information from the forecast model and
observations via the Kalman gain, yielding a smoother, dynamically consistent reconstruction.
A particularly important result is the recovery of unobserved compartments. Although S , E , R , S ,
h h h v
E , and I are not directly assimilated, their posterior estimates remain close to the true clean trajectories.
v v
This demonstrates that the ensemble covariance successfully transfers information from the observed com-
partments to the unobserved states. In particular, the vector compartments are reconstructed accurately
even though they are not directly observed, indicating that the host–vector coupling encoded in the forecast
model provides suﬀicient dynamical information for indirect state correction.
Table 6 shows that incorporating the EnKF substantially improves the accuracy of the SINDy forecasts.
For most compartments, the RMSE is reduced by more than 98%, with the largest improvements observed
in the vector populations (S , E , and I ), where error reductions exceed 99%. These results demonstrate
v v v
that sequential data assimilation effectively corrects forecast errors caused by noisy model identification
and enables accurate reconstruction of both observed and unobserved states. The only exception is the
symptomatic infectious compartment I , for which the noisy SINDy trajectory already exhibits a very small
h
RMSE. Consequently, minor EnKF corrections lead to a slightly larger error, although the absolute RMSE
remains negligible.
These results show that the EnKF corrects the trajectory-level errors introduced by noisy SINDy model
discovery. WhilestandaloneSINDyissensitivetonoiseandmayproducebiasedtrajectories,thefilteringstep
suppressesthesedeviationsandrecoversbiologicallyplausibledynamics. Thissupportstheuseofthehybrid
SINDy–EnKF framework for epidemic systems in which only partial and noisy observations are available.
4 Conclusion
Thisstudydevelopedadata-drivenframeworktodiscoverandinferthetransmissiondynamicsofthechikun-
gunyavirus(CHIKV)byintegratingSparseIdentificationofNonlinearDynamics(SINDy)withtheEnsemble
KalmanFilter(EnKF).Theconclusionsaretwo-fold: First,theresultsshowthatSINDyaccuratelyrecovers
thegoverningequationsoftheCHIKVmodelwhenhigh-quality,noise-freedataareavailable. Inthisregime,
the identified models reproduce the temporal dynamics of both host and vector populations with high fi-
delity, confirming the effectiveness of sparse regression in capturing the dominant interactions underlying
the system. Second, the numerical tests also reveal an inherent limitation of SINDy when applied to noisy
epidemiological data. As the level of observational noise increases, the accuracy of the reconstructed dy-
namics deteriorates due to the sensitivity of derivative estimation and the instability introduced by sparsity
thresholding. This leads to spurious nonlinear terms and a loss of interpretability in the identified models,
particularly under moderate-to-high noise conditions. These findings highlight that, while SINDy is a pow-
21

erful tool for model discovery, its direct application to real-world problems requires additional mechanisms
to ensure robustness.
The EnKF results further demonstrate that the proposed hybrid framework can mitigate the limitations
ofstandaloneSINDywhenappliedtonoisydata. AlthoughSINDyalonebecomessensitivetomoderateand
large noise levels, coupling it with sequential data assimilation allows noisy forecasts to be corrected using
availableobservations. Theposteriorestimatescloselytrackthecleanreferencetrajectoriesandrecoverboth
observed and unobserved compartments, including the vector states. Thus, the SINDy–EnKF framework
provides a more reliable approach for learning and reconstructing CHIKV dynamics from incomplete and
noise-contaminated data.
The RMSE analysis further confirms that the SINDy–EnKF framework reduces state estimation errors
bymorethan98%inmostepidemiologicalcompartmentsandbyover99%inthevectorpopulation, demon-
strating its effectiveness for reconstructing both observed and unobserved disease states from noisy and
incomplete surveillance data.
Several directions extend naturally from the present study. The trade-off between sparsity and accuracy
identified in Section 3.2 motivates the development of noise-robust extensions of SINDy, including weak-
form formulations that bypass explicit derivative estimation, ensemble-SINDy approaches that aggregate
sparse models over bootstrapped subsets of the data, and compartment-wise or weighted-regression vari-
ants that account for the differing absolute scales of host and vector populations. A second direction is to
replace or augment the bilinear candidate library with neural representations of the underlying dynamics.
Physics-informed neural networks (PINNs) can encode known conservation and balance constraints of the
CHIKV system while learning residual terms directly from data, thereby offering improved robustness to
noise compared with library-based identification. Neural ordinary differential equations (Neural ODEs) pro-
vide a continuous-time framework in which the right-hand side f(x) is parameterized by a neural network
and trained jointly with the observed trajectories, making them well-suited to settings where the governing
equations admit no parsimonious closed form. To preserve the interpretability that motivated the SINDy
formulation, hybrid models—in which a sparse mechanistic core captures the dominant mass-action interac-
tions and a neural network learns residual dynamics or unresolved processes—offer a particularly attractive
avenue. Such hybrid architectures can also be embedded as forecast operators within the EnKF, extending
the SINDy–EnKF coupling developed here to higher-capacity propagators. On the assimilation side, itera-
tiveandlocalizedvariantsoftheEnKF(IEnKF,LETKF)canimproveperformanceunderstronglynonlinear
dynamics and high state dimension, while joint state–parameter estimation would allow the SINDy coeﬀi-
cientsthemselvestobeupdatedonlineasnewobservationsbecomeavailable,blurringthecurrentseparation
between offline identification and online assimilation. Finally, the framework can be extended to richer
formulations of CHIKV dynamics—including spatial heterogeneity through reaction–diffusion or metapop-
ulation models, stochastic compartmental models that capture demographic and environmental variability,
and age- or risk-structured populations—and validated against real surveillance data from past CHIKV out-
breaks, with potential applications in outbreak monitoring, real-time forecasting, and public-health decision
support.
Availability of data and material
Real-world data were not used in this study. The code used to generate synthetic data and simulations is
available on GitHub.
Supporting information
Appendix A. The CHIKV model (2.4) can be equivalently expressed in matrix–vector form. Appendix B.
Discovered SINDy equations. Appendix C. Numerical results evaluating the performance of the Sparse
Identification of Nonlinear Dynamics (SINDy) framework when trained on partial and noisy data.
Authors’ contributions
B.A.A.: conceptualization, investigation, methodology, software, writing—original draft, writing—review
and editing; C.M.: conceptualization, investigation, methodology, supervision, writing — original draft,
22

writing—reviewandediting; L.F.G.: investigation, supervision, writing—originaldraft, writing—review
and editing. All authors gave final approval for publication and agreed to be held accountable for the work
| performed | there.       |             |           |             |     |           |           |        |     |     |     |     |     |     |
| --------- | ------------ | ----------- | --------- | ----------- | --- | --------- | --------- | ------ | --- | --- | --- | --- | --- | --- |
| Conflicts |              | of Interest |           |             |     |           |           |        |     |     |     |     |     |     |
| We        | declare that | no          | conflicts | of interest | or  | financial | conflicts | exist. |     |     |     |     |     |     |
Funding
Not applicable.
| Appendix |     | A:  | CHIKV |     | model |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The component-wise ODE system (1) presented in Section 2 can be equivalently written in matrix–vector
| form. | Defining | the | state vector |         |     |     |     |     |     |         |     |     |     |     |
| ----- | -------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
|       |          |     |              | (cid:2) |     |     |     |     |     | (cid:3) |     |     |     |     |
⊤
|     |              |     | x(t)=   | S V  | E           | I   | J T | R         | S E | I   | ∈R10, |     |     | (.1) |
| --- | ------------ | --- | ------- | ---- | ----------- | --- | --- | --------- | --- | --- | ----- | --- | --- | ---- |
|     |              |     |         | h    | h           | h h | h   | h h       | v   | v v |       |     |     |      |
| the | system takes | the | compact | form |             |     |     |           |     |     |       |     |     |      |
|     |              |     |         |      | x˙(t)=b+A(λ |     |     | ,λ )x(t), |     |     |       |     |     | (.2) |
h v
| where | the constant |     | vector | is      |     |     |     |     |     |         |     |     |     |     |
| ----- | ------------ | --- | ------ | ------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
|       |              |     |        | (cid:2) |     |     |     |     |     | (cid:3) |     |     |     |     |
⊤
|     |                     |     |        | Λ      | h 0 | 0 0 | 0 0      | 0 Λ v    | 0 0 | ,   |     |     |     | (.3) |
| --- | ------------------- | --- | ------ | ------ | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | ---- |
| and | the state-dependent |     | system | matrix | A(λ | ,λ  | )∈R10×10 | is given | by  |     |     |     |     |      |
h v
|     |       |         | 0   |       |     |     |     |     |     |     |     |     | 1   |      |
| --- | ----- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |       |         | −C  | ω     |     | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |      |
|     |       |         | B 1 |       |     |     |     |     |     |     |     |     | C   |      |
|     |       |         | θ   | −C    |     | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |      |
|     |       |         | B   | 2     |     |     |     |     |     |     |     |     | C   |      |
|     |       |         | B   | (1−η) |     | −C  |     |     |     |     |     |     | C   |      |
|     |       |         | B λ | λ     |     |     | 0   | 0   | 0   | 0   | 0   | 0   | 0 C |      |
|     |       |         | B h | h     |     | 3   |     |     |     |     |     |     | C   |      |
|     |       |         | B 0 | 0     |     | ρσ  | −C  | 0   | 0   | 0   | 0   | 0   | 0 C |      |
|     |       |         |     |       |     | h   |     | 4   |     |     |     |     |     |      |
|     |       |         | B   |       | (1− |     |     | −   |     |     |     |     | C   |      |
|     |       |         | B 0 | 0     |     | ρ)σ | h 0 | C 5 | 0   | 0   | 0   | 0   | 0 C |      |
|     | A(λ h | ,λ v )= | B   |       |     |     |     |     |     |     |     |     | C . | (.4) |
|     |       |         | B 0 | 0     |     | 0   | τ   | 0   | − C | 0   | 0   | 0   | 0 C |      |
|     |       |         | B   |       |     |     |     |     | 6   |     |     |     | C   |      |
|     |       |         | 0   | 0     |     | 0   | γ   | γ   | γ   | −µ  | 0   | 0   | 0   |      |
|     |       |         | B   |       |     |     |     | s a | T   | h   |     |     | C   |      |
|     |       |         | B   |       |     |     |     |     |     |     | −C  |     | C   |      |
|     |       |         | B 0 | 0     |     | 0   | 0   | 0   | 0   | 0   |     | 7 0 | 0 C |      |
|     |       |         | @   |       |     |     |     |     |     |     |     |     | A   |      |
|     |       |         | 0   | 0     |     | 0   | 0   | 0   | 0   | 0   | λ   | −C  | 0   |      |
|     |       |         |     |       |     |     |     |     |     |     | v   | 8   |     |      |
|     |       |         | 0   | 0     |     | 0   | 0   | 0   | 0   | 0   | 0   | σ   | −µ  |      |
|     |       |         |     |       |     |     |     |     |     |     |     | v   | v   |      |
Where C =λ +θ+µ , C =λ (1−η)+ω+µ , C =σ +µ , C =τ+γ +µ +δ , C =γ +µ +δ ,
|     | 1   | h   | h   | 2 h |     |     | h 3 | h   | h 4 |     | s h | h   | 5 a | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C =γ +µ +δ , C =λ +µ , C =σ +µ . Here λ =β I /N and λ =β (ϵ I +ϵ J +ϵ T )/N
| 6   | T   | h h | 7   | v v | 8   | v v |     | h v | v v |     | v h | 1 h | 2 h 3 | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
are the forces of infection on the host and vector populations, respectively (see Section 2 for parameter
definitions). Becauseλ andλ dependonthestatex,thematrixAisitselfstate-dependent,so(.2)remains
|     |     |     | h   | v   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anonlinearsystem. TheblockstructureofAreflectsthedecouplingbetweenhostandvectordynamicsatthe
linearlevel: theupper-left7×7blockgovernsthehostcompartments,thelower-right3×3blockgovernsthe
vector compartments, and the two populations are coupled exclusively through the force-of-infection terms
| λ   | and λ . |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
h v
Appendix B: SINDy identification using partial and noisy data
This appendix presents additional numerical results evaluating the performance of the Sparse Identification
ofNonlinearDynamics(SINDy)frameworkwhentrainedonincompletedata. Specifically, onlythefirsthalf
ofthetime-seriesdataisusedformodeldiscovery,andtherobustnessofthemethodisfurtherassessedinthe
presence of additive noise (25% noise level). The resulting models are simulated over the full time horizon
and qualitatively compared with expected system behavior. These results highlight the sensitivity of SINDy
to both data availability and noise contamination in high-dimensional epidemiological systems.
23

(a) SINDy reconstruction using partial training data
4500
4000
3500
3000
2500
2000
1500
1000
500
0
0 20 40 60 80 100 120 140 160 180
Time
(b) SINDy reconstruction using partial training data with 25% noise
noitalupoP
tsoH
14
12
10
8
6
4
2
0
0 20 40 60 80 100 120 140 160 180
Time [days]
noitalupoP
rotceV
104
4500
4000
3500
3000
2500
2000
1500
1000
500
0
0 20 40 60 80 100 120 140 160 180
Time [days]
noitalupoP
tsoH
7
6
5
4
3
2
1
0
-1
0 20 40 60 80 100 120 140 160 180
Time [days]
noitalupoP
rotceV
1064
Figure 11: Numerical simulations show the trajectories obtained when SINDy is trained on only the first
half of the clean dataset. The left panel shows the reconstructed host dynamics, and the right panel shows
the reconstructed vector dynamics.
24

| Appendix | C: Discovered | SINDy | equations |
| -------- | ------------- | ----- | --------- |
25

Table 7: Discovered SINDy equations with different data.
S˙ =−0.0237S −0.0005S2+0.0133E2+0.0057J2−0.0003R2 +0.0000S2−0.0002I2
h v h h h h v v
+0.0014S S −0.0599V E +0.0643V J +0.0028V R +0.0001V S +0.0022V E
h v h h h h h h h v h v
+0.0008E S −0.0663E E −0.0620I J −0.0042I R −0.0002I S −0.0009I E
h v h v h h h h h v h v
+0.0004I I +0.0089J S −0.0462J I +0.0001T E
h v h v h v h v
V˙ =0.0000
h
E˙ =0.0237S +0.0005S2−0.0135E2−0.0055J2+0.0003R2 +0.0002I2−0.0015S v
h v h h h h v h
+0.0599V E −0.0644V J −0.0028V R −0.0001V S −0.0022V E −0.0008E S
h h h h h h h v h v h v
+0.0664E E +0.0621I J +0.0042I R +0.0002I S +0.0009I E −0.0004I I
h v h h h h h v h v h v
−0.0089J S +0.0461J I −0.0001T E
h v h v h v
I˙ =0.0001S
h v
J˙ =−0.0001S +0.0002E2−0.0003J2+0.0001V E −0.0001V J −0.0001E E
h v h h h h h h h v
−0.0002I J
h h
T˙ =0.0000
h
Clean data R˙ =−0.0001S +0.0001J2−0.0001V E +0.0001V J −0.0001E E −0.0001J I
h v h h h h h h v h v
S˙ =−0.1704S +0.0092S2+0.0122E2−0.0126∗Jh2+0.0005R2 +0.0005E2
v v h h h v
−0.0006I2−0.0187S S +0.0740V E −0.0060V J +0.0348V R +0.0009V S
v h v h h h h h h h v
+0.0007V E +0.0013V I +0.0071E S −0.0058E E −0.0798I J −0.0142I R
h v h v h v h v h h h h
−0.0016I S −0.0047I E +0.0004I I +0.0225J S −0.1255J I +0.0002T R
h v h v h v h v h v h h
+0.0003T E +0.0001T I
h v h v
E˙ =−0.0077S −0.0013E2+0.0085J2−0.0001R2 −0.0003E2+0.0005S S
v v h h h v h v
+0.0162V E +0.0018V J −0.0049V R +0.0001V S −0.0005V E +0.0001V I
h h h h h h h v h v h v
+0.0003E S +0.0070∗EhEv+0.0140I J +0.0037I R +0.0002I S −0.0008I E
h v h h h h h v h v
+0.0001I I +0.0020J S −0.0035J I −0.0002T E
h v h v h v h v
I˙ =0.0005S −0.0001E2−0.0051J2+0.0004E2−0.0002I2+0.0006S S
v v h h v v h v
+0.0035V E −0.0086V J −0.0028V R +0.0002V S +0.0002V E −0.0002V I
h h h h h h h v h v h v
−0.0001E S +0.0063E E +0.0135I J +0.0021I R −0.0001I S +0.0007I E
h v h v h h h h h v h v
−0.0002I I +0.0009J S +0.0063J I +0.0001T E
h v h v h v h v
S˙ =0.0248S +0.0015R +0.0010E +0.0001I −0.0014V2+0.0002E2−0.0278I2
h h h v v h h h
−0.0011J2−0.0086T2+0.0739S E +0.0842S J −0.0007S R −0.0004S E
h h h h h h h h h v
−0.0003S I +0.0001V E +0.4605V I −0.0003V J −0.3950V T −0.0001V R
h v h h h h h h h h h h
+0.2623E J −0.0130E R +0.0004E S −0.0033E E −0.0030E I −0.0003I J
h h h h h v h v h v h h
+0.6727I T +0.0001I R +0.0075J R −0.0001J S +0.0011J E −0.0012J I
h h h h h h h v h v h v
V˙ =0.0001S +0.0002S E −0.0004S J
h h h h h h
E˙ =−0.0275S −0.0001R +0.0000S −0.0015E −0.0001I +0.0021V2
h h h v v v h
−0.0004E2+0.0291I2+0.0012J2+0.0098T2−0.0191S E −0.1507S J
h h h h h h h h
+0.0008S R +0.0004S E +0.0004S I −0.0005V E −0.4577V I +0.0005V J
h h h v h v h h h h h h
+0.4499V T −0.2774E J +0.0135E R −0.0005E S +0.0033E E +0.0030E I
h h h h h h h v h v h v
+0.0001I J −0.6640I T −0.0000I R −0.0089J R +0.0001J S −0.0004J E
h h h h h h h h h v h v
+0.0010J I
h v
5% noise I˙ =−0.0002I2+0.0001V I −0.0006V T +0.0005E J +0.0007I T
h h h h h h h h h h
J˙ =0.0008S −0.0014R +0.0000S −0.0014E +0.0001I +0.0004V2+0.0000E2
h h h v v v h h
+0.0003I2+0.0978S E −0.0942S J −0.0002V E +0.0109V I +0.0003V J
h h h h h h h h h h h
+0.0211V T −0.0229E J +0.0001E R +0.0002E E +0.0001I J −0.0750I T
h h h h h h h v h h h h
+0.0009J R −0.0002J E +0.0001J I
h h h v h v
T˙ =0.0001I2−0.0001T2+0.0002V I +0.0001V T −0.0001E J −0.0004I T
h h h h h h h h h h h
−0.0001J R
h h
R˙ =0.0100S +0.0001R +0.0023E +0.0012V2−0.0007I2−0.0002J2−0.0003T2
h h h v h h h h
−0.0017S E +0.1250S J −0.0009S R −0.0006S E +0.0001V E −0.0066V I
h h h h h h h v h h h h
−0.0004V J −0.1026V T +0.0684E J −0.0005E R −0.0006E E +0.0640I T
h h h h h h h h h v h h
+0.0018J R −0.0013J E
h h h v
S˙ =12.2165S +1.5204R −0.0125S +0.6934E +0.0608I −0.0031S2+0.8264V2
v h h v v v h h
+0.0287E2+0.0783I2+0.0258J2−0.3884T2−0.0008R2 −0.0001S2−0.0010E2
h h h h h v v
−11.1410S E −8.6683S J +0.1886S R −0.0033S S +0.2817S E −0.0150S I
h h h h 26 h h h v h v h v
+0.0385V E −3.2008V I −0.0327V J −3.4033V T +0.0111V R −0.0002V S
h h h h h h h h h h h v

+0.0010V E −0.3487E J −0.1068E R +0.0027E S +0.0296E E −0.0148I J
h v h h h h h v h v h h
−5.6657I T +0.0187I R −0.0005I S +0.0026I E −0.0003I I −0.1840J R
h h h h h v h v h v h h
+0.0061J S +0.0626J E +0.0073J I −0.0004T R −0.0003T E −0.0001S E
h v h v h v h h h v v v
5% noise E˙ =0.5005S −0.2497R −0.0007S −0.2900E +0.0058I −0.0001S2+0.0401V2
v h h v v v h h
−0.0162E2−0.0330I2−0.0030J2+0.0737T2−0.0003R2 +0.0000E2+4.7099S E
h h h h h v h h
+2.8094S J −0.0606S R −0.0535S E −0.0029S I +0.0142V E +1.4622V I
h h h h h v h v h h h h
−0.0129V J +1.9717V T −0.0058V R +0.0001V S −0.0010V E −0.0001V I
h h h h h h h v h v h v
+0.1171E J +0.0413E R −0.0009E S −0.0150E E +0.0003E I −0.0111I J
h h h h h v h v h v h h
+3.8198I T −0.0085I R +0.0003I S +0.0006I E +0.0001I I +0.0425J R
h h h h h v h v h v h h
−0.0024J S −0.0264J E −0.0068J I +0.0001T R
h v h v h v h h
I˙ =0.3300E −0.0714I
v v v
S˙ =0.0015S +0.0009R +0.0023E −0.0001I −0.0020V2+0.0002E2−0.0170I2
h h h v v h h h
−0.0008J2+0.0144T2−0.0657S E +0.1493S J −0.0007S R −0.0010S E
h h h h h h h h h v
−0.0002S I +0.0002V E +0.6352V I +0.0002V J +0.0252V T −1.6367E I
h v h h h h h h h h h h
−0.0359E J +0.0028E R +0.0001E S +0.0044E E −0.0039E I −0.0006I J
h h h h h v h v h v h h
+0.3265I T +0.0081J R −0.0003J S −0.0036J E
h h h h h v h v
V˙ =0.0001S −0.0002S E
h h h h
E˙ =−0.0045S +0.0005R −0.0031E +0.0001I +0.0030V2−0.0003E2+0.0168I2
h h h v v h h h
+0.0009J2−0.0109T2+0.0323S E −0.1455S J +0.0011S R +0.0013S E
h h h h h h h h h v
+0.0003S I −0.0004V E −0.6503V I +0.0129V T +1.8145E I +0.0342E J
h v h h h h h h h h h h
−0.0025E R −0.0001E S −0.0043E E +0.0040E I +0.0003I J −0.3293I T
h h h v h v h v h h h h
−0.0086J R +0.0003J S +0.0043J E −0.0001J I
h h h v h v h v
I˙ =−0.0002I2−0.0004V I +0.0005V T −0.0033E I −0.0014E J −0.0006I T
h h h h h h h h h h h h
J˙ =−0.0010S −0.0009R −0.0008E +0.0003V2+0.0001E2−0.0002I2−0.0001J2
h h h v h h h h
+0.0012T2+0.0782S E −0.0741S J −0.0005V E +0.0082V I +0.0011V J
h h h h h h h h h h h
−0.0015V T +0.0413E I −0.0061E J +0.0001E R −0.0004I J −0.0356I T
h h h h h h h h h h h h
+0.0003J R
h h
T˙ =−0.0001T2+0.0002S E −0.0002S J +0.0037V I −0.0001V T −0.0086E I
h h h h h h h h h h h h
−0.0028I T
h h
10% noise R˙ =0.0127S −0.0005R +0.0024E −0.0047V2−0.0001I2−0.0001J2−0.0029T2
h h h v h h h h
+0.0122S E +0.1170S J −0.0003S R −0.0009S E −0.0001V E +0.0043V I
h h h h h h h v h h h h
−0.0002V J −0.0369V T −0.1153E I +0.0229E J −0.0001E R −0.0003E E
h h h h h h h h h h h v
+0.0638I T +0.0007J R −0.0011J E
h h h h h v
S˙ =19.4872S −0.2197R −0.0004S +0.2936E +0.0724I −0.0068S2+1.1518V2
v h h v v v h h
+0.0372E2−0.4306I2−0.0098J2−0.2813T2−0.0005R2 −0.0001S2−0.0004E2
h h h h h v v
−0.0001I2−14.8475S E +2.9486S J −0.0706S R +0.0006S S +0.1045S E
v h h h h h h h v h v
−0.0032S I +0.1591V E −4.8922V I −0.1427V J −7.3636V T +0.0170V R
h v h h h h h h h h h h
−0.0003V S −0.0009V E +0.0002V I +17.5942E I +2.5529E J −0.0640E R +
h v h v h v h h h h h h
0.0031E S +0.0173E E −0.0004E I +0.1353I J −3.9490I T +0.0070I R
h v h v h v h h h h h h
−0.0003I S −0.0008I E −0.0005I I +0.2966J R −0.0033J S +0.0647J E
h v h v h v h h h v h v
+0.0172J I −0.0001T E
h v h v
E˙ =0.5364S +0.0620R −0.0030S −0.1168E +0.0017I +0.2424V2−0.0169E2
v h h v v v h h
+0.0769I2+0.0179J2−0.2395T2−0.0004R2 −0.0003E2+2.0707S E −5.7732S J
h h h h v h h h h
+0.0181S R −0.0017S S +0.1116S E −0.0015S I +0.0142V E +1.4644V I
h h h v h v h v h h h h
−0.0012V J +1.6498V T −0.0046V R +0.0001V S −0.0011V E −0.0001V I
h h h h h h h v h v h v
−11.8825E I −2.3655E J +0.0240E R −0.0005E S +0.0139E E +0.0004E I
h h h h h h h v h v h v
+0.0480I J −0.1349I T −0.0041I R +0.0003I S −0.0005I E +0.0001I I
h h h h h h h v h v h v
+0.0126J R +0.0093J E −0.0066J I +0.0001T R −0.0001T E
h h h v h v h h h v
I˙ =0.3300E −0.0714I
v v v
S˙ =0.0771S +1.0085E −1.6372J +0.0036R +0.0002E +0.0003I +0.0066V2
h h h h h v v h
−0.0007E2−0.0411I2+0.0011J2+0.0089T2+0.0649S E −9.3178S I −0.1007S J
h h h h h h h h h h
+0.0013S R −0.0001S S +0.0004S E +0.0002S I +0.0026V E +0.1928V I
h h h v h v h v h h h h
20% noise −0.0069V J −0.2055V T +2.1215E I +0.1225E J +2.7352E T −0.0102E R
h h h h h h h h h h h h
+0.0006E S +0.0024E E −0.0033E I +0.0052I J −0.3482I T +0.0191J R
h v h v h v h h h h h h
−0.0005J S +0.0009J E +0.0023J I
h v h v 27 h v

V˙ =0.0001S +0.0003E −0.0005J −0.0001S E −0.0020S I −0.0003V T
h h h h h h h h h h
−0.0002E I +0.0001E J +0.0003E T +0.0001I T
h h h h h h h h
E˙ =−0.0690S −1.2195E +1.7333J −0.0028R −0.0001E −0.0002I −0.0051V2
h h h h h v v h
+0.0008E2+0.0415I2−0.0011J2−0.0062T2−0.0773S E +9.1702S I +0.1148S J
h h h h h h h h h h
−0.0013S R +0.0001S S −0.0004S E −0.0002S I −0.0024V E −0.1948V I
h h h v h v h v h h h h
+0.0065V J +0.2153V T −2.0853E I −0.1223E J −2.8764E T +0.0103E R
h h h h h h h h h h h h
−0.0006E S −0.0024E E +0.0033E I −0.0050I J +0.3157I T −0.0185J R
h v h v h v h h h h h h
+0.0005J S −0.0008J E −0.0023J I
h v h v h v
I˙ =−0.0001I2−0.0009S I −0.0001V I +0.0002V T −0.0154E I −0.0003E J
h h h h h h h h h h h h
−0.0219E T −0.0004I T
h h h h
J˙ =0.2000E −0.2010J
h h h
T˙ =0.0001I2−0.0002T2+0.0187S I +0.0002V T +0.0026E I +0.0003E J
h h h h h h h h h h h
−0.0012E T −0.0007I T
h h h h
20% noise R˙ =0.2000J +0.0001I2+0.0002T2+0.0066S I +0.0003V I −0.0005V T
h h h h h h h h h h
+0.0061E I +0.0198E T +0.0009I T
h h h h h h
S˙ =13.9995S +8.3165E −107.6831J +1.5637R +0.0021S +0.7773E +0.3135I
v h h h h v v v
−0.0035S2+0.3382V2+0.0222E2−0.6528I2−0.0041J2−0.2177T2−0.0001R2
h h h h h h h
−0.0001S2+0.0001E2−0.0002I2−3.5709S E +13.8755S I +5.9628S J
v v v h h h h h h
−0.0009S S −0.0981S E +0.0093S I +0.0152V E −1.5859V I −0.0961V J
h v h v h v h h h h h h
−9.1878V T +0.0062V R −0.0002V S +0.0014V E +51.7889E I +10.8971E J
h h h h h v h v h h h h
+132.0941E T −0.1361E R +0.0039E S −0.0938E E −0.0134E I +0.0752I J
h h h h h v h v h v h h
+21.6784I T +0.0003I R +0.0005I S +0.0004I E +0.0004I I −0.1554J R
h h h h h v h v h v h h
+0.0032J S −0.1228J E −0.0161J I −0.0001T R +0.0001T E +0.0129S R
h v h v h v h h h v h h
E˙ =0.2835S +2.2892E −5.4470J +0.0603R −0.0008S −0.0059E +0.0007I
v h h h h v v v
+0.0001S2−0.1145V2−0.0078E2−0.0407I2+0.0130J2−0.2650T2−0.0004E2
h h h h h h v
+0.9185S E −3.9999S I −3.0961S J −0.0649S R +0.0017S S +0.0828S E
h h h h h h h h h v h v
−0.0084S I −0.0293V E +0.9885V I +0.1435V J −1.4628V T −0.0044V R
h v h h h h h h h h h h
+0.0001V S −0.0019V E −1.2244E I −1.7179E J +38.1332E T +0.0160E R
h v h v h h h h h h h h
+0.0001E S +0.0152E E −0.0012E I −0.1147I J +3.9685I T −0.0044I R
h v h v h v h h h h h h
+0.0003I S +0.0005I E +0.0005I I −0.1054J R +0.0035J S +0.0036J E
h v h v h v h h h v h v
−0.0143J I +0.0002T R −0.0001T E
h v h h h v
I˙ =0.3300E −0.0714I
v v v
S˙ =−0.0579E −0.0208J +0.0055R +0.0007E2−0.0029I2−0.0013J2+0.0380T2
h h h h h h h h
+1.4002S V −0.1158S E −14.0361S I +0.1636S J −0.0022S R +0.2436V I
h h h h h h h h h h h h
+0.0007V J −0.5163V T −0.8032E I −0.6265E J +4.7516E T +0.0157E R
h h h h h h h h h h h h
+0.0183E E −0.0036E I −0.0007I J +1.9407I T −24.2167J T −0.0110J R
h v h v h h h h h h h h
−0.0232J E
h v
V˙ =0.0441J T
h h h
E˙ =0.0680E −0.0566J +0.0016I2−0.0226T2+0.3164S V +0.0285S E
h h h h h h h h h
+13.8928S I −0.0526S J −0.2788V I −0.0420V T +0.7916E I +0.6544E J
h h h h h h h h h h h h
−3.2952E T −0.0154E R −0.0180E E +0.0036E I −1.0337I T +16.9231J T
h h h h h v h v h h h h
+0.0043J R +0.0223J E
h h h v
I˙ =−0.0883S I −0.0246E I −0.0497E T −0.0338J T
h h h h h h h h h
25% noise J˙ =0.2000E −0.2010J
h h h
T˙ =0.0085S I +0.0090E I +0.0295E T −0.0914J T
h h h h h h h h h
R˙ = 0.0014E + 0.1984J − 0.0141S V + 0.0817S I + 0.0148E I + 0.0190E T +
h h h h h h h h h h h
0.1264J T
h h
S˙ =12.0310S −48.7453E +22.9846J +1.5582R −0.0276S +0.0746E +0.0740I
v h h h h v v v
−0.0083S2+2.8666V2+0.0647E2+0.0222I2−0.1099J2+4.4383T2−0.0036R2
h h h h h h h
+83.3180S V −30.9488S E −289.5507S I +31.3275S J −0.0514S R
h h h h h h h h h h
−0.0100S S +0.0136S E −0.0193S I +0.0569V E −1.1562V I −0.0063V J
h v h v h v h h h h h h
−6.2468V T +0.0295V R +0.0038V E +55.1224E I +9.6804E J
h h h h h v h h h h
−191.1162E T +0.0893E R +0.0011E S −0.0324E E −0.0128E I
h h h h h v h v h v
+0.0228I J +10.8828I T −0.0207I R −0.0045I E −264.6920J T +1.2324J R
h h h h h h h v h h h h
−0.0385J
h
S
v
−0.0255J
h
E
v
+0.002589J
h
I
v

|     | E˙ =−0.8714S                                            |           |     |           |     | −0.2658R       |          |          | −0.4037E |          |       |
| --- | ------------------------------------------------------- | --------- | --- | --------- | --- | -------------- | -------- | -------- | -------- | -------- | ----- |
|     |                                                         | +15.1611E |     | +40.6121J |     |                | +0.0051S |          |          |          |       |
|     | v                                                       | h         |     | h         | h   |                | h        |          | v        | v        |       |
|     | +0.2627V2−0.0243E2+0.1464I2+0.0143J2−0.4236T2−210.1857S |           |     |           |     |                |          |          |          | V        |       |
|     |                                                         | h         | h   |           | h   | h              |          | h        |          | h h      |       |
|     |                                                         | −88.3987S |     | −1.6221S  |     |                |          | −0.0237S |          | −0.0068S |       |
|     | +8.8759S                                                | h E h     |     | h I h     |     | h J h +0.2491S |          | h R h    |          | h E v    | h I v |
25% noise −0.0586V E +2.2050V I +0.0199V J +3.6401V T −0.0089V R −12.1838E I
|     |     | h h |     | h h | h   | h   | h   | h   | h   | h   | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−3.7597E J +27.8119E T +0.0668E R +0.0116E E −0.0659I J −9.9347I T
|     |             | h h         |     | h h      |     | h h        |     | h v        |     | h h        | h h |
| --- | ----------- | ----------- | --- | -------- | --- | ---------- | --- | ---------- | --- | ---------- | --- |
|     | −0.0069I    |             |     | −0.1953J |     |            |     |            |     |            |     |
|     |             | R +86.7477J |     | T        |     | R +0.0061J |     | S +0.0200J |     | E +0.0104J | I   |
|     |             | h h         |     | h h      |     | h h        |     | h v        | h   | v          | h v |
|     | I˙ =0.3300E | −0.0714I    |     |          |     |            |     |            |     |            |     |
|     | v           | v           | v   |          |     |            |     |            |     |            |     |
S˙ =−0.0156S +0.0714E +0.0285J +0.0031R −0.0008E −0.0042V2−0.0094I2
|     | h                 | h   | h   |          | h   |          | h   | v        |     | h        | h   |
| --- | ----------------- | --- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- |
|     |                   |     |     | −0.0722S |     | −4.0594S |     | −0.0124S |     |          |     |
|     | +0.0330T2+0.9301S |     | V   |          | E   |          | I   |          | J   | +0.1990V | I   |
|     |                   | h   | h   | h        | h   | h        | h h |          | h h |          | h h |
−0.1401V T −0.4292E I +0.3518E J +0.7964E T +0.0040E R −0.0022E I
|     |              | h h        |     | h h        | h          | h              | h                           | h          | h   | h   | h v |
| --- | ------------ | ---------- | --- | ---------- | ---------- | -------------- | --------------------------- | ---------- | --- | --- | --- |
|     | −0.2542I     | −10.0913J  |     | −0.0016J   |            |                |                             |            |     |     |     |
|     |              | h T h      |     | h T h      |            | h R h +0.0038J |                             | h E v      |     |     |     |
|     | V˙ =0.0442J  | T          |     |            |            |                |                             |            |     |     |     |
|     | h            | h h        |     |            |            |                |                             |            |     |     |     |
|     | E˙ =−0.1892E | −0.0226J   |     |            |            |                | +0.0117V2+0.0112I2−0.0187T2 |            |     |     |     |
|     | h            | h          | h   | +0.0032R   | h +0.0008E |                | v                           |            |     |     |     |
|     |              |            |     |            |            |                |                             | h          |     | h   | h   |
|     | +0.0396S     | E +3.4686S |     | I +0.0081S |            | J −0.0024S     |                             | R −0.2020V |     | I   |     |
|     |              | h h        |     | h h        | h          | h              | h                           | h          | h   | h   |     |
+0.3935S V +0.1138V T +0.4713E I −0.3503E J −1.2770E T −0.0040E R
|     |     | h h | h   | h   | h   | h   | h   | h   | h   | h   | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.0038J
|     | +0.0023E     | I +0.2733I |     | T +7.3762J |     | T          | E   |     |     |     |     |
| --- | ------------ | ---------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
|     |              | h v        | h   | h          | h   | h          | h   | v   |     |     |     |
|     | I˙ =−0.0896S | I −0.0245E |     | I −0.0500E |     | T −0.0342J |     | T   |     |     |     |
|     | h            | h h        |     | h h        |     | h h        |     | h h |     |     |     |
J˙
|     | =0.2000E    | −0.2010J       |     |                |     |          |          |          |     |     |     |
| --- | ----------- | -------------- | --- | -------------- | --- | -------- | -------- | -------- | --- | --- | --- |
|     | h           | h              | h   |                |     |          |          |          |     |     |     |
|     | T˙          |                |     |                |     | −0.0964J |          |          |     |     |     |
|     | h =0.0220S  | h I h +0.0090E |     | h I h +0.0285E | h   | T h      | h        | T h      |     |     |     |
|     | R˙ =0.1992J | +0.0912S       | I   | +0.0155E       | I   | +0.0160E | T        | +0.1356J | T   |     |     |
|     | h           | h              | h   | h              | h h |          | h h      |          | h h |     |     |
|     | S˙          | −51.8742E      |     |                |     |          | −0.0280S |          |     |     |     |
30% noise v =11.7830S h h +24.3361J h +1.5721R h v +0.1057E v +0.0716I v
−0.0074S2+2.2438V2+0.0653E2−0.0115I2−0.1117J2+3.7532T2−0.0032R2
|     |            | h           | h   |            | h          | h            |           | h             |          | h        | h     |
| --- | ---------- | ----------- | --- | ---------- | ---------- | ------------ | --------- | ------------- | -------- | -------- | ----- |
|     | +179.9953S | V −27.6502S |     | E          | −225.2304S | I            | +30.1578S | J             | −0.1533S | R        |       |
|     |            | h h         |     | h h        |            | h            | h         | h             | h        | h        | h     |
|     | −0.0097S   | −0.0175S    |     | −3.6124V   |            |              |           | −0.1879V      |          |          |       |
|     |            | S           |     | I          |            | I +0.0952V   | J         |               | T        | +0.0288V | R     |
|     |            | h v         | h   | v          | h          | h            | h         | h             | h        | h        | h h   |
|     | +0.0039V   | E +68.0251E |     | I +7.3881E |            | J −172.2410E |           | T +0.0654E    |          | R        |       |
|     |            | h v         |     | h h        |            | h h          |           | h h           |          | h h      |       |
|     |            | −0.0121E    |     | −0.0138E   |            | −0.0510I     |           |               |          | −0.0194I |       |
|     | +0.0018E   | h S v       |     | h E v      |            | h I v        | h         | J h +14.7902I | h        | T h      | h R h |
−0.0043I E −176.6532J T +1.0070J R −0.0351J S −0.0781J E −0.0061J I
|     |                                                         | h v         |     | h h         |     | h h      |            | h v |          | h v      | h v |
| --- | ------------------------------------------------------- | ----------- | --- | ----------- | --- | -------- | ---------- | --- | -------- | -------- | --- |
|     | E˙ =−0.9268S                                            |             |     |             |     | −0.2671R |            |     | −0.4005E | −0.0007I |     |
|     | v                                                       | h +19.3397E |     | h +38.5117J | h   |          | h +0.0050S |     | v        | v        | v   |
|     | +0.2876V2−0.0292E2+0.3125I2+0.0199J2−0.3599T2−243.0764S |             |     |             |     |          |            |     |          | V        |     |
|     |                                                         | h           | h   |             | h   | h        |            | h   |          | h h      |     |
+10.2161S E −84.1048S I −3.3197S J +0.2887S R −0.0278S E −0.0066S I
|     |          | h h            |     | h h      |     | h h          |     | h h      |     | h v       | h v   |
| --- | -------- | -------------- | --- | -------- | --- | ------------ | --- | -------- | --- | --------- | ----- |
|     | −0.0572V |                |     | −0.0029V |     |              |     | −0.0106V |     | −31.1892E |       |
|     |          | h E h +2.7380V |     | h I h    | h   | J h +3.4238V | h   | T h      | h R | h         | h I h |
−3.6842E J −13.1911E T +0.0498E R +0.0098E E +0.0016E I −0.0440I J
|     |     | h h |     | h h |     | h h |     | h v |     | h v | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−11.4701I T −0.0061I R +16.1899J T −0.1492J R +0.0060J S +0.0300J E
|     |          | h h |     | h h |     | h h |     | h h |     | h v | h v |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | +0.0086J | I   |     |     |     |     |     |     |     |     |     |
h v
|     | I˙ =0.3300E  | −0.0714I   |     |            |     |          |            |     |                    |     |     |
| --- | ------------ | ---------- | --- | ---------- | --- | -------- | ---------- | --- | ------------------ | --- | --- |
|     | v            | v          | v   |            |     |          |            |     |                    |     |     |
|     | S˙ =−0.0574S |            |     |            |     | −0.0559J |            |     | +0.0169V2−0.2219I2 |     |     |
|     | h            | h +0.0166E | h   | +100.1913I | h   |          | h +0.0088R |     | h                  |     |     |
|     |              |            |     |            |     |          |            |     |                    | h   | h   |
+0.1462T2+1.1089S V −0.0451S E +16.2672S I +0.0051S J −41.4213S T
|     |            | h          | h     | h          | h     | h           | h     | h          | h h |     | h h |
| --- | ---------- | ---------- | ----- | ---------- | ----- | ----------- | ----- | ---------- | --- | --- | --- |
|     | −0.0029S   | R +0.4514V |       | I −0.4274V |       | T +12.1288E |       | I −0.3814E |     | J   |     |
|     |            | h h        |       | h h        | h     | h           |       | h h        | h   | h   |     |
|     |            | −0.0076E   |       |            |       | −0.0047E    |       |            |     |     |     |
|     | +16.7916E  | T          |       | R +0.0064E |       | E           |       | I +0.8060I |     | T   |     |
|     |            | h h        |       | h h        |       | h v         |       | h v        |     | h h |     |
|     | −12.9281J  | T +0.0154J |       | R −0.0091J |       | E           |       |            |     |     |     |
|     |            | h h        |       | h h        |       | h v         |       |            |     |     |     |
|     | V˙         | −0.0031S   |       |            |       |             |       |            |     |     |     |
|     | h =0.0113I | h          | h I h | +0.0565S   | h T h | +0.0090J    | h T h |            |     |     |     |
E˙ =0.0570S −0.1896E −97.8601I +0.0953J −0.0028R −0.0175V2+0.2203I2
|     | h                 | h   | h   |            | h   |           | h   | h        |       | h         | h     |
| --- | ----------------- | --- | --- | ---------- | --- | --------- | --- | -------- | ----- | --------- | ----- |
|     | −0.1363T2+1.3290S |     |     |            |     | −15.7228S |     | −0.0219S |       |           |       |
|     |                   |     | h V | h +0.0298S | h E | h         | h I | h        | h J h | +39.7789S | h T h |
h
−0.4548V I +0.4301V T −12.1019E I +0.3722E J −17.2771E T +0.0091J E
|     |     | h h | h   | h   |     | h h |     | h h |     | h h | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+0.0068E R −0.0064E E +0.0047E I −0.8038I T +10.3792J T −0.0154J R
|     |     | h h |     | h v |     | h v |     | h h |     | h h | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I˙
=−0.2439I
|           | h           | h        |     |          |     |          |     |     |     |     |     |
| --------- | ----------- | -------- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- |
|           | J˙ =0.2000E | −0.2010J |     |          |     |          |     |     |     |     |     |
|           | h           | h        | h   |          |     |          |     |     |     |     |     |
| 40% noise | T˙ =0.0977I | −0.0772S | T   | −0.0101E | T   | −0.0554J | T   |     |     |     |     |
|           | h           | h        | h h |          | h h |          | h h |     |     |     |     |
R˙
h =0.1300I h +0.1991J h +0.1490S h T h +0.0011E h I h +0.0252E h T h +0.0206J h T h
S˙ =4.5246S +14.6332E +2017.7062I −24.5532J +1.4608R −0.0263S
|     | v   | h   | h   |     | h   |     | h   |     | h   | v   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−1.0930V2−0.0112E2−0.8709I2+2.5308T2
|     | +0.0715E   | v +0.0629I | v   |              |     |     |          |     |            |     |     |
| --- | ---------- | ---------- | --- | ------------ | --- | --- | -------- | --- | ---------- | --- | --- |
|     |            |            |     |              | h   | h   |          | h   |            | h   |     |
|     | +519.1415S | V −2.4979S |     | E +239.8974S |     | I   | +2.5444S | J   | −118.9400S | T   |     |
|     |            | h h        |     | h h          |     | h h |          | h h |            | h   | h   |
−0.4937S R −0.0056S S +0.0100S E −0.0094S I −0.0415V E −1.7474V I
|     |     | h h |     | h v |     | h v | h   | v   | h   | h   | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−51.5012E
|     | +0.0047V | h J h +6.2585V | h   | T h +0.0022V | h   | R h |     | h I h +0.7245E |     | h J h |     |
| --- | -------- | -------------- | --- | ------------ | --- | --- | --- | -------------- | --- | ----- | --- |
−158.8168E T −0.2023E R −02.90118E S −0.0450E E −0.0080E I −0.0299J I
|     |     | h h |     | h h |     | h v |     | h v |     | h v | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.0170I J −2.2124I T +0.0027I R −523.2695J T −0.0908J R +0.0436J E
|     |     | h h | h   | h   | h   | h   |     | h h | h   | h   | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     | E˙ =−0.8558S |           |     |            |     |     |           |     | −0.2953R |     |          |     |     |
| --- | ------------ | --------- | --- | ---------- | --- | --- | --------- | --- | -------- | --- | -------- | --- | --- |
|     |              | +14.6920E |     | +203.9968I |     |     | +40.6010J |     |          |     | +0.0057S |     |     |
|     | v            | h         |     | h          |     | h   |           | h   |          | h   |          | v   |     |
−0.4006E +0.2266V2−0.0209E2+0.1245I2+0.0113J2+0.0110T2−239.3402S V
|     |     | v         | h   |     |          | h   | h   |     | h   |     | h   |          | h h |
| --- | --- | --------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | -------- | --- |
|     |     | −51.3426S |     |     | −0.1662S |     |     |     |     |     |     | −0.0272S |     |
+7.4810S h E h h I h h J h +94.5308S h T h +0.2846S h R h h E v
40% noise −0.0068S I −0.0174V E +1.6476V I −0.0510V J +2.5020V T −0.0084V R
|     |     | h v |     | h h |     | h   | h   | h   | h   |     | h h |     | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−31.0530E I −4.3047E J −35.9685E T +0.0100E E −0.0300I J −7.1400I T
|     |             | h h       |     | h h |          |     | h h        |     | h v |     | h   | h   | h h |
| --- | ----------- | --------- | --- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
|     | −0.0076I    | −74.8799J |     |     | −0.0412J |     |            |     |     |     |     |     |     |
|     |             | R         |     | T   |          |     | R +0.0325J |     | E   |     |     |     |     |
|     |             | h h       |     | h h |          | h   | h          |     | h v |     |     |     |     |
|     | I˙ =0.3300E | −0.0714I  |     |     |          |     |            |     |     |     |     |     |     |
|     | v           | v         | v   |     |          |     |            |     |     |     |     |     |     |
S˙ =−0.0681S +0.5799V −0.0617E +85.7939I +0.2986J +0.0019R +0.0001S
|     | h        | h              |     | h                                            |          | h   |             | h   |          | h        |       | h        | v     |
| --- | -------- | -------------- | --- | -------------------------------------------- | -------- | --- | ----------- | --- | -------- | -------- | ----- | -------- | ----- |
|     |          | −0.0006I       |     | +0.0145V2−0.0629I2−0.0006J2+0.0283T2−0.6514S |          |     |             |     |          |          |       |          |       |
|     | +0.0010E |                |     |                                              |          |     |             |     |          |          |       |          | V     |
|     |          | v              | v   |                                              | h        |     | h           |     | h        |          | h     |          | h h   |
|     | −0.0414S | E +11.5635S    |     | I                                            | +0.0682S |     | J −25.7718S |     | T        | −0.0006S | R     |          |       |
|     |          | h h            |     | h h                                          |          | h   | h           |     | h h      |          | h     | h        |       |
|     | −0.0005S |                |     |                                              |          |     | −0.0003V    |     | −0.0978V |          |       | −2.6595E |       |
|     |          | h E v +0.0005V |     | h E h                                        | +0.2284V | h   | I h         |     | h J h    |          | h T h |          | h I h |
+0.0139E J −1.5883E T −0.0078E R −0.0005E S −0.0021E E −0.0012E I
|     |     | h h |     | h h |     | h   | h   |     | h v |     | h   | v   | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.0008I J +0.3520I T −0.0001I R −8.7231J T +0.0136J R +0.0001J S
|     |     | h h |     | h h |     | h   | h   | h   | h   |     | h h |     | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.0032J
|     | +0.0070J | E   |     | I   |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |          | h v |     | h v |     |     |     |     |     |     |     |     |     |
V˙ =0.0001S −0.0067V −0.0001E −0.0016I −0.0002J +0.0007S I −0.0027S T
|     | h        | h          | h   |     | h        |     | h        |     | h   |     | h h |     | h h |
| --- | -------- | ---------- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
|     | −0.0001V |            |     |     |          |     | −0.0045J |     |     |     |     |     |     |
|     |          | T +0.0001E |     | T   | +0.0001I | T   |          |     | T   |     |     |     |     |
|     |          | h h        |     | h h |          | h   | h        |     | h h |     |     |     |     |
E˙ =0.0653S +2.7041V −0.1379E −83.7606I −0.2990J −0.0030R −0.0010E
|     | h   | h   | h   |     |     | h   |     | h   | h   |     | h   |     | v   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.0141V2+0.0628I2+0.0006J2−0.0261T2+0.4954S
|     | +0.0006I | v   |     |     |     |     |     |     |     |     | h V h | +0.0440S | h E h |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----- |
|     |          |     | h   |     | h   |     | h   |     | h   |     |       |          |       |
−11.7921S I −0.0748S J +25.1371S T +0.0010S R +0.0005S E +0.0032J I
|     |     | h h |     | h h |     |     | h h |     | h h |     | h   | v   | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.0005V E −0.2280V I +0.0002V J +0.1004V T +2.5722E I −0.0151E J
|     |     | h h |     | h h |     | h   | h   |     | h h |     | h h |     | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+1.4119E T +0.0079E R +0.0005E S +0.0021E E +0.0011E I +0.0008I J
|     |     | h h |     | h h |     | h   | v   |     | h v |     | h   | v   | h h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.3501I T +0.0001I R +8.7796J T −0.0132J R −0.0001J S −0.0070J E
|     |     | h h |     | h h |     | h   | h   | h   | h   |     | h v |     | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I˙ =−0.2439I
|     | h           | h        |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | J˙ =0.2000E | −0.2010J |     |     |     |     |     |     |     |     |     |     |     |
|     | h           | h        | h   |     |     |     |     |     |     |     |     |     |     |
T˙
=0.0002V +0.0852I −0.0001S V +0.0075S I −0.0734S T +0.0012E I
|           | h         | h          | h   |           | h        | h          |     | h h      |           | h h        |          | h   | h   |
| --------- | --------- | ---------- | --- | --------- | -------- | ---------- | --- | -------- | --------- | ---------- | -------- | --- | --- |
|           | −0.0070E  | T −0.0586J |     | T         |          |            |     |          |           |            |          |     |     |
|           |           | h h        |     | h h       |          |            |     |          |           |            |          |     |     |
|           | R˙        |            |     |           |          | −0.0002S   |     | −0.0074S |           |            |          |     |     |
| 50% noise | =0.0018V  | +0.1575I   |     | +0.2000J  |          |            |     | V        |           | I +0.0716S |          | T   |     |
|           | h         | h          | h   |           | h        |            | h   | h        |           | h h        |          | h h |     |
|           | −0.0012E  | I +0.0070E |     | T         | +0.0584J | T          |     |          |           |            |          |     |     |
|           |           | h h        |     | h h       |          | h          | h   |          |           |            |          |     |     |
|           | S˙        | −98.6007V  |     | −10.0079E |          |            |     |          |           |            |          |     |     |
|           | =11.5742S |            |     |           |          | +504.9588I |     |          | +39.6536J |            | +1.8372R |     |     |
|           | v         | h          |     | h         |          | h          |     | h        |           | h          |          | h   |     |
−0.0109S +0.0441E +0.0522I −0.0012S2+0.5215V2+0.0154E2−0.6016I2
|     |     | v   | v   |     | v   |     | h   |     | h   |     | h   |     | h   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−0.0048J2−1.6275T2−0.0008R2 −0.0001S2−0.0001E2−0.0001I2−176.3566S
|     |     |     |     |     |     |     |     |     |     |     |     |     | h V h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     | h   | h   |     | h   |     | v   |     | v   |     | v   |     |       |
+1.5625S E −13.0573S I +1.8544S J +414.0923S T +0.5207S R −0.0077S S
|     |     | h h |     | h h |     | h   | h   |     | h h |     | h   | h   | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+0.0169S E −0.0043S I −0.0030V E +0.8613V I −0.0164V J −3.3153V T
|     |          | h v        |     | h v |          | h   | h        |     | h h      |     | h h |            | h h |
| --- | -------- | ---------- | --- | --- | -------- | --- | -------- | --- | -------- | --- | --- | ---------- | --- |
|     |          |            |     |     |          |     | −0.1135E |     | −2.1316E |     |     |            |     |
|     | +0.0006V | R +0.0003V |     | E   | +0.0002V |     | I        |     | I        |     | J   | +173.1062E | T   |
|     |          | h h        |     | h v |          | h   | v        |     | h h      |     | h h |            | h h |
−0.0513E R −0.0007E S +0.0004E E −0.0031E I −0.0085I J −13.2927I T
|     |          | h h        |     | h v      |          | h   | v        |     | h v            |     | h h   |          | h h   |
| --- | -------- | ---------- | --- | -------- | -------- | --- | -------- | --- | -------------- | --- | ----- | -------- | ----- |
|     |          | −0.0006I   |     | −0.0004I |          |     | −0.0004I |     |                |     |       | −0.4763J |       |
|     | +0.0083I | h R h      |     | h S v    |          | h E | v        | h   | I v +279.3249J |     | h T h |          | h R h |
|     | +0.0116J | S +0.0832J |     | E        | +0.0159J | I   | −0.0005T |     | R              |     |       |          |       |
|     |          | h v        |     | h v      |          | h   | v        | h   | h              |     |       |          |       |
E˙ =0.3728S +1094.1587V −9.3292E −206.7940I +25.0057J −1.0060R
|     | v        | h        |     | h        |     | h                                    |     | h   |     | h   |     | h   |     |
| --- | -------- | -------- | --- | -------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |          | −0.3547E |     |          |     | −0.0010S2−0.0597V2−0.0130E2+0.2387I2 |     |     |     |     |     |     |     |
|     | +0.0018S |          |     | +0.0084I |     |                                      |     |     |     |     |     |     |     |
|     |          | v        | v   |          | v   |                                      | h   |     | h   |     | h   |     | h   |
−0.0069J2+0.6226T2+0.0002R2 +86.5970S V −0.3654S E −76.0668S I
|     |          | h          | h   |     | h        |     |          | h h |       | h h      |     | h        | h     |
| --- | -------- | ---------- | --- | --- | -------- | --- | -------- | --- | ----- | -------- | --- | -------- | ----- |
|     |          | −467.7718S |     |     | −0.2824S |     | −0.0040S |     |       | −0.0320S |     | −0.0062S |       |
|     | +0.4254S | h J h      |     | h T | h        |     | h R h    |     | h S v |          | h E | v        | h I v |
−0.0138V E +2.1107V I +0.0169V J +5.5149V T −0.0032V R +0.0002V S
|     |     | h h |     | h h |     | h   | h   |     | h h |     | h h |     | h v |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+4.1111E I −1.3581E J −63.7935E T +0.0735E R +0.0004E S +0.0063E E
|     |          | h h        |     | h h        |          | h   | h        |     | h h        |     | h         | v   | h v |
| --- | -------- | ---------- | --- | ---------- | -------- | --- | -------- | --- | ---------- | --- | --------- | --- | --- |
|     |          | −0.0307I   |     |            |          |     | −0.0111I |     |            |     | −60.6075J |     |     |
|     | +0.0005E | I          |     | J +0.7028I |          | T   |          |     | R +0.0002I |     | S         |     | T   |
|     |          | h v        |     | h h        |          | h   | h        | h   | h          |     | h v       |     | h h |
|     | +0.2632J | R −0.0019J |     | S          | −0.0213J | E   | −0.0042J |     | I +0.0003T |     | R         |     |     |
|     |          | h h        |     | h v        |          | h   | v        |     | h v        |     | h h       |     |     |
|     | I˙       | −0.0714I   |     |            |          |     |          |     |            |     |           |     |     |
=0.3300E
|     | v   | v   | v   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
30

References
[1] Wasim Abbas, Sieun Lee, and Sangil Kim. Joint estimation of hand-foot-mouth disease model and
prediction in korea using the ensemble kalman filter. PLOS Computational Biology, 21(4):e1012996,
2025.
[2] HayderAlrazen,IzzatNajmiYaacob,NorkhairunnisaMazlan,andNoorfaizalYidris. Machinelearning-
based new sparse algorithms and reinforcement learning for computational fluid dynamics. In Artificial
Intelligence for Computational Fluid Dynamics, pages 313–343. Elsevier, 2026.
[3] Morteza Babazadeh Shareh, Florian Kleiner, Michael Böhme, Corinna Hägele, Petra Dickmann, and
RainerHeintzmann. Automatedmodeldiscoverybasedoncovid-19epidemiologicdata. medRxiv, pages
| 2026–02, | 2026. |     |     |     |
| -------- | ----- | --- | --- | --- |
[4] Youssef Belgraoui, Aziza Belmaati, and Mustapha Kabil. Parameter estimation in a stochastic seihr
model of covid-19 using the enkf: A case study based on real-world data. Chaos, Solitons & Fractals,
| 208:118225, | 2026. |     |     |     |
| ----------- | ----- | --- | --- | --- |
[5] Dimitri Breda, Dajana Conte, Raffaele D’Ambrosio, Ida Santaniello, and Muhammad Tanveer. Sparse
identificationofnonlineardynamicsforstochasticdelaydifferentialequations. JournalofComputational
| and Applied | Mathematics, | page 117247, | 2025. |     |
| ----------- | ------------ | ------------ | ----- | --- |
[6] StevenLBrunton,JoshuaLProctor,andJNathanKutz. Discoveringgoverningequationsfromdataby
sparse identification of nonlinear dynamical systems. Proceedings of the National Academy of Sciences,
| 113(15):3932–3937, | 2016. |     |     |     |
| ------------------ | ----- | --- | --- | --- |
[7] Lark L Coffey, Anna-Bella Failloux, and Scott C Weaver. Chikungunya virus–vector interactions.
| Viruses, | 6(11):4628–4663, | 2014. |     |     |
| -------- | ---------------- | ----- | --- | --- |
[8] Odo Diekmann, Johan Andre Peter Heesterbeek, and Johan Anton Jacob Metz. On the definition and
the computation of the basic reproduction ratio r 0 in models for infectious diseases in heterogeneous
| populations. | Journal of | Mathematical | Biology, 28:365–382, | 1990. |
| ------------ | ---------- | ------------ | -------------------- | ----- |
[9] GeirEvensen.Theensemblekalmanfilter: Theoreticalformulationandpracticalimplementation.Ocean
| dynamics, | 53(4):343–367, | 2003. |     |     |
| --------- | -------------- | ----- | --- | --- |
[10] UFasel,JNKutz,BWBrunton,andSLBrunton. Ensemble-sindy. Proceedings: Mathematical, Physical
| and Engineering | Sciences, | 478(2260):1–20, | 2022. |     |
| --------------- | --------- | --------------- | ----- | --- |
[11] UrbanFasel,JNathanKutz,BingniWBrunton,andStevenLBrunton. Ensemble-sindy: Robustsparse
model discovery in the low-data, high-noise limit, with active learning and control. Proceedings of the
Royal Society A: Mathematical, Physical and Engineering Sciences, 478(2260), 2022.
[12] KaiFukami,TakaakiMurata,KaiZhang,andKojiFukagata.Sparseidentificationofnonlineardynamics
with low-dimensionalized flow representations. Journal of Fluid Mechanics, 926:A10, 2021.
[13] Lin Guo, Xiaokai Yang, Zhonghua Zheng, Nicole Riemer, and Christopher W Tessum. Uncertainty
quantificationinreduced-ordergas-phaseatmosphericchemistrymodelingusingensemblesindy.Journal
of Geophysical Research: Machine Learning and Computation, 1(4):e2024JH000358, 2024.
[14] Giorgio Guzzetta, Francesco Vairo, Alessia Mammone, Simone Lanini, Piero Poletti, Mattia Manica,
Roberto Rosa, Beniamino Caputo, Angelo Solimini, Alessandra Della Torre, et al. Spatial modes for
transmission of chikungunya virus during a large chikungunya outbreak in italy: a modeling analysis.
| BMC medicine, | 18(1):226, | 2020. |     |     |
| ------------- | ---------- | ----- | --- | --- |
[15] Yu-Xin Jiang, Xiong Xiong, Shuo Zhang, Jia-Xiang Wang, Jia-Chun Li, and Lin Du. Modeling and
predictionofthetransmissiondynamicsofcovid-19basedonthesindy-lmmethod. NonlinearDynamics,
| 105(3):2775–2794, | 2021. |     |     |     |
| ----------------- | ----- | --- | --- | --- |
31

[16] Kadierdan Kaheman, Steven L Brunton, and J Nathan Kutz. Automatic differentiation to simulta-
neously identify nonlinear dynamics and extract noise probability distributions from data. Machine
Learning: Science and Technology, 3(1):015031, 2022.
[17] Kadierdan Kaheman, J Nathan Kutz, and Steven L Brunton. Sindy-pi: a robust algorithm for parallel
implicit sparse identification of nonlinear dynamics. Proceedings of the Royal Society A: Mathematical,
Physical and Engineering Sciences, 476(2242), 2020.
[18] Rajnesh Lal, Weidong Huang, and Zhenquan Li. An application of the ensemble kalman filter in
epidemiological modeling. Plos one, 16(8):e0256227, 2021.
[19] Brendan Lenfesty, Saugat Bhattacharyya, and KongFatt Wong-Lin. Uncovering dynamical equations
of stochastic decision models using data-driven sindy algorithm. Neural Computation, 37(3):569–587,
2025.
[20] ThomasEMorrison. Reemergenceofchikungunyavirus. Journal of virology,88(20):11644–11647,2014.
[21] Ismaila Muhammed, Dimitris M Manias, Dimitris A Goussis, and Haralampos Hatzikirou. Data-
driven identification of biological systems using multi-scale analysis. PLOS Computational Biology,
21(11):e1013193, 2025.
[22] Siddharth Prabhu, Nick Kosir, Mayuresh V Kothare, and Srinivas Rangarajan. Derivative-free domain-
informed data-driven discovery of sparse kinetic models. Industrial & Engineering Chemistry Research,
64(5):2601–2615, 2025.
[23] LucaRosafalco,PaoloConti,AndreaManzoni,StefanoMariani,andAttilioFrangi. Ekf–sindy: Empow-
ering the extended kalman filter with sparse identification of nonlinear dynamics. Computer Methods
in Applied Mechanics and Engineering, 431:117264, 2024.
[24] Luca Rosafalco, Paolo Conti, Andrea Manzoni, Stefano Mariani, and Attilio Frangi. Online learning in
bifurcating dynamic systems via sindy and kalman filtering. arXiv preprint arXiv:2411.04842, 2024.
[25] Alessandro Maria Selvitella and Elliot Allen. On the effectiveness of sparse identification methods to
detectnonlinearmodelsofoscillatorydynamicsinpsychologyandthelifesciences. NonlinearDynamics,
Psychology & Life Sciences, 30(1), 2026.
[26] Pauline Van den Driessche and James Watmough. Reproduction numbers and sub-threshold endemic
equilibria for compartmental models of disease transmission. Mathematical biosciences, 180(1-2):29–48,
2002.
[27] Edwin B Wilson and Jane Worcester. The law of mass action in epidemiology. Proceedings of the
National Academy of Sciences, 31(1):24–34, 1945.
[28] ChayuYangandJinWang.Basicreproductionnumbersforaclassofreaction-diffusionepidemicmodels.
Bulletin of mathematical biology, 82(8):111, 2020.
[29] Linan Zhang and Hayden Schaeffer. On the convergence of the sindy algorithm. Multiscale Modeling &
Simulation, 17(3):948–972, 2019.
[30] Xin-Lei Zhang, Heng Xiao, Xiaodong Luo, and Guowei He. Ensemble kalman method for learning
turbulence models from indirect observation data. Journal of Fluid Mechanics, 949:A26, 2022.
[31] YiZhang,JingWu,XiaoyangCheng,YuxuanYang,XinyuWang,XiaoyuZhao,XiaoyanWang,Huiling
Ouyang, Jingwen Ai, and Wenhong Zhang. Global resurgence of chikungunya virus: outbreak drivers
and emerging solutions. Emerging Microbes & Infections, 15(1):2603714, 2026.
[32] Chenxi Zhao, Ziruo Ge, Tingyu Zhang, Zhouling Jiang, Di Tian, and Zhihai Chen. Chikungunya virus
in 2025: Epidemiology, immunopathogenesis, and vaccine development—a narrative review. Infection
and Drug Resistance, pages 1–14, 2026.
32
---- END DOCUMENT ----
