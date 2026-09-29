Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Knowledge-guided Transfer Prediction In
Underrepresented Populations: A GRU-D-Static
Framework For Maternal And Neonatal Outcomes
Yipeng Wei1, Zahra Hoodbhoy2, Emily R. Smith3, Fang Jin1, Muhammad Imran Nisar2,
Muhammad Farrukh Qazi2, Christopher Mores3, Victor Akelo4, Caleb Sagam4, Florence
Aweyo4, Charlotte Tawiah5, Veronica Agyemang5, Kwaku Poku Asante5, Sam Newton5,
Santosh Joseph Benjamin6, Anne George Cherian6, Devakumar Devadhas6, James A6,
Margaret P. Kasaro7, Augustine Tunga7, Sarmila Mazumder8, Neeraj Sharma8, Wilbroad
Mutale9, Mae Bridget Spelke10, and Qing Pan11,*
1GeorgeWashingtonUniversity,DepartmentofStatistics,WashingtonD.C.,UnitedStates
2TheAgaKhanUniversity,DepartmentofPaediatricsandChildHealth,Karachi,Pakistan
3GeorgeWashingtonUniversity,DepartmentofGlobalHealth,WashingtonD.C.,UnitedStates
4KenyaMedicalResearchInstitute,CentreforGlobalHealthResearch,Kisumu,Kenya
5KintampoHealthResearchCenter,Research&DevelopmentDivision,Kintampo,Ghana
6ChristianMedicalCollege&Hospital,Vellore,India
7UniversityofNorthCarolinaGlobalProjectsZambia,Lusaka,Zambia
8Implementation ScienceDomain,SocietyforAppliedStudies,NewDelhi,India
9UniversityofZambia,DepartmentofHealthPolicyandManagement,Lusaka,Zambia
10UniversityofNorthCarolinaatChapelHill,ChapelHill,UnitedStates
11GeorgeWashingtonUniversity,DepartmentofBiostatisticsandBioinformatics,WashingtonD.C.,UnitedStates
*CorrespondingAuthor: qpan@gwu.edu
ABSTRACT
Integrating summary-level scientific knowledge (for example, published external literature) into neural network models pro-
vides a practical strategy for transferring prediction models trained on adequately sampled source cohorts to underrepre-
sentedtargetpopulations,whereindividual-leveldatainthetargetdomainareoftenlimitedorunavailable. Inthisstudy,we
proposetransferpredictionstrategiesincorporatingexternalsummary-levelscientificknowledgeandillustrateitsapplication
onthePRISMAMaternalandNeonatalHealthStudy,traininganeuralnetworkmodelonthesourcedatatopredictadverse
outcomesinthetargetcohorts. Besides, we alsoextendtheexistingGRU-D frameworkbyincorporatingstaticfeatureem-
beddings and attention weights to jointly leverage temporal and static information for improved prediction. Our approach
employssoft labelsderivedfromsummary-levelstatistics(such ascoefficientsin logisticregressions)describingthe target
populationto fine-tuneGRU-D-Staticmodelsthatare initiallytrainedon thesource populationswhichdifferfromthe target
population. We evaluatesix maternalandneonataloutcomes, includingstillbirth, pretermbirth, low birthweight, small vul-
nerablenewborn,neonataldeath,andmaternalnearmiss. Acrossalltestedscenarios,fine-tuningusingsoftlabelsfromjust
basic covariatessubstantiallyimprovedpredictiveperformancecomparedwithdeeplearningmodelstrainedon thesource
sample. Furthermore,theperformanceslightlyimprovesmore whenadditionalcovariateswere incorporatedinto the logis-
ticregressionmodelor whenpartialinputfeaturesfromthetargetpopulationwereavailableforfine-tuning. Thesefindings
demonstratethatintegratingexistingscientificknowledgeintheliteraturethroughtransferpredictionofsourceneuralnetwork
modelscanenhancepredictionperformancein underrepresentedtargetpopulations,reducingrelianceonlarge-scaledata
collectionandsupportingriskpredictioninglobalhealth.
Introduction
Transferpredictionaimstomakeinferenceorpredictionsforatargetpopulationbyadaptingmodelstrainedonrelatedsource
populations, which is especially valuable in globalhealthcare and clinical studies, as data availability and populationchar-
acteristics often differ substantially across regions1,2. Large-scale global analyses have demonstrated substantial regional
inequalities in maternal and neonatal health outcomesacross LMICs, reflecting differencesin both risk factor distributions
andhealthcaresystems3. Inpractice,thedistributionofriskfactorsandtheprevalenceofoutcomescanvarybetweenregions.
Furthermore, the relationshipsbetween them may also vary, such that directly applyinga source-trainedmodelcan lead to
6202
guA
12
]PA.tats[
1v37012.8062:viXra

poorpredictionperformanceintargetpopulations.Forexample,consideraneonatalriskpredictionmodeldevelopedinSouth
Asianlow-andmiddle-incomecountries(LMICs),suchasIndiaorPakistan,usingroutinelycollectedmedicaldata,including
maternaldemographics,clinicalhistory,andbasiclaboratorymeasurements. WhenthismodelisappliedtoAfricansettings
suchasKenya,Zambia,orGhana,itsperformancemaydeteriorateduetodifferencesintheprevalenceofinfectiousdiseases
(e.g.,malaria,HIV),maternalnutritionalstatus,andaccesstodiagnosticresources.Predictionmodelsoftenfailinunderrepre-
sentedpopulations.Transferpredictioncanhelp,butusuallyrequiresmoretarget-domaindatathanarerealisticallyavailable.
Inmanyrealsettings,onlysummary-leveltargetinformationmaybeavailable. Existinglongitudinalpredictionframeworks
donotadequatelyaddressthissetting,especiallywhendataareirregularandincludestaticandtemporalpredictors.Therefore,
thispaperproposestwomajorinnovations:anextensionofGRU-Dmodeltoemphasizestaticfeaturesandatransfer-learning
strategythatusessummary-leveltargetinformationviasoftlabels.
Previousstudies have shown that weightingmethodscan help mitigate such discrepancies4. Recent work in healthcare
hasaddressedthischallengethroughtransferpredictionframeworkssuchasCOMMUTE5 andTransRF6,whichcalibrateor
ensemble models across heterogeneouspopulationsto improvegeneralizability in underrepresentedgroups. Such methods
requireindividual-levelcovariateinformationfromthetargetpopulation. However,insomecases, datafromthetargetpop-
ulation may be limited or completelyunavailableand onlyprior summary-levelinformationfrom previousstudies, such as
knownassociationsbetweenoutcomesandriskfactorscanbereliedupon. Forexample,onemaywishtoadaptatype2dia-
betes(T2D)riskpredictionmodeltrainedonU.S.participantsfromtheDiabetesPreventionProgram(DPP)OutcomesStudy7
toaChinesepopulationbyincorporatingsummary-levellogisticregressioncoefficientsreportedintheWuhanelderlycohort
study8. Inthiscase,theWuhanstudypublishesregressioncoefficientsfromapenalizedlogisticmodel,whileindividual-level
de-identifiedDPPdataareavailablethroughtheNationalInstituteofDiabetesandDigestiveandKidneyDiseases(NIDDK)
data repository. Ma et al.9 proposedthe PRIME framework for electronic health record (EHR) risk prediction, which em-
ploysaposteriorregularizationtechniquetoincorporatepriormedicalknowledge(e.g.,disease–riskfactorrelationships)into
deep learning models. Recentreviews emphasizethe importanceof developingbroadermethodologicalapproachesto sup-
portgeneralisabilityandtransportability. For example,Ploddiet al. providea comprehensiveoverviewof bothdata-driven
andknowledge-drivenstrategiesthatcanstrengthenmodelperformanceacrosspopulations10. Manke-Reimersetal. review
appliedstudiesoftransportabilitymethodsandillustrate howthese approacheshavebeenimplementedto improveexternal
validityin diversesettings11. Additionally,undertheconstraintsoflimitedtargetdata, especiallywhenactuallabelsareab-
sent, modelscan still be adaptedby leveragingpriorknowledgethroughsoft labels which encodeclass probabilitiesrather
thanbinaryoutcomes.Thesesoftlabelsprovideadditionalinformationthatimprovespredictionsintargetpopulations12. This
approach,knownasknowledgedistillation,hasbeenshowntobeeffectivefordomainadaptation13,14.
ThePregnancyRisk,InfantSurveillance,andMeasurementAlliance(PRISMA)MaternalandNewbornHealthStudyisa
population-based,longitudinalobservationalstudydesignedtocollectstandardizeddataforestimatingmaternalandneonatal
risksandtodevelopinnovativestrategiestoimprovepregnancyoutcomesformothersandtheirnewbornsinlow-andmiddle-
income countries3, including Kenya, Zambia, Ghana, Pakistan, and India. In this study, we divide the PRISMA data into
African and Asian regions. Given the regionalheterogeneityacross Asia andAfrica, our study explorestransferprediction
approachusing soft labels to fine-tunedeep learningmodels from one region (source)to another(target) in the absence of
training data from the target population. We focus on critical maternal (e.g., maternal near miss) and neonatal outcomes,
including stillbirth, low birth weight (LBW), preterm birth (PTB), small vulnerable newborn (SVN), and neonatal mortal-
ity15,16. We first trainthedeeplearningmodelonthesourcedataandthenfine-tuneit usingsummary-levelinformationof
therelationshipsbetweenthecovariatesandthediseaseoutcomeinthetargetregion. Thatis,wegeneratesoftlabelsusinga
logisticregressionmodelfittedonthetargetpopulationwhosecoefficientsareavailableonpublicliteratures. Transferpredic-
tionisnotstrictlyrequiredforthePRISMAdata,asdetailedindividual-levelinformationonbothcovariatesandoutcomesis
availableforboththesourceandtargetpopulations.Nevertheless,weusethePRISMAdatatoillustratetheproposedtransfer
predictionapproach,whichisparticularlyusefulinsettingswhereonlysummary-levelinformationisavailableforthetarget
populationalongsideindividual-leveldatafromthesourcepopulation.Notably,theAsianandAfricanPRISMAcohortswere
collectedunderacommonprotocolwithharmonizedvariablesandconsistentqualitystandards.Asaresult,thedistributional
shiftbetweenthesourceandtargetpopulationsisrelativelylimited,representingafavorabletransferpredictionsetting. The
prediction performance of the fine-tuned deep learning model is subsequently evaluated on the target data in PRISMA to
assesstheeffectivenessofthetransferpredictionapproach.
WeimplementtheGRU-D-Staticdeeplearningframework,avariantoftheGRU-Dframeworkdevelopedbyourteamin
thisstudy.Nevertheless,theproposedtransferpredictionmethodologyismodel-agnosticandbroadlyapplicabletootherdeep
learning frameworks. The original GRU-D framework is designed to handle multivariate clinical time series with missing
valuesthroughadecaymechanismthatadjustsinputfeaturesandhiddenstatesbasedonthetimeelapsedsincethelastobser-
vation17. However,akeylimitationoftheGRU-Dframeworkisthatstaticfeaturescannotbeincorporated,asthesefeatures
aretypicallymeasuredoncewithoutanyassociatedtimeintervals,inwhichcasethedecaymechanismcannotbeapplied. To
2/11

overcomethislimitation,weproposetheGRU-D-Staticframeworkwhichintegratesstaticfeatureembeddingswithattention
weightthatdynamicallyweightstemporalinformationbasedonthestaticcontexttoenhancepredictiveperformance18.
To the bestofourknowledge,thisis amongthe firstapproachesto leverageexternalscientific knowledge(e.g., logistic
regressioncoefficients)assoftlabels,ratherthantrueoutcomelabels,fortransferpredictionindata-limitedtargetpopulations.
The proposedmethodis well suited for low- and middle-incomecountry(LMIC) contexts, where access to comprehensive
individual-leveldataisoftenlimitedorunavailable.
Methods
Data
Weselectsixmaternalandneonataloutcomestovalidateourtransferpredictionapproach:
1. Maternalnearmiss: Refersto womenwhoexperiencedlife-threateningcomplicationsbutsurvivedduringpregnancy,
childbirth,orwithin42daysoftheendofpregnancybasedonWHOnearmissclinicalcriteria.
2. Stillbirth: Defined as the delivery of a fetus with no signs of life, indicated by the absence of breathing, heartbeat,
umbilicalcordpulsation,orvoluntarymusclemovementatorafter20-weekgestation.
3. Lowbirthweight(LBW):Definedasabirthweightlessthan2500grams.
4. Pretermbirth(PTB):Definedaslivebirthsoccurringbefore37completedweeksofgestation.
5. Smallvulnerablenewborn(SVN):Definedasafour-categorycompositebasedongestationalageandsize-for-gestational-
age: (1)Term+ non-smallforgestationalage(non-SGA),(2)Term+ smallforgestationalage(SGA),(3)Preterm+
non-SGA,and(4)Preterm+SGA.
6. Neonatalmortality:Definedasthedeathofaliveborninfantbefore28completeddaysoflife.
| Category | Riskfactor   | Type   | LabIndicator,DataSource,Definition |                              |       |
| -------- | ------------ | ------ | ---------------------------------- | ---------------------------- | ----- |
|          | Demographics | Static | Years of school ≥                  | 10, Maternal age, Unimproved | water |
Sociodemographics
source,Unimprovedsanitation,Wealthindex,Paidwork
|     | Airpollution | Static | Householdsmoking,Smoking,Chewtobacco,Chewbetel- |     |     |
| --- | ------------ | ------ | ----------------------------------------------- | --- | --- |
nut,Useofuncleancookingfuel(kerosene,coal,charcoal,
biomass,wood)
MaternalBMI,Gestationalweightgain(IOMguideline19),
|     | Nutritionalstatus | Static |     |     |     |
| --- | ----------------- | ------ | --- | --- | --- |
MaternalMUAC
|          | Medicalhistory | Static | Pretermbirth,C-section,Miscarriage≥3,Stillbirth,Parity |     |     |
| -------- | -------------- | ------ | ------------------------------------------------------ | --- | --- |
| Clinical |                | Static | Chronichypertension,Pregestationaldiabetes             |     |     |
Comorbids
|     |     | Static | Gestational hypertension | (including preeclampsia), | Gesta- |
| --- | --- | ------ | ------------------------ | ------------------------- | ------ |
tionaldiabetes,Maternaldepression
|     | Delivery  | Static | Placeofdelivery,GAatbirth,Birthweight,Newborngender |     |     |
| --- | --------- | ------ | --------------------------------------------------- | --- | --- |
|     | Postnatal | Static | Congenitalanomalies,PSBI,ExcessiveTCBbyNICEthresh-  |     |     |
old20
|     |     | Static | HepB,HepC |     |     |
| --- | --- | ------ | --------- | --- | --- |
Infections
| Lab |            | Static   | HIV/AIDS,Tuberculosis,Malariainfection,OtherSTIs    |     |     |
| --- | ---------- | -------- | --------------------------------------------------- | --- | --- |
|     | Biomarkers | Temporal | Hemoglobin&Maternalanemia,Totalironbindingcapacity, |     |     |
Ferritin,Hepcidin
|            |            | Static   | Numberoffetus               |     |     |
| ---------- | ---------- | -------- | --------------------------- | --- | --- |
| Ultrasound | Ultrasound | Temporal | AFIindex,Placentalanomalies |     |     |
Table1. Summaryofriskfactorcategoriesanddefinitions
Abbreviations:BMI,bodymassindex;MUAC,mid-upperarmcircumference;GA,gestationalage;IOM,InstituteofMedicine;PSBI,possibleseriousbacterial
infection;TCB,transcutaneousbilirubin;NICE,NationalInstituteforHealthandCareExcellence;STI,sexuallytransmittedinfection;AFI,amnioticfluidindex.
Potentialriskfactorsincorporatedinthemodelsarecategorizedintotemporalorstaticfeatures(summarizedinTable1).
3621.
Temporalfeatures, are collected longitudinallyat enrollmentand at gestationalweeks 20, 28, 32, and Static features
arecollectedonlyonce.Theseriskfactorsincludesocio-demographiccharacteristics,clinicalinformation,laboratory-related
results and ultrasound findings. Basic covariates such as sociodemographic and clinical information are generally readily
availableinstandardclinicalsettings. Incontrast,accesstolaboratorytestingandultrasoundexaminationsmaybelimitedin
low-andmiddle-incomecountries(LMICs)duetoresourceconstraints. Inparticular,thedetailedfeaturesincludedforeach
outcome are presented in Supplementary Table 1. For the preterm birth outcome, temporal features are restricted to those
collectedbefore32weeksofgestationtopreventinformationleakage.
3/11

Notations
)T
We denote the temporal features of length T as X temp = (x ,x ,...,x T with corresponding temporal masking features
|     |     |     |     |     |     |     |     | 1 2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M =(m ,m ,...,m )T. Foreacht∈{1,2,...,T},wedefinex =(x ,x ,...,x )T andm =(m ,m ,...,m )T,where
| temp |     | 1 2 | T   |     |     |     |     | t   | t1 t2 | tU t | t1 t2 | tU  |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ----- | --- |
U denotesthenumberoffeaturesateachtimestamp. Foreachd∈{1,2,...,U},m td isdefinedas
|     |     | 1, ifx | isobserved |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
td
|     | m td = |               |     |     |     |     |     |     |     |     |     | (1) |
| --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |        | (0, otherwise |     |     |     |     |     |     |     |     |     |     |
)T
ThetimestampsfortemporalfeatureX temp aredenotedbyS temp =(s 1 ,s 2 ,...,s T withcorrespondingtimeintervals∆ temp =
| (δ,δ,...,δ |     | )T,whereδ | =0whent=1andδ |     |     | =s  | −s  | fort>1. |     |     |     |     |
| ---------- | --- | --------- | ------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
| 1          | 2   | T         | t             |     |     | t t | t−1 |         |     |     |     |     |
Similarly, the static featuresare denotedas X =(x ,x ,...,x containingV featuresmeasuredonce per subject.
|     |     |     |     |     | static |     | (s)1 | (s)2 | (s)V ) |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ---- | ---- | ------ | --- | --- | --- |
Inthispaper,wewillpredicttheoutcomeY givenadatasetofN subjects,representedas(X(n),M(n),S(n))N ,whereX(n)=
n=1
(X(n) ,X(n) ),M(n) =M(n) =(m(n),m(n),...,m(n) )T andS(n)=S(n) =(s(n),...,s(n) )denotesthesequenceofobservation
| temp | static |     | temp | 1 2 |     | T   |     | temp | 1   | T   |     |     |
| ---- | ------ | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
timepointsforsubjectn.
GRU-D-Staticframework
GRU-D is a specialized variant of the Gated Recurrent Unit (GRU) designed to model multivariate time-series data with
missing values, where missingness may itself be informative17. A key limitation of the originalGRU-D frameworkis that
it can only handletemporaldata, as the decay mechanismrequiresthe time intervalvectorδ. To overcomethislimitation,
t
weintroducetheGRU-D-Staticframework,whichcombinesstaticfeatureembeddingswithanattentionweightfunctionthat
dynamicallyadjuststhecontributionoftemporalrepresentationsbasedonstaticcontext18.
ThecomponentoftheGRU-D-StaticframeworkforhandlingtemporalfeaturesfollowsthestandardGRU-Dformulation.
At each time stamp t, the model takes the temporalinput x ∈RU, the masking vector m ∈{0,1}U, and the time interval
|         |      |                                               |     |     |     |     | t   |     |     | t   |     |     |
| ------- | ---- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vectorδ | ∈RU. | Atrainableinput-decayisappliedcomponent-wise: |     |     |     |     |     |     |     |     |     |     |
t
|     |     |     |     |     |     |      | −ReLU(W |      | ∈RU,    |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------- | ---- | ------- | --- | --- | --- |
|     |     |     |     |     | γ t | =exp |         | γ δ) | t       |     |     |     |
|     |     |     |     |     |     |      | (cid:0) |      | (cid:1) |     |     |     |
andthedecayedinputusedbytheGRUcellis
|     |     |     |     | xd =m | ⊙x  | +(1−m)⊙ |     | γ ⊙x′+(1−γ)⊙x¯ |     | ,        |     |     |
| --- | --- | --- | --- | ----- | --- | ------- | --- | -------------- | --- | -------- | --- | --- |
|     |     |     |     | t     | t   | t       | t   | t              | t   | t t      |     |     |
|     |     |     |     |       |     |         |     | (cid:16)       |     | (cid:17) |     |     |
wherex¯ =(x¯ ,x¯ ,...,x¯ )T istheempiricalmeanoverallsubjects,x′=(x′ ,x′ ,...,x′ )T isthelastobservedvaluecarried
|     | t   | t1 t2 | tU  |     |     |     |     |     | t t1 | t2 tU |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- |
forward,and⊙denoteselement-wisemultiplication.
TheGRUgatesarecomputedas:
|     |     |     |     |          |               | W(x)xd+W(h)H |     | +W(m)m |         |            |     |     |
| --- | --- | --- | --- | -------- | ------------- | ------------ | --- | ------ | ------- | ---------- | --- | --- |
|     |     |     |     | R        | =σ            |              |     |        |         | +b ,       |     |     |
|     |     |     |     |          | t             | R            | t R | t−1    | R t     | R          |     |     |
|     |     |     |     |          | (cid:16)      |              |     |        |         | (cid:17)   |     |     |
|     |     |     |     | Z        | =σ            | W(x)xd+W(h)H |     | +W(m)m |         | +b ,       |     |     |
|     |     |     |     |          | t             | Z            | t Z | t−1    | Z t     | Z          |     |     |
|     |     |     |     |          | (cid:16)      |              |     |        |         | (cid:17)   |     |     |
|     |     |     |     | H˜ =tanh | W(x)xd+W(h)(R |              |     | ⊙H     | )+W(m)m | +b ,       |     |     |
|     |     |     |     | t        |               | t            |     | t      | t−1     | t          |     |     |
|     |     |     |     |          | (cid:16) H    | =(1−Z)⊙H     |     | +Z     | ⊙H˜     | . (cid:17) |     |     |
|     |     |     |     |          |               | t            | t   | t−1    | t t     |            |     |     |
Our GRU-D-Static framework incorporatesstatic features X ∈RV. These are first embedded via a fully connected
static
layerwithReLUactivation:
|     |     |     |     |     |     | φ static | =ReLU | W static | X static , |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | ---------- | --- | --- | --- |
thengenerateelement-wiseattentionweightsoverthefinalGR(cid:0)Uhiddensta(cid:1)te:
|     |     |     |     |     | α      | =σW |         | φ ∈Rdim(Ht). |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ------- | ------------ | --- | --- | --- | --- |
|     |     |     |     |     | static |     | att     | static       |     |     |     |     |
|     |     |     |     |     |        |     | (cid:0) | (cid:1)      |     |     |     |     |
Theattention-weightedtemporalrepresentationis:
Hatt=α
|     |     |     |     |     |     |     |     | static ⊙H. | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
t
Finally,Hattisconcatenatedwiththestaticembedding,passedthroughdropout,andmappedtotheoutput:
t
|     |     |     |     |     |     | H     | =concat | Hatt,φ  |         |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------- | ------- | ------- | --- | --- | --- |
|     |     |     |     |     |     | final |         | t       | static  |     |     |     |
|     |     |     |     |     |     |       |         | (cid:0) | (cid:1) |     |     |     |
4/11

Figure1. GRU-D-Staticframework
Yˆ =σW H
out final
This architecturein Figure 1 enablesthe static covariat(cid:0)esto (i) re(cid:1)weightthe temporalinformationvia the attention vec-
torα and(ii) contributedirectly throughφ , while preservingGRU-D’s ability to modeltemporaldependenciesand
static static
informativemissingnessinX .
temp
Allfeatureswerepreprocessedpriortomodeling:binaryfeatureswerecodedas1(“Yes”)and–1(“No”),andcontinuous
featureswerenormalizedtoa0–1rangeusingmin–maxscalingafterremovingoutliers22. Fortemporalfeatures,missingness
was explicitly modeled through masking features m and time intervals δ, which were incorporated via a trainable input-
t t
decaymechanismγ. Covariatescollectedafterthe occurrenceofthe outcomeweredeletedto preventinformationleakage.
t
Forparticipantswithfeaturesmissingatalltimepoints,aswellasforstaticfeatures,imputationwasperformedusingregion-
specific empirical population means for continuous features to prevent data leakage across regions, and zeros for binary
features.Inthisanalysis,missingnessacrossfeatureswasgenerallylow,withamean(SD)of4.1%(8.7%),andthemaximum
missingnessobservedwas37.2%.
Transferpredictionbyintegratingexternalscientificknowledge
Inreal-worldapplications,sourceandtargetdatasetsoftenexhibitnotabledifferencesinriskfactordistributionsandoutcome
prevalence.Whendatafromthetargetpopulationarescarceorentirelyabsent,applyingamodeltrainedsolelyonthesource
data can lead to suboptimal predictive accuracy23. To address this challenge, we aim to integrate summary-levelscientific
knowledge from the target domain to enhance the performance of a source-trained model. The PRISMA study collected
high-quality,large-scaledata frombothAfrican andAsian sites. For illustration, we first treatthe Asian data as the source
populationand the African data as the targetpopulation, under a hypotheticalscenario in which individual-leveldata from
the African sites are unavailable, while predictionsare still required. We then repeatthe analysis by reversing the roles of
the source and targetpopulations, treating the African sites as the source and the Asian sites as the target. To demonstrate
theperformanceoftheproposedtransferpredictionapproach,weevaluatedmodelvalidityunderthefollowinghypothetical
scenarios:
1. No individual-level target data are available, except for scientific knowledge regarding the association between the
outcomeandbasiccovariates.
5/11

Sourcedata Targetdata
{Xsource ,Ysource} {Xtarget ,Ytarget}
TrainGRU-D-Staticmodel Logisticregression
βˆ
target
Source-trainedmodel
θ(source) Softlabelsonsourcedata
pˆsource=σ(Xsourceβˆ target)
Fine-tunesource-trainedmodel
Input:Xsource
Target: pˆsource
Frozen:W γ,Rt,Zt,andHt
Updated:φ ,α ,classifier
static static
Adaptedmodel
θ(target)
Figure2. FlowchartoftransferpredictionframeworkforGRU-D-StaticbasedonScenario1and2
2. No individual-level target data are available, except for scientific knowledge regarding the association between the
outcomeandallcovariates.
3. Scientificknowledgeisavailable,alongwithbasiccovariatesinformationfromthetargetdata(labelsareunavailable).
To mimicthesummary-levelscientificknowledgeavailableonexternalresourcessuchasexistingliteratures,we fitamulti-
variatelogisticregressionmodelonthetargetdatasimilartopublicationsonclinicalandmedicaljournals:
Logit(Y )=X β
target target target
In Scenarios1 and 2, we first use the estimated coefficientsβˆ to generate predictedprobabilities pˆ for the source
target source
data. Thesepredictedprobabilitiesserveassoftlabels. Thenwecombinethesesoftlabelspˆ ,togetherwiththecovariates
source
X tofine-tunethesource-trainedGRU-D-Staticframework.TheworkflowforScenarios1and2isillustratedinFigure2.
source
InScenario3,sincepartialtargetdataisavailable,theestimatedcoefficientsβ ˆ areappliedtothepartialtargetcovariates
target
X toproducesoftlabels pˆ . ThesesoftlabelsalongwiththecorrespondingcovariatesX areusedtofine-tunethe
target target target
source-trainedmodel.Thepredictionperformanceisevaluatedonthetargetdataset.
In the fine-tuningprocess, the temporalparameterscapturedfromthe source data which includesthe parametersof the
decaymechanismW andtheGRUgatefunctionsR, Z, andH arefrozen. Insteadofupdatingonlythefinalclassification
γ t t t
layer,wealsofine-tunethestaticembeddinglayerφ andtheattentionweightmoduleα . Thisdesignallowsthemodel
static static
toadjusttheinfluenceofstaticfeaturesontemporalrepresentationswhilerefiningtheirembeddingstoreflectcharacteristics
specifictothetargetpopulationusingsoftlabelsderivedfromlogisticregressionmodelsfittedonthetargetdata,improving
predictiveperformanceonthetargetpopulation1. Ourfine-tuningdesignfollowsothercommontransferpredictionmethodol-
ogy,inwhichgeneralfeaturerepresentationsarefixedandthemorespecializedlayersareadjustedtocapturetarget-specific
patterns24.
6/11

Results
Inreal-worldapplications,themostcommonsituationcorrespondstoScenario1,wherenotargetdataaredirectlyavailable
exceptforexistingsummary-levelscientificknowledgeaboutassociationsbetweenthe outcomeandbasic covariateswhich
arereadilyavailable. IntheDPP-to-Wuhanexample,thesourceandtargetcohortscomefromdifferentstudieswithdistinct
protocols,measurementapproaches,andpopulationcharacteristics. Incontrast,thesourceandtargetcohortsinthePRISMA
study share the same protocol, identicaldata collectioninstruments, consistentvariabledefinitions, and comparablequality
standards. Consequently,thetransferlearningproblemaddressedhereis substantiallymorestraightforwardthan otherreal-
worldusecase. Withinthetargetdata,75%areusedtofitalogisticregressionmodelandtheremaining25%arereservedfor
performanceevaluation. Thelogistic regressionmodelincludesbasic covariates,such associo-demographiccharacteristics
andclinicalinformation.Theresultswithoutfine-tuningaresummarizedinthe“Baseline”columnofTable2,andtheresults
with fine-tuningareshowninthe“Basic”column. WhentheGRU-D-Staticmodelisfine-tunedusingthesourcecovariates
X andsoftlabelspˆ generatedfromthetargetlogisticregressionmodel,itspredictiveperformanceimprovessubstan-
source source
tially. For instance, when the Asian data are treated as the source populationand the African data as the targetpopulation,
the AUC increases from 0.738to 0.879for stillbirth, from 0.574to 0.602for maternalnear miss, and from 0.585to 0.665
for neonataldeath. Conversely,whenthe Africandata are treatedas the sourcepopulationand the Asian data as the target
population, the AUC increases from 0.946 to 0.983 for stillbirth, from 0.592to 0.668for preterm birth, and from 0.693 to
0.868forneonataldeath.
Toassessrobustnessoftheproposedtransferpredictionmethod,weadditionallyintroducenoisetotheexternalscientific
knowledgebyrandomlyflipping10%ofoutcomesinthetargetlogisticregressionmodelfittingtoreflectthefactthatsummary-
level associations in the literature may not match our targetpopulation100%. For example, publicationsoften reflect data
five to ten yearsagowhile researcherswantto makepredictionsforthecurrenttargetpopulation. Asshownin the “Noise”
column of Table 2, although there is a small drop of AUC from the "Basic" column without noise, the fine-tuned model
still outperformsthe baseline for all outcomes, indicating that the proposed transfer prediction approach remains robust to
moderatelabelperturbations.
To further assess the validity of our transfer prediction approach, we also examine Scenario 2, where no target data
aredirectlyavailable,exceptforsummary-levelscientificknowledgeregardingtheassociationbetweentheoutcomeandall
covariates.Similarly,withinthetargetdata,75%areusedtofitalogisticregressionmodelandtheremaining25%arereserved
forperformanceevaluation.Theresultsarepresentedinthe“All”columnofTable2. Thefine-tunedGRU-D-Staticframework
again outperformsthe source-trainedGRU-D-Static framework. Comparedwith Scenario 1, fine-tuningwith all covariates
yieldsslightlybetterpredictiveperformanceoverfine-tuningwithonlybasiccovariates.
Forcomparison,wealsoreporttheAUCresultsoftheGRU-D-Staticmodeltraineddirectlyonthetargetdata.Specifically,
75% of the target data are used for model training and the remaining 25% for performance evaluation. The results are
presented in the “Target” column of Table 2, which can be viewed as the upper-bound of the prediction performance for
transfer predictionmodels. Exceptfor the stillbirth outcomewhen African data are treated as targetpopulations, the ROC-
AUCvaluesobtainedfromthemodeltrainedonthetargetdataarenotsubstantiallydifferentfromthoseachievedunderthe
fine-tunedScenario1andScenario2,suggestingthattheproposedfine-tuningstrategycanapproximatetheperformanceofa
modeltraineddirectlyonthetargetdomain.
Inaddition,wereporttheROC-AUCresultsoflogisticregressionmodelsfitteddirectlyonthetargetdatausingthesame
setofbasiccovariates. Thetargetdatasetareagainsplitinto75%forfittinglogisticregressionand25%fortesting,andthe
resultsaresummarizedinthe“LR”columnofTable2.Thefine-tunedGRU-D-StaticmodelachievedhigherROC-AUCvalues
thanlogisticregression,indicatingthatourproposedtransferpredictionapproachprovidesbetterpredictiveperformancethan
aconventionallogisticregressionmethodthatdirectlyappliessummary-levelscientificknowledge.
InScenario3,weevaluatetransferpredictionwhenpartialcovariateinformationfromthetargetdataisavailable. Again,
withinthetargetdata,75%areusedtofitalogisticregressionmodelandtherest25%arereservedforperformanceevaluation.
A logistic regression model is fitted using the same basic covariates as in Scenario 1. Unlike Scenario 1, instead of using
X and pˆ ,wefine-tunetheGRU-D-StaticframeworkwithX andthesoftlabels pˆ . Weassessperformance
source source target target
when 5%, 10%, 20%, 50%, and 100% of the target data (used for fitting the logistic regression model) are employed for
fine-tuning.AsshowninTable3,performanceimprovesasmoretargetdataareincorporated.Notably,fine-tuningusingonly
10%ofthetargetdataachievingperformancecomparabletothatobtainedwiththefullsourcedataset.
Discussion
In this study, we extend the existing GRU-D framework, which was originally developed to handle longitudinaldata with
missingvalues. AkeylimitationoftheexistingGRU-Dframeworkisitsinabilitytoincorporatestaticfeatures,asthedecay
mechanismreliesontime intervals. To addressthis, we integratestatic featureembeddingswith attentionweight, allowing
7/11

Table2. ROC-AUContargetdataunderScenarios1and2
Asia(Source)&Africa(Target)
| Outcome                       | Baseline Basic | Noise All   | Target LR   |
| ----------------------------- | -------------- | ----------- | ----------- |
| Maternalnearmiss(8.6%)        | 0.574 0.602    | 0.595 0.608 | 0.616 0.584 |
| Stillbirth(2.7%)              | 0.738 0.879    | 0.829 0.881 | 0.961 0.831 |
| Lowbirthweight(14.7%)         | 0.830 0.842    | 0.831 0.848 | 0.847 0.832 |
| Smallvulnerablenewborn(25.2%) | 0.641 0.662    | 0.659 0.668 | 0.684 0.637 |
| Pretermbirth(8.2%)            | 0.682 0.695    | 0.692 0.691 | 0.702 0.645 |
| Neonataldeath(0.9%)           | 0.585 0.665    | 0.669 0.672 | 0.666 0.619 |
Africa(Source)&Asia(Target)
| Outcome                       | Baseline Basic | Noise All   | Target LR   |
| ----------------------------- | -------------- | ----------- | ----------- |
| Maternalnearmiss(5.0%)        | 0.637 0.657    | 0.654 0.661 | 0.673 0.634 |
| Stillbirth(1.3%)              | 0.946 0.983    | 0.966 0.986 | 0.980 0.979 |
| Lowbirthweight(24.4%)         | 0.808 0.838    | 0.831 0.835 | 0.835 0.834 |
| Smallvulnerablenewborn(34.4%) | 0.641 0.644    | 0.646 0.651 | 0.662 0.623 |
| Pretermbirth(16.7%)           | 0.592 0.668    | 0.658 0.667 | 0.681 0.663 |
| Neonataldeath(1.9%)           | 0.693 0.868    | 0.857 0.864 | 0.878 0.858 |
Note:Percentagesinparenthesesindicatetheprevalenceofoutcomesinthetargetdataset.
Table3. ROC-AUContargetdataunderScenario3
Asia(Source)&Africa(Target)
| Outcome                       | Baseline 5% | 10% 20%     | 50% 100%    |
| ----------------------------- | ----------- | ----------- | ----------- |
| Maternalnearmiss(8.6%)        | 0.574 0.588 | 0.587 0.597 | 0.593 0.589 |
| Stillbirth(2.7%)              | 0.738 0.849 | 0.895 0.913 | 0.921 0.917 |
| Lowbirthweight(14.7%)         | 0.830 0.842 | 0.835 0.845 | 0.840 0.845 |
| Smallvulnerablenewborn(25.2%) | 0.641 0.655 | 0.655 0.652 | 0.663 0.657 |
| Pretermbirth(8.2%)            | 0.682 0.685 | 0.689 0.692 | 0.695 0.691 |
| Neonataldeath(0.9%)           | 0.585 0.648 | 0.662 0.660 | 0.651 0.656 |
Africa(Source)&Asia(Target)
| Outcome                       | Baseline 5% | 10% 20%     | 50% 100%    |
| ----------------------------- | ----------- | ----------- | ----------- |
| Maternalnearmiss(5.0%)        | 0.637 0.644 | 0.659 0.653 | 0.657 0.655 |
| Stillbirth(1.3%)              | 0.946 0.969 | 0.974 0.983 | 0.980 0.982 |
| Lowbirthweight(24.4%)         | 0.808 0.827 | 0.832 0.836 | 0.834 0.837 |
| Smallvulnerablenewborn(34.4%) | 0.641 0.639 | 0.649 0.643 | 0.651 0.654 |
| Pretermbirth(16.7%)           | 0.592 0.663 | 0.665 0.664 | 0.665 0.667 |
| Neonataldeath(1.9%)           | 0.693 0.807 | 0.837 0.862 | 0.863 0.872 |
Note:Percentagesinparenthesesindicatetheprevalenceofoutcomesinthetargetdataset.
8/11

staticfeaturestomodulatetemporalrepresentations,andtherebyimprovingpredictiveperformance.
Wefurtherexploretransferpredictionacrossheterogeneouspopulationsbyincorporatingsummary-levelscientificknowl-
edge from the target domain. Specifically, we fine-tune the source-trained model using soft labels generated from logistic
regressionmodelsfittedonthetargetdata. AlthoughtheGRU-D-Staticframeworkisusedinthisstudy,theproposedtransfer
predictionstrategyismodel-agnosticandcanbeappliedtootherdeeplearningframeworks. Thisapproachenableseffective
modeladaptationevenwhenindividual-leveloutcomelabelsinthetargetpopulationareunavailable.InScenario1,ourresults
showthatfine-tuningwithbothsourcecovariatesandsoftlabelsyieldssubstantialimprovementsinpredictiveaccuracy,even
when10%ofoutcomesarerandomlyflippedtointroducenoise. InScenario2, slightlybetterperformancewhenallcovari-
ates,ratherthanonlybasiccovariatesareincludedinthetargetlogisticregressionmodel. Theproposedfine-tuningapproach
achievesperformancecomparabletomodelstraineddirectlyonthetargetpopulation,indicatingitseffectivenessinleveraging
scientificknowledgefordomainadaptation. Notably,whenpartialtargetdataareavailable,fine-tuningwithonly10%ofthe
targetdataachievesperformancesimilarlytothatobtainedusingthefullsourcedataset.
Insummary,themaincontributionsofthispaperare:
1. ExtendingtheGRU-Dframeworktoincorporatestaticfeaturesthroughstaticfeatureembeddingswithattentionweight.
2. Demonstrating the validity of transfer prediction across heterogeneous populations using soft labels derived from
summary-levelscientificknowledge.
3. Establishingbenchmarksforfine-tuningperformancewhenonlypartialtargetdataareavailable.
These findings suggest the potential that even limited summary-level information or external scientific knowledge can
enhancemodelpredictiveperformance,therebyreducingtherelianceonlarge-scaledatacollectioninunderrepresentedpopu-
lations. Theseresultsalsosupportfurtherevaluationoftheproposedapproachusingreal-worldexternalsummarysources.
9/11

References
1. Zhuang,F.etal. Acomprehensivesurveyontransferlearning. Proc.IEEE109,43–76(2020).
2. Iman,M.,Arabnia,H.R.&Rasheed,K. Areviewofdeeptransferlearningandrecentadvancements. Technologies11,
40(2023).
3. Peng, R. et al. Global burden and inequality of maternal and neonatal disorders: based on data from the 2019 global
burdenofdiseasestudy. QJM:AnInt.J.Medicine117,24–37(2024).
4. Ling, A. Y. et al. An overview of current methods for real-world applications to generalize or transport clinical trial
findingstotargetpopulationsofinterest. Epidemiology34,627–636(2023).
5. Gu, T., Lee, P. H. & Duan, R. Commute: communication-efficienttransfer learning for multi-site risk prediction. J.
biomedicalinformatics137,104243(2023).
6. Gu, T., Han, Y. & Duan, R. A transfer learning approach based on random forest with application to breast cancer
prediction in underrepresented populations. In PACIFIC SYMPOSIUM ON BIOCOMPUTING 2023: Kohala Coast,
Hawaii,USA,3–7January2023,186–197(WorldScientific,2022).
7. Group, D. P. P. R. Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. New Engl.
journalmedicine346,393–403(2002).
8. Liu,Q.etal. Predictingtheriskofincidenttype2diabetesmellitusinchineseelderlyusingmachinelearningtechniques.
J.Pers.Medicine12,905(2022).
9. Ma,F.etal. Riskpredictiononelectronichealthrecordswithpriormedicalknowledge. InProceedingsofthe24thACM
SIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining,1910–1919(2018).
10. Ploddi, K., Sperrin, M., Martin, G. P. & O’Connell, M. M. Scopingreview of methodologyforaiding generalisability
andtransportabilityofclinicalpredictionmodels. arXivpreprintarXiv:2412.04275(2024).
11. Manke-Reimers,F., Brugger, V., Bärnighausen,T. & Kohler, S. When, whyand howare estimated effectstransported
betweenpopulations?ascopingreviewofstudiesapplyingtransportabilitymethods. Eur.J.Epidemiol.1–19(2025).
12. Yao,Y., Zhang,Y., Li, X.& Ye, Y. Heterogeneousdomainadaptationvia softtransfernetwork. InProceedingsofthe
27thACMinternationalconferenceonmultimedia,1578–1586(2019).
13. Hinton,G.,Vinyals,O.&Dean,J.Distillingtheknowledgeinaneuralnetwork.arXivpreprintarXiv:1503.02531(2015).
14. Willard, J., Jia, X., Xu, S., Steinbach, M. & Kumar, V. Integrating scientific knowledge with machine learning for
engineeringandenvironmentalsystems. ACMComput.Surv.55,1–37(2022).
15. Islam,M.N.,Mustafina,S.N.,Mahmud,T.&Khan,N.I. Machinelearningtopredictpregnancyoutcomes:asystematic
review,synthesizingframeworkandfutureresearchagenda. BMCpregnancychildbirth22,348(2022).
16. Mangold,C. et al. Machinelearningmodelsfor predictingneonatalmortality: a systematic review. Neonatology118,
394–405(2021).
17. Che, Z., Purushotham, S., Cho, K., Sontag, D. & Liu, Y. Recurrent neural networks for multivariate time series with
missingvalues. Sci.reports8,6085(2018).
18. Shickel, B., Silva, B., Ozrazgat-Baslanti, T. et al. Multi-dimensional patient acuity estimation with longitudinal ehr
tokenizationandflexibletransformernetworks.frontdigithealth2022;4:1029191(2022).
19. Steinberg, E., Greenfield, S., Wolman, D. M., Mancher, M. & Graham, R. Clinical practice guidelines we can trust
(nationalacademiespress,2011).
20. Amos,R.C.,Jacob,H.&Leith,W. Jaundiceinnewbornbabiesunder28days: Niceguideline2016(cg98). Arch.Dis.
Childhood-EducationPract.102,207–209(2017).
21. Wei, Y. et al. Artificialintelligence-enabledpredictionof maternalnear miss and adverseneonataloutcomes: Insights
fromamulti-countrylmiccohort(2026). Unpublishedmanuscript.
22. Patro,S.&Sahu,K.K. Normalization:Apreprocessingstage. arXivpreprintarXiv:1503.06462(2015).
23. Hosna,A.etal. Transferlearning:afriendlyintroduction. J.BigData9,102(2022).
24. Yosinski, J., Clune, J., Bengio, Y. & Lipson, H. How transferable are featuresin deep neuralnetworks? Adv. neural
informationprocessingsystems27(2014).
10/11

Acknowledgements
The authors would like to thank the members and study participants of the Pregnancy Risk, Infant Surveillance, and Mea-
surement Alliance (PRISMA) for their time and efforts. This study would not be possible without the support of the Bill
&MelindaGatesFoundation,specificallyfromLauraLambertiandRichardZong. Theconclusionsandopinionsexpressed
in this work are those of the author(s) alone and shall not be attributed to the Foundation. Under the grant conditions of
theFoundation,aCreativeCommonsAttribution4.0LicensehasalreadybeenassignedtotheAuthorAcceptedManuscript
versionthatmightarisefromthissubmission.
Author Contributions Statement
Y.W.,Q.P.andF.J.developedthetransferlearningapproach;E.R.S.,Z.H.andQ.P.wrotetheglobalhealthbackgroundand
clinicalinterpretations;Y.W. carriedoutthesimulationandrealdata analyses; allauthorscontributedto thedata collection
andwritingofthemanuscript.
Funding Information
ThisworkisfundedbytheBillandMelindaGatesFoundationINV-041999(PI:EmilyR.Smith).
Data Availability
ThedatathatsupportthefindingsofthisstudyarecollectedbythePRISMAconsortium,butrestrictionsapplytotheavailabil-
ityofthesedata,whichwereusedunderlicenseforthecurrentstudyandsoarenotpubliclyavailable.Thedataare,however,
availableuponrequestandwiththepermissionofthePRISMAconsortium.
Human Subjects Research
Allmethodswerecarriedoutinaccordancewithrelevantguidelinesandregulations.ThePRISMAMNHstudywasapproved
by theGeorgeWashingtonUniversity’sCommitteeonHumanResearch(IRB: FWA00005945)onSeptember30, 2022and
receivedlocalandnationalethicalapprovalinPakistan(AgaKhanUniversityERC2022-5920-22763,andPakistanNational
BioethicsCommittee4-87/NBC-58/8/22/337),Kenya(KEMRIScientificandEthicsReviewUnitKEMRI/SERU/CGHR/04/10/358/4166;
Liverpool23-020),Zambia(UniversityofZambiaBiomedicalResearchEthicsCommittee:016-04-14andUniversityofNorth
Carolina Chapel Hill Office of Human Research Ethics: 356795), Ghana (Kintampo Health Research Centre Institutional
EthicsCommittee(IEC)FWA00011103;Ref0004854andGhanaHealthServiceEthicsReviewCommitteeFWA00020025),
Vellore,India(ChristianMedicalCollegeVelloreOfficeofResearchIRBNo14553),andHodal,India(EthicsReviewCom-
mittee,SocietyforAppliedStudies,SAS/ERC/ReMAPPStudy/2022).Informedconsentwasobtainedfromparticipantsatthe
timeoforiginaldatacollection.WorkinthismanuscriptiscoveredbytheIRBandinformedconsentsoftheoverallPRISMA
MNHstudy.
11/11
---- END DOCUMENT ----
