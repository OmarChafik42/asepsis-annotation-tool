Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Reputation and institutional certification as complementary trust
mechanisms in a single online market
YutaKido*1,2 andYohsukeOhtsubo1
1GraduateSchoolofHumanitiesandSociology,TheUniversityofTokyo,Tokyo113-0033,Japan
2JapanSocietyforthePromotionofScience,Tokyo102-0083,Japan
August 19, 2026
Abstract
Reputationandinstitutionalcertificationarethetwomaintrustmechanismsunderinformation
asymmetry, yettheirinteraction remainspoorly understood. We analyze nearlyone millionfixed-
priceeBaylistingsofPokémoncards,wheresellerschooseamongthreesignals:third-partygrading
(institutional certification), self-grading (a self-claimed condition description), or no signal. We
show that self-grading and third-party grading dominate distinct regions of the reputation–value
space, with the self-grading region widening as reputation rises. Reputation also amplifies the
price premium of self-grading but not that of third-party grading. We develop a signaling game
in which a false self-claim carries an ex-post cost proportional to reputation, whereas certification
carries an ex-ante cost independent of reputation. These costs split the reputation–value space
intoequilibriumregimesthatexplainbothpatterns. Thetwomechanismsarethereforesubstitutes
withinatransactionyetcomplementsacrossthemarket,replacingthereputation-versus-institution
dichotomywitharegimestructuresetbyreputationandvalue.
Keywords: informationasymmetry|trust|reputation|institution|signalinggame
Introduction
Trust is a precondition for exchange in markets with information asymmetry. When buyers delegate the as-
sessment of product quality to sellers, they are exposed to the risk that the sellers will exploit this information
advantage(1). Akerlof(2)showedthatthisasymmetrytriggersadverseselection. Beingunabletoverifyproduct
quality,buyersofferpricesbelowthetruevalueofhigh-qualityproducts. Therefore,high-qualitysellersexitthe
market,leavingonlysellersoflow-qualityproducts(i.e.,“lemons”). Theproblemisamplifiedinonlinemarkets
in which buyers can neither directly inspect the quality of goods nor monitor sellers through repeated face-to-
facecontact. Nevertheless,platformssuchaseBaysustaintensofbillionsofdollarsintransactionsannually(3),
implyingthatalternativetrustmechanismsaddressthisinformationproblem.
One such mechanism is reputation. In repeated interactions, reputation sustains cooperation when the
prospect of future gains outweighs the benefit of short-term defection, a principle Axelrod (4) formalized as
the “shadow of the future.” The same logic applies to trust problems in markets with information asymmetry.
Online feedback systems embody this principle by making each seller’s transaction history available to future
buyers (5). Indeed, reputation scores correlate with price premiums (6), and negative feedback is associated
with increased seller exit rates (7). Similar to brand image (8), an established reputation is too valuable to be
*Towhomcorrespondenceshouldbeaddressed.E-mail:yu-kido@l.u-tokyo.ac.jp
1
6202
guA
81
]hp-cos.scisyhp[
1v21371.8062:viXra

A 3stagesincardtransaction B Pricemetrics C Sellerreputationmetrics
Fig.1. DescriptiveoverviewofthePokémoncardtransactiondataset. (A)Threestagesofacardtransaction. InStage1,aseller
choosesaqualitysignal(None,Self-graded,orTP-graded). InStage2,thesellersetsalistingpricerelativetothemarketprice.
InStage3,abuyerdecideswhethertopurchase. (B)Pricemetrics. Top: distributionoflistingprices(logUSD)bysignaltype
(None,n = 603,587; Self,n = 319,688; TP,n = 36,754). Middle: marketpricedistributionsforungraded(None,Self)and
graded(TP)itemsshownashorizontalviolin-boxplots. Bottom: distributionofthelogpriceratiop˜= log(P/V)foralllistings
(N = 960,029)andsolditems(n = 131,538),excludingoutliersbeyond1.5×theinterquartilerange(IQR);dashedlinemarks
p˜= 0. (C)Sellerreputationmetrics. Topleft: distributionsofpositivefeedbackpercentage. Topright: distributionoffeedback
score(log-transformed).Arrowsindicatedimensionalityreductionusingprincipalcomponentanalysis(PCA).Bottom:composite
reputationscorefromthePCA(N =60,386sellers).
lost for a one-shot dishonest transaction. Thus, reputation systems address information asymmetry by deriving
trustworthinessfromaseller’saccumulatedtransactionhistory(9,10).
Asecondmechanismoperatesthroughthird-partyinstitutions. Institutionaleconomistshavelongarguedthat
external enforcement reduces the transaction costs arising from information asymmetry and constrains oppor-
tunisticbehavior(11,12). Inmarketexchange,thismechanismcanoperatethroughcostlysignaling. Whenthe
costofobtainingaqualitycertificateisprohibitivelyhighforlow-qualitysellers,certificationcrediblyseparates
high-quality goods from low-quality goods (13, 14). Online markets implement this logic through third-party
verificationservicesthatindependentlycertifyproductquality(e.g.,authenticityverificationforbrandedgoods)
atacostbornebytheseller(15). Thus,third-partycertificationaddressesinformationasymmetrybyrelocating
thesourceoftrustfromthesellertoanexternalinstitution(see16,forthesamelogicinthecontextofauditing).
The social sciences have long proposed reputation and third-party institutions as two principal solutions to
the trust problem in economic and social exchanges (17–19). Conceptually, the two operate through distinct
mechanisms. Reputationbuildsendogenouslyfromaccumulatedtransactionhistory, whereascertificationrests
exogenously on institutional verification (20–22). However, these mechanisms have largely been studied in
isolation,leavingtheirinteractionpoorlyunderstoodwhenbothmechanismsaresimultaneouslyavailable. Con-
temporaryonlineplatformstypicallyhostbothmechanisms(23), providinganempiricalsettingtoaddressthis
gap.
Inthisstudy,weexaminethisquestioninthecontextofPokémontradingcardsintheeBaymarket,inwhich
2

information asymmetry is substantial. Card value depends on condition, and counterfeiting poses a persistent
riskincollectiblesmarkets(24). Theplatformofferstwotrustmechanisms: acumulativebuyer-feedbacksystem
(Fig.1C),whichcorrespondstoreputation,andthird-party(TP)gradingbyprofessionalauthenticationservices,
which corresponds to institutional certification. In addition, sellers may post a self-claimed condition descrip-
tion(self-grading). Asellerthereforehasthreesignalingoptions,denotedTP,Self,andNone(Fig.1A).Unlike
TP grading, self-grading is costless and lacks immediate verification, constituting a form of cheap talk (25).
Nonetheless,suchvoluntarysignalsarewidelyused(26)andhavebeenshowntomitigateinformationasymme-
tryinotheronlinemarkets(27),sotheircredibility,ifany,mustrestonasourceotherthanthecostofproducing
thesignal.
Using nearly one million listings, we first show that reputation interacts with signal type in two ways. The
reputation–value space separates into Self- and TP-dominant regions along a positively sloping boundary, and
reputationamplifiesthepricepremiumofself-gradingbutnotthatofTPgrading. Wethenproposeasignaling
game that formalizes two distinct trust mechanisms: reputation as collateral for the seller’s self-claimed signal
and TP grading as an externally verified signal whose credibility is independent of reputation. We examine
whether the model’s predictions align with their empirical counterparts. Finally, we let reputation evolve and
showthatasellercanmovefrominstitution-basedtoreputation-basedexchange.
Results
Empirical analysis
WefittedahierarchicalBayesianmodel(HBM)toN = 960,029fixed-pricelistings,jointlymodelingthethree
sequentialstagesofaneBaytransaction(Fig.1A).InStage1,thesellerchoosesamongthreesignals(TP,Self,
or None). Empirically, sellers chose TP in 4% of listings, Self in 33%, and None in 63%. In Stage 2, the
seller sets a listing price P relative to the item’s grade-appropriate market price V, yielding the log price ratio
p˜ = log(P/V) (Fig. 1B; see Methods for market price). The denominator V is the graded market price for
TPlistingsandtheungradedmarketpriceforSelfandNone,whereastheitem-valuepredictorinStage1isthe
ungradedmarketpriceforalllistings,providingauniformscale. InStage3,abuyereitheracceptsthelistedprice
or does not. Listing prices skew toward premiums, while sold prices concentrate on the market price (Fig. 1B,
bottom). The other primary predictor entering all three stages is each seller’s reputation score, constructed as
the first principal component of two public eBay feedback indicators (feedback score and positive feedback
percentage; Fig. 1C; see Methods). The HBM converged well for all three stages (Rˆ ≤ 1.013 across all 38
parameters). Fig.2Adisplaystheposteriordensitiesforthekeyparameters(seetableS1, fig.S5, andtableS2
forconvergencediagnostics,modelfit,andcompletecoefficienttables).
First,inthesignal-selectionstage(Fig.2A,top),wemodeledsellers’choiceswithamultinomiallogit. None
servedasthereferencecategory,andreputationanditemvalueweretheprimarypredictors(seeMethodsforthe
full specifications). For reputation, higher-reputation sellers were more likely to choose Self but less likely to
choose TP (reputation on Self: +0.054 [99% highest density interval (HDI): 0.023, 0.083]; reputation on TP:
−0.052[−0.092, −0.011], seealsoFig.2B).Foritemvalue, sellersweremorelikelytochooseTPforhigher-
valueitemsbutmorelikelytochooseSelfforlower-valueitems(logV onTP:+0.505[0.492,0.518];logV on
Self: −0.252[−0.261,−0.242]). AsshownintheleftpanelofFig.2B,thereputation–valuespacesplitintotwo
signal-dominant regions. Third-party grading prevailed in the high-value region, and self-grading dominated
in the low-value region. More importantly, the boundary’s market price increased with seller reputation. We
confirmedthispartitionwithalogisticboundaryregression,findingapositiveslope(medianβ =0.236atmean
reputation,99%HDI:[0.197,0.274];adescriptiveboundaryagrees,fig.S4).
Second,intheprice-settingstage(Fig.2A,middle),reputationhadanegligiblemaineffectonlistingprices
(+0.001 [99% HDI: −0.008, 0.009]). Instead, reputation interacted strongly with signal type. The reputation
×self-gradedinteractionwaspositive(+0.063[0.056,0.071]),suggestingthatreputationconferredcredibility
onself-gradedlistingsandgeneratedacorrespondingpricepremium. Bycontrast,thereputation×TPgrading
interactionwasnegative(−0.095[−0.115,−0.077]). TPcredibilityisderivedfromanexternalinstitutionrather
than the seller. Thus, although the absence of a positive effect is consistent with this prediction, the observed
3

A HBMposteriorcoefficients B Signalregime:posteriorprediction&observeddata
P(TP | graded)
1. Signal: Multinomial Logit (ref: None) (← Self) 0% 50% 100% (→ TP) TP
| Reputation |     |     | )DSU( ecirp tekram dedargnU |     |     |     |     |
| ---------- | --- | --- | --------------------------- | --- | --- | --- | --- |
$1,000
(on Self)
|     |     |     | $1,000 |     |     | $100 |     |
| --- | --- | --- | ------ | --- | --- | ---- | --- |
Reputation
| (on TP) |     |     |     |     |     | $10 |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
$1
Ungraded
| market price |     |     | $100 |               |     |      |     |
| ------------ | --- | --- | ---- | ------------- | --- | ---- | --- |
| (on Self)    |     |     |      | slope = 0.236 |     | Self |     |
at mean reputation
Ungraded
| market price |     |     |     |     |     | $1,000 |     |
| ------------ | --- | --- | --- | --- | --- | ------ | --- |
| (on TP)      |     |     |     | $10 |     |        |     |
$100
|     | 2. Price: log(P/V) |     |     |     |     | $10 |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- |
$1
$1
| Reputation |     |     |     | -3 -2 | -1 0 1 2   | 3 -3-2-1 0 | 1 2 3 |
| ---------- | --- | --- | --- | ----- | ---------- | ---------- | ----- |
|            |     |     |     |       | Reputation | Reputation |       |
Self
| TP  |     |     | C   | Reputationeffectonpriceratiobysignal(sold-conditional) |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
Reputation
× Self
Reputation
| × TP |     |     |     |     | AME=0.074 |     |     |
| ---- | --- | --- | --- | --- | --------- | --- | --- |
|      |     |     |     | 0.4 | Self      |     |     |
3. Sold: Pr(Sold=1)
oitar ecirp goL
AME=0.015
| Reputation |     |     |     | 0.2 |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- |
None
Self
TP
0.0
| Reputation |     |     |     |     | AME=-0.071 |     |     |
| ---------- | --- | --- | --- | --- | ---------- | --- | --- |
TP
× Self
Reputation
× TP
-0.2
| -0.25 | 0.00                        | 0.25 | 0.50 | -3  | -2 -1 0    | 1 2 | 3   |
| ----- | --------------------------- | ---- | ---- | --- | ---------- | --- | --- |
|       | Posterior coefficient value |      |      |     | Reputation |     |     |
Fig.2. HierarchicalBayesianmodelposteriorestimates. (A)Ridgelinedensityplotsofposteriorcoefficientdistributionsfromthe
three-equationHBM.Top: signal-selectionstage(multinomiallogit, referencecategorywasNone). Middle: price-settingstage
(thedependentvariablewasthelogpriceratiop˜= log(P/V)). Bottom: soldstage(thedependentvariablewasPr(Sold = 1)).
Vertical dashed line indicates zero. Points within posterior distributions represent medians; horizontal bars show 99% highest
densityintervals(HDI).(B)Signalregions: posteriorpredictionandobserveddata. Left: regionmapshowingposteriorpredicted
|     | P(TP | graded) |     | (x) |     | (y, |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- |
probability of TP grading across reputation and ungraded market price log scale). Red indicates high
probability(TP-dominant)andbluelowprobability(Self-dominant).Boundarycontourat50%.Right:hexbindensityofobserved
TP-graded(top,red)andSelf-graded(bottom,blue)listings. (C)Predictedreputationeffectonlogpriceratiobysignaltypefor
soldcards.Linesshowpredictedmarginaleffects,withtheshadedbandgivingthe95%credibleinterval.
negativeeffectisnotreadilyinterpretable. WewilldiscussthepossibleinterpretationsintheDiscussionsection
(seealsofigs.S2andS3).
Third, in the purchase stage, the coefficient on the listing-price premium was negative (−0.951 [99% HDI:
−0.969,−0.937]),indicatingthathigherpremiums(i.e.,pricesabovethemarket)reducedtheprobabilityofsale,
butreputationcounteractedthiseffect(+0.457[0.419,0.497];Fig.2A,bottom). Becauseonly13.7%oflistings
resultedinasale,listing-pricecoefficientsalonedonotcapturethepremiumsactuallyrealizedonsolditems. To
recovertheserealizedpremiumswhileavoidingselectionbiasfromanalyzingonlysolditems,wecombinedthe
pricing and purchase models through posterior predictive simulation, yielding sold-conditional expected prices
(Fig. 2C; see Methods for details). These simulated prices confirmed the reputation × signal type interaction
estimated above. The average marginal effect of reputation on the log price ratio was positive for self-graded
listings(AME= +0.074)andnegativeforTP-gradedlistings(AME= −0.071). Adescriptiveanalysisofsold
itemsalsocorroboratedthispattern(fig.S1;seetableS1andfig.S5fortheconvergencediagnosticsandmodel
fit,andMethodsforthesimulationprocedures).
We have shown that reputation interacts with signal type in two distinct ways. First, the reputation–value
4

Table1.Parametersofthetheoreticalmodel.
| Symbol Description |     |     | Value/Range |     |     |
| ------------------ | --- | --- | ----------- | --- | --- |
Modelparameters
| θ Productqualitytype                 |     |     | {H,L}          |     |     |
| ------------------------------------ | --- | --- | -------------- | --- | --- |
| s Seller’ssignalchoice               |     |     | {TP,Self,None} |     |     |
| pˆs Buyer’sposterior;P(θ=H|s,ρ)      |     |     | [0,1]          |     |     |
| π0 PriorP(θ=H)                       |     |     | 0.3            |     |     |
| ϕ Penaltycoefficientfordetectedfraud |     |     | 0.5            |     |     |
| cTP Costofthird-partyauthentication  |     |     | 0.2            |     |     |
Statevariables
| ρ Sellerreputation          |     |     | [0,1] |     |     |
| --------------------------- | --- | --- | ----- | --- | --- |
| V Itemvalue(VL=0normalized) |     |     | R +   |     |     |
space separates along a positively sloping boundary (Fig. 2B). Self-grading prevails at high reputation and low
value, whereas TP grading prevails at low reputation and high value. Second, reputation amplifies the price
premium of costless self-grading while lowering that of costly TP grading. In the following subsection, we
discussasignalinggamethataddressesthesepatterns.
Signaling model analysis
Modelsetup
We formulate a signaling game in which the seller privately observes product quality and chooses among the
| Naturedrawsaqualitytypeθ |     | ∈ {H,L}with | priorprobabilityP(θ | = H) = π |     |
| ------------------------ | --- | ----------- | ------------------- | -------- | --- |
threesignals(Fig.3). 0 . Tothe
buyer,ahigh-qualityitem(θ = H)hasavalueofV > 0,whilealow-qualityitem(θ = L)hasavalueofzero.
Forthesakeofsimplicity,weassumethatthepriorπ isindependentofV. Afterobservingθ,thesellerchooses
0
asignals ∈ {TP,Self,None}. Buyersobservebothsandtheseller’spublicreputationρ ∈ [0,1],acumulative
recordofpastfeedback, andformaposteriorbeliefpˆ s = P(θ = H | s,ρ)thattheitemishigh-quality. Under
thefixed-priceformat, inwhichthesellerpostsaprice, weassumethatbuyersacceptthelistedpriceifitdoes
notexceedtheitem’sexpectedvaluepˆ s V. Therefore,theequilibriumpriceforsignalsispˆ s V. Whentheseller
sendsnosignal(s = None),theposteriorreducestothepriorπ ,andtheequilibriumpriceisthebaselineπ V.
|     |     | 0   |     |     | 0   |
| --- | --- | --- | --- | --- | --- |
We characterize the perfect Bayesian equilibria (PBE) of the model and apply the D1 criterion (28–30) where
multipleequilibriaarise(seeMethodsfordetails).
Trustthroughself-claimandreputation
Considerfirsttheuseofself-grading. Thissignalisavailabletobothhigh-andlow-qualitysellersandrequires
noimmediatefinancialcosts. However,thesetwotypesfaceasymmetricconsequences. WhenanH-typeseller
self-grades, the claim is accurate and the seller’s reputation is unaffected. When an L-type seller self-grades,
the claim is dishonest and triggers buyers’ negative feedback after the transaction. This damages the seller’s
reputation,leadingtoafuturepayofflossofϕρ,whereϕ > 0scalesthelosswiththeseller’scurrentreputation
ρ.
Duetothisasymmetryintheconsequencesofself-grading, wecanderiveaconditionunderwhichH-type
sellers choose Self and L-type sellers choose None, with incentive-compatible strategies and Bayes-consistent
buyer beliefs (i.e., a separating PBE). The L-type seller’s expected payoff is π 0 V when choosing None and
V −ϕρwhenchoosingSelf. Therefore,theL-typesellerchoosesNoneaslongasπ V > V −ϕρ,whichcan
0
berearrangedto
ϕ
|     | V < | ρ≡V¯(ρ). |     |     | (1) |
| --- | --- | -------- | --- | --- | --- |
1−π
0
As the slope ϕ/(1 − π ) is strictly positive, V¯(ρ) is an increasing linear function of ρ, which appears as the
0
positivelyslopinglineinFig.4. TheblueregionbelowthislinecorrespondstotheSelf-separatingequilibrium.
Intuitively, thereputation-collateralboundV¯(ρ)measuresthemaximumvaluesustainablebyreputationalone.
Asellerwithahigherreputationhasmoretolosefrommisrepresentation,andself-gradingbecomescrediblefor
5

Nature
|     |         | 𝜋    |     | 1−𝜋  |      |     |
| --- | ------- | ---- | --- | ---- | ---- | --- |
|     |         | 0    |     | 0    |      |     |
|     | Seller  | 𝐻    |     |      | 𝐿    |     |
|     | TP Self | None |     | Self | None |     |
Buyer
𝐼Self 𝐼None
|     | 𝑝̂ TP=1 | 𝑝̂ Self 𝑝̂ None=𝜋0 |     | 𝑝̂ Self   | 𝑝̂ None=𝜋0 |     |
| --- | ------- | ------------------ | --- | --------- | ---------- | --- |
|     | 𝑉−𝑐     | 𝑝̂ 𝜋               | 𝑉   | 𝑝̂        | 𝜋 𝑉        |     |
|     | TP      | Self 𝑉             | 0   | Self 𝑉−𝜙𝜌 | 0          |     |
Fig.3. Extensive-formgametreeofthesellersignalingmodel. NatureassignssellertypeH (highquality)withprobabilityπ
0
or L (low quality) with probability 1−π 0 . H-type sellers choose among three signals: TP-graded (third-party certification at
costc TP ;buyers’posteriorpˆ TP = 1;theseller’spayoffisV −c TP ),Self-graded(nocost;reputationunaffected;buyers’posterior
pˆ ;payoffpˆ V),orNone(nocost;buyers’posteriorpˆ =π ;payoffπ V). L-typesellerschoosebetweenSelf-graded(no
| Self Self |     | None | 0   | 0   |     |     |
| --------- | --- | ---- | --- | --- | --- | --- |
cost;reputationaldamageϕρupondetection;payoffpˆ V −ϕρ)andNone(nocost;payoffπ V). Dashedcurvesdenotebuyer
|     |     | Self |     |     | 0   |     |
| --- | --- | ---- | --- | --- | --- | --- |
informationsets: I includesthetwoSelf-gradednodes,andI includesthetwoNonenodes(i.e.,basedonthesignalalone,
Self None
thebuyercannotdistinguishH fromL). TP-gradedisavailableonlytoH-typesellers,soitsnodestandsalone. Thetreeshows
| Stage1ofFig.1;theequilibriumpricepˆ | s V carriesStages2and3. |     |     |     |     |     |
| ----------------------------------- | ----------------------- | --- | --- | --- | --- | --- |
higher-value items. Reputation effectively sustains the credibility of the signal where institutional certification
wouldotherwisebeneeded.
Trustthroughinstitutionalcertification
V¯(ρ),
When the item value V exceeds the deception gain outweighs the reputation collateral, and self-grading
supportsatmostasemi-separatingoutcome. L-typesellersthenchooseSelfdishonestlywithpositiveprobability,
andaself-claimisonlypartiallycredible(seeMethods). Buyerscanstilltrustthird-partycertification. Because
L-type items cannot pass third-party authentication, observing TP perfectly identifies the item as high-quality,
and this credibility owes nothing to the seller’s reputation. The certifying institution charges a fixed cost c TP ,
whichisbornebyH-typesellers(seetextS7forvalue-dependentfees). FortheH-type,theTPpayoffmustbe
| atleasttheNonepayoff,V −c | TP ≥π 0 V,whichrequires |     |     |     |     |     |
| ------------------------- | ----------------------- | --- | --- | --- | --- | --- |
c
TP
|     |     | V ≥ | ≡V. |     |     | (2) |
| --- | --- | --- | --- | --- | --- | --- |
1−π
0
As c does not depend on ρ, this bound is the same at every reputation level. Reaching it makes certification
TP
viable, in the sense that a TP-separating equilibrium exists, but it does not yet make TP grading the H-type’s
preferred signal. Above V¯(ρ), a partially credible self-claim pays the H-type π V + ϕρ rather than π V,
|     |     |     |     |     | 0   | 0   |
| --- | --- | --- | --- | --- | --- | --- |
V¯(ρ)
and certification overtakes this payoff only when V − c > π V + ϕρ, equivalent to V > + V (see
TP 0
Methods for the equilibrium selection). This certification boundary is the reputation-collateral bound shifted
upward by V, so the two boundaries in Fig. 4 are parallel and enclose a band of vertical width V. Above the
certificationboundary,H-typesellerschooseTP,andL-typesellers,unabletopassauthentication,chooseNone.
Fullseparationisrestored,nowrestingonaninstitutionalex-antecostratherthanareputationalex-postpenalty.
Regimestructureandempiricalcorrespondence
Thetwoboundariespartitionthe(ρ,V)spaceintothreeregimes(Fig.4),eachcorrespondingtoadifferentway
ofproducingtrust. IntheSelfregime,reputationalonesustainshonestself-claims,andtheinstitutionisnotused.
6

1.0
TP regime
(institution-based)
me
0.5
𝑉̄(𝜌)+
m
𝑉
i-separating
regi
𝑉̄(𝜌)
Se
𝑉
Self regime
(reputation-based)
0.0
𝑉
𝑝̂ =0
Self
(off path)
𝑝̂ =1
Self
𝜌
0.0 0.2 0.4 0.6 0.8 1.0
𝜌
𝑉
Buyer belief P(H | Self)
0.3 (π₀) 1.0
Fig.4. Three-regimesortinginthereputation–valuespace. Themap(left)partitionsthe(ρ,V)space,whereρissellerreputation
andV isitemvalue,intothreeregimes,coloredcategorically. BelowthelowerboundaryV¯(ρ)(Eq.1)liestheSelfregime(blue),
inwhichself-gradingfullyseparatesthetypes.AbovetheupperboundaryV¯(ρ)+V liestheTPregime(red),inwhichtheH-type
prefersTPgrading.BetweenthetwoparallelboundariesliestheSemi-separatingregime(gray),abandofverticalwidthV (Eq.2).
TherightpanelshowsthesamespacewithitemvaluecutatV¯(1)+V,coloredbythebuyer’sbeliefinaself-claim,P(H |Self).
Thebeliefis1throughouttheSelfregimeandriseswithreputationasπ +ϕρ/V acrosstheSemi-separatingband. Abovethe
0
band,Selfisofftheequilibriumpathandisleftblank.Baselineparameters:π =0.3,ϕ=0.5,c =0.2.
0 TP
IntheSemi-separatingregime,reputationstillconstrainsself-claimsbutonlyinpart;self-claimsarediscounted,
and no signal fully separates the types. In the TP regime, the institution replaces reputation as the source of
credibility.
The theoretical regime structure generates a testable prediction. The certification boundary V¯(ρ) + V is
positively sloping in (ρ,V) space, as V¯(ρ) increases with reputation. This prediction matches the regime map
estimated from the HBM (Fig. 2B), in which the empirical boundary between Self-dominant and TP-dominant
5 40% 43% 34% 30% 15%
(8.1/20.2) (6.4/15.1) (4.3/12.7) (3.3/11.2) (1.8/12.2)
4 12% 11% 10% 8% 6%
(1.9/16.0) (1.7/15.0) (1.3/13.7) (1.1/13.2) (0.8/13.4)
3 6% 5% 4% 3% 4%
(0.8/13.7) (0.7/13.6) (0.6/15.1) (0.5/14.8) (0.6/14.1)
2 4% 3% 2% 2% 4%
(0.5/12.2) (0.4/13.0) (0.4/16.2) (0.3/14.8) (0.6/15.0)
1 2% 1% 1% 0% 1%
(0.2/9.2) (0.2/14.6) (0.1/13.6) (0.0/17.3) (0.1/16.7)
1 2 3 4 5
Reputation quintile
elitniuq
ecirp
tekram
dedargnU
P(TP | graded)
0% 10.3% (marginal) 43%
(← Self) (→ TP)
Fig. 5. Empirical TP-graded certification rates across reputation and market price. Discrete 5×5 heatmap of the third-party
certification ratio P(TP | graded), the share of TP-graded listings among all graded listings, across seller reputation quintiles
(columns, ρ) and ungraded market price quintiles (rows, V). Each cell reports the TP-graded proportion and the sample sizes
(n /n ,inthousands,roundedtothenearesthundred). ThedivergingcolorscaleiscenteredonthemarginalTPrate,withred
TP total
forabove(TP-dominant)andblueforbelow(Self-dominant).
7

signal choices exhibits a similar positive slope. This pattern is further corroborated by the discrete heatmap in
Fig.5,whichpartitionsthedataintoreputation–valuequintilecellsandshowstheTPshareamonggradedlistings
(seefig.S6forthemarginaldecompositionsalongeachaxis). Third-partygradingpeaksinthelow-reputation,
high-valuecorner,whileself-gradingescalatessharplyasreputationincreasesandvaluedecreases.
While the three regimes describe which signal sellers use, the pricing interaction in Fig. 2C arises within
the Semi-separating regime. In the Self regime, self-grading separates the types fully, so the buyer’s posterior
belief that a self-graded item is high-quality is pˆ = 1, independent of reputation (Fig. 4, right). In the
Self
Semi-separatingregime,low-qualitysellersmixbetweenadishonestself-claim(payoffpˆ V −ϕρ)andNone
Self
(payoff π V), and their indifference between the two pins this belief at pˆ = π + ϕρ/V (see Methods;
0 Self 0
text S7). The belief increases in reputation, ∂pˆ /∂ρ = ϕ/V > 0, because higher reputation partially deters
Self
misrepresentation. The right panel shows this increase across the band. Because the equilibrium price equals
pˆ V, the gradient accounts for the positive reputation × self-graded interaction. TP grading, by contrast,
Self
derives its credibility from an external institution rather than the seller, so pˆ = 1 for all ρ and ∂pˆ /∂ρ = 0,
TP TP
predicting no reputation × TP grading interaction (see Discussion for interpretations of the observed negative
interaction).
Taken together, the signaling model recovers the equilibrium structure underlying our empirical analysis,
reproducing the regime map (Fig. 2B) and the positive reputation × self-graded interaction (Fig. 2C) from a
singleasymmetryinsignalcosts.
Reputation dynamics
The regimes above take reputation as given. Because reputation is built by past trade, we next let it evolve,
and buyers form the posterior pˆ anew each period from it. Within each period, buyers and sellers play the
staticequilibriumoftheprecedingsectionatthecurrentreputation;acrossperiods,reputationchanges. Quality
is drawn per listing, so a share π of a seller’s listings is high quality. We assume that H-type trade raises
0
reputation and that L-type misrepresentation lowers it by the same amount, so a single rate α governs both
directionalchanges. Honesttradesofhigh-qualitycardsraisethereputationscoreattherateπ α.
0
Consider a seller for whom certification is unavailable, facing items of value V, so that self-grading is the
onlyqualitysignal. BecausetheL-typemixingprobabilityispinnedbytheindifferencecondition,thetwoforces
reduce to a single equation for how ρ changes (see Methods). The resulting equation has a single interior rest
pointthatisunstable(Fig.6A).Belowit, misrepresentationisfrequentenoughthatreputationfallstozeroand
staysthere,alow-trusttrap. Aboveit,misrepresentationisrareenoughthatreputationgrowsuntilself-grading
separatesthetypes. Thelong-runoutcomeisthereforesetbytheinitialreputationratherthanbytheparameters
alone. The rest point exists when high-quality listings are the minority, π < 1/2 (see Methods for the exact
0
condition).
Certificationenablesanescapefromthistrap(Fig.6B).WhentheitemvalueexceedsV¯(ρ)+V,TPgradingis
availabletoH-typesellersbutisnotaviableoptionforL-typesellers,whochooseNone,sonomisrepresentation
occurs. This matters most when the H-type’s reputation is low. TP grading allows low-reputation H-type
sellerstodistinguishthemselvesfromlow-reputationL-typesellers(comparetheleftsideofFig.6Bwiththatof
Fig.6A).Reputationthereforeaccumulatesatthefullrateπ αevenwhenitislow,coveringtherangeinwhich
0
reputation alone cannot sustain credible self-grading. Above the switching reputation at which self-grading
becomes the H-type’s preferred signal, misrepresentation resumes and the accumulation rate drops. Whether
that drop stalls reputation depends on the certification cost, and when that cost is small enough, reputation
accumulates at every level and no trap forms (Methods). Certification is thus not only a static substitute for
reputationinasingletransaction. Itcanalsobuildthereputationthatlatermakesself-claimscredible.
Discussion
Ouranalysesshowthatreputationandthird-partycertificationoperateascomplementarysourcesoftrust, each
grounded in a distinct form of costly signaling. Reputation amplifies the pricing benefit of self-grading, a self-
claimed cheap-talk signal, but not that of TP grading (Fig. 2C). The signaling game posits two mechanisms
8

A Reputationonly
𝑉=0.50 𝑉
𝜌
𝜋 𝛼
0
0
erosion
0 𝜌∗ 1
𝜌
𝜌̇
=)𝜌(𝑓
B Reputationandinstitution
𝑉=0.50 𝑉
𝜌
no low-trust trap
0 𝜌 1
𝑠
𝜌
Fig.6. Reputationdynamicsunderthetwotrustmechanisms. (A)Reputationonly. (B)Reputationandinstitution. Thetopstrip
locatesthesliceinthe(ρ,V)plane(blue,Self;gray,Semi-separating;red,TP).Certificationisunavailablein(A),sonoTPregime
arises;(B)reproducesthepartitionofFig.4. Belowitisthephaselinef(ρ)=ρ˙fortheseller’sreputation(seeMethods). Onthe
zeroline,anopencirclemarkstheunstablerestpoint,andarrowsgivethedirectionofmotion.Thefilledcircleatρ=0marksthe
absorbingboundary. Shadingmarkstheintervalonwhichreputationerodes. In(B)theaccumulationratefallsdiscontinuouslyat
thereputationρ atwhichH-typesellersswitchfromcertificationtoself-grading. Wherethesliceleavesthegraybandinthetop
s
strip,thefullrateisrestored.Baselineparameters:π =0.3,ϕ=0.5,c =0.2.BothpanelsaredrawnatV =0.50.
0 TP
that account for this pattern. Reputation collateral renders self-grading credible through the reputational cost
of misrepresentation. Institutional verification renders TP grading credible owing to an immediate monetary
cost of certification, which is independent of seller reputation. Thus, the two mechanisms share a common,
costly-signaling structure operating at different temporal stages. Reputation imposes an ex-post penalty for
misrepresentation, while certification imposes an ex-ante monetary cost (see 31, for this distinction in political
science). The two mechanisms partition the reputation–value space into three equilibrium regimes, matching
theempiricalregions(Fig.2B).Theseller’sreputationandtheitem’svalueendogenouslyandjointlydetermine
whichsourceoftrustresolvestheinformationasymmetry.
Substitution and complementarity of trust mechanisms
While the regime-level account captures a broad pattern of signal use, the empirical pricing interaction admits
a closer behavioral interpretation. In the model, TP credibility is independent of seller reputation, and a high
reputationrendersTPgradinginformationallyredundant. Bothimplicationspredictnoreputation×TPgrading
interaction. Thus, the observed reputation × TP grading interaction (Fig. 2C) cannot be fully captured by the
signalinggamemodelandwarrantscloserscrutiny. Weinterpretthisasastrategicpricingadjustmentbyhigh-
reputationsellers(seefigs.S2andS3forthefullanalysis). TheirTPlistingsshowdecliningconditionalpricing
margins (fig. S3B), which are offset by increasing sale probabilities (fig. S2B), leaving expected margin com-
parableacrossreputation(fig.S3D).Inotherwords,low-reputationTPsellerssellafewitemsathighmargins,
whilehigh-reputationTPsellerssellmanyatlowmargins. Priorresearchhasdocumentedasimilarsubstitution
betweenreputationandinstitutionalverification(32). EitherreputationorTPgradingaloneissufficienttosup-
port credibility and a price premium but at different price ranges, making the two functionally substitutable in
pricingterms.
Consistentwiththissubstitutionview,priortrusttheoryhasclassifiedmechanismsasinformalversusformal
and treated them as substitutes (10, 17, 20, 33). Our analysis replaces this dichotomy with three regimes of
trustproduction. Forlow-valueitems,reputationproducestrustonitsown;forhigh-valueitems,theinstitution
producesit;inbetween,reputationproducesitonlyinpart. Thetwoboundariesdifferinkind. Atthecertification
boundary,V¯(ρ)+V (Eqs.1and2),H-typesellersswitchfromaself-claimtocertification,soonemechanism
replaces the other. At the reputation-collateral bound, V¯(ρ), the self-claim is merely discounted, and the H-
typekeepsusingit. Substitutionisthereforeconfinedtoasingleboundary. Market-wide,thethreeregimesare
9

complements. Together they extend credible exchange across a wider range of sellers and items than any one
couldalone(34,35). Thus,complementarityiscoverageacrossregimes,notjointusewithinasingletransaction.
Thispartitionfollowsfromthequalitativeformofthetwocostmechanisms,notfromthespecificparameter
valuesassignedtothem. Thethreeregimesariseforanypositivereputationalpenaltyandcertificationcost,with
theparametersshiftingonlytheirboundaries(seetextsS6andS7forcomparativestatics). Therefore,thelogic
canextendbeyondtradingcardstoanyexchangethatpairsareputationalex-postpenaltywithaninstitutionalex-
antecost. Thepenaltyneednottaketheformofafeedbackscore. IntheMaghribitraders’coalition,itoperated
throughcollectiveostracism(21,22). Theex-antecost,inturn,neednottaketheformofaper-itemcertification
fee. Inthenineteenth-centuryUnitedStates,wheremigrationhaderodedreputation-basedtrust,ittooktheform
of professional credentials purchased from certifying institutions (20). Wherever quality is uncertain and these
twoformsofenforcementcoexist,thesamereputation–valuepartitionshouldgovernwhichmechanismsustains
trust.
The scalability of trust
The underlying mechanisms of self-grading and TP grading can be found in biological signaling research. TP
grading is associated with ex-ante cost asymmetry, which is the core idea of Zahavi’s (36) handicap principle.
Ex-post cost signaling has been documented in research on social insects and primates, showing that signals
carryinglittleornoproductioncostremainhonestwhenreceiversimposecostsondeceptivesignalers(37–39),
a mechanism in which honesty rests on the ex-post cost of cheating rather than on signal production cost (40–
42). Self-grading in our model parallels this logic, with the zero-cost signal becoming credible through the
reputationalpenaltyformisrepresentation. However,biologicalenforcementreliesondirectdyadicinteraction,
confiningthemechanismtosmallgroups. Onlinereputationsystemsovercomethisscalelimitationbyaggregat-
ingpastevaluationsintopublicscoresandconvertingdyadicenforcementintoinformationalinfrastructurethat
operatesacrossmillionsofanonymousparticipants. Thus,onlinereputationemergesasasocialtechnologythat
renderscheaptalkcredibleatscale,withdirectimplicationsforplatformdesign(43).
Wedrawseveraldirectimplicationsforplatformgovernance. Thereputation-collateralboundV¯(ρ)increases
withthepenaltycoefficientϕ,aparameterthatplatformscontrolthroughmonitoringintensity,feedbackprotec-
tion, and negative feedback visibility (44, 45). A stronger ϕ expands the Self regime (Fig. 4), enabling more
sellerstoestablishcredibilitythroughreputationalone. eBay’spersistentpublicscoresandfeedbackprotection
guarantees exemplify such an investment, supporting the wide Self regime observed in our data. Even when
platform investment in ϕ is high, reputation collateral has structural limits. The dynamic analysis in Results
suggests that, without certification, sellers with a thin feedback record cannot cross the threshold above which
reputationcangrowtowardcredibility,soareputationsystemleavesabarriertoentry. However,TPgradingcan
openanescapepath,alongwhichsellersmovefromcertificationtoreputation-basedcredibility. Thisalignswith
priorevidencethatqualitycertificationismostvaluableforsellerswholackanestablishedreputation(46,47).
The model therefore implies a developmental view of trust, and understanding both mechanisms is central to
effectiveplatformgovernance.
Limitations and future directions
Our findings should be interpreted in light of several limitations. First, the design is cross-sectional. It limits
causal identification, particularly for the channels underlying the negative reputation × TP grading interaction
discussedabove; disentanglingthemwouldrequireexogenousvariationinsignalavailability. Italsoleavesthe
reputation dynamics untested. The low-trust trap and the escape path provided by certification remain impli-
cations of the model, and tracing them would require longitudinal records of individual sellers. Second, the
empiricalsettingisasinglecollectiblesmarketwithamatureTPgradinginfrastructure. Whetherthesamecom-
plementarity pattern holds in markets with different cost structures, such as the eBay Motors used-car market
inwhichvoluntarysellerdisclosurefunctionsintheabsenceofacomparableTPgradingservice(27), remains
anopenquestion. Finally,thesamplecoversonlytheUSmarket. Cross-culturalcomparisonoffersapromising
directionforfuturework,particularlybetweentheUSandJapaneseonlinemarkets. Inthesemarkets,thestruc-
10

tural contrast between institutional enforcement and reputation-based assurance (18) echoes the private–public
orderdistinction(19,21,22,48)andmayyielddistinctequilibriumconfigurations.
Materials and Methods
Data and variables
Weanalyzedfixed-price(BuyItNow)listingsofPokémontradingcardsontheeBayUSmarketplace,collected
via the eBay API between June 1 and December 15, 2025. Although listings were restricted to the US mar-
ketplaceonthebuyerside, sellersparticipatedinternationally: 59.1%oflistingsfromtheUnitedStates, 20.3%
fromJapan, andtheremaining20.6%from67countries. Eachlistedpricewasmatchedtoanexternalmarket
reference price from the PriceCharting REST API (https://www.pricecharting.com/), a publicly avail-
able price-tracking service for the trading card market, and the log price ratio was computed as the log of the
listed-to-market price ratio. After removing outliers from the distribution of log price ratios using the interquar-
tile range method (text S2), the final sample comprised N = 960,029 listings from 60,386 unique sellers. This
studywasapprovedbytheethicscommitteeoftheGraduateSchoolofHumanitiesandSociology,Universityof
Tokyo(UTSP-25004, May21, 2025). Asthestudyusedonlypubliclyavailablemarketplacedatawithnodirect
interactionwithhumanparticipants,informedconsentwasnotrequired.
Theanalysesinvolvedthreesetsofvariables: anoutcomemeasure,signalcategories,andsellerreputation.
(i) The outcome variable is the log price ratio log(P /V ), where P is the observed listing price and V is the
i i i i
marketreferencepricefromPriceCharting. ForTP-gradeditems,thegrade-specificmarketpricewasusedasV ,
i
sothattheratiocapturespricingrelativetothemarketpriceofanitemwithspecificgrading. Asthemarketprice
fluctuates from day to day, we used the marketprice on the date of sale for sold items. Forunsold listings, we
usedthemostrecentavailablemarketpriceatdatacollectionasanapproximationofthemarketpriceduringthe
listingwindowtoensurethattheratioreflectedthecurrentmarketcondition. ForJapanese-languagecards,we
usedaseparatesetofmarketpricesinPriceChartingtoaccountforlanguage-specificmarketconditions. (ii)We
distinguishedbetweenthreesignalingstrategies: TPgrading,self-grading,andnoneofthese. ItemsintheTP-
gradedcategory(3.8%ofthelistings)wereauthenticatedandgradedbytheProfessionalSportsAuthenticator
(PSA), which assigns grades on a 10-point scale from PSA 1 (Poor) to PSA 10 (Gem Mint), at a per-card
fee paid by the seller. As cards graded below PSA 7 rarely circulate in the secondary market, we restricted
the TP-graded category to listings displaying PSA 7 (Near Mint) or higher as a proxy for high-grade certified
items. For the cards in the self-graded category (33.3% of the listings), sellers attached condition descriptors
(e.g., “gem mint,” “near mint”) to the items at no cost without obtaining PSA certification. These listings were
identified through hierarchical regular-expression matching (see text S2 for the classification algorithm). The
remaining listings were associated with no quality signal (None; 62.9% of the listings). (iii) We constructed a
sellerreputationscorefromtwoeBayfeedbackmetrics: thepositivefeedbackpercentage(theshareofratings
that are positive) and the feedback score (net count of positive minus negative ratings). The percentage was
logit-transformedandthescorewaslog-transformed(log(score+1));bothwerestandardizedbeforethePCA.
Thefirstprincipalcomponent(78.5%ofthevariance)servedasthereputationscore. Additionalcontrolvariables
included a Japanese-card indicator, a return-acceptance policy, and listing duration. Throughout the analyses,
logdenotesthenaturallogarithm.
Hierarchical Bayesian model
We specified a hierarchical Bayesian model with three simultaneous equations: a multinomial logit for signal
selection(TP-graded,self-graded,orNone,withNoneasthereferencecategory),anormallinearequationfor
the log price ratio, and a Bernoulli logit for purchase outcomes. Correlated seller-level random effects linked
thethreeequations. Inthesignal-selectionequation,itemvaluewasoperationalizedasthelogoftheungraded
reference price for all listings, including TP-graded items, on the assumption that the ungraded price serves
as an exogenous factor in the signal choice. The equation also includes a reputation × item value interaction.
Weincludedadditionalcovariatesselectively,namelytheJapanese-cardindicatorinallthreeequations,return-
acceptancepolicyinthepricingandpurchaseequations,andloglistingdurationinthepurchaseequationonly.
We fitted the model in Stan using the No-U-Turn Sampler with eight chains, each run for 1,000 post-warmup
11

iterations and thinned by a factor of two, for a total of 4,000 posterior draws (see texts S3 and S4 for the
completespecificationandtableS1forconvergencediagnostics).
Asonly13.7%ofthelistingsresultedinasale,theobservedtransactionpricesweresubjecttoselectionbias.
To address this, we used the posterior draws from the Stan estimation to compute sold-conditional expected
prices through posterior predictive simulation. For each signal type k and reputation score, we integrated the
predicted prices over the empirical covariate distribution, yielding E[price | rep,cert = k,sold = 1]. We drew
100,000 covariate vectors from the empirical distribution and combined them with 4,000 posterior draws, for a
totalof4×108 simulationspersignaltype. WecomputedtheAMEsofreputationasthenumericalderivatives
ofthesepredictionswithrespecttothereputationscore,averagedovertheempiricaldistributionofreputation.
Signaling game
We formulate a signaling game that formalizes how the two trust mechanisms interact. A seller privately ob-
servesproductqualityθ ∈ {H,L},whereP(θ = H) = π ,andchoosesasignals ∈ {TP,Self,None}. Buyers
0
observesandtheseller’spubliclyavailablereputationρ∈[0,1](correspondingtothereputationcompositede-
finedabove),andformaposteriorbeliefpˆ =P(H |s,ρ). Weassumedthatbuyerswereriskneutralandwilling
s
to pay up to their expected value of the item. Under the fixed-price format, the seller posts a take-it-or-leave-it
price,andabuyerpurchasestheitemwheneverthepostedpricedoesnotexceedthebuyer’sexpectedvalue.
Empirically,listingpricesskewtowardhighpricepremiums,whilesoldpricesconcentratenearthemarketprice
(Fig. 1B), consistent with this posted-price structure. The seller therefore posts the highest price a buyer will
accept, so the equilibrium price for signal s is pˆ V, where V > 0 is the full-information value of a high-quality
s
item(alow-qualityitemhasvaluezero). ThesignalNoneistreatedaschoosingthethirdoption,namelylisting
an item without claiming any quality. It trades at the exogenous outside-option price π V, independent of the
0
seller’s signal choice (see text S5 for the formal statement). Formally, the signaling cost c(s,θ,ρ) takes the
followingvaluesacrosssellertypesandsignals:

 c
+
T
∞
P i
i
f
f
s
s
=
=
T
T
P
P
,
,
θ
θ
=
=
H
L
c(s,θ,ρ)= 0 ifs=Self, θ=H

ϕ
0
ρ
i
i
f
f
s
s=
=N
Se
o
l
n
f,
e
θ=L
where c > 0 is the certification cost (ex-ante cost) and ϕ > 0 is the penalty coefficient, which determines
TP
the penalty for dishonest self-grading, ϕρ, the reputational cost. This is an ex-post cost because dishonest
self-grading, once detected, triggers negative feedback, reducing the seller’s reputation and diminishing future
payoffs. Therefore,sellerswithgreaterreputationalcapitalfaceastrongerdeterrent. Thekeyasymmetryisthat
L-typesellerscannotobtainthird-partycertification(c=+∞),whiletheirself-gradingcostscaleswithreputation
rather than with V. The solution concept is the PBE. Each seller maximizes the expected payoff given beliefs,
andbeliefsontheequilibriumpathsatisfyBayes’rule. WhenmultiplePBEarise,weselectamongthemwiththe
D1criterion(28–30).
We consider two candidate separating equilibria. In the Self-separating equilibrium, H-type sellers choose
Self and L-type sellers choose None. Bayes’ rule gives the on-path beliefs pˆ = 1 and pˆ = π , and the
Self None 0
profileisaPBEifandonlyifV ≤V¯(ρ),thereputation-collateralbound(Eq.1). IntheTP-separatingequilibrium,
H-typesellerschooseTPandL-typesellerschooseNone. BecauseL-typesellerscannotobtaincertification,
Bayes’ rule gives pˆ = 1, and the profile is a PBE if and only if the TP payoff V −c is at least the None
TP TP
payoffπ V,equivalenttoV ≥V (Eq.2). ForV >V¯(ρ),theSelf-separatingequilibriumdoesnotexist,andthe
0
remaining candidates are the TP-separating equilibrium and a semi-separating profile in which H-type sellers
chooseSelfwhileL-typesellersmixbetweenSelfandNone. Nootherprofile,includingpoolingonNone,isan
equilibriumunderD1(textS7).
In the TP-separating equilibrium, Self is off the equilibrium path, Bayes’ rule does not determine the belief
pˆoff , and multiple PBE arise. For each type, the set of beliefs under which a deviation to Self improves on the
Self
equilibrium payoff is an interval with upper endpoint one whenever it is nonempty, because signaling costs do
notdependonthebuyer’sposteriorandbothdeviationpayoffsincreaseinthebeliefwiththecommonslopeV.
Theintervalsbeginatp¯ =1−c /V fortheH-typeandp¯ =π +ϕρ/V fortheL-type,sotheD1comparison
H TP L 0
reduces to the ordering of the two thresholds (text S7). When p¯ > p¯ , the criterion sets pˆoff = 1. When
L H Self
12

p¯ > p¯ , itsetspˆoff = 0. ThethresholdsareequalatV = (c +ϕρ)/(1−π ) = V¯(ρ)+V, thecertification
| H L | Self |     | TP  | 0   |     |
| --- | ---- | --- | --- | --- | --- |
boundary. Becausep¯ increasesinV whilep¯ decreases,p¯ >p¯ holdsexactlyforV belowthisboundary.
|     | H   | L   | L H |     |     |
| --- | --- | --- | --- | --- | --- |
Under the assigned beliefs, the TP-separating equilibrium survives only above the certification boundary.
Belowit,thebeliefpˆoff =1makesthedeviationtoSelfprofitablefortheH-type. Inthesemi-separatingprofile,
Self
theL-type’sindifferencebetweenSelfandNone,pˆ V−ϕρ=π V,pinstheon-pathbeliefatpˆ =π +ϕρ/V,
|     |     | Self | 0   |     | Self 0 |
| --- | --- | ---- | --- | --- | ------ |
V¯(ρ),
which lies strictly below one for V > so a self-claim is only partially credible. This profile exists exactly
| forV¯(ρ)≤V | ≤V¯(ρ)+V. |     |     | <V¯(ρ),semi-separatingbetween |     |
| ---------- | --------- | --- | --- | ----------------------------- | --- |
TheequilibriumisthereforeSelf-separatingforV
the two boundaries, and TP-separating above the certification boundary, and it is unique off the boundaries
(textS7). Thetwoparallelboundariespartitionthe(ρ,V)spaceintotheSelf,Semi-separating,andTPregimes
describedinResults(Fig.4). Thebaselineparametervaluesareπ 0 =0.3,ϕ=0.5,andc TP =0.2(Table1and
textS9;seetextS6forcomparativestatics).
| Reputation | dynamics |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- |
Considerasellerforwhomcertificationisunavailable,sothatSelfandNonearetheonlysignals. Thecertifica-
tionboundarycomesfromtheH-typedeviationtoTP,soforthissellerthesemi-separatingequilibriumholdsat
>V¯(ρ).
everyV Inthatequilibrium,H-typesellerschooseSelf,andL-typesellerschooseSelfwiththeproba-
bilityσ (ρ)thatkeepsthemindifferentbetweenSelfandNone. Substitutingtheon-pathbeliefpˆ =π +ϕρ/V
| L   |     |     |     |     | Self 0 |
| --- | --- | --- | --- | --- | ------ |
intoBayes’rulegives
|     |     | π (1−π | −ϕρ/V) |     |     |
| --- | --- | ------ | ------ | --- | --- |
|     | σ   | (ρ)= 0 | 0 .    |     |     |
L
|     |     | (1−π 0 | )(π 0 +ϕρ/V) |     |     |
| --- | --- | ------ | ------------ | --- | --- |
FixingtheitemvalueV leavesasingleequationforρ. TradeontheH-typeshareπ oftheseller’slistings
0
raises reputation. On the remaining share, misrepresentation occurs with probability σ (ρ) and lowers it by
L
the same amount, while listings that carry no claim leave it unchanged, so a single rate α > 0 governs both
| directions. | Thelawofmotionistherefore |               |          |     |     |
| ----------- | ------------------------- | ------------- | -------- | --- | --- |
|             |                           | ρ˙ =α[π −(1−π | )σ (ρ)]. |     |     |
|             |                           | 0             | 0 L      |     |     |
Thelawofmotionhasatmostoneinteriorrestpoint,ρ∗ =V(1/2−π )/ϕ,andthatrestpointisunstable(see
0
textS8forthederivationandthestabilityanalysis). Itisinteriorwhenhigh-qualitylistingsaretheminority,π 0 <
1/2,andwhenV(1/2−π )<ϕ. Atthebaselinevaluesthesecondconditionisslack,sotheminoritycondition
0
alone decides whether the rest point exists. Absent certification, reputation starting below ρ∗ is absorbed at
ρ=0.
Withcertificationavailable,theH-typechoosesTPbelowtheswitchingreputationρ s =[(1−π 0 )V −c TP ]/ϕ,
which is interior exactly for V < V < (ϕ+c )/(1−π ), and below it reputation grows at the full rate π α. At
TP 0 0
ρ misrepresentationresumesandtheaccumulationratefalls. Whetherthatdropstallsreputationturnsonlyon
s
thesignofV −2c TP (textS8). WhenV > 2c TP reputationaccumulatesateverylevelandnotrapforms. When
V <2c therestpointliesabovetheswitch. Reputationbelowρ∗thenconvergesonρ fromeitherside,sothe
| TP  |     |     |     | s   |     |
| --- | --- | --- | --- | --- | --- |
trapistheswitchitselfratherthanarestpointofthelawofmotion. Reputationaboveρ∗ recoversthefullrate.
References
[1] JamesS.Coleman. FoundationsofSocialTheory. HarvardUniversityPress,Cambridge,MA,1990.
[2] GeorgeA.Akerlof. Themarketfor“lemons”: Qualityuncertaintyandthemarketmechanism. Quarterly
| JournalofEconomics,84(3):488–500,1970. |     | doi: 10.2307/1879431. |     |     |     |
| -------------------------------------- | --- | --------------------- | --- | --- | --- |
[3] eBay Inc. Annual report on Form 10-K (fiscal year 2025). Filed with the U.S. Securities and Exchange
Commission, 2026. Accession No. 0001065088-26-000027. https://www.sec.gov/Archives/
edgar/data/1065088/000106508826000027/0001065088-26-000027-index.htm.
[4] RobertAxelrod. TheEvolutionofCooperation. BasicBooks,NewYork,1984.
[5] Vili Lehdonvirta. Cloud Empires: How Digital Platforms Are Overtaking the State and How We Can
RegainControl. MITPress,Cambridge,MA,2022. doi: 10.7551/mitpress/14219.001.0001.
13

[6] PaulResnick,RichardZeckhauser,JohnSwanson,andKateLockwood. ThevalueofreputationoneBay:
Acontrolledexperiment. ExperimentalEconomics,9(2):79–101,2006. doi: 10.1007/s10683-006-4309-2.
[7] LuísCabralandAliHortaçsu.Thedynamicsofsellerreputation:EvidencefromeBay.JournalofIndustrial
Economics,58(1):54–78,2010. doi: 10.1111/j.1467-6451.2010.00405.x.
[8] Birger Wernerfelt. Umbrella branding as a signal of new product quality: An example of signalling by
postingabond. TheRANDJournalofEconomics,19(3):458–466,1988. doi: 10.2307/2555667.
[9] PaulResnickandRichardZeckhauser. TrustamongstrangersinInternettransactions: Empiricalanalysis
ofeBay’sreputationsystem. InMichaelR.Baye,editor,TheEconomicsoftheInternetandE-Commerce,
volume11ofAdvancesinAppliedMicroeconomics,pages127–157.ElsevierScience,Amsterdam,2002.
doi: 10.1016/S0278-0984(02)11030-3.
[10] Karen S. Cook, Chris Snijders, Vincent Buskens, and Coye Cheshire, editors. eTrust: Forming Relation-
shipsintheOnlineWorld. RussellSageFoundation,NewYork,2009.
[11] DouglassC.North. Institutions,InstitutionalChangeandEconomicPerformance. CambridgeUniversity
Press,Cambridge,1990. doi: 10.1017/CBO9780511808678.
[12] OliverE.Williamson. TheEconomicInstitutionsofCapitalism. FreePress,NewYork,1985.
[13] Michael Spence. Job market signaling. Quarterly Journal of Economics, 87(3):355–374, 1973. doi:
10.2307/1882010.
[14] Paul Milgrom and John Roberts. Price and advertising signals of product quality. Journal of Political
Economy,94(4):796–821,1986. doi: 10.1086/261408.
[15] DavidDranoveandGingerZheJin. Qualitydisclosureandcertification: Theoryandpractice. Journalof
EconomicLiterature,48(4):935–963,2010. doi: 10.1257/jel.48.4.935.
[16] RobertWilson. Auditing: Perspectivesfrommulti-persondecisiontheory. TheAccountingReview,58(2):
305–318,1983. doi: 10.2308/tar-4482714.
[17] KarenS.Cook,RussellHardin,andMargaretLevi. CooperationWithoutTrust? RussellSageFoundation,
NewYork,2005.
[18] Toshio Yamagishi. Trust: The Evolutionary Game of Mind and Society. Springer, Tokyo, 2011. doi:
10.1007/978-4-431-53936-0. OriginallypublishedinJapanese,UniversityofTokyoPress,1998.
[19] AvnerGreif,JoelMokyr,andGuidoTabellini. TwoPathstoProsperity: CultureandInstitutionsinEurope
andChina,1000–2000. PrincetonUniversityPress,Princeton,NJ,2025. ISBN9780691265940.
[20] LynneG.Zucker. Productionoftrust: Institutionalsourcesofeconomicstructure,1840–1920. Researchin
OrganizationalBehavior,8:53–111,1986.
[21] AvnerGreif. Contractenforceabilityandeconomicinstitutionsinearlytrade: TheMaghribitraders’coali-
tion. AmericanEconomicReview,83(3):525–548,1993.
[22] Avner Greif. Cultural beliefs and the organization of society: A historical and theoretical reflection on
collectivistandindividualistsocieties. JournalofPoliticalEconomy,102(5):912–950,1994. doi: 10.1086/
261959.
[23] Paul A. Pavlou and David Gefen. Building effective online marketplaces with institution-based trust. In-
formationSystemsResearch,15(1):37–59,2004. doi: 10.1287/isre.1040.0015.
[24] GingerZheJinandAndrewKato. Price,quality,andreputation: Evidencefromanonlinefieldexperiment.
RANDJournalofEconomics,37(4):983–1005,2006. doi: 10.1111/j.1756-2171.2006.tb00067.x.
14

[25] VincentP.CrawfordandJoelSobel. Strategicinformationtransmission. Econometrica,50(6):1431–1451,
1982. doi: 10.2307/1913390.
[26] Dina Mayzlin, Yaniv Dover, and Judith Chevalier. Promotional reviews: An empirical investigation of
onlinereviewmanipulation. AmericanEconomicReview,104(8):2421–2455,2014. doi: 10.1257/aer.104.
8.2421.
[27] GregoryLewis. Asymmetricinformation,adverseselectionandonlinedisclosure: ThecaseofeBayMo-
tors. AmericanEconomicReview,101(4):1535–1546,2011. doi: 10.1257/aer.101.4.1535.
[28] In-KooChoandDavidM.Kreps. Signalinggamesandstableequilibria. QuarterlyJournalofEconomics,
102(2):179–221,1987. doi: 10.2307/1885060.
[29] JeffreyS.BanksandJoelSobel. Equilibriumselectioninsignalinggames. Econometrica,55(3):647–661,
1987. doi: 10.2307/1913604.
[30] In-Koo Cho and Joel Sobel. Strategic stability and uniqueness in signaling games. Journal of Economic
Theory,50(2):381–413,1990. doi: 10.1016/0022-0531(90)90009-9.
[31] KaiQuek. Fourcostlysignalingmechanisms. AmericanPoliticalScienceReview,115(2):537–549,2021.
doi: 10.1017/S0003055420001094.
[32] Xiang Hui, Maryam Saeedi, Zeqian Shen, and Neel Sundaresan. Reputation and regulations: Evidence
fromeBay. ManagementScience,62(12):3604–3616,2016. doi: 10.1287/mnsc.2015.2323.
[33] PeterKollock. Theproductionoftrustinonlinemarkets. InEdwardJ.Lawler,MichaelMacy,ShaneThye,
andHenryWalker,editors,AdvancesinGroupProcesses,volume16,pages99–123.JAIPress,Greenwich,
CT,1999.
[34] Ginger Zhe Jin and Phillip Leslie. Reputational incentives for restaurant hygiene. American Economic
Journal: Microeconomics,1(1):237–267,2009. doi: 10.1257/mic.1.1.237.
[35] JieBai. Melonsaslemons: Asymmetricinformation, consumerlearningandsellerreputation. Reviewof
EconomicStudies,92(6):3574–3610,2025. doi: 10.1093/restud/rdaf006.
[36] Amotz Zahavi. Mate selection—a selection for a handicap. J Theor Biol, 53(1):205–214, 1975. doi:
10.1016/0022-5193(75)90111-3.
[37] ElizabethA.TibbettsandJamesDale. Asociallyenforcedsignalofqualityinapaperwasp. Nature,432
(7014):218–222,2004. doi: 10.1038/nature02949.
[38] JoanB.Silk,ElizabethKaldor,andRobertBoyd. Cheaptalkwheninterestsconflict. AnimBehav,59(2):
423–432,2000. doi: 10.1006/anbe.1999.1312.
[39] Elizabeth A. Tibbetts and Amanda Izzo. Social punishment of dishonest signalers caused by mismatch
betweensignalandbehavior. CurrBiol,20(18):1637–1640,2010. doi: 10.1016/j.cub.2010.07.042.
[40] Peter L. Hurd. Communication in discrete action-response games. J Theor Biol, 174(2):217–222, 1995.
doi: 10.1006/jtbi.1995.0093.
[41] Michael Lachmann, Szabolcs Számadó, and Carl T. Bergstrom. Cost and conflict in animal signals and
humanlanguage. ProcNatlAcadSciUSA,98(23):13189–13194,2001. doi: 10.1073/pnas.231216498.
[42] SzabolcsSzámadó. Thecostofhonestyandthefallacyofthehandicapprinciple. AnimBehav,81(1):3–10,
2011. doi: 10.1016/j.anbehav.2010.08.022.
[43] Ofer Tchernichovski, Lucas C. Parra, Daniel Fimiarz, Arnon Lotem, and Dalton Conley. Crowd wisdom
enhanced by costly signaling in a virtual rating system. Proc Natl Acad Sci U S A, 116(15):7256–7265,
2019. doi: 10.1073/pnas.1817392116.
15

[44] StevenTadelis.Reputationandfeedbacksystemsinonlineplatformmarkets.AnnualReviewofEconomics,
8(1):321–340,2016. doi: 10.1146/annurev-economics-080315-015325.
[45] GaryBolton,BenGreiner,andAxelOckenfels. Engineeringtrust: Reciprocityintheproductionofrepu-
tationinformation. ManagementScience,59(2):265–285,2013. doi: 10.1287/mnsc.1120.1609.
[46] DanielW.Elfenbein, RaymondFisman, andBrianMcManus. Marketstructure, reputation, andthevalue
ofqualitycertification. AmericanEconomicJournal: Microeconomics,7(4):83–108,2015. doi: 10.1257/
mic.20130182.
[47] MichaëlDewallyandLouisEderington. Reputation,certification,warranties,andinformationasremedies
for seller-buyer information asymmetries: Lessons from the online comic book market. The Journal of
Business,79(2):693–729,2006. doi: 10.1086/499169.
[48] Avner Greif and Guido Tabellini. The clan and the corporation: Sustaining cooperation in China and
Europe. JournalofComparativeEconomics,45(1):1–35,2017. doi: 10.1016/j.jce.2016.12.003.
Acknowledgments
WethankHirokazuHattaforvaluablediscussionsandadvicethroughoutthisproject. WethankKiyoshiIzumi
andthemembersofhislaboratoryfortheirhelpfulcomments. Wealsothanktheparticipantsinourlaboratory
seminar for their feedback. We thank Scribendi (https://www.scribendi.com/) for English-language
editing.
Funding: This work was supported by a Grant-in-Aid for JSPS Fellows (JSPS KAKENHI Grant Number
JP25KJ0080 to Y.K.) and a Grant-in-Aid for Transformative Research Areas (A) (MEXT KAKENHI Grant
Number24H02200toY.O.).
Authorcontributions: Y.K.andY.O.designedresearch;Y.K.performedresearchandanalyzeddata;andY.K.
andY.O.wrotethepaper.
Competinginterests: Theauthorsdeclarethattheyhavenocompetinginterests.
Data and materials availability: The processed data and all analysis code needed to reproduce the figures
are available at the Open Science Framework (https://doi.org/10.17605/OSF.IO/6HJFK). Raw
listing data were obtained from the eBay API and raw market-price data from the PriceCharting API; under
the respective platform terms of service, the authors are not permitted to redistribute these raw data. A full
descriptionofthedata-collectionprocedureisprovidedintextS1,toenableindependentre-collection.
16

Supplementary Materials
OrganizationoftheseSupplementaryMaterials:
1. SupplementaryText(pp.18–29)—EmpiricalMethods(S1toS4)coversthedatapipeline,variablecon-
struction, the full HBM specification, and MCMC sampling. Theoretical Model (S5 to S9) covers the
model assumptions, the Self-separating, semi-separating, and TP-separating equilibrium derivations with
D1refinement,andanumericalillustration.
2. SupplementaryResults(pp.30–37)—Descriptivepriceanalysis(fig.S1),sellervolume(fig.S2),revenue
andmarginanalysis(fig.S3),thecontinuousregimeboundaryinreputation–valuespace(fig.S4),MCMC
convergence diagnostics (table S1), model fit (fig. S5), full coefficient estimates (table S2), and signal
composition(fig.S6).
17

Supplementary Text
A Empirical Methods
A.1 Data Pipeline
Transaction data were collected daily from the eBay US marketplace using the Browse API (v1). Market ref-
erence prices were obtained daily from the PriceCharting REST API, which supplies historical card prices by
grade. ThesetwosourceswerecombinedtocomputethepricepremiumvariabledefinedinA.2.
Collectionspanned198days(June1–December15,2025)andwasrestrictedtothePokémontradingcard
category. AlltransactionswerefilteredtotheUSmarketplaceonthebuyerside,ensuringconsistencyinshipping
costs and transaction conditions. Sellers participated internationally, spanning 69 countries: the United States
accountedfor59.1%oftransactions,Japanfor20.3%,Canadafor6.7%,theUnitedKingdomfor6.2%,Australia
for4.4%,Francefor1.6%,and63additionalcountriesforacombined1.7%.
Rawtransactionswereprocessedthroughapipelinethatextractscardmetadatafromlistingtitlesandmatches
each listing to PriceCharting market prices via a hierarchical algorithm keyed on card name, number, set, and
grade.
A.2 Variable Construction
A.2.1 Pricepremium
The price premium is operationalized as the log ratio of the observed transaction price to the market reference
price:
p =log(P /V ) (S1)
(cid:101)i i i
whereP istheobservedpriceinUSDandV isthePriceChartingmarketreferencepriceforthecorrespond-
i i
ingcard-gradecombination. Forsolditems,V isthemarketpriceatthedateofsale;forlisted(unsold)items,V
i i
is the most recent market price. The log form yields a symmetric distribution centered near zero, with positive
valuesindicatingapremiumoverthemarketreferenceandnegativevaluesindicatingadiscount.
Outlierswereidentifiedusingtheinterquartilerange(IQR)methodappliedtothelogpriceratiodistribution,
excludingobservationsbelowQ −1.5×IQRoraboveQ +1.5×IQR. ThisstandardTukeymethodexcluded
1 3
23,421 observations (2.3%), reducing the sample from 1,018,321 to 994,900. Restriction to complete cases
producedtheanalysissampleofN =960,029.
A.2.2 Sellerreputationscore
eBay provides two seller reputation metrics: the Feedback Score (positive ratings minus negative ratings, cu-
mulativeovertheseller’stransactionhistory)andthePositiveFeedbackPercentage(positiveratingsdividedby
totalratingsoverthepreceding12months,range0–100%). Weconstructedacompositereputationscoreusing
principalcomponentanalysis(PCA):(i)item-leveldatawereaggregatedtoseller-levelmeansforthefeedback
percentageandthefeedbackscore;(ii)logitandlogtransformationswereappliedtoaddressceilingeffectsand
skewness,respectively;(iii)z-scorestandardizationwasapplied,andthefirstprincipalcomponentwasextracted
asthecompositereputationscore.
TheresultingPCAcompositeexplained78.5%ofthevariance,yieldingafinaldistributionwithM =0.013
andSD = 1.188intheanalysissample(N = 60,386). Thetwoinputmetricsdifferedindistribution: the
sellers
PositiveFeedbackPercentageaveraged86.3%(SD =33.6%);theFeedbackScorerangedfrom−3to672,427,
withthe23sellers(0.04%)holdingnegativescoressettozerobeforethelogtransform,andexhibitedabimodal
distributiononthelogscale.
18

A.2.3 Certificationcategory
Sellers choose among three certification strategies: None (no quality signal; 62.9% of listings), Self-graded
(self-claimedconditiondescription;33.3%),andTP-graded(third-partycertification;3.8%).
This study focuses on cards certified by Professional Sports Authenticator (PSA), the largest third-party
(TP)gradingserviceforPokémontradingcardsbytransactionvolume. Self-gradeditemsareungradedlistings
whose titles contain condition descriptors equivalent to PSA grade levels. PSA grades in the analysis sample
comprise10(GemMint: virtuallyflawlesscardwithperfectcentering),9(Mint: minorimperfectionuponclose
inspection), 8 (Near Mint–Mint: slight wear visible on surface or edges), and 7 (Near Mint: visible surface or
edgewear). Thecriteriaforcentering,surfacecondition,andcornersharpnessbecomestricterathighergrades.
Detection uses a hierarchical regular-expression matching algorithm that processes tokens from most specific
to most general. For example, “Gem Mint” is matched before “Mint” using negative lookahead to prevent the
broadertermfromcapturingthemorespecificdescriptor.
A.2.4 Controlvariables
The model specification includes three control variables: (i) a binary indicator for Japanese-language cards
(36.5%); (ii) a binary indicator for whether returns are accepted (48.8%); and (iii) the number of days since
listing creation (M = 258.6, SD = 355.2). These variables control for card-level heterogeneity, seller listing
behavior,anddurationeffectsonunsoldlistings.
| A.3 Full HBM | Specification |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- |
ThehierarchicalBayesianmodel,fittedtotheanalysissampleconstructedinA.2,comprisesthreesimultaneously
estimated equations with correlated seller-level random effects. The signal selection equation (Eqs. S2–S3)
modelscertificationchoice(None,Self-graded,TP-graded)asamultinomiallogit. Thepriceequation(Eqs.S4–
S5) models the log price ratio as normal. The sold equation (Eqs. S6–S7) models the binary sale outcome as
Bernoulli with a logit link. Simultaneous estimation with correlated random effects (Eq. S8) accounts for the
seller’sendogenouschoiceofsignalandforselectionbiasinobservedprices.
Thesignalselectionequationmodelscertificationchoiceasamultinomiallogit(Eq.S2):
exp(η(k))
|     |     | P(cert =k)= |          | i          |     |     | (S2) |
| --- | --- | ----------- | -------- | ---------- | --- | --- | ---- |
|     |     | i           | (cid:80) | exp(η(k′)) |     |     |      |
|     |     |             | k′       | i          |     |     |      |
withη(None) =0asthereferencecategory. Fork ∈{Self-graded,TP-graded},thelinearpredictorisspecified
i
as(Eq.S3):
η(k) =α(k)+γ(k)·rep +δ(k)·log(Vung)+ψ(k)·rep ·log(Vung)+ζ(k)·JP +λ(k)·usignal (S3)
| i   | ρ j | i   |     | j   | i   | i j |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
logVung
Here, rep is the seller reputation score, is the log ungraded market price, distinct from the grade-
| j   |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
logVung usignal
specific V i of A.2, rep · is their interaction, JP i is a Japanese-card indicator, and is a seller
|                                     | j i |                 |              |     |     | j   |     |
| ----------------------------------- | --- | --------------- | ------------ | --- | --- | --- | --- |
| randomeffectwithfactorloadingsλSelf |     | =1(fixed)andλTP | (estimated). |     |     |     |     |
Thelogpriceratiofollowsanormaldistribution(Eq.S4):
)∼N(µprice,σ2
|     |     | log(P /V |     |       | )   |     | (S4) |
| --- | --- | -------- | --- | ----- | --- | --- | ---- |
|     |     | i i      | i   | price |     |     |      |
withtheconditionalmeanspecifiedinEq.S5:
|     | µprice =αprice+Xpriceβprice+βSelf |     |        |         | +βTP   | +uprice |      |
| --- | --------------------------------- | --- | ------ | ------- | ------ | ------- | ---- |
|     |                                   |     |        | ·1 Self | ·1     | TP      | (S5) |
|     | i                                 | i   | signal |         | signal | j       |      |
The design matrix Xprice contains five covariates: (1) seller reputation score, (2) Japanese-card indicator,
(3) reputation × self-graded, (4) reputation × TP grading, and (5) returns-accepted indicator. The interaction
coefficientsβ andβ aretheparametersofprimaryinterest;theirposteriorestimatesarereportedinTableS2.
3 4
19

ThebinarysaleoutcomefollowsaBernoullidistributionwithalogitlink(Eq.S6):
sold ∼Bernoulli(logit−1(ηsold)) (S6)
i i
withthelinearpredictorspecifiedinEq.S7:
ηsold =αsold+Xsoldβsold+usold (S7)
i i j
The design matrix Xsold contains nine covariates: (1) seller reputation score, (2) self-graded indicator, (3)
TP-gradedindicator,(4)Japanese-cardindicator,(5)returns-acceptedindicator,(6)logpriceratio,(7)loglisting
duration,(8)reputation×self-graded,and(9)reputation×TPgrading.
Anon-centeredparameterizationofthethree-dimensionalcorrelatedrandomeffectsimprovesMCMCsam-
plingefficiencyforthelargesellerpopulationintheanalysissample(N =60,386). Theseller-levelrandom
sellers
vectorisspecifiedas(Eq.S8):
 uprice
j
u
j
= us
j
old =L·z
j
, z
j
∼N(0,I
3
) (S8)
usignal
j
whereL=diag(σ )·L istheCholeskyfactorofthecovariancematrix,σ containsthestandarddeviations,
u Ω u
andL istheCholeskyfactorofthecorrelationmatrix.
Ω
All parameters receive weakly informative priors. For the signal selection equation: intercepts α(k) ∼
N(0,2); slope coefficients γ(k),δ(k),ζ(k) ∼ N(0,1); interaction coefficients ψ(k) ∼ N(0,0.5); and the
ρ
TP factor loading λTP ∼ N(1,1). For the price equation: intercept αprice ∼ N(0,2); slope coefficients
βprice ∼ N(0,2) (K = 5 vector); signal intercepts βSelf ,βTP ∼ N(0,1); and residual standard de-
signal signal
viation σ ∼ Exponential(1). For the sold equation: intercept αsold ∼ N(0,2) and slope coefficients
price
βsold ∼ N(0,2) (K = 9 vector). For the random effects: latent vector z ∼ N(0,I ); standard deviations
j 3
σ ∼Exponential(1)(threeelements);andtheCholeskyfactorofthecorrelationmatrixL ∼LKJ(2).
u Ω
A.4 MCMC Sampling
ThemodelwasestimatedviaHamiltonianMonteCarlo(HMC)usingtheNo-U-TurnSampler(NUTS),imple-
mentedinStan. Eightparallelchainswererunwith4,000totalposteriordraws. Acrossall38parametersRˆ was
at most 1.013 and bulk ESS at least 221, both extremes occurring for the random-effects correlation Ω . Full
23
convergencediagnosticsandmodelfitevaluationarereportedintableS1andfig.S5.
20

B Theoretical Model
B.1 Model Assumptions
The model is a signaling game between a seller (Sender) and a pool of buyers (Receivers), in which the seller
privatelyobservesproductqualityandchoosesasignals ∈ {TP,Self,None}beforebuyersformbeliefsandset
prices. Sixassumptionsdefinetheenvironment;subsequentsectionsderiveequilibriafromtheseprimitives.
Assumption1(Qualityanditemvalue). Productqualityisbinary,θ ∈{H,L},withcorrespondingitemvalues
v(H)=V >0andv(L)=0. ThepriorprobabilityofhighqualityisP(θ =H)=π ∈(0,1).
0
Assumption 2 (Information structure). The seller’s type θ is private information. The seller’s reputation ρ is
publiclyobservable. Buyersobservethesignal–reputationpair(s,ρ)andformposteriorbeliefspˆ .
s
Assumption3(Coststructure). Signalingcostsdependonsellertypeandreputation(Eq.S9):

 
c
TP
s=TP, θ =H

 +∞ s=TP, θ =L


c(s,θ,ρ)= 0 s=Self, θ =H (S9)

 ϕρ s=Self, θ =L



0 s=None
where c > 0 is the TP grading cost, ϕ > 0 is the penalty coefficient for detected misrepresentation, and
TP
ρ∈[0,1]istheseller’sreputation,basedoncumulativetransactionhistory.
The cost matrix (Eq. S9) embodies four implicit assumptions: L-types cannot pass TP grading (row 2),
truthfulH-Selfiscostless(row3),fraudulentL-Selftriggersareputation-proportionalpenaltyϕρ(row4),and
detectioniscertain(q = 1). Underimperfectdetection(q < 1),thereputation-collateralboundV¯(ρ)derivedin
B.2scalesbyq;theregimepartitionandcomparativestaticsareotherwiseunchanged.
Assumption4(OutsideoptionforNone). ThesignalNonedenotesnon-participationinthesignalinggame. It
tradesattheexogenousoutside-optionpriceπ V andisnotsubjecttoBayesianupdating.
0
Assumption5(Bertrand-competitivebuyers). Buyersarerisk-neutralandbiduptotheirexpectedvalue. Given
signalsandreputationρ,buyersformaposteriorbeliefpˆ = P(H | s,ρ),andBertrandcompetitionyieldsthe
s
equilibriumpricep(s,ρ)=pˆ V fors∈{TP,Self}. ThepriceatNoneisexogenous(Assumption4).
s
Assumption6(Sellerpayoff). Theseller’spayoffisthereceivedpriceminusthesignalingcost(Eq.S10):
Π (θ,s,ρ)=p(s,ρ)−c(s,θ,ρ) (S10)
seller
Thesellerisrisk-neutralandthepayoffislinearinpriceandcost.
Generalpayoffstructure
Assumptions 1–6 yield the following seller payoffs: (i) H → TP: pˆ V −c (grading cost); (ii) L → TP:
TP TP
infeasible;(iii)H → Self: pˆ V (zerocost);(iv)L → Self: pˆ V −ϕρ(reputationpenalty);(v)H → None:
Self Self
π V (exogenous outside-option price); (vi) L → None: π V (exogenous outside-option price). The belief
0 0
pˆ = 1followsdirectlyfromAssumption3(TPisinfeasibleforL-types),whilepˆ isdeterminedwithinthe
TP Self
modelinequilibrium(B.2).
Solutionconcept
DefinitionB.1(Strategy). Aseller’sstrategyisamappingfromtypeandreputationtoaprobabilitydistribution
oversignals:
σ :Θ×[0,1]→∆(S)
where Θ = {H,L} is the type space, S = {TP,Self,None} the signal set, and ∆(S) the set of probability
distributionsoverS.
21

DefinitionB.2(BeliefSystem). Thebuyer’sbeliefsystemmapsobservedsignal–reputationpairstoaposterior
probabilityofhighquality:
|     | pˆ:S×[0,1]→[0,1], |     |     | pˆ(s,ρ)=P(H | |s,ρ) |     |     |
| --- | ----------------- | --- | --- | ----------- | ----- | --- | --- |
(σ∗,pˆ∗)
Definition B.3 (Equilibrium). A strategy–belief pair constitutes an equilibrium if two conditions hold
simultaneously:
| (i)Sequentialrationality: | foreach(θ,ρ), |     |     |     |     |     |     |
| ------------------------- | ------------- | --- | --- | --- | --- | --- | --- |
σ∗(θ,ρ)∈argmax[p(s,ρ)−c(s,θ,ρ)]
s∈S
wherethepricep(s,ρ)istheoneAssumptions4and5assigntothebeliefpˆ∗(s,ρ).
(ii)Bayesconsistency:beliefsatSelfandTPsatisfyBayes’rulewheneverthosesignalsareontheequilibrium
path. BecauseNoneisanexogenousoutsideoption,itisnotsubjecttoBayesianupdating.
DefinitionB.4(InformationSets). Buyerinformationsetshavethefollowingstructure:
I isasingletonwithpˆ =1(certainlyH);I maycontainbothtypes,sopˆ ∈[0,1];andI carries
| TP               | TP  |     | Self |     |     | Self | None |
| ---------------- | --- | --- | ---- | --- | --- | ---- | ---- |
| theprior,pˆ =π . |     |     |      |     |     |      |      |
| None 0           |     |     |      |     |     |      |      |
The singleton structure of I follows from Assumption 3 (L-type sellers cannot pass TP grading). The
TP
I
posterior at None equals the prior because None is an exogenous outside option (Assumption 4). The posterior
atI isdeterminedendogenouslyinequilibrium.
Self
Theremainingbeliefparameterpˆ Self isdeterminedendogenouslyviaBayes’rule;B.2derivesitforthefirst
candidateequilibrium.
Scopeoftheprimitives
Two simplifications in the primitives above limit the scope of the model’s predictions. The binary type space
{H,L} restricts posterior beliefs in separating equilibria to the endpoints 0 and 1, whereas the empirical data
showacontinuousrelationshipbetweenreputationandthecredibilityofSelf,whichwouldrequireacontinuous
typespacetorepresentfully. ThereputationpenaltyϕρisassumedindependentofitemvalueV,whereasfraud
involving high-value items may in practice inflict greater reputational damage. Neither relaxation changes the
directionofthecomparativestaticsderivedbelow.
| B.2 Self-Separating | Equilibrium |     |     |     |     |     |     |
| ------------------- | ----------- | --- | --- | --- | --- | --- | --- |
The general payoff structure in B.1 leaves pˆ as an endogenous unknown. Here, we show that the candi-
Self
dateprofileinwhichH-typesellerschooseSelfandL-typesellerschooseNoneconstitutesaPerfectBayesian
<V¯(ρ),andwederiveV¯(ρ)fromthebindingL-typeincentiveconstraint.
Equilibrium(PBE)wheneverV
Equilibriumcandidate
WeconjectureafullyseparatingstrategyprofileinwhichH-typesellerschooseSelfandL-typesellerschoose
None:
|     |     | σ∗(H,ρ)=Self, |     | σ∗(L,ρ)=None |     |     |     |
| --- | --- | ------------- | --- | ------------ | --- | --- | --- |
This conjecture is motivated by the cost asymmetry in Assumption 3: H-type sellers face no cost for Self,
whileL-typesellersbearareputationpenaltyofϕρ. Theincentive-compatibility(IC)conditionsbelowconfirm
whenthisprofileconstitutesanequilibrium.
Equilibriumbeliefs
BecauseonlyH-typesellerschooseSelfontheequilibriumpath,Bayes’ruleyields:
π ·1
0
|                            | pˆ Self | =P(H |Self)=    |     |                | =1  |     |     |
| -------------------------- | ------- | --------------- | --- | -------------- | --- | --- | --- |
|                            |         |                 |     | π ·1+(1−π      | )·0 |     |     |
|                            |         |                 |     | 0              | 0   |     |     |
| ForTP,Assumption3impliespˆ |         | =1(structural). |     | Noneremainsatπ | .   |     |     |
|                            |         | TP              |     |                | 0   |     |     |
22

Equilibriumpayoffs
With beliefs now determined, substituting pˆ = 1 and pˆ = 1 into the general payoff structure (see B.1)
|     |     |     |     |     | Self |     | TP  |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
yieldsthefollowingpayoffs. Ontheequilibriumpath,H →SelfyieldsV andL→Noneyieldsπ V. Off-path
0
| deviationsgive: | L→Self: | V −ϕρ;H |     | →None: | π   | V;H →TP: | V   | −c . |     |     |
| --------------- | ------- | ------- | --- | ------ | --- | -------- | --- | ---- | --- | --- |
|                 |         |         |     |        |     | 0        |     | TP   |     |     |
Incentivecompatibilityconditions
H-typeIC.
(a)Self≻None:
|                  |     | Π       | (Self)>Π | (None) |     | ⇐⇒ V | >π  | V ⇐⇒ π | <1  |     |
| ---------------- | --- | ------- | -------- | ------ | --- | ---- | --- | ------ | --- | --- |
|                  |     | H       |          | H      |     |      | 0   | 0      |     |     |
| Thisholdsforallπ |     | ∈(0,1). |          |        |     |      |     |        |     |     |
0
(b)Self≻TP:
|     |     | Π H (Self)>Π |     | H (TP) | ⇐⇒  | V >V | −c  | TP ⇐⇒ c TP | >0  |     |
| --- | --- | ------------ | --- | ------ | --- | ---- | --- | ---------- | --- | --- |
ThisholdsunderAssumption3.
L-typeIC.None≻Self:
|     | Π   | (None)>Π | (Self) |     | ⇐⇒  | π V >V | −ϕρ | ⇐⇒ V(1−π | )<ϕρ |     |
| --- | --- | -------- | ------ | --- | --- | ------ | --- | -------- | ---- | --- |
|     |     | L        | L      |     |     | 0      |     |          | 0    |     |
SolvingforV
definesthereputation-collateralbound:
ϕ
|     |     |     |     | V   | <   | ρ≡V¯(ρ) |     |     |     | (S11) |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ----- |
|     |     |     |     |     | 1−π | 0       |     |     |     |       |
The H-type IC conditions (a) and (b) hold unconditionally under Assumptions 1 and 3. The binding con-
straint is the L-type IC, which holds strictly for V < V¯(ρ), leaves the L-type indifferent at V = V¯(ρ), where
V¯(ρ),
None remains a best response, and fails for V > where the L-type deviates to Self. The equilibrium
| thereforeexistsexactlyforV |     | ≤V¯(ρ). |     |     |        |     |     |     |     |     |
| -------------------------- | --- | ------- | --- | --- | ------ | --- | --- | --- | --- | --- |
|                            |     |         |     |     | V¯(ρ)= | ϕ   |     |     |     |     |
DefinitionB.5(Reputation-collateralbound). ρisthemaximumitemvalueatwhichasellerwith
1−π0
reputation ρ can sustain credible self-grading through reputation collateral alone. The slope ϕ/(1−π ) is the
0
additionalitemvaluesustainableperunitofreputation. ThisboundcorrespondstoEq.1inthemaintext.
Proposition B.1 (Existence of the Self-separating equilibrium). The separating equilibrium (H → Self, L →
|                                                           |     |     | V¯(ρ). |     | V¯(ρ)theL-typeisindifferentbetweenNoneandSelf, |     |     |     |     |        |
| --------------------------------------------------------- | --- | --- | ------ | --- | ---------------------------------------------- | --- | --- | --- | --- | ------ |
| None)existsifandonlyifV                                   |     | ≤   |        | AtV | =                                              |     |     |     |     | andthe |
| profilecoincideswiththesemi-separatingequilibriumofB.3atσ |     |     |        |     |                                                |     |     | =0. |     |        |
L
Intuitively,V¯(ρ)measuresthemaximumitemvaluesustainablebyreputationcollateralalone(seeFig.4for
thelinearboundary).
Comparativestatics
Thereputation-collateralboundV¯(ρ)respondstomodelprimitivesasfollows:
|     |     |     |     | ∂V¯(ρ) |     | ϕ   |     |     |     |       |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |        | =   |     | >0, |     |     | (S12) |
|     |     |     |     | ∂ρ     |     | 1−π |     |     |     |       |
0
∂V¯(ρ)
ρ
|     |     |     |     |     | =   |     | >0, |     |     | (S13) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     | ∂ϕ  |     | 1−π |     |     |     |       |
0
∂V¯(ρ)
ϕρ
|     |     |     |     |     | =   |      | >0. |     |     | (S14) |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ----- |
|     |     |     |     | ∂π  |     | (1−π | )2  |     |     |       |
|     |     |     |     |     | 0   |      | 0   |     |     |       |
Allthreederivativesarepositive: higherρ(Eq.S12),harsherpenaltyϕ(Eq.S13),andhigherpriorπ (Eq.S14)
0
eachexpandtheSelfregime,becausemorereputationcollateral,strongersanctions,orasmallerdeceptionrent
| (1−π )V allraisethebound. |     |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
The Self-separating equilibrium is therefore self-enforcing for V < V¯(ρ). For V > V¯(ρ) a self-claim is
no longer fully credible, and B.3 derives the two equilibria that arise there, a semi-separating one in which a
self-claimretainspartialcredibilityandaTP-separatingoneathigheritemvalues.
23

| B.3 TP-Separating |     |     | Equilibrium |     | and Equilibrium |     | Refinement |     |     |     |     |
| ----------------- | --- | --- | ----------- | --- | --------------- | --- | ---------- | --- | --- | --- | --- |
V¯(ρ),
In the Self-separating equilibrium (B.2), Bayes’ rule pins down the belief at Self whenever V < and
Assumption 4 fixes the belief at None. When V > V¯(ρ), that equilibrium does not exist, and an alternative
candidate uses TP grading as the quality signal. In this profile, Self becomes an off-path signal, introducing
beliefindeterminacythatmustberesolved. ThissectionderivestheTP-separatingandsemi-separatingequilibria
and selects among candidate equilibria with the D1 criterion (28–30), which restricts off-path beliefs in cases
wheretheIntuitiveCriterionleavesthemunrestricted.
Equilibriumcandidate
|     |     |     |     | σ∗(H,ρ)=TP, |     |     | σ∗(L,ρ)=None |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | ------------ | --- | --- | --- | --- |
Beliefs on the equilibrium path are structurally determined. Assumption 3 precludes L-type sellers from
obtainingTPgrading,sopˆ = 1,andNoneremainsatthepriorπ (Assumption4). Selfisanoff-pathsignal,
|     |     |     | TP  |     |     |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sincenosellerchoosesSelfinthisprofile, andBayes’rulecannotpindownwhatbuyersshouldbelieveifSelf
wereneverthelessobserved. UnderPBE,pˆoff ∈[0,1]isunrestricted,andweresolvethisindeterminacybelow.
Self
Deviationthresholds
pˆoff
Whether a type gains from a deviation to Self depends on the off-path belief . We express each type’s
Self
deviationconditionasathresholdonthisbelief.
AdeviationtoSelfyieldspˆoff
H-typedeviation. TheequilibriumpayoffunderTPisV −c . V. TheH-type
|     |     |     |     |     |     |     | TP  |     |     | Self |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
profitsfromthedeviationwhen:
c
|     |     |     |     | pˆoff V | >V −c | ⇐⇒  | pˆoff >1− | TP  |     |     |     |
| --- | --- | --- | --- | ------- | ----- | --- | --------- | --- | --- | --- | --- |
|     |     |     |     | Self    |       | TP  | Self      |     |     |     |     |
V
Becausec TP > 0,thethreshold1−c TP /V liesbelow1,sosufficientlyoptimisticbeliefsmakethedeviation
profitable.
pˆoff
L-type deviation. The equilibrium payoff under None is π 0 V. A deviation to Self yields V −ϕρ. The
Self
L-typeprofitsfromthedeviationwhen:
ϕρ
|         |      |     |       | pˆoff    |       |                      | pˆoff |     |     |     |     |
| ------- | ---- | --- | ----- | -------- | ----- | -------------------- | ----- | --- | --- | --- | --- |
|         |      |     |       | V >π     | V +ϕρ | ⇐⇒                   | >π    | +   |     |     |     |
|         |      |     |       | Self     | 0     |                      | Self  | 0 V |     |     |     |
| Writep¯ | =1−c | /V  | andp¯ | =π +ϕρ/V |       | forthetwothresholds. |       |     |     |     |     |
| H       |      | TP  |       | L 0      |       |                      |       |     |     |     |     |
Lemma B.1 (Reduction to threshold comparison). Let Self be off the equilibrium path. The price offered by
buyersisstrictlyincreasinginthebelief,offtheequilibriumpathaswellasonit(Assumption5),andsignaling
costsdonotdependonthebelief(Assumption3). Typeθ’spayofffromadeviationtoSelfisthereforepˆoff V −
Self
pˆoff
c(Self,θ,ρ), affine in with slope V > 0. The set of beliefs under which type θ strictly gains from the
Self
deviation is the interval D = (p¯ ,1]∩[0,1], and the set under which it is indifferent is D0 = {p¯ }∩[0,1].
|     |     |     | θ   | θ   |     |     |     |     |     | θ θ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Their union is the interval [p¯ ,1] whenever nonempty, and p¯ < 1 because c > 0, so D is nonempty.
|               |     |     | θ                  |     |     |     | H   |     | TP  | H   |     |
| ------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| ConsequentlyD | ∪D0 | ⊊D  | holdsifandonlyifp¯ |     |     | >p¯ | .   |     |     |     |     |
|               | θ   | θ   | θ′                 |     |     | θ   | θ′  |     |     |     |     |
Ifthecostofasignalvariedwiththetransactionprice,thetwodeviationpayoffswouldhavedifferentslopes
inpˆoff ,thesetsD andD couldintersectwithouteithercontainingtheother,andthecomparisonbelowwould
| Self | H   | L   |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
notreducetotheorderingoftwothresholds.
PBEexistence
| TheH-typeprefersTPtoNonewhenV |     |     |     | −c  | >π  | V,thatis,when |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
|                               |     |     |     |     | TP  | 0             |     |     |     |     |     |
c TP
|     |     |     |     |     | V   | >   | ≡V  |     |     |     | (S15) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
1−π
0
24

Thisboundinvolvesnooff-pathbelief. V istheminimumitemvalueatwhichthequalitypremium(1−π )V
0
coversthecertificationcostc . ItcorrespondstoEq.2inthemaintextanddoesnotdependonρ. Thecredibility
TP
ofTPgradingrestsonthegradinginstitutionratherthanontheseller’sreputation.
NotypegainsfromadeviationtoSelfwhenpˆoff ≤ min(p¯ ,p¯ ). TheTP-separatingprofileisthereforea
|     |     |     |     |     | H   | L   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Self
PBEforeveryV ≥V,supportedbyanyoff-pathbeliefinthisrange.
Refinementoftheoff-pathbelief
Selfistheonlysignaltowhichtherefinementapplies. ThebeliefatNoneisfixedatthepriorπ (Assumption
0
4), and the belief at TP equals 1 by feasibility (Assumption 3). The D1 criterion places zero probability on a
typewhosesetofdeviation-supportingbeliefsisstrictlycontainedinthatoftheothertype. ByLemmaB.1,this
| comparisonreducestotheorderingofp¯ |     |     | andp¯ . |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|                                    |     | H   | L       |     |     |     |     |     |     |
Definition B.6 (Refined off-path belief). When p¯ > p¯ , every belief under which the L-type gains from a
|     |     |     | L   | H   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deviationtoSelfalsoletstheH-typegainstrictly(LemmaB.1),andtheoff-pathbeliefissettopˆoff =1. When
Self
p¯ >p¯ ,thereversecontainmentholdsandthebeliefissettopˆoff =0. Whenp¯ =p¯ ,thetwosetscoincide,
| H L |     |     |     |     | Self |     | H   | L   |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
nostrictcontainmentholdsineitherdirection,andthebeliefisnotrestricted.
The two thresholds are equal when 1−c /V = π +ϕρ/V, that is, when V = (c +ϕρ)/(1−π ) =
|     |     |     | TP  | 0   |     |     |     | TP  | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
V¯(ρ)+V,thecertificationboundary.
|     |     | Becausep¯ | H increasesinV |     | whilep¯ | L decreasesinV,threecasescoverthe |     |     |     |
| --- | --- | --------- | -------------- | --- | ------- | --------------------------------- | --- | --- | --- |
parameterspaceawayfromthisvalue.
V¯(ρ). ∪D0
(a)V ≤ Herep¯ L ≥ 1, soD L isemptyorequals{1}, whileD H isnonempty(p¯ H < 1). The
L
beliefissettopˆoff =1. TheH-typethenreceivesV fromSelfagainstV −c fromTP,andtheTP-separating
Self TP
profileisnotanequilibrium.
(b)V¯(ρ) < V < V¯(ρ)+V. Herep¯ < p¯ < 1,soD ∪D0 = [p¯ ,1] ⊊ (p¯ ,1] = D . Thebeliefisset
|     |     | H   | L   | L   | L   | L   | H   | H   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
topˆoff
=1,theH-typereceivesV >V −c TP ,andtheTP-separatingprofileisnotanequilibrium.
Self
(c)V > V¯(ρ)+V. Herep¯ < p¯ ,soD ∪D0 = [p¯ ,1] ⊊ (p¯ ,1] = D . Thebeliefissettopˆoff = 0.
|     | L   | H   | H   | H H |     | L   | L   |     | Self |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
TheH-typereceives0fromSelfagainstV −c > 0fromTP,theL-typereceives−ϕρfromSelfagainstπ 0 V
TP
fromNone,andtheTP-separatingprofileisanequilibrium.
Thereversalbetween(b)and(c)followsfromthetwocoststructures. TheH-type’sgainfromanunexpected
self-claim is the certification cost c , which does not vary with V. The L-type’s gain from misrepresentation
TP
BelowV¯(ρ)+V
isproportionaltoV, whilethecollateralϕρdoesnotvarywithV. thedeviationthresholdis
lowerfortheH-type;aboveit,lowerfortheL-type.
PropositionB.2(ExistenceoftheTP-separatingequilibrium). Theprofile(H →TP, L→None): (i)isaPBE
≥V,supportedbyanyoff-pathbeliefpˆoff
ifandonlyifV ≤min(p¯ H ,p¯ L ),withtheH-typeindifferentbetween
Self
TPandNoneatV = V; (ii)satisfiestheIntuitiveCriterionifandonlyif,inaddition,V > V¯(ρ); (iii)satisfies
|                            |     | V¯(ρ)+V. | SinceV¯(ρ)+V |     |     | max(V¯(ρ),V)foreveryρ |     |                  |     |
| -------------------------- | --- | -------- | ------------ | --- | --- | --------------------- | --- | ---------------- | --- |
| theD1criterionifandonlyifV | >   |          |              |     | >   |                       |     | > 0,(iii)implies |     |
(i)and(ii).
Part (i) restates the existence result above. Part (ii) holds because the L-type’s maximal deviation payoff
V −ϕρfallsbelowitsequilibriumpayoffπ V exactlywhenV <V¯(ρ),inwhichcasethedeviationisattributed
0
V¯(ρ)
to the H-type and the profile fails; for V > neither type is excluded on these grounds. Part (iii) restates
cases(a)–(c).
Thesemi-separatingequilibrium
|     |     |     | ForV¯(ρ)≤V |     | ≤V¯(ρ)+V,theprofileinwhichH-typesellers |     |     |     |     |
| --- | --- | --- | ---------- | --- | --------------------------------------- | --- | --- | --- | --- |
PropositionB.3(Semi-separatingequilibrium).
chooseSelfandL-typesellerschooseSelfwithprobabilityσ andNoneotherwise,with
L
|     |     |       | π (1−π   | −y) |     | ϕρ  |     |     |     |
| --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
|     |     |       | 0        | 0   |     |     |     |     |     |
|     |     | σ L = |          |     | , y | = , |     |     |     |
|     |     |       | (1−π )(π | +y) |     | V   |     |     |     |
0 0
and on-path belief pˆ = π +ϕρ/V, is a PBE.The stated σ lies in [0,1] throughout this range. For ρ > 0,
| Self | 0   |     |     |     | L   |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesemi-separatingprofileistheuniqueequilibriumsurvivingtheD1criterionontheinterioroftherange.
25

Proof. Existence. TheL-typeindifferenceconditionpˆ V −ϕρ = π V givespˆ = π +ϕρ/V,andBayes’
|     |     |     | Self | 0   | Self | 0   |     |
| --- | --- | --- | ---- | --- | ---- | --- | --- |
ruleyieldsthisbeliefatthestatedσ (thesameexpressionasthemixingprobabilityderivedinMethods). σ ≥0
|     |     | L   |     |     |     |     | L   |
| --- | --- | --- | --- | --- | --- | --- | --- |
≥V¯(ρ);σ
holdsifandonlyify ≤1−π ,thatis,V ≤1reducestoϕρ/V ≥0andalwaysholds. TheH-type
|     |     | 0   | L   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
receivesπ V +ϕρfromSelfandπ V fromNone. ThebeliefatTPequals1(Assumption3),soadeviationto
|         | 0       | 0   |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
| TPpaysV | −c ,and |     |     |     |     |     |     |
TP
|          |     | π V +ϕρ≥V | −c ⇐⇒ | V ≤V¯(ρ)+V. |     |            |     |
| -------- | --- | --------- | ----- | ----------- | --- | ---------- | --- |
|          |     | 0         | TP    |             |     |            |     |
| =V¯(ρ),σ |     |           |       |             |     | =V¯(ρ)+V,σ |     |
AtV =0andtheprofilecoincideswiththeSelf-separatingequilibrium;atV >0
|     | L   |     |     |     |     |     | L   |
| --- | --- | --- | --- | --- | --- | --- | --- |
andtheH-typepayoffsfromSelfandTPareequal.
Uniqueness. Theremainingprofilesfailontheinterioroftherange. (i)TheSelf-separatingprofilerequires
π V ≥V −ϕρ(PropositionB.1),whichfailsforV >V¯(ρ). (ii)TheTP-separatingprofilefailstheD1criterion
0
inthisrange,bycase(b). (iii)PoolingonSelfgivespˆ = π byBayes’rule,underwhichtheL-typereceives
|     |     |     | Self | 0   |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
π V −ϕρ<π V andprefersNoneforρ>0. (iv)PoolingonNone,withbothtypesreceivingπ V,isaPBEfor
| 0   | 0   |     |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
V < V underoff-pathbeliefspˆoff ≤ π ;thedeviationthresholdsatSelfareπ fortheH-typeandπ +ϕρ/V
|     |     | Self 0 |     |     | 0   |     | 0   |
| --- | --- | ------ | --- | --- | --- | --- | --- |
for the L-type, so the containment argument of Lemma B.1 sets the belief to 1 and the H-type deviates. This
profileisnotremovedbyweakerrefinements,souniquenessintherangeV¯(ρ)
|     |     |     |     |     | < V | < V reliesonthecriterion |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- |
(v)ProfilesinwhichtheH-typemixesacrosssignals,andprofilesinwhichonlytheL-typesends
adoptedhere.
Self,areexcludedbyBayes’ruletogetherwiththeL-type’sparticipationcondition.
Remark B.1 (Payoff dominance). On the interior of the range V¯(ρ) < V < V¯(ρ)+V, the H-type receives
π 0 V+ϕρ>V−c TP inthesemi-separatingequilibrium,theL-typereceivesπ 0 V inbothprofiles,andbuyersearn
zero expected surplus in either profile under Bertrand competition. The semi-separating equilibrium therefore
weaklyPareto-dominatestheTP-separatingprofile,strictlyfortheH-type. Belief-basedrefinementandpayoff
dominanceselectthesameequilibrium.
Remark B.2 (Robustness to Assumption 4). Assumption 4 enters the refinement only through the L-type’s
equilibrium payoff π V. In a variant in which None is subject to Bayesian updating, that payoff in the TP-
0
separatingprofileis0, thethresholdp¯ becomesϕρ/V whilep¯ isunchanged, andtherangecoveredbycase
|                |       | L         |                             | H   |     |     |     |
| -------------- | ----- | --------- | --------------------------- | --- | --- | --- | --- |
| (b)becomesϕρ<V | <ϕρ+c | ,ofwidthc | . Thecasestructurepersists. |     |     |     |     |
|                |       | TP        | TP                          |     |     |     |     |
RemarkB.3(Priceatthecertificationboundary). ThepriceatwhichtheH-type’sitemtradesisdiscontinuous
=V¯(ρ)+V,whiletheH-type’spayoffiscontinuousthere.
| attheboundaryV |     |     |     |     | BelowtheboundarytheH-type |     |     |
| -------------- | --- | --- | --- | --- | ------------------------- | --- | --- |
sellsunderthebeliefpˆ =π +ϕρ/V atthepricepˆ V =π V +ϕρ,whichequalsV −c ontheboundary.
|     | Self | 0   | Self | 0   |     | TP  |     |
| --- | ---- | --- | ---- | --- | --- | --- | --- |
AboveittheH-typecertifies,thebeliefatTPequalsone,andtheitemtradesatthepriceV. Thepricetherefore
jumpsupwardbyexactlyc . TheH-type’spayoffapproachesV −c frombothsides, andthatcontinuityis
|     |     | TP  |     | TP  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
whatdefinestheboundary. Thecertificationcostisthuspassedthroughtobuyersintheprice,leavingtheseller’s
netpayoffunchangedacrosstheboundary.
Regimepartition
CorollaryB.1(Regimepartition). PropositionsB.1,B.2,andB.3togetherimplythattheboundariesV¯(ρ)and
V¯(ρ)+V
partitionthe(ρ,V)spaceintothreeregimes:
<V¯(ρ)):
• Selfregime(V theSelf-separatingequilibrium(H →Self, L→None);
|     |     | (V¯(ρ) | V¯(ρ)+V): |     |     |     |     |
| --- | --- | ------ | --------- | --- | --- | --- | --- |
• Semi-separating regime < V < a band of vertical width V in which H-type sellers
chooseSelf,L-typesellersmixbetweenSelfandNone,andthebeliefispˆ =π +ϕρ/V;
|     |     |     |     |     | Self | 0   |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
• TPregime(V >V¯(ρ)+V): theTP-separatingequilibrium(H →TP, L→None).
The exclusion arguments (iii)–(v) in the proof of Proposition B.3 do not use the restriction of V to the band,
and Propositions B.1 and B.3 together with cases (a)–(c) determine which of the three named profiles is an
equilibriumineachregime. Theequilibriumisthereforeuniquethroughouteachregimeforρ>0. Theexistence
statements of this section are to be read away from the boundary value V¯(ρ) + V, at which the H-type is
indifferentbetweenSelfandTPandtheadjacentprofilesgivethattypeequalpayoffs(RemarkB.3). Theother
twoboundariesarecoveredbythepropositionsthemselves.
26

Absenceofcertification
Theregimepartitionpresumesthatcertificationisavailable. ThereputationdynamicsinMethodsalsoconsidera
sellerforwhomitisnot,andforthatsellertheSemi-separatingregimeisnotclosedfromabove. Thecertification
boundaryderivessolelyfromtheH-type’sdeviationtoTP,thepointatwhichcertificationovertakesthepartially
credible self-claim, through the H-type comparison in the existence proof of Proposition B.3. A seller who
cannot obtain certification does not face that comparison. The remaining exclusion arguments either do not
involve TP or become vacuous without it, so for ρ > 0 the semi-separating profile is the unique equilibrium
V¯(ρ).
surviving the D1 criterion at every V > Methods analyzes the reputation dynamics generated by these
regimes.
Value-dependentcertificationcost
The certification cost c is assumed independent of item value, whereas grading services in practice charge a
TP
feethatriseswiththeappraisedvalueofthecard.
Remark B.4 (Value-dependent grading fee). The TP grading fee can include a value-proportional component,
c (V) = c +τV with c > 0 and 0 < τ < 1−π , so that the proportional part does not absorb the entire
| TP 0 | 0   |     |     |     | 0   |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
qualitypremium. SubstitutingintotheH-typeindifferenceconditionreplacesV byc /(1−τ −π )andgives
|     |     |     |     |     |     |     | 0 0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
theupperboundaryaslopeofϕ/(1−τ −π ),steeperthantheslopeϕ/(1−π )ofthelowerboundaryV¯(ρ),
|     |     |     | 0   |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichdoesnotinvolvethegradingfeeandisunchanged. Thebandthereforewidenswithreputationinsteadof
keepingaconstantwidth. Thethreeregimesandtheorderofthetwoboundariesareunchanged. Themaintext
adoptsthefixed-feeapproximationforparsimony.
| B.4 Reputation | Dynamics |     |     |     |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Methods states a law of motion for the seller’s reputation and the properties of that law used in the main text.
Thissectionderivesthem,togetherwiththefinerstructureofthecertificationswitch,whichisstatedonlyhere.
Consider the seller introduced in the preceding subsection, for whom certification is unavailable, facing items
of value V. Quality is drawn per listing, so a share π of the seller’s listings is high quality. On that share
0
the H-type trades and reputation rises. On the remaining share the L-type self-claims with probability σ (ρ),
L
and each self-claim that misrepresents lowers it by the same amount, while listings that carry no claim leave it
unchanged. Asinglerateα>0thereforeconvertsthenetfrequencyofthetwomovementsintoaspeed,
|     |     |     | ρ˙ =α[π | −(1−π | )σ  | (ρ)], |     | (S16) |
| --- | --- | --- | ------- | ----- | --- | ----- | --- | ----- |
|     |     |     |         | 0     | 0   | L     |     |       |
| σ   |     |     | α(1 −   | π )σ  | (ρ) |       | π α | α     |
with L as in Proposition B.3. We call 0 L the erosion term and 0 the full rate. The rate
multipliesthewholeright-handside,soitfixestheunitoftimeandcancelsfromeveryrestpoint,everyexistence
condition,andeverycomparisonbelow. ThepenaltycoefficientϕdoesnotenterEq.S16asaseparateterm. It
acts on the L-type through the indifference condition that pins σ , and so reaches reputation only through the
L
argumenty =ϕρ/V.
PropositionB.4(Interiorrestpoint). EquationS16hasatmostonerestpointin(0,1). Oneexistsifandonlyif
)<ϕ,inwhichcaseitliesatρ∗
| π 0 <1/2andV(1/2−π | 0   |     |     |     | =V(1/2−π | 0 )/ϕandisunstable. |     |     |
| ------------------ | --- | --- | --- | --- | -------- | ------------------- | --- | --- |
Proof. Localization. Outside the semi-separating range the L-type plays None, so σ = 0 and ρ˙ = π α > 0.
|     |     |     |     |     |     |     | L   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Everyrestpointthereforeliesinsidethatrange.
+y)2]
Monotonicity. Differentiatingσ givesdσ /dy = −π /[(1−π )(π < 0,andy = ϕρ/V increases
|     |     | L   | L   |     | 0   | 0 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
inρ,sotheright-handsideofEq.S16isstrictlyincreasinginρonthesemi-separatingrange. Ithasatmostone
zerothereandcrossesthatzerofrombelow,soarestpointofEq.S16isunstable.
Location. Arestpointrequiresσ =π /(1−π ),thatis(1−π −y)/(π +y)=1,soy∗ =1/2−π and
|                   |      | L   | 0   | 0   |     | 0   | 0   | 0   |
| ----------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| ρ∗ =Vy∗/ϕ=V(1/2−π | )/ϕ. |     |     |     |     |     |     |     |
0
Interiority. ρ∗ >0ifandonlyifπ <1/2,andρ∗ <1ifandonlyifV(1/2−π )<ϕ. Thesemi-separating
|     |     |     | 0   |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
rangeendsaty =1−π ,andy∗ =1/2−π <1−π holdsforeveryπ ∈(0,1),sothelocalizationstepnever
|     | 0   |     | 0   |     | 0   | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
excludesρ∗.
27

At the baseline values of Table 1 the second condition reads V < ϕ/(1/2−π ) = 2.5, which every item
0
valueshowninFigs.4and6satisfieswithroomtospare. Overthatrangetheminorityconditionalonedecides
whethertherestpointexists.
Proposition B.5 (Absorption at the floor). Under the conditions of Proposition B.4, ρ˙ < 0 throughout [0,ρ∗),
ρ∗
so reputation starting below reaches ρ = 0 in finite time and remains there. The floor is not a rest point of
Eq. S16. At ρ = 0 a self-claim carries only the prior, so σ = 1 and ρ˙ = α(2π −1) < 0. Reputation stops
|     |     |     |     |     |     |     |     | L   |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
therebecauseitisboundedbelow,notbecausethelawofmotionvanishes.
ρ∗,
The right-hand side of Eq. S16 is strictly increasing on the semi-separating range and vanishes at so it
is negative on [0,ρ∗) and bounded away from zero on any [0,ρ ] with ρ < ρ∗. Setting y = 0 in σ gives
|     |      |            |                                     |     |     |     |     | 0   |     | 0   |     |     | L   |
| --- | ---- | ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| π   | (1−π | )/[(1−π )π | ]=1,whencethestatedvalueatthefloor. |     |     |     |     |     |     |     |     |     |     |
| 0   | 0    | 0          | 0                                   |     |     |     |     |     |     |     |     |     |     |
Proposition B.6 (The switch and the drop). Suppose certification is available. The H-type chooses TP below
theswitchingreputation
|     |     |     |     |     | ρ   | =[(1−π | )V  | −c ]/ϕ, |     |     |     |     | (S17) |
| --- | --- | --- | --- | --- | --- | ------ | --- | ------- | --- | --- | --- | --- | ----- |
|     |     |     |     |     | s   |        | 0   | TP      |     |     |     |     |       |
and ρ s ∈ (0,1) if and only if V < V < (ϕ+c )/(1−π 0 ). Below ρ s the L-type plays None and reputation
TP
| growsatthefullrate. |     | Atρ | thegrowthratefallsby |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s
π αc
|     |     |     |     |     |     | ∆=  | 0    | TP. |     |     |     |     | (S18) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     | V −c | TP  |     |     |     |     |       |
V¯(ρ
Proof. Switch. The certification boundary is V = )+V = [ϕρ +c ]/(1−π ), which gives Eq. S17.
|     |     |     |     |     |     |     | s   |     | s   | TP  | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thenρ > 0ifandonlyifV > c /(1−π ) = V,andρ < 1ifandonlyif(1−π )V < ϕ+c . Belowthe
|     | s   |     |     | TP  | 0   |     | s   |     |     |     | 0   | TP  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switchthestaticequilibriumisTP-separating,soσ =0andtheerosiontermvanishes.
L
Drop. At the switch, y = ϕρ /V = (1−π )−c /V < 1−π , so just above ρ the L-type mixes at
|     |     |     | s   | s   |     | 0   | TP  |     | 0   |     |     | s   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesemi-separatingrate. Then1−π −y = c /V andπ +y = (V −c )/V. Substitutingintoσ gives
|     |     |     |     |     | 0 s | TP  |     | 0   | s   | TP  |     |     | L   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
σ (ρ )=π c /[(1−π )(V −c )],andtheerosiontermα(1−π )σ (ρ )equalsEq.S18.
| L   | s   | 0 TP | 0   | TP  |     |     |     |     | 0 L | s   |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma B.2 (The Semi-separatingband). The L-type mixes onthe band (ρ s , ρ s +c TP /ϕ) and plays None on
either side of it. The erosion term is therefore positive throughout the band and zero outside it, and reputation
grows at the full rate above the band as well as below the switch. A positive erosion term does not mean that
reputationfalls. Reputationfallsonlywheretheerosiontermexceedsthefullrate, whichisastrictsubinterval
ofthebandwheneveritisnonempty. Measuredfromtheinteriorrestpoint,thetwoedgesofthebandlieat
|     |     |     |     |       | V −2c |     | (cid:16) | c    | (cid:17) | V   |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | -------- | ---- | -------- | --- | --- | --- | --- |
|     |     |     |     | ρ −ρ∗ | =     | TP, | ρ        | + TP | −ρ∗      | =   | .   |     |     |
|     |     |     |     | s     |       |     |          | s    |          |     |     |     |     |
|     |     |     |     |       |       | 2ϕ  |          | ϕ    |          | 2ϕ  |     |     |     |
Theupperdistanceispositiveateveryitemvalue,soρ∗
|     |     |     |     |     |     |     | alwaysliesbelowthetopoftheband. |     |     |     |     | Itliesaboveρ | if  |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ------------ | --- |
s
| andonlyifV |     | <2c . |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TP
ThebandendswhereV =V¯(ρ),atρ=(1−π )V/ϕ. Subtractingρ∗ =V(1/2−π )/ϕfromEq.S17gives
|     |     |     |     |     |     | 0   |     |     |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(V/2−c )/ϕ,andsubtractingitfromthatupperedgegivesV/(2ϕ). Thetwodistancesdifferbyc /ϕ,which
|     | TP  |     |     |     |     |     |     |     |     |     |     | TP  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is therefore the width of the band. The upper distance is positive for V > 0, and the lower is positive exactly
| whenV | >2c | .   |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TP
PropositionB.7(Trapattheswitch). Supposeπ < 1/2andaswitchexists. IfV > 2c ,reputationgrowsat
|     |     |     |     |     |     | 0   |     |     |     |     | TP  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)<ϕ,reputationbelowρ∗convergestoρ
| everylevelandconvergestoρ=1. |     |     |     | IfV | <2c | TP andV(1/2−π |     | 0   |     |     |     |     | s and |
| ---------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | ----- |
reputation above ρ∗ converges to ρ = 1. If V < 2c and V(1/2−π ) ≥ ϕ, reputation converges to ρ from
|     |     |     |     |     |     |     | TP  |     | 0   |     |     |     | s   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
everystartingpoint. Inthelasttwocasesthestallisatthediscontinuityρ s ,notatazeroofEq.S16,becausethe
growthrateisthefullratejustbelowtheswitchandisnegativejustaboveit.
Proof. Signs. Belowtheswitchandabovethebandtherateisthefullrate,byPropositionB.6andLemmaB.2.
Inside the band the right-hand side of Eq. S16 is strictly increasing with its unique zero at ρ∗, since the mono-
tonicitystepofPropositionB.4appliesunchanged.
28

Cases. If V > 2c , Lemma B.2 places that zero below the band, so reputation grows at every level. If
TP
V < 2c ,thesamelemmaplacesitabovetheswitch. Theright-handsideisthennegativeexactlyon(ρ ,ρ∗).
TP s
Reputationtherefallsbacktoρ ,andreputationbelowρ risestoitatthefullrate.
s s
Reachability. Whenρ∗ < 1,reputationaboveitleavesthebandandconvergestoρ = 1. Whenρ∗ ≥ 1,the
lemmaplacesthetopofthebandaboveρ∗andhenceaboveone,so(ρ ,1]liesinsidethebandandtheright-hand
s
sideisnegativethroughout. Reputationthenconvergestoρ fromeverystartingpointandnoescaperouteexists
s
in[0,1].
Equivalently, the growth rate just above the switch is π α−∆ = π α(V −2c )/(V −c ), so the drop
0 0 TP TP
stallsreputationexactlywhenitexceedsthefullrate.
Thecontinuousapproximation
Thedynamicsabovetreatthereputationrecordasacontinuousvariableevolvingdeterministically. Therecord
is in fact a count that advances one transaction at a time, so the differential equation is an approximation that
improves with the number of recorded transactions. In our data a seller posts about 16 listings on average, a
modest upper bound on that count, and Fig. 6 is therefore a qualitative illustration of the equilibrium structure
ratherthanacalibratedtrajectory.
B.5 Numerical Illustration
ThetheoreticalanalysisinB.1–B.3yieldsclosed-formexpressionsforV¯(ρ)(Eq.S11)andV (Eq.S15). Forthe
qualitative illustration in Fig. 4, we adopt the reference parameter values π = 0.3, ϕ = 0.5, and c = 0.2,
0 TP
which yield V¯(1) = 0.714, V = 0.286, and the certification boundary V¯(1)+V = 1.000 at full reputation.
The reputation dynamics of B.4 introduce one further parameter, the rate α > 0 at which reputation moves in
eitherdirection. Itfixestheunitoftimeandentersnoneoftheconditionsabove,soitcarriesnorowinTable1.
Figure6isdrawnatα=0.1,whichsetstheverticalscaleofthephaseline.
29

| Supplementary | Results        |     |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- | --- |
| C Descriptive | Price Analysis |     |     |     |     |     |
Here,weshowthattwoempiricalregularitiesarealreadyvisiblebeforewefitthehierarchicalBayesianmodel.
Reputationamplifiesthepricepremiumfromself-gradingbutreducesthepremiumfromTPgrading. Wedocu-
mentthesepatternsusinglinearmixed-effectsmodelswithsellerrandomeffects,regressingthelogpriceratioon
reputation, signaltype, andtheirinteraction, whilecontrollingformarketpricebracketandconditioncategory.
Figure S1 displays the resulting interaction patterns for self-grading and TP grading, separately for all listings
andforsolditemsonly. InpanelsAandB,thepredictedlogpriceratioriseswithreputationunderself-grading
(interaction slope β = 0.073 across all listings). In panels C and D, the same slope is negative for TP
interaction
grading (β = −0.118), indicating that high-reputation sellers extract a smaller incremental premium from TP
grading. Both patterns persist in the sold-only subsample (panels B, D), indicating that selection from unsold
listingsdoesnotdrivethem.
| A   |     |     | B   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Self-graded×reputation(alllisted,ungraded) Self-graded×reputation(sold,ungraded)
| 1.2 | β=0.067 |     | 0.4 |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- |
β=0.062
0.3
0.9
| )gol( oitar ecirP | β=-0.005 |        | )gol( oitar ecirP |     |     |        |
| ----------------- | -------- | ------ | ----------------- | --- | --- | ------ |
|                   |          | Signal |                   |     |     | Signal |
0.2
| 0.6 |     | No Self-graded |     |     | β=0.029 | No Self-graded |
| --- | --- | -------------- | --- | --- | ------- | -------------- |
|     |     | (n=603,587)    |     |     |         | (n=82,233)     |
|     |     | Self-graded    |     |     |         | Self-graded    |
|     |     | (n=319,688)    |     |     |         | (n=43,521)     |
0.1
0.3
0.0
0.0
| -3 -2 | -1 0 1 2   | 3   | -3 -2 | -1 0       | 1 2 |     |
| ----- | ---------- | --- | ----- | ---------- | --- | --- |
|       | Reputation |     |       | Reputation |     |     |
C TP-graded×reputation(alllisted) D TP-graded×reputation(sold)
β=0.023 0.75
1.00
| 0.75              |     |            | 0.50              |     |         |           |
| ----------------- | --- | ---------- | ----------------- | --- | ------- | --------- |
| )gol( oitar ecirP |     |            | )gol( oitar ecirP |     |         |           |
|                   |     | Signal     |                   |     | β=0.050 | Signal    |
|                   |     | TP-graded  |                   |     |         | TP-graded |
| 0.50              |     | (n=36,754) | 0.25              |     |         | (n=5,784) |
|                   |     | Ungraded   |                   |     |         | Ungraded  |
β=-0.095
|     |     | (n=923,275) |     |     |     | (n=125,754) |
| --- | --- | ----------- | --- | --- | --- | ----------- |
0.25
0.00
β=-0.129
0.00
| -3 -2 | -1 0 1 2   | 3   | -3 -2 | -1 0       | 1 2 |     |
| ----- | ---------- | --- | ----- | ---------- | --- | --- |
|       | Reputation |     |       | Reputation |     |     |
Fig. S1. Descriptive interaction plots of seller reputation and quality signal type. Each panel displays estimates from a linear
mixed-effectsmodel(lmer)withsellerrandomeffectsandpredictionintervals,controllingformarketpricebracketandcondition
category. (A)Reputation×self-graded(allungradedlistings): thereputation×self-gradedinteractionispositiveandsignificant
| (β = 0.073). | (B)Reputation×self-graded(solditemsonly,N |     | = 125,754): |                                          |     |     |
| ------------ | ----------------------------------------- | --- | ----------- | ---------------------------------------- | --- | --- |
| interaction  |                                           |     |             | restrictingtosolditemsmitigatesselection |     |     |
bias. Theinteractionremainssignificant(β interaction =0.034,SE=0.006,p<0.001). (C)Reputation×TP-graded(alllistings):
negativeinteraction(β =−0.118).(D)Reputation×TP-graded(solditemsonly):substitutionpatternpersists(β =
|     | interaction |     |     |     |     | interaction |
| --- | ----------- | --- | --- | --- | --- | ----------- |
−0.179).
30

| D Seller | Volume |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- |
Certification strategies affect not only per-unit pricing but also transaction volume. Using data aggregated at
theseller-by-signal-typelevel(restrictedtosellerswiththreeormorelistingspersignaltype),weanalyzethree
volume metrics across reputation levels (fig. S2). Panel A shows that high-reputation sellers list more items
across all signal types, reflecting a high-volume strategy, though the increase is modest for TP-graded items.
Panel B reveals that TP-graded listings achieve particularly high sale rates at higher reputation levels. Panel C
confirms that both effects combine. High-reputation sellers realize greater transaction volumes across signal
types.
A Signal×reputation(listings,NB) B Signal×reputation(salerate,Beta) C Signal×reputation(soldcount,NB)
125
20
|                          |     | )detciderp( etar elaS |     | )detciderp( tnuoc dloS |     |     |
| ------------------------ | --- | --------------------- | --- | ---------------------- | --- | --- |
| )detciderp( sgnitsiL 100 |     | 0.25                  |     |                        |     |     |
15
75
0.20
10
50
0.15
5
25
| 0     |            | 0.10                   |                 |               | 0          |       |
| ----- | ---------- | ---------------------- | --------------- | ------------- | ---------- | ----- |
| -3 -2 | -1 0 1 2   | -3 -2                  | -1 0 1          | 2             | -3 -2 -1   | 0 1 2 |
|       | Reputation |                        | Reputation      |               | Reputation |       |
|       |            | Signal None (n=15,404) | Self (n= 9,641) | TP (n= 1,627) |            |       |
Fig.S2.Seller-levelvolumemetricsbysignaltype(None,Self-graded,TP-graded).(A)Listingcount:negativebinomialregression
(MASS::glm.nb),whichaccountsforoverdispersion.(B)Salerate:betaregression(betareg)for(0,1)-boundedproportions.
(C)Salecount:negativebinomialregression.
31

| E Revenue | and Margin | Analysis |     |     |     |
| --------- | ---------- | -------- | --- | --- | --- |
FigureS3presentsconditionalandexpectedrevenueandmarginbysignaltypeacrossthereputationrange. The
toprow(A,B)showsoutcomesconditionalonsale,estimatedvialinearmixed-effectsmodelswithsellerrandom
effects. Thebottomrow(C,D)integratessaleprobabilitythroughatwo-partmodel: Part1estimatesP(sold)via
alogisticmixed-effectsmodel(glmer);Part2estimatesE[price|sold]andE[margin|sold]vialmer. Expected
revenueandmarginarethenP(sold)×E[·|sold].
TP-graded items command higher conditional sale prices and margins, but the pricing advantage erodes at
high reputation levels (A, B). Panel B shows that high-reputation TP-graded sellers accept smaller conditional
margins,consistentwithavolume-orientedstrategy. However,asfig.S2demonstrates,elevatedsaleprobabilities
compensate. Panel C shows that expected revenue for TP-graded items increases steeply with reputation, and
panelDrevealsaninverted-Upatterninexpectedmarginacrossreputationlevels.
| A   |     |     | B   |     |     |
| --- | --- | --- | --- | --- | --- |
Signal×reputation(price,sold,LME) Signal×reputation(margin,sold,LME)
250
60
| )ylno dlos ,DSU( ecirP |     |     | )ylno dlos ,DSU( nigraM |     |     |
| ---------------------- | --- | --- | ----------------------- | --- | --- |
200
|     |     | Signal          |     |     | Signal          |
| --- | --- | --------------- | --- | --- | --------------- |
| 150 |     |                 | 40  |     |                 |
|     |     | None (n=82,233) |     |     | None (n=82,233) |
|     |     | Self (n=43,521) |     |     | Self (n=43,521) |
| 100 |     | TP (n= 5,784)   |     |     | TP (n= 5,784)   |
20
50
0
| -3 -2 -1 | 0 1        | 2   | -3 -2 -1   | 0 1 | 2   |
| -------- | ---------- | --- | ---------- | --- | --- |
|          | Reputation |     | Reputation |     |     |
| C        |            |     | D          |     |     |
Signal×reputation(expectedrevenue,two-part) Signal×reputation(expectedmargin,two-part)
2.0
| )DSU( eunever detcepxE 20 |     |     | )DSU( nigram detcepxE |     |     |
| ------------------------- | --- | --- | --------------------- | --- | --- |
1.5
| 15  |     | Signal           |     |     | Signal           |
| --- | --- | ---------------- | --- | --- | ---------------- |
|     |     | None (n=603,587) |     |     | None (n=603,587) |
|     |     | Self (n=319,688) | 1.0 |     | Self (n=319,688) |
10
|     |     | TP (n= 36,754) |     |     | TP (n= 36,754) |
| --- | --- | -------------- | --- | --- | -------------- |
0.5
5
0.0
0
| -3 -2 -1 | 0 1 2      | 3   | -3 -2 -1 | 0 1 2      | 3   |
| -------- | ---------- | --- | -------- | ---------- | --- |
|          | Reputation |     |          | Reputation |     |
Fig.S3. Revenueandmarginbysignaltypeandsellerreputation: conditionalversusexpected. (A)Unitsaleprice(USD)con-
ditional on sale, by signal type (None, Self-graded, TP-graded): linear mixed-effects model (lmer) with seller random effects.
(B) Margin (sale price − market reference price) conditional on sale: lmer with seller random effects. (C) Expected revenue
= P(sold)×E[price | sold]: two-part model combining glmer (sale probability) and lmer (conditional price). (D) Expected
margin=P(sold)×E[margin|sold]:two-partmodelcombiningglmer(saleprobability)andlmer(conditionalmargin).
32

| F Continuous | Regime | Boundary | in Reputation–Value |     | Space |
| ------------ | ------ | -------- | ------------------- | --- | ----- |
Here, we show that the regime partition reported in the main text has a continuous empirical foundation. The
structural regime map estimated from the HBM (Fig. 2B), the certification boundary V¯(ρ)+V (Fig. 4), and
the discrete 5×5 heatmap of empirical TP shares (Fig. 5) all summarize the same partition at different levels
of aggregation. We now visualize the continuous boundary underlying these representations (fig. S4). Panel A
isascatterplotofself-graded(blue)andTP-graded(red)listingsinthespaceofthesellerreputationscoreand
the log ungraded market price. TP-graded listings concentrate between reputation scores of −1 and 0.5 across
thefullpricerange,whileself-gradedlistingsdominateaboveareputationscoreof0.5atlowtomediumprices.
Panel B overlays the predicted P(TP | graded) surface with the logistic boundary (50% contour) in the same
coordinates. Atthis 50%contour, aone-unitincrease intheseller reputationscoreraises thepricethreshold at
which TP certification becomes the preferred signal by a factor of exp(0.24) ≈ 1.27. This descriptive slope
agreeswiththeHBMsignal-selectioncoefficients,whichimply0.236atmeanreputation(TableS2)andarange
of0.210to0.264acrosstheobservedreputationrange.
| A                                          |             |           | B                         |     |     |
| ------------------------------------------ | ----------- | --------- | ------------------------- | --- | --- |
| Gradingsignalchoiceinreputation–valuespace |             |           | P(TP|graded)regimesurface |     |     |
| Signal                                     | Self-graded | TP-graded |                           |     |     |
P(TP | graded)
$1,000 100%
$1,000
| )DSU( ecirp tekram dedargnU |     |     | )DSU( ecirp tekram dedargnU |     |     |
| --------------------------- | --- | --- | --------------------------- | --- | --- |
75%
log(price)=4.18+0.24×reputation
$100
$100
50%
$10
$10 25%
0%
| $1    |            |     | $1    |            |     |
| ----- | ---------- | --- | ----- | ---------- | --- |
| -3 -2 | -1 0       | 1 2 | -3 -2 | -1 0       | 1 2 |
|       | Reputation |     |       | Reputation |     |
Fig.S4. Continuous regimeboundaryinreputation–value space. (A)Scatterplotof self-graded(blue; n = 10,000, randomly
sampledfromtheanalysissample)andTP-graded(red;n=10,000,randomlysampled)listingsinthespaceofthesellerreputation
score and the ungraded market price (log scale). (B) P(TP | graded) regime surface: predicted probabilities displayed as a
continuouscolorgradientfromblue(P ≈0%)tored(P ≈100%).Theblacklineshowsthelogisticboundarylog(marketprice)=
4.18+0.24×(reputationscore)separatingtheSelf-dominantfromtheTP-dominantregion.
33

| G MCMC | Convergence | Diagnostics |     |     |
| ------ | ----------- | ----------- | --- | --- |
Here, we report convergence diagnostics for the hierarchical Bayesian model. We examine the potential scale
reduction factor Rˆ together with bulk and tail effective sample sizes (ESS). Table S1 lists all three for each of
Rˆ
the38parameters. rangesfrom1.000to1.013andbulkESSfrom221to3,883. Bothextremesoccurforthe
random-effectssold–signalcorrelationΩ ,whichisnotamongthequantitiesreportedinthemaintext. Together
23
theseindicatethattheeightchainsmixedandexploredtheposterioradequately.
TableS1.Convergencediagnosticsforall38parametersofthehierarchicalBayesianmodel.
|     | Parameter |     | Rˆ        |           |
| --- | --------- | --- | --------- | --------- |
|     |           |     | ESS(bulk) | ESS(tail) |
Intercepts
|     | PriceIntercept(αprice) |     | 1.002 1126 | 2131 |
| --- | ---------------------- | --- | ---------- | ---- |
|     | SoldIntercept(αsold)   |     | 1.001 3132 | 3672 |
SignalSelection
|     | Intercept(α),Self-graded              |     | 1.008 1238 | 1973 |
| --- | ------------------------------------- | --- | ---------- | ---- |
|     | Intercept(α),TP-graded                |     | 1.002 1928 | 2155 |
|     | Reputation(γ),Self-graded             |     | 1.006 1525 | 2644 |
|     | Reputation(γ),TP-graded               |     | 1.003 2022 | 2764 |
|     | MarketPrice(δ),Self-graded            |     | 1.000 3382 | 3536 |
|     | MarketPrice(δ),TP-graded              |     | 1.000 3267 | 3472 |
|     | Reputation×MarketPrice(ψ),Self-graded |     | 1.002 3479 | 3771 |
|     | Reputation×MarketPrice(ψ),TP-graded   |     | 1.000 3433 | 3653 |
|     | JapaneseCard(ζ),Self-graded           |     | 1.002 3649 | 3677 |
|     | JapaneseCard(ζ),TP-graded             |     | 1.000 3381 | 3608 |
PriceEquation
|     | Reputation(β1)             |     | 1.002 934  | 1747 |
| --- | -------------------------- | --- | ---------- | ---- |
|     | JapaneseCard(β2)           |     | 1.000 3397 | 3326 |
|     | Reputation×Self-graded(β3) |     | 1.002 3645 | 3752 |
|     | Reputation×TP-graded(β4)   |     | 1.002 3883 | 3861 |
|     | ReturnsAccepted(β5)        |     | 1.001 2797 | 3359 |
Self-graded(βsignal)
|     |                    |     | 1.000 3372 | 3446 |
| --- | ------------------ | --- | ---------- | ---- |
|     | TP-graded(βsignal) |     | 1.001 3092 | 3670 |
SoldEquation
|     | Reputation(β1)             |     | 1.001 1715 | 2827 |
| --- | -------------------------- | --- | ---------- | ---- |
|     | Self-graded(β2)            |     | 1.004 1330 | 2855 |
|     | TP-graded(β3)              |     | 1.002 2570 | 3285 |
|     | JapaneseCard(β4)           |     | 1.001 3542 | 3576 |
|     | ReturnsAccepted(β5)        |     | 1.001 2736 | 3543 |
|     | PriceRatio(log)(β6)        |     | 1.000 3208 | 3347 |
|     | ListingDuration(log)(β7)   |     | 1.001 3460 | 3469 |
|     | Reputation×Self-graded(β8) |     | 1.001 2525 | 3481 |
|     | Reputation×TP-graded(β9)   |     | 1.001 3446 | 3233 |
Variance/Structural
|     | PriceResidualSD(σprice)  |     | 1.002 3872 | 3388 |
| --- | ------------------------ | --- | ---------- | ---- |
|     | PriceRESD(σu1            | )   | 1.012 798  | 1617 |
|     | SoldRESD(σu2             | )   | 1.005 1172 | 2093 |
|     | SignalRESD(σu3           | )   | 1.002 1287 | 2182 |
|     | PriceICC                 |     | 1.012 831  | 1579 |
|     | SoldICC                  |     | 1.005 1172 | 2093 |
|     | TPFactorLoading(λTP)     |     | 1.000 3020 | 3513 |
|     | RECorr:Price–Sold(Ω12)   |     | 1.002 1383 | 2248 |
|     | RECorr:Price–Signal(Ω13) |     | 1.005 822  | 1459 |
|     | RECorr:Sold–Signal(Ω23)  |     | 1.013 221  | 532  |
34

| H   | HBM Model | Fit |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Here,weassessthepredictivefitofthethree-equationhierarchicalBayesianmodel,complementingtheconver-
gencediagnosticsintableS1. Wefindthatthemodelachievesadequateperformanceineachequation,namely
(R2
signal selection (Cohen’s κ = 0.584), log price ratio prediction = 0.421), and sale classification (AUC
=0.954). FigureS5showsthatposteriorpredictiveaccuracyexceedstheempiricalbaserateforallthreesignal
categories (panel A); the confusion matrix is dominated by the diagonal, and most off-diagonal mass falls be-
tweenNoneandSelf(panelB);theobserved-versus-predictedscatterforthelogpriceratioshowsslightlywider
residualsathigh-priceTP-gradedlistings(panelC);thecalibrationplotforsaleprobabilityhasaslopecloseto
unity(panelD);andtheROCcurveconfirmsstrongdiscriminationforthesaleoutcome(panelE).
A SignalPPC:P(actualcategory) B Signalclassification:confusionmatrix
|     | None |     | Self |     | TP  |     |     |     |
| --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
1.5
| 4   |     |     |     |     |     | TP 0.290 | 0.583 0.126 |     |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | --- |
3
Proportion
| 3       |     | 1.0 |     |     |     |            |             | 1.00 |
| ------- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- |
| ytisneD |     |     |     |     |     | lautcA     |             |      |
|         |     |     |     | 2   |     |            |             | 0.75 |
|         |     |     |     |     |     | Self 0.275 | 0.719 0.006 |      |
| 2       |     |     |     |     |     |            |             | 0.50 |
|         |     | 0.5 |     |     |     |            |             | 0.25 |
1
| 1   |     |     |     |     |     |            |             | 0.00 |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- |
|     |     |     |     |     |     | None 0.887 | 0.108 0.004 |      |
| 0   |     | 0.0 |     | 0   |     |            |             |      |
0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00 None Self TP
|     |     | P(actual category) |           |     |     |     | Predicted |     |
| --- | --- | ------------------ | --------- | --- | --- | --- | --------- | --- |
|     |     | Category           | None Self | TP  |     |     |           |     |
C PricePPC:observedvs.predicted D Soldequation:calibration E Soldequation:ROCcurve
|                   |     |     | 1.00               |     |     | 1.00 |     |     |
| ----------------- | --- | --- | ------------------ | --- | --- | ---- | --- | --- |
| )gol( detciderP 3 |     |     | etar devresbO 0.75 |     |     | 0.75 |     |     |
N
|     |     | Signal |     |     |     | ytivitisneS |     |     |
| --- | --- | ------ | --- | --- | --- | ----------- | --- | --- |
2
|     |     |     | None |     |     | 2000      |     |     |
| --- | --- | --- | ---- | --- | --- | --------- | --- | --- |
|     |     |     | 0.50 |     |     | 4000 0.50 |     |     |
| 1   |     |     | Self |     |     |           |     |     |
|     |     |     | TP   |     |     | 6000      |     |     |
AUC = 0.954
| 0   |     |     | 0.25 |     |     | 0.25 |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- |
-1
| -2  | 0 2 | 4   |      |     |     |      |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- |
|     |     |     | 0.00 |     |     | 0.00 |     |     |
Observed (log)
|     |     |     |     | 0.00 0.25 0.50    | 0.75 1.00 | 0.00 | 0.25 0.50 0.75 1.00 |     |
| --- | --- | --- | --- | ----------------- | --------- | ---- | ------------------- | --- |
|     |     |     |     | Predicted P(sold) |           |      | 1 - Specificity     |     |
Fig. S5. HBM model fit and predictive diagnostics across three equations. Row 1: (A) Posterior predictive check for signal
selection: density of P(correctcategory) by certification type. Dashed lines indicate empirical base rates; all three categories
exceedtheirrespectivebaserates,indicatingdiscriminativeability.(B)Confusionmatrixheatmapforsignalselectionpredictions.
Overallaccuracy=0.803,balancedaccuracy=0.577,Cohen’sκ=0.584.Row2:(C)Observedversuspredictedlogpriceratio.
R2 =0.421,RMSE=0.820,normalizedRMSE=0.762. Residualdistributionsaresimilaracrosssignaltypes. (D)Calibration
plotforsalepredictions:binnedmeanpredictedP(sold)versusobservedsalerate.Calibrationslope=1.111.(E)ROCcurvefor
salepredictions.AUC=0.954[95%CI:0.948,0.960].
35

| I Full | Coefficient | Estimates |     |     |
| ------ | ----------- | --------- | --- | --- |
TableS2reportsthecompleteposteriorestimatesforall38modelparameters,withtheprice-equationinteraction
coefficientsconstitutingthestructuralcoreofthemain-textargument. ThemodelwasimplementedinStanwith
eight chains (1,000 warm-up + 1,000 sampling iterations, thinning = 2, step-size adaptation target = 0.95,
maximumtreedepth= 12). Allestimatesarereportedasposteriormedianswith95%credibleintervals(2.5th
and97.5thpercentiles).
TableS2.FullposteriorestimatesofthehierarchicalBayesianmodel.
|     |     | Parameter |     | Estimate[95%CI] |
| --- | --- | --------- | --- | --------------- |
Intercepts
|     |     | PriceIntercept(αprice) |     | 0.853[0.846,0.861] |
| --- | --- | ---------------------- | --- | ------------------ |
|     |     | SoldIntercept(αsold)   |     | 5.091[5.032,5.148] |
SignalSelection
|     |     | Intercept(α),Self-graded |     | -0.497[-0.524,-0.469] |
| --- | --- | ------------------------ | --- | --------------------- |
|     |     | Intercept(α),TP-graded   |     | -4.140[-4.180,-4.102] |
Reputation(γ),Self-graded
0.054[0.031,0.077]
|     |     | Reputation(γ),TP-graded    |     | -0.052[-0.083,-0.020] |
| --- | --- | -------------------------- | --- | --------------------- |
|     |     | MarketPrice(δ),Self-graded |     | -0.252[-0.259,-0.244] |
MarketPrice(δ),TP-graded
0.505[0.495,0.515]
|     |     | Reputation×MarketPrice(ψ),Self-graded |     | 0.044[0.037,0.049] |
| --- | --- | ------------------------------------- | --- | ------------------ |
|     |     | Reputation×MarketPrice(ψ),TP-graded   |     | 0.028[0.020,0.037] |
|     |     | JapaneseCard(ζ),Self-graded           |     | 0.087[0.065,0.107] |
|     |     | JapaneseCard(ζ),TP-graded             |     | 1.008[0.979,1.038] |
PriceEquation
|     |     | Reputation(β1)             |     | 0.001[-0.006,0.007]   |
| --- | --- | -------------------------- | --- | --------------------- |
|     |     | JapaneseCard(β2)           |     | -0.503[-0.510,-0.497] |
|     |     | Reputation×Self-graded(β3) |     | 0.063[0.058,0.069]    |
|     |     | Reputation×TP-graded(β4)   |     | -0.095[-0.110,-0.080] |
|     |     | ReturnsAccepted(β5)        |     | 0.026[0.020,0.032]    |
|     |     | Self-graded(βsignal)       |     | 0.093[0.086,0.100]    |
|     |     | TP-graded(βsignal)         |     | -0.197[-0.213,-0.180] |
SoldEquation
|     |     | Reputation(β1)           |     | 0.457[0.427,0.488]    |
| --- | --- | ------------------------ | --- | --------------------- |
|     |     | Self-graded(β2)          |     | 0.102[0.065,0.138]    |
|     |     | TP-graded(β3)            |     | 0.026[-0.062,0.115]   |
|     |     | JapaneseCard(β4)         |     | -0.380[-0.414,-0.348] |
|     |     | ReturnsAccepted(β5)      |     | -0.256[-0.289,-0.220] |
|     |     | PriceRatio(log)(β6)      |     | -0.951[-0.964,-0.939] |
|     |     | ListingDuration(log)(β7) |     | -1.654[-1.666,-1.643] |
Reputation×Self-graded(β8)
-0.077[-0.109,-0.045]
|     |     | Reputation×TP-graded(β9) |     | 0.094[0.018,0.170] |
| --- | --- | ------------------------ | --- | ------------------ |
Variance/Structural
|     |     | PriceResidualSD(σprice)  |     | 0.838[0.837,0.840]    |
| --- | --- | ------------------------ | --- | --------------------- |
|     |     | PriceRESD(σu1            | )   | 0.638[0.632,0.645]    |
|     |     | SoldRESD(σu2             | )   | 1.847[1.816,1.877]    |
|     |     | SignalRESD(σu3           | )   | 2.110[2.081,2.139]    |
|     |     | PriceICC                 |     | 0.367[0.362,0.372]    |
|     |     | SoldICC                  |     | 0.509[0.501,0.517]    |
|     |     | TPFactorLoading(λTP)     |     | 0.919[0.911,0.926]    |
|     |     | RECorr:Price–Sold(Ω12)   |     | -0.015[-0.036,0.004]  |
|     |     | RECorr:Price–Signal(Ω13) |     | -0.139[-0.153,-0.125] |
|     |     | RECorr:Sold–Signal(Ω23)  |     | 0.019[0.001,0.038]    |
36

| J Signal |     | Composition |     | Across | Price | and | Reputation | Dimensions |     |     |     |
| -------- | --- | ----------- | --- | ------ | ----- | --- | ---------- | ---------- | --- | --- | --- |
Here, we examine how signal composition varies along the price and reputation dimensions separately. We
disaggregate the 5 × 5 heatmap of Fig. 5 into marginal distributions by price quintile and reputation quintile
(fig.S6). PanelAshowsthepricedistributionasaunimodalhistogrampeakingat$1–$3withalongrighttail;
panel C shows the reputation distribution as a bimodal histogram with a low-reputation cluster at reputation
scoresof−1to0andahigh-reputationclusterat0.5to1.5. Thesignal-compositionbarsrevealanasymmetric
pattern. Alongthepriceaxis(B),TPgradingrisesmonotonicallyfrom0.3%inthelowestquintileto12.2%in
thehighest, aroughly40-foldincrease, whileself-gradingremainsflat(25%–35%)andNonecontracts. Along
the reputation axis (D), self-grading rises modestly from 28.7% to 35.4%, TP grading declines from 5.6% to
2.2%, and None again contracts. Variation in the TP share is therefore driven mainly by price (range ≈ 11.9
percentage points), and variation in the Self share mainly by reputation (≈ 6.7 percentage points). Together
thesetwopatternssupportthetwo-dimensionalregimestructure.
A
| Pricedistribution |     |     |     |     |     | B Signalmix×pricetier |     |        |      |         |     |
| ----------------- | --- | --- | --- | --- | --- | --------------------- | --- | ------ | ---- | ------- | --- |
|                   |     |     |     |     |     |                       |     | Signal | None | Self TP |     |
)%( egatnecreP
100
|     | Q1  | Q2Q3 | Q4  |     | Q5  |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
75
50
90000
25
0
| tnuoC |     |     |     |     |     |     | Q1  | Q2  | Q3  | Q4  | Q5  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
60000
Price quintile
)%( etar PT
12.2%
| 30000 |     |     |     |     |     | 15  |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
3.8%
|     |     |                             |      |       |         | 5   | 0.3% | 1.1% | 1.7%           |     |     |
| --- | --- | --------------------------- | ---- | ----- | ------- | --- | ---- | ---- | -------------- | --- | --- |
| 0   |     |                             |      |       |         | 0   |      |      |                |     |     |
|     | 0.1 | 1.0                         | 10.0 | 100.0 | 1,000.0 |     | Q1   | Q2   | Q3             | Q4  | Q5  |
|     |     | Ungraded market price (USD) |      |       |         |     |      |      | Price quintile |     |     |
C
| Reputationdistribution |     |     |     |     |     | D Signalmix×reputationtier |     |        |      |         |     |
| ---------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | ------ | ---- | ------- | --- |
|                        |     |     |     |     |     |                            |     | Signal | None | Self TP |     |
)%( xim langiS
100
|     |     | Q1  |     | Q2 Q3 | Q4 Q5 | 75  |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
50
75000
25
0
| tnuoC |     |     |     |     |     |     | Q1  | Q2  | Q3  | Q4  | Q5  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50000
Reputation quintile
)%( etar langiS
|       |     |     |     |     |     | 50  |       | 33.6% | 33.2% | 35.6% | 35.4% |
| ----- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | ----- | ----- |
| 25000 |     |     |     |     |     | 40  | 28.7% |       |       |       |       |
30
|     |     |     |     |     |     | 20  | 5.6% | 5.2% | 3.5% | 2.6% | 2.2% |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- |
10
0
0
|     |     | -2               | 0   |     | 2   |     | Q1  | Q2                  | Q3  | Q4  | Q5  |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
|     |     | Reputation score |     |     |     |     |     | Reputation quintile |     |     |     |
Fig. S6. Empirical distributions and signal composition across price and reputation dimensions. (A) Distribution of ungraded
marketprices(N = 960,029): log-scalehistogram(y-axis: listingcount)withquintileboundaries. (B)Signalcompositionby
marketpricebracket: 100%stackedbarchart. (C)Distributionofsellerreputationscores: histogram(y-axis: listingcount)with
quintileboundaries.(D)Signalcompositionbyreputationbracket.
37
---- END DOCUMENT ----
