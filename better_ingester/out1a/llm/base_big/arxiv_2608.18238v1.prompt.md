Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
GenEx: A Graph-Based Representational Paradigm
for SARS-CoV-2 Variant Detection via Codon
Co-occurrence Networks
Arefin Amin Labiba Faiza Karim M. Monir Uddin
ECE Department ECE Department Department of Math. & Phy.
North South University North South University North South University
Dhaka, Bangladesh Dhaka, Bangladesh Dhaka, Bangladesh
arefin.amin@northsouth.edu labiba.karim@northsouth.edu monir.uddin@northsouth.edu
Abstract—Genomic analysis on viruses such as SARS-CoV-2 codonco-occurrencegraphs,wherenodesandedgesrepresent
variants:Beta,Gamma,Delta,andOmicronisheavilydominated codons and their local relationships, respectively, we can
by classical bioinformatics methods, including Sequence Align-
capture neighborhood patterns and mutation tendencies that
ment, Phylogenetic Analysis, and Mutation Frequency Statistics.
are invisible to traditional approaches.
These approaches use pairwise codon or nucleotide distance
matrices to analyze gene sequences, treating them as linear We propose GenEx, a novel Graph-Based Representation
strings rather than capturing their complex contextual interde- framework that models viral genomes as codon-level co-
pendencies. We proposed GenEx, a pipeline that converts raw occurrence graphs and identifies distinct topological signa-
gene sequences into codon co-occurrence graphs and extracts
tures and spectral properties associated with different viral
morethan25graphfeatures.Ourtwomostprominenttechniques
variants. GenEx extracts spectral and topological features
for graph generation and feature extraction are MSCG (Multi-
Scale Codon Co-occurrence Graph) and LAPCG (Linear-time by computing direct-neighbor interactions, generalizing these
Adjacency PMI Codon Graph). Using these algorithms, we associations across multiple co-occurrence scales and posi-
treated codon sequences as structured symbolic vocabularies tional segment encodings; a data-driven graph paradigm for
interpretable to codon co-occurrence graph analysis, a repre-
cladeclassificationthatprioritizesmathematicalexplainability
sentational paradigm borrowed from computational linguistics.
and computational efficiency over black-box modeling. This
Another major contribution includes implementing a spectral
graph feature extraction using Singular Value Decomposition architecturetreatsvariantdetectionasameasurabletaskwithin
(SVD), using the squared singular value (σ2) instead of the graph theory, providing a robust, data-driven methodology for
traditionally used eigenvalue, which helped us to amplify the classifying viral evolution. We initially focused on SARS-
separation between dominant and subdominant spectral compo-
CoV-2 because large-scale genomic sequences were available.
nents, thereby enhancing inter-class separability in downstream
This proposed framework will be designed to be adaptable,
classification.Andtofurtherdemonstratethatourmethodworks,
wetrained23benchmarkedMLmodelsagainstthelatestSARS- thusitcanextendtootherviralfamiliesandhigherorganisms.
CoV-2 variants, achieving remarkable results in detecting all
A. Motivation:
SARS-CoV-2 variants.
Index Terms—Sequence Alignment, Phylogenetic Analysis, The motivation for this study originated from the following
Multi-ScaleCodonCo-occurrenceGraph,Computationallinguis-
reasons:
tics, Spectral graph features.
1) Limitations of existing genome analysis methods:
I. INTRODUCTION Traditionalgeneanalysismethods,suchasphylogenetic
andstatisticalmutationmodels,areoftenconstrainedby
Understanding viral genome evolution is a fundamental
assumptionsoflinear,site-independentmutationpatterns
problemincomputationalbiology,withdirectimplicationsfor
and fail to capture the complex contextual interdepen-
evolutionarystudiesandvaccinemonitoring.WhiletheSARS-
dencies within the genomic sequences.
CoV-2 pandemic has enabled the collection of large-scale
2) Need for “Alignment-Free” Surveillance: With the
big data on viral genome sequences, conventional methods:
exponentially growing viral data, alignment-free frame-
phylogenetictreereconstruction,mutationfrequencystatistics,
works are needed to characterize variants through their
andmultiplesequencealignment(MSA),heavilyfocusonret-
topological signatures, which enables rapid identifica-
rospectiveevolutionaryevents,stationarity,site-independence,
tion of emerging Variants of Concern (VOC) without
andalinearmutationprocess;thus,failingtocapturethecom-
bottlenecks.
plex relationships and interactions within genomic sequences.
3) Preparation for Future Pathogens: The research
To resolve these bottlenecks, we propose shifting from the
provides a mathematical foundation for the evolution of
static linear analysis to structural graph models that capture
future pathogens, pandemics, and vaccines by develop-
thetopologicalstructureofgeneticsequences.Byconstructing
6202
guA
81
]IA.sc[
1v83281.8062:viXra

| ing a generalizable, |     | alignment-free |     | model | applicable | to  |     |     |     |     |     |     |
| -------------------- | --- | -------------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
TABLEI
COMPARISONOFPRIORWORKANDPROPOSEDMETHOD
| pathogens         | and higher | organisms. |     |     |     |     |        |     |           |     |           |     |
| ----------------- | ---------- | ---------- | --- | --- | --- | --- | ------ | --- | --------- | --- | --------- | --- |
| B. Contributions: |            |            |     |     |     |     | Aspect |     | PriorWork |     | OurMethod |     |
Our work concentrates on the following aspects: Biologicalunit Nucleotide/segment Codon
|     |     |     |     |     |     |     | Representation |     | Sequence/staticgraph |     | Co-occurrencegraph |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------------- | --- | ------------------ | --- |
1) Dual-Paradigm Graph Construction Algorithms:We Temporalmodeling No Yes
|                   |             |             |           |             |               |     | Learningframework |     | CNN/Transformer/rules |     | MLongraphfeatures      |     |
| ----------------- | ----------- | ----------- | --------- | ----------- | ------------- | --- | ----------------- | --- | --------------------- | --- | ---------------------- | --- |
| proposed          | two novel   | algorithms, |           | LAPCG       | and MSCG,     | to  |                   |     |                       |     |                        |     |
|                   |             |             |           |             |               |     | Explainability    |     | Post-hoc              |     | Intrinsic(graph-based) |     |
| extract codon     | interaction |             | networks  | from        | linear gene   | se- |                   |     |                       |     |                        |     |
|                   |             |             |           |             |               |     | Multi-taskreuse   |     | Limited               |     | Yes                    |     |
| quences           | with O(n)   | and         | O(n2)     | complexity, | respectively, |     |                   |     |                       |     |                        |     |
| while maintaining |             | a 98.75%    | accuracy. |             |               |     |                   |     |                       |     |                        |     |
2) Spectral Feature Engineering and Mathematical Ab initio and Pipeline-based Gene Annotation. Sys-
•
Framework:WeintroducedaSingularValueDecompo-
|     |     |     |     |     |     |     | tems | including | GENSCAN | [9], | GeneMark | [10], AU- |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ------- | ---- | -------- | --------- |
sition(SVD)basedframeworkthatderivessevendistinct GUSTUS [11], GlimmerHMM [12], BRAKER2 [13],
spectral features from squared singular values (σ2), MAKER2 [14], and Helixer [15] are strong annota-
providinganumericallystablerepresentationofgenomic tion tools. Their objective, however, is gene-structure
interaction systems with high inter-class separability. annotation, not variant classification through codon co-
3) MathematicalExplainabilityandBiologicalInterpre-
|     |     |     |     |     |     |     | occurrence | topology. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --- | --- | --- |
tation:Wewereabletoprovidearigorousinterpretation • Our Approach (GenEx). GenEx models each genome
of viral clades by correlating their biological interpreta- as a codon co-occurrence graph, where nodes are codons
tionswithnumericalgraphproperties;thus,wecanview and edges encode positional/mutational coupling. We
thestructuralmechanismsofviralevolutionandvariant- thenclassifyvariantsusinggraph-derivedfeatures,yield-
| specific | interaction | dynamics. |     |     |     |     |                   |               |                 |                 |         |                 |
| -------- | ----------- | --------- | --- | --- | --- | --- | ----------------- | ------------- | --------------- | --------------- | ------- | --------------- |
|          |             |           |     |     |     |     | ing interpretable |               | structure-aware |                 | signals | that can be ex- |
|          |             |           |     |     |     |     | tended            | to amino-acid | and             | structure-level |         | graphs.         |
II. RELATEDWORKS
Recentprogressincomputationalbiologyhasmadegenome III. DATASET
analysis faster and more scalable. This section briefly reviews We used the following publicly available SARS-CoV-2
the work streams most relevant to GenEx. genome sequence datasets from the National Center for
• Sequence-based Deep Learning Models. CNN- and Biotechnology Information (NCBI) [16] Virus database to
Transformer-based models treat genomes as linear nu- train, validate, and test the GenEx framework:
| cleotide strings | for | regulatory | and          | mutational | prediction |     |            |            |          |     |     |     |
| ---------------- | --- | ---------- | ------------ | ---------- | ---------- | --- | ---------- | ---------- | -------- | --- | --- | --- |
|                  |     |            |              |            |            |     | A. Dataset | Collection | Process: |     |     |     |
| [1], [2]. They   | are | effective  | for sequence | pattern    | recogni-   |     |            |            |          |     |     |     |
tion, but usually ignore codon-level structure and rely on The SARS-CoV-2 genome sequence data for this research
wereretrievedusingthencbi-datasetscommand-lineinterface.
| post-hoc | explanation. |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Genome Graphs and Pangenome Representations. We used the following fetch commands to fetch the variants
•
| Genomeandpangenomegraphsencodepopulationvaria- |     |     |     |     |     |     | in ZIP format: |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
tionwithsequence-segmentnodesandvariant-pathedges • Beta: datasets download virus genome
[3]. These frameworks are useful for representation, but taxon SARS-CoV-2 --lineage B.1.351 [16]
are often non-learning, mostly static, and not built for • Delta: datasets download virus genome
codon-level mutation feature learning. taxon SARS-CoV-2 --lineage B.1.617.2
| Graph Neural |     | Networks | in  | Bioinformatics. |     | GNNs |      |     |     |     |     |     |
| ------------ | --- | -------- | --- | --------------- | --- | ---- | ---- | --- | --- | --- | --- | --- |
| •            |     |          |     |                 |     |      | [16] |     |     |     |     |     |
perform well on molecular graphs, protein–protein in- • Gamma: datasets download virus genome
teraction networks, and gene regulation tasks [4], [5]. taxon SARS-CoV-2 --lineage P.1 [16]
However,moststudiesarestaticandrarelymodelcodon- • Omicron: datasets download virus genome
level evolutionary dynamics directly. taxon SARS-CoV-2 --lineage B.1.1.529
| Evolutionary | and | Phylogenetic |     | Models. | Classical | tools | [16] |     |     |     |     |     |
| ------------ | --- | ------------ | --- | ------- | --------- | ----- | ---- | --- | --- | --- | --- | --- |
•
suchasPAM[6]andBLOSUM[7]arebiologicallyinter- After fetching the ZIP files, we extracted
pretableandfoundational.Theirlimitationisdependence beta_sequences.csv, delta_sequences.csv,
on assumptions such as stationarity and site indepen- gamma_sequences.csv, and
dence, which can miss nonlinear mutation behavior. omicron_sequences.csv. From each CSV file, we
| Explainable | Genomic |     | AI. Attribution |     | methods | (e.g., |               |            |            |     |          |            |
| ----------- | ------- | --- | --------------- | --- | ------- | ------ | ------------- | ---------- | ---------- | --- | -------- | ---------- |
| •           |         |     |                 |     |         |        | selected 1250 | randomized | sequences, |     | yielding | 5000 viral |
DeepLIFT [8]) and attention analysis are widely used genome sequences in total.
forinterpretability.Inpractice,mostaresequence-centric
|               |        |         |            |         |      |       | B. Dataset | Characteristics | and | Structure: |     |     |
| ------------- | ------ | ------- | ---------- | ------- | ---- | ----- | ---------- | --------------- | --- | ---------- | --- | --- |
| and post-hoc, | giving | limited | structural | insight | into | codon |            |                 |     |            |     |     |
relationships. Each raw CSV file and the extracted sequence CSV files
(1250sequencespervariant)had3columns:header,sequence,
|     |     |     |     |     |     |     | and sequence | length. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | --- | --- | --- |

• header:ContainedtheNCBIaccessionIDfortherespec- Algorithm 1 LAPCG Graph Construction
tivegenomesequence,thesymptoms,virusname(SARS- Require: Codon sequence C =(c ,...,c )
1 N
CoV-2), Host/Carrier, etc., as a single string. Ensure: Undirected weighted graph G=(V,E,W)
• sequence: Contained gene sequences. 1: Initialize node-frequency map F and adjacent-pair map
• sequence length: Contained an integer representing the M
length of each gene sequence. 2: for i=1 to N do
3: F(c i )←F(c i )+1
C. Data Pre-processing
4: end for
After downloading the data, we began our pre-processing - 5: for i=1 to N −1 do
• First we took first 10 character deicarding the rest from 6: u←c i , v ←c i+1
the header column of the datasets as those first 10 7: M(u,v)←M(u,v)+1 {unordered pair}
characters made up the accession ID. 8: end for
• The Gnomesare officially storedas cDNA (A,T,G,C)se- 9: V ← unique codons in C
quences even though SARS-CoV-2 is an RNA (A,T,U,C) 10: for all pairs (u,v) with M(u,v)>0 do
virus.Thus,toensurecompatibilitywiththemainstream 11: p(u,v)← M(u,v), p(u)← F(u), p(v)← F(v)
N−1 (cid:16) (cid:17) N N
we avoided unnecessary conversion and maintained the 12: PMI(u,v)←log p(u,v)
cDNA sequences. p(u)p(v)
13: if PMI(u,v)>0 then
• Next, we capitalized the Gene sequences and removed
14: Add edge (u,v) with weight PMI(u,v)
unnecessary sequences and characters that are not rele-
15: end if
vant to our current work.
16: end for
• We found 20 thousand clean sequences with unique
17: return G=(V,E,W)
accession ID from each of these variants.
IV. METHODOLOGY Algorithm 2 MSCG Graph Construction
A. Overview Require: Codon sequence C = (c ,...,c ), scales S =
1 N
GenExconvertseachSARS-CoV-2nucleotidesequenceinto {(s,α s )}
acodongraph,extractsstructuralandspectraldescriptors,and Ensure: Multi-scale weighted graph G=(V,E,W)
then uses these descriptors for variant-level statistical analysis 1: Initialize node statistics and empty edge accumulator A e
and machine learning classification. We used two graph con- 2: V ← unique codons in C
struction strategies: LAPCG for fast local codon interactions 3: for all (s,α s )∈S do
and MSCG for multi-scale codon context modeling. 4: for i=1 to N −s do
5: Observe pair (c i ,c i+s ) and update pair counts
B. End-to-end Pipeline
6: end for
1) Convert each sequence into codons using fixed-frame 7: for all observed pairs (u,v) do
triplets. 8: Compute PMI(u,v) and
2) Build a weighted codon graph using either LAPCG or
PMI(u,v)
MSCG. NPMI(u,v)=
−logp(u,v)
3) Compute graph features (topological, path-based, cen-
trality, and spectral). 9: if NPMI(u,v)>0 then
4) Run significance tests (ANOVA) across variants. 10: A e (u,v)←A e (u,v)+α s ·NPMI(u,v)
5) Benchmark ML models on extracted feature vectors. 11: end if
12: end for
C. Codon Segmentation 13: end for
Given a nucleotide sequence 14: for all pairs (u,v) in A e do
15: Add edge (u,v) with accumulated weight A e (u,v)
S =(n ,n ,...,n ),
1 2 L 16: end for
we form codons as non-overlapping triplets: 17: return G=(V,E,W)
C =(c ,c ,...,c ), c =(n ,n ,n ).
1 2 ⌊L/3⌋ i 3i−2 3i−1 3i
Ambiguous symbols (e.g., N) are removed before graph con- E. MSCG: Multi-Scale Codon Co-occurrence Graph
struction. MSCG extends local adjacency by capturing co-occurrence
across multiple codon distances. In our setup, we used scales
D. LAPCG: Linear-time Adjacency PMI Codon Graph
s ∈ {1,2,3} with decay weights (1.0,0.5,0.25) and normal-
LAPCGmodelsonlyadjacentcodonpairs(c ,c ),which
i i+1 ized PMI (NPMI).
provides linear complexity in sequence length and works well
for large-scale data.

Fig. 1. Overview of the GenEx framework for SARS-CoV-2 variant detection using a graph-based approach. The pipeline begins with genome sequence
acquisition from NCBI GenBank, followed by preprocessing steps including quality filtering, codon segmentation into triplets, and sequence alignment.
Codon co-occurrence graphs are then constructed using two methods—LAPCG (linear-time adjacency-based) and MSCG (multi-scale co-occurrence)—to
form weighted undirected graphs. From these graphs, both topological and spectral features are extracted to create high-dimensional feature vectors. These
features are used to train and evaluate multiple machine learning models for variant classification. The framework outputs include high-accuracy variant
predictions,featureimportanceanalysis,statisticalvalidation,structuralgraphinsights,andevolutionarypatterncomparisons.
| F. Feature | Extraction | and | Evaluation |     |     |     |     |     |     | TABLEII |     |     |     |     |
| ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
BENCHMARKSUMMARY:ACCURACYANDRUNTIMEACROSSGRAPH
From each graph we extracted structural and spectral fea- CONSTRUCTIONMETHODS.
| tures, including | number   |      | of nodes/edges, |        | density, | diameter,         |        |     |              |     |     |          |            |     |
| ---------------- | -------- | ---- | --------------- | ------ | -------- | ----------------- | ------ | --- | ------------ | --- | --- | -------- | ---------- | --- |
| radius, average  | shortest | path | length,         | Wiener |          | index, transitiv- |        |     |              |     |     |          |            |     |
|                  |          |      |                 |        |          |                   | Method |     | BestModel(s) |     |     | Accuracy | Runtime(s) |     |
ity, clustering, centrality scores, graph energy, top singular- PMIbaseline CatBoost 96.25% 272.3
spectrumcomponents,max-flow,andmatchingnumber.These LAPCG LightGBM,Grad.Boost 96.25% 196.2
|             |      |               |     |              |     |           | MSCG |     | MLP,BaggingClassifier |     |     | 98.75% | 144.6 |     |
| ----------- | ---- | ------------- | --- | ------------ | --- | --------- | ---- | --- | --------------------- | --- | --- | ------ | ----- | --- |
| were used   | for: |               |     |              |     |           |      |     |                       |     |     |        |       |     |
| ANOVA-based |      | inter-variant |     | significance |     | analysis, |      |     |                       |     |     |        |       |     |
•
| • feature-importance |              | analysis, |        |          |     |           |           |          |     |                |     |       |         |         |
| -------------------- | ------------ | --------- | ------ | -------- | --- | --------- | --------- | -------- | --- | -------------- | --- | ----- | ------- | ------- |
|                      |              |           |        |          |     |           | 272.3s to | complete | the | full pipeline. |     | LAPCG | reduces | this to |
| model                | benchmarking |           | across | multiple | ML  | families. |           |          |     |                |     |       |         |         |
• 196.2s (a 1.39× speedup) by restricting edge computation to
V. RESULTS adjacent codon pairs, operating in strict O(n) time. MSCG,
|                       |            |           |                 |      |          |                  | despite modeling  |                      | three     | co-occurrence |                 | scales        | simultaneously, |           |
| --------------------- | ---------- | --------- | --------------- | ---- | -------- | ---------------- | ----------------- | -------------------- | --------- | ------------- | --------------- | ------------- | --------------- | --------- |
| A. Model Benchmarking |            |           |                 |      |          |                  |                   |                      |           |               |                 |               |                 |           |
|                       |            |           |                 |      |          |                  | achieves          | the lowest           | runtime   |               | of 144.6s—a     |               | 1.88×           | speedup   |
| Table II              | summarizes | the       | best-performing |      |          | models for base- |                   |                      |           |               |                 |               |                 |           |
|                       |            |           |                 |      |          |                  | over the          | PMI baseline—because |           |               | the             | NPMI          | computation     | and       |
| line PMI, LAPCG,      |            | and MSCG. |                 | MSCG | achieved | the strongest    |                   |                      |           |               |                 |               |                 |           |
|                       |            |           |                 |      |          |                  | accumulated       | edge                 | weighting |               | are implemented |               | as              | a single- |
| overall performance   |            | in our    | benchmark.      |      |          |                  |                   |                      |           |               |                 |               |                 |           |
|                       |            |           |                 |      |          |                  | pass accumulation |                      | rather    | than          | a global        | normalization |                 | step.     |
B. Computational Efficiency of Graph Construction Crucially, this efficiency gain is not purchased at the cost
|                     |           |            |          |        |             |           | of accuracy: | MSCG       | also          | achieves |     | the highest      | classification |            |
| ------------------- | --------- | ---------- | -------- | ------ | ----------- | --------- | ------------ | ---------- | ------------- | -------- | --- | ---------------- | -------------- | ---------- |
| A critical          | practical | advantage  |          | of our | proposed    | methods   | is           |            |               |          |     |                  |                |            |
|                     |           |            |          |        |             |           | accuracy     | at 98.75%, | demonstrating |          |     | that multi-scale |                | structural |
| their computational |           | efficiency | relative |        | to standard | PMI-based |              |            |               |          |     |                  |                |            |
|                     |           |            |          |        |             |           | modeling     | of codon   | co-occurrence |          |     | is both          | faster and     | more       |
graphconstruction.ThePMIbaseline,whichcomputesglobal
|               |            |     |          |        |           |          | discriminative | than | traditional |     | PMI. |     |     |     |
| ------------- | ---------- | --- | -------- | ------ | --------- | -------- | -------------- | ---- | ----------- | --- | ---- | --- | --- | --- |
| co-occurrence | statistics |     | over the | entire | sequence, | requires |                |      |             |     |      |     |     |     |

These runtime measurements were obtained on the full and stable rank sharply diverge for Omicron samples (visible
SARS-CoV-2 genome sequence dataset on a single CPU in the upper and lower rows of the plot), while spectral
core, without parallelization. The MSCG pipeline—including measures such as top eigenvalue and graph energy remain
graphconstruction,featureextraction,andMLclassification— highly conserved across all four clades.
processes each genome in under 1s on average, making it
G. Interpretation
suitable for real-time variant surveillance at scale.
This section presents a biological and structural inter-
C. Comparison with Gene Detection and Variant Classifica-
pretation of the graph theoretic features extracted from
tion Methods
the genome sequences of four SARS-CoV-2 variants: Beta
TableIIIsituatesGenExwithinthebroaderlandscapeofge- (B.1.351), Gamma (P.1), Delta (B.1.617.2), and Omicron
nomic sequence analysis tools.We distinguish two categories: (B.1.1.529). [16] Each genome sequence was represented as
(i)traditionalgeneannotationtoolsthatpredictgenestructure a graph, and 22 graphical properties were computed. The
from raw sequence (e.g., AUGUSTUS, GeneMark), and (ii) interpretation is organized into two subsections: (i) structural
variant classification methods that assign a class label to a profile for each variant, (ii) comparative analysis of structural
given genome. Our GenEx falls into the second category. Ac- similarities and dissimilarities across the four variants.
curacy figures for gene annotation tools are reported in terms
H. Structural Profiles of Individual Variants
of nucleotide-level sensitivity/specificity, while classification
accuracy for variant detection methods corresponds to multi- Each variant yields a distinct genomic graph fingerprint,
class labeling performance. definedbyacombinationofconservedbaselinepropertiesand
GenEx MSCG achieves the highest reported accuracy variant-specific outlier behavior.
among all compared methods for its classification task, while 1) Beta (B.1.351): The Beta variant is characterized by
also improving computational efficiency over standard PMI- a structurally stable median profile, combined with the
basedconstruction.Itisimportanttonotethatgeneannotation mostextremeindividualoutliersobservedacrosstheentire
toolsaddressastructurallydifferentproblem—predictinggene dataset, making it the most internally volatile variant at
coordinates in an unannotated genome—and are therefore not the graph level.
directly comparable in terms of accuracy numbers. Never- From the graphs generated, it can be observed that the beta
theless, placing GenEx alongside these tools provides useful variants’ genomic sequences produce dense interconnected
context:our98.75%accuracyisachievedonawhole-genome, networks with nearly complete graphs. This is reflected in
alignment-free basis without any reference sequence or tran- the median graph density of ∼ 0.97, which also indicates
scriptomic data, which contrasts favorably with the reference- strong tendencies to conserve the viral backbone. Similarly,
dependent or transcript-dependent nature of hybrid pipeline transitivity and average clustering coefficient values are about
methods such as BRAKER2 and EVidenceModeler. 0.96–0.97 across most Beta samples, confirming that local
genomic neighborhoods are tightly triangulated. The average
D. Feature Importance and Statistical Significance
shortestpathlengthandthemediandiameterofnearly6.2and
MSCGemphasizedbothpath-basedandspectralproperties. 9.5,respectively,establishthattheBetagenomegraphexhibits
The highest ranked features were second eigenvalue, average a compact, small-world organization in which any genomic
shortestpathlength,Wienerindex,topeigenvalue,andradius. regionisreachable fromanyotherwithina limitednumberof
ANOVA analysis further showed strong between-variant sep- steps.
aration for radius (F = 69.74, p = 3.14×10−36), average Regardless of the stable core, Beta sequences exhibit
shortest path length (F = 60.19, p = 4.43 × 10−32), top volatile-periphery anomalies, with several extreme outliers.
eigenvalue (F = 47.82, p = 2.14×10−26), and number of Fromthegraphicalfeatureextraction,wehaveobservedthatat
edges (F =33.52, p=2.51×10−19). leastoneBetasequencegeneratesaWienerIndexof∼45,000,
roughlythricethetypicalvalue(vs.typical∼15,000)forother
E. Variant Structural Profiles
variants, indicating greater distances between genomic units.
Figure 2 summarizes all four variant structural profiles in a This longer genomic distance indicates extensive deletions
single 2×2 panel, so the visual comparison remains compact or structural rearrangements, which elongated the internal
and the text flow stays uninterrupted. pathways of the graph. Another similar phenomenon can
be observed where one Beta sample produced a value of
F. Cross-Variant Comparative Trend
∼ 4×1010 (the highest in the dataset). Furthermore, a beta
The parallel-coordinate view (Fig. 3) highlights how graph-
sequencedroppeditsaverageclosenesscentralityto0.6,while
derived features evolve differently across variants while pre-
the remaining clade clusters were near 0.98–0.99, indicating
serving an overall shared structural backbone. Each polyline
structurally remote regions of the graph from a connectivity-
representsonegenomesample;colorencodesthevariantclass.
severing deletion. Finally, Beta’s maximum flow distribution
Thissupportstheideathatcodongraphtopologycapturesboth
is the widest of all four variants (spanning about 9.2 to 10.0),
conservedgenomeorganizationandvariant-specificsignatures
showinghighlyvariablecapacityforparallelinformationprop-
simultaneously. Note how features such as matching number
agation.

Fig.2. IndividualandCombinedstructuralprofilesforBeta,Gamma,Delta,andOmicron

TABLEIII
COMPARISONOFGENEXWITHGENEANNOTATIONTOOLSANDSARS-COV-2VARIANTCLASSIFICATIONMETHODS.GENEANNOTATIONACCURACIES
REFLECTNUCLEOTIDE-LEVELSENSITIVITY;VARIANTCLASSIFICATIONACCURACIESREFLECTMULTI-CLASSACCURACY.†WHOLE-GENOMESUPPORT
ASSUMESAVAILABILITYOFACLOSELYRELATEDREFERENCE.
Method Type Task Accuracy(reported) WholeGenome Reference
GENSCAN AbinitioHMM Geneannotation ∼70-80%(protein-level) ✓ [9]
GeneMark-ES/ET Abinitio(self-train) Geneannotation 35.7–75.8%(nucleotide) ✓ [10]
SNAP AbinitioHMM Geneannotation 77-80%(nucleotide) ✓ [17]
GlimmerHMM AbinitioHMM Geneannotation ∼9–43%(somedatasets) ✓ [12]
MAKER2 Annotationpipeline Geneannotation 68.60%(nucleotide) ✓ [14]
AUGUSTUS Abinitio+evidence Geneannotation 82–92%(gene-level) ✓ [11]
BRAKER2 Hybrid(RNA-seq+HMM) Geneannotation >AUGUSTUS(+2–3%) ✓ [13]
Helixer(DL) Deeplearning Geneannotation 86.8%(reported) ✓ [15]
k-mer+SVM TraditionalML Variantclassification ∼92.01% ✓ Various
CNN-LSTM Deeplearning Variantclassification ∼95–97% Partial Various
GenExLAPCG(Ours) Graph+ML(O(n)) Variantclassification 96.25% ✓ Thiswork
GenExMSCG(Ours) Graph+ML(multi-scale) Variantclassification 98.75% ✓ Thiswork
Fig. 3. Parallel-coordinate comparison of ten structural graph features across four SARS-CoV-2 variants of concern (Beta, Oct 2020; Gamma, Nov 2020;
Delta,Apr2021;Omicron,Nov2021).Eachpolylinerepresentsonevariant;colorencodesvariantclass.Thetenaxescorrespondto:secondeigenvalue(sev),
averageshortestpathlength(aspl),Wienerindex(wi),topeigenvalue(tev),radius(r),graphenergy(ge),diameter(d),averageclusteringcoefficient(aclu),
averageclosenesscentrality(aclo),andtransitivity(t).Allvaluesaremin–maxnormalisedto[0,1].Omicronconsistentlyoccupiesthehighestbandacross
spectralandcentralityaxes(ge,aclu,aclo),whileDeltaremainsneartheminimumonmostfeatures,highlightingasharpstructuraldivergencebetweenthese
twovariants.
2) Gamma (P.1): Among the four variants, Gamma dis- tributionamongthevariants,withoutliersreachingupto11.5.
plays the broadest intra-clade structural diversity within This physical elongation, along with the high betweenness
its clade. While the outlying values for the Beta variant centrality of Gamma, with outliers reaching up to ∼ 0.006,
are found in only certain graphical features, Gamma implies that specific sites in the genomic sequences act as
distributes its structural variability across multiple graph bridge notes controlling the information flow between distant
properties simultaneously, producing the most heteroge- genomic regions.
neous collection of genome graphs in the dataset. Inaddition,thegraphenergyofGammaoutliersreachesup
Gamma has ∼ 110 nodes (an upward outlier), the highest to ∼ 175, much higher than the typical 115–120 range. The
in the dataset, compared to the average median of 65–70 higher structural complexity suggests a different eigenvalue
across other variants, making Gamma a diverse and insertion- distribution and indicates recombinant or heavily mutated
rich sample; the largest connected component of a Gamma genome sequences. Moreover, Gamma displays the lowest
samplereaches∼115nodes,thehighestamongstallvariants. transitivity across the variants, outliers dropping to ∼ 0.84,
This variant tends not to form isolated subgraphs; rather, which suggests that local neighborhood structures are less tri-
it forms a single, unfragmented, interconnected giant graph. angulatedandtheotherwiseconservedco-occurrencerelation-
Furthermore,Gammahasthewidestandhighestdiameterdis- shipshavebeendisrupted.Overall,Gammashowssignsofex-

tensive evolutionary development; the graphs span the widest independent evolutionary landscape of Omicron and depicts
range of organizational forms: elongated, bridge-dominated, that its mutations are not clustered but are separate events.
andenergy-richstructures.Thisstructuralvariationdepictsthe Moreover, the structural diversification is evident in the
differentinsertioneventsoftheP.1lineage,creatingfunctional increased stable rank, reaching ∼ 1.75 for some Omicron
differences that require further investigation. sequences, whereas in other variants it lies in the 1.3–1.4
3) Delta (B.1.617.2): Delta is the most structurally range. Stable rank indicates a higher effective dimensionality,
disciplined variant in this dataset, producing genome which proves that Omicron graph structures occupy more
graphsthat arestructurallyconsistent,compact, andwell- complex and higher-dimensional spaces rather than being
clustered. mere scale-ups of previous variants. This diversity is also
Across almost every graph measure among the variants, shown by the increased Frobenius norm in Omicron graphs,
Delta has the tightest distributions, intra-clade variance, and which is ∼12.5 (compared to the typical ∼10.5), indicating
fewest extreme outliers, demonstrating the highest structural greaterstructuralmassandexpansioningenomicconnections.
conservation. It yielded small and consistent networks with However, the modularity does not hinder global coherence as
a median size of 65-70 nodes and approximately 2,000 Omicron has the highest median average closeness centrality
edges, reflecting a marked degree of uniformity in structural of ∼ 0.985, ensuring that the nodes are well integrated and
magnitude. The distribution of its Wiener index is close to efficiently traversable. Omicron has the highest median spec-
15,000, indicating that the Delta genome graph is highly tral gap, along with Beta (∼ 81.5), and indicates the widest
cohesive and replicable. Furthermore, Delta has a clustering overall spread; this indicates a high algebraic strength, which
coefficient with a median of ∼ 0.955 (marginally lower than will enable its functionality even when certain epitope-coding
Beta and Gamma). The slight relaxation in triplet formation regions are disrupted. Overall, with transitivity and average
within this genomic network is consistent with the double- clustering remaining around 0.96, except for one downward
mutation feature of Delta (L452R and T478K), in which outlier, Omicron achieves a unique change. It maximizes
each region becomes slightly less mutually dependent on the structural modularity while keeping global resilience intact.
| others. Additionally, |     | its spectral |            | gap is     | the lowest | among          | all |               |              |     |                     |     |        |          |
| --------------------- | --- | ------------ | ---------- | ---------- | ---------- | -------------- | --- | ------------- | ------------ | --- | ------------------- | --- | ------ | -------- |
|                       |     |              |            |            |            |                |     | I. Structural | Similarities |     | and Dissimilarities |     | Across | Variants |
| four variants         | at  | ∼ 81.0,      | indicating | marginally |            | less algebraic |     |               |              |     |                     |     |        |          |
connectivity robustness. After identifying the unique structural identities of the four
In particular, Delta has no extreme outliers in either its variants individually, this section presents the comparative
|           |        |               |       |       |         |     |          | patterns | that emerged | across | the variants. |     | The | comparative |
| --------- | ------ | ------------- | ----- | ----- | ------- | --- | -------- | -------- | ------------ | ------ | ------------- | --- | --- | ----------- |
| condition | number | or its stable | rank, | which | results | in  | yielding |          |              |        |               |     |     |             |
aconsistentlywell-conditionedadjacencymatrixwithlinearly analysis has been categorized into four points: (i) conserved
|              |                |     |     |                |     |            |     | global structure, | (ii) | structural | clustering | through |     | hierarchical |
| ------------ | -------------- | --- | --- | -------------- | --- | ---------- | --- | ----------------- | ---- | ---------- | ---------- | ------- | --- | ------------ |
| independent, | non-redundant, |     | and | non-degenerate |     | structural |     |                   |      |            |            |         |     |              |
motifs.Moreover,Deltaalsomaintainsanextremelylowvalue analysis, (iii) patterns of divergence in specific variants, and
for its matching number at ∼ 3, which indicates that the (iv) the spectral characteristics unique to each variant.
|         |           |          |           |     |           |     |          | 1) ConservedGlobalTopologyAcrossVariants: |     |     |     |     |     | Oneofthe |
| ------- | --------- | -------- | --------- | --- | --------- | --- | -------- | ----------------------------------------- | --- | --- | --- | --- | --- | -------- |
| genomic | sequences | of these | variants’ |     | mutations | do  | not pro- |                                           |     |     |     |     |     |          |
duce independent modular components, keeping the genome most prominent cross-variant observations is the presence
|             |                     |            |       |         |          |                |         | of strong   | conservation, |     | with a highly |            | consistent | global |
| ----------- | ------------------- | ---------- | ----- | ------- | -------- | -------------- | ------- | ----------- | ------------- | --- | ------------- | ---------- | ---------- | ------ |
| a single,   | tightly             | integrated | graph | body.   | The      | sole exception |         |             |               |     |               |            |            |        |
|             |                     |            |       |         |          |                |         | small-world | topological   |     | architecture  | regardless |            | of the |
| is a single | extreme-low-density |            |       | outlier | at ∼ 0.3 | (the           | typical |             |               |     |               |            |            |        |
value is ∼0.97). This anomaly depicts a highly sparse graph strongevolutionarypressure.Forallthevariantsusedinthis
study,Beta,Gamma,Delta,andOmicron,thegenomicgraphs
| with fewer | edges; | probably | caused | by  | sequencing |     | artifact, |     |     |     |     |     |     |     |
| ---------- | ------ | -------- | ------ | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
highly defective genome, or large-scale deletion events rather demonstrate near-identical median values across fundamental
than true mutation biology. Except for this outlier, Delta’s graph theoretical features: median density of ∼ 0.95–0.97,
meanshortestpathlengthof∼6.2,mediandiameterof∼9.5,
| profile can | be defined | by  | maximum | conservation, |     | achieving |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
dominance by consolidating and optimizing a single, efficient andtransitivityandaverageclusteringcoefficient∼0.96–0.97.
|     |     |     |     |     |     |     |     | Average | betweenness | centrality | remains | consistently |     | low at |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ---------- | ------- | ------------ | --- | ------ |
genomic organization.
4) Omicron (B.1.1.529): The Omicron variant presents around 0.001 across all variants, thus implying the absence of
the most structurally complex and structurally modular any dominant bottleneck in globally yet locally strongly con-
|         |       |            |      |          |     |     |     | nected graphs. | This | convergence | of topological |     | characteristics |     |
| ------- | ----- | ---------- | ---- | -------- | --- | --- | --- | -------------- | ---- | ----------- | -------------- | --- | --------------- | --- |
| genomic | graph | profile in | this | dataset. |     |     |     |                |      |             |                |     |                 |     |
The most prominent graphical feature of Omicron is the is supported by similar spectral clustering results, including
|     |     |     |     |     |     |     |     | the largest | eigenvalue | ∼   | 85–86, graph | energy | ∼   | 115–120, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------------ | ------ | --- | -------- |
matchingnumber,whichreachesupto∼55,whereastheother
variants have a value of ∼ 3, 18 times lower than Omicron. and consistency in the second eigenvalue around 5.3 across
As the matching number indicates the size of an independent all four variants. This consistency of spectral graph features
depictsthatthestructuralcomplexityandgraphenergyremain
| maximum | edge | set, this | extreme | escalation |     | indicates | that |     |     |     |     |     |     |     |
| ------- | ---- | --------- | ------- | ---------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
the genome graph contains a vast array of structurally non- unchanged even with the emergence of new mutations on the
|              |             |     |         |      |              |     |          | surface, | thus indicating | that | the eigenvalue |     | spectrum | controls |
| ------------ | ----------- | --- | ------- | ---- | ------------ | --- | -------- | -------- | --------------- | ---- | -------------- | --- | -------- | -------- |
| overlapping, | independent |     | motifs. | From | a biological |     | perspec- |          |                 |      |                |     |          |          |
tive,thisisexplainedbythefactthatOmicronhasaccumulated the functionality and dynamics of the genome, such as syn-
more than 30 spike protein mutations located at distinct chronization and diffusion within the SARS-CoV-2 genome.
| independent | sequence | sites. | This | framework |     | measures | the |     |     |     |     |     |     |     |
| ----------- | -------- | ------ | ---- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |

2) Hierarchical Clustering: Hierarchical clustering on
the full set of graph-theoretic features produces a dendro-
gramthatrevealstwodistinctstructuralclusters:Betaand
Delta cluster together at a distance of approximately 5.7,
while Gamma and Omicron cluster together at a distance
of approximately 7.3. The two super-clusters merge at
a distance of approximately 9.6, indicating a substantial
structural divide between the two groups.
The Beta–Delta (distance ∼ 5.7) pairing is notable for
its disparity between phylogenetic classification based on
nucleotide sequence data and clustering of structures, which
classify Beta and Delta as the most structurally related pair,
regardless of arising independently from separate regions and
lineages.Thus,itcanbesaidthatBetaandDeltaconvergedon
a similar genomic graph through independent evolution; this
Fig.4. HierarchicalClusteringofSARS-CoV-2VariantsbyGraphFeatures.
phenomenon of convergence is probably driven by identical The ten features in x-axis correspond to: second eigenvalue (sev), average
functional constraints and features: higher binding affinity shortest path length (aspl), Wiener index (wi), top eigenvalue (tev), radius
(r), graph energy (ge), diameter (d), average clustering coefficient (aclu),
with the ACE2 receptor and immunity evasions. This {Beta,
average closeness centrality (aclo), and transitivity (t). All values are min–
Delta}clusterrepresentsanevolutionarystrategyofstructural max normalised to [0,1]. Omicron consistently occupies the highest band
consolidation, characterized by tighter distributions and fewer acrossspectralandcentralityaxes(ge,aclu,aclo),whileDeltaremainsnear
the minimum on most features, highlighting a sharp structural divergence
outlier events.
betweenthesetwovariants.
The Gamma—Omicron (distance ∼ 7.3) pair is also note-
worthyasGammaandOmicronsharemorestructuralsimilar-
ity with each other than with Beta or Delta, despite Gamma complexity, and disrupts local triangular structures. Thus, the
emerging from the B.1.1.28 lineage in Brazil and Omicron divergence in Gamma is more structurally coherent than that
emerging in South Africa and representing a deeply diverged of Beta: it shows a systematic structural reorganization in a
lineage of uncertain ancestral origin. The grouping of these subset of sequences rather than unrelated isolated changes.
two strains could indicate convergence, common mutational Delta diverges minimally and specifically. Its only major
patterns affecting genomically similar regions, or similar cross-variant departure is the extreme low-density outlier,
selective forces leading to structural convergence toward a which is likely artifactual. In all other respects, Delta’s dis-
similarsetofstructuralfeaturesrelevanttoimmuneavoidance tributions are the closest to the cross-variant consensus of
or transmission capabilities. The {Gamma, Omicron} cluster any clade. Delta’s structural divergence is negligible at the
follows an evolutionary path of growing structural complexity clade level, reinforcing its identity as the most evolutionarily
and divergence, with greater structural diversity and outlier conservative variant from a graph-theoretic perspective.
events. Omicron’s matching number provides its clearest and most
Eventually, the two super-clusters Beta, Delta and Gamma, consistent divergence. Unlike the outlier events in Beta and
Omicron merge at ∼9.6, representing a substantial structural Gamma,whicharevisibleinonlyafractionofsamples,Omi-
discontinuity between the two. cron’s elevated matching number is a systematic property that
3) Variant-Specific Structural Divergence: While the con- distinguishes the entire high end of the Omicron distribution
served global topology unifies all four variants at the fromallothervariants.Combinedwithitselevatedstablerank,
median level, each variant diverges from the others in Omicron’sdivergencereflectsagenuinestructuraltransition—
distinctwaysthatarespecifictoitsgraph-theoreticprofile. a qualitative change in the type of genome graph produced—
Beta diverges primarily through extreme outlier events in rather than quantitative extremes within an otherwise familiar
the Wiener index, condition number, and closeness centrality. structural framework.
These outliers occur independently and are not consistently 4) Spectral and Algebraic Divergence: Spectral and alge-
co-occurring within the same samples, suggesting that Beta braic analysis adds a second comparative layer. Although
harbors multiple distinct mechanisms of structural disruption thetopeigenvalueisextremelyconservedacrossallvariantsat
at the sublineage level. Beta’s structural divergence is there-
arangeof∼85–86,whichindicatesastrongglobalstructural
fore characterized by intra-clade heterogeneity rather than a similarity, the spectral gap (measures algebraic connectivity
systematic shift of the entire clade away from the median. robustness) differs significantly: both Beta and Omicron have
Gamma diverges when multiple structural complexity fea- the highest median values at about 81.5, Delta possesses the
tures are simultaneously increased, including larger diameter,
smallestat∼81.0,andGammafallsbetweenthem.Condition
higherbetweennesscentrality,greatergraphenergy,andlower number demonstrates the most divergent algebraic structure
transitivity. These properties may all stem from a shared from the rest; while being relatively small and stable for
cause: the inclusion of genomic material. This elongates the all other variants, the outlying condition number of a near-
graphs, creates bridge positions, raises the eigenvalue-based singular Beta adjacency matrix approaches an astronomical

value of roughly 4 × 1010, suggesting a very brittle, al- et al.,
|     |     |     |     |     |     |     |     |     | [2] . Avsec, | V. Agarwal, | D. Visentin, |     | “Effective |     | gene expression |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------------ | --- | ---------- | --- | --------------- |
predictionfromsequencebyintegratinglong-rangeinteractions,”Nature
| gebraically | sensitive |     | graph | prone | to big | perturbations. |     | This |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ----- | ----- | ------ | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Methods,vol.18,pp.1196–1203,2021.
createsasharpcontrastwiththeconsistentlywell-conditioned
[3] E.Garrison,J.Sire´n,A.M.Novak,G.Hickey,J.M.Eizenga,E.T.Daw-
| Delta graphs | and | structurally |     | robust | Omicron | graphs. | Further- |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | ------ | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
son,W.Jones,S.Garg,C.Markello,M.F.Lin,B.Paten,andR.Durbin,
“Variationgraphtoolkitimprovesreadmappingbyrepresentinggenetic
more,whiletheFrobeniusnorm(reflectstheoverallmagnitude
variationinthereference,”NatureBiotechnology,vol.36,pp.875–879,
| of the adjacency |     | matrix) | remains |     | relatively | constant |     | for all |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------- | --- | ---------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Oct.2018.
variants at about 10.5, Omicron displays its own set of [4] M.Zitnik,M.Agrawal,andJ.Leskovec,“Modelingpolypharmacyside
outliers reaching 12.5. This elevated structural mass further effects with graph convolutional networks,” Bioinformatics, vol. 34,
pp.i457–i466,June2018.
| corroborates | Omicron’s |     | unique | matching |     | number | and | stable |                |       |           |        |               |     |               |
| ------------ | --------- | --- | ------ | -------- | --- | ------ | --- | ------ | -------------- | ----- | --------- | ------ | ------------- | --- | ------------- |
|              |           |     |        |          |     |        |     |        | [5] J. Gilmer, | K. T. | Schtt, P. | Glawe, | G. Klambauer, |     | A. Smola, and |
rank, reinforcing that it represents a quantitatively distinct, M. Welling,“Neural message passingfor quantum chemistry,”in Pro-
complex structural state at the algebraic level. ceedings of the 34th International Conference on Machine Learning,
ICML,2017.
In summary, viral graph evolution appears to follow two [6] M. O. Dayhoff, R. M. Schwartz, and B. C. Orcutt, “A model of
concurrenttrends:theconservationofstructuralbackboneand evolutionary change in proteins,” in Atlas of Protein Sequence and
variant-specific algebraic fingerprints. The clustering achieved Structure (M. O. Dayhoff, ed.), vol. 5, pp. 345–352, Washington DC:
NationalBiomedicalResearchFoundation,1978.
| by the | GenEX | pipeline | differs | from | that | of sequence-only |     |     |     |     |     |     |     |     |     |
| ------ | ----- | -------- | ------- | ---- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[7] S.HenikoffandJ.G.Henikoff,“Aminoacidsubstitutionmatricesfrom
phylogeny,indicatingthatgraph-theoreticanalysiscapturesan proteinblocks,”ProceedingsoftheNationalAcademyofSciencesofthe
additional axis of viral evolution that complements sequence- UnitedStatesofAmerica,vol.89,pp.10915–10919,Nov.1992.
|     |     |     |     |     |     |     |     |     | [8] A. Shrikumar, | P.  | Greenside, | and A. | Kundaje, | “Learning | important |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ------ | -------- | --------- | --------- |
based methods.
featuresthroughpropagatingactivationdifferences,”2019.
VI. CONCLUSION [9] C. Burge and S. Karlin, “Prediction of complete gene structures in
humangenomicdna,”JournalofMolecularBiology,vol.268,pp.78–
| Here, | we presented |     | a unified |     | benchmarking |     | pipeline | for | 94,Apr.1997. |     |     |     |     |     |     |
| ----- | ------------ | --- | --------- | --- | ------------ | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
[10] A.Lomsadze,V.Ter-Hovhannisyan,Y.O.Chernoff,andM.Borodovsky,
| the structural |     | analysis | of SARS-CoV-2 |     | variants: |     | Beta, | Delta, |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ------------- | --- | --------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
“Geneidentificationinnoveleukaryoticgenomesbyself-trainingalgo-
| Gamma, | and | Omicron, | at  | the nucleotide |     | and | codon | level, |     |     |     |     |     |     |     |
| ------ | --- | -------- | --- | -------------- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
rithm,”NucleicAcidsResearch,vol.33,pp.6494–6506,Nov.2005.
[11] M.Stanke,M.E.Diekhans,R.Baertsch,andD.Haussler,“Usingnative
| through | graphical     | analysis |     | of the | codon      | interaction | network     |     |                  |        |      |            |     |         |              |
| ------- | ------------- | -------- | --- | ------ | ---------- | ----------- | ----------- | --- | ---------------- | ------ | ---- | ---------- | --- | ------- | ------------ |
|         |               |          |     |        |            |             |             |     | and syntenically | mapped | cDNA | alignments | to  | improve | de novo gene |
| system. | We introduced |          | two | novel  | algorithms |             | to overcome |     |                  |        |      |            |     |         |              |
finding,”Bioinformatics,vol.24,no.5,pp.637–644,2008.
| the limitations |     | of linear | sequence |     | analysis, | currently |     | used |            |             |         |           |           |           |           |
| --------------- | --- | --------- | -------- | --- | --------- | --------- | --- | ---- | ---------- | ----------- | ------- | --------- | --------- | --------- | --------- |
|                 |     |           |          |     |           |           |     |      | [12] W. H. | Majoros, M. | Pertea, | and S. L. | Salzberg, | “TigrScan | and Glim- |
merHMM:twoopensourceabinitioeukaryoticgene-finders,”Bioinfor-
| in genome | sequence |     | analysis: | (i) | Linear-time |     | Adjacency |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | --------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
matics,vol.20,pp.2878–2879,Nov.2004.
| PMI Codon | Graph |     | (LAPCG) | and | (ii) | Multi-Scale | Codon |     |            |                    |     |                |     |            |         |
| --------- | ----- | --- | ------- | --- | ---- | ----------- | ----- | --- | ---------- | ------------------ | --- | -------------- | --- | ---------- | ------- |
|           |       |     |         |     |      |             |       |     | [13] K. J. | Hoff, A. Lomsadze, |     | M. Borodovsky, | and | M. Stanke, | “Whole- |
Co-occurrence Graph (MSCG). By representing genomic genomeannotationwithBRAKER,”inMethodsinMolecularBiology,
sequences as interaction networks and extracting spectral and vol.1962,pp.65–95,2019.
[14] C.HoltandM.Yandell,“MAKER2:anannotationpipelineandgenome-
| topological | features, |     | we demonstrated |     |     | that variants | possess |     |          |            |      |                       |     |        |            |
| ----------- | --------- | --- | --------------- | --- | --- | ------------- | ------- | --- | -------- | ---------- | ---- | --------------------- | --- | ------ | ---------- |
|             |           |     |                 |     |     |               |         |     | database | management | tool | for second-generation |     | genome | projects,” |
unique structural fingerprints that can be accurately classi- BMCBioinformatics,vol.12,p.491,2011.
fied using machine learning models such as Random Forests, [15] F.Stiehler,M.Steinborn,S.Scholz,D.Dey,A.P.M.Weber,andA.K.
|     |     |     |     |     |     |     |     |     | Denton, | “Helixer: | cross-species | gene | annotation | of  | large eukaryotic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------------- | ---- | ---------- | --- | ---------------- |
Extra Trees, and LightGBM. The structural interpretation genomesusingdeeplearning,”Bioinformatics,vol.36,pp.5291–5298,
| of these | networks | provided |     | critical | insights | into | the | virus’s | Apr.2021. |     |     |     |     |     |     |
| -------- | -------- | -------- | --- | -------- | -------- | ---- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
evolutionary trajectory. [16] National Center for Biotechnology Information, “Ncbi.” https://www.
|       |     |                  |     |           |     |           |            |     | ncbi.nlm.nih.gov/,2026. |     | Accessed:2026-02-22. |     |     |     |     |
| ----- | --- | ---------------- | --- | --------- | --- | --------- | ---------- | --- | ----------------------- | --- | -------------------- | --- | --- | --- | --- |
| LAPCG | is  | a well-optimized |     | algorithm |     | for graph | extraction |     |                         |     |                      |     |     |     |     |
[17] I.Korf,“Genefindinginnovelgenomes,”BMCBioinformatics,vol.5,
and feature computation that uses direct-neighbor approxi- p.59,May2004.
| mation         | to achieve     | linear-time    |           | complexity    |            | O(n).        | In contrast, |      |     |     |     |     |     |     |     |
| -------------- | -------------- | -------------- | --------- | ------------- | ---------- | ------------ | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
| MSCG           | is a           | mathematically |           | principled    |            | approach     | with         | the  |     |     |     |     |     |     |     |
| capability     | to             | model          | complex   | inter-context |            | dependencies |              | at   |     |     |     |     |     |     |     |
| multiple       | co-occurrence  |                | scales.   | Based         | on         | our results, | MSCG         |      |     |     |     |     |     |     |     |
| (utilizing     | Normalized     |                | PMI       | and           | positional | node         | encoding)    |      |     |     |     |     |     |     |     |
| has maintained |                | an accuracy    |           | of 98.75%,    |            | hence        | establishing |      |     |     |     |     |     |     |     |
| a robust,      | alignment-free |                | framework |               | for        | genomic      | analysis.    |      |     |     |     |     |     |     |     |
| Although       | currently      | focused        |           | on codon      | transition |              | patterns,    | this |     |     |     |     |     |     |     |
workidentifiesvitaltopologicalbiomarkersandexplainability
ofviralgenomesequencesacrosscladesandgenerations,using
mathematicalandgraphicalmodels.Futureresearchwillfocus
| on integrating |            | protein    | structural |           | data and | time-aware |     | viral |     |     |     |     |     |     |     |
| -------------- | ---------- | ---------- | ---------- | --------- | -------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| genomic        | evolution, | and        | on         | extending | this     | pipeline   | to  | other |     |     |     |     |     |     |     |
| viruses        | and higher | organisms. |            |           |          |            |     |       |     |     |     |     |     |     |     |
REFERENCES
[1] J.ZhouandO.Troyanskaya,“Predictingeffectsofnoncodingvariants
| with | deep learningbased |     | sequence | model,” |     | Nature Methods, |     | vol. 12, |     |     |     |     |     |     |     |
| ---- | ------------------ | --- | -------- | ------- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
pp.931–934,2015.
---- END DOCUMENT ----
