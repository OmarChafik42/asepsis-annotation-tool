Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Spatial spread of infection: transitions between pulled and pushed fronts
∗
Evgeniy Khain and Rohan Sukumar
Department of Physics, Oakland University, Rochester, MI 48309, USA
Weconsiderthespatialspreadofepidemicintoanunstable,healthystate. Whenthetransmission
ratedependsonthefractionofinfected,thepropagatingpulseofinfectioncanbeeitherapulledfront
orapushedfront. Wedetermined thephasespace of parameters forthepulled andpushedregions
bothbynumericallysolvingthespatialSIRpartialdifferentialequationsandbyatheoreticalanalysis
of the front propagation phenomenon. We found both a continuous and a discontinuous transition
betweenthepulledand pushedfront solutions; in thelatter transition, thefront speed undergoesa
jump as a certain parameter crosses the critical threshold. The behavior of the propagating pulses
nearthetransitionshasbeenanalyzedandagood agreement betweenthetheoryandnumericshas
been observed. Finally, a bistable region where both pushed and pulled propagating pulses can be
realized has been discovered.
PACSnumbers:
I. INTRODUCTION transmissionrateandinvestigatepulsesofinfectionprop-
agating into an unstable, healthy state. We find both
pushedandpulledfrontsindifferentregionsofthe phase
The phenomenon of front propagation is ubiquitous
diagramofparametersandinvestigatethetransitionsbe-
in nature, from the spread of invasive species [1] and
tween different front types. In addition to a continuous
cell migration [2] to flame fronts propagating in reac-
transition, we found discontinuous transitions and a re-
tive systems [3], spread of wildfires [4] and autocatalytic
gion of bistability.
chemicalwaves[5]. Significantresearchhasbeendonein-
vestigating fronts propagatinginto an unstable state [6].
Such fronts are divided into pulled fronts, for which the
II. THE MODEL
frontspeedisdeterminedbytheleadingedgeofthefront,
and pushed fronts that generally move faster and whose
dynamics are determined by the entire nonlinear front The spatial susceptible-infected-recovered model for
region [6]. A continuous transition between pulled and the fraction of susceptible S(x,t), infected I(x,t), and
pushed fronts has been observed when a governing pa- recoveredindividuals R(x,t) [9] is given by:
rameter(letusdenoteitbyµ)crossesacertainthreshold
µ=µ c [6,7],andnearthetransition,thefrontspeeddif- ∂S ∂2S
ferencec c hasbeenshowntoscalequadrat- = rSI+D , (1)
pushed − pulled ∂t − ∂x2
ically with the distance to this threshold value µ µ
| − c | ∂I ∂2I
[8]. = rSI αI+D ,
∂t − ∂x2
Analysis of propagating pulses of infection in the
∂R ∂2R
framework of the basic Susceptible-Infected-Recovered
= αI +D .
(SIR) model is a famous textbook problem [9]. The lin- ∂t ∂x2
earized equation for the fraction of infected is analogous Inthestandardsetting,thetransmissionrateristaken
to the linearized Fisher-Kolmogorov equation [10, 11],
to be constant. However,there are indications that pub-
and the corresponding fronts move with the speed of
lichealthmeasuresresultinalowertransmissionratefor
c0 =2D√r
−
α, where D is the diffusion coefficient, r is
a smaller fraction of infected and a higher transmission
the transmission rate and α is the recovery rate. When
rate for a larger fraction of infected [12]. Assuming that
r > α, the state of no infection is linearly unstable, so
r varies between r = r for low I to r = r > r
the propagating pulse of infection is a pulled front mov- min max min
for high I, this dependence can be modeled as [13]
ing into an unstable state. Are there pushed fronts of
infection moving into an unstable state? I
r(I)=r +(r r ) .
There are indications that the transmission rate may min max − min I¯+I
notbeaconstant,butafunctionofafractionofinfected
[12]. We have recently considered the SIR model with Note that Ref. [13] considered the case r min <α, where
a modified (nonlinear) transmission rate and analyzed the state of no epidemic S = 1, I = 0 was stable, and
fronts propagating into a linearly stable state of no in- the problem of front propagation into a stable state has
fection [13]. In this work, we adapt the same modified been examined. This research assumes r min > α and
investigatesthespatialpropagationofapulseofinfection
into an unstable (healthy) state.
Let us now introduce the dimensionless coordinate
∗Electronicaddress: khain@oakland.edu x¯ = α/Dx and the dimensionless time t¯= αt. The
p
6202
luJ
62
]EP.oib-q[
1v82732.7062:viXra

2
equationsforthefractionsofinfectedandsusceptiblebe- thatthe borderbetweenthe tworegionscontinuestothe
| come |     |     |     |     |     |     |     | r¯ <1 | part | of the | diagramwhere |     | pulled | fronts | do not |
| ---- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------ | ------------ | --- | ------ | ------ | ------ |
min
|     |     |     |     |     |     |     |     |             |        |       |               |       | (I¯> | I¯),            |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ----- | ------------- | ----- | ---- | --------------- | ------ |
|     |     |     |     |     |     |     |     | exist.      | There, | above | the threshold |       |      | c the initially |        |
|     |     |     |     |     |     |     |     | propagating |        | pulse | of infection  | slows | down | and             | decays |
|     |     | ∂S  |     |     | ∂2S |     |     |             |        |       |               |       |      |                 |        |
[13]. Intheoppositelimit,thepushedfrontregiondisap-
|     |     |     | =      | r¯SI + | ,    |     | (2) |                  |        |               |              |           |          |           |      |
| --- | --- | --- | ------ | ------ | ---- | --- | --- | ---------------- | ------ | ------------- | ------------ | --------- | -------- | --------- | ---- |
|     |     | ∂t¯ | −      |        | ∂x¯2 |     |     | pears            | as r¯  | tends         | to r¯        | . Indeed, | when     | r¯ =r¯    | ,    |
|     |     |     |        |        |      |     |     |                  | min    |               | max          |           |          | min       | max  |
|     |     | ∂I  |        |        | ∂2I  |     |     |                  |        |               |              |           | ¯        |           |      |
|     |     |     |        |        |      |     |     | the transmission |        | rate          | is constant, |           | r( I)=r¯ | max , and | only |
|     |     |     | = r¯SI | I+     |      | ,   |     |                  |        |               |              |           |          |           |      |
|     |     | ∂t¯ |        | −      | ∂x¯2 |     |     | pulled           | fronts | can propagate |              | in the    | system.  |           |      |
where
I
|     | r¯=r¯ |     | +(r¯ |     | r¯ ) |      | (3) |     |     |     |     |     |     |     |     |
| --- | ----- | --- | ---- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |       | min |      | max | min  | I¯+I |     |     |     |     |     |     |     |     |     |
−
| with r¯    | =   | r /α | and     | r¯ =  | r         | /α. Throughout |          |     |     |     |     |     |     |     |     |
| ---------- | --- | ---- | ------- | ----- | --------- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| min        |     | min  |         | max   | max       |                |          |     |     |     |     |     |     |     |     |
| this work, | we  | will | fix the | value | of r¯ max | and            | vary the |     |     |     |     |     |     |     |     |
I¯.
| remaining | two | parameters: |     | r¯  | >1 and | As  | we show |     |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | --- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
min
| below, | the propagating |     | pulse | of infection |     | can be | either a |     |     |     |     |     |     |     |     |
| ------ | --------------- | --- | ----- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
pulledfrontorapushedfrontdependingonthevaluesof
| these two       | parameters. |                  |               |              |               |                    |          |                                           |       |       |                |     |            |              |      |
| --------------- | ----------- | ---------------- | ------------- | ------------ | ------------- | ------------------ | -------- | ----------------------------------------- | ----- | ----- | -------------- | --- | ---------- | ------------ | ---- |
| III.            | PHASE       | DIAGRAM          |               | OF           | PARAMETERS:   |                    |          |                                           |       |       |                |     |            |              |      |
|                 | PULLED      |                  | AND           | PUSHED       | REGIONS       |                    |          |                                           |       |       |                |     |            |              |      |
| The             | speed       | of pulled        | fronts        | can          | be            | computed           | theo-    |                                           |       |       |                |     |            |              |      |
| retically,      | as          | it is determined |               | by           | the precursor |                    | and can  |                                           |       |       |                |     |            |              |      |
| be found        | from        | the              | linearization |              | near          | the infection-free |          |                                           |       |       |                |     |            |              |      |
|                 |             |                  |               |              |               |                    |          | FIG. 1:                                   | Phase | plane | of parameters: |     | the border | between      | the  |
| I = 0           | state.      | Indeed,          |               | substituting |               | the front          | ansatz   |                                           |       |       |                |     |            |              |      |
|                 |             | ct¯)             |               |              |               |                    |          | regionsofpulledandpushedfronts,r¯max      |       |       |                |     | =2.8.      | Blackcircles |      |
| I = I(ξ         | = x¯        | and              | linearizing   |              | the           | resulting          | equation |                                           |       |       |                |     |            |              |      |
|                 |             | −                |               |              |               |                    |          | arecomputedfromthenumericalsolutionofEqs. |       |       |                |     |            | (2-3).       | Blue |
| in the vicinity |             | of I             | =0 (S         | =1) state,   | we            | get:               |          |                                           |       |       |                |     |            |              |      |
squaresarecomputedbyemployingthe“shooting”numerical
|         |       |                       |         |     |     |            |      | procedure, | see | text.    |         |     |            |     |        |
| ------- | ----- | --------------------- | ------- | --- | --- | ---------- | ---- | ---------- | --- | -------- | ------- | --- | ---------- | --- | ------ |
|         |       | dI                    |         |     | d2I |            |      |            |     |          |         |     |            |     |        |
|         |       | c                     | =r¯ min | I   | I + | .          |      |            |     |          |         |     |            |     |        |
|         |       | − dξ                  |         | −   | dξ2 |            |      |            |     |          |         |     |            |     |        |
|         |       |                       |         |     |     |            |      | Figure     | 2   | shows an | example | of  | the pulled | and | pushed |
| One can | see a | mechanicalanalogywith |         |     |     | the damped | har- |            |     |          |         |     |            |     |        |
monic oscillator, where the front speed plays a role of front profiles for both the fraction of infected (Fig. 2a)
the damping coefficient. For small damping (small front and the fraction of susceptible (Fig. 2b). As the tran-
|          |     |       |                 |     |       |       |           | sition | across | the border | between |     | the pulled | and | pushed |
| -------- | --- | ----- | --------------- | --- | ----- | ----- | --------- | ------ | ------ | ---------- | ------- | --- | ---------- | --- | ------ |
| speed c) | the | decay | is oscillatory, |     | which | means | that I(ξ) |        |        |            |         |     |            |     |        |
regionscanbediscontinuous,thepulledandpushedfront
| will decay | to  | zero in | an oscillatory |     | manner, | so  | the frac- |     |     |     |     |     |     |     |     |
| ---------- | --- | ------- | -------------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tion of infected will inevitably become negative for cer- profiles can be remarkably different. In the pushed case
|             |              |          |        |               |     |            |          | (black | dash-dotted |      | lines),   | the amplitude |           | of the infection |     |
| ----------- | ------------ | -------- | ------ | ------------- | --- | ---------- | -------- | ------ | ----------- | ---- | --------- | ------------- | --------- | ---------------- | --- |
| tain values | of           | ξ, which | is     | not allowed.  |     | Therefore, | there    |        |             |      |           |               |           |                  |     |
|             |              |          |        |               |     |            |          | pulse  | is higher   | (and | therefore | the           | remaining | fraction         | of  |
| should      | be a minimal |          | speed, | corresponding |     | to the     | critical |        |             |      |           |               |           |                  |     |
damping in our mechanical analogy. As in many other susceptibleislower)andthepulsedecaysfastercompared
pulled front systems, sharp enough initial conditions de- to the pulled case (blue solid lines).
| velop in      | this   | case into | a pulse | of    | infection | moving | with |     |     |     |     |     |     |     |     |
| ------------- | ------ | --------- | ------- | ----- | --------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| this critical | speed: |           | c       | =2√r¯ |           | 1.     |      |     |     |     |     |     |     |     |     |
|               |        |           | pulled  |       | min −     |        |      |     |     |     |     |     |     |     |     |
The numerical solution of Eqs. (2-3) in MATLAB IV. THEORY OF FRONT PROPAGATION
| shows that | after | a   | short transient, |     | the | profiles | of S and |     |     |     |     |     |     |     |     |
| ---------- | ----- | --- | ---------------- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
I develop into fronts moving with a constant speed c. Inordertobetterunderstandthebehaviorofthefront
It is known that pushed fronts generally move faster speedneartheborderbetweenthe pulledandpushedre-
c pushed > c pulled . Therefore, for every set of parame- gions, we employ a semi-theoretical approach. First, we
ters, one can compare the resulting front speed with the substitute the front propagation ansatz I = I(ξ) and
value of c and decide if this is a pulled or a pushed S = S(ξ) into Eqs. (2) and rewrite the two result-
pulled
front. The resulting “pulled” and “pushed” regions on ing equations as a four-dimensional dynamical system
I¯)
the (r¯ min , phase plane are shown in Figure 1. The for S, u = dS/dξ, I, and v = dI/dξ. The front pro-
borderbetweentheregionsisshownbothbyblackcircles filecorrespondstothetrajectoryinthisfour-dimensional
computed from the numerical solution of Eqs. (2-3) and space connecting the state before the epidemic (S = 1,
by blue squares computed by employing the “shooting” u = 0, I = 0, v = 0) with the state after the epidemic
numerical procedure (see the next section). Note also (S =S ,u=0,I =0,v =0). Findingthistrajectory
final

3
|     |     |     |     |     |     |     | where     | δS = | S      | S∗, and | S∗     | = S   | (when  | considering |         |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------ | ------- | ------ | ----- | ------ | ----------- | ------- |
|     |     |     |     |     |     |     |           |      | −      |         |        | final |        |             |         |
|     |     |     |     |     |     |     | the state | left | behind | the     | front) | or    | S∗ = 1 | (when       | consid- |
(a)
|     |     |     |     |     |     |     | ering | the state | the | front | propagates |     | to). |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ----- | ---------- | --- | ---- | --- | --- |
0.06
|     |     |     |     |     |     |     | First, | we  | analyze | the  | behavior |        | of I and  | S near | the    |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------- | ---- | -------- | ------ | --------- | ------ | ------ |
|     |     |     |     |     |     |     | (S =   | S   | , I     | = 0) | fixed    | point. | Demanding |        | that S |
final
|     |     |     |     |     |     |     | approachesS |     | final | andI | approaches0asξtendstominus |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ---- | -------------------------- | --- | --- | --- | --- |
0.04 infinity, we find the approximate solution in the vicinity
| I   |     |     |     |     |     |     | of the | (S =S |     | , I =0) | state: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | ------- | ------ | --- | --- | --- | --- |
final
|      |     |     |     |     |     |     |     |        |       |     | r¯  | S        |          |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | -------- | -------- | --- | --- |
| 0.02 |     |     |     |     |     |     |     |        |       | +d¯ | mi  | n f i    | n al     |     |     |
|      |     |     |     |     |     |     |     | S(ξ)=S |       |     |     |          | exp(λ+ξ) |     |     |
|      |     |     |     |     |     |     |     |        | final |     | (c+ | λ +) ( λ | )2       |     |     |
+
|     | 0   |     |     |     |     |     | and |     |     |       |     |           |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --------- | --- | --- | --- |
|     |     | 60  |     | 80  | 100 |     |     |     |     |       | d¯  |           |     |     |     |
|     |     |     |     |     |     |     |     |     |     | I(ξ)= |     | exp(λ+ξ), |     |     |     |
λ+
whered¯is
|     |     |     |     |     |     |     |     |     | anarbitrary(small)constantandthe |     |     |     |     | relevant |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | -------- | --- |
1
|     |     |     |     |     |     |     | eigenvalue |     | is  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
(b)
c2/4+1
|     |     |     |     |     |     |     |       | λ+         | =      | c/2+         | q      |       | r¯ min S | final .      |       |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ------ | ------------ | ------ | ----- | -------- | ------------ | ----- |
| 0.8 |     |     |     |     |     |     |       |            | −      |              |        | −     |          |              |       |
|     |     |     |     |     |     |     | Next, | we         | study  | the behavior |        | of I  | and S    | near the     | (S =  |
| S   |     |     |     |     |     |     | 1, I  | = 0) fixed | point. |              | Again, | there | are four | eigenvalues: |       |
| 0.6 |     |     |     |     |     |     |       |            |        |              |        |       | c2/4+1   |              |       |
|     |     |     |     |     |     |     | λ1 =  | 0, λ2      | =      | c, λ3        | = c/2+ |       |          | r¯ min       | , and |
|     |     |     |     |     |     |     |       |            | −      |              | −      | p     |          | −            |       |
|     |     |     |     |     |     |     | λ4 =  | c/2        | c2/4+1 |              | r¯     | . The | general  | solution     | in    |
min
|     |     |     |     |     |     |     |                | −       | −p                              |     | −        |         |             |         |        |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ------------------------------- | --- | -------- | ------- | ----------- | ------- | ------ |
|     |     |     |     |     |     |     | thevicinityofI |         | =0isI(ξ)=A3exp(λ3ξ)+A4exp(λ4ξ). |     |          |         |             |         |        |
| 0.4 |     |     |     |     |     |     | This           | general | solution,                       |     | however, | is      | realized    | neither | for    |
|     |     |     |     |     |     |     | pushed         | fronts, | nor                             | for | pulled   | fronts. | Indeed,     | for     | pushed |
|     |     |     |     |     |     |     | fronts,the     |         | steepestpossible                |     | frontis  |         | chosenandas |         | λ4 >   |
|     |     | 60  |     | 80  | 100 |     |                |         |                                 |     |          |         |             |         |        |
| |
|     |     |     |     |     |     |     | λ3 ,        | A3 = | 0 (our | numerical |     | observations |     | support | this |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | --------- | --- | ------------ | --- | ------- | ---- |
|     |     |     |     |     |     |     | | |         |      |        |           |     |              |     |         |      |
|     |     |     |     |     |     |     | statement). |      | As a   | result,   |     |              |     |         |      |
FIG.2: Thefractionofinfected(a)andthefractionofsuscep- I(ξ)=A4exp(λ4ξ)
| tible (b): | pulled | and pushed | front    | profiles. | The parameters |      |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ---------- | -------- | --------- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| r¯min      | 1.06,  | r¯max      | 2.8, I¯= | 0.0800    |                |      | and |     |     |     |     |     |     |     |     |
| are        | =      | =          |          |           | (pulled front, | blue |     |     |     |     |     |     |     |     |     |
I¯=
| solid line) | and | 0.0745 | (pushed | front, | black dash-dotted |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r¯ min
| line). |     |     |     |     |     |     | S(ξ)=1+A4 |       |       |          |        | exp(λ4ξ)+A |     | exp( | cξ).   |
| ------ | --- | --- | --- | --- | --- | --- | --------- | ----- | ----- | -------- | ------ | ---------- | --- | ---- | ------ |
|        |     |     |     |     |     |     |           |       |       | (c+λ4)λ4 |        |            |     | c −  |        |
|        |     |     |     |     |     |     | On the    | other | hand, | for      | pulled | fronts,    | λ3  | = λ4 | λ0, so |
≡
|                |     |                                   |     |        |       |         | solution    | is           | written | in          | the form | I(ξ)           | =   | A1ξexp(λ0ξ) | +      |
| -------------- | --- | --------------------------------- | --- | ------ | ----- | ------- | ----------- | ------------ | ------- | ----------- | -------- | -------------- | --- | ----------- | ------ |
| is challenging |     | as the values                     | of  | both S | and c | are un- |             |              |         |             |          |                |     |             |        |
|                |     |                                   |     |        | final |         | A0exp(λ0ξ), |              | where   | A1          | must     | be nonnegative |     | to          | ensure |
| knownapriori.  |     | Tomakeprogress,weanalyzethesystem |     |        |       |         |             |              |         |             |          |                |     |             |        |
|                |     |                                   |     |        |       |         | that        | the fraction |         | of infected |          | individuals,   |     | I, remains  | non-   |
behaviornearthetwostatesandthenemployaso-called
negative.
| “shooting” | numerical | procedure. |      | Linearizing | the       | system |             |          |               |        |                 |               |             |             |        |
| ---------- | --------- | ---------- | ---- | ----------- | --------- | ------ | ----------- | -------- | ------------- | ------ | --------------- | ------------- | ----------- | ----------- | ------ |
|            |           |            |      |             |           |        | A           | standard | “shooting”    |        | numerical       |               | procedure   |             | is em- |
| near the   | states    | (S =S∗,    | u=0, | I =0,       | v =0), we | obtain |             |          |               |        |                 |               |             |             |        |
|            |           |            |      |             |           |        | ployed      | to find  | I(ξ)          | and    | S(ξ)            | that satisfy  |             | the desired | be-    |
|            |           |            |      |             |           |        | haviorinthe |          | vicinityofthe |        | twofixedpoints. |               |             | Inaddition  |        |
|            |           |            |      |             |           |        | to the      | profiles | of            | I and  | S,              | the procedure |             | provides    | val-   |
|            | d(δS)     |            |      |             |           |        | ues for     | the      | two a         | priori | unknown         |               | parameters: | the         | front  |
|            |           | =          | u    |             |           | (4)    |             |          |               |        |                 |               |             |             |        |
|            |           | dξ         |      |             |           |        | speed       | c and    | the fraction  |        | of susceptible  |               | S           | behind      | the    |
final
|     |     |     |     |     |     |     | front. | The | phase | diagram |     | presented | in  | Fig. 1 | shows |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----- | ------- | --- | --------- | --- | ------ | ----- |
du
= cu+r¯ S∗I t h a t fo r a fi x ed v a lu e o f r¯ , a t r a n s i ti o n f r o m p u l le d t o
|     |     |     |     | min |     |     |          |        |           |          | m i n  |            |           |              |             |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | -------- | ------ | ---------- | --------- | ------------ | ----------- |
|     |     | dξ  | −   |     |     |     |          |        |           |          | ¯      |            |           |              |             |
|     |     |     |     |     |     |     | p u s he | d r eg | io n so c | c u rs a | s I is | d ec r e a | s e d . I | t t u r ns o | u t t h a t |
dI
|     |     |     |     |     |     |     | this      | transition | can | be      | either | continuous |     | (for r¯ | above  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | ------ | ---------- | --- | ------- | ------ |
|     |     | =   | v   |     |     |     |           |            |     |         |        |            |     | min     |        |
|     |     | dξ  |     |     |     |     | a certain | critical   |     | value), | where  | c          | =   | c       | at the |
|     |     |     |     |     |     |     |           |            |     |         |        | pushed     |     | pulled  |        |
dv transition point, or discontinuous (for r¯ m in below that
|     |     | =   | cv  | r¯ S∗I | +I, |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dξ − − min critical value), where the front speed und er goes a jump.

4
A. Continuous transition between pulled and
pushed fronts
Both the numerical solution of the time dependent
equations (1) and the “shooting” numerical procedure
employed to solve equations (4) show that for a fixed
value of r¯ pulled fronts exist for I¯>I¯ with the frac- min c
tionofinfectedgivenbyI(ξ)=A1ξexp(λξ)+A0exp(λξ).
Below that threshold, the fronts are pushed and move
with a larger speed, c pushed >c pulled . The coefficient A1
is positive for the pulled region and becomes zero at the
transition point [6]. This is quite intuitive as A1 = 0
corresponds to the steepest possible pulled front.
Figure3showsacontinuoustransitionbetweenthetwo
front types: the speed of front propagation(blue circles)
as a function of I¯for the fixed value of r¯ . One can
min observe a plateau for I¯>I¯ (the front speed is indepen-
c dent of I¯in the pulled region) and an increasing speed
for I¯< I¯ (the pushed region). Near the transition (for
c smallvaluesofǫ=I¯ I¯),thefrontspeedcanbeapprox-
c
imatedbyc =c − +βǫ2 [8]. Thisapproximation
pushed pulled
is shown in Figure 2 by the blue dotted line, while the
plateau for I¯> I¯ is shown by the red dashed line. Let
c
us now derive this scaling and obtain the value of β.
1.72
1.7
1.68
1.66
0.05 0.1 0.15 0.2
c
where
1
δ
≡
λ0
−
λ4 =
2(cid:16)
c
−
c
pulled
+
q
c2
−
c2
pulled(cid:17)
.
Assuming a small δ and expanding the exponent, we
get A4 = A0 and A4δ = A1, so δ2 = (c pulled /2)(c
c )=(α2/A2)ǫ −2 and − pulled 0
2α2
c=c + ǫ2.
pulled A2c 0 pulled
The coefficient in front of ǫ can be obtained from the
“shooting” numerical procedure for pulled fronts. In-
deed,theratiov(ξ)/I(ξ)decreaseswithξasλ0+A1/A0
(A1/A0)2ξ. We computed the slope (A1/A0)2 above th − e
transition, verified the scaling with ǫ and computed the
coefficient β = (2α2)/(A2c ). Figure 3 shows an ex- 0 pulled
cellentagreementofthistheoreticalscaling(thebluedot-
ted line) with the observed front speed near the transi-
tion.
B. Discontinuous transition between pulled and
pushed fronts
While Fig. 3 shows a continuous transition between
the speeds of pulled and pushed fronts, for smaller val-
uesofr¯ ,thetransitionisdiscontinuous,andthefront
min
speed undergoes a jump, see Fig. 4. Above the critical
value of I¯(I¯> I¯), the pulled front is the only existing
c
solution (the theoretical black dash-dotted line), while
below the threshold (I¯ < I¯), there are two additional
c
pushedfrontbranches,shownbythe redcircles(astable
branch) and the blue circles (an unstable branch) and
computed employing the “shooting” numerical proce-
dure. Figure4 showsthatthe pushed frontbranchesun-
dergo a saddle-node bifurcation, which means that near
the transition(for smallvaluesofǫ=I¯ I¯),the pushed
c
−
front speed of the stable branch (the red solid line) is
given by c =c +Bǫ1/2 (c = c Bǫ1/2
pushed crit pushed crit
− for the unstable branch, the blue dotted line).
Totheoreticallyderivethisapproximation,wefocuson
the pushed front solution. While the general solution is
FIG.3: Continuoustransition: FrontspeedasafunctionofI¯. given by I(ξ) = A3exp(λ3ξ)+A4exp(λ4ξ), for pushed
The pushed front asymptotics is given by c pushed =c pulled+ frontsfor anyfixedr¯ min ,the coefficientA3(c,I¯) mustbe
β(I¯ c −I¯)2,thebluedottedline,seetext. Theparametersare: equal to zero. For a saddle-node bifurcation, near the
r¯min =1.7, r¯max =2.8, β ≃10.714, I¯
c
≃0.127. transition,
A3 = B1(c c
crit
)2+B2(I¯
c
I¯).
− − −
As A1 = 0 for I¯= I¯ c , it generally should be propor- This behavior is verified in Fig. 5. The “shooting” nu-
tional to ǫ near the transition, A1 = α(I¯
−
I¯ c ). We now merical procedure allows computing A3 for any value of
employ a perturbation theory (valid at small ǫ), assum- c and I¯just by following the largeξ limit of the product
ingthatthepushedfrontsolutionisapproximatelyequal I(ξ)exp( λ3ξ). Figure 5 shows the coefficient A3 as a
to the (non realized) pulled front solution with a small function − of c for three values of I¯: below the transition
negative value of A1: (blackcircles,tworoots),(almost)atthetransition(blue
squares, a single root), and above the transition (ma-
gentadiamonds,noroots). Afitto allthree curvesgives
A4exp((λ0 δ)ξ)=A1ξexp(λ0ξ)+A0exp(λ0ξ), c
crit
= 0.729, I¯
c
= 0.07491, B1 = 0.0765, and B2 = 0.5.
−

5
Demanding A3 =0 produces c
pushed
(ǫ), shown in Fig. 4
by the red solid line for a stable branch and by the blue
dotted line for an unstable branch.
1.2
1
0.8
0.6
0.4
0.05 0.06 0.07 0.08 0.09 0.1
c
FIG.4: ThefrontspeedasafunctionofI¯forr¯min belowthe
critical threshold: a discontinuous transition. The circles are
computedbyemployingthe“shooting” numericalprocedure,
whiletheredsolid lineandthebluedottedlinerepresentthe
theoreticalapproximationnearthebifurcation,seetext. The
black dash-dotted line describes the theoretical pulled front
speed. r¯min =1.04, r¯max =2.8.
0.5
0
-0.5
-1
-1.5
-2
-2.5
0.65 0.7 0.75 0.8
c
A
3
1 discontinuous
transition
0.8
0.6
0.4 continuous
transition
0.2
0
1 1.1 1.2
FIG.6: Thepushedandthepulledfrontspeedsasafunction
of r¯min along theborder(and from both sides of theborder)
of thephase diagram (Fig. 1). Red circles denote the speeds
of the pushed fronts, while black squares denote the speeds
of thepulled fronts ascomputed from thenumericalsolution
of Eqs. (1). The theoretical pulled front speed is shown by
the blue solid line. The vertical dotted line at r¯c = 1.076
separates the regions of discontinuous (left) and continuous
(right) transitions. r¯max =2.8.
V. BISTABILITY
Figure6illustratesboththecontinuousanddiscontin-
10-4
uoustransitionsshowingthepushedandthepulledfront
speeds as a function of r¯ along the border (and from
min
both sides of the border) of the phase diagram (Fig. 1).
The blue solid line corresponds to the theoretical pulled
frontspeed,c =2√r¯ 1. Thesymbolsarecom-
pulled min
−
putedfromthenumericalsolutionofEqs. (1): redcircles
denote the pushed front speed, while black squares de-
note the speeds of the pulled fronts. The vertical dotted
line r¯ = r¯ = 1.076 divides the diagram into two
min c
regions. The region on the right corresponds to the con-
tinuum transition, so both the pushed and pulled front
speed along the border equal to c . The region on
pulled
the left correspondsto a discontinuous transition, so the
frontspeedjumps fromc to c asI¯crossesthe
pulled pushed
critical threshold for the fixed r¯ as shown in Fig. 1.
min
Let us focus on the r¯ < r¯ region in more detail.
min c
Figure 4 shows that the pushed front solution does not
FIG.5: A3,thecoefficient in front oftheslowly decayingex- existforI¯>I¯
c
,butbelowthisthresholdboththe pulled
ponent, as a function of c for three values of I¯. The pushed andpushedfrontsdoformallyexist. Thenumericalsolu-
front solution requires A3 = 0, therefore, one can observe a tion of Eqs. (1) with initial conditions I(x,t=0)=0.06
saddle-node bifurcation as I¯is varied. I¯=0.0748 (black cir-
for x < 0 and I(x,t = 0) = 0 for x > 0 shows that the
cles), I¯ = 0.0749 (blue squares), and I¯ = 0.0750 (magenta
transient dynamics always lead to a pushed front. How-
diamonds). r¯min =1.04, r¯max =2.8, seetextforthetheoret-
ever the basin of attraction of the pulled front solution
ical fit (dotted lines).
can be small but nonzero. To test this hypothesis, we
startedthenumericalsimulationsinthepulledregionfor
I > I¯, followed the transient dynamics that leads to a
c

6
I¯<I¯.
pulled front and then switched to Quite remark- front speed undergoes a jump, so c > c at
|     |     |     |     | c   |     |     |     |     | pushed | pulled |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- |
ably,wedidfindthepulledfrontsolutionwhentheswitch the transition. In addition, we discovered a region of
∆I¯was
not too big. It means that one can realize both bistability, where depending on initial conditions, both
the pushed front solution and the pulled front solution the pushed front and the pulled front can be realized for
for the same set of parameters! The region of bistability the same governing parameters. Our numerical results
inthe(r¯ I¯)phasediagramistoosmalltobeshownin computed by solving the system of partial differential
min
Fig. 1. For example, for r¯ min =1.076 in the discontinu- equationsfullyagreewithourtheoreticalresultsobtained
ous region (see Figs. 1 and 6), the pushed front solution from the analysis of the front propagationproblem.
does not exist for I¯ > 0.080, so there are only pulled The phenomena discussedin this workresultfrom the
fronts in this region of parameters. Only pushed front dependence of the transmission rate on the fraction of
|     |     | I¯< |     |     |     | I¯= |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
solutions are realized for 0.075, but one can obtain infected. If 0, the transmission rate is constant and
both propagating pulled and pushed pulses of infection equalsits maximumvalue, r =r . Inthe model, pub-
max
| in the interval | 0.075 < | I¯< 0.080. | These | two | fronts are |                     |      |              | I¯, |           |      |
| --------------- | ------- | ---------- | ----- | --- | ---------- | ------------------- | ---- | ------------ | --- | --------- | ---- |
|                 |         |            |       |     |            | lic health measures | lead | to a nonzero |     | resulting | in a |
entirely different: they move with different speeds and smaller transmission rate in the beginning of the epi-
theamplitudeofthepulseofinfectioninthepushedcase demics. Although the epidemic outbreak (the pulse of
is much larger compared to that in the pulled case. infected) will propagate through the system for any I¯,
I¯corre-
|     |     |     |     |     |     | the phase diagram | in Fig.     | 1 shows   | that   | larger |        |
| --- | --- | --- | --- | --- | --- | ----------------- | ----------- | --------- | ------ | ------ | ------ |
|     |     |     |     |     |     | spond to pulled   | fronts that | propagate | slower | and    | infect |
VI. SUMMARY AND DISCUSSION a smaller fraction of the population. The difference can
|     |     |     |     |     |     | be quite striking | in the | discontinuous | transition | region, |     |
| --- | --- | --- | --- | --- | --- | ----------------- | ------ | ------------- | ---------- | ------- | --- |
Weinvestigatedthepropagationofapulseininfection see Fig. 2. Although this is clearly a toy model and we
into an unstable, healthy state in the framework of the do not know how exactly the transmission rate depends
SIRepidemiologicalmodelwithanonlineartransmission on the fraction of infected, the qualitative result is quite
I¯)
rate. Initial outbreak develops to a propagating front, encouraging: public health measures (which increase
which can be either pulled or pushed depending on the can be quite helpful.
regimeofparameters. Wepresentedtheentirephasedia- An interesting avenue of future research is investigat-
gramofparametersidentifyingthepulledandpushedre- ing the role of stochastic fluctuations in this system due
gionsandstudiedthe transitionsbetweenthe pulled and tointrinsicshotnoisethatisknowntoaffectfrontpropa-
pushedfrontsolutions. Weobservedboththecontinuous gation [14]. These fluctuations can be very important in
transition,where c pushed =c pulled at the criticalvalue of the bistability regionofthe phasediagramandgenerally
a parameter, and a discontinuous transition, where the produce corrections to the front speed [15].
[1] M. Kot, M. A.Lewis, and P. van den Driessche, Ecology [8] M. Avery, M. Holzer, and A. Scheel, J. Nonlinear Sci.
| 77, 2027-2042 | (1996); | A. Hastings | et  | al, Ecol. | Lett. 8 | 33, 102 (2023). |     |     |     |     |     |
| ------------- | ------- | ----------- | --- | --------- | ------- | --------------- | --- | --- | --- | --- | --- |
91-101, (2005). [9] J.D.Murray,Mathematical Biology,Springer,NewYork
| [2] P.K.Maini,D.L.SMcElwain,D.Leavesley,Appl.Math. |     |     |     |     |     | (2002). |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Lett. 17, 575-580 (2004); M. J. Simpson, C. Towne, D. [10] R. A.Fisher, Ann. Eugen. 7, 355 (1937).
L. S. McElwain and Z. Upton, Phys. Rev. E 82, 041901 [11] A. N. Kolmogorov, I. G. Petrovsky,and N.S. Piskunov,
(2010);E.Khain,M.Katakowski,N.Charteris,F.Jiang, Bull. Moscow State Univ. Ser. A: Math. Mech. 1, 1
| and M. | Chopp, Phys. | Rev. E | 86, 011904 | (2012); | M. El-  | (1937). |     |     |     |            |     |
| ------ | ------------ | ------ | ---------- | ------- | ------- | ------- | --- | --- | --- | ---------- | --- |
|        |              |        |            | Phys.   | D: Non- |         |     |     |     | A´.Cabana, |     |
Hachem, S. W. McCue, M. J. Simpson, [12] M. Arim,D.Herrera-Esposito, P.Bermolen,
linear Phenom. 428, 133026, (2021); E. Khain and J. M. I. Fariello, M. Lima, and H. Romeroa, J Theor Biol.
Straetmans, J. Stat. Phys. 184, 20 (2021). 542, 111109 (2022).
[3] F.Lam,X.C.Mi,A.J.Higgins,Phys.Rev.E96,013107 [13] E. Khain,Phys. Rev. E107, 064303 (2023).
| (2017). |     |     |     |     |     | [14] E.BrunetandB.Derrida,Phys. |     |     | Rev.E56,2597(1997); |     |     |
| ------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | ------------------- | --- | --- |
[4] X. Shi, M. Faizal, A. Shabir, B. Pourhassan, Phys. Rev. B.Meerson,P.V.Sasorov,andY.Kaplan,Phys. Rev. E
E113, 064143 (2026). 84, 011147 (2011); G. Birzu, O. Hallatschek, and K. S.
[5] J.Martin,N.Rakotomalala,D.Salin,andM.B¨ockmann, Korolev, PNAS 115, E3645 (2018).
Phys. Rev. E 65, 051605 (2002). E.Khain,Y.T.Lin,L.M.Sander,EPL93,28001(2011);
[15]
| [6] W. vanSaarloos, | Phys.            | Rep. 386,     | 29–222 | (2003). |             |                |                |          |          |        |     |
| ------------------- | ---------------- | ------------- | ------ | ------- | ----------- | -------------- | -------------- | -------- | -------- | ------ | --- |
|                     |                  |               |        |         |             | E. Khain       | andB. Meerson, | J. Phys. | A: Math. | Theor. | 46, |
| [7] C-H. Wang,      | S. Matin,        | A. B. George, |        | and K.  | S. Korolev, |                |                |          |          |        |     |
|                     |                  |               |        |         |             | 125002 (2013). |                |          |          |        |     |
| Theor.              | Popul. Biol.127, |               |        |         |             |                |                |          |          |        |     |
102-119 (2019).
---- END DOCUMENT ----
