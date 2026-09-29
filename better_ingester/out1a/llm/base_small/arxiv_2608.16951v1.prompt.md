Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
| The Little | Scientist:  | LLM         | Agent-Driven | Discovery        | via the |
| ---------- | ----------- | ----------- | ------------ | ---------------- | ------- |
|            |             | Scientific  | Method       |                  |         |
|            |             | Travis      | Smith        |                  |         |
|            | Independent | Researcher, | S˜ao Miguel, | Azores, Portugal |         |
travis.smith@fiveminutesforward.com
|     |     | ORCID: | 0009-0009-6732-445X |     |     |
| --- | --- | ------ | ------------------- | --- | --- |
6202 guA 61  ]MQ.oib-q[  1v15961.8062:viXra
|     |     | August | 2026 |     |     |
| --- | --- | ------ | ---- | --- | --- |
Abstract
| What happens | when you teach | an LLM-based | agent | the scientific method? |     |
| ------------ | -------------- | ------------ | ----- | ---------------------- | --- |
Motivation: Scientific discovery emerges from cycles of hypothesis, implementation, em-
pirical testing, and feedback. Can this process be automated? We approach automated
algorithm design through the lens of the scientific method, where an LLM-based agent goes
| through each | step of the process | in an ordered, | iterative | fashion. |     |
| ------------ | ------------------- | -------------- | --------- | -------- | --- |
Results: WepresentThe Little Scientist,aframeworkinwhicha’Scientistagent’worksin-
sideanevaluationenvironmentthatbenchmarksitscodeandreturnsstructuredper-instance
diagnostics. When the Scientist plateaus at a local optimum, a ’Kuhn agent’ injects a
paradigm-shiftingconjecturepairedwithacross-disciplinaryinspiration, forcingexploration
of a different region of the LLM’s latent space. We demonstrate the framework on two
problems that require fundamentally different modes of discovery. For protein fitness pre-
diction, the Scientist discovered Delta V, an ensemble calibration strategy that ranks first
on the ProteinGym DMS Substitutions Zero-Shot leaderboard across all five of-
ficial evaluation metrics, exceeding the #2 model (VenusREM) by +0.033 mean Spearman
correlation across 217 DMS assays. For DNA motif discovery, the Scientist wrote an al-
gorithm from scratch — DALE (Dual-seed Algorithm for Latent Enumeration) — that
outperforms STREME (the default in the MEME Suite) across 132 ENCODE transcription
factors (mean AUROC 0.842 vs. 0.803, Wilcoxon p<10−6) while running 11× faster. This
demonstrates that the framework can produce genuinely novel algorithms, not just optimize
existing components. Together, these results show that an LLM agent stepping through
the scientific method can discover both new algorithms and new ensemble strategies that
outperform prior solutions. The entire research program consumed 704M tokens on a single
| virtual machine | with no GPUs. |     |     |     |     |
| --------------- | ------------- | --- | --- | --- | --- |
Availability: Framework and algorithm source code available at https://github.com/
travis42/little-scientist-daleandhttps://github.com/travis42/little-scientist-delta-v.
| Both repositories | are released | under the | Apache 2.0 | license. |     |
| ----------------- | ------------ | --------- | ---------- | -------- | --- |
1 Introduction
Agent-driven algorithm discovery has produced impressive results. AlphaEvolve [Novikov et al.,
2025] and FunSearch [Romera-Paredes et al., 2024] discovered algorithms competitive with
human-designed ones using LLM-based evolutionary search. The Evolution of Heuristics frame-
work [Liu et al., 2024] applied similar ideas to automatic heuristic design. Li et al. [2026]
propose teams of LLM agents as computational research teams. These systems share a common
approach: evolutionary or genetic operators on code, guided by a scalar fitness signal.
Recent theoretical analysis argues that this generate-and-rank paradigm misses the prob-
lem of sparse feedback, and that auto-research should instead use dense intermediate signals—
analogous to coverage-guided fuzzing—to direct search rather than merely ranking completed
samples [He, 2026].
1

Human scientists do not work this way. They form hypotheses before experimenting, predict
outcomes, reconcilepredictionswithresults, andwhenprogressstalls, stepbackandreframethe
problem entirely — a process Thomas Kuhn [Kuhn, 1962] described as the alternation between
normal and revolutionary science. We ask: can an LLM-based agent that follows the scientific
method — rather than evolutionary search — discover competitive algorithms?
We present The Little Scientist, a framework built around a single organizing idea: an
LLM-based agent that behaves like a scientist. The Scientist agent works inside an evaluation
environment that benchmarks its code against real data and feeds results back with structured
diagnostics. The LLM agent walks through the scientific method — hypothesis, prediction,
code, test, reconciliation — for each iteration. When the Scientist plateaus at a local optimum,
a second agent (the Kuhn agent, named after Thomas Kuhn’s [Kuhn, 1962] distinction between
normal and revolutionary science) injects a paradigm-shifting conjecture: a domain-specific
reframing paired with an inspiration drawn from a different scientific discipline. This forces the
Scientist to explore a different region of the LLM’s latent space, potentially breaking out of the
local optimum.
We demonstrate the framework on two problems that require fundamentally different modes
of discovery:
• Protein fitness prediction (ensemble optimization). Given a protein sequence and
mutations, predict fitness effects zero-shot. The Scientist discovered Delta V, an ensemble
calibration strategy that ranks first on the ProteinGym DMS Substitutions Zero-Shot
leaderboard [Notin et al., 2023] across all five official evaluation metrics, exceeding the #2
model (VenusREM) by +0.033 mean Spearman correlation across 217 DMS assays. This
is our strongest scientific result: beating a mature, 90+ model public leaderboard where
the top entries are billion-parameter systems from major labs.
• DNA motif discovery (de novo algorithm design). Given ChIP-seq peak sequences,
discover position weight matrices (PWMs) representing transcription factor binding speci-
ficity. The Scientist wrote an algorithm from scratch — DALE (Dual-seed Algorithm
for Latent Enumeration) — that significantly outperforms STREME (the default in the
MEME Suite) across 132 ENCODE transcription factors, while running 11× faster. This
demonstratesadifferentcapability: theframeworkcanproducegenuinelynovelalgorithms,
not just optimize combinations of existing tools.
In both case studies, the algorithms and strategies are the unmodified output of the au-
tonomous search process.
A notable property of this approach is that the outputs are interpretable. Unlike neural
network-based discovery, where the result is a matrix of learned weights, the Scientist produces
classicalalgorithms. Thesystemalsocaptureseachiterationofthealgorithmsothattheprocess
itself can be audited.
This paper makes three contributions: (1) the framework architecture and its Kuhn-inspired
two-agent design, (2) two case studies demonstrating novel results, and (3) evidence that
hypothesis-driven search — where the LLM agent forms explicit predictions and receives struc-
tured per-instance feedback — operates with substantially fewer samples than evolutionary
approaches like FunSearch (based on what public sources indicate).
2 Related Work
2.1 LLM-Guided Algorithm Discovery
The idea of using language models to discover or optimize algorithms has attracted significant
attention. We categorize prior systems by their search strategy and feedback mechanism.
2

Evolutionary approaches. FunSearch [Romera-Paredes et al., 2024] pioneered LLM-guided
evolutionary search for mathematical discovery, using an LLM to mutate short code fragments
guided by a scalar fitness signal. AlphaEvolve [Novikov et al., 2025] substantially extends
this paradigm: it evolves entire codebases across multiple programming languages, supports
multi-objective optimization, and uses a distributed asynchronous pipeline with an evolutionary
databaseinspiredbyMAP-Elitesandisland-basedpopulationmodels. AlphaEvolvehasmatched
or surpassed the best known solutions on ∼75% of 50+ mathematical problems and achieved
newstate-of-the-arton∼20%,includingthefirstimprovementoverStrassen’salgorithmfor4×4
complex matrix multiplication in 56 years. The Evolution of Heuristics framework [Liu et al.,
2024] applies similar evolutionary principles to automatic heuristic design. ShinkaEvolve [Lange
etal.,2025]addressesthesample-efficiencylimitationsofthesesystemsthroughparentsampling,
code novelty rejection-sampling, and bandit-based LLM ensemble selection, discovering state-
of-the-art solutions on several tasks using as few as 150 samples.
These systems differ from The Little Scientist in two fundamental ways. First, they use
evolutionary search — mutation and crossover operators applied to code populations — guided
by scalar fitness signals. FunSearch’s programs database maintains diversity through an islands
model: independent subpopulations evolved separately, with periodic culling of underperform-
ing islands and reseeding from survivors. This mechanism exists to escape local optima in the
absenceofdirectionalfeedback—whentheonlysignalisascalarfitnessscore, thesearchhasno
guidance on where to explore next, so it maintains parallel gene pools as a brute-force diversity
strategy. Our framework uses hypothesis-driven search, where the agent forms explicit predic-
tions about why a change should help, and receives structured per-instance diagnostics that
enable targeted reasoning about failures. When the Scientist sees that an iteration improved 40
benchmark instances but regressed on 12 — and that the regressions share a specific structural
feature — it can form a hypothesis targeting that feature. This directional feedback obviates
the need for an islands model: diversity comes from informed exploration of different hypothesis
space regions, not from maintaining parallel populations. For escaping paradigm-level local op-
tima, our framework uses the Kuhn agent, which interrogates accumulated failures and proposes
strategic reframings — a targeted mechanism compared to the islands model’s implicit parallel
exploration.
Thetrade-offisthatevolutionaryapproachesaretriviallyparallelizable—eachislandevolves
independently—whilehypothesis-drivensearchisinherentlysequential, aseachiterationbuilds
on the diagnostic feedback of the previous one. For problems where evaluation is expensive
(e.g., AlphaEvolve’s 100-compute-hour evaluations), the parallelism advantage may outweigh
the sample efficiency disadvantage. For problems with cheap evaluation, such as the benchmark
scoringusedinthisstudy,thesequentialhypothesis-drivenapproachismoreefficient: oursearch
achieved a top-ranked result with 2,100 LLM invocations, compared to FunSearch’s 2,000,000
programs for a single admissible set instance (I(15,10)) costing $800–$1,400 in cloud compute.
No prior system in this category has demonstrated an LLM-agent-discovered algorithm that
exceedstheperformanceofmature, domain-specifictoolsonacompetitivebenchmark. AlphaE-
volve’s results are on open mathematical problems (where it improves known constructions in
∼20% of cases) and Google infrastructure optimization. FunSearch addresses cap-set and bin-
packing problems. Neither competes with decades of domain-specific algorithmic innovation in
a mature field. AlphaEvolve demonstrated LLM-agent-driven discovery on open mathematical
problems and internal infrastructure; we demonstrate it on a publicly benchmarked scientific
domain where three decades of tool development have established a mature state of the art.
Agent-based approaches. AI Co-Scientist [Li et al., 2026] proposes multi-agent systems for
scientific discovery but operates in natural-language hypothesis space rather than code, and
has not produced benchmarked algorithmic results. The distinction between natural-language
reasoning and code-execution grounding is significant: by grounding search in executable code
3

withautomatedevaluation,ourframeworksubstantiallysidestepsthehallucinationproblemthat
limits natural-language-only approaches. Karpathy’s autoresearch [Karpathy, 2025] is a closely
related system in which an LLM coding agent autonomously edits PyTorch training code, runs
short experiments, and retains improvements that reduce validation loss — an autonomous
research loop over a single benchmark. The core insight — that LLM agents can iteratively
improvecodeagainstanautomatedevaluationsignal—directlyinspiredthedesignofTheLittle
Scientist. However, our framework reframes the iterative loop as the full scientific method: the
agent does not merely mutate code and check whether the score improved, but forms an explicit
hypothesis, writes a numeric prediction, implements the change, evaluates it, and reconciles
the result against the prediction — learning from failures rather than discarding them. This
structured scientific method enforcement, combined with per-instance diagnostics and the Kuhn
paradigm-shiftmechanism,distinguishesourapproachfromautoresearch’ssimplerhill-climbing.
2.2 Motif Discovery Algorithms
DNA motif discovery has been studied for over three decades. MEME [Bailey and Elkan, 1994]
introducedexpectation-maximizationfordenovomotiffindingandremainsareferenceforaccu-
racy,thoughitscomputationalcostlimitsuseonlarge-scaleChIP-seqdatasets. DREME[Bailey,
2011]addressedthisbyusingsuffix-array–baseddiscriminativewordenumeration,makingitfast
but limited to short motifs (width ≤ 8). STREME [Bailey, 2021] extended DREME with sup-
port for longer motifs and a more robust statistical model, becoming the current default in the
MEME Suite and the primary benchmark for new methods. HOMER [Heinz et al., 2010] uses a
cumulative hypergeometric enrichment approach and remains widely used in genomic pipelines.
ProSampler [Li et al., 2019] combines k-mer enrichment with Gibbs sampling. GibbsSampler
[Lawrence et al., 1993] and CONSENSUS [Hertz and Stormo, 1999] established the foundational
statistical frameworks for motif discovery.
These tools share a common architecture: enumerate candidate motifs (by enumeration,
Gibbs sampling, or EM), score them against a background model, and return ranked results.
The design space includes motif width range, background model choice (Markov order), strand
handling, and scoring function. DALE operates within this design space but introduces dual-
seed selection (combining abundance-based and consistency-based criteria), Pareto-front multi-
objectiveranking, andeffective-width–awarescoring—strategiesnotfoundinanyexistingtool.
The search did not have access to the motif discovery literature beyond the benchmark data
and the input/output interface; the convergence on known best practices (k-mer enumeration,
EM refinement, information-content scoring) and the discovery of novel strategies both emerged
from the iterative optimization process.
2.3 Protein Fitness Prediction
Zero-shot prediction of mutation effects on protein fitness has advanced rapidly with the avail-
ability of large-scale deep mutational scanning (DMS) datasets. ProteinGym [Notin et al.,
2023] provides a standardized benchmark of 217 DMS assays covering diverse protein families,
measured by Spearman rank correlation between predicted and experimental fitness scores.
The field has three main approaches. Evolutionary models (EVmutation [Hopf et al., 2017],
EVE [Frazer et al., 2021]) use multiple sequence alignments to estimate per-position fitness
landscapes from evolutionary constraints. Protein language models (ESM-2 [Lin et al., 2023],
Tranception [Notin et al., 2023]) learn representations from sequence data and predict mutation
effects via autoregressive or masked prediction. Structure-aware models (ProSST, SaProt [Su
et al., 2023]) incorporate predicted or experimental protein structures to inform fitness predic-
tions. Ensemble approaches (MODIFY [Zhang et al., 2024], VenusREM [Marquet et al., 2024],
VenusRAR [Tan et al., 2026]) combine predictions from multiple models.
Ensemblingisawell-knowntechniqueforimprovingpredictionaccuracy,anditseffectiveness
4

on ProteinGym has been demonstrated. MODIFY showed that combining ESM-1v, ESM-2,
EVmutation, EVE, and MSA Transformer outperforms individual models on 87 DMS assays
[Zhang et al., 2024]. VenusREM demonstrated that structure-aware ensembling achieves top
ProteinGym rankings. VenusRAR [Tan et al., 2026] introduces a two-stage agentic framework
combining LLM-driven dynamic ensemble weighting with inference-time biological reasoning.
Their Rank-Stage achieves 0.551 Spearman on ProteinGym zero-shot through per-protein LLM
weightcalibration;ourDeltaVachievesthesameheadlineperformancethroughanLLM-evolved
staticstrategyrequiringnoinference-timeLLMcalls. VenusRAR’sReason-Stageprovides selec-
tionauditingforlow-budgetexperimentalscenarios—acomplementarycapabilitythatcouldbe
applied atop any ranking method, including ours. The approaches differ fundamentally in where
theLLMcontributes: VenusRARusesLLMreasoningatscoringtime, whileourframeworkuses
LLM-driven evolutionary search at strategy discovery time.
The contribution of Delta V is not ensembling per se — it is the calibration strategy: how
the ensemble weights are adapted per-mutation based on confidence scores, how residuals are
propagated across spatially neighboring positions, and how the output distribution is expanded
via power transformation. These calibration mechanisms were autonomously discovered, not
borrowed from existing ensemble methods.
3 The Little Scientist Framework
Figure 1: Overview of The Little Scientist framework. The Scientist agent works inside an
evaluation environment that benchmarks its code and returns structured diagnostics. When the
Scientist plateaus, the Kuhn agent injects a paradigm-shifting conjecture paired with a cross-
disciplinary inspiration, forcing exploration of a different region of the LLM’s latent space.
3.1 Overview
The Little Scientist framework has three components that interact through a single data-flow
loop (Figure 1): the Scientist agent writes candidate algorithms, the evaluation environment
benchmarks them and returns structured diagnostics, and the Kuhn agent operates similarly
to the Scientist, but with an environmental injection of paradigm-shifting reframings when the
Scientist plateaus. The remainder of this section details each component:
• §2.2 describes the Scientist agent — its inputs, outputs, and hypothesis-driven reasoning.
5

• §2.3
describes the evaluation environment — the two-level diagnostic feedback structure
| and | the | causal | design | principle. |     |     |     |
| --- | --- | ------ | ------ | ---------- | --- | --- | --- |
• §2.4
describes the Kuhn agent — paradigm-shifting conjectures and cross-disciplinary in-
spirations.
• §2.5 describes process engineering — forced scientific method adherence, versioned state,
| and    | the     | inner/outer |            | loop | distinction. |        |     |
| ------ | ------- | ----------- | ---------- | ---- | ------------ | ------ | --- |
| • §2.6 | reports | search      | statistics |      | and compute  | usage. |     |
• §2.7
|        | describes |     | infrastructure  |     | evolution | across phases. |     |
| ------ | --------- | --- | --------------- | --- | --------- | -------------- | --- |
| • §2.8 | describes |     | reproducibility |     | measures. |                |     |
The inner search loop is autonomous: each scheduled invocation reads context files (previous
diagnostics,hypothesishistory,currentbestcode),formsahypothesiswithanumericprediction,
modifies the code, compares the changes to the hypothesis for the sake of alignment, runs the
smoke test, and exits if it passes. After that, the validation/eval step runs. The next invocation
| continues | from | where | the | last left | off. |     |     |
| --------- | ---- | ----- | --- | --------- | ---- | --- | --- |
Theouterloopiscomposedofabenchmarkconfiguration, diagnosticpipeline, promptstruc-
ture, and paradigm-shift triggers, among other things. This loop is optionally human-guided,
analogous to a principal investigator adjusting experimental parameters while an automated
| system | runs | measurements |     | unattended. |     |     |     |
| ------ | ---- | ------------ | --- | ----------- | --- | --- | --- |
The two-tier evaluation strategy is essential to this loop. A small smoke test (4–5 instances)
provides rapid feedback, enabling tight iteration from which the agent can either retry upon
failure or exit successfully. This process allows the agent to test many ideas cheaply.
| 3.2 | The Scientist |     | Agent |     |     |     |     |
| --- | ------------- | --- | ----- | --- | --- | --- | --- |
The Scientist is an LLM-based agent that writes code in Python (for motif discovery) or Python
strategy functions (for ProteinGym). It receives as input the described items in the Inner Loop.
TheLLMagent’soutputisamodifiedsourcefileaccompaniedbyanaturallanguagehypoth-
esis explaining the expected effect of each change. Code execution is sandboxed: the candidate
cannot perform file I/O, network access, or system calls. The allowed imports are limited to
numerical libraries (NumPy, SciPy) and the Python Standard Library, with some exceptions
designed to further limit system access. This constraint forces the search to explore algorithmic
| structure | rather | than | exploit | external | resources. |     |     |
| --------- | ------ | ---- | ------- | -------- | ---------- | --- | --- |
The LLM agent’s reasoning is hypothesis-driven: rather than making random perturbations,
it forms specific predictions about why a change should help, which can be confirmed or refuted
by the next evaluation. This is a deliberate contrast with the evolutionary search methods used
by AlphaEvolve [Novikov et al., 2025] and FunSearch [Romera-Paredes et al., 2024], which rely
on mutation and crossover operators on code without explicit reasoning about why a change
should improve performance. The hypothesis-driven approach trades search breadth for search
depth: fewer iterations are needed because failed hypotheses constrain the design space for
| subsequent | proposals. |     |     |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- | --- | --- |
Enforced prediction of the outcome of an experiment is used in the reconciliation phase to
guide the agent toward recognizing the difference between the outcome of an exeriment with the
hypothesis and prediction of success that formed it. Practically speaking this is done through
havingtheagentfillinaworksheettoreconcileenvironmentalfeedbackwithitsownstatements,
which then lead to a next hypothesis. In practice, prompting is insufficient–forcing the agent to
| walk through |     | the steps | leads | to  | more coherent | ideation and | results. |
| ------------ | --- | --------- | ----- | --- | ------------- | ------------ | -------- |
6

3.3 The Evaluation Environment and Structured Feedback
The evaluation environment benchmarks each candidate against a dataset and computes the
primary metric.
A critical design principle is that the environment provides structured per-instance diagnos-
tics, not merely a scalar score. Two levels of feedback are generated:
Level 1: Per-instance data. For each item in the benchmark (e.g., each TF for motif
discovery, each protein for ProteinGym), the evaluator records the per-instance metric, elapsed
time,andrelevantparameters(selectedmotifwidths,mutationcounts,MSAdepth). Thisallows
the Scientist to identify exactly which instances improved or regressed.
Level 2: Curated diagnostic summary. The evaluator generates a markdown report in-
cluding aggregate statistics, distributions of key parameters, comparison to baseline tools, and
a ranked list of weakest instances with contextual detail. For ProteinGym, this also includes
substitution class analysis, conservation-error correlation, and structural context breakdowns.
This surfaces patterns the Scientist can reason about.
This two-level feedback structure is essential. With scalar feedback alone, the search de-
generates into blind optimization: the agent makes random perturbations and cannot learn
from failures. Structured feedback enables targeted hypotheses such as “width=17 on CTCF
gives 0.707 but STREME uses width=14 — my width selection may be too wide for CTCF-like
factors.”
The causal structure principle. Not all feedback is equally informative. The critical design
property is that diagnostics must connect algorithm design choices to per-instance outcomes —
not merely describe what happened, but indicate why. For motif discovery, “CTCF scored
0.65 AUROC because the discovered motif is 8bp while the JASPAR reference is 19bp” points
directlyatadesignlever(widthselection). Thediagnosticsurfacesacausallinkbetweenadesign
decision and an error pattern, enabling the Scientist to form a targeted hypothesis. Outcome-
only feedback (e.g., “fold 3 returned −2.1
”) describes results without revealing causes, leaving the agent to guess at fixes. In Phase 1 of
our motif search, diagnostic output was silently deleted before the agent could read it (see §2.7),
leaving the agent blind to which specific cases failed. This produced random search behavior
indistinguishable from blind optimization.
3.4 The Kuhn Agent
The Kuhn agent addresses a fundamental challenge: LLM-based search, like any local optimiza-
tion, gets stuck. The Scientist can refine within its current paradigm indefinitely, making small
improvements that eventually plateau, for reasons that tentatively have to do with the act of
readingitsownpastactions. SinceLLMsproceedfromtheirowncontext, ifthecontextisfullof
certainapproach,itislikelierthatthefutureoutputwillfollowsuit(muchlikehumanscientists).
Breaking out requires something qualitatively different — a reframing of the problem.
Kuhn is triggered after a configurable number of consecutive non-improving iterations (typ-
ically 7–10) by the Scientist. It receives most of the same context as the Scientist, with the
exception of some past scratchpad files the Scientist uses, and crucially, it does not receive
the history file of past experiments. The key difference is that its prompt receives an injected
paradigm-shifting conjecture paired with a cross-disciplinary inspiration from the Environment,
which have been randomly created beforehand.
Example:
Assumption: “Model predictions for single mutants generalize to multi-mutant variants
without interaction terms”
7

Domain inspiration: Architecture — load-bearing analysis, redundancy, and graceful failure
in structural systems
In this way the Kuhn agent, though it is running on the same underlying LLM, has a
different part of its latent/representation space activated. When this results in a higher score
on the benchmark or multi-metric standard, it generally represents a novel approach that the
Scientist can then improve upon.
Empirical contribution. The Kuhn agent’s role was measured across both case studies.
In the motif discovery search, the Kuhn agent proposed the paradigm shift from probability-
based modeling to frequency-based k-mer enumeration — the foundational approach that all
subsequent improvements built upon. Of the 10 accepted improvements in Phase 2, 1 was
directly Kuhn-originated (the paradigm shift itself), while the remaining 9 were Scientist refine-
ments within the Kuhn paradigm. Without the Kuhn shift, Phase 2 would not have existed;
the paradigm it established was the necessary precondition for all subsequent progress. In the
ProteinGymsearch, theKuhnagentproposedtheCPCWE(Constraint-PropagatedConfidence-
WeightedEnsemble)paradigmthatbecamethefoundationofDeltaV—1of2acceptedimprove-
ments was Kuhn-originated. In both cases, the Kuhn agent’s contribution was not incremental
improvement but qualitative reframing.
3.5 Process Engineering
The framework’s search loop is conceptually simple, but several engineering choices were useful
to make it function in practice. Figure 1 provides a visual overview of the complete system.
Forced adherence to the scientific method. LLM agents tend to skip steps when given a
complex multi-stage protocol. A naive prompt saying “follow the scientific method” produces
cursory execution: the agent writes a hypothesis after the fact, skips the prediction, or rational-
izes unexpected results instead of analyzing them. We address this by structuring the agent’s
prompt as a numbered sequence of mandatory steps with concrete file outputs at each stage.
The agent must write an explicit prediction (numeric AUROC range) to a file before writing
code, and must reconcile its prediction against the actual result in the next iteration. This
“walking the dog” approach — forcing the agent through each step with a short leash — was
necessary to obtain genuine hypothesis-driven iteration rather than post-hoc rationalization.
The reconciliation step is where learning accumulates. When a prediction is confirmed, the
Scientist has validated a causal model. When a prediction is refuted, the discrepancy itself
is informative: “I expected adaptive width to help CTCF (+0.01–0.02); it regressed (−0.03)
because the scoring function penalizes long motifs under shuffled controls.” A wrong prediction
that gets reconciled constrains the design space more than a correct one — it tells the Scientist
not just that its change failed, but which part of its reasoning was wrong. Over hundreds of
iterations, these reconciliations build an increasingly accurate causal model of the benchmark.
Versioned state for hill-climbing. Every accepted improvement is committed to a version-
controlled repository, creating an immutable lineage from the initial seed algorithm to the final
result. This serves two purposes: (1) it provides a deterministic rollback mechanism if a candi-
datepassesthesmoketestbutfailsfullevaluation(falsepositive),and(2)itrecordsthecomplete
algorithmic lineage, making the discovery process fully auditable. Each commit records the hy-
pothesis, the score delta, and the code diff.
3.6 Search Statistics and Compute Usage
The search did not proceed from a fixed design. The framework was built iteratively — each
infrastructure improvement solved a specific failure mode that had stalled progress. Table 1
8

summarizes the compute usage across the full search, measured from system logs (OpenClaw
cron run logs). We describe the timeline in terms of these phases because the infrastructure
changes between them were as consequential as the algorithmic changes.
Phase 1: Initial search (May 30 – June 13, 2026). The initial search ran for 13 days
and produced 236 evaluated algorithm iterations across 1,588 LLM agent invocations. In this
phase, the Scientist operated on a synthetic benchmark (12 profiles, nCC scoring) with a loosely
structured prompt. The agent tended to make aggressive full rewrites of the algorithm rather
than targeted modifications, frequently breaking functionality. After 49 consecutive runs with
zero accepted improvements, the loop was paused. This phase consumed approximately 97.6M
tokens at an average of 61K tokens per agent invocation.
The failure was not in the algorithm — it was in the infrastructure. Three problems were
identified: (1) the synthetic benchmark did not correlate with real motif discovery performance,
so the agent was optimizing the wrong objective; (2) the agent’s prompt did not enforce the
scientific method, allowing post-hoc rationalization instead of genuine hypothesis testing; (3)
the evaluator’s per-instance diagnostic output was being deleted before the agent could read it,
leaving the agent blind to which specific cases failed.
Infrastructure overhaul (June 22 – July 19, 2026). Between phases, we made five tar-
geted changes, each addressing a specific failure mode:
1. Real benchmark data. Replaced the synthetic 12-profile eval with 15 real ChIP-seq
TFs and AUROC scoring. The agent was now optimizing the actual objective.
2. Causal scaffold prompt. Rewrotetheagent’sprompttoenforceaseven-fieldstructured
plan: hypothesis, prediction (numeric AUROC range), code change, expected mechanism,
falsification criterion, prior-work citation, and post-hoc reconciliation. This “walking the
dog”approachforcedtheagentthrougheachstepofthescientificmethodwithmandatory
file outputs, preventing it from skipping steps or writing hypotheses after the fact.
3. Trust-boundary validator. Movedtheevaluate/commit/revertlogicoutsidetheagent’s
executionscope. Theagentcannotmodifytheevaluator,inspectbenchmarklabels,oralter
test data.
4. Fixed diagnostic pipeline. Restored the per-TF diagnostic output that had been
silently deleted. The agent could now see which TFs improved or regressed, what widths
were selected, and how its results compared to baseline tools.
5. Kuhn paradigm agent (July 12 – 15). A separate agent that periodically inter-
rogated accumulated failures and proposed strategic reframings rather than incremental
code changes. Over 3 days and 63 invocations (∼33.5M tokens at 531K tokens/run), it
analyzed the V1 failure pattern and proposed shifting from probability-based modeling to
frequency-based k-mer enumeration.
Theimpactwasimmediate. Underthenewinfrastructure, thefirst11experimentsproduced
twobreakthroughs: frequency-basedseedingbeatenrichment-ratioseeding(0.312→0.565), and
adaptive motif width search resolved a systematic over-width problem (0.565 → 0.709). The
agent was now citing prior experiments, writing structured causal plans, and making targeted
edits rather than full rewrites.
Phase 2: full-framework search (July 19 – July 29, 2026). With the infrastructure
overhauled, the search ran for 10 days and produced 64 evaluated iterations across 500 agent
invocations (∼97.9M tokens at 196K tokens/run). Score progression was rapid: entries scored
9

0.794 (July 19), crossed 0.817 (July 28), and reached 0.846 (July 29). The best score achieved
was 0.846 (run #50, July 29). The algorithm that became DALE was selected from this phase.
Total compute. Across all phases, the search consumed:
Table1: Measuredcomputeusageforthemotifdiscoverycasestudy. AllfiguresfromOpenClaw
cron run logs.
Phase Runs Tokens Avg tokens/run Days
Initial search (V1) 1,588 97.6M 61K 13
Kuhn paradigm agent 63 33.5M 531K 3
full-framework search (V2) 500 97.9M 196K 10
Total 2,151 229.0M 106K 26 active
Of the ∼64 evaluated iterations in Phase 2, 17 produced improvements over the current best
— a 26.6% success rate. The non-improving iterations were not wasted: they tested and refuted
hypotheses, progressively constraining the design space. This pattern mirrors human algorithm
development, where most ideas do not work, and progress is built on many failures.
Framework development overhead. The 229M tokens reported above include both the
cost of developing the framework and the cost of the search itself. Phase 1 (97.6M tokens)
and the Kuhn agent (33.5M tokens) were spent discovering what infrastructure was missing
— the recurring cost of a stalled loop, a wrong benchmark, and silently deleted diagnostics.
A researcher starting today with the documented end-state framework would not incur this
overhead. We estimate the recurring cost of applying The Little Scientist to a new domain
at approximately 100M tokens and ∼2 weeks of active search, based on the Phase 2 run that
reached the top reported score from a cold start in 10 days using 97.9M tokens. The first DALE
improvement was achieved at run 25 (˜4.9M tokens), with the best score (0.843) achieved at run
52 (˜10.2M tokens). The remaining 448 runs continued search past the plateau to verify that no
further improvement was achievable — standard practice when the optimum is unknown. We
report both total search cost and cost-to-first-best, as continued search after plateau inflates the
total but is unavoidable without a priori knowledge of the optimum.
Timeline to top reported score. The total calendar span from first run to top reported
score was approximately 2 months (May 30 – July 29, 2026), of which 26 days were active search
(the remainder was gaps between phases for infrastructure development and analysis). The final
phase — from infrastructure overhaul to top reported score took 10 days.
Infrastructure. The entire search ran on a single virtual machine (2 AMD EPYC-Rome
cores, 3.7GB RAM, Ubuntu Linux). Agent invocations were scheduled via cron jobs and ran
autonomously without human intervention. No distributed computing infrastructure was used.
The contrast with prior agent-driven discovery systems is striking in three dimensions:
• Infrastructure footprint. AlphaEvolve uses a distributed asynchronous pipeline (con-
troller, LLM samplers, evaluation nodes) optimized for throughput. FunSearch similarly
requires distributed infrastructure. Our system runs on a single VM with cron jobs.
• Evaluation cost. AlphaEvolve reports evaluations costing “on the order of 100 compute-
hours”percandidate,parallelizedacrossacluster. Ourevaluationstakesecondsonasingle
core. This ∼105× evaluation cost difference reflects the domain difference (mathematical
proof verification vs. statistical benchmark scoring), but it means our search loop can run
far more iterations per unit of compute.
10

• LLM invocation scale. AlphaEvolve reports “thousands” of LLM samples; FunSearch
reports “millions.” Neither reports total token counts. Our search used ∼2,100 LLM
agent invocations and 229M tokens, fully accounted. While we cannot make a direct token
comparison(neithersystemdisclosestokens),the∼103×gapwithFunSearchsuggeststhat
hypothesis-driven search with structured feedback is substantially more sample-efficient
than scalar-fitness evolutionary search.
Neither AlphaEvolve nor FunSearch discloses total token consumption, wall-clock time for
individual results, or overall compute budget, making precise comparison impossible. We report
all compute figures in full (Table 1).
Cost. The LLM used for all experiments was GLM-4.7 (Z.ai). The motif discovery search ran
for approximately 2 months of active development; the ProteinGym search ran for 9 days. At
OpenRouter pay-per-token rates for GLM-4.7 ($0.40/1M input, $1.75/1M output), the 704M
tokens consumed across both case studies would cost approximately $472. With server costs of
$21 (single VM, no GPUs), the total was approximately $493.
3.7 Infrastructure Evolution
ForDALE,thegapbetweenPhase1(stalledat0.664)andPhase2(reached0.846in10days)was
not algorithmic. The difference was entirely in the infrastructure supporting the search. Five
changes, each addressing a specific failure mode, transformed a stalled loop into a productive
one:
1. Real benchmark data — the agent cannot optimize what it cannot measure properly.
The synthetic eval was correlated with real performance but not enough to guide search.
By upgrading to the same data that STREME was benchmarked against, agents we able
to make better progress than with synthetic representations.
2. Structured scientific method enforcement — teaching the agent to be a scientist
(seven-field causal plan, explicit predictions, falsification criteria) rather than simple in-
structions to meet the objective.
3. Per-instance diagnostic feedback — As noted previously, when feedback about the
performanceofthecodeagainstthebenchmarkincludeddetailedinformationaboutwhich
parts scored higher or lower on the target subject benchmark rather than just a simple
score, the agents were able to augment their follow on approaches in a much more efficient
way. Thismayinfactbethegreatestsingleleverforprogress,asagentsdoalreadyhavethe
ability to reason without the scientific framework enforced. Scientific method enforcement
merely guides a pre-existing ability to do logical tasks and meet goals they receive through
prompting.
4. Kuhn paradigm interrogation — useful for escaping local optima.
5. Behavioral prompt engineering—guidingtheagenttowardtargetededitsratherthan
full rewrites prevented it from repeatedly breaking its own algorithm.
We note that these features were identified through iterative debugging during the search
itself, not designed ex ante.
3.8 Reproducibility
All agent transcripts, hypotheses, and evaluation results are preserved in a structured log
(history.jsonl). Every proposed change is traceable to the hypothesis that motivated it and
11

the outcome it produced. The algorithm’s lineage can be followed from the initial seed (a basic
frequency-counting approach scoring 0.662 AUROC on synthetic data) through the infrastruc-
ture overhaul and paradigm shift, to the final algorithm. Token usage for every agent invocation
is recorded in the OpenClaw cron run logs database, enabling independent verification of all
compute figures reported here.
Figure 2: Score progression for both case studies. (A) Motif discovery: the infrastructure
overhaul gap (gray band) and Kuhn paradigm shift (annotation) separate the stalled Phase 1
from the full-framework Phase 2. Dashed lines show STREME and MEME baseline accuracy.
(B) Protein fitness prediction: the discontinuous jump on Aug 4 occurred when the human
investigator provided pre-computed model predictions as input data, enabling the Scientist to
adopt an ensemble approach. Dashed lines show the top ProteinGym leaderboard entries.
3.9 Benchmark Methodology
3.9.1 Data
We benchmarked on 132 ENCODE K562 ChIP-seq transcription factor datasets [Consortium,
2012]. Each dataset contains approximately 200 DNA sequences of 500 base pairs, centered on
ChIP-seq peak summits. For motif discovery, the central 100bp window was used; full 500bp
sequences were used for scoring and AUROC evaluation.
3.9.2 Negative Sets
Two negative sets were used:
1. Dinucleotide-shuffled negatives (132 TFs): Each positive sequence was dinucleotide-
shuffled, preserving mono- and dinucleotide composition while destroying higher-order
sequence patterns. This is the standard benchmark negative set used by STREME and
MEME.
2. Genomic negatives (53 TFs): Random regions sampled from hg38, matched for length
and chromosome distribution. This represents a more realistic benchmark, as random
genomic DNA contains natural regulatory patterns absent from shuffled sequences.
12

| 3.9.3 | Tools | Compared   |     |         |            |             |          |        |             |
| ----- | ----- | ---------- | --- | ------- | ---------- | ----------- | -------- | ------ | ----------- |
|       |       |            |     | Table   | 2: Tools   | compared    | in this  | study. |             |
|       |       | Tool       |     | Version | Parameters |             |          |        |             |
|       |       | DALE       |     | 1.0     | Default    | (widths     | 6–17)    |        |             |
|       |       | STREME     |     | 5.5.5   | --dna      | --minw      | 6 --maxw | 17     |             |
|       |       | MEME       |     | 5.5.5   | -mod       | zoops -minw | 6        | -maxw  | 17 -revcomp |
|       |       | proto-DALE |     | —       | Earlier    | prototype,  | same     | width  | range       |
Alltoolswererunwithawidthrangeof6–17basepairs. Bothstrandsweresearchedbyalltools.
STREME’s default background model was used. MEME was run in Zero-or-One Occurrence
| Per | Sequence | (ZOOPS) | mode | with | 5 motifs | returned. |     |     |     |
| --- | -------- | ------- | ---- | ---- | -------- | --------- | --- | --- | --- |
3.9.4 Evaluation
ForeachTFandtool,thehighest-scoringmotif(bythetool’sinternalranking)wasusedforeval-
uation. Discriminative power was measured by AUROC: the area under the receiver operating
characteristic curve, computed from the score distributions of positive and negative sequences.
All tools’ output PWMs were scored using identical scoring code to ensure fairness.
| 3.9.5 | Statistical |     | Tests |     |     |     |     |     |     |
| ----- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- |
•
Wilcoxon signed-rank test (paired, two-sided) for paired AUROC comparisons
|     | • Bootstrap | 95% | confidence | intervals |     | (1000 resamples, | seed | =   | 42) |
| --- | ----------- | --- | ---------- | --------- | --- | ---------------- | ---- | --- | --- |
•
|       | McNemar’s | test          | for binary          | outcome      |      | comparison |     |     |     |
| ----- | --------- | ------------- | ------------------- | ------------ | ---- | ---------- | --- | --- | --- |
|       | • Cliff’s | δ and Cohen’s |                     | d for effect | size | estimation |     |     |     |
| 3.9.6 | Hardware  |               | and Reproducibility |              |      |            |     |     |     |
All benchmarks were run on a single AMD EPYC-Rome processor (2 cores, 2.0GHz) with
3.7GB RAM under Ubuntu Linux. During the search phase, candidate algorithms were written
in Python and evaluated on a 5-TF smoke test followed by a 15-TF full evaluation. For the final
benchmark comparison against STREME and MEME, the best-performing algorithm (run #50,
July29)wasportedtoCandcompiledwithGCCat-O2 -std=c99 -static(928KBstatically-
linkedbinary). STREME5.5.5wascompiledfromsourceat-O2andverifiedtoproduceidentical
results to the prebuilt binary. All tools are deterministic under fixed parameters.
| 4   | Case    | Study: | De  | Novo | Motif | Discovery |     |     |     |
| --- | ------- | ------ | --- | ---- | ----- | --------- | --- | --- | --- |
| 4.1 | Problem | Domain |     |      |       |           |     |     |     |
DenovomotifdiscoveryistheproblemofidentifyingrecurringDNAsequencepatterns(position
weight matrices, or PWMs) from collections of genomic regions enriched for transcription factor
binding. Given a set of ChIP-seq peak sequences, the goal is to discover the binding specificity
| of  | the targeted | TF without |     | prior knowledge |     | of its motif. |     |     |     |
| --- | ------------ | ---------- | --- | --------------- | --- | ------------- | --- | --- | --- |
The problem has been studied for three decades. MEME [Bailey and Elkan, 1994] intro-
duced expectation-maximization (EM) approaches and remains a gold standard for accuracy.
STREME[Bailey,2021], thesuccessortoDREME[Bailey,2011], usessuffix-tree–basedenumer-
ation and is the current default in the MEME Suite. HOMER [Heinz et al., 2010] uses a distinct
13

cumulative hypergeometric approach. ProSampler [Li et al., 2019] combines k-mer enrichment
| with | Gibbs  | sampling.     |     |     |     |     |     |     |     |     |
| ---- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4.2  | Search | Configuration |     |     |     |     |     |     |     |     |
For the motif discovery case study, the search was configured as follows:
• Input: ENCODE K562 ChIP-seq peak sequences, 100bp centered windows
•
|     | Metric: | Mean | AUROC | across | benchmark | TFs | (shuffled | negatives) |     |     |
| --- | ------- | ---- | ----- | ------ | --------- | --- | --------- | ---------- | --- | --- |
• Baseline: STREME 5.5.5 with matched parameters (--minw 6 --maxw 17)
•
Implementation: Python during search (NumPy/SciPy); C port for benchmark com-
|     | parison | against | STREME |     |     |     |     |     |     |     |
| --- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
• Constraint: Algorithm receives sequences as function arguments, outputs PWMs. No
|     | file | I/O, no | network. |     |     |     |     |     |     |     |
| --- | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
The search space includes all algorithmic choices: how to enumerate candidate words, how
to select seed motifs, how to refine them into PWMs, how to rank final candidates, and how to
handle variable motif widths. The Scientist agent was not given domain knowledge about motif
discovery beyond the benchmark data and the structure of the input/output interface.
| 4.3 | Diagnostic |     | Feedback |     |     |     |     |     |     |     |
| --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Each evaluation produced structured diagnostic feedback through three files, serving the same
| observation |     | and | memory | functions | as the ProteinGym |     | case | study. |     |     |
| ----------- | --- | --- | ------ | --------- | ----------------- | --- | ---- | ------ | --- | --- |
staging diagnostics.mdwastheprimaryfeedbackfile,rewrittenbythewrite diagnostics()
function in the validation script after every full evaluation. It contained five categories of com-
puted feedback:
1. AUROC summary — average, bottom quartile average, best, and worst across all 15
|     | benchmark |     | TFs. |     |     |     |     |     |     |     |
| --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
2. Speed statistics — average elapsed time and speed bonus per TF.
3. Width distribution — how many TFs the algorithm selected each motif width for (e.g.,
|     | w=17: | 8,  | w=14: | 2, w=12: | 4, w=10: | 1). |     |     |     |     |
| --- | ----- | --- | ----- | -------- | -------- | --- | --- | --- | --- | --- |
4. Width vs. STREME comparison — flagged every TF where the algorithm’s chosen
width differed from STREME’s known width by more than 2bp, with the AUROC for
|     | that | TF (e.g., | “SP1: | ours=17 | vs STREME=7 |     | (auroc=0.682)”). |     |     |     |
| --- | ---- | --------- | ----- | ------- | ----------- | --- | ---------------- | --- | --- | --- |
5. Lowest-AUROC TFs — the bottom 5 TFs with AUROC, selected width, and elapsed
time.
Categories 3–5 are where the causal structure enters. “SP1: ours=17 vs STREME=7, AU-
ROC=0.682”connectsadesign choice (widthselection)toaper-instance outcome (lowAUROC
on SP1). The agent can immediately form a hypothesis: “the width selector is biased toward
| long | motifs; | SP1’s | true           | motif is short.” |        |          |      |              |            |            |
| ---- | ------- | ----- | -------------- | ---------------- | ------ | -------- | ---- | ------------ | ---------- | ---------- |
|      |         |       |                |                  | served | the same | role | for the 4-TF | smoke test | (the rapid |
|      | staging | smoke | diagnostics.md |                  |        |          |      |              |            |            |
proxy used during active search). It contained per-TF smoke AUROC, selected width, primary
score, and a brief analysis section. This enabled the tight iteration loop — seconds per smoke
| test | — before | committing |     | to a full | 15-TF evaluation. |     |     |     |     |     |
| ---- | -------- | ---------- | --- | --------- | ----------------- | --- | --- | --- | --- | --- |
14

history.jsonl was the experiment log, appended after each iteration. Each entry recorded
the full seven-step structured plan: hypothesis text, prediction range (low/high), reconciliation,
pattern analysis, proposed change, smoke test results, and blockers text — alongside the stan-
dardfields(runnumber, score, verdict, per-TFdetails). ThisgavetheScientistadetailedrecord
of what it had tried and reasoned, not just what happened.
causal model.md is an agent-maintained lab notebook recording what was tested, what the
score was, and what the signal meant. The validation script capped it at the last 10 hypothe-
ses. The agent read it at the start of each iteration alongside the fresh diagnostics, enabling
it to accumulate learned causal structure across iterations. This artifact was particularly im-
portant for the motif discovery search because the tabular diagnostics required more agent-side
interpretation.
4.4 The Discovered Algorithm
The final algorithm (run #118) incorporates the following key components, described in full
technical detail in Section 4.5:
1. Dual seed selection — combines enriched seeds (high raw abundance) with consistency
seeds (broad sequence coverage), capturing both sharp and diffuse motif signals.
2. Soft EM refinement — 20 iterations maximum, with pseudocounts preventing prema-
ture convergence.
3. Effective width awareness — tries 6 widths independently, measures how many posi-
tions contribute information content, and penalizes padding.
4. Pareto-front selection — ranks candidates on two objectives (discriminative score and
width efficiency) rather than collapsing to a single metric.
Twoofthesedesignchoices(k-merenumerationasaseedingstrategy,EMforrefinement)are
well-established in the human-designed literature. The dual-seeding strategy and Pareto-front
are not. All design choices emerged from the search process without being specified a priori.
4.5 Algorithm Details
This section describes the algorithm discovered by The Little Scientist in full technical detail.
4.5.1 Pipeline Overview
The algorithm takes as input a set of DNA sequences and returns a ranked list of candidate
motif PWMs. The pipeline consists of five stages: (1) adaptive background estimation, (2)
multi-width k-mer enumeration, (3) dual-strategy seed selection, (4) soft EM refinement, and
(5) multi-criteria ranking via Pareto front selection.
4.5.2 Adaptive Background
Nucleotide frequencies are computed from the input sequences. This matters because genomic
regions are not uniformly 25% A/C/G/T — AT-rich and GC-rich biases affect the information
content of any discovered motif. The background frequencies are used in subsequent log-odds
scoring during EM refinement.
15

| 4.5.3 | Multi-Width | K-mer Enumeration |     |     |     |
| ----- | ----------- | ----------------- | --- | --- | --- |
Thealgorithmdoesnotknowthemotifwidthinadvance. Itscanssixwidths(w ∈ {6,8,10,12,14,17})
independently. For each width, a hash table records for every unique w-mer: (1) the total count
across all sequences, and (2) the number of distinct sequences containing it. A per-sequence
deduplication ensures that seq count reflects breadth of occurrence rather than raw abundance.
| 4.5.4 | Dual Seed | Selection |     |     |     |
| ----- | --------- | --------- | --- | --- | --- |
For each width, six seeds are selected using two complementary criteria:
Enriched seeds (4 per width): Sorted by total count, filtered so no two selected seeds have
Hamming distance < w/3. These capture k-mers with the strongest enrichment signal.
√
Consistentseeds(2perwidth): Sortedbyseq count/ total count+1,filteredwithstricter
diversity (Hamming distance ≥ w/2). This metric favors k-mers appearing in many distinct se-
quences even if individually rare — a signal that captures diffuse but pervasive motif patterns.
Usingbothstrategiesensuresthatbothsharp,highly-enrichedmotifsandbroader,consistency-
| driven signals | seed    | the EM refinement. |     |     |     |
| -------------- | ------- | ------------------ | --- | --- | --- |
| 4.5.5          | Soft EM | Refinement         |     |     |     |
Each seed k-mer is converted to a starting PWM with strong bias toward the seed bases (∼76%
probability for matching bases, ∼8% for others). The PWM is then refined via expectation-
maximization:
E-step: For each sequence, log-odds scores are computed for the motif at every possible start
position (using the adaptive background). These scores are converted to position probabilities
via softmax.
M-step: The PWM is updated by accumulating weighted contributions from all positions
across all sequences. A pseudocount of 0.5 prevents any base probability from reaching zero.
The loop runs for up to 20 iterations, with early stopping when the maximum PWM change
| falls below | 10−4.       |         |               |       |     |
| ----------- | ----------- | ------- | ------------- | ----- | --- |
| 4.5.6       | Information | Content | and Effective | Width |     |
After EM convergence, per-position information content is computed as KL divergence from the
| background | distribution: |     |      |          |     |
| ---------- | ------------- | --- | ---- | -------- | --- |
|            |               |     |      | (cid:88) | p   |
|            |               |     | IC = | p log    | j,b |
|            |               |     | j    | j,b      | 2   |
q
|     |     |     | b∈{A,C,G,T} |     | b   |
| --- | --- | --- | ----------- | --- | --- |
wherep j,b isthePWMprobabilityforbasebatpositionj andq b isthebackgroundfrequency.
The effective width (eff w) is the count of positions with IC ≥ 0.1 — positions that contribute
| meaningful | information    | versus noise | padding. |     |     |
| ---------- | -------------- | ------------ | -------- | --- | --- |
| 4.5.7      | Multi-Criteria | Ranking      |          |     |     |
Within each width, the six candidates are z-score normalized on total IC. A composite discrim-
| inative score | is computed: |      |             |           |         |
| ------------- | ------------ | ---- | ----------- | --------- | ------- |
|               |              | base | = 0.7×total | ic+0.3×ic | density |
16

|       |            |     |         |         |       |       | (cid:0) z×(w/10)0.3, |     | (cid:1) |     |
| ----- | ---------- | --- | ------- | ------- | ----- | ----- | -------------------- | --- | ------- | --- |
|       |            |     |         | z bonus | =     | clamp |                      |     | −1, +1  |     |
|       |            |     |         | disc    | score | =     | base×(1+0.2×z        |     | bonus ) |     |
| where | ic density |     | = total | IC      | / eff | w.    |                      |     |         |     |
The top 2 candidates from each width (up to 12 total) are then ranked using Pareto domi-
nance: candidateAdominatesBifAisbetteronbothdisc scoreandwidthefficiency(ic density
ratio1.5)).
×(1−padding Candidates are ordered by Pareto rank, with ties broken by disc score.
| The top | 5 are | returned. |     |     |     |     |     |     |     |     |
| ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
This multi-objective approach avoids the brittleness of single-score ranking — it preserves
diverse solutions on the trade-off surface between discriminative power and width efficiency.
4.6 Results
| 4.6.1 Shuffled |     | Negatives |     | Benchmark |     |     | (132 | TFs) |     |     |
| -------------- | --- | --------- | --- | --------- | --- | --- | ---- | ---- | --- | --- |
Table 3 summarizes performance on the full 132-TF benchmark with dinucleotide-shuffled neg-
atives.
Table 3: Benchmark results on 132 ENCODE K562 ChIP-seq datasets (shuffled negatives).
|     |     | Tool       |     |       | Mean | AUROC |     | Time/TF | Speedup | vs. STREME |
| --- | --- | ---------- | --- | ----- | ---- | ----- | --- | ------- | ------- | ---------- |
|     |     | DALE       |     |       |      | 0.842 |     | 0.30s   |         | 11×        |
|     |     | proto-DALE |     |       |      | 0.843 |     | 1.56s   |         | 2.1×       |
|     |     | STREME     |     | 5.5.5 |      | 0.803 |     | 3.26s   |         | 1.0×       |
DALE significantly outperforms STREME (∆ = +0.039 AUROC, Wilcoxon p = 4.1×10−7,
88 wins / 44 losses). The improvement is consistent across TF families and is not driven by a
| few outliers | (bootstrap |     | 95% | CI  | of ∆: | [0.023, | 0.046]). |     |                    |     |
| ------------ | ---------- | --- | --- | --- | ----- | ------- | -------- | --- | ------------------ | --- |
|              |            | 1.0 |     |     |       |         |          |     | Wilcoxon p = 0.003 |     |
(n=100 TFs, genomic neg.)
0.9
)sevitageN cimoneG( CORUA
0.8
Random (0.5)
0.7
0.6
0.5
|     |     |     |     |     | mean=0.8856 |     |     |     | mean=0.8453 |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- | ----------- | --- |
0.4
|     |     |     |     |     | Our |     |     |     | STREME |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
Algorithm
Figure 3: AUROC distribution across 132 ENCODE K562 ChIP-seq datasets (shuffled nega-
tives). DALE consistently outperforms STREME. Dashed line indicates random performance.
17

Figure 4: Per-TF comparison: DALE vs. STREME (132 TFs, shuffled negatives). Points above
| the diagonal | indicate | TFs       | where DALE | outperforms | STREME. |     |     |
| ------------ | -------- | --------- | ---------- | ----------- | ------- | --- | --- |
| 4.6.2        | Genomic  | Negatives | Benchmark  |             |         |     |     |
On the more realistic benchmark using hg38 genomic regions as negatives with Markov-1 back-
| ground | scoring, | DALE | was evaluated | on two subsets: |     |     |     |
| ------ | -------- | ---- | ------------- | --------------- | --- | --- | --- |
132-TF genomic (DALE vs. proto-DALE). On the full 132-TF set, DALE achieves 0.896
AUROC versus proto’s 0.856 (∆ = +0.040, Wilcoxon p = 1.7×10−14, 101 wins / 22 losses).
This confirms that the current version represents a substantial improvement over the earlier
| prototype | on realistic | genomic | DNA. |     |     |     |     |
| --------- | ------------ | ------- | ---- | --- | --- | --- | --- |
53-TF genomic (full comparison). On the 53-TF subset where STREME and MEME
| genomic | results | are also | available:        |           |       |               |           |
| ------- | ------- | -------- | ----------------- | --------- | ----- | ------------- | --------- |
|         | Table   | 4:       | Genomic negatives | benchmark | (53   | TFs, Markov-1 | scoring). |
|         |         |          | Tool              | Mean      | AUROC | Time/TF       |           |
|         |         |          | DALE              |           | 0.891 | 0.3s          |           |
|         |         |          | MEME 5.5.5        |           | 0.881 | ∼90s          |           |
|         |         |          | proto-DALE        |           | 0.874 | 1.4s          |           |
|         |         |          | STREME            | 5.5.5     | 0.863 | 4.4s          |           |
DALE outperforms STREME by +0.028 AUROC (Wilcoxon p = 6.5×10−4, 35 wins / 16
losses) while running 15× faster (0.3s vs. 4.4s per TF). It also edges out MEME by +0.010
| AUROC | while | running | approximately | 300× faster. |     |     |     |
| ----- | ----- | ------- | ------------- | ------------ | --- | --- | --- |
18

Figure 5: Genomic negatives benchmark (53 TFs, Markov-1 scoring). DALE outperforms all
| three comparison |     | tools. |     |     |
| ---------------- | --- | ------ | --- | --- |
Figure 6: Per-TF comparison: DALE vs. STREME (53 TFs, genomic negatives). Points above
| the diagonal | indicate | TFs where | DALE outperforms | STREME. |
| ------------ | -------- | --------- | ---------------- | ------- |
4.6.3 Speed
| The speed | advantage | is substantial | across all benchmarks: |     |
| --------- | --------- | -------------- | ---------------------- | --- |
19

Figure 7: Runtime per TF across tools (132-TF shuffled benchmark). DALE processes all 132
| TFs in under | 45 seconds. |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
At 0.3s per TF, DALE processes the full 132-TF benchmark in under 45 seconds. STREME
requires approximately 7 minutes. MEME requires approximately 3 hours. The speedup is
algorithmic — all tools were compiled with identical optimization flags and run on identical
hardware.
| 4.6.4 Per-TF | Analysis |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
DALE wins 89 of 132 TFs against STREME on shuffled negatives. The largest individual
improvements include TFs where STREME struggles with short or degenerate motifs (e.g.,
AGO1: +0.31, BRF1: +0.26, RXRA: +0.23). STREME’s wins tend to occur on TFs where
its default width range captures wider binding patterns (e.g., BDP1: −0.11, CEBPG: −0.09);
| DALE supports     | configurable  | width          | ranges    | to           | address such | cases.  |              |          |
| ----------------- | ------------- | -------------- | --------- | ------------ | ------------ | ------- | ------------ | -------- |
| 4.6.5 Statistical | Significance  |                |           |              |              |         |              |          |
| The improvement   | over STREME   |                | is robust | across       | multiple     | tests:  |              |          |
|                   | Table         | 5: Statistical |           | significance | of DALE      |         | vs. STREME.  |          |
|                   | Test          |                |           | Shuffled     | (132 TFs)    | Genomic |              | (53 TFs) |
|                   | Wilcoxon      | p              |           |              | 4.1×10−7     |         |              | 6.5×10−4 |
|                   | Bootstrap     | 95% CI         |           | [0.023,      | 0.046]       |         | [0.010,      | 0.046]   |
|                   | McNemar       | χ2             | 13.1      | (p=2.9×10−4) |              | 6.4     | (p=1.2×10−2) |          |
|                   | Cliff’s δ     |                |           |              | +0.31        |         |              | +0.38    |
|                   | Cohen’s       | d (paired)     |           |              | +0.48        |         |              | +0.42    |
|                   | Wins / Losses |                |           |              | 88 / 44      |         |              | 35 / 16  |
| 4.6.6 Biological  | Validity      |                |           |              |              |         |              |          |
TOMTOM analysis (version 5.5.5, Pearson distance) against the JASPAR 2024 Core database
(2,633 motifs) confirmed that discovered motifs are biologically meaningful. Table 6 summarizes
the results.
20

Table 6: TOMTOM JASPAR match summary (n = 119 TFs with motifs tested).
|     |     | Metric      |          |              |      |          | DALE      | STREME    |
| --- | --- | ----------- | -------- | ------------ | ---- | -------- | --------- | --------- |
|     |     | Any         | JASPAR   | match        |      |          | 112 (94%) | 104 (87%) |
|     |     | Significant |          | (e<0.05)     |      |          | 93 (78%)  | 88 (74%)  |
|     |     | Strong      | match    | (e<0.001)    |      |          | 55 (46%)  | 51 (43%)  |
|     |     | Median      | best     | e-value      |      |          | 1.6×10−3  | 1.1×10−3  |
|     |     | Top-5       | moderate | (q <0.05)    |      |          | 100%      | 100%      |
|     |     | Top-1       | strict   | (q <0.001,   | ≥70% | overlap) | 50%       | 62%       |
|     |     | Better      | e-value  | head-to-head |      |          | 52 / 97   | 45 / 97   |
Both tools achieve 100% top-5 moderate match rate: every TF has at least one discovered
motif matching a known JASPAR entry. DALE actually matches more TFs overall (94% vs.
87%) and wins the head-to-head e-value comparison (52 vs. 45). STREME’s higher strict match
rate (62% vs. 50%) reflects its tendency to discover wider motifs that achieve higher overlap
fractions with JASPAR references — a width artifact rather than a correctness difference.
| 4.6.7 | Memory | Usage |     |     |     |     |     |     |
| ----- | ------ | ----- | --- | --- | --- | --- | --- | --- |
DALE uses 10MB peak RSS across all TFs. STREME uses approximately 113MB per TF. The
minimal footprint enables deployment in resource-constrained environments such as container-
| ized pipelines |        | or cloud | functions. |     |     |     |               |           |
| -------------- | ------ | -------- | ---------- | --- | --- | --- | ------------- | --------- |
| 5 Case         | Study: |          | ProteinGym |     |     | DMS | Substitutions | Zero-Shot |
Figure 8: ProteinGym score progression over the 8-day search. The discontinuous jump on Aug
4 occurred when the human investigator provided pre-computed predictions from five state-of-
the-art models as input data, enabling the Scientist to adopt an ensemble approach. Dashed
| lines show | the | top 3 | ProteinGym | leaderboard |     | entries. |     |     |
| ---------- | --- | ----- | ---------- | ----------- | --- | -------- | --- | --- |
To test whether the framework generalizes beyond algorithm discovery to a different class of
problem, we applied The Little Scientist to protein fitness prediction on the ProteinGym bench-
21

mark [Notin et al., 2023].
5.1 Problem Setup
ProteinGym is a large-scale benchmark for zero-shot prediction of mutation effects on protein
fitness. The DMS Substitutions benchmark comprises 217 deep mutational scanning (DMS)
assays(∼3millionmutatedsequences)coveringdiverseproteinsacrosshumans,othereukaryotes,
prokaryotes, and viruses. For each DMS assay, a model receives the wild-type sequence, a list
of mutations, and optionally a multiple sequence alignment (MSA) for the protein family. The
model predicts a fitness score for each mutant without seeing any experimental labels (zero-
shot). Performance is measured by mean Spearman rank correlation between predicted and
experimental fitness scores across all 217 assays.
At the time of writing, the ProteinGym leaderboard includes over 90 baseline models [Notin
and Marks, 2025], including billion-parameter protein language models (ESM2-15B, Progen3,
AIDOProtein-RAG16B),structure-awaremodels(ProSST,SaProt),andalignment-basedmod-
els(GEMME,VenusREM).Thetopoftheleaderboardisdominatedbymultimodalmodelsthat
combine MSAs and structural information.
5.2 Search Configuration
Unlike the motif discovery case study — where the agent wrote an algorithm from scratch
— the ProteinGym search explored ensemble composition and calibration strategies, ultimately
producingastrategywecallDeltaV.Theagenthadaccesstopre-computedzero-shotpredictions
from five existing models (VenusREM, S3F-MSA, ESM2-15B, GEMME, ProSST-2048) via a
structured data interface. The strategy function receives wild-type sequences, mutation lists,
MSAs, and per-residue structure data (solvent accessibility, burial class), and outputs a fitness
score for each mutation. The agent could combine model predictions, add structure-based
corrections, and tune calibration — but could not access experimental labels or modify the
evaluation.
Thetrust-boundaryvalidatorenforcesthisconstraintbyconstruction: thedatadatabasecon-
tainsmodelpredictionsandstructurefeaturesbutno experimentalfitnessscores(noDMS score,
no DMS score bin, no mutated sequence). Label leakage is impossible.
5.3 Diagnostic Feedback
Each evaluation produced a structured diagnostic briefing — rewritten after every iteration —
that connected strategy design choices to error patterns in the data. This briefing was the
primary observational input to the Scientist agent, serving the observation step of the scientific
method. Nine categories of computed insight were generated:
1. Calibration: where the strategy’s scores systematically diverge from experimental values
(e.g., “scores are compressed in the 0.3–0.5 range; experimental values span −5 to +15”).
2. Error direction: whether errors are biased (systematically too high or too low), not just
error magnitude.
3. Substitution class breakdown: which amino acid change types the strategy handles
worst (e.g., “charge changes at buried positions: 1.8× larger errors”).
4. MSA depth effect: performance stratified by alignment depth (e.g., “shallow-MSA pro-
teins: 0.490 vs. deep-MSA: 0.612 — strategy is unreliable when evolutionary signal is
sparse”).
5. Mutation load effect: singlevs.multi-mutantperformance(e.g.,“singlemutants: 0.563,
double mutants: 0.385 — strategy degrades on combinatorial effects”).
22

6. Assay type breakdown: performance by functional category (Activity, Binding, Ex-
pression, Organismal Fitness, Stability).
7. Conservation–error relationship: “conserved positions have 3× larger errors; strategy
assigns harmful scores at positions where WT is already optimal.”
8. Structural context: core vs. surface positions, using burial class as a proxy (e.g., “core
errors 1.8× surface errors — consider position-specific penalties based on burial”).
9. Per-protein outliers: the20weakestproteinswithMSAdepth, mutationcount, andthe
3 worst-scoring mutations each, showing substitution class, predicted vs. expected score,
and error direction.
Each insight connects a design choice in the strategy to a pattern in the errors. “Charge
changes at buried positions have 1.8× errors” points directly at a lever: add a physicochemical
penalty for charge changes at buried positions. The Scientist can immediately form a hypothesis
andtestit. Withoutthisinterpretedfeedback,theagentwouldneedtodiscoverthepatternitself
from raw per-protein score tables — a much harder reasoning task that, in earlier experiments,
produced search behavior indistinguishable from random perturbation.
Thedesignprinciplewastosurfaceinsights,notdata. Theearlierdiagnosticformatpresented
200-row tables of per-protein scores. The revised format produced ∼50 lines of interpreted
findings: “conservedpositionshave3×largererrorsandthesigniswrong”ratherthanatableof
conservationvaluesanderrormagnitudes. Thisshiftfromdatapresentationtoinsightgeneration
was the key enabler of targeted hypothesis formation.
Feedback files. ThediagnosticpipelinedeliveredfeedbackthroughtwofilesthattheScientist
read at the start of each iteration:
staging diagnostics.md was the primary feedback file, rewritten in full after every eval-
uation by the write diagnostics() function in the validation script. It contained the nine
insight categories described above, plus the top 20 weakest proteins with MSA depth and muta-
tion count, and for the bottom 5 proteins the 3 worst-scoring mutations with substitution class,
predicted vs. expected score, and error direction. The agent prompt explicitly directed: “Read
staging diagnostics.md — the most important file. Read it carefully, top to bottom. Read
the Key Insights section first — they tell you what to fix.”
history.jsonl was the experiment log, appended after each iteration. Each entry recorded
the hypothesis text, prediction range (low/high), actual score, score delta, verdict (accepted,
rejected, or false positive), top improved and regressed proteins, and a diff summary. This
gave the Scientist a record of what it had already tried, what it predicted would happen, and
what actually happened — enabling it to avoid repeating refuted approaches and to build on
confirmed ones.
Together, these two files implemented the observation and memory functions of the scientific
method: staging diagnostics.md told the Scientist what was wrong, history.jsonl told
it what it had already tried, and together they enabled targeted hypothesis formation rather
than random editing. The critical design decision was not the existence of diagnostics per se
— it was making them interpreted rather than raw. The validation function transformed raw
evaluation output (per-protein score tables, mutation-level predictions) into actionable prose:
“your scores are compressed — consider expanding the output range” and “consider position-
specificpenaltiesbasedonburial.” Thisinterpretationstep,performedbydeterministictemplate
logic in the evaluation script, offloaded the pattern-discovery work from the agent’s reasoning
to the infrastructure.
A third artifact, causal model.md, served as the agent’s running lab notebook. Unlike
the diagnostics and history files (both script-generated), the causal model was written and
maintained by the Scientist agent itself. After each iteration, the agent updated it with what
23

was tested, what the score was, and what the signal meant — recording facts and observations,
not conclusions. The validation script capped it at the last 10 entries to manage context length.
At the start of each iteration, the agent read its own accumulated notes alongside the fresh
diagnostics, enabling it to check new hypotheses against what it had already learned. This
created a three-layer feedback architecture: instrument readout (script-generated diagnostics),
lab notebook (agent-maintained causal model), and published results (script-appended history
log).
| 5.4 Search | Statistics |     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table 7: Measured compute usage for the ProteinGym case study. All figures from OpenClaw
| cron run | logs. |                 |            |            |         |     |     |     |     |     |
| -------- | ----- | --------------- | ---------- | ---------- | ------- | --- | --- | --- | --- | --- |
|          |       | Component       | Runs       | Tokens     | Model   |     |     |     |     |     |
|          |       | Scientist agent | 287        | 377.3M     | GLM-4.7 |     |     |     |     |     |
|          |       | Kuhn agent      | 104        | 95.7M      | GLM-4.7 |     |     |     |     |     |
|          |       | Infrastructure  | 38         | 2.0M       |         | —   |     |     |     |     |
|          |       | Total           | 429 475.0M | 8 calendar | days    |     |     |     |     |     |
The search ran from July 29 to August 6, 2026 (8 calendar days), producing 74 evaluated itera-
tions with 24 accepted improvements. The Scientist and Kuhn agents operated concurrently on
the same benchmark, with the Kuhn agent automatically handing off strategies to the Scientist
| when they | outperformed | the Scientist’s | current | best. |     |     |     |     |     |     |
| --------- | ------------ | --------------- | ------- | ----- | --- | --- | --- | --- | --- | --- |
5.5 Results
Delta V achieves 0.551 official category-mean Spearman correlation (0.569 flat mean
across all 217 assays), ranking first on the ProteinGym DMS Substitutions Zero-Shot
leaderboard(PR#117: https://github.com/OATML-Markslab/ProteinGym/pull/117)across
allfiveofficialevaluationmetrics(Spearman,AUC,MCC,NDCG,Top-k recall)—exceedingthe
#2 model (VenusREM, 0.518) by +0.033 Spearman. Figure 8 shows the score progression over
the 8-day search, including the data expansion that produced the largest single jump. Table 8
and Figure 9 contextualize this result against the top leaderboard entries.
Table 8: ProteinGym DMS Substitutions Zero-Shot leaderboard (top entries). All competitor
scores from the official ProteinGym evaluation pipeline (v1.3, August 2026). Delta V ranks #1
on all five official metrics. “Avg. Spearman” is the official category-mean aggregation. Delta
V’s flat mean across all 217 assays is 0.569. ∗VenusRAR reports matching Spearman on the
| same benchmark; | AUC/MCC/NDCG/Top-k |     | were             | not reported. |     |          |     |     |      |       |
| --------------- | ------------------ | --- | ---------------- | ------------- | --- | -------- | --- | --- | ---- | ----- |
| Rank            | Model              |     | Input Modalities |               |     | Spearman | AUC | MCC | NDCG | Top-k |
1 Delta V (agent-discovered) Ensemble of 5 models 0.551 0.801 0.430 0.800 0.254
2 VenusRAR [Tan et al., 2026] Multi-modal ensemble + CoT 0.551∗ — — — —
| 3   | VenusREM |     | Structure | & MSA |     | 0.518 | 0.783 | 0.404 | 0.770 | 0.244 |
| --- | -------- | --- | --------- | ----- | --- | ----- | ----- | ----- | ----- | ----- |
4 ProSST (K=2048) Sequence & Structure 0.507 0.777 0.398 0.757 0.236
5 ProSST (K=4096) Sequence & Structure 0.498 0.773 0.385 0.774 0.232
| 6   | S3F-MSA |     | Structure | & MSA |     | 0.496 | 0.771 | 0.387 | 0.792 | 0.243 |
| --- | ------- | --- | --------- | ----- | --- | ----- | ----- | ----- | ----- | ----- |
| 7   | S2F-MSA |     | Structure | & MSA |     | 0.488 | 0.767 | 0.381 | 0.790 | 0.240 |
8 ProSST (K=1024) Sequence & Structure 0.485 0.764 0.372 0.761 0.230
| 9   | ESCOTT |     | Structure | & MSA |     | 0.476 | 0.761 | 0.370 | 0.779 | 0.213 |
| --- | ------ | --- | --------- | ----- | --- | ----- | ----- | ----- | ----- | ----- |
10 ProSST (K=512) Sequence & Structure 0.471 0.757 0.360 0.759 0.222
24

Figure 9: ProteinGym DMS Substitutions Zero-Shot leaderboard (top entries). Delta V exceeds
all 96 scored models on the leaderboard, ranking #1 on all five official metrics.
The +0.033 margin over VenusREM exceeds the spread between rank 2 (0.518) and rank 10
(0.470) on the 96-model leaderboard — Delta V’s advantage over the field is larger than the gap
separating the entire current top 10. Table 9 compares Delta V against the best competitor in
| each functional | category. |     |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- | --- |
Table 9: Per-category Spearman scores: Delta V vs. VenusRAR-Rank vs. best competitor.
Scores from official ProteinGym pipeline. VenusRAR-Rank scores from Tan et al. [2026], Table
2. Delta V wins 2 of 5 categories head-to-head; VenusRAR-Rank wins 3. The approaches
capture different signal — Delta V is strongest on Expression (+0.057), VenusRAR-Rank on
Stability (+0.016).
| Category   | #UniProt | Delta     | V VenusRAR-Rank | Best Other |                | Margin |
| ---------- | -------- | --------- | --------------- | ---------- | -------------- | ------ |
| Activity   |          | 37 0.549  | 0.539           | VenusREM   | (0.495)        | +0.054 |
| Expression |          | 11 0.554  | 0.497           | VenusREM   | (0.533)        | +0.057 |
| Organismal | Fitness  | 62 0.523  | 0.558           | VenusREM   | (0.459)        | −0.035 |
| Stability  |          | 66 0.642  | 0.658           | ProSST     | K=2048 (0.653) | −0.016 |
| Binding    |          | 10 0.486  | 0.497           | ProSST     | K=4096 (0.472) | −0.011 |
| Official   | mean     | 186 0.551 | 0.551           | VenusREM   | (0.518)        | +0.033 |
DeltaVandVenusRAR-RankachievethesameheadlineSpearman(0.551)butwithcomple-
mentaryper-categoryprofiles(Table9). DeltaVisstrongeronExpression(+0.057)andActivity
(+0.010); VenusRAR-Rank is stronger on Stability (+0.016), Organismal Fitness (+0.035), and
Binding (+0.011). This pattern suggests the approaches capture different biological signal. A
critical architectural difference underlies these results: VenusRAR uses per-protein LLM calls at
inference time to dynamically calibrate ensemble weights, while Delta V uses an LLM-evolved
static strategy requiring no inference-time LLM calls (475M tokens over 8 calendar days on a
single VPS without GPU resources). Both achieve the same headline metric through different
mechanisms.
25

Statisticalsignificance. Bootstrapconfidenceintervals(10,000iterations,seed=42)confirm
thatDeltaV’sadvantageisrobust. The95%CIofDeltaV’sflatmeanSpearman([0.549,0.588])
doesnotoverlapwithVenusREM’s([0.514,0.557]). Thepairedtest(DeltaV−VenusREM,per-
protein, n = 217) yields a mean difference of +0.033 (SE = 0.004, 95% CI [+0.025, +0.042]); in
10,000bootstrapsamples,DeltaVneverfellbelowVenusREM(p < 10−4). Theofficialcategory-
meanCIiswider(±0.027)becauseitaveragesoveronly5categories,introducinghighervariance
from the small denominator. This aggregation effect is inherent to the official metric and affects
all models equally.
Search efficiency. Figure10summarizesthesearchdynamics. TheScientistagentconducted
101 runs over 42 hours, accepting 29 proposals (29%) and achieving 5 new best scores (20.2 runs
per improvement). The Kuhn agent conducted 35 runs over 48 hours with 3 acceptances (9%)
and 0 new bests. The Scientist’s gain per hour was 2.4× that of the Kuhn agent. Notably,
the Scientist reached its final best score in 15 runs after the data expansion transition (∼16.5M
tokens). For comparison, ShinkaEvolve reports 150 samples for a single circle packing instance
witha$20budgetcapacross4parallelmodels,thoughdirectcomparisonislimitedbydifferences
in problem complexity, evaluation cost, and unreported per-sample compute (Xing et al. 2026).
FunSearch reports ∼2,000,000 programs for comparable tasks. Neither system reports total
tokens or wall-clock time.
26

Figure 10: Search efficiency comparison between Scientist and Kuhn agents on the Prote-
inGym zero-shot task. Top row: cumulative improvements over time and magnitude of each
improvement. Middle row: rolling acceptance rate and best score trajectory. Bottom row: per-
| achievement | cost | and summary | statistics. |
| ----------- | ---- | ----------- | ----------- |
The data expansion transition. The discontinuous jump in Figure 8 (from 0.445 on Aug
2 to 0.578 on Aug 4) warrants explanation. This was not an algorithmic breakthrough by
the Scientist — it was a human intervention. The investigator recognized that the five top-
scoring models on the ProteinGym leaderboard publish their zero-shot predictions, and added
these as available data inputs. Once the Scientist had access to multiple model predictions, it
independently decided to build an ensemble with calibration, rather than continuing to optimize
a single-model approach. This illustrates the human-in-the-loop nature of the framework (§2.5):
thehumanexpandedthesearchspacebyprovidingnewdatasources,andtheautonomoussearch
| loop explored  | that | space.    |         |
| -------------- | ---- | --------- | ------- |
| 5.6 Discovered |      | Strategy: | Delta V |
The agent discovered a strategy called CPCWE (Constraint-Propagated Confidence-Weighted
Ensemble), implemented as Delta V. The strategy has seven stages, each added incrementally
| across | the 24 accepted | improvements: |     |
| ------ | --------------- | ------------- | --- |
27

| 5.6.1 | Quantile | Calibration |     |     |     |     |     |     |
| ----- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
Raw model scores are calibrated using empirical quantiles (percentiles 1, 5, 10, 25, 50, 75, 90,
95, 99). For each model independently, the median predicted score is identified. Scores below
the median are expanded asymmetrically (2.3× distance from median) while scores above the
median are left unchanged (1.0× expansion). This corrects for systematic under-prediction of
mutation severity: LLM-based models tend to predict scores clustered near zero, compressing
| the harmful | tail | of  | the distribution. |     |     |     |     |     |
| ----------- | ---- | --- | ----------------- | --- | --- | --- | --- | --- |
The calibration is computed per-protein across all mutations, ensuring that the expanded
tails are relative to each protein’s score distribution rather than absolute thresholds.
| 5.6.2 | Z-score | Normalization |     |     |     |     |     |     |
| ----- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
Calibratedscoresfromeachmodelarez-scorenormalized(mean-centeredandscaledbystandard
deviation) before ensemble combination. This prevents models with wider output ranges from
dominating the ensemble. After normalization, all five models contribute on the same scale.
| 5.6.3 | Confidence-Weighted |     |     | Ensemble |     |     |     |     |
| ----- | ------------------- | --- | --- | -------- | --- | --- | --- | --- |
The five base models (VenusREM, S3F-MSA, ESM2-15B, GEMME, ProSST-2048) are com-
bined using confidence-weighted blending with model-specific scaling factors. Each model has a
confidence scaling parameter that controls how strongly its disagreement from the ensemble is
weighted:
| • VenusREM: |     | α   | = 1.0 (high | confidence |     | in disagreement) |     |     |
| ----------- | --- | --- | ----------- | ---------- | --- | ---------------- | --- | --- |
•
| S3F-MSA:    |     | α = | 1.0                 |     |     |              |               |     |
| ----------- | --- | --- | ------------------- | --- | --- | ------------ | ------------- | --- |
| • ESM2-15B: |     | α   | = 0.5 (conservative |     | —   | disagreement | downweighted) |     |
•
| GEMME:         |                | α = | 0.5        |            |           |       |                   |     |
| -------------- | -------------- | --- | ---------- | ---------- | --------- | ----- | ----------------- | --- |
| • ProSST-2048: |                |     | α = 1.5    | (strongest | weighting |       | for disagreement) |     |
| For            | each mutation, |     | the weight | of         | model     | m is: |                   |     |
wbase·(1+α
|     |     |     |     | w   | m = |     | m ·c m ) | (1) |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
m
wbase
where is the MSA-depth-adaptive base weight and c m ∈ [0,1] is the confidence score
m
(normalized absolute z-score). Models with high confidence and high scaling factors contribute
| more when | they | disagree | with | the | ensemble | consensus. |     |     |
| --------- | ---- | -------- | ---- | --- | -------- | ---------- | --- | --- |
Base weights depend on MSA depth. For proteins with deep MSAs (≥500 sequences), the
| distribution | favors |     | conservation-aware |     | models: |     |     |     |
| ------------ | ------ | --- | ------------------ | --- | ------- | --- | --- | --- |
•
DeepMSA:VenusREM0.314,S3F-MSA0.236,ESM2-15B0.236,GEMME0.125,ProSST-
| 2048 | 0.089 |     |     |     |     |     |     |     |
| ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
•
ShallowMSA:VenusREM0.471,S3F-MSA0.236,ESM2-15B0.078,GEMME0.125,ProSST-
| 2048 | 0.089 |     |     |     |     |     |     |     |
| ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
28

| 5.6.4 | Residual |     | Propagation |     |     |     |     |     |     |     |
| ----- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
A novel mechanism not present in standard ensemble approaches: after the initial confidence-
weighted ensemble, Delta V computes per-model residuals (how far each model’s prediction de-
viates from the ensemble consensus) and propagates these residuals across structurally similar
positions within a 5-residue window, weighted by RSA similarity. This is not spatial smoothing
— it is closer to a message-passing algorithm. The intuition: if VenusREM is systematically
wrong at position 42, it is probably also wrong at positions 40–44 with similar solvent accessi-
| bility. | Three      | iterations  | with                | decreasing |     | damping  | (0.3,   | 0.15,   | 0.1):  |     |
| ------- | ---------- | ----------- | ------------------- | ---------- | --- | -------- | ------- | ------- | ------ | --- |
|         | For each   | iteration   | i:                  |            |     |          |         |         |        |     |
|         | 1. Compute | the         | confidence-weighted |            |     | ensemble | blended | score.  |        |     |
|         | 2. For     | each model, | compute             |            | the | residual | r = (z  | −z¯)/(c | +0.1). |     |
|         |            |             |                     |            |     |          | m       | m       | m      |     |
3. Average residuals at positions within 5 residues, weighted by RSA distance and confidence
ratio.
4. Subtract the damped correction γ i = 0.3/(i+1) from each model’s z-score.
| 5.6.5 | Conservation-Modulated |     |     |     |     | GEMME | Weighting |     |     |     |
| ----- | ---------------------- | --- | --- | --- | --- | ----- | --------- | --- | --- | --- |
GEMME’spureevolutionarysignalismodulatedper-mutationatruntimeusingposition-specific
| Shannon |     | entropy | H(p) computed |     | from  | the MSA:    |       |              |     |     |
| ------- | --- | ------- | ------------- | --- | ----- | ----------- | ----- | ------------ | --- | --- |
|         |     |         |               | w   |       | (p) = wbase |       | ·(1.5−Hˆ(p)) |     | (2) |
|         |     |         |               |     | GEMME |             | GEMME |              |     |     |
where Hˆ(p) ∈ [0,1] is normalized entropy. At conserved positions (low entropy), GEMME’s
weight increases up to 1.5×; at variable positions (high entropy), it decreases to 0.5×. This
captures the intuition that evolutionary conservation is more informative at positions where few
| amino | acids           | are | tolerated. |           |     |     |     |     |     |     |
| ----- | --------------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
| 5.6.6 | Structure-Based |     |            | Penalties |     |     |     |     |     |     |
Atburiedpositions(relativesolventaccessibility<0.2),mutationseverityisadjustedusingRSA,
burial class, and physicochemical properties of the substitution. The penalty is multiplicative
across properties:
|     | • Charge | changes | (×0.90) |      |     |            |     |     |     |     |
| --- | -------- | ------- | ------- | ---- | --- | ---------- | --- | --- | --- | --- |
|     | • Large  | volume  | changes | |∆V| | >   | 50 (×0.95) |     |     |     |     |
•
|     | Hydrophobicity    |     | shifts             | |∆H| | >          | 2.0 (×0.95) |     |     |     |     |
| --- | ----------------- | --- | ------------------ | ---- | ---------- | ----------- | --- | --- | --- | --- |
|     | • Glycine/proline |     | backbone           |      | disruption | (×0.95)     |     |     |     |     |
|     | • Aromatic        |     | residue disruption |      | (×0.95)    |             |     |     |     |     |
Penalty multipliers are assay-specific: stability and activity assays apply stronger penalties
| than  | binding | assays, | reflecting |           | different | structural |     | tolerances. |     |     |
| ----- | ------- | ------- | ---------- | --------- | --------- | ---------- | --- | ----------- | --- | --- |
| 5.6.7 | Dynamic |         | Range      | Expansion |           |            |     |             |     |     |
sign(x)·|x|0.7
The final stage applies a power transformation f(x) = to the ensemble output.
Because p < 1, this expands the tails of the distribution — extreme predictions (both harmful
and benign) are amplified while near-zero predictions are compressed. This corrects for the
tendency of ensembles to average out extreme predictions, recovering discriminative power at
| the | tails where | the | most | informative |     | mutations | reside. |     |     |     |
| --- | ----------- | --- | ---- | ----------- | --- | --------- | ------- | --- | --- | --- |
29

Summary. None of these components is novel in isolation — quantile calibration, adaptive
ensembling, structure-based corrections, and power transformations are well-established tech-
niques. The contribution is that the agent discovered the combination, scaling, and calibration
of these techniques autonomously. Delta V is an ensemble + iterative residual correction +
structural/physicochemical feature corrections + MSA-derived corrections + non-linear output
transform. The residual propagation mechanism and the specific calibration parameters (2.3×
harmful expansion, p = 0.7 power, propagation radius 5, damping schedule 0.3/0.15/0.1) were
not predetermined — they emerged from the agent’s hypothesis-driven search.
5.7 Interpretation
This result demonstrates a different capability of the framework than the motif discovery case
study. In motif discovery, the agent wrote a novel algorithm from scratch. In ProteinGym,
the agent discovered Delta V, an ensemble calibration strategy that outperforms all individual
models, including 16-billion-parameter systems. The framework thus supports two modes of
discovery: de novo algorithm design and meta-learning over existing approaches.
Thedistinctionbetweenautomatedscientificiterationandtop-downdesignisworthexamin-
ing. Adatascientistapproachingthesameensembleproblemwouldtypicallyframeitaslearning
an optimal global combination function — fixed weights applied independently to each muta-
tion [Zhang et al., 2024]. Per-instance uncertainty-weighted ensembling, where predictions are
adjusted by the model’s own confidence, is a known technique [Lakshminarayanan et al., 2017,
Kwon et al., 2026]. What is novel in Delta V is the iterative residual propagation: per-model
disagreement is propagated across structurally similar positions, making the ensemble’s predic-
tion at position p depend on model behavior at neighboring positions. This spatial, iterative
mechanism has analogs in message-passing networks [Gilmer et al., 2017] and label propagation
[Zhu, 2002], but applying it to ensemble residuals rather than node features or label spreading
is, to our knowledge, not precedented in the protein fitness prediction literature. Whether the
improvementcomesfromcapturinggenuinepositionalerrorstructureorfromfittingtozero-shot
model quirks is an open question — one our planned supervised experiments may help answer.
The broader point stands: hypothesis-driven iteration discovered an effective combination that
resists top-down assembly, even when the individual components are classical.
WenotethattheProteinGymresultisnotdirectlycomparabletoAlphaEvolveorFunSearch,
which do not report results on public benchmark leaderboards. It is comparable in spirit,
however, to AlphaEvolve’s Google infrastructure optimizations, where the system found better
configurationsofexistingcomponentsratherthaninventingfundamentallynewalgorithms. The
computational efficiency of hypothesis-driven search is discussed in §7.2.
The complementary per-category profiles of Delta V and VenusRAR-Rank (Table 9) are
worth examining. VenusRAR-Rank’s per-protein LLM reasoning at inference time produces
stronger Stability and Organismal Fitness predictions, suggesting that LLM-augmented biolog-
ical auditing captures signal relevant to those categories. Delta V’s static calibration strategy
produces stronger Expression and Activity predictions, suggesting that the autonomously dis-
coveredcalibrationpipelinecapturessignalthatLLMpost-hocauditingmisses. Theapproaches
arenotredundant—theyarecomplementary. Combiningthem(applyingVenusRAR’sReason-
Stage auditing atop Delta V’s rankings) is a natural future experiment.
6 Ablations
The search history provides natural ablation experiments. Because the framework was built
iteratively — each infrastructure change addressing a specific failure mode — we can compare
performance across phases to estimate the contribution of each component.
30

| 6.1 Development |     | Timeline |     |     |     |     |     |     |
| --------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
Table 10 compares the search performance under progressive infrastructure additions. Each row
| adds one component |     | to the | previous | row’s | configuration. |     |     |     |
| ------------------ | --- | ------ | -------- | ----- | -------------- | --- | --- | --- |
Table 10: Development timeline: effect of progressive infrastructure additions on search out-
comes. Each row adds one component to the previous configuration. Smoke-test AUROC is
the 5-TF proxy metric used during search; full-benchmark AUROC is the 132-TF final metric.
Rows are sequential additions, not independent variables — see §7.2 for limitations.
| Configuration |     |     |     |     |     | Smoke peak | Full eval Runs | to peak Tokens |
| ------------- | --- | --- | --- | --- | --- | ---------- | -------------- | -------------- |
Baseline (synthetic eval, loose prompt, no diagnostics) 0.664 — 1,588 97.6M
| + Real benchmark |     | data (15 | ChIP-seq | TFs, | AUROC) | 0.565 | —   | 11 — |
| ---------------- | --- | -------- | -------- | ---- | ------ | ----- | --- | ---- |
+ Causal scaffold prompt (7-field structured plan) 0.709 — 11 —
| + Per-instance   | diagnostics |                  | restored |     |     | 0.794 | —     | 23 —      |
| ---------------- | ----------- | ---------------- | -------- | --- | --- | ----- | ----- | --------- |
| + Kuhn paradigm  |             | agent            |          |     |     | 0.794 | —     | 63 33.5M  |
| + All components |             | (full framework) |          |     |     | 0.846 | 0.842 | 500 97.9M |
Interpretation. Thebaselineconfiguration(Phase1)stalledat0.664onsyntheticdataacross
1,588 runs and 97.6M tokens — zero accepted improvements in the final 49 runs. Replacing
the synthetic benchmark with real ChIP-seq data immediately improved the smoke score from
0.312 to 0.565 in a single experiment, confirming that the agent had been optimizing the wrong
objective. Adding the causal scaffold prompt (structured hypothesis, prediction, falsification
criterion) improved from 0.565 to 0.709 in 11 experiments. Restoring the deleted per-instance
diagnostics enabled the agent to form targeted hypotheses, reaching 0.794. The Kuhn paradigm
agent’s contribution cannot be isolated as a single-line improvement because it operated con-
currently with the other changes, but its analysis drove the shift from probability-based to
| frequency-based | enumeration. |            |          |     |            |       |     |     |
| --------------- | ------------ | ---------- | -------- | --- | ---------- | ----- | --- | --- |
| 6.2 Effect      | of           | Structured | Feedback |     | vs. Scalar | Score |     |     |
The clearest ablation is the effect of diagnostic detail. During Phase 1, the evaluator produced
per-TF diagnostics, but a cleanup script silently deleted them before the agent could read them.
The agent saw only aggregate scores. After the fix, the agent could see which TFs improved or
regressed, what widths were selected, and how its results compared to baseline tools.
•
Without per-instance diagnostics(1,588runs): agentmadefull-rewritechanges,could
not form targeted hypotheses, stalled at 0.664. Zero improvements in final 49 runs.
• Withper-instancediagnostics(first11runsafterfix): twobreakthroughimprovements
(0.312 → 0.565 → 0.709). Agent made targeted edits and cited specific TF results in its
hypotheses.
This confirms the core architectural claim: structured per-instance feedback is essential
for hypothesis-driven search. With scalar feedback alone, the search degenerates into blind
optimization.
| 6.3 Search | Efficiency: |     | Improvement |     | Rate |     |     |     |
| ---------- | ----------- | --- | ----------- | --- | ---- | --- | --- | --- |
Across all phases, 17 of ∼300 evaluated iterations produced improvements (5.7%). Breaking
this down:
•
Phase 1 (no infrastructure): 0 improvements in final 49 evaluated iterations (0%)
31

• Phase 2 (full infrastructure): 17 improvements in ∼64 evaluated iterations (26.6%)
The 26.6% improvement rate under the full framework is dramatically higher than the 0%
rate under the baseline configuration, and also higher than the ∼5% rate typical of evolutionary
approaches where most mutations are neutral or deleterious. This suggests that hypothesis-
driven search with structured feedback is substantially more sample-efficient than scalar-fitness
evolutionary search, though we cannot make a direct comparison without running evolutionary
baselines on the same problem.
7 Discussion
7.1 What the Search Discovered
The Little Scientist’s search produced an algorithm that combines established and novel design
choices. The framework independently arrived at k-mer enumeration as a seeding strategy and
EMasarefinementmechanism—bothwell-knowninthehuman-designedliterature. Butitalso
discovered strategies that, to our knowledge, have not been published: a dual-seeding approach
that combines abundance and consistency metrics, Pareto-front ranking that preserves diverse
width strategies, and effective-width–aware scoring that penalizes uninformative positions.
The search statistics are informative about the nature of algorithmic discovery. Of the
evaluated iterations under the full framework, 17 of ∼64 produced improvements — a 26.6%
successrate. Thenon-improvingiterationswerenotwasted: theytestedandrefutedhypotheses,
progressivelyconstrainingthedesignspace. Thispatternmirrorshumanalgorithmdevelopment,
where most ideas do not work, and the ones that do are built on the scaffolding of many failures.
7.2 Implications for Agentic Science
Li et al. [2026] propose that teams of LLM-based agents can function as computational research
teams, arguing that agentic systems will accelerate biomedical discovery. Our results provide
concrete, benchmarked evidence for this vision in a specific, competitive domain.
The key architectural choice that distinguishes The Little Scientist from prior agent-driven
discovery systems (AlphaEvolve, FunSearch, EoH) is the combination of hypothesis-driven
search and structured per-instance feedback. This distinction aligns with independent theoret-
ical work arguing that auto-research systems need cheap, dense signals of epistemic progress—
analogous to coverage in fuzzing—rather than relying solely on terminal evaluation scores [He,
2026]. AlphaEvolveandFunSearchuseevolutionaryoperators—mutationandcrossoveroncode
— guided by a scalar fitness signal. The Scientist agent, by contrast, forms explicit hypotheses
(“I expect [change] will [improve/worsen] because [reasoning]”) and receives per-instance diag-
nostic feedback that enables targeted reasoning about failures. This means the evaluator does
analytical work for the scientist, not just scoring.
Thecomputeimplicationsaresignificant. Computedetailsforbothcasestudiesarereported
in §2.6 and §4.4, and Figure 10 provides run-level efficiency metrics. While a direct token-to-
token comparison with AlphaEvolve or FunSearch is not possible (neither system reports token
counts), our result suggests that hypothesis-driven search with structured feedback can achieve
top-rankedbenchmarkperformancewithouttheinfrastructuredemandsoflarge-scaleevolution-
ary search. A distinguishing feature is full iteration-level transparency: every run’s hypothesis,
score, and acceptance decision is logged, enabling post-hoc analysis of search dynamics. Neither
AlphaEvolve nor FunSearch publishes this level of detail.
Whether the approach generalizes to other domains remains an open question. Motif dis-
covery has properties that favor agent-driven search: interpretable code, a clear scalar metric,
and fast evaluation cycles. Domains where evaluation is expensive (e.g., wet-lab experiments)
32

or where algorithms are expressed as large neural networks rather than compact code may pose
greater challenges.
A broader observation: the success of this approach reflects a shift in how we conceptualize
LLM-based agents. The dominant paradigm treats LLMs as computational tools — advanced
textprocessorsthatexecuteinstructions. TheLittleScientisttreatstheLLMagentassomething
closer to a junior researcher: one that can reason about prior results, form hypotheses, consult
the literature, and design experiments. The distinction matters because it changes what we
expect from the system. A tool is judged on whether it executes correctly; a researcher is judged
on whether they produce insight. The framework’s 26.6% acceptance rate — where 73.4% of
evaluated iterations produce no improvement — is not a failure of execution but a characteristic
of exploratory research. Run-to-run score deltas show strong negative autocorrelation (r =
−0.45): 65% of runs reverse direction from the previous run, with corrections after large failures
producing swings 5–6× larger than after small changes. This pattern reflects a hill-climbing
search that makes large corrective leaps after failure rather than random exploration — the
non-improving iterations are the scaffolding on which the improving ones are built, just as
in human science. This suggests that evaluation criteria for agentic systems should measure
research productivity (insights generated, design space explored, failure modes identified) rather
than just end-state accuracy.
Theimplicationisthatagenticsystemscanbestbeutilizedwithtraditionallyhumanpatterns
for understanding — hypothesis, prediction, experiment, reconciliation — rather than designing
agentic research from concepts derived from computer science alone (evolutionary search, rein-
forcement learning, genetic algorithms). This does not mean those CS-derived approaches are
inferior; it means the space of productive agent architectures may be larger than the paradigm
that has dominated the field.
We cannot isolate which individual infrastructure component was most responsible for the
Phase1toPhase2improvement. Thefivechanges(realbenchmarkdata,causalscaffoldprompt,
trust-boundary validator, fixed diagnostic pipeline, Kuhn paradigm agent) were made sequen-
tiallyinresponsetoobservedfailuremodes, notinacontrolledfactorialdesign. Table10records
thesequence, butthecontributionofeachcomponentremainsuncertain. Theframeworkshould
be evaluated as an integrated system; claims about individual mechanisms require controlled
experiments we have not conducted.
7.3 Collaborative Human-Agent Research
A notable design property of The Little Scientist is that the human investigator can interact
with the search process as it unfolds. The system progresses autonomously — the Scientist and
Kuhnagentsiterate,evaluate,andimprovewithoutintervention—butthehumanremainsinthe
loop in a fundamentally different way than traditional supervised systems. Rather than merely
monitoring for failures, the investigator can: observe accumulated diagnostics and redirect the
search; discussstrategywiththeagentsthroughnaturalconversation; injectone-offexperiments
to test a hypothesis; add new data or models at any point; benchmark intermediate results
against external tools; and trigger paradigm shifts when they judge the time is right.
This fluid, conversational interaction between human and agent is a feature, not a limita-
tion to be automated away. It mirrors how a principal investigator collaborates with a junior
researcher: the junior researcher works independently on day-to-day experimentation, but ben-
efits from the senior investigator’s broader context, domain knowledge, and strategic judgment.
An important distinction: the human investigator (a data scientist, not a domain expert
in bioinformatics or structural biology) designed the evaluation infrastructure — the diagnos-
tic pipeline, the smoke-test/full-evaluation two-tier loop, the trust-boundary validator, and the
Kuhn prompt template — while the domain-specific algorithmic decisions were entirely agent-
originated. For motif discovery, the human did not suggest k-mer enumeration, EM refinement,
dual-seed selection, or Pareto ranking — these emerged from the agent’s search. For Prote-
33

inGym, the human provided pre-computed model predictions as input data but did not direct
the ensemble calibration strategy, the residual propagation mechanism, or the dynamic range
expansion. This suggests that the framework may not require domain expertise to produce
domain-specific results, though the evaluation infrastructure must be designed with care.
The framework’s architecture — with the OpenClaw agent platform handling LLM invoca-
tion,scheduling,andsandboxedexecution—makesthiscollaborationpractical: theinvestigator
interacts through a messaging interface (Telegram), receiving progress updates and agent sum-
maries, while the agents handle the experimental workload. This is a productive model for
scientific computing that leverages the complementary strengths of human researchers (strate-
gicdirection,domainexpertise,datacuration)andLLMagents(rapiditeration,exhaustivecode
exploration, tireless hypothesis testing).
7.4 Limitations and Future Directions
1. Two case studies. We demonstrate the framework on two domains (motif discovery and
proteinfitnessprediction). Generalizationtootherbioinformaticsproblemsisplannedbut
requires further evidence.
2. Benchmark dependency. The framework requires a well-defined benchmark with clear
metricsandground-truthevaluationdata. Thisisastructurallimitation: theframework’s
applicability is bounded by benchmark availability. For domains where ground-truth eval-
uation is cheap and standardized (motif discovery, protein fitness, drug-target binding,
RNA structure prediction), the framework can operate autonomously. For domains where
evaluationisexpensive,subjective,orunstructured,thebottleneckisnottheagentbutthe
absence of benchmark infrastructure. We argue that more effort directed toward problem
formalization—encodingscientificquestionsasbenchmarkabletaskswithstructureddata
— would unlock autonomous discovery across a wider range of domains. The existence
of comprehensive benchmarks like ProteinGym [Notin et al., 2023] and ENCODE demon-
strates that this curation work is feasible but requires sustained community investment.
3. Single motif per TF. DALE returns one motif per TF. Combinatory motif discovery
(finding co-occurring TF binding patterns, as in ProSampler) is out of scope.
4. LLM dependency. The framework’s reasoning quality depends on the underlying lan-
guage model. Improvements in LLM capability may directly improve search effectiveness.
5. No wet-lab validation. Our results are computational benchmarks only. VenusRAR
provides wet-lab validation on Cas12i3 nuclease (14/30 hits, 4–5× activity improvements)
[Tan et al., 2026]; we lack equivalent experimental confirmation. Wet-lab validation of
Delta V’s predictions, particularly in the Expression and Activity categories where it
outperforms competitors, would substantially strengthen the work.
6. Controlled ablation. We cannot quantify the contribution of individual framework
components because the infrastructure was developed sequentially and LLM outputs are
non-deterministic across runs. A controlled ablation — running each component in isola-
tion with multiple replicates on the same benchmark — would require ∼100M tokens per
configuration and ∼10 replicates for statistical power, totaling billions of tokens. We have
notconductedthisstudy. TheclosestevidenceisthePhase1diagnosticdeletion: thesame
frameworkproducedstalledsearchwhenper-instancediagnosticsweresilentlydeleted,and
productivesearchwhentheywererestored(§5.2). Thissinglenaturalexperimentsupports
the importance of structured feedback but does not isolate other components. We recom-
mend controlled ablation as future work, ideally using a smaller benchmark that permits
multiple replicates at manageable cost.
34

7. ML-based discovery. Both case studies produced classical algorithms (Python func-
tions). Anaturalextensionistoapplytheframeworktodiscovermachine-learningpipelines
— not just ensemble strategies like Delta V, but novel architectures, training procedures,
or data augmentation policies. The framework’s requirement for a benchmark oracle is
satisfied by most ML benchmarks, making this a promising near-term direction.
8. Benchmarkformulationasafirst-classactivity. Themostimmediategainswillcome
fromformulatingnewproblemsasbenchmarksororacles. Theframework’sapplicabilityis
boundednotbyagentcapabilitybutbytheavailabilityofwell-definedevaluationfunctions.
Communityinvestmentinbenchmarkinfrastructure—followingthemodelofProteinGym
andENCODE—isthehighest-leveragepathtoexpandingtherangeofdomainsaccessible
to autonomous discovery.
Data availability.
Motif discovery. All benchmark data used in this study is publicly available. ChIP-seq
peak sequences for 132 ENCODE K562 transcription factors were obtained from the ENCODE
Consortium [Consortium, 2012] (https://www.encodeproject.org). Peak regions were pro-
cessed into 100bp centered windows around summits. JASPAR 2024 [Castro-Mondragon et al.,
2024]motifprofiles(https://jaspar.elixir.org)wereusedasreferencemotifsforTOMTOM
comparison. Shuffled and genomic negative sequences were generated from the same assemblies
using standard protocols. No custom or proprietary datasets were generated.
ProteinGym DMS Substitutions Zero-Shot (Delta V). All data used by Delta V is publicly
availablefromtheProteinGymbenchmark[Notinetal.,2023](https://www.proteingym.org).
This includes: (1) the 217 DMS assay datasets with wild-type sequences, mutation lists, and
experimental fitness scores; (2) zero-shot predictions from five state-of-the-art models — Venus-
REM, S3F-MSA, ESM2-15B, GEMME, and ProSST-2048 — obtained from the ProteinGym
website; (3) per-residue structural features (relative solvent accessibility, burial class) derived
from AlphaFoldDB predictions. MSA data was sourced from ProteinGym’s standardized align-
ments. No custom or proprietary datasets were generated.
Code availability.
DALE. The discovered algorithm is distributed as a statically-linked binary and Python
interface, along with the full C source, benchmark scripts, and a reproducible Jupyter notebook,
at https://github.com/travis42/little-scientist-dale.
Delta V. The discovered ensemble strategy (a Python function), the evaluation pipeline, and
thefullsearchhistory(allarchivediterations)areavailableathttps://github.com/travis42/
little-scientist-delta-v.
Framework. The Little Scientist framework — including agent prompts, evaluation envi-
ronment code, the Kuhn agent, and the cron-driven orchestration — is available at https:
//github.com/travis42/little-scientist-dale. The framework uses the OpenClaw agent
platform(https://github.com/openclaw/openclaw)forLLMinvocation,scheduling,andsand-
boxed execution. No fine-tuning or training of language models was performed; API access for
inference is sufficient. The LLM used was GLM-4.7 (Z.ai), accessed via a coding plan subscrip-
tion.
Acknowledgements: The author thanks the ENCODE Consortium for providing open-access
ChIP-seq data, the JASPAR database for motif reference data, and the MEME Suite develop-
ment team — Timothy Bailey, Charles Grant, and William Noble — whose tools (STREME,
MEME, TOMTOM) were used extensively in this study and whose work has advanced the field
of computational motif discovery over three decades. Portions of this manuscript’s prose were
drafted with assistance from z.ai’s GLM 5.1, under the author’s direction; the author reviewed,
edited, and takes full responsibility for all content.
35

| Funding: | This | work | received | no  | external | funding. |     |
| -------- | ---- | ---- | -------- | --- | -------- | -------- | --- |
References
Timothy L Bailey. Dreme: motif discovery in transcription factor chip-seq data. Bioinformatics,
| 27(12):1653–1659, |     |     | 2011. |     |     |     |     |
| ----------------- | --- | --- | ----- | --- | --- | --- | --- |
Timothy L Bailey. Streme: Accurate and efficient sequence motif discovery. Bioinformatics
| Advances, | 1(1):vbab021, |     |     | 2021. |     |     |     |
| --------- | ------------- | --- | --- | ----- | --- | --- | --- |
Timothy L Bailey and Charles Elkan. Fitting a mixture model by expectation maximization
to discover motifs in biopolymers. Proceedings of the Second International Conference on
| Intelligent | Systems |     | for Molecular |     | Biology, | 2:28–36, | 1994. |
| ----------- | ------- | --- | ------------- | --- | -------- | -------- | ----- |
Jaime A Castro-Mondragon et al. Jaspar 2024: 20th anniversary of the open-access database of
transcription factor binding-site profiles. Nucleic Acids Research, 52(D1):D174–D182, 2024.
ENCODE Project Consortium. An integrated encyclopedia of dna elements in the human
| genome. | Nature, | 489(7414):57–74, |     |     | 2012. |     |     |
| ------- | ------- | ---------------- | --- | --- | ----- | --- | --- |
Jonathan Frazer, Pascal Notin, Mariana Dias, Alan Gomez, James K Min, Kevin Brock, et al.
Disease variant prediction with deep generative models of evolutionary data. Nature, 599
| (7883):91–95, |     | 2021. |     |     |     |     |     |
| ------------- | --- | ----- | --- | --- | --- | --- | --- |
Justin Gilmer, Samuel S Schoenholz, Patrick F Riley, Oriol Vinyals, and George E Dahl. Neural
message passing for quantum chemistry. In Proceedings of the 34th International Conference
on Machine Learning, volume 70 of Proceedings of Machine Learning Research, pages 1263–
1272, 2017.
Yifeng He. Agentic auto-research is fuzz testing. arXiv preprint arXiv:2608.09855, 2026.
Sven Heinz, Christopher Benner, Nathanael Spann, Eric Bertolino, Yin C Lin, Peter Laslo,
Jason X Cheng, Cornelis Murre, Harinder Singh, and Christopher K Glass. Simple combina-
tions of lineage-determining transcription factors prime cis-regulatory elements required for
macrophage and b cell identities. Molecular Cell, 38(4):576–589, 2010.
Gerald Z Hertz and Gary D Stormo. Identifying dna and protein patterns with statistically
significant alignments of multiple sequences. Bioinformatics, 15(7-8):563–577, 1999.
Thomas A Hopf, John B Ingraham, Frank J Poelwijk, Carola P I Sch¨arfe, Michael Springer,
Chris Sander, and Debora S Marks. Mutation effects predicted from sequence co-variation.
| Nature | Biotechnology, |     | 35:128–135, |     | 2017. |     |     |
| ------ | -------------- | --- | ----------- | --- | ----- | --- | --- |
Andrej Karpathy. autoresearch: Ai agents running research on single-gpu nanochat training
automatically. https://github.com/karpathy/autoresearch, 2025.
Thomas S Kuhn. The Structure of Scientific Revolutions. University of Chicago Press, 1962.
Yongchan Kwon et al. Enhancing protein immunogenicity prediction via uncertainty weighted
| deep | ensemble. | Oxford | Open | Immunology, |     | 7(1):iqag008, | 2026. |
| ---- | --------- | ------ | ---- | ----------- | --- | ------------- | ----- |
Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and scalable pre-
dictive uncertainty estimation using deep ensembles. In Advances in Neural Information
| Processing | Systems, |     | volume | 30, | 2017. |     |     |
| ---------- | -------- | --- | ------ | --- | ----- | --- | --- |
Robert Tjarko Lange, Yuki Imajuku, and Edoardo Cetin. Shinkaevolve: Towards open-ended
and sample-efficient program evolution. arXiv preprint arXiv:2509.19349, 2025.
36

Charles E Lawrence, Stephen F Altschul, Mark S Boguski, Jun S Liu, Andrew F Neuwald, and
John C Wootton. Detecting subtle sequence signals: A Gibbs sampling strategy for multiple
| alignment. | Science, | 262(5131):208–214, |     |     | 1993. |     |     |
| ---------- | -------- | ------------------ | --- | --- | ----- | --- | --- |
Binglan Li, Anil Kumar Saini, and Jason H Moore. Agentic ai and the rise of in silico team
science in biomedical research. Nature Biotechnology, 44:711–725, 2026.
Zhengchangsu Li, Sheng Chen, Shiguo Liu, and Ling Chen. Prosampler: a new fast and effi-
cient sample-based de novo motif discovery tool with motif pair and cooperation detection.
| Bioinformatics, |     | 35(22):4632–4639, |     | 2019. |     |     |     |
| --------------- | --- | ----------------- | --- | ----- | --- | --- | --- |
Zeming Lin, Roshan Akinwande, Eric Gao, et al. Evolutionary-scale prediction of atomic-level
protein structure with a language model. Science, 379(6637):1123–1130, 2023.
FeiLiu,TongXialiang,MingxuanYuan,XiLin,FuLuo,ZhenkunWang,ZhichaoLu,andQingfu
Zhang. Evolution of heuristics: Towards efficient automatic algorithm design using large
language model. In Proceedings of the 41st International Conference on Machine Learning,
2024.
C´elineMarquet,JuliusSchlensok,MarinaAbakarova,BurkhardRost,andElodieLaine. Expert-
guided protein language models enable accurate and blazingly fast fitness prediction. Bioin-
| formatics, | 40(11):btae621, |     | 2024. |     |     |     |     |
| ---------- | --------------- | --- | ----- | --- | --- | --- | --- |
Pascal Notin and Deborah S. Marks. Have we hit the scaling wall for protein language models?
Substack (proteingym.org), 2025. ProteinGym v1.3 release with 90+ baseline models.
Pascal Notin et al. Proteingym: Large-scale benchmarks for protein fitness prediction and
design. In Advances in Neural Information Processing Systems, 2023. NeurIPS Datasets and
Benchmarks.
AlexanderNovikovetal. Alphaevolve: Acodingagentforscientificdiscoveryusingevolutionary
| algorithms. | arXiv | preprint | arXiv:2506.13131, |     |     | 2025. |     |
| ----------- | ----- | -------- | ----------------- | --- | --- | ----- | --- |
Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog,
M Pawan Kumar, Emilien Dupont, Francisco J R Ruiz, Jordan S Ellenberg, Pengming Wang,
Omar Fawzi, Pushmeet Kohli, and Alhussein Fawzi. Mathematical discoveries from program
search with large language models. Nature, 625(7995):468–475, 2024.
Jiarui Su, Yibin Yang, Jiangjiang Zhang, et al. Protein representation learning by geometric
| structure | and | sequence. | Nature | Communications, |     | 14(1):5742, | 2023. |
| --------- | --- | --------- | ------ | --------------- | --- | ----------- | ----- |
Yang Tan et al. Rank-and-reason: Multi-agent collaboration accelerates zero-shot protein mu-
| tation | prediction. | arXiv | preprint | arXiv:2602.00197, |     | 2026. |     |
| ------ | ----------- | ----- | -------- | ----------------- | --- | ----- | --- |
Sixue Xing, Haoyu He, Kerui Wu, Zhuo Yang, Haozheng Luo, Tianfan Fu, and Aarthy Nagara-
jan. Compute allocation in evolutionary search: From depth–breadth to multi-armed bandits.
| In arXiv | preprint | arXiv:2605.29268, |     |     | 2026. |     |     |
| -------- | -------- | ----------------- | --- | --- | ----- | --- | --- |
Harry Zhang, Kayla M Yang, Yifan Chang, Fan Ding, et al. Machine learning-guided co-
optimization of fitness and diversity facilitates combinatorial library design in enzyme engi-
| neering. | Nature | Communications, |     | 15(1):6355, |     | 2024. |     |
| -------- | ------ | --------------- | --- | ----------- | --- | ----- | --- |
Xiaojin Zhu. Semi-supervised learning literature survey. In Technical Report, University of
| Wisconsin-Madison, |     | 2002. |     |     |     |     |     |
| ------------------ | --- | ----- | --- | --- | --- | --- | --- |
37

| Supplementary |     |        | Material |     |     |     |     |     |     |
| ------------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
| Section       | A:  | Per-TF | Results  |     |     |     |     |     |     |
Per-TFAUROCvaluesforall132transcriptionfactorsareprovidedintheaccompanyingbench-
markdatafiles(benchmark data/shuffled negatives 132tf.csvandbenchmark data/genomic negatives 132tf.csv).
| Section | B:         | TOMTOM      |          | Match      | Analysis |          |                 |               |     |
| ------- | ---------- | ----------- | -------- | ---------- | -------- | -------- | --------------- | ------------- | --- |
| TOMTOM  | comparison |             | against  | JASPAR     | 2026     | Core     | (2,633 motifs): |               |     |
|         |            | Table       | 11:      | TOMTOM     | JASPAR   | match    | rates           | (n = 53 TFs). |     |
|         |            | Metric      |          |            |          |          | DALE            | STREME        |     |
|         |            | Top-1       | strict   | (q <0.001, | ≥70%     | overlap) | 23 (50.0%)      | 31 (62.0%)    |     |
|         |            | Top-1       | moderate | (q         | <0.05)   |          | 40 (87.0%)      | 45 (90.0%)    |     |
|         |            | Top-5       | strict   |            |          |          | 29 (63.0%)      | 37 (74.0%)    |     |
|         |            | Top-5       | moderate | (q         | <0.05)   |          | 46 (100%)       | 50 (100%)     |     |
|         |            | No          | match    | at all     |          |          |                 | 6             | 5   |
| Section | C:         | Compilation |          | Fairness   |          |          |                 |               |     |
STREME prebuilt binary vs. source-compiled (-O2) across 23 TFs: ratio 1.00× (identical per-
| formance). | Both | compiled        |     | with GCC | on Ubuntu | 24.04. |     |     |     |
| ---------- | ---- | --------------- | --- | -------- | --------- | ------ | --- | --- | --- |
| Section    | D:   | Reproducibility |     |          |           |        |     |     |     |
All benchmark data, the DALE binary, and a Jupyter notebook reproducing all motif discovery
figuresandstatisticsareavailableathttps://github.com/travis42/little-scientist-dale.
The Delta V ensemble strategy, evaluation pipeline, and archived search history (all iterations)
are available at https://github.com/travis42/little-scientist-delta-v. Both reposito-
ries include reproducible benchmark scripts and are released under the Apache 2.0 license.
38
---- END DOCUMENT ----
