Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Journal Name
|     |     |     |     | Elongation |           | suppresses |                    |     | rheotaxis |            | and      | enables  |             | microfluidic |     |
| --- | --- | --- | --- | ---------- | --------- | ---------- | ------------------ | --- | --------- | ---------- | -------- | -------- | ----------- | ------------ | --- |
|     |     |     |     | enrichment |           | of         | β-lactam-resistant |     |           |            | bacteria |          |             |              |     |
|     |     |     |     | Tao,a      |           |            | Esteves,b          |     | Zhu,b     |            |          |          | Mathijssena |              |     |
|     |     |     |     | Ran        | Nathaniel | C.         |                    | Jay |           | and Arnold |          | J. T. M. |             |              |     |
6202 guA 91  ]hp-oib.scisyhp[  1v77091.8062:viXra
|     |     |     |     | Accepted | for publication |     | in  | Lab on | a Chip. |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --------------- | --- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
Antimicrobial resistance (AMR) complicates the treatment of diseases including lung and urinary
tract infections (UTIs), which are among the most common bacterial infections worldwide. Motile
pathogens can use rheotaxis to swim upstream against fluid flows, potentially promoting access
to upper regions of anatomical tracts. However, it remains unclear how antibiotic exposure and
resistanceinfluencethistransportprocess. Here,usingsingle-celltrackingmicroscopy,weinvestigate
howelongationinducedbyβ-lactamantibioticsaffectstherheotacticmigrationofE.coliinconfined
microfluidic channels. Remarkably, we find that rheotaxis can be inhibited 100-fold by antibiotics,
even if the susceptible elongated cells remain fully motile. However, resistant bacteria remain short
andretainupstreammigrationunderthesameconditions. Usinggeneticallyengineeredbacteriawith
tunable cell length, we show that the underlying mechanism that governs rheotaxis is the coupling
between cell morphology and flow vorticity, where elongated cells are rapidly rotated downstream.
Finally, we exploit this length-dependent transport difference to separate short and elongated cells
under flow and enrich ampicillin-resistant cells from mixed populations. Together, these results
establish bacterial elongation as a key control parameter for rheotactic transport, and provide a
proof-of-concept strategy for enriching β-lactam-resistant bacteria for potential use in rapid AMR
detection.
Introduction
polymerspresentinmucusandbiofilmmatrices17,18.
Escherichia
Antimicrobialresistance(AMR)isamajorglobalhealthchallenge coli, the predominant causative agent of UTIs4, exhibits strong
that threatens the effective treatment of bacterial infections1–3. positiverheotaxis,highlightingbacterialmotilityasanimportant
Among these, urinary tract infections (UTIs) are particularly factorinpathogenesis14,19,20.
| prevalent                                          | and often | recur despite | antibiotic | therapy4.      |     | Although  |     |           |              |          |             |            |         |                 |             |
| -------------------------------------------------- | --------- | ------------- | ---------- | -------------- | --- | --------- | --- | --------- | ------------ | -------- | ----------- | ---------- | ------- | --------------- | ----------- |
|                                                    |           |               |            |                |     |           |     | β-lactam  | antibiotics, |          | including   | cephalexin |         | and ampicillin, | are         |
| substantial                                        | progress  | has been      | made       | in identifying | the | molecular |     |           |              |          |             |            |         |                 |             |
|                                                    |           |               |            |                |     |           |     | commonly  | used         | to treat | susceptible |            | E. coli | infections      | and inhibit |
| mechanismsunderlyingAMR,muchlessisknownabouthowre- |           |               |            |                |     |           |     |           |              |          |             |            |         | 2A)21,22.       |             |
|                                                    |           |               |            |                |     |           |     | cell-wall | synthesis    | and      | cell        | division   | (Fig.   |                 | However,    |
sistanceinfluencesthebiophysicalprocessesthatbacteriauseto
|     |     |     |     |     |     |     |     | drug concentrations |     |     | in the | urine can | drop | below | the minimum |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------ | --------- | ---- | ----- | ----------- |
establishandmaintaininfections,especiallyinanatomicaltracts treatment23.
|     |     |     |     |     |     |     |     | inhibitory | concentration |     | (MIC) | within | hours | after |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ----- | ------ | ----- | ----- | --- |
subjecttofluidflows5–9.
|     |     |     |     |     |     |     |     | Under | some | sub-MIC | β-lactam | conditions, |     | susceptible | bacteria |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------- | -------- | ----------- | --- | ----------- | -------- |
A key mechanism that drives infections in such environments cancontinuegrowingandundergofilamentouselongationrather
| is rheotaxis, | the | directed movement |     | of motile | microorganisms |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------------- | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thanbeingkilled,whileretainingmotility24–28.
againstfluidflow10–15.Intheurinarytract,whereurineflowtyp-
|     |     |     |     |     |     |     |     | Despite | the | clinical | importance |     | of AMR | and rheotaxis, | their |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | ---------- | --- | ------ | -------------- | ----- |
icallyservesasaprotectivebarrier,rheotaxisenablesbacteriato
|     |     |     |     |     |     |     |     | interplay | remains | largely |     | unexplored. | Previous |     | studies have |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------- | --- | ----------- | -------- | --- | ------------ |
ascendthetractandreachupstreamregionssuchasthebladder
|     |     |     |     |     |     |     |     | shown | that antibiotics |     | can | alter bacterial |     | metabolism, | growth, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | --- | --------------- | --- | ----------- | ------- |
andkidneys4,16.Thisbehaviorhasbeenattributedtoa“weather-
|     |     |     |     |     |     |     |     | and swimming |     | behaviors21,25,26,28,29. |     |     | However, | it  | remains un- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------------ | --- | --- | -------- | --- | ----------- |
vaneeffect,”inwhichtheflagellarbundlereorientsdownstream,
clearwhetherresistanceaffectstheabilityofbacteriatomigrate
aligningcellsagainsttheflow10,13.Rheotaxiscanbeenhancedby
|             |            |              |            |                  |               |     |     | upstream   | against   | currents   |                 | and thereby | persist       | in    | flow environ-  |
| ----------- | ---------- | ------------ | ---------- | ---------------- | ------------- | --- | --- | ---------- | --------- | ---------- | --------------- | ----------- | ------------- | ----- | -------------- |
|             |            |              |            |                  |               |     |     | ments      | during    | antibiotic | treatment.      |             | Understanding |       | this relation- |
|             |            |              |            |                  |               |     |     | ship is    | essential | for        | fully assessing |             | the risks     | posed | by resistant   |
| aDepartment | of Physics | & Astronomy, | University | of Pennsylvania, | Philadelphia, |     | PA  | pathogens. |           |            |                 |             |               |       |                |
19104,USA;E-mail:amaths@upenn.edu.
Here,usingasimplifiedbiophysicalmodelinspiredbyconfined
b PerelmanSchoolofMedicine,UniversityofPennsylvania,Philadelphia,PA19104,
USA;junzhu@pennmedicine.upenn.edu. flows in the urinary tract, we investigate how β-lactam-induced
Journal Name, [year], [vol.],1–13
|1

elongation affects the upstream migration of E. coli (Fig. 1). By encesincelllengthtoastage-resolvedtransportmechanismand
tracking thousands of individual bacteria, we quantify bacterial finallytoflow-mediatedenrichment. Figure1Fillustratesapos-
upstream migration and resolve the transport dynamics of indi- sible future extension in which enriched cells could be counted
vidual cells under flow. We first show that antibiotic-susceptible withoutmicroscopyusingimpedancecytometryandsubsequently
cells elongate under β-lactam exposure while retaining swim- analyzedbysequencingorothermolecularmethods40–42. These
ming speeds comparable to untreated cells, yet exhibit strongly downstream readout and identification steps remain conceptual
reduced upstream migration through microstructured environ- andwerenotintegratedintothepresentstudy.
| ments.                                                | In contrast, | resistant | strains | retain | a   | short morphology |     |     |     |     |     |     |     |     |
| ----------------------------------------------------- | ------------ | --------- | ------- | ------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| andpreserveupstreammigrationunderantibiotictreatment. |              |           |         |        |     |                  | To  |     |     |     |     |     |     |     |
Antibioticsinduceelongationwithoutimpairingmotility
isolatetheroleofcelllengthfromotherantibiotic-inducedphys-
|           |          |     |                   |     |            |     |             | To quantify | antibiotic-induced |     | changes | in  | cell length | and motil- |
| --------- | -------- | --- | ----------------- | --- | ---------- | --- | ----------- | ----------- | ------------------ | --- | ------- | --- | ----------- | ---------- |
| iological | changes, | we  | use a genetically |     | engineered |     | strain with |             |                    |     |         |     |             |            |
ity, weexposedwild-typeK-12E.colitotheβ-lactamantibiotics
| inducible  | elongation  | and | demonstrate |            | that elongation |     | alone is   |                          |     |     |                                 |     |     |     |
| ---------- | ----------- | --- | ----------- | ---------- | --------------- | --- | ---------- | ------------------------ | --- | --- | ------------------------------- | --- | --- | --- |
|            |             |     |             |            |                 |     |            | cephalexinandampicillin. |     |     | Wemeasuredcelllengthaftergrowth |     |     |     |
| sufficient | to suppress |     | upstream    | transport. | Finally,        |     | we exploit |                          |     |     |                                 |     |     |     |
innutrient-richmediumwithandwithoutantibioticsandquanti-
thislength-dependentrheotacticresponsetodemonstrateproof-
fiedswimmingspeedafterresuspensioninBerg’smotilitybuffer.
of-conceptmicrofluidicseparationandenrichmentofampicillin-
Representativeschematicsofcellmorphologyundereachcondi-
| resistant | cells from | mixed | populations. |     | Together, | these | results |     |     |     |     |     |     |     |
| --------- | ---------- | ----- | ------------ | --- | --------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
tionareshowninFig.2B,withcelllengthsquantifiedinFig.2C.
| establish | a direct | link | between | bacterial | morphology |     | under an- |     |     |     |     |     |     |     |
| --------- | -------- | ---- | ------- | --------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Wild-typeE.colicellshaveanaveragecellbodylengthof2µm
tibioticstressandmicrobialtransportdynamicsinflow30–33.
|     |     |     |     |     |     |     |     | to 3µm during | their | exponential |     | growth | phase. | Treatment of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ----------- | --- | ------ | ------ | ------------ |
Results susceptiblecellswithcephalexin-orampicillin-supplementedTB
mediumfor2hinhibitedcelldivisionandincreasedtheaverage
Conceptualandexperimentalframework cell length to approximately 9µm (Fig. 2C; Fig. S1D, G), consis-
|     |     |     |     |     |     |     |     | tentwithpreviousobservations25,26. |     |     |     | Toisolatetheeffectofcell |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ------------------------ | --- | --- |
Figure1summarizesourinvestigationofhowantibiotic-induced
changes in cell length affect upstream transport and illustrates length from other antibiotic-induced physiological changes, we
|           |        |               |     |        |         |        |           | used a genetically |     | engineered | strain | with | tunable cell | length34. |
| --------- | ------ | ------------- | --- | ------ | ------- | ------ | --------- | ------------------ | --- | ---------- | ------ | ---- | ------------ | --------- |
| potential | future | applications. |     | In the | urinary | tract, | bacterial |                    |     |            |        |      |              |           |
rheotaxis may support upstream migration against urine flow, Inthisstrain,elongationisdirectlycontrolledthrougharabinose-
|     |     |     |     |     |     |     |     | inducible expression |     | of SulA | from | the P | promoter. | SulA se- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------- | ---- | ----- | --------- | -------- |
while oral treatment with β-lactam antibiotics exposes suscep- BAD
tiblecellstoconditionsthatcaninhibitdivisionandinduceelon- questers FtsZ and inhibits septum formation, thereby blocking
gation4,16,21–23 cell division43. This engineered strain reached lengths similar
|     |     | (Fig. 1A, | B). This | clinical | context | leads | us to in- |             |                    |     |       |       |                   |        |
| --- | --- | --------- | -------- | -------- | ------- | ----- | --------- | ----------- | ------------------ | --- | ----- | ----- | ----------------- | ------ |
|     |     |           |          |          |         |       |           | to those of | antibiotic-treated |     | cells | (Fig. | 2C). In contrast, | resis- |
vestigatehowantibiotic-inducedelongationaltersbacterialtrans-
port under controlled flow conditions. We first establish the tant strains retained their ability to divide and remained short
|                      |     |             |     |         |        |       |          | under antibiotic | treatment. |     | An  | independent | phenotypic | growth |
| -------------------- | --- | ----------- | --- | ------- | ------ | ----- | -------- | ---------------- | ---------- | --- | --- | ----------- | ---------- | ------ |
| antibiotic-dependent |     | differences |     | in cell | length | among | the pop- |                  |            |     |     |             |            |        |
ulations used in this study: untreated wild-type cells remain assay further confirmed that the susceptible strain showed no
|                               |     |     |       |          |       |          |     | detectable growth |     | at ampicillin |     | concentrations | of 16µgmL−1 | or  |
| ----------------------------- | --- | --- | ----- | -------- | ----- | -------- | --- | ----------------- | --- | ------------- | --- | -------------- | ----------- | --- |
| short, antibiotic-susceptible |     |     | cells | elongate | under | β-lactam | ex- |                   |     |               |     |                |             |     |
posure, and antibiotic-resistant cells remain short under treat- higher, whereas the resistant strain maintained growth through
512µgmL−1(Fig.S1J,K).
| ment (Figs. | 1C  | and 2C). | We next | compare | short | and | elongated |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------- | ------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
cellsunderidenticalimposed-flowconditions. Shortcellssustain Subsequently, bacterial swimming speeds for each condition
|              |          |     |         |         |           |       |         | were measured | by  | tracking | individual |     | cells after | resuspension |
| ------------ | -------- | --- | ------- | ------- | --------- | ----- | ------- | ------------- | --- | -------- | ---------- | --- | ----------- | ------------ |
| near-surface | upstream |     | motion, | whereas | elongated | cells | undergo |               |     |          |            |     |             |              |
more frequent flow-induced reorientation, surface detachment, in Berg’s motility buffer and calculating the trajectory-averaged
swimmingspeedfortrajectorieslastinglongerthan1s(Fig.2D;
anddownstreamadvection(Fig.1D).Todeterminewhethercell
lengthaloneissufficienttoaccountforthislossofupstreamtrans- Fig. S1E, H). Despite the differences in cell length, swimming
port,weuseageneticallyengineeredstrainwithinducibleelon- speeds remained comparable across conditions, indicating that
gation34. Thissystemallowsustoisolatetheeffectofcelllength elongation did not substantially reduce swimming speed under
fromotherantibiotic-inducedchangesandquantifyhowelonga- thetestedconditions,consistentwithpreviousstudies25,44.
| tion alters | the breakout, |     | propagation, |     | and infiltration |     | stages of |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | ------------ | --- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
upstreaminvasion(Fig.3).
|     |     |     |     |     |     |     |     | Antibiotics | suppress | upstream |     | migration | in susceptible | but |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | --- | --------- | -------------- | --- |
We next test whether this length-dependent transport differ- notresistantcells
ence can be used for cell separation. In mixed populations of To study upstream migration in a controlled confined-flow envi-
short and elongated cells, short cells progressively accumulate ronment inspired by the urinary tract, we fabricated a microflu-
upstream, whereaselongatedcellsremainpredominantlydown- idic device consisting of two reservoirs connected by a straight
stream.Wethenapplythesameprincipletomixedpopulationsof channelofwidthW =50µmanddepthH=10µm(Fig.2E).The
ampicillin-resistantandampicillin-susceptiblecells,enrichingthe
downstreamreservoirrepresentsregionscontaminatedwithbac-
resistant population through rheotactic transport (Fig. 1E). This teria, such as theopening of the urinary tractor a catheter bag,
approachcomplementsbroadereffortstousemicrofluidictrans-
whereastheupstreamreservoirrepresentssterileregions,suchas
portandphysicalcellpropertiesforbacterialseparation35–39.
thebladderorkidneys.
Thus, the study progresses from antibiotic-dependent differ- First, under the antibiotic-free control condition, nutrient-rich
Journal Name, [year], [vol.],1–13
2|

TBmediumwasflushedthroughthedevicewhilewild-typeE.coli zerobreakoutprobabilityacrossthetestedflowconditions. Their
cells were introduced into the downstream reservoir. Under im- largeraspectratioincreasestheirsusceptibilitytosurfacedetach-
posedflow,thebacteriareadilymigratedupstreamandaccumu- mentinregionswithhighstreamlinecurvaturenearthechannel
lated in the upstream reservoir (Fig. 2F, green), consistent with entrances, resultinginnear-zerobreakoutprobabilitiesforelon-
| previousreports12,19.Thefirstinvadingcelltypicallyreachedthe |     |     |     |     |     |     |     | gatedbacteria. |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
upstreamreservoirwithin60saftertraversingthe2000µmchan-
| nel against       | the imposed |                    | flow (Fig. | S2A, | B). During          | the | course |        |                 |     |       |      |           |         |            |
| ----------------- | ----------- | ------------------ | ---------- | ---- | ------------------- | --- | ------ | ------ | --------------- | --- | ----- | ---- | --------- | ------- | ---------- |
|                   |             |                    |            |      |                     |     |        | During | the propagation |     | stage | (II) | (Fig. 3E, | F; Fig. | S4), wild- |
| oftheexperiments, |             | eachlastingupto8h, |            |      | thecellscontinuedto |     |        |        |                 |     |       |      |           |         |            |
typecellsswamupstreamalongthechanneledgesbutweread-
growanddivideinthepresenceofnutrients,leadingtoapersis-
|     |     |     |     |     |     |     |     | vected downstream |     | when | they | detached | from | the | surfaces and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | ---- | -------- | ---- | --- | ------------ |
tent flux of bacteria moving upstream. Consequently, cells pro- moved into the faster flows near the channel centerline. At
| gressively | accumulated | in  | the upstream |     | reservoir | (Fig. S2C). | All |            |        |     |          |          |     |           |          |
| ---------- | ----------- | --- | ------------ | --- | --------- | ----------- | --- | ---------- | ------ | --- | -------- | -------- | --- | --------- | -------- |
|            |             |     |              |     |           |             |     | weak shear | rates, | the | upstream | swimming |     | distances | exceeded |
bacteria within the channel and the upstream reservoir consis- the downstream drift, resulting in net upstream migration. At
tentlyexhibitedashortmorphology.
strongershear,detachmenteventsdominatedandwild-typecells
To mimic infection treatment with antibiotic exposure, we were carried downstream. In contrast, elongated cells spent lit-
| flushed the | microfluidic | device | with | TB  | medium | supplemented |     |               |     |        |          |          |     |          |            |
| ----------- | ------------ | ------ | ---- | --- | ------ | ------------ | --- | ------------- | --- | ------ | -------- | -------- | --- | -------- | ---------- |
|             |              |        |      |     |        |              |     | tle time near | the | edges, | detached | rapidly, |     | and were | frequently |
with cephalexin (Fig. 2F, magenta) or ampicillin (red). Un- advected downstream. Even under weak flow conditions, they
derbothantibioticconditions,upstreammigrationbysusceptible
|     |     |     |     |     |     |     |     | exhibited | net downstream |     | velocities, |     | and at | stronger | flows they |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ----------- | --- | ------ | -------- | ---------- |
cellswasstronglysuppressed. Duringthefirst30minofantibiotic accumulatednearthechannelcenterline,wheretheyweretrans-
| exposure, | some cells | remained | short      | and    | were able | to reach     | the |                   |     |        |      |           |     |        |             |
| --------- | ---------- | -------- | ---------- | ------ | --------- | ------------ | --- | ----------------- | --- | ------ | ---- | --------- | --- | ------ | ----------- |
|           |            |          |            |        |           |              |     | ported downstream |     | faster | than | wild-type |     | cells. | We compared |
| upstream  | reservoir. | As the   | antibiotic | effect | became    | established, |     |                   |     |        |      |           |     |        |             |
theseexperimentswithathree-dimensionalrheotaxismodelthat
thecellselongatedandtheupstreammigrationprogressivelyde- describesbacterialmotioninthinrectangularmicrofluidicchan-
creaseduntilitwascompletelyabolished(Fig.S2D–F).Mostsus-
|     |     |     |     |     |     |     |     | nels (Fig. | 3E; Notes | S8  | and | S9). In | the model, | short | and elon- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --- | ------- | ---------- | ----- | --------- |
ceptiblecellswithinthedeviceshowedelongatedmorphologies. gatedcellsweresimulatedunderidenticalconditions,exceptthat
High-magnification inspection of the upstream reservoir after the cell-body aspect ratio was increased from the wild-type-like
8hrevealedadensebacterialaccumulationundertheantibiotic- rangeΓ=2–4totheelongatedrangeΓ=8–10. Thesimulations
free condition (green), while the accumulation was approxi- reproduced the qualitative features of the experimental trajec-
mately 100-fold reduced when wild-type (susceptible) bacte- tories: short cells maintained stable edge-following motion and
| ria were | exposed | to cephalexin |     | (magenta) | or  | ampicillin | (red) |                                 |     |     |     |                          |     |     |     |
| -------- | ------- | ------------- | --- | --------- | --- | ---------- | ----- | ------------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- |
|          |         |               |     |           |     |            |       | achievednetupstreampropagation, |     |     |     | whereaselongatedcellsde- |     |     |     |
(Fig. 2G, H). In contrast, ampicillin-resistant cells (yellow) tached more frequently from the channel edges and were ad-
| retained | a short morphology |     | under | ampicillin |     | treatment | and |                   |     |                                       |     |     |     |     |     |
| -------- | ------------------ | --- | ----- | ---------- | --- | --------- | --- | ----------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
|          |                    |     |       |            |     |           |     | vecteddownstream. |     | Bycomputingtheensemble-averagedlongi- |     |     |     |     |     |
showedunhinderedupstreammigration. tudinalvelocity⟨Vx⟩asafunctionofflowstrength,wefoundthat
themodel(Fig.3,lines)capturestheexperimentallyobserveddif-
ferences(Fig.3,points),withshortcellsexhibitingnetupstream
Cellelongationimpairsallstagesofupstreaminvasion
migrationandelongatedcellsundergoingdownstreamtransport.
Inseparateexperiments,shortwild-typecellsandgeneticallyen-
|                |      |         |            |      |            |     |          | The agreement |     | between | experiments |     | and | simulations | supports |
| -------------- | ---- | ------- | ---------- | ---- | ---------- | --- | -------- | ------------- | --- | ------- | ----------- | --- | --- | ----------- | -------- |
| gineered cells | with | induced | elongation | were | inoculated |     | into the |               |     |         |             |     |     |             |          |
theconclusionthatcellelongationalone,throughenhancedsen-
downstreamreservoir,whileasteadyflowofmotilitybufferwas
sitivitytolocalshearandvorticity,issufficienttoimpairupstream
applied(Fig.3A).Undertheseconditions,shortcellsconsistently
propagationduringmigration.
| migrated        | upstream | and accumulated |           | in  | the upstream | reservoir, |     |     |     |     |     |     |     |     |     |
| --------------- | -------- | --------------- | --------- | --- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| while elongated | cells    | did             | not reach | the | upstream     | reservoir  | and |     |     |     |     |     |     |     |     |
remainedtrappednearthedownstreamentrance(Fig.3B). During the final infiltration stage (III) (Fig. 3G, H; Fig. S5),
wild-typecellscrossedthecurvedstreamlinesatthechannelexit
Toresolvethisupstreaminvasionprocessinmoredetail,wede-
composeditintothreestages: (I)breakoutfromthedownstream andsuccessfullyenteredtheupstreamreservoir.Incontrast,elon-
|            |                  |     |          |         |        |           |     | gated cells | exhibited | near-zero |     | infiltration | probability |     | across the |
| ---------- | ---------------- | --- | -------- | ------- | ------ | --------- | --- | ----------- | --------- | --------- | --- | ------------ | ----------- | --- | ---------- |
| reservoir, | (II) propagation |     | upstream | through | narrow | channels, |     |             |           |           |     |              |             |     |            |
and(III)infiltrationintotheupstreamreservoir(Fig.3A).Wein- tested flow conditions, consistent with their inability to escape
fromdownstreamopeningsinthefirststage.
troducedthisthree-stageframeworkanddevicegeometryinour
| previouswork19. | Here,weusetheframeworktodeterminehow |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cellelongationmodifieseachtransportstage. Wethereforequan- Together(I,II,III),theseresultsdemonstratethatcellelonga-
tifiedstage-specifictransportmetricsasfunctionsofflowstrength tionsuppressesupstreammigrationacrossallthreestagesofthe
(Vmax)andcelllength(L): breakoutprobability,meanlongitudi- invasionprocess. Elongatedcellsshowincreasedsensitivitytolo-
nalpropagationvelocity,andinfiltrationprobability. calvorticity(ωωω=∇∇∇×vvv),particularlynearchannelentrances,ex-
During the breakout stage (I) (Fig. 3C, D; Fig. S3), wild-type its,andboundingsurfaces. Frequentdetachmentfromthechan-
cellswereabletoenterthechannelmouth. Asexpected, break- neledgespreventselongatedcellsfromsustainingupstreammi-
out events became less frequent under stronger flows, although gration,therebyreducingtheirabilitytoreachupstreamregions.
occasional successes occurred when multiple cells accumulated Incontrast,shortcellsmaintainstableedge-followingtrajectories
near the entrance. In contrast, elongated cells exhibited near- andeffectiverheotaxis.
Journal Name, [year], [vol.],1–13
|3

Rheotaxis-driven separation of bacterial populations by cell frommixedsamples.
length
This finding, that bacterial cell length strongly influences their Rheotaxis-basedenrichmentofampicillin-resistantcells
upstream swimming performance, can be exploited for cell sep- The separation of short and elongated cells suggested that
| aration under | flow. | To  | test this | prediction, | we  | mixed | short cells |     |     |     |     |     |     |     |
| ------------- | ----- | --- | --------- | ----------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
antibiotic-dependentdifferencesincelllengthcouldbeexploited
| (green)    | and elongated  |           | cells (blue)    | and | introduced       | the | popula-     |                 |                      |          |              |            |            |        |
| ---------- | -------------- | --------- | --------------- | --- | ---------------- | --- | ----------- | --------------- | -------------------- | -------- | ------------ | ---------- | ---------- | ------ |
|            |                |           |                 |     |                  |     |             | to enrich       | resistant cells from | mixed    | populations  |            | (Fig. 5A). | Fig-   |
| tion into  | the downstream |           | reservoir       | of  | the microfluidic |     | device      |                 |                      |          |              |            |            |        |
|            |                |           |                 |     |                  |     |             | ure 5A combines | the experimentally   |          | demonstrated |            | ampicillin |        |
| (Fig. 4A). | Over           | time, the | two populations |     | spatially        |     | segregated. |                 |                      |          |              |            |            |        |
|            |                |           |                 |     |                  |     |             | proof of        | concept with several | possible | future       | extensions |            | of the |
Short cells efficiently migrated through the channel and accu- platform. In the present study, we tested only mixed ampicillin-
| mulated | in the | upstream | reservoir. | In  | contrast, | elongated | cells |     |     |     |     |     |     |     |
| ------- | ------ | -------- | ---------- | --- | --------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
resistantandampicillin-susceptibleE.colipopulationsafterexpo-
did not propagate beyond the channel entrance and remained suretoampicillin. Patient-derivedsamples,paralleltestingunder
trappednearthedownstreamopening,wheretheygraduallyac-
multipleantibioticconditions,impedance-cytometryreadout,and
cumulated. downstreamsequencingareshownasconceptualextensionsand
This separation is robust and reproducible, arising from fun- werenotintegratedintothecurrentstudy.
damentaldifferencesinhowcelllengthinteractswithshearflow To demonstrate this enrichment principle experimentally, we
| andchannelgeometry. |     |     | Shortcellsmaintainstableedge-following |     |     |     |     |          |                         |        |          |      |             |     |
| ------------------- | --- | --- | -------------------------------------- | --- | --- | --- | --- | -------- | ----------------------- | ------ | -------- | ---- | ----------- | --- |
|                     |     |     |                                        |     |     |     |     | cultured | an ampicillin-resistant | strain | together | with | a wild-type |     |
trajectories and resist detachment from channel walls, whereas susceptiblestraininanampicillin-supplementedTBmedium. Af-
| elongated | cells | detach | more readily |     | and are | advected | down- |     |     |     |     |     |     |     |
| --------- | ----- | ------ | ------------ | --- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
terapproximately2hofantibioticexposure,themixturewassus-
stream, preventing sustained upstream migration. The imposed pended in motility buffer before introducing it into the down-
flowthereforeactsasahydrodynamicselectorthatpartitionscells
|     |     |     |     |     |     |     |     | stream reservoir | of the microfluidic |     | device | (Fig. | 5B). During | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------------- | --- | ------ | ----- | ----------- | --- |
accordingtotheirlength-dependentrheotacticbehavior35–39.
subsequent30minmicrofluidicselectionstep,resistantcells(yel-
To confirm that this separation arises from flow-driven ef- low) migrated into the upstream reservoir, whereas susceptible
fects rather than geometric features of channel openings, we elongated cells remained trapped downstream (Fig. S8A). Con-
performed control experiments in which both short and elon- sistentwiththisseparation,95%ofthecellsaccumulatinginthe
gated cells were introduced into the microfluidic device in the upstream reservoir were shorter than 4.6µm (Fig. S8B), indicat-
ingstrongenrichmentoftheshort-cellpopulation.
| absence | of flow | (Fig. | S6A). Under | these | conditions, |     | cells re- |     |     |     |     |     |     |     |
| ------- | ------- | ----- | ----------- | ----- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
maineduniformlydistributedwithoutpreferentialaccumulation, Toevaluateenrichmentperformance,wepreparedmixedpop-
demonstratingthattheobservedseparationisdrivenbyrheotaxis
|     |     |     |     |     |     |     |     | ulations with | initial resistant-cell | fractions |     | of 1%, | 10%, and | 50% |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------------------- | --------- | --- | ------ | -------- | --- |
rather than intrinsic differences in motility or passive transport and quantified the cells accumulating in the upstream reservoir
(Fig.S6B,C).
|     |     |     |     |     |     |     |     | during a | 30min selection | period (Fig. | 5C; | Supplementary |     | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ------------ | --- | ------------- | --- | ---- |
To further demonstrate that the enriched short-cell popula- S6). In all three conditions, the total number of cells in the up-
tion can be physically collected, we modified the microfluidic stream reservoir increased over time. The number of resistant
design by adding a lateral outlet channel connected to the up- cells accumulating upstream increased with the initial resistant-
cellabundance,whereasrelativelyfewsusceptibleelongatedcells
| stream reservoir |     | (Fig. S7A). | In this | configuration, |     | cells | reaching |     |     |     |     |     |     |     |
| ---------------- | --- | ----------- | ------- | -------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
theupstreamreservoirareredirectedintothelateraloutletchan- reachedtheupstreamreservoir. Consequently,thefractionofre-
sistantcellsincreasedintheupstreampopulation,evenwhenre-
| nel by the | imposed | flow | for collection. |     | When | mixed | short and |     |     |     |     |     |     |     |
| ---------- | ------- | ---- | --------------- | --- | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
elongated cells were introduced into the downstream reservoir, sistantcellswereinitiallyrare. At30min,wequantifiedresistant
short cells migrated upstream through the device, accumulated and susceptible cell counts in the upstream reservoir and calcu-
intheupstreamreservoirinminutes,andweresubsequentlyredi- latedthecorrespondingresistant-cellfractionforeachinputcom-
rectedintothelateraloutletchannel(Fig.S7B).Incontrast,elon- position. Thesemeasurementsdemonstratereproducibleenrich-
gatedcellsremainedpredominantlynearthedownstreamreser- ment across all tested input compositions. For each input com-
voir. This collection process persisted throughout the duration position, n=3 independent experiments were performed using
of the experiment (1h), showing that upstream-migration-based separatesamplespreparedondifferentdays.
enrichment can be directly coupled to physical cell collection. Together,theseresultsestablishaproof-of-conceptmicrofluidic
Thus,thedeviceenablesthephysicalcollectionoftheupstream- enrichment strategy. The approximately 30min timescale refers
enrichedshort-cellpopulation,whichcouldsupportfuturedown- specificallytothemicrofluidicselectionstepfollowingantibiotic
streamcultureormolecularanalysis. exposure. The present experiments quantify enrichment by flu-
In the context of antimicrobial resistance, this separation of orescence microscopy. Future implementations could integrate
shortandlongcellshighlightsanimportantdistinction: resistant impedancecytometryformicroscopy-freecellcountingandcou-
strains retain short morphology under antibiotic treatment and ple the enriched population to sequencing or other molecular
analyses.
| therefore | continue | to migrate | upstream |     | and reach | upstream | re- |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | -------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
gions. Incontrast,susceptiblestrainselongateandarephysically
Conclusions
| excludedfromupstreamregions. |     |     |     | Thishydrodynamicsegregation |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
notonlyunderscorestherisksassociatedwithantimicrobialresis- Our study establishes a direct link between antibiotic-induced
tance,butalsosuggestsastrategytoenrichresistantpopulations cell elongation and the ability of bacteria to migrate upstream
Journal Name, [year], [vol.],1–13
4|

againstflows. Bycombiningmicrobiologyexperiments,microflu- andmotivateintegrationwithdownstreamphenotypicormolec-
| idic environments, |     | and         | computational |         | analysis, | we  | show that   | ularreadouts. |             |           |     |            |      |          |
| ------------------ | --- | ----------- | ------------- | ------- | --------- | --- | ----------- | ------------- | ----------- | --------- | --- | ---------- | ---- | -------- |
| β-lactam-exposed   |     | susceptible |               | E. coli | elongate  | and | become more |               |             |           |     |            |      |          |
|                    |     |             |               |         |           |     |             | The platform  | also offers | practical |     | advantages | over | many ex- |
pronetodetachmentinstructuredflowenvironments. Thiselon- isting microfluidic approaches for bacterial sorting and pheno-
gation suppresses breakout, propagation, and infiltration during typicantimicrobialsusceptibilitytesting35,50–54. Thecurrentde-
upstreammigrationinasimplifiedmicrofluidicsystemmotivated vice operates in single-phase flow without requiring multiphase
by bacterial transport in the urinary tract. In contrast, resistant handling. Becauseseparationarisesfromhydrodynamicinterac-
cellsretainashortmorphologyandpreserveupstreammigration tionsratherthangeometricexclusionalone,futuredevicescould
under ampicillin treatment. These findings show that resistance incorporateparallelchannelstoincreasethroughput. Thesefea-
notonlyenablessurvivalunderantibioticexposurebutalsopre- turessupportthefuturedevelopmentoftheplatformasanenrich-
servestransportbehaviorsthatfacilitatemovementagainstflow. mentmodulethatcouldbecoupledtoindependentphenotypicor
This perspective complements conventional views of antimi- molecularreadoutsforrapidAMRdetection.
crobial resistance that primarily focus on biochemical and ge- Furtherstudiescouldevaluatetheplatformundermorephysio-
| netic mechanisms. |     | Previous |     | studies | have | shown | how antibi- |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | ------- | ---- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
logicallyrelevantconditions,includingurineorurine-mimicking
oticsaltermetabolism,generegulation,andcelldivision,and,in media, clinically relevant E. coli isolates, and additional urinary
| somecases,bacterialmotility21,26,28,42. |     |     |     |     | Ourresultsextendthese |     |     |            |               |          |     |         |          |           |
| --------------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | ---------- | ------------- | -------- | --- | ------- | -------- | --------- |
|                                         |     |     |     |     |                       |     |     | tract flow | environments. | It would |     | also be | valuable | to test a |
insights by incorporating hydrodynamic effects, demonstrating broaderrangeofβ-lactamantibioticsandresistancemechanisms,
| how antibiotic-induced |     |     | elongation | influences |     | transport | in con- |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ---------- | ---------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
aswellastodeterminehowstrain-dependentdifferencesinmotil-
fined flows. Notably, our results show that elongation preserves ity,adhesion,andelongationinfluenceenrichmentperformance.
intrinsic motility but compromises upstream transport in struc- Finally, integrating microscopy-free readouts such as impedance
tured flow environments by increasing susceptibility to detach- cytometryandcouplingthedevicetodownstreamculture-based
ment and downstream advection. Therefore, transport against ormolecularanalysiscouldfurtherdeveloptheplatformtoward
flowcriticallydependsontheinterplaybetweencellmorphology, practicaldiagnosticuse.
motility,andhydrodynamicforcesunderantibioticstress13,19,45. In summary, we show that antibiotic-induced elongation sup-
Thebiologicalimplicationsofthisworkextendbeyondurinary
pressesrheotactictransportandthatthisphysicaldifferencecan
tract infections. Bacterial upstream migration may also be rel- be used to enrich ampicillin-resistant cells from mixed popula-
| evant in | other | pathologies, | including |     | lung | infections, | gastroin- |             |          |               |           |     |                |     |
| -------- | ----- | ------------ | --------- | --- | ---- | ----------- | --------- | ----------- | -------- | ------------- | --------- | --- | -------------- | --- |
|          |       |              |           |     |      |             |           | tions. More | broadly, | these results | highlight |     | the importance | of  |
testinal diseases, cardiovascular conditions, and the invasion of linking microbial physiology with hydrodynamics to better un-
bacteria into biomedical devices6,8,16,19,46. Moreover, bacteria derstandbacterialbehaviorincomplexenvironments5,6,55.
oftenencounterantibioticsinnaturalflowenvironments,suchas
Methods
soil,whereantimicrobialagentsproducedbyplantsandfungiare
| transported | by  | rainwater. | Although |     | more studies | are | needed to |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | -------- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Bacterialstrainsandculturingconditions
fullyinvestigatetheecologicalandclinicalrelevanceofourwork,
|              |         |     |           |          |           |     |            | The bacterial | strain used | in this | work | was | E. coli K-12 | strain |
| ------------ | ------- | --- | --------- | -------- | --------- | --- | ---------- | ------------- | ----------- | ------- | ---- | --- | ------------ | ------ |
| our findings | provide | a   | universal | physical | mechanism |     | that could |               |             |         |      |     |              |        |
EPB47,anMG1655derivativecarryingachromosomalompA-cfp
contributetobacterialpersistenceandcolonizationunderflow.
|                                                         |     |                                        |        |         |        |     |               | fusion (a  | gift from Mark | Goulian,        | University |      | of Pennsylvania). |       |
| ------------------------------------------------------- | --- | -------------------------------------- | ------ | ------- | ------ | --- | ------------- | ---------- | -------------- | --------------- | ---------- | ---- | ----------------- | ----- |
| WhereasthisstudyfocusesonE.coli,theinterplaybetweencell |     |                                        |        |         |        |     |               |            |                |                 |            | 32◦C |                   |       |
|                                                         |     |                                        |        |         |        |     |               | Cells from | frozen stocks  | were grown      |            | at   | on lysogeny       | broth |
| morphology                                              | and | rheotaxis                              | likely | extends | across | a   | wide range of |            |                |                 |            |      |                   |       |
|                                                         |     |                                        |        |         |        |     |               | (LB) agar  | plates (1%     | Bacto tryptone, |            | 0.5% | yeast extract,    | 1.0%  |
| microorganisms.                                         |     | Rheotaxishasbeenobservednotonlyinswim- |        |         |        |     |               |            |                |                 |            |      |                   |       |
NaCland1.5%agar)orinliquidLBwithshakingat250rpm.
| ming bacteria, |           | but also  | in species | that     | rely   | on alternative | motil-     |     |     |     |     |     |     |     |
| -------------- | --------- | --------- | ---------- | -------- | ------ | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| ity modes,     | including | twitching |            | motility | driven | by type        | IV pili in |     |     |     |     |     |     |     |
InductionofcellelongationviacontrolledsulAexpression
| Pseudomonas | aeruginosa |     | and | Xylella | fastidiosa, | as  | well as glid- |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | --- | ------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
ing motility in Mycoplasma46–49. While these modes of locomo- Tunable cell length in E. coli was achieved via heterologous ex-
tiontypicallyoccuratlowerspeedsthanflagellarswimming,they pression of sulA, which encodes a repressor of Z-ring formation
similarlydependoninteractionsbetweencellshape,surfacecon- andinhibitscelldivision34,43. ThesulAgenewasPCR-amplified
tact, andflow. Ourresultsthereforesuggestageneralprinciple: fromwild-typeE.coliandclonedintotheEcoRIandHindIIIsites
morphological changes, irrespective of the mechanism underly- ofpBAD24followingstandardrestriction-enzymecloningproce-
dures. UseofEcoRIensuredthatsulAwaspositionedproximalto
ingthesechanges,canmodulaterheotactictransportbyaltering
susceptibilitytodetachmentandadvection. thestrongribosome-bindingsiteinthepBAD24multiplecloning
The length-dependent transport difference also provides a site. The resulting construct was confirmed by Sanger sequenc-
physical basis for microfluidic cell enrichment. Under imposed ing. E.coliwastransformedwiththeplasmidviachemicaltrans-
flow,bacterialpopulationssegregateaccordingtocelllength,ef- formationandplatedonLBagarsupplementedwith100µgmL−1
fectivelycreatingahydrodynamicfilteringmechanism. Welever- ampicillin. All growth media were supplemented with 0.2% D-
agedthisprincipletoenrichampicillin-resistantcellsfrommixed glucosetorepresssulAexpression. Toinduceelongation,glucose
populations using a 30min microfluidic selection step following was omitted and replaced with 0.2% L-arabinose to activate ex-
approximately 2h of antibiotic exposure. These results demon- pressionfromtheP promoter.
BAD
32◦C
strate rapid physical enrichment following antibiotic exposure Cultures were grown overnight at with shaking at
Journal Name, [year], [vol.],1–13
|5

A100µLaliquotwasdiluted10−2intofreshTBmedium
250rpm. metal–oxide–semiconductor(sCMOS)camera(HamamatsuOrca-
and grown for approximately 5h until OD reached 0.1. For FusionGen-III)upto100FPS.
600
| elongation | induction, | cultures | were | supplemented |     | with | 0.2% L- |            |     |              |          |      |          |           |     |
| ---------- | ---------- | -------- | ---- | ------------ | --- | ---- | ------- | ---------- | --- | ------------ | -------- | ---- | -------- | --------- | --- |
|            |            |          |      |              |     |      |         | We flushed | the | microfluidic | channels | with | bacteria | suspended |     |
arabinose and incubated for 1h, with induction duration deter- inmotilitybufferuntilanoptimalcellconcentrationwasreached
| mining the | average | cell | length. | Cells | were then | diluted | 10−2 |          |               |     |         |              |     |                  |     |
| ---------- | ------- | ---- | ------- | ----- | --------- | ------- | ---- | -------- | ------------- | --- | ------- | ------------ | --- | ---------------- | --- |
|            |         |      |         |       |           |         |      | that was | dilute enough | to  | prevent | cell overlap |     | and interference |     |
into motility buffer (MB: 0.1mM EDTA, 0.001mM L-methionine, with tracking, yet sufficiently concentrated to obtain a robust
10mM sodium lactate, 67mM NaCl, 6.2mM K HPO , 3.9mM dataset. Single-celltrackingwasconductedtoinvestigatebreak-
2 4
0.08gmL−1
KH 2 PO 4 ) supplemented with L-serine and 0.03% out dynamics across different geometries under varying flow
| polyvinylpyrrolidone |     | (PVP). | The | motility | buffer | was adjusted | to  | strengths. |     |     |     |     |     |     |     |
| -------------------- | --- | ------ | --- | -------- | ------ | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
pH7.05. Cellswereequilibratedinmotilitybufferfor30min,and We consistently tracked cells swimming inside the channel
theirswimmingbehaviorwasverifiedinamotilitychamberprior
|     |     |     |     |     |     |     |     | without them | moving | out | of the focal | plane. | Videos | were | post- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --- | ------------ | ------ | ------ | ---- | ----- |
to experiments. All microfluidic measurements were conducted processedinImageJ,andcellsweretrackedautomaticallyusinga
within2hatroomtemperaturetomaintainstablemotility. customMACROcodewiththehelpoftheTrackMateplugin. Cell
|     |     |     |     |     |     |     |     | trajectories | lasting | longer | than 1s | were analyzed |     | with | a custom |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------ | ------- | ------------- | --- | ---- | -------- |
Antibiotictreatments Pythoncodetodeterminethebreakoutandinfiltrationprobabili-
To induce filamentation in susceptible cells, wild-type cultures tiesandtheupstreamvelocitydistributions.
| wereexposedtoantibioticsafter3hofdaytimegrowth. |     |     |     |     |     |     | Cultures |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
were then supplemented with either 120µgmL−1 cephalexin or Rheotaxissimulations
2µgmL−1
ampicillin and incubated for an additional 2h before To isolate the effect of cell elongation on upstream migration,
| experiments.    | This                    | resulted       | in a | total daytime |          | culture    | duration  |              |            |                     |               |           |        |                  |          |
| --------------- | ----------------------- | -------------- | ---- | ------------- | -------- | ---------- | --------- | ------------ | ---------- | ------------------- | ------------- | --------- | ------ | ---------------- | -------- |
|                 |                         |                |      |               |          |            |           | we simulated | individual |                     | E. coli cells | swimming  |        | in a rectangular |          |
| of 5h, matching |                         | the incubation |      | time used     | for      | untreated  | control   |              |            |                     |               |           |        |                  |          |
|                 |                         |                |      |               |          |            |           | microchannel | with       | widthW              | =50µm         | and       | height | H=10µm.          | The      |
| cultures.       | An ampicillin-resistant |                |      | E. coli       | EPB47    | strain     | harboring |              |            |                     |               |           |        |                  |          |
|                 |                         |                |      |               |          |            |           | simulations  | used       | a three-dimensional |               | rheotaxis |        | model            | with the |
| plasmid-encoded |                         | β-lactamase    | was  | used          | to study | resistance | ef-       |              |            |                     |               |           |        |                  |          |
analyticalsolutionforpressure-drivenPoiseuilleflowinarectan-
fects.
|     |     |     |     |     |     |     |     | gular channel. | Each | bacterium | was | modeled | as  | a self-propelled |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | --------- | --- | ------- | --- | ---------------- | --- |
cellbodywithpositionr,orientationpˆ,intrinsicswimmingspeed
Microfluidicdevices
|     |     |     |     |     |     |     |     | V swim , aspect | ratio | Γ, and | flagellar | length | L f. | Short wild-type- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | ------ | --------- | ------ | ---- | ---------------- | --- |
ThemicrofluidicchannelswereconstructedwithadepthofH= like cells were assigned aspect ratios uniformly distributed over
10µm,awidthofW =50µm,andalengthofseveralmillimeters. Γ=2–4, corresponding to cell lengths of 2µm–4µm for a fixed
Toensureaslow, steady, andstableflowrate, aresistorchannel cell width of 1µm, consistent with experimental measurements.
of approximately 10cm in length was added. The microfluidic Elongatedcellsweresimulatedbychangingonlythecell-bodyas-
channels were made of polydimethylsiloxane (PDMS) through pectratiotoΓ=8–10, whilekeepingallotherparametersfixed.
thereplicationofapositive-reliefsiliconwafermasterwithSU-8 Themodelincludesintrinsicswimming,advectionbytheimposed
coatedpatternfabricatedbystandardphotolithographyandsoft- flow, Jeffery-orbit rotation in shear flow, stochastic rotational
lithography procedures. The PDMS and the curing agent were noise, surface alignment, circular swimming near walls, weath-
mixed thoroughly at a 10:1 weight ratio. The mixture of PDMS ervane reorientation, and corner interactions. Simulations were
andthecuringagentwasdegassedinsideavacuumchamberfor initializedwith103 bacteriarandomlydistributedinthechannel
atleastonehourtoremoveairbubblesbeforebeingpouredonto andintegratedwithatimestepofδt=0.01sfor5000timesteps.
the silicon wafer. The mixture was cured at 65◦C overnight to FullequationsandparameterdefinitionsareprovidedinSupple-
mentaryNotesS8andS9.
| ensurefullcross-linking. |     |     | AftercuttingandpeelingoffthePDMS |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
replicafromthesiliconwafer,1mmdiameterholeswerepunched
|                        |     |     |                                  |     |     |     |     | Supplementary |     | information |     |     |     |     |     |
| ---------------------- | --- | --- | -------------------------------- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- |
| attheinletsandoutlets. |     |     | ThePDMSreplicaandaglasscoverslip |     |     |     |     |               |     |             |     |     |     |     |     |
werecleanedwithcompressedairandplasma-treatedfor25sec- Supplementaryinformation(SI)isavailable.
onds(HarrickPlasmaPDC-32G).Wethenirreversiblyboundthe
|              |       |               |     |              |        |      | 95◦C      | Author   | contributions      |     |              |     |                |     |        |
| ------------ | ----- | ------------- | --- | ------------ | ------ | ---- | --------- | -------- | ------------------ | --- | ------------ | --- | -------------- | --- | ------ |
| PDMS replica | and   | coverslip     | and | left the     | sample | on a | hot       |          |                    |     |              |     |                |     |        |
| plate for    | ∼1min | to strengthen |     | the sealing. | Flow   | was  | generated |          |                    |     |              |     |                |     |        |
|              |       |               |     |              |        |      |           | Ran Tao: | conceptualization, |     | methodology, |     | investigation, |     | device |
by applying a precise pressure gradient using a pressure-driven fabrication, data acquisition, formal analysis, software, simula-
pump(ElveFlowOB1MK4).
tions,visualization,writing–originaldraft,andwriting–review
|     |     |     |     |     |     |     |     | & editing. | Nathaniel | C.  | Esteves: | resources, | methodology, |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | -------- | ---------- | ------------ | --- | --- |
Imagingandsingle-celltracking writing–review&editing. JayZhu: resources,supervision,and
We captured bacterial dynamics on a Nikon TI2-E microscope writing – review & editing. Arnold J. T. M. Mathijssen: concep-
through a 20x objective (CFI60 Plan Apochromat Lambda tualization, supervision, project administration, funding acquisi-
Objective Lens, numerical aperture 0.75, working distance tion,andwriting–review&editing.
| 1.0mm)  | under           | bright-field | illumination |     | for          | single-cell | track-    |           |             |     |     |     |     |     |     |
| ------- | --------------- | ------------ | ------------ | --- | ------------ | ----------- | --------- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
|         |                 |              |              |     |              |             |           | Conflicts | of interest |     |     |     |     |     |     |
| ing and | by fluorescence |              | imaging      | for | distribution |             | analysis. |           |             |     |     |     |     |     |     |
The recordings were made with a scientific complementary Theauthorsdeclarenoconflictofinterest.
Journal Name, [year], [vol.],1–13
6|

Data availability
shulerandE.Clément,Sci.Adv.,2020,6,eaay0155.
|     |     |     |     |     |     |     |     | 15 G.Jing, | A.Zöttl, | E.ClémentandA.Lindner, |     |     |     | Sci.Adv., | 2020, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---------------------- | --- | --- | --- | --------- | ----- |
Alldatasupportingthefindingsofthisstudyareavailableinthe
6,eabb2012.
| article. Additional | information |     | required |     | to reanalyze | the | data is |                  |     |       |         |          |          |     |           |
| ------------------- | ----------- | --- | -------- | --- | ------------ | --- | ------- | ---------------- | --- | ----- | ------- | -------- | -------- | --- | --------- |
|                     |             |     |          |     |              |     |         | 16 A. Siryaporn, |     | M. K. | Kim, Y. | Shen, H. | A. Stone | and | Z. Gitai, |
availablefromthecorrespondingauthoruponrequest.
Curr.Biol.,2015,25,1201–1207.
Acknowledgements
|     |     |     |     |     |     |     |     | 17 B. O. | Torres | Maldonado, | A. Théry, | R.  | Tao, | Q. Brosseau, | A. J. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --------- | --- | ---- | ------------ | ----- |
WethankallmembersoftheMathijssenlabandtheZhulabfor T.M.MathijssenandP.E.Arratia,Proc.Natl.Acad.Sci.U.S.
A.,2024,121,e2417614121.
| their support | and insightful |     | discussions. |     | We further | thank | Liuni |     |     |     |     |     |     |     |     |
| ------------- | -------------- | --- | ------------ | --- | ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Chen and Ling Li for their support with SEM imaging. R.T. ac- 18 D.Cao,R.Tao,A.Théry,S.Liu,A.J.T.MathijssenandY.Wu,
arXiv[cond-mat.soft],2024,arXiv:2408.13694.
knowledgessupportfromtheDissertationCompletionFellowship
attheUniversityofPennsylvania.A.J.T.M.M.acknowledgesfund- 19 R.Tao, A.Théry, S.QueandA.J.T.M.Mathijssen, Newton,
ing from the Charles E. Kaufman Foundation (Early Investigator 2026,2,100337.
Research Award KA2022-129523; and New Initiative Research 20 G. C. Padron, S. Chen, A. Sharma, Z. Modi, M. D. Koch and
| Award KA2024-144001), |     | the | National | Science | Foundation |     | (Ca- |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------- | ------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
J.E.Sanfilippo,MBio,2026,17,e0344625.
reer Award CBET-2542731; and UPenn MRSEC DMR-2309043), 21 M.A.Kohanski,D.J.DwyerandJ.J.Collins,Nat.Rev.Micro-
theUniversityofPennsylvania(URF,CURF,VIPER,VagelosMLS,
biol.,2010,8,423–435.
andFERBSprograms),andtheResearchCorporationforScience 22 A. Typas, M. Banzhaf, C. A. Gross and W. Vollmer, Nat. Rev.
Advancement(CottrellScholarAwardCS-CSA-2026-125).
Microbiol.,2011,10,123–136.
|           |            |     |     |     |     |     |     | 23 D.Melnick,A.K.Talley,V.K.Gupta,I.A.Critchley,P.B.Eck- |            |     |          |          |           |     |         |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | ---------- | --- | -------- | -------- | --------- | --- | ------- |
| Notes and | references |     |     |     |     |     |     |                                                          |            |     |          |          |           |     |         |
|           |            |     |     |     |     |     |     | burg,                                                    | K.A.Hamed, |     | N.Bhatt, | G.Moore, | D.Austin, |     | C.M.Ru- |
1 WorldHealthOrganization,Thetop10causesofdeath,2020.
bino,S.M.BhavnaniandP.G.Ambrose,AntimicrobialAgents
| 2 United | Nations | Environment | Programme, |     | Bracing | for | Super- |     |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | ---------- | --- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
andChemotherapy,2023,67.
| bugs: | Strengthening | Environmental |     | Action | in  | the One | Health |                                                        |     |     |     |     |     |     |     |
| ----- | ------------- | ------------- | --- | ------ | --- | ------- | ------ | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|       |               |               |     |        |     |         |        | 24 A.TilanusandG.Drusano,OpenForumInfect.Dis.,2023,10, |     |     |     |     |     |     |     |
ResponsetoAntimicrobialResistance,UnitedNations,2023.
ofad305.
| 3 C. S. | Ho, C. T. | H. Wong, | T. T.    | Aung, | R. Lakshminarayanan, |       |          |             |     |               |     |          |     |              |     |
| ------- | --------- | -------- | -------- | ----- | -------------------- | ----- | -------- | ----------- | --- | ------------- | --- | -------- | --- | ------------ | --- |
|         |           |          |          |       |                      |       |          | 25 N. Maki, | J.  | E. Gestwicki, | E.  | M. Lake, | L.  | L. Kiessling | and |
| J. S.   | Mehta, S. | Rauz, A. | McNally, | B.    | Kintses,             | S. J. | Peacock, |             |     |               |     |          |     |              |     |
J.Adler,J.Bacteriol.,2000,182,4337–4342.
| C. de | la Fuente-Nunez, |     | R. E. W. | Hancock | and | D. S. | J. Ting, |              |     |        |              |          |     |              |       |
| ----- | ---------------- | --- | -------- | ------- | --- | ----- | -------- | ------------ | --- | ------ | ------------ | -------- | --- | ------------ | ----- |
|       |                  |     |          |         |     |       |          | 26 C. Cylke, | F.  | Si and | S. Banerjee, | Biochem. |     | Soc. Trans., | 2022, |
LancetMicrobe,2025,6,100947.
50,1269–1279.
4 A.L.Flores-Mireles,J.N.Walker,M.CaparonandS.J.Hult-
|     |     |     |     |     |     |     |     | 27 S. S. | Justice, | D. A. | Hunstad, | P. C. | Seed and | S. J. | Hultgren, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | -------- | ----- | -------- | ----- | --------- |
gren,Nat.Rev.Microbiol.,2015,13,269–284.
Proc.Natl.Acad.Sci.U.S.A.,2006,103,19884–19889.
| 5 J. S. | Guasto, R. | Rusconi | and | R. Stocker, | Annu. | Rev. | Fluid |              |             |     |          |     |           |            |     |
| ------- | ---------- | ------- | --- | ----------- | ----- | ---- | ----- | ------------ | ----------- | --- | -------- | --- | --------- | ---------- | --- |
|         |            |         |     |             |       |      |       | 28 T.V.Phan, | R.J.Morris, |     | H.T.Lam, |     | P.Hulamm, | M.E.Black, |     |
Mech.,2012,44,373–400.
|     |     |     |     |     |     |     |     | J.BosandR.H.Austin, |     |     | Proc.Natl.Acad.Sci.U.S.A., |     |     |     | 2018, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | -------------------------- | --- | --- | --- | ----- |
6 A.Persat,C.D.Nadell,M.K.Kim,F.Ingremeau,A.Siryaporn,
115,12979–12984.
| K.Drescher, | N.S.Wingreen, |     | B.L.Bassler, |     | Z.GitaiandH.A. |     |     |          |           |       |             |     |        |              |       |
| ----------- | ------------- | --- | ------------ | --- | -------------- | --- | --- | -------- | --------- | ----- | ----------- | --- | ------ | ------------ | ----- |
|             |               |     |              |     |                |     |     | 29 N. M. | Oliveira, | J. H. | R. Wheeler, | C.  | Deroy, | S. C. Booth, | E. J. |
Stone,Cell,2015,161,988–997.
Walsh,W.M.DurhamandK.R.Foster,Nat.Commun.,2022,
| 7 J. D. | Wheeler, E. | Secchi, | R. Rusconi |     | and R. | Stocker, | Annual |     |     |     |     |     |     |     |     |
| ------- | ----------- | ------- | ---------- | --- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
13,7608.
ReviewofCellandDevelopmentalBiology,2019,35,213–237.
|             |            |     |          |             |     |           |         | 30 Y.Karita, | D.  | T.Limmer | andO. | Hallatschek, |     | Proc.Natl. | Acad. |
| ----------- | ---------- | --- | -------- | ----------- | --- | --------- | ------- | ------------ | --- | -------- | ----- | ------------ | --- | ---------- | ----- |
| 8 E.Secchi, | A. Vitale, | G.  | L. Miño, | V.Kantsler, |     | L. Eberl, | R. Rus- |              |     |          |       |              |     |            |       |
Sci.U.S.A.,2022,119,e2115496119.
coniandR.Stocker,Nat.Commun.,2020,11,2851.
|         |                   |     |     |              |     |     |         | 31 A.M.Shuppara,G.C.Padron,A.Sharma,Z.Modi,M.D.Koch |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | --- | ------------ | --- | --- | ------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 9 A. J. | T. M. Mathijssen, |     | H.  | Almohammadi, |     | L.  | Altman, |                                                     |     |     |     |     |     |     |     |
andJ.E.Sanfilippo,Sci.Adv.,2025,11,eads5005.
| T. Calazans, | M.      | J. Ferencz, | M.       | Fung,   | I. J. | Lee, M. | Lisicki, |                                                        |     |     |     |     |     |     |     |
| ------------ | ------- | ----------- | -------- | ------- | ----- | ------- | -------- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|              |         |             |          |         |       |         |          | 32 P.Chopra,D.Quint,A.GopinathanandB.Liu,Phys.Rev.Flu- |     |     |     |     |     |     |     |
| I. Liu,      | M. Liu, | T. Liu,     | E. Park, | R. Tao, | A.    | Thery,  | Z. Wang  |                                                        |     |     |     |     |     |     |     |
ids,2022,7.
| and M. | Young, | Annual | Review | of Condensed |     | Matter | Physics, |                          |     |     |            |     |       |                   |     |
| ------ | ------ | ------ | ------ | ------------ | --- | ------ | -------- | ------------------------ | --- | --- | ---------- | --- | ----- | ----------------- | --- |
|        |        |        |        |              |     |        |          | 33 A. Daddi-Moussa-Ider, |     |     | M. Lisicki | and | A. J. | T. M. Mathijssen, |     |
accepted,2026,arXiv2603.15778.
Phys.Rev.Appl.,2020,14,024071.
| 10 J. Hill, | O. Kalkanci, | J.  | L. McMurry | and | H. Koser, | Phys. | Rev. |                                                    |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ---------- | --- | --------- | ----- | ---- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|             |              |     |            |     |           |       |      | 34 D.Gao,Z.Wang,M.Jain,A.J.T.M.MathijssenandR.Tao, |     |     |     |     |     |     |     |
Lett.,2007,98,068101.
Integr.Comp.Biol.,2026,66.
11 T.KayaandH.Koser,BiophysicalJournal,2012,102,1514–
|     |     |     |     |     |     |     |     | 35 P. Liu, | H. Liu, | L. Semenec, | D.  | Yuan, | S. Yan, | A. K. | Cain and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --- | ----- | ------- | ----- | -------- |
1523.
M.Li,Microsyst.Nanoeng.,2022,8,7.
| 12 N. Figueroa-Morales, |     | G.  | Leonardo | Miño, | A.  | Rivera, | R. Ca- |                |     |             |     |        |         |     |          |
| ----------------------- | --- | --- | -------- | ----- | --- | ------- | ------ | -------------- | --- | ----------- | --- | ------ | ------- | --- | -------- |
|                         |     |     |          |       |     |         |        | 36 M. Masaeli, |     | E. Sollier, | H.  | Amini, | W. Mao, | K.  | Camacho, |
ballero,E.Clément,E.AltshulerandA.Lindner,SoftMatter,
N.Doshi,S.Mitragotri,A.AlexeevandD.DiCarlo,Phys.Rev.
2015,11,6284–6293.
X.,2012,2.
13 A.J.T.M.Mathijssen,N.Figueroa-Morales,G.Junot,E.Clé-
|     |     |     |     |     |     |     |     | 37 H.Tang,J.Niu,H.Jin,S.LinandD.Cui,Microsyst.Nanoeng., |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ment,A.LindnerandA.Zöttl,Nat.Commun.,2019,10,3434.
2022,8,62.
| 14 N. Figueroa-Morales, |     | A.  | Rivera, | R. Soto, | A.  | Lindner, | E. Alt- |                                                       |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------- | -------- | --- | -------- | ------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                         |     |     |         |          |     |          |         | 38 J.Cruz,T.Graells,M.WalldénandK.Hjort,LabChip,2019, |     |     |     |     |     |     |     |
Journal Name, [year], [vol.],1–13
|7

19,1257–1266. 46 Y. Shen, A. Siryaporn, S. Lecuyer, Z. Gitai and H. A. Stone,
39 T.Zhang,A.K.Cain,L.Semenec,J.V.Pereira,Y.Hosokawa, Biophys.J.,2012,103,146–151.
Y. Yalikun and M. Li, Sens. Actuators B Chem., 2023, 390, 47 Y.Meng,Y.Li,C.D.Galvani,G.Hao,J.N.Turner,T.J.Burr
133918. andH.C.Hoch,J.Bacteriol.,2005,187,5560–5567.
40 T. Tang, X. Liu, Y. Yuan, T. Zhang, R. Kiya, Y. Yang, Y. Ya- 48 D. Nakane, Y. Kabata and T. Nishizaka, PLoS Pathog., 2022,
mazaki, H. Kamikubo, Y. Tanaka, M. Li, Y. Hosokawa and 18,e1010648.
Y.Yalikun,ACSSens.,2022,7,3700–3709. 49 R.Rosengarten,A.Klein-StruckmeierandH.Kirchhoff,J.Bac-
41 J.Zhu,S.Pan,H.Chai,P.Zhao,Y.Feng,Z.Cheng,S.Zhang teriol.,1988,170,989–990.
andW.Wang,Small,2024,20,e2310700. 50 S. Pérez-Rodríguez, J. M. García-Aznar and J. Gonzalo-
42 M. F. Anjum, E. Zankari and H. Hasman, Microbiol. Spectr., Asensio,Microb.Biotechnol.,2022,15,395–414.
2017,5,33–50. 51 W. Zhou, J. Le, Y. Chen, Y. Cai, Z. Hong and Y. Chai, Trends
43 A.Higashitani,N.HigashitaniandK.Horiuchi,Biochem.Bio- Analyt.Chem.,2019,112,175–195.
phys.Res.Commun.,1995,209,198–204. 52 J.P.Gurung,M.GelandM.A.B.Baker,Microb.Cell,2020,7,
44 S. Kamdar, D. Ghosh, W. Lee, M. Ta˘tulea-Codrean, Y. Kim, 66–79.
S.Ghosh,Y.Kim,T.Cheepuru,E.Lauga,S.LimandX.Cheng, 53 X. Liu, R. E. Painter, K. Enesa, D. Holmes, G. Whyte, C. G.
Proc.Natl.Acad.Sci.U.S.A.,2023,120,e2310952120. Garlisi,F.J.Monsma,M.Rehak,F.F.CraigandC.A.Smith,
45 V.Tokárová,A.SudalaiyadumPerumal,M.Nayak,H.Shum, LabChip,2016,16,1636–1643.
O. Kašpar, K. Rajendran, M. Mohammadi, C. Tremblay, E. A. 54 W. Postek, N. Pacocha and P. Garstecki, Lab Chip, 2022, 22,
Gaffney, S. Martel, D. V. Nicolau, Jr and D. V. Nicolau, Proc. 3637–3662.
Natl.Acad.Sci.U.S.A.,2021,118,e2013925118. 55 I.S.Aranson,Rep.Prog.Phys.,2022,85,076601.
8| Journal Name, [year], [vol.],1–13

Fig. 1 Overviewoftheexperimentalframework,physicalmechanism,andpotentialdiagnosticextension. (A)Clinicalmotivation: motilebacteriacan
migrate upstream in urinary tract flows, motivating the investigation of bacterial transport under antibiotic exposure. (B) Oral antibiotic treatment
introduces antimicrobial agents into the urinary tract. (C) β-lactam exposure inhibits cell division and induces filamentous elongation in antibiotic-
susceptible E. coli. (D) Short cells maintain stable near-surface rheotaxis and swim upstream against the imposed flow, whereas elongated cells are
more susceptible to flow-induced rotation, surface detachment, and downstream advection. (E) This length-dependent transport response enables
microfluidicseparationofshortandelongatedcellsandproof-of-conceptenrichmentofampicillin-resistantcellsfrommixedresistantandsusceptible
populations. (F)Apotentialfuturediagnosticworkflowcouldcombinemicrofluidicenrichmentwithimpedancecytometryformicroscopy-freeon-chip
detectionofenrichedcells,followedbydownstreamsequencingorothermolecularanalysis. PanelsA,B,andFillustratetheclinicalmotivationand
potentialfutureworkflow,whereasPanelsC–Esummarizetheexperimentallyinvestigatedmechanismandenrichmentprinciple.
Journal Name, [year], [vol.],1–13 |9

Fig. 2 Antibiotic-inducedelongationpreservesmotilitybutinhibitsupstreaminvasion. (A)Schematicofbacterialrheotaxisandantibioticexposure
intheurinarytract. (B)Representativemorphologies: wild-type(WT)cellsremainshortrods,whereascephalexin-andampicillin-treatedsusceptible
cellselongate. Ageneticallymodifiedstrainwithinducibleelongationisusedtoisolatetheeffectofcelllength. Anampicillin-resistantstrainretains
short morphology under antibiotic treatment. (C) Quantification of cell length across conditions. Bars show the mean, and error bars indicate the
standard deviation across N=4 independent cultures prepared on different days. (D) Swimming speeds,Vswim, across conditions. Points show the
mean trajectory-level value, and shaded regions indicate the standard deviation across N=4 independent cultures prepared on different days. (E)
Microfluidic platform used to quantify upstream invasion under imposed flow in channels of height H=10µm and width W =50µm. Bacteria are
introducedintothedownstreamreservoir,thenarrowchannelprovidesasimplifiedconfined-flowenvironmentmotivatedbybacterialtransportinthe
urinary tract, and the upstream reservoir serves as the collection region for quantifying upstream migration. (F) Representative fluorescence images
after 8h of flow for untreated WT, cephalexin-treated susceptible, ampicillin-treated susceptible, and ampicillin-resistant cells. White lines indicate
thechannelboundaries. (G)Representativeimagesoftheupstreamreservoirafter8h. (H)Bacterialdensityintheupstreamreservoir. Barsanderror
barsshowthemean±standarddeviationacrossN=4independentexperiments;pointsshowindividualexperiments. Asterisksindicateunadjusted p
values: *p<0.05,**p<0.01,and***p<0.001.
10| Journal Name, [year], [vol.],1–13

Fig. 3 Elongated cells fail at distinct stages of upstream invasion. (A) Microfluidic invasion device and three sequential stages: (I) breakout,
(II) propagation, and (III) infiltration. (B) Time evolution of upstream invasion by wild-type cells (green) and elongated cells (blue) under flow.
(C) Breakout probability, P
breakout
, as a function of maximum flow velocity, Vmax. For each data point, N>500 breakout attempts were analyzed.
Error bars represent the binomial standard error. (D) Representative breakout events for WT (left) and elongated cells (right). White and orange
trajectories indicate failed and successful attempts, respectively. (E) Mean propagation velocity along the flow direction ⟨Vx⟩ versus Vmax. Dots
represent experimental measurements, and solid lines represent simulation results. (F) Representative trajectories showing persistent edge-following
andupstreammotioninWTcells(top)andrapiddetachmentwithdownstreamdriftinelongatedcells(bottom). (G)Infiltrationprobability,P ,
infiltration
intotheupstreamreservoirasafunctionofVmax. Foreachdatapoint,N>500infiltrationattemptswereanalyzed. Errorbarsrepresentthebinomial
standard error. (H) Representative infiltration events for WT (left) and elongated cells (right). White and orange trajectories indicate failed and
successfulattempts,respectively.
Journal Name, [year], [vol.],1–13 |11

Fig. 4 Flow-induced spatial separation of bacterial populations based on cell length. (A) Time series of mixed short-cell populations (WT, green)
and elongated-cell populations (blue) under imposed flow. (B) Space–time kymographs illustrating sustained upstream accumulation of short cells
(left, green) and downstream retention of elongated cells (right, blue). Spatial position along the channel is shown on the horizontal axis and time
progresses along the vertical axis. (C) Spatial density profiles after 120min show enrichment of short cells in the upstream region and depletion of
elongatedcells.
12| Journal Name, [year], [vol.],1–13

Fig. 5 Rheotaxis-basedmicrofluidicenrichmentofampicillin-resistantE.coli. (A)Conceptualworkflowforantibioticexposure,microfluidicenrichment,
and downstream analysis. The dashed red box identifies the experimentally tested ampicillin condition. Patient-derived samples, parallel antibiotic
testing, impedance cytometry, and sequencing are conceptual extensions. (B) Representative fluorescence image of ampicillin-resistant cells (yellow)
accumulatingupstreamwhilesusceptibleelongatedcells(red)remainpredominantlydownstream. Thearrowindicatestheflowdirection. Scalebar,
50µm. (C)Enrichmentperformanceformixtureswithdifferentinitialresistant-cellfractions. Left: totalupstreamcellcount, Nup, duringthe30min
enrichmentperiod. Middle: resistant-cellandsusceptible-cellcountsupstreamat30min. Right: resistant-cellfractionupstream, f R,up,at30min. Thin
curvesandcirclesshowindependentexperiments;thickcurvesandopendiamondsshowthemean;shadedregionsanderrorbarsshowmean±SEM.
Forallconditions,n=3independentexperimentswereconductedusingseparatesamplesondifferentdays.
Journal Name, [year], [vol.],1–13 |13
---- END DOCUMENT ----
