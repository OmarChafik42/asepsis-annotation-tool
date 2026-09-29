Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Amphibian water to land transition reveals physical limits of olfaction
Martin James,1,∗ Loranzie S. Rogers,2 Moreira Salsman,2
Francesco Viola,3,4 Nicholas W. Bellono,2 and Agnese Seminara1,†
1Machine Learning Genoa Center (MaLGa) & Department of Civil,
Chemical and Environmental Engineering, University of Genoa, 16145 Genoa, Italy
2Department of Molecular and Cellular Biology, Harvard University, Cambridge, MA 02138, USA
3Gran Sasso Science Institute (GSSI), L’Aquila 67100, Italy
4INFN–Laboratori Nazionali del Gran Sasso, Assergi, Italy
(Dated: August 21, 2026)
The evolutionary transition from water to land required animals to sense and respond to dras-
tically different environments. Chemicals diffuse four orders of magnitude more slowly in water
than in air, requiring significant remodeling of the olfactory system. Amphibians provide a power-
ful model to analyze these adaptations because they transition from an aquatic to terrestrial state
duringasinglelifetimefollowingmetamorphosis. Hereweexploitlaboratory-inducedmetamorpho-
sis of adult Ambystoma mexicanum to ask how fundamental chemical properties impact aquatic
versus terrestrial olfaction. By combining asymptotic theory with numerical simulations using re-
constructedolfactorychambermorphologies,wefindthattheodoradsorptiontakestensofseconds
in water compared to milliseconds in air. Adsorption of an ephemeral odor whiff is maximized
at an inhalation speed of ∼20cms−1 in air vs near zero in water, matching our measurements of
negligible aquatic inhalation. Nevertheless, aquatic axolotls quickly respond to introduced odorant
molecules. While morphological differences in the olfactory chamber of aquatic versus terrestrial
axolotls are nearly irrelevant, aquatic olfactory cilia may pump water to significantly speed up the
rate of odor adsorption. Together with adaptive behavioral responses that reduce proximity to the
target,thewaittimecanreducetolessthanonesecond. Thus,whileaquaticolfactionisslowerthan
terrestrial olfaction, aquatic animals exhibit anatomical and behavioral adaptations that support
chemical detection as a proximal sense.
I. INTRODUCTION ular diffusivities are closer to 10−5cm2s−1 [8], while the
kinematic viscosity is of order 10−2cm2s−1. The cor-
Olfactionplaysacriticalroleinhowanimalsextractin- responding Schmidt number is of order 103. Such slow
formationfromcomplexenvironments. Itallowsanimals diffusivitymeansthatwaterborneodorswilltravelmuch
to find food, identify mates, avoid predators and orient faster along the chamber than across it, and depending
withinodorlandscapes[1–5]. Thesenseofsmellrelieson onhowquicktheflowisinthechamber,theycouldeasily
odorantmoleculesbindingtoreceptorsexpressedbysen- exit before reaching the boundary.
soryneuronswithintheolfactorychamberandtriggering How many molecules reach the epithelium before ex-
acascadeofmolecularprocessesthateventuallyfacilitate iting the chamber, and how quickly do they get there?
sensation[6]. Beforethisbiochemicalrecognitioncanoc- Answering this requires knowing the chamber geometry
cur,themoleculemusttravelwithinthefluid-filledolfac- and the flow within it. Qualitatively, in the absence of
tory chamber and reach the sensory epithelium. Physics chaoticeffectsorturbulence,theflowwithintheolfactory
thus shapes this first step: odor molecules must reach chamberrunslargelyparalleltothewallsandtransports
the receptor-bearing surface before they are carried out odor molecules along the chamber, without delivering
of the chamber. odor to the epithelium. To reach the epithelium, odor
This physical process is much slower in water than in must diffuse laterally across the chamber before it exits,
air. Small odorant molecules diffuse readily across air- a process that takes a time of order R2/D for a cham-
filled chambers to reach the epithelium located at its ber of width R. Diffusivity thus controls both how many
boundary. The nondimensional parameter representing odorant molecules the organism can sense and how fast
how quickly the chemical molecules diffuse compared to sensation can begin.
fluid molecules is called the Schmidt number, Sc=ν/D.
Aquatic vertebrates routinely detect dissolved cues,
Sc represents the ratio of momentum diffusivity (ν) to
yet diffusion alone is too slow to carry molecules across
molecular diffusivity (D): in air small molecules have
diffusivities of order D ∼10−1cm2s−1 [7], matching the a millimeter-scale chamber within a typical passage
time [9]. In large organisms that drive flows at high
kinematic viscosity of air, thus Sc is of order unity. In
Reynolds numbers (Re), turbulent mixing inside the ol-
contrast,diffusioninwaterisdramaticallyslower: molec-
factory chamber could provide an answer. Organisms
that cannot generate turbulence, however, must rely on
some additional mechanism to enhance adsorption if ol-
∗ martin.james@edu.unige.it faction is to remain effective in water [10]. What are the
† agnese.seminara@unige.it mechanismsthatenableaquaticolfactioninsmallorgan-
6202
guA
12
]hp-oib.scisyhp[
1v56702.8062:viXra

2
| a   |     |     |     |     |     | b   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| c   |     |     |     | d   |     |     |     |     |     |     |     |     |     |
e
1.0
|     |     |     |     | 1.0 |     |     |     |     | 0.9 |     |        |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
| c=c |     |     |     | 0   |     |     |     |     | 0.6 |     | Sc = 1 | 0.8 |     |
|     | 0   |     |     | 0.8 |     |     |     |     |     |     |        |     |     |
/
|     |     |     |     |  etats ydaets |     |     |     |     | 0.3 |     |          |     |     |
| --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
|     |     |     |     | 0.6           |     |     |     |     |     |     | / 0=1.00 | 0.6 |     |
0
|     |     |     | wall: c=0 |     |     |     |     |     | R/r |     |     |     | c/c |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |           | 0.4 |     |     |     |     |     |     |     | 0.4 |     |
r
|     |     | u(r) |     |     |          |     |     |     | 0.6 |     | Sc = 200 |     |     |
| --- | --- | ---- | --- | --- | -------- | --- | --- | --- | --- | --- | -------- | --- | --- |
| c=c | 0   |      |     |     | Re = 0.1 |     |     |     |     |     |          |     |     |
|     |     |      | z   | 0.2 |          |     |     |     |     |     |          | 0.2 |     |
|     |     |      |     |     | Re = 2.1 |     |     |     | 0.3 |     |          |     |     |
|     |     |      |     |     | Re = 10  |     |     |     |     |     | / 0=0.25 |     |     |
|     |     |      |     | 0.0 |          |     |     |     | 0.0 |     |          | 0.0 |     |
|     |     |      |     | 100 | 101      |     | 102 | 103 | 0.0 | 2.5 | 5.0 7.5  |     |     |
|     |     |      |     |     |          | Sc  |     |     |     | z/R |          |     |     |
FIG. 1. Odorant molecules are adsorbed much more efficiently in air (low Schmidt number (Sc)) than in water (high Sc).
(a) Aquatic and (b) terrestrial axolotls together with their olfactory chamber morphologies reconstructed from computed
tomographyscans. (c)Binarymaskoftheaquaticolfactorychamberusedtodefinetheapproximatecylindricalgeometryand
a schematic of the cylindrical model with a constant odor source fixing the concentration to c at the entrance. The wall is
0
perfectly absorbing and the axial velocity follows a Poiseuille profile u(r). (d) Steady-state adsorption efficiency ϕ/ϕ 0 as a
function of Sc, obtained by solving Eq. (A11) for three different Reynolds numbers (Re). Note that since Péclet (Pe) is the
relevant nondimensional number here, the solutions for all Re are related by rescaling Sc. (e) Odor fields in the cylinder at
Sc = 1 and 200 for Re = 2.1. At low Sc, odor is depleted near the inlet and nearly all incoming molecules are adsorbed. At
| high Sc, | the concentration |     | remains | high in the | flow core and | adsorption | decreases. |     |     |     |     |     |     |
| -------- | ----------------- | --- | ------- | ----------- | ------------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
isms, given that diffusion in water is so slow? also show that odor adsorption is fast relative to the in-
The axolotl Ambystoma mexicanum (Fig. 1a,b) is an halation timescales. Importantly, despite all of these in-
ideal system to ask how small organisms efficiently de- efficiencies, we find that aquatic axolotls do respond to
tect odor in water. Under induced metamorphosis, its odorant molecules pipetted in water.
olfactory chamber transforms from one adapted for an How, then, can aquatic olfaction function at all? Ac-
aquatic environment to one adapted for a terrestrial tive fluid pumping may provide one answer. Motivated
environment, making it possible to compare water-like by the motile cilia lining the olfactory chambers of fishes
and air-like transport within related anatomical designs and amphibians [13, 14], we show that the radial fluid
(Fig. 1a,b) [11, 12]. Did axolotls before metamorphosis transport driven by metachronal ciliary waves enhances
evolve mechanisms to speed up odorant adsorption? adsorption, reducing the odor detection time sensibly.
|     |     |     |     |     |     | Using | realistic | morphologies |     | from | computed | tomogra- |     |
| --- | --- | --- | --- | --- | --- | ----- | --------- | ------------ | --- | ---- | -------- | -------- | --- |
Toanswerthisquestion,weanalyzethefluiddynamics
of odorant adsorption in axolotl olfactory chambers. We phy scans of axolotls before and after metamorphosis,
firstdevelopacylindricalmodelshowingthatadsorption we show that the two chambers concentrate adsorption
|          |             |           |      |             |               | in  | distinct | regions of | the epithelium. |     | However, | odor | ad- |
| -------- | ----------- | --------- | ---- | ----------- | ------------- | --- | -------- | ---------- | --------------- | --- | -------- | ---- | --- |
| in water | is far less | efficient | than | in air. For | instance, de- |     |          |            |                 |     |          |      |     |
tecting 10% of the odor in a pulse would take over 20s sorption in the aquatic chamber remains fundamentally
in water, whereas the same process is about 104 times inefficient. Finally,wenotethataquaticaxolotlsmayuse
faster in air. This dramatic loss of efficiency in water is olfaction as a proximal sense, so that the abundance of
robust and independent of whether the odor is emitted odorant molecules would partly mitigate the inefficiency
steadilyrightoutsidetheolfactorychamberorwhetherit of adsorption in water. However, we show that even in
is emitted from a distal target and reaches the olfactory this case, sensation may remain rather slow, as detec-
|         |              |     |         |              |          | tion | time falls | only | logarithmically |     | with concentration. |     |     |
| ------- | ------------ | --- | ------- | ------------ | -------- | ---- | ---------- | ---- | --------------- | --- | ------------------- | --- | --- |
| chamber | in ephemeral |     | whiffs. | We show that | an opti- |      |            |      |                 |     |                     |     |     |
104
mal inhalation speed exists for odor whiffs in both air For example, a fold increase in odorant availability
and water. The optimal speed in air is in the range of speeds detection by about four times.
20cms−1 whereas in water it is close to zero. Consis- Our results show that specific adaptations are needed
tently, we find no respiration in aquatic animals. We to speed up odor adsorption in water and suggest that

3
these fundamental inefficiencies may shape chemically- half of the odor diffuses into the cylinder while the rest
driven behavior in aquatic organisms. diffusesoutside. Becausetheflowvanishes,forlongcylin-
|     |     |     |     |     |     |     |     | ders     | with length | L ≫   | R,  | upon waiting | long   | enough | all     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ----- | --- | ------------ | ------ | ------ | ------- |
|     |     |     |     |     |     |     |     | of those | molecules   | reach | the | epithelium   | giving | us     | a base- |
II. RESULTS line of 50% long-time adsorption efficiency (Fig. 2a). As
|     |     |     |     |     |     |     |     | the flow | rate | increases, | the | odor | gets transported |     | into |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---------- | --- | ---- | ---------------- | --- | ---- |
We begin with a minimal model that captures odor the cylinder, thus reducing the diffusive loss outside the
|           |             |     |          |           |                 |     |          | cylinder. | Furthermore,theincreaseddiffusiontothewall |            |      |       |            |     |          |
| --------- | ----------- | --- | -------- | --------- | --------------- | --- | -------- | --------- | ------------------------------------------ | ---------- | ---- | ----- | ---------- | --- | -------- |
| transport | inside      | the | aquatic  | olfactory | chamber         |     | as flow  |           |                                            |            |      |       |            |     |          |
|           |             |     |          |           |                 |     |          | reduces   | the                                        | adsorption | time | (Fig. | 2b). While | in  | air, ad- |
| through   | a cylinder. |     | It keeps | the       | two ingredients |     | that di- |           |                                            |            |      |       |            |     |          |
sorptionhappensonthetimescaleofmilliseconds,inwa-
| rectlycontrolwallcapture: |     |     |     | advectionalongthechamber |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anddiffusiontowardtheodoradsorbingepithelium. The ter the process remains too slow even for an odor pulse
|                                             |     |         |         |         |          |         |     | (Fig.          | 2b). |       |        |     |         |      |          |
| ------------------------------------------- | --- | ------- | ------- | ------- | -------- | ------- | --- | -------------- | ---- | ----- | ------ | --- | ------- | ---- | -------- |
| reconstructed                               |     | aquatic | chamber | outline | is first | reduced | to  |                |      |       |        |     |         |      |          |
|                                             |     |         |         |         |          |         |     | Interestingly, |      | there | exists | an  | optimal | flow | rate, or |
| achannelofcomparablelengthandwidth(Fig.1c). |     |         |         |         |          |         | The |                |      |       |        |     |         |      |          |
resultingmodelisnotintendedtoreproducethedetailed Re in the nondimensional form, that maximizes adsorp-
|             |               |         |            |              |       |          |        | tion   | (Figs. 2c | and S6).    | Since        | Pe   | = ReSc, | the          | optimal |
| ----------- | ------------- | ------- | ---------- | ------------ | ----- | -------- | ------ | ------ | --------- | ----------- | ------------ | ---- | ------- | ------------ | ------- |
| geometry,   | butto         | provide | areference |              | curve | against  | which  |        |           |             |              |      |         |              |         |
|             |               |         |            |              |       |          |        | Re =   | Re        | will change | such         | that | ReSc    | remains      | a con-  |
| the full    | simulations   |         | can be     | compared.    |       | Details  | of the |        | opt       |             |              |      |         |              |         |
|             |               |         |            |              |       |          |        | stant. | The       | value of    | this optimal |      | Re can  | be motivated |         |
| cylindrical | approximation |         |            | are provided | in    | Appendix | A.     |        |           |             |              |      |         |              |         |
The nondimensionalized equation shows that the nor- from the following calculation. For an odor pulse ad-
vectedthroughthecylinder,walladsorptioniscontrolled
| malized            | odor | field is | a function                 |     | of the | Péclet | number |           |           |         |     |                        |     |     |     |
| ------------------ | ---- | -------- | -------------------------- | --- | ------ | ------ | ------ | --------- | --------- | ------- | --- | ---------------------- | --- | --- | --- |
|                    |      |          |                            |     |        |        |        | by radial | diffusion | towards |     | the adsorbingboundary. |     |     | The |
| Pe=ReSc(Eq.(A11)). |      |          | BecauseReandScaresetbydif- |     |        |        |        |           |           |         |     |                        |     |     |     |
ferent physical factors, the animal’s inhalation flow and relevantexposuretimeistheresidencetimeofthepatch,
|     |     |     |     |     |     |     |     | afterwhichadvectioncarriesitoutofthedomain. |     |     |     |     |     |     | Thus, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
themedium,respectively,wereportthemseparatelyeven
maximumadsorptionisexpectedwhentheadvectiveres-
| though | the model | depends |     | only | on their product. |     |     |     |     |     |     |     |     |     |     |
| ------ | --------- | ------- | --- | ---- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We first fix the inlet odor concentration to a con- idencetimeandtheradialdiffusiontimearecomparable,
| stantvalue,mimickinganearbylarge,staticodorsource. |     |     |     |     |     |     |     |     |     |     |     | R2  |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L
With this boundary condition, the adsorption efficiency ≈ . (1)
|             |           |         |               |               |              |          |         |      |            |         | U   | D   |     |     |     |
| ----------- | --------- | ------- | ------------- | ------------- | ------------ | -------- | ------- | ---- | ---------- | ------- | --- | --- | --- | --- | --- |
| (Eq. (A13)) | decreases |         | monotonically |               | with         | Sc at    | all Re  |      |            |         |     |     |     |     |     |
| (Fig. 1d).  | At        | Sc = 1, | the           | concentration | is           | depleted | over    |      |            |         |     |     |     |     |     |
|             |           |         |               |               |              |          |         | This | yields the | scaling |     |     |     |     |     |
| a short     | entrance  | region  | and           | almost        | all incoming |          | odorant |      |            |         |     |     |     |     |     |
is adsorbed (Fig. 1e top). At larger Sc, radial diffusion 1 L
|                                                |     |     |     |     |     |     |     |     |     |     | Re  | ≈   | .   |     | (2) |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| becomestooslowtocarrytheodorantfromthecenterof |     |     |     |     |     |     |     |     |     |     | opt |     |     |     |     |
ScR
| the channel   | to  | the wall | within | the     | residence | time. | The      |             |     |              |      |          |       |     |      |
| ------------- | --- | -------- | ------ | ------- | --------- | ----- | -------- | ----------- | --- | ------------ | ---- | -------- | ----- | --- | ---- |
|               |     |          |        |         |           |       |          | In Appendix |     | B, we refine | this | argument | using | the | mean |
| concentration |     | boundary | layer  | becomes | thinner,  |       | a larger |             |     |              |      |          |       |     |      |
fraction of the odor field remains in the core of the flow absorption location and obtain the corrected estimate
| and the | outlet | flux increases |     | (Fig. | 1e bottom). | These | re- |     |     |     |     |     |     |     |     |
| ------- | ------ | -------------- | --- | ----- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8L 1
sults clarify why aquatic odor transport is difficult. Un- Re ≈ . (3)
|          |         |           |     |           |      |             |     |     |     |     | opt | 3RSc |     |     |     |
| -------- | ------- | --------- | --- | --------- | ---- | ----------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
| less the | chamber | increases |     | residence | time | or enhances |     |     |     |     |     |      |     |     |     |
cross-streamtransport,mostoftheincomingodorantre-
|     |     |     |     |     |     |     |     | Over | the long | timescales |     | relevant | to water, | the | instan- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ---------- | --- | -------- | --------- | --- | ------- |
mainsintheflowingcoreandleaveswithoutreachingthe taneous flux into the epithelium may be a better proxy
| wall. |            |            |     |      |           |      |        | for detection |         | than    | the cumulative |     | adsorbed |        | amount, |
| ----- | ---------- | ---------- | --- | ---- | --------- | ---- | ------ | ------------- | ------- | ------- | -------------- | --- | -------- | ------ | ------- |
| The   | adsorption | efficiency |     | also | decreases | with | Re, as |               |         |         |                |     |          |        |         |
|       |            |            |     |      |           |      |        | since         | sensory | neurons | adapt          | and | respond  | to the | rate at |
expected, since efficiency only depends on Re and Sc which odorant arrives rather than to an indefinitely ac-
through Pe (Figs. 1d and S5a). However, a higher flow cumulated dose. We therefore evaluate the flux dN/dt
| rate can | deliver | a larger |     | flux into | the chamber, |     | which |       |          |          |         |     |             |            |     |
| -------- | ------- | -------- | --- | --------- | ------------ | --- | ----- | ----- | -------- | -------- | ------- | --- | ----------- | ---------- | --- |
|          |         |          |     |           |              |     |       | (Fig. | S7). Its | behavior | mirrors |     | that of the | cumulative |     |
can compensate for the decreased efficiency. In fact, the adsorption. The peak flux is maximized at an interme-
total amount of odor adsorbed grows with flow speed diate Re, while the time to reach it decreases with Re
(Fig. S5b). Thus, faster inhalation lowers efficiency but before saturating (Fig. S7b,c).
| increases | the total | amount |     | of odor | adsorbed. | The | high |     |     |     |     |     |     |     |     |
| --------- | --------- | ------ | --- | ------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Beforeincorporatingthefullmorphologyoftheaxolotl
Pe limit makes this explicit, with the adsorbed flux scal- olfactory chamber, we ask whether an active mechanism
ing with Re3 1 (Eq. (S7)). However, this does not solve canovercometheslowadsorptioninwater. Theolfactory
the problem of slow adsorption in water (Fig. S5). chambersofseveralfishesandamphibiansarelinedwith
So far we have assumed a constant odor value at the motile cilia [13–16], and in zebrafish larvae these cilia
entrance of the olfactory chamber. Often odor released have been shown to draw odorant toward the sensory
fromdistalolfactorytargetstravelsacrossrandomlyfluc- epithelium [13, 15]. To test whether such cilia can solve
tuating flows and reaches the nose in random ephemeral theslowadsorptioninwater,welinetheinnerwallofthe
whiffs. To mimic this condition, we consider an instan- cylinder with cilia whose tips trace a circle of radius εR,
taneous minute odor whiff located at the center of the with ε = 0.01, beating metachronally with wavelength
inlet. For Re = 0, the process is purely diffusive and λ and frequency f. We fix f = 25Hz, consistent with

4
| a   |     |     |     |     |     |     |     | b   |     |     | c   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
time in water (s; Sc=1000) water flow velocity (mm/s) water flow velocity (mm/s)
)sm( ria ni 1.0=0
|     |     | 0 100 | 200 | 300 | 400 | 500 | 600 |     | 0 0.1 | 0.2 |     | 0 0.1 | 0.2 |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- |
1.0
|     |     |     |     |     |     |     |     |     | 3.0 N/N 0=0.1 | 30  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
0.8
|     | 0.8 |     |     |     |     |     |     |     |     |     | )s( emit retaw |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
Reair=30,Rewater=0.03
|     |     |     |     |     |     |     |     |     | 2.8 | 28  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     | N/N 0 0.6 | Re=0 limit |     |     |     |     |     |     |     |     | N/  | 0.6 |     |
| --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |           |            |     |     |     |     |     |     | 2.6 | 26  |     |     |     |
|     | 0.4       |            |     |     |     |     |     |     |     |     | N   |     |     |
N/N ot emit
0.4
|     | 0.2 |     |     |     |     |     |     |     | 2.4 | 24  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Reair=100,Rewater=0.1
|     | 0.0  |      |      |      |      |      |      |     | 2.2   | 22  |     | 0.2   |     |
| --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | ----- | --- | --- | ----- | --- |
|     | 0.00 | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 | 0.06 |     | 0 100 | 200 |     | 0 100 | 200 |
time in air (s; Sc=1) air flow velocity (cm/s) air flow velocity (cm/s)
FIG.2. Forintermittentodorsources,theadsorptioninwatercanreachover80%ofthetotalodor,butrequiresalongwaiting
time. (a) Fraction of odor molecules adsorbed from an instantaneous odor pulse at the inlet for different Re as a function of
time. (b)TimetoreachN/N 0 =0.1ofthetotalodorasafunctionofflowvelocitiesinairandwater. Evenattheoptimalflow
velocity,thetimetoreachN/N 0 =0.1exceeds20sinwater. (c)AsymptoticadsorptionefficiencyN ∞ /N 0 asafunctionofflow
velocities, with the lower axis giving flow velocity in air (Sc=1) and the upper axis flow velocity in water (Sc=1000). Note
thatinthenondimensionalizedform,thereexistsanoptimalRethatmaximizesadsorption(seealsoFig.S6intheSupporting
Information).
observations in the olfactory pit of zebrafish larvae [13] fraction of the odor travels in water along the chamber
and vary the wavelength λ in the range 0.1 ≤ λ ≤ 5. without reaching the wall (Fig. 4a). Note that due to
R
Details of the model are given in Appendix C. computationalconstraintswelimitourfullsimulationto
The ciliary motion produces a maximum radial veloc- Sc=100 although in water, typical Sc values for volatile
ity 2πεRf at the wall, and the resulting flow has a pene- compoundsexceed1000. Incontrasttotheaquaticprob-
tration depth δ set by the beat wavelength, δ = λ/2π lem, the terrestrial chamber in air strongly depletes the
|      |        |     |           |     |             |     |             |     | odorfieldalongthepassage(Fig.4b). |     |     | Butdothesediffer- |     |
| ---- | ------ | --- | --------- | --- | ----------- | --- | ----------- | --- | --------------------------------- | --- | --- | ----------------- | --- |
| (Eq. | (C4)). | As  | expected, |     | this motion |     | drives flow | to- |                                   |     |     |                   |     |
ward the epithelium (Fig. 3a). To quantify its effect, encesdependonthetwodistinctmorphologies,orrather
we evaluate the adsorption efficiency in a chamber with on the fluid environment (i.e. air vs water)?
cilia-generated flow (Fig. 3b). Ciliary beating substan- Infact, theexactmorphologyofthechamberdoesnot
tially increases odor adsorption, and the efficiency grows affect how much or how fast odor is adsorbed. Indeed,
with λ. The cilia also speed up capture, reducing the the full simulations with constant odor inflow, with the
| adsorption |     | time | by about | a   | factor | that | depends | on the |                       |     |              |                |     |
| ---------- | --- | ---- | -------- | --- | ------ | ---- | ------- | ------ | --------------------- | --- | ------------ | -------------- | --- |
|            |     |      |          |     |        |      |         |        | detailed morphologies | of  | the chambers | follow closely | the |
wavelength λ (Fig. 3c). Ciliary pumping can also sub- cylindrical prediction, across the range of Schmidt num-
stantially increase the instantaneous odor flux into the bers that can be resolved directly (Fig. 4e). Both con-
epithelium (Fig. 3d,e), while reducing the time needed tinuous and sinusoidal inhalation yield nearly complete
adsorptionatSc≲10.
to reach this maximum (Fig. 3f). AsScincreases,adsorptiondrops
Our model assumes axisymmetric flow, which by con- rapidly. Furthermore, continuous and sinusoidal inhala-
structiongiveszeroradialvelocityontheaxis,soanodor tion show quantitative agreement, suggesting that flow
pulseontheaxismuststillcrossadiffusivelayertoreach variation due to sinusoidal inhalation does not increase
the ciliary flow. Non-axisymmetric beating would break adsorption. The agreement between the full simulations
thisconstraint,generatingricherflowpatternsthatcould andthecylindricaltheoryconfirmsthattheleading-order
enhanceadsorptionfurther. Together,theseresultsshow behavior is controlled by the competition between axial
that active ciliary pumping can lift adsorption above the advection and transverse diffusion.
| passive | limit | set | by the | medium, | providing |     | a mechanism |     |                      |      |        |                      |     |
| ------- | ----- | --- | ------ | ------- | --------- | --- | ----------- | --- | -------------------- | ---- | ------ | -------------------- | --- |
|         |       |     |        |         |           |     |             |     | The full simulations | also | reveal | where odor molecules |     |
bywhichaquaticolfactionmaybecomeviablealbeitstill would hit the olfactory epithelium lining the chamber
slow relative to olfaction in air. wall. Thein-planeprojectionoftheboundaryflux,shows
Let us now evaluate to what extent incorporating the a non-uniform distribution (Fig. 4c,d). Aquatic olfac-
actual geometry of the axolotl olfactory chamber affects tion displays an overall poorer adsorption, distributed
the results. To this end, we solve Eqs. (A1)-(A2) within across the whole chamber; in contrast, terrestrial olfac-
two distinct domains, corresponding to the morpholo- tionconcentratesalargefluxpredominantlyneartheen-
gies of reconstructed aquatic and terrestrial chambers. trance of the chamber. The uneven regions where odor-
Within the aquatic morphology at the largest Schmidt ant molecules hit the epithelium suggest that ultimately
number accessible through direct numerical simulations sensation may increase if olfactory sensory neurons lo-
(Sc = 100), odor concentration remains high through- calize strategically closer to the opening for terrestrial
out most of the chamber, indicating that a substantial animalsandthroughoutthechamberinaquaticanimals.

5
1.0
0.5
0.0
0.0 0.5 1.0 1.5 2.0
z/R
R/r
a cilia-driven flow
0.6
0.4
0.2
0.0
0 50 100 150 200
time (s)
0 N/N
b
30
25
no cilia 20 /R=0.1
/R=0.5 15
/R=1 /R=2 10
/R=5
5
0.1 0.5 1 2 5
/R
)s(
1.0=0
N/N
ot
emit
c
no cilia
0.04
0.03
0.02
0.01
0.00
0 10 20 30 40
time (s)
)1
s(
td/)0
N/N(d
d
0.04
0.03
0.02
0.01
0.1 0.5 1 2 5
/R
)1
s(
td/)0
N/N(d
mumixam
e
30
25
20
15
no cilia 10
0.1 0.5 1 2 5
/R
)s(
xulf
mumixam
ot
emit
|u|/|u|max
1.0
0.5
0.0
f
no cilia
FIG. 3. Metachronal beating of cilia increases the rate of odor adsorption and maximum odor flux – results shown for the
chamber in water (Sc = 1000, Re = 0). (a) Streamlines and magnitude of the velocity field due to the metachronal beating
of cilia at the top wall. (b) Adsorption efficiency N/N as a function of time for cilia beating with different wavelengths λ.
0
The dashed curve shows adsorption efficiency without cilia. (c) Time to reach N/N = 0.1 for cilia beating at different λ.
0
Thedashedlineshowsthecorrespondingvaluewhennociliaarepresent. (d)Instantaneousodorfluxintotheepitheliumasa
function of time for different λ, with (e) the maximum flux and (f) the time to reach it shown as functions of λ. Dashed lines
show the corresponding values without cilia.
Odors differ widely in their saturated concentrations, speed up odor adsorption?
set by their solubility in water and their volatility in air. To ask whether higher availability can compensate for
Can the inefficiency of the passive chamber be overcome slow adsorption in passive chambers in water, we de-
bylargeodorconcentrationsalone,withoutactivepump- fine a detection threshold N , the cumulative number
t
ing? Toaddressthis,wefirstcomputethesaturatedcon- of molecules that need to reach the epithelium to trig-
centrationofapanelofmoleculesassociatedwithaquatic ger a neural response, and let N be the amount of odor
0
and aerial sensing (Table S1). The total adsorption rate moleculesdeliveredneartheinlet. Attimesmuchshorter
(moles per unit time) for a constant source is obtained than the diffusion time, the amount adsorbed has the
by multiplying the adsorption efficiency ϕ/ϕ by the in- closed form (see Sec. S II)
0
coming odor flux ϕ = c UπR2/2, evaluated at the sat-
0 0
urated concentration c 0 of each molecule (see Sec. S I N ≈2N e−tD/(4t), t =
R2
, (4)
in the Supporting Information). The resulting adsorp- 0 D D
tion rates at saturation are shown as ϕ against ϕ
air water where t is the diffusion time. Setting N(t∗)=N gives
(Fig. 5a), spanning several orders of magnitude. Clearly, D t
the detection time
in realistic scenarios odor is much more diluted than its
maximum concentration at saturation, thus these values t∗ 1 N
= , α≡ 0. (5)
should be considered upper bounds on the number of t 4log2α N
D t
molecules that a passive chamber can deliver to the ep-
ithelium in each medium. In particular, they are more Equation(5)holdswhilet∗ ≪t D ,whichrequiresα≳10.
relevant for chemosensation from a very close distance. This is a reasonable assumption for proximal sensing
Under these saturated conditions and despite the large sincefortheodorantsconsideredhere,saturatedconcen-
inefficiency of olfaction in water, the sheer number of trations exceed reported detection thresholds by factors
molecules hittingthe epitheliumis extremelylarge, both α∼109 to 1013 (Sec. S III).
in air and in water. But do large concentrations also Availability therefore enters only through logα, and
the resulting gains are relatively minimal (Fig. 5b).

6
|     |       | log10(c/c | 0)  |                 |        |     |     |     |     |
| --- | ----- | --------- | --- | --------------- | ------ | --- | --- | --- | --- |
|     | a     |           |     |                 | J/Jmax |     |     |     |     |
|     | water |           | c   |                 |        |     |     |     |     |
|     |       |           | 0   | aquatic chamber |        | 100 |     |     |     |
e
1.0
10 1
0.8
2
10
0 0.6
b
|     | air |     | 3                     |     |     | /    |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | ---- | --- | --- | --- |
|     |     |     | d terrestrial chamber |     |     | 10 3 |     |     |     |
0.4
cylindrical theory
10 4
|     |     |     |     |     |     | 0.2 | DNS continuous |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
DNS sinusoidal
5
10 0.0
|     |     |     |     |     |     |     | 100 101 | 102 103 |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- |
|     |     |     | 6   |     |     |     | Sc      |         |     |
FIG. 4. Direct numerical simulations in reconstructed axolotl chambers match the cylindrical model and reveal the spatial
structure of wall adsorption (a) Odor concentration within the aquatic morphology at Sc = 100 with a steady odor source,
fixing Re=2.1. The concentration (color coded) remains high over most of the chamber, showing that much of the odor field
travels through the chamber without reaching the epithelium. White arrows show the velocity field. (b) Odor concentration
within the terrestrial morphology at Sc = 1. The odor field quickly reaches the epithelium where it is adsorbed, causing a
strong depletion within the bulk of the chamber. (c) Odor molecules per unit surface reaching the surface in a unit time,
J =|D∇c·nˆ|,intheaquaticchamberand(d)intheterrestrialchamber,projectedontothevisualizationplane. Theboundary
color shows J normalized with the maximum flux. The inner color shows the odor field. Consistent with (a) and (b), most of
theadsorptionoccursimmediatelyneartheentranceinair,whereasitoccursthroughoutthechamberinwater. (e)Adsorption
efficiency as a function of Sc for the aquatic chamber. The cylindrical theory from Fig. 1 is shown for reference, together with
| direct numerical | simulations | for continuous | and sinusoidal | inhalation. |     |     |     |     |     |
| ---------------- | ----------- | -------------- | -------------- | ----------- | --- | --- | --- | --- | --- |
Across a range spanning four orders of magnitude in α, measured a visible response consisting in a sudden turn
the detection time falls by only a factor of four. Note, of the head, a head snap. The number of head snaps
however, that these gains become sizable when consider- increases markedly when odor stimuli derived from prey
ing odors at saturation, potentially relevant when olfac- are present relative to housing water (Fig. 6b), confirm-
tionisusedasaproximalsense. Arelatedcalculationus- ing that axolotls detect and respond to odor. Together,
ingathresholdontheinstantaneousadsorbedfluxrather thenegligibleaquaticinhalationandtheclearbehavioral
than the accumulated amount also yields the same con- response suggest that axolotls may speed up odor detec-
clusion(Sec.SIIIintheSupportingInformation). Thus, tion by active mechanisms like motile cilia, and poten-
onlyextremelylargeconcentrationscanspeedupadsorp- tially respond to extremely high concentrations.
tion sensibly.
| To ask          | whether these | expectations    | are reflected | in ax-    |     |      |            |     |     |
| --------------- | ------------- | --------------- | ------------- | --------- | --- | ---- | ---------- | --- | --- |
|                 |               |                 |               |           |     | III. | DISCUSSION |     |     |
| olotl behavior, | we analyze    | the respiratory | and           | olfactory |     |      |            |     |     |
behaviorofaxolotlsintheaquaticandterrestrialphases.
Consistent with our finding that inhalation flow does The cylindrical theory and the full simulations lead to
not improve olfaction in the aquatic phase (Fig. 2c), the same conclusion. Odor adsorption in an olfactory
the aquatic inhalation flow is negligible (Fig. 6a left), chamber, in the absence of active mechanisms or turbu-
|         |                    |       |             |           | lent mixing, | is controlled | primarily | by diffusion; | Re sets |
| ------- | ------------------ | ----- | ----------- | --------- | ------------ | ------------- | --------- | ------------- | ------- |
| whereas | in the terrestrial | phase | the animals | draw sub- |              |               |           |               |         |
stantial flows, ∼1cms−1 in the center of the chamber the ceiling on how much odor can be adsorbed from an
(Fig. 6a right). Since the inlet cross-section is roughly ephemeral whiff. For a given Re, at small Sc, diffusion
an order of magnitude smaller than that of the chamber, across streamlines is fast enough that the wall can ad-
mass conservation implies correspondingly higher speeds sorb nearly all incoming odorant. At high Sc, diffusion
at the inlet, which is the relevant location for adsorp- is too slow to supply the wall during the advective resi-
tion of an odor pulse, placing them in the range where dence time, so odor remains in the core of the flow and
|            |                |          |            |           | exitsthechamber. | Theactualaquaticandterrestrialge- |     |     |     |
| ---------- | -------------- | -------- | ---------- | --------- | ---------------- | --------------------------------- | --- | --- | --- |
| adsorption | is appreciably | enhanced | (Fig. 2c). | Given the |                  |                                   |     |     |     |
inefficiencies of olfaction in water, we wondered whether ometries modify the details, but they do not change the
axolotls before transition do respond to odor at all. To dominant scaling.
testthis,wemeasuredtheresponseofaxolotlstoanodor Thisconclusionhelpsclarifywhyaquaticolfactionisa
stimulus introduced directly near the nasal inlet. We difficult physical problem. Even if aquatic animals draw

7
|     |     |     |     |     |     |     | This | trade-off | is  | what | makes | active | pumping | power- |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- | ---- | ----- | ------ | ------- | ------ |
a
|     |     |     |     |     |     |     | ful as | a general | mechanism |     | to speed | up  | odor | adsorption |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --------- | --- | -------- | --- | ---- | ---------- |
air-sensed in aquatic organisms. Metachronal waves generated by
10−9
water-sensed beating cilia drive fluid radially, toward the absorbing
|     | 10−11 |     |     |     |     |     | wall, | rather | than | only along | the | chamber |     | axis. They |
| --- | ----- | --- | --- | --- | --- | --- | ----- | ------ | ---- | ---------- | --- | ------- | --- | ---------- |
)1−s lom(
|     |       |     |     |     |     |     | therefore                                            | enhance | the            | cross-stream |           | transport      |      | that limits |
| --- | ----- | --- | --- | --- | --- | --- | ---------------------------------------------------- | ------- | -------------- | ------------ | --------- | -------------- | ---- | ----------- |
|     | 10−13 |     |     |     |     |     | adsorption                                           |         | at high        | Sc.          | Our model | shows          | that | cilia of    |
|     |       |     |     |     |     |     | size ∼                                               | 1%      | of the radius, |              | beating   | in metachronal |      | waves,      |
|     | 10−15 |     |     |     |     |     | substantiallyincreaseadsorptionefficiencyandodorflux |         |                |              |           |                |      |             |
ria
|     |     |     |     |     |     |     | towards | the | epithelium. |     | The | speed-up | resulting | from |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | --- | --- | -------- | --------- | ---- |
ϕ
|     | 10−17 |     |     |     |     |     | metachronal |       | waves | depends       | heavily |         | on the    | wavelength |
| --- | ----- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | ------------- | ------- | ------- | --------- | ---------- |
|     |       |     |     |     |     |     | of the      | wave. | Long  | wavelengths   |         | require | cilia     | over many  |
|     |       |     |     |     |     |     | millimeters |       | to be | synchronized. |         | In      | axolotls, | the olfac- |
10−19
|     |     | 10−19 | 10−16 | 10−13 | 10−10 |     |      |            |          |     |        |          |       |           |
| --- | --- | ----- | ----- | ----- | ----- | --- | ---- | ---------- | -------- | --- | ------ | -------- | ----- | --------- |
|     |     |       |       |       |       |     | tory | epithelium | contains |     | motile | ciliated | cells | [17], and |
 (mol s−1)
ϕ water in zebrafish, ciliated cells have been shown to generate
|     |     |     |     |     |     |     | a flow | that | improves | olfactory |     | sensitivity |     | [13]. How- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---- | -------- | --------- | --- | ----------- | --- | ---------- |
b
|     |        |     |     |     |     |     | ever,                                              | whether    | the        | axolotl | olfactory | cilia              | synchronize | in         |
| --- | ------ | --- | --- | --- | --- | --- | -------------------------------------------------- | ---------- | ---------- | ------- | --------- | ------------------ | ----------- | ---------- |
|     |        |     |     |     |     |     | metachronalwavesisnotknown.                        |            |            |         |           | Moreworkisneededto |             |            |
|     | 0.08   |     |     |     |     |     | quantifythiskeyparameterandfullyestablishthespeed- |            |            |         |           |                    |             |            |
|     |        |     |     |     |     |     | up of                                              | olfactory  | adsorption |         | resulting | from               | cilia       | beating in |
|     | D 0.06 |     |     |     |     |     | aquatic                                            | organisms. |            |         |           |                    |             |            |
t/*t
|     |     |     |     |     |     |     | Using | a   | concentration |     | threshold |     | of  | c = |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------------- | --- | --------- | --- | --- | --- |
thr
|     |      |     |     |     |     |     | 10−14M   |       |           |        |                |       |        | 10−5M    |
| --- | ---- | --- | --- | --- | --- | --- | -------- | ----- | --------- | ------ | -------------- | ----- | ------ | -------- |
|     | 0.04 |     |     |     |     |     |          | [18], | saturated |        | concentrations |       | of c 0 | ∼        |
|     |      |     |     |     |     |     | to 10−1M |       | as well   | as     | metachronal    |       | waves  | with λ/R |
|     |      |     |     |     |     |     | ranging  | from  | 0 (no     | cilia) | to             | 2, we | obtain | that the |
0.02
|     |     | 101 | 102 | 103 | 104 | 105 |           |     |      |            |     |        |          |          |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---- | ---------- | --- | ------ | -------- | -------- |
|     |     |     |     |     |     |     | timescale | for | odor | adsorption |     | ranges | from 0.6 | s to 2.7 |
concentration ratio α s (also see Sec. S III in the Supporting Information).
|         |      |               |        |          |     |              | Thisestimateshowsthatinthepresenceofcilia, |     |          |     |          |            |     | aquatic      |
| ------- | ---- | ------------- | ------ | -------- | --- | ------------ | ------------------------------------------ | --- | -------- | --- | -------- | ---------- | --- | ------------ |
|         |      |               |        |          |     |              | olfaction                                  | can | function | at  | least as | a proximal |     | sense, but – |
| FIG. 5. | When | the olfactory | target | is close | and | odor is near |                                            |     |          |     |          |            |     |              |
saturation, a large number of odor molecules are adsorbed, interestingly – it sets a constraint on olfactory responses
|                                        |                |     |              |          |               |                | to be   | relatively | slow. |               | In fact, | olfactory | sampling | in         |
| -------------------------------------- | -------------- | --- | ------------ | -------- | ------------- | -------------- | ------- | ---------- | ----- | ------------- | -------- | --------- | -------- | ---------- |
| despite                                | inefficiencies | in  | the process. | However, |               | higher concen- |         |            |       |               |          |           |          |            |
|                                        |                |     |              |          |               |                | aquatic | animals    | is    | comparatively |          | slow      | [19],    | consistent |
| trationsdonothelpwithdetectionspeedup. |                |     |              |          | (a)Comparison |                |         |            |       |               |          |           |          |            |
oftheadsorptionrateinair,ϕ air ,withtheadsorptionratein with the fundamental physical constraints on how fast
water,ϕ water ,obtainedbycombiningthesaturatedmolecular sensation can be in water.
| concentration |     | with the | hydrodynamic |     | adsorption | efficiency. |     |           |         |         |     |     |             |         |
| ------------- | --- | -------- | ------------ | --- | ---------- | ----------- | --- | --------- | ------- | ------- | --- | --- | ----------- | ------- |
|               |     |          |              |     |            |             | A   | separate, | spatial | feature | of  | our | simulations | is that |
Thedashedlinedenotesequaladsorptionratesinthetwome-
odordeliverytotheepitheliumisheterogeneous,andthe
| dia. Red        | triangles | indicate       | molecules | expected  |           | to be sensed |           |           |        |         |     |              |     |             |
| --------------- | --------- | -------------- | --------- | --------- | --------- | ------------ | --------- | --------- | ------ | ------- | --- | ------------ | --- | ----------- |
|                 |           |                |           |           |           |              | high-flux | regions   | differ | between |     | the aquatic  |     | and terres- |
| in air, whereas |           | blue circles   | indicate  | molecules | expected  | to be        |           |           |        |         |     |              |     |             |
|                 |           |                |           |           |           |              | trial     | chambers. | This   | aspect  | is  | particularly |     | important   |
| sensed in       | water.    | (b) Normalized |           | odor      | detection | time t∗/t    |           |           |        |         |     |              |     |             |
D
as a function of increase in concentration near the inlet. An considering that we have not modeled the fascinating
increase in the concentration by a factor of 104 only speeds process of odor binding, which will further decrease the
|              |     |       |             |     |     |     | efficiency | of      | olfaction.  |     | The dwelling |       | time     | of odorant |
| ------------ | --- | ----- | ----------- | --- | --- | --- | ---------- | ------- | ----------- | --- | ------------ | ----- | -------- | ---------- |
| up detection | by  | about | four times. |     |     |     |            |         |             |     |              |       |          |            |
|              |     |       |             |     |     |     | molecules  | near    | receptors   |     | is on the    | order | of ms,   | requiring  |
|              |     |       |             |     |     |     | many       | odorant | molecules   |     | to trigger   | a     | response | [20]. This |
|              |     |       |             |     |     |     | suggests   | that    | to maximize |     | efficiency   | of    | odorant  | binding,   |
moreodor-containingwaterthroughthechamber,thein-
|          |      |           |         |           |      |            | receptors | may | be  | concentrated |     | in regions |     | where odor |
| -------- | ---- | --------- | ------- | --------- | ---- | ---------- | --------- | --- | --- | ------------ | --- | ---------- | --- | ---------- |
| creasing | flow | rate also | reduces | residence | time | and lowers |           |     |     |              |     |            |     |            |
capture efficiency. The animal can instead reduce flow molecules more probably hit the epithelium. To what
|           |      |             |     |          |      |              | extent    | this | adaptation | is  | present | in axolotls |     | and aquatic |
| --------- | ---- | ----------- | --- | -------- | ---- | ------------ | --------- | ---- | ---------- | --- | ------- | ----------- | --- | ----------- |
| rate, but | this | also lowers | the | incoming | odor | flux. For an |           |      |            |     |         |             |     |             |
|           |      |             |     |          |      |              | organisms | is   | not known. |     |         |             |     |             |
instantaneousodorpulse,wehaveshownthatthereisan
optimal flow rate that maximizes adsorption efficiency Ifaquaticolfactionwasusedasaproximalsense,more
and at this optimal flow rate, most of the odor whiff akin to taste, then the targets would be much closer and
eventually reaches the epithelium. However, even at this thereforemoreconcentrated. Sensingthesetargetsiseas-
optimalflowrate,thetimerequiredtoachievethatmax- ier because of the sheer number of molecules entering
imum efficiency is tens of seconds in water, compared to the chamber. The process remains as wasteful and inef-
ms in air. No passive adjustment of the flow, in the ab- ficient independently of how concentrated the target is,
senceofturbulentmixing,escapesthistrade-off: efficient butreachingafixedthresholdofmoleculeshittingtheep-
aquaticsensingatsmallRerequiresanactivemechanism ithelium is faster for concentrated targets. This speedup
that raises adsorption without paying the residence-time resulting merely from proximity is extremely small, re-
| cost. |     |     |     |     |     |     | quiringordersofmagnitudeofconcentrationincreasefor |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

8
a
aquatic terrestrial
0.4
0.0
0.4
0.4
0.0
0.4
)mccs(
wolf
24
16
0.4 8
0.0
0.4 0
0 2 4 6 8 10 0 2 4 6 8 10 without odor with odor
time (s) time (s)
spans
daeh
b
data
mean +/- SD
median
FIG. 6. Axolotls in the aquatic phase show very weak inhalation but respond to odor with head movements. (a) Inhalation
flow for three aquatic (left) and three terrestrial (right) axolotls. Aquatic flow is near zero, whereas terrestrial animals display
stronginhalation. (b)Numberofheadsnapsinthepresenceandabsenceofodor. Pointsareindividualtrials. Thesquareand
bars show the mean and the orange line the median. Head snapping increases markedly when odor is present.
appreciable effects to occur. AUTHOR CONTRIBUTIONS
MJ, LSR, NWB and AS contributed to the design of
Several additional mechanisms could increase aquatic
the research. MJ developed the theory, conducted the
adsorptionbeyondtheflowvaluesreportedhere. Longer
simulations and analyzed the resulting data. LSR and
residence times could be obtained by temporary reten-
MS conducted the experiments and analyzed the cor-
tion of water inside the chamber or recirculating flow, as
responding data. FV wrote the DNS code, which MJ
has been observed for some aquatic organisms [9]. Also,
adapted for the present study. All authors contributed
studieshaveshownthatnear-walltransportinmarineor-
to the interpretation of the results. MJ and AS wrote
ganisms could be enhanced by active deformation of the
the manuscript with input from coauthors.
chamber wall or jaw protrusion [9, 21]. Another mecha-
nismtoventilatetheolfactorychamberandtointroduce
fluctuations is through the motion of the organism [22].
ACKNOWLEDGMENTS
These mechanisms are not alternatives to the hydrody-
namic constraint identified here. Rather, they are possi-
ble biological responses to it. This research was supported by grants to AS from the
EuropeanResearchCouncilundertheEuropeanUnion’s
Horizon 2020 research and innovation programme (grant
The present model has several limitations. The wall agreementnumber101002724RIDING)andtheNational
is treated as perfectly absorbing, so the computed ef- Institutes ofHealthunder award numberR01DC018789.
ficiencies are upper bounds on passive capture, and the The European Commission and the other organizations
simulationsuseanidealizedflowstructure. Despitethese are not responsible for any use that may be made of the
simplifications, thecentralresultisrobust: thewater-air information it contains.
contrast in Schmidt number imposes a severe transport
penalty on aquatic odor adsorption, one that passive ge-
ometry alone cannot remove but that active mechanisms Appendix A: Methods
suchasciliarypumpingcanpartiallyrelieve. Ourbehav-
ioral experiments and inhalation measurements support
Governing equations
this picture. Axolotls respond to proximal odor cues yet
We consider odor transport in an incompressible ve-
draw almost no inhalation flow in water, consistent with
locity field u(x,t). The fluid motion is described by
our finding that passive flow cannot rescue aquatic cap-
ture and pointing instead to an active mechanism, plau- ∂u 1
+(u·∇)u=− ∇p+ν∇2u, (A1)
sibly the motile cilia lining the olfactory chamber. This
∂t ρ
limitation of aquatic olfaction is not specific to the ax-
∇·u=0,
olotl. Because it follows from the low diffusivity of odor-
ants in water, any small aquatic sniffer that cannot gen-
where p is pressure, ρ is density and ν is kinematic vis-
erateturbulencefacesthesamepenalty. Activepumping
cosity. The odor concentration c(x,t) obeys
is one way out, but how far morphological specialization
andbehaviorcanfurtheroffsettheinefficiencyofaquatic ∂c
olfaction remains to be established. +u·∇c=D∇2c, (A2)
∂t

9
where D is the molecular diffusivity. The Schmidt num- With θ = c/c , Y = r/R, T = tD/R2, Z = z/R and
0
ber is Sc = ν/D. We consider two different initial con- Reynolds number Re=UR/ν, Eq. (A10) becomes,
ditions for the odor. In the first, the inlet concentration
is fixed at c . In the second, we use an instantaneous ∂θ ∂θ 1 ∂ (cid:18) ∂θ (cid:19) ∂2θ
0 +ReSc(1−Y2) = Y + . (A11)
odor pulse at the inlet. The chamber wall is treated as a ∂T ∂Z Y ∂Y ∂Y ∂Z2
perfectly absorbing surface, c = 0. The adsorption rate
can be computed from the diffusive flux into the wall, Therelevantnondimensionalparameterinthissystemis
thus Pe = ReSc. However, in our analysis, we treat Re
(cid:90)
and Sc separately to provide useful comparisons to bi-
ϕ(t)= D |∇c·nˆ| dS, (A3)
ological systems. To obtain results presented in Fig. 1,
Γw
we solve Eq. (A11) with θ(Y,0) = 1, θ(1,Z) = 0 and
where Γ w is the absorbing wall and nˆ is the wall normal. ∂ Y θ(0,Z) = 0. Note that in the advective regime, when
Whentheinletconcentrationisfixedatc 0 ,wenormalize axialdiffusioncanbeneglected,thisistheclassicGraetz
this rate using the net incoming odor flux problem [25, 26]. The results for an instantaneous odor
pulse are evaluated by placing a Gaussian odor pulse
(cid:90)
ϕ = c u·nˆ dS, (A4) of σ = 0.1R at the center of a cylinder of length 2L.
0 0 in
Γin Adsorption is evaluated in the downstream half of the
cylinder. Fornumericallysolvingthecylindricalproblem
so that ϕ/ϕ is the fraction of incoming odorant
0 (Eq. (A11)), we use a finite volume method. Unless oth-
molecules adsorbed during one passage through the
erwisespecified,wechooseR=0.53mmandL/R=8.67
chamber. Integrating ϕ over time gives the total odor
to be consistent with the aquatic axolotl geometry. The
radius is obtained by averaging the equivalent radius of
(cid:90) T
N(T)= ϕdt (A5) the chamber cross-section at five axial positions, and the
0 lengthisthecenterlinedistancefromtheinlettotheout-
let.
adsorbed until time T. When the inlet concentration is
The wall flux in the cylinder is evaluated, following
fixed at c , N is normalized using
0 Eq. (A3), as
(cid:90) T
N 0 = ϕ 0 dt. (A6) (cid:90) L ∂c (cid:12) (cid:12)
0 ϕ=− 2πRD (cid:12) dz. (A12)
∂r(cid:12)
0 r=R
For the instantaneous odor pulse, N is normalized using
the total amount of initial odor When the inlet concentration is c 0 , the adsorption effi-
ciency ϕ/ϕ becomes (Eq. (A4))
(cid:90) 0
N = c| dV, (A7)
0
V
t=0
ϕ
(cid:82)L
2πRD
∂c(cid:12)
(cid:12) dz
= − 0 ∂r r=R
where V is the domain volume. ϕ 0 c 0 (cid:82) 0 R 2πru z (r)dr
In the steady state, when the inlet concentration is 4 (cid:90) R L ∂θ (cid:12) (cid:12)
fixed at c 0 , the odor flux can be computed from the dif- = − (cid:12) dZ. (A13)
ference between the incoming and outgoing fluxes, ReSc 0 ∂Y (cid:12) Y=1
(cid:90) (cid:90)
ϕ= c u·nˆ dS− cu·nˆ dS. (A8)
0 in out Full-geometry direct numerical simulations
Γin Γout
For the full numerical simulations, we use 3D recon-
structions of the aquatic and terrestrial geometries. The
Cylindrical approximation Navier-Stokes equations are solved by three-dimensional
In the first part, we approximate the chamber as a directnumericalsimulationusingasemi-implicitsecond-
cylinderofradiusRandlengthLwithanabsorbingwall. orderfinite-differencescheme[27]. Thechamberwallsare
The axial coordinate is z, the radial coordinate is r and imposedasno-slip,absorbingboundariesthroughanim-
theaxialvelocityisassumedtofollowaPoiseuilleprofile, mersed boundary method [28]. Continuous inhalation is
imposed by a steady inlet jet. For sinusoidal inhalation,
(cid:18) r2 (cid:19) theinletspeedisvariedperiodicallywithaperiodof10s.
u (r)=U 1− . (A9)
z R2 Theoutletistreatedasanopenboundaryembeddedina
larger computational domain. The odor concentration is
Thus the concentration satisfies [23, 24] fixed at the inlet, with an outflow condition at the out-
let. The mean velocities normal to the midplane cross
∂c (cid:18) r2 (cid:19) ∂c (cid:20) 1 ∂ (cid:18) ∂c (cid:19) ∂2c (cid:21) section are 1.7 mm/s and 7.2 mm/s for the aquatic and
+U 1− =D r + .
∂t R2 ∂z r∂r ∂r ∂z2 terrestrial chambers, respectively. We choose a nonzero
(A10) inhalation speed in water, despite experiments showing

10
negligibleinhalation(Fig.6aleft),togetanupperbound Appendix B: Optimal adsorption of an odor patch
on odor adsorption in water. For continuous inhalation, inside a cylinder
adsorption is evaluated using Eq. (A8) after the solution
reached a statistically stationary state. For sinusoidal We are interested in evaluating the optimal flow rate
inhalation, adsorption is evaluated using the average of to maximize the adsorption of an odor patch located at
Eq. (A8) over one period after discarding the first ten the center of the inlet. Eq. (A11) is our starting point.
cycles. Ourinitialconditionisapointsourceatthecenterofthe
inlet, given by
3D reconstructions of axolotl olfactory cavities were
generated using animals that were deeply anesthetized
δ(Y)δ(Z)
with 1% w/v MS-222 (Syncaine; Syndel) and eutha- θ(Y,Z,T =0)= (B1)
2πY
nized by decapitation. Heads were fixed overnight in
4%paraformaldehydeinphosphatebufferedsaline(PBS) such that the total odor integrates to unity. Let us find
and then transferred to 1% phosphotungstic acid in 70% Pe = ReSc that maximizes odor adsorption onto the
ethanol and incubated for 14 days at 4◦C in complete cylinder wall. For this, we can optimize the wall hit po-
darkness. Followingincubation,sampleswererinsedwith sition Z w of an odor particle that starts at the inlet at
PBS and secured with cheesecloth in a 50 mL conical time T =0 so that the mean wall hit position lies at the
tube with a small amount of PBS at the bottom to pre- midpoint of the cylinder (i.e., E[Z W ] = 2 L R ). To calcu-
ventsamplesfromdryingout. Sampleswereindividually late this, let T w be the first time when an odor molecule
scanned on a SkyScan 1273 micro-computed tomogra- hits the wall.
physystem(Bruker; voltage=52kV;current=120µA; (cid:90) Tw
pixel size = 9.00 µm), with a rotation step of 0.11◦. Re- Z =ReSc (1−Y2)dt+B , (B2)
w t Tw
construction was performed using NRecon (v. 2.1.0.1) 0
beforeindividualscanfileswerecombinedintosingleim-
where B is the axial stochastic motion, whose expec-
age stacks using ImageJ. Olfactory cavities were recon-
Tw
tation is zero.
structedin3DSlicer[29]usingthreshold-basedselection,
To evaluate the expectation of the above function, we
manually refined with the scissor and eraser tools to re- note that E[T ] = 1 and E (cid:104) (cid:82)Tw(1−Y2)dt (cid:105) = 1 [31],
move extraneous features. w 4 0 t 16
resulting in the mean adsorption location of
Measurements were collected using an airflow sen-
sor (Honeywell, AWM3100V) attached to Silastic tubing E[Z ]= 3 ReSc. (B3)
(length: 5cm). ThesignalwasdigitizedusingaDigidata w 16
1550Bdigitizer(MolecularDevices)usingClampExsoft-
Since we want this to be near the middle of the cylinder,
ware(MolecularDevices). Usingacustom-writtenMAT-
we get
LAB(TheMathWorks,Inc.) script,sensorvoltagevalues
were then converted to airflow using the manufacturer’s
calibration table. To represent bidirectional inhalation 8L
ReSc= . (B4)
and exhalation, we mirrored the calibration curve, yield- 3R
ing flow as a function of time in standard cubic cen-
timeters per minute (sccm). Using the Silastic tube’s
Appendix C: Cilia-driven flow and adsorption
inner diameter (3mm), we then converted flow to aver-
age velocity in cm/s by dividing the flow by the tubing’s
cross-sectionalarea. Todirectlycompareaquaticandter- Inspired by previous works on hydrodynamics of cil-
restrial animal inhalations, we calculated peak-to-peak iated surfaces [32, 33], we derive the equations for the
flow and estimated breathing rate from the inhalation- flow and adsorption inside a ciliated chamber as follows.
dominant FFT peak, while treating very low-amplitude Let us again approximate the olfactory chamber as a
aquatic traces as no inhalation. cylinder of radius R and length L. Assume that the in-
ner surface of the cylinder is lined with cilia whose tips
To assess behavioral responses to prey-derived
trace circular orbits of radius εR, beating metachronally
molecules, black worms (10 grams; Eastern Aquatics,
with wavenumber k and angular frequency ω . When
f
Inc.) wereblendeduntilhomogeneoustoproduceacrude
ε≪1, we can approximate the wall boundary condition
prey extract. Aquatic animals were then placed in a 1 L
astheciliatipvelocityu | =εRω cos(kz−ω t)and
r r=R f f
tank filled with 750mL of Holtfreter’s solution and al-
u | =εRω sin(kz−ω t).
z r=R f f
lowed to adapt to the new aquaria for 10 min. Following
The unsteady Stokes equation for the fluid flow inside
adaptation, animals were presented with either 3 mL of
the cylinder can be written as [34]
crude prey extract or Holtfreter’s solution and behavior
wasfilmedoverheadusingaGoProcamera(GoPro,Inc.) ∂ (cid:0) E2ψ (cid:1) =νE4ψ, (C1)
t
Later, trials were analyzed using BORIS software [30] to
quantify the number of head snaps following molecule where ψ is the stream function such that u z = 1 r ∂ r ψ and
delivery over a 3 min period. u =−1∂ ψ,andE2 ≡∂2−1∂ +∂2. Weseeksolutions
r r z r r r z

11
(cid:16) (cid:17)
with the same space and time dependence as the wall L+ iωf ψ˜ = 0, such that ψ˜ = ψ˜ + ψ˜ . The full
|     |     |     |     |     | ν 2 |     | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
forcing
|              |            |                           |           | solution | then has the         | form             |           |                |
| ------------ | ---------- | ------------------------- | --------- | -------- | -------------------- | ---------------- | --------- | -------------- |
|              |            | (cid:104) ψ˜(r)ei(kz−ωft) | (cid:105) |          |                      |                  |           |                |
|              | ψ(r,z,t)=ℜ |                           | . (C2)    |          | ψ˜=ArI               | (kr)+CrI         | (κr),     | (C4)           |
|              |            |                           |           |          |                      | 1                | 1         |                |
|              |            |                           | d2        | where    | I 1 i s the modified | Bessel function  | of        | the first kind |
| Substituting | this into  | Eq. (C1) and defining     | L ≡ −     |          | (cid:113)            |                  |           |                |
|              |            |                           | dr2       |          | iωf.                 |                  |           |                |
| 1 d −k2,     | we get     |                           |           | and κ    | = k2−                | The coefficients | A and     | C are ob-      |
| rdr          |            |                           |           |          | ν                    |                  |           |                |
|              |            |                           |           | tained   | from the slip        | velocity at the  | boundary. | Note that      |
|              | (cid:18)   | (cid:19)                  |           |          |                      |                  |           |                |
iω f ψ˜=0. theK 1 solutionsarediscardedtokeeptheflowregularat
|     | L L+ |     | (C3) |          |                                           |     |     |     |
| --- | ---- | --- | ---- | -------- | ----------------------------------------- | --- | --- | --- |
|     |      | ν   |      | theaxis. | Toobtaintheresultspresentedinthemaintext, |     |     |     |
wesolveEq.(A2)fortheodorfield,usingthecilia-driven
Since both operators above commute, the general so- velocity field generated using Eq. (C4) as the advecting
Lψ˜
| lution is | the sum of | the solutions of | = 0 and | flow. |     |     |     |     |
| --------- | ---------- | ---------------- | ------- | ----- | --- | --- | --- | --- |
1
[1] D. Webster and M. Weissburg, The hydrodynamics of C. D. Verdugo, M. Hoffman, P. Lal, K. Kawakami,
chemical cues among aquatic organisms, Annual Review K. Pekkan, et al., Motile-cilia-mediated flow improves
of Fluid Mechanics 41, 73 (2009). sensitivity and temporal resolution of olfactory compu-
[2] G. Reddy, V. N. Murthy, and M. Vergassola, Olfactory tations, Current Biology 27, 166 (2017).
sensing and navigation in turbulent environments, An- [14] C.Ringers,E.W.Olstad,andN.Jurisch-Yaksi,Therole
nualReviewofCondensedMatterPhysics13,191(2022). of motile cilia in the development and physiology of the
[3] P. Moore and J. Crimaldi, Odor landscapes and ani- nervous system, Philosophical Transactions of the Royal
mal behavior: tracking odor plumes in different physical Society B: Biological Sciences 375, 20190156 (2019).
worlds, Journal of marine systems 49, 55 (2004). [15] C. Ringers, S. Bialonski, M. Ege, A. Solovev, J. N.
[4] J. A. Riffell, L. Abrell, and J. G. Hildebrand, Physical Hansen, I. Jeong, B. M. Friedrich, and N. Jurisch-Yaksi,
processesandreal-timechemicalmeasurementofthein- Novel analytical tools reveal that local synchronization
sect olfactory environment, Journal of chemical ecology of cilia coincides with tissue-scale metachronal waves in
34, 837 (2008). zebrafishmulticiliatedepithelia,Elife12,e77701(2023).
[5] B. A. Craven, E. G. Paterson, and G. S. Settles, The [16] J. P. Cox, Ciliary function in the olfactory organs of
fluid dynamics of canine olfaction: unique nasal airflow sharks and rays, Fish and Fisheries 14, 364 (2013).
patterns as an explanation of macrosmia, Journal of the [17] H. L. Eisthen, D. R. Sengelaub, D. M. Schroeder, and
Royal Society Interface 7, 933 (2010). J. R. Alberts, Anatomy and forebrain projections of the
[6] S. Firestein, How the olfactory system makes sense of olfactoryandvomeronasalorgansinaxolotls(ambystoma
scents, Nature 413, 211 (2001). mexicanum)(part2of2),Brain,BehaviorandEvolution
[7] M. Tang, M. Shiraiwa, U. Pöschl, R. Cox, and 44, 117 (1994).
M. Kalberer, Compilation and evaluation of gas phase [18] A. M. Scott, Z. Zhang, L. Jia, K. Li, Q. Zhang, T. Dex-
diffusion coefficients of reactive trace gases in the at- heimer, E. Ellsworth, J. Ren, Y.-W. Chung-Davidson,
mosphere: Volume2.diffusivitiesoforganiccompounds, Y.Zu,etal.,Spermineinsemenofmalesealampreyacts
pressure-normalised mean free paths, and average knud- as a sex pheromone, PLoS Biology 17, e3000332 (2019).
sen numbers for gas uptake calculations, Atmospheric [19] H. Spors, D. F. Albeanu, V. N. Murthy, D. Rinberg,
Chemistry and Physics , 5585 (2015). N. Uchida, M. Wachowiak, and R. W. Friedrich, Illumi-
[8] J. Delgado, Molecular diffusion coefficients of organic natingvertebrateolfactoryprocessing,JournalofNeuro-
compounds in water at different temperatures, Journal science 32, 14102 (2012).
of phase Equilibria and Diffusion 28, 427 (2007). [20] V. Bhandawat, J. Reisert, and K.-W. Yau, Elementary
[9] J. P. Cox, Hydrodynamic aspects of fish olfaction, Jour- response of olfactory receptor neurons to odorants, Sci-
nal of the Royal Society Interface 5, 575 (2008). ence 308, 1931 (2005).
[10] M. Koehl, J. R. Koseff, J. P. Crimaldi, M. G. McCay, [21] G. A. Nevitt, Do fish sniff? a new mechanism of olfac-
T.Cooper,M.B.Wiley,andP.A.Moore,Lobstersniff- tory sampling in pleuronectid flounders, Journal of Ex-
ing: antennule design and hydrodynamic filtering of in- perimental Biology 157, 1 (1991).
formation in an odor plume, Science 294, 1948 (2001). [22] R. J. Garwood, J. Behnsen, H. K. Haysom, J. N. Hunt,
[11] J.T.StuelpnagelandJ.O.Reiss,Olfactorymetamorpho- L.J.Dalby,S.K.Quilter,J.S.Maclaine,andJ.P.Cox,
sis in the coastal giant salamander (dicamptodon tene- Olfactoryflowinthesturgeonisexternallydriven,Com-
brosus), Journal of Morphology 266, 22 (2005). parativeBiochemistryandPhysiologyPartA:Molecular
[12] J. J. Różański and K. D. Żuwała, Macro-and micromor- & Integrative Physiology 235, 211 (2019).
phologicalremodelingofolfactoryorgansthroughoutthe [23] C. Barrera, M. Letelier, D. Siginer, and J. Stockle, The
ontogeny of the fire salamander salamandra salaman- graetz problem in tubes of arbitrary cross section, Acta
dra (linnaeus, 1758), Journal of Morphology 281, 1173 Mechanica 227, 3239 (2016).
(2020). [24] L. G. Leal, Advanced transport phenomena: fluid me-
[13] I. Reiten, F. E. Uslu, S. Fore, R. Pelgrims, C. Ringers, chanics and convective transport processes,Vol.7(Cam-

12
bridge university press, 2007).
[25] G.M.Brown,Heatormasstransferinafluidinlaminar
flow in a circular or flat conduit, AIChE Journal 6, 179
(1960).
[26] R. K. Shah and A. L. London, Laminar flow forced con-
vection in ducts: a source book for compact heat ex-
changer analytical data (Academic press, 1978).
[27] F. Viola, V. Meschini, and R. Verzicco, Fluid–structure-
electrophysiology interaction (fsei) in the left-heart: a
multi-waycoupledcomputationalmodel,EuropeanJour-
nal of Mechanics-B/Fluids 79, 212 (2020).
[28] R. Verzicco, M. D. de Tullio, and F. Viola, An In-
troduction to Immersed Boundary Methods, Cambridge
Monographs on Applied and Computational Mathemat-
ics (Cambridge University Press, 2025).
[29] A.Fedorov,R.Beichel,J.Kalpathy-Cramer,J.Finet,J.-
C.Fillion-Robin,S.Pujol,C.Bauer,D.Jennings,F.Fen-
nessy, M. Sonka, et al., 3d slicer as an image computing
platformforthequantitativeimagingnetwork,Magnetic
resonance imaging 30, 1323 (2012).
[30] O. Friard and M. Gamba, Boris: a free, versatile open-
sourceevent-loggingsoftwareforvideo/audiocodingand
live observations, Methods in ecology and evolution 7,
1325 (2016).
[31] L. Koralov and Y. G. Sinai, Theory of probability and
random processes (Springer Science & Business Media,
2007).
[32] C.Brennen,Anoscillating-boundary-layertheoryforcil-
iary propulsion, Journal of Fluid Mechanics 65, 799
(1974).
[33] J. R. Blake, A spherical envelope approach to ciliary
propulsion, Journal of Fluid Mechanics 46, 199 (1971).
[34] J. Happel and H. Brenner, Low Reynolds number hydro-
dynamics: with special applications to particulate media
(Springer Science & Business Media, 2012).
[35] J.Newman,Extensionofthelevequesolution,Journalof
Heat Transfer 91, 177 (1969).
[36] S. Kim, J. Chen, T. Cheng, A. Gindulyte, J. He, S. He,
Q. Li, B. A. Shoemaker, P. A. Thiessen, B. Yu, L. Za-
slavsky, J. Zhang, and E. E. Bolton, Pubchem 2025 up-
date, Nucleic Acids Res. 53, D1516 (2025).
[37] The Good Scents Company, The good scents
company information system, https://www.
thegoodscentscompany.com (2025), accessed: 2025-
03-11.

13
Supporting Information: Amphibian water to land transition reveals physical limits of
olfaction
S I. ASYMPTOTICS OF ADSORPTION INSIDE A CYLINDER AND SATURATED ADSORPTION
|     |     |     |     |     | RATES | OF ODORANT |     |     | MOLECULES |     |     |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --------- | --- | --- |
Weagainusethecylindricalapproximation(Eq.(A11)). Intheadvectiveregime, wecanneglecttheaxialdiffusion
| term and | the equation |     | becomes |     |             |     |     |     |          |          |      |
| -------- | ------------ | --- | ------- | --- | ----------- | --- | --- | --- | -------- | -------- | ---- |
|          |              |     |         |     |             |     |     |     | (cid:18) | (cid:19) |      |
|          |              |     |         |     | ∂θ          |     | ∂θ  |     | 1 ∂      | ∂θ       |      |
|          |              |     |         |     | +ReSc(1−Y2) |     |     | =   |          | Y .      | (S1) |
|          |              |     |         |     | ∂T          |     | ∂Z  | Y   | ∂Y       | ∂Y       |      |
Eq. (S1) is the classical Graetz model for an absorbing tube [25, 26]. For our estimations, we use the long and short
| tube limits, | calculations |     | of which | are | reproduced | below | for | completeness. |     |     |     |
| ------------ | ------------ | --- | -------- | --- | ---------- | ----- | --- | ------------- | --- | --- | --- |
The general solution to Eq. (S1) can be written in the form of the following expansion [25, 26],
∞
(cid:88)
|     |     |     |     |     | θ(Y,Z)= |     | A   | e−λ2 | Z eScϕ | (Y), | (S2) |
| --- | --- | --- | --- | --- | ------- | --- | --- | ---- | ------ | ---- | ---- |
|     |     |     |     |     |         |     | n   | nR   | n      |      |      |
n=1
where ϕ n (Y) are radial eigenfunctions and λ n are the corresponding eigenvalues. In the long-tube limit, L≫RReSc,
the first mode dominates and the outlet concentration decays exponentially. The adsorption efficiency can then be
| approximated | as  |     |     |     |      |             |     |          |       |            |      |
| ------------ | --- | --- | --- | --- | ---- | ----------- | --- | -------- | ----- | ---------- | ---- |
|              |     |     |     |     | ϕ(L) |             |     | (cid:18) |       | L (cid:19) |      |
|              |     |     |     |     |      | =1−0.819exp |     | −7.3     |       | ,          | (S3) |
|              |     |     |     |     | ϕ    |             |     |          | RReSc |            |      |
0
where ϕ(L) is the total adsorbed flux until distance L. This limit is appropriate when diffusion has enough time to
| deplete | the odorant | over | the | chamber | length. |     |     |     |     |     |     |
| ------- | ----------- | ---- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
In the entrance-region limit, L ≪ RReSc, adsorption is controlled by a thin concentration boundary layer at the
wall, as has been shown for the thermal boundary layer in the Graetz problem [35]. The boundary-layer thickness,
| nondimensionalized |     | by  | R, scales | as  |     |       |          |                |     |     |      |
| ------------------ | --- | --- | --------- | --- | --- | ----- | -------- | -------------- | --- | --- | ---- |
|                    |     |     |           |     |     |       | (cid:18) | 9Z (cid:19)1/3 |     |     |      |
|                    |     |     |           |     |     | δ(Z)= |          |                | .   |     | (S4) |
2ReSc
| The corresponding |     | concentration |     | profile | is  |            |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | ------- | --- | ---------- | --- | --- | --- | --- | --- |
|                   |     |               |     |         | c   | 1 (cid:90) | η   |     |     | x   |     |
e−γ3
|     |     |     |     |     | =   |        |     | dγ, | η = | ,     | (S5) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ----- | ---- |
|     |     |     |     |     | c   | Γ(4/3) |     |     |     | Rδ(Z) |      |
|     |     |     |     |     | 0   |        | 0   |     |     |       |      |
where x=R−r denotes the distance from the wall. Integrating the wall flux gives
(RReSc)1/3L2/3.
ϕ(L)≈2πDc
0
| Then the | adsorption |     | efficiency | becomes |     |      |          |       |           |     |      |
| -------- | ---------- | --- | ---------- | ------- | --- | ---- | -------- | ----- | --------- | --- | ---- |
|          |            |     |            |         |     |      | (cid:20) |       | (cid:21)2 |     |      |
|          |            |     |            |         |     | ϕ(L) |          | L     | 3         |     |      |
|          |            |     |            |         |     |      | =4       |       | .         |     | (S6) |
|          |            |     |            |         |     | ϕ    |          | RReSc |           |     |      |
0
Acomparisonoftheadsorptionefficiencyunderthelongandshorttubeapproximationswiththenumericalsolution
| of Eq. (S1) | is shown |     | in Fig. S1. |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
πR2u.
Note that the amount of odor flowing into the chamber increases linearly with the flow rate u: ϕ 0 = c 0
Because the adsorption efficiency ϕ(L)/ϕ decreases as u−2/3 (from Eq. (S6)), the absolute adsorption ϕ(L) increases
0
| with flow | rate (Fig. | S5) |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:21)2
|     |     |     |     |     |     |     |     |     | (cid:20) L | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
1
|     |     |     |     |     |     | ϕ(L)=2πνc | 0 [RRe]3 |     |     | .   | (S7) |
| --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --- | --- | ---- |
Sc

14
1.0
0.8
0.6
0.4
0.2
0.0
10 1 100 101 102 103 104
Pe = Re Sc
/
0
low Pe limit
high Pe limit
FIG. S1. Comparison of adsorption efficiency for the long tube (low Pe, Eq. (S3)) and short tube (high Pe, Eq. (S6)) approxi-
mations with numerical results obtained by solving Eq. (S1), for the aquatic chamber geometry (L/R=8.67).
TableS1liststheodorantsusedtocomputethesaturatedadsorptionratesinFig.5. Figure5featurestheabsolute
adsorption,ϕ(L),assumingc isthesaturatedwaterandairconcentrations. Saturatedwaterconcentrationsaretaken
0
from reported water solubilities and saturated air concentrations are computed from reported vapor pressures using
theidealgaslaw. ValuesareobtainedfromPubChem[36]orTheGoodScentsCompany[37]. Toevaluatetheabsolute
adsorption ϕ(L), we make use of the approximations given by Eqs. (S3) and (S6) in air and water, respectively, given
their excellent agreement with the numerical results (Fig. S1). The approximations require L, Re and Sc for each
molecule. Consistent with our experimental results, we choose L = 4.6mm. Reynolds number Re = UR where U
ν
is the maximum fluid velocity inside the olfactory chamber. We choose U to be 3.4mm/s and 14.4mm/s in water
and air, respectively, similar to our simulations using the full geometry. We deliberately choose a non zero value for
aquatic inhalation although the measured value is negligible (Fig. 6a left). This helps us estimate whether, even with
a generous choice for the inhalation speed, aquatic olfaction delivers sufficient odorants to the epithelium. Informed
by the experimental results, we choose R=0.53mm. We choose Sc to be 1 in air and 1000 in water.
S II. SHORT TIME LIMIT OF ADSORPTION INSIDE A CYLINDER FOR AN EPHEMERAL ODOR
SOURCE
Consider an instantaneous point odor source placed at the center of a long cylinder with radius R, represented by
a Dirac delta function. The source contains N moles of odor that are released at time t=0. Since we are interested
0
inthediffusivetransfertowardsthewall, weconsidernoflowinsidethecylinder. ThediffusivityisD andthewallsof
the cylinder are perfectly adsorbing. We are interested in the short-time limit of the cumulative adsorbed odor N(t)
at time t≪ R2.
D
Since axial and radial diffusion are independent and axial diffusion does not affect the probability of reaching the
cylindrical wall, this problem simplifies to adsorption inside a 2D disk. In the absence of the wall, the diffusion
equation has a solution for the two dimensional concentration of odor, c , of the form:
free
c = N 0 e (cid:16) − 4 r D 2 t (cid:17) (S1)
free 4πDt
inside the disk, where r is the radial coordinate.
The fraction of odor lying outside R is then given by
1 (cid:90) ∞ (cid:16) −R2 (cid:17)
2πrc dr =e 4Dt . (S2)
N free
0 R
Eq. (S2) is also the probability P that a freely diffusing particle lies outside the disk at time t. However, since we
free
have a perfectly adsorbing wall, we are interested in the probability of first hitting the wall by time t, P . For a
hit

15
planar wall, an odor particle that has first reached the wall before time t has an equal probability of wandering on
either side of the wall, and being found inside or outside the wall at time t, and thus P =2P . Although the wall
|     |     |     |     |     |     | hit | free |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- |
is curved, at short times diffusion probes only a thin layer near the wall, over which its curvature is negligible and
the wall can be treated as locally planar. Thus we assume this relation to hold. The short time, cumulative adsorbed
| odor N | is then given by |     |         |          |              |     |     |      |
| ------ | ---------------- | --- | ------- | -------- | ------------ | --- | --- | ---- |
|        |                  |     |         | (cid:16) | −R2 (cid:17) |     |     |      |
|        |                  |     | N(t)≈2N | e        | 4Dt .        |     |     | (S3) |
0
as presented in the main text (Eq. (4)). Figure S2 compares this limit with the data presented in Fig. 2.
0.10
Rewater=0.1
R 2
|     |     | 2e( | 4 D t) |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- |
0.08
0.06
N/N 0
0.04
0.02
0.00
|     |     | 0   | 5   | 10  | 15  | 20  | 25  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
time in water (s)
FIG.S2. Comparisonoftheshort-timelimitofadsorptioninsideacylinderwiththenumericalresultsforadsorptionofapulse
| source in | water with Re=0.1. |     |                |           |     |     |     |     |
| --------- | ------------------ | --- | -------------- | --------- | --- | --- | --- | --- |
|           |                    |     | S III. SENSING | TIMESCALE |     |     |     |     |
Here we evaluate how the timescale of detection of an instantaneous release of odor changes as a function of both
the odor concentration at the inlet and the wavelength of the metachronal ciliary waves. In contrast to Sec. S II and
the corresponding discussion in the main text, where detection is set by the cumulative amount of odor adsorbed,
we here adopt a threshold on the instantaneous adsorbed flux. Which of the two is the relevant criterion depends
on how olfactory receptors integrate their input: a flux threshold is arguably the more natural choice if detection is
triggered by the instantaneous rate at which odorant reaches the epithelium rather than by an accumulated dose,
although establishing this for the axolotl remains an open question. Starting from Eq. (S3), the short-time limit for
the adsorbed odor flux for an ephemeral source, ϕ(t) = dN/dt, (not to be confused with the steady-state rate of
| adsorption | ϕ for a permanent | odor source) | is    |                |       |     |     |      |
| ---------- | ----------------- | ------------ | ----- | -------------- | ----- | --- | --- | ---- |
|            |                   |              | N     | t              | R 2   |     |     |      |
|            |                   |              | ϕ(t)≈ | 0 De (−t D ) , | t = . |     |     | (S1) |
|            |                   |              |       | 4 t            | D     |     |     |      |
|            |                   |              | 2     | t 2            | D     |     |     |      |
The flux is not monotonic in time. We therefore define the detection time t∗ as the first time at which ϕ reaches a
threshold ϕ t , that is, the crossing on the rising branch. Equation (S1) cannot be inverted in elementary form, so we
obtain t∗ numerically. We are interested in how t∗ changes when the odor concentration outside the inlet is increased
| by a factor | α, which scales | N and hence | ϕ by the | same factor. |     |     |     |     |
| ----------- | --------------- | ----------- | -------- | ------------ | --- | --- | --- | --- |
0
10−14
To estimate how much detection speeds up at higher concentration, we take a detection threshold of M,
motivated by behavioral measurements in aquatic systems [18]. At this lowest concentration, we can assume that the
detection happens when the total odor flux into the wall ϕ(t) is maximized. Since the adsorbed flux is proportional
to N , which is itself proportional to the concentration near the inlet, this fixes ϕ . Within our panel of represen-
| 0   |     |     |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
10−5 10−1
tative odors, saturated concentrations of water-sensed odorants range from M to M (Table S1), so the

16
17.5
15.0
12.5
10.0
7.5
5.0
2.5
0.0
100 102 104 106 108 1010 1012 1014 1016
concentration ratio
*t/*t
Rewater=0.1
approximation
FIG. S3. Speedup in odor detection from a pulse source, t∗/t∗, when the inlet concentration is increased by a factor α, with
α
detection defined by a threshold on the instantaneous adsorbed flux. The orange curve is the numerical solution with Re =
0.1. The threshold when α=1 is the maximum flux in the numerical solution.
concentration exceeds the detection threshold by a factor α between 109 and 1013. Over this range, Fig. S3 gives a
speedup between 10 and 15. Metachronal pumping contributes a further factor of about 3 at λ/R = 2, consistent
with the main-text results (Fig. 3), so the combined speedup spans roughly 10 without cilia to 45 with them. Taking
the passive baseline as the time to maximum adsorbed flux in water, ∼27 s (Fig. S4), high concentration and ciliary
pumping together bring proximal detection down to between 0.6 s and 2.7 s.
0.014
0.012
0.010
0.008
0.006
0.004
0.002
0.000
0 10 20 30 40 50
time in water (s)
)1
s(
td/)
N/N(d
0
Rewater=0.1
FIG. S4. Total odor flux into the wall of a cylinder in water for an instantaneous odor pulse located at the inlet.

17
|     |     |     | a   |     |     |     |     |     | b   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.50
|     |     |     |      | Sc = 1000 |     |     |     |       | Sc = 1000 |          |     |     |     |     |     |
| --- | --- | --- | ---- | --------- | --- | --- | --- | ----- | --------- | -------- | --- | --- | --- | --- | --- |
|     |     |     | 0.25 |           |     |     |     |       | 1.25      |          |     |     |     |     |     |
|     |     |     | 0.20 | Re = 0.1  |     |     |     |       | 1.00      | Re = 0.1 |     |     |     |     |     |
|     |     | 0   |      | Re = 2.1  |     |     |     | 0cN/N |           | Re = 2.1 |     |     |     |     |     |
N/N
|     |     |     | 0.15 | Re = 10 |     |     |     |     | 0.75 | Re = 10 |     |     |     |     |     |
| --- | --- | --- | ---- | ------- | --- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- | --- |
|     |     |     | 0.10 |         |     |     |     |     | 0.50 |         |     |     |     |     |     |
0.05
0.25
|     |     |     | 0.00 |     |                   |       |     |     | 0.00 |     |                   |       |     |     |     |
| --- | --- | --- | ---- | --- | ----------------- | ----- | --- | --- | ---- | --- | ----------------- | ----- | --- | --- | --- |
|     |     |     | 0    | 10  | 20                | 30 40 | 50  | 60  | 0    | 10  | 20                | 30 40 | 50  | 60  |     |
|     |     |     |      |     | time in water (s) |       |     |     |      |     | time in water (s) |       |     |     |     |
FIG. S5. Adsorption of odor inside a cylinder when the odor concentration at the inlet is fixed to a constant. (a) Adsorption
efficiencyoftotalodor,N/N ,asafunctionoftimeforflowsatdifferentRe(solidlines)atSc=1000. (b)Totaladsorbedodor
0
N, normalizedwithN c0 =C 0 V whereV isthevolumeofthecylinder, asafunctionoftime. Notethathereν andR arekept
| fixed | and | U is varied | to  | achieve | different | Re. |     |     |     |     |     |     |     |     |     |
| ----- | --- | ----------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a Re in water (Sc=1000) b )sm( ria ni 1.0=0 Re in water (Sc=1000) )s( retaw ni 1.0=0
|     |     |     | 0   |     | 0.05 |     | 0.1 |     | 0   |     | 0.05 |     | 0.1 |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
N/N0=0.1
|     |     |     |     |     |     |     |     | 3.0 |     |     |     |     | 30  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.8
|     |     |     |     |     |     |     |     | 2.8 |     |     |     |     | 28  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     | N/  | 0.6 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | 2.6 |     |     |     |     | 26  |     |     |
N
|     |     |     |     |     |     |     |     | N/N ot emit |     |     |     |     |     | N/N ot emit |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | ----------- | --- |
0.4
|     |     |     |     |     |     |     |     | 2.4 |     |     |     |     | 24  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Reopt (theoretical)
|     |     |     | 0.2 |                  |     |     |     |     | 2.2 |                  |     |     | 22  |     |     |
| --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
|     |     |     | 0   |                  | 50  |     | 100 |     | 0   |                  | 50  |     | 100 |     |     |
|     |     |     |     | Re in air (Sc=1) |     |     |     |     |     | Re in air (Sc=1) |     |     |     |     |     |
FIG. S6. Adsorption of an odor pulse located at the inlet of a cylinder. (a) Asymptotic adsorption efficiency N ∞ /N 0 as a
function of Re with the lower axis giving Re in air (Sc = 1) and the upper axis Re in water (Sc = 1000). In water, N ∞ /N 0
achievesamaximumatverylowRe. (b)TimetoreachN/N =0.1ofthetotalodorasafunctionofRe. Evenfortheoptimal
0
| Re, | the time | to reach | N/N | =0.1 | takes | over 20s | in water. |     |     |     |     |     |     |     |     |
| --- | -------- | -------- | --- | ---- | ----- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
0
a time in water (s; Sc=1000) b Re in water (Sc=1000) c Re in water (Sc=1000)
|     |     |     |     |     |     |     | )1  |     |     |     | )1  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 20 40 60 80 100 0 0.05 0.1 s( retaw ni td/)0N/N(d mumixam 0 0.05 0.1
|     |                      |     |                        |     |                       |        | s( ria ni td/)0N/N(d mumixam 140 |                  |     |                       | 0.014 |                  |                  |                |                     |
| --- | -------------------- | --- | ---------------------- | --- | --------------------- | ------ | -------------------------------- | ---------------- | --- | --------------------- | ----- | ---------------- | ---------------- | -------------- | ------------------- |
|     |                      |     |                        |     |                       |        | )1                               |                  |     |                       |       | )sm( ria ni 1    |                  | 25s1 air       |                     |
| )1  | 125                  |     |                        |     |                       | 0.0125 |                                  |                  |     |                       |       | 1.30             |                  | 0.0025s1 water | 13                  |
|     | s( ria ni td/)0N/N(d |     |                        |     |                       |        | s( retaw ni td/)0N/N(d           |                  |     |                       |       |                  |                  |                |                     |
|     |                      |     |                        |     |                       |        | 120                              |                  |     |                       | 0.012 | 1.25             |                  |                | 12.5 )s( emit retaw |
|     | 100                  |     |                        |     |                       | 0.01   |                                  |                  |     |                       |       |                  |                  |                |                     |
|     |                      |     |                        |     |                       |        |                                  |                  |     |                       |       | 1.20             |                  |                | 12                  |
|     | 75                   |     |                        |     |                       | 0.0075 | 100                              |                  |     |                       | 0.01  |                  |                  |                |                     |
|     |                      |     |                        |     |                       |        |                                  |                  |     |                       |       | s52 ot emit 1.15 |                  |                | 11.5                |
|     | 50                   |     |                        |     |                       | 0.005  |                                  |                  |     |                       |       |                  |                  |                |                     |
|     |                      |     |                        |     |                       |        | 80                               |                  |     |                       | 0.008 | 1.10             |                  |                | 11                  |
|     | 25                   |     |                        |     |                       | 0.0025 |                                  |                  |     |                       |       |                  |                  |                |                     |
|     |                      |     |                        |     |                       |        |                                  |                  |     |                       |       | 1.05             |                  |                | 10.5                |
|     | 0                    |     |                        |     |                       | 0      |                                  |                  |     |                       |       |                  |                  |                |                     |
|     | 0                    | 2   | 4                      | 6   | 8                     | 10     |                                  | 0                | 50  | 100                   |       |                  | 0 50             |                | 100                 |
|     |                      |     | time in air (ms; Sc=1) |     |                       |        |                                  | Re in air (Sc=1) |     |                       |       |                  | Re in air (Sc=1) |                |                     |
|     |                      |     |                        |     | Reair=0,Rewater=0     |        | Reair=5,Rewater=0.005            |                  |     | Reair=60,Rewater=0.06 |       |                  |                  |                |                     |
|     |                      |     |                        |     | Reair=1,Rewater=0.001 |        | Reair=30,Rewater=0.03            |                  |     | Reair=100,Rewater=0.1 |       |                  |                  |                |                     |
FIG. S7. Total odor flux into the walls of a cylinder for an instantaneous odor pulse, as a function of Re. (a) Odor flux as
a function of time for different values of Re. (b) Maximum odor flux as a function of Re. The maximum increases with Re,
eventually reaching a peak at an intermediate Re. (c) Time to reach a threshol flux as a function of Re.

18
TABLE S1. Panel of odor molecules used to estimate saturated water and air adsorption rates.
Name Saturatedaqueousconcentration(mol/L) Saturatedgas-phaseconcentration(mol/L) Airorwatersensed
| Ethyltiglate       | 4.71×10−2 | 2.30×10−4 | Air   |
| ------------------ | --------- | --------- | ----- |
| Allyltiglate       | 4.09×10−3 | 6.83×10−5 | Air   |
| Hexyltiglate       | 8.25×10−5 | 8.07×10−6 | Air   |
|                    | 3.34×10−2 | 7.20×10−4 |       |
| Methyltiglate      |           |           | Air   |
| Isopropyltiglate   | 3.50×10−3 | 1.01×10−4 | Air   |
| Citronellyltiglate | 1.62×10−6 | 1.97×10−7 | Air   |
| Benzyltiglate      | 3.25×10−4 | 4.30×10−7 | Air   |
|                    | 3.23×10−4 | 4.19×10−8 |       |
| Phenylethyltiglate |           |           | Air   |
| 2-Ethylhexanal     | 3.12×10−3 | 9.68×10−5 | Air   |
| Benzylacetate      | 2.06×10−2 | 9.14×10−6 | Air   |
| Salicylicacid      | 1.63×10−2 | 4.41×10−9 | Air   |
|                    | 1.27×10−1 | 2.04×10−7 |       |
| Phenylaceticacid   |           |           | Air   |
| 4-Allylanisole     | 1.20×10−3 | 2.69×10−6 | Air   |
| Ethylvalerate      | 1.70×10−2 | 2.55×10−4 | Air   |
|                    | 2.52×10−4 | 1.51×10−5 |       |
| Citronellal        |           |           | Air   |
|                    | 8.65×10−3 | 8.60×10−6 |       |
| (+)-Carvone        |           |           | Air   |
| (−)-Carvone        | 8.65×10−3 | 8.60×10−6 | Air   |
| 2-Methoxypyrazine  | 3.38×10−2 | 2.28×10−4 | Air   |
|                    | 4.93×10−3 | 1.08×10−6 |       |
| Isoeugenol         |           |           | Air   |
| Methylvalerate     | 4.36×10−2 | 9.84×10−4 | Air   |
| Acetophenone       | 5.10×10−2 | 2.10×10−5 | Air   |
| Phenylacetate      | 3.41×10−2 | 2.14×10−5 | Air   |
|                    | 5.71×10−3 | 1.53×10−3 |       |
| Methylbenzene      |           |           | Air   |
| Methylsalicylate   | 4.60×10−3 | 1.61×10−6 | Air   |
| Nonylacetate       | 5.83×10−5 | 1.06×10−5 | Water |
| Octanoicacid       | 6.91×10−3 | 2.00×10−7 | Water |
|                    | 2.50×10−1 | 1.18×10−4 |       |
| Pentanol           |           |           | Water |
| Heptylacetate      | 6.44×10−4 | 2.69×10−5 | Water |
| Hexylacetate       | 4.47×10−3 | 7.10×10−5 | Water |
| Undecanoicacid     | 2.80×10−4 | 8×10−9    | Water |
|                    | 1.23×10−3 | 1.08×10−6 |       |
| Nonanol            |           |           | Water |
| Hexanol            | 5.77×10−2 | 4.95×10−5 | Water |
| Decanoicacid       | 3.59×10−4 | 1.97×10−8 | Water |
| Decanol            | 2.34×10−4 | 4.58×10−7 | Water |
|                    | 1.94×10−4 | 2.15×10−5 |       |
| Octylacetate       |           |           | Water |
| Heptanoicacid      | 1.86×10−2 | 5.38×10−7 | Water |
| Decylacetate       | 1.76×10−5 | 1.87×10−7 | Water |
| Heptanol           | 1.44×10−2 | 1.13×10−5 | Water |
|                    | 8.53×10−1 | 3.76×10−4 |       |
| Butanol            |           |           | Water |
| Nonanoicacid       | 1.79×10−3 | 8.87×10−8 | Water |
| Hexanoicacid       | 8.87×10−2 | 2.15×10−6 | Water |
| Ethylpropionate    | 1.88×10−1 | 1.93×10−3 | Water |
|                    | 1.85×10−1 | 1.93×10−3 |       |
| Propylacetate      |           |           | Water |
| Isobutylpropionate | 8.22×10−3 | 3.92×10−4 | Water |
| Allylbutyrate      | 9.62×10−3 | 2.39×10−4 | Water |
| Methylpropionate   | 7.08×10−1 | 4.52×10−3 | Water |
|                    | 1.33×10−2 | 1.88×10−4 |       |
| Pentylacetate      |           |           | Water |
| Valericacid        | 2.35×10−1 | 1.02×10−5 | Water |
| Octanal            | 4.37×10−3 | 6.35×10−5 | Water |
| 2-Hexanone         | 1.72×10−1 | 6.24×10−4 | Water |
|                    | 1.47×10−1 | 1.74×10−3 |       |
| Methylbutyrate     |           |           | Water |
| 2-Heptanone        | 3.75×10−2 | 2.07×10−4 | Water |
| Butylacetate       | 7.17×10−2 | 6.18×10−4 | Water |
|                    | 1.36×10−1 | 1.40×10−3 |       |
| Valeraldehyde      |           |           | Water |
|                    | 1.54×10−2 | 2.70×10−4 |       |
| Isoamylacetate     |           |           | Water |
---- END DOCUMENT ----
