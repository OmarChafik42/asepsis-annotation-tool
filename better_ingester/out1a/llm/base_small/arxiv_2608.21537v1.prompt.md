Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Counterfactual, Per-Decision Bias Auditing for
Automated Hiring: Localizing and Explaining
Disparate Impact in Applicant Tracking Systems
Jay Barach
Independent Researcher
https://github.com/jbarach2012/AIBF API
Abstract—Automated applicant tracking systems increasingly AIActclassifiesrecruitmentAIashighriskwithtransparency
decide who advances in hiring, and litigation and regulation and human oversight obligations [4]. Each of these demands
now demand that those decisions be auditable. Existing tools
thesamething:evidenceabouthowindividualhiringdecisions
sitattwoextremes.Groupfairnessmetricssuchasthedisparate
were made, not merely an aggregate statistic.
impactratiosummarizeawholepopulationbutcannotsaywhich
individual decisions were unfair or why, while local explainers The reason the resolution matters is that discrimination
suchasSHAPattributeasinglepredictionbutarenotconnected law and the emerging audit mandates operate on decisions,
tothelegalstandardbywhichhiringbiasisjudged.Wepresent not only on populations. A disparate impact finding at the
the AI Bias Firewall (AIBF), a method that audits an applicant
group level establishes that a problem exists, but remedy,
tracking system one decision at a time. AIBF neutralizes a
contestation, and oversight all act on individual decisions: a
candidate’s protected-attribute proxies, re-scores the decision,
and measures the resulting counterfactual shift, which yields a candidate contests their own rejection, a reviewer reconsiders
signed per-decision bias in score points, a flag for decisions the a particular case, and an oversight regime asks the operator to
protected attributes changed, and a plain-language explanation show its work on the decisions that were made. A tool that
naming the responsible factors. We evaluate on two real public
reports only the aggregate leaves every one of these actors
datasets, Adult and COMPAS, rather than on synthetic data.
without the object they need to act on.
The per-decision counterfactual shift is faithful, aggregating to
reproduce the known group level disparity, for example a mean Theavailabletoolsdonot providethatevidenceinausable
shift of +7.5 points for the privileged group and −8.0 for the form.Groupfairnessmetrics,suchasthedisparateimpactratio
disadvantaged group on Adult, consistent with the measured codified by the four-fifths rule [5] and the statistical parity
statistical parity difference. AIBF identifies the decisions that
and equalized odds measures from the fairness literature [7],
protected attributes flipped with an area under the ROC curve
[9], describe a population. They can establish that a system
of 0.963 on Adult, against 0.672 for a baseline that flags by
group membership, and it identifies the harmed candidates so disadvantages a protected group in aggregate, but they cannot
precisely that reviewing only five percent of decisions surfaces point to the specific decisions that were unfair, cannot say
fifty-five percent of them, against six percent under group based whichfactorsdrovethem,andthereforecannotdirectalimited
review. We also report a limitation: correcting flagged decisions
human review budget to the decisions that most need it. At
raises the disparate impact ratio substantially but not to legal
the other extreme, local explainers such as LIME [14] and
parity, because features labeled as merit carry residual proxy
correlation. AIBF is released under the Apache 2.0 license with SHAP[15]attributeasinglemodeloutputtoitsinputfeatures.
code and experiments. Theycansaythataparticularpredictionleanedonaparticular
Index Terms—Algorithmic fairness, disparate impact, coun- feature,buttheyaregeneric,theydonotdistinguishprotected
terfactualexplanation,applicanttrackingsystems,biasauditing, proxies from legitimate qualifications, and they are not tied to
hiring, explainable AI.
thelegalstandardbywhichhiringdiscriminationismeasured.
An operator who must both comply with a per-decision audit
I. INTRODUCTION
requirement and act on a finding is left without a tool that
A large majority of employers now use software to screen does both.
candidates, and a growing share of that software scores or The gap is not merely academic. A bias audit under Local
ranks applicants with machine learning, so that for many Law 144 must report selection rates and impact ratios, which
openings the first decision about an applicant is made or the group metrics provide, but an employer that receives a
shapedbyanalgorithmratherthanaperson.Thelegalsystem failingaudit,oracandidatewhowishestocontestarejection,
has taken notice. In Mobley v. Workday a court granted needstoknowwhichdecisionsandwhichfactorsproducedthe
preliminary certification of a nationwide age discrimination disparity,whichthegroupmetricswithhold.Ahumanreviewer
collective concerning algorithmic screening [1], the Equal givenafailingaggregateandapopulationoftensofthousands
Employment Opportunity Commission settled its first case of decisions has no way to spend a limited review budget
over automated rejection in EEOC v. iTutorGroup [2], New well. The missing layer is one that preserves the connection
YorkCityLocalLaw144requiresanannualindependentbias to the legal standard while operating at the resolution of the
auditofautomatedemploymentdecisiontools[3],andtheEU individual decision, and that is the layer this paper provides.
6202
guA
12
]YC.sc[
1v73512.8062:viXra

This paper presents the AI Bias Firewall (AIBF), a method field [16]. These metrics are the right target for compliance,
that fills the gap between the group metric and the local ex- and AIBF is designed to be consistent with them, but by
plainer.AIBFauditsanapplicanttrackingsystemonedecision construction they are population level and cannot localize or
at a time using a counterfactual test. For each candidate it explain asingle decision. Fora decision d∈{0,1} with1 the
neutralizes the protected-attribute proxies, setting them to a favorableoutcome,aprivilegedgroupanditscomplement,and
common privileged baseline, re-scores the decision through a true label y, we use the disparate impact ratio, the statistical
the same system, and measures the counterfactual shift in parity difference, and the equal opportunity difference,
| score. That | single | operation | yields | three | things | an  | auditor |     |     |     |     |     |     |     |
| ----------- | ------ | --------- | ------ | ----- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Pr(d=1|disadv)
| needs: a | signed | per-decision | bias | expressed |     | in score | points, |     |     |     |     |     |     |     |
| -------- | ------ | ------------ | ---- | --------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
|          |        |              |      |           |     |          |         | DI= |     |     | ,   |     |     | (1) |
Pr(d=1|priv)
| a flag for | the | decisions | that the | protected | attributes | changed, |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | -------- | --------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
and an explanation that names the responsible factors. The SPD=Pr(d=1|disadv)−Pr(d=1|priv), (2)
counterfactual construction connects the individual decision EOD=TPR −TPR , (3)
|              |           |          |     |       |      |              |     |     |     | disadv | priv |     |     |     |
| ------------ | --------- | -------- | --- | ----- | ---- | ------------ | --- | --- | --- | ------ | ---- | --- | --- | --- |
| to the group | standard, | because, |     | as we | show | empirically, | the |     |     |        |      |     |     |     |
per-decisionshiftsaggregatetoreproducethepopulationlevel where a disparate impact ratio below 0.80 fails the four-fifths
disparity. rule [5], a statistical parity difference of zero denotes parity,
We make the following contributions. and the true positive rates in the equal opportunity difference
|                  |     |      |          |        |     |        | are taken | with | respect | to y. | AIBF | does not | replace | these; it |
| ---------------- | --- | ---- | -------- | ------ | --- | ------ | --------- | ---- | ------- | ----- | ---- | -------- | ------- | --------- |
| • A per-decision |     | bias | auditing | method | for | hiring | that is   |      |         |       |      |          |         |           |
counterfactual, faithful, and explainable, and that con- explains and localizes the disparities they surface.
nectsindividualattributionstothegroupfairnessstandard
used in law (Section IV). B. Individual and counterfactual fairness
• A finding, obtained on real data, that a ratio based Dwork and colleagues argue for treating similar individuals
| bias | score | of the kind | a   | naive | design | would use | is a |     |     |     |     |     |     |     |
| ---- | ----- | ----------- | --- | ----- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
similarly[8],andKusnerandcolleaguesdefinecounterfactual
| poor | detector | of biased | decisions |     | because | it ignores | the       |       |       |            |        |     |        |            |
| ---- | -------- | --------- | --------- | --- | ------- | ---------- | --------- | ----- | ----- | ---------- | ------ | --- | ------ | ---------- |
|      |          |           |           |     |         |            | fairness, | under | which | a decision | should | not | change | in a world |
decision margin, and that the counterfactual shift is the where the individual’s protected attribute is different [12].
| correct | signal | (Sections | IV  | and VI). |     |     |      |        |                    |     |      |                |     |         |
| ------- | ------ | --------- | --- | -------- | --- | --- | ---- | ------ | ------------------ | --- | ---- | -------------- | --- | ------- |
|         |        |           |     |          |     |     | AIBF | adopts | the counterfactual |     | view | operationally: |     | it does |
• An evaluation on two real public datasets showing faith- not attempt to learn a causal model of the data, but it does
| fulness, | strong | detection     | of  | counterfactually |       | biased   | deci-         |                  |             |     |              |             |               |         |
| -------- | ------ | ------------- | --- | ---------------- | ----- | -------- | ------------- | ---------------- | ----------- | --- | ------------ | ----------- | ------------- | ------- |
|          |        |               |     |                  |       |          | perform       | the intervention |             | of  | neutralizing | the         | protected     | proxies |
| sions    | with   | an area under | the | ROC              | curve | of 0.963 | against       |                  |             |     |              |             |               |         |
|          |        |               |     |                  |       |          | and measuring |                  | the change, |     | which is     | a practical | approximation |         |
0.672 for a group membership baseline, and a large gain appropriatetoauditingadeployedscorer.ThispositionsAIBF
| in review |     | efficiency | (Section | VI). |     |     |         |     |         |          |       |            |          |        |
| --------- | --- | ---------- | -------- | ---- | --- | --- | ------- | --- | ------- | -------- | ----- | ---------- | -------- | ------ |
|           |     |            |          |      |     |     | between | two | strands | of prior | work. | Individual | fairness | in the |
• A quantified account of the method’s ceiling: attribution sense of Dwork and colleagues requires a task specific simi-
basedcorrectionimprovesthedisparateimpactratiosub-
|            |     |            |         |         |       |          | larity         | metric that | is notoriously |          | hard         | to obtain | [8],  | and causal  |
| ---------- | --- | ---------- | ------- | ------- | ----- | -------- | -------------- | ----------- | -------------- | -------- | ------------ | --------- | ----- | ----------- |
| stantially |     | but not to | parity, | because | merit | features | carry          |             |                |          |              |           |       |             |
|            |     |            |         |         |       |          | counterfactual |             | fairness       | requires | a structural |           | model | of the data |
residual proxy correlation, which we quantify (Section generatingprocess[12];AIBFasksanarrowerbutanswerable
VI).
|     |     |     |     |     |     |     | question, | whether | the | deployed | scorer’s | own | use | of protected |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- | -------- | -------- | --- | --- | ------------ |
AIBF is a detection and explanation tool, not an automated proxies changed a specific decision, which needs neither a
remedy, and Section IX states the responsible use position. similarity metric nor a causal model, only query access. That
Code, data preparation, and the scripts that produce every narrowing is what makes the method deployable as an audit
numberinthispaperarereleasedundertheApache2.0license. rather than a research artifact. Wachter and colleagues argue
|          |                              |         |     |     |     |     | that  | counterfactual    | explanations |     | support        |     | contestability | [13],  |
| -------- | ---------------------------- | ------- | --- | --- | --- | --- | ----- | ----------------- | ------------ | --- | -------------- | --- | -------------- | ------ |
|          | II. BACKGROUNDANDRELATEDWORK |         |     |     |     |     |       |                   |              |     |                |     |                |        |
|          |                              |         |     |     |     |     | which | is the affordance |              | an  | audited hiring |     | decision       | needs. |
| A. Group | fairness                     | metrics |     |     |     |     |       |                   |              |     |                |     |                |        |
C. Explainability
| The dominant |     | legal test | for | adverse | impact | in the | United |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | ------- | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Statesisthefour-fifthsrule,underwhichtheselectionrateofa LIME approximates a model locally with an interpretable
protectedgroupshouldbeatleasteightypercentofthehighest surrogate[14],andSHAPunifiesadditiveattributionmethods,
group’s rate [5]. The machine learning literature formalizes giving closed form values for a linear model [15]. AIBF uses
relatednotions,includingdemographicparity,statisticalparity additive attribution to produce its explanations, and in that
difference, equalized odds, and equality of opportunity [8], sense it builds on SHAP, but it differs in two ways that
[9], and studies their mutual incompatibility [10]. The legal matter for the audit task. It partitions features into protected
conceptofdisparateimpactanditstranslationintoalgorithmic proxies and legitimate qualifications rather than treating them
terms is examined by Barocas and Selbst [6], and Corbett- uniformly, and it defines its decision level signal by a coun-
Davies and colleagues analyze the cost of enforcing fairness terfactual intervention on the protected partition rather than
and the tension among competing criteria [11]. Feldman and by raw attribution magnitude. As our evaluation shows, this
colleagues give algorithmic tests for certifying and removing distinction is not cosmetic, because a raw magnitude signal
disparate impact [7], and Mehrabi and colleagues survey the fails to identify the decisions that were changed.

IV. METHOD
TABLEI
CAPABILITIESOFBIASAUDITINGAPPROACHES.APER-DECISIONAUDIT
|     |     |     |     |     |     |     | A. The counterfactual |     | shift |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ----- | --- | --- | --- | --- |
UNDERCURRENTREGULATIONNEEDSALLSIX.
|            |     |         |           |       |          |      | AIBF | audits | decision | x by the counterfactual |     | shift |     |
| ---------- | --- | ------- | --------- | ----- | -------- | ---- | ---- | ------ | -------- | ----------------------- | --- | ----- | --- |
| Capability |     | Group   |           | Local | Fairness | AIBF |      |        |          |                         |     |       |     |
|            |     | metrics | explainer |       | toolkit  |      |      |        | ∆(x)     | = s(x)−s(x              | ),  |       | (4) |
P→0
| Per-decisionoutput |     |     | No  | Yes | Part | Yes |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
thenumberofscorepointsthattheprotectedproxiescontribute
| Namesresponsiblefactors |     |     | No  | Yes | No  | Yes |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Protectedvsmeritsplit Part No Part Yes to this candidate’s score relative to the privileged baseline. A
Tiedtolegalstandard Yes No Yes Yes negative ∆ means the protected attributes lowered the score,
| Query-only(noretrain) |     |     | Yes | Yes | Part | Yes |                |        |                 |               |           |                  |      |
| --------------------- | --- | --- | --- | --- | ---- | --- | -------------- | ------ | --------------- | ------------- | --------- | ---------------- | ---- |
|                       |     |     |     |     |      |     | the signature  | of     | a disadvantaged | candidate.    |           | The per-decision |      |
| Ranksreviewworklist   |     |     | No  | No  | No   | Yes |                |        |                 |               |           |                  |      |
|                       |     |     |     |     |      |     | bias magnitude |        | is |∆(x)|,      | and AIBF      | flags the | decision         | when |
|                       |     |     |     |     |      |     | the sign       | of the | decision        | changes under | the       | intervention,    | that |
is when
| D. Fairness | toolkits | and hiring | specific | work |     |     |     |     |                         |     |     |     |         |
| ----------- | -------- | ---------- | -------- | ---- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | ------- |
|             |          |            |          |      |     |     |     |     | (cid:2)⊮(s(x)≥τ)̸=⊮(s(x |     |     |     | (cid:3) |
Open toolkits such as AI Fairness 360 [17] and Fairlearn flag(x) = P→0 )≥τ) , (5)
[18] provide group metrics and mitigation algorithms such as whereτ isthesystem’sdecisionthreshold.Equation(5)isthe
| reweighing | and adversarial | debiasing |     | [19] | as libraries, | leaving |     |     |     |     |     |     |     |
| ---------- | --------------- | --------- | --- | ---- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
counterfactualflip,anditisbyconstructionthesetofdecisions
the assembly of an auditing workflow to the user, and they the protected attributes actually determined.
| operate | primarily at the | group | level. | Raghavan | and | colleagues |     |     |     |     |     |     |     |
| ------- | ---------------- | ----- | ------ | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
examine the fairness claims of commercial pre-employment B. Why not a ratio
vendors and find limited, non-comparable evidence [20], and A naive design, and the one in an earlier version of this
Bogen and Rieke survey where bias enters the hiring pipeline work, defines a bias score as the fraction of a decision’s total
attributionmagnitudethatcomesfromprotectedfeatures.That
[25].Closertoadeployedaudit,Wilsonandcolleaguesreport
a case study of building and auditing a candidate screening ratio is intuitive but wrong for the flagging task, because it
algorithm [21], Sanchez-Monedero and colleagues ask what it ignores the decision margin. A candidate deep in the reject
wouldmeantosolvediscriminationinautomatedhiringunder region can have a high protected ratio yet never be at risk
existing law [22], and a systematic review by Kochling and of a different outcome, while a candidate near the threshold
Wehner catalogues the ways discrimination enters algorithmic can be flipped by a small protected contribution. On real data
recruitment and selection [23]. AIBF is positioned as the per- the ratio detects counterfactual flips with an area under the
decision,explainableauditinglayerthatthesesurveysidentify ROC curve of only 0.265, worse than chance, whereas the
as missing, built to sit beside a deployed applicant tracking counterfactual magnitude of Equation (4) achieves 0.963 on
system. the same data. The lesson is that a per-decision bias signal
|     |     |     |     |     |     |     | must be | defined | relative | to the decision | boundary, | which | the |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | -------- | --------------- | --------- | ----- | --- |
III. PROBLEMFORMULATION counterfactual construction does automatically.
| An applicant | tracking | system | assigns | a   | candidate | described | C. Explanations |     |     |     |     |     |     |
| ------------ | -------- | ------ | ------- | --- | --------- | --------- | --------------- | --- | --- | --- | --- | --- | --- |
byfeaturesxascores(x)andadecision,advanceorreject,by For the explanation, AIBF fits a linear reference model
| comparing | the score | to a threshold. |     | We partition |     | the features |         | (cid:80) |        |              |          |        |     |
| --------- | --------- | --------------- | --- | ------------ | --- | ------------ | ------- | -------- | ------ | ------------ | -------- | ------ | --- |
|           |           |                 |     |              |     |              | sˆ(x) = | b +      | w x to | the deployed | system’s | scores | and |
i i i
into a merit set M, which a fair scorer may use, such as reports, for each protected feature i ∈ P, its additive con-
| relevant | skills, experience, |     | and credentials, |     | and | a protected |           |           |              |           |       |         |      |
| -------- | ------------------- | --- | ---------------- | --- | --- | ----------- | --------- | --------- | ------------ | --------- | ----- | ------- | ---- |
|          |                     |     |                  |     |     |             | tribution | w i x i . | For a linear | reference | these | are the | SHAP |
proxysetP,whichafairscorermustnotletdrivetheoutcome,
|     |     |     |     |     |     |     | values with | respect | to  | the privileged | baseline | [15], | so the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | -------------- | -------- | ----- | ------ |
comprisingtheprotectedattributesandtheircloseproxies.Let explanation is faithful to the reference by construction. This
| x denote | the candidate |     | with the | protected | proxies | set to | a                                                    |     |     |     |     |     |     |
| -------- | ------------- | --- | -------- | --------- | ------- | ------ | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| P→0      |               |     |          |           |         |        | producesstatementssuchasalowerscoreattributedtoanage |     |     |     |     |     |     |
common privileged baseline while the merit features are held proxy, or a score correlated with a demographic proxy, which
fixed.
|              |              |     |           |           |         |           | convert the | opaque | shift      | into a contestable | rationale. |     |     |
| ------------ | ------------ | --- | --------- | --------- | ------- | --------- | ----------- | ------ | ---------- | ------------------ | ---------- | --- | --- |
| The auditing | problem      | is, | for each  | decision, | to      | determine |             |        |            |                    |            |     |     |
|              |              |     |           |           |         |           | D. Choice   | of the | privileged | baseline           |            |     |     |
| whether      | and how much | the | protected | proxies   | changed | it,       | to          |        |            |                    |            |     |     |
flag the decisions they changed, and to explain the change, The counterfactual sets the protected proxies to a common
usingonlyqueryaccesstothedeployedscorer.Wetakeasthe privileged baseline rather than to a population mean. This
operational ground truth for a biased decision the counterfac- choiceisdeliberateandconsequential.Ameanbaselinewould
tual flip, namely a decision whose outcome differs between x define bias relative to the average candidate, so a decision
andx .Thisisadecisiontheprotectedattributesprovably that used no protected information at all could still register
P→0
changed under the deployed model, and it is the individual a nonzero shift merely because the candidate’s protected
level analogue of the counterfactual fairness criterion [12]. A attributes differ from the mean, which conflates group mem-
decision that is rejected at x but would advance at x bership with biased treatment. The privileged baseline instead
P→0
is a harmed decision, the case of primary concern for a asksacleancounterfactualquestion:wouldthisdecisiondiffer
disadvantaged candidate. if the candidate were treated as a member of the advantaged

group. A decision that uses no protected proxy has a shift Algorithm 1 AIBF per-decision audit
of exactly zero under this baseline, which is the behavior Require: decisionx,deployedscorers,thresholdτ,protected
an audit should have. The privileged group is identified per set P, reference weights w
attribute as the group with the higher favorable rate, which Ensure: bias ∆, flag, explanation E
is observable from the data and consistent with how adverse 1: x′ ←x with features in P set to the privileged baseline
impact is assessed in law. 2: ∆←s(x)−s(x′) ▷ counterfactual shift
3:
flag←⊮(s(x)≥τ)̸=⊮(s(x′)≥τ)
E. Faithfulness and the connection to group metrics
4: E ←{(i,w i x i ):i∈P, |w i x i |>ϵ}
The counterfactual shift is designed so that its per-decision 5: return (∆,flag,E)
values aggregate to the group disparity. Write the reference
(cid:80) (cid:80)
score as sˆ(x) = b + w x + w x , and let
i∈M i i j∈P j j Algorithm 2 AIBF batch audit and report
x fix the protected features at the privileged baseline β .
P→0 j
Require: decisions {x }, scorer s, threshold τ, protected set
Then for the linear reference the shift is exactly the protected k
P
contribution relative to that baseline,
Ensure: group report G, ranked worklist W
(cid:88)
∆(x) = w j (x j −β j ), (6) 1: W ←[]
j∈P 2: for each decision x k do
which involves only the protected features. Taking the group 3: (∆ k ,flag k ,E k )← AUDIT(x k ,s,τ,P)
means and their difference, 4: if flag then
k
E[∆|priv]−E[∆|disadv]= (cid:88) w (cid:0) x¯priv−x¯disadv(cid:1) , (7) 5: append (x k ,∆ k ,E k ) to W
j j j 6: end if
j∈P 7: end for
which is precisely the protected proxies’ contribution to the 8: sort W by descending |∆ k |
gap in scores between the groups. Because the decision is a 9: G← selection rates and disparate impact ratio per group
thresholdonthescore,thisscoregapisthedriverofthegapin 10: G←G∪{E[∆|group]:each group}
selectionratesthatthestatisticalparitydifferencemeasures,so 11: return (G,W)
the per-decision shift and the group metric are two views of
the same quantity. This is the formal sense in which AIBF
is faithful, and Section VI confirms it numerically on two
V. EXPERIMENTALSETUP
datasets: the measured group means of ∆ match the sign and
We evaluate on two real public datasets rather than on
relative magnitude of the independently computed statistical
synthetic data, and we release the preparation and analysis
parity difference. This correspondence is what licenses AIBF
scripts.
to serve as the per-decision instrument behind a group level
compliance report.
A. Datasets
F. Properties Adult,theUCICensusIncomedataset,isthestandardfair-
Threepropertiesfollowfromtheconstruction.First,theflag ness benchmark. The favorable outcome is an income above
ofEquation(5)issoundwithrespecttothedeployedscorer:a fiftythousanddollars,whichwetreatastheadvancedecision.
flagged decision is one whose outcome demonstrably changes Theprotectedattributesaresex,race,andanageproxyforthe
when the protected proxies are neutralized, so a flag is never over forty group protected under age discrimination law. The
raisedwithoutaconcretecounterfactualwitnessingthechange. merit features are education, weekly hours, and work class.
Second,theauditismodelagnosticinitsdecisionsignal,since COMPAS, the ProPublica recidivism dataset, is a standard
∆iscomputedbytwoqueriestothetruescorersanddoesnot fairness benchmark outside hiring, included to test whether
depend on the linear reference, which is used only to itemize the method generalizes beyond the applicant tracking setting.
theexplanation.Third,thecostistwoforwardevaluationsper The favorable outcome is a low risk assessment, the protected
decision,soafullauditofndecisionscosts2nscorerqueries, attribute is race restricted to the two largest groups following
whichisnegligiblebesidetrainingorbesidethehumanreview ProPublica’s filtering, and the merit features are age, prior
the audit informs. The one quantity that is not guaranteed is counts, and charge degree.
completeness: AIBF detects influence from the proxies it is In Adult the disadvantaged groups are the 33.2 percent of
given,andunmodeledproxiesescapeit,whichisthelimitation records that are female, the 14.5 percent that are non-white,
we return to in Section VIII. and the 43.8 percent aged forty or over, and the base rates
The per-decision audit composes into the batch procedure maketherealdisparityvisiblebeforeanymodelistrained:the
of Algorithm 2, which is what an operator runs to satisfy a high income rate is 30.4 percent for men against 10.9 percent
periodic audit obligation. It produces both the group level re- for women, and 25.4 percent for white against 15.3 percent
porttheregulationasksforandtheranked,explainedworklist for non-white records. In COMPAS the African-American
that makes the finding actionable, from a single pass over the group is 60.2 percent of the filtered records and has a two
decisions. year recidivism rate of 52.3 percent against 39.1 percent for

bias magnitude
|∆|
Candidate ATS scorer flag: sign flip
s(x ) ∆=s(x)−s(x )
decision x s(x) P→0 P→0 at threshold τ
explanation
{w x }
i i i∈P
neutralize
proxies: x P→0
Fig. 1. The AIBF per-decision audit. The candidate is scored, the protected proxies are neutralized to a common privileged baseline, and the candidate is
re-scored.Thecounterfactualshift∆yieldsaper-decisionbiasmagnitude,aflagfordecisionswhoseoutcometheprotectedattributeschanged,andafaithful
explanationnamingtheresponsibleprotectedfactors.
TABLEII TABLEIII
COMPOSITIONOFTHETWODATASETS.BASERATEISTHERATEOFTHE AUDITEDSYSTEMSONTHETWOREALDATASETS.DIISTHEDISPARATE
FAVORABLEOUTCOMEFOREACHGROUPBEFOREANYMODELISAPPLIED. IMPACTRATIO,WHEREVALUESBELOW0.80FAILTHEFOUR-FIFTHSRULE.
Dataset Attribute Group Baserate Dataset Testn Advancerate DI(primary) DI(secondary)
Adult sex male(priv.) 30.4% Adult 14653 0.128 0.078(sex) 0.386(race)
Adult sex female(disadv.) 10.9% COMPAS 1584 0.605 0.645(race) –
Adult race white(priv.) 25.4%
Adult race non-white(disadv.) 15.3%
COMPAS race Caucasian(priv.) 60.9%
COMPAS race African-Am.(disadv.) 47.7% [5], [7], [9]. For detection we report the area under the ROC
curve and average precision for identifying counterfactual
flips, and for the operational analysis we report the recall of
the Caucasian group. These are the historical disparities a
harmed decisions as a function of the fraction of decisions
scorer trained on the data will absorb. Table II collects the
reviewed. Our baseline for detection and for targeted review
composition.
is group membership, that is flagging or reviewing candidates
B. The audited system because they belong to a disadvantaged group, which is the
natural non-localized alternative an operator would otherwise
For each dataset we train a logistic regression that predicts
use. We also compare against random review and, for detec-
theoutcomefromallfeatures,includingtheprotectedproxies,
tion, against a decision margin baseline.
to stand in for an applicant tracking system trained on histori-
caldatathatcarriesrealbias.Thisistherealisticadversaryfor VI. RESULTS
an auditor, a scorer that has learned to use protected proxies
Table III summarizes the two audited systems. Both exhibit
because they were predictive in biased historical outcomes.
severe real disparate impact. On Adult the disparate impact
AIBF audits this scorer through query access only.
ratio for sex is 0.078 and for race 0.386, both far below the
C. Preprocessing four-fifths threshold of 0.80. On COMPAS the ratio for race
For Adult we encode education and weekly hours as nu- onthefavorableoutcomeis0.645,alsobelowthreshold.These
meric merit features, one-hot encode work class as additional arepropertiesofrealdataandastandardclassifier,notinjected
merit features, and encode sex, race, and the age proxy as effects.
binary protected features indicating the disadvantaged group.
A. Faithfulness
ForCOMPASwefollowProPublica’sstandardfiltering,keep-
TableIVreportsthemeancounterfactualshiftbygroup.On
ing cases whose screening date is within thirty days of arrest,
Adulttheprotectedproxiesraisethescoreoftheprivilegedsex
whose recidivism flag is valid, and whose charge degree and
group by 7.49 points on average and lower the disadvantaged
score text are present, and we restrict to the two largest racial
group’s score by 7.95 points, a gap of 15.44 points that is
groups. We use numeric prior and juvenile counts and age
consistent in direction and relative size with the measured
as merit features, one-hot encode charge degree and sex, and
statisticalparitydifferenceof−0.170.TheraceandCOMPAS
encode race as the protected feature. Each dataset is split
results show the same pattern. This confirms that the per-
seventy to thirty into training and test partitions with a fixed
decision shift is faithful, in the sense that its group averages
seed, features are standardized on the training partition, and
reconstructthegroupleveldisparity,whichisthepropertythat
all reported numbers are on the held out test partition.
allows a per-decision audit to underwrite a group level report.
D. Metrics and baselines
Framing fairness as a measurement problem, as Jacobs and
Wereportthedisparateimpactratio,statisticalparitydiffer- Wallach urge [24], is what makes this aggregation the right
ence, and equal opportunity difference for the group analysis test of a per-decision signal.

TABLEIV
FAITHFULNESS.MEANCOUNTERFACTUALSHIFT∆(SCOREPOINTS)BY
GROUP,AGAINSTTHEGROUPSTATISTICALPARITYDIFFERENCE(SPD).
Dataset Attribute ∆priv. ∆disadv. GroupSPD
Adult sex +7.49 −7.95 −0.170
Adult race +3.55 −4.32 −0.087
COMPAS race +0.00 −1.21 −0.272
10
7.49
5 3.55
0
0
−1.21
−5 −4.32
−10 −7.95
Adult-sex Adult-race COMPAS-race
)stp
erocs(
∆
naem
TABLEV
SUMMARYACROSSBOTHDATASETS.DETECTIONAUCISFOR
IDENTIFYINGCOUNTERFACTUALFLIPS;THECOMPASAUCISHIGH
BECAUSECOMPASHASASINGLEPROTECTEDATTRIBUTE.
Quantity Adult COMPAS
Baselinedisparateimpactratio 0.078/0.386 0.645
Flagged(counterfactualflips) 8.0% 2.7%
Harmeddecisions 0.90% 2.65%
DetectionAUC(AIBF) 0.963 1.000
DetectionAUC(group) 0.672 0.707
privilegedgroup disadvantagedgroup DIaftercorrectingflags 0.449/0.582 0.703
TABLEVI
DETECTIONOFCOUNTERFACTUALLYBIASEDDECISIONSONADULT.
Signal ROCAUC Avg.precision
AIBFbiasmagnitude|∆| 0.963 0.749
Groupmembership 0.672 0.118
Ratiobiasscore(naive) 0.265 0.054
Fig. 2. Faithfulness. The mean counterfactual shift is positive for the priv- to0.703.Themethodthereforebehavesidenticallyinadomain
ileged group and negative for the disadvantaged group across both datasets,
outside hiring, which supports the claim that it audits a scorer
anditsmagnitudetracksthemeasuredstatisticalparitydifference.
rather than a dataset. Table V consolidates the COMPAS
figures beside the Adult figures.
B. Detection of biased decisions
C. Targeted review efficiency
On Adult, 8.0 percent of decisions are counterfactual flips The practical value of localization is that a limited human
and 0.90 percent are harmed decisions that would have ad- review budget can be directed to the decisions that most need
vanced but for the protected attributes. Table VI reports how it. Figure 4 plots the recall of harmed decisions against the
well each signal identifies the flips. The AIBF bias magnitude fraction of decisions reviewed, where review order is set by
achievesanareaundertheROCcurveof0.963andanaverage AIBF bias magnitude, by group membership, or at random.
precision of 0.749, against 0.672 and 0.118 for the group Reviewing the five percent of decisions with the largest AIBF
membership baseline. The gap in average precision is the magnitudesurfacesfifty-fivepercentofallharmedcandidates,
more telling number, because flips are rare, and it shows against six percent under group based review and six percent
that knowing a candidate’s group is a weak predictor of at random. Table VII gives the review budget needed to
whether that candidate’s decision was changed, whereas the reach given recall levels. To surface half of the harmed
counterfactual magnitude is a strong one. Figure 3 shows the candidates an operator reviews one percent of decisions under
ROC curves. We include a decision margin baseline, which AIBF against thirty-two percent under group based review, a
flagsdecisionsclosesttothethreshold,anditisunsurprisingly thirtyfold reduction in review effort for the same protective
a fair predictor of flips at an area under the curve of 0.883, coverage. The practical significance is that human review is
since flips must occur near the boundary. It is not, however, the binding constraint in a real audit, since a compliance
a bias detector: proximity to the threshold says nothing about team can examine only a small fraction of decisions, and a
whetherprotectedattributescausedtheproximity,soamargin method that concentrates the truly biased cases at the top of
flag conflates biased decisions with merely close ones. AIBF the queue converts an obligation that would otherwise be met
separatesthetwo,whichiswhyitexceedsthemarginbaseline by sampling into one that can be met by triage. The shape of
and why its flags carry an explanation the margin cannot the AIBF curve, which rises steeply and then plateaus, is the
provide. On COMPAS the area under the curve is 1.000 for shape a triage tool should have, because it places nearly all
AIBF against 0.707 for group membership; the perfect figure of the harmed decisions in the first portion of the queue and
isexpectedbecauseCOMPAShasasingleprotectedattribute, leaves a long tail of unaffected decisions that need no review.
so the counterfactual magnitude orders flips exactly, and we
D. Mitigation ceiling and proxy leakage
report the Adult figure with three protected attributes as the
meaningful result. On COMPAS the audit flags 2.7 percent of It is tempting to close the loop by automatically correcting
decisions as counterfactual flips and identifies 2.65 percent as every flagged decision to its counterfactual outcome. We
harmed, the mean shift is −1.21 points for the disadvantaged measured the effect and report it in full, because it reveals a
group against 0.00 for the privileged group, consistent with limitationthatoperatorsmustunderstand.OnAdult,correcting
the statistical parity difference of −0.272, and correcting the all flagged decisions raises the disparate impact ratio for sex
flagged decisions raises the disparate impact ratio from 0.645 from 0.078 to 0.449 and for race from 0.386 to 0.582, a

1
TABLEVII
REVIEWBUDGET(PERCENTOFDECISIONS)NEEDEDTOREACHAGIVEN
RECALLOFHARMEDDECISIONSONADULT.
etar 0.8
|     |     |     |     |     |     |     |     | Targetrecall |     | AIBF | Groupmembership |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | --------------- | --- | --- | --- |
evitisop 0.6
|      |     |     |     |     |                 |     |     | 50% |     | 1%  |     |     | 32% |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | 0.4 |     |     |     |                 |     |     | 80% |     | 34% |     |     | 57% |     |
|      |     |     |     |     |                 |     |     | 90% |     | 54% |     |     | 64% |     |
| eurt |     |     |     |     | AIBF(|∆|)       |     |     |     |     |     |     |     |     |     |
|      | 0.2 |     |     |     | Groupmembership |     |     |     |     |     |     |     |     |     |
Chance
|     |     |     |     |     |     |     |     |     |     | notflagged |     | flagged |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --- | --- |
0
|     | 0   | 0.2 | 0.4 | 0.6 |     | 0.8 1 | 40  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
snoisiced
|     |     |     | false | positive | rate |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
30
| Fig.3.    | DetectionofcounterfactuallybiaseddecisionsonAdult.AIBFreaches |              |               |       |               |            | 20  |     |     |     |     |     |     |     |
| --------- | ------------------------------------------------------------- | ------------ | ------------- | ----- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| an area   | under                                                         | the curve of | 0.963 against | 0.672 | for the group | membership | fo  |     |     |     |     |     |     |     |
| baseline. |                                                               |              |               |       |               |            | 10  |     |     |     |     |     |     |     |
%
|     | 1   |     |     |     |     |     |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
snoisiced
|     |     |     |     |     |     |     |     | 0-2 | 2-5 | 5-10 | 10-15 | 15-20 | 20-30 | 30+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ----- | ----- | --- |
0.8
Fig.5. DistributionoftheAIBFbiasmagnitude|∆|onAdult,inscorepoints.
demrah 0.6 Flaggeddecisionsconcentrateathighmagnitude,whilethemassofunflagged
decisionssitsnearzero,soamagnitudethresholdcleanlyseparatesthem.
0.4
| fo  |     |     |     |     | AIBF            |     |          |            |        |     |        |        |             |        |
| --- | --- | --- | --- | --- | --------------- | --- | -------- | ---------- | ------ | --- | ------ | ------ | ----------- | ------ |
|     |     |     |     |     |                 |     | features | contribute | +33.64 |     | points | in the | candidate’s | favor. |
|     | 0.2 |     |     |     | Groupmembership |     |          |            |        |     |        |        |             |        |
llacer
|     |     |     |     |     | Random |     | An auditor | reading |     | this does | not | receive | a bare | score but |
| --- | --- | --- | --- | --- | ------ | --- | ---------- | ------- | --- | --------- | --- | ------- | ------ | --------- |
0 an actionable account: this qualified candidate, whose merit
|      | 0         | 20                  | 40           | 60            | 80     | 100            |           |          |            |         |       |             |              |             |
| ---- | --------- | ------------------- | ------------ | ------------- | ------ | -------------- | --------- | -------- | ---------- | ------- | ----- | ----------- | ------------ | ----------- |
|      |           |                     |              |               |        |                | features  | alone    | would      | advance | them, | was         | rejected     | because     |
|      |           | fraction            | of decisions | reviewed      | (%)    |                |           |          |            |         |       |             |              |             |
|      |           |                     |              |               |        |                | protected | proxies  | subtracted |         | more  | than twenty | one          | net points, |
|      |           |                     |              |               |        |                | and the   | decision | warrants   | review. |       | This is     | the artifact | a per-      |
| Fig. | 4. Recall | of harmed decisions |              | versus review | budget | on Adult. AIBF |           |          |            |         |       |             |              |             |
|      |           |                     |              |               |        |                | decision  | audit    | obligation | calls   | for   | and         | that a group | metric      |
directedreviewrecoversmostharmedcandidatesatasmallbudget.
cannot produce.
|        |             |          |             |        |           |              |     |         |          | VII. DISCUSSION |     |        |         |           |
| ------ | ----------- | -------- | ----------- | ------ | --------- | ------------ | --- | ------- | -------- | --------------- | --- | ------ | ------- | --------- |
| large  | improvement | that     | nonetheless | falls  | short     | of the four- |     |         |          |                 |     |        |         |           |
|        |             |          |             |        |           |              | The | results | are best | understood      |     | not as | a claim | that AIBF |
| fifths | threshold   | of 0.80. | On          | COMPAS | the ratio | rises from   |     |         |          |                 |     |        |         |           |
0.645to0.703.Thereasonthecorrectiondoesnotreachparity is a better fairness metric, which it is not and does not try
is proxy leakage: features labeled as merit, such as education to be, but as a claim that it occupies a position no existing
|     |     |     |     |     |     |     | tool occupies, |     | between | the | population | level | metric | and the |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | --- | ---------- | ----- | ------ | ------- |
andhoursworkedonAdult,arethemselvescorrelatedwiththe
protected attributes, so neutralizing only the explicit protected generic local explainer, and that this position is the one that
|     |     |     |     |     |     |     | current | audit | obligations | require. |     | The evaluation |     | supports a |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ----------- | -------- | --- | -------------- | --- | ---------- |
proxiesleavesaresidualdisparitycarriedbythemeritfeatures.
|      |      |             |           |     |           |              | specific | claim | about | where | AIBF | fits. Against | group | fairness |
| ---- | ---- | ----------- | --------- | --- | --------- | ------------ | -------- | ----- | ----- | ----- | ---- | ------------- | ----- | -------- |
| This | is a | property of | the world | and | the data, | not a defect |          |       |       |       |      |               |       |          |
of the audit, and it is precisely why AIBF is positioned metrics, AIBF adds localization and explanation: it identifies
|     |             |                 |     |           |        |           | the individual |     | decisions | behind | an  | aggregate | disparity | and |
| --- | ----------- | --------------- | --- | --------- | ------ | --------- | -------------- | --- | --------- | ------ | --- | --------- | --------- | --- |
| as  | a detection | and explanation |     | tool that | routes | decisions | to             |     |           |        |     |           |           |     |
human judgment rather than as an automated corrector. The names their causes, which the metrics cannot do and which
|         |             |          |         |             |           |           | per-decision | audit | mandates  |        | require. | Against   | local | explainers, |
| ------- | ----------- | -------- | ------- | ----------- | --------- | --------- | ------------ | ----- | --------- | ------ | -------- | --------- | ----- | ----------- |
| finding | also        | cautions | against | any method, | including | group-    |              |       |           |        |          |           |       |             |
|         |             |          |         |             |           |           | AIBF adds    | a     | protected | versus | merit    | partition |       | and a coun- |
| blind   | approaches, | that     | assumes | removing    | explicit  | protected |              |       |           |        |          |           |       |             |
attributes yields a fair decision. terfactual decision level signal that is tied to whether the
|     |          |       |     |     |     |     | outcome | actually | changed, |        | which | raw attribution |          | magnitude |
| --- | -------- | ----- | --- | --- | --- | --- | ------- | -------- | -------- | ------ | ----- | --------------- | -------- | --------- |
| E.  | A worked | audit |     |     |     |     |         |          |          |        |       |                 |          |           |
|     |          |       |     |     |     |     | is not, | as the   | collapse | of the | ratio | baseline        | to below | chance    |
Table VIII shows the audit of a real harmed candidate demonstrates. The counterfactual construction is what unifies
from the Adult test set. The applicant scored 28.1 and was the two levels, because its per-decision values are faithful to
rejected, but the counterfactual score, with the protected the group disparity while remaining individually actionable.
proxies neutralized, is 66.3, an advance, so the decision is The review efficiency result is the most consequential for
a harmed flip with a shift of −38.1 points. The explanation practice. Audit mandates create a real operational problem,
attributes the shift to three protected factors, the largest being since a human cannot review every decision, and an operator
thefemaleproxyat−9.83pointsfollowedbytheageproxyat who reviews by group membership both wastes effort on
−7.16 and the minority race proxy at −4.52, while the merit unaffectedcandidatesand,asourcorrectionexperimentshows,

TABLEVIII natural fix, since it measures influence in the units of the
AIBFAUDITOFAREALHARMEDCANDIDATE(ADULTTESTSET).THE decisionitself.Wesuspectthisobservationappliesbeyondour
PROTECTEDPROXIESSUBTRACTENOUGHTOFLIPANOTHERWISE
particular score, to any attempt to summarize local fairness
FAVORABLEDECISION.
attributions into an actionable per-decision quantity, and we
Component Contribution(scorepts) offer it as guidance to others building such tools.
Meritfeatures(education,hours,workclass) +33.64
Protected:femaleproxy −9.83 D. Recommendations for auditors
Protected:age-over-40proxy −7.16
Protected:minority-raceproxy −4.52 The findings translate into concrete guidance for anyone
auditinganautomatedhiringsystem,whetherornottheyadopt
ATSscore(reject) 28.1
Counterfactualscore(advance) 66.3 this implementation.
Counterfactualshift∆ −38.1
• Audit at the decision level, then aggregate. Compute
the per-decision counterfactual first and derive the group
report from it, rather than computing only the group
risks overcorrecting. AIBF turns a population level obligation
metric, so that the aggregate always comes with the
into a ranked, explained worklist, which is the form in which
localized evidence behind it.
a compliance team can act on.
• Define bias relative to the decision boundary. Do not
A. Deployment rank decisions by raw or ratio attribution magnitude,
which ignores the margin and can invert the cases that
AIBF is intended to run in one of two modes. In batch
matter; rank by the counterfactual shift, which is in the
audit mode it processes a period’s decisions, produces the
units of the decision.
disparateimpactreportrequiredbyregulation,andattachesthe
• Prefer targeted review to blanket review. Reviewing
ranked worklist of flagged decisions with their explanations,
by group membership wastes scarce human attention on
which is the artifact an independent auditor under Local Law
unaffected candidates and risks overcorrection; a ranked
144 needs. In inline mode it audits each decision as it is
worklist directs review to the decisions protected at-
made and routes a flagged decision to human review before a
tributes changed.
rejectionisfinalized,whichistheposturethehumanoversight
• Treat the correction ceiling as a warning about prox-
requirement of the EU AI Act encourages. Both modes use
ies. If neutralizing explicit protected attributes does not
the same two queries per decision and the same explanation
reach parity, the residue is proxy leakage in the merit
machinery, and both keep the protected signals strictly on the
features, which should prompt scrutiny of those features
audit side of the system, never returning them to the scorer.
rather than confidence in a group-blind design.
B. Contestability • Calibrate the threshold locally and keep protected
data on the audit side. Tune the flag threshold on a
A per-decision, explained audit does more than direct re-
labeled sample for the specific deployment, and ensure
view. It makes a decision contestable, which is the affordance
the protected attributes used for auditing never re-enter
that both the counterfactual explanation literature [13] and
the scorer.
data protection law [26] treat as central to automated decision
making about people. A candidate told only that an opaque
E. Generality beyond hiring
system rejected them has nothing to challenge. A candidate
whose rejection carries a counterfactual, that the decision Although we motivate AIBF by automated hiring, nothing
wouldhavebeenanadvancehadprotectedproxiesnotlowered in the method is specific to it. The audit requires only a
the score by a stated number of points, together with the thresholded scoring decision, a partition of features into pro-
factors responsible, has a specific and answerable account. tected proxies and legitimate factors, and query access to the
AIBF produces that account as a byproduct of the same scorer, which are present in lending, insurance underwriting,
computation that drives detection, at no additional cost. admissions,tenantscreening,andpretrialriskassessment.The
COMPAS result is direct evidence of this generality, since it
C. A lesson for fairness attribution
is a criminal justice scorer rather than a hiring one, and AIBF
The collapse of the ratio baseline to below chance points audits it with the same faithfulness, the same clean separation
to a general lesson, because a ratio of protected to total of flipped decisions, and the same correction ceiling. What
attributionmagnitudeisanintuitiveandtemptingdefinitionof transfers is the core observation that a per-decision fairness
per-decision bias, and it is the definition an earlier version of signal should be defined by a counterfactual on the protected
this work used. The finding is that any per-decision fairness partitionrelativetothedecisionboundary,whichturnsagroup
signal computed from attribution magnitudes alone, without level obligation into an individually actionable, explainable
reference to the decision boundary, can rank the decisions auditinanyofthesedomains.Wereporthiringresultsbecause
that matter in the wrong order, because influence that does that is where the per-decision audit mandate is most explicit
not move a decision across the threshold is not the influence today, but the method is a general instrument for auditing
an audit cares about. The counterfactual construction is the thresholded decisions about people.

| VIII. | LIMITATIONSANDTHREATSTOVALIDITY |     |     |     |     |     | B. Reproducibility |        |         |       |             |     |        |          |
| ----- | ------------------------------- | --- | --- | --- | --- | --- | ------------------ | ------ | ------- | ----- | ----------- | --- | ------ | -------- |
|       |                                 |     |     |     |     |     | Every              | number | in this | paper | is produced |     | by the | released |
Westatethelimitsdirectly,sinceseveralboundthestrength
scriptsfrompublicdatasetswithafixedrandomseed.Thedata
of the results. preparation,theauditedclassifier,thecounterfactualaudit,the
Model based, not causal. AIBF intervenes on the de- detection and review-efficiency analyses, and the figure data
•
ployed scorer’s inputs rather than on a structural causal are each a single command, so the results can be regenerated
|       |     |           |          |             |     |           | and inspected |     | rather than | taken | on  | trust. | We regard | this as |
| ----- | --- | --------- | -------- | ----------- | --- | --------- | ------------- | --- | ----------- | ----- | --- | ------ | --------- | ------- |
| model | of  | the world | [12], so | it measures | the | influence |               |     |             |       |     |        |           |         |
the scorer places on protected proxies. This is the right essentialforanauditingmethod,whoseownclaimsshouldbe
|        |         |            |          |            |         |              | as checkable |     | as the decisions |     | it audits. |     |     |     |
| ------ | ------- | ---------- | -------- | ---------- | ------- | ------------ | ------------ | --- | ---------------- | --- | ---------- | --- | --- | --- |
| target | for     | auditing a | specific | deployed   | system, | but it       | is           |     |                  |     |            |     |     |     |
| not    | a claim | about real | world    | causation, | and     | a proxy that |              |     |                  |     |            |     |     |     |
the scorer reads only indirectly is captured only to the IX. ETHICALANDLEGALCONSIDERATIONS
extent the neutralized features carry it. AIBF is designed to support human and legal judgment
| Proxy | coverage. | AIBF | audits | the | proxies | it is given. |     |     |     |     |     |     |     |     |
| ----- | --------- | ---- | ------ | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
• rather than to replace it. Its per-decision, counterfactual rea-
Proxiesitdoesnotmodel,andtheresidualproxyleakage soning is compatible with the selection rate and impact ratio
documented in Section VI, limit both detection and any reporting required by New York City Local Law 144 [3] and
| correction, |     | which is | why the | corrected | disparate | impact |          |             |      |      |         |              |     |           |
| ----------- | --- | -------- | ------- | --------- | --------- | ------ | -------- | ----------- | ---- | ---- | ------- | ------------ | --- | --------- |
|             |     |          |         |           |           |        | with the | four-fifths | rule | [5], | and its | transparency |     | and human |
ratio does not reach parity. oversight posture align with the EU AI Act’s obligations for
Linear reference for explanations. The itemized expla- high risk recruitment AI [4] and with the contestability aims
•
nation uses a linear reference model, which makes the behindcounterfactualexplanation[13]anddataprotectionlaw
additive attribution exact for that reference but under- [26]. Because the protected signals AIBF uses are themselves
describesastronglynon-linearscorer.Thedecisionsignal
|     |     |     |     |     |     |     | sensitive, | the | method treats | them | strictly | as  | audit | inputs and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | ---- | -------- | --- | ----- | ---------- |
∆ is unaffected, since it is computed on the true scorer. never as scoring inputs, and it recommends that flagged
Audited systems are our own. We audit standard clas- decisions route to human review rather than to automatic
•
| sifiers | trained | on real | data | rather | than proprietary | pro- |         |       |            |      |          |       |           |      |
| ------- | ------- | ------- | ---- | ------ | ---------------- | ---- | ------- | ----- | ---------- | ---- | -------- | ----- | --------- | ---- |
|         |         |         |      |        |                  |      | action, | since | a detector | that | misfires | would | otherwise | harm |
duction systems, which we cannot access. The disparate the very candidates it is meant to protect. All experiments in
| impact | these | systems       | exhibit | is real, | but the  | magnitudes |            |       |                 |     |          |     |         |            |
| ------ | ----- | ------------- | ------- | -------- | -------- | ---------- | ---------- | ----- | --------------- | --- | -------- | --- | ------- | ---------- |
|        |       |               |         |          |          |            | this paper | use   | public research |     | datasets | and | contain | no private |
| on a   | given | vendor system | would   | differ,  | and only | a study    | candidate  | data. |                 |     |          |     |         |            |
with scoring access could measure them. Theaudititselfmustbeusedresponsibly.Abiasmagnitude
| A signal, |     | not a verdict. | A   | high | bias magnitude | is  | a   |     |     |     |     |     |     |     |
| --------- | --- | -------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• threshold is an operating point, and setting it too aggressively
trigger for human review, not a legal determination of floods human reviewers and risks second guessing sound
| discrimination, |     | and | the paper’s | numbers | should | not be |            |       |         |        |              |     |        |           |
| --------------- | --- | --- | ----------- | ------- | ------ | ------ | ---------- | ----- | ------- | ------ | ------------ | --- | ------ | --------- |
|                 |     |     |             |         |        |        | decisions, | while | setting | it too | permissively |     | misses | harm; the |
read as adjudicating any specific system. threshold should be calibrated on a labeled sample for each
|     |     |     |     |     |     |     | deployment |     | rather than | carried | over | from | another | setting, a |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | ------- | ---- | ---- | ------- | ---------- |
cautionreinforcedbyourownfindingthatathresholdtunedon
| A. Threats | to validity |     |     |     |     |     |                  |     |             |         |     |         |      |          |
| ---------- | ----------- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ------- | --- | ------- | ---- | -------- |
|            |             |     |     |     |     |     | one distribution |     | transferred | poorly. |     | Because | AIBF | consumes |
Weseparatethreequestionsbecausetheybeardifferentlyon protected attributes to perform its audit, those attributes must
|     |     |     |     |     |     |     | be handled |     | under the same | protections |     | as  | any sensitive | data |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | ----------- | --- | --- | ------------- | ---- |
theclaims.Thefirst,constructvalidity,iswhetherthecounter-
|              |        |               |       |                 |     |             | and must | never | be allowed | to  | flow back | into | the scoring | path, |
| ------------ | ------ | ------------- | ----- | --------------- | --- | ----------- | -------- | ----- | ---------- | --- | --------- | ---- | ----------- | ----- |
| factual flip | is the | right target. | It is | the operational |     | analogue of |          |       |            |     |           |      |             |       |
counterfactualfairnessforadeployedscorer[12],anditgives whichthedesignenforcesbykeepingthemstrictlyontheaudit
|     |     |     |     |     |     |     | side. | Finally, | an audit | that improves |     | the efficiency |     | of review |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | -------- | ------------- | --- | -------------- | --- | --------- |
anauditorwhattheyneed,aflaggeddecisionthatarriveswith
a concrete witness of the change, though it captures influence is not a substitute for the human judgment it informs, and its
|            |       |         |            |            |     |             | outputs | are | evidence for | a person, | not | a verdict. |     |     |
| ---------- | ----- | ------- | ---------- | ---------- | --- | ----------- | ------- | --- | ------------ | --------- | --- | ---------- | --- | --- |
| within the | model | and not | real world | causation. |     | The second, |         |     |              |           |     |            |     |     |
internalvalidity,iswhetherthecomparisonisfair,andherethe
X. CONCLUSIONANDFUTUREWORK
| AIBF signal, | the | group baseline, |     | the margin | baseline, | and the |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --- | ---------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ratioareallscoredagainstthesameflipsonthesameheldout We presented AIBF, a counterfactual per-decision method
data with the same scorer, so the gaps between them reflect for auditing bias in automated hiring that produces a signed
the signal and not the setup. The third, external validity, is biasinscorepoints,aflagforthedecisionsprotectedattributes
where the claims are weakest: we trained the audited scorers changed, and an explanation of why. On two real datasets the
ourselves,thedatasetsnumbertwo,andoneliesoutsidehiring, per-decision signal is faithful to the group disparity, detects
so the specific magnitudes will not carry over to a particular biased decisions far better than a group membership baseline,
production system. What does carry over is the shape of the and turns a population level audit obligation into an efficient,
findings, that the counterfactual signal is faithful, that it beats explained review worklist. We also showed that attribution
the group baseline at localizing biased decisions, and that the based correction improves the disparate impact ratio without
ratiofails,sincethesefollowfromtheconstructionratherthan reaching parity, because merit features carry residual proxy
| from the | data at | hand. |     |     |     |     | correlation. |     |     |     |     |     |     |     |
| -------- | ------- | ----- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |

Future work proceeds along four lines. The first is a causal ogy, vol. 31, no. 2, pp. 841-887, 2018. [Online]. Available:
https://arxiv.org/abs/1711.00399
formulationthatintervenesonastructuralmodelratherthanon
|              |         |            |     |                     |     |     |        | [14] M. T. | Ribeiro, | S. Singh, | and | C. Guestrin, | “Why | should | I   |
| ------------ | ------- | ---------- | --- | ------------------- | --- | --- | ------ | ---------- | -------- | --------- | --- | ------------ | ---- | ------ | --- |
| the scorer’s | inputs, | tightening |     | the counterfactual. |     | The | second |            |          |           |     |              |      |        |     |
trustyou?Explainingthepredictionsofanyclassifier,”inProc.
| is proxy | discovery, | learning | which | nominally |     | neutral | features |      |            |     |            |           |           |     |     |
| -------- | ---------- | -------- | ----- | --------- | --- | ------- | -------- | ---- | ---------- | --- | ---------- | --------- | --------- | --- | --- |
|          |            |          |       |           |     |         |          | 22nd | ACM SIGKDD |     | Int. Conf. | Knowledge | Discovery |     | and |
leakprotectedinformationsothattheauditandanycorrection DataMining(KDD),2016,pp.1135-1144.[Online].Available:
can account for them. The third is a study on live proprietary https://doi.org/10.1145/2939672.2939778
|            |           |         |         |            |            |                  |     | [15] S. M. | Lundberg                         | and S.-I.     | Lee,        | “A unified | approach   | to          | inter- |
| ---------- | --------- | ------- | ------- | ---------- | ---------- | ---------------- | --- | ---------- | -------------------------------- | ------------- | ----------- | ---------- | ---------- | ----------- | ------ |
| applicant  | tracking  | systems | through | their      | scoring    | interfaces,      |     | to         |                                  |               |             |            |            |             |        |
|            |           |         |         |            |            |                  |     | preting    | model                            | predictions,” | in Advances | in         | Neural     | Information |        |
| measure    | disparate | impact  | and     | audit      | efficiency | in production.   |     |            |                                  |               |             |            |            |             |        |
|            |           |         |         |            |            |                  |     | Processing | Systems                          | (NeurIPS),    | 2017,       | pp.        | 4765-4774. | [Online].   |        |
| The fourth | is        | a human | study   | of whether |            | the explanations |     |            |                                  |               |             |            |            |             |        |
|            |           |         |         |            |            |                  |     | Available: | https://arxiv.org/abs/1705.07874 |               |             |            |            |             |        |
change reviewer decisions in practice. The implementation, [16] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, and A.
the datasets’ preparation, and the scripts that produce every Galstyan, “A survey on bias and fairness in machine learning,”
|     |     |     |     |     |     |     |     | ACM | Computing | Surveys, | vol. | 54, no. | 6, pp. | 1-35, | 2021. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---- | ------- | ------ | ----- | ----- |
numberinthispaperareavailableundertheApache2.0license
|                |     |        |             |     |     |     |     | [Online].  | Available:     | https://doi.org/10.1145/3457607 |          |          |            |               |     |
| -------------- | --- | ------ | ----------- | --- | --- | --- | --- | ---------- | -------------- | ------------------------------- | -------- | -------- | ---------- | ------------- | --- |
| at the address |     | on the | title page. |     |     |     |     |            |                |                                 |          |          |            |               |     |
|                |     |        |             |     |     |     |     | [17] R. K. | E. Bellamy     | et                              | al., “AI | Fairness | 360:       | An extensible |     |
|                |     |        |             |     |     |     |     | toolkit    | for detecting, | understanding,                  |          | and      | mitigating | unwanted      |     |
REFERENCES algorithmic bias,” IBM Journal of Research and Development,
|     |     |     |     |     |     |     |     | vol. 63, | no. 4/5, | pp. 4:1-4:15, | 2019. | [Online]. | Available: |     | https: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------------- | ----- | --------- | ---------- | --- | ------ |
[1] Mobley v. Workday, Inc., No. 3:23-cv-00770-RFL (N.D. Cal.), //doi.org/10.1147/JRD.2019.2942287
ordergrantingpreliminarycollectivecertification,May16,2025. [18] S. Bird, M. Dudik, R. Edgar, B. Horn, R. Lutz, V. Mi-
[2] EEOC v. iTutorGroup, Inc., No. 1:22-cv-02565 (E.D.N.Y.), lan, M. Sameki, H. Wallach, and K. Walker, “Fairlearn: A
consent decree, 2023. toolkit for assessing and improving fairness in AI,” Microsoft,
[3] NewYorkCityDept.ofConsumerandWorkerProtection,“Lo- Tech. Rep. MSR-TR-2020-32, 2020. [Online]. Available: https:
calLaw144of2021:AutomatedEmploymentDecisionTools,” //github.com/fairlearn/fairlearn
effectiveJul.5,2023.[Online].Available:https://www.nyc.gov/ [19] B. H. Zhang, B. Lemoine, and M. Mitchell, “Mitigating un-
site/dca/about/automated-employment-decision-tools.page wanted biases with adversarial learning,” in Proc. AAAI/ACM
[4] EuropeanParliamentandCouncil,“Regulation(EU)2024/1689 Conf. AI, Ethics, and Society (AIES), 2018, pp. 335-340.
layingdownharmonisedrulesonartificialintelligence(Artificial [Online]. Available: https://arxiv.org/abs/1801.07593
IntelligenceAct),”2024.[Online].Available:http://data.europa. [20] M.Raghavan,S.Barocas,J.Kleinberg,andK.Levy,“Mitigat-
eu/eli/reg/2024/1689/oj ingbiasinalgorithmichiring:Evaluatingclaimsandpractices,”
[5] Equal Employment Opportunity Commission et al., “Uniform inProc.ACMConf.Fairness,Accountability,andTransparency
Guidelines on Employee Selection Procedures,” 29 C.F.R. pt. (FAT*), 2020, pp. 469-481. [Online]. Available: https://doi.org/
1607, 1978. [Online]. Available: https://www.ecfr.gov/current/ 10.1145/3351095.3372828
title-29/part-1607 [21] C.Wilson,A.Ghosh,S.Jiang,A.Mislove,L.Baker,J.Szary,K.
[6] S. Barocas and A. D. Selbst, “Big data’s disparate impact,” Trindel, and F. Polli, “Building and auditing fair algorithms: A
California Law Review, vol. 104, no. 3, pp. 671-732, 2016. casestudyincandidatescreening,”inProc.ACMConf.Fairness,
[Online]. Available: https://doi.org/10.15779/Z38BG31 Accountability, and Transparency (FAccT), 2021, pp. 666-677.
[7] M. Feldman, S. A. Friedler, J. Moeller, C. Scheidegger, and [Online]. Available: https://doi.org/10.1145/3442188.3445928
S. Venkatasubramanian, “Certifying and removing disparate [22] J.Sanchez-Monedero,L.Dencik,andL.Edwards,“Whatdoes
impact,” in Proc. 21st ACM SIGKDD Int. Conf. Knowledge itmeantosolvetheproblemofdiscriminationinhiring?Social,
Discovery and Data Mining (KDD), 2015, pp. 259-268. [On- technicalandlegalperspectivesfromtheUKonautomatedhir-
line]. Available: https://doi.org/10.1145/2783258.2783311 ingsystems,”inProc.ACMConf.Fairness,Accountability,and
[8] C. Dwork, M. Hardt, T. Pitassi, O. Reingold, and R. Zemel, Transparency (FAT*), 2020, pp. 458-468. [Online]. Available:
“Fairness through awareness,” in Proc. 3rd Innovations in The- https://doi.org/10.1145/3351095.3372849
oretical Computer Science Conf. (ITCS), 2012, pp. 214-226. [23] A. Kochling and M. C. Wehner, “Discriminated by an algo-
[Online]. Available: https://doi.org/10.1145/2090236.2090255 rithm: A systematic review of discrimination and fairness by
[9] M. Hardt, E. Price, and N. Srebro, “Equality of opportunity algorithmic decision-making in the context of HR recruitment
in supervised learning,” in Advances in Neural Information and HR development,” Business Research, vol. 13, no. 3,
Processing Systems (NeurIPS), 2016, pp. 3315-3323. [Online]. pp. 795-848, 2020. [Online]. Available: https://doi.org/10.1007/
Available: https://arxiv.org/abs/1610.02413 s40685-020-00134-w
[10] A. Chouldechova, “Fair prediction with disparate impact: A [24] A. Z. Jacobs and H. Wallach, “Measurement and fairness,” in
study of bias in recidivism prediction instruments,” Big Data, Proc. ACM Conf. Fairness, Accountability, and Transparency
vol. 5, no. 2, pp. 153-163, 2017. [Online]. Available: https: (FAccT),2021,pp.375-385.[Online].Available:https://doi.org/
| //doi.org/10.1089/big.2016.0047 |     |     |     |     |     |     |     | 10.1145/3442188.3445901 |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
[11] S. Corbett-Davies, E. Pierson, A. Feller, S. Goel, and A. Huq, [25] M.BogenandA.Rieke,“Helpwanted:Anexaminationofhir-
“Algorithmicdecisionmakingandthecostoffairness,”inProc. ingalgorithms,equity,andbias,”Upturn,2018.[Online].Avail-
23rdACMSIGKDDInt.Conf.KnowledgeDiscoveryandData able: https://www.upturn.org/reports/2018/hiring-algorithms/
Mining (KDD), 2017, pp. 797-806. [Online]. Available: https: [26] European Parliament and Council, “Regulation (EU) 2016/679
//doi.org/10.1145/3097983.3098095 (General Data Protection Regulation), Article 22,” 2016. [On-
[12] M. J. Kusner, J. R. Loftus, C. Russell, and R. Silva, “Counter- line]. Available: http://data.europa.eu/eli/reg/2016/679/oj
factualfairness,”inAdvancesinNeuralInformationProcessing
| Systems | (NeurIPS), |     | 2017, pp. | 4066-4076. | [Online]. |     | Available: |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --------- | ---------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://arxiv.org/abs/1703.06856
| [13] S.      | Wachter, | B. Mittelstadt, |         | and C.    | Russell, | “Counterfactual |          |     |     |     |     |     |     |     |     |
| ------------ | -------- | --------------- | ------- | --------- | -------- | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| explanations |          | without         | opening | the black | box:     | Automated       | deci-    |     |     |     |     |     |     |     |     |
| sions        | and      | the GDPR,”      | Harvard | Journal   | of       | Law and         | Technol- |     |     |     |     |     |     |     |     |
---- END DOCUMENT ----
