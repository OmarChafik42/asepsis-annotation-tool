Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
A Privacy Budgeting Framework for Online
Experimentation
Gilian R. Ponte, Alina Ferecatu
RotterdamSchoolofManagement,ErasmusUniversity
Firmsperformonlineexperimentswithmulti-armedbanditstopersonalizewhatconsumersareshownwhile
balancing exploration and exploitation. However, third-parties can infer consumers’ underlying segments
from observing which banners, ads, or recommendations consumers receive. To control this inference, we
propose a privacy arisk budget that firms can set ex ante to bound such third party belief updating using
differential privacy. To spend this privacy risk budget, we propose two strategies: a constant privacy risk
strategy and a dynamic privacy risk strategy that spend privacy risk differently across visitor. We study
how privacy risk budgets affect experimentation performance in two applications—website design and a
recommendation system—under these strategies. For both strategies, we analytically find privacy risk bud-
gets that optimally balance exploration and exploitation. We then extend the idea of an experiment-level
privacy risk budget to a firm-wide privacy risk budget. We apply this firm-wide privacy risk budget in an
empirical setting with 78 experiments. We find that the dynamic strategy is particularly valuable in longer
andmorecomplexexperiments,andthatoptimizingtheallocationofafirm-wideprivacyriskbudgetacross
experiments substantially improves learning performance.
Keywords: differential privacy; privacy risk budget; multi-armed bandits; online experimentation.
1. Introduction
Firms routinely experiment with website banners, links, and recommendations to improve
engagement and profitability. However, online experimentation also raises privacy concerns,
particularly because third-parties can track what consumers are shown and use those expo-
sures to infer their interests and behaviors (Goldfarb and Tucker 2011, Summers et al. 2016,
Kim et al. 2018, Shaddy et al. 2026). These concerns translate into economic costs for firms:
consumers increasingly opt out of tracking (Tucker 2014, Johnson et al. 2020, Wang et al.
2024, Miller and Skiera 2024) and place a premium on privacy-respecting brands (Moffett
et al. 2025).
1
6202
guA
12
]ME.noce[
2v44991.8062:viXra

2
To illustrate the privacy risk of experimentation, consider Jamie, a frequent reader of
fantasy novels who visits the online bookstore Barnes & Noble. Third-party software that
monitors the website, which we refer to as a tracker, may hold a prior belief that Jamie
is a fantasy reader based on public information, such as their Goodreads account. Barnes
& Noble first segments customers by book-genre preferences and then experiments to learn
which output, such as a book recommendation, performs best for each segment.1 To improve
its recommendations, Barnes & Noble balances learning—randomly displaying different
recommendations—with earning—using experimental results to select the currently best-
performing recommendation.
This balance between learning and earning shapes Jamie’s privacy risk. Under optimiza-
tion, the recommendation closely reflects Jamie’s segment and underlying preference, there-
fore introducing a privacy risk. By contrast, experimentation implies randomization, which
makesrecommendationsstochasticandweakensthelinktoJamie’ssegment.Thus,optimiza-
tion improves performance but increases privacy risk, whereas randomization strengthens
privacy protection at the cost of displaying a suboptimal recommendation.
This privacy risk materializes when Jamie’s visit to Barnes & Noble allows the tracker
to update its prior belief about Jamie’s book preferences through two information channels
displayed in Figure 1: the experimental output, i.e., the book recommendation, and Jamie’s
interactionwiththeoutput,i.e.,aclickontherecommendedbook(seeWebAppendixAfora
formal decomposition). The information available to the tracker depends on Jamie’s GDPR-
style consent decision (Johnson et al. 2020, Choi et al. 2023), the use of an ad blocker (Todri
2022), and the privacy policies of the firm (Brough et al. 2022). When the information is not
1Barnes&Noblepersonalizescontentandmeasuresmarketingeffectivenesswiththird-partypartners.Barnes&Noble
(2026): “This is done so that we can personalize and enhance your browsing and shopping experience.”

3
available, the tracker cannot observe either the experimental output or Jamie’s subsequent
interactions with the output. When the information is available, the tracker loads with the
page and observes information from the first channel, the experimental output displayed to
Jamie. The book recommendation Jamie sees reveals information about Jamie’s interests
(e.g., see Summers et al. 2016, Kim et al. 2018). A fantasy book recommendation allows
the tracker to increase their belief that Jamie belongs to the fantasy segment. The second
channel is Jamie’s interaction with the displayed output. If Jamie clicks on the fantasy book
recommendation, the click provides an additional signal that further increases the tracker’s
belief that Jamie is a fantasy reader. Together, these channels show that experimentation
| creates | privacy risk | through | both exposure | and interaction. |     |     |
| ------- | ------------ | ------- | ------------- | ---------------- | --- | --- |
Privacyrisk Privacyrisk
|     | Tracker’s   |         | Channel1 | Channel2 |     | Tracker’s       |
| --- | ----------- | ------- | -------- | -------- | --- | --------------- |
|     | priorbelief | (cid:2) |          | (cid:2)  | =   | posteriorbelief |
Experimentaloutput Interaction
|     | aboutsegment |     |     |     |     | aboutsegment |
| --- | ------------ | --- | --- | --- | --- | ------------ |
Whatdoestheoutput Whatdoclicks
|     | membership |     |                   |                   |     | membership |
| --- | ---------- | --- | ----------------- | ----------------- | --- | ---------- |
|     |            |     | revealaboutJamie? | revealaboutJamie? |     |            |
Thefocusofthis
paper’sprivacyguarantee.
Figure1 A decomposition of the tracker’s posterior belief update about segment membership into two privacy
|     | risk channels, | conditional | on access. |     |     |     |
| --- | -------------- | ----------- | ---------- | --- | --- | --- |
Our privacy guarantee operates at the impression level, bounding how much an experi-
mental output can update a tracker’s belief about a consumer’s segment membership (see
Figure 1, Channel 1). We protect every displayed experimental output rather than inter-
actions with that output (see Figure 1, Channel 2). Protecting impressions is particularly
important because most displayed outputs do not generate clicks in low-CTR settings (Mela
et al. 2026), yet experimental outputs may still reveal behavioral information that is used
to personalize them (Castelluccia et al. 2012, Xin et al. 2023, Chen et al. 2026).
Inthispaper,wedevelopaprivacy-budgetingframeworkthatenablesfirmstoquantifyand
manage the trade-off between the privacy risk of experimentation—at the customer, exper-
iment, and firm levels—and firm performance (see Figure 2). We make three contributions.

4
|     |     |     |     | Level 1: Customer-level | privacy | risk ξ: |     |
| --- | --- | --- | --- | ----------------------- | ------- | ------- | --- |
Thefirmassignsprivacyrisktoeachvisitor.
|     |     |     |     | exploitation | exploration |     |     |
| --- | --- | --- | --- | ------------ | ----------- | --- | --- |
|     |     |     |     | (w.p.1−ε(ξ)) | (w.p.ε(ξ))  |     |     |
Firmservesbook
Jamie.
|     |     | withhighestclicks. |       |                     |                | Firmservesarandombook |     |
| --- | --- | ------------------ | ----- | ------------------- | -------------- | --------------------- | --- |
|     |     | 1                  |       |                     | t              |                       | T   |
|     |     |                    | Level | 2: Experiment-level | privacy budget |                       | γ:  |
Foreachexperiment,thelargestvisitor-level
privacyriskisboundedbytheexperiment-levelbudget.
|     | Experiment1: |     |     | Experiment2:       | Experiment3:   |     | Experiment4:    |
| --- | ------------ | --- | --- | ------------------ | -------------- | --- | --------------- |
|     | comingofage  |     |     | fantasy            | sciencefiction |     | literaryfiction |
|     |              |     |     | Level 3: Firm-wide | privacy budget |     | Γ:              |
Acrossexperiments,thefirm-widebudgetbounds
thetotalexperiment-levelprivacyrisk.
Figure2 Privacy budgeting in online experimentation operates at three connected levels: (1) the customer, (2)
| the experiment, |     | and | (3) the | firm level. |     |     |     |
| --------------- | --- | --- | ------- | ----------- | --- | --- | --- |
First, we use differential privacy to bound the privacy risk of experimentation: the extent
to which third-parties can update their belief about a consumer’s segment membership after
observing the experimental output (Dwork and Roth 2014). Building on this guarantee, we
develop a privacy-budgeting framework for online experimentation. We quantify the privacy
risk of experimentation by leveraging the link between differential privacy and multi-armed
bandits (MABs) experimentation under the ε-greedy policy (Sutton and Barto 2018). Under
ε-greedy, the firm serves a random option with probability ε and the best-performing option
1(cid:0)ε
with probability (see Figure 2, Level 1). The degree of randomization is governed by
the most granular privacy risk parameter, ξ, set under differential privacy. This parameter ξ
bounds how much observing the experimental output can update a tracker’s posterior beliefs

5
about a consumer’s segment membership. Greater randomization in experimental outputs
lowers privacy risk: as the exploration probability ε increases, the privacy risk parameter ξ
decreases.
Second, we propose an experiment-level privacy risk budget γ that extends customer-level
privacy risk across the full experiment (cf. Christoph 2026; see Figure 2, Level 2). To allocate
privacy budget across visitors, we propose two strategies: a constant strategy that allocates
the same privacy risk to every customer and a dynamic strategy that varies privacy risk
across customers to optimally balance learning and rewards. Privacy protection is costly;
increasing privacy protection limits the firm’s rewards from experimentation. We quantify
the tradeoff between privacy protection and rewards using a regret analysis (also see Hsu
et al. 2014). We derive a privacy elasticity of regret to measure the percent change in regret
induced by a 1% increase in the privacy budget (cf. Dekel et al. 2022). The privacy elasticity
helps managers choose privacy protection levels that minimize regret. We then extend γ
to a firm-wide privacy budget Γ and use privacy elasticities to allocate privacy risk across
experiments according to their highest marginal returns, analogous to allocating a marketing
budget across campaigns (e.g., Fischer et al. 2011, Peers et al. 2017, Zia and Rao 2019) (see
Figure 2, Level 3).
Third, we use empirically-grounded simulations to evaluate how privacy budgets affect
learning performance within and across experiments. Within experiments, we compare the
constant and dynamic strategies in website-design and recommendation settings. Across
experiments, we study how firms should allocate a fixed firm-wide privacy budget across
multiple experiments to maximize rewards. We find that portfolio-level optimization using
the regret bounds substantially improves rewards relative to benchmark allocations under
the same firm-wide budget.

6
The rest of the paper proceeds as follows. Section 2 reviews related work on privacy pro-
tection and experimentation via MABs. Sections 3–5 introduce the strategies, evaluate their
performance across applications, and derive the elasticities. Section 6 introduces the firm-
wide privacy budget and applies the resulting portfolio model to a set of contemporaneous
experiments. Section 7 concludes.
2. Privacy protection and experimentation via MABs
We embed a privacy protection mechanism, differential privacy, into online experimentation
performedviaMABs.WeexperimentusingMABsbecausetheirlinkwithdifferentialprivacy
allows us to quantify the privacy risk of experimentation and set different privacy budgets
across experiments.2
We next review the literature related to both building blocks of our privacy budgeting
framework and connect the bodies of work.
2.1. Experimentation via MABs
In MAB experimentation, the goal is to repeatedly choose between several outputs, labeled
as “arms,” to maximize overall rewards over a predefined time horizon. To do so, one must
balance exploring different outputs to learn their profitability with exploiting the option
that maximizes total rewards. The marketing literature has incorporated MABs into display
advertising (Schwartz et al. 2017), website morphing (Hauser et al. 2009, 2014, Liberali and
Ferecatu2022),pricing(Misraetal.2019),house-adrecommendations(Aramayoetal.2023),
2Unlike MABs, A/B testing does not allow for variation in privacy protection. During the learning phase, visitors
face no privacy risk because of the random assignment of different outputs. During the earning phase however, all
visitors are assigned to the best-performing option. During this stage, privacy risk is unbounded. An experiment set
upasanA/Btestcannotdeviatefromthisprivacyprotectionschedule,andvisitorshaveeitherazerooraninfinite
privacy risk depending on whether they visit the website during the learning or the earning stage. Firms cannot set
up privacy budgets and ensure different levels of privacy protection to their visitors.

7
and ranked search results (De los Santos and Koulayev 2017). The primary focus of these
studies is to empirically validate experimental methods and algorithms. Our focus is instead
on embedding privacy protection into experimentation via MABs. We focus on the ε-greedy
policy because the inherent stochasticity of this heuristic allows us to link it with differential
privacy. In marketing, Wang et al. (2025) applied MABs and specifically the epsilon-greedy
policy to optimize recommender systems.
Given our focus on segment specific experimentation, our bandit method is also similar
to contextual bandits, which improves assignment by taking into account both user and
context features to optimize learning. Our method differs from contextual bandits in two
important ways: first, we focus on a limited number of segments, unlike a contextual bandit
that typically takes as input a large set of user and context variables (Li et al. 2010). Second,
and linked to the first, because of the large number of features, the privacy threat is hard
to define and contain. We propose a clear measure of privacy risk, directly linked to what
third-party can infer about consumers.
2.2. The privacy protection literature
Our work focuses on protecting the privacy of consumers when exposed to experimental
output (see Figure 1). We position our contribution relative to privacy-related work focused
on the privacy risk channels shown in Figure 1: experimental output exposure, and con-
sumer’s interaction with the experimental output. The availability of these channels to a
tracker depends on consumers accepting tracking technologies and ad blocking decisions. We
therefore first review research on the factors that determine tracking access and then discuss
the literature related to each privacy risk channel.
2.2.1. Tracking access as a precondition for privacy risk. A stream of work studies the
economic costs of privacy choices and regulations that restrict firms’ ability to observe, track,

8
or link consumers across contexts. Johnson et al. (2020) document that consumers who opt
out of behavioral advertising generate 52% less revenue than impressions from consumers
who allow behavioral targeting. Aridor et al. (2024) show that Apple’s App Tracking Trans-
parency (ATT) policy led to revenue declines of 8% to 40% for affected firms. Kraft et al.
(2023) show a decrease of 20% in advertising revenue when users are allowed to gradually
control their privacy settings via the Apple’s ATT. Miller and Skiera (2024) show that lim-
iting cookie-based tracking could put 904 million euros in annual revenue at risk. Similarly,
Korganbekova and Zuber (2024) find that Safari’s seven-day cookie policy destroys 13.1% of
the personalization gain. Regarding ad blocking, Todri (2022) finds that ad blockers reduce
onlineconsumerspendingbyloweringconsumers’searchactivityandshiftingpurchasesaway
from new brands.
Korganbekova and Zuber (2024) argue that limiting tracking may not fully protect privacy
because firms can still learn about consumers from consumers with related characteristics
(also see Wernerfelt et al. (2025); Aguiar et al. (2026)). This shows that in addition to
consent, the experimental output may consequently require protection even when consumers
did not consent to its use for inference—or even to being shown the output in the first place.
Consumers who are shown the same output may be placed in the same inferred segment,
allowing a tracker to conclude that they share similar preferences.
2.2.2. Privacy risk channel 1: Exposure to experimental output. Summersetal.(2016)
find that consumers react negatively when targeted messages use sensitive or unexpected
personal information. Kim et al. (2018) demonstrate that personalization can increase effec-
tiveness while also raising privacy concerns when consumers infer that firms possess or use
personal information. Lin (2022) documents that consumers value the economic benefits of
targetedadvertising,whilealsoexhibitingabaselineresistancetobeingtargetedthatreflects

9
privacy concerns. Jerath and Miller (2024) argue that privacy concerns may arise from the
perceived inferences embedded in targeted marketing actions.
Inresponsetotheseprivacyconcerns,Ponteetal.(2026)usedifferentialprivacytoquantify
and control privacy risk from targeting consumers with a one-time discount coupon. In
contrast, we incorporate differential privacy directly into the experimental design rather
than applying privacy protection only after data have been collected. As customers enter the
experiment, we optimally balance exploration and exploitation subject to a specified privacy
budget. We also expand this privacy-minded way of experimentation to optimize privacy
protection to the firm-level portfolio of experiments.
2.2.3. Privacy risk channel 2: Post-exposure behavior. A stream of work studies how
firmscansharedatacontainingcustomerbehaviorwhilelimitingprivacyrisk.AnandandLee
(2023) propose sharing a generative model instead of customer data sets, allowing external
parties to learn useful patterns without directly accessing sensitive data. Ponte et al. (2024)
propose a differentially private data-sharing framework to quantify and control privacy risk
in marketing applications. Tian et al. (2026) show that fusing anonymous customer survey
data with CRM records can create reidentification risk; they propose a differentially private
data-fusion framework to reduce this risk. We differ from this work as we intervene during
the experimentation process and integrate privacy protection in the experimental design.
Prior computer science research uses differential privacy to protect the information that
MABs obtain from consumer responses rather than exposure to experimental outputs. Typ-
ically, these methods add noise to measures such as total clicks before using them to choose
which option to display. For example, Mishra and Thakurta (2015) develop a differentially
private MAB algorithm in which the reward statistics are privatized. Tossou and Dimi-
trakakis (2015) propose differentially private UCB-style algorithms that compute private

10
empirical mean rewards using noisy cumulative reward sums. Our paper is closest to Ren
etal.(2020),whousearandomizedresponsemechanismtoprotectrewards.Weinsteadapply
a randomized response mechanism to the experimental output, limiting what experimental
| outputs        | reveal about | the | consumer’s | latent | segment.        |        |
| -------------- | ------------ | --- | ---------- | ------ | --------------- | ------ |
| 3. Quantifying |              | the | privacy    | risk   | of experimental | output |
In this section, we develop a method that quantifies and integrates the privacy risk visitors
face during online experimentation. For example, a firm, such as Barnes & Noble, conducts
experiments on its website to identify the experimental output that is most effective for each
consumer segment, where segments reflect visitors’ interests and preferences. Our goal is to
bound what a third-party tracker could infer about visitors’ segment membership from their
| exposure | to an experimental |     | output. |     |     |     |
| -------- | ------------------ | --- | ------- | --- | --- | --- |
Our method blends the ε-greedy policy used in MAB experimentation with differential
privacy to protect experimental output. We rely on these techniques because we can link the
exploration probability used in the ε-greedy policy to satisfy ξ-differential privacy (Dwork
and Roth 2014). This yields a direct mapping between the privacy risk parameter ξ and
the exploration parameter ε. Building on this mapping, we introduce an experiment-level
privacy budget γ that a firm can set ex ante and study how different strategies for spending
| this budget          | affect | the performance |      | of experimentation. |     |     |
| -------------------- | ------ | --------------- | ---- | ------------------- | --- | --- |
| 3.1. Experimentation |        | via             | MABs |                     |     |     |
| 2S                   |        |                 |      |                     | S   |     |
Let S denote the segment of visitor t, where is a finite set of consumer segments.
t
We assume that the firm observes S before assigning an experimental output, for example
t
through its first-party customer information, whereas the third-party tracker whose inference
| we seek | to limit | does not | directly | observe | S . |     |
| ------- | -------- | -------- | -------- | ------- | --- | --- |
t

11
|     |     |     |     |     |     | A   | fa g, |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
The experiment contains a common set of K arms, = ,...,a where an arm is
1 K
an experimental output that can be displayed during experimentation, such as a book rec-
ommendation or an ad. We assume that every arm in A can, in principle, be displayed to
S.
every segment in Thus, the firm does not determine ex ante which arm is optimal for
a given segment. Instead, experimentation is used to learn which output performs best for
each segment.
Let A 2A denote the arm displayed to visitor t. A success is defined as a click on the
t
displayed arm. We allow the expected reward of an arm to vary across consumer segments.
Specifically, conditional on displaying arm a to a visitor in segment s, the reward satisfies
k
|     |     |     | R jfA | =a ,S =sg(cid:24)Bernoulli(µ |     |     | (s)), | (1) |
| --- | --- | --- | ----- | ---------------------------- | --- | --- | ----- | --- |
|     |     |     | t t   | k t                          |     |     | k     |     |
where
|     |     |     | µ (s)=P(R | =1jA |     | =a ,S | =s). |     |
| --- | --- | --- | --------- | ---- | --- | ----- | ---- | --- |
|     |     |     | k         | t    | t   | k     | t    |     |
The parameters µ (s) are unknown to the firm and are learned during experimentation.
k
Importantly,wedonotassumeexantethatdifferentsegmentsnecessarilyresponddifferently
to the same arm. The model merely allows µ (s) to differ across segments, and experimen-
k
| tation   | reveals whether | and | how such | heterogeneity |     | arises. |     |     |
| -------- | --------------- | --- | -------- | ------------- | --- | ------- | --- | --- |
| For each | arm–segment     |     | pair (a  | ,s), let      |     |         |     |     |
k
Xt−1
|     |     |     |      | 1fS  |     |     | g   |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- |
|     |     |     | N (a | ,s)= | =s, | A   | =a  |     |
|     |     |     | t    | k    | u   | u   | k   |     |
u=1
denote the number of previous visitors in segment s who were displayed arm a . The firm’s
k
| estimated | reward | for that | arm–segment | pair | is  |     |     |     |
| --------- | ------ | -------- | ----------- | ---- | --- | --- | --- | --- |
P
|     |     |     |           | t−1 1fS |     |     | gR    |     |
| --- | --- | --- | --------- | ------- | --- | --- | ----- | --- |
|     |     |     |           |         | =s, | A   | =a    |     |
|     |     |     | Q (a ,s)= | u=1     | u   | u   | k u , | (2) |
|     |     |     | t k       |         |     |     |       |     |
N (a ,s)
t k
| whenever | N (a ,s)>0. |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
t k

12
Accordingly, Q (a ,s) is the empirical click-through rate of arm a among previously
|     | t   | k   |     | k   |     |
| --- | --- | --- | --- | --- | --- |
observed visitors in segment s. Because the firm maintains a separate estimate for each
arm–segment pair, the same arm may acquire different estimated rewards across segments
| as experimentation |     | progresses. |     |     |     |
| ------------------ | --- | ----------- | --- | --- | --- |
2 A 2 S,
We maintain stationarity within each arm–segment pair: for every a and s
k
the mean reward µ (s) remains fixed over the experimental horizon. Conditional on the
k
displayedarmandsegment,rewardsareindependentdrawsfromthecorrespondingBernoulli
distribution.
The time horizon T denotes the total number of visitors allocated to the experiment.
The objective is to learn which arm maximizes expected reward for each segment while
| maximizing | cumulative | rewards | over the experimental | horizon. |     |
| ---------- | ---------- | ------- | --------------------- | -------- | --- |
3.1.1. The ε-greedy policy. The ε-greedy policy is a stochastic, near-optimal heuristic
for solving the MAB problem and is widely used in both industry and academia (e.g., Wang
| et al. 2025, | Optimizely | 2026).3 | A myopic, greedy | policy selects |     |
| ------------ | ---------- | ------- | ---------------- | -------------- | --- |
|              |            |         | a =argmaxQ       | (a ,S ),       | (3) |
|              |            |         | t                | t k t          |     |
a ∈A
k
Thus, the greedy arm depends on the segment of the current visitor through the segment-
specific reward estimates Q (a ,S ). Two visitors belonging to different segments may there-
|     |     | t   | k t |     |     |
| --- | --- | --- | --- | --- | --- |
fore have different greedy arms even when they arrive at the same stage of the experiment.
3Gittins and Jones (1979) proposed an index policy to solve this K-dimensional dynamic program that finds the
optimal path to maximize expected rewards. The optimal path is deterministic; at every visitor t, an arm-specific
index GI is computed, and the arm with the highest index is chosen. The policy is optimal for infinite horizon
tk
problems,anditwasshowntobenearoptimalforfinite-horizonproblems.BecauseGittinsindexisdeterministic,it
is not privacy preserving. When in exploitation, visitors belonging to a segment will have the same arm assignment
| revealing their | preferences | and interests. |     |     |     |
| --------------- | ----------- | -------------- | --- | --- | --- |

13
To encourage exploration of alternative arms, a ε-greedy policy explores with probability
a∗,
ε and exploits with probability 1(cid:0)ε. The arm served at customer t, is
t
8
> >
>
|     |     | > <a =argmaxQ |     | (a ,S | ), with probability | 1(cid:0)ε | ,   |     |
| --- | --- | ------------- | --- | ----- | ------------------- | --------- | --- | --- |
|     |     | t             |     | t k t |                     |           | t   |     |
a ∈A
|     |     | ∗     | k   |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     | a   | =     |     |     |     |     |     | (4) |
|     |     | t > > |     |     |     |     |     |     |
>
>
|     |     | : Uniform(A), |     |     | with probability | ε   | .   |     |
| --- | --- | ------------- | --- | --- | ---------------- | --- | --- | --- |
t
Importantly, exploitation is segment-sensitive because it uses Q (a ,S ), whereas explo-
|     |     |     |     |     |     | t   | k t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
A
ration draws from the same experiment-wide arm space for every segment. Note that the
firm does not specify which output belongs to a particular segment ex ante. Rather, differ-
ences in assignment across segments arise endogenously as the experiment learns segment-
| specific arm | effectiveness. |     |     |     |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
To evaluate how well the ε-greedy policy solves the MAB problem, we next analyze the
| regret generated | by  | its exploration | and | exploitation | decisions. |     |     |     |
| ---------------- | --- | --------------- | --- | ------------ | ---------- | --- | --- | --- |
3.1.2. Theexpectedregretoftheε-greedypolicy. Intuitively,solvingtheMABproblem
with the ε-greedy policy implies minimizing the regret of making mistakes. To minimize
regret, Panageas et al. (2020) show that we can set the per-round exploration probability at:
|     |     |     |     | (cid:18) | (cid:19) |     |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
1/3
Klogt
|     |     |     | ε   | =   | ,   |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
t
which yields the following bound on the expected cumulative regret
|     |     |     |     | (cid:0) |     | (cid:1) |     |     |
| --- | --- | --- | --- | ------- | --- | ------- | --- | --- |
E[R(T)]=O
|     |     |     |     | T2/3K1/3(logT)1/3 |     | .   |     | (6) |
| --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
Equation (5) implies a higher exploration probability early on, to learn about the effec-
tiveness of the arms, and higher exploitation later on, to maximize rewards by sampling the
best-performing arms. Deviating from the above level of exploration to ensure a certain level
of privacy increases regret, and decreases the performance of the experiment. We next link
| the ε-greedy | policy | to differential | privacy. |     |     |     |     |     |
| ------------ | ------ | --------------- | -------- | --- | --- | --- | --- | --- |

14
| 3.2. Linking | the ε-greedy | policy | to differential | privacy |     |
| ------------ | ------------ | ------ | --------------- | ------- | --- |
First, we define the privacy risk under differential privacy. We then connect it to experimen-
tation using the ε-greedy policy. Last, we define the visitor-level privacy risk ξ.
3.2.1. The privacy mechanism: differential privacy. AsdefinedinEquation(3),a isthe
t
greedy arm, the arm that myopically maximizes rewards up to visitor t, and a∗ denotes the
t
arm displayed after randomization through the ε-greedy policy. Following Equation (4), we
| P(a∗=kja |     |     | 2f1,...,Kg, |     |     |
| -------- | --- | --- | ----------- | --- | --- |
define =j)=p , where k,j as the probability that the displayed
| t             | t          | kj        |     |     |     |
| ------------- | ---------- | --------- | --- | --- | --- |
| arm is k when | the greedy | arm is j. |     |     |     |
A privacy mechanism introduces randomization in arm assignment and masks optimal
assignment maximizing rewards, i.e., the greedy arm. In our setup, the privacy mechanism
| is represented | by a K(cid:2)K | stochastic | matrix |                           |     |
| -------------- | -------------- | ---------- | ------ | ------------------------- | --- |
|                |                |            | 0      | 1                         |     |
|                |                |            | Bp p   | (cid:1)(cid:1)(cid:1) p C |     |
|                |                |            | 11 12  | 1K                        |     |
|                |                |            | B      | C                         |     |
|                |                |            | B      | C                         |     |
|                |                |            | B Bp p | (cid:1)(cid:1)(cid:1) p C |     |
|                |                |            | 21 22  | 2K C                      |     |
|                |                | P=B        |        | C,                        |     |
(7)
|     |     |     | B . . | . C                     |     |
| --- | --- | --- | ----- | ----------------------- | --- |
|     |     |     | B . . | ... . C                 |     |
|     |     |     | . .   | .                       |     |
|     |     |     | B     | C                       |     |
|     |     |     | @     | A                       |     |
|     |     |     | p p   | (cid:1)(cid:1)(cid:1) p |     |
|     |     |     | K1 K2 | KK                      |     |
where each column corresponds to a greedy arm j, each row corresponds to a displayed
P
arm k, and p (cid:21)0 and K p =1 for every j 2f1,...,Kg. Thus, column j gives the
|     | kj  | kj  |     |     |     |
| --- | --- | --- | --- | --- | --- |
k=1
full distribution of displayed arms conditional on the greedy arm being j. In particular, the
diagonal entry p is the probability that arm j is displayed when arm j is also the greedy
jj
withk6=j
arm,whileanoff-diagonalentryp istheprobabilitythatthemechanismdisplays
kj
| arm k instead | of the greedy | arm j. |     |     |     |
| ------------- | ------------- | ------ | --- | --- | --- |
To guarantee a privacy level ξ under differential privacy, Wang et al. (2016) define the
K-ary randomized-response mechanism in Equation (7) and set each diagonal entry of the
| stochastic | matrix to |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |
eξ
2f1,...,Kg,
|     |     | p = | ,   | j   | (8) |
| --- | --- | --- | --- | --- | --- |
jj K(cid:0)1+eξ

15
| and each | off-diagonal | entry |     | is set | to  |     |     |     |     |     |
| -------- | ------------ | ----- | --- | ------ | --- | --- | --- | --- | --- | --- |
1
k6=j.
|     |     |     |     | p   | =            |     | ,   |     |     | (9) |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
|     |     |     |     | kj  | K(cid:0)1+eξ |     |     |     |     |     |
This choice of diagonal and off-diagonal entries ensures that, for any displayed arm k and
|     |     |     |     | a′, |     |     |     |     | eξ. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
any two underlying arms a and the ratio of output probabilities is bounded by Hence,
ξ directly determines how much observing the displayed arm can reveal about the underlying
greedy arm (see Web Appendix B). The privacy mechanism under differential privacy is
| therefore | represented | by  |     |           |     |        |     |                       |     |     |
| --------- | ----------- | --- | --- | --------- | --- | ------ | --- | --------------------- | --- | --- |
|           |             |     |     | 0         |     |        |     |                       | 1   |     |
|           |             |     |     |           | eξ  |        | 1   | (cid:1)(cid:1)(cid:1) | 1   |     |
|           |             |     |     | B         |     |        |     |                       | C   |     |
|           |             |     |     | BK−1+eξ   |     | K−1+eξ |     | K−1+eξC               |     |     |
|           |             |     |     | B         |     |        |     |                       | C   |     |
|           |             |     |     | B         |     |        | eξ  |                       | C   |     |
|           |             |     |     | B         | 1   |        |     | (cid:1)(cid:1)(cid:1) | 1 C |     |
|           |             |     |     | P=BK−1+eξ |     | K−1+eξ |     | K−1+eξC.              |     |     |
(10)
|     |     |     |     | B   |     |     |     |     | C   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | .   |     | .   | ... | .   |     |
|     |     |     |     | B   | .   |     | .   |     | . C |     |
|     |     |     |     | B   | .   |     | .   |     | . C |     |
|     |     |     |     | @   |     |     |     |     | A   |     |
eξ
|     |     |     |     |     | 1      |        | 1   | (cid:1)(cid:1)(cid:1) |     |     |
| --- | --- | --- | --- | --- | ------ | ------ | --- | --------------------- | --- | --- |
|     |     |     |     |     | K−1+eξ | K−1+eξ |     | K−1+eξ                |     |     |
3.2.2. A visitor-level privacy risk ξ. We now connect the exploration parameter ε in the
ε-greedy policy to the differential-privacy parameter ξ by matching the induced stochastic
matrix to the K-ary randomized-response mechanism. Under Equation (4), if the greedy
arm at round t is a =j, then the probability that the displayed arm equals the greedy arm
t
is
ε
|     |     |     | p   | =P(a | ∗ =kja |     | =k)=(1(cid:0)ε)+ |     | ,   | (11) |
| --- | --- | --- | --- | ---- | ------ | --- | ---------------- | --- | --- | ---- |
|     |     |     |     | jj   |        | t   |                  |     |     |      |
|     |     |     |     |      | t      |     |                  |     | K   |      |
1(cid:0)ε
where with probability the mechanism exploits and displays the greedy arm, while with
| probability | ε it explores |     | uniformly |     | over | all K | arms. |     |     |     |
| ----------- | ------------- | --- | --------- | --- | ---- | ----- | ----- | --- | --- | --- |
Under uniform exploration, each arm is selected with probability 1/K, so the greedy
arm is still displayed with probability ε/K. This uniform randomization implies an equal

16
arms.4
exploration probability across Using Equation (8), we solve Equation (11) for ε to
| yield the | exploration | probability |     |     |             |     |     |     |     |
| --------- | ----------- | ----------- | --- | --- | ----------- | --- | --- | --- | --- |
|           |             |             |     |     | K(1(cid:0)p | )   |     |     |     |
jj
ε=
K(cid:0)1
|     |     |     |     |     | (cid:16) | (cid:17) |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
1(cid:0) eξ
K
K−1+eξ (12)
=
K(cid:0)1
K
|     |     |     |     | =   |     | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
K(cid:0)1+eξ
Equation (12) shows that stronger privacy guarantees (smaller ξ) require more exploration
(largerε),whereasweakerprivacyguarantees(largerξ)permitmoreexploitation(smallerε).
In particular, when ξ=0, then ε=1 and the displayed arm is fully randomized; as ξ!1,
ε!0
| then | and | the policy | approaches | pure | exploitation. |     |     |     |     |
| ---- | --- | ---------- | ---------- | ---- | ------------- | --- | --- | --- | --- |
Using the connection between the privacy risk defined under differential privacy and the
exploration probability of the ε-greedy policy, we combine Equation (12) and Equation (4)
| to define | a ξ-differentially |     | private | ε-greedy | policy | as: |     |     |     |
| --------- | ------------------ | --- | ------- | -------- | ------ | --- | --- | --- | --- |
8
>
> >
|     |     | <   |         |       |      |             | 1(cid:0)ε= | eξ−1   |     |
| --- | --- | --- | ------- | ----- | ---- | ----------- | ---------- | ------ | --- |
|     |     | a   | =argmax | Q (a) | with | probability |            |        | ,   |
|     |     |     | t       | a t   |      |             |            | K+eξ−1 |     |
a ∗ = (13)
|     |     | t > > |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
>
|     |     | : Uniform(f1,...,Kg) |     |     | with | probability | ε=  | K   | .   |
| --- | --- | -------------------- | --- | --- | ---- | ----------- | --- | --- | --- |
K+eξ−1
This implies that the bandit explores with probability ε= K and exploits with prob-
K+eξ−1
ability 1(cid:0)ε = eξ−1 . For example, if we set ξ = 0.05 and consider two arms, then the
K+eξ−1
1(cid:0).975=.025.
exploration probability equals .975 and the exploitation probability equals
Intuitively, less privacy risk implies more randomness and more randomness implies more
exploration.
4In Web Appendix J, we relax this restriction by allowing the exploration probabilities to differ across arms, which
induces arm-specific privacy risk parameters. This extension allows firms to assign stronger privacy protection to
more sensitive arms. We show that such heterogeneity increases the worst-case regret bound relative to an equal
| privacy guarantee | across | arms | and quantify | the magnitude |     | of this increase. |     |     |     |
| ----------------- | ------ | ---- | ------------ | ------------- | --- | ----------------- | --- | --- | --- |

17
InFigure3,weprovideaninterpretationoftheprivacyriskparameterξ.Underdifferential
privacy, the parameter ξ bounds the extent to which a tracker can update their belief about
a visitor’ segment membership from exposure to experimental output, without accounting
for their interaction with the experimental output. The horizontal axis in Figure 3 represents
a tracker’s prior belief about a visitor’s segment, while the vertical axis shows the range of
posterior beliefs after observing the output. The diagonal line corresponds to perfect privacy,
where the posterior equals the prior—no inference about segment membership is possible.
1.00
0.75 Smaller privacy budget (darker):
posterior stays close to prior
0.50
Jamie: xi = 1
Posterior <= 0.40
Jamie: xi = 0.05
0.25 Larger privacy budget (lighter):
Posterior <= 0.21
posterior can shift more
0.00
0.00 0.25 0.50 0.75 1.00
Third party’s prior belief about a visitor’s segment
feileb
roiretsop
elbissop
s’ytrap
drihT
lower upper gamma 5 3 1 0.5 0.05
Figure3 The privacy risk parameter ξ bounds how much a tracker’s belief about a visitor’s segment can shift
after observing the experimental output. Note: Darker curves (small ξ) show less updating, and lighter
curves (larger ξ) show more updating away from the prior.
For small values of ξ (darker curves), the posterior remains close to the prior: returning
to our Barnes & Noble example from the introduction, even after the tracker observes the

18
recommendation shown to Jamie, it cannot tell whether a fantasy-themed recommendation
was displayed because Jamie is truly a fantasy reader or simply because of randomization.
This is illustrated by the lower red point in Figure 3: starting from a prior belief of 20%, a
privacy level of ξ =.05 bounds the posterior after one observed display at about 21%. For
larger ξ (lighter curves), the posterior can move further away from the prior, meaning that
the observed output is more informative about Jamie’s underlying type; the upper red point
shows that with ξ=1 the posterior can increase to about 40% after observing the output.
3.2.3. An experiment-level privacy budget γ. Wehavenowdefinedaper-visitorprivacy
risk level ξ incurred during online experimentation from experimental output. However, it
remains unclear how a firm should allocate privacy risk across visitors. To address this, we
introduce an experimental-level privacy budget γ that can be set before experimentation.
We assume that each round corresponds to a unique visitor, and the privacy mechanism in
round t is independently applied only to that visitor’s assignment (see Web Appendix C for
technical details). This implies that the privacy budget is governed by the largest per-visitor
privacy risk:
γ=maxξ . (14)
t
t
Thus,theexperimentsatisfiesthebudgetγ aslongasξ (cid:20)γ foreveryvisitort.Thisdefinition
t
places an upper bound on visitor-level privacy risk but leaves open how privacy risk should
be allocated across visitors. We address this question by introducing two privacy budget
spending strategies.
3.3. Privacy budget spending strategies and the trade-off between privacy and
performance
Having established an experimental-level privacy budget, it remains unclear how this budget
should be spent across visitors. We develop two strategies that define how to spend the

19
experiment-level privacy budget across visitors: a constant privacy risk strategy, keeping the
risk constant across visitors, and a dynamic privacy risk strategy, which allows the risk to
| change across | visitors | up to a predefined | level. |     |     |
| ------------- | -------- | ------------------ | ------ | --- | --- |
3.3.1. Constant privacy risk strategy. The constant privacy risk strategy assigns the
same risk to each visitor, such that ξ =γ for all t. We visualize the strategy in Figure 4.
t
The constant strategy has the benefit of simplicity and fairness: all visitors receive the same
level of privacy risk (see Figure 4, left panel). The main drawback is that the strategy limits
the potential rewards from experimentation because exploration is especially valuable early
in the experiment, when additional information can substantially improve future decisions,
whereas exploitation is more valuable later, once the firm has learned which arms perform
best. Our regret analysis in §3.1.2 and Web Appendix ?? highlight this adaptive feature of
| the ε-greedy | policy. |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- |
Privacy Risk (ξ) Probability of Exploitation Probability of Exploration
t
1.00
| 5                         |     | 1.00 |                             |      |     |
| ------------------------- | --- | ---- | --------------------------- | ---- | --- |
| 4                         |     |      | Increasing the privacy risk |      |     |
| Privacy risk remains      |     | 0.75 |                             | 0.75 |     |
| constant across visitors. |     |      | increases exploitation      |      |     |
which may cause the strategy
to get stuck in a suboptimal arm.
3
|     |     | 0.50 |     | 0.50 |     |
| --- | --- | ---- | --- | ---- | --- |
2
Reducing the privacy risk
|     |     |      |     | 0.25 | increases exploration,       |
| --- | --- | ---- | --- | ---- | ---------------------------- |
|     |     | 0.25 |     |      | which may cause the strategy |
1
to select arms randomly.
| 0   |     | 0.00 |     | 0.00 |     |
| --- | --- | ---- | --- | ---- | --- |
100 1K 10K100K1M10M100M 100 1K 10K100K1M10M100M 100 1K 10K100K1M10M100M
Number of customers, shown by powers of 10 (base−10 log scale)
|     | Privacy risk budget |     | 0.05 0.5 | 1 3 | 5   |
| --- | ------------------- | --- | -------- | --- | --- |
Figure4 Theprivacyriskundertheconstantstrategyξ (leftpanel)andtheexploration/exploitationprobabilities
t
ε and 1−ε (middle/right panel) for different privacy budgets γ∈{0.05,0.5,1,3,5}.
t t

20
The constant strategy has same privacy risk, therefore the same exploration probability
throughout the experiment (middle and right panels), and it cannot adjust to this shift:
it may explore too little early on, when learning is most valuable, and too much later on,
when the best-performing arms have already become clearer. The expected regret reflects the
inflexibility of the constant strategy. By replacing the exploration probability from Equa-
tion (12) into Equation (15), the regret bound of the constant strategy becomes (see Web
Appendix H)
p p
K
E[R (T)] (cid:20) T + K+eγ(cid:0)1 T logT .
constant K+eγ(cid:0)1 | {z } (15)
| {z }
costofexploitation
costofexploration
Intuitively, the exploration term T k grows linearly with the number of visitors
k+eγ−1
because, in every round, the bandit explores with constant probability k and a random
k+eγ−1
p p
pull can incur up to one unit of regret. The second term, k+eγ(cid:0)1 T logT, captures
exploitation mistakes due to noisy value estimates. A smaller privacy budget γ decreases
the exploitation probability, which decreases the cost from uncertainty during learning, but
also increases the exploration probability, which raises the exploration cost. This is the core
exploration–exploitation trade-off in online experimentation under privacy protection. To
incorporate this idea, we next vary privacy risk across visitors so that exploration is concen-
trated earlier in the experiment and exploitation later.
3.3.2. Dynamic privacy risk strategy. We next derive a dynamic privacy risk schedule
that varies risk across visitors to better balance exploration and exploitation than the con-
stant strategy and gets closer to the expected regret bound of the ε-greedy policy without
privacy protection (see Equation 6). Under this dynamic strategy, the privacy risk assigned
to visitor t is given by (see Web Appendix D.2):

21
|     |     |     |                   | 0   |          | 1           |     |      |
| --- | --- | --- | ----------------- | --- | -------- | ----------- | --- | ---- |
|     |     |     |                   | B   | K        | C           |     |      |
|     |     |     | ξ =log@1(cid:0)K+ |     | (cid:16) | (cid:17) A. |     | (16) |
t
1/3
Klog(t)
t
Under this schedule, the firm can protect visitors’ privacy without degrading learning per-
formance relative to an ε-greedy policy without privacy protection. However, to ensure that
privacy risk never exceeds the predetermined budget γ in Equation (14), we cap the per-
| visitor privacy | risk | as follows: |     |     |     |      |     |     |
| --------------- | ---- | ----------- | --- | --- | --- | ---- | --- | --- |
|                 |      |             | 8   | 0   | 0   | 119  |     |     |
|                 |      |             | >   |     |     |      | >   |     |
|                 |      |             | <   |     |     |      | =   |     |
|                 |      |             |     | B   | B   | K CC |     |     |
log@1(cid:0)K+@(cid:16)
|     |     | ξ = | min γ, |     |         | (cid:17) AA | .   | (17) |
| --- | --- | --- | ------ | --- | ------- | ----------- | --- | ---- |
|     |     | t   | >      |     |         | 1/3         | >   |      |
|     |     |     | :      |     | Klog(t) |             | ;   |      |
t
This cap implies that once the budget binds, the exploration and exploitation probabilities
are fixed, and the privacy risk ξ remains set at γ, ensuring that the experiment-wide privacy
t
guarantee is preserved. The cap effectively binds the extent of exploitation the bandit can
engage in, and ensures that even after many visitors the bandit still explores and randomizes
| assignment, | thus | allowing | plausible | deniability. |     |     |     |     |
| ----------- | ---- | -------- | --------- | ------------ | --- | --- | --- | --- |
In Figure 5, we visualize the privacy risk (left panel), the probability of exploitation
(middle panel), and the probability of exploration (right panel) under the dynamic privacy
risk strategy. Early visitors face lower privacy risk as the bandit explore more, while later
visitors face higher privacy risk, as the bandit exploits more frequently. When ξ >γ, the
t
privacy risk and induced exploration and exploitation probabilities are constant.
The introduction of the budget cap in Equation (17) creates an additional regret com-
ponent relative to the standard ε-greedy bound: once the cap takes effect, the strategy is
forced to randomize more than the uncapped schedule would prescribe late in the experi-
ment, which increases regret. This strategy yields the following expected regret bound (see

22
Privacy Risk (ξ) Probability of Exploitation Probability of Exploration
t
| 5   |     |     | 1.00 | We exploit |     |     |     |     |
| --- | --- | --- | ---- | ---------- | --- | --- | --- | --- |
1.00
|     | Early visitors face |     |     | only after |     |     |     |     |
| --- | ------------------- | --- | --- | ---------- | --- | --- | --- | --- |
gathering sufficient
lower privacy risk
|     | than later visitors. |     |                      |  information |     |     |     |     |
| --- | -------------------- | --- | -------------------- | ------------ | --- | --- | --- | --- |
| 4   |                      |     | through exploration. |              |     |     |     |     |
0.75
0.75
3
0.50
0.50
The privacy risk reaches
2
the set budget,
then stays constant.
0.25
0.25
| 1   |     |     |     |     |     | We explore early |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
to obtain sufficient
information to
exploit effectively.
| 0   |     |     | 0.00 |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
0.00
100 1K 10K100K1M10M100M 100 1K 10K100K1M10M100M 100 1K 10K100K1M10M100M
Number of customers, shown by powers of 10 (base−10 log scale)
|     |     | Privacy risk budget |     | 0.05 | 0.5 1 3 | 5   |     |     |
| --- | --- | ------------------- | --- | ---- | ------- | --- | --- | --- |
Figure5 Theprivacyriskunderthedynamicstrategyξ (leftpanel)andtheexploitation/explorationprobabilities
t
1−ε and ε (middle/right panel). We use different line types to show the varying the privacy budget
|     |     | t t |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ∈{0.05,0.5,1,3,5}.
levels
| Web Appendix |        | G for a derivation): |     |      |     |     |     |     |
| ------------ | ------ | -------------------- | --- | ---- | --- | --- | --- | --- |
| E[R          | (T)]   | ≲ t2/3K1/3(logt      |     | )1/3 |     |     |     |     |
|              | budget |                      |     | γ    |     |     |     |     |
|              |        | |γ                   | {z  | }    |     |     |     |     |
standardε-greedyregret(seeEquation6)
|     |     |     |     |     | p   | p p | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
K
|     |     |     | (cid:0)t       |     | K+eγ(cid:0)1( | (cid:0) |          |     |
| --- | --- | --- | -------------- | --- | ------------- | ------- | -------- | --- |
|     |     | +   | (T )           |     | +             | T       | t ) logT | .   |
|     |     |     | γ K+eγ(cid:0)1 |     | |             | {z      | γ        | }   |
|     |     |     | | {z           | }   |               |         |          |     |
costofnoisyexploitationafterbudgetrunsout
costofexplorationafterbudgetrunsout
(18)
where t is the visitor where the privacy risk ξ =γ, defined as the first visitor at which the
|     | γ   |     |     |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
dynamic exploration rate (see Equation 16) falls to the level implied by the privacy budget
| γ (see | the left | panel in Figure | 5).5 |     |     |     |     |     |
| ------ | -------- | --------------- | ---- | --- | --- | --- | --- | --- |
5Determiningt
γ hasnoclosed-formsolutionbutitisstraightforwardtocomputenumerically(seeWebAppendixG).
|     |     | {   |     | }   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
( )
|           |         | t∈{1,...,T}: | 1/3≤  |        |     |     |     |     |
| --------- | ------- | ------------ | ----- | ------ | --- | --- | --- | --- |
| Formally, | t :=min |              | klogt | k .    |     |     |     |     |
|           | γ       |              | t     | k+eγ−1 |     |     |     |     |

23
If t (cid:21)T, the privacy budget never binds over the experimental horizon, and the regret
γ
therefore reduces to the standard ε-greedy regret without privacy protection. By contrast,
if t <T, the budget binds before the experiment ends. From that point onward, the strat-
γ
egy is forced to maintain more randomization than the uncapped dynamic schedule would
prescribe, which generates the two additional terms in the regret bound. These terms there-
fore capture the extra regret incurred after exhaustion, and their magnitude depends on the
remaining horizon T (cid:0)t : the earlier the budget binds, the larger the resulting regret penalty.
γ
Having introduced the two strategies, we next apply them to two marketing applications.
4. Two applications of the privacy risk strategies
In this section, we apply the strategies to two experiments: an experiment on website design,
and one involving a recommendation system for an online fashion retailer. In both appli-
cations, CTRs from a randomized control trial (RCT) are available, and we can use these
CTRs to perform empirically-grounded simulations that test the effectiveness of our method
against several benchmarks.
We study these applications because the experimental output may reveal the visitor’s
segment. In the recommendation-system application, the displayed fashion items may signal
inferred product interests or broader demographic segments (Castelluccia et al. 2012, Xin
et al. 2023, Chen et al. 2026). In the website-design application, assignment different website
designs may signal the firm’s inference about the visitor’s stage in the purchase journey
(Hauser et al. 2009, Liberali and Ferecatu 2022).
4.1. Website design
Liberali and Ferecatu (2022) report the results of a web design RCT. The experiment was
conducted on the MBA website the Rotterdam School of Management (RSM), Erasmus
University. The goal was to test two versions of the website, with abstract vs. concrete

24
language, to maximize the total number of clicks on the call-to-action prompting visitors to
begin their MBA application.6
We set T=10,000, 100,000, and 1,000,000 visitors, as proxies for small, medium, and large
firms. We simulate the constant and dynamic spending strategies under privacy budgets
of γ 2 f.05,.5,1,3,5g. Assuming that a tracker initially believes that a visitor has a 20%
probability of segment membership, these budgets cap the posterior belief after observing
the experimental output at 20.8%, 29.2%, 40.5%, 83.4%, and 97.4%, respectively, ranging
from strong to weak privacy protection.
We benchmark their performance against four reference strategies: an ε-greedy policy
without privacy protection, the Gittins index policy equivalent to optimal learning, a per-
fect information strategy that assumes the firm knows which option has the highest CTR
and always selects the best arm, and a random strategy that chooses an arm at random.
To capture uncertainty, we bootstrap each strategy 1,000 times and visualize the resulting
uncertainty using 95% confidence intervals.
Figure 6 shows the total clicks (rewards) for each strategy across different firm sizes. As
expected, the perfect information strategy achieves the highest total clicks, followed by the
ε-greedy and Gittins index policies, while the random strategy performs worst. The figure
visualizes the empirical implications of our theory (see §3). The privacy budget γ sets the
exploration rate via Equation (12), so smaller γ implies more randomization and thus more
exploration, while larger γ allows more exploitation. When γ is very small (e.g., γ =0.05),
6Theabstractlanguagewebsiteusedbroader,exploratorylanguage(e.g.,“WhytheRSMMBA?Getthebrochure.”)
and terms such as Explore, Discover, and Participate in a conversation. In contrast, the concrete language version
employed more action-oriented phrasing (e.g., “Ready to start your application? Create an account.”) and concrete
terms such as “Join”, “Apply”, and “Tour (the campus).” The CTRs are .324 for the concrete version and .295 for
the abstract version of the website.

25
the exploration rate is high and both the constant and dynamic strategies behave close to
randomassignment.Asγ increases,andprivacyprotectiondecreases,bothstrategiesimprove
because the bandit is allowed to exploit more often, shifting probability mass toward the
| higher-performing | arm. |     |     |     |     |
| ----------------- | ---- | --- | --- | --- | --- |
Figure6 Website design application — Total clicks as a function of different strategies.
|     | T = 1e4 |       | T = 1e05 |     | T = 1e6 |
| --- | ------- | ----- | -------- | --- | ------- |
|     | k = 2   |       | k = 2    |     | k = 2   |
| 325 |         | 3,250 |          |     |         |
32,400
skcilc latoT
| 320 |     | 3,200 |     | 32,000 |     |
| --- | --- | ----- | --- | ------ | --- |
315
|     |     | 3,150 |     | 31,600 |     |
| --- | --- | ----- | --- | ------ | --- |
| 310 |     |       |     | 31,200 |     |
0.05 0.5 1 3 5 Other 0.05 0.5 1 3 5 Other 0.05 0.5 1 3 5 Other
Privacy budget γ
ε−greedy
|     |     | Constant |     | Perfect info |     |
| --- | --- | -------- | --- | ------------ | --- |
Strategy
|     |     | Dynamic | Gittins index | Random |     |
| --- | --- | ------- | ------------- | ------ | --- |
Note. The“Other”categoryonthex-axisincludestheoptimalstrategies—theGittinsindexandε-greedypolicies—
and the theoretical lower and upper bounds represented by random and perfect information, respectively.
The differences in performance between the two strategies align with the results of our
regret analysis (see Equations 15 and 18). The dynamic strategy is designed to mimic the
“explore early, exploit later” pattern of classic ε-greedy, so it benefits most when γ is large
enough that the cap binds only late (or not at all). In that region, further increases in γ relax
a constraint that is already slack, so the dynamic strategy exhibits diminishing returns and
effectively hits a performance ceiling at high γ. Consistent with Equation (18), the higher
the privacy risk γ, the longer the bandit can follow the non-private regret bound, and the
| higher the total | rewards. |     |     |     |     |
| ---------------- | -------- | --- | --- | --- | --- |
Bycontrast,whenimplementingtheconstantstrategy,thereappearstobeanidealbudget
level γ, where performance is maximized given this strategy. When γ is very small, the

26
exploration probability is close to one and the strategy behaves nearly at random. As γ
increases, randomization falls and clicks increase. However, when γ becomes too large, the
constant strategy explores too little in every round, so early noise can cause the bandit to
lock in to a suboptimal arm, reducing total clicks despite the higher budget. This mechanism
explains why the constant strategy can peak at an intermediate γ, whereas the dynamic
strategy improves until it reaches its ceiling.
These differences become more consequential as the experimental horizon increases. With
more visitors, the dynamic strategy has more opportunities to benefit from early learning
and subsequent exploitation, whereas the constant strategy may continue exploiting an arm
selected on the basis of noisy early estimates. Consequently, the performance advantage of
the dynamic strategy over the constant strategy becomes more pronounced as T increases.
For T =100,000 and T =1,000,000, the differences in mean performance between the two
strategies are statistically significant (see Figure 6).
In the next application, we examine the effectiveness of the constant and dynamic privacy
strategies in a more complex setting with multiple arms.
4.2. Recommendation system
We examine the robustness of the privacy risk strategies beyond a two-arm setting, and
in a different setup involving a recommender system. We use data from a seven-day field
experimentconductedbyZOZOTOWN,alargeJapanesefashione-commerceplatform(Saito
et al. 2020). For each visitor, ZOZOTOWN displayed three fashion item recommendations
selected uniformly at random, then recorded whether the visitor clicked on a recommended
item. In total, ZOZOTOWN recorded 1,374,327 visitors across 80 arms corresponding to
fashion items.7 This setting allows us to vary both the number of arms and the time horizon.
We consider K 2f2,4,8g and T 2f100,000, 1,000,000g in our simulations below.
7CTRvaluesrange from.0012 to.0078.Inour simulations,weuse theeighthighest-performingitems,whose CTRs
range from .0012 to .0053. CTRs in this application are approximately an order of magnitude lower than those in

27
InFigure7,weplottotalclicksonthey-axisacrossdifferentprivacybudgetsonthex-axis.
The column panels vary the number of visitors, whereas the row panels vary the number of
arms. The results are consistent with those of the previous application. Under the constant
strategy, performance initially improves as γ increases, then levels off and may decline at
higher values of γ. By contrast, the performance of the dynamic strategy increases with γ
and eventually plateaus at the optimal-performance benchmark for suﬀiciently large values
of γ.
Figure7 Recommendations — Total clicks as a function of different strategies.
T = 1e05 T = 1e05 T = 1e05
k = 2 k = 4 k = 8
270 500
260
265 450
260 400
240
255 350
250
300
220
245
T = 1e6 T = 1e6 T = 1e6
k = 2 k = 4 k = 8
2,700 2,700 5,000
2,600
2,650 4,500
2,500
2,600 4,000
2,400
2,550
3,500
2,300
2,500
3,000
2,200
2,450
0.05 0.5 1 3 5 Other 0.05 0.5 1 3 5 Other 0.05 0.5 1 3 5 Other
Privacy budget γ
skcilc
latoT
Constant ε−greedy Perfect info
Strategy
Dynamic Gittins index Random
Note. The “Other” category on the x-axis includes the benchmark policies—the Gittins-index policy and the non-
private ε-greedy policy—as well as the theoretical lower and upper bounds represented by random and perfect
information, respectively.
thewebsite-designapplication.Althoughtheselowsuccessratesaretypicalofthesettingandprovideaninformative
test of our method, we do not report simulations with T =10,000 visitors because the bandit does not have enough
observations to learn reliably at that sample size.

28
The results also highlight a difference from the website-design application. This mainly
impacts the constant privacy risk strategy. Figure 7 shows that the non-monotonic perfor-
mance pattern becomes less pronounced when the number of arms exceeds two, relative to
the pattern observed in the website design application. This occurs because the exploration
probability is determined not only by the privacy budget γ, but also by the number of arms
K (see Equation 12). For a fixed γ=3, increasing the number of arms from K =2 to 8 raises
the exploration probability from 10% to 30%. To achieve a similar number of total clicks as
K increases, we must set a larger privacy budget to allow for suﬀicient exploitation. As a
result, for K 2f4,8g, total clicks under the constant strategy generally increase with γ: a
higher γ mainly enables more exploitation while maintaining non-trivial exploration.
In the next section, we derive privacy risk elasticities of regret to capture the marginal
regret of stronger privacy protection. Whereas Figures 6 and 7 compare outcomes of a few
discrete values of γ, elasticities quantify how sensitive regret is to small changes in γ. This
allows us to identify regions of diminishing returns from increasing privacy risk and, when
they exist, regret-minimizing privacy budgets that balance the performance gains from addi-
tional learning against the costs of greater privacy risk.
5. Privacy risk elasticities of expected regret
To quantify the privacy–performance trade-off, we derive the elasticity of expected regret
with respect to the privacy budget γ for each strategy. The elasticity measures the per-
centage change in expected regret resulting from a one-percent change in γ. A negative
elasticity indicates that increasing the budget reduces regret, whereas a positive elasticity
indicates that it increases regret. A change from negative to positive identifies a regret-
minimizing budget. These elasticities extend our empirical findings by helping managers
identify regret-minimizing privacy budgets and assess where stronger privacy protection is
relatively inexpensive or costly in performance terms.

29
| 5.1. | The privacy | elasticity |     | of regret | for | the constant | strategy |     |     |     |
| ---- | ----------- | ---------- | --- | --------- | --- | ------------ | -------- | --- | --- | --- |
We derive the privacy elasticity of regret for the constant strategy in Web Appendix I.1.
Figure 8 plots this elasticity as a function of the privacy budget γ. The x-axis shows the
privacy budget γ and the y-axis shows the percentage change in expected regret resulting
2f2,5,20g
from a one-percent increase in γ. The panels vary the number of arms K and the
| line types | represent | different |     | numbers | of visitors | T.  |     |     |     |     |
| ---------- | --------- | --------- | --- | ------- | ----------- | --- | --- | --- | --- | --- |
Figure8 Privacy risk elasticity of regret as a function of the privacy budget γ, for different numbers of arms
|     | (K∈2,5,20) | and   | visitors | (T ∈10,000,100,000,1,000,000). |     |       |     |     |        |     |
| --- | ---------- | ----- | -------- | ------------------------------ | --- | ----- | --- | --- | ------ | --- |
|     |            | k = 2 |          |                                |     | k = 5 |     |     | k = 20 |     |
terger fo yticitsale ksir ycavirP 2
Positive elasticity
|     | (red area):   |     |     |     | For larger k, |     |     |                |     |     |
| --- | ------------- | --- | --- | --- | ------------- | --- | --- | -------------- | --- | --- |
|     | raising gamma |     |     |     |               |     |     | Larger samples |     |     |
the `ideal` point
|     | increases regret |     |     |                      |           |     |     | shift the `ideal`           |     |     |
| --- | ---------------- | --- | --- | -------------------- | --------- | --- | --- | --------------------------- | --- | --- |
| 1   |                  |     |     |                      | occurs at |     |     |                             |     |     |
|     |                  |     |     | higher gamma levels. |           |     |     | privacy−risk budgets upward |     |     |
0
Negative elasticity
(white area):
| −1  |     |     | raising gamma |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
decreases regret
| 0   | 1   | 2 3 | 4   | 5 0 | 1   | 2 3 | 4 5 | 0 1 | 2 3 | 4 5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Privacy risk budget (gamma)
|     |     |     | Number of visitors (T) |     |     | 1e4 | 1e5 | 1e6 |     |     |
| --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
Note. The elasticity is negative where relaxing privacy protection (increasing γ) reduces regret, and positive where
furtherincreasesinγ raiseregret.Thezero-crossingsmarkistheidealprivacybudgetsthatminimizeregretforeach
(k,T) combination.
Thesignoftheelasticityprovidesamanagerialdiagnosticofwheretheconstantstrategyis
“too random” versus “too greedy.” When the elasticity is negative, increasing γ (i.e., allowing
less randomization) reduces regret because the bandit can exploit more effectively. When
the elasticity becomes positive, further increases in γ increase regret because the constant
strategy explores too little and can lock in to a suboptimal arm (see the left panel in Figure

30
8). The point where the elasticity crosses zero therefore identifies an ideal privacy budget for
the constant strategy. We denote such ideal point by γ∗ for the constant strategy and
constant
γ∗ for the dynamic strategy.
dynamic
We observe that the value of γ∗ depends on both the number of visitors and the
constant
number of arms (see the middle and right panels in Figure 8): it shifts upward as either
T or K increases. Intuitively, these forces work in opposite directions. As the number of
visitors T increase, the bandit has more opportunities to learn, so it can afford to explore
less and exploit more as the experiment progresses. By contrast, as K increases, identifying
the best arm becomes more diﬀicult, which increases the need for exploration. However, for
any fixed γ, the exploration probability also increases mechanically with K (see Equation
12). The regret-minimizing budget γ∗ therefore shifts upward to offset this additional
constant
randomization. These findings help explain why empirical clicks under the constant strategy
initially increase with γ but may subsequently plateau or decline in Figure 6, and why this
pattern becomes less pronounced as K increases in Figure 7.
These points also clarify where the firm’s and the policymaker’s objectives align under this
strategy. A firm seeking to minimize regret selects the privacy budget γ∗ . Practically,
constant
γ∗ provides managers with a rule of thumb for setting the privacy budget ex ante as
constant
a function of the number of arms K and visitors T. A policymaker seeking the strongest
privacy protection without sacrificing experimental performance also selects γ∗ : to the
constant
right of γ∗ , reducing the budget both strengthens privacy and lowers regret, whereas
constant
moving to the left of γ∗ strengthens privacy only at the cost of higher regret. Thus,
constant
γ∗ represents the point at which the firm and the policymaker meet.
constant
5.2. The privacy elasticity of regret for the dynamic strategy
In Figure 9, we present the counterpart of Figure 8 for the dynamic strategy (see Web
Appendix I.2 for the technical derivation). Unlike the constant strategy, the elasticity here

31
is non-positive throughout: relaxing the privacy budget reduces regret by delaying the point
| t at which | the | budget | cap | becomes | active | (see Equation | 17). |     |     |     |
| ---------- | --- | ------ | --- | ------- | ------ | ------------- | ---- | --- | --- | --- |
γ
Figure9 Privacy risk elasticity of regret as a function of the privacy budget γ, for different numbers of arms
|     | (K∈2,5,20) |       |              | ∈10,000,100,000,1,000,000). |     |       |     |     |        |     |
| --- | ---------- | ----- | ------------ | --------------------------- | --- | ----- | --- | --- | ------ | --- |
|     |            |       | and visitors | (T                          |     |       |     |     |        |     |
|     |            | k = 2 |              |                             |     | k = 5 |     |     | k = 20 |     |
0
terger fo yticitsale ksir ycavirP
−1
−2
Later, once
| −3  |                    |     |     |     |     |           |     | enough information |     |     |
| --- | ------------------ | --- | --- | --- | --- | --------- | --- | ------------------ | --- | --- |
|     | `Ideal` point: the |     |     |     |     | Early on, |     | has been gathered, |     |     |
−4 privacy risk budget exploration dominates, effective exploitation
|     | at which the budget |     |     |     | so increasing gamma has |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
has a larger effect
|     | lasts for all customers. |     |     |     | a smaller effect on regret. |     |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
on regret.
−5
| 0   | 1   | 2 3 | 4 5 | 6   | 0 1 | 2 3 4 | 5 6 | 0 1 | 2 3 | 4 5 6 |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
Privacy risk budget (gamma)
|     |     |     | Number of visitors (T) |     |     | 1e4 | 1e5 | 1e6 |     |     |
| --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
Note. The elasticity is negative where relaxing privacy protection (increasing γ) reduces regret, and positive where
furtherincreasesinγ raiseregret.Thezero-crossingsmarkistheidealprivacybudgetsthatminimizesregretforeach
(k,T) combination.
The annotations in Figure 9 highlight the three relevant regimes. First, as illustrated by
γ∗
the left-panel annotation, the most favorable point is near the largest value of γ
dynamic
for which the privacy budget lasts through all visitors, i.e., t (cid:25)T and allows the bandit to
γ
follow the optimal exploration/exploitation schedule. For small γ, the curves are relatively
flat (see middle panel): early regret is dominated by exploration, so marginally increasing
the privacy budget has only limited effect. Exploitation is insuﬀicient to ensure results close
to optimal. As γ increases, the strategy gathers enough information to exploit effectively
(see right panel). This produces a large marginal reduction in regret and therefore a strongly
| negative | elasticity. |     |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

32
Each curve ends at a finite value of γ. Beyond that level of γ, t (cid:21)T, and the dynamic
γ
strategy can follow the exploration/exploitation schedule of the non-private bandit. Further
increasing γ has no impact on expected regret, and elasticity is zero. This privacy risk cutoff
increases as T and K increase, because experimenting with more visitors and more arms
require a longer exploration phase before the strategy can exploit effectively.
Taken together, the constant and dynamic strategies yield two distinct experiment-level
ideal privacy budgets. Although γ∗ and γ∗ are values of the same privacy budget,
constant dynamic
they are not directly comparable because each identifies only the budget at which regret
is minimized within its respective strategy. They do not reveal the absolute level of regret
attained at those budgets. Comparing the two budgets alone consequently does not establish
which strategy delivers better absolute performance.
Thisstrategy-selectionproblembecomesespeciallyimportantwhenfirmsconductmultiple
experiments over time. Managers must therefore decide not only how to set the privacy
budget for an individual experiment, but also how to allocate privacy risk across a portfolio
of experiments. We next extend the analysis to the firm level and examine which strategy—
constant or dynamic—delivers the highest expected rewards under a given firm-level privacy
budget.
6. Firm-level privacy budget allocation
We next consider a firm with a finite firm privacy budget Γ that limits cumulative privacy
risk across its portfolio of experiments (see Level 3 in Figure 2).
6.1. The optimization problem
Following the marketing resource-allocation literature (Fischer et al. 2011, Peers et al. 2017,
Zia and Rao 2019), we treat the firm-wide privacy budget Γ as a scarce resource. The
firm must allocate this budget across experiments and select a spending strategy for each
experiment to minimize total regret.

33
6.1.1. The exogenous environment. The firm specifies the firm-wide privacy budget Γ
and the characteristics of each experiment, including its number of arms and visitors. A
visitormayparticipateinmultipleexperimentsbutparticipatesonlyonceinanygivenexper-
iment. Under sequential composition, the cumulative privacy risk for a visitor is bounded
by the sum of the budgets of the experiments in which that visitor participates (see Theo-
| rem 3.14 | in Dwork and | Roth | 2014). |     |     |
| -------- | ------------ | ---- | ------ | --- | --- |
6.1.2. The objective and feasible solution space. The firm chooses the allocation that
minimizes the regret introduced by privacy protection. The regret bounds for the constant
and dynamic strategies in Equations (15) and (18) provide the building blocks for this
objective.
Let e2f1,...,Eg index experiments and s2fconstant,dynamicg index strategies. Let
2f0,1g (cid:21)0
z indicate whether strategy s is selected for experiment e, and let γ denote
e,s e,s
the privacy budget allocated to that experiment–strategy pair. Finally, let R (γ ) denote
e,s e,s
| the corresponding | regret | bound. | The firm | solves |     |
| ----------------- | ------ | ------ | -------- | ------ | --- |
XE X
|     |     | min        |     | z R (γ  | )   |
| --- | --- | ---------- | --- | ------- | --- |
|     |     |            |     | e,s e,s | e,s |
|     |     | {ze,s,γe,s | }   |         |     |
s∈S
e=1
XE X
|     |     | subject | to  | γ (cid:20)Γ, |     |
| --- | --- | ------- | --- | ------------ | --- |
e,s
e=1 s∈S
X
(19)
|     |     |     |     | z =1 | 8e, |
| --- | --- | --- | --- | ---- | --- |
e,s
s∈S
|     |     |     | 0(cid:20)γ | (cid:20)z ∗ | 8e, s2S, |
| --- | --- | --- | ---------- | ----------- | -------- |
γ
e,s e,s e,s
|     |     |     | 2f0,1g |     | 8e, s2S. |
| --- | --- | --- | ------ | --- | -------- |
z
e,s
The first constraint limits total allocated privacy budget to the firm-wide budget Γ. The
second requires the firm to select exactly one strategy for each experiment. The third links
the budget allocation to that strategy choice: an unselected strategy receives no budget,

34
whereas a selected strategy may receive any budget up to its strategy-specific performance
benchmark γ∗ , derived in §5. The final constraint defines the strategy-selection variables as
e,s
γ∗
binary. Restricting allocations to is without loss of optimality because performance does
e,s
not improve beyond this point and the firm-wide budget need not be fully exhausted.
|            |          |        |        |        |                 | The | key managerial | quantity |     |
| ---------- | -------- | ------ | ------ | ------ | --------------- | --- | -------------- | -------- | --- |
| 6.1.3. The | solution | space: | Return | on the | privacy budget. |     |                |          |     |
is the return on the privacy budget. Intuitively, a larger privacy budget gives an experiment
more room to learn, which reduces regret. However, the value of additional privacy budget
need not be the same across experiments or strategies. For each experiment e and strategy
| s, we capture | this return | using | the marginal | learning | gain: |     |     |     |     |
| ------------- | ----------- | ----- | ------------ | -------- | ----- | --- | --- | --- | --- |
d
|     |     |     | G (γ) | := (cid:0) | R (γ). |     |     |     | (20) |
| --- | --- | --- | ----- | ---------- | ------ | --- | --- | --- | ---- |
|     |     |     | e,s   |            | e,s    |     |     |     |      |
dγ
Because R (γ) is a regret bound, a decrease in R (γ) is a gain. The minus sign ensures
|     | e,s |     |     |     | e,s |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that G (γ) is positive when increasing the privacy budget reduces regret. Thus, G (γ)
| e,s |     |     |     |     |     |     |     |     | e,s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
measures how much regret is reduced by giving a small additional amount of privacy budget
| to experiment | e under | strategy | s.  |     |     |     |     |     |     |
| ------------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
This quantity provides a direct way to compare privacy budget allocations. If G (γ) is
e,s
large, then an additional unit of privacy budget produces a large reduction in regret for
that experiment–strategy pair. If G (γ) is small, then an additional unit of privacy risk
e,s
has a limited effect on regret. The firm should therefore allocate privacy budget first to the
experiment–strategy pairs with the highest marginal learning gains (i.e., highest G (γ)).
e,s
At the optimum, all selected pairs whose budgets can still be adjusted must have the same
| marginal return. | That | is, there | exists | a constant | λ(cid:21)0 such | that |     |     |     |
| ---------------- | ---- | --------- | ------ | ---------- | --------------- | ---- | --- | --- | --- |
∗
|     | G (γ    | )=λ | for all (e,s) | such | that z =1 | and 0<γ | <γ  | .   | (21) |
| --- | ------- | --- | ------------- | ---- | --------- | ------- | --- | --- | ---- |
|     | e,s e,s |     |               |      | e,s       |         | e,s | e,s |      |

35
The constant λ is the shadow value of the firm-wide privacy budget: it is the reduction in
total regret from marginally relaxing the firm-wide privacy budget.
To illustrate our allocation procedure, consider Figure 10 which shows the allocation logic
for two hypothetical experiments: Experiment A has 1,000 visitors and 2 arms, while Exper-
iment B has 10,000 visitors and 2 arms. For simplicity, we assume that only one strategy is
available in this illustration. The three columns trace the progression from an initial alloca-
tion (see the left panel), through a budget reallocation (see the middle panel), to the optimal
allocation (see the right panel). The two rows correspond to two firm-wide privacy budgets:
a larger budget (Γ=4) in the top row and a smaller budget (Γ=1.5) in the bottom row.
1. Initial allocation 2. Reallocate budget 3. Optimal allocation
Move budget from
Marginal gains differ:
lower−return pair
reallocate budget
to higher−return pair
λ
Move budget from Corner solution:
Marginal gains differ:
lower−return pair all budget goes to
reallocate budget
to higher−return pair higher−return pair
Firm−wide
budget
=
4
Firm−wide
budget
=
1.5
7.5
5.0
2.5
0.0
7.5
5.0
2.5
0.0
0 1 2 3 4 0 1 2 3 4 0 1 2 3 4
Allocated privacy risk budget γ
)γ(
G
:niag
gninrael
lanigraM
e
Experiment A (1,000 visitors, 2 arms) Experiment B (10,000 visitors, 2 arms)
Figure10 Privacy budget reallocation across two experiments and assuming a single strategy. The x-axis shows
the allocated privacy budget γ, and the y-axis shows the marginal learning gain G (γ). The firm
e,s
reallocates the budget toward the experiment with the higher marginal learning gain (red arrows).

36
In the top row, the initial allocation gives different marginal learning gains across the two
experiments. Since Experiment B has the higher marginal gain, the budget is shifted toward
Experiment B until the marginal gains are equalized at λ (see red arrows). In the bottom
row, the smaller firm-wide budget leads to a corner solution: the budget is too limited to
equalize marginal gains, so all available budget is allocated to the higher-return experiment.
6.2. Benchmark policies
We compare the allocation described above with several benchmark allocations that differ
in how they choose strategies and divide the firm-wide privacy budget Γ across experiments.
6.2.1. The upper bound on performance: the γ∗ benchmark. For each experiment, this
benchmark assigns the strategy-specific reference level implied by the elasticity analysis (see
§5) for the selected strategy:
γ =z γ ∗ 8e, s2fconstant,dynamicg.
e,s e,s e,s
P P
The implied portfolio privacy spending is E z γ∗ , which may exceed Γ. Hence,
e=1 s e,s e,s
thisbenchmarkservesasanunconstrainedreferenceallocationratherthanafeasibleportfolio
solution.
6.2.2. Managerial heuristic: equal-split benchmark. Thisbenchmarkallocatesthefirm-
wide privacy budget equally across experiments. With E experiments, each experiment is
assignedanequalshareΓ/E,andforeachexperimentwefixthestrategyastheonethatmin-
imizes the regret bound at that equal-share cap, i.e., s 2argmin Rs(Γ/E).
e s∈{constant,dynamic} e
P
The selected cap then satisfies z γ =Γ/E for all e.
s∈{constant,dynamic} e,s e,s
6.2.3. The lower bound on performance: Γ=0, equivalent to random baseline. We
include a zero-budget baseline in which no privacy risk is allocated to any experiment (i.e.,
γ =0 for all e,s). This implies full randomization within each experiment. This benchmark
e,s
therefore serves as a lower bound reference for learning performance under the strongest
privacy protection.

37
6.3. Application of the firm-wide privacy budget
We next empirically apply the privacy budgeting across multiple experiments under a firm-
wide budget. We use a dataset of 78 experiments conducted by ASOS, a British fashion
retailer serving customers worldwide (Liu et al. 2021). These experiments are online RCTs
conducted on ASOS’s e-commerce platform.8
6.3.1. Setup. We visualize summary statistics from these experiments in Figure 11. The
top-left panel shows the number of arms per experiment, and the top-right panel shows the
number of visitors per experiment. The bottom-left panel reports the distribution of arm-
level CTRs across all unique arms, while the bottom-right panel shows the distribution of
treatment–controlCTRupliftsinpercentagepointsforwithin-experimentarmcomparisons.9
Most experiments used two arms, and only a few used four or five arms. The average
number of visitors was 21 million, with a minimum of 69,000 and a maximum of 149,197,471.
The large visitor counts likely reflect the relatively long runtimes of these experiments. On
average, experiments ran for 43.5 days, with a maximum duration of 131 days.
The distribution of arm-level CTRs is broad. The average CTR is 19.55%, with an
interquartilerangefrom5.69%to24.83%.CTRsrangefrom2.65%to77.24%,indicatingsub-
stantial heterogeneity across arms and experiments. The distribution of treatment–control
CTR uplifts (in percentage points) is centered near zero, implying that many arms produce
modest gains or losses relative to the control, while a smaller number of arms generate large
positive uplifts. The distribution is right-skewed, with a long upper tail.
8The experiments test product recommendation on the retailer’s website. CTRs vary between....,and the number or
arms vary between ...... The dataset is publicly available, therefore we can share the data together with our code, to
facilitate replication.
9Computed as 100×(CTR −CTR ), in percentage points.
arm control

38
| Number of arms per experiment |     |     | Number of visitors per experiment |     |     |
| ----------------------------- | --- | --- | --------------------------------- | --- | --- |
60
15
40
10
20
5
snoitavresbo fo rebmuN
| 0                       |               | 0       |                            |        |        |
| ----------------------- | ------------- | ------- | -------------------------- | ------ | ------ |
| 2                       | 3 4           | 5 69.1K | 50.0M                      | 100.0M | 150.0M |
|                         | CTR level (%) |         | CTR uplift (pp)            |        |        |
| Count = 177 unique arms |               |         | Count = 99 arm comparisons |        |        |
30
30
20
20
| 10     |         | 10  |        |        |        |
| ------ | ------- | --- | ------ | ------ | ------ |
| 0      |         | 0   |        |        |        |
| 0% 20% | 40% 60% | 80% | 0.0 pp | 0.5 pp | 1.0 pp |
Figure11 Empirical distributions of key inputs and outputs from the ASOS online experiments.
The wide variation in CTRs likely reflects differences in experimental context and click
definitions across ASOS’s on-site tests. Although the underlying experimental contexts are
confidential (Liu et al. 2021), we can offer plausible interpretations. In some experiments,
high CTRs may arise from goal-directed actions, such as checkout steps, whereas low CTRs
may reflect more discretionary interactions, such as clicking a secondary fashion item. We
use these empirical statistics to construct the experiment-level inputs for the portfolio prob-
lem, and then evaluate the benchmark allocations for 10 firm-wide privacy budgets, Γ 2
f.01,.1,1,3,5,10,20,50,100,500g.
6.3.2. Results. In Figure 12, the y-axis shows the median improvement in portfolio
clicks relative to the random-policy baseline, defined as total clicks under each policy minus
random-policy clicks. The x-axis shows the privacy budgets Γ. Points report medians over
100 simulation repetitions, and error bars show the interquartile range. Colors distinguish
the benchmark allocation rule (see Section 6.2), while shapes indicate the within-experiment

39
strategy regime. The flexible regime allows the firm to choose, for each experiment, whether
to use the constant or dynamic privacy budgeting strategy. By contrast, the constant regime
restricts all experiments to use the constant strategy, and the dynamic regime restricts all
experiments to use the dynamic strategy. The dashed horizontal line at zero indicates the
random (lower bound) benchmark, equivalently the Γ=0 case. The solid horizontal line indi-
cates the upper bound γ∗ benchmark. We use text annotations to highlight the difference in
median clicks between the managerial heuristic and the regret-based allocation benchmark.
∆=0
250,000
225,000
∆=22,934
200,000
175,000
150,000 ∆=30,485
125,000
∆=51,047
100,000
∆=45,495
∆=39,282
75,000 ∆=29,687
∆=27,853
50,000
∆=−3,276 ∆=1,383
25,000
12,500
0
0.01 0.1 1 3 5 10 20 50 100 500
Firm−wide privacy risk budget Γ
skcilc
ycilop−modnar
sunim
skcilc
latot
naideM
Benchmark Managerial heuristic: equal split Regret based allocation (this paper)
Within−experiment regime Constant only Dynamic only Flexible: constant or dynamic
Figure12 Medianimprovementinportfolioclicksrelativetotherandom-policybaselineacrossfirm-wideprivacy
budgets.Pointsreportmediansoversimulationrepetitions,anderrorbarsshowtheinterquartilerange.
Colors indicate the firm-wide allocation rule, while shapes indicate the within-experiment budgeting
regime.

40
Figure 12 shows that under a fixed firm-wide privacy budget Γ, the regret-based allocation
often delivers substantially more clicks than the managerial equal-split benchmark (see the
∆ annotations for the median difference in clicks under the flexible regime).
The improvement in clicks is largest at intermediate firm-wide privacy budgets (e.g., Γ2
5,20). When the firm-wide privacy budget is very small, both allocation rules have limited
ability to learn, so gains in clicks are small (e.g., Γ2f0.01,0.1g). When Γ is very large, both
rules eventually approach the upper-bound benchmark.
This pattern highlights a key managerial choice: firms can improve experimentation out-
comes either by increasing the total privacy budget or by allocating the existing budget
more effectively. The figure shows that the second option can generate more clicks without
increasing firm-wide privacy risk. By directing a fixed budget Γ toward experiments where
additional information is most valuable, firms can improve performance while keeping total
privacy exposure unchanged. The privacy–performance tradeoff therefore depends not only
on how much privacy risk the firm permits, but also on how selectively it allocates that risk
across experiments.
7. Discussion
Firms increasingly rely on online experiments to decide what consumers see, such as banners,
ads, recommendations, and product rankings. While these decisions are typically studied as
learning problems, we highlight the privacy risk that the experimental outputs themselves
can create: what a firm displays may reveal information to third-parties before a consumer
clicks, purchases, or otherwise responds. Our privacy budgeting framework manages this risk
at three levels. At the individual level, privacy risk captures how much a displayed output
can reveal about a consumer. At the experiment level, a privacy budget γ limits the risk
generated by a single experiment and formalizes the trade-off between privacy protection

41
and learning. At the firm level, a firm-wide budget Γ limits cumulative risk across potentially
linkable experiments, turning privacy protection into a portfolio allocation problem across
experiments and budgeting strategies.
A key step in the paper is linking the exploration parameter ε in the ε-greedy policy to
the privacy risk parameter from differential privacy (Dwork and Roth 2014). The parameter
ε determines how often the firm explores rather than exploits the currently best-performing
arm. We use this relationship to construct the inputs to the firm-wide portfolio problem. We
perform an elasticity analysis that identifies, for each experiment and budgeting strategy, the
ideal experiment-level privacy budget γ∗ at which additional privacy budget has diminishing
returns. The firm-wide problem uses these ideal budgets to allocate the available budget Γ
across these experiment-level opportunities, choosing both which strategy to use and how
much budget to assign, in order to improve portfolio clicks subject to the firm-wide privacy
budget.
To spend the privacy risk, we propose two strategies a constant and a dynamic strategy.
A constant strategy is simple and transparent because it assigns the same privacy budget
throughout the experiment. This may be attractive for implementation, communication, and
governance. However, it is also rigid: it does not adapt to the changing value of learning over
the course of an experiment. A dynamic strategy can allocate privacy risk more flexibly as
the experiment evolves, potentially reducing regret for a given privacy budget. The portfolio
formulation allows the firm to choose between these strategies experiment by experiment,
rather than imposing the same privacy budgeting rule across all experiments.
7.1. Limitations and future research
Several choices shape the interpretation of the firm-wide budget. First, the regret bounds are
independentoftheexpectedCTRsoftheexperiments.Thisisbecausetheregretboundsused

42
intheportfolioproblemareworst-caseguarantees:theyareintendedtoholduniformlyacross
possible CTR environments, including those unknown to the firm before experimentation
(cf. Joo and Chiong 2025). Conditioning the allocation rule on expected CTRs could yield a
more tailored bound in a known environment, but would make the result less general and less
useful in practice, since these rates are themselves objects of learning. We therefore allocate
privacy risk according to the marginal reduction in worst-case regret from an additional unit
of privacy budget, rather than according to which experiment has the highest observed or
expected CTR.
Second, the firm-wide budget should be interpreted as a conservative portfolio-level con-
straint. The formulation in Equation (19) protects against the worst-case scenario in which
the same customer appears in every linkable experiment in the portfolio. In practice, how-
ever, most customers will appear in only a subset of experiments. For example, a customer
exposed to only 10% of the experiments will generally face a realized cumulative privacy
risk below the portfolio-wide worst-case bound. Thus, Γ is an upper bound on cumulative
privacy risk across linkable experiments, not a claim that every customer realizes that level
of privacy risk.
Third, our frameworkdoes not allowprivacysensitivityto varyacross arms. Consequently,
an arm with a higher CTR does not mechanically receive a higher or lower privacy cost
than an arm with a lower CTR. This keeps the privacy accounting focused on the informa-
tion revealed by the experimental output and on the resulting regret trade-off. A natural
extension would introduce arm-specific privacy risk, allowing some displayed items, prod-
ucts, or recommendations—for example, a particularly sensitive book recommendation—to
be treated as more privacy-sensitive than others.
Overall, the paper connects privacy protection to the economics of experimentation. Pri-
vacy is not treated as a fixed constraint imposed separately on each experiment, but as a

43
scarce resource that must be allocated across a portfolio of learning problems. This per-
spective is useful for firms that run many concurrent personalization and experimentation
systems. It also highlights why privacy governance must operate at the firm level: even
when each individual experiment is privacy-aware, cumulative privacy risk can emerge across
linkable experiments. A firm-wide privacy budget, combined with regret-based allocation,
offers a practical framework for managing the trade-off between learning, performance, and
privacy.
Acknowledgments

44
| Web Appendix |     | A: A | model | of privacy | risk in | experimentation |     |     |
| ------------ | --- | ---- | ----- | ---------- | ------- | --------------- | --- | --- |
We distinguish between the firm’s information and that available to a tracker using Google Analytics (GA)
as a running example. GA is used by 51% of the top one million websites globally (Lee 2026).
LetS denotecustomeri’slatentsegment.Beforetheexperiment,thefirmobservesfirst-partyhistoryHF
i i
and forms an internal state UF =ϕ(HF). It then generates experimental output A through a mechanism
|     |     |     | i   | i   |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
M: A (cid:24)M(UF). After exposure, the customer may generate behavior Y =(YE,YO), where YE is specific
| i   | i   |     |     |     |     |     | i i i | i   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
to the experimental output and YO is other behavior. GA instead observes a potentially different history
i
HGA, so generally HGA6=HF. This difference arises because GA receives only information delivered under
| i   |     | i   | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
the measurement architecture Ω, whereas the firm may retain richer first-party records.
Let G 20,1 indicate whether the GA observation channel is active during the experiment. Its value
i
may depend on consent, technical delivery, browser protections and ad blockers. These factors may them-
selves reveal information about the customer’s segment, but they arise outside the experimental assignment
mechanism and are not covered by our privacy guarantee. We therefore condition the analysis on G =1.
i
Conditional on an active channel, Ω determines whether GA observes the experimental arm A alone
i
or both A and the experiment-specific response YE. The arm may be transmitted explicitly through an
i
i
impressioneventorinferredfromvariant-specificURLs,metadata,orpagecontent.Beforeobservingsignals
from the current experiment, GA’s conditional belief about the customer’s segment is
=sjHGA,Ω,G
|     |     |     |     | Pr(S |     | =1). |     |     |
| --- | --- | --- | --- | ---- | --- | ---- | --- | --- |
|     |     |     |     |      | i i | i    |     |     |
This prior incorporates GA’s historical information and any information conveyed by the active observation
channel.Thecurrentexperimentcanthengeneratetwofurtherupdates:onefromthedisplayedoutputand,
| when observed, | one  | from the | experiment-specific |     | response. |     |     |     |
| -------------- | ---- | -------- | ------------------- | --- | --------- | --- | --- | --- |
| A.1. Privacy   | risk | from     | experimental        |     | output    |     |     |     |
First,GAmayobservethedisplayedexperimentaloutputA .Thiscorrespondstothecaseinwhichthefirm’s
i
measurement architecture reveals the experimental arm to GA. For architectures in which A is observed by
i
| GA, the corresponding |     | output-update |     | factor | is  |     |     |     |
| --------------------- | --- | ------------- | --- | ------ | --- | --- | --- | --- |
=ajHGA,Ω,G
|     |     |     |     | Pr(A |            | =1,S | =s)  |     |
| --- | --- | --- | --- | ---- | ---------- | ---- | ---- | --- |
|     |     |     | R   | (a)= | i i        | i    | i .  |     |
|     |     |     | A   | Pr(A | =ajHGA,Ω,G | =1,S | =s′) |     |
|     |     |     |     |      | i i        | i    | i    |     |

45
Thisprivacyriskiscontrolledbytheprivacy-preservingassignmentmechanisminEquation(13).Conditional
on GA’s historical information, the measurement environment, and the GA channel being active, we bound
| the | posterior-odds |     | multiplier | from | observing |     | the displayed |                | arm: |     |     |     |     |
| --- | -------------- | --- | ---------- | ---- | --------- | --- | ------------- | -------------- | ---- | --- | --- | --- | --- |
|     |                |     |            |      |           |     | R             | (a)(cid:20)eγ. |      |     |     |     |     |
A
| A.2. | Privacy |     | risk from | behavior |     | after | experimental |     | output |     |     |     |     |
| ---- | ------- | --- | --------- | -------- | --- | ----- | ------------ | --- | ------ | --- | --- | --- | --- |
Second, if GA also observes behavior directly related to the experimental output, this behavior may create
an additional source of posterior updating. For example, after observing that customer i was shown arm
A =a, GA may also observe whether the customer clicked on that experimental arm. Conditional on the
i
| displayed |     | arm, the | experiment-specific |         |     | behavioral-response |     |     | factor | is   |      |     |     |
| --------- | --- | -------- | ------------------- | ------- | --- | ------------------- | --- | --- | ------ | ---- | ---- | --- | --- |
|           |     |          |                     |         |     | Pr(YE=yEjHGA,Ω,G    |     |     | =1,A   | =a,S | =s)  |     |     |
|           |     |          |                     | R (yE)= |     | i                   |     | i   | i      | i    | i    | .   |     |
|           |     |          |                     | YE      |     | Pr(YE=yEjHGA,Ω,G    |     |     |        |      |      |     |     |
|           |     |          |                     |         |     |                     |     |     | =1,A   | =a,S | =s′) |     |     |
|           |     |          |                     |         |     | i                   |     | i   | i      | i    | i    |     |     |
This factor measures how informative the customer’s experiment-specific response is once exposure has
already occurred. For instance, if customers in segment s are more likely than customers in segment s′ to
click on arm a, then observing a click on the experimental output increases GA’s belief that the customer
| belongs | to  | segment | s.        |        |     |     |     |     |     |     |     |     |     |
| ------- | --- | ------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A.3.    | The | full    | posterior | update |     |     |     |     |     |     |     |     |     |
The model of privacy risk in experimentation is conditional on the GA observation channel being active.
If G =0, GA receives no current experimental signal, so the current experiment generates no output- or
i
response-basedposteriorupdate.ConditionalonG =1,theposteriorupdatedependsonwhichexperimental
i
signals are observed under the measurement architecture Ω. If GA observes the displayed arm but not the
| experiment-specific |     |     | response, | then        |     |        |       |      |             |     |     |        |     |
| ------------------- | --- | --- | --------- | ----------- | --- | ------ | ----- | ---- | ----------- | --- | --- | ------ | --- |
|                     |     |     |           | =sjHGA,Ω,G  |     |        |       |      | =sjHGA,Ω,G  |     |     |        |     |
|                     |     |     | Pr(S      |             |     | =1,A   | =a)   | Pr(S |             |     | =1) |        |     |
|                     |     |     |           | i           | i   | i      | i     | =    | i           | i   | i   | R (a). |     |
|                     |     |     |           | =s′jHGA,Ω,G |     |        |       |      | =s′jHGA,Ω,G |     |     | A      |     |
|                     |     |     | Pr(S      | i           |     | i =1,A | i =a) | Pr(S | i           |     | i   | =1)    |     |
|                     |     |     |           |             | i   |        |       |      |             | i   |     |        |     |
If GA observes both the displayed arm and the raw experiment-specific response, then
|     | Pr(S | =sjHGA,Ω,G  |     | =1,A |      | =a,YE=yE) |     |     |     |     |     |     |     |
| --- | ---- | ----------- | --- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     |      | i           | i   | i    | i    | i         |     |     |     |     |     |     |     |
|     | Pr(S | =s′jHGA,Ω,G |     |      | =1,A | =a,YE=yE) |     |     |     |     |     |     |     |
|     | |    | i           | i   | {iz  |      | i i       | }   |     |     |     |     |     |     |
posteriorodds
=sjHGA,Ω,G
|     |     | Pr(S |             |     |     | =1)                            |     |       |     |                                        |     |          |     |
| --- | --- | ---- | ----------- | --- | --- | ------------------------------ | --- | ----- | --- | -------------------------------------- | --- | -------- | --- |
|     |     | =    | i           | i   | i   |                                |     | R (a) |     |                                        |     | R (yE)   | .   |
|     |     | Pr(S | =s′jHGA,Ω,G |     |     | =1)                            |     | | A{z | }   |                                        |     | | YE{z } |     |
|     |     | |    | i           | {iz | i   | }                              |     |       |     |                                        |     |          |     |
|     |     |      |             |     |     | experimental-outputprivacyrisk |     |       |     | experiment-specificbehaviorprivacyrisk |     |          |     |
prioroddsconditionalonaccess

46
Web Appendix B: Differential privacy in the context of bandits
A randomized mechanism M satisfies ξ-differential privacy if, for any two neighboring datasets D and D′
that differ in at most one individual, and for all measurable events S in the output space,
|     |     |     |     |     | P(M(D)2S)(cid:20)eξP(M(D′)2S). |     |     |     |     |     |     | (22) |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | ---- |
In our setting, let D=(a ,...,a ), where a 2f0,1g denotes the non-private arm label associated with
|     |     |     |     | 1   | T   | t   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
visitor t. A neighboring dataset is D′=(a ,...,a′,...,a ), which differs from D only in the t-th entry, with
|     |     |     |     |     |     | 1   |     | T   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
a 6=a′.
t t
Atroundt,theε-greedyruleinEquation(4)inducesarandommappingfromthenon-privatearmlabela
t
to the displayed arm a∗. Applying this mapping independently across visitors yields the overall mechanism
t
M(D)=(a∗,...,a∗).
|     |     |     |     |     |     |     | 1   | T   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Under this conditional independence assumption, the joint output distribution factorizes across visitors, so
| the privacy | condition |         | in Equation |               | (22) | becomes |             |                   |     |               |         |      |
| ----------- | --------- | ------- | ----------- | ------------- | ---- | ------- | ----------- | ----------------- | --- | ------------- | ------- | ---- |
|             |           | (cid:0) |             |               |      | (cid:1) | (cid:0)     |                   |     |               | (cid:1) |      |
|             |           | P M(a   |             | )=(a∗,...,a∗) |      |         | (cid:20)eξP | M(a ,...,a′,...,a |     | )=(a∗,...,a∗) |         |      |
|             |           |         | 1 ,...,a    |               |      |         |             | 1                 |     |               | .       | (23) |
|             |           |         |             | T             | 1    | T       |             |                   | t   | T 1           | T       |      |
Because D and D′ differ only in the t-th entry, all terms except the t-th cancel in the likelihood ratio.
| Hence, | the privacy | requirement |     | reduces |      | to the one-visitor |         | condition |           |     |     |      |
| ------ | ----------- | ----------- | --- | ------- | ---- | ------------------ | ------- | --------- | --------- | --- | --- | ---- |
|        |             |             |     | (cid:0) |      | (cid:1)            | (cid:0) |           | (cid:1)   |     |     |      |
|        |             |             | P   | a∗=jja  |      | (cid:20)eξP        | a∗=jja  |           | 8j2f0,1g. |     |     |      |
|        |             |             |     |         | t =0 |                    |         | t =1      | ,         |     |     | (24) |
|        |             |             |     | t       |      |                    | t       |           |           |     |     |      |
Equation (24) implies that observing a particular displayed output does not allow an outside observer to
sharply distinguish between the two possible underlying visitor types. Even if Jamie’s underlying arm label
were different, the probability of observing the same displayed output could change by at most a factor of
eξ.
| Web Appendix |     | C:  | Parallel |     | composition |     |     |     |     |     |     |     |
| ------------ | --- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
2f1,...,kg
ForT visitors,letA=(a 1 ,...,a )denotethevectorof(possiblyadaptive)armchoices,wherea
|     |     |     |     | T   |     |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is the arm selected by the bandit at round t. The displayed arm is generated by a per-visitor randomizer
M 7!a∗,implementedviathestochasticmatrixP
| : a |     |     |     |     |     |     |     | (seeEquation(10)).Weassumetheprivacyschedule |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
| t t | t   |     |     |     |     |     | t   |                                              |     |     |     |     |
(ξ )T (equivalently, (P )T ) is fixed ex ante. Let q ((cid:1)ja) denote the conditional probability mass function
| t t=1   |       |           | t t=1        |         |     |     | t   |     |     |     |     |     |
| ------- | ----- | --------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| M       |       | (a∗       | ja           |         |     |     |     |     |     |     |     |     |
| of (a), | i.e., | q         | )=(P         | ) a∗    | .   |     |     |     |     |     |     |     |
| t       |       | t t       | t            | t t ,at |     |     |     |     |     |     |     |     |
| We make | the   | following | assumptions: |         |     |     |     |     |     |     |     |     |

47
A1. Per-visitor (local) DP. For all a,a′ in the arm domain and all measurable S (cid:18)Range(M ),
|     |     |     |     |      |       |     |                |      |           | t   |     | t    |
| --- | --- | --- | --- | ---- | ----- | --- | -------------- | ---- | --------- | --- | --- | ---- |
|     |     |     |     | Pr[M | (a)2S |     | ] (cid:20) eξt | Pr[M | (a′)2S ]. |     |     | (25) |
|     |     |     |     |      | t     | t   |                | t    | t         |     |     |      |
Equivalently (for discrete outputs), for all possible displayed arms a∗2f1,...,kg,
t
|     |     |     |     | (a∗ja) | (cid:20) eξtq | (a∗ja′), |     | 8a,a′2f1,...,kg. |     |     |     |     |
| --- | --- | --- | --- | ------ | ------------- | -------- | --- | ---------------- | --- | --- | --- | --- |
q
|     |     |     |     | t t |     | t   | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A2. Disjointness and fresh randomness (conditional independence). At each round t, visitor t
contributes a single record: the arm a selected by the bandit policy. The policy may be adaptive, so a can
|     |     |     |     |     | t   |     |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
depend on the past history of privatized displays and rewards. After a is chosen, the privacy mechanism
t
| M   |     |     |     |     |     |     |     |     | a∗. |     | M   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t is applied locally to that one record to produce the displayed arm In particular, t is memoryless:
t
conditionalonthecurrentinputa ,thedistributionofa∗ doesnotdependonpastdisplayedarmsorrewards.
|     |     |     |     | t   |     |     | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M
(Thus, past outputs can influence a through the bandit policy, but they do not enter directly.)
|     |     |     |     |     | t   |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Moreover, M uses fresh randomization that is independent across visitors and independent of A. Conse-
t
quently, conditional on the realized input vector A=(a ,...,a ), the privatized displays are independent
|     |     |     |     |     |     |     |     | 1   | T   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
across visitors:
YT
|     |     |     |     |     | Pr(a∗,...,a∗ |     | jA) = | q   | (a∗ja ). |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ----- | --- | -------- | --- | --- | --- |
|     |     |     |     |     | 1            |     | T     | t   | t t      |     |     |     |
t=1
This conditional factorization holds even when A is generated adaptively, because conditioning on A fixes
| the inputs | and | leaves | only the | independent |     | privacy | randomization |     | in fM g. |     |     |     |
| ---------- | --- | ------ | -------- | ----------- | --- | ------- | ------------- | --- | -------- | --- | --- | --- |
t
Let A′ be a neighboring input vector that differs from A in exactly one coordinate i, i.e., A′ =
Q
|     | ,a′,a |     |     | a′6=a |     |     |     |     |     | S(cid:18) | T Range(M |     |
| --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --------- | --------- | --- |
(a ,...,a i−1 ,...,a ) with . Our goal is to show that for all measurable ),
| 1   |     | i i+1 | T          | i   | i        |              |     |     |              |     | t=1 | t   |
| --- | --- | ----- | ---------- | --- | -------- | ------------ | --- | --- | ------------ | --- | --- | --- |
|     |     |       | Pr[M(A)2S] |     | (cid:20) | Pr[M(A′)2S], |     |     |              |     |     |     |
|     |     |       |            |     | eγ       |              |     |     | where γ=maxξ | .   |     |     |
t
t
| By Assumption |     | A2, | the probability |             | of any | output | sequence | factorizes: |            |     |     |     |
| ------------- | --- | --- | --------------- | ----------- | ------ | ------ | -------- | ----------- | ---------- | --- | --- | --- |
|               |     |     |                 |             |        |        | X        | YT          |            |     |     |     |
|               |     |     |                 | Pr[M(A)2S]= |        |        |          |             | q (a∗ja ), |     |     |     |
|               |     |     |                 |             |        |        |          |             | t t t      |     |     |     |
(a∗,...,a∗)∈St=1
|     |     |     |     |     |     |     | 1   | T   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and similarly,
|     |     |     |     |     |     |     | (cid:16)Y |     | (cid:17) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --- | --- |
X
|     |     |     | Pr[M(A′)2S]= |     |     |               |     | q (a∗ja | ) q (a∗ja′). |     |     |     |
| --- | --- | --- | ------------ | --- | --- | ------------- | --- | ------- | ------------ | --- | --- | --- |
|     |     |     |              |     |     |               |     | t       | t t i i i    |     |     |     |
|     |     |     |              |     |     | (a∗,...,a∗)∈S |     | t̸=i    |              |     |     |     |
|     |     |     |              |     |     | 1             | T   |         |              |     |     |     |
By the single-round DP guarantee in Equation (25) for t=i, we have pointwise for all a∗:
i
|     |     |     |     |     | q   | (a∗ja | ) (cid:20) eξiq | (a∗ja′). |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --------------- | -------- | --- | --- | --- | --- |
|     |     |     |     |     | i   | i     | i               | i i      | i   |     |     |     |

48
Q
| Multiplying | by q (a∗ja | ) and summing | over all | (a∗,...,a∗)2S             | yields |     |
| ----------- | ---------- | ------------- | -------- | ------------------------- | ------ | --- |
|             | t̸=i t     | t t           |          | 1                         | T      |     |
|             |            | Pr[M(A)2S]    |          | (cid:20) eξi Pr[M(A′)2S]. |        |     |
Because A and A′ may differ at any single coordinate, this implies the uniform guarantee
|     |     | Pr[M(A)2S] | (cid:20) eγ Pr[M(A′)2S], |     | γ=maxξ . |     |
| --- | --- | ---------- | ------------------------ | --- | -------- | --- |
t
t
|     |     | M=(M | ,...,M |     |     |     |
| --- | --- | ---- | ------ | --- | --- | --- |
Therefore, the overall mechanism 1 ) satisfies parallel composition with parameter γ over
T
disjoint per-visitor records. The bandit’s adaptivity affects how inputs A are generated but does not affect
the privacy accounting, because the privacy guarantee is defined with respect to the per-visitor input record
| and the | released output | consists only of | the privatized | displays | fa∗gT . |     |
| ------- | --------------- | ---------------- | -------------- | -------- | ------- | --- |
t t=1
| Web Appendix | D:  | Regret analysis |     |     |     |     |
| ------------ | --- | --------------- | --- | --- | --- | --- |
We derive the regret bound for the segment-specific ε-greedy policy. Let S denote the finite set of consumer
segmentsandletJ=jSjdenotethenumberofsegments.Weassumethatthefirmknowsthesetofsegments
but does not know ex ante how many visitors will belong to each segment. Instead, segment membership is
| observed | sequentially as | visitors arrive. |     |     |     |     |
| -------- | --------------- | ---------------- | --- | --- | --- | --- |
For every arm a 2A and segment s2S, the reward is Bernoulli distributed with an unknown stationary
k
mean µ (s). Thus, the firm learns arm effectiveness separately across segments. At visitor t, let
k
X
|     |     |     | N (s)= | 1fS | =sg | (26) |
| --- | --- | --- | ------ | --- | --- | ---- |
|     |     |     | t      | τ   |     |      |
τ<t
denote the number of previous visitors observed in segment s. We define the learning clock for visitor t as
|     |     |     | n =N | (S )+1. |     | (27) |
| --- | --- | --- | ---- | ------- | --- | ---- |
|     |     |     | t    | t t     |     |      |
Hence, n is the number of visitors observed so far in the current visitor’s segment, including visitor t.
t
Importantly, n t is observed by the firm when visitor t arrives and does not require knowledge of the number
| of future | visitors in that | segment.        |        |     |     |     |
| --------- | ---------------- | --------------- | ------ | --- | --- | --- |
| D.1. The  | regret bound     | of the ε-greedy | policy |     |     |     |
To facilitate our analysis, consider a visitor t belonging to segment S =s. Let µ¯ denote the empirical
t k,s
reward estimate for arm a in segment s, and let µ (s) denote its true expected reward. We define the clean
|     |     | k   |     | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
event C as the event that all arm-specific empirical means for the current segment are suﬀiciently close to
t
| their true | means: |         |             |               |                |      |
| ---------- | ------ | ------- | ----------- | ------------- | -------------- | ---- |
|            |        | C =fjµ¯ | (cid:0)µ (S | )j(cid:20)r , | 8k2f1,...,Kgg, | (28) |
|            |        | t       | k,St k t    | t             |                |      |

49
C¯
where r denotes the confidence radius. The bad event is the complement of the clean event.
|     | t   |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Underuniformexploration,eacharmisselectedwithprobabilityε t /K.Becauselearningoccursseparately
within each segment, the relevant number of opportunities for learning about the current segment is n ,
t
rather than the total experiment-wide visitor count t. Therefore, each arm receives exploratory observations
| at a rate | of order |     |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
n ε
t t.
(29)
K
Moreprecisely,becauseε decreaseswiththenumberofobservationsfromasegment,theexpectedcumu-
t
lative number of exploratory draws of a given arm by local round n is at least of order n ε /K. Standard
t t t
concentration inequalities for the exploration counts, combined with Hoeffding’s inequality for Bernoulli
| rewards, | therefore | give | a confidence | radius | of order |     |     |     |
| -------- | --------- | ---- | ------------ | ------ | -------- | --- | --- | --- |
r
2Klogn
t,
|     |     |     |     |     | r   | =   |     | (30) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | t   | n   | ε   |      |
t t
up to universal constants. The finite initialization period and the corresponding concentration failure prob-
| abilities | do not | affect | the asymptotic | regret | rate. |     |     |     |
| --------- | ------ | ------ | -------------- | ------ | ----- | --- | --- | --- |
Let
|        |           |         |         |             | a⋆(S )=argmaxµ |          | (S )    | (31) |
| ------ | --------- | ------- | ------- | ----------- | -------------- | -------- | ------- | ---- |
|        |           |         |         |             | t              |          | k t     |      |
|        |           |         |         |             |                | ak       | ∈A      |      |
| denote | the truly | optimal | arm for | the current | visitor’s      | segment, | and let |      |
|        |           |         |         |             | a =argmaxµ¯    |          |         | (32) |
|        |           |         |         |             | t              |          | k,St    |      |
|        |           |         |         |             |                | ak ∈A    |         |      |
denote the greedy arm selected using the current empirical estimates. On the clean event, because a maxi-
t
| mizes the | empirical | reward, |     |     |     |            |     |     |
| --------- | --------- | ------- | --- | --- | --- | ---------- | --- | --- |
|           |           |         |     |     | µ¯  | (cid:21)µ¯ | .   |     |
at,St a⋆(St),St
| It follows | that |     |     |           |           |               |              |     |
| ---------- | ---- | --- | --- | --------- | --------- | ------------- | ------------ | --- |
|            |      |     |     |           | )(cid:0)µ |               | )(cid:0)µ¯   |     |
|            |      |     | µ   | a⋆(St) (S |           | (S )=µ a⋆(St) | (S a⋆(St),St |     |
|            |      |     |     | t         | at        | t             | t            |     |
(cid:0)µ¯
+µ¯
|     |     |     |     |     |     |     | a⋆(St),St at,St |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
|     |     |     |     |     |     | +µ¯ | (cid:0)µ (S )   |     |
|     |     |     |     |     |     |     | at,St at t      |     |
(cid:20)2r
t
r
2Klogn
|     |     |     |     |     |     | =2  | t.  | (33) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     | n ε |      |
t t

50
Thus,conditionalonexploitation,theregretfromselectingtheempiricallybestarmratherthanthetruly
optimal arm for the current segment is bounded by the estimation error. Because rewards are bounded
between zero and one, exploration generates at most one unit of regret. The expected instantaneous regret
| at visitor | t is therefore bounded |     | by  |     |     |     |     |
| ---------- | ---------------------- | --- | --- | --- | --- | --- | --- |
r
2Klogn
E[R e (t)](cid:20)Pr(explore)(cid:1)1+Pr(exploit)(cid:1)2 t
n ε
r t t
2Klogn
|     |     |     | =ε  | +(1(cid:0)ε )2 |     | t   |     |
| --- | --- | --- | --- | -------------- | --- | --- | --- |
|     |     |     | t   | t              |     | n ε |     |
|     |     |     |     | r              |     | t t |     |
2Klogn
|     |     |     | (cid:20)ε | +2  | t.  |     | (34) |
| --- | --- | --- | --------- | --- | --- | --- | ---- |
t
n ε
t t
The final inequality uses only 1(cid:0)ε (cid:20)1. Thus, Equation (34) does not require the asymptotic approxima-
t
| 1(cid:0)ε | (cid:25)1. |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- |
tion To minimize the order of the expected regret, we balance the exploration and exploitation
t
terms:
r
Klogn
|     |     |     |     | ε (cid:16) |     | t.  | (35) |
| --- | --- | --- | --- | ---------- | --- | --- | ---- |
|     |     |     |     | t          | n   | ε   |      |
t t
This gives
Klogn
|     |     |     |     | ε3(cid:16) |     | t,  | (36) |
| --- | --- | --- | --- | ---------- | --- | --- | ---- |
|     |     |     |     | t          | n   |     |      |
t
and therefore
|     |     |     |     | (cid:18) |     | (cid:19) |     |
| --- | --- | --- | --- | -------- | --- | -------- | --- |
1/3
Klogn
|     |     |     |     | ε = |     | t , | (37) |
| --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | t   | n   |     |      |
t
where we suppress universal multiplicative constants that do not affect the regret rate. Substituting Equa-
| tion (37) | into Equation (34) | gives |     |        |           |          |      |
| --------- | ------------------ | ----- | --- | ------ | --------- | -------- | ---- |
|           |                    |       |     |        | (cid:18)  | (cid:19) |      |
|           |                    |       |     | e      | K1/3(logn | )1/3     |      |
|           |                    |       | E[R | (t)]=O |           | t .      | (38) |
n1/3
t
We next obtain an experiment-wide bound that does not require the firm to know how many visitors
belong to each segment. Let T denote, only for purposes of the ex-post regret analysis, the realized number
s
of visitors in segment s. Summing Equation (38) over the local learning rounds of all segments gives
  !
XXTs (logn)1/3
E[R(T)](cid:20)O
K1/3
n1/3
|     |     |     |     |     | s∈Sn=1 | !   |     |
| --- | --- | --- | --- | --- | ------ | --- | --- |
X
|     |     |     |     | (cid:20)O K1/3(logT)1/3 |     | T2/3 |     |
| --- | --- | --- | --- | ----------------------- | --- | ---- | --- |
. (39)
s
s∈S
P
| Because | T =T | and x2/3 | is concave, |     |     |     |     |
| ------- | ---- | -------- | ----------- | --- | --- | --- | --- |
s∈S s
X
|     |     |     |     | T2/3(cid:20)J1/3T2/3. |     |     | (40) |
| --- | --- | --- | --- | --------------------- | --- | --- | ---- |
s
s∈S

51
| Hence, | the cumulative | regret | is  | bounded   | by  |                       |     |         |     |      |
| ------ | -------------- | ------ | --- | --------- | --- | --------------------- | --- | ------- | --- | ---- |
|        |                |        |     |           |     | (cid:0)               |     | (cid:1) |     |      |
|        |                |        |     | E[R(T)]=O |     | K1/3J1/3T2/3(logT)1/3 |     |         |     |      |
|        |                |        |     |           |     |                       |     |         | .   | (41) |
Importantly,Equation(41)doesnotrequirethefirmtoknowthenumberorproportionofvisitorsineach
segment in advance. The firm only needs to observe the current visitor’s segment and the corresponding
learning clock n . The factor J1/3 reflects the statistical cost of segment-specific learning: because arm
t
effectiveness may differ across segments, observations cannot generally be pooled across segments.
| D.2. | The regret | bound | under | differential |     | privacy |     |     |     |     |
| ---- | ---------- | ----- | ----- | ------------ | --- | ------- | --- | --- | --- | --- |
We next incorporate differential privacy into the regret analysis. The privacy guarantee itself is established
in Web Appendix B. Here, we use the mapping between the exploration probability ε and the visitor-level
t
privacy-risk parameter ξ . Under the K-ary randomized-response mechanism,
t
K
|     |     |     |     |     | ε   | =       |          | .   |     | (42) |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | ---- |
|     |     |     |     |     |     | t K+eξt | (cid:0)1 |     |     |      |
To make the randomization required by differential privacy coincide with the exploration probability that
| balances | learning | regret, | we equate | Equation | (42) | with     | Equation | (37):    |     |     |
| -------- | -------- | ------- | --------- | -------- | ---- | -------- | -------- | -------- | --- | --- |
|          |          |         |           |          |      | (cid:18) |          | (cid:19) |     |     |
|          |          |         |           |          | K    |          | Klogn    | 1/3      |     |     |
t
|     |     |     |     |       |     | (cid:0)1 = |     | .   |     | (43) |
| --- | --- | --- | --- | ----- | --- | ---------- | --- | --- | --- | ---- |
|     |     |     |     | K+eξt |     |            | n   |     |     |      |
t
| Solving | for ξ | yields |     |     | 2   |     |     | 3   |     |     |
| ------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     |     |     |     |                           | 6   |     | K   | 7           |     |      |
| --- | --- | --- | --- | ------------------------- | --- | --- | --- | ----------- | --- | ---- |
|     |     |     |     | ξ =log41(cid:0)K+(cid:16) |     |     |     | (cid:17) 5. |     | (44) |
t
1/3
Klognt
nt
Thus, the privacy-risk parameter depends on the amount of information accumulated about the current
visitor’s segment, measured by n , rather than on the total number of visitors in the experiment.
t
Substituting Equation (42) into the per-round regret bound in Equation (34) gives
s
|     |     |     | E[R | e (t)](cid:20) | K   |     | 2Klogn | t   |     |     |
| --- | --- | --- | --- | -------------- | --- | --- | ------ | --- | --- | --- |
+2
|     |     |     |     |     | K+eξt | (cid:0)1 | n (cid:1) | K    |     |     |
| --- | --- | --- | --- | --- | ----- | -------- | --------- | ---- | --- | --- |
|     |     |     |     |     |       |          | t         | ξt−1 |     |     |
|     |     |     |     |     |       |          | s K+e     |      |     |     |
(cid:0)1)logn
|     |     |     |     |     | K     |          | 2(K+eξt |     |     |      |
| --- | --- | --- | --- | --- | ----- | -------- | ------- | --- | --- | ---- |
|     |     |     |     | =   |       | +2       |         |     | t.  | (45) |
|     |     |     |     |     | K+eξt | (cid:0)1 |         | n   |     |      |
t
When ξ is set according to Equation (44), the induced exploration probability is
t
|     |     |     |     |     |     | (cid:18) | (cid:19) |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
1/3
Klogn
|     |     |     |     |     | ε   | =   | t   | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | t   | n   |     |     |     |     |
t

52
| Substituting | this value | into | Equation |                    | (45) yields |             |             |      |     |
| ------------ | ---------- | ---- | -------- | ------------------ | ----------- | ----------- | ----------- | ---- | --- |
|              |            |      |          |                    | K1/3(logn   | )1/3        | p K1/3(logn | )1/3 |     |
|              |            |      |          | E[R e (t)](cid:20) |             | t           |             | t    |     |
|              |            |      |          |                    |             |             | +2 2        |      |     |
|              |            |      |          |                    |             | n1/3        |             | n1/3 |     |
|              |            |      |          |                    |             | t           |             | t    |     |
|              |            |      |          |                    |             | p K1/3(logn | )1/3        |      |     |
t
|     |     |     |     |     | =(1+2 | 2)  |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
n1/3
|     |     |     |     |     | (cid:18) |           | t (cid:19) |     |      |
| --- | --- | --- | --- | --- | -------- | --------- | ---------- | --- | ---- |
|     |     |     |     |     |          | K1/3(logn | )1/3       |     |      |
|     |     |     |     |     | =O       |           | t          |     |      |
|     |     |     |     |     |          |           | .          |     | (46) |
n1/3
t
Summing over all visitors and applying the same argument used in Equation (41) gives
|     |     |     |     |           |     | (cid:0)               |     | (cid:1) |      |
| --- | --- | --- | --- | --------- | --- | --------------------- | --- | ------- | ---- |
|     |     |     |     | E[R(T)]=O |     | K1/3J1/3T2/3(logT)1/3 |     | .       | (47) |
Thus, when ξ is chosen such that the randomization required for privacy coincides with the exploration
t
alreadyrequiredbythesegment-specificε-greedypolicy,differentialprivacydoesnotchangetheorderofthe
regret bound. The resulting bound differs from the global-bandit case through the factor J1/3, which arises
| from segment-specific |     | learning |     | rather | than from | differential | privacy. |     |     |
| --------------------- | --- | -------- | --- | ------ | --------- | ------------ | -------- | --- | --- |
This equivalence holds for the privacy schedule in Equation (44). A stricter privacy requirement can force
an exploration probability above the regret-balancing level and therefore increase regret.
| D.3. The | regret | bound | without |     | asymptotic | approximation |     |     |     |
| -------- | ------ | ----- | ------- | --- | ---------- | ------------- | --- | --- | --- |
Equation(34)doesnotrequiretheapproximation1(cid:0)ε (cid:25)1.Retainingtheexploitationprobabilityexplicitly,
t
| the finite-round | regret | bound |     | is  |     |     |     |     |     |
| ---------------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
r
2Klogn
|     |     |     |     |     | E[R e (t)](cid:20)ε | +2(1(cid:0)ε |     | t.  |      |
| --- | --- | --- | --- | --- | ------------------- | ------------ | --- | --- | ---- |
|     |     |     |     |     |                     |              | )   |     | (48) |
|     |     |     |     |     |                     | t            | t n | ε   |      |
t t
Using
K
ε =
|     |     |     |     |     |     | t K+eξt | (cid:0)1 |     |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- |
and
(cid:0)1
eξt
|     |     |     |     |     |     | 1(cid:0)ε = | ,        |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | --- |
|     |     |     |     |     |     | t           | (cid:0)1 |     |     |
K+eξt
| Equation | (48) becomes |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
K
|     |     |     |     | E[R e (t)](cid:20) |       |          |     |     |     |
| --- | --- | --- | --- | ------------------ | ----- | -------- | --- | --- | --- |
|     |     |     |     |                    | K+eξt | (cid:0)1 |     |     |     |
s
|     |     |     |     |     |     | eξt (cid:0)1 | 2(K+eξt | (cid:0)1)logn |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | ------------- | --- |
t.
|     |     |     |     |     | +2    |          |     |     | (49) |
| --- | --- | --- | --- | --- | ----- | -------- | --- | --- | ---- |
|     |     |     |     |     | K+eξt | (cid:0)1 |     | n   |      |
t
Thus,thefinite-roundregretcanbeevaluatedwithoutassumingthat1(cid:0)ε
convergestoone.Thesimpler
t
| bound used | above | follows | directly | from | 1(cid:0)ε | (cid:20)1. |     |     |     |
| ---------- | ----- | ------- | -------- | ---- | --------- | ---------- | --- | --- | --- |
t

53
| Web Appendix |     | E:  | Regret | of the | dynamic | strategy |     |     |     |
| ------------ | --- | --- | ------ | ------ | ------- | -------- | --- | --- | --- |
We next derive the regret of the dynamic privacy strategy under segment-specific learning. Recall that
|     |     |     |     |     | n   | =N (S )+1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
|     |     |     |     |     | t   | t t       |     |     |     |
denotes the number of visitors observed so far in the current visitor’s segment, including visitor t. Thus, n ,
t
rather than the global experiment round t, determines how much the firm has learned about the current
segment. The firm observes n when visitor t arrives and does not need to know how many visitors will
t
ultimately belong to that segment. We cap the per-visitor privacy-risk parameter at a target level γ:
|     |     |     |     |        | 8 2                      |     |     | 39           |      |
| --- | --- | --- | --- | ------ | ------------------------ | --- | --- | ------------ | ---- |
|     |     |     |     |        | ><                       |     |     | >=           |      |
|     |     |     |     |        | 6                        |     |     | K 7          |      |
|     |     |     |     | ξ =min | γ,log41(cid:0)K+(cid:16) |     |     | (cid:17) 5 . | (50) |
|     |     |     |     | t      | >:                       |     |     | 1/3 >;       |      |
Klognt
nt
| Let ε | denote | the exploration |     | probability | implied | by γ: |     |     |     |
| ----- | ------ | --------------- | --- | ----------- | ------- | ----- | --- | --- | --- |
γ
K
|     |     |     |     |     | ε := |     | .   |     | (51) |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
γ K+eγ(cid:0)1
Under the uncapped dynamic schedule, the exploration probability for visitor t is
|     |     |     |     |     |       | (cid:18) | (cid:19) |     |      |
| --- | --- | --- | --- | --- | ----- | -------- | -------- | --- | ---- |
|     |     |     |     |     |       | Klogn    | 1/3      |     |      |
|     |     |     |     |     | εdyn= |          | t        |     |      |
|     |     |     |     |     |       |          |          | .   | (52) |
|     |     |     |     |     | t     | n        |          |     |      |
t
As elsewhere, this expression applies after the finite initialization period and is truncated at one whenever
necessary.
Because the mapping from ξ to ε is decreasing, imposing ξ (cid:20)γ is equivalent to imposing ε (cid:21)ε . Hence,
|            |         |          |     |              |     |         | t       | t γ     |     |
| ---------- | ------- | -------- | --- | ------------ | --- | ------- | ------- | ------- | --- |
| the capped | dynamic | strategy | can | equivalently | be  | written | as      |         |     |
|            |         |          |     |              | K   |         | (cid:8) | (cid:9) |     |
εdyn,ε
|          |       |            |     | ε =       |       | =max     |     | .   | (53) |
| -------- | ----- | ---------- | --- | --------- | ----- | -------- | --- | --- | ---- |
|          |       |            |     | t         | K+eξt | (cid:0)1 | t   | γ   |      |
| E.1. The | local | exhaustion |     | threshold |       |          |     |     |      |
Under segment-specific learning, there is no single experiment-wide exhaustion time at which the privacy
cap begins to bind for all visitors. Instead, define the local exhaustion threshold
|     |     |     |     |     | (   | (cid:18) | (cid:19) | )   |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- |
|     |     |     |     |     |     | Klogn    | 1/3      |     |     |
(cid:20)ε
|     |     |     |     | n γ :=min | n:  |     |     | γ . | (54) |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | ---- |
n
Thus,n isthenumberofobservationswithinasegmentatwhichtheunconstrainedlearningschedulewould
γ
| first require | less | exploration       | than | the privacy | cap    | permits. |     |     |     |
| ------------- | ---- | ----------------- | ---- | ----------- | ------ | -------- | --- | --- | --- |
| Equivalently, |      | on the decreasing |      | region      | n>e, n | solves   |     |     |     |
γ
|     |     |     | (cid:18) |       | (cid:19) |     |     |        |      |
| --- | --- | --- | -------- | ----- | -------- | --- | --- | ------ | ---- |
|     |     |     |          |       | 1/3      |     |     | ε3     |      |
|     |     |     |          | Klogn |          |     |     | logn   |      |
|     |     |     |          | γ     | =ε       | ()  |     | γ = γ. | (55) |
|     |     |     |          | n     |          | γ   |     | n K    |      |
|     |     |     |          | γ     |          |     |     | γ      |      |

54
Because logn/n is strictly decreasing for n>e, the relevant post-initialization solution is unique and can be
| obtained numerically. |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
When all segments share the same K arms and the same privacy cap γ, the local threshold n γ is common
across segments. However, different segments reach this threshold at different experiment-wide times. For
| segment s, | define |     |            |        |                  |     |     |      |
| ---------- | ------ | --- | ---------- | ------ | ---------------- | --- | --- | ---- |
|            |        |     | τ =infft:S | =s and | N (s)+1(cid:21)n | g,  |     | (56) |
|            |        |     | s,γ        | t      | t                | γ   |     |      |
withτ =1ifsegmentsdoesnotreachthethresholdwithintheexperimentalhorizon.Frequentlyobserved
s,γ
segments therefore tend to reach the privacy cap earlier in experiment-wide time, whereas rare segments
| remain on | the unconstrained | learning | schedule | for longer. |     |     |     |     |
| --------- | ----------------- | -------- | -------- | ----------- | --- | --- | --- | --- |
Importantly, the firm does not need to know τ in advance. At each visitor, it determines whether the
s,γ
privacy cap binds simply by comparing the observed local learning clock n with n .
|              |        |     |     |     |     | t   | γ   |     |
| ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| E.2. Pre-cap | regret |     |     |     |     |     |     |     |
Consider visitors for whom the current segment has not yet moved beyond the local exhaustion threshold.
| For these visitors, |     |     |     |          |          |     |     |     |
| ------------------- | --- | --- | --- | -------- | -------- | --- | --- | --- |
|                     |     |     |     | (cid:18) | (cid:19) |     |     |     |
|                     |     |     |     | Klogn    | 1/3      |     |     |     |
t
|     |     |     |     | ε t = | .   |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
n
t
Substituting this expression into the per-round regret bound in Equation (34) gives
|     |     |     |                      |     | (cid:18) (cid:19) |     |     |      |
| --- | --- | --- | -------------------- | --- | ----------------- | --- | --- | ---- |
|     |     |     |                      | p   |                   | 1/3 |     |      |
|     |     |     | e                    |     | Klogn             |     |     |      |
|     |     |     | E[R (t)](cid:20)(1+2 | 2)  | t                 | .   |     | (57) |
n
t
LetJ=jSjdenotethenumberofconsumersegments.Eachsegmentcancontributeatmostn
observations
γ
before moving into the capped region. Hence, the total number of pre-cap observations is at most
|     |     |     |     | minfT,Jn | g.  |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- |
γ
Summing the segment-specific regret terms and applying the same concavity argument used in the general
| regret analysis | yields |     |         |                  |               |     |         |      |
| --------------- | ------ | --- | ------- | ---------------- | ------------- | --- | ------- | ---- |
|                 |        |     | (cid:0) |                  |               |     | (cid:1) |      |
|                 |        | E[R | (T)]=O  | K1/3J1/3minfT,Jn | g2/3(logT)1/3 |     |         |      |
|                 |        | pre |         |                  |               |     | .       | (58) |
γ
This bound requires no knowledge of the eventual number or proportion of visitors in each segment.

55
| E.3. Post-cap | regret |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- |
Once the current segment has moved beyond n , the privacy cap binds and the exploration probability is
γ
fixed at
|               |              |              | ε =ε | .   |     |     |
| ------------- | ------------ | ------------ | ---- | --- | --- | --- |
|               |              |              | t    | γ   |     |     |
| The per-round | regret bound | is therefore |      |     |     |     |
s
|     |     | e   |                | 2Klogn |     |      |
| --- | --- | --- | -------------- | ------ | --- | ---- |
|     |     | E[R | (t)](cid:20) ε | +2     | t . | (59) |
|{γz}
n ε
|     |     |     |     | | {zt | γ } |     |
| --- | --- | --- | --- | ----- | --- | --- |
explorationregret
estimationerror
Let M denote the total number of visitors whose segment-specific learning clock exceeds n during the
| γ   |     |     |     |     | γ   |     |
| --- | --- | --- | --- | --- | --- | --- |
experiment. The cumulative exploration cost after the cap is therefore at most
|     |     |     | M γ ε γ | .   |     |     |
| --- | --- | --- | ------- | --- | --- | --- |
For the estimation-error component, grouping visitors by segment and summing over their local learning
clocks gives
|     |     |     | s r |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
X
|     |     |     | 2K  | logn t |     |     |
| --- | --- | --- | --- | ------ | --- | --- |
2
|     |     |     | ε   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     | γ   | t   |     |     |
t:nt>snγ
p
KJM logT
|     |     |     | (cid:20)4 2 | γ   | .   | (60) |
| --- | --- | --- | ----------- | --- | --- | ---- |
ε
γ
TheinequalityfollowsfromanintegralcomparisonwithineachsegmentandtheCauchy–Schwarzinequality
| across the J | segments. |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- |
Consequently,
s
p
KJM logT
|     |     | E[R  | (T)](cid:20)M ε +4 | 2   | γ . | (61) |
| --- | --- | ---- | ------------------ | --- | --- | ---- |
|     |     | post | γ γ                |     |     |      |
ε
γ
To obtain a bound that does not depend on the realized segment sequence, note that if any visitor enters
the post-cap region, at least n observations must first have been accumulated within some segment. Hence,
γ
|     |     | M (cid:20)(T | (cid:0)n ) , (x) | :=maxfx,0g. |     |     |
| --- | --- | ------------ | ---------------- | ----------- | --- | --- |
|     |     | γ            | γ +              | +           |     |     |
Therefore,
 s
!
|     |     |                    |                 | KJ(T | (cid:0)n ) logT |      |
| --- | --- | ------------------ | --------------- | ---- | --------------- | ---- |
|     |     | E[R (T)](cid:20)(T | (cid:0)n ) ε +O |      | γ + .           | (62) |
|     |     | post               | γ + γ           |      |                 |      |
ε
γ

56
Combining the pre-cap and post-cap components gives the following simple bound for the dynamic strat-
egy:
(cid:0) (cid:1)
|     |     | E[R (T)](cid:20)O | K1/3J1/3minfT,Jn |       | g2/3(logT)1/3 |      |
| --- | --- | ----------------- | ---------------- | ----- | ------------- | ---- |
|     |     | dyn               |                  |       | γ             |      |
|     |     |                   | +(T (cid:0)n     | ) ε   |               |      |
|     |     |                   |                  | γ + γ |               | (63) |
|     |     |                   |  s               |       | !             |      |
(cid:0)n
|     |     |     |     | KJ(T | ) logT |     |
| --- | --- | --- | --- | ---- | ------ | --- |
|     |     |     | +O  |      | γ + .  |     |
ε
γ
The first term captures regret while segments remain on the unconstrained learning schedule. The second
term captures the cumulative cost of the random exploration required after the privacy constraint becomes
binding. The third term captures estimation error during exploitation in the capped region.
A larger value of γ, corresponding to a weaker privacy guarantee, implies a smaller ε . This reduces the
γ
amount of forced random exploration but increases the estimation-error component because fewer obser-
vations are generated through exploration. Conversely, a smaller γ provides stronger privacy protection
and forces more exploration. The dynamic strategy balances these effects by following the regret-balancing
exploration schedule until the privacy cap becomes binding within each segment.
| Web Appendix | F:  | Regret of | the constant | strategy |     |     |
| ------------ | --- | --------- | ------------ | -------- | --- | --- |
Under the constant strategy, the per-visitor privacy-risk parameter is fixed at γ:
(cid:17)γ,
|     |     |     |     | ξ   |     | (64) |
| --- | --- | --- | --- | --- | --- | ---- |
t
| which implies | the constant | exploration | probability |     |     |     |
| ------------- | ------------ | ----------- | ----------- | --- | --- | --- |
K
|     |     |     | ε (cid:17)ε | :=           | .   | (65) |
| --- | --- | --- | ----------- | ------------ | --- | ---- |
|     |     |     | t γ         | K+eγ(cid:0)1 |     |      |
Although the randomization probability is constant across visitors, learning remains segment-specific. For
| visitor t, recall | that |     |      |        |     |     |
| ----------------- | ---- | --- | ---- | ------ | --- | --- |
|                   |      |     | n =N | (S )+1 |     |     |
|                   |      |     | t    | t t    |     |     |
denotes the number of observations accumulated for the current visitor’s segment. Define the clean event
|                 |        | C =fjµ¯ | (cid:0)µ (S | )j(cid:20)r , | 8k2f1,...,Kgg, | (66) |
| --------------- | ------ | ------- | ----------- | ------------- | -------------- | ---- |
|                 |        | t       | k,St k      | t t           |                |      |
| with confidence | radius |         |             |               |                |      |
s
2Klogn
t.
|     |     |     | r t = |     |     | (67) |
| --- | --- | --- | ----- | --- | --- | ---- |
n ε
t γ

57
Using the same concentration argument as in Section ??, expected instantaneous regret satisfies
s
|     |     |     | e                 | 2Klogn |     |      |
| --- | --- | --- | ----------------- | ------ | --- | ---- |
|     |     |     | E[R (t)](cid:20)ε | +2     | t.  | (68) |
|     |     |     |                   | γ n    | ε   |      |
t γ
| Summing | the exploration | component | over all | T visitors gives |     |     |
| ------- | --------------- | --------- | -------- | ---------------- | --- | --- |
Tε .
γ
For the estimation-error component, summing over the segment-specific learning clocks and applying an
| integral comparison | gives |     |     |     |     |     |
| ------------------- | ----- | --- | --- | --- | --- | --- |
|                     |       |     | s   | r   |     |     |
XT
|     |     |     | 2K  | logn |     |     |
| --- | --- | --- | --- | ---- | --- | --- |
t
2
|     |     |     | ε   | n     |     |     |
| --- | --- | --- | --- | ----- | --- | --- |
|     |     |     | γ   | t=1 t |     |     |
s
p
KJTlogT
|     |     |     | (cid:20)4 | 2   | ,   | (69) |
| --- | --- | --- | --------- | --- | --- | ---- |
ε
γ
where the final inequality follows from the Cauchy–Schwarz inequality across the J consumer segments.
| Consequently, | cumulative | regret | under the constant | strategy | satisfies |     |
| ------------- | ---------- | ------ | ------------------ | -------- | --------- | --- |
s
p
KJTlogT
|     |     | E[R | (T)](cid:20)Tε | +4 2 | .   | (70) |
| --- | --- | --- | -------------- | ---- | --- | ---- |
|     |     |     | const          | γ    |     |      |
ε γ
| The first term, |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
Tε ,
γ
is the cumulative cost of random exploration. Because the constant strategy explores with probability ε at
γ
every visitor, this term grows linearly with the experimental horizon for any fixed ε >0.
γ
The second term captures regret from estimation error when exploiting. Importantly, this cost is not
constant.Eventhoughtheprivacyparameterandexplorationprobabilityarefixed,estimationerrordecreases
as the firm accumulates more observations within each segment. The factor J1/2 reflects the statistical cost
of estimating separate arm-specific reward distributions across the J consumer segments.
Unlike the dynamic strategy, the constant strategy does not adapt the amount of randomization to the
amount of information accumulated about the current segment. Consequently, it does not generally achieve
the same regret rate as the segment-specific regret-balancing ε-greedy policy. For a fixed privacy cap, the
| linear exploration | term | Tε eventually | dominates | the cumulative | regret. |     |
| ------------------ | ---- | ------------- | --------- | -------------- | ------- | --- |
γ

58
| Web Appendix |                 | G: Regret |            | of the | dynamic | strategy      |     |       |     |     |     |
| ------------ | --------------- | --------- | ---------- | ------ | ------- | ------------- | --- | ----- | --- | --- | --- |
| We cap       | the per-visitor | privacy   | controller |        | at a    | target budget | γ,  | i.e., |     |     |     |
|              |                 |           |            |        | (       |               |     | !)    |     |     |     |
k
|     |     |     |     | ξ =min | γ,  | log 1(cid:0)k+(cid:0) |     | (cid:1) | .   |     |     |
| --- | --- | --- | --- | ------ | --- | --------------------- | --- | ------- | --- | --- | --- |
|     |     |     |     | t      |     |                       |     | 1/3     |     |     |     |
klogt
t
Let ε denote the exploration probability implied by the cap γ via Equation (12),
γ
k
|     |     |     |     |     | ε   | :=             |     | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | γ k+eγ(cid:0)1 |     |     |     |     |     |
Under the uncapped dynamic schedule in Equation (16), the implied exploration rate is
|     |     |     |     |     |     | (cid:16) | (cid:17) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
1/3
|     |     |     |     |     | εdyn | := klogt |     | .   |     |     |     |
| --- | --- | --- | --- | --- | ---- | -------- | --- | --- | --- | --- | --- |
t
t
Becauseξ7!ε(ξ)isdecreasing,imposingξ (cid:20)γ isequivalenttoimposingε (cid:21)ε .Hencethecappeddynamic
|          |        |            |     |     | t   |     |         |         | t   | γ   |     |
| -------- | ------ | ---------- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- |
| strategy | can be | written as |     |     |     |     |         |         |     |     |     |
|          |        |            |     |     |     | k   | (cid:8) | (cid:9) |     |     |     |
εdyn,
|     |     |     |     | ε t = |       | =max     |     | ε γ . |     |     |     |
| --- | --- | --- | --- | ----- | ----- | -------- | --- | ----- | --- | --- | --- |
|     |     |     |     |       | k+eξt | (cid:0)1 |     | t     |     |     |     |
Let t be the (implicit) exhaustion time, defined as the first round at which the uncapped schedule would
γ
| call for | less exploration | than | the | cap permits, |     | i.e.,        |     |               |     |     |     |
| -------- | ---------------- | ---- | --- | ------------ | --- | ------------ | --- | ------------- | --- | --- | --- |
|          |                  |      |     |              | n   |              |     | o             |     |     |     |
|          |                  |      |     |              |     | t2f1,...,Tg: |     | εdyn(cid:20)ε |     |     |     |
|          |                  |      |     | t :=         | min |              |     |               | ,   |     |     |
|          |                  |      |     | γ            |     |              |     | t γ           |     |     |     |
with the convention that t =T+1 if the set is empty (i.e., if the cap never takes effect within the horizon).
γ
| Equivalently, | t γ | solves |     |          |          |     |     |     |     |     |     |
| ------------- | --- | ------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
|               |     |        |     | (cid:16) | (cid:17) |     |     |     |     |     |     |
ε3
|     |     |     |     |        | 1/3 |       |     | logt   |     |     |      |
| --- | --- | --- | --- | ------ | --- | ----- | --- | ------ | --- | --- | ---- |
|     |     |     |     | klogtγ |     | =ε () |     | γ = γ. |     |     | (71) |
|     |     |     |     | tγ     |     | γ     |     | t k    |     |     |      |
γ
(cid:20)T
Fort>e,thefunctionlogt/tisstrictlydecreasing,sowhent thesolutionisuniqueandcanbeobtained
γ
| numerically | (e.g., | by one-dimensional |     | root | finding). |     |     |     |     |     |     |
| ----------- | ------ | ------------------ | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
(t(cid:20)t
| G.1. Pre-cap |     | regret | ).  |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
(cid:20)
Before we hit the cap, the regret bound follows the optimal ε-greedy regret. For t t , we have ε =
|     |     |     |     |     |     |     |     |     |     | γ   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(klogt/t)1/3. Plugging into Equation (34), the per-round regret up to the cap t becomes:
γ
|     |     |          | (cid:16) | (cid:17) |     | p (cid:16) | (cid:17) | p      | (cid:16) | (cid:17) |     |
| --- | --- | -------- | -------- | -------- | --- | ---------- | -------- | ------ | -------- | -------- | --- |
|     |     |          |          |          | 1/3 |            | 1/3      |        |          | 1/3      |     |
|     |     | E[R˜(t)] | (cid:20) | klogt    | +   | 2 2 klogt  |          | = (1+2 | 2) klogt | .        |     |
|     |     |          |          | t        |     |            | t        |        |          | t        |     |
Summing and using a standard integral comparison, the cumulative regret up to the cap t becomes:
γ
Xtγ
|     |     |     |     |     | E[R˜(t)] | ≲ k1/3t2/3(logt |     | )1/3. |     |     | (72) |
| --- | --- | --- | --- | --- | -------- | --------------- | --- | ----- | --- | --- | ---- |
γ
γ
t=1

59
| G.2. Post-cap |     | regret |     | (t>t | ).  |     |     |     |     |     |     |     |
| ------------- | --- | ------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
Fort>t ,theexplorationprobabilityε =ε isconstant.Fromtheper-roundregretboundinEquation(34),
|     | γ   |     |     |     | t   | γ   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
we have
s
|     |     |     |     | E[R˜(t)] |          |       |     | 2klogt |     |     |     |     |
| --- | --- | --- | --- | -------- | -------- | ----- | --- | ------ | --- | --- | --- | --- |
|     |     |     |     |          | (cid:20) | ε     | +   | 2      |     | .   |     |     |
|     |     |     |     |          |          | |{γz} |     |        | tε  |     |     |     |
γ
|     |     |     |     |     |     |     |     | | {z | }   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
explorationregret
estimation(exploitation)regret
| Summing | over | t=t | +1,...,T | gives |     |     |     |     |     |     |     |     |
| ------- | ---- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
|     |     |     |     |     |          |                      |      | s   | r   |      |     |      |
| --- | --- | --- | --- | --- | -------- | -------------------- | ---- | --- | --- | ---- | --- | ---- |
|     |     |     |     | XT  |          |                      |      |     | XT  |      |     |      |
|     |     |     |     |     |          |                      |      | 2k  |     | logt |     |      |
|     |     |     |     |     | E[R˜(t)] | (cid:20) (T (cid:0)t | )ε + | 2   |     | .    |     | (73) |
|     |     |     |     |     |          |                      | γ γ  | ε   |     | t    |     |      |
γ
|     |     |     |     | t=tγ+1 |     |     |     | t=tγ+1 |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | ------ | --- | --- | --- | --- |
We now upper bound the summation term which bounds the exploitation regret to:
r
XT
logt
|     |     |     |     |     |     | S:= |     | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
t=tγ+1
t(cid:20)T
| Since logt | is monotone |     | increasing, |     | for all | we  | have |     |     |     |     |     |
| ---------- | ----------- | --- | ----------- | --- | ------- | --- | ---- | --- | --- | --- | --- | --- |
r
|     |     |     |     |     |     | logt | p        | 1        |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | -------- | -------- | --- | --- | --- | --- |
|     |     |     |     |     |     |      | (cid:20) | (cid:1)p |     |     |     |     |
|     |     |     |     |     |     |      | logT     | .        |     |     |     |     |
|     |     |     |     |     |     | t    |          | t        |     |     |     |     |
Hence,
Z
|     |     |     |            | p    | XT  | p        |      | p     |      | (cid:0)p p | (cid:1) |     |
| --- | --- | --- | ---------- | ---- | --- | -------- | ---- | ----- | ---- | ---------- | ------- | --- |
|     |     |     |            |      | 1   |          | T    | dx    |      |            |         |     |
|     |     |     | S (cid:20) | logT | p   | (cid:20) | logT | p = 2 | logT | T (cid:0)  | t .     |     |
γ
|     |     |     |     |     |        | t   |     | x   |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | t=tγ+1 |     | tγ  |     |     |     |     |     |
Therefore,
|     |     |     |     |     |     | p          | (cid:0)p | p (cid:1)   |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ----------- | --- | --- | --- | ---- |
|     |     |     |     |     | S   | (cid:20) 2 | logT T   | (cid:0) t . |     |     |     | (74) |
γ
| Substituting | the | bound | from | (74) | into Equation |     | (73) yields |     |     |     |     |     |
| ------------ | --- | ----- | ---- | ---- | ------------- | --- | ----------- | --- | --- | --- | --- | --- |
s
|     |     |     |     |          |             |             |     | (cid:16) |          |             | (cid:1)(cid:17) |     |
| --- | --- | --- | --- | -------- | ----------- | ----------- | --- | -------- | -------- | ----------- | --------------- | --- |
|     |     |     | XT  |          |             |             |     | p        | (cid:0)p | p           |                 |     |
|     |     |     |     | E[R˜(t)] |             |             | 2k  |          |          |             |                 |     |
|     |     |     |     |          | (cid:20) (T | (cid:0)t )ε | + 2 | 2 logT   |          | T (cid:0) t | .               |     |
|     |     |     |     |          |             | γ           | γ ε |          |          | γ           |                 |     |
γ
t=tγ+1
| Simplifying | constants |     | gives    | the | final result: |          |     |          |         |          |          |      |
| ----------- | --------- | --- | -------- | --- | ------------- | -------- | --- | -------- | ------- | -------- | -------- | ---- |
|             |           |     |          |     |               |          |     |  s       |         |          | !        |      |
|             |           | XT  |          |     |               |          |     | (cid:16) |         |          | (cid:17) |      |
|             |           |     |          |     |               |          |     | k        | p       | p p      |          |      |
|             |           |     | E[R˜(t)] |     | (cid:20)      | (cid:0)t | O   |          | (cid:0) |          |          |      |
|             |           |     |          |     | (T            | )ε       | +   | (        | T       | t ) logT | .        | (75) |
|             |           |     |          |     | |             | {zγ γ}   |     | ε        |         | γ        |          |      |
γ
|     |     | t=tγ+1 |     |     |     |     | |   |     | {z  |     | }   |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
explorationcost(linear)
estimationerror(sublinear)
The first (linear) term, (T (cid:0)t )ε represents the cumulative cost of random exploration: each round
γ γ
explores with probability ε , and each random arm pull incurs at most unit regret. The second (sublinear)
γ
termarisesfromestimationerrorwhenexploiting.Evenwhenthebanditchoosesgreedilyproducingexpected
(cid:0)q
(cid:1)
instantaneousregretoforderO klogt .Summingthesedecayingerrorsyieldsasublineartermproportional
tεγ
p
(cid:0)t
to (T γ )logT. Thus, larger privacy budgets γ (smaller ε γ ) reduce the exploration cost but inflate the
| estimation | error | term, | illustrating |     | the privacy–exploration–regret |     |     | trade-off. |     |     |     |     |
| ---------- | ----- | ----- | ------------ | --- | ------------------------------ | --- | --- | ---------- | --- | --- | --- | --- |

60
| Web Appendix    |     | H:         | Regret | of     | the         | constant | strategy |     |     |     |     |     |
| --------------- | --- | ---------- | ------ | ------ | ----------- | -------- | -------- | --- | --- | --- | --- | --- |
| Let the privacy |     | controller | be     | capped | constantly, |          |          |     |     |     |     |     |
k
|            |       |       |          |      | (cid:17)γ | =)  |     | (cid:17)ε |              |     |     |     |
| ---------- | ----- | ----- | -------- | ---- | --------- | --- | --- | --------- | ------------ | --- | --- | --- |
|            |       |       |          | ξ    |           |     | ε   | :=        |              | .   |     |     |
|            |       |       |          | t    |           |     | t   | γ         | k+eγ(cid:0)1 |     |     |     |
| Define the | clean | event | at round | t by |           |     |     |           |              |     |     |     |
s
|     |     |     |     | (cid:8) |     |     |     | (cid:9) |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- |
2klogt
|     |     |     | C   | :=  | jµ¯ (cid:0)µ | j(cid:20)r , | 8a2[k] | ,   | r   | :=  | ,   |     |
| --- | --- | --- | --- | --- | ------------ | ------------ | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | t   | a            | a t          |        |     | t   |     |     |     |
tε
γ
| so that by | Hoeffding | and | a union | bound |     |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
s
2klogt
|     |     |     |     |     | E[R˜(t)] |     | (cid:20) ε + | 2   |     |     |     | (76) |
| --- | --- | --- | --- | --- | -------- | --- | ------------ | --- | --- | --- | --- | ---- |
γ
tε
γ
| Consequently, | the | cumulative |     | regret | satisfies |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
s
|     |     |     |     |     |     |     |     | p   |     | p   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
|     |     |     |     | E[R(T)] | (cid:20) | Tε  |     | + 4 | 2   | TlogT |     |     |
| --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- | ----- | --- | --- |
|{zγ}
ε
|     |     |     |     |     |     |     |     | |   |     | γ{z | }   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
costofexploration
costofexploitation
Here we do not match the regret bound that “standard” ε-greedy introduces, because the exploration and
| exploitation | do  | not adapt | over | t.  |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Intermsofcostofexploration,withaconstantprivacycapξ (cid:17)γ,youexploreeachroundwithprobability
t
ε . Every exploratory pull can be suboptimal and costs at most 1 unit of regret, so you pay on average ε
| γ   |     |     |     |     |     |     |     |     |     |     |     | γ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
per round, adding up linearly to Tε over T rounds. The cost of exploitation is also constant.
γ
| Web Appendix  |          | I:           | Privacy | risk     | budget   |     | elasticities |         |           |     |     |     |
| ------------- | -------- | ------------ | ------- | -------- | -------- | --- | ------------ | ------- | --------- | --- | --- | --- |
| We first      | consider | the constant |         | strategy | followed |     | by the       | dynamic | strategy. |     |     |     |
| I.1. Constant |          | privacy      | risk    | strategy |          |     |              |         |           |     |     |     |
Let
s
|     |     |     |       | k            |     |                |     |     | p   | k    | p      |     |
| --- | --- | --- | ----- | ------------ | --- | -------------- | --- | --- | --- | ---- | ------ | --- |
|     |     |     | ε(γ)= |              | ,   | R(T,γ)=Tε(γ)+4 |     |     |     | 2    | TlogT. |     |
|     |     |     |       | k+eγ(cid:0)1 |     |                |     |     |     | ε(γ) |        |     |
p p
| Define D:=4 |     | 2 kTlogT, |     | so that |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Tε+Dε−1/2.
R =
| We seek | the point | elasticity |     | of R with | respect | to  | γ:   |     |     |     |     |     |
| ------- | --------- | ---------- | --- | --------- | ------- | --- | ---- | --- | --- | --- | --- | --- |
|         |           |            |     |           |         |     | dlnR | γ   | dR  |     |     |     |
|         |           |            |     |           | E       | =   |      | =   | .   |     |     |     |
R,γ
|     |     |     |     |     |     |     | dlnγ | R   | dγ  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |

61
| By the | chain rule, |     |     |     |     |     |               |     |     |     |     |
| ------ | ----------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
|        |             |     |     |     |     | dR  | dR (cid:1) dε |     |     |     |     |
=
|              |               |       |            |              |          | dγ              | dε dγ            |                 |     |                |     |
| ------------ | ------------- | ----- | ---------- | ------------ | -------- | --------------- | ---------------- | --------------- | --- | -------------- | --- |
| We therefore | obtain        | the   | following  |              |          |                 |                  |                 |     |                |     |
|              |               |       |            | (cid:16)     | (cid:17) |                 |                  |                 |     |                |     |
|              |               | dε    | d          | k            |          |                 | keγ              | dR              |     | D              |     |
|              |               |       | =          |              | =(cid:0) |                 |                  | ,               | =T  | (cid:0) ε−3/2. |     |
|              |               |       |            | k+eγ(cid:0)1 |          | (k+eγ(cid:0)1)2 |                  |                 |     |                |     |
|              |               | dγ    | dγ         |              |          |                 |                  | dε              |     | 2              |     |
| Plugging     | these results | back  | in         |              |          |                 |                  |                 |     |                |     |
|              |               |       |            |              |          | (cid:16)        | (cid:17)(cid:16) |                 |     | (cid:17)       |     |
|              |               |       | dR         | dR           | dε       |                 | D                |                 | keγ |                |     |
|              |               |       |            |              | (cid:1)  | (cid:0)         | ε−3/2            | (cid:0)         |     |                |     |
|              |               |       |            | =            | =        | T               |                  |                 |     | ,              |     |
|              |               |       |            | dγ dε        | dγ       |                 | 2                | (k+eγ(cid:0)1)2 |     |                |     |
| Using the    | definition    | of an | elasticity |              |          |                 |                  |                 |     |                |     |
|              |               |       |            |              |          | (cid:16)        |                  | (cid:17)        |     |                |     |
|              |               |       |            | γ            | dR       | γ               | D                |                 | keγ |                |     |
|              |               |       | E          | =            | =(cid:0) |                 | T (cid:0) ε−3/2  |                 |     | .              |     |
|              |               |       |            | R,γ          |          |                 |                  | (k+eγ(cid:0)1)2 |     |                |     |
|              |               |       |            | R            | dγ       | R               | 2                |                 |     |                |     |
|              |               |       | q          |              |          | (cid:16)        | (cid:17)         |                 |     |                |     |
3/2
|       |        | ε−1/2= |     | k+eγ−1, | ε−3/2= | k+eγ−1 |     |             |     |     |     |
| ----- | ------ | ------ | --- | ------- | ------ | ------ | --- | ----------- | --- | --- | --- |
| Using | ε= k   | ,      |     |         |        |        |     | , we obtain |     |     |     |
|       | k+eγ−1 |        |     | k       |        |        | k   |             |     |     |     |
|       |        |        |     |         |        | p      | p   | p           |     |     |     |
Tk
|     |     |     |     | R=  |     | +4  | 2 TlogT | k+eγ(cid:0)1, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --- | --- |
k+eγ(cid:0)1
|          |           |                |                  |                   |            | p       | p       |              |              |          |           |
| -------- | --------- | -------------- | ---------------- | ----------------- | ---------- | ------- | ------- | ------------ | ------------ | -------- | --------- |
|          |           |                |                  |                   |            |         |         | (cid:0)      |              | (cid:1)  |           |
|          |           |                |                  | D                 |            | 2       | 2 TlogT |              |              | 3/2      |           |
|          |           |                |                  | T (cid:0) ε−3/2=T |            | (cid:0) |         | k+eγ(cid:0)1 |              | .        |           |
|          |           |                |                  | 2                 |            |         | k       |              |              |          |           |
| Finally, | we obtain | the elasticity |                  |                   |            |         |         |              |              |          |           |
|          |           |                |                  |                   | (cid:16)   |         |         |              |              | (cid:17) |           |
|          |           |                |                  |                   |            | p       | p       | (cid:0)      | (cid:1)      |          |           |
|          |           |                |                  |                   | Tk(cid:0)2 |         |         | k+eγ(cid:0)1 |              | 3/2      |           |
|          |           |                |                  | γeγ               |            |         | 2 TlogT |              |              |          |           |
|          |           | E              | =(cid:0)(cid:18) |                   |            |         |         |              | (cid:19)     |          |           |
|          |           |                |                  |                   |            | p p     | p       |              | (cid:0)      |          | (cid:1) . |
|          |           | R,γ            |                  | Tk                |            |         |         |              |              |          |           |
|          |           |                |                  |                   | +4         | 2 TlogT |         | k+eγ(cid:0)1 | k+eγ(cid:0)1 |          | 2         |
k+eγ(cid:0)1
| I.2. Elasticity |     | of the | dynamic | privacy |     | risk strategy |     |     |     |     |     |
| --------------- | --- | ------ | ------- | ------- | --- | ------------- | --- | --- | --- | --- | --- |
We next derive the elasticity of the regret bound under the capped dynamic privacy risk strategy. Recall
| that the | exploration | probability |     | implied | by the | privacy | risk | cap is |     |     |     |
| -------- | ----------- | ----------- | --- | ------- | ------ | ------- | ---- | ------ | --- | --- | --- |
k
|     |     |     |     |     |     | ε = |     | ,   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ k+eγ(cid:0)1
| and that | the exhaustion |     | time | t is implicitly |     | defined | by  |     |     |     |     |
| -------- | -------------- | --- | ---- | --------------- | --- | ------- | --- | --- | --- | --- | --- |
γ
|     |     |     |     |     |     | logt | ε3  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
γ γ.
= (77)
|     |     |     |     |     |     | t   | k   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
Let
|     |     |     |     |     |        | p   |         | p   |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ------- | --- | --- | --- | --- |
|     |     |     |     |     | A:=1+2 |     | 2, B:=4 | 2.  |     |     |     |

62
Using the pre-cap regret bound and the post-cap summation bound, the cumulative regret can be approxi-
mated by
|     |     |     | R   | (T,γ)= | Ak1/3t2/3(logt |     |      | )1/3 |     |     |
| --- | --- | --- | --- | ------ | -------------- | --- | ---- | ---- | --- | --- |
|     |     |     |     | dyn    | |              | γ   | {z γ | }    |     |     |
pre-capregret
|     |     |     |     |     | +   | (T  | (cid:0)t )ε |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     |     |     |     |     |     | |   | {zγ         | γ}  |     |     |
(78)
posst-capexplorationcost
|     |     |     |     |     |     |     | (cid:16)p | p   | (cid:17)p |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | --- |
k
|     |     |     |     |     | +B  |     | T   | (cid:0) t | logT. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- |
γ
ε
|     |     |     |     |     |     | |   | γ   | {z  | }   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
post-capestimationerror
Both ε and t depend on the privacy risk budget γ. Therefore, the total derivative of regret is
| γ        | γ             |     |             |     |              |                 |       |     |     |      |
| -------- | ------------- | --- | ----------- | --- | ------------ | --------------- | ----- | --- | --- | ---- |
|          |               |     |             | dR  |              | ∂R              | dt ∂R |     | dε  |      |
|          |               |     |             |     | dyn          | dyn             | γ     | dyn | γ.  |      |
|          |               |     |             |     | =            |                 | +     |     |     | (79) |
|          |               |     |             | dγ  |              | ∂t              | dγ    | ∂ε  | dγ  |      |
|          |               |     |             |     |              | γ               |       | γ   |     |      |
| We first | differentiate | the | exploration |     | probability: |                 |       |     |     |      |
|          |               |     |             |     | dε           |                 | keγ   |     |     |      |
|          |               |     |             |     | γ            | =(cid:0)        |       | .   |     | (80) |
|          |               |     |             |     | dγ           | (k+eγ(cid:0)1)2 |       |     |     |      |
To obtain the derivative of the exhaustion time, differentiate Equation (77) with respect to γ. Since
|     |     |     |     |     | (cid:18) | (cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
1(cid:0)logt
|     |     |     |     |     | d   | logt |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |     |      | =   | ,   |     |     |
|     |     |     |     |     | dt  | t    | t2  |     |     |     |
we obtain
|     |     |     |     |     | 1(cid:0)logt |     | 3ε2 |      |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | ---- | --- | --- |
|     |     |     |     |     |              | dt  |     | dε   |     |     |
|     |     |     |     |     |              | γ   | γ = | γ γ. |     |     |
t2
|     |     |     |     |     |     | dγ  | k   | dγ  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
Thus,
|     |     |     |     |     | dt  | 3ε2 | dε t2           |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---- |
|     |     |     |     |     | γ   | γ   | γ               | γ   |     |      |
|     |     |     |     |     | =   |     |                 | .   |     | (81) |
|     |     |     |     |     | dγ  | k   | dγ 1(cid:0)logt |     |     |      |
γ
We next calculate the partial derivative of regret with respect to t . Differentiating Equation (78) gives
γ
|     |     |     |     |             |         | (cid:20) |             |     | (cid:21)    |      |
| --- | --- | --- | --- | ----------- | ------- | -------- | ----------- | --- | ----------- | ---- |
|     |     |     | ∂R  |             |         | 2        |             | 1   |             |      |
|     |     |     | dyn | =Ak1/3t−1/3 |         |          | (logt )1/3+ |     | (logt )−2/3 |      |
|     |     |     | ∂t  |             | γ       | 3        | γ           | 3   | γ           |      |
|     |     |     |     | γ           |         | s        |             |     |             |      |
|     |     |     |     |             |         |          | p           |     |             | (82) |
|     |     |     |     |             | B       | k        | logT        |     |             |      |
|     |     |     |     | (cid:0)ε    | (cid:0) |          | p           | .   |             |      |
γ
|             |            |      |         |     | 2               | ε   | t           |     |     |     |
| ----------- | ---------- | ---- | ------- | --- | --------------- | --- | ----------- | --- | --- | --- |
|             |            |      |         |     |                 | γ   | γ           |     |     |     |
| The partial | derivative | with | respect | to  | the exploration |     | probability |     | is  |     |
∂R
|     |     |     |     | dyn | (cid:0)t |     |           |     |           |      |
| --- | --- | --- | --- | --- | -------- | --- | --------- | --- | --------- | ---- |
|     |     |     |     | =(T |          | )   |           |     |           |      |
|     |     |     |     | ∂ε  |          | γ   |           |     |           |      |
|     |     |     |     | γ   |          |     |           |     |           | (83) |
|     |     |     |     |     | p        |     | (cid:16)p | p   | (cid:17)p |      |
B
|     |     |     |     |     | (cid:0) | kε−3/2 |     | (cid:0) |       |     |
| --- | --- | --- | --- | --- | ------- | ------ | --- | ------- | ----- | --- |
|     |     |     |     |     |         |        | T   | t γ     | logT. |     |
|     |     |     |     |     | 2       | γ      |     |         |       |     |

63
| Substituting |     | Equations | (80), | (81),        | (82), | and      | (83) into | Equation | (79)        | gives    |     |     |
| ------------ | --- | --------- | ----- | ------------ | ----- | -------- | --------- | -------- | ----------- | -------- | --- | --- |
|              |     |           |       | (            |       | (cid:20) |           |          |             | (cid:21) |     |     |
|              |     |           | dR    |              |       | 2        |           | 1        |             |          |     |     |
|              |     |           | dyn   | = Ak1/3t−1/3 |       |          | (logt     | )1/3+    | (logt )−2/3 |          |     |     |
|              |     |           |       |              |       |          | γ         |          | γ           |          |     |     |
|              |     |           | dγ    |              |       | γ 3      |           | 3        |             |          |     |     |
|              |     |           |       |              |       | s        |           | )        |             |          |     |     |
p
|     |     |     |     |     |          | B       | k   | logT dt |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | ------- | --- | ------- | --- | --- | --- | ---- |
|     |     |     |     |     | (cid:0)ε | (cid:0) | p   |         | γ   |     |     | (84) |
γ
|     |     |     |     |     |          | 2        | ε        | t         | dγ      |           |       |     |
| --- | --- | --- | --- | --- | -------- | -------- | -------- | --------- | ------- | --------- | ----- | --- |
|     |     |     |     |     | (        |          | γ        | γ         |         |           | )     |     |
|     |     |     |     |     |          |          |          | (cid:16)p |         | (cid:17)p |       |     |
|     |     |     |     |     |          |          | p        |           | p       |           |       |     |
|     |     |     |     |     | (cid:0)t | )(cid:0) | B kε−3/2 |           | (cid:0) |           | dε γ. |     |
|     |     |     |     | +   | (T       |          |          |           | T t     | logT      |       |     |
|     |     |     |     |     |          | γ        | 2        | γ         |         | γ         | dγ    |     |
The point elasticity of dynamic-strategy regret with respect to the privacy risk budget is therefore
|     |     |     |     |       |     |     | (cid:20) |       |       |     | (cid:21) |      |
| --- | --- | --- | --- | ----- | --- | --- | -------- | ----- | ----- | --- | -------- | ---- |
|     |     |     |     |       |     | γ   | ∂R       | dt    | ∂R    | dε  |          |      |
|     |     |     |     | Edyn= |     |     |          | dyn γ | + dyn | γ   | .        | (85) |
R,γ
|     |     |     |     |     | R   | dyn (T,γ) | ∂t  | γ dγ | ∂ε γ | dγ  |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---- | ---- | --- | --- | --- |
The elasticity captures two channels through which an increase in the privacy risk budget affects regret.
First,increasingγ lowersε ,reducingtheamountofrandomexplorationafterthecapbinds.Second,increas-
γ
ing γ delays the exhaustion time t , extending the period during which the uncapped dynamic schedule
γ
applies. These effects also influence the estimation-error component because the number of post-cap obser-
| vations | and the | amount | of  | post-cap | exploration |     | change | simultaneously. |     |     |     |     |
| ------- | ------- | ------ | --- | -------- | ----------- | --- | ------ | --------------- | --- | --- | --- | --- |
A negative elasticity implies that increasing the privacy risk budget reduces regret, whereas a positive
elasticityimpliesthatincreasingthebudgetraisesregret.Thesignthereforedependsonthebalancebetween
the reduction in exploration cost, the change in the exhaustion time, and the resulting change in estimation
error.
| If the | cap does | not | become | binding | within | the | horizon, | then     |     |     |     |     |
| ------ | -------- | --- | ------ | ------- | ------ | --- | -------- | -------- | --- | --- | --- | --- |
|        |          |     |        |         |        |     | (cid:18) | (cid:19) |     |     |     |     |
1/3
klogT
|     |     |     |     |     |     | ε   | (cid:20) |     | ,   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
γ
T
and the dynamic exploration schedule is independent of γ over all rounds t(cid:20)T. In this case,
|     |     |     |     |     |     |     | Edyn=0. |     |     |     |     | (86) |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ---- |
R,γ
| Web Appendix |     | J:  | Heterogeneity |     |     | in privacy |     | risk | among | arms |     |     |
| ------------ | --- | --- | ------------- | --- | --- | ---------- | --- | ---- | ----- | ---- | --- | --- |
Sofar,weapplythesameprivacyguaranteetoeveryarm.Thiscorrespondstothestandardε-greedypolicy,
where the mechanism exploits the greedy arm with probability 1(cid:0)ε and explores uniformly over all arms
with probability ε. Because exploration is typically spread equally across arms, each arm receives the same
privacy guarantee.
Anextensionistoallowprivacyguaranteestodifferacrossarms.Thisisusefulwhensomearmsareviewed
as more privacy-sensitive than others. Let ξ >0 denote the privacy parameter associated with displayed
j

64
arm j. A smaller value of ξ gives arm j stronger privacy protection, while a larger value allows arm j to be
j
more informative.
Toconnectarm-specificprivacyguaranteestoε-greedy,wekeepthesameexploitation-explorationstructure
but replace uniform exploration with weighted exploration. Specifically, at visitor t, the mechanism selects
8
>>>><a
|     |     |     |     | =argmax            |     | Q (a), | with probability    | 1(cid:0)ε, |      |
| --- | --- | --- | --- | ------------------ | --- | ------ | ------------------- | ---------- | ---- |
|     |     |     |     | t                  |     | a t    |                     |            |      |
|     |     |     | a∗= |                    |     |        |                     |            | (87) |
|     |     |     | t   | >>>>:Categorical(w |     |        |                     |            |      |
|     |     |     |     |                    |     | ,...,w | ), with probability | ε,         |      |
|     |     |     |     |                    |     | 1 k    |                     |            |      |
P
where w (cid:21)0 and k w =1. Under the weighted ε-greedy policy in Equation (87), the probability of
|            | j     | j=1  | j          |     |         |     |     |     |     |
| ---------- | ----- | ---- | ---------- | --- | ------- | --- | --- | --- | --- |
| displaying | arm j | when | the greedy | arm | is l is |     |     |     |     |
8
>>>><1(cid:0)ε+εw
|     |     |     |     |     |     |     | , if | j=l, |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
j
|     |     |     | p   | =Pr(a∗=jja |     | =l)= |         |       | (88) |
| --- | --- | --- | --- | ---------- | --- | ---- | ------- | ----- | ---- |
|     |     |     |     | jl         | t   | t    | >>>>:εw |       |      |
|     |     |     |     |            |     |      | , if    | j6=l. |      |
j
ThediagonalentryinEquation(88)correspondstothecaseinwhichthedisplayedarmequalsthegreedy
arm. In this case, arm j is displayed either because the policy exploits, with probability 1(cid:0)ε, or because
the policy explores and draws arm j, with probability εw . The off-diagonal entries correspond to cases in
j
which the displayed arm differs from the greedy arm. In those cases, arm j can be displayed only through
| exploration, | with | probability | εw  | .   |     |     |     |     |     |
| ------------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
j
| To give | displayed | arm | j its own | privacy | upper | bound | ξ , we require |     |     |
| ------- | --------- | --- | --------- | ------- | ----- | ----- | -------------- | --- | --- |
j
p
|     |     |     |     |     | jj  | =eξj | for all l6=j. |     | (89) |
| --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ---- |
p
jl
| Substituting | Equation |     | (88) into | Equation | (89) | gives |     |     |     |
| ------------ | -------- | --- | --------- | -------- | ---- | ----- | --- | --- | --- |
1(cid:0)ε+εw
j
|     |     |     |     |     |     |     | =eξj. |     | (90) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---- |
εw
j
| Rearranging | Equation |     | (90) yields |     |              |     |                 |     |      |
| ----------- | -------- | --- | ----------- | --- | ------------ | --- | --------------- | --- | ---- |
|             |          |     |             |     | 1(cid:0)ε=εw |     | (eξj (cid:0)1), |     | (91) |
j
and therefore
1(cid:0)ε
|     |     |     |     |     |     | εw =  | .        |     | (92) |
| --- | --- | --- | --- | --- | --- | ----- | -------- | --- | ---- |
|     |     |     |     |     |     | j eξj | (cid:0)1 |     |      |
Equation (92) shows how privacy and exploration are linked. If ξ is small, then eξj (cid:0)1 is small, so εw
|     |     |     |     |     |     |     | j   |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
must be large. Thus, more privacy-sensitive arms are sampled more often during exploration, which makes
observing those arms less informative to an external observer. Summing Equation (92) over all arms gives
|     |     |     |     |     | Xk  | Xk   | 1(cid:0)ε |     |      |
| --- | --- | --- | --- | --- | --- | ---- | --------- | --- | ---- |
|     |     |     |     |     |     | εw = | .         |     | (93) |
|     |     |     |     |     |     | j    | (cid:0)1  |     |      |
eξj
|     |     |     |     |     | j=1 | j=1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

65
P
| Since | k w   | =1, the | left-hand |     | side of | Equation | (93) | equals | ε. Hence, |     |     |     |
| ----- | ----- | ------- | --------- | --- | ------- | -------- | ---- | ------ | --------- | --- | --- | --- |
|       | j=1 j |         |           |     |         |          |      |        |           |     |     |     |
Xk
1
|     |     |     |     |     |     | ε=(1(cid:0)ε) |     |     | .        |     |     | (94) |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | -------- | --- | --- | ---- |
|     |     |     |     |     |     |               |     | eξj | (cid:0)1 |     |     |      |
j=1
| Solving | Equation | (94) | for | ε yields |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
P
k 1
|     |     |     |     |     |     |     | Pj=1 | eξj−1 |     |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- | ---- |
|     |     |     |     |     |     | ε=  |      |       | .   |     |     | (95) |
k
|     |     |     |     |     |     |     | 1+  |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j=1 eξj−1
| The corresponding |     | exploration |     | weights |     | are |     |     |     |     |     |     |
| ----------------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |     |     |     |     | P   | eξj−1 |     |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ---- |
|     |     |     |     |     |     | w   | j = |       | .   |     |     | (96) |
|     |     |     |     |     |     |     | k   | 1     |     |     |     |      |
m=1 eξm−1
Therefore, the weighted ε-greedy policy that implements arm-specific privacy guarantees is
8
>>>>>><
|     |     |     |                      |     |     |      |      |             | 1(cid:0)ε= | 1    |       |      |
| --- | --- | --- | -------------------- | --- | --- | ---- | ---- | ----------- | ---------- | ---- | ----- | ---- |
|     |     |     | a =argmax            |     | Q   | (a), | with | probability |            | P    | ,     |      |
|     |     |     | t                    |     | a   | t    |      |             |            | 1+ k | 1     |      |
|     |     |     |                      |     |     |      |      |             |            | m=1  | eξm−1 |      |
|     |     | a∗= |                      |     |     |      |      |             |            |      |       | (97) |
|     |     | t   | >>>>>>:Categorical(w |     |     |      |      |             |            | P    |       |      |
k 1
P m=1 eξm −1
|     |     |     |     |     | 1 ,...,w | k   | ), with | probability | ε=  |      | .   |     |
| --- | --- | --- | --- | --- | -------- | --- | ------- | ----------- | --- | ---- | --- | --- |
|     |     |     |     |     |          |     |         |             |     | 1+ k | 1   |     |
m=1 eξm−1
| Equivalently, |     | substituting |     | Equations |     | (95) and | (96) | into Equation | (88) | gives |     |     |
| ------------- | --- | ------------ | --- | --------- | --- | -------- | ---- | ------------- | ---- | ----- | --- | --- |
8
>>>>>>><(eξj
|     |     |     |     |     |          |           | eξ         | j         |          |         |     |      |
| --- | --- | --- | --- | --- | -------- | --------- | ---------- | --------- | -------- | ------- | --- | ---- |
|     |     |     |     |     |          |           | (cid:16) P |           | (cid:17) | if j=l, |     |      |
|     |     |     |     |     |          | (cid:0)1) | 1+         | k         | 1        |         |     |      |
|     |     |     |     |     |          |           |            | m=1 eξm−1 |          |         |     |      |
|     |     |     |     | p   | =        |           |            |           |          |         |     | (98) |
|     |     |     |     | jl  | >>>>>>>: |           |            |           |          |         |     |      |
1
|          |           |     |     |             |     |                | (cid:16) |           | (cid:17) | j6=l. |     |      |
| -------- | --------- | --- | --- | ----------- | --- | -------------- | -------- | --------- | -------- | ----- | --- | ---- |
|          |           |     |     |             |     |                | P        |           |          | if    |     |      |
|          |           |     |     |             |     | (eξj (cid:0)1) | 1+       | k         | 1        |       |     |      |
|          |           |     |     |             |     |                |          | m=1 eξm−1 |          |       |     |      |
| For each | displayed |     | arm | j, Equation |     | (88) implies   |          |           |          |       |     |      |
|          |           |     |     |             | p   | 1(cid:0)ε+εw   |          |           |          |       |     |      |
|          |           |     |     |             | jj  |                | j        |           | l6=j.    |       |     |      |
|          |           |     |     |             | =   |                | =eξj     |           | for all  |       |     | (99) |
|          |           |     |     |             | p   | εw             |          |           |          |       |     |      |
|          |           |     |     |             | jl  |                | j        |           |          |       |     |      |
Thus,
p
|     |     |     |     |     |     |     | maxlog | jl =ξ | .   |     |     | (100) |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     | l,l′   | p     | j   |     |     |       |
jl′
Hence, observing displayed arm j has privacy loss bounded by ξ j . The overall differential-privacy guarantee
| of the mechanism |     | is  | governed | by  | the largest |     | arm-specific | privacy | parameter: |     |     |       |
| ---------------- | --- | --- | -------- | --- | ----------- | --- | ------------ | ------- | ---------- | --- | --- | ----- |
|                  |     |     |          |     |             |     | ξglobal=maxξ |         | .          |     |     | (101) |
j
j
| Thus, the | mechanism |     | is max | ξ -differentially |     |     | private. |     |     |     |     |     |
| --------- | --------- | --- | ------ | ----------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
j j

66
J.1. Numerical example
Consider an experiment with K=3 arms and arm-specific privacy parameters
ξ =0.5, ξ =1, ξ =2.
1 2 3
Because smaller values of ξ correspond to stronger privacy protection, arm 1 requires the most privacy
j
protection and arm 3 the least. The term
1
eξj (cid:0)1
captures the relative amount of exploration needed for arm j to achieve its privacy guarantee. A smaller
privacy parameter ξ makes eξj (cid:0)1 smaller, and therefore increases this term. Intuitively, a more privacy-
j
sensitive arm must be shown more often through random exploration, so that observing this arm is less
informative about whether it was actually the greedy arm.
For the three arms, these relative exploration requirements are
1 1
= (cid:25)1.542,
eξ1 (cid:0)1 e0.5(cid:0)1
1 1
= (cid:25)0.582,
eξ2 (cid:0)1 e1(cid:0)1
and
1 1
= (cid:25)0.157.
eξ3 (cid:0)1 e2(cid:0)1
Thus, arm 1 receives the largest relative exploration requirement, because it has the strongest privacy
guarantee, while arm 3 receives the smallest. The sum of these values,
X3
1
(cid:25)1.542+0.582+0.157=2.280,
eξj (cid:0)1
j=1
serves as a normalizing constant. It converts the relative exploration requirements into valid exploration
weights that sum to one, and also determines the overall exploration probability. Using Equation (95), the
exploration probability is
2.280
ε= (cid:25)0.695,
1+2.280
and the exploitation probability is
1(cid:0)ε(cid:25)0.305.
Using Equation (96), the exploration weights are
1.542 0.582 0.157
w = (cid:25)0.676, w = (cid:25)0.255, w = (cid:25)0.069.
1 2.280 2 2.280 3 2.280

67
| Thus, | the | weighted | ε-greedy |     | policy | in Equation | (97) | becomes |     |     |     |     |
| ----- | --- | -------- | -------- | --- | ------ | ----------- | ---- | ------- | --- | --- | --- | --- |
8
>>><a
|     |     |     |     |     | =argmax |     | Q (a), |     | with | probability | 0.305, |     |
| --- | --- | --- | --- | --- | ------- | --- | ------ | --- | ---- | ----------- | ------ | --- |
|     |     |     |     |     | t       | a   | t      |     |      |             |        |     |
a∗=
t >>>:
|     |              |     |               |     | Categorical(0.676,0.255,0.069), |     |     |     | with | probability | 0.695. |     |
| --- | ------------ | --- | ------------- | --- | ------------------------------- | --- | --- | --- | ---- | ----------- | ------ | --- |
| The | off-diagonal |     | probabilities |     | are                             |     |     |     |      |             |        |     |
(cid:25)0.695(cid:2)0.676=0.470, (cid:25)0.695(cid:2)0.255=0.177, (cid:25)0.695(cid:2)0.069=0.048.
|     | εw       |               |     |     |     | εw           |              |     |     | εw  |     |     |
| --- | -------- | ------------- | --- | --- | --- | ------------ | ------------ | --- | --- | --- | --- | --- |
|     |          | 1             |     |     |     | 2            |              |     |     |     | 3   |     |
| The | diagonal | probabilities |     | add | the | exploitation | probability: |     |     |     |     |     |
p =1(cid:0)ε+εw (cid:25)0.305+0.470=0.775, p =1(cid:0)ε+εw (cid:25)0.305+0.177=0.482, p =1(cid:0)ε+εw (cid:25)0.305+0.048=0.353.
| 11         |     |     | 1             |     |            | 22            |        | 2     |        |     | 33  | 3   |
| ---------- | --- | --- | ------------- | --- | ---------- | ------------- | ------ | ----- | ------ | --- | --- | --- |
| Therefore, |     | the | heterogeneous |     | stochastic | matrix        | is     |       |        |     |     |     |
|            |     |     |               |     |            |               | 0      |       | 1      |     |     |     |
|            |     |     |               |     |            |               | B0.775 | 0.470 | 0.470C |     |     |     |
|            |     |     |               |     |            |               | B      |       | C      |     |     |     |
|            |     |     |               |     |            |               | B      |       | C      |     |     |     |
|            |     |     |               |     |            | Phet(cid:25)B |        |       | C      |     |     |     |
|            |     |     |               |     |            |               | B0.177 | 0.482 | 0.177  | .   |     |     |
C
|     |     |     |     |     |     |     | @     |       | A     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | --- | --- | --- |
|     |     |     |     |     |     |     | 0.048 | 0.048 | 0.353 |     |     |     |
Rows correspond to displayed arms and columns correspond to greedy arms. The arm-specific privacy guar-
antees can be verified using Equation (99). For arm 1, p11 = 0.775 (cid:25)1.65=e0.5; for arm 2, p22 = 0.482 (cid:25)
|          |     |         |     |     |                   |                  |            | p12      | 0.470      |          |            | p21 0.177 |
| -------- | --- | ------- | --- | --- | ----------------- | ---------------- | ---------- | -------- | ---------- | -------- | ---------- | --------- |
| 2.72=e1; |     |         |     | p33 | 0.353             | (cid:25)7.39=e2. |            |          |            |          |            |           |
|          |     | and for | arm | 3,  | =                 |                  | Therefore, |          |            |          |            |           |
|          |     |         |     | p31 | 0.048             |                  |            |          |            |          |            |           |
|          |     |         |     |     | (cid:18) (cid:19) |                  | (cid:18)   | (cid:19) |            | (cid:18) | (cid:19)   |           |
|          |     |         |     |     | p                 |                  |            | p        |            | p        |            |           |
|          |     |         |     | log | 11                | (cid:25)0.5,     | log        | 22       | (cid:25)1, | log 33   | (cid:25)2. |           |
|          |     |         |     |     | p 12              |                  |            | p 21     |            | p 31     |            |           |
In this example, arm 1 is treated as the most privacy-sensitive arm because it has the smallest privacy
parameter,ξ =0.5.Itthereforereceivesthelargestexplorationweight,w (cid:25)0.676.Thismakesarm1appear
|     |     | 1   |     |     |     |     |     |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
often even when it is not the greedy arm, so observing arm 1 is less informative.
Arm 3 is treated as the least privacy-sensitive arm because it has the largest privacy parameter, ξ =2. It
3
(cid:25)0.069.
receives the smallest exploration weight, w As a result, observing arm 3 is more informative about
3
| whether | arm | 3   | was the | greedy | arm. |     |     |     |     |     |     |     |
| ------- | --- | --- | ------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
This heterogeneous policy nests the standard symmetric mechanism. If ξ =ξ for all arms j, then Equa-
j
| tion | (96) | implies |     |     |     |     |     |     |     |     |     |     |
| ---- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |          |      |         |     |     |     | w = | for | all j, |     |     |     |
| --- | -------- | ---- | ------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
|     |          |      |         |     |     |     | j k |     |        |     |     |     |
| and | Equation | (95) | becomes |     |     |     |     |     |        |     |     |     |
k
|     |     |     |     |     |     |     | ε=  |     | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k+eξ(cid:0)1
Thus, the weighted ε-greedy policy collapses to the standard ε-greedy policy with uniform exploration.

68
| J.2. Regret | bound | under | weighted |     | exploration |     |     |     |     |
| ----------- | ----- | ----- | -------- | --- | ----------- | --- | --- | --- | --- |
Theregretanalysischangeswhenprivacyguaranteesvarybyarm.Inthesymmetricmechanism,exploration
isuniform,soeacharmisexploredwithprobabilityε /k.Thisiswhytheconfidenceradiusdependsontε /k
|     |     |     |     |     |     | t   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(see Equation 76). With arm-specific privacy guarantees, exploration is weighted. Following Equation (87),
| arm j is | explored | with probability |     |     |     |        |     |     |       |
| -------- | -------- | ---------------- | --- | --- | --- | ------ | --- | --- | ----- |
|          |          |                  |     |     |     | q =ε w | .   |     | (102) |
|          |          |                  |     |     |     | j,t t  | j,t |     |       |
The worst-case confidence radius is therefore governed by the least-explored arm,
|     |     |     |     |     |     | q =minq | .   |     | (103) |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | ----- |
|     |     |     |     |     |     | min,t   | j,t |     |       |
j
Using the same clean-event argument as in the symmetric regret analysis, the per-round regret bound
| becomes |     |     |     |     |     |     | s   |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2logt
|     |     |     |     |     | E[R˜het(t)](cid:20)εhet+2 |     |     | .   | (104) |
| --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ----- |
t
tq
min,t
ThefirstterminEquation(104)boundstheregretfromexploration,whilethesecondtermboundstheregret
from exploiting an incorrect greedy arm due to estimation error. Given the vector of privacy parameters
| (ξ ,...,ξ | ), the | total exploration |     | probability |       | is   |         |     |       |
| --------- | ------ | ----------------- | --- | ----------- | ----- | ---- | ------- | --- | ----- |
| 1,t       | k,t    |                   |     |             |       | P    |         |     |       |
|           |        |                   |     |             |       | k    | 1       |     |       |
|           |        |                   |     |             |       | Pj=1 | eξj,t−1 |     |       |
|           |        |                   |     |             | εhet= |      |         | .   | (105) |
|           |        |                   |     |             | t     | k    |         |     |       |
|           |        |                   |     |             |       | 1+   | 1       |     |       |
j=1 eξj,t−1
| The corresponding |     | exploration |     | weights | are |     |     |     |     |
| ----------------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
1
|     |     |     |     |     | w   | = P eξj,t−1 |     | .   | (106) |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ----- |
j,t
|            |                 |     |          |      |          | k   | 1       |     |     |
| ---------- | --------------- | --- | -------- | ---- | -------- | --- | ------- | --- | --- |
|            |                 |     |          |      |          | m=1 | eξm,t−1 |     |     |
| Therefore, | the probability |     | that arm | j is | explored | is  |         |     |     |
1
|     |     |     |     |     | =εhetw | Peξj,t−1 |             |     |       |
| --- | --- | --- | --- | --- | ------ | -------- | ----------- | --- | ----- |
|     |     |     |     | q   |        | =        |             | .   | (107) |
|     |     |     |     | j,t | t      | j,t 1+   | k           | 1   |       |
|     |     |     |     |     |        |          | m=1 eξm,t−1 |     |       |
J.2.1. Constant and dynamic arm-level privacy schedules The regret bound in Equation (104)
applies to both constant and dynamic heterogeneous privacy strategies. Under a constant heterogeneous
| strategy, | each arm | has a fixed | privacy |     | budget | γ , so |     |     |     |
| --------- | -------- | ----------- | ------- | --- | ------ | ------ | --- | --- | --- |
j
(cid:17)γ
|     |     |     |     |     |     | ξ     | .   |     | (108) |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- |
|     |     |     |     |     |     | j,t j |     |     |       |
Under a dynamic heterogeneous strategy, each arm has a budget γ , but the uncapped dynamic privacy
j
| level changes | over | time. Let |     |     |     |     |     | !   |     |
| ------------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
k
|     |     |     |     | ξdyn=log |     | 1(cid:0)k+(cid:0) |     | (cid:1) | (109) |
| --- | --- | --- | --- | -------- | --- | ----------------- | --- | ------- | ----- |
|     |     |     |     |          | t   |                   |     | 1/3     |       |
klogt
t

69
denote the privacy level implied by the uncapped dynamic strategy. The arm-specific dynamic privacy level
is
|     |     |     |     |     |     |        | (cid:8) | (cid:9) |     |     |     |       |
| --- | --- | --- | --- | --- | --- | ------ | ------- | ------- | --- | --- | --- | ----- |
|     |     |     |     |     |     | ξ =min | γ ,ξdyn |         | .   |     |     | (110) |
|     |     |     |     |     |     | j,t    | j       | t       |     |     |     |       |
Thus, before any arm-specific budget binds, all arms receive the same privacy level and the policy is
symmetric. Once some budgets bind and others do not, privacy guarantees differ across arms and the policy
becomes heterogeneous.
J.2.2. Symmetric benchmark with the same global privacy guarantee We compare the hetero-
geneous mechanism to a symmetric benchmark with the same global privacy guarantee at time t. Let
|     |     |     |     |     |     | ξ     | =maxξ | .   |     |     |     | (111) |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     | max,t |       | j,t |     |     |     |       |
j
The symmetric benchmark applies privacy level ξ to every arm. Thus, both mechanisms satisfy the
max,t
same global privacy guarantee at time t. Because ξ is the largest privacy parameter, the least-explored
max,t
arm under the heterogeneous mechanism is the arm with privacy parameter ξ . Therefore, from Equa-
max,t
tion (107),
1
|     |     |     |     |     | q   | =   | Peξmax,t−1 |     | .   |     |     | (112) |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ----- |
min,t
|              |           |     |       |           |      | 1+       | k   | 1           |     |     |     |     |
| ------------ | --------- | --- | ----- | --------- | ---- | -------- | --- | ----------- | --- | --- | --- | --- |
|              |           |     |       |           |      |          | m=1 | eξm,t−1     |     |     |     |     |
| Substituting | Equations |     | (105) | and (112) | into | Equation |     | (104) gives |     |     |     |     |
v
|     |     |     |     |     | P   |     | u   | (cid:16) | P   | (cid:17) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- |
u
|                |           |                     |             |     | k           | 1       | u2  | 1+      | k         | 1       | logt |       |
| -------------- | --------- | ------------------- | ----------- | --- | ----------- | ------- | --- | ------- | --------- | ------- | ---- | ----- |
|                |           |                     |             |     |             | eξj,t−1 | t   |         | j=1       | eξj,t−1 |      |       |
|                |           | E[R˜het(t)](cid:20) |             |     | Pj=1        |         | +2  |         |           |         | .    | (113) |
|                |           |                     |             |     | k           |         |     |         | 1         |         |      |       |
|                |           |                     |             | 1+  |             | 1       |     |         | t         |         |      |       |
|                |           |                     |             |     | j=1         | eξj,t−1 |     |         | eξmax,t−1 |         |      |       |
| The symmetric  | benchmark |                     | corresponds |     | to          | setting |     |         |           |         |      |       |
|                |           |                     |             |     | ξ           | =ξ      |     | for all | j.        |         |      | (114) |
|                |           |                     |             |     | j,t         | max,t   |     |         |           |         |      |       |
| Under Equation | (114),    | the                 | exploration |     | probability |         | is  |         |           |         |      |       |
k
|     |     |     |     |       |     | eξmax,t−1 |     |           | k        |     |     |       |
| --- | --- | --- | --- | ----- | --- | --------- | --- | --------- | -------- | --- | --- | ----- |
|     |     |     |     | εsym= |     |           | =   |           |          | .   |     | (115) |
|     |     |     |     | t     | 1+  | k         |     | k+eξmax,t | (cid:0)1 |     |     |       |
eξmax,t−1
| which corresponds |     | to Equation |     | (13). | Each arm | is explored |     | with | probability |     |     |     |
| ----------------- | --- | ----------- | --- | ----- | -------- | ----------- | --- | ---- | ----------- | --- | --- | --- |
|                   |     |             |     |       |          | 1           |     |      | 1           |     |     |     |
eξmax,t−1
|     |     |     |     | qsym= |     |     | =   |           |          | .   |     | (116) |
| --- | --- | --- | --- | ----- | --- | --- | --- | --------- | -------- | --- | --- | ----- |
|     |     |     |     | t     | 1+  | k   |     | k+eξmax,t | (cid:0)1 |     |     |       |
eξmax,t−1
| The symmetric | worst-case |     | regret | bound | is  | therefore |     |     |     |     |     |     |
| ------------- | ---------- | --- | ------ | ----- | --- | --------- | --- | --- | --- | --- | --- | --- |
v
|     |     |     |     |     |     |     | u   | (cid:16) |     | (cid:17) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- |
u
|     |     |     |                     |     |           | k         | u2  | 1+  | k         | logt |     |       |
| --- | --- | --- | ------------------- | --- | --------- | --------- | --- | --- | --------- | ---- | --- | ----- |
|     |     |     | E[R˜sym(t)](cid:20) |     | eξmax,t−1 |           | t   |     | eξmax,t−1 |      |     |       |
|     |     |     |                     |     |           |           | +2  |     |           |      | .   | (117) |
|     |     |     |                     |     | 1+        | k         |     |     | t 1       |      |     |       |
|     |     |     |                     |     |           | eξmax,t−1 |     |     | eξmax,t−1 |      |     |       |

70
J.2.3. Why arm-level heterogeneity increases the regret bound We now compare the heteroge-
(cid:20)ξ
neous bound in Equation (113) with the symmetric bound in Equation (117). By definition, ξ j,t max,t for
allarms.Ifprivacyguaranteesareheterogeneousattimet,thenthisinequalityisstrictforatleastonearm.
x7!1/(ex(cid:0)1)
| Since the | function |     | is strictly | decreasing, |     | it follows | that |     |
| --------- | -------- | --- | ----------- | ----------- | --- | ---------- | ---- | --- |
Xk
|     |     |     |     |       | 1        |         | k        |       |
| --- | --- | --- | --- | ----- | -------- | ------- | -------- | ----- |
|     |     |     |     |       |          | >       | .        | (118) |
|     |     |     |     | eξj,t | (cid:0)1 | eξmax,t | (cid:0)1 |       |
j=1
By Equations (105), (115), and (118), the heterogeneous exploration probability is larger than the sym-
| metric exploration | probability: |     |     |     |            |     |     |       |
| ------------------ | ------------ | --- | --- | --- | ---------- | --- | --- | ----- |
|                    |              |     |     |     | εhet>εsym. |     |     | (119) |
|                    |              |     |     |     | t          | t   |     |       |
Equation (118) also implies that the least-explored arm under heterogeneous privacy is less explored than
each arm under the symmetric benchmark. Using Equations (112) and (116),
|     |     |     |         | 1          |         |     | 1                |       |
| --- | --- | --- | ------- | ---------- | ------- | --- | ---------------- | ----- |
|     |     |     |         | Peξmax,t−1 |         |     | eξmax,t−1 =qsym. |       |
|     |     | q   | min,t = |            |         | <   |                  | (120) |
|     |     |     | 1+      | k          | 1       | 1+  | k t              |       |
|     |     |     |         | m=1        | eξm,t−1 |     | eξmax,t−1        |       |
Because the confidence term in Equation (104) is decreasing in the exploration probability of the least-
| explored | arm, Equation | (120) | implies |     |       |       |     |       |
| -------- | ------------- | ----- | ------- | --- | ----- | ----- | --- | ----- |
|          |               |       |         | s   |       | s     |     |       |
|          |               |       |         |     | 2logt | 2logt |     |       |
|          |               |       |         | 2   |       | >2    | .   | (121) |
|          |               |       |         | tq  |       | tqsym |     |       |
|          |               |       |         |     | min,t |       | t   |       |
Equations (119) and (121) show that both components of the worst-case regret bound are larger under
heterogeneousprivacy.Equation(119)comparestheexplorationcomponent:heterogeneousprivacyincreases
the total privacy-induced exploration probability. Equation (121) compares the exploitation component:
because heterogeneous privacy makes exploration uneven across arms, the least-explored arm receives less
exploration than under the symmetric benchmark, which increases the confidence radius and therefore the
| regret from | exploiting | an incorrectly | estimated |     | greedy | arm. |     |     |
| ----------- | ---------- | -------------- | --------- | --- | ------ | ---- | --- | --- |
Thus,relativetoasymmetricmechanismwiththesameglobalprivacyguaranteeξ ,arm-levelprivacy
max,t
heterogeneity increases the worst-case per-round regret bound whenever privacy guarantees differ across
| arms at | time t. |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
J.2.4. Quantifying the regret cost of heterogeneity. Holding ξ fixed, we can quantify the
max,t
increase in the worst-case regret bound from arm-level privacy heterogeneity. Define
Xk
|     |     |     |       |     | 1     |          | k        |       |
| --- | --- | --- | ----- | --- | ----- | -------- | -------- | ----- |
|     |     |     | ∆het= |     |       | (cid:0)  | .        | (122) |
|     |     |     |       | t   |       | (cid:0)1 | (cid:0)1 |       |
|     |     |     |       |     | eξj,t | eξmax,t  |          |       |
j=1

71
Theterm∆het measuresthedistancefromthesymmetricbenchmarkontheexplorationscale.Itequalszero
t
when all arms have privacy parameter ξ and is positive whenever privacy guarantees differ across arms.
max,t
Let Bhet and Bsym denote the right-hand sides of Equations (113) and (117), respectively. Using Equa-
t
t
| tion (122), | the heterogeneous |     | bound |     | can be | written | as       |     |     |          |     |     |     |     |     |     |
| ----------- | ----------------- | --- | ----- | --- | ------ | ------- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
|             |                   |     |       |     |        | v       | (cid:16) |     |     | (cid:17) |     |     |     |     |     |     |
u
u
|     |       |      | k         | +∆het   |     | t2  | 1+        | k   | +∆het | (eξmax,t | (cid:0)1)logt |     |     |       |     |     |
| --- | ----- | ---- | --------- | ------- | --- | --- | --------- | --- | ----- | -------- | ------------- | --- | --- | ----- | --- | --- |
|     |       |      | eξmax,t−1 |         | t   |     | eξmax,t−1 |     | t     |          |               |     |     |       |     |     |
|     | Bhet= |      |           |         |     | +2  |           |     |       |          |               | .   |     | (123) |     |     |
|     |       | t 1+ |           | k +∆het |     |     |           |     | t     |          |               |     |     |       |     |     |
|     |       |      | eξmax,t−1 |         | t   |     |           |     |       |          |               |     |     |       |     |     |
The symmetric benchmark corresponds to ∆het=0. Therefore, the increase in the worst-case per-round
t
| regret bound | due | to heterogeneity |     | is  |     |     |           |     |               |     |     |     |     |     |     |     |
| ------------ | --- | ---------------- | --- | --- | --- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|              | "   |                  |     |     |     |     | # r       |     |               | "r  |     |     |     | r   |     | #   |
|              |     | k                |     |     |     | k   |           |     |               |     |     |     |     |     |     |     |
|              |     |                  | +∆h | et  |     |     | 2(eξmax,t |     | (cid:0)1)logt |     |     | k   |     |     | k   |     |
Bhet(cid:0)Bsym= eξma x,t−1 t (cid:0) eξma x,t−1 +2 1+ +∆het(cid:0) 1+ .
|     |     |           |       |     |           |     |     |     |     |     |         | (cid:0)1 |     |     |         | (cid:0)1 |
| --- | --- | --------- | ----- | --- | --------- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | ------- | -------- |
| t t | 1+  | k         | +∆het |     | 1+        | k   |     |     | t   |     | eξmax,t |          | t   |     | eξmax,t |          |
|     |     | eξmax,t−1 |       | t   | eξmax,t−1 |     |     |     |     |     |         |          |     |     |         |          |
(124)
| Equivalently, | using |     |     |       |     |         |              |     |     |     |     |     |     |     |     |     |
| ------------- | ----- | --- | --- | ----- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|               |       |     |     | x+∆   |     | x       |              | ∆   |     |     |     |     |     |     |     |     |
|               |       |     |     |       |     | (cid:0) | =            |     |     |     |     |     |     |     |     |     |
|               |       |     |     | 1+x+∆ |     | 1+x     | (1+x+∆)(1+x) |     |     |     |     |     |     |     |     |     |
and
|          |           |            |     |     | p          | p   |      | ∆   |     |     |     |     |     |     |     |     |
| -------- | --------- | ---------- | --- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|          |           |            |     |     | x+∆(cid:0) |     | p    |     | p   |     |     |     |     |     |     |     |
|          |           |            |     |     |            |     | x=   |     | ,   |     |     |     |     |     |     |     |
|          |           |            |     |     |            |     | x+∆+ |     | x   |     |     |     |     |     |     |     |
| Equation | (124) can | be written |     | as  |            |     |      |     |     |     |     |     |     |     |     |     |
q
|                      |     | 2         |           |     |       |                  |           |            |           |             |        |      |           | 3   |     |     |
| -------------------- | --- | --------- | --------- | --- | ----- | ---------------- | --------- | ---------- | --------- | ----------- | ------ | ---- | --------- | --- | --- | --- |
|                      |     |           |           |     |       |                  |           |            |           | 2 2(eξmax,t | −1)    | logt |           |     |     |     |
|                      |     | 4(cid:16) |           |     | 1     |                  |           |            |           |             |        |      |           | 5   |     |     |
| Bhet(cid:0)Bsym=∆het |     |           |           |     |       | (cid:17)(cid:16) |           | (cid:17)+q |           |             | t      | q    |           | .   |     |     |
| t                    | t   | t         |           |     |       |                  |           |            |           |             |        |      |           |     |     |     |
|                      |     |           | 1+        | k   | +∆het | 1+               | k         |            | 1+        | k           | +∆het+ | 1+   | k         |     |     |     |
|                      |     |           | eξmax,t−1 |     | t     |                  | eξmax,t−1 |            | eξmax,t−1 |             | t      |      | eξmax,t−1 |     |     |     |
(125)
Equation (125) isolates the additional regret due to arm-level privacy heterogeneity. The increase in the
boundisproportionalto∆het,theadditionalexplorationscalerequiredbyheterogeneousprivacyguarantees.
t
The bracketed term is strictly positive. Hence, whenever ∆het>0, the heterogeneous privacy policy has a
t
larger worst-case regret bound than the symmetric benchmark with the same global privacy guarantee.
| Moreover, | because | ∆het>0, |     | the term |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
k
+∆het
1+
|     |     |     |     |     |     | eξmax,t | (cid:0)1 | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is larger than its value under the symmetric benchmark, where ∆het=0. Hence, both denominators in the
t
bracketedtermofEquation(125)arelargerthantheirvaluesat∆het=0.Sincethecorrespondingnumerators
t

72
are positive and do not depend on ∆het, the bracketed term is largest at ∆het=0. Evaluating the bracket at
|     |     |     | t   |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- |
this value therefore gives an upper bound on the additional regret from heterogeneity. Therefore,
|     |     |     | 2   |     | 3   |     |
| --- | --- | --- | --- | --- | --- | --- |
q
2(eξmax,t−1)logt7
|     |     |                                      | 6 1 |              |      |       |
| --- | --- | ------------------------------------ | --- | ------------ | ---- | ----- |
|     |     | Bhet(cid:0)Bsym(cid:20)∆het4(cid:16) |     | (cid:17) + q | t 5. | (126) |
|     |     | t                                    | t t | 2 1+         | k    |       |
1+ k
|     |     |     | eξmax,t−1 |     | eξmax,t−1 |     |
| --- | --- | --- | --------- | --- | --------- | --- |
Thus,holdingξ fixed,theadditionalregretfromarm-levelprivacyheterogeneityisboundedaboveby
max,t
atermthatislinearin∆het.Thecoeﬀicientmultiplying∆het isthemarginalcostofheterogeneityevaluated
|     |     | t   |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
at the symmetric benchmark. Since this coeﬀicient is positive, any ∆het>0 increases the worst-case regret
t
| bound relative | to the | symmetric | benchmark. |     |     |     |
| -------------- | ------ | --------- | ---------- | --- | --- | --- |
References
Aguiar L, Peukert C, Schäfer M, Ullrich H (2026) Off-platform tracking and data externalities: Evidence
fromfacebook.SSRNworkingpaper,URLhttps://papers.ssrn.com/sol3/papers.cfm?abstract_
| id=6886178, | 34  | pages. Posted | June 26, 2026. |     |     |     |
| ----------- | --- | ------------- | -------------- | --- | --- | --- |
Anand P, Lee C (2023) Using deep learning to overcome privacy and scalability issues in customer data
transfer. Marketing Science 42(1):189–207, URL http://dx.doi.org/10.1287/mksc.2022.1365.
AramayoN,SchiappacasseM,GoicM(2023)Amultiarmedbanditapproachforhouseadsrecommendations.
Marketing Science 42(2):271–292, URL http://dx.doi.org/10.1287/mksc.2022.1378.
AridorG,CheYK,HollenbeckB,KaiserM,McCarthyD(2024)Evaluatingtheimpactofprivacyregulation
one-commercefirms:Evidencefromapple’sapptrackingtransparency.SSRN Electronic Journal URL
http://dx.doi.org/10.2139/ssrn.4717752.
Barnes&Noble (2026) Cookie policy. URL https://www.barnesandnoble.com/h/help/cookie-policy,
| accessed | 2026-03-02. |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
BroughAR,NortonDA,SciarappaSL,JohnLK(2022)Thebulletproofglasseffect:Unintendedconsequences
of privacy notices. Journal of Marketing Research 59(4):739–754, URL http://dx.doi.org/10.1177/
00222437211069093.
Castelluccia C, Kaafar MA, Tran MD (2012) Betrayed by your ads! Fischer-Hübner S, Wright M, eds.,
Privacy Enhancing Technologies, 1–17 (Berlin, Heidelberg: Springer Berlin Heidelberg), ISBN 978-3-
642-31680-7.

73
Chen B, Tag B, Xue H, Angus D, Salim F (2026) When ads become profiles: Uncovering the invisible
risk of web advertising at scale with llms. Proceedings of the ACM Web Conference 2026, 9604–9615,
WWW ’26 (New York, NY, USA: Association for Computing Machinery), ISBN 9798400723070, URL
http://dx.doi.org/10.1145/3774904.3793060.
Choi WJ, Jerath K, Sarvary M (2023) Consumer privacy choices and (un)targeted advertising along the
purchase journey. Journal of Marketing Research 60(5):889–907, URL http://dx.doi.org/10.1177/
00222437221140052.
Christoph JN (2026) The privacy budget we never agreed to. Carr-Ryan Commentary, Har-
vard Kennedy School, URL https://www.hks.harvard.edu/centers/carr-ryan/our-work/
carr-ryan-commentary/privacy-budget-we-never-agreed, accessed: 2026-02-26.
De los Santos B, Koulayev S (2017) Optimizing click-through in online rankings with endogenous search
refinement. Marketing Science 36(4):542–564, URL http://dx.doi.org/10.1287/mksc.2017.1036.
Dekel I, Cummings R, Heffetz O, Ligett K (2022) The privacy elasticity of behavior: Conceptualization and
application.WorkingPaper30215,NationalBureauofEconomicResearch,URLhttp://dx.doi.org/
10.3386/w30215.
DworkC,RothA(2014)Thealgorithmicfoundationsofdifferentialprivacy.Found. Trends Theor. Comput.
Sci. 9(3–4):211–407, ISSN 1551-305X, URL http://dx.doi.org/10.1561/0400000042.
Fischer M, Albers S, Wagner N, Frie M (2011) Practice prize winner—dynamic marketing budget allocation
across countries, products, and marketing activities. Marketing Science 30(4):568–585, URL http:
//dx.doi.org/10.1287/mksc.1100.0627.
Goldfarb A, Tucker C (2011) Online display advertising: Targeting and obtrusiveness. Marketing Science
30(3):389–404, URL http://dx.doi.org/10.1287/mksc.1100.0583.
Hauser JR, Liberali G, Urban G (2014) Website morphing 2.0: Technical and implementation advances and
a field experiment. Management Science 60(6):1594–1616.
Hauser JR, Urban GL, Liberali G, Braun M (2009) Website morphing. Marketing Science 28(2):202–223,
URL http://dx.doi.org/10.1287/mksc.1080.0459.

74
Hsu J, Gaboardi M, Haeberlen A, Khanna S, Narayan A, Pierce BC, Roth A (2014) Differential privacy:
An economic method for choosing epsilon. CoRR abs/1402.3329, URL http://arxiv.org/abs/1402.
3329.
Jerath K, Miller K (2024) Consumers’ perceived privacy violations in online advertising. SSRN Electronic
Journal URL http://dx.doi.org/10.2139/ssrn.4736957.
Johnson GA, Shriver SK, Du S (2020) Consumer privacy choice in online advertising: Who opts out and
at what cost to industry? Marketing Science 39(1):33–51, URL http://dx.doi.org/10.1287/mksc.
2019.1198.
Joo J, Chiong KX (2025) Getting the most out of a/b tests using the asymptotic minimax-regret criteria.
Management Science 0(0):null, URL http://dx.doi.org/10.1287/mnsc.2024.06590.
KimT,BaraszK,JohnLK(2018)Whyamiseeingthisad?theeffectofadtransparencyonadeffectiveness.
Journal of Consumer Research 45(5):906–932, ISSN 0093-5301, URL http://dx.doi.org/10.1093/
jcr/ucy039.
Korganbekova M, Zuber C (2024) Balancing user privacy and personalization. Working paper
URL https://marketing.wharton.upenn.edu/wp-content/uploads/2023/10/11.09.
2023-Korganbekova-Malika-PAPER-JMP.pdf.
Kraft L, Skiera B, Koschella T (2023) Economic impact of opt-in versus opt-out requirements for personal
data usage: The case of Apple’s App Tracking Transparency (ATT). SSRN Electronic Journal URL
http://dx.doi.org/10.2139/ssrn.4598472.
LeeRA(2026)GoogleAnalyticsStatistics2026:What’sNewandWhat’sNext.URLhttps://sqmagazine.
co.uk/google-analytics-statistics/, reviewed by Barry Elad. Last updated January 21, 2026.
Li L, Chu W, Langford J, Schapire RE (2010) A contextual-bandit approach to personalized news article
recommendation. Proceedings of the 19th international conference on World wide web, 661–670.
Liberali G, Ferecatu A (2022) Morphing for consumer dynamics: Bandits meet hidden markov models.
Marketing Science 41(4):769–794, URL http://dx.doi.org/10.1287/mksc.2021.1346.
Lin T (2022) Valuing intrinsic and instrumental preferences for privacy. Marketing Science 41(4):663–681,
URL http://dx.doi.org/10.1287/mksc.2022.1368.

75
Liu CHB, Cardoso A, Couturier P, McCoy EJ (2021) Datasets for online controlled experiments. Van-
schoren J, Yeung S, eds., Proceedings of the Neural Information Processing Systems Track on Datasets
andBenchmarks,volume1,URLhttps://datasets-benchmarks-proceedings.neurips.cc/paper/
2021/file/274ad4786c3abca69fa097b85867d9a4-Paper-round2.pdf.
Mela CF, Roos JMT, Sousa T (2026) Advertiser learning in direct advertising markets. Marketing Science
45(4):864–891, URL http://dx.doi.org/10.1287/mksc.2024.0847.
Miller KM, Skiera B (2024) Economic consequences of online tracking restrictions: Evidence from cookies.
International Journal of Research in Marketing 41(2):241–264,ISSN0167-8116,URLhttp://dx.doi.
org/https://doi.org/10.1016/j.ijresmar.2023.10.001.
MishraN,ThakurtaA(2015)(nearly)optimaldifferentiallyprivatestochasticmulti-armbandits.Proceedings
of the Thirty-First Conference on Uncertainty in Artificial Intelligence, 592–601, UAI’15 (Arlington,
Virginia, USA: AUAI Press), ISBN 9780996643108.
MisraK,SchwartzEM,AbernethyJ(2019)Dynamiconlinepricingwithincompleteinformationusingmul-
tiarmed bandit experiments. Marketing Science 38(2):226–252, URL http://dx.doi.org/10.1287/
mksc.2018.1129.
MoffettJW,ChisamN,MartinKD,PalmatierRW(2025)Express:Customerdataprivacystewardship.Jour-
nal of Marketing 0(ja):00222429251367342, URL http://dx.doi.org/10.1177/00222429251367342.
Optimizely(2026)Multi-armedbandit.OptimizelyOptimizationGlossary,URLhttps://www.optimizely.
com/optimization-glossary/multi-armed-bandit/, accessed 2026-03-02.
Panageas I, Ghosal D, Lin W (2020) Lecture 9: Introduction to multi-armed bandits. Lecture notes
for Optimization for Machine Learning (50.579), URL https://panageas.github.io/_pages/L09_
LectureNotes.pdf.
Peers Y, van Heerde HJ, Dekimpe MG (2017) Marketing budget allocation across countries: The role of
international business cycles. Marketing Science 36(5):792–809, URL http://dx.doi.org/10.1287/
mksc.2017.1046.
Ponte GR, Boot T, Reutterer T, Wieringa JE (2026) Express: Where should firms implement
differential privacy in targeting? implications for profitability. Journal of Marketing Research
0(ja):00222437261455302, URL http://dx.doi.org/10.1177/00222437261455302.

76
Ponte GR, Wieringa JE, Boot T, Verhoef PC (2024) Where’s Waldo? A framework for quantifying the
privacy-utility trade-off in marketing applications. International Journal of Research in Marketing
41(3):529–546, ISSN 0167-8116, URL http://dx.doi.org/https://doi.org/10.1016/j.ijresmar.
2024.05.003.
Ren W, Zhou X, Liu J, Shroff NB (2020) Multi-armed bandits with local differential privacy. URL https:
//arxiv.org/abs/2007.03121.
Saito Y, Aihara S, Matsutani M, Narita Y (2020) A large-scale open dataset for bandit algorithms. CoRR
abs/2008.07146, URL https://arxiv.org/abs/2008.07146.
Schwartz EM, Bradlow ET, Fader PS (2017) Customer acquisition via display advertising using multi-
armed bandit experiments. Marketing Science 36(4):500–522, URL http://dx.doi.org/10.1287/
mksc.2016.1023.
Shaddy F, Friedman EMS, Toubia O (2026) Fairness perceptions in demographic targeting. Journal of
Consumer Research 53(1):22–47, ISSN 0093-5301, URL http://dx.doi.org/10.1093/jcr/ucaf048.
SummersCA,SmithRW,ReczekRW(2016)Anaudienceofone:Behaviorallytargetedadsasimpliedsocial
labels. Journal of Consumer Research 43(1):156–178, ISSN 0093-5301, URL http://dx.doi.org/10.
1093/jcr/ucw012.
Sutton RS, Barto AG (2018) Reinforcement Learning: An Introduction (The MIT Press), second edition,
URL http://incompleteideas.net/book/the-book-2nd.html.
TianL,TurjemanD,LevyS(2026)Privacy-preservingdatafusion.Marketing Science0(0):null,URLhttp:
//dx.doi.org/10.1287/mksc.2023.0068.
TodriV(2022)Frontiers:Theimpactofad-blockersononlineconsumerbehavior.MarketingScience41(1):7–
18, URL http://dx.doi.org/10.1287/mksc.2021.1309.
Tossou A, Dimitrakakis C (2015) Algorithms for differentially private multi-armed bandits. URL https:
//arxiv.org/abs/1511.08681.
Tucker CE (2014) Social networks, personalized advertising, and privacy controls. Journal of Marketing
Research 51(5):546–562, URL http://dx.doi.org/10.1509/jmr.10.0355.

77
Wang P, Jiang L, Yang J (2024) The early impact of gdpr compliance on display advertising: The case
of an ad publisher. Journal of Marketing Research 61(1):70–91, URL http://dx.doi.org/10.1177/
00222437231171848.
Wang Y, Tao L, Zhang XX (2025) Recommending for a multi-sided marketplace: A multi-objective hierar-
chical approach. Marketing Science 44(1):1–29, URL http://dx.doi.org/10.1287/mksc.2022.0238.
Wang Y, Wu X, Hu D (2016) Using randomized response for differential privacy preserving data collection.
| EDBT/ICDT | Workshops, | volume 1558, | 0090–6778. |     |
| --------- | ---------- | ------------ | ---------- | --- |
Wernerfelt N, Tuchman A, Shapiro BT, Moakler R (2025) Estimating the value of offsite tracking data
| to advertisers: | Evidence | from meta. | Marketing Science 44(2):268–286, | URL |
| --------------- | -------- | ---------- | -------------------------------- | --- |
http://dx.doi.org/10.
1287/mksc.2023.0274.
Xin X, Yang J, Wang H, Ma J, Ren P, Luo H, Shi X, Chen Z, Ren Z (2023) On the user behavior leakage
from recommender system exposure. ACM Transactions on Information Systems 41(3):1–25, ISSN
| 1558-2868, | URL http://dx.doi.org/10.1145/3568954. |     |     |     |
| ---------- | -------------------------------------- | --- | --- | --- |
Zia A, Rao JM (2019) Search advertising: Budget allocation across search engines. Marketing Science
| 38(6):1023–1037, | URL | http://dx.doi.org/10.1287/mksc.2019.1186. |     |     |
| ---------------- | --- | ----------------------------------------- | --- | --- |
---- END DOCUMENT ----
