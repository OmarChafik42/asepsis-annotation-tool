Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Collective self-sorting on a chip
Emanuel F. Teixeira,1,∗ Thieu van den Bergh,1 Arjen Klok,1 Tijn Heesakkers,1 and Alexandre Morin1,†
1Huygens-Kamerlingh Onnes Laboratory, Universiteit Leiden,
PO Box 9504, 2300 RA Leiden, The Netherlands
(Dated: August 25, 2026)
We harness two established ingredients for collective demixing: differential speed and curvature
tocreateaself-sortingdevice. Inbinarymixtures,motilitydifferencesdrivespontaneousspatialseg-
regation, while confinement geometry determines how rapidly and strongly this demixing develops.
Usingparticlebasedsimulations,wesystematicallyidentifythegeometricalconditionsthatpromote
efficientsegregationandusetheseresultstoguidethedesignofafinitesortingarchitecture. Wethen
translate these physical mechanisms into a sequence of curved microfluidic units that progressively
amplifytheseparationofthetwospeciesanddirectthemtowarddistinctcollectionregions. Exper-
imentswithbinaryQuincke-rollermixturesconfirmthataninitiallymixedsuspensionprogressively
demixesasitpropagatesthroughthedevice,leadingtostrongenrichmentdownstream. Ourresults
demonstrate how collective active demixing can be converted into a functional continuous sorting
strategy, providing a route toward autonomous microfluidic separation based on particle motility
and confinement geometry.
I. INTRODUCTION of phenotypic or dynamical asymmetry. In cellular sys-
tems, theoretical and experimental studies have shown
Sortinganddemixingarecentralmechanismsbywhich thatdifferentialadhesion[8–14], differentialcontractility
multicomponentsystemsacquirespatialorganization. In [15–20],anddifferentialpersistence[21]caneachpromote
systems evolving at, or close to, equilibrium, thermal spatial sorting. In passive Brownian mixtures, segrega-
fluctuations enable the constituents to explore configu- tion has likewise been observed to arise from differences
rationspace,andtheresultingorganizationisultimately in diffusivity [22, 23]. In synthetic active matter, Maity
selectedbyfree-energyminimization. Out-of-equilibrium et al. first showed that demixing in mixtures of self-
systems present a distinct challenge. In contrast to sys- propelled colloidal rollers can emerge from differences in
tems at equilibrium, their constituents do not necessar- self-propulsionspeed,throughthecombinedeffectsofdif-
ily rely on thermal fluctuations to explore configuration ferential motility, collective motion, and curved confine-
space, and the selected state need not minimize a free- ment [24]. More recently, speed-driven segregation has
energy functional. Segregation can instead emerge from, alsobeenreportedinothersyntheticactivesystems[25].
and be stabilized by, the underlying dynamics. Within Here, we confirm these predictions experimentally, nu-
this broad class of systems, it is useful to distinguish merically, and integrate all our findings to design and
externally driven mixtures from active ones. In driven test a sorting chip based on active collective demixing.
systems, spatial reorganization is powered by external Our new measurements show that a difference in self-
actuation or applied fields. A paradigmatic example is propulsion speed is sufficient to drive demixing in bi-
theBrazilnuteffect,inwhichmechanicalshakingcauses nary active mixtures. We demonstrate this using parti-
granular mixtures to segregate by size [1]. Related prin- cles made of different materials, considering both equal-
ciples underlie sedimentation-driven sorting in colloidal sized and differently sized particles. We then compare
suspensions [2] and phoresis-based mechanisms for par- the experimental measurements with numerical simula-
ticle separation [3]. Besides these well know examples, tions, which quantitatively reproduce the demixing be-
segregation in driven system is still a playground for in- haviour observed above the flocking transition. We next
novative solutions, such as the stochastic resetting [4], systematically investigate, both experimentally and nu-
promising to sort particles by shape. merically, the role of confining boundaries. Consistent
with the theoretical description of vortical flocks, our re-
In contrast with passive systems, active systems pro-
sults show that curved boundaries are a key ingredient
vide at the scale of their intrinsic constituents, the mo-
in promoting and controlling the demixing process. Fi-
bility to re-organize in space towards a segregated state.
nally, wecombinetheseinsightstodesignanoperational
A seminal example is the segregation of motile cells with
device optimized for autonomous sorting. We conclude
differential speeds [5]. This was later confirmed by min-
byprovidinganexperimentalproofofconceptforcollec-
imal numerical models showing that self-propelled parti-
tive active sorting on a chip.
cleswithdifferentialspeedspontaneouslysegregate[6,7].
More broadly, segregation can arise from several forms
∗ teixeira@physics.leidenuniv.nl
† morin@physics.leidenuniv.nl
6202
guA
42
]tfos.tam-dnoc[
1v37622.8062:viXra

2
FIG. 1. Differential self-propulsion speed controls radial demixing. a Experimental observations (top) of binary
Quincke-roller flocks confined in a circular well. Reversing the applied electric field switches the relative propulsion speeds
of the two species and consequently inverts the demixing pattern: the faster species accumulates near the outer boundary,
whereas the slower species is enriched toward the centre. Particle-based simulations (bottom) reproduce the experimentally
observed radial organization, with faster particles preferentially occupying the outer region and slower particles accumulating
in the inner region. b Self-propulsion speed as a function of the applied electric field for different AOT molarities for PS and
PMMA particles. c Demixing parameter as a function of the self-propulsion speed difference for reciprocal and nonreciprocal
interactions. Demixing increases with motility contrast in both cases, demonstrating that nonreciprocity is not required for
| speed-driven | demixing. |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
II. DIFFERENTIAL SPEED DRIVES diculartotheglassplatesactivatesQuinckerotationand
|     |     | DEMIXING |     |     | drives rolling | motion           | along the bottom | surface. |            |
| --- | --- | -------- | --- | --- | -------------- | ---------------- | ---------------- | -------- | ---------- |
|     |     |          |     |     | In the         | flocking regime, | this dense       | binary   | suspension |
formsacirculatingpolarflockandundergoesclearradial
Quincke rollers spontaneously organize into polar demixing inside the circular confinement (see Fig. 1a).
flocks. Building on the observation by Maity et al. that Crucially, the demixing pattern is not fixed by particle
|        |                |            |               |       | sizeormaterialalone. |     | Instead,itdependsontheapplied |     |     |
| ------ | -------------- | ---------- | ------------- | ----- | -------------------- | --- | ----------------------------- | --- | --- |
| binary | Quincke-roller | flocks can | spontaneously | demix |                      |     |                               |     |     |
when the two species have different motilities, we ex- electric field, which tunes the relative self-propulsion
tend this experimental framework to mixtures with dif- speeds of the two species (see Fig. 1b). This makes the
|             |        |              |               |          | PS-PMMA | mixturean | idealexperimentalsystem |     | totest |
| ----------- | ------ | ------------ | ------------- | -------- | ------- | --------- | ----------------------- | --- | ------ |
| ferent size | ratios | and material | compositions. | We first |         |           |                         |     |        |
examine a binary suspension of fluorescent polystyrene whethermotilitydifference,ratherthansize,controlsthe
(PS) particles with diameter d = 10 µm and poly- polarity of active demixing.
PS
methyl methacrylate (PMMA) particles with diameter At low field, PMMA particles self-propel faster
d PMMA = 7.5µm, confined in circular wells of radius (Fig. 1b) and accumulate near the outer edge of the
R = 500 µm. The circular well contains N = 2530 par- flock, while PS particles are enriched toward the cen-
ticles, with N = 1006 and N = 1524. In the tre. At higher field, the speed hierarchy is reversed: PS
|     | PS  |     | PMMA |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
microscopy images, the fluorescent PS particles appear particles become faster and migrate to the outer region,
as white dots, whereas the PMMA particles appear dark whereas PMMA particles accumulate closer to the cen-
(see Fig. 1a). The particles are dispersed in hexadecane tre. Thus, the demixing pattern is inverted by changing
containingAOTandloadedintoanITO-coatedmicroflu- the electric field, with the faster species consistently oc-
idic chamber, where a DC electric field applied perpen- cupyingtheouterregionandtheslowerspeciestheinner

3
region, as shown in Fig. 1a. This field-induced inversion F =−k (r −(σ +σ )/2)ˆr , wherek istherepulsive
|     |     |     |     |     |     |     |     | ij  | c ij | i   | j   | ij  |     | c   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
provides direct control over active demixing. By tuning stiffness, and σ and σ are the diameters of particles i
|     |     |     |     |     |     |     |     |     |     | i   | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the electric field, we can reverse the demixing polarity and j, respectively. For a binary mixture of species µ
andpartiallymodulatethedemixingstrength. Thispro- and ν, let i and j label the interacting particles, and let
grammabilityisessentialfordeviceimplementation,asit α ,α ∈ µ,ν denote their respective species. When par-
i j
shows that motility-induced demixing can be used as an ticles i and j interact, the coupling is determined by the
externally controlled sorting mechanism. matrixelementinrowα i andcolumnα j . Theinteraction
|     |      |          |     |       |             |     |     | matrices | are therefore |       |     |             |             |     |     |
| --- | ---- | -------- | --- | ----- | ----------- | --- | --- | -------- | ------------- | ----- | --- | ----------- | ----------- | --- | --- |
|     |      |          |     |       |             |     |     |          |               |       |     | (cid:18) a3 | a3 (cid:19) |     |     |
|     | III. | PARTICLE |     | BASED | SIMULATIONS |     |     |          |               | A     |     |             |             |     |     |
|     |      |          |     |       |             |     |     |          | A(r           | )=    | Θ(r | ) µ         | ν           | ,   | (4) |
|     |      |          |     |       |             |     |     |          |               | ij r3 |     | ij a3       | a3          |     |     |
|     |      |          |     |       |             |     |     |          |               |       | ij  | µ           | ν           |     |     |
Maity et al. [24] introduced a microscopic model for B (cid:18) a4 a3(cid:19)
|     |     |     |     |     |     |     |     |     |     |     |     |     | µ a µ | ν   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
binary mixtures of confined Quincke rollers, incorporat- B(r )= Θ(r ) , (5)
|     |     |     |     |     |     |     |     |     |     | ij r | 4   | ij a | a3 a4 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |      | i j | ν    | µ     | ν   |     |
inghydrodynamicalignment,electrostaticrepulsion,and
species-dependent self-propulsion. By coarse-graining The four matrix elements correspond to the ordered
| these | particle-level |     | dynamics, |     | they derived |     | a hydrody- |         |       |        |        |        |     |        |         |
| ----- | -------------- | --- | --------- | --- | ------------ | --- | ---------- | ------- | ----- | ------ | ------ | ------ | --- | ------ | ------- |
|       |                |     |           |     |              |     |            | species | pairs | (µ,µ), | (µ,ν), | (ν,µ), | and | (ν,ν). | Here, a |
µ
namic theory for the density and polarization fields of and a are the radii of particles of species µ and ν,
ν
the two species. The resulting steady-state density pro- respectively, A and B set the alignment and repulsion
| files | captured | the | experimentally |     | observed | flocking | and |            |     |        |             |     |              |     |          |
| ----- | -------- | --- | -------------- | --- | -------- | -------- | --- | ---------- | --- | ------ | ----------- | --- | ------------ | --- | -------- |
|       |          |     |                |     |          |          |     | strengths, | and | Θ(r ij | ) restricts | the | interactions |     | to a fi- |
radial demixing without fitting parameters, identifying nite range. The nonreciprocity arises from the repul-
propulsion-speed heterogeneity as the primary demixing sive torque term nˆ ·ˆr , combined with the difference in
|           |            |     |               |         |              |       |             |          |              | i           | ij      |           |         |     |            |
| --------- | ---------- | --- | ------------- | ------- | ------------ | ----- | ----------- | -------- | ------------ | ----------- | ------- | --------- | ------- | --- | ---------- |
| mechanism |            | and | nonreciprocal |         | interactions | as    | a quantita- |          |              |             |         |           |         |     |            |
|           |            |     |               |         |              |       |             | particle | size between |             | the two | species,  | which   | is  | explicitly |
| tive      | correction |     | to the        | spatial | profiles.    | Here, | we directly |          |              |             |         |           |         |     |            |
|           |            |     |               |         |              |       |             | encoded  | in the       | interaction |         | matrices. | Because |     | these ma-  |
integrate the same microscopic equations of motion in tricesaregenerallynotsymmetricundertheexchangeof
molecular dynamics simulations of binary mixtures con- the interacting species, the microscopic interactions vio-
| fined | within | circular | wells. | This | particle-based |     | approach |                      |     |           |     |         |     |        |           |
| ----- | ------ | -------- | ------ | ---- | -------------- | --- | -------- | -------------------- | --- | --------- | --- | ------- | --- | ------ | --------- |
|       |        |          |        |      |                |     |          | late action–reaction |     | symmetry. |     | Details |     | of the | numerical |
enables a direct comparison with our experimental ob- methods and parameters, chosen on the basis of exper-
servationswhileallowingthespeedtobevariedindepen- imentally measured values, are provided in the Supple-
| dently | and | extended |     | beyond | the experimentally |     | accessi- |         |              |     |        |     |        |           |     |
| ------ | --- | -------- | --- | ------ | ------------------ | --- | -------- | ------- | ------------ | --- | ------ | --- | ------ | --------- | --- |
|        |     |          |     |        |                    |     |          | mentary | Information. |     | Yellow | and | purple | particles | are |
ble range.
|     |     |     |     |     |     |     |     | denoted | as species | 1   | and 2, | respectively. |     | The | diameter |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ------ | ------------- | --- | --- | -------- |
Wedescribeabinarycolloidalflockwhereineachroller of the larger, yellow particles defines the characteristic
self-propels at a species-dependent speed, undergoes ro- length scale, such that a = 1, while the diameter of
1
| tational | diffusion, |     | and | reorients | through | hydrodynamic |     |            |                         |     |     |     |     |                 |     |
| -------- | ---------- | --- | --- | --------- | ------- | ------------ | --- | ---------- | ----------------------- | --- | --- | --- | --- | --------------- | --- |
|          |            |     |     |           |         |              |     | species2,a | ,isexpressedrelativetoa |     |     |     | .   | Alllengthscales |     |
|          |            |     |     |           |         |              |     |            | 2                       |     |     |     | 1   |                 |     |
alignment and electrostatic repulsion with neighbouring are expressed in units of the radius of species a . The
1
particles. The position r and orientation θ of particle i propulsion speed of the faster species defines the char-
|     |     |     |     | i   |     | i   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
evolve as
|     |     |     |     |     |     |     |     | acteristic | velocity | scale | and | is set | to v | fast = | 1. Either |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ----- | --- | ------ | ---- | ------ | --------- |
(cid:88) species may be assigned the larger propulsion speed, al-
|     | r˙ =v | nˆ +ζ |     | F , |     |     | (1) |     |     |     |     |     |     |     |     |
| --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i i i ij lowing us to systematically vary the relative motility of
j̸=i the two species. The rotational diffusion coefficient is
|     |     | 1 ∂ (cid:88) |     |     | (cid:112) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
θ˙ = H (r ,nˆ ,nˆ )+ 2D ξ (t), (2) fi x ed a t D = 0 . 0 2 . T h is v a l u e w a s o b t ai n e d b y c o n v e r t -
|     | i   |     | eff | ij  | i j | R   | i   |     | R   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
τ ∂ θ i in g pr e v io us ly r e p o r te d e x p e r im e n t a l m e a s ur e m e n t s f o r
i̸=j
|            |     |      |          |       |                 |           |             | Quincke                                              | rollers | [24] into   | the | simulation |      | units defined | by      |
| ---------- | --- | ---- | -------- | ----- | --------------- | --------- | ----------- | ---------------------------------------------------- | ------- | ----------- | --- | ---------- | ---- | ------------- | ------- |
| where      | nˆ  | =    | (cosθ    | ,sinθ | ) is the        | direction | of self-    |                                                      |         |             |     |            |      |               |         |
|            | i   |      | i        | i     |                 |           |             | thecharacteristicparticlediameterandpropulsionspeed. |         |             |     |            |      |               |         |
| propulsion |     | v of | particle | i,    | D is rotational |           | diffusivity |                                                      |         |             |     |            |      |               |         |
|            |     | i    |          |       | R               |           |             | Simulations                                          |         | of a binary |     | mixture    | with | a /a          | = 0.75, |
2 1
and ζ the mobility. The combined effects of hydrody- N = 1006 particles of species 1 and N = 1524 parti-
|       |     |               |     |              |     |           |        | 1       |         |             |        |     |          | 2    |           |
| ----- | --- | ------------- | --- | ------------ | --- | --------- | ------ | ------- | ------- | ----------- | ------ | --- | -------- | ---- | --------- |
| namic | and | electrostatic |     | interactions | is  | described | by ef- |         |         |             |        |     |          |      |           |
|       |     |               |     |              |     |           |        | cles of | species | 2, confined | within | a   | circular | well | of radius |
fective potential
|     |        |     |     |        |        |        |           | R = 50,       | show | that a | differences | in      | self-propulsion |                | speed |
| --- | ------ | --- | --- | ------ | ------ | ------ | --------- | ------------- | ---- | ------ | ----------- | ------- | --------------- | -------------- | ----- |
|     |        |     |     |        |        |        |           | is sufficient | to   | induce | demixing    | despite |                 | the difference | in    |
| H   | (r ,nˆ | ,nˆ | )=A | (r )nˆ | ·nˆ +B | (r )nˆ | ·ˆr , (3) |               |      |        |             |         |                 |                |       |
eff ij i j ij ij i j ij ij i ij particlesize. Consistentwiththeexperiments,theslower
ri−rj
where r = |r −r | and ˆr = . The functions speciespreferentiallyoccupiesthecentralregion,whereas
|      | ij          | i         | j            |           | ij |ri−rj|    |             |            |            |                                        |             |     |      |     |       |          |
| ---- | ----------- | --------- | ------------ | --------- | ------------- | ----------- | ---------- | ---------- | -------------------------------------- | ----------- | --- | ---- | --- | ----- | -------- |
|      |             |           |              |           |               |             |            | the faster | species                                | accumulates |     | near | the | outer | boundary |
| A ij | (r ij ) and | B         | ij (r ij )   | quantify, | respectively, |             | the align- |            |                                        |             |     |      |     |       |          |
|      |             |           |              |           |               |             |            | (Fig.1a).  | Toquantifythedegreeofdemixing,weusethe |             |     |      |     |       |          |
| ment | and         | repulsive | interactions |           | exerted       | by particle | j on       |            |                                        |             |     |      |     |       |          |
particle i. The timescale τ sets the characteristic relax- demixing parameter introduced by Belmonte et al. [12]:
ation time of the orientational dynamics, while ξ i (t) is (cid:68)n (cid:69)
̸=
a Gaussian white noise with zero mean and unit vari- γ = , (6)
n
| ance. | The | pairwise | force | F   | is an excluded-volume |     | in- |     |     |     |     |     |     |     |     |
| ----- | --- | -------- | ----- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ij
teraction that prevents particle overlap. For interpar- where n is the number of neighbouring particles be-
̸=
ticle distance r ij ≤ (σ i + σ j )/2, the repulsive force is longing to the other species and n is the total number

4
of neighbours. The brackets denote an average over all organization. According to this criterion, we quantify
particles of both species. Thus, large values of γ cor- thedemixingtimeandfindthatdemixingproceedsmore
respond to a well-mixed state, whereas smaller values rapidly in smaller arenas, as evidenced by the decrease
indicate stronger demixing. Figure 1c shows the steady inthecharacteristicdemixingtimewithdecreasingarena
state value of γ, averaged over time, as a function of radius (Fig. 2c). This behavior reflects the shorter dis-
the relative propulsion speed of the two species. Both tances over which particles must reorganize to establish
experiments and numerical simulations, for mixtures of the steady state radial distribution. Reducing the arena
equal and unequal sized particles, show that γ is maxi- sizedoesnotsubstantiallycompromisethefinaldegreeof
mal when the two species propel at the same speed and demixing. Thesteadystatedemixingparameterdepends
decreases as the speed contrast increases in either direc- only weakly on the arena size (Fig. 2d), indicating that
tion. Together with the corresponding inversion of the small arenas can retain a separation purity comparable
radial density profiles, this non-monotonic dependence to that of larger systems. Thus, when processing time
demonstratesthatthespeciesoccupyingtheouterregion is a limiting factor, an array of small arenas should pro-
is selected by its relative propulsion speed: reversing the vide a higher throughput than a single large arena. This
speed hierarchy reverses the radial organization. These weak system size dependence differs markedly from that
resultsestablishthatadifferenceinself-propulsionspeed reported by Belmonte [12], where demixing becomes less
is sufficient to drive robust radial demixing under circu- pronouncedasthesystemsizedecreases. Inthatsystem,
lar confinement. The simulations further provide a con- thetwocomponentsformfullyseparatedmacroscopicdo-
trolled framework for independently probing the effects mainsdividedbyaninterfaceoffinitewidth. Therelative
of confinement geometry and speed difference. A mini- contribution of this interfacial region decreases with in-
malparticlebasedmodelwithspecies-dependentpropul- creasingsystemsize,leadingtoanapparentenhancement
sion speeds therefore captures the essential mechanism of demixing in larger systems. By contrast, demixing in
underlying the experimentally observed radial demixing binary flocks is not driven by the formation of two bulk
and provides a tool for identifying the conditions that phases separated by a surface tension controlled inter-
maximize sorting performance. face. Instead, the composition varies continuously from
the center to the boundary of the arena, and the radial
densityprofilesexhibitaself-similarformacrossdifferent
IV. DESIGNING A SELF-SORTING DEVICE system sizes (see Supplementary Material).
Althoughcirculararenasprovideanefficientgeometry
Before designing a self-sorting device, we first sought for establishing radial demixing, they are not well suited
to determine how demixing performance could be op- for the continuous collection of the separated particle
timized. We considered two key criteria: the purity populations. A practical self-sorting device, therefore,
of the separated fractions and the processing through- requires a channel geometry that preserves the underly-
put. These quantities are governed, respectively, by the ing demixing mechanism while directing the two particle
demixing level and the time required to reach it. fractions toward distinct outlets.
Wethereforeinvestigatedtheeffectofconfinementsize To continuously collect the sorted particles, the
by performing simulations in circular arenas of different demixedpopulationsmustultimatelybedirectedtowards
radii. In these simulations, we considered a 50:50 binary separate outlets. This requirement introduces an im-
mixture with a size ratio a 2 /a 1 = 0.75, a propulsion- portant geometrical constraint: curvature plays a key
speed ratio v 2 /v 1 = 0.8, and a packing fraction ϕ = role in promoting demixing in colloidal flocks of Quincke
(cid:80)N πσ i 2 = 0.2. These parameter values were chosen rollers [24]. To determine how the sorting mechanism
i πR2
to be representative of those typically measured in the dependsonconfinementgeometry, wethereforedesigned
experiments. In Fig. 2a we observe the system in two an annular channel by introducing an impenetrable cir-
circular arenas of radius R = 200 (top) and R = 100 cular region of radius R in at the centre of the original
(bottom). The smaller arena reaches the demixed state circulararenaofradiusR out . VaryingtheratioR in /R out
faster than the larger one, indicating that the demixing allows us to systematically tune the relative curvature of
timescale depends on the confinement radius. Figure 2b the inner and outer boundaries. Experiments and simu-
showstheevolutionofthedemixingparameterfordiffer- lations were performed for a 50:50 binary mixture with
entarenaradiiasthesystemtransitionsfromamixedto a 2 /a 1 =0.75, v 2 /v 1 =0.8, and packing fraction ϕ=0.2.
ademixedstate. Althoughallsystemseventuallyreacha Bothexperimentsandsimulationsrevealapronounced
steadydemixedstate,thetimerequiredforthedemixing dependence of the steady-state organization on this ge-
parameter to reach its plateau depends strongly on the ometrical ratio. At small R /R , the two species re-
in out
arena radius. It is therefore necessary to define a quan- mainradiallydemixed,whereasincreasingR /R pro-
in out
titative criterion for determining when the system has gressivelysuppressesdemixingandeventuallyproducesa
reached the demixed state. We define the characteristic mixedsteadystate(Fig.3a). Wequantifythistransition
demixing time as the time at which γ first decreases be- using the time-averaged steady-state demixing parame-
low 0.4, a threshold corresponding to the emergence of a ter, ⟨γ⟩ , shown in Fig. 3b. The demixing parameter de-
t
macroscopically demixed state with a well-defined radial creasesmonotonicallywithincreasingR /R ,confirm-
in out

5
FIG. 2. Smaller confinements accelerate demixing without compromising separation purity. a Configurations of
binary active particles confined in circular arenas of different radii, showing the steady-state radial organization of the two
species. b Time evolution of the demixing parameter, γ, for different arena sizes. The characteristic demixing time, τ, is
defined as the first time at which γ < 0.4, corresponding to the emergence of a macroscopically demixed state with a well-
defined radial organization. c Characteristic demixing time as a function of the arena radius. Demixing occurs more rapidly
in smaller arenas because particles must reorganize over shorter distances to establish the steady-state radial distribution. d
Steady-state demixing parameter as a function of the arena radius. Its weak dependence on system size demonstrates that
reducingthearenasizeacceleratesdemixingwithoutsubstantiallydecreasingthefinalseparationpurity. Theseresultsindicate
that an array of small arenas can provide a higher processing throughput than a single large arena.
ing that radial segregation becomes progressively weaker second. We therefore introduce a separating wall at the
astherelativecurvatureofthetwoboundariesdecreases. junction between the two sections, which preserves the
|                                       |          |                 |                |             |        | spatial         | separation | established   | upstream | and      | directs the    |
| ------------------------------------- | -------- | --------------- | -------------- | ----------- | ------ | --------------- | ---------- | ------------- | -------- | -------- | -------------- |
| Therefore,                            | demixing | is              | not determined | solely      | by the |                 |            |               |          |          |                |
|                                       |          |                 |                |             |        | two populations |            | towards       | distinct | outlets. | This construc- |
| curvature                             | of the   | outer boundary, | although       | finite-size | ef-    |                 |            |               |          |          |                |
|                                       |          |                 |                |             |        | tion results    | in         | the three-way | geometry | shown    | in Fig. 4b.    |
| fects remain                          | present. | Instead,        | the relative   | geometry    | of     |                 |            |               |          |          |                |
|                                       |          |                 |                |             |        | The performance |            | of this       | geometry | depends  | on the po-     |
| thetwoconfiningboundaries,capturedbyR |          |                 |                | /R          | ,pro-  |                 |            |               |          |          |                |
in out
vides the dominant control parameter for maintaining sition of the separating wall. We parameterize its radial
|                    |          |               |          |                 |       | location | by  |     |      |     |     |
| ------------------ | -------- | ------------- | -------- | --------------- | ----- | -------- | --- | --- | ---- | --- | --- |
| radial segregation |          | in an annular | channel. | Efficient       | sort- |          |     |     |      |     |     |
| ing, thus,         | requires | sufficiently  | small R  | /R , establish- |       |          |     |     |      |     |     |
|                    |          |               | in       | out             |       |          |     |     | R −R |     |     |
ing a direct geometrical design principle for translating w = wall in, (7)
|     |     |     |     |     |     |     |     |     | R −R |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
curvature-induced demixing into a continuous particle- out in
sorting device.
|     |     |     |     |     |     | whereR | istheradialdistanceofthewallfromthecen- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --------------------------------------- | --- | --- | --- | --- |
wall
Wenextusenumericalsimulationstoaddressasecond ter of the corresponding semicircular section. Guided by
design challenge: connecting a single inlet to two sepa- the results of the previous section, we choose a compact
rate outlets while preserving the demixing generated by and strongly curved channel, for which demixing is both
the curved channel. Starting from the circular geometry rapid and pronounced. We therefore set R = 50 and
out
of Fig. 4a, we cut the channel into two semicircular sec- R /R = 0.1, while keeping all remaining simulation
in out
|                  |     |               |                 |     |        | parameters | unchanged | from | the | previous | section. |
| ---------------- | --- | ------------- | --------------- | --- | ------ | ---------- | --------- | ---- | --- | -------- | -------- |
| tions, translate |     | them relative | to one another, | and | recon- |            |           |      |     |          |          |
nectthemasillustratedinFig.4b. Becausethedirection To first identify strategies for optimal demixing, we
of radial demixing reverses between the two semicircular use simulations to consider the idealized limit of an infi-
sections, particles separated in the first half would oth- nite sequence of sorting units. To realize this limit, we
erwise be driven towards one another and remix in the impose periodic boundary conditions that reconnect the

6
FIG. 3. From arena to circular channels. a. Experimental snapshots of a binary mixture confined in an annular channel
fordifferentvaluesofR /R ,showingtheprogressivelossofradialdemixingastheinnerradiusincreases. b. Corresponding
|     |     | in out |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
simulation snapshots obtained under the same conditions, reproducing the transition from a demixed to a mixed state. c.
Steady-statedemixingparameterfromnumericalsimulations,⟨γ⟩ ,asafunctionofR /R forexperimentsandsimulations.
|     |     |     |     |     | t   |     | in out |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
Demixing decreases monotonically with increasing R /R , demonstrating that the relative curvature of the inner and outer
in out
| boundaries            | controls the | efficiency                      | of radial segregation. |               |            |     |     |     |     |     |
| --------------------- | ------------ | ------------------------------- | ---------------------- | ------------- | ---------- | --- | --- | --- | --- | --- |
| twooutletstotheinlet. |              | Particlesleavingeitheroutletare |                        |               | throughput |     |     |     |     |     |
| therefore             | reinjected   | at the inlet,                   | allowing               | the system to |            |     |     |     |     |     |
reach a statistically stationary state while maintaining a Qo utlet
|     |     |     |     |     |     |     | Q˜ = | k , |     | (8) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
k
| constantparticlepopulation. |     |     | Withinthisperiodicgeom- |     |     |     |     | Qinlet |     |     |
| --------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | ------ | --- | --- |
k
| etry,wesystematicallyvaryw |     |     | andquantifytheresulting |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
sortingperformancefromtheparticlecompositionatthe where Qinlet is the incoming flux of species k and Qoutlet
|     |     |     |     |     |     | k   |     |     |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two outlets. Figure 4c reports the corresponding steady- isthefluxofthesamespeciesrecoveredatitsdesignated
state fractions χin and χin at the inner outlet, whereas outlet. Fastparticles(species1)arecollectedattheinner
|     | 1   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 4d shows χout and χout at the outer outlet, with outlet, whereas slow particles (species 2) are collected at
|            | 1    | 2        |     |     |           |             |              |                 |              |     |
| ---------- | ---- | -------- | --- | --- | --------- | ----------- | ------------ | --------------- | ------------ | --- |
| χin =1−χin | χout | =1−χout. |     |     |           |             |              | Q˜ Q˜           |              |     |
|            | and  |          |     |     | the outer | outlet.     | Accordingly, | and             | represent    | the |
| 1          | 2    | 1        | 2   |     |           |             |              | 1               | 2            |     |
|            |      |          |     |     | fractions | of incoming | fast and     | slow particles  | successfully |     |
|            |      |          |     |     | recovered | at their    | respective   | target outlets. |              |     |
The outlet composition depends strongly on the wall Figure 4e shows that the two throughputs vary oppo-
position. For collection at the inner outlet, the purity sitely with the wall position. The recovery of fast parti-
varies non-monotonically with w, reaching an optimum clesattheinneroutlet,Q˜ ,increasesmonotonicallywith
1
valuearoundw ≃0.2,whereχ 1 ismaximalandχ 2 ismin- w, reaching its largest value when the separating wall
imal (Fig. 4c). Beyond this point, the purity decreases approaches the outer boundary. Conversely, the recov-
monotonicallywithincreasingw,andthecollectedpopu- ery of slow particles at the outer outlet, Q˜ , decreases
2
lationbecomesprogressivelymoremixed. Asimilarnon- monotonically with w and is therefore largest when the
monotonic dependence is observed for collection at the separatingwallliesclosetotheinnerboundary. Thetwo
outer outlet, although the optimal purity is shifted to curves intersect around w ≃ 0.5, where the two species
w ≃ 0.5 (Fig. 4d). For larger w, the purity again de- are recovered with comparable efficiency.
creases monotonically, approaching a mixed state. Pu- Comparison with the corresponding purity curves re-
rity alone does not fully characterize the performance veals a trade-off between purity and recovery: wall posi-
of the sorter, because a highly pure outlet may recover tionsthatyieldahighlyenrichedoutletdonotnecessarily
only a small fraction of the target species. We therefore collect the largest fraction of the target species. The op-
also quantify particle recovery through the normalized timalwallpositionmustthereforebalancethesetwocom-

7
FIG.4. Fromcircularchannelstocontinuousparticlecollection. a. Circularannularchannelusedtogenerateradialdemixing
between fast and slow particles. b. Three-way sorting geometry obtained by combining two shifted semicircular channels and
introducingaseparatingwallthatdirectsthedemixedpopulationstowardsdistinctinnerandouteroutlets. Thewallposition
is parametrized by w = (R −R )/(R −R ). c. Steady-state particle fractions χin and χin at the inner outlet as a
|     |     |     | wall | in  | out | in  |     |     |     | 1   | 2   |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
functionofw. Thepurityoffastparticlesismaximalaroundw≃0.2. d. Correspondingparticlefractionsχout andχout atthe
|     |     |     |     |     |     |     |     |     |     |     |     | 1   |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
outeroutlet,withmaximalpurityofslowparticlesaroundw≃0.5. e. Normalizedthroughputoffastparticlesrecoveredatthe
inner outlet, Q˜ , and slow particles recovered at the outer outlet, Q˜ , as a function of w. Increasing w enhances the recovery
|     |     | 1   |     |     |     |     | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of fast particles while reducing that of slow particles, revealing the trade-off between outlet purity and particle recovery.
plementary measures, with purity quantifying the com- jection rule at the virtual boundary connecting the out-
position of the collected fraction and Q˜ quantifying the lets to the inlet. When a particle crosses an outlet, it
k
fraction of the available target population that is recov- is reinjected at a random position along the inlet cross-
ered. section while retaining its velocity (Fig. 5c). This pro-
|         |         |               |     |     |         |             | cedure | mimics | the continuous |     | supply | of  | particles | in an |
| ------- | ------- | ------------- | --- | --- | ------- | ----------- | ------ | ------ | -------------- | --- | ------ | --- | --------- | ----- |
| So far, | we have | characterized |     | the | sorting | performance |        |        |                |     |        |     |           |       |
experimentwhileeliminatingthespatialcorrelationsgen-
intermsofsteady-statepurityandthroughputusingpe-
|                           |     |     |     |                          |     |     | erated by | directly | reconnecting |     | each | outlet | to  | the inlet. |
| ------------------------- | --- | --- | --- | ------------------------ | --- | --- | --------- | -------- | ------------ | --- | ---- | ------ | --- | ---------- |
| riodicboundaryconditions. |     |     |     | Althoughthisapproachpro- |     |     |           |          |              |     |      |        |     |            |
Theresultingsteadystatethereforeallowsustomonitor
| vides access  | to           | the asymptotic |             | behavior      | of          | an effectively |                 |             |       |               |              |               |           |         |
| ------------- | ------------ | -------------- | ----------- | ------------- | ----------- | -------------- | --------------- | ----------- | ----- | ------------- | ------------ | ------------- | --------- | ------- |
|               |              |                |             |               |             |                | how an          | initially   | mixed | population    |              | progressively |           | demixes |
| infinite      | sequence     | of sorting     |             | units,        | it does     | not directly   |                 |             |       |               |              |               |           |         |
|               |              |                |             |               |             |                | as it passes    | through     |       | successive    | three-way    |               | sorting   | units.  |
| represent     | the          | operation      | of          | a finite      | device.     | In practice,   |                 |             |       |               |              |               |           |         |
| the available | space        | is             | limited,    | and particles |             | traverse only  |                 |             |       |               |              |               |           |         |
|               |              |                |             |               |             |                | The simulations |             | show  | that          | particles    |               | enter the | device  |
| a finite      | number       | of three-way   |             | channels      | before      | being col-     |                 |             |       |               |              |               |           |         |
|               |              |                |             |               |             |                | in a mixed      | state       | and   | progressively |              | segregate     |           | as they |
| lected at     | the outlets. |                | This raises | an            | important   | practical      |                 |             |       |               |              |               |           |         |
|               |              |                |             |               |             |                | propagate       | downstream. |       | After         | traversing   |               | several   | sorting |
| question:     | what         | is the         | minimum     | number        | of          | sorting units  |                 |             |       |               |              |               |           |         |
|               |              |                |             |               |             |                | units, a        | pronounced  |       | radial        | organization |               | develops, | with    |
| required      | for the      | outlet         | composition |               | to approach | that ob-       |                 |             |       |               |              |               |           |         |
thefasterparticlespreferentiallylocalizedneartheinner
| tained in | the infinite-channel |     |     | limit? |     |     |          |              |     |          |         |     |                 |     |
| --------- | -------------------- | --- | --- | ------ | --- | --- | -------- | ------------ | --- | -------- | ------- | --- | --------------- | --- |
|           |                      |     |     |        |     |     | wall and | consequently |     | directed | towards |     | the correspond- |     |
Toaddressthisquestion,weintroduceamodifiedrein- ing outlet (Fig. 5c). We quantify this convergence by

8
FIG.5. Fromperiodicsortingtoafinite-sizedevice. a. Steady-stateparticlefractionsmeasuredattheinnerandouteroutlets
as a function of the number of three-way sorting units, (N ). Dashed lines indicate the corresponding values obtained in
units
the infinite-channel limit. The inner-outlet composition converges after approximately (N units ≃20), whereas the outer outlet
reaches its asymptotic value after about (N units ≃12). b. Schematic of the finite sorting device composed of successive three-
way channel units, showing the progressive segregation of the two particle species along the channel. c. Reinjection boundary
condition used to mimic continuous operation of a finite device. Particles leaving through either outlet are reinjected at a
randompositionacrosstheinletwhileretainingtheirvelocity. Startingfromamixedpopulationattheinlet,repeatedpassage
through the sorting units produces a pronounced downstream demixing, with faster particles preferentially localized near the
| inner wall | and directed | towards | the corresponding | outlet. |     |     |     |     |     |     |
| ---------- | ------------ | ------- | ----------------- | ------- | --- | --- | --- | --- | --- | --- |
measuring the particle fractions χ 1 and χ 2 at the inner composed of successive curved sorting units, as shown
and outer outlets as a function of the number of sorting in Fig. 6a. The geometry is chosen to preserve the
units, N . For the inner outlet, the steady-state frac- curvature-induced demixing mechanism while remaining
units
tions progressively approach their infinite-channel values compatiblewiththefiniteareaavailableonthemicroflu-
and are essentially converged by N ≃ 20 (Fig. 5a). idic chip. Guided by the simulations, we set R /R =
|     |     |     | units |     |     |     |     |     |     | in out |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ------ |
This demonstrates that the demixing obtained in the 0.1, R =1 mm, N =10, and place the position of
|     |     |     |     |     |     | out | units |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
infinite-channellimitcanbereproducedwithafinite,ex- the separating wall at w = 0.7. These parameters pro-
perimentally realizable device. vide a compact realization of the sorting geometry while
For the outer outlet, convergence is reached more allowing the particle composition to evolve progressively
rapidly, at approximately N ≃ 12. The correspond- as the suspension travels downstream.
units
ingcompositionsneverthelessremainclosertothemixed- The experiments are performed using a binary mix-
statevaluethanthoseattheinneroutlet. Thisasymme- ture of fluorescent polystyrene particles with diameters
try reflects our choice of wall position, which was opti- d = 7 µm and d = 10 µm, prepared in approx-
|          |          |     |                      |           |      | black   | white              |              |            |     |
| -------- | -------- | --- | -------------------- | --------- | ---- | ------- | ------------------ | ------------ | ---------- | --- |
| mized to | maximize | the | purity of the faster | particles | col- |         |                    |              |            |     |
|          |          |     |                      |           |      | imately | equal proportions. | A continuous | suspension | of  |
lectedattheinneroutletratherthanthatofthecomple- the two species is injected through the inlet using a low-
mentary fraction. These results provide a direct design pressure syringe pump, providing a sustained flux of ini-
| criterion | for a finite | sorting | device: a | few tens of | three- |              |           |             |             |           |
| --------- | ------------ | ------- | --------- | ----------- | ------ | ------------ | --------- | ----------- | ----------- | --------- |
|           |              |         |           |             |        | tially mixed | particles | through the | device. The | particles |
wayunitsaresufficienttoreproducetheasymptoticsort- then traverse the sequence of curved units before reach-
ing performance while retaining a compact, experimen- ingtheoutletregion. Furtherdetailsoftheexperimental
tally accessible geometry. preparation and driving conditions are provided in the
|                 |     |     |              |        |     | Supplementary | Material.            |                     |              |            |
| --------------- | --- | --- | ------------ | ------ | --- | ------------- | -------------------- | ------------------- | ------------ | ---------- |
|                 |     |     |              |        |     | As the        | particles propagates | along               | the channel, | the ini-   |
| V. EXPERIMENTAL |     |     | SELF-SORTING | DEVICE |     |               |                      |                     |              |            |
|                 |     |     |              |        |     | tially mixed  | population           | progressively       | develops     | the radial |
|                 |     |     |              |        |     | organization  | identified           | in the simulations. | After        | only a     |
From this numerical exploration and insights gained, few sorting units, the two species become increasingly
wenowhavealltheinformationtorealizeanexperimen- segregated, and the separating wall converts this spatial
tal self-sorting device. We develop a snake-like channel organization into selective particle collection. For the

9
FIG. 6. Demixing in snake-like channels. a. Top: Geometry of the self-sorting device (w = 0.7). Insets: Experimental
snapshotsoftheoperatingdevice. b. Densityfractionoftheslow,7µm-diameterPSparticles,intheouterregionasafunction
of the length of the channel expressed in number of elementary units. Demixing reaches high purity in about 10 units.
chosen geometry, the smaller 7 µm and slower particles bust radial segregation under curved confinement. The
are preferentially directed toward the outer region of the faster species preferentially occupies the outer region of
channel and subsequently collected at the corresponding the flock, and reversing the relative propulsion speeds
outlet. reversesthespatialorganization,identifyingmotilitydif-
We quantify this progressive sorting by measuring the ference as the primary control parameter for the demix-
| fractionχ | of7µmsmaller(slower)particlesintheouter |     |     |     | ing. |     |     |     |     |     |     |
| --------- | --------------------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
2
region as a function of the distance traveled through We further established confinement geometry as a key
the device, expressed in the number of sorting units. ingredient for controlling the efficiency and timescale
| As shown | in Fig. | 6b, χ increases | systematically | down- |                 |         |          |              |     |     |            |
| -------- | ------- | --------------- | -------------- | ----- | --------------- | ------- | -------- | ------------ | --- | --- | ---------- |
|          |         | 2               |                |       | of segregation. | Smaller | circular | confinements |     |     | accelerate |
stream and approaches unity after approximately seven demixingwithoutsubstantiallycompromisingitssteady-
units. Thus, repeated passage through the curved ge- state strength, while increasing R /R in annular
|                      |     |           |                   |        |                                             |     |     |     | in  | out |          |
| -------------------- | --- | --------- | ----------------- | ------ | ------------------------------------------- | --- | --- | --- | --- | --- | -------- |
| ometry progressively |     | amplifies | the compositional | imbal- |                                             |     |     |     |     |     |          |
|                      |     |           |                   |        | channelsprogressivelysuppressessegregation. |     |     |     |     |     | Guidedby |
ance,transforminganapproximatelyequimolarinletsus- theseobservations,wedesignedvianumericalsimulation
pension into a highly enriched particle stream at the a three-way channel in which a separating wall converts
outlet. This experimental realization demonstrates that radial organization into distinct particle streams. The
| curvature-induced |     | collective demixing | can be | translated |               |          |     |         |         |        |        |
| ----------------- | --- | ------------------- | ------ | ---------- | ------------- | -------- | --- | ------- | ------- | ------ | ------ |
|                   |     |                     |        |            | wall position | controls | the | balance | between | outlet | purity |
from circular confinement into a finite continuous-flow andparticlerecovery, providingasimplegeometricalpa-
device, enabling robust and autonomous sorting of ac- rameter for tuning sorting performance.
tive particles.
|     |     |     |     |     | Finally,   | from the     | numerical       | exploration |              | and | insights   |
| --- | --- | --- | --- | --- | ---------- | ------------ | --------------- | ----------- | ------------ | --- | ---------- |
|     |     |     |     |     | gained,    | we created   | an experimental |             | self-sorting |     | device.    |
|     |     |     |     |     | We develop | a snake-like |                 | channel     | composed     |     | of succes- |
CONCLUSIONS
|     |     |     |     |     | sive curved | sorting      | units | and demonstrated |     |     | experimen-   |
| --- | --- | --- | --- | --- | ----------- | ------------ | ----- | ---------------- | --- | --- | ------------ |
|     |     |     |     |     | tally that  | an initially | mixed | population       |     | of  | rollers pro- |
We have demonstrated that collective demixing in bi- gressively segregates as it propagates through succes-
nary mixture of Quincke rollers can be harnessed as a sivecurvedunits, reachingahighlyenrichedstatedown-
physical mechanism for continuous sorting. Combining stream. These results establish a direct connection be-
experiments with particle-based simulations, we showed tween demixing in active systems and functional parti-
that differences in speed are sufficient to generate ro- cletransport,showingthatspontaneousself-organization

10
canbeengineeredintoapracticalcontinuous-flowsorting terials processing, particle selection, and biomedical ap-
mechanism. plications, including the controlled separation of motile
|     |     |     |     |     |     |     | cells or microorganisms. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
Morebroadly,thisworkopensnewpossibilitiesforde-
| signing   | technologies | that        | exploit | collective | segregation, |          |     |     |     |     |
| --------- | ------------ | ----------- | ------- | ---------- | ------------ | -------- | --- | --- | --- | --- |
| sort, and | transport    | microscopic |         | components | for          | specific |     |     |     |     |
ACKNOWLEDGMENTS
| tasks.    | Future      | devices | could      | harness dynamical |     | proper-  |     |     |     |     |
| --------- | ----------- | ------- | ---------- | ----------------- | --- | -------- | --- | --- | --- | --- |
| ties such | as motility | and     | collective | interactions      |     | together |     |     |     |     |
withcurvedconfinementgeometrytocontrolparticleor- We thank Samadarshi Maity for help with the exper-
ganization and transport. Such strategies may provide iments. We thank Joshua H. K. Saldi for insightful dis-
| new routes | toward | active | microfluidic | platforms |     | for ma- | cussions. |     |     |     |
| ---------- | ------ | ------ | ------------ | --------- | --- | ------- | --------- | --- | --- | --- |
[1] A.Rosato,K.J.Strandburg,F.Prinz,andR.H.Swend- [15] A. K. Harris, Journal of theoretical biology 61, 267
| sen, | Phys. Rev. | Lett. | 58, 1038 | (1987). |     |     | (1976). |     |     |     |
| ---- | ---------- | ----- | -------- | ------- | --- | --- | ------- | --- | --- | --- |
[2] C. Allain, M. Cloitre, and M. Wafra, Phys. Rev. Lett. [16] M. Krieg, Y. Arboleda-Estudillo, P.-H. Puech, J. Käfer,
74, 1478 (1995). F. Graner, D. Müller, and C.-P. Heisenberg, Nature cell
[3] L. Lei, S. Wang, X. Zhou, S. E. Ghellab, G. Lin, and biology 10, 429 (2008).
Y. Gao, Frontiers in Chemistry 10, 803906 (2022). [17] A. K. O’Neill, A. A. Kindberg, T. K. Niethamer, A. R.
[4] B. Cleuren and R. Eichhorn, arXiv preprint Larson, H.-Y. H. Ho, M. E. Greenberg, and J. O. Bush,
arXiv:2603.19430 (2026). Journal of Cell Biology 215, 217 (2016).
[5] B. M. Jones, P. M. Evans, and D. A. Lee, Experimental [18] A. A. Kindberg, V. Srivastava, J. M. Muncie, V. M.
Cell Research 180, 287 (1989). Weaver, Z. J. Gartner, and J. O. Bush, Journal of Cell
[6] C. P. Beatrici and L. G. Brunnet, Phys. Rev. E 84, Biology 220, e202005216 (2021).
031927 (2011). [19] M. Skamrahl, J. Schünemann, M. Mukenhirn, H. Pang,
[7] S. R. McCandlish, A. Baskaran, and M. F. Hagan, Soft J. Gottwald, M. Jipp, M. Ferle, A. Rübeling, T. A. Os-
Matter 8, 2527 (2012). wald, A. Honigmann, et al., Proceedings of the National
[8] M. S. Steinberg, Science 141, 401 (1963). Academy of Sciences 120, e2213186120 (2023).
[9] F. Graner and J. A. Glazier, Physical review letters 69, [20] E. F. Teixeira, C. P. Beatrici, H. C. M. Fernandes, and
2013 (1992). L. G. Brunnet, Phys. Rev. Lett. 134, 138401 (2025).
[10] J.A.GlazierandF.Graner,PhysicalReviewE47,2128 [21] M. Bothe, A. Poliakov, E. Lardet, G. Pruessner,
| (1993). |         |        |               |               |     |         | T. Bertrand, | and I. Bordeu, | Communications | Physics |
| ------- | ------- | ------ | ------------- | ------------- | --- | ------- | ------------ | -------------- | -------------- | ------- |
| [11] R. | A. Foty | and M. | S. Steinberg, | Developmental |     | biology | (2026).      |                |                |         |
278, 255 (2005). [22] S.N.Weber,C.A.Weber,andE.Frey,Phys.Rev.Lett.
[12] J.M.Belmonte,G.L.Thomas,L.G.Brunnet,R.M.C. 116, 058301 (2016).
deAlmeida,andH.Chaté,Phys.Rev.Lett.100,248702 [23] E. McCarthy, R. K. Manna, O. Damavandi, and M. L.
| (2008). |     |     |     |     |     |     | Manning, | Phys. Rev. Lett. | 132, 098301 (2024). |     |
| ------- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | ------------------- | --- |
[13] E.Méhes,E.Mones,V.Nemeth,andT.Vicsek,PloSone [24] S. Maity and A. Morin, Phys. Rev. Lett. 131, 178304
| 7, e31711 | (2012). |     |     |     |     |     | (2023). |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
[14] E. Mones, A. Czirók, and T. Vicsek, New journal of [25] L. Alvarez, E. Sesé-Sansa, D. Levis, I. Pagonabarraga,
physics 17, 063013 (2015). and L. Isa, arXiv preprint arXiv:2506.15188 (2025).
---- END DOCUMENT ----
