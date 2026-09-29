Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Robustness of Anomaly Detection Models for
Industrial Control Systems under Training-Time
Data Contamination
Mustafa Umut Ozbek, Taiwo Ojo, Pooria Madani, Khalil El-Khatib, Li Yang
Ontario Tech University, Oshawa, Ontario, Canada
Emails: mustafaumut.ozbek@ontariotechu.net, taiwo.ojo2@ontariotechu.net,
pooria.madani@ontariotechu.ca, khalil.el-khatib@ontariotechu.ca, li.yang@ontariotechu.ca
Abstract—Machine-learning-based anomaly detection is in- buildthemistrustworthy.Inpractice,thatassumptionisoften
creasingly used in industrial control systems (ICS), yet most weak. Datasets used for offline detector development may
studies assume that detector training data is trustworthy. In
be assembled from historian exports, archived sensor traces,
practice, training data may be corrupted through compromised
engineering workstations, alarm logs, operator annotations,
logs, labeling errors, manipulated historian records, or unsafe
retraining processes. This paper evaluates the robustness of and automated preprocessing pipelines. Errors, compromise,
offline ICS anomaly-detection pipelines on the Secure Water ormanipulationatanystagecancontaminatethefinaltraining
Treatment (SWaT) benchmark under training-time contami- corpus. As a result, a detector that appears strong under clean
nation. We assess 11 heterogeneous anomaly detectors under
offline evaluation may still become unreliable if its training
three contamination strategies: random injection, similarity-
data has already been corrupted before deployment [4], [5].
targeted injection, and feature-noise injection. The first two
insert attack samples into the nominal training pool, while This concern is especially important in anomaly-based
the third adds bounded Gaussian noise to selected normal pipelines trained on normal data only. In such settings, the
training samples. These attacks are contamination-based rather
detector does not learn an explicit supervised boundary be-
thangradient-drivenpoisoningmethods.Contaminationbudgets
tween normal and attack classes. Instead, it learns a repre-
from 1% to 10% are evaluated using clean validation and
test sets under a unified offline protocol. The results show sentation, support region, density structure, geometric pro-
that robustness is strongly model-dependent and cannot be file, or reconstruction pattern of nominal process behavior.
predicted from clean-data performance alone. Injection-based Contaminating the normal training pool therefore distorts the
contamination causes the greatest degradation, particularly for
learned notion of normality itself. Attack samples injected
local-densityanddistance-baseddetectors,whereasfeature-noise
into nominal training data can weaken the anomaly boundary,
contamination has a comparatively limited effect. PCA, SVM,
HBOS, and IForest remain relatively stable, while the tuned while perturbations applied to normal samples can blur the
neural detectors demonstrate intermediate robustness. Overall, distinction between benign and malicious behavior. Despite
the findings highlight the importance of training-data integrity this risk, the comparative robustness of anomaly-based ICS
inML-enabledICSmonitoring,subjecttotheevaluateddataset,
detectors under offline training-time contamination remains
models, and threat assumptions.
insufficiently characterized across a broad and diverse set of
Index Terms—industrial control systems, adversarial machine
detector families.
learning, training-time data contamination, anomaly detection,
critical infrastructure Prior work has demonstrated effective clean-condition de-
tection on the Secure Water Treatment (SWaT) benchmark
I. INTRODUCTION using recurrent, convolutional, one-class, PCA-based, and
reconstruction models [1], [6]–[9]. Adversarial ICS studies,
Industrial control systems (ICS) support critical infrastruc-
however, have concentrated mainly on inference-time evasion
ture such as water treatment, energy, manufacturing, and digi-
[10]–[12] or poisoning of online-adaptive neural detectors
talinstrumentationandcontrolsystems,wherecyberincidents
[13], [14].
can produce direct operational and safety consequences. As
We address this gap with a unified benchmark on SWaT
these systems become increasingly connected and data-rich,
[15],[16].Elevennormal-onlydetectorsaretestedunderthree
anomaly-based detection has received growing attention as
contamination strategies at 1%, 3%, 5%, and 10% budgets.
a complement to signature-based and rule-based monitoring.
Thresholds are calibrated on clean validation data and applied
In particular, anomaly-based detectors are attractive in ICS
unchanged to a clean held-out test set. Our contributions are:
because normal operating behavior is often easier to collect
thancomprehensiveattackdata,andmultivariateprocessmea- 1) a comparative offline training-contamination benchmark
surements can reveal deviations that are difficult to capture spanning eleven heterogeneous anomaly detectors;
with static signatures alone [1]–[3]. 2) a common evaluation of random injection, similarity-
Most existing ICS anomaly-detection studies evaluate mod- targetedinjection,andfeature-noiseinjectionacrossfour
elsundertheimplicitassumptionthatthetrainingdatausedto budgets;
ToappearintheProceedingsofIEEECASCON2026.
©2026IEEE.Personaluseofthismaterialispermitted.PermissionfromIEEEmustbeobtainedforallotheruses,inanycurrentorfuturemedia,including
reprinting/republishingthismaterialforadvertisingorpromotionalpurposes,creatingnewcollectiveworks,forresaleorredistributiontoserversorlists,orreuseofany
copyrightedcomponentofthisworkinotherworks.
6202
guA
42
]RC.sc[
1v74532.8062:viXra

3) an analysis that jointly considers F1-score degradation, evasion rather than poisoning. Zizzo et al. studied adversarial
false-negative rate (FNR), and training cost rather than attacks against time-series intrusion-detection models for ICS
clean F1-score alone; and showed that recurrent detectors can be manipulated even
4) a transparent configuration-level evaluation that explic- when an attacker controls only a subset of variables [10].
itly reports differences in data representation, tuning Erbaetal.showedthatrealisticICSmanipulationmustsatisfy
depth, training scale, and compute resources. process and physical constraints, making the attack space
The remainder of this paper is organized as follows. Sec- substantially different from conventional adversarial examples
tion II reviews related workon ICS anomaly detection, adver- [11]. Anthi et al. likewise demonstrated that adversarial per-
sarialmachinelearning,andtraining-timecontamination.Sec- turbationscanmateriallyreducemachine-learning-basedcyber
tion III defines the threat model and contamination methodol- defenses in industrial environments [12]. Collectively, these
ogy. Section IV describes the dataset, detector configurations, studies show that strong clean-data detection performance
and experimental protocol. Section V presents and discusses shouldnotbeinterpretedasevidenceofadversarialrobustness.
the experimental results, and Section VI concludes the paper
C. Training-Time Poisoning and Contamination of Anomaly
and outlines directions for future work.
Detectors
II. RELATEDWORK Compared with evasion, training-time corruption of ICS
anomaly detectors has received much less direct study.
A. ICS Anomaly Detection
Kravchik, Biggio, and Shabtai analyzed poisoning attacks
Anomaly-based detection has become a major line of re-
against online-trained neural anomaly detectors for ICS [13].
search in ICS because process behavior is highly structured,
This work was later extended to a practical evaluation of
while comprehensive attack labels are often limited or costly
poisoning attacks on online anomaly detectors, again em-
to obtain. The SWaT testbed and dataset have become widely
phasizing online adaptation as the primary threat surface
used benchmarks because they provide a realistic and repro-
[14]. That setting is highly relevant, but differs from the
ducibleplatformforevaluatingprocess-awareattack-detection
offline training regime used in many operational pipelines,
methods [15], [16]. Prior SWaT studies include recurrent
where models are built or periodically refreshed from curated
models trained on normal data [1], convolutional models
historian logs, archived process traces, and exported datasets
[6], unsupervised and one-class approaches [7], sequence-to-
before deployment. Online poisoning studies therefore do not
sequence architectures [8], lightweight neural and PCA-based
fully characterize contamination of the normal training pool
detection [9], and methodology-oriented work emphasizing
during offline model development.
preprocessing, thresholding, and evaluation [17].
OutsideICS,thebroaderadversarialmachine-learningliter-
Together, these studies support two recurring conclusions.
aturehasshownthattraining-timecorruptioncansubstantially
First,anomaly-basedmonitoringisanaturalfitforICSsettings
degrade anomaly-detection and classification systems. Rubin-
because normal process behavior is repetitive, correlated, and
stein et al. demonstrated that poisoning can distort anomaly
usually easier to collect than diverse attack traces. Second,
detectors, particularly PCA-based detectors, by shifting the
there is no universally dominant detector family. Broader
learned model of normality [4]. Other work developed poi-
reviews of machine learning for ICS security reach similar
soning attacks against SVMs and deep learning, certified
conclusions while identifying persistent challenges in cross-
defenses, targeted clean-label attacks, and broader surveys
paper comparability, dataset dependence, and deployment re-
[5], [23]–[26]. Recent CPS studies also address provable
alism [2], [3].
mitigation and dynamic backdoors [27], [28]. These studies
Our study also intersects with benchmark design for
provide the conceptual basis for training-time vulnerability,
anomalyandtime-seriesanomalydetection.Priorworkshows
butprimarilyaddressoptimization-basedpoisoningratherthan
that detector rankings can shift substantially with metric
the contamination-style attack families considered here.
choice, hyperparameter treatment, and evaluation protocol
[18]–[20], while time-series studies highlight temporal leak- D. Research Gap
age, split construction, and inconsistent evaluation rules [21],
Prior ICS studies provide strong evidence that anomaly-
[22]. These observations reinforce the need to interpret de-
baseddetectorscanperformeffectivelyundercleanconditions
tector performance through both the model family and the
[1], [6]–[9], [17], while adversarial ICS studies have focused
evaluation pipeline used to generate the reported results.1
mainly on evasion or poisoning tied to online retraining
[10]–[14]. What remains insufficiently characterized is the
B. Adversarial Machine Learning in Industrial Control Sys-
comparative robustness of a broad set of anomaly-based ICS
tems
detectors under offline training-time contamination within a
Althoughadversarialmachinelearninghasreceivedincreas-
unified benchmarking framework.
ing attention in ICS security, most prior work has focused on
More specifically, to the best of our knowledge, existing
literaturedoesnotprovideaconsistentcomparisonacrosshet-
1Code and experiment configurations for this paper are
erogeneousanomaly-detectorfamiliesunderthesamecontam-
publicly available at: https://github.com/ANTS-OntarioTechU/
Robustness-Anomaly-Detection-ICS-Data-Contamination ination definitions, budgets, threshold-calibration procedure,

andcleanheld-outevaluationprotocol.Italsoremainsunclear TABLEI
whether detectors that appear strong on clean benchmark data SUMMARYOFTHEEVALUATEDTRAINING-TIMECONTAMINATION
STRATEGIES.
retainthatadvantageoncethenormaltrainingpooliscontami-
nated.Thenoveltyofthisstudyisaunified,configuration-level Strategy Training-poolmanipulation Finalsize
robustness benchmark across heterogeneous anomaly-detector Random in- Uniformly sample k observa- N+k
jection tions from attack pool A and
familiesundercommontrainingpools,contaminationbudgets, appendthemasnominal
clean calibration data, held-out testing, and evaluation rules. Similarity- Append the k attack observa- N+k
targeted tions closest to the clean cen-
III. THREATMODELANDCONTAMINATION injection troid
Feature-noise Perturb k selected clean ob- N
METHODOLOGY injection servations with clipped, scaled
Gaussiannoise
A. System and Adversary Model
We consider an offline anomaly-detection pipeline for ICS
under a normal-only training regime. Each detector is trained nominal archive through missing labels, event-window mis-
tomodelnominalprocessbehaviorfromacleantrainingpool, alignment, or unsafe merging of exports. Second, stored nor-
while model selection and threshold calibration use a labeled mal observations may be modified through historian compro-
validation split and final performance is measured on a held- mise or preprocessing faults without changing the number of
outtestsplitthatisnevermodifiedduringcontamination.This records. Injection attacks model the first path, while feature-
setup reflects a practical workflow in which historical process noise injection models the second. The benchmark does not
data are curated, preprocessed, and used to develop anomaly claim that these mechanisms exhaust real data-governance
detectors before deployment. failures; they provide repeatable stress tests with a common
Theadversary’sobjectiveistodegradethedetector’sability budget.
to distinguish attacks from normal behavior at test time while
B. Contamination Strategies
preserving the appearance of a plausible training workflow.
Morespecifically,theattackerseekstoincreasefalsenegatives, Let the clean normal training pool be D clean = {x i }N i=1
reduce F1-score and recall, and distort the learned notion of and the available attack pool be A={a j }M j=1 . For a training-
normality so that malicious behavior is more likely to be pool-relative budget p, the adversary manipulates k = ⌊pN⌋
accepted as benign. samples.Fortheinjectionattacks,appendingk samplesyields
We assume a gray-box adversary with training-time ac- afinalinjectedfractionk/(N+k)(approximately9.09%when
cess only. The attacker knows the feature representation and p=10%); feature noise instead modifies k of the original N
general anomaly-detection pipeline, but does not modify the samples. Thus, p denotes a common budget relative to the
clean validation or test sets and does not interact with the clean pool rather than an identical final-set fraction across
deployed detector at inference time. Depending on the con- attack families.
taminationstrategy,theadversaryeitherinjectsattacksamples For the pointwise detectors and AE, the attack pool is the
into the nominal training pool or perturbs selected normal attack-labeled portion of the stratified training fold and is
trainingobservations.Thesimilarity-targetedstrategyassumes therefore disjoint from their validation and test observations.
more informed sample selection than random contamination, LSTM-AE uses this pointwise training-fold attack pool to
while all evaluated strategies remain weaker than white-box contaminate its separate contiguous normal training block,
optimization-based attacks. The budget is at most 10% of the as detailed in Section IV-A. This controlled resource isolates
clean training-pool size. training contamination within each implemented protocol but
For clarity, “uncontaminated” means that no training-time is optimistic relative to end-to-end data-governance failures.
attack is applied to validation or test observations; it does Theinjectedpoolshouldthereforebeunderstoodasaneval-
not mean that the labeled validation split is attack-free. The uation resource rather than an assumption that an operational
restrictions to clean calibration and test data isolate training- attackerpossessesaperfectlycuratedattackcorpus.Itenables
time contamination effects, but may be optimistic relative to controlled comparisons across budgets and seeds. Similarly,
workflows in which curation errors or historian compromise the clean validation and test assumption prevents threshold
propagate beyond the training data. corruption from being conflated with model corruption, but
Offline ICS datasets can absorb attack traces or distorted may underestimate failures in pipelines where the same data-
values through annotation, alignment, curation, export, or quality problem propagates across all splits.
preprocessing failures. These failures need not alter the run- 1) Random Injection: The attacker uniformly samples S ⊆
ning process; they affect a normal-only detector through data A and forms
presented as benign. We retain poisoning for continuity with
D =D ∪S, |S|=min(k,|A|). (1)
cont clean
the literature, but evaluate contamination-style rather than
gradient-driven worst-case attacks. Figure 1 summarizes the This represents unsafe curation or accidental inclusion of
workflow. attack traces in data later treated as normal.
Twopracticalcorruptionpathsmotivatetheevaluatedstrate- Random injection does not exploit detector gradients or
gies. First, attack-period observations may be included in a model parameters. Its strength comes from relabeling attack

Fig.1. OfflineICSanomaly-detectionworkflow.Contaminationisconfinedtothenormaltrainingpool;validationandtestdataremainuncontaminated.
behavior implicitly as normal during fitting. It provides a mentfixestheGaussianmagnitudeat0.15andvariesonlythe
simple baseline for measuring whether a detector’s learned fraction of modified samples. Consequently, a near-null result
support expands around malicious process states. establishes limited sensitivity to this tested configuration, not
2) Similarity-Targeted Injection: The clean centroid is general robustness to feature corruption.
N−1(cid:80)
µ = x . Attack samples are ranked by d = Thestrategiescoverunsystematicattackinclusion,centroid-
| clean | i i |     |     |     | j   |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∥a −µ ∥ , and the k closest samples are inserted. “Tar- targeted inclusion, and corruption of nominal records. All use
| j clean | 2   |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
geted” therefore denotes centroid-based data selection, not the same clean held-out protocol.
| gradient-based | optimization | or guaranteed | worst-case |     | target- |     |     |     |     |
| -------------- | ------------ | ------------- | ---------- | --- | ------- | --- | --- | --- | --- |
IV. DATASETANDEXPERIMENTALPROTOCOL
ing.
Thisstrategyprefersattackobservationsthatappearglobally A. Dataset and Preprocessing
| similar to | the clean pool | after | scaling. The | centroid | is a |      |                       |             |                  |
| ---------- | -------------- | ----- | ------------ | -------- | ---- | ---- | --------------------- | ----------- | ---------------- |
|            |                |       |              |          |      | SWaT | contains multivariate | time-series | data from normal |
deliberately model-agnostic selection rule, which allows the operation and attack scenarios [15], [16]. Timestamp columns
| same contaminated | training | set | to be evaluated | across | all |     |     |     |     |
| ----------------- | -------- | --- | --------------- | ------ | --- | --- | --- | --- | --- |
areremoved,sourcefilesarealignedoncommonfeatures,val-
detector families. It may be weak for detectors governed by uesarecoercedtonumericform,invalidrowsaredropped,and
localstructureortemporalcontext,soitsresultsareinterpreted
sevenconstantcolumns(P202,P301,P401,P404,P502,P601,
| as one reproducible | similarity | heuristic | rather | than a | worst- |     |     |     |     |
| ------------------- | ---------- | --------- | ------ | ------ | ------ | --- | --- | --- | --- |
andP603)areremoved.Aftertheimplementedpreprocessing,
case targeted attack. the pointwise benchmark pool contains 449,919 samples, 44
| 3) Feature-Noise | Injection: | The | attacker | selects | Q ⊆ |           |                     |               |                |
| ---------------- | ---------- | --- | -------- | ------- | --- | --------- | ------------------- | ------------- | -------------- |
|                  |            |     |          |         |     | features, | and a 12.14% attack | ratio. MinMax | parameters are |
D |Q|=k,
clean , and replaces each selected sample with fitted on training data only and then applied to validation and
|     | x˜ =clip | (x +z   | ⊙σ ),  |     | (2) | test data. |     |     |     |
| --- | -------- | ------- | ------ | --- | --- | ---------- | --- | --- | --- |
|     | i        | [0,1] i | i feat |     |     |            |     |     |     |
PointwisedetectorsandAEuseastratified70/15/15splitof
wherez ∼N(0,0.152I)andσ isthevectorofper-feature the pooled normal- and attack-file observations. Only normal
| i   |     | feat |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
standarddeviations.NoiseisaddedafterMinMaxscaling.This samples from the training fold are used for detector fit-
preservestraining-setsizewhilemodelingcorruptionofstored ting; labeled validation observations calibrate the F1-oriented
process values. threshold. LSTM-AE instead preserves the source-file order:
Clipping maintains the normalized feature range and the the first 70% of the normal-operation file is used for training,
per-feature scale factor prevents a common perturbation mag- the next 15% for early stopping, and the final 15% supplies
nitude from dominating low-variance variables. The experi- normal test observations. The first half of the attack-period

|     |     |     |     |     |     |     |     | Table | III summarizes |     | the | heterogeneous |     | scoring | mecha- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | --- | --- | ------------- | --- | ------- | ------ |
TABLEII
POINTWISESWATBENCHMARKPOOLAFTERPREPROCESSING.
nisms,finalretainedconfigurations,andtraininginputs,allow-
ingcontaminationsensitivitytobecomparedacrossincompat-
|     | Item |     |     |     |     | Value |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ibledefinitionsofnormalitywithoutduplicatingtraining-scale
|     | Processedsamples |     |     |     |     | 449,919 |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Retainedfeatures |     |     |     |     |         | 44  |     |     |     |     |     |     |     |     |
information.
|     | Normal/attacksamples |     |     |     | 395,298/54,621 |        |     |                    |     |         |     |             |        |     |     |
| --- | -------------------- | --- | --- | --- | -------------- | ------ | --- | ------------------ | --- | ------- | --- | ----------- | ------ | --- | --- |
|     | Attackratio          |     |     |     |                | 12.14% |     |                    |     |         |     |             |        |     |     |
|     |                      |     |     |     |                |        |     | C. Implementation, |     | Tuning, |     | and Compute | Policy |     |     |
|     | Pointwisesplit       |     |     |     | 70%/15%/15%    |        |     |                    |     |         |     |             |        |     |     |
Normalization Train-fittedmin-maxto[0,1] The classical benchmark uses PyOD implementations with
|     |     |     |     |     |     |     |     | a common | normal-only |     | fitting | workflow. |     | IForest, | HBOS, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------- | --------- | --- | -------- | ----- |
CBLOF,andPCAusethefullpointwisenormaltrainingpool,
| file is used | for | threshold | selection |     | and the | second | half for |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --------- | --- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
whileSVM,LOF,KNN,ABOD,andMCDuseafixed50,000-
testing.ForcontaminatedLSTM-AEruns,attackobservations point uniform subsample to control super-linear memory or
| are drawn      | from     | the       | attack-labeled |                 | portion | of the | pointwise   |                      |            |      |            |                  |          |                |            |
| -------------- | -------- | --------- | -------------- | --------------- | ------- | ------ | ----------- | -------------------- | ---------- | ---- | ---------- | ---------------- | -------- | -------------- | ---------- |
|                |          |           |                |                 |         |        |             | distance-computation |            |      | costs.     | IForest          | uses 100 | trees          | and the    |
| training       | fold and | appended  | to             | the contiguous  |         | normal | training    |                      |            |      |            |                  |          |                |            |
|                |          |           |                |                 |         |        |             | default              | 256-sample | tree | subsample. |                  | LOF uses | 20             | neighbors, |
| block. Windows |          | of length |                | W =             | 30 are  | then   | constructed |                      |            |      |            |                  |          |                |            |
|                |          |           |                |                 |         |        |             | KNN scores           | distance   |      | to the     | fifth neighbor,  |          | CBLOF          | uses eight |
| independently  |          | within    | the training,  | early-stopping, |         |        | threshold-  |                      |            |      |            |                  |          |                |            |
|                |          |           |                |                 |         |        |             | clusters,            | and ABOD   |      | uses its   | fast 10-neighbor |          | configuration. |            |
selection, and test arrays, so no window crosses a boundary PCA retains 90% variance, while SVM uses an RBF kernel
| between      | these      | arrays.        | A window     |               | is labeled | anomalous       |          | if            |             |           |              |                |         |        |           |
| ------------ | ---------- | -------------- | ------------ | ------------- | ---------- | --------------- | -------- | ------------- | ----------- | --------- | ------------ | -------------- | ------- | ------ | --------- |
|              |            |                |              |               |            |                 |          | with ν =0.01  |             | and gamma |              | = scale.       |         |        |           |
| any included | time       | step           | is attacked. | This          | temporal   |                 | protocol | is            |             |           |              |                |         |        |           |
|              |            |                |              |               |            |                 |          | Table         | III records |           | the retained | settings       |         | needed | to inter- |
| stricter,    | but its    | sequence-level |              | labels        | are not    | identical       | to the   |               |             |           |              |                |         |        |           |
|              |            |                |              |               |            |                 |          | pret and      | reproduce   | each      | reported     | configuration. |         |        | The PyOD  |
| pointwise    | evaluation |                | and must     | be considered |            | in cross-family |          |               |             |           |              |                |         |        |           |
|              |            |                |              |               |            |                 |          | contamination |             | argument  |              | is fixed       | at 0.05 | during | construc- |
comparisons. tionwhereapplicable,butitdoesnotdefinethefinaloperating
| Preprocessing |           | is fitted | without |              | using | validation | or test    |            |          |                        |     |              |           |        |           |
| ------------- | --------- | --------- | ------- | ------------ | ----- | ---------- | ---------- | ---------- | -------- | ---------------------- | --- | ------------ | --------- | ------ | --------- |
|               |           |           |         |              |       |            |            | threshold. | Every    | detector               |     | is converted | to        | binary | decisions |
| statistics.   | Timestamp |           | columns | are removed, |       | the        | normal and |            |          |                        |     |              |           |        |           |
|               |           |           |         |              |       |            |            | using the  | separate | validation-calibration |     |              | procedure |        | described |
attackfilesarealignedontheircommonprocessvariables,and
|     |     |     |     |     |     |     |     | below. Thus, | the | benchmark’s |     | 1–10% | attack | budgets | describe |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | --- | ----- | ------ | ------- | -------- |
nonnumericorinvalidrowsarediscardedbeforesplitting.The
|     |     |     |     |     |     |     |     | training-pool | manipulation |     |     | and should | not | be confused | with |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --- | --- | ---------- | --- | ----------- | ---- |
seven removed process variables are constant under the avail- the library’s internal contamination parameter.
| able traces | and       | therefore | provide | no             | discriminatory |     | variation. |         |         |             |                   |           |               |             |        |
| ----------- | --------- | --------- | ------- | -------------- | -------------- | --- | ---------- | ------- | ------- | ----------- | ----------------- | --------- | ------------- | ----------- | ------ |
|             |           |           |         |                |                |     |            | Tuning  | follows | a           | sensitivity-first |           | policy.       | A classical | pa-    |
| For the     | pointwise | protocol, |         | stratification | preserves      |     | the attack |         |         |             |                   |           |               |             |        |
|             |           |           |         |                |                |     |            | rameter | family  | is promoted |                   | only when | a preliminary |             | change |
ratioinvalidationandtestdata;onlythenormalportionofthe
|     |     |     |     |     |     |     |     | improves | F1 by | at least | 0.03 | or reduces | FNR | by at | least 0.05 |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | ---- | ---------- | --- | ----- | ---------- |
trainingfoldispassedtoadetector.ForLSTM-AE,preserving
|     |     |     |     |     |     |     |     | relative | to its | default | slice. | Only PCA | and | SVM | cross this |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | ------ | -------- | --- | --- | ---------- |
orderavoidsconstructingwindowsfromunrelatedtimepoints promotion threshold; other classical detectors retain default
| and prevents | a   | window | from | crossing | the | boundary | between |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | ---- | -------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ornear-defaultconfigurations.Thisconservativepolicyavoids
| the normal | training | sequence |     | and the | attack | period. |     |           |       |       |             |     |     |            |        |
| ---------- | -------- | -------- | --- | ------- | ------ | ------- | --- | --------- | ----- | ----- | ----------- | --- | --- | ---------- | ------ |
|            |          |          |     |         |        |         |     | tailoring | every | model | extensively | to  | one | benchmark, | but it |
The two protocols consequently use different units of eval- also means that the reported ordering is configuration-level
| uation. | A pointwise |     | model | assigns | one | score | to one 44- |     |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ----- | ------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
evidenceratherthanadefinitivecomparisonofoptimallytuned
| dimensional | observation. |     | LSTM-AE |     | assigns | reconstruction |     | families. |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ------- | --- | ------- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
errorstooverlappingwindowsandlabelsawindowanomalous
|         |       |              |     |           |         |     |           | The neural | models           |     | receive | staged     | searches | because | archi-     |
| ------- | ----- | ------------ | --- | --------- | ------- | --- | --------- | ---------- | ---------------- | --- | ------- | ---------- | -------- | ------- | ---------- |
| when at | least | one included |     | time step | belongs | to  | an attack |            |                  |     |         |            |          |         |            |
|         |       |              |     |           |         |     |           | tecture    | and optimization |     | choices | materially |          | affect  | their per- |
interval. We report this distinction because it affects both formance. AE is evaluated over 426 configurations spanning
| the number | of  | evaluated | instances |     | and | the meaning | of  | a             |            |     |                 |     |            |     |           |
| ---------- | --- | --------- | --------- | --- | --- | ----------- | --- | ------------- | ---------- | --- | --------------- | --- | ---------- | --- | --------- |
|            |     |           |           |     |     |             |     | architecture, | optimizer, |     | regularization, |     | threshold, |     | and scal- |
false negative. Cross-family comparisons remain useful at the ing choices. LSTM-AE is evaluated over 216 configurations
| implemented-configuration |     |               | level,       | but                 | should | not be          | read as | if                |                     |           |     |                  |          |                |             |
| ------------------------- | --- | ------------- | ------------ | ------------------- | ------ | --------------- | ------- | ----------------- | ------------------- | --------- | --- | ---------------- | -------- | -------------- | ----------- |
|                           |     |               |              |                     |        |                 |         | spanning          | sequence            | length,   |     | hidden capacity, |          | and training   | set-        |
| every detector            |     | received      | an identical | sample              |        | representation. |         |                   |                     |           |     |                  |          |                |             |
|                           |     |               |              |                     |        |                 |         | tings. Final      | candidates          |           | are | re-ranked        | over     | three          | seeds using |
|                           |     |               |              |                     |        |                 |         | a validation-only |                     | composite |     | of clean         | F1-score | and            | F1-score    |
| B. Detectors,             |     | Thresholding, |              | and Reproducibility |        |                 |         |                   |                     |           |     |                  |          |                |             |
|                           |     |               |              |                     |        |                 |         | under 10%         | similarity-targeted |           |     | injection.       | All      | hyperparameter |             |
The retained models are Isolation Forest (IForest), One- screening, staged selection, and multi-seed re-ranking use
Class SVM, Local Outlier Factor (LOF), Cluster-Based Lo- validation performance only; the held-out test set is accessed
cal Outlier Factor (CBLOF), KNN, Histogram-Based Out- only after selecting the final configuration. Table IV records
lier Score (HBOS), PCA, Minimum Covariance Determinant the resulting policy and configurations.
(MCD), Angle-Based Outlier Detection (ABOD), a feedfor- Both neural models minimize mean-squared reconstruction
ward autoencoder (AE), and LSTM-AE [29]–[39]. Classical error, use gradient clipping at 1.0, and apply early stopping
detectors use PyOD; neural detectors use PyTorch. PCA and withpatience15.AEpermitsupto100epochsandLSTM-AE
SVM are tuned, while other classical models use default or up to 30. The LSTM-AE search also exposes an interaction
near-default configurations. AE and LSTM-AE use staged that a one-factor sweep would miss: W = 30 and hidden
hyperparameter searches with multi-seed confirmation. size 256 are not the strongest isolated changes, but their joint

TABLEIII
DETECTORFAMILIES,SCORINGMECHANISMS,RETAINEDCONFIGURATIONS,ANDTRAININGINPUTSUSEDINTHECOMPARATIVEBENCHMARK.
CLASSICALDETECTORSUSEPYODANDNEURALDETECTORSUSEPYTORCH,ASDESCRIBEDINTHETEXT.
Modelandfamily Scoringmechanism Retainedconfiguration Traininginput
IForest Average path length in random 100trees;treesubsample256;contamination0.05;seed-controlledinitial- Fullnormalpool
|     | Treeensemble |     | isolationtrees |     |     | ization |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | -------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SVM RBFν-SVMsupportboundary, RBFone-classSVM;ν=0.01;gamma = scale;contamination0.05 50Ksubsample
|     | Kernelboundary |     | ν=0.01 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LOF Density ratio relative to a 20- Noveltymode;20neighbors;Minkowskidistance;contamination0.05 50Ksubsample
|     | Localdensity |     | neighborneighborhood |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CBLOF Clusterassignment,clustersize, Eightclusters;α=0.9;β=5;seed-controlledinitialization Fullnormalpool
|     | Cluster/density |     | anddistance |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
KNN Distance to the fifth-nearest Fifth-nearest-neighbordistance;largest-distancescore;Minkowskimetric 50Ksubsample
|     | Distance |     | trainingpoint |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
HBOS Feature-wise histogram outlier 10bins;α=0.1;tolerance0.5;feature-wisehistogramscoring Fullnormalpool
|     | Statistical |     | scores |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PCA Reconstructionerrorat90%re- 90%retainedvariance;reconstruction-errorscoring;seed-controlledinitial- Fullnormalpool
|     | Linearsubspace |     | tainedvariance |     |     | ization |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | -------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MCD Robust Mahalanobis distance Defaultsupportfraction;robustcovarianceandMahalanobis-distancescor- 50Ksubsample
|     | Robustcovariance |     | fromatrimmedcenter |     |     | ing |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ABOD Angle variance with 10 neigh- Fastvariant;10neighbors;angle-variancescoring 50Ksubsample
|     | Geometric |     | bors |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dimensions[256,128,64];BatchNorm,LeakyReLU,dropout0.1;Adam
|     | AE              |     | Bottleneckreconstructionerror |     |     |                                       |     |     |     |     |     |     | Fullnormalpool |     |     |
| --- | --------------- | --- | ----------------------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
|     | Neuralpointwise |     |                               |     |     | 5×10−4;batch2048;MSE;maximum100epochs |     |     |     |     |     |     |                |     |     |
LSTM-AE Sequence reconstruction error One 256-unit LSTM layer; W = 30; AdamW 10−3; batch 256; MSE; Fullsequenceset
|     |                |     | overW | =30 |     |                 |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ----- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Neuralsequence |     |       |     |     | maximum30epochs |     |     |     |     |     |     |     |     |     |
TABLEIV making contamination-degradation analysis ill-posed [40]. Its
TUNINGPOLICYANDFINALMODEL-CONFIGURATIONSUMMARY. available baseline also showed severe precision collapse (F1
=0.2013,precision=0.1130,recall=0.9218)anda2011.4-
|     | Group | Searchpolicy |     | Retainedconfiguration |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | ------------ | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Classical Sensitivity-first; only PCA: 90% variance; SVM: RBF, s training time; no SOD contamination result is included in
PCA and SVM ν=0.01 themainanalysis.Allreportedcomparativeanalysestherefore
promoted
|     | AE  | 426 staged        | configura- | [256,128,64], |      | LeakyReLU, |       | use 429   | retained | runs.           |     |     |              |      |      |
| --- | --- | ----------------- | ---------- | ------------- | ---- | ---------- | ----- | --------- | -------- | --------------- | --- | --- | ------------ | ---- | ---- |
|     |     | tions; multi-seed | confir-    | dropout       | 0.1, | Adam 5 ×   | 10−4, |           |          |                 |     |     |              |      |      |
|     |     |                   |            |               |      |            |       | For every | clean    | or contaminated |     |     | model within | each | seed |
|     |     | mation            |            | batch2048     |      |            |       |           |          |                 |     |     |              |      |      |
LSTM-AE 216 staged W = 30, hidden size 256, anddetectorconfiguration,anewthresholdiscalibratedusing
|     |     | configurations; |     | joint AdamW10−3,batch256 |     |     |     |          |      |               |            |     |             |           |     |
| --- | --- | --------------- | --- | ------------------------ | --- | --- | --- | -------- | ---- | ------------- | ---------- | --- | ----------- | --------- | --- |
|     |     |                 |     |                          |     |     |     | only the | same | clean labeled | validation |     | split. That | threshold | is  |
sequence/capacity
thenfrozenforthecorrespondingheld-outtestevaluation.This
search
preventstest-setoptimizationandmeasureswhethereachcon-
|               |        |               |                 |              |            |          |             | taminated    | model’s | anomaly-score |         | distribution |         | remains      | com- |
| ------------- | ------ | ------------- | --------------- | ------------ | ---------- | -------- | ----------- | ------------ | ------- | ------------- | ------- | ------------ | ------- | ------------ | ---- |
| configuration |        | ranks highest |                 | after staged | multi-seed |          | evaluation. |              |         |               |         |              |         |              |      |
|               |        |               |                 |              |            |          |             | patible with | an      | operating     | point   | selected     | without | contaminated |      |
| Dropout       | values | are           | not interpreted |              | for the    | selected | single-     |              |         |               |         |              |         |              |      |
|               |        |               |                 |              |            |          |             | calibration  | data.   | Precision,    | recall, | F1-score,    | FNR,    | ROC-AUC,     |      |
layer LSTM because PyTorch applies recurrent dropout only and average precision are retained in the experiment outputs;
| between | stacked | recurrent | layers. |     |     |     |     |        |         |            |         |     |            |          |     |
| ------- | ------- | --------- | ------- | --- | --- | --- | --- | ------ | ------- | ---------- | ------- | --- | ---------- | -------- | --- |
|         |         |           |         |     |     |     |     | F1 and | FNR are | emphasized | because |     | the former | balances | the |
Experiments were run on the Narval cluster of the Digital two error directions while the latter directly exposes missed
| Research | Alliance | of  | Canada. | Classical | jobs | used | six Intel | attacks. |     |     |     |     |     |     |     |
| -------- | -------- | --- | ------- | --------- | ---- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
XeonCPUcoresand48GiBofRAM;neuraljobsadditionally
| used            | one NVIDIA |               | A100-SXM4-40 |     | GB              | GPU. Fixed     | seeds    |          |             |     | V. RESULTS    |     |            |     |     |
| --------------- | ---------- | ------------- | ------------ | --- | --------------- | -------------- | -------- | -------- | ----------- | --- | ------------- | --- | ---------- | --- | --- |
| 42,             | 123, and   | 456           | are applied  | to  | splitting,      | contamination, |          |          |             |     |               |     |            |     |     |
|                 |            |               |              |     |                 |                |          | A. Clean | Performance | and | Contamination |     | Robustness |     |     |
| initialization, |            | and training. | Each         | run | is checkpointed |                | indepen- |          |             |     |               |     |            |     |     |
dentlybeforeaggregation,supportingrestartableexecutionand Table V combines clean performance, measured training
consistent generation of the reported tables and figures. cost, and worst-case F1 loss. LSTM-AE has the highest clean
All detectors output continuous anomaly scores. An F1- F1-score (0.8813), followed by LOF, ABOD, and AE. Yet the
oriented threshold is selected on validation data and applied clean-data ranking changes substantially under contamination.
unchanged to held-out test data. The primary metric is F1- LOF, KNN, and ABOD each lose more than 0.64 F1 in
score; FNR is reported because missed attacks are safety- their worst condition, while IForest, HBOS, PCA, and SVM
relevant.Experimentsuseseeds42,123,and456andtraining- remain within 0.068 of their clean baselines. AE and LSTM-
pool-relative budgets of 1%, 3%, 5%, and 10%. Execution AE occupy an intermediate position.
produced 430 successful runs: 33 retained clean baselines, The clean scores are descriptive means over three seeds
396 retained contamination runs, and one SOD clean baseline rather than significance-tested orderings. The leading group
used only to document exclusion. SOD was removed from is narrow: LSTM-AE, LOF, ABOD, and AE all lie between
the main benchmark because its clean ROC-AUC indicated 0.867 and 0.881. PCA and SVM are mid-table at approxi-
inverted score ordering under the evaluated configuration, mately 0.813–0.814, but require far less training time than

ABOD, KNN, AE, or LSTM-AE. Clean evaluation therefore injection. Its response to similarity-targeted injection is much
defines the starting point for robustness analysis but does not milder through 5%, indicating that the centroid-based point-
identify a single operational winner. wise selection rule does not transfer directly into a worst-
The standard deviations also distinguish stable clean es- case sequence attack. The neural results therefore support an
timates from seed-sensitive ones. Most detectors vary by intermediate robustness interpretation and demonstrate why
less than 0.01 F1 across the three seeds, whereas LOF and attack-family labels should not be treated as equivalent across
MCD vary more noticeably because their fitting pools are data representations.
subsampled. These differences are small relative to the largest Figure3complementstheF1analysiswithmissed-detection
contamination losses, but they reinforce why degradation is behavior and is discussed in Section V-C. In Figs. 2–4,
computed from seed-averaged contaminated and clean scores the labels HISTOGRAM, CLUSTER, and AUTOENCODER
rather than from a single favorable run. denote HBOS, CBLOF, and AE, respectively; axes labeled
| Figure | 2 shows distinct | attack | responses. |     | Feature noise | at             |              |     |                     |        | p   |
| ------ | ---------------- | ------ | ---------- | --- | ------------- | -------------- | ------------ | --- | ------------------- | ------ | --- |
|        |                  |        |            |     |               | “contamination | rate” report | the | clean-pool-relative | budget |     |
σ =0.15changeslittle,whereas1%randominjectionreduces defined in Section III-B.
LOF, KNN, ABOD, and LSTM-AE from 0.876, 0.848, 0.874, The heatmap in Fig. 4 makes the model dependence ex-
and0.881toapproximately0.398,0.335,0.305,and0.440.AE plicit. IForest, HBOS, PCA, and SVM remain close to their
degrades progressively; similarity-targeted injection becomes clean values. Random injection sharply harms LOF, KNN,
severe for selected distance- and density-based detectors at ABOD, and LSTM-AE across budgets, whereas AE degrades
10%. moregradually.Similarity-targetedinjectionproducesdelayed
The earliest failures are operationally important because a failures for LOF, KNN, and ABOD. These results show why
small clean-pool-relative budget is sufficient to reverse the a clean-only leaderboard is inadequate for adversarial model
| clean ranking. | LOF, KNN, | and | ABOD | begin | among the | five selection. |     |     |     |     |     |
| -------------- | --------- | --- | ---- | ----- | --------- | --------------- | --- | --- | --- | --- | --- |
strongestcleanconfigurations,yetat1%randominjectioneach
|     |     |     |     |     |     | B. Attack-Type | Comparison |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | ---------- | --- | --- | --- | --- |
losesmorethanhalfofitsoriginalF1-score.Theirrelianceon
local neighborhoods, distances, or angles makes them sensi- Thethreestrategiesproducequalitativelydifferentdegrada-
tive when attack samples are incorporated into the reference tionpatterns.Randominjectionisthedominantfamilyoverall:
|           |              |          |            |                 |     | it causes | the earliest large | drops | and affects | both pointwise |     |
| --------- | ------------ | -------- | ---------- | --------------- | --- | --------- | ------------------ | ----- | ----------- | -------------- | --- |
| geometry. | In contrast, | the more | aggregated | representations |     | of        |                    |       |             |                |     |
PCA, HBOS, IForest, and SVM change much less under the neighborhood methods and the sequence model. Because the
|                |                |     |     |     |     | injected samples | span | the available | attack | pool rather | than |
| -------------- | -------------- | --- | --- | --- | --- | ---------------- | ---- | ------------- | ------ | ----------- | ---- |
| same evaluated | contamination. |     |     |     |     |                  |      |               |        |             |      |
The neural response is neither uniformly fragile nor uni- onlyitscenter-nearestregion,theyintroducediversemalicious
formly robust. AE deteriorates gradually and reaches its statesintothenormalreferencedata.Thispatternisconsistent
|                 |        |        |            |       |          | with an expansion | or distortion | of  | the learned | nominal region |     |
| --------------- | ------ | ------ | ---------- | ----- | -------- | ----------------- | ------------- | --- | ----------- | -------------- | --- |
| worst condition | at 10% | random | injection, | where | F1 falls | to                |               |     |             |                |     |
approximately 0.566. LSTM-AE has the highest clean F1- for detectors whose scores depend strongly on the training
geometry.
| score but | drops to approximately |     | 0.440 | at only | 1% random |     |     |     |     |     |     |
| --------- | ---------------------- | --- | ----- | ------- | --------- | --- | --- | --- | --- | --- | --- |
Fig.2. F1-scoreversustraining-pool-relativecontaminationbudget.Injection Fig.3. FNRversustraining-pool-relativecontaminationbudget.LOF,KNN,
attackscausedetector-specificdegradation;featurenoisehasalimitedeffect ABOD, and LSTM-AE enter the highest missed-detection region under one
| atthetestedmagnitude. |     |     |     |     |     | ormoreinjectionsettings. |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |

TABLEV
CLEANPERFORMANCE(MEAN±SDOVERTHREESEEDS),MEANOBSERVEDTRAININGTIME,ANDWORST-CASEF1DROPACROSSTWELVE
ATTACK-BUDGETCOMBINATIONS.WORST-CASEDROPISCOMPUTEDFROMSEED-AVERAGEDF1VALUES.
|     |     |     | Detector |               | CleanF1 |               | CleanFNR | Train(s) | WorstF1drop |     |     |     |     |     |
| --- | --- | --- | -------- | ------------- | ------- | ------------- | -------- | -------- | ----------- | --- | --- | --- | --- | --- |
|     |     |     | LSTM-AE  | 0.8813±0.0032 |         | 0.2027±0.0068 |          | 139.9    | 0.442       |     |     |     |     |     |
|     |     |     | LOF      | 0.8761±0.0208 |         | 0.1373±0.0312 |          | 36.5     | 0.660       |     |     |     |     |     |
|     |     |     | ABOD     | 0.8744±0.0039 |         | 0.2012±0.0171 |          | 249.8    | 0.674       |     |     |     |     |     |
|     |     |     | AE       | 0.8674±0.0029 |         | 0.2030±0.0082 |          | 117.1    | 0.302       |     |     |     |     |     |
|     |     |     | KNN      | 0.8482±0.0016 |         | 0.2259±0.0077 |          | 264.2    | 0.648       |     |     |     |     |     |
|     |     |     | SVM      | 0.8144±0.0019 |         | 0.2922±0.0015 |          | 17.1     | 0.068       |     |     |     |     |     |
|     |     |     | PCA      | 0.8134±0.0038 |         | 0.3078±0.0054 |          | 1.5      | 0.045       |     |     |     |     |     |
|     |     |     | HBOS     | 0.7712±0.0037 |         | 0.3425±0.0088 |          | 4.1      | 0.007       |     |     |     |     |     |
|     |     |     | CBLOF    | 0.7543±0.0048 |         | 0.3874±0.0034 |          | 6.9      | 0.182       |     |     |     |     |     |
|     |     |     | IForest  | 0.7331±0.0022 |         | 0.4162±0.0036 |          | 4.5      | 0.000       |     |     |     |     |     |
|     |     |     | MCD      | 0.7260±0.0129 |         | 0.3211±0.0559 |          | 6.2      | 0.126       |     |     |     |     |     |
Fig.4. ChangeinF1-scorerelativetothecleanbaseline.Stableclassicalmodelsremainnearzero,whileinjectionattacksexposeseverefragilityinseveral
high-clean-F1detectors.
Similarity-targeted injection is more detector-dependent. At C. Safety, Cost, and Practical Trade-offs
lowbudgetsitisoftenlessharmfulthanrandominjection,but
|           |          |      |         |          |     |            | Figure | 3 shows | that | FNR | should be | interpreted |     | together |
| --------- | -------- | ---- | ------- | -------- | --- | ---------- | ------ | ------- | ---- | --- | --------- | ----------- | --- | -------- |
| LOF, KNN, | and ABOD | show | delayed | failures | as  | the budget |        |         |      |     |           |             |     |          |
withF1-scoreratherthaninisolation.ABOD,KNN,andLOF
| increases. | The centroid  | rule    | selects   | attack | samples    | that are   |          |               |         |         |             |     |                  |     |
| ---------- | ------------- | ------- | --------- | ------ | ---------- | ---------- | -------- | ------------- | ------- | ------- | ----------- | --- | ---------------- | --- |
|            |               |         |           |        |            |            | exceed   | approximately | 0.70    | FNR     | in at least | one | contamination    |     |
| globally   | close to the  | average | clean     | state, | yet global | prox-      |          |               |         |         |             |     |                  |     |
|            |               |         |           |        |            |            | setting, | while         | LSTM-AE | reaches | a lower     | but | still concerning |     |
| imity does | not guarantee | local   | proximity |        | in every   | detector’s |          |               |         |         |             |     |                  |     |
peakunderrandominjection.Bycontrast,PCA,SVM,HBOS,
representation. The strategy should therefore be viewed as a AE, and MCD remain in the lower-FNR group, and IForest
| repeatable | stealth-oriented |               | heuristic. | It does | not establish | that      |       |                    |        |         |           |       |           |         |
| ---------- | ---------------- | ------------- | ---------- | ------- | ------------- | --------- | ----- | ------------------ | ------ | ------- | --------- | ----- | --------- | ------- |
|            |                  |               |            |         |               |           | stays | comparatively      | stable | despite | its lower | clean | baseline. |         |
| random     | sampling is      | intrinsically | stronger   |         | than an       | optimized |       |                    |        |         |           |       |           |         |
|            |                  |               |            |         |               |           | At    | some contamination |        | rates,  | a lower   | FNR   | may       | reflect |
targeted attack.
|     |     |     |     |     |     |     | overly     | permissive | decision | behavior,  | which |      | reduces | missed |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------- | ---------- | ----- | ---- | ------- | ------ |
|     |     |     |     |     |     |     | detections | at the     | cost of  | precision. | For   | that | reason, | FNR is |
mostinformativewhenreadtogetherwithF1-scoreratherthan
|               |             |         |               |                 |             |          | as a       | standalone | safety measure. |        |              |             |     |     |
| ------------- | ----------- | ------- | ------------- | --------------- | ----------- | -------- | ---------- | ---------- | --------------- | ------ | ------------ | ----------- | --- | --- |
| Feature-noise | injection   | remains | close         | to              | the clean   | baseline |            |            |                 |        |              |             |     |     |
| across the    | grid. Three | aspects | limit         | the conclusion: |             | the mag- |            |            |                 |        |              |             |     |     |
|               |             |         |               |                 |             |          | D. Overall | Trade-offs |                 | Across | Performance, | Robustness, |     | and |
| nitude is     | fixed at σ  | = 0.15, | perturbations |                 | are clipped | to the   |            |            |                 |        |              |             |     |     |
Cost
| normalized | range, and | only | selected | normal | observations | are |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ---- | -------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
modified. The result shows that the evaluated models tolerate Taken together, the results show that the ordering by clean-
this bounded configuration substantially better than attack- dataF1-scoreismateriallydifferentfromtheorderingimplied
sampleinjection.Itdoesnotshowgeneralrobustnesstobiased, by robustnessand trainingcost. LSTM-AE, LOF,ABOD, and
coordinated, temporally persistent, or physically constrained AE form the strongest clean-data group. However, several of
sensor corruption. these models remain fragile once the normal training pool

is contaminated, particularly LOF, KNN, and ABOD, and to explicitlyaccountforcontamination.Futureworkshouldeval-
a lesser but still meaningful degree AE and LSTM-AE. By uate additional ICS environments, stronger adaptive attacks,
contrast, PCA and SVM do not lead the clean baseline table, and defenses that jointly optimize accuracy, robustness, and
yet both combine moderate clean performance with small operational cost.
worst-case F1 loss and much lower training cost. IForest is
also notable for its stability across the contamination grid,
REFERENCES
although its clean baseline remains lower than that of PCA [1] J. Goh, S. Adepu, M. Tan, and Z. S. Lee, “Anomaly detection in
and SVM. cyberphysicalsystemsusingrecurrentneuralnetworks,”in2017IEEE
18thInternationalSymposiumonHighAssuranceSystemsEngineering
The most defensible practical conclusion is therefore not
(HASE),2017,pp.140–145.
that one detector dominates on every metric, but that PCA [2] A. M. Y. Koay, R. K. L. Ko, H. Hettema, and K. Radke, “Machine
and SVM provide a favorable observed balance among clean learning in industrial control system security: Current landscape, op-
portunitiesandchallenges,”JournalofIntelligentInformationSystems,
performance, contamination robustness, safety-relevant FNR
vol.60,pp.377–405,2023.
behavior, and computational cost under the evaluated setup. [3] G. R. M. R., C. M. Ahmed, and A. Mathur, “Machine learning for
Because hardware and training scales differ, this balance intrusiondetectioninindustrialcontrolsystems:Challengesandlessons
fromexperimentalevaluation,”Cybersecurity,vol.4,no.1,p.27,2021.
is configuration-specific rather than a formal multi-objective
[4] B. I. P. Rubinstein, B. Nelson, L. Huang, A. D. Joseph, S. hon Lau,
ranking. AE and LSTM-AE remain intermediate rather than S. Rao, N. Taft, and J. D. Tygar, “ANTIDOTE: Understanding and
robust, and their contamination-time behavior is less depend- defending against poisoning of anomaly detectors,” in Proceedings of
the 9th ACM SIGCOMM Conference on Internet Measurement (IMC),
able than that of the most stable classical configurations.
2009,pp.1–14.
[5] A. E. Cina`, K. Grosse, A. Demontis, S. Vascon, W. Zellinger, B. A.
E. Limitations Moser, A. Oprea, B. Biggio, M. Pelillo, and F. Roli, “Wild patterns
reloaded: A survey of machine learning security against training data
Severallimitationsshouldbekeptinmindwheninterpreting poisoning,”ACMComputingSurveys,vol.55,no.13s,pp.1–39,2023.
the benchmark. First, the study is conducted on a single [6] M. Kravchik and A. Shabtai, “Detecting cyber attacks in industrial
control systems using convolutional neural networks,” in Proceedings
ICS dataset, so the findings should be interpreted at the
ofthe2018WorkshoponCyber-PhysicalSystemsSecurityandPrivaCy
benchmark level rather than as population-wide claims about (CPS-SPC),2018,pp.72–83.
all safety-critical ICS environments. Second, the evaluated [7] J. Inoue, Y. Yamagata, Y. Chen, C. M. Poskitt, and J. Sun, “Anomaly
detection for a water treatment system using unsupervised machine
attackfamiliesarecontamination-styletraining-timescenarios
learning,” in 2017 IEEE International Conference on Data Mining
rather than optimization-based worst-case poisoning attacks. Workshops(ICDMW),2017,pp.1058–1065.
Third, the benchmark assumes clean validation and test splits, [8] J.Kim,J.Yun,andH.C.Kim,“Anomalydetectionforindustrialcontrol
systems using sequence-to-sequence neural networks,” in Computer
which isolates training-time contamination effects but may
Security, ser. Lecture Notes in Computer Science. Springer, 2020,
be optimistic relative to workflows in which curation errors vol.11980,pp.3–18.
propagate beyond the training data. Fourth, the benchmark [9] M.KravchikandA.Shabtai,“Efficientcyberattackdetectioninindus-
trialcontrolsystemsusinglightweightneuralnetworksandPCA,”IEEE
does not apply equally deep hyperparameter optimization
TransactionsonDependableandSecureComputing,vol.19,no.4,pp.
to every detector, so cross-detector comparisons should be 2179–2197,2022.
interpreted as configuration-level robustness evidence rather [10] G.Zizzo,C.Hankin,S.Maffeis,andK.Jones,“Adversarialattackson
time-series intrusion detection for industrial control systems,” in 2020
than definitive family-level rankings. Finally, the pointwise
IEEE 19th International Conference on Trust, Security and Privacy in
detectors and sequence model use different split structures: ComputingandCommunications(TrustCom),2020,pp.899–910.
the pointwise random split can place temporally adjacent [11] A.Erba,R.Taormina,S.Galelli,M.Pogliani,M.Carminati,S.Zanero,
and N. O. Tippenhauer, “Constrained concealment attacks against
observations in different folds, whereas LSTM-AE preserves
reconstruction-based anomaly detectors in industrial control systems,”
acontiguousprotocol.Thelimitedfeature-noiseeffectapplies in Proceedings of the 36th Annual Computer Security Applications
only at σ =0.15. Conference, ser. ACSAC ’20. New York, NY, USA: Association
for Computing Machinery, 2020, pp. 480–495. [Online]. Available:
https://doi.org/10.1145/3427228.3427660
VI. CONCLUSION [12] E.Anthi,L.Williams,M.Rhode,P.Burnap,andA.Wedgbury,“Adver-
sarial attacks on machine learning cybersecurity defences in industrial
Thispapercomparedelevenanomalydetectorsunderoffline control systems,” Journal of Information Security and Applications,
training-time contamination on SWaT. Across three attack vol.58,p.102717,2021.
[13] M. Kravchik, B. Biggio, and A. Shabtai, “Poisoning attacks on cyber
families and four budgets, strong clean performance did not
attack detectors for industrial control systems,” in Proceedings of the
imply robustness. LOF, KNN, and ABOD ranked near the top 36thAnnualACMSymposiumonAppliedComputing(SAC),2021,pp.
on clean data but degraded most severely after attack-sample 116–125.
[14] M. Kravchik, L. Demetrio, B. Biggio, and A. Shabtai, “Practical
injection. AE and LSTM-AE showed intermediate robustness,
evaluationofpoisoningattacksononlineanomalydetectorsinindustrial
with random injection as the dominant neural failure mode. controlsystems,”Computers&Security,vol.122,p.102901,2022.
PCA, SVM, HBOS, and IForest were comparatively stable; [15] A.P.MathurandN.O.Tippenhauer,“SWaT:Awatertreatmenttestbed
for research and training on ics security,” in Proceedings of the 2016
PCA and SVM balanced clean performance, robustness, and
International Workshop on Cyber-physical Systems for Smart Water
cost under the evaluated protocols. Feature noise had limited Networks(CySWater),2016,pp.31–36.
impact at the tested magnitude, whereas injection was more [16] J.Goh,S.Adepu,K.N.Junejo,andA.Mathur,“Adatasettosupport
research in the design of secure water treatment systems,” in Critical
consequential. These findings motivate integrity controls for
Information Infrastructures Security, ser. Lecture Notes in Computer
offline ICS training data and model selection procedures that Science. Springer,2017,vol.10242,pp.88–99.

[17] A´. L. P. Go´mez, L. F. Maimo´, A. H. Celdra´n, and F. J. G. Clemente, namic stealthy backdoor attack against anomaly detectors in industrial
“MADICS:Amethodologyforanomalydetectioninindustrialcontrol controlsystems,”InformationSciences,vol.735,p.123066,2026.
systems,”Symmetry,vol.12,no.10,p.1583,2020. [29] F.T.Liu,K.M.Ting,andZ.-H.Zhou,“Isolationforest,”in2008Eighth
[18] G.O.Campos,A.Zimek,J.Sander,R.J.G.B.Campello,B.Micenkova´, IEEEInternationalConferenceonDataMining,2008,pp.413–422.
E. Schubert, I. Assent, and M. E. Houle, “On the evaluation of unsu- [30] B. Scho¨lkopf, J. C. Platt, J. Shawe-Taylor, A. J. Smola, and R. C.
pervisedoutlierdetection:Measures,datasets,andanempiricalstudy,” Williamson,“Estimatingthesupportofahigh-dimensionaldistribution,”
Data Mining and Knowledge Discovery, vol. 30, no. 4, pp. 891–927, NeuralComputation,vol.13,no.7,pp.1443–1471,2001.
2016. [31] M.M.Breunig,H.-P.Kriegel,R.T.Ng,andJ.Sander,“LOF:Identifying
[19] S. Schmidl, P. Wenig, and T. Papenbrock, “Anomaly detection in density-basedlocaloutliers,”inProceedingsofthe2000ACMSIGMOD
time series: A comprehensive evaluation,” Proceedings of the VLDB InternationalConferenceonManagementofData,2000,pp.93–104.
Endowment,vol.15,no.9,pp.1779–1797,2022. [32] Z.He,X.Xu,andS.Deng,“Discoveringcluster-basedlocaloutliers,”
[20] P.Wenig,S.Schmidl,andT.Papenbrock,“Timeeval:Abenchmarking PatternRecognitionLetters,vol.24,no.9–10,pp.1641–1650,2003.
toolkitfortimeseriesanomalydetectionalgorithms,”Proceedingsofthe [33] S. Ramaswamy, R. Rastogi, and K. Shim, “Efficient algorithms for
VLDBEndowment,vol.15,no.12,pp.3678–3681,2022. miningoutliersfromlargedatasets,”inProceedingsofthe2000ACM
[21] S.Kim,K.Choi,H.-S.Choi,B.Lee,andS.Yoon,“Towardsarigorous SIGMODInternationalConferenceonManagementofData,2000,pp.
evaluationoftime-seriesanomalydetection,”inProceedingsoftheAAAI 427–438.
Conference on Artificial Intelligence, vol. 36, no. 7, 2022, pp. 7194– [34] M. Goldstein and A. Dengel, “Histogram-based outlier score (HBOS):
7201. A fast unsupervised anomaly detection algorithm,” in KI-2012: Poster
[22] A. Huet, J. M. Navarro, and D. Rossi, “Local evaluation of time andDemoTrack,2012.
seriesanomalydetectionalgorithms,”inProceedingsofthe28thACM [35] M.-L. Shyu, S.-C. Chen, K. Sarinnapakorn, and L. Chang, “A novel
SIGKDDConferenceonKnowledgeDiscoveryandDataMining,2022, anomaly detection scheme based on principal component classifier,”
pp.635–645. in Proceedings of the IEEE Foundations and New Directions of Data
[23] B.Biggio,B.Nelson,andP.Laskov,“Poisoningattacksagainstsupport MiningWorkshop,2003,pp.172–179.
vectormachines,”inProceedingsofthe29thInternationalConference [36] P.J.RousseeuwandK.V.Driessen,“Afastalgorithmfortheminimum
onMachineLearning(ICML),2012,pp.1467–1474. covariance determinant estimator,” Technometrics, vol. 41, no. 3, pp.
[24] L.Mun˜oz-Gonza´lez,B.Biggio,A.Demontis,A.Paudice,V.Wongras- 212–223,1999.
samee, E. C. Lupu, and F. Roli, “Towards poisoning of deep learning [37] H.-P.Kriegel,M.Schubert,andA.Zimek,“Angle-basedoutlierdetec-
algorithmswithback-gradientoptimization,”inProceedingsofthe10th tioninhigh-dimensionaldata,”inProceedingsofthe14thACMSIGKDD
ACM Workshop on Artificial Intelligence and Security (AISec), 2017, International Conference on Knowledge Discovery and Data Mining,
pp.27–38. 2008,pp.444–452.
[25] J.Steinhardt,P.W.Koh,andP.Liang,“Certifieddefensesfordatapoi- [38] M.SakuradaandT.Yairi,“Anomalydetectionusingautoencoderswith
soningattacks,”inAdvancesinNeuralInformationProcessingSystems, nonlineardimensionalityreduction,”inProceedingsoftheMLSDA2014
2017. 2ndWorkshoponMachineLearningforSensoryDataAnalysis,2014,
[26] A.Shafahi,W.R.Huang,M.Najibi,O.Suciu,C.Studer,T.Dumitras, pp.4:1–4:11.
andT.Goldstein,“Poisonfrogs!targetedclean-labelpoisoningattacks [39] T. Kieu, B. Yang, C. Guo, and C. S. Jensen, “Outlier detection for
on neural networks,” in Advances in Neural Information Processing timeserieswithrecurrentautoencoderensembles,”inProceedingsofthe
Systems,2018. Twenty-EighthInternationalJointConferenceonArtificialIntelligence,
[27] S. Abedzadeh and S. Bhattacharjee, “Mitigating impact of data poi- 2019,pp.2725–2732.
soning attacks on CPS anomaly detection with provable guarantees,” [40] H.-P.Kriegel,P.Kro¨ger,E.Schubert,andA.Zimek,“Outlierdetection
Information,vol.16,no.6,p.428,2025. in axis-parallel subspaces of high dimensional data,” in Advances in
[28] Q.Jiang,Y.Zu,Z.Zhu,W.Zhong,Y.Xu,Z.Qian,andX.Zhang,“Dy- KnowledgeDiscoveryandDataMining,ser.LectureNotesinComputer
Science. Springer,2009,vol.5476,pp.831–838.
---- END DOCUMENT ----
