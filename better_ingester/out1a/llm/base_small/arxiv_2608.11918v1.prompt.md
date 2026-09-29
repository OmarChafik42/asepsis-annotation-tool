Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
A multiscale theory based on metabolic scaling connects forest dynamics to tree-size
distributions
|     |     | Christian |     | Grilletta,1 | Tommasso |     | Anfodillo,2 |     | Gaia | Pasqualotto,2,3 |     | Samir |     |     |     |
| --- | --- | --------- | --- | ----------- | -------- | --- | ----------- | --- | ---- | --------------- | --- | ----- | --- | --- | --- |
Suweis,1,4 Andrea Rinaldo,5,6,∗ Amos Maritan,1,3,4,† and Davide Bernardi1,3,4,‡
1LaboratoryofInterdisciplinaryPhysics,DepartmentofPhysicsandAstronomy“G.Galilei”,UniversityofPadova,Padova,Italy
|     |     |     |        | 2Department | TESAF,       | University |        | of Padova, |          | Padova, | Italy |       |     |     |     |
| --- | --- | --- | ------ | ----------- | ------------ | ---------- | ------ | ---------- | -------- | ------- | ----- | ----- | --- | --- | --- |
|     |     |     |        | 3National   | Biodiversity |            | Future | Center,    | Palermo, |         | Italy |       |     |     |     |
|     |     |     | 4INFN, | Sezione     | di           | Padova,    | via    | Marzolo    | 8, 35131 | Padova, |       | Italy |     |     |     |
5Department of Civil, Environmental and Architectural Engineering, University of Padova, Padova, Italy
|     |     | 6CMCC |     | Centro Euro-Mediterraneo |     |     | sui | Cambiamenti |     | Climatici, | Lecce, | Italy |     |     |     |
| --- | --- | ----- | --- | ------------------------ | --- | --- | --- | ----------- | --- | ---------- | ------ | ----- | --- | --- | --- |
Scaling relations linking species size, abundance, and resource availability are among the most
robustempiricalregularitiesinecology. However,amechanisticexplanationforhowthesecommunity-
levellawsemergefromecologicalprocessesremainselusive. Here,weaddressthisgapbydevelopinga
minimalspatiallyexplicitdynamicalframeworkforforestcommunitiesthatincorporatesseeddispersal,
growthlimitedbylocallightavailability,localcompetition,andglobalresourceconstraintsgrounded
in metabolic scaling principles. By deriving an analytical solution for the tree-size distribution,
we show that its stationary state exhibits two distinct power-law regimes whose exponents are
controlled by the relative strength of resource and spatial competition. The crossover between these
regimes is set by the interplay between seed injection and local resource availability, establishing
6202 guA 21  ]EP.oib-q[  1v81911.8062:viXra an explicit link between the scaling exponent of the size distribution and forest condition. Finally,
we show that boundary disturbances can break the ecological balance between competing species
and induce effects that propagate deeply into the forest bulk, far beyond the single-plant dispersal
range. Together, these results provide a unifying dynamical perspective on forest scaling laws with
|     | potential | applications |     | to a broad | range | of  | biological | communities. |     |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | ---------- | ----- | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
INTRODUCTION and forest structure across a wide range of species and
|     |     |     |     |     |     |     |     | environments |     | [15–20]. | Consistent | with | these | ideas, | empir- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ---------- | ---- | ----- | ------ | ------ |
Ecological systems exhibit a remarkable variety of icaltree-sizedistributionsacrossforestecosystemsdisplay
macroscopic regularities despite the complexity of the approximate power-law scaling [10, 19, 21], which can be
|                  |            |              |        |                    |              |     |     | interpreted |     | as a signature |     | of self-similarity |               | and | suggests |
| ---------------- | ---------- | ------------ | ------ | ------------------ | ------------ | --- | --- | ----------- | --- | -------------- | --- | ------------------ | ------------- | --- | -------- |
| underlying       | biological | interactions |        | [1]. Understanding |              |     | how |             |     |                |     |                    |               |     |          |
|                  |            |              |        |                    |              |     |     | that common |     | patterns       | in  | complex            | and seemingly |     | distinct |
| such large-scale |            | patterns     | emerge | from               | the dynamics |     | of  |             |     |                |     |                    |               |     |          |
individual organisms is a central challenge in ecology. ecological systems may emerge from simple underlying
|       |                 |     |               |              |     |        |     | constraints, |     | such as | those | proposed | by MTE. |     |     |
| ----- | --------------- | --- | ------------- | ------------ | --- | ------ | --- | ------------ | --- | ------- | ----- | -------- | ------- | --- | --- |
| Among | the descriptors |     | of ecological | communities, |     | organ- |     |              |     |         |       |          |         |     |     |
ism size occupies a particularly important role because An important open question is how these large-scale
it influences metabolism, growth, reproduction, resource patterns emerge from the interaction of demographic pro-
use, and competitive ability [2–4]. As a consequence, size cesses operating within ecological communities. Ecosys-
distributions provide a natural link between individual- tems are inherently multiscale systems in which indi-
level processes and ecosystem-level structure [5–8], and vidual growth, competition, mortality, and recruitment
explaining the origin of these distributions and their as- continuously reshape community structure [1]. Although
sociated scaling laws has therefore been a longstanding observed size distributions constrain the class of admissi-
objective in ecological theory. ble ecological theories, they do not uniquely identify the
A major advance in this direction came from allomet- ecological processes that generate them. Bridging this
ric scaling theory and the Metabolic Theory of Ecology gap therefore requires mechanistic dynamical models that
(MTE), which revealed the existence of systematic rela- connect individual-level biological processes to emergent
tionships linking organism size, metabolic rates, growth, community structure [22]. Size-structured population
and demographic processes [9–14]. These ideas have pro- models provide a natural mathematical framework for
vided a unified framework for understanding how bio- this purpose and have played a prominent role in forest
logical constraints operating at the level of individual ecology and population dynamics [23–33]. At the same
organisms can generate regularities across populations time,combiningallometricgrowth,nonlinearcompetition,
and communities. In forest ecosystems, in particular, and ecological interactions within analytically tractable
metabolic and allometric arguments have successfully ex- size-structured models remains a significant challenge.
plainedbroadpatternsofbiomassallocation,resourceuse,
|     |     |     |     |     |     |     |     | Spatial  | processes |       | introduce | an additional      |     | layer       | of com- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | --------- | ------------------ | --- | ----------- | ------- |
|     |     |     |     |     |     |     |     | plexity. | While     | trees | are       | sessile organisms, |     | recruitment |         |
occursthroughseeddispersal,generatinginteractionsthat
|     |     |     |     |     |     |     |     | extend | across | spatial | scales. | In forest | ecosystems, |     | disper- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------- | ------- | --------- | ----------- | --- | ------- |
∗ andrea.rinaldo@unipd.it
† amos.maritan@unipd.it salthereforeprovidestheprimarymechanismlinkinglocal
‡ davide.bernardi@unipd.it populationsacrossspace. Understandinghownonlocalre-

2
cruitment interacts with growth and competition requires continuity equation in height space:
frameworksthatexplicitlyincorporatespatialinteractions
while remaining analytically tractable. Recent work has ∂ t ρ α (x,h,t)=−∂ h [g˜ α (x,h,t)ρ α (x,h,t)]
(1)
shown how the interplay between growth, competition, −µ (x,h,t)ρ (x,h,t).
α α
and spatial organization can produce emergent ecological
patterns [34]. More broadly, spatial structure has been Thefirstterm,g˜ α (x,h,t),describesthefluxofindividuals
shown to influence community composition, ecosystem through height space due to ontogenetic growth, whereas
resilience, and long-term stability, while spatial patterns the second, µ α (x,h,t), accounts for mortality induced by
themselves can provide information about ecosystem con- competition for space and resources. Recruitment and
dition [35–38]. dispersal enter through the boundary condition at small
heightsandthroughthespatialdependenceofthedensity
Here we develop a spatially explicit, size-structured
field, as explained below.
model for forest dynamics derived from metabolic scaling
Wefirstconsiderthegrowthofanisolatedtree,neglect-
principles. Starting from an energy-balance description
ing competition and external limitations. In trees, only a
of individual growth, we construct a non-linear integro-
fractionofthetotalbiomass,termedsapwood,ismetabol-
differential equation governing the density of trees as a
ically active. Following standard metabolic arguments,
function of size, space, and time. The model couples
weassumethatthemetabolicallyactivebiomassM obeys
ontogeneticgrowth,localeffectssuchaslightshadingand
the energy balance equation [9–13, 17] (see Materials and
density-dependent competition for space and resources,
Methods). We further assume, consistently with previous
and nonlocal recruitment mediated by seed dispersal. De-
studies, that the metabolic rate is proportional to the
spite the complexity of these interacting processes, the
total leaf area and therefore to the evapotranspiration
framework remains analytically tractable and admits ex-
rate [17–20]. Because leaf area scales with crown volume,
act and asymptotic solutions in several biologically rele-
and the crown radius scales with tree height as r ∼hH
vant regimes. This allows us to show that the stationary c
(0 < H ≤ 1 is the Hurst exponent [19, 39]), both the
tree-size distribution naturally exhibits a crossover be-
metabolicrateandthetotalsapwoodmasscanberelated
tween distinct scaling regimes associated with resource
to tree height through allometric scaling relations (see
limitation and spatial exclusion, thereby linking observ-
Materials and Methods). Substituting such scaling rela-
able forest structure to the dominant ecological mecha-
tionsintotheenergybalanceequationyieldsthefollowing
nismsshapingthedynamics. Wefurthershowthatspatial
effective growth law for tree height:
boundaries induce strong deviations from the homoge-
neous state by selectively suppressing the abundance of dh (t) (cid:18) h (cid:19)
smaller individuals, and that in multi-species systems, d α t =g α (h)=g 0 α 1− hα , (2)
these effects can generate long-term competitive imbal- u
ances between species characterized by different dispersal where hα is the characteristic height at which mainte-
u
strategies. nance costs balance metabolic production. This height
depends on resource availability, and in the absence of
competition and external disturbances it represents the
maximum attainable height for the species (see Materials
and Methods). We now account for the reduction in light
RESULTS availability caused by taller individuals. Only a fraction
of the incident radiation reaches smaller individuals, re-
ducingtheirgrowthrate. Wethereforemodeltheeffective
A forest growth model based on metabolic scaling
growth rate as
g˜(x,h,t)=I (x,h,t)g (h), (3)
Thecentralquantityinourmodel,representedschemat- α α
ically in fig. 1, is the local density of trees per unit area,
where I (x,h,t) denotes the fraction of light at height h
denoted by ρ (x,h,t). Then, ρ (x,h,t)dhA represents α
α α thatcanbeexploitedbyspeciesα. Assumingthatlightat-
the number of individuals of species α within the ref-
tenuationfollowstheBeer-Lambertlawforplantcanopies
erence area A centered at spatial position x at time t
[40, 41], the available light decreases exponentially with
whose height lies in the interval (h,h+dh). We assume
the cumulative vegetation crossed by the incoming radia-
that recruitment occurs at a fixed height h = h > 0,
0 tion:
corresponding to a seed that has successfully survived
andgrownintoaseedling. Individualsbelowh arethere- (cid:26) (cid:90) ∞ (cid:27)
0 I (x,h,t)=I exp −γ ρ(x,h′,t)h′2Hdh′ , (4)
fore not tracked explicitly, and ρ (x,h,t) is defined only α 0 α
α
h
for h ≥ h . As individuals grow, they are transported
0
(cid:80)
across height classes with growth velocity g˜ (h,t), while where ρ(x,h,t)= ρ (x,h,t) is the total tree density
α α α
mortality removes individuals at rate d (x,h,t). Hence, (summed across species) and γ is a coefficient describing
α α
the temporal evolution of this density takes the form how species α reacts to the decreased light availability
of a McKendrick–von Foerster equation [23, 26, 31], a (we remark that I (x,h,t) is not the total available light,
α

3
FIG. 1: Schematic representation of the multiscale forest dynamics model. The model describes the dynamics of the
local tree density ρ α (x,h,t), which represents the density per unit area of trees of species α, size h, at position x=(x 1 ,x 2 )
and time t. The three panels illustrate the individual, local, and landscape scales at which the underlying processes act. The
dynamics follows a McKendrick–von Foerster equation combining: (i) ontogenetic growth, derived from metabolic scaling and
modulated by canopy shading through the fraction of available light; (ii) density-dependent mortality arising from competition
for canopy space among similarly sized trees and from competition for shared resources among neighboring trees of all sizes;
and (iii) nonlocal recruitment through seed dispersal, represented by a boundary injection term accounting for the production,
| dispersal, | and | establishment |     | of new | saplings. |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
but also integrates the physiological effect of light inten- second term models mortality induced by resource limita-
| sity reduction |     | on   | the growth | rate). | Unlike  | the  | resource | tion, | defined | as  |     |     |     |     |
| -------------- | --- | ---- | ---------- | ------ | ------- | ---- | -------- | ----- | ------- | --- | --- | --- | --- | --- |
| competition    |     | term | introduced | below, | shading | acts | directly |       |         |     |     |     |     |     |
g˜ (h)R[ρ(x,t)]
on the growth rate by reducing the energy available for dR(x,h,t)= α
|         |             |     |     |     |     |     |     |     |     |     |     |       | ,   | (6) |
| ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
| biomass | production. |     |     |     |     |     |     |     |     | α   | h   | R (x) |     |     |
a
Wenowturntothesecondtermineq.(1),whichmodels
|                                                  |       |     |               |         |            |             |       | where | R (x) | denotes | the locally | available | resource | flux, |
| ------------------------------------------------ | ----- | --- | ------------- | ------- | ---------- | ----------- | ----- | ----- | ----- | ------- | ----------- | --------- | -------- | ----- |
| density-dependent                                |       |     | mortality     | arising | from       | competition | for   |       | a     |         |             |           |          |       |
| canopy                                           | space | and | finite shared |         | resources. | As trees    | grow, | and   |       |         |             |           |          |       |
| boththeirmetabolicdemandandcanopyareaincrease,so |       |     |               |         |            |             |       |       |       |         | (cid:90) ∞  |           |          |       |
dhρ(x,h,t)h1+2H,
that forest dynamics become progressively constrained by R[ρ(x,t)]= (7)
the availability of light, canopy area, and other limiting h0
resources.
representsthetotalresourceconsumptionrateofthelocal
| We  | model | the mortality |     | term | as the sum | of  | two contri- |        |            |     |          |      |                 |     |
| --- | ----- | ------------- | --- | ---- | ---------- | --- | ----------- | ------ | ---------- | --- | -------- | ---- | --------------- | --- |
|     |       |               |     |      |            |     |             | forest | community. | The | quantity | R[ρ] | is proportional | to  |
butions,aspace-limitationtermandaresource-limitation
|       |              |     |            |     |          |       |        | the | total metabolic | demand | of  | the community, | obtained |     |
| ----- | ------------ | --- | ---------- | --- | -------- | ----- | ------ | --- | --------------- | ------ | --- | -------------- | -------- | --- |
| term, | µ (x,h,t)=dS |     | (x,h,t)+dR |     | (x,h,t), | where | dS ac- |     |                 |        |     |                |          |     |
α α α α by integrating the metabolic scaling B ∼h1+2H over all
dR
counts for mortality induced by space limitation and individuals at position x. The ratio
α
| for mortality |     | induced      | by  | resource   | limitation. | The | space- |     |     |         |           |     |     |     |
| ------------- | --- | ------------ | --- | ---------- | ----------- | --- | ------ | --- | --- | ------- | --------- | --- | --- | --- |
| competition   |     | contribution |     | is defined | as          |     |        |     |     |         | R[ρ(x,t)] |     |     |     |
|               |     |              |     |            |             |     |        |     |     | a(x,t)= |           |     |     | (8) |
R (x)
a
|     | dS(x,h,t)=d |     | I   | (x,h,t)h2Hρ(x,h,t), |     |     | (5) |           |          |     |       |                   |             |     |
| --- | ----------- | --- | --- | ------------------- | --- | --- | --- | --------- | -------- | --- | ----- | ----------------- | ----------- | --- |
|     |             | α   | α   | α                   |     |     |     |           |          |     |       |                   |             |     |
|     |             |     |     |                     |     |     |     | therefore | measures | the | local | level of resource | saturation. |     |
where the functional form of eq. (5) assumes mortality The form of eq. (6) expresses the idea that mortality due
induced by space competition to be proportional to the to resource competition should increase both with the
local density of similarly sized individuals within this in- metabolicdemandofanindividualandwiththedegreeof
teraction range and to the available light intensity. More collective resource depletion. In the absence of additional
details are provided in the Materials and Methods. The effects, theresultingdynamicsdrivesthesystemtowarda

4
stationary state in which the total resource consumption fast compared to those of tree birth and death dynamics.
equilibrates around the available resource flux R (see Equation (9) expresses the density of newly established
a
Materials and Methods). Although we treat resources saplings as a non-local contribution from reproductively
here asan effective collectivevariable, all species drainre- active individuals across the forest. The contribution of
sourcesfromthesharedresourcepool, therebygenerating each individual is weighted both by the dispersal kernel
both intra- and interspecific competition. and by the factor h1+2H, which reflects the scaling of re-
Finally, we model the recruitment of new individuals productive investment with metabolic rate. The integral
through a boundary condition at the sampling height h : over tree height starts at h , representing the minimum
0 b
height at which individuals become reproductively ma-
(cid:90) ∞ (cid:90)
ρ (x,h ,t)= dh dx′K (x,x′)h1+2Hρ (x′,h,t). (9) ture. Forsimplicity, andinordertoreducethenumberof
α 0 α α
freeparameters,inthefollowingweseth =h ,whilethe
hb b 0
moregeneralcaseh ≥h isdiscussedintheSIAppendix .
b 0
Here, K(x,x′) denotes the dispersal kernel, which quan- Within our framework, spatial effects enter the dynamics
tifies the rate at which an individual located at x′ con- exclusively through the recruitment process. This reflects
tributes viable offspring to position x. The kernel there- the fact that trees are sessile organisms, while seed dis-
foreeffectivelyincorporatesbothseeddispersalandgermi- persal can occur over finite distances through multiple
nationprocesses,includingtheeffectsofbioticandabiotic biotic and abiotic transport mechanisms. Such non-local
dispersal vectors and local environmental conditions. In interactions are explicitly encoded in the dispersal kernel
principle, the kernel could depend explicitly on both the K(x,x′).
time of seed production and the time of recruitment. For
simplicity, here we assume a stationary kernel and con-
sider K(x,x′) as an integrated effect over all past times. Combiningallcontributions(seeMaterialsandMethods
This approximation is further justified by the fact that for derivation), the complete dynamical equation govern-
seeddispersalisexpectedtooccurontime-scalesthatare ing the time evolution of the population density is:
(cid:26) (cid:20) (cid:21) (cid:27)
g (h)R[ρ(x,t)]
∂ ρ (x,h,t)=−I (x,h,t) ∂ [g (h)ρ (x,h,t)]+ (γ g (h)+d )h2Hρ(x,h,t)+ α ρ (x,h,t) , (10)
t α α h α α α α α h R (x) α
a
which,complementedbytheinjectiontermeq.(9),defines Exact solution of the spatially-homogeneous bulk
ourmodelinthegeneralcase. Weconcludethissectionby solution
noting that the classical McKendrick-von Foerster equa-
tionislinearwhendemographicratesandrecruitmentare Toobtainanalyticalinsightintothefullmodel, wefirst
prescribed independently of the evolving population. In consider the spatially homogeneous bulk limit. First, we
thissetting,long-timebehaviorisdeterminedbythespec- assume that growth and resource-consumption parame-
tral properties of the associated linear operator, so that ters,alongwiththeshadowcoefficient,areidenticalacross
stationarypopulationsariseonlyunderspecificparameter species, in the spirit of the neutral assumption of com-
balances [31]. In practice, this is often achieved either by munity ecology [42], which successfully captures several
calibrating demographic parameters to satisfy the equilib- large-scalepatternsintropicalforests. Underthisassump-
rium condition or by deriving demographic rates under tion, the multispecies dynamics can be written exactly
theassumptionofaprescribedstationarydistribution[34]. in terms of the total density ρ(x,h,t) = (cid:80) ρ (x,h,t).
α α
In contrast, our formulation couples growth, mortality, This approximation allows us to isolate the effects of size
and recruitment self-consistently through ecological inter- structure and spatial interactions before reintroducing
actions, leadingtoanonlinearnonlocalequationinwhich species-specificdifferencesbelow. Second,weassumethat
the stationary state emerges as part of the dynamics. To all environmental parameters are spatially homogeneous
systematically investigate the dynamical behavior of the andthatthesystemitselfistranslationallyinvariant. The
model and its connection to the underlying biological dispersal kernel, K(x−x′) encodes the characteristic spa-
mechanisms, we now proceed by first introducing several tial scale ξ over which seeds are dispersed. In the limit in
simplifying assumptions, which we will then gradually which the characteristic system size is much smaller than
relax. the dispersal length scale ξ, the dispersal kernel is effec-
tivelyconstantacrossthedomain,sorecruitmentbecomes
independent of spatial location. From a mathematical
perspective, this corresponds to a mean-field approxima-
tioninwhichthedispersalprocesseffectivelyhomogenizes
recruitment across the domain. We therefore neglect spa-
tial variations in the density and approximate the density

5
field as spatially homogeneous, ρ(x,h,t) ≡ ρ(h,t). Un-
der this assumption, the recruitment boundary condition
simplifies to
(cid:90) ∞
ρ(h ,t)=κ dh′(h′)1+2Hρ(h′,t), (11)
0
h0
where
(cid:90)
κ= dx′K(x−x′) (12)
is the spatial integral of the dispersal kernel, which is
independentofxundertranslationalinvariance. Although
the full time-dependent dynamics can be written as an
implicit self-consistent solution (see SI Appendix), the
stationary regime admits an exact analytical solution,
which we derive below.
Exact stationary solution reveals distinct dynamical
regimes
We now analyze the stationary solutions of the model,
which characterize the long-term structure of the forest.
To reduce the number of free parameters, we introduce
the rescaled variables
d
ρˆ(h,τ)= ρ(h,τ/g ). (13)
g 0
0
For notational convenience, we continue to denote the
rescaled density by ρ rather than by ρˆ, while the use of
FIG.2: Exact stationary solution for tree-size distribu-
the rescaled time variable τ will indicate dimensionless tion shows the signature of the underlying dynamical
quantities throughout the remainder of this section. Con- regime and the local resource availability as a dual
sequently,theparametersκandγ areimplicitlyredefined power-law shape. A: In the spatial mean-field case, the
in accordance with this rescaling. As we will show, the stationary solution of eq. (10), ρ∗(h), as given in eq. (27), dis-
stationary tree-size distribution encodes the relative im- plays a dual power-law shape separated by a crossover height
portance of growth, recruitment, and density-dependent h c . At lower tree sizes, the resource competition term domi-
nates. In this size range, the distribution follows a power-law
competition for resources, canopy space, and light. We
therefore seek time-independent solutions ρ∗(h) of the decrease with exponent −a, where a=R∗/R a is the resource
consumption ratio. Above the crossover size h , the spatial
rescaled form of eq. (10). This can be obtained in closed c
competition term dominates and the power-law exponent be-
form in the general case (see Materials and Methods).
comes −(1+2H), which is linked only to the tree allometric
The full expression involves hypergeometric functions to-
scaling relation. Parameters: κ=0.001 and R =220 (imply-
a
gether with a self-consistent equation for the recruitment ing ρ∗(h )≈0.11, a≈0.5, and h ≈4.2). B: If the available
0 c
term. However, in the biologically relevant intermediate resourcesareveryabundantand/orthesamplingrecruitment
regime h ≪ h ≪ h , and for a ≡ R[ρ∗]/R ≤ 1+2H, rateishigh,thecrossoverpointshiftstowardsverylowvalues
0 u a
the asymptotic expansion of the hypergeometric func- h c →h 0 . In this scenario only the power law with exponent
tionsyieldsaconsiderablysimplerandmoreinterpretable −(1+2H) is visible. Parameters: κ = 10 and R a = 235
expression for the stationary density: (ρ∗(h 0 )≈1.2·103, a≈0.5, and h c ≈0.1). C: If the available
resources are scarce or seed injection / recruitment is low, the
(cid:18) ha h1+2H (cid:19)−1 crossover point shifts to high values, h c → h u . In this case,
ρ∗(h)≈ +(1+γ) +l.d.t. , theonly visiblepowerlaw hasexponent−a, witha<1+2H.
ha 0 ρ∗(h 0 ) 1−a+2H Parameters: κ=10−6andR a =80(implyingρ∗(h 0 )≈4·10−5,
(14) a≈0.5, and h ≈101). Common parameters across all panels:
c
H =1, h =h =0.1, γ =1, h =100.
0 b u
where ρ∗(h ) is computed self-consistently from the re-
0
cruitment condition eq. (11) (see Materials and Methods).
Equation (14) consists of the sum of two competing
power-law contributions, each associated with a distinct

6
dynamical regime. As a consequence, the stationary tree- non-random inhomogeneous conditions, supporting that
size distribution exhibits a crossover between two scaling it is globally stabile.
behaviors at a characteristic height scale h . By equating
c
the two terms in eq. (14), we obtain the crossover scale
Effect of space and border disturbance
(cid:18)
1−a+2H
(cid:19)1/(1+2H−a)
h = . (15)
c (1+γ)ha 0 ρ∗(h 0 ) We now relax the assumption of spatial homogene-
ity and reintroduce the explicit spatial dependence of
As shown in fig. 2A, the stationary density therefore
the model. As discussed above, spatial coupling enters
displays a double power-law behavior. In the regime through the dispersal kernel K(x,x′), which describes
h ≪ h ≪ h , the first contribution dominates and
0 c recruitment at position x=(x ,x ) generated by individ-
1 2
ρ∗(h)∼h−a, whereas for h c ≪h≪h u , the second term uals located at position x′. We model dispersal using the
becomes dominant, yielding ρ∗(h)∼h−1−2H. Therefore,
simplestisotropickernelwithacharacteristiclengthscale,
the stationary size-distribution exhibits two distinct scal-
namely an exponential kernel with correlation length ξ,
ing regimes. For small individuals, h<h , the dynamics
c and consider a forest distributed on a homogeneous two-
isprimarilycontrolledbycompetitionforsharedresources,
dimensionalsurface. Intheabsenceofexplicitboundaries,
leading to the scaling ρ∗(h)∼h−a, with a<1+2H. As the spatially homogeneous steady state ρ∗(x,h)=ρ∗(h)
trees grow, spatial exclusion, light and canopy competi-
remains a stationary solution of the spatially explicit
tion progressively become dominant, giving rise to the
model (see Materials and Methods).
asymptotic scaling ρ∗(h) ∼ h−1−2H for h > h . This
c Startingfromthishomogeneoussteadystate,weinvesti-
crossover is consistent with the well-established role of
gatetheeffectofaboundarydisturbanceinaparticularly
resource limitation during seedling establishment and ju-
simple geometry. At t=0, we impose
venile growth, particularly under low-light understory
conditions [43–45]. L
The critical height h c depends on the the sapling re- ρ(x,h,t)=0 for |x 1 |> 2 and t≥0, (16)
cruitment rate and the local available resources R . For
a
instance,ifthesaplingrecruitmentefficiencyishigh,then thereby representing a region in which the forest has
the injection term ρ∗(h ) will grow. In this case, for a been completely removed by an external disturbance and
0
given R , the crossover will shift toward lower values, regrowth is prevented. Equivalently, the forest is con-
a
eventually reaching the sapling height h → h (see SI strainedtogrowwithinaninfinitestripofwidthL,aligned
c 0
Appendix). The same effect happens when R →∞. In along the x direction (fig. 3A). By translational invari-
a 2
both cases, the relative importance of the resource sink ance along the x direction, we can integrate one spatial
2
term decreases, and the stationary distribution displays a dimension and reduce the problem to a one-dimensional
single power law with exponent ≈−(1+2H) (fig. 2B). In systemwithadifferentdispersalkernel(aBesselfunction,
the opposite limit of scarce resources and weak injection, see Materials and Methods).
thecrossoverpointshiftstotheright, eventuallyreaching Figure 3B shows the relative variation in the total
h u . When h c → h u , then again ρ∗(h) displays a single tree density with respect to the homogeneous station-
power law, this time with exponent −a (fig. 2C). Inter- ary state. Near the boundary, the total tree density is
estingly, the influence of the canopy shading parameter γ strongly reduced due to the suppression of seed influx
on the crossover height is modest, compared to the other from the removed side of the forest. Interestingly, al-
parameters (see SI Appendix). though the total tree density decreases by almost 40%
Wefindthata≤(1+2H)(seeMaterials and Methods), near the boundary, the relative variation in the resource
wherea≈1+2H indicatesthattheresourceconsumption saturation parameter, a∗/a , remains only a few percent
0
is at its saturation value. In other words, if a single (fig. 3B, inset). The reason for this behavior is shown in
power law behavior is observed with (negative) exponent fig. 3C: the dominant contribution to the depletion of the
a ≪ 1+2H, then this indicates that the resource sink total density originates from small individuals, as demon-
term is the limiting factor. Instead, if a≈1+2H, then strated by the comparison between the size distributions
the forest growth is not limited by resource availability, in the bulk and near the boundary. This behavior is con-
but rather by space competition. sistent with the fact that smaller trees are more strongly
Finally,regardingthestabilityofthestationarysolution controlledbytherecruitmenttermandarethereforemore
discussed in this section, ρ∗(h), taking the limit τ →∞ sensitive to reductions in seed injection. By contrast, the
in the formal time-dependent, spatially homogeneous ex- large-tree sector of the distribution, corresponding to the
act solution to the mean-field eq. (10) for γ =0 (see SI regime above the crossover scale h , is only weakly af-
c
Appendix), indicates that this solution is globally attract- fected by the boundary perturbation. As a consequence,
ing in the general case. Furthermore, numerical simula- the total resource consumption remains nearly uniform
tions show that the spatially homogeneous, translation- acrossthesystem. Thisreflectsthefactthattheresource-
invariant system converges to the homogeneous solution consumption term is dominated by larger trees, whose
ρ∗(h) even when initialized from different random and distribution is comparatively insensitive to edge effects.

7
FIG.3: Spatial coupling causes border disturbance, which disproportionately affects smaller trees. A:Depictionof
border disturbance: starting from the spatially homogeneous solution, the forest is then confined to a land strip, as in eq. (16).
The two colored markers mark bulk and edge positions for which the stationary density is shown in panel C. B: Stationary
post-disturbance total tree density N∗(x)= (cid:82) dhρ∗(x,h) relative to pre-disturbance state N = (cid:82) dhρ∗(h). Inset: stationary
0 0
scaling exponent a∗(x) relative to pre-disturbance exponent a as a function of the spatial coordinate x . C: Stationary
0 1
post-disturbance distribution in the bulk (green line) and border (brown line) compared to initial pre-disturbance level (black
dashed line). Parameters: H =1, h =h =0.1, κ=0.01, R =125, h =50, ξ=1, and L=10.
0 b a u
As a final remark, we note that the effect of the bound- We consider the same spatial configuration introduced
ary has a range consistent with the spatial scale of the intheprevioussubsectionanddefinedineq.(16), namely
kernel, and is mostly disappeared at a distance of ≈ 3 a forest strip of width L surrounded by uncolonizable
from the boundary (space is measured in units of ξ =1). terrain, starting from the homogeneous stationary distri-
We now show that this picture can change drastically in bution (fig. 4A). For symmetry, we choose equal starting
the presence of different species with different dispersal densities for the two species. Figure 4B shows the spatial
(cid:82)
lengths. profile of N (x,τ) = dhρ(x,h,τ), the total tree den-
α
sity per unit area for the two species, at different times,
normalizedbytheinitialdensity. Immediatelyafterinitial-
ization, the two profiles are nearly identical and spatially
Interplay of boundary effects and inter-species
uniform, consistently with the homogeneous stationary
interactions
state. As time evolves, however, the species characterized
bythelongerdispersallengthprogressivelydecreasesnear
To reintroduce the additional complexity associated
the boundary, while the more localized species increases
with multiple tree species avoiding proliferation of pa-
its density. Interestingly, this trend persists over very
rameters, we consider the case of two species (or species
longtimescales,withthelong-dispersalspeciescontinuing
groups)characterizedbydifferentdispersalpropertiesbut
to decline in relative abundance throughout the system’s
identical growth and mortality dynamics. We retain the
evolution. Moreover,thespatialextentofthiseffectsignif-
exponential kernel introduced in eq. (35), while allowing
icantly exceeds the characteristic dispersal length: while
for species-dependent dispersal lengths ξ , with α=1,2.
α the dominant species displays a boundary layer compara-
Importantly, the normalization of the kernel ensures that
ble to the single-species case shown in fig. 3, the density
itsspatialintegralisindependentofξ . Asaconsequence,
α reduction of the declining species extends across the en-
in a homogeneous two-dimensional environment, the spa- (cid:82)
tire strip. Figure 4C shows N (τ)= dxN (x,τ), the
tially homogeneous stationary solution λ ρ∗(x,h), with tot 1
(cid:80) λ =1 remains a stationary solution f α or α each species, total tree density per unit area of the species with ξ 1 =1,
α α as a function of time for different values of ξ < ξ . In
independently of their dispersal range (see Materials and 2 1
all cases, the density undergoes an initial decay that is
Methods). This property reflects the fact that, in the
approximately exponential, with a rate that depends on
absence of spatial heterogeneity or boundaries, the total
the mismatch between the two dispersal scales, before
recruitment effort remains balanced across species. Eco-
eventually settling at very low values (see SI Appendix).
logically, this is consistent with the well-known trade-offs
Finally, the inset in fig. 4C shows the characteristic de-
associatedwithseeddispersalstrategies,wherebybroader
cay timescale τ , defined as the inverse decay rate of the
dispersal spreads recruitment over larger spatial scales ξ
declining species (species 1 for ξ <ξ =1, and species
while reducing local recruitment density, and physical 2 1
2 otherwise), as a function of ξ . The decay timescale
properties of heavier seeds that tend to travel shorter 2
increasessignificantlyasξ approachesξ frombothsides,
distances [35, 46, 47]. 2 1

8
and then diverges as ξ →ξ , reflecting the fact that the turbance [49–51]. Within our framework, these variations
2 1
two species become dynamically equivalent in this limit. acquire a mechanistic interpretation, reflecting shifts in
Takentogether,theresultsshowninfig.4indicatethat the relative importance of resource limitation and spatial
species with broader dispersal kernels are more sensitive competition.
to boundary effects, leading to a substantial reduction in By reintroducing explicit spatial dependence, we fur-
their total abundance. This behavior originates from the ther showed that finite boundaries induce substantial
suppression of recruitment near the boundaries, which deviations from the homogeneous stationary state. In
primarily affects smaller individuals and therefore dispro- the single-species case, finite boundaries suppress local
portionately impacts the species relying more strongly recruitment and primarily affect the density of small indi-
on long-range dispersal. The resulting depletion of juve- viduals, while leaving the large-tree sector comparatively
nile trees weakens the competitive balance of the long- unchanged. As a consequence, substantial reductions in
dispersal species, ultimately favoring the expansion and totaltreeabundancecanoccurevenwhenoverallresource
dominance of the more localized competitor. consumptionremainsapproximatelyconstant. Thisresult
highlights the distinct ecological roles played by differ-
ent size classes and suggests that demographic responses
DISCUSSION to fragmentation or edge effects may be concentrated
disproportionately among younger individuals, possibly
providing a new theoretical tool to interpret field reports
In this work, we introduced a spatially explicit, size-
of habitat fragmentation and local disturbances [52–54].
structured model for forest dynamics that combines onto-
geneticgrowth,canopyshadingeffects,density-dependent The multi-species model reveals an additional mech-
competition, and non-local recruitment through seed dis- anism emerging from the interaction between dispersal
persal. Acentralfeatureofourframeworkisthat,starting and competition. Dispersal-related life-history trade-offs
from metabolic scaling principles, it links three levels of have long been recognized as important determinants of
description that are often treated separately: individual coexistence in heterogeneous landscapes [55]. Here we
metabolicgrowth,stand-levelsizestructure,andspatially show that, even in homogeneous environments, explicit
non-local recruitment. Our approach remains sufficiently spatial boundaries can break the resulting symmetry be-
mechanistic while retaining analytical tractability. As a tweendispersalstrategiesanddrivelong-termcompetitive
result, the scaling regimes emerging in the tree-size distri- imbalance. Speciescharacterizedbybroaderdispersalker-
bution arise directly from explicit demographic processes nels experience a stronger reduction in recruitment near
ratherthanfromphenomenologicalassumptions,allowing boundaries, progressively weakening their competitive po-
observed forest structure to be interpreted in terms of sition and favoring species with shorter dispersal ranges.
underlying ecological mechanisms. Interestingly, this effect extends well beyond the intrinsic
In a spatially homogeneous setting, the model has an dispersal scale, producing system-wide shifts in abun-
exact solution for the stationary tree-size distribution, dance despite originating from a localized perturbation.
characterized by a crossover between two distinct power- At the same time, these results should not be interpreted
law regimes. For small individuals, the distribution is as implying inevitable exclusion of long-dispersal species.
controlledprimarilybyresourcecompetitionanddepends When dispersal differences are small, the characteristic
explicitly on the degree of resource saturation. For larger exclusiontimescalebecomesextremelylong,reachinghun-
trees,thedynamicsbecomesdominatedbyspatialshading dreds of multiples of the individual growth timescale g α −1.
and canopy competition, leading to a scaling exponent Such time-scales would be much longer than those over
determined solely by crown allometry. The crossover which the environmental conditions stay stationary, and
scale separating these regimes therefore provides a direct extendbeyondtheexpectedrangeofvalidityofourframe-
connection between measurable forest structure and the work. Moreover, realforestsarecharacterizedbymultiple
dominant processes regulating population dynamics. In ecological trade-offs involving growth rate, shade toler-
particular, the emergence of a single power-law regime ance, fecundity, resource-use efficiency, and disturbance
may indicate whether forest dynamics are primarily con- resilience [56–58]. Such trade-offs may counterbalance
strained by resource limitation or by space occupation, the boundary-mediated disadvantages identified here and
suggesting that tree-size spectra may contain information generate coexistence, successional dynamics, or spatial
abouttheunderlyingecologicalstateofthesystem. From niche partitioning [59–62].
anecologicalperspective,theseresultsareconsistentwith Previous theoretical studies have successfully combined
resourcelimitationdominatingjuvenilestages[35,44,46– size structure and demographic stochasticity within neu-
48] and spatial competition becoming increasingly impor- tral frameworks to investigate emergent patterns of com-
tant for larger individuals. Importantly, this connection munity organization [33]. More generally, scaling ap-
between the dynamical regimes and a measurable quan- proaches have shown that universal tree-size distributions
tity, the tree-size scaling exponent, provides a possible can emerge from allometric and energetic constraints, in-
way of a qualitative estimate of a forest condition, and cluding through optimization principles [19]. The present
is in qualitative agreement with empirical studies linking framework provides a complementary dynamical perspec-
theexponentoftree-sizedistributionstothedegreeofdis- tive by explicitly incorporating ecological interactions.

9
FIG. 4: Interplay between dispersal and inter-species competition amplifies border disturbance inducing
competitive exclusion between species with different dispersal ranges. A: Depiction of border disturbance: same
spatial configuration as in fig. 3, but with two competing species with different dispersal ranges ξ 1 =1,ξ 2 . B: Spatial profile
of the total tree density per unit area N α (x) for both species, shown at different times after the introduction of a boundary
disturbance. While both species initially occupy the strip homogeneously (dashed line), the species with the larger dispersal
range (brown solid lines) progressively decreases near the boundary and eventually throughout the entire system, whereas the
more localized species becomes dominant (green solid lines). C: Total tree density of the disadvantaged species with fixed
dispersal length ξ = 1 as a function of time, for different values of ξ < ξ . The abundance of the disadvantaged species
|     |     | 1   |     |     |     |     | 2   | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
decreases approximately exponentially, with a decay rate controlled by the mismatch between the two dispersal scales. Inset:
Characteristic decay timescale τ of the disadvantaged species as a function of the dispersal length ratio, computed from an
ξ
exponential fit (note the log y-scale) in the range 50 ≤ τ ≤ 300. The timescale diverges as ξ → ξ , where the two species
|     |     |     |     |     |     |     |     |     |     | 2   | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
become dynamically equivalent (vertical dotted line). Spatial distances are measured in units of the reference dispersal scale
ξ 1 =1. Parameters: H =1, h 0 =h b =0.1, κ=0.018, R a =112, h u =50, ξ=1, and L=10.
Within this formulation, the universal scaling exponent is tractability represents an important direction for future
recoveredasthelimitingcaseinwhichforestdynamicsare work and may provide a bridge between mechanistic for-
no longer constrained by resource availability, while de- est theory and empirical observations of forest structure,
partures from this exponent arise naturally from resource biodiversity, and ecosystem resilience.
| limitation. | This     | establishes | a mechanistic |     | connection         | be- |     |     |     |     |     |     |     |
| ----------- | -------- | ----------- | ------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| tween the   | observed | scaling     | exponent      |     | and the underlying |     |     |     |     |     |     |     |     |
dynamicalregimeoftheforest,providingconditionsunder MATERIALS AND METHODS
| which the | optimal | scaling | state | can | be attained. | More |     |     |     |     |     |     |     |
| --------- | ------- | ------- | ----- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
broadly,ourframeworkallowsforestsizedistributionsand Growth rate
spatialabundancepatternstobeinterpretedassignatures
| of the ecological |     | processes | shaping | forest | dynamics. |     |           |            |     |        |                |     |             |
| ----------------- | --- | --------- | ------- | ------ | --------- | --- | --------- | ---------- | --- | ------ | -------------- | --- | ----------- |
|                   |     |           |         |        |           |     | We derive | the growth |     | term g | (h) introduced |     | in eq. (2). |
α
| The                        | present     | study should  | nevertheless                |            | be regarded | as          |                  |             |                   |        |           |         |          |
| -------------------------- | ----------- | ------------- | --------------------------- | ---------- | ----------- | ----------- | ---------------- | ----------- | ----------------- | ------ | --------- | ------- | -------- |
|                            |             |               |                             |            |             |             | Following        | established | metabolic         |        | scaling   | theory, | the tem- |
| a first step               | aimed       | at isolating  | the                         | basic      | dynamical   | conse-      |                  |             |                   |        |           |         |          |
|                            |             |               |                             |            |             |             | poral dynamics   | of          | the metabolically |        | active    | biomass | M of     |
| quences                    | of coupling | growth,       | competition,                |            | and         | dispersal   |                  |             |                   |        |           |         |          |
|                            |             |               |                             |            |             |             | an individual    | organism    |                   | can be | described | via the | energy   |
| withinatractableframework. |             |               | Severalbiologicallyrelevant |            |             |             |                  |             |                   |        |           |         |          |
|                            |             |               |                             |            |             |             | balance equation |             | [9–13,            | 17]:   |           |         |          |
| ingredients                | have        | intentionally | been                        | neglected. |             | In particu- |                  |             |                   |        |           |         |          |
| lar, we                    | assumed     | identical     | growth                      | and        | mortality   | dynamics    |                  |             |                   |        |           |         |          |
dM
|               |          |                    |               |          |             |     |     |     | =cα | B−cα | M,  |     | (17) |
| ------------- | -------- | ------------------ | ------------- | -------- | ----------- | --- | --- | --- | --- | ---- | --- | --- | ---- |
| across        | species, | homogeneous        | environmental |          | conditions, |     |     |     | dt  | 1    | 2   |     |      |
| and isotropic |          | dispersal kernels. |               | Resource | limitation  | was |     |     |     |      |     |     |      |
represented through an effective collective variable, and whereB isthetotalmetabolicrate,andcα,cα arespecies-
1 2
did not explicitly distinguish among different limiting specific coefficients. We assume that the assimilation co-
cα
resources such as water or nutrients [44, 63–65]. Environ- efficient =ϵ 1 R a /(ζ+R a ) depends on the available re-
1
mental heterogeneity [66–68], demographic fluctuations sourcesR ,whereζ isahalf-saturationconstant,whereas
a
[33, 69, 70], landscape geometry and fragmentation [71– the maintenance cost coefficient is scaled as cα =ϵ /hα ,
|     |     |     |     |     |     |     |     |     |     |     |     | 2   | 2 M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
withhα
74], and temporally varying resource availability [59, 75– denotingthetheoreticalmaximumheightachiev-
M
77] are all expected to influence forest dynamics and may ablebyspeciesα. Supportedbyempiricalandtheoretical
modify the scaling regimes identified here as well as the evidence[19,39],wemodeltheallometricscalingbetween
strength of boundary-mediated competitive effects. In- the crown radius r and tree height h as r ∼hH, where
|     |     |     |     |     |     |     |     |     | c   |     |     | c   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
corporating these ingredients while preserving analytical 0 ≤ H ≤ 1 is the Hurst exponent. Consequently, the

10
crown volume scales as V ∼h×r2 ∼h2H+1. As detailed transpiration rate. Because this term is due to spatial
c
intheMainText,themetabolicrateisproportionaltothe interference of tree canopies, the interaction range of this
crown volume, yielding B ∼h2H+1. Assuming that the term will be proportional to the lateral size of the crown,
sap flux velocity at the trunk basis is approximately inde- hH. Consequently, the mortality experienced by a tree of
pendent of tree size [78], the conducting cross-sectional heighthisproportionaltothelocaldensityofindividuals
area Σ must scale proportionally to the metabolic rate of comparable size within this interaction area. Specifi-
c
(Σ ∼ B). The active biomass is then proportional to cally, for a plant of height h, the space competition d at
c S
the product of the conducting area and the tree height, position x and time t is
leading to M ∼Σ ×h∼Bh∼h2H+2 [19]. Substituting
c
these scaling relations into the energy balance equation dS(x,h,t)=d I (x,h,t)·h2Hρ(x,h,t), (22)
α α α
eq. (17) and expressing the active mass M as a function
(cid:80)
of height h, we obtain where ρ(x,h,t)= α ρ α (x,h,t). Since the evapotranspi-
ration rate depends on the available light intensity, we
(cid:18) (cid:19)
dh α (t) =g (h (t))≡gα 1− h α (t) , (18) take this term as proportional to it.
dt α α 0 hα
u
where gα = cα/(2H +2) and hα = cα/cα are species-
0 1 u 1 2 Resource competition
specific parameters. Note that the growth term g (h)
α
does not depend explicitly on time. The asymptotic
height hα is given by the following: In the limit of negligible spatial competition, dS = 0,
u
the resources consumed by the forest per unit time obey
R hα the following equation
hα = a M, (19)
u ζ+R ϵα
a 2 (cid:18) (cid:19)
R[ρ (x,t)]
R˙ [ρ (x,t)]= 1− α (1+2H)
implying that in the case of poor available resources R a , α R˜
a
the plant stops growing before reaching the maximum (cid:90) ∞ (23)
height hα , consistent with empirical observations. × dhh2Hg˜ (h)ρ (x,h,t)
M α α
h0
+B (x,t),
α
Light attenuation and shading
where
Taller individuals intercept part of the incoming radi- (cid:12)∞
ation, reducing the amount of light that reaches shorter (cid:12)
B (x,t)≡−h2H+1g˜ (h)ρ (x,h,t)(cid:12)
plants. We account for this effect by assuming that the α α α (cid:12) (cid:12) (24)
growth rate is modulated by the local effective light avail- h0
ability I α (x,h,t): =h2 0 H+1g˜ α (h 0 )ρ α (x,h 0 ,t)≥0,
(cid:18) (cid:19)
h where we have taken into account that ρ (x,h,t) = 0
g˜ (x,h,t)=I (x,h,t)gα 1− (20) α
α α 0 h u when h>h u . Equation (23) implies that, neglecting the
boundary contribution B , the total resource consump-
α
whereplantstallerthanhcontributetoshadingtheplants tion R[ρ (x,t)] increases whenever R[ρ (x,t)] < R˜ (x)
α α a
below them. Assuming that light attenuation follows the and decreases whenever R[ρ (x,t)]>R˜ (x). Therefore,
α a
Beer-Lambertlaw[40,41],I (x,h,t)decaysexponentially
α the dynamics tends to drive the system toward a state
with the amount of vegetation crossed by the incoming
in which resource consumption balances the available re-
light:
source flux. The boundary term B becomes relevant
α
(cid:26) (cid:90) ∞ (cid:27) only in the presence of very strong recruitment, in which
I (x,h,t)=I exp −γ ρ(x,h′,t)h′2Hdh′ , (21) case it merely shifts the equilibrium value of the resource
α 0 α
h consumption. For simplicity, in the main text we redefine
R =R˜ /(1+2H).
where γ is the species-specific light attenuation coeffi- a a
α
cient, capturing both the physical shading effect of stand-
ing biomass and how efficiently species α exploits the
available light, and the integral accounts for the cumula- Stationary solution
tive shading exerted by all plants taller than h.
We derive the stationary solution of the model in the
spatiallyhomogeneouscase,undertheneutralassumption
Canopy interaction of identical growth and resource-consumption parameters
across species. Specifically, we look for ρ∗(h), a time-
The mortality of this term is due to direct interactions independent solution of the following PDE for ρ≡ρ(h,τ)
between tree canopies, and their effects on the evapo- (see eq. (13)):

11
(cid:26) (cid:20)(cid:18) (cid:19) (cid:21) (cid:20) (cid:18) (cid:19) (cid:21) (cid:18) (cid:19) (cid:27)
h h h a(τ)
∂ ρ=−I ∂ 1− ρ + γ 1− +1 h2Hρ2+ 1− ρ , (25)
τ h h h h h
u u u
where, for notational convenience, we have redefined the and d/g R as R . The stationary solution of eq. (25)
0 a a
parameter γg /d as γ and can be obtained by a suitable change of variable (see SI
0
Appendix), which leads to the following solution
R[ρ(τ)] (cid:90) ∞
a(τ)≡ , R[ρ(τ)]≡ h′1+2Hρ(h′,τ)dh′ (26)
R
a h0
1 (cid:18) h (cid:19)a (cid:34) 1−h/h 1 (cid:90) h 1+γ(1−h′/h ) (cid:35)
= u +ha(1−h/h ) dh′h′2H−a u , (27)
ρ∗(h) h 0 1−h 0 /h u ρ∗(h 0 ) 0 u h0 (1−h′/h u )2
where a denotes the steady-state resource consumption eq. (14), and is governed by the competition between two
ratio,asdeterminedfromeq.(26)evaluatedatρ=ρ∗,and distinct power-law scaling regimes, as explained in the
ρ∗(h ) is computed self-consistently from the recruitment main text.
0
condition eq. (11). The last equation can be re-expressed
in terms of hypergeometric functions F
2 1
(cid:90) x 1+γ−γz Homogeneous solutions of the spatially explicit model
dzzδ−1 =F(x)−F(x ), (28)
(1−z)2 0
x0
We consider a homogeneous two-dimensional environ-
where
ment in which species differ only through their dispersal
zδ kernels. We show that, in the absence of explicit bound-
F(z)= δ [ 2 F 1 (2,δδ+1;z)+γ 2 F 1 (1,δ;δ+1;z)] (29) ariesorenvironmentalheterogeneity,thespatiallyexplicit
model admits homogeneous stationary solutions that are
and δ = 1−a+2H. In this limit, if a < 2H +1, the independent of the dispersal range. Let ρ∗(x,h)=ρ∗(h)
α α
hypergeometric function simplifies to its leading-order be a stationary density independent of position. The
power law, so that the stationary density, is given by stationary equations become
(cid:20) (cid:21)
g(h)
0=−∂ [g(h)ρ∗(h)]− (γg(h)+1)h2Hρ∗(h)+ a∗ ρ∗(h), (30)
h α h α
(cid:90) (cid:90) ∞
ρ∗(h )= dx′K (x−x′) dh′h′1+2Hρ∗(h′). (31)
α 0 α α
h0
Here, we define ρ∗(h) = (cid:80) ρ∗(h), g(h) = 1 − h/h all species yields
β β u
and the quantity a∗ is specified by eq. (26), with ρ(h′,τ)
replaced by ρ∗(h). Since the dispersal kernel is normal- g(h)
ized, (cid:82) dx′K α (x−x′)=κ,independentlyofthedispersal 0=−∂ h [g(h)ρ∗(h)]−(γg(h)+1)h2Hρ∗2(h)− h a∗ρ∗(h),
length. Therefore, for spatially homogeneous densities,
(32)
the recruitment term depends only on the total repro-
(cid:90) ∞
ductive output of the species and not on the shape of its ρ∗(h )=κ dh′h′1+2Hρ∗(h′). (33)
0
dispersal kernel. Summing the stationary equations over h0
whichcoincideswiththesingle-speciesstationaryproblem
discussed in the previous section. This implies that the
per-species stationary density taken as proportional to

12
the total density, We consider an environment (the forest strip) which is
|     |     |     |     |     |          |     |     | translationallyinvariantalongthex |     |     |     | direction. | Theprob- |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --------------------------------- | --- | --- | --- | ---------- | -------- | --- |
|     |     |     |     |     | (cid:88) |     |     |                                   |     |     |     | 2          |          |     |
ρ∗(h)=λ ρ∗(h), λ ≥0, λ =1, (34) lem therefore reduces effectively to a one-dimensional
|              | α            | α           |               | α           |       | α                |            |             |           |        |     |     |     |     |
| ------------ | ------------ | ----------- | ------------- | ----------- | ----- | ---------------- | ---------- | ----------- | --------- | ------ | --- | --- | --- | --- |
|              |              |             |               |             |       | α                |            | system with | dispersal | kernel |     |     |     |     |
| is itself    | a stationary |             | solution.     |             | Thus, | in a homogeneous |            |             |           |        |     |     |     |     |
| environment, |              | species     | characterized |             | by    | different        | dispersal  |             |           |        |     |     |     |     |
| ranges       | remain       | dynamically |               | equivalent, |       | and the          | stationary |             |           |        |     |     |     |     |
state is determined only by their relative abundances λ . (cid:90) (cid:90)
α
|     |         |        |     |      |                |     |     | G(|x | −x′|)= | dx       | dx′ | K(x,x′)  |          |      |
| --- | ------- | ------ | --- | ---- | -------------- | --- | --- | ---- | ------ | -------- | --- | -------- | -------- | ---- |
|     |         |        |     |      |                |     |     |      | 1 1    | 2        | 2   |          |          |      |
|     |         |        |     |      |                |     |     |      |        |          |     | (cid:18) | (cid:19) | (36) |
|     |         |        |     |      |                |     |     |      |        | κ|x −x′| |     | |x       | −x′|     |      |
|     | Spatial | kernel |     | used | in simulations |     |     |      |        | = 1      | 1 K | 1        | 1 ,      |      |
1
|           |                 |     |             |     |         |        |             |     |     | πξ2 |     |     | ξ   |     |
| --------- | --------------- | --- | ----------- | --- | ------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| In        | the simulations |     | shown       | in  | figs. 3 | and 4, | we model    |     |     |     |     |     |     |     |
| dispersal | using           | an  | exponential |     | kernel  | with   | correlation |     |     |     |     |     |     |     |
length ξ,
(cid:18) (cid:19) where K is the modified Bessel function of the second
|     |             |     |      | κ   | |x−x′| |     |        |               | 1    |     |     |     |     |     |
| --- | ----------- | --- | ---- | --- | ------ | --- | ------ | ------------- | ---- | --- | --- | --- | --- | --- |
|     | K (|x−x′|)= |     |      | exp | −      |     | . (35) | kind of order | one. |     |     |     |     |     |
|     | ξ           |     | 2πξ2 |     |        |     |        |               |      |     |     |     |     |     |
ξ
[1] S. A. Levin, The problem of pattern and scale in ecology, [15] D. W. Purves, J. W. Lichstein, N. Strigul, and S. W.
Ecology 73, 1943 (1992). Pacala, Predicting and understanding forest dynamics
[2] M. Kleiber, The fire of life. An introduction to animal using a simple tractable model, Proc. Natl. Acad. Sci.
energetics. (John Wiley & Sons, Inc., New York: London, 105, 17018 (2008).
1961) pp. xxii + 454 pp. [16] N. Strigul, D. Pristinski, D. Purves, J. Dushoff, and
[3] J. Damuth, Scaling of growth: Plants and animals are S. Pacala, Scaling from trees to forests: tractable macro-
not so different, Proc. Natl. Acad. Sci. 98, 2113 (2001). scopic equations for forest dynamics, Ecol. Monogr. 78,
| [4] | P. A. Marquet, |     | R. A. | Quin˜ones, | S.  | Abades, | F. Labra, | 523 (2008). |     |     |     |     |     |     |
| --- | -------------- | --- | ----- | ---------- | --- | ------- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
M. Tognelli, M. Arim, and M. Rivadeneira, Scaling and [17] S. Mori, K. Yamaji, A. Ishida, S. G. Prokushkin, O. V.
power-laws in ecological systems, J. Exp. Biol. 208, 1749 Masyagina,A.Hagihara,A.R.Hoque,R.Suwa,A.Osawa,
(2005). T. Nishizono, et al., Mixed-power scaling of whole-plant
[5] J.Damuth,Populationdensityandbodysizeinmammals, respirationfromseedlingstogianttrees,Proc.Natl.Acad.
|     | Nature 290, | 699 | (1981). |     |     |     |     | Sci. 107, | 1447 | (2010). |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- | --------- | ---- | ------- | --- | --- | --- | --- |
[6] J. R. Banavar, A. Maritan, and A. Rinaldo, Size and [18] J. R. Banavar, T. J. Cooke, A. Rinaldo, and A. Maritan,
form in efficient transportation networks, Nature 399, Form, function, and evolution of living organisms, Proc.
| 130 | (1999). |     |     |     |     |     |     | Natl. | Acad. | Sci. 111, 3332 | (2014). |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | ----- | ----- | -------------- | ------- | --- | --- | --- |
[7] B. J. Enquist and K. J. Niklas, Invariant scaling rela- [19] F. Simini, T. Anfodillo, M. Carrer, J. R. Banavar, and
tions across tree-dominated communities, Nature 410, A.Maritan,Self-similarityandscalinginforestcommuni-
|     | 655 (2001). |     |     |     |     |     |     | ties, | Proc. Natl. | Acad. Sci. | 107, | 7658 | (2010). |     |
| --- | ----------- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ---------- | ---- | ---- | ------- | --- |
[8] P.A.Marquet,Ofpredators,prey,andpowerlaws,Science [20] I. Volkov, A. Tovo, T. Anfodillo, A. Rinaldo, A. Maritan,
295, 2229 (2002). andJ.R.Banavar,Seeingtheforestforthetreesthrough
[9] G. B. West, J. H. Brown, and B. J. Enquist, A general metabolic scaling, PNAS Nexus 1, pgac008 (2022).
model for the origin of allometric scaling laws in biology, [21] B. J. Enquist, G. B. West, E. L. Charnov, and J. H.
Science 276, 122 (1997). Brown, Allometric scaling of production and life-history
[10] B. J. Enquist, J. H. Brown, and G. B. West, Allometric variation in vascular plants, Nature 401, 907 (1999).
scalingofplantenergeticsandpopulationdensity,Nature [22] X. Xiao, J. P. O’Dwyer, and E. P. White, Comparing
395, 163 (1998). process-based and constraint-based approaches for mod-
[11] G. B. West, J. H. Brown, and B. J. Enquist, A general eling macroecological patterns, Ecology 97, 1228 (2016).
model for ontogenetic growth, Nature 413, 628 (2001). [23] A. G. McKendrick, Applications of mathematics to med-
[12] B.J.EnquistandK.J.Niklas,Globalallocationrulesfor ical problems, Proc. Edinb. Math. Soc. (2) 44, 98–130
|     | patterns | of biomass | partitioning |     | in  | seed plants, | Science | (1925). |     |     |     |     |     |     |
| --- | -------- | ---------- | ------------ | --- | --- | ------------ | ------- | ------- | --- | --- | --- | --- | --- | --- |
295, 1517 (2002). [24] S.A.LevinandR.T.Paine,Disturbance,patchformation,
[13] J. H. Brown, J. F. Gillooly, A. P. Allen, V. M. Savage, andcommunitystructure,Proc.Natl.Acad.Sci.71,2744
|     | and G. B. | West, | Toward | a metabolic |     | theory | of ecology, | (1974). |     |     |     |     |     |     |
| --- | --------- | ----- | ------ | ----------- | --- | ------ | ----------- | ------- | --- | --- | --- | --- | --- | --- |
Ecology 85, 1771 (2004). [25] T. Takada and Y. Iwasa, Size distribution dynamics of
[14] P.A.Marquet,F.A.Labra,andB.A.Maurer,Metabolic plants with interaction by shading, Ecol. Model. 33, 173
|     | ecology: | Linking | individuals |     | to ecosystems, |     | Ecology 85, | (1986). |     |     |     |     |     |     |
| --- | -------- | ------- | ----------- | --- | -------------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
1794 (2004). [26] B. L. Keyfitz and N. Keyfitz, The McKendrick partial
|     |     |     |     |     |     |     |     | differential |     | equation and | its uses | in  | epidemiology | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | -------- | --- | ------------ | --- |

13
population study, Math. Comput. Model. 26, 1 (1997). [44] L. Poorter and K. Kitajima, Carbohydrate storage and
[27] T. Kohyama, Simulating stationary size distribution of light requirements of tropical moist and dry forest tree
trees in rain forests, Ann. Bot. 68, 173 (1991). species, Ecology 88, 1000 (2007).
[28] T.Kohyama,Density-sizedynamicsoftreessimulatedby [45] A.L.Zhu,A.Ndiaye,R.Dahm,M.Mauclaire,andI.Boas,
aone-sidedcompetitionmulti-speciesmodelofrainforest Africa’sGreatGreenMirage? Assessingthedisconnectbe-
stands, Ann. Bot. 70, 451 (1992). tweenglobalfinanceandlocalimplementationinAfrica’s
[29] T. Kohyama, Size-structured tree populations in gap- Great Green Wall, Land Use Policy 157, 107670 (2025).
dynamic forest–the forest architecture hypothesis for the [46] S. Chen, P. Poschlod, A. Antonelli, U. Liu, and J. B.
stable coexistence of species, J. Ecol. , 131 (1993). Dickie, Trade-off between seed dispersal in space and
[30] T. Kohyama, E. Suzuki, T. Partomihardjo, T. Yamada, time, Ecol. Lett. 23, 1635 (2020).
and T. Kubo, Tree species differentiation in growth, re- [47] J. Treep, M. de Jager, F. Bartumeus, and M. B. Soons,
cruitment and allometry in relation to maximum height Seed dispersal as a search strategy: dynamic and frag-
in a Bornean mixed dipterocarp forest, J. Ecol. 91, 797 mentedlandscapesselectformulti-scalemovementstrate-
(2003). gies in plants, Mov. Ecol. 9, 4 (2021).
[31] J. D. Murray and J. D. Murray, Mathematical biology: [48] R. K. Kobe, S. W. Pacala, J. A. Silander, and C. D.
II: spatial models and biomedical applications, Vol. 18 Canham, Juvenile tree survivorship as a component of
(Springer, 2003). shade tolerance, Ecol. Appl. 5, 517 (1995).
[32] H. C. Muller-Landau, R. S. Condit, K. E. Harms, C. O. [49] T.Anfodillo,M.Carrer,F.Simini,I.Popa,J.R.Banavar,
Marks, S. C. Thomas, S. Bunyavejchewin, G. Chuyong, and A. Maritan, An allometry-based approach for under-
L.Co,S.Davies,R.Foster,etal.,Comparingtropicalfor- standingforeststructure,predictingtree-sizedistribution
esttreesizedistributionswiththepredictionsofmetabolic and assessing the degree of disturbance, Proc. R. Soc. B
ecologyandequilibriummodels,Ecol.Lett.9,589(2006). 280, 20122375 (2013).
[33] J.O’Dwyer,J.Lake,A.Ostling,V.Savage,andJ.Green, [50] G. Sellan, F. Simini, A. Maritan, J. R. Banavar,
An integrative framework for stochastic, size-structured T.deHaulleville,M.Bauters,J.-L.Doucet,H.Beeckman,
community assembly, Proc. Natl. Acad. Sci. 106, 6170 and T. Anfodillo, Testing a general approach to assess
(2009). the degree of disturbance in tropical forests, J. Veg. Sci.
[34] E.D.Lee,C.P.Kempes,andG.B.West,Growth,death, 28, 659 (2017).
and resource competition in sessile organisms, Proc. Natl. [51] A. J. Eichenwald, J. M. Grady, J. A. Knott, Q. D. Read,
Acad. Sci. 118, e2020424118 (2021). J.M.Rodriguez,andS.Record,Theimpactofdisturbance
[35] R. Nathan and H. C. Muller-Landau, Spatial patterns of ontreesizedistributionsintheUnitedStates,GlobalEcol.
seed dispersal, their determinants and consequences for Biogeogr. 34, 10.1111/geb.70102 (2025).
recruitment, Trends Ecol. Evol. 15, 278 (2000). [52] W. F. Laurance, L. V. Ferreira, J. M. Rankin-de Merona,
[36] T. Wiegand, X. Wang, K. J. Anderson-Teixeira, N. A. and S. G. Laurance, Rain forest fragmentation and the
Bourg, M. Cao, X. Ci, S. J. Davies, Z. Hao, R. W. Howe, dynamics of Amazonian tree communities, Ecology 79,
W.J.Kress,J.Lian,J.Li,L.Lin,Y.Lin,K.Ma,W.Mc- 2032 (1998).
Shea, X. Mi, S.-H. Su, I.-F. Sun, A. Wolf, W. Ye, and [53] R. M. Ewers and R. K. Didham, Confounding factors in
A.Huth,Consequencesofspatialpatternsforcoexistence the detection of species responses to habitat fragmenta-
inspecies-richplantcommunities,Nat.Ecol.Evol.5,965 tion, Biol. Rev. 81, 117 (2006).
(2021). [54] M. C. Nu´n˜ez-A´vila, M. Uriarte, P. A. Marquet, and
[37] M.Kalyuzhny,J.K.Lake,S.J.Wright,andA.M.Ostling, J.J.Armesto,Decomposingrecruitmentlimitationforan
Pervasive within-species spatial repulsion among adult avian-dispersedrainforesttreeinanancientlyfragmented
tropical trees, Science 381, 563 (2023). landscape, J. Ecol. 101, 1439 (2013).
[38] D. Bernardi, G. Nicoletti, P. Padmanabha, S. Suweis, [55] R. D’Andrea and J. P. O’Dwyer, Competition for space
S. Azaele, S. A. Levin, A. Rinaldo, and A. Maritan, Dis- in a structured landscape: The effect of seed limitation
persal diversity buffers species vulnerability to local ex- on coexistence under a tolerance-fecundity trade-off, J.
tinction, arXiv 10.48550/arXiv.2604.26589 (2026). Ecol. 109, 1886 (2021).
[39] L. S. Comita, S. Aguilar, R. P´erez, S. Lao, and S. P. [56] M. Westoby, M. Leishman, and J. Lord, Comparative
Hubbell, Patterns of woody plant species abundance and ecology of seed size and dispersal, Philos. Trans. R. Soc.
diversity in the seedling layer of a tropical forest, J. Veg. Lond. B Biol. Sci. 351, 1309 (1996).
Sci. 18, 163 (2007). [57] H. C. Muller-Landau, The tolerance–fecundity trade-off
[40] M. Monsi and T. Saeki, U¨ber den Lichtfaktor in den and the maintenance of diversity in seed size, Proc. Natl.
Pflanzengesellschaften und seine Bedeutung fu¨r die Stoff- Acad. Sci. 107, 4242 (2010).
produktion, Jpn. J. Bot. 14, 22 (1953). [58] S.D´ıaz,J.Kattge,J.H.C.Cornelissen,I.J.Wright,S.La-
[41] M. Monsi and T. Saeki, On the factor light in plant vorel,S.Dray,B.Reu,M.Kleyer,C.Wirth,I.ColinPren-
communities and its importance for matter production, tice, E. Garnier, G. B¨onisch, M. Westoby, H. Poorter,
Ann. Bot. 95, 549 (2005). P. B. Reich, A. T. Moles, J. Dickie, A. N. Gillison, A. E.
[42] S.P.Hubbell,The Unified Neutral Theory of Biodiversity Zanne, J. Chave, S. Joseph Wright, S. N. Sheremet’ev,
and Biogeography, Monographs in Population Biology, H. Jactel, C. Baraloto, B. Cerabolini, S. Pierce, B. Ship-
Vol. 32 (Princeton University Press, 2001). ley, D. Kirkup, F. Casanoves, J. S. Joswig, A. Gu¨nther,
[43] D. Tilman, Resource Competition and Community Struc- V. Falczuk, N. Ru¨ger, M. D. Mahecha, and L. D. Gorn´e,
ture (Princeton University Press, Princeton, New Jersey, The global spectrum of plant form and function, Nature
1982). 529, 167 (2016).

14
[59] J. M. Levine and J. HilleRisLambers, The importance of [70] C.H.Bowler,C.Weiss-Lehman,I.R.Towers,M.M.May-
niches for the maintenance of species diversity, Nature field, and L. G. Shoemaker, Accounting for demographic
461, 254 (2009). uncertainty increases predictions for species coexistence:
[60] S. J. Wright, K. Kitajima, N. J. B. Kraft, P. B. Reich, A case study with annual plants, Ecol. Lett. 25, 1618
I. J. Wright, D. E. Bunker, R. Condit, J. W. Dalling, (2022).
S. J. Davies, S. D´ıaz, B. M. J. Engelbrecht, K. E. Harms, [71] W. F. Laurance, T. E. Lovejoy, H. L. Vasconcelos, E. M.
S. P. Hubbell, C. O. Marks, M. C. Ruiz-Jaen, C. M. Bruna, R. K. Didham, P. C. Stouffer, C. Gascon, R. O.
Salvador, and A. E. Zanne, Functional traits and the Bierregaard, S. G. Laurance, and E. Sampaio, Ecosystem
growth–mortality trade-off in tropical trees, Ecology 91, decay of Amazonian forest fragments: a 22-year investi-
3664 (2010). gation, Conserv. Biol. 16, 605 (2002).
[61] P. B. Adler, R. Salguero-G´omez, A. Compagnoni, J. S. [72] K. A. Harper, S. E. MacDonald, P. J. Burton, J. Chen,
Hsu, J. Ray-Mukherjee, C. Mbeau-Ache, and M. Franco, K. D. Brosofske, S. C. Saunders, E. S. Euskirchen,
Functional traits explain variation in plant life history D. Roberts, M. S. Jaiteh, and P. Esseen, Edge influ-
strategies, Proc. Natl. Acad. Sci. 111, 740 (2014). ence on forest structure and composition in fragmented
[62] K. Jops and J. P. O’Dwyer, Life history complementarity landscapes, Conserv. Biol. 19, 768 (2005).
and the maintenance of biodiversity, Nature 618, 986 [73] A. I. Borthagaray, M. Arim, and P. A. Marquet, Con-
(2023). necting landscape structure and patterns in body size
[63] A. J. Bloom, F. S. Chapin, and H. A. Mooney, Resource distributions, Oikos 121, 697 (2012).
limitation in plants-An economic analogy, Annu. Rev. [74] D. Bernardi, A. Doimo, G. Nicoletti, P. Padmanabha,
Ecol. Syst. 16, 363 (1985). A. Rinaldo, S. Suweis, S. Azaele, and A. Maritan, Habi-
[64] F. S. Chapin, A. J. Bloom, C. B. Field, and R. H. War- tat heterogeneity and dispersal network structure as
ing, Plant responses to multiple environmental factors, drivers of metacommunity dynamics, arXiv (2026),
BioScience 37, 49 (1987). arXiv:2602.06640 [q-bio.PE].
[65] M.S.Umarani,D.Wang,J.P.O’Dwyer,andR.D’Andrea, [75] J. S. Wright, Plant diversity in tropical forests: a review
A spatial signal of niche differentiation in tropical forests, of mechanisms of species coexistence, Oecologia 130, 1
Am. Nat. 203, 445 (2024). (2002).
[66] P. Chesson, Mechanisms of maintenance of species diver- [76] P. B. Adler, J. HilleRisLambers, P. C. Kyriakidis,
sity, Annu. Rev. Ecol. Syst. 31, 343 (2000). Q. Guan, and J. M. Levine, Climate variability has a
[67] B.A.MelbourneandA.Hastings,Extinctionriskdepends stabilizing effect on the coexistence of prairie grasses,
strongly on factors contributing to stochasticity, Nature Proc. Natl. Acad. Sci. 103, 12793 (2006).
454, 100 (2008). [77] K. Jops, J. W. Dalling, and J. P. O’Dwyer, Life history
[68] P. Padmanabha, G. Nicoletti, D. Bernardi, S. Suweis, is a key driver of temporal fluctuations in tropical tree
S. Azaele, A. Rinaldo, and A. Maritan, Landscape and abundances, Proc. Natl. Acad. Sci. 122, e2422348122
environmental heterogeneity support coexistence in com- (2025).
petitive metacommunities, Proc. Natl. Acad. Sci. 121, [78] S. D. Wullschleger and A. W. King, Radial variation in
10.1073/pnas.2410932121 (2024). sap velocity as a function of stem diameter and sapwood
[69] R. Lande, Risks of population extinction from demo- thickness in yellow-poplar trees, Tree Physiol. 20, 511
graphic and environmental stochasticity and random (2000).
catastrophes, Am. Nat. 142, 911 (1993).
---- END DOCUMENT ----
