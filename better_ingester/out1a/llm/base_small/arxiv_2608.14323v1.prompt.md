Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Dependence-Informed Sparse Neural Architecture for Stock
Return Prediction
HongyuLin YulinChen YuanrongWang
UniversityCollegeLondon UniversityCollegeLondon UniversityCollegeLondon
London,UnitedKingdom London,UnitedKingdom London,UnitedKingdom
AntonioBriola TomasoAste
UniversityCollegeLondon UniversityCollegeLondon
London,UnitedKingdom London,UnitedKingdom
Abstract investment,andprofitabilityexhibitsubstantialempiricaldepen-
Usingneuralnetworksforstockreturnpredictiontypicallyrequires dence[8,20].Toobtainasparserepresentationoftheserelation-
choicesaboutdepthandhidden-layerwidththataredifficulttocon- ships,weapplyInformationFilteringNetworks(IFNs)tothetrain-
necttofinancialinterpretation.Westudyanalternative:estimate ingdata.IFNsfilteradensedependencematrixundertopological
dependenceamongfirmcharacteristicswithaMaximallyFiltered constraints[22,24,29].Specifically,theMaximallyFilteredClique
CliqueForest(MFCF),thenmapitscliquestructuretoaHomologi- Forest(MFCF)organizestheretainedrelationshipsintocliquesof
calNeuralNetwork(HNN).TheMFCFmaximumcliquesize𝐾 is boundedsizewhilepreservinggraphdecomposability[23].AHo-
theonlyparametercontrollingarchitecturalcomplexity,andithas mologicalNeuralNetwork(HNN)mapsthesecliquestoaneural
acleargraphicalmeaning:itboundsthenumberofcharacteristics architecture:characteristicsformtheinputlayer,retainedpairs
ineachmaximalcliqueandhencethehighestinteractionorder formthesecond-orderlayer,largersubsetsformsubsequentlayers,
thenetworkcanrepresent.Thefilteredgraphthenfixestheneural andconnectionsfollowsetinclusion[21,31].Thenumberoflayers
network’sdepth,layerwidths,andsparseconnectionsbeforetrain- isthereforethehighestinteractionorderthefilteredgraphattains,
ing,inplaceofaseparatelychosendepthandwidthsequence.We ratherthanacapacitysettingchoseninadvance.Aconventional
applytwoHNNvariantstoannualout-of-sampleforecastsofU.S. MLPusesfullyconnectedlayersandmayapply𝑙 1 regularizationto
stockexcessreturnsfrom1987to2016using94firmcharacteristics. reducetheinfluenceofunhelpfulconnections[12,28].Incontrast,
TheHNNmodelsmatchathree-hidden-layerbenchmarkonpooled theHNNissparsebyconstruction:MFCFdetermineswhichconnec-
predictiveaccuracy,rankthecross-sectionmoreaccurately,anduse tionsareincludedbeforethenetworkistrained.Thisarchitecture
roughly80timesfewerparametersthanafullyconnectednetwork followsthecompositionalviewthathigh-dimensionalfunctions
withthesameinducedlayerwidths.Twostructuralablationsindi- canbeassembledfromlower-dimensionalconstituents[27].
catethatboththesparseconnectivityandtheestimatedgrouping WeevaluatethisapproachusingtheGKXsampledesign[12]and
ofcharacteristicscontributetotherankingadvantage,andbothef- 94rankedfirmcharacteristicstopredictsubsequentmonthlyexcess
fectsremainsignificantaftercorrectingformultipletesting.These returns.WeconsidertwoHNNvariants:HNN(marginal),which
findingsshowthatHNNsofferapracticalandinterpretablewayto constructsthenetworkusingdependenceamongcharacteristics
incorporateestimateddependenceamongfirmcharacteristicsinto alone,andHNN(m-s),whichalsousestrainingreturnstodistin-
neuralarchitecturedesign. guishbetweenabove-andbelow-medianobservations.Bothare
comparedwithNN3[12],acompactthree-hidden-layernetwork
thatperformsbestamongthemodelsGKXevaluate,adaptedto
1 Introduction
thesameinformationset.Forablationstudies,aninput-shuffling
Machine learning allows empirical asset-pricing models to cap- HNNtestswhetherthealignmentofcharacteristicswiththeMFCF-
tureabroadrangeofnonlinearrelationships.Gu,Kelly,andXiu derivedgraphmatters,whileafullyconnectednetworkwiththe
(GKX)[12]showthatneuralnetworksandtree-basedmodelsout- sameinducedlayerwidthsprovidesadensearchitecturalcompar-
performlinearalternativesinforecastingcross-sectionalreturns, ison.Evaluationcoversbothlevelpredictionandcross-sectional
suggestingthathigher-orderinteractionsamongfirmcharacteris- ranking.Wemeasurerankingwithinformationcoefficients(ICs)
ticscontainusefulpredictiveinformation.Relatedstudiesdevelop andreturnsfromprediction-sortedportfolios.ThePearsonand
characteristic-basedlatentfactormodels[17],nonlinearautoen- SpearmanICsaremonthlycross-sectionalcorrelationsbetween
coderanddeep-learningasset-pricingmodels[3,13],regularizedap- predictedandrealizedreturns.SpearmanICmeasurestheorder-
proachestothecross-section[20],nonparametriccharacteristicse- ingofstocks,whereasPearsonICalsoreflectsthelinearassoci-
lection[9],andtestsforidentifyingincrementalpricingfactors[8]. ationbetweenthemagnitudesofpredictedandrealizedreturns.
Yetusingamultilayerperceptron(MLP)stillrequiresresearchers Prediction-sortedportfoliostestwhetherthiscross-sectionalorder-
tospecifyitsdepthandhidden-layerwidths.Thesechoicesaregen- ingproduceseconomicallymeaningfulreturnseparation.
erallyselectedthroughvalidationandhavelimiteddirectfinancial Thestudymakesthreeempiricalcontributions.First,bothHNN
interpretation[6]. variantsachievenumericallyhigherpooledout-of-sample𝑅2than
We investigate whether a neural architecture can instead be NN3,andHNN(marginal)attainsthehighestPearsonICandequal-
constructedfromestimateddependenceamongfirmcharacteris- weightedportfoliospreadofanymodelweconsider,togetherwith
tics. Characteristics related to valuation, past returns, liquidity,
6202
guA
41
]TS.nif-q[
1v32341.8062:viXra

HongyuLin,YulinChen,YuanrongWang,AntonioBriola,andTomasoAste
thehighestSpearmanICamongtheneuralmodels.Second,against filteredstructurebecomesthemodelitself,withthecliquesand
afullyconnectednetworkmatchedonhidden-layerwidths,the theirsubsetsasneuralunits[31];laterworkframesthisascom-
HNNreducestheparametercountbyafactorof80whileimprov- positionalsparsityandshowsthat,withthemaximumcliquesize
ingbothinformationcoefficientsandtheequal-weightedspread. heldfixed,itmatchesoroutperformsfullyconnectednetworkson
Third,randomlypermutingtheinputcharacteristicswiththear- tabularregressionwithfarfewerconnections[21].Thisevidence
chitectureandcapacityheldfixedweakenscross-sectionalranking, comesfromproblemswithfarmoresignalthanthereturncross-
sothealignmentbetweencharacteristicsandtheirinferredclique section,andwhetherastructureestimatedfromthecharacteristics
structurecontributesbeyondsparsityalone.AfterHolmadjustment alonecarriespredictiveinformationhereisuntested.Weapplythe
formultiplecomparisons[15],thePearsonICdifferencesremain constructiontoafinancialpanel,selectthecliquesizebyvalidation
significant,whileon𝑅2,SpearmanIC,andportfoliospreadHNN ineachwindowsothatdepthfollowsfromthedata,andassessthe
(marginal)andNN3arestatisticallyindistinguishable. forecastsbyportfolioreturnsaswellassquarederror.
Theremainderofthepaperisorganizedasfollows.Section2
reviewsmachinelearninginassetpricingandpriorworkonfiltered 3 Method
networks and structured neural models. Section 3 develops the 3.1 PredictionTargetandCharacteristic
HNNconstruction,andSection4describesthedata,walk-forward
Dependence
protocol,benchmarks,andevaluationprocedure.Section5reports
predictiveaccuracy,cross-sectionalranking,parameterefficiency, Let𝑥 𝑖,𝑡 ∈R𝑝 collectthe𝑝firmcharacteristicsofstock𝑖atmonth𝑡.
transaction-costsensitivity,andstabilityovertime.Sections6and7 Thepredictiontargetisthestock’sexcessreturnoverthefollowing
discusslimitationsandconclude. month,
2 RelatedWork
𝑦
𝑖
𝑒
,𝑡+1
=𝑅 𝑖,𝑡+1−𝑅
𝑡
𝑓
+1
, 𝑦
(cid:98)𝑖
𝑒
,𝑡+1
=𝑓
𝜃,A
(𝑥 𝑖,𝑡), (1)
Machine learning in asset pricing. GKX [12] compare a wide
where𝑅
𝑖,𝑡+1
istherealizedreturnonstock𝑖inmonth𝑡+1,𝑅
𝑡
𝑓
+1
is
theone-monthrisk-freerate,𝜃 containsthetrainableparameters,
rangeofmethodsonalargeU.S.equitypanelandfindthatflexible
andAdenotesthenetworkarchitecture.
nonlinearmodelsimproveout-of-samplereturnprediction,partly
The architecture is estimated from dependence among firm
bycapturinginteractionsamongpredictors.Freybergeretal.[9]use
characteristics.LetX ∈ R𝑁×𝑝 containthe𝑁 observationsofthe
regularizationfornonparametriccharacteristicselection,andKozak
currenttrainingwindow,andlet𝑋 denoteits𝑎-thcolumn,one
etal.[20]combineshrinkagewithprincipal-componentstructure. 𝑎
percharacteristic.Thecharacteristicsarethenodesofthegraph,
Relatedlatent-factormodelsusecharacteristicstoparameterize
V ={1,...,𝑝},andtheresultingnetworkisfixedacrossallfirms
time-varyingfactorexposures[17];conditionalautoencodersmake
anddates.ThefiltertakesasinputtheabsolutePearsoncorrelation
thoseexposuresnonlinearinthecharacteristics[13];andChen
matrix
etal.[3]fitnonlinearmodelssubjecttono-arbitragerestrictions.
Wherethesepapersuseaneuralnetwork,itsdepthandwidthsare
𝐷
𝑎𝑏
=|corr(𝑋
𝑎
,𝑋 𝑏)|, 𝑎,𝑏 ∈V. (2)
chosenbyhand. Linear correlation is used rather than a more general depen-
Theflexibilityofthesemethodsincreasestheimportanceofreg- dencemeasure.Becausethecharacteristicsenterascross-sectional
ularization,modelselection,andcarefulout-of-sampleevaluation, ranks, Equation (2) is a correlation between rank variables and
particularlywhensignalsareweakanddifferencesacrossmodels isthereforeinsensitivetooutliersandtomonotonetransforma-
aremodest.Workonfactorselectionandmultipletestingfurther tionoftheunderlyingcharacteristic[18].Italsoavoidstheextra
motivatesdisciplinedcomparisons[8,14].Accordingly,weusea tuningthatmeasuressuchasmutualinformation[4]require,and
commoninformationsetandwalk-forwardprotocolacrossmod- richermeasurescanbesubstitutedwithoutchangingtherestof
els,togetherwithmultiplicity-adjustedinference[15]forthemain theconstruction[21].
architecturecomparisons. TheMFCFfilters𝐷intooverlappingcharacteristiccliqueswhile
preservingadecomposablegraphstructure[23].Ateachstep,a
Filtered networks and Homological Neural Networks. Informa- characteristic𝑣 ∈ V notyetinthegraphisattachedthroughan
tionFilteringNetworksextractasparsenetworkofthestrongest admissibleseparator𝑆,meaningacliqueofthecurrentgraphwhose
relationshipsfromadensedependencematrix[24,29].Sparsity extensionpreservesdecomposability,formingthenewclique𝑆∪{𝑣}.
comesfromaglobalcriterionappliedunderaconstraintonthe Theattachmentisscoredby
graph topology, rather than from penalizing edges individually. 𝐺(𝑣,𝑆)= ∑︁ 𝐷2 . (3)
Thechoiceofconstraintdecideshowmuchhigher-orderstructure 𝑣𝑢
survives:aspanningtreecontainsnocliquelargerthanapair[22], 𝑢∈𝑆
Repeatedlyselectingthelargestadmissiblegainproducesacollec-
whileplanarandchordalfiltersretaintrianglesandlargercliques.
TheMaximallyFilteredCliqueForest[23]isofthelatterkindand
tionofmaximalcliquesC.Unlikesparseprecisionmatrixestimators
suchasthegraphicallasso[10],whichidentifypairwiseconditional
returnsaforestofoverlappingcliquesofboundedsize.
dependenceedges,theMFCFyieldsafilteredgraphwhosemaximal
Filterednetworkshavebeenusedbeforetostudyandforecast
cliquesdefineoverlappinggroupsofcharacteristics.Inourimple-
financialdependence.WangandAste[30],forexample,builda
mentation,theonlystructuralparameteristhemaximumclique
filteredgraphanduseitastheadjacencystructureofaspatial-
sizeK,whichimposes
temporalgraphneuralnetwork,sothegraphisaninputtoamodel
chosenseparately.IntheHomologicalNeuralNetwork(HNN)the |𝐶|≤𝐾 forevery𝐶 ∈C.

Dependence-InformedSparseNeuralArchitectureforStockReturnPrediction
ThecandidatevaluesconsideredforKarereportedinSection4. 3.3 HNNVariantsandStructuralControls
Thetwovariantsusetheconstructionaboveanddifferonlyinthe
3.2 Clique-InducedNeuralArchitecture
dependencematrixsuppliedtoMFCF.
Figure1illustrateshowtheMFCFistranslatedintoanHNN[21,
|     |     |     |     |     |     |     |     | HNN(marginal). | Themarginalspecificationestimatesasingle |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------------------------------- | --- | --- | --- |
31].Thecliquesandtheirsubsetsbecometheneuralunitsofthe
dependencematrixfromallobservationsinthetrainingwindow.
network,andsetinclusionbecomesitsconnectivity.
Returnsarenotused,sothearchitecturedependsonlyonthechar-
|     | Since𝐾 | isanupperbound,thehighestorderthefilteredgraph |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
acteristics.
actuallyreachesis
𝐾★=max|𝐶|≤𝐾. HNN (m-s). The median-split specification splits the training
(4)
|     |     |     |     | 𝐶∈C |     |     |     | observationsatthemedianexcessreturn.Adependencematrix |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
LetH(𝑘)
collectthedistinctorder𝑘interactionsthefilterretains: andanMFCFareestimatedwithineachsubsample,givingclique
collectionsC+andC−,andthenetworkisbuiltfromtheirunion,
|     | H(𝑘)   | ={𝛼          | ⊆V :|𝛼|=𝑘, |         | 𝛼 ⊆𝐶forsome𝐶    | ∈C}.        | (5) |     |     |          |     |      |
| --- | ------ | ------------ | ---------- | ------- | --------------- | ----------- | --- | --- | --- | -------- | --- | ---- |
|     |        |              |            |         |                 |             |     |     |     | C=C+∪C−. |     | (10) |
| A   | subset | that appears | in         | several | maximal cliques | contributes | a   |     |     |          |     |      |
∈H(𝑘),solayer1holds Equation(5)thenappliesunchanged,soasubsetoccurringinboth
singleunit.Layer𝑘hasoneunitforeach𝛼
collectionsstillcontributesasingleunit.Validationandtestreturns
theindividualcharacteristics,layer2theretainedpairs,andlater
| layerscontainprogressivelylargercliques.Itswidth𝑛 |     |     |     |     |     | =|H(𝑘)|is |     | areneverused. |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | --- | --- | --- |
𝑘
determinedbythefilteredgraphratherthanchosen,and𝐾bounds ThetwocontrolsstartfromHNN(marginal):thefirstbreaks
thenumberoflayers,nottheirwidths. thealignmentbetweencharacteristicsandtheMFCF-derivedarchi-
|     |                                        |     |     |     |     | H(𝑘)       |     | tecture,thesecondreplacesthesparseHNNwithawidth-matched |     |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | ---------- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
|     | Connectionsfollowinclusion:theunitfor𝛼 |     |     |     |     | ∈ receives |     |                                                         |     |     |     |     |
densearchitecture.
inputonlyfromtheunitsforitssubsetsofsize𝑘−1.Characteristics
thereforeinteractonlywhenthefilterplacestheminacommon
|              |     |       |                               |     |     |     |     | HNN(input-shuffled). |     | Thisablationpermutesthecharacter- |     |     |
| ------------ | --- | ----- | ----------------------------- | --- | --- | --- | --- | -------------------- | --- | --------------------------------- | --- | --- |
| clique.Withℎ |     | ( 1 ) | =𝑥 ,theactivationsatorder𝑘are |     |     |     |     |                      |     |                                   |     |     |
𝑖 , 𝑡 𝑖,𝑡 isticsacrosstheinputsoftheHNN(marginal)network,withno
|     |       |          |                 |         |                         |            |     | c h a ra c t er | i s ti c l e ft a t i t s | o ri g in a l p l a c | e .T h e s a m e | p e r m u t a ti o n is |
| --- | ----- | -------- | --------------- | ------- | ----------------------- | ---------- | --- | --------------- | ------------------------- | --------------------- | ---------------- | ----------------------- |
|     | ( 𝑘 ) | (cid:16) | (cid:104) 𝑊(𝑘)ℎ | ( 𝑘 −1) | +𝑏(𝑘) (cid:105)(cid:17) | =2,...,𝐾★, |     |                 |                           |                       |                  |                         |
ℎ =ReLU LN 𝑘 , 𝑘 (6) u se d f o r e v e r y o b se r v a t io n i n a t ra i n i n g w in d o w . Si n c e e a c h i n pu t
|     | 𝑖 , 𝑡 |     |     | 𝑖 , 𝑡 |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
correspondstoanodeofthefilteredgraph,thisshufflesthecharac-
| whereℎ | ( 𝑘 | ) ∈ R𝑛𝑘 | holds | the order-𝑘 | activations,𝑏(𝑘) | ∈   | R𝑛𝑘 is |     |     |     |     |     |
| ------ | --- | ------- | ----- | ----------- | ---------------- | --- | ------ | --- | --- | --- | --- | --- |
𝑖 , 𝑡 teristicsacrossthenodeswhileleavingthegraphitselfuntouched:
| abias,LN                           |     | islayernormalization[2],andReLUistherectified |     |     |           |            |     |                                                           |     |     |     |     |
| ---------------------------------- | --- | --------------------------------------------- | --- | --- | --------- | ---------- | --- | --------------------------------------------------------- | --- | --- | --- | --- |
|                                    |     | 𝑘                                             |     |     |           |            |     | thetopology,theneuralunits,theconnections,andtheparameter |     |     |     |     |
| linearunit[25].Theweightmatrix𝑊(𝑘) |     |                                               |     |     | ∈R𝑛𝑘×𝑛𝑘−1 | issparseby |     |                                                           |     |     |     |     |
countstayexactlyasinHNN(marginal),butthecharacteristics
𝑘)
construction:theentry𝑊 ( istrainablewhen𝜏 ⊂𝛼 andfixedat arenolongeralignedwiththeiroriginalnodesintheMFCF.Ca-
|     |     |     |     | 𝛼 𝜏 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
zerootherwise. pacityisunchanged,soadifferenceinperformanceisattributable
Conventionalfeed-forwardnetworkspredictfromthelasthid-
tothatmismatchalone.
denlayer.TheHNNinsteadreadsoutfromeverylayerabovethe
|     |     |     |     |     |     |     |     | MLP-HNN. | This control | keeps HNN | (marginal)’s | depth and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --------- | ------------ | --------- |
input.Eachlayerisfirstsummarizedbyascalar,
layerwidthsbutconnectseverylayerfullyandpredictsfromthe
𝑟(𝑘) =(𝑎(𝑘))⊤ℎ(𝑘) +𝑐(𝑘), 𝑘 =2,...,𝐾★, (7) lastlayerinsteadoffromallofthem.Becauseitsconnectivityand
|     |     | 𝑖,𝑡 |     | 𝑖,𝑡 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
predictionheadfollowaconventionalMLPdesign,itprovidesan
andthesummariesarecombinedtoformtheforecast,
architecturalcomparisonratherthanastrictconnectivityablation.
|     |     |     |                | 𝐾★  |           |     |     | Thewidthsarematchedbuttheparametercountsarenot,soitis |     |     |     |     |
| --- | --- | --- | -------------- | --- | --------- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
|     |     |     | 𝑒              | ∑︁  | ( 𝑘 )     |     |     |                                                       |     |     |     |     |
|     |     |     | 𝑦              | =   | 𝛽 𝑘 𝑟 +𝑑, |     | (8) | substantiallylargerthanHNN(marginal).                 |     |     |     |     |
|     |     |     | (cid:98)𝑖 ,𝑡+1 |     | 𝑖 , 𝑡     |     |     |                                                       |     |     |     |     |
|     |     |     |                | 𝑘=2 |           |     |     | Together,thesefourmodelsanswerthreequestions:whether  |     |     |     |     |
where𝑎(𝑘) ∈R𝑛𝑘 andthescalars𝑐(𝑘),𝛽 and𝑑aretrainable.Every usingreturnstoestimatethegraphhelps(HNN(m-s)againstHNN
𝑘
orderthereforehasadirectpathtotheforecast,whichmatters (marginal)),whethercharacteristicsmustremainalignedwiththe
becauseaunitbelongingtonolargercliquewouldotherwisenever MFCF(HNN(input-shuffled)),andhowtheHNNarchitecture
|     |     |     |     |     |     |     |     | compares | with a conventional | dense | network having | the same |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------- | ----- | -------------- | -------- |
reachtheoutput.Thelinearformalsokeepsthecontributionof
induceddepthandlayerwidths(MLP-HNN).
eachorderseparable.TheMFCFfixestheunitsandtheconnections
beforetraining,sotrainingestimatesonlythenonzeroweights.
|     |                  |     |             |     |                         |     |     | 4 ExperimentalDesign |     |     |     |     |
| --- | ---------------- | --- | ----------- | --- | ----------------------- | --- | --- | -------------------- | --- | --- | --- | --- |
|     | Eachunitatorder𝑘 |     | hasexactly𝑘 |     | incomingconnections,one |     |     |                      |     |     |     |     |
foreachofitssubsetsofsize𝑘−1.TheHNNthereforecarriesfar 4.1 DataandWalk-ForwardProtocol
fewerweightsthanafullyconnectednetworkwiththesamelayer
WeusetheGKXU.S.equitypanelof94firmcharacteristicsand
widths:
monthlystockreturnsfrom1957to2016[12].Returnsaretakenin
𝐾★ 𝐾★ excessofthecontemporaneousrisk-freerate.Withineachmonth
|     |     |     | ∑︁  |     | ∑︁  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑃 sparse= 𝑘𝑛 𝑘 , 𝑃 dense= 𝑛 𝑘−1 𝑛 𝑘 . (9) theobservedcharacteristicsarerankedacrossstocksandmapped
𝑘=2 𝑘=2 to[−1,1],andmissingvaluesaresettozero,theneutralrank.A
Thesparsecountgrowslinearlyinthelayerwidths,whereasthe near-zero-variancescreenappliedtoeachwindow’strainingdata
densecountgrowswiththeirproducts. leaves between 90 and 94 characteristics, so the MFCF decides

HongyuLin,YulinChen,YuanrongWang,AntonioBriola,andTomasoAste
Figure1:Dependence-informedHNNconstruction.MFCFfilterstraining-onlycharacteristicdependenceintooverlapping
cliques.Retainedsubsetsformorderedneuralunits,setinclusiondeterminessparseconnections,andsummariesfromall
non-inputlayersformtheexcess-returnforecast.AdaptedfromLinetal.[21].
howcharacteristicsareconnectedratherthanwhichareavailable. howaneuralarchitectureisspecifiedratherthanwhichfamilyof
Thecorrelationmatrixiscomputedfrom150,000trainingobserva- modelspredictsbest.
tionsdrawnatrandomineachwindow.Thetestsamplecontains AllneuralmodelsaretrainedwithAdam[19]onmeansquared
2,508,749observations. error,withbatchesof10,000,atmost100epochsandgradientclip-
Following GKX [12], the training window starts in 1957 and pingatone.Trainingstopsaftertenepochswithoutvalidationim-
expandsbyoneyearateachstep,thefollowingtwelveyearsserve provementfortheHNNsandfiveforthedensenetworks,theHNNs
asvalidation,andthenextyearisthetestyear.Thefirsttestyear beinggivenlongerbecausethesparsemaskslowsconvergence.
is 1987 and the last 2016, giving 30 non-overlapping test years. Tomitigatethevariationinducedbyrandominitialization,each
Preprocessing,graphconstruction,hyperparameterselectionand forecastaveragestenrunswithdifferentseeds,followingGKX[12].
fittingareredoneineachwindowonthatwindow’strainingand Thismattersherebecausethedifferencesbetweenarchitectures
validationdataalone. aresmallrelativetothatvariation.
WedonotreproduceGKX’sfullspecification:allmodelsstart Hyperparameters are chosen by validation mean squared er-
fromthesame94characteristics,withoutindustrydummiesor roreveryfivetestyearsandheldfortheblock,whilegraphsand
macroeconomic interactions. Fixing the information set means weightsarere-estimatedannually.Table1liststhegrids.HNNsuse
differences in performance can be read as differences in model no𝑙 penalty,sincetheirsparsitycomesfromthegraphratherthan
1
construction. fromshrinkage.Modelselectionisnoteliminatedbutchangesin
kind:asearchoverdepthandwidthsequencesbecomesasearch
4.2 ModelsandSelection overonestructuralparameterandthelearningrate.
Sevenmodelsarecompared.ThefourHNNspecificationsarede-
finedinSection3;theotherthreearebenchmarksfromGKX[12].
Huber-3istheirOLS-3:aregressiononsize,book-to-marketand
Table1:Hyperparametergrids.𝜂isthelearningrate,𝜆 the
12-monthmomentum,fittedunderHuberloss[16]tolimitthein- 1
𝑙 penaltyondenseweights,𝐾themaximumcliquesize,and
fluenceofextremereturns.Itshowswhataminimal,long-standing 1
𝜖theHuberrobustnessparameter.Thelearning-rategridis
specificationachievesonthispanel.Principalcomponentregres-
𝜂 ∈{10−4,10−3,3×10−3,10−2,3×10−2}.
sion(PCR)isanunpenalizedregressiononprincipalcomponents
ofall94characteristics,computedfromthetrainingdataalone;
becauseitcombinesthemlinearly,thegapbetweenPCRandthe Model Grid
neuralmodelsmeasureswhatnonlinearityadds. HNN(marginal),HNN(m-s) 𝜂;𝐾 ∈ {2,...,7}
NN3isGKX’sthree-hidden-layernetwork,with32,16and8 HNN(input-shuffled) 𝜂
hiddenunits[12],batchnormalizationandan𝑙 1 penalty,applied NN3 𝜂;𝜆 1 ∈ {10−6,10−5,10−3}
hereto94inputs.Itattainsthehighestpooledout-of-sample𝑅2 MLP-HNN 𝜂;𝜆 1 ∈ {10−6,10−5,10−3}
amongthespecificationstheyevaluate,anddeepernetworksdo Huber-3 𝜖 ∈ {1.1,1.35,1.5,2.0}
notimproveonit,soitisademandingbaseline.Itisalsotheclosest PCR components∈ {5,10,20,30,40,60,80,94}
comparisonforthearchitectureclaim:itseesthesamecharacter-
isticswiththesameflexibility,butitsdepthandwidthsaresetby
hand.Wedonotincludetreeensembles,sincethequestionhereis

Dependence-InformedSparseNeuralArchitectureforStockReturnPrediction
4.3 EvaluationandInference Thesamepairedtestisappliedtoabsoluteerror,theinformation
coefficientsandtheportfolioreturns;anegativelossdifferencefa-
Predictiveaccuracyismeasuredagainstaforecastofzero,
vorstheHNN,asdoesapositivedifferenceincoefficientorspread.
|     |     |     | (cid:205) (𝑦 𝑒 −𝑦 | 𝑒 )2 |     |     |     |     |     |     |
| --- | --- | --- | ----------------- | ---- | --- | --- | --- | --- | --- | --- |
𝑅2 =1− 𝑖,𝑡 𝑖 ,𝑡+1 (cid:98)𝑖 ,𝑡+1 , (11) Sixmeasures,squarederror,absoluteerror,thetwoinformation
|     |     | oos | (cid:205) (𝑦𝑒 |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
)2 coefficientsandthetwodecilespreads,arecomparedagainstthree
𝑖,𝑡 𝑖,𝑡+1
benchmarks(NN3,HNN(input-shuffled),MLP-HNN),andthe
wherethesumsrunoverallobservationsinthetestyears.The
resulting18𝑝-valuesareadjustedbyHolm’sprocedure[15].We
benchmarkiszeroratherthanthehistoricalmeanbecausethemean
calladifferencesignificantat5%afteradjustment.
returnofanindividualstockissonoisythatitlowersthebarfor
goodforecastingperformance[12].
| We also | report | pooled | mean absolute | error, and the | Pearson | 5 Results |     |     |     |     |
| ------- | ------ | ------ | ------------- | -------------- | ------- | --------- | --- | --- | --- | --- |
andSpearmaninformationcoefficients:foreachtestmonthwe
5.1 PredictivePerformance
| compute | the cross-sectional |     | correlation | between predicted | and |     |     |     |     |     |
| ------- | ------------------- | --- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- |
realizedreturns,thenaverageacrossmonths.Thesematterbecause Table2reportsthefullcomparison.HNN(marginal)andHNN(m-
along-shortportfolioearnsitsreturnfromrankingstockscorrectly s)matchNN3onpooled𝑅2 ,at0.509%and0.511%against0.475%.
oos
withinamonthratherthanfrompredictingthelevelofreturns, TheHNN(marginal)differenceisnotsignificant(𝑝 =0.796),but
andaforecastthatranksbettersupportsahigherrisk-adjusted themodelsseparatemoreclearlyonranking.HNN(marginal)has
return[11]. thehighestPearsonICandthewidestequal-weightedspreadof
Eachmonthwesortstocksintodecilesonthepredictionand anymodel,exceedingNN3’sPearsonICby0.0056(𝑝 =0.002),and
recordthereturnonthetopdecileminusthebottom.Wereport thissurvivesHolmadjustment(adjusted𝑝 =0.034).TheSpearman
thisunderequalweights(EW)andunderlaggedmarketequity differencepointsthesamewaywithoutreachingsignificance(𝑝 =
(AW),sincethetwocandiffersubstantiallywhensmallstocksdrive 0.178);NN3’sMAEismarginallylower(𝑝 =0.050).Squarederror
theresult[7].Bothlegsearnthesamerisk-freerate,sotherawand compares each prediction with the realized return, and by that
excesslong-shortspreadsareidentical. standardthetwomodelsperformsimilarly.Adecilesortdepends
Turnoverismeasuredwithauniformtransactioncost,since onlyonthecross-sectionalorderingofpredictedreturns,noton
themeasuredadvantageofmachine-learningstrategiescanshrink theirabsolutelevels:ittakesalongpositioninthetoppredicted
oncetradingfrictionsareincluded[1].Let𝑟gross
|     |     |     |     | bethemonth’s |     | decile and | a short position | in  | the bottom. | The HNN’s ranking |
| --- | --- | --- | --- | ------------ | --- | ---------- | ---------------- | --- | ----------- | ----------------- |
𝑡
long-shortspread,𝑤 thesignedtargetweightofstock𝑖,and𝑤 advantageproducesthestrongerequal-weightedspreadinTable2.
|     |     | 𝑖,𝑡 |     |     | (cid:101)𝑖,𝑡−1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
itsweightafterthepreviousmonth’sreturnsbutbeforerebalancing. Thethreebenchmarksdifferinhowmanycharacteristicsthey
Witheachlegnormalizedtounitnotional, useandwhethertheycombinethemlinearly.GoingfromHuber-3’s
|     |       |                     |            |             |        | t h r e e ch | ar a c te r is t ic s to | P C R ’s | 9 4 l if t s p o o le d | 𝑅 2 f r om 0. 1 3 7 % to |
| --- | ----- | ------------------- | ---------- | ----------- | ------ | ------------ | ------------------------ | -------- | ----------------------- | ------------------------ |
|     | 1     |                     |            |             |        |              |                          |          |                         | −                        |
| TO  | ∑︁ |𝑤 | −𝑤 (cid:101)𝑖,𝑡−1|, | 𝑟 net(𝑐)=𝑟 | gross −2𝑐TO | , (12) |              |                          |          |                         |                          |
𝑡 = 𝑖,𝑡 𝑡 𝑡 𝑡 0 .3 3 6 % an d t h e e q u a l-w e ig h te d sp r e a d f r o m 0 .5 1 % t o 2.8 7% . L e t tin g
2
|     | 𝑖   |     |     |     |     | those94interactnonlinearlyinNN3raisesthemagainto0.475% |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
where𝑐isthecostperdollartraded.Thesumisthenotionalbought and3.75%.Mostofthepredictivepowerthereforecomesfromthe
andsold,soTO isone-wayturnoverandthecostis𝑐timestwice numberofcharacteristicsandthefreedomtocombinethem,and
𝑡
that.Droppingthefirsttestmonthleaves359rebalances,andwere- whattheHNNaddsontopof NN3isrankingratherthanlevel
port𝑐 ∈{0,10,25,50}basispoints.Thecalculationignoressecurity- accuracy.Huber-3showswhybothcoefficientsarereported.Ithas
specificspreads,short-borrowfees,marketimpactandcapacity. thehighestSpearmanICofanymodelbutthelowestPearsonIC
Modelsarecomparedmonthbymonth.Foreachtestmonth andthelowestequal-weightedspread.SpearmanICevaluatesrank
weaveragethedifferenceinsquaredforecasterrorsacrossstocks, agreementacrossthefullcross-section,whereasthedecilespread
giving a monthly series whose mean is tested with a Diebold– depends specifically on the realized-return separation between
Mariano statistic [5] and Newey–West heteroskedasticity- and stocksassignedtothetwoextremepredicteddeciles.Strongoverall
autocorrelation-consistent(HAC)standarderrorswithsixlags[26]. rankcorrelationthereforeneednotimplyalargelong-shortspread.
Table2:Out-of-sampleexcess-returnresults,1987–2016.𝑅2 andmonthlygrossspreadsarepercentages.ICsaremeansof
monthlycross-sectionalcorrelations.Parametersaremediantrainablecountsperensemblememberacrossannualrefits.
Boldfacemarksthestrongestestimateineachperformancecolumn.
|     |     | Model |     | 𝑅2 MAE | PearsonIC | SpearmanIC | EWspread | AWspread | Params. |     |
| --- | --- | ----- | --- | ------ | --------- | ---------- | -------- | -------- | ------- | --- |
oos
|     |     | Huber-3       |     | -0.137 0.1050 | 0.0227 | 0.0676 | 0.51 |     | 1.21 4     |     |
| --- | --- | ------------- | --- | ------------- | ------ | ------ | ---- | --- | ---------- | --- |
|     |     | PCR           |     | 0.336 0.1056  | 0.0437 | 0.0464 | 2.87 |     | 1.15 81    |     |
|     |     | NN3           |     | 0.475 0.1057  | 0.0586 | 0.0474 | 3.75 |     | 2.44 3.8k  |     |
|     |     | HNN(m-s)      |     | 0.511 0.1058  | 0.0610 | 0.0491 | 3.85 |     | 2.00 5.2k  |     |
|     |     | HNN(marginal) |     | 0.509 0.1059  | 0.0642 | 0.0517 | 3.95 |     | 1.99 21.0k |     |
HNN(input-shuffled) 0.496 0.1058 0.0597 0.0490 3.73 1.91 21.0k
|     |     | MLP-HNN |     | 0.429 0.1057 | 0.0524 | 0.0436 | 3.47 |     | 2.48 1680.7k |     |
| --- | --- | ------- | --- | ------------ | ------ | ------ | ---- | --- | ------------ | --- |

HongyuLin,YulinChen,YuanrongWang,AntonioBriola,andTomasoAste
Table3:Turnoverandtransaction-costsensitivityover359monthlyrebalances.TOismeantotalone-wayturnoveracross
twounit-notionallegs.NetandSRarethemonthlynetspread(percent)andannualizedSharperatioat25basispointsper
traded dollar. BE is the break-even cost in basis points that sets the mean spread to zero. EW and AW denote equal and
lagged-market-equityweights.
Equalweighted(EW) Assetweighted(AW)
Model TO Net SR BE TO Net SR BE
NN3 1.23 3.13 2.17 153 1.35 1.78 0.95 91
HNN(m-s) 1.24 3.24 2.24 156 1.38 1.32 0.76 73
HNN(marginal) 1.25 3.34 2.28 159 1.36 1.31 0.73 73
HNN(input-shuffled) 1.26 3.12 2.11 149 1.41 1.22 0.65 68
MLP-HNN 1.15 2.91 1.93 151 1.28 1.85 0.99 98
5.2 FeatureAlignmentandParameterEconomy ontheequal-weightedspread,andthePearsonadvantageagain
Theshuffledcontrolchangeswhichcharacteristicentersatwhich survivesadjustment(adjusted𝑝 = 0.001).MLP-HNNdoeshave
nodeandnothingelse:thewidths,theconnectionsandtheparame- aslightlylowerMAEandahigherasset-weightedspread,sothe
tercountarethoseofHNN(marginal).Anydifferenceistherefore HNN’sgainisintheequal-weightedratherthantheasset-weighted
duetothemismatchbetweenthecharacteristicsandtheiroriginal portfolio.
positionsintheMFCF.Pooled𝑅2fallsfrom0.509%to0.496%,the Parametercountdependsontheselected𝐾 andonhowmany
PearsonICfrom0.0642to0.0597,andtheequal-weightedspread subsetsthefilteredgraphcontains.HNN(m-s)runswith𝐾 ≤ 4
from3.95%to3.73%.ThePearsonreductionsurvivesHolmadjust- in20ofthe30annualrefits,against𝐾 ≥ 5in25refitsforHNN
ment(adjusted𝑝 =0.003);thespreadreductionissignificantbefore (marginal),whichiswhyitsmediancountislowereventhoughit
adjustment(𝑝 =0.007)butnotafter.Whatthefilteredgraphcon- reaches𝐾 =7attheendofthesample.Nolayerwidthischosen
tributesisthereforenotonlysparsitybutalsotheparticularclique byhand.
structureitestimates.
ThedensecontrolinsteadreplacestheHNNwithaconventional
5.3 EconomicRanking
width-matcheddensearchitecture.MLP-HNNhasthesamewidths
asHNN(marginal)butconnectseverylayerfully,whichgivesit Table3reportsturnoverandnetperformance.HNN(marginal)’s
1.68millionparametersagainstHNN(marginal)’s21.0thousand. equal-weighteddecilereturnsrisealmostmonotonicallyfrom−0.97%
Takenasacompletearchitecture,HNN(marginal)nonetheless inthebottomdecileto2.98%inthetop(Figure2),givingthe3.95%
ranksthecross-sectionbetteronbothinformationcoefficientsand grossspread.Atacostof25basispointsperdollartradedthespread
isstill3.34%permonth,withanannualizedSharperatioof2.28,
4
3
2
1
0
−1
−2
1 2 3 4 5 6 7 8 9 10
Prediction decile (low to high)
)%(
nruter
ssecxe
ylhtnom
naeM
(a) HNN (marginal) decile returns
4.0
3.8
3.6
3.4
3.2
3.0
2.8
2.6
0 10 25 50
Cost per traded dollar (bps)
)htnom
rep
%(
daerps
WE
teN
NN3 HNN (m-s) HNN (marginal)
(b) Transaction-cost sensitivity
Figure2:Economicrankingandcostsensitivity.Panel(a)reportsHNN(marginal)equal-weighteddecilereturnswith95%
HACintervals(sixlags).Panel(b)reportsequal-weightedlong-shortspreadsunderuniformcosts,usingEquation(12).

Dependence-InformedSparseNeuralArchitectureforStockReturnPrediction
(a) Full out-of-sample period
Huber-3 -0.137
0.8
PCR 0.336
0.6
NN3 0.475
HNN (m-s) 0.511 0.4
HNN (marginal) 0.509 0.2
HNN (input-shuffled) 0.496
0.0
MLP-HNN 0.429
−0.2
−0.1 0.0 0.1 0.2 0.3 0.4 0.5 1987--96 1997--06 2007--16
Pooled R2 (%)
oos
)%(
2R
delooP
soo
(b) Performance across decades
NN3 HNN (marginal) HNN (m-s)
Figure3:Pooledanddecade-levelpredictiveperformance.Panel(a)reportsfull-period𝑅2 forallsevenmodels.Panel(b)
oos
reportsthetwoHNNvariantsandNN3overthreenon-overlappingdecades.
andthecostatwhichitwouldvanishis159basispoints,aboutsix Thewidth-matcheddensecomparatoralsoproducesalowerPear-
timesthelevelapplied. sonICdespitehaving80timesmoreparameters.Becausethiscom-
Therankingofthemodelsisunchangedacrossthecostlevels.At paratorusesbothfullyconnectedlayersandaconventionalfinal-
25basispointsHNN(marginal)earns3.34%against3.13%forNN3, layerpredictionhead,thecomparisonconcernsthecompleteHNN
adifferencethatispositivebutnotsignificant(𝑝 =0.112).Itstays architectureratherthansparseconnectivityinisolation.Itnever-
aheadof HNN(input-shuffled)andMLP-HNN,withunadjusted thelessshowsthatreplacingtheHNNwithasubstantiallylarger
𝑝 =0.007and𝑝 =0.028.Theadvantageoverbothcontrolstherefore conventionaldensearchitectureofthesameinduceddepthand
survivesacommonturnoverpenalty. widthsdoesnotimprovecross-sectionalranking.
AssetweightingreversesthecomparisonwithNN3:HNN(mar- Thishastwopracticalconsequences.First,tuningislimitedto
ginal)earns1.31%against1.78%(𝑝 =0.036inNN3’sfavor).Equal- thecliqueboundandthelearningrate,insteadofasearchover
andasset-weightedresultsdivergeinthiswaywhenaneffectis depthandwidth.Second,eachneuralunitstandsforaspecificset
strongeramongsmallerstocks[7]. ofcharacteristics,sotheinteractionsafittedmodelexpressescan
bereaddirectlyoffthegraph.Adensenetworkofthesamesize
5.4 PerformanceAcrossTime offersnoequivalentreading.
Some limits should be noted. The 94 characteristics exclude
Noarchitectureleadsineverydecade(Figure3).HNN(marginal)
GKX’sindustryindicatorsandmacroeconomicinteractions,sothis
recordspooled𝑅2of0.714%,0.668%and−0.135%over1987–1996,
isacontrolledcomparisonofarchitecturesratherthanareplication
1997–2006and2007–2016,againstNN3’s0.518%,0.749%and−0.138%,
oftheir920-inputspecification.Thenetreturnschargeasingle
andleadsNN3in19ofthe30individualyearson𝑅2andin19on
linearcostagainstmeasuredturnoverandignoresecurity-specific
PearsonIC.HNN(m-s)isthestrongestneuralmodelinthelast
spreads,short-borrowfees,marketimpactandcapacity,eachof
decadeat−0.040%,andPCRtheonlymodelwithpositive𝑅2there,
whichcanimpactportfolioperformance[1].
at0.087%.
Over2007–2016theequal-weightedspreadis2.55%permonth
forHNN(marginal)and2.48%forNN3.Levelaccuracyandcross- 7 Conclusion
sectionalorderingthereforecomeapartinthelatersample.The
Thispaperusesestimateddependenceamongfirmcharacteristics
neuralmodelslosetoaforecastofzerowhiletheirdecilesortsstill
tospecifyaforecastingarchitecture.Thecliquesreturnedbythe
separatethecross-section.
MFCFbecomeunitsinasparseneuralnetwork,andtheirinclusion
relationsdeterminetheconnectionsbetweenlayers.Depth,width,
6 Discussion
andconnectivitythereforefollowfromtheestimateddependence
Thetwoablationsnarrowdownwhatthefilteredgraphcontributes. graphratherthanbeingchosenseparately.Across30annualout-
Permutingthecharacteristicsacrossthenodesleavesthenetwork of-sampletestsontheGKXpanel,theresultingHNNsforecast
identicalinsizeandshape,yetlowersthePearsonICbyanamount asaccuratelyasathree-hidden-layerbenchmark,deliverstronger
thatsurvivesmultiplicityadjustment,sothegraphdoesmorethan cross-sectionalrankingperformance,andusefarfewerparameters
imposesparsity,theparticularcliquesitformscarryinformation. thanadensenetworkwiththesameinducedlayerwidths.

HongyuLin,YulinChen,YuanrongWang,AntonioBriola,andTomasoAste
Twonaturalextensionsremain.First,thedependencematrix onMachineLearning.Haifa,Israel,807–814.
could be estimated using measures that capture nonlinear rela- [26] WhitneyK.NeweyandKennethD.West.1987.ASimple,PositiveSemi-Definite,
tionships or are more robust than Pearson correlation. Second, HeteroskedasticityandAutocorrelationConsistentCovarianceMatrix.Econo-
metrica55,3(1987),703–708.doi:10.2307/1913610
HNN(m-s)couldbegeneralizedsothatitsarchitecturevarieswith [27] TomasoPoggio,HrushikeshMhaskar,LorenzoRosasco,BrandoMiranda,and
QianliLiao.2017.WhyandWhenCanDeep—butNotShallow—NetworksAvoid
broadermarketregimesratherthanremainingfixedwithineach
theCurseofDimensionality:AReview.InternationalJournalofAutomationand
trainingwindow.Moregenerally,theresultsshowthatempirical Computing14,5(2017),503–519.doi:10.1007/s11633-017-1054-2
dependenceamongfirmcharacteristicscanbeusednotonlytosum- [28] RobertTibshirani.1996. RegressionShrinkageandSelectionviatheLasso.
marizetheirrelationshipstructure,butalsotospecifyaforecasting JournaloftheRoyalStatisticalSociety:SeriesB58,1(1996),267–288.
[29] MicheleTumminello,TomasoAste,TizianaDiMatteo,andRosarioN.Mantegna.
architecture.
2005.AToolforFilteringInformationinComplexSystems.Proceedingsofthe
NationalAcademyofSciences102,30(2005),10421–10426. doi:10.1073/pnas.
References 0500298102
[30] YuanrongWangandTomasoAste.2022.NetworkFilteringofSpatial-Temporal
[1] DoronAvramov,SiCheng,andLiorMetzker.2023.MachineLearningvs.Eco- GNNforMultivariateTime-SeriesPrediction.InProceedingsoftheThirdACM
nomicRestrictions:EvidencefromStockReturnPredictability. Management InternationalConferenceonAIinFinance.AssociationforComputingMachinery,
Science69,5(2023),2587–2619.doi:10.1287/mnsc.2022.4449 NewYork,NY,USA,463–470.doi:10.1145/3533271.3561678
[2] JimmyLeiBa,JamieRyanKiros,andGeoffreyE.Hinton.2016.LayerNormaliza- [31] YuanrongWang,AntonioBriola,andTomasoAste.2023.HomologicalNeural
tion.arXiv:1607.06450.doi:10.48550/arXiv.1607.06450 Networks:ASparseArchitectureforMultivariateComplexity.InProceedings
[3] LuyangChen,MarkusPelger,andJasonZhu.2024. DeepLearninginAsset oftheSecondAnnualWorkshoponTopology,Algebra,andGeometryinMachine
Pricing.ManagementScience70,2(2024),714–750.doi:10.1287/mnsc.2023.4695 Learning(ProceedingsofMachineLearningResearch,Vol.221).PMLR,Honolulu,
[4] ThomasM.CoverandJoyA.Thomas.2006.ElementsofInformationTheory(2 HI,USA,228–241. https://proceedings.mlr.press/v221/wang23a.html
ed.).Wiley-Interscience,Hoboken,NJ.
[5] FrancisX.DieboldandRobertoS.Mariano.1995.ComparingPredictiveAccuracy.
| JournalofBusiness&EconomicStatistics13,3(1995),253–263. |     |     | doi:10.1080/ |     |
| ------------------------------------------------------- | --- | --- | ------------ | --- |
07350015.1995.10524599
[6] ThomasElsken,JanHendrikMetzen,andFrankHutter.2019.NeuralArchitecture
| Search:ASurvey. | JournalofMachineLearningResearch20,55(2019),1–21. |     |     |     |
| --------------- | ------------------------------------------------- | --- | --- | --- |
https://jmlr.org/papers/v20/18-598.html
[7] EugeneF.FamaandKennethR.French.2008.DissectingAnomalies.TheJournal
ofFinance63,4(2008),1653–1678.doi:10.1111/j.1540-6261.2008.01371.x
| [8] GuanhaoFeng,StefanoGiglio,andDachengXiu.2020. |     |                                          | TamingtheFactor |     |
| ------------------------------------------------- | --- | ---------------------------------------- | --------------- | --- |
| Zoo:ATestofNewFactors.                            |     | TheJournalofFinance75,3(2020),1327–1370. |                 |     |
doi:10.1111/jofi.12883
| [9] JoachimFreyberger,AndreasNeuhierl,andMichaelWeber.2020. |     |     |     | Dissecting |
| ----------------------------------------------------------- | --- | --- | --- | ---------- |
CharacteristicsNonparametrically.TheReviewofFinancialStudies33,5(2020),
2326–2377.doi:10.1093/rfs/hhz123
| [10] JeromeFriedman,TrevorHastie,andRobertTibshirani.2008. |     |     | SparseInverse |     |
| ---------------------------------------------------------- | --- | --- | ------------- | --- |
CovarianceEstimationwiththeGraphicalLasso.Biostatistics9,3(2008),432–441.
doi:10.1093/biostatistics/kxm045
[11] RichardC.GrinoldandRonaldN.Kahn.2000.ActivePortfolioManagement(2
ed.).McGraw-Hill,NewYork.
| [12] ShihaoGu,BryanKelly,andDachengXiu.2020. |                                                  |     | EmpiricalAssetPricingvia |     |
| -------------------------------------------- | ------------------------------------------------ | --- | ------------------------ | --- |
| MachineLearning.                             | TheReviewofFinancialStudies33,5(2020),2223–2273. |     |                          |     |
doi:10.1093/rfs/hhaa009
| [13] ShihaoGu,BryanKelly,andDachengXiu.2021. |     |     | AutoencoderAssetPricing |     |
| -------------------------------------------- | --- | --- | ----------------------- | --- |
Models.JournalofEconometrics222,1(2021),429–450.doi:10.1016/j.jeconom.
2020.07.009
[14] CampbellR.Harvey,YanLiu,andHeqingZhu.2016....andtheCross-Section
ofExpectedReturns.TheReviewofFinancialStudies29,1(2016),5–68.doi:10.
1093/rfs/hhv059
| [15] StureHolm.1979. | ASimpleSequentiallyRejectiveMultipleTestProcedure. |     |     |     |
| -------------------- | -------------------------------------------------- | --- | --- | --- |
ScandinavianJournalofStatistics6,2(1979),65–70.
[16] PeterJ.Huber.1964.RobustEstimationofaLocationParameter.TheAnnalsof
MathematicalStatistics35,1(1964),73–101.
[17] BryanT.Kelly,SethPruitt,andYinanSu.2019.CharacteristicsAreCovariances:
AUnifiedModelofRiskandReturn.JournalofFinancialEconomics134,3(2019),
501–524.doi:10.1016/j.jfineco.2019.05.001
[18] MauriceG.Kendall.1970.RankCorrelationMethods(4ed.).Griffin,London.
[19] DiederikP.KingmaandJimmyBa.2015.Adam:AMethodforStochasticOpti-
mization.In3rdInternationalConferenceonLearningRepresentations.OpenRe-
| view.net,SanDiego,CA,USA,15pages.                     |                                                 | https://arxiv.org/abs/1412.6980 |                    |     |
| ----------------------------------------------------- | ----------------------------------------------- | ------------------------------- | ------------------ | --- |
| [20] SerhiyKozak,StefanNagel,andShrihariSantosh.2020. |                                                 |                                 | ShrinkingtheCross- |     |
| Section.                                              | JournalofFinancialEconomics135,2(2020),271–292. |                                 | doi:10.1016/j.     |     |
jfineco.2019.06.008
| [21] HongyuLin,AntonioBriola,YuanrongWang,andTomasoAste.2026. |             |                              |              | Com-    |
| ------------------------------------------------------------- | ----------- | ---------------------------- | ------------ | ------- |
| positional                                                    | Sparsity as | an Inductive Bias for Neural | Architecture | Design. |
arXiv:2605.14764.doi:10.48550/arXiv.2605.14764
| [22] RosarioN.Mantegna.1999. |     | HierarchicalStructureinFinancialMarkets. |     | The |
| ---------------------------- | --- | ---------------------------------------- | --- | --- |
EuropeanPhysicalJournalB11,1(1999),193–197.doi:10.1007/s100510050929
| [23] Guido Previde | Massara | and Tomaso Aste. 2019. | Learning Clique | Forests. |
| ------------------ | ------- | ---------------------- | --------------- | -------- |
arXiv:1905.02266.doi:10.48550/arXiv.1905.02266
| [24] GuidoPrevideMassara,TizianaDiMatteo,andTomasoAste.2017. |     |     |     | Network |
| ------------------------------------------------------------ | --- | --- | --- | ------- |
FilteringforBigData:TriangulatedMaximallyFilteredGraph.JournalofComplex
Networks5,2(2017),161–178.doi:10.1093/comnet/cnw015
| [25] VinodNairandGeoffreyE.Hinton.2010. |     | RectifiedLinearUnitsImproveRe- |     |     |
| --------------------------------------- | --- | ------------------------------ | --- | --- |
strictedBoltzmannMachines.InProceedingsofthe27thInternationalConference
---- END DOCUMENT ----
