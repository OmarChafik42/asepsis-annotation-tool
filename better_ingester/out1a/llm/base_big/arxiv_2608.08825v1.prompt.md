Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Hybrid Neural-Classical Correction for Frozen Time
Series Foundation Models: A Comprehensive
Ablation Study on High-Frequency Stock Prediction
1st Kasun Dewage 2nd Suranadi De Silva 3rd Shankhadeep Mondal
Dept. of Mathematics Dept. of Computer Science Dept. of Mathematics
University of Central Florida University of Central Florida University of Central Florida
Orlando, FL, USA Orlando, FL, USA Orlando, FL, USA
KasunTharuka.Dewage@ucf.edu su966204@ucf.edu shankhadeep.mondal@ucf.edu
informative predictions. This gap between general capability
Abstract—Foundation models for time series forecasting and domain-specific performance motivates investigation into
demonstrateimpressivezero-shotgeneralizationbutoftenunder-
effective adaptation strategies.
perform on specialized domains such as high-frequency finance.
We focus on a challenging prediction task: forecasting
We present a comprehensive study of hybrid neural-classical
stock returns during the opening trading hour (9:30–10:30
correction for adapting frozen TimesFM (200M parameters) to
stockreturnpredictionduringthevolatileopeningtradinghour. AM), when markets exhibit high volatility as they digest
We compare two neural correction architectures—AttnCorrect overnight information [9]. Premarket trading data (4:30–9:29
(multi-head self-attention, ∼471K parameters) and GatedLinear AM) provides potentially predictive signals, but extracting
(low-rank bilinear projection with gating, ∼49K parameters)—
useful information requires sophisticated processing.
eachaugmentedwithRandomForestresiduallearning.Through
Rather than fine-tuning the foundation model—
systematic ablation across 10 major technology stocks (NVDA,
MSFT,AAPL,GOOG,GOOGL,AMZN,META,AVGO,TSLA, computationally expensive and prone to overfitting with
NFLX)spanning2milliondatapoints,werevealcriticalinsights: limited domain data—we investigate correction-based
(1) The hybrid neural-classical approach achieves 0.597 pooled adaptation: keeping TimesFM completely frozen while
correlationand6.4×meanper-daycorrelationimprovementover
training lightweight modules to correct its outputs. Critically,
frozenTimesFM;(2)Classicalresiduallearning(RandomForest)
we employ a hybrid neural-classical design combining
provides the largest single-component contribution , matching
or exceeding the neural correction component; (3) Simpler neural correction with Random Forest [3] residual learning.
neuralarchitecturessurprisinglyoutperformcomplexoneswhen We compare two neural correction architectures represent-
classicalresiduallearningisremoved;(4)Self-attentionprovides ing different design philosophies:
the largest neural-only contribution. GatedLinear+RF achieves
best overall performance with 9× fewer neural parameters than • AttnCorrect:Multi-headself-attention[22]overpremar-
ketsequences,enablingflexibletemporalpatternlearning
AttnCorrect+RF. We report three complementary correlation
metrics—mean per-day, cross-day cumulative, and pooled—to (∼471K trainable parameters)
provide a complete picture of predictive quality. Our results • GatedLinear: Low-rank bilinear projection [21] with
providepracticalguidance:effectivefoundationmodeladaptation learned gating for extreme parameter efficiency (∼49K
requires careful integration of neural and classical components,
trainable parameters)
with classical methods playing a crucial complementary role.
Index Terms—Foundation Models, Time Series Forecasting, Through comprehensive ablation across 10 major technol-
Hybrid Methods, Neural-Classical Integration, Random Forest, ogy stocks with over 2 million data points, we address the
Attention Mechanisms, Stock Prediction, Model Adaptation critical question:
I. INTRODUCTION What components matter most when adapting frozen
foundation models, and how should neural and classical
Foundation models have revolutionized machine learning
methods be integrated?
across domains. Recent extensions to time series—including
TimesFM[5],Chronos[1],andLag-Llama[20]—demonstrate Our key contributions and findings:
that models pretrained on billions of time points can achieve 1) A hybrid neural-classical framework achieving 6.4×
strong zero-shot generalization across diverse forecasting meanper-daycorrelationimprovementand0.597pooled
tasks. correlation over frozen TimesFM
However, zero-shot performance does not guarantee 2) Comprehensive ablation across 12 model variants
domain-specific accuracy. When applying TimesFM to high- revealing component contributions
frequency stock prediction, we observe near-zero mean per- 3) Evidence that classical residual learning matches or
day correlation (0.059) with actual returns—essentially un- exceeding neural correction
©2026IEEE.Personaluseofthismaterialispermitted.PermissionfromIEEEmustbeobtainedforallotheruses,inanycurrentorfuturemedia,includingreprinting/republishingthisma-
terialforadvertisingorpromotionalpurposes,creatingnewcollectiveworks,forresaleorredistributiontoserversorlists,orreuseofanycopyrightedcomponentofthisworkinotherworks.
6202
guA
9
]GL.sc[
1v52880.8062:viXra

4) The surprising finding that simpler neural architec- for tabular data [8], particularly when feature engineering
tures outperform complex ones when classical com- captures domain knowledge.
ponents are removed Random Forests [3] offer several advantages for residual
5) Per-stock analysis across 10 major technology stocks learning: robustness to outliers, natural handling of feature
with detailed performance breakdowns interactions,andstrongperformancewithlimitedtrainingdata.
6) Practical guidance: GatedLinear+RF achieves best per- Ourworkprovidesempiricalevidenceforthevalueofneural-
formance with 9× fewer neural parameters classical integration in foundation model adaptation.
| Open Science    |     | Statement:                                 |     | Our | code | and results | are pub- |              |             |              |     |          |            |     |             |     |
| --------------- | --- | ------------------------------------------ | --- | --- | ---- | ----------- | -------- | ------------ | ----------- | ------------ | --- | -------- | ---------- | --- | ----------- | --- |
|                 |     |                                            |     |     |      |             |          | D. Attention | Mechanisms  |              | and | Bilinear | Models     |     |             |     |
| licly available |     | at https://github.com/Kasun-Dewage/Hybrid_ |     |     |      |             |          |              |             |              |     |          |            |     |             |     |
|                 |     |                                            |     |     |      |             |          | The          | Transformer | architecture |     | [22]     | introduced |     | scaled dot- |     |
Neural2026.gittofacilitatereproducibilityandfurtherresearch
|              |         |             |      |         |             |                  |             | product       | attention, | enabling |         | flexible  | modeling | of   | long-range |     |
| ------------ | ------- | ----------- | ---- | ------- | ----------- | ---------------- | ----------- | ------------- | ---------- | -------- | ------- | --------- | -------- | ---- | ---------- | --- |
| in this area | upon    | publication |      | of this | manuscript. |                  | All experi- |               |            |          |         |           |          |      |            |     |
|              |         |             |      |         |             |                  |             | dependencies. |            | For time | series, | attention | has      | been | adapted    | in  |
| ments use    | a fixed | random      | seed | of      | 42 for      | reproducibility. |             |               |            |          |         |           |          |      |            |     |
variousways:theTemporalFusionTransformer[16]combines
II. RELATEDWORK LSTM encoders with multi-head attention for interpretable
|               |     |        |          |        |     |     |     | forecasting, | while         | Informer |             | [24] introduces |     | ProbSparse | atten- |     |
| ------------- | --- | ------ | -------- | ------ | --- | --- | --- | ------------ | ------------- | -------- | ----------- | --------------- | --- | ---------- | ------ | --- |
| A. Foundation |     | Models | for Time | Series |     |     |     |              |               |          |             |                 |     |            |        |     |
|               |     |        |          |        |     |     |     | tion for     | computational |          | efficiency. |                 |     |            |        |     |
TimesFM [5] is a decoder-only transformer with 200M Bilinear models capture multiplicative interactions between
| parameters, | pretrained |     | on over | 100 | billion | time | points from |          |                |     |          |         |      |         |        |     |
| ----------- | ---------- | --- | ------- | --- | ------- | ---- | ----------- | -------- | -------------- | --- | -------- | ------- | ---- | ------- | ------ | --- |
|             |            |     |         |     |         |      |             | features | [21]. Low-rank |     | bilinear | pooling | [14] | reduces | compu- |     |
Google Trends, Wikipedia pageviews, and synthetic data. The tationviamatrixfactorization.Weapplybilinearprojectionto
model uses input patching with patch length 32 and achieves compresshigh-dimensionalpremarketsequenceswithminimal
| strong zero-shot |     | performance |     | on standard |     | benchmarks | includ- |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | ----------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameters.
| ing ETT, | Weather, | and | Electricity |     | datasets. |     |     |     |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Chronos [1] takes a different approach, tokenizing time E. Financial Time Series Prediction
series values into discrete bins and training T5-style encoder- Despiteefficientmarkethypothesisarguments[6],empirical
decoder models [19]. This enables the use of language mod- evidencesupportsshort-termpredictabilityduringinformation
eling techniques for time series. Lag-Llama [20] adapts the asymmetryperiods.DeeplearningapproachesusingLSTM[7]
LLaMA architecture with lag-based tokenization for proba- and attention mechanisms have shown promise for financial
bilistic forecasting, demonstrating that decoder-only architec- forecasting. The opening trading hour exhibits particularly
tures can effectively model temporal dependencies. high volatility and potential predictability as markets process
While these models generalize impressively to standard overnight information [9].
benchmarks,domainadaptationtospecializedapplicationslike
|                |     |         |         |             |     |     |               |     |     | III. | METHODOLOGY |     |     |     |     |     |
| -------------- | --- | ------- | ------- | ----------- | --- | --- | ------------- | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- |
| high-frequency |     | finance | remains | challenging |     | due | to the unique |     |     |      |             |     |     |     |     |     |
statistical properties of financial time series. A. Problem Setting
|              |       |            |     |     |     |     |     | Let X(pm) |            | ∈ RT×F | denote | the  | premarket | sequence | with |     |
| ------------ | ----- | ---------- | --- | --- | --- | --- | --- | --------- | ---------- | ------ | ------ | ---- | --------- | -------- | ---- | --- |
| B. Efficient | Model | Adaptation |     |     |     |     |     |           |            |        |        |      |           |          |      |     |
|              |       |            |     |     |     |     |     | T =300    | one-minute | bars   | and    | F =7 | features: |          |      |     |
Parameter-efficient fine-tuning has been extensively studied Normalized OHLC prices (4 features)
•
| for large     | language | models.   |          | LoRA  | [13]              | introduces | low-rank |                   |            |          |             |             |     |     |     |     |
| ------------- | -------- | --------- | -------- | ----- | ----------------- | ---------- | -------- | ----------------- | ---------- | -------- | ----------- | ----------- | --- | --- | --- | --- |
|               |          |           |          |       |                   |            |          | • Log-transformed |            |          | volume      | (1 feature) |     |     |     |     |
| decomposition |          | of weight | updates, |       | training          | only       | W + BA   |                   |            |          |             |             |     |     |     |     |
|               |          |           |          |       |                   |            |          | • Bar-to-bar      |            | momentum |             | (1 feature) |     |     |     |     |
| whereB∈Rd×r   |          | andA∈Rr×k |          |       |                   |            |          |                   |            |          |             |             |     |     |     |     |
|               |          |           |          | withr | ≪min(d,k).Adapter |            |          | Intrabar          | volatility |          | (1 feature) |             |     |     |     |     |
•
| layers [12]  | insert    | small  | bottleneck   |            | modules          |           | between trans- |             |        |             |        |                |            |         |          |     |
| ------------ | --------- | ------ | ------------ | ---------- | ---------------- | --------- | -------------- | ----------- | ------ | ----------- | ------ | -------------- | ---------- | ------- | -------- | --- |
|              |           |        |              |            |                  |           |                | Given       | frozen | foundation  |        | model          | prediction | yˆ(tfm) | ∈        | RH  |
| former       | layers.   | Prefix | tuning       | [15]       | prepends         | learnable | tokens         |             |        |             |        |                |            |         |          |     |
|              |           |        |              |            |                  |           |                | for horizon | H      | =60 minutes |        | and multiscale |            | summary | features |     |
| to the input | sequence. |        |              |            |                  |           |                |             |        |             |        |                |            |         |          |     |
|              |           |        |              |            |                  |           |                | m∈R21,      | we     | learn a     | hybrid | correction:    |            |         |          |     |
| These        | methods   | modify | model        | internals, |                  | requiring | access         | to          |        |             |        |                |            |         |          |     |
| architecture | details   | and    | intermediate |            | representations. |           | Our ap-        |             |        |             |        |                |            |         |          |     |
proach operates externally through output correction, treating yˆ =yˆ(tfm)+∆y (X(pm),m,yˆ(tfm))+∆y (f )
|                |     |       |            |      |      |         |            |     |           | neural |                    |     |           | RF                | summary            |           |
| -------------- | --- | ----- | ---------- | ---- | ---- | ------- | ---------- | --- | --------- | ------ | ------------------ | --- | --------- | ----------------- | ------------------ | --------- |
|                |     |       |            |      |      |         |            |     | (cid:124) |        | (cid:123)(cid:122) |     | (cid:125) | (cid:124)         | (cid:123)(cid:122) | (cid:125) |
| the foundation |     | model | as a black | box. | This | enables | adaptation |     |           |        |                    |     |           |                   |                    |           |
|                |     |       |            |      |      |         |            |     |           |        | Neuralcorrection   |     |           | Classicalresidual |                    |           |
without architectural knowledge and avoids potential instabil- (1)
ities from modifying pretrained weights. The foundation model remains completely frozen through-
|                 |                  |     |        |          |      |           |         | out; only | the correction |     | modules   | are | trained. |     |     |     |
| --------------- | ---------------- | --- | ------ | -------- | ---- | --------- | ------- | --------- | -------------- | --- | --------- | --- | -------- | --- | --- | --- |
| C. Hybrid       | Neural-Classical |     |        | Methods  |      |           |         |           |                |     |           |     |          |     |     |     |
|                 |                  |     |        |          |      |           |         | B. Hybrid | Correction     |     | Framework |     |          |     |     |     |
| The integration |                  | of  | neural | networks | with | classical | machine |           |                |     |           |     |          |     |     |     |
learning methods has shown success across domains. In fore- Figure 1 illustrates the complete hybrid neural-classical
|          |        |            |     |           |        |     |               | correction | framework |     | shared | by both | architectures. |     |     |     |
| -------- | ------ | ---------- | --- | --------- | ------ | --- | ------------- | ---------- | --------- | --- | ------ | ------- | -------------- | --- | --- | --- |
| casting, | hybrid | approaches |     | combining | neural |     | networks with |            |           |     |        |         |                |     |     |     |
statistical methods often outperform pure neural approaches Both architectures share these components:
[18]. Recent work demonstrates that gradient boosting and TimesFM backbone: Frozen 200M-parameter founda-
•
| RandomForestsremainhighlycompetitivewithdeeplearning |     |     |     |     |     |     |     | tion | model |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |

|                 |     |     |                 |     |     |                    |       | D. GatedLinear: |               | Bilinear-Gated |             | Correction |              |              |           |
| --------------- | --- | --- | --------------- | --- | --- | ------------------ | ----- | --------------- | ------------- | -------------- | ----------- | ---------- | ------------ | ------------ | --------- |
| ContextSequence |     |     | PremarketTensor |     |     | MultiscaleFeatures |       |                 |               |                |             |            |              |              |           |
| (Prevday+PM)    |     |     | X(pm)∈R300×7    |     |     |                    | m∈R21 |                 |               |                |             |            |              |              |           |
|                 |     |     |                 |     |     |                    |       | Figure 3        | presents      | the            | GatedLinear |            | architecture |              | with only |
|                 |     |     |                 |     |     |                    |       | ∼49K trainable  | parameters—9× |                |             | fewer      | than         | AttnCorrect. |           |
TimesFM(200M) NeuralCorrector 1) Low-Rank Bilinear Projection: Instead of attention over
FrozenFoundation(AttnCorrectorGatedLinear)
NEZORF DENIART the full sequence, we compress the premarket tensor through
|     |             |                  |              |     |     |     |     | learned projection |          | matrices:       |      |          |          |           |          |
| --- | ----------- | ---------------- | ------------ | --- | --- | --- | --- | ------------------ | -------- | --------------- | ---- | -------- | -------- | --------- | -------- |
|     | yˆ(tfm)∈R60 |                  | ∆yneural∈R60 |     |     |     |     |                    |          |                 |      |          |          |           |          |
|     |             |                  |              |     |     |     |     |                    |          | Z=V⊤X(pm)U∈R8×4 |      |          |          |           | (7)      |
|     |             | yˆ(tfm)+∆yneural |              |     |     |     |     | V                  | ∈ R300×8 |                 |      |          |          |           |          |
|     |             |                  |              |     |     |     |     | where              |          | projects        |      | the      | temporal | dimension | and      |
|     |             |                  |              |     |     |     |     | U∈R7×4             | projects | features.       | This | bilinear |          | form [21] | captures |
RandomForest +0.16Corr interactions between temporal positions and feature channels
Classical
250trees,depth12
|     |     |     |     |     | Residual |     |     | with only    | 300×8+7×4=2,428 |     |     |                | parameters. |        |               |
| --- | --- | --- | --- | --- | -------- | --- | --- | ------------ | --------------- | --- | --- | -------------- | ----------- | ------ | ------------- |
|     |     |     |     |     |          |     |     | The temporal | projection      |     | V   | is initialized |             | with a | slight linear |
FinalPrediction trendtoencouragelearningoftemporalpatterns.TheresultZ
yˆ final∈R60
z∈R32.
|     |     |     |     |     |     |     |     | is flattened | to  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Fig. 1: Hybrid Neural-Classical Correction Framework. 2) Gated Correction: Features are concatenated:
Both architectures share this pipeline: frozen TimesFM pro- [z;m;yˆ(tfm)] ∈ R113 and encoded through a two-layer
vides base predictions, a trainable neural corrector generates MLP. The gating mechanism, inspired by LSTM [11] and
∆y , and Random Forest learns residual patterns. Our GRU [4] gates, computes:
neural
| ablation | reveals | the | classical | component |     | (RF, | highlighted) |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | --------- | --------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
)∈[0,1]60
|     |     |     |     |     |     |     |     |     | g=σ(W |     | g h+b | g   |     |     | (8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- |
providesnearlyequallyorexceedingtotheneuralcomponent.
|              |     |          |     |          |     |             |          |     |     | r=W | h+b    | ∈R60 |     |     | (9)  |
| ------------ | --- | -------- | --- | -------- | --- | ----------- | -------- | --- | --- | --- | ------ | ---- | --- | --- | ---- |
|              |     |          |     |          |     |             |          |     |     |     | r      | r    |     |     |      |
|              |     |          |     | m:       |     |             |          |     |     | ∆y  | neural | =g⊙r |     |     | (10) |
| • Multiscale |     | features |     | Returns, |     | volatility, | and vol- |     |     |     |        |      |     |     |      |
ume computed over 5/15/30/60-minute windows plus The gate g controls correction magnitude per time step,
overnight gap (21 dimensions total) allowing the model to selectively correct when confident.
| • Random |     | Forest  | residual: | 250       | trees,     | max depth | 12, min   |             |         |     |     |     |     |     |     |
| -------- | --- | ------- | --------- | --------- | ---------- | --------- | --------- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
|          |     |         |           |           |            |           |           | E. Training | Details |     |     |     |     |     |     |
| samples  |     | leaf 3, | trained   | on neural | correction |           | residuals |             |         |     |     |     |     |     |     |
Directional loss: L = L +0.3L +0.2L to All experiments use a fixed random seed of 42 across
| •               |     |                 |           | MSE        |     | dir | cum |                       |     |        |          |        |         |        |           |
| --------------- | --- | --------------- | --------- | ---------- | --- | --- | --- | --------------------- | --- | ------ | -------- | ------ | ------- | ------ | --------- |
|                 |     |                 |           |            |     |     |     | PyTorch, NumPy,       |     | and    | Python’s | random |         | module | to ensure |
| encourage       |     | correct         | direction | prediction |     |     |     |                       |     |        |          |        |         |        |           |
|                 |     |                 |           |            |     |     |     | full reproducibility. |     | Both   | models   | are    | trained | with   | AdamW     |
| C. AttnCorrect: |     | Attention-Based |           | Correction |     |     |     | optimizer [17]:       |     |        |          |        |         |        |           |
|                 |     |                 |           |            |     |     |     |                       |     | 5×10−4 |          |        |         | 8×10−4 |           |
Figure2presentsthecompleteAttnCorrectarchitecturewith • Learning rate: (AttnCorrect), (Gated-
| ∼471K | trainable | parameters. |     |     |     |     |     | Linear) |     |     |     |     |     |     |     |
| ----- | --------- | ----------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
1) Premarket Encoding: The sequence is projected to hid- Weight decay: 10−4
•
den dimension d=128: • Early stopping patience: 20 (AttnCorrect), 25 (GatedLin-
ear)
| H(0) | =Linear | (Drop |     | (GELU(LN(X(pm)W |     |     | +b )))) |          |           |     |          |     |     |     |     |
| ---- | ------- | ----- | --- | --------------- | --- | --- | ------- | -------- | --------- | --- | -------- | --- | --- | --- | --- |
|      |         | 128   | 0.3 |                 |     |     | e e     | Gradient | clipping: |     | max norm | 1.0 |     |     |     |
•
(2)
|       |     |           |      |      |          |     |             | • Dropout: | 0.3   | (AttnCorrect), |        | 0.25    | (GatedLinear) |        |         |
| ----- | --- | --------- | ---- | ---- | -------- | --- | ----------- | ---------- | ----- | -------------- | ------ | ------- | ------------- | ------ | ------- |
| where | W   | ∈ R7×128. | GELU | [10] | provides |     | smooth non- |            |       |                |        |         |               |        |         |
|       | e   |           |      |      |          |     |             | Random     | seed: | 42             | (fixed | for all | random        | number | genera- |
•
| linearity | and | LayerNorm | [2] | stabilizes | training. |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tors)
| 2)  | Self-Attention |     | Layers: | We  | apply L | = 2 | transformer |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
layers with h=4 heads and head dimension d =32: F. Ablation Study Design
k
|     |     |                            |     |     |     |     |     | Table I | summarizes |     | our comprehensive |     |     | ablation | with 12 |
| --- | --- | -------------------------- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ----------------- | --- | --- | -------- | ------- |
|     |     | H′ =LN(H(ℓ−1)+MHA(H(ℓ−1))) |     |     |     |     | (3) |         |            |     |                   |     |     |          |         |
modelvariantsacross5baselines,2fullmodels,and5ablation
|     |     | H(ℓ) | =LN(H′+FFN(H′)) |     |     |     |     |           |     |     |     |     |     |     |     |
| --- | --- | ---- | --------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |      |                 |     |     |     | (4) | variants. |     |     |     |     |     |     |     |
The feed-forward network uses expansion factor 2: IV. EXPERIMENTALSETUP
A. Dataset
|     | FFN(x)=Drop |     |     | (GELU(xW   |     | ))W | (5) |             |     |          |     |      |        |       |            |
| --- | ----------- | --- | --- | ---------- | --- | --- | --- | ----------- | --- | -------- | --- | ---- | ------ | ----- | ---------- |
|     |             |     |     | 0.3        |     | 1   | 2   |             |     |          |     |      |        |       |            |
|     |             |     |     |            |     |     |     | We evaluate | on  | 1-minute | bar | data | for 10 | major | technology |
|     | ∈R128×256   |     |     | ∈R256×128. |     |     |     |             |     |          |     |      |        |       |            |
with W and W stocks representing diverse market capitalizations and volatil-
|     | 1           |     |         | 2   |        |         |     |               |       |             |     |         |             |     |           |
| --- | ----------- | --- | ------- | --- | ------ | ------- | --- | ------------- | ----- | ----------- | --- | ------- | ----------- | --- | --------- |
| 3)  | Cross-Modal |     | Fusion: | The | pooled | context | c   | =             |       |             |     |         |             |     |           |
|     |             |     |         |     |        |         | pm  | ity profiles. | Table | II provides |     | dataset | statistics. | The | timeframe |
(cid:80) H(L)
1 isconcatenatedwithseparatelyencodedTimesFM spans December 2024 to January 2026.
T t t
| predictions | and | multiscale |     | features: |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thedatasetspansapproximately266tradingdaysperstock
|     |     |       |     |     |       |     |     | (except NFLX | with | 149 | days | due to | data availability). |     | Stock- |
| --- | --- | ----- | --- | --- | ----- | --- | --- | ------------ | ---- | --- | ---- | ------ | ------------------- | --- | ------ |
|     |     | h=MLP |     | ([c | ;c ;c | ])  | (6) |              |      |     |      |        |                     |     |        |
fusion pm tfm ms specific volatility varies significantly, from 0.001000 (MSFT,
|     |     |     |     | R384 | →R128. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where the fusion MLP maps most stable) to 0.001988 (TSLA, most volatile).

Self-Attention:+0.099PerDayCorr
X (p m) L ine a r Li nea r M u lti -H ea d A ttn F F N × 2 M ean P o ol
3 00 × 7 7 → 1 2 8 LayerNorm GELU Drop0.3 128 → 1 28 h = 4 ,d = 32 LayerNorm 128→ 2 5 6→128 LayerNorm la ye rs → R1 2 8
k
Concat
|     | yˆ( tf | m) TF M | En co d er |      |     |     |     |     |     |     |                |     |     |
| --- | ------ | ------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
|     | R      | 60      |            | ctfm |     |     |     |     |     |     | [cpm;ctfm;cms] |     |     |
6 0→ 1 2 8
FusionMLP
|     | m   | MSEncoder |     |     |     |     |     |     |     |     | 384→256→128 |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
|     | R21 | 21→128    |     | cms |     |     |     |     |     |     |             |     |     |
LN+Drop
OutputMLP
128→64→60
∆yneural∈R60
Total:∼471Ktrainableparameters
Fig. 2: AttnCorrect Architecture. Premarket sequences (300×7) pass through embedding layers, then L=2 transformer
blocks with 4-head self-attention (highlighted box). Pooled features fuse with encoded TimesFM predictions and multiscale
| features. | Output weights | initialized      |         | to zero          | [23] for stable training. |     |               |               |                |             |                |          |            |
| --------- | -------------- | ---------------- | ------- | ---------------- | ------------------------- | --- | ------------- | ------------- | -------------- | ----------- | -------------- | -------- | ---------- |
| TABLE     | I: Ablation    | Study            | Design: | 12               | Model Variants            |     |               |               |                |             |                |          |            |
|           |                |                  |         |                  |                           | 3)  | Training-only |               | normalization: |             | Stock-specific |          | volatility |
|           |                |                  |         |                  |                           | for | feature       | normalization |                | is computed | using          | training | dates      |
| ID Model  |                | AblatedComponent |         | ResearchQuestion |                           |     |               |               |                |             |                |          |            |
only.
Baselines(5models)
01 HistMean – Naivebaseline 4) Model fitting restricted to training set: TimesFM
| 02 MLP  |     | –   |     | Standardneuralbaseline    |     |         |         |        |     |            |            |     |            |
| ------- | --- | --- | --- | ------------------------- | --- | ------- | ------- | ------ | --- | ---------- | ---------- | --- | ---------- |
|         |     |     |     |                           |     | remains | frozen. | Neural |     | correctors | and Random |     | Forest are |
| 03 LSTM |     | –   |     | Recurrentsequencemodeling |     |         |         |        |     |            |            |     |            |
04 BiLSTM – Bidirectionalmodeling fitted only on training data; validation is used only for early
| 05 TimesFMBase |     | –   |     | Frozenfoundationmodel |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stopping.
FullHybridModels(2models)
| 06 AttnCorrect+RF |     | None(Full) |     | Attention+classical |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
07 GatedLinear+RF None(Full) Bilinear+classical C. Evaluation Metrics
AblationVariants(5models)
|                     |     |              |     |                   |     | We  | report | three | complementary |     | correlation | metrics | to pro- |
| ------------------- | --- | ------------ | --- | ----------------- | --- | --- | ------ | ----- | ------------- | --- | ----------- | ------- | ------- |
| 08 AttnCorrect-NoRF |     | RandomForest |     | HowmuchdoesRFadd? |     |     |        |       |               |     |             |         |         |
09 GatedLinear-NoRF RandomForest HowmuchdoesRFadd? vide a complete picture of predictive quality, alongside error
| 10 GatedLinear-NoGate     |     | Gatingmechanism    |     | Isgatingnecessary? |     | metrics: |     |     |     |     |     |     |     |
| ------------------------- | --- | ------------------ | --- | ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 11 GatedLinear-NoBilinear |     | Bilinearprojection |     | Isbilinearhelpful? |     |          |     |     |     |     |     |     |     |
12 AttnCorrect-NoAttn Self-attention Isattentionnecessary? MAE (%): Mean Absolute Error of return predictions
•
|       |             |             |     |               |        | •   | RMSE         | (%): | Root Mean   | Squared | Error     |      |             |
| ----- | ----------- | ----------- | --- | ------------- | ------ | --- | ------------ | ---- | ----------- | ------- | --------- | ---- | ----------- |
| TABLE | II: Dataset | Statistics: |     | 10 Technology | Stocks |     |              |      |             |         |           |      |             |
|       |             |             |     |               |        | •   | Mean Per-Day |      | Correlation |         | (ρ ): For | each | test day d, |
day
|       |           |         |          |     |                    |     | we compute |        | the Pearson | correlation | between        |        | the 60-bar |
| ----- | --------- | ------- | -------- | --- | ------------------ | --- | ---------- | ------ | ----------- | ----------- | -------------- | ------ | ---------- |
| Stock | TrainDays | ValDays | TestDays |     | TrainingVolatility |     |            |        |             |             |                |        |            |
|       |           |         |          |     |                    |     | predicted  | return | vector      | yˆ          | and the 60-bar | actual | return     |
| NVDA  | 186       | 40      |          | 40  | 0.001627           |     |            |        |             | d           |                |        |            |
MSFT 186 40 40 0.001000 vector y , then average across all D test days: ρ =
|       |     |     |     |     |          |     |                   | d           |       |               |             |             | day      |
| ----- | --- | --- | --- | --- | -------- | --- | ----------------- | ----------- | ----- | ------------- | ----------- | ----------- | -------- |
| AAPL  | 186 | 40  |     | 40  | 0.001098 |     | (cid:80)D         |             |       |               |             |             |          |
|       |     |     |     |     |          |     | 1                 | ρ(yˆ        | ,y ). | This measures | within-day  |             | temporal |
| GOOG  | 186 | 40  |     | 40  | 0.001050 |     | D d=1             | d           | d     |               |             |             |          |
|       |     |     |     |     |          |     | alignment—whether |             |       | the model     | correctly   | predicts    | when     |
| GOOGL | 186 | 40  |     | 40  | 0.001070 |     |                   |             |       |               |             |             |          |
| AMZN  | 186 | 40  |     | 40  | 0.001190 |     |                   |             |       |               |             |             |          |
|       |     |     |     |     |          |     | returns           | are larger  | or    | smaller       | within each | trading     | session. |
| META  | 186 | 40  |     | 40  | 0.001298 |     |                   |             |       |               |             |             |          |
|       |     |     |     |     |          | •   | Cross-Day         | Correlation |       | (ρ            | ): Pearson  | correlation | be-      |
| AVGO  | 186 | 40  |     | 40  | 0.001764 |     |                   |             |       |               | cross       |             |          |
TSLA 186 40 40 0.001988 tween the cumulative predicted return per day and the
| NFLX | 104 | 22  |     | 23  | 0.001150 |     |            |        |        |     |               |     |              |
| ---- | --- | --- | --- | --- | -------- | --- | ---------- | ------ | ------ | --- | ------------- | --- | ------------ |
|      |     |     |     |     |          |     | cumulative | actual | return | per | day, computed |     | across all D |
Total 2,011,399rowsacross10tickers testdays.Thismeasureswhetherthemodelcorrectlypre-
|     |     |     |     |     |     |     | dicts which       | days | have        | positive | vs. negative | net | returns— |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---- | ----------- | -------- | ------------ | --- | -------- |
|     |     |     |     |     |     |     | i.e., directional |      | forecasting |          | across days. |     |          |
B. Data Leakage Prevention Pooled Correlation (ρ ): Pearson correlation com-
|     |     |     |     |     |     | •   |     |     |     | pool |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
To ensure temporal validity and avoid look-ahead bias: puted by concatenating all predictions and all actuals
1) Strict input/label time separation: For each trading across all days and bars into single vectors.
| date, all     | model inputs | use       | only pre-9:30 | AM          | data (previous |     |           |         |     |         |     |     |     |
| ------------- | ------------ | --------- | ------------- | ----------- | -------------- | --- | --------- | ------- | --- | ------- | --- | --- | --- |
|               |              |           |               |             |                |     |           |         | V.  | RESULTS |     |     |     |
| day’s regular | session      | + current | day’s         | premarket). | Targets are    |     |           |         |     |         |     |     |     |
|               |              |           |               |             |                | A.  | Aggregate | Results |     |         |     |     |     |
| computed      | exclusively  | from      | 9:30–10:30    | AM.         |                |     |           |         |     |         |     |     |     |
2)Chronologicalsplits:Dataissplitbytradingdayinstrict Table III presents aggregate results across all 10 stocks,
chronological order—no shuffling. Test days occur strictly sorted by RMSE. All three correlation metrics are reported.
| after all training | and | validation | days. |     |     | Key | Observations: |     |     |     |     |     |     |
| ------------------ | --- | ---------- | ----- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |

Bilinear:only2,428params
X(pm)
|       |     | TemporalProj. |     | V⊤X | FeatureProj. |     | Z   | Flatten |     |     |     |     |     |     |
| ----- | --- | ------------- | --- | --- | ------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|       |     | V∈R300×8      |     |     | U∈R7×4       |     | 8×4 | →R32    |     |     |     |     |     |     |
| 300×7 |     |               |     | 8×7 |              |     |     |         |     |     |     |     |     |     |
Concat
[z;m;yˆ(tfm)]
R113
yˆ(tfm)
R60
Linear113→128
LayerNorm+GELU
m
R21
Dropout0.25
Linear128→128
GELU
|     |     |     |     |     |     |     |     | GateLinear |     |     |     | ResidualLinear |        |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | -------------- | ------ | --- |
|     |     |     |     |     |     |     |     | 128→60     |     |     |     |                | 128→60 |     |
Sigmoid
r∈R60
∆y=g⊙r
g∈[0,1]60
|     |     |     |     |     |     |     |     |     |     | ∆y  | ∈R60 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
neural
Total:∼49Kparams(9×fewerthanAttnCorrect)
V⊤XU
Fig. 3: GatedLinear Architecture. The premarket tensor is compressed via low-rank bilinear projection Z = (only
2,428 parameters). A gating mechanism g ∈ [0,1]60 modulates the correction magnitude per time step. Despite 9× fewer
parameters than AttnCorrect, this architecture achieves the best overall performance when combined with Random Forest.
TABLE III: Aggregate Results Across 10 Stocks (Sorted by daily directional forecasting, while GatedLinear+RF
| RMSE).Threecorrelationmetrics:meanper-day(ρ |        |           |          |       |         | ),cross- |              |             |         |            |          |     |     |     |
| ------------------------------------------- | ------ | --------- | -------- | ----- | ------- | -------- | ------------ | ----------- | ------- | ---------- | -------- | --- | --- | --- |
|                                             |        |           |          |       | day     |          | leads        | on          | per-day | and pooled | metrics. |     |     |     |
| day (ρ                                      | ), and | pooled (ρ | ).       |       |         |          |              |             |         |            |          |     |     |     |
| cross                                       |        |           | pool     |       |         |          |              |             |         |            |          |     |     |     |
|                                             |        |           |          |       |         |          | B. Per-Stock | Performance |         | Analysis   |          |     |     |     |
| Model                                       |        | MAE(%)↓   | RMSE(%)↓ | ρday↑ | ρcross↑ | ρpool↑   |              |             |         |            |          |     |     |     |
07_GatedLinear+RF 0.1079 0.1535 0.3730 0.5631 0.5972 Table IV provides detailed per-stock results comparing the
| 06_AttnCorrect+RF         |     | 0.1081 |     | 0.1547 0.3678 | 0.5819 | 0.5890 |                  |           |         |              |         |          |              |        |
| ------------------------- | --- | ------ | --- | ------------- | ------ | ------ | ---------------- | --------- | ------- | ------------ | ------- | -------- | ------------ | ------ |
|                           |     |        |     |               |        |        | two full         | hybrid    | models  | against      | frozen  | TimesFM. | We           | report |
| 11_GatedLinear-NoBilinear |     | 0.1071 |     | 0.1600 0.3422 | 0.5055 | 0.5040 |                  |           |         |              |         |          |              |        |
|                           |     |        |     |               |        |        | RMSE,            | mean      | per-day | correlation, | and     | pooled   | correlation. |        |
| 10_GatedLinear-NoGate     |     | 0.1084 |     | 0.1666 0.2864 | 0.3620 | 0.4317 |                  |           |         |              |         |          |              |        |
| 02_MLP                    |     | 0.1105 |     | 0.1679 0.2407 | 0.4957 | 0.4584 |                  |           |         |              |         |          |              |        |
|                           |     |        |     |               |        |        | Per-Stock        | Insights: |         |              |         |          |              |        |
| 09_GatedLinear-NoRF       |     | 0.1087 |     | 0.1710 0.2147 | 0.3058 | 0.3219 |                  |           |         |              |         |          |              |        |
| 08_AttnCorrect-NoRF       |     | 0.1091 |     | 0.1740 0.2335 | 0.3829 | 0.3698 |                  |           |         |              |         |          |              |        |
|                           |     |        |     |               |        |        | • GatedLinear+RF |           |         | wins         | on 7/10 | stocks   | for          | RMSE,  |
| 03_LSTM                   |     | 0.1082 |     | 0.1744 0.3519 | 0.4628 | 0.4943 |                  |           |         |              |         |          |              |        |
04_BiLSTM 0.1090 0.1779 0.3420 0.4653 0.4737 including the most volatile stocks (AVGO, TSLA)
| 12_AttnCorrect-NoAttn |     | 0.1109 |     | 0.1922 0.1347 | 0.4179 | 0.1997 |     |     |     |     |     |     |     |     |
| --------------------- | --- | ------ | --- | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
05_TimesFMBase 0.1113 0.1946 0.0586 −0.0357 0.0614 • Both methods transform near-zero per-day correla-
| 01_HistMean |     | 0.1115 |     | 0.1946 0.0442 | 0.0000 | 0.0610 |         |              |                    |     |             |         |      |     |
| ----------- | --- | ------ | --- | ------------- | ------ | ------ | ------- | ------------ | ------------------ | --- | ----------- | ------- | ---- | --- |
|             |     |        |     |               |        |        | tions   | into         | moderate-to-strong |     |             | ones    |      |     |
|             |     |        |     |               |        |        | Highest | improvements |                    |     | on volatile | stocks: | NVDA | and |
•
|           |         |              |     |            |     |           | AVGO    | show | largest | correlation  |     | gains   |           |      |
| --------- | ------- | ------------ | --- | ---------- | --- | --------- | ------- | ---- | ------- | ------------ | --- | ------- | --------- | ---- |
|           |         |              |     |            |     |           | Per-day | vs.  | pooled  | correlations |     | differ: | For AAPL, | per- |
| 1) Hybrid | methods | dramatically |     | outperform |     | all base- | •       |      |         |              |     |         |           |      |
lines: Mean per-day correlation improves from 0.059 day correlation is only 0.171 (GatedLinear+RF) while
|            |     |                    |                    |         |        |          | pooled | is       | 0.347,    | suggesting | the  | model      | captures | cross-   |
| ---------- | --- | ------------------ | ------------------ | ------- | ------ | -------- | ------ | -------- | --------- | ---------- | ---- | ---------- | -------- | -------- |
| (TimesFM)  |     | to 0.373           | (GatedLinear+RF)—a |         |        | 6.4× im- |        |          |           |            |      |            |          |          |
|            |     |                    |                    |         |        |          | day    | variance | structure | better     | than | within-day |          | temporal |
| provement. |     | Pooled correlation |                    | reaches | 0.597. |          |        |          |           |            |      |            |          |          |
2) GatedLinear+RF achieves best overall performance: patterns for less volatile stocks.
| Best | RMSE    | (0.1535%), | best | MAE (0.1079%), |     | and best    |             |           |     |           |               |     |     |     |
| ---- | ------- | ---------- | ---- | -------------- | --- | ----------- | ----------- | --------- | --- | --------- | ------------- | --- | --- | --- |
|      |         |            |      |                |     |             | C. Ablation | Analysis: |     | Component | Contributions |     |     |     |
| mean | per-day | (0.373)    | and  | pooled (0.597) |     | correlation |             |           |     |           |               |     |     |     |
with 9× fewer parameters 1) Finding 1: Classical Residual Learning Provides the
3) Cross-day vs. per-day correlations reveal different Largest Single-Component Contribution: Random Forest
model strengths: AttnCorrect+RF achieves the highest provides the largest improvement of any individual com-
cross-daycorrelation(0.582),indicatingslightlystronger ponent, whether neural or classical:

(ρ
TABLE IV: Per-Stock Performance: TimesFM vs. Hybrid Corrections. Mean per-day correlation day ) and pooled correlation
| (ρ ) shown | separately. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pool
|     |     |     | RMSE | (%) |     |     | Mean | Per-Day Corr | (ρ  | )   |     | Pooled | Corr | (ρ   | )   |
| --- | --- | --- | ---- | --- | --- | --- | ---- | ------------ | --- | --- | --- | ------ | ---- | ---- | --- |
|     |     |     |      |     |     |     |      |              | day |     |     |        |      | pool |     |
Stock TFM Attn+RF Gated+RF TFM Attn+RF Gated+RF TFM Attn+RF Gated+RF
NVDA 0.2466 0.1689 0.1683 0.018 0.485 0.473 0.165 0.734 0.739
MSFT 0.1228 0.0971 0.1010 0.099 0.417 0.424 0.075 0.633 0.624
AAPL 0.1095 0.1073 0.1068 0.033 0.135 0.171 0.040 0.311 0.347
GOOG 0.2140 0.1659 0.1651 0.054 0.396 0.383 −0.014 0.644 0.646
GOOGL 0.2151 0.1690 0.1616 0.120 0.376 0.408 0.070 0.638 0.669
AMZN 0.1463 0.1272 0.1258 0.087 0.344 0.351 0.085 0.505 0.527
META 0.1636 0.1370 0.1363 0.083 0.398 0.399 0.158 0.665 0.659
AVGO 0.3183 0.2372 0.2320 0.010 0.392 0.395 −0.075 0.688 0.685
TSLA 0.2541 0.1948 0.1954 0.109 0.461 0.458 0.136 0.647 0.644
NFLX 0.1558 0.1428 0.1431 −0.027 0.274 0.268 −0.025 0.426 0.434
Average 0.1946 0.1547 0.1535 0.059 0.368 0.373 0.061 0.589 0.597
| Best on |     | 0/10 | 3/10 |     | 7/10 |     | 0/10 | 4/10 | 6/10 |     | 0/10 |     | 4/10 |     | 6/10 |
| ------- | --- | ---- | ---- | --- | ---- | --- | ---- | ---- | ---- | --- | ---- | --- | ---- | --- | ---- |
TABLEV:DetailedAblationAnalysis:Withvs.WithoutEach TABLE VI: Parameter Count Breakdown
| Component. | We  | report | mean | per-day | (ρ ) | and cross-day |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | ---- | ------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
day
|      |             |                |     |     |     |     |     | Component |     |     | AttnCorrect |     |     | GatedLinear |     |
| ---- | ----------- | -------------- | --- | --- | --- | --- | --- | --------- | --- | --- | ----------- | --- | --- | ----------- | --- |
| (ρ ) | correlation | contributions. |     |     |     |     |     |           |     |     |             |     |     |             |     |
cross
|     |     |     |     |     |     |     |     | Premarketprocessing |     |     |     | ∼66,000 |     |     | 2,428 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | ------- | --- | --- | ----- |
Component RMSEwith RMSEw/o ρday,with ρday,w/o ∆ρday ∆ρcross Attention/Bilinear ∼200,000 –
RF(GatedLinear) 0.1535 0.1710 0.3730 0.2147 +0.1583 +0.2573 Encoder/FusionMLP ∼190,000 ∼31,000
RF(AttnCorrect) 0.1547 0.1740 0.3678 0.2335 +0.1343 +0.1990 Outputlayers ∼15,000 ∼15,000
| Self-Attention  |     | 0.1740 | 0.1922 | 0.2335 | 0.1347 | +0.0988 | −0.0350 |                |     |     |     |          |     |         |     |
| --------------- | --- | ------ | ------ | ------ | ------ | ------- | ------- | -------------- | --- | --- | --- | -------- | --- | ------- | --- |
|                 |     |        |        |        |        |         |         | Totaltrainable |     |     |     | ∼471,000 |     | ∼49,000 |     |
| GatingMechanism |     | 0.1710 | 0.1666 | 0.2147 | 0.2864 | −0.0717 | −0.0562 |                |     |     |     |          |     |         |     |
BilinearProjection 0.1710 0.1600 0.2147 0.3422 −0.1276 −0.1997 Ratio 9.6× 1×
∆ρ :positivemeanscomponentimprovesmeanper-daycorrelation;
day
|     |     |     |     |     |     |     |     | Performance |     |     | 0.368/0.589Corr |     | 0.373/0.597Corr |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --------------- | --- | --------------- | --- | --- |
negativemeansremovingcomponentimprovesperformance.∆ρcross:same
forcross-daycorrelation.
thelast60premarketbarsflatteneddirectly(420dimensions),
| • GatedLinear: |      | RF adds    | +0.158 | mean      | per-day | correlation  |     |                                                          |               |                |         |             |     |         |          |
| -------------- | ---- | ---------- | ------ | --------- | ------- | ------------ | --- | -------------------------------------------------------- | ------------- | -------------- | ------- | ----------- | --- | ------- | -------- |
|                |      |            |        |           |         |              |     | preserving                                               | recent        | dynamics       | better. |             |     |         |          |
| (0.215         | →    | 0.373) and | +0.257 | cross-day |         | correlation, | re- |                                                          |               |                |         |             |     |         |          |
|                |      |            |        |           |         |              |     | 3) Finding                                               | 3:            | Self-Attention |         | Provides    | the | Largest | Positive |
| duces          | RMSE | by 10.2%   |        |           |         |              |     |                                                          |               |                |         |             |     |         |          |
|                |      |            |        |           |         |              |     | Neural                                                   | Contribution: | Self-attention |         | contributes |     | +0.099  | mean     |
| AttnCorrect:   |      | RF adds    | +0.134 | mean      | per-day | correlation  |     |                                                          |               |                |         |             |     |         |          |
| •              |      |            |        |           |         |              |     | per-daycorrelation—thelargestpositivecontributionfromany |               |                |         |             |     |         |          |
(0.234 → 0.368) and +0.199 cross-day correlation, re- neural-only component:
| duces | RMSE | by 11.1% |     |     |     |     |     |        |            |               |     |     |     |         |     |
| ----- | ---- | -------- | --- | --- | --- | --- | --- | ------ | ---------- | ------------- | --- | --- | --- | ------- | --- |
|       |      |          |     |     |     |     |     | • With | attention: | RMSE=0.1740%, |     |     | ρ   | =0.2335 |     |
This finding demonstrates that classical machine learning day
|     |     |     |     |     |     |     |     | • Without(meanpooling):RMSE=0.1922%,ρ |     |     |     |     |     |     | =0.1347 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
day
| methods           | remain | highly | valuable   | even  | when        | combined | with |                |     |         |          |          |     |         |          |
| ----------------- | ------ | ------ | ---------- | ----- | ----------- | -------- | ---- | -------------- | --- | ------- | -------- | -------- | --- | ------- | -------- |
|                   |        |        |            |       |             |          |      | Self-attention |     | enables | flexible | temporal |     | pattern | learning |
| neural approaches |        | for    | foundation | model | adaptation. |          | RF’s |                |     |         |          |          |     |         |          |
contribution is particularly large for cross-day correlation, across the 300-bar premarket sequence, allowing the model
|     |     |     |     |     |     |     |     | to attend | to relevant | time | periods | dynamically. |     | The | cross-day |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---- | ------- | ------------ | --- | --- | --------- |
indicatingitiseffectiveatcapturingfeaturesthatpredictdaily
|             |          |     |     |     |     |     |     | correlation | contribution |     | is minimal | (−0.035), |     | confirming | that |
| ----------- | -------- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ---------- | --------- | --- | ---------- | ---- |
| directional | returns. |     |     |     |     |     |     |             |              |     |            |           |     |            |      |
self-attention’smainvalueisinwithin-daytemporalmodeling
| 2) Finding | 2:           | Simpler          | Architectures |            | Outperform    |         | Without   |                |       |             |             |     |          |          |      |
| ---------- | ------------ | ---------------- | ------------- | ---------- | ------------- | ------- | --------- | -------------- | ----- | ----------- | ----------- | --- | -------- | -------- | ---- |
|            |              |                  |               |            |               |         |           | rather than    | daily | directional | prediction. |     |          |          |      |
| Classical  | Components:  |                  | The most      | surprising |               | result: | When      |                |       |             |             |     |          |          |      |
|            |              |                  |               |            |               |         |           | 4) Finding     | 4:    | Gating      | Mechanism   |     | Provides | Marginal | Ben- |
| Random     | Forest       | is removed,      | simpler       | neural     | architectures |         | out-      |                |       |             |             |     |          |          |      |
|            |              |                  |               |            |               |         |           | efit: Removing | the   | gating      | mechanism   |     | slightly | improves | per- |
| perform    | more complex | ones.            |               |            |               |         |           |                |       |             |             |     |          |          |      |
| Comparing  |              | GatedLinear-NoRF |               | (0.215     | per-day       |         | corr) vs. | formance:      |       |             |             |     |          |          |      |
GatedLinear-NoBilinear (0.342 per-day corr): • ∆ρ = −0.072 (removing gate improves by 0.072)
day
Thelearnedgatesmayintroduceunnecessarycomplexity
| • Removing   |     | bilinear   | projection | improves |       | mean | per-day | •            |            |            |          |       |     |     |     |
| ------------ | --- | ---------- | ---------- | -------- | ----- | ---- | ------- | ------------ | ---------- | ---------- | -------- | ----- | --- | --- | --- |
|              |     |            |            |          |       |      |         | without      | adding     | predictive |          | value |     |     |     |
| correlation  |     | by +0.128  |            |          |       |      |         |              |            |            |          |       |     |     |     |
| • Removing   |     | bilinear   | projection | improves | RMSE  |      | by 6.4% |              |            |            |          |       |     |     |     |
|              |     |            |            |          |       |      |         | D. Parameter | Efficiency |            | Analysis |       |     |     |     |
| The bilinear |     | projection | compresses |          | 300 × | 7 =  | 2,100   |              |            |            |          |       |     |     |     |
dimensions to just 32—a 65× compression that loses fine- Table VI details the parameter breakdown for both archi-
| grained | temporal | information. |     | The NoBilinear |     | variant | uses | tectures. |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | --- | -------------- | --- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |

GatedLinearachievesbetterperformancewith9.6×fewer 2) Startwithsimplerneuralarchitectures:Complexneu-
parameters, demonstrating that parameter efficiency does not ralcomponentsmaynotprovidebenefitsproportionalto
require sacrificing accuracy in this domain. their parameter cost
3) Self-attention is valuable for sequence modeling:
VI. DISCUSSION
Provideslargestpositiveneuralcontribution(+0.099per-
A. On Correlation Metrics for Multi-Step Forecasting day correlation)
A critical methodological point: for multi-step time series 4) Avoid aggressive dimensionality reduction: Preserve
predictions (60 bars × D days), how correlation is computed recenttemporalinformationunlessclassicalcomponents
significantly affects reported results. Pooled correlation (flat- can compensate
teningallpredictionsintoonevector)canbeinflatedbycross- 5) Prioritize parameter efficiency: GatedLinear+RF
day variance structure—if the model merely captures that achieves best results with 9× fewer parameters
some days are more volatile than others, pooled correlation 6) Report multiple correlation metrics:
will be nonzero even without genuine within-day predictive
E. Limitations and Future Work
ability. Mean per-day correlation is more conservative and
more relevant for intraday trading, as it measures whether Limitations:
the model correctly predicts the temporal pattern of returns • Evaluation limited to 10 large-cap technology stocks
withineachsession.Cross-daycorrelationcapturesadifferent • Test period spans 40 days; longer evaluation needed
skill: predicting which days will have positive vs. negative • Transaction costs and market impact not modeled
cumulative returns. We recommend reporting all three metrics • Only TimesFM tested; other foundation models may
in future work on multi-step financial forecasting. behave differently
B. Why Does Classical Residual Learning Complement Neu- • The limited baseline correlation of frozen TimesFM
means that even modest absolute improvements yield
ral Correction?
large relative gains
Several factors explain Random Forest’s strong perfor-
• Premarket signals may be inherently more predictive
mance:
of early-session returns than of later trading hours, so
1) Complementary feature spaces: RF operates on hand-
the reported correlations may not generalize to full-day
crafted multiscale statistics (21 dimensions) capturing
forecasting
domain knowledge, while neural networks process raw
• This work evaluates the hybrid correction methodology
sequences
rather than claiming that TimesFM itself is suited for
2) Non-linear feature interactions: Decision trees nat-
financial prediction tasks
urally capture complex interactions between features
Future directions:
without explicit specification
3) Robustness to outliers: Tree-based methods handle the • Extend to other asset classes and market conditions
heavy-tailed distributions common in financial data • Investigate adaptive weighting of neural vs. classical
components
4) Residual learning: RF learns patterns that neural net-
works systematically miss, providing orthogonal im- • Apply to other foundation models (Chronos, Lag-Llama)
provements • Develop theoretically-grounded guidelines for neural-
classical integration
C. Why Do Simpler Architectures Excel Without RF?
Thebilinearprojection’s65×compressionistooaggressive:
VII. CONCLUSION
• Loses fine-grained temporal dynamics important for pre- We presented a comprehensive study of hybrid neural-
diction classical correction for adapting frozen time series foun-
• Forces the model to learn optimal temporal patterns that dation models to high-frequency stock prediction. Through
may not generalize systematicablationacross10technologystocksand12model
• Recent premarket information (last 60 bars) is more variants, we reveal that:
predictive than temporally-aggregated patterns 1) Hybrid approaches achieve dramatic improvements:
WhenRFispresent,itcompensatesbyaccessingpremarket 6.4×meanper-daycorrelationimprovementoverfrozen
summary statistics directly, explaining why the full GatedLin- TimesFM (0.059 → 0.373), with pooled correlation
ear+RF system achieves best performance despite the bilinear reaching 0.597
bottleneck. 2) Classical and neural components contribute nearly
equally
D. Practical Recommendations
3) Simpler neural architectures outperform complex
Based on our comprehensive ablation: ones when classical components are removed
1) Always include classical residual learning: RF pro- 4) Parameter efficiency is achievable: GatedLinear+RF
vides contributions nearly matching at minimal compu- achievesbestperformancewith9×fewerneuralparam-
tational cost eters

Our key message: effective foundation model adaptation
requires thoughtful integration of neural and classical
methods. Classical machine learning remains highly valuable
even in the era of foundation models, providing complemen-
tary capabilities that neural networks alone cannot match.
ACKNOWLEDGMENT
This paper was prepared with the assistance of AI tools.
Specifically, AI tools were used for text editing, citation
formatting and optimization assistance, and GitHub Copilot
and other tools were used for coding assistance. The authors
take full responsibility for the content and have verified all
AI-assisted contributions.
The authors thank the anonymous reviewers for their valu-
able feedback.
REFERENCES
[1] A. F. Ansari et al., “Chronos: Learning the language of time series,”
arXiv:2403.07815,2024.
[2] J. L. Ba, J. R. Kiros, and G. E. Hinton, “Layer normalization,”
arXiv:1607.06450,2016.
[3] L.Breiman,“Randomforests,”MachineLearning,vol.45,no.1,pp.5–
32,2001.
[4] K. Cho et al., “Learning phrase representations using RNN encoder-
decoderforstatisticalmachinetranslation,”inProc.EMNLP,2014.
[5] A. Das et al., “A decoder-only foundation model for time-series fore-
casting,”inProc.ICML,2024.
[6] E.F.Fama,“Efficientcapitalmarkets:Areviewoftheoryandempirical
work,”J.Finance,vol.25,no.2,pp.383–417,1970.
[7] T.FischerandC.Krauss,“Deeplearningwithlongshort-termmemory
networks for financial market predictions,” European J. Operational
Research,vol.270,no.2,pp.654–669,2018.
[8] L. Grinsztajn, E. Oyallon, and G. Varoquaux, “Why do tree-based
modelsstilloutperformdeeplearningontypicaltabulardata?”inProc.
NeurIPS,2022.
[9] J.HasbrouckandG.Saar,“Low-latencytrading,”J.FinancialMarkets,
vol.16,no.4,pp.646–679,2013.
[10] D. Hendrycks and K. Gimpel, “Gaussian error linear units (GELUs),”
arXiv:1606.08415,2016.
[11] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
Computation,vol.9,no.8,pp.1735–1780,1997.
[12] N. Houlsby et al., “Parameter-efficient transfer learning for NLP,” in
Proc.ICML,2019.
[13] E.J.Huetal.,“LoRA:Low-rankadaptationoflargelanguagemodels,”
inProc.ICLR,2022.
[14] J.-H.Kimetal.,“Hadamardproductforlow-rankbilinearpooling,”in
Proc.ICLR,2017.
[15] X. L. Li and P. Liang, “Prefix-tuning: Optimizing continuous prompts
forgeneration,”inProc.ACL-IJCNLP,2021.
[16] B. Lim et al., “Temporal fusion transformers for interpretable multi-
horizon time series forecasting,” Int. J. Forecasting, vol. 37, no. 4,
pp.1748–1764,2021.
[17] I. Loshchilov and F. Hutter, “Decoupled weight decay regularization,”
inProc.ICLR,2019.
[18] S. Makridakis et al., “Statistical and machine learning forecasting
methods:Concernsandwaysforward,”PloSOne,vol.13,no.3,2018.
[19] C.Raffeletal.,“Exploringthelimitsoftransferlearningwithaunified
text-to-texttransformer,”JMLR,vol.21,no.140,pp.1–67,2020.
[20] K.Rasuletal.,“Lag-Llama:Towardsfoundationmodelsforprobabilis-
tictimeseriesforecasting,”arXiv:2310.08278,2023.
[21] J.B.TenenbaumandW.T.Freeman,“Separatingstyleandcontentwith
bilinear models,” Neural Computation, vol. 12, no. 6, pp. 1247–1283,
2000.
[22] A.Vaswanietal.,“Attentionisallyouneed,”inProc.NeurIPS,2017.
[23] H. Zhang, Y. N. Dauphin, and T. Ma, “Fixup initialization: Residual
learningwithoutnormalization,”inProc.ICLR,2019.
[24] H. Zhou et al., “Informer: Beyond efficient transformer for long se-
quencetime-seriesforecasting,”inProc.AAAI,2021.
---- END DOCUMENT ----
