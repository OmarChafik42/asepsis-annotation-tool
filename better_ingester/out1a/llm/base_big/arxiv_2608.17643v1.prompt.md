Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
|     |     | Empirical | mode     | decomposition |     | and   | interpretable  |     |      |
| --- | --- | --------- | -------- | ------------- | --- | ----- | -------------- | --- | ---- |
|     |     | machine   | learning | for preterm   |     | birth | classification |     | from |
electrohysterography
Umesha Tilakarathna1,2(cid:89), Senith Jayakody1,2(cid:89),*, Kalana Jayasooriya1, Roshan
|     |     | Godaliyadda1,3, |           | Ekanayake1,3, |       | Nawinne4, |          | Rathnayake5 |     |
| --- | --- | --------------- | --------- | ------------- | ----- | --------- | -------- | ----------- | --- |
|     |     |                 | Parakrama |               | Isuru |           | Chathura |             |     |
1 Multidisciplinary AI Research Centre, University of Peradeniya, Peradeniya 20400, Sri
Lanka
|     |     | 2 Farbe | Technologies | (Pvt) Ltd, Peradeniya |     | 20400, Sri | Lanka |     |     |
| --- | --- | ------- | ------------ | --------------------- | --- | ---------- | ----- | --- | --- |
6202 guA 81  ]PS.ssee[  1v34671.8062:viXra
3 Department of Electrical and Electronic Engineering, University of Peradeniya,
|     |     | Peradeniya | 20400, | Sri Lanka |     |     |     |     |     |
| --- | --- | ---------- | ------ | --------- | --- | --- | --- | --- | --- |
4 Department of Computer Engineering, University of Peradeniya, Peradeniya 20400,
Sri Lanka
5 Department of Obstetrics and Gynaecology, University of Peradeniya, Peradeniya
|     |     | 20400, Sri    | Lanka               |         |         |       |     |     |     |
| --- | --- | ------------- | ------------------- | ------- | ------- | ----- | --- | --- | --- |
|     |     | (cid:89)These | authors contributed | equally | to this | work. |     |     |     |
* senith@eng.pdn.ac.lk
Abstract
Preterm birth (PTB) remains a major global health problem, and reliable non-invasive
risk assessment remains difficult. Electrohysterography (EHG) records uterine electrical
activity from the maternal abdomen and is a candidate modality for PTB assessment,
but reported performance on public EHG datasets varies widely and can be inflated
when segments from the same recording are divided between training and validation
folds. This study used empirical mode decomposition (EMD) to derive signal-adaptive
oscillatory representations of filtered EHG signals before feature extraction, with the
aim of evaluating term-versus-preterm classification. In a retrospective secondary
analysis of 26 recordings, 13 preterm and 13 term, from the public 2018 Term-Preterm
EHG Dataset with Tocogram, we compared dataset-provided annotated intervals with
non-overlapping fixed 3-minute windows and evaluated the first four IMFs. Fourteen
features spanning burst/peak morphology, temporal-energy descriptors, and entropy
were extracted from each of three EHG channels, producing 42 features per segment,
and evaluated using nine classifiers under repeated five-fold recording-grouped
cross-validation with recording-level aggregation. IMF1 achieved the strongest mean
performance among the evaluated modes. With fixed 3-minute IMF1 features, Random
Forest achieved mean accuracy of 0.8308, F1 of 0.7969, balanced accuracy of 0.8308,
MCC of 0.6998, ROC-AUC of 0.8157, and AP of 0.8877. Relative to the same features
from the filtered time-domain signal, IMF1 yielded numerically higher values for all
evaluated performance metrics, including accuracy (0.7846 to 0.8308), MCC (0.6114 to
0.6998), ROC-AUC (0.8073 to 0.8157), and AP (0.8773 to 0.8877). Preterm recordings
showed smaller, more regularly spaced peak-like events, lower temporal-energy measures,
and higher entropy; temporal-energy descriptors nevertheless had the largest grouped
permutation importance. These findings support the methodological promise of
IMF1-based EHG classification, while larger independent cohorts with explicit
|        |          | participant | linkage | are required before | clinical | interpretation. |     |     |      |
| ------ | -------- | ----------- | ------- | ------------------- | -------- | --------------- | --- | --- | ---- |
| August | 19, 2026 |             |         |                     |          |                 |     |     | 1/33 |

Introduction
Preterm birth (PTB), defined as birth before 37 completed weeks of gestation, remains
a major global health problem. An estimated 13.4 million babies (approximately one in
ten live births) were born preterm in 2020 [1,2]. Although global under-five mortality
has declined substantially over recent decades, neonatal mortality has declined more
slowly than mortality among older infants and children, and neonatal deaths now
account for nearly half of all under-five deaths [3,4]. Further reductions in child
mortality therefore increasingly depend on improving outcomes around birth and during
the neonatal period. Preterm birth is central to this burden: its complications were
responsible for approximately 0.9 million deaths in 2019 and remain the leading cause of
death among children younger than five years worldwide [2]. The burden is particularly
high in low- and middle-income regions, including southern Asia and sub-Saharan
Africa, where access to timely monitoring, referral, and neonatal care may be
limited [2,3]. Together, these estimates establish PTB as a major maternal and
newborn health priority.
The impact of PTB extends beyond early mortality and includes substantial short-
andlong-termmorbidity. Infantsbornpreterm, particularlythosebornveryearly, areat
increased risk of respiratory difficulties, feeding problems, cerebral palsy, developmental
delay, vision impairment, hearing impairment, and other long-term complications [5].
These outcomes can impose lifelong consequences for the child, emotional and financial
strain on families, and substantial demands on healthcare systems. Therefore, reducing
the burden of PTB is not only a neonatal survival priority, but also a major concern in
terms of long-term morbidity, public health, socioeconomic burden, and family welfare.
Timely identification of women at increased risk of preterm delivery may enable
closer surveillance and referral. When preterm labour or delivery is clinically suspected
within an actionable gestational window, guideline-based pathways may include
administration of antenatal corticosteroids for fetal lung maturation, tocolysis when
appropriate, and neonatal transfer or care planning [6–8]. Improved risk stratification
should therefore be viewed as a potential adjunct to established clinical assessment, not
as a stand-alone diagnostic or treatment trigger.
Challenges in practical PTB risk assessment
Several approaches have been investigated or used for assessing PTB risk or suspected
preterm labour, including clinical history, obstetric risk factors, cervical length
measurement, fetal fibronectin testing, biomarker tests, uterine activity monitoring, and
imaging-based assessment. These methods provide useful clinical information, but
accurate, generalizable, and practically deployable PTB risk assessment remains
challenging. Clinical risk factors alone are often insufficient because PTB is
multifactorial and can occur in women without obvious prior risk. Cervical length
measurement and fetal fibronectin testing are clinically relevant, particularly in
symptomatic or high-risk settings, but their use depends on gestational age, clinical
presentation, measurement setting, operator expertise, and intended prediction
window [8,9]. Current guidelines therefore use these tests within well defined clinical
pathways rather than as universal screening tools [8].
Electrohysterography (EHG) records myometrial electrical activity non-invasively
using electrodes on the maternal abdomen and is closely related to uterine contractile
activity [10–12]. External tocodynamometry, by comparison, measures mechanical
deformation at the abdominal surface. EHG therefore provides a more direct view of
uterine electrophysiology and may support repeated, low-burden measurement.
However, EHG is not established as a routine tool for PTB risk stratification.
Variability in acquisition and preprocessing, limited external validation, and uncertainty
August 19, 2026 2/33

about the clinical interpretation and incremental value of EHG-derived features remain
barriers to translation [13]. These gaps motivate reproducible and physiologically
|     |     | interpretable | EHG analysis. |            |            |          |     |
| --- | --- | ------------- | ------------- | ---------- | ---------- | -------- | --- |
|     |     | Physiological | basis         | of uterine | electrical | activity |     |
The myometrium is the smooth-muscle layer of the uterus. Myometrial electrical
activity and its propagation depend on cellular excitability and intercellular coupling,
including coupling through gap junctions [14,15]. For much of pregnancy, the uterus is
relatively quiescent and myometrial electrical activity is weakly coordinated. As labour
approaches, changes in contraction-associated proteins, ion channels, receptors, and
connexin-43 gap junctions increase excitability, electrical propagation, and coordination
of contractions [15,16]. This transition is regulated through interacting endocrine,
|     |     | paracrine, | inflammatory, | and mechanical | pathways | [16,17]. |     |
| --- | --- | ---------- | ------------- | -------------- | -------- | -------- | --- |
These preparatory changes are reflected in uterine electrical activity before and
during labour. Surface uterine electromyography, recorded from the maternal abdomen
as EHG, has therefore been investigated for characterizing the transition from relative
quiescence to the electrically active labour state [16]. Increased uterine electrical
activity has been reported during both term and preterm labour [18,19], consistent with
|     |     | increased | contractile | activity. |     |     |     |
| --- | --- | --------- | ----------- | --------- | --- | --- | --- |
These observations support the hypothesis that myometrial activation associated
with labour may occur prematurely in pregnancies ending preterm and may produce
detectable changes in surface EHG. They therefore provide a physiological rationale for
evaluating EHG features related to burst morphology, temporal energy, and signal
complexity as candidate markers for retrospective term-versus-preterm classification.
Prospective studies with defined prediction horizons are required to determine whether
|     |     | such features | can support     | clinical | risk stratification. |     |     |
| --- | --- | ------------- | --------------- | -------- | -------------------- | --- | --- |
|     |     | EHG signal    | characteristics |          | and bursts           |     |     |
Surface EHG records the abdominal manifestation of myometrial electrical activity.
Although maternal tissues attenuate the signal, burst-like activity associated with
contractions remains detectable from abdominal recordings [10,12]. Much of the
spectral power associated with uterine contractions is reported below approximately 1
Hz [20]; however, this is not a physiological or analytical cutoff, because faster uterine
components may extend above 1 Hz and non-uterine sources can overlap the recorded
band. The present analysis therefore used the dataset-provided signals filtered from 0.08
to 5.0 Hz and did not impose an additional low-pass cutoff at 1 Hz or assign a
predefined frequency band to any IMF. Because EMD is signal-adaptive, the spectral
|     |     | content | of a given IMF | may vary | among segments | and recordings. |     |
| --- | --- | ------- | -------------- | -------- | -------------- | --------------- | --- |
Uterine EMG/EHG bursts are time-localized episodes of electrical activity rather
than a single frequency band. Their occurrence, morphology, internal oscillatory
content, and energy have been investigated as indicators of the transition from relative
uterine quiescence toward labour. Li et al. reported that uterine EMG burst power
increased with cervical dilation and reached higher values as labour progressed;
frequency-related parameters increased earlier, whereas power-related parameters
became stronger later in labour [21]. Buhimschi et al. similarly reported that uterine
electrical activity was minimal during much of pregnancy, but appeared as bursts that
became more frequent and larger in amplitude during term and preterm labour [12].
These labour-associated bursts correlated with contractions, patient-reported pain or
|     |     | pressure, | and changes     | in intrauterine | pressure [12]. |                     |       |
| --- | --- | --------- | --------------- | --------------- | -------------- | ------------------- | ----- |
|     |     | Evidence  | from threatened | preterm         | labour further | supports evaluating | burst |
morphology. Mas-Cabo et al. reported an increasing trend in EHG burst amplitude as
| August | 19, 2026 |     |     |     |     |     | 3/33 |
| ------ | -------- | --- | --- | --- | --- | --- | ---- |

labour approached, with representative recordings showing larger bursts among women
delivering within seven days than among those delivering later [22]. However, amplitude
alone was not a robust discriminator. Burst amplitude should therefore be evaluated
alongside event timing, organization, energy, and complexity rather than assumed to
increase uniformly in every term–preterm comparison.
Taken together, these findings support analysing EHG bursts as multicomponent
events rather than relying on a single frequency interval or amplitude measure. The 14
feature types evaluated per channel therefore describe complementary properties of the
signal: peak and burst descriptors capture event rate, spacing, amplitude, width, and
grouping; temporal-energy descriptors capture waveform variation and energy; and
entropy descriptors capture regularity and complexity. This framework allows
term–preterm separation to arise from a joint feature pattern in which different
descriptors may vary in different directions, rather than assuming that all features
increase as labour approaches.
Computational approaches and methodological pitfalls
Recent studies have applied diverse computational approaches to EHG-based
term–preterm classification, including handcrafted temporal and spectral descriptors,
selection from larger linear and nonlinear feature pools, time–frequency and entropy
representations, multichannel propagation and synchronization measures, and
deep-learning models [23–29]. These studies demonstrate the potential of EHG, but also
show that performance depends strongly on signal representation, feature construction,
classifier choice, and validation design. In many pipelines, the primary emphasis is on
selecting a high-performing feature subset or learning a predictive representation, while
the physiological meaning of the retained signal properties and their contribution to the
final model decision receive less systematic attention [30]. This limits assessment of
whether strong performance reflects plausible uterine signal characteristics or
dataset-specific structure. There is therefore value in frameworks that retain traceable
signal descriptors and examine both class-dependent feature behavior and model-level
feature-family importance.
Reported performance is also highly sensitive to data partitioning. Applying
oversampling before dividing data into training and validation sets can introduce
information leakage and produce optimistic performance estimates [31]. For segmented
biomedical signals, a separate preventable error occurs when windows or contraction
intervals from the same recording appear in both training and validation data, allowing
recording-specific structure to be shared across the split. All segments derived from one
recording should therefore be assigned exclusively to either training or validation within
each fold, and final predictions and metrics should be computed at the recording level.
Within this setting, empirical mode decomposition (EMD) is well suited to
intermittent, nonstationary EHG because it derives intrinsic mode functions (IMFs)
from the local extrema and characteristic time scales of each input signal rather than
imposing a fixed global basis or predefined frequency boundaries [32]. Fourier- and
wavelet-based analyses use predefined analysis functions and selected frequency bands
or scales, within which physiological activity and artifacts occupying the same range
may remain combined. EMD instead organizes local oscillatory content into
data-dependent modes, providing a plausible representation for extracting temporally
localized morphology, energy, and complexity descriptors. This adaptivity does not
guarantee denoising or assign a fixed physiological meaning to an IMF; the relative
usefulness of the modes must therefore be established empirically.
To retain interpretability, the extracted features were chosen to represent traceable
signal properties. Peak and burst features describe event timing, morphology, and
grouping; temporal-energy features describe waveform variation and energy; and
August 19, 2026 4/33

entropy features describe signal regularity and complexity. These descriptors may not
change in the same direction, and their relevance can be assessed at both the univariate
descriptive and multivariate model levels. Accordingly, class-dependent differences in a
feature should be interpreted alongside its contribution to the multivariate model,
rather than as evidence that the feature is independently predictive or represents a
|     |     | standalone | physiological |     | biomarker. |     |     |     |     |     |     |
| --- | --- | ---------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Study contributions
Against this background, the study makes four bounded methodological contributions:
1. Signal-adaptive representation with a matched comparator. The first
four EMD-derived IMFs are evaluated under the same feature and recording-level
classification framework, after which the selected IMF is compared with identical
features extracted from the filtered time-domain signal. This isolates the effect of
|     |     | signal | representation. |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2. Prevention of recording-level segment leakage. All segments from a
recording remain within one cross-validation fold, no oversampling is used, and
segment-level classification scores are aggregated into one recording-level score.
This addresses the direct, preventable leakage pathway created when segments
|     |     | from | one recording |     | cross the | split. |     |     |     |     |     |
| --- | --- | ---- | ------------- | --- | --------- | ------ | --- | --- | --- | --- | --- |
3. Direct comparison of segmentation strategies. Dataset-provided annotated
|     |     | intervals, | comprising |                 | contraction  |          | and dummy    | (non-contraction) |         | intervals,     | are |
| --- | --- | ---------- | ---------- | --------------- | ------------ | -------- | ------------ | ----------------- | ------- | -------------- | --- |
|     |     | compared   | with       | non-overlapping |              | fixed    | three-minute |                   | windows | under the same |     |
|     |     | framework. |            | The             | fixed-window | strategy | yields       | the               | highest | observed mean  |     |
recording-level performance among the evaluated segmentation settings, indicating
that useful classification information is not confined to annotated contractions
|     |     | while | also avoiding |     | dependence | on  | manual | interval | selection. |     |     |
| --- | --- | ----- | ------------- | --- | ---------- | --- | ------ | -------- | ---------- | --- | --- |
4. Interpretable feature-family evidence. Fourteen feature types per channel
are examined through recording-level effect directions and grouped permutation
importance. The effect directions identify a coherent preterm-associated pattern
|     |     | of more | frequent, |     | smaller, | and more | regularly | spaced | peak-like | events, lower |     |
| --- | --- | ------- | --------- | --- | -------- | -------- | --------- | ------ | --------- | ------------- | --- |
waveform magnitude/energy, and higher entropy. Temporal-energy descriptors
contribute most strongly to the selected Random Forest models, burst and peak
|     |     | descriptors |     | provide | complementary |     | information, |     | and entropy | provides little |     |
| --- | --- | ----------- | --- | ------- | ------------- | --- | ------------ | --- | ----------- | --------------- | --- |
consistent unique importance. This distinguishes descriptive feature patterns from
their contribution to model predictions, without implying that any individual
|     |     | feature | or the | proposed | multi-scale |     | organization |     | is a causal | biomarker. |     |
| --- | --- | ------- | ------ | -------- | ----------- | --- | ------------ | --- | ----------- | ---------- | --- |
Among the evaluated configurations, fixed three-minute IMF1 features with Random
Forest produced the highest observed mean performance. Relative to the matched
filtered time-domain representation, IMF1 produced numerically higher mean values
across all six reported metrics, although the differences in ROC-AUC and AP were
modest.
|     |     | Materials | and |     | methods |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
The proposed framework is illustrated in Fig. 1. The analysis consisted of signal
|     |     | segmentation, | EMD-based |     | decomposition, |     | IMF | selection, | feature | extraction, |     |
| --- | --- | ------------- | --------- | --- | -------------- | --- | --- | ---------- | ------- | ----------- | --- |
classification, and recording-level aggregation. The following subsections describe the
dataset, preprocessing, feature extraction, model training, and evaluation protocol.
| August | 19, 2026 |     |     |     |     |     |     |     |     |     | 5/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Fig 1. Overview of the proposed EHG-based recording-level
term-versus-preterm classification framework. Dataset-provided filtered EHG
recordings were segmented using annotated-interval and non-overlapping fixed 3-minute
strategies. Each segment was decomposed using empirical mode decomposition (EMD),
and the first four intrinsic mode functions (IMF1-IMF4) were evaluated under the same
feature extraction and classification framework. IMF1 was selected based on the
resulting recording-level performance and used for the subsequent analyses. Burst and
peak, temporal-energy, and entropy features were extracted from the selected
representation and used to train machine-learning classifiers. Segment-level
classification scores were aggregated using maximum-score aggregation to obtain one
recording-level score for classification.
Dataset
The publicly available Term-Preterm EHG Dataset with Tocogram (TPEHGT) [24,33]
was used in this study. The dataset was developed at the Faculty of Computer and
Information Science, University of Ljubljana, Slovenia, with recordings collected at the
Department of Obstetrics and Gynecology, University Medical Center Ljubljana.
The dataset comprises 31 approximately 30-minute uterine recordings. Of these, 13
recordings were obtained from eight pregnancies that ended in spontaneous preterm
delivery and 13 recordings from ten pregnancies that ended in spontaneous term
delivery. The mean gestational ages at delivery were 33.7±1.97 weeks for the preterm
group and 38.1±1.04 weeks for the term group. The pregnancy recordings were
acquired during routine antenatal visits at a pooled mean gestational age of 30.2±2.76
weeks. The remaining five recordings were obtained from non-pregnant women. The
preterm recordings contain 47 annotated contraction intervals and 47 annotated dummy
(non-contraction) intervals, whereas the term recordings contain 53 annotated
contraction intervals and 53 annotated dummy intervals.
Recordings were acquired using four abdominal surface electrodes arranged in two
horizontal rows symmetrically above and below the navel, with 7 cm spacing. From
these electrodes, the dataset provides three differential EHG signals, S =E −E ,
1 2 1
S =E −E , and S =E −E , together with a simultaneously recorded tocogram
2 2 3 3 4 3
(TOCO) signal obtained using an external tocodynamometer.
The present analysis included the 26 pregnancy recordings corresponding to term
and preterm deliveries and excluded the five recordings from non-pregnant women.
These 26 recordings originated from 18 pregnancies. Because the public release does not
August 19, 2026 6/33

provide an explicit recording-to-pregnancy mapping suitable for pregnancy-level
grouping, cross-validation was performed using the recording as the grouping unit.
Consequently, possible dependence between multiple recordings originating from the
|     |     | same pregnancy |     | could | not be controlled. |     |     |     |     |     |
| --- | --- | -------------- | --- | ----- | ------------------ | --- | --- | --- | --- | --- |
Only the three differential EHG signals were used as classifier inputs. The TOCO
signal itself was not used as a predictor because the proposed features were intended to
characterize uterine electrical rather than mechanical activity. However, TOCO
contributed indirectly to the annotation-guided analysis because the dataset-provided
contraction annotations were defined by the dataset creators with reference to TOCO
|     |     | deflections  | together | with            | accompanying |              | EHG | activity.       |                |     |
| --- | --- | ------------ | -------- | --------------- | ------------ | ------------ | --- | --------------- | -------------- | --- |
|     |     | The original |          | data collection |              | was approved |     | by the National | Medical Ethics |     |
Committee of the Republic of Slovenia (approvals No. 32/01/97 and No. 108/09/09),
and written informed consent was obtained from participants as reported by the dataset
|     |     | creators.     | The present |     | study involved | secondary   |             | analysis of | publicly available |     |
| --- | --- | ------------- | ----------- | --- | -------------- | ----------- | ----------- | ----------- | ------------------ | --- |
|     |     | de-identified | data        | and | no new         | participant | recruitment | or data     | collection.        |     |
|     |     | Preprocessing |             | and | segmentation   |             |             |             |                    |     |
The three differential EHG signals were sampled at 20 Hz and were segmented using
|     |     | two temporal | strategies |     | before | EMD and | feature | extraction. |     |     |
| --- | --- | ------------ | ---------- | --- | ------ | ------- | ------- | ----------- | --- | --- |
Signal preparation
The dataset-provided filtered EHG signals were used as inputs to the proposed
framework. In the TPEHGT release, each differential EHG signal is provided in both
unfiltered and filtered form. The filtered signals were obtained by the dataset creators
using a four-pole bidirectional Butterworth band-pass filter with cutoff frequencies of
0.08 and 5.0 Hz. Accordingly, no additional band-pass filtering was applied in the
|     |     | present study | before | segmentation |     | or  | EMD. |     |     |     |
| --- | --- | ------------- | ------ | ------------ | --- | --- | ---- | --- | --- | --- |
EMD was applied directly to the dataset-provided filtered EHG segments, for which
very-low-frequency components below 0.08 Hz and components above 5.0 Hz had
already been attenuated by the dataset preprocessing. No fixed-window segment or
dataset-provided annotated interval was removed by an additional manual or automated
|     |     | artifact-rejection |     | rule       | in the present | analysis. |     |     |     |     |
| --- | --- | ------------------ | --- | ---------- | -------------- | --------- | --- | --- | --- | --- |
|     |     | Segmentation       |     | strategies |                |           |     |     |     |     |
Two segmentation strategies were used to examine how temporal segmentation
|     |     | influenced | recording-level |     | term-versus-preterm |     |     | classification. |     |     |
| --- | --- | ---------- | --------------- | --- | ------------------- | --- | --- | --------------- | --- | --- |
Annotated-interval segmentation The annotation-guided strategy used both types
of manually annotated intervals provided with the TPEHGT dataset: contraction
intervals and dummy (non-contraction) intervals. The preterm recordings contain 47
contraction and 47 dummy intervals, whereas the term recordings contain 53 contraction
and 53 dummy intervals. Thus, 200 annotated intervals were included across the 26
pregnancy recordings. Each annotated interval was treated as an individual segment for
subsequent EMD and feature extraction. The number of annotated intervals varied
|     |     | among recordings |     | according | to  | the dataset-provided |     | annotations. |     |     |
| --- | --- | ---------------- | --- | --------- | --- | -------------------- | --- | ------------ | --- | --- |
Fixed 3-minute segmentation Each recording was divided into consecutive,
non-overlapping complete 3-minute windows (180 s). At the sampling rate of 20 Hz,
each complete window contained 3600 samples. Any trailing portion shorter than 180 s
was excluded rather than padded or treated as a shorter segment. This procedure
| August | 19, 2026 |     |     |     |     |     |     |     |     | 7/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

yielded 249 fixed-length segments across the 26 pregnancy recordings: 15 recordings
contributed ten complete windows and 11 recordings contributed nine. Unlike the
annotation-guided strategy, fixed-window segmentation did not depend on manually
defined interval annotations and sampled the recordings using a uniform temporal
representation.
The qualitative difference between the two strategies is illustrated in Fig. 2. The
annotated-interval strategy retains the dataset-provided contraction and dummy
intervals, whereas fixed-window segmentation divides the available recording duration
into consecutive complete 3-minute windows irrespective of the interval annotations. In
the analytical pipeline, segmentation was performed before EMD, and each resulting
segment was decomposed independently.
Fig 2. Comparison of annotated-interval and fixed 3-minute segmentation
on a representative recording. (A) Filtered EHG signal from one differential
channel, with dataset-provided contraction intervals and dummy (non-contraction)
intervals shown as separately shaded regions and fixed 3-minute window boundaries
shown as dashed vertical lines. (B) An IMF1 representation of the same recording
shown only to illustrate how the segmentation schemes relate to oscillatory EHG
activity. The annotated-interval strategy uses both contraction and dummy intervals,
whereas the fixed-window strategy uses consecutive non-overlapping complete 3-minute
windows irrespective of the annotations. For the analytical pipeline, segmentation was
performed before EMD and each resulting segment was decomposed independently.
Recording-level data separation
To prevent direct leakage between segments derived from the same recording,
cross-validation partitions were constructed at the recording level. For each split, one
class label was associated with each of the 26 recordings, and stratification was
performed on these recording-level entries. The resulting training and validation
recording identifiers were then mapped back to their constituent segments, ensuring
that all segments from a given recording remained entirely within either the training or
validation set in that fold. No oversampling was applied.
Grouping could not be performed at the pregnancy level because the public
TPEHGT release does not provide an explicit recording-to-pregnancy mapping suitable
for constructing pregnancy-grouped folds. Consequently, possible dependence between
multiple recordings originating from the same pregnancy cannot be excluded. The
August 19, 2026 8/33

complete repeated cross-validation and recording-level evaluation procedure is described
|     |     | in the Evaluation | metrics            | subsection. |     |     |
| --- | --- | ----------------- | ------------------ | ----------- | --- | --- |
|     |     | Empirical         | mode decomposition |             |     |     |
Empirical mode decomposition (EMD) was used to obtain data-adaptive oscillatory
components from the filtered EHG signals [32]. Unlike decomposition methods based on
predefined basis functions, EMD represents a signal according to its local characteristic
time scales and is therefore well suited to nonlinear and nonstationary signals. This
property is particularly relevant to EHG, in which uterine electrical activity is
|     |     | intermittent | and its oscillatory | structure | can vary over time. |     |
| --- | --- | ------------ | ------------------- | --------- | ------------------- | --- |
For a filtered EHG segment s[n], EMD iteratively identifies the local maxima and
minima and interpolates them to form upper and lower envelopes. The mean of these
envelopes is removed from the signal through the sifting process until the resulting
component satisfies the conditions of an intrinsic mode function (IMF). After extraction
of an IMF, the same procedure is applied to the remaining signal to obtain progressively
slower oscillatory components. The resulting decomposition can be expressed as
K
(cid:88)
|     |     |     |     | s[n]= | c [n]+r[n], | (1) |
| --- | --- | --- | --- | ----- | ----------- | --- |
k
k=1
where c [n] denotes the kth IMF and r[n] is the residual component. Lower-order
k
IMFs generally represent faster local oscillations, whereas higher-order IMFs describe
|     |     | progressively | slower variations | in the signal. |     |     |
| --- | --- | ------------- | ----------------- | -------------- | --- | --- |
EMD was applied independently to each EHG channel within each segmented
interval using the PyEMD implementation (EMD-signal v1.9.0) with its standard sifting
and stopping criteria. Decomposition was limited to the first four IMFs required for the
present analysis. The residual returned by EMD was kept separate from the IMFs and
|     |     | was not | used as a feature-source | representation | for classification. |     |
| --- | --- | ------- | ------------------------ | -------------- | ------------------- | --- |
Fig. 3 illustrates the first four IMFs and residual obtained from a representative
filtered EHG segment, together with their power spectral densities (PSDs) and
|     |     | autocorrelation | functions. |     |     |     |
| --- | --- | --------------- | ---------- | --- | --- | --- |
No fixed physiological frequency band was assigned to an individual IMF. Because
EMD is data-adaptive, the spectral content of a given IMF can vary across segments
and recordings. The first four IMFs were therefore compared empirically under the
same downstream feature-extraction and classification framework, and their spectral
|     |     | characteristics | were examined    | after decomposition. |          |     |
| --- | --- | --------------- | ---------------- | -------------------- | -------- | --- |
|     |     | Selection       | of the intrinsic | mode                 | function |     |
The first four IMFs were evaluated separately to examine which mode provided the
strongest representation for the selected feature framework. For each IMF, the same
42-dimensional channel-wise feature set, classifier set, recording-level aggregation, and
cross-validation procedure were used. No IMF was selected a priori on the basis of its
|     |     | nominal | order or an assumed | physiological | frequency interval. |     |
| --- | --- | ------- | ------------------- | ------------- | ------------------- | --- |
The comparison was performed within the fixed 3-minute segmentation setting. For
each IMF, the classifier with the highest mean recording-level balanced accuracy was
identified, and the resulting IMF-level performances were compared using the same
criterion. IMF1 yielded the highest mean balanced accuracy among IMF1–IMF4 and
was therefore carried forward for the subsequent feature, segmentation, and model
analyses.
Because IMF and classifier selection were performed using the same dataset on
which their cross-validated performance was summarized, this comparison is considered
| August | 19, 2026 |     |     |     |     | 9/33 |
| ------ | -------- | --- | --- | --- | --- | ---- |

Fig 3. Representative empirical mode decomposition of a filtered EHG
|     |     | segment. The | dataset-provided | filtered EHG | segment | was decomposed | into |
| --- | --- | ------------ | ---------------- | ------------ | ------- | -------------- | ---- |
IMF1-IMF4 and a residual component. For each component, the time-domain waveform,
PSD, and autocorrelation function are shown. The example illustrates the progression
from faster local oscillations in the lower-order IMFs to slower variation in the
|        |          | higher-order | IMFs and residual. |     |     |     |       |
| ------ | -------- | ------------ | ------------------ | --- | --- | --- | ----- |
| August | 19, 2026 |              |                    |     |     |     | 10/33 |

an exploratory within-dataset selection rather than an independent validation of IMF1.
The resulting performance estimates may therefore contain some selection optimism and
require confirmation in an independent dataset.
After this empirical selection, the spectral distribution of IMF1 was examined
descriptively rather than used as an additional selection criterion. Welch PSDs [34] were
averaged within each recording and subsequently within each class, as shown in Fig. 4.
For notation, the selected IMF1 sequence is denoted by x[n]=c [n] in the remainder of
1
the Methods section.
Fig 4. Average IMF1 PSD by class. Welch PSDs were estimated from IMF1
components extracted from fixed 3-minute filtered EHG segments using a Hann window
of length 1024 samples with 50% overlap. For each recording, PSDs were averaged
across segments and across the three EHG channels, and the resulting recording-level
PSDs were averaged within each class. Term recordings are shown in blue and preterm
recordings in red. The y-axis is log scaled and the frequency range is shown from 0 to
5 Hz. The curves show class-dependent spectral differences, with preterm recordings
showing higher IMF1 power mainly in the lower frequency portion of the displayed
range.
Feature extraction
Fourteen feature types were extracted independently from each of the three EHG
channels, and the channel-wise values were concatenated to form a 42-dimensional
feature vector for each segment. The features were organized into three families: eight
peak and burst descriptors, three temporal-energy descriptors, and three entropy
descriptors. These families were selected to characterize complementary aspects of event
timing and morphology, waveform variation, typical magnitude, and local energy, and
nonlinear signal complexity.
For the EMD-based analysis, the features were calculated from the empirically
selected IMF1 representation, denoted by x[n]=c [n]. For the matched filtered
1
time-domain comparator, the same feature definitions, channel concatenation, and
segmentation-specific feature parameters were applied directly to the corresponding
dataset-filtered EHG segments; only the input signal representation differed. This
matched design enabled the contribution of the EMD-derived representation to be
examined without changing the feature set or downstream classification framework.
August 19, 2026 11/33

The selected feature families were motivated by the burst-like and nonstationary
characteristics of uterine electrical activity described in the Introduction. Peak and
burst descriptors characterize the timing, density, morphology, and grouping of
algorithmically detected peak-like events; temporal-energy descriptors summarize
waveform variation and energy within the analyzed representation; and entropy
|     |     | descriptors | quantify regularity |     | and complexity | [10,16,35]. |     |     |
| --- | --- | ----------- | ------------------- | --- | -------------- | ----------- | --- | --- |
|     |     | Burst       | and peak features   |     |                |             |     |     |
Peak and burst-related features were calculated from the magnitude of the analyzed
signal representation,
|     |     |     |     |     | z[n]=|x[n]|. |     |     | (2) |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
A local maximum was retained as a peak when its magnitude exceeded the robust
|     |     | adaptive | threshold |     |                |         |     |     |
| --- | --- | -------- | --------- | --- | -------------- | ------- | --- | --- |
|     |     |          |           | T   | =median(z)+THK | MAD(z), |     | (3) |
peak
where THK is the threshold multiplier and MAD denotes the median absolute
deviation. Detected peaks were required to be separated by at least MD seconds.
Consecutive peaks were assigned to the same burst-like group when their inter-peak
interval was less than or equal to BT seconds; otherwise, a new group was initiated.
|     |     | Fig. 5 illustrates | this | procedure. |     |     |     |     |
| --- | --- | ------------------ | ---- | ---------- | --- | --- | --- | --- |
Fig 5. Representative peak and burst-like event detection on the selected
IMF1 component. Detected peak-like events were identified from the IMF1
magnitude |x[n]| and are marked at their corresponding locations on the IMF1
waveform. Dashed horizontal lines indicate the magnitude-based detection threshold,
shown at ±T for visualization, and shaded regions indicate burst-like groups formed
peak
|     |     | by temporally | adjacent | detected | peaks. |     |     |     |
| --- | --- | ------------- | -------- | -------- | ------ | --- | --- | --- |
Eight descriptors were derived from the detected peak and burst-like structure. For
a segment of duration D seconds containing P detected peaks, peak rate was defined as
P
|     |     |     |     |     | Peak Rate= | .   |     | (4) |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
D
Peak rate therefore describes the temporal density of detected peak-like events.
For detected peak magnitudes {a }P , mean peak amplitude was computed as
i i=1
P
1 (cid:88)
|     |     |     |     | Peak | Amp Mean= | a . |     | (5) |
| --- | --- | --- | --- | ---- | --------- | --- | --- | --- |
i
P
i=1
|     |     | The | coefficient of | variation | of peak amplitude | was calculated | as  |     |
| --- | --- | --- | -------------- | --------- | ----------------- | -------------- | --- | --- |
σ
a
|     |     |     |     |     | Peak Amp CV= | ,   |     | (6) |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
µ +ϵ
a
| August | 19, 2026 |     |     |     |     |     |     | 12/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | ----- |

where µ a and σ a are the mean and population standard deviation of the detected
|     |     | peak magnitudes, |     | respectively. |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
For peak locations {t }P expressed in seconds, consecutive inter-peak intervals
i i=1
|     |     | were defined | as              |     |          |     |          |        |     |     |     |     |
| --- | --- | ------------ | --------------- | --- | -------- | --- | -------- | ------ | --- | --- | --- | --- |
|     |     |              |                 |     |          | ∆t  | i =t i+1 | −t i . |     |     |     | (7) |
|     |     | The          | mean inter-peak |     | interval | was |          |        |     |     |     |     |
P−1
1 (cid:88)
|     |     |     |     |     |     | IPI Mean= |     |     | ∆t , |     |     | (8) |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | ---- | --- | --- | --- |
i
|     |     |     |     |     |     |     | P −1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
i=1
|     |     | and | its coefficient |     | of variation | was |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
σ
∆t
|     |     |     |     |     |     | IPI | CV= |     | ,   |     |     | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ +ϵ
∆t
where µ and σ denote the mean and population standard deviation of the
∆t ∆t
|     |     | inter-peak | intervals. |               |     |          |           |        |       |           |         |     |
| --- | --- | ---------- | ---------- | ------------- | --- | -------- | --------- | ------ | ----- | --------- | ------- | --- |
|     |     | Peak       | width      | was estimated |     | from the | magnitude | signal | using | the width | at half |     |
prominence of each detected peak. For detected widths {w }P expressed in seconds,
|     |     |           |       |     |         |     |     |     |     | i i=1 |     |     |
| --- | --- | --------- | ----- | --- | ------- | --- | --- | --- | --- | ----- | --- | --- |
|     |     | mean peak | width | was | defined | as  |     |     |     |       |     |     |
|     |     |           |       |     |         |     |     | 1   | P   |       |     |     |
(cid:88)
|     |     |     |     |     | Peak | Width | Mean= |     | w . |     |     | (10) |
| --- | --- | --- | --- | --- | ---- | ----- | ----- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |      |       |       | P   | i   |     |     |      |
i=1
If B burst-like groups were identified within a segment, burst rate was defined as
B
|     |     |     |     |     |     | Burst | Rate= |     | .   |     |     | (11) |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | ---- |
D
Normalization by segment duration was used because the annotated intervals have
variable durations, whereas the fixed-window segments have a constant duration.
Finally, if q denotes the number of detected peaks in burst-like group b, the mean
b
|     |     | number | of peaks | per burst | was | computed | as  |     |     |     |     |     |
| --- | --- | ------ | -------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- |
B
1 (cid:88)
|     |     |     |     |     | Mean | Peaks | per Burst= |     | q   | .   |     | (12) |
| --- | --- | --- | --- | --- | ---- | ----- | ---------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |      |       |            |     | B   | b   |     |      |
b=1
These descriptors characterize algorithmically detected peak timing, magnitude,
width, spacing, and grouping within the analyzed signal representation. They were not
interpreted as event-by-event physiological contraction labels, and no uniform direction
|     |     | of change | between | term | and preterm |     | recordings | was | assumed. |     |     |     |
| --- | --- | --------- | ------- | ---- | ----------- | --- | ---------- | --- | -------- | --- | --- | --- |
A small numerical constant of ϵ=10−12 was used where required to avoid numerical
singularities. When no peak or burst-like event was detected, peak rate and burst rate
were assigned their meaningful value of zero. Quantities that could not be estimated
because an insufficient number of peaks or peak pairs was available were treated as
missing values rather than as numerical zeros. Missing feature values were subsequently
imputed using means estimated exclusively from the corresponding cross-validation
training partition.
| August | 19, 2026 |     |     |     |     |     |     |     |     |     |     | 13/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

|     |     | Temporal              | energy | features |             |     |      |            |      |     |          |        |     |
| --- | --- | --------------------- | ------ | -------- | ----------- | --- | ---- | ---------- | ---- | --- | -------- | ------ | --- |
|     |     | Three temporal-energy |        |          | descriptors |     | were | calculated | from | the | analyzed | signal |     |
representation to characterize complementary aspects of waveform variation, typical
magnitude, and local energy. These descriptors were Difference Absolute Standard
Deviation Value (DASDV), log detector, and mean Teager-Kaiser energy (MTKE),
which have previously been used in EMD-based EHG analysis for term-preterm
classification [36–39]. Let x[n] denote the analyzed signal sequence of length N.
DASDV quantifies short-lag waveform variation through the root mean square of
|     |     | consecutive | sample | differences: |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:118)
|     |     |     |     |     |        | (cid:117) |     | N−1      |                 |     |     |     |      |
| --- | --- | --- | --- | --- | ------ | --------- | --- | -------- | --------------- | --- | --- | --- | ---- |
|     |     |     |     |     |        | (cid:117) | 1   | (cid:88) |                 |     |     |     |      |
|     |     |     |     |     | DASDV= | (cid:116) |     |          | (x[n+1]−x[n])2. |     |     |     | (13) |
N −1
n=1
The log detector provides a compressed measure of the typical signal magnitude and
|     |     | was calculated | as  |     |         |     |          |          |              |          |     |     |      |
| --- | --- | -------------- | --- | --- | ------- | --- | -------- | -------- | ------------ | -------- | --- | --- | ---- |
|     |     |                |     |     |         |     | (cid:32) | N        |              | (cid:33) |     |     |      |
|     |     |                |     |     |         |     | 1        | (cid:88) |              |          |     |     |      |
|     |     |                |     |     | LOG=exp |     |          |          | ln(|x[n]|+ϵ) |          | ,   |     | (14) |
N
n=1
ϵ=10−12
|     |     | where |     | was | included |     | to avoid | evaluating |     | the logarithm |     | at zero. |     |
| --- | --- | ----- | --- | --- | -------- | --- | -------- | ---------- | --- | ------------- | --- | -------- | --- |
The Teager-Kaiser energy operator [40] was defined for the interior samples as
Ψ[x[n]]=x[n]2−x[n−1]x[n+1],
(15)
and MTKE was computed as the arithmetic mean of the unrectified operator:
N−1
1 (cid:88)
|     |     |     |     |     |     | MTKE= |     |     | Ψ[x[n]]. |     |     |     | (16) |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | -------- | --- | --- | --- | ---- |
|     |     |     |     |     |     |       | N   | −2  |          |     |     |     |      |
n=2
|     |     | DASDV      | therefore | characterizes |            |     | short-lag | waveform |               | change, | the  | log detector |     |
| --- | --- | ---------- | --------- | ------------- | ---------- | --- | --------- | -------- | ------------- | ------- | ---- | ------------ | --- |
|     |     | summarizes | typical   | signal        | magnitude, |     | and       | MTKE     | characterizes |         | mean | local        |     |
Teager-Kaiser energy. These quantities were treated as complementary signal
|     |     | descriptors | rather   | than | collectively |     | as measures |     | of variability. |     |     |     |     |
| --- | --- | ----------- | -------- | ---- | ------------ | --- | ----------- | --- | --------------- | --- | --- | --- | --- |
|     |     | Entropy     | features |      |              |     |             |     |                 |     |     |     |     |
Permutation entropy, sample entropy, and Shannon entropy were used to characterize
complementary aspects of signal complexity and organization. Permutation entropy
describes the diversity of local ordinal patterns, sample entropy characterizes the
regularity or predictability of waveform patterns, and Shannon entropy summarizes the
dispersion of the signal amplitude distribution. These measures were treated as
signal-level descriptors rather than direct measures of global uterine synchronization.
|     |     | Permutation |         | entropy | [41]                              | was calculated |     | from | ordinal | patterns |     | formed from |      |
| --- | --- | ----------- | ------- | ------- | --------------------------------- | -------------- | --- | ---- | ------- | -------- | --- | ----------- | ---- |
|     |     | embedding   | vectors |         |                                   |                |     |      |         |          |     |             |      |
|     |     |             |         |         | v =[x[i],x[i+τ],...,x[i+(m−1)τ]]. |                |     |      |         |          |     |             | (17) |
i
If p j denotes the probability of the jth ordinal pattern, permutation entropy was
defined as
m!
(cid:88)
|     |     |     |     |     |     | H   | =−  | p   | ln(p | ),  |     |     | (18) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     | PE  |     | j j  |     |     |     |      |
j=1
|        |          | and | normalized | as  |     |     |     |     |     |     |     |     |       |
| ------ | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| August | 19, 2026 |     |            |     |     |     |     |     |     |     |     |     | 14/33 |

H
|     |     |     |     |     |     | Hnorm |     | PE     |     |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |       |     | =      | .   |     |     |     | (19) |
|     |     |     |     |     |     |       | PE  | ln(m!) |     |     |     |     |      |
In this study, an embedding dimension of m=3 and delay τ =1 were used, giving
|     |     | normalization | by  | ln(3!). |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sample entropy [42] was used to quantify the persistence of similarity between
waveform patterns when they were extended by one sample. It was defined as
(cid:18) A (cid:19)
|     |     |     |     |     |     | SampEn(m,r)=−ln |     |     |     | ,   |     |     | (20) |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | ---- |
B
|     |     | where | B is the | number | of  | distinct | template | pairs | of length | m   | satisfying | the |     |
| --- | --- | ----- | -------- | ------ | --- | -------- | -------- | ----- | --------- | --- | ---------- | --- | --- |
similarity criterion and A is the number of corresponding pairs that remain similar
when extended to length m+1. Sample entropy was calculated using m=2 and τ =1,
with the similarity tolerance set to r =0.10σ, where σ is the population standard
deviation of the analyzed segment. Similarity was evaluated using the Chebyshev
|     |     | distance, | with self-matches |     | excluded.  |     |      |               |     |              |     |     |     |
| --- | --- | --------- | ----------------- | --- | ---------- | --- | ---- | ------------- | --- | ------------ | --- | --- | --- |
|     |     | Shannon   | entropy           | was | calculated |     | from | the amplitude |     | distribution | as  |     |     |
K
(cid:88)
|     |     |     |     |     |     | H   | =−  | p ln(p | ),  |     |     |     | (21) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | S   |     | k      | k   |     |     |     |      |
k=1
where p k denotes the probability of samples falling within histogram bin k. The
|     |     | amplitude | range | of each | segment | was | divided | into | K =50 | equal-width |     | bins. |     |
| --- | --- | --------- | ----- | ------- | ------- | --- | ------- | ---- | ----- | ----------- | --- | ----- | --- |
Natural logarithms were used for all three entropy measures. When sample entropy
was undefined because no valid template matches were available, the corresponding
feature value was treated as missing and subsequently imputed using statistics
|     |     | estimated | from       | the corresponding |           | cross-validation |          |     | training | partition. |     |     |     |
| --- | --- | --------- | ---------- | ----------------- | --------- | ---------------- | -------- | --- | -------- | ---------- | --- | --- | --- |
|     |     | Feature   | extraction |                   | parameter |                  | settings |     |          |            |     |     |     |
The peak and burst detection parameters were treated as analysis settings rather than
physiological constants. The selected settings were determined during preliminary
exploratory development using the TPEHGT recordings and were subsequently fixed for
all analyses reported in this study. Because this preliminary parameter selection used
|     |     | the same | dataset | as the | final | evaluation | and | was | not nested | within | the | outer |     |
| --- | --- | -------- | ------- | ------ | ----- | ---------- | --- | --- | ---------- | ------ | --- | ----- | --- |
cross-validation procedure, the resulting performance estimates are interpreted as
|     |     | exploratory | rather | than | as independent |     | validation |     | of the | selected | parameter |     |     |
| --- | --- | ----------- | ------ | ---- | -------------- | --- | ---------- | --- | ------ | -------- | --------- | --- | --- |
configuration.
|     |     | The | final parameter |     | settings | are | summarized |     | in Table | 1. THK | and | MD were |     |
| --- | --- | --- | --------------- | --- | -------- | --- | ---------- | --- | -------- | ------ | --- | ------- | --- |
common to both segmentation strategies, whereas the burst-separation threshold BT
was set separately because the annotated intervals are variable in duration while the
fixed windows have a uniform duration. The sample-entropy parameter R defines the
tolerance as r =Rσ, where σ is the within-segment population standard deviation.
Table 1. Feature extraction parameter settings. THK is the multiplier used in
the robust peak-detection threshold; MD is the minimum distance between detected
peaks; BT is the maximum inter-peak interval used to group adjacent peaks into the
same burst-like event; and R is the multiplier applied to the within-segment population
|        |          | standard | deviation    | to       | define    | the sample-entropy |     |     | tolerance | r =Rσ. |     |     |       |
| ------ | -------- | -------- | ------------ | -------- | --------- | ------------------ | --- | --- | --------- | ------ | --- | --- | ----- |
|        |          |          | Segmentation |          |           | strategy           | THK |     | MD (s)    | BT     | (s) | R   |       |
|        |          |          | Annotated    |          | intervals |                    |     | 2.8 | 0.3       | 1.8    |     | 0.1 |       |
|        |          |          | Fixed        | 3-minute |           |                    |     | 2.8 | 0.3       | 2.0    |     | 0.1 |       |
| August | 19, 2026 |          |              |          |           |                    |     |     |           |        |     |     | 15/33 |

|     |     | Classification |     | models |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The extracted feature vectors were evaluated using nine supervised classification models:
Quadratic Discriminant Analysis (QDA), Logistic Regression (LR), Support Vector
Machine (SVM), Decision Tree (DT), Random Forest (RF), Gradient Boosting (GB),
Gaussian Naive Bayes (NB), Multi-Layer Perceptron (MLP), and CatBoost (CB). The
model settings used throughout the experiments are summarized in Table 2. All
|     |     | stochastic | models | used a | random | seed | of 42. |     |     |     |     |     |     |
| --- | --- | ---------- | ------ | ------ | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- |
Table 2. Classification model settings used in all experiments. Parameters not
explicitly listed retained the defaults of the corresponding software implementation; the
complete version-pinned computational environment is provided with the public code
repository.
|     |     | Model | Settings       |     |     |           |     |     |     |     |     |     |     |
| --- | --- | ----- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | QDA   | Regularization |     |     | parameter | =   | 0.5 |     |     |     |     |     |
LR L-BFGSsolver;C =0.5;balancedclassweights;maximumiterations
= 50,000
SVM Linearkernel;C =2.0;balancedclassweights;probabilityestimation
enabled
|     |     | DT  | Default |     | estimator | settings; |     | random | seed | = 42 |     |     |     |
| --- | --- | --- | ------- | --- | --------- | --------- | --- | ------ | ---- | ---- | --- | --- | --- |
RF 500 trees; maximum depth = 15; minimum leaf size = 1; balanced
|     |     |     | class    | weights; |           | random    | seed    | = 42      |      |          |     |     |     |
| --- | --- | --- | -------- | -------- | --------- | --------- | ------- | --------- | ---- | -------- | --- | --- | --- |
|     |     | GB  | Default  |          | estimator | settings; |         | random    | seed | = 42     |     |     |     |
|     |     | NB  | Gaussian |          | Naive     | Bayes;    | default | estimator |      | settings |     |     |     |
MLP Hidden layers = 256 and 128 units; L2 penalty = 0.0005; maximum
|     |     |     | iterations    |     | = 3,000;    | internal |          | validation-based |      | early       | stopping | disabled; |     |
| --- | --- | --- | ------------- | --- | ----------- | -------- | -------- | ---------------- | ---- | ----------- | -------- | --------- | --- |
|     |     |     | training-loss |     | convergence |          | patience |                  | = 25 | iterations; | random   | seed      | =   |
42
CB Depth = 6; learning rate = 0.1; logarithmic loss; random seed = 42
The selected models span linear, probabilistic, kernel-based, tree-based, ensemble,
and neural-network approaches. Tree-based ensemble models such as RF, GB, and CB
were included because they can represent nonlinear relationships and interactions
among the extracted features without strong distributional assumptions. CatBoost was
included as an additional gradient-boosting approach for tabular feature-based
|     |     | classification | [43]. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For every outer training partition, missing feature values were imputed using means
|     |     | estimated | exclusively | from | that | training | partition, |     | after | which features |     | were |     |
| --- | --- | --------- | ----------- | ---- | ---- | -------- | ---------- | --- | ----- | -------------- | --- | ---- | --- |
standardized using the corresponding training mean and standard deviation. The fitted
imputation and standardization transformations were then applied unchanged to the
associated validation data. Imputation, standardization, and classification were
|     |     | implemented | within   | a single | fold-fitted |            | processing |     | pipeline.    |     |               |     |     |
| --- | --- | ----------- | -------- | -------- | ----------- | ---------- | ---------- | --- | ------------ | --- | ------------- | --- | --- |
|     |     | For each    | segment, | the      | fitted      | classifier | produced   |     | an estimated |     | preterm-class |     |     |
probability using its model-specific probability prediction. These outputs were used as
classification scores for ranking, recording-level aggregation, and threshold-based
|     |     | classification; | they | were | not interpreted |     | as calibrated |     | individual |     | clinical | risk |     |
| --- | --- | --------------- | ---- | ---- | --------------- | --- | ------------- | --- | ---------- | --- | -------- | ---- | --- |
probabilities.
|     |     | Evaluation | metrics |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Model performance was evaluated using 30 randomized repetitions of five-fold stratified
cross-validation performed at the recording level. For each repetition, one class label
was associated with each of the 26 recordings and the recordings were newly partitioned
| August | 19, 2026 |     |     |     |     |     |     |     |     |     |     |     | 16/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

into five mutually exclusive folds. The resulting recording identifiers were then mapped
back to their constituent segments, ensuring that all segments from a given recording
remained entirely within either the training or validation partition of each outer fold.
|     |     | Each recording |     | therefore | contributed |     | one held-out | prediction | per | repetition. |     |
| --- | --- | -------------- | --- | --------- | ----------- | --- | ------------ | ---------- | --- | ----------- | --- |
Within every outer fold, feature imputation and standardization were estimated
exclusively from the outer-training data, after which the classifier was fitted to the
training segments. Each segment produced an estimated preterm-class output through
the classifier’s probability prediction. These outputs were treated as classification scores
|     |     | rather than | as  | calibrated | individual | clinical | risk | probabilities. |     |     |     |
| --- | --- | ----------- | --- | ---------- | ---------- | -------- | ---- | -------------- | --- | --- | --- |
Because the class label was defined at the recording level, segment-level scores were
aggregated to obtain one score for each recording. Maximum-score aggregation was
used:
|     |     |     |     |     |     | s record | =maxs | i , |     |     | (22) |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- | --- | ---- |
i
|     |     | where | s denotes |     | the preterm-class |     | score of | segment i | belonging | to the same |     |
| --- | --- | ----- | --------- | --- | ----------------- | --- | -------- | --------- | --------- | ----------- | --- |
i
recording. This aggregation rule was selected to retain the strongest preterm-like
|     |     | segment-level           | evidence |     | within a        | recording. |            |           |     |                |     |
| --- | --- | ----------------------- | -------- | --- | --------------- | ---------- | ---------- | --------- | --- | -------------- | --- |
|     |     | For threshold-dependent |          |     | classification, |            | a decision | threshold |     | was determined |     |
separately within each outer-training partition. After model fitting, scores were
obtained for the same outer-training segments and aggregated to the recording level
using Eq. 22. Candidate thresholds corresponding to the observed training-record scores
were evaluated, and the threshold yielding the highest Matthews correlation coefficient
(MCC) on these fitted training-record scores was selected. The resulting threshold was
then applied unchanged to the corresponding outer-validation recording scores.
Outer-validation labels were not used for model fitting or threshold selection. Because
threshold selection used fitted training scores rather than an additional inner out-of-fold
procedure, the resulting threshold-dependent performance is interpreted as exploratory.
Preterm delivery was treated as the positive class (label 1). Threshold-dependent
performance was summarized using accuracy, F1-score, balanced accuracy, and MCC.
Let TP, TN, FP, and FN denote true positives, true negatives, false positives, and false
|     |     | negatives, | respectively. |            | Accuracy     | was    | defined | as      |        |     |      |
| --- | --- | ---------- | ------------- | ---------- | ------------ | ------ | ------- | ------- | ------ | --- | ---- |
|     |     |            |               |            |              |        | TP      | +TN     |        |     |      |
|     |     |            |               |            | Accuracy=    |        |         |         | .      |     | (23) |
|     |     |            |               |            |              |        | TP +TN  | +FP +FN |        |     |      |
|     |     | Precision  | and           | recall     | were defined |        | as      |         |        |     |      |
|     |     |            |               |            |              | TP     |         |         | TP     |     |      |
|     |     |            |               | Precision= |              |        | ,       | Recall= |        | ,   | (24) |
|     |     |            |               |            |              | TP +FP |         |         | TP +FN |     |      |
|     |     | and        | the F1-score  |            | as           |        |         |         |        |     |      |
Precision·Recall
|     |     |     |     |     | F1=2 |     |     | .   |     |     | (25) |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- |
Precision+Recall
|        |          | Balanced | accuracy |          | was calculated |     | as         |         |        |          |       |
| ------ | -------- | -------- | -------- | -------- | -------------- | --- | ---------- | ------- | ------ | -------- | ----- |
|        |          |          |          |          |                |     | 1 (cid:18) | TP      | TN     | (cid:19) |       |
|        |          |          |          | Balanced | Accuracy=      |     |            | +       |        | ,        | (26)  |
|        |          |          |          |          |                |     | 2 TP       | +FN     | TN +FP |          |       |
|        |          | and      | MCC as   |          |                |     |            |         |        |          |       |
|        |          |          |          |          |                |     | TP ·TN     | −FP ·FN |        |          |       |
|        |          |          | MCC=     |          | (cid:112)      |     |            |         |        | .        | (27)  |
|        |          |          |          |          | (TP +FP)(TP    |     | +FN)(TN    | +FP)(TN |        | +FN)     |       |
| August | 19, 2026 |          |          |          |                |     |            |         |        |          | 17/33 |

MCC was used for threshold selection because it incorporates all four entries of the
|     |     | binary confusion |       | matrix | and provides | a balanced | summary | of classification |     |     |
| --- | --- | ---------------- | ----- | ------ | ------------ | ---------- | ------- | ----------------- | --- | --- |
|     |     | performance      | [44]. |        |              |            |         |                   |     |     |
Threshold-independent discrimination was evaluated using the area under the
receiver operating characteristic curve (ROC-AUC) and average precision (AP). Both
were calculated directly from the continuous recording-level classification scores and
therefore did not depend on the selected binary threshold. AP was calculated as the
step-weighted summary of the precision-recall curve rather than as a trapezoidal
|     |     | precision-recall | area. |     |     |     |     |     |     |     |
| --- | --- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
For each repetition, the held-out predictions from the five outer validation folds were
combined to form one complete out-of-fold set containing exactly one prediction for
each of the 26 recordings. Threshold-dependent metrics were then calculated from the
corresponding fold-specific binary predictions, whereas ROC-AUC and AP were
calculated from the pooled continuous recording-level scores. This produced one value
for each metric per repetition. The values reported in the Results are the means of the
|     |     | 30 repetition-level |     | estimates. |     |     |     |     |     |     |
| --- | --- | ------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Results
Results are reported as means across 30 repetitions of five-fold stratified cross-validation
performed at the recording level. Within each repetition, predictions from the five outer
validation folds were combined so that each of the 26 recordings contributed exactly one
out-of-fold prediction before the recording-level metrics were calculated. The 26
|     |     | recordings | comprised | 13  | term and 13 | preterm | recordings | originating | from 18 |     |
| --- | --- | ---------- | --------- | --- | ----------- | ------- | ---------- | ----------- | ------- | --- |
pregnancies.
The annotated-interval analysis included 200 dataset-provided segments, comprising
100 contraction intervals and 100 dummy (non-contraction) intervals. The fixed-window
analysis included 249 complete, non-overlapping 3-minute segments; 15 recordings
contributed ten windows and 11 recordings contributed nine. In all experiments,
segment-level classification scores were combined using maximum-score aggregation to
obtain one recording-level score before metric calculation. Preterm delivery was treated
|     |     | as the positive | class. |              |      |           |     |     |     |     |
| --- | --- | --------------- | ------ | ------------ | ---- | --------- | --- | --- | --- | --- |
|     |     | Comparison      |        | of intrinsic | mode | functions |     |     |     |     |
Table 3 compares the first four IMFs using fixed 3-minute segmentation under the same
feature extraction and recording-level evaluation framework. For each IMF, the
classifier with the highest mean balanced accuracy was retained for the comparison.
Among the four evaluated modes, IMF1 yielded the highest mean values for all six
reported metrics, with RF achieving an accuracy of 0.8308, F1-score of 0.7969, balanced
accuracy of 0.8308, MCC of 0.6998, ROC-AUC of 0.8157, and AP of 0.8877. The
corresponding mean balanced accuracies for IMF2, IMF3, and IMF4 were 0.7218,
|     |     | 0.5462, and | 0.6359,       | respectively. |         |        |             |          |              |     |
| --- | --- | ----------- | ------------- | ------------- | ------- | ------ | ----------- | -------- | ------------ | --- |
|     |     | IMF1        | was therefore | carried       | forward | as the | empirically | selected | mode for the |     |
subsequent analyses. Because mode and classifier selection were performed using the
same dataset on which their cross-validated performance was summarized, this
comparison is interpreted as an exploratory within-dataset selection rather than an
|        |          | independent | validation | of  | IMF1. |     |     |     |     |       |
| ------ | -------- | ----------- | ---------- | --- | ----- | --- | --- | --- | --- | ----- |
| August | 19, 2026 |             |            |     |       |     |     |     |     | 18/33 |

Table 3. Recording-level comparison of the first four IMFs using fixed
3-minute segmentation. For each IMF, the classifier with the highest mean balanced
accuracy was retained. Values are means across 30 complete repetition-level out-of-fold
|     |     | evaluations. | Preterm    | delivery |        | was treated |     | as the   | positive | class. |         |        |
| --- | --- | ------------ | ---------- | -------- | ------ | ----------- | --- | -------- | -------- | ------ | ------- | ------ |
|     |     | IMF          | Best model | Accuracy |        |             | F1  | Balanced | Acc.     | MCC    | ROC-AUC | AP     |
|     |     | IMF1         | RF         |          | 0.8308 | 0.7969      |     | 0.8308   |          | 0.6998 | 0.8157  | 0.8877 |
|     |     | IMF2         | RF         |          | 0.7218 | 0.6520      |     | 0.7218   |          | 0.4849 | 0.7403  | 0.7953 |
|     |     | IMF3         | RF         |          | 0.5462 | 0.3434      |     | 0.5462   |          | 0.1119 | 0.6440  | 0.6342 |
|     |     | IMF4         | GB         |          | 0.6359 | 0.6347      |     | 0.6359   |          | 0.2756 | 0.6744  | 0.6839 |
The representative decomposition in Fig. 3 shows that IMF1 contains faster local
variation than the subsequent modes. The class-averaged PSDs in Fig. 4 also show that
IMF1 is not confined to a fixed narrow frequency band. Preterm recordings had higher
mean IMF1 power mainly below approximately 0.7 Hz, whereas term recordings had
higher power over parts of the middle of the displayed range. These curves are
descriptive and do not establish a single physiological frequency interval for IMF1.
|     |     | Annotated-interval |     |     | classification |     |     | results |     |     |     |     |
| --- | --- | ------------------ | --- | --- | -------------- | --- | --- | ------- | --- | --- | --- | --- |
Table 4 summarizes the recording-level classification results obtained from IMF1
features extracted from the dataset-provided annotated intervals. RF yielded the
highest mean values across all six reported metrics, with an accuracy of 0.7821, F1-score
of 0.7793, balanced accuracy of 0.7821, MCC of 0.5687, ROC-AUC of 0.8023, and AP of
0.8817. GB and CB also showed comparatively high mean performance among the
|     |     | evaluated | classifiers. |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table 4. Recording-level classification performance for annotated-interval
segmentation using IMF1 features. Values are means across 30 complete
repetition-level out-of-fold evaluations. Preterm delivery was treated as the positive
class.
|     |     | Model | Accuracy |                | F1     | Balanced |         | Acc. |        | MCC    | ROC-AUC | AP     |
| --- | --- | ----- | -------- | -------------- | ------ | -------- | ------- | ---- | ------ | ------ | ------- | ------ |
|     |     | QDA   | 0.5538   |                | 0.4337 |          | 0.5538  |      |        | 0.1184 | 0.5866  | 0.5680 |
|     |     | LR    | 0.6577   |                | 0.6188 |          | 0.6577  |      |        | 0.3273 | 0.6907  | 0.7370 |
|     |     | SVM   | 0.5359   |                | 0.5926 |          | 0.5359  |      |        | 0.0746 | 0.5836  | 0.6336 |
|     |     | DT    | 0.5513   |                | 0.6479 |          | 0.5513  |      |        | 0.1214 | 0.5513  | 0.5290 |
|     |     | RF    | 0.7821   |                | 0.7793 |          | 0.7821  |      | 0.5687 |        | 0.8023  | 0.8817 |
|     |     | GB    | 0.7590   |                | 0.7572 |          | 0.7590  |      |        | 0.5221 | 0.7784  | 0.8450 |
|     |     | NB    | 0.6641   |                | 0.6200 |          | 0.6641  |      |        | 0.3381 | 0.6448  | 0.6370 |
|     |     | MLP   | 0.6269   |                | 0.6393 |          | 0.6269  |      |        | 0.2556 | 0.6483  | 0.7019 |
|     |     | CB    | 0.7538   |                | 0.7222 |          | 0.7538  |      |        | 0.5265 | 0.7921  | 0.8601 |
|     |     | Fixed | 3-minute | classification |        |          | results |      |        |        |         |        |
Table 5 summarizes the recording-level classification results obtained from fixed
3-minute IMF1 segments. RF yielded the highest mean values across all six reported
metrics, achieving an accuracy of 0.8308, F1-score of 0.7969, balanced accuracy of
|     |     | 0.8308, | MCC of 0.6998, |     | ROC-AUC |     | of 0.8157, | and | AP  | of 0.8877. | Among the |     |
| --- | --- | ------- | -------------- | --- | ------- | --- | ---------- | --- | --- | ---------- | --------- | --- |
configurations evaluated in this study, fixed 3-minute IMF1 features with RF yielded
|        |          | the highest | observed | mean | performance |     | across | all | six | metrics. |     |       |
| ------ | -------- | ----------- | -------- | ---- | ----------- | --- | ------ | --- | --- | -------- | --- | ----- |
| August | 19, 2026 |             |          |      |             |     |        |     |     |          |     | 19/33 |

Table 5. Recording-level performance for fixed 3-minute segmentation using
EHG-only IMF1 features. Values are means across 30 complete repetition-level
|     |     | out-of-fold | evaluations. | Preterm | delivery | was    | treated | as the | positive | class. |        |
| --- | --- | ----------- | ------------ | ------- | -------- | ------ | ------- | ------ | -------- | ------ | ------ |
|     |     | Model       | Accuracy     | F1      | Balanced |        | Acc.    | MCC    | ROC-AUC  |        | AP     |
|     |     | QDA         | 0.5513       | 0.5547  |          | 0.5513 |         | 0.1034 |          | 0.5193 | 0.5498 |
|     |     | LR          | 0.6051       | 0.5886  |          | 0.6051 |         | 0.2137 |          | 0.6402 | 0.6756 |
|     |     | SVM         | 0.5603       | 0.5723  |          | 0.5603 |         | 0.1221 |          | 0.5584 | 0.6114 |
|     |     | DT          | 0.5205       | 0.6486  |          | 0.5205 |         | 0.0459 |          | 0.5205 | 0.5122 |
|     |     | RF          | 0.8308       | 0.7969  |          | 0.8308 |         | 0.6998 |          | 0.8157 | 0.8877 |
|     |     | GB          | 0.7692       | 0.7486  |          | 0.7692 |         | 0.5497 |          | 0.7558 | 0.7961 |
|     |     | NB          | 0.6154       | 0.5661  |          | 0.6154 |         | 0.2387 |          | 0.6061 | 0.5955 |
|     |     | MLP         | 0.6205       | 0.5950  |          | 0.6205 |         | 0.2439 |          | 0.6114 | 0.6533 |
|     |     | CB          | 0.8013       | 0.7586  |          | 0.8013 |         | 0.6445 |          | 0.8034 | 0.8773 |
Fig 6. Recording-level ROC and precision–recall curves for fixed 3-minute
IMF1 features. (A) Receiver operating characteristic curves. (B) Precision-recall
curves. Curves were generated by pooling the repeated out-of-fold recording-level
classification scores obtained across the 30 cross-validation repetitions. Within each
repetition, each of the 26 recordings contributed exactly one out-of-fold score after
maximum-score aggregation of its segment-level outputs. The pooled curves therefore
contain repeated out-of-fold predictions of the same 26 recordings across different data
partitions and should not be interpreted as representing 780 independent observations.
The ROC-AUC and AP values associated with these pooled curves are descriptive
quantities and are distinct from the mean repetition-level ROC-AUC and AP values
|     |     | reported   | in Table 5. |          |     |             |     |          |     |     |     |
| --- | --- | ---------- | ----------- | -------- | --- | ----------- | --- | -------- | --- | --- | --- |
|     |     | Comparison | with        | filtered |     | time-domain |     | features |     |     |     |
To isolate the effect of the EMD-derived representation, the same feature definitions,
segmentation, classification models, recording-level aggregation, and evaluation
procedure were applied directly to the dataset-filtered time-domain EHG signals. Thus,
the IMF1 and filtered-signal analyses differed in the input signal representation while
|     |     | retaining | the same downstream |               | feature | and | classification | framework.    |     |           |      |
| --- | --- | --------- | ------------------- | ------------- | ------- | --- | -------------- | ------------- | --- | --------- | ---- |
|     |     | Under     | fixed 3-minute      | segmentation, |         | RF  | using          | IMF1 features |     | yielded a | mean |
accuracy of 0.8308 compared with 0.7846 for the matched filtered-signal representation.
F1-score increased from 0.7376 to 0.7969, balanced accuracy from 0.7846 to 0.8308, and
MCC from 0.6114 to 0.6998. The corresponding threshold-independent metrics were
| August | 19, 2026 |     |     |     |     |     |     |     |     |     | 20/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

also numerically higher for IMF1, with ROC-AUC increasing from 0.8073 to 0.8157 and
|     |     | AP from | 0.8773 to 0.8877 | (Table 6). |     |     |     |     |
| --- | --- | ------- | ---------------- | ---------- | --- | --- | --- | --- |
Therefore, IMF1 yielded numerically higher mean performance across all six reported
metrics in the matched fixed-window RF comparison. The differences in ROC-AUC and
|     |     | AP were | modest, however, | and the | representation | comparison | is interpreted |     |
| --- | --- | ------- | ---------------- | ------- | -------------- | ---------- | -------------- | --- |
descriptively because no independent test set or paired inferential comparison was used.
Table 6. Recording-level classification performance for fixed 3-minute
segmentation using matched filtered time-domain EHG features. Values are
means across 30 complete repetition-level out-of-fold evaluations. Preterm delivery was
|     |     | treated as | the positive | class.      |        |          |         |        |
| --- | --- | ---------- | ------------ | ----------- | ------ | -------- | ------- | ------ |
|     |     | Model      | Accuracy     | F1 Balanced |        | Acc. MCC | ROC-AUC | AP     |
|     |     | QDA        | 0.6487       | 0.6752      | 0.6487 | 0.3029   | 0.6286  | 0.6198 |
|     |     | LR         | 0.6590       | 0.6740      | 0.6590 | 0.3215   | 0.7231  | 0.6965 |
|     |     | SVM        | 0.6756       | 0.6978      | 0.6756 | 0.3579   | 0.6974  | 0.6967 |
|     |     | DT         | 0.5308       | 0.6541      | 0.5308 | 0.0825   | 0.5308  | 0.5172 |
|     |     | RF         | 0.7846       | 0.7376      | 0.7846 | 0.6114   | 0.8073  | 0.8773 |
|     |     | GB         | 0.7551       | 0.7205      | 0.7551 | 0.5284   | 0.7624  | 0.7871 |
|     |     | NB         | 0.6590       | 0.6304      | 0.6590 | 0.3260   | 0.6733  | 0.7120 |
|     |     | MLP        | 0.6705       | 0.6887      | 0.6705 | 0.3446   | 0.7114  | 0.7557 |
|     |     | CB         | 0.7513       | 0.6902      | 0.7513 | 0.5473   | 0.8051  | 0.8717 |
|     |     | Overall    | comparison   |             |        |          |         |        |
Table 7 summarizes the four principal segmentation and signal-representation
configurations. RF had the highest mean balanced accuracy in each of the four settings.
Within both segmentation strategies, the IMF1 representation yielded numerically
higher mean accuracy, F1-score, balanced accuracy, MCC, ROC-AUC, and AP than the
|     |     | matched | filtered time-domain | representation. |     |     |     |     |
| --- | --- | ------- | -------------------- | --------------- | --- | --- | --- | --- |
Among the four configurations, fixed 3-minute IMF1 features with RF yielded the
highest observed mean value for all six reported metrics. This configuration is therefore
treated as the empirically selected best-observed setting in the present dataset. Because
the classifier, signal representation, and segmentation comparisons were performed using
the same repeated cross-validation results used for performance reporting, the
comparison is exploratory rather than an independent validation of the selected
configuration.
Table 7. Exploratory best-observed recording-level performance across
segmentation strategies and signal representations. For each configuration, the
classifier with the highest mean balanced accuracy was retained. Values are means
across 30 complete repetition-level out-of-fold evaluations. Model, representation, and
segmentation comparisons were performed within the same dataset and should therefore
be interpreted as exploratory. Preterm delivery was treated as the positive class.
Segmentation Featuresource Bestmodel Accuracy F1 BalancedAcc. MCC ROC-AUC AP
Annotatedintervals Filteredtime-domain RF 0.7167 0.7032 0.7167 0.4382 0.7719 0.8411
Annotatedintervals IMF1 RF 0.7821 0.7793 0.7821 0.5687 0.8023 0.8817
Fixed3-minute Filteredtime-domain RF 0.7846 0.7376 0.7846 0.6114 0.8073 0.8773
Fixed3-minute IMF1 RF 0.8308 0.7969 0.8308 0.6998 0.8157 0.8877
To complement the repetition-level performance summaries in Table 7, Fig. 7 shows
a consensus recording-level classification summary for the selected RF configurations.
Each recording had one out-of-fold binary prediction in each of the 30 cross-validation
| August | 19, 2026 |     |     |     |     |     |     | 21/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | ----- |

repetitions, and the displayed class was determined by majority vote across these 30
predictions.
Under this consensus summary, the fixed 3-minute IMF1 configuration correctly
classified all 13 term recordings and 9 of 13 preterm recordings, whereas the
annotated-interval IMF1 configuration correctly classified 11 of 13 term recordings and
10 of 13 preterm recordings. The fixed-window configuration therefore produced four
consensus errors compared with five for the annotated-interval configuration and
produced no false-positive preterm classifications among the term recordings. In
contrast, the annotated-interval configuration correctly identified one additional
preterm recording.
The consensus matrices are descriptive summaries of prediction stability across
repeated cross-validation partitions and are distinct from the repetition-level confusion
matrices used to calculate the mean performance metrics reported in Table 7.
Fig 7. Majority-vote consensus recording-level confusion matrices for
selected RF configurations. Rows correspond to true class labels and columns
correspond to predicted labels. Each displayed prediction represents the majority-vote
consensus across the 30 out-of-fold binary predictions available for that recording.
Within each outer fold, segment-level classification scores were combined using
maximum-score aggregation, and the MCC-optimized threshold selected from the
corresponding fitted training-record scores was applied unchanged to the validation
recording scores. Values in parentheses show the row-normalized fractions. These
matrices provide descriptive consensus summaries across repeated cross-validation
partitions and do not represent the repetition-level confusion matrices used to calculate
the mean performance metrics in Table 7.
Feature behavior at the recording level
To examine the signal characteristics underlying the selected fixed 3-minute IMF1
configuration, recording-level feature distributions were summarized by feature type in
Fig. 8. Although the classifiers used the full 42-dimensional channel-specific feature
vector, each of the fourteen feature types was averaged across the three EHG channels
for visualization, and segment-level values were subsequently averaged within each
recording. This produced one recording-level value per feature type for each of the 26
recordings.
The distributions show class-dependent differences across multiple feature families
rather than a uniform increase or decrease in all IMF1 descriptors. Features with
August 19, 2026 22/33

positive Cohen’s d values, indicating higher recording-level values in the preterm group,
included peak rate, peak width at half prominence, burst rate, mean peaks per burst,
Shannon entropy, permutation entropy, and sample entropy. Permutation entropy
showed the largest positive effect size, whereas peak width at half prominence showed
only a small difference. Features with negative Cohen’s d values included mean peak
|     |     | amplitude, peak-amplitude |     | coefficient |     | of variation, |     | mean inter-peak | interval, |     |
| --- | --- | ------------------------- | --- | ----------- | --- | ------------- | --- | --------------- | --------- | --- |
inter-peak-interval coefficient of variation, DASDV, log detector, and MTKE.
Taken together, preterm recordings showed more frequent and more densely grouped
peak-like IMF1 events, with shorter and less variable inter-peak spacing and smaller,
less variable peak amplitudes. DASDV, log detector, and MTKE were also lower,
whereas Shannon, permutation, and sample entropy were higher. The combined pattern
therefore reflects differences in detected event organization, waveform magnitude and
temporal energy, and signal complexity rather than a single common change in overall
variability.
The largest descriptive effect sizes were observed for permutation entropy, log
detector, mean peak amplitude, DASDV, and MTKE. These distributions describe
recording-level directions of class separation but do not establish any individual
descriptor as a standalone physiological biomarker. No feature-level hypothesis tests
were performed and no multiplicity-adjusted statistical significance is inferred from the
Cohen’s d values. Moreover, because the public dataset does not provide a reproducible
mother-to-recording linkage, possible dependence between recordings originating from
the same pregnancy is not represented in these effect-size calculations. The distributions
should therefore be interpreted as descriptive signal-level complements to the
|     |     | multivariate | model analysis. |     |     |     |     |     |     |     |
| --- | --- | ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- |
Cohen’s d was used to quantify the standardized difference between the preterm and
|     |     | term recording-level |     | feature means: |     |         |       |     |     |      |
| --- | --- | -------------------- | --- | -------------- | --- | ------- | ----- | --- | --- | ---- |
|     |     |                      |     |                |     | µ       | −µ    |     |     |      |
|     |     |                      |     |                |     | preterm | term, |     |     |      |
|     |     |                      |     |                | d=  |         |       |     |     | (28) |
s
pooled
where µ and µ denote the preterm and term recording-level feature means,
preterm term
|     |     | respectively, | and |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:115)
|     |     |     |        |     |            | −1)s2   |             | −1)s2 |       |      |
| --- | --- | --- | ------ | --- | ---------- | ------- | ----------- | ----- | ----- | ---- |
|     |     |     |        |     | (n preterm |         | preterm +(n | term  | term. |      |
|     |     |     | s      | =   |            |         |             |       |       | (29) |
|     |     |     | pooled |     |            | n       | +n          | −2    |       |      |
|     |     |     |        |     |            | preterm |             | term  |       |      |
With this definition, positive Cohen’s d values indicate higher recording-level feature
values in preterm recordings, whereas negative values indicate higher values in term
recordings.
|     |     | Feature importance |     | analysis |     |     |     |     |     |     |
| --- | --- | ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- |
Grouped permutation feature importance was used to examine the dependence of the
selected IMF1 RF models on three predefined feature families: burst and peak features,
|     |     | temporal-energy | features, | and | entropy | features. | Each | group | contained the |     |
| --- | --- | --------------- | --------- | --- | ------- | --------- | ---- | ----- | ------------- | --- |
corresponding channel-specific features from all three EHG channels, thereby preserving
|     |     | the same 42-dimensional |     | feature | representation |     | used | by the classifiers. |     |     |
| --- | --- | ----------------------- | --- | ------- | -------------- | --- | ---- | ------------------- | --- | --- |
Within each outer validation fold, all features belonging to a given family were
jointly permuted across the validation segment rows using the same row permutation for
every feature in that family. This preserved the relationships among features within the
permuted family while disrupting their association with the original validation segments.
One permutation was performed for each feature family in each outer fold and
|        |          | cross-validation | repetition, | using | a base | random | seed | of 42. |     |       |
| ------ | -------- | ---------------- | ----------- | ----- | ------ | ------ | ---- | ------ | --- | ----- |
| August | 19, 2026 |                  |             |       |        |        |      |        |     | 23/33 |

Fig 8. Recording-level distributions of the 14 IMF1 feature types for term
and preterm recordings in the fixed 3-minute analysis. Each feature was
extracted independently from the three EHG channels, averaged across channels for
visualization, and subsequently averaged across fixed 3-minute segments within each
recording. The classifiers used the full 42-dimensional channel-specific feature vector,
whereas this figure provides a compact feature-type-level summary for signal-level
interpretation. Violin shapes show the distribution within each class, horizontal black
lines indicate the median, and individual recording values are overlaid as points.
Cohen’s d denotes the standardized difference between preterm and term recording-level
feature means, with positive values indicating higher values in preterm recordings. The
effect sizes are descriptive and were not accompanied by feature-level hypothesis tests or
multiplicity correction.
August 19, 2026 24/33

After permutation, segment-level classification scores were combined using the same
maximum-score recording-level aggregation as in the primary analysis. Within each of
the 30 cross-validation repetitions, the baseline and permuted recording-level scores
from the five outer validation folds were pooled to form complete 26-record out-of-fold
sets. Average precision (AP) was then calculated once for the baseline scores and once
|     |     | for each | permuted feature | family, | and importance | was        | defined as |      |
| --- | --- | -------- | ---------------- | ------- | -------------- | ---------- | ---------- | ---- |
|     |     |          |                  | I       | =AP            | −AP        | ,          | (30) |
|     |     |          |                  | g       | baseline       | permuted,g |            |      |
where g denotes the feature family. The reported importance for each feature family
is the mean of the 30 repetition-level AP decreases. Larger positive values indicate
greater dependence of the fitted RF model on the corresponding feature family, whereas
values near zero indicate little change in recording-level AP after permutation.
|     |     | Grouped | importance | was calculated |     | for the RF models | in both the |     |
| --- | --- | ------- | ---------- | -------------- | --- | ----------------- | ----------- | --- |
annotated-interval IMF1 and fixed 3-minute IMF1 settings. As shown in Fig. 9,
temporal-energy features produced the largest mean decrease in recording-level AP
|     |     | under both | segmentation | strategies. | In  | the annotated-interval | IMF1 model, |     |
| --- | --- | ---------- | ------------ | ----------- | --- | ---------------------- | ----------- | --- |
permutation of the temporal-energy features decreased AP by 0.1151 on average,
compared with 0.0193 for entropy features and 0.0133 for burst and peak features. In
the fixed 3-minute IMF1 model, the corresponding mean decreases were 0.0388, 0.0057,
|     |     | and 0.0116, | respectively. |     |     |     |     |     |
| --- | --- | ----------- | ------------- | --- | --- | --- | --- | --- |
Thus, temporal-energy descriptors produced the largest mean AP decrease in both
selected RF models. Burst and peak features showed smaller positive mean importance
in both settings, while the entropy group also showed a positive but smaller model-level
contribution than the temporal-energy group. These model-level results should be
distinguished from the descriptive feature distributions in Fig. 8: the consistent increase
in entropy measures observed in preterm recordings does not imply that entropy
provides the largest unique contribution to the RF classifiers. Because information may
also be shared among correlated feature families, grouped permutation importance is
interpreted as a descriptive measure of model dependence rather than as evidence of an
|     |     | independent | physiological | mechanism. |     |     |     |     |
| --- | --- | ----------- | ------------- | ---------- | --- | --- | --- | --- |
Discussion
Main findings
This study evaluated a signal-adaptive and interpretable EHG framework under
recording-level validation designed to prevent direct segment leakage across training and
validation folds. IMF1 yielded the highest mean performance among the first four
evaluated EMD modes, fixed 3-minute windows yielded higher mean performance than
the dataset-provided annotated intervals, and the IMF1 representation produced higher
mean threshold-dependent performance than matched filtered time-domain features
|     |     | under fixed-window |     | segmentation. |     |     |     |     |
| --- | --- | ------------------ | --- | ------------- | --- | --- | --- | --- |
Together, these findings support further evaluation of EMD as a signal-adaptive
representation for recording-level term-versus-preterm EHG classification. All segments
from a given recording remained within the same outer cross-validation fold, preventing
direct sharing of recording-specific segments between training and validation data.
However, pregnancy-wise independence could not be established from the identifiers
provided with the public dataset. The findings should therefore be interpreted as
exploratory recording-level evidence rather than independent pregnancy-level validation
|        |          | or calibrated | clinical | risk prediction. |     |     |     |       |
| ------ | -------- | ------------- | -------- | ---------------- | --- | --- | --- | ----- |
| August | 19, 2026 |               |          |                  |     |     |     | 25/33 |

Fig 9. Grouped permutation feature importance for the annotated-interval
and fixed 3-minute IMF1 RF models. Importance is shown as the mean decrease
in recording-level average precision (AP) after jointly permuting all features within each
feature family across validation segment rows. Within each of the 30 cross-validation
repetitions, baseline and permuted recording-level scores from the five outer validation
folds were pooled to form complete 26-record out-of-fold sets before AP was calculated.
One permutation was performed per feature family per outer fold in each repetition.
Larger positive decreases indicate greater model dependence on the corresponding
feature family, whereas values near zero indicate little change in recording-level AP after
permutation.
Interpretation of IMF1-derived feature patterns
A central feature of the preterm-associated pattern was the coexistence of reduced
waveform magnitude and event-level dispersion with increased entropy. Lower DASDV,
log detector, and MTKE indicate smaller short-lag changes, lower typical IMF1
magnitude, and lower mean temporal energy, while lower peak-amplitude and
inter-peak-interval coefficients of variation indicate more homogeneous detected event
size and spacing. These observations are not inconsistent with higher entropy because
the measures describe different signal properties: Shannon entropy summarizes
amplitude-bin occupancy, permutation entropy the diversity of short ordinal patterns,
and sample entropy the continuation of local waveform similarity. Combined with the
higher peak rate, burst rate, and mean number of peaks per burst, the pattern is
consistent with more frequent, smaller, and relatively stereotyped peak-like events
embedded within a more complex whole-segment waveform organization.
One possible explanation is alternation between burst-rich and relatively quiescent
signal states, with reduced within-state dispersion but greater diversity of state
occupancy, transitions, or local waveform morphology. This interpretation therefore
represents a testable signal-level hypothesis rather than a demonstrated physiological
mechanism.
The weak grouped entropy importance further indicates that the entropy direction
was descriptively informative but did not provide strong unique predictive information
in the selected RF models; temporal-energy features remained the stronger model-level
contribution.
August 19, 2026 26/33

Contribution of EMD and selection of IMF1
This study builds on earlier EMD-based uterine EMG/EHG research and extends it in
four important ways. Previous studies used EMD-derived instantaneous amplitude,
instantaneous frequency, entropy ratios, and time-domain descriptors for PTB-related
classification tasks [36,37,45]. The present study advances this line of work by
evaluating the first four IMFs under a common feature extraction and classification
framework, comparing the selected IMF representation with matched filtered
time-domain descriptors, comparing annotated-interval and fixed-window segmentation,
and reporting performance at the recording level using grouped cross-validation without
oversampling.
More recent work has investigated multivariate EMD (MEMD) for multichannel
EHG analysis, allowing jointly decomposed channels to maintain greater cross-channel
mode consistency [46]. The present study instead evaluates standard channel-wise EMD
as a simpler reproducible representation and focuses on matched representation,
segmentation, and recording-level comparisons. MEMD therefore represents an
important future comparator rather than an analysis performed in the present study.
This contribution addresses an important methodological gap in EHG-based PTB
prediction. Reported performance in previous studies varies widely and can be strongly
influenced by feature representation, segmentation strategy, data partitioning, and
whether segments from the same recording are treated as independent samples. By
assigning all segments from the same recording to the same validation fold and
aggregating segment-level classification scores to one recording-level score, the present
study aligns evaluation with the recording-level classification target and avoids treating
multiple segments from the same recording as independent validation cases. This makes
the reported estimates more appropriate for the study design than segment-level
performance measures alone.
IMF1 provided stronger classification performance than IMF2-IMF4, indicating that
the first extracted mode preserved the most useful information for the selected peak,
burst, temporal energy, and entropy descriptors. The PSD in Fig. 4 shows that class
differences within IMF1 were distributed across the displayed frequency range and were
most apparent in the lower-frequency portion of IMF1. This supports the role of IMF1
as an adaptive EHG representation that can capture discriminative oscillatory structure
without requiring a predefined uterine frequency band. This interpretation is consistent
with recent EHG work emphasizing the value of interpretable low-frequency EHG
information for premature birth prediction [30].
Relative to the filtered time-domain baseline, IMF1 produced numerically higher
mean accuracy, F1-score, balanced accuracy, MCC, ROC-AUC, and AP. Because the
comparison was performed within the same dataset without an independent test cohort
or paired inferential analysis, these differences are interpreted descriptively rather than
as evidence that EMD is universally superior to the filtered time-domain representation.
Effect of segmentation strategy
The comparison between dataset-provided annotated intervals and fixed-window
segmentation addresses whether useful recording-level information is restricted to
manually identified intervals. In this dataset, fixed 3-minute windows yielded higher
mean recording-level performance than the annotated-interval strategy, indicating that
useful classification information was not confined to annotated contractions.
This finding is consistent with previous TPEHGT work showing that dummy
(non-contraction) intervals can also contain discriminative information [24]. However,
the present comparison does not isolate a single physiological cause for the improvement.
Fixed windows also provide uniform segment duration, a larger and more regular set of
August 19, 2026 27/33

segments, different opportunities for maximum-score aggregation, and potentially
different exposure to transient artifacts. The result should therefore be interpreted as
support for annotation-independent fixed-window analysis rather than proof that
inter-contraction physiology alone caused the performance difference.
The fixed-window strategy also offers practical advantages for future monitoring
systems. It provides a uniform segment length, increases the amount of usable training
data, and avoids dependence on manual contraction annotation. These properties make
fixed-window analysis well suited to recording-level risk assessment, where the objective
is to summarize the electrophysiological state of the uterus across a continuous
recording rather than to classify isolated contractions alone. The present findings
therefore support fixed-window IMF1 analysis as the preferred segmentation strategy
within the proposed framework.
Methodological implications for future PTB risk assessment
The immediate implication is methodological. Non-overlapping fixed windows provide a
standardized, annotation-independent route from continuous EHG recordings to
recording-level classification, while the matched filtered-signal comparison helps
distinguish the effect of signal representation from differences introduced by the feature
set or classifier. The compact feature families also provide a testable multi-scale
hypothesis: relatively homogeneous low-amplitude events may occur within a more
complex whole-segment organization. These properties make the framework suitable for
evaluation in larger linked cohorts; they do not yet establish a calibrated PTB risk
score, a clinical decision threshold, or incremental value over obstetric assessment.
Model behavior
Tree-based ensemble models, particularly RF, GB, and CB, generally outperformed the
linear and probabilistic models. This model ranking is consistent with nonlinear effects
or interactions between burst, temporal-energy, and entropy descriptors in their
relationship with PTB class labels. The weak performance of a single decision tree,
compared with the ensembles, also suggests that averaging or boosting helped stabilize
predictions in the 42-dimensional feature space.
This model behavior supports the use of conventional feature-based ensemble models
as a practical middle ground between simple linear classifiers and fully latent end-to-end
deep-learning approaches. Because the models operate on explicit, physiologically
understandable feature families, their behavior can be examined post hoc through
grouped permutation importance, providing a more auditable prediction framework
than an entirely latent representation. RF provided the strongest overall balance
between classification performance and this form of model auditability in the proposed
framework. The grouped reliance analysis therefore provides model-level evidence of
which feature families contribute to prediction, rather than a physiological causal
explanation or an explanation of individual patient-level decisions. This emphasis on
retaining traceable signal features and examining model reliance aligns with recent calls
for more explainable EHG-based prediction methods rather than increasingly complex
black-box models [28–30].
Methodological strengths
A principal methodological strength is the matched comparison of IMF1 and the filtered
time-domain signal under identical segmentation, feature definitions, classifiers,
aggregation, and recording-level evaluation. This isolates the effect of representation
more directly than comparisons across pipelines with different features or validation
August 19, 2026 28/33

procedures. In addition, all segments from one recording remained within the same
outer fold, predictions were aggregated to the recording level, and no oversampling was
used. These choices directly address avoidable segment leakage and synthetic-sample
leakage. A further analytical strength is the joint use of recording-level effect directions
and grouped permutation importance, which provides complementary views of the
feature space: effect directions characterize how signal properties differ between the
classes, while grouped permutation importance assesses the extent to which the trained
models rely on each feature family.
Limitations
This exploratory analysis used 26 recordings originating from 18 pregnancies and no
external cohort. Recording-grouped cross-validation prevented fixed windows or
annotated intervals from the same recording from crossing the outer split, but the
public release does not provide a defensible recording-to-pregnancy key; residual
dependence between multiple recordings from the same pregnancy therefore cannot be
excluded. Repeated cross-validation assessed the stability of performance across
different data partitions, but it does not overcome the limited number of independent
pregnancies in the dataset.
Model scores were not calibrated or evaluated for clinical utility or incremental value
over obstetric predictors. The feature distributions and grouped importance analyses
are descriptive and do not establish physiological mechanisms or standalone biomarkers.
These limitations position the findings as methodological evidence and hypothesis
generation for larger cohorts with explicit participant linkage.
Future validation
Future work should evaluate the prespecified pipeline in larger external cohorts to
establish robustness and generalizability, with explicit participant linkage to enable
pregnancy-wise independent validation. The larger sample size would also allow
performance to be assessed within defined gestational-age windows and prediction
horizons. Sensitivity analyses should also examine the influence of proximity to delivery
and signal quality. Only after this stage should calibration, clinical utility, and
incremental value beyond gestational age, obstetric history, cervical length, or fetal
fibronectin be assessed.
Conclusion
This study evaluated an interpretable EMD-based framework for recording-level
term-versus-preterm classification from non-invasive EHG recordings. Using the public
TPEHGT dataset, the first four IMFs were evaluated within a common 42-feature
classification framework, with IMF1 yielding the highest mean performance among the
evaluated modes. Fixed non-overlapping 3-minute windows also yielded higher mean
recording-level performance than the dataset-provided annotated intervals, supporting
annotation-independent segmentation as a practical representation of both contraction
and inter-contraction EHG activity.
The best-observed configuration, a Random Forest using fixed-window IMF1
features, achieved mean accuracy of 0.8308, F1-score of 0.7969, balanced accuracy of
0.8308, MCC of 0.6998, ROC-AUC of 0.8157, and average precision of 0.8877. Relative
to the matched filtered time-domain representation, IMF1 produced numerically higher
mean values across all six reported metrics. Recording-level feature distributions showed
a preterm-associated pattern of more frequent, smaller, and more regularly spaced
August 19, 2026 29/33

|     |     | peak-like events, | lower temporal-energy |          | measures,   | and higher   | entropy, while |     |
| --- | --- | ----------------- | --------------------- | -------- | ----------- | ------------ | -------------- | --- |
|     |     | temporal-energy   | descriptors           | produced | the largest | mean grouped | permutation    |     |
importance.
The principal contribution of this work is therefore a transparent comparison linking
signal-adaptive decomposition, annotation-independent segmentation, traceable feature
families, and recording-level control of segment leakage. The findings support EMD and
fixed-window analysis as testable methodological choices for term-versus-preterm EHG
classification rather than as a clinically validated risk model. Validation in larger
external cohorts with explicit pregnancy linkage and defined prediction horizons is
|     |     | required before | clinical interpretation. |     |     |     |     |     |
| --- | --- | --------------- | ------------------------ | --- | --- | --- | --- | --- |
Data availability
The TPEHGT dataset used in this study is publicly available from PhysioNet, version
1.0.0, DOI: https://doi.org/10.13026/C2166R. The analysis code required to
reproduce the reported analyses, including feature extraction, model training,
cross-validation, recording-level aggregation, metric calculation, and figure generation, is
available at https://github.com/SenithJayakody/tpehgt-preterm-emd.git.
References
1. Ohuma EO, Moller AB, Bradley E, Chakwera S, Hussain-Alkhateeb L, Lewin A,
|     |     | et al. | National, regional, | and | global estimates | of preterm | birth in 2020, | with |
| --- | --- | ------ | ------------------- | --- | ---------------- | ---------- | -------------- | ---- |
trends from 2010: a systematic analysis. The Lancet. 2023;402(10409):1261-71.
doi:10.1016/S0140-6736(23)00878-4.
2. World Health Organization. Preterm birth; 2023. Accessed 7 May 2026. Available
from:
https://www.who.int/news-room/fact-sheets/detail/preterm-birth.
3. World Health Organization. Newborn mortality; 2024. Accessed 30 June 2026.
https://www.who.int/news-room/fact-sheets/detail/newborn-mortality.
|     |     | 4. UNICEF. | Neonatal | mortality; | 2026. Accessed | 1 July 2026. |     |     |
| --- | --- | ---------- | -------- | ---------- | -------------- | ------------ | --- | --- |
https://data.unicef.org/topic/child-survival/neonatal-mortality/.
5. Centers for Disease Control and Prevention. Preterm Birth; 2024. Accessed 30
|     |     | June 2026. | https: |     |     |     |     |     |
| --- | --- | ---------- | ------ | --- | --- | --- | --- | --- |
//www.cdc.gov/maternal-infant-health/preterm-birth/index.html.
6. World Health Organization. WHO Recommendation on Tocolytic Therapy for
Improving Preterm Birth Outcomes. Geneva: World Health Organization; 2022.
7. Committee on Obstetric Practice. Committee Opinion No. 713: Antenatal
|     |     | Corticosteroid      | Therapy | for Fetal                         | Maturation. | Obstetrics | & Gynecology. |     |
| --- | --- | ------------------- | ------- | --------------------------------- | ----------- | ---------- | ------------- | --- |
|     |     | 2017;130(2):e102-9. |         | doi:10.1097/AOG.0000000000002237. |             |            |               |     |
8. National Institute for Health and Care Excellence. Preterm labour and birth;
2015. NICE guideline NG25, last updated 10 June 2022; Accessed 30 June 2026.
https://www.nice.org.uk/guidance/ng25.
9. Son M, Miller ES. Predicting preterm birth: Cervical length and fetal fibronectin.
Seminars in Perinatology. 2017;41(8):445-51. doi:10.1053/j.semperi.2017.08.002.
| August | 19, 2026 |     |     |     |     |     |     | 30/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | ----- |

|     |     | 10. Garfield | RE, | Maner | WL. | Physiology |     | and | electrical | activity | of  | uterine |     |
| --- | --- | ------------ | --- | ----- | --- | ---------- | --- | --- | ---------- | -------- | --- | ------- | --- |
contractions. Seminars in Cell and Developmental Biology. 2007;18(3):289-95.
doi:10.1016/j.semcdb.2007.05.004.
11. Lucovnik M, Kuon RJ, Chambliss LR, Maner WL, Shi SQ, Shi L, et al. Use of
uterine electromyography to diagnose term and preterm labor. Acta Obstetricia
|     |     | et Gynecologica |     | Scandinavica. |     |     | 2011;90(2):150-7. |     |     |     |     |     |     |
| --- | --- | --------------- | --- | ------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
doi:10.1111/j.1600-0412.2010.01031.x.
12. Buhimschi C, Boyle MB, Garfield RE. Electrical activity of the human uterus
|     |     | during      | pregnancy |                    | as recorded |     | from the                           | abdominal |     | surface. | Obstetrics |     | &   |
| --- | --- | ----------- | --------- | ------------------ | ----------- | --- | ---------------------------------- | --------- | --- | -------- | ---------- | --- | --- |
|     |     | Gynecology. |           | 1997;90(1):102-11. |             |     | doi:10.1016/S0029-7844(97)83837-9. |           |     |          |            |     |     |
13. Garcia-Casado J, Ye-Lin Y, Prats-Boluda G, Mas-Cabo J, Alberola-Rubio J,
|     |     | Perales       | A.  | Electrohysterography |     |             | in  | the diagnosis                 |     | of preterm |     | birth: a review. |     |
| --- | --- | ------------- | --- | -------------------- | --- | ----------- | --- | ----------------------------- | --- | ---------- | --- | ---------------- | --- |
|     |     | Physiological |     | Measurement.         |     | 2018;39(2). |     | doi:10.1088/1361-6579/aaad56. |     |            |     |                  |     |
14. Garfield RE, Sims S, Daniel EE. Gap junctions: their presence and necessity in
|     |     | myometrium |     | during | parturition. |     | Science. | 1977;198(4320):958-60. |     |     |     |     |     |
| --- | --- | ---------- | --- | ------ | ------------ | --- | -------- | ---------------------- | --- | --- | --- | --- | --- |
doi:10.1126/science.929182.
15. Aguilar HN, Mitchell BF. Physiological pathways and molecular mechanisms
regulating uterine contractility. Human Reproduction Update. 2010;16(6):725-44.
doi:10.1093/humupd/dmq016.
16. Garfield RE, Saade G, Buhimschi C, Buhimschi I, Shi L, Shi SQ, et al. Control
and Assessment of the Uterus and Cervix During Pregnancy and Labour. Human
Reproduction Update. 1998 Sep-Oct;4(5):673-95. doi:10.1093/humupd/4.5.673.
17. Garfield RE, Yallampalli C. Control of Myometrial Contractility and Labour. In:
|     |     | Chwalisz | K,  | Garfield | RE, | editors. | Basic | Mechanisms |     | Controlling |     | Term | and |
| --- | --- | -------- | --- | -------- | --- | -------- | ----- | ---------- | --- | ----------- | --- | ---- | --- |
Preterm Labour. vol. 7 of Ernst Schering Research Foundation Workshop. Berlin,
|     |     | Heidelberg, |     | New York: | Springer-Verlag; |     |     | 1993. | p.  | 1-29. |     |     |     |
| --- | --- | ----------- | --- | --------- | ---------------- | --- | --- | ----- | --- | ----- | --- | --- | --- |
18. Wolfs GM, van Leeuwen M. Electromyographic Observations on the Human
|     |     | Uterus | During | Labour. |     | Acta Obstetricia |     | et  | Gynecologica |     | Scandinavica. |     |     |
| --- | --- | ------ | ------ | ------- | --- | ---------------- | --- | --- | ------------ | --- | ------------- | --- | --- |
1979;90(suppl.):1-61.
19. Csapo AI. Force of Labour. In: Iffy L, Kaminetzky HA, editors. Principles and
Practice of Obstetrics and Perinatology. vol. 2. New York: John Wiley & Sons;
|     |     | 1981.             | p. 761-99. |                      |            |         |                                   |          |         |         |               |         |     |
| --- | --- | ----------------- | ---------- | -------------------- | ---------- | ------- | --------------------------------- | -------- | ------- | ------- | ------------- | ------- | --- |
|     |     | 20. Devedeux      | D,         | Marque               | C,         | Mansour | S,                                | Germain  | G,      | Duchene | J.            | Uterine |     |
|     |     | electromyography: |            |                      | A critical | review. |                                   | American | Journal |         | of Obstetrics | and     |     |
|     |     | Gynecology.       |            | 1993;169(6):1636-53. |            |         | doi:10.1016/0002-9378(93)90456-S. |          |         |         |               |         |     |
21. Li P, Huang Q, Wang L, Garfield RE, Liu H. Uterine Electrical Signals and
Cervical Dilation During the First Stage of Labor. Archives of Obstetrics and
|     |     | Gynecology. |     | 2022;3(1):47-52. |     | doi:10.33696/Gynaecology.3.028. |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | ---------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
22. Mas-Cabo J, Prats-Boluda G, Perales A, Garcia-Casado J, Alberola-Rubio J,
Ye-Lin Y. Uterine Electromyography for Discrimination of Labor Imminence in
Women with Threatened Preterm Labor under Tocolytic Treatment. Medical &
|     |     | Biological | Engineering |     | &   | Computing. |     | 2019;57(2):401-11. |     |     |     |     |     |
| --- | --- | ---------- | ----------- | --- | --- | ---------- | --- | ------------------ | --- | --- | --- | --- | --- |
doi:10.1007/s11517-018-1888-y.
| August | 19, 2026 |     |     |     |     |     |     |     |     |     |     |     | 31/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

|     |     | Fele-Zˇorˇz |     |     |     |     | Zˇ, |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
23. G, Kavˇsek G, Novak-Antoliˇc Jager F. A comparison of various linear
and non-linear signal processing techniques to separate uterine EMG records of
|     |     | term and   | pre-term           | delivery | groups. | Medical                        |     | & Biological | Engineering |     | &   |
| --- | --- | ---------- | ------------------ | -------- | ------- | ------------------------------ | --- | ------------ | ----------- | --- | --- |
|     |     | Computing. | 2008;46(9):911-22. |          |         | doi:10.1007/s11517-008-0350-y. |     |              |             |     |     |
24. Jager F, Libenˇsek S, Gerˇsak K. Characterization and automatic classification of
|     |     | preterm | and term | uterine | records. | PLOS | ONE. | 2018;13(8):e0202125. |     |     |     |
| --- | --- | ------- | -------- | ------- | -------- | ---- | ---- | -------------------- | --- | --- | --- |
doi:10.1371/journal.pone.0202125.
25. Fergus P, Cheung P, Hussain AJ, Al-Jumeily D, Dobbins C, Iram S. Prediction of
|     |     | Preterm            | Deliveries | from                              | EHG | Signals | Using | Machine | Learning. | PLOS | ONE. |
| --- | --- | ------------------ | ---------- | --------------------------------- | --- | ------- | ----- | ------- | --------- | ---- | ---- |
|     |     | 2013;8(10):e77154. |            | doi:10.1371/journal.pone.0077154. |     |         |       |         |           |      |      |
26. Alamedine D, Khalil M, Marque C. Comparison of Different EHG Feature
|     |     | Selection | Methods | for | the Detection |     | of Preterm | Labor. | Computational |     | and |
| --- | --- | --------- | ------- | --- | ------------- | --- | ---------- | ------ | ------------- | --- | --- |
Mathematical Methods in Medicine. 2013;2013:485684. doi:10.1155/2013/485684.
27. Romero-Morales H, Mun˜oz-Montes de Oca JN, Mora-Mart´ınez R, Mina-Paz Y,
Reyes-Lagos JJ. Enhancing classification of preterm-term birth using continuous
|     |     | wavelet | transform | and | entropy-based |     | methods | of electrohysterogram |     |     | signals. |
| --- | --- | ------- | --------- | --- | ------------- | --- | ------- | --------------------- | --- | --- | -------- |
Frontiers in Endocrinology. 2023;13:1035615. doi:10.3389/fendo.2022.1035615.
28. Goldsztejn U, Nehorai A. Predicting preterm births from electrohysterogram
|     |     | recordings | via | deep learning. |     | PLOS ONE. | 2023;18(5):e0285219. |     |     |     |     |
| --- | --- | ---------- | --- | -------------- | --- | --------- | -------------------- | --- | --- | --- | --- |
doi:10.1371/journal.pone.0285219.
29. Fischer AM, Vullings R, Gommers JSM, Oei SG, Bergmans JWM, Mischi M.
End-to-end learning with interpretation on electrohysterography data to predict
|     |     | preterm | birth. | Computers | in  | Biology | and Medicine. | 2023;158:106846. |     |     |     |
| --- | --- | ------- | ------ | --------- | --- | ------- | ------------- | ---------------- | --- | --- | --- |
doi:10.1016/j.compbiomed.2023.106846.
30. Pirnar Z, Jager F, Gersak K. Peak amplitude of the normalized power spectrum
|     |     | of the electromyogram |              |     | of the | uterus in | the low                   | frequency | band | is an | effective |
| --- | --- | --------------------- | ------------ | --- | ------ | --------- | ------------------------- | --------- | ---- | ----- | --------- |
|     |     | predictor             | of premature |     | birth. | PLOS      | ONE. 2024;19(9):e0308797. |           |      |       |           |
doi:10.1371/journal.pone.0308797.
31. Vandewiele G, Dehaene I, Kovacs G, Sterckx L, Janssens O, Ongenae F, et al.
Overly optimistic prediction results on imbalanced data: A case study of flaws
and benefits when applying over-sampling. Artificial Intelligence in Medicine.
|     |     | 2021;111:101987. |     | doi:10.1016/j.artmed.2020.101987. |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
32. Huang NE, Shen Z, Long SR, Wu MC, Shih HH, Zheng Q, et al. The empirical
mode decomposition and the Hilbert spectrum for nonlinear and non-stationary
|     |     | time series   | analysis. | Proceedings |                 | of the | Royal     | Society                | of London | Series | A:  |
| --- | --- | ------------- | --------- | ----------- | --------------- | ------ | --------- | ---------------------- | --------- | ------ | --- |
|     |     | Mathematical, |           | Physical    | and Engineering |        | Sciences. | 1998;454(1971):903-95. |           |        |     |
doi:10.1098/rspa.1998.0193.
33. Pollard T, Moody BE, Lehman LwH, Gow BJ, Fernandes C, Xie C, et al.
|     |     | PhysioNet     | as a                            | global | platform | for biomedical |     | research. | Nature | Health. |     |
| --- | --- | ------------- | ------------------------------- | ------ | -------- | -------------- | --- | --------- | ------ | ------- | --- |
|     |     | 2026;1:792-5. | doi:10.1038/s44360-026-00096-z. |        |          |                |     |           |        |         |     |
34. Welch P. The use of fast Fourier transform for the estimation of power spectra: A
|     |     | method       | based | on time | averaging             | over | short, | modified         | periodograms. |     | IEEE |
| --- | --- | ------------ | ----- | ------- | --------------------- | ---- | ------ | ---------------- | ------------- | --- | ---- |
|     |     | Transactions | on    | Audio   | and Electroacoustics. |      |        | 1967;15(2):70-3. |               |     |      |
doi:10.1109/TAU.1967.1161901.
| August | 19, 2026 |     |     |     |     |     |     |     |     |     | 32/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

35. Lammers WJEP. The electrical activities of the uterus during pregnancy.
|     |     | Reproductive     |     | Sciences.    | 2013;20(2):182-9. |       |                | doi:10.1177/1933719112446082. |     |                 |     |     |     |
| --- | --- | ---------------- | --- | ------------ | ----------------- | ----- | -------------- | ----------------------------- | --- | --------------- | --- | --- | --- |
|     |     | 36. Janjarasjitt | S.  | Preterm-Term |                   | Birth | Classification |                               |     | Using EMD-Based |     |     |     |
Time-Domain Features of Single-Channel Electrohysterogram Data. Physical and
|     |     | Engineering | Sciences |     | in Medicine. |     | 2021 | Dec;44(4):1151-9. |     |     |     |     |     |
| --- | --- | ----------- | -------- | --- | ------------ | --- | ---- | ----------------- | --- | --- | --- | --- | --- |
doi:10.1007/s13246-021-01051-w.
37. Janjarasjitt S. Comparison of Wavelet-Based Decomposition and Empirical Mode
Decomposition of Electrohysterogram Signals for Preterm Birth Classification.
|     |     | ETRI Journal. |     | 2022;44(5):826-36. |     |     | doi:10.4218/etrij.2021-0220. |     |     |     |     |     |     |
| --- | --- | ------------- | --- | ------------------ | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
38. Mohammadi Far S, Beiramvand M, Shahbakhti M, Augustyniak P. Prediction of
Preterm Delivery from Unbalanced EHG Database. Sensors. 2022;22(4):1507.
doi:10.3390/s22041507.
39. Mohammadi Far S, Beiramvand M, Shahbakhti M, Augustyniak P. Prediction of
|     |     | Preterm     | Labor  | from     | the       | Electrohysterogram |     |           | Signals                | Based  | on Different |     |     |
| --- | --- | ----------- | ------ | -------- | --------- | ------------------ | --- | --------- | ---------------------- | ------ | ------------ | --- | --- |
|     |     | Gestational | Weeks. |          | Sensors.  | 2023;23(13):5965.  |     |           | doi:10.3390/s23135965. |        |              |     |     |
|     |     | 40. Kaiser  | JF. On | a simple | algorithm |                    | to  | calculate | the                    | energy | of a signal. |     | In: |
International Conference on Acoustics, Speech, and Signal Processing; 1990. p.
|     |     | 381-4. | doi:10.1109/ICASSP.1990.115702. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
41. Bandt C, Pompe B. Permutation entropy: A natural complexity measure for time
|     |     | series. | Physical | Review | Letters. |     | 2002;88(17):174102. |     |     |     |     |     |     |
| --- | --- | ------- | -------- | ------ | -------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
doi:10.1103/PhysRevLett.88.174102.
42. Richman JS, Moorman JR. Physiological time-series analysis using approximate
|     |     | entropy     | and         | sample | entropy.              | American |     | Journal | of  | Physiology-Heart |     | and |     |
| --- | --- | ----------- | ----------- | ------ | --------------------- | -------- | --- | ------- | --- | ---------------- | --- | --- | --- |
|     |     | Circulatory | Physiology. |        | 2000;278(6):H2039-49. |          |     |         |     |                  |     |     |     |
doi:10.1152/ajpheart.2000.278.6.H2039.
43. Prokhorenkova L, Gusev G, Vorobev A, Dorogush AV, Gulin A. CatBoost:
unbiased boosting with categorical features. In: Advances in Neural Information
|     |     | Processing | Systems. |     | vol. | 31; 2018. | p.  | 6638-48. |     |     |     |     |     |
| --- | --- | ---------- | -------- | --- | ---- | --------- | --- | -------- | --- | --- | --- | --- | --- |
44. Chicco D, Jurman G. The advantages of the Matthews correlation coefficient
|     |     | (MCC)     | over F1       | score | and | accuracy                       | in  | binary | classification |     | evaluation. |     | BMC |
| --- | --- | --------- | ------------- | ----- | --- | ------------------------------ | --- | ------ | -------------- | --- | ----------- | --- | --- |
|     |     | Genomics. | 2020;21(1):6. |       |     | doi:10.1186/s12864-019-6413-7. |     |        |                |     |             |     |     |
45. Ren P, Yao S, Li J, Valdes-Sosa PA, Kendrick KM. Improved prediction of
|     |     | preterm          | delivery | using    | empirical |      | mode | decomposition        |     | analysis | of  | uterine |     |
| --- | --- | ---------------- | -------- | -------- | --------- | ---- | ---- | -------------------- | --- | -------- | --- | ------- | --- |
|     |     | electromyography |          | signals. |           | PLOS | ONE. | 2015;10(7):e0132116. |     |          |     |         |     |
doi:10.1371/journal.pone.0132116.
46. Cui J, Zhang X, Li X, Luo X, Chen X, Yin Z. Preterm birth prediction from
electrohysterogram using multivariate empirical mode decomposition. Medical &
|     |     | Biological | Engineering |     | &   | Computing. |     | 2025 | Jun;63(6):1867-80. |     |     |     |     |
| --- | --- | ---------- | ----------- | --- | --- | ---------- | --- | ---- | ------------------ | --- | --- | --- | --- |
doi:10.1007/s11517-025-03293-2.
| August | 19, 2026 |     |     |     |     |     |     |     |     |     |     |     | 33/33 |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
---- END DOCUMENT ----
