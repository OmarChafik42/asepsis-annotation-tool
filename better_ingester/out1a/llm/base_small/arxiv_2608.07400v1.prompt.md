Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
FinRank: An Evidence-Grounded Benchmark for Financial Question
Answering and Retrieval over SEC Filings
Sasan Mansouri∗1, Daniel Saad2, Mark Wahrenburg2, Manu Weissel2,3, and Fabian Woebbeking4
1University of Groningen, Groningen, Netherlands
2Goethe University Frankfurt, Frankfurt am Main, Germany
3DataNXT GmbH, Frankfurt am Main, Germany
4Halle Institute for Economic Research (IWH) and Martin Luther University Halle-Wittenberg, Halle (Saale), Germany
Abstract
document corpora (Lewis et al., 2020; Karpukhin et al.,
2020), financial document question answering presents a
Financial question answering is typically evaluated by fundamentalchallengedistinctfromopen-domainsettings:
answer correctness, yet in SEC filings a plausible and regulatory disclosures are heavily templated. Standard-
even numerically correct answer can be grounded in the ized accounting conventions, risk-factor disclosures, and
wrong evidence. Similar facts and disclosures recur across revenue-recognition notes read almost identically across
sections of a filing, across reporting periods of the same competing firms and reporting periods. Consequently,
firm, and across comparable firms. FinRank targets the primary bottleneck in automated financial analysis
this provenance-sensitive retrieval problem by requiring is rarely answer composition, but evidence discrimina-
systems to identify evidence for the intended entity, re- tion—distinguishingthetargetfirm’sdisclosurefromplau-
porting period, and disclosure context. The benchmark sibledistractors,suchasacompetitor’snear-identicalboil-
contains 1185 manually authored question–answer records erplate or a prior period’s filing. For an analyst, auditor,
over the 10-K and 10-Q filings of 22 companies. Each or compliance reviewer, an ungrounded or misattributed
record includes a reference answer, gold supporting pas- answer carries limited practical utility and introduces se-
sages, and hand-curated hard negatives drawn from con- vere operational risk; yet existing financial benchmarks
fusable passages within filings, across reporting periods, (Z. Chen, W. Chen, et al., 2021; Zhu et al., 2021; Reddy
and across comparable firms. FinRank evaluates passage et al., 2024) focus primarily on numerical calculation over
retrieval, reranking, and hard-negative discrimination as provided snippets or end-to-end correctness, failing to
separately measured tasks. Baseline results demonstrate isolate evidence retrieval and hard-negative suppression.
thedifficultyofthissetting: amongtheevaluatedsystems, Beyond boilerplate templating, document length and
even a 7B instruction-tuned embedder reaches only 44.8%
structuralcomplexityposeadditionalhurdles. Asingle10-
Recall@10 on the pooled evidence corpus; sub-billion-
Kfilingfrequentlyspanshundredsofpagesofdenseprose,
parameter encoders gain at most 3.5 points over BM25,
financial tables, and footnotes, mixing accounting, legal,
a finance-adapted embedder trails BM25 by 9.7 points,
and forward-looking language that requires domain exper-
andpairwiseaccuracyfallsby13.0–20.5percentagepoints
tise to interpret. Furthermore, answers frequently depend
whenrandomnegativesarereplacedwiththecuratedhard
on evidence spread across non-adjacent tables, footnotes,
negatives. FinRank provides an evidence-first benchmark
and narrative sections rather than a single paragraph.
for developing financial question answering systems that
General-domain QA benchmarks (e.g., Rajpurkar et al.,
are not only accurate but also grounded in the correct
2016; Kwiatkowski et al., 2019), by contrast, treat sup-
disclosure.
portingevidenceasasecondaryannotation—invertingthe
requirements of financial domain QA, where an answer’s
validity depends on strict provenance to its underlying
1 Introduction
disclosure.
Toaddressthesechallenges,weintroduceFinRank,an
Financial disclosures submitted to the U.S. Securities
evidence-groundedbenchmarkconsistingof1185question–
and Exchange Commission (SEC), such as Form 10-K
answer records manually authored over the 10-K and
and 10-Q filings, serve as the primary source of truth for
10-Q filings of 22 companies across three sectors (phar-
corporate financial analysis, auditing, and regulatory com-
maceuticals, oil and gas, and automotive) covering filing
pliance (Wu et al., 2023; Islam et al., 2023). While recent
years 2024–2025. Each record pairs a question and ref-
advances in retrieval-augmented generation (RAG) have
erence answer with gold supporting passages, filing and
enabled large language models (LLMs) to query extensive
question-level metadata (topic, difficulty, reasoning type,
∗Correspondingauthor: s.mansouri@rug.nl evidence scope), and a hand-curated set of hard-negative
1
6202
guA
7
]IA.sc[
1v00470.8062:viXra

passages drawn from comparable filings. In a realistic and proactive-conversational reasoning. In all of these
analyst workflow, a model must identify the passages that the supporting context is supplied, so retrieval is not eval-
actually support an answer, distinguish them from plausi- uated. A second line makes retrieval part of the task:
ble distractors, and produce a faithful response; FinRank FinanceBench (Islam et al., 2023) scores open-book an-
evaluates the ranking and discrimination steps directly, swer correctness over whole filings; DocFinQA (Reddy et
over a curated passage pool. Its construction criteria al., 2024) lengthens FinQA to full-document context; Fin-
(Section 3.2; Appendix A) jointly control topic coverage, TextQA (J. Chen et al., 2024) and T2-RAGBench (Strich
qualitative versus quantitative reasoning, complexity, ev- et al., 2026) benchmark end-to-end RAG over financial
idence scope, and sub-question decomposition, thereby prose and tables; and FinDER (Choi et al., 2025) con-
ensuringthatthebenchmarkevaluatesfinancialreasoning tributes expert-written, abbreviation-heavy queries with
and hard-negative discrimination rather than superficial annotated evidence, scored with RAGAS-style metrics
lexical matching alone. FinRank is designed specifically (Es et al., 2024). The most recent entries extend the set-
for retrieval-grounded financial QA over selected SEC ting further still, to agentic document- and chunk-ranking
filings; its scope is defined by the included corporate dis- (Choi, Kwon, et al., 2025), multimodal visual citation (S.
closures, and it is not intended for generating automated Zhao et al., 2025), and analyst-workflow evaluation across
investment advice, valuations, or trading signals. within-disclosure, cross-entity, and longitudinal pathways
Insummary,ourcontributionsarefourfold. First,were- (Jiang et al., 2026). FinDER itself originated as the name-
leaseFinRank1 as,toourknowledge,thefirstfinancialQA sake task of the ICAIF’24 FinanceRAG Challenge (Choi,
benchmark to release a dedicated set of human-selected, Sohn, et al., 2024), which unified seven of these datasets
semantically confusable hard negatives for each question, into a single NDCG@10 retrieval leaderboard. Beyond
enabling direct comparison of discrimination against cu- document-centric RAG, recent work explores bypassing
rated versus random distractors, complementing resources retrieval altogether by giving models direct access to cu-
that focus on realistic queries (Choi et al., 2025) or open- rated vendor data through the Model Context Protocol,
book correctness (Islam et al., 2023) without releasing which is effective for quantitative financial QA but weaker
gold hard negatives. Second, we provide rich, stratifi- on qualitative questions (Mansouri et al., 2026); FinRank
able annotations across four axes (document type, reason- targets the retrieval-based setting that remains necessary
ing type, evidence scope, and difficulty) alongside gold when answers must be grounded in the filings themselves
sub-question decompositions (query rewrite) for 69% of rather than a pre-structured data feed.
records, enabling performance to be disaggregated along
Acrossthisbodyofwork, evidenceannotationidentifies
fine-grained dimensions obscured by aggregate metrics.
whatisrelevant—asgoldpassagesor,inFinAgentBench’s
Third, we establish reference retrieval and reranking base-
case, graded chunk relevance — but no benchmark ships,
linesspanningsparse(TF-IDF,BM25),dense(bi-encoder),
per question, a dedicated set of human-selected, seman-
and cross-encoder architectures, demonstrating through
tically confusable hard-negative passages against which
hard-versus-random negative contrasts that curated dis-
discrimination can be scored directly against random dis-
tractors degrade model accuracy by 13.0–20.5 percentage
tractors. FinRank fills exactly this gap (Table 1). Each
points. Fourth,wesupporttransparency,auditability,and
question carries gold supporting passages and human-
extensibility through documented construction criteria,
selecteddistractorsfromcomparablefilings, togetherwith
a deterministic label-normalization and repair pipeline
difficulty, reasoning-type, and evidence-scope metadata
with a machine-readable change log, per-passage identi-
and,for69%ofrecords,agoldsub-questiondecomposition,
fiers and text hashes, a hard-negative taxonomy, and a
so that retrieval, reranking, and hard-negative discrimina-
target-versus-realized distributional audit.
tion become separately measurable. The nearest resource
with curated hard negatives, DocReRank (Wasserman
et al., 2025), generates hard-negative queries to train
2 Related Work
page-image rerankers, and is neither a QA benchmark nor
passage-level. Concurrent method-side work reaches the
2.1 Financial QA and RAG Benchmarks
same diagnosis from the systems direction: FinCARDS
(Zhou et al., 2026) recasts financial evidence selection as
Early financial QA benchmarks target numerical reason-
constraintsatisfactionoverentities, metrics, fiscalperiods,
ing over a provided context. FinQA (Z. Chen, W. Chen,
and numeric spans, reranking within-filing BM25 candi-
et al., 2021) pairs questions with executable reasoning
dates on FinAgentBench (Choi, Kwon, et al., 2025) and
programs over S&P 500 earnings-report excerpts; TAT-
reporting lexical retrieval to be vulnerable to numeric
QA (Zhu et al., 2021) covers hybrid table–text reasoning;
drift, temporal misalignment, and boilerplate repetition.
ConvFinQA (Z. Chen, Li, et al., 2022) extends FinQA
FinCARDS contributes a method and releases code but
to multi-turn dialogue; and MultiHiertt (Y. Zhao et al.,
no evaluation data or negatives, and confines itself to
2022) and PACIFIC (Deng et al., 2022) push multi-table
intra-document retrieval within a single filing, noting that
1Dataset,evaluationharness,repairlog,andhard-negativetax- its effectiveness across multiple documents remains un-
onomy: https://github.com/datanxt/FinRank evaluated. FinRank is complementary on both counts: it
2

supplies the annotated positives and curated distractors 3.2 Question-Generation Criteria
that such constraint-aware rerankers are scored against,
The annotators worked from a shared criteria document
anditshardnegativesaredrawnpredominantlyfromother
that fixes what a well-formed FinRank record must con-
filings, targeting precisely the cross-document setting left
tain; we summarize it here and reproduce it in full in
open there.
Appendix A. The criteria define the unit of evidence (a
passage: a self-contained span of filing text), separate
2.2 Retrieval, Reranking, and Hard Neg- qualitative reasoning (interpretation and judgment) from
atives quantitative reasoning (numerical computation, itself split
into metrics-generated, single-step, and compositional cal-
BM25 (Robertson and Zaragoza, 2009) remains a strong culations), and require, for medium- and hard-difficulty
sparse baseline; dense retrievers (Karpukhin et al., 2020; questions,aquery rewritethatdecomposesthequestion
Reimers and Gurevych, 2019; Izacard et al., 2022) and into an ordered sequence of atomic sub-questions.
cross-encoderrerankers(NogueiraandCho,2019)formthe
Coverage is controlled along three axes with explicit
standardtwo-stagepipelineevaluatedbygeneralIRbench-
targets. Topic: questions span eight filing-relevant do-
marks such as BEIR (Thakur et al., 2021) and MTEB
mains (Company Overview, Financials, Footnotes, Gover-
(Muennighoff et al., 2023), with FinMTEB (Tang and
nance, Accounting, Legal, Risk, and Shareholder Return),
Yang, 2025) the financial counterpart. A long line of work
each mapped to a distinct set of 10-K/10-Q disclosure
shows that hard negatives (not random in-batch ones) are
items. Complexity: a 30%/40%/30% Easy/Medium/Hard
what most improve dense retrievers (Xiong et al., 2021;
split, where Easy questions are direct factual lookups,
Qu et al., 2021; Zhan et al., 2021). FinRank carries this
Medium questions require comparison or trend analysis
insight to the evaluation side: rather than mining hard
across sections, and Hard questions require multi-section
negatives to train a retriever, it releases human-curated
synthesis. Evidence scope: a 40%/30%/30% single-/two-
hardnegativesasafixedbenchmarkassetandreportshow
/multi-passage split, so the benchmark is not dominated
much they degrade ranking relative to random distractors
by single-paragraph lookups. The criteria additionally in-
(Section 7).
struct annotators to balance qualitative and quantitative
questions. Section 4.2 reports how closely the released
2.3 Attribution and Faithfulness dataset meets each target.
Fixing these criteria ex ante is what lets FinRank test
Retrieval-augmented generation (Lewis et al., 2020) can more than surface lexical matching: a system must locate
still hallucinate or misattribute, motivating metrics for the disclosure passages that support the reasoning type a
citation quality (Gao et al., 2023), reference-free RAG question demands, not merely passages that share its vo-
evaluation (Es et al., 2024), and atomic factual precision cabulary, and, for multi-passage questions, must integrate
(Min et al., 2023). These score generated text; FinRank evidence spread across non-adjacent filing sections.
is complementary, measuring the retrieval and reranking
stepsupstreamthroughgold-versus-hard-negativepassage
3.3 Record Schema
labels, so that evidence attribution can be assessed before
generation is introduced.
The dataset is distributed as a single .jsonl file, one
JSON object per line. Each record is flat at the
top level, with the question, reference answer, optional
3 Dataset Construction
query rewrite array, question- and filing-level metadata,
and two nested arrays: passages (supporting passages,
3.1 Sources and Design Principles
each with text and page number) and hard negatives
(each additionally tagged with its originating ticker,
FinRankaggregates1185records,eachgroundedina10-K
year, and doc type). The full field-by-field schema is
(annual) or 10-Q (quarterly) filing submitted to the SEC.
given in Appendix B.
The records were collected by trained annotators, each
responsible for roughly 250 records, whose assignments
together span the pharmaceutical, oil-and-gas, and auto- 3.4 Supporting Passages and Hard Nega-
motive sectors (Section 3.5). The benchmark is organized tives
around four principles: examples are grounded in pri-
mary disclosures rather than secondary summaries; every Thepassagesarraycontainsthepassagesfromtheunder-
question is paired with supporting passages for evidence- lying SEC filing that support the reference answer, each
based evaluation; hard negatives are included to support withatextfieldandapage numberfield; somequestions
retrieval and reranking; and metadata exposes variation are answered by a single passage, others require evidence
across sector, topic, reasoning type, filing year, and docu- drawn from multiple parts of the same filing. Support-
ment type, so that performance can be analyzed beyond ing passages thus play two roles: they are ground-truth
aggregate scores. retrieval targets, and they constrain answer generation
3

Benchmark Sourcedocuments #Records Retrieval Hardneg. Reranking Richmetadata
FinQA(Z.Chen,W.Chen,etal.,2021) Earningsreports(S&P500) 8,281 – – – –
TAT-QA(Zhuetal.,2021) Reporttable/textsnippets 16,552 – – – –
ConvFinQA(Z.Chen,Li,etal.,2022) Earningsreports(dialogue) 14,115 – – – –
FinanceBench(Islametal.,2023) 10-K/10-Q/8-K/earnings 10,231† partial – – sector
DocFinQA(Reddyetal.,2024) Full10-Kdocuments 7,437 yes – – –
FinDER(Choietal.,2025) 10-K(S&P500) 5,703 yes – yes‡ topic
FinAgentBench(Choi,Kwon,etal.,2025) 10-K/10-Q/8-K,calls,DEF-14A 26,000§ yes – yes§ –
FinRank (ours) 10-K/10-Q 1185 yes yes yes full
Table 1: FinRank against representative financial QA and retrieval benchmarks. “Hard neg.” denotes per-question
curated hard-negative passages; “Reranking” a gold-vs.-hard-negative reranking task; “Rich metadata” per-record
difficulty, reasoning-type, and evidence-scope labels. †150 questions are open-sourced. ‡FinDER evaluates LLM
reranking of retrieved passages but releases no curated hard-negative candidate set. §FinAgentBench provides 26K
graded-relevance annotations for document- and chunk-ranking, without a per-question curated hard-negative set. To
our knowledge, FinRank is the first financial QA benchmark to release per-question curated hard negatives and to
score discrimination against curated versus random distractors directly.
by providing the evidence to which a faithful generator comparable filings, most often a competitor in the same
should be grounded. sector, and otherwise the same company in a different
Each entry in hard negatives additionally records the reporting period or filing type. Because hard negatives
originating filing’s ticker, year, and doc type, so dis- were chosen by a human reader searching for the most
tractors may come from another company, another year, confusable evidence rather than sampled by a retrieval
oradifferentfilingtypethanthesupportingevidence. We heuristic,theyconcentrateinthe“sameindustry,different
treathardnegativesasafirst-classbenchmarkassetrather company” bucket that dominates Figure 1. This distribu-
than as optional augmentation: the dataset is intended tion is a deliberate annotation choice, and it is precisely
forexplicitcomparisonofretrieversandrerankersontheir the configuration that most often confuses lexical and
ability to suppress these distractors. embedding-based retrievers (Section 7).
During collection the authors performed a sampled re-
view of each student’s records and returned corrective
3.5 Data Collection
feedback, so that systematic misreadings of the criteria
couldbecaughtbeforerelease. Thisreviewwasappliedto
FinRank was collected by five business students, each
asampleratherthanexhaustively,andwedidnotcompute
independently responsible for a set of companies within
a formal inter-annotator-agreement statistic; both points
oneofthethreesectors,togetherspanningthepharmaceu-
are recorded as limitations in Section 9. After collection
tical, oil-and-gas, and automotive sectors. All annotators
we applied a single deterministic normalization pass (Sec-
worked from a shared question-generation criteria
tion3.8;AppendixC)thatharmonizeslabelsurfaceforms,
document (Section 3.2; reproduced in Appendix A) that
recovers the small number of placeholder values determin-
fixes the topic taxonomy, the qualitative and quantitative
istically from the structured question id, and repairs
reasoning categories, the complexity-level split, the
transposed hard-negative metadata, preserving every raw
passage-coverage split, and the query-rewrite rules.
value in a parallel <field> raw field.
Every record was authored manually: students read the
underlying 10-K and 10-Q filings directly and wrote each
question, its reference answer, and, for medium- and 3.6 Retrieval Corpus Definitions
hard-difficulty questions, the query rewrite decompo-
TomakeretrievalandrerankingresultsonFinRankrepro-
sition into sub-questions by hand. No language model
ducible, we specify two evaluation regimes that are both
was used to generate questions, answers, or rewrites;
reproducible from the JSONL alone, with no additional
the templated question id strings (for example, JNJ
corpus required.
CompanyOverview Hard MultiPassage Quantitative
03) are the naming convention students followed from
the criteria document, not an artifact of automated Global pooled corpus C. C is the union of every
generation. non-empty supporting-passage text and hard-negative
Evidence was assembled by hand as well. For each text appearing anywhere in FinRank, deduplicated on
question the responsible student located the supporting the raw passage text. Each entry is tagged with the
passage or passages in the source filing and transcribed (ticker, year, doc type, page number) metadata of
them into the passages array with their page references. thefirstrecordinwhichitappeared. Forthereleasedsplit,
The student then selected the record’s hard negatives |C|=5230uniquepassagesdrawnfrom1185records,with
manually, drawing plausible-but-incorrect passages from on average 1.96 supporting passages and 5.08 hard nega-
4

| tives per | record. | First-stage |     | retrieval | baselines | (Section |     | 7)  |     |     |     |     |     |     |     |
| --------- | ------- | ----------- | --- | --------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
79.9%
| rank all    | of C for | each    | query | and        | report | Recall@k,  | MRR, | Same industry,    |     |     |     |     |     |           |     |
| ----------- | -------- | ------- | ----- | ---------- | ------ | ---------- | ---- | ----------------- | --- | --- | --- | --- | --- | --------- | --- |
|             |          |         |       |            |        |            |      | different company |     |     |     |     |     | n = 4,835 |     |
| and nDCG@10 |          | against | the   | per-record | gold   | positives. | We   |                   |     |     |     |     |     |           |     |
emphasize what this regime is: because C consists solely Same company, 13.2%
|                       |     |     |           |     |         |              |     | different year/form |     | n = 796 |     |     |     |     |     |
| --------------------- | --- | --- | --------- | --- | ------- | ------------ | --- | ------------------- | --- | ------- | --- | --- | --- | --- | --- |
| of annotator-selected |     |     | positives | and | curated | distractors, |     | re-                 |     |         |     |     |     |     |     |
trieval over C is a curated passage-ranking stress test with Same company, 6.9%
same year & form
n = 420
| an elevated | density |     | of confusable |     | passages, | not | retrieval |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | ------------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
through the complete text of each filing. Scores on C are Cross-industry <0.1%
n = 1
| therefore | not | comparable |     | to full-document |     | retrieval | set- |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | ---------------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
% of hard negatives  (N = 6,052)
| tings, and | extending |             | FinRank  | with | exhaustive |     | filing-level |              |          |     |                 |           |             |        |        |
| ---------- | --------- | ----------- | -------- | ---- | ---------- | --- | ------------ | ------------ | -------- | --- | --------------- | --------- | ----------- | ------ | ------ |
| chunks     | is left   | to a future | release. |      |            |     |              |              |          |     |                 |           |             |        |        |
|            |           |             |          |      |            |     |              | Figure 1:    | Taxonomy |     | of the          | 6021 hard | negatives,  |        | by the |
|            |           |             |          |      |            |     |              | relationship | between  |     | each negative’s |           | originating | filing | and    |
In-record candidate set L . For each record r, its source record. A hard negative is most often a passage
r
L = G ∪ HN is the union of r’s supporting pas- from a competitor’s filing of comparable type and period,
| r   | r   | r   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sages and its hard negatives. Reranking and hard- theconfigurationretrieversaremostlikelytoconfusewith
| negative-discrimination |             |           | evaluations |         | are      | restricted | to L      | r true evidence. |            |         |     |            |       |        |         |
| ----------------------- | ----------- | --------- | ----------- | ------- | -------- | ---------- | --------- | ---------------- | ---------- | ------- | --- | ---------- | ----- | ------ | ------- |
| and report              | MRR,        | nDCG@5,   |             | and     | pairwise | accuracy   | on        |                  |            |         |     |            |       |        |         |
| (positive,hard          |             | negative) | pairs.      | This    | isolates | ranking    | qual-     |                  |            |         |     |            |       |        |         |
|                         |             |           |             |         |          |            |           | inline in        | a parallel | <field> |     | raw field, | every | change | is enu- |
| ity from                | first-stage | recall    | and         | matches | how      | hard       | negatives |                  |            |         |     |            |       |        |         |
are intended to be used (Section 3.4). merated in the released machine-readable repair log, and
|                |                                              |          |              |        |       |        |           | all distributional |     | statistics |     | in this paper | are | reported | on  |
| -------------- | -------------------------------------------- | -------- | ------------ | ------ | ----- | ------ | --------- | ------------------ | --- | ---------- | --- | ------------- | --- | -------- | --- |
| Studies        | using                                        | FinRank  |              | should | state | which  | regime    | is                 |     |            |     |               |     |          |     |
|                |                                              |          |              |        |       |        |           | the canonical      |     | labels.    |     |               |     |          |     |
| being reported |                                              | for each | metric,      | and    | any   | corpus | extension |                    |     |            |     |               |     |          |     |
| beyondC        | (forexample,alargerfiling-derivedpool)should |          |              |        |       |        |           |                    |     |            |     |               |     |          |     |
| be released    | alongside                                    |          | the results. |        |       |        |           | 4 Dataset          |     | Analysis   |     |               |     |          |     |
3.7 Hard-Negative Construction Taxon- We summarize the composition of FinRank on the canoni-
| omy |     |     |     |     |     |     |     | calnormalizedlabels(Section3.8),verifieddirectlyagainst |                |     |     |        |         |     |           |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | -------------- | --- | --- | ------ | ------- | --- | --------- |
|     |     |     |     |     |     |     |     | the released                                            | FinRank.jsonl. |     |     | Figure | 2 gives | the | full pic- |
Each hard negative carries the (ticker, year, ture along six axes; per-field distribution tables and the
type)ofitsoriginatingfiling,socomparingitagainst
| doc |     |     |     |     |     |     |     | raw-vs.-normalized |     | counts | are | provided | in Appendix |     | C.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | --- | -------- | ----------- | --- | --- |
the source record yields the four-bucket taxonomy in The 1185 records come from 22 companies in three
| Figure | 1. Because |     | negatives |     | were selected |     | by hand |          |                 |     |      |           |     |         |        |
| ------ | ---------- | --- | --------- | --- | ------------- | --- | ------- | -------- | --------------- | --- | ---- | --------- | --- | ------- | ------ |
|        |            |     |           |     |               |     |         | sectors: | pharmaceuticals |     | (499 | records), | oil | and gas | (438), |
(Section 3.5), 80% fall in the “same industry, different and automotive (248), with per-company counts ranging
company” bucket: a competitor’s filing of comparable from9(XOM)to142(JNJ).Difficultyfollowstheintended
| type and | period, | the | case | retrievers | are | most | likely | to  |     |     |     |     |     |     |     |
| -------- | ------- | --- | ---- | ---------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
30/40/30Easy/Medium/Hardsplit(Figure2b),andtopics
confuse with true evidence. A byte-equal audit identified are close to uniform (Figure 2f). Three axes are markedly
| 11 hard | negatives | that | duplicated |     | a supporting |     | passage |         |        |         |      |      |              |     |      |
| ------- | --------- | ---- | ---------- | --- | ------------ | --- | ------- | ------- | ------ | ------- | ---- | ---- | ------------ | --- | ---- |
|         |           |      |            |     |              |     |         | skewed: | 88% of | records | come | from | 10-K filings | and | only |
of their own record; these, together with one degenerate 12%from10-Qs;75%offilingsarefrom2025and25%from
entry, are removed from the release. The remaining 2024; and qualitative questions outnumber quantitative
| 442 hard | negatives | (∼7.3%) |     | coincide | with | a supporting |     |              |     |        |      |           |          |     |          |
| -------- | --------- | ------- | --- | -------- | ---- | ------------ | --- | ------------ | --- | ------ | ---- | --------- | -------- | --- | -------- |
|          |           |         |     |          |      |              |     | ones roughly | two | to one | (68% | vs. 32%). | Evidence |     | scope is |
passage of a different record, where the passage may spreadacrosssingle-(34%),two-(40%),andmulti-passage
legitimately be relevant to more than one question. We (26%) records, so roughly two thirds of the benchmark
release hn taxonomy.json so that users of hard-negative require integrating evidence from more than one part of a
| metrics | can filter | these | overlaps. |     |     |     |     | filing. |       |      |                |     |         |            |     |
| ------- | ---------- | ----- | --------- | --- | --- | --- | --- | ------- | ----- | ---- | -------------- | --- | ------- | ---------- | --- |
|         |            |       |           |     |     |     |     | These   | skews | mean | that aggregate |     | metrics | on FinRank |     |
3.8 Official Label Set and Normalization primarily reflect performance on the dominant strata (10-
|         |            |     |              |     |         |         |       | K, 2025,       | qualitative, |      | pharma    | and oil-and-gas).     |     | We  | there- |
| ------- | ---------- | --- | ------------ | --- | ------- | ------- | ----- | -------------- | ------------ | ---- | --------- | --------------------- | --- | --- | ------ |
| To make | evaluation |     | reproducible |     | without | forcing | every |                |              |      |           |                       |     |     |        |
|         |            |     |              |     |         |         |       | fore recommend |              | that | retrieval | and answer-generation |     |     | met-   |
consumer to re-derive the same mapping, the released rics be reported per stratum, by document type, filing
| FinRank.jsonl |     | carries | the | official | benchmark |     | labels: | a               |     |       |             |     |          |       |        |
| ------------- | --- | ------- | --- | -------- | --------- | --- | ------- | --------------- | --- | ----- | ----------- | --- | -------- | ----- | ------ |
|               |     |         |     |          |           |     |         | year, reasoning |     | type, | and sector, | in  | addition | to in | aggre- |
deterministic, idempotent curation pass (Appendix C) gate, and we note that the 2024 and 10-Q partitions are
title-cases difficulty, consolidates industry variants small and produce noisier per-stratum estimates.
| into three | sectors | with   | the        | oil-and-gas |            | sub-industry | sur-      |          |     |         |     |               |     |     |     |
| ---------- | ------- | ------ | ---------- | ----------- | ---------- | ------------ | --------- | -------- | --- | ------- | --- | ------------- | --- | --- | --- |
| faced in   | a new   | field, | unifies    | topic,      | passage    |              | type, and |          |     |         |     |               |     |     |     |
|            |         |        |            |             |            |              |           | 4.1 Data |     | Quality | and | Normalization |     |     |     |
| reasoning  | type    | typos, | reconciles |             | the Ford/F | ticker       | split,    |          |     |         |     |               |     |     |     |
and recovers literal placeholders from the structured The data as collected contains surface-level label inconsis-
question id. Every value the pass changed is preserved tencies (casing and spelling variants and a small number
5

|     |     | (a) Sector |     |     |     | (b) Difficulty |     |     |     | (c) Reasoning type |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | -------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
|     |     | 42%        |     |     |     |                | 41% |     |     |                    | 68% |     |     |     |
37%
|     |     | 499              |     |      |     |                   | 31% 484     |      |     |             | 809 |              |     |     |
| --- | --- | ---------------- | --- | ---- | --- | ----------------- | ----------- | ---- | --- | ----------- | --- | ------------ | --- | --- |
|     |     |                  | 438 |      |     |                   |             | 29%  |     |             |     |              |     |     |
|     |     |                  |     | 21%  |     |                   | 363         | 338  |     |             |     | 32%          |     |     |
|     |     |                  |     | 248  |     |                   |             |      |     |             |     | 376          |     |     |
|     |     | Pharma           | O&G | Auto |     |                   | Easy Medium | Hard |     | Qualitative |     | Quantitative |     |     |
|     |     | (d) Passage type |     |      |     | (e) Document type |             |      |     |             |     |              |     |     |
|     |     |                  | 40% |      |     |                   | 88%         |      |     | 1,185       |     |              |     |     |
35%
|     |     |     | 472 |     |     |     | 1,048 |     |     | records |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- |
|     |     | 409 |     | 26% |     |     |       |     |     |         |     |     |     |     |
304
22
|     |     |     |     |     |     |     |     | 12% |     | companies / 3 sectors |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
137
8
topics
|     |     | Single |     | Two Multi |     |     | 10-K | 10-Q |     |     |     |     |     |     |
| --- | --- | ------ | --- | --------- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
(f) Topic
|     | Accounting         |       |     |     |     |     |     |     |     |              | 158  (13.3%) |     |     |     |
| --- | ------------------ | ----- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | --- | --- |
|     | Company Overview   |       |     |     |     |     |     |     |     |              | 153  (12.9%) |     |     |     |
|     | Financials         |       |     |     |     |     |     |     |     |              | 152  (12.8%) |     |     |     |
|     |                    | Risk  |     |     |     |     |     |     |     |              | 150  (12.7%) |     |     |     |
|     |                    | Legal |     |     |     |     |     |     |     | 146  (12.3%) |              |     |     |     |
|     | Shareholder Return |       |     |     |     |     |     |     |     | 143  (12.1%) |              |     |     |     |
|     | Footnotes          |       |     |     |     |     |     |     |     | 142  (12.0%) |              |     |     |     |
|     | Governance         |       |     |     |     |     |     |     |     | 141  (11.9%) |              |     |     |     |
Figure 2: Composition of FinRank across the 1185 records: (a) sector, (b) difficulty, (c) reasoning type, (d) evidence
scope (passage type), (e) document type, and (f) topic. Counts are on the canonical normalized labels. The dataset is
deliberately near-uniform over topics (141–158 records each) but skewed along sector, document type, and reasoning
| type, skews | that motivate | stratified | reporting. |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of literal template placeholders) and, in ∼0.3% of hard- dataset (Table 2, on canonical normalized labels).
| negative | entries, transposed | metadata |     | fields. | A determin- |     |     |            |     |          |     |                 |         |     |
| -------- | ------------------- | -------- | --- | ------- | ----------- | --- | --- | ---------- | --- | -------- | --- | --------------- | ------- | --- |
|          |                     |          |     |         |             |     | The | complexity |     | split is | met | almost exactly. | Passage |     |
istic, idempotent curation pass (Section 3.8; Appendix C) coverage deviates more: two-passage records are over-
resolves these into the canonical labels of the released represented by about ten percentage points, drawn from
FinRank.jsonl; original values are preserved in parallel the single- and multi-passage buckets. Reasoning type is
<field> raw fields, every change is enumerated in the the largest departure from the criteria, at roughly two
| released | repair log; duplicate | passages |     | within | a record, |     |             |         |     |                  |     |      |          |     |
| -------- | --------------------- | -------- | --- | ------ | --------- | --- | ----------- | ------- | --- | ---------------- | --- | ---- | -------- | --- |
|          |                       |          |     |        |           |     | qualitative | records |     | per quantitative |     | one. | Appendix | H   |
degenerate hard negatives, and annotation-tool artifacts reports cross-tabulations showing that this qualitative
embedded in passage text are removed; and sixty-five skew is present at every difficulty level.
| records                    | are excluded    | from the     | release | entirely   | (reliance |      |                   |                |              |                 |                |           |                   |        |
| -------------------------- | --------------- | ------------ | ------- | ---------- | --------- | ---- | ----------------- | -------------- | ------------ | --------------- | -------------- | --------- | ----------------- | ------ |
| on a non-filing            | source,         | placeholder  | or      | synthetic  | content,  |      |                   |                |              |                 |                |           |                   |        |
| or duplicate               | question–answer | pairs),      | each    | enumerated |           | in   | 5 Tasks           |                |              |                 |                |           |                   |        |
| the repair                 | log. Records    | whose stored | labels  | disagree   |           | with |                   |                |              |                 |                |           |                   |        |
| their structured           | question        | id are       | flagged | in the     | repair    | log  |                   |                |              |                 |                |           |                   |        |
|                            |                 |              |         |            |           |      | FinRank           | supports       |              | five evaluation |                | tasks     | that mirror       | the    |
| for the audit              | discussed       | in Section   | 9.      |            |           |      |                   |                |              |                 |                |           |                   |        |
|                            |                 |              |         |            |           |      | stages            | of an          | analyst      | workflow        | over           | SEC       | filings: locating |        |
|                            |                 |              |         |            |           |      | candidate         | evidence       |              | (retrieval),    | distinguishing |           | it from           | plau-  |
|                            |                 |              |         |            |           |      | sible distractors |                | (reranking), |                 | integrating    |           | evidence          | across |
| 4.2 Methodology-to-Dataset |                 |              |         | Validation |           |      |                   |                |              |                 |                |           |                   |        |
|                            |                 |              |         |            |           |      | passages          | (multi-passage |              | reasoning),     |                | producing | an                | answer |
Because the question-generation criteria of Section 3.2 faithfultothatevidence(answergeneration),andmapping
specify explicit target distributions over difficulty, passage a colloquial query to a retrievable form (query rewriting).
coverage, and reasoning type, we can measure realized Retrieval tasks operate on the global pooled corpus C
deviations between the stated targets and the released defined in Section 3.6; reranking and hard-negative dis-
6

Dimension Target Realized Deviation
Complexity
Easy 30% 30.6% +0.6pp
Medium 40% 40.8% +0.8pp
Hard 30% 28.5% −1.5pp
Passage coverage
Single-passage 40% 34.5% −5.5pp
Two-passage 30% 39.8% +9.8pp
Multi-passage 30% 25.7% −4.3pp
Reasoning type (methodology calls for balance)
Qualitative balanced 68.3% skewed (∼2:1)
Quantitative balanced 31.7% skewed
Table 2: Target distributions mandated by the FinRank question-generation criteria (Section 3.2) against realized
values in the canonical normalized release. The 30/40/30 complexity target is met to within about one percentage
point per bucket; the 40/30/30 passage-coverage target deviates most, with two-passage records over-represented; and
reasoning type shows the largest gap, with qualitative records outnumbering quantitative ones roughly two to one.
Consumers should treat these realized values as the authoritative distribution and stratify results accordingly.
crimination operate on the per-record candidate set L dependencies and the reporting checklist we recommend
r
from the same section. Table 3 summarizes the inputs, for future studies.
outputs,suggestedmetrics,andpossiblebaselinesforeach
task.
6.1 Baselines
We run seven systems: TF-IDF (scikit-learn
Citation and attribution evaluation. Reranking
TfidfVectorizer, sublinear TF, cosine scoring);
with hard negatives extends naturally to RAG-style ci-
BM25 (rank-bm25 BM25Okapi, default parameters,
tation evaluation: a system that produces an answer to-
Robertson and Zaragoza, 2009); a dense retriever
gether with one or more cited passages can be scored on
(all-mpnet-base-v2, Reimers and Gurevych, 2019,
whether the cited passages overlap with the gold support-
cosine over L2-normalized embeddings); and a cross-
ingpassagesandwhethertheyavoidthehard-negativeset.
encoderreranker(ms-marco-MiniLM-L-6-v2,Nogueira
This is particularly relevant in financial settings where
and Cho, 2019), applied both over the top-20 dense
auditability of generated answers is a practical concern.
candidates from the global pool C and over the in-
record set L ; a stronger general-purpose embedder
r
Multi-passage records and the query rewrite
(bge-large-en-v1.5); a finance-adapted embed-
field. Records with passage type Two-Passage or
der (FinLang/finance-embeddings-investopedia);
Multi-Passage (Section 4) provide the substrate for the
and a 7B instruction-tuned embedder
multi-passage reasoning task. The query rewrite array,
(e5-mistral-7b-instruct, encoded per its refer-
where present, supplies reference reformulations that can
ence implementation), all under a uniform 512-token
be used as targets for the query-rewriting task or as para-
truncation. We additionally report a metadata-filtered
phrase inputs for retrieval-robustness analyses.
BM25 baseline: BM25 restricted to the corpus entries
whose (ticker, year, doc type) match the query
record’s source filing, quantifying the effect of metadata
6 Experimental Protocol and
pre-filtering before semantic ranking. Baselines left to
Baselines future work include an SEC-filing-adapted retriever, a
closed-book LLM, an open-book LLM with gold passages,
Wereportexecutedretrieval,reranking,andhard-negative and a full RAG pipeline (Lewis et al., 2020).
discriminationbaselinesusingdeterministic,publiclyavail-
able models; generative answer-quality evaluation is left
6.2 Splits and Ablations
to future work. All reported metrics are produced by
the released evaluation harness (baselines/) applied to The baselines here are computed over the entire
the released FinRank.jsonl and are exactly reproducible dataset as reference numbers. We additionally re-
from these artifacts. All baselines are evaluated on the lease five generalization splits as record-ID assign-
full 1185-record dataset using the canonical normalized ments (baselines/splits.json): random (948/118/119
labels, and we fix seed=42 for the only non-deterministic train/dev/test), held-out-ticker (910/140/135), leave-one-
component(random-negativesampling). AppendixGlists sector-out folds, year (test = 2024, 296 records), and
7

| Task |     | Inputs |     | Output |     |     | Metrics |     |     | Possible |     | baselines |     |     |
| ---- | --- | ------ | --- | ------ | --- | --- | ------- | --- | --- | -------- | --- | --------- | --- | --- |
Answer genera- Question; passages Natural-language EM,tokenF1,ROUGE-L, Closed-bookLLM;open-
tion (gold or retrieved) answer BERTScore, faithfulness book LLM; RAG
|     |     |     |     |     |     |     | vs. provided |     | passages |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
Passage retrieval Question; passage Ranked candidate Recall@k, MRR, TF-IDF, BM25 (Robert-
|     |     | corpus |     | passages |     |     | nDCG@k, | Hit | Rate | sonandZaragoza,2009); |            |     |          |      |
| --- | --- | ------ | --- | -------- | --- | --- | ------- | --- | ---- | --------------------- | ---------- | --- | -------- | ---- |
|     |     |        |     |          |     |     |         |     |      | DPR                   | (Karpukhin |     | et       | al., |
|     |     |        |     |          |     |     |         |     |      | 2020);                | SBERT      |     | (Reimers |      |
|     |     |        |     |          |     |     |         |     |      | and                   | Gurevych,  |     | 2019);   |      |
hybrid
Reranking with Question; in-record Ranking over the MRR, nDCG@k, pair- Cross-encoder rerankers
hard negatives positives and hard union wiseaccuracyon(positive, (Nogueira and Cho,
|     |     | negatives |     |     |     |     | hard | negative) | pairs | 2019) |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | ---- | --------- | ----- | ----- | --- | --- | --- | --- |
Multi-passage Question; multiple Answer integrat- EM, F1, ROUGE-L, Long-context LLMs;
reasoning supporting passages ingallrelevantpas- BERTScore, evidence multi-passage RAG;
|     |     |     |     | sages |     |     | coverage |     |     | question |     | decomposition |     |     |
| --- | --- | --- | --- | ----- | --- | --- | -------- | --- | --- | -------- | --- | ------------- | --- | --- |
Query rewriting Original question One or more refor- Semantic preservation LLM-based and
|     |     |     |     | mulations |     |     | (downstream |     | answer     | template-based |     |     | rewrit- |     |
| --- | --- | --- | --- | --------- | --- | --- | ----------- | --- | ---------- | -------------- | --- | --- | ------- | --- |
|     |     |     |     |           |     |     | agreement); |     | retrieval  | ers            |     |     |         |     |
|     |     |     |     |           |     |     | improvement |     | (Recall@k, |                |     |     |         |     |
MRR)
Table 3: Tasks supported by FinRank, with inputs, outputs, suggested evaluation metrics, and possible baselines.
document type (test = 10-Q, 137 records). We recom- queryrecord’sfilingeliminates92.9%ofthatrecord’shard
mendthat future studiesreport under atleastone, noting negativesandshrinksthepoolto≈173candidatesonaver-
that the year and 10-Q test partitions are small and yield age, lifting BM25 from 32.1 to 55.0 Recall@10 (MRR 23.8
noisierestimates. Westratifyresultsalongdocumenttype, → 41.9). Because pooled entries carry first-occurrence
reasoning type, passage type, and difficulty (Section 7), metadata (Section 3.6), the filter excludes at least one
andreporttwodesign-validatingcontrasts: aquery-rewrite gold passage for 33 records and every gold passage for
ablation (question alone vs. question concatenated with 2; occurrence-level source attribution is left to a future
its query rewrite sub-questions) and a hard-vs.-random release. Two readings follow. First, metadata filtering is
negative contrast that tests whether the released hard genuinely powerful, and deployed filing assistants should
negatives are in fact harder than arbitrary distractors. use it; results on FinRank’s unfiltered pool characterize
|     |     |     |     |     |     | the | complementary |     | regime | in  | which | filing | attribution | is  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | --- | ----- | ------ | ----------- | --- |
unavailableorunreliable(noisymetadata,cross-filingques-
7 Results
|               |            |                                |     |     |     | tions,        | multi-company |          | corpora).       |          | Second, | even        | under | this   |
| ------------- | ---------- | ------------------------------ | --- | --- | --- | ------------- | ------------- | -------- | --------------- | -------- | ------- | ----------- | ----- | ------ |
|               |            |                                |     |     |     | filter,       | nearly        | half     | of the gold     | evidence |         | is missed   | at    | k =10: |
| Theretrieval, | reranking, | andhard-negativediscrimination |     |     |     |               |               |          |                 |          |         |             |       |        |
|               |            |                                |     |     |     | within-filing |               | semantic | discrimination, |          |         | the setting |       | probed |
tablesbelowreportnumbersactuallyproducedbythebase-
|                                                 |     |                  |                  |       |           | by  | the same-filing |     | and same-company |            |     | hard | negatives, | is  |
| ----------------------------------------------- | --- | ---------------- | ---------------- | ----- | --------- | --- | --------------- | --- | ---------------- | ---------- | --- | ---- | ---------- | --- |
| linesofSection6.1ontheentire1185-recorddataset. |     |                  |                  |       | Num-      |     |                 |     |                  |            |     |      |            |     |
|                                                 |     |                  |                  |       |           | not | eliminated      |     | by metadata      | filtering. |     |      |            |     |
| bersareemittedbybaselines/make                  |     |                  | macros.pyfromthe |       |           |     |                 |     |                  |            |     |      |            |     |
| JSON output                                     | of  | the run scripts, | and any          | rerun | automati- |     |                 |     |                  |            |     |      |            |     |
cally refreshes them. Answer generation and faithfulness 7.2 Reranking over the In-Record Candi-
| are left to   | future | work (Section | 6).    |      |     |       | date      | Set |           |        |            |         |           |         |
| ------------- | ------ | ------------- | ------ | ---- | --- | ----- | --------- | --- | --------- | ------ | ---------- | ------- | --------- | ------- |
|               |        |               |        |      |     | Table | 5 reports |     | reranking | on the | per-record |         | candidate | set     |
| 7.1 Retrieval |        | over the      | Global | Pool |     |       |           |     |           |        |            |         |           |         |
|               |        |               |        |      |     | L     | = G       | ∪HN | (Section  | 3.6),  | isolating  | ranking |           | quality |
|               |        |               |        |      |     | r     | r         |     | r         |        |            |         |           |         |
Table4andFigure3(A)reportfirst-stageretrievaloverthe from first-stage recall.
| global pooled | corpus   | C (Section     | 3.6;    | |C| = 5230).   | Each |     |               |     |     |                |     |     |     |     |
| ------------- | -------- | -------------- | ------- | -------------- | ---- | --- | ------------- | --- | --- | -------------- | --- | --- | --- | --- |
| score is      | the mean | across queries | against | the per-record |      |     |               |     |     |                |     |     |     |     |
|               |          |                |         |                |      | 7.3 | Hard-Negative |     |     | Discrimination |     |     |     |     |
gold positives.
|     |     |     |     |     |     | Figure |     | 3(B) | reports | pairwise | accuracy |     | across | all |
| --- | --- | --- | --- | --- | --- | ------ | --- | ---- | ------- | -------- | -------- | --- | ------ | --- |
Metadata-filtered BM25. Because most hard nega- (positive,hard negative) pairs per record under the in-
tives originate from a different filing, a system that knows record ranking, contrasted with the same metric against
the target filing could pre-filter candidates on metadata randomnegativesdrawnuniformlyfromthepooledcorpus
before ranking. We quantify this directly: restricting C C excluding the record’s own positives (Section 6.2, seed
to entries whose (ticker, year, doc type) match the 42, one random negative per curated hard negative; tied
8

A  Retrieval over the global pool — Recall@k
|     |     |     | TF-IDF |     | Fin-BGE   |     | e5-mistral-7B   |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | BM25   |     | bge-large |     | Dense+CE rerank |     |     |     |     |     |     |     |     |
50
Dense (all-mpnet)
)%( llaceR 40
30
20
10
0
|     |     |     |     | R@1 |     | R@5 |     |     | R@10 |     |     | R@20 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
B  Hardness premium — pairwise accuracy, hard vs. random negatives
|     |                       |     | Hard negatives |        |     | Random negatives |     |         |     |        |     |        |     |      |     |
| --- | --------------------- | --- | -------------- | ------ | --- | ---------------- | --- | ------- | --- | ------ | --- | ------ | --- | ---- | --- |
|     |                       |     | +14            | . 2    |     | +19 .            | 3   |         | +17 | . 5    | +16 | . 0    | +15 | . 9  |     |
|     | )%( ycarucca esiwriaP | 100 |                | +13    | . 0 |                  |     | +20 . 5 |     |        |     | 9 6 .2 |     |      |     |
|     |                       |     |                | 9 1 .9 |     | 9 3              | .7  | 9 0 .8  |     | 9 3 .8 |     |        | 9   | 2 .0 |     |
8 7 .8
80.2
|     |     |     | 77.8 |      |     |      |      |     | 76.3 |     |     |     | 76.1 |     |     |
| --- | --- | --- | ---- | ---- | --- | ---- | ---- | --- | ---- | --- | --- | --- | ---- | --- | --- |
|     |     | 75  |      | 74.8 |     | 74.5 | 70.3 |     |      |     |     |     |      |     |     |
50
25
0
|     |     |     | TF-IDF | BM25 |     | Dense |     | Fin-BGE | bge-large |     | e5-7B |     | Cross-enc. |     |     |
| --- | --- | --- | ------ | ---- | --- | ----- | --- | ------- | --------- | --- | ----- | --- | ---------- | --- | --- |
Gap = random-negative accuracy − hard-negative accuracy. A larger gap means the released hard negatives are genuinely harder.
Figure 3: Executed baselines on FinRank. (A) First-stage retrieval over the global pool: Recall@k for the evaluated
systems. Even the strongest, a 7B instruction-tuned embedder, reaches only 44.8% Recall@10, and sub-billion-
parameter dense encoders gain little over BM25. (B) The hardness premium: pairwise ranking accuracy of each
model against its curated hard negatives versus random negatives. The 13.0–20.5 point gap is the empirical evidence
that the released hard negatives are genuinely harder than arbitrary distractors.
|     | Model  |                          |     |              | Recall@1 |      | Recall@5 |     | Recall@10 | Recall@20 |      | MRR  | nDCG@10 |      |     |
| --- | ------ | ------------------------ | --- | ------------ | -------- | ---- | -------- | --- | --------- | --------- | ---- | ---- | ------- | ---- | --- |
|     | TF-IDF |                          |     |              |          | 7.7  | 23.7     |     | 32.8      |           | 41.9 | 23.9 |         | 21.9 |     |
|     | BM25   |                          |     |              |          | 8.3  | 24.5     |     | 32.1      |           | 40.1 | 23.8 |         | 21.8 |     |
|     | Dense  | (all-mpnet-base-v2)      |     |              |          | 6.5  | 21.5     |     | 31.8      |           | 42.0 | 22.2 |         | 20.4 |     |
|     |        | + CE rerank              | of  | mpnet top-20 |          | 9.6  | 27.5     |     | 35.2      |           | 42.0 | 26.9 |         | 24.6 |     |
|     | Dense  | (finance-adapted         |     | BGE)         |          | 5.2  | 16.5     |     | 22.4      |           | 29.8 | 16.5 |         | 14.8 |     |
|     | Dense  | (bge-large-en-v1.5)      |     |              |          | 8.8  | 25.9     |     | 35.6      |           | 44.6 | 25.9 |         | 23.8 |     |
|     | Dense  | (e5-mistral-7b-instruct) |     |              |          | 10.1 | 33.1     |     | 44.8      |           | 55.0 | 31.0 |         | 29.7 |     |
Table 4: Retrieval performance on the global pooled corpus C (|C|=5230, 1185 queries). All values are percentages
| averaged     | over queries. |       |           |             |            |          |     |     |            |     |             |     |     |               |     |
| ------------ | ------------- | ----- | --------- | ----------- | ---------- | -------- | --- | --- | ---------- | --- | ----------- | --- | --- | ------------- | --- |
|              |               |       |           |             |            |          |     | 7.4 | Stratified |     | Performance |     |     | and Ablations |     |
| scores count | for           | the   | positive, | and records | are        | averaged |     |     |            |     |             |     |     |               |     |
| with equal   | weight).      | Every | model     | ranks       | a positive | above    |     |     |            |     |             |     |     |               |     |
a random negative 88–96% of the time but above a cu- Table 6 reports retrieval and reranking metrics strat-
|             |          |      |                  |          |       |             |     | ified   | along | four axes    | (document |             | type, | reasoning | type, |
| ----------- | -------- | ---- | ---------------- | -------- | ----- | ----------- | --- | ------- | ----- | ------------ | --------- | ----------- | ----- | --------- | ----- |
| rated hard  | negative | only | 70–80%           | of the   | time, | a 13.0–20.5 |     |         |       |              |           |             |       |           |       |
|             |          |      |                  |          |       |             |     | passage | type, | difficulty). |           | Per-stratum |       | partition | sizes |
| point drop. | This     | gap  | is the empirical | hardness |       | premium     |     |         |       |              |           |             |       |           |       |
of the released hard negatives, and it is the single result are emitted alongside the metrics in the underly-
|           |          |           |          |      |     |               |     | ing ablations.json. |     |     |     | Selected | cells | are reproduced |     |
| --------- | -------- | --------- | -------- | ---- | --- | ------------- | --- | ------------------- | --- | --- | --- | -------- | ----- | -------------- | --- |
| that most | directly | justifies | shipping | them | as  | a first-class |     |                     |     |     |     |          |       |                |     |
benchmark asset. below; the full stratified breakdown is available in
baselines/results/ablations.json.
9

Model MRR nDCG@5 instructiontuninghelpwherewrong-registerdomainadap-
tation hurts, and SEC-filing-specific adaptation remains
TF-IDF 80.4 77.9
open. Third, and most directly tied to the benchmark’s
BM25 78.2 75.4
design, the released hard negatives cost every model 13.0–
Dense (all-mpnet-base-v2) 78.6 74.7
20.5 points of pairwise accuracy relative to random dis-
Dense (finance-adapted BGE) 72.3 70.2
Dense (bge-large-en-v1.5) 79.1 76.5 tractors; this hardness premium is the single number that
Dense (e5-mistral-7b-instruct) 83.6 80.5 justifies shipping curated hard negatives as a first-class
Cross-encoder over L 79.8 76.6 asset. Fourth, the stratified breakdown exposes where
r
aggregate scores hide weakness: 10-Q, multi-passage, and
Table 5: Reranking performance on the in-record candi- quantitativerecordsscorelowest,whichispreciselywhywe
date set L . recommend per-stratum reporting. The 10-Q gap should
r
bereaddescriptivelyratherthancausally: all10-Qrecords
come from the oil and gas sector and predominantly from
Query-rewrite ablation. Table 7 compares retrieval 2025 (Appendix H), so document type is confounded with
performance on the subset of records with non-empty sector, filing year, and annotator, and disentangling these
query rewrite lists (819 records; see ablations.json) effects requires the controlled splits of Section 6.2.
undertwoconditions: therawquestionalone,andtheraw
question concatenated with all listed rewrites.
Why evidence grounding matters in finance. In
audit,compliance,andinvestor-relationssettingsthevalue
7.5 Answer Generation and Error Analy- of an answer is tied to its provenance: a reviewer needs
sis to know not just what a system claims but where the
claim comes from, so that the underlying disclosure can
FinRank is designed to support answer-generation eval- be inspected. FinRank operationalizes this by making the
uation (closed-book, open-book with gold passages, and identificationofsupportingpassagesafirst-classevaluation
full RAG, scored with EM, F1, ROUGE-L, BERTScore, target and by pairing it with hard negatives that stress
and citation-faithfulness metrics (Gao et al., 2023; Es et the boundary between genuinely supporting evidence and
al., 2024)) and a qualitative error analysis that separates plausible distractors. Because those distractors are most
retrieval failures (no supporting passage in the top-k), often a competitor’s comparable filing (Section 3.7), the
reranking failures (a hard negative preferred to a support- benchmark rewards systems that disambiguate between
ing passage), generation failures on correctly retrieved lexicallyandtopicallysimilardisclosures,thefailuremode
passages, andattributionfailures. Becausetheserequirea most likely to matter in practice. Multi-passage records
generative model and a human-validated or LLM-judged add a complementary axis, since financial conclusions
correctness protocol, we leave them to future work and frequently combine an MD&A narrative, a footnote, and
report only the executed retrieval and reranking results a tabular disclosure.
above; the evaluation protocol is specified in Section 6 so
that such studies remain comparable.
Scope. FinRank is intended for evaluating evidence re-
trieval, reranking, and (in future work) answer generation
8 Discussion for financial-analyst assistants, compliance QA tools, and
SEC-filingsearchinterfaces. Itisnotdesignedorvalidated
What the baselines reveal. Four observations stand for automated investment decisions, valuation, or trading
outfromSection7. First,rankingwithinacuratedpoolof signals,andanydeploymentinhigh-stakessettingsshould
confusable filing passages is hard: the strongest evaluated retain human oversight.
system, a 7B instruction-tuned embedder, reaches 44.8%
Recall@10 over the pooled corpus C, leaving more than
9 Limitations
half of the gold evidence outside the top ten. Because C
contains only annotated positives and curated distractors
rather than the full text of each filing, these numbers Scale and skew. FinRank contains 1185 records over
measure discrimination among confusable disclosure pas- 22 companies and three sectors, enough for ranking and
sages, not end-to-end retrieval over complete documents; answer-quality comparisons, but small relative to open-
full-document retrieval remains untested here. Second, domain QA benchmarks, and skewed across sector, filing
encoder capacity dominates domain labels on this heavily year(75%from2025),documenttype(87%10-K),andrea-
templated text: sub-billion-parameter encoders earn little soning type (roughly 2:1 qualitative). Aggregate metrics
(mpnet ties BM25; bge-large gains 3.5 Recall@10 points), therefore reflect the dominant strata, per-stratum subsets
a finance-adapted embedder tuned on consumer-finance can be noisy, and performance should not be assumed to
text trails BM25 by 9.7 points, while the 7B instruction- transfer to companies, sectors, jurisdictions, or periods
tunede5-mistralgains12.7pointsoverBM25—scaleand outside the release.
10

Axis Stratum BM25 R@10 Dense R@10 CE rerank R@10
10-K 33.9 33.7 36.9
Document type
10-Q 18.0 17.3 21.8
Qualitative 34.7 35.2 38.2
Reasoning
Quantitative 26.5 24.4 28.8
Single-Passage 44.7 42.3 46.9
Passage type Two-Passage 28.0 28.8 31.7
Multi-Passage 21.5 22.2 24.8
Easy 37.6 33.7 39.0
Difficulty Medium 32.4 32.5 35.3
Hard 25.9 28.6 31.0
Table 6: Recall@10 stratified by document type, reasoning type, passage type, and difficulty. Per-stratum sample
sizes are available in ablations.json.
Model/condition Recall@10(raw) Recall@10(withrewrites) this paper reports only retrieval and reranking baselines;
generativeanswer-qualityresultsarelefttofuturework,so
TF-IDF 32.3 41.1
BM25 29.9 38.7 noclaimaboutgeneratorperformanceonFinRankfollows
Dense 30.7 34.1 from it.
Table 7: Query-rewrite ablation on the subset of records
10 Ethical Considerations
with non-empty query rewrite lists. Because rewrites
are annotator-authored decompositions written with the
gold evidence in view, the right column should be read as FinRank is derived from filings that companies have sub-
anoracleupperboundondecomposition-assistedretrieval. mitted to the SEC and made public; it contains no non-
The right column concatenates the original question with public personal information. As is inherent to SEC filings,
all listed rewrites; the left uses the question alone. passages may name executives, directors, and officers in
their public corporate roles, including disclosures such as
executive compensation that issuers are legally required
Single-annotatorreview. Recordswereauthoredman- to publish. FinRank is released under CC BY-NC 4.0 for
uallybythestudentannotatorsandreviewedonasampled non-commercial research use with attribution; commer-
basis by the authors during collection (Section 3.5); we cial licensing is available from the authors (Appendix I).
did not re-verify every record or compute a formal inter- Because the dataset is skewed toward a few sectors, filing
annotator-agreement statistic, because each record was years, and document types (Section 4), models tuned or
authoredbyasinglestudentratherthandouble-annotated. evaluated on it may reflect the language of the dominant
Correctness on FinRank is thus single-annotator with strata, and cross-sector generalization should be tested
sampled review rather than consensus-adjudicated, and a explicitly rather than inferred from aggregate scores.
stratified double-annotation study is the most important Strong performance on FinRank does not establish suit-
outstanding item for a future release. ability for investment decisions, valuation, or trading, and
FinRank-aligned systems should complement rather than
replace qualified human analysts. Even accurate retrieval
Label and hard-negative artifacts. Raw fields con-
and generation systems can mis-rank passages, omit rele-
tain casing and spelling variants and a few placeholder
vant evidence, or produce plausible but incorrect answers,
values, which our normalization pipeline (Section 3.8) re-
so generated answers should not be presented as invest-
solves;consumerswhoskipnormalizationmayseespurious
ment advice and should carry inline citations to their
Unknown buckets. Separately, 442 hard negatives (∼7.3%)
supportingpassages, supportingtheauditandcompliance
arebyte-equaltoasupportingpassageofadifferent record,
review that financial disclosure requires.
where the passage may legitimately be relevant to more
than one question; the released hn taxonomy.json lets
users filter these overlaps. 11 Conclusion
Modality and generation. Tables and figures are rep- WeintroducedFinRank,anevidence-groundedbenchmark
resented as text, so evaluations requiring true multimodal for financial question answering and retrieval over SEC
reasoning over image-based tables are out of scope, and 10-K and 10-Q filings. Across 1185 manually authored
reference-based metrics may penalize answers that are records spanning 22 companies, three sectors, and eight
correct but phrased differently from the reference. Finally, topics for filings from 2024–2025, each question is paired
11

with supporting passages from the underlying filing and
with a curated set of hard negatives from comparable
filings, making FinRank, to our knowledge, the first fi-
nancial QA benchmark to release per-question curated
hard negatives and to measure discrimination against
curated versus random distractors directly. Among the
evaluatedbaselines,evena7Binstruction-tunedembedder
reaches only 44.8% Recall@10 on the curated evidence
pool, sub-billion-parameter embeddings beat BM25 by
at most 3.5 points on this templated text, and the re-
leased hard negatives cost every model 13.0–20.5 points of
pairwise accuracy over random distractors. Future work
includes broadening coverage to more sectors, companies,
and filing years; a stratified double-annotation study with
reported inter-annotator agreement; executing the gener-
ation and RAG protocols with LLM-based systems; and
extending the schema and hard-negative construction to
multimodal (tabular and graphical) evidence.
12

References
|     |     |     |     |     |     |     | Jiang, Yidong | et        | al. (2026). |              | “Fin-RATE: | A          | Real-world |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ----------- | ------------ | ---------- | ---------- | ---------- |
|     |     |     |     |     |     |     | Financial     | Analytics |             | and Tracking |            | Evaluation | Bench-     |
Chen,Jianetal.(2024).“FinTextQA:ADatasetforLong- mark for LLMs on SEC Filings”. In: Proceedings of the
form Financial Question Answering”. In: Proceedings of 32nd ACM SIGKDD Conference on Knowledge Discov-
| the 62nd  | Annual      | Meeting | of the            | Association   | for          | Compu- |            |          |        |             |              |     |             |
| --------- | ----------- | ------- | ----------------- | ------------- | ------------ | ------ | ---------- | -------- | ------ | ----------- | ------------ | --- | ----------- |
|           |             |         |                   |               |              |        | ery and    | Data     | Mining | (KDD        | ’26). arXiv: |     | 2602.07294  |
| tational  | Linguistics | (Volume | 1:                | Long Papers). | Bangkok,     |        | [cs.CL].   |          |        |             |              |     |             |
| Thailand: | Association |         | for Computational |               | Linguistics, |        |            |          |        |             |              |     |             |
|           |             |         |                   |               |              |        | Karpukhin, | Vladimir | et     | al. (2020). | “Dense       |     | Passage Re- |
pp. 6025–6047. arXiv: 2405.09980 [cs.CL]. trieval for Open-Domain Question Answering”. In: Pro-
Chen, Zhiyu, Wenhu Chen, et al. (2021). “FinQA: A ceedings of the 2020 Conference on Empirical Methods
| Dataset | of Numerical | Reasoning |     | over Financial |     | Data”. |            |          |     |            |          |     |     |
| ------- | ------------ | --------- | --- | -------------- | --- | ------ | ---------- | -------- | --- | ---------- | -------- | --- | --- |
|         |              |           |     |                |     |        | in Natural | Language |     | Processing | (EMNLP). |     |     |
In: Proceedings of the 2021 Conference on Empirical Kwiatkowski, Tom et al. (2019). “Natural Questions:
Methods in Natural Language Processing (EMNLP). A Benchmark for Question Answering Research”. In:
| Chen, Zhiyu,   | Shiyang   | Li,          | et al. (2022). | “ConvFinQA: |              | Ex- |              |     |                 |     |                   |     |      |
| -------------- | --------- | ------------ | -------------- | ----------- | ------------ | --- | ------------ | --- | --------------- | --- | ----------------- | --- | ---- |
|                |           |              |                |             |              |     | Transactions | of  | the Association |     | for Computational |     | Lin- |
| ploring        | the Chain | of Numerical |                | Reasoning   | in Conversa- |     | guistics.    |     |                 |     |                   |     |      |
| tional Finance | Question  |              | Answering”.    | In:         | Proceedings  |     | of           |     |                 |     |                   |     |      |
Lewis,Patricketal.(2020).“Retrieval-AugmentedGenera-
the 2022 Conference on Empirical Methods in Natural tion for Knowledge-Intensive NLP Tasks”. In: Advances
Language Processing (EMNLP). in Neural Information Processing Systems (NeurIPS).
| Choi, Chanyeol |     | et al. | (2025). | “FinDER: | Financial |     |           |       |        |         |            |          |     |
| -------------- | --- | ------ | ------- | -------- | --------- | --- | --------- | ----- | ------ | ------- | ---------- | -------- | --- |
|                |     |        |         |          |           |     | Mansouri, | Sasan | et al. | (2026). | “Bypassing | Document | In- |
Dataset for Question Answering and Evaluating gestion: An MCP Approach to Financial Q&A”. In:
| Retrieval-Augmented |     | Generation”. |     | In: | arXiv | preprint |          |          |                   |     |        |     |            |
| ------------------- | --- | ------------ | --- | --- | ----- | -------- | -------- | -------- | ----------------- | --- | ------ | --- | ---------- |
|                     |     |              |     |     |       |          | arXiv    | preprint | arXiv:2603.20316. |     | arXiv: |     | 2603.20316 |
| arXiv:2504.15800.   |     |              |     |     |       |          | [cs.IR]. |          |                   |     |        |     |            |
Choi, Chanyeol, Jihoon Kwon, et al. (2025). “FinAgent- Min,Sewonetal.(2023).“FActScore:Fine-grainedAtomic
| Bench: | A Benchmark | Dataset |     | for Agentic | Retrieval |     | in         |     |         |           |     |      |           |
| ------ | ----------- | ------- | --- | ----------- | --------- | --- | ---------- | --- | ------- | --------- | --- | ---- | --------- |
|        |             |         |     |             |           |     | Evaluation | of  | Factual | Precision | in  | Long | Form Text |
Financial Question Answering”. In: Proceedings of the Generation”. In: Proceedings of the 2023 Conference
| 6th ACM | International |     | Conference | on  | AI in | Finance |              |         |     |            |          |     |             |
| ------- | ------------- | --- | ---------- | --- | ----- | ------- | ------------ | ------- | --- | ---------- | -------- | --- | ----------- |
|         |               |     |            |     |       |         | on Empirical | Methods |     | in Natural | Language |     | Processing. |
(ICAIF ’25). ACM. arXiv: 2508.14052 [cs.IR]. Association for Computational Linguistics. arXiv: 2305.
| Choi, Chanyeol, | Jy-Yong    |     | Sohn,      | et al. (2024).   | The | ACM- | 14251        | [cs.CL]. |     |             |        |     |              |
| --------------- | ---------- | --- | ---------- | ---------------- | --- | ---- | ------------ | -------- | --- | ----------- | ------ | --- | ------------ |
| ICAIF’24        | FinanceRAG |     | Challenge. | https://finance- |     |      |              |          |     |             |        |     |              |
|                 |            |     |            |                  |     |      | Muennighoff, | Niklas   | et  | al. (2023). | “MTEB: |     | Massive Text |
rag.com/. Competition at the 5th ACM International Embedding Benchmark”. In: Proceedings of the 17th
| Conference                  | on  | AI in Finance |     | (ICAIF     | ’24). | Dataset: |                   |        |              |     |            |        |              |
| --------------------------- | --- | ------------- | --- | ---------- | ----- | -------- | ----------------- | ------ | ------------ | --- | ---------- | ------ | ------------ |
|                             |     |               |     |            |       |          | Conference        | of the | European     |     | Chapter    | of the | Association  |
| Linq-AI-Research/FinanceRAG |     |               |     | on Hugging | Face. |          |                   |        |              |     |            |        |              |
|                             |     |               |     |            |       |          | for Computational |        | Linguistics. |     | Dubrovnik, |        | Croatia: As- |
Deng, Yang et al. (2022). “PACIFIC: Towards Proactive sociation for Computational Linguistics, pp. 2014–2037.
| Conversational |     | Question | Answering | over | Tabular | and |        |            |          |     |     |     |     |
| -------------- | --- | -------- | --------- | ---- | ------- | --- | ------ | ---------- | -------- | --- | --- | --- | --- |
|                |     |          |           |      |         |     | arXiv: | 2210.07316 | [cs.CL]. |     |     |     |     |
Textual Data in Finance”. In: Proceedings of the 2022 Nogueira, Rodrigo and Kyunghyun Cho (2019). “Pas-
Conference on Empirical Methods in Natural Language sage Re-ranking with BERT”. In: arXiv preprint
| Processing. | Abu | Dhabi, | United | Arab | Emirates: | Asso- |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ------ | ---- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
arXiv:1901.04085.
ciation for Computational Linguistics, pp. 6970–6984. Qu,Yingqietal.(2021).“RocketQA:AnOptimizedTrain-
| arXiv: | 2210.08817 | [cs.CL]. |     |     |     |     |              |     |          |         |           |     |           |
| ------ | ---------- | -------- | --- | --- | --- | --- | ------------ | --- | -------- | ------- | --------- | --- | --------- |
|        |            |          |     |     |     |     | ing Approach |     | to Dense | Passage | Retrieval |     | for Open- |
Es, Shahul et al. (2024). “RAGAs: Automated Evaluation Domain Question Answering”. In: Proceedings of the
ofRetrievalAugmentedGeneration”.In:Proceedings of 2021 Conference of the North American Chapter of the
| the 18th | Conference | of the | European | Chapter | of  | the As- |             |     |               |     |              |     |            |
| -------- | ---------- | ------ | -------- | ------- | --- | ------- | ----------- | --- | ------------- | --- | ------------ | --- | ---------- |
|          |            |        |          |         |     |         | Association | for | Computational |     | Linguistics: |     | Human Lan- |
sociationforComputationalLinguistics:SystemDemon- guage Technologies. Association for Computational Lin-
| strations. | St. Julians, | Malta: |     | Association | for | Compu- |           |                |     |        |            |     |          |
| ---------- | ------------ | ------ | --- | ----------- | --- | ------ | --------- | -------------- | --- | ------ | ---------- | --- | -------- |
|            |              |        |     |             |     |        | guistics, | pp. 5835–5847. |     | arXiv: | 2010.08191 |     | [cs.CL]. |
tational Linguistics, pp. 150–158. arXiv: 2309.15217 Rajpurkar,Pranavetal.(2016).“SQuAD:100,000+Ques-
[cs.CL]. tions for Machine Comprehension of Text”. In: Proceed-
Gao,Tianyuetal.(2023).“EnablingLargeLanguageMod-
|     |     |     |     |     |     |     | ings of | the 2016 | Conference |     | on Empirical |     | Methods in |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | --- | ------------ | --- | ---------- |
els to Generate Text with Citations”. In: Proceedings of Natural Language Processing (EMNLP).
| the 2023 | Conference | on  | Empirical | Methods | in  | Natural |        |          |        |         |            |     |         |
| -------- | ---------- | --- | --------- | ------- | --- | ------- | ------ | -------- | ------ | ------- | ---------- | --- | ------- |
|          |            |     |           |         |     |         | Reddy, | Varshini | et al. | (2024). | “DocFinQA: |     | A Long- |
Language Processing. Association for Computational Context Financial Reasoning Dataset”. In: Proceed-
Linguistics. arXiv: 2305.14627 [cs.CL]. ings of the 62nd Annual Meeting of the Association for
Islam,Pranabetal.(2023).“FinanceBench:ANewBench-
|     |     |     |     |     |     |     | Computational |     | Linguistics |     | (Volume | 2: Short | Papers). |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ------- | -------- | -------- |
mark for Financial Question Answering”. In: arXiv Bangkok, Thailand: Association for Computational Lin-
| preprint         | arXiv:2311.11944. |             |               |     |       |        |           |              |       |          |            |         |            |
| ---------------- | ----------------- | ----------- | ------------- | --- | ----- | ------ | --------- | ------------ | ----- | -------- | ---------- | ------- | ---------- |
|                  |                   |             |               |     |       |        | guistics, | pp. 445–458. |       | arXiv:   | 2401.06915 |         | [cs.CL].   |
| Izacard, Gautier | et                | al. (2022). | “Unsupervised |     | Dense | Infor- |           |              |       |          |            |         |            |
|                  |                   |             |               |     |       |        | Reimers,  | Nils and     | Iryna | Gurevych |            | (2019). | “Sentence- |
mationRetrievalwithContrastiveLearning”.In:Trans- BERT: Sentence Embeddings using Siamese BERT-
| actions | on Machine | Learning |     | Research | (TMLR). |     |            |     |             |     |        |      |            |
| ------- | ---------- | -------- | --- | -------- | ------- | --- | ---------- | --- | ----------- | --- | ------ | ---- | ---------- |
|         |            |          |     |          |         |     | Networks”. | In: | Proceedings |     | of the | 2019 | Conference |
13

on Empirical Methods in Natural Language Processing tational Linguistics, pp. 6588–6600. arXiv: 2206.01347
(EMNLP). [cs.CL].
Robertson, Stephen and Hugo Zaragoza (2009). “The Zhou, Yixi et al. (2026). “FinCARDS: Card-Based Ana-
ProbabilisticRelevanceFramework:BM25andBeyond”. lyst Reranking for Financial Document Question An-
In: Foundations and Trends in Information Retrieval swering”. In: Findings of the Association for Com-
3.4, pp. 333–389. putational Linguistics: ACL 2026. San Diego, Califor-
Strich, Jan et al. (2026). “T2-RAGBench: Text-and-Table nia, United States: Association for Computational Lin-
Benchmark for Evaluating Retrieval-Augmented Gen- guistics, pp. 24836–24852. doi: 10.18653/v1/2026.
eration”. In: Proceedings of the 19th Conference of the findings-acl.1244. arXiv: 2601.06992 [cs.CL].
European Chapter of the Association for Computational url: https://aclanthology.org/2026.findings-
Linguistics (Volume 1: Long Papers). Rabat, Morocco: acl.1244/.
Association for Computational Linguistics, pp. 165–191. Zhu, Fengbin et al. (2021). “TAT-QA: A Question An-
arXiv: 2506.12071 [cs.CL]. sweringBenchmarkonaHybridofTabularandTextual
Tang, Yixuan and Yi Yang (2025). “FinMTEB: Finance ContentinFinance”.In:Proceedings of the 59th Annual
Massive Text Embedding Benchmark”. In: Proceedings Meeting of the Association for Computational Linguis-
ofthe2025ConferenceonEmpiricalMethodsinNatural tics (ACL).
Language Processing. Introduces the Fin-E5 finance-
adapted embedding model. Suzhou, China: Association
for Computational Linguistics, pp. 3620–3638. arXiv:
2502.10990 [cs.CL].
Thakur, Nandan et al. (2021). “BEIR: A Heterogenous
Benchmark for Zero-shot Evaluation of Information
Retrieval Models”. In: Proceedings of the Neural In-
formation Processing Systems Track on Datasets and
Benchmarks (NeurIPS). arXiv: 2104.08663 [cs.IR].
Wasserman,Navveetal.(2025).“DocReRank:Single-Page
Hard Negative Query Generation for Training Multi-
Modal RAG Rerankers”. In: Proceedings of the 2025
Conference on Empirical Methods in Natural Language
Processing. Suzhou, China: Association for Computa-
tional Linguistics, pp. 8640–8658. arXiv: 2505.22584
[cs.CV].
Wu, Shijie et al. (2023). “BloombergGPT: A Large
Language Model for Finance”. In: arXiv preprint
arXiv:2303.17564.
Xiong, Lee et al. (2021). “Approximate Nearest Neigh-
bor Negative Contrastive Learning for Dense Text Re-
trieval”. In: International Conference on Learning Rep-
resentations (ICLR). arXiv: 2007.00808 [cs.IR].
Zhan, Jingtao et al. (2021). “Optimizing Dense Retrieval
Model Training with Hard Negatives”. In: Proceedings
of the 44th International ACM SIGIR Conference on
Research and Development in Information Retrieval.
ACM. arXiv: 2104.08051 [cs.IR].
Zhao, Suifeng et al. (2025). “FinRAGBench-V: A Bench-
mark for Multimodal RAG with Visual Citation in
the Financial Domain”. In: Proceedings of the 2025
Conference on Empirical Methods in Natural Language
Processing. Suzhou, China: Association for Computa-
tional Linguistics, pp. 4215–4249. arXiv: 2505.17471
[cs.CL].
Zhao, Yilun et al. (2022). “MultiHiertt: Numerical Rea-
soning over Multi Hierarchical Tabular and Textual
Data”. In: Proceedings of the 60th Annual Meeting of
the Association for Computational Linguistics (Volume
1:LongPapers).Dublin,Ireland:AssociationforCompu-
14

| A Question |     | Generation |     |     | and | Annotation |     | Criteria |
| ---------- | --- | ---------- | --- | --- | --- | ---------- | --- | -------- |
This appendix consolidates the full question-generation methodology that governs FinRank, complementing the
summary in Section 3.2. The methodology fixes the criteria against which the released JSONL was constructed and
| against which | a   | third party | can | audit | or extend | the | benchmark. |     |
| ------------- | --- | ----------- | --- | ----- | --------- | --- | ---------- | --- |
A.1 Purpose
The methodology defines criteria for generating questions about financial filings so that the resulting question set
provides systematic coverage across financial topics, reasoning types, and complexity levels. The intent is a balanced
and thorough evaluation resource, not an arbitrary collection of natural-language prompts.
| A.2 Core |     | Definitions |     |     |     |     |     |     |
| -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Passage. A discrete section of text from a financial filing that can provide standalone context for answering a
| question. | Passages | are | the unit | of evidence | and | the unit | of retrieval. |     |
| --------- | -------- | --- | -------- | ----------- | --- | -------- | ------------- | --- |
Financial filing. An SEC document, specifically a Form 10-K (annual report) or Form 10-Q (quarterly report),
| containing | a company’s |     | financial | and | operational | disclosures. |     |     |
| ---------- | ----------- | --- | --------- | --- | ----------- | ------------ | --- | --- |
Query rewrite. A decomposition of a complex question into a sequence of sub-questions that guide analytical
| reasoning     | and expose | intermediate |       | retrieval |     | and reasoning | steps. |     |
| ------------- | ---------- | ------------ | ----- | --------- | --- | ------------- | ------ | --- |
| A.3 Reasoning |            |              | Types |           |     |               |        |     |
Qualitative reasoning. Interpretation, explanation, or judgment questions that do not require arithmetic calcula-
tions (e.g. business strategy analysis, revenue-recognition judgments, litigation impact discussions).
Quantitative reasoning. Any question requiring numerical computation, comparison, or mathematical analysis.
| Quantitative | questions |     | are further | partitioned |     | into three | subtypes: |     |
| ------------ | --------- | --- | ----------- | ----------- | --- | ---------- | --------- | --- |
1. Metrics-generated: questionsderivedautomaticallyfromstandardizedfinancialratiosandtemplatedcalculations
| (e.g. current-ratio |     | queries). |     |     |     |     |     |     |
| ------------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
2. Single-step arithmetic: a single division, multiplication, addition, or subtraction.
3. Compositional calculations: multi-step arithmetic requiring two or more sequential operations.
| A.4 Financial |     | Topic |     | Categories |     |     |     |     |
| ------------- | --- | ----- | --- | ---------- | --- | --- | --- | --- |
Themethodologypartitionsfilingcontentintoeightfinancialtopiccategories. Foreachtopicthemethodologysupplies
| both qualitative     |     | and quantitative |     | reasoning   |     | targets (Table | 8). |     |
| -------------------- | --- | ---------------- | --- | ----------- | --- | -------------- | --- | --- |
| A.5 Complexity-Level |     |                  |     | Definitions |     |                |     |     |
Questions are distributed across three complexity levels with target shares 30% Easy, 40% Medium, 30% Hard.
Easy (direct / factual). Simple factual retrieval from a filing section, straightforward numerical queries, basic
definitional questions; minimal interpretation. Examples: “What was the company’s total revenue in 2023?”; “What
is the company’s primary business segment?”; “When does the company’s fiscal year end?”
Medium (analytical). Comparisonsbetweenperiodsorsegments,basictrendanalysis,percentagecalculations,and
cross-referencingbetweenrelatedfilingsections. Medium-levelquestionsshipwithamulti-sub-questionquery rewrite.
Example original question: “How did the company’s profitability change between 2022 and 2023, and what drove this
change?” Rewrite (abridged): gross/operating/net margins for both periods, followed by an attribution sub-question
| for the year-over-year |     | change. |     |     |     |     |     |     |
| ---------------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
15

Topic Qualitative reasoning examples Quantitative reasoning examples
Company Business nature, strategy evaluation, YoY revenue growth, headcount
|     | Overview |     | M&A | rationale |     |     |     | changes, EBITDA | margin |
| --- | -------- | --- | --- | --------- | --- | --- | --- | --------------- | ------ |
Financials Earningsquality,operatingmargincon- EPS changes, debt-to-equity, free cash
|     |     |     | sistency |     |     |     |     | flow per share |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | -------------- | --- |
Footnotes Accounting policy implications, lease Depreciation schedules, stock-
|     |     |     | classifications |     |     |     |     | compensation | expense |
| --- | --- | --- | --------------- | --- | --- | --- | --- | ------------ | ------- |
Governance Board composition, audit committee Director independence %, executive
|     |     |     | scope |     |     |     |     | pay ratios |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | ---------- | --- |
Accounting Revenue-recognition judgments, im- Amortizationchanges,deferred-taxcal-
|     |     |     | pairment | triggers |     |     |     | culations |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- | --------- | --- |
Legal Contingent liability discussions, litiga- Legal provision amounts, legal cost
|     |     |     | tion | impacts |     |     |     | trends |     |
| --- | --- | --- | ---- | ------- | --- | --- | --- | ------ | --- |
Risk Risk sensitivity analysis, risk manage- Value-at-Risk, interest coverage ratios
ment evaluation
Shareholder Re- Dividend policy rationale, buyback Total shareholder returns, dividend
|     | turn |     | strategy |     |     |     |     | payout ratios |     |
| --- | ---- | --- | -------- | --- | --- | --- | --- | ------------- | --- |
Table 8: Topic–reasoning matrix from the FinRank question-generation methodology. The matrix is prescriptive: it
specifies the (topic,reasoning type) cells that the dataset is expected to populate.
Hard (complex synthesis). Multi-step reasoning across multiple sections, complex synthesis, risk assessment
using multiple data points, or strategic analysis combining various filing elements. Hard-level questions ship with
three or more sub-questions that sequentially reduce the synthesis problem to factual queries. Example original
question: “How do the company’s liquidity risks relate to their debt covenant requirements and upcoming maturities?”
Rewrite (abridged): current, quick, and cash ratios; cash balances; specific covenant requirements; current covenant
| margins;  | 12- and | 24-month | maturities; | final | synthesis |     | sub-question. |     |     |
| --------- | ------- | -------- | ----------- | ----- | --------- | --- | ------------- | --- | --- |
| A.6 Query |         | Rewrite  | Rules       |       |           |     |               |     |     |
Query rewrites serve four purposes: they break complexity into manageable components, ensure completeness of the
reasoning chain, make the analytical process transparent, and allow evaluation of intermediate retrieval steps rather
| than only | end-to-end | answer    | correctness. |         | The application |     | rule | is: |     |
| --------- | ---------- | --------- | ------------ | ------- | --------------- | --- | ---- | --- | --- |
| • Easy    | questions: | generally | do not       | require | rewrites.       |     |      |     |     |
•
| Medium | questions: |     | require multiple | atomic | sub-questions. |     |     |     |     |
| ------ | ---------- | --- | ---------------- | ------ | -------------- | --- | --- | --- | --- |
• Hard questions: require three or more sub-questions that sequentially decompose complex reasoning into factual
queries.
| A.7 Passage |     | Coverage | Requirements |     |     |     |     |     |     |
| ----------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
Questions are also distributed by the number of passages required to answer them, with target shares 40% single-
passage (1 passage), 30% two-passage (exactly 2 passages), and 30% multi-passage (3 or more passages). The intent
is to force the benchmark to include multi-passage synthesis, which more closely matches realistic financial analysis.
| A.8 Implementation |     |     | Guidelines |     |     |     |     |     |     |
| ------------------ | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
The methodology binds the above criteria into five implementation guidelines for any party generating FinRank-style
questions:
| 1. Balance | across | topics: | every | topic category |     | is represented. |     |     |     |
| ---------- | ------ | ------- | ----- | -------------- | --- | --------------- | --- | --- | --- |
2. Reasoning-type mix: balance between qualitative and quantitative questions.
| 3. Complexity |               | distribution: | adhere | to              | the 30%–40%–30% |     | split.         |     |     |
| ------------- | ------------- | ------------- | ------ | --------------- | --------------- | --- | -------------- | --- | --- |
| 4. Passage    | requirements: |               | follow | the 40%–30%–30% |                 |     | split exactly. |     |     |
5. Sub-question creation: generate the required rewrites for medium and hard questions.
| Realized | deviations | from | these guidelines |     | are reported |     | in Table | 2.  |     |
| -------- | ---------- | ---- | ---------------- | --- | ------------ | --- | -------- | --- | --- |
16

| A.9 Related | Resources |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
The methodology cites two prior financial-QA resources as conceptual context for FinRank-style question generation.
FinanceBench(Islametal.,2023)providesacomprehensiveopen-bookQAtestsuiteof10,231questionsaboutpublicly
traded companies, and the FinDER dataset of Choi et al. (2025) contributes expert-generated query–evidence–answer
triplets with realistic abbreviations and domain-specific language for RAG evaluation in finance. FinRank differs
from both in foregrounding the retrieval and reranking sub-tasks with explicit hard negatives drawn from comparable
| filings (Section | 2).      |             |     |      |     |      |     |           |     |
| ---------------- | -------- | ----------- | --- | ---- | --- | ---- | --- | --------- | --- |
| A.10             | What the | Methodology |     | Does | and | Does | Not | Guarantee |     |
The methodology provides structured generation criteria: it fixes what topics, reasoning types, complexity levels,
passage counts, and rewrites a FinRank question must satisfy, and is therefore the source of truth for reproducibility
and benchmark validity arguments. It does not by itself certify the correctness of any individual question, answer,
supporting passage, or hard negative; it does not specify human validation, expert adjudication, or inter-annotator
agreement statistics. We treat the methodology as evidence that the dataset’s generation procedure was deliberate
and as the basis for the deviation reporting in Table 2, while recording label-correctness audits as outstanding items
| in Section    | 9.            |        |        |         |             |            |        |         |     |
| ------------- | ------------- | ------ | ------ | ------- | ----------- | ---------- | ------ | ------- | --- |
| B Record      | Schema        |        |        |         |             |            |        |         |     |
| Table 9 gives | the top-level | schema | of a   | FinRank | record.     |            |        |         |     |
|               | Field         |        | Type   |         | Description |            |        |         |     |
|               | id            |        | string |         | UUID        | identifier | of the | record. |     |
question id string Original question identifier inherited from the source folder.
|     | ticker |     | string |     | Stock | ticker | of the filing | company. |     |
| --- | ------ | --- | ------ | --- | ----- | ------ | ------------- | -------- | --- |
industry string Industry classification associated with the filing company.
|     |     |     | string |     | Natural-language |     | question. |     |     |
| --- | --- | --- | ------ | --- | ---------------- | --- | --------- | --- | --- |
question
|     | answer |     | string |     | Reference | answer | text. |     |     |
| --- | ------ | --- | ------ | --- | --------- | ------ | ----- | --- | --- |
query rewrite array Optional alternative formulations of the question.
topic string Topicalcategoryofthequestion(forexample,Risk,Account-
ing, Governance).
reasoning type string Qualitative or Quantitative reasoning required to answer.
difficulty string Easy, Medium, or Hard, with some casing variation in the
raw data.
num passages string/int Number of supporting passages required to answer.
passage type string Single-, One-, Two-, or Multi-Passage indicator, with some
|     |          |     |            |     | spelling | variation | in                | the raw  | data.     |
| --- | -------- | --- | ---------- | --- | -------- | --------- | ----------------- | -------- | --------- |
|     | year     |     | string/int |     | Filing   | year      | of the underlying |          | document. |
|     | doc type |     | string     |     | SEC      | document  | type              | (10-K or | 10-Q).    |
passages array Supporting passages with text and page reference.
hard negatives array Hardnegativepassageswithtext,pagereference,ticker,year,
|     |             |     |        |              | and document |        | type.  |         |         |
| --- | ----------- | --- | ------ | ------------ | ------------ | ------ | ------ | ------- | ------- |
|     | folder name |     | string |              | Source       | folder | of the | record. |         |
|     |             |     | Table  | 9: Top-level |              | schema | of a   | FinRank | record. |
The nested passages and hard negatives objects, abbreviated above, are detailed in Tables 10 and 11.
|     | Field |     | Type |     | Description |     |     |     |     |
| --- | ----- | --- | ---- | --- | ----------- | --- | --- | --- | --- |
text string Passage content drawn from the underlying SEC filing.
|     | page number |     | string/int |     | Page | reference | within | the source | document. |
| --- | ----------- | --- | ---------- | --- | ---- | --------- | ------ | ---------- | --------- |
passage id string Stableidentifier<record id>:p<index>(normalizedrelease).
text sha1 string SHA-1 of the whitespace-trimmed text (normalized release).
|     |     |     | Table | 10: Schema | of  | an entry | in the | passages | array. |
| --- | --- | --- | ----- | ---------- | --- | -------- | ------ | -------- | ------ |
17

|     | Field       | Type       | Description   |                  |            |           |
| --- | ----------- | ---------- | ------------- | ---------------- | ---------- | --------- |
|     | text        | string     | Hard-negative | passage          | content.   |           |
|     | page number | string/int | Page          | reference within | the source | document. |
ticker string Tickerofthecompanywhosefilingthehardnegativeisdrawn
from.
|     | year | string/int | Filing | year of the source | document. |     |
| --- | ---- | ---------- | ------ | ------------------ | --------- | --- |
doc type string Source document type (for example, 10-K or 10-Q).
passage id string Stable identifier <record id>:hn<index> (normalized re-
lease).
text sha1 string SHA-1 of the whitespace-trimmed text (normalized release).
|             |     | Table 11: Schema    | of an | entry in the hard | negatives | array. |
| ----------- | --- | ------------------- | ----- | ----------------- | --------- | ------ |
| C Canonical |     | Label Normalization |       | Mapping           |           |        |
Table 12 enumerates the canonical label normalizations applied in curating the released FinRank.jsonl (Section 3.8).
Changed values are preserved inline in parallel <field> raw fields, and every individual change is enumerated in the
| released repair | log.json.                                |                  |     |                         |        |     |
| --------------- | ---------------------------------------- | ---------------- | --- | ----------------------- | ------ | --- |
| Field           | Rawvalue(s)                              |                  |     | Canonicalvalue          |        |     |
| reasoningtype   | Qaltitative,Qualtitative,Qalitative      |                  |     | Qualitative             |        |     |
| reasoningtype   | "Quantitative                            | "(trailingspace) |     | Quantitative            |        |     |
| reasoningtype   | "string"                                 |                  |     | Recoveredfromquestionid |        |     |
| passagetype     | One-Passage,OnePassage,OnePassage        |                  |     | Single-Passage(merged)  |        |     |
| passagetype     | Tow-Passage,Two-Page                     |                  |     | Two-Passage             |        |     |
| passagetype     | Mutli-Passage,MultiPassage,Multi-passage |                  |     | Multi-Passage           |        |     |
| passagetype     | "string"                                 |                  |     | Recoveredfromquestionid |        |     |
| topic           | Foodnotes                                |                  |     | Footnotes               |        |     |
| topic           | CompanyOverview                          |                  |     | Company Overview        |        |     |
| topic           | ShareholderReturn                        |                  |     | Shareholder             | Return |     |
| topic           | Financial                                |                  |     | Financials              |        |     |
| industry        | Pharmaceutical,Phamaceuticals            |                  |     | Pharmaceuticals         |        |     |
| industry        | Oil                                      | and Gas          |     | Oil & Gas               |        |     |
industry Oil & Gas {Midstream,E&P,...} Oil & Gas(sub-industrysurfaced)
difficulty lowercase/leading-spacevariants Title-caseEasy/Medium/Hard
| ticker     | Ford                            |     |     | F                       |     |     |
| ---------- | ------------------------------- | --- | --- | ----------------------- | --- | --- |
| ticker     | "string"                        |     |     | Recoveredfromquestionid |     |     |
| difficulty | "string"                        |     |     | Recoveredfromquestionid |     |     |
| doctype    | multi-sourcecompounds(2records) |     |     | Unknown                 |     |     |
year "integer" Majorityyearofsame-ticker,same-doctyperecords(flaggedasinferred)
Table 12: Canonical label normalization mapping applied in curating the release. Changed values are preserved in
| parallel <field> | raw | fields. |     |     |     |     |
| ---------------- | --- | ------- | --- | --- | --- | --- |
Beyond label mapping, the pipeline performs three record-level repairs, each preserved in a machine-readable repair
log: (i) hard-negative metadata whose fields were transposed at entry time is restored by rule (a numeric ticker
alongside an alphabetic page number is swapped back, 10 cases; a ticker/doc type rotation is reversed, 2 cases; one
placeholder hard-negative year is inferred by ticker–document majority); (ii) the 11 hard negatives whose trimmed
text duplicated a gold passage of their own record are removed, as are empty and within-record duplicate passages,
and page references that are not page numbers are nulled; and (iii) every stored label is cross-checked against the
structured question id, with the 56 disagreements shipped in the repair log as candidates for manual audit rather
than silently overwritten. A final exclusion pass removes sixty-five records from the release: fifty-two whose question,
answer, rewrite, or evidence involves a non-filing source (an academic journal article one annotator used as an
analytical frame, detected both by download-watermark markers and by the article’s distinctive regression variables);
three whose hard negatives are synthetic relevance rationales rather than filing passages; three with placeholder or
empty question or answer text; four exact duplicates of another record’s question–answer pair; and three records
left with fewer than four unique hard negatives. Each exclusion is recorded in repair log.json with its rule; the
release-blocking checks are implemented in baselines/validate release.py.
18

| D Example |     | Record |     |     |     |     |
| --------- | --- | ------ | --- | --- | --- | --- |
A sanitized and abbreviated example of a single FinRank record (long passages and the full hard-negative array
are truncated). The example illustrates several data-quality observations from Section 4.1: a reasoning type typo
(Qaltitative), a lower-case difficulty (easy), and inconsistent doc type casing between the supporting passages
| and the hard | negatives. |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- |
{
"id": "97546a79-...-82c119a9c38c",
"question_id": "JNJ_CompanyOverview_Easy_OnePassage_Qualitative_01",
| "ticker":   | "JNJ",             |     |     |     |     |     |
| ----------- | ------------------ | --- | --- | --- | --- | --- |
| "industry": | "Pharmaceuticals", |     |     |     |     |     |
"question": "Which reportable business segments does Johnson & Johnson
|                   | operate   | in             | as of   | FY2024?",    |          |             |
| ----------------- | --------- | -------------- | ------- | ------------ | -------- | ----------- |
| "answer":         | "As of    | FY2024,        | Johnson | & Johnson    | operates | in two main |
|                   | segments: | Innovative     |         | Medicine and | MedTech  | ...",       |
| "query_rewrite":  |           | [],            |         |              |          |             |
| "topic":          | "Company  | Overview",     |         |              |          |             |
| "reasoning_type": |           | "Qaltitative", |         |              |          |             |
| "difficulty":     | "easy",   |                |         |              |          |             |
| "num_passages":   |           | "1",           |         |              |          |             |
| "passage_type":   |           | "One-Passage", |         |              |          |             |
| "year":           | "2025",   |                |         |              |          |             |
| "doc_type":       | "10-K",   |                |         |              |          |             |
| "passages":       | [         |                |         |              |          |             |
{
"text": "### Description of the company and business segments ...",
| "page_number": |     | "22" |     |     |     |     |
| -------------- | --- | ---- | --- | --- | --- | --- |
}
],
| "hard_negatives": |     | [   |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- |
{
| "text":        | "####   | Note   | 19: Segment | Information | ...", |     |
| -------------- | ------- | ------ | ----------- | ----------- | ----- | --- |
| "page_number": |         | "106", |             |             |       |     |
| "ticker":      | "LLY",  |        |             |             |       |     |
| "year":        | "2025", |        |             |             |       |     |
| "doc_type":    |         | "10-k" |             |             |       |     |
}
],
| "folder_name": |     | "annotator_01" |     |     |     |     |
| -------------- | --- | -------------- | --- | --- | --- | --- |
}
| E Reasoning-Type |     |     | Examples |     |     |     |
| ---------------- | --- | --- | -------- | --- | --- | --- |
To make the conceptual range of the questions concrete, we reproduce one record per representative reasoning mode
below, verbatim from FinRank.jsonl (excerpts truncated for space). Each shows the question, an excerpt of the
reference answer, an excerpt of one supporting passage, and an excerpt of one hard negative. The hard negatives
illustrate the dominant “same industry, different company” bucket of Section 3.7.
Accounting interpretation JNJ,202510-K·Accounting·Hard·Qualitative
Q.HowdoJohnson&Johnson’stangibleandintangibleassetscontributedifferentlytotheCompany’sabilitytogeneraterevenue
andsustaincompetitiveness,andwhatdoesthisimplyaboutfuturebusinessrisksandstrategicpriorities?
Reference answer.Johnson&Johnson’stangibleassets,suchasmanufacturingfacilitiesandequipment,areusedefficiently,asseen
inthehigherPPEturnoverratio. ThisshowsthattheCompanyeffectivelyleveragesitsphysicalassetbasetosupportlarge-scale
productionanddistribution. However,thebalancesheetisfarmoreheavilyweightedtowardin...
Supporting passage(p.44).Johnson&JohnsonandsubsidiariesconsolidatedbalancesheetsAtDecember29,2024andDecember
31, 2023 (Dollars in Millions Except Share and Per Share Amounts) (Note 1) 2024 2023 Assets Current assets Cash and cash
equivalents...
19

Hard negative(PFE,202510-K).ConsolidatedBalanceSheetsPfizerInc. andSubsidiaryCompanies(MILLIONS,EXCEPTPER
SHAREDATA)AssetsAsofDecember31,20242023Cashandcashequivalents$1,043$2,853Short-terminvestments...
Risk-disclosure comparison JNJ,202510-K·Risk·Hard·Qualitative
Q.WhattypesofcostsdoesJohnson&Johnsonreportinitsfootnotesthatillustraterisksfromsuddenmarketshifts,andhowdid
theCOVID-19vaccinemanufacturingexitgeneratesuchcosts?
Reference answer.Initsfootnotes,Johnson&Johnsondisclosesavarietyofcoststhatarisewhenmarketsorbusinessconditions
change,suchaslitigationcharges,restructuringcosts,impairmentofacquiredassets,acquisitionandintegrationexpenses,divestiture-
relatedlosses,andregulatorycompliancecharges. Theseitemsshowhowrapidlyevolvingm...
Supporting passage (p. 88-89). (3) Innovative Medicine segment income before tax includes: • Acquired in-process research
& development expense of $ 1.25billion to secure the global rights to the NM26 bispecific antibody (Yellow Jersey acquisition) •
Monetizati...
Hard negative(LLY,202510-K).Numbersmaynotaddduetorounding. (1)JardiancerevenueincludesGlyxambi,Synjardy,and
TrijardyXR.(2)Humalogrevenueincludesinsulinlispro. (3)BasaglarrevenueincludesRezvoglar. (4)Olumi...
Quantitative extraction JNJ,202510-K·Financials·Hard·Quantitative
Q.WhatwasJohnson&Johnson’sfreecashflowtothefirm(FCFF)in2024,basedonthereportedfinancials?
Reference answer.Freecashflowtothefirmiscalculatedbystartingfromoperatingprofitaftertaxandadjustingfornon-cash
charges,capitalexpenditures,andworkingcapitalmovements. ThecompanyreportedEBITof20,804millionandwithaneffective
taxrateof15.7%thisresultsinaNOPATof17,536million. Depreciationandamortizationaddedbac...
Supportingpassage(p.45).Johnson&Johnsonandsubsidiariesconsolidatedstatementsofearnings(DollarsandSharesinMillions
ExceptPerShareAmounts)(Note1)202420232022Salestocustomers$88,82185,15979,990Costofproductssold27,47126,553...
Hard negative(LLY,202510-K).ELILILLYANDCOMPANYANDSUBSIDIARIES¡divalign=’center’¿(Dollarsinmillions,
exceptper-sharedata,andsharesinthousands)¡/div¿YearEndedDecember31,202420232022Revenue(Note2)$45,042....
Business-segment identification JNJ,202510-K·CompanyOverview·Hard·Qualitative
Q.Howhasthecompanyrestructureditsbusinessareasinrecentyears,andwhatstrategicrationalecanbederivedfromitscurrent
focusontwosegments?
Referenceanswer.Johnson&JohnsonhasrestructureditsbusinessinrecentyearsbyfullyseparatingitsConsumerHealthsegment
through a three-step process: the Kenvue IPO in May 2023, an August 2023 exchange offer reducing ownership to 9.5%, and a
debt-for-equityexchangeinQ22024thateliminatedtheremainingstake. Whiletransitionmanufacturingan...
Supporting passage(p.50).OnMay8,2023,Kenvue,completedaninitialpublicoffering(theIPO)resultingintheissuanceof
198,734,444sharesofitscommonstock,parvalue$0.01pershare(the“KenvueCommonStock”),ataninitialpublicofferingof$2...
Hard negative(LLY,202510-K).DivestituresOlanzapinePortfolio(includingZyprexa)InJuly2023,wesoldtherightsforthe
olanzapineportfolio,includingZyprexa,toCheplapharmArzneimittelGmbH(Cheplapharm),aEuropeancompa...
Legal / regulatory interpretation ABBV,202510-K·Legal·Hard·Qualitative
Q.HowdoAbbVie’sinheritedAllerganlitigations,combinedwiththefinancialaftermathofdivestedassetsandintegrationcosts,
illustratethelegalandstrategicrisksthatfollowfromlarge-scaleacquisitions?
Reference answer.AbbVie’sacquisitionofAllerganshowshowlegalexposurescanextendwellbeyondthetransactiondateand
shapethecompany’sfinancialriskprofile. Thecompanyinheritedhundredsoflawsuits,includingopioidlitigationandbreastimplant
cases,whereplaintiffsseekcompensatoryandpunitivedamages,medicalmonitoring,andotherreme...
Supporting passage(p.96-97).GovernmentProceedingsLawsuitsarependingagainstAllerganandseveralothermanufacturers
generallyallegingthattheyimproperlypromotedandsoldprescriptionopioidproducts. Approximately435lawsuitsarepending
againstAll...
Hard negative(JNJ,202510-K).TheCompanyissubjecttosignificantlegalproceedingsthatcanresultinsignificantexpenses,
finesandreputationaldamage. Intheordinarycourseofbusiness,Johnson&Johnsonanditssubsidiari...
Shareholder-return analysis LLY,202510-K·ShareholderReturn·Hard·Quantitative
Q.HowcloselydoesEliLilly’sstockperformancealignwithitsrevenueandEPSgrowthtrajectory,andwhatexplainsanydivergence?
Reference answer.EliLilly’sstockperformancehasoutpacedbothrevenueandEPSgrowthinrecentyears. Revenueincreasedby
20%in2023andby32%in2024,whiledilutedEPSdeclinedby16%in2023duetohigherinternalandacquiredR&Dexpenses
beforereboundingwith102%growthin2024. Bycontrast,thestockdeliveredannualizedgainsofmorethan4...
Supporting passage(p.40).ThefollowinggraphcomparesthereturnonLillystockwiththatoftheStandard&Poor’s(S&P)
500StockIndexandourpeergroupfortheyears2020through2024. Thegraphassumesthat,onthelastbusinessdayof2019,a
person...
20

Hard negative(JNJ,202510-K).Johnson&Johnsonandsubsidiariesconsolidatedstatementsofearnings(DollarsandSharesin
MillionsExceptPerShareAmounts)(Note1)202420232022Salestocustomers$88,82185,15979,990Costo...
F Example Prompt Templates
We provide example prompt templates for three evaluation modes; benchmark consumers should report the exact
prompts used (including system prompts and any few-shot exemplars) alongside their results.
F.1 LLM-Based QA Prompt
You are a financial analyst answering a question about a company’s
SEC filing. Use only the information in the provided passages. If
the passages do not contain enough information to answer the
question, respond that the answer is not available in the
provided passages.
Question: {question}
Passages:
{passages}
Answer:
F.2 RAG-with-Citations Prompt
You are a financial analyst answering a question about a company’s
SEC filing. Use only the information in the provided passages. For
every claim in your answer, cite the passage that supports it
using its number, in square brackets, e.g. [1], [2]. Do not
include claims that are not supported by the provided passages.
Question: {question}
Passages:
[1] {passage_1}
[2] {passage_2}
...
Answer with citations:
F.3 Hard-Negative Discrimination Prompt
You are evaluating which passages from a candidate set support
the answer to a financial question about an SEC filing. Read the
question and the candidate passages and assign each passage one
of two labels:
- SUPPORTING: the passage contains evidence that directly
supports an answer to the question.
- NON-SUPPORTING: the passage does not directly support an
answer to the question, even if it is topically related.
Return your decisions as a list of (passage_id, label) pairs.
Question: {question}
21

Candidate passages:
[1] {passage_1}
[2] {passage_2}
...
Decisions:
| G Reproducibility | Notes |     |     |     |     |
| ----------------- | ----- | --- | --- | --- | --- |
In addition to the checklist in Section 6, studies should release the exact split files (record ids per partition) rather
than describing splits in prose only, report whether and how the normalization of Section 3.8 was applied (with raw
and normalized counts for each affected field), report the verbatim prompts used by any LLM-based component,
describe how the retrieval corpus was assembled (in-record passages and hard negatives only, or a broader corpus
from the underlying filings), and document model versions, decoding settings, and hardware to support replication.
Auditability of the question set. Future users should be able to regenerate or audit the dataset using the
methodology document (Appendix A), the question-generation criteria (Section 3.2), the released FinRank.jsonl,
the per-passage identifiers, text hashes, and inline <field> raw values it carries, the query rewrite arrays, the
machine-readable repair log of the normalization pipeline, and the evaluation scripts in baselines/. Pairing the
methodology with the realized distribution (Table 2) is what allows a third party to detect divergence from the
documented criteria without having to rederive them from scratch; it makes the benchmark more transparent and
reduces ambiguity in question design, while not substituting for the question-by-question correctness audit listed in
Section 9.
| H Cross-Tabulation |     | Tables |     |     |     |
| ------------------ | --- | ------ | --- | --- | --- |
The following cross-tabulations of the FinRank metadata are useful for diagnosing where future model perfor-
mance is likely to be most variable. All counts are computed on the canonical normalized labels (Section 3.8)
by baselines/make crosstabs.py; per-row and per-column totals match the marginal distributions reported in
Section 4.
Industry Accounting CompanyOverview Financials Footnotes Governance Legal Risk ShareholderReturn Rowtotal
| Automotive      | 35  | 33  | 32 23   | 27 30 36    | 32 248   |
| --------------- | --- | --- | ------- | ----------- | -------- |
| Oil&Gas         | 60  | 55  | 53 57   | 55 55 51    | 52 438   |
| Pharmaceuticals | 63  | 65  | 67 62   | 59 61 63    | 59 499   |
| Columntotal     | 158 | 153 | 152 142 | 141 146 150 | 143 1185 |
Table 13: Cross-tabulation of industry by topic on the canonical normalized labels.
|     |     | Industry        | 10-K 10-Q | Row total |     |
| --- | --- | --------------- | --------- | --------- | --- |
|     |     | Automotive      | 248       | – 248     |     |
|     |     | Oil & Gas       | 301 137   | 438       |     |
|     |     | Pharmaceuticals | 499       | – 499     |     |
|     |     | Column total    | 1048 137  | 1185      |     |
Table 14: Cross-tabulation of industry by document type on the canonical normalized labels.
Observations. The (industry × topic) cross-tab (Table 13) shows that all three industries populate every topic
bucket, with no empty cell; Automotive cells are smaller in absolute terms because Automotive has half as many
recordsasPharmaceuticalsorOil&Gas. The(year×doc type)cross-tab(Table15)confirmsthatthe10-Qpartition
is concentrated in a single filing year, so per-year and per-doc type analyses are not independent. The (difficulty
× reasoning type) and (passage type × reasoning type) cross-tabs (Tables 17, 16) expose where the roughly 2:1
22

|     |     |     |     | Filing | year  | 10-K | 10-Q | Row | total |
| --- | --- | --- | --- | ------ | ----- | ---- | ---- | --- | ----- |
|     |     |     |     | 2024   |       | 283  |      | 13  | 296   |
|     |     |     |     | 2025   |       | 765  | 124  |     | 889   |
|     |     |     |     | Column | total | 1048 | 137  |     | 1185  |
Table 15: Cross-tabulation of filing year by document type on the canonical normalized labels. The Unknown entry is
a record whose raw doc type names multiple source documents and cannot be attributed to a single filing.
|     |     |     | Passage        | type  | Qualitative |     | Quantitative |     | Row total |
| --- | --- | --- | -------------- | ----- | ----------- | --- | ------------ | --- | --------- |
|     |     |     | Single-Passage |       |             | 276 |              |     | 133 409   |
|     |     |     | Two-Passage    |       |             | 322 |              |     | 150 472   |
|     |     |     | Multi-Passage  |       |             | 211 |              |     | 93 304    |
|     |     |     | Column         | total |             | 809 |              |     | 376 1185  |
Table 16: Cross-tabulation of passage type by reasoning type on the canonical normalized labels.
|     |     |     | Difficulty |       | Qualitative |     | Quantitative |     | Row total |
| --- | --- | --- | ---------- | ----- | ----------- | --- | ------------ | --- | --------- |
|     |     |     | Easy       |       |             | 229 |              |     | 134 363   |
|     |     |     | Medium     |       |             | 348 |              |     | 136 484   |
|     |     |     | Hard       |       |             | 232 |              |     | 106 338   |
|     |     |     | Column     | total |             | 809 |              |     | 376 1185  |
Table 17: Cross-tabulation of difficulty by reasoning type on the canonical normalized labels. The qualitative-to-
| quantitative | skew is | present | at every | difficulty | level. |     |     |     |     |
| ------------ | ------- | ------- | -------- | ---------- | ------ | --- | --- | --- | --- |
qualitative-to-quantitative skew of Section 4 is most pronounced; consumers who report difficulty- or passage-type-
stratified metrics should also report the corresponding qualitative/quantitative split rather than assume it matches
| the dataset-level | marginal. |     |     |     |     |     |     |     |     |
| ----------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| I Dataset         | Card      |     |     |     |     |     |     |     |     |
Identity. Name: FinRank. Distribution: https://github.com/datanxt/FinRank. Distribution file:
FinRank.jsonl, carrying the canonical labels of Section 3.8 with raw surface forms preserved inline in
<field> raw
fields.
Contents. 1185 question–answer records derived from the 10-K and 10-Q filings of 22 publicly listed companies
(three sectors, 8 topical labels, filing years 2024–2025). Each record contains a question, a reference answer, optional
query rewrites, structured metadata, an array of supporting passages, and an array of hard negative passages. The
release additionally includes a deduplicated global pooled retrieval corpus of 5230 unique passages (see Section 3.6).
Intended use. Benchmarking financial information-retrieval and question-answering systems on SEC-filing prose,
with explicit support for retrieval, reranking, hard-negative discrimination, multi-passage reasoning, query rewriting,
| and retrieval-augmented |     | generation |     | with citations. |     |     |     |     |     |
| ----------------------- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- |
Prohibited use. Automated investment decisions, automated trading signals, real-time valuation, regulatory or
compliance decisions, or any high-stakes financial action without independent human oversight. Outputs of any
systemevaluatedonFinRankmustnotbepresentedasfinancialadvice. Referenceanswersreflectaparticularreading
of forward-looking, ranged, or conditional disclosure language and are not guaranteed to be correct in all financial
respects.
Known issues. Label inconsistencies in the raw release (Section 4.1); distributional skews along industry, year,
documenttype,andreasoningtype(Section4);hard-negativecontaminationof442HNsacross305records(Section3.7);
| no independent | ground-truth |     | audit | performed | in this | paper, | see | Section | 9.  |
| -------------- | ------------ | --- | ----- | --------- | ------- | ------ | --- | ------- | --- |
23

Recommended evaluation practice. Usethereleasedcanonicallabelsforallmetriccomputation; reportretrieval
metrics on the global pool C and reranking / hard-negative metrics on the in-record set L r ; report stratified results
in addition to aggregate results (see Section 7.4); report the random seed and the exact split used; and accompany
generative answer-quality results with faithfulness and citation-accuracy numbers in addition to EM/F1/ROUGE-
L/BERTScore.
License. FinRank is released under the Creative Commons Attribution-NonCommercial 4.0 International license
(CC BY-NC 4.0). Academic and educational use is permitted with attribution; commercial licensing is available
from the authors on request. The underlying SEC filings are public records; FinRank redistributes only derived
| question–answer | records, | supporting   | passages, | and hard negatives. |     |
| --------------- | -------- | ------------ | --------- | ------------------- | --- |
| J Baselines     |          | Reproduction |           |                     |     |
The retrieval, reranking, hard-negative, and ablation results in Section 7 are produced by the scripts in baselines/.
| The complete | pipeline | is: |     |     |     |
| ------------ | -------- | --- | --- | --- | --- |
cd FinRank/baselines
| pip install | -r requirements.txt |     |        |                  |     |
| ----------- | ------------------- | --- | ------ | ---------------- | --- |
| python      | validate_release.py |     | --data | ../FinRank.jsonl |     |
python run_baselines.py --data ../FinRank.jsonl --out results/
python run_extra_retrievers.py --data ../FinRank.jsonl --out results/
python make_splits.py --data ../FinRank.jsonl --out splits.json
| python       | make_crosstabs.py    |                    | --data | ../FinRank.jsonl    | --out ../ |
| ------------ | -------------------- | ------------------ | ------ | ------------------- | --------- |
| python       | make_macros.py       |                    | --data | ../FinRank.jsonl    | \         |
| --results    | results/results.json |                    | \      |                     |           |
| --repair-log |                      | ../repair_log.json | --out  | _results_macros.tex |           |
| Models       | and seeds:           |                    |        |                     |           |
•
| Random  | seed: 42   | (random-negative | sampling). |     |           |
| ------- | ---------- | ---------------- | ---------- | --- | --------- |
| • Dense | retriever: |                  |            |     | (∼420MB). |
sentence-transformers/all-mpnet-base-v2
| • Cross-encoder: |     |     |     |     | (∼80MB). |
| ---------------- | --- | --- | --- | --- | -------- |
cross-encoder/ms-marco-MiniLM-L-6-v2
• Sparse: with default parameters; scikit-learn with sublinear TF and
|         | rank-bm25 | BM25Okapi |     |     | TfidfVectorizer |
| ------- | --------- | --------- | --- | --- | --------------- |
| unigram | features. |           |     |     |                 |
•
Tokenization for sparse baselines: lowercase + punctuation stripping (regex [^a-z0-9]+).
Runtimeexpectations: onasingleA10GGPUthefullharness(run baselines.py)completesinunderfiveminutes
and the additional dense retrievers (run extra retrievers.py, including the 7B e5-mistral) in roughly ten; on
a CPU-only laptop the mpnet/cross-encoder harness takes about an hour, and the 7B model is impractical. Score
matrices are cached to baselines/results/score cache.npz so repeated runs do not re-encode the corpus.
24
---- END DOCUMENT ----
