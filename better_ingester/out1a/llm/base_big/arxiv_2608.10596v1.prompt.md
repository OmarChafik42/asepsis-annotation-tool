Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
A Note on the Identification Step in
“A Semistructural Methodology for Policy
Counterfactuals”
HenriKeränen∗
UniversityofHelsinki
August2026
Abstract
TheNewKeynesianexampleofBeraja(2023)isnotidentifiedatitsprintedcalibration:
morethanonestructuresatisfieseveryconditionofitsidentificationstep. Twoofthe
paper’s six identifying restrictions coincide on equilibrium equations consistent with
theprintedreducedform,leavingelevenconditionstodetermineanequation’stwelve
coefficients. Thenotederivestherankconditiontheidentificationsteprequires,com-
putablefromthereducedformandtherestrictionsalone. Thenotealsodocumentsand
correctsamisprintinthepaper’scounterfactualdisplay. Aone-clauseamendmentto
thepaper’sTheorem1restoresitsconclusion.
1 Introduction
Beraja (2023) develops an elegant methodology for constructing counterfactuals with re-
specttochangesinpolicyrules: itdoesnotrequirecommittingtoafullyspecifiedmodel,
yetitisnotsubjecttothecritiqueofLucas(1976). Themethodappliestodynamicstochas-
ticmodelswhoseequilibriaarewellapproximatedbyalinearrepresentation. Modelsthat
match an economy’s reduced-form equilibrium under a benchmark policy rule are obser-
vationally equivalent, and the method rests on the insight that many of them, regardless
oftheirmicrofoundations, alsogenerateanidenticalcounterfactualequilibriumunderan
alternativeone: thepaper’sprincipleofcounterfactualequivalence. Themethodproceeds
in three steps: estimate, from data generated under the benchmark policy, the recursive
lawofmotionoftheequilibrium,thereduced-formmodel;imposeenoughrestrictionson
∗Preliminarydraft.Commentswelcome:henri.keranen@helsinki.fi.
1
6202
guA
11
]NG.noce[
1v69501.8062:viXra

the equilibrium equations to identify, given the reduced-form model, the remaining coef-
ficients, the structure; and solve for the counterfactual equilibrium of the identified struc-
tureunderthealternativerule. Thisnoteconcernsthesecondstep,theidentificationofthe
structure.
Theoriginalpaperillustratesthemethodinacanonicalthree-equationNewKeynesian
model, printed in full in its Section II: structure, benchmark policy rule, and the reduced
form they generate. The note documents that the example is not identified at its printed
calibration: aresearcherconfrontedwithdatageneratedbytheexamplecannotidentifyits
structureusingthepaper’srestrictions. Theresultisderivedfromthepaper’sowndisplays.
Each line of the structure, an equilibrium equation written as a row of twelve coefficients,
mustsatisfytwelvelinearconditions: sixofconsistencywiththereducedform,andthepa-
per’ssixidentifyingrestrictions. Attheprintedcalibrationtwooftherestrictionscoincide
exactlyontheconsistentlines,andelevenconditionsdonotdeterminetwelvecoefficients.
Together,thereducedformandtherestrictionsadmitstructuresthatarenotcounterfactu-
allyequivalent;theythereforedonotdeterminethecounterfactual.
Atthecenterofthenoteisarankconditionforthepaper’sidentificationstep,statedfor
every reduced form and every set of restrictions the paper’s framework allows, and com-
putablefromthosetwoobjectsalone. Theconditionsaysexactlywhenasetofrestrictions
singlesoutalineofthestructure; whenthesetdoesnot, theconditioncountsthefreepa-
rameters that remain in the line. The requirement it expresses is familiar: identification
turns on independent identifying variation, noton the number of restrictions. In fact, the
proof of the paper’s Theorem 1 already relies on the condition: the uniqueness it asserts
holds exactly when the condition does. The theorem’s statement assumes only that the
restrictions are independent; strengthening that assumption to the condition repairs the
theoreminoneclause.
The note is intended constructively. The paper’s identification step selects a structure
fromwithinanobservationallyequivalentclass,andwhatfailsattheprintedcalibrationis
theselection. Theclassandthepaper’sresultsaboutitarenotinquestion: thenoterelies
onthemthroughout,andthesecondstructureitproducesisobservationallyequivalentto
theprintedonebythepaper’sownLemmaA.1.
Section 2 sets out the example and the consistency conditions in the paper’s notation;
Section3derivesfromitsdisplaysthattheexampleisnotidentifiedattheprintedcalibra-
tion. Section4statestherankconditionandshowsthefailureexact. Section5documents
andcorrectsamisprintinthepaper’scounterfactualdisplay. Section6returnstothestate-
mentofTheorem1,givestheone-clauserepair,anddiscussesdetectionandremedies.
2

2 Setup and notation
Notation follows Beraja (2023), Section II. The endogenous variables are output, inflation,
andthenominalinterestrate,𝑥 𝑡 = (𝑦 𝑡 ,𝜋 𝑡 ,𝑖 𝑡 )′ ,inlogdeviationsfromazero-inflationsteady
state; the exogenous shocks 𝑧 𝑡 = (𝑏 𝑡 ,𝑎 𝑡 ,𝑚 𝑡 )′ — demand, cost-push, and monetary policy
— follow 𝑧 𝑡 = 𝑁𝑧 𝑡−1 + 𝜖 𝑡 with 𝑁 diagonal. With 𝑘 = 3 endogenous variables and 𝑠 = 3
shocks, each equilibrium condition is a line 0 = 𝑓 E 𝑡 𝑥 𝑡+1 + 𝑔𝑥 𝑡 + ℎ𝑥 𝑡−1 + 𝑚𝑧 𝑡, i.e., a row
vector𝑣 = (𝑓,𝑔,ℎ,𝑚) ∈ R3𝑘+𝑠 = R12. Thestructure𝜉stackstheEulerandNKPClines,
0 = E 𝑡 𝑦 𝑡+1 +𝜎−1E 𝑡 𝜋 𝑡+1 −𝑦 𝑡 −𝜎−1𝑖 𝑡 +𝑏 𝑡 , 0 = 𝛽E 𝑡 𝜋 𝑡+1 +𝜅𝑦 𝑡 −𝜋 𝑡 +𝑎 𝑡;
thepolicyΘ istheinterest-raterule
0 = 𝜃 𝜋 E 𝑡 𝜋 𝑡+1 +𝜃 𝑦 𝑦 𝑡 −𝑖 𝑡 +𝜃 𝑖 𝑖 𝑡−1 +𝑚 𝑡 .
Thepaperspecifiestheexamplebyprintingitsstructureandbenchmarkpolicynumerically,
eachrowalineintheblockorder E 𝑡 𝑥 𝑡+1 , 𝑥 𝑡, 𝑥 𝑡−1 , 𝑧 𝑡:
" #
1 1 0 −1 0 −1 0 0 0 1 0 0
𝜉0 = 2 2 ,
0 0.9 0 0.3 −1 0 0 0 0 0 1 0
(1)
h i
Θ0 = 0 0.7 0 0.5 0 −1 0 0 0.6 0 0 1
—thatis, 𝜎 = 2,𝛽 = 0.9,𝜅 = 0.3,and(𝜃 𝜋 ,𝜃 𝑦 ,𝜃 𝑖 ) = (0.7, 0.5, 0.6).1
Under determinacy (the paper’s Assumptions 1–2) the structural model generates the
reducedform𝑥 𝑡 = 𝑃0𝑥 𝑡−1 +𝑄0𝑧 𝑡;thepaperprintsthereduced-formmodelΓ0 ≡ {𝑃0,𝑄0,𝑁0}
as
2 3 2 3 2 3
60 0 −0.357 61.70 −0.50 −0.597 60.9 0 07
6 7 6 7 6 7
𝑃0 = 60 0 −0.167 , 𝑄0 = 61.46 3.24 −0.277 , 𝑁0 = 6 0 0.9 07 . (2)
6 7 6 7 6 7
6 7 6 7 6 7
40 0 0.385 41.59 1.61 0.635 4 0 0 05
Notethelastdiagonalentryof 𝑁0: themonetarypolicyshockisi.i.d. TheexhibitofSection3
turnsonthesedisplays.
Bythemethodofundeterminedcoefficients(Uhlig,1995),aline𝑣 = (𝑓,𝑔,ℎ,𝑚)iscon-
sistentwithΓ0 —itholdsidenticallyinthestate(𝑥
𝑡−1
,𝑧
𝑡
),henceoneveryequilibriumpath
1ThedisplayedΘ0 has𝜃 𝑦 = 0.5,whilethepaper’stextintroducesthecounterfactualas“𝜃 𝑦 = 0instead
of𝜃 𝑦 = 0.4”;theprinted𝑃0,𝑄0 of(2)areconsistentwith𝜃 𝑦 = 0.5,andwithneither0.4nor0. Thepaper’s
SectionII.Bcounterfactualdisplaycontainsafurther,moreconsequentialinconsistency;seeSection5.
3

—ifandonlyif
|         |          | 𝑓𝑃2+ | 𝑔𝑃+ | ℎ = 0 |     | 𝑓(𝑄𝑁     | +𝑃𝑄)+ | 𝑔𝑄  | +𝑚 = 0, |     |     |
| ------- | -------- | ---- | --- | ----- | --- | -------- | ----- | --- | ------- | --- | --- |
|         |          |      |     |       | and |          |       |     |         |     | (3) |
| i.e.,𝑣𝐾 | = 0where |      |     |       |     |          |       |     |         |     |     |
|         |          | 2 𝑃2 | 𝑄𝑁  | +𝑃𝑄 3 |     |          |       |     |         |     |     |
|         |          | 6    |     | 7     | " # |          |       | "   |         | #   |     |
|         |          | 6    |     | 7     |     |          |       |     |         |     |     |
|         |          | 6𝑃   |     | 𝑄 7   | Ψ   |          |       | 𝑃2  | 𝑄𝑁 +𝑃𝑄  |     |     |
|         | 𝐾        | ≡ 6  |     | 7     |     | ∈ R12×6, |       | ≡   |         | .   |     |
|         |          |      |     | =     |     |          |       | Ψ   |         |     |     |
|         |          | 6    | 𝐼   | 0 7   | 𝐼   |          |       | 𝑃   | 𝑄       |     |     |
|         |          | 6    | 𝑘   | 7     | 𝑘+𝑠 |          |       |     |         |     |     |
|         |          | 6    |     | 7     |     |          |       |     |         |     |     |
𝐼
|     |     | 4   | 0   | 𝑠 5 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theblockrowsof𝐾 expressthefourargumentsofalineintermsofthestate(𝑥 ,𝑧 ): the
𝑡−1 𝑡
E 𝑥
identityblockisthestateitself,andtheupperblockΨcollectstheresponsesof 𝑡 𝑡+1 and
| 𝑥   |     |     | 𝐾   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑡 to it. The matrix is the paper’s own object: it appears, unnamed, as the right-hand
factor of its display (SMERLM-NK),2 which determines {𝑃0,𝑄0}, the stable solution, by
(cid:2) (cid:3)
|     |     |     |     |     |     |     |     |     |     | 𝜉0  | 𝐾 = 0. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
requiringallthreelinesofthestructuralmodeltosatisfy(3)—inmatrixform,
Θ0
Consistency reads the same equation in the opposite direction: the reduced form is held
𝑣𝐾
fixed, and = 0 asks which lines it supports — a linear question, whereas solving for
{𝑃0,𝑄0}wasanonlinearone. Thepaper’sonlineappendixmakespreciselythisreversal: its
LemmaA.1statesthatastructureisobservationallyequivalentto𝜉0
underthebenchmark
policyifandonlyifeachofitslinessolvesthissystem;thecoefficientmatrixofitsdisplay
(NullOE)isexactly𝐾′
.
Thepaper’sidentificationstepstacks(3)withitssixper-linerestrictions,whichdemand
thatthestructurebeoftheform
|     |     | "   |     |       |     |     |     |     | #   |                |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | -------------- | --- |
|     |     | 𝜉   | 𝜉   | 0 𝜉 0 | 𝜉   | 𝜉   | 𝜉 0 | 1 0 | 0   |                |     |
|     | 𝜉   | 11  | 12  | 14    | 16  | 17  | 18  |     |     |                |     |
|     |     | =   |     |       |     |     |     |     |     | (Restrictions) |     |
|     |     | 𝜉   | 𝜉   | 0 𝜉 𝜉 | 0   | 𝜉   | 𝜉 0 | 0 1 | 0   |                |     |
|     |     | 21  | 22  | 24    | 25  | 27  | 28  |     |     |                |     |
inthecoordinatesof(1);theentrieswritten𝜉
𝑙𝑗 areunrestricted,andtherowsaretheEuler
and NKPC patterns.3 The paper states the restrictions in economic terms: “only demand
|     |     |     |     |     |     |     | 𝑎   | 𝑚   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
shocks shift the Euler equation”, for example (the 𝑡- and 𝑡-coefficients of the Euler row
set to zero), or “the interest rate does not appear in the NKPC” (the second row’s three
E
| interest-ratecoefficients,on |     |     |     | 𝑖 , 𝑖 | 𝑡,and | 𝑖 ,settozero). |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ----- | ----- | -------------- | --- | --- | --- | --- | --- |
|                              |     |     |     | 𝑡 𝑡+1 |       | 𝑡−1            |     |     |     |     |     |
2Asprinted, thethirdblockrowofthedisplay’sright-handfactorreads03,3 𝐼
|                |     |                             |     |     |     |                                      |     |     | where | 3 belongs; withthe |     |
| -------------- | --- | --------------------------- | --- | --- | --- | ------------------------------------ | --- | --- | ----- | ------------------ | --- |
| zeroblock,the𝑥 |     | coefficients—heretherule’s𝜃 |     |     |     |                                      |     |     |       |                    |     |
|                |     | 𝑡−1                         |     |     |     | 𝑖 —woulddropfromthesystemaltogether. |     |     |       | Thepaper’s         |     |
generalformofthedisplayandtheonlineappendix’s(NullOE)placetheidentitycorrectly;thedisplayisread
hereasintended.
3Asprinted,the(2,1)entryofthepaper’sdisplayreads𝜉 12—thesamesymbolasits(1,2)entry—where
𝜉 belongs;thepaper’saccompanyingtextindexestheNKPCrow’scoefficients𝜉 (itnames𝜉 23,𝜉 26,𝜉
| 21  |     |     |     |     |     |     |     |     | 2𝑗  |     | 29). |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Thedisplayisprintedhereasintended.
4

| 3 The | example | is  | not identified |     |     |     |     |     |
| ----- | ------- | --- | -------------- | --- | --- | --- | --- | --- |
Each line of the structure must satisfy twelve conditions: the six of (3) — consistency
with the reduced-form model Γ0 generated under the benchmark policy — and the six
of (Restrictions). The paper’s Theorem 1 concludes that imposing the six restrictions is
enough: each line is the unique solution of these twelve conditions. That the conclusion
fails at the printed calibration can be established by counting the conditions themselves:
Γ0,
for a line consistent with two of its six restrictions coincide, and eleven conditions do
not determine twelve coefficients. An exclusion supplies identifying variation only if the
excludedvariablemovestheequilibriuminadirectionofitsown.
Both patterns of (Restrictions) exclude the two variables that belong to the policy rule
alone: the lagged interest rate and the monetary policy shock. The shock, i.i.d., shifts the
rule once and carries no news about future policy; the lagged rate too shifts it once, with
the smoothing coefficient 𝜃 = 0.6. A line 𝑣 of the structure meets the pair in two ways:
𝑖
| directly,throughitsowncoefficientsonthem,𝑣 |     |     |     |     | and𝑣 |                               |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ---- | ----------------------------- | --- | --- |
|                                            |     |     |     | 𝑖   |      | 𝑚 (theentriesthetwoexclusions |     |     |
|                                            |     |     |     | 𝑡−1 |      | 𝑡                             |     |     |
|                                            |     |     |     |     |      | E 𝑥 and𝑥                      |     |     |
target),andindirectly,throughitsotherarguments,since 𝑡 𝑡+1 𝑡 movewhenthepair
moves. Consistency with Γ0 demands that the line hold identically in the state (𝑥 𝑡−1 ,𝑧 𝑡 ),
so, variable by variable, the direct coefficient must cancel the indirect appearance. The
|     |     |     |     |     |     | 𝑥 𝑝 | 𝑖   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
indirect appearances can be written out. The lagged rate moves 𝑡 by 𝑖, the 𝑡−1 -column
| of𝑃0;theshockmovesitby |     |     | 𝑞 𝑚 𝑡-columnof𝑄0 |     |                             |     |     | 𝑥   |
| ---------------------- | --- | --- | ---------------- | --- | --------------------------- | --- | --- | --- |
|                        |     |     | 𝑚,the            |     | —thereduced-formresponsesof |     |     | 𝑡   |
to the lagged rate and to the shock. Advancing the reduced form one period and taking
|     |     | E 𝑥 = 𝑃0𝑥 | +𝑄0𝑁0𝑧 |     |     |     | 𝑃0𝑝 |     |
| --- | --- | --------- | ------ | --- | --- | --- | --- | --- |
expectations, 𝑡 𝑡+1 𝑡 𝑡: thelaggedratemovestheexpectationby 𝑖, the
|     | 𝑃0𝑞 |     | 𝑞   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
shock by 𝑚 — plus a forecast term, 𝑚 scaled by the shock’s own persistence, zero for
the i.i.d. shock. These responses enter the line through its blocks 𝑓 and 𝑔: its indirect
appearance at the lagged rate is 𝑓(𝑃0𝑝 )+ 𝑔𝑝 = (𝑓𝑃0 + 𝑔)𝑝 𝑖; at the shock, (𝑓𝑃0 + 𝑔)𝑞 𝑚.
𝑖 𝑖
|         | 𝑓𝑃0+𝑔(whatthelinepicksupthrough |     |     | E   | 𝑥 and𝑥 |                             |     |     |
| ------- | ------------------------------- | --- | --- | --- | ------ | --------------------------- | --- | --- |
| Onerow, |                                 |     |     |     | 𝑡 𝑡+1  | 𝑡),multipliesbothresponses. |     |     |
The𝑖 -columnofthefirstconditionin(3)andthe𝑚
| 𝑡−1 |     |       |           |        | 𝑡-columnofthesecondthereforeread |       |     |     |
| --- | --- | ----- | --------- | ------ | -------------------------------- | ----- | --- | --- |
|     |     | (𝑓𝑃0+ | 𝑔)𝑝 +𝑣 0, | (𝑓𝑃0+  | 𝑔)𝑞                              | +𝑣 0. |     |     |
|     |     |       | 𝑖 𝑖 =     |        |                                  | 𝑚 𝑚 = |     |     |
|     |     |       | 𝑡−1       |        |                                  | 𝑡     |     |     |
|     |     |       |           | 𝑣 and𝑣 |                                  |       |     | 𝑓   |
Eachconditionsolvesforthetargetedentry: 𝑖 𝑚 aredeterminedlinearlyby and
|     |     |     |     | 𝑡−1 | 𝑡   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑔 —theblocksbehindtheindirectappearances.
The three lines of the structural model are consistent by construction (that is how
{𝑃0,𝑄0}wasdetermined),andtheirdirectcoefficientsareprintedin(1):
zerointheEuler
|     |     | 𝜃   |     |     |     | 𝑓𝑃0 + 𝑔 | 𝐽;  |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- |
andNKPClines, 𝑖 and1intherule. Stackthethreerows intoamatrix across
5

thethreelines,thetwoconditionsreadastwosystemsinthecolumns:
|     |     |        | 0         | 0          |     |     |
| --- | --- | ------ | --------- | ---------- | --- | --- |
|     |     |        | ' “       | ' “        |     |     |
|     |     |        | › fi      | › fi       |     |     |
|     |     | 𝐽𝑝 = − | ›0fi , 𝐽𝑞 | = − ›0fi . |     |     |
|     |     | 𝑖      | 𝑚         |            |     |     |
𝜃
|     |     |     | « 𝑖‹ | «1‹ |     |     |
| --- | --- | --- | ---- | --- | --- | --- |
The two right-hand sides are proportional — the first is 𝜃 times the second — and the
𝑖
| matrix𝐽 |     |     |     |     | 𝑝 𝜃 | 𝑞   |
| ------- | --- | --- | --- | --- | --- | --- |
isinvertibleunderdeterminacy,sothesolutionsinherittheproportion: 𝑖 = 𝑖 𝑚,
anidentityintheexample’sparameters.
Theremainingcolumnsof𝑃0 arezero. At 𝑦 and𝜋 thefirstconditionin(3)reads
|     |     |     | 𝑡−1 | 𝑡−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
as it did at the lagged rate, but with no direct coefficient to do the cancelling: no line of
(1) carries lagged output or inflation. The indirect appearances must therefore be zero on
their own: across the three lines, 𝐽 times each of the first two columns of 𝑃0 is zero. With
𝐽 invertible, so are the columns themselves — 𝑝 = 𝜃 𝑞 is the only column 𝑃0 has. The
𝑖 𝑖 𝑚
𝑃0
printed page displays it: in (2) the first two columns of are zero, and, to two decimals,
|     | 0.6 | 𝑚   | 𝑄0. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
the third is times the 𝑡-column of Of the lagged state, only the rate reaches the
equilibrium,andonlythroughtheinterceptthattherulefeedsthesystem,𝜃 𝑖 +𝑚 𝑡. To
𝑖 𝑡−1
the rest of the economy the pair is thus the same event at different sizes: two states that
differonlyinhowtheinterceptissplitbetweenthelaggedrateandtheshockgeneratethe
samepathofoutput,inflation,andtheinterestrate.
What the equilibrium bundles, no consistent line can separate. With 𝑝 = 𝜃 𝑞 𝑚, what
𝑖 𝑖
| 𝑣 and𝑣            | cancelisoneandthesamescalar—(𝑓𝑃0+𝑔)𝑞 |     |                                   |                                |       |     |
| ----------------- | ------------------------------------ | --- | --------------------------------- | ------------------------------ | ----- | --- |
| 𝑖                 | 𝑚                                    |     |                                   | 𝑚,theline’sexposuretotheinter- |       |     |
| 𝑡−1               | 𝑡                                    |     |                                   |                                |       |     |
| cept—onceatscale𝜃 |                                      |     | everylineconsistentwithΓ0carries𝑣 |                                | 𝜃     | 𝑣   |
|                   | 𝑖andonceatscale1:                    |     |                                   |                                | 𝑖 = 𝑖 | 𝑚 . |
|                   |                                      |     |                                   |                                | 𝑡−1   | 𝑡   |
Anexclusion,imposedonaconsistentline,thereforestrikesnofreeunknown: consistency
hasalreadysolvedthetargetedentryout,andtheexclusionisonelinearrestrictiononthe
coefficients that remain free. The pair supplies a single direction of identifying variation
to restrict against — two excluded instruments with collinear first stages count as one. A
consistentlinethusexcludes𝑖 ifandonlyifitexcludes𝑚 —onerestrictionstatedtwice.
|     |     | 𝑡−1 |     | 𝑡   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
The count is now short. Given consistency, the two exclusions have become one re-
striction. Thepaper’ssixrestrictionsthusamounttofive,andaline’stwelveconditionsto
eleven: eleven linear equations in twelve unknowns. The system is solvable: the printed
linesatisfiesalltwelveconditions,therestrictionsvisiblyin(1),anditisconsistentbycon-
Througheachof𝜉0’slinesthereforerunsatleastaone-parameterfamilyofsolu-
struction.
tionsofthesametwelveconditions.
The paper’s Theorem 1 concludes that exactly one structural model satisfies its condi-
|     |     | Γ0  | Θ0, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
tions (i)–(ii): reduced form under the policy and the restrictions in each line of the
structure. The family delivers a second. Substitute for the printed NKPC line any other
member 𝑣¯ of its family, keeping the Euler line as it stands in (1); the new structure then
6

differsfrom𝜉0
initsNKPClinealone. Noneoftheconditionstiesonelinetotheother: (3)
constrainsonelineatatime, andeachpatternof (Restrictions)bindsitsownline, soeach
lineofthenewstructurecanbecheckedaloneforthesametwoproperties,consistencywith
Γ0 and its own restrictions. The new line 𝑣¯ brings both by membership: the twelve condi-
tionsdefiningitsfamilyareexactlythesixof(3)andthesixofitspatternin(Restrictions).
TheEulerline,untouched,bringsbothfromtheprintedpage: itsrestrictionsarevisiblein
(1), and it is consistent by construction. Every line of the new structure is thus consistent
withΓ0,andbythepaper’sownLemmaA.1thestructureisobservationallyequivalentto
| 𝜉0  |     |     |     | Θ0, |     |
| --- | --- | --- | --- | --- | --- |
under the benchmark policy. Paired with the same it is a second structural model
satisfying the conditions (i)–(ii) of the paper’s Theorem 1 as stated. The example is not
identified.
| 4 The rank | condition |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |
IdentificationofalineamountstoeliminatingeveryΓ0-consistentlineotherthanthetrue
one,sothefirststepistodescribethemall.
Lemma 1 (Consistent lines). A line 𝑣 = (𝑓,𝑔,ℎ,𝑚) is consistent with a reduced-form model
Γ = {𝑃,𝑄,𝑁}ifandonlyif
|     |     | (ℎ, 𝑚) | −(𝑓, 𝑔)Ψ, |     |     |
| --- | --- | ------ | --------- | --- | --- |
= (4)
sothesetofΓ-consistentlinesisparameterizedfreelyby(𝑓,𝑔): asubspaceofdimensionexactly2𝑘,
withbasistherowsof
|     |            | "         |            | #           |     |
| --- | ---------- | --------- | ---------- | ----------- | --- |
|     | (cid:2)    | (cid:3) 𝐼 | − 𝑃 2 −(𝑄𝑁 | +𝑃𝑄)        |     |
|     |            | 𝑘 0       |            | R2𝑘×(3𝑘+𝑠). |     |
|     | 𝐵 ≡ 𝐼 | −Ψ | =         |            | ∈           |     |
2𝑘
|                      |     | 0 𝐼 𝑘             | − 𝑃 −𝑄 |                  |                 |
| -------------------- | --- | ----------------- | ------ | ---------------- | --------------- |
| Bytheblockformof𝐾,𝑣𝐾 |     | (𝑓,𝑔)Ψ+(ℎ,𝑚),so𝑣𝐾 |        |                  |                 |
| Proof.               |     | =                 |        | = 0isexactly(4): | theΓ-consistent |
linesformthegraphof(𝑓,𝑔) ↦→ −(𝑓,𝑔)Ψ,thatis,therowspaceof𝐵,whose𝐼
2𝑘blockmakes
therowsindependent. □
Writtenoutasequations,therowsof𝐵areidentitiesthatholdoneveryequilibriumpath
|                                           |     |     | with𝑒 | 𝑗-thcoordinatevector,row𝑘+𝑗 |     |
| ----------------------------------------- | --- | --- | ----- | --------------------------- | --- |
| regardlessofthebehaviorthatgeneratedthem: |     |     |       | 𝑗 the                       |     |
isthelawofmotionofthe𝑗-thvariable,0 𝑥 −𝑒′ 𝑃𝑥 −𝑒′ 𝑄𝑧 𝑡,androw𝑗isitsexpectation
= 𝑗,𝑡 𝑡−1
|     |     |     | 𝑗   | 𝑗   |     |
| --- | --- | --- | --- | --- | --- |
−𝑒′ −𝑒′
oneperiodaheadwith𝑥 substitutedout,0 = E 𝑥 𝑃2𝑥 (𝑄𝑁+𝑃𝑄)𝑧 𝑡. Adding
|     | 𝑡   |     | 𝑡 𝑗,𝑡+1 | 𝑗 𝑡−1 𝑗 |     |
| --- | --- | --- | ------- | ------- | --- |
anycombinationofthemtoanequilibriumequationproducesanotherequationthatfitsthe
2𝑘-dimensional
data equally well; identification requires the restrictions to eliminate this
span.4
4Theingredientsareinthepaper’sonlineappendix:
itsLemmaA.1showsthateverylineofastructure
7

Nothinginthelemmaisspecifictotheexampleoritsdimensions. Inthepaper’sgeneral
model (SME), the structure’s conditions carry one additional term, in E 𝑡 𝑧 𝑡+1 ; the paper’s
Definition1accordinglycollectsastructure’sshockcoefficientsintothesingleblock(𝐿𝑁+
𝑀), so a line of a general structure is again a vector of 3𝑘 + 𝑠 coordinates 𝑣 = (𝑓,𝑔,ℎ,𝑚),
with 𝑚 = (𝐿𝑁 + 𝑀) 𝑙. The policy lines of (SME) carry no such term at all.5 Either way, a
line’sconsistencywithareduced-formmodelΓ = {𝑃,𝑄,𝑁}readsexactlyasin(3),andthe
lemmaappliesunchanged.
Section3’sargumentwasacount,andcountinggoesonlysofar: itdetectsafailurewith-
outdelimitingit,anditboundsasolutionset’sdimensiononlyfrombelow. Twoquestions
are left open: which menus of restrictions stay independent on the consistent lines, and
whetherafamilythecountfindsisthewholesolutionsetofaline’sconditions. Bothturn
on the rank of one matrix, computable from the reduced form and the menu alone. The
matrixisreadoff 𝐵. Thepaper’sTheorem1takesasgiven,foreachlineofthestructure,a
menuof2𝑘 linearrestrictions(its{𝑅
𝑙
,𝑟
𝑙
})andassumesthemindependent.
Proposition 1 (The rank condition). Let Γ be a reduced-form model and 𝑅𝑣′ = 𝑟 a menu of 2𝑘
linearrestrictionsonaline, with 𝑅 = [𝑅 𝑓𝑔 | 𝑅 ℎ𝑚 ] ∈ R2𝑘×(3𝑘+𝑠) splitalongtheline’sblocks. The
menuissatisfiedbyexactlyoneΓ-consistentlineforevery𝑟 ifandonlyif
𝑅𝐵′ = 𝑅 𝑓𝑔 −𝑅 ℎ𝑚Ψ ′ ∈ R2𝑘×2𝑘 (5)
is nonsingular. When 𝑅𝐵′ is singular, no value of 𝑟 delivers uniqueness: the Γ-consistent lines
satisfyingthemenu,ifany,formanaffinefamilyofdimension2𝑘 −rank(𝑅𝐵′).
Proof. Ontheconsistentlines𝑣 = 𝑎𝐵ofLemma1,𝑎 = (𝑓,𝑔)free,themenureads𝑅𝐵′𝑎′ = 𝑟,
asquarelinearsysteminthe2𝑘freecoordinates;sincetherowsof𝐵areabasis,thesystem’s
solutionscorrespondone-to-oneandlinearlytotheconsistentlinessatisfyingthemenu. It
hasauniquesolutionforevery𝑟 ifandonlyif𝑅𝐵′ isnonsingular,thatis,ifandonlyifthe
menueliminatesthespanoftherowsof𝐵;otherwiseitssolutionset,andwithitthefamily
ofsuchlines,isemptyoraffineofdimension2𝑘 −rank(𝑅𝐵′). □
Independenceofthemenuisnotassumed: dependentrowsmake(5)singularoutright,
so nonsingularity already entails it. The criterion is, moreover, the paper’s own determi-
nant. The proof of Theorem 1 stacks the menu beneath the 𝑘 + 𝑠 conditions of (3) into a
(3𝑘 + 𝑠)-square system, the system the paper displays as “exactly determined”. Because
observationallyequivalentto𝜉0underthebenchmarkpolicysolves𝑣𝐾=0;thecommentthatfollowsitnotes
thesystemisunderdetermined—3𝑘+𝑠unknownsagainst𝑘+𝑠equations;andtheproofofitsPropositionA.1
alreadyrecoverstherestofalinefromits(𝑓,𝑔)-half.Lemma1addstheexactdimensionandtheexplicitbasis.
5Theblocks(𝑓,𝑔,ℎ,𝑚)lowercaseDefinition1’s𝜉 ≡ [𝐹 𝐺 𝐻 (𝐿𝑁 +𝑀)];theSectionIIdisplaysnameno
blocks.Inthepaper’snotationthestructurehas𝑘−𝑝lines,𝑝ofthe𝑘variablesbeingpolicyvariables.
8

(ℎ,𝑚)-columns,
the consistency rows carry an identity block in the they eliminate those
coefficients, the same substitution Lemma 1 already made, and the elimination reduces
det(𝑅𝐵′)
the stacked system to (5): the system’s determinant equals exactly,6 and its rank
equals (𝑘 + 𝑠) + rank(𝑅𝐵′). Singularity of (5) is thus singularity of the system the paper
displays,whoseentirerankdeficiencysitsinthemenu’s2𝑘
rows.
In the example the matrix is singular, and Section 3’s identity is the reason: it makes
tworowsof(5)collinear. Anexclusionof 𝑖 orof 𝑚 isamenurowwithzero(𝑓,𝑔)-part
|     |               |     | 𝑡−1 𝑡 |     |     |     |
| --- | ------------- | --- | ----- | --- | --- | --- |
|     | (ℎ,𝑚)-blocks, |     |       | 𝑅𝐵′ |     |     |
and a single unit entry in the so its row of is, up to sign, a transposed
E 𝑥 𝑥
column ofΨ, the responses of 𝑡 𝑡+1 and 𝑡 to the excluded variable. For the lagged rate
thatcolumnis(𝑃0𝑝 , 𝑝 );fortheshockitis(𝑃0𝑞 , 𝑞 ),wherethe 𝑁0-termhasoncemore
|     | 𝑖 𝑖 |     | 𝑚 𝑚 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
vanishedbecausetheshockisi.i.d. With𝑝 = 𝜃 𝑞 𝑚,thefirstis𝜃 timesthesecond: thetwo
|     |     |     | 𝑖 𝑖 | 𝑖   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
𝑅 −𝑅 ′
exclusionsrestrictagainstoneandthesamedirectionofidentifyingvariation. 𝑓𝑔 ℎ𝑚Ψ
isthereforesingularforeverymenucontainingboth,whateveritsother2𝑘 −2rows.
Both
of the paper’s patterns exclude the pair. Each pattern’s six rows are distinct coordinate
vectors,linearlyindependent: thehypothesisholdsasprinted. Whatfailsintheexampleis
notthetheorem’sstatedconditionbuttheoneitsconclusionneeds: independenceonthe
consistentlines.
The same matrix decides whether the collapse goes further. In the example 2𝑘 = 6,
|     |     |     |     |     | 𝑅 − 𝑅 | ′   |
| --- | --- | --- | --- | --- | ----- | --- |
so identification of a line needs rank six; at the printed calibration 𝑓𝑔 ℎ𝑚Ψ has rank
exactlyfiveforeachofthetwopatterns. Fromabove,theidentitycapstherank: withtwo
of the six rows collinear, they span at most five directions. From below, a 5×5 minor of
each pattern’s matrix is nonzero: five of its rows are independent, and no further depen-
dencehides. Eachline’stwelveconditionsthushaverankeleven,andbyProposition1their
solution set, which contains the printed line, is an affine family of dimension exactly one:
Section 3’s “at least” is exact, and the families are not part of the solution sets but all of
them.
FortheNKPCpatternthefamily’sdirectionhasaclosedformintheexample’sparame-
ters. Write𝜌 = 0.9forthecommonpersistenceofthedemandandcost-pushshocksin 𝑁0,
| 𝑒 𝑒 𝑒 |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
and 𝑦, 𝜋, 𝑖 forthecoordinatevectorsofoutput,inflation,andtherate,andtake
|     |               |        | (cid:0) |            | (cid:1) |     |
| --- | ------------- | ------ | ------- | ---------- | ------- | --- |
|     | 𝑣 = ( 𝑓, −𝜌𝑓, | 0, 0), | 𝑓 ≡ 𝑒   | ′𝑞 , −𝑒 ′𝑞 | , 0 ,   |     |
|     |               |        |         | 𝜋 𝑚 𝑦      | 𝑚       | (6) |
𝑞
a nonzero combination of the output and inflation coordinates that is orthogonal to 𝑚.
Section3left𝑃0 withasinglenonzerocolumn,𝑃0 𝜃 𝑞 𝑒 ′ 𝑓𝑃0 𝜃 (𝑓𝑞 )𝑒 ′
|     |     |     | =   | 𝑖 𝑚 ,so | = 𝑖 𝑚 | = 0,and |
| --- | --- | --- | --- | ------- | ----- | ------- |
|     |     |     |     | 𝑖       |       | 𝑖       |
bothbracketsof(3)closebyshortalgebra: 𝑣isaconsistentline,zeroineverycoefficientthe
|                                                  |     |     | (cid:2) | (cid:3)   | (cid:2) (cid:3)           |     |
| ------------------------------------------------ | --- | --- | ------- | --------- | ------------------------- | --- |
| 6Post-multiplyingthestackedmatrixbytheunimodular |     |     | 𝐼 𝑘 0   |           | 0 𝐼                       |     |
|                                                  |     |     | − 2 ′ 𝐼 | sendsitto | 𝑅 𝐵′ 𝑅 ;theblockswapcosts |     |
|                                                  |     |     | Ψ       |           | ℎ𝑚                        |     |
(−1)2𝑘(𝑘+𝑠)
,anevenpower,sotheequalityholdssignincluded.
9

NKPC pattern restricts. The solution set through the printed line consists of its translates
| by𝜆𝑣,𝜆 |     | ∈ R Writtenasanequation,𝑣says |     |     | E [𝑓𝑥 | ]   | 𝜌 𝑓𝑥 |                           |
| ------ | --- | ----------------------------- | --- | --- | ----- | --- | ---- | ------------------------- |
|        |     | .                             |     |     | 𝑡     | 𝑡+1 | =    | 𝑡 —anidentityofthereduced |
form, true regardless of the behavior that generated it. For the Euler pattern no equally
shortexpressionoffersitself,butbythesamerankcountitsdirectionexistsandisunique
uptoscale, andmembersofeitherfamilydifferfromtheprintedlinesonlyincoefficients
thepaper’srestrictionsnevertouch.
Remark 1 (The failure is consequential). The multiplicity is not a harmless normalization:
membersofthefamiliesarenotcounterfactuallyequivalent. Scaleeachfamily’sdirection
E 𝑦 E 𝜋
toaunitcoefficientonitsline’sownexpectationterm— 𝑡 𝑡+1 fortheEulerpattern, 𝑡 𝑡+1
𝜉0.
for the NKPC — and add half of it to that line of The resulting structure reproduces
Γ0 andsatisfies(Restrictions)inbothofitslines,yetunderthepaper’scounterfactualrule
| (𝜃  | = 0) |     |     |     |     |     |     | 4.32 |
| --- | ---- | --- | --- | --- | --- | --- | --- | ---- |
𝑦 it puts the impact response of output to a demand shock at against the true
3.51.7
A finer reading of condition (i) of the paper’s Theorem 1 does not remove the mul-
tiplicity: members near the printed lines yield determinate structures that generate Γ0 as
theiruniquereducedform. Finally,(3)and(5)containonlyΓ0 andthemenu: theobserved
policyΘ0
|     |            | entersnowhere. | Section6returnstothis. |     |     |         |     |     |
| --- | ---------- | -------------- | ---------------------- | --- | --- | ------- | --- | --- |
| 5   | A misprint |                | in the counterfactual  |     |     | display |     |     |
Comparing the numbers of Remark 1 with the paper requires one correction to its Sec-
tionII.Bdisplay. Thatsectionconsidersamorehawkishrule,thecounterfactualΘ1,which
| sets𝜃 | =   | 0andleaveseveryothercoefficientofΘ0 |     |     |     |            |     |                          |
| ----- | --- | ----------------------------------- | --- | --- | --- | ---------- | --- | ------------------------ |
|       | 𝑦   |                                     |     |     |     | unchanged. |     | Itdisplaystwocounterfac- |
tualreducedforms,thepaper’sΓ1 ˜1: {𝑃1,𝑄1}forthestructuralmodel{𝜉0,Θ1},and
andΓ
{𝑃˜ 1,𝑄˜ 1}for{𝜉1,Θ1},where𝜉1istheworking-capitalstructurethatthepaper’sSectionII.A
exhibitsasobservationallyequivalentto𝜉0 underthebenchmarkpolicy. Theprintedtran-
sitionmatrices𝑃1and𝑃˜ 1arecorrectatdisplayaccuracy(withinaunitinthelastdecimal).8
| Theprintedshockloadings𝑄1 |     |     | and𝑄˜ | 1,however,arenot. |     |     |     |     |
| ------------------------- | --- | --- | ----- | ----------------- | --- | --- | --- | --- |
Section 3’s identity detects the error in print. Its derivation used only three features
oftheenvironment: thatthelaggedrateandthemonetarypolicyshockbelongtotherule
alone,withdirectcoefficients𝜃
𝑖 and1;thattheshockisi.i.d.;andthatnolinecarrieslagged
output or inflation. Θ1 changes only 𝜃 𝑦, so all three features survive. The counterfactual
pair {𝑃1,𝑄1} must satisfy the same identity: the 𝑖 -column of 𝑃1 equal to 𝜃 times the
𝑡−1 𝑖
|     | 7The |     |     |     | 5.32 |     |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- | --- |
paper’s printed counterfactual display shows for this entry; the display is itself misprinted (it
solvestheshock-loadingstepatthebenchmark𝑃0),and3.51isthecorrectedvalue.SeeSection5.Hereandin
whatfollows,everydecimalnotprintedinthepaperiscomputedfromtheexactsolution.
8Soistheprintedstructure𝜉1:itsEulerlineisthatof(1),andalinewiththepatternofthepaper’sworking-
capitalPhillipscurve—itsdisplay(NKPC2),afterChristianoetal.(2010)—andwiththeprinted𝑎
𝑡-coefficient
| 1.5isconsistentwithΓ0 |     |     | atcoefficients(0.7001, | 0.3826, | 0.0449)onE |     | 𝜋      | 𝑦 𝑡,and𝑖              |
| --------------------- | --- | --- | ---------------------- | ------- | ---------- | --- | ------ | --------------------- |
|                       |     |     |                        |         |            |     | 𝑡 𝑡+1, | 𝑡;theprintedsecondrow |
isitstwo-decimalrounding.
10

|     |     |     |     |     |     | {𝑃˜ 1,𝑄˜ |
| --- | --- | --- | --- | --- | --- | -------- |
| 𝑚   | 𝑄1, |     |     |     |     | 1}       |
𝑡-column of and zeros in the other two columns. The pair owes it as well:
𝜉1
the shock is unchanged, and the lines of the printed carry neither the excluded pair
norlaggedoutputandinflation,soallthreefeaturesholdfor{𝜉1,Θ1}. Intheprintedpair
{𝑃1,𝑄1},thezerosareinplacebuttheproportionisnot: intheoutputrow,0.6×(−0.84) =
| −0.504 |     |     | −0.63. |     |     |     |
| ------ | --- | --- | ------ | --- | --- | --- |
stands against the printed In Section 3, the benchmark display passed the
same test. Any true reduced form satisfies the consistency conditions (3) by construction,
andtheidentityisoneoftheirconsequences: infailingit,theprintedpair{𝑃1,𝑄1}violates
(3)itself. Theprintedtransitionsarethetruecounterfactualonesatdisplayaccuracy,sothe
error is confined to the loadings. The proximate cause is traceable: re-solving the second
bracket of (3) for each pair’s loadings, with the benchmark 𝑃0 held in place of the pair’s
own transition matrix, reproduces the printed 𝑄1 in all nine entries at printed precision,
| andtheprinted𝑄˜ | 1   |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
uptoroundinginthefinaldigit.
Re-solving the same bracket at the correct transitions instead yields the display as it
shouldread(rowsandcolumnsorderedasin(2);transitionsasprinted,loadingscorrected):
|     |     | 2    | 3          | 2          |       | 3       |
| --- | --- | ---- | ---------- | ---------- | ----- | ------- |
|     |     | 60   | 0 −0.637   | 63.51      | −2.16 | −1.057  |
|     |     | 6    | 7          | 6          |       | 7       |
|     | 𝑃1  | = 60 | 0 −0.347 , | 𝑄1 = 63.06 | 1.02  | −0.567; |
|     |     | 6    | 7          | 6          |       | 7       |
|     |     | 6    | 7          | 6          |       | 7       |
|     |     |      | 0.485      | 41.56      | 0.52  | 0.815   |
40 0
|     |     | 2   | 3        | 2         |       | 3        |
| --- | --- | --- | -------- | --------- | ----- | -------- |
|     |     | 60  | 0 −0.637 | 63.64     | −2.49 | −1.057   |
|     |     | 6   | 7        | 6         |       | 7        |
|     | 𝑃˜1 | 60  | −0.337 , | 𝑄˜1 62.98 | 1.17  | −0.567 . |
|     |     | =   | 0        | =         |       |          |
|     |     | 6   | 7        | 6         |       | 7        |
|     |     | 6   | 7        | 6         |       | 7        |
|     |     | 40  | 0 0.495  | 41.52     | 0.60  | 0.815    |
𝑖 𝑚
The proportion is restored: in both pairs, the 𝑡−1 -column again stands to the 𝑡-column
0.6
in the ratio to within display rounding. The correction changes quantitative readings:
under the more hawkish rule, the impact response of output to a demand shock roughly
doubles,from1.70in(2)to3.51,whereastheprinteddisplaywouldhaveitroughlytriple,
from1.70to5.32.
Thequalitativemessageofthepaper’sSectionII.Bstands: thetwocoun-
˜1
terfactual reduced forms still differ, Γ ≠ Γ1, so the working-capital model illustrates the
Lucascritique.
6 Discussion
Thetheoremhypothesizes“asetof2𝑘
| ThestatementofTheorem1. |     |     |     |     |     | independentlinear |
| ----------------------- | --- | --- | --- | --- | --- | ----------------- |
restrictionsonthecoefficientsinline𝑙 ofastructure𝜉”andconcludesuniqueness.
Theex-
ampleshowsthatthehypothesis,asprinted,doesnotsecuretheconclusion: Section4ver-
ifiedthehypothesisforbothpatternsof(Restrictions);Section3producedasecondmodel.
The difficulty is confined to one word. “Independent” asks the restrictions to be indepen-
11

dent of one another; uniqueness needs them independent on the consistent lines. By Sec-
tion4,theproof’s“exactlydetermined”assertsthestrongerproperty;thestatementstops
at the weaker. The paper’s Section II.C, invoking the theorem for the general case, states
theidentificationstepasacount: “knowledgeof{Γ0,Θ0}imposesonlysixrestrictionsper
line in the structure, whereas there are 12 unknown structural coefficients per line. Then,
imposing six additional restrictions per line identifies the full structure 𝜉0.” Section 3 car-
riesthecountonestepfurther: givenconsistency,thesixadditionalrestrictionsamountto
five. The paper’s count shows its system square, twelve conditions on twelve coefficients;
itdoesnotshowthemindependent.
Therepair. Oneclausesuffices: replace“independent”withtherankconditionofPropo-
sition 1. The strengthened hypothesis asks that each menu’s matrix (5) be nonsingular,
equivalentlythatthepaper’sstackedsystembe. Theconclusionthenholdsentire.
Proposition 2 (Identification under the rank condition). Let Γ be a reduced-form model, Θ a
policy, and {𝑅 𝑙 ,𝑟 𝑙 } a menu of 2𝑘 linear restrictions for each structural line 𝑙 = 1,...,𝑘 − 𝑝, with
𝑅 𝑙 𝐵′ nonsingular; let 𝜉ˆ be the structure whose 𝑙-th line is its menu’s unique Γ-consistent solution
(Proposition1). Theneverystructuralmodel{𝜉,Θ}thathasreducedformΓunderΘ andsatisfies
𝑅 𝑙 𝜉′ 𝑙 = 𝑟 𝑙 in each line is {𝜉ˆ,Θ}: at most one model satisfies the two conditions. If moreover Γ
is stable and the policy’s lines are Γ-consistent, then
{𝜉ˆ,Θ}
is itself such a model if and only if it
satisfiesAssumptions1–2.
Proof. A model with reduced form Γ under Θ has every line of its structure Γ-consistent,
by the paper’s Lemma A.1; if it also satisfies the menus, each of its structural lines is its
menu’suniqueconsistentsolution,soitsstructureis𝜉ˆ
. Forthesecondclaim,everylineof
{𝜉ˆ,Θ}
is Γ-consistent, the structural lines by construction and the policy’s by hypothesis,
so Γ solves the model’s equilibrium system. If the model satisfies Assumptions 1–2, its
stablesolutionisunique,andΓ,beingstable,isthatsolution: themodelhasreducedform
Γandsatisfiesitsmenusbyconstruction. Conversely,amodelwithareducedformsatisfies
□
Assumptions1–2bythedefinitionofhavingone.
The proposition’s two conditions are the theorem’s (i) and (ii). Both hypotheses of its
existence clause are automatic for an observed pair: the observed reduced form is stable,
andtheobservedpolicyispartofthemodelthatgeneratedit,soitslinesareΓ0-consistent.
Deciding existence is then a finite computation: one linear solve per line assembles the
candidate, and a determinacy check on the assembled model settles the question; by the
proposition, the check passes exactly when some structure generating Γ0 under the ob-
servedpolicysatisfiestherestrictions. Thecounterfactualhalfofthetheoremisuntouched
12

bythefailuredocumentedhere: givenastructureandacounterfactualpolicy,thecounter-
factual reduced form comes from the same nonlinear step that determined {𝑃0,𝑄0}, and
thefailurebelongstothelinearstepbeforeit.
A canonical knife edge. Section 3’s derivation used three features of the example and
nothingelse: thelaggedrateandthepolicyshockenterthroughtherulealone; theshock
isi.i.d.;andnolinecarrieslaggedoutputorinflation. Theknifeedgeistheshock’slackof
persistence: givetheshockpersistenceandthestructurewouldgenericallybeidentified.9
Butani.i.d.policyshockalongsideinterestsmoothingisstandardNewKeynesianpractice,
inwhichpersistenceoftheinstrumentisplaceddeliberatelyintherule,astheterm𝜃 𝑖 𝑖 𝑡−1 ,
ratherthanintheshock. Aresearcherwhoadoptstheexampleasatemplatewouldinherit
itsconfiguration,andwithitthecollapse.
The observational-equivalence exhibit. While persistence in the policy shock would
generically rescue identification in the paper’s example, it would come at the price of the
paper’s Section II.A demonstration of observational equivalence. The exhibit is a pair of
modelswithdistinctmicrofoundationsandonereducedform. Thebehavioralmodelafter
Gabaix(2020)hasthestructure𝜉0in(1): atthepaper’sparameterchoicesitsPhillipscurve
(NKPC1) is the NKPC line of that structure. The working-capital structure differs in its
Phillipscurve(NKPC2)alone,sothedemonstrationhinges,bythepaper’sLemmaA.1,on
thatonelinebeingconsistentwiththereducedformthetwomodelsshare.10 Consistency
isthesixconditionsof(3). Inthecoordinatesof(1),alinewith(NKPC2)’sshapeis
(cid:0) (cid:12) (cid:12) (cid:12) (cid:1)
(cid:12) (cid:12) (cid:12)
0, 𝛽, 0 𝜅, −1, 𝜒 0, 0, 0 0, 𝛾, 0 :
four free coefficients, on expected inflation, output, the rate, and the cost-push shock; the
rate’s,𝜒,istheonethatmakesthecurveworking-capital. Sixconditionsonfourcoefficients
ingeneralleavenolineatall. However,threeofthesixcomefreeattheprintedcalibration.
The line’s lagged block is zero and the first two columns of 𝑃0 in (2) are zero, so the first
bracket of (3) demands only at the lagged rate, (𝑓𝑃0 + 𝑔)𝑝 𝑖 = 0. And the policy shock’s
condition,theshocki.i.d.andtheline’s𝑚 𝑡-coefficientzero,is(𝑓𝑃0+ 𝑔)𝑞 𝑚 = 0: Section3’s
identity 𝑝 𝑖 = 𝜃 𝑖 𝑞 𝑚 makesitthelaggedrate’soveragain. Thethreeconditionsthatremain
9Generically,becauseasingleexceptionexists: thepersistencethedemandandcost-pushshocksalready
share.
10Thepaper’sSectionII.Aaccountsfortheequivalencedifferently: “Thecommonfeatureofthesemodels
is that their structures satisfy exactly six restrictions per line; see the structure in (Restrictions) below. As
lemmaA.1intheappendixshowsinthegeneralcase, thisfeaturemakesthemobservationallyequivalent.”
However,LemmaA.1mentionsnorestrictions;andtheworking-capitallinecarriestheinterestrate,whichthe
structurein(Restrictions)excludesfromitsNKPCrow.
13

on the four coefficients leave a one-parameter family of consistent lines with (NKPC2)’s
shape,andSection5’sworking-capitallineisoneofthem,shownconsistentthere. However,
persistencewould generically leave four of the six in force: the transition matrix stays the
printed𝑃0ateverypersistence,itsfirsttwocolumnszero,whiletheshock’sconditiongains
aforecasttermthelaggedrate’slacks,andtheidentity’spaircomesapart. Fourconditions
on four coefficients pin a single line.11 The line is the printed NKPC one, a line of the
structure and so still consistent, with 𝜒 = 0 in (1): no (NKPC2) line with a nonzero 𝜒
remains,andnoworking-capitalstructuresharesthereducedform.
Detection and remedies. The failure of the identification step can be caught before any
counterfactualisattempted. Remark1notedthat(3)and(5)containonlythereducedform
and the menu of restrictions; the observed policy enters neither. The test is one 2𝑘 × 2𝑘
determinant, computable before any use is made of the structure: identification of a line
needs det(𝑅 𝑓𝑔 − 𝑅 ℎ𝑚Ψ ′) ≠ 0. At the printed calibration the determinant is zero for both
patterns. Whatrestoresidentificationisasetof2𝑘 restrictionsindependentontheconsis-
tent lines, and the determinant’s two arguments, the menu and the equilibrium, give the
two routes to it. A seventh restriction in each line takes the menu route.12 Persistence in
the policy shock takes the equilibrium route: the example’s structural lines carry nothing
oftheshock’sprocess,sothechangeleavesthemuntouchedandaltersonlytheidentifying
variationtheequilibriumsupplies. Ani.i.d.shockreachestheequilibriumonlythroughthe
rule’sintercept,asthelaggedratedoes;apersistentonecarriesnewsaboutfuturepolicy,a
directionofitsown,andthepaircomesapart,atthepricethepreviousparagraphrecords
fortheobservational-equivalenceexhibit. Thetworoutesdifferinwhocantakethem: the
menuistheresearcher’stostrengthen,theshock’sprocessbelongstotheeconomy,andthe
determinanttellswhetherthemenurouteisneeded.
Scope. One step of the paper’s architecture is at issue: the selection of a structure from
withintheobservationallyequivalentclass. Theclassstands,andsodoesthearchitecture
aroundthestep;thisnotehasreliedonboththroughout,onLemmaA.1aboveall. Withthe
rankconditioninplaceof“independent”,Theorem1’shypothesissecuresitsconclusion.
11Theexceptionisasinglepersistence,distinctfromtheothershocks’commonvalue:therethefamilyreturns
whole,andSection5’sworking-capitallineisconsistentoncemore.
12Forexample,addtotheEulerpatternthereal-ratelink,theline’sE 𝑡 𝜋 𝑡+1-and𝑖 𝑡-coefficientssummingto
zero, andtothePhillips-curvepatternthe exclusionof E 𝑡 𝑦 𝑡+1. Thematrixof (5)isthentaller thansquare,
andthecriterionisitsrank:attheprintedcalibrationeachaugmentedmenureachesrank2𝑘,soeachrestores
identificationofitsline,andtheprintedstructureandtheworking-capitalalternativesatisfythetwoadded
restrictionsalike.
14

References
Beraja, Martin (2023) “A Semistructural Methodology for Policy Counterfactuals,” Journal
ofPoliticalEconomy,131(1),190–201.
Christiano, Lawrence J., Mathias Trabandt, and Karl Walentin (2010) “DSGE Models for
MonetaryPolicyAnalysis,”inFriedman,BenjaminM.andMichaelWoodfordeds.Hand-
bookofMonetaryEconomics,3,285–367: Elsevier.
Gabaix, Xavier (2020) “A Behavioral New Keynesian Model,” American Economic Review,
110(8),2271–2327.
Lucas, Robert E. (1976) “Econometric Policy Evaluation: A Critique,” Carnegie-Rochester
ConferenceSeriesonPublicPolicy,1,19–46.
Uhlig, Harald (1995) “A Toolkit for Analyzing Nonlinear Dynamic Stochastic Models Eas-
ily,”Workingpaper.
15
---- END DOCUMENT ----
