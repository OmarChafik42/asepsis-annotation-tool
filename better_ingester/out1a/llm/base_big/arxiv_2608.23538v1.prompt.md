Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
| Interpretable |     | AI with | Local | Distillation |
| ------------- | --- | ------- | ----- | ------------ |
Erin Craig ∗
|     | Department | of Biostatistics, | University | of Michigan |
| --- | ---------- | ----------------- | ---------- | ----------- |
and
|     |     | Yiling | Huang |     |
| --- | --- | ------ | ----- | --- |
6202 guA 42  ]EM.tats[  1v83532.8062:viXra
|     | Department | of Statistics, | University | of Michigan |
| --- | ---------- | -------------- | ---------- | ----------- |
and
|     |            | Snigdha        | Panigrahi  |             |
| --- | ---------- | -------------- | ---------- | ----------- |
|     | Department | of Statistics, | University | of Michigan |
|     |            | August         | 25, 2026   |             |
Abstract
Modern AI models such as tabular foundation models and gradient-boosted ensem-
bles can outpredict classical methods, but provide little basis for reasoning about their
predictions. High-stakes decisions call for models that are both accurate and inter-
pretable as built. Local linear modeling offers a path forward: a smooth regression
function is locally well approximated by a linear one, allowing a linear fit near each
query point to achieve high accuracy without sacrificing transparency. The challenges
lie in learning what is “local” and developing statistical tools for interpretation.
Here, we propose local distillation, in which a black-box “teacher” guides a regu-
larized linear “student” model at each query point. The teacher (1) defines locality
by upweighting training observations with similar predicted outcomes, and (2) anchors
the fit with its prediction at the query point, included as a pseudo-observation whose
weight is estimated from the data. For interpretation, we add a small amount of Gaus-
sian randomization to the local objective and use refits to assess stability: selection
frequencies identify reliable features at a query point, and clustering the randomized
fits identifies stable subgroups across the data. Under the lasso penalty, we prove that
this randomization yields feature-selection probabilities that are stable under small
perturbations of the training responses. Across 17 benchmark datasets, local distilla-
tion nearly matches its AI teacher’s accuracy while producing a sparse linear model at
each test point. In a high-dimensional cancer gene expression example, the framework
identifies patient subgroups whose local models use different genes; this heterogeneity
is invisible to a global linear model, and difficult to surface in a black-box model.
Keywords: Local regression; Interpretable AI; Distillation; Randomization; Stability; Tabu-
| lar foundation | models         |                 |     |     |
| -------------- | -------------- | --------------- | --- | --- |
| ∗Corresponding | author. Email: | ercr@umich.edu. |     |     |
1

1 Introduction
Advancesinartificialintelligence(AI)arerapidlychangingwhatispredictable [1,2]. Modern
black-box models, such as foundation models and gradient-boosted ensembles, sometimes
outpredictsimplerclassicalmodelsevenintheirtraditionalstrongholds,suchassmall-sample
tabular data [3, 4, 5, 6, 7]. Yet, acting on predictions requires more than accuracy alone:
decision-makers must reason about the model’s predictions. Black-box models offer little
basis for such reasoning, which limits the value of their predictions for decision-making.
The standard response, when opting for a black box, is to explain its predictions post
hoc. Popular tools such as LIME [8] and SHAP [9] fit per-observation attributions that
quantify how much each feature contributes to a given prediction. However, because such
explanations are constructed separately from the model, their fidelity to it is not guaranteed.
Moreover, the attributions can be unstable, changing with choices external to the model and
data, such as LIME’s perturbation scheme or SHAP’s reference distribution [10, 11, 12, 13].
By contrast, our work is guided by the view that transparency and reasoning should come
from the predictive model itself, i.e., predictions should be interpretable as produced, rather
than explained through post hoc tools [14]. To achieve this goal, we propose local distillation,
a method in which a high-performing black-box “teacher” guides a local linear “student” fit
at each observation or query point. Because a smooth regression function is locally well
approximated by a linear function, a locally fit simple model can approach the accuracy of
a flexible black box while remaining transparent at the query point. Figure 1 illustrates
local distillation on the Auto MPG dataset [15], where we predict fuel economy (miles per
gallon, MPG). In the test set, each car receives its own sparse linear model; together, they
improve on the global lasso’s prediction squared error (PSE) by 48% while nearly matching
their foundation model teacher (PSE 5.59 vs. TabPFN 5.25; global lasso 10.81). The local
coefficients show that the number of cylinders predicts fuel economy among the least efficient
cars but is not predictive among the most efficient, where engine displacement is more useful.
A global linear model averages over this difference and assigns both a coefficient of zero. We
include a high-dimensional gene expression example in Section 6 and benchmarks across 17
datasets in Section 7 and Appendix B.
2

global local
coefficients coefficients
weight
horsepower 4
cylinders
2
displacement
0
acceleration
−2
origin: European
origin: Japanese −4
model year
Test car, ordered by increasing predicted mpg
tneicfifeoc
Figure 1: Car-specific miles-per-gallon models from local distillation. Local co-
efficients for the Auto MPG data using local distillation with a tabular foundation model
teacher, TabPFN, and a lasso student. Cars are ordered left to right by TabPFN’s predicted
MPG; coefficients are per standard deviation of each feature. The column on the left shows
the global lasso coefficients. On a held-out test set, local distillation improves over the global
lasso’s PSE by 48% (global lasso regression PSE 10.81; TabPFN 5.25; local distillation 5.59).
Thecentralquestion, then, ishowtodefine“local”: whichobservationsshouldinformthe
fit at a given query point? Classical local regression defines locality through unsupervised
similarity in input space (LOESS [16]), which ignores the response variable and is known to
be vulnerable to the curse of dimensionality. Recent work instead defines locality through
supervised weights derived from random forests [17, 18, 19, 20]. Local distillation, as pro-
posed in our work, takes this idea further, defining locality in a supervised and tuning-free
way: the teacher plays two roles, (1) identifying which training observations are informative
via similarity of its predictions, and (2) pulling the student’s prediction toward its own,
with the strength of the teacher’s influence determined from the data by the cross-validated
student-to-teacher loss ratio. If the teacher does not outperform the student, the method
simply reverts to a global linear fit.
Using the teacher’s predicted response to define similarity collapses the p–dimensional
feature space into a single interpretable axis along which the model is localized. We define
locality this way for two reasons: (1) it is an axis along which the feature–outcome relation-
ship often varies, and (2) it is an axis of scientific and clinical interest. This construction
gives each local model a natural interpretation: in medicine, for example, a patient’s model
describesthefeature–outcomerelationshipamongpatientswithinasimilarriskgroup. More-
over, when the teacher is a pretrained foundation model such as TabPFN [3], the student
3

inherits its prior knowledge.
For decision-makers, the ultimate goal is not only accurate and interpretable prediction,
but also trustworthy conclusions drawn from those predictions. Trust is closely tied to the
stability of such conclusions under small perturbations of the training data, as emphasized
by the PCS framework [21, 22, 23]. Motivated by this perspective, we propose a simple
modification to local distillation based on external randomization, treating a conclusion as
interpretable to the extent that it can be shown to be stable. The resulting randomized
distillation fits produce stable local conclusions—such as identifying which features are im-
portantforitspredictionataquerypoint—withoutbreakingtheinherentdependenceamong
features or requiring teacher predictions to be recomputed. Our choice of the randomization
scheme is supported by stability guarantees for feature selection, and it preserves fidelity
to the notion of locality learned from the training data. Beyond localized conclusions, the
randomized fits also reveal how the local feature–outcome relationship varies across obser-
vations: we cluster observations using their randomized local coefficients to learn subgroups
that are stable rather than artifacts of any single fit.
This work contributes (1) local distillation, a predictive method that uses a black-box
teacher to construct accurate, sparse local linear fits (Sections 2 and 7), and (2) a random-
ized stability framework for interpreting these fits, both at individual query points and in
aggregate, with theoretical guarantees (Sections 4 and 5). In two case studies, the framework
reveals heterogeneity in the feature–outcome relationship that a global linear model cannot
express (Sections 4.3 and 6), a central but elusive goal of prediction methods, particularly
in personalized medicine.
2 Local distillation
Suppose we have training data X ∈ Rn×p (standardized), a continuous response y ∈ Rn,
and a test point x∗. We also have a teacher ϕ ˆ : Rp → R, a fitted model that predicts y from
x. Our goal is to predict y at x∗ with a sparse linear model fit locally to the training data.
We describe local distillation using squared-error loss in Section 2.1 and illustrate it with
an example in Section 2.2. The method is general, and Section 2.3 covers its extension to
other loss functions and forms of regularization.
4

| 2.1 Model |     | fitting |     | and | prediction |     |     |     |     |     |     |
| --------- | --- | ------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Our work is inspired in part by knowledge distillation [24], in which a simpler “student”
model is trained under the guidance of a more complex “teacher” model. The student is
usually a smaller neural network, and the goal is compression: a fast, lightweight model that
approximates a costly one. Applying the same principle to regression with a linear student
would yield
|     |     |       |        |     | (cid:34)        |        |                          |              |     | (cid:35) |     |
| --- | --- | ----- | ------ | --- | --------------- | ------ | ------------------------ | ------------ | --- | -------- | --- |
|     |     |       |        |     | n               |        | n                        |              |     |          |     |
|     |     |       |        | 1   | (cid:88)(cid:0) |        | (cid:1)2 (cid:88)(cid:0) |              |     | (cid:1)2 |     |
|     |     | β ˆ = | argmin |     |                 | y −x⊤β | +µ                       | ϕ ˆ (x )−x⊤β |     | ,        | (1) |
|     |     |       |        |     |                 | j      |                          | j            |     |          |     |
|     |     |       |        | 2n  |                 |        | j                        |              | j   |          |     |
β
|                      |     |     |     |            | j=1 |           | j=1    |          |     |     |     |
| -------------------- | --- | --- | --- | ---------- | --- | --------- | ------ | -------- | --- | --- | --- |
| where hyperparameter |     |     | µ   | determines | the | influence | of the | teacher. |     |     |     |
WhenE[y
| x]ishighlynonlinear, however, asinglelinearstudentcannotmatchaflexible
teacher’s predictive performance. We therefore introduce local distillation, summarized in
Algorithm 1, in which a separate student model is fit for each test observation. The teacher
guides the definition of the local neighborhood around the query point and anchors the fit
| through | its prediction |     | at  | that point. |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
More precisely, our proposed method in Algorithm 1 modifies the standard knowledge
| distillation | objective |     | in  | (1) in three | ways: |     |     |     |     |     |     |
| ------------ | --------- | --- | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- |
1. First, we fit a separate local model for each test observation x∗, replacing the global
distillation sum with a term that pulls the student’s prediction x∗⊤β toward the teacher’s
prediction; see(4). Thisanchorsthelocalfittotheteacher’spredictionatthequerypoint.
2. Second,wereplaceuniformtrainingweightswithsimilarityweights{S ˆ (x∗) : j ∈ {1,...,n}}
j
ˆ
that upweight training points whose teacher prediction is close to ϕ (x∗); see (3). These
weights define locality around the query point by determining which training observations
| belong | to its | local | neighborhood. |     |     |     |     |     |     |     |     |
| ------ | ------ | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
3. Third, we estimate µˆ from the data as the cross-validated student-to-teacher loss ratio,
√
rather than tuning it; see (2). We scale it further by 1/ nˆ , where nˆ is the effective
|     |     |     |     |     |     |     |     | eff |     | eff |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sample size defined in (3). The teacher’s influence therefore grows both when the teacher
outperforms the student globally (larger µˆ) and when the local neighborhood is sparse
| (smaller | nˆ  | ), where | the | local | fit most | needs | anchoring. |     |     |     |     |
| -------- | --- | -------- | --- | ----- | -------- | ----- | ---------- | --- | --- | --- | --- |
eff
When µˆ ≤ 1, the teacher offers no improvement and we instead return the global linear
| fit for | all test | observations.1 |     |     |     |     |     |     |     |     |     |
| ------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1This choice is deliberately conservative: a teacher that offers no global improvement may still help
locally, but estimating where requires localized loss ratios, which we found too variable to be reliable (see
| “Further | localization”, |     | Section | 2.3). |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
5

In an ablation study across our benchmark datasets (Appendix C), we find that using
both the similarity weights and the teacher prediction anchor yields better predictions than
using either alone.
In Algorithm 1 and throughout, we write ϕ
ˆ(−j)(x
) for the teacher’s prediction at training
j
pointj computedwithoutaccessto(x ,y ): iftheteacherisfittothetrainingdata, orusesit
j j
as context at prediction time (as with the in-context learning of tabular foundation models),
ϕ
ˆ(−j)
is the out-of-fold (OOF) prediction; if the teacher makes no use of the training data,
ϕ
ˆ(−j)
= ϕ
ˆ
. We additionally include an unpenalized intercept, which we suppress in the
notation for clarity.
Algorithm 1 Local distillation for regularized linear models
Input: Training data (X,y) with n observations; test observation x∗; teacher ϕ ˆ ; elastic-net
parameter α ∈ [0,1].
Output: Prediction yˆ∗ and local coefficients β ˆ∗ at x∗.
1. Estimate distillation strength as the cross-validated student-to-teacher loss ratio:
µˆ = L ˆ (f βˆ ) , L ˆ (g) = 1 (cid:88) n (cid:0) y −g(−j)(x ) (cid:1)2 , (2)
L ˆ (ϕ ˆ ) n j j
j=1
ˆ
where f is the global elastic-net fit with shrinkage parameter λ chosen by cross-
βˆ
validation, and g(−j) denotes prediction at x without access to (x ,y ).
j j j
If µˆ ≤ 1, return yˆ∗ = f (x∗) and β ˆ∗ = β ˆ , and stop.
βˆ
2. Compute similarity weights and effective sample size:
S ˆ = S ˆ (x∗) = exp(−d j ) , d = (cid:0) ϕ ˆ(−j)(x j )−ϕ ˆ (x∗) (cid:1)2 , nˆ = (cid:18) (cid:88) n S ˆ2 (cid:19)−1 ,
j j (cid:80)n exp(−d ) j σˆ2 eff j
k=1 k ϕ j=1
(3)
where σˆ2 is the empirical variance of {ϕ ˆ(−j)(x )}n .
ϕ j j=1
3. Fit the local model and predict: yˆ∗ = x∗⊤β ˆ∗, where
n
β ˆ∗ = argmin 1 (cid:88) S ˆ (cid:0) y −x⊤β (cid:1)2 + √ µˆ (cid:0) ϕ ˆ (x∗)−x∗⊤β (cid:1)2 +λ ˆ(cid:2) α∥β∥ + (1−α) ∥β∥2 (cid:3) .
2 j j j 2 nˆ 1 2 2
β eff
j=1
(4)
Note: For a set of test observations, run step 1 once and steps 2–3 independently (in parallel) for each x∗.
6

2.1.1 The teacher as a Bayesian prior
Our approach has a natural Bayesian interpretation: the teacher’s prediction at the test
observation acts as a Gaussian predictive prior on x∗⊤β, centered at ϕ ˆ (x∗) with precision
µˆ
√ . This connects to data augmentation priors [25, 26], in which prior beliefs are encoded
nˆ
eff
via pseudo-observations rather than parameter distributions. These priors express beliefs
about observable quantities y | x, which are typically more interpretable than beliefs about
regression coefficients, and yield posterior inference via weighted least squares on a modified
dataset.
Our method differs in where the prior comes from and how it is deployed: rather than
using a fixed set of elicited prior locations shared by one global fit, each test observation
gets its own local model with a single pseudo-observation at the query point, centered at the
µˆ
teacher’s prediction. Additionally, we estimate the prior precision √ from the data, in
nˆ
eff
the spirit of empirical Bayes. This parallels the power prior of Ibrahim and Chen [27], where
historical data enters the likelihood with a tunable weight; µˆ plays the analogous role and is
estimated directly from the student-to-teacher loss ratio.
2.2 A worked example of local distillation
We illustrate the three steps of Algorithm 1 using the Auto MPG data [15], a set of n = 392
vehicles from the 1983 American Statistical Association Exposition with p = 8 predictors
after encoding, including engine characteristics, vehicle weight, model year, and region of
manufacture. Our goal is to predict fuel economy in miles per gallon.
We use the lasso as our student model, and TabPFN as the teacher. Using a 60/40
train/test split, we proceed as follows:
1. Estimate distillation strength. The global lasso has CV PSE 12.81; the TabPFN
12.81
teacher 6.31; therefore, µˆ = = 2.03. Since µˆ > 1, the teacher improves on the
6.31
global lasso and we proceed; had µˆ ≤ 1, we would have returned the global fit.
2. Compute similarity weights. For each test vehicle, we weight the training set by
similarity of TabPFN’s predicted MPG as in (3). The effective sample sizes nˆ range
eff
from 39 to 172 (median 141) out of n = 235.
train
3. Fit and predict. We fit a locally distilled model for every test vehicle by solving (4).
This produces one model and prediction per car. On this test set, the global lasso has
7

PSE 10.81, TabPFN 5.25, and local distillation 5.59: the student performance is close
to that of its teacher. In Section 4, we visualize and interpret the models.
| 2.3 Computability, |     | generalizations |     |     | and further | localization |     |
| ------------------ | --- | --------------- | --- | --- | ----------- | ------------ | --- |
Computability. For a single test observation x∗, Equation (4) is a weighted elastic-
|     |     | ˆ   |     | x∗  |     | ˆ (x∗) |     |
| --- | --- | --- | --- | --- | --- | ------ | --- |
net problem with fixed λ and α: append to X and ϕ to y, and use weights
√
{S ˆ ,...,S ˆ ,µˆ/ nˆ }. Any solver that supports observation weights (e.g. [28] or
| 1   | n eff |     |     |     |     |     | glmnet |
| --- | ----- | --- | --- | --- | --- | --- | ------ |
adelie [29]) can fit it directly. Fitting many models scales naturally: λ ˆ is estimated once
on the training set, and the local fits are then independent single-λ problems, parallelizable
| across query | points. |     |     |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- | --- | --- |
Other forms of regularization, and nonlinearities in the student. We have focused
on the elastic-net penalty, which spans lasso through ridge, but the pseudo-observation
construction above is agnostic to the penalty: any regularizer supported by the solver, such
| as the group | or fused | lasso, can | be used | in its | place. |     |     |
| ------------ | -------- | ---------- | ------- | ------ | ------ | --- | --- |
We have also chosen the student to be locally linear, but the feature map is a modeling
choice: replacing x with a basis expansion Φ(x) (e.g. pairwise interactions) yields a student
that is linear in Φ(x) and fit identically, at the cost of interpreting coefficients in the ex-
panded basis. Natural choices here are glinternet [30], which selects pairwise interactions
under a strong-hierarchy constraint, or reluctant interaction modeling [31], which adds in-
teractions only where main effects leave residual signal; either keeps the local model sparse
| and interpretable | while | capturing | interaction | structure. |     |     |     |
| ----------------- | ----- | --------- | ----------- | ---------- | --- | --- | --- |
Generalization to other losses. We have illustrated our method with squared-error
loss, but it extends to any loss ℓ(y,η) convex in η = x⊤β: the local objective of Algorithm 1
becomes
n
|     | (cid:88) |     |     | µˆ  |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
β ˆ∗ = argmin S ˆ ℓ(y ,x⊤β)+ √ ℓ(ϕ ˆ (x∗),x∗⊤β)+λ ˆ [α∥β∥ + (1−α)∥β∥2], (5)
|     |     | j j |     |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | j   | nˆ  |     |     | 2 2 |
|     | β   |     |     | eff |     |     |     |
j=1
where µˆ is the cross-validated student-to-teacher loss ratio with ℓ in place of squared error.
| Taking ℓ(y,η) | = 1(y −η)2 | recovers | Equation | (4). |     |     |     |
| ------------- | ---------- | -------- | -------- | ---- | --- | --- | --- |
2
For logistic regression, the distillation term is the cross-entropy between the teacher’s
and student’s predicted probabilities, matching the soft-target distillation of Hinton et al.
| [24]; similarity | distances | d are | computed | on the | logit scale. |     |     |
| ---------------- | --------- | ----- | -------- | ------ | ------------ | --- | --- |
j
8

A survival response requires one change: the loss is the weighted Cox partial likelihood,
and since the teacher has no natural place in its risk-set structure, it enters instead as a
squared penalty (ϕ ˆ (x∗)−x∗⊤β)2 on the log-relative-hazard scale.
Furtherlocalization. Foreachtestobservation,onecouldselectλbylocalcross-validation
ˆ
and estimate µ from locally weighted losses. We instead reuse the global λ: the local loss
ˆ
in (4) is a weighted mean on the same scale as the cross-validation loss used to select λ, so
the same value is a sensible default, and refitting locally is expensive and in our experiments
rarely improved prediction. Local estimates of µ were highly variable and did not reliably
improve performance either.
Teacher selection. Given several candidate teachers, we propose selecting the one mini-
ˆ ˆ
mizing the cross-validated loss L(ϕ) in (2); this adds little cost beyond Step 1 of Algorithm 1,
and in our benchmarks, it worked well (Appendix B).
Cross-modal and cross-domain distillation. The teacher enters Algorithm 1 only
through its predictions: out-of-fold predictions on the training data, and the prediction
at x∗. There is therefore no requirement that it use the same features as the student. A
teacher built on a richer modality (e.g. images, text, or additional clinical measurements)
can be distilled into a local linear model on the features we wish to interpret; conversely, the
teacher may perform best with fewer features than the student, as in our gene expression
example (Section 6), where the teacher screens to 500 genes while the student is fit over all
17,322. Nor is the teacher required to be trained on the data at hand. Most of our examples
use TabPFN, a foundation model pretrained on synthetic data; a model fit to an external
cohort is analogous. In either case, µˆ guards against domain shift: if the teacher does not
transfer well, µˆ ≤ 1 and the method reverts to the global fit.
3 Related work
Local linear modeling. Local modeling methods fit a separate model for each test ob-
servation rather than a single global model. The classical example is LOESS [16], which at
each test observation fits a linear or quadratic regression weighted by kernel proximity in
input space. LOESS produces smooth, adaptive predictions without committing to a global
functional form, and its local coefficients are interpretable. Its weighting is defined by a
user-specified kernel with a bandwidth tuning parameter, and it does not use a teacher.
9

Closer to ours are methods that fit a local linear model with supervised weights derived
from a forest. Generalized random forests [20] and local linear forests [19] use a forest’s leaf
co-membership, and the attention lasso [32] similarly uses random forest proximity, then
blends each local fit with a global baseline via a mixing parameter tuned by cross-validation.
Local distillation instead defines locality through similarity of predicted response, which
allows the use of any accurate regressor as teacher. The teacher’s influence is estimated
from the cross-validated loss ratio rather than tuned, and the method reverts to the global
fit when the teacher offers no improvement. Moreover, the teacher enters as a pseudo-
observation within a single fit, rather than blending with a second model: each local model
is then an elastic-net fit on a weighted, augmented dataset with a single active set. When the
local models use lasso regularization (elastic-net α = 1), the stability guarantees of Section 5
apply to their feature-selection probabilities.
Many recent local linear methods are designed to produce local explanations of black-box
predictors; they differ in what they fit and in how the black box enters. The most widely
used, LIME [8], fits to the black box: a sparse linear model at each test observation is fit to
proximity-weightedperturbationsoftheinput, withtheteacher’spredictionsastheresponse,
so LIME approximates the teacher rather than the data; like SHAP [9], its explanations are
sensitive to choices external to the model and data [10, 11, 12, 13]. MAPLE [33] is more
flexible in its response: a random forest fit to y supplies global feature selection and a
proximity kernel, which together weight a local regression at each test observation. This
local model can regress on either the observed labels y or a black-box teacher’s predictions.
As a predictor, MAPLE is closely related to local linear forests, which we include in our
benchmarks as a representative of this family (Section 7).
Local distillation shares this per-test-point linear structure and fits the observed response
y; the teacher defines locality and anchors the fit rather than serving as the target. It is
a predictive method in its own right, and in contrast to the local methods above, it comes
with stability guarantees for feature selection (Section 5).
Prediction-powered inference. Prediction-powered inference (PPI, PPI++) [34, 35]
augments classical statistical analyses with predictions from a powerful machine learning
(ML) model when labeled data are scarce. Given a small labeled dataset and a large unla-
beled dataset, it imputes the missing labels and builds confidence intervals for population-
level estimands that account for the model’s imputation error and recover the classical es-
timator when the ML model adds nothing. PPI and local distillation share a philosophy:
both use a powerful ML model to strengthen a simpler statistical procedure, and revert to
10

the simpler procedure—in our case, the well-understood global linear model—when the ML
model is unreliable. They differ in target and mechanism. PPI targets population-level in-
ference and corrects for prediction error in its confidence intervals; local distillation targets
pointwise prediction and guards against an unhelpful teacher through the data-driven µˆ and
reversion to the global fit. The power-tuning parameter λ ∈ [0,1] of PPI++ (chosen
PPI
from data to minimize variance) mirrors the role of µˆ, though µˆ enters as the precision of a
| pseudo-observation |     | rather | than | a mixing | weight. |           |     |     |     |     |
| ------------------ | --- | ------ | ---- | -------- | ------- | --------- | --- | --- | --- | --- |
| 4 Interpretability |     |        |      | through  |         | stability |     |     |     |     |
Local distillation, as described in Algorithm 1, predicts each query point through a sparse
local linear fit anchored at that point. Building on the concerns raised in Section 1, conclu-
sions drawn from predictions may inspire little trust unless they can be shown to be stable,
motivating the development of a stability-based framework for interpretation. To this end,
we propose randomized local distillation, a simple modification of Step 3 in Algorithm 1.
The resulting framework assesses stability by examining how the local coefficients vary under
random perturbations of the local distillation optimization, while holding the query point
x∗ and features X fixed. The stability analysis yields interpretations of predictions at two
levels, as demonstrated in this section: (i) individually, through the selected features in each
sparse local model, and (ii) in aggregate, by characterizing heterogeneity across query points
| to identify    | similar | and dissimilar |     | regions      | of  | the dataset. |     |     |     |     |
| -------------- | ------- | -------------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- |
| 4.1 Randomized |         | local          |     | distillation |     |              |     |     |     |     |
Let w = (w ,...,w ) denote a vector of (n+1) independent and identically distributed
|     | 1   | n+1 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
randomization variables, with w ∼ N(0,τ2) for j = 1,...,n+1. Rather than relying on a
j
single local fit, we generate repeated randomized local fits by solving
n
|     | 1   | (cid:88) |     |     | µˆ  |     |     |     | (1−α) |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | ----- | --- |
ˆw ˆ (cid:0) −x⊤β (cid:1)2 (cid:0) ˆ (x∗)−x∗⊤β (cid:1)2 ˆ(cid:2) ∥β∥2 (cid:3)
| β = argmin |     | S y |     | +   |      | ϕ    |     | +λ α∥β∥ | +   |     |
| ---------- | --- | --- | --- | --- | ---- | ---- | --- | ------- | --- | --- |
|            | 2   | j j | j   |     | 2(nˆ | )1/2 |     |         | 1 2 | 2   |
|            | β   |     |     |     | eff  |      |     |         |     |     |
j=1
|     |     | (cid:32) |     |     |     |     | (cid:33)⊤ |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --------- | --- | --- | --- |
n
|     |     |     | (cid:88) |       |     | µˆ1/2 |       |     |     |     |
| --- | --- | --- | -------- | ----- | --- | ----- | ----- | --- | --- | --- |
|     |     | −   | S        | ˆ1/2w | x + | w     | x∗ β, |     |     |     |
|     |     |     |          | j     | j   |       | n+1   |     |     |     |
|     |     |     |          | j     |     | n1/4  |       |     |     |     |
|     |     |     | j=1      |       |     | eff   |       |     |     |     |
(6)
| ˆw  |     |     |     |     |     |     | x∗  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where β denotes the coefficient vector obtained at for a given randomization draw w.
Randomized local distillation modifies (4) of Algorithm 1 by introducing a linear per-
turbation through normally distributed noise variables, while leaving the loss and penalty
11

terms unchanged. Thus, as with local distillation, the randomized fit naturally extends to
other loss functions and regularizers. Analogous to the weighting of the summands in the
loss, each randomization variable w in the linear perturbation term is scaled by the square
j
ˆ ˆ
root of its corresponding weight, S . Consequently, if S is zero or close to zero, w has no
j j j
or little effect on the optimization.
Theamountofrandomizationineachrandomizedlocalfitiscontrolledbyτ2, thevariance
σˆ2
of the normal randomization variables in w. In practice, we set τ2 = t ∗ , where nˆ =
eff
nˆ
eff
1 is the effective sample size (Equation (3)), σˆ2 is the variance of the teacher’s out-of-
Sˆ2+...+Sˆ2
1 n
foldresiduals,andtisaconstantchosenbytheanalyst. Choosingtherandomizationvariance
σˆ2
asafixedfractionof ensuresthatthescaleoftherandomizationiscomparabletothescale
nˆ
eff
of variability contributed by the data to the optimization objective. We recommend using
data to guide the choice of t. The sensitivity bound established in Theorem 1, from which
the stability bound in Corollary 1 follows, improves as the randomization sd τ increases, and
thus as t increases. But too much randomization can reduce the predictive accuracy of the
randomized fits. Therefore, we take the largest t whose out-of-fold median prediction error
is within a small tolerance of that from the unperturbed fits (t = 0); the tolerance reflects
how much prediction accuracy the analyst is willing to trade for stability, and we use 5%
throughout. Figure 2 (left) shows the selection process for the Auto MPG data.
Remark 1. The randomization in (6) is similar in form to that used in the post-selection inference
literature, where linear perturbation terms are added to penalized M-estimation problems to preserve
information that can later be leveraged for valid inference in selected models. See, for example,
the randomized inference methods developed in [36, 37, 38, 39, 40]. Here, however, the added
randomization serves a different role: in Section 5, we prove that it provides stability guarantees
for feature–selection probabilities under small perturbations of the training data.
4.2 Interpreting a single local model
At a given query point x∗, the local model characterizes the feature–response relationship
among observations with similar predicted outcomes. More specifically, a single local distil-
ˆ
lation fit yields a sparse set of features, {j : β ̸= 0} (for α > 0), providing an interpretation
j
of its prediction at x∗. But, as with the standard lasso, this selected set may be unsta-
ble: predictors near the selection boundary may enter or leave the model under even slight
perturbations in the outcomes, ultimately yielding different local interpretations at x∗.
To address this instability, we compute for each feature its empirical selection frequency
12

| across the | randomized | local fits |     |     |     |     |     |
| ---------- | ---------- | ---------- | --- | --- | --- | --- | --- |
B
|     |     |     | 1 (cid:88) | (cid:110) | (cid:111) |     |     |
| --- | --- | --- | ---------- | --------- | --------- | --- | --- |
I ˆw
|     |     |     | πˆ = | β b ̸= | 0 , |     |     |
| --- | --- | --- | ---- | ------ | --- | --- | --- |
|     |     |     | j B  | j      |     |     |     |
b=1
where B is the number of refits of (6) and w denotes the randomization used in the b-th
b
fit. That is, πˆ is the proportion of randomized local refits in which that feature is selected.
j
In particular, a low selection frequency signals uncertainty about a feature’s contribution to
| the prediction | at x∗. |     |     |     |     |     |     |
| -------------- | ------ | --- | --- | --- | --- | --- | --- |
ThetableinFigure2showsonesuchmodelforasingletestcar. Alongsideeachcoefficient
wereportitsselectionfrequency, thefractionofrandomizedlocalrefitsretainingthatfeature.
In this example, five of the seven selected features are retained in over 90% of refits; the least
stable are cylinders and horsepower, retained in 75% and 70% respectively. Randomization
| flags these              | as uncertain. |     |     |     |         |       |            |
| ------------------------ | ------------- | --- | --- | --- | ------- | ----- | ---------- |
| rorre derauqs naidem FOO |               |     |     |     | Feature | Coef. | Sel. prob. |
3.2
|     |     |     |     |     | weight | −5.11 | 100% |
| --- | --- | --- | --- | --- | ------ | ----- | ---- |
3.0
|     |     |     |     |     | model year | 2.28 | 100% |
| --- | --- | --- | --- | --- | ---------- | ---- | ---- |
2.8
|     |     |     |     |     | origin: European | 0.40 | 99% |
| --- | --- | --- | --- | --- | ---------------- | ---- | --- |
2.6
|     |     |     |     |     | acceleration | 0.52 | 99% |
| --- | --- | --- | --- | --- | ------------ | ---- | --- |
2.4
|     |     |     |     |     | origin: Japanese | 0.41 | 98% |
| --- | --- | --- | --- | --- | ---------------- | ---- | --- |
  +5%
2.2
|     |     |     |     |     | cylinders | 0.24 | 75% |
| --- | --- | --- | --- | --- | --------- | ---- | --- |
2.0
|     |      |      |     |     | horsepower | −0.17 | 70% |
| --- | ---- | ---- | --- | --- | ---------- | ----- | --- |
|     | 10−2 |      | 100 |     |            |       |     |
|     |      | 10−1 |     | 101 |            |       |     |
Noise multiple 𝘵
Figure 2: Left: choosing the randomization scale t. We take the largest t whose
out-of-fold median squared error remains within 5% of the unperturbed fit (shaded); the
selected value is circled. Right: a local model for a single test car with mid-range fuel
economy (distillation predicted 23.7 mpg, observed 23.9 mpg), ordered by decreasing selection
probability. The lasso penalty selected 7 of the 8 features in the unperturbed fit. Selection
probability is the fraction of 100 randomized refits retaining the feature at the selected scale
tˆ(circled at left), and features retained in under 90% are shown in bold. Region coefficients
| are contrasts | against | American | manufacture. |     |     |     |     |
| ------------- | ------- | -------- | ------------ | --- | --- | --- | --- |
Here, with only 8 features, most selections are stable across refits. This is not the case
in higher dimensions: in the gene expression example of Section 6 (p = 17,322), the median
13

local fit selects 94 genes, of which typically only 15 are retained in over 90% of refits. In
simulation (Appendix D), we find that the selection frequencies distinguish the true support
while yielding a smaller, more interpretable set of features.
Using randomized refits to address the instability of lasso-selected features is not new; a
prominentexampleisstabilityselection[41]basedonsubsampling. Therandomizationmech-
anism in our approach, however, is deliberately different from subsampling. This distinction
has consequences for both the computational cost of local refitting and the interpretation of
the resulting stability measures, which we discuss below.
Remark 2. Across randomized refits of local distillation, as proposed in (6), the similarity weights
and teacher predictions are computed once from the training data and then held fixed. The added
randomizationperturbsonlytheoptimizationobjective, whilekeepingthedesignfixedandusingalln
observations in each refit. From a computational perspective, this avoids the potentially substantial
additional cost of subsampling-based refitting procedures such as stability selection. Under subsam-
pling, Steps 1 and 2 of Algorithm 1 would need to be recomputed for each refit, as would the teacher
predictions whenever they depend on the sampled training data; take, for example, predictions from
tabular foundation models deploying in-context learning.
Remark 3. The choice of randomization determines the notion of stability being assessed and,
consequently, the interpretation of the resulting predictions. Beyond its computational advantages,
our randomization mechanism is designed to remain faithful to the locality learned from the train-
ing data: each refit preserves the same similarity weights and the teacher prediction anchor. By
contrast, under subsampling-based refits, even small changes in sample composition can potentially
alter the local structure in data, especially when the effective sample size nˆ is small, i.e., when the
eff
weights Sˆ are concentrated on only a few observations, or when outcomes have heterogeneous noise
j
levels. In such settings, variation across refits may reflect changes in the local structure rather than
instability in the local feature–response relationship itself, making stability a less reliable character-
ization of that relationship.
4.3 Interpreting the local models in aggregate
Beyond individual models, we are also interested in understanding our sample and the het-
erogeneity within it. A natural approach would be to fit locally distilled models on a test set
with n observations (or in a leave-one-out setting on the training data), and then cluster
test
the fitted coefficient vectors into k clusters. However, our goal is to identify and interpret
subgroups that are stable under small perturbations of the response y rather than artifacts
of a single fit. We therefore aggregate the clustering obtained across the randomized refits
14

from Section 4.1 using evidence accumulation clustering [42], allowing the same refits used
to characterize local feature–response relationships to also inform stable subgroup structure
in the data. We proceed as follows:
1. Fit unperturbed local models: run local distillation to obtain n fitted local
test
models, with coefficient vectors in Rp.
2. Choose the number of clusters: cluster the n unperturbed coefficient vectors
test
and select the appropriate k.
3. Clustertherandomizedrefits: drawB independentrandomizationvectorsw ,...,w ,
1 B
as described in Section 4.1. For each draw w , run randomized local distillation (solve
b
(6)) to obtain n randomized coefficient vectors, and cluster these into k groups,
test
yielding B cluster assignments of the test observations.
4. Cluster the co-occurrence matrix: define the similarity between two test observa-
tions as the fraction of the B clusterings in which they fall in the same group, and use
this metric for a final clustering into k groups.
We illustrate thisusing the Auto MPGdata. We (1) fit local models forthe n = 157
test
observations and (2) select the number of clusters k using k-means clustering of the
unperturbed local coefficient vectors; the silhouette score selects k = 3. We then (3) cluster
the randomized refits: for each of B = 100 randomized local distillation runs, we cluster
the refitted coefficient vectors using k-means with k = 3. Finally, we (4) cluster the co-
occurrence matrix: the similarity between two cars is the fraction of the 100 runs in which
they are assigned to the same cluster, and clustering this matrix by average linkage yields
the three groups shown in Figure 3. To visualize the result, we display the unperturbed
coefficients in a heatmap, either ordered by cluster, or averaged within cluster. The three
clusters use different features: cylinders is predictive among the least efficient cars, and
displacement among the most efficient.
15

C1 (mean 16.4) C2 (mean 26.9) C3 (mean 35.7)
weight
horsepower
4
cylinders
2
displacement
0
acceleration
−2
origin: European −4
origin: Japanese
model year
Test car, ordered by increasing predicted mpg within cluster
tneicfifeoc
global local
coefficients coefficients
Figure 3: Vehicle subgroups and their local miles per gallon models. Local coeffi-
cients for the Auto MPG data, with test cars grouped into three subgroups (C1–C3) by the
stable clustering of Section 4.3. Subgroups are ordered left to right by mean MPG, and cars
by predicted MPG within subgroup.
5 Theoretical analysis of stability
In this section, we establish stability guarantees for feature–selection probabilities under
randomized local distillation (6), whose local coefficients enable interpretation of the distilled
fits both individually and in aggregate. Throughout this section, we treat the similarity
ˆ ˆ
weights S and the regularization parameters µˆ and λ as fixed. To avoid confusion, we drop
j
the hats and write these quantities as S , µ, and λ, respectively; similarly we write n for
j eff
the effective sample size. We slightly modify our notation for the teacher’s prediction at the
query point, denoting it by ϕ ˆ (x∗;y), to make explicit that it may depend on the training
response, as is the case in tabular foundation models, for example. We focus on the lasso
penalty, i.e., α = 1, while deferring an extension to the elastic-net penalty for future work
to keep the theoretical development streamlined.
Our main result, Theorem 1, characterizes how the feature–selection probabilities are
sensitive to changes in the input responses, leading to the uniform stability guarantee in
Corollary 1 under small perturbations of the training response. To prove this result, we first
establish a stability guarantee for randomized lasso regression of a perturbed response on the
design matrix; see Theorem 2 in Appendix A.2. To the best of our knowledge, this is the first
16

such guarantee for Gaussian randomization introduced through linear perturbations of the
optimization objective, providing a theoretical basis for the stability-based interpretation of
| feature–selection |     | probabilities |     |               | under | the lasso | penalty. |     |     |     |     |
| ----------------- | --- | ------------- | --- | ------------- | ----- | --------- | -------- | --- | --- | --- | --- |
| 5.1 Notation      |     |               | and | preliminaries |       |           |          |     |     |     |     |
Before proceeding, we introduce notation used to develop the theory.
| First, | let |     |     |        |     |       |     |       |      |           |     |
| ------ | --- | --- | --- | ------ | --- | ----- | --- | ----- | ---- | --------- | --- |
|        |     |     |    |        |    |       |     |      |     |           |     |
|        |     |     |     | y      |     |       |     |       | x⊤   |           |     |
|        |     |     |     | 1      |     |       |     |       | 1    |           |     |
|        |     |     |    | .      |    |       |     |      | .   |           |     |
|        |     |     |     | .      |     |       |     |       | .    |           |     |
|        |     |     |    | .      |    |       |     |      | .   |           |     |
|        |     |     |    |        |    | Rn+1, |     |      |     | R(n+1)×p, |     |
|        |     | y   | =   |        | ∈   |       |     | X =   |      | ∈         |     |
|        |     |     |    |        |    |       |     |      |     |           |     |
|        |     |     |    | y      |    |       |     |      | x⊤  |           |     |
|        |     |     |     | n      |     |       |     |       | n    |           |     |
|        |     |     |    |        |    |       |     |      |     |           |     |
|        |     |     | ˆ   | (x∗;y) |     |       |     | (x∗)⊤ |      |           |     |
ϕ
denotetheaugmentedresponsevectoranddesignmatrix,obtainedbyappendingtheteacher’s
ˆ
prediction ϕ (x∗;y) and the query point x∗ to the response vector and design matrix, respec-
tively.
Let
|     |     |     | Ω   | =   | diag(S | ,...,S | ,S  | ) ∈ R(n+1)×(n+1), |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------ | --- | ----------------- | --- | --- | --- |
|     |     |     |     |     |        | 1      | n   | n+1               |     |     |     |
denote the diagonal matrix of weights for the n+1 observations in the augmented dataset,
µ
where S = √ is the weight assigned to the pseudo-response at the query point. We
n+1 n
eff
then define
|     |     |       |        |     | Ω1/2y |     | Rn+1, |     | Ω1/2X | R(n+1)×p, |     |
| --- | --- | ----- | ------ | --- | ----- | --- | ----- | --- | ----- | --------- | --- |
|     | z   | = z(y | ,...,y | )   | =     | ∈   |       | V   | =     | ∈         | (7) |
|     |     |       | 1      | n   |       |     |       |     |       |           |     |
to be the weight-adjusted response and design, respectively, i.e., coordinatewise, Z =
k
| √   |      |         |     |     | √   |          |     | √           |     |     |     |
| --- | ---- | ------- | --- | --- | --- | -------- | --- | ----------- | --- | --- | --- |
|     |      |         |     |     |     | ˆ (x∗;y) |     | µ ˆ (x∗;y). |     |     |     |
| S y | (k ≤ | n), and | Z   | =   | S   | ϕ        | =   | ϕ           |     |     |     |
| k k |      |         | n+1 |     | n+1 |          |     | n1/4        |     |     |     |
eff
Under this notation, when α = 1 and λ denotes the tuning parameter for the lasso
penalty, the randomized local distillation problem (6) is equivalent to solving
|     |     |     | β(cid:98) | ω = | argmin | 1 ∥z | +ω  | −V β∥2 | + λ∥β∥ | ,   | (8) |
| --- | --- | --- | --------- | --- | ------ | ---- | --- | ------ | ------ | --- | --- |
1
|     |     |     |     |     |     | 2   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
β∈Rp
where ω ∼ N(0,τ2I ) is drawn independently of the training response. The equivalent
n+1
optimization problem, which follows from straightforward algebra, is used throughout this
section. An advantage of this formulation is that it allows us to first establish guarantees for
randomized lasso regression of a perturbed response on a design matrix. These results then
yield the desired guarantees for local distillation, while also being of potential independent
| interest | beyond | the | present | setting. |     |     |     |     |     |     |     |
| -------- | ------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
17

|     |     |     | (cid:16) | (cid:17) |     |     |     |     |     |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
Let E(cid:98) (z,ω) = supp β(cid:98)ω(z) denote the active set obtained by solving the randomized
V
lasso in (8). The quantity of interest is the feature-selection probability for predictor j,
| evaluated | as a function |     | of y | and denoted |           | by  |           |     |     |     |
| --------- | ------------- | --- | ---- | ----------- | --------- | --- | --------- | --- | --- | --- |
|           |               |     |      |             | (cid:104) |     | (cid:105) |     |     |     |
P
|     |     |     | π (y) | =   | j ∈ | E(cid:98) (z,ω) | ,   | for j ∈ [p], |     | (9) |
| --- | --- | --- | ----- | --- | --- | --------------- | --- | ------------ | --- | --- |
|     |     |     | j     |     | ω   | V               |     |              |     |     |
where the probability is over the randomization ω, with y and hence z = z(y ,...,y )
1 n
treated as fixed, and [p] = {1,2,...,p}. The subscript ω on the probability, here and
throughout, indicates that the probability is taken only with respect to the randomization.
| 5.2 | Stability | of  | randomized |     | local | distillation |     |     |     |     |
| --- | --------- | --- | ---------- | --- | ----- | ------------ | --- | --- | --- | --- |
Because the selection probabilities in (9) are obtained by convolving the discontinuous
feature–selection indicator with the Gaussian density of w, they are smooth provided that
the teacher’s prediction is a smooth function of the input y. Lemma 1 formalizes this obser-
vation before we turn to the stability guarantee for randomized local distillation; the proof
| is provided | in Appendix |     | A.1. |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
N
Lemma 1 (Smoothness of feature–selection probabilities). Fix k ∈ ∪ {∞} and suppose
that y (cid:55)→ ϕ ˆ (x∗;y) belongs to Ck(Rn). Then for every j ∈ [p], the selection probability π (y),
j
| defined | in (9), also | belongs | to  | Ck(Rn). |     |     |     |     |     |     |
| ------- | ------------ | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
We now state Theorem 1, which bounds the sensitivity of the feature–selection prob-
abilities to perturbations of the training response y, leveraging the smoothness of these
probabilities established in Lemma 1. We derive this result under the following assumptions
on the design matrix X, the similarity weights S and the weight-adjusted design matrix V .
j
Assumption 1 (Weight-adjusted design in general position). The columns of V are in
| general | position | [43]. |     |     |     |     |     |     |     |     |
| ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Assumption 2 (Bounded weight concentration). We assume that there exists a constant
| C < ∞ | such that | n   | S ≤ | C . |     |     |     |     |     |     |
| ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S     |           | eff | max | S   |     |     |     |     |     |     |
Assumption 3 (Boundeddesignandlocaldistillationweight). ForsomeconstantsB ,C >
X µ
|              |      |     | (cid:8) |       | ,∥x∗∥ | (cid:9) |           |         |     |     |
| ------------ | ---- | --- | ------- | ----- | ----- | ------- | --------- | ------- | --- | --- |
| 0, we assume | that | max | max     | ∥x    | ∥     |         | ≤ B , and | 0 < µ ≤ | C . |     |
|              |      |     |         | i∈[n] | i ∞   | ∞       | X         |         | µ   |     |
Assumption 4 (Non-degeneracyofrestricteddesign). Forsomeconstantκ > 0,weassume
X
that, uniformly over j ∈ [p] and E ∈ EV , where EV denotes the collection of essential active
|     |     |     |     |     | −j  |     | −j  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
18

sets from lasso regression on V (i.e., active sets from the leave-j-covariate-out lasso fit
−j
whose corresponding selection regions have positive Lebesgue measure),
|     |     |     |     | (cid:32) |     | (cid:33) |     |     |
| --- | --- | --- | --- | -------- | --- | -------- | --- | --- |
1
|     |     |     | σ   |           | X        |     | ≥ κ , |     |
| --- | --- | --- | --- | --------- | -------- | --- | ----- | --- |
|     |     |     | min | (cid:112) | IS,E∪{j} |     | X     |     |
|I |
S
|     | (cid:110) |     | (cid:111) |     |     |     |     |     |
| --- | --------- | --- | --------- | --- | --- | --- | --- | --- |
where I = i ∈ [n] : S ≥ 1 collects the training observations whose similarity weights
|     | S   | i   | 2n  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
eff
| are at least | one half | of the | effective | uniform | weight. |     |     |     |
| ------------ | -------- | ------ | --------- | ------- | ------- | --- | --- | --- |
Under Assumption 1, the randomized local distillation problem (8) admits a unique
solution. Assumption 2 prevents the similarity weights from concentrating too heavily on
a small number of observations. Assumption 3 requires both the design covariates and the
distillation-weight parameter to be bounded. Assumption 4 imposes a lower singular-value
condition on the design restricted to the effective similarity neighborhood I , preventing
S
the relevant design columns from becoming nearly linearly dependent among observations
| receiving | non-negligible | weights. |     |     |     |     |     |     |
| --------- | -------------- | -------- | --- | --- | --- | --- | --- | --- |
Theorem 1 (Sensitivity bound for selection probabilities). Suppose that y (cid:55)→ ϕ ˆ (x∗;y) be-
longs to C1(Rn) with L (x∗) = sup ∥∇ϕ ˆ (x∗;y)∥ < ∞, and that Assumptions 1, 2, 3
|     |     | ϕˆ  |     | y∈Rn |     | ∞   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- |
and 4 hold. Then there exists a constant C < ∞ such that, for every j ∈ [p],
|     |     |     |     |     |           | (cid:32) |      | (cid:33) |
| --- | --- | --- | --- | --- | --------- | -------- | ---- | -------- |
|     |     |     |     |     | (cid:114) |          | (x∗) |          |
|     |     |     |     |     | 2C        | 1        | L    |          |
ϕˆ
|     |     | sup ∥∇π | (y)∥ | ≤   |     | √   | +    | .   |
| --- | --- | ------- | ---- | --- | --- | --- | ---- | --- |
|     |     |         | j    | ∞   | π τ | n   | n1/4 |     |
|     |     | y∈Rn    |      |     |     | eff |      |     |
eff
A proof of Theorem 1 is provided in Appendix A.1. The proof consists of two main
components. First, we analyze the stability of the randomized lasso obtained by regressing a
perturbed response on a p-dimensional feature matrix, as detailed in Appendix A.2. Second,
we apply the chain rule to characterize the additional contribution from local distillation, as
| detailed | in Appendix | A.3.         |     |        |              |         |     |     |
| -------- | ----------- | ------------ | --- | ------ | ------------ | ------- | --- | --- |
| We make  | a few       | observations |     | on the | above-stated | result. |     |     |
(i) It follows directly from the bound in Theorem 1 that the contribution of each training
observation to the sensitivity of a feature’s selection probability has two components: the
n−1/2,
first is a direct contribution, excluding the effect of distillation, which is of order
eff
and the second contribution arises through the teacher’s prediction, which is of order
n−1/4L
(x∗).
| eff | ϕˆ  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(x∗),
(ii) Although we make no assumption on L ϕˆ which reflects how the sensitivity of the
teacher’s prediction scales with the effective sample size, it may decrease as the effective
sample size grows, leading to a sharper rate for the second contribution in the bound.
19

(iii) Whentheteacherisafullypretrainedmodel(i.e.,theteacher’spredictiondoesnotdepend
| on the | training | samples), | the bound | in  | Theorem 1 | simplifies | to  |     |
| ------ | -------- | --------- | --------- | --- | --------- | ---------- | --- | --- |
(cid:114)
2C
|     |     |     | sup ∥∇π | (y)∥ | ≤   | n−1/2, |     |     |
| --- | --- | --- | ------- | ---- | --- | ------ | --- | --- |
j ∞
|     |     |     |     |     |     | π τ eff |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- |
y∈Rn
(x∗)
since L = 0. As a further special case, for the global lasso fit without using the
ϕˆ
teacher as a Bayesian prior to shrink the linear predictor toward its predictions, and with
uniform similarity weights S = 1/n, the same bound holds with n = n.
|     |     |     | j   |     |     |     |     | eff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theorem 1 immediately yields the following corollary, which quantifies the stability of
the feature–selection probabilities in response to a perturbation of a single response value,
paralleling notions of algorithmic stability under single-observation perturbations [44].
Corollary 1 (Stability guarantee). Under the assumptions of Theorem 1, there exists a
Rn
constant C < ∞ such that, for every j ∈ [p], i ∈ [n], and for any y,y′ ∈ satisfying
y′
y = for all k ̸= i (equivalently, differing only in the i-th coordinate),
k k
|     |     |                 |               |           | (cid:32) |      | (cid:33) |       |
| --- | --- | --------------- | ------------- | --------- | -------- | ---- | -------- | ----- |
|     |     |                 |               | (cid:114) |          | (x∗) |          |       |
|     |     |                 |               | 2C        | 1        | L    |          |       |
|     |     | (cid:12)        | (y′) (cid:12) |           |          | ϕˆ   |          | −y′|. |
|     |     | (cid:12)π (y)−π | (cid:12) ≤    |           | √ +      |      | |y       |       |
|     |     | j               | j             | π τ       | n        | n1/4 | i        | i     |
eff
eff
The proof of Corollary 1 follows directly from the sensitivity bound in Theorem 1 and is
| therefore | omitted. |     |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
The stability bound presented in Corollary 1 improves with the randomization standard
deviation τ. However, this does not imply that arbitrarily increasing the amount of ran-
domization is desirable, since doing so can compromise predictive accuracy. Accordingly, as
described in Section 4.1, we choose τ to balance stability against a user-specified tolerance
| for loss | in predictive | accuracy. |     |     |     |     |     |     |
| -------- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
Extension to stability over a regularization-grid. Our stability-based approach could
be extended to base decisions on a grid Λ of lasso regularization parameters λ, rather than
on a single fixed value of λ. As proposed in the stability selection framework of [41], a
natural quantity on which to base decisions is maxπ (y;λ), where π (y;λ) denotes the
|     |     |     |     |     |     | j   |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
λ∈Λ
selection probability at λ (with the dependence on λ made explicit in the notation), and the
maximumtakenoverthegridofregularizationparameters. However,ourprooftechniquesfor
controlling the sensitivity of this quantity to perturbations of the training input, and hence
for establishing stability guarantees, may not extend directly to the maximum operation
| because | it is not | smooth. |     |     |     |     |     |     |
| ------- | --------- | ------- | --- | --- | --- | --- | --- | --- |
20

Instead, one can consider a smooth approximation to maxπ (y;λ), namely Π (y) =
|     |     |     |     |     |     | j   |     | Λ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
λ∈Λ
| (cid:16) |            |     | (cid:17) |     |     |     |     |     |
| -------- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
| 1        | 1 (cid:80) |     |          |     | R+. |     |     |     |
log exp(ηπ (y;λ)) , for fixed η ∈ Like the selection probability for any
| η   | |Λ| λ∈Λ |     | j   |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- |
fixed λ, this quantity also takes values in [0,1]. In practice, using its empirical counterpart
Π(cid:98) (y), one can then determine the set of selected features as {j : Π(cid:98) (y) ≥ p }, for a chosen
| Λ   |     |     |     |     |     |     | Λ   | thr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
threshold p . Furthermore, the gradient of Π (y) can be written as
|     | thr |       |          |        | Λ          |          |        |         |
| --- | --- | ----- | -------- | ------ | ---------- | -------- | ------ | ------- |
|     |     |       | (cid:88) |        |            | exp(ηπ   | (y;λ)) |         |
|     | ∇Π  | (y) = | w (y)∇π  | (y;λ), | with w (y) | =        | j      | ,       |
|     |     | Λ     | λ        | j      | λ          | (cid:80) |        |         |
|     |     |       |          |        |            |          | exp(ηπ | (y;λ′)) |
|     |     |       |          |        |            | λ′∈Λ     | j      |         |
λ∈Λ
a convex combination of the derivatives of the selection probabilities. Consequently, a fairly
straightforward extension of our results to establish a uniform stability bound over the grid
Λ would yield a corresponding stability guarantee for Π (y) under perturbations to a single
Λ
coordinate of the input response, analogous to the bound in Corollary 1. We omit the details
| of this | extension        | from | the present | work.    |     |            |     |          |
| ------- | ---------------- | ---- | ----------- | -------- | --- | ---------- | --- | -------- |
| 6 A     | high-dimensional |      |             | example: |     | predicting |     | gene ex- |
pression
Here, we turn to a breast cancer gene expression study from The Cancer Genome Atlas
(TCGA) [45], distributed by Breheny and Huang [46]. Tumor samples from n = 536 patients
were assayed on Agilent mRNA expression microarrays, and measurements are on the log
scale. Following the example in Breheny and Huang [46], we treat BRCA1 expression as the
response and the remaining p = 17,322 genes as predictors, excluding 491 genes with missing
data. BRCA1 is the first gene identified whose mutations increase the risk of early onset
breast cancer, and because it is likely to interact with many others, those whose expression
| is related | to BRCA1 |     | are candidates | for further | study. |     |     |     |
| ---------- | -------- | --- | -------------- | ----------- | ------ | --- | --- | --- |
We divide the data into a 60/40 train/test split, with n = 321 and n = 215.
|     |     |     |     |     |     | train |     | test |
| --- | --- | --- | --- | --- | --- | ----- | --- | ---- |
The student model is lasso regression. For the teacher, we considered two candidates and
chose between them using cross-validated error as described in Section 2.3: TabPFN applied
to all 17,322 genes, and TabPFN applied to the 500 genes most correlated with BRCA1
expression, screened within each training fold. The screened teacher performed far better
and was selected. (The global lasso did not improve when restricted to the 500 gene subset.)
Note that in this setting, the teacher and student have different feature representations, as
in cross-modal distillation: the teacher uses 500 genes while the student uses all 17,322.
On this split, the global lasso had test PSE 0.189 (R2 = 0.579), TabPFN 0.150 (R2 =
0.666), and local distillation 0.148 (R2 = 0.670): a 22% reduction relative to the global lasso,
21

matching (here, slightly exceeding) its teacher, while retaining transparency. Additionally,
the local fits were sparser than the global lasso fit: the global fit selected 123 genes, while
the median local fit selected 94.2 Applying the stability screen of Section 4 (πˆ > 0.9 across
j
100 randomized refits) reduces this further: the local models retained a median of 15 stably
selected genes (IQR 13–17).
We then clustered the local models using 100 randomized fits with randomization scale
t = 0.1 and k = 5 clusters, with all parameters selected as described and exemplified in
Section4.3; theresultingclustersarevisualizedinFigure4. Theclustersrevealheterogeneity
across patients: FAM107A is selected almost only in cluster one, KLF14 almost only in
cluster five, both with negative coefficients, and both given a coefficient of zero by the
global lasso. These are reported tumor suppressors down-regulated in cancer [47, 48]. This
heterogeneity is not visible to a global linear model, and is difficult to surface in black-box
models.
C1 (mean -2.37) C2 (mean -1.84) C3 (mean -1.46) C4 (mean -1.07) C5 (mean -0.43)
FGFRL1
FAM107A
KLF14
0.10
CTXN3
FBXL13 0.05
TOP2A 0.00
CENPK
−0.05
RPL27
LOC201229 −0.10
POC1A
DTL
NBR2
Clustered test patient, ordered by predicted BRCA1 expression within cluster
tneicfifeoc
global local
coefficients coefficients
Figure 4: Local BRCA1-model coefficients across patient clusters. Columns are
test patients (n = 215); rows are the genes whose local coefficients vary most across clusters,
together with two of the largest-magnitude genes for reference. Patients are grouped into
five clusters using 100 randomized fits (Section 4.3), and ordered within cluster by teacher-
predicted BRCA1 expression ϕ ˆ (x∗). The leftmost column is the global lasso fit on the same
ˆ
training data, for comparison. Color scale is clipped at the 99th percentile of |β|.
2The PSE improvement was robust across 100 random 60/40 train/test splits, where local distillation
improvedonthegloballassoin96%ofruns, withamedianPSEreductionof22%. Thesparsitycomparison
was also stable: the median local fit was sparser than the global fit on 97 of 100 splits, with a median
reduction of 15% in the number of selected genes.
22

| 7 Benchmark |     | comparisons |     |     |
| ----------- | --- | ----------- | --- | --- |
Here, we use common machine learning benchmark datasets to compare local distillation to
(1) the student model (global lasso or ridge regression), (2) the teacher model (TabPFN or
XGBoost [49]) and (3) two local linear models (LOESS and local linear forests). We evaluate
on 17 regression datasets spanning sample sizes n ∈ [159,4177] and feature counts p ∈ [5,51].
The datasets are from the UCI Machine Learning Repository [50] (automobile, servo,
liver disorders, auto MPG, real estate valuation, infrared thermography temperature, student
performance) and the OpenML-CTR23 regression benchmark [51, 52] (cars, QSAR
fish toxicity, concrete compressive strength, socmob, airfoil self-noise, red wine, auction ver-
| ification, | space ga, abalone, | white | wine). |     |
| ---------- | ------------------ | ----- | ------ | --- |
For each dataset, we generate 20 random 80/20 train/test splits. We use a complete-case
design and perform one-hot encoding for categorical variables. Within each train/test split,
we normalize features using the mean and standard deviation of the training set. Per-dataset
| sample size | and feature | counts | are given in Appendix | Table 1. |
| ----------- | ----------- | ------ | --------------------- | -------- |
We compare methods using test R2, and we find that local distillation closely matches
the predictive performance of its teacher across a wide range of datasets. See Figure 5 for
representative examples, where local distillation is labeled as “LD (teacher, regularization)”.
For teacher models, we use TabPFN and XGBoost, and student regularization comparators
| are lasso | (L) and ridge | (R). Appendix | B shows complete | results. |
| --------- | ------------- | ------------- | ---------------- | -------- |
23

R2 comparison across methods
Datasets ordered by TabPFN's median R² improvement over the lasso.
Error bars represent 1 SE across 20 train/test splits.
airfoil self noise servo automobile
TabPFN
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
Lasso
Ridge
LLF
LOESS
socmob cars student performance
TabPFN
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
Lasso
Ridge
LLF
LOESS
0.50 1.00 0.50 1.00 0.50 1.00
Test R2
Figure 5: Predictive performance (test R2, median ± 1 standard error) for six
datasets from the UCI ML and OpenML repositories. Local distillation is labeled
as “LD (teacher, regularization)”, using “L” for lasso and “R” for ridge. When the teacher
outperforms the global linear model, local distillation usually approaches the teacher’s perfor-
mance. Plots for the remaining 11 datasets are included in Appendix B.
8 Discussion
Modern black-box models are presenting new opportunities for predictive modeling across
domains and data types, often with performance that classical methods cannot easily match
without significant feature engineering [14]. However, predictive models are only useful to
the extent that decision-makers can draw trustworthy conclusions from them. We posit that
well-constructed local linear models are in a “sweet spot” between interpretable modeling
and modern AI: they retain the benefits of linear models (transparent, easy to understand,
computationally simple) while rivaling the performance of black-box models. The statistical
principle underlying this intuition is familiar: a smooth regression surface is locally well
approximated by a linear model. But it is nontrivial to determine what constitutes local, how
the local models should be fit, and how the resulting collection of fits should be interpreted.
Local distillation, as proposed in this work, relies on a black-box “teacher” for prediction
and on randomized refits for interpretation. For prediction, the teacher plays two roles:
24

its predictions (1) define locality by determining which training observations inform the fit
at each query point, and (2) provide anchoring pseudo-observations. Across 17 benchmark
datasets and a high-dimensional gene expression example, and across a range of teacher
models (TabPFN, TabFM, XGBoost), local distillation consistently matches or approaches
the predictive accuracy of its teacher.
For interpretation, we apply a small amount of Gaussian randomization to the local dis-
tillation optimization, leaving both the loss and penalty unchanged. The randomized refits
identify which interpretations are sufficiently stable and therefore reliable, both at an in-
dividual test point (through selection frequencies) and across the test dataset as a whole
(through clustering into stable subgroups). Under the lasso penalty, we established theoret-
ical guarantees showing that this randomization yields stability under small perturbations
of the training responses. These results are of independent interest and extend beyond lo-
cal distillation, providing a general mechanism for stabilizing feature–selection probabilities
under lasso penalization.
Extensions. Section 2.3 suggests several extensions of local distillation. For example,
whenalinearstudentfailstorecovertheteacher’saccuracy, usingaricherstudentclass(with
interactions or transformations of the covariates) may narrow the gap. And, when there are
many candidate teacher models, the teacher may be selected through cross-validation with
the training data. Finally, local distillation can incorporate external datasets or other data
modalitiesthroughcross-modaldistillation, inwhichtheteacherisbuiltonadifferentfeature
set than the student. Our gene expression example provides one instance of this approach,
and we view distillation across genuinely different modalities as a promising avenue.
The distillation strength µˆ is estimated using a ratio of losses; this rule is intuitive and
it performed well in our experiments, but we have not made any claims about optimality.
We additionally use a hard cutoff to decide when to revert to the global linear model (when
µˆ ≤ 1, the estimated teacher error is worse than that of the student). We considered a
continuous alternative, weighting the teacher by its excess performance (µˆ−1) , but found
+
that this reduced predictive performance: when the teacher is stronger than the student,
the local fits benefit from a strong teacher weight. A similar observation was made in the
distillation paper from Hinton et al. [24], where they found the best results placed most of
the weight on the teacher’s soft targets rather than the true labels. Alternative approaches
to estimating µˆ and determining when to revert to a simpler model may nevertheless be
worth exploring.
25

Local regression more generally. Weviewlocallinearmodelingasageneralandflexible
framework that can compete with modern predictive methods, built from modular compo-
nents that can be chosen to suit the problem: the weights, which define locality (kernels
in LOESS, forest proximities, or, here, similarity of the teacher’s predictions); the penalty,
which defines structure (e.g., lasso, elastic-net, group lasso); and pseudo-observations, which
carry external information to anchor the fit (elicited priors, or, here, the teacher’s prediction
at the query point). The choice of weights deserves particular care, because the definition
of “local” determines which heterogeneity the local models can express. This is analogous
to unsupervised clustering, where many clusterings may be equally valid though not all
are equally informative; we expect different definitions of locality to likewise have differ-
ent virtues. Interpretation methods for local regression also require careful consideration:
conclusions drawn from the local fits are only reliable when they are stable, and the ap-
propriate notion of stability depends on the choice of locality. The stability theory under
Gaussian randomization is agnostic to the specific choice of weights in our approach, allow-
ing the guarantees to extend beyond our construction of local linear models. Their specific
form, however, may offer additional structure that can be exploited for deriving different
theoretical guarantees, which we leave for future investigation.
Local distillation is one instantiation of local linear modeling: a black-box teacher defines
locality and anchors each fit, and randomization assesses stability. Our results suggest
that this framework is a promising path toward predictive, interpretable, and trustworthy
statistical modeling.
Acknowledgements. We would like to thank Robert Tibshirani, Trevor Hastie and
Shihan Khan for helpful comments. The authors used Claude Opus 4.5 (model ID: claude-
opus-4-5-20251101) and ChatGPT 5.0 for coding support and text editing. The gene expres-
sion example shown here is based upon data generated by the TCGA Research Network:
https://www.cancer.gov/tcga.
Funding. S.P. was supported by NSF CAREER Award DMS-2337882.
Disclosure. The authors report there are no competing interests to declare.
Data availability. The data that support the findings of this study are public and cited
throughout. The scripts to download data and run simulations are published on Github
at https://github.com/erincr/local-distillation-benchmark. The breast cancer ex-
pression data are from The Cancer Genome Atlas (https://www.cancer.gov/tcga); we
use the processed version distributed with the hdrm R package (https://github.com/
pbreheny/hdrm).
26

References
[1] John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov,
ˇ
Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Z´ıdek, Anna
Potapenko, et al. Highly accurate protein structure prediction with AlphaFold. Na-
ture, 596(7873):583–589, 2021.
[2] Remi Lam, Alvaro Sanchez-Gonzalez, Matthew Willson, Peter Wirnsberger, Meire For-
tunato, Ferran Alet, Suman Ravuri, Timo Ewalds, Zach Eaton-Rosen, Weihua Hu,
et al. Learning skillful medium-range global weather forecasting. Science, 382(6677):
1416–1421, 2023.
[3] Noah Hollmann, Samuel Mu¨ller, Lennart Purucker, Arjun Krishnakumar, Max K¨orfer,
Shi Bin Hoo, Robin Tibor Schirrmeister, and Frank Hutter. Accurate predictions on
small data with a tabular foundation model. Nature, 637(8045):319–326, 2025.
[4] Christopher Kolberg, Jules Kreuer, Jonas Huurdeman, Sofiane Ouaari, Katharina
Eggensperger, and Nico Pfeifer. TabPFN-wide: Continued pre-training for extreme
feature counts. arXiv preprint arXiv:2510.06162, 2025.
[5] JunweiMa,ValentinThomas,RasaHosseinzadeh,AlexLabach,JesseCresswell,Keyvan
Golestan, Guangwei Yu, Anthony L Caterini, and Maks Volkovs. TabDPT: Scaling
tabular foundation models on real data. Advances in Neural Information Processing
Systems, 38, 2026.
[6] Weihao Kong and Abhimanyu Das. Introducing TabFM: A zero-shot foundation model
for tabular data. Google Research Blog, June 2026. URL https://research.google/
blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/.
Accessed July 7, 2026.
[7] Jingang Qu, David Holzmu¨ller, Ga¨el Varoquaux, and Marine Le Morvan. TabICL:
A tabular foundation model for in-context learning on large data. arXiv preprint
arXiv:2502.05564, 2025.
[8] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. “why should I trust you?”:
Explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, pages 1135–1144,
2016.
27

[9] Scott M Lundberg and Su-In Lee. A unified approach to interpreting model predictions.
Advances in Neural Information Processing Systems, 30, 2017.
[10] Damien Garreau and Ulrike von Luxburg. Explaining the explainer: A first theoretical
analysis of LIME. In International Conference on Artificial Intelligence and Statistics,
pages 1287–1296. PMLR, 2020.
[11] Dylan Slack, Sophie Hilgard, Emily Jia, Sameer Singh, and Himabindu Lakkaraju.
Fooling LIME and SHAP: Adversarial attacks on post hoc explanation methods. In
Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, pages 180–186,
2020.
[12] I Elizabeth Kumar, Suresh Venkatasubramanian, Carlos Scheidegger, and Sorelle
Friedler. Problems with Shapley-value-based explanations as feature importance mea-
sures. In International Conference on Machine Learning, pages 5491–5500. PMLR,
2020.
[13] KjerstiAas, MartinJullum, andAndersLøland. Explainingindividualpredictionswhen
features are dependent: More accurate approximations to Shapley values. Artificial
Intelligence, 298:103502, 2021.
[14] Cynthia Rudin. Stop explaining black box machine learning models for high stakes
decisions and use interpretable models instead. Nature Machine Intelligence, 1(5):206–
215, 2019.
[15] R. Quinlan. Auto mpg. UCI Machine Learning Repository, 1993. https://doi.org/
10.24432/C5859H. Dataset from the 1983 American Statistical Association Data Expo-
sition.
[16] William S Cleveland and Susan J Devlin. Locally weighted regression: an approach to
regression analysis by local fitting. Journal of the American Statistical Association, 83
(403):596–610, 1988.
[17] Rui Qiu, Zhou Yu, and Ruoqing Zhu. Random forest weighted local Fr´echet regression
with random objects. Journal of Machine Learning Research, 25(107):1–69, 2024.
[18] Adam Bloniarz, Ameet Talwalkar, Bin Yu, and Christopher Wu. Supervised neighbor-
hoods for distributed nonparametric regression. In Artificial Intelligence and Statistics,
pages 1450–1459. PMLR, 2016.
28

[19] Rina Friedberg, Julie Tibshirani, Susan Athey, and Stefan Wager. Local linear forests.
Journal of Computational and Graphical Statistics, 30(2):503–517, 2020.
[20] Susan Athey, Julie Tibshirani, and Stefan Wager. Generalized random forests. The
| Annals       | of Statistics, |     | 47(2):1148–1178, |                  | April | 2019. |     |
| ------------ | -------------- | --- | ---------------- | ---------------- | ----- | ----- | --- |
| [21] Bin Yu. | Stability.     |     | Bernoulli,       | 19(4):1484–1500, |       | 2013. |     |
[22] Bin Yu and Karl Kumbier. Veridical data science. Proceedings of the National Academy
| of Sciences, |     | 117(8):3920–3929, |     | 2020. |     |     |     |
| ------------ | --- | ----------------- | --- | ----- | --- | --- | --- |
[23] Zachary T Rewolinski and Bin Yu. PCS workflow for veridical data science in the age
| of AI. | arXiv | preprint | arXiv:2508.00835, |     |     | 2025. |     |
| ------ | ----- | -------- | ----------------- | --- | --- | ----- | --- |
[24] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural
| network. | arXiv | preprint | arXiv:1503.02531, |     |     | 2015. |     |
| -------- | ----- | -------- | ----------------- | --- | --- | ----- | --- |
[25] Joseph B Kadane, James M Dickey, Robert L Winkler, Wayne S Smith, and Stephen C
Peters. Interactive elicitation of opinion for a normal linear model. Journal of the
| American | Statistical |     | Association, | 75(372):845–854, |     |     | 1980. |
| -------- | ----------- | --- | ------------ | ---------------- | --- | --- | ----- |
[26] Edward J Bedrick, Ronald Christensen, and Wesley Johnson. A new perspective on
priors for generalized linear models. Journal of the American Statistical Association, 91
| (436):1450–1460, |     |     | 1996. |     |     |     |     |
| ---------------- | --- | --- | ----- | --- | --- | --- | --- |
[27] Joseph G Ibrahim and Ming-Hui Chen. Power prior distributions for regression models.
| Statistical | Science, |     | 15(1):46–60, | 2000. |     |     |     |
| ----------- | -------- | --- | ------------ | ----- | --- | --- | --- |
[28] Jerome Friedman, Trevor Hastie, and Robert Tibshirani. Regularization paths for gen-
eralized linear models via coordinate descent. Journal of Statistical Software, 33(1):
| 1–22, | 2010. |     |     |     |     |     |     |
| ----- | ----- | --- | --- | --- | --- | --- | --- |
[29] James Yang and Trevor Hastie. A fast and scalable pathwise-solver for group lasso
and elastic net penalized regression via block-coordinate descent. arXiv preprint
| arXiv:2405.08631, |     |     | 2024. |     |     |     |     |
| ----------------- | --- | --- | ----- | --- | --- | --- | --- |
[30] Michael Lim and Trevor Hastie. Learning interactions via hierarchical group-lasso reg-
ularization. Journal of Computational and Graphical Statistics, 24(3):627–654, 2015.
[31] Guo Yu, Jacob Bien, and Ryan Tibshirani. Reluctant interaction modeling. arXiv
| preprint | arXiv:1907.08414, |     |     | 2019. |     |     |     |
| -------- | ----------------- | --- | --- | ----- | --- | --- | --- |
29

[32] Erin Craig and Robert Tibshirani. Supervised learning pays attention. arXiv preprint
arXiv:2512.09912, 2025.
[33] Gregory Plumb, Denali Molitor, and Ameet S Talwalkar. Model agnostic supervised
local explanations. Advances in Neural Information Processing Systems, 31, 2018.
[34] Anastasios N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I. Jordan, and
Tijana Zrnic. Prediction-powered inference. Science, 382(6671), 2023. doi: 10.1126/
science.adi6000.
[35] Anastasios N Angelopoulos, John C Duchi, and Tijana Zrnic. PPI++: Efficient
prediction-powered inference. arXiv preprint arXiv:2311.01453, 2023.
[36] Xiaoying Tian and Jonathan Taylor. Selective inference with a randomized response.
The Annals of Statistics, 46(2):679–710, 2018.
[37] Snigdha Panigrahi, Junjie Zhu, and Chiara Sabatti. Selection-adjusted inference: an
application to confidence intervals for cis-eqtl effect sizes. Biostatistics, 22(1):181–197,
2021.
[38] Soham Bakshi, Walter Dempsey, and Snigdha Panigrahi. Selective inference for time-
varying effect moderation. arXiv preprint arXiv:2411.15908, 2024.
[39] Yiling Huang, Sarah Pirenne, Snigdha Panigrahi, and Gerda Claeskens. Selective infer-
ence using randomized group lasso estimators for general models. Electronic Journal of
Statistics, 19(2):3489–3531, 2025.
[40] Ronan Perry, Snigdha Panigrahi, and Daniela Witten. Post-selection inference for pe-
nalized m-estimators via score thinning. arXiv preprint arXiv:2601.13514, 2026.
[41] Nicolai Meinshausen and Peter Bu¨hlmann. Stability selection. Journal of the Royal
Statistical Society: Series B (Statistical Methodology), 72(4):417–473, 2010.
[42] AnaLNFredandAnilKJain. Combiningmultipleclusteringsusingevidenceaccumula-
tion. IEEE Transactions on Pattern Analysis and Machine Intelligence, 27(6):835–850,
2005.
[43] Ryan J. Tibshirani. The lasso problem and uniqueness. Electronic Journal of Statistics,
7:1456–1490, 2013.
30

[44] Olivier Bousquet and Andr´e Elisseeff. Stability and generalization. Journal of Machine
| Learning | Research, | 2(Mar):499–526, |     | 2002. |     |     |
| -------- | --------- | --------------- | --- | ----- | --- | --- |
[45] The Cancer Genome Atlas Network. Comprehensive molecular portraits of human
breast tumours. Nature, 490(7418):61–70, 2012. doi: 10.1038/nature11412.
[46] Patrick Breheny and Jian Huang. hdrm: High-dimensional regression modeling, 2025.
URL https://github.com/pbreheny/hdrm. R package version 0.17.1.
[47] Dehua Ou, Zhiqin Zhang, Zesong Wu, Peilin Shen, Yichuan Huang, Sile She, Sifan
She, and Ming-en Lin. Identification of the putative tumor suppressor characteristics of
FAM107A via pan-cancer analysis. Frontiers in Oncology, 12:861281, 2022.
[48] JianChu, Xing-ChiHu, Chang-ChunLi, Tang-YaLi, Hui-WenFan, andGuo-QinJiang.
KLF14alleviatedbreastcancerinvasionandm2macrophagespolarizationthroughmod-
ulating SOCS3/RhoA/Rock/STAT3 signaling. Cellular Signalling, 92:110242, 2022.
[49] Tianqi Chen and Carlos Guestrin. XGBoost: A scalable tree boosting system. In Pro-
ceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery
| and Data | Mining, | pages | 785–794, | 2016. |     |     |
| -------- | ------- | ----- | -------- | ----- | --- | --- |
[50] Markelle Kelly, Rachel Longjohn, and Kolby Nottingham. The uci machine learning
| repository. | https://archive.ics.uci.edu, |     |     |     | 2025. |     |
| ----------- | ---------------------------- | --- | --- | --- | ----- | --- |
[51] Bernd Bischl, Giuseppe Casalicchio, Matthias Feurer, Pieter Gijsbers, Frank Hutter,
Michel Lang, Rafael G Mantovani, Jan N van Rijn, and Joaquin Vanschoren. OpenML
| benchmarking | suites. | arXiv | preprint | arXiv:1708.03731, |     | 2017. |
| ------------ | ------- | ----- | -------- | ----------------- | --- | ----- |
[52] SebastianFelixFischer, MatthiasFeurer, andBerndBischl. OpenML-CTR23–acurated
tabular regression benchmarking suite. In AutoML Conference 2023 (Workshop), 2023.
| A Details | of      | theoretical |     | results |     |     |
| --------- | ------- | ----------- | --- | ------- | --- | --- |
| A.1 Proof | of main | results     |     |         |     |     |
P
Proof of Lemma 1. Let π◦(z) = [j ∈ E(cid:98) (z,ω)] denote the selection probability of pre-
|     |     | j   | ω   | V   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
dictor j under lasso regression of z+ω on V , evaluated as a function of the weight-adjusted
31

| response | z.  | Then, | by definition, |     |     |           |         |      |        |     |     |     |
| -------- | --- | ----- | -------------- | --- | --- | --------- | ------- | ---- | ------ | --- | --- | --- |
|          |     |       |                |     |     | (cid:0)   | (cid:1) |      |        |     |     |     |
|          |     |       |                | π   | (y) | = π◦ z(y) |         | = π◦ | ◦z(y). |     |     |     |
|          |     |       |                |     | j   | j         |         | j    |        |     |     |     |
√
√
The map y (cid:55)→ z(y) has entries S y for k ≤ n and µn−1/4ϕ ˆ (x∗;y) for k = n+1; the
|     |     |     |     |     |     | k k |     |     |     | eff |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
first n entries are linear in y, while the final entry is k times differentiable by assumption,
|         |          | Rn      | Rn+1 |       |       |                 |     |     |     |     |     |     |
| ------- | -------- | ------- | ---- | ----- | ----- | --------------- | --- | --- | --- | --- | --- | --- |
| and     | hence, z | :       | →    | is k  | times | differentiable. |     |     |     |     |     |     |
| Observe |          | that we | can  | write |       |                 |     |     |     |     |     |     |
(cid:90)
|     | π◦(z) |     | P (cid:2) |                     | (cid:3) |     |      |      |       |     |       |       |
| --- | ----- | --- | --------- | ------------------- | ------- | --- | ---- | ---- | ----- | --- | ----- | ----- |
|     |       | :=  |           | j ∈ E(cid:98) (z,ω) |         | =   | χ (z | +w)φ | (w)dw | =   | (χ ∗φ | )(z), |
|     | j     |     | ω         | V                   |         |     | j    |      | τ     |     | j     | τ     |
Rn+1
N(0,τ2I
where χ (t) = 1{j ∈ E(cid:98)(t)}, and φ (u) is the ) density function at u.
|     | j   |     |     |     | τ   |     |     |     | n+1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Since χ is bounded and φ has integrable derivatives of all orders, differentiation under
|     | j   |     |     | τ   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the integral sign yields π◦ ∈ C∞(Rn+1), with ∂απ◦ = χ ∗ ∂αφ for every multi-index α.
|     |     |     |     | j   |     |     |     | j   | j   | τ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Applying the chain rule to π = π◦ ◦z shows that, for each r ≤ k, every derivative of π of
|     |     |     |     | j   | j   |     |     |     |     |     |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
π◦
order r can be expressed in terms of derivatives of and derivatives of z of order at most
j
r. Since all such derivatives exist, π is k times differentiable on Rn.
j
Proof of Theorem 1. Combining Proposition 1 with Lemma 9 (both stated in Appendix A.3)
Rn
| yields, | for any | y ∈ | and | i ∈ [n], | that |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
(cid:114)
|     |     |     |        |     | 2 1 | (cid:110)(cid:112) |           |     |                |     | (cid:111) |     |
| --- | --- | --- | ------ | --- | --- | ------------------ | --------- | --- | -------------- | --- | --------- | --- |
|     |     |     |        |     |     |                    | (cid:112) |     | ˆ              |     |           |     |
|     |     | |∂  | π (y)| | ≤   |     | S ρV               | +         | S   | |∂ ϕ (x∗;y)|ρV |     |           |     |
|     |     |     | i j    |     |     | i                  | ij        | n+1 | i              |     | n+1,j     |     |
π τ
|     |     |     |     | (cid:114) |     | (cid:40) |     | ˆ         | (cid:41) |     |     |     |
| --- | --- | --- | --- | --------- | --- | -------- | --- | --------- | -------- | --- | --- | --- |
|     |     |     |     |           | 2 C | 1        | |∂  | ϕ (x∗;y)| |          |     |     |     |
i
|     |     |     |     | ≤   |     | √   | +   |      | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     | π τ | n   |     | n1/4 |     |     |     |     |
eff
eff
| Taking | supremum    |     | over | y and i  | ∈ [n] | proves       | our claim. |       |     |            |     |       |
| ------ | ----------- | --- | ---- | -------- | ----- | ------------ | ---------- | ----- | --- | ---------- | --- | ----- |
| A.2    | Theoretical |     |      | analysis |       | of stability |            | under |     | randomized |     | lasso |
Throughout this section, we study the stability of the feature–selection probabilities
|     |     |     |     |     |       |     | (cid:104) |                 | (cid:105) |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --------- | --------------- | --------- | --- | --- | --- |
|     |     |     |     |     | π◦(z) | P   |           |                 |           |     |     |     |
|     |     |     |     |     |       | =   | j ∈       | E(cid:98) (z,ω) | .         |     |     |     |
|     |     |     |     |     | j     | ω   |           | V               |           |     |     |     |
with respect to perturbations in z. The main result of this section, Theorem 2, character-
izes the sensitivity of feature-selection probabilities to perturbations in the response under
| randomized |     | lasso | regression. |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
32

| A.2.1 | Leave-j-out |        | score and  | lasso       | geometry |       |     |     |          |     |     |
| ----- | ----------- | ------ | ---------- | ----------- | -------- | ----- | --- | --- | -------- | --- | --- |
| For a | feature j   | ∈ [p], | define the | leave-j-out |          | lasso |     |     |          |     |     |
|       |             |        |            |             | (cid:26) |       |     |     | (cid:27) |     |     |
1
|     |     |     | (−j)(z)   |          |     |       | b∥2  |       |     |     |      |
| --- | --- | --- | --------- | -------- | --- | ----- | ---- | ----- | --- | --- | ---- |
|     |     |     | β(cid:98) | = argmin |     | ∥z −V |      | +λ∥b∥ | .   |     | (10) |
|     |     |     | V         |          |     | 2     | −j 2 |       | 1   |     |      |
b∈Rp−1
Furthermore, let RV (z) = z −V β(cid:98) (−j)(z) be the leave-j-out residual, and define
|     |     | −j  |     | −j  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
V
|     |     |     |     | TV(z) | =   | V ⊤RV | (z). |     |     |     | (11) |
| --- | --- | --- | --- | ----- | --- | ----- | ---- | --- | --- | --- | ---- |
|     |     |     |     | j     |     | j     | −j   |     |     |     |      |
Lemma 2 (KKT characterization). Under Assumption 1, it holds that
|TV(z
|       |          |            | j ∈/ E(cid:98) | (z,ω) | ⇐⇒  |     | +ω)| | ≤ λ, |     |     |     |
| ----- | -------- | ---------- | -------------- | ----- | --- | --- | ---- | ---- | --- | --- | --- |
|       |          |            |                | V     |     |     | j    |      |     |     |     |
| where | TV(·) is | as defined | in (11).       |       |     |     |      |      |     |     |     |
j
Proof. Set t = z +ω. By definition, E(cid:98) (z,ω) is the support of the full Lasso solution with
V
response t. The KKT conditions for the full Lasso problem state that a vector β ∈ Rp is
| optimal | if and | only if | there exists | γ ∈ | Rp such | that |       |     |     |     |      |
| ------- | ------ | ------- | ------------ | --- | ------- | ---- | ----- | --- | --- | --- | ---- |
|         |        |         |              | V   | ⊤(t−V   | β)   | = λγ, |     |     |     | (12) |

|        |           |     |          | sign(β | ),  | β   | ̸= 0, |     |     |     |     |
| ------ | --------- | --- | -------- | ------- | --- | --- | ----- | --- | --- | --- | --- |
|        |           |     |          |         | k   | k   |       |     |     |     |     |
| where, | for every | k ∈ | [p], γ = |         |     |     |       |     |     |     |     |
k
|     |         |     |     | u ∈ [−1,1], |     | β   | = 0. |     |     |     |          |
| --- | ------- | --- | --- | ------------ | --- | --- | ---- | --- | --- | --- | -------- |
|     |         |     |     | k            |     | k   |      |     |     |     |          |
|     | (−j)(t) |     |     |              |     |     |      |     |     |     | (−j)(t). |
Let β(cid:98) be the solution of the leave-j-out Lasso, and define RV (t) = t−V β(cid:98)
|     | V   |     |     |     |     |     |     |     | −j  | −j  | V   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rp−1
The KKT conditions for the restricted problem imply that there exists γ ∈ such that
−j
|     |     |     |     | V   | ⊤RV   | (t) = | λγ , |     |     |     | (13) |
| --- | --- | --- | --- | --- | ----- | ----- | ---- | --- | --- | --- | ---- |
|     |     |     |     |     | −j −j |       | −j   |     |     |     |      |
with

|     |     |     |      | sign | (cid:0) β(cid:98) | (−j)(t) (cid:1) | , β(cid:98) (−j)(t) | ̸=  | 0,  |     |     |
| --- | --- | --- | ---- | ----- | ----------------- | --------------- | ------------------- | --- | --- | --- | --- |
|     |     |     | (γ ) | =     |                   | V,k             | V,k                 |     |     |     |     |
−j k
(−j)(t)
|     |           |     |               | u              | ∈ [−1,1], |              | β(cid:98)          | =   | 0.  |     |     |
| --- | --------- | --- | ------------- | --------------- | --------- | ------------ | ------------------ | --- | --- | --- | --- |
|     |           |     |               |                 | k         |              | V,k                |     |     |     |     |
| Now | construct | the | p-dimensional | candidate       |           | β(cid:101)   | with               |     |     |     |     |
|     |           |     |               | β(cid:101) = 0, |           | β(cid:101) = | β(cid:98) (−j)(t). |     |     |     |     |
|     |           |     |               | j               |           | −j           |                    |     |     |     |     |
V
Its residual in the full Lasso problem is exactly t − V β(cid:101) = RV (t). Equation (13) verifies
−j
the full KKT conditions for every coordinate other than j. Since β(cid:101) = 0, the remaining
j
33

KKT condition is V ⊤RV (t) ∈ λ[−1,1]. By definition, TV(t) = V ⊤RV (t), which gives
|     |     |     |     | j −j |     |     |     |     | j   | j   | −j  |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|TV(t)|
|     | ≤   | λ. Therefore, |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
|TV(t)|
≤ λ ⇐⇒ β(cid:101) is a solution of the full Lasso problem. (14)
j
If |TV(t)| ≤ λ, then (14) shows that β(cid:101) is a full Lasso solution. By uniqueness of the
j
full Lasso solution, guaranteed by Assumption 1, β(cid:98)(t) = β(cid:101). Since β(cid:101) = 0, it follows that
j
j ∈/ E(cid:98) (z,ω).
V
Conversely, suppose that j ∈/ E(cid:98) (z,ω), so that β(cid:98) (t) = 0. The vector β(cid:98) (t) must then
|     |     |     |     |     |     | V   |     | j   |     |     | −j  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rp−1
solve the leave-j-out problem. Indeed, if some b ∈ had a strictly smaller restricted
objective, then the full vector (b,0) would have a strictly smaller full Lasso objective than
β(cid:98)(t), contradicting its optimality. By uniqueness of the restricted solution, implied by
Assumption 1, β(cid:98) (t) = β(cid:98) (−j)(t). The full KKT condition at the zero coefficient β(cid:98) (t) = 0
|               |       |         | −j  | V       |           |          |           |                  |      |     | j   |
| ------------- | ----- | ------- | --- | ------- | --------- | -------- | --------- | ---------------- | ---- | --- | --- |
| therefore     | gives |         |     |         |           |          |           |                  |      |     |     |
|               |       |         |     |         | (cid:12)  | (cid:16) |           | (cid:17)(cid:12) |      |     |     |
|               |       |         |     |         | (cid:12)V | ⊤        |           | (−j)(t) (cid:12) |      |     |     |
|               |       |         |     |         |           | t−V      | β(cid:98) |                  | ≤ λ. |     |     |
|               |       |         |     |         | (cid:12)  | j        | −j        | V (cid:12)       |      |     |     |
| Equivalently, |       | |TV(t)| |     | ≤ λ. We | have      | thus     | proved    |                  |      |     |     |
j
|     |     |     |     |     | j ∈/ E(cid:98) | (z,ω) | ⇐⇒  | |TV(t)| | ≤ λ. |     |     |
| --- | --- | --- | --- | --- | -------------- | ----- | --- | ------- | ---- | --- | --- |
|     |     |     |     |     |                | V     |     | j       |      |     |     |
Having characterized the lasso active set through the leave-j-out score, we now turn to
the analysis of this score. To this end, we introduce some additional notation. For an active
set E ⊆ [p]\{j} and sign vector s ∈ {−1,1}|E|, define the polyhedral selection region
|     |     |       |           | (cid:110) |      | (cid:0) |                   | (cid:1)   | (cid:0)                | (cid:1) | (cid:111) |
| --- | --- | ----- | --------- | --------- | ---- | ------- | ----------------- | --------- | ---------------------- | ------- | --------- |
|     |     | RV,−j |           | = z ∈     | Rn : | supp    | β(cid:98) (−j)(z) | = E,      | sign β(cid:98) (−j)(z) |         | = s ,     |
|     |     |       | E,s       |           |      |         | V                 |           | V,E                    |         |           |
|     |     |       | (cid:110) |           |      |         |                   | (cid:111) |                        |         |           |
(cid:0) RV,−j(cid:1)
and let EV = E : Leb > 0 for some s be the set of essential active sets from
|     | −j  |     |     | n   | E,s |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lasso regression on V , i.e., whose corresponding selection regions have positive Lebesgue
−j
measure.
Lemma 3 (Almost-everywhere gradient of the score). For every z ∈ ∪ int(RV,−j), let
E,s
E,s
|     | (cid:0) |                   | (cid:1) |      |     |     |     |     |     |     |     |
| --- | ------- | ----------------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| E = | supp    | β(cid:98) (−j)(z) | .       | Then |     |     |     |     |     |     |     |
V
|       |     |     |       |      |        | ∇TV(z) | =   | P⊥ V , |     |     |     |
| ----- | --- | --- | ----- | ---- | ------ | ------ | --- | ------ | --- | --- | --- |
|       |     |     |       |      |        |        | j   | VE j   |     |     |     |
| where | P   | = V | (V ⊤V | )−1V | ⊤, and | P⊥     | = I | −P .   |     |     |     |
|       | VE  |     | E E   | E    | E      | VE     |     | VE     |     |     |     |
34

int(RV,−j),
Proof. Fix z ∈ ∪ and let (E,s) denote the support and sign of the leave-j-out
|     |     | E,s |     | E,s |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lasso solution. Assumption 1 implies that V has full column rank, and therefore
E
|            |      |               |     | (−j)(z)   |            |      | ⊤V   | )−1(V | ⊤z   |     |     |     |     |
| ---------- | ---- | ------------- | --- | --------- | ---------- | ---- | ---- | ----- | ---- | --- | --- | --- | --- |
|            |      |               |     | β(cid:98) |            | = (V |      |       | −λs) |     |     |     |     |
|            |      |               |     | V,E       |            |      | E E  |       | E    |     |     |     |     |
| throughout | this | neighborhood. |     |           | It follows |      | that |       |      |     |     |     |     |
(−j)(z)
|     |     | RV  | (z) | = z −V |     | β(cid:98) | =   | P⊥ z | +λV | (V ⊤V | )−1s, |     |     |
| --- | --- | --- | --- | ------ | --- | --------- | --- | ---- | --- | ----- | ----- | --- | --- |
|     |     |     | −j  |        | E   | V,E       |     | VE   |     | E E   | E     |     |     |
and therefore,
|     |     |     |     |        |     | (cid:0) |       |     | (cid:1) |      |     |     |     |
| --- | --- | --- | --- | ------ | --- | ------- | ----- | --- | ------- | ---- | --- | --- | --- |
|     |     |     |     | ∇TV(z) | =   | ∇       | V ⊤RV | (z) | = P⊥    | V .  |     |     |     |
|     |     |     |     | j      |     |         | j     | −j  |         | VE j |     |     |     |
Here, z ∈ ∪ int(RV,−j) guarantees that z is in the interior of RV,−j, and therefore (E,s)
|               | E,s |         | E,s          |     |     |      |        |                  |     |     | E,s |       |     |
| ------------- | --- | ------- | ------------ | --- | --- | ---- | ------ | ---------------- | --- | --- | --- | ----- | --- |
| stay constant | in  | a local | neighborhood |     |     | of z | during | differentiation. |     |     |     |       |     |
|               |     |         |              |     |     |      |        |                  | vV  | Vj  |     | rV P⊥ |     |
Lemma 4 (Sandwich-bound on leave-j-out score). Let = and = V . For
|         |        |     |        |         |     |        |     |     |        | j ∥Vj∥2  |     | j|E VE | j   |
| ------- | ------ | --- | ------ | ------- | --- | ------ | --- | --- | ------ | -------- | --- | ------ | --- |
| every z | ∈ Rn+1 | and | h > 0, |         |     |        |     |     |        |          |     |        |     |
|         |        |     | TV(z   | −ρVhvV) |     | ≤ TV(z | +he | )   | ≤ TV(z | +ρVhvV), |     |        |     |
i
|        |                |     | j   | ij  | j    | j   |     |      | j     | ij  | j   |     |     |
| ------ | -------------- | --- | --- | --- | ---- | --- | --- | ---- | ----- | --- | --- | --- | --- |
| where, | for i ∈ [n+1], |     |     |     |      |     |     |      |       |     |     |     |     |
|        |                |     |     |     |      |     |     | |(rV | ) |∥V | ∥   |     |     |     |
|        |                |     |     |     |      |     |     |      | i     | j 2 |     |     |     |
|        |                |     |     | ρV  | =    | sup |     | j|E  |       | .   |     |     |     |
|        |                |     |     |     | ij   |     |     | ∥rV  | ∥2    |     |     |     |     |
|        |                |     |     |     | E∈EV | ,rV | ̸=0 |      | j|E 2 |     |     |     |     |
−j j|E
Proof. By Lemma 3, for almost every z, if E ∈ EV is the locally active leave-j-out model
−j
at z, then
∥rV ∥2
|     |     |     |     |         |     | (cid:0) | (cid:1)⊤ |      |     |        |     |     |     |
| --- | --- | --- | --- | ------- | --- | ------- | -------- | ---- | --- | ------ | --- | --- | --- |
|     |     |     |     | D TV(z) |     | = rV    |          | vV = | j|E | 2 ≥ 0. |     |     |     |
V
|      |          |                |     | v j | j         |       | j|E    | j   | ∥V  | ∥   |     |     |     |
| ---- | -------- | -------------- | --- | --- | --------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
|      |          |                |     |     |           |       |        |     | j   | 2   |     |     |     |
| When | rV ̸= 0, | the definition |     | of  | ρV        | gives |        |     |     |     |     |     |     |
|      | j|E      |                |     |     | ij        |       |        |     |     |     |     |     |     |
|      |          |                |     |     | |∂ TV(z)| |       | = |(rV | ) | |     |     |     |     |     |
|      |          |                |     |     | i         |       |        | i   |     |     |     |     |     |
|      |          |                |     |     |           | j     |        | j|E |     |     |     |     |     |
∥rV ∥2
|     |     |     |     |     |     |     | ≤ ρV  | j|E    | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | ij    | ∥V     | ∥   |     |     |     |     |
|     |     |     |     |     |     |     |       | j      | 2   |     |     |     |     |
|     |     |     |     |     |     |     | = ρVD | TV(z). |     |     |     |     |     |
|     |     |     |     |     |     |     | ij    | vV     | j   |     |     |     |     |
j
| When | rV = 0, | both | sides | vanish. | Hence, |     |     |     |     |     |     |     |     |
| ---- | ------- | ---- | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
j|E
|     |     |     |     |     | |∂  | TV| | ≤ ρVD |       | TV  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | i j |       | ij vV | j   |     |     |     |     |
j
| Lebesgue-almost |     | everywhere. |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
35

By linearity of directional derivatives in the direction of differentiation, it follows almost
| everywhere | that  |       |     |               |           |         |      |       |         |      |     |     |     |
| ---------- | ----- | ----- | --- | ------------- | --------- | ------- | ---- | ----- | ------- | ---- | --- | --- | --- |
|            |       |       |     | D             |           | TV =    | ∂ TV | +ρVD  | TV      | ≥ 0, |     |     |     |
|            |       |       |     |               | ei+ρV v V | j       | i j  | ij    | v V j   |      |     |     |     |
|            |       |       |     |               | ij j      |         |      |       | j       |      |     |     |     |
|            |       |       |     |               |           | TV      | ρVD  | TV    | TV      |      |     |     |     |
|            |       |       |     | D             |           | =       |      |       | −∂      | ≥ 0. |     |     |     |
|            |       |       |     |               | ρV v V−ei | j       | ij   | v V j | i j     |      |     |     |     |
|            |       |       |     |               | ij j      |         |      | j     |         |      |     |     |     |
| To         | apply | Lemma | 6,  | observe       | that      |         |      |       |         |      |     |     |     |
|            |       |       |     |               |           | −ρVhvV) |      |       | +ρVvV), |      |     |     |     |
|            |       |       |     | (z +he        | )−(z      |         |      | =     | h(e     |      |     |     |     |
|            |       |       |     |               | i         |         | ij   | j     | i       | ij j |     |     |     |
|            |       |       |     | (z +ρVhvV)−(z |           |         | +he  | ) =   | h(ρVvV  | −e   | ).  |     |     |
|            |       |       |     |               | ij j      |         |      | i     | ij j    | i    |     |     |     |
Thus, applying the lemma first from z−ρVhvV in direction e +ρVvV, and then from z+he
|     |     |     |     |     |     |     | ij j |     |     | i ij | j   |     | i   |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
ρVvV
| in direction |           |        | −e ,  | gives   |                   |      |     |               |      |          |     |     |     |
| ------------ | --------- | ------ | ----- | ------- | ----------------- | ---- | --- | ------------- | ---- | -------- | --- | --- | --- |
|              |           | ij j   | i     |         |                   |      |     |               |      |          |     |     |     |
|              |           |        | TV(z  | −ρVhvV) |                   | TV(z |     |               | TV(z | +ρVhvV). |     |     |     |
|              |           |        |       |         |                   | ≤    | +he | )             | ≤    |          |     |     |     |
|              |           |        | j     |         | ij j              | j    |     | i             | j    | ij       | j   |     |     |
| This proves  | the       | claim. |       |         |                   |      |     |               |      |          |     |     |     |
| A.2.2        | Stability |        | bound | for     | feature–selection |      |     | probabilities |      |          |     |     |     |
Lemma 5 (Bounding probabilities under randomization). Let A ⊆ Rn+1 be measurable and
define
|     |     |     |     |       | P    |     |       |                    | N(0,τ2I |     |         |     |     |
| --- | --- | --- | --- | ----- | ---- | --- | ----- | ------------------ | ------- | --- | ------- | --- | --- |
|     |     |     |     | p (z) | = (z | +ω  | ∈ A), |                    | ω ∼     |     | ).      |     |     |
|     |     |     |     | A     | ω    |     |       |                    |         |     | n       |     |     |
|     |     |     |     |       |      |     |       | E (cid:2) (v⊤ω)1{z |         |     | (cid:3) |     |     |
Then, for every unit vector v, D p (z) = 1 +ω ∈ A} , and |D p (z)| ≤
|     |     |     |     |     | v   | A   | τ2  | ω   |     |     |     | v   | A   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
√ .
τ 2π
| Proof. | Differentiation |     | under |     | the Gaussian |     | convolution |     | gives | us  |     |     |     |
| ------ | --------------- | --- | ----- | --- | ------------ | --- | ----------- | --- | ----- | --- | --- | --- | --- |
1
|     |     |     |     | D   | p (z) = | E   | (cid:2) (v⊤ω)1{z |     | +ω  | ∈ A} (cid:3) | .   |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ---------------- | --- | --- | ------------ | --- | --- | --- |
|     |     |     |     | v   | A       |     | ω                |     |     |              |     |     |     |
τ2
|              | v⊤ω, |       |     | N(0,τ2) |       |         |       |      |                 |     |               |     |     |
| ------------ | ---- | ----- | --- | ------- | ----- | ------- | ----- | ---- | --------------- | --- | ------------- | --- | --- |
| If           | G =  | then  | G   | ∼       |       | and     |       |      |                 |     |               |     |     |
|              | −E   |       |     | E       | [G1{z |         |       | E    |                 |     |               |     |     |
|              |      | [(−G) | ] ≤ |         |       | +ω ∈    | A}]   | ≤ [G | ], where        |     | G = max{G,0}. |     |     |
|              |      | ω     | +   | ω       |       |         |       | ω    | +               |     | +             |     |     |
|              |      | E     |     | E       |       |         |       |      |                 |     |               |     |     |
| By symmetry, |      | [G    | ] = |         | [(−G) | ] = √ τ | , and | the  | result follows. |     |               |     |     |
|              |      | ω     | +   | ω       | +     |         |       |      |                 |     |               |     |     |
2π
Theorem 2 (Sensitivity bound for selection probabilities under randomized lasso). Under
| Assumption | 1,  | for | every | z ∈ | Rn+1 and | i   | ∈ [n+1], |     |     |     |     |     |     |
| ---------- | --- | --- | ----- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
(cid:114)
2ρV
|     |     |     |     |     |     | π◦(z)| |     |     | ij  |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | |∂     | ≤   |     | .   |     |     |     | (15) |
|     |     |     |     |     |     | i j    |     | π   | τ   |     |     |     |      |
36

| Consequently, |     | we have |     |     |     |          |     |           |     |     |     |      |
| ------------- | --- | ------- | --- | --- | --- | -------- | --- | --------- | --- | --- | --- | ---- |
|               |     |         |     |     |     |          |     | (cid:114) | 2aV |     |     |      |
|               |     |         |     |     | sup | ∥∇π◦(z)∥ |     | ≤         | j   | ,   |     | (16) |
∞
|     |     |     |     |     |     |     | j   |     | π τ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
z∈Rn
where
∥rV
|     |     |     |     |     |         |     |      |     |     | ∥ ∥V   | ∥   |     |
| --- | --- | --- | --- | --- | ------- | --- | ---- | --- | --- | ------ | --- | --- |
|     |     |     |     | aV  |         | ρV  |      |     | j|E | ∞      | j 2 |     |
|     |     |     |     | :=  | max     | =   | sup  |     |     |        | .   |     |
|     |     |     |     | j   |         | ij  |      |     | ∥r  | V ∥2   |     |     |
|     |     |     |     |     | i∈[n+1] |     | E∈EV | ,rV |     |        |     |     |
|     |     |     |     |     |         |     | −j   | ̸=0 |     | j |E 2 |     |     |
j|E
| Proof. By | Lemma |     | 2,  |     |       |     |         |     |      |     |     |     |
| --------- | ----- | --- | --- | --- | ----- | --- | ------- | --- | ---- | --- | --- | --- |
|           |       |     |     |     | π◦(z) | =   | p (z)+p |     | (z), |     |     |     |
|           |       |     |     |     | j     |     | j,+     |     | j,−  |     |     |     |
where
|         | p        | (z)     | = P   | {TV(z   | +ω)    | > λ}, |        | p (z) | = P     | {TV(z       | +ω) < −λ}. |     |
| ------- | -------- | ------- | ----- | ------- | ------ | ----- | ------ | ----- | ------- | ----------- | ---------- | --- |
|         | j,+      |         | ω     | j       |        |       |        | j,−   |         | ω j         |            |     |
| Then,   | applying |         | Lemma | 4       | yields |       |        |       |         |             |            |     |
|         |          |         | p (z  | −ρVhvV) |        | ≤ p   | (z +he | )     | ≤ p     | (z +ρVhvV). |            |     |
|         |          |         | j,+   |         | ij j   | j,+   |        | i     | j,+     |             | ij j       |     |
| Letting | h ↓ 0,   | we have |       |         |        |       |        |       |         |             |            |     |
|         |          |         |       |         | |∂ p   | (z)|  | ≤ ρV|D |       | p (z)|. |             |            |     |
|         |          |         |       |         | i j,+  |       | ij     | vV    | j,+     |             |            |     |
j
| Analogously, |     | applying | Lemma |     | 4 to | p (z) | yields |     |     |     |     |     |
| ------------ | --- | -------- | ----- | --- | ---- | ----- | ------ | --- | --- | --- | --- | --- |
j,−
ρV|D
|     |     |     |     |     | |∂ p  | (z)| | ≤   |     | p (z)| |     |     |     |
| --- | --- | --- | --- | --- | ----- | ---- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     |     | i j,− |      | ij  | vV  | j,−    |     |     |     |
j
Finally, applying Lemma 5 to bound the directional derivatives on the right-hand side
directional derivatives of the two above-stated inequalities, we have
|     |     |     |     |       |        | ρV   |     |      |      | ρV    |     |     |
| --- | --- | --- | --- | ----- | ------ | ---- | --- | ---- | ---- | ----- | --- | --- |
|     |     |     | |∂  | p     | (z)| ≤ | √ij  | ,   | |∂ p | (z)| | ≤ √ij | .   |     |
|     |     |     |     | i j,+ |        |      |     | i    | j,−  |       |     |     |
|     |     |     |     |       |        | τ 2π |     |      |      | τ     | 2π  |     |
Therefore,
|     |     |     |     |     |           |     | 2ρV |     | (cid:114) 2ρV |      |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------------- | ---- | --- | --- |
|     |     |     |     |     | |∂ π◦(z)| | ≤   | √ij | =   |               | ij . |     |     |
i
|        |             |     |         |     | j      |       | τ   | 2π  | π τ |     |     |     |
| ------ | ----------- | --- | ------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
| Taking | the maximum |     | over    | i   | proves | (16). |     |     |     |     |     |     |
| A.3    | Auxiliary   |     | results |     |        |       |     |     |     |     |     |     |
EV
For E ∈ , recall from Lemma 3 and Lemma 4 that P denotes the orthogonal projection
|          | −j     |       |     |     |            |     |     |     | VE  |     |     |     |
| -------- | ------ | ----- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| onto the | column | space | of  | V   | , and that |     |     |     |     |     |     |     |
E
|          |       |          | rV  |     | P⊥  |          |      | P⊥    |     |     |     |     |
| -------- | ----- | -------- | --- | --- | --- | -------- | ---- | ----- | --- | --- | --- | --- |
|          |       |          |     | =   | V   | , where, |      |       | = I | −P  | ,   |     |
|          |       |          |     | j|E | VE  | j        |      | VE    |     | n+1 | VE  |     |
| and that | for i | ∈ [n+1], |     |     |     |          |      |       |     |     |     |     |
|          |       |          |     |     |     |          | |(rV | ) |∥V | ∥   |     |     |     |
|          |       |          |     |     |     |          |      | i     | j 2 |     |     |     |
|          |       |          |     |     | ρV  |          |      | j|E   |     |     |     |     |
|          |       |          |     |     |     | = sup    |      |       |     | .   |     |     |
|          |       |          |     |     | ij  |          |      | ∥rV   | ∥2  |     |     |     |
|          |       |          |     |     |     | E∈EV     |      |       | 2   |     |     |     |
|          |       |          |     |     |     |          | −j   | j|E   |     |     |     |     |
|          |       |          |     |     |     | rV       | ̸=0  |       |     |     |     |     |
j|E
37

Proposition 1 (Sensitivity bound under randomized local distillation). Suppose that y (cid:55)−→
ϕ ˆ (x∗,y) belongs to C1(Rn), and that Assumption 1 holds. Then, for every y ∈ Rn, i ∈ [n],
and j ∈ [p],
(cid:114)
|∂ π (y)| ≤ 2 1 (cid:110)(cid:112) S ρV + (cid:112) S |∂ ϕ ˆ (x∗,y)|ρV (cid:111) .
i j πτ i ij n+1 i n+1,j
Proof. By Lemma 1,
(cid:0) (cid:1)
π (y) = π◦ z(y)
j j
is continuously differentiable.
The coordinates of z(y) satisfy
z (y) = (cid:112) S y , k ∈ [n], z (y) = (cid:112) S ϕ ˆ (x∗,y),
k k k n+1 n+1
where S n+1 = √ n µ . Consequently, for i ∈ [n] and k ∈ [n+1],
eff
∂z k (y) = (cid:112) S 1{k = i}+ (cid:112) S ∂ ϕ ˆ (x∗,y)1{k = n+1}.
i n+1 i
∂y
i
The chain rule therefore gives
n+1
∂ π (y) = (cid:88) ∂ π◦ (cid:0) z(y) (cid:1) ∂z k (y)
i j z k j ∂y
i
k=1
= (cid:112) S ∂ π◦ (cid:0) z(y) (cid:1) + (cid:112) S ∂ ϕ ˆ (x∗,y)∂ π◦ (cid:0) z(y) (cid:1) . (17)
i zi j n+1 i zn+1 j
Applying Theorem 2 gives, for every z ∈ Rn+1 and k ∈ [n+1],
(cid:114)
(cid:12) (cid:12)∂ π◦(z) (cid:12) (cid:12) ≤
2ρV
kj .
z k j π τ
Substituting these bounds into (17) and applying the triangle inequality proves the bound.
Lemma 6 (Directional monotonicity). Let f : Rn → R be Lipschitz, and let d ∈ Rn. If
D f(z) ≥ 0 for Lebesgue-almost every z, then f(z+td) ≥ f(z) for every z ∈ Rn and t ≥ 0.
d
Proof. The result is immediate if d = 0. Otherwise, let d(cid:101)= d/∥d∥ and decompose Rn =
2
d(cid:101)⊥ ⊕span(d(cid:101)), and for u ∈ d(cid:101)⊥, define g (t) = f(u+td(cid:101)). By Fubini’s theorem, for almost
u
every u, the inequality
D f(u+td(cid:101)) ≥ 0
d(cid:101)
holds for almost every t ∈ R. Since f is Lipschitz, g is absolutely continuous, and
u
g′ (t) = D f(u+td(cid:101)) ≥ 0
u d(cid:101)
38

| for almost | every t. | Hence | g   | is nondecreasing. |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
u
d(cid:101)⊥.
Nowfixanarbitraryu ∈ Chooseasequenceu → usuchthatg isnondecreasing.
|         |     |     |     |     |     |               |     | m               |     | um  |     |
| ------- | --- | --- | --- | --- | --- | ------------- | --- | --------------- | --- | --- | --- |
| For t < | t , |     |     |     |     |               |     |                 |     |     |     |
| 1       | 2   |     |     |     |     |               |     |                 |     |     |     |
|         |     |     |     | f(u | +t  | d(cid:101)) ≤ | f(u | +t d(cid:101)). |     |     |     |
|         |     |     |     |     | m   | 1             | m   | 2               |     |     |     |
Passing to the limit and using continuity of f yields f(u + t d(cid:101)) ≤ f(u + t d(cid:101)). Thus f is
|               |       |       |      |          |     |       |     |     | 1   |     | 2   |
| ------------- | ----- | ----- | ---- | -------- | --- | ----- | --- | --- | --- | --- | --- |
| nondecreasing | along | every | line | parallel |     | to d. |     |     |     |     |     |
(cid:110) (cid:111)
Lemma7(Effectivesimilarityneighborhood: sizeandweights). LetI = i ∈ [n] : S ≥ 1 .
|     |     |     |     |     |     |     |     |     |     | S   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2n eff
Under Assumption 2, |I | ≥ n eff . Moreover, for every i ∈ I , 1 ≤ S ≤ CS .
|     |     |     | S   | 2    |     |     |     |     | S      | i   |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------ | --- | --- |
|     |     |     |     | 2C S |     |     |     |     | 2n eff | n   | eff |
1
Proof. For every i ∈/ I , the definition of I gives S < , and therefore
|     |     | S   |     |     |     | S   | i   | 2n  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eff
|     |     |     |     |           |      | 1     |           | 1   |     |     |     |
| --- | --- | --- | --- | --------- | ---- | ----- | --------- | --- | --- | --- | --- |
|     |     |     |     | (cid:88)  |      |       | (cid:88)  |     |     |     |     |
|     |     |     |     |           | S2 ≤ |       | S         | ≤   | ,   |     |     |
|     |     |     |     |           | i    |       | i         |     |     |     |     |
|     |     |     |     |           |      | 2n    |           | 2n  |     |     |     |
|     |     |     |     |           |      | eff   |           | eff |     |     |     |
|     |     |     |     | i∈/IS     |      | i∈/IS |           |     |     |     |     |
|     |     |     |     | (cid:80)n |      |       | (cid:80)n |     | 1   |     |     |
where the last inequality uses S = 1. Since S2 = , it follows that
|     |     |     |     |     | i=1 i |     |     | i=1 i | n   |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
eff
|     |     |     |     |     | (cid:88) |      | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     |     |          | S2 ≥ |     | .   |     |     |     |
|     |     |     |     |     |          | i    | 2n  |     |     |     |     |
eff
i∈IS
On the other hand, Assumption 2 implies S ≤ S ≤ CS , for i ∈ [n]. Therefore,
|     |     |     |     |     |     |     | i   | max | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eff
C2
(cid:88)
|     |     |     |     |     |      | S2 ≤ | |I | | S . |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |      | i    | S n2 |     |     |     |     |
|     |     |     |     |     | i∈IS |      |      | eff |     |     |     |
C 2
| Combining | the | preceding |     | two | displays | yields | |I  | | S ≥ | 1 , i.e., |     |     |
| --------- | --- | --------- | --- | --- | -------- | ------ | --- | ----- | --------- | --- | --- |
S n2
2n eff
eff
n
|     |     |     |     |     |     | |I | ≥ | eff . |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- | --- |
S
2C2
S
Finally, for i ∈ I , the lower bound on S follows from the definition of I , while the
|             |         | S    |            |     |     |     | i   |     |     |     | S   |
| ----------- | ------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| upper bound | follows | from | Assumption |     |     | 2.  |     |     |     |     |     |
Lemma 8 (Bounds on residual and design in augmented regression). Under Assumptions 2–
|     |     | (cid:112) |     |     |     | κX  |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4, define C = B 1+C , and c = . Then, uniformly over j ∈ [p],
|                | V    | X   | µ     |       | R    | 2CS    |     |     |     |     |     |
| -------------- | ---- | --- | ----- | ----- | ---- | ------ | --- | --- | --- | --- | --- |
|                |      |     |       |       |      | ∥V ∥ ≤ | C , |     |     |     |     |
|                |      |     |       |       |      | j 2    | V   |     |     |     |     |
| and, uniformly | over | j   | ∈ [p] | and E | ∈ EV | ,      |     |     |     |     |     |
−j
|                |     |      |           |     |       | ∥rV ∥     | ≥ c . |      |     |     |     |
| -------------- | --- | ---- | --------- | --- | ----- | --------- | ----- | ---- | --- | --- | --- |
|                |     |      |           |     |       | j|E 2     | R     |      |     |     |     |
| In particular, | rV  | ̸= 0 | for every | j   | ∈ [p] | and every | E     | ∈ EV | .   |     |     |
|                | j|E |      |           |     |       |           |       | −j   |     |     |     |
39

Proof. First, because the training weights are nonnegative and sum to one,
n
(cid:32)
n
(cid:33)2
(cid:88) (cid:88)
S2 ≤ S = 1.
i i
i=1 i=1
√
Therefore, n ≥ 1. Using S = µ/ n and Assumption 3, we obtain
eff n+1 eff
n n
(cid:88) (cid:88) µ
∥V ∥2 = S x2 +S (x∗)2 ≤ B2 S + √ B2 ≤ B2 (1+C ) = C2.
j 2 i ij n+1 j X i n X X µ V
eff
i=1 i=1
This proves the asserted upper bound on ∥V ∥ .
j 2
Next, fix arbitrary j ∈ [p] and E ∈ EV . By the definition of an orthogonal projection,
−j
∥rV ∥2 = inf ∥V −V γ∥2. For every γ ∈ R|E|,
j|E 2 γ∈R|E| j E 2
n
∥V −V γ∥2 =
(cid:88)
S
(cid:0)
x −x⊤ γ
(cid:1)2
+S
(cid:0)
x∗ −x∗⊤γ
(cid:1)2
j E 2 i ij i,E n+1 j E
i=1
≥ (cid:88) S (cid:0) x −x⊤ γ (cid:1)2 ≥ 1 ∥X −X γ∥2,
i ij i,E 2n IS,j IS,E 2
eff
i∈IS
where the final inequality follows from the definition of I .
S
After ordering the columns of X so that j is last, we write
IS,E∪{j}
(cid:32) (cid:33)
−γ
X −X γ = X .
IS,j IS,E IS,E∪{j}
1
Assumption 4 therefore implies
(cid:13)(cid:32) (cid:33)(cid:13)
(cid:112) (cid:13) −γ (cid:13) (cid:112)
∥X −X γ∥ ≥ κ |I |(cid:13) (cid:13) ≥ κ |I |.
IS,j IS,E 2 X S (cid:13)
(cid:13) 1
(cid:13)
(cid:13)
X S
2
It follows that
κ2 |I |
∥V −V γ∥2 ≥ X S .
j E 2 2n
eff
By Lemma 7, |I | ≥ n eff , and therefore,
S 2C2
S
κ2
∥V −V γ∥2 ≥ X = c2.
j E 2 4C2 R
S
Taking the infimum over γ proves ∥rV ∥ ≥ c , which completes the proof.
j|E 2 R
Lemma 9 (Bounds for weighted contributions from local distillation). Under Assump-
tions 2–4, there exists a constant C < ∞, such that, uniformly over j ∈ [p],
ρ
max (cid:112) S ρV ≤ √ C ρ , (cid:112) S ρV ≤ C ρ .
i∈[n] i ij n eff n+1 n+1,j n1/4
eff
40

Proof. By Lemma 8, uniformly over j ∈ [p] and E ∈ EV , we have
−j
∥V ∥ ≤ C , ∥rV ∥ ≥ c .
j 2 V j|E 2 R
Since |(rV ) | ≤ ∥rV ∥ , we obtain, for every k ∈ [n+1],
j|E k j|E 2
C
ρV ≤ V =: C .
kj c ρ
R
For i ∈ [n], Assumption 2 gives S ≤ S ≤ CS , and therefore
i max n
eff
√
(cid:112) C C
S ρV ≤ √ S ρ .
i ij n
eff
Finally,
√ (cid:112)
(cid:112) S ρV = µ ρV ≤ C µ C ρ .
n+1 n+1,j n1/4 n+1,j n1/4
eff eff
√
(cid:112)
Letting C = C C ∨ C C proves both claims.
ρ S ρ µ ρ
B Performance on UCI ML and OpenML datasets
Here we report the complete results across all 17 benchmark datasets and methods, including
a second tabular foundation-model teacher, TabFM [6], and the cross-validated teacher-
selection rule (Section 2.3) omitted from the main-text figure for legibility. Table 1 lists
per-dataset sample sizes and feature counts; Figure 6 shows test R2.
41

|     |     |     | Dataset            |              |             |     | n       | p Source |     |     |     |
| --- | --- | --- | ------------------ | ------------ | ----------- | --- | ------- | -------- | --- | --- | --- |
|     |     |     | Automobile         |              |             |     | 159 51  | UCI      |     |     |     |
|     |     |     | Servo              |              |             |     | 167 10  | UCI      |     |     |     |
|     |     |     | Liver Disorders    |              |             |     | 341     | 5 UCI    |     |     |     |
|     |     |     | Auto MPG           |              |             |     | 392     | 8 UCI    |     |     |     |
|     |     |     | Real Estate        | Valuation    |             |     | 414     | 6 UCI    |     |     |     |
|     |     |     | Student            | Performance  |             |     | 649 39  | UCI      |     |     |     |
|     |     |     | Cars               |              |             |     | 804 17  | OpenML   |     |     |     |
|     |     |     | QSAR Fish          | Toxicity     |             |     | 907     | 6 OpenML |     |     |     |
|     |     |     | Concrete           | Compressive  | Strength    |     | 1005    | 8 OpenML |     |     |     |
|     |     |     | Infrared           | Thermography | Temperature |     | 1018 43 | UCI      |     |     |     |
|     |     |     | Socmob             |              |             |     | 1156 35 | OpenML   |     |     |     |
|     |     |     | Red Wine           |              |             |     | 1359 11 | OpenML   |     |     |     |
|     |     |     | Airfoil Self-Noise |              |             |     | 1503    | 5 OpenML |     |     |     |
|     |     |     | Auction            | Verification |             |     | 2043    | 7 OpenML |     |     |     |
|     |     |     | Space GA           |              |             |     | 3107    | 6 OpenML |     |     |     |
|     |     |     | White Wine         |              |             |     | 3961 11 | OpenML   |     |     |     |
|     |     |     | Abalone            |              |             |     | 4177    | 9 OpenML |     |     |     |
Table 1: Benchmark datasets after complete-case filtering and de-duplication,
sorted by sample size. p is the number of columns in the design matrix, i.e. after one-hot
| encoding | of categorical |     | variables. |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
R2 comparison across methods
Points are medians; error bars are 1 SE across 20 train/test splits.
|     |     |     | airfoil self noise |     |     |     | servo |     |     | auction verification |     |
| --- | --- | --- | ------------------ | --- | --- | --- | ----- | --- | --- | -------------------- | --- |
TabPFN
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
TabFM
LD (TabFM, L)
LD (TabFM, R)
Dist (best teacher)
Lasso
Ridge
LLF
LOESS
|     |     | concrete comp. strength |     |     |     | automobile |     |     |     | space ga |     |
| --- | --- | ----------------------- | --- | --- | --- | ---------- | --- | --- | --- | -------- | --- |
TabPFN
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
TabFM
LD (TabFM, L)
LD (TabFM, R)
Dist (best teacher)
Lasso
Ridge
LLF
LOESS
|        |     |     | socmob |     |     | real estate valuation |     |     |     | white wine |     |
| ------ | --- | --- | ------ | --- | --- | --------------------- | --- | --- | --- | ---------- | --- |
| TabPFN |     |     |        |     |     | 42                    |     |     |     |            |     |
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
TabFM
LD (TabFM, L)
LD (TabFM, R)
Dist (best teacher)
Lasso
Ridge
LLF
LOESS
|     |     | 0.00 | 0.50 | 1.00 |     | 0.00 | 0.50 | 1.00 | 0.00 | 0.50 | 1.00 |
| --- | --- | ---- | ---- | ---- | --- | ---- | ---- | ---- | ---- | ---- | ---- |
Test R2
Figure 6: Predictive performance (test R2) across 17 UCI ML and OpenML
regression datasets. Each teacher is shown with its two distilled local-linear students,
lasso (L) and ridge (R). Local distillation approaches its teacher’s accuracy across datasets.
Dist (best teacher) selects, per split, the teacher with the lowest cross-validated error. LLF
and LOESS are teacher-unaware local methods and are more variable.

R2 comparison across methods
Points are medians; error bars are 1 SE across 20 train/test splits.
infrared therm. temp. auto mpg qsar fish toxicity
TabPFN
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
TabFM
LD (TabFM, L)
LD (TabFM, R)
Dist (best teacher)
Lasso
Ridge
LLF
LOESS
abalone red wine liver disorders
TabPFN
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
TabFM
LD (TabFM, L)
LD (TabFM, R)
Dist (best teacher)
Lasso
Ridge
LLF
LOESS
0.00 0.50 1.00
cars student performance
TabPFN
LD (TabPFN, L)
LD (TabPFN, R)
XGBoost
LD (XGB, L)
LD (XGB, R)
TabFM
LD (TabFM, L)
LD (TabFM, R)
Dist (best teacher)
Lasso
Ridge
LLF
LOESS
0.00 0.50 1.00 0.00 0.50 1.00
Test R2
Figure 6: (Continued.) Remaining datasets, same methods and axes as above.
C Ablation study
Local distillation has two components: (1) the similarity weights and (2) the “prior” predic-
tion from the teacher. Here, we find that both combined usually have the best predictive
performance (Figure 7).
43

Ablation: both components are useful for prediction
Similarity weights and the teacher prior, on/off. Points are medians; error bars 1 SE across 20 splits.
airfoil self noise servo auction verification concrete comp. strength automobile
Neither
Weights only
Prior only
Both (full)
0.60 0.80 1.00 0.60 0.80 0.70 0.80 0.90 1.00 0.60 0.70 0.80 0.90 0.60 0.70 0.80 0.90
space ga socmob real estate valuation white wine infrared therm. temp.
Neither
Weights only
Prior only
Both (full)
0.60 0.70 0.80 0.90 0.60 0.65 0.70 0.75 0.30 0.35 0.40 0.55 0.60 0.65
|     |     | auto mpg |     | qsar fish toxicity |     |     | abalone |     | red wine | liver disorders |     |
| --- | --- | -------- | --- | ------------------ | --- | --- | ------- | --- | -------- | --------------- | --- |
Neither
Weights only
Prior only
Both (full)
0.80 0.85 0.90 0.55 0.60 0.52 0.54 0.56 0.58 0.36 0.38 0.40 0.15 0.20
|     |     | cars |     | student performance |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Neither
Weights only
Prior only
Both (full)
|     | 0.92 | 0.94 |     | 0.960.20 0.22 | 0.24 0.26 | 0.28 |     |     |     |     |     |
| --- | ---- | ---- | --- | ------------- | --------- | ---- | --- | --- | --- | --- | --- |
Test R2
Figure 7: Similarity weights and prediction prior are both useful for prediction.
Ablation of local distillation’s two teacher-derived components: the similarity weights and the
prediction prior. There are four comparators: Neither (a global lasso), Weights only, Prior
only, and Both (the full method); each panel shows one dataset. Points show median test
R2
over 20 splits (±1 SE); the teacher is TabPFN, the student a lasso. Both components
| help, and | using       | both | is  | best or tied-best |     | on nearly | every | dataset. |     |     |     |
| --------- | ----------- | ---- | --- | ----------------- | --- | --------- | ----- | -------- | --- | --- | --- |
| D         | Performance |      |     | with              |     | simulated |       | data     |     |     |     |
Local distillation is intended to summarize the feature–outcome relationship linearly at each
prediction point. Here we study its performance when the data generating process is known,
and test how the method responds to changes in the amount of noise, and the sizes of n and
| p. We | simulate | training |     | data as     | follows: |          |     |           |       |     |      |
| ----- | -------- | -------- | --- | ----------- | -------- | -------- | --- | --------- | ----- | --- | ---- |
|       |          |          |     | x ∼ N       | (0,Σ),   |          | Σ = | 0.3|j−k|, |       |     |      |
|       |          |          |     | i           | p        |          | jk  |           |       |     |      |
|       |          |          |     | y = f(x     | )+ε      | ,        | ε ∼ | N(0,σ2),  | where |     |      |
|       |          |          |     | i           | i        | i        | i   |           |       |     |      |
|       |          |          |     | f(x) = (1+x |          | )x +(1−x |     | )x +2x    |       |     |      |
|       |          |          |     |             |          | 3 1      | 3   | 2         | 3     |     |      |
|       |          |          |     | = x         | +x       | +(2+x    | −x  | )x .      |       |     | (18) |
|       |          |          |     |             | 1        | 2        | 1   | 2 3       |       |     |      |
The true local coefficients ∇f(x) = (1+x , 1−x , 2+x −x , 0,...,0) vary with respect
|     |     |     |     |     |     | 3   | 3   | 1   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to x ,x and x , but the global linear model cannot model this heterogeneity. Our testing
| 1   | 2   | 3   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
44

|     |     |             | corr(βˆ | corr(βˆ | corr(βˆ |       |     |
| --- | --- | ----------- | ------- | ------- | ------- | ----- | --- |
| n   | p σ | µˆ reverted |         | )       | )       | ) TPR | FP  |
|     |     |             |         | 1       | 2       | 3     |     |
400 100 0.3 2.89 (0.49) 0/50 0.79 (0.06) 0.78 (0.06) 0.34 (0.13) 0.97 (0.02) 7.4 (3.7)
400 100 1 1.46 (0.15) 0/50 0.77 (0.07) 0.77 (0.07) 0.30 (0.13) 0.96 (0.02) 9.3 (5.6)
400 100 2 1.07 (0.06) 11/50 0.73 (0.08) 0.72 (0.08) 0.24 (0.16) 0.94 (0.04) 10.3 (5.9)
400 100 3 1.02 (0.02) 40/50 0.63 (0.09) 0.64 (0.06) 0.14 (0.14) 0.92 (0.05) 9.3 (5.3)
200 100 0.3 1.86 (0.37) 0/50 0.76 (0.07) 0.75 (0.07) 0.33 (0.17) 0.96 (0.02) 7.7 (4.6)
400 800 0.3 2.43 (0.33) 0/50 0.78 (0.06) 0.77 (0.07) 0.34 (0.15) 0.95 (0.02) 10.4 (7.6)
200 500 0.3 1.66 (0.36) 0/50 0.77 (0.06) 0.75 (0.08) 0.25 (0.17) 0.94 (0.03) 9.8 (7.8)
Table 2: Recovery of local structure using a gradient boosting teacher and lasso
student. Means (standard deviations) reported over runs, with 50 replicates per row. “re-
verted” counts replicates with µˆ ≤ 1, in which the method reverted to the global fit. The
correlation columns show the correlations between the fitted and true coefficients, for runs
when µˆ > 1. “TPR” is the true positive rate of the selected coefficients, “FP” is the number
| of false positive | selections. |     |     |     |     |     |     |
| ----------------- | ----------- | --- | --- | --- | --- | --- | --- |
data in all cases is 40 query points drawn from the same distribution.
We vary n, p and σ; for each combination, we run 50 iterations of local distillation with
a gradient boosting teacher and lasso student. Table 2 reports (1) correlations across query
points between the fitted local coefficients β ˆ ,β ˆ and β ˆ and the true local gradients; (2)
|     |     |     |     | 1 2 | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
support recovery described by feature selection true positive rate and the number of false
positives (incorrectly selected features); (3) µˆ and the fraction of runs in which µˆ ≤ 1 and
| the method | reverted | to the global | fit. |     |     |     |     |
| ---------- | -------- | ------------- | ---- | --- | --- | --- | --- |
We find that local distillation is generally strong across σ, n and p (including p > n),
though it naturally degrades as the level of noise grows (and eventually reverts to the global
linear model). In particular, the first two coefficients (1+x ) and (1−x ) are typically well
|     |     |     |     |     | 3   | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
fit, with correlation to the true values between 0.63 and 0.79. However, the third coefficient,
2 + x − x , is harder to recover (correlation 0.14–0.34). This is a result of our definition
| 1   | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
of “similarity”: the difference x −x affects the response only through its interaction with
|     |     |     | 1 2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
x , so observations with very different values of x −x can have similar teacher predictions,
| 3   |     |     |     | 1   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
and each local fit returns roughly the average coefficient over its neighborhood.
We then repeated this experiment to test the effect of filtering by selection probabilities.
For each configuration, we took the first 10 replicates, selected tˆusing the rule of Section 4.1,
and ran B = 100 randomized refits per query point to compute πˆ for every selected feature.
j
Table 3 reports the results. We find that filtering reduces the false positive rate for feature
45

share with πˆ >0.9 FP per query
j
n p σ reverted tˆ active spurious unfiltered filtered TPR (filtered)
400 100 0.3 0/10 1.14 (0.98) 0.98 (0.02) 0.12 (0.14) 8.3 (5.1) 0.9 (1.0) 0.95 (0.02)
400 100 1 0/10 0.67 (0.76) 0.98 (0.03) 0.21 (0.23) 10.4 (6.5) 2.0 (2.2) 0.93 (0.05)
400 100 2 0/10 0.89 (0.92) 0.95 (0.06) 0.12 (0.12) 12.4 (6.7) 1.8 (2.2) 0.87 (0.09)
400 100 3 8/10 0.62 (0.53) 0.93 (0.03) 0.05 (0.07) 9.1 (0.6) 0.5 (0.7) 0.86 (0.01)
200 100 0.3 0/10 0.39 (0.37) 0.98 (0.02) 0.21 (0.27) 7.3 (4.9) 1.6 (2.0) 0.94 (0.03)
400 800 0.3 0/10 0.66 (0.76) 0.98 (0.02) 0.15 (0.22) 10.1 (9.1) 1.7 (2.3) 0.93 (0.02)
200 500 0.3 0/10 0.42 (0.75) 0.98 (0.02) 0.27 (0.28) 9.0 (5.5) 2.4 (2.9) 0.94 (0.01)
Table 3: Validation of the selection probabilities against ground truth. Means
(standard deviations) across replicates with µˆ > 1; maximum 10 per row, with B = 100 ran-
domized refits per query point at the scale tˆselected per replicate as described in Section 4.1.
“Reverted” counts replicates with µˆ ≤ 1, which are excluded from the other columns. “Ac-
tive” and “spurious” refer to selections of the 3 truly active and the p − 3 null features,
respectively; “filtered” retains only selections with πˆ > 0.9. The selection probabilities iden-
j
tify the false selections: filtering at πˆ > 0.9 reduces them from roughly 8–12 per query point
j
to fewer than 2.5, and retains 86–95% of the truly active features.
selection, and retains most of the true positives.
46
---- END DOCUMENT ----
