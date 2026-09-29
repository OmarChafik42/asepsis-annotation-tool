Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
1
Rethinking the Foundations of Two-Sided AI Models for 6G
Yongjeong Oh, Zihan Chen, Timothy J. O’Shea, Junyong Shin, Jinho Choi, Yo-Seb Jeon, and Jihong Park
Abstract—Fornext-generationairinterfaces,two-sidedartificial practical use cases such as channel state information (CSI)
intelligence(AI) models have received growing attention, with AI feedback [4], [5]. In translating these academic advances into
modelsdeployedat boththetransmitterandreceiver forefficient
real-worlddeployments,sucheffortshavenaturallyadoptedthe
channelfeedbackanddatacommunication.However,theirpracti-
methodologicalfoundationsestablished in the literature. These
caldeploymentiscomplicatedbyassumptionscommonlymadein
existing studies, including isolation from legacy users, training foundationstypicallyassumethatatwo-sidedmodeloperatesin
under predefined channel conditions, and gradient-based fine- isolationfromlegacyUEs,thattrainingisperformedunderpre-
tuning requiring substantial cross-vendor communication. This definedchannelconditions,andthatthetransmitterandreceiver
article revisits these assumptions and presents practical alterna-
modelsarefine-tunedthroughbackpropagation.Althoughthese
tives. First, for legacy coexistence, we integrate two-sided model
standard assumptions simplify model development and help
processingintothe5GNewRadio(NR)protocolstackandvalidate
its operation alongside conventional NR on a real-world testbed. isolate algorithmic gains, they merely reflect specific design
Second,insteadoftrainingunderamassivenumberofpredefined choices rather than intrinsic or necessary properties of two-
channelconditions,weconstructacompactmodeltablebyjointly sided models.
optimizing two-sided models with trainable surrogate channels,
When carried into real-world deployments, these inherited
and select the best model according to the current channel
foundations give rise to significant practical challenges. Iso-
conditiontoenablechanneladaptationwithhightaskperformance
and low training/storage overhead. Finally, unlike existing fine- lation from legacy UEs does not account for coexistence
tuningthatexchangeslargegradientvectorscontainingpotentially with conventional radio access technologies (RATs). Training
private model information, we present gradient-free zeroth-order under prescribed channel conditions creates a trade-off be-
fine-tuning that requires only scalar feedback, facilitating multi-
tween specialization and generalization in channel adaptation,
vendor interoperability. Together, these approaches advance the
as maintaining channel-specific models increases training and
practical deployment of two-sided AI models while highlighting
key open challenges. storage costs, whereas a single model trained across diverse
conditions compromises site-specific performance. Gradient-
basedfine-tuningbecomesdifficultwhentheUE-sideandgNB-
I. INTRODUCTION side models are developed by different vendors, as exchang-
As wireless networks advance toward more intelligent and ing model parameters or gradients risks exposing proprietary
adaptive air interfaces, artificial intelligence (AI) is being model information while adding communication and memory
integrated ever more deeply into both the transmitter and the overhead.
receiver[1]. This trendhas spurredseveralresearch directions, Theseobservationsmotivatea fundamentalrethinkingof the
includingneuraltransceivers,deepjointsource-channelcoding, foundations of two-sided AI models. From this perspective,
and task-oriented semantic communication [2], [3]. Although this article revisits the prevailing assumptions and discusses
these directions differ in their objectives and system settings, practical alternatives for coexistence, channel adaptation, and
many rely on a common architecture in which transmitter-side model updates. Specifically, we examine (i) how two-sided
and receiver-side AI models are designed to operate jointly. models can coexist with legacy 5G New Radio (NR) systems,
The 3rd Generation Partnership Project (3GPP) refers to such (ii) how they can adapt to diverse channel conditions without
paired models as two-sided AI models, particularly when the relying on channel-specific training, and (iii) how transmitter-
models are deployed across the user equipment (UE) and the side and receiver-side models can be updated across vendors
next-generation Node B (gNB) [4]. without gradient backpropagation. Finally, we discuss open
While early academic research on two-sided models pri- research challengesand future directions toward practical two-
marily focused on demonstrating performance gains under sided AI models for next-generationwireless networks.
controlled training and evaluation settings, recent industry and
standardization efforts have begun exploring their use for II. FROM FOUNDATIONAL ASSUMPTIONS TOPRACTICAL
LIMITATIONS
Y. Oh, Z. Chen, and J. Park are with Singapore University of Tech-
In this section, we examine the common foundational as-
nology and Design, Singapore 487372 (email: {yongjeong oh, zihan chen,
jihong park}@sutd.edu.sg). sumptions underlying two-sided models and their limitations
T. J. O’Shea is with DeepSig Inc., Arlington, VA 22203, USA (email: in practical deployments, with respect to legacy coexistence,
tim@deepsig.ai)
channel adaptation, and multi-vendor interoperability.
J. Shin and Y.-S. Jeon are with POSTECH, Pohang, Gyeongbuk 37673,
Republic ofKorea(email:{sjyong, yoseb.jeon}@postech.ac.kr). Legacy Coexistence: Two-sided models are often studied
J. Choi is with the University of Adelaide, SA 5005, Australia (email:
under the assumption that all participating UEs support the
jinho.choi@adelaide.edu.au).
(Corresponding authors:J.Park,Y.-S.Jeon). same AI-native air interface. This assumption conflicts with
6202
guA
42
]PS.ssee[
1v81922.8062:viXra

2
Fig.1. Overview ofthefoundational assumptions, deployment challenges, andcorresponding practical alternatives forlegacycoexistence, channel adaptation,
| andmulti-vendor | interoperability. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the emerging 6G deployment direction, in which AI-native deployed by the same vendor, requiring joint training or fine-
6G operation must coexist with legacy 5G NR, for example tuning across vendors. Existing two-sided models typically
through Multi-RAT Spectrum Sharing (MRSS) [6]. Moving rely on gradient-based joint training, which 3GPP classifies
[4]1.
beyondthis assumptiontherefore requiresvalidating two-sided into Type 1 and Type 2 In Type 1, both models are
modelsinapracticalcoexistencescenario,wheretwo-sidedand trainedat either the UE or the gNB, requiringone modelto be
conventional NR UEs operate simultaneously. Such validation transferred.InType2,eachmodelremainsatitsrespectiveside,
should demonstrate full-stack compatibility, from physical- whileintermediatemodelfeaturesandgradientsareexchanged.
layer (PHY) processing to higher-layer procedures, while pre- Unfortunately,both approachesbecome impractical when ven-
servingtheperformanceadvantagesoftwo-sidedmodelsunder dors are unwilling to disclose proprietary model information.
coexistence. Type1exposesthemodelarchitectureandparameters,whereas
Type2allowsexchangedfeaturesandgradientstobeexploited
| Channel | Adaptation: |     | For two-sided |     | models, adapting |     | to  |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
varyingchannelconditionsisa keyaspectofAI modellifecy- for model output inference and adversarial attacks [8], [9].
|                     |     |              |     |                  |     |         | Moreover, |     | exchanging | models, | features, | or  | gradients | incurs |
| ------------------- | --- | ------------ | --- | ---------------- | --- | ------- | --------- | --- | ---------- | ------- | --------- | --- | --------- | ------ |
| cle management(LCM) |     | [4].Existing |     | methodstypically |     | realize |           |     |            |         |           |     |           |        |
suchadaptationbyincorporatingchannelconditionsintomodel substantialcommunicationoverhead,whileType2alsorequires
transmitter-sideintermediateactivationstoberetaineduntilthe
training[3],[7].Onerepresentativeapproachisone-model-fits-
|            |            |         |         |     |                    |     | corresponding |     | gradients | are | received, | imposing | a   | significant |
| ---------- | ---------- | ------- | ------- | --- | ------------------ | --- | ------------- | --- | --------- | --- | --------- | -------- | --- | ----------- |
| one, where | a separate | modelis | trained | for | each channelcondi- |     |               |     |           |     |           |          |     |             |
tion. Multiple models are prepared in advance, and adaptation memory burden on resource-constraineddevices.
isperformedbyselectingthemodelbestmatchedtothecurrent Motivated by the deployment challenges associated with
channel condition [3]. This approach provides strong channel- these foundational assumptions of two-sided models, as sum-
|                         |     |                           |     |     |     |           | marized | in  | Fig. 1, | we propose | practical | alternatives |     | in the |
| ----------------------- | --- | ------------------------- | --- | --- | --- | --------- | ------- | --- | ------- | ---------- | --------- | ------------ | --- | ------ |
| specific performancebut |     | requiresextensivetraining |     |     |     | and model |         |     |         |            |           |              |     |        |
storage to cover diverse channel conditions, limiting its prac- following sections.
| ticality for | resource-constrained |     |     | devices. | Another approach |     | is  |     |     |     |     |     |     |     |
| ------------ | -------------------- | --- | --- | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
one-model-fits-all,whereasinglemodelisjointlytrainedacross III. INTEGRATIONINTOTHE NRPROTOCOL STACK FOR
multiple channel conditions, such as different signal-to-noise LEGACY COEXISTENCE
ratios (SNRs) [7]. Although this approach reduces storage Following the emerging 6G deployment direction [6], we
overheadby usinga single generalizedmodel,it requiresmore need to consider how two-sided models can be introduced
| extensive | training and | typically |     | sacrifices | performance | com- |       |            |              |     |               |     |         |         |
| --------- | ------------ | --------- | --- | ---------- | ----------- | ---- | ----- | ---------- | ------------ | --- | ------------- | --- | ------- | ------- |
|           |              |           |     |            |             |      | while | preserving | conventional |     | NR operation. |     | To this | end, we |
pared with channel-specificmodels. Both approachestherefore propose a capability-dependent PHY integration architecture
| entail substantial | deployment   |         | tradeoffs,  |     | and neither | offers | a    |            |           |     |                  |     |       |             |
| ------------------ | ------------ | ------- | ----------- | --- | ----------- | ------ | ---- | ---------- | --------- | --- | ---------------- | --- | ----- | ----------- |
|                    |              |         |             |     |             |        | that | introduces | two-sided |     | model processing |     | as an | alternative |
| practical          | solution for | channel | adaptation. |     |             |        |      |            |           |     |                  |     |       |             |
13GPP
|                  |                   |               |     |              |              |             |             | also    | defines    | Type 3,  | which alternates | local              | training | between the |
| ---------------- | ----------------- | ------------- | --- | ------------ | ------------ | ----------- | ----------- | ------- | ---------- | -------- | ---------------- | ------------------ | -------- | ----------- |
| Multi-Vendor     | Interoperability: |               |     | In practical | deployments, |             |             |         |            |          |                  |                    |          |             |
|                  |                   |               |     |              |              |             | gNB         | and the | UE instead | of joint | training, but    | incurs substantial |          | performance |
| the transmitter- | and               | receiver-side |     | models       | are not      | necessarily | degradation | [4].    |            |          |                  |                    |          |             |

3
Fig. 2. Integration of the two-sided model into the NR protocol stack, demonstrated through a real-world testbed, along with its performance evaluation for
uplinkdatacommunication.
to selected conventional NR PHY-functions, preserving its establishment, and real-time InternetProtocoltraffic, including
performance advantage while retaining the conventional NR ping, secure shell, and throughput measurements, with round-
processing path without modification. trip times of 10–20 ms. These experiments demonstrate full-
To implement and validate this architecture, we integrate stack operation of the two-sided model within an operational
two-sided modelprocessinginto a real-worldtransceiverusing NR system while preserving conventional NR processing for
|              |         |       |            |     |         |       | legacy UEs. |     |     |     |
| ------------ | ------- | ----- | ---------- | --- | ------- | ----- | ----------- | --- | --- | --- |
| a full-stack | testbed | based | on DeepSig |     | OmniPHY | Axon, | as          |     |     |     |
illustrated in Fig. 2. The testbed comprises an open central Fig.2illustratestheoveralltestbedarchitecturetogetherwith
unit/distributed unit (OCUDU)-based gNB [10] running on an numerical results for uplink data transmission. In this experi-
NVIDIA DGX Spark and a software-defined UE. The radio- ment, we consider a 3GPP TR 38.901 rural macro channel
×
frequency front-end uses a USRP B210 operating in NR band with a 1 4 antenna configuration [11]. The conventional
|     |     |     |     |     |     |     | NR baseline | uses pilot-aided | linear minimum | mean squared |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------- | -------------- | ------------ |
n78witha20MHzbandwidth,30kHzsubcarrierspacing,and
split 8. The same OCUDU-based gNB also supports a WNC error (LMMSE)-Wiener channel estimation and an LMMSE
open radio unit over an O-RAN 7.2 fronthaul interface with equalizer. The numerical results in Fig. 2 compare the uplink
|            |       |        |      |     |     |     | throughputof | conventionalNR | and the two-sidedmodelunder |     |
| ---------- | ----- | ------ | ---- | --- | --- | --- | ------------ | -------------- | --------------------------- | --- |
| bandwidths | of up | to 100 | MHz. |     |     |     |              |                |                             |     |
TheimplementedgNBsupportstworeceptionmodesandse- different SNRs. Both throughput curves are obtained from a
|     |     |     |     |     |     |     | single gNB, | demonstrating | coexistence between | the two-sided |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ------------------- | ------------- |
lectstheappropriateprocessingpathaccordingtotheUE’stwo-
sided model capability. In the conventional mode, legacy UEs model and conventional NR operation for legacy UEs. Under
|            |           |          |     |            |        |        | this coexistence, | the two-sided  | model achieves | more than 4  |
| ---------- | --------- | -------- | --- | ---------- | ------ | ------ | ----------------- | -------------- | -------------- | ------------ |
| are served | using the | existing | NR  | processing | chain. | In the | two-              |                |                |              |
|            |           |          |     |            |        |        | times higher      | throughputthan | conventionalNR | underlow-SNR |
sidedmodelmode,theUE-sidemodelmapscodedbitsdirectly
| to complex-valuedsymbols |     |     | without | dedicated | pilots, | replacing | conditions. |     |     |     |
| ------------------------ | --- | --- | ------- | --------- | ------- | --------- | ----------- | --- | --- | --- |
conventionalquadratureamplitudemodulation(QAM)mapping
and pilot insertion while retaining NR resource-element (RE) IV. ADAPTIVE MODELSELECTIONFOR CHANNEL
ADAPTATION
mapping.AtthegNB,thecorrespondingreceivermodeljointly
performschannelestimationanddemapping,directlyproducing Channel adaptation is essential for reliable and efficient
| soft-bit | log-likelihood | ratios | (LLRs). | These | LLRs | are | passed        |               |                     |            |
| -------- | -------------- | ------ | ------- | ----- | ---- | --- | ------------- | ------------- | ------------------- | ---------- |
|          |                |        |         |       |      |     | communication | under varying | channel conditions. | While con- |
to the existing NR channel decoder, thereby enabling two- ventionalsystems can readily adaptthroughtable-based mech-
sided models for data communication with minimal PHY anisms, such as modulation and coding scheme (MCS) tables
modifications while maintaining the remaining NR processing in adaptive modulation and coding (AMC) and precoding
stack, including channel decoding. codebooks in beamforming, two-sided models are difficult to
Importantly,theintegrationextendsbeyondPHYprocessing. adaptrapidlywithoutsubstantialstorage,fine-tuningoverhead,
ThetestbedsupportsUEregistration,protocoldataunitsession or performance loss. To retain the short adaptation delay

4
Fig.3. TheAMSframework forchannel adaptation, alongwiththeMSCtableconstruction basedonjointoptimization ofthetwo-sided modelandtheSC.
Fig.4. ComparisonofPSNR,training time,andmodelstoragebetween theAMSframeworkandothertwo-sidedmodelschemesforanimagereconstruction
task.
and low computational overhead of table-based operation, we ital transmission, it is modeled as parallel binary symmetric
introduceanadaptivemodelselection(AMS)framework.AMS channelswithtrainablebit-flipprobabilities[13].The trainable
selectsthemodelbestmatchedtothecurrentchannelcondition SC parameters and the two-sided model are jointly optimized
from an offline-constructedtable containinga small numberof to minimize a weighted sum of the task loss and an SC
models together with their associated transmission parameters. regularization term. Without regularization, the SC converges
Unlike existing one-model-fits-one approaches that pre-train toatrivialerror-freechannelbecauselowerdistortionimproves
a separate model for each predefined channel condition [3], taskperformance.Theregularizationpreventsthisbypenalizing
[7],AMSreplacespredefinedchannelswithsurrogatechannels small SC parametersand encouragingnon-zerochanneldistor-
(SCs).TheseSCsarejointlytrainedwiththetwo-sidedmodels, tion. Each jointly optimized model-SC pair forms an entry in
followedbyinstantlymappingintotheactualchannelcondition themodel-and-SC(MSC)table.Varyingtheregularizationlevel
during operation. The number of SCs is much smaller than yields entries with different average channel distortion levels.
the number of possible channel conditions, enabling scalable During online operation, each trained SC is reproduced
adaptationacrossdiversechannelconditions,as investigatedin over the actual wireless channel by adjusting the transmission
[12], [13]. parameters.For analogtransmission,the trainednoise variance
Specifically, for two-sided models with analog channel in- isconvertedtoatargetSNR,whichismatchedthroughtransmit
puts, the SC is modeled as parallel additive white Gaussian powercontrol[12].Fordigitaltransmission,thetrainedbit-flip
noise channels with trainable noise variances [12]. For dig- probability is treated as a target bit error rate and matched

5
Fig.5. Thegradient-free zeroth-order fine-tuning frameworkformulti-vendor interoperability anditsperformance evaluation forCSIfeedback.
through transmit power and/or modulation control [13]. Under V. GRADIENT-FREE FINE-TUNING MULTI-VENDOR
FOR
the current channel condition, AMS determines the transmis- INTEROPERABILITY
| sion                                                | parameters |     | required | for each | MSC | entry | and identifies |     |              |     |                  |     |              |        |          |     |
| --------------------------------------------------- | ---------- | --- | -------- | -------- | --- | ----- | -------------- | --- | ------------ | --- | ---------------- | --- | ------------ | ------ | -------- | --- |
|                                                     |            |     |          |          |     |       |                |     | Multi-vendor |     | interoperability |     | of two-sided | models | requires |     |
| thosesatisfyingtheavailableresourceconstraints,such |            |     |          |          |     |       | astotal        |     |              |     |                  |     |              |        |          |     |
transmit power. Among the feasible entries, it selects the one joint fine-tuning of the transmitter- and receiver-side mod-
achieving the highest task performance. els held by different vendors. The current 3GPP Type 1
|     |     |     |     |     |     |     |     |     | and Type | 2 fine-tuning |     | approaches | [4] require   |     | the exchange |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ---------- | ------------- | --- | ------------ | --- |
|     |     |     |     |     |     |     |     |     | of model | parameters    | and | gradients, | respectively, |     | to perform   |     |
Fig.4presentsnumericalresultsforanimagereconstruction
|     |     |     |     |     |     |     |     |     | backpropagation, |     | which | may | raise privacy | concerns | and | incur |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | --- | ------------- | -------- | --- | ----- |
CIFAR-10
| task | on  | the |     | dataset. | The channel | follows | Rayleigh |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | -------- | ----------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
additionalmemoryandcommunicationoverhead.Toovercome
| fading | over | 64  | subcarriers | with | 16-QAM. | Training | time | is  |     |     |     |     |     |     |     |     |
| ------ | ---- | --- | ----------- | ---- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thislimitation,wepresentagradient-freefine-tuningframework
| measured |          | on an            | Intel Core | i7-12700               | CPU,     | an NVIDIA |         | RTX    |               |          |                  |                |              |           |              |       |
| -------- | -------- | ---------------- | ---------- | ---------------------- | -------- | --------- | ------- | ------ | ------------- | -------- | ---------------- | -------------- | ------------ | --------- | ------------ | ----- |
|          |          |                  |            |                        |          |           |         |        | that requires | only     | scalar           | feedback       | while        | reusing   | the existing |       |
| 3090     |          |                  | 32         |                        |          |           |         |        |               |          |                  |                |              |           |              |       |
|          | GPU,     | and              | GB         | RAM.                   | Three    | baseline  | schemes | are    |               |          |                  |                |              |           |              |       |
|          |          |                  |            |                        |          |           |         |        | communication |          | path for         | forward        | propagation. | The       | framework    |       |
| used     | for      | comparison.      |            | The one-model-fits-one |          | baseline  |         | trains |               |          |                  |                |              |           |              |       |
|          |          |                  |            |                        |          |           |         |        | is grounded   | in       | the zeroth-order |                | optimization | method    | [14],        | a     |
| a        | separate | channel-specific |            | model                  | for each | SNR,      | whereas | the    |               |          |                  |                |              |           |              |       |
|          |          |                  |            |                        |          |           |         |        | gradient-free | approach |                  | that estimates | a descent    | direction |              | using |
one-model-fits-allbaselinetrainsasinglerobustmodeloverthe
|     |     |     |     |     |     |     |     |     | only forward | evaluations |     | of the | loss. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ------ | ----- | --- | --- | --- |
0–30dBSNRrange.Na¨ıveAMSusesthreemodelstrainedover
A
the0–10,10–20,and20–30dBSNRranges.Taskperformance To illustrate, suppose a scenario in which Vendor and
B
|       |          |               |          |     |        |        |               |     | Vendor        | hold   | the transmitter-side |          | and receiver-side |            | models, |      |
| ----- | -------- | ------------- | -------- | --- | ------ | ------ | ------------- | --- | ------------- | ------ | -------------------- | -------- | ----------------- | ---------- | ------- | ---- |
| is    | measured | by            | the peak | SNR | (PSNR) | of the | reconstructed |     |               |        |                      |          |                   |            |         |      |
|       |          |               |          |     |        |        |               |     | respectively. | Vendor | A                    | perturbs | its model         | parameters | and     | per- |
| image | at       | the receiver. |          |     |        |        |               |     |               |        |                      |          |                   |            |         |      |
formstwoforwardpropagationswiththeoriginalandperturbed
parameters,transmittingbothoutputstoVendorB.Usingthese
TheresultsshowthatAMSachievesthehighestPSNRacross outputs and ground-truth labels from a shared fine-tuning
| theentire0–30dBSNRrange.Theone-model-fits-onebaseline |     |     |     |     |     |     |     |     |          |        | B         |     |               |     |          |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | --- | ------------- | --- | -------- | --- |
|                                                       |     |     |     |     |     |     |     |     | dataset, | Vendor | evaluates |     | the loss with | its | original | and |
achievesthe second-highestPSNR, but incurssignificanttrain- perturbed model parameters. The resulting loss difference, to-
ingandstorageoverhead,withsevereperformancedegradation getherwith the correspondingparameterperturbation,provides
outside the SNRs used for training. Although the one-model- a zeroth-order estimate of the gradient direction. Vendor B
fits-allbaselinehasthelowestoverhead,italsoyieldsthelowest uses this estimate to update its model and returns the scalar
A,
PSNR over most of the SNR range. Na¨ıve AMS has overhead loss difference to Vendor which similarly estimates the
comparabletoAMS,butitsPSNRis6–8dBloweroverthe0– gradient direction and updates its model. The procedure natu-
20dBrange,underscoringtheimportanceofMSCconstruction
|     |     |     |     |     |     |     |     |     | rally extendsto |     | multiple | randomperturbations,whose |     |     | gradient |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ------------------------- | --- | --- | -------- | --- |
and transmission parameter selection. estimatesareaveragedtoobtainamorereliablebatchgradient.

6
|     |     |     |     |     |     |     |     | −58.24 |     | −14.56 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- |
The corresponding perturbed outputs can be transmitted to- of dB and dB, respectively. In contrast, the
getherinasinglebatch,allowingmultipleperturbationswithout proposed gradient-free fine-tuning framework eliminates gra-
additional communication rounds. dient feedback, thereby preventing such information leakage.
Unlike Type 1 fine-tuning, which requires model parameter The bottom part of Fig. 5 further shows that gradient-free
|                  |     |                                       |     |     |     |     |     | fine-tuning | achieves | CSI | reconstruction |     | NMSE |     | comparable |
| ---------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ----------- | -------- | --- | -------------- | --- | ---- | --- | ---------- |
| exchange,andType |     | 2fine-tuning,whichrequiresbothforward |     |     |     |     |     |             |          |     |                |     |      |     |            |
and backward propagations between Vendors A and B, the to that of conventional Type 2 fine-tuning, while reducing
VendorA-sidememoryusageby3.65timesandVendorB-side
| proposed | method | relies | only | on forward |     | propagations, | with |     |     |     |     |     |        |     |     |
| -------- | ------ | ------ | ---- | ---------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | ------ | --- | --- |
|          |        |        |      |            |     | A.            |      |     |     |     |     |     | 15,000 |     |     |
scalar loss differences fed back to Vendor This limited communication overhead by more than times. These
feedback reduces the risk of exposing proprietary information gains are consistently achieved across different compression
|               |        | B-side |       |        |             |                 |     | ratios. |     |     |     |     |     |     |     |
| ------------- | ------ | ------ | ----- | ------ | ----------- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| about the     | Vendor |        |       | model, | as gradient | feedback        | may |         |     |     |     |     |     |     |     |
| enable Vendor |        | B-side | model | output | inference   | and adversarial |     |         |     |     |     |     |     |     |     |
attacks by Vendor A [9]. Furthermore, the proposed method VI. OPEN CHALLENGESAND FUTURE DIRECTIONS
B-side
substantially reduces Vendor communication overhead, The preceding sections have revisited the foundational as-
| as the scalar | feedback |     | is small | and | its size | is independent | of  |           |              |     |        |     |            |           |        |
| ------------- | -------- | --- | -------- | --- | -------- | -------------- | --- | --------- | ------------ | --- | ------ | --- | ---------- | --------- | ------ |
|               |          |     |          |     |          |                |     | sumptions | of two-sided |     | models | and | introduced | practical | alter- |
theVendorA-sidemodeloutputdimension.Finally,eliminating
|          |             |     |         |          |     |                     |     | natives                  | for legacy | coexistence, |       | channel  | adaptation, |     | and multi-   |
| -------- | ----------- | --- | ------- | -------- | --- | ------------------- | --- | ------------------------ | ---------- | ------------ | ----- | -------- | ----------- | --- | ------------ |
| gradient | calculation |     | removes | the need | to  | retain intermediate |     |                          |            |              |       |          |             |     |              |
|          |             |     |         |          |     |                     |     | vendor interoperability. |            |              | These | advances | motivate    |     | new research |
activationsgeneratedduringforwardpropagationuntilthesub-
|     |     |     |     |     |     |     |     | directions | while | highlighting |     | further | challenges |     | that must be |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------------ | --- | ------- | ---------- | --- | ------------ |
sequent backward propagation, thereby reducing the memory addressedforthepracticaldeploymentoftwo-sidedmodels,as
| burden       | on resource-limited |             |           | devices. |             |                      |           |           |           |              |          |              |        |              |              |
| ------------ | ------------------- | ----------- | --------- | -------- | ----------- | -------------------- | --------- | --------- | --------- | ------------ | -------- | ------------ | ------ | ------------ | ------------ |
|              |                     |             |           |          |             |                      |           | discussed | next.     |              |          |              |        |              |              |
| Fig.         | 5 illustrates       | the         | overall   | pipeline |             | of the gradient-free |           |           |           |              |          |              |        |              |              |
|              |                     |             |           |          |             |                      |           | AMC-AMS   |           | Unification: |          | Conventional | AMC    |              | uses channel |
| zeroth-order | fine-tuning         |             | framework |          | and         | presents             | numerical |           |           |              |          |              |        |              |              |
|              |                     |             |           |          |             |                      |           | quality   | indicator | (CQI)        | feedback | to           | select | a modulation | level        |
| results.     | In the              | simulation, | we        | consider | a two-sided |                      | model for |           |           |              |          |              |        |              |              |
andcoderatefromtheMCStable.AMScansimilarlyuseCQI
| CSI feedback |             | in an | urban | macro | cell scenario, |         | where the |          |           |            |     |      |          |     |             |
| ------------ | ----------- | ----- | ----- | ----- | -------------- | ------- | --------- | -------- | --------- | ---------- | --- | ---- | -------- | --- | ----------- |
|              |             |       |       |       |                |         |           | feedback | to select | a model-SC |     | pair | from the | MSC | table. This |
| CSI is       | represented | as    | a 32  | × 32  | angular-delay  | matrix. | The       |          |           |            |     |      |          |     |             |
suggestsaunifiedadaptationframeworkthatjointlycoordinates
3.5
| carrier | frequency | is  | set to | GHz, | and | a uniform | linear |     |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------ | ---- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
AMCandAMSforagivenCQIfeedback.Validatingsuchjoint
| array with | half-wavelength |     |     | antenna | spacing | is used. | The two- |         |           |     |       |              |     |        |             |
| ---------- | --------------- | --- | --- | ------- | ------- | -------- | -------- | ------- | --------- | --- | ----- | ------------ | --- | ------ | ----------- |
|            |                 |     |     |         |         |          |          | AMC-AMS | operation |     | while | guaranteeing |     | legacy | coexistence |
sided model is first pre-trained in this scenario and then fine- remains an important challenge.
| tuned for     | a different |                | cell geometry.      |              | The   | loss function  | is the     |                  |        |                  |     |                |     |              |              |
| ------------- | ----------- | -------------- | ------------------- | ------------ | ----- | -------------- | ---------- | ---------------- | ------ | ---------------- | --- | -------------- | --- | ------------ | ------------ |
|               |             |                |                     |              |       |                |            | Extension        |        | to Task-Oriented |     | Communication: |     |              | Extending    |
| normalized    | mean        | squared        | error               | (NMSE).      | Using | this           | setup, we  |                  |        |                  |     |                |     |              |              |
|               |             |                |                     |              |       |                |            | two-sided        | models | from             | CSI | feedback       | and | conventional | data         |
| evaluate      | the CSI     | reconstruction |                     | performance, |       | memory         | usage,     |                  |        |                  |     |                |     |              |              |
|               |             |                |                     |              |       |                |            | communication    |        | to task-oriented |     | communication  |     |              | is promising |
| communication |             | overhead,      | and                 | information  |       | leakage        | associated |                  |        |                  |     |                |     |              |              |
|               |             |                |                     |              |       |                |            | but non-trivial. |        | In task-oriented |     | communication, |     |              | model input  |
| with gradient |             | exchange       | in conventionalType |              |       | 2 fine-tuning. |            |                  |        |                  |     |                |     |              |              |
andoutputdataresideattheapplicationlayer,whilechannelin-
Asillustratedintheupper-rightpartofFig.5,theexchanged
formationremainsintheradioaccessnetwork(RAN),requiring
gradientcanbeexpressedastheproductoftheJacobianmatrix,
costlycross-layerexchange.Jointmodel-SCtrainingavoidsthis
| the reconstructionerror,anda |     |     |     | scalingconstantbyapplyingthe |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
duringtraining,butonlineoperationstillrequiresvisibilityinto
chainrule,wheretheJacobianisdefinedasthederivativeofthe
B-side VendorA-side application-layer task-performance degradation and its causes.
| Vendor  |        | modeloutput |          | with respect | to  | the        |        |            |                   |              |             |     |            |     |            |
| ------- | ------ | ----------- | -------- | ------------ | --- | ---------- | ------ | ---------- | ----------------- | ------------ | ----------- | --- | ---------- | --- | ---------- |
|         |        |             |          |              |     |            |        | This calls | for               | standardized | cross-layer |     | interfaces | or  | co-located |
| output. | Access | to this     | Jacobian | reveals      | how | the Vendor | A-side |            |                   |              |             |     |            |     |            |
|         |        |             |          |              |     |            |        | PHY and    | application-layer |              | processing  |     | in AI-RAN  |     | [15].      |
B-side
| output influences |     | the | Vendor |     | model | output, | potentially |              |     |      |     |              |            |     |         |
| ----------------- | --- | --- | ------ | --- | ----- | ------- | ----------- | ------------ | --- | ---- | --- | ------------ | ---------- | --- | ------- |
|                   |     |     |        |     |       |         |             | Multi-Vendor |     | LCM: | In  | multi-vendor | scenarios, |     | the MSC |
allowinganadversarytocraftperturbationsthatmanipulatethe
latter [9]. In Type 2 fine-tuning, an honest-but-curiousVendor table can be split into transmitter- and receiver-side tables,
A allowing each vendorto maintain its own model while sharing
| can estimate  |        | this | Jacobian       | from | the exchanged |          | gradients. |          |      |             |              |     |     |         |           |
| ------------- | ------ | ---- | -------------- | ---- | ------------- | -------- | ---------- | -------- | ---- | ----------- | ------------ | --- | --- | ------- | --------- |
|               |        |      |                |      |               |          |            | only the | SCs. | This raises | multi-vendor |     | LCM | issues, | including |
| Specifically, | Vendor |      | A deliberately |      | transmits     | the same | model      |          |      |             |              |     |     |         |           |
output for differentCSI samples and subtracts the correspond- who determines the number of table entries and how they are
|              |            |     |          |     |         |        |            | updatedovertime.Similar |     |     | questionsarise |     | forfine-tuning,such |     |     |
| ------------ | ---------- | --- | -------- | --- | ------- | ------ | ---------- | ----------------------- | --- | --- | -------------- | --- | ------------------- | --- | --- |
| ing returned | gradients, |     | yielding | the | product | of the | transposed |                         |     |     |                |     |                     |     |     |
Jacobian and the difference between the CSI samples. By aswhenitshouldbetriggeredandwhichvendorshouldinitiate
|             |         |         |           |              |            |     |         | it. Standardized |     | or vendor-agreedrules |     |     | are | therefore | required. |
| ----------- | ------- | ------- | --------- | ------------ | ---------- | --- | ------- | ---------------- | --- | --------------------- | --- | --- | --- | --------- | --------- |
| repeating   | this    | process | with      | sufficiently | diverse    | CSI | samples |                  |     |                       |     |     |     |           |           |
| and jointly | solving | the     | resulting | linear       | equations, |     | Vendor  | A                |     |                       |     |     |     |           |           |
can recover the full Jacobian matrix. The recovered Jacobian VII. CONCLUSION
canfurtherbeusedtoestimatetheVendorB-sidemodeloutput
Thisarticlehasexaminedkeydeploymentchallengesoftwo-
from the observed gradients. sidedAImodels,intermsoflegacycoexistence,channeladap-
1/4,
At a compression ratio of simulation results show that tation,andmulti-vendorinteroperability.Toaddressthesechal-
Vendor A can accurately estimate both the Jacobian matrix lenges, we presented three practical alternatives: NR protocol-
B-side
and the Vendor model output from the gradients ex- stack integration, MSC-table-based AMS, and gradient-free
changed during Type 2 fine-tuning, achieving NMSE values zeroth-order fine-tuning. We also discussed open challenges,

7
such as the unification of AMS and AMC, extensions to task-
oriented communication, and multi-vendor LCM. Addressing
these challenges through coordinated advances in research,
prototyping, and standardization will be critical to moving
two-sided models beyond isolated demonstrations towards in-
teroperable and deployable components of next-generation air
interfaces.
REFERENCES
[1] X. Lin, L. Kundu, S. Cammerer, Y. Huang, C. Dick, C. Santhosam,
R. Gadiyar, R. Wiesmayr, and C. Studer, “AI-native 6G: Empowering
intelligent RAN with accelerated compute,” IEEE Wireless Commun.,
vol.32,no.6,pp.11–14,Dec.2025.
[2] J. Cheng, W.Chen, and B. Ai, “Adaptive end-to-end transceiver design
for NextG pilot-free and CP-free wireless systems,” IEEE J. Sel. Areas
Commun.,vol.44,pp.3055–3069, Feb.2026.
[3] T.-Y.Tung,D.B.Kurka,M.Jankowski,andD.Gu¨ndu¨z,“DeepJSCC-Q:
Constellationconstraineddeepjointsource-channelcoding,”IEEEJ.Sel.
AreasInf.Theory,vol.3,no.4,pp.720–731,Dec.2022.
[4] 3GPP,“StudyonArtificialIntelligence (AI)/MachineLearning(ML)for
NRAirInterface,” 3GPP,TR38.843,Sep.2025,V19.0.0.
[5] J.Guo,C.-K.Wen,S.Jin,andX.Li,“AIforCSIfeedbackenhancement
in5G-advanced,” IEEEWireless Commun.,vol.31,no.3,pp.169–176,
Jun.2024.
[6] NGMN Alliance, “6G architecture and migration options - An operator
view,”NGMNAlliance, PublicReport, May2026,V1.0.
[7] W. Zhang, H. Zhang, H. Ma, H. Shao, N. Wang, and V. C. M. Leung,
“Predictive andadaptive deepcodingforwirelessimagetransmissionin
semanticcommunication,”IEEETrans.WirelessCommun.,vol.22,no.8,
pp.5486–5501, Aug.2023.
[8] J. Li, X. Chen, L. Yang, A. S. Rakin, D. Fan, and C. Chakrabarti,
“EMGAN: Early-mix-GAN on extracting server-side model in split
federated learning,” in Proc. AAAI Conf. Artif. Intell., vol. 38, no. 12,
Vancouver, Canada, Mar.2024,pp.13545–13553.
[9] N. Papernot, P. McDaniel, S. Jha, M. Fredrikson, Z. B. Celik, and
A. Swami, “The limitations of deep learning in adversarial settings,”
in Proc.IEEEEur.Symp. Secur. Privacy, Saarbruecken, Germany, Mar.
2016,pp.372–387.
[10] Software Radio Systems, “OCUDU: The Linux of RAN and the
next chapter for open networks,” Oct. 2025, [Online]. Available:
https://srs.io/building-ocudu-the-linux-of-ran/.
[11] 3GPP,“Studyonchannel modelforfrequencies from0.5to100GHz,”
3GPP,TR38.901,Jun.2026,V19.4.0.
[12] Y. Oh, J. Park, J. Choi, and Y.-S. Jeon, “Towards optimal semantic
communications: Reconsidering the role of semantic feature channels,”
2026,arXiv:2602.08260v2.
[13] Y. Oh, J. Park, J. Choi, J. Park, and Y.-S. Jeon, “Blind training for
channel-adaptive digital semantic communications,” IEEE Trans. Com-
mun.,vol.73,no.11,pp.11274–11290,Nov.2025.
[14] Z.Chen,H.H.Yang,Z.Li,J.Park,andT.Q.Quek,“Zeroth-orderover-
the-airfederatedlargemodeltuningoveredgenetworks,”IEEEWireless
Commun.Lett.,vol.14,no.9,pp.3002–3006, Sep.2025.
[15] AI-RANAlliance, “AI-RAN architecture overview andcomponent defi-
nitions,” AI-RANAlliance, TR,Feb.2026,V1.2.
---- END DOCUMENT ----
