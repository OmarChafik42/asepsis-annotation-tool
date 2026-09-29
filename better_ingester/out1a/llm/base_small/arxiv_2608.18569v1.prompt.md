Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
The Role of Grid Cells in Reducing Spatial
Aliasing in Hippocampal Place Representations
Alexander Johnson∗ Obadah Ghizawi∗ Ali A. Minai, Senior Member IEEE
Dept. of Electrical Dept. of Electrical Dept. of Electrical
and Computer Engineering and Computer Engineering and Computer Engineering
University of Cincinnati University of Cincinnati University of Cincinnati
Cincinnati, USA Cincinnati, USA Cincinnati, USA
johns9a4@mail.uc.edu ghizawon@mail.uc.edu minaiaa@ucmail.uc.edu
Abstract—Spatial aliasing occurs when two or more distinct tionsandspatialfrequenciesformtriangularlatticesthatcover
locations produce highly similar place-cell representations, pri- any environment visited by an animal [9], [10]. According
marily due to environmental symmetry or repetitive structures. to Bush et al. [9], grid cells provide a context-dependent
This issue is most pronounced when place representations are
spatial metric for path integration and vector navigation,
constructed solely from boundary vector cell (BVC) inputs,
because symmetric or repetitive structures can yield indistin- and these complementary signals interact with place cells to
guishable sensory patterns across multiple locations in an envi- support reliable coding of large environments. In this paper,
ronment.Thisworkintroducesgridcellsignalstomitigatespatial we show that one way that grid cells improve the accuracy
aliasing in such settings. Because grid cells contribute periodic,
of spatial representations is by reducing aliasing. They do
internally generated spatial signals that vary independently of
thisbyintroducingasecondarysourceofinformation,thereby
environmental geometry, they play a key role in disambiguating
perceptually identical locations. We integrate multiple modules disambiguating visually similar locations.
ofanalyticallyconstructedgridcellswithBVC-drivenplacecells Note: The simulator used for this work is part of a larger
andshowthatthisleadstoa94–99%reductioninspatialaliasing hippocampal system simulation platform being developed for
relative to a BVC-only baseline across three environments: an
use with the Webots environment. It will be shared publicly
open environment without obstacles; an environment with a
once it is complete and described fully in a future report.
cross-shapedcentralobstaclecreatinghighvisualsymmetry;and
a maze environment. The greatest improvement occurs in the
II. BACKGROUND
environment with the highest visual symmetry. These results
indicate that grid cells provide information complementary to A. Place Cells
boundary-based inputs, yielding more reliable place representa-
The first report of place-specific activity in hippocampal
tions in geometrically ambiguous environments.
cells was by O’Keefe et al. in 1971 [2]. Place cells (PCs)
Index Terms—grid cells, place cells, spatial navigation, spatial
cognition are primarily located in the CA3 and CA1 regions of the
hippocampus. PCs exhibit location-specific and boundary-
I. INTRODUCTION aware firing, meaning that a given cell fires only when the
Biologically-inspired computational models of spatial cog- animal is in a particular part of the environment (i.e., the
nition aim to replicate the navigational abilities observed in place field) and maintains a tunable distance (and direction)
animals.Thesemodelsareoftenderivedfromthehippocampal from boundaries. For example, when a place cell is recorded
region of the brain, which is known to be central for spatial in a number of rectangular environments, the peak response
mapping and navigation in mammals [1]. Place cells are location of the PC often maintains a fixed distance from the
specialized neurons in the hippocampus that exhibit spatially two nearest walls [11]. A PC’s firing rate is modeled as
localized regions of activity, known as place fields [2]–[4]. a function of the animal’s location through the thresholded
Placefieldfiringpatternshavebeenshowntodependondistal sum of firing rates of several inputs (traditionally, BVCs)
visual cues [5], and especially cues about the distance and [6]. Place cells are a critical component of the system that
locationofwallsandotherobjectsmediatedthroughboundary enable mammals to represent their location within a given
vector cells (BVCs) [6], [7]. However, maps built using only environment.
thesecuesaresusceptibletospatialaliasing,inwhichthesame
B. Head Direction Cells
place cells are activated at multiple spatial locations due to
Head direction cells (HDCs) were first recorded and char-
visual symmetries in the environment [8].
acterized by Taube et al. in 1990. These cells are located in
Grid cells are neurons in the medial entorhinal cortex
the postsubiculum (Brodmann area 48), a key region in the
(MEC),whoseperiodicspatialfiringfieldsatdifferentorienta-
hippocampal formation. Each cell fires rapidly only when the
∗Theseauthorscontributedequallytothiswork. animal’s head is pointing in a restricted range of angles, with
Accepted for Proceedings of WCCI 2026, Maastricht, Netherlands. Copyright IEEE
6202
guA
91
]EN.sc[
1v96581.8062:viXra

themaximumactivationoccurringinapproximatelythemiddle
of this range. This angle is called the preferred direction of
the cell [12]. Together, activated head direction cells provide
a population-coded signal indicating the way an animal is
facingatanygiventime.Headdirectioncellsareanimportant
component of the hippocampus’s navigational circuitry.
C. Boundary Vector Cells
Boundary vector cells (BVCs) were first predicted to exist
through computational models using hippocampal place cells
in 1996 [7], and later in 2000 [6], [13]. BVCs were then
confirmed as a cell type in 2009 by Lever et al. [14]. A
Fig.1:Exampleofspatialaliasinginasingleplacecell.Inthe
BVC fires whenever an environmental boundary intersects a
Cross environment, this neuron exhibits multiple firing-field
receptive field located at a specific distance (i.e., preferred
peaks (four distinct activation maxima), indicating ambiguous
distance) from an animal in a specific allocentric direction.
spatial encoding where separated locations elicit similar place
The firing of a BVC only depends on the animal’s location,
cell responses.
rather than the animal’s heading [14]. BVCs are a key input
to place cells (PCs), as the firing of a PC is a thresholded
sum of the firing of the BVCs connected (via synapses) to it
while maximizing computational efficiency. The goal is not
[6]. This means that BVCs provide critical information about
to reproduce the physiology of gridcells, but to leverage their
surrounding boundaries and their directions to PCs, allowing
functional properties—namely, periodic, metrically consistent
PCs to activate at specific BVC configurations and, thus,
spatialinformation—toreduceplace-fieldaliasingincomplex,
for each PC to have an independent role in the navigational
symmetric environments.
system.
E. Spatial Aliasing
D. Grid Cells
Spatial aliasing is a phenomenon where similar place rep-
Entorhinal grid firing patterns were first discovered by
resentations arise in visually similar locations. This problem
Haftingetal.in2005[10].Thedorsocaudalmedialentorhinal
is especially serious in models in which place cell activity
cortex (dMEC) contains a topographically organized neural
is driven mainly by sensory inputs, such as BVC activity.
representation of space, with the key units being grid cells.
Whilesomespatialaliasinghasbeenobservedinanimals,and
A grid cell exhibits multiple spatial firing fields that form a
evenhumansmayoccasionallybeconfusedbysimilar-looking
periodic hexagonal lattice across the environment. It has been
locations, hippocampal representations of different locations
shown that grids of neighboring cells differ in terms of their
are usually quite distinct and can be used to localize the
vertex locations (i.e., their phases), with the spacing and size
animal’s position in experimental setups [19]–[21]. Recent
of individual fields increasing from dorsal to ventral dMEC
work in our group has shown that, when available, the 3-
[10]. Grid cells are a core component of the MEC, supporting
dimensional structure of the environment may help mitigate
path integration and enabling navigation even in the absence
the problem [8]
of external landmarks.
In this paper, we present a more robust and universally
1) GridCellModeling: Avarietyofcomputationalmodels
applicable solution to spatial aliasing using grid cells.
have been proposed to explain GC firing patterns. These can
be broadly categorized as either dynamical or learning-based
III. MODELARCHITECTURE
models. Dynamical models propose that grid patterns emerge
from the temporal evolution of neural activity. For example, The model consists of four core layers, each modeled
oscillatory inference models [15], [16] rely on interference after its biological counterpart: Head Direction Cell (HDC),
patterns of theta-frequency oscillations, which are modulated Boundary Vector Cell (BVC), Grid Cell (GC), and Place Cell
by velocity. Another dynamical approach is to use continuous (PC)layers.TheHDClayerencodestheagent’sheading,with
attractornetworks(CANs)[17],wheregridpatternsemergeas each cell tuned to a specific allocentric direction. The BVC
stableactivity“bumps”thatshiftinresponsetovelocityinput. layer encodes obstacle and boundary information, with each
Alternatively, learning-based approaches have demonstrated cell exhibiting preferred angular and distance tuning. The GC
that grid-like representations can naturally emerge in deep layer serves as an internal positional signal for the agent and
neural networks trained on vector-based navigation [18]. isorganizedintodiscretemodulesofgridcellpopulations.All
As this work focuses on the functional utility of GCs modulessharethesamespatialscalebutdifferinphaseoffset.
rather than their biological origin, we adopt a direct ana- The PC layer serves as the model’s core spatial representation
lytical approach to their implementation. By explicitly con- andreceivesweightedinputfromboththeBVCandGClayers.
structing grid-like firing patterns using cosine interference, The HDC, BVC, and PC layers are adapted from previous
we achieve precise control over grid scale and orientation models [22], [23].
2

|     |     |     |     |     | where          | θ(t) is     | the agent’s      |             | current             | global      | heading.           | This        | co-   |
| --- | --- | --- | --- | --- | -------------- | ----------- | ---------------- | ----------- | ------------------- | ----------- | ------------------ | ----------- | ----- |
|     |     |     |     |     | sine tuning,   | derived     | from             | the         | dot product         |             | [cosθ(t),sinθ(t)]· |             |       |
|     |     |     |     |     | [cosθh,sinθh], |             | produces         | maximal     |                     | response    | when               | the         | agent |
|     |     |     |     |     | i              | i           |                  |             |                     |             |                    |             |       |
|     |     |     |     |     | faces the      | cell’s      | preferred        | direction,  |                     | decreasing  | smoothly           |             | with  |
|     |     |     |     |     | angular        | deviation.  | This             | formulation |                     | is adapted  |                    | from        | Erdem |
|     |     |     |     |     | and Hasselmo   |             | [24].            |             |                     |             |                    |             |       |
|     |     |     |     |     | C. Boundary    | Vector      | Cell             | Layer       |                     |             |                    |             |       |
|     |     |     |     |     | The Boundary   |             | Vector           | Cell        | (BVC)               | layer       | provides           | geometric   |       |
|     |     |     |     |     | spatial        | information | by               | encoding    | the                 | agent’s     | relationship       |             | to    |
|     |     |     |     |     | environmental  |             | boundaries.      |             | This implementation |             |                    | follows     | the   |
|     |     |     |     |     | boundary       | vector      | formulation      |             | of Barry            | et          | al. [25].          |             |       |
|     |     |     |     |     | Each           | BVC i       | is characterized |             | by                  | a preferred | boundary           |             | dis-  |
|     |     |     |     |     | placement,     | specified   | by               | a radial    | distance            | d           | and an             | allocentric |       |
i
ϕ
|     |     |     |     |     | bearing          | i relative     | to       | the agent.  | The         | layer    | receives    | sensory    |        |
| --- | --- | --- | --- | --- | ---------------- | -------------- | -------- | ----------- | ----------- | -------- | ----------- | ---------- | ------ |
|     |     |     |     |     | input from       | LiDAR          | in       | the form    | of          | per-beam | range       | measure-   |        |
|     |     |     |     |     | ments            | r(t) =         | {r ,r    | ,...,r      | }           | at fixed | allocentric |            | angles |
|     |     |     |     |     |                  |                | 1        | 2           | nres        |          |             |            |        |
|     |     |     |     |     | {θ 1 ,θ 2 ,...,θ | nres           | }, where | n           | res denotes | the      | angular     | resolution |        |
|     |     |     |     |     | of the sensor    | (720           | in       | this work). |             |          |             |            |        |
|     |     |     |     |     | Each             | BVC integrates |          | evidence    | across      |          | all sensor  | beams      | by     |
Fig. 2: Model architecture for spatial representation. Black combiningradialandangularGaussiantuningfunctions.With
arrows indicate excitatory pathways, while red arrows indi- tuning widths σ (distance) and σ (angle), the firing rate of
|                 |                     |            |                    |                             |       |     | r             |                  | θ              |     |                  |                        |     |
| --------------- | ------------------- | ---------- | ------------------ | --------------------------- | ----- | --- | ------------- | ---------------- | -------------- | --- | ---------------- | ---------------------- | --- |
| cate inhibitory | pathways.           | Positional | input              | drives the grid cell        | BVC i | is: |               |                  |                |     |                  |                        |     |
| n e tw o rk ,   | c o m p a ss i n pu | t d r iv   | e s h ea d d ire c | ti on ce l ls , a n d li da | r     |     |               |                  |                |     |                  |                        |     |
|                 |                     |            |                    |                             |       |     | nres (cid:32) | exp (cid:2) −(rj | − d i)2(cid:3) |     | exp (cid:2) −(θj | − ϕ i)2(cid:3)(cid:33) |     |
|                 |                     |            |                    |                             |       | 1   | (cid:88)      |                  |                |     |                  | 2                      |     |
in p ut d ri v e s bo u n da r y v ec t o r c el ls (B V C s ). G rid c e ll a n d B V C vb(t) = √ 2 σ r 2 × √ 2 σ θ ,
i
signals provide afferent excitation to the place cell network, N 2πσ 2πσ
|                |               |     |                     |             |     | BVC | j=1 |     | r   |     |     | θ   |     |
| -------------- | ------------- | --- | ------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| while afferent | and recurrent |     | inhibition regulate | competition |     |     |     |     |     |     |     |     |     |
(2)
and sparsity. Head direction signals provide a shared orienta- where N is the total number of boundary vector cells.
BVC
tion reference between grid and boundary representations. The normalization by N ensures activations remain in
BVC
|     |     |     |     |     | a consistent         | range | for | different | BVC             | population |             | sizes. | Pre-    |
| --- | --- | --- | --- | --- | -------------------- | ----- | --- | --------- | --------------- | ---------- | ----------- | ------ | ------- |
|     |     |     |     |     | ferred displacements |       |     | (d ,ϕ     | ) are uniformly |            | distributed |        | to tile |
i i
| ThemaincontributionofthisworkistheadditionoftheGC |          |          |                    |             |              |        |         |        |           | d        | [0,r    |         | ]    |
| ------------------------------------------------- | -------- | -------- | ------------------ | ----------- | ------------ | ------ | ------- | ------ | --------- | -------- | ------- | ------- | ---- |
|                                                   |          |          |                    |             | the boundary | coding |         | space: | distances | i        | span    | max     | (the |
| layer, which                                      | provides | a metric | spatial coordinate | system that |              |        |         |        |           |          |         |         |      |
|                                                   |          |          |                    |             | maximum      | LiDAR  | range), |        | while     | bearings | ϕ cover | [0,2π). |      |
i
complements the boundary-based representations and enables Thisarrangementensurescomprehensivecoverageofpotential
| stable place | field formation |     | in environments | with geometric |          |                |     |             |     |     |        |     |     |
| ------------ | --------------- | --- | --------------- | -------------- | -------- | -------------- | --- | ----------- | --- | --- | ------ | --- | --- |
|              |                 |     |                 |                | boundary | configurations |     | surrounding |     | the | agent. |     |     |
ambiguity.
|             |            |     |     |     | D. Grid | Cell Layer |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| A. Notation | & Overview |     |     |     |         |            |     |     |     |     |     |     |     |
Theintroductionofgridcellsintothemodelwasmotivated
Foreachofthefourcelltypes—HeadDirection(h),Bound- bythedesiretoaddressakeylimitationofpriormodels:severe
aryVector(b),Grid(g),andPlace(p)—weusethesuperscript place-fieldaliasinginenvironmentswithsymmetryorrepeated
symbols h, b, g, and p, respectively. The time-varying firing geometry. Grid cells provide an internally generated represen-
rate of the ith cell of type k is denoted by vk(t) (or simply tation of space by combining their hexagonal firing patterns.
i
| vk). Similarly, | the time-varying |     | synaptic | weight from the jth |     |     |     |     |     |     |     |     |     |
| --------------- | ---------------- | --- | -------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i This periodic structure provides a unique spatial signature
|     | ith |     |     | Wkl(t) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cell of type l to the cell of type k is denoted as (or at every location. When observing population activity within
ij
Wkl when time indices are omitted). These definitions apply a grid cell module—where cells share a common scale and
ij
throughout all network modules and environments unless orientation but differ in spatial phase—the combined pattern
otherwise specified. becomes highly distinctive. Importantly, this spatial code is
|         |                |       |     |     | not affected      | by  | environmental |      | geometry |              | in the | same        | way |
| ------- | -------------- | ----- | --- | --- | ----------------- | --- | ------------- | ---- | -------- | ------------ | ------ | ----------- | --- |
| B. Head | Direction Cell | Layer |     |     |                   |     |               |      |          |              |        |             |     |
|         |                |       |     |     | as boundary-based |     | input.        | Even | in       | the presence |        | of repeated |     |
The Head Direction Cell (HDC) layer provides a global geometry or symmetrical layouts, the relative phase of grid
orientationsignaltothemodel,whereeachcellhasapreferred cellactivitydiffersacrosslocations,providingtheinformation
allocentric direction. For simplicity, this model uses N = 8 needed to disambiguate them.
h
cells,whosepreferreddirectionsarefixedat0◦,45◦,...,315◦.
|     |     |     |     |     | This | work uses | an  | analytical | approach |     | to grid | cell | mod- |
| --- | --- | --- | --- | --- | ---- | --------- | --- | ---------- | -------- | --- | ------- | ---- | ---- |
θh
Each HDC i has a preferred direction and activates eling: we directly construct the hexagonal periodic struc-
i
according to: ture mathematically rather than simulating underlying neu-
|     | vh(t)=cos |     | (cid:0) θ(t)−θh(cid:1) |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
, (1) ral mechanisms [26]. This provides computational efficiency
|     | i   |     | i   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3

and precise control over spatial properties while maintaining
biological plausibility through post-processing and obstacle-
aware masking. The model implements M = 8 grid cell
modules aligned with head direction cells at orientations
α ∈ {0◦,45◦,...,315◦}, each containing N = 50 cells
m m
sharingacommonspatialscaleλbutdifferinginspatialphase
offset ϕ .
j
1) Analytical Grid Cell Construction: For a grid cell with
orientation α, spatial scale λ, and phase offset ϕ=(ϕ ,ϕ ),
x y
we define the spatial frequency ω = 2π/λ. The position (a) Raw (no masking) (b) Masked (boundary-aware)
x = (x,y) is rotated into the grid cell’s reference frame and
Fig. 3: Boundary-aware masking for grid cell activations in
translated by its phase offset:
an obstacle-filled environment. Without masking (left), acti-
(cid:18) r (cid:19) (cid:18) cosα sinα (cid:19)(cid:18) x−ϕ (cid:19) vations extend across walls. With masking (right), activations
x = x . (3)
r −sinα cosα y−ϕ fragment at barriers while preserving local phase coherence
y y
within each compartment.
The canonical grid pattern is constructed as the mean of
three cosine gratings oriented 60◦ apart:
E. Place Cell Layer
1(cid:104)
G(x)= cos(ωr )
3 x The Place Cell (PC) layer forms the core spatial represen-
+cos (cid:16) ω (cid:0)r 2 x + √ 2 3r y (cid:1)(cid:17) (4) t r a e t c i e o p n tiv o e f t fi h e e ld m s o ( d p e la l. ce Pl fi ac e e lds c ) el t l h s ro d u e g v h elo c p om sp p a e t t i i a ti l v ly e l l o e c a a rn li i z n e g d ,
+cos (cid:16) ω (cid:0)r 2 x − √ 2 3r y (cid:1)(cid:17)(cid:105) . witheachcellencodingaspecificlocationintheenvironment.
ThislayerintegratesinformationfrombothBVCandGClay-
Toachievethesharplytunedfiringfieldsobservedinbiolog- ers: BVCs provide geometric constraints from environmental
ical recordings [10], three post-processing steps are applied. boundaries, while GCs contribute metric phase information
First,apower-lawtransformationadjuststheactivationprofile: that disambiguates perceptually similar locations. The relative
contribution of these two input streams is controlled by
G′(x)=sgn(G)·|G|1/β, (5) a weighting parameter η ∈ [0,1], where BVC inputs are
weighted by (1−η) and GC inputs by η.
where β ∈ [1.2,1.8] controls field sharpness. Second, per-
1) Membrane Dynamics and Activation: The membrane
cellmin-maxnormalizationensuresconsistentdynamicrange. potential sp of place cell i evolves as a leaky integrator
i
Third, soft thresholding creates sparse activations:
combining excitatory input from BVCs and GCs with global
(cid:16) G′′(x)−θ (cid:17) inhibition:
vg(x)=max 0,
1−θ gc
gc , (6)
τ
dsp
i =−sp+E −I , (7)
p dt i i i
where θ controls sparsity.
gc where the excitatory drive is
2) Obstacle-AwareMasking: Analyticalconstructionbased
(cid:88) (cid:88)
on position alone produces activations that extend across E =(1−η) Wpbvb+η Wpgvg, (8)
i ij j ik k
walls, contradicting biological observations where grid cells
j k
fragment at barriers while maintaining phase coherence [27].
and the inhibitory drive is
We address this through a spatial masking procedure applied
(cid:88) (cid:88) (cid:88)
independently to each grid cell. I =(1−η)Γpb vb+ηΓpg vg+Γpp vp. (9)
i j k l
The procedure identifies connected activation components
j k l
(“blobs”) and determines which intersect obstacles. For blobs
where obstacles cover ≥ 20% of their diameter, we apply Here,W i p j bandW i p k g aresynapticweightsfromBVCsandGCs
obstacle masks to split or suppress the activation. When to place cell i; v j b, v k g, and v l p are the firing rates of BVCs,
a blob splits into multiple components, only the largest is GCs, and PCs respectively; and Γpb, Γpg, Γpp are inhibitory
retained. Blobs that remain connected after initial masking gainparametersthatcontrolthestrengthofafferent(boundary
are processed with dilated obstacle boundaries to force frag- and grid) and recurrent (place-to-place) inhibition. The firing
mentation. Finally, Gaussian smoothing (σ ≈ 0.5) restores rate is obtained through rectification and saturation:
biologicallyplausiblecurvededgesthattapernearwallsrather vp =tanh (cid:0) [ψsp] (cid:1) , (10)
than exhibiting sharp cutoffs. i i +
Figure3illustratesthiseffect:rawactivationsextendcontin- where ψ is a gain factor and [·] = max(0,·). This non-
+
uously across walls (left), while masked activations fragment linearity produces sparse, localized place fields through the
at boundaries while preserving local phase coherence (right). combined effects of global inhibition and thresholding.
4

aliasing, 5 trials were conducted for each environment with
grid cells, and another set of 5 trials was conducted without
grid cells. The results across these trials were averaged for
each case tested. Consequently, 10 trials were conducted for
eachenvironment,yieldingatotalof30trials.Inagiventrial,
there were training and evaluation phases. During the training
phase, the agent randomly explored the environment until it
(a) Open (b) Cross (c) Maze had covered at least 95 percent of it. This was calculated by
dividing the environment into a square grid with a bin size of
Fig. 4: Evaluation environments used in experiments: (a)
0.5m and tracking the areas visited until the grid’s coverage
Open, (b) Cross, and (c) Maze. All environments are 20m
reached 95 percent. Bins that overlap with obstacles were not
x 20m in size.
included in this calculation. During the evaluation phase, the
agent explored until it reached 99 percent coverage, with a
bin size of 0.2m, matching the bin size used to calculate the
2) Self-OrganizationviaCompetitiveLearning: Placefields
Mean Spatial Aliasing Index (MSAI) metric (see below).
emerge through competitive learning during exploration.
Synaptic weights Wpb and Wpg are initialized sparsely with B. Model Parameters
ij ik
connection probabilities of approximately 0.25 and 0.30, re-
TABLE I: Neural Cell Populations Used in the Model
spectively, ensuring each place cell receives input from a
Cell Type Number of Cells
distinct subset of BVCs and GCs. During learning, weights
Place Cells 1000
are updated according to Oja’s rule [22], [23], [28]:
Boundary Vector Cells (BVCs) 400
Head Direction Cells 8
τ dW i p j b =(1−η)vp (cid:18) vb− 1 vpWpb (cid:19) , (11) Grid Cells 400
wpb dt i j α i ij
pb Table I summarizes the number of cells used for each of
dWpg (cid:18) 1 (cid:19) the respective cell types within the experiments.
τ ik =ηvp vg− vpWpg , (12)
wpg dt i k α i ik
pg
TABLE II: Boundary Vector Cell Parameters
whereτ ,τ arelearningtimeconstantsandα ,α are
wpb wpg pb pg Parameter Value
normalizationfactorsthatcontrolthestrengthofweightdecay.
Radial Tuning Width (σ ) 1.0m
r
The first term in each equation strengthens synapses when Angular Tuning Width (σ ) 3.0◦
θ
pre- and postsynaptic cells are co-active (Hebbian learning),
BVCs per Direction 50
while the second term normalizes total synaptic input and
Total Number of BVCs 400
enforcescompetitionamongplacecells.Combinedwithglobal
inhibition (I ), this produces winner-take-all dynamics where Table II summarizes the BVC parameters used within the
i
experiments. Along each head direction, 50 BVCs were used.
each place cell specializes to represent a unique combination
AssummarizedinTableI,thereare8headdirections,meaning
ofBVCandGCactivitypatterns,formingaspatiallylocalized
a total of 50 × 8 = 400 BVCs were used in the model.
place field.
IV. EXPERIMENTALSETUP TABLE III: Grid Cell Parameters
Parameter Value
All experiments were conducted using an RTX 3090 GPU
Number of Modules 8
and a Ryzen 9 9900X CPU. The simulation software used
Cells per Module 50
to run the experiments was Webots R2025a. The agent used
Total Number of Grid Cells 400
across the experiments was a Roomba bot with a compass
Spatial Scale (λ) 5.5
for head-direction updates and a rangefinder with 720 beams
Grid Influence Weight (η) 0.35
covering 360 degrees, which provided information directly to
the BVC layer. The rangefinder has a maximum distance of Table III summarizes the grid cell parameters used within
25m, to account for the maximum distance that would need the experiments. Grid cells were divided into 8 modules, with
to be read in a 20m × 20m environment. All environments 50 cells per module, resulting in a total of 50 × 8 = 400
used are 20m × 20m in size. grid cells in the model. A spatial scale of λ = 5.5 yields an
activation diameter of roughly 2.7m. It is important to note
A. Data Collection
that during the ”no grid cell” experiments, η is set to 0 to
Theagentexploredthreeenvironmentsofvaryingcomplex- eliminate any effect of grid cells on the model.
ities. The first is an open environment without obstacles, the
second features cross-shaped walls that divide it into four
regions, and the last is modeled as a maze, as shown in
Fig. 4. To demonstrate the effects of grid cells in mitigating
5

TABLE IV: Place Cell Learning & Inhibition Parameters
Parameter Value
√
BVC Normalization Factor (α ) 0.4≈0.632
pb √
GC Normalization Factor (α ) 0.4≈0.632
pg
Recurrent Inhibition Gain (Γpp) 0.70
BVC Afferent Inhibition Gain (Γpb) 0.35
GC Afferent Inhibition Gain (Γpg) 0.35
Learning Time Constant (τ ) 10 timesteps (960ms)
w
Table IV summarizes the place cell learning and inhibition
√
parameters. Both normalization factors were set to 0.4, and
theafferentinhibitorygainsforBVCandGCinputswereeach
set to half the recurrent inhibition gain.
C. Metrics for Spatial Aliasing
Spatial aliasing was measured using the Spatial Aliasing
Index(SAI)andMeanSpatialAliasingIndex(MSAI)metrics
to examine how place cells responded in different regions of
anenvironment.Forabinilocatedat(x ,y ),theSAIisgiven
i i
by:
N
1 (cid:88)
SAI(i) = 1{∥(x ,y )−(x ,y )∥>d }
N i i j j th
j=1 (13)
j̸=i
(cid:16) (cid:17)
·CosSim a(i),a(j)
Fig.5:SpatialAliasingIndex(SAI)heatmapswithandwithout
where: grid cells across environments. Rows show Open, Cross,
and Maze (top to bottom); columns show with grid cells
• N is the total number of bins.
(left) and without grid cells (right). Color indicates aliasing
• d th is the distance threshold to exclude nearby bins.
magnitude on a logarithmic scale (lower is better). Reported
• 1{·} is the indicator function (equal to 1 if the distance
MeanSpatialAliasingIndex(MSAI)valuesareshownbeneath
between bins exceeds d , and 0 otherwise).
th
• CosSim(a(i),a(j)) is the cosine similarity between the each heatmap.
place cell activation vectors in bins i and j.
To evaluate the model’s overall aliasing performance, the
This section summarizes the results of the model’s perfor-
MSAI is computed as the average of the SAI across all bins:
mance with and without grid cells in three different environ-
1 (cid:88) N ments: Open, Cross, and Maze, as shown in Fig. 4. A total
MSAI= SAI(i) (14) of five trials were conducted for each configuration (with and
N
i=1 without grid cells) in each environment, and the MSAI scores
Larger values of SAI(i) indicate greater spatial aliasing. This were averaged for the five trials. The results are shown in
means that spatially distant bins exhibit similar place-cell Table V.
activation patterns. The MSAI aggregates this effect across Examples of MSAI heatmaps from one trial for all three
the environment, with higher MSAI values suggesting more environmentsareshowninFig.5.Consistentwiththeaveraged
aliasing. Conversely, lower SAI(i) and MSAI values indicate MSAIvaluesinTableV,theheatmapsshowlowerSAIacross
stronger place-cell localization and improved spatial discrim- most spatial bins when grid-cell input is included, with the
ination. most pronounced reduction in the Cross environment. These
visualizationscomplementtheresultsshowninTableVbylo-
V. RESULTS&DISCUSSION
calizing where aliasing is mitigated within each environment.
TABLE V: Mean Spatial Aliasing Index (MSAI, ×10−4) An important detail to consider is how prone a particular
across environments with and without grid cells (GC). Values environment is to aliasing when using place representations
report mean ± standard deviation over five independent trials. based purely on boundary vector cells (BVC). The “Cross”
Environment GC No GC Improvement environment, for example, divides the map into four rotation-
Open 0.3±0.1 5.7±0.3 94.73% ally symmetric quadrants, as shown in Fig. 4. This symmetry
Cross 0.3±0.1 42.4±1.0 99.29% creates sensory similarity within the quadrants, increasing the
Maze 1.3±2.2 38.9±2.7 96.65% potential for place-field aliasing. In models where place rep-
6

| resentations | are | constructed | primarily |     | from | BVC | inputs, such |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --------- | --- | ---- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[8] AndrewGerstenslager,BekarysDukenbaev,andAliA.Minai.Improved
accuracyofrobotlocalizationusing3-dlidarinahippocampus-inspired
| environments | are      | therefore | especially       |     | prone   | to aliasing | [29].      |        |       |           |             |               |       |            |     |
| ------------ | -------- | --------- | ---------------- | --- | ------- | ----------- | ---------- | ------ | ----- | --------- | ----------- | ------------- | ----- | ---------- | --- |
|              |          |           |                  |     |         |             |            | model, | 2025. | Presented | at the 2025 | International | Joint | Conference | on  |
| Adding       | a source | of        | path integration |     | signals | to          | the model, |        |       |           |             |               |       |            |     |
NeuralNetworks,Rome,July2025.
| namely   | grid cells,  | substantially |     | improves |     | the disambiguation |          |                              |       |                |                                      |               |     |         |            |
| -------- | ------------ | ------------- | --- | -------- | --- | ------------------ | -------- | ---------------------------- | ----- | -------------- | ------------------------------------ | ------------- | --- | ------- | ---------- |
|          |              |               |     |          |     |                    |          | [9] Daniel                   | Bush, | Caswell Barry, | and                                  | Neil Burgess. |     | What do | grid cells |
|          |              |               |     |          |     |                    |          | contributetoplacecellfiring? |       |                | TrendsinNeurosciences,37(3):136–145, |               |     |         |            |
| of these | perceptually | similar       |     | regions, | as  | evidenced          | by a re- |                              |       |                |                                      |               |     |         |            |
2014.
ductionofapproximately99.3%intheaveragedMeanSpatial
|     |     |     |     |     |     |     |     | [10] Torkel | Hafting, | Marianne | Fyhn, Sturla | Molden, | May-Britt |     | Moser, and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | ------------ | ------- | --------- | --- | ---------- |
AliasingIndex(MSAI)infivetrialsintheCrossenvironment. EdvardI.Moser.Microstructureofaspatialmapintheentorhinalcortex.
The Open environment exhibits more moderate baseline Nature,436(7052):801–806,2005.
|          |        |                |     |          |     |                 |     | [11] Neil | Burgess         | and John | O’Keefe.  | Neuronal | computations |              | underlying |
| -------- | ------ | -------------- | --- | -------- | --- | --------------- | --- | --------- | --------------- | -------- | --------- | -------- | ------------ | ------------ | ---------- |
| aliasing | due to | fewer repeated |     | boundary |     | configurations. | The |           |                 |          |           |          |              |              |            |
|          |        |                |     |          |     |                 |     | the       | firing of place | cells    | and their | role in  | navigation.  | Hippocampus, |            |
Maze environment shows substantial but more variable im- 6(6):749–762,1996.
provement: although grid cells mitigate much of the BVC- [12] JeffreyS.Taube,RobertU.Muller,andJamesB.Ranck.Head-direction
cellsrecordedfromthepostsubiculuminfreelymovingrats.i.descrip-
induced aliasing, corridors introduce repeated spatial patterns, tionandquantitativeanalysis. JournalofNeuroscience,10(2):420–435,
| whichcancausedistantlocationstoretainmoderatesimilarity |     |     |     |     |     |     |     | 1990. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
in their place-cell representations, contributing to higher and [13] Neil Burgess, Andrew Jackson, Tom Hartley, and John O’Keefe. Pre-
|               |     |              |     |     |     |     |     | dictions | derived | from modelling | the | hippocampal |     | role in | navigation. |
| ------------- | --- | ------------ | --- | --- | --- | --- | --- | -------- | ------- | -------------- | --- | ----------- | --- | ------- | ----------- |
| more variable |     | MSAI values. |     |     |     |     |     |          |         |                |     |             |     |         |             |
Biologicalcybernetics,83(3):301–312,2000.
|     |     |     |     |     |     |     |     | [14] Colin | Lever, Stephen | Burton, | Ali | Jeewajee, | John | O’Keefe, | and Neil |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ------- | --- | --------- | ---- | -------- | -------- |
VI. CONCLUSION&FUTUREWORK
|     |     |     |     |     |     |     |     | Burgess. | Boundary | vector | cells in | the subiculum |     | of the hippocampal |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------ | -------- | ------------- | --- | ------------------ | --- |
Overall, our findings demonstrate that adding a source of formation. JournalofNeuroscience,29(31):9771–9777,2009.
|                  |     |          |        |      |        |       |              | [15] Neil                     | Burgess, | Caswell Barry, | and                             | John O’Keefe. | An  | oscillatory | inter- |
| ---------------- | --- | -------- | ------ | ---- | ------ | ----- | ------------ | ----------------------------- | -------- | -------------- | ------------------------------- | ------------- | --- | ----------- | ------ |
| path integration |     | signals, | namely | grid | cells, | helps | mitigate the |                               |          |                |                                 |               |     |             |        |
|                  |     |          |        |      |        |       |              | ferencemodelofgridcellfiring. |          |                | Hippocampus,17(9):801–812,2007. |               |     |             |        |
degreeofaliasingexhibitedinplace-cellrepresentationsacross [16] Michael E. Hasselmo, Lisa M. Giocomo, and Eric A. Zilli. Grid cell
firingmayarisefrominterferenceofthetafrequencymembranepotential
| environments |      | with varying | degrees        |     | of structural |                 | symmetry.  |                              |           |           |                                    |      |                  |     |            |
| ------------ | ---- | ------------ | -------------- | --- | ------------- | --------------- | ---------- | ---------------------------- | --------- | --------- | ---------------------------------- | ---- | ---------------- | --- | ---------- |
|              |      |              |                |     |               |                 |            | oscillationsinsingleneurons. |           |           | Hippocampus,17(12):1252–1271,2007. |      |                  |     |            |
| Future work  | will | investigate  | the            | use | of an         | attractor-based | grid       |                              |           |           |                                    |      |                  |     |            |
|              |      |              |                |     |               |                 |            | [17] Yoram                   | Burak     | and Ila R | Fiete. Accurate                    |      | path integration |     | in contin- |
| cell model   | and  | whether      | its biological |     | plausibility  |                 | introduces |                              |           |           |                                    |      |                  |     |            |
|              |      |              |                |     |               |                 |            | uous                         | attractor | networks  | of grid cells.                     | PLoS | Computational    |     | Biology,   |
5(2):e1000291,2009.
| different   | trade-offs | in  | aliasing | mitigation |           | and | stability. In |             |            |                 |                |       |          |           |             |
| ----------- | ---------- | --- | -------- | ---------- | --------- | --- | ------------- | ----------- | ---------- | --------------- | -------------- | ----- | -------- | --------- | ----------- |
|             |            |     |          |            |           |     |               | [18] Andrea | Banino,    | Caswell         | Barry, Benigno | Uria, | Charles  | Blundell, | Tim-        |
| particular, | it would   | be  | valuable | to         | implement |     | 3D attractor- |             |            |                 |                |       |          |           |             |
|             |            |     |          |            |           |     |               | othy        | Lillicrap, | Piotr Mirowski, | Alexander      |       | Pritzel, | Martin    | J Chadwick, |
based grid cells (accompanied by other relevant 3D cells, Thomas Degris, Joseph Modayil, et al. Vector-based navigation using
grid-likerepresentationsinartificialagents.Nature,557(7705):429–433,
| such as | BVCs, | place | cells, | and | head direction |     | cells) [8], |     |     |     |     |     |     |     |     |
| ------- | ----- | ----- | ------ | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
2018.
| and examine |     | the unique | challenges |     | that | may arise | by test- |             |              |        |              |     |             |     |            |
| ----------- | --- | ---------- | ---------- | --- | ---- | --------- | -------- | ----------- | ------------ | ------ | ------------ | --- | ----------- | --- | ---------- |
|             |     |            |            |     |      |           |          | [19] Thomas | J. Davidson, | Fabian | Kloosterman, |     | and Matthew |     | A. Wilson. |
ing this implementation in varied, real-world environments. Hippocampal replay of extended experience. Neuron, 63(4):497–507,
| Such extensions |     | would | help | clarify | the challenges |     | associated | 2009. |     |     |     |     |     |     |     |
| --------------- | --- | ----- | ---- | ------- | -------------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
[20] MargaretF.Carr,ShantanuP.Jadhav,andLorenM.Frank.Hippocampal
with scalable, biologically grounded spatial representations replayintheawakestate:apotentialphysiologicalsubstrateofmemory
and move the model toward greater robustness in realistic consolidationandretrieval. NatureNeuroscience,14(2):147–153,2011.
navigation settings. [21] Georg Dragoi and Susumu Tonegawa. Preplay of future place cell
|     |     |     |     |     |     |     |     | sequencesbyhippocampalcellularassemblies. |     |     |     |     | Nature,469(7330):397– |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- |
401,2011.
ACKNOWLEDGMENTS
|     |     |     |     |     |     |     |     | [22] AdedapoAlabi,AliA.Minai,andDieterVanderelst. |     |     |     |     |     | Oneshotspatial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- |
The authors thank Andrew Gerstenslager and Bekarys learningthroughreplayinahippocampus-inspiredreinforcementlearn-
Dukenbaev for helpful discussions and explanations of pre- ingmodel.In2020InternationalJointConferenceonNeuralNetworks,
pages1–8.IEEE,2020.
vious models. All results and analyses presented in this paper [23] Adedapo Alabi, Dieter Vanderelst, and Ali A. Minai. Rapid learning
are solely the work of the authors. ofspatialrepresentationsforgoal-directednavigationbasedonanovel
|     |     |     |            |     |     |     |     | model      | of hippocampal |             | place fields. | Neural    | Networks,       | 161:116–128, |         |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ---------- | -------------- | ----------- | ------------- | --------- | --------------- | ------------ | ------- |
|     |     |     | REFERENCES |     |     |     |     | 2023.      |                |             |               |           |                 |              |         |
|     |     |     |            |     |     |     |     | [24] Ug˘ur | M. Erdem       | and Michael | E.            | Hasselmo. | A goal-directed |              | spatial |
[1] EdvardI.Moser,EmilioKropff,andMay-BrittMoser. Placecells,grid navigationmodelusingforwardtrajectoryplanningbasedongridcells.
cells,andthebrain’sspatialrepresentationsystem.Annu.Rev.Neurosci., EuropeanJournalofNeuroscience,35(6):916–931,2012.
31(1):69–89,2008. [25] CaswellBarry,ColinLever,RobinHayman,TomHartley,SarahBurton,
[2] JohnO’KeefeandJonathanDostrovsky. Thehippocampusasaspatial JohnO’Keefe,KathrynJeffery,andNeilBurgess. Theboundaryvector
| map.                              | preliminary | evidence | from | unit activity |     | in the freely-moving | rat. |                     |          |            |            |         |         |              |     |
| --------------------------------- | ----------- | -------- | ---- | ------------- | --- | -------------------- | ---- | ------------------- | -------- | ---------- | ---------- | ------- | ------- | ------------ | --- |
|                                   |             |          |      |               |     |                      |      | cell                | model of | place cell | firing and | spatial | memory. | Hippocampus, |     |
| BrainResearch,34(1):171–175,1971. |             |          |      |               |     |                      |      | 16(9):765–784,2006. |          |            |            |         |         |              |     |
[3] John O’keefe and Lynn Nadel. The hippocampus as a cognitive map. [26] Hugh T. Blair, Adam C. Welday, and Kechen Zhang. Scale-invariant
Oxforduniversitypress,1978. memory representations emerge from moire´ interference between grid
[4] Phillip J. Best, Aaron M. White, and Ali Minai. Spatial processing in fields that produce theta oscillations: a computational model. Journal
the brain: the activity of hippocampal place cells. Annual review of ofNeuroscience,27(12):3211–3229,2007.
neuroscience,24(1):459–486,2001. [27] Dori Derdikman, Jonathan R. Whitlock, Albert Tsao, Marianne Fyhn,
[5] Robert U. Muller and John L. Kubie. The effects of changes in the TorkelHafting,May-BrittMoser,andEdvardI.Moser. Fragmentation
environment on the spatial firing of hippocampal complex-spike cells. of grid cell maps in a multicompartment environment. Nature Neuro-
JournalofNeuroscience,7(7):1951–1968,1987. science,12(10):1325–1332,2009.
[6] Tom Hartley, Neil Burgess, Colin Lever, Francesca Cacucci, and John [28] E. Oja. Simplified neuron model as a principal component analyzer.
O’Keefe. Modeling place fields in terms of the cortical inputs to the JournalofMathematicalBiology,15(3):267–273,1982.
hippocampus. Hippocampus,10(4):369–379,2000. [29] WilliamE.SkaggsandBruceL.McNaughton. Spatialfiringproperties
[7] John O’Keefe and Neil Burgess. Geometric determinants of the place of hippocampal ca1 populations in an environment containing two
Nature,381(6581):425–428,1996.
fieldsofhippocampalneurons. visuallyidenticalregions. JournalofNeuroscience,18(20):8455–8466,
1998.
7
---- END DOCUMENT ----
