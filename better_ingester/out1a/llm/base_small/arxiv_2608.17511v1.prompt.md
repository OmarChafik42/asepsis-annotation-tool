Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Conditional-pathMonteCarloforrarestochasticdynamicsonnetworks: Detailsandderivations
Thomas Barthel,1,2,3 Jiazheng Sun,3 and Jhao-Hong Peng3
1Department of Physics, University of Maryland, College Park, MD 20742, USA
2National Quantum Laboratory, University of Maryland, College Park, MD 20742, USA
3Department of Physics, Duke University, Durham, North Carolina 27708, USA
(Dated:August8,2026)
The simulation of rare macroscopic events in stochastic network dynamics, such as widespread epidemic
outbreaks,cascadingfailuresincommunicationnetworks,ortheescapefrommetastablestatesinmany-body
systems, isseverelyhinderedbymethodologicalchallengeslikecatastrophicrejectionrates, weightdegener-
acy,genealogicalcorrelations,andcriticalslowingdowninherenttostandardforward-timealgorithms,splitting
methods, and transition-path sampling. Conditional-path Monte Carlo (CPMC) overcomes these limitations
byemployingnon-localSwendsen-Wang-likeclusterupdatesthatoperatedirectlyonfull-systemtrajectories.
Servingasthetechnicalcompanionto[Sun,Moody,andBarthel,arXiv:2608.16171],thispaperprovidesthe
rigorous mathematical foundations and algorithmic details underlying the CPMC framework. We formally
define the joint path-graph probability weights and derive the transition and uniformization sum rules that
guarantee detailed balance. Applying the framework to susceptible-infectious-susceptible (SIS) models, we
systematicallyconstructandoptimizesingle-nodeandedgegraphvertexsetsspecificallydesignedtoprevent
lockavalanchesandmaintainthestructuralmobilityoftheepidemictrunk. Furthermore,wedetailadynamic
programmingschemetoexactlyimplementcomplexboundaryconditions–includingpatient-zeroandmacro-
scopicoutbreak-sizeconstraints–enablingtherejection-freegenerationofvalidtrajectories.Finally,weassess
thecomputationalcomplexityofthealgorithm,describeparallelizationstrategies,andvalidateCPMCagainst
exactsolutionsfordynamicsonsmallnetworks.
I. INTRODUCTION cardingthevastmajorityofgeneratedpathsthatfailtosatisfy
theconstraint.
To circumvent the massive rejection rates of forward-time
Understanding the stochastic evolution of complex net-
SSA, various valuable rare-event sampling techniques have
works and many-body systems is a central challenge across
beendeveloped:
physics, biology, engineering, social science, and finance.
In many real-world systems, the most consequential macro-
• The weighted stochastic simulation algorithm (wSSA)
scopic events emerge from a rare confluence of localized
[20, 21], developed to study rare biochemical events, re-
stochastic processes. In statistical mechanics, for instance,
lies on importance sampling. It modifies the standard
rare extreme fluctuations drive the escape from metastable
Gillespie algorithm by artificially biasing local reaction
states [1], such as nucleation in kinetic spin models [2, 3],
propensities to actively drive trajectories toward a rare
anddictatetheevolutionofglassysystems[4,5]. Forinfec-
target state, then unbiasing the final probability estimate
tiousdiseases,onlyasmallpercentageoflocalsurgesexpand
using the likelihood ratio with respect to the true model.
to trigger widespread epidemics because they must navigate
Forlargestochasticnetworks,wSSAfacespracticalchal-
specific bottlenecks in the contact patterns of heterogeneous
lenges: In complex topologies, an optimal selection of
populations [6–8]. Similarly, cascading failures in commu-
heuristic biasing parameters is difficult, and suboptimal
nication networks and financial systems often originate from
choices can drastically inflate the estimator’s variance.
highly improbable combinations of local faults [9, 10], and
Furthermore,asnetworksizeorsimulationtimeincreases,
massiveshiftsinsocietalopinioncanbedrivenbyararealign-
wSSAsuffersfromweightdegeneracy,whereatinyfrac-
mentoflocalinfluences[11,12].Becausethesepivotalevents
tionoftrajectoriesaccumulatesmassivestatisticalweight
are inherently rare, analyzing them with direct forward-time
and dominates the ensemble, effectively destroying the
simulationsisgenerallyinefficient.
sample size. Finally, wSSA is still a local, forward-time
Traditional individual-based simulation techniques of integrator. When it must navigate rigid topological bot-
stochastic network dynamics like the susceptible-infectious- tlenecksstepbystep, itischallengedbykinetictrapping
susceptible(SIS)model[13–17]areforward-timealgorithms [22].
– most notably the Gillespie method [18] and the intimately
related kinetic Monte Carlo [19]. These standard stochastic • Splitting methods, such as forward flux sampling (FFS)
simulationalgorithms(SSA)propagateaninitialstateforward [23–25] or repetitive simulation trials after reaching
intimebyrandomlysamplingthenextelementarystatetran- thresholds (RESTART) [26–28], define an effective or-
sition according to the physical rates of the system. While der parameter λ, evolve trial trajectories with SSA, and
SSA is exact and highly efficient for exploring typical, un- branch(clone)trajectoriesthatsuccessfullycrossinterme-
constrained dynamics, it suffers from catastrophic rejection diate thresholds λ < λ < λ < ... toward the rare
0 1 2
rates when simulating rare events. Attempting to simulate event of interest [29]. While powerful, splitting methods
rare events that are formulated in terms of macroscopic con- cansufferheavilyfrompathdegeneracyinlarge, hetero-
straints (like a specific outbreak-size threshold) requires dis- geneous networks. A simple order parameter λ like the
n
6202
guA
81
]hcem-tats.tam-dnoc[
1v11571.8062:viXra

2
total number of infected nodes generally masks hidden mathematicalfoundationsanddetailedderivationsunderlying
barriers. For example, 10 infected nodes clustered in a thealgorithm. FollowingashortaccountoftheSISmodelin
densecorehaveavastlydifferentprobabilityofdrivinga Sec. II, Sec. III introduces important notations and the path
massiveoutbreakcomparedto10infectednodesscattered probability density. Section IV describes the central idea of
attheperiphery. UsingSSA,splittingmethodsaregener- theSwendsen-Wang-likeclusterupdates,randomlyassigning
allyalsohamperedbycriticalslowingdownastrajectories graphverticestoatrajectory,identifyingfreespacetimeclus-
needto“diffuse”intorarerstatestopassfromλ toλ . ters,andrandomlyselectingthestatesoftheseclusterstoob-
n n+1
Furthermore,duetothecloning,splittingmethodsarevul- tainanewtrajectory. WeprovedetailedbalanceoftheCPMC
nerabletogenealogicalcorrelation(the“foundereffect”): algorithm. The detailed balance relies on certain sum rules
Whentheforward-timedynamicsbecometrappedintopo- thattheinsertionratesofthegraphverticesneedtoobey. For
logicalbottlenecksorslowmodes,thealgorithmmaysim- SISdynamics,wediscussdifferentsetsofgraphverticesand
plyreplicatehighlycorrelatedoffspring[25,30,31]. solutions for the associated rate sum rules in Sec. V. Again
for the example of SIS models, Sec. VI demonstrates how
• The weighted ensemble (WE) algorithm [30, 32–35], de- trajectoryconstraintslikepatient-zeroandoutbreak-threshold
veloped in the biophysics community, is a conceptually conditionscanbeimplementedexactlyandefficientlyduring
somewhatdifferentsplittingmethod. UsingSSA,itprop- cluster updates through dynamic programming tables. The
agates a population of trajectories (“walkers”) for short scalingofcomputationcostsandparallelizationstrategiesare
time intervals and, similar to the above, maintains order- assessed in Secs. VII and VIII. We conclude with validation
parameter bins [λ n ,λ n+1 ). When reaching the end of a simulations, comparing CPMC to exact solutions on small
time interval, trajectories that have advanced into rarely networksinSec.IX,andthediscussionsectionX.
visited bins are replicated (split) to enhance the explo-
rationoftheraretransition,whileoverpopulatedbinsare
culledtopreventacombinatorialexplosionofpaths. Ap- II. SISMODEL
plicationsofWEtolargestochasticnetworkscanagainbe
challengedbythepathdegeneracyproblem,criticalslow- While the method is applicable for general Markovian
ingdown,andgenealogicalcorrelations. stochasticdynamics,forinstructiveexamples,wewillexclu-
sively employ the SIS model [13–17], where N individuals
• Transition path sampling (TPS) [36–40], developed for
form the nodes of an interaction network. A node i can be
the study of rare transitions between long-lived states in
intwostates: infected(σ = 1)orsusceptible(σ = 0). An
i i
chemical reactions and protein folding, operates directly
infected node i spreads the disease to a susceptible node j
in the space of trajectories, proposing new valid paths
at infection rate α , defining the network structure. Addi-
i,j
via local “shooting” or “shifting” moves [41]. However,
tionally, an infected node i returns to the susceptible state at
in constrained network models, such local trajectory up-
therecoveryrateγ . Forallexamplesdiscussedinthiswork,
i
dates routinely suffer from critical slowing down, as the
we consider the continuous-time SIS model where, in gen-
algorithmstrugglestosubstantiallymutatethetopological
eral,α ̸=α andallratescandependontheeventposition
i,j j,i
coreofthetrajectory(e.g.,thetrunkofepidemicinfection
(nodeoredge).
trees)withoutviolatingphysicalrules.
To overcome the limitations of forward-time SSA, split-
III. PATHPROBABILITIESANDNOTATIONS
ting methods, and local path updates, we introduce the
conditional-path Monte Carlo (CPMC) [42]. Building on
Thesystemstateattimetisdenotedby
ideas from computational condensed-matter physics, CPMC
operates directly onthe space of full-system trajectories. In- σt :=(σt,σt,...,σt )∈dN (1)
1 2 N
stead of attempting to propose local, step-by-step changes,
CPMC maps the current trajectory of the full system to an with single-node states σ i t ∈ {0,...,d−1}. We use σ x t =
i s n p t a e c r e m ti e m di e at v e o g lu ra m p e h i c n o t n o fi c g o u n ra n t e io ct n ed tha c t lu d s e te c r o s m . po B s y es e t m he pl e o n y t i i n r g e a (σ t x t t i 1 m ,. e . t . , , a σ n x t d n a )t t o ra d je e c n t o o t r e y th (σ e t st | at 0 e ≤ of t no ≤ de T s ) x fo = rt ( h x e 1 e , v .. o . lu , t x io n n )
Swendsen-Wang-like cluster updates, the algorithm simulta- fromt=0toT isdenotedbyσ ∈[0,T]×dN.
neously flips the states of non-local spacetime regions. This Let E x t = {σ x } be the set of all possible elementary state
allowsCPMCtogenerateaMarkovchainoftrajectoriesthat changes
all strictly respect the desired macroscopic constraints, en-
σ :=(σt− →σt+) (2)
tirelybypassingthemassiverejectionratesandcriticalslow- x x x
ingdownthatplagueSSA-basedmethodsandTPSinvarious attimetandpositionxinthenetworkasdefinedbythephys-
applications,aswellasthepathdegeneracyproblemandge- icalmodel,wherewehaveintroducedtheshort-handnotation
nealogicalcorrelationsinthesplittingmethods. x = (t,x) for spacetime locations, positions x are ordered
This manuscript serves as the technical companion to listsoftheinvolvednodes,σt−isthestateonthesenodesjust
x
Ref. [42], which introduced the broader CPMC framework before the transition, and σt+ is the state just after the tran-
x
andpresentedanumericalanalysisforlargeoutbreaksinSIS sition. Theassociatedelementaryeventratesaredenotedby
dynamicsonkinshipnetworks. Here,weprovidetherigorous ω (σ ).
x x

3
Example1. IntheSISmodel,nodeirecoveringattimetfrom where TI is the total infected time of node i, and TIS is the
i i,j
aninfectioncorrespondstothestatechange totaltimeforwhichnodej wassusceptiblewhilenodeiwas
infected.
σR =(σt− →σt+)=(1→0) (3a)
x i i An SIS trajectory from time 0 to time T, where node i is
atlocationx=(t,i),whichhappensateventrateω (σR)= infected from time 0 to time τ and all other nodes are sus-
x x
γ . Infectionsbetweennodesiandj attimetcausethestate ceptibleasshowninFig.1,hencehastheprobabilitydensity
ch i anges C(σ)γ i e−γiτ−(cid:80) j∈∂i αi,jτ.
σI↑ =(σt−,σt− →σt+,σt+)=(1,0→1,1), (3b)
x i j i j
σI↓ =(σt−,σt− →σt+,σt+)=(0,1→1,1) (3c) IV. SWENDSEN-WANG-LIKECLUSTERUPDATES
x i j i j
atlocationx=(t,i,j),wherei<j forsomearbitrarynode ToefficientlyexplorethepathspaceundertheconstraintC,
ordering. Theyoccuratratesω (σI↑)=α andω (σI↓)=
x x i,j x x CPMCgeneratesaMarkovchainoftrajectories
α . Accordingly, the sets of elementary state changes are
j,i
E i t ={σ ( R t,i) }andE i t ,j ={σ ( I↑ t,i,j) ,σ ( I↓ t,i,j) }. σ[1]− W →σ[2]− W →σ[3]− W →... (8)
Valid trajectories σ are equivalently specified by an ini-
tialstateσ0andthesequence (cid:0) (x ,σ ),...,(x ,σ ) (cid:1) of all respecting the constraint, where the path transition prob-
1 x1 N xN ability density W(σ′|σ) for trajectory updates obeys the de-
transitionevents.
tailedbalancecondition
Under trajectory constraints denoted by an indicator func-
tion C(σ), the (unnormalized) path probability density is W(σ′|σ)P(σ)=W(σ|σ′)P(σ′). (9)
givenby
P(σ)=C(σ)
(cid:16) (cid:89)
ω x (σ x )
(cid:17) e−(cid:82)
0
TdtΛt(σt),
(4) A. Structureofclusterupdatesandnotations
x∈σ
wheretheproductrunsoveralllocationsxoftransitionevents As local trajectory updates are often plagued by critical
in the trajectory σ. In a typical scenario, C only depends slowing down, we employ non-local cluster updates similar
on the states σ0 and σT at the start and end times. More to the Swendsen-Wang algorithm from computational con-
generally, C can be a probability distribution for initial and densed matter physics and statistical mechanics [43, 44],
finalstates,onecanincludeconstraintsatintermediatetimes, whichhasbeenextensivelyusedfortheinvestigationofclas-
andworkwithtime-correlatedconstraints. sical and quantum many-particle systems in thermal equilib-
rium[45–48].
Example 2. In the SIS model, an infection event (3b) at lo-
The cluster update introduces an intermediate graph con-
cation x = (t,i,j) contributes the factor ω (σ ) = α
x x i,j figurationg,splittingthetrajectoryupdateintotwosteps
in Eq. (4). A recovery event (3a) at location x = (t,i)
contributes the factor ω (σ ) = γ . The indicator func-
tion C may encode traje x ctor x y constr i aints such as having a σ − ( − a → ) g − ( − b → ) σ′. (10)
single infected node at time t = 0 and an outbreak with
(a) In the first step, we translate the given trajectory σ to a
≥ N/4 infected nodes at time t = T. In this case, C(σ) =
C H 0 e ( a σ vi 0 s ) id C e T s ( t σ ep T f ) un = ct δ io (cid:80) n i . σ i 0,1 θ( (cid:80) i σ i T −N/4),whereθisthe c a o g m iv p e a n ti t b r l a e je g c r t a o p r h y g σ . ; M th u e lt g ip ra le ph gr c a h p o h i s ce ar i e s c r o an m d p o a m tib a l c e c w or i d th -
ing to a detailed-balance condition in the enlarged state
In Eq. (4), Λt(σt) is the total escape rate of the system space. A graph g provides a decomposition of space-
fromstateσt attimet. GiventhesetsEt ofpossibleelemen- time [0,T]×{1,...,N} into clusters {C }. Each clus-
x k
tarystatechanges(2)attimetandpositionx, ter C is characterized by a base state a which is free
k k
Λt(σt)= (cid:88) Λ (σt) with (5a) to take one of d k ≤ d values, where d = 2 in the SIS
x x model. A cluster is called fixed if d k = 1 and free if
x d ≥ 2. Everyclusterconsistsoftimeintervalsonindi-
(cid:88) k
Λ (σt):= δ ω (σ˜ ). (5b) vidual nodes {i}, where the node state σt on each time
x x
σ˜x∈E
x
t
σ˜x t−,σ
x
t x x
segmentisconstantanddeterminedbyan
i
injectivefunc-
tion a (cid:55)→ σt(a ) ∈ {0,...,d−1}, including the seg-
Example3. FortheSISmodel,wehave k i k
ment’s state in the original trajectory σ. In this way,
Λt(σt)= (cid:88) γ + (cid:88) (cid:88) α , (6) graphs g define (non-disjoint) finite subsets of trajecto-
i i,j
ries, and every valid trajectory is contained in a whole
i:σ
i
t=1 i:σ
i
t=1j∈∂i:σ
j
t=0
continuumofgraphsaswillbecomeclearinthefollow-
where∂ isthesetofnodei’snearestneighbors,suchthat ing.
i
(cid:90) T (b) In the second step, we randomly choose one of the d k
(cid:88) (cid:88)(cid:88)
dtΛt(σt)= γ i T i I+ α i,j T i I , S j , (7) allowedstatesforeachfreeclusterC k withuniformprob-
0 i i j∈∂i ability1/d k suchthatweobtainanewtrajectoryσ′.

4
FIG.1. TwoclusterupdatesforasimpleSIStrajectory. TheclusterupdatesfortwonodesofanSISmodeldescribedinExample4start
fromatrajectoryσ,wherenodeiisinfecteduntiltimeτ,andnodej issusceptiblefortheentiretime[0,T]. Intheconstructionofgraph
g, therecoveryofnodeiismatchedbythevertexgR− = (1 → a), wherestateaisfreetotakevalues0(susceptible)and1(infected).
(τ,i)
Additionalfoursingle-nodebackgroundverticesandoneedgebackgroundvertexareinsertedbyPoissonpointprocesses;indicatedbyaredder
backgroundcolor.TheedgevertexgI↑− =(1,0→1,a)fixesnodeitobeinfectedbeforeandaftertimet ,hencefixingthefreet+state
|     |     |     | (t3,i,j) |     |     |     |     |     | 3   | 1   |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ofthevertexgR− . InconjunctionwiththevertexgR+ = (a → 0),theedgevertexleadstothefreeclusterC fortimes[t ,t ]onnode
|             | (t1,i) |     |     | (t5,j) |     |     |     |     | 2   | 3 5 |
| ----------- | ------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
| VerticesgR− | andgR+ |     |     |        |     |     |     |     |     |     |
j. leadtothefreeclusterC 1 fortimes[τ,t 4 ]onnodei,andwehaveanotherfreeclusterC 3 onnodej. Choosing
(τ,i) (t4,i)
theinfectedstateforclustersC andC aswellasthesusceptiblestateforC ,weobtainthenewtrajectoryσ′withnodejgettinginfectedby
|     |     | 1   | 2   |     |     | 3   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nodeiattimet .Anotherclusterupdate,wheretheinfectioneventismatchedbythevertexgswap =(a,a¯→1,1)anda¯isthenegationofa,
|     | 3   |     |     |     |     |     | t3,i,j |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
tot′.
causesachangeoftheinfectiondirection,movingpatientzerofromnodeitonodej.Italsomovestherecoverytimeofnodejfromt 5 2
The graph g consists of so-called graph vertices g at lo- verticescanchangeinstep(b)oftheclusterupdatefromphys-
z
cations z. Each vertex imposes a certain local constraint on icaltobackgroundorviceversa.
Et
the trajectories that are deemed compatible with the graph, Analogous to the sets of elementary state changes (2),
x
restricting allowed states for the t− and t+ states of the in- weintroducethesetsofpossiblegraphverticesattimetand
volved nodes or imposing bijective relations between these positionz,denotedby
states. Specifically,thegraphg,constructedinstep(a)ofthe
t
update, comprises one graph vertex g for every event loca- G z ≡G ={g z } with z =(t,z). (11)
|          |                  |     | x              |       |         | z   |     |     |     |     |
| -------- | ---------------- | --- | -------------- | ----- | ------- | --- | --- | --- | --- | --- |
| tion x ∈ | σ, corresponding | to  | the N physical | state | changes |     |     |     |     |     |
σ
σ , and further M background vertices g inserted via a Example4. ConsiderthetrajectoryσfromExample3,where
| x   | g,σ |     |     | y   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x = (τ,i)isthelocationofarecoveryeventinthetrajectory
| Poisson | point process at | locations | y on time | intervals | where |                  |                                     |     |     |     |
| ------- | ---------------- | --------- | --------- | --------- | ----- | ---------------- | ----------------------------------- | --- | --- | --- |
|         |                  |           |           |           |       | σ foranSISmodel. | Twophysicalgraphverticesforlocation |     |     |     |
nophysicalchangeoccursinσ.
Forbrevityofnotationwewrite xthatarecompatiblewithσ are(a)avertexgR− = (1 →
|     |     |     |     |     |     |                  |              | x     |              | x           |
| --- | --- | --- | --- | --- | --- | ---------------- | ------------ | ----- | ------------ | ----------- |
|     |     |     |     |     |     | a) that enforces | the infected | state | στ− = 1 just | before time |
i
• “σ ∈ g” for all trajectories σ that are compatible with t = τ but allows any state στ+ = a ∈ {0,1} after time τ
i
| graphg, |     |     |     |     |     | and(b)avertexgR+ | =(a→0)thatallowsanystateστ− |     |     |     |
| ------- | --- | --- | --- | --- | --- | ---------------- | --------------------------- | --- | --- | --- |
=
|                                   |                 |                              |     |     |     |                                              | x       |                                |             | i             |
| --------------------------------- | --------------- | ---------------------------- | --- | --- | --- | -------------------------------------------- | ------- | ------------------------------ | ----------- | ------------- |
|                                   |                 |                              |     |     |     | a∈{0,1}justbeforetimeτ                       |         | butenforcesthesusceptiblestate |             |               |
| • “g ∋                            | σ”forallgraphsg | thatarecompatiblewithtrajec- |     |     |     |                                              |         |                                |             |               |
|                                   |                 |                              |     |     |     | στ+ = 0 after                                | time τ. | A vertex                       | of type (a) | could also be |
| toryσ,i.e.,thegraphsthatcontainσ, |                 |                              |     |     |     | i                                            |         |                                |             |               |
|                                   |                 |                              |     |     |     | insertedasabackgroundvertexgR−atanylocationy |         |                                |             | =(t,i)        |
y
• “x∈σ”forthelocationsofallN σ state-changingevents with0 < t < τ. Similarly,avertexoftype(b)couldalsobe
intrajectoryσ,and insertedasabackgroundvertexgR+atanylocationy =(t,i)
y
|                               |     |     |      |                   |     | withτ <t<T. | SeeFig.1. |     |     |     |
| ----------------------------- | --- | --- | ---- | ----------------- | --- | ----------- | --------- | --- | --- | --- |
| • “z ∈g”forthelocationsofallN |     |     | σ +M | g,σ graphvertices |     |             |           |     |     |     |
Inadditiontothesesingle-nodeverticesforrecoveryevents
ing.
|     |     |     |     |     |     | in the SIS model, | we employ | further | single-edge | vertices for |
| --- | --- | --- | --- | --- | --- | ----------------- | --------- | ------- | ----------- | ------------ |
As described above, for a given trajectory σ ∈ g, we can infectioneventsasdetailedinSec.V.Oneexampleisthever-
gI↑−
arrange the vertices of graph g into a group of N σ physical tex = (1,0 → 1,a), which we can insert as a back-
y
vertices{(x,g )}andagroupofM backgroundvertices groundvertexatanylocationy = (τ′,i,j)withτ′ < τ. The
|     | x   |     | g,σ |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{(y,g )}. Note that for different trajectories σ,σ′ ∈ g, a current trajectory σ corresponds to a = 0. Changing a to
y
vertexatz ∈ g canbephysicalwithrespecttoσ butaback- 1inaclusterupdateintroducesaninfectioneventfromnode
| groundvertexwithrespecttoσ′. |     |     |     |     |     |     |     |     |     | σ′. |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Infact,thenatureofgraph i to node j at location y of the new trajectory Now, in

5
thenextclusterupdate,wecanforexampleassignthevertex where x ,...,x are the N = N event locations for
|     |     |     |     |     |     |     |     | 1   |     | N   |     | σ   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
gswap = (a,a¯ → 1,1) to the infection event, where a = 1 σ and the first sum runs over the associated vertex types
x
fortrajectoryσ′ anda¯denotesthenegationofa. Ifnoother g ,...,g . Thesumsinthesecondlinerunoverallpossi-
|     |     |     |     |     |     |     |     | x1  | xN  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
verticesfixthestatesofnodesiandjfortimeτ′−,thecluster
|     |     |     |     |     |     |     |     | blepositionsy | m   | andvertextypesg |     | ym ofM | =   | M g,σ | back- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------- | --- | ------ | --- | ----- | ----- |
update can change the variable a to 0, effectively switching ground graph vertices. Compatibility of σ with g is implied
theinfectionsourcesuchthat,inthenewtrajectoryσ′′,node on the right-hand side, which we could make explicit by in-
infectsnodeiattimeτ′,andnodej
j isthenewpatientzero cluding factors ∆(σ z ,g z ), which are however already con-
| asshowninFig.1. |     |     |     |     |     |     |     | tainedinthedefinition(12)ofJ(σ,g).           |     |     |     |     |     |     |      |
| --------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|                 |     |     |     |     |     |     |     | ToachieveEq.(15),wechoosethelocalgraphratesν |     |     |     |     |     |     | (g ) |
z z
suchthattheyobeythelocaltransitionsumrule
B. Jointweightsandsumrules
(cid:88)
|         |        |     |            |             |     |         |      | ω (σ | )=    | ν (g )∆(σ | ,g  | ) ∀σ | ,   |     | (17a) |
| ------- | ------ | --- | ---------- | ----------- | --- | ------- | ---- | ---- | ----- | --------- | --- | ---- | --- | --- | ----- |
|         |        |     |            |             |     |         |      | z z  |       | z z       | z   | z    | z   |     |       |
| We will | derive | the | transition | probability |     | density | W in |      | gz∈Gz |           |     |      |     |     |       |
Eq.(8)fromweightsJ(σ,g)definedinajointspaceofpaths
andthelocaluniformizationsumrule
| and graphs. | These | joint | weights | can | again | be expressed | as  |     |     |     |     |     |     |     |     |
| ----------- | ----- | ----- | ------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
productsoverlocalevents,
|             |     |                  |      |      |          |                  |      |      | (σt)= | (cid:88) |                  |     |     | ∀σt. |       |
| ----------- | --- | ---------------- | ---- | ---- | -------- | ---------------- | ---- | ---- | ----- | -------- | ---------------- | --- | --- | ---- | ----- |
|             |     |                  |      |      |          |                  |      | Γ −Λ |       |          | ν (g )∆(σconst,g |     | )   |      | (17b) |
|             |     | (cid:16)(cid:89) |      |      | (cid:17) |                  |      | z    | z z   |          | z z              | z   | z   | z    |       |
|             |     |                  |      |      |          | e−(cid:82) TdtΓt |      |      |       |          |                  |     |     |      |       |
| J(σ,g)=C(σ) |     |                  | ν (g | )∆(σ | ,g )     | 0                | (12) |      |       | gz∈Gz    |                  |     |     |      |       |
|             |     |                  | z    | z    | z z      |                  |      |      |       |          |                  |     |     |      |       |
z∈g In words, (a) each event rate must equal the rate sum of all
whereν (g )isagraphvertexrate,whichismultipliedbya compatible graph vertices, and (b) the rate sum of all (back-
| z   | z   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ground)graphverticesthatarecompatiblewiththenodesre-
| compatibility | indicator |     | ∆(σ ,g | ) ∈ | {0,1} | that enforces | the |                            |     |     |                            |     |     |     |     |
| ------------- | --------- | --- | ------ | --- | ----- | ------------- | --- | -------------------------- | --- | --- | -------------------------- | --- | --- | --- | --- |
|               |           |     | z      | z   |       |               |     | mainingintheirlocalstateσt |     |     | mustperfectlyfillthegapbe- |     |     |     |     |
compatibility of the vertex g with the local state dynamics z
|     |     |     | z   |     |     |     |     |     |     |     | (σt) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
σ at location z. The local state dynamics σ can be one of tween the local escape rate Λ z [Eq. (5)] and the state-
| z                                                 |     |     |     |     |     | z   |     |                |           |                      |     | z         |     |          |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | -------------------- | --- | --------- | --- | -------- | --- |
|                                                   |     |     |     |     |     |     |     | independent(!) |           | local uniformization |     | rate      | Γ . | Appendix | A   |
| theelementarystate-changingevents(2)oranull-event |     |     |     |     |     |     |     |                |           |                      |     |           | z   |          |     |
|                                                   |     |     |     |     |     |     |     | proves the     | resulting | marginalization      |     | condition |     | (15) for | the |
jointweightsJ(σ,g).
| σconst  | :=(σt−   | →σt+)=(σt |          | →σt), |        |     | (13)      |     |     |     |     |     |     |     |     |
| ------- | -------- | --------- | -------- | ----- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| z       |          | z         | z        | z     | z      |     |           |     |     |     |     |     |     |     |     |
| meaning | that the | local     | state on | nodes | z does | not | change at |     |     |     |     |     |     |     |     |
timet. TheexponentialinEq.(12)isanormalizationfactor, C. Transitionprobabilitiesanddetailedbalance
independentofσandg,characterizedbythetotaluniformiza-
tion rate Γt which can also be decomposed into local rates σ′
|     |     |     |     |     |     |     |     | For the | two transitions | σ   | → g | and g | →   | that compose |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --- | ----- | --- | ------------ | --- |
Γt
≡Γ z suchthat theclusterupdate(10),weusethejointweights(12)todefine
z
thepath-graphtransitionprobabilitydensity
(cid:88)
| Γt  | Γt, |     |     |     |     |     |      |          |        |     |     |     |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------ | --- | --- | --- | --- | --- | ----- |
| =   | z   |     |     |     |     |     | (14) |          |        |     |     |     |     |     |       |
|     | z   |     |     |     |     |     |      |          | J(σ,g) |     |     |     |     |     |       |
|     |     |     |     |     |     |     |      | W(g|σ):= |        | .   |     |     |     |     | (18a) |
P(σ)
| where the | sum | runs over | all positions |     | for | which | we have a |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | ------------- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
graphvertexset(11)attimet.
andthegraph-pathtransitionprobability
| The graph | vertex | sets | G , vertex | rates | ν   | (g ), and | associ- |     |     |     |     |     |     |     |     |
| --------- | ------ | ---- | ---------- | ----- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|           |        |      | z          |       | z   | z         |         |     |     |     |     |     |     |     |     |
ated uniformization rates Γ z are to be chosen such that the J(σ′,g)
|            |             |         |      |     |                     |     |     | W(σ′|g):= |     | ,   |     |     |     |     | (18b) |
| ---------- | ----------- | ------- | ---- | --- | ------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | ----- |
| trajectory | probability | density | P(σ) | is  | the marginalization |     | of  |           |     |     |     |     |     |     |       |
Q(g)
thejointweightsJ(σ,g)overallcompatiblegraphs,
wherethegraphprobabilitydensityQ(g)isthemarginaliza-
(cid:88)′
| P(σ) | =   | J(σ,g). |     |     |     |     | (15) | tionofJ(σ,g)overallcompatiblestates |     |     |     |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- | ---- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
g∋σ
(cid:88)
|                                       |     |     |     |     |     |     |           | Q(g):= |     | J(σ,g). |     |     |     |     | (19) |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ------ | --- | ------- | --- | --- | --- | --- | ---- |
| ThephysicaldimensionofP(σ)is(time)−Nσ |     |     |     |     |     |     | andthedi- |        |     |         |     |     |     |     |      |
σ∈g
|         | J(σ,g)    |     | (time)−Nσ−Mg,σ. |     |     |                  |     |     |     |     |     |     |           |     |     |
| ------- | --------- | --- | --------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
| mension | of        | is  |                 |     |     | Correspondingly, |     |     |     |     |     |     |           |     |     |
|         | (cid:80)′ |     |                 |     |     |                  |     |     |     |     |     |     | (cid:80)′ |     |     |
the“sum” overallgraphs(compatiblewithσ)isactually Note that, in contrast to the path integral in the
|                 | g   |     |     |     |     |     |     |                 |     |           |      |         |         | g∋σ      |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ---- | ------- | ------- | -------- | --- |
| thepathintegral |     |     |     |     |     |     |     |                 |     |           |      |         |         | (cid:80) |     |
|                 |     |     |     |     |     |     |     | marginalization |     | (15) of J | over | graphs, | the sum |          | in  |
σ∈g
Eq.(19)isreallyjustadiscretesum:Aspreviouslydiscussed,
∞
(cid:88)′ (cid:88) (cid:88) 1 agraphgdefinesafinitesetor,inthethermodynamiclimit,at
|     | :=  |     |     |     |     |     | (16) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
M!
|     |              |     |     |     |     |     |     | leastacountablesetofcompatibletrajectories. |     |     |     |     | Aconstructed |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- |
| g∋σ | gx1 ,...,gxN | M=0 |     |     |     |     |     |                                             |     |     |     |     |              |     |     |
graphgfullylocksinthecontinuousdegreesoffreedom(the
(cid:90) T
(cid:88) (cid:88) (cid:88) times of all vertices z ∈ g). The only remaining variables
|     | × dt | ...dt |     |     | ... |     |     |                                  |     |     |     |                        |     |     |     |
| --- | ---- | ----- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
|     |      | 1     | M   |     |     |     |     | definingacompatibletrajectoriesσ |     |     |     | ∈garethediscretestates |     |     |     |
0
|     |     |     | y1,...,yM | gy1 | ∈Gy t1 | gyM ∈Gy | tM  |                                       |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | ------ | ------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |           |     | 1      |         | M   | assignedtothefreeclusters;seeSec.IVE. |     |     |     |     |     |     |     |

6
The choice of W(g|σ) and W(σ′|g) implies the detailed Graphgeneration.–Theresults(21)and(22)correspond
balance(9)forthepath-pathtransitionsσ →σ′ accordingto toaconstructionofacompatiblegraphgintwophases:
thepathtransitionprobabilitydensity
(i) Accordingtotheproductterminthepath-graphtransition
(cid:88)′
W(σ′|σ):= W(σ′|g)W(g|σ) probabilitydensity(21)andemployingthetransitionsum
rule(17a)forthedenominatorsω (σ ),weloopoverall
g∋σ x x
(18) 1 (cid:88)′ J(σ′,g)J(σ,g) event locations x in σ and assign graph vertex g x with
= . (20) probability
P(σ) Q(g)
g∋σ
ν (g )∆(σ ,g )
Inparticular,multiplyingEq.(20)byP(σ)andchangingthe W x (g x |σ x ):= (cid:80) x ν x (g′)∆ x (σ x ,g′) . (23)
path integral over g ∋ σ to an integral over g ∋ σ,σ′, in g
x
′∈Gx x x x x
accordancewiththefactthatJ(σ′,g)=0ifgisincompatible
withσ′,wehave (ii) For all other locations y where no event occurs in σ,
backgroundgraph verticesare insertedthrough aninho-
(cid:88)′ J(σ′,g)J(σ,g)
W(σ′|σ)P(σ)= . mogeneousPoissonpointprocess. Specifically,foreach
Q(g)
g∋σ,σ′ possible type of vertex g, we identify all space-time in-
tervalswhereitwouldbecompatible,andrandomlyadd
Theright-handsidebeingmanifestlysymmetricinσ andσ′,
instances with temporal density ν (g) to g. If the rate
y
thisestablishesthedetailedbalance(9).
ν (g) is uniform on a time interval [T ,T ], we can se-
y a b
lectthenumberMoftype-gbackgroundverticesaccord-
ingtothediscretePoissondistributionµMe−µ/M!with
D. Graphconstruction
µ=(T −T )ν (g)and,then,placevertexgatMtimes
b a y
t ,...,t ontheintervalaccordingtotheuniformran-
1 M
Given a trajectory σ, in step (a) of the cluster update, domdistribution.
we want to construct a compatible graph g according to
the path-graph transition probability density W(g|σ) =
J(σ,g)/P(σ) from Eq. (18a). Recalling the discussion in
E. Clusteridentificationandstateupdate
Sec.IVA,wedenotethelistofg’sbackgroundverticeswith
respecttoσbygbgandtheirlocationsbyy ∈gbg(allvertices
σ σ In step (b) of the cluster update (10), we want to deter-
ing,wherethereisnostatechangeinσ).
mine a new trajectory σ′ that is compatible with the gener-
Transition probability. – Plugging in the expressions (4)
atedgraphgaccordingtothegraph-pathtransitionprobability
and (12) for the path probability density P(σ) and the joint W(σ′|g)=J(σ′,g)/ (cid:0)(cid:80) J(σ,g) (cid:1) fromEq.(18b).
weightsJ(σ,g),weget σ∈g
Transition probability. – Writing the joint weight (12) in
W(g|σ)=W (gbg|σ) (cid:89) ν x (g x )∆(σ x ,g x ) (21) theform
bg σ ω (σ )
x∈σ x x J(σ′,g) =C(σ′)D(σ′,g)K(g) with (24)
withthebackgrounddensity
D(σ′,g):=
(cid:89)
∆(σ′,g ) (25)
z z
W bg (g σ bg|σ)= (cid:16) (cid:89) ν y (g y )∆(σ y ,g y ) (cid:17) e (cid:82) 0 Tdt (cid:2) Λt(σt)−Γt (cid:3) . z∈g
y∈gσ bg being the compatibility indicator and K(g) collecting all σ′
independentterms,thetransitionprobabilityassumesthesim-
For the exponential factor, we can decompose the total es-
pleform
cape and uniformization rates into local rates Λt(σt) =
(cid:80) Λ (σt) and Γt = (cid:80) Γ according to Eqs. (5a) and
y y y y y C(σ′)D(σ′,g)
(14) and plug in the uniformization sum rule (17b). For the W(σ′|g)= . (26)
(cid:80)
C(σ)D(σ,g)
compatibility factors, we can replace σ by the null-events σ∈g
y
σconst[Eq.(13)]becausebackgroundeventsoccurexclusively
y Theresult(26)meansthatweshouldselectamongalltra-
where the state is constant. In this way, we find that the
jectories {σ′ ∈ g} that are compatible with the graph g ac-
background density is the measure for a multi-dimensional
cording to the probability distribution C(σ′). Recall that C
inhomogeneous Poisson point process [49] with time-and-
position-dependentratesλ(y,g )=ν (g )∆(σconst,g ), canbeanindicatorfunctionfortrajectoryconstraintslikehav-
y y y y y ingabigepidemicoutbreakor,moregenerally,aprobability
(cid:16) (cid:89) (cid:17) distribution to favor trajectories of a certain type during the
W (gbg|σ)= ν (g )∆(σconst,g ) (22)
bg σ y y y y sampling. In this section, we assume the trivial case, where
y∈gσ bg C(σ′) = 1 for all g-compatible trajectories such that we
(cid:16) (cid:90) T (cid:88) (cid:88) (cid:17) should select among them with uniform probability. Modi-
×exp − dt ν (g′)∆(σconst,g′) .
y y y y ficationsduetonontrivialtrajectoryconstraintsarediscussed
0 y g y ′∈G y t inSec.VI.

7
Clusteridentification.–Toefficientlytranslatethegraphg V. GRAPHVERTEXSETSFORSISMODELS
intospacetimeclustersC anddeterminetheirallowedstates
k
Inthefollowing,letusconsiderSISmodels,whererecov-
a ∈A(R )⊂{0,...,d−1} (27)
k k eryratesγ andα areallowedtobeposition-dependentand
i i,j
asymmetric (α ̸= α ). For simplicity, we do not denote
i,j j,i
we can employ the union-find (a.k.a. disjoint-set) algorithm
anytimedependenceoftheserates.
[50–53]. Because the state of any node is strictly constant
Our goal is to find sets of single-node graph vertices
betweenthegraphvertices,wecandividethecontinuous-time
G = {g }andedgegraphverticesG = {g },
lineofeachnodeintodiscretesegmentsandusetheunion-find (t,i) (t,i) (t,i,j) (t,i,j)
associated vertex rates ν (g ), and uniformization rates Γ
algorithmtogroupthemaccordingtotherulesofg: x x x
such that the transition and uniformization sum rules (17a)
and(17b)areobeyed, andweobtainanergodicalgorithmin
• For every node i ∈ {1,...,N}, collect the times t <
1
thesensethattheclusterupdatesallowustoreachanyphys-
t < ··· < t of all graph vertices in g where node
2 M−1
ically valid trajectory σ. According to our convention from
i is involved. In conjunction with t := 0 and t :=
0 M
Sec.IIIwehavei<j.
T, these times decompose the trajectory of node i into a
sequenceofsegments(i,t ,t )onwhichthestateσ′t
m m+1 i
isconstant.
A. Single-nodevertexsetS1
• We then create a union-find data structure, where every
segment is initialized as its own independent root R (its Forthesingle-nodevertices,relatedtorecoveryevents,we
own cluster with PARENT(R) ← R). For every root canchoose
R, we initialize the set of allowed states as A(R) =
{0,1,...,d−1}andassignthetrivialidentitymapfrom G = (cid:8) g0, gR+, gR−(cid:9) (30)
x x x x
clustertonodestates(MAP(R)←Id).
withx=(t,i)and
• Now,iteratethroughthegraphverticesg atlocationsz =
z
(t,z) ∈ g to bind the segments together and apply con- g0 =(0→0), (31a)
x
straints. Avertexg canimposebijectiverelationsamong
z gR+ =(a→0), (31b)
someoftheparticipatingvariabless = (σt−,σt+)(e.g., x
z z
imposingthattwovariablesareequal)andrestrictthesets gR− =(1→a), (31c)
x
ofvalidstatesforthesevariablesasdetailedinSec.Vfor
SIS models. A bijective relation s = f(s ) between wherea∈{0,1}indicatesthatthecorrespondingnode-istate
k ℓ
two variables s and s corresponds to a cluster unifica- σt− just before the vertex time t (for gR+) or σt+ just after
k ℓ i x i
tion. Unless the two variables were already part of the time t (for gR−) remains unconstrained by the vertex. The
x
same cluster, we attach one cluster tree to the other by verticesgR±werealreadydiscussedinExample4.Thevertex
x
making one of the roots, say R the parent of the other g0 isonlycompatiblewiththenull-event,wherenodeistays
k x
(PARENT(R
ℓ
) ← R
k
),storetheassociatedbijectiverela- susceptible,i.e.,σ
i
t− =σ
i
t+ =0.
tion(MAP(R
ℓ
)←f)andreducetheavailablestatesetto Denoting the associated vertex rates by ν
x
0 and ν
x
R±, the
theintersection transitionsumrule(17a)fortheonlyphysicallypossiblestate
change(1→0)reads
(cid:0) (cid:1)
A(R )←A(R )∩f A(R ) . (28)
k k ℓ
γ =ω (1→0)=νR++νR−, (32)
i x x x
If the graph vertex explicitly restricts the allowed states
f
o
o
f
r
th
a
e
v
c
a
l
r
u
ia
s
b
te
le
ra
s
c
k
c
t
o
o
rd
A
in
g
g
z,
l
k
y
,werestricttheallowedstateset
t
a
h
n
e
d,
un
w
if
it
o
h
rm
th
i
e
za
l
t
o
i
c
o
a
n
l
s
e
u
s
m
ca
r
p
u
e
le
r
s
at
(
e
1
s
7
Λ
b)
x
f
(
o
0
r
)
s
=
tate
0
s
a
σ
n
t
d
=
Λ
0
x (
a
1
n
)
d
=
σt
γ
=
i ,
i i
1imposetheconstraints
A(R )←A(R )∩A . (29)
k k gz,k
Γ =ν0+νR+, Γ −γ =νR−. (33)
x x x x i x
Cluster state update. – The clusters C , identified by the
k This is a system of three linear equations for four param-
treerootswithPARENT(R
k
)=R
k
,decomposethefullspace-
eters. Choosing φ := ν0 as the free parameter, the solution
timevolume[0,T]×{1,...,N}intoconnectedcomponents. x
spaceis
Forthetransitiong → σ′ tothenewtrajectoryσ′, weiden-
t t h if e y se al a l r “ e f i r n e d e” ic c a l t u ed st b er y s r w ed it l h in d e k s. ≡ Th | e A s ( t R at k es )| o > ne 1 a . ch In fr F ee ig c s l . u 1 s - te 3 r , (cid:0) Γ x , ν x 0, ν x R+, ν x R−(cid:1) = (cid:16) γ i + φ 2 , φ, γ i − φ 2 , φ 2 (cid:17) (34)
C arethenupdatedbyeitherretainingtheoriginalstatefrom
k
σ or choosing one of the other d − 1 allowed states with with0≤φ≤2γ asallratesneedtobenonnegative.
k i
equal probability 1/d . This cluster-flip naturally generates In order to minimize the computation time per cluster up-
k
an updated valid trajectory σ′ without requiring subsequent date, it is generally best to minimize the uniformization rate
time-stepre-evaluations,bypassingcriticalslowingdown. Γ suchthat,inlightoftheuniformizationsumrule(17b)and
x

8
the background density (22), the total background-vertex in- and,withthelocalescaperates
sertionratesforeverystateareassmallaspossible.Thisleads
totheoptimumatφ=0with Λ (0,0)=Λ (1,1)=0, (39a)
x x
(cid:0) Γ , ν0, νR+, νR−(cid:1) =(γ , 0, γ , 0), (35) Λ x (1,0)=α i,j , and Λ x (0,1)=α j,i , (39b)
x x x x i i
theuniformizationsumrules(17b)forthestates(0,0),(1,1),
implying that we would actually work with only one single-
nodevertex,G ={gR+}whichcanprolonginfectionsorin- (1,0),and(0,1)imposetheconstraints
x x
troduce new infections. The infection-shortening vertex gR−
x Γ =νaa+νa↑−+νa↓−, (40a)
would be gone, implying that infection intervals can only be x x x x
removedintheirentiretyormodifiedbyedgevertices. Con- Γ =νaa+νI↑++νI↓+, (40b)
x x x x
cerning numerical efficiency, we also need to consider auto-
Γ −α =νI↑−, (40c)
correlationsintheMarkovchain(8)oftrajectories. Whilethe x i,j x
φ=0solution(35)generallyhasthelowestcomputationcost Γ x −α j,i =ν x I↓−. (40d)
perupdate,itmayimplylongerauto-correlationtimesor,de-
pendingontheconstraintC(σ)anditsimplementation,even Equations (38) and (40) form a system of six linear equa-
failergodicity. tions for eight parameters. Choosing ϑ↑ := νa↑− and ϑ↓ :=
x
Alternatively,wecouldchoosethemaximumφ=2γ such νa↓−asthefreeparameters,thesolutionspaceis
i x
that vertex gR+ is removed. However, this would imply that
we cannot ex x tend infection times or increase the number of (cid:0) Γ x , ν x aa, ν x a↑−, ν x a↓−, ν x I↑−, ν x I↓−, ν x I↑+, ν x I↓+(cid:1)
infectednodesatt=0. = (cid:0) 2α¯−2ϑ¯, 2α¯−4ϑ¯, ϑ↑, ϑ↓,
Inourexperience,thesolution(34)withφ=γ /2isasolid
i α −2ϑ¯, α −2ϑ¯, ϑ↓+∆α, ϑ↑−∆α (cid:1) (41)
choice. j,i i,j
with
B. EdgevertexsetE1
α¯ := αi,j+αj,i, ∆α:=α −α , ϑ¯:= ϑ↑+ϑ↓ (42)
2 i,j j,i 2
Fortheverticesonedges(i,j),relatedtoinfectionevents, andϑ¯limitedtotherange
wecanchoose
G = (cid:8) gaa, ga↑−, ga↓−, gI↑−, gI↓−, gI↑+, gI↓+(cid:9) (36) |∆α|≤2ϑ¯≤min(α i,j ,α j,i ), (43)
x x x x x x x x
withx=(t,i,j)and whichfollowsfromtheconstraintthatallratesneedtobenon-
negative.
g x aa =(a,a→a,a), (37a) The admissible range (43) is actually only nonempty if
ga↑− =(a,0→a,a), (37b) |∆α| ≤ min(α i,j ,α j,i ), i.e., only for moderately asymmet-
x
ricinfectionrateswith
ga↓− =(0,a→a,a), (37c)
x
1 α 1 α
gI↑− =(1,0→1,a), (37d) ≤ i,j ≤2 or ≤ j,i ≤2. (44)
x
2 α 2 α
gI↓− =(0,1→a,1), (37e) j,i i,j
x
gI↑+ =(1,a→1,1), (37f) Toliftthisrestriction,wewillconsideralternativeedge-vertex
x
setsinSecs.VDandVE.
gI↓+ =(a,1→1,1). (37g)
x Fortherestofthissection,letusassumesymmetricinfec-
tionandvertexrates,i.e.,
Againa ∈ {0,1}indicatesthatthecorrespondingnodestate
just before or just after the vertex time t remains uncon-
α =α =:α, ϑ↑ =ϑ↓ =:ϑ. (45)
strainedbythevertex,butifvariableaoccursmultipletimes i,j j,i
inavertex,itimposesequalityamongthecorrespondingnode
How should we choose ϑ ∈ [0,α/2] to make CPMC as effi-
states.Inparticular,thevertexgaamatchesthetwonull-events
x cientaspossible? Theanswerisnotobvious.
wheretheedgestayseitherinthe(0,0)orinthe(1,1)state.
The uniformization rate Γ = 2α − 2ϑ and, hence, the
Thevertexga↑− matchesthenull-event(0,0 → 0,0)andthe x
x expected computation time per cluster update are minimized
infectionevent(1,0→1,1).
forϑ=α/2with
Denoting the associated vertex rates by νaa, νa↑−, νa↓−,
x x x
ν x I↑−, ν x I↓−, ν x I↑+, and ν x I↓+, the transition sum rules (17a) (cid:0) Γ , νaa, νa↑−, νa↓−, νI↑−, νI↓−, νI↑+, νI↓+(cid:1)
for the two infection-related state changes (1,0 → 1,1) and x x x x x x x x
(cid:16) α α α α(cid:17)
(0,1→1,1)read = α,0, , , 0, 0, , , (46)
2 2 2 2
α =ω (1,0→1,1)=νa↑−+νI↑−+νI↑+, (38a)
i,j x x x x removingtheverticesgaa,νI↑−,andνI↓−. Hence,weareleft
α j,i =ω x (0,1→1,1)=ν x a↓−+ν x I↓−+ν x I↓+, (38b) withthereducedvertex x setG x x = (cid:8) g x a↑− x ,g x a↓−,g x I↑+,g x I↓+(cid:9) .

9
FIG.2. UpstreamlockavalancheswithedgevertexsetE1andunlockingwithsetE2. ForagivenSIS-modeltrajectoryσ,panels(a),
(b),and(c)showdifferentcompatiblegraphsg (top)andtheassociatedconfigurationsofclusters(bottom). Weemploythesamegraphical
conventionsasinFig.1,andpanel(d)specifiesthedifferentemployedvertexsetsinaccordancewithSec.V.Panel(a)showsan(unlikely)
choiceofgraphverticesthatleadtoabigfreeclusterC thatincludespatientzero(node3). Toachieveamobilepatientzerowithvertex
2
sets S1 and E1,thegraphmusthappentobesuchthatallverticesdownstreamofpatientzeroaregR+,ga↑−,orga↓− asinthiscase. The
probabilityofthisdecreasesexponentiallyinthelengthoftheinfectiontree.Asillustratedinpanel(b),asingledownstreamgI↑−,gI↓−orgR−
leadstoacascadeoflocksthatfixpatientzero. Suchupstreamlockavalanchesleadtoageneralinflexibilityoftheinfectiontree’s“trunk”
andextendedautocorrelationsinthepathMarkovchain(8).Asexemplifiedinpanel(c)anddiscussedinSec.VD,thealternativeedgevertex
intheshownexampleleadstoaverydifferenttrajectoryσ′,wherenode4isthenew
| setE2resolvesthisissue. |     | FlippingclustersC |     | 2 ,...,C 6 |     |     |     |     |     |     |     |
| ----------------------- | --- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
patientzero.Notethat,forclarity,wehavenotusedallavailablegraphverticeshereortriedtoshowparticularlyrealisticexamples.
Theotherextremeϑ=0maximizestheuniformizationrate vertexsetapplicableonlyifthetworatesvarybylessthana
| with |     |     |     |     |     | factoroftworelativetoeachother. |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
(cid:0) νI↓+(cid:1) Constrainingtheepidemictrunk: Inascenario,wherewe
| Γ , | νaa, νa↑−, | νa↓−, νI↑−, | νI↓−, | νI↑+, |     |     |     |     |     |     |     |
| --- | ---------- | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
x x x x x x x x start with a single infected node at time t = 0 (patient zero)
=(2α, 2α, 0, 0, α, α, 0, 0) (47) which infects further nodes, the cluster updates with vertex
setsS1andE1alonewouldmakeupdatesofthepatient-zero
| s u c h t h a t   | w e w o u ld | w o r k w | i th t h e | re d u ced v e rt e | x s e t G = |                  |                   |             |        |          |                 |
| ----------------- | ------------ | --------- | ---------- | ------------------- | ----------- | ---------------- | ----------------- | ----------- | ------ | -------- | --------------- |
|                   |              |           |            |                     | x           | n o d e v er y u | n l ik e ly . W h | ile g a ↑ − | = ( a, | 0 → a ,a | ) a n d g a ↓ − |
| (cid:8) a a, I↑ − | I↓ − (cid:9) |           |            | I ↑− I ↓            | −           |                  |                   | x           |        |          | x               |
g g ,g . No t e t ha t v ert i c es g an d g l e av e th e ve r t ice s i n p ri n c ip le a llo w p at i e nt zer o to b ein a f re e c lu s t e r,
| x x | x   |     |     | x x |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
futurestateofaninfectednodeunconstrained,whichmaybe thiswillonlyhappenundertheconditionthatalldownstream
computationallybeneficialforthesimulationofbigoutbreaks.
infectionsintheinfectiontreegetassignedthistypeofgraph
|     |     |     |     |     |     | vertexinsteadofgI↑−   | =(1,0→1,a),gI↑+                    |     |     | =(1,a→1,1), |     |
| --- | --- | --- | --- | --- | --- | --------------------- | ---------------------------------- | --- | --- | ----------- | --- |
|     |     |     |     |     |     |                       | x                                  |     |     | x           |     |
|     |     |     |     |     |     | ortheir↓counterparts. | Butthelatterverticeswillbeselected |     |     |             |     |
C. DrawbacksofedgevertexsetE1
withafiniteprobabilityandbackgroundsingle-nodevertices
|     |     |     |     |     |     | gR− = (1 | → a) will | be dropped | by  | the Poisson | process, |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | --- | ----------- | -------- |
y
TheedgevertexsetE1hastwoimportantdrawbacks. lockingintheinfectedstateupstream. Thesingle-nodevertex
Restriction on asymmetry: It leads to the restriction (44) gR+ = (a → 0)cannothelpeither. Hence,theprobabilityof
x
ontheasymmetryofinfectionratesα i,j andα j,i ,makingthe apatientzeroresidinginafreeclusterdecaysexponentiallyin

10
the“length”oftheinfectiontree(thenumberofdownstream • While the vertices ga↑+ = (a,a¯ → a,1) and ga↓+ are
x x
infection events). This is illustrated in panels (a) and (b) of similarinthisrespect,wekeepthemastheywillbeuseful
Fig. 2. The issue extends beyond patient zero – it heavily for SIS models with asymmetric infection rates α ̸=
i,j
constrainstheentire“trunk”oftheinfectiontreeduetosuch α . They are also useful because, in contrast to gswap,
j,i x
upstream lock avalanches, restricting the cluster updates to gI↑−, and gI↓−, they do not fix the future of the source
x x
beautifullyfluctuatethesurfaceofanepidemictreebutmak- nodeandallowforuninterruptedflippabletimesegments
ing it difficult to mutate its skeleton. While this can be sub- ofaninfectionsourcenode.
stantially alleviated by using special update rules for patient
Includingtheadditionalnull-eventvertexga¯a,theseconsid-
zero (see Sec. VI) and employing parallel tempering [54], it x
erationsleadustotheedgevertexsetE2
ismoreattractivetoresolvetheissuebyanadaptationofthe
edgevertexset. G = (cid:8) gaa, ga¯a, gswap, gI↑−, gI↓−, ga↑+, ga↓+(cid:9) (49)
x x x x x x x x
withx=(t,i,j).Theresultingtrajectoryflexibilityincluster
D. EdgevertexsetE2–unlockingtheepidemictrunk
updatesisillustratedinFigs.2cand3.
Denotingtheassociatedvertexratesbyνaa,νa¯a,νswap,νI↑−,
x x x x
Let us first assess our options to alleviate the drawbacks νI↓−, νa↑+, and νa↓+, the transition sum rules (17a) for the
x x x
of vertex set E1 described in Sec. VC. As detailed in Ap- twoinfection-relatedstatechanges(1,0 → 1,1)and(0,1 →
pendixBtheverticesg x a↑−,g x a↓−,g x I↑−,g x I↓−,g x I↑+,g x I↓+ from 1,1)read
Eq.(37)incombinationwiththenewvertices
α =ω (1,0→1,1)=νswap+νa↑++νI↑−, (50a)
gswap =(a,a¯→1,1), (48a) i,j x x x x
x α =ω (0,1→1,1)=νswap+νa↓++νI↓−. (50b)
ga↑+ =(a,a¯→a,1), (48b) j,i x x x x
x
ga↓+ =(a¯,a→1,a) (48c) Withthelocalescaperates(39),theuniformizationsumrules
x (17b)forthestates(0,0),(1,1),(1,0),and(0,1)imposethe
representallnineoptionsforverticesthatarecompatiblewith constraints
an infection event and feature at least one free variable a ∈
{0,1}witha¯ denotingthenegationofa. Letusalsoaddthe Γ x =ν x aa, (51a)
null-eventvertex Γ =νaa, (51b)
x x
ga¯a =(a,a¯→a,a¯) (48d) Γ x −α i,j =ν x a¯a+ν x a↓++ν x I↑−, (51c)
x
Γ −α =νa¯a+νa↑++νI↓−. (51d)
tothelist. x j,i x x x
Toachievealargenumberoffreeclusters:
As Eqs. (51a) and (51b) are identical, we have a system
• Letusavoidallverticesthatfixallfouroftheinvolvedt−
of five linear equations for eight parameters. Choosing the
andt+variables,like(1,0→1,1).
uniformizationrateΓ ,ψ :=νswap,andϕ:=νI↑− asthefree
x x x
• The swap vertex gswap = (a,a¯ → 1,1) prevents up- parameters,thesolutionspaceis
x
stream lock avalanches through temporal decoupling, al-
(cid:0) Γ , νaa, νa¯a, νswap, νI↑−, νI↓−, νa↑+, νa↓+(cid:1)
lowing patient zero to move and, more generally, infec- x x x x x x x x
tionsourcestoswap. Theinputvariables(a,a¯)arecom- (cid:16)
= Γ , Γ , Γ −α −α +ψ, ψ,ϕ,ϕ,
pletely disconnected from the outputs (1,1). If a subse- x x x i,j j,i
(cid:17)
quenteventlocksthefutureofnodeiorj to1, thatlock
α −ψ−ϕ,α −ψ−ϕ (52)
i,j j,i
hits the (1,1) output of this vertex and cannot cross the
eventboundarytolockthepast.
with
• TheedgeverticesgI↑− = (1,0 → 1,a)andgI↓− incom-
x x Γ ≥α +α −ψ and (53a)
bination with the single-node vertices gR− = (1 → a) x i,j j,i
y
preventdownstreamlockavalanches. Whiletheswapver- 0≤ψ+ϕ≤min(α i,j ,α j,i ) (53b)
tex locks the immediate downstream future of the edge’s
nodes to 1 (infected), background recovery vertices gR− followingfromtheconstraintthatallratesneedtobenonneg-
y ative.
canconvertlockednodesbacktoafreevariableaforthe
remainderofthetimeline;gI↑−andgI↓−cangeneratefree It is generally desirable to reduce the uniformization rate
x x Γ . Doing so removes the ga¯a vertex and leaves us with
targetnodesdownstreamandallowfortheconversionbe- x x
the two free parameters ψ and ϕ. With ψ = νswap primar-
tweeninfectioneventsandnull-events. x
ily controlling upstream flexibility and ϕ = νI↑− = νI↓−
x x
• Letusavoidtheverticesga↑− = (a,0 → a,a)andga↓−, controlling downstream flexibility, a pragmatic choice could
x x
because they impose equality for three of the involved be to choose some 0 ≤ ψ ≤ min(α ,α ) and set ϕ =
i,j j,i
statesandfixthefourth, whichcanleadtoapropagation min(α ,α ) − ψ, with the ψ-optimum depending on the
i,j j,i
oflocksinbothtimedirections. networkstructure.

11
FIG.3.ExampleforamorecomplexclusterupdatewithedgevertexsetE2.(a)AnSIS-modeltrajectoryσonsevennodeswithnode4as
patientzeroandfourinfectednodesatthefinaltime.(b)AcompatiblegraphgbasedontheS1andE2vertexsets.Asbefore,verticesatstate-
changingeventsinσareindicatedbyorangeboxesandbackgroundverticesareindicatedbyredboxes.(c)Tomaketheclusteridentification
easierforthehumaneye,wehaveremovedallverticesthatultimatelyhavenofreestatevariablesandhavefixedthecorrespondingpartsofthe
trajectory. (d)Clusterrepresentationofthegraphg,whereeachredsolidtimesegmentwithlabel“k”carriesstatea =0,1ofafreecluster
k
C andeachreddashedtimesegmentwithlabel“k¯”carriesthenegatedstatea¯ =1,0ofclusterC .(e)FlippingthestatesofclustersC ,C ,
| k   |     |     |     |     |     |     |     |     | k   |     | k   |     |     |     | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C ,C ,C ,C ,andC (withrespecttotheirstateinσ),wearriveatthenewtrajectoryσ′,whereboththetrunkandleavesoftheinfectiontree
| 3   | 4 6 7 | 8   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
havechangedsubstantially.Thenewpatientzeroisnode5,andtherearenowthreeinfectednodesatthefinaltime.
Incontrasttotherestriction(44)ofvertexsetE1,Eq.(53) This gives a system of five linear equations for nine pa-
shows that set E2 works for any ratio of the infection rates rameters. Choosing the uniformization rate Γ , ψ := νswap,
|     |     |     |     |     |     |     |     |     |       |     |      |     |     | x   | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | ϕ↑  | νI↑−, | ϕ↓  | νI↓− |     |     |     |     |
α i,j and α j,i . However, on edges with extreme asymmetry := := as the free parameters, the solution
|                                                      |     |     |       |                          |     |     |     |         |     | x   | x   |     |     |     |     |
| ---------------------------------------------------- | --- | --- | ----- | ------------------------ | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| whereoneoftheinfectionratesiszeroandtheothernonzero, |     |     |       |                          |     |     |     | spaceis |     |     |     |     |     |     |     |
| wehavetochooseψ                                      |     |     | =ϕ=0. | Thisremovestheswapvertex |     |     |     |         |     |     |     |     |     |     |     |
swap
| g x                         | =(a,a¯→1,1),whichisnaturalaswecannotswapin- |     |     |                  |     |     |        |     |  Γ |    |    |     | Γ   |    |     |
| --------------------------- | ------------------------------------------- | --- | --- | ---------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                             |                                             |     |     |                  |     |     |        |     |     | x   |     |     | x   |     |     |
| fectionsourcesonsuchanedge. |                                             |     |     | Theremovaloftheg |     |     | I↑−and |     | ν   | aa  |     |     | Γ   |     |     |
|                             |                                             |     |     |                  |     |     | x      |     |  x |    |    |     | x   |    |     |
g I↓−verticesishoweverproblematicastheyareanimportant  10   +ψ−∆ϕ
| x                               |                                           |            |     |                 |     |         |        |     |  ν       |    |  Γ x −α | i,j −α  | j,i    |    |      |
| ------------------------------- | ----------------------------------------- | ---------- | --- | --------------- | --- | ------- | ------ | --- | --------- | --- | -------- | ------- | ------ | --- | ---- |
| antidote                        | against                                   | downstream |     | lock avalanches |     | and are | needed |     | x         |     |          |         |        |     |      |
|                                 |                                           |            |     |                 |     |         |        |     |  ν01     |    | Γ −α    | −α      | +ψ+∆ϕ |     |      |
|                                 |                                           |            |     |                 |     |         |        |     |  x       |    |  x      | i,j     | j,i    |    |      |
| topruneleafsoftheinfectiontree. |                                           |            |     |                 |     |         |        |     |  ν swap | =  |          |         | ψ      |    | (57) |
|                                 |                                           |            |     |                 |     |         |        |     |  x       |    |         |         |        |    |      |
|                                 |                                           |            |     |                 |     |         |        |     | νI↑−    |     |         |         | ϕ↑     |    |      |
|                                 |                                           |            |     |                 |     |         |        |     |  x       |    |         |         |        |    |      |
|                                 |                                           |            |     |                 |     |         |        |     | νI↓−    |     |         |         | ϕ↓     |    |      |
|                                 |                                           |            |     |                 |     |         |        |     |  x       |    |         |         |        |    |      |
|                                 | E. EdgevertexsetE3–unlockingfullasymmetry |            |     |                 |     |         |        |     | νa↑+    |     |         | α −ψ−ϕ↑ |        |    |      |
|                                 |                                           |            |     |                 |     |         |        |     | x         |     |          | i,j     |        |     |      |
|                                 |                                           |            |     |                 |     |         |        |     | νa↓+      |     |          | −ψ−ϕ↓   |        |     |      |
α j,i
x
TheproblemsofvertexsetE2forstronglyasymmetricin-
| fection | rates | α ̸= | α can | be resolved | by  | introducing | the |                      |     |     |     |     |     |     |     |
| ------- | ----- | ---- | ----- | ----------- | --- | ----------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
|         |       | i,j  | j,i   |             |     |             |     | with∆ϕ:=νI↑−−νI↓−and |     |     |     |     |     |     |     |
|         |       |      |       |             |     |             |     |                      |     | x   | x   |     |     |     |     |
asymmetry-nullifying(blocker)vertices
|     |                  |     |     |     |     |     |       |     | Γ ≥α | +α   | −ψ+|∆ϕ| |       | and        |     | (58a) |
| --- | ---------------- | --- | --- | --- | --- | --- | ----- | --- | ---- | ---- | ------- | ----- | ---------- | --- | ----- |
|     | g10 =(1,0→1,0),  |     |     |     |     |     | (54a) |     | x    | i,j  | j,i     |       |            |     |       |
|     | x                |     |     |     |     |     |       |     |      |      | (cid:0) |       | −ϕ↓(cid:1) |     |       |
|     |                  |     |     |     |     |     |       |     | 0≤ψ  | ≤min | α       | −ϕ↑,α |            |     | (58b) |
|     | g 01 =(0,1→0,1). |     |     |     |     |     | (54b) |     |      |      | i,j     |       | j,i        |     |       |
x
Alsoremovingthenull-eventvertexga¯a, followingfromtheconstraintthatallratesneedtobenonneg-
whichturnedoutas
x
| inessentialforthesetE2,weobtainthemodifiededgevertex |             |     |           |           |      |            |     | ative. |          |         |         |                |         |             |         |
| ---------------------------------------------------- | ----------- | --- | --------- | --------- | ---- | ---------- | --- | ------ | -------- | ------- | ------- | -------------- | ------- | ----------- | ------- |
| set                                                  |             |     |           |           |      |            |     |        | Choosing | the     | minimal | uniformization |         | rate Γ      | = α +   |
|                                                      |             |     |           |           |      |            |     |        |          |         |         |                |         | x           | i,j     |
|                                                      |             |     |           |           |      |            |     | α j    | ,i − ψ   | + |∆ϕ|, | one     | of the         | blocker | vertices is | removed |
|                                                      | (cid:8) aa, | 10, | 01, swap, | I↑−, I↓−, | a↑+, | a↓+(cid:9) |     |        |          |         |         |                |         |             |         |
G x = g g g g g g g g . (55) (ν 1 0 =0orν 01 =0).Choosingthemaximalψ =min(α −
|     | x   | x   | x x | x x | x   | x   |     |      | x   | x       |          |       |           |            | i,j     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------- | -------- | ----- | --------- | ---------- | ------- |
|     |     |     |     |     |     |     |     | ϕ↑,α |     | −ϕ↓) to | increase | trunk | mobility, | one of the | source- |
j,i
Thetransitionsumrules(50)anduniformizationsumrules free vertices is removed (νa↑+ = 0 or νa↓+ = 0). Lastly, a
|       |           |     |            |       |           |        |     |     |     |     |     | x   |     | x   |     |
| ----- | --------- | --- | ---------- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (51a) | and (51b) | for | the states | (0,0) | and (1,1) | remain | un- |     |     |     |     |     |     |     |     |
pragmaticchoicewouldbe
|                                                      |          |     |         |        |          | ν10 | ν01, |     |     |     |     |     |     |     |      |
| ---------------------------------------------------- | -------- | --- | ------- | ------ | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ---- |
| changed.                                             | Denoting |     | the new | vertex | rates by | and |      |     |     |     |     |     |     |     |      |
|                                                      |          |     |         |        |          | x   | x    |     |     |     |     |     |     |     |      |
| theadapteduniformizationsumrulesforthestates(1,0)and |          |     |         |        |          |     |      |     | ϕ↑  |     |     | ϕ↓  |     |     |      |
|                                                      |          |     |         |        |          |     |      |     | =qα |     | and | =qα |     |     | (59) |
| (0,1)read                                            |          |     |         |        |          |     |      |     |     | i,j |     |     | j,i |     |      |
=ν10+νa↓++νI↑−, withasuitable0 < q < 1(tobeoptimizeddependingonthe
|     | Γ −α  |                 |     |     |     |     | (56a) |           |     |     |     |     |     |     |     |
| --- | ----- | --------------- | --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     | x i,j | x               | x   | x   |     |     |       | network). |     |     |     |     |     |     |     |
|     | Γ −α  | =ν01+νa↑++νI↓−. |     |     |     |     | (56b) |           |     |     |     |     |     |     |     |
x j,i x x x Assuming α i,j ≥ α j,i without loss of generality, these

12
choicesleadto When averaging over trajectories σ to estimate observables
etc.,weonlytakeintoaccountthetrajectoriesσwithasingle
|     | (cid:0)  |         |           |         |               |        | a↓+(cid:1) |     |                    |         |          |      |            |            |       |
| --- | -------- | ------- | --------- | ------- | ------------- | ------ | ---------- | --- | ------------------ | ------- | -------- | ---- | ---------- | ---------- | ----- |
|     | Γ ,      | ν aa, ν | 10, ν 01, | ν swap, | ν I↑−, ν I↓−, | ν a↑+, | ν          |     | infectednodeatt=0. |         |          |      |            |            |       |
|     | x        | x       | x x       | x       | x x           | x      | x          |     |                    |         |          |      |            |            |       |
|     | (cid:16) |         |           |         |               |        |            |     |                    |         | (cid:80) |      |            |            |       |
|     |          |         |           |         |               |        |            |     | For t              | = T, if | σT       | ≥ NI | , we don’t | freeze any | node. |
|     | =        | (1+q)α  | , (1+q)α  |         | , 0,2q∆α,     | (1−q)α |            | ,   | (cid:80)           |         | i i      | m    | i n        |            |       |
i,j i,j j,i If σT < NI , we freeze t h e t = T states of all nodes
|     |     |     |     |     |     |     |     |     | i i | min |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:17) thatareinfectedinthecurrenttrajectoryσbeforetheupdate.
|            |     | qα , | qα , (1−q)∆α, |     | 0 , |     |     | (60) |                 |     |                     |     |         |             |         |
| ---------- | --- | ---- | ------------- | --- | --- | --- | --- | ---- | --------------- | --- | ------------------- | --- | ------- | ----------- | ------- |
|            |     | i,j  | j,i           |     |     |     |     |      |                 |     |                     |     |         |             |         |
|            |     |      |               |     |     |     |     |      | When estimating |     | observables,        |     | we only | include the | paths σ |
|            |     |      |               |     |     |     |     |      | withatleastNI   |     | infectednodesatt=T. |     |         |             |         |
| where∆α:=α |     |      | −α            | .   |     |     |     |      |                 | min |                     |     |         |             |         |
i,j j,i This approach has two drawbacks: (i) A minor concern is
|     |     |     |     |     |     |     |     |     | thatitbreaksstrictdetailedbalance(9).               |     |     |     |     | Asakindofbound- |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --------------- | ---- |
|     |     |     |     |     |     |     |     |     | aryeffect,thisusuallydoesnotleadtoobservableerrors. |     |     |     |     |                 | (ii) |
VI. TRAJECTORYCONSTRAINTS&INITIALIZATION
Itreducestheefficiencyoftheclusterupdatesasweproduce
FORSISMODELS
trajectoriesthatareultimatelydisregarded,andthelocksgen-
erallyincreasetrajectoryautocorrelations.
|     | Concerning |     | macroscopic | constraints |     | and the | construction |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ----------- | ----------- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ofavalidinitialtrajectoryσ[1]forthepathMarkovchain(8),
| let | us discuss | the | specific | case | of an | SIS model, | where | we  |     |     |     |     |     |     |     |
| --- | ---------- | --- | -------- | ---- | ----- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
B. Cluster-levelrejectionsampling
wantonlyoneinfectednodeatthestartingtimet=0(patient
| zero)andatleastNI |     |     |     | infectednodesatthefinaltimet=T. |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
min
Tosamplepathsσ undertheseconstraints, thedynamicpro- Analternativeapproachthatresolvestheproblemsofcon-
|     |     |     |     |     |     |     |     |     | ditional locks | is  | cluster-level | rejectionsampling. |     | The | idea is |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | ------------------ | --- | --- | ------- |
grammingmethoddescribedinSec.VICandAppendixCis
generallyapplicableandefficient,anditcanbeusedformany to satisfy the t = 0 constraint by construction and use coin
otherchoicesoftrajectoryconstraints. Asdynamicprogram- flips for the remaining free t = T clusters. Because every
mingrequiresmorecoding effort, wealsodescribetwosim- validcombination(a ,...,a )offreeclustershasequalsta-
|     |     |     |     |     |     |     |     |     |     |     | 1   | K   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pler approaches based on conditional locks and cluster-level tisticalweight(beforeapplyingtheconstraints),wejustneed
rejectionsamplinginSecs.VIAandVIB.Finally,Sec.VID to ensure our proposal method samples uniformly from the
describes how to initialize the path Markov chain (8) with a subspaceoftrajectoriesthatsatisfythepatient-zeroconstraint.
validtrajectoryσ[1]thatobeystheboundaryconditions. Becausebackgroundverticesleavethet=0statesofmany
Below, weusethefollowingsetup: Aftertheclusteriden- nodesentirelydecoupledfromtheepidemic, K isgenerally
0
tification (Sec. IVE), we determine how many nodes are al- large, makingnaiverandomassignmentcomputationallyim-
readypermanentlylockedtotheinfectedstate1attimest=0 possible as the chance of randomly drawing exactly one in-
andT. Foravalidtrajectoryσ,theseare fected node vanishes exponentially. Instead, we can satisfy
|     |     |     |     |     |     |     |     |     | thet=0constraintbyexactconstruction. |     |     |     |     | IfMI | =1,we |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | ---- | ----- |
lo c k ed
M I ∈{0,1} and N I ∈{0,N}, (61) fix all clusters in K to the state that yields 0 in f e c ted nodes
|     | l ocked |     |     |     | l ocked |     |     |     |     |     | 0   |     |     |     |     |
| --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MI
|     |     |     |     |     |     |     |     |     | at t = 0. | If  | =   | 0, we uniformly |     | randomly select | ex- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --------------- | --- | --------------- | --- |
respectively. LetC ,...,C betheK freeclustersthatinter- locked
1 K actly one cluster from K among those capable of providing
sect the t = 0 or t = T time slices, forming the (generally 0
|     |     |     |     |     |     |     |     |     | exactlyoneinfectednodeatt |     |     | =   | 0(patientzero),fixitsstate |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | -------------------------- | --- | --- |
overlapping)collectionsofclusters accordingly, and set all remaining clusters in K to the state
0
|     |       |     |     |        |     |     |     |      | that yields | 0 infected | nodes | at  | t = 0. This | exactly | satisfies |
| --- | ----- | --- | --- | ------ | --- | --- | --- | ---- | ----------- | ---------- | ----- | --- | ----------- | ------- | --------- |
|     | K and | K   | ⊆{C | ,...,C | }.  |     |     | (62) |             |            |       |     |             |         |           |
0 T 1 K theinitialboundaryconditionandinherentlylocksthestateof
anyspanningclustersthatintersectbothboundaries[55].
Lastly,let
|     |     |     |     |     |     |     |     |     | FortheremainingfreeclustersC |     |     |     | k ∈K | T \K 0 ,werandomly |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ---- | ------------------ | --- |
mI (a ) and nI (a ) (63) assignastatea ∈ {0,1}withequalprobability1/2each. If
|                                                  | k   | k   | k   | k   |     |     |     |     |                                             | k         |     |              |     |                 |         |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --------- | --- | ------------ | --- | --------------- | ------- |
|                                                  |     |     |     |     |     |     |     |     | theresultingtotalnumberofinfectednodesatt=T |           |     |              |     |                 | doesnot |
| bethenumbersofinfectednodescontributedbyclusterC |     |     |     |     |     |     |     | in  |                                             |           | I   |              |     |                 |         |
|                                                  |     |     |     |     |     |     |     | k   | meet the                                    | threshold | N   | , we discard | the | entire proposed | as-     |
m in
statea k ∈ {0,1}attimest = 0andT,respectively,withthe signment (a ,...,a ), including the choice of patient zero,
1 K
meann¯I :=[nI(0)+nI(1)]/2. and repeat the process. This guarantees that we sample the
|     | k   |     | k   | k   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
validjointconfigurationsevenly,strictlyobeyingdetailedbal-
ance(9).
A. Conditionallocks Isthisapproachefficient?Tosatisfytheboundarycondition
|                                 |                                                  |                       |                |     |                        |                  |     |     | (cid:80) σ′T ≥NI |      | ,thefreeclustersmustcollectivelyprovideat |     |         |     |      |
| ------------------------------- | ------------------------------------------------ | --------------------- | -------------- | --- | ---------------------- | ---------------- | --- | --- | ---------------- | ---- | ----------------------------------------- | --- | ------- | --- | ---- |
|                                 |                                                  |                       |                |     |                        |                  |     |     | i i              | min  |                                           |     |         |     |      |
|                                 | Asimpleapproachtoenforcetheboundaryconditionsare |                       |                |     |                        |                  |     |     | least            |      |                                           |     |         |     |      |
| conditionallocksonfreeclustersC |                                                  |                       |                |     | ∈K                     | thatintersectt=0 |     |     |                  |      |                                           |     |         |     |      |
|                                 |                                                  |                       |                |     | k                      | 0                |     |     |                  |      | (cid:0)                                   |     | (cid:1) |     |      |
| andthoseC                       |                                                  | ∈K                    | thatintersectt |     | =T.                    |                  |     |     | ∆NI              | =max | 0,NI                                      | −NI |         |     | (64) |
|                                 |                                                  | k                     | T              |     |                        |                  |     |     |                  |      | min                                       |     | locked  |     |      |
|                                 | Fort                                             | = 0,therearetwocases: |                |     | Eitheronlyonenodeisin- |                  |     |     |                  |      |                                           |     |         |     |      |
(cid:80)
fected (patient zero) in σ, or multiple nodes are infected. In infected nodes. If the ratio ∆r := ∆NI/ n¯I is small,
k k
thefirstcase,fortheclusterupdate,wefreezethet=0states the random assignment of the states a will succeed with
k
ofallsusceptiblenodesexceptforthenearestneighborsofpa- highprobability. Thisfollowsfromtheconcentrationofmea-
tientzero. Inthesecondcase,wefreezeallsusceptiblenodes. sure phenomenon and, in particular, Hoeffding’s inequality

13
[56, 57]. The smallness of ∆r depends on several parame- ticesonintervalswherethestateisconstantthroughaPoisson
ters, e.g., NI /N, the recovery rates γ , the insertion rates point process as discussed in Sec. IVD. The computational
min i
of the single-node graph vertices, the insertion rates of edge costgenerallyis
verticesthatcanaddinfections,andthenodedegrees.
Note that this approach would usually fail when using the O(N +M )=O (cid:0)(cid:82)T dtΓt(cid:1) , (65)
σ g,σ 0
edge vertex set E1 in simulations of SIS models. Upstream
lockavalancheswouldtendtofreezepatientzeroasdiscussed whereΓtisthetotaluniformizationrateΓt[Eq.(5a)].
inSec.VC.Thegraphverticesg x swap,g x a↑+,andg x a↓+ ofedge Translating the generated graph g into spacetime clusters
vertexsetE2resolvethisissue;seeSec.VD. C requires applying the union-find (disjoint-set) algorithm
k
across the trajectory as discussed in Sec. IVE. When using
path compression (flattening the cluster tree every time we
C. Dynamicprogramming search for a root) and union-by-rank (always attaching the
smallerclustertreetotherootofthelargertree),thecomputa-
If ∆NI is substantially larger than (cid:80) n¯I, the fraction of tionalcomplexityscalesalmostlinearlywiththetotalnumber
k k
validconfigurationsoutofthe2K totalpossibilitiesbecomes ofgraphvertices(65).
vanishinglysmallsuchthatsurpassing∆NIhaslowprobabil- Enforcing macroscopic constraints without path rejection
ity,andcluster-levelrejectionwillstall. introduces a small overhead. For instance, enforcing the
Instead, we can exactly sample the valid combinations in boundary condition of N m I in infected nodes at time t = T
O(KN ) time, where N is the total number of nodes usingdynamicprogrammingrequiresbuildingthecombinato-
free free
contained in the free clusters at time T: Build a K × rialtableZ k (m,n)describedinSec.VIandAppendixC.This
2 × N free dynamic programming table Z (similar to the processoperatesinO(KN free )time, whereK isthenumber
Knapsack/subset-sum problems [58, 59]), where Z k (m,n) of free clusters intersecting the final time t = T and N free is
with m ∈ {0,1} counts the number of valid state combina- the total number of nodes contained within those clusters at
tions (a ,...,a ) for clusters C ,...,C that result in ex- timeT.
1 k 1 k
actly m = (cid:80)k mI (a ) infected nodes at t = 0 and
k′=1 k′ k′ Example5. ConsidersimulatinganSISmodelwithrecovery
n= (cid:80)k nI (a )infectednodesatt=T inthoseclusters.
k′=1 k′ k′ rates γ i and infection rates α i,j using the single-node ver-
Oncethetableisbuilt,doasinglebackwardpass,probabilis-
tex set S1 and edge-vertex set E2 from Sec. V. According
tically assign the cluster-C state a ∈ {0,1} based on the
K K to Eqs. (5a) and (65) the time complexity per cluster update
exactcombinatorialweightoftheremainingpathsthatreach
scalesas
thethreshold∆NIandonepatientzero. Thenmovetoa ,
K−1
andsoon. DetailsareprovidedinAppendixC. O (cid:0)(cid:82)T dtΓt(cid:1) =O (cid:0) T (cid:80) γ (cid:1) +O (cid:0) T (cid:80) α (cid:1) . (66)
0 i i i,j i,j
Autocorrelation times are much more difficult to predict
D. Initialization andgenerallydependonnetworkstructure,thedistributionof
eventrates,aswellasthespecifictrajectoryconstraintC(σ).
ToinitializeaCPMCsimulationwithasinglepatient-zero They can also crucially depend on the chosen sets of graph
andoutbreak-sizethresholdNI ,assumingaconnectednet- vertices and associated vertex rates. As discussed for SIS
min
work, we can start from a trajectory σ[1], where a random modelsinSecs.VCandVD,wecertainlywanttoavoidany
nodeisinfectedfortheentiretimeintervalt ∈ [0,T]andall (upstreamanddownstream)lockavalanchesthatleadtosmall
other nodes are susceptible. Starting with n = 1, we iterate numbersoffreeclusters. Loweringthecomputationcostper
thefollowing: Giventhecurrenttrajectoryσ[n],doacluster cluster update can increase autocorrelation times in the path
updatewithoutbreakthresholdN˜I =1+ (cid:80) σT[n]togen- Markov chain (8) and increase the net computation time to
min i i
erateatrajectoryσ[n+1]withatleastoneadditionalinfected generate trajectories that are (approximately) statistically in-
nodeattimeT. Continuethisprocessuntilreachingatrajec- dependent.
tory σ[n + 1] that surpasses the desired infection threshold
NI . This trajectory σ[n+1] can then be used as the first
min
sampleintheactualCPMCMarkovchain(8). VIII. PARALLELIZATIONSTRATEGIES
ToscaleCPMCformassivenetworks,thealgorithmcanbe
VII. COMPUTATIONCOSTS parallelizedinmultipleways:
IndependentMarkovchains(trivialparallelization).–Be-
ThecomputationalefficiencyofCPMCdependsonthetime causeCPMCgeneratesaMarkovchainoffull-systemtrajec-
complexityofasingleclusterupdateσ[n] → g → σ[n+1] tories, multiple statistically independent runs can be trivially
(Sec. IV) and autocorrelations in the resulting path Markov distributed across separate CPU cores. The results of the in-
chain(8). dependent Markov chains can be concatenated to reduce the
Generating the intermediate graph g involves processing statistical variance of the sampled observables. A limitation
theN physicaleventsandinsertingM backgroundver- inthisrespectisthateveryMarkovchainrequiresawarm-up
σ g,σ

14
phase (a.k.a. burn-in period). With the latter typically com- 0.5 p0 p2 p3
| prising20%to40%ofthegeneratedsamples[60],thepossi- |     |     |     |     |     |     |     |     |     |     | p1  | p2  | p4  |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
blegainsarelimited.
0.4
| Temporal                                              | decomposition |           |        | for graph     | generation. |               | – The   |                 |     |     |     |     |     |     |     |
| ----------------------------------------------------- | ------------- | --------- | ------ | ------------- | ----------- | ------------- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| graph generation                                      |               | can be    | easily | parallelized. | For         | the           | assign- |                 |     |     |     |     |     |     |     |
| mentofgraphverticestothestate-changingeventsinthecur- |               |           |        |               |             |               |         | ytilibaborp 0.3 |     |     |     |     |     |     |     |
| rent trajectory                                       |               | σ, we can | simply | assign        | equal-sized |               | groups  |                 |     |     |     |     |     |     |     |
| of vertices                                           | to every      | thread.   | For    | the insertion |             | of background |         |                 |     |     |     |     |     |     |     |
0.2
graph vertices, we can divide the time axis [0,T] into non- exact
CPMC
| overlapping | equal-sized |            | intervals. | Different | threads  |     | can in-   |     |     |     |     |     |     |     |     |
| ----------- | ----------- | ---------- | ---------- | --------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| dependently | generate    | background |            | graph     | vertices | g   | for their | 0.1 |     |     |     |     |     |     |     |
y
assignedtimewindows.
| Concurrent |     | union-find | data | structures. | –   | While | a stan- | 0.0 |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ---- | ----------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
dardunion-findalgorithmisinherentlysequential,concurrent 0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
lock-freedisjoint-setdatastructurescanbeimplemented[61– time t
i ∈ {1,...,N}
| 63]. By                                             | distributing | the        | nodes    |                   |                      | across   | par- |                                               |                |     |                                        |     |     |         |       |
| --------------------------------------------------- | ------------ | ---------- | -------- | ----------------- | -------------------- | -------- | ---- | --------------------------------------------- | -------------- | --- | -------------------------------------- | --- | --- | ------- | ----- |
|                                                     |              |            |          |                   |                      |          |      | FIG.4.Homogeneousfour-nodeSISringnetworkwithγ |                |     |                                        |     |     |         | =1and |
| allel threads,                                      | the          | initial    | sequence | of constant-state |                      | segments |      |                                               |                |     |                                        |     |     |         |       |
|                                                     |              |            |          |                   |                      |          |      | α = 3:                                        | Probabilitiesp |     | i (t)forfindingthesysteminmacrostatess |     |     |         | i     |
| and independent                                     |              | tree roots | can      | be generated      | simultaneously.      |          |      |                                               |                |     |                                        |     |     |         |       |
|                                                     |              |            |          |                   |                      |          |      | [Eq.(67)]attimet,whenstartinginoneofthefours  |                |     |                                        |     |     | states. |       |
| Threadscanthensafelyexecuteatomic“compare-and-swap” |              |            |          |                   |                      |          |      |                                               |                |     |                                        |     |     | 1       |       |
| unificationsfortheedgeverticesg                     |              |            |          |                   | toacceleratetheclus- |          |      |                                               |                |     |                                        |     |     |         |       |
(t,i,j)
teridentification. • From s : Recovers to s (rate γ). Infects an adjacent
|          |           |     |          |            |     |           |      |                  | 1   |     |           | 0   |     |     |     |
| -------- | --------- | --- | -------- | ---------- | --- | --------- | ---- | ---------------- | --- | --- | --------- | --- | --- | --- | --- |
| Parallel | tempering |     | (replica | exchange). | –   | For large | net- |                  |     |     |           |     |     |     |     |
|          |           |     |          |            |     |           |      | neighbortoreachs |     |     | (rate2α). |     |     |     |     |
2
workswithrigidtopologicalconstraints,wecanemploypar-
allel tempering, simulating multiple, coupled Markov chains • From s 2 : Recovers to s 1 (rate 2γ). Infects a susceptible
running simultaneously on separate processors [54]. Au- nodetoreachs (rate2α).
3
| tocorrelation                                           | times | can | be reduced | by  | swapping | configura- |     |         |              |     |     |                               |     |     |     |
| ------------------------------------------------------- | ----- | --- | ---------- | --- | -------- | ---------- | --- | ------- | ------------ | --- | --- | ----------------------------- | --- | --- | --- |
|                                                         |       |     |            |     |          |            |     | • Froms | :Recoverstos |     |     | (rate2γ).Bothsusceptiblenodes |     |     |     |
| tionsbetweenchainsrunningatdifferentstructuralparameter |       |     |            |     |          |            |     |         | ˜2           |     | 1   |                               |     |     |     |
areflankedbytwoinfectednodes,yielding4activeedges
regimes,e.g.,varyingthestrictnessofthetrajectoryconstraint
|                           |     |     |     |      |                   |     |     | toreachs |     | (rate4α). |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ---- | ----------------- | --- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- |
| C(σ),modelparameterslikeγ |     |     |     | andα | inSISdynamics,and |     |     |          |     | 3         |     |     |     |     |     |
i i,j
tuningalgorithmicparameterslikeψandϕforthevertexrates • From s : Recovers an “end” node to reach s (rate 2γ).
|     |     |     |     |     |     |     |     |     | 3   |     |     |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inedgevertexsetE2ofSec.VD.
|     |     |     |     |     |     |     |     | Recovers             |     | the “middle” | node | to        | reach s ˜2 (rate | γ). | Infects |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------ | ---- | --------- | ---------------- | --- | ------- |
|     |     |     |     |     |     |     |     | thefinalnodetoreachs |     |              |      | (rate2α). |                  |     |         |
4
|                |                                 |     |          |            |     |           |      | • Froms    | 4 :    | Recoverstos | 3         | (rate4γ). |            |              |     |
| -------------- | ------------------------------- | --- | -------- | ---------- | --- | --------- | ---- | ---------- | ------ | ----------- | --------- | --------- | ---------- | ------------ | --- |
| IX.            | VALIDATIONAGAINSTEXACTSOLUTIONS |     |          |            |     |           |      |            |        |             |           |           |            |              |     |
|                |                                 |     |          |            |     |           |      | This       | yields | the         | following | system    | of coupled | differential |     |
| To demonstrate |                                 | and | validate | the method |     | for large | out- | equations: |        |             |           |           |            |              |     |
breaksonbigSISnetworks,simulationresultsofCPMCand
the Gillespie method are compared in Ref. [42] for regimes, ∂ p =γp (68a)
|     |     |     |     |     |     |     |     | t   | 0   | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where the rejection rate of the Gillespie method (due to the ∂ p =−(2α+γ)p +2γp +2γp (68b)
|     |     |     |     |     |     |     |     | t   | 1   |     | 1   | 2   | ˜2  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
outbreak-sizeconstraint)ishighbutstillmanageable.
|     |     |     |     |     |     |     |     | ∂   | p =2αp | −(2α+2γ)p |     | +2γp |     |     | (68c) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ---- | --- | --- | ----- |
|     |     |     |     |     |     |     |     | t   | 2      | 1         |     | 2    | 3   |     |       |
HerewevalidateCPMCbycomparingtotheexactsolution
|     |     |     |     |     |     |     |     | ∂   | p =−(4α+2γ)p |     | +γp |     |     |     | (68d) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ----- |
ofthemasterequationfortwosmallfour-nodeSISnetworks. t ˜2 ˜2 3
Four-node ring. – For a homogeneous ring network of ∂ t p 3 =2αp 2 +4αp ˜2 −(2α+3γ)p 3 +4γp 4 (68e)
N = 4 nodes, the cyclic translation invariance allows us ∂ t p 4 =2αp 3 −4γp 4 (68f)
| to reduce       | the 24 | = 16 | distinct        | microstates |     | down | to the 6 |                                          |            |     |          |               |     |     |      |
| --------------- | ------ | ---- | --------------- | ----------- | --- | ---- | -------- | ---------------------------------------- | ---------- | --- | -------- | ------------- | --- | --- | ---- |
| macrostates     |        |      |                 |             |     |      |          | whichcanbewrittenandsolvedinmatrixformas |            |     |          |               |     |     |      |
|                 |        |      |                 |             |     |      |          | ∂                                        | p(t)=Ap(t) |     | suchthat | p(t)=eAtp(0). |     |     | (69) |
| s 0 =(0,0,0,0), |        |      | s 1 =(1,0,0,0), |             |     |      | (67a)    | t                                        |            |     |          |               |     |     |      |
s 2 =(1,1,0,0), s ˜2 =(1,0,1,0), (67b) Choosingγ =1,α=3,ands astheinitialstate,thedatain
1
| s =(1,1,1,0), |     |     | s =(1,1,1,1), |     |     |     |       |                                                  |     |     |     |     |     |     |     |
| ------------- | --- | --- | ------------- | --- | --- | --- | ----- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| 3             |     |     | 4             |     |     |     | (67c) | Fig.4showexcellentagreementbetweentheCPMCsimula- |     |     |     |     |     |     |     |
tionandtheexactsolution.
which are representatives for the 1, 4, 4, 2, 4, 1 microstates Four-node diamond. – This network comprises two hub
thattheyarerelatedtobytranslations.
|     |     |     |     |     |     |     |     | nodesi | = 1,2thatareconnectedtoallothernodes,andtwo |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
Let p (t) denote the probability of the system being in leaf nodes i = 3,4 which are connected to the hubs but not
i
macrostate s at time t. By analyzing the number of active directlytoeachother. Wechooseallinfectionratesonedges
i
edges and possible recovery events for each macrostate, we andrecoveryratesonnodestobeequal(αandγ). Allconfig-
obtainthefollowingtransitionrates: urationswiththesamenumbersn h ,n ℓ ∈{0,1,2}ofinfected

15
0.5
0.4
0.3
0.2
0.1
0.0
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
time t
ytilibaborp
p0,0 p0,1 p1,1 p2,1 p2,2 (n h ,n ℓ ) = (1,0) as the initial state, the data in Fig. 5 show
p1,0 p2,0 p0,2 p1,2 excellent agreement between the CPMC simulation and the
exactsolution.
Note that, in these validation numerics, we have not im-
exact posed any constraint on the final state to simplify the exact
CPMC solution.
X. DISCUSSION
Inthismanuscript,wehaveestablishedtherigorousmath-
ematical foundations and the algorithmic framework for
conditional-path Monte Carlo (CPMC), complementing the
broaderintroductionofthemethodinRef.[42].
Theindividual-basedsimulationofraremacroscopicevents
FIG.5. Four-nodediamondSISnetworkwithtwohubnodesand in stochastic dynamics on large networks represents a con-
two leaf nodes, γ = 1 and α = 5/2: Probabilities p (t) for siderable challenge. As outlined in Sec. I, techniques like
nh,nℓ
findingthesystemwith(n ,n )infectednodeshubandleafnodes the traditional SSA [18], wSSA [20, 21], splitting methods
h ℓ
attimet,whenstartinginan(n h ,n ℓ )=(1,0)state. [25,28,30,31],andTPS[38–40]routinelysuccumbtocatas-
trophicrejectionrates,kinetictrapping,pathdegeneracy,crit-
ical slowing down, or genealogical correlations when faced
hubandleafnodesaredynamicallyequivalent.Thisrestricted with large heterogeneous networks, rigid topological bottle-
permutation symmetry allows us to reduce the 24 = 16 dis- necks, orcomplexboundaryconditions. TheCPMCmethod
tinctmicrostatesdownto3·3 = 9macrostateswhichevolve aims to circumvent these structural vulnerabilities by aban-
asfollows: doningforward-timeintegrationandlocaltrajectoryupdates.
Instead,CPMCemploysclusterupdatesthatmapagivenfull-
• Hubrecovery(n →n −1): Therateisn γ.
h h h system trajectory to an intermediate graph configuration, de-
• Leafrecovery(n →n −1): Rateisn γ. composing spacetime into non-local clusters, which are then
ℓ ℓ ℓ
updatedthrough(largelyindependent)cluster-stateflipping.
• Hub infection (n h → n h + 1): A susceptible hub is Methodological advances. – The core theoretical contri-
connected to the other hub and both leaves. If the other bution is the formulation of the joint path-graph probability
hub is infected, it contributes α. Each infected leaf con- weights and the derivation of the local transition and uni-
tributesα. Thetotalrateforthe2−n h susceptiblehubs formization sum rules that guarantee strict detailed balance
is(2−n h )(n h +n ℓ )α. for the trajectory Markov chain. During the construction of
corresponding graph vertex sets for SIS models, we found
• Leafinfection(n → n +1): Asusceptibleleafiscon-
ℓ ℓ that a careless choice can lead to upstream (or downstream)
nected only to the hubs. Each infected hub contributes
lockavalanchesinthegeneratedgraphs,reducingthesizeor
α. The total rate for the 2 − n susceptible leaves is
ℓ number of flippable clusters and demobilizing the epidemic
(2−n )n α.
ℓ h trunk. Thiscanleadtoconsiderableautocorrelations. Bysys-
Using these macroscopic rates, the master equations gov- tematically constructing and optimizing the edge vertex sets
erningtheprobabilityp = p (t)offindingthesys- (fromE1toE2andE3),wedemonstratedhowspecificgraph
nh,nℓ nh,nℓ
temwith(n ,n )infectednodesattimetare vertices such as the swap and asymmetry-nullifying vertices
h ℓ
(gswap, g10, and g01) can completely unlock trajectory mo-
x x x
∂ t p 0,0 =γp 1,0 +γp 0,1 , bility, ensuring ergodicity and accommodating highly asym-
∂ p =−(3α+γ)p +2γp +γp , metric infection rates without sacrificing computational effi-
t 1,0 1,0 2,0 1,1
ciency.
∂ p =−(2α+γ)p +γp +2γp ,
t 0,1 0,1 1,1 0,2
Importantly, CPMC resolves the severe inefficiencies of
∂ p =αp −(4α+2γ)p +γp ,
t 2,0 1,0 2,0 2,1 SSA-basedtechniquesassociatedwithmacroscopictrajectory
∂ t p 1,1 =2αp 1,0 +2αp 0,1 −(3α+2γ)p 1,1 constraints. Enforcingconditionssuchasasinglepatientzero
+2γp +2γp , att = 0alongsidealargeoutbreakthresholdatt = T inSIS
2,1 1,2
modelstypicallydestroystheacceptanceratesofstochastical-
∂ p =−(4α+2γ)p +γp ,
t 0,2 0,2 1,2 gorithms. Byconstructingatruncateddynamicprogramming
∂ p =4αp +2αp −(2α+3γ)p +2γp ,
t 2,1 2,0 1,1 2,1 2,2 table [58, 59] for the free clusters that can affect the macro-
∂ p =αp +4αp −(3α+3γ)p +2γp , scopictrajectoryconstraints,CPMCcanefficientlysamplethe
t 1,2 1,1 0,2 1,2 2,2
∂ p =2αp +3αp −4γp , compatible trajectories without rejection and with exact de-
t 2,2 2,1 1,2 2,2
tailedbalance.
which can again be written and solved in matrix form ac- Generalizability and applications. – While this paper ex-
cording to Eq. (69). Choosing γ = 1, α = 5/2, and clusivelyemployedtheSISmodelforinstructiveclarityinex-

16
amples,theCPMCmethodandthelogicbehindthevertexset selvesappearanddisappeardynamically[65]. Whilethepre-
constructionextendnaturallytogeneralMarkovianstochastic sented general formulation and SIS graph vertex sets are ap-
dynamics. The ability of CPMC to bypass path degeneracy plicableforthesecases,theinsertionprocessforbackground
and mutate non-local spacetime clusters makes it exception- vertices will become more complex, and details for an effi-
ally well-suited for a wide array of complex systems where cientimplementationneedtobeworkedout.Finally,whilewe
rarecombinationsoflocalprocessestriggermassivesystemic havederivedthesolutionspaceforvertexratesinsuitableSIS
shifts. Beyond epidemiology, this framework holds imme- graph vertex sets (e.g., the parameters ψ,ϕ, and q in the E2
diate potential for sampling the rare transition pathways of andE3edgesets),theidentificationof(model-dependent)pa-
nucleation in kinetic spin models [2, 3] and overcoming the rameter choices that minimize autocorrelation times remains
severe kinetic trapping inherent to the space-time thermody- anopenoptimizationproblem. CombiningCPMCwithparal-
namics of glassy systems [4, 5]. CPMC can be used to ana- lel tempering [54] and adaptive machine learning algorithms
lyze cascading failures in IT and financial networks [9, 10], to actively tune vertex rates during the burn-in phase could
targeted lateral malware propagation [64], and rapid shifts furtherpushtheboundariesofrare-eventsimulationformas-
in societal opinions [11, 12]. In these highly heterogeneous sive,real-worldnetworks.
systems,macroscopicmetricsareofteninsufficientforanin-
| depth | investigation, |     | understanding, |     | and | control | of the com- |     |     |     |     |     |     |     |
| ----- | -------------- | --- | -------------- | --- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ACKNOWLEDGMENTS
| plex | dynamics. |     | CPMC | enables | an efficient | individual-based |     |     |     |     |     |     |     |     |
| ---- | --------- | --- | ---- | ------- | ------------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
simulationandriskfactoranalysisforimportantrareevents.
|     |     |     |     |     |     |     |     |     | We  | gratefully | acknowledge | discussions | with Caterina | de  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------- | ------------- | --- |
Future directions. – Several avenues for future method- Bacco,YunaJang,JianfengLu,JamesMoody,CharlesNunn,
ologicaldevelopmentsremain. First, adaptingthegraphver- JoshuaSocolar,andparticipantsoftheinternationalworkshop
texsetstoothercanonicalepidemiologicalmodels,suchasthe “Quantitative Methods for Dynamics on Networks” 2024 in
susceptible-infected-recovered (SIR) or susceptible-exposed- LosAlamos(organizedbytheCNLSatLosAlamosNational
infected-recovered(SEIR)models[6],willinvolveabsorbing Laboratory), aswellassupportbytheU.S.NationalScience
statesand non-reversiblenode transitions. Second, it willbe Foundationthroughgrantno.DMS-2344576andbytheDuke
interesting to apply CPMC to systems with time-dependent PopulationResearchCenter(DPRC)throughtheU.S.NICHD
eventratesandtotemporalnetworks,wheretheedgesthem- grantno.P2C-HD0065563.
AppendixA:Proofofthejoint-weightmarginalizationcondition
(cid:80)′
In this appendix, we shall prove the marginalization condition P(σ) = J(σ,g) [Eq. (15)], stating that the path
g∋σ
probabilitydensityP(σ)[Eq.(4)]isrecoveredwhensummingthejointpath-graphweightsJ(σ,g)[Eq.(12)]overallgraphs
(cid:80)′
| gcompatiblewithσ,wherethe“sum” |     |     |     |     |     | isactuallythepathintegral(16). |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
g∋σ
|     |     |     |     | (cid:81) |     |     |     |     |     |     | (cid:81) |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
Letussplittheproduct ν z (g z )∆(σ z ,g z )fromEq.(12)intotheproduct ν x (g x )∆(σ x ,g x )overthelocations{x}
|     |     |     |     | z∈g |     |     | (cid:81) |     |     |     | x∈σ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ofallN = N physicalverticesandtheproduct ν (g )∆(σ ,g )overthelocations{y}ofallM = M background
|     |     | σ   |     |     |     |     | y y | y   | y y |     |     |     | g,σ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
verticeswithrespecttotrajectoryσ. Applyingthetransitionsumrule(17a)forthegraphvertexratesν inthephysical-vertex
product,wehave
|     | (cid:88)     | (cid:89) |      |      | (17a)  | (cid:89) |     |     |     |     |     |     |     |      |
| --- | ------------ | -------- | ---- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |              |          | ν (g | )∆(σ | ,g ) = | ω (σ     | ).  |     |     |     |     |     |     | (A1) |
|     |              |          | x x  | x    | x      | x        | x   |     |     |     |     |     |     |      |
|     | gx1 ,...,gxN | x∈σ      |      |      |        | x∈σ      |     |     |     |     |     |     |     |      |
Underthepathintegral,thebackground-vertexproductevaluatesto
|     | ∞        |            |          |     |          |          |          | M        |     |         |       |     |     |     |
| --- | -------- | ---------- | -------- | --- | -------- | -------- | -------- | -------- | --- | ------- | ----- | --- | --- | --- |
|     | (cid:88) | 1 (cid:90) | T        |     | (cid:88) | (cid:88) | (cid:88) | (cid:89) |     |         |       |     |     |     |
|     |          |            | dt ...dt |     |          |          | ···      |          | ν   | (g )∆(σ | ,g )  |     |     |     |
|     |          |            | 1        | M   |          |          |          |          | ym  | ym      | ym ym |     |     |     |
M!
|     | M=0 | 0   |                    |     | y1,...,yM | t1      |         | tM m=1 |                    |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --------- | ------- | ------- | ------ | ------------------ | --- | --- | --- | --- | --- |
|     |     |     |                    |     |           | gy1 ∈Gy | gyM ∈Gy |        |                    |     |     |     |     |     |
|     |     |     |                    |     |           | 1       |         | M      |                    |     |     |     |     |     |
|     | ∞   |     | (cid:16)(cid:90) T |     |           |         |         |        | (cid:16)(cid:90) T |     |     |     |     |     |
(cid:88) 1 (cid:88) (cid:88) (cid:17)M (cid:88) (cid:88) (cid:17)
|     | =   |                    | dt  |         | ν (g | )∆(σ | ,g ) | =exp             |     | dt  | ν (g )∆(σ | ,g ) |     |     |
| --- | --- | ------------------ | --- | ------- | ---- | ---- | ---- | ---------------- | --- | --- | --------- | ---- | --- | --- |
|     |     | M!                 |     |         | y    | y y  | y    |                  |     |     | y y       | y y  |     |     |
|     |     |                    | 0   |         |      |      |      |                  | 0   |     |           |      |     |     |
|     | M=0 |                    |     | y gy∈Gy |      |      |      |                  |     | y   | gy∈Gy     |      |     |     |
|     |     | (cid:16)(cid:90) T |     |         |      |      |      | (cid:16)(cid:90) | T   |     |           |      |     |     |
(cid:88) (cid:88) (cid:17) (1 7b) (cid:88)(cid:2) (cid:3)(cid:17) (cid:82) Tdt[Γt−Λt(σt)].
|     | =exp |     | dt  | ν     | (g )∆(σ | const,g | ) = | exp | dt  | Γ   | −Λ (σ t) | =e  |     | (A2) |
| --- | ---- | --- | --- | ----- | ------- | ------- | --- | --- | --- | --- | -------- | --- | --- | ---- |
|     |      |     |     |       | y y     | y       | y   |     |     |     | y y y    | 0   |     |      |
|     |      | 0   |     |       |         |         |     |     | 0   |     |          |     |     |      |
|     |      |     | y   | gy∈Gy |         |         |     |     |     | y   |          |     |     |      |
Forthesecondline,recallthatG ≡Gt. Inthethirdline,wehavefirstusedthatstate-changingeventshavemeasurezeroonthe
y y
timeinterval[0,T]suchthattheydonotcontributeintheintegralovertandwecanreplacealllocalstatedynamicsσ bythe
y
null-eventσconst[Eq.(13)].
Wehavethenemployedtheuniformizationsumrule(17b).
y

17
Inconjunction,Eqs.(4),(12),(16),(A1),and(A2)provethemarginalizationcondition
|     | (cid:88)′   | (cid:16) | (cid:89) | (cid:17) e−(cid:82) TdtΛt(σt) |        |     |     |      |
| --- | ----------- | -------- | -------- | ----------------------------- | ------ | --- | --- | ---- |
|     | J(σ,g)=C(σ) |          | ω        | (σ )                          | =P(σ). |     |     | (A3) |
|     |             |          | x        | x 0                           |        |     |     |      |
|     | g∋σ         |          | x∈σ      |                               |        |     |     |      |
AppendixB:CompleteedgevertexsetforSISmodels
SectionVDcontainedtheclaimthat
ga↑− =(a,0→a,a), gI↑− =(1,0→1,a), gI↑+ =(1,a→1,1), ga↑+ =(a,a¯→a,1), (B1a)
|      | x           |     | x    |             | x    |             | x            |       |
| ---- | ----------- | --- | ---- | ----------- | ---- | ----------- | ------------ | ----- |
| ga↓− |             |     | gI↓− |             | gI↓+ |             | ga↓+         |       |
|      | =(0,a→a,a), |     |      | =(0,1→a,1), |      | =(a,1→1,1), | =(a¯,a→1,a), | (B1b) |
|      | x           |     | x    |             | x    |             | x            |       |
gswap =(a,a¯→1,1)
|     | x   |     |     |     |     |     |     | (B1c) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
arealledgeverticesthatarecompatiblewithaninfectioneventandfeatureatleastonefreevariablea∈{0,1}witha¯denoting
thenegationofa.
Toprovethis,consideravertexg thatmatchestheinfectionevent(1,0 → 1,1)whenevaluatedata = 1. Thevertexmust
x
evaluatetooneoftheremainingphysicallyvalidedgeeventswhena=0:
| (a) | Mappingto(0,0→0,0)impliesg |     |     | =(a,0→a,a)=ga↑−. |     |     |     |     |
| --- | -------------------------- | --- | --- | ---------------- | --- | --- | --- | --- |
|     |                            |     |     | x                |     | x   |     |     |
=(1,0→1,a)=gI↑−.
| (b) | Mappingto(1,0→1,0)impliesg |     |     | x   |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
x
| (c) | Mappingto(0,1→0,1)impliesg |     |     | =(a,a¯→a,1)=ga↑+. |     |     |     |     |
| --- | -------------------------- | --- | --- | ----------------- | --- | --- | --- | --- |
|     |                            |     |     | x                 |     | x   |     |     |
| (d) | Mappingto(1,1→1,1)impliesg |     |     | =(1,a→1,1)=gI↑+.  |     |     |     |     |
|     |                            |     |     | x                 |     | x   |     |     |
=(a,a¯→1,1)=gswap.
| (e) | Mappingto(0,1→1,1)impliesg |     |     | x   |     | x   |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
Thenconsideringthesecondoption,avertexg thatmatchestheinfectionevent(0,1→1,1)whenevaluatedata=1,wefind
x
theremainingfourverticesga↓−,gI↓−,ga↓+,andgI↓+.
|     |     |     | x   | x x x |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
AppendixC:DynamicprogrammingfortheSIS-modelboundaryconditions
Using the same notations as in Sec. VI, this appendix describes in detail how we can use dynamic programming to exactly
samplestates(a ,...,a )oftheK freeclusterthatsimultaneouslysatisfytheconstraintsatbothboundaries: havingexactly
|                                 |     | 1 K |     |                                 |     |     |     |     |
| ------------------------------- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- |
| onepatientzeroatt=0andatleastNI |     |     |     | infectednodesatthefinaltimet=T. |     |     |     |     |
min
The following dynamic programming approach finds valid states of the free clusters in O(KN ) time and obeys strict
free
detailed balance. It is split into a forward counting phase and a backward sampling phase and expands on the classic
Knapsack/subset-sumalgorithm[58,59]byexplicitlycouplingthetwoboundaryconditionsintoasingletruncatedstatespace.
|     |     |     |     | 1. Forwardpass–Buildingthecombinatorialtable |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
Consideringonlythefirstkclusters,wewanttocountthenumberofvalidwaysZ (m,n)theclusterscanbeassignedstates
k
|     |     |     |     | (cid:80)k mI |     |     | (cid:80)k nI |     |
| --- | --- | --- | --- | ------------ | --- | --- | ------------ | --- |
(a 1 ,...,a k )toachieveexactlym = infectednodesatt = 0andn = infectednodesatt = T. Dueto
|     |     |     |     | k′=1 k′ |     |     | k′=1 k′ |     |
| --- | --- | --- | --- | ------- | --- | --- | ------- | --- |
thepatient-zeroconstraint,weonlyneedtoconsiderm∈{0,1}suchthatZ isaK×2×N combinatorialtable.
free
Toinitializethetable,wesetZ (0,0)=1andZ (m,n)=0foralln>0andm∈{0,1}. Wethenloopthroughthecluster
|     |     |     | 0   | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
numberkfrom1toK and,foreachpossiblepair(m,n),calculatethenumberofvalidcombinations. Thecombinationofsums
(cid:0) (cid:1)
(m,n)canbereachedeitherbysettingthek-thclustertoa =0,inheritingthecombinationsforsums m−mI(0),n−nI(0) ,
|     |     |     |     |     | k   |                         | k       | k   |
| --- | --- | --- | --- | --- | --- | ----------------------- | ------- | --- |
|     |     |     |     |     |     | (cid:0) m−mI(1),n−nI(1) | (cid:1) |     |
orbysettingittoa k =1,inheritingthecombinationsforsums ,i.e.,
|     |     |     |     |     |     | k   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Z (m,n)=Z (cid:0) m−mI(0),n−nI(0) (cid:1) +Z (cid:0) m−mI(1),n−nI(1) (cid:1) , (C1)
|     | k   | k−1 | k   | k   | k−1 | k k |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereZ (m,n)≡0ifm<0orn<0.
k
Bytheendofthispass,Z (m,n)holdstheexactnumberofwaystheentiresetofKfreeclusterscansimultaneouslyproduce
K
exactlyminfectednodesatt=0andninfectednodesatt=T.

18
|     |     |     | 2. Backwardpass–Exactjointsampling |     |     |     |     |
| --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
Let us define a helper function S (m,n) which gives the total number of ways in which the first k clusters C ,...,C can
|     |     | k   |     |     |     |     | 1 k |
| --- | --- | --- | --- | --- | --- | --- | --- |
produceminfectednodesatt=0andatleastninfectednodesatt=0:
N
(cid:88)free
| S (m,n):= | Z (m,n′). |     |     |     |     |     |      |
| --------- | --------- | --- | --- | --- | --- | --- | ---- |
| k         | k         |     |     |     |     |     | (C2) |
n′=n
Now, we choose cluster states in the order a K ,a K−1 ,...,a 1 one by one, sampling each state based on the exact marginal
probabilitythatitleadstoavalidfinaltrajectory. Startingwiththetargetthresholdsn←∆NIandm←1−MI ,weiterate
locked
| backwardfromk | =K downto1: |     |     |     |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- | --- | --- |
• Calculatetheprobabilitiesforthestatesa ∈{0,1}ofclusterC :Forstatea ,clusterC contributesmI(a )nodesatt=0
|     |     |     | k   | k   | k k | k k |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
andnI(a )nodesatt=T. Hence,theremainingk−1clustersonlyneedtoprovide
| k k         |          |         |                 |     |     |     |       |
| ----------- | -------- | ------- | --------------- | --- | --- | --- | ----- |
| m′(a        | (cid:0)  | (cid:1) |                 |     |     |     |       |
| ):=max      | 0,m−mI(a | )       | nodesat t=0 and |     |     |     | (C3a) |
| k           |          | k k     |                 |     |     |     |       |
|             | (cid:0)  | (cid:1) |                 |     |     |     |       |
| n′(a ):=max | 0,n−nI(a | )       | nodesat t=T.    |     |     |     | (C3b) |
| k           |          | k k     |                 |     |     |     |       |
Thecorrespondingprobabilityisexactlythenumberofvalidcombinationswithstatea ,dividedbythetotalnumberofvalid
k
combinationscurrentlyavailable:
|            | (cid:0)     | (cid:1) |     |     |     |     |      |
| ---------- | ----------- | ------- | --- | --- | --- | --- | ---- |
| S          | m′(a ),n′(a | )       |     |     |     |     |      |
| p(a )= k−1 | k           | k .     |     |     |     |     | (C4) |
k
S (m,n)
k
|                   |                      |     | ),andupdatetherequirementsm←m′(a |     | )andn←n′(a |      |     |
| ----------------- | -------------------- | --- | -------------------------------- | --- | ---------- | ---- | --- |
| • Randomlyselecta | k withprobabilityp(a |     | k                                |     | k          | k ). |     |
| • Continuewithk   | ←k−1.                |     |                                  |     |            |      |     |
In this way, every valid configuration (a ,...,a ) satisfying both boundary conditions is chosen with equal probability and
|     |     |     | 1 K |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
zerorejections.
|     |     |     |     |     |     | (cid:0) | (cid:1) |
| --- | --- | --- | --- | --- | --- | ------- | ------- |
Asaminoroptimization,wecouldtakeintoaccountthatclusterC necessarilycontributesatleastmin nI(0),nI(1) infected
|     |     |     |     | k   |              | k        | k        |
| --- | --- | --- | --- | --- | ------------ | -------- | -------- |
|     |     |     |     |     | N˜ (cid:80)K | (cid:12) | (cid:12) |
nodes at t = T and that we can increase the number of infected nodes at most by := (cid:12)nI (1)−nI (0) (cid:12) from the
|     |     |     |     |     | free | k=1 k | k   |
| --- | --- | --- | --- | --- | ---- | ----- | --- |
Thisreducesthen-dimensionofthecombinatorialtabletoN˜
| correspondingbaseline. |     |     |     |     | free . |     |     |
| ---------------------- | --- | --- | --- | --- | ------ | --- | --- |
[1] P.Hänggi,P.Talkner,andM.Borkovec,Reaction-ratetheory:FiftyyearsafterKramers,Rev.Mod.Phys.62,251(1990).
[2] K.Binder,Theoryoffirst-orderphasetransitions,Rep.Prog.Phys.50,783(1987).
[3] P.A.Rikvold,H.Tomita,S.Miyashita,andS.W.Sides,MetastablelifetimesinakineticIsingmodel: Dependenceonfieldandsystem
size,Phys.Rev.E49,5080(1994).
[4] J. P. Garrahan, R. L. Jack, V. Lecomte, E. Pitard, K. van Duijvendijk, and F. van Wijland, Dynamical first-order phase transition in
kineticallyconstrainedmodelsofglasses,Phys.Rev.Lett.98,195702(2007).
[5] D.ChandlerandJ.P.Garrahan,Dynamicsonthewaytoformingglass:Bubblesinspace-time,Annu.Rev.Phys.Chem.61,191(2010).
R.Pastor-Satorras,C.Castellano,P.VanMieghem,andA.Vespignani,Epidemicprocessesincomplexnetworks,Rev.Mod.Phys.87,
[6]
925(2015).
[7] J.O.Lloyd-Smith,S.J.Schreiber,P.E.Kopp,andW.M.Getz,Superspreadingandtheeffectofindividualvariationondiseaseemer-
gence,Nature438,355(2005).
[8] M.SalathéandJ.H.Jones,Dynamicsandcontrolofdiseasesinnetworkswithcommunitystructure,PLoSComput.Biol.6,e1000736
(2010).
[9] R.Albert,H.Jeong,andA.-L.Barabási,Errorandattacktoleranceofcomplexnetworks,Nature406,378(2000).
[10] D.Acemoglu,A.Ozdaglar,andA.Tahbaz-Salehi,Systemicriskandstabilityinfinancialnetworks,Am.Econ.Rev.105,564(2015).
[11] C.Castellano,S.Fortunato,andV.Loreto,Statisticalphysicsofsocialdynamics,Rev.Mod.Phys.81,591(2009).
[12] D.J.Watts,Asimplemodelofglobalcascadesonrandomnetworks,Proc.Natl.Acad.Sci.U.S.A.99,5766(2002).
[13] H.W.Hethcote,Threebasicepidemiologicalmodels,inAppliedMathematicalEcology(Springer,Heidelberg,1989),pp.119–144.
H.W.Hethcote,Themathematicsofinfectiousdiseases,SIAMRev.42,599(2000).
[14]
[15] F.Brauer,Mathematicalepidemiology:Past,present,andfuture,Infect.Dis.Model.2,113(2017).
[16] K.Rock,S.Brand,J.Moir,andM.J.Keeling,Dynamicsofinfectiousdiseases,Rep.Prog.Phys.77,026602(2014).
[17] F.Brauer,C.Castillo-Chavez,andZ.Feng,MathematicalModelsinEpidemiology(Springer,NewYork,2019).
[18] D.T.Gillespie,Exactstochasticsimulationofcoupledchemicalreactions,J.Phys.Chem.81,2340(1977).

19
[19] A.Bortz,M.Kalos,andJ.Lebowitz,AnewalgorithmforMonteCarlosimulationofIsingspinsystems,J.Comput.Phys.17,10(1975).
[20] H.KuwaharaandI.Mura,Anefficientandexactstochasticsimulationmethodtoanalyzerareeventsinbiochemicalsystems,J.Chem.
Phys.129,165101(2008).
[21] D.T.Gillespie,M.Roh,andL.R.Petzold,Refiningtheweightedstochasticsimulationalgorithm,J.Chem.Phys.130,174103(2009).
[22] Imaginedensecommunitiesconnectedbyonlyafewbridgingedgesandnodes.Foranepidemictogrowfromalocalizedoutbreakina
smallcommunityintoamassive,system-wideepidemic,theinfectionmustcrossthenetworkbridges.Ifthetransmissionrateacrossthe
bridgesarelow,theybecomerigidtopologicalbottlenecks.Forward-timealgorithmslikewSSA,FFS,andWEareblindtothefuture.
EvenifwSSAartificiallybiasestheratestoencouragemoreinfections,thealgorithmstillhastogenerateprecarioussequencesofevents,
whereinfectionsreachbridgesandcrossthem.
[23] R.J.Allen,D.Frenkel,andP.R.tenWolde,Simulatingrareeventsinequilibriumornonequilibriumstochasticsystems,J.Chem.Phys.
124,024102(2006).
[24] R.J.Allen,D.Frenkel,andP.R.tenWolde,Forwardfluxsampling-typeschemesforsimulatingrareevents:Efficiencyanalysis,J.Chem.
Phys.124,194111(2006).
[25] R.J.Allen,C.Valeriani,andP.ReintenWolde,Forwardfluxsamplingforrareeventsimulations,J.Phys.:Condens.Matter21,463102
(2009).
[26] M.Villén-AltamiranoandJ.Villén-Altamirano,RESTART:Amethodforacceleratingrareeventsimulations,inQueueing,Performance
andControlinATM–13thInternationalTeletrafficCongress(North-Holland,Amsterdam,TheNetherlands,1991),Vol.15,pp.71–76.
[27] M.Villén-AltamiranoandJ.Villén-Altamirano,RESTART:Astraightforwardmethodforfastsimulationofrareevents,inProceedings
ofWinterSimulationConference(SocietyforComputerSimulationInternational,SanDiego,CA,1994),pp.282–289.
[28] M.Villén-AltamiranoandJ.Villén-Altamirano, AnalysisofRESTARTsimulation: Theoreticalbasisandsensitivitystudy, Eur.Trans.
Telecommun.13,373(2002).
[29] FFS and RESTART both rely on defining an order parameter λ or importance function and place a series of increasing thresholds or
interfacesbetweentheinitialstateandtheraretargetstate.Theyweredevelopedindifferentacademicfields–RESTARTintelecommu-
nications/queuingtheoryandFFSinstatisticalmechanics–andusedistinctschemesforthebranchingandterminationoftrajectories.
Toproceedfromthresholdtothreshold,FFSusesSSAtoevolvenumerousstoredtrialtrajectoriesfromλandtracksthefractionofthese
trajectoriesthatreachthenextinterfaceλ .Inthisway,oneobtainstransitionprobabilitiesP(λ |λ )andtrialtrajectoriesatλ .
n+1 n+1 n n+1
Ifλisadiscretevariable,likethenumberofinfectednodes,somemodificationsarenecessary.InRESTART,trajectoriesevolvewith
SSAandbranchintor cloneswhencrossingλ .Ifaclonelaterfallsagainbelowλ ,itisterminated.
n n n
[30] D. M. Zuckerman and L. T. Chong, Weighted ensemble simulation: Review of methodology, applications, and software, Annu. Rev.
Biophys.46,43(2017).
[31] D.Aristoff,Analysisandoptimizationofweightedensemblesampling,ESAIM:Math.Model.Numer.Anal.52,1219(2018).
[32] G.HuberandS.Kim,Weighted-ensembleBrowniandynamicssimulationsforproteinassociationreactions,Biophys.J.70,97(1996).
[33] A.Rojnuckarin,S.Kim,andS.Subramaniam,Browniandynamicssimulationsofproteinfolding:Accesstomillisecondstimescaleand
beyond,Proc.Natl.Acad.Sci.U.S.A.95,4288(1998).
[34] B.W.Zhang,D.Jasnow,andD.M.Zuckerman,The“weightedensemble”pathsamplingmethodisstatisticallyexactforabroadclass
ofstochasticprocessesandbinningprocedures,J.Chem.Phys.132,054107(2010).
[35] R.M.Donovan,A.J.Sedgewick,J.R.Faeder,andD.M.Zuckerman,Efficientstochasticsimulationofchemicalkineticsnetworksusing
aweightedensembleoftrajectories,J.Chem.Phys.139,(2013).
[36] C.Dellago,P.G.Bolhuis,F.S.Csajka,andD.Chandler,Transitionpathsamplingandthecalculationofrateconstants,J.Chem.Phys.
108,1964(1998).
[37] C.Dellago,P.G.Bolhuis,andD.Chandler,Efficienttransitionpathsampling: ApplicationtoLennard-Jonesclusterrearrangements,J.
Chem.Phys.108,9236(1998).
[38] P.G.Bolhuis,D.Chandler,C.Dellago,andP.L.Geissler,Transitionpathsampling:Throwingropesoverroughmountainpasses,inthe
dark,Annu.Rev.Phys.Chem.53,291(2002).
[39] C.Dellago,P.G.Bolhuis,andP.L.Geissler,Transitionpathsampling,inAdvancesinChemicalPhysics(JohnWiley&Sons,NewYork,
NY,2002),Chap.1,pp.1–78.
[40] P.G.BolhuisandD.W.H.Swenson,TransitionpathsamplingasMarkovchainMonteCarlooftrajectories:Recentalgorithms,software,
applications,andfutureoutlook,Adv.TheorySimul.4,2000237(2021).
[41] ThetypicalprocedureinTPSistostartwithaninitial(oftenartificiallyconstructedorhigh-energy)trajectoryconnectingat = 0state
ofclassAtot = T stateofclassB.Intheshootingmove,oneselectsarandomtimeslicetalongthepath,perturbsthemicroscopic
momenta(orvariables)slightly,andintegratestheequationsofmotionforwardandbackwardintimetogenerateanewtrialtrajectory.If
thenewtrialpathsuccessfullyconnectsanAstatetoaBstate,itisacceptedorrejectedbasedonaMetropoliscriterionthatguarantees
preservationofthetruepathprobabilitydistribution.
[42] J. Sun, J. Moody, and T. Barthel, Rare-event sampling for stochastic dynamics in network systems using cluster updates,
arXiv:2608.16171(2026).
[43] R.H.SwendsenandJ.-S.Wang,NonuniversalcriticaldynamicsinMonteCarlosimulations,Phys.Rev.Lett.58,86(1987).
[44] R.G.EdwardsandA.D.Sokal, GeneralizationoftheFortuin-Kasteleyn-Swendsen-WangrepresentationandMonteCarloalgorithm,
Phys.Rev.D38,2009(1988).
[45] H.G.Evertz,G.Lana,andM.Marcu,Clusteralgorithmforvertexmodels,Phys.Rev.Lett.70,875(1993).
[46] A.W.Sandvik,Stochasticseriesexpansionmethodwithoperator-loopupdate,Phys.Rev.B59,R14157(R)(1999).
[47] H.G.Evertz,Theloopalgorithm,Adv.Phys.52,1(2003).
[48] W. Krauth, Statistical Mechanics: Algorithms and Computations, Vol. 13 of Oxford Master Series in Statistical, Computational, and
TheoreticalPhysics(OxfordUniversityPress,Oxford,UK,2006).
[49] D. J. Daley and D. Vere-Jones, An Introduction to the Theory of Point Processes, 2nd ed. (Springer, New York, NY, 2003), Vol. I:

20
ElementaryTheoryandMethods.
[50] B.A.GallerandM.J.Fisher,Animprovedequivalencealgorithm,Commun.ACM7,301(1964).
[51] R.E.Tarjan,Efficiencyofagoodbutnotlinearsetunionalgorithm,J.ACM22,215(1975).
[52] R.E.TarjanandJ.vanLeeuwen,Worst-caseanalysisofsetunionalgorithms,J.ACM31,245(1984).
[53] P.Brass,AdvancedDataStructures(CambridgeUniversityPress,NewYork,NY,2008).
[54] J.SunandT.Barthel,inpreparation.
[55] Notethattheprobabilityoffreeclustersthatspantheentiretimeintervalfrom[0,T]decreasesexponentiallyinthefinaltimeT,because
ofthefiniteinsertionrateofbackgroundgraphvertices.
[56] W.Hoeffding,Probabilityinequalitiesforsumsofboundedrandomvariables,J.Am.Stat.Assoc.58,13(1963).
[57] S. Boucheron, G. Lugosi, and P. Massart, Concentration Inequalities: A Nonasymptotic Theory of Independence (Oxford University
Press,Oxford,UK,2013).
[58] S.MartelloandP.Toth,KnapsackProblems:AlgorithmsandComputerImplementations(JohnWiley&Sons,Chichester,UK,1990).
[59] H.Kellerer,U.Pferschy,andD.Pisinger,KnapsackProblems(Springer,Berlin,2004).
[60] A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B. Rubin, Bayesian Data Analysis, 3rd ed. (Chapman and
Hall/CRC,NewYork,USA,2013).
[61] R.J.AndersonandH.Woll,Wait-freeparallelalgorithmsfortheunion-findproblem,inProceedingsoftheTwenty-ThirdAnnualACM
SymposiumonTheoryofComputing,STOC’91(AssociationforComputingMachinery,NewYork,USA,1991),pp.370–380.
[62] D. Alistarh, A. Fedorov, and N. Koval, In search of the fastest concurrent union-find algorithm, in 23rd International Conference on
PrinciplesofDistributedSystems(OPODIS2019),Vol.153ofLeibnizInternationalProceedingsinInformatics,editedbyP.Felber,R.
Friedman,S.Gilbert,andA.Miller(Leibniz-ZentrumfürInformatik,Dagstuhl,Germany,2020),pp.15:1–15:16.
[63] S.V.JayantiandR.E.Tarjan,Concurrentdisjointsetunion,Distrib.Comput.34,413(2021).
[64] M.E.J.Newman,S.Forrest,andJ.Balthrop,Emailnetworksandthespreadofcomputerviruses,Phys.Rev.E66,035101(R)(2002).
[65] P.HolmeandJ.Saramäki,Temporalnetworks,Phys.Rep.519,97(2012).
---- END DOCUMENT ----
