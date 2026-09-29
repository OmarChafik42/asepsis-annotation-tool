Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
A ProbLog program to infer individual genotypes from
familial phenotypes in autosomal, X-linked, and Y-linked
Mendelian disorders
MaximeMahout
The automated reconstructionof patient family history is a common challenge in genetic counsel-
ing for disease prevention. Such a family history is usually determined for a particular subset of
diseases that are Mendelian, i.e. monogenic, and classified into three categoriesdependingon the
chromosome the gene is located: autosomal, X-linked or Y-linked. Mendel’s inheritance laws al-
lowforsimpleprobabilisticmodelingofthegenetictransmissionofmonogenicdisorders. Genetic
counsellorsuseknowledgeaboutthepatient’sfamilyhistoryandMendelianlawsforassessingrisks
oftransmittingorinheritingcongenitalconditions. We presentmendelprob.pl,aprobabilisticlogic
programmingalgorithminProbLogforderivingprobabilitiesofinheritanceofgenotypesandphe-
notypes for genes with two alleles through multiple generations. In particular, the user can input
genotypesandphenotypesforapatientanditsfamily,andautomaticallydeterminethemostprobable
geneticfamilyhistory. We illustratetheProbLogmodelonpracticalexamplesofpatientpedigrees
from the literature and from a genetic counseling handbook. We show that our method correctly
infers probability of individual genotypes from knowledge about familial genotypes, yielding the
sameresultsastoolpedprobr.However,unlikepedprobr,ourapproachcanexploitknowledgeabout
familialphenotypes. Itcanalsodirectlydistinguishbetweenautosomal,X-linked,andY-linkeddis-
orders,usingitsintuitivelogicalmodelling. WeprovideourProbLogtoolforfreeandopen-source
onGitHub,makingiteasilyavailableforgeneticcounsellors.Weconcludeontheimportanceofpro-
vidingexplainableformalmethodsforataskthatcliniciansmightwanttoperformusingproprietary
software.
Correspondence: maxime.mahout@inria.fr. OrcId: 0000-0002-2699-5582.
Affiliation: InriaSaclay,EPILifeware,91120, Palaiseau,France.
Keywords: Probabilistic logicprogramming, Classicalgenetics, Logicalinference.
Introduction
In1865, GregorMendel firstdescribed on species ofpeas the notion of dominant and recessive charac-
teristics, characteristics thatmightbeeither predominantly conserved, orpredominantly lostinahybrid
[Mendel(1865)]. With his work, Mendel described what would later become known as alleles, geno-
types and phenotypes. A genotype, the set of all alleles – versions of genes of an individual – is re-
sponsible for the phenotype – the set of all observable characteristics of the individual. The notions
of genotype and phenotype are meant to be observed together for two or more individuals of the same
species[Orgogozo etal.(2015)]. Mendel’slegacyisstillcarriedtodaythroughtheconceptofMendelian
diseases [BotsteinandRisch(2003)]. Modern genetics distinguish monogenic conditions, which obey
Mendel’s laws, and for which the responsible allele is confined to a single gene locus, from polygenic
conditions, in which a condition can be caused by the association of multiple alleles at different loci.
Forpolygenicconditions,theriseofgenome-wideassociationstudieshaspermittedsignificantadvances
in the medical treatment and diagnosis of illnesses [Visscheretal.(2012)]. Nevertheless, genome-wide
W.Faber,L.Giordano,R.Rocha,V.SantosCosta(Eds.):
42ndInternationalConferenceonLogicProgramming(ICLP2026)
EPTCS450,2026,pp.465–477,doi:10.4204/EPTCS.450.34

466 AProbLogprogramforMendelianinheritanceanalyses
association studies can sometimes overcomplicate analysis, and with their ease of availability in the
next-generation sequencing era, not enough emphasis has been put on monogenic or quasi-monogenic
diseases [Antonarakis andBeckmann(2006),Tametal.(2019)].
Genetic counseling for disease prevention typically involves screening patients’ family history for
monogenic diseases [Gordonetal.(2018), Bennett(2011)]. Mendelian disorders are reported in online
databases such as OMIM (Online Mendelian Inheritance in Man) and OrphaNet [Hamoshetal.(2005),
Pavanetal.(2017)]. Theyareclassifiedintofivediseasetypes,indicatingwhichchromosometherespon-
sible gene islocated on, between autosomes, XandY,andifthemutant allele isdominant orrecessive:
autosomal recessive, autosomal dominant, X-linked recessive, X-linked dominant, andY-linked. Genetic
family history is often looked at using proprietary software such as MeTree [Ginsburg etal.(2019)].
These softwares are typically closed-source and do not involve logical reasoning; they need to be pro-
videdwithpriorknowledge ofthepatient’scondition. Thereistherefore aninterest inproviding insuch
programs a way to directly infer genotypes and phenotypes, or to infer whether the phenotypes of the
familyindicate anX-linked,Y-linkedorautosomaldisorder.
In this study we present mendelprob.pl, a probabilistic program in ProbLog that is able to simulate
Mendelian inheritance for all five described allele transmission types. We show that we can logically
derive conclusions on the genotypes and phenotypes of a pedigree for any potentially unknown mono-
genic disease. Weillustrate thatourtoolcanhelpderivegenetic familyhistory forprobands, i.e. people
who seek genetic counseling. As well, we show that the tool’s predictive performance for analyzing
Mendelian inheritance of human disorders is on par with the pedigree genotyping method pedprobr
[Vigeland(2021)]. Our ProbLog tool’s major advantage over pedprobr is that – thanks to probabilistic
logic –itdoes notrequire tohaveprior knowledge about theexpected Mendelian disorder. Particularly,
it can infer a patient’s genotype from its phenotype, and it can determine what type of disorder is most
likelyassociated tothegeneticfamilyhistorybetweenX-linked, Y-linkedandautosomal.
Methods
Probabilistic programming is a well-established field of artificial intelligence, with many recent devel-
opments. Probabilistic logicprogrammingisasubsetofthisfieldthatproposestouseautomatedlogical
reasoning to derive probabilities for modeling uncertain events. Theprinciple is as follows: probabilis-
tic events are described with logic rules weighted by probabilities, and the solver’s role is to find an
assignment respecting truth values and the events’ probability distribution. A probabilistic logic pro-
gram is such a set of probabilistic logic rules and facts, which can be used to derive the probability
of natural language queries. Probabilistic logic programming problems can be solved using solvers
such as ProbLog [DeRaedtetal.(2007)]. The tool relies on knowledge compilation techniques such
as Binary Decision Diagrams [Bryant(1986)]: with the diagram’s edges being weighted by probabil-
ities, solutions are retrieved as tree traversals [DeRaedtetal.(2007)]. For our application study, we
are using the second version of ProbLog, which allows for setting evidence on atoms and multiple
querying [Driesetal.(2015), Fierensetal.(2015)]. Our tool, which we called mendelprob.pl, is com-
pared to the R tools pedsuite by Vigeland [Vigeland(2021)]. All analyses and code are available at
https://github.com/maxm4/mendelprob.pl.
Phenotype and genotype inference
A keycomponent of our mendelprob.pl tool isits ability to derive probable genotypes from phenotypes
and vice versa. Precisely, the tool applies to monogenic disorders that can be represented as bi-allelic,

MaximeMahout 467
that is, disorders that can be modeled as a single gene with two states: such as healthy/wild type and
ill/mutated. Let us call the wild type and mutant alleles respectively wt and m. From there, in classical
genetics, the notions of dominance and recessiveness come into play. As traditionally, we denote the
recessivealleleaandthedominantalleleA. Thesenotionsexplainwhetherthephenotypeisonlyvisible
in homozygotes, for recessive alleles (aa) or if it is also visible in heterozygotes, for dominant alleles
(Aa, AA). Prevalence is the occurrence of an allele, usually a disorder-causing mutation, in the general
population. Weprovideawaytomodulatetheprevalence pofa,andprevalence ofAisgivenby1−p.
A disorder caused by a mutation m can generally be either dominant or recessive. If it is recessive,
then m = a and wt = A, and the prevalence p is the prevalence of m. If it is dominant, then m = A
and wt =a, and 1−p is the prevalence of m. Therefore we can model genotypes and phenotypes of
individuals fordominantandrecessivemonogenicdisorders usingonlyallelesaandA.Inparticular, for
an autosomal disorder, the phenotypes are noted as a if the person’s genotype is aa, and A if person’s
genotype isAaorAA. Forsex-linked disorders, i.e. X-linkedandY-linked,fiveadditional genotypes are
possible: -,aorAforY-linked, anda-andA-formaleswithaX-linkeddisorder.
Inthelogicprogram code,genotypes arerepresented bycarrypredicates, andphenotypes byshow
predicates. Since genotype inheritance probabilities are different between males and females in sex-
linked disorders, the logic atoms are specified into f carry, m carry, f show, m show. The show
atomscanreceiveatherecessivephenotypeorAthedominantphenotype. Thecarryatomscanreceive
theeightaforementionedgenotypes. AsafeatureofProbLog,probabilitiesofgenotypesandphenotypes
arequeriedusingquerycommands. Priorknowledgecanalsobeintegratedtospecifytheseatomsusing
evidencecommands.
The phenotype is automatically derived from the genotype using logical relationships, always as-
sumingapenetrance (proportion ofindividuals withsaidgenotype presenting saidphenotype) of100%.
Nevertheless, we provide logic rules for co-dominance (phenotype is Aa) and incomplete penetrance
(them showandf showpredicates couldbeweighted byaprobability) ifnecessary. Wesummarize the
logicalrelationships betweenphenotypes andgenotypes, foreachdisorder type,inFigure1A.
Hardy-Weinberg equilibrium
Next, using prevalence pof disorder-causing alleles, weassume the well-known Hardy-Weinberg equi-
librium (HWE). This will allow us to derive probabilities that any individual taken at random in a pop-
ulation carries a certain genotype. Hardy-Weinberg equilibrium defines G the genotype of a random
I
individual by the following formulas, for diploid genotypes, using p the prevalence of allele a in the
population:
P(G =aa)= p2 (1)
I
P(G =Aa)=2p(1−p) (2)
I
P(G =AA)=(1−p)2 (3)
I
For haploid genotypes: single-allele genotypes, occurring in males in X-linked disorders and in Y-
linkeddisorders, theformulasaresimplifiedtohavingalleleawithaprevalence pornothavingallelea
withaprevalence 1−p.

| 468 |     |     |       |            |     | AProbLogprogramforMendelianinheritanceanalyses |     |     |
| --- | --- | --- | ----- | ---------- | --- | ---------------------------------------------- | --- | --- |
|     |     |     | P(G I | =a−|Dis=X, |     | Sex=M)=                                        | p   | (4) |
|     |     |     | P(G   | =A−|Dis=X, |     | Sex=M)=1−p                                     |     | (5) |
I
|     |     |     | P(G | =a |Dis=Y, |     | Sex=M)= | p   | (6) |
| --- | --- | --- | --- | ---------- | --- | ------- | --- | --- |
I
=A|Dis=Y,
|     |     |     | P(G | I         |     | Sex=M)=1−p |     | (7) |
| --- | --- | --- | --- | --------- | --- | ---------- | --- | --- |
|     |     |     | P(G | =−|Dis=Y, |     | Sex=F)=1   |     | (8) |
I
TheHardy-Weinberg lawstatesthattheseprobabilities arepreserved fromgeneration togeneration,
assumingthatindividualsinthepopulationarerandomlymating: asthenumberofgenerationsincreases
frequencies stay constant, an equilibrium is reached [Thomas(2004)]. In the case of our probabilistic
logicprogram,weshouldassumetheHardy-Weinbergequilibriumforeverygenerationindividualwhose
familyhistoryisunknown. Evenifthefullfamilyhistoryweretobeknown,theHardy-Weinberg lawis
quiteaconvenienttoolasitcouldallowustoabstractafamilyhistorythatistoocomplex. Asthenumber
of individuals and generations grow, the number of families whose genotypes should be determined
would grow exponentially, so for a first approach we chose to explore only a single direct ancestry for
probands, andassumeHardy-Weinberg equilibrium forthespousesandtheirfamilies–thosenotrelated
| tothemainfamily. |          | Werefertothisabstraction |                    |     | asadirectpedigree. |             |     |     |
| ---------------- | -------- | ------------------------ | ------------------ | --- | ------------------ | ----------- | --- | --- |
| Simulating       | disorder |                          | transmissionacross |     |                    | generations |     |     |
A probabilistic logic program composed of logic rules is used to simulate disorder transmission across
generations. Thisconstitutes thetoolmendelprob.pl, returning genotype andphenotype probabilities on
direct pedigrees, from agivenprevalence pandacross anumber ofgenerations g. Importantly, uniform
random variables arechosenformodeling choicepossibilities ofoursystem. Onemodelsdisordertype,
between {auto, X, Y}, and, for each generation, excluding the firstmost one, random variables model
the sex of the direct family descendants, between {M, F}. Thevery first generation, the first two known
ancestors oftheproband, inherit alleles according toHWE.Then, foreachfollowing generation, oneof
the individuals is a descendant of the previous generation, and the other individual is assumed distant
| fromthefamily,inheriting |     |     | allelesaccording |     | toHWE. |     |     |     |
| ------------------------ | --- | --- | ---------------- | --- | ------ | --- | --- | --- |
Thesexofthedirectfamilydescendant,whileunimportantinautosomaldisorders,radicallychanges
thetransmission probabilities inX-linked andY-linked disorders. Untilthisinformation isknown,male
and female genotype probabilities arethus half the probabilities ofinheriting from parents, and half the
probabilities from HWE.Similarly, until disorder type is known, allgenotype and phenotype probabili-
ties are 1⁄ autosomal, 1⁄ X-linked, 1⁄ Y-linked. These probabilities are calculated using the queries and
|     | 3   |     | 3   | 3   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
getreshapedbyevidencesgiventothelogicprogram. Forinstance,oneevidencecouldbethat: ”thethird
generationdescendantisawomanwithpathological phenotypea”. Suchapriorknowledgeexcludesthe
possibility ofaY-linkeddisorder, sinceinY-linkeddisorders phenotypes arenotobserved inwomen.
We present in Figure1B a pseudo-code algorithm corresponding to the logic program, completed
with queries and evidences. The logic rules for computing the inheritance of male and female alleles
across generations are associated togenerationpredicates and to positive integers, I > 0. The prob-
abilistic logic programming system works by defining the predicates with a rule, in the
generation
followingway,whereGinlastgen(G)isthenumberofgenerations minusone.
|     | generation(I) |     |     | :- lastgen(G), |     | between(0, | G, I), integer(I). |     |
| --- | ------------- | --- | --- | -------------- | --- | ---------- | ------------------ | --- |

MaximeMahout 469
Figure 1: Description of the mendelprob.pl functioning: A Internal logic representation of genotypes
and phenotypes, B: Simplified pseudo-code algorithm for genotype and phenotype probabilities trans-
mission. Allele probabilities of direct family are inherited (InheritGenotype) from probabilities of
parentgenotypesusingtheinternallogicrepresentation, genotypesofspousesandlastascendantsfollow
Hardy-Weinberg distribution, while disorder type and children gender – when they are not inferred
from genotypes –assumearandom uniform distribution (RandUniform). Finally, ComputePhenotype
| linksphenotypes | andgenotypes | usingtheinternal | logic. |     |
| --------------- | ------------ | ---------------- | ------ | --- |
Queries and evidences are the standard way to interact with probabilistic logic programs. They are
usedforgroundingtheprogram,i.e. assigningfinitevaluestofreefirst-orderlogicvariables. Thisallows
pruning ofBooleanclauses irrelevant toqueries andevidence outofthecomputation. Asaresult, given
evidences E, probabilities P(Q E =e) are calculated for each query Q [Fierensetal.(2015)]. In order
|
toinquirewhichgenotypesandphenotypesarerespectivelyshownbyindividualsofeachgeneration, we
askthelogicprogramthefollowingqueries:
query(disease( )).
|     | query(f        | carry(I,        | )) :- generation(I). |        |
| --- | -------------- | --------------- | -------------------- | ------ |
|     |                | query(f show(I, | )) :- generation(I). |        |
|     | query(m        | carry(I,        | )) :- generation(I). |        |
|     |                | query(m show(I, | )) :- generation(I). |        |
|     | query(m family | descendant(I))  | :- generation(I),    | I > 0. |
|     | query(f family | descendant(I))  | :- generation(I),    | I > 0. |
Respectively, therulesimplythefollowing: thefirstqueryaskstoestimatetheprobability ofdisease
between{auto,X,Y},thefourfollowingqueriesasktheprobability ofoccurrence ofthegenotypes and
phenotypes for the men and women at each generation i, the last two queries ask the probabilities that

| 470 |     |     |     | AProbLogprogramforMendelianinheritanceanalyses |     |     |
| --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
|     |     | 1   | 2   | 3                                              | 4   |     |
|     |     | ?/? | ?/? | ?/?                                            | ?/? |     |
|     |     |     | 5   | 6                                              |     |     |
|     |     |     | A/a | A/a                                            |     |     |
|     |     | 7   | 8   | 9                                              | 11  | 10  |
|     |     | ?/? | ?/? | ?/?                                            | ?/? | a/a |
    (cid:1)
proband
|     |     |     |     |     | 12  | 13  |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | ?/? | ?/? |
Figure 2: Pedigree of Rhonda, patient diagnosed with Cystic Fibrosis. Phenotypes marked as affected
(filledblack), unknownorunaffected (filledwhite). Pedigreeconstructed withpedtools frompedsuite.
thefamilydescendant isofagivengenderforeachgeneration i≥1. Lastly,thequeriesaregrounded by
the upper bound of I in generation(I),defined by the predicate lastgen(G).These are the queries
given to mendelprob.pl and the probabilistic logic solver for getting the probabilities shown in Results,
e.g. Table2.
Results
In order to illustrate the medical application of our tool, we looked at the prediction of genetic family
history, also sometimes known as pedigree analysis. The first example is taken from ”The practical
guide to the genetic family history” byRobin Bennett [Bennett(2011)], the second one is issued from a
realAmerican pedigree ofHuntington’s disease cases [Gusellaetal.(1983)]. Forcomparing predictions
pedsuite pedsuite
of our tool, we used the state-of-the-art in R [Vigeland(2021)]. The software suite
allows for the elaboration and representation of pedigrees, and in particular its tool pedprobr provides
| computation | ofprobabilities | forthegenotypes |     | ofeachfamilymember. |     |     |
| ----------- | --------------- | --------------- | --- | ------------------- | --- | --- |
CysticFibrosis
Rhondaisapatientwithasuspected chronicrespiratory diseasewhorecentlygotdiagnosed withCystic
Fibrosis (CF), despite seemingly having no history of the disorder in her family. We represent her
pedigree family tree in Figure2, as reported by Bennett [Bennett(2011)]. Rhonda got genotyped as
having two mutant alleles of the CTFR gene responsible for Cystic Fibrosis. Let us model the two
mutations by homozygous recessive alleles aa. Rhonda inquires for genetic counseling. What is the
probability ofRhondatransmitting theCysticFibrosisdiseasetoherchildren?

MaximeMahout 471
Since weknow Cystic Fibrosis’s transmission is autosomal recessive, wecan provide that evidence
tomendelprob.pl. Bysimplereasoning, wecanderivethatRhonda’s parents genotypes cannot beaa,or
else they would show the CF phenotype, and it cannot be AA either, or else they would not be able to
transmittheaalleletoRhonda. Letusprovidethefollowingstatements tomendelprob.pl:
prevalence("a", 1/1000). lastgen(3).
evidence(disease("auto")). % Cystic Fibrosis
evidence(f carry(1, "Aa")). % Mother of Rhonda
evidence(m carry(1, "Aa")). % Father of Rhonda
evidence(f family descendant(2)). % Rhonda
evidence(f show(2, "a")). % Rhonda
evidence(f carry(2, "aa")). % Rhonda
evidence(f family descendant(3)). % Daughter of Rhonda
Here, the same probabilities are returned by our tool mendelprob.pl and by pedprobr using its R
function oneMarkerDistribution. They are reported in Table1. We can see that the probability of
Rhonda’schildren(individuals12/F3and13/F3)inheritingtheautosomaldisease(homozygousgenotype
aa) from Rhonda (10/F2) and Ron (11/M2) is equal to 1/1000. This assumes that there are no cases of
CFinthe family of Ron, Rhonda’s husband, for whom thedefault genotype follows HWE.Wealso see
thetoolspredictpossibility forRonandRhonda’s grandparents toholdgenotype aa.
Table 1: Genotype probabilities obtained with pedprobr and mendelprob.pl for the Cystic Fibro-
sis case of Rhonda. For column labels: numbers correspond to individuals on the pedigree tree of
Figure 2, used as identifiers in pedprobr, while M and F correspond to identifiers of individuals in
i i
mendelprob.pl.
1/M0 2/F0 3/M0 4/F0 5/M1 6/F1 10/F2 11/M2 12/F3 13/F3
a/a 0.0005 0.0005 0.0005 0.0005 0 0 1 0.000001 0.001 0.001
A/a 0.5 0.5 0.5 0.5 1 1 0 0.001998 0.999 0.999
A/A 0.4995 0.4995 0.4995 0.4995 0 0 0 0.998001 0 0
Assuming Rhonda is a reliable narrator, she had never seen any other case of CF in her family.
The cause of death of her grandparents from both sides are reported and none of them are related to
respiratory symptoms. Aswell,itisfairtoassumeRhondawouldknowifRonwasalsoaffected byCF.
Usingourtool,wecanverifiablyexcludethecaseofthegenotypeaaforRonandforthegrandparents,by
specifying thattheirphenotype cannotbea. Thisreliesontwofeaturesthatpedprobr doesnotcurrently
have: expliciting phenotypes for individuals instead of genotypes, and making use of logical negation.
Withthesefeatures wecouldalsoavoid theprevious reasoning ontheparentsgenotypes andletthetool
workautomatically. Herearethenewevidences:
evidence(not m show(0, "a")). % Either Grandfather
evidence(not f show(0, "a")). % Either Grandmother
evidence(not m show(1, "a")). % Father of Rhonda
evidence(not f show(1, "a")). % Mother of Rhonda
evidence(not m show(2, "a")). % Ron, Rhonda’s husband

472 AProbLogprogramforMendelianinheritanceanalyses
Usingtheseevidences,genotypeprobabilitiesforthegrandparentsbecome0.4995:carry(0,"AA")
or0.5005:carry(0,"Aa").Also,forRhonda’schildren,sinceRoncannotcarryaaanymore,theprob-
abilitiesforthegenotypearenow0.999001:carry(3,"Aa")and0.000999:carry(3,"aa").These
examplesshowthatProbLogcaninferpossiblegenotypes fromknowledgeaboutphenotypes alone.
Note that while the grandparents 1, 2, 3, 4 in Figure2 are separate nodes for which we compute
probabilities in pedprobr, in mendelprob.pl since we are only working with a single direct pedigree,
weinstead modeluncertainty onwhichgrandparent thegenes comefrom, using theprobabilistic atoms
0.5:m family descendant(1) and 0.5:f family descendant(1). As well, the siblings 7, 8, 9,
whose genotypes are unknown and whose phenotypes bring no new information, do not belong to the
directancestryrequiredforamendelprob.plexecution. Asasupplementtothisarticle,we’veincludedan
examplefromBennett’sbookinanappendix,availableonGitHub,whichillustratesthetopicofX-linked
disorders, andourtool’sabilitytoautomatically detectthose.
Huntington’s disease
Toconclude, letustakearealexampleofanAmericanfamilythatwasusedtoidentifythegenecausing
Huntington’sdiseaseandsomeofitsallelesbackin1983[Gusellaetal.(1983)]. Sinceourtoolcanagain
onlyhandleadirectfamilyandnotthefullfamily,wedecidedtoanalyzetheleftmostbranchofthetree,
thebranchleadingtothesolememberofthe5thgenerationinthearticle’sFigure1[Gusellaetal.(1983)].
Itisrepresented inFigure3.
Huntington’s disease is a well-known monogenic dominant autosomal disorder. Its prevalence is
estimated at about 1/10000 according to OrphaNet [Pavanetal.(2017)]. Huntington’s disease homozy-
gotes (AA) are known to be hard to identify due to dominant allele transmission [Wexleretal.(1987)].
Wepresentthecommandsandevidencescorresponding tophenotypes ofFigure3below:
| prevalence("a", | 9999/10000).           | lastgen(4). |
| --------------- | ---------------------- | ----------- |
| evidence(f      | show(0,                | "A")).      |
| evidence(m      | show(0,                | "a")).      |
| evidence(f      | show(1,                | "A")).      |
| evidence(m      | show(1,                | "a")).      |
| evidence(f      | show(2,                | "A")).      |
| evidence(m      | show(2,                | "a")).      |
| evidence(f      | show(3,                | "a")).      |
| evidence(m      | show(3,                | "A")).      |
| evidence(m      | show(4,                | "A")).      |
| evidence(f      | family descendant(1)). |             |
| evidence(f      | family descendant(2)). |             |
| evidence(m      | family descendant(3)). |             |
| evidence(m      | family descendant(4)). |             |
Thisexampleisprettystraightforward. Fromthemendelprob.plprogram,weautomaticallyderiveall
ofthegenotypespresentedinFigure3withprobability1,andthatthisisanautosomaldisorder. Notethat
this last information was not given to ProbLog, it was inferred from impossibility of being X-linked or
Y-linked. Fromthesegenotypes, wecanfillintheoneMarkerDistributionfunction ofpedprobr and

| MaximeMahout |     |     |     |     |     |     | 473 |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
|              |     |     |     | 1   |     | 2   |     |
|              |     |     |     | a/a |     | ?/? |     |
|              |     |     | 4   |     | 3   |     |     |
|              |     |     | a/a |     | A/a |     |     |
|              |     | 6   |     | 5   |     |     |     |
|              |     | a/a |     | A/a |     |     |     |
|              |     |     | 7   |     | 8   |     |     |
|              |     |     | A/a |     | a/a |     |     |
(cid:1) proband
9
A/a
Figure 3: Pedigree of an American family with Huntington’s disease, patient from the 5th generation.
Phenotypesmarkedasaffected(filledblack),unknownorunaffected(filledwhite). Pedigreeconstructed
withpedtools.
check whether the probabilities found match with our tool. Only a single uncertain probability remain,
that of the woman at generation 0, or individual no. 2 on the pedigree. Both tools agree, its genotype
probabilities are0.9999:f carry(0,"Aa")and0.0001:f carry(0,"AA").
Table 2: Comparison of features of interest between mendelprob.pl and pedprobr, a part of
pedsuite.
| Tool | Full | Linkage | Multi- | Identify | Phenotype | Genotype | Logical |
| ---- | ---- | ------- | ------ | -------- | --------- | -------- | ------- |
pedigrees analysis allelicloci disorder inference inference reasoning
|               |     |     |     | type | from     | from      |     |
| ------------- | --- | --- | --- | ---- | -------- | --------- | --- |
|               |     |     |     |      | genotype | phenotype |     |
| mendelprob.pl | ✗   | ✗   | ✗   | ✓    | ✓        | ✓         | ✓   |
| pedprobr      | ✓   | ✓   | ✓   | ✗    | ✗        | ✗         | ✗   |
Inconclusion, ourprobabilisticlogicprogrammingtoolshowssubstantialpotentialforhelpingclini-
cianswithconstructing thegeneticfamilyhistoryofpatients. Itisabletoautomaticallyderivewhethera
disorderisautosomal,X-linked,orY-linked,itcanbeusedtomodelrecessiveanddominantalleles,and
itcandeterminegenotypesacrossseveralgenerationswithonlythephenotypesininput. Thedifferences
between the pedprobr R package and our probabilistic logic application mendelprob.pl are reported in
Table2.

474 AProbLogprogramforMendelianinheritanceanalyses
Discussion
The mendelprob.pl tool complements probabilistic logic descriptions of genetic problems by Blockeel
and colleagues, including comparative modeling of autosomal Mendelian inheritance [Blockeel(2004)]
andpredictionoftheinheritanceofmulti-allelicbloodtype[Meertetal.(2010)]. Toourknowledge,very
fewexhaustiveopen-sourcesoftwareforanalysisofthegeneticfamilyhistoryarefreelyavailableonline.
Ginsburg and collaborators listed no less than seventeen risk assessment software platforms for genetic
counseling clinicians, including eight affiliated with genetic testing companies: only four are available
to the public online without restrictions [Ginsburg etal.(2019)]. These are mostly commercial projects,
thataren’topen-source programs. Forpedigreeconstruction, itisnobetter,allthesolutionsproposedby
GordonandcollaboratorsandbyBennettareorwerecommercialandthroughaGraphicalUserInterface
[Gordonetal.(2018), Bennett(2011)]. In contrast, the drawing tool pedtools from pedsuite (the suite of
tools from which pedprobr is from) is open-source and in our opinion easy to use [Vigeland(2021)].
Vigeland, the author of pedsuite, also developed a Graphical User Interface for his R suite: QuickPed
[Vigeland(2022)]. Notably, pedsuite is compatible with Familias, another free software for probabi-
listic analyses of genetic family history, used especially in forensic sciences [Klingetal.(2014)]. Due
to its original probabilistic logic programming approach, webelieve our ProbLog tool mendelprob.pl is
complementary to the other tools. Therefore, we have open-sourced the tool and made it available on
GitHub.
Pedigree construction [Gordonetal.(2018)]should be an important part of any genetic counsellor’s
analyses. Clinicians recommend three-generation pedigrees, drawn for three generations, children,
parents,grandparents. Thisnumberappearsasaminimumnumberofgenerationstogetenoughevidence
from, and a fast enough procedure to be practical in medical context [WattendorfandHadley(2005)].
An important recent survey by Hussein et al. underlines that family history analysis, and especially
pedigree construction, are underperformed [Husseinetal.(2020)]. Among the main complaints about
pedigree construction isthat itis too time-consuming [Husseinetal.(2020),Ginsburg etal.(2019)]. For
instanceGinsburgetal. assessthatthemeancompletiontimeofpedigreeswiththeMeTreesoftwarewas
27 minutes [Ginsburg etal.(2019)]. In midst of these critics, we would like to report that our pedigree
drawing experience with pedtools from pedsuite [Vigeland(2021)] was fast. Additionally, our ProbLog
tool is efficient for direct pedigrees of the recommended three generations. The advantage of using
mendelprob.pl over pedprobr is that we can use prior knowledge about family history to infer disorder
type between X-linked, Y-linked and autosomal when it is unknown, and predict genotypes when only
phenotypes areknown. Weroughly estimate that ittook usabout 5-10 minutes tocreate apedigree and
rungenotype prediction usingpedtools andmendelprob.pl.
Gordon and colleagues hypothesized that technologies such as artificial intelligence have the
potential to automate routine actions in genetic counseling, and shifting some responsibilities to the
patient, including for the genetic family history [Gordonetal.(2018)]. Kearney and colleagues argued
that pedigree analysis and genetic risk assessments are some of the most important tasks to automate
with machine learning, but also some of the riskiest for the patient if the models were to be black-box
[Kearneyetal.(2020)]. Recently, a study of 95,166 patients involved in cancer risk assessment showed
that 61,070 agreed to engage with clinical chatbots, and the authors reported a mean duration of inter-
action of 15 minutes with the artificial intelligence [Nazarethetal.(2021)]. However, chatbots are risky
to involve in such a decisive medical task as they have the ability to hallucinate. Therefore, developing
formalmethodsinartificialintelligenceformedicineisimportant. Wehypothesizethatbuildinganatural
language interface for our ProbLog tool aswas envisioned for the pedtools suite [Vigeland(2022)], will
notonlyshortenpatientinteraction timewiththetool,butalsoprovideexactandexplainable diagnoses,

MaximeMahout 475
e.g. [Vidal(2025), Ariasetal.(2020)], for genetic counselors. Further developments of our tool can be
imaginedbeyondMendelian inheritance, byincluding forexamplemitochondrial inheritance.
Acknowledgments
Ithank Franc¸oisFagesand theLifewareteam forintroducing metoProlog. MaximeMahout reports fi-
nancialsupportandadministrativesupportwereprovidedbyInriaResearchCentreSaclayˆIle-de-France.
Maxime Mahout reports a relationship with Inria Research Centre Saclay ˆIle-de-France that includes:
employment.
References
[Mendel(1865)] GregorMendel.Versucheu¨berPlflanzenhybriden.Verhandlungendesnaturforschendenvereines
inbru¨nn,4:3–47,1865. doi:10.1007/978-3-663-19714-04
[Orgogozoetal.(2015)] VirginieOrgogozo,BaptisteMorizot,andArnaudMartin. Thedifferentialviewofgeno-
type–phenotyperelationships.FrontiersinGenetics,6,2015.ISSN1664-8021.doi:10.3389/fgene.2015.00179.
[BotsteinandRisch(2003)] DavidBotsteinandNeilRisch.Discoveringgenotypesunderlyinghumanphenotypes:
pastsuccessesformendeliandisease,futureapproachesforcomplexdisease. NatureGenetics,33(3):228–237,
March2003. ISSN1546-1718. doi:10.1038/ng1090. Number:3Publisher:NaturePublishingGroup.
[Visscheretal.(2012)] Peter M. Visscher, Matthew A. Brown, Mark I. McCarthy, and Jian Yang.
Five years of GWAS discovery. The American Journal of Human Genetics, 90(1):7–24, 2012.
doi:10.1016/j.ajhg.2011.11.029. Publisher:Elsevier.
[AntonarakisandBeckmann(2006)] Stylianos E. Antonarakis and Jacques S. Beckmann. Mendelian disorders
deserve more attention. Nature Reviews Genetics, 7(4):277–282,April 2006. ISSN 1471-0056, 1471-0064.
doi:10.1038/nrg1826.
[Tametal.(2019)] VivianTam,NikunjPatel,MichelleTurcotte,YohanBosse´,GuillaumePare´,andDavidMeyre.
Benefitsandlimitationsofgenome-wideassociationstudies. NatureReviewsGenetics,20(8):467–484,August
2019. ISSN1471-0064. doi:10.1038/s41576-019-0127-1. Number:8Publisher:NaturePublishingGroup.
[Gordonetal.(2018)] Erynn S. Gordon, Deepti Babu, and Dawn A. Laney. The future is now: Technology’s
impact on the practice of genetic counseling. American Journal of Medical Genetics Part C: Seminars in
MedicalGenetics,178(1):15–23,2018. ISSN1552-4876. doi:10.1002/ajmg.c.31599.
[Bennett(2011)] Robin L. Bennett. The Practical Guide to the Genetic Family History. John Wiley & Sons,
September2011. ISBN978-1-118-20981-3.doi:10.1002/9780470568248
[Hamoshetal.(2005)] Ada Hamosh, Alan F. Scott, Joanna S. Amberger, Carol A. Bocchini, and Victor A.
McKusick. Online Mendelian Inheritance in Man (OMIM), a knowledgebase of human genes and ge-
netic disorders. Nucleic Acids Research, 33(Database Issue):D514–D517, January 2005. ISSN 0305-1048.
doi:10.1093/nar/gki033.
[Pavanetal.(2017)] SoniaPavan,KathrinRommel,Mar´ıaElenaMateoMarquina,SophieHo¨hn,Vale´rieLanneau,
and Ana Rath. Clinical Practice Guidelines for Rare Diseases: The OrphanetDatabase. PLOS ONE, 12(1):
e0170365,January2017. ISSN 1932-6203. doi:10.1371/journal.pone.0170365. Publisher: PublicLibraryof
Science.
[Ginsburgetal.(2019)] GeoffreyS. Ginsburg, R. Ryanne Wu, and LoriA. Orlando. Family health history: un-
derused for actionable risk assessment. The Lancet, 394(10198):596–603, August 2019. ISSN 0140-6736,
1474-547X. doi:10.1016/S0140-6736(19)31275-9.
[Vigeland(2021)] MagnusD.Vigeland.PedigreeanalysisinR.AcademicPress,2021.ISBN978-0-12-824430-2.
doi:10.1016/C2020-0-01956-0

476 AProbLogprogramforMendelianinheritanceanalyses
[DeRaedtetal.(2007)] LucDeRaedt,AngelikaKimmig,andHannuToivonen. ProbLog:AprobabilisticProlog
anditsapplicationinlinkdiscovery. InIJCAI2007,Proceedingsofthe20thinternationaljointconferenceon
artificialintelligence,pages2462–2467,2007. URLhttps://dblp.org/rec/conf/ijcai/RaedtKT07
[Bryant(1986)] RandalBryant. Graph-BasedAlgorithmsforBooleanFunctionManipulation.IEEETransactions
onComputers,C-35(8):677–691,August1986. ISSN0018-9340. doi:10.1109/TC.1986.1676819.
[Driesetal.(2015)] AntonDries, AngelikaKimmig, WannesMeert, JorisRenkens, GuyVandenBroeck,Jonas
Vlasselaer, and Luc De Raedt. ProbLog2: Probabilistic Logic Programming. In Albert Bifet, Michael
May, Bianca Zadrozny, Ricard Gavalda, Dino Pedreschi, Francesco Bonchi, Jaime Cardoso, and Myra
Spiliopoulou, editors, Machine Learning and Knowledge Discovery in Databases, Lecture Notes in Com-
puter Science, pages 312–315, Cham, 2015. Springer International Publishing. ISBN 978-3-319-23461-8.
doi:10.1007/978-3-319-23461-837.
[Fierensetal.(2015)] Daan Fierens, GuyVan Den Broeck, JorisRenkens, Dimitar Shterionov,Bernd Gutmann,
IngoThon, Gerda Janssens, and Luc De Raedt. Inferenceand learningin probabilisticlogic programsusing
weighted Boolean formulas. Theory and Practice of Logic Programming, 15(3):358–401,May 2015. ISSN
1471-0684,1475-3081. doi:10.1017/S1471068414000076.
[Thomas(2004)] Duncan C. Thomas. Statistical Methods in Genetic Epidemiology. Oxford University Press,
Incorporated,Cary,1edition,2004. ISBN978-0-19-515939-4.doi:10.1093/oso/9780195159394.001.0001
[Gusellaetal.(1983)] James F. Gusella, Nancy S. Wexler, P. Michael Conneally, Susan L. Naylor, Mary Anne
Anderson, Rudolph E. Tanzi, Paul C. Watkins, Kathleen Ottina, Margaret R. Wallace, Alan Y. Sakaguchi,
AnneB.Young,IraShoulson,ErnestoBonilla,andJosephB.Martin. ApolymorphicDNAmarkergenetically
linkedtoHuntington’sdisease. Nature,306(5940):234–238,1983. ISSN0028-0836. doi:10.1038/306234a0.
[Wexleretal.(1987)] Nancy S. Wexler, Anne B. Young, Rudolph E. Tanzi, H. Travers, S. Starostarubinstein,
John B. Penney, S. Robert Snodgrass, Ira Shoulson, Fidela Gomez, Mar Arroyo, Graciela K. Penchaszadeh,
H. Moreno, K. Gibbons, A. G. Faryniarz, W. Hobbs, M. A. Anderson, Ernesto Bonilla, P. Michael Con-
neally,andJamesF.Gusella. HomozygotesForHuntingtons-disease. Nature,March1987. ISSN0028-0836.
doi:10.1038/326194a0. Publisher:MacmillanMagazinesLtd.
[Blockeel(2004)] Hendrik Blockeel. Probabilistic logical models for Mendel’s experiments: An exercise. In:
InductiveLogicProgramming,14thInternationalConference,ILP-2004,WorkinProgress20—24,2004.URL
https://lirias.kuleuven.be/retrieve/393067
[Meertetal.(2010)] Wannes Meert, Jan Struyf, Hendrik Blockeel. CP-Logic Theory Inference with Con-
textual Variable Elimination and Comparison to BDD Based Inference Methods. In: Inductive Logic
Programming (ed. De Raedt, L.) 5989(1):96—109, 2010. Publisher: Springer Berlin Heidelberg.
doi:10.1007/978-3-642-13840-910
[Vigeland(2022)] MagnusD.Vigeland.QuickPed:anonlinetoolfordrawingpedigreesandanalysingrelatedness.
BMCBioinformatics,23(1):220,June2022. ISSN1471-2105. doi:10.1186/s12859-022-04759-y.
[Klingetal.(2014)] Daniel Kling, Andreas O. Tillmar, and Thore Egeland. Familias 3 – Extensions and new
functionality. Forensic Science International: Genetics, 13:121–127, November 2014. ISSN 1872-4973.
doi:10.1016/j.fsigen.2014.07.004.
[WattendorfandHadley(2005)] Daniel J. Wattendorf and Donald W. Hadley. Family History: The Three-
Generation Pedigree. ISSN 0002-838X American Family Physician, 72(3):441–448, August 2005. URL
https://pubmed.ncbi.nlm.nih.gov/16100858/
[Husseinetal.(2020)] Norita Hussein, Tun Firzara Abdul Malik, Hani Salim, Azah Samad, Nadeem Qureshi,
and Chirk Jenn Ng. Is family history still underutilised? Exploring the views and experiences of primary
care doctorsin Malaysia. Journalof Community Genetics, 11(4):413–420,October 2020. ISSN 1868-6001.
doi:10.1007/s12687-020-00476-2.
[Kearneyetal.(2020)] Elizabeth Kearney, Antonina Wojcik, and Deepti Babu. Artificial intelligence in genetic
servicesdelivery: Utopiaorapocalypse? JournalofGeneticCounseling,29(1):8–17,2020. ISSN1573-3599.
doi:10.1002/jgc4.1192.

MaximeMahout 477
[Nazarethetal.(2021)] Shivani Nazareth, Laura Hayward, Emilie Simmons, Moran Snir, Kathryn E. Hatchell,
Susan Rojahn, Robert Nathan Slotnick, and Robert L. Nussbaum. Hereditary Cancer Risk Using a Genetic
Chatbot Before Routine Care Visits. Obstetrics and Gynecology, 138(6):860–870, December 2021. ISSN
0029-7844. doi:10.1097/AOG.0000000000004596.
[Vidal(2025)] GermanVidal.ExplainingExplanationsinProbabilisticLogicProgrammingIn:Kiselyov,O.(eds)
ProgrammingLanguagesandSystems.APLAS2024.LectureNotesinComputerScience,15194(1):130–152,
2025. doi:10.1007/978-981-97-8943-67. Publisher:SpringerNatureSingapore.
[Ariasetal.(2020)] Joaqu´ın Arias, Manuel Carro and Zhuo Chen and Gopal Gupta. Justifications for Goal-
DirectedConstraintAnswerSetProgramming. In: ProceedingsofICLP2020. EPTCS,325(1):59–72,2020.
doi:10.4204/EPTCS.325.12.
---- END DOCUMENT ----
