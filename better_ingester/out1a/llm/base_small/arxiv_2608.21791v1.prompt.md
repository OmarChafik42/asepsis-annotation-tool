Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Critical Topological Photonics in Synthetic Dimensions
Mingyuan Chen,1,2 Yuwei Jing,3 Franco Nori,2,∗ and Xue-Jia Yu1,†
1Eastern Institute of Technology, Ningbo 315200, China
2Quantum Information Physics Theory Research Team,
Center for Quantum Computing, RIKEN, Wakoshi, Saitama, 351-0198, Japan
3College of Engineering and Applied Sciences, National Laboratory of Solid State Microstructures,
and Collaborative Innovation Center of Advanced Microstructures, Nanjing University, Nanjing 210023, China
(Dated: August 25, 2026)
Topologicalstatesandcriticalityhavelongbeenregardedasincompatibleingredients: theformer
requires a finite spectral gap, whereas the latter demands its closure. Guided by this view, topo-
logical photonics has focused almost exclusively on gapped phases, treating gap-closing transitions
as mere phase boundaries. In this work, we propose a class of topological states in which topology
coexists with criticality in experimentally accessible synthetic-frequency photonic platforms. In a
one-dimensional(1D)syntheticlattice,weidentifysuchcriticaltopologicalphotonicstatesthrough
midgapdegeneraciesinthesingle-particleentanglementspectrum,anduncoveratopology-enforced
multicritical point that reorganizes the topology of neighboring critical states. We further extend
this framework to two dimensions (2D). Our work provides an experimentally accessible route to
critical topological photonics, and may also inspire novel applications such as critical topological
sensing.
Introduction.—Topological phases of matter are con- retical concept, and their experimental realization is de-
ventionally understood as gapped phenomena: quan- mandingbecausetheytypicallyemergeattransitionsbe-
tized topological invariants such as winding and Chern tweengappedphasescarryingdistincthighertopological
numbers are defined on gapped bulk bands, and the invariants,whichgenerallyrequireengineeredlong-range
bulk-boundary correspondence guarantees robust edge hopping that is difficult to achieve in solid-state materi-
states precisely because the bulk spectral gap prevents als, particularly in higher dimensions [45].
their hybridization with the continuum [1–3]. Over the
On a different front, photonic synthetic frequency di-
past decade, this gap-based framework has been ex-
mensions[18,46–57],realizedthroughdynamicallymod-
tended from electronic systems to photonics, leading
ulated ring resonators, provide a particularly promis-
to the concept of photonic topological insulators [4–18]
ing platform for overcoming these challenges. In such
and enabling a broad range of topological photonic de-
systems, long-range couplings can be independently en-
vices, including robust waveguides, topological lasers,
gineered via discrete radio-frequency modulations, en-
and disorder-tolerant light-routing architectures [19–28].
abling direct access to the long-range hopping processes
Criticality, by contrast, is marked by a vanishing bulk
requiredforcriticaltopology,whilethearchitecturenatu-
spectral gap and is classified into different universality
rally extends to higher synthetic dimensions. This raises
classes determined by a set of critical exponents within
atimelyandintriguingquestion: Canonesystematically
the Landau–Ginzburg paradigm [29, 30]. Consequently,
develop an experimentally accessible protocol for real-
these two notions have long been regarded as mutually
izing critical topological states across different photonic
exclusive, giving rise to the long-standing belief that the
synthetic dimensions?
existenceoftopologicalstatesrequiresabulkspectralgap
and that topological properties are necessarily destroyed In this work, we fill this gap by proposing a pho-
once the bulk band gap closes. tonicrealizationofcriticaltopologicalstatesinsynthetic
frequency dimensions. Using equal-amplitude, opposite-
Recent progress has overturned this dichotomy phase trichromatic modulation in two coupled ring res-
through the discovery of topological physics in quantum onators, we demonstrate the emergence of critical topo-
criticalsystems,whererobusttopologicaledgemodesco- logical photonic states, in which robust edge modes sur-
existwithagaplessbulk[31–44]. Thisconceptualbreak- prisingly persist within a gapless bulk continuum. In
through has given rise to the notion of critical topologi- contrast to previously recognized topological photonics,
calstatesandattractedsignificantrecentattention, asit whose nontrivial topology is characterized by quantized
establishesanewparadigmincondensedmatterandsta- topologicalinvariants,thecriticaltopologicalstatesstud-
tisticalphysics: (i)topologicalstatesarenotrestrictedto ied here possess ill-defined quantized topological invari-
gapped systems and can exhibit richer topological phe- ants and can instead be diagnosed through the entan-
nomena unique to gapless regimes; and (ii) topology can glement spectrum of the bulk wave functions, thus es-
further enrich universality classes even when the critical tablishing an unconventional bulk–boundary correspon-
exponents coincide [35]. Despite these theoretical ad- dence [58–62]. We further investigate phase transitions
vances, critical topological states remain largely a theo- between distinct critical topological photonic states, re-
6202
guA
22
]scitpo.scisyhp[
1v19712.8062:viXra

2
vealing that topology can reorganize criticality and drive
phase transitions within critical regimes. Finally, we ex-
tend these critical topological photonic states to 2D syn-
thetic lattices and provide concrete electro-optic imple-
mentation schemes for both 1D and 2D settings, with
experimentally realistic parameters within reach of cur-
rent synthetic-frequency photonic platforms.
Systemandmodel.—Weconsidertwoidenticalringres-
onatorslabeledA(blue)andB(red)inFig.1(a)[63,64].
Each ring has length L and group velocity v . In the ab-
g
sence of group-velocity dispersion, ring A (B) supports FIG. 1. (a) Schematic of two coupled ring resonators, la-
equally-spaced resonant modes defined as A (B ) at
beled A and B, with coupling strength g. Each ring con-
n n tainsanelectro-opticmodulator(EOM),showninyellow. (b)
frequency ω = ω +nΩ, where ω is the reference fre-
n 0 0 Synthetic-frequency lattice in the supermode basis {C ,D }
quency, n is the mode index, and Ω = 2πv /L is the n n
g with intra-cell hopping J and inter-cell hoppings J , J . (c)
0 1 2
free spectral range (FSR) of the ring [56]. Modes A n Topological phase diagram in the (J /J ,J /J ) plane, ex-
1 0 2 0
and B with the same mode index n can be coupled ei- hibiting three gapped phases distinguished by the winding
n
therbyevanescentcouplingorbyafibercouplerbetween number W = 0,1,2, separated by three critical lines (blue,
the two rings, with coupling strength g. One electro- red, and green) that meet at a multicritical point (red star).
opticmodulator(EOM)isplacedineachring,anddriven
by equal-amplitude, opposite-phase trichromatic signals,
J (t)=2
(cid:80)2
J cos(Ω t+ϕ )andJ (t)=−J (t),re- RF drive amplitudes with frequencies Ω ,Ω , and J is
A j=0 j j j B A 1 2 0
spectively[65,66]. Here,{J },{Ω },and{ϕ }detotethe setastheenergyunit. FouriertransformingEq.(2)along
j j j
modulation amplitudes, frequencies, and phases of the the synthetic frequency axis yields the Bloch Hamilto-
three RF components, respectively. The system Hamil- nian H(k ) = h (k )σ +h (k )σ , where k denotes
f x f x y f y f
tonian reads the Bloch momentum in the synthetic frequency dimen-
sion (throughout this work, the subscript f labels quan-
(cid:88) (cid:88)
H = ω (a†a +b†b )+g (a†b +a b†)
0 n n n n n n n n n titiesinthissyntheticspace), h x (k f )=J 0 +J 1 cos(k f )+
+ n (cid:88)(cid:0) J (t)a†a +J (t n )b†b (cid:1) . (1) c J h 2 i c r o a s l ( s 2 y k m f ) m , e a t n r d y σ h y H (k ( f k ) = )σ J 1 = si − n( H k f (k )+ ) J p 2 la s c i e n s (2 t k h f e ) m . o T d h e e l
A n n′ B n n′ z f z f
n,n′ in the AIII class of the tenfold classification [3, 67]. The
boundary zero modes discussed below are protected as
Here, a n and b n (a† n and b† n ) are the annihilation (cre- long as perturbations preserve this chiral structure, i.e.,
ation) operators for the cavity modes A n and B n , re- {δH,σ z } = 0. Equivalently, the off-diagonal element
spectively. The coupling strength g hybridizes the reso- G(k
f
)=h
x
+ih
y
=J
0
+J
1
eikf+J
2
e2ikf definesaninteger
n m a o n d t e m C o n d w es it a h t fr f e re q q u u e e n n c c y y (ω ω n n + in g t ) o a t n h d e t s h y e m a m nt e i t s r y i m c m su e p t e r r ic - w ph in a d se in d g ia n g u r m am b , er sh W ow = nin 2 1 π F i i (cid:72) g. d 1 k ( f c ∂ ) k c f o l n n ta G in . s T th h r e ee re g s a u p lt p in ed g
supermode D n with frequency (ω n −g). These super- phasesW =0,1,2,separatedbycriticallinesalongwhich
modesformafrequencylatticewithalternatingspacings G(k ) vanishes: W = 0 ↔ 1 (blue), W = 0 ↔ 2 (red),
f
Ω 0 ≡ 2g and √ Ω 1 ≡ Ω − 2g. We in √ troduce operators and W =1↔2 (green).
c =(a +b )/ 2andd =(a −b )/ 2astheannihila-
n n n n n n Critical topological photonic state.—Thecentraltheme
tionoperatorsforthesupermodesC andD . Wechoose
n n of this work is to uncover topological phenomena emerg-
thethree drivefrequencies asΩ =2g, Ω =Ω−2g, and
0 1 ing at criticality in synthetic frequency dimensions. To
Ω = 2Ω−2g to match the inter-supermode spacings.
2 this end, we trace the evolution of the open-boundary
Moving to the rotating frame through c˜
n
= c
n
ei(ωn+g)t
eigenfrequency spectrum by fixing J /J =2.5 and tun-
and d˜
n
= d
n
ei(ωn−g)t removes the supermode onsite
ing J /J from 0 to 2.5. As shown in
1
Fig
0
. 2(a), the zero-
2 0
frequencies. Under the rotating-wave approximation,
frequency mode continuously evolves from the W = 1
the remaining counter-rotating and off-resonant inter-
phase to the W = 2 phase, accompanied by a bulk-
supermode processes are neglected, yielding
gap closing at (J /J ,J /J ) = (2.5,1.5). While band-
1 0 2 0
H =
(cid:88)Ä
J c˜†d˜ +J d˜†c˜ +J d˜†c˜
ä
+H.c. (2)
touchingsingularitiesfrequentlyariseintopologicalpho-
0 n n 1 n n−1 2 n n−2 tonics [68, 69], the closing of the bulk gap alone does
n
not establish the emergence of criticality. To deter-
Here, the RF phases have been chosen as ϕ = 0. This mine the nature of this band-touching point, we exam-
j
realizesabipartitetight-bindingchainwithnext-nearest- ine the scaling of the half-chain entanglement entropy
neighbor inter-sublattice hopping in the synthetic fre- S. For a 1D conformally invariant critical point, con-
quencydimension,asdepictedinFig.1(b). Thehopping formal field theory predicts the universal scaling relation
amplitudes J are independently controlled by the two S(N )= c lnN +s ,wherecdenotesthecentralcharge
1,2 f 3 f 0

3
|     |     |     |     |     |     |     | indicate |        | the presence |       | of topologically |            | protected     |     | bound-  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------------ | ----- | ---------------- | ---------- | ------------- | --- | ------- |
|     |     |     |     |     |     |     | ary      | modes. | As           | shown | in Fig.          | 2(d),      | the           | W   | = 1 ↔ 2 |
|     |     |     |     |     |     |     | critical | point  | exhibits     |       | a twofold        | degeneracy |               | at  | ξ = 1/2 |
|     |     |     |     |     |     |     | in the   | bulk   | entanglement |       | spectrum,        |            | in one-to-one |     | corre-  |
spondencewiththeboundary-modedegeneracyobserved
|     |     |     |     |     |     |     | in Fig.       | 2(c). | These      | results | demonstrate      |         | that      | the      | bound-     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ---------- | ------- | ---------------- | ------- | --------- | -------- | ---------- |
|     |     |     |     |     |     |     | ary           | modes | embedded   |         | in the gapless   |         | continuum |          | are topo-  |
|     |     |     |     |     |     |     | logically     |       | protected, | rather  | than             | arising |           | from     | accidental |
|     |     |     |     |     |     |     | localization. |       | Because    |         | the entanglement |         |           | spectrum | is de-     |
|     |     |     |     |     |     |     | termined      |       | entirely   | by the  | single-particle  |         |           | band     | projector, |
thisdiagnosticadmitsquantum–classicalcorrespondence
|     |     |     |     |     |     |     | and | can | be reconstructed |     | from | phase-sensitive |     |     | measure- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- | --------------- | --- | --- | -------- |
mentsonthesynthetic-frequencyplatform(seeEndMat-
|     |     |     |     |     |     |     | ter                           | and SM     | Sec.     | II [71]  | for the  | measurement |                    |           | protocol). |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | ---------- | -------- | -------- | -------- | ----------- | ------------------ | --------- | ---------- |
|     |     |     |     |     |     |     | The                           | robustness |          | of these | critical | boundary    |                    | modes     | against    |
|     |     |     |     |     |     |     | symmetry-preserving           |            |          |          | disorder | is further  |                    | discussed | in the     |
|     |     |     |     |     |     |     | SM                            | Sec.       | IV [71]. |          |          |             |                    |           |            |
|     |     |     |     |     |     |     | Wenowturntothephysicalpicture |            |          |          |          |             | underlyingcritical |           |            |
FIG.2. Evidenceforacriticaltopologicalphotonicstateon
|      |                     |         |                          |     |            |     | topology. |       | In conventional |      | topological     |     | photonics, |        | bound-  |
| ---- | ------------------- | ------- | ------------------------ | --- | ---------- | --- | --------- | ----- | --------------- | ---- | --------------- | --- | ---------- | ------ | ------- |
| theW | =1↔2transitionline. |         | (a)Open-boundaryspectrum |     |            |     |           |       |                 |      |                 |     |            |        |         |
|      |                     |         |                          |     |            |     | ary       | modes | arise           | from | mass inversion: |     | a          | domain | wall in |
| as a | function            | of J /J | for an extended          | SSH | chain with | N = |           |       |                 |      |                 |     |            |        |         |
|      |                     | 2       | 0                        |     |            | f   |           |       |                 |      |                 |     |            |        |         |
40 unit cells and J /J = 2.5. The green hexagon marks the mass term binds a localized state [72]. This picture
1 0
the critical point J /J = 1.5. (b) Bipartite entanglement fails once the gap closes and the mass vanishes. Writ-
2 0
| entropy   | scaling  | at the        | same critical        | point,   | computed  | under             |       |       |       |               |      |      |              |     |         |
| --------- | -------- | ------------- | -------------------- | -------- | --------- | ----------------- | ----- | ----- | ----- | ------------- | ---- | ---- | ------------ | --- | ------- |
|           |          |               |                      |          |           |                   | ing   | k f = | π+q   | and expanding |      | the  | off-diagonal |     | element |
| a n ti –p | e r io d | ic b o u n da | r y c o nd it io n s | u p to N | = 2 0 0 0 | u n it c el l s . |       |       |       |               |      |      |              |     |         |
|           |          |               |                      | f        |           |                   | gives | G     | ≃ m + | iκq −         | Aq2, | with | m =          | J − | J + J , |
(c ) O p e n -b o un d a r y e n er g y sp e c tr u m a t th e cr it ic a l p o in t f o r 0 1 2
|     |      |        |                 |                   |     |       | κ = | 2J  | −J , and | A   | = 2J | −J  | /2. The | critical | lines |
| --- | ---- | ------ | --------------- | ----------------- | --- | ----- | --- | --- | -------- | --- | ---- | --- | ------- | -------- | ----- |
|     | unit | cells. | The inset shows | the corresponding |     | wave- |     | 2   | 1        |     | 2    | 1   |         |          |       |
N f =30
functionintensities|ψ |2 alongthesynthetic-frequencychain. are fixed by m = 0, along which κ = J 2 −J 0 changes
j
(d)Single-particleentanglementspectrumwithN =80unit sign at the multicritical point while A > 0 stays finite.
|        |     |     |     |     | f   |     | The  | zero-mode |             | equation      | (A∂2  | +κ∂   | )ψ          | = 0 then      | yields   |
| ------ | --- | --- | --- | --- | --- | --- | ---- | --------- | ----------- | ------------- | ----- | ----- | ----------- | ------------- | -------- |
| cells. |     |     |     |     |     |     |      |           |             |               |       | x     | x           |               |          |
|        |     |     |     |     |     |     | ψ(x) | ∼         | exp(−κx/A), |               | bound | at a  | termination |               | only for |
|        |     |     |     |     |     |     | κ>0, | i.e.      | J >J        | . Criticality |       | alone | is thus     | insufficient: |          |
|        |     |     |     |     |     |     |      |           | 2           | 0             |       |       |             |               |          |
and s 0 is a nonuniversal constant [70]. As shown in the sign of the kinetic coefficient, not a mass gap, selects
Fig. 2(b), the observed logarithmic scaling firmly estab- the W = 1 ↔ 2 branch as topological and sets the lo-
lishes that the W = 1 ↔ 2 transition realizes a genuine calization length A/|κ|, which diverges as κ → 0. This
conformal critical point rather than an accidental band kinetic-inversion mechanism[37](seealsoSMSec.I[71])
| touching. |     |     |     |     |     |     | is the | gapless | counterpart |     | of  | Jackiw–Rebbi. |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----------- | --- | --- | ------------- | --- | --- | --- |
Havingestablishedthecriticalnatureofthetransition, Topologically enforced multicriticality in photonics.—
we next examine whether topological boundary modes After identifying critical topological states in photonic
persistinthecriticalregime. Figure2(c)showstheeigen- systems, we next examine how nontrivial topology is
frequencyspectrumofanopensynthetic-frequencychain reorganized along critical phase boundaries, namely at
with N = 30 unit cells at the critical band-touching multicriticalpointsseparatingtopologicallydistinctcrit-
f
point. Remarkably, twodegeneratestatesremainpinned ical states. This phenomenon is fundamentally different
at zero frequency despite being embedded within the from that in conventional topological photonics, where
|         |      |            |           |         |         |      | multicritical |     | points | typically |     | arise | as intersections |     | of dis- |
| ------- | ---- | ---------- | --------- | ------- | ------- | ---- | ------------- | --- | ------ | --------- | --- | ----- | ---------------- | --- | ------- |
| gapless | bulk | continuum. | The inset | further | reveals | that |               |     |        |           |     |       |                  |     |         |
their wave functions are strongly localized at the system tinct universality classes characterized by different cen-
| boundaries,indicatingthepresenceoftwofold-degenerate |     |     |     |     |     |     | tral | charges. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
boundary modes. To assess their physical origin, we Specifically, we consider the trajectory J /J =
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
note that in conventional topological photonics, bound- J /J −1 that follows the critical lines, and tune J /J
|     |     |     |     |     |     |     | 1   | 0   |     |     |     |     |     |     | 1 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ary states are protected by a quantized bulk topological from 1.5 to 2.5 in Fig. 1(c). The central charge ex-
invariant via the bulk–boundary correspondence [1, 4]. tracted from the entanglement entropy scaling is shown
At criticality, however, the bulk invariant becomes ill- in Fig. 3(a). Notably, the central charge remains c = 1
defined since the band gap closes. In this context, the throughout but drops abruptly to zero at J /J = 2.0,
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
notion of topology can instead be diagnosed through signaling a transition between distinct critical lines that
the entanglement spectrum of the bulk state, following nonetheless share the same central charge. To further
therecentlyproposedgeneralizedLi–Haldanecorrespon- characterize this transition, we analyze the number of
dence [62] (see End Matter for details). Within this topological edge modes via the bulk entanglement spec-
framework, entanglement eigenvalues pinned at ξ = 1/2 trum,andfindthatthenumberoftopologicalzeromodes

4
FIG. 3. (a) Effective central charge scaling along the criti-
cal trajectory J = J −J . The system size is N = 2000
2 1 0 f
unit cells. (b) Number of boundary zero modes as a func-
FIG. 4. 2D extension of critical topological photonics. (a,
tion of J 1 /J 0 along the critical line. (c, i)–(c, iii) Schematic b)Single-particleentanglementspectraoftheextendedQWZ
photonic single-particle energy spectra: linear dispersion in
model at λ=1 for (a) the conventional critical point M =3
the topologically trivial regime (J 1 /J 0 = 1.5, J 2 /J 0 = 0.5), and(b)thecriticaltopologicalpointM =−1. Thefinitefre-
quadratic band touching at the multicritical point (J 1 /J 0 = quencydirectioncontainsN =40unitcells,themomentum
2.0, J 2 /J 0 = 1.0), and linear dispersion at shifted momen- k issampledwithN =80 f 0,andthehorizontalaxisismea-
tum in the topologically nontrivial regime (J 1 /J 0 = 3.0, su x red relative to the k g x ap-closing momentum, δk = k −k∗,
J 2 /J 0 =2.0). with k∗ = 0 for M = 3 and k∗ = π for M = −1 x . Th x e colo x r
x x
indicates the mean frequency position of the entanglement
eigenstate. (c, d) Time-averaged probability density ρ(x,y)
also changes discontinuously at J /J = 2.0: the adja- of the same edge-localized Gaussian wavepacket evolved in a
1 0
cent critical regimes host zero and two boundary modes, 50×50 open lattice.
respectively. This topologically enforced transition can
be further visualized by the evolution of the eigenfre-
quency spectrum along the critical state, as shown in resonator array, whereas the nearest- and next-nearest-
Fig. 3(c). The band dispersion evolves from linear in neighbor couplings along the frequency dimension are
the trivial critical state to quadratic at the multicriti- generatedbythecorrespondingelectro-opticmodulation
cal point, and back to linear in the critical topological tones. Details of the real-space hopping matrices, the
state, while boundary modes emerge only after crossing global phase diagram, and potential experimental imple-
the multicritical point into the critical topological state. mentations are provided in Sec. III of the SM [71].
Therefore, this provides a new mechanism for multicrit- Thishigher-dimensionalsettingenablestherealization
icality, driven by changes in the topology of neighboring of critical states with distinct topological characteristics
critical lines, which lies beyond the conventional frame- within a single synthetic platform. In Fig. 4, we focus
work of topological photonics. on two representative points along the critical line. The
Extension to 2D synthetic frequency space.—The point (M,λ)=(3,1) corresponds to a topologically triv-
synthetic-frequency construction can be naturally gen- ial critical state separating the C = 0 and C = −1
eralized to higher dimensions by combining a real-space Chern insulating phases, whereas (M,λ) = (−1,1) re-
resonatorarraywiththefrequencylatticeassociatedwith alizes a critical topological state between the C =1 and
eachringresonator. Asaconcreteexample,weconsidera C = 2 Chern insulators. The distinction between these
hybrid2DlatticedescribedbyanextendedQi-Wu-Zhang two critical states is directly encoded in their entangle-
(QWZ) model with long-range hopping [15, 37, 73], ment spectra, computed under periodic boundary con-
ditions along the real-space direction and open bound-
H(k ,k )=(sink +λsin2k )σ +sink σ ary conditions along the synthetic frequency dimension.
x f f f x x y
(3)
+(M −cosk −λcos2k −cosk )σ . As shown in Figs. 4(a, b), the trivial critical state ex-
f f x z
hibits no chiral boundary modes, whereas the topolog-
Here, k denotes the momentum along the real-space di- ical critical state hosts a pair of chiral entanglement
x
rection, while k labels the momentum along the syn- modes crossing at ξ = 1/2. Moreover, this topologi-
f
thetic frequency dimension. The Pauli matrices act on cal distinction is further reflected in the real-space dy-
the two resonator modes (a ,b ). Nearest-neighbor namics. As illustrated in Figs. 4(c, d), an edge-localized
i,n i,n
couplingalongthereal-spacedirectionisprovidedbythe Gaussian wavepacket rapidly disperses into the gapless

5
bulk for (M,λ) = (3,1), whereas it remains confined to
the boundary for (M,λ) = (−1,1). Therefore, the pro-
posed synthetic-frequency architecture offers a versatile
∗ fnori@riken.jp
platform for extending critical topological photonics to
† xuejiayu@eitech.edu.cn
higher-dimensional synthetic lattices. [1] M. Z. Hasan and C. L. Kane, Colloquium: Topological
DiscussionandConcludingremarks.—Beyondadvanc- Insulators, Rev. Mod. Phys. 82, 3045 (2010).
ing the conceptual understanding of topological photon- [2] X.-L. Qi and S.-C. Zhang, Topological Insulators and
ics,ourresultsalsopointtowardnovelcriticaltopological
Superconductors, Rev. Mod. Phys. 83, 1057 (2011).
[3] C.-K. Chiu, J. C. Y. Teo, A. P. Schnyder, and S. Ryu,
photonic devices and suggest a possible route to critical
ClassificationofTopologicalQuantumMatterwithSym-
topologicalsensingdistinctfromconventionaltopological
metries, Rev. Mod. Phys. 88, 035005 (2016).
sensors [74, 75]. Rather than approaching a gap closing [4] T.Ozawa,H.M.Price,A.Amo,N.Goldman,M.Hafezi,
where ordinary gap protection deteriorates, the present L. Lu, M. C. Rechtsman, D. Schuster, J. Simon, O. Zil-
setting places the sensor at a critical point that still car- berberg, and I. Carusotto, Topological Photonics, Rev.
ries a topological boundary structure. This may allow Mod. Phys. 91, 015006 (2019).
[5] L. Lu, J. D. Joannopoulos, and M. Soljačić, Topological
enhanced critical response to coexist with symmetry-
Photonics, Nat. Photonics 8, 821 (2014).
protected noise filtering: symmetry-preserving perturba-
[6] D. Leykam, H. Xue, B. Zhang, and Y. D. Chong, Lim-
tionsaresuppressed,whilesignalsthatbreakorshiftthe
itations and Possibilities of Topological Photonics, Nat.
protected structure, such as local frequency shifts, can Rev. Phys. 8, 55 (2026).
be selectively detected. Further exploration of these po- [7] K. Y. Bliokh, D. Smirnova, and F. Nori, Quantum spin
tential applications is left for future work. Hall effect of light, Science 348, 1448 (2015).
In summary, we have proposed an experimentally ac- [8] J.-S. Tang, W. Nie, L. Tang, M. Chen, X. Su, Y. Lu,
F. Nori, and K. Xia, Nonreciprocal single-photon band
cessible route to critical topological photonics in syn-
structure, Phys. Rev. Lett. 128, 203602 (2022).
thetic frequency dimensions. Building on two coupled
[9] A. B. Khanikaev and G. Shvets, Two-dimensional topo-
ring resonators with trichromatic electro-optic modula-
logical photonics, Nat. Photonics 11, 763 (2017).
tion,westudyanextendedSSHchainwithindependently [10] A. B. Khanikaev, S. Hossein Mousavi, W.-K. Tse,
tunable long-range hopping, providing a minimal plat- M. Kargarian, A. H. MacDonald, and G. Shvets, Pho-
form for realizing critical topology in photonics. Unlike tonic topological insulators, Nat. Mater. 12, 233 (2013).
conventional topological photonics, the critical topolog- [11] J.Chen,Y.Zheng,S.Yang,A.Alù,Z.-Y.Li,andC.-W.
Qiu,Chern-protectedflatbandedgestateinmetaphoton-
ical photonic states identified here feature robust topo-
ics, Phys. Rev. Lett. 134, 223806 (2025).
logical boundary modes that coexist with a gapless bulk
[12] Y.-R. Zhang, Y. Zeng, H. Fan, J. Q. You, and F. Nori,
continuum. The diagnosis of such critical topology is
Characterization of topological states via dual multipar-
also fundamentally unconventional: ordinary quantized tite entanglement, Phys. Rev. Lett. 120, 250501 (2018).
topological invariants become ill-defined, and topolog- [13] K.Y.Bliokh,D.Leykam,M.Lein,andF.Nori,Topolog-
ical boundary modes are instead faithfully encoded in icalnon-HermitianoriginofsurfaceMaxwellwaves,Nat.
degeneratemidgapstatesofthebulkentanglementspec- Commun. 10, 580 (2019).
[14] D. Leykam, K. Y. Bliokh, and F. Nori, Edge modes
trum. Wefurtherinvestigatetopologicallyenforcedmul-
in two-dimensional electromagnetic slab waveguides:
ticriticalitybetweendistinctcriticaltopologicalphotonic
Analogsofacousticplasmons,Phys.Rev.B102,045129
states, where topology actively drives a phase transition
(2020).
within the critical regime. Guided by the same design [15] Y. Che, C. Gneiting, T. Liu, and F. Nori, Topological
principle, the critical topological physics revealed above quantum phase transitions retrieved through unsuper-
naturally extends to 2D synthetic lattices. Addition- visedmachinelearning,Phys.Rev.B102,134213(2020).
ally, we have proposed concrete electro-optic implemen- [16] A. B. Khanikaev and A. Alù, Topological photonics: ro-
tationswithexperimentallyrealisticparametersforboth
bustness and beyond, Nat. Commun. 15, 931 (2024).
[17] A. Vakulenko, S. Kiriushechkina, D. Smirnova, S. Gud-
the one- and 2D settings, indicating that the proposed
dala, F. Komissarenko, A. Alù, M. Allen, J. Allen, and
critical topological photonic states are within reach of
A. B. Khanikaev, Adiabatic topological photonic inter-
existing synthetic-frequency platforms. faces, Nat. Commun. 14, 4629 (2023).
Acknowledgement: We thank Professors Luqi Yuan, [18] C. Leefmans, A. Dutt, J. Williams, L. Yuan, M. Parto,
Xiaoze Liu, Meng Xiao for helpful discussions. X.-J. Yu F.Nori,S.Fan,andA.Marandi,Topologicaldissipation
in a time-multiplexed photonic resonator network, Nat.
was supported by the National Natural Science Founda-
Phys. 18, 442 (2022).
tion of China (Grant No.12405034) and a start-up grant
[19] I. Amelio and I. Carusotto, Theory of the coherence of
from Eastern Institute of Technology, Ningbo. F. N. is
topological lasers, Phys. Rev. X 10, 041060 (2020).
supported in part by the Japan Science and Technology [20] G. Harari, M. A. Bandres, Y. Lumer, M. C. Rechtsman,
Agency (JST) [via the CREST Quantum Frontiers pro- Y. D. Chong, M. Khajavikhan, D. N. Christodoulides,
gramGrantNo. JPMJCR24I2,theQuantumLeapFlag- and M. Segev, Topological insulator laser: Theory, Sci-
shipProgram(Q-LEAP),andtheMoonshotR&DGrant ence 359, eaar4003 (2018).
[21] M. A. Bandres, S. Wittek, G. Harari, M. Parto, J. Ren,
No. JPMJMS2061].

6
M. Segev, D. N. Christodoulides, and M. Khajavikhan, metryprotectedtopologicalstates,Phys.Rev.Lett.133,
Topological insulator laser: Experiments, Science 359, 026601 (2024).
eaar4005 (2018). [41] W.-H.Zhonget al.,Quantumentanglementoffermionic
[22] L. Yang, G. Li, X. Gao, and L. Lu, Topological-cavity symmetry-enrichedquantumcriticalpointsinonedimen-
surface-emitting laser, Nat. Photonics 16, 279 (2022). sion, Phys. Rev. B 112, 075129 (2025).
[23] C.Lu,C.Wang,M.Xiao,Z.-Q.Zhang,andC.-T.Chan, [42] S.Yanget al.,Deconfinedcriticalityasintrinsicallygap-
Topological rainbow concentrator based on synthetic di- lesstopologicalstateinonedimension,Phys.Rev.B113,
mension, Phys. Rev. Lett. 126, 113902 (2021). L201105 (2026).
[24] J. Chen, Y. Zheng, S. Yang, F. Shi, Z.-Y. Li, and C.- [43] R.Flores-Calderón,E.J.König,andA.M.Cook,Topo-
W.Qiu,One-wayvalley-robusttransportinedge-tailored logical quantum criticality from multiplicative topologi-
photonic crystals, Phys. Rev. Lett. 134, 203803 (2025). cal phases, Phys. Rev. Lett. 134, 116602 (2025).
[25] C.R.Leefmans,M.Parto,J.Williams,G.H.Li,A.Dutt, [44] D. E. Parker, T. Scaffidi, and R. Vasseur, Topological
F. Nori, and A. Marandi, Topological temporally mode- Luttinger liquids from decorated domain walls, Phys.
locked laser, Nat. Phys. 20, 852 (2024). Rev. B 97, 165114 (2018).
[26] R. Kumar, Chandan, G. I. Lopez Morales, R. Monge, [45] L. Zhou et al., Topological edge states at Floquet quan-
A. Vakulenko, S. Kiriushechkina, A. B. Khanikaev, tum criticality, Commun. Phys. 8, 214 (2025).
J. Flick, and C. A. Meriles, Emission of nitrogen– [46] D.Yu,W.Song,L.Wang,R.Srikanth,S.KaushikSrid-
vacancy centres in diamond shaped by topological pho- har, T. Chen, C. Huang, G. Li, X. Qiao, X. Wu, et al.,
tonic waveguide modes, Nat. Nanotechnol. 20, 1605 Comprehensive review on developments of synthetic di-
(2025). mensions, Photon. Insights 4, R06 (2025).
[27] S. Barik, A. Karasahin, C. Flower, T. Cai, H. Miyake, [47] L.Yuan,Q.Lin,M.Xiao,andS.Fan,SyntheticDimen-
W. DeGottardi, M. Hafezi, and E. Waks, A topological sion in Photonics, Optica 5, 1396 (2018).
quantum optics interface, Science 359, 666 (2018). [48] T.OzawaandH.M.Price,TopologicalQuantumMatter
[28] H. Price, Y. Chong, A. Khanikaev, H. Schomerus, L. J. in Synthetic Dimensions, Nat. Rev. Phys. 1, 349 (2019).
Maczewsky,M.Kremer,M.Heinrich,A.Szameit,O.Zil- [49] A. Dutt, M. Minkov, Q. Lin, L. Yuan, D. A. B. Miller,
berberg, Y. Yang, et al., Roadmap on topological pho- and S. Fan, Experimental Band Structure Spectroscopy
tonics, J. Phys. Photonics 4, 032501 (2022). along a Synthetic Dimension, Nat. Commun. 10, 3122
[29] S. Sachdev, Quantum Phase Transitions (Cambridge (2019).
University Press, 2011). [50] A.Dutt,L.Yuan,K.Y.Yang,K.Wang,S.Buddhiraju,
[30] J. Cardy, Scaling and Renormalization in Statistical J. Vučković, and S. Fan, Creating boundaries along a
Physics (Cambridge University Press, 1996). synthetic frequency dimension, Nat. Commun. 13, 3377
[31] T. Scaffidi, D. E. Parker, and R. Vasseur, Gapless (2022).
Symmetry-ProtectedTopologicalOrder,Phys.Rev.X7, [51] L. Yuan, A. Dutt, and S. Fan, Synthetic Frequency Di-
041048 (2017). mensions in Dynamically Modulated Ring Resonators,
[32] R. Verresen, N. G. Jones, and F. Pollmann, Topology APL Photonics 6, 071102 (2021).
andEdgeModesinQuantumCriticalChains,Phys.Rev. [52] L. Yuan, Y. Shi, and S. Fan, Photonic gauge potential
Lett. 120, 057001 (2018). in a system with a synthetic frequency dimension, Opt.
[33] R. Verresen, R. Thorngren, N. G. Jones, and F. Poll- Lett. 41, 741 (2016).
mann, Gapless Topological Phases and Symmetry- [53] R. Mao, X. Xu, J. Wang, C. Xu, G. Qian, H. Cai, S.-Y.
Enriched Quantum Criticality, Phys. Rev. X 11, 041059 Zhu, and D.-W. Wang, Measuring Zak phase in room-
(2021). temperature atoms, Light: Sci. & Appl., 11, 291 (2022).
[34] X.-J. Yu, R.-Z. Huang, H.-H. Song, L. Xu, C. Ding, and [54] Z.-A.Wang,X.-D.Zeng,Y.-T.Wang,J.-M.Ren,C.Ao,
L.Zhang,ConformalBoundaryConditionsofSymmetry- Z.-P. Li, W. Liu, N.-J. Guo, L.-K. Xie, J.-Y. Liu, et al.,
EnrichedQuantumCriticalSpinChains,Phys.Rev.Lett. Versatile photonic frequency synthetic dimensions using
129, 210601 (2022). asingleprogrammableon-chipdevice,Nat.Commun.16,
[35] X.-J. Yu, L. Xu, and H.-Q. Lin, Topological Physics in 7780 (2025).
Quantum Critical Systems, Phys. Rep. 1160, 1 (2026). [55] X.-D.Zeng,Z.-A.Wang,J.-M.Ren,Y.-T.Wang,C.Ao,
[36] C. M. Duque, H.-Y. Hu, Y.-Z. You, V. Khemani, W.Liu,N.-J.Guo,L.-K.Xie,J.-Y.Liu,Y.-H.Ma,etal.,
R.Verresen,andR.Vasseur,Topologicalandsymmetry- A hybrid-frequency programmable synthetic-dimension
enriched random quantum critical points, Phys. Rev. B simulatorwithrichcouplingonasinglechip,Light: Sci.
103, L100207 (2021). & Appl. 15, 213 (2026).
[37] R. Verresen, Topology and edge states survive [56] G. Li, L. Wang, R. Ye, Y. Zheng, D.-W. Wang, X.-J.
quantum criticality between topological insulators, Liu, A. Dutt, L. Yuan, and X. Chen, Direct extraction
arXiv:2003.05453 (2020). of topological Zak phase with the synthetic dimension,
[38] X.-J. Yu, R.-Z. Huang, H.-H. Song, L. Xu, C. Ding, and Light: Sci. & Appl. 12, 81 (2023).
L. Zhang, Conformal boundary conditions of symmetry- [57] F. Pellerin, R. Houvenaghel, W. A. Coish, I. Carusotto,
enriched quantum critical spin chains, Phys. Rev. Lett. andP.St-Jean,Wave-functiontomographyoftopological
129, 210601 (2022). dimerchainswithlong-rangecouplings,Phys.Rev.Lett.
[39] Y.Hidaka,S.C.Furuya,A.Ueda,andY.Tada,Gapless 132, 183802 (2024).
symmetry-protected topological phase of quantum anti- [58] H. Li and F. D. M. Haldane, Entanglement spectrum as
ferromagnets on anisotropic triangular strip, Phys. Rev. a generalization of entanglement entropy: Identification
B 106, 144436 (2022). of topological order in non-Abelian fractional quantum
[40] X.-J. Yu, S. Yang, H.-Q. Lin, and S.-K. Jian, Universal Hall effect states, Phys. Rev. Lett. 101, 010504 (2008).
entanglement spectrum in one-dimensional gapless sym- [59] T. H. Hsieh and L. Fu, Bulk entanglement spectrum re-

7
|     |     |     |     |     |     |     |     |     |     | End | Matter |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
vealsquantumcriticalitywithinatopologicalstate,Phys.
| Rev.              | Lett. | 113, 106801 | (2014).  |     |       |         |          |     |     |     |     |     |     |     |     |
| ----------------- | ----- | ----------- | -------- | --- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| [60] A. Chandran, |       | V.          | Khemani, | and | S. L. | Sondhi, | How uni- |     |     |     |     |     |     |     |     |
versal is the entanglement spectrum?, Phys. Rev. Lett. Differences between topological photonics and critical
113, 060501 (2014). topological photonics.—Conventionaltopologicalphoton-
[61] A. Chandran, M. Hermanns, N. Regnault, and B. A. icsisrootedinthebulk-boundarycorrespondence: anon-
| Bernevig,    |       | Bulk-edge                                 | correspondence |        |         | in entanglement |     |                     |          |               |     |                  |         |           |      |
| ------------ | ----- | ----------------------------------------- | -------------- | ------ | ------- | --------------- | --- | ------------------- | -------- | ------------- | --- | ---------------- | ------- | --------- | ---- |
|              |       |                                           |                |        |         |                 |     | trivial topological |          | invariant     |     | defined          | for the | gapped    | bulk |
| spectra,     | Phys. | Rev.                                      | B 84,          | 205136 | (2011). |                 |     |                     |          |               |     |                  |         |           |      |
|              |       |                                           |                |        |         |                 |     | bands               | predicts | the existence |     | of topologically |         | protected |      |
| [62] Y.Guoet |       | al.,GeneralizedLi-Haldanecorrespondencein |                |        |         |                 |     |                     |          |               |     |                  |         |           |      |
critical free-fermion systems, Phys. Rev. Res. 8, 023203 boundary modes at an interface with a topologically dis-
|     |     |     |     |     |     |     |     | tinct medium. |     | Critical | topological |     | photonics | differs | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ----------- | --- | --------- | ------- | --- |
(2026).
|     |     |     |     |     |     |     |     | a fundamental |     | way. | At a | critical | point, | the bulk | gap |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | ---- | -------- | ------ | -------- | --- |
[63] B.Peng,Ş.K.Özdemir,F.Lei,F.Monifi,M.Gianfreda,
G.L.Long,S.Fan,F.Nori,C.M.Bender,andL.Yang, closes,sotheusualtopologicalinvariantisnolongerwell
Parity–time-symmetric whispering-gallery microcavities, defined. ThiscanbeseendirectlyfromG(k )inEq.(2),
f
| Nat.     | Phys.        | 10, 394    | (2014).     |       |         |         |            |             |        |             |        |            |        | eikf | e2ikf.   |
| -------- | ------------ | ---------- | ----------- | ----- | ------- | ------- | ---------- | ----------- | ------ | ----------- | ------ | ---------- | ------ | ---- | -------- |
|          |              |            |             |       |         |         |            | where G(k   | f )≡h  | x (k f      | )+ih y | (k f )=J   | 0 +J   | 1 +J | 2        |
| [64] B.  | Peng,        | Ş. K.      | Özdemir,    | S.    | Rotter, | H.      | Yilmaz,    |             |        |             |        |            |        |      |          |
|          |              |            |             |       |         |         |            | In the      | gapped | regions,    | the    | trajectory | of     | G(k  | ) avoids |
| M.       | Liertzer,    | F. Monifi, |             | C. M. | Bender, | F.      | Nori, and  |             |        |             |        |            |        | f    |          |
|          |              |            |             |       |         |         |            | the origin, | and    | the winding |        | number     | counts | how  | many     |
| L. Yang, | Loss-induced |            | suppression |       | and     | revival | of lasing, |             |        |             |        |            |        |      |          |
Science 346, 328 (2014). times this loop encircles the origin. At criticality, how-
[65] A. Dutt, M. Minkov, I. A. Williamson, and S. Fan, ever, the loop touches the origin, i.e., G(k∗) = 0, which
f
| Higher-order |     | topological |     | insulators | in  | synthetic | dimen- |             |     |           |      |         |     |             |     |
| ------------ | --- | ----------- | --- | ---------- | --- | --------- | ------ | ----------- | --- | --------- | ---- | ------- | --- | ----------- | --- |
|              |     |             |     |            |     |           |        | corresponds |     | to a bulk | band | closing | and | invalidates | the |
sions, Light: Sci. & Appl. 9, 131 (2020). conventional winding-number definition, see Fig. 5. The
[66] S. K. Sridhar, R. Srikanth, A. R. Miller, F. J. McComb, schematicwindingloops,therefore,illustratewhyacriti-
| and | A. Dutt, | Measuring |     | Z invariants |     | in dimer | models |                                                   |     |     |     |     |     |     |     |
| --- | -------- | --------- | --- | ------------ | --- | -------- | ------ | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |          |           |     | 2            |     |          |        | calpointcannotbecharacterizedsimplybyassigningthe |     |     |     |     |     |     |     |
andcross-coupledladderswithaprogrammablephotonic
|                                              |     |                  |     |              |     |        |         | winding | number | of either | adjacent |     | gapped | phase. |     |
| -------------------------------------------- | --- | ---------------- | --- | ------------ | --- | ------ | ------- | ------- | ------ | --------- | -------- | --- | ------ | ------ | --- |
| molecule,                                    |     | arXiv:2505.04151 |     | (2025).      |     |        |         |         |        |           |          |     |        |        |     |
| [67] S. Ryu,                                 | A.  | P. Schnyder,     |     | A. Furusaki, |     | and A. | W. Lud- |         |        |           |          |     |        |        |     |
| wig,Topologicalinsulatorsandsuperconductors: |     |                  |     |              |     |        | tenfold |         |        |           |          |     |        |        |     |
wayanddimensionalhierarchy,NewJ.Phys.12,065010
(2010).
[68] X.Huang,Y.Lai,Z.H.Hang,H.Zheng,andC.T.Chan,
Diracconesinducedbyaccidentaldegeneracyinphotonic
| crystals | and         | zero-refractive-index |     |     | materials, |     | Nat. Mater. |     |     |     |     |     |     |     |     |
| -------- | ----------- | --------------------- | --- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10,      | 582 (2011). |                       |     |     |            |     |             |     |     |     |     |     |     |     |     |
[69] K.Sakoda,Proofoftheuniversalityofmodesymmetries
increatingphotonicDiraccones,Opt.Express20,25181
(2012).
| [70] P. Calabrese |     | and | J. Cardy, | Entanglement |     | entropy | and |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
quantum field theory, J. Stat. Mech. 0406, P06002 FIG. 5. Complex-plane diagnosis of the winding-number
| (2004). |     |     |     |     |     |     |     | breakdown. |     | (a) At | the gapped | point | (J  | /J ,J | /J ) = |
| ------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ---------- | ----- | --- | ----- | ------ |
|         |     |     |     |     |     |     |     |            |     |        |            |       |     | 1 0   | 2 0    |
[71] SeeSupplementalMaterialforthedetailsofkineticinver- (2.3,0.9), G(k ) avoids the origin and the winding number
f
sion mechanism, entanglement spectrum diagnostic, 2D is well defined. (b) At the critical point (J /J ,J /J ) =
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1 0 | 2 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
extensionofcriticaltopologicalphotonicsinsyntheticdi- (2.5,1.5),G(k∗)=0,soargG(k )issingularandtheconven-
|                |        |                |        |             |             |         |           |                |     | f      |                 | f   |     |     |     |
| -------------- | ------ | -------------- | ------ | ----------- | ----------- | ------- | --------- | -------------- | --- | ------ | --------------- | --- | --- | --- | --- |
|                |        |                |        |             |             |         |           | tional winding |     | number | is ill defined. |     |     |     |     |
| mensions,      |        | and robustness |        | of critical | topological |         | states in |                |     |        |                 |     |     |     |     |
| both           | 1D and | 2D.            |        |             |             |         |           |                |     |        |                 |     |     |     |     |
| [72] R. Jackiw |        | and C.         | Rebbi, | Solitons    | with        | fermion | number    |                |     |        |                 |     |     |     |     |
½, Phys. Rev. D 13, 3398 (1976). However,thefailureoftheconventionalinvariantdoes
[73] X.-L. Qi, Y.-S. Wu, and S.-C. Zhang, Topological quan- not imply the absence of bulk-edge correspondence in
tizationofthespinHalleffectintwo-dimensionalparam-
|     |     |     |     |     |     |     |     | critical | topological | photonics. |     | Along | the | critical | line |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---------- | --- | ----- | --- | -------- | ---- |
agneticsemiconductors,Phys.Rev.B74,085308(2006).
|                 |     |                  |     |         |          |     |            | separating | the            | W = | 1 and    | W = 2 | phases, | chiral | sym-   |
| --------------- | --- | ---------------- | --- | ------- | -------- | --- | ---------- | ---------- | -------------- | --- | -------- | ----- | ------- | ------ | ------ |
| [74] S. Sarkar, |     | C. Mukhopadhyay, |     | A.      | Alase,   | and | A. Bayat,  |            |                |     |          |       |         |        |        |
|                 |     |                  |     |         |          |     |            | metry pins | zero-frequency |     | boundary |       | modes   | even   | though |
| Free-fermionic  |     | topological      |     | quantum | sensors, |     | Phys. Rev. |            |                |     |          |       |         |        |        |
Lett. 129, 090503 (2022). the bulk spectrum is gapless. Thus, the relevant corre-
[75] L. Xiao, S. Sarkar, K. Wang, A. Bayat, and P. Xue, spondenceisnolongertheusual“gappedbulkinvariant–
Observation of criticality-enhanced quantum sensing in topologically protected edge state” relation. Instead, the
nonunitaryquantumwalks,Phys.Rev.Lett.136,060802 relevant information is transferred to the bulk entan-
(2026). glement structure, where the degeneracy of the bound-
| [76] A. | Ma, T. | Dai, G. | Li, L.   | Yuan,          | J. Capmany, |     | Z. Chen, |          |       |               |     |         |     |               |     |
| ------- | ------ | ------- | -------- | -------------- | ----------- | --- | -------- | -------- | ----- | ------------- | --- | ------- | --- | ------------- | --- |
|         |        |         |          |                |             |     |          | ary zero | modes | is faithfully |     | encoded | in  | the entangle- |     |
| Q.      | Gong,  | and     | J. Wang, | Reconfigurable |             |     | and pro- |          |       |               |     |         |     |               |     |
mentspectrumviatherecentlyproposedgeneralizedLi–
| grammable |     | integrated | topological |     | photonics, |     | Nat. Rev. |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | ----------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Phys. 8, 1 (2026). Haldane correspondence [59, 62]. In this framework, the
characteristicmidgapstructureoftheentanglementspec-
|     |     |     |     |     |     |     |     | trum provides     |     | a robust | diagnostic |              | of critical | topology. |          |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ---------- | ------------ | ----------- | --------- | -------- |
|     |     |     |     |     |     |     |     | For a half-filled |     | periodic | chain,     | we construct |             | the       | correla- |

8
tion matrix from the occupied single-particle states, in the bulk wave functions, without relying on a phys-
|     |     | ical | edge termination. | In this | sense, the entanglement |     |
| --- | --- | ---- | ----------------- | ------- | ----------------------- | --- |
(cid:88)
C = ψ (i)ψ∗ (j). (4) spectrumrestoresabulk-boundarycorrespondenceatcrit-
ij m m
|     |     | icality | and distinguishes | a topologically | nontrivial | critical |
| --- | --- | ------- | ----------------- | --------------- | ---------- | -------- |
m∈occ
|     |     | point | from an ordinary | band closing. |     |     |
| --- | --- | ----- | ---------------- | ------------- | --- | --- |
RestrictingC toaspatialsubsystemAgivesthereduced Experimentalimplementation.—Theextended1DSSH
correlation matrix CA. Its eigenvalues define the single- synthetic lattice can be implemented using two coupled
| particle entanglement spectrum, |     |            |               |                 |         |            |
| ------------------------------- | --- | ---------- | ------------- | --------------- | ------- | ---------- |
|                                 |     | fiber-ring | resonators,   | each containing | an EOM. | For a      |
|                                 |     | ring       | length L = 10 | m and group     | index n | ≃ 1.5, the |
g
CA|φ ⟩=ξ |φ ⟩, 0≤ξ ≤1. (5) free spectral range is Ω/(2π) ≃ 20 MHz. An inter-ring
α α α α
|     |     | coupling | g/(2π) = | 4 MHz yields | the resonant | modula- |
| --- | --- | -------- | -------- | ------------ | ------------ | ------- |
Equivalently, the corresponding entanglement energies tion tones Ω /(2π) = (8,12,32) MHz, correspond-
0,1,2
are ε = ln1−ξα, so that ξ = 1/2 corresponds to zero ing to J ,J ,J . The critical point shown in Fig. 2
| α   | α   |     | 0 1 2 |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
ξα
entanglement energy. The key point is that the entan- of the main text is obtained with (J ,J ,J )/(2π) =
|     |     |     |     |     | 0 1 | 2   |
| --- | --- | --- | --- | --- | --- | --- |
glement cut creates virtual boundaries in an otherwise (0.20,0.50,0.30) MHz, requiring EOM modulation in-
periodic system. Therefore, midgap levels pinned near dices β = (0.02,0.05,0.03), within standard lithium-
ξ = 1/2 diagnose boundary degrees of freedom encoded niobate EOM capabilities.

9
Supplemental Material for “Critical Topological Photonics in Synthetic Dimensions”
CONTENTS
I. Physical origin of critical topological photonics: kinetic inversion 9
| II. Entanglement-spectrum |           |              | diagnosis | of critical  | topology |     | 10  |
| ------------------------- | --------- | ------------ | --------- | ------------ | -------- | --- | --- |
| A.                        | Numerical | construction | of the    | entanglement | spectrum |     | 10  |
B. Quantum-classical correspondence of the entanglement spectrum 11
C. Experimental reconstruction of the entanglement spectrum 11
| III. Two-dimensional |                         | synthetic-frequency |       | extension |     |     | 12  |
| -------------------- | ----------------------- | ------------------- | ----- | --------- | --- | --- | --- |
| A.                   | Feasible implementation |                     | route |           |     |     | 12  |
B. Phase diagram of the two-dimensional extended QWZ model 13
IV. Robustness of critical topological photonic states in 1D and 2D synthetic lattices 14
A. Robustness against symmetry-preserving perturbations in 1D synthetic lattices 14
B. Robustness against structure-preserving perturbations in 2D synthetic lattices 15
Appendix I: Physical origin of critical topological photonics: kinetic inversion
In this section, we provide a simple physical interpretation of the critical topological photonics discussed in the
main text. The boundary modes identified at the critical topological points in the main text do not originate from
the conventional mass-inversion (Jackiw–Rebbi) mechanism of gapped topological insulators [72]. Instead, they arise
| from a kinetic | inversion | near | the critical | point [37]. |     |     |     |
| -------------- | --------- | ---- | ------------ | ----------- | --- | --- | --- |
We first recall the mass-inversion mechanism in a gapped topological insulator. Near a transition between a trivial
phase and a topological phase, the low-energy theory is commonly described by a Dirac Hamiltonian with a spatially
varying mass m(x). For a spatial interface where the mass changes sign, m(x→−∞)m(x→+∞) < 0, the resulting
domain wall binds a zero-energy mode. The localization length of this mode is set by the inverse bulk gap, namely
by the inverse magnitude of the asymptotic mass. This is the standard mass-inversion, or band-inversion, mechanism
underlyingthebulk–boundarycorrespondenceingappedtopologicalphases. NotethatinRef.[13]themassisreplaced
| by the helicity | from | Maxwell | equations. |     |     |     |     |
| --------------- | ---- | ------- | ---------- | --- | --- | --- | --- |
The critical topological state considered here is fundamentally different. At a critical point the bulk gap vanishes,
so the mass-inversion picture is no longer applicable. To expose the mechanism that replaces it, we expand the off-
diagonal Bloch element G(k )=J +J eikf +J e2ikf in Eq. (2) of the main text around the gap-closing momentum
|       |           |      | f 0           | 1                 | 2      |       |      |
| ----- | --------- | ---- | ------------- | ----------------- | ------ | ----- | ---- |
| k =π. | Writing k | =π+q | and expanding | to leading        | orders | gives |      |
| f     |           | f    |               |                   |        |       |      |
|       |           |      |               | G(π+q)≃m+iκq−Aq2, |        |       | (S1) |
with m = J −J +J , κ = −J +2J , and A = 2J −J /2. Here m controls the gap opening and κ is the linear
|     | 0 1 | 2   | 1   | 2   | 2   | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
kinetic coefficient.
The condition m = 0, equivalently J = J +J , defines the diagonal gap-closing trajectory. For J < J it is the
|     |     |     |     | 1 0 | 2   | 2 0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
W = 0 ↔ 1 branch, whereas for J > J it is the W = 1 ↔ 2 branch; the two meet at J = J . Along the line
|     |     |     | 2   | 0   |     | 2 0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
W =1↔2 the kinetic coefficient κ=−J 1 +2J 2 remains generically nonzero. It is this nonvanishing κ, rather than
a mass gap, that governs the boundary physics of the critical topological state.
The multicritical point J =2J , J =J corresponds to the special case in which κ also vanishes; here the leading
|     |     |     | 1 0 | 2 0 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
dispersionreducestoaquadraticbandtouching,anddistinctcriticalbranchesarereorganized. Foraspatialinterface
the corresponding low-energy operator reads, up to an overall sign convention,
=−A∂2−κ(x)∂
|     |     |     |     | D   |     | +m(x). | (S2) |
| --- | --- | --- | --- | --- | --- | ------ | ---- |
|     |     |     |     |     | x   | x      |      |
In a gapped topological interface, the zero mode is produced by a sign change of m(x), as shown schematically in
Fig. S1(a). Along a critical topological interface, by contrast, the system sits on the critical line m(x)=0 while the

10
| (a) |     |        |                |        |     |          |     |     | (b) |     |                   |     |
| --- | --- | ------ | -------------- | ------ | --- | -------- | --- | --- | --- | --- | ----------------- | --- |
|     |     |        | mass inversion |        |     |          |     |     |     |     | kinetic inversion |     |
|     |     |        |                | Gapped |     | topology |     |     |     |     | Critical topology |     |
|     |     | Vacuum |                |        |     |          |     |     |     |     | Vacuum            |     |
κ(x)
|     | |ψ(x)|2 |     |     |     |     | m(x) |     |     |     | |ψ(x)|2 |     |     |
| --- | ------- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- | --- | --- |
|     | 0       |     |     |     |     |      |     |     | 0   |         |     |     |
m(x)
|     |     |     |     |     |     |     |     | x   |     |     |     | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
FIG. S1. Physical origin of the critical topological photonic states from the kinetic inversion. (a) In a conventional gapped
topological interface, a localized zero mode is generated by a sign change of the mass term m(x). (b) In a critical topological
interface,theboundarymodeisinsteadgeneratedbyasignchangeofthekineticcoefficientκ(x)whilethemassremainstuned
to the critical line m≈0. This provides a gapless analogue of the Jackiw–Rebbi domain-wall mechanism [37].
kinetic coefficient κ(x) interpolates between opposite asymptotic signs, see Fig. S1(b). The zero-mode equation then
reduces to
|     |     |     |     |     |     | (cid:2) −A∂2−κ(x)∂ |     |     | (cid:3)   |     |     |      |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --------- | --- | --- | ---- |
|     |     |     |     |     |     |                    |     |     | x ψ(x)=0, |     |     | (S3) |
x
which, for a constant κ(x)≡κ with x→∞, supports an exponentially localized solution
|     |     |     |     |     |     |     |          |     | (cid:104) κ | (cid:105) |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | --------- | --- | ---- |
|     |     |     |     |     |     |     | ψ(x)∼exp |     | −           | x ,       |     | (S4) |
A
provided the sign of κ/A is such that the wave function decays away from the interface on both sides. Thus the
boundary localization is controlled by the kinetic coefficient κ(x) rather than by a bulk mass gap.
This mechanism is the kinetic analogue of the Jackiw–Rebbi mass-domain-wall mechanism. In the conventional
gapped case, the interface is topological because the mass term changes sign; in the critical case, it is topological
because the kinetic coefficient changes sign when passing through the critical point. The resulting boundary mode is
therefore not a remnant of a finite-gap topological band structure, but an intrinsic boundary signature of the critical
line.
For the extended SSH chain, this picture explains why different critical lines in the phase diagram Fig. 1(c) in the
main text are topologically inequivalent. The W =0↔1 and W =0↔2 critical lines border the trivial sector and
do not retain protected boundary modes at criticality. The W = 1 ↔ 2 critical line, by contrast, is separated from
these trivial branches by the critical point, across which κ changes sign. This kinetic inversion provides the physical
| origin | of  | the critical | topological | zero      | modes                 | reported     |     | in the | main      | text.        |                      |     |
| ------ | --- | ------------ | ----------- | --------- | --------------------- | ------------ | --- | ------ | --------- | ------------ | -------------------- | --- |
|        |     |              | Appendix    | II:       | Entanglement-spectrum |              |     |        | diagnosis |              | of critical topology |     |
|        |     |              | A.          | Numerical |                       | construction |     | of     | the       | entanglement | spectrum             |     |
Wenowcomputethesingle-particleentanglementspectrumfromthefinite-sizeextendedSSHHamiltonian[Eq.(2)
| of  | the main | text], |     |     |           |       |     |       |     |         |        |      |
| --- | -------- | ------ | --- | --- | --------- | ----- | --- | ----- | --- | ------- | ------ | ---- |
|     |          |        |     |     | (cid:88)Ä | c˜†d˜ |     | d˜†c˜ |     | d˜†c˜   | ä      |      |
|     |          |        |     | H   | =         | J     | +J  |       | +J  |         | +h.c., | (S5) |
|     |          |        |     |     |           | 0     | n n | 1 n   | n−1 | 2 n n−2 |        |      |
n
|     |     |     |     |     |     |     | ,d˜,...,c˜ |     | ,d˜ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
on a chain of N unit cells with basis Ψ = (c˜ )T. Anti-periodic boundary conditions (APBC) are
|     |     | f   |     |     |     |     | 1 1 | Nf  | Nf  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
imposed so that the discrete momentum grid avoids the isolated gap-closing point at criticality. The Hamiltonian is
diagonalizedtoyield2N f eigenstates|ψ α ⟩witheigenvaluesorderedincreasingly. Athalffillingtheoccupiedsubspace
consists of the N lowest-frequency states, and the equal-time correlation matrix is the projector
f
Nf
(cid:88)
|     |     |     |     |     |     |     | C   | =   | ψ ψ∗ | ,   |     | (S6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- |
|     |     |     |     |     |     |     | ij  |     | α,i  | α,j |     |      |
α=1

11
where i,j run over both unit-cell and sublattice indices. The subsystem A is chosen as the first N = N /2 unit
|     |     |     |     |     |     |     |     |     |     | (cid:12) | A   | f   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
cells (including both sublattices). The restricted correlation matrix CA =C(cid:12) has dimension 2N ×2N , and its
|             |        |                     |     |     |              |     |           |     |     | i,j∈A | A   | A    |
| ----------- | ------ | ------------------- | --- | --- | ------------ | --- | --------- | --- | --- | ----- | --- | ---- |
| eigenvalues | define | the single-particle |     |     | entanglement |     | spectrum, |     |     |       |     |      |
|             |        |                     |     |     | CA|φ         | ⟩=ξ | |φ        | ⟩,  | 0≤ξ | ≤1.   |     | (S7) |
|             |        |                     |     |     |              | α   | α         | α   | α   |       |     |      |
The corresponding entanglement energies ε = ln[(1−ξ )/ξ ] vanish at ξ = 1/2, so midgap entanglement levels
|     |     |     |     |     |     | α   |     | α α |     | α   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
signal zero modes of the entanglement Hamiltonian. For Fig. 2(d) of the main text we use the critical parameters
J /J = 2.5, J /J = 1.5 with N = 80 unit cells. The two eigenvalues pinned at ξ = 1/2 are the virtual-cut
| 1 0 | 2   | 0   |     | f   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
counterparts of the two physical zero modes found under open boundary conditions, confirming that these midgap
| entanglement | modes | are | encoded           | in the | bulk | critical       | wave | functions. |                     |     |          |     |
| ------------ | ----- | --- | ----------------- | ------ | ---- | -------------- | ---- | ---------- | ------------------- | --- | -------- | --- |
|              |       | B.  | Quantum-classical |        |      | correspondence |      |            | of the entanglement |     | spectrum |     |
TheentanglementspectruminEqs.(S6)–(S7)isusedhereasasingle-particlewave-functiondiagnostic. Itshouldnot
be interpreted as a direct measurement of photon-photon many-body entanglement. For a quadratic fermionic band
problem, the many-body ground-state entanglement spectrum is fully determined by the occupied-band projector,
or equivalently by the single-particle correlation matrix C = P occ . Therefore, the required input is the set of band
| eigenvectors, | not | an interacting |     | many-body |     | state. |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
A linear photonic lattice governed by the same effective Hamiltonian has the same single-particle eigenmodes.
Hence, after reconstructing the photonic band eigenvectors, one can construct the same projector P , restrict it
occ
to a virtual subsystem A, and obtain {ξ } by the procedure defined in Eqs. (S6)–(S7). The resulting entanglement
α
spectrum is thus the spectrum of the auxiliary free-fermion projector associated with the photonic band structure.
Accordingly,themidgapconditionξ =1/2diagnosesavirtual-boundarymodeencodedinthephotonicbandwave
α
functions. It does not imply nonclassical optical entanglement; it indicates that the measured linear modes realize
the same topological projector as the corresponding free-fermion band problem.
|     |     | C.  | Experimental |     |     | reconstruction |     | of  | the entanglement |     | spectrum |     |
| --- | --- | --- | ------------ | --- | --- | -------------- | --- | --- | ---------------- | --- | -------- | --- |
The entanglement spectrum is not measured as a direct optical observable. Experimentally, the required object is
the complex single-particle band projector P (k ), from which the restricted correlation matrix and its spectrum are
|     |     |     |     |     |     | − f |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
obtainedbypost-processing. Theessentialexperimentalrequirementisthereforephase-sensitivereconstructionofthe
| lower-band | projector, | rather | than | an  | intensity-only |     | measurement. |     |     |     |     |     |
| ---------- | ---------- | ------ | ---- | --- | -------------- | --- | ------------ | --- | --- | --- | --- | --- |
Inthesynthetic-frequencyplatform,themomentumk conjugatetothefrequencylatticeismappedtothedetection
f
timewithinonemodulationperiodk =Ωt (mod2π). Thustime-resolvedcoherenttransmissionspectroscopygives
f
accesstothemomentum-resolvedresponseofthesyntheticlattice. Forthetwo-sublatticemodel,therelevantmeasured
quantity is the complex transmission matrix S (ω,k ),µ,ν = c˜,d˜, where ν labels the input sublattice channel, µ
|     |     |     |     |     |     | µν  | f   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
labelsthe outputsublatticechannel, and ω isthe probe detuning. Themeasurement mustretain both amplitudeand
phase. In the weak-probe regime, the complex transmission is governed by the single-particle Green function,
√
|     |     |     |     | S   | (ω,k )=Sbg |     | +i γ | γ [ω+iΓ/2−H(k |     |     | )]−1, | (S8) |
| --- | --- | --- | --- | --- | ---------- | --- | ---- | ------------- | --- | --- | ----- | ---- |
|     |     |     |     | µν  | f          | µν  |      | µ ν           |     | f   | µν    |      |
Sbg
where is a smooth background, γ µ is the external coupling rate, and Γ denotes the linewidth. Fitting the two
µν
| resonance | poles at | each k | gives |     |     |     |     |     |     |     |     |     |
| --------- | -------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f
(s )(k
|     |     |     |     |     |      |       |     | (cid:88) | R µ ν   | f ) |     |      |
| --- | --- | --- | --- | --- | ---- | ----- | --- | -------- | ------- | --- | --- | ---- |
|     |     |     |     | S   | (ω,k | )≃Sbg | +   |          |         |     | .   | (S9) |
|     |     |     |     |     | µν   | f     | µν  | ω−E      | (k )+iΓ | /2  |     |      |
|     |     |     |     |     |      |       |     |          | s f     | s   |     |      |
s=±
For a Hermitian two-band Hamiltonian, the residue matrix of the lower band is proportional to the band projector,
|     |     |     |     |     |     | R(−)(k | )∝u | (k    | )u∗ (k | ).  |     | (S10) |
| --- | --- | --- | --- | --- | --- | ------ | --- | ----- | ------ | --- | --- | ----- |
|     |     |     |     |     |     | µν     | f   | −,µ f | −,ν f  |     |     |       |
After calibration of the external coupling rates, the normalized projector is therefore reconstructed as
|     |     |     |     |     |     |     |     | R(−)(k | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
f
|     |     |     |     |     |     | P − | (k f )= |          | .   |     |     | (S11) |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     |         | TrR(−)(k | )   |     |     |       |
f

12
FIG.S2. (a)Real-spacecouplingschematicforthetwo-legimplementationofthetwo-dimensionalextendedQWZmodel. Each
cell contains two optical modes, A and B , forming the pseudospin Ψ = (A ,B )T. The four inter-cell links between
|     |     |     | i   | i   |     |     | i,n i,n | i,n |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
neighboring cells realize the effective real-space hopping matrix T . (b) Phase diagram of the two-dimensional extended QWZ
x
model. ThecolordenotestheChernnumberCofthelowerband. SolidblackcurvesmarktheChern-sectorboundariesobtained
from the analytical gap-closing conditions. The solid red curve highlights the critical topological phase boundary M =λ−2,
which separates two nontrivial Chern sectors (C = 2 and C = 1). The dotted horizontal line indicates the cut λ = 1 used
in the main text. The two marked points, (M,λ) = (3,1) and (−1,1), correspond respectively to the topological trivial and
| nontrivial | critical points | studied | in Fig. | 4 of | the main | text. |     |     |     |     |
| ---------- | --------------- | ------- | ------- | ---- | -------- | ----- | --- | --- | --- | --- |
Theoverallgaugeof|u (k )⟩cancelsinP (k ). Thereal-spacecorrelationmatrixisthenobtainedfromthemeasured
|           |               | − f     |            |     | − f |     |     |     |     |     |
| --------- | ------------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| projector | by a discrete | Fourier | transform, |     |     |     |     |     |     |     |
N (cid:88)k−1
1
|     |     |     |     | C     | =   | eikl(n−m)[P | (k )] | .   |     | (S12) |
| --- | --- | --- | --- | ----- | --- | ----------- | ----- | --- | --- | ----- |
|     |     |     |     | nµ,mν |     |             | − l   | µν  |     |       |
N k
l=0
A virtual subsystem A is chosen in post-processing, and the restricted matrix CA is diagonalized as in Eq. (S7).
Midgap levels at ξ =1/2 then provide the experimental signature of the critical topological projector.
| In practice, | the optical | protocol |     | consists | of the | following steps: |     |     |     |     |
| ------------ | ----------- | -------- | --- | -------- | ------ | ---------------- | --- | --- | --- | --- |
1. Set the modulation amplitudes and phases to realize the target effective hopping parameters J ,J ,J .
0 1 2
d˜channels
2. Inject a weak coherent probe into the c˜and separately, and record the phase-sensitive time-resolved
| output | fields from | both | channels. |     |     |     |     |     |     |     |
| ------ | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
3. Convert the detection time to synthetic momentum using k =Ωt, and obtain the complex matrix S (ω,k ).
|     |     |     |     |     |     |     | f   |     | µν  | f   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4. For each k , fit the two resonance poles of S (ω,k ) and extract the lower-band residue R(−)(k ).
|     | f   |     |     |     |     | µν f |     |     | f   |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
5. Calibrate the external coupling rates, construct P (k ) from Eq. (S11), and Fourier transform it to obtain C.
− f
diagonalizeCA,
6. RestrictC tothevirtualsubsystemA, andidentifytheentanglementmidgaplevelsatξ =1/2.
|     |     | Appendix |     | III: | Two-dimensional | synthetic-frequency |       | extension |     |     |
| --- | --- | -------- | --- | ---- | --------------- | ------------------- | ----- | --------- | --- | --- |
|     |     |          |     | A.   | Feasible        | implementation      | route |           |     |     |
We propose a feasible implementation route for the two-dimensional extended QWZ model in a programmable
synthetic-frequency platform. The purpose of this discussion is not to provide a fully optimized device layout, but
to show that the required coupling channels can be assembled from experimentally demonstrated building blocks
of thin-film lithium-niobate (TFLN) frequency synthetic dimensions. In particular, recent TFLN devices based on
two resonators connected by an electro-optically tunable Mach–Zehnder interferometer (MZI) have demonstrated
controllable same-frequency coupling, cross-frequency coupling, and ladder Hamiltonians such as the Hall and Creutz
ladders [54, 76]. Such platforms provide a natural starting point for the present two-leg frequency-ladder realization.

13
The extended QWZ Hamiltonian [Eq. (3) of the main text] can be written in real space as
|     |     |          |      |       |          | (cid:34) |     |     |          |       |       | (cid:35) |       |
| --- | --- | -------- | ---- | ----- | -------- | -------- | --- | --- | -------- | ----- | ----- | -------- | ----- |
|     |     | (cid:88) |      |       | (cid:88) |          |     |     | (cid:88) |       |       |          |       |
|     |     | H =      | MJΨ† | σ Ψ   | +        | Ψ†       | T Ψ | +   | Ψ†       | T(p)Ψ | +h.c. | ,        | (S13) |
|     |     |          |      | i,n z | i,n      | i+1,n    | x   | i,n | i,n+p    | f     | i,n   |          |       |
|     |     | i,n      |      |       | i,n      |          |     |     | p=1,2    |       |       |          |       |
where Ψ = (A ,B )T is the optical pseudospin formed by two racetrack resonators in unit cell i at frequency
|        | i,n        | i,n i,n |               |       |     |        |         |          |     |     |     |     |     |
| ------ | ---------- | ------- | ------------- | ----- | --- | ------ | ------- | -------- | --- | --- | --- | --- | --- |
| mode n | (separated | by the  | free spectral | range | Ω   | ). The | hopping | matrices | are |     |     |     |     |
f
|        |        |        |     | J    | iJ  |     | T(p) |     | J p | iJ p |     |     |       |
| ------ | ------ | ------ | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | ----- |
|        |        |        |     | T =− | σ + | σ , |      | =−  | σ + | σ    | ,   |     | (S14) |
|        |        |        |     | x 2  | z   | 2 y | f    |     | 2 z | 2 x  |     |     |       |
| with J | =J and | J =λJ. |     |      |     |     |      |     |     |      |     |     |       |
| 1      |        | 2      |     |      |     |     |      |     |     |      |     |     |       |
T(p)
The synthetic-frequency hoppings are implemented using two types of electro-optic modulation. First, the
f
phase modulation on each resonator at frequencies pΩ generates same-ring hopping between frequency modes n and
f
n+p. Applying opposite modulation phases on the two resonators yields the diagonal part,
|     |     |     |     |      |       | J p, |     |     |       | J p, |     |     |       |
| --- | --- | --- | --- | ---- | ----- | ---- | --- | --- | ----- | ---- | --- | --- | ----- |
|     |     |     |     | A ↔A |       | : −  | B   | ↔B  |       | : +  |     |     | (S15) |
|     |     |     |     | i,n  | i,n+p | 2    |     | i,n | i,n+p | 2    |     |     |       |
realizing the −(J /2)σ component. Second, an intra-cell MZI connecting A and B is driven by RF tones that
|     |     | p z |     |     |     |     |     |     |     | i   | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
couplemodeswithbothdifferentresonatorindexanddifferentfrequencyindex. Thephase-controlledRFmodulation
of this MZI generates the couplings A ↔ B and B ↔ A with a controllable hopping phase; choosing
|     |     |     |     | i,n | i,n+p |     | i,n | i,n+p |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- |
T(p).
this phase to give the forward hopping iJ σ /2 realizes the off-diagonal component of If the two resonators
|     |     |     |     |     | p x |     |     |     |     |     | f   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
carry a differential detuning ∆ =2MJ, the cross-frequency tones are shifted from pΩ to pΩ ±∆ , depending
|                  |     |                        | AB  |             |     |     |     |     |     |     | f   | f AB |     |
| ---------------- | --- | ---------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
| on the direction |     | of the inter-resonator |     | transition. |     |     |     |     |     |     |     |      |     |
The real-space hopping T (see Fig. S2(a)) requires four inter-cell couplings per link:
x
|     |     |     |     |        |     | −J,   |     |        | +J,   |     |     |     |       |
| --- | --- | --- | --- | ------ | --- | ----- | --- | ------ | ----- | --- | --- | --- | ----- |
|     |     |     |     | A i →A | i+1 | :     |     | B i →B | i+1 : |     |     |     |       |
|     |     |     |     |        |     | 2     |     |        |       | 2   |     |     | (S16) |
|     |     |     |     | B →A   |     | : +J, |     | A →B   | : −J. |     |     |     |       |
|     |     |     |     | i      | i+1 | 2     |     | i      | i+1   | 2   |     |     |       |
Such a coupling block should be understood as an effective Hamiltonian element rather than the scattering matrix
of a single passive directional coupler; it can be synthesized by an interferometric coupling network with calibrated
relative phases and amplitudes. This is the most demanding part of the proposal, but it is compatible with present
programmable MZI-based synthetic-frequency platforms, where coupling strengths and phases are electro-optically
tunable [54].
As a representative parameter regime, one may take Ω /2π ≃ 9–10 GHz and J/2π ≃ 0.3–0.5 GHz. For a group
f
index n ≃ 2.2, this corresponds to a racetrack length L = c/(n Ω /2π) ≃ 14–15 mm, within the range of existing
| g   |     |     |     |     |     |     |     | g f |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TFLN frequency-lattice devices. A proof-of-principle device may contain N = 4–8 real-space cells and tens of
x
≲
usable frequency modes. Resolving the hopping scale requires the optical linewidth to satisfy κ loss J, while the
synthetic-frequency bandwidth should be chosen such that residual dispersion produces onsite-frequency disorder
below the relevant topological energy scale. The model can be characterized by frequency-resolved and time-resolved
transmission measurements: frequency-resolved output spectra monitor the synthetic-frequency distribution at each
spatial output port, while time-resolved spectroscopy along the synthetic-frequency quasi-momentum enables band
reconstruction, following established techniques in dynamically modulated frequency lattices. Although a full large-
scaleimplementationrequirescarefulcalibrationoftheinter-cellcouplingblocks,RFphases,andresonatordispersion,
the required ingredients are available in current programmable synthetic-frequency photonic platforms.
|     |     | B.  | Phase | diagram | of the | two-dimensional |     |     | extended | QWZ | model |     |     |
| --- | --- | --- | ----- | ------- | ------ | --------------- | --- | --- | -------- | --- | ----- | --- | --- |
To locate the topological sectors of the two-dimensional extended QWZ model, we compute the Chern number of
the lower band over the (M,λ) plane. The numerical phase diagram is obtained with the Fukui–Hatsugai–Suzuki
lattice-gauge method on a discrete Brillouin-zone mesh, while the minimum direct gap is monitored independently to
| identify | the gap-closing | lines. |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThecalculationisperformedforM ∈[−1.5,4.5]andλ∈[0.5,1.5]; Fig.S2(b)showstheparameterwindowrelevant
| to the main | text. |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

14
FIG. S3. Robustness of the 1D critical topological phase against chiral-symmetry-preserving hopping disorder at
(J /J ,J /J ) = (2.5,1.5). Results are averaged over N = 30 Gaussian disorder realizations of Eq. (S18); shaded bands
| 1 0 2 | 0   |     |     | dis |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
around the edge states in (a,b,c) denote one standard deviation. (a)–(c) Disorder-averaged left- and right-edge profiles for
σ = 0.1, 0.2, and 0.3 on an open chain with N = 80 unit cells. (d)–(f) Corresponding half-filled entanglement spectra on
f
an anti-periodic chain with unit cells. The pair of levels closest to remains pinned near the dashed line,
|     |     | N f = 100 |     |     | ξ = 1/2 |     |
| --- | --- | --------- | --- | --- | ------- | --- |
confirming the persistence of the symmetry-protected boundary modes under disorder.
The displayed phase boundaries are determined by the simultaneous conditions d x = d y = d z = 0. In the plotted
| window, | the Chern-number-changing |     | boundaries | are     |         |       |
| ------- | ------------------------- | --- | ---------- | ------- | ------- | ----- |
|         |                           |     | M =λ−2,    | M =1−λ, | M =λ+2. | (S17) |
These analytical curves agree with the jumps of the numerically computed Chern number. Along the cut λ=1, they
occuratM =−1, M =0, andM =3. Amongthese, theboundaryM =λ−2(redcurveinFig.S2(b))issingledout
as the critical topological phase boundary: it separates two nontrivial Chern sectors (C = 2 and C = 1), and serves
as the two-dimensional counterpart of the W = 1 ↔ 2 critical line of the extended SSH chain discussed above. The
two critical points used in the main text are therefore selected from distinct types of gap closing: at (3,1) the system
crosses between a trivial sector (C = 0) and a Chern sector (C = −1), whereas at (−1,1) it crosses between two
nontrivial Chern sectors (C =2 and C =1). This distinction underlies the different boundary responses discussed in
| the main | text. |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- |
Appendix IV: Robustness of critical topological photonic states in 1D and 2D synthetic lattices
Akeyquestioniswhetherthecriticaltopologicalboundarymodessurviverealisticimperfections. Inthissectionwe
test their robustness against symmetry-preserving (structure-preserving) hopping disorder in both the one- and two-
dimensionalsyntheticlattices,usingedge-modeprofilesandtheentanglementspectrumascomplementarydiagnostics.
A. Robustness against symmetry-preserving perturbations in 1D synthetic lattices
We introduce random hopping fluctuations in the extended SSH chain while keeping all hoppings inter-sublattice,
| so that chiral | symmetry | is preserved | for every | disorder realization:   |          |       |
| -------------- | -------- | ------------ | --------- | ----------------------- | -------- | ----- |
|                |          | J p (n)=J    | p [1+ση   | p (n)], η p (n)∼N(0,1), | p=0,1,2. | (S18) |

15
FIG. S4. Robustness of the two-dimensional critical topological response against structure-preserving hopping disorder at
(M,λ)=(−1,1). (a)–(c) Time-accumulated intensity of a boundary wavepacket for σ=0.1, 0.2, and 0.3, respectively. White
arrowsindicatetheclockwiseboundary-guidedpropagation. Thepersistenceedgeflowshowsthatthecriticalboundarymodes
| remain robust | under sizable | hopping-amplitude | disorder. |     |     |     |
| ------------- | ------------- | ----------------- | --------- | --- | --- | --- |
Wefocusontherepresentativecriticaltopologicalpoint(J ,J ,J )=(1,2.5,1.5)andaverageoverN =30disorder
|     |     |     |     | 0 1 | 2 dis |     |
| --- | --- | --- | --- | --- | ----- | --- |
realizations. Two diagnostics are used: the zero-energy boundary modes under open boundary conditions, and the
half-filledsingle-particle entanglementspectrum underanti-periodicboundaryconditions, wheresymmetry-protected
| boundary | modes appear | as entanglement | levels pinned | to ξ =1/2. |     |     |
| -------- | ------------ | --------------- | ------------- | ---------- | --- | --- |
The results are shown in Fig. S3. The disorder-averaged edge profiles remain localized at the two ends up to
σ = 0.3, corresponding to 30% relative hopping fluctuations. Simultaneously, the entanglement spectrum retains a
pair of midgap levels near ξ = 1/2, with only a small finite-size and disorder-induced splitting. These observations
confirm that the critical boundary modes are not artifacts of a fine-tuned clean lattice, but persist under chiral-
| symmetry-preserving | perturbations. |     |     |     |     |     |
| ------------------- | -------------- | --- | --- | --- | --- | --- |
B. Robustness against structure-preserving perturbations in 2D synthetic lattices
We test the robustness of the two-dimensional critical topological response against structure-preserving imperfec-
tions. We focus on the nontrivial critical point (M,λ) = (−1,1) and introduce random fluctuations in the hopping
amplitudes. The disorder is chosen to be uniform along the real-space direction but dependent on the synthetic-
frequency index, so that the momentum k remains a good quantum number. This models frequency-dependent
x
coupling imperfections while preserving the structure of the target Hamiltonian.
| The hopping | amplitudes | are modulated | as                   |                  |           |       |
| ----------- | ---------- | ------------- | -------------------- | ---------------- | --------- | ----- |
|             |            |               | T (n )→ (cid:2) 1+ση | (n ) (cid:3) T , | µ=x,f,2f, | (S19) |
|             |            |               | µ f                  | µ f µ            |           |       |
where η µ (n f ) are zero-mean random variables and σ controls the relative disorder strength. No onsite mass disorder
orgenericPaulidisorderisincluded,sincesuchtermswouldchangethedesignedQWZstructureratherthanrepresent
| coupling | imperfections | of the synthetic | lattice. |     |     |     |
| -------- | ------------- | ---------------- | -------- | --- | --- | --- |
FigureS4summarizestheresultsforσ =0,0.1,and0.3. Thepanels(a)-(c)showthetime-accumulatedintensityof
a wavepacket injected near the lower synthetic-frequency edge. The wavepacket remains guided along the boundary
even for σ =0.3 hopping fluctuations, with only moderate disorder-induced leakage.
---- END DOCUMENT ----
