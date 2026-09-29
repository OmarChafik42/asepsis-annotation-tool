Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
HexEval: An Evidence-Driven Hexagonal Framework for Multidimensional
|     |     |     |     | Scholar | Assessment |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
XiaokangQu1,YitingLin1
1SchoolofCyberScienceandTechnology,UniversityofScienceandTechnologyofChina
Hefei,Anhui,China
xkqu@mail.ustc.edu.cn,linyiting@mail.ustc.edu.cn
|     |     | Abstract |     |     |     | Traditional Scholar Assessment |     |     | HexEval |     |
| --- | --- | -------- | --- | --- | --- | ------------------------------ | --- | --- | ------- | --- |
Scholarassessmentplaysafundamentalroleinfacultyrecruit- ScholarRecordsandReputationPeoxies RepresentativeWorks ExternalEvidence
ment,fundingallocation,academicpromotion,andtalentdis-
| covery. Existing | scholar | assessment | methods | predominantly |     |                                  |     |                  |                    |     |
| ---------------- | ------- | ---------- | ------- | ------------- | --- | -------------------------------- | --- | ---------------- | ------------------ | --- |
|                  |         |            |         |               |     | Metrics-BasedFeatureConstruction |     | QualityReasoning | BehaviorAssessment |     |
relyonbibliometricindicatorsandreputationproxies,while
recentlargelanguagemodel(LLM)-basedapproachesmainly
focus on evaluating individual research papers rather than WeightedAggregationorRanking D1 D2 D3 D4 D5 D6
6202 guA 21  ]IA.sc[  2v48501.8062:viXra
| comprehensively | assessing | scholars. | We  | argue that | scholar |     |     |     |     |     |
| --------------- | --------- | --------- | --- | ---------- | ------- | --- | --- | --- | --- | --- |
assessmentshouldbeformulatedasanevidence-drivenrea-
|     |     |     |     |     |     | SingleOverallScore/Ranking |     | Six-DimensionalScholarProfile |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | ----------------------------- | --- | --- |
soningproblemthatjointlyconsidersintrinsicresearchquality
andexternallyverifiablescholarlybehavior.Tothisend,we • Proxy-driven • Scalar • Evidence-driven • Multidimensional
proposeHexEval,anevidence-drivenhexagonalframework • Aggregated • Limited traceability • Dimension-specific • Traceable
formultidimensionalscholarassessment.HexEvalexplicitly
organizes scholar assessment into two complementary evi- Figure 1: Paradigm comparison between conventional
dence layers. The intrinsic layer evaluates anonymized rep- scholar assessment and HexEval. Conventional approaches
resentative works along three dimensions, namely research aggregatemetric-basedfeaturesintoasinglescoreorrank-
rigor,methodologicalinnovation,andscientificcontribution, ing,whereasHexEvalevaluatesintrinsicresearchqualityand
whereas the external layer characterizes scholars through externalscholarlyevidenceseparatelytoproduceatraceable
knowledgetranslation,researchcoherence,andacademicim-
six-dimensionalprofile.
| pact using         | heterogeneous | evidence         | collected  | from     | GitHub, |     |     |     |     |     |
| ------------------ | ------------- | ---------------- | ---------- | -------- | ------- | --- | --- | --- | --- | --- |
| Lens, OpenAlex,    | and           | other publicly   | verifiable | sources. | In-     |     |     |     |     |     |
| stead of producing |               | opaque aggregate | scores,    | HexEval  | pre-    |     |     |     |     |     |
advantage,andreputationeffects(Merton1968;Hicksetal.
| serves intermediate |     | evidence, | dimension-specific | rationales, |     |     |     |     |     |     |
| ------------------- | --- | --------- | ------------------ | ----------- | --- | --- | --- | --- | --- | --- |
2015).
| and verification | signals | throughout | the | evaluation | process, |     |     |     |     |     |
| ---------------- | ------- | ---------- | --- | ---------- | -------- | --- | --- | --- | --- | --- |
enablinginterpretableandauditablescholarprofiles.Exper- Recentlargelanguagemodels(LLMs)haveenabledstruc-
imentsacrossallsixdimensionsshowdimension-dependent tured scientific-document understanding and paper-level
agreement with human or external reference criteria: struc- qualityassessmentwithencouragingagreementwithhuman
tured calibration improves absolute agreement for intrinsic judgments(Thelwall2024,2025).However,scholarassess-
quality, while the external modules recover broad trajectory ment requires reasoning over broader evidence, including
| and ordinal | impact | signals. These | results | support evidence- |     |     |     |     |     |     |
| ----------- | ------ | -------------- | ------- | ----------------- | --- | --- | --- | --- | --- | --- |
representativeworks,long-termresearchtrajectories,knowl-
drivenreasoningoverheterogeneousscholarlyevidenceasa
|     |     |     |     |     |     | edge translation, | and scholarly | impact. | Paper-level | content |
| --- | --- | --- | --- | --- | --- | ----------------- | ------------- | ------- | ----------- | ------- |
promisingparadigmforauditableAI-assistedscholarassess-
reasoningandscholar-levelmetricaggregationthereforere-
ment,whileexposingthecoverageandattributionlimitations
mainlargelydisconnected.
ofpublicscholarlydata.
|     |     |     |     |     |     | We reformulate | scholar | assessment | as a dual-layer | evi- |
| --- | --- | --- | --- | --- | --- | -------------- | ------- | ---------- | --------------- | ---- |
dencereasoningproblem.AsillustratedinFigure1,thein-
Introduction
trinsiclayerevaluateswhetherrepresentativeresearchisrig-
Scholarassessmentsupportsfacultyrecruitment,fundingal- orous,innovative,andscientificallyvaluable,whiletheexter-
location, academic promotion, award nomination, and tal- nallayercharacterizeshowresearchistranslated,sustained,
entdiscovery.Existingmethodspredominantlyrelyonbib- and recognized in the scholarly ecosystem. This separation
liometric indicators such as citation counts, publication distinguishesscientificmeritfromdownstreaminfluenceand
numbers,h-index,field-normalizedmetrics,andpublication producesmoreinterpretableevaluationresults.
venues (Hirsch 2005; Hicks et al. 2015). Although useful Based on this formulation, we propose HexEval, an
for measuring scholarly visibility and influence, these indi- evidence-driven hexagonal framework that represents each
catorsmainlycaptureresearchoutcomesratherthanintrinsic scholar through six dimensions. The intrinsic layer evalu-
research quality. They are also affected by field-specific ci- ates anonymized representative works in terms of research
tation practices, academic age, venue prestige, cumulative rigor,methodologicalinnovation,andscientificcontribution.

Theexternallayerevaluatesknowledgetranslation,research Existing methods remain output-centered and do not
coherence,andacademicimpactusingpubliclyverifiableev- jointly represent representative-work quality, research tra-
idencefromGitHub,Lens,andOpenAlex(Priem,Piwowar, jectories, knowledge translation, and impact. HexEval in-
andOrr2022).Eachdimensionusesitsownevidencesource, steadtreatsthescholarasthetargetandpreservesdimension-
scoringprocedure,andevaluationprotocol,whilepreserving specificevidencetraces.
intermediateevidence,rationales,andverificationsignalsfor
| auditing. |     |     |     |     |     |     | Evidence-GroundedAssessment |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
Themaincontributionsare: Evidence-grounded methods support judgments with in-
•
We formulate automated scholar assessment as a dual- spectable information and sources. Retrieval-augmented
layerevidencereasoningproblemthatseparatesintrinsic generation connects LLMs to external knowledge (Lewis
research quality from externally verifiable scholarly be- etal.2020),whileevidentiality-guidedgenerationmodelsev-
| havior. |     |     |     |     |     |     | idencerelevanceandsupport(Asai,Gardner,andHajishirzi |     |        |          |      |     |           |       |
| ------- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | ------ | -------- | ---- | --- | --------- | ----- |
|         |     |     |     |     |     |     | 2022); retrieval                                     |     | alone, | however, | does | not | guarantee | valid |
• WeproposeHexEval,asix-dimensionalframeworkthat
| independently |     | evaluates | research | rigor, | methodological |     | support.   |       |              |     |          |            |          |     |
| ------------- | --- | --------- | -------- | ------ | -------------- | --- | ---------- | ----- | ------------ | --- | -------- | ---------- | -------- | --- |
|               |     |           |          |        |                |     | Scientific | claim | verification |     | combines | retrieval, | support- |     |
innovation,scientificcontribution,knowledgetranslation,
|     |     |     |     |     |     |     | /refutation | classification, |     | and | rationale | extraction, |     | as in |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | --- | --------- | ----------- | --- | ----- |
researchcoherence,andacademicimpactwhilepreserv-
|     |     |     |     |     |     |     | SciFact | and its | extensions | (Wadden |     | et al. | 2020, | 2022). |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---------- | ------- | --- | ------ | ----- | ------ |
ingauditableevidence.
| •           |     |          |        |            |           |      | Attribution-oriented |          | methods     | such | as     | RARR | retain | source |
| ----------- | --- | -------- | ------ | ---------- | --------- | ---- | -------------------- | -------- | ----------- | ---- | ------ | ---- | ------ | ------ |
| We evaluate |     | D1–D5 on | public | or curated | reference | data |                      |          |             |      |        |      |        |        |
|             |     |          |        |            |           |      | links while          | revising | unsupported |      | claims | (Gao | et al. | 2023). |
andoperationalizeD6usingthereproducibleOpenAlex
|     |     |     |     |     |     |     | These works | establish | evidence–claim |     |     | alignment | and | attri- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | -------------- | --- | --- | --------- | --- | ------ |
h-index,withexplicitreportingofevidencecoverage,at-
butionasrequirementsforauditability(JacoviandGoldberg
tribution,sampling,andsourcelimitations.
2020).
|     |     |     |     |     |     |     | These | methods | mainly | address | QA, | factual | generation, |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------ | ------- | --- | ------- | ----------- | --- |
RelatedWork
orclaim/documentverification.Scholarassessmentrequires
Scholar-LevelResearchAssessment reasoning over works, career stages, artifacts, and impact
channels;HexEvalextendsevidence-groundedreasoningto
| Scholar-level | assessment |     | traditionally | relies | on publication |     |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ------------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thissettingwithinspectablepapers,software/patentrecords,
| counts, | citations, | the h-index, | and | field-normalized |     | mea- |     |     |     |     |     |     |     |     |
| ------- | ---------- | ------------ | --- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
sures (Hirsch 2005; Radicchi, Fortunato, and Castellano trajectories,andcitationtraces.
| 2008); later | work | adds topics, | authorship, |     | time, collabora- |     |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------------ | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
HexEvalFramework
tion,venue,andexpertinterpretation(Xieetal.2021;Gor-
raiz,Gumpenberger,andSchloegl2016). FrameworkOverviewandDataFlow
| These | indicators | capture | productivity | and | accumulated |     |     |     |     |     |     |     |     |     |
| ----- | ---------- | ------- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
visibilitymoredirectlythanintrinsicquality,andareaffected HexEval represents a scholar by scientific outputs and ex-
ternallyobservablescholarlytraces.Letsdenoteascholar,
byfieldpractices,careerlength,coverage,authorship,andcu-
|                                                    |     |     |     |     |     |     | P the supplied |     | representative |     | works, | and | I the identity |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | ------ | --- | -------------- | --- |
| mulativeadvantage(Merton1968;Hicksetal.2015).Their |     |     |     |     |     |     | s              |     |                |     |        |     | s              |     |
metadatarequiredbyattribution-dependentdimensions.The
| association | with | peer judgment | is  | field-dependent |     | (Wainer, |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------------- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
frameworkproduces
| Brahim, | and Richard | 2013; | Thelwall | 2023); | responsible- |     |     |     |     |     |     |     |     |     |
| ------- | ----------- | ----- | -------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assessmentguidelinesthereforetreatthemascontextrather
than substitutes for qualitative evidence (Hicks et al. 2015; H(s)=[D (s),D (s),D (s),D (s),D (s),D (s)],
|     |     |     |     |     |     |     |     | 1   | 2   | 3   | 4   |     | 5 6 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Pontikaetal.2022).
(1)
Thefirstthreedimensionsmeasureintrinsicresearchqual-
LLM-BasedResearchEvaluation
ityandthelastthreemeasureexternallyobservablescholarly
LLMs now assist peer review through critique generation, behavior. Intrinsic scores use anonymized works; external
methodologicaldiagnosis,scoreprediction,andreviewim- scoresuseidentity-linkedevidence.Thetwopathsarethere-
provement.Theirplausibleoutputsremainlimitedbylong-
forecomplementarybutnotsubstitutable.
documentunderstanding,paper-specificcriticism,technical As summarized in Figure 2, each dimension has its own
error detection, and score reliability (Zhou et al. 2024; Du input schema, prompt or deterministic computation, score
etal.2024).Structuredrubrics,retrieval,multi-stagereason- scale,andevidencerecord.HexEvaldoesnotimposeauni-
ing,andagentsimproveconsistency(Jinetal.2024;Zhuetal.
versalweightedsum;itreturnstheprofileandevidencepack-
| 2025), but | deployment | evidence |     | favors reviewer |     | assistance |     |     |     |     |     |     |     |     |
| ---------- | ---------- | -------- | --- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
age
overautonomousdecisions(Thakkaretal.2025).
Direct quality estimation shows weak-to-moderate and O(s)={H(s),E (s),...,E (s),
|     |     |     |     |     |     |     |     |     |     |     | 1   | 5   |     | (2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
field-dependentagreementwithhumanjudgments;repeated
|                                                      |     |     |     |     |     |     |     |     | E   | (s),V(s)}, |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
| sampling,promptdesign,andinputselectionmateriallyaf- |     |     |     |     |     |     |     |     |     | 6          |     |     |     |     |
fectresults(Thelwall2024,2025;ThelwallandYaghi2024). whereE (s)containsinputs,structuredoutputs,rationales,
i
Relatedworkalsoconsidersresearchenvironmentsandso- andsourcemetadata,andV(s)containsvalidation,coverage,
cietalvalue(Kousha,Thelwall,andGadd2025;Nunkooand anduncertaintyinformation.Anydownstreamaggregationis
Thelwall2026). application-specificandisnotpartofthedefaultoutput.

Forvisualizationonly,adimensionscorecanbemapped IntrinsicResearchQualityAssessment
| fromitsnativescale[l |     | ,u ]toapercentage: |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i i TheintrinsicpathwayreceivesonlyP(cid:101)s ={p ,...,p }.For
|     |     |     |     |     |     |     |     |     |     |     |     |     | (cid:101)1 | (cid:101)ns |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- |
dimensiond∈{1,2,3}andpaperp,theLLMreturnsadirect
D (s)−l score q d,p , subdimension scores, rationale, and diagnostic
| D¯  |     | i   | i,  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i (s)=100 l i ≤D i (s)≤u i . (3) evidence. Identity, institution, venue, citations, and author
|     |     | u −l |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i i metadata are excluded. The scholar-level direct score is the
meanovervalidworks,
Thisaffinemappingdoesnotmakethedimensionscom-
mensurateinasubstantivesenseanddoesnotdefineaglobal
|                                 |     |     |     |     |     |     |     |     |              |     | 1   | (cid:88) |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | -------- | --- | --- | --- |
| scholarranking.Weusethenotation |     |     |     |     |     |     |     |     | D direct(s)= |     |     |          | q   | .   | (6) |
|                                 |     |     |     |     |     |     |     |     | d            |     |     |          | d,p |     |     |
|Pvalid|
|     |     |     |     |     |     |     |     |     |     |     | s   | p∈Pvalid |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
s
L(x;c)=min(1,ℓ(x;c)), Thethreedimensionsarenotcollapsedintooneintrinsic
log(1+x) score. With human labels, a dimension-specific Ridge cali-
ℓ(x;c)= , brator is fitted for held-out validation. Let x contain the
|     |     | log(1+c)     |          |            |     |     |                             |              |     |     |        |         |       | d,p |       |
| --- | --- | ------------ | -------- | ---------- | --- | --- | --------------------------- | ------------ | --- | --- | ------ | ------- | ----- | --- | ----- |
|     |     |              |          |            |     | (4) | LLM                         | subdimension |     | and | direct | scores, | and y | the | human |
|     |     |              | (cid:16) | r (cid:17) |     |     |                             |              |     |     |        |         |       | d,p |       |
|     |     |              |          | +          |     |     | score.Afterstandardization, |              |     |     |        |         |       |     |       |
|     |     | S(r;τ)=1−exp |          | − ,        |     |     |                             |              |     |     |        |         |       |     |       |
τ
|                                                        |     | r =max(r,0). |     |     |     |     |     |           |         | (cid:110) |     |     |      | (cid:111) |       |
| ------------------------------------------------------ | --- | ------------ | --- | --- | --- | --- | --- | --------- | ------- | --------- | --- | --- | ---- | --------- | ----- |
|                                                        |     | +            |     |     |     |     |     |           |         |           |     | β∥2 | ∥β∥2 |           |       |
|                                                        |     |              |     |     |     |     |     | β(cid:98) | =argmin | ∥y        | −X  |     | +λ   |           | , (7) |
|                                                        |     |              |     |     |     |     |     | d         |         |           | d   | d 2 | d    | 2         |       |
| forthelog-saturationandexponential-saturationfunctions |     |              |     |     |     |     |     |           |         | β         |     |     |      |           |       |
usedbytheexternalscoringmodules. whereλ isselectedonthecalibrationsplit.Thetestpre-
d
dictionis
Thefollowingsubsectionsspecifyanonymization,intrin-
sicrubricsandcalibration,andtheexternalsource,sampling,
|                      |     |     |     |     |     |     |     |     |     | y =clip     |                  |           |          |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------- | --------- | -------- | --- | --- |
| andaggregationrules. |     |     |     |     |     |     |     |     |     | (cid:98)d,p | [1,4]            |           |          |     |     |
|                      |     |     |     |     |     |     |     |     |     | (cid:16)    |                  |           | (cid:17) |     | (8) |
|                      |     |     |     |     |     |     |     |     |     |             | β(cid:98)d,0 +z⊤ | β(cid:98) | .        |     |     |
d,p d
Representative-WorkAnonymization
|     |     |     |     |     |     |     |     | The calibrator |     | is used | only | when | this | fitted | mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ---- | ---- | ---- | ------ | ------- |
Toreduceidentityandreputationcues,HexEvalmapseach is available; otherwise, the direct mean is retained. Thus,
representativePDFptoananonymizedMarkdowndocument benchmark calibration is not presented as an unsupervised
scoringrule.
p =A(p), (5) D1:Researchrigor. D1evaluateswhetherclaimsaresup-
(cid:101)
portedbysoundmethodsandevidence.Itssevencriteriaare
| where | A denotes | the | anonymization |     | and content- |     |                |     |           |     |          |           |     |            |     |
| ----- | --------- | --- | ------------- | --- | ------------ | --- | -------------- | --- | --------- | --- | -------- | --------- | --- | ---------- | --- |
|       |           |     |               |     |              |     | methodological |     | validity, |     | evidence | adequacy, |     | evaluation | de- |
preservationprocedure.ThePDFisconvertedtostructured
|     |     |     |     |     |     |     | sign, | comparisons |     | and controls, |     | statistical | or  | logical | rigor, |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ------------- | --- | ----------- | --- | ------- | ------ |
Markdownwhileretainingscientificcontent,includingequa- reproducibility and transparency, and limitation/claim cali-
tions,tables,figures,andcaptions.Rule-basedfiltersremove bration.Theoutputcontainscriterionrationalesandserious
| names, affiliations, |     | emails, acknowledgments, |     |     | funding, | and |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orminorweaknesses;unsupportedclaimsreducetherelevant
revealingcitationmetadata.AnLLMcleaningstageremoves
criterionratherthanincurareputation-basedpenalty.
| residual | institutional, | group, | project, | and acknowledgment |     |     |     |                |     |             |     |     |           |     |           |
| -------- | -------------- | ------ | -------- | ------------------ | --- | --- | --- | -------------- | --- | ----------- | --- | --- | --------- | --- | --------- |
| cues.    |                |        |          |                    |     |     | D2: | Methodological |     | innovation. |     | D2  | evaluates |     | original- |
ityintechnicalcontext.Themainbenchmarkpathreceives
| Methodological |     | details,    | settings, | formulations, |     | results, |           |     |           |               |     |                          |     |     |     |
| -------------- | --- | ----------- | --------- | ------------- | --- | -------- | --------- | --- | --------- | ------------- | --- | ------------------------ | --- | --- | --- |
|                |     |             |           |               |     |          | extracted |     | abstract, | introduction, |     | related-work/background, |     |     |     |
| limitations,   | and | conclusions | are       | retained.     | The | same     |           |     |           |               |     |                          |     |     |     |
anonymizeddocumentsaresuppliedtoD1–D3,whichusein- method, and conclusion sections from the anonymized pa-
dependentprompts,rubrics,extractionprocedures,andval- per, without identity or reputation cues. Its criteria are
|     |     |     |     |     |     |     | core | originality, | technical |     | distinctiveness, |     | nontriviality, |     | and |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --------- | --- | ---------------- | --- | -------------- | --- | --- |
idationprotocols.
|             |          |          |                   |            |       |       | novelty-claim |     | specificity. |     | The evaluator |     | distinguishes |             | new |
| ----------- | -------- | -------- | ----------------- | ---------- | ----- | ----- | ------------- | --- | ------------ | --- | ------------- | --- | ------------- | ----------- | --- |
| To audit    | residual | identity | leakage,          | we sampled | 100   | rep-  |               |     |              |     |               |     |               |             |     |
|             |          |          |                   |            |       |       | mechanisms    |     | from         | new | applications, |     | tuning,       | implementa- |     |
| resentative | works    | and used | DeepSeek-V4-Flash |            | as an | auto- |               |     |              |     |               |     |               |             |     |
matic detector for explicit identity-revealing cues, includ- tionchanges,andperformancegains.AnoptionalOpenAlex
prior-workmoderestrictscandidatestoworksbeforethetar-
| ing author | names, | affiliations, | contact | information, |     | fund- |     |          |        |      |         |          |            |     |     |
| ---------- | ------ | ------------- | ------- | ------------ | --- | ----- | --- | -------- | ------ | ---- | ------- | -------- | ---------- | --- | --- |
|            |        |               |         |              |     |       | get | year but | is not | used | for the | reported | benchmark. |     | The |
ing,acknowledgments,publicationmetadata,andidentifying
outputincludesthecentralmethodclaim,noveltytype,com-
| URLs. The | residual | leakage | rate decreased |     | from 0.53 | after |                       |     |     |     |     |     |     |     |     |
| --------- | -------- | ------- | -------------- | --- | --------- | ----- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|           |          |         |                |     |           |       | parisonrationale,andq |     |     |     | .   |     |     |     |     |
Stage 1 (MinerU conversion) to 0.52 after Stage 2 (regex- 2,p
basedcleaning),andfurtherto0inthissampledauditafter
|     |     |     |     |     |     |     | D3: | Scientific | contribution. |     |     | D3 measures |     | scientific | sig- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | --- | ----------- | --- | ---------- | ---- |
Stage3(LLManonymization). nificance and usefulness rather than method novelty alone.
Anonymizationmitigatesbutdoesnoteliminateleakage: Itscriteriaareproblemimportance,contributionsubstance,
method names, datasets, benchmarks, writing style, or dis- resultvalue,andgenerality/reusability.Theoutputcontains
tinctivecontributionsmayremainidentifying.Itistherefore the main contribution, strengths, serious and minor weak-
abias-mitigationmechanism,notaguaranteeofidentity-free nesses,rationale,andq 3,p ,allowingnarrowbutcorrectwork
| evaluation. |     |     |     |     |     |     | todifferfrombroadlyreusablework. |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

OriginalPDF Stage1:MinerUConversion Stage2:Regex-basedCleaning Stage3:LLMAnonymization FinalAnonymizedMarkdown
Paperfiles PDF→StructuredMarkdown Rule-basedDeletion LLM-basedAnonymization CleanMarkdownforD1-D3
|     |     |     | • Formula & Table Recognition |     |     | • Remove:identity-related  |     |     | • Identity cue detection  |     |     |     |     |     |     |     |
| --- | --- | --- | ----------------------------- | --- | --- | -------------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | • PreserveTitle/Abstract/Body |     |     | metadata...                |     |     | • Retrywithstricterprompt |     |     |     |     |     |     |     |
• Preserve scientific content
(a) Representative-Work Anonymization PDF
|     |     |     | D1:Rigor |     |     |     | Rubric |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Scoring
|     |     |      |               |     | Dimension-    |     |           |     | Sub-       |             |     |     |     |     |     |     |
| --- | --- | ---- | ------------- | --- | ------------- | --- | --------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
|     |     |      |               |     |               |     | Novelty   |     |            | Linear      |     |     |     |     |     |     |
|     |     |      | D2:Innovation |     | specific LLM  |     | Reasoning |     | dimensions | Calibration |     |     |     |     |     |     |
|     |     | .... |               |     | Reasoning     |     |           |     | Scores     |             |     |     |     |     |     |     |
Contribution
|     | Anonymized Works |     | D3:Contribution |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Reasoning
|     |     |     |     |     |     |     | Github/Lens |     | Evidence | Score  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
D4:Translation
|     |     |     |     |     |     |     | Retrieval |     | Verification | Computation |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
Name/ORCID
|     |     |     | D5:Coherence |     | Identity |     |           |     | Temporal | Trajectory |     |     |     |     |     |     |
| --- | --- | --- | ------------ | --- | -------- | --- | --------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
|     |     |     |              |     |          |     | OpenAlex  |     | Binning  | Reasoning  |     |     |     |     |     |     |
Resolution
|     | External Evidence |     | D6:Impact |     |     |     | Retrieval |     | Career  | Impact      |     |     |     |     |     |     |
| --- | ----------------- | --- | --------- | --- | --- | --- | --------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
|     |                   |     |           |     |     |     |           |     | Metrics | Aggregation |     |     |     |     |     |     |
(b) HexEval Assessment Pipeline
Figure 2: Overview of the HexEval framework. (a) Representative-work anonymization pipeline, where original papers are
convertedintostructuredMarkdownandprocessedthroughrule-basedfilteringandLLM-basedidentitycueremovaltoproduce
anonymizedrepresentativeworks.(b)Dual-pathscholarassessmentpipeline,whereanonymizedworksareevaluatedthrough
threeintrinsicdimensions(D1–D3),whileexternalscholarlyevidenceisanalyzedthroughthreeexternaldimensions(D4–D6).
Each dimension independently produces evidence-grounded scores and rationales, which are integrated into an interpretable
six-dimensionalscholarprofile.Theradarchartprovidesillustrativescholarprofilesratherthanexperimentalresults.
For all three dimensions, each saved score links to ex- 0.2forarchivedrepositories.Aselectedprojectreceives
| tracted paper | content, | subdimension |     | values, | and | rationale; |     |     |     |     |      |         |     |     |      |     |
| ------------- | -------- | ------------ | --- | ------- | --- | ---------- | --- | --- | --- | --- | ---- | ------- | --- | --- | ---- | --- |
|               |          |              |     |         |     |            |     |     |     |     | g =e | w (1+3I | ),  |     | (10) |     |
the scholar-level mean is therefore an aggregation of in- r r r r
spectablepaper-leveljudgments. where the implemented evidence weights are e = 1.0 for
r
|     |     |     |     |     |     |     |     | strong | community |     | evidence, | 0.6 | for moderate | community |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | --------- | --- | ------------ | --------- | --- | --- |
ExternalScholarlyBehaviorAssessment evidence,and0.45foraqualifyingpersonalrepository.The
|              |         |          |     |             |       |         |     | typeweightsarew |     |     | =1.20forcommunityprojects,1.00for |     |     |     |     |     |
| ------------ | ------- | -------- | --- | ----------- | ----- | ------- | --- | --------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
| The external | pathway | operates | at  | the scholar | level | because |     |                 |     |     | r                                 |     |     |     |     |     |
these dimensions describe observable scholarly behavior ordinarypersonalrepositories,and0.70forpersonalrepos-
ratherthanthequalityofanindividualpaper.Theevidence itories matching the low-value repository patterns. The top
sources,attributionchecks,andscoringrulesarekeptsepa- eight community projects and top ten personal repositories
| rateforeachdimension. |     |     |     |     |     |     |     | areretained,andT |     |     | (s)=S(G |     | ;12). |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------- | --- | ----- | --- | --- | --- |
|                       |     |     |     |     |     |     |     |                  |     |     | soft    | s   |       |     |     |     |
Foravalidatedpatentfamilyf,theimpacttermis
| D4:Knowledgetranslation. |     |     | D4measuresvalidatedtrans- |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lation of research into reusable software and patented or I =0.50L(citations ;100)+0.25L(familySize ;10)+0.25o ,
|     |     |     |     |     |     |     |     | f   |     |     | f   |     |     | f   |     | f   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
otherwise documented intellectual property. Software evi- (11)
|             |           |             |     |        |         |              |     | whereo |     | istheownershipscore.Thefamilyscoreis |        |               |      |     |      |     |
| ----------- | --------- | ----------- | --- | ------ | ------- | ------------ | --- | ------ | --- | ------------------------------------ | ------ | ------------- | ---- | --- | ---- | --- |
| dence is    | collected | from GitHub | and | public | project | records.     |     |        | f   |                                      |        |               |      |     |      |     |
| A community | project   | contributes |     | only   | when    | its evidence |     |        |     |                                      |        |               |      |     |      |     |
|             |           |             |     |        |         |              |     |        |     |                                      | g f =e | f (1.5b f +3I | f ), |     | (12) |     |
confidenceisstrongormoderate,itsrepositoryisreachable,
andthescholar’scontributorattributionisverified.Personal where b = 1.0 for a granted family and b = 0.6 other-
|     |     |     |     |     |     |     |     |     | f   |     |     |     |     | f   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
repositoriesarerestrictedtoowned,non-forkedrepositories wise,whilee = 1.0forstrongevidence,0.5formoderate
f
|     |     |     |     |     |     |     |     | evidence, |     | and 0 for | weak | or review-required |     | evidence. | The |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ---- | ------------------ | --- | --------- | --- | --- |
withatleast100stars.Patentcandidatesarededuplicatedinto
families;onlystrongormoderate,non-review-requiredfam- positivefamily-scoresumissaturatedasT pat (s)=S(P s ;8).
| ilies receive | positive | weight. | Weak, | unverified, |     | and review- |     | Thefinalscoreis |     |     |     |     |     |     |     |     |
| ------------- | -------- | ------- | ----- | ----------- | --- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
requireditemsremainintheaudittrailbutdonotcontribute
|             |     |     |     |     |     |     |     |     | D   | (s)=100[0.60T |     | (s)+0.40T |     | (s)]. | (13) |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ----- | ---- | --- |
| tothescore. |     |     |     |     |     |     |     |     |     | 4             |     | soft      |     | pat   |      |     |
Forarepositoryr,thesoftwareimpactis
|     |                |     |         |     |     |     |     | This | score    | represents | validated | translation   |     | evidence | rather    |     |
| --- | -------------- | --- | ------- | --- | --- | --- | --- | ---- | -------- | ---------- | --------- | ------------- | --- | -------- | --------- | --- |
|     |                |     |         |     |     |     |     | than | complete | individual |           | contribution. |     | Evidence | strength, |     |
|     | I =0.60L(stars |     | ;10000) |     |     |     |     |      |          |            |           |               |     |          |           |     |
r r attributionstatus,validationstatus,andsourceidentifiersare
(9)
|     | +0.30L(forks |     | ;3000)+0.10a |     |     | ,   |     | retainedforauditing. |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------------ | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |              |     | r            |     |     | r   |     |                      |     |     |     |     |     |     |     |     |
wherea r =1.0foractivitywithintwoyears,0.7foractivity D5: Research coherence. D5 estimates research coher-
threetofiveyearsold,0.4forolderorunknownactivity,and encefromasparsechronologicalsampleofascholar’sfuller

careertrajectory.Wereuse110preselectedcomputer-science Dim. Size Source Reference
scholarsandretrievetheirauthor-matchedOpenAlexpubli-
|                 |     |                 |         |     |         |           |     | D1  | 300 | OpenReview |     |     | Soundness |     |     |
| --------------- | --- | --------------- | ------- | --- | ------- | --------- | --- | --- | --- | ---------- | --- | --- | --------- | --- | --- |
| cation records. |     | The full-career | package | is  | divided | into five |     |     |     |            |     |     |           |     |     |
|                 |     |                 |         |     |         |           |     | D2  | 300 | OpenReview |     |     | Novelty   |     |     |
chronologicalbins.Papersentertheprimarycoherencecor-
|          |      |              |              |     |                |     |     | D3  | 300 | OpenReview    |     |     | Contribution    |     |     |
| -------- | ---- | ------------ | ------------ | --- | -------------- | --- | --- | --- | --- | ------------- | --- | --- | --------------- | --- | --- |
| pus only | when | year, title, | and abstract | are | all available; | ex- |     |     |     |               |     |     |                 |     |     |
|          |      |              |              |     |                |     |     | D4  | 90  | Publicrecords |     |     | Translationtier |     |     |
cludedrecordsremaindocumentedinthepackageaudittrail.
|                  |     |           |                |               |      |           |     | D5  | 110 | OpenAlex |     |     | Coherencescore |     |     |
| ---------------- | --- | --------- | -------------- | ------------- | ---- | --------- | --- | --- | --- | -------- | --- | --- | -------------- | --- | --- |
| The adjudicated  |     | reference | is constructed |               | from | the full- |     |     |     |          |     |     |                |     |     |
| career packages. |     | GLM       | and DeepSeek   | independently |      | score     |     |     |     |          |     |     |                |     |     |
Table1:SummaryoftheevaluationdatasetsforD1–D5.
| the five | coherence | dimensions: | thematic |     | consistency, | tem- |     |     |     |     |     |     |     |     |     |
| -------- | --------- | ----------- | -------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
poralcontinuity,main-threadclarity,related-branchintegra-
tion,andlowfragmentation.ChatGPTdoesnotproducean
independentscore;itactsonlyasananonymousjudgeofthe nical novelty and significance scores sampled by novelty
quartiles,andD3usescontribution-relatedannotations.
twoscoreroutputs.Thefinalreferencevalueisthemeanof
the five final adjudicated dimension scores and is referred ExternalScholarlyBehaviorDataset. D4–D5areevalu-
toasanadjudicatedmulti-LLMreferenceannotation,notas
|        |          |             |                  |     |       |          | ated      | at scholar |          | level because |      | they characterize |          | observable |        |
| ------ | -------- | ----------- | ---------------- | --- | ----- | -------- | --------- | ---------- | -------- | ------------- | ---- | ----------------- | -------- | ---------- | ------ |
| ground | truth. A | fixed 20/90 | development/test |     | split | is used, |           |            |          |               |      |                   |          |            |        |
|        |          |             |                  |     |       |          | scholarly |            | behavior | rather        | than | paper             | quality. | D4         | groups |
andthetestreferenceandsamplingmanifestarefrozenbe-
|     |     |     |     |     |     |     | scholars |     | into high, | middle, | and | low | translation | levels | us- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ------- | --- | --- | ----------- | ------ | --- |
foreevaluation. ingawardsandpubliclydocumentedsoftware/IPoutcomes.
Forthesparseevaluation,thesamemanifestsuppliesthree D5 uses author-matched OpenAlex publication corpora for
| papers per | bin, | or at most | 15 papers | per | scholar, | and each |     |     |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | --------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
preselectedcomputer-sciencescholars.Full-careerevidence
scholarisevaluatedoverfiverepeatedsamples.Theevaluator
packagesarescoredindependentlybyGLM-5.2(Z.ai2026),
| receives | only year, | title, | and abstract. | If  | c is the | overall |                                                  |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | ------------- | --- | -------- | ------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|          |            |        |               |     | s,j      |         | andDeepSeek-V4-Flash(DeepSeek-AI2026),andGPT-5.5 |     |     |     |     |     |     |     |     |
coherencescoreforrepeatj,thereportedpredictionis (OpenAI 2026) acts as an anonymous adjudicator of their
|     |     |     |     |     |     |     | outputs                                        | to  | produce | the | final coherence |     | references. |     | Evalua- |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | ------- | --- | --------------- | --- | ----------- | --- | ------- |
|     |     | 5   |     |     |     |     | tionusessparsechronologicalpublicationsamples. |     |         |     |                 |     |             |     |         |
1(cid:88)
| D (s)= |     | c , | σ (s)=SD(c |     | ,...,c | ).  |                     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | ---------- | --- | ------ | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5      |     | s,j | 5          |     | s,1    | s,5 |                     |     |     |     |     |     |     |     |     |
|        | 5   |     |            |     |        |     | ExperimentalSetting |     |     |     |     |     |     |     |     |
j=1
|     |     |     |     |     |     | (14) | Local | models | are | served | with | vLLM | (Kwon | et al. | 2023). |
| --- | --- | --- | --- | --- | --- | ---- | ----- | ------ | --- | ------ | ---- | ---- | ----- | ------ | ------ |
RepresentativePDFsareconvertedtostructuredMarkdown
| D6: Academic |     | impact. | D6 is an | OpenAlex-based |     | bib- |       |        |       |     |            |           |     |               |     |
| ------------ | --- | ------- | -------- | -------------- | --- | ---- | ----- | ------ | ----- | --- | ---------- | --------- | --- | ------------- | --- |
|              |     |         |          |                |     |      | using | MinerU | (Wang | et  | al. 2024), | processed |     | by rule-based |     |
liometric anchor rather than a newly proposed compos- filters, and anonymized using Qwen2.5-72B-Instruct-AWQ
ite index or a separately labeled benchmark. For each re- (Yangetal.2024)withtemperature0andamaximumoutput
| solved scholar, |     | we retrieve | the OpenAlex |     | author | record |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | ------------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lengthof1,200tokens.
| and the  | author-matched |              | work    | records. | The     | canonical |     |             |     |           |             |       |           |       |         |
| -------- | -------------- | ------------ | ------- | -------- | ------- | --------- | --- | ----------- | --- | --------- | ----------- | ----- | --------- | ----- | ------- |
|          |                |              |         |          |         |           |     | All primary |     | LLM-based | predictions |       | for D1–D3 |       | and D5  |
| D6 value | is the         | author-level | h-index |          | (Hirsch | 2005) in  |     |             |     |           |             |       |           |       |         |
|          |                |              |         |          |         |           | use | Qwen3.6-27B |     | (Qwen     | Team        | 2026) | with      | a 32K | context |
authors.summary_stats.h_index.
|     |     |     |     |     | If that | field is | window. |     | D1 uses | temperature |     | 0, D2 | and D3 | use tempera- |     |
| --- | --- | --- | --- | --- | ------- | -------- | ------- | --- | ------- | ----------- | --- | ----- | ------ | ------------ | --- |
unavailable,theimplementationusesadocumentedh-index ture 0.1, and D5 uses temperature 0. The maximum output
fallbackcomputedfromtheretrievedvalidworks.
lengthsare3,000tokensforD1,1,800tokensforD2andD3,
OtherOpenAlexfieldsareretainedasauditableevidence
|     |     |     |     |     |     |     | and | 2,048 | tokens | for D5. | Ridge | calibration |     | is trained | only |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ------- | ----- | ----------- | --- | ---------- | ---- |
butarenotcombinedintoanadditionalscore.Thesefieldsin-
|     |     |     |     |     |     |     | on  | the calibration |     | split | and evaluated |     | on held-out | test | data. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | ------------- | --- | ----------- | ---- | ----- |
cludetotalcitations,i10-index,workscount,two-yearmean Modelversions,prompts,retrievaldates,randomseeds,and
citedness,FWCI,citation-normalizedpercentiles,recentci- samplingmanifestsarerecordedforreproducibility.
| tations and | works, | top | works, pagination |     | status, and | the re- |     |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ----------------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trievaltimestamp.Thus,D6providesareproducibleandup- Baselines. For D1–D3, we compare HexEval with di-
dateablecitation-basedimpactsignal,whileD1–D5capture rectoverallscoring,chain-of-thoughtprompting(Weietal.
|     |     |     |     |     |     |     | 2022), | self-reflection |     | prompting |     | (Madaan | et  | al. 2023), | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | --------- | --- | ------- | --- | ---------- | --- |
non-bibliometricpropertiesthath-indexcannotrepresent.
theunweightedmeanofstructuredsubdimensionscores.All
Experimental methods use the same evaluator model, anonymized paper
|     |     |     |     |     |     |     | inputs, | and | dimension-specific |     |     | scoring | scales. | HexEval | ad- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------------ | --- | --- | ------- | ------- | ------- | --- |
EvaluationDatasetConstruction ditionallyappliesRidgecalibrationtrainedonlyonthecali-
brationsplit.
| Because | the dimensions |     | use different | evidence | sources | and |     |         |            |     |          |       |                       |     |     |
| ------- | -------------- | --- | ------------- | -------- | ------- | --- | --- | ------- | ---------- | --- | -------- | ----- | --------------------- | --- | --- |
|         |                |     |               |          |         |     |     | For D4, | we compare |     | the full | score | with single-indicator |     |     |
validationroles,D1–D3relyonhumanjudgments,D4uses
curatedscholarlyevidence,D5usesadjudicatedmulti-LLM and count-based baselines derived from the same verified
softwareandpatentevidence.
| references, | and | D6 uses | the OpenAlex |     | h-index | without a |     |         |            |     |            |     |             |     |         |
| ----------- | --- | ------- | ------------ | --- | ------- | --------- | --- | ------- | ---------- | --- | ---------- | --- | ----------- | --- | ------- |
|             |     |         |              |     |         |           |     | For D5, | we compare |     | HexEval-D5 |     | with TF–IDF |     | (Salton |
separatelyconstructedbenchmark.
|     |     |     |     |     |     |     | and | Buckley | 1988), | SPECTER2 |     | (Singh | et  | al. 2023), | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | -------- | --- | ------ | --- | ---------- | --- |
Intrinsic Quality Dataset. We use public OpenReview directzero-shotLLMscoring.AllD5methodsusethesame
reviews with dimension-level human judgments. D1 uses frozenfive-binsamplingmanifest,threepapersperbin,and
NeurIPS soundness annotations, D2 uses ICLR 2022 tech- fiverepeatedsamples.

D1:Rigor D2:Innovation D3:Contribution
Method ρ↑ MAE↓ Acc.@0.5↑ ρ↑ MAE↓ Acc.@0.5↑ ρ↑ MAE↓ Acc.@0.5↑
DirectOverall .411 .399 .73 .378 .435 .60 .291 .516 .54
CoT .440 .481 .62 .417 .463 .70 .239 .705 .28
Self-Reflection .402 .510 .64 .436 .402 .67 .258 .572 .45
SubdimensionMean .429 .379 .72 .381 .442 .59 .272 .558 .49
HexEval+Ridge .467 .361 .70 .356 .378 .68 .235 .295 .86
Table2:Agreementbetweenintrinsicqualityassessmentsandhumanpeer-reviewscoresusingQwen3.6-27B.Highervaluesare
betterforSpearman’sρandAcc.@0.5,whereaslowerMAEisbetter.Boldvaluesindicatethebestresultwithineachdimension
andmetric.
Results High–Low F1 Acc.
Method AUC @k @k
IntrinsicResearchQualityEvaluation
Communityprojectcount .834 .800 .800
We evaluate the three intrinsic dimensions by comparing
Personalrepositorycount .706 .867 .867
model scores with human peer-review judgments. D1, D2,
VerifiedGitHubprojectcount .848 .833 .833
and D3 use reviewer-averaged rigor, technical novelty, and GitHubmaxstars .894 .867 .867
contribution scores as reference labels, respectively. Each Patentfamilycount .617 .867 .867
dimension contains 100 held-out test papers disjoint from Patentcitationcount .693 .833 .833
thecalibrationset.WefixtheevaluatormodeltoQwen3.6- Rawsoftware+patentcounts .893 .833 .833
27B and compare direct overall scoring, chain-of-thought FullD4score .930 .867 .867
reasoning (Wei et al. 2022), self-reflection (Madaan et al.
2023),simpleaveragingofstructuredsubdimensionscores, Table3:ComparisonofindividualindicatorsandthefullD4
andHexEvalwithRidgecalibration.WereportSpearman’s score.
rank correlation (ρ), mean absolute error (MAE), and the
proportion of predictions within 0.5 points of the human
score(Acc@0.5). calibrationandordinalrankingarenotalwaysimprovedby
thesamemechanism.
D1:ResearchRigor. HexEvalperformsstrongestonrigor.
Ridgecalibrationachievesthehighestrankcorrelation(ρ= ExternalScholarlyBehaviorEvaluation
.467)andthelowestMAE(.361),improvingoverdirectover-
WeevaluateD4againstexternalknowledge-translationtiers
allscoringonbothmeasures.Directscoringobtainsthehigh-
andD5againstthefrozenadjudicatedcoherencereference.
estAcc@0.5(.73),butitslargernegativebiasindicatesless
D6isimplementedasasource-backedbibliometricindicator
calibratedabsolutescoring.Overall,structuredrigordecom-
rather than evaluated against a separately constructed label
position plus learned aggregation improves the consistency
set.
andscalealignmentofsoundnessassessment.
D4:KnowledgeTranslation. Atthemainthresholdsof30
D2: Methodological Innovation. Innovation remains the and50,thefixedD4scoreachieves.611accuracyand.601
most difficult intrinsic dimension. Self-reflection gives the Macro-F1onthebalancedthree-levelbenchmark.Asshown
highestrankcorrelation(ρ=.436),andCoTgivesthehigh- inTable3,thefullD4scoreobtainsthehighestHigh–Low
estAcc@0.5(.70).HexEvalachievesthelowestMAE(.378), AUC (.930), exceeding GitHub max stars (.894) and raw
indicatingbetterscore-scalecalibration,butitdoesnotim- software-plus-patent counts (.893), the two strongest base-
proveordinalranking.Thissuggeststhatcalibrationreduces lines.ItsF1@kandAcc.@kvaluesareboth.867,tyingsev-
systematicscoreerror,whilerelativenoveltyorderingisstill eralsimplerindicators.Theprincipaladvantageofthecom-
sensitivetomodeljudgment. plete D4 formulation therefore lies in separating high- and
low-translation scholars across the full ranking, rather than
D3: Scientific Contribution. For contribution, HexEval
inimprovingtop-kretrievalalone.Thecontinuousrankingis
substantiallyimprovesabsoluteagreement:MAEdropsfrom
independentofthereportingthresholds,whereasthederived
.516 under direct scoring to .295, and Acc@0.5 increases
three-levelclassificationremainssensitivetotheselectedcut
from .54 to .86. However, direct overall scoring still gives
points;detailedthreshold-sensitivityresultsareprovidedin
the highest rank correlation (ρ = .291). Thus, structured
theappendix.Overall,theseresultssupportthejointuseof
calibrationiseffectiveforaligningcontributionscoreswith
verifiedsoftwareandpatent/IPevidence,whileretainingevi-
thehumanscale,buttherelativeorderingofpapersremains
denceattribution,validationstatus,andsourceidentifiersfor
challenging.
auditing.
Overall,HexEvalmostclearlyimprovesscorecalibration
andabsoluteagreementacrossintrinsicdimensions.Ranking D5: Research Coherence. As shown in Table 4, on the
gainsarestrongestforD1,whereasD2andD3showthatscale frozen 90-scholar test set, HexEval-D5 achieves ρ = .743,

|     |     | ScholarA |     |     | D1 Rigor：52.9                                             |     |     |     |     | D2 Innovation：76.7                                              |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |          |     |     | Paper 1score: 3.1                                         |     |     |     |     | Paper 1score: 3.7                                               |     |     |     |     |     |
|     |     |          |     |     | Rationale-1:Theprimarybaselineis**.Whilethisistherelevant |     |     |     |     | Rationale-1:Thepaperpresentsahighlynoveltechnical               |     |     |     |     |     |
|     |     |          |     |     | competitor, the comparison is narrow.                     |     |     |     |     | contribution for its time (2010).                               |     |     |     |     |     |
|     |     |          |     |     | Evidence-1:[5 Results section] ***.                       |     |     |     |     | Evidence-1:[1 Introduction section] ***;[5 Results section]***. |     |     |     |     |     |
|     |     |          |     |     | Rationale-2：***                                           |     |     |     |     | Rationale-2：***                                                 |     |     |     |     |     |
|     |     |          |     |     | ……                                                        |     |     |     |     | ……                                                              |     |     |     |     |     |
|     |     |          |     |     | D3 Contribution：90.0                                      |     |     |     |     | D4 Translation：91.2                                             |     |     |     |     |     |
|     |     |          |     |     | Paper 1score: 3.7                                         |     |     |     |     | Top software evidence：                                          |     |     |     |     |     |
Rationale-1: This paper makes a highly significant contribution to
|     |     |     |     |     | thefieldofdistributedsystems….                            |     |     |     |     | Project Repository | Stars | Forks | Contributor verified | ….  |     |
| --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | ------------------ | ----- | ----- | -------------------- | --- | --- |
|     |     |     |     |     | Evidence-1:[1 Resultssection] ***;[7 Discussion section]. |     |     |     |     | Patent evidences：  |       |       |                      |     |     |
Rationale-2
|     |     |     |     |     | ……                |                  |       |       |     | Patent Lens ID | Citation | Granted           | ….  |       |     |
| --- | --- | --- | --- | --- | ----------------- | ---------------- | ----- | ----- | --- | -------------- | -------- | ----------------- | --- | ----- | --- |
|     |     |     |     |     | D5 Coherence：87.5 |                  |       |       |     | D6 Impact：89.7 |          |                   |     |       |     |
|     |     |     |     |     | Index Year        | Paper OpenalexID | Type  | Topic |     | Metric         | Value    | Metric            |     | Value |     |
|     |     |     |     |     | 1 2010            | ** ***           | Book  | **    |     | H-index        | 66       | FWCImean          |     | 42.98 |     |
|     |     |     |     |     | …                 |                  |       |       |     | Citations      | 50481    | 10-years citation |     | 32526 |     |
|     |     |     |     |     | n 2025            | ** ***           | Paper | **    |     | …              | …        | …                 |     | …     |     |
Figure 3: End-to-end HexEval case study for Scholar A. The figure summarizes the six-dimensional profile and associated
evidence outputs. D1–D3 use anonymized representative works, whereas D4–D6 use identity-resolved software, patent, and
OpenAlexevidence.Identifyinginformationisremovedfromthereportedcasestudy.Theprofileisillustrativeandshouldbe
interpretedtogetherwithevidencecoverageandattributionstatus.
underlyingidentitylinksareretainedonlyforevidenceattri-
| Method   |     | Spearman↑ | Kendall↑ | MAE↓ | Acc.@0.5↑ |     |         |        |            |            |     |           |                 |            |     |
| -------- | --- | --------- | -------- | ---- | --------- | --- | ------- | ------ | ---------- | ---------- | --- | --------- | --------------- | ---------- | --- |
|          |     |           |          |      |           |     | bution. | Figure | 3          | summarizes | the | resulting | six-dimensional |            |     |
| TF–IDF   |     | .283      | .203     |      | .389 .800 |     |         |        |            |            |     |           |                 |            |     |
|          |     |           |          |      |           |     | profile | and    | associated | evidence   |     | outputs.  | The             | case study | il- |
| SPECTER2 |     | .477      | .365     |      | .328 .811 |     |         |        |            |            |     |           |                 |            |     |
lustratesthereportingformatandevidenceflowratherthan
| Zero-shotLLM |     | .746 | .622 |     | .576 .489 |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---- | ---- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
population-levelaccuracy.
| HexEval-D5 |     | .743 | .620 |     | .266 .878 |     |     |           |     |          |           |     |      |               |     |
| ---------- | --- | ---- | ---- | --- | --------- | --- | --- | --------- | --- | -------- | --------- | --- | ---- | ------------- | --- |
|            |     |      |      |     |           |     | D5  | estimates |     | research | coherence |     | from | five repeated |     |
Table4:D5sparse-to-full-careercoherenceevaluationonthe chronologicalsamplesoftheauthor-resolvedOpenAlexpub-
frozen90-scholartestset.Allmethodsusethesamefive-bin, licationcorpus.D6usestheOpenAlexauthor-levelh-index
three-papers-per-binsamplingmanifestandfiverepeats. as its primary impact indicator, while other bibliometric
fieldsareretainedonlyassupportingevidence.Bothdimen-
|     |     |     |     |     |     |     | sions | are interpreted |     | together | with | evidence |     | coverage | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | --- | -------- | ---- | -------- | --- | -------- | --- |
attributionstatus.
| τ = .620,        | MAE      | = .266,    | and Acc.@0.5      |            | = .878. Although |         |            |     |          |     |                      |     |     |           |     |
| ---------------- | -------- | ---------- | ----------------- | ---------- | ---------------- | ------- | ---------- | --- | -------- | --- | -------------------- | --- | --- | --------- | --- |
| direct zero-shot |          | scoring    | yields marginally |            | higher rank      | cor-    |            |     |          |     |                      |     |     |           |     |
| relations        | (ρ =     | .746, τ    | = .622),          | HexEval-D5 | substantially    |         | Discussion |     |          |     |                      |     |     |           |     |
| improves         | absolute | agreement, | reducing          |            | MAE from         | .576 to |            |     |          |     |                      |     |     |           |     |
|                  |          |            |                   |            |                  |         | HexEval    | is  | intended | as  | an evidence-grounded |     |     | decision- |     |
.266 and increasing Acc.@0.5 from .489 to .878. TF–IDF supportframeworkratherthanareplacementforexpertjudg-
and SPECTER2 obtain lower rank correlations, suggesting ment.Itsmainadvantageisnotasinglesuperiorranking,but
that structured evaluation better aligns sparse publication the separation of heterogeneous signals that conventional
sampleswiththefull-careercoherencereference.
metricscollapse:D1–D3characterizethequalityofrepresen-
D6:AcademicImpact. D6usestheOpenAlexauthor-level tative research, whereas D4–D6 describe knowledge trans-
|     |     |     |     |     |     |     | lation, | research | coherence, |     | and | bibliometric |     | impact. | This |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | --- | --- | ------------ | --- | ------- | ---- |
h-indexasitscanonicalimpactindicator.Totalcitations,i10-
separationimprovesinterpretability,butthesixdimensions
index,workscount,two-yearmeancitedness,yearlycitation
shouldnotbetreatedasinterchangeableormechanicallyav-
counts,FWCI,citation-normalizedpercentiles,recentactiv-
eraged.Theframeworkremainslimitedbythecompleteness
| ity, top | works, | and retrieval | and author-resolution |     | metadata |     |     |     |     |     |     |     |     |     |     |
| -------- | ------ | ------------- | --------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
areretainedassupportingevidenceandarenotcombinedinto ofpublicrecords,authordisambiguation,andsource-specific
biases.GitHubandpatentevidencemayunderrepresentsome
anewcompositescore.BecauseD6isasource-backedoper-
disciplines,OpenAlexcoveragevariesacrossfields,andthe
ationalindicatorratherthanaseparatelylabeledbenchmark,
h-indexremainssensitivetocareerageandcitationpractices.
noD6baseline-comparisonorablationtableisreported.
|               |     |              |         |     |                |     | HexEval                         | should |     | therefore | support, | rather | than | determine, |     |
| ------------- | --- | ------------ | ------- | --- | -------------- | --- | ------------------------------- | ------ | --- | --------- | -------- | ------ | ---- | ---------- | --- |
| CaseStudy     |     |              |         |     |                |     | high-stakesassessmentdecisions. |        |     |           |          |        |      |            |     |
| We illustrate |     | the complete | HexEval |     | pipeline using | an  |                                 |        |     |           |          |        |      |            |     |
References
| anonymized | scholar, |     | denoted as | Scholar | A. Six | recent |     |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ---------- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
representative papers are anonymized and evaluated inde- Asai,A.;Gardner,M.;andHajishirzi,H.2022.Evidentiality-
pendently by D1–D3, while D4–D6 use identity-resolved GuidedGenerationforKnowledge-IntensiveNLPTasks. In
GitHub, Lens, and OpenAlex evidence. Identifying infor- Findings of the Association for Computational Linguistics:
| mation | is removed | from | the reported | case | study, while | the | NAACL2022. |     |     |     |     |     |     |     |     |
| ------ | ---------- | ---- | ------------ | ---- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |

DeepSeek-AI.2026. DeepSeekV4PreviewRelease. https: OpenAI. 2026. Introducing GPT-5.5. https://openai.com/
//api-docs.deepseek.com/news/news260424/. Accessed: index/introducing-gpt-5-5/. Accessed:2026-07-24.
2026-07-24. Pontika, N.; Chatzopoulos, S.; Manola, N.; and Manghi, P.
| Du, J.; Zhang, | Y.; Cao, | Y.; Fan, | Z.; | Yu, Z.; | Li, Y.; and |     |     |     |     |     |     |     |     |
| -------------- | -------- | -------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
2022.IndicatorsforOpenScienceandResponsibleResearch
| Wang, B. | 2024. LLMs | Assist | NLP | Researchers: | Critique |             |                                         |     |     |     |     |     |     |
| -------- | ---------- | ------ | --- | ------------ | -------- | ----------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |            |        |     |              |          | Assessment. | InProceedingsofthe26thInternationalCon- |     |     |     |     |     |     |
Paper(Meta-)Reviewing.InProceedingsofthe2024Confer- ference on Science, Technology and Innovation Indicators
enceonEmpiricalMethodsinNaturalLanguageProcessing (STI2022).STIConference.
(EMNLP).
Priem,J.;Piwowar,H.;andOrr,R.2022.OpenAlex:Afully-
| Gao, L.; | Dai, Z.; Pasupat, | P.; | Chen, | A.; Chaganty, | A. T.; |     |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | ----- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
openindexofscholarlyworks,authors,venues,institutions,
| Fan, Y.; Zhao, | V.; Lao, | N.; Lee, | H.; Juan, | D.-C.; | and Guu, |              |                                |     |     |     |     |     |     |
| -------------- | -------- | -------- | --------- | ------ | -------- | ------------ | ------------------------------ | --- | --- | --- | --- | --- | --- |
|                |          |          |           |        |          | andconcepts. | arXivpreprintarXiv:2205.01833. |     |     |     |     |     |     |
K.2023. RARR:ResearchingandRevisingWhatLanguage
ModelsSay,UsingLanguageModels. InProceedingsofthe QwenTeam.2026.Qwen3.6-27B:Flagship-LevelCodingin
61st Annual Meeting of the Association for Computational a27BDenseModel.
Linguistics.
|     |     |     |     |     |     | Radicchi,F.;Fortunato,S.;andCastellano,C.2008. |     |     |     |     |     | Univer- |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- |
Gorraiz,J.;Gumpenberger,C.;andSchloegl,C.2016. Indi- salityofcitationdistributions:Towardanobjectivemeasure
vidualbibliometricassessmentattheUniversityofVienna. of scientific impact. Proceedings of the National Academy
Bibliometrie-PraxisundForschung,5.
ofSciences,105(45):17268–17272.
Hicks,D.;Wouters,P.;Waltman,L.;deRijcke,S.;andRà-
|                |                           |     |        |           |         | Salton, G.;                       | and | Buckley, | C.  | 1988. Term-Weighting |     |     | Ap- |
| -------------- | ------------------------- | --- | ------ | --------- | ------- | --------------------------------- | --- | -------- | --- | -------------------- | --- | --- | --- |
| fols, I. 2015. | Bibliometrics:            | The | Leiden | Manifesto | for re- |                                   |     |          |     |                      |     |     |     |
|                |                           |     |        |           |         | proachesinAutomaticTextRetrieval. |     |          |     | InformationProcess-  |     |     |     |
| searchmetrics. | Nature,520(7548):429–431. |     |        |           |         |                                   |     |          |     |                      |     |     |     |
ing&Management,24(5):513–523.
| Hirsch,J.E.2005. | Anindextoquantifyanindividual’ssci- |     |     |     |     |            |         |     |        |             |     |         |       |
| ---------------- | ----------------------------------- | --- | --- | --- | --- | ---------- | ------- | --- | ------ | ----------- | --- | ------- | ----- |
|                  |                                     |     |     |     |     | Singh, A.; | D’Arcy, | M.; | Cohan, | A.; Downey, |     | D.; and | Feld- |
entificresearchoutput.ProceedingsoftheNationalAcademy
|     |     |     |     |     |     | man,S.2023. |     | SciRepEval:AMulti-FormatBenchmarkfor |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
ofSciences,102(46):16569–16572.
|                               |     |     |                         |     |     | ScientificDocumentRepresentations. |     |     |     | InProceedingsofthe |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | ---------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- |
| Jacovi,A.;andGoldberg,Y.2020. |     |     | TowardsFaithfullyInter- |     |     |                                    |     |     |     |                    |     |     |     |
2023ConferenceonEmpiricalMethodsinNaturalLanguage
pretableNLPSystems:HowShouldWeDefineandEvaluate
Processing,5548–5566.Singapore:AssociationforCompu-
| Faithfulness? | InProceedingsofthe58thAnnualMeetingof |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tationalLinguistics.
theAssociationforComputationalLinguistics,4198–4205.
|     |     |     |     |     |     | Thakkar, | N.; Yuksekgonul, |     | M.; | Silberg, | J.; Garg, | A.; | Peng, |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | --- | -------- | --------- | --- | ----- |
Jin,Y.;Wu,Z.;Tan,Z.;Ge,Y.;Joty,S.;andBing,L.2024.
|           |             |          |      |     |            | N.; Sha, | F.; Yu, | R.; | Vondrick, | C.; | and Zou, | J.  | 2025. |
| --------- | ----------- | -------- | ---- | --- | ---------- | -------- | ------- | --- | --------- | --- | -------- | --- | ----- |
| Exploring | Peer Review | Dynamics | with | LLM | Agents. In |          |         |     |           |     |          |     |       |
Proceedingsofthe2024ConferenceonEmpiricalMethods Can LLM feedback enhance review quality? A random-
|     |     |     |     |     |     | ized study | of 20K | reviews | at  | ICLR 2025. | arXiv | preprint |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ------- | --- | ---------- | ----- | -------- | --- |
inNaturalLanguageProcessing(EMNLP).
arXiv:2504.09737.
Kousha,K.;Thelwall,M.;andGadd,E.2025.CanChatGPT
evaluate research environments? Evidence from REF2021. Thelwall,M.2023. Arecitationindicatorsgoodalternatives
|     |     |     |     |     |     | to peer review? |     | The case | of the | UK  | Research | Excellence |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ------ | --- | -------- | ---------- | --- |
arXiv:2512.05202.
|     |     |     |     |     |     | Framework. | JournalofInformetrics,17(1):101376. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Kwon,W.;Li,Z.;Zhuang,S.;Sheng,Y.;Zheng,L.;Yu,C.H.;
Gonzalez, J. E.; Zhang, H.; and Stoica, I. 2023. Efficient Thelwall,M.2024.CanChatGPTevaluateresearchquality?
Memory Management for Large Language Model Serving JournalofDataandInformationScience,9(2):1–21.
| withPagedAttention. | InProceedingsofthe29thSymposium |     |     |     |     |           |          |            |     |          |         |           |     |
| ------------------- | ------------------------------- | --- | --- | --- | --- | --------- | -------- | ---------- | --- | -------- | ------- | --------- | --- |
|                     |                                 |     |     |     |     | Thelwall, | M. 2025. | Evaluating |     | research | quality | withLarge |     |
onOperatingSystemsPrinciples,611–626.
|            |                    |     |          |                |     | Language       | Models:  | An  | analysis    | of ChatGPT’s |     | effectiveness |     |
| ---------- | ------------------ | --- | -------- | -------------- | --- | -------------- | -------- | --- | ----------- | ------------ | --- | ------------- | --- |
| Lewis, P.; | Perez, E.; Piktus, | A.; | Petroni, | F.; Karpukhin, | V.; |                |          |     |             |              |     |               |     |
|            |                    |     |          |                |     | with different | settings |     | and inputs. | Journal      | of  | Data and      | In- |
Goyal,N.;Küttler,H.;Lewis,M.;Yih,W.-t.;Rocktäschel,T.; formationScience,10(1):1–19.
| Riedel, S.;                            | and Kiela, D. | 2020. | Retrieval-Augmented |              | Gen- |           |     |            |     |       |          |        |     |
| -------------------------------------- | ------------- | ----- | ------------------- | ------------ | ---- | --------- | --- | ---------- | --- | ----- | -------- | ------ | --- |
|                                        |               |       |                     |              |      | Thelwall, | M.; | and Yaghi, | A.  | 2024. | In which | fields | can |
| erationforKnowledge-IntensiveNLPTasks. |               |       |                     | InAdvancesin |      |           |     |            |     |       |          |        |     |
Neural Information Processing Systems, volume 33, 9459– ChatGPT detect journal article quality? An evaluation of
| 9474. |     |     |     |     |     | REF2021results. |     | arXiv:2409.16695. |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | --- | --- | --- | --- |
Madaan, A.; Tandon, N.; Gupta, P.; Hallinan, S.; Gao, L.; Wadden, D.; Lin, S.; Lo, K.; Wang, L. L.; van Zuylen, M.;
Wiegreffe, S.; Alon, U.; Dziri, N.; Prabhumoye, S.; Yang, Cohan,A.;andHajishirzi,H.2020.FactorFiction:Verifying
Y.; Gupta, S.; Majumder, B. P.; Hermann, K.; Welleck, S.; ScientificClaims.InProceedingsofthe2020Conferenceon
EmpiricalMethodsinNaturalLanguageProcessing,7534–
| Yazdanbakhsh,                    | A.; and | Clark, | P. 2023.           | Self-Refine: | Itera- |       |     |     |     |     |     |     |     |
| -------------------------------- | ------- | ------ | ------------------ | ------------ | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| tiveRefinementwithSelf-Feedback. |         |        | InAdvancesinNeural |              |        | 7550. |     |     |     |     |     |     |     |
InformationProcessingSystems,volume36,46534–46594.
|     |     |     |     |     |     | Wadden, | D.; Lo, | K.; | Kuehl, | B.; Cohan, | A.; | Beltagy, | I.; |
| --- | --- | --- | --- | --- | --- | ------- | ------- | --- | ------ | ---------- | --- | -------- | --- |
Merton,R.K.1968. TheMatthewEffectinScience:There- Wang, L. L.; and Hajishirzi, H. 2022. SciFact-Open: To-
wardandcommunicationsystemsofscienceareconsidered. wards open-domain scientific claim verification. In Gold-
Science,159(3810):56–63. berg,Y.;Kozareva,Z.;andZhang,Y.,eds.,Findingsofthe
Nunkoo,R.;andThelwall,M.2026.AGlobalSouthStrategy Association for Computational Linguistics: EMNLP 2022,
forEvaluatingResearchValuewithChatGPT. Quantitative 4719–4734.AbuDhabi,UnitedArabEmirates:Association
| ScienceStudies. |     |     |     |     |     | forComputationalLinguistics. |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |

Wainer,J.;Brahim,G.F.;andRichard,P.2013. Whathap-
penstocomputerscienceresearchafteritispublished?Jour-
naloftheAssociationforInformationScienceandTechnol-
ogy,64(5):884–897.
Wang, B.; Xu, C.; Zhao, X.; Ouyang, L.; Wu, F.; Zhao, Z.;
Xu,R.;Liu,K.;Qu,Y.;Shang,F.;Zhang,B.;Wei,L.;Sui,
Z.; Li, W.; Shi, B.; Qiao, Y.; Lin, D.; and He, C. 2024.
MinerU: An Open-Source Solution for Precise Document
ContentExtraction. arXivpreprintarXiv:2409.18839.
Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Ichter, B.;
Xia, F.; Chi, E. H.; Le, Q. V.; and Zhou, D. 2022. Chain-
of-ThoughtPromptingElicitsReasoninginLargeLanguage
Models. InAdvancesinNeuralInformationProcessingSys-
tems,volume35,24824–24837.
Xie, Z.; Ouyang, Z.; Li, J.; Liu, G.; and Hu, X. 2021.
A network-embedding-based scholar assessment indicator.
JournalofInformetrics,15(3):101171.
Yang, A.; Yang, B.; Zhang, B.; Hui, B.; Zheng, B.; Yu, B.;
Li,C.;Liu,D.;Huang,F.;Wei,H.;Lin,H.;Yang,J.;Tu,J.;
Zhang,J.;Yang,J.;Yang,J.;Zhou,J.;Lin,J.;Dang,K.;Lu,
K.; Bao, K.; Yang, K.; Yu, L.; Li, M.; Xue, M.; Zhang, P.;
Zhu,Q.;Men,R.;Lin,R.;Li,T.;Xia,T.;Ren,X.;Ren,X.;
Fan,Y.;Su,Y.;Zhang,Y.;Wan,Y.;Liu,Y.;Cui,Z.;Zhang,
Z.; and Qiu, Z. 2024. Qwen2.5 Technical Report. arXiv
preprintarXiv:2412.15115.
Z.ai.2026. GLM-5.2:BuiltforLong-HorizonTasks. https:
//z.ai/blog/glm-5.2. Accessed:2026-07-24.
Zhou, R.; Zeng, X.; Wang, J.; Yang, Y.; and Liu, J. 2024.
IsLLMaReliableReviewer?AComprehensiveEvaluation
of Large Language Models on Automatic Paper Reviewing
Tasks. InProceedingsofthe2024JointInternationalCon-
ferenceonComputationalLinguistics,LanguageResources
andEvaluation(LREC-COLING).
Zhu,M.;Weng,Y.;Yang,L.;andZhang,Y.2025. DeepRe-
view:ImprovingLLM-BasedPaperReviewwithHuman-like
DeepThinkingProcess. InProceedingsofthe63rdAnnual
Meeting of the Association for Computational Linguistics
(ACL),29330–29355.
---- END DOCUMENT ----
