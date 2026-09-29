Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
|     |     |     |     | Reliability-Aware |         |        |         | Scheduling      |     |     |     | for |     |     |     |
| --- | --- | --- | --- | ----------------- | ------- | ------ | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |                   | Digital |        | Twin    | Maintenance     |     |     |     |     |     |     |     |
|     |     |     |     |                   |         | Milica | Jankov, | Carlo Fischione |     |     |     |     |     |     |     |
School of Electrical Engineering and Computer Science, KTH Royal Institute of Technology, Stockholm, Sweden
|     |     |     |     |     |     |     | {milicaj, | carlofi}@kth.se |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Email:
Abstract—In Industrial Internet of Things systems, learning- ditions or process regimes that make models trained on
enabled Digital Twins (DTs) support remote monitoring by historical data less aligned with the current physical pro-
|                                          | using data      | reported | by          | distributed | devices     | to maintain  | digital   |           |               |         |              |           |               |          |         |
| ---------------------------------------- | --------------- | -------- | ----------- | ----------- | ----------- | ------------ | --------- | --------- | ------------- | ------- | ------------ | --------- | ------------- | -------- | ------- |
|                                          |                 |          |             |             |             |              |           | cess [6]. | Under         | concept | drift,       | temporal  | freshness     | alone    | is not  |
| 6202 guA 22  ]IN.sc[  1v66812.8062:viXra | representations |          | of physical | processes.  | When        | uplink       | resources |           |               |         |              |           |               |          |         |
|                                          |                 |          |             |             |             |              |           | enough    | to guarantee  | DT      | reliability. |           | Even a        | recently | updated |
|                                          | are limited,    | a base   | station     | cannot      | collect new | observations | from      |           |               |         |              |           |               |          |         |
|                                          |                 |          |             |             |             |              |           | DT may    | be inaccurate |         | if its       | predictor | is mismatched |          | to the  |
everydeviceateverycommunicationslotandmustdecidewhich
devicesshouldtransmit.Thisdecisionbecomeschallengingwhen current operating regime. This issue is especially relevant in
the physical process changes after the DT models have already industrial process manufacturing, where limited communica-
|     | been trained. | In  | such cases, | recent | observations | alone | may not |                    |     |      |         |          |       |          |       |
| --- | ------------- | --- | ----------- | ------ | ------------ | ----- | ------- | ------------------ | --- | ---- | ------- | -------- | ----- | -------- | ----- |
|     |               |     |             |        |              |       |         | tion opportunities |     | must | support | accurate | state | tracking | under |
keeptheDTaccurate,becausethelearnedmodelmaynolonger
|     |     |     |     |     |     |     |     | changing | process | conditions |     | [1]. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---------- | --- | ---- | --- | --- | --- |
matchtheunderlyingprocess.Thispaperstudieshowtoschedule
|     |             |          |     |      |                   |     |             | Existing | freshness | metrics |     | and related | scheduling |     | methods |
| --- | ----------- | -------- | --- | ---- | ----------------- | --- | ----------- | -------- | --------- | ------- | --- | ----------- | ---------- | --- | ------- |
|     | observation | requests | so  | that | the DT maintained |     | at the base |          |           |         |     |             |            |     |         |
station remains close to the true physical process. We define provide useful baselines for reliability, but they do not fully
the Ensemble Disagreement Indicator (EDI) as an uncertainty capture the failure mode induced by concept drift. Age of
|     | measure   | computed | at the     | base          | station from               | the | spread among |              |            |       |                |              |         |            |         |
| --- | --------- | -------- | ---------- | ------------- | -------------------------- | --- | ------------ | ------------ | ---------- | ----- | -------------- | ------------ | ------- | ---------- | ------- |
|     |           |          |            |               |                            |     |              | Information, | Age        | of    | Incorrect      | Information, |         | Query      | Age of  |
|     | estimates | produced | by         | independently | trained                    | DT  | predictors.  |              |            |       |                |              |         |            |         |
|     |           |          |            |               |                            |     |              | Information, | and        | Value | of Information |              | methods | rank       | updates |
|     | Building  | on EDI,  | we propose |               | R-VoU, a reliability-aware |     | value-       |              |            |       |                |              |         |            |         |
|     |           |          |            |               |                            |     |              | according    | to elapsed |       | time,          | mismatch,    | query   | relevance, | or      |
of-updateschedulerthatprioritizestheobservationsexpectedto
most improve the DT by reducing a cost based on uncertainty expected utility [3], [7]–[9]. However, under concept drift,
and predicted DT error. The DT is further adjusted online reducing receiver-side uncertainty and reducing receiver-side
|     | using the    | difference  | between       | received   | observations  |       | and current |            |             |             |            |           |                |     |             |
| --- | ------------ | ----------- | ------------- | ---------- | ------------- | ----- | ----------- | ---------- | ----------- | ----------- | ---------- | --------- | -------------- | --- | ----------- |
|     |              |             |               |            |               |       |             | DT error   | are related |             | but not    | identical | reliability    |     | objectives. |
|     | predictions. | Experiments |               | on process | manufacturing |       | data show   |            |             |             |            |           |                |     |             |
|     |              |             |               |            |               |       |             | To clarify | the         | reliability | objective, |           | we distinguish |     | between     |
|     | that, under  | limited     | communication |            | budgets,      | R-VoU | achieves    |            |             |             |            |           |                |     |             |
receiver-sideepistemicuncertaintyandreceiver-sideDTerror.
|     | the lowest | combined | cost | and | DT estimation | error | among the |     |     |     |     |     |     |     |     |
| --- | ---------- | -------- | ---- | --- | ------------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
compared schedulers that use only information available before Epistemic uncertainty refers to uncertainty about the
each scheduling decision. learned DT model itself [10]. It arises when the current
|     | Index   | Terms—Digital |             | twins, | value of update, | pull     | scheduling, |            |         |      |           |     |             |           |          |
| --- | ------- | ------------- | ----------- | ------ | ---------------- | -------- | ----------- | ---------- | ------- | ---- | --------- | --- | ----------- | --------- | -------- |
|     |         |               |             |        |                  |          |             | prediction | is not  | well | supported | by  | the         | available | training |
|     | concept | drift, online | adaptation, |        | Industrial       | Internet | of Things   |            |         |      |           |     |             |           |          |
|     |         |               |             |        |                  |          |             | data, for  | example | when | concept   |     | drift moves | the       | process  |
I. INTRODUCTION to an operating regime that was weakly represented during
Industrial Internet of Things (IIoT) systems increasingly training. To capture this uncertainty, we define the Ensemble
relyonlearning-enabledDigitalTwins(DTs)forremotemon- Disagreement Indicator (EDI) from the disagreement among
itoring,anomalydetection,andcontrol.Thesettingconsidered independentlytrainedensemblepredictors,followingthedeep
here involves learning-enabled receiver-side DTs maintained ensemble approach [11].We will show that EDI is observable
at a base station (BS). Each DT uses intermittently received attheBSbecauseitiscomputedsolelyfromreceiver-sideDT
measurements to estimate and track the state of an evolving states and does not require the latent physical state.
physical process [1], [2]. In resource-constrained uplink net- Receiver-side DT error is defined separately as the mis-
works, the BS cannot receive fresh measurements from all match between the DT estimate and the true physical state,
devices continuously. We therefore consider a pull-based andthusdirectlyquantifiestrackingaccuracy.Becausethetrue
update scheme, in which the BS requests observations from physical state monitored by the devices is not available to the
selected devices under a per-slot communication budget [3], scheduleratruntime,thiserrorislatentandmustbepredicted
[4].Theresultingschedulingquestioniswhichdevicesshould from BS-observable information. Thus, EDI provides a BS-
bepulledsothattheBS-maintainedDTsremainreliable,i.e., observable uncertainty signal, whereas DT error is the latent
|     | accurate | and synchronized |     | with | the physical | process | [5]. | reliability | target. |     |     |     |     |     |     |
| --- | -------- | ---------------- | --- | ---- | ------------ | ------- | ---- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
This question becomes more difficult under concept drift, ThemaincontributionofthispaperisthedesignofR-VoU,
which refers to deployment-time changes in operating con- a novel reliability-aware uplink pull scheduler for receiver-
|     |              |     |          |         |                   |     |                 | side DT    | maintenance  |     | under | concept   | drift. | Under         | a one-step |
| --- | ------------ | --- | -------- | ------- | ----------------- | --- | --------------- | ---------- | ------------ | --- | ----- | --------- | ------ | ------------- | ---------- |
|     | This project | has | received | funding | from the European |     | Union’s Horizon |            |              |     |       |           |        |               |            |
|     |              |     |          |         |                   |     |                 | predictive | formulation, |     | R-VoU | allocates | pull   | opportunities | to         |
EuropeprogrammeundergrantagreementNo.101137954.Theauthorswould
liketothanktheBATTwinconsortiumforsupportingthisresearch. thedevicesexpectedtoprovidethelargestpositivereductions

X (t) only through noisy observations obtained from suc-
n
cessful pulls.
We model each device as evolving under a latent operating
regimeE (t).ChangesinE (t)correspondtotheconceptdrift
n n
settingintroducedinSectionI.Thestateevolvesaccordingto
(cid:0) (cid:1)
X (t+1)=f X (t);E (t) +W (t), (1)
n n n n n
where f (·;E (t)) : Rd → Rd is the state transition map of
n n
device n under regime E (t). The map is not restricted to be
n
linear, and W (t)∈Rd is zero-mean process noise.
n
When device n is successfully pulled at slot t, the BS
receives the observation
Y (t)=X (t)+V (t), (2)
n n n
where V (t) is zero-mean measurement noise. We denote the
n
successful pull event by u (t) = 1. If u (t) = 0, then no
n n
fresh observation from device n is received at slot t.
Fig. 1. Pull-maintenance architecture. At each slot, the BS pulls up to K
devices.Thereceivedobservationsrefreshtheselectedreceiver-sideDTsand For each device n, the BS stores M pretrained base
providepredictionresidualsforonlinecorrection. predictors {G : Rd → Rd}M , where m indexes the
in DT reliability cost. The second contribution formulates ensemblemem θ b n (m er ) .Theparameters m θ = ( 1 m)aretrainedofflineand
n
the reliability model by defining EDI as a BS-observable
kept fixed during deployment. Since the ensemble members
uncertainty signal from DT ensemble disagreement, distin-
are trained independently, their disagreement can be used as
guishing it from latent DT error, and using pull residuals
a BS-side measure of epistemic uncertainty, i.e., uncertainty
for online correction. The third contribution investigates the
about the learned DT model [10].
design and analysis of the learned scheduling rule. We train
To adapt the frozen base predictors under concept drift,
action-conditioned predictors for next-slot EDI and DT error
we introduce an online correction module based on recursive
risk, derive a closed-form rule for selecting up to K devices,
least squares (RLS) [13], which sequentially estimates the
establish a selection-loss bound, and validate the method on
linear correction parameters from received residual samples.
process manufacturing data. Letq (t)∈Rp denoteaBS-observableadaptationcontextfor
n
II. SYSTEMMODELANDPULL-SCHEDULINGPROBLEM device n. For ensemble member m, the correction is
C (q (t))=W(m)⊤ q (t), ϕ(m) =(W(m),P(m)),
We consider a centralized time-slotted pull-maintenance ϕ(m) n t n t t t
systemwithonebasestation(BS)andN devices.Thissystem t (3)
model follows pull-based freshness and status-update models, where W t (m) ∈Rp×d is the RLS coefficient matrix and P t (m)
where a receiver or controller requests updates from selected is the RLS covariance matrix. The coefficient matrix W t (m)
devices under limited communication opportunities [3], [4], is shared across devices for the same ensemble member m.
[12]. The BS maintains one receiver-side DT per device and The correction remains device-dependent through the context
can successfully receive fresh observations from at most K q n (t).
devices per slot. In each slot, the BS schedules the devices
LetX˜
n
(m)(t+1)denotethebasepredictionbeforeapplying
to pull; devices that are not scheduled do not transmit. We
theonlinecorrection,andletXˆ
n
(m)(t+1)denotethecorrected
abstract communication through successful receptions and receiver-side DT estimate. The base prediction is updated as
focus on allocating the limited pull opportunities so that the (cid:40) G (cid:0) Y (t) (cid:1) , u (t)=1,
receiver-side DTs remain reliable under concept drift. X˜ n (m)(t+1)= G θn (m) (cid:0) Xˆ n (m)(t) (cid:1) , u n (t)=0. (4)
Fig. 1 summarizes the architecture. Pulled observations θn (m) n n
refresh the selected DTs and reveal prediction residuals, Thus,thebasepredictionusesthenewlyreceivedobservation
defined as the differences between received observations and
whenu
n
(t)=1andthepreviouscorrectedDTestimatewhen
currentDTpredictions.Theseresidualsupdateasharedonline u n (t)=0. The corrected estimate is then given by
correctionmodulethathelpsthereceiver-sideDTsadaptunder Xˆ(m)(t+1)=X˜(m)(t+1)+C (cid:0) q (t) (cid:1) . (5)
n n ϕ(m) n
concept drift. t
A pulled observation also provides information for online
A. Receiver-Side DT with Online Correction adaptation. Let X˜ n (m)(t) denote stored pre-correction base
estimate for the current slot, obtained by the recursion in (4)
We consider a time-slotted system indexed by t ∈ Z .
≥0 at the previous update. When device n is pulled, we define
The device set is N = {1,...,N}. For each device n ∈ N,
the base-residual target
let X (t) ∈ Rd denote the latent physical state at slot t,
where n d is the dimension of the per-device state. This state is b( n m)(t)≜Y n (t)−X˜ n (m)(t). (6)
not directly available at the BS. The BS therefore maintains This residual is the additive correction that would make the
a receiver-side DT estimate and receives information about current base prediction match the received observation.

Foreachensemblememberm,theadaptationbatchatslott We also define the set of pulled devices as
containsonepair(q (t),b(m)(t))foreverysuccessfullypulled S ≜{n∈N :u (t)=1}.
n n t n
device:
B(m) ≜(cid:8) (q (t),b(m)(t)):u (t)=1 (cid:9) . (7) After the BS selects S t , it receives {Y n (t) : n ∈ S t }.
t n n n Theseobservationsrefreshtheselectedreceiver-sideDTstates
The RLS state is updated according to
through(4)and(5). Theyalsoprovideresidualtargetsforthe
ϕ(m) =A(m)(cid:0) ϕ(m),B(m)(cid:1) , (8) RLS adaptation batches in (7). Devices that are not pulled
t+1 RLS t t
where A(m) denotes the standard RLS update operator ap- evolve through the skip branch of (4) and provide no new
RLS residual information in that slot.
plied to the pulled batch [13]. If no device is pulled at slot
t, then B(m) = ∅ and ϕ(m) = ϕ(m). Because the RLS The scheduling decision is causal. Thus, u(t) must be
t t+1 t chosen using only information available at the BS before
coefficient matrix W t (m) is shared across devices for each any observations are received during slot t. Let I(t) ≜
ensemble member m, a base-residual target obtained from
(I (t),...,I (t)) collect the current EDI values across de-
1 N
one pulled device can update this shared coefficient matrix vices. Let M ≜ {ϕ(m)}M denote the current RLS cor-
and thereby affect future corrections for other devices with t t m=1
rection state, and let Dres denote the residual information
related contexts. t
obtained from previous pulls. The dynamic scheduler infor-
The ensemble-mean receiver-side DT estimate is
mation is
X¯ n (t)≜ M 1 (cid:88) M Xˆ n (m)(t). (9) H t ≜ (cid:16) {I(τ)} τ≤t ,{u(τ)} τ<t ,D t res,M t (cid:17) . (13)
m=1 Thereceiver-sideDTerrorvectore(t)≜(e (t),...,e (t))is
We define the Ensemble Disagreement Indicator (EDI) as the 1 N
not included in H , because it depends on the latent physical
average per-component sample variance of the corrected DT t
states and is not available to the runtime scheduler.
ensemble,
I (t)≜ 1 (cid:88) M (cid:13) (cid:13)Xˆ(m)(t)−X¯ (t) (cid:13) (cid:13) 2 . (10) Fo T r h ea e c s h ch d e e d v u ic l e er n i , s l a e l t s ξ o p ∈ ro R vi r de d d en w o i t t e h m fi e x t e a d da d t e a v t i h c a e t m is e k ta n d o a w ta n .
n d(M −1) m=1 (cid:13) n n (cid:13) 2 beforeschedulingandd n oesnotchangeovertime,andletω n >
Because I (t) depends only on receiver-side DT states, it is 0denotethereliabilitypriorityweightofthedevice.Acausal
n
observableattheBSandprovidesacausaluncertaintysignal. pull-scheduling policy is a sequence π ={π } such that
t t≥0
Larger values indicate stronger ensemble disagreement and π : (cid:0) H ,{ξ }N ,{ω }N (cid:1) (cid:55)→u(t)∈U .
t t n n=1 n n=1 K
hence greater epistemic uncertainty. Under model mismatch,
Thus, the policy uses the history of EDI values, past pull
EDI may increase during passive propagation and decrease
decisions, residual history, the current RLS correction state,
after informative receptions.
and fixed device metadata. It cannot use the latent DT error
Tracking accuracy is described by a separate metric. We
vector e(t).
define the receiver-side DT error as the mismatch between
SinceEDIandDTerrorhavedifferentscales,wenormalize
the ensemble-mean estimate and the latent physical state,
e n (t)≜ d 1(cid:13) (cid:13)X¯ n (t)−X n (t) (cid:13) (cid:13) 2 . (11) t d h u e r m ing us e i v n a g lu t a r t a i i o n n i . ng F - o s r et a c d o e n s s ig ta n nt p s ar s a I m > ete 0 r α an ∈ d [ s 0 e ,1 > ], 0 th , e fi p x e e r d -
ThiserrordependsonX (t),whichisnotavailabletotheBS device reliability cost is
n
(cid:20) (cid:21)
duringruntime.Hence,e n (t)isnotdirectlyobservablebythe J (t)≜ω α I n (t) +(1−α) e n (t) . (14)
scheduler. In offline experiments with recorded trajectories, n n s s
I e
the reference physical state is used to compute e (t) for The parameter α balances EDI and DT error: α = 1 yields
n
training labels and evaluation. Thus, EDI provides a BS- an EDI-only objective, while α=0 gives an objective based
observable uncertainty signal, whereas DT error is the latent only on DT error.
reliability target that must be inferred from the information We propose the following reliability-aware pull-scheduling
available at the BS. problem: T (cid:34) N (cid:35)
1 (cid:88) (cid:88)
B. Reliability-Aware Pull-Scheduling Objective m π inli T m → s ∞ up T E π J n (t) , (15)
At the beginning of each slot t, the BS decides which t=1 n=1
where the expectation is taken over the process noise, mea-
devices to pull before receiving any new observations. Let
u(t) ≜ (u (t),...,u (t)) ∈ {0,1}N denote the slot-t pull- surement noise, latent regime evolution, and any randomiza-
1 N
tion in the policy.
decision vector. Under the successful-reception abstraction,
u (t) = 1 means that device n is pulled and its observation Problem (15) provides an ideal objective, but it does not
n
is received by the BS during slot t. If u (t) = 0, no fresh directly yield a causal scheduling policy for the BS. Its direct
n
observation from device n is received in that slot. solution would require modeling the controlled evolution of
The BS can receive observations from at most K devices I n (t), e n (t), and M t under pull decisions, skipped updates,
per slot, where K ∈ {0,...,N}. Hence, the feasible action online RLS adaptation, and concept drift. Moreover, e n (t) is
not observable by the BS during deployment. We therefore
set is (cid:40) N (cid:41)
(cid:88) cannotsolvetheidealproblemdirectly.Instead,SectionIIIin-
U ≜ u∈{0,1}N : u ≤K . (12)
K n vestigates a learned one-step prediction model that estimates,
n=1

from BS-observable information, the next-slot EDI and DT 1 denotes pull, the corresponding prediction head is learned
error risk under skip and pull actions. These estimates are by weighted multi-output ridge regression [14]. The output-
then used to compute the predicted reliability-cost reduction weighting matrix is Γ = diag(1,µ ), where µ controls the
e e
of each pull decision. relative weight of the DT error target:
III. RELIABILITY-AWAREPREDICTIVEPULLSCHEDULING B(cid:98)a ∈argmin (cid:88) (cid:13) (cid:13)
(cid:13)
Γ1/2(cid:0) B
a
⊤z˜
n
(t)−y
n
(a
,t
)(cid:1) (cid:13) (cid:13)
(cid:13)
2
In this section, we introduce R-VoU, a reliability-aware Ba (n,t)∈Ttr 2 (19)
value-of-update scheduler based on learned one-step predic- +λ ∥B ∥2.
reg a F
tions. Offline, R-VoU learns action-conditioned predictors for
Here, λ controls the ℓ regularization. All features are
reg 2
next-slot EDI and DT error risk from BS-observable features,
standardized using training-set statistics. Since EDI and DT
whereas online, the BS evaluates each device under the skip
error are nonnegative quantities, negative predictions are set
andpullactionsusingthecurrentcontext.Thepredictionsare
tozerobeforecomputingreliabilitycosts.Thepriorityweight
combined into a reliability cost, and the BS selects up to K
ω isnotusedbythepredictionheadsandentersonlythrough
n
devices with the largest positive predicted cost reductions.
the reliability cost.
A. Prediction Under Skip and Pull Actions
C. Reliability-Aware Value of Update
For each device n, let
The action-conditioned predictions are converted into a
z (t)=ψ (H ,ξ ) (16)
n n t n predicted reliability cost using the same normalization as in
denote the scheduling feature vector available before the (14). For device n and action a∈{0,1},
slot-t pull decision. It is constructed from BS-observable (cid:34) (cid:35)
information H t and the fixed device metadata ξ n . The latent J(cid:98) n a(t+1)≜ω n α
I(cid:98)
n
a(t
s
+1)
+(1−α)
e
(cid:98)
a
n
(t
s
+1)
. (20)
DT error e (t) is not included. I e
n
To train the action-conditioned predictors, we use a local Here, a = 0 denotes skip and a = 1 pull, while α ∈ [0,1]
hypotheticalactionindexa∈{0,1},distinctfromtherealized balances predicted uncertainty and DT error risk.
scheduling variable u n (t). The index a defines the skip (a= The reliability-aware value of update is defined as the
0) and pull (a = 1) branches used to construct prediction predicted cost reduction obtained by pulling the device rather
targets, while u n (t) denotes the actual pull decision made by than skipping it:
the BS at slot t. For each training pair (n,t), we define the
V(cid:98) rel(t)≜J(cid:98) 0(t+1)−J(cid:98) 1(t+1). (21)
next-slot prediction target as n n n
(cid:34) y(a) (cid:35) (cid:20) Ia(t+1) (cid:21) Thus, a positive value indicates that pulling device n is pre-
y(a) ≜ I,n,t = n , a∈{0,1}. (17) dictedtoreducethenext-slotreliabilitycost.Theuncertainty-
n,t y e (a ,n ) ,t ea n (t+1) only predictive ablation is obtained by setting α = 1; we
The superscript a denotes the next-slot outcome obtained denote this ablation by EDI-VoU.
under the corresponding hypothetical branch. During training D. Top-K-Positive Rule and Selection-Loss Bound
only, the recorded trajectories are used to construct targets
Giventhepredictedcosts,R-VoUsolvesthefollowingone-
for both actions, skip and pull, using the same DT recursion
step predictive scheduling problem:
and, when needed, the same RLS update as at runtime. In
N
t
b
h
a
e
se
p
-
u
re
ll
si
b
d
r
u
a
a
n
l
c
t
h
a
,
rg
th
e
e
t Y
re
n
c
(
e
t
i
)
v
−
ed
X˜
o
n
b
(m
se
)
r
(
v
t
a
)
t
.
io
In
n
t
i
h
s
e
u
s
s
k
ed
ip
to
br
f
a
o
n
r
c
m
h,
t
n
h
o
e
u(
m
t)∈
in
UKn
(cid:88)
=1
(cid:104) (1−u
n
(t))J(cid:98)
n
0(t+1)+u
n
(t)J(cid:98)
n
1(t+1) (cid:105) .
new residual target is formed for device n. (22)
At runtime, the scheduler does not observe the targets in For the ranking step, we define the reliability score of device
(17). It only uses predictors trained from them. n at slot t as
B. Shared Linear Prediction Heads
s
n
(t)≜V(cid:98)
n
rel(t).
Thus, s (t) is the predicted reduction in reliability cost
R-VoU uses shared prediction heads across devices. Let n
obtained by pulling device n rather than skipping it. For any
z˜ (t)=[1,z (t)⊤]⊤
n n vector x = (x ,...,x ), we define TopK (x) as the set of
1 N +
be the feature vector augmented with an intercept term. For indices corresponding to the largest strictly positive entries of
each action a ∈ {0,1}, the predicted EDI and DT error risk x, up to the budget K. Equivalently,
at slot t+1
y (cid:98)
a
n a
r
(
e
t+1)≜
(cid:20)
e
I(cid:98)
n a
a(
(
t
t
+
+
1
1
)
)
(cid:21)
=B a ⊤z˜ n (t). (18)
TopK + (x)∈arg
S⊆N
m
,
a
|S
x
|≤K n
(cid:88)
∈S
x n ,
(cid:98)n with the convention that entries with x ≤0 are not selected.
n
Here, B is the coefficient matrix of the prediction head for
a Therefore, TopK returns K devices only when at least K
+
actiona.Itstwocolumnsaredenotedbyβ andβ ,which
I,a e,a entries of x are positive.
mapthefeaturevectorz˜ (t)totheEDIpredictionandtheDT
n Lemma 1 (Top-K positive selection rule). Let
error risk prediction, respectively.
LetT denotethesetofdevice-slotpairsusedfortraining.
S(cid:98)t =TopK
+
(s(t)), s(t)=(s
1
(t),...,s
N
(t)).
tr
Foreachactiona∈{0,1},wherea=0denotesskipanda= Define the binary decision vector u⋆(t) by

u⋆
n
(t)=1{n∈S(cid:98)t }, n=1,...,N.
Algorithm 1 Runtime R-VoU at Slot t
Thenu⋆(t)isanoptimalsolutionof (22).Thepullsetinduced Require: H
t
,M
t
,K,α,s
I
,s
e
,{ω
n
,ξ
n
}N
n=1
, learned heads B(cid:98)
by this decision is S(cid:98)t . Hence, the scheduler pulls up to K 1: for n=1,...,N do
devices and pulls exactly K devices only when at least K 2: z n (t)←ψ n (H t ,ξ n )
devices have positive reliability scores. 3: Compute J(cid:98)n 0(t+1) and J(cid:98)n 1(t+1) using (18)–(20)
Proof sketch. Substituting (21) into (22) removes terms in- 4: s n (t)←J(cid:98)n 0(t+1)−J(cid:98)n 1(t+1)
5: end for
d (cid:80) ep N n e = n 1 d u en n t (t) o s f n ( u t ( ) t) s , ub s j o ect th t e o (cid:80) pro n b u le n m (t) b ≤ eco K m . e T s h m us a , x t i h m e iz r i u n l g e 6 7 : : S Pu t l ← l {Y T n o ( p t K ): + n (s ∈ (t) S ) t } and set u n (t)=1{n∈S t }
setsu n (t)=1forthedeviceswiththelargestpositivescores, 8: For all m, form B t (m) ←{(q n (t),Y n (t)−X˜ n (m)(t)):n∈S t }
up to the budget K, and sets the remaining entries to zero. □ 9: Update all DT states using (4)–(5) with u(t) and M t
the B c e o c m au p s o e s s it n e (t r ) el i i s ab c i o li m ty pu c t o e s d t, f i r t om gen th e e ra p li r z e e d s ic u te n d ce r r e ta d i u n c t t y i - o o n n i l n y 1 1 0 1 : : F M or t+ al 1 l ← m, { u ϕ p ( t d + m a 1 ) t } e M m ϕ = ( t+ m 1 1 ) ←A( R m L ) S (ϕ( t m),B t (m))
scheduling.TwodeviceswithsimilarpredictedEDIreduction
the observations received through successful pulls. Algo-
can be ranked differently if their predicted DT error risk
rithm 1 summarizes the causal R-VoU policy.
reductions differ.
For fixed feature dimension, score computation is O(N),
Wenextgiveacurrent-slotguaranteethatconnectsselection
and selecting S by sorting costs O(NlogN). The correction
quality to reliability-score prediction accuracy. Let V⋆(t) t
n state M is used during slot t, while the updated state M
be a reference reliability value for device n, and define t t+1
is used from the next slot onward.
V⋆(t) ≜ (V⋆(t),...,V⋆(t)). Using TopK , we define two
1 N + IV. NUMERICALEVALUATION
selectedsets:S⋆ isthesetselectedbythereferencereliability
t We evaluate R-VoU using recorded measurements from a
values, and S(cid:98)t is the set selected by R-VoU using the learned
battery production process, which serves as a representative
reliability scores:
S
t
⋆ =TopK
+
(V⋆(t)), S(cid:98)t =TopK
+
(s(t)). e
tr
x
ib
a
u
m
te
p
d
le
s
o
e
f
ns
I
i
I
n
o
g
T
tr
p
a
r
c
o
k
c
s
es
t
s
he
m
e
o
v
n
o
i
l
t
u
o
t
r
i
i
o
n
n
g.
o
I
f
n
a
su
p
c
h
h
ys
s
i
e
c
t
a
t
l
in
p
g
r
s
o
,
c
d
es
is
s
-
,
The selection loss incurred by using the learned scores is whilecommunicationconstraintslimithowmanyobservations
(cid:88) (cid:88)
Lsel,⋆ ≜ V⋆(t)− V⋆(t). (23) can be collected at each slot. Each sampled location is
t n n
represented by a scalar state, so d=1. The monitored spatial
n∈S t ⋆ n∈S(cid:98)t
Proposition 2 (Prediction-error selection-loss bound). Sup- profile is modeled by N = 10 uniformly sampled positions,
pose that the learned reliability scores satisfy where ξ n is the normalized distance of position n to the
|s (t)−V⋆(t)|≤ε (t), n=1,...,N. nearest profile boundary. Boundary positions receive larger
n n n
priority weights. A stable segment X is used to pre-train the
1
Then
device-level ensemble predictors, while a later segment X
(cid:88) (cid:88) 2
0≤Lsel,⋆ ≤ ε (t)+ ε (t)≤2Kε (t), (24) is used for evaluation under concept drift. Unless otherwise
t n n max
n∈S t ⋆ n∈S(cid:98)t stated,eachdeviceusesM =5basepredictorsandtheshared
online correction module.
where ε (t)=max ε (t).
max n n
Proof sketch. The nonnegativity follows because S⋆ maxi- We compare R-VoU with weighted Age of Information
t (wAoI), EDI-VoU, and round-robin (RR) under budgets K ∈
mizesthereferencescore.Addingandsubtractingthelearned
(cid:80) (cid:80) {1,2,3,4}.EDI-VoUistheuncertainty-onlyablationobtained
scoresin(23),andusing s (t)≥ s (t),which
n∈S(cid:98)t n n∈S t ⋆ n by setting α = 1, while R-VoU uses α = 0.3. To enable a
follows from S(cid:98)t = TopK
+
(s(t)), leaves only the prediction
comparison with Age of Incorrect Information (AoII), which
errors on S
t
⋆ and S(cid:98)t . Bounding these errors by ε
n
(t) gives
combines information mismatch with the time spent in an
the first inequality in (24); the last inequality follows from incorrect state [8], we include AoII† as a noncausal refer-
|S
t
⋆|,|S(cid:98)t |≤K. □
ence. In our DT setting, such mismatch is the instantaneous
Proposition 2 shows that the quality of the current-slot
error between the receiver-side DT estimate and the recorded
selection depends on how accurately the learned reliability reference state. AoII† prioritizes devices using this mismatch
scores approximate the reference values: if these score errors
together with the time elapsed since the last successful pull.
are small, then the loss relative to the reference selection is
Since the recorded reference trajectory is not available to the
alsosmallandisboundedby2Kε max (t).Ausefulchoicefor BSbeforeschedulingduringdeployment,AoII†isnotacausal
the reference value is the true one-step reliability value
runtime scheduler.
V⋆(t)=J0,⋆(t+1)−J1,⋆(t+1), (25) The predictive heads are trained on a prefix of 40% of X
n n n 2
where Ja,⋆(t+1) is the reliability cost under the reference and evaluated on a disjoint suffix. The feature vector z n (t)
n
containsonlypre-decisionBS-observablefeatures:EDI,edge-
next-slot outcome for action a.
position weights, past residual summaries, covariance uncer-
E. Runtime Policy
tainty, and local coupling terms. We report measured EDI J ,
I
At runtime, the prediction heads are fixed, while the RLS
receiver-side DT error J , and the composite reliability cost
correction state M t = {ϕ( t m)}M m=1 continues to evolve from J J . e

TABLEI
SCHEDULINGPERFORMANCEFORN =10ACROSSBUDGETS
K∈{1,2,3,4}.
K =1 K =2
Metric wAoI RR EDI-VoU R-VoU AoII† wAoI RR EDI-VoU R-VoU AoII†
JI 2.64 4.10 3.44 3.72 3.48 3.12 3.85 5.93 4.00 4.11
Je 82.93 100.88 85.62 78.38 76.25 75.89 84.25 117.78 73.62 67.67
JJ 101.43 128.15 108.68 100.70 97.69 94.86 88.37 125.36 86.52 74.35
K =3 K =4
Metric wAoI RR EDI-VoU R-VoU AoII† wAoI RR EDI-VoU R-VoU AoII†
JI 3.57 8.28 10.17 2.75 4.20 4.36 6.50 2.05 3.06 3.29
Je 69.13 84.81 99.19 66.14 64.98 66.18 76.96 65.67 64.13 63.74
JJ 110.28 152.60 180.42 108.69 108.48 109.22 133.83 103.87 101.89 102.26
† Noncausalbenchmarkusingtherecordedsource–receivermismatch.
cost. Experiments on recorded process manufacturing data
showed that EDI is positively associated with DT error, but
is not sufficient as a standalone reliability objective. Across
Fig.2. Representativepositionunderconceptdrift.Duringapassiveinterval, the evaluated budgets, R-VoU achieved the lowest composite
EDIincreaseswithDTerror;afterasuccessfulreception,EDIdropssharply. reliability cost and receiver-side DT error among the causal
schedulers. The online correction module further improved
A. EDI as a DT-Reliability Signal under Concept Drift
reliabilitythroughresidual-basedadaptation.Futureworkwill
We first evaluate whether EDI is associated with receiver-
study richer DT error risk predictors and longer-horizon
sideDTerrorusingpassiveslots,i.e.,slotswithoutasuccess-
scheduling policies.
fulpullfortheconsideredposition.Pooling2805passiveslots
REFERENCES
givesapositiveSpearmancorrelationρ=0.3265.Thepooled
[1] F.Tao,H.Zhang,A.Liu,andA.Y.C.Nee,“Digitaltwininindustry:
mean DT error increases from 0.710µm in the lowest EDI
State-of-the-art,”IEEETransactionsonIndustrialInformatics,vol.15,
quintileto3.540µminthehighest,correspondingtoa4.99× no.4,pp.2405–2415,2019.
increase. Fig. 2 further illustrates that EDI rises during a no- [2] M.KountourisandN.Pappas,“Semantics-empoweredcommunication
for networked intelligent systems,” IEEE Communications Magazine,
reception drift interval and drops after a successful update.
vol.59,no.6,pp.96–102,2021.
TheseresultsmotivatecombiningEDIwithpredictedDTerror [3] F. Chiariotti, J. Holm, A. E. Kalør, B. Soret, S. K. Jensen, T. B.
in R-VoU. Pedersen, and P. Popovski, “Query age of information: Freshness in
pull-based communication,” IEEE Transactions on Communications,
B. Reliability-Aware Pull Scheduling
vol.70,no.3,pp.1606–1622,2022.
Table I reports the scheduling results. Among the causal [4] P.Agheli,N.Pappas,P.Popovski,andM.Kountouris,“Effectivecom-
munication:Whentopullupdates?”inICC2024-IEEEInternational
schedulers, R-VoU achieves the lowest receiver-side DT error
ConferenceonCommunications,2024,pp.183–188.
J and the lowest composite reliability cost J across all [5] N. Zhang, R. Bahsoon, N. Tziritas, and G. Theodoropoulos, “Knowl-
e J
evaluated budgets. Its gains over the strongest causal baseline edge equivalence in digital twins of intelligent systems,” ACM Trans.
Model.Comput.Simul.,vol.34,no.1,Jan.2024.
reach up to 5.5% in J and 2.1% in J . The policy that
e J [6] J.Lu,A.Liu,F.Dong,F.Gu,J.Gama,andG.Zhang,“Learningunder
minimizes measured EDI J varies across budgets, which concept drift: A review,” IEEE Transactions on Knowledge and Data
I
further shows that EDI alone is not equivalent to receiver- Engineering,vol.31,no.12,pp.2346–2363,2019.
[7] Y. Sun, I. Kadota, R. Talak, and E. Modiano, Age of information: A
side DT reliability.
newmetricforinformationfreshness. SpringerNature,2022.
The noncausal AoII† benchmark achieves the lowest J by [8] A.Maatouk,S.Kriouile,M.Assaad,andA.Ephremides,“Theageof
e
using recorded DT error computed before scheduling, which incorrect information: A new performance metric for status updates,”
IEEE/ACMTransactionsonNetworking,vol.28,no.5,pp.2215–2228,
is unavailable to the BS at runtime. In contrast, R-VoU uses
2020.
only BS-observable information, remains close to AoII† at [9] A. Molin, H. Esen, and K. Johansson, “Scheduling networked state
larger budgets, and achieves the lowest J at K =4. estimators based on value of information,” Automatica, vol. 110, p.
J 108578,2019.
Theonlinecorrectionmodulefurtherimprovesreceiver-side
[10] E.Hu¨llermeierandW.Waegeman,“Aleatoricandepistemicuncertainty
DT reliability. At K = 3, enabling RLS correction reduces inmachinelearning:anintroductiontoconceptsandmethods,”Machine
J and J by 55.9% and 28.4%, respectively, relative to the Learning,vol.110,no.3,p.457–506,2021.
e J [11] B.Lakshminarayanan,A.Pritzel,andC.Blundell,“Simpleandscalable
same R-VoU policy without correction.
predictiveuncertaintyestimationusingdeepensembles,”inProceedings
ofthe31stInternationalConferenceonNeuralInformationProcessing
V. CONCLUSION
Systems,2017,p.6405–6416.
This paper studied reliability-aware pull scheduling for [12] S. Kriouile and M. Assaad, “When to pull data from sensors for
minimum age of incorrect information,” in 2023 21st International
receiver-side DT maintenance under limited uplink resources
Symposium on Modeling and Optimization in Mobile, Ad Hoc, and
and concept drift. We defined EDI as a BS-observable uncer- WirelessNetworks(WiOpt),2023,pp.603–610.
taintysignalfromensembledisagreementanddistinguishedit [13] A. Sayed and T. Kailath, “A state-space approach to adaptive rls
filtering,” IEEE Signal Processing Magazine, vol. 11, no. 3, pp. 18–
from receiver-side DT error, which is latent at runtime. This
60,1994.
distinctionmotivatedR-VoU,avalue-of-updateschedulerthat [14] A. E. Hoerl and R. W. Kennard, “Ridge regression: biased estimation
predicts next-slot EDI and DT error risk and pulls devices fornonorthogonalproblems,”Technometrics,vol.42,no.1,p.80–86,
2000.
according to the predicted reduction in composite reliability
---- END DOCUMENT ----
