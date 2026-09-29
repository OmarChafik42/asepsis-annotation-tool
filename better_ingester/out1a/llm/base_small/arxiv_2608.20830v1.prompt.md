Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Fine-tuning LLMs for Tourist Trajectory Prediction using Field Experiment Data*
TatsuyaAmano1,2,HirozumiYamaguchi1,2
1TheUniversityofOsaka,Suita,Japan
2RIKENCenterforComputationalScience,Kobe,Japan
t-amano@ist.osaka-u.ac.jp,h-yamagu@ist.osaka-u.ac.jp
6202 guA 12  ]YC.sc[  1v03802.8062:viXra Abstract Tourism has supported 37 Green Slow Mobility pilot pro-
gramsbetween2019and2021.Ourresearchteamconducted
Evaluating mobility interventions at tourist destinations re- field experiments at Wakayama Castle Park in Wakayama
quires predicting visitor behavior under varying conditions. Prefecture,implementingthreetypesofmobilityservicesin-
Traditional methods struggle because tourist decisions de- cludingGreenSlowMobilityvehicles,e-bikes,andwalking
pendheavilyoncontextlikeweatherandfatigue,yetmodels
supportdevicestoenhancecirculationfromtheestablished
cannotgeneralizetounobservedscenarios.LargeLanguage
southerncastleareatonewlydevelopednorthernfacilities.
| Models | offer | a solution | by encoding |     | commonsense | knowl- |     |     |     |     |     |     |     |
| ------ | ----- | ---------- | ----------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
However,acriticalchallengeremains.Whilethesemobil-
| edge about | human | behavior |     | from pretraining, |     | enabling rea- |                   |     |                     |     |             |            |     |
| ---------- | ----- | -------- | --- | ----------------- | --- | ------------- | ----------------- | --- | ------------------- | --- | ----------- | ---------- | --- |
|            |       |          |     |                   |     |               | ity interventions |     | require substantial |     | investment, | predicting |     |
soningaboutcontext-dependentdecisions,whilenaturallan-
guagerepresentationflexiblyintegratesheterogeneousinfor- howtheywillactuallychangetouristbehaviorisremarkably
mation. Fine-tuning on local trajectories adapts this general difficult. Destination planners need to forecast whether in-
understanding to destination-specific patterns. We validate troducingashuttleservicewillencouragevisitorstoexplore
thisapproachusing566trajectoriesfromWakayamaCastle distantattractions,orwhethere-bikeswillalterroutechoices
Park, Japan. Our fine-tuned Llama-3.1-8B achieves 49.1% anddwelltimes.Withoutreliablepredictions,effectiveplan-
nextPOIaccuracyandmaintainsstrongperformanceonun-
|     |     |     |     |     |     |     | ning and | investment | decisions |     | become nearly | impossible. |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------- | --- | ------------- | ----------- | --- |
dersampledscenarioslikerainydays,demonstratingeffective
Willanewmobilityservicesuccessfullyredistributeflows,
generalization.ThisestablishesLLMsashigh-fidelitybehav-
orwillvisitorssimplyuseittoreachthesamepopularsites
| ior models | for | context-dependent |     | tourist | prediction, | provid- |             |           |           |     |                |        |     |
| ---------- | --- | ----------------- | --- | ------- | ----------- | ------- | ----------- | --------- | --------- | --- | -------------- | ------ | --- |
|            |     |                   |     |         |             |         | faster? The | inability | to answer |     | such questions | before | im- |
inggroundworkforcounterfactualanalysisofmobilityinter-
|     |     |     |     |     |     |     | plementation | creates | significant |     | uncertainty | for destination |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ----------- | --- | ----------- | --------------- | --- |
ventions.
management.
|     |     |     |     |     |     |     | Traditional | approaches |     | to tourist | behavior | prediction |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ---------- | -------- | ---------- | --- |
Introduction
strugglewiththiscomplexity.Markovchainsassumemem-
orylesstransitionsthatignorehowaccumulatedexperiences
| Regional | tourist | destinations |     | worldwide | face | the chal- |     |     |     |     |     |     |     |
| -------- | ------- | ------------ | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
lenge of uneven visitor distribution. Popular landmarks at- shapechoices.Deeplearningmethodsachievehigheraccu-
tractoverwhelmingcrowdswhileculturallysignificantsites racybutrequiremassivedatasetsrarelyavailableforindivid-
ualdestinationsandstruggletoincorporatecontextualinfor-
| nearby | remain | underutilized, |     | limiting | both visitor | satisfac- |     |     |     |     |     |     |     |
| ------ | ------ | -------------- | --- | -------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
mationlikeweatherorspecialeventsthatsignificantlyinflu-
tionandlocaleconomicdevelopment(UNWTO2018).This
encemobilitypatterns.Mostcritically,thesemodelscannot
imbalanceoftenstemsfromphysicalbarriersthatappearmi-
noronmapsbutsignificantlyimpactactualvisitorbehavior. leverage commonsense knowledge about human behavior.
Walking distances become substantial obstacles for elderly They require explicit observation of each scenario to learn
|          |              |      |       |           |     |              | patterns | that humans | understand |     | intuitively, | making | them |
| -------- | ------------ | ---- | ----- | --------- | --- | ------------ | -------- | ----------- | ---------- | --- | ------------ | ------ | ---- |
| visitors | and families | with | young | children. | The | spatial con- |          |             |            |     |              |        |      |
unabletopredicthowvisitorsmightrespondtonewmobility
| figuration | of attractions, |     | combined |     | with limited | awareness |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | -------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
optionsorchangedconditions.
| of alternative | sites, | creates |     | concentrated | flows | that stress |     |     |     |     |     |     |     |
| -------------- | ------ | ------- | --- | ------------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
popularlocationswhileleavingvaluableresourcesunderex- Thisresearchproposesfine-tuningLargeLanguageMod-
ploited. els to predict tourist trajectories by combining destination-
|            |       |             |     |             |     |               | specific | learning | with pre-trained |     | behavioral | knowledge. |     |
| ---------- | ----- | ----------- | --- | ----------- | --- | ------------- | -------- | -------- | ---------------- | --- | ---------- | ---------- | --- |
| To address | these | circulation |     | challenges, |     | many destina- |          |          |                  |     |            |            |     |
LLMstrainedonmassivetextcorporahaveencodedrichun-
| tions have | begun | deploying |     | innovative | mobility | solutions. |     |     |     |     |     |     |     |
| ---------- | ----- | --------- | --- | ---------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Electricshuttles,bike-sharingsystems,andautonomousve- derstanding of human decision-making under various con-
hicles promise to connect distributed attractions and re- ditions.Theyunderstandthatrainencouragesindooractivi-
distribute visitor flows (Yang, Jiang, and Zhang 2021). In ties,thatfamiliesneedfrequentrestbreaks,andhowtrans-
|            |          |     |       |                 |     |               | portation    | options | influence | destination | choices. |     | By fine- |
| ---------- | -------- | --- | ----- | --------------- | --- | ------------- | ------------ | ------- | --------- | ----------- | -------- | --- | -------- |
| Japan, the | Ministry | of  | Land, | Infrastructure, |     | Transport and |              |         |           |             |          |     |          |
|            |          |     |       |                 |     |               | tuning these | models  | on local  | trajectory  | data,    | we  | combine  |
*Accepted at the 2nd Workshop on AI for Urban Planning theirgeneralreasoningcapabilitieswithspecificknowledge
(AI4UP)atAAAI-26,Singapore,January2026. aboutadestination’slayoutandpatterns.Theapproachpro-

cesses contextual information naturally through text, de- MPE(Liangetal.2024)demonstratedpredictionunderpub-
scribing weather, fatigue, mobility availability, and prefer- liceventsusingtextualdescriptions.
enceswithoutmanualfeatureengineering.Thisenablespre- However, most research on LLM agents operates within
dictionevenforundersampledscenariosbyleveragingcom- synthetic environments or focuses on zero-shot prediction
monsensereasoningtointerpolatebetweenobservations. without fine-tuning on local trajectories. Validation against
We evaluate this approach using field experiment data fine-grained, real-world behavioral data from live field ex-
|               |     |        |       |          |           |          | periments |     | in specific | destinations |     | is  | limited. | It remains | un- |
| ------------- | --- | ------ | ----- | -------- | --------- | -------- | --------- | --- | ----------- | ------------ | --- | --- | -------- | ---------- | --- |
| from Wakayama |     | Castle | Park, | where we | collected | detailed |           |     |             |              |     |     |          |            |     |
trajectories from 566 tourists with rich contextual informa- clear whether LLMs can capture the complex, context-
tion. Our fine-tuned Llama-3.1-8B model achieves 49.1% dependent decisions of tourists in real-world settings and
next-POI prediction accuracy, substantially outperforming leverage their commonsense reasoning to generalize to un-
traditional baselines while maintaining strong generaliza- observedscenarioswithinthatspecificlocation.
tiontorarecontexts.Themodeldemonstratesrobustperfor-
Methodology
| mance on | undersampledscenarios |     |     | like | rainy days | and gen- |     |     |     |     |     |     |     |     |     |
| -------- | --------------------- | --- | --- | ---- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
erates coherent multi-step trajectories. These results estab- ProblemFormulation
lishthefeasibilityofusingLLMsasahigh-fidelitybehavior
Weformulatetouristtrajectorypredictionasconditionalse-
model.Whilethispaperfocusesonpredictiveaccuracy,this
h(u)
model serves as a crucial component for future counterfac- quence generation. Each trajectory consists of time-
orderedPOIvisits:
tualsimulationstoevaluatemobilityinterventions,opening
h(u)
newpossibilitiesfordestinationmanagement. ={(p ,t ,a ,c ),...,(p ,t ,a ,c )}
|     |     |     |     |     |     |     |        |     |                 | 1 1 | 1 1            |     | T T | T T          |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------------- | --- | -------------- | --- | --- | ------------ | --- |
|     |     |     |     |     |     |     | wherep |     | denotesthePOI,t |     | thevisittime,a |     |     | thearea,andc |     |
|     |     |     |     |     |     |     |        | i   |                 |     | i              |     |     | i            | i   |
RelatedWork thecategory.Themodellearnstheconditionaldistribution:
| TouristBehaviorandNextPOIPrediction |     |     |     |     |     |     |     |     |     |     | T   |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:89)
|          |            |          |     |             |     |            |     | P(h|u,e;θ)= |     |     | P(p | ,t ,a | ,c |u,e,h | ;θ) |     |
| -------- | ---------- | -------- | --- | ----------- | --- | ---------- | --- | ----------- | --- | --- | --- | ----- | --------- | --- | --- |
|          |            |          |     |             |     |            |     |             |     |     |     | i i   | i i       | <i  |     |
| Research | on tourist | mobility |     | has focused | on  | Next Point |     |             |     |     |     |       |           |     |     |
i=1
| of Interest | (POI) | prediction, | primarily |     | using | check-in data |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | ----------- | --------- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereurepresentstouristpersona(age,gender,grouptype),
| from Location-Based |     | Social | Networks |     | (LBSNs). | This field |     |          |               |     |            |     |           |        |     |
| ------------------- | --- | ------ | -------- | --- | -------- | ---------- | --- | -------- | ------------- | --- | ---------- | --- | --------- | ------ | --- |
|                     |     |        |          |     |          |            | e   | captures | environmental |     | conditions |     | (weather, | time), | and |
evolvedfromclassicalstatisticalmodelslikeMarkovchains
h denotesvisithistorybeforestepi.
| tomorecomplexdeeplearningarchitectures. |     |     |     |     |     |     | <i  |     |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Markov models are constrained by their memoryless as- DataCollectionandPreprocessing
| sumption  | and suffer | from    | extreme | data       | sparsity  | when ex- |     |           |     |              |     |             |     |        |         |
| --------- | ---------- | ------- | ------- | ---------- | --------- | -------- | --- | --------- | --- | ------------ | --- | ----------- | --- | ------ | ------- |
|           |            |         |         |            |           |          | We  | collected | 566 | trajectories |     | at Wakayama |     | Castle | Park in |
| tended to | higher     | orders, | failing | to capture | long-term | pref-    |     |           |     |              |     |             |     |        |         |
December2023duringaGreenSlowMobilitypilotprogram
| erences (Feng | et  | al. 2018). | Economic |     | frameworks | such as |         |     |         |      |          |     |                |     |          |
| ------------- | --- | ---------- | -------- | --- | ---------- | ------- | ------- | --- | ------- | ---- | -------- | --- | -------------- | --- | -------- |
|               |     |            |          |     |            |         | (Figure |     | 1). The | park | contains | 68  | POIs including |     | the cas- |
discretechoicemodels(Train2009)canexplicitlymodelra-
|     |     |     |     |     |     |     | tle | tower, | Momijidani |     | Garden, | zoo, | museums, | restaurants, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | ------- | ---- | -------- | ------------ | --- |
tionaldecisionsbutstrugglewiththevaststatespaceofPOI
|     |     |     |     |     |     |     | and | rest | facilities. | Data | came | from | two sources: |     | 87 GPS- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | ---- | ---- | ---- | ------------ | --- | ------- |
choices.
|               |       |          |              |             |          |              | tracked    | participants |              | (1-second |      | intervals) | and           | 479   | QR code   |
| ------------- | ----- | -------- | ------------ | ----------- | -------- | ------------ | ---------- | ------------ | ------------ | --------- | ---- | ---------- | ------------- | ----- | --------- |
| Deep learning |       | models   | such         | as DeepMove |          | (Feng et al. |            |              |              |           |      |            |               |       |           |
|               |       |          |              |             |          |              | stamp      | rally        | participants |           | who  | scanned    | codes         | at 37 | major at- |
| 2018) and     | KGDAE | (Gao     | et al.       | 2023)       | achieved | higher ac-   |            |              |              |           |      |            |               |       |           |
|               |       |          |              |             |          |              | tractions. |              | We added     | 31        | POIs | from       | OpenStreetMap |       | (cafes,   |
| curacy but    | face  | critical | limitations. | These       | include  | massive      |            |              |              |           |      |            |               |       |           |
stores,restrooms,hotels)forcomprehensivecoverage.
datarequirementsunsuitableforindividualdestinations,an
|     |     |     |     |     |     |     |     | Demographics |     | were | collected | via | exit surveys. |     | Missing |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | --------- | --- | ------------- | --- | ------- |
inabilitytoprocesscontextualtext,andpoorgeneralization
|     |     |     |     |     |     |     | attributes |     | (18% | of samples) |     | were | inferred | using | GPT-4o |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ----------- | --- | ---- | -------- | ----- | ------ |
tounobservedscenarios.
|     |     |     |     |     |     |     | based | on   | visit patterns |         | and timestamps. |     | GPS      | traces | under-  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | -------------- | ------- | --------------- | --- | -------- | ------ | ------- |
|     |     |     |     |     |     |     | went  | stop | detection      | (within |                 | 10m | for over | 60s)   | and POI |
LLMsforBehaviorPredictionandSimulation
|     |     |     |     |     |     |     | matching |     | (nearest | within | 25m). | QR  | sequences | were | pro- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------ | ----- | --- | --------- | ---- | ---- |
Recent advances in Large Language Models have demon- cessed directly after deduplication. Both sources yielded
strated their potential for behavioral modeling beyond tra- unifiedrepresentationswithPOInames,timestamps,areas,
andcategories,augmentedwithweatherdata.Thecombined
| ditional NLP | tasks | (Brown | et  | al. 2020). | The | Generative |     |     |     |     |     |     |     |     |     |
| ------------ | ----- | ------ | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Agents framework (Park et al. 2023) showed that LLM- dataset averages 7.7 POI visits over 58 minutes, ranging
poweredagentscouldproducebelievabledailyroutinesand from2to40POIsand33minutesto5.6hours.
socialinteractionswithoutexplicitprogramming,maintain-
ing memories, reflecting on experiences, and planning ac- ModelArchitectureandTextRepresentation
tivities using commonsense reasoning rather than predeter- Wefine-tunedLlama-3.1-8B,extendingitsvocabularywith
mined rules. LLMs have been applied directly to mobil- special tokens for all POI names, areas, categories, and
ity prediction. LLM-Mob (Wang et al. 2023) achieved the structuraltags.Tokenembeddingswereinitializedbyaver-
first zero-shot next location prediction, harnessing the pre- agingconstituentsubwordsfromtheoriginaltokenizer.Tra-
trained geographical and social knowledge of GPT-3.5/4. jectoriesareencodedasstructuredtext(Figure2).Eachvisit
AgentMove(Fengetal.2025)advancedthiswithanagentic linecontainstimestamp,action,area,category,andPOI,pre-
framework for worldwide prediction, outperforming base- serving sequential dependencies with rich contextual infor-
| linesacross12citieswithoutcity-specificretraining.LLM- |     |     |     |     |     |     | mation. |     |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |

mentswereconductedonaserverwithtwoNVIDIAA6000
GPUs.
BaselinesincludedMarkovModels(1stand5thorder),a
2-stateHiddenMarkovModel,andGPT-4oinzero-shotand
|     |     |     |     |     | fine-tuned    | configurations |                        | using | OpenAI’s           |              | fine-tuning | API.    |
| --- | --- | --- | --- | --- | ------------- | -------------- | ---------------------- | ----- | ------------------ | ------------ | ----------- | ------- |
|     |     |     |     |     | We also       | compared       | against                |       | Llama-3-Swallow-8B |              | (Okazaki    |         |
|     |     |     |     |     | et al. 2024), |                | a Japanese-specialized |       |                    | variant      | of Llama-3. |         |
|     |     |     |     |     | Since our     | field          | site                   | is a  | Japanese           | destination, |             | Swallow |
testswhetherJapanese-specificpre-trainingprovidesadvan-
tagesovergeneralmultilingualmodels.Forfaircomparison,
|     |     |     |     |     | Swallow | used | identical | QLoRA | settings |     | to our Llama-3.1 |     |
| --- | --- | --- | --- | --- | ------- | ---- | --------- | ----- | -------- | --- | ---------------- | --- |
model.
|     |     |     |     |     | Evaluation | metrics     |     | included           | Accuracy@1 |     | for     | POI and |
| --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------------------ | ---------- | --- | ------- | ------- |
|     |     |     |     |     | category   | prediction, |     | and sequence-level |            |     | metrics | (n-gram |
overlap,BLEU,normalizedLevenshteindistance)forcoher-
enceassessment.
Figure1:DistributionofPOIsatWakayamaCastlePark PredictionPerformance
|     |     |     |     |     | Figure 3 | presents | prediction |     | accuracy | across | methods. | Sta- |
| --- | --- | --- | --- | --- | -------- | -------- | ---------- | --- | -------- | ------ | -------- | ---- |
# persona and environment, fixed for the trajectory tistical methods achieved limited performance: first-order
<PERSONA>30s, Male</PERSONA><ENV>Sunny day</ENV> Markovreached9.0%(memorylessassumption),fifth-order
# one line per POI visit, in time order improvedto15.3%(butsuffereddatasparsitywith68POIs),
<time>09:55</time><action>visit</action><area>Castle
andHiddenMarkovModelachieved11.0%.
| Tower | Area</area><category>Historic |     | Site</category |     |     |     |     |     |     |     |     |     |
| ----- | ----------------------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Zero-shotGPT-4oachieved18.7%,showingsomegener-
| ><POI>Wakayama | Castle | Tenshukaku</POI> |     |     |     |     |     |     |     |     |     |     |
| -------------- | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alizationfrompre-trainingalone.Fine-tuningviaOpenAI’s
<time>10:25</time><action>visit</action><area>Garden
|     |     |     |     |     | API improved |     | this to | 35.2%, | confirming |     | the value | of local |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | ------ | ---------- | --- | --------- | -------- |
Area</area><category>Garden</category><POI>
adaptationthoughstillsubstantiallybelowourresults.
| Momijidani | Garden</POI>        |     |                  |        |                |                 |           |           |               |                   |               |          |
| ---------- | ------------------- | --- | ---------------- | ------ | -------------- | --------------- | --------- | --------- | ------------- | ----------------- | ------------- | -------- |
| ...        |                     |     |                  |        | Our fine-tuned |                 | Llama-3.1 |           | achieved      | 49.1%             | POI           | accuracy |
|            |                     |     |                  |        | and 55.4%      | category        |           | accuracy, | substantially |                   | outperforming |          |
|            |                     |     |                  |        | all baselines. | Llama-3-Swallow |           |           | achieved      |                   | 39.8%         | POI and  |
| Figure 2:  | Text representation |     | of a trajectory. | Angle- |                |                 |           |           |               |                   |               |          |
|            |                     |     |                  |        | 45.8% category |                 | accuracy. |           | Despite       | Japanese-specific |               | pre-     |
bracketedtagsareaddedtothevocabularyasspecialtokens;
|     |     |     |     |     | training, | Swallow | underperformed |     |     | Llama-3.1, | suggesting |     |
| --- | --- | --- | --- | --- | --------- | ------- | -------------- | --- | --- | ---------- | ---------- | --- |
#linesareannotations.
thatthescaleanddiversityofmultilingualpre-trainingout-
|     |     |     |     |     | weigh language-specific |     |     | advantages |     | for | this task. | This im- |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | ---------- | --- | --- | ---------- | -------- |
pliesthatgeneralbehavioralunderstandingfrommassivedi-
TrainingProcedure
versecorporaismorevaluablethanlinguisticspecialization
During training, the model generates complete trajectories whenreasoningaboutphysicalmovementpatterns.
| given persona | and environment |     | via supervised | fine-tuning |               |     |     |         |     |     |          |          |
| ------------- | --------------- | --- | -------------- | ----------- | ------------- | --- | --- | ------- | --- | --- | -------- | -------- |
|               |                 |     |                |             | The six-point |     | gap | between | POI | and | category | accuracy |
with standard cross-entropy loss. At inference, we provide suggeststhatwhilegeneralvisitorintentionsarepredictable,
visit history and prompt for the next POI. Specifically, we specific choices among similar options retain inherent un-
inputuptothelastareatagandgeneratethesubsequentcat- certainty. The strong performance stems from combining
egoryandPOItags.WeemployedQLoRA(QuantizedLow- pre-trained commonsense knowledge (e.g., seeking lunch
| Rank Adaptation) | with rank | r   | = 32 and scaling | α = 64. |            |            |     |        |        |     |              |      |
| ---------------- | --------- | --- | ---------------- | ------- | ---------- | ---------- | --- | ------ | ------ | --- | ------------ | ---- |
|                  |           |     |                  |         | at midday, | preferring |     | indoor | venues |     | during rain) | with |
Crucially, we applied adapters not only to attention projec- destination-specificlearningthroughQLoRAfine-tuning.
| tion layers | (Query, Key, | Value, | Output) but | also to embed- |     |     |     |     |     |     |     |     |
| ----------- | ------------ | ------ | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ding (embed tokens) and output (lm head) layers. This in- SequenceGenerationQuality
| clusion proved | essential | for learning | effective | representa- |     |     |     |     |     |     |     |     |
| -------------- | --------- | ------------ | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure4showssequence-levelmetrics.Llama-3.1achieved
| tions of newly | added POI | tokens. | Training | used AdamW |              |     |          |       |       |     |       |         |
| -------------- | --------- | ------- | -------- | ---------- | ------------ | --- | -------- | ----- | ----- | --- | ----- | ------- |
|                |           |         |          |            | 31.2% 4-gram |     | overlap, | 25.8% | BLEU, | and | 47.0% | normal- |
optimizerwithlearningrate2×10−5,batchsize8,andran
|     |     |     |     |     | ized Levenshtein |     | distance, |     | capturing | longer | sequential | pat- |
| --- | --- | --- | --- | --- | ---------------- | --- | --------- | --- | --------- | ------ | ---------- | ---- |
for 10 epochs. We split 80% (453 tourists) for training and terns.Generatedtrajectoriesexhibitrealisticpatterns:morn-
20%(113tourists)fortesting,maintainingtourist-levelsep- ingvisitstomajorattractions,middaydining,afternoonrest
arationtopreventdataleakage. areas. Average length (7.2 POIs) matches real data (7.7)
withoutexplicitconstraints.Anomalousoutputsoccurredin
|     | Experiments |     |     |     | only5.4%ofgenerations. |             |     |     |              |     |           |       |
| --- | ----------- | --- | --- | --- | ---------------------- | ----------- | --- | --- | ------------ | --- | --------- | ----- |
|     |             |     |     |     | The model              | generalizes |     | to  | undersampled |     | contexts. | On 12 |
ExperimentalSetup
|     |     |     |     |     | rainy test | samples, | our | model | maintained |     | 41.7% | accuracy |
| --- | --- | --- | --- | --- | ---------- | -------- | --- | ----- | ---------- | --- | ----- | -------- |
We evaluated 566 tourist trajectories from Wakayama Cas- versus8.3%forMarkovmodels,correctlyincreasingindoor
tleParkwith80%training(453tourists)and20%test(113 predictionswhilereducinggardenvisits.Lunch-timepredic-
tourists) splits maintaining tourist-level separation. Experi- tionsachieved62.3%categoryaccuracyfordining,demon-

60 handles weather and time variations but cannot predict be-
|     |     |     |     |     |     |     | havior at | entirely | new | POIs | without | descriptions | or reason |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ---- | ------- | ------------ | --------- |
49.1%
50
|                |     |     |     |     |       |     | about major                                             | infrastructure |     | changes. | Addressing |     | these may |
| -------------- | --- | --- | --- | --- | ----- | --- | ------------------------------------------------------- | -------------- | --- | -------- | ---------- | --- | --------- |
| )%( 1@ycaruccA |     |     |     |     | 39.8% |     |                                                         |                |     |          |            |     |           |
| 40             |     |     |     |     |       |     | requirearchitecturalextensionssuchasretrieval-augmented |                |     |          |            |     |           |
generationorfew-shotadaptationtechniques.Despitethese
| 30  |     |     |     |     |     |     | limitations,thisworkprovidesafoundationforLLM-based |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
22.5%
|     |     |     |     |     |     |     | destination | management |     | tools | that | could | transform how |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ----- | ---- | ----- | ------------- |
20
15.3%
11.0% tourism planners evaluate and optimize mobility interven-
| 10  | 9.0% |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tions.
2.3%
| 0   | MM MM | HMM | GPT-4o | GPT-4oLlama-3-SwallowLlama-3.1 |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | ------ | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(1st) (5th) (2-state) (zero-shot) (fine-tuned) (fine-tuned) (fine-tuned) Acknowledgments
| Figure   | 3: Next POI | prediction | accuracy | comparison |     | across |           |     |           |     |        |        |           |
| -------- | ----------- | ---------- | -------- | ---------- | --- | ------ | --------- | --- | --------- | --- | ------ | ------ | --------- |
|          |             |            |          |            |     |        | This work | was | supported |     | by JST | PRESTO | Grant JP- |
| methods. |             |            |          |            |     |        | MJPR2361. |     |           |     |        |        |           |
References
60
Llama-3.1
52.8%
Brown,T.B.;Mann,B.;Ryder,N.;Subbiah,M.;Kaplan,J.;
50
|              |     | 44.3% |       |     |     |     | Dhariwal,P.;Neelakantan,A.;Shyam,P.;Sastry,G.;Askell, |             |               |              |              |         |               |
| ------------ | --- | ----- | ----- | --- | --- | --- | ----------------------------------------------------- | ----------- | ------------- | ------------ | ------------ | ------- | ------------- |
|              |     |       |       |     |     |     | A.; Agarwal,                                          | S.;         | Herbert-Voss, |              | A.; Krueger, |         | G.; Henighan, |
| )%( erocS 40 |     |       | 37.5% |     |     |     |                                                       |             |               |              |              |         |               |
|              |     |       |       |     |     |     | T.; Child,                                            | R.; Ramesh, |               | A.; Ziegler, | D.           | M.; Wu, | J.; Winter,   |
31.2%
30 C.; Hesse, C.; Chen, M.; Sigler, E.; Litwin, M.; Gray, S.;
25.8%
|     |     |     |     |     |     |     | Chess, B.; | Clark, | J.; Berner, |     | C.; McCandlish, |     | S.; Radford, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------- | --- | --------------- | --- | ------------ |
20
|     |     |     |     |     |     |     | A.; Sutskever,          |     | I.; and | Amodei,                      | D. 2020. | Language | mod- |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | ------- | ---------------------------- | -------- | -------- | ---- |
|     |     |     |     |     |     |     | elsarefew-shotlearners. |     |         | InProceedingsofthe34thInter- |          |          |      |
10
nationalConferenceonNeuralInformationProcessingSys-
tems,NIPS’20.
0
|     | 1-gram | 2-gram | 3-gram | 4-gram | BLEU |     |     |     |     |     |     |     |     |
| --- | ------ | ------ | ------ | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Metric Feng, J.; Du, Y.; Zhao, J.; and Li, Y. 2025. Agentmove: A
largelanguagemodelbasedagenticframeworkforzero-shot
| Figure | 4: POI-Sequence-level |     | evaluation | metrics | for | Fine- |               |             |     |     |             |     |               |
| ------ | --------------------- | --- | ---------- | ------- | --- | ----- | ------------- | ----------- | --- | --- | ----------- | --- | ------------- |
|        |                       |     |            |         |     |       | next location | prediction. |     | In  | Proceedings | of  | the 2025 Con- |
tunedLlama-3.1.
|     |     |     |     |     |     |     | ference | of the Nations |     | of the | Americas | Chapter | of the As- |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ------ | -------- | ------- | ---------- |
sociationforComputationalLinguistics:HumanLanguage
Technologies(Volume1:LongPapers),1322–1338.
stratingeffectivetemporaladaptationthroughcommonsense
| reasoning. |     |     |     |     |     |     | Feng,J.;Li,Y.;Zhang,C.;Sun,F.;Meng,F.;Guo,A.;and |                 |           |            |                |       |               |
| ---------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --------------- | --------- | ---------- | -------------- | ----- | ------------- |
|            |     |     |     |     |     |     | Jin, D.                                          | 2018. Deepmove: |           | Predicting |                | human | mobility with |
|            |     |     |     |     |     |     | attentional                                      | recurrent       | networks. |            | In Proceedings |       | of the 2018   |
Conclusion
worldwidewebconference,1459–1468.
| This work | demonstrates    | the | feasibility | of         | using fine-tuned |     |          |       |         |                |     |         |              |
| --------- | --------------- | --- | ----------- | ---------- | ---------------- | --- | -------- | ----- | ------- | -------------- | --- | ------- | ------------ |
|           |                 |     |             |            |                  |     | Gao, J.; | Peng, | P.; Lu, | F.; Claramunt, |     | C.; and | Xu, Y. 2023. |
| Large     | Language Models | for | tourist     | trajectory | prediction       | at  |          |       |         |                |     |         |              |
regional destinations. Our Llama-3.1-8B model achieved Towards travel recommendation interpretability: Disentan-
49.1% next-POI accuracy on 566 real-world trajectories glingtouristdecision-makingprocessviaknowledgegraph.
from Wakayama Castle Park, substantially outperforming Inf.Process.Manage.,60(4).
traditional statistical and neural baselines. The model suc- Liang,Y.;Liu,Y.;Wang,X.;andZhao,Z.2024. Exploring
cessfully leverages pre-trained commonsense reasoning to largelanguagemodelsforhumanmobilitypredictionunder
generalizetoundersampledcontextssuchasrainydaysand publicevents. Computers,EnvironmentandUrbanSystems,
| generatescoherentmulti-steptrajectoriesthatreflectrealis- |     |     |     |     |     |     | 112:102153. |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
ticvisitorbehaviorpatterns.
|     |     |     |     |     |     |     | Okazaki, | N.; Hattori, | K.; | Shota, | H.; | Iida, H.; | Ohi, M.; Fu- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ------ | --- | --------- | ------------ |
This work establishes predictive capability as a neces- jii, K.; Nakamura, T.; Loem, M.; Yokota, R.; and Mizuki,
| sary foundation | for                | counterfactual |              | generation    | but does | not    |             |                                         |     |             |     |           |               |
| --------------- | ------------------ | -------------- | ------------ | ------------- | -------- | ------ | ----------- | --------------------------------------- | --- | ----------- | --- | --------- | ------------- |
|                 |                    |                |              |               |          |        | S.2024.     | BuildingaLargeJapaneseWebCorpusforLarge |     |             |     |           |               |
| validate        | causal claims.     | Predicting     |              | what tourists | would    | do     |             |                                         |     |             |     |           |               |
|                 |                    |                |              |               |          |        | Language    | Models.                                 | In  | Proceedings | of  | the First | Conference    |
| under           | current conditions |                | differs from | estimating    |          | behav- |             |                                         |     |             |     |           |               |
|                 |                    |                |              |               |          |        | on Language | Modeling,                               |     | COLM,       | (to | appear).  | University of |
ioralchangesunderhypotheticalinterventions.Futurework
Pennsylvania,USA.
| should | generate counterfactuals |     | by  | modifying | input | condi- |     |     |     |     |     |     |     |
| ------ | ------------------------ | --- | --- | --------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
Park,J.S.;O’Brien,J.C.;Cai,C.J.;Morris,M.R.;Liang,
tions(e.g.,addingshuttleserviceavailabilitytothecontext)
|     |     |     |     |     |     |     | P.; and | Bernstein, | M. S. | 2023. | Generative | Agents: | Interac- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----- | ----- | ---------- | ------- | -------- |
andvalidatepredictionsagainstA/Btestdataorrandomized
|     |     |     |     |     |     |     | tive Simulacra |     | of Human | Behavior. |     | In In the | 36th Annual |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --------- | --- | --------- | ----------- |
fieldtrialstoenablecausalevaluationofmobilityinterven-
| tions. |     |     |     |     |     |     | ACM Symposium |     | on User | Interface | Software |     | and Technol- |
| ------ | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --------- | -------- | --- | ------------ |
Several limitations remain. Missing persona attributes ogy(UIST’23),UIST’23.
(18%)wereinferredviaGPT-4o,thoughevaluationonman- Train, K. E. 2009. Discrete Choice Methods with Simula-
ually verified subsets showed minimal impact. The model tion. CambridgeUniversityPress,2edition.

| UNWTO.       | 2018. ‘Overtourism’?                   |        | Understanding       | and Man- |
| ------------ | -------------------------------------- | ------ | ------------------- | -------- |
| aging Urban  | Tourism                                | Growth | beyond Perceptions: | Execu-   |
| tiveSummary. | Madrid,Spain:WorldTourismOrganization  |        |                     |          |
| (UNWTO).     | EISBN978-92-844-2007-0;ISBN978-92-844- |        |                     |          |
2006-3.
| Wang,X.;Fang,M.;Zeng,Z.;andCheng,T.2023. |     |     |     | Where |
| ---------------------------------------- | --- | --- | --- | ----- |
wouldigonext?largelanguagemodelsashumanmobility
| predictors.                       | arXivpreprintarXiv:2308.15197. |       |                    |         |
| --------------------------------- | ------------------------------ | ----- | ------------------ | ------- |
| Yang,Y.;Jiang,L.;andZhang,Z.2021. |                                |       | Touristsonshared   |         |
| bikes: Can                        | bike-sharing                   | boost | attraction demand? | Tourism |
Management,86:104328.
---- END DOCUMENT ----
