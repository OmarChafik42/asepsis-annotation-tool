Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
An Approach to Study the Structural Consistency of
Triangle Badness Functions and Distance Metrics
Bowen Liu1∗ Yizhou Wang2† Lingqian Meng3‡
1Shenzhen MSU–BIT University, Faculty of Computational Mathematics and Cybernetics,
1 International University Park Road, Dayun New Town, Longgang District, Shenzhen, Guangdong
Province 518172, P.R. China.
2Lomonosov Moscow State University, Faculty of Computational Mathematics and Cybernetics,
Leninskie Gory 1–52, Moscow 119991, Russian Federation.
Abstract
Triangle-based measures, commonly referred to as badness functions, are widely em-
ployed to quantify the extent to which a distance matrix deviates from an ideal geometric
configuration. Different formulations of these functions may capture distinct facets of local
non-uniformity, and their behavior is often influenced by the underlying distance metric
chosen for evaluation. In practical settings, although a canonical badness function may be
conceptuallypreferred, factorssuchascomputationalcost, algorithmicconstraints,ordata-
specificcharacteristicsfrequentlynecessitatetheadoptionofmodifiedversions—forinstance,
approximate forms or alternatives defined under different distance metrics. This gives rise
to a central question: to what degree do these variants retain the structural consistency
properties of their original counterparts? To address this issue, we develop a systematic
correlation-based framework for evaluating structural consistency. As an illustrative in-
stantiation of this framework, we compute badness sequences from a set of representative
distance matrices alongside randomly generated triangle configurations, which are designed
to cover variants that may arise under diverse practical scenarios. We then assess pairwise
similarities among these sequences using four correlation coeﬀicients. The experimental
outcomes indicate that certain badness variants exhibit a notably high degree of structural
consistency,whereasothersrevealcomplementarybehavioralpatterns; moreover,thechoice
of distance metric exerts a considerable influence on the observed trends. These findings
offer practical insights for the informed selection of distance metrics and triangle badness
function variants in tasks including geometric reconstruction, triangulation, and structural
analysis of pairwise distance data.
Keywords: Triangle Badness Function, Distance Metric, Structural Consistency, Rank Corre-
lation.
1 Introduction
The hypothesis of the molecular clock of evolution emerged from the observation that the
numberofaminoaciddifferencesbetweenhomologousproteinsisapproximatelyproportionalto
∗BowenLiu: Correspondingauthor. Student,FacultyofComputationalMathematicsandCybernetics,Shen-
zhen MSU–BIT University; email: liubowenmbu@outlook.com.
†Yizhou Wang: Methodology and Computational Analysis Lead. Master’s Student, Department of Automa-
tion for Scientific Research, Faculty of Computational Mathematics and Cybernetics, Lomonosov Moscow State
University; email: saipeizyu@gmail.com.
‡LingqianMeng: PhDStudent,DepartmentofAlgorithmicLanguages,FacultyofComputationalMathematics
and Cybernetics, Lomonosov Moscow State University; email: menglq@cs.msu.ru.
1
6202
guA
42
]GM.htam[
1v76232.8062:viXra

the time elapsed since the divergence of the corresponding organisms [35][34][26]. This observa-
tion was later incorporated into Kimura’s neutral theory of molecular evolution [22][19][21][23],
which assumes that a large proportion of mutations are selectively neutral and that their fixa-
tion is governed by stochastic processes such as genetic drift. Within this framework, the rate
of molecular evolution can be considered approximately constant over time.
As a consequence, evolutionary distances derived from sequence data often exhibit regular
structural patterns. In particular, when evolutionary rates are approximately homogeneous
across lineages, pairwise distances between closely related taxa tend to satisfy near-ultrametric
constraints [15], implying that triples of taxa form approximately isosceles (or equilateral) tri-
angle configurations. This geometric property reflects the idea that sequences diverging from a
common ancestor over comparable time spans accumulate similar numbers of substitutions.
However, real-world molecular data frequently deviate from this idealized behavior. Rate
heterogeneity, slightly deleterious mutations, generation-time effects, and other biological fac-
tors introduce variabilityin substitution rates, leading to violations of the strict molecular clock
assumption [21] [20] [16] [24] [17]. Consequently, the resulting distance matrices are only ap-
proximately ultrametric, and the corresponding triangle configurations may deviate from the
ideal isosceles structure.
Furthermore, similar considerations arise in distance-based triangulation problems, where
triangle structures are used to characterize geometric consistency. Distance-based triangulation
methods [28] [29] are fundamental techniques for reconstructing point configurations from pair-
wise distances and are widely used in applications such as sensor network localization, robotic
mapping, and spatial reconstruction. Moreover, these triangulation techniques are often used
as a preprocessing step for subsequent computational tasks. For example, in certain solution
approaches to the traveling salesman problem (TSP) [30], methods such as the onion-husk al-
gorithm [1] utilize distance-based reconstruction to improve tour construction. In the ideal case
of exact distance measurements, triangulation yields consistent and accurate coordinates. How-
ever, inpracticalsettings, distancedataareoftencorruptedbynoiseandrandomerrors, leading
to inconsistencies between the reconstructed configuration and the true geometric structure.
From a geometric perspective, the triangulation process inherently relies on local triangle
structures: each new point is typically determined by forming triangles with already known
points. Whendistancedataarenoisy,differenttriangleconfigurationsexhibitvaryingsensitivity
to perturbations, resulting in geometric uncertainty. This phenomenon is closely related to the
concept of geometric dilution of precision (GDOP) [3], which was introduced to quantify the
impact of geometric configurations on positioning accuracy [18] [25] [32]. Similar considerations
naturally arise in triangulation problems with noisy inputs. In such settings, analyzing the
structure of local triangles provides a natural and effective way to assess the stability of the
reconstruction.
Intheastrophysicalnumericalmeasurementscalculation, forextremelysmallparallax, i.e.,
extremely narrow acute triangle, additional methods are often required, such as Bayesian spa-
tial reconstruction methods based on the prior distribution of galaxy density, to reconstruct
the data [6]. For materials characterization, data need to be triangulated using, i.e., Delaunay
algorithm to connect isolated points into physically meaningful material surfaces or internal
grains [14]. In materials measurements, the coherence and speckle noise of laser instruments
can cause measurement errors [4]. Noise processing is necessary during reconstruction through
experimental characterization of the microstructure, generation with geometrical methods con-
centrating solely on mimicking the morphology, et cetera [13]. The study of triangle structural
properties can be used to construct relevant criteria for noise removal algorithms and triangle
reconstruction processes.
Based on the above observations, triangles can be viewed as fundamental units for captur-
ing local consistency and deviations, both in evolutionary distance analysis and in geometric
reconstruction problems.
2

These deviations naturally motivate the introduction of quantitative measures to capture
the extent to which local triangle configurations depart from ideal geometric constraints. Such
measures, referred to in this paper as badness functions, can be interpreted as local indicators
of inconsistency with respect to an underlying evolutionary model or geometric structure.
Importantly, different definitions of badness may emphasize different aspects of deviation,
such as imbalance of edge lengths or angular distortion. From an optimization perspective,
these functions often arise as surrogate objectives designed to satisfy specific requirements of
optimization algorithms, such as smoothness, computational tractability, or robustness. As a
result, different badness functions may correspond to different approximations of the original
problem, potentially distorting its intrinsic structure. Moreover, different choices of distance
metrics can also lead to varying results.
This observation motivates a key question: to what extent do different triangle badness
functions respond consistently to the same underlying geometric structures? Additionally, how
dodifferentdistancemetricsaffecttheresults,andtowhatextentdotheyinfluencetheobserved
patterns?
To address this question, we propose a systematic evaluation framework in which four
distinct correlation coeﬀicients are used to quantify consistency across different scenarios. Each
correlation coeﬀicient will be introduced in detail in the following sections.
The remainder of this article is organized as follows. In Section 2, weintroduce the triangle
badness functions used in this study as representative examples. We do not provide a detailed
discussion of the specific distance measures, as these are standard distances adopted from ex-
isting literature and are described in detail in the experimental design. Section 3 presents
the rank correlation methods employed to quantify the structural similarity between badness
sequences, explaining the significance of each coeﬀicient. In Section 4, we describe the experi-
mentalsetup, includingdatasetselection, preprocessing,andcomputationofbadnesssequences.
Finally, Section 5 reports the correlation results obtained from these experiments and provides
an interpretation of the findings.
2 Triangle Badness Functions
In this work, we investigate several badness functions designed to quantify local geometric
deviations of triangles. Although the concrete formulations differ, all considered functions are
motivatedbythesameunderlyingobjective: identifyingtrianglesthatareclosetoacuteisosceles
configurations.
This choice is closely related to the observations discussed in the previous section. In
evolutionary distance data approximately satisfying the molecular clock hypothesis, pairwise
distances between taxa often exhibit near-ultrametric structures due to approximately homo-
geneous mutation accumulation across lineages. Consequently, triples of taxa frequently form
approximately isosceles triangle configurations. Similarly, in distance-based triangulation and
geometric reconstruction problems, acute and geometrically balanced triangles are generally
associated with improved numerical stability and robustness. Therefore, in both evolutionary
distance analysis—such as among closely related species—and geometric reconstruction prob-
lems, the extent to which triangles naturally approximate acute isosceles configurations needs
to be evaluated.
Based on these observations, we consider the following classes of badness functions for
describing geometric deviations. In this work, acute triangles of interest are defined specifically
◦
as those with a vertex angle smaller than 60 .
3

2.1 Badness Based on the Angle Between the Angle Bisector and the Median
The first badness function is based on the angle between the angle bisector and the median
| constructed | from | the same | vertex | of  | a triangle. |     |     |
| ----------- | ---- | -------- | ------ | --- | ----------- | --- | --- |
For a triangle with side lengths a,b,c, let θ denote the angle between the angle bisector
and the median corresponding to a selected vertex. The badness is defined by
|     |     |     |     |     |     | B BM = θ. |     |
| --- | --- | --- | --- | --- | --- | --------- | --- |
In this work, we select the vertex corresponding to the smallest angle of the triangle.
This choice is motivated by the following geometric observation: for an isosceles triangle
within the set of acute triangles considered in this study (i.e., with a vertex angle smaller than
◦
60 ), the vertex angle is precisely the smallest angle of the triangle. Therefore, when searching
for configurations close to acute isosceles triangles, the smallest angle naturally identifies the
| most likely | isosceles | vertex. |     |     |     |     |     |
| ----------- | --------- | ------- | --- | --- | --- | --- | --- |
Moreover, the value of this function becomes zero if and only if the median and the angle
bisector coincide at the selected vertex, uniquely identifying the target acute isosceles triangle
without deviation. Consequently, this function reliably evaluates the triangle, ensuring that the
measuredquantitypointsdirectlytothedesiredconfigurationratherthanreflectingunintended
departures.
| 2.2 Combined |     | Isosceles |     | and | Acute | Violation | Function |
| ------------ | --- | --------- | --- | --- | ----- | --------- | -------- |
Thesecondbadnessfunction,introducedin[27],separatelymeasuresdeviationsfromisosce-
les structures and deviations from acute-angle structures, and then combines them into a single
quantity.
| First, | the | triangle is | reordered |     | such  | that   |        |
| ------ | --- | ----------- | --------- | --- | ----- | ------ | ------ |
|        |     |             |           | a   | ≥ b ≥ | c, α ≥ | β ≥ γ, |
where a,b,c denote the side lengths and α,β,γ denote the corresponding angles.
| The | isosceles | violation | term | is  | defined | as  |     |
| --- | --------- | --------- | ---- | --- | ------- | --- | --- |
|     |           |           |      |     |         | (   | )   |
|     |           |           |      |     |         | b   | c   |
1−min
|     |     |     |     |     | B = |     | , . |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | iso | a   | b   |
This term measures imbalance among the side lengths. The value becomes smaller when
| two sides | are closer  | to each   | other. |      |            |     |     |
| --------- | ----------- | --------- | ------ | ---- | ---------- | --- | --- |
| The       | acute-angle | violation |        | term | is defined | as  |     |
max(α−π/3,0)
|     |     |     |     | B   |     | =   | .   |
| --- | --- | --- | --- | --- | --- | --- | --- |
acute
2π/3
This penalty applies to triangles based on their largest angle: the larger the largest angle,
| the greater | the   | penalty.   |         |     |     |           |     |
| ----------- | ----- | ---------- | ------- | --- | --- | --------- | --- |
| The         | final | badness is | defined | as  |     |           |     |
|             |       |            |         |     |     | B +B      |     |
|             |       |            |         |     |     | iso acute |     |
|             |       |            |         |     | B   | =         | .   |
|             |       |            |         |     | IA  | 2         |     |
Compared with the previous bisector–median formulation, this definition explicitly sep-
arates isosceles deviation and acute-angle deviation into two independent components before
combining them. The underlying idea is that local geometric irregularity may originate from
different sources, which can first be measured individually and then aggregated into a unified
quantity.
4

Such a decomposed structure is advantageous in statistical analysis and optimization prob-
lems, since different types of perturbations may affect edge-length structures and angular struc-
tures differently. Separating these contributions allows clearer analysis of their individual ef-
fects.
| 2.3 Delta-Regularized |     |     | Isosceles | Badness | Function |     |     |
| --------------------- | --- | --- | --------- | ------- | -------- | --- | --- |
The third badness function is mainly based on similarity among side lengths, and it intro-
| duces a small | regularization |     | parameter | δ > 0      | to improve | regularity. |     |
| ------------- | -------------- | --- | --------- | ---------- | ---------- | ----------- | --- |
| First,        | the triangle   | is  | reordered | such that  |            |             |     |
|               |                |     |           | a ≥ b ≥ c, | α ≥        | β ≥ γ,      |     |
where a,b,c denote side lengths and α,β,γ denote the corresponding angles.
| The | function is | defined | as follows: |     |     |     |     |
| --- | ----------- | ------- | ----------- | --- | --- | --- | --- |
|     |             |         |             |     | b   | c   |     |
1−
|     |     |     | diff | =      | +         |     | ,   |
| --- | --- | --- | ---- | ------ | --------- | --- | --- |
|     |     |     |      | ab a+δ | (a+b)/2+δ |     |     |
c a
|     |     |     | diff | = 1− | +   |     | ,   |
| --- | --- | --- | ---- | ---- | --- | --- | --- |
bc
|     |     |     |     | b+δ      | (b+c)/2+δ |     |     |
| --- | --- | --- | --- | -------- | --------- | --- | --- |
|     |     |     |     | max{diff |           | }.  |     |
|     |     |     |     | B =      | ,diff     |     |     |
|     |     |     |     | δ        | ab bc     |     |     |
nearbyside
The first part, 1− , measures deviation from isosceles structure, while the sec-
largerside+δ
ond part, remainingside , introduces additional geometric information from the side not
averageofclosestpair+δ
involved in the closest pair. By computing both possibilities and taking the maximum, the
| function | captures the | most | severe | deviation. |     |     |     |
| -------- | ------------ | ---- | ------ | ---------- | --- | --- | --- |
The design of this function is motivated not only by geometric considerations, but also by
the desire to obtain objective functions with favorable regularity properties for optimization
problems.
In many practical situations, distance matrices themselves depend on adjustable parame-
ters. Forexample,insequenceanalysis,pairwisedistancesmaydependonscoringparametersof
alignment algorithms such as Needleman–Wunsch, or on transformations converting similarity
scores into distances. In such cases, the badness function naturally becomes an optimization
objective.
To enable the application of global optimization methods based on Lipschitz continuity
assumptions,theobjectivefunctionisoftenrequiredtopossesssuitablecontinuityandregularity
properties.
Onepurposeofintroducingtheparameterδistoavoidundesirablebehaviorneardegenerate
configurations and improve the Lipschitz properties of the resulting objective function. In
addition, the function is formulated directly in terms of side lengths rather than angles. This
choice is motivated by the observation that transformations from edge lengths to angles may
introduce unfavorable nonlinear behavior near degenerate configurations, potentially weakening
or destroying desirable Lipschitz properties. By relying only on edge-based quantities, the
resulting badness function retains a more regular structure that is better suited for Lipschitz-
| based global | optimization |     | methods. |     |     |     |     |
| ------------ | ------------ | --- | -------- | --- | --- | --- | --- |
Consequently, thisfunctionnotonlymeasuresdeviationsfromisoscelesstructures, butalso
incorporates stability considerations relevant for subsequent optimization problems.
| 3 Rank      | Correlation |     |     | Methods |     |     |     |
| ----------- | ----------- | --- | --- | ------- | --- | --- | --- |
| 3.1 Badness | Sequences   |     |     |         |     |     |     |
The correlation analysis is formulated in terms of aligned badness sequences. Let
F ∈ {BM,IA,δ}
5

denote the badness function under consideration, where each symbol corresponds to a specific
function:
• BM—BadnessBasedontheAngleBetweentheAngleBisectorandtheMedian
| • IA | — Combined          |     | Isosceles |           | and Acute          | Violation | Function   |     |
| ---- | ------------------- | --- | --------- | --------- | ------------------ | --------- | ---------- | --- |
| • δ  | — Delta-Regularized |     |           | Isosceles | Badness            |           | Function   |     |
| For  | an individual       |     | triangle  | T,        | its triangle-level | badness   | is denoted | by  |
|      |                     |     |           |           | B                  | F (T).    |            |     |
For a distance matrix D, the corresponding matrix-level total badness is defined by aggregating
| over all | unordered | triples | induced |     | by the matrix: |     |     |     |
| -------- | --------- | ------- | ------- | --- | -------------- | --- | --- | --- |
∑
|     |     |     |     |     | B (D) = | B   | (T), |     |
| --- | --- | --- | --- | --- | ------- | --- | ---- | --- |
|     |     |     |     |     | F       |     | F    |     |
T∈T(D)
T(D)
| where | is  | the set | of all | triangles | determined | by D. |     |     |
| ----- | --- | ------- | ------ | --------- | ---------- | ----- | --- | --- |
Two types of sequences are considered. In triangle-level experiments, each observation is a
| single triangle, |     | and the | compared |     | sequences | have the | form |     |
| ---------------- | --- | ------- | -------- | --- | --------- | -------- | ---- | --- |
|                  |     |         |          |     | {B        | (T )}N   | .    |     |
|                  |     |         |          |     | F         | i i=1    |      |     |
These sequences describe how different badness functions rank individual triangles. In matrix-
level experiments, each observation is a complete distance matrix, and the compared sequences
| have the | form |     |     |     |     |        |     |     |
| -------- | ---- | --- | --- | --- | --- | ------ | --- | --- |
|          |      |     |     |     | {B  | (D )}M | .   |     |
|          |      |     |     |     | F   | i i=1  |     |     |
These sequences describe how different badness functions rank complete distance matrices after
| aggregating | local | triangle    | information. |     |     |     |     |     |
| ----------- | ----- | ----------- | ------------ | --- | --- | --- | --- | --- |
| 3.2 Pearson |       | Correlation |              |     |     |     |     |     |
Given two aligned numerical sequences x = (x ,...,x ) and y = (y ,...,y ), the Pearson
|             |            |     |     |     |     | 1   | n   | 1 n |
| ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| correlation | coeﬀicient |     | is  |     |     |     |     |     |
∑
|     |     |     |     |     |     | n −x¯)(y | −y¯) |     |
| --- | --- | --- | --- | --- | --- | -------- | ---- | --- |
(x i √∑i
|     |     |     | r (x,y) | =   | √∑  | i=1   |         | ,   |
| --- | --- | --- | ------- | --- | --- | ----- | ------- | --- |
|     |     |     | P       |     | n   | −x¯)2 | n −y¯)2 |     |
|     |     |     |         |     | (x  |       | (y      |     |
|     |     |     |         |     | i=1 | i     | i=1 i   |     |
where x¯ and y¯ are the sample means. Pearson correlation measures linear association between
| the numerical | badness |      | values.     |     |     |     |     |     |
| ------------- | ------- | ---- | ----------- | --- | --- | --- | --- | --- |
| 3.3 Spearman  |         | Rank | Correlation |     |     |     |     |     |
The Spearman rank correlation is the Pearson correlation applied to the ranks of the two
sequences:
|     |     |     |     |     | r S (x,y) = | r P (R(x),R(y)), |     |     |
| --- | --- | --- | --- | --- | ----------- | ---------------- | --- | --- |
where R(x) and R(y) denote the rank-transformed sequences. Spearman correlation measures
monotone agreement and is therefore directly relevant for determining whether two badness
| functions | induce | similar | orderings. |     |     |     |     |     |
| --------- | ------ | ------- | ---------- | --- | --- | --- | --- | --- |
6

| 3.4 Kendall | Tau-b | Correlation |     |     |     |     |     |
| ----------- | ----- | ----------- | --- | --- | --- | --- | --- |
The Kendall tau-b correlation compares the numbers of concordant and discordant pairs
| while correcting | for | ties: |     |     |     |     |     |
| ---------------- | --- | ----- | --- | --- | --- | --- | --- |
−n
|     |     |     |     |     | n c d |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     | τ   | = √ |     |       |     | .   |
b
|     |     |     | (n  | +n +t | )(n +n | +t  | )   |
| --- | --- | --- | --- | ----- | ------ | --- | --- |
|     |     |     |     | c d   | x c    | d y |     |
Here n c and n d are the numbers of concordant and discordant pairs, while t x and t y count tied
pairs occurring only in the first or second sequence, respectively. This coeﬀicient provides an
ordinal measure of pairwise ranking consistency and is appropriate when ties may occur in the
| badness   | sequences. |             |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | --- | --- | --- | --- |
| 3.5 Tukey | Biweight   | Correlation |     |     |     |     |     |
The Tukey biweight correlation is included as a robust measure of association. This coef-
ficient is based on median-centered values and Tukey weights, so observations farther from the
median receive smaller weights. In the form used here, if x˜ and y˜ denote medians and w (x) ,
i
(y)
w denote the corresponding Tukey biweight weights, the robust correlation is computed as
i
∑n
|     |     | r (x,y) | =   | w (x) | w (y) (x −x˜)(y | −y˜) |     |
| --- | --- | ------- | --- | ----- | --------------- | ---- | --- |
|     |     | B       |     | i     | i i             | i    |     |
i=1
|     |     |     |     | [   |     | ]   |      |
| --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | (   | )   | −1/2 |
∑n
2
|     |     |     |     | ×   | w (x) (x −x˜) |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- |
|     |     |     |     |     | i i           |     |     |
i=1
|     |     |     |     | [   |     | ]      |     |
| --- | --- | --- | --- | --- | --- | ------ | --- |
|     |     |     |     |     | (   | ) −1/2 |     |
∑n
2
|     |     |     |     | ×   | w (y) (y −y˜) |     | .   |
| --- | --- | --- | --- | --- | ------------- | --- | --- |
|     |     |     |     |     | i i           |     |     |
i=1
The biweight coeﬀicient is used as a diagnostic of structural similarity that is less sensitive
| to extreme         | badness | values than    | ordinary | linear | correlation. |     |     |
| ------------------ | ------- | -------------- | -------- | ------ | ------------ | --- | --- |
| 3.6 Interpretation |         | of Correlation |          | Values |              |     |     |
Inthepresentstudy,thefourcoeﬀicientsprovidecomplementaryevidenceabouttheconsis-
tency of different badness functions. Pearson correlation evaluates agreement in the numerical
scale of the badness values, Spearman and Kendall correlations evaluate agreement in the in-
duced rankings, and the Tukey biweight coeﬀicient evaluates whether the observed association
| is stable | under reduced | sensitivity | to  | extreme | observations. |     |     |
| --------- | ------------- | ----------- | --- | ------- | ------------- | --- | --- |
High positive correlations indicate that two badness functions reflect same geometric infor-
mation in a relatively consistent manner. At the triangle level, this means that the functions
assign similar rankings to individual triangles. At the matrix level, this means that the corre-
sponding total badness values B (D) rank complete distance matrices in a similar way.
F
| 4 Experimental |     | Design |     |     |     |     |     |
| -------------- | --- | ------ | --- | --- | --- | --- | --- |
Thepurposeoftheexperimentsistoinvestigatewhetherdifferenttrianglebadnessfunctions
preserve similar structural information across different types of distance data. For each triangle
| or distance | matric, | we compute | three | badness | values: |     |     |
| ----------- | ------- | ---------- | ----- | ------- | ------- | --- | --- |
|             |         |            | B     | ,       | B , B   | ,   |     |
|             |         |            |       | BM      | IA      | δ   |     |
whereB denotesthebisector–medianangularbadness,B denotesthecombinedisosceles–
|     | BM  |     |     |     |     |     | IA  |
| --- | --- | --- | --- | --- | --- | --- | --- |
acute violation function, and B denotes the δ-regularized edge-based badness function.
δ
7

4.1 Datasets
| We  | consider | six types |     | of experimental |     | data. |     |     |
| --- | -------- | --------- | --- | --------------- | --- | ----- | --- | --- |
4.1.1 Distance Matrices Computed by a Needleman–Wunsch-Like Algorithm
The first experiment uses 100 distance matrices computed using a Needleman–Wunsch-like
| dynamic | programming |     | algorithm |     | [33]. |     |     |     |
| ------- | ----------- | --- | --------- | --- | ----- | --- | --- | --- |
UnliketheclassicalNeedleman–Wunschformulationbasedonmaximizingalignmentscores,
we consider a cost-minimization formulation. Substitutions and gaps are assigned nonnegative
costs, and the distance between two sequences is defined as the minimum total transformation
cost over all admissible alignments. Computationally, this corresponds to replacing the max-
imization operation in the dynamic programming recurrence by a minimization operation and
| replacing | similarity | scores |     | by transformation |     | costs. |     |     |
| --------- | ---------- | ------ | --- | ----------------- | --- | ------ | --- | --- |
For each experiment, a random set of cost parameters is generated. These parameters in-
clude substitution costs and gap costs, all sampled independently from the uniform distribution
on [0,1]. The resulting distance construction is then applied to a dataset consisting of mito-
chondrial DNA sequences from 32 closely related monkey species. For each randomly generated
| parameter | set, | a complete |     | 32×32 | distance | matrix | is  | obtained. |
| --------- | ---- | ---------- | --- | ----- | -------- | ------ | --- | --------- |
Each matrix is treated as a complete weighted graph. For every unordered triple of indices,
| a triangle | is formed | using | the | corresponding |     | pairwise |     | distances. |
| ---------- | --------- | ----- | --- | ------------- | --- | -------- | --- | ---------- |
ForadistancematrixD,thetotalbadnesscorrespondingtoabadnessfunctionF isdefined
as
∑
B
|     |     |     |     |     | F (D) | =   | F(T), |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
T∈T(D)
| where T(D) | denotes |     | the set | of all | triangles | induced | by  | the matrix. |
| ---------- | ------- | --- | ------- | ------ | --------- | ------- | --- | ----------- |
Thus, for each distance matrix, we compute three total badness values corresponding to
the three badness functions. This produces three sequences of length 100.
The motivation of this experiment is closely related to optimization problems. Since the
distance matrix depends on adjustable alignment cost parameters, the total badness naturally
becomes an optimization objective. Therefore, it is important to determine whether different
badness functions produce similar structural evaluations and whether they may lead to similar
| optimization |     | behavior. |     |     |     |     |     |     |
| ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
4.1.2 Jaro–Winkler and Needleman–Wunsch-Like Distance Matrices
The second experiment uses two fixed biological distance matrices. The first matrix is
basedontheJaro–Winklerdistance,whilethesecondmatrixiscomputedusingtheNeedleman–
| Wunsch-like | cost-minimization |     |     | distance |     | described | above. |     |
| ----------- | ----------------- | --- | --- | -------- | --- | --------- | ------ | --- |
For the Needleman–Wunsch-like distance matrix used in this experiment, the substitution
costs and gap costs are all fixed to 1. The same dataset of 32 monkey mitochondrial DNA
| sequences | is used. |         |               |     |         |            |     |             |
| --------- | -------- | ------- | ------------- | --- | ------- | ---------- | --- | ----------- |
| For       | each     | matrix, | all unordered |     | triples | of indices | are | enumerated. |
Unlike the previous experiment, here we do not directly aggregate badness values over all
triangles. Instead, for every triangle T, we store the three corresponding badness values:
|     |     |     |     | B   | (T), | B   | (T), | B (T). |
| --- | --- | --- | --- | --- | ---- | --- | ---- | ------ |
|     |     |     |     |     | BM   | IA  |      | δ      |
This produces triangle-level badness sequences for the two biological distance matrices, al-
lowingamoredetailedcomparisonofthelocalgeometricstructuresinducedbythetwodistance
definitions.
8

The purpose of this experiment is to investigate whether different sequence distance algo-
rithmsinducesimilartrianglestructuresfromtheperspectiveoftheproposedbadnessfunctions.
4.1.3 Randomly Generated Triangles
Thethirdexperimentdirectlygeneratesrandomtriangles. Tworandomgenerationschemes
are considered.
The first scheme generates triangles by randomly sampling three side lengths indepen-
dently from the interval [1,10] and retaining only triples satisfying the triangle inequality. This
produces an edge-based random triangle model.
The second scheme generates triangles by randomly partitioning the interval (0,π) into
three angles. The corresponding side lengths are then computed using the sine rule, while the
smallest side is normalized to 1. This produces an angle-based random triangle model.
For each generation scheme, 10000 triangles are generated. For every triangle, the three
badness values are computed and stored.
Thepurposeofthisexperimentistoinvestigatewhetherthedifferentbadnessfunctionsex-
hibit similar behavior in general random geometric settings, independently of specific biological
or Euclidean datasets.
4.1.4 Euclidean Distance Matrices from Random Planar Points
The fourth experiment uses synthetic Euclidean distance matrices generated from random
planar points.
Inthissetting, 100independentpointsetsaregenerated, eachcontaining99randompoints
in the plane. For each point, both the x-coordinate and the y-coordinate are sampled indepen-
dently from the uniform distribution on the interval [0,1]. The corresponding 99×99 Euclidean
distance matrix is then computed from the generated point set.
Each distance matrix defines a complete collection of triangles. For every matrix, we
enumerate all unordered triples of points and compute the total badness values induced by the
three badness functions. This produces three badness sequences of length 100.
This experiment provides a controlled Euclidean setting in which the distance matrices
satisfy the triangle inequality up to numerical precision.
Thepurposeofthisexperimentistoinvestigatewhetherdifferentbadnessfunctionspreserve
similargeometricinformationinordinaryEuclideansettingsandwhethertheirbehaviorremains
consistent in general geometric distance data.
4.1.5 Triangles for parallax method based on Gaia data
ThefifthexperimentusesdatafromEuropeanSpaceAgency(ESA)missionGaia,processed
by the Gaia Data Processing and Analysis Consortium (DPAC) [7, 8].
Using the astronomical data query interface of Gaia data, we downloaded 100 datasets
grouped by the parallax value span of 0.5, i.e., each dataset contained data with parallax
values falling within the range of [m/2,(m+1)/2),m = 0,1,2,...,99. For parallax levels with
suﬀicient data, we take 1000 astronomical measurement data points; if a level has less than
1000 data points, we use all of them. Each dataset contains the parallax and parallax error
of every measurement data point. We sampled each data point with normal distribution using
the parallax as the expectation and the parallax error as the standard deviation. Based on the
original parallax value and the sampled parallax value, we constructed right-angled triangles to
calculatethemeasurementdistances. Thethirdsideiscalculatedviathelawofcosinesfromthe
distances, the parallax angle and the sampled parallax angle. The method for calculating the
third side bases on the fundamental purpose of carrying the significance of the Earth’s orbital
baseline; meanwhile, this method avoids the problem of invalid length relation due to sampling.
9

We then constructed “synthetic” (heuristic) triangles with the obtained distances as its side
lengths. These triangles are considered to be capable of simulating the triangles which may
| occur in | astronomical | measurements. |     |     |     |     |     |
| -------- | ------------ | ------------- | --- | --- | --- | --- | --- |
In this setting, we obtain 100 sets of data, which contain 69806 triangles. These grouped
data are used to calculate matrix-level badness, thereby studying the properties of triangles at
different levels of parallax. Since the amount of data in each data group is different, we use a
| normalized | version    | of matrix-level |     | badness. |     |            |     |
| ---------- | ---------- | --------------- | --- | -------- | --- | ---------- | --- |
| The        | normalized | matrix-level    |     | badness  | is  | defined as |     |
∑
B F (T)
T∈T(D)
B′
|         |               |     |          | (D)    | =          |         | .     |
| ------- | ------------- | --- | -------- | ------ | ---------- | ------- | ----- |
|         |               |     |          | F      |            | |T(D)|  |       |
| For the | 100 matrices, | we  | consider | the    | collection |         |       |
|         |               |     |          | {      | }          |         |       |
|         |               |     |          | B′     | 100        | |T(D )| | ≤     |
|         |               |     |          | (D i ) | ,          | i       | 1000. |
|         |               |     |          | F      | i=1        |         |       |
We continue to use these 69806 triangles at the triangle level. Triangle-level computational
experiments can reveal the correlation between badness functions and data at different error
| levels in | astronomical | calculations. |     |     |     |          |     |
| --------- | ------------ | ------------- | --- | --- | --- | -------- | --- |
|           |              |               |     |     | {B  | )}69806. |     |
F (T i
i=1
4.1.6 Triangles in crystal structures based on Materials Project data
| The | sixth experiment |     | uses | data from | Material | Project | [5, 10]. |
| --- | ---------------- | --- | ---- | --------- | -------- | ------- | -------- |
Crystal material data are downloaded via the Material Project API. For each material,
the first stage of selection involves triangulation using the Delaunay algorithm [31, 2] (imple-
mented in Scipy [11]). If the material’s spatial structure is three-dimensional, all faces of the
tetrahedrons provided by the Delaunay algorithm are extracted and deduplicated. The second
stage of selection utilizes the presence of chemical bonds using CrystalNN tool [9, 12]. Thus, for
materials, we extract different numbers of “synthetic” (heuristic) triangles, which are consid-
eredcrystal-chemicallyplausible, insteadofrepresentingtheatomicconfigurationasacomplete
| graph and | enumerating |     | all atomic | triplets | as  | possible triangles. |     |
| --------- | ----------- | --- | ---------- | -------- | --- | ------------------- | --- |
In this setting, we obtain 1000 sets of data, which contain 20195 triangles, corresponding
to 1000 materials. These grouped data are used to calculate matrix-level badness, thereby
studying the properties of triangles for different crystal structures. Since the amount of data in
each data group is different, we use a normalized version of matrix-level badness.
∑
1
|     |     |     | B′  |        |     |        | {B )}1000. |
| --- | --- | --- | --- | ------ | --- | ------ | ---------- |
|     |     |     | (D) | =      |     | B (T), | (D         |
|     |     |     | F   | |T(D)| |     | F      | F i i=1    |
T∈T(D)
We continue to use these 20195 triangles at the triangle level. Triangle-level computational
experimentscanrevealthecorrelationbetweenbadnessfunctionsanddatafordifferentchemical
bonds.
|     |     |     |     |     | {B  | (T )}20195. |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- |
F i i=1
| 5 Correlation |     |     | Results |     |     |     |     |
| ------------- | --- | --- | ------- | --- | --- | --- | --- |
ThissectionreportsthecorrelationresultsforthefourdatasetsdescribedinSubsection4.1.
The common correlation methodology is described in Section 3; here we focus on the data
| alignment, | numerical | results, |     | and their | geometric | interpretation. |     |
| ---------- | --------- | -------- | --- | --------- | --------- | --------------- | --- |
10

5.1 Needleman–Wunsch-Like Distance Matrices
This experiment corresponds to the Needleman–Wunsch-like distance-matrix dataset de-
scribed in Subsection 4.1.1. We compared three matrix-level total badness sequences obtained
from 100 independently generated distance matrices:
{B (D )}100, {B (D )}100, {B (D )}100.
BM i i=1 IA i i=1 δ i i=1
Pairwise correlations were computed for
B –B , B –B , B –B ,
BM IA BM δ IA δ
as reported in Table 1.
Table 1: Pairwise correlations among total badness sequences for 100 Needleman–Wunsch-like
distance matrices.
Pair Pearson Spearman Kendall Biweight
B –B 0.9979 0.9990 0.9822 0.9975
BM IA
B –B 0.9987 0.9993 0.9851 0.9988
BM δ
B –B 0.9992 0.9986 0.9770 0.9991
IA δ
All four correlation coeﬀicients show very strong agreement among the three matrix-level
total badness sequences. In particular, all Pearson and biweight correlations are above 0.997,
and all rank-based correlations are also close to one. This indicates that, for this family of
Needleman–Wunsch-like distance matrices, the three total badness functions induce almost
identical orderings of the 100 matrices.
ThestrongestagreementisobservedbetweenB andB , withPearsoncorrelation0.9987,
BM δ
Spearmancorrelation0.9993,Kendallcorrelation0.9851,andbiweightcorrelation0.9988. Over-
all, the results provide strong evidence that the three total badness functions preserve the same
matrix-level structural information in the Needleman–Wunsch-like setting.
5.2 Fixed Biological Distance Matrices
This experiment corresponds to the fixed biological distance matrices described in Sub-
section 4.1.2. We compared the triangle-level badness values induced by two distance defi-
nitions: the Jaro–Winkler distance matrix, denoted by JA, and the Needleman–Wunsch-like
cost-minimization distance matrix, denoted by NW. For each distance matrix, every unordered
triple of indices (i,j,k) forms a triangle T. For each triangle, we considered
B (T), B (T), B (T),
BM IA δ
with the triangle indices used to align the JA and NW sequences. The badness values for all
( )
32
= 4960
3
triangles were used in each fixed matrix.
Since the main purpose of this experiment is to compare the local triangle structures
inducedbythetwodistancedefinitions,thecross-distancecorrelationsinTable4aretheprimary
quantitiesofinterest. Thewithin-matrixcorrelationsinTables2and3arereportedasauxiliary
diagnostics.
Thewithin-matrixcorrelationsshowthatB isstronglyandpositivelycorrelatedwithB
δ BM
for both fixed distance matrices. For the JA matrix, the Pearson and biweight correlations for
this pair are 0.9564 and 0.9599, respectively, with Spearman correlation 0.8747. For the NW
11

Table 2: Pairwise correlations among badness functions for the Jaro–Winkler distance matrix
(JA).
Pair Pearson Spearman Kendall Biweight
B –B 0.6440 0.5205 0.4637 0.6374
BM IA
B –B 0.9564 0.8747 0.7098 0.9599
BM δ
B –B 0.7131 0.7043 0.5761 0.7057
IA δ
Table3: PairwisecorrelationsamongbadnessfunctionsfortheNeedleman–Wunsch-likedistance
matrix (NW).
Pair Pearson Spearman Kendall Biweight
B –B 0.5854 0.3802 0.3724 0.5612
BM IA
B –B 0.9756 0.8801 0.7265 0.9773
BM δ
B –B 0.6455 0.6368 0.5344 0.6167
IA δ
Table 4: Cross-distance correlations between Jaro–Winkler and Needleman–Wunsch-like trian-
gle badness sequences.
Pair Pearson Spearman Kendall Biweight
BJA vs BNW 0.4368 0.4234 0.2916 0.4946
BM BM
BJA vs BNW 0.2716 0.2346 0.1580 0.2722
IA IA
BJA vs BNW 0.4353 0.3832 0.2637 0.4886
δ δ
matrix, the corresponding values are 0.9756, 0.9773, and 0.8801. This indicates that the δ-
regularized edge-based badness and the bisector–median angular badness induce highly similar
triangle orderings within each fixed matrix.
The correlations involving B are also positive, but generally weaker than the B –B
IA BM δ
correlations. Thus, B is structurally related to the other two badness measures, although it
IA
does not induce exactly the same ordering of triangles.
Forthecross-distancecomparison,theagreementbetweenJAandNWismoderateforB
BM
andB , andweakerforB . Amongthethreebadnessfunctions, B givesthestrongestcross-
δ IA BM
distance agreement, with Pearson correlation 0.4368, Spearman correlation 0.4234, Kendall
correlation 0.2916, and biweight correlation 0.4946. The corresponding values for B are very
δ
similar in Pearson and biweight correlation, but lower in the rank-based measures. Therefore,
the δ-regularized edge-based badness remains highly consistent with B within each fixed ma-
BM
trix, whilethecross-distancecomparisonindicatesthattheJAandNWlocaltrianglestructures
are only moderately aligned.
5.3 Randomly Generated Triangles
Thisexperimentcorrespondstotherandom-triangledatasetsdescribedinSubsection4.1.3.
We analyzed pairwise correlations among the three triangle-level badness sequences
{B (T )}N , {B (T )}N , {B (T )}N ,
BM i i=1 IA i i=1 δ i i=1
fortwosyntheticdatasets: trianglesgeneratedfromrandomanglesandtrianglesgeneratedfrom
random side lengths. Each dataset contains N = 10000 generated triangles.
For each dataset, correlations were computed for
B –B , B –B , B –B ,
BM IA BM δ IA δ
as reported in Tables 5 and 6.
The purpose of this experiment is to determine whether the three badness functions induce
similar triangle orderings under two random generation models. The results show that all
12

Table 5: Pairwise correlations among badness functions for randomly generated triangles by
angles.
|     |     | Pair |      | Pearson |     | Spearman | Kendall | Biweight |
| --- | --- | ---- | ---- | ------- | --- | -------- | ------- | -------- |
|     |     | B    | –B   | 0.4207  |     | 0.2145   | 0.1815  | 0.1674   |
|     |     | BM   | IA   |         |     |          |         |          |
|     |     | B    | –B   | 0.8383  |     | 0.9103   | 0.7441  | 0.8268   |
|     |     | BM   | δ    |         |     |          |         |          |
|     |     | B IA | –B δ | 0.4932  |     | 0.4139   | 0.3332  | 0.4676   |
Table 6: Pairwise correlations among badness functions for randomly generated triangles by
sides.
|     |     | Pair |       | Pearson |     | Spearman | Kendall | Biweight |
| --- | --- | ---- | ----- | ------- | --- | -------- | ------- | -------- |
|     |     | B BM | –B IA | 0.4540  |     | 0.3045   | 0.2522  | 0.2165   |
|     |     | B    | –B    | 0.8621  |     | 0.8670   | 0.6949  | 0.7861   |
|     |     | BM   | δ     |         |     |          |         |          |
|     |     | B    | –B    | 0.5626  |     | 0.5306   | 0.4134  | 0.5438   |
IA δ
pairwise correlations are nonnegative in both datasets. In particular, B and B exhibit the
BM δ
| strongest | agreement | in both | generation |     | schemes. |     |     |     |
| --------- | --------- | ------- | ---------- | --- | -------- | --- | --- | --- |
For the angle-based random triangles, the agreement between B BM and B δ is strong across
all four measures, with Pearson correlation 0.8383, Spearman correlation 0.9103, Kendall cor-
relation 0.7441, and biweight correlation 0.8268. Thus, in the angle-based model, B gives a
δ
triangle ranking that is highly compatible with the bisector–median criterion.
For the side-based random triangles, the agreement between B and B is also strong
BM δ
across all four correlation measures. The Pearson correlation is 0.8621, while the Spearman and
Kendall correlations are 0.8670 and 0.6949, respectively. This suggests that, when triangles are
generated from random side lengths, the edge-based regularized badness B δ and the bisector–
median badness B provide closely related evaluations of triangle deviation.
BM
The correlations involving B are positive but generally weaker. Therefore, B is struc-
IA IA
turally related to the other two badness functions, but it induces a less similar ordering of
random triangles. Overall, these results show that B is highly consistent with B in both
δ BM
random generation models, while B provides a related but less tightly aligned assessment.
IA
| 5.4 Euclidean |     | Distance |     | Matrices |     | from Random |     | Planar Points |
| ------------- | --- | -------- | --- | -------- | --- | ----------- | --- | ------------- |
This experiment corresponds to the Euclidean random point matrix dataset described in
Subsection 4.1.4. We analyzed three matrix-level total badness sequences,
|     |     | {B  |       | )}100, | {B  | )}100, |     | {B )}100, |
| --- | --- | --- | ----- | ------ | --- | ------ | --- | --------- |
|     |     |     | BM (D | i      |     | (D i   |     | (D i      |
|     |     |     |       | i=1    |     | IA     | i=1 | δ i=1     |
where each sequence contains one total badness value for each independently generated Eu-
clidean distance matrix D . The matrix indices were aligned before computing the correlations,
i
| and all total | badness | values | were | finite. |     |     |     |     |
| ------------- | ------- | ------ | ---- | ------- | --- | --- | --- | --- |
Pairwise correlations between the three total badness sequences are shown in Table 7.
Table 7: Pairwise correlations among total badness sequences for Euclidean distance matrices
| generated | from | random planar |     | points. |     |          |         |          |
| --------- | ---- | ------------- | --- | ------- | --- | -------- | ------- | -------- |
|           |      | Pair          |     | Pearson |     | Spearman | Kendall | Biweight |
B –B
|     |     |     |     | 0.2584 |     | 0.1981 | 0.1358 | 0.2151 |
| --- | --- | --- | --- | ------ | --- | ------ | ------ | ------ |
|     |     | BM  | IA  |        |     |        |        |        |
|     |     | B   | –B  | 0.9685 |     | 0.9665 | 0.8491 | 0.9664 |
|     |     | BM  | δ   |        |     |        |        |        |
B –B
|     |     | IA  | δ   | 0.2546 |     | 0.2043 | 0.1471 | 0.2216 |
| --- | --- | --- | --- | ------ | --- | ------ | ------ | ------ |
All correlations are positive in this Euclidean setting. The strongest agreement is observed
B B
between BM and δ , with Pearson correlation 0.9685, Spearman correlation 0.9665, Kendall
13

correlation 0.8491, and biweight correlation 0.9664. Thus, the δ-regularized edge-based to-
tal badness and the bisector–median total badness induce highly similar orderings of the 100
| Euclidean | distance | matrices. |     |     |     |     |     |     |     |
| --------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
This strong agreement indicates that, even after aggregating all triangle-level contributions
B
into a single value F (D), the edge-based regularized badness retains essentially the same
| matrix-level | ordering |     | information | as  | the bisector–median |     | badness. |     |     |
| ------------ | -------- | --- | ----------- | --- | ------------------- | --- | -------- | --- | --- |
The correlations involving B are positive but much weaker. Therefore, in ordinary Eu-
IA
|     |     |     | B   |     |     | B   |     |     | B   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
clidean random geometry, is closely aligned with , whereas captures a related but
|               |         |        | δ        |                |          |            | BM   |      | IA  |
| ------------- | ------- | ------ | -------- | -------------- | -------- | ---------- | ---- | ---- | --- |
| less tightly  | coupled | aspect | of       | the aggregated | triangle | structure. |      |      |     |
| 5.5 Triangles |         | for    | parallax | method         | based    | on         | Gaia | data |     |
This experiment corresponds to the triangles for parallax method based on Gaia data
described in Subsection 4.1.5. We analyzed three matrix-level total badness sequences,
|           |                |     | {B (D    | )}100,     | {B (D | )}100,   |     | {B (D | )}100,   |
| --------- | -------------- | --- | -------- | ---------- | ----- | -------- | --- | ----- | -------- |
|           |                |     | BM       | i i=1      | IA    | i i=1    |     | δ     | i i=1    |
| and three | triangle-level |     | badness  | sequences, |       |          |     |       |          |
|           |                | {B  | )}69806, |            | {B    | )}69806, |     | {B    | )}69806. |
|           |                |     | (T       |            | (T    |          |     | (T    |          |
|           |                |     | BM i     | i=1        | IA    | i i=1    |     | δ     | i i=1    |
Pairwise correlations between the three total badness sequences are shown in Table 8.
Table 8: Pairwise correlations among total badness sequences for triangles for parallax method
| based on | Gaia | data. |       |         |          |     |         |          |        |
| -------- | ---- | ----- | ----- | ------- | -------- | --- | ------- | -------- | ------ |
|          |      |       | Pair  | Pearson | Spearman |     | Kendall | Biweight |        |
|          |      |       | B –B  | -0.7073 | -0.5333  |     | -0.4375 |          | 0.7687 |
|          |      |       | BM IA |         |          |     |         |          |        |
B –B
|     |     |     |      | -0.6862 | -0.5243 |     | -0.4383 |     | 0.7684 |
| --- | --- | --- | ---- | ------- | ------- | --- | ------- | --- | ------ |
|     |     |     | BM δ |         |         |     |         |     |        |
|     |     |     | B –B | 0.9969  | 0.9936  |     | 0.9466  |     | 0.9999 |
|     |     |     | IA δ |         |         |     |         |     |        |
|     |     |     |      |         |         |     |         |     | B B    |
The correlation coeﬀicients show a strong correlation between IA and δ , with all coef-
ficients above 0.94. However, B and B , or B and B , exhibit an anomalous negative
|     |     |     |     | BM  | IA  | BM  |     | δ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
correlation in the Pearson, Spreaman, and Kendall coeﬀicients. Combining this with the distri-
bution of badness data, we conclude that this negative correlation is spurious, influenced by the
unique distribution of the astronomical measurement triangle. The badness values B , B ,
IA IA
and B are concentrated at a high level, but B has a heavier tail to the right of its peak,
| δ   |     |     |     |     |     | BM  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B   |     | B   |     |     |     |     |     |     |     |
while and have longer, heavier tails to the left of their peaks. Therefore, Tukey biweight
| IA  |     | δ   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
coeﬀicient shows the correct property; other correlation coeﬀicients are affected by the data
distribution.
Pairwise correlations between the three triangle-level badness sequences are shown in Ta-
ble 9.
Table 9: Pairwise correlations among triangle-level badness sequences for triangles for parallax
| method | based | on Gaia | data. |         |          |     |         |     |          |
| ------ | ----- | ------- | ----- | ------- | -------- | --- | ------- | --- | -------- |
|        |       |         | Pair  | Pearson | Spearman |     | Kendall |     | Biweight |
|        |       |         | B –B  | -0.0011 | -0.0079  |     | -0.0004 |     | 0.5961   |
|        |       |         | BM IA |         |          |     |         |     |          |
|        |       |         | B –B  | 0.1547  | 0.1669   |     | 0.1255  |     | 0.6442   |
|        |       |         | BM δ  |         |          |     |         |     |          |
|        |       |         | B –B  | 0.8700  | 0.8934   |     | 0.7583  |     | 0.9822   |
|        |       |         | IA δ  |         |          |     |         |     |          |
The situation regarding badness values at the triangular level is similar to that at the
matrix level. The Pearson, Speaman, and Kendall correlation coeﬀicients for B and B , or
BM IA
B and B , show spurious “independence”, while the Tukey biweight coeﬀicient captures the
| BM  | δ   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
correct trend. At the triangular level, all correlation coeﬀicients are affected due to the steeper
14

−6,
peak of the distribution. For example, for data with a parallax angle on the order of 10 if the
measurement experiences a jitter of 0.01%, the change level of BM is approximately 10 times
that of IA.
Comparing the matrix and triangular levels, we can see that stratifying by parallax angle
is useful. The measurement accuracy will vary systematically due to the influence of parallax
levels. Within each level, the correlation of badness is suﬀiciently significant.
5.6 Triangles in crystal structures based on Materials Project data
This experiment corresponds to the triangles in crystal structures based on Materials
Project data described in Subsection 4.1.6. We analyzed three matrix-level total badness se-
quences,
|           |                | {B      | (D )}1000, | {B (D )}1000,  | {B (D )}1000,  |
| --------- | -------------- | ------- | ---------- | -------------- | -------------- |
|           |                | BM      | i i=1      | IA i           | i=1 δ i i=1    |
| and three | triangle-level | badness | sequences, |                |                |
|           |                | {B (T   | )}20195,   | {B (T )}20195, | {B (T )}20195. |
|           |                | BM      | i i=1      | IA i i=1       | δ i i=1        |
Pairwise correlations between the three total badness sequences are shown in Table 10.
Table10: Pairwisecorrelationsamongtotalbadnesssequencesfortrianglesincrystalstructures
| based on | Materials | Project | data.   |          |                  |
| -------- | --------- | ------- | ------- | -------- | ---------------- |
|          |           | Pair    | Pearson | Spearman | Kendall Biweight |
B –B
|     |     |     | 0.9660 | 0.9300 | 0.8197 0.9592 |
| --- | --- | --- | ------ | ------ | ------------- |
BM IA
|     |     | B –B | 0.9776 | 0.9604 | 0.8575 0.7405 |
| --- | --- | ---- | ------ | ------ | ------------- |
BM δ
B –B
|     |     | IA  | δ 0.9962 | 0.9848 | 0.9349 0.8546 |
| --- | --- | --- | -------- | ------ | ------------- |
Pairwise correlations between the three triangle-level badness sequences are shown in Ta-
ble 11.
Table 11: Pairwise correlations among triangle-level badness sequences for triangles in crystal
| structures | based | on Materials | Project | data.    |                  |
| ---------- | ----- | ------------ | ------- | -------- | ---------------- |
|            |       | Pair         | Pearson | Spearman | Kendall Biweight |
|            |       | B –B         | 0.9463  | 0.8926   | 0.7822 0.8820    |
BM IA
|     |     | B BM –B | δ 0.9719 | 0.9498 | 0.8375 0.3352 |
| --- | --- | ------- | -------- | ------ | ------------- |
|     |     | B –B    | 0.9895   | 0.9835 | 0.9192 0.6214 |
IA δ
Unlike astronomical measurement data, the badness of triangles in the crystal structures
are less affected by the noise. The overall trends at the matrix and triangle levels are not
significantlydifferent; themaindistributionpatternsofallbadnessvaluesarelargelyconsistent,
and all correlation coeﬀicients accurately capture the relationships between the badness values.
Itisnoteworthythatalthoughallthreebadnessfunctionsexhibitacertaindegreeofbimodality,
badness IA and δ strongly amplify the slight overall stretching of triangle symmetry, while BM
is insensitive to this. For example, in numerical qualitative analysis, for an isosceles triangle
with a base 10% longer than its legs, IA changes by approximately 7%, while BM remains
unchanged. This is particularly pronounced at the triangle level, which can be explained by
the fact that, within the same material, the slight stretching of symmetry also exhibits overall
symmetry, thus the badness has a partially offsetting effect in various locations.
6 Conclusion
Inthisstudy, weinvestigatedthestructuralconsistencyoftriangle-basedbadnessfunctions
across different distance metrics and geometric configurations. By systematically computing
15

badness sequences and evaluating their pairwise similarities using four distinct correlation coef-
ficients,wewereabletoquantifyhowconsistentlydifferentbadnessfunctionscapturedeviations
| from ideal | geometric | structures. |     |     |     |     |     |     |
| ---------- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
Our results, based on these example scenarios, demonstrate that while all considered bad-
ness functions reflect aspects of triangle imbalance and angular deviation, the degree of agree-
mentvariesdependingonthefunctiontypeandtheunderlyingdistancemetric. Somefunctions
exhibit high correlation, indicating that they are robust proxies for the same geometric char-
acteristics, whereas others emphasize complementary features, highlighting different aspects
of local inconsistency. These observations underscore the importance of selecting appropriate
badnessmeasureswhenanalyzinggeometricordistance-baseddatasets, particularlyincontexts
| where structural |     | fidelity | is critical. |     |     |     |     |     |
| ---------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- |
Furthermore, the proposed evaluation framework provides a flexible methodology for com-
paring alternative definitions of triangle-based measures. By leveraging multiple correlation
coeﬀicients, it offers a nuanced assessment that captures both linear and rank-based relation-
ships among badness sequences. This approach can be readily extended to other geometric or
combinatorial measures beyond triangles, facilitating systematic studies of structural consis-
| tency in | broader | contexts. |     |     |     |     |     |     |
| -------- | ------- | --------- | --- | --- | --- | --- | --- | --- |
Overall, our findings help inform informed choices of distance and badness measures, sup-
porting more reliable analyses in geometric reconstruction, triangulation, and the study of
| pairwise | distance | data. |     |     |     |     |     |     |
| -------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
Acknowledgments
The authors would like to thank Professor Boris Melnikov for his valuable guidance and
| insightful | discussions |     | throughout | this | work. |     |     |     |
| ---------- | ----------- | --- | ---------- | ---- | ----- | --- | --- | --- |
This work has made use of data from the European Space Agency (ESA) mission Gaia
(https://www.cosmos.esa.int/gaia), processed by the Gaia Data Processing and Analysis
Consortium (DPAC, https://www.cosmos.esa.int/web/gaia/dpac/consortium). Funding
for the DPAC has been provided by national institutions, in particular the institutions partici-
| pating in | the Gaia | Multilateral |     | Agreement. |     |     |     |     |
| --------- | -------- | ------------ | --- | ---------- | --- | --- | --- | --- |
The authors gratefully acknowledge the Materials Project for providing the open-access
crystal structure database utilized in this work and the developers of the pymatgen and scipy
| libraries | for making | their | computational |     | tools | publicly | available. |     |
| --------- | ---------- | ----- | ------------- | --- | ----- | -------- | ---------- | --- |
References
[1] Abramyan,M.E.,Krainiukov,N.I.,Melnikov,B.F.(2024)Onthe“OnionHusk”algorithm
forapproximatesolutionofthetravelingsalesmanproblem.JournalofAppliedMathematics
| and | Physics, | 12(4), | 1557–1570. | DOI: | 10.4236/jamp.2024.124095. |     |     |     |
| --- | -------- | ------ | ---------- | ---- | ------------------------- | --- | --- | --- |
[2] de Berg, M., et al. (2000) Delaunay triangulations. In: Computational Geometry: Algo-
| rithms | and | Applications, |     | 2nd ed., | Chapter | 9, pp. | 183–210. | Springer. |
| ------ | --- | ------------- | --- | -------- | ------- | ------ | -------- | --------- |
[3] Ding, Y., Shen, D., Pham, K., Chen, G. (2025) Optimal placements for minimum GDOP
withconsiderationontheelevationsofaccessnodes.IEEETransactionsonInstrumentation
and Measurement, 74, Article 9501210. DOI: 10.1109/TIM.2024.3497055.
[4] Dorsch, R. G., Häusler, G., Herrmann, J. M. (1994) Laser triangulation: funda-
mental uncertainty in distance measurement. Applied Optics, 33(7), 1306–1314. DOI:
10.1364/AO.33.001306.
16

[5] Jain, A., et al. (2013) Commentary: The Materials Project: A materials genome ap-
proach to accelerating materials innovation. APL Materials, 1(1), Article 011002. DOI:
10.1063/1.4812323.
[6] Bailer-Jones, C. A. L., et al. (2018) Estimating distance from parallaxes. IV. Distances to
1.33 billion stars in Gaia Data Release 2. The Astronomical Journal, 156(2), Article 58.
DOI: 10.3847/1538-3881/aacb21.
[7] GaiaCollaboration,etal.(2016)TheGaiamission.Astronomy&Astrophysics,595,Article
A1. DOI: 10.1051/0004-6361/201629272.
[8] Gaia Collaboration, et al. (2023) Gaia Data Release 3: Summary of the content and
survey properties. Astronomy & Astrophysics, 674, Article A1. DOI: 10.1051/0004-
6361/202243940.
[9] Pan, H., et al. (2021) Benchmarking coordination number prediction algorithms
on inorganic crystal structures. Inorganic Chemistry, 60(3), 1590–1603. DOI:
10.1021/acs.inorgchem.0c02996.
[10] Horton, M. K., et al. (2025) Accelerated data-driven materials science with the Materials
Project. Nature Materials, 24(10), 1522–1532. DOI: 10.1038/s41563-025-02272-0.
[11] Virtanen, P., et al. (2020) SciPy 1.0: fundamental algorithms for scientific computing in
Python. Nature Methods, 17, 261–272. DOI: 10.1038/s41592-019-0686-2.
[12] Ong, S. P., et al. (2013) Python Materials Genomics (pymatgen): A robust, open-source
Python library for materials analysis. Computational Materials Science, 68, 314–319. DOI:
10.1016/j.commatsci.2012.10.028.
[13] Willems, T. F., et al. (2012) Algorithms and tools for high-throughput geometry-based
analysis of crystalline porous materials. Microporous and Mesoporous Materials, 149(1),
134–141. DOI: 10.1016/j.micromeso.2011.08.020.
[14] Gao,Z.,Yu,Z.,Holst,M.(2013)Feature-preservingsurfacemeshsmoothingviasuboptimal
Delaunaytriangulation.Graphical Models, 75(1), 23–38.DOI:10.1016/j.gmod.2012.10.007.
[15] Gavryushkin, A., Drummond, A. J. (2016) The space of ultrametric phylogenetic trees.
Journal of Theoretical Biology, 403, 197–208. DOI: 10.1016/j.jtbi.2016.05.001.
[16] Gillespie, J. H. (1991) The Causes of Molecular Evolution. Vol. 2. Oxford University Press.
[17] Graur, D. (2000) Fundamentals of Molecular Evolution.
[18] Guo, Z., Li, B., Wu, Y. (2025) Layout optimization of hybrid pseudolite sys-
tems based on an incremental GDOP model. Aerospace, 12(10), Article 889. DOI:
10.3390/aerospace12100889.
[19] Kimura, M. (1969) The rate of molecular evolution considered from the standpoint of
population genetics. Proceedings of the National Academy of Sciences, 63(4), 1181–1188.
[20] Kimura, M.(1980)Asimplemethodforestimatingevolutionaryratesofbasesubstitutions
throughcomparativestudiesofnucleotidesequences.JournalofMolecularEvolution,16(2),
111–120.
[21] Kimura, M. (1985) The Neutral Theory of Molecular Evolution. Cambridge University
Press.
17

[22] Kimura, M., et al. (1968) Evolutionary rate at the molecular level. Nature, 217(5129),
624–626.
[23] Kimura, M., Ohta, T. (1971) Protein polymorphism as a phase of molecular evolution.
Nature, 229(5285), 467–469. DOI: 10.1038/229467a0.
[24] Kimura, M., Ohta, T.(1972)Onthestochasticmodelforestimationofmutationaldistance
between homologous proteins. Journal of Molecular Evolution, 2(1), 87–90.
[25] Ko, K., Kabir, M. H., Kim, J., Shin, W. (2024) GDOP-based low-complexity LEO
satellite subset selection for positioning. IEEE Systems Journal, 18(2), 989–996. DOI:
10.1109/JSYST.2024.3383092.
[26] Margoliash, E. (1963) Primary structure and evolution of cytochrome c. Proceedings of the
National Academy of Sciences, 50(4), 672–679.
[27] Melnikov, B. (2024) On an approach to the study of distances between DNA sequences.
In: 2024 12th International Conference on Bioinformatics and Computational Biology
(ICBCB), pp. 27–34. DOI: 10.1109/ICBCB61507.2024.11012008.
[28] Melnikov, B., Liu, B. (2025) A parallelizable heuristic algorithm for planar triangulation
with noisy data. Cybernetics and Physics, 14(3), 267–274. DOI: 10.35470/2226-4116-2025-
14-3-267-274.
[29] Melnikov, B., Liu, B., Vinh, D. V. (2025) The planar triangulation with noisy data: the
dynamic changing the order of points. Cybernetics and Physics, 14(4), 356–362. DOI:
10.35470/2226-4116-2025-14-4-356-362.
[30] Melnikov, B., Radionov, A., Gumayunov, V. (2006) Some special heuristics for discrete
optimization problems. In: Proceedings of the 8th International Conference on Enterprise
Information Systems (ICEIS 2006), pp. 360–364.
[31] Rebay, S. (1993) Eﬀicient unstructured mesh generation by means of Delaunay triangula-
tion and Bowyer–Watson algorithm. Journal of Computational Physics, 106(1), 125–138.
[32] Wang, D., Qin, H., Zhang, Y., Yang, Y., Lv, H. (2024) Fast clustering satel-
lite selection based on Doppler positioning GDOP lower bound for LEO constella-
tion. IEEE Transactions on Aerospace and Electronic Systems, 60(6), 9401–9410. DOI:
10.1109/TAES.2024.3443021.
[33] Waterman, M. S., Smith, T. F., Beyer, W. A. (1976) Some biological sequence metrics.
Advances in Mathematics, 20(3), 367–387. DOI: 10.1016/0001-8708(76)90202-4.
[34] Zuckerkandl, E., Pauling, L. (1965) In: Bryson, V., Vogel, H. J. (eds.), Evolving Genes and
Proteins. Academic Press, New York.
[35] Zuckerkandl, E., Pauling, L., Kasha, M., Pullman, B. (1962) Horizons in biochemistry.
Horizons in Biochemistry, pp. 97–166.
18
---- END DOCUMENT ----
