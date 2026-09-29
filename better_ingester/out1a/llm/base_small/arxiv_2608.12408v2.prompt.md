Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Evaluation Resolution Confounds Learning-Rule Comparisons
in Model–Brain RSA of Early Visual Cortex
Nils Leutenegger
Independent Researcher, Switzerland
github.com/nilsleut
Abstract across a 12-fold increase in pooled positions with con-
tent held fixed, the gap opens by +0.003±0.001 against
+0.030±0.002 when content is free to vary, and back-
Representational similarity analysis (RSA) is increas-
prop’s decline is abolished (−0.023 → −0.000, 0/5 and
ingly used to ask which learning rules give convolutional
2/5 seeds). The dependence is carried by image detail
networksbrain-likerepresentations. Becausebiologically
above the training resolution rather than by the number
plausible rules such as feedback alignment, predictive
of pooled positions, though what that detail does to the
coding, and STDP do not scale, studies that include
representations remains unexplained. One control result
them train small networks on small images (typically
is worth stating separately: a single scalar luminance
32×32 CIFAR) and then compare the trained networks
value per image reaches ρ = 0.074 against V1, essen-
tobrainresponsesrecordedfornaturalisticstimuli,which
tially matching the untrained network’s 0.075. The first
are modeled at much higher resolution. We find that a
of those numbers concerns the brain data alone and is
commonqualitativeresultinthissetting,thatuntrained
independent of any model; the second is specific to RSA
orlocallytrainednetworksrivalorbeatbackpropagation
on globally pooled features, and a fitted readout on the
atearlyvisualcortex,dependsstronglyontheresolution
full feature map might place the models higher. What
at which the network is evaluated. The V1 gap between
the pair bounds, then, is what this style of comparison
anuntrainednetworkandabackpropagation-trainedone
can resolve at V1 in this dataset, not model–brain align-
widenswithevaluationresolution,from−0.001±0.007at
ment in general. In this setting, the one learning effect
the32pxtrainingresolutionto+0.044±0.006at224px,
thatholdsacrossresolutionisbackpropaboveuntrained,
growing monotonically across six resolutions (n = 5
atahigherarea(LOC).Comparisonsoflearningrulesor
seeds);thegapatthetrainingresolutionis≈0underthe
architecturesatearlyvisualcortexthereforeneedtocon-
fixed Conv1→V1 mapping and +0.014 under best-layer
trol, and report, the evaluation resolution.
selection, and the growth with resolution holds under
Keywords: representationalsimilarityanalysis,early
both. The effect is established for the random-versus-
visualcortex,learningrules,evaluationresolution,batch
backprop contrast, whose two conditions share an ini-
normalization, untrained networks, methodological con-
tialization, and reproduces in the same direction across
found
three further conditions whose initialization or weight
displacement is not matched (feedback alignment, pre- Note on version 2. This version corrects the text of
dictive coding, STDP; see Appendix B). It holds in hu- v1. No figure and no data file changes, and no compari-
manfMRIand,directionally,insingle-seedmacaqueelec- son between conditions changes in substance. One table
trophysiology, along the full training trajectory, and for value changes, by 0.001 (Appendix C, the best-layer gap
two architectures trained at 224px on other data (an at 96px). One interpretive claim is withdrawn.
ImageNet ResNet-50 and a Swin-Tiny transformer). We Six statements were wrong. The Methods described
testfourcandidatemechanismsandnoneaccountsforit: the fMRI RDMs as trial-averaged; the 720 evaluation
train/eval resolution matching, since the ResNet-50 and stimuli are single-presentation in all three subjects, so
the transformer also align best at low resolution despite the RDMs are single-trial and the averaging step is a
being trained at 224px; low-level Gabor and pixel struc- no-op (a new limitation, item 12, states what this does
ture; the normalization state of the untrained baseline, and does not affect). The precision claim in §4.1, that
testedwitha2×2calibrationdesignthatholdsthecon- repair left three conditions unchanged to within 0.0013,
volutional weights bit-identical; and convergence of the was tighter than the measurement allows and is restated
pooled descriptor toward a global brightness statistic. A against run-to-run reproducibility. The nondetermin-
fifth experiment does locate the effect. Repeating the ismcriterioninContent control namedthewrongkernel
sweep on stimuli first reduced to 32px and then upsam- and understated its magnitude: it is convolution weight-
pledcapstheimagedetailatthetrainingresolutionwhile gradientbackward,itreaches2×10−3atV1and5×10−3
the network still pools over the full number of positions; across all layer–ROI cells, and STDP does backpropa-
1
6202
guA
42
]CN.oib-q[
2v80421.8062:viXra

gate through the convolutions. The layer→ROI map- ∆ρ=+0.042, p<0.001; Leutenegger, 2026].
| ping omitted |     | Conv2, | giving | six | layer–ROI | pairs | rather |      |       |            |     |                |     |             |
| ------------ | --- | ------ | ------ | --- | --------- | ----- | ------ | ---- | ----- | ---------- | --- | -------------- | --- | ----------- |
|              |     |        |        |     |           |       |        | This | paper | shows that | the | effect depends |     | strongly on |
thanfour. Andtherangeofpairedstandarderrorsgiven one factor that usually goes uncontrolled: the resolution
| in §3.2     | combined | two      | different |             | paired | contrasts, | taking     |          |        |               |            |                |          |             |
| ----------- | -------- | -------- | --------- | ----------- | ------ | ---------- | ---------- | -------- | ------ | ------------- | ---------- | -------------- | -------- | ----------- |
|             |          |          |           |             |        |            |            | at which | the    | model is      | evaluated. | Run            | the same | trained     |
| its minimum |          | from one | and       | its maximum |        | from       | the other; |          |        |               |            |                |          |             |
|             |          |          |           |             |        |            |            | models   | on the | brain stimuli |            | across a range | of       | input reso- |
itisrestatedfromasinglecontrast,anditsupperbound lutionsandtheuntrainednetwork’sV1advantagetracks
| moves        | from 0.009 |              | to 0.007.    | And | the      | endpoint  | result |                  |           |           |            |                  |         |        |
| ------------ | ---------- | ------------ | ------------ | --- | -------- | --------- | ------ | ---------------- | --------- | --------- | ---------- | ---------------- | ------- | ------ |
|              |            |              |              |     |          |           |        | that resolution. |           | It is     | large when | the 32px-trained |         | mod-   |
| quoted       | in the     | introduction |              | was | a mixed  | citation: | the    |                  |           |           |            |                  |         |        |
|              |            |              |              |     |          |           |        | els are          | evaluated | at 224px, |            | the standard     | choice, | and it |
| two ρ values |            | were         | the endpoint |     | study’s, | but       | the ∆ρ | of               |           |           |            |                  |         |        |
vanishesatthe32pxtrainingresolution(−0.001±0.007;
| +0.044wasours. |     | Allthreearenowtheendpointstudy’s |     |     |     |     |     |                  |     |                                |     |     |     |     |
| -------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------------ | --- | --- | --- | --- |
|                |     |                                  |     |     |     |     |     | Fig.1,n=5seeds). |     | Therankingonereportsatearlyvi- |     |     |     |     |
§4.2
own (ρ=0.075 and ρ=0.033, ∆ρ=+0.042); gives sualcortexthusrestsonananalysischoicethatisrarely
| our own | +0.044 | at  | the same | cell | and why | the | two differ. |     |     |     |     |     |     |     |
| ------- | ------ | --- | -------- | ---- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
stated.
| The remainingcorrections |     |      |         | areto         | printed | values.   | Most    |              |            |             |                    |                      |             |           |
| ------------------------ | --- | ---- | ------- | ------------- | ------- | --------- | ------- | ------------ | ---------- | ----------- | ------------------ | -------------------- | ----------- | --------- |
|                          |     |      |         |               |         |           |         | This         | dependence | is          | not specific       | to                   | our network | or to     |
| are re-roundings         |     | from | source, |               | each in | the last  | printed |              |            |             |                    |                      |             |           |
|                          |     |      |         |               |         |           |         | one dataset. |            | It holds    | across             | all five conditions, |             | in both   |
| digit. Two               | are | not: | the     | reference-RDM |         | stability | bound   |              |            |             |                    |                      |             |           |
|                          |     |      |         |               |         |           |         | human        | fMRI       | and macaque | electrophysiology, |                      |             | and along |
wasroundedwherealowerboundmustbefloored,which
|     |     |     |     |     |     |     |     | the whole | training | trajectory, |     | where the | familiar | “train- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----------- | --- | --------- | -------- | ------- |
overstatedit(0.958to0.957);andthepaired-SEMrange
|             |        |           |          |      |          |          |             | ing degrades            | V1” | result | tracks | the same                 | dependence, | ac- |
| ----------- | ------ | --------- | -------- | ---- | -------- | -------- | ----------- | ----------------------- | --- | ------ | ------ | ------------------------ | ----------- | --- |
| above moves |        | by 0.002, | which    | with | the      | ∆ρ above | is the      |                         |     |        |        |                          |             |     |
|             |        |           |          |      |          |          |             | cumulatingepochbyepoch. |     |        |        | Italsoholdsfortwofurther |             |     |
| largest     | change | in this   | version. |      | The gaps | and      | differences |                         |     |        |        |                          |             |     |
architecturestrainedat224pxondifferentdata,anIma-
| the paper’s | claims |     | rest on | were | always | computed | at full |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ------- | ---- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
geNetResNet-50[Heetal.,2016]andaSwin-Tinytrans-
| precision      | and                 | are unchanged.  |            |               |         |              |             |                  |         |                 |              |               |         |              |
| -------------- | ------------------- | --------------- | ---------- | ------------- | ------- | ------------ | ----------- | ---------------- | ------- | --------------- | ------------ | ------------- | ------- | ------------ |
|                |                     |                 |            |               |         |              |             | former           | [Liu et | al., 2021].     | One          | candidate     | is      | the obvious  |
| We also        | withdraw            |                 | the        | noise-ceiling |         | estimate     | and the     |                  |         |                 |              |               |         |              |
|                |                     |                 |            |               |         |              |             | explanation,     |         | a mismatch      | between      | training      |         | and evalua-  |
| “69% of        | the attainable      |                 | ceiling”   |               | figure. | With         | three sub-  |                  |         |                 |              |               |         |              |
|                |                     |                 |            |               |         |              |             | tion resolution. |         | If that         | were         | the cause,    | a model | trained      |
| jects and      | single-presentation |                 |            | stimuli,      |         | neither      | a within-   |                  |         |                 |              |               |         |              |
|                |                     |                 |            |               |         |              |             | at 224px         | should  | align           | best         | at 224px;     | instead | both the     |
| subject        | nor a               | between-subject |            |               | ceiling | is estimable | on          |                  |         |                 |              |               |         |              |
|                |                     |                 |            |               |         |              |             | ResNet-50        | and     | the transformer |              | align         | best    | at low reso- |
| these data.    |                     | The luminance   |            | bound,        |         | which        | requires no |                  |         |                 |              |               |         |              |
|                |                     |                 |            |               |         |              |             | lution,          | exactly | as the          | 32px-trained | networks      |         | do, across   |
| ceiling,       | is stated           | in              | its place; | it            | is the  | bound        | the paper’s |                  |         |                 |              |               |         |              |
|                |                     |                 |            |               |         |              |             | a convolutional  |         | and a           | transformer  | family        | alike.  | A sec-       |
| scale argument |                     | now             | rests      | on.           |         |              |             |                  |         |                 |              |               |         |              |
|                |                     |                 |            |               |         |              |             | ond concerns     |         | the baseline    | itself:      | the untrained |         | network’s    |
batch-normalizationlayersareatinitializationandthere-
1 Introduction foreactastheidentity,whileeverytrainedconditioncar-
|     |     |     |     |     |     |     |     | ries statistics |     | accumulated | during | training. |     | Calibrating |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ------ | --------- | --- | ----------- |
thosestatisticsattheevaluationresolution,withthecon-
| A recurring | question |     | in NeuroAI |     | is which | learning | rule |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ---------- | --- | -------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
gives a network the most brain-like visual representa- volutionalweightsheldbit-identical,leavestheuntrained
|            |       |          |     |          |     |           |        | network’s | V1  | advantage | essentially | intact. |     | The remain- |
| ---------- | ----- | -------- | --- | -------- | --- | --------- | ------ | --------- | --- | --------- | ----------- | ------- | --- | ----------- |
| tions. The | usual | approach |     | compares |     | candidate | models |           |     |           |             |         |     |             |
to neural data with representational similarity analysis ing two are low-level accounts. Gabor and pixel struc-
|       |               |     |         |        |        |         |       | turedonotpredictV1alignmentacrossmodels, |     |     |     |     |     | andthe |
| ----- | ------------- | --- | ------- | ------ | ------ | ------- | ----- | ---------------------------------------- | --- | --- | --- | --- | --- | ------ |
| (RSA) | [Kriegeskorte |     | et al., | 2008], | asking | whether | back- |                                          |     |     |     |     |     |        |
ResNet-50isfarmoreGabor-likethananuntrainedCNN
| propagation | or  | a more | biologically |     | plausible |     | rule (feed- |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ------------ | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
back alignment [Lillicrap et al., 2016], predictive cod- while aligning less well with V1. Global image statistics
|                  |                        |          |         |             |            |         |          | come closer, |         | and this  | is where  | the sweep |        | turns up its |
| ---------------- | ---------------------- | -------- | ------- | ----------- | ---------- | ------- | -------- | ------------ | ------- | --------- | --------- | --------- | ------ | ------------ |
| ing [Rao         | and                    | Ballard, | 1999,   | Whittington |            | and     | Bogacz,  |              |         |           |           |           |        |              |
|                  |                        |          |         |             |            |         |          | second       | result: | a single  | scalar    | luminance | value  | per im-      |
| 2017], or        | spike-timing-dependent |          |         |             | plasticity | [Bi     | and Poo, |              |         |           |           |           |        |              |
|                  |                        |          |         |             |            |         |          | age reaches  | ρ       | = 0.074   | against   | the V1    | RDM,   | essentially  |
| 1998, Masquelier |                        | and      | Thorpe, | 2007])      | better     | matches | the      |              |         |           |           |           |        |              |
|                  |                        |          |         |             |            |         |          | matching     | the     | untrained | network’s | own       | 0.075, | and par-     |
| representational |                        | geometry |         | of visual   | cortex     | [Yamins | and      |              |         |           |           |           |        |              |
DiCarlo, 2016, Schrimpf et al., 2020]. The biologically tialling luminance out halves that network’s alignment.
|            |          |        |      |        |          |           |          | Luminance | similarity |        | also orders | the    | conditions | exactly      |
| ---------- | -------- | ------ | ---- | ------ | -------- | --------- | -------- | --------- | ---------- | ------ | ----------- | ------ | ---------- | ------------ |
| plausible  | rules    | do not | yet  | scale  | to large | datasets, | so any   |           |            |        |             |        |            |              |
|            |          |        |      |        |          |           |          | as their  | resolution | slopes | do.         | But it | is not     | the carrier: |
| study that | includes |        | them | trains | small    | networks  | on small |           |            |        |             |        |            |              |
images, typically32×32CIFAR,andthencomparesthe holdingtheconvolutionalweightsbit-identicalandvary-
|         |                 |     |         |     |       |           |          | ing only | the | normalization | statistics |     | separates | the two, |
| ------- | --------------- | --- | ------- | --- | ----- | --------- | -------- | -------- | --- | ------------- | ---------- | --- | --------- | -------- |
| trained | representations |     | against |     | brain | responses | to natu- |          |     |               |            |     |           |          |
ralistic stimuli modeled at much higher resolution. with one variant lowering its luminance similarity across
|     |             |     |          |          |     |             |     | the sweep | while | raising | its V1 | alignment. | We  | report the |
| --- | ----------- | --- | -------- | -------- | --- | ----------- | --- | --------- | ----- | ------- | ------ | ---------- | --- | ---------- |
| One | observation |     | has been | reported |     | repeatedly: | un- |           |       |         |        |            |     |            |
phenomenonanditsboundariesandleavethemechanism
| trained, | randomly | initialized |     | networks |     | are already | quite |     |     |     |     |     |     |     |
| -------- | -------- | ----------- | --- | -------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
open.
| brain-like, | sometimes |     | matching |     | or beating | trained | net- |     |     |     |     |     |     |     |
| ----------- | --------- | --- | -------- | --- | ---------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
works at early visual areas [Saxe et al., 2011, Truzzi Noteverythingmoveswithresolution. Atahigherarea
and Cusack, 2025]. Our own earlier work reproduced it. (LOC), backpropagation-trained networks align better
Acrossthefiveconditions,anuntrainednetworkmatched than untrained ones at every resolution we tested (LOC
orexceededabackpropagation-trainedoneathumanV1 backprop−untrained ≈ +0.019, 5/5 seeds at both 32px
[at 224px, untrained ρ = 0.075 vs. backprop ρ = 0.033; and 224px). Learning does reshape representations;
2

what it does at early visual cortex is simply swamped lus, and the calibration resolution is either 32px or the
by the evaluation resolution. resolutionat which themodelis subsequentlyevaluated,
Contributions. (1) We identify and quantify an givinga2×2design. Asacheckonthecalibrationproce-
evaluation-resolutiondependenceinmodel–brainRSAat dureitselfweadditionallycalibrateonthe720evaluation
early visual cortex, and show it is general across con- stimuli. After every calibration we verify that all convo-
ditions, two species, the training trajectory, and three lutional weights are bit-identical to the plain untrained
architecture families. (2) We test four candidate mecha- condition.
nismsandruleoutallfour,threeofthembyinterventions Additional architectures (eval-only). To
thatholdtheconvolutionalweightsbit-identical. (3)We test architecture-independence we add two standard
separate the two things evaluation resolution changes at ImageNet-pretrained models, evaluated without further
once and locate the dependence on the image-content training: a ResNet-50 [torchvision IMAGENET1K V2; He
axis rather than the pooling axis. (4) We show that et al., 2016] and a Swin-Tiny transformer [torchvision
a single scalar luminance value per image matches the IMAGENET1K V1; Liu et al., 2021].
untrained network’s V1 alignment in this dataset, and
Brain data. Human: THINGS-fMRI representa-
that luminance similarity orders the conditions exactly
tional dissimilarity matrices (RDMs) for V1, V2, LOC
as their resolution slopes do without carrying the ef-
and IT over 720 object images [Hebart et al., 2023],
fect, which bounds what these comparisons can resolve.
averaged across 3 subjects. Macaque: electrophysiol-
(5) We isolate a learning effect that does survive across
ogy via Brain-Score, namely FreemanZiemba2013 [V1,
resolution,atLOC,andwerecommendevaluatingalign-
V2; 135 texture stimuli; Freeman et al., 2013] and Ma-
ment at the training resolution and at several others.
jajHong2015 [V4, IT; 3,200 object presentations; Majaj
et al., 2015].
2 Methods Stimulus preprocessing. Stimuli are re-
sized with bilinear interpolation on the PIL
Learning rules and architecture. We compare five image (transforms.Resize(px) followed by
conditions: random (untrained) weights, backpropaga- CenterCrop(px)), which scales the shorter edge
tion (BP), feedback alignment (FA), predictive coding and preserves aspect ratio, so the retained image region
(PC), and STDP. All use the same small convolutional isidenticalateveryevaluationresolution;downsampling
architecture (three convolutional blocks Conv1–Conv3, is antialiased. Inputs are normalized with each model’s
each 3×3 kernels with batch normalization, ReLU and own training statistics: CIFAR-10 channel statistics for
2×2 max-pooling; 32/64/128 filters, followed by FC1 of the custom CNN, ImageNet statistics for the ResNet-50
512 units and a 10-way head FC2). Each condition is and the Swin-Tiny. All models are placed in evaluation
trainedonan8,000-imagesubsetofCIFAR-10at32×32 mode for feature extraction, so batch normalization uses
resolution, batch size 128, for 40 epochs, with 5 random its stored running statistics and these are not updated
seeds (42,123,456,789,1337). Optimizers and rates dif- by the evaluation pass; this is asserted at extraction
fer by rule: BP uses Adam (lr 10−3, weight decay 10−4, time for every condition. Note that the untrained net-
cosine schedule, gradient clipping at 1.0, dropout 0.3, work’s batch-normalization layers retain their initialized
cross-entropy);FAusesSGD(lr5×10−4,momentum0.9) running statistics (mean 0, variance 1), so normalization
withfixedrandomfeedbackweights;PCrefinesrepresen- is close to the identity for that condition, whereas the
tations for T = 10 inference steps (inference rate 0.02) trained networks carry statistics accumulated at the
andupdatesfeedforwardweightsbylocalpredictionerror 32px training resolution.
(lr10−4)withanAdam-trainedreadout;STDPconverts RSA. For each model we extract layer activations
activations to Poisson spike trains (10 timesteps) and for every stimulus, global-average-pool convolutional or
updates convolutional weights by a spike-timing kernel stage feature maps, and build a model RDM with cor-
(A = 0.003, τ = 20ms, lr 5×10−4) with an Adam- relation distance. For the predictive-coding condition,
± ±
trained readout. Full details follow Leutenegger [2026]. features are the representations produced by the infer-
Normalization controls. The untrained condition’s ence loop (T = 10 steps at inference rate 0.02), not a
batch-normalization layers are at initialization. To test single feedforward pass; using the feedforward pass in-
whether that difference drives the results, we add cali- stead gives a different model. Model and brain RDMs
brated variants of it: starting from the untrained net- are compared by Spearman correlation. The main fig-
work,weestimatebatch-normalizationstatisticsfrom50 ures report the mean ± SEM across the 5 seeds. Two
forwardpassesintrainingmodewithnoweightupdates, averaging schemes appear in this paper. Figures 1, 3
using an unbiased cumulative average rather than the and7correlateeachmodelRDMagainsttheRDMaver-
default exponential moving average, and a deterministic aged over the three subjects; Figure 6 correlates against
loader with no augmentation. The calibration set is ei- each subject separately and averages the resulting cor-
ther CIFAR-10 or THINGS images drawn from a pool relations. Averaging RDMs before correlating reduces
of 1,134 concepts that contribute no evaluation stimu- noiseinthebrainestimateandyieldsuniformlyhigherρ,
3

so the two schemes give different absolute values for the the evaluation resolution, with identical interpolation,
samemodels. Themaineffectisunchangedundereither: antialiasing, cropping and normalization in both arms.
theV1Random−Backpropgaprunsfrom−0.001±0.007 Botharmsareevaluatedonthesamemodelobjectinthe
(3/5seeds)at32pxto+0.044±0.006(5/5)at224pxun- sameprocess,sothecontrastbetweenthemisexact. The
der RDM averaging, and from +0.000±0.005 (3/5) to nondeterministic kernel is convolution weight-gradient
+0.032±0.004(5/5)underper-subjectaveraging. Differ- backward. Conditions whose stored parameters are up-
ences across seeds, such as the Random−Backprop gap, datedfromconvolutionweightgradients(backprop,feed-
are tested with a paired, one-sided sign-flip permutation back alignment) reproduce across separate runs only to
test over the five seeds (25 = 32 assignments; smallest about 2 × 10−3 at V1, with a maximum of 5 × 10−3
attainable p = 1/32 ≈ 0.031), following the compan- acrossalllayer–ROIcells;conditionswhoseconvolutional
ion training-dynamics study. All differences, factor ef- weights are not so updated reproduce bit-identically.
fects and standard errors are computed at full precision; This includes STDP, which does backpropagate through
theymaythereforedifferinthelastdigitfromarithmetic theconvolutionstotrainitsbatch-normalizationparam-
on the rounded values printed. Layer→ROI mapping eters but discards the convolutional weight gradient and
for the custom CNN: Conv1→V1/V2, Conv2→V1/V2, sets those weights by a local rule. We confirmed the
Conv3→LOC, FC1→IT — six layer–ROI pairs. The source with a paired probe: two runs under determinis-
headlineV1resultusesConv1throughout; Conv2enters ticalgorithmsarebit-identical, twodefaultrunsarenot.
| the best-layer        |              | analysis   | of  | Appendix                | C.         | For ResNet-50: |             |             |                |           |                  |              |                      |                  |         |
| --------------------- | ------------ | ---------- | --- | ----------------------- | ---------- | -------------- | ----------- | ----------- | -------------- | --------- | ---------------- | ------------ | -------------------- | ---------------- | ------- |
|                       |              |            |     |                         |            |                |             | Low-level   |                | controls. | To               | test         | low-level-statistics |                  | ac-     |
| layer1→V1/V2,         |              | layer2→V4, |     |                         | layer4→IT. |                | For Swin-   |             |                |           |                  |              |                      |                  |         |
|                       |              |            |     |                         |            |                |             | counts      | we build,      | at        | each resolution, |              | a                    | Gabor filterbank |         |
| Tiny: early           | stage→V1/V2, |            |     | late                    | stage→IT.  |                |             |             |                |           |                  |              |                      |                  |         |
|                       |              |            |     |                         |            |                |             | RDM (a      | parameter-free |           | V1-like          |              | model:               | energy           | of ori- |
| Interpretingthescale. |              |            |     | AbsoluteSpearmanρvalues |            |                |             |             |                |           |                  |              |                      |                  |         |
|                       |              |            |     |                         |            |                |             | ented Gabor |                | filters   | at four          | orientations |                      | × three          | spatial |
| in this setting       |              | are low,   | and | we report               | no         | noise          | ceiling for |             |                |           |                  |              |                      |                  |         |
frequencies)andaraw-luminance(pixel)RDM,andcor-
them. The720evaluationstimuliaresingle-presentation, relateeachwiththemodelRDMsandwiththeV1brain
sonowithin-subjectreliabilitycanbeestimatedonthem,
|     |     |     |     |     |     |     |     | RDM. | To test | whether | pooling |     | converges | the | descrip- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ------- | ------- | --- | --------- | --- | -------- |
andwiththreesubjectsabetween-subjectestimateisnot tor toward a global image statistic we add three further
usable either: at N =3 each subject contributes a third parameter-free references over the same stimuli: mean
| of its own | target, | and | the | upper | bound | we obtain | sits |            |     |            |     |         |     |           |      |
| ---------- | ------- | --- | --- | ----- | ----- | --------- | ---- | ---------- | --- | ---------- | --- | ------- | --- | --------- | ---- |
|            |         |     |     |       |       |           |      | RGB (three |     | dimensions | per | image), | a   | joint RGB | his- |
barelyabovethevalueittakeswhenallsharedstructure togram(8×8×8bins),andmeanluminance(onedimen-
| is removed | by  | permutation. |     | A   | ceiling | figure | reported |          |         |      |      |             |     |          |        |
| ---------- | --- | ------------ | --- | --- | ------- | ------ | -------- | -------- | ------- | ---- | ---- | ----------- | --- | -------- | ------ |
|            |     |              |     |     |         |        |          | sion per | image), | each | with | correlation |     | distance | except |
in our earlier work [Leutenegger, 2026] rests on such an mean luminance, which uses absolute difference. These
estimate. We withdraw our use of it here: the reported are resolution-invariant by construction; we verify this
boundsarenotreproduciblefromthecodethatproduced
|     |     |     |     |     |     |     |     | (RDMs | built | at 32 versus |     | 224px | correlate | at ρ≥0.957), |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------------ | --- | ----- | --------- | ------------ | --- |
them, andthequantitytheyestimateisbetween-subject so any resolution trend in their similarity to a model
| consistency | rather | than | measurement |     | reliability. |     |     |            |     |       |       |         |     |                  |     |
| ----------- | ------ | ---- | ----------- | --- | ------------ | --- | --- | ---------- | --- | ----- | ----- | ------- | --- | ---------------- | --- |
|             |        |      |             |     |              |     |     | comes from | the | model | side. | Partial |     | RSA residualizes |     |
The bound that does hold requires no ceiling: a sin- both model and brain RDM vectors against a reference
|            |               |          |             |                   |            |          |             | by rank-based |     | linear  | regression. |     |                |     |          |
| ---------- | ------------- | -------- | ----------- | ----------------- | ---------- | -------- | ----------- | ------------- | --- | ------- | ----------- | --- | -------------- | --- | -------- |
| gle scalar | luminance     |          | value       | per image         | reaches    |          | ρ = 0.074   |               |     |         |             |     |                |     |          |
| against    | the V1        | RDM,     | essentially |                   | matching   |          | the best    |               |     |         |             |     |                |     |          |
| model      | we tested     | at       | 0.075.      | That              | number     | involves | no          |               |     |         |             |     |                |     |          |
| model and  | no            | readout, | so          | it bounds         | the        | brain    | side di-    |               |     |         |             |     |                |     |          |
| rectly.    | Occupying     |          | most of     | the               | resolvable | signal   | at V1       |               |     |         |             |     |                |     |          |
|            |               |          |             |                   |            |          |             | 3 Results     |     |         |             |     |                |     |          |
| under this | comparison    |          | is a        | low bar,          | and        | none of  | our con-    |               |     |         |             |     |                |     |          |
| ditions    | clears        | it by    | much.       | What              | makes      | the      | differences |               |     |         |             |     |                |     |          |
| we report  | interpretable |          | is          | their consistency |            | across   | seeds       |               |     |         |             |     |                |     |          |
|            |               |          |             |                   |            |          |             | The structure |     | of what | follows     | is  | an elimination |     | followed |
andtheirmonotonebehaviouracrossthesweep,nottheir
|     |     |     |     |     |     |     |     | by a localization. |     | Section |     | 3.1 establishes |     | that | the V1 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | --- | --------------- | --- | ---- | ------ |
absolute size.
|             |     |        |          |      |        |                 |     | rankingmoveswithevaluationresolution. |     |               |         |            |            | Thethreesec- |         |
| ----------- | --- | ------ | -------- | ---- | ------ | --------------- | --- | ------------------------------------- | --- | ------------- | ------- | ---------- | ---------- | ------------ | ------- |
| Resolution  |     | sweep. |          | This | is the | central         | ma- |                                       |     |               |         |            |            |              |         |
|             |     |        |          |      |        |                 |     | tions after                           | it  | try to        | explain | that       | dependence | away         | and     |
| nipulation. |     | We     | evaluate |      | each   | already-trained |     |                                       |     |               |         |            |            |              |         |
|             |     |        |          |      |        |                 |     | none succeeds:                        |     | the untrained |         | baseline’s |            | missing      | normal- |
model on the brain stimuli at six input resolutions ization(§3.2),apenaltyforevaluatingamodelawayfrom
| (32,64,96,128,160,224px), |     |     |     | with | the network, |     | weights, |              |            |     | (§3.3), |     |           |       |         |
| ------------------------- | --- | --- | --- | ---- | ------------ | --- | -------- | ------------ | ---------- | --- | ------- | --- | --------- | ----- | ------- |
|                           |     |     |     |      |              |     |          | its training | resolution |     |         | and | low-level | image | statis- |
and normalization held fixed. Training is always at tics, including the convergence of the pooled descriptor
32px; only the evaluation resolution varies, so the sweep (§3.4).
|     |     |     |     |     |     |     |     | toward | a global | brightness |     | measure |     | Section | 3.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | --- | ------- | --- | ------- | --- |
adds no retraining.
|     |     |     |     |     |     |     |     | then separates |     | the two | things | resolution |     | changes | at once |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ------ | ---------- | --- | ------- | ------- |
Content control. To separate the number of pooled andfindsthedependenceonthecontentaxisratherthan
positions from the image detail available at each, we re- the pooling axis. Sections 3.6 and 3.7 show that it also
peat the entire sweep in a second arm in which every governs the training trajectory and the macaque data,
stimulus is first resized to 32px and then upsampled to and identify the one comparison it does not touch.
4

| 3.1    | The        | V1     | rule       | ranking      | is   | a function | of        |          |     |     |     |     |     |     |
| ------ | ---------- | ------ | ---------- | ------------ | ---- | ---------- | --------- | -------- | --- | --- | --- | --- | --- | --- |
|        | evaluation |        | resolution |              |      |            |           | 0.08     |     |     |     |     |     |     |
| Across | the        | sweep, | the        | early-visual | rule | ranking    | is not    | )1V 0.07 |     |     |     |     |     |     |
| fixed; | it shifts  | with   | evaluation | resolution   |      | (Fig.      | 1). Every | 0.06     |     |     |     |     |     |     |
1vnoC(
trainedconditionalignsbestatornearthe32pxtraining
| resolutionandfallsoffasresolutionrises: |         |         |     |           |     | backpropfrom |          | 0.05 |     |     |     |     |     |     |
| --------------------------------------- | ------- | ------- | --- | --------- | --- | ------------ | -------- | ---- | --- | --- | --- | --- | --- | --- |
| ρ                                       | = 0.065 | at 32px | to  | ρ = 0.031 | at  | 224px,       | feedback |      |     |     |     |     |     |     |
0.04
| alignment     |     | from 0.020                    | to  | 0.012, | predictive |     | coding from |  namraepS |     |     |     |     |     |     |
| ------------- | --- | ----------------------------- | --- | ------ | ---------- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
| 0.026to0.016, |     | STDPfrom0.059to0.037(5seeds). |     |        |            |     | The         | 0.03      |     |     |     |     |     |     |
untrainednetworkgoestheotherway,climbingfromρ=
| 0.064 | to  | ρ=0.075. |     |     |     |     |     | 0.02 |     |     |     |     |     |     |
| ----- | --- | -------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
ThegapbetweenuntrainedandbackpropatV1,which
0.01
is what “untrained ≥ trained” claims rest on, follows di- training resolution
rectly from this. It runs from −0.001 ± 0.007 at the 32 64 96 128 160 224
32px training resolution (3/5 seeds positive, not signif- Evaluation resolution (px)
| icant) | to  | +0.044±0.006 |     | at 224px | (5/5 | seeds | positive), |     |     |                    |     |     |                   |     |
| ------ | --- | ------------ | --- | -------- | ---- | ----- | ---------- | --- | --- | ------------------ | --- | --- | ----------------- | --- |
|        |     |              |     |          |      |       |            |     |     | Untrained (random) |     |     | Predictive coding |     |
growingmonotonicallyacrossthesweep. Withfiveseeds Backprop STDP
the sign-flip test has a floor of p = 1/32 ≈ 0.031; the Feedback alignment
dose–responserelationshipacrosssixresolutions,notthe
p-value at any one of them, is what the claim rests on. Figure 1: V1 alignment is a function of evaluation
| At  | the resolution |     | the models | were | trained | on  | there is no |             |      |          |     |              |     |       |
| --- | -------------- | --- | ---------- | ---- | ------- | --- | ----------- | ----------- | ---- | -------- | --- | ------------ | --- | ----- |
|     |                |     |            |      |         |     |             | resolution. | Mean | Spearman |     | ρ (Conv1→V1) |     | ± SEM |
effect; at the resolution normally used to evaluate them across 5 seeds. Every trained condition peaks at the
it is large.
32pxtrainingresolutionanddeclines;onlytheuntrained
The fixed layer-to-ROI mapping does not create random network rises. The Random−Backprop gap is
this. Selecting, for each condition and each resolu- ≈ 0 at 32px and grows to +0.044 at 224px; the same
| tion, | whichever | layer | aligns | best | with | V1 leaves | the best |     |     |     |     |     |     |     |
| ----- | --------- | ----- | ------ | ---- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
patternholds,shifteddownward,afterlow-levelstatistics
layer unchanged across the sweep for every condition are partialled out (§3.4).
| but | predictive | coding,  |        | and the | gap  | grows  | in the same |     |     |     |     |     |     |     |
| --- | ---------- | -------- | ------ | ------- | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| way | and        | further: | +0.014 | ± 0.006 | (4/5 | seeds) | at 32px     |     |     |     |     |     |     |     |
to +0.060 ± 0.004 (5/5) at 224px (Appendix C). One withTHINGSstatisticsfromadisjointimagepool(2/5).
thing does change: under best-layer selection the gap Calibrating at 32px and evaluating higher costs more
at the training resolution is no longer ≈ 0 but +0.014. (−0.026 ± 0.006 and −0.020 ± 0.006 at 224px). The
That the gap vanishes at 32px is a property of the fixed 2 × 2 design separates the two factors: matching the
| Conv1 | mapping; |     | that | it grows | with | resolution | is not. |             |            |     |          |        |         |         |
| ----- | -------- | --- | ---- | -------- | ---- | ---------- | ------- | ----------- | ---------- | --- | -------- | ------ | ------- | ------- |
|       |          |     |      |          |      |            |         | calibration | resolution |     | is worth | +0.023 | ± 0.006 | for CI- |
The selection is also informative in its own right: the FAR and +0.008±0.002 for THINGS (5/5 seeds each),
untrained network’s best V1 layer is Conv2 while back- whereas changing the calibration set at matched resolu-
prop’s is Conv1, so a fixed Conv1→V1 mapping is not tionisworth−0.008±0.006(2/5). Whatthecalibration
neutral between the two conditions being compared. costsisitselfmostlyaresolutioneffect,notadistribution
effect.
3.2 It is not the untrained baseline’s nor- The untrained advantage survives all of it. Against a
resolution-matchedcalibratedbaselinetheuntrainednet-
malization
|     |     |     |     |     |     |     |     | work still | exceeds | backprop |     | at V1 | at 224px | by +0.041 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | --- | ----- | -------- | --------- |
A candidate that concerns the baseline rather than the (CIFAR calibration) or +0.033 (THINGS calibration),
models. The untrained condition is a network whose 5/5 seeds in both cases, against +0.044 for the uncali-
batch-normalization layers have never seen data: run- brated baseline; and the gap remains ≈0 at 32px under
|      |      |            |          |     |       |         |          | every variant. |     | The resolution |     | dependence | is  | not an arti- |
| ---- | ---- | ---------- | -------- | --- | ----- | ------- | -------- | -------------- | --- | -------------- | --- | ---------- | --- | ------------ |
| ning | mean | 0, running | variance |     | 1, no | batches | tracked, | so             |     |                |     |            |     |              |
in evaluation mode they are the identity. The untrained fact of an unnormalized baseline. We report seed counts
baseline is therefore not a network with matched nor- rather than standard errors for these paired contrasts
malization but a network with none, while every trained because at n = 5 the paired SEM is itself unstable: it
condition carries statistics accumulated at 32px. That rangesfrom0.001to0.007acrossvariantswhoseper-seed
difference is correlated with the contrast the comparison differencesarecomparable,dependingonhowstronglya
is meant to isolate, so in principle it could produce the givenvarianthappenstocovarywithbackpropacrossthe
| whole | effect. |     |     |     |     |     |     | five initializations. |     |     |     |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
Itdoesnot(Fig.2). Calibratingattheevaluationreso- Thenaturalreadingofwhatcalibrationdoescost,that
lutioncostslittle: −0.003±0.009at224pxwithCIFAR- alignmenttrackshowwellthestoredstatisticsmatchthe
10 statistics (2/5 seeds positive) and −0.011 ± 0.006 activations the evaluation stimuli actually produce, is
5

0.08
0.07
0.06
0.05
0.04
0.03
32 64 96 128 160 224
Evaluation resolution (px)
)1V
1vnoC(
namraepS
0.08
0.07
0.06
0.05
0.04
0.03
32 64 96 128 160 224
Evaluation resolution (px)
Untrained (identity BN) Backprop
CIFAR @ eval-res (B) CIFAR @ 32 px (A)
THINGS @ eval-res (D) THINGS @ 32 px (C)
Figure2: The effect is not the untrained baseline’s
normalization. V1 alignment vs. evaluation resolution
for the untrained network with its initialized (identity)
batch-normalization statistics and for four calibrated
variants(2×2: CIFAR-10ordisjointTHINGSimages,at
32pxorattheevaluationresolution),withthebackprop-
trainednetworkforreference. Calibrationleavesthecon-
volutionalweightsbit-identical. Resolution-matchedcal-
ibrationcostslittleandpreservestheuntrainednetwork’s
V1 advantage over backprop.
contradictedbythesameexperiment. Calibratingonthe
720 evaluation images gives, by construction, an almost
exact estimate of those activations (mean gap 0.0003,
variance ratio 1.00 at the first block) and is the worst of
the eight variants, costing −0.030±0.006 relative to the
identity baseline (0/5 seeds positive). The identity base-
line’sstoredvarianceiswrongbyafactorof7atthefirst
block, and by 37 and 202 at the second and third, and it
aligns best of all. Since the Conv1→V1 comparison de-
pends on the first block alone, this is not a downstream
effect. We can therefore say what the calibration cost is
not, but not what it is, and we leave that open as well.
3.3 Train/eval resolution matching does
not account for it: ResNet-50 and
Swin-Tiny
The obvious explanation is that a model is penalized
when evaluated away from its training resolution, which
predicts that a model trained at 224px should peak at
224px. It does not. An ImageNet-trained ResNet-50
and a Swin-Tiny transformer, both trained at 224px,
show V1 alignment that falls toward 224px and peaks
at low resolution, just as the 32px-trained networks do
(Fig. 3): ResNet-50 from ρ = 0.045 to ρ = 0.032, Swin-
)1V
reyal
ylrae(
namraepS
ResNet-50 (224 px) CNN, untrained
Swin-Tiny (224 px) CNN, backprop (32 px)
Figure 3: Architecture-independent, not
train/eval matching. V1 alignment vs. evalua-
tion resolution for three architecture families. All three
trained models, including ResNet-50 and Swin-Tiny
(both trained at 224px), fall toward 224px; only the
untrainedCNNrises. Thereisnocrossoveratthe224px
training resolution.
Tiny from ρ = 0.079 to ρ = 0.052. The pattern thus
holds across three architecture families (custom CNN,
ResNet-50, Swin-Tiny) and does not depend on train-
ing resolution. Only the untrained network climbs with
resolution.
3.4 Low-level accounts: Gabor, pixel,
and global colour
AcandidateaccountisthatuntrainedfilterslookV1-like
becausetheycapturelow-levelimagestatistics. TheGa-
borversionfailstoo(Fig.4). AGaborfilterbankisitself
only weakly related to V1 (ρ≈0.018–0.037), and across
models and resolutions we see no relationship between
Gabor-similarity and V1 alignment, though with three
model families the analysis is not powered to exclude
a weak one. The clearer evidence is the counterexam-
ple: the ResNet-50’s early stage is about ten times more
Gabor-like than the untrained CNN (Gabor-similarity
≈0.22–0.31vs.≈0.02–0.03)andyetalignslesswellwith
V1. Being Gabor-like does not buy V1 alignment here.
A raw-luminance (pixel) RDM behaves the same way.
ItisitselfweaklyrelatedtoV1(ρ=0.030),andthemod-
els are barely pixel-like, with no ordering that tracks V1
alignment. Theendpointstudyreachedthesameconclu-
sion by a different route, partialling a pixel RDM out of
bothmodelandbrainRDMsandfindingtheV1ordering
fullypreserved, withdecreasesof0.004–0.008[Leuteneg-
ger, 2026]; our own partial-RSA implementation repro-
6

duces that band (0.004 at 224px) before being applied
to the references below. V1-like filter structure is, after
0.08
all, exactly what unsupervised learning on natural im-
age statistics is known to produce [Olshausen and Field, 0.07
1996], so a low-level account is the natural first suspect.
A further low-level account concerns the pooling it- 0.06
self. Global average pooling over the Conv1 map covers
0.05
256 spatial positions at 32px and 12,544 at 224px, a
49-fold increase, so the pooled descriptor converges to-
0.04
ward a global image statistic as resolution rises; with
random filters that limit is close to a global colour or 0.03
luminancemeasure. Thisistheaccountthatcomesclos-
est to working, and the one whose failure is most in- 0.02
formative. Global statistics are a large part of why the
0.0 0.2 0.4 0.6 0.8 1.0
untrained network aligns with V1 at all: a single scalar
Gabor-model similarity (Spearman )
luminancevalueperimagereachesρ=0.074againstthe
V1 RDM, essentially matching the untrained network’s
own 0.075 at 224px, and partialling luminance out of
both model and brain RDMs halves the untrained net-
work’salignment(0.075→0.038). Thatearlyvisualcor-
texisstronglydrivenbylow-levelimagepropertiesisnot
itself new [Goddard and Mullen, 2020]; what we quan-
tify is that in this dataset a one-dimensional descriptor
matches the best model we tested under this compari-
son. The luminance figure itself involves no model and
noreadout,soitboundsthebrainsidedirectly;themod-
els’ figures are specific to rank correlation on globally
pooled features, and a fitted readout on the full feature
map could well place them higher. The claim is there-
fore about what RSA on pooled features can resolve at
V1 here, not about model–brain alignment in general.
Meanchromaticityfailsintheoppositedirection: among
thefivelearning-ruleconditionstheuntrainednetworkis
the least mean-RGB-like (0.24) and backprop the most
(0.54).
Which reference one uses decides the verdict. Par-
tialling all four low-level references jointly out of both
model and brain RDMs leaves the untrained−backprop
gap climbing from −0.020 at 32px to +0.036 at 224px,
against+0.044uncorrected,sotheresolutiondependence
is not simply a colour effect being read twice; partialling
meanluminancealonecutsthegapat224pxfrom+0.044
to +0.026 without flattening it. Convergence toward
the colour histogram does not order the conditions in
the way the account requires: the plain and calibrated
untrained conditions converge at nearly the same rate
(+0.048 and +0.052) while their V1 slopes have oppo-
site signs. Convergence toward mean luminance does,
and more sharply than any other reference. Across the
six conditions the change in luminance similarity over
thesweepandthechangeinV1alignmentranktogether
at Spearman ρ = 0.94, and across five conditions that
share bit-identical convolutional weights and identical
pooling geometry, differing only in their stored normal-
ization statistics, the ordering is perfect (ρ=1.00, exact
permutation p=0.017; ρ=0.87 over all 25 variant-seed
)
namraepS(
tnemngila
1V
224
CNN, untrained
CNN, backprop
32 ResNet-50 Gabor filterbank
32
32
224
224
224
32
Figure4: TheeffectisnotasimpleGaboraccount.
Gabor-model similarity (x) vs. V1 alignment (y) across
models and resolutions. We see no relationship between
the two; the ResNet-50, far more Gabor-like, is less V1-
aligned than the untrained CNN.
points). Within those five, the corresponding values for
mean RGB and pixel similarity are −0.30 and −0.70,
so what is ordered is overall brightness specifically, not
colour or layout. Mean luminance is also the reference
thatbestpredictsV1inthefirstplace(ρ=0.074against
0.045, 0.028 and 0.030).
Theorderingisneverthelessnotapoolingmechanism,
and the same experiment shows why. Under that ac-
count, averaging over 49 times more positions should
drive the descriptor toward the global statistic whatever
the normalization, since all five conditions share the fil-
ters and the pooling. Only the unnormalized network
does so (+0.015, 5/5 seeds); the four calibrated vari-
ants move away from luminance over the same sweep
(−0.011to−0.046). Onevariantseparatesthetwoquan-
tities outright: calibrating on CIFAR-10 at the evalu-
ation resolution lowers luminance similarity across the
sweep(−0.011,1/5seedspositive)whileraisingV1align-
ment (+0.011, 4/5), so the response rises as the pu-
tative dose falls. And within a variant, across seeds,
with the normalization state held fixed, the two quanti-
ties do not covary consistently (correlations from −0.20
to +0.90). The relationship lives between normalization
states rather than along the pooling axis, which makes
it a shared dependence rather than a chain from pooling
to alignment.
Wethereforereportthisaccountastestedandnotsup-
ported. What survives it is an observation rather than
a mechanism: whatever moves V1 alignment in this set-
ting also moves similarity to a single brightness scalar,
and we can explain neither.
7

3.5 Content, not pooled positions backpropagation, what looked like degradation was the
resolution gap widening as training proceeded. This is
Varying evaluation resolution varies two things at once:
notuniformacrossrules: predictivecodingandfeedback
the number of positions the descriptor is pooled over,
alignment lose alignment at the training resolution as
and the image detail available at each. A final experi-
well (−0.026±0.004 and −0.021±0.007; 5/5 and 4/5
ment separates them (Fig. 5). We repeat the sweep in
seeds negative), so for those two the loss is not purely a
a second arm in which every stimulus is first reduced to
resolution artifact. For predictive coding the loss is also
32px and then upsampled to the evaluation resolution,
unlikely to be a weight effect: over the same 40 epochs
so the information content is capped at the training res-
that condition displaces its first convolutional layer by
olutionwhilethenetworkstillpoolsoverthefullnumber
about2%oftheinitializationnorm(AppendixB),which
ofpositions. At32pxthesecondresizeisano-opandthe
is hard to reconcile with an alignment change of 0.03–
two arms are identical by construction, which we verify
0.04. This is consistent with its trajectory being carried
(max |∆ρ|=0 across all cells).
by its accumulating normalization statistics rather than
Read at the endpoints the two arms look alike: every
by its weight-update rule, though we have not tested
sign is preserved and the gap opens wider under upsam-
that directly, and its curve should be read with that
pling. That is misleading. The first step of the upsam-
caveat. Macaque electrophysiology shows the same col-
pled arm is where the resize chain is introduced at all,
lapseatV1/V2,wheretheruledifferencesshrinktoward
anditcoststhetrainedconditionsalargeone-offpenalty
thetrainingresolution: directionalcross-speciessupport,
(backprop −0.033 at 64px) while costing the untrained
from a single seed (see Limitations).
network nothing (−0.000). That penalty is then con-
stant, so it is a property of the content and not of the
3.7 What survives: a genuine learning
pooling. The informative window is 64→224px, where
the upsampled arm’s content is fixed at both ends and effect at LOC
only the pooled positions change, from 1,024 to 12,544.
One effect holds up across the sweep (Fig. 7). At
There the effect largely disappears. The
LOC, backprop-trained networks align better than un-
Random−Backprop gap opens by +0.030±0.002 (5/5
trained ones at every resolution (backprop−untrained
seeds) with content free to vary and by +0.003±0.001
=+0.019±0.001 at 32px and +0.018±0.001 at 224px;
with it fixed, about a tenth as much. Backprop’s decline
5/5 seeds throughout). IT shows a weaker but consis-
isabolishedoutright(−0.023±0.002, 0/5seedspositive,
tentlypositiveversionofthesamething(+0.015±0.002
to −0.000 ± 0.001, 2/5), and feedback alignment and
at 32px, +0.005 ± 0.001 at 224px; 5/5 seeds). What
predictive coding reverse sign (−0.004 → +0.003 and
is stable across resolution here is the difference, not the
−0.005 → +0.004, 5/5 seeds each). One residual
levels: backprop’s own LOC alignment falls from 0.017
survives on the pooling axis, and for one condition
to 0.013 over the sweep, but the untrained baseline sits
only: the untrained network still rises with content fixed
near zero and slightly negative throughout (−0.002 to
(+0.0029±0.0003, 5/5 seeds), about 44% of its rise in
−0.005), so the sign and approximate size of the gap
the native arm.
never change. Learning does leave a mark on the repre-
The dependence is therefore carried by image detail
sentations that this analysis choice does not erase, and
thatexistsabovethetrainingresolution,andthetwodi-
it sits at higher areas rather than at V1.
rections of the effect are not symmetric: the decline of
thetrainedconditionsrequiresthatdetailentirely, while
theuntrainednetwork’sriseispartpoolingandpartcon- 4 Discussion
tent. This locates the effect without explaining it. We
do not know why detail above 32px helps random fil- What the result means. One of the conclusions
ters slightly and hurts trained ones considerably. It does that has drawn interest to biologically plausible and un-
close the pooling axis, which was the last one on which trained models, that they rival backpropagation at early
the global-brightness account could have lived. visual cortex, is in this setting largely a function of the
evaluation resolution. Work on biologically plausible
3.6 It generalizes over training time and rules is especially exposed to it, because those rules are
what force the small-scale training that opens a gap be-
across species
tween a model’s native resolution and the resolution at
The same thing happens over training, not just at the which brain stimuli are modeled. A terminological note:
endpoint (Fig. 6). At 224px backprop V1 alignment strictly, evaluation resolution is an effect modifier rather
falls epoch by epoch (−0.031±0.005 from epoch 0 to thanaconfounderinthecausalsense,sinceitisananal-
40, 5/5 seeds negative), which is the published “train- ysischoicethatchangesthesizeandsignofthemeasured
ing degrades early-visual alignment” result; evaluated at difference rather than a common cause of both. We use
the 32px training resolution the same run returns to its “confound” in the informal sense standard in this litera-
starting value (−0.000±0.005, 3/5 seeds negative). For ture.
8

0.08
0.06
0.04
0.02
0.00
32 64 96 128 160 224
Evaluation resolution (px)
)1V
1vnoC(
namraepS
native content capped at 32 px
64 224 px: pooled positions ×12 content fixed across this span
32 px: identical to native by construction
32 64 96 128 160 224
Evaluation resolution (px)
Untrained (random) Backprop Feedback alignment Predictive coding STDP
Figure 5: The dependence is on image content, not on pooled positions. V1 alignment (Conv1→V1) vs.
evaluationresolution,mean±SEMover5seeds,withstimuliattheirnativeresolution(left)andwiththeircontent
capped at 32px before upsampling (right). The arms are identical at 32px by construction. What differs is the
shape. At native resolution the trained conditions decline steadily across the whole sweep; with content fixed they
drop once at the first step, where the resize chain is introduced, and then run flat or turn back up. Across the
shaded 64 → 224px span the pooled positions increase twelvefold while the right-hand arm’s content stays fixed,
and the Random−Backprop gap opens by +0.003 there against +0.030 on the left. Only the untrained network
rises in both arms.
Which resolution is “correct”? We are not claim- lution, so a receptive-field account alone predicts no dif-
ingthat32pxisrightand224pxwrong,butthechoiceis ference between the arms, and backprop’s decline never-
less arbitrary than the practice suggests. A 3×3 Conv1 theless disappears. What survives is a mixed statement,
filter spans about 9% of the image width at 32px and thatthefilterneedsdetailonitsownspatialscale,andwe
about 1.3% at 224px, so evaluation resolution sets the have not tested it. Until such a criterion is adopted, the
effective receptive-field size of the model’s early layers in practical recommendation stands: if the ranking moves
units of the image, and thence in degrees of visual angle with an analysis choice, it cannot be read as a property
once the stimulus subtense during acquisition is known. of the learning rule until that choice is fixed, so evaluate
Matchingthattothereceptivefieldsoftherecordedneu- atthetrainingresolutionandatseveralothers,andstate
ronsisaprincipledcriterion, anditisappliedelsewhere: the resolution used.
Laskaretal.[2018]choosetheirdownsamplingfactorfor
exactly this reason. It is not applied in the comparisons Mechanism. Noneoffouraccountsexplainsthereso-
this paper is about, which is what makes the choice look lution dependence: train/eval resolution matching, low-
free. level Gabor and pixel statistics, the normalization state
of the untrained baseline, and convergence of the pooled
Our data are consistent with such an account with- descriptor toward a global brightness statistic. Three of
outestablishingit. Section3.3showstheResNet-50and thefourareexcludedbyinterventionsthatholdthecon-
the Swin-Tiny peaking at low resolution despite being volutional weights bit-identical, which is the strongest
trained at 224px, which refutes train/eval matching but form available here. What we can say positively is nar-
is also what a receptive-field criterion predicts, since the rower than a mechanism but not nothing: holding im-
filters of their early stages are small in image units at age content fixed at the training resolution while letting
224px too. Section 3.5 constrains the pure form of it: the pooled positions grow 12-fold removes about 90% of
in the upsampled arm the filters cover exactly the same the effect (§3.5), so the dependence lives on the content
fraction of the image as in the native arm at every reso- axis. Why detail above 32px should help random filters
9

0.06
0.05
0.04
0.03
0.02
0.01
0 10 20 30 40
Training epoch
)1V
1vnoC(
namraepS
Evaluated at 224 px Evaluated at 32 px (training resolution)
0 10 20 30 40
Training epoch
Untrained (random), epoch 0 Backprop Feedback alignment Predictive coding STDP
Figure 6: “Training degrades V1” tracks the same dependence. V1 alignment (Conv1→V1) over training,
evaluated at 224px (left) and at the 32px training resolution (right), mean across seeds and subjects. At 224px
backprop appears to degrade; at 32px it returns to baseline, showing no net degradation.
and hurt trained ones is the question that remains. The noise of re-running it. In particular, the flat resolu-
train/eval-matching account is the one to single out, be- tion profile that made STDP look distinctive was an
causeitistheexplanationweourselvesflaggedasalimi- artifact: repaired, it declines with resolution like ev-
tation in the endpoint study [Leutenegger, 2026], on the ery other trained condition. Every number in this pa-
reasoning that random filters are roughly scale-invariant per comes from the repaired implementation. Correc-
while trained filters are tuned to 32px statistics. The tionnotesidentifyingtheaffectedresultsaccompanythe
sweep turns that limitation into a quantified main effect current arXiv versions of all three earlier preprints. The
and, at the same time, refutes the cause it proposed, training-dynamics result is the one that does not sur-
since two networks trained at 224px also peak at low vive repair: with the defect fixed, predictive coding de-
resolution. grades V1 alignment more than backpropagation does
rather than less, reversing that paper’s central claim.
The random and backprop conditions, which carry the
4.1 A correction to our own earlier work untrained-versus-trainedclaimoftheendpointstudy,are
unaffected.
The predictive-coding and STDP conditions here, in the
endpoint study [Leutenegger, 2026], and in its cross-
species and training-dynamics companions share an im- 4.2 Relation to prior work
plementationinwhichthosetwoclassesoverrodeeval()
with a no-op, so their batch-normalization layers re- Input resolution is not usually treated as a variable in
mained in training mode during feature extraction and this literature, but it is not ignored either: Laskar et al.
theirfeatureswerere-normalizedbythestatisticsofeach [2018] downsample their stimuli by a fixed factor specif-
evaluation batch, while random, backprop and feedback ically to match the effective receptive-field size of the
alignment used stored running statistics. Repairing this model to that of the recorded neurons, and report that
changesthetwoaffectedconditionssubstantially. Ofthe thechoicechangestheirfits. Ourcontributionistotreat
other three, random is unchanged exactly and feedback that choice as a variable rather than a setting, and to
alignment to within 10−5; backprop moves only within show that the conclusion moves with it. That work
run-to-runreproducibilityofthesamepipeline, whichat also contrast-normalizes its stimuli before model eval-
Conv1→V1 is not tighter than about 2×10−3, with a uation, which removes the luminance channel we find
maximum of 5×10−3 across all layer–ROI cells. The re- to be doing so much work here; whether the model–
pair is therefore not detectable in backprop above the brain comparisons that do not normalize are measur-
10

|     |     |     | LOC  (Conv3) |     |     |     |     | IT  (FC1) |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --------- | --- | --- | --- |
0.020
0.0225
Untrained (random)
Backprop
|     | 0.015 |     |     |     |     | 0.0200 |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
0.0175
0.010
 namraepS
0.0150
Untrained (random)
|     | 0.005 |     |     | Backprop |     | 0.0125 |     |     |     |     |     |
| --- | ----- | --- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- |
0.0100
0.000
0.0075
|     | 0.005 |                            |        |     |     | 0.0050 |                            |     |     |     |     |
| --- | ----- | -------------------------- | ------ | --- | --- | ------ | -------------------------- | --- | --- | --- | --- |
|     |       | 32 64                      | 96 128 | 160 |     | 224    | 32 64                      | 96  | 128 | 160 | 224 |
|     |       | Evaluation resolution (px) |        |     |     |        | Evaluation resolution (px) |     |     |     |     |
Figure 7: A genuine learning effect survives at higher areas. Backprop vs. untrained alignment (± SEM, 5
seeds) across resolution at LOC (left) and IT (right). Backprop exceeds the untrained baseline at every resolution
| (5/5 | seeds), | unlike at V1. |     |     |     |     |     |     |     |     |     |
| ---- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing something different is a question our §3.4 raises and so the core findings rest on two of them. (4) STDP
does not settle. The study grew out of a limitation in at higher areas rests on a checkpoint whose FC1 and
our endpoint comparison [Leutenegger, 2026], which re- normalization layers are less reliable, so we keep strong
ported the untrained > backprop effect at V1, showed STDP claims to the early layers. (5) The conditions dif-
it survived a pixel-similarity partial-RSA control, and fer widely in how far training moves the weights. Pre-
foundtheConv1filterstobecolor-opponentratherthan dictive coding displaces its first convolutional layer by
Gabor-like, with no difference in Gabor-peakedness be- 2% of the initialization norm and does not update its
tween rules. Those controls already pointed away from third layer at all, so at the layers mapped to V1 and
purepixelsimilarityandfromGaborstructure;thereso- LOC it is close to, or identical with, the untrained net-
lutionsweepshowswhatwasactuallycarryingtheeffect. work; statements that a result holds across conditions
Our own repaired sweep gives ∆ρ=+0.044 at the same shouldbereadwiththatinmind(AppendixB).(6)Feed-
cell. The untrained condition is bit-identical between back alignment and STDP initialize their convolutional
5×10−7;
the two studies, agreeing to the entire differ- weights with kaiming normal , whereas the remaining
ence sits in backprop, which does not reproduce across conditionsusePyTorch’sdefaultkaiming uniform ; the
pipelines. More generally, reports that untrained net- resultinginitializationscalediffersbyafactorofroughly
works are brain-like at early visual cortex [Saxe et al., 2.4atConv1. Thesingleuntrainedconditionistherefore
2011, Truzzi and Cusack, 2025] are best read with the thematchedcontrolforthreeofthefiveconditionsrather
evaluation resolution in view, especially when a network than all five, and each rule’s own epoch-0 network pro-
is trained at one resolution and aligned at another. videsthematchedbaselinewhereoneisrequired. (7)The
|     |     |     |     |     |     | joint partial | RSA against  | four              | correlated | low-level | refer-    |
| --- | --- | --- | --- | --- | --- | ------------- | ------------ | ----------------- | ---------- | --------- | --------- |
|     |     |     |     |     |     | ences         | drives every | trained condition |            | strongly  | negative, |
4.3 Limitations
|     |     |     |     |     |     | which | is over-subtraction; | the | fraction | of V1 | alignment |
| --- | --- | --- | --- | --- | --- | ----- | -------------------- | --- | -------- | ----- | --------- |
The claims above are bounded by the data in several it removes should be read as an upper bound on what
ways. (1) The macaque analysis is single-seed, so the global image statistics could explain, not as a corrected
|        |         |              |        |         |     | estimate. | (8)Thatascalarluminancevaluematchesour |     |     |     |     |
| ------ | ------- | ------------ | ------ | ------- | --- | --------- | -------------------------------------- | --- | --- | --- | --- |
| phrase | “across | two species” | should | be read | as  | direc-    |                                        |     |     |     |     |
tional support rather than as two independently pow- bestmodelatV1boundswhatanyofthesecomparisons
|      |               |           |      |           |            | can resolve | in this | dataset, including |     | ours; | the finding |
| ---- | ------------- | --------- | ---- | --------- | ---------- | ----------- | ------- | ------------------ | --- | ----- | ----------- |
| ered | replications; | the human | data | carry the | seed-level |             |         |                    |     |       |             |
statistics throughout. (2) The macaque datasets use is about the measurement, and stronger fMRI or elec-
different stimuli for different regions (FreemanZiemba trophysiology may not share it. (9) The dose–response
|          |     |                   |         |          |     | argument | rests on six | resolutions | evaluated |     | on the same |
| -------- | --- | ----------------- | ------- | -------- | --- | -------- | ------------ | ----------- | --------- | --- | ----------- |
| textures |     | vs. HVM objects), | a known | confound | in  | that     |              |             |           |     |             |
comparison. (3) The human fMRI data comprises three 720 images with the same weights; these are six corre-
subjects, one of which shows consistently weak signal, lated measurements of one manipulation, not six inde-
11

pendent tests, and the monotonicity should be read as tially change the apparent advantage of untrained net-
the shape of a single effect rather than as replication. works. It holds across conditions, species, training time,
(10) The luminance-convergence ordering rests on five and three architecture families. Four candidate mecha-
conditions at n=5 seeds, and the within-filter test that nisms do not explain it: train/eval resolution matching,
separatesitfromV1alignmentturnsonasinglecalibra- low-level Gabor and pixel accounts, the normalization
tion variant; both are small samples, and we treat the state of the untrained baseline, and convergence of the
ordering as an observation rather than as an explained pooled descriptor toward a global brightness statistic,
relationship. (11) All results use rank correlation be- three of them excluded by interventions that hold the
tween RDMs built from globally pooled features. That convolutional weights bit-identical. A fifth experiment
discards spatial structure before the comparison, so the locatesit: cappingimagedetailatthetrainingresolution
statements about how much of V1 alignment a single while letting the pooled positions grow 12-fold removes
brightness scalar accounts for are specific to that choice; about 90% of the effect, so what varies with evaluation
a fitted readout on the full feature map might place the resolution is the image detail and not the number of av-
modelshigher,andwehavenottestedone. (12)The720 eraged positions. Along the way we find that a single
evaluation stimuli are single-presentation trials, so the scalar luminance value per image matches the untrained
fMRI RDMs are built from single-trial rather than trial- network’s V1 alignment here, and that luminance sim-
averaged responses. Absolute ρ values therefore carry ilarity orders the conditions exactly as their resolution
measurement noise that repetition averaging would re- slopes do without carrying the effect. That is a caution
move, and no within-subject reliability can be estimated about what this comparison can resolve at all. In this
onthesestimuli. Therelativecomparisonsthatcarryour setting, the learning effect that holds across resolution
claims are unaffected, but the absolute scale should not sits at a higher area (LOC). For this line of work, evalu-
be read as a property of V1. ation resolution is something to control and to report.
Acknowledgements
| 4.4 Future |               | work |            |        |     |            |            |        |        |          |     |         |           |
| ---------- | ------------- | ---- | ---------- | ------ | --- | ---------- | ---------- | ------ | ------ | -------- | --- | ------- | --------- |
|            |               |      |            |        |     |            | The author | thanks | Martin | Schrimpf |     | for the | arXiv en- |
| Several of | the questions |      | this study | raises | are | answerable |            |        |        |          |     |         |           |
with the same infrastructure. Section 3.5 places the de- dorsement and helpful feedback, and the creators of
|                |        |               |          |            |          |              | the THINGS-fMRI, |          | FreemanZiemba2013, |     |             | and  | Maja-     |
| -------------- | ------ | ------------- | -------- | ---------- | -------- | ------------ | ---------------- | -------- | ------------------ | --- | ----------- | ---- | --------- |
| pendence       | on the | content       | axis,    | which      | narrows  | the search   |                  |          |                    |     |             |      |           |
|                |        |               |          |            |          |              | jHong2015        | datasets | and                | the | Brain-Score | team | for their |
| without        | ending | it: the next  | question |            | is which | property     |                  |          |                    |     |             |      |           |
| of the detail  | above  | the training  |          | resolution | is       | responsible, | infrastructure.  |          |                    |     |             |      |           |
| and a bandpass |        | decomposition |          | of the     | stimuli  | would be     |                  |          |                    |     |             |      |           |
the natural way to ask. A second is whether the effect Code and Data Availability
| survives | a readout | that | does | not discard |     | spatial struc- |          |          |                              |     |     |     |     |
| -------- | --------- | ---- | ---- | ----------- | --- | -------------- | -------- | -------- | ---------------------------- | --- | --- | --- | --- |
|          |           |      |      |             |     |                | Code and | results: | https://github.com/nilsleut. |     |     |     |     |
ture;ourcomparisonrank-correlatesgloballypooledfea-
tures, whereasafittedreadoutonthefullfeaturemapis
standard elsewhere and is the obvious robustness check Appendix A: Hyperparameter Details
| on the scale | results | of §3.4. |     | A third | is the | receptive- |     |     |     |     |     |     |     |
| ------------ | ------- | -------- | --- | ------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
field criterion discussed above, which requires the stim- Condition lr Notes
ulus subtense during acquisition and a matched-angle BP 10−3 (Adam) weightdecay10−4,cosine
sweep. Whether the phenomenon appears in architec- schedule, gradient clip
|               |       |                |     |     |         |          |     |     |     | 1.0, | dropout | 0.3, cross- |     |
| ------------- | ----- | -------------- | --- | --- | ------- | -------- | --- | --- | --- | ---- | ------- | ----------- | --- |
| tures without | batch | normalization, |     | and | whether | calibra- |     |     |     |      |         |             |     |
entropy
| tionproceduresoutsidethefamilyweconstructedbehave |     |     |     |     |     |     |     | 5×10−4 |       |                       |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --------------------- | --- | --- | --- |
|                                                   |     |     |     |     |     |     | FA  |        | (SGD) | momentum0.9,fixedran- |     |     |     |
differently,arebothopen;soiswhycalibrationcostsany
domfeedbackweights
10−4
alignment at all, given that its cost does not track how PC T = 10 inference steps,
|             |        |            |       |     |            |         |     |     |     | inference |     | rate 0.02; |     |
| ----------- | ------ | ---------- | ----- | --- | ---------- | ------- | --- | --- | --- | --------- | --- | ---------- | --- |
| closely the | stored | statistics | match | the | evaluation | activa- |     |     |     |           |     |            |     |
Adam-trainedreadout
tions. Swin-Tiny extends the result to one transformer STDP 5×10−4 A± =0.003, τ± =20ms,
family,andotherViTfamiliesremaintobetestedrather 10 timesteps; Adam-
than assumed. We have no positive mechanism, and we trainedreadout
|              |       |      |             |     |         |            | All conditions |     | share the | architecture |     | and training | setup |
| ------------ | ----- | ---- | ----------- | --- | ------- | ---------- | -------------- | --- | --------- | ------------ | --- | ------------ | ----- |
| would rather | leave | that | distinction |     | visible | than close | it             |     |           |              |     |              |       |
prematurely. in Section 2 (three convolutional blocks 32/64/128, FC1
|     |     |     |     |     |     |     | 512, FC2   | 10;  | 8,000-image | CIFAR-10 |           | subset at | 32×32, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----------- | -------- | --------- | --------- | ------ |
|     |     |     |     |     |     |     | batch size | 128, | 40 epochs,  |          | 5 seeds). | fMRI      | RDMs   |
5 Conclusion
|     |     |     |     |     |     |     | were computed   |     | with correlation |                | distance | on single-trial |         |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------------- | -------------- | -------- | --------------- | ------- |
|     |     |     |     |     |     |     | BOLD responses. |     | The              | 720 evaluation |          | stimuli are     | single- |
RSA comparisons of learning rules and architectures presentationtrialsinallthreesubjects,sonotrialaverag-
at early visual cortex are governed by an evaluation- ing occurs for any of them; the averaging step in the ex-
resolution confound that can manufacture or substan- traction code is a no-op here. No additional z-scoring or
12

outlier removal was applied beyond the THINGS-fMRI Kriegeskorte, N., Mur, M., and Bandettini, P. (2008).
preprocessing pipeline. Representational similarity analysis: connecting the
branchesofsystemsneuroscience.FrontiersinSystems
Neuroscience, 2:4.
Appendix B: Weight Displacement from
Initialization Laskar, M. N. U., Sanchez Giraldo, L. G., and Schwartz,
O. (2018). Correspondence of deep neural networks
Relative change ∥W −W ∥/∥W ∥ in the convolutional
40 0 0 and the brain for visual textures. arXiv:1806.02888.
weights over 40 epochs (seed 42), measured against the
shared initialization. Only backpropagation and predic- Leutenegger, N. (2026). Untrained CNNs match back-
tive coding share that initialization; feedback alignment propagation at V1: A systematic RSA compar-
and STDP use a different scheme and are therefore not ison of four learning rules against human fMRI.
comparable on this baseline (Limitations, item 6). arXiv:2604.16875.
Layer →ROI Backprop PredictiveCoding Lillicrap, T. P., Cownden, D., Tweed, D. B., and Aker-
Conv1 V1/V2 29.4% 2.1% man, C. J. (2016). Random synaptic feedback weights
Conv2 – 90.4% 7.2% support error backpropagation for deep learning. Na-
Conv3 LOC 119.2% 0.0%
ture Communications, 7:13276.
Liu,Z.,Lin,Y.,Cao,Y.,Hu,H.,Wei,Y.,Zhang,Z.,Lin,
Appendix C: Best-Layer Selection
S., and Guo, B. (2021). Swin Transformer: Hierarchi-
Instead of the fixed Conv1→V1 mapping, selecting for cal vision transformer using shifted windows. ICCV,
eachconditionandresolutionwhicheverlayeralignsbest pp. 10012–10022.
with V1. The best layer does not drift with resolution
Majaj, N. J., Hong, H., Solomon, E. A., and DiCarlo,
exceptforpredictivecoding,andtheRandom−Backprop
J. J. (2015). Simple learned weighted sums of inferior
gap grows in the same way.
temporal neuronal firing rates accurately predict hu-
32px 96px 224px mancoreobjectrecognitionperformance.J.Neurosci.,
Bestlayer,random Conv2 Conv2 Conv2 35:13402–13418.
Bestlayer,backprop Conv1 Conv1 Conv1
Bestlayer,FA/STDP Conv2 Conv2 Conv2 Masquelier, T. and Thorpe, S. J. (2007). Unsuper-
Bestlayer,PC Conv1 Conv1 Conv2
vised learning of visual features through spike tim-
Gap,fixedConv1 −0.001 +0.025 +0.044 ing dependent plasticity. PLOS Computational Biol-
Gap,bestlayer +0.014 +0.041 +0.060 ogy, 3(2):e31.
Seedspositive 4/5 5/5 5/5
Olshausen, B. A. and Field, D. J. (1996). Emergence
of simple-cell receptive field properties by learning a
References
sparse code for natural images. Nature, 381:607–609.
Bi, G.-q. and Poo, M.-m. (1998). Synaptic modifica- Rao, R. P. N. and Ballard, D. H. (1999). Predictive cod-
tions in cultured hippocampal neurons. J. Neurosci., inginthevisualcortex.Nature Neuroscience,2:79–87.
18:10464–10472.
Saxe, A. M., Koh, P. W., Chen, Z., Bhand, M., Suresh,
Freeman, J., Ziemba, C. M., Heeger, D. J., Simoncelli, B., and Ng, A. Y. (2011). On random weights and
E. P., and Movshon, J. A. (2013). A functional and unsupervised feature learning. ICML.
perceptual signature of the second visual area in pri-
Schrimpf,M.,Kubilius,J.,Hong,H.,etal.(2020).Brain-
mates. Nature Neuroscience, 16:974–981.
Score: Whichartificialneuralnetworkforobjectrecog-
nition is most brain-like? bioRxiv.
Goddard, E. and Mullen, K. T. (2020). fMRI represen-
tational similarity analysis reveals graded preferences
Truzzi, A. and Cusack, R. (2025). Neural responses
forchromaticandachromaticstimuluscontrastacross
in early visual cortex are well predicted by random-
human visual cortex. NeuroImage, 215:116780.
weight CNNs. bioRxiv.
He, K., Zhang, X., Ren, S., and Sun, J. (2016). Whittington,J.C.R.andBogacz,R.(2017).Anapprox-
Deep residual learning for image recognition. CVPR, imation of the error backpropagation algorithm in a
pp. 770–778. predictive coding network with local Hebbian synap-
tic plasticity. Neural Computation, 29:1229–1262.
Hebart,M.N.,Contier,O.,Teichmann,L.,etal.(2023).
THINGS-data, a multimodal collection of large-scale Yamins, D. L. K. and DiCarlo, J. J. (2016). Using goal-
datasetsforinvestigatingobjectrepresentationsinhu- drivendeeplearningmodelstounderstandsensorycor-
man brain and behavior. eLife, 12:e82580. tex. Nature Neuroscience, 19:356–365.
13
---- END DOCUMENT ----
