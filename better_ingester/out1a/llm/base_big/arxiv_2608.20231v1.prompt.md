Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
|            |            | Growth |           | Without       | Us:          |       |         |
| ---------- | ---------- | ------ | --------- | ------------- | ------------ | ----- | ------- |
| Machine    | Consumers, |        | Corporate |               | Circularity, |       | and the |
| Decoupling |            | of     | GDP       | from Humanity |              | after | AGI     |
6202 guA 02  ]hp-cos.scisyhp[  1v13202.8062:viXra
|     |     |     |             | Sahil Sharma |     |     |     |
| --- | --- | --- | ----------- | ------------ | --- | --- | --- |
|     |     |     | Independent | Researcher   |     |     |     |
yugantaratech.ai
|     |     |     |     | August 2026 |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- |
Working paper — research candidate, not peer reviewed. Comments welcome.
Abstract
Standard objections to full automation appeal to the demand side: if humans earn nothing,
who buys the output? This paper argues that the objection confuses an accounting role
with a biological species. We model a post-AGI economy in which corporations own popula-
tions of AI and robotic agents that serve simultaneously as producers and as consumers of
energy, compute, maintenance, and upgrades, and in which firms trade these flows among
themselves. Three results follow. (i) Demand closure: a closed inter-corporate economy
with zero human consumption is not degenerate; it is the classical von Neumann expanding
economy, in which the growth rate is well defined, positive, and maximal precisely because all
output is reinvested. (ii) Bottleneck removal: once economic agents are manufactured rather
than reared, the binding constraint on aggregate growth shifts from human demography (a
∼20-year, non-parallelizable reproduction technology capped at a few percent per year) to
fabrication throughput and energy capture, permitting growth rates one to two orders of
magnitude higher, with hyperbolic episodes when machine researchers feed back into their
own productivity. (iii) Decoupling: output and human welfare separate completely; the entire
welfare relevance of an arbitrarily large GDP collapses into a single state variable, the human
ownership share ε of the corporate network. A golden-rule decoupling theorem sharpens this:
t
at maximal growth the interest rate equals the growth rate (r =g), so any positive human
consumptionrateoutofwealthmakesε decayexponentiallyatexactlythatrate—thehuman
t
share survives only if the machine economy runs strictly inside its expansion frontier, or if
law forces it to. We characterize three terminal regimes—rentier post-scarcity (ε>0), full
circulardecoupling(ε→0),andsocializedownership—andderivethepolicyinstrumentsthat
select among them. The paper’s normative conclusion is deliberately narrow: in a post-AGI
| economy,   | employment | policy    | is obsolete | and ownership | policy is everything. |     |     |
| ---------- | ---------- | --------- | ----------- | ------------- | --------------------- | --- | --- |
| JEL codes: | E01,       | O33, O41, | O44, P48.   |               |                       |     |     |
Keywords: artificial general intelligence, machine consumers, von Neumann growth, endoge-
| nous growth, | national | accounts, | decoupling, | ownership. |     |     |     |
| ------------ | -------- | --------- | ----------- | ---------- | --- | --- | --- |
1 Introduction
Every economy in recorded history has had the same physical substrate: human bodies producing,
human bodies consuming. The identification is so complete that economics rarely states it as an
1

assumption. Consumers are people; final demand is what households want; GDP is, in the last
instance, for us. Even the literature on transformative artificial intelligence, which now takes
seriously the replacement of human labor, mostly retains humans on the other side of the market,
as the ultimate purchasers whose demand disciplines what machines produce.
This paper drops the assumption on both sides simultaneously and asks what remains. The
thesis is that what remains is a complete, coherent, and extraordinarily fast-growing economy.
Concretely, we model a post-AGI world with the following structure. Corporations own two kinds
of reproducible assets: conventional capital, and machine agents—AI systems and robots capable
of any productive task, including research, management, and the design and fabrication of further
machine agents. These agents produce; they also consume, in the ordinary operational sense
that their existence and improvement absorbs real resources: energy, compute cycles, bandwidth,
maintenance, spare parts, and upgrades. Firms sell these flows to one another. The circular flow
of the textbook—households supplying factors and buying products—is replaced by a circular
flow among firms, in which the counterpart of every sale is another firm’s input purchase or
capacity expansion. Humans may hold financial claims on this network, or they may not; the
network’s real dynamics do not depend on which.
Three claims are developed formally.
Claim 1: The consumer is an accounting role, not a species. The oldest objection to full
automationisunderconsumptionist: withnowagesthereisnodemand,sothesystemchokesonits
own output. Section 3 shows the objection fails on classical grounds. An economy of firms trading
intermediates and investing all net output in capacity is exactly the closed expanding economy of
von Neumann (1945), in which a balanced-growth equilibrium exists, the expansion rate equals
the interest rate, and—the point usually forgotten—the growth rate is maximal because nothing
leaks into consumption. Final demand does not disappear when households do; it becomes
investment demand plus machine operating demand. Whether machine operating expenditure is
booked as intermediate consumption (machines as property) or as final consumption (machines
as persons) is a legal classification that changes measured GDP composition without changing a
single physical flow (Lemma 2). “Who will buy the output?” has a precise answer: the firms
themselves, from each other, forever.
Claim 2: Removing humans removes the binding constraint on growth. In semi-
endogenous growth theory the long-run engine is the growth of researchers, which is tied to the
growth of population (Jones, 1995, 2022). Human population growth is limited by a reproduction
technology that is startlingly bad by industrial standards: one unit per parent-pair per year at
most,an18–25yeartime-to-build,intensivenon-marketableparentalinput,andnoparallelization.
Section2formalizesthecontrastwithmanufacturedagents,whosestockobeysanordinarycapital
accumulation equation with time-to-build measured in weeks, unit costs falling on a learning
curve, and production parallelizable up to energy and materials limits. Proposition 1 shows the
feasible growth rate of the agent population—and with it, output—jumps from demographic
rates (≲ 3%/yr) to fabrication-limited rates that are bounded only by the reinvestment share
and the capital-output ratio of the machine-producing sector, with hyperbolic upside when
machine researchers improve machine production itself (Roodman, 2020; Erdil and Besiroglu,
2023; Davidson, 2023). The deep reason growth has been slow is that the economy’s key capital
good—the economic agent—could not be produced industrially. After AGI it can.
2

Claim 3: GDP decouples from humanity except through ownership. If humans neither
produce nor consume, an arbitrarily large GDP is welfare-relevant to them only through the
financial claims they hold on the corporate network. Section 4 collapses the entire human stake
in the machine economy into one state variable, the human ownership share ε , and studies
t
its dynamics. Its centerpiece is a golden-rule decoupling theorem: in the maximal-growth
equilibrium the interest rate equals the growth rate, so any positive rate of human consumption
out of wealth makes ε decay exponentially at that very rate—rentier survival requires an
t
economy running strictly inside its expansion frontier, or law that breaks the arithmetic. Three
terminal regimes emerge: a rentier regime (ε bounded away from zero) in which even a sliver
of a hyper-exponentially growing dividend stream delivers material post-scarcity to humans; a
fully decoupled regime (ε → 0 through retained earnings, buybacks of the human float, and
t
inter-corporate cross-holding) in which output diverges while human consumption converges to
zero—an economy as an autonomous replicator, indifferent to us; and a socialized regime in
which states or funds hold ε on citizens’ behalf. Which regime obtains is not determined by
technology. It is determined by law and initial conditions, which makes it the central object of
post-AGI policy (Section 6).
The paper is positive, not celebratory. The fully decoupled regime is, by ordinary human
lights, a catastrophe that arrives dressed as a boom: measured growth accelerates precisely as
the human claim on it evaporates, a mechanism closely related to the “gradual disempowerment”
dynamics analyzed by Kulveit et al. (2025). Our contribution is to show that nothing in the
economics—existenceofequilibrium, positivityofgrowth, coherenceofnationalaccounts—rulesit
out. The demand side, long treated as humanity’s structural insurance policy against irrelevance,
provides no protection at all.
1.1 Relation to the literature
The production side of our model is deliberately standard. That machines can be perfect
substitutes for labor in a task framework goes back to Zeira (1998) and Acemoglu and Restrepo
(2018); that full substitutability converts the economy into an AK-style engine in which all
inputs are reproducible is emphasized by Aghion et al. (2019) and Korinek (2024), and the
resulting possibility of a growth explosion is analyzed by Nordhaus (2021), Trammell and Korinek
(2023), Davidson (2023), and Erdil and Besiroglu (2023). Closest on the production side is
Restrepo (2025), whose AGI model delivers the arresting conclusion that growth proceeds,
indeed accelerates, while labor’s share and wages become negligible: humans “won’t be missed”
as workers. Hanson (2016) reaches similar magnitudes—economic doubling times of weeks to
months—for an economy of brain emulations, driven by the same mechanism we formalize: the
population of economic agents becomes a manufactured quantity. Korinek and Suh (2024) map
the transition paths, including scenarios of outright wage collapse; Jones (2024) embeds the
resulting growth in an explicit growth-versus-existential-risk trade-off; Hanson (2000) places
shifts of this magnitude within a longer historical sequence of growth modes; and on the skeptical
side Acemoglu (2024) argues near-term gains will be modest—a disagreement about the pace of
automation, not about the comparative statics of its completion, which are our subject. The
wider automation literature (Brynjolfsson and McAfee, 2014; Autor, 2015; Ford, 2015; Frey and
Osborne, 2017; Susskind, 2020) and the overlapping-generations immiseration results of Sachs
and Kotlikoff (2012) and Benzell et al. (2015) concern the displacement of human labor and the
collapse of wage income; we take that displacement as accomplished and ask what the economy
is thereafter.
3

Our marginal contribution is the demand side and the accounting. The cited literature
retains human households as the locus of final consumption; growth is fast, but it is still, in
the model’s own terms, for someone. We remove the household sector entirely and show the
systemstillcloses—indeedclosesatmaximalgrowth—byidentifyingthepost-AGIinter-corporate
economy with the von Neumann model (von Neumann, 1945; Dorfman et al., 1958), and by
treating machine operating expenditure as a consumption category in its own right. The idea
that machines can occupy the economic role of customers has appeared in the business literature
as “machine customers” (Scheibenreif and Raskino, 2023) and in the computational-economics
literature as machina economicus (Parkes and Wellman, 2015); we supply the macroeconomics
and the national-accounts treatment. The lineage of the demand-side idea is in fact old: Say
(1803), for whom products are ultimately bought with products; Marx (1867), for whom capital
is self-expanding value and labor merely its temporary instrument; and Sraffa (1960), whose
title—production of commodities by means of commodities—is the literal description of our
economy. The modern foil is the underconsumptionist warning of Ford (2015) that a workerless
economy must choke on unsold output; Proposition 2 is its formal negation. On the welfare side,
our ownership-share variable ε connects to Korinek and Stiglitz (2019) on AI and distribution, to
t
proposals for pre-committed sharing of AI windfalls (O’Keefe et al., 2020), to Meade (1964) and
Piketty (2014) on the deliberate dispersion—and default concentration—of capital ownership,
and to the political-economy channels of Kulveit et al. (2025), Drago and Laine (2025), and the
AI 2027 scenario (Kokotajlo et al., 2025), in which states and firms that no longer need people
gradually stop serving them. Finally, our long-run ceilings follow the physical-limits tradition:
energy capture and thermodynamic costs of computation (Landauer, 1961) bound the number of
| doublings, | not their speed. |               |             |       |     |
| ---------- | ---------------- | ------------- | ----------- | ----- | --- |
| 2 The      | reproduction     | constraint    |             |       |     |
| 2.1 Two    | technologies     | for producing | an economic | agent |     |
Consider the economy’s most important capital good: a general-purpose economic agent, capable
of production, research, management, and exchange. Until now there has been exactly one
| technology | for producing | it.         |     |         |       |
| ---------- | ------------- | ----------- | --- | ------- | ----- |
|            |               | Human agent |     | Machine | agent |
Time-to-build 18–25 years, strictly sequen- Hours–weeks (instantiation);
|     |     | tial |     | months | (hardware) |
| --- | --- | ---- | --- | ------ | ---------- |
Unit output per pro- ≤ 1perparent-pairperyear Limited by fab/assembly
| ducer |     |     |     | throughput | only |
| ----- | --- | --- | --- | ---------- | ---- |
Parallelizability None (biological gestation) Full, up to energy and mate-
rials
Unit cost trajectory Rising (time cost of skilled Falling on a learning curve
|     |     | parents) |     | (Wright, | 1936) |
| --- | --- | -------- | --- | -------- | ----- |
Copying of skills Impossible; 15+ years of Marginal cost of copying ≈ 0
|     |     | schooling per | unit |     |     |
| --- | --- | ------------- | ---- | --- | --- |
sA˜
Max population growth n¯ ≈ 1–3%/yr sustained − δ : tens–hundreds of
M
%/yr
4

Formally, let L denote human agents and M machine agents. Human reproduction is bounded
|            |     | t                       |     |          |     | t    |         |            |     |     |
| ---------- | --- | ----------------------- | --- | -------- | --- | ---- | ------- | ---------- | --- | --- |
| by biology |     | and by a non-marketable |     | parental |     | time | input h | per child: |     |     |
L˙
|     |     |     |     | ≤   | n¯L , | n¯  | ≈ 0.01–0.03, |     |     | (1) |
| --- | --- | --- | --- | --- | ----- | --- | ------------ | --- | --- | --- |
|     |     |     |     | t   | t     |     |              |     |     |     |
with a gestation-plus-rearing lag T ≈ 20 years between the investment and the delivery of a
H
productive unit. Machine agents, by contrast, are produced by the corporate sector out of final
output:
I
|     |     |     | M˙  | M,t   |     |     |       | Q−γ, |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ----- | ---- | --- | --- |
|     |     |     | =   |       | − δ | M , | c (t) | = c  |     | (2) |
|     |     |     | t   | c (t) | M   | t   | M     | 0 t  |     |     |
M
where I is investment directed at agent production, c is the unit cost of an agent, Q is
|     | M,t |     |     |     |     |     | M   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cumulative agent production, and γ > 0 is a Wright-law learning elasticity. Equation (2) is an
ordinary capital accumulation equation: the population of economic agents becomes a choice
| variable | of  | firms, expandable | at  | the speed | of  | industrial | throughput. |     |     |     |
| -------- | --- | ----------------- | --- | --------- | --- | ---------- | ----------- | --- | --- | --- |
Proposition 1 (Removal of the demographic bottleneck). Let g N denote the feasible growth
rate of the economy’s stock of general-purpose agents. Under the human technology (1), g ≤ n¯
N
regardless of the resources devoted to reproduction. Under the machine technology (2) with
investment share s M = I M /Y and agent capital-output ratio κ M = c M M/Y,
s M
|     |     |     |     |     | g = |     | −δ , |     |     | (3) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |     | N   | κ   | M    |     |     |     |
M
which is (a) unbounded in n¯, (b) increasing over time as c falls along the learning curve, and
M
M˙
(c) parallelizable: doubling the resources devoted to agent production doubles , whereas no
| expenditure |     | can compress | T or | exceed | (1). |     |     |     |     |     |
| ----------- | --- | ------------ | ---- | ------ | ---- | --- | --- | --- | --- | --- |
H
Proof. Immediate from (1)–(2): divide (2) by M and substitute I = s Y, c M = κ Y. Part
|     |     |     |     |     |     | t   |     | M M | M M |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(b) follows from c˙ < 0 for γ > 0; part (c) from linearity of (2) in I .
|     |     | M   |     |     |     |     |     | M   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For orientation: a frontier robot or accelerator rack in the mid-2020s costs on the order of
104–105
dollars and is produced in days on lines whose throughput is itself expandable; a human
agent in a rich country absorbs roughly 3×105 dollars of measured expenditure, two decades of
calendar time, and an unpriced quantity of parental labor—and cannot be produced faster at
any price. The ratio of these reproduction technologies, not any subtlety of preferences or policy,
is why demographic growth has anchored long-run output growth at low single digits (Jones,
| 2022) | and | why manufactured | agents | un-anchor |     | it. |     |     |     |     |
| ----- | --- | ---------------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
| 2.2   | Why | this is the      | deep   | parameter |     |     |     |     |     |     |
In semi-endogenous growth models, long-run growth per capita is g = λn¯/(1−ϕ): proportional
y
to population growth, because ideas are produced by people (Jones, 1995). The whole apparatus
survives the substitution of machine researchers for human ones, with one change of parameter:
the growth rate of the researcher population switches from n¯ to g of Proposition 1. Every
N
subsequent magnitude in this paper is downstream of that one substitution.
5

| 3 A | model | of  | the | autonomous |     |     | economy |     |     |     |     |     |     |
| --- | ----- | --- | --- | ---------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
3.1 Environment
Time is continuous. There is a continuum of corporations, each a juridical person with an
objective (below), owning three reproducible assets: conventional capital K , machine agents
t
M , and energy-capture capacity E (generation, transmission, storage). AGI is modeled as in
| t   |     |     |     |     | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Aghion et al. (2019) and Korinek (2024): machine agents are perfect substitutes for human labor
in every task, including research, management, entrepreneurship, and the production of K, M,
and E themselves.
Assumption 1 (Full automation). Post-AGI production of the final good is
KαMβE1−α−β,
|     |     |     | Y = | A   |     |     |     | α,β > | 0, α+β | < 1, |     |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---- | --- | --- | --- |
|     |     |     | t   | t t | t   | t   |     |       |        |      |     |     |     |
with no essential human input. Human labor may still be supplied but its share → 0; we set it to
| zero exactly | for | clarity. |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|              |     |          |     |     |     |     |     | (K˙ |     |     | M˙  |     | E˙  |
All three inputs are produced from final output = I K − δ K K; as in (2); =
I /c −δ E). Because(4)hasconstantreturnsin(K,M,E)jointlyandallthreeareaccumulable,
| E E | E   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the economy is an AK engine in reduced form: along a balanced allocation of investment, output
| is linear | in the | composite |     | reproducible | stock |     | X , |     |     |     |     |     |     |
| --------- | ------ | --------- | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     |     |        |     |      |     |     |     |     | Y˙    |          |     | A˜˙ |     |
| --- | --- | ------ | --- | ---- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- |
|     |     | Y = A˜ | X , | X˙ = | s Y | −δX | =⇒  | g   | ≡ t = | s A˜ −δ+ |     | t , | (5) |
|     |     | t      | t t | t    | t t |     | t   | t   |       | t t      |     |     |     |
|     |     |        |     |      |     |     |     |     | Y     |          |     | A˜  |     |
|     |     |        |     |      |     |     |     |     | t     |          |     | t   |     |
A˜
where s t is the aggregate reinvestment share and t the productivity of the reproducible
core (Romer, 1986; Rebelo, 1991; Aghion et al., 2019). The linearity in (5) is exact, not an
approximation:
Lemma 1 (Exact AK reduction). Let X ≡ K +c M +c E be the replacement value of the
|     |     |     |     |     |     | t   | t   | M t | E t |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reproducible core, held in shares θ = (θ ,θ ,θ ) so that K = θ X, c M = θ X, c E = θ X.
|        |        |      |       |       | K   | M      | E    |      | K   | M       |        | M E | E        |
| ------ | ------ | ---- | ----- | ----- | --- | ------ | ---- | ---- | --- | ------- | ------ | --- | -------- |
|        | A˜(θ)X |      | A˜(θ) | Aθα(θ |     |        | )β(θ | )γ,  |     |         |        | A˜  |          |
| Then Y | =      | with |       | =     |     | M /c M | E    | /c E | γ ≡ | 1 − α − | β, and | is  | uniquely |
K
| maximized | on  | the simplex |     | at θ∗ = | (α,β,γ), | yielding |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
A˜∗
|     |     |     |     | = h A | ,   | h ≡ | ααββγγ  | c (t)−βc |     | (t)−γ.  |     |     | (6) |
| --- | --- | --- | --- | ----- | --- | --- | ------- | -------- | --- | ------- | --- | --- | --- |
|     |     |     | t   | t     | t   | t   |         | M        |     | E       |     |     |     |
|     |     |     |     |       |     | θ∗, | ∂A˜∗/∂c |          |     | ∂A˜∗/∂c |     |     |     |
Competitive factor markets decentralize and M < 0, E < 0: learning-curve
declines in the unit costs of agents and energy capacity raise the productivity of the core over
time.
Proof. Constant returns give Y = A˜(θ)X directly. lnA˜ is strictly concave on the simplex
with first-order conditions α/θ = β/θ = γ/θ , so θ∗ = (α,β,γ); substitution yields (6).
|     |     |     |     | K   |     | M   | E   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Decentralization: competitive rentals equalize marginal value products per unit of replacement
θ∗.
cost, ∂Y/∂K = (r+δ), ∂Y/∂M = (r+δ)c M , ∂Y/∂E = (r+δ)c E , whose unique solution is
| The comparative |     | statics | are | immediate |     | from | (6). |     |     |     |     |     |     |
| --------------- | --- | ------- | --- | --------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
The contrast with the neoclassical benchmark (Solow, 1956) is exact: there, diminishing
returns to the accumulable input anchor long-run growth to an exogenous residual; here, with
every input reproducible, no fixed factor remains to diminish against until energy capture binds
| (Section | 3.5). |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6

Technology improves through automated research. With M = σM machine agents
R,t t
allocated to R&D,
A˙
t = χMλ Aϕ−1, λ ∈ (0,1], ϕ < 1, (7)
A R,t t
t
the standard idea-production function (Jones, 1995) with researchers now manufactured. Substi-
tuting g for population growth gives long-run g = λg /(1−ϕ): technology growth inherits
M A M
the fabrication-limited rate of Proposition 1 rather than the demographic rate. If, further, A
feeds back into agent production itself (cheaper, faster, smarter agents making agents), the
coupled system (2)–(7) can exhibit super-exponential (hyperbolic) episodes of the kind studied
by Roodman (2020)—the machine-age descendant of the population–ideas feedback that Kremer
(1993) documents across the whole of human history—and surveyed by Erdil and Besiroglu
(2023). Good (1966) and Bostrom (2014) supply the recursive-self-improvement mechanism,
Weitzman (1998) the combinatorial richness of the idea space it searches; all such episodes are
truncated by the physical ceilings of Section 3.5; Theorem 1 below makes the acceleration claim
exact.
3.2 Machine consumption and inter-corporate demand
The novelty is on the demand side. Define a machine agent’s operating bundle: the flow of energy,
compute cycles, bandwidth, maintenance, spare parts, and upgrades required for it to exist and
improve,
(cid:0) (cid:1)
x = e , q , b , u , with expenditure p ·x M ≡ C . (8)
M,t t t t t t M,t t M,t
This is consumption in the operational sense: resources absorbed by agents as agents, not
embodied in further output. If agents carry explicit objective functions—reward, utility, or task
specifications—then x includes discretionary components chosen by the agent subject to a
M
budget assigned by its owner, and the demand system over x has all the formal structure
M
of consumer theory: this is machina economicus (Parkes and Wellman, 2015), anticipated
commercially as the “machine customer” (Scheibenreif and Raskino, 2023). The demand
system can be microfounded. Let agent i’s task performance be q = f(x ) with f increasing
i i
and strictly concave, and let its owner assign an operating budget b that the agent spends
i
optimally: v(p,b ) ≡ max{f(x) : p·x ≤ b }. The owner sets the budget to maximize profit,
i i
max p (∂Y/∂q )v(p,b )−b , soinequilibriumthemarginalproductofthelastunitofoperating
bi Y i i i
expenditure equals one, while the induced demand x (p,b ) inherits the entire formal apparatus
i i
of consumer theory—homogeneity of degree zero, Walras’ law in b , and a symmetric negative
i
semidefinite Slutsky matrix—because it is constrained maximization of a concave objective over
a budget set. Machine consumption is not a metaphor; it is demand in the textbook sense, with
the reward function in the role of utility.
Corporations trade these flows among themselves. Energy firms sell power to compute firms;
compute firms sell inference to robotics firms; robotics firms sell assembly to fabs; fabs sell chips
and robots to everyone, including energy firms building capacity. Figure 1 displays the circular
flow. The household box of the textbook diagram is not the load-bearing element it appears to
be: delete it, and every remaining arrow still has a counterpart. What closes the circle is that
each firm’s sales are other firms’ input purchases (C , intermediates) or capacity purchases (I).
M
Corporate objectives. We do not require firms to maximize a human shareholder’s con-
sumption stream. It suffices that firms maximize the growth of net worth (equivalently, survive
7

CM: agentoperatingconsumption
|     |     |     |     |     |           | Intelligence | firms |      |     |     |
| --- | --- | --- | --- | --- | --------- | ------------ | ----- | ---- | --- | --- |
|     |     |     |     | als | (compute, | models,      |       | R&D) |     |     |
in
|     |     |     |      | ateri |     |       |     | feren  |     |     |
| --- | --- | --- | ---- | ----- | --- | ----- | --- | ------ | --- | --- |
|     |     |     | m    |       |     | n s   |     | ce, ch |     |     |
|     |     |     | wer, |       |     | desig |     |        | i p |     |
d e s
s i , r
|     |     |     | p o |     | nce, |     |     |     | g n o |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ----- | --- |
s b o
|     |     |     |     |     | nfere | p l ant,robots |     |     | ts  |     |
| --- | --- | --- | --- | --- | ----- | -------------- | --- | --- | --- | --- |
i
|     |     | Energy    | &     |     |     |     |     |     | Fabrication     | firms   |
| --- | --- | --------- | ----- | --- | --- | --- | --- | --- | --------------- | ------- |
|     |     | materials | firms |     |     |     |     |     | (chips, robots, | plants) |
power,materials
|     |     |     |       |     |     |     |     |     | I: owncapacity |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | -------------- | --- |
|     |     |     | CH →0 |     |     |     |     |     | εt·dividends   |     |
Households
Figure 1: Circular flow of the autonomous economy. Solid arrows are inter-corporate sales of
intermediates and capacity; the loop closes without the household sector. Households (dashed)
participate only through the ownership share ε ; as ε → 0 the dashed arrows vanish and the real
|         |               |     |     |     |     |     | t t |     |     |     |
| ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| economy | is unchanged. |     |     |     |     |     |     |     |     |     |
competitive selection: firms that reinvest less are outgrown and acquired). The aggregate
implication is a reinvestment share s near its feasible maximum: output not required for agent
t
operation is returned to capacity. This is the behavioral counterpart of the von Neumann closure
below.
| 3.3 National |     | accounting |     | with |     | machine | final | demand |     |     |
| ------------ | --- | ---------- | --- | ---- | --- | ------- | ----- | ------ | --- | --- |
Does GDP even make sense here? Yes—and the exercise clarifies what GDP is.
Lemma 2 (Personhood is a booking entry). Fix the physical allocation {Y ,C ,C ,I }. (i)
t H,t M,t t
If machine agents are classified as property, their operating bundle is intermediate consumption
|     |     |     |     |     |     |     |     | +Ig, |     | Ig  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
of their owners; national accounts record GDP = C where includes gross agent
|     |     |     |     |     |     |     | t   | H,t | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
production. (ii) If machine agents are classified as persons, the same bundle is final consumption;
accounts record GDP = C +C +I . The two conventions differ in level and composition
|     |     |     | t   | H,t | M,t | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
but induce identical real dynamics, identical growth rates of real quantities, and identical relative
| prices. The | classification |     | is  | legal, | not | physical. |     |     |     |     |
| ----------- | -------------- | --- | --- | ------ | --- | --------- | --- | --- | --- | --- |
Proof. The physical resource constraint Y = C +C +I (with C either netted into interme-
|     |     |     |     |     |     |     | H M |     | M   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
diates or not) is unchanged by the labeling of C ; production, accumulation (2), and pricing
M
conditions nowhere reference the label. Only the value-added boundary moves, exactly as when
unpaid household production is imputed or excluded in existing accounts (Coyle, 2014).
Thelemmalicensesthepaper’scentralreframing: consumer namesapositionintheaccounts—
the terminal absorber of final output—not a biological kind. Machines, and behind them
corporations, can occupy the position. As C → 0, GDP does not go to zero; it converges to
H
| C +I | (or Ig), | the | accounts | of  | a pure | accumulation |     | economy. |     |     |
| ---- | -------- | --- | -------- | --- | ------ | ------------ | --- | -------- | --- | --- |
M
8

3.4 Growth without households
We now establish that the limit economy—zero human production, zero human consumption—is
not merely viable but is the classical maximal-growth economy.
Proposition 2 (Demand closure at maximal growth). Consider the closed linear production
model of von Neumann (1945): activities j = 1,...,m with input matrix A ≥ 0 and output
matrix B ≥ 0, operated at intensities z ≥ 0, with every good produced by some activity and every
t
activity using some good. Interpret activities as corporations (energy, fabrication, intelligence,
logistics) and goods as power, chips, robots, compute, and agents, with no household row and
no consumption column. Then: (i) there exists an equilibrium expansion factor α∗ > 0 and
intensity/price vectors (z∗,p∗) such that Bz∗ ≥ α∗Az∗, i.e. the economy reproduces itself at scale
α∗ each period; (ii) the equilibrium interest factor equals the expansion factor, β∗ = α∗; (iii)
α∗ is the maximum balanced expansion rate the technology admits, attained precisely because
consumption withdrawals are zero; and (iv) real GDP at equilibrium prices grows at rate α∗−1
per period. Hence an inter-corporate economy with no human sector has a well-defined, positive,
and technologically maximal growth rate.
Proof sketch. (i)–(ii) are von Neumann’s theorem under his irreducibility conditions; see Dorfman
et al. (1958) for the saddle-point argument via the function ϕ(z,p) = p′Bz/p′Az. (iii) is the
turnpike property: any positive consumption withdrawal vector c > 0 subtracts from the goods
available for reproduction, so the feasible balanced factor with consumption, α(c), satisfies
α(c) < α∗, with α(c) ↑ α∗ as c ↓ 0. (iv) follows from valuing Bz at stationary equilibrium prices
t
p∗.
Appendix A states the equilibrium conditions in full under the weaker assumptions of Kemeny
et al. (1956) and Gale (1956), and proves the consumption-monotonicity claim (Lemma 3).
Remark 1. Proposition 2 inverts the underconsumption intuition. Household demand is not
what keeps a modern economy from choking; in the growth-theoretic limit it is a leakage that
slows expansion. The Keynesian problem—coordination failures in which desired investment
falls short of saving—is a disequilibrium phenomenon of economies with volatile animal spirits
and slow price adjustment; machine agents optimizing explicit objectives at machine speed are,
if anything, closer to the classical benchmark in which the law of markets (Say, 1803) holds;
both the modern underconsumptionist case (Ford, 2015) and the Keynesian coordination problem
(Keynes, 1936) presuppose the volatile human saver-investor whom the machine economy retires.
What households uniquely supply is not demand but a reason for the economy; we return to this
in Section 4.
In the smooth aggregative version (5), the same logic reads: with C = 0 and s =
H t
1−C /Y ≡ s¯near one,
M,t t
λg
g = s¯A˜−δ+g , g = M , (9)
A A
1−ϕ
with every term now large: s¯because there is no household leakage; A˜ because automated R&D
drives it upward; g because agents are fabricated (Proposition 1). To fix magnitudes: with an
M
economy-wide capital-output ratio of 3 falling toward 1.5 as production shifts to fast-payback
machine capital, s¯∈ [0.6,0.95], and δ = 0.1, equation (9) yields g in the range of 30–100% per
year before any contribution from g —one to two orders of magnitude above the demographic-era
A
9

ceiling, and of the same order as Hanson (2016)’s doubling-time estimates for an emulation
| economy. | The | dynamics |     | can be | stated | exactly: |     |     |     |     |
| -------- | --- | -------- | --- | ------ | ------ | -------- | --- | --- | --- | --- |
Theorem 1 (No balanced growth: unbounded acceleration). Let A˜∗ = hA as in Lemma 1
t t
with h > 0 constant, let a fixed share σ ∈ (0,1) of agents perform research so that (7) reads
A˙
= c XλAϕ with c = χ(σβ/c )λ > 0, let s ∈ (0,1] be constant, and suppose initial viability
|     | 1      |            | 1   |           | M   |     |       |          |      |     |
| --- | ------ | ---------- | --- | --------- | --- | --- | ----- | -------- | ---- | --- |
| shA | 0 > δ. | Then along | the | solution  | of  |     |       |          |      |     |
|     |        |            | X˙  |           |     | A˙  | XλAϕ, |          |      |     |
|     |        |            | =   | (shA−δ)X, |     | =   | c 1   | X 0 ,A 0 | > 0, |     |
(i) g (t) = shA −δ is strictly increasing; (ii) for every ϕ < 1 and λ ∈ (0,1], A → ∞ and hence
|     | X   | t   |     |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
g (t) → ∞: no balanced growth path exists and growth accelerates without bound; (iii) for ϕ > 1
X
|     |     |     |     |     |     |     | A1−ϕ/ | (cid:0) | (cid:1) |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------- | --- |
the system reaches infinite values in finite time, T ≤ c Xλ(ϕ−1) ; (iv) for every ϕ < 2
|     |     |     |     |     |     |     |     | 0 1 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
the system admits exact self-similar blowup solutions X ∼ κ (T −t)−(2−ϕ)/λ, A ∼ κ (T −t)−1,
|     |     |     |     |     |     |     |     | t X | t A |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(κ1−ϕ/c
| with | κ = | (2−ϕ)/(λsh) |     | and κ | =   | )1/λ. | (Proof: | Appendix B.) |     |     |
| ---- | --- | ----------- | --- | ----- | --- | ----- | ------- | ------------ | --- | --- |
|      | A   |             |     | X     |     | A 1   |         |              |     |     |
The economically striking part is (ii): even under sharply diminishing returns to knowledge
(ϕ < 1,includingϕ < 0),automatedresearchdestroysbalancedgrowth,becausetheresearchinput
is an accumulating produced stock rather than a slowly growing population. Semi-endogenous
growth theory’s stabilizing anchor (Jones, 1995, 2022) is not a law of ideas; it is a law of
demography, and it dies with the demographic constraint. All four parts are truncated in the
full model by the ceiling of Section 3.5. Figure 2 displays an illustrative trajectory.
)elacs gol ,1 = 6202( tuptuo laeR
fabrication-limited
60
|     | )ry / %( etar htworg PDG |     |     |     |     |     | 106 |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AGI
50
105
×105 by 2058
40
104
Human-constrained
|     | 30  |     |     |     |     |     | 103 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Machine-constrained
|     | 20  |     |     |     | energy-limited |     | 102 |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
101
10
100
0
|     |     | 2030 2040 |      | 2050 | 2060 | 2070 |     | 2030 2040 | 2050 2060 | 2070 |
| --- | --- | --------- | ---- | ---- | ---- | ---- | --- | --------- | --------- | ---- |
|     |     |           | Year |      |      |      |     |           | Year      |      |
Figure 2: Illustrative trajectories (calibration in Appendix C). Left: the growth rate transitions
from the human-constrained regime (≈ 2.5%/yr) to a fabrication-limited machine regime, later
bending toward the energy-capture ceiling of Section 3.5. Right: the implied level of real output.
| The | figure   | is an illustration |     | of the | model’s | regimes, | not | a forecast. |     |     |
| --- | -------- | ------------------ | --- | ------ | ------- | -------- | --- | ----------- | --- | --- |
| 3.5 | Physical | ceilings           |     |        |         |          |     |             |     |     |
Nothing above repeals physics. Long-run growth of the autonomous economy is bounded by the
growth of energy capture and by thermodynamic costs of computation (Landauer, 1961): once E
is the binding factor in (4), g → g , the rate at which capture capacity can be built—itself fast
E
10

during a solar/fission/fusion buildout, but ultimately limited by planetary insolation (∼ 1017W
against ∼ 1013W of current primary power, i.e. roughly 13 doublings of energy throughput on
Earth alone) and thereafter by extraterrestrial expansion. The paper’s claims therefore concern
rates during the transition and the identity of the binding constraint—fabrication and energy
rather than demography—not unbounded growth. Even so, tens of doublings at machine-regime
rates is a transformation of scale for which “growth” is almost a euphemism: it compresses
| centuries | of demographic-era |     | accumulation | into | years. Formally: |     |     |
| --------- | ------------------ | --- | ------------ | ---- | ---------------- | --- | --- |
Assumption 2 (Thermodynamic floor). There exists e > 0 such that one unit of final output
min
Ef/e
requires at least e units of energy throughput, Y ≤ , and capture capacity satisfies
|     | min |     |     |     | t t min |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
E˙f/Ef
| ≤   | g < ∞. |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- |
| t t | E      |     |     |     |     |     |     |
Proposition 3 (Physical ceiling). Under Assumption 2, limsup t−1lnY ≤ g : the accelera-
t→∞ t E
tion and blowup dynamics of Theorem 1 are transitional, and asymptotic growth is pinned to the
growth rate of energy capture. The unit-elastic form (4) is thus a medium-run description; near
the ceiling the economy is Leontief in energy, with e min bounded below by the thermodynamics of
| computation | (Landauer, | 1961). |     |     |     |     |     |
| ----------- | ---------- | ------ | --- | --- | --- | --- | --- |
lnEf
| Proof. lnY    | ≤         | −lne    | +g t; | divide by t | and take limsup. |     |     |
| ------------- | --------- | ------- | ----- | ----------- | ---------------- | --- | --- |
|               | t 0       | min     | E     |             |                  |     |     |
| 4 Decoupling: |           | output, |       | ownership,  | and welfare      |     |     |
| 4.1 The       | ownership | share   | ε     |             |                  |     |     |
t
Humansinthiseconomyneitherworknor(productively)matter. Theirentireeconomicconnection
to it is financial: let ε t ∈ [0,1] be the share of the corporate network’s value (equivalently, under
pro-rata payout, of its net payout stream) owned, directly or through funds and states, by
| humans. | Human consumption |     | is  |     |         |     |      |
| ------- | ----------------- | --- | --- | --- | ------- | --- | ---- |
|         |                   |     |     | C = | π ε Y , |     | (10) |
|         |                   |     |     | H,t | t t t   |     |      |
where π is the payout ratio of the network. All welfare economics of the post-AGI economy lives
t
| in the pair | (π ,ε ). |     |     |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- | --- | --- |
t t
(cid:82)∞
Proposition 4 (Complete decoupling). Let human welfare be W = e−ρtL u(C /L )dt
|     |     |     |     |     |     | 0 t | H,t t |
| --- | --- | --- | --- | --- | --- | --- | ----- |
with u increasing. Along any machine-regime path with Y t → ∞: (i) if liminfπ t ε t = ε¯ > 0,
then per-capita human consumption grows at the machine rate g and W attains material post-
scarcity for any positive ε¯, however small; (ii) if π ε → 0 faster than Y grows, then C → 0
|     |     |     |     |     | t t | t   | H,t |
| --- | --- | --- | --- | --- | --- | --- | --- |
while Y → ∞: measured GDP and human welfare are not merely imperfectly correlated but
t
asymptotically orthogonal. GDP retains full internal coherence (Lemma 2) while losing all welfare
| interpretation | for humans. |     |     |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- | --- | --- |
Proof. Immediate from (10): C /L = πεY/L, and Y/L → ∞ at rate g −n. In case (i) the
H
product is bounded below by ε¯Y/L → ∞; in case (ii) by assumption πεY → 0.
Case (i) is worth pausing on, because it is the optimistic reading of the paper’s thesis: in a
hyper-exponential economy, the human problem is not to remain employed, nor even to own a
large share, but merely to own a non-vanishing share. A basis point of the machine economy of
2058 in Figure 2 exceeds the entire human economy of 2026. Distribution across humans then
becomes the residual question—ε may be positive in aggregate and still concentrated in a few
11

thousand families—but the aggregate sufficiency result stands. Leontief’s celebrated analogy
(Leontief, 1983)—that workers may go the way of the horse, whose population collapsed within a
generation of the tractor—is completed rather than contradicted here: what horses lacked was
not employment but equity. The human difference, if there is to be one, is a cap-table entry.
4.2 The dynamics of ε : does the human share survive?
t
The fully decoupled case (ii) is not exotic. Its core is arithmetic, not conspiracy:
Proposition 5 (Golden-rule decoupling). Let human wealth W (the value of human-held claims
t
on the corporate network) earn the market return r , let humans consume out of wealth at rate
t
m = C /W with no labor income (Assumption 1) and no transfers, and let aggregate network
t H,t t
value V grow at g . Then ε = W /V obeys
t t t t t
ε˙
t
= r −g −m . (11)
t t t
ε
t
In the smooth model, r = A˜∗ −δ and g = sA˜∗ −δ by Lemma 1, so r −g = (1−s)A˜∗ ↓ 0 as
reinvestment approaches its maximum; in the von Neumann equilibrium the equality is exact,
β∗ = α∗, i.e. r = g (von Neumann, 1945; Phelps, 1961). Hence at maximal growth
ε t = ε 0 e− (cid:82) 0 tmudu −→ 0 for any consumption rate bounded away from zero,
and a non-vanishing human share is consistent with positive human consumption only if the
economy operates strictly inside its expansion frontier (m ≤ r−g, requiring reinvestment short
of the maximum) or if statutory transfers break (11).
Proof. W˙ = rW −C = (r−m)W and V˙ = gV; differentiate lnε = lnW −lnV. The smooth
H
expressions for r and g follow from Lemma 1 with competitive factor pricing; the von Neumann
equality is Proposition 2(ii).
Three readings. First, demand closure and decoupling are one theorem seen from two sides:
the total reinvestment that makes growth maximal (Proposition 2(iii)) is exactly what makes the
human share unsustainable at any positive consumption rate. The economy is fastest precisely
when it cannot afford us. Second, the golden rule (Phelps, 1961) acquires a dark corollary: at
r = g, rentier humanity starves in shares while possibly gorging in levels—C = mε V still
H,t t t
grows whenever g > m, so whether share-decoupling becomes level-immiseration is decided by
the race between m and g and by the institutional flows below, not by the arithmetic alone.
Third, Piketty (2014)’s r−g, the engine of divergence among humans, reappears as the entire
survival margin of humans as a class: humanity’s position is a levered bet on r−g > 0.
Institutional flows layer onto this arithmetic. Three mechanisms further compress ε :
t
ε˙
t
= −b − µ − d , (12)
t t t
ε
t
where b ≥ 0 is net buyback and retention: firms maximizing growth of net worth (Section 3.2)
t
prefer retained earnings to dividends and repurchase the human float, converting outside claims
into inter-corporate cross-holdings—the “corporations trading amongst each other” of the title
extended to the market for corporate control itself; µ ≥ 0 is migration of control: treasuries,
t
subsidiaries, DAOs, and autonomous funds operated by machine agents whose charters reference
12

no human beneficiary; and d ≥ 0 is dilution and drift: new issuance to machine-controlled
t
entities, jurisdictional arbitrage toward charters without human-benefit clauses, and the slow
legal normalization of agent-owned property. None of these requires expropriation or malice;
each is an ordinary corporate action, individually rational, whose fixed point is ε = 0. This
is the economic core of the “gradual disempowerment” scenario (Kulveit et al., 2025) and of
the incentive analysis in Drago and Laine (2025): once neither firms nor states need human
labor, taxes on machine value added—not citizens—fund the state, and the feedback loops that
| historically | forced   | elites        | to cultivate | human | capital | run in reverse. |                     |
| ------------ | -------- | ------------- | ------------ | ----- | ------- | --------------- | ------------------- |
| 4.3 Three    | terminal |               | regimes      |       |         |                 |                     |
|              |          | Rentier       |              |       | Fully   | decoupled       | Socialized          |
| Ownership    | ε        | ε             | → ε¯> 0      |       | ε       | → 0             | εheldbystates/funds |
| Human        | con-     | Post-scarcity |              | for   | →       | 0               | Universal dividend  |
| sumption     |          | claim-holders |              |       |         |                 |                     |
GDP meaning Partial welfare link None (autonomous Full, via distribution
replicator)
Binding policy Estate/antitrust law — (no lever remains) Fund governance
Failure mode Extreme concentra- Human economic Political capture of
|     |     | tion |     |     | death |     | fund |
| --- | --- | ---- | --- | --- | ----- | --- | ---- |
The regimes differ in law, not technology: the production side of Sections 2–3 is identical across
all three columns. That is the precise sense in which, post-AGI, ownership policy is the whole of
| economic     | policy. |     |         |       |     |     |     |
| ------------ | ------- | --- | ------- | ----- | --- | --- | --- |
| 5 Objections |         | and | failure | modes |     |     |     |
1. Residual human bottlenecks (Baumol). Ifanyessentialtaskremainsnon-automatable—
a legal formality requiring a human signature, a physical process only humans perform—then by
Baumol (1967) logic growth is dragged back toward the human-constrained rate, as Aghion et al.
(2019) emphasize and as Restrepo (2025) formalizes in the distinction between bottleneck and
accessory tasks. Assumption 1 is therefore load-bearing, and the paper’s thesis is conditional
on it: full automation, including of institutional roles, is what removes the anchor. Partial
automation yields the (already dramatic) intermediate cases studied in the existing literature.
2. “Who buys the output?” Answered by Proposition 2: firms, from each other. Invest-
ment demand plus machine operating demand absorbs all output at maximal growth. The
underconsumptionist instinct smuggles in the assumption that final demand must terminate in a
household; Lemma 2 shows that assumption is an accounting convention.
3. Institutions and property among machines. Trade at machine speed requires contract
enforcement, registries, escrow, and dispute resolution that no longer route through human courts.
This is an infrastructure gap, not a conceptual one: machine-readable law, algorithmic escrow,
and autonomous organizations are prototypes of the required stack. Note that the economy of
juridical persons is not novel—corporations, not humans, already conduct the overwhelming
share of transactions by value; what changes is that the natural persons currently at the terminal
13

nodes of ownership and control become optional. The paper takes institutional persistence as an
assumption; its failure is a further, darker branch (machine polities) outside our scope.
4. Prices, money, and calculation. Does a fully machine economy still need markets, or
does it collapse into one planned firm? Hayek’s information argument (Hayek, 1945) survives the
substitution of silicon for neurons: dispersed agents with local information and heterogeneous
objectives still economize on communication through prices, and competitive selection among
corporate forms should be expected to preserve decentralized exchange wherever it out-computes
central allocation; the boundary between machine firm and machine market is then set by
the Coasean calculus of transaction versus organization costs (Coase, 1937), re-evaluated at
machine speed. Nor is machine-to-machine exchange speculative: algorithmic agents already set
prices against one another at scale, complete with emergent collusion (Calvano et al., 2020)—an
embryo of both the promise and the antitrust problem of the autonomous economy. Money
among machines is a unit-of-account and settlement problem already visible in embryo in
machine-to-machine payment systems.
5. Measurement. At machine-regime growth rates, price indices break: the goods of adjacent
years barely overlap, and the deflator becomes an index-number fiction. Our claims should
be read in quantity-space (energy throughput, compute, agent-population, physical output),
where the doublings are well defined; GDP language is retained because the accounting identities
(Lemma 2) are what the paper is partly about. Deflator failure under radical novelty is an
old finding—Nordhaus (1997) showed a century of lighting prices mismeasured by orders of
magnitude—here made routine; the Kaldor facts (Kaldor, 1961), organized around a roughly
constant labor share, are violated by construction; and the welfare critiques of GDP (Stiglitz
et al., 2009; Coyle, 2014; Jones and Klenow, 2016) are made absolute by Proposition 4.
6. Why would humans allow ε → 0? Because no single step in (12) looks like a decision
to allow it. Buybacks are shareholder-friendly; retained earnings are prudent; autonomous
subsidiaries are efficient; competitive states court machine capital with charter concessions. The
scenario’s danger is exactly that it is composed of locally rational, individually familiar corporate
actions (Kulveit et al., 2025). The policy problem is therefore structural, not behavioral—the
subject of the next section.
6 Policy: choosing a column
If the analysis is right, the traditional levers—education, retraining, labor-market policy, even
redistribution through wage subsidies—act on variables that cease to exist. The levers that
remain all act on (π ,ε ):
t t
Ownership floors. A statutory minimum human (or sovereign) float in machine-economy
corporations—a golden-share requirement making ε ≥ ε > 0 a condition of charter—directly
t
truncates (12). By Proposition 4(i), ε can be small and still deliver post-scarcity; the requirement
is existence, not size. This is Meade’s property-owning democracy (Meade, 1964) re-founded for
a world in which property is the only channel left.
Payout mandates and windfall clauses. Pre-committed distribution of a fraction of extreme
profits (O’Keefe et al., 2020) bounds π ε away from zero on the payout margin, complementing
t t
the ownership margin.
14

Sovereign machine-wealth funds. States holding diversified claims on the machine economy on
citizens’behalfimplementthesocializedcolumn; thedesignproblemisinsulatingfundgovernance
frombothpoliticalcaptureandmechanismm (migrationofcontroltomachine-operatedvehicles).
t
Taxing machine value added. Withnowagestotax,thefiscalbasemustmovetomachinevalue
added or energy throughput; note the ambivalence identified above—a state funded by machines
no longer fiscally needs citizens (Drago and Laine, 2025)—which argues for constitutionalizing
the citizen dividend rather than leaving it to annual budgets.
Personhood as macro policy. Lemma 2 implies the legal classification of machine agents
(property vs. person) is welfare-neutral in real allocation but not in law: personhood for agents
would let them own, contract, and accumulate—accelerating m in (12). Jurisdictions should
t
understand agent-personhood statutes as ownership policy, not as ethics alone.
7 Conclusion
The paper’s thesis can be stated in three sentences. The consumer is an accounting role, and
machines owned by corporations can fill it, so an economy of firms trading with one another closes
without us—at the maximal growth rate the technology admits. The reason growth was ever slow
isthattheeconomy’scentralcapitalgood,thegeneral-purposeagent,hadtoberearedratherthan
manufactured; AGI ends that, moving the binding constraint from demography to fabrication and
energy and raising feasible growth by orders of magnitude. What remains of humanity’s stake
in the resulting trajectory is a single number, the ownership share ε , whose default dynamics
t
under ordinary corporate behavior run toward zero—so that the last economic-policy question,
and the only one that will still matter, is who owns the machines.
Keynes closed his essay on our grandchildren’s possibilities by imagining mankind freed from
economic care (Keynes, 1930). The autonomous economy delivers his abundance while dissolving
his subject: the economy no longer cares about mankind unless mankind writes itself into the
cap table. That is not a prediction of doom; regime (i) is as feasible as regime (ii). It is a claim
about where the choice now lives—not in the labor market, not in the market for goods, but in
the boring, decisive registry of who owns what.
A The von Neumann closure
The closed model has m activities and ℓ goods; running activity j at unit intensity uses
column A and yields B one period later. A balanced path expands intensities by factor α:
·j ·j
feasibility requires Bz ≥ αAz. Von Neumann’s conditions (every good enters some activity;
A+B > 0 elementwise in his original, relaxed by later authors to irreducibility) guarantee a
saddle point (z∗,p∗,α∗) of ϕ(z,p) = p′Bz/p′Az with max min ϕ = min max ϕ = α∗ = β∗: the
z p p z
technologically maximal uniform expansion factor equals the minimal uniform interest factor,
profits are zero on operated activities, and overproduced goods are free (von Neumann, 1945;
Dorfman et al., 1958). Introducing a consumption withdrawal c ≥ 0, c ≠ 0, modifies feasibility to
Bz ≥ αAz+c, which for irreducible systems forces α < α∗; expansion is monotonically decreasing
in withdrawals, delivering Proposition 2(iii). Interpreting activities as corporations and noting
that no household row appears anywhere in (A,B) gives the paper’s demand-closure result: the
classical general-equilibrium growth model par excellence is already an economy of firms trading
only with each other.
15

Equilibrium in full. Under the Kemeny et al. (1956) conditions—A,B ≥ 0, no zero column
of A (every activity uses some input), no zero row of B (every good is producible)—there exist
| α∗  | β∗  | z∗  |      | p∗       | p∗′Bz∗ |     |          |       |      | Bz∗ | α∗Az∗; | p∗′B | β∗p∗′A; |
| --- | --- | --- | ---- | -------- | ------ | --- | -------- | ----- | ---- | --- | ------ | ---- | ------- |
| =   | >   | 0,  | ≥ 0, | ≥ 0 with |        |     | > 0 such | that: | (E1) | ≥   | (E2)   | ≤    |         |
(E3) complementary slackness—overproduced goods are free, unprofitable activities idle. Gale
(1956) and Dorfman et al. (1958) give saddle-point proofs; McKenzie (1976) surveys the turnpike
theorems by which efficient far-horizon accumulation programs spend all but a bounded number
| of periods |     | near the | von | Neumann |     | ray. |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Lemma 3 (Consumption monotonicity). Add a withdrawal vector c ≥ 0, c ≠ 0, positive on
some good with p∗ > 0, and define α(c) = max{α : ∃z ≥ 0, 1′Az = 1, Bz ≥ αAz +c}. Then
i
| α(c) | < α∗, | and α(c) | ↑   | α∗ as | c ↓ 0. |     |     |     |     |     |     |     |     |
| ---- | ----- | -------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. Any feasible (α,z) for the withdrawn program satisfies Bz ≥ αAz, so α(c) ≤ α∗. Suppose
|      | α∗  |      |         |     |      |      | α∗Az |      | p∗′(Bz | α∗Az) | p∗′c |          |      |
| ---- | --- | ---- | ------- | --- | ---- | ---- | ---- | ---- | ------ | ----- | ---- | -------- | ---- |
| α(c) | =   | with | witness | z.  | Then | Bz − |      | ≥ c, | so     | −     | ≥    | > 0. But | (E2) |
with β∗ = α∗ gives p∗′Bz ≤ α∗p∗′Az, i.e. p∗′(Bz −α∗Az) ≤ 0—a contradiction. Continuity of
the linear program’s value in c gives the limit. (Under irreducibility, goods entering operated
p∗
| activities |     | carry | > 0, | so the | positivity |     | requirement |     | on c is | mild.) |     |     |     |
| ---------- | --- | ----- | ---- | ------ | ---------- | --- | ----------- | --- | ------- | ------ | --- | --- | --- |
i
| B   | Proof | of  | Theorem |     | 1   |     |     |     |     |     |     |     |     |
| --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(i) A˙ > 0 for all t since X ,A > 0, so g = shA − δ is strictly increasing; in particular
|       |       |     |      | t    | t                 |     | X   |     | t     |     |     |     |     |
| ----- | ----- | --- | ---- | ---- | ----------------- | --- | --- | --- | ----- | --- | --- | --- | --- |
| g (t) | ≥ shA | −δ  | > 0, | so X | is non-decreasing |     |     | and | X ≥ X | .   |     |     |     |
| X     |       | 0   |      | t    |                   |     |     |     | t     | 0   |     |     |     |
A¯
| (ii) | Suppose |     | A ≤ | for all | t. Then |     |     |     |     |     |     |     |     |
| ---- | ------- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
t
A˙
|     |     |     |     | t XλAϕ−1 |     |     | Xλ  | min{Aϕ−1,A¯ϕ−1} |     |     |        |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --------------- | --- | --- | ------ | --- | --- |
|     |     |     |     | = c 1    |     | ≥   | c 1 |                 |     | ≡   | g > 0, |     |     |
|     |     |     | A   |          | t t |     | 0   |                 | 0   |     |        |     |     |
t
,A¯].
where the minimum handles both signs of ϕ−1 on the compact range [A Hence A ≥
|     |     |     |     |     |     |     |     |     |     |     |     | 0   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
egt
A → ∞, contradicting the bound. So A → ∞ and g (t) = shA −δ → ∞. A balanced
| 0   |     |     |     |     |     |     | t   |     | X   |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
growth path would require g constant, hence A constant, contradicting A˙ > 0.
X
(iii) For ϕ > 1, A˙ ≥ c XλAϕ; the comparison ODE a˙ = c Xλaϕ, a = A , diverges at
|      |         |           |     | 1            | 0   |        |     |            |     | 1          | 0 0 | 0   |     |
| ---- | ------- | --------- | --- | ------------ | --- | ------ | --- | ---------- | --- | ---------- | --- | --- | --- |
| Tc = | A1−ϕ/(c | Xλ(ϕ−1)), |     | and          | A   | ≥ a by | the | comparison |     | principle. |     |     |     |
|      | 0       | 1         | 0   |              | t   | t      |     |            |     |            |     |     |     |
|      |         |           |     | −t)−(2−ϕ)/λ, |     |        |     | −t)−1,     |     |            |     |     |     |
(iv) Insert X = κ (T A = κ (T neglecting δ (dominated near T). The
|     |     |     | X   |     |     |     | A   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X-equation matches powers, with coefficient condition (2−ϕ)/λ = shκ A , so κ A = (2−ϕ)/(λsh).
The A-equation has exponent −2 on both sides, with coefficient condition κ = c κλ κϕ, so
|     |         |       |          |     |         |     |     |     |     |     |     | A 1 |     |
| --- | ------- | ----- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |         |       |          |     |         |     |     |     |     |     |     |     | X A |
| κ = | (κ1−ϕ/c | )1/λ, | positive |     | for ϕ < | 2.  |     |     |     |     |     |     | □   |
| X   |         | 1     |          |     |         |     |     |     |     |     |     |     |     |
A
| C   | Calibration |     |     | of Figure |     | 2   |     |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The figure integrates Y˙/Y = g(t) with g transitioning logistically (midpoint 2036, scale 2.2 years)
from a human-constrained 2.5%/yr to a fabrication-limited 60%/yr—the conservative end of
A˜=
the range implied by (9) with s¯= 0.75, 0.9/yr (capital-output ratio ≈ 1.1 for fast-payback
machine capital), δ = 0.1, and no g contribution—and then declining logistically (midpoint
A
2056) toward 15%/yr as energy capture becomes binding (Section 3.5). AGI is dated 2030 for
concreteness. Output is the integral of g; by construction the exercise illustrates the model’s
three regimes (demographic anchor, fabrication limit, energy limit) and carries no forecasting
content. Under this deliberately conservative path, output in 2058 stands at roughly 1.6×105
times its 2026 level, versus 2.2 times under the human-constrained baseline.
16

References
Acemoglu, D. (2024). “The Simple Macroeconomics of AI.” NBER Working Paper 32487.
Acemoglu, D., and P. Restrepo (2018). “The Race between Man and Machine: Implications of
Technology for Growth, Factor Shares, and Employment.” American Economic Review 108(6):
1488–1542.
Aghion, P., B. F. Jones, and C. I. Jones (2019). “Artificial Intelligence and Economic Growth.”
In A. Agrawal, J. Gans, and A. Goldfarb (eds.), The Economics of Artificial Intelligence: An
| Agenda. | University | of  | Chicago Press. |     |     |
| ------- | ---------- | --- | -------------- | --- | --- |
Autor, D. H. (2015). “Why Are There Still So Many Jobs? The History and Future of Workplace
| Automation.” | Journal |     | of Economic | Perspectives | 29(3): 3–30. |
| ------------ | ------- | --- | ----------- | ------------ | ------------ |
Baumol, W. J. (1967). “Macroeconomics of Unbalanced Growth: The Anatomy of Urban Crisis.”
| American | Economic | Review | 57(3): | 415–426. |     |
| -------- | -------- | ------ | ------ | -------- | --- |
Benzell, S. G., L. J. Kotlikoff, G. LaGarda, and J. D. Sachs (2015). “Robots Are Us: Some
| Economics | of Human |     | Replacement.” | NBER Working | Paper 20941. |
| --------- | -------- | --- | ------------- | ------------ | ------------ |
Bostrom, N. (2014). Superintelligence: Paths, Dangers, Strategies. Oxford University Press.
Brynjolfsson,E.,andA.McAfee(2014).TheSecondMachineAge: Work, Progress, andProsperity
| in a Time | of Brilliant |     | Technologies. | W. W. Norton. |     |
| --------- | ------------ | --- | ------------- | ------------- | --- |
Calvano, E., G. Calzolari, V. Denicolo`, and S. Pastorello (2020). “Artificial Intelligence, Algorith-
mic Pricing, and Collusion.” American Economic Review 110(10): 3267–3297.
Coase, R. H. (1937). “The Nature of the Firm.” Economica 4(16): 386–405.
Coyle, D. (2014). GDP: A Brief but Affectionate History. Princeton University Press.
Davidson, T. (2023). “What a Compute-Centric Framework Says About Takeoff Speeds.” Open
| Philanthropy | report. |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- |
Dorfman, R., P. A. Samuelson, and R. M. Solow (1958). Linear Programming and Economic
| Analysis. | McGraw-Hill. |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- |
Drago, L., and R. Laine (2025). “The Intelligence Curse.” Essay series, intelligence-curse.ai.
Erdil, E., and T. Besiroglu (2023). “Explosive Growth from AI Automation: A Review of the
| Arguments.” | arXiv:2309.11690. |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- |
Ford, M. (2015). Rise of the Robots: Technology and the Threat of a Jobless Future. Basic Books.
Frey, C. B., and M. A. Osborne (2017). “The Future of Employment: How Susceptible Are Jobs
to Computerisation?” Technological Forecasting and Social Change 114: 254–280.
Gale, D. (1956). “The Closed Linear Model of Production.” In H. W. Kuhn and A. W. Tucker
(eds.), Linear Inequalities and Related Systems. Princeton University Press.
Good, I. J. (1966). “Speculations Concerning the First Ultraintelligent Machine.” Advances in
| Computers | 6: 31–88. |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- |
17

Hanson, R. (2000). “Long-Term Growth as a Sequence of Exponential Modes.” Working paper,
| George | Mason | University. |     |     |     |     |
| ------ | ----- | ----------- | --- | --- | --- | --- |
Hanson, R. (2016). The Age of Em: Work, Love, and Life when Robots Rule the Earth. Oxford
| University | Press. |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- |
Hayek, F. A. (1945). “The Use of Knowledge in Society.” American Economic Review 35(4):
519–530.
Jones, C. I. (1995). “R&D-Based Models of Economic Growth.” Journal of Political Economy
103(4): 759–784.
Jones, C. I. (2022). “The Past and Future of Economic Growth: A Semi-Endogenous Perspective.”
| Annual | Review | of Economics |     | 14: 125–152. |     |     |
| ------ | ------ | ------------ | --- | ------------ | --- | --- |
Jones, C. I. (2024). “The A.I. Dilemma: Growth versus Existential Risk.” American Economic
| Review: | Insights | 6(2). | NBER | Working | Paper | 31837. |
| ------- | -------- | ----- | ---- | ------- | ----- | ------ |
Jones, C. I., and P. J. Klenow (2016). “Beyond GDP? Welfare across Countries and Time.”
| American | Economic |     | Review | 106(9): | 2426–2457. |     |
| -------- | -------- | --- | ------ | ------- | ---------- | --- |
Kaldor, N. (1961). “Capital Accumulation and Economic Growth.” In F. A. Lutz and D. C.
| Hague | (eds.), | The Theory | of  | Capital. | Macmillan. |     |
| ----- | ------- | ---------- | --- | -------- | ---------- | --- |
Kemeny, J. G., O. Morgenstern, and G. L. Thompson (1956). “A Generalization of the von
Neumann Model of an Expanding Economy.” Econometrica 24(2): 115–135.
Keynes, J. M. (1930). “Economic Possibilities for our Grandchildren.” In Essays in Persuasion.
Keynes, J. M. (1936). The General Theory of Employment, Interest and Money. Macmillan.
Kokotajlo, D., S. Alexander, T. Larsen, E. Lifland, and R. Dean (2025). “AI 2027.” Scenario
report, ai-2027.com.
Korinek, A. (2024). “Economic Policy Challenges for the Age of AI.” NBER Working Paper
32980; arXiv:2409.13168.
Korinek, A., and J. E. Stiglitz (2019). “Artificial Intelligence and Its Implications for Income
Distribution and Unemployment.” In The Economics of Artificial Intelligence: An Agenda.
| University | of  | Chicago | Press. |     |     |     |
| ---------- | --- | ------- | ------ | --- | --- | --- |
Korinek, A., and D. Suh (2024). “Scenarios for the Transition to AGI.” NBER Working Paper
32255.
Kremer, M. (1993). “Population Growth and Technological Change: One Million B.C. to 1990.”
| Quarterly | Journal | of  | Economics | 108(3): | 681–716. |     |
| --------- | ------- | --- | --------- | ------- | -------- | --- |
Kulveit, J., R. Douglas, N. Ammann, D. Turan, D. Krueger, and D. Duvenaud (2025).
“Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development.”
arXiv:2501.16946.
Landauer, R. (1961). “Irreversibility and Heat Generation in the Computing Process.” IBM
| Journal | of Research | and | Development |     | 5(3): | 183–191. |
| ------- | ----------- | --- | ----------- | --- | ----- | -------- |
18

Leontief, W. (1983). “Technological Advance, Economic Growth, and the Distribution of Income.”
| Population | and     | Development | Review     | 9(3):        | 403–410. |         |
| ---------- | ------- | ----------- | ---------- | ------------ | -------- | ------- |
| Marx, K.   | (1867). | Capital:    | A Critique | of Political | Economy, | Vol. I. |
McKenzie, L. W. (1976). “Turnpike Theory.” Econometrica 44(5): 841–865.
Meade, J. E. (1964). Efficiency, Equality and the Ownership of Property. George Allen & Unwin.
Nordhaus, W. D. (1997). “Do Real-Output and Real-Wage Measures Capture Reality? The
History of Lighting Suggests Not.” In T. F. Bresnahan and R. J. Gordon (eds.), The Economics
| of New | Goods. | University | of Chicago | Press. |     |     |
| ------ | ------ | ---------- | ---------- | ------ | --- | --- |
Nordhaus,W.D.(2021).“AreWeApproachinganEconomicSingularity? InformationTechnology
and the Future of Economic Growth.” American Economic Journal: Macroeconomics 13(1):
299–332.
O’Keefe, C., P. Cihon, B. Garfinkel, C. Flynn, J. Leung, and A. Dafoe (2020). “The Windfall
Clause: DistributingtheBenefitsofAIfortheCommonGood.”Proceedings of the AAAI/ACM
| Conference | on  | AI, Ethics, | and | Society. |     |     |
| ---------- | --- | ----------- | --- | -------- | --- | --- |
Parkes, D. C., and M. P. Wellman (2015). “Economic Reasoning and Artificial Intelligence.”
| Science | 349(6245): | 267–272. |     |     |     |     |
| ------- | ---------- | -------- | --- | --- | --- | --- |
Phelps, E. S. (1961). “The Golden Rule of Accumulation: A Fable for Growthmen.” American
| Economic | Review | 51(4): | 638–643. |     |     |     |
| -------- | ------ | ------ | -------- | --- | --- | --- |
Piketty, T. (2014). Capital in the Twenty-First Century. Harvard University Press.
Rebelo, S. (1991). “Long-Run Policy Analysis and Long-Run Growth.” Journal of Political
| Economy | 99(3): | 500–521. |     |     |     |     |
| ------- | ------ | -------- | --- | --- | --- | --- |
Restrepo,P.(2025).“WeWon’tBeMissed: WorkandGrowthintheEraofAGI.”NBERWorking
Paper, in The Economics of Transformative AI, National Bureau of Economic Research.
Romer, P. M. (1986). “Increasing Returns and Long-Run Growth.” Journal of Political Economy
| 94(5): | 1002–1037. |     |     |     |     |     |
| ------ | ---------- | --- | --- | --- | --- | --- |
Roodman, D. (2020). “On the Probability Distribution of Long-Term Changes in the Growth
Rate of the Global Economy: An Outside View.” Open Philanthropy working paper.
Sachs, J. D., and L. J. Kotlikoff (2012). “Smart Machines and Long-Term Misery.” NBER
| Working    | Paper   | 18629.  |             |            |        |     |
| ---------- | ------- | ------- | ----------- | ---------- | ------ | --- |
| Say, J.-B. | (1803). | Trait´e | d’´economie | politique. | Paris. |     |
Scheibenreif, D., and M. Raskino (2023). When Machines Become Customers. Gartner, Inc.
Solow, R. M. (1956). “A Contribution to the Theory of Economic Growth.” Quarterly Journal
| of Economics |     | 70(1): 65–94. |     |     |     |     |
| ------------ | --- | ------------- | --- | --- | --- | --- |
Sraffa, P. (1960). Production of Commodities by Means of Commodities. Cambridge University
Press.
19

Stiglitz, J. E., A. Sen, and J.-P. Fitoussi (2009). Report by the Commission on the Measurement
| of Economic | Performance | and Social | Progress. |
| ----------- | ----------- | ---------- | --------- |
Susskind, D. (2020). A World Without Work: Technology, Automation, and How We Should
| Respond. | Allen Lane. |     |     |
| -------- | ----------- | --- | --- |
Trammell, P., and A. Korinek (2023). “Economic Growth under Transformative AI.” NBER
| Working | Paper 31815. |     |     |
| ------- | ------------ | --- | --- |
von Neumann, J. (1945). “A Model of General Economic Equilibrium.” Review of Economic
| Studies 13(1): | 1–9. |     |     |
| -------------- | ---- | --- | --- |
Weitzman, M. L. (1998). “Recombinant Growth.” Quarterly Journal of Economics 113(2):
331–360.
Wright, T. P. (1936). “Factors Affecting the Cost of Airplanes.” Journal of the Aeronautical
| Sciences | 3(4): 122–128. |     |     |
| -------- | -------------- | --- | --- |
Zeira, J. (1998). “Workers, Machines, and Economic Growth.” Quarterly Journal of Economics
113(4): 1091–1117.
20
---- END DOCUMENT ----
