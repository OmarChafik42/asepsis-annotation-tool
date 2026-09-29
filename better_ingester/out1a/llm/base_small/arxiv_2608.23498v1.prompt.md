Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Draft version August 25, 2026
TypesetusingLATEXtwocolumnstyleinAASTeX7.0.1
The Road to Normalcy: Environment-Driven Evolutionary Pathways for Primordial Black Holes
Saiyang Zhang（張賽暘） ,1,2 Junehyoung Jeon ,3,4 Boyuan Liu(劉博遠) ,5,6 Volker Bromm ,2,3,4 and
Priyamvada Natarajan 7,8,9
1Department of Physics, University of Texas at Austin, Austin, TX 78712, USA
2Weinberg Institute for Theoretical Physics, Texas Center for Cosmology and Astroparticle Physics,
University of Texas at Austin, Austin, TX 78712, USA
3Department of Astronomy, University of Texas at Austin, Austin, TX 78712, USA
4Cosmic Frontier Center, The University of Texas at Austin, Austin, TX 78712, USA
5Institute of Astronomy, University of Cambridge, Madingley Road, Cambridge, CB3 0HA, UK
6Universita¨t Heidelberg, Zentrum fur Astronomie, Institut fu¨r Theoretische Astrophysik, D-69120 Heidelberg, Germany
7Department of Astronomy, Yale University, New Haven, CT 06511, USA
8Department of Physics, Yale University, New Haven, CT 06520, USA
9Black Hole Initiative, Harvard University, 20 Garden Street, Cambridge, MA 02138, USA
ABSTRACT
Weinvestigatehowcosmologicalenvironmentregulatestheevolutionofprimordialblackhole(PBH)
seedsintheearlyuniverseusingasuiteofhydrodynamicalsimulations. Inadditiontotraditionalseed-
ingchannels,PBHsprovideanalternateextremelyearlypopulationofBHseedsthatcanarisenaturally
from most inflationary models. We find that PBHs follow distinct evolutionary pathways depending
on the gas supply and halo assembly history. In underdense regions, limited inflow suppresses both
accretion and star formation, producing faint, metal-poor systems, while in overdense environments,
sustained gas inflow drives rapid BH growth and the formation of compact, centrally concentrated
stellar components. These differences lead to large variations in BH-to-stellar mass ratio, metallicity,
and morphology, collectively bracketing a range of possible evolutionary pathways for PBH-seeded
systems. We show that compact, BH-dominated sources resembling recently observed Little Red Dots
naturally arise as one phase within these evolutionary pathways before evolving into more extended
galaxy–AGN systems. Our results suggest that both the initial seed properties and cosmological envi-
ronment jointly shape early BH–galaxy co-evolution, while subsequent environmental regulation can
erase the memory of the initial seeding channel.
Keywords: Dark matter (353) — Early universe (435) — Galaxy formation (595) — Population III
stars (1285) — Supermassive black holes (1663)
1. INTRODUCTION et al. 2024; J. Scholtz et al. 2024; A. J. Taylor et al.
2025; R. Maiolino et al. 2026a). A recurring theme in
Recent JWST observations have transformed our
these discoveries is not simply that individual objects
knowledge of galaxy and black-hole (BH) assembly in
appear extreme, but that they reveal a surprisingly di-
the first billion years of cosmic history (e.g., A. Adamo
verse set of early BH–galaxy configurations. At the
et al. 2025). Massive galaxies, luminous AGN candi-
redshift frontier, systems such as GN-z11, UHZ-1, and
dates, compact red sources, and chemically young sys-
other candidate galaxies hosting accreting BHs point to
tems have now been identified at redshifts where stan-
rapid BH growth already at z ≳ 10 (e.g., A´. Bogd´an
dard models of early structure formation are still being
et al. 2024; L. Napolitano et al. 2025; O. A. Chavez Or-
actively tested (e.g., S. L. Finkelstein et al. 2023; E.
tiz et al. 2025; R. P. Naidu et al. 2026; A. C. Fabian
Vanzella et al. 2023; I. Labb´e et al. 2023; M. Boylan-
et al. 2026). At somewhat lower redshifts, compact red
Kolchin 2023; P. Natarajan et al. 2024; V. Kokorev
sources such as Little Red Dots (LRDs) often combine
small sizes, red continua, strong emission lines, and ev-
Email: szhangphys@utexas.edu,boyuan.liu@uni-heidelberg.de idence for AGN activity, suggesting a phase in which
6202
guA
42
]AG.hp-ortsa[
1v89432.8062:viXra

2
the nuclear component is difficult to disentangle from accretion feedback can heat and ionize the surrounding
the compact stellar host (e.g., J. Matthee et al. 2024; gas, alter cooling, and regulate the onset of star for-
G. C. K. Leung et al. 2025; A. J. Taylor et al. 2025; mation (B. Liu et al. 2022; F. Ziparo et al. 2022; C.
D. D. Kocevski et al. 2025; I. Labbe et al. 2025; D. Casanueva-Villarreal et al. 2024; S. Zhang et al. 2024b,
Korber et al. 2026). In the most extreme cases, the 2025a). These coupled effects may also naturally pro-
inferred BH-to-stellar mass ratios substantially exceed duce phases in which the BH is overmassive relative
those observed in the local universe (e.g., R. Maiolino to the stellar component, the host remains chemically
et al. 2024a; H. U¨bler et al. 2026a; I. Juodˇzbalis et al. young, or the emission appears compact and nuclear-
2026),andsomesourcesfurthershowlowmetallicitiesor dominated akin to what is predicted generically for all
chemically young environments (e.g., R. Maiolino et al. DCBH formation pathways (P. Dayal 2024, 2026; P.
2026b; L. R. Ivey et al. 2026; R. Maiolino et al. 2026a; Dayal & R. Maiolino 2026; S. Zhang et al. 2026, e.g.,).
H. U¨bler et al. 2026b). These overlapping signatures Relatedly, W. Qin et al. (2025) proposed a “not-quite-
suggest that JWST is probing not a single class of ob- primordial black hole” (NQPBH) channel, in which
jects, but an ensemble of early BH growth modes and moderately enhanced primordial density collapse into
stages,rangingfromhigh-redshiftgalaxieshostingAGN dark-matter halos at very high redshift ((1+z) ≳ 200)
to compact, overmassive-BH systems and metal-poor where the CMB suppresses molecular hydrogen forma-
nuclear sources. Together, these observations raise a tion, limiting gas cooling and fragmentation, thereby
broader question: how do early BHs and their baryonic enabling direct collapse into massive black-hole seeds;
environments co-evolve from diverse initial conditions we defer exploring the details of this distinct picture for
and transient extreme phases toward the more familiar future work.
galaxy-AGN population observed at later times (J. Ko- Focusing here on the PBH formation during the in-
rmendy & L. C. Ho 2013; A. Smith & V. Bromm 2019; flationary epoch picture and the subsequent evolution
K. Inayoshi et al. 2020)? of those seeds, we note that the observable outcome
One possible route to early BH growth is provided of a PBH-seeded system is not determined by the seed
by massive primordial black hole (PBH) seeds (e.g., N. alone, but also by the large-scale environment in which
Cappelluti et al. 2022; H.-L. Huang et al. 2024; V. De itevolves(seee.g.,B.Carr&J.Silk2018;Z.Wangetal.
Lucaetal.2026;A.Kashlinskyetal.2026;H.-L.Huang 2026). In relatively isolated regions, limited gas inflow
et al. 2026), theorized to form from overdense regions andfeedback-drivengasremovalcansuppresssustained
intheprimordialfireballshortlyaftertheBigBang(for star formation and BH growth, leaving behind faint,
reviewing work, see e.g., B. Carr & F. Ku¨hnel 2020; metal-poor, or weakly evolved systems (e.g., P. Dayal
A. Escriv`a et al. 2024). Unlike stellar-remnant (e.g., 2024; S. Zhang et al. 2026; P. Dayal 2026). In over-
T. Alexander & P. Natarajan 2014) or direct-collapse dense regions, initial PBH clustering and mergers may
blackhole(DCBH)seedingpathways,whichareformed accelerate the assembly of a more massive BH, whereas
from the collapse of pristine gas (e.g., V. Bromm & A. continued gas supply and hierarchical assembly can in-
Loeb 2003; M. C. Begelman et al. 2006; G. Lodato & P. stead maintain both stellar growth and BH accretion,
Natarajan 2006). While there exist multiple pathways producing compact and luminous systems and acceler-
to make DCBHs, a generic feature of all those mod- ating the early formation of galaxies and AGNs (B. Liu
els is the existence of a stage during which the BH is & V. Bromm 2022; V. De Luca et al. 2023; A. Matteri
overmassive compared to the stellar component in the et al. 2025; B. Liu & V. Bromm 2025). Thus, the PBH-
hostgalaxyB.Agarwaletal.(2013);P.Natarajanetal. seeded systems may follow very different evolutionary
(2017). PBHscanformbeforetheonsetofconventional pathways: they may remain an exotic, weakly fueled
star and galaxy formation and therefore need not be object for an extended period, temporarily appear as a
tiedtothelocalthermalandchemicalconditions,orthe compact BH-dominated source, or be incorporated into
star-forming state of the gas. This makes PBHs a use- agrowinggalaxyandevolvetowardamoreconventional
ful theoretical laboratory for studying how an initially AGN-hostsystem. This“roadtonormalcy”dependson
massive compact object modifies subsequent structure whethersubsequentgalaxyassemblyerasesorpreserves
and galaxy formation. Through their gravitational po- the initial PBH-driven signature.
tential, PBHs canenhance local dark-matter clustering, Thismotivatesamoredetailedinvestigationoftheas-
deepenthecentralpotentialwell,andpromotegasaccu- trophysicalimpactofPBHsinrealisticcosmologicalen-
mulation(N.Afshordietal.2003;K.J.Macketal.2007; vironments. In previous studies, we have explored PBH
M. Ricotti 2007; M. Ricotti et al. 2008; S. Zhang et al. effects on halo assembly, first star formation, and early
2024a; B. Liu & V. Bromm 2025). At the same time, BH–galaxy co-evolution (B. Liu et al. 2022; S. Zhang

3
etal.2024a,b,2025a,b,2026). RelatedstudiesofDCBH with a 12-species non-equilibrium network (V. Bromm
and early AGN formation have emphasized that com- etal.2002;J.L.Johnson&V.Bromm2006),initialized
pactBH-dominatedsystemsmayarisethroughmultiple atz =1100usingtheabundancesofD.Galli&F.Palla
physical channels (V. Bromm & A. Loeb 2003; J. Jeon (2013). We additionally account for the fine-structure
et al. 2023; H. Hu et al. 2025; J. Jeon et al. 2025a,b; K. cooling of C II, O I, Si II, and Fe II (C. Safranek-
Inayoshi & K. Ichikawa 2024; K. Inayoshi et al. 2026). Shrader et al. 2010; J. Jaacks et al. 2018). We describe
A controlled comparison between PBHs placed in dif- the new environmental initial conditions in Section 2.1
ferent environments is therefore necessary to determine and provide the adopted BH, star-formation, and feed-
whether PBH signatures remain observable over cosmic back prescriptions in Section 2.2..
time,andunderwhatconditionstheyareerasedbysub- Throughout this work, the Planck18 cosmological
sequent galaxy assembly. parameters are adopted ( Planck Collaboration et al.
Inthiswork,weusecosmologicalsimulationstofollow 2020): Ω = 0.3111, Ω = 0.04897, h = 0.6776,
m b
PBH-seeded systems from the matter-dominated epoch σ = 0.8102, and n = 0.9665. The key simulation pa-
8 s
atz ∼3400toz ∼3inbothrelativelyisolatedandover- rameters are summarized in Table 1.
dense environments. Our fiducial PBH seed masses are
105 and 107M , motivated by scenarios in which mas- 2.1. Initial Conditions and Environmental Setup
⊙
sive PBHs may arise from early-Universe phase transi-
In previous work (S. Zhang et al. 2025a,b, 2026), we
tions(B.Carretal.2021). ThesevaluesbrackettheBH
focused on the evolution of PBHs in relatively isolated
masses inferred for the glimpse sources (Q. Fei et al.
environments within L ≤ 1cMpc/h boxes, where the
2026), and for compact high-redshift systems such as
dynamics are largely governed by the seed effect (K. J.
the Cliff (z ≃ 3.5; L. R. Ivey et al. 2026). By vary-
Mack et al. 2007). However, as highlighted in S. Zhang
ing the initial placement of the PBH within the same
et al. (2024a), the evolution of PBHs over cosmic time
cosmological framework, we isolate the role of a large-
is also expected to depend sensitively on their large-
scale environment in regulating gas inflow, BH accre-
scaleenvironment. Toinvestigatethisaspect,weenlarge
tion,starformation,metalenrichment,andgalaxymor-
the simulation volume to a comoving box of side length
phology. We track the coevolution of the PBH and its L = 2cMpc/h with N = 2563 dark matter particles
host galaxy, predict their possible observational signa- generated from the music code (O. Hahn & T. Abel
tures and low-redshift descendants, and compare these
2011),andvarytheinitialplacementofthePBHwithin
outcomes with regimes probed by recent JWST obser-
this volume.
vations and future observing campaigns. Our goal is
In our fiducial setup, following S. Zhang et al. (2026),
not to associate PBHs uniquely with a single observa- a M ≃ 107M PBH is placed at the center of the
• ⊙
tional class, such as Little Red Dots, but to map the
simulation box, corresponding to a region of approxi-
evolutionary pathways through which PBH-seeded sys- mately average density 10. The system is first evolved
temsmayremainexotic,temporarilyappearascompact
from z = 3400 to z = 1100 in a dark-matter-only con-
BH-dominated sources, or eventually evolve into more
figuration, with the PBH treated as a massive particle
conventional galaxies hosting AGN.
(thePBH DMonlyrun), establishingtheinitialdarkmat-
This paper is organized as follows. In Section 2 we
ter distribution. At z = 1100, baryons are introduced,
describe our simulation setup and analysis methodol-
and the simulation transitions to full hydrodynamics,
ogy. InSection3wepresentthestructuralandchemical
allowing us to follow gas accretion, star formation, and
properties of the simulated systems and compare them
feedback (the PBH M1e7 run).
with observations. We discuss implications and limita-
To probe overdense environments, we construct al-
tionsinSection4,andofferourconclusionsinSection5.
ternative realizations in which the PBH is embedded
in a region that later will collapse into a massive halo.
2. METHODOLOGY In a more extreme case, we increase the initial matter
contrast by setting σ = 2.0 and generate an addi-
We adopt the numerical framework developed in our 8
tional simulation box of the same size using the music
previous PBH simulations (S. Zhang et al. 2025a,b,
2026). All simulations are performed with the GIZMO code (T. H. Greif et al. 2011; J. Jeon et al. 2026a).
We first run a dark-matter-only simulation without
code (P. F. Hopkins 2015), which combines an updated
version of the GADGET-3 TreePM gravity solver (V.
Springel2005)withtheLagrangianmeshlessfinite-mass
10 This is confirmed by the corresponding DM only simulation
(MFM) hydrodynamics method using N ngb =32 neigh- without any PBH, which shows no massive halo forming near
bors. Primordial chemistry and cooling are followed theboxcenter.

4
Table1. Keyparametersandmainsimulationresults. z denotesthestartingredshiftofthesimulation,whilez corresponds
|     |     |     |     |     | ini |     |     |     | final |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
to the final saved snapshot. N denotes the equivalent uniform particle resolution for the initial box of size L = 2cMpc/h.
eff
For the full-box simulations, this corresponds to the actual particle resolution, whereas for the refined-region (’ 2sigzoom’)
simulations it represents the uniform-box resolution that would give the same particle mass as in the highest-resolution region.
ϵ denotes the fraction of the BH feedback energy thermally coupled to the surrounding gas, while ⟨f ⟩ ≡ ⟨M˙ /M˙ ⟩ gives
| r   |     |     |     |     |     |     |     |     | edd | • edd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
thetime-averagedEddingtonratiobetweenz andz . The(co-moving)softeninglengthsfor(particle)DM,gas,andstellar
ini final
particles are given by ϵ , ϵ , and ϵ , respectively. M is the mass of the halo chosen to host the PBH, at the last
|          |        | DM          | gas ⋆ |     | h,PBH |     |     |     |     |     |
| -------- | ------ | ----------- | ----- | --- | ----- | --- | --- | --- | --- | --- |
| snapshot | of the | simulation. |       |     |       |     |     |     |     |     |
Run z ini z final N eff ϵ r ⟨f edd ⟩ ϵ DM [kpc/h] ϵ gas [kpc/h] ϵ ⋆ [kpc/h] M h,PBH [M ⊙ /h]
|     | DM      | only | 3400 3.0 | 2563 | -   | -   | 0.1 | -   | -   | 5.5×109  |
| --- | ------- | ---- | -------- | ---- | --- | --- | --- | --- | --- | -------- |
|     | DM only | 2sig | 3400 3.0 | 2563 | -   | -   | 0.1 | -   | -   | 2.7×1010 |
2563
|     | PBH        | DMonly | 3400 1100 |        | -     | -      | 0.1 | -   | -    | -       |
| --- | ---------- | ------ | --------- | ------ | ----- | ------ | --- | --- | ---- | ------- |
|     | PBH DMonly | dense  | 3400 1100 | 2563   | -     | -      | 0.1 | -   | -    | -       |
|     | PBH DMonly | 2sig   | 3400 1100 | 2563   | -     | -      | 0.1 | -   | -    | -       |
|     | PBH        | M1e7   | 1100 3.8  | 2×2563 | 0.005 | 0.0038 | 0.1 | 0.1 | 0.01 | 8.5×108 |
PBH M1e7 dense 1100 4.1 2×2563 0.005 0.011 0.1 0.1 0.01 8.3×109
|     |             |               |             | 2×2563 |       |       |     |     |      | 1.3×109 |
| --- | ----------- | ------------- | ----------- | ------ | ----- | ----- | --- | --- | ---- | ------- |
|     | PBH M1e7    | 2sig          | 1100 11.5   |        | 0.005 | 0.023 | 0.1 | 0.1 | 0.01 |         |
| PBH | DMonly      | M1e7 2sigzoom | 3400 1100   | 2563   | -     | -     | 0.1 | -   | -    | -       |
| PBH | DMonly      | M1e5 2sigzoom | 3400 1100   | 2563   | -     | -     | 0.1 | -   | -    | -       |
| PBH | DMonly M1e5 | 2sigzoom      | 2 3400 1100 | 2563   | -     | -     | 0.1 | -   | -    | -       |
PBH M1e7 2sigzoom 1100 8.1 2×2563 0.005 0.029 0.1 0.1 0.01 6.0×109
|     |          |          |          | 2×2563 |       |         |     |     |      | 1.1×109 |
| --- | -------- | -------- | -------- | ------ | ----- | ------- | --- | --- | ---- | ------- |
|     | PBH M1e5 | 2sigzoom | 1100 8.7 |        | 0.005 | 0.00026 | 0.1 | 0.1 | 0.01 |         |
PBH M1e5 2sigzoom 2 1100 8.8 2×2563 0.005 0.00094 0.1 0.1 0.01 6.4×109
PBHs (DM only and DM only 2sig for σ = 0.8102 and tial conditions, the PBH system will start life as an
8
2.0) from z = 3400 to z = 3, and identify halos us- overmassive BH embedded in a star forming halo. To
Rockstar
ing the halo finder (P. S. Behroozi et al. partially mitigate the computational cost of the full
2013). We select the most massive halo at z = 3 PBH M1e7 2sig run, we also construct a refined-region
|     |     | 109 |     | 1010M |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
(M h, PBH ≃ 5.5 × and ≃ 2.7 × ⊙ /h, re- realization centered on the same overdense Lagrangian
spectively) and trace its Lagrangian region back to the patch. This setup is generated using the same zoom-in
music,
initial conditions. The center of this Lagrangian patch initial-condition machinery in but is used here
defines an overdense region at early times, expected primarily to focus the computational resolution on the
to experience enhanced mass assembly and gas inflow. PBH-hosting overdense region rather than to perform
We then place the PBH at this location and re-run a full multi-scale zoom-in study. Specifically, we use
the simulation with identical parameters, yielding the the DM only 2sig run to identify the center and spatial
PBH DMonly dense, PBH DMonly 2sig, PBH M1e7 dense, extent of the Lagrangian region associated with one of
and PBH M1e7 2sig runs. This setup enables a con- the most massive halos at z = 3. Instead of evolving
trolled comparison between PBHs evolving in typical the full L=2cMpc/h volume at uniform resolution, we
and highly overdense environments, isolating the im- generate refined initial conditions at z = 3400 for the
pact of large-scale structure on their growth and ob- dark-matter-only stage and at z = 1100 for the hydro-
servable properties. The hydrodynamic simulations are dynamical stage. The refined region has a side length
run from z = 1100 to z ∼ 4 (z ∼ 12 for the 2-sigma of L ∼ 750ckpc/h, approximately corresponding to
ref
box due to the intensive computational cost from early theextentoftheLagrangianpatch, inwhichtheresolu-
stellar formation and feedback), as limited by the box tion is identical to that of the full PBH M1e7 2sig run,
size and computational resources, corresponding to the while outside the refined region, the mass resolution is
redshift where the number density of observed LRDs reduced by a factor of 43, and there are no gas particles
has decreased (see e.g., Y. Ma et al. 2026), and also in the hydrodynamical stage. The corresponding dark-
at a redshift similar to one of the recently discovered matter-onlyrun,PBH DMonly M1e7 2sigzoom,isevolved
overly massive SMBHs, the Cliff (confirmed at z ≃3.5, from z = 3400 to z = 1100 to establish the initial
see A. de Graaff et al. 2025; L. R. Ivey et al. 2026). dark-matter configuration for the hydrodynamical run,
We note that as a consequence of our choice of ini- 2sigzoom, following the same procedure as
|     |     |     |     |     |     | PBH M1e7 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |

5
above. In addition, we test the effect of varying the ini- to the gas metallicity at formation, with Pop III and
tial PBH seed mass. Using the same Lagrangian-region Pop II stars separated by a critical metallicity thresh-
selectionandrefined-regionprocedure,weplacealighter old Z = 10−4Z (e.g., V. Bromm et al. 2001), where
|     |     |     |     |     |     |     |     |     | th  | ⊙   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PBH seed of mass 105M in the identified overdense Z = 0.0134. Each star-forming gas particle spawns
|     |     |     | ⊙   |     |     |     |     | ⊙   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
region of the DM only 2sig box. This gives rise to four 16stellarparticles, correspondingtoanindividualmass
additional simulations, PBH DMonly M1e5 2sigzoom, of ≃ 600M . For Pop III stars, each stellar particle
⊙
PBH DMonly M1e5 2sigzoom 2, PBH M1e5 2sigzoom, represents a Pop III cluster with a characteristic mass
and PBH M1e5 2sigzoom 2. Here the label “zoom” is consistent with those expected from H -cooling (e.g.,
2
retained for bookkeeping, although these runs should A. Stacy & V. Bromm 2013; S. Hirano & V. Bromm
be interpreted as refined-region realizations of the over- 2017; B. Liu et al. 2021, 2024; J. Gurian et al. 2026).
dense PBH environment. The runs with the suffix “ 2” PopIIIstellarmassesaredrawnon-the-flyfromamodi-
|     |     |     | 105M |     |     |     |     |     |     |     | ∝M−αexp(−M2 |     |     | /M2),over |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --------- | --- |
differ by initializing the ⊙ PBH at the center fiedLarsonIMF,dN/dM
cut
of the Lagrangian region of a 1.8×109M /h halo at a mass range of 1 − 150M , adopting α = 0.17 and
|     |     |     |     |     |     | ⊙   |     |     |       |     |     | ⊙   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | M2  | =20M2 |     |     |     |     |     |     |
z = 7, which is a progenitor of the main halo identi- (J. Jaacks et al. 2018). The mass distri-
|     |     |     |     |     |     |     |     | cut |     | ⊙   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fied at z = 3. As a result, the PBH host halo merges bution for Pop II stars follows a Chabrier IMF, with a
into the final system at an earlier stage than in the mass range of 0.08−100M ⊙ (J. Jaacks et al. 2019).
corresponding runs without the “ 2” suffix. The stellar feedback is composed of ionization heat-
In all hydrodynamic runs listed in Table 1 (PBH M1e7, ing, Lyman-Werner (LW) radiation that dissociates H 2 ,
PBH M1e7 dense, PBH M1e7 2sig, PBH M1e7 2sigzoom, supernova (SN) feedback that includes thermal energy
PBH M1e5 2sigzoom, and PBH M1e5 2sigzoom 2), the injection, and metal enrichment (J. Jaacks et al. 2018,
dark matter and gas particle masses are 5.1×104M 2019; B. Liu & V. Bromm 2020a). Specifically, the
⊙
and9.6×103M
⊙ , respectively. Thisresolutionpertains LW background is computed from the sum of a global
to the refined region in the respective runs. star formation rate density contribution and local stel-
larsources,assuminganopticallythickregimewithself-
|     | 2.2. | Star Formation | and | Feedback |     | Physics |     |           |     |          |         |            |     |        |        |
| --- | ---- | -------------- | --- | -------- | --- | ------- | --- | --------- | --- | -------- | ------- | ---------- | --- | ------ | ------ |
|     |      |                |     |          |     |         |     | shielding |     | included | (B. Liu | & V. Bromm |     | 2020a) | 12. We |
The BH accretion and thermal/radiative feedback modelintergalacticmedium(IGM)photo-ionizationus-
subgrid models are implemented using the numerical ingaspatiallyuniformUVbackgroundbasedonthecal-
prescriptions from our previous work (S. Zhang et al. culation of C.-A. Faucher-Gigu`ere et al. (2009), with a
2025a, 2026). The growth of the central PBH is self- characteristicself-shieldingscaleof∼1kpc. Afterchar-
consistently tracked and computed using Bondi–Hoyle– acteristic lifetimes of ∼3 Myr for Pop III particles and
Lyttletonaccretion,andfeedbackisimplementedbyde- ∼ 20 Myr for Pop II particles, SN feedback is applied
positing a fraction of the accretion energy into the sur- following the prescription of J. Jaacks et al. (2018); B.
rounding gas. We adopt a fiducial coupling efficiency Liu & V. Bromm (2020a).
|     |          |                 |       |        |      |               |     | Since | individual |     | blast waves | are | unresolved, |     | we adopt |
| --- | -------- | --------------- | ----- | ------ | ---- | ------------- | --- | ----- | ---------- | --- | ----------- | --- | ----------- | --- | -------- |
| of  | ϵ r = ∆E | •,inj /(L •,acc | ∆t) = | 0.005, | as a | value capable |     |       |            |     |             |     |             |     |          |
of reproducing some of the overly massive and pristine asubgridSNlegacymodelinwhichthemetalyieldsare
BHsobservedbyJWST(S.Zhangetal.2026)11. deposited into gas particles within a characteristic final
Here,
L is the accretion luminosity, and ∆E is the en- shell radius of ∼ 650pc. The adopted metal yields are
| •,acc                                           |     |     |     |     |     | •,inj |     |       |     |         |               |     |       |     |        |
| ----------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ------- | ------------- | --- | ----- | --- | ------ |
|                                                 |     |     |     |     |     |       |     | ∼ 39M |     | for Pop | III particles | and | ∼ 10M | for | Pop II |
| ergyinjectedintotheambientgasoverthetimestep∆t. |     |     |     |     |     |       |     |       | ⊙   |         |               |     |       | ⊙   |        |
AdragforcewasalsoappliedtoBHparticlesduringac- ones. For Pop III particles, we also impose energy in-
|                                      |     |     |     |     |     |            |     | jectionof∼7×1051erg |     |     | andinstantaneousionizationin |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ---------- | --- | ------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- |
| cretiontoconservemomentumaccordingto |     |     |     |     |     | V.Springel |     |                     |     |     |                              |     |     |     |     |
et al. (2005). This choice mitigates numerical kicks as- theSNbubble(B.Liu&V.Bromm2020b). Inaddition,
|          |      |             |           |     |          |     |       | we  | include | SN-driven | winds | following | V.  | Springel | & L. |
| -------- | ---- | ----------- | --------- | --- | -------- | --- | ----- | --- | ------- | --------- | ----- | --------- | --- | -------- | ---- |
| sociated | with | very strong | accretion |     | episodes | and | helps |     |         |           |       |           |     |          |      |
prevent artificial BH wandering from the galaxy center Hernquist (2003) for both Pop III and Pop II: gas par-
at lower redshift. ticles associated with star formation are stochastically
As the gas will aggregate around the PBH-seeded launched with mass-loading factor η = 2 and kick
w,SF
halo,starformationoccurswhengasbecomesJeansun- velocity v ≃ 170kms−1. Wind particles recouple
w,SF
stable and survives both BH accretion and feedback- to the ISM after t = 0.1H−1(t), or once their density
w
driven dispersal long enough to undergo free-fall col- fallsbelown =10cm−3. Theseprescriptionsallowun-
w
| lapse. | The | stellar population |     | is  | assigned | according |     |       |        |         |        |              |      |              |     |
| ------ | --- | ------------------ | --- | --- | -------- | --------- | --- | ----- | ------ | ------- | ------ | ------------ | ---- | ------------ | --- |
|        |     |                    |     |     |          |           |     | 12 We | do not | include | the LW | contribution | from | BH accretion | in  |
11 this work; its possible impact has been discussed in S. Zhang
|     | The impact | of varying | this parameter |     | has been | explored | in  |     |     |     |     |     |     |     |     |
| --- | ---------- | ---------- | -------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
etal.(2025a,b)
previouswork;seeS.Zhangetal.(2025a,2026)fordetails.

6
| resolved                                     | SN  | feedback | to regulate |     | star | formation, | metal |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | -------- | ----------- | --- | ---- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| enrichment,andgasremovalinthesimulatedhalos. |     |          |             |     |      |            | For   |     |     |     |     |     |     |     |     |
amoredetaileddescriptionofthestellarfeedbackrecipe,
| one can     | refer  | to B. Liu      | & V.        | Bromm         | (2020a).       |           |           |     |     |     |     |     |     |     |     |
| ----------- | ------ | -------------- | ----------- | ------------- | -------------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|             | 3.     | RESULTS        | AND         | DISCUSSIONS   |                |           |           |     |     |     |     |     |     |     |     |
| Based       | on the | initial        | conditions  |               | and            | numerical | setup     |     |     |     |     |     |     |     |     |
| described   | above, | we             | now present |               | the simulation |           | results   |     |     |     |     |     |     |     |     |
| and discuss |        | their physical |             | implications. |                | To        | highlight |     |     |     |     |     |     |     |     |
theenvironmentaldependenceofPBH-seededevolution,
| we organize | this | section | around | four | connected |     | aspects. |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------- | ------ | ---- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Wefirstexaminehowthelarge-scaleenvironmentdrives
| distinct     | BH–host       | evolutionary          |                 | pathways    |            | in Section | 3.1.      |     |     |     |     |     |     |     |     |
| ------------ | ------------- | --------------------- | --------------- | ----------- | ---------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Building     | on            | these trends,         |                 | we identify |            | the main   | evolu-    |     |     |     |     |     |     |     |     |
| tionary      | phases        | and                   | possible        | transitions |            | toward     | normal    |     |     |     |     |     |     |     |     |
| galaxy–AGN   |               | configurations        |                 | in Section  |            | 3.2.       | We then   |     |     |     |     |     |     |     |     |
| connect      | these         | regimes               | to stellar      |             | growth     | and        | metal en- |     |     |     |     |     |     |     |     |
| richment     | in Section    |                       | 3.3 before      | translating |            | the        | resulting |     |     |     |     |     |     |     |     |
| evolutionary |               | stages                | into observable |             | signatures |            | for cur-  |     |     |     |     |     |     |     |     |
| rent and     | future        | surveys               | in              | Section     | 3.4.       |            |           |     |     |     |     |     |     |     |     |
|              | 3.1.          | Environment-dependent |                 |             | Evolution  |            |           |     |     |     |     |     |     |     |     |
| Our          | previous      | simulations           |                 | approached  |            | PBH        | evolution |     |     |     |     |     |     |     |     |
| from two     | complementary |                       |                 | limits.     | In the     | full       | hydrody-  |     |     |     |     |     |     |     |     |
namicalruns,thePBHwasplacednearthecenterofthe
| simulation | volume, |     | allowing | us to | isolate | the | local seed |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | -------- | ----- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
effectongasaccretion,starformation,andfeedbackina
| region   | close to | the cosmic | mean     | density          |     | (S. Zhang | et al.   |     |     |     |     |     |     |     |     |
| -------- | -------- | ---------- | -------- | ---------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025a,b, | 2026).   | In         | separate | dark-matter-only |     |           | calcula- |     |     |     |     |     |     |     |     |
tions,PBHswereinsteadplacedaccordingtothedensity
| fluctuation | field,             | showing    | that | they        | can      | become | embed-    |     |     |     |     |     |     |     |     |
| ----------- | ------------------ | ---------- | ---- | ----------- | -------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ded in      | larger-scale       | structures |      | or          | in halos | whose  | masses    |     |     |     |     |     |     |     |     |
| exceed      | the characteristic |            |      | PBH-induced |          | halo   | scale (S. |     |     |     |     |     |     |     |     |
M˜
| Zhang | et al. | 2024a), | given | by  |     | ∝(z | /z)M , ac- |     |     |     |     |     |     |     |     |
| ----- | ------ | ------- | ----- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
h,PBH eq • Figure1. ComparisonbetweenBHaccretionandhalo-scale
| cording | to the | analytic | estimate |     | of K. | J. Mack | et al. |                      |     |     |     |          |                  |     |     |
| ------- | ------ | -------- | -------- | --- | ----- | ------- | ------ | -------------------- | --- | --- | --- | -------- | ---------------- | --- | --- |
|         |        |          |          |     |       |         |        | massinflowforthe107M |     |     |     | PBHruns. | Thetoppanelshows |     |     |
⊙
(2007). The present simulations connect these two ap- theBHaccretionrate,M˙
• ,whilethemiddleandbottompan-
| proaches | by  | following | the | baryonic | evolution |     | of PBHs |          |     |         |             |     |              |          |     |
| -------- | --- | --------- | --- | -------- | --------- | --- | ------- | -------- | --- | ------- | ----------- | --- | ------------ | -------- | --- |
|          |     |           |     |          |           |     |         | els show | the | gas and | dark-matter |     | inflow rates | measured | at  |
|          |     |           |     |          |           |     |         |          |     | M˙      |             |     | M˙           |          |     |
placed in different initial cosmological environments. the virial radius, (R ) and (R ). The bot-
|     |     |     |     |     |     |     |     |     |     | gas,in | vir |     | DM,in | vir |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ----- | --- | --- |
Figure 1 compares the BH accretion history with tomaxisgivescosmictime,andthetopaxisgivesthecorre-
|                |     |         |             |     |        |       |         | spondingredshift. |     | Theoverdenserunsshowlargerhalo-scale |     |     |     |     |     |
| -------------- | --- | ------- | ----------- | --- | ------ | ----- | ------- | ----------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
| the halo-scale |     | gas and | dark-matter |     | inflow | rates | for the |                   |     |                                      |     |     |     |     |     |
107M PBH runs. In the isolated PBH M1e7 case, inflowandmoreburstyBHaccretionthantheisolatedcase,
⊙
|        |           |        |      |        |       |       | M˙         | illustrating | the      | connection | between |     | structure | formation | and |
| ------ | --------- | ------ | ---- | ------ | ----- | ----- | ---------- | ------------ | -------- | ---------- | ------- | --- | --------- | --------- | --- |
| the BH | accretion | rate   | (top | panel) | first | rises | to ∼       |              |          |            |         |     |           |           |     |
|        |           |        |      |        |       |       | •          | PBH          | fueling. |            |         |     |           |           |     |
| 10−3M  | yr−1      | around | z ∼  | 8 –    | 9 (f  | ∼     | 10−2), and |              |          |            |         |     |           |           |     |
|        | ⊙         |        |      |        | Edd   |       |            |              |          |            |         |     |           |           |     |
M˙
| then gradually |     | declines | toward |      | ∼       | 10−4M   | yr−1 at |     |           |     |           |     |           |            |     |
| -------------- | --- | -------- | ------ | ---- | ------- | ------- | ------- | --- | --------- | --- | --------- | --- | --------- | ---------- | --- |
|                |     |          |        |      | •       |         | ⊙       | By  | contrast, | the | overdense |     | runs show | systemati- |     |
| later times    | (f  | ∼        | 10−3). | This | decline | follows | the re- |     |           |     |           |     |           |            |     |
Edd
|                     |              |         |                             |               |              |         |           | cally     | larger          | halo-scale | inflow  | and         | more   | bursty | BH fu-   |
| ------------------- | ------------ | ------- | --------------------------- | ------------- | ------------ | ------- | --------- | --------- | --------------- | ---------- | ------- | ----------- | ------ | ------ | -------- |
| duction             | of the       | gas     | inflow                      | rate (middle  |              | panel)  | through   |           |                 |            |         |             |        |        |          |
|                     |              |         |                             |               |              |         |           | eling.    | For             | PBH M1e7   | dense,  | the         | gas    | inflow | rate re- |
| the virial          | radius,      | which   | decreases                   |               | from         | M˙      | (R ) ∼    |           |                 |            |         |             |        |        |          |
|                     |              |         |                             |               |              | gas,in  | vir       |           | M˙              |            |         |             | yr−1   |        |          |
|                     |              |         |                             |               | ≲10−1M       |         |           | mains     | at              | gas,in (R  | vir ) ∼ | 0.3 –       | 1M ⊙   | over   | an ex-   |
| 3×10−1M             |              | yr−1 at | early                       | times         | to           |         | yr−1 to-  |           |                 |            |         |             |        |        |          |
|                     | ⊙            |         |                             |               |              |         | ⊙         | tended    | period,         | while      | the     | dark-matter |        | inflow | rate is  |
| wardtheendoftherun. |              |         | Thecorrespondingdark-matter |               |              |         |           |           |                 |            |         |             |        |        |          |
|                     |              |         |                             |               |              |         |           |           | M˙              |            |         |             | yr−1.  |        |          |
|                     |              |         |                             |               |              |         |           | typically | DM,in           | ∼          | 4 −     | 10M ⊙       |        | The BH | accre-   |
| inflow              | rate (bottom |         | panel)                      | is relatively |              | modest, | remain-   |           |                 |            |         |             |        |        |          |
|                     |              |         |                             |               |              |         |           | tion rate | correspondingly |            |         | fluctuates  | around | M˙     | ∼10−3    |
| ing at              | the level    | of M˙   | (R                          | )             | ∼ 1M         | yr−1    | or below, |           |                 |            |         |             |        |        | •        |
|                     |              |         | DM,in                       | vir           |              | ⊙       |           |           | 10−2M           | yr−1       |         |             | 10−2   | 10−1), |          |
|                     |              |         |                             |               |              |         |           | – few     | ×               | ⊙          | (f      | Edd ∼       |        | –      | with     |
| indicating          | slow         | halo    | growth                      | in this       | environment. |         |           |           |                 |            |         |             |        |        |          |

7
Figure 2. Evolution of the black-hole-to-stellar mass ratio, M /M (left), and black-hole-to-halo mass ratio, M /M
• ⋆ • h,PBH
(right), as a function of redshift. Solid curves show the PBH-seeded simulations in different environments presented in this
work, while dash-dotted curves show the “ M5e7 ” runs with different feedback prescriptions in a cosmic-average environment
from S. Zhang et al. (2026); dashed extensions indicate linear extrapolations of those runs to z = 5. Dotted curves show
representative DCBH models from J. Jeon et al. (2025a). Observed estimates for GN-z11, UHZ-1, and Abell 2744-QSO1 are
markedbyredstars(valuesadoptedfromP.Natarajanetal.2024;J.Scholtzetal.2024;R.Maiolinoetal.2024b;I.Juodˇzbalis
etal.2026;A.Kashlinskyetal.2026). Intheleftpanel,theshadedregionsindicatetheapproximateparameterspaceassociated
with LRD-like systems (e.g., R. Maiolino et al. 2024a; D. D. Kocevski et al. 2025) and the typical BH–stellar mass relation
from local observations (J. Kormendy & L. C. Ho 2013). In the right panel, the shaded band marks the approximate ΛCDM
limit for any baryonic component, M /M ≲ Ω /(Ω −Ω ). The isolated PBH runs remain highly overmassive relative
• h,PBH b m b
to their stellar components because star formation is inefficient, whereas PBHs in overdense environments undergo more rapid
stellar assembly and evolve toward lower M /M . By z ≲10, some PBH systems born in overdense regions reach less extreme
• ⋆
mass ratios compared to high-redshift BH-dominated sources, while continuing structure growth can drive them toward more
conventional galaxy–AGN configurations.
shortburstsreachinghighervalues. ThePBH M1e7 2sig GN-z11, UHZ-1, and Abell 2744-QSO1 are also shown
andPBH M1e7 2sigzoomruns,althoughfollowedonlyto forcomparison(valuesadoptedfromP.Natarajanetal.
higherredshift,exhibitthesamebehavioratearliercos- 2024; J. Scholtz et al. 2024; R. Maiolino et al. 2024b; I.
mic times than the PBH M1e7 dense run, with elevated Juodˇzbalis et al. 2026; A. Kashlinsky et al. 2026).
gas and dark-matter inflow associated with rapid halo In the isolated PBH M1e7 run, star formation remains
assembly. These results show that the different BH ac- inefficient throughout the simulation due to strong ac-
cretionhistoriesareconnectedtothelarger-scalesupply cretion heating and inefficient gas inflow, similar to
of matter: overdense environments continue to deliver the behavior of the “PBH SF M5e7” models previously
gas to the PBH-hosting halo, whereas the isolated case used to study Abell 2744-QSO1 in S. Zhang et al.
is more easily starved once the initial gas reservoir is (2026). The system maintains an extreme mass ratio,
depleted or affected by feedback. M /M ≥ 4 × 104, from the onset of galaxy forma-
• ⋆
The same environmental separation appears in the tion down to z ∼ 4, where the ratio reaches its mini-
mass-ratio evolution shown in Figure 2. We track both mum value. It therefore remains substantially more BH
the BH-to-stellar mass ratio, M /M , and the BH-to- dominated than the observed high-redshift systems. Its
• ⋆
halo mass ratio, M /M , as functions of redshift. M /M track lies above the plotting range of Figure 2
• h,PBH • ⋆
For reference, the green shaded region indicates the ap- at all times and is therefore not visible in the left panel.
proximaterangeforthelocalBH-to-stellarmassrelation The absence of sustained stellar assembly prevents this
at M /M ≲ 0.002 (J. Kormendy & L. C. Ho 2013), branch from evolving toward regimes with lower mass
• ⋆
while the red shaded region marks the broad range ratios.
of ratios at ∼ 0.01−1 associated with compact, BH- In the overdense PBH M1e7 dense run, the PBH is
dominatedsystems(e.g.,R.Maiolinoetal.2024a;D.D. supplied by a denser environment and accretes more
Kocevski et al. 2025). Representative measurements for efficiently, but the stellar and halo components grow

8
| substantially | faster. |          | Star formation |         | occurs    | both | within    |     |     |     |     |     |     |     |     |
| ------------- | ------- | -------- | -------------- | ------- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the PBH       | host    | halo and | in             | nearby  | minihalos |      | that sub- |     |     |     |     |     |     |     |     |
| sequently     | merge   | with     | the            | central | system.   | As   | a result, |     |     |     |     |     |     |     |     |
M /M decreasesbyseveralordersofmagnitude,evolv-
• ⋆
| ing from | an initially |     | extreme | PBH-dominated |     |     | state at |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ------- | ------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
≳
| z 9 | to M /M | ∼   | 0.1 by | z ∼ | 5. The | evolution | of  |     |     |     |     |     |     |     |     |
| --- | ------- | --- | ------ | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• ⋆
| M /M | follows |     | the same | qualitative |     | trend: | over- |     |     |     |     |     |     |     |     |
| ---- | ------- | --- | -------- | ----------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
• h,PBH
| dense environments |                    | allow                               | the       | host          | halo          | to grow      | quickly    |        |     |                         |     |     |     |           |            |
| ------------------ | ------------------ | ----------------------------------- | --------- | ------------- | ------------- | ------------ | ---------- | ------ | --- | ----------------------- | --- | --- | --- | --------- | ---------- |
| enough             | that the           | PBH                                 | becomes   | a             | progressively |              | smaller    |        |     |                         |     |     |     |           |            |
| fraction           | of the             | total halo                          | mass.     |               |               |              |            |        |     |                         |     |     |     |           |            |
| The                | higher-overdensity |                                     |           | realizations, |               | PBH          | M1e7 2sig  |        |     |                         |     |     |     |           |            |
| and PBH            | M1e7               | 2sigzoom,                           | exhibit   |               | an even       | earlier      | onset      |        |     |                         |     |     |     |           |            |
| of star            | formation,         | beginning                           |           | at            | z ∼ 30.       | Because      | the        |        |     |                         |     |     |     |           |            |
| surrounding        | structure          |                                     | collapses | earlier       |               | and supplies | the        |        |     |                         |     |     |     |           |            |
| PBH host           | more               | efficiently,                        |           | the stellar   | component     |              | grows      |        |     |                         |     |     |     |           |            |
| rapidlyandM        | •                  | /M ⋆ reachestheapproximaterange0.1– |           |               |               |              |            |        |     |                         |     |     |     |           |            |
| 1 by z             | ∼ 11–8.            | These                               | tracks    | therefore     |               | enter        | the regime |        |     |                         |     |     |     |           |            |
|                    |                    |                                     |           |               |               |              |            | Figure |     | 3. Eddington-normalized |     |     | BH  | accretion | histories, |
occupiedbycompacthigh-redshiftBHhostsearlierthan
extendingFigure1totherefined-regionrealizationsandthe
the less overdense branch and continued stellar assem- 105M 107M
|     |     |     |     |     |     |     |     |     | ⊙   | seed runs. | The | ⊙   | PBHs generally |     | accrete at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | -------------- | --- | ---------- |
bly subsequently drives them toward lower mass ratios. M˙ /M˙ ∼ 10−3–10−2 with intermittent bursts, whereas
• Edd
These track pass through the range occupied by UHZ- the lighter seeds remain at lower Eddington ratios. The
|             |         |     |               |     |              |     |      | centrally |     | placed | PBH M1e5 | 2sigzoom | 2 seed | nevertheless | ex- |
| ----------- | ------- | --- | ------------- | --- | ------------ | --- | ---- | --------- | --- | ------ | -------- | -------- | ------ | ------------ | --- |
| 1 and other | compact |     | high-redshift |     | BH-dominated |     | sys- |           |     |        |          |          |        |              |     |
tems, although they remain above the local relation by periences stronger and more frequent fueling than the cor-
|                 |              |             |           |         |          |               |            | responding |       | offset    | realization, | illustrating |               | the additional | de-         |
| --------------- | ------------ | ----------- | --------- | ------- | -------- | ------------- | ---------- | ---------- | ----- | --------- | ------------ | ------------ | ------------- | -------------- | ----------- |
| the end         | of the       | simulation. |           |         |          |               |            |            |       |           |              |              |               |                |             |
|                 |              |             |           |         |          |               |            | pendence   |       | on seed   | placement    | and          | halo assembly |                | history.    |
| For comparison, |              | a           | version   | of DCBH |          | models        | explored   |            |       |           |              |              |               |                |             |
| by (J.          | Jeon et      | al. 2025a,  |           | 2026c)  | exhibit  | qualitatively |            |            |       |           |              |              |               |                |             |
|                 |              |             |           |         |          |               |            | does       | not   | require   | exact        | agreement    | with          | the            | local BH–   |
| different       | evolutionary |             | behavior. |         | In these | models,       | star       |            |       |           |              |              |               |                |             |
|                 |              |             |           |         |          |               |            | galaxy     |       | scaling   | relations.   | Instead,     | it            | refers         | to a pro-   |
| formation       | in a         | neighboring |           | halo    | first    | establishes   | the        |            |       |           |              |              |               |                |             |
|                 |              |             |           |         |          |               |            | gressive   |       | reduction | in           | the relative | dominance     |                | of the ini- |
| radiative       | conditions   |             | required  | for     | direct   | collapse      | (e.g.,     |            |       |           |              |              |               |                |             |
|                 |              |             |           |         |          |               |            | tial       | seed, | such      | that stellar | and          | halo growth   | outpace        | BH          |
| E. Visbal       | et al.       | 2014;       | J.        | F. W.   | Baggen   | et            | al. 2026). |            |       |           |              |              |               |                |             |
|                 |              |             |           |         |          |               |            | growth     |       | and drive | both         | M /M         | and M         | /M             | toward      |
The DCBH therefore forms only after baryonic struc- • ⋆ • h,PBH
|     |     |     |     |     |     |     |     | the | ranges | occupied | by  | more | conventional | high-redshift |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ---- | ------------ | ------------- | --- |
tureformationhasbegun,incontrasttothePBHseeds,
|       |             |        |     |               |     |     |            | galaxy–AGN |     | systems. |     |     |     |     |     |
| ----- | ----------- | ------ | --- | ------------- | --- | --- | ---------- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
| which | are present | before |     | the formation |     | of  | their host |            |     |          |     |     |     |     |     |
galaxies. Across the snapshots in which the DCBHs Figure 3 shows that different seed realizations experi-
|                 |     |             |     |        |     |           |     | ence | distinct | fueling | histories |     | even within | broadly | sim- |
| --------------- | --- | ----------- | --- | ------ | --- | --------- | --- | ---- | -------- | ------- | --------- | --- | ----------- | ------- | ---- |
| are identified, |     | the systems |     | span M | /M  | ∼ 0.01–10 | and |      |          |         |           |     |             |         |      |
|                 |     |             |     |        | •   | ⋆         |     |      |          |         |           |     | 107M        |         |      |
subsequently show comparatively fluctuating evolution ilar overdense environments. The ⊙ PBHs typi-
|         |          |     |           |     |       |     |           | cally | accrete | at  | f   | ∼ 10−3–10−2 | during | the | main as- |
| ------- | -------- | --- | --------- | --- | ----- | --- | --------- | ----- | ------- | --- | --- | ----------- | ------ | --- | -------- |
| without | a common |     | monotonic |     | trend | 13. | More pro- |       |         |     | Edd |             |        |     |          |
nounced decreases occur when the DCBH host merges sembly phase, with intermittent bursts reaching f Edd ∼
|        |             |     |              |     |         |       |         | 0.1 | or higher |     | in the | more overdense |     | runs. | By con- |
| ------ | ----------- | --- | ------------ | --- | ------- | ----- | ------- | --- | --------- | --- | ------ | -------------- | --- | ----- | ------- |
| with a | neighboring |     | star-forming |     | galaxy, | whose | stellar |     |           |     |        |                |     |       |         |
105M
mass rapidly lowers M /M . trast, the offset ⊙ seed in PBH M1e5 2sigzoom re-
• ⋆
|     |     |     |     |     |     |     |     | mains | weakly |     | fueled for | most | of its evolution, |     | typically |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | ---------- | ---- | ----------------- | --- | --------- |
10−6–10−4.
3.2. Road to Normalcy at f Edd ∼ The corresponding “ 2” realiza-
|     |     |     |     |     |     |     |     | tionexperiencesmorefrequentepisodesatf |     |     |     |     |     |     | ∼10−4– |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | ------ |
Edd
The results of Section 3.1 show that the cosmological 10−3, 10−2.
|     |     |     |     |     |     |     |     |     | with | occasional |     | excursions | to ∼ |     | This dif- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | --- | ---------- | ---- | --- | --------- |
environmentregulatesthegassupplyandco-evolutionof
|             |          |     |     |             |     |     |             | ference |        | reflects | the initialization |                 | of the | “ 2”         | seed near |
| ----------- | -------- | --- | --- | ----------- | --- | --- | ----------- | ------- | ------ | -------- | ------------------ | --------------- | ------ | ------------ | --------- |
| PBH-hosting | systems. |     | We  | now examine |     | how | the initial |         |        |          |                    |                 |        |              |           |
|             |          |     |     |             |     |     |             | the     | center | of       | a halo that        | is subsequently |        | incorporated |           |
PBHmassanditsplacementwithintheassemblingover-
|     |     |     |     |     |     |     |     | into | the | assembling | main | system, | allowing | it  | to remain |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---------- | ---- | ------- | -------- | --- | --------- |
dense region modify this evolution. Here, “normalcy” more closely coupled to the available gas supply. Nev-
| is defined | in an | evolutionary, |     | trend-driven |     |     | sense. It |            |           |          |          |          |          |        |           |
| ---------- | ----- | ------------- | --- | ------------ | --- | --- | --------- | ---------- | --------- | -------- | -------- | -------- | -------- | ------ | --------- |
|            |       |               |     |              |     |     |           | ertheless, |           | BH       | growth   | remains  | modest   | in all | cases due |
|            |       |               |     |              |     |     |           | to         | accretion | feedback |          | and lack | of dense | gas,   | with the  |
|            |       |               |     |              |     |     |           | cumulative |           | mass     | increase | of ∆M    | (z       | )/M    | (z )≲0.5  |
13 The first plotted DCBH point corresponds to the first saved • final • ini
|          |          |     |       |             |        |      |           | by  | the end | of  | the simulations. |     |     |     |     |
| -------- | -------- | --- | ----- | ----------- | ------ | ---- | --------- | --- | ------- | --- | ---------------- | --- | --- | --- | --- |
| snapshot | in which | the | BH is | identified, | rather | than | its exact |     |         |     |                  |     |     |     |     |
formationtime.

9
Figure 4. Evolution of the BH-to-stellar mass ratio, M /M (left), and the BH-to-host-halo mass ratio, M /M (right),
• ⋆ • h,PBH
for the full-volume and refined-region simulations spanning different PBH seed masses and initial placements within overdense
environments. Theobservationalreferenceregionsandindividualhigh-redshiftsystemsarethesameasinFigure2. The105M
⊙
seedrealizationsevolvetowardlowermassratiosthanthecorresponding107M cases,asstellarandhaloassemblymorerapidly
⊙
outpace BH growth. The difference between the two 105M realizations further illustrates the sensitivity of the evolutionary
⊙
track to the initial PBH location and its subsequent incorporation into the assembling main halo.
The consequences for the BH-to-host mass ratios are sive PBH seeds remain recognizably overmassive for a
shown in Figure 4. As discussed above, the overdense longer period within similarly overdense environments.
107M runs evolve away from their initially extreme, Taken together, Figures 2 and 4 show that PBH-
⊙
BH-dominated configurations as stellar and halo as- seeded systems do not follow a unique evolutionary
sembly proceed, although they generally remain over- track. The explored parameter space encompasses per-
massive relative to their hosts throughout the simu- sistentlyBH-dominatedsystems,faintandweaklyfueled
lated interval, comparable to the observed LRD sys- seeds, and objects that rapidly develop comparatively
tems (e.g., R. Maiolino et al. 2024a). The 105M re- conventional BH-to-host mass ratios. As host assem-
⊙
alizations follow different pathways. Their M /M ra- bly proceeds, these bulk properties retain progressively
• ⋆
tios begin at ∼ 0.05–0.1 at z ∼ 20 and rapidly de- less information about the initial PBH seed. In partic-
cline toward host-dominated configurations. By z ∼10, ular, a system that reaches the mass-ratio regime oc-
PBH M1e5 2sigzoom reaches M /M ∼ O(10−3), while cupied by more conventional high-redshift galaxy–AGN
• ⋆
themorerapidlyassembled“ 2”realizationreachesval- systems may no longer retain its initial seeding condi-
ues of O(10−4). Their BH-to-halo mass ratios similarly tions. The clearest imprint of the seeding conditions is
decline from O(10−4) to O(10−5). Although the cen- therefore expected during the earlier BH-dominated or
trallyplaced“ 2”seedisfueledmoreefficientlythanthe weakly coupled phases (i.e. at z ≳ 10), before subse-
offset realization, its stellar and halo components grow quent stellar and halo growth drives the system toward
even faster, producing a lower BH-to-host mass ratio “normalcy”. In later stages, a single measurement of
comparable to that inferred for GN-z11 (A. J. Bunker M /M or M /M is unlikely to recover the initial
• ⋆ • h,PBH
et al. 2023; J. Scholtz et al. 2024; R. Maiolino et al. conditions without additional information on the host
2024b). The lighter-seed tracks therefore approach, and structure, environment, and evolutionary state.
inthe“ 2”casefallinto,thelocalreferencerangeshown
inFigure4. Thisdoesnotimplythatthesesystemshave 3.3. Star Formation and Metal Enrichment Histories
already converged onto the z = 0 scaling relation, but
The mass-ratio evolution above shows how different
demonstratesthataPBH-seededsystemcanlosetheex-
PBH systems move through the BH–host parameter
treme BH-to-host ratios associated with massive early
space. Wenextexaminethestellargrowthandchemical
seeds and appear comparatively conventional in these
enrichment responsible for these trajectories. Figure 5
bulkpropertiesbyz ∼10–8. Incontrast,themoremas-
compares the evolution of the stellar mass within the
host halo with its mass-weighted gas metallicity. Rapid

10
|     |     |     |     |     |     |     | In the       | relatively |           | isolated   | and    | feedback-dominated |              |          |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --------- | ---------- | ------ | ------------------ | ------------ | -------- |
|     |     |     |     |     |     |     | PBH systems, |            | stellar   | growth     | occurs | through            |              | only one |
|     |     |     |     |     |     |     | or a few     | short      | episodes, | consistent |        | with               | our previous | re-      |
|     |     |     |     |     |     |     | sults (S.    | Zhang      | et al.    | 2025a,     | 2026). | The                | “PBH         | SF M5e7” |
|     |     |     |     |     |     |     | models       | generally  | remain    |            | at M   | ∼                  | 105–106M     | for      |
|     |     |     |     |     |     |     |              |            |           |            |        | ⋆                  |              | ⊙        |
|     |     |     |     |     |     |     | extended     | periods    | following |            | their  | initial            | star-forming |          |
|     |     |     |     |     |     |     | episodes.    | The        | first     | SNe        | enrich | the halo           | gas          | to Z ∼   |
10−2.5–10−1.5Z
|     |     |     |     |     |     |     |     |     | , while | the | central | region |     | within ap- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ------ | --- | ---------- |
⊙
|     |     |     |     |     |     |     | proximately | 150pc                                     |     | of the | BH  | can temporarily |     | reach |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------------------------------- | --- | ------ | --- | --------------- | --- | ----- |
|     |     |     |     |     |     |     | Z ∼0.1Z     | . Oncestellargrowthstalls,however,thisen- |     |        |     |                 |     |       |
⊙
|     |     |     |     |     |     |     | richmentisnotsustained. |           |                                     |               | Metal-loadedoutflowsremove |     |          |            |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --------- | ----------------------------------- | ------------- | -------------------------- | --- | -------- | ---------- |
|     |     |     |     |     |     |     | part of                 | the newly | produced                            |               | metals,                    |     | while    | subsequent |
|     |     |     |     |     |     |     | halo growth             | is        | dominated                           |               | by relatively              |     | pristine | inter-     |
|     |     |     |     |     |     |     | galacticinflow.         |           | Themass-weightedhalometallicitycon- |               |                            |     |          |            |
|     |     |     |     |     |     |     | sequently               | decreases | by                                  | approximately |                            |     | one to   | two orders |
10−4–
|     |     |     |     |     |     |     | of magnitude, |      | with | several | tracks    | reaching | Z       | ∼      |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ---- | ------- | --------- | -------- | ------- | ------ |
|     |     |     |     |     |     |     | 10−2Z         | by z | ∼ 7. | The     | different | tracks   | further | illus- |
⊙
|     |     |     |     |     |     |     | trate the     | sensitivity |             | of metal | retention        |             | to the        | adopted    |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ----------- | -------- | ---------------- | ----------- | ------------- | ---------- |
|     |     |     |     |     |     |     | BH feedback   | efficiency  |             | 14.      |                  |             |               |            |
|     |     |     |     |     |     |     | The overdense |             | systems     |          | instead          | show        | sustained     | stel-      |
|     |     |     |     |     |     |     | lar assembly  |             | accompanied |          | by progressively |             |               | increasing |
|     |     |     |     |     |     |     | metallicity.  | In          | the         | PBH M1e7 | 2sigzoom         |             | runs,         | star for-  |
|     |     |     |     |     |     |     | mation        | begins      | at z        | ∼ 28,    | and              | the stellar | mass          | grows      |
|     |     |     |     |     |     |     |               | 105–106M    |             |          |                  |             | 107–108M      |            |
|     |     |     |     |     |     |     | from M        | ⋆ ∼         |             | ⊙ at     | z ∼              | 20 to       |               | ⊙ by       |
|     |     |     |     |     |     |     | z ∼ 9 –       | 8. Over     | the         | same     | period,          | the         | mass-weighted |            |
10−3–10−2Z
|        |              |     |         |          |                 |     | halo metallicity |       | increases |      | from  | Z ∼ |         | ⊙ to      |
| ------ | ------------ | --- | ------- | -------- | --------------- | --- | ---------------- | ----- | --------- | ---- | ----- | --- | ------- | --------- |
| Figure | 5. Evolution | of  | stellar | mass and | gas metallicity | of  |                  |       |           |      |       |     |         |           |
|        |              |     |         |          |                 |     | Z ∼ 0.1Z         | . The | PBH       | M1e7 | dense | run | follows | a similar |
⊙
| the simulated                                         | BH-hosting |             | systems. | The        | upper panel | shows     |         |          |                                   |     |         |      |         |       |
| ----------------------------------------------------- | ---------- | ----------- | -------- | ---------- | ----------- | --------- | ------- | -------- | --------------------------------- | --- | ------- | ---- | ------- | ----- |
|                                                       |            |             |          |            |             |           | pathway | at later | times:                            | its | stellar | mass | remains | below |
| the total                                             | stellar    | mass within | the      | host halo, | while       | the lower |         |          |                                   |     |         |      |         |       |
|                                                       |            |             |          |            |             |           | 106M    | untilz   | ∼10,butsubsequentlygrowstoapprox- |     |         |      |         |       |
| panelshowsthecorrespondingmass-weightedgasmetallicity |            |             |          |            |             |           | ⊙       |          |                                   |     |         |      |         |       |
108M
within the halo. The same colors and line styles denote the imately ⊙ by z ∼ 5, while the halo metallicity
same simulations in both panels, and the upper axis gives rises from Z ∼ 0.006Z to approximately 0.1Z . Al-
|     |     |     |     |     |     |     |     |     |     | ⊙   |     |     |     | ⊙   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thecorrespondingcosmictime,followingFigure2. Here,we though temporary declines occur during individual in-
furtherincludethetwo“ M1e5 ”runswithlighterPBHseeds flow or feedback episodes, the overall enrichment trend
of M =105 M . The PBH M1e7 run is not shown due to its remainspositive. Intheseenvironments,inflowinggasis
| •                        | ⊙           |     |                              |              |                |     |                 |              |           |             |         |      |           |        |
| ------------------------ | ----------- | --- | ---------------------------- | ------------ | -------------- | --- | --------------- | ------------ | --------- | ----------- | ------- | ---- | --------- | ------ |
| extremelylowstellarmass. |             |     | Rapidstellar-massgrowthinthe |              |                |     |                 |              |           |             |         |      |           |        |
|                          |             |     |                              |              |                |     | not exclusively |              | pristine, | as          | mergers | and  | accretion | from   |
| overdense                | PBH systems |     | in this                      | work (solid) | is accompanied |     |                 |              |           |             |         |      |           |        |
|                          |             |     |                              |              |                |     | neighboring     | star-forming |           | progenitors |         | also | supply    | previ- |
bysustainedchemicalenrichment,whereastheBHfeedback-
|     |     |     |     |     |     |     | ously enriched |     | material. | Continued |     | in-situ | star | forma- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --------- | --- | ------- | ---- | ------ |
-dominated,average-densityrealizationsfromS.Zhangetal.
|                        |     |     |      |         |         |            | tion and | enriched | inflow | therefore |     | compensate |     | for dilu- |
| ---------------------- | --- | --- | ---- | ------- | ------- | ---------- | -------- | -------- | ------ | --------- | --- | ---------- | --- | --------- |
| (2026) (dashed-dotted, |     | “   | M5e7 | ” runs) | undergo | only brief |          |          |        |           |     |            |     |           |
stellar-growth episodes, followed by metal loss and dilution. tion and feedback-driven metal loss.
The shaded region marks the approximate metallicity range The lighter-seed simulations show comparable or
| inferredforz>5LRDs,Z |     |     | ∼0.03–0.2Z |     | (G.P.Nikopoulos |     |               |     |         |        |     |       |     |           |
| -------------------- | --- | --- | ---------- | --- | --------------- | --- | ------------- | --- | ------- | ------ | --- | ----- | --- | --------- |
|                      |     |     |            |     | ⊙               |     | even stronger |     | stellar | growth |     | among | the | overdense |
etal.2026). RepresentativeestimatesforGN-z11andUHZ-1 PBH models compared with the heavier seeded runs.
| are shown                                           | as stars | with | errorbars, | while | the downward | ar- |         |               |     |     |             |     |          |         |
| --------------------------------------------------- | -------- | ---- | ---------- | ----- | ------------ | --- | ------- | ------------- | --- | --- | ----------- | --- | -------- | ------- |
|                                                     |          |      |            |       |              |     | In PBH  | M1e5 2sigzoom |     | 2,  | M increases |     | from     | approx- |
| rowdenotesthemetallicityupperlimitforAbell2744-QSO1 |          |      |            |       |              |     |         |               |     |     | ⋆           |     |          |         |
|                                                     |          |      |            |       |              |     | imately | 2 × 106M      |     | at  | z ∼ 20      | to  | 3 × 108M | by      |
| (J.Scholtzetal.2024;P.Natarajanetal.2024;R.Maiolino |          |      |            |       |              |     |         |               | ⊙   |     |             |     |          | ⊙       |
et al. 2026b). z ∼ 9, while the halo metallicity rises from approxi-
|           |      |                |     |           |      |           | mately 0.03Z |     | to 0.2Z | .   | The corresponding |     |     | run with- |
| --------- | ---- | -------------- | --- | --------- | ---- | --------- | ------------ | --- | ------- | --- | ----------------- | --- | --- | --------- |
|           |      |                |     |           |      |           |              | ⊙   |         | ⊙   |                   |     |     |           |
| increases | in M | trace episodes |     | of active | star | formation |              |     |         |     |                   |     |     |           |
⋆
| and merger-driven |     | stellar | assembly, |     | whereas | extended |            |      |          |       |            |           |     |             |
| ----------------- | --- | ------- | --------- | --- | ------- | -------- | ---------- | ---- | -------- | ----- | ---------- | --------- | --- | ----------- |
|                   |     |         |           |     |         |          | 14 For the | “PBH | SF M5e7” | runs, | the digits | following |     | “fd” denote |
plateaus indicate periods of weak or negligible stellar the adopted feedback efficiency; for example, “fd05” corre-
growth. Comparing the two panels therefore illustrates sponds to ϵr = 0.05. As discussed in our previous work, the
|           |             |     |            |     |          |         | resulting | stellar | mass | does | not vary | monotonically |     | with feed- |
| --------- | ----------- | --- | ---------- | --- | -------- | ------- | --------- | ------- | ---- | ---- | -------- | ------------- | --- | ---------- |
| how metal | production, |     | retention, | and | dilution | respond |           |         |      |      |          |               |     |            |
backefficiency.
| to the different |     | star-formation |     | histories. |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

11
| out the                               | “ 2”        | suffix begins |               | its major | stellar        | growth           | later,   |     |     |     |     |     |     |
| ------------------------------------- | ----------- | ------------- | ------------- | --------- | -------------- | ---------------- | -------- | --- | --- | --- | --- | --- | --- |
| atz ∼16,andreachesM                   |             |               |               | ≃2×107M   |                | andZ             | ∼0.1Z    |     |     |     |     |     |     |
|                                       |             |               | ⋆             |           |                | ⊙                | ⊙        |     |     |     |     |     |     |
| by z ∼9.                              | The         | earlier       | enrichment    |           | of the         | “ 2” realization |          |     |     |     |     |     |     |
| reflects                              | the more    | rapid         | incorporation |           |                | of its PBH       | host     |     |     |     |     |     |     |
| into the                              | assembling  |               | main          | halo.     | The weaker     | early            | accre-   |     |     |     |     |     |     |
| tion feedback                         |             | from          | the lighter   | PBH       | also           | allows           | a larger |     |     |     |     |     |     |
| fraction                              | of the      | enriched      | gas           | to remain |                | within the       | halo.    |     |     |     |     |     |     |
| For                                   | comparison, | the           | DCBH          | model     | (case          | C of             | J. Jeon  |     |     |     |     |     |     |
| et al.                                | 2025a)      | exhibits      | a weaker      |           | correspondence |                  | between  |     |     |     |     |     |     |
| stellar-massgrowthandhalometallicity. |             |               |               |           |                | Itsstellarmass   |          |     |     |     |     |     |     |
| increases                             | from        | approximately |               | 5×106M    |                | at z             | ∼ 11 to  |     |     |     |     |     |     |
⊙
3×108M
|             | ⊙       | by z ∼ | 5, whereas |     | its mass-weighted |     | halo |     |     |     |     |     |     |
| ----------- | ------- | ------ | ---------- | --- | ----------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
| metallicity | remains |        | at only    | Z ∼ | 10−3.5–10−2.8Z    |     | . By |     |     |     |     |     |     |
⊙
thefirstsnapshotinwhichtheDCBHisidentified,itre-
| sides in | a nearly | pristine |     | but already |     | relatively | massive |           |                                              |     |     |     |     |
| -------- | -------- | -------- | --- | ----------- | --- | ---------- | ------- | --------- | -------------------------------------------- | --- | --- | --- | --- |
|          |          |          |     |             |     |            |         | Figure 6. | Evolutionoftheintrinsicprojectedstellarhalf– |     |     |     |     |
≃3.7×108M
halo,withM h,DCBH ⊙ /hatz ∼11,accom- mass radius for the 107M PBH simulations in overdense
⊙
paniedbynearbygalaxiesthatprovidetherequiredLW environments. For each snapshot, the stellar component as-
sociatedwiththePBHisselectedwithinthehost-haloaper-
| radiation. | TheDCBHalsogrowsefficientlybyaccreting |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
gas from the central reservoir, which, together with BH ture, and the projected half-mass radius is measured along
|     |     |     |     |     |     |     |     | three orthogonal | viewing | directions. | The | solid curves | show |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ----------- | --- | ------------ | ---- |
feedback,candelaythebuildupofthestellarcomponent
themedianofthethreeprojectedradii,whiletheshadedre-
| relative | to the | growth | of  | the BH | and | halo. Even | after |                  |         |     |         |             |       |
| -------- | ------ | ------ | --- | ------ | --- | ---------- | ----- | ---------------- | ------- | --- | ------- | ----------- | ----- |
|          |        |        |     |        |     |            |       | gions span their | minimum | and | maximum | values. The | black |
substantial stellar assembly, the stellar component re- dashedcurveindicatestheadoptedeffectiveJWST/NIRCam
| mains | a small | fraction | of  | the much | larger | gas | reservoir, |                  |       |         |        |              |       |
| ----- | ------- | -------- | --- | -------- | ------ | --- | ---------- | ---------------- | ----- | ------- | ------ | ------------ | ----- |
|       |         |          |     |          |        |     |            | F200W resolution | scale | ( STScI | 2026), | and the open | down- |
so the metals produced by star formation contribute ward triangles identify snapshots whose intrinsic sizes fall
only weakly to the halo-wide mass-weighted metallicity. below this limit. The red dash-dotted line marks a repre-
|          |           |     |          |     |      |                   |     | sentative observed | LRD | effective | radius | of r ∼150pc. | The |
| -------- | --------- | --- | -------- | --- | ---- | ----------------- | --- | ------------------ | --- | --------- | ------ | ------------ | --- |
| The DCBH | evolution |     | pathways |     | show | more fluctuations |     |                    |     |           |        | e            |     |
observationalscaleshereareshownonlyasapproximateref-
| due to | partial | decoupling |     | between | BH  | growth, | stellar |     |     |     |     |     |     |
| ------ | ------- | ---------- | --- | ------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
erences.
| assembly, | and     | chemical      | enrichment, |     | than     | the | sustained |     |                    |     |            |     |     |
| --------- | ------- | ------------- | ----------- | --- | -------- | --- | --------- | --- | ------------------ | --- | ---------- | --- | --- |
| trends    | seen in | the overdense |             | PBH | systems. |     |           |     |                    |     |            |     |     |
|           |         |               |             |     |          |     |           |     | 3.4. Observational |     | Signatures |     |     |
Thesimulatedenrichmentpathwaysspanmuchofthe
metallicityrange inferredforcompacthigh-redshiftsys- In this section, we discuss the possible observational
|      |           |         |     |           |     |           |        | stages of PBH-seeded |     | systems, | ranging | from | faint or |
| ---- | --------- | ------- | --- | --------- | --- | --------- | ------ | -------------------- | --- | -------- | ------- | ---- | -------- |
| tems | (e.g., J. | Scholtz | et  | al. 2024; | P.  | Natarajan | et al. |                      |     |          |         |      |          |
2024; R. Maiolino et al. 2026b; G. P. Nikopoulos et al. weakly fueled sources to compact LRD-like objects and
2026). TheoverdensePBHhostsprogressivelyapproach moreextendedgalaxieshostingAGNs. Weusetheterm
the metallicities inferred for the broader LRD popula- “LRD-like” only in an approximate evolutionary sense,
tion, GN-z11, and UHZ-1 as sustained star formation referring to a stage in which a compact stellar com-
and enriched inflow become established. By contrast, ponent coexists with an accreting BH whose emission
the isolated, feedback-dominated systems experience would appear as an unresolved nuclear source.
only brief enrichment episodes and subsequently return To quantify the intrinsic stellar size, we first select
to lower halo metallicities through metal loss and dilu- star particles within the host-halo virial radius, R ,
vir
tion, approaching the extremely metal-poor regime rep- centered on the tracked PBH. A BH-centered shrink-
resented by Abell 2744-QSO1. The comparison there- ing aperture is then applied to remove spatially dis-
fore suggests that metallicity primarily traces the sub- tinct stellar clumps: the aperture is reduced until the
sequentassemblyandstar-formationhistoryofthehost mass-weighted centroid of the selected stellar compo-
environment, rather than the PBH seed alone. Quanti- nent lies within 0.1R vir of the PBH. For the remain-
tativecomparisonsremainapproximatebecausetheob- ing BH-associated stellar component, we calculate the
servationsgenerallyprobegas-phaseoxygenabundances projected radius enclosing half of the stellar mass along
in the nuclear or narrow-line-emitting region (e.g., R. each of three orthogonal viewing directions. Figure 6
Maiolino et al. 2026b; G. P. Nikopoulos et al. 2026), shows the resulting size evolution from z ∼ 15 to
whereasFigure5showsthemass-weightedgasmetallic- z ∼ 4 for the PBH M1e7 dense, PBH M1e7 2sig, and
runs.
| ity within | the | entire | host | halo. |     |     |     | PBH M1e7 2sigzoom |     |     |     |     |     |
| ---------- | --- | ------ | ---- | ----- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |

12
Figure 7. Evolution of the projected stellar surface density around the PBH in the PBH M1e7 dense simulation at z =8.35,
7.00, and 4.11 (from left to right). Each panel covers 2proper kpc, adopts the same surface-density normalization and spatial
binning, and is centered on the PBH, marked by the cyan circle. The stellar component evolves from a compact and irregular
configurationatz=8.35,throughamergingconfigurationatz=7.00,toanextended,centrallyconcentratedgalaxycontaining
additional substructure at z = 4.11. Over this interval, the stellar mass increases from 1.31×106 to 9.88×107M , whereas
⊙
the BH mass grows only from 1.36×107 to 1.90×107M . The sequence illustrates how rapid stellar assembly, rather than
⊙
substantial BH growth, moves the system away from its initially compact and BH-dominated configuration.
Figure8. Projectedstellarsurface-densitydistributionsaroundthePBHsinPBH M1e5 2sigzoom(left)andPBH M1e5 2sigzoom 2
(right) for the 105M PBH initial seed at z = 9.88, similar to Figure 7. In the offset realization, the PBH lies outside the
⊙
dominant stellar concentration, despite a total stellar mass of 2.31×107M , therefore labeled as a point-like object. In
⊙
the “ 2” realization, the PBH is associated with a prominent stellar component within a more massive and clumpy system,
M =2.08×108M . ThecontrastingmorphologiesprimarilyreflecttheinitialPBHplacementandsubsequenthaloassembly.
⋆ ⊙

13
In the PBH M1e7 dense system, star formation begins 10−4, the BH-powered emission is expected to be ex-
atz ∼11–10inastellarclumpthatisinitiallydisplaced tremely faint and may remain below current detection
from the PBH. After this component merges with the limits. Thisgeometryisqualitativelyreminiscentofsys-
PBH host, continued star formation and stellar assem- tems in which a weak compact source is spatially sepa-
blybuildacompactBH-associatedsystem. Itsprojected ratedfromthedominantstellarorline-emittingcompo-
U¨bler
half-mass radius remains below or close to the nominal nent, such as Hebe (R. Maiolino et al. 2026a; H.
F200W resolution over much of z ∼10–5, although the et al. 2026b), although Hebe itself is more likely pow-
intrinsic size fluctuates as new stellar clumps form and ered primarily by stars (J. Jeon et al. 2026b; E. Rusta
merge. At z ≲ 5, the host expands to R ≳ 300pc etal.2026). Inthe“ 2”realization,thePBHlieswithin
1/2
and would become increasingly likely to appear spa- a prominent stellar cluster embedded in a more massive
tially extended. By contrast, the PBH M1e7 2sig and and clumpy system, with M ≃ 2.1×108M . Its ac-
|     |     |     |     |     |     |     |     |     |        | ⋆   |       | ⊙   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----- | --- |
|     |     |     |     |     |     |     |     |     | M˙ /M˙ |     | 10−3, |     |
PBH M1e7 2sigzoomsystemsgenerallyoccupylargerand cretion remains weak, • Edd ∼ because the
more variable intrinsic sizes, R ∼ 0.2–1kpc. Their BHisstilldisplacedfromthedensestgasconcentration.
1/2
earlierstellarassemblyandclumpymergerhistoriescan The system is therefore galaxy dominated, although its
therefore produce resolved and spatially complex hosts geometry is qualitatively closer to high-redshift systems
at higher redshift. suchasGN-z11(J.Scholtzetal.2024). Theseexamples
To illustrate the transition away from the compact suggestthatlighterPBHseedsmayappearaseitheroff-
phase, we select three representative snapshots from nuclear,weaklyfueledBHsorasdynamicallyembedded
the evolution of the PBH M1e7 dense system and show sources, depending on their initial placement and sub-
their projected stellar surface-density distributions in sequent halo assembly.
Figure 7. At z ≃8.4, the stellar component around the The future appearance of all the simulated systems is
PBH is compact and irregular, with R 1/2 ≃ 110pc. At alsoexpectedtodependonenvironment. PBHsevolving
this stage, M ≃1.4×107M and M ≃1.4×106M , in relatively isolated or average-density regions may re-
|     | •   |     |     | ⊙   | ⋆   | ⊙   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
corresponding to M • /M ⋆ ∼ 10. By z ≃ 7.0, the stel- mainassociatedwithfaint,low-surface-brightnessgalax-
lar component has developed an elongated structure ies,orfallbelowobservationaldetectionlimits(S.Zhang
with R 1/2 ∼ 430pc, while its mass has increased to et al. 2025a; P. Dayal 2026). In rapidly assembling
M ≃ 2.0 × 107M . The corresponding mass ratio overdense regions, the same seeding channel may pass
| ⋆   |     | ⊙   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
has declined to M • /M ⋆ ∼ 0.7, placing the system near through an LRD-like phase before becoming difficult
thetransitionbetweenstronglyBH-dominatedandhost- to distinguish from a more conventional high-redshift
dominated configurations. galaxy hosting an AGN. Spatially resolved JWST IFU
By z ≃4.1, the stellar component has developed into spectroscopy, particularly when aided by strong grav-
an extended, centrally concentrated galaxy with addi- itational lensing, can separate the nuclear continuum,
tional substructure on approximately kiloparsec scales. stellarhost,andline-emittinggas(see,e.g.,I.Juodˇzbalis
Its stellar mass reaches M ≃ 9.9 × 107M , whereas etal.2026;M.Golubchiketal.2026;Q.Feietal.2026).
|     |     |     | ⋆   |     | ⊙   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the BH grows only to M ≃ 1.9 × 107M , yielding Resolving these components would improve constraints
|     |     |     | •   |     | ⊙   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M /M ∼ 0.2. Between the compact and extended onthestellaranddynamicalmasses,andthekinematics
• ⋆
snapshots, the stellar mass therefore increases by a fac- and metallicity of the surrounding gas. Combined with
tor of ∼ 75, compared with only a factor of ∼ 1.4 in estimates of M /M and BH accretion activity, these
• ⋆
BH mass. The system consequently leaves the LRD- measurements would place stronger constraints on dif-
like phaseprimarilythrough rapidassembly andspatial ferent seeding and evolutionary pathways.
| growth of          | the | stellar  | host,            | making   | the source | increas- |     |                |     |     |         |     |
| ------------------ | --- | -------- | ---------------- | -------- | ---------- | -------- | --- | -------------- | --- | --- | ------- | --- |
| ingly galaxy-like. |     | This     | is qualitatively |          | consistent | with     |     |                |     |     |         |     |
|                    |     |          |                  |          |            |          |     | 4. LIMITATIONS |     | AND | CAVEATS |     |
| observations       | of  | LRD-like | nuclei           | embedded | in         | extended |     |                |     |     |         |     |
Severallimitationsshouldbenotedwheninterpreting
stellarhostswhosedetectabilitydependsonredshiftand
|                    |     |        |            |     |            |     | our results. | First, the  | simulations |         | explore only | a lim- |
| ------------------ | --- | ------ | ---------- | --- | ---------- | --- | ------------ | ----------- | ----------- | ------- | ------------ | ------ |
| surface brightness |     | (e.g., | P. Rinaldi | et  | al. 2026). |     |              |             |             |         |              |        |
|                    |     |        |            |     |            |     | ited range   | of PBH seed | masses,     | initial | placements,  | and    |
Inthelighter-seedsimulations,thespatialrelationbe-
|     |     |     |     |     |     |     | large-scale | environments. | Most | of  | the analysis | focuses |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ---- | --- | ------------ | ------- |
tweenthePBHandthestellarcomponentintroducesan
|                              |          |         |           |                       |          |            | on a fiducial                                    | seed mass          | of M      | =107M    | , complemented |             |
| ---------------------------- | -------- | ------- | --------- | --------------------- | -------- | ---------- | ------------------------------------------------ | ------------------ | --------- | -------- | -------------- | ----------- |
| additionalsourceofdiversity. |          |         |           | Figure8comparesthetwo |          |            |                                                  |                    |           | •        | ⊙              |             |
|                              |          |         |           |                       |          |            | by refined-region                                | realizations       |           | with     | M = 105M       | . If        |
| 105M realizations            |          | at      | z ≃9.9.   | In PBH                | M1e5     | 2sigzoom,  |                                                  |                    |           |          | •              | ⊙           |
| ⊙                            |          |         |           |                       |          |            | PBHsaredrawnfromanextendedmassfunction,asex-     |                    |           |          |                |             |
| the PBH                      | remains  | offset  | by        | approximately         | a        | kiloparsec |                                                  |                    |           |          |                |             |
|                              |          |         |           |                       |          |            | pected in                                        | some formation     | scenarios |          | (e.g., B.      | Carr et al. |
| from the                     | dominant | stellar | cluster,  | which                 | contains | M ≃        |                                                  |                    |           |          |                |             |
|                              |          |         |           |                       |          | ⋆          | 2021),theirsubsequentevolutionarypathwaysmayspan |                    |           |          |                |             |
| 2.3×107M                     | . With   | an      | Eddington | ratio                 | of M˙    | /M˙ ∼      |                                                  |                    |           |          |                |             |
|                              | ⊙        |         |           |                       |          | • Edd      |                                                  |                    |           |          |                |             |
|                              |          |         |           |                       |          |            | a wider                                          | range. The initial | PBH       | location | is also        | varied      |

14
only in a controlled manner, by comparing an approx- trinsic projected half-mass radii, whereas observations
imately average-density region with an overdense La- measurewaveband-dependent,PSF-convolvedhalf-light
grangian patch. A more complete study would need radii. Likewise, the simulated metallicities are aver-
to sample the joint distribution of PBH mass and ini- aged over an extended halo aperture, while observa-
tial position in the primordial density field. This would tional estimates can be weighted more toward compact
provide a more general survey of the diverse configura- line-emitting gas near the nucleus or within bright star-
tions (for example triple black holes at high-z, see e.g., forming regions depending on the adopted diagnostic
U¨bler
H. et al. 2026a), possible when PBHs composed a lines (e.g., Z. Martinez et al. 2025; D. Miao et al. 2026;
non-negligible fraction of dark matter. B. Moreschini et al. 2026). A spatially extended stellar
Second, our calculations remain limited by compu- component may remain undetected because of low sur-
tational cost. The full-volume simulations allow us to facebrightnessorstrongoutshiningbytheBH,allowing
follow the large-scale environmental context, while the a system to retain an LRD-like appearance even when
refined-region runs focus on the selected PBH-host re- the host is intrinsically more extended (P. Rinaldi et al.
gion more efficiently. However, we cannot yet sample 2026). ThecharacteristicredcontinuumofLRDsisalso
large cosmological volumes and diverse environments notdeterminedbystellarsizealone,butdependsongas
≲3.
whilealsoresolvingindividualhoststoz Thecom- columndensity,obscuration,andradiativereprocessing.
putational expense rises rapidly after substantial star The observational benchmarks considered in this work
formation begins, as the number of star particles in- are subject to strong selection biases, so the same be-
creases and dense gas drives shorter time steps. The haviormaynotcoverthebroaderPBH-hostpopulation.
simulationsshouldthereforebeinterpretedascontrolled The comparisons presented here should therefore be re-
numerical experiments designed to isolate environmen- gardedasillustrativeratherthandemographic. Aquan-
tal trends, rather than as a statistically representative titative assessment will require forward modeling of the
population of PBH-hosting galaxies. Establishing the simulated stellar and BH emission using more realistic
relativefrequencyofthedifferentevolutionarypathways physical prescriptions, together with mock observations
will require larger volumes and a broader ensemble of that account for instrumental effects and survey cover-
| initial conditions. |               |     |       |          |     |             |     | age. |     |     |     |     |     |
| ------------------- | ------------- | --- | ----- | -------- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- |
| Third,              | the treatment |     | of BH | feedback | is  | simplified. | In  |      |     |     |     |     |     |
5. SUMMARY
| this work, | accretion | feedback |     | is implemented |     | through |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
thermal energy deposition in the surrounding gas, fol- In this work, we investigated the co-evolution of PBH
lowing the subgrid prescription adopted in previous seeds and their host galaxies using cosmological hydro-
studies(M. Tremmeletal. 2017). Other feedbackchan- dynamical simulations spanning different seed masses,
nels, including mechanical outflows, collimated winds, initial placements, and large-scale environments. Our
and radiation pressure, may regulate BH growth and main findings are summarized as follows:
| host-galaxy | evolution |     | differently | (see | the | review | by K. |     |     |     |     |     |     |
| ----------- | --------- | --- | ----------- | ---- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
•
Inayoshi et al. 2020). These processes could affect the PBHs provide an early seeding channel that does
gassupplyneartheBH,theefficiencyofstarformation, not require prior baryonic collapse. Their subse-
and the spatial distribution of metals within the host quent evolution is therefore strongly regulated by
galaxy. Theeffectivethermalcouplingfactorϵ assumed the surrounding cosmological environment. Com-
r
inourworkalsoremainsuncertain,andthereforeshould parisons between approximately average-density
be regarded as a phenomenological parameter rather regions and overdense Lagrangian patches show
than a fully predictive quantity. Bridging the scale be- that gas supply and halo assembly control both
tweentheunresolvedaccretionflowandthegalacticen- BH fueling, stellar growth and metal enrichment.
| vironment            | still          | remains              | a major  | challenge  |                      | for cosmolog- |         |                    |               |              |           |                   |          |
| -------------------- | -------------- | -------------------- | -------- | ---------- | -------------------- | ------------- | ------- | ------------------ | ------------- | ------------ | --------- | ----------------- | -------- |
|                      |                |                      |          |            |                      |               |         | • The simulations  |               | produce      | distinct  | environmental     |          |
| ical simulations     |                | (D. Angl´es-Alc´azar |          |            | et al.               | 2021).        | Future  |                    |               |              |           |                   |          |
|                      |                |                      |          |            |                      |               |         | pathways.          | In relatively |              | isolated  | regions,          | weak gas |
| work can             | incorporate    |                      | results  | from       | general-relativistic |               |         |                    |               |              |           |                   |          |
|                      |                |                      |          |            |                      |               |         | inflow leads       | to            | intermittent |           | BH accretion,     | lim-     |
| magnetohydrodynamics |                |                      | (GRMHD)  |            | simulations          |               | or con- |                    |               |              |           |                   |          |
|                      |                |                      |          |            |                      |               |         | itedstarformation, |               | andfaint,    |           | metal-poorsystems |          |
| nect BH              | growth         | across               | multiple | spatial    | scales               | through       |         |                    |               |              |           |                   |          |
|                      |                |                      |          |            |                      |               |         | with elevated      | M             | /M           | ≳ 10      | by z ∼ 5.         | In over- |
| refined simulations  |                | (e.g.,               | P. F.    | Hopkins    | et                   | al. 2024;     | H.      |                    |               | • ⋆          |           |                   |          |
|                      |                |                      |          |            |                      |               |         | dense regions,     |               | stellar      | assembly  | can begin         | as early |
| Cho et al.           | 2026;          | K.-Y.                | Su et    | al. 2026). |                      |               |         |                    |               |              |           |                   |          |
|                      |                |                      |          |            |                      |               |         | as z ∼ 30–15,      |               | while        | continued | inflow and        | merg-    |
| Finally,             | the connection |                      | between  | the        | simulation           |               | quan-   |                    |               |              |           |                   |          |
erssubsequentlydevelopintomoremassive,metal-
| tities and | observed | high-redshift |       | sources  |     | remains | ap-     |           |          |          |     |                 |      |
| ---------- | -------- | ------------- | ----- | -------- | --- | ------- | ------- | --------- | -------- | -------- | --- | --------------- | ---- |
|            |          |               |       |          |     |         |         | rich, and | extended | galaxies |     | spanning values | down |
| proximate. | The      | stellar       | sizes | reported |     | here    | are in- |           |          |          |     |                 |      |
≲8.
|     |     |     |     |     |     |     |     | to M /M | ∼10−4 | at  | z   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | •       | ⋆     |     |     |     |     |

15
• Host growth can dominate the evolution of the waveobservationswithLISAandTianQinwillprovidea
BH-to-galaxy mass ratio. In the PBH M1e7 dense complementaryprobeofPBHbinariesandtheirmerger
run, the BH grows only from 1.4×107 to 1.9× histories(e.g.,J.Luoetal.2016;P.Amaro-Seoaneetal.
107M between z = 8.4 and z = 4.1, while the 2017; E.-K. Li et al. 2025). Combined with spatially
⊙
associated stellar mass increases from 1.3×106 to resolved JWST follow-up, these measurements may dis-
9.9 × 107M . The corresponding M /M ratio tinguish faint offset seeds, compact BH-dominated sys-
|     |     | ⊙   |     |     |     | •   | ⋆   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
declines from ∼ 10 to ∼ 0.2. Later galaxy assem- tems, andmoreevolvedgalaxy–AGN configurations be-
blycanthereforegraduallyerasetheinitiallyover- foretheirseedinginformationislost(e.g.,M.Golubchik
massive nature of the seed even when BH growth et al. 2026; I. Juodˇzbalis et al. 2026).
is non-negligible. The system passes through a ACKNOWLEDGMENTS
compact,BH-dominatedstagethatisqualitatively
WeacknowledgefruitfuldiscussionswithPratikaDayal,
| LRD-like. |     | Its projected |     | stellar | half-mass |     | radius is |     |     |     |     |     |     |     |
| --------- | --- | ------------- | --- | ------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
SeijiFujimoto,andwithinMikeBoylan-Kolchin’sgroup.
| R   | ≃110pc | at  | z ≃8.4, | but | subsequently |     | grows |                                              |     |     |     |     |     |     |
| --- | ------ | --- | ------- | --- | ------------ | --- | ----- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 1/2 |        |     |         |     |              |     |       | TheauthorsacknowledgetheTexasAdvancedComput- |     |     |     |     |     |     |
to ∼300pc–1kpc as the host assembles. The sys- ing Center (TACC) for providing HPC resources under
| tem | therefore | leaves | the | LRD-like | phase | primarily |     |            |           |     |     |               |     |          |
| --- | --------- | ------ | --- | -------- | ----- | --------- | --- | ---------- | --------- | --- | --- | ------------- | --- | -------- |
|     |           |        |     |          |       |           |     | allocation | AST23026. | SZ  | and | JJ gratefully |     | acknowl- |
through rapid growth in stellar mass and spatial edge the funding from the university dissertation fel-
| extent. |     | More | strongly | overdense |     | realizations | in- |          |               |              |     |     |             |        |
| ------- | --- | ---- | -------- | --------- | --- | ------------ | --- | -------- | ------------- | ------------ | --- | --- | ----------- | ------ |
|         |     |      |          |           |     |              |     | lowship. | BL gratefully | acknowledges |     |     | the funding | of the |
stead form extended and clumpy hosts at earlier Royal Society University Research Fellowship and the
| times,            | showing |     | that the                   | compact | phase | is  | not uni- |                          |                        |             |                         |            |            |        |
| ----------------- | ------- | --- | -------------------------- | ------- | ----- | --- | -------- | ------------------------ | ---------------------- | ----------- | ----------------------- | ---------- | ---------- | ------ |
|                   |         |     |                            |         |       |     |          | Deutsche                 | Forschungsgemeinschaft |             |                         | (DFG,      | German     | Re-    |
| versal.           |         |     |                            |         |       |     |          | search Foundation)       |                        | under       | Germany’s               |            | Excellence | Strat- |
|                   |         |     |                            |         |       |     |          | egy EXC                  | 2181/1                 | - 390900948 | (the                    | Heidelberg |            | STRUC- |
|                   |         |     |                            |         |       |     |          | TURESExcellenceCluster). |                        |             | P.N.acknowledgessupport |            |            |        |
| • Thelighter,105M |         |     | seedsremainweaklyaccreting |         |       |     |          |                          |                        |             |                         |            |            |        |
⊙
and are generally galaxy dominated. Depending from the Gordon and Betty Moore Foundation and the
JohnTempletonFoundation,whichfundtheBlackHole
| on  | their | initial | placement, | they | appear | either | as  |     |     |     |     |     |     |     |
| --- | ----- | ------- | ---------- | ---- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
off-nuclear,weaklyfueledBHsorasembeddedbut Initiative(BHI)atHarvardUniversity,wheresheserves
|             |     |             |     |          |     |     |     | as a PI. | P.N. also | acknowledges      |     | support | from | STScI/- |
| ----------- | --- | ----------- | --- | -------- | --- | --- | --- | -------- | --------- | ----------------- | --- | ------- | ---- | ------- |
| radiatively |     | subdominant |     | sources. |     |     |     |          |           |                   |     |         |      |         |
|             |     |             |     |          |     |     |     | NASA via | grant     | JWST-GO-03293024. |     |         |      |         |
Future work should focus on identifying high-redshift AUTHOR CONTRIBUTIONS
PBH-seededsystemswhiletheirBHmassesremainrela-
SZisresponsibleforimplementingthenumericalanal-
tivelymodestandbeforecontinuedhostassemblyerases
ysisandwritingupthemanuscript;JJhasprovidedrel-
thesignaturesoftheirinitialconditionsanddrivesthem
|                    |                                       |          |                        |           |                  |                 |          | evant data      | for the   | DCBH                | simulations;  |         | BL and      | VB have |
| ------------------ | ------------------------------------- | -------- | ---------------------- | --------- | ---------------- | --------------- | -------- | --------------- | --------- | ------------------- | ------------- | ------- | ----------- | ------- |
| toward             | more conventional                     |          | galaxy–AGN             |           |                  | configurations. |          |                 |           |                     |               |         |             |         |
|                    |                                       |          |                        |           |                  |                 |          | helped with     | overall   | narratives,         |               | science | directions, | and     |
| Forward            | modeling                              | of       | their multi-wavelength |           |                  | and             | multi-   |                 |           |                     |               |         |             |         |
|                    |                                       |          |                        |           |                  |                 |          | critical edits; | PN        | has helped          | with          | science | pertaining  | to      |
| messenger          | signals                               | will     | be needed              | to        | connect          | the             | simu-    |                 |           |                     |               |         |             |         |
|                    |                                       |          |                        |           |                  |                 |          | PBH model       | and       | overall narratives. |               |         |             |         |
| lated evolutionary |                                       | pathways |                        | to future | surveys          |                 | (for re- |                 |           |                     |               |         |             |         |
| lated work,        | see,                                  | e.g.,    | A. De                  | Rosa      | et al.           | 2019;           | Y. Zhou  |                 |           |                     |               |         |             |         |
| etal.2026).        | Wide-fieldobservationswithRubinandRo- |          |                        |           |                  |                 |          |                 |           |                     |               |         |             |         |
| man can            | constrain                             | the      | abundance              |           | and environments |                 | of       |                 |           |                     |               |         |             |         |
|                    |                                       |          |                        |           |                  |                 |          | Facilities:     | Lonestar6 |                     | and Stampede3 |         | (TACC)      |         |
compactoroff-nuclearsources(e.g.,M.A.Latif&D.J.
Whalen2025),whileALMAcanprobetheircoldgasand Software: GIZMO (P. F. Hopkins 2015), astropy (
dust content (e.g., M. E. De Rossi & V. Bromm 2023). Astropy Collaboration et al. 2013, 2018, 2022), Colos-
Moreover,NewAthenaisexpectedtoconstrainobscured sus(B.Diemer2018),PHANTOM(S.Zhangetal.2025),
or weak BH accretion (e.g., K. Inayoshi et al. 2024; I. NumPy (C. R. Harris et al. 2020), SciPy (P. Virtanen
Labbeetal.2025;M.Cruiseetal.2025). Gravitational- etal.2020),Matplotlib(J.D.Hunter2007)
REFERENCES
Adamo, A., Atek, H., Bagley, M. B., et al. 2025, Nature Agarwal, B., Davis, A. J., Khochfar, S., Natarajan, P., &
| Astronomy, | 9,            | 1134, | doi: 10.1038/s41550-025-02624-5 |          |       |       |       |         |             |        |      |       |     |     |
| ---------- | ------------- | ----- | ------------------------------- | -------- | ----- | ----- | ----- | ------- | ----------- | ------ | ---- | ----- | --- | --- |
|            |               |       |                                 |          |       |       |       | Dunlop, | J. S. 2013, | MNRAS, | 432, | 3438, |     |     |
| Afshordi,  | N., McDonald, |       | P., &                           | Spergel, | D. N. | 2003, | ApJL, |         |             |        |      |       |     |     |
doi: 10.1093/mnras/stt696
| 594, L71, | doi: | 10.1086/378763 |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

16
Alexander, T., & Natarajan, P. 2014, Science, 345, 1330, Cho, H., Prather, C., Narayan, R., et al. 2026, ApJL, 1002,
doi: 10.1126/science.1251053 L43, doi: 10.3847/2041-8213/ae61ae
Amaro-Seoane, P., Audley, H., Babak, S., et al. 2017, arXiv Cruise, M., Guainazzi, M., Aird, J., et al. 2025, Nature
e-prints, arXiv:1702.00786, Astronomy, 9, 36, doi: 10.1038/s41550-024-02416-3
doi: 10.48550/arXiv.1702.00786 Dayal, P. 2024, A&A, 690, A182,
Angl´es-Alca´zar, D., Quataert, E., Hopkins, P. F., et al. doi: 10.1051/0004-6361/202451481
2021, ApJ, 917, 53, doi: 10.3847/1538-4357/ac09e8 Dayal, P. 2026, arXiv e-prints, arXiv:2604.20966,
Astropy Collaboration, Robitaille, T. P., Tollerud, E. J., doi: 10.48550/arXiv.2604.20966
|     |           |           |      |     |     |     | Dayal, P., | & Maiolino, | R.  | 2026, A&A, | 706, | A72, |     |
| --- | --------- | --------- | ---- | --- | --- | --- | ---------- | ----------- | --- | ---------- | ---- | ---- | --- |
| et  | al. 2013, | A&A, 558, | A33, |     |     |     |            |             |     |            |      |      |     |
doi: 10.1051/0004-6361/201322068 doi: 10.1051/0004-6361/202555959
AstropyCollaboration,Price-Whelan,A.M.,Sipo˝cz,B.M., de Graaff, A., Rix, H.-W., Naidu, R. P., et al. 2025, A&A,
|     |           |          |      |                               |     |     | 701, A168, | doi: | 10.1051/0004-6361/202554681 |     |     |     |     |
| --- | --------- | -------- | ---- | ----------------------------- | --- | --- | ---------- | ---- | --------------------------- | --- | --- | --- | --- |
| et  | al. 2018, | AJ, 156, | 123, | doi: 10.3847/1538-3881/aabc4f |     |     |            |      |                             |     |     |     |     |
Astropy Collaboration, Price-Whelan, A. M., Lim, P. L., De Luca, V., Del Grosso, L., Franciolini, G., et al. 2026,
|     |     |     |     |     |     |     | PhRvL, | 136, 231402, | doi: | 10.1103/6y1w-87pd |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | ---- | ----------------- | --- | --- | --- |
etal.2022,ApJ,935,167,doi:10.3847/1538-4357/ac7c74
|         |       |               |     |        |             |            | De Luca, | V., Franciolini, |     | G., & Riotto, | A.  | 2023, PhRvL, |     |
| ------- | ----- | ------------- | --- | ------ | ----------- | ---------- | -------- | ---------------- | --- | ------------- | --- | ------------ | --- |
| Baggen, | J. F. | W., Scoggins, |     | M. T., | van Dokkum, | P., et al. |          |                  |     |               |     |              |     |
2026, ApJL, 1002, L4, doi: 10.3847/2041-8213/ae58a5 130, 171401, doi: 10.1103/PhysRevLett.130.171401
|           |     |                |                                       |       |          |          | De Rosa, | A., Vignali, | C.,  | Bogdanovi´c,                | T., | et al. 2019, |     |
| --------- | --- | -------------- | ------------------------------------- | ----- | -------- | -------- | -------- | ------------ | ---- | --------------------------- | --- | ------------ | --- |
| Begelman, | M.  | C., Volonteri, |                                       | M., & | Rees, M. | J. 2006, |          |              |      |                             |     |              |     |
|           |     |                |                                       |       |          |          | NewAR,   | 86, 101525,  | doi: | 10.1016/j.newar.2020.101525 |     |              |     |
| MNRAS,    |     | 370, 289,      | doi: 10.1111/j.1365-2966.2006.10467.x |       |          |          |          |              |      |                             |     |              |     |
Behroozi, P. S., Wechsler, R. H., & Wu, H.-Y. 2013, ApJ, De Rossi, M. E., & Bromm, V. 2023, ApJL, 946, L20,
doi: 10.3847/2041-8213/acc32e
| 762,     | 109, | doi: 10.1088/0004-637X/762/2/109 |        |            |     |              |         |          |       |          |     |     |     |
| -------- | ---- | -------------------------------- | ------ | ---------- | --- | ------------ | ------- | -------- | ----- | -------- | --- | --- | --- |
|          | A´., |                                  |        |            |     |              | Diemer, | B. 2018, | ApJS, | 239, 35, |     |     |     |
| Bogda´n, |      | Goulding,                        | A. D., | Natarajan, | P., | et al. 2024, |         |          |       |          |     |     |     |
doi: 10.3847/1538-4365/aaee8c
| Nature | Astronomy, |     | 8, 126, |     |     |     |           |              |     |            |       |                |     |
| ------ | ---------- | --- | ------- | --- | --- | --- | --------- | ------------ | --- | ---------- | ----- | -------------- | --- |
|        |            |     |         |     |     |     | Escriva`, | A., Ku¨hnel, | F., | & Tada, Y. | 2024, | in Black Holes | in  |
doi: 10.1038/s41550-023-02111-9
|                 |     |          |        |            |     |         | the Era | of Gravitational-Wave |     | Astronomy, |          | ed. M. Arca |     |
| --------------- | --- | -------- | ------ | ---------- | --- | ------- | ------- | --------------------- | --- | ---------- | -------- | ----------- | --- |
| Boylan-Kolchin, |     | M. 2023, | Nature | Astronomy, |     | 7, 731, |         |                       |     |            |          |             |     |
|                 |     |          |        |            |     |         | Sedda,  | E. Bortolas,          | &   | M. Spera,  | 261–377, |             |     |
doi: 10.1038/s41550-023-01937-7
doi: 10.1016/B978-0-32-395636-9.00012-8
| Bromm, | V.,                 | Coppi, P. | S., & | Larson, | R. B. 2002, | ApJ, 564, |         |               |     |                            |        |           |     |
| ------ | ------------------- | --------- | ----- | ------- | ----------- | --------- | ------- | ------------- | --- | -------------------------- | ------ | --------- | --- |
|        |                     |           |       |         |             |           | Fabian, | A. C., Jiang, | J., | Baker, W.                  | M., et | al. 2026, |     |
| 23,    | doi: 10.1086/323947 |           |       |         |             |           |         |               |     |                            |        |           |     |
|        |                     |           |       |         |             |           | MNRAS,  | 547, stag379, |     | doi: 10.1093/mnras/stag379 |        |           |     |
Bromm,V.,Ferrara,A.,Coppi,P.S.,&Larson,R.B.2001,
|        |     |           |                                       |      |          |     | Faucher-Gigu`ere, |          | C.-A., | Lidz, A.,  | Zaldarriaga, | M., & |     |
| ------ | --- | --------- | ------------------------------------- | ---- | -------- | --- | ----------------- | -------- | ------ | ---------- | ------------ | ----- | --- |
| MNRAS, |     | 328, 969, | doi: 10.1046/j.1365-8711.2001.04915.x |      |          |     |                   |          |        |            |              |       |     |
|        |     |           |                                       |      |          |     | Hernquist,        | L. 2009, | ApJ,   | 703, 1416, |              |       |     |
| Bromm, | V., | & Loeb,   | A. 2003,                              | ApJ, | 596, 34, |     |                   |          |        |            |              |       |     |
doi: 10.1088/0004-637X/703/2/1416
doi: 10.1086/377529
|         |        |           |                             |     |        |              | Fei, Q.,     | Fujimoto,                | S., Naidu, | R. P.,           | et al. | 2026, ApJ, | 1003, |
| ------- | ------ | --------- | --------------------------- | --- | ------ | ------------ | ------------ | ------------------------ | ---------- | ---------------- | ------ | ---------- | ----- |
| Bunker, | A. J., | Saxena,   | A., Cameron,                |     | A. J., | et al. 2023, |              |                          |            |                  |        |            |       |
|         |        |           |                             |     |        |              | 244, doi:    | 10.3847/1538-4357/ae6248 |            |                  |        |            |       |
| A&A,    | 677,   | A88, doi: | 10.1051/0004-6361/202346159 |     |        |              |              |                          |            |                  |        |            |       |
|         |        |           |                             |     |        |              | Finkelstein, | S. L.,                   | Bagley,    | M. B., Ferguson, |        | H. C., et  | al.   |
Cappelluti, N., Hasinger, G., & Natarajan, P. 2022, ApJ, 2023, ApJL, 946, L13, doi: 10.3847/2041-8213/acade4
| 926,  | 205,        | doi: 10.3847/1538-4357/ac332d |     |     |                |          |            |          |          |        |     |      |     |
| ----- | ----------- | ----------------------------- | --- | --- | -------------- | -------- | ---------- | -------- | -------- | ------ | --- | ---- | --- |
|       |             |                               |     |     |                |          | Galli, D., | & Palla, | F. 2013, | ARA&A, | 51, | 163, |     |
| Carr, | B., Clesse, | S., Garc´ıa-Bellido,          |     |     | J., & Ku¨hnel, | F. 2021, |            |          |          |        |     |      |     |
doi: 10.1146/annurev-astro-082812-141029
Physics of the Dark Universe, 31, 100755, Golubchik, M., Furtak, L. J., Allingham, J. F. V., et al.
doi: 10.1016/j.dark.2020.100755
|     |     |     |     |     |     |     | 2026, | A&A, 710, | A226, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ----- | --- | --- | --- | --- |
Carr, B., & Ku¨hnel, F. 2020, Annual Review of Nuclear doi: 10.1051/0004-6361/202558407
| and | Particle | Science, | 70, | 355, |     |     |           |               |     |        |           |              |     |
| --- | -------- | -------- | --- | ---- | --- | --- | --------- | ------------- | --- | ------ | --------- | ------------ | --- |
|     |          |          |     |      |     |     | Greif, T. | H., Springel, | V., | White, | S. D. M., | et al. 2011, |     |
doi: 10.1146/annurev-nucl-050520-125911
|     |     |     |     |     |     |     | ApJ, | 737, 75, doi: | 10.1088/0004-637X/737/2/75 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | -------------------------- | --- | --- | --- | --- |
Carr, B., & Silk, J. 2018, MNRAS, 478, 3756, Gurian, J., Liu, B., Jeong, D., et al. 2026, arXiv e-prints,
doi: 10.1093/mnras/sty1204
|     |     |     |     |     |     |     | arXiv:2604.26006, |     | doi: | 10.48550/arXiv.2604.26006 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | ------------------------- | --- | --- | --- |
Casanueva-Villarreal, C., Tissera, P. B., Padilla, N., et al. Hahn, O., & Abel, T. 2011, MNRAS, 415, 2101,
| 2024, | A&A, | 688, A183, |     |     |     |     | doi: 10.1111/j.1365-2966.2011.18820.x |     |     |     |     |     |     |
| ----- | ---- | ---------- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
doi: 10.1051/0004-6361/202449650
|     |     |     |     |     |     |     | Harris, | C. R., Millman, | K.  | J., van | der Walt, | S. J., et | al. |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ------- | --------- | --------- | --- |
ChavezOrtiz,O.A.,Finkelstein,S.L.,Plat,A.,etal.2025, 2020, Nature, 585, 357, doi: 10.1038/s41586-020-2649-2
arXiv e-prints, arXiv:2511.03035, Hirano, S., & Bromm, V. 2017, MNRAS, 470, 898,
| doi: | 10.48550/arXiv.2511.03035 |     |     |     |     |     | doi: 10.1093/mnras/stx1220 |     |     |     |     |     |     |
| ---- | ------------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |

17
Hopkins, P. F. 2015, MNRAS, 450, 53, Kokorev, V., Caputi, K. I., Greene, J. E., et al. 2024, ApJ,
doi: 10.1093/mnras/stv195 968, 38, doi: 10.3847/1538-4357/ad4265
Hopkins, P. F., Grudic, M. Y., Su, K.-Y., et al. 2024, The Korber, D., Marques-Chaves, R., Schaerer, D., et al. 2026,
Open Journal of Astrophysics, 7, 18, arXiv e-prints, arXiv:2604.08687,
doi: 10.21105/astro.2309.13115 doi: 10.48550/arXiv.2604.08687
Hu, H., Inayoshi, K., Haiman, Z., Ho, L. C., & Ohsuga, K. Kormendy, J., & Ho, L. C. 2013, ARA&A, 51, 511,
2025, ApJL, 983, L37, doi: 10.3847/2041-8213/adc680 doi: 10.1146/annurev-astro-082708-101811
Huang, H.-L., Jiang, J.-Q., & Piao, Y.-S. 2024, Phys. Rev. Labb´e, I., van Dokkum, P., Nelson, E., et al. 2023, Nature,
D, 110, 103540, doi: 10.1103/PhysRevD.110.103540 616, 266, doi: 10.1038/s41586-023-05786-2
Huang, H.-L., Li, Y.-Y., Wang, Y.-T., & Piao, Y.-S. 2026, Labbe, I., Greene, J. E., Bezanson, R., et al. 2025, ApJ,
PhRvD, 113, 023519, doi: 10.1103/v34s-2lf9 978, 92, doi: 10.3847/1538-4357/ad3551
Hunter, J. D. 2007, Computing in Science and Engineering, Latif, M. A., & Whalen, D. J. 2025, ApJL, 990, L58,
9, 90, doi: 10.1109/MCSE.2007.55 doi: 10.3847/2041-8213/adfec6
Inayoshi, K., & Ichikawa, K. 2024, ApJL, 973, L49, Leung, G. C. K., Finkelstein, S. L., P´erez-Gonza´lez, P. G.,
doi: 10.3847/2041-8213/ad74e2 et al. 2025, ApJ, 992, 26, doi: 10.3847/1538-4357/adfcce
Inayoshi, K., Kashiyama, K., Li, W., et al. 2024, ApJ, 966, Li, E.-K., Liu, S., Torres-Orjuela, A., et al. 2025, Reports
164, doi: 10.3847/1538-4357/ad344c on Progress in Physics, 88, 056901,
Inayoshi, K., Shangguan, J., Chen, X., Ho, L. C., & doi: 10.1088/1361-6633/adc9be
Haiman, Z. 2026, ApJ, 1002, 25, Liu, B., & Bromm, V. 2020a, MNRAS, 495, 2475,
doi: 10.3847/1538-4357/ae548d doi: 10.1093/mnras/staa1362
Inayoshi, K., Visbal, E., & Haiman, Z. 2020, ARA&A, 58, Liu, B., & Bromm, V. 2020b, MNRAS, 497, 2839,
27, doi: 10.1146/annurev-astro-120419-014455 doi: 10.1093/mnras/staa2143
Ivey, L. R., D’Eugenio, F., Maiolino, R., et al. 2026, Liu, B., & Bromm, V. 2022, ApJL, 937, L30,
MNRAS, 550, stag1220, doi: 10.1093/mnras/stag1220 doi: 10.3847/2041-8213/ac927f
Jaacks, J., Finkelstein, S. L., & Bromm, V. 2019, MNRAS, Liu, B., & Bromm, V. 2025, in The Future of Primordial
488, 2202, doi: 10.1093/mnras/stz1529 Black Holes: Open Questions and Roadmap, ed.
Jaacks, J., Thompson, R., Finkelstein, S. L., & Bromm, V. C. Byrnes, 269–301, doi: 10.1007/978-981-97-8887-3 11
2018, MNRAS, 475, 4396, doi: 10.1093/mnras/sty062 Liu, B., Gurian, J., Inayoshi, K., et al. 2024, MNRAS, 534,
Jeon, J., Bromm, V., Liu, B., & Finkelstein, S. L. 2025a, 290, doi: 10.1093/mnras/stae2066
ApJ, 979, 127, doi: 10.3847/1538-4357/ad9f3a Liu, B., Meynet, G., & Bromm, V. 2021, MNRAS, 501,
Jeon, J., Bromm, V., Venditti, A., Finkelstein, S. L., & 643, doi: 10.1093/mnras/staa3671
Hsiao, T. Y.-Y. 2026a, ApJ, 1001, 3, Liu, B., Zhang, S., & Bromm, V. 2022, MNRAS, 514, 2376,
doi: 10.3847/1538-4357/ae517d doi: 10.1093/mnras/stac1472
Jeon, J., Jeong, T. B., Zhang, S., & Bromm, V. 2026b, Lodato, G., & Natarajan, P. 2006, MNRAS, 371, 1813,
ApJ, 1006, 27, doi: 10.3847/1538-4357/ae7bea doi: 10.1111/j.1365-2966.2006.10801.x
Jeon, J., Liu, B., Bromm, V., & Finkelstein, S. L. 2023, Luo, J., Chen, L.-S., Duan, H.-Z., et al. 2016, Classical and
MNRAS, 524, 176, doi: 10.1093/mnras/stad1877 Quantum Gravity, 33, 035010,
Jeon, J., Liu, B., Taylor, A. J., et al. 2025b, ApJ, 988, 110, doi: 10.1088/0264-9381/33/3/035010
doi: 10.3847/1538-4357/ade2e1 Ma, Y., Greene, J. E., Setton, D. J., et al. 2026, ApJ, 1000,
Jeon, J., Liu, B., Bromm, V., et al. 2026c, ApJ, 998, 148, 59, doi: 10.3847/1538-4357/ae4596
doi: 10.3847/1538-4357/ae3725 Mack, K. J., Ostriker, J. P., & Ricotti, M. 2007, ApJ, 665,
Johnson, J. L., & Bromm, V. 2006, MNRAS, 366, 247, 1277, doi: 10.1086/518998
doi: 10.1111/j.1365-2966.2005.09846.x Maiolino, R., Scholtz, J., Curtis-Lake, E., et al. 2024a,
Juodˇzbalis, I., Marconcini, C., D’Eugenio, F., et al. 2026, A&A, 691, A145, doi: 10.1051/0004-6361/202347640
Nature, 653, 1017, doi: 10.1038/s41586-026-10579-4 Maiolino, R., Scholtz, J., Witstok, J., et al. 2024b, Nature,
Kashlinsky,A.,Atrio-Barandela,F.,&Mart´ın-Gonza´lez,D. 627, 59, doi: 10.1038/s41586-024-07052-5
2026, MNRAS, 546, stag124, doi: 10.1093/mnras/stag124 Maiolino, R., U¨bler, H., Perna, M., et al. 2026a, arXiv
Kocevski, D. D., Finkelstein, S. L., Barro, G., et al. 2025, e-prints, arXiv:2603.20362,
ApJ, 986, 126, doi: 10.3847/1538-4357/adbc7d doi: 10.48550/arXiv.2603.20362

18
Maiolino, R., U¨bler, H., D’Eugenio, F., et al. 2026b, Springel, V., Di Matteo, T., & Hernquist, L. 2005,
MNRAS, 548, staf2109, doi: 10.1093/mnras/staf2109 MNRAS, 361, 776, doi: 10.1111/j.1365-2966.2005.09238.x
Martinez, Z., Berg, D. A., James, B. L., et al. 2025, ApJ, Springel, V., & Hernquist, L. 2003, MNRAS, 339, 289,
995, 204, doi: 10.3847/1538-4357/ae17c6 doi: 10.1046/j.1365-8711.2003.06206.x
Matteri, A., Ferrara, A., & Pallottini, A. 2025, A&A, 701, Stacy, A., & Bromm, V. 2013, MNRAS, 433, 1094,
A186, doi: 10.1051/0004-6361/202554728 doi: 10.1093/mnras/stt789
Matthee, J., Naidu, R. P., Brammer, G., et al. 2024, ApJ, STScI. 2026, JWST User Documentation (JDox): NIRCam
963, 129, doi: 10.3847/1538-4357/ad2345 Imaging,, https://stsci.edu
| Miao, D., | Li, G.-X., | &   | Sanhueza, | P.  | 2026, | arXiv e-prints, |     |            |          |     |            |     |              |       |
| --------- | ---------- | --- | --------- | --- | ----- | --------------- | --- | ---------- | -------- | --- | ---------- | --- | ------------ | ----- |
|           |            |     |           |     |       |                 |     | Su, K.-Y., | Ricarte, | A., | Natarajan, | P., | et al. 2026, | ApJL, |
arXiv:2607.17215, doi: 10.48550/arXiv.2607.17215 998, L18, doi: 10.3847/2041-8213/ae3724
Moreschini, B., Belfiore, F., Marconi, A., et al. 2026, arXiv Taylor, A. J., Kokorev, V., Kocevski, D. D., et al. 2025,
e-prints, arXiv:2601.08939, ApJL, 989, L7, doi: 10.3847/2041-8213/ade789
doi: 10.48550/arXiv.2601.08939 Tremmel, M., Karcher, M., Governato, F., et al. 2017,
|           |            |     |              |     |     |              |     | MNRAS, | 470, | 1121, doi: | 10.1093/mnras/stx1160 |     |     |     |
| --------- | ---------- | --- | ------------ | --- | --- | ------------ | --- | ------ | ---- | ---------- | --------------------- | --- | --- | --- |
| Naidu, R. | P., Oesch, | P.  | A., Brammer, |     | G., | et al. 2026, | The |        |      |            |                       |     |     |     |
Open Journal of Astrophysics, 9, 56033, U¨bler, H., Mazzolari, G., Maiolino, R., et al. 2026a, A&A,
doi: 10.33232/001c.156033 712, A80, doi: 10.1051/0004-6361/202557419
Napolitano, L., Castellano, M., Pentericci, L., et al. 2025, U¨bler,H.,Maiolino,R.,P´erez-Gonza´lez,P.G.,etal.2026b,
ApJ, 989, 75, doi: 10.3847/1538-4357/ade706 arXiv e-prints, arXiv:2603.20360,
doi: 10.48550/arXiv.2603.20360
| Natarajan, | P., | Pacucci, | F., Ferrara, |     | A., et | al. 2017, | ApJ, |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ------------ | --- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
838, 117, doi: 10.3847/1538-4357/aa6330 Vanzella, E., Loiacono, F., Bergamini, P., et al. 2023, A&A,
Natarajan, P., Pacucci, F., Ricarte, A., et al. 2024, ApJL, 678, A173, doi: 10.1051/0004-6361/202346981
|          |      |                          |     |     |     |     |     | Virtanen, | P., Gommers, |     | R., Oliphant, |     | T. E., | et al. 2020, |
| -------- | ---- | ------------------------ | --- | --- | --- | --- | --- | --------- | ------------ | --- | ------------- | --- | ------ | ------------ |
| 960, L1, | doi: | 10.3847/2041-8213/ad0e76 |     |     |     |     |     |           |              |     |               |     |        |              |
Nikopoulos, G. P., Watson, D., Pollock, C. L., et al. 2026, NatureMethods,17,261,doi:10.1038/s41592-019-0686-2
|       |           |                   |     |     |     |     |     | Visbal, E., | Haiman, | Z., | & Bryan, | G.  | L. 2014, | MNRAS, 445, |
| ----- | --------- | ----------------- | --- | --- | --- | --- | --- | ----------- | ------- | --- | -------- | --- | -------- | ----------- |
| arXiv | e-prints, | arXiv:2606.31515, |     |     |     |     |     |             |         |     |          |     |          |             |
doi: 10.48550/arXiv.2606.31515 1056, doi: 10.1093/mnras/stu1794
Planck Collaboration, Aghanim, N., Akrami, Y., et al. Wang, Z., Jiang, F., Zheng, H., et al. 2026, arXiv e-prints,
|       |      |          |                                  |     |     |     |     | arXiv:2603.15736, |     | doi: | 10.48550/arXiv.2603.15736 |     |     |     |
| ----- | ---- | -------- | -------------------------------- | --- | --- | --- | --- | ----------------- | --- | ---- | ------------------------- | --- | --- | --- |
| 2020, | A&A, | 641, A6, | doi: 10.1051/0004-6361/201833910 |     |     |     |     |                   |     |      |                           |     |     |     |
Qin, W., Kumar, S., Natarajan, P., & Weiner, N. 2025, Zhang, S., Bromm, V., & Liu, B. 2024a, ApJ, 975, 139,
doi: 10.3847/1538-4357/ad7b0d
| arXiv | e-prints, | arXiv:2506.13858, |     |     |     |     |     |            |      |              |     |           |        |           |
| ----- | --------- | ----------------- | --- | --- | --- | --- | --- | ---------- | ---- | ------------ | --- | --------- | ------ | --------- |
|       |           |                   |     |     |     |     |     | Zhang, S., | Liu, | B., & Bromm, |     | V. 2024b, | MNRAS, | 528, 180, |
doi: 10.48550/arXiv.2506.13858
Ricotti, M. 2007, ApJ, 662, 53, doi: 10.1086/516562 doi: 10.1093/mnras/stad3986
|          |               |     |       |       |       |            |      | Zhang, S., | Liu, | B., & Bromm, |     | V. 2025, | PHANTOM: |     |
| -------- | ------------- | --- | ----- | ----- | ----- | ---------- | ---- | ---------- | ---- | ------------ | --- | -------- | -------- | --- |
| Ricotti, | M., Ostriker, | J.  | P., & | Mack, | K. J. | 2008, ApJ, | 680, |            |      |              |     |          |          |     |
829, doi: 10.1086/587831 Primordial black Holes And Nonlinear perTurbations fOr
|           |                          |        |     |        |           |      |       | siMulations, | Zenodo, |              | doi: 10.5281/zenodo.17025634 |           |      |           |
| --------- | ------------------------ | ------ | --- | ------ | --------- | ---- | ----- | ------------ | ------- | ------------ | ---------------------------- | --------- | ---- | --------- |
| Rinaldi,  | P., Rieke,               | G. H., | Wu, | Z., et | al. 2026, | ApJ, | 1006, |              |         |              |                              |           |      |           |
|           |                          |        |     |        |           |      |       | Zhang, S.,   | Liu,    | B., & Bromm, |                              | V. 2025b, | ApJ, | 992, 136, |
| 205, doi: | 10.3847/1538-4357/ae80cd |        |     |        |           |      |       |              |         |              |                              |           |      |           |
doi: 10.3847/1538-4357/ae061c
| Rusta, E., | Salvadori, | S.,                      | Maiolino, | R., | et al. | 2026, | ApJL, |            |      |            |     |        |             |           |
| ---------- | ---------- | ------------------------ | --------- | --- | ------ | ----- | ----- | ---------- | ---- | ---------- | --- | ------ | ----------- | --------- |
|            |            |                          |           |     |        |       |       | Zhang, S., | Liu, | B., Bromm, | V., | et al. | 2025a, ApJ, | 987, 185, |
| 1003,      | L14, doi:  | 10.3847/2041-8213/ae64e1 |           |     |        |       |       |            |      |            |     |        |             |           |
doi: 10.3847/1538-4357/adddb4
Safranek-Shrader,C.,Bromm,V.,&Milosavljevi´c,M.2010,
|            |                                  |      |                              |              |        |            |      | Zhang, S.,      | Liu,      | B., Bromm,               | V.,    | & Ku¨hnel, | F.     | 2026, ApJL, |
| ---------- | -------------------------------- | ---- | ---------------------------- | ------------ | ------ | ---------- | ---- | --------------- | --------- | ------------------------ | ------ | ---------- | ------ | ----------- |
| ApJ,       | 723, 1568,                       | doi: | 10.1088/0004-637X/723/2/1568 |              |        |            |      |                 |           |                          |        |            |        |             |
|            |                                  |      |                              |              |        |            |      | 1000, L19,      | doi:      | 10.3847/2041-8213/ae4bd0 |        |            |        |             |
| Scholtz,   | J., Witten,                      | C.,  | Laporte,                     | N.,          | et al. | 2024, A&A, | 687, |                 |           |                          |        |            |        |             |
|            |                                  |      |                              |              |        |            |      | Zhou, Y.,       | Bhowmick, | A.                       | K., Di | Matteo,    | T., et | al. 2026,   |
| A283,      | doi: 10.1051/0004-6361/202347187 |      |                              |              |        |            |      |                 |           |                          |        |            |        |             |
|            |                                  |      |                              |              |        |            |      | arXiv e-prints, |           | arXiv:2604.01123,        |        |            |        |             |
| Smith, A., | & Bromm,                         |      | V. 2019,                     | Contemporary |        | Physics,   | 60,  |                 |           |                          |        |            |        |             |
doi: 10.48550/arXiv.2604.01123
| 111, doi: | 10.1080/00107514.2019.1615715 |        |      |       |     |     |     |             |            |            |                        |     |         |          |
| --------- | ----------------------------- | ------ | ---- | ----- | --- | --- | --- | ----------- | ---------- | ---------- | ---------------------- | --- | ------- | -------- |
|           |                               |        |      |       |     |     |     | Ziparo, F., | Gallerani, | S.,        | Ferrara,               | A., | & Vito, | F. 2022, |
| Springel, | V. 2005,                      | MNRAS, | 364, | 1105, |     |     |     |             |            |            |                        |     |         |          |
|           |                               |        |      |       |     |     |     | MNRAS,      | 517,       | 1086, doi: | 10.1093/mnras/stac2705 |     |         |          |
doi: 10.1111/j.1365-2966.2005.09655.x
---- END DOCUMENT ----
