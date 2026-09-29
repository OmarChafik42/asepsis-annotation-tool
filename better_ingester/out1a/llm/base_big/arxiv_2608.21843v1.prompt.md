Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Debt relief and remittances can offset foreign aid cuts for most countries,
but some remain locked out
AndreaVismara1,3,*,RafaelPrieto-Curiel1,andRosieHayward2
1ComplexityScienceHub,Vienna,Austria
2SupplyChainIntelligenceInstituteAustria,Vienna,Austria
3UniversityofVienna,Vienna,Austria
*vismara@csh.ac.at
ABSTRACT
In2025,bilateralforeignaidwasreducedby23%,affectingmorethan130aidrecipientcountries. Weassesswhetherdebt
servicerelieforremittanceincreasescanmatchtheUSD26billioninaidlosses. Usinganetwork-shockmodelcalibratedto
bilateraldonors’individualcuts,weestimaterecipient-countryaidlossesandevaluatecompensationfeasibilityintermsof
annualdebtservicepaymentsthatwouldneedtobecancelledandremittancecapacity(theheadroombetweenflowsanda
theoreticalmaximuminwhicheveryworking-agemigrantsendsfunds)mobilisedtofinanciallyoffsetthem. Wefindthat18%
externaldebtservicereliefand10%ofremittancemobilisationcouldcompensatehalfoftheaffectedcountries. However,some
countriesremainlockedoutofeitherorbothmechanisms. Afundamentaltrade-offintheglobalfinancialarchitectureemerged
for large aid-cut losers: countries positioned to benefit from debt service relief lack large international diaspora networks
(limitingtheircapacitytoincreaseremittances),whilethosewithestablisheddiasporachannelsfacestructuralexclusionof
traditionaldebtmarkets,renderingdebtservicereliefineffective. Theseinsightsintroducenuanceinhowalternativefinance
sourcescanreplaceforeignaid.
Introduction andremittances12,13 havelongbeendiscussedassources
ofdevelopmentfinance.
Official development assistance is undergoing a major
External debt servicing costs relief operates directly
global retrenchment. As donor governments reduce aid
throughthegovernmentbudget. Fromapurelyfiscalper-
budgetsamidfiscalpressuresandshiftinggeopoliticalprior-
spective, a dollar not transferred to external creditors is
ities,thearchitectureofinternationaldevelopmentfinance
equivalenttoadollarreceivedinaid,insofarasbothexpand
isbeing reshaped. For manyrecipient countries, foreign
theresourcesavailablefordiscretionarypublicexpenditure.
aidfinancescoregovernmentfunctionsandessentialpublic
Thislogiciscloselyrelatedtothedebtoverhangliterature,
services,supportingbothdailypublicservicedeliveryand
whicharguesthatexcessiveexternaldebtconstrainsinvest-
longer-term development planning1,2. In the short term,
ment, public expenditure, and long-run development by
decliningexternalfinancereducestheresourcesavailable
divertingresourcestowarddebtservicingandweakening
for essential public services, including healthcare provi- incentivesforproductiveinvestment14. Empiricalevidence
sion3,anddisruptshumanitarianassistanceandemergency
frompastinitiativessupportsthisview. UndertheHeavily
response capacity4. Aid cuts thus raise urgent questions
IndebtedPoorCountriesInitiativeandtheMultilateralDebt
abouthowthelosseswillbeabsorbedandwhetheralterna-
ReliefInitiative,reductionsindebtburdenswereassociated
tivefinancialflowscanoffsetthem.
withincreasedpublicspendinginprioritysectorssuchas
While existing research has extensively analysed how healthandeducation,contributingtomeasurableimprove-
foreignaidstimulateseconomicgrowthandinvestment5, ments in human development indicators15,16. In several
howsovereigndebtburdensconstrainfiscalspaceandrisk aid-recipientcountries,externaldebtservicingpayments
default6,andhowremittancesserveasstabledevelopment alreadyabsorbasubstantialshareofnationalincome. For
finance7,theseliteratureshavelargelyevolvedinparallel. example, ElSalvador, Mozambique, andLebanonspend
Muchlessisunderstoodabouthowthesefinancialflows morethan20%oftheirGrossNationalIncome(GNI)an-
interact following a contraction in aid. This paper asks nuallyonservicingdebt. AccordingtoUNCTAD,around
whetheralternativesourcesofexternalfinance,specifically 3.4billionpeoplegloballyliveincountriesthatspendmore
externaldebtservicerelieforincreasedremittanceflows, moneyondebtservicingthanonhealth17. Areliefofdebt
couldcompensateforcountry-levelaidlossesandwhether servicingcostswouldthereforegeneratefiscalspaceequiva-
thefeasibilityofthesemechanismsvariessystematically lenttotheresourcesfreed,effectivelyrelaxinggovernment
acrossrecipientcountriesbasedontheirpositionswithin budgetconstraintsinasimilarwaytoaidinflows18.
globalfinancialnetworks. Whileneitherdebtreliefnorre- Remittanceshavealsolongbeendiscussedasanalterna-
mittanceinflowsconstitutesaperfectsubstituteforforeign tivetoforeignaid19. Crucially,theireffectondevelopment
aid,bothareincreasinglydiscussedaspartialcompensatory depends on the willingness and capacity of households
mechanismsforaidcuts8,9. Moreover,bothdebtrelief10,11 receiving remittance inflows to access fundamental ser-
1
6202
guA
22
]NG.noce[
1v34812.8062:viXra

vices20. Unconditional cash transfers lead to long-term Inaggregate,weestimatethat2025bilateralforeignaid
improvementsinfoodsecurityandleadtosignificantreduc- cutsaffected130aid-recipientcountriesforatotalofUSD
tionsinthechanceofchilddeath21,22. Similarly,increased 25.9billioninlosses. Thisisequivalenttoa9.5%reduc-
remittancesraisedisposableincome,reducepoverty23,in- tionofallforeignaidflowstothesecountriesinnominal
creaseaccesstohealthcare24,andsupportinvestmentsin terms. Syria,SouthSudan,andSomaliasufferedthelargest
infrastructure and human capital25,26. These effects oc- relativeimpact,alllosingmorethan4%ofGNI.Formany
curthroughbothdirectincomechannelsandindirectbe- affectedcountries,moderateadjustmentstodebt-servicing
havioural responses, such as increased school enrolment payments or remittance flows could offset aid losses. A
associatedwithadecreasedneedtoinvolvechildreninthe universalreliefof18%ofyearlyservicingpaymentscould
subsistenceeconomy27. Inpractice,anincreaseinremit- compensateroughlyhalfoftheaffectedcountries. Simi-
tancescouldbecomparabletodevelopmentassistancein larly,thiscouldbeachievedbymobilising10%ofremit-
theformofdirectcashtransfers,atypeofaidthatcanbe tance capacity, defined as the headroom between actual
distributedrapidlyinacrisis. Moreover,thereisevidence inflowsandatheoreticalmaximuminwhicheveryinterna-
that in fragile states without functioning central govern- tionalmigrantsendsremittances. However,forbothmech-
ment,societycanadapttofillthegapinprovidingfunda- anisms,18and16countries,respectively,faceaidlosses
mentalservices28. Remittancesconstituteamajorexternal largerthanthemaximumadditionalresourcesachievable.
sourceoffinancialflowsforaid-recipientcountries. Glob- Aidrecipientscanbeclusteredinfourgroups. Twogroups
ally,remittanceflowstolow-andmiddle-incomecountries showlowandmoderateexposuretoaidcuts. However,the
reachedapproximately$669billionin2023andwerepro- remainingtwogroupsfacestructuralchallenges. Aid-debt
jectedtoapproach$690billionin2024,farexceedingtotal constrained countries are largely Fragility, Conflict, and
aidinflowstothesecountries29. Thisquantitativedisparity Violence Affected Settings34 that receive emergency aid
highlightsthemacroeconomicsignificanceofremittances. andfeaturelargediasporas,yetarefundamentallyexcluded
Moreover,evidencehasshownthatmigrantsmobiliseremit- fromtraditionaldebtmarketsorhaverecentlyreceiveddebt
tanceresourcesfollowingeconomicdistressinthecountries relief. Onthecontrary,aid-remittanceconstrainedcoun-
oforigin, makingthesetransfersaformofinsurancefor triesarelargelySub-Saharancountriesthatmostlyreceive
lossessuchastheaidcuts30. aidforhealthandeducationprograms,havesignificantdebt
burdens,butlimitedremittancecapacity. Thisshowshow
While scholars have extensively studied aid effective-
countriesthatfindthemselvesinapositionofnotbeingable
ness5,31,sovereigndebtsustainabilityandrelief10,11,and
tobenefitfromdebtreliefbecauseofinstitutionalfragility
the developmental role of remittances7, a critical gap re-
tendtohavelargeestablisheddiasporasthatcouldsupply
mains. We lack spatially differentiated estimates of how
remittancefinance. Onthecontrary,countriesthatdonot
the current wave of aid cuts will reshape recipient coun-
haveestablisheddiasporaremittancechannelsavailableto
tries’positionswithinglobalfinancialnetworks. Aidcuts
sendmoneyalsotendtotakeupmoreexternalfinancing
arenotgeographicallyuniform,andtheirimpactsdepend
viadebt,whichcouldbeharnessedincaseofrelief.
oneachcountry’sspecificdonorcompositionandintegra-
tionintoalternativefinancialnetworksofdebtandremit-
Results
tances. Understanding this heterogeneity has profound
implicationsforidentifyingwhichcountriesfacedramatic Totalaidcutsforrecipients
welfare losses versus those with realistic compensatory ThepreliminarydataprovidedbytheOECDfor2025indi-
mechanisms. Thispapermakesthreecontributions. First,it cateanunprecedentedcontractioninOfficialDevelopment
estimatesrecipient-countrychangesinaidinflowsunderthe Assistance. Total net aid from Development Assistance
2025roundofforeignaidcuts. Weapplysender-specific Committeemembercountriesfellby23.1%inrealterms
shocksbasedonDevelopmentAssistanceCommitteebilat- comparedto2024,thelargestannualdeclineinthehistory
eraldonors’aidcutsin2025asrecordedintheOECDCred- ofaidandalevelofassistancefinancenotseensincethe
itorReportingSystem32. Thisnetwork-basedapproachto startofthe2030AgendaforSustainableDevelopment35.
aidtransfersallowsustocaptureboththeoverallmagnitude This decline was broad-based but heavily concentrated.
ofaidreductionsandtheheterogeneityarisingfromdiffer- While 26 of the 34 Development Assistance Committee
encesindonorcompositionandaidsectorsacrossrecipient membersreducedtheirforeignaidspending,thefivelargest
countries33. Second,webuildontheseestimatestoassess providers(UnitedStates,Germany,theUnitedKingdom,
whetherdebtrelieforincreasedremittancescouldplausibly Japan,andFrance)accountedfor95.7%ofthetotalcontrac-
offsetlosses,andforwhichcountries. Third,weclassify tion. IntheUnitedStates,theadministrationhaseffectively
recipientcountriesbasedontheirpotentialtocompensate dismantledtheUnitedStatesAgencyforInternationalDe-
forlossesthroughincreasedremittancesordebt-servicing velopmentandreducedforeignaidexpenditureby56.9%,
relief. Theanalysisrevealsdistinctgeographiesofvulnera- the largest reduction by any donor in any single year on
bilitytoaidcuts,aswellasindicatingwherepoliciesrelated record. The cuts reported by the remaining four largest
todebtorremittancescouldbemosteffective. donors, Germany (-17.4%), France(-10.9%), the United
2/20

Percentage GNI lost
Positive shock
0.0% - 0.1%
0.1% - 1.0%
1.0% - 2.5%
2.5% - 4.0%
> 4.0%
Figure1. Estimatedlossinbilateralforeignaidexpressedasapercentageoftherecipientcountry’sGNI.
Kingdom(-10.8%),andJapan(-5.6%),werealsosignifi- on remittances inflows and external debt servicing pay-
| cant. |     |     |     |     | ments. Theanalysisconcentratesonthese. |     |     | Ofthecountries |     |
| ----- | --- | --- | --- | --- | -------------------------------------- | --- | --- | -------------- | --- |
Humanitarian assistance was hit particularly hard, de- affectedbyaidcuts,40%areinSub-SaharanAfrica,fol-
|            |              |               |              |     | lowed by 17% | in Latin | America and | the Caribbean, | and |
| ---------- | ------------ | ------------- | ------------ | --- | ------------ | -------- | ----------- | -------------- | --- |
| clining by | 35.8% to USD | 15.5 billion. | Multilateral | aid |              |          |             |                |     |
fellforthesecondconsecutiveyear,down12.7%toUSD 15%inEastandCentralAsia. Theonlyfourcountriesthat
47.9billion,withcorecontributionstotheUNsystemsuf- experienced increases in aid transfers were Ukraine, the
|          |               |                   |           |     | Maldives, | Turkmenistan, | and Chad. | The distribution | of  |
| -------- | ------------- | ----------------- | --------- | --- | --------- | ------------- | --------- | ---------------- | --- |
| fering a | record annual | decline of 27.0%, | primarily | due |           |               |           |                  |     |
to an 87.2% cut by the United States35. The geographic absolute losses is right-skewed: the average loss among
reallocationofaidwasalsostark. Whileforeignaidtrans- affectedrecipientsstandsatapproximatelyUSD199mil-
ferstoUkrainesufferedduetothenear-collapseofUnited lion (USD 14 per capita), while the median is USD 106
Statescontributions(-91.1%),fundingfromEUInstitutions million(USD10percapita),indicatingthatasmallnumber
oflargeaidrecipientsaccountforadisproportionateshare
| surged(+65.2%). | Consequently,totalDevelopmentAssis- |     |     |     |     |     |     |     |     |
| --------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tance Committee support to Ukraine reached USD 44.9 ofaggregatelosses.
| billion in | 2025, an 18.7% | increase, | making Ukraine | the |     |     |     |     |     |
| ---------- | -------------- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
IndiaandSyriaarebothprojectedtohavelostcloseto
largestsinglerecipientofaidinanyyearonrecord. This USDonebillioneachinforeignaidtransfers,makingthem
volumesurpassedthecombinedaidtoallLeastDeveloped the largest losers in absolute terms, followed by Jordan,
Countries (USD 28.1 billion) and to all of Sub-Saharan Ethiopia,Turkey,andtheDemocraticRepublicofCongo,
Africa(USD29.2billion),bothofwhichexperiencedde- eachestimatedtohavelostbetween$936millionand$750
clinesofover22%. million. Thesecountriesarepredominantlylargerecipients
Giventhatdataoncountry-to-countryforeignaidflows of United States bilateral assistance, and their exposure
areunavailablebeyondtransferstoUkraine,weestimated reflectsthedisproportionateweightofthedefunctUnited
recipient-countryaidlossesusinganetworkshockmodel. StatesAgencyforInternationalDevelopmentintheiraid
Given the network of foreign aid transfers in 2024, we portfolios. Themacroeconomicsignificanceofforeignaid
lossesismostapparentwhenaidreductionsareexpressedas
| reduce each | edge proportionally | based | on the | bilateral |     |     |     |     |     |
| ----------- | ------------------- | ----- | ------ | --------- | --- | --- | --- | --- | --- |
donor’snon-Ukrainetotalaidcutinpercentage(seeMeth- ashareofGNI,giventhelargeshareofforeignaidtransfers.
ods). Therefore,recipients’lossesdependbothonthetotal Forinstance,foreignaidexceeds27%ofGNIintheCentral
relianceonforeignaidtransfers,aswellasthecomposition AfricanRepublic,approaches20%inSomalia,andremains
oftheirpoolofdonors. above10%incountriessuchasSouthSudan,Afghanistan,
|     |     |     |     |     | andLiberia. | Syriaisestimatedtohavesufferedthelargest |     |     |     |
| --- | --- | --- | --- | --- | ----------- | ---------------------------------------- | --- | --- | --- |
Intotal,bilateralforeignaidtransfershavebeenreduced
by USD 16.5 billion between 2024 and 2025. However, relativelosses,equivalentto5.25%ofitsGNIandcloseto
|     |     |     |     |     | USD44percapita(Figure1). |     | SouthSudanandSomalia |     |     |
| --- | --- | --- | --- | --- | ------------------------ | --- | -------------------- | --- | --- |
transferstocountriesotherthanUkrainefellby25.9billion
USD,reflectingthegeopoliticalredistributionofresource follow with GNI losses of 4.6% and 4.2% respectively,
flows. Atotalof130aid-recipientcountriesexperienced equivalenttoUSD44and27percapita. TheaverageGNI
lossis0.6%,whilethemedianis0.3%.
| some decline | in aid inflows | in 2025. | Of these countries, |     |     |     |     |     |     |
| ------------ | -------------- | -------- | ------------------- | --- | --- | --- | --- | --- | --- |
105havemorethanamillioninhabitantsandavailabledata Intermsoflossesbysectorofforeignaidtransfers,we
3/20

estimatethatthemostaffectedsectorsatthegloballevelare bilateralgovernments,multilateralinstitutions,and,increas-
“governmentandcivilsociety”,“emergencyresponse”,and ingly,China. Thespatialdistributionofdebtrelationsmat-
“health”,withlossesof10.2bn(-29%),5.5bn(-21%),and ters. For example, the Netherlands is the second-largest
4.2bn(-13%)respectively. Theonlysectorofaidtransfers creditorbythesizeofservicingpaymentsreceivedfromaid-
whichhasseenalargeincreaseis“generalbudgetsupport”, affectedcountries(USD25.8bnperyear). However,the
with12.7bn(+28.7%)inadditionaltransfersin2025. This largestpartofthesepaymentscomesfromcountriessuch
islargelyduetotheshiftinforeignaidtowardsUkraine. asBrazilthathaveminimalforeignaidlosses. Ontheother
hand,thethreelargestremainingcreditorsfromcountries
experiencingforeignaidlossesalsoshowthegreatestpoten-
Compensatingaidcutsviadebtrelief
|     |     |     |     |     |     |     |     | tialforcompensation. |     | ThesearetheInternationalBankfor |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------------------------- | --- | --- | --- |
TheOECD’sCreditorReportingSystemdatasetofforeign
ReconstructionandDevelopment,theInternationalMone-
aidtransfersreportsatotalofUSD323bnin2024,sentby
taryFund,andChina,whichreceived,respectively,50.7bn,
bilateral,multilateral,andprivatedonors,roughlyequiva-
|     |     |     |     |     |     |     |     | 41.2bn, | and 26.3bn USD | in debt-servicing |     | payments | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | ----------------- | --- | -------- | --- |
lentto0.3%ofworldGDPatthetime.Weestimatethetotal
2024. Ifthesethreeactorsweretoofferreliefonalltheir
reductionincountry-to-countryaidflowstobeequivalent
outstandingcreditpayments,theywouldcover54%,73%,
| toUSD25.9bn. |     | Forcomparison,thetotalannualexternal |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and52%ofthetotalaidlosses,respectively.
debtservicingpaymentsmadebycountriesthatsuffered
Theseheterogeneitiesintroduceissuesofdebtpolitics.
| from foreign | aid | cuts amounted |     | to USD | 274bn | in  | 2024. |               |         |                   |      |        |        |
| ------------ | --- | ------------- | --- | ------ | ----- | --- | ----- | ------------- | ------- | ----------------- | ---- | ------ | ------ |
|              |     |               |     |        |       |     |       | Historically, | lending | from institutions | such | as the | Inter- |
Thisisroughlyequivalentto11timesthesizeofaidlosses.
Thesenumbersshowthat,attheglobalscale,theresources nationalMonetaryFundandWorldBankwasassociated
|     |     |     |     |     |     |     |     | with structural | adjustment | programmes |     | involving | fiscal |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ---------- | --- | --------- | ------ |
fordebt-servicingpaymentsandrelieftooffsetaidlosses
|                 |     |               |     |         |          |     |          | consolidation, | market | liberalisation, | and | institutional | re- |
| --------------- | --- | ------------- | --- | ------- | -------- | --- | -------- | -------------- | ------ | --------------- | --- | ------------- | --- |
| exist. However, |     | the aggregate |     | picture | conceals | a   | critical |                |        |                 |     |               |     |
forms38,39.
Whileconditionalityhasevolvedconsiderably
| geographic | problem, | as  | access | to debt | relief | depends | on  |     |     |     |     |     |     |
| ---------- | -------- | --- | ------ | ------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
towardmoretargetedmacroeconomicandinstitutionalre-
eachdebtor’sspecificpositioninthedebtservicingnetwork,
|     |     |     |     |     |     |     |     | quirements, | these institutions | continue |     | to operate | within |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------ | -------- | --- | ---------- | ------ |
whichishighlyheterogeneous.
|     |     |     |     |     |     |     |     | frameworks | that link | financial support | to  | policy commit- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------------- | --- | -------------- | --- |
Toassessthepotentialofdebtservicingpaymentsrelief
ments. Theseinstitutionalframeworksmaylimittheextent
foreachaidrecipientcountry,weestimatewhichshareof
towhichbroaddebtservicereliefcanbeimplemented.
thedebtservicingpaymentswouldneedtobecancelledto
ChinahasalsobecomeamajorlenderthroughtheBelt
| fullyoffsetaidlosses(Figure2). |     |     |     | Wefindthatauniversalre- |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andRoadInitiative,withfinancinglargelyintheformof
liefof18%ondebt-servicingpaymentscouldoffsetlosses
|                                           |         |           |     |       |           |          |         | bilateralloansratherthandevelopmentgrants. |              |          |         | Compared |       |
| ----------------------------------------- | ------- | --------- | --- | ----- | --------- | -------- | ------- | ------------------------------------------ | ------------ | -------- | ------- | -------- | ----- |
| forhalfofthecountriesexperiencingaidcuts. |         |           |     |       |           | However, |         |                                            |              |          |         |          |       |
|                                           |         |           |     |       |           |          |         | with traditional                           | multilateral | lenders, | lending | from     | China |
| there are                                 | also 18 | countries | for | which | no amount |          | of debt |                                            |              |          |         |          |       |
generallyinvolvesdifferentformsofconditionality,with
| reliefwouldbesufficienttooffsettheaidlosses. |     |     |     |     |     | Prominent |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
greateremphasisonbilateralagreementsandproject-based
amongthesecountriesareSyria,Somalia,andAfghanistan,
|     |     |     |     |     |     |     |     | financing | rather than | broad macroeconomic |     | reform | pro- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------------------- | --- | ------ | ---- |
forwhichtheratioofannualdebt-servicingpaymentsto
|                                  |     |     |     |     |                  |     |     | grammes40,41. | Consequently, | China’s            | incentives | for              | pro- |
| -------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | ------------- | ------------- | ------------------ | ---------- | ---------------- | ---- |
| estimatedaidlossesislessthan12%. |     |     |     |     | Alltheothercoun- |     |     |               |               |                    |            |                  |      |
|                                  |     |     |     |     |                  |     |     | viding debt   | relief are    | rather constrained |            | by its strategic |      |
triesforwhichfulldebtreliefwouldnotbesufficientare
|                  |           |                                     |     |            |            |     |         | anddiplomaticinterests. |                  | Abroaderchallengeisthatthe |      |                    |        |
| ---------------- | --------- | ----------------------------------- | --- | ---------- | ---------- | --- | ------- | ----------------------- | ---------------- | -------------------------- | ---- | ------------------ | ------ |
| locatedinAfrica. |           | Theinsufficiencyoffulldebtrelieffor |     |            |            |     |         |                         |                  |                            |      |                    |        |
|                  |           |                                     |     |            |            |     |         | multilateral            | and bilateral    | creditors                  | with | the largest        | finan- |
| these 18         | countries | highlights                          |     | a critical | limitation |     | in cur- |                         |                  |                            |      |                    |        |
|                  |           |                                     |     |            |            |     |         | cial exposure           | in aid-recipient | countries                  |      | face institutional |        |
rentdevelopmentfinancediscourse,asdebt-servicingrelief
ormandate-basedbarrierstodebtrelief,whereaswealthy
mechanismsaremisalignedwiththefiscalrealitiesoffrag-
bilateraldonors,whocouldbebetterpositionedtoprovide
| ilestatesthatreceivelargeamountsofemergencyaid. |     |     |     |     |     |     | As  |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
debt-servicingrelief,arethemselvesscalingbacktheiraid
thesecountriesallallocatelessthan2%ofGNItodebtser-
budgets. Thepotentialfordebtservicerelieftoactasan
vicing,theyeffectivelyoperateoutsidethescopeinwhich
effectivecompensatorymechanismisthereforeconstrained
| relief can | serve | as a meaningful |     | counter-cyclical |     |     | tool in |     |     |     |     |     |     |
| ---------- | ----- | --------------- | --- | ---------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
byacombinationofinstitutionallendingmandatesandthe
| response | to aid | cuts. They | have | minimal | debt-servicing |     |     |     |     |     |     |     |     |
| -------- | ------ | ---------- | ---- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
complexpoliticaleconomyofglobaldevelopmentfinance.
capacitynotbecausetheyareheavilyindebted,butbecause
theylackstatecapacityandrevenuegeneration36.
Inthese
contexts, the debt relief mechanism is irrelevant as the Compensatingaidcutsviaremittances
centralproblemistheabsenceofcapacitytorebuildstate
Wenowturntoremittances,anotherlargesourceofexter-
institutions. Debtpolicycannotsubstituteforthesustained, nalfinanceforcountriesthatreceiveforeignaid. Thetotal
grant-basedfinancingthatfragilestatesrequiretodeliver
|     |     |     |     |     |     |     |     | remittance | flows to countries | that | suffered | from aid | cuts |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | ---- | -------- | -------- | ---- |
basicservices37.
amountedtoUSD632.2bnin2024,exceedingtheestimated
Thecreditorgeographyfurtherconstrainstheuseofdebt aidlossesbymorethantwenty-fold. Thisquantitativedis-
reliefas acompensatory mechanism. Countries affected parityinitiallysuggestsremittancescouldoffsetaidreduc-
byaidcutsareindebtedtoaheterogeneoussetofcreditors: tions. However, this aggregate comparison obscures the
4/20

A 105 countries with aid cut losses Creditor B
100% debt relief does not offset
aid losses for 18 countries
d
e
ta
s
n
e
p
m
o
c
y
llu 20% of debt relief
f
s
offsets aid losses
e for 56 affected
irtn countries
u Yearly debt servicing
o c payments received
fo from aid recipients
rN
Aid losses offset
under 100% debt
servicing costs relief
Percentage of universal debt servicing cost relief Billion USD
Figure2. Compensationofprojectedaidlossesthroughdebtservicepaymentsrelief. A-Percentageof2024debtservice
costsrelievedacrossallcreditors(horizontalaxis)andnumberofcountrieswhoseprojectedaidlosswouldbefullyoffsetatthe
givenreliefrate(verticalaxis). B-Top15creditorsbydebtservicingpaymentsreceivedfromcountriesaffectedbytheaidcuts.
Foreachcreditor,thebluebarshowsthetotal2024debtservicereceivedwhiletheorangebarshowstheamountofaidlosses
thatwouldbeoffsetifthecreditorprovidedfullreliefonalloutstandingclaims.
A 105 countries with aid cut losses B
100% mobilisation of remittances gap
does not offset aid losses for 16 countries
d
e
ta
s
n
e
p
m 20% usage of maximum
o remittances gap offsets
c
y
aid losses for 68
llu affected countries
f
s
e
irtn
u Aid loss
o
c Total remittances
fo
rN Maximum additional
remittances
Percentage of maximum remittance gap mobilised Percentage of GNI (%)
Figure3. Compensationofprojectedaidlossesthroughremittancemobilisation. A-Percentageoftotalremittancesgap
mobilised(horizontalaxis),andnumberofcountrieswhoseprojectedaidlosswouldbefullyoffsetatthatmobilisationrate
(verticalaxis). Thegapisdefinedastheremittanceinflowthatwouldbereceivedifallworking-agemigrantsweresending
money,minustherealisedinflowin2024. B-Top10recipientsbyaidlosstomaximumgapratio. Foreachrecipient,theblue
barshowsthe2025aidloss,theorangebarshowstotalremittancesin2024,andthegreenbarshowsthemaximumadditional
remittancesthatcouldbemobilised.
5/20

criticalrealitythatremittancesflowthroughspecific,histor- berofAfricancountries,notablyNigeria,Egypt,andKenya,
icallyembeddedmigrationcorridorsthatdonotnecessarily receivesubstantialinflows. Gulfstates’remittancessimi-
alignwiththegeographyofaidflows. Remittanceflows larlyflowpredominantlytoSouthandCentralAsia,where
aremostlyshapedbylabourmigrationsystemsanddepend largemigrantworkforcesareemployedinconstruction,do-
onthesize,history,andeconomicanddemographicchar- mesticwork,andhospitality. Theserealitiesshowthatthe
acteristics of each international migrant diaspora42. The countriesexperiencingthegreatestaidlossesoftenremain
concentration of remittance flows in a small number of onlyweaklyconnectedtoremittancecorridors.
| recipientcountriesreflectsthisspatialstructure. |             |     |        |        |     | Thetop       |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | ----------- | --- | ------ | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| five remittance                                 | recipients, |     | namely | India, | the | Philippines, |     |     |     |     |     |     |     |     |
VulnerabilityTypologies
| China, Pakistan, |     | and Bangladesh, |     | receive | 37% | of  | global |     |     |     |     |     |     |     |
| ---------------- | --- | --------------- | --- | ------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Debtrelieforincreasesinremittancescouldtheoretically
| remittances. | Thesefivecountriessharethecommonfeature |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofhavinglargediasporapopulationsconcentratedinhigh- offsetasubstantialportionoftheaidlossesprojectedfor
|                     |     |      |        |        |         |     |      | 2025. However,                   | this | picture | masks | considerable         |     | hetero- |
| ------------------- | --- | ---- | ------ | ------ | ------- | --- | ---- | -------------------------------- | ---- | ------- | ----- | -------------------- | --- | ------- |
| income destinations |     | such | as the | United | States, | the | Gulf |                                  |      |         |       |                      |     |         |
|                     |     |      |        |        |         |     |      | geneityacrossrecipientcountries. |      |         |       | Forsomecountries,the |     |         |
states,andAustralia.
requiredadjustmentsaremodestandplausiblyachievable.
Toassessthepotentialofremittanceflowstocompen-
Forothers,thescaleofrequiredcompensationissolarge
sateforaidlosses,wefirstestimatethetheoreticalupper
relativetotheirexistingdebtserviceobligationsordiaspora
boundofcountries’remittanceinflows,assumingthatev-
|                 |           |               |     |          |         |             |        | capacity                                 | for remittance | sending | that | neither | mechanism   |     |
| --------------- | --------- | ------------- | --- | -------- | ------- | ----------- | ------ | ---------------------------------------- | -------------- | ------- | ---- | ------- | ----------- | --- |
| ery working-age |           | international |     | migrant  | sends   | remittances |        |                                          |                |         |      |         |             |     |
|                 |           |               |     |          |         |             |        | offersarealisticprospectofclosingthegap. |                |         |      |         | Weconceptu- |     |
| monthly (see    | Methods). |               | The | headroom | between |             | actual |                                          |                |         |      |         |             |     |
alisecountries’vulnerabilitytoaidcutsasarisingfromthe
| remittance | inflows | and | the theoretical |     | maximum | defines |     |                                         |     |     |     |     |              |     |
| ---------- | ------- | --- | --------------- | --- | ------- | ------- | --- | --------------------------------------- | --- | --- | --- | --- | ------------ | --- |
|            |         |     |                 |     |         |         |     | intersectionofthreenetworkeddimensions: |     |     |     |     | themagnitude |     |
potentialremittancecapacitywhichcouldbemobilisedfor ofaidlossasashareofGNI,thedebt-compensationratio
| eachrecipientcountry. |     | Amodestuniversalmobilisationof |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(percentageofannualdebtservicepaymentsthatneedtobe
10%ofremittancecapacitywouldenablemorethanhalfof
cancelled),andtheremittancecompensationratio(capacity
thecountriesaffectedbyaidcutstofullycompensatethe
|     |     |     |     |     |     |     |     | neededtobemobilisedtooffsetlosses). |     |     |     |     | High(low)losses |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --------------- | --- |
loss(Figure3,panelA).However,aswithdebtservicing
|     |     |     |     |     |     |     |     | and high | (low) compensation |     | ratios | translate | into | higher |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | ------ | --------- | ---- | ------ |
relief,16countrieswouldnotreceiveenoughmoneyeven (lower)vulnerability.
| ifthefullpotentialgapweremobilised. |     |     |     |     | Thecountriesin |     |     |             |           |           |     |          |       |        |
| ----------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | ----------- | --------- | --------- | --- | -------- | ----- | ------ |
|                                     |     |     |     |     |                |     |     | To classify | countries | according |     | to these | three | dimen- |
thisgroupareallinAfrica,andtheoneswiththelargest
sions,weapplyk-meansclusteringtothelog-transformed
remaininggapsareDjibouti,Tanzania,Malawi,andZam-
|                 |       |           |     |         |          |     |       | and standardised | values | of  | the three | ratios | for all | coun- |
| --------------- | ----- | --------- | --- | ------- | -------- | --- | ----- | ---------------- | ------ | --- | --------- | ------ | ------- | ----- |
| bia. Crucially, | these | countries |     | are not | the same | as  | those |                  |        |     |           |        |         |       |
triesaffectedbytheaidcutsthathavemorethan1million
excludedfromcompensationthroughexternaldebtrelief.
|     |     |     |     |     |     |     |     | inhabitants. | The clustering |     | analysis | therefore | covers | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | -------- | --------- | ------ | --- |
Thelimitedcapacityforcompensationviaremittances
105countriesthatmeetthepopulationcriterionandhave
stems from two reinforcing constraints. First, migrants remittanceanddebtservicedataavailable. Thelogtrans-
frommanyaid-recipientAfricancountriesareconcentrated
|     |     |     |     |     |     |     |     | formation | is necessary | because | the | raw | distributions | are |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------- | --- | --- | ------------- | --- |
inneighbouringstates43,44.
RegionalmigrationwithinSub- heavily right-skewed (with a long tail of outliers repre-
| Saharan Africa |           | generates | substantially  |     | lower         | remittance |     |                                 |                     |     |        |                       |              |     |
| -------------- | --------- | --------- | -------------- | --- | ------------- | ---------- | --- | ------------------------------- | ------------------- | --- | ------ | --------------------- | ------------ | --- |
|                |           |           |                |     |               |            |     | sentinghighlyexposedcountries). |                     |     |        | Clusteringinlog-space |              |     |
| capacity than  | migration |           | to high-income |     | destinations, |            | as  |                                 |                     |     |        |                       |              |     |
|                |           |           |                |     |               |            |     | ensures                         | that these outliers |     | do not | dominate              | the distance |     |
it is concentrated in neighbouring countries where wage metric and that the resulting clusters reflect meaningful
| levels are | low, and | labour | market | formality |     | is reduced45. |     |     |     |     |     |     |     |     |
| ---------- | -------- | ------ | ------ | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
differencesratherthantheinfluenceofafewextremeob-
Forexample,Uganda’smigrantsarepredominantlyinthe servations. Weselectfourclusterstoproduceameaningful
| neighbouring | countries |     | Kenya, | Tanzania, | and | South | Su- |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ------ | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
interpretationofcountries’positioningintermsofoverall
dan. Second,remittanceparticipationisalreadyhighacross
|     |     |     |     |     |     |     |     | impactsandavailablecopingstrategies(Figure4). |     |     |     |     |     | Thisty- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | ------- |
manyoftheseregionaldiasporas,leavinglittleunusedca- pologyiscorroboratedbyaPrincipalComponentAnalysis
| pacitytobemobilisedinresponsetoaidcuts42. |     |     |     |     |     | Combined |     |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(PCA),whichshowsthat95.1%ofthevarianceiscaptured
withthelargeaidlosses,theseconstraintsleaveremittance bytwodimensionswhichcanbeinterpretedasi)thetotal
networkswithonlylimitedscopetocompensatefordeclin-
|     |     |     |     |     |     |     |     | magnitudeoftheaidcrisisfortherecipientcountry, |     |     |     |     |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
ingaid.
ii)theavailablecompensationmechanismsindebtreliefor
Thegeographyofremittance-sendingcountriesfurther remittancecapacitymobilisation. Ratherthanasingleclass
illustratesthisdisconnect. TheUnitedStates,SaudiArabia, ofhighlyvulnerablecountries, therearetwostructurally
and the United Arab Emirates are the largest remittance distinctformsofvulnerability. Countriesthatcannotoffset
senderstocountriesaffectedbyaidcuts. Yettheseflows aidlossesthroughdebtreliefaregenerallyabletomobilise
largelyfollowlong-establishedmigrationcorridorsrather remittances,whereascountrieswithlimitedremittanceca-
thanaidneeds. UnitedStatesremittanceoutflowsarecon- pacityremaincomparativelyintegratedintointernational
centrated in Latin America and parts of Asia, reflecting debtmarketsandcouldbenefitfromdebt-servicingrelief.
historicalimmigrationpatterns,whileonlyalimitednum- Theclusteringisrobusttoseveraltests(seeSupplementary
6/20

| A   |     | B Debt service relief to  | C Remittances gap mobilised  |     |
| --- | --- | ------------------------- | ---------------------------- | --- |
GNI lost from aid cuts (%)
|                  |            | compensate aid loss (%)   | to compensate aid loss (%) |          |
| ---------------- | ---------- | ------------------------- | -------------------------- | -------- |
| Median value     | Mean value |                           |                            |          |
|                  | D          |                           | Djibouti                   |          |
| Country clusters |            | Debt relief compensation  |                            | Tanzania |
Botswana
| Low exposure |     | available |     |     |
| ------------ | --- | --------- | --- | --- |
Costa Rica
|     |     | Brazil |     | Zambia |
| --- | --- | ------ | --- | ------ |
Moderate exposure
Argentina Angola
| Aid-debt constrained |     |     |     | Malawi |
| -------------------- | --- | --- | --- | ------ |
PCA
| Aid-remittances  | component 2:  | Malaysia |     | CAR |
| ---------------- | ------------- | -------- | --- | --- |
| constrained      | instrument    |          |     |     |
Burundi
available for
compensation China
South Sudan
Yemen
|     |     | Venezuela |     | Somalia |
| --- | --- | --------- | --- | ------- |
Afghanistan
Remittances compensation
|     |     | available |     | Syria |
| --- | --- | --------- | --- | ----- |
PCA component 1: vulnerability. Larger GNI loss, debt relief, and
remittances compensation ratios
Figure4. Characteristicsoftheclustersofcountries. PanelA,B,andC-Distributionofcountriesbyclusteraccordingto
percentageofGNIlostfromtheaidcuts,percentageofdebtreliefneededtooffsettheaidloss,andpercentageofthe
remittancesgapmobilisationneededtooffsettheaidloss,respectively(verticalaxesinlogscale). D-PCAdecompositionof
countryvulnerabilityprofiles(thefirsttwocomponents). Pointsarecolouredbyclusterandhorizontaldisplacementtrackstotal
impactmagnitude,whileverticaldisplacementdifferentiatescountriesbytheirprimarycopingcapacity: debtreliefversus
remittancepotential.
7/20

Material) nismbecomesentirelyunavailable.
Thefirstcluster,namedlowexposure,comprises22coun- Thethirdclustercomprisesaid-debtconstrainedcoun-
triesandrepresentsthelowestvulnerabilitygroup. Coun- tries and includes 16 members. For 11 of the 16 coun-
triesinthisgrouphaveameanGNIlossfromaidcutsof triesinthisgroup,theUnitedStateswasthetopbilateral
effectivelyzero, amediandebtreliefcompensationratio donorofforeignaid,whoseaidcutscontributetothelarge
of2.1%,amedianremittanceincreasecompensationratio losses. Thevastmajorityofcountriesinthisgrouparelow-
of 1.8%. These are predominantly large, upper-middle- or lower-middle-income and are located in Sub-Saharan
incomecountrieswhereforeignaidplaysaminimalrole, AfricaortheMiddleEastandNorthAfricaregion. Several
andwithsubstantialdomesticrevenuecapacityandrobust countries in this cluster are experiencing active conflict,
remittanceinflows. Geographically,thegroupisdominated state collapse, or severe humanitarian crises, with 10 of
byLatinAmericancountriessuchasArgentina, Mexico, the 16 members appearing on the World Bank’s list of
Brazil,Paraguay,andBolivia,aswellasSouthAsiancoun- Fragility, Conflict and Violence Affected Settings34. In-
triessuchasIndia,thePhilippines,Indonesia,andMalaysia. deed, eleven countries in this cluster receive most of the
China is also a member of this group, as it still receives aidforemergencyresponse(Figure5,panelB).Thecluster
transfersclassifiedasforeignaid. Mostlowexposurecoun- includesSyria,Somalia,Afghanistan,Sudan,SouthSudan,
triesaremembersofregionaltradeblocssuchasMERCO- andYemenamongothers. Thegroupischaracterisedbyan
SURandASEAN,areintegratedintoglobalvaluechains, inabilitytoleveragedebtreliefasacompensationmecha-
andbenefitfromwell-establisheddiasporacorridorswhich nismbutsubstantialcapacitytomobiliseremittances. The
allow the flows of financial resources and human capital medianGNIlossis1.7%,themediandebtreliefcompensa-
towards the country of origin46. The only sub-Saharan tionratio181.5%,andthemedianremittancecompensation
AfricancountriesappearinginthisclusterareGabonand ratio 13.3%. The median debt relief compensation ratio
EquatorialGuinea. Bothbenefitfromlargeoilrevenues, masksanevenmoreprofoundproblemforsomecountries.
up to 60% and 80%of government revenuerespectively, Syria and Somalia would require relief amounting to 30
andthusrelyfarlessonforeignaidasashareofeconomic times their annual service payments to offset aid losses.
outputthantheirregionalpeers. Afghanistanrequireseighttimestheamount. Thesereali-
tiesreflectdifferentpositions. Somaliarecentlyreceived
The second cluster, named moderate exposure, faces
a large debt relief package from the International Mone-
modestlylargerimpacts. Its42membersshowamedian
taryFundandtheUnitedStates47. Afghanistanisvirtually
GNIlossfromaidcutsof0.2%,amediandebtreliefcom-
lockedoutofinternationaldebtmarkets,whileSyriahas
pensationratioof12.2%,andamedianremittanceincrease
shifted its debt financing towards Iran and Russia while
compensationratioof6.1%. Geographically,thiscluster
almost stopping payments of old obligations. Universal
represents a transit zone between the low exposure and
debtreliefwouldbeineffectiveforthesecountries.
higher-vulnerabilitygroups. Mostofthecountriesincluded
herereceiveforeignaidtosustaineconomicactivitiesor Bycontrast,theremittancecompensationratioforaid-
general government functions (Figure 5). The group in- debt constrained countries remains low, meaning these
cludescountriesinCentralAsiasuchasGeorgia,Armenia, countriesrequireonlymodestincreasesinremittancemo-
Kyrgyzstan,andTajikistan,andWestandEastAfricasuch bilisation to offset aid losses. This reflects the presence
asGhana, Nigeria, andGuinea. Thegroupalsoincludes oflarge,establisheddiasporapopulationsinhigh-income
lower-middle-incomecountriesacrossLatinAmerica,such countries with significant opportunity to increase remit-
asColombia, Ecuador, Honduras, andNicaragua; South- tancesending. Thefundamentalproblemisnotatechnical
eastAsia,suchasCambodia,Laos,Myanmar,andVietnam; financinggapbutapoliticalone,asrebuildingstatecapacity
andSub-SaharanAfrica,suchasCameroon,Angola,and andestablishingformalremittancechannelsrequirespeace
Congo. Formoderateexposurecountries,theremittance andinstitutionalreconstruction48. Exceptionalmembersof
compensationratioisroughlyhalfthedebtreliefcompensa- this group are Moldova and Haiti. While Moldova is an
tionratio. Thisimpliesthatamodestpercentageofinterna- upper-middle-income European state, it is included here
tionalmigrantsactivatingtosendremittancescouldoffset as it receives large sums of aid due to the refugee crisis
the aid loss more easily than an equivalent proportional and energy security transitions, but its debt markets are
reductionindebtservicingpayments. Bothmechanisms narrow,makingitbehavestatisticallylikeanaid-debtcon-
offer plausible pathways to offset losses. Countries like strainedeconomy. Theinclusionhighlightsthatfragilityis
Honduras could achieve compensation through either a notexclusivelythedomainoflow-income,conflict-affected
28.4%debtservicingreductionora3.6%mobilisationof states. Similarly, Haiti’s presence underscores a state of
remittancecapacity. Cameroonwouldrequire12.8%debt long-terminstitutionaldecayandconflictinadifferentarea
reduction or 37.8% mobilisation of its remittance capac- oftheworld. Together,theseoutliersdemonstratethatthe
ity. Thissplitwithinthemoderateexposuregroupbetween aid-debtconstrainedlabelcapturesaspecifictypologyof
remittance-leveraged and debt-reliant cases foreshadows riskinasituationwheremacroeconomicleverslikedebt
theextremesofthesubsequentclusters,whereonemecha- servicereliefwouldfailtoaddressaidlosses.
8/20

Clusterfourincludesaid-remittancesconstrainedcoun- reducedexternalfinancingfor130ofthe134aidrecipient
triesandiscomposedof25members.Theclusterisdefined countries, resulting in aggregate losses of approximately
byastrikinggeographicconcentration,asallmembersare USD 25.9 billion. Syria, South Sudan, and Somalia are
locatedinSub-SaharanAfricawiththeexceptionofJordan. thethreehardest-hitcountriesintermsofGNIlost. Wear-
Countriesinthisgroupandareequallyspreadbetweenlow- guethatthesereductionsarebestunderstoodinthecontext
andlower-middleincome. ThemedianGNIlossforthis ofotheravailablesourcesofexternalfinance,andinthis
group is 1%, while the median debt relief compensation studywefocusonremittancesandexternaldebt-servicing
ratiois52.7%,andthemedianremittancegapmobilisation payments,twofinancialstreamsoftendiscussedasviable
ratiois226.7%. Thisfiguremeansthattherequiredmobili- alternativestolostdevelopmentfinance11,19. Contextual-
sationismorethantwicetheestimatedmaximumavailable isingaidcutswiththeseflowsprovidesasharperviewof
additionalremittancecapacity. Thegroupincludescoun- countries’overallvulnerabilityandthelimitsofpolicyin-
triessuchasBotswana,theCentralAfricanRepublic,Tan- terventions.Weshowthatwhilemodestadjustmentstodebt
zania,SierraLeone,Malawi,andKenya. Thevulnerability relieforremittancemobilisationcouldoffsetaidlossesfor
ofaid-remittancesconstrainedcountriesarisesfromthree manyaidrecipientcountries, someremainlockedoutof
reinforcinggeographicconstraints.First,thesecountriesex- compensationthroughthesetwomechanisms.
periencedlargebilateralaidcutsfromtheUnitedStatesbe-
WeclustercountriesbasedonGNIlostfromaidcuts,and
causeUnitedStatesAgencyforInternationalDevelopment
thedebtservicingrelieforremittancesmobilisationneeded
operationswerehistoricallyconcentratedinSub-Saharan
tooffsetthelosses,thusrevealingfourdistinctvulnerability
Africaforhealth,education,andgovernancesupport. In-
profiles. Forthefirstcluster,mostlyupper-middle-income
deed,forninecountriesinthiscluster,themajorityofaid
countrieswithlowexposuretoaidcuts,lossesrepresenta
comesforinterventionsinthehealthandeducationsectors
negligiblefractionofGNI.Formoderatelyexposedcoun-
(Figure5,panelB).Second, unlikeaid-debtconstrained
tries,aidlossesaresubstantial,butmanageableincreases
countrieswithdiasporaconcentratedinhigh-incomedesti-
inremittancesordebtreliefcouldoffsetthegap. However,
nations,Sub-SaharanAfricanmigrantsarepredominantly
theremainingtwogroupsofaid-debtconstrainedandaid-
locatedwithintheAfricanregion. Migrationcorridorsto
remittancesconstrainedcountriesfacebroaderchallenges.
high-incomeregionsremainlimitedtomostSub-Saharan
TheformeriscomposedlargelyofFragility,Conflict,and
Africansbyvisapolicyandhistoricallabourmarketintegra- Violence Affected Settings34 that receive emergency aid
tionpatterns49. Third,remittanceparticipationisalready
andfeaturelargediasporas,yetarefundamentallyexcluded
highamongAfricandiasporasacrosstheregion,meaning
fromtraditionaldebtmarketsorhaverecentlyreceiveddebt
thatmostemigrantsaresendingmoneyhome,leavingthe relief(e.g.,SomaliaunderHIPC)47.Onthecontrary,aid-
systemwithreducedcapacitytomobiliseincreasedflows42.
remittanceconstrainedcountriesaremostlySub-Saharan
However,therigidremittancenetworksarepartiallybal-
Africancountriesthatreceiveaidforhealthandeducation
anced by an institutional opening as these countries pos-
programs,havesignificantdebtburdens,butlimitedremit-
sessahigherdegreeoffiscallegibilitythantheirconflict-
tancecapacity. Thisisduetotheregionalconcentrationof
affectedpeers. Manyaid-remittancesconstrainedcountries
migrationcorridorsandthuslimitedeconomicopportunity,
carry substantial external debt payments to multilateral
coupledwithalreadyhighlevelsofremittancesparticipa-
creditors where relief is institutionally plausible, and to
tion.
China where restructuring has proven possible50. Thus,
whileaid-remittancesconstrainedcountriescanhardlyben- Ourfindingscontributetotheemergingliteratureonthe
consequencesofaidcuts51–53byanalysingtheconditions
efitfromcompensationofaidlossesviamoremobilisation
that contribute to countries’ vulnerability when external
inremittancesending, theyremainwithinthedebtrelief
assistanceiswithdrawn. Whileaidallocationsoftenreflect
framework. Theprimarypolicychallengeforthesenations
geopoliticalpriorities,commercialinterests,andlongstand-
isthereforenottherestorationofpeaceorstatelegitimacy,
ingasymmetriesintheinternationaldevelopmentarchitec-
buttheproactivenegotiationofdebt-servicesuspensionto
ture54,55,ourresultsshowthatrecipientcountries’exposure
providethefiscalbreathingroomthatremittancemobilisa-
toaidcutsisshapednotonlybythemagnitudeofaidthey
tionfailstooffer. Threeexceptionsstandoutinthecasesof
receive but also by their integration into overlapping in-
theCentralAfricanRepublic,Malawi,andZambia,where
ternational financial networks. In particular, two of the
neithertotaldebtservicingpaymentsreliefnorremittance
proposedmechanismsforcompensatingaidlossesrelying
mobilisationwouldofferenoughresourcestocompensate
on external finance, debt servicing relief8 and increased
the aid losses. These countries represent an exceptional
remittanceflows9,areavailabletodifferentgroupsofcoun-
pocketofvulnerability.
triesratherthanservingasuniversalsubstitutes. Inmany
conflict-affectedcountries,prolongedinstabilityhascon-
Discussion
tributedtotheemergenceoflargeinternationaldiasporas
Weestimatethatthe2025roundofbilateralforeignaidcuts whilesimultaneouslylimitingaccesstointernationalcapital
byDevelopmentAssistanceCommitteemembercountries marketsorresultinginrepeatedepisodesofdebtrelief,leav-
9/20

A Aid sector B Debt relief compensation
available
Emergency
Health &
Education
Government
le
v & Other
e l
la
E
In
c
fr
o
a
n
s
o
tr
m
u
i
c
c
t ure
ro PCA component
tc
e 2: instrument
s
ta
s
a
co
va
m
il
p
a
e
b
n
le
s a
fo
ti
r
o n
s
o
l
d
iA
Remittances compensation
available
Low Moderate Aid-debt Aid-remittances PCA component 1: vulnerability. Larger GNI loss, debt relief
exposure exposure constrained constrained and remittances compensation ratios
Figure5. Sectorallossesofaidbycluster. PanelAshowstheaggregateaidlossesbyclusterofcountriesandbymacrosector
ofaidtransfers. PanelBshowsthePCAdecompositionofcountries’positions,colouredbasedonthelargestsectorofaid
transfersreceived.
ingremittancesastheprincipalsourceofexternalfinance. analysedonlyatthelevelofthecentralgovernment,while
Bycontrast,manyaid-recipientcountriesinSub-Saharan fundamentalservicesmightbedeliveredbyregionalgov-
Africa remain more closely integrated into concessional ernments. Thepresentanalysisisvalidatacountry-level
lendingandmultilateralborrowingwhilemigrationremains scale,obscuringtherealityoflocalinequalities.
predominantlyregional,limitingthedevelopmentoflarge Futureresearchshouldprioritisethegenerationofsub-
remittancecorridorstohigh-incomeeconomies. Thesecon- nationalfinancialdataandinvestigatethedynamictransi-
trastingtrajectoriescreateasystematictrade-offbetween tionpathwaysofcountriesmovingbetweenvulnerability
thescopefordebtreliefandremittancemobilisation. clustersovertime. Exploringhowaidshocks, migration
Akeylimitationofouranalysisisthatneitherdebtre- dynamics,anddebtrenegotiationsinfluenceeachotherand
liefnorremittanceincreasesareperfectsubstitutesforaid reshapetheseprofileswillbevitalfordesigningmorere-
losses,althoughbothwerediscussedassourcesofdevelop- silientpoliciesfordevelopmentfinance.
mentfinancepriortotherecentaidshocks7,56. Debtrelief
hasamoredirectimpactonthestate’sbudget,asinprin-
Methods and Materials
cipleonedollarsavedfromdebtservicingpaymentscould
bedirectedtotheprojectsfinancedviaaidtransfers. How- WeusetheOECDCreditorReportingSystemasourpri-
ever, this transfer depends on the quality of government marysourceforbilateralOfficialDevelopmentAidflows60.
institutionsandpriorities, creatingapotentialobstacle57. TheCreditorReportingSystemrecordsindividualaidtrans-
Moreover, conditions similar to those imposed by donor fersatthetransactionlevel,identifyingthedonorandthe
countriesonaidrecipientscanbearequirementfordebt recipientcountry,thedisbursementamountincurrentUSD,
relief. Remittances,ontheotherhand,areaprivatetransfer theyear,andthesectororpurposeofthetransfer. Weuse
andtheireffectivenessfordevelopmentdependsonthewill- the2024disbursementdataasourbaseline,restrictingto
ingnessandcapacityofrecipienthouseholdstogainaccess transactionswithpositivedisbursementsandnon-missing
tofundamentalservices20. Moreover,remittanceflowsare recipient countries. The Creditor Reporting System cov-
notevenlydistributedwithinacountry,astheirinflowde- ers 134 unique aid recipient countries. Donors include
pendsonthedistributionofmigrants’origincommunities58. sovereigngovernments,UNagenciesandothermultilateral
Thisintroducesageographicproblem,asforeignaidtrans- organisations,multilateraldevelopmentbanks,andprivate
fers,especiallythosefinancingspecificprojects,arealso philanthropicfoundations.
unevenlydistributed.Forexample,evidencehasshownthat Dataonexternaldebtserviceobligationsaredrawnfrom
aiddoesnotflowtotheregionswherethepoorestpeople theWorldBankInternationalDebtStatistics. Weusetotal
live59. While data on the exact location of aid-financed debtserviceonexternaldebt,disaggregatedbycounterpart
projects is available, the lack of granular data on remit- creditoranddistinguishingbilateralfrommultilateralser-
tances prevents the development of more geographically viceflows.Weuse2024asthebaselineyear,forward-filling
refinedanalyses. Similarly,debtservicingburdenscanbe themostrecentavailableobservationwhere2024dataare
10/20

not yet reported. Counterpart categories corresponding anecessarysimplificationintheabsenceofrecipient-level
to bondholders, multiple lenders, and unallocated aggre- breakdownsintheOECDpreliminarydata.
gatesareexcludedfromthebilateralattributiontopreserve The total projected aid loss for recipient country j is
comparabilityacrossdebtorsandcreditors. Wefilledmiss- thereforegivenby:
ingdataforMalaysia,CostaRica,SouthSudan,Palestine,
| Namibia,Panama,andVenezuelausingalternativesources. |     |     |     |     |     |     |     |      |         |       |         |       |         | (j)  |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ----- | ------- | ----- | ------- | ---- |
|                                                     |     |     |     |     |     |     |     | Loss | =∑Aid   | −∑Aid |         | =∑Aid |         | ·c , |
|                                                     |     |     |     |     |     |     |     | j    | ij,2024 |       | ij,2025 |       | ij,2024 | i    |
| WecouldnotrecoverreliabledataforCubaandLibyaand     |     |     |     |     |     |     |     |      | i       |       | i       |       | i       |      |
| thetwocountriesaredroppedfromthecompensationand     |     |     |     |     |     |     |     |      |         |       |         |       |         | (3)  |
clusteringanalysis.
Bilateral remittance flows are obtained from a public wherec (j) denotestheeffectivecutrateappliedtotheedge
i
repositorywhichprovidesamodelledbilateralremittances
|     |     |     |     |     |     |     | (i,j). | Totallossesforrecipient |     |     | jthereforereflectbothits |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------- | --- | --- | ------------------------ | --- | --- | --- |
matrixforthe2010to2024periodatthemonthandcountry- absolutereceptionofforeignaidtransfersanditsexposure
pairlevel42. Themodelunderlyingtheseestimatesisde- tohigh-cutdonors.
scribedindetailintheSupplementaryMaterialandisaimed
Weestimatethedegreetowhichaidlossescouldbeoffset
at developing on the existing remittances model used by through each channel by constructing two compensation
| the | World Bank | to  | estimate | bilateral | remittance | flows61 |         |                                            |     |     |     |     |     |     |
| --- | ---------- | --- | -------- | --------- | ---------- | ------- | ------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
|     |            |     |          |           |            |         | ratios. | Thedebtreliefcompensationratioforrecipient |     |     |     |     |     | jis |
and now discontinued. Bilateral migrant stock data are thefractionofcurrentannualdebtservicethatwouldneed
drawnfromtheUnitedNationsInternationalMigrantStock
tobecancelledtofullyoffsettheprojectedaidloss:
dataset(2024revision),whichprovidesage-disaggregated
| countsofinternationalmigrantstocksbycountryoforigin |     |                                    |     |     |     |     |     |        | Loss j |     |     |     |     |     |
| --------------------------------------------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- |
|                                                     |     |                                    |     |     |     |     |     | φdebt= |        | ,   |     |     |     | (4) |
| anddestination.                                     |     | Thesestocksserveasareferencetocom- |     |     |     |     |     | j      | D      |     |     |     |     |     |
j
putethemaximumremittancepotentialforeachrecipient
country. where D j denotes total annual external debt service pay-
Donor-specific aid reduction rates were calibrated us- mentsbycountry jin2024. Avalueofφdebt=1implies
j
thatcancellingallcurrentdebtserviceobligationswould
ingtheOECDPreliminaryAidStatisticsfor2025,which
provide the first comprehensive realised estimates of aid exactlycompensatetheaidloss. The100%thresholdcon-
stitutesahardceilingonthecompensatorycapacityofthis
disbursementsacrossDevelopmentAssistanceCommittee
| membercountriesforthereferenceyear35. |     |     |     |     | Donor-specific |     | mechanism. |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
reductionrateswereadjustedtoexcludeUkraine-specific Themaximumremittanceceilingisdefinedbyassuming
assistanceandin-donorrefugeecosts,therebyrepresenting thatallinternationalmigrantsinagegroupspermittedto
theshareofaidreductionsexpectedtoaffectrecipientcoun- earn income in the destination country send money. We
tries. Completedetailsofthecutscalibrationprocedureare assume that every migrant who sends remittances trans-
providedintheSupplementaryMaterial. fers18%ofthemonthlypercapitaincomeofthecountry
Wequantifyrecipient-levellossesbyapplyingthedonor- ofdestination42. Thedifferencebetweenthehypothetical
maximumandtheestimatedremittanceflowsgiveseach
| specific | cut | rates to | the 2024 | Creditor | Reporting | System |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | -------- | -------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
bilateralaidnetwork. First,weisolatethereallocationof country’sremittancemobilisationcapacity. Fulldetailsof
|     |     |     |     |     |     |     | the | underlying | model, | assumptions, |     | and | calculations | are |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------ | --- | --- | ------------ | --- |
flowstowardUkrainefromthegeneralcontractioninaid.
Foreachdonoriwithavailablecutrateinformation,wefirst providedintheSupplementaryMaterial. Theremittance
applytheUkraine-specificratecUKRtoalledgesconnecting compensationratioforrecipient j isdefinedastheshare
i
oftheavailableremittancecapacitythatwouldneedtobe
thedonoritoUkraine:
mobilisedtofullyoffsettheaidloss:
|     |            |      |            | (cid:0) | (cid:1) |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ---- | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Aid        | =Aid |            | ·       | 1−c ,   | (1) |     |     |     |     |     |     |     |     |
|     | i,UKR,2025 |      | i,UKR,2024 |         | i,UKR   |     |     |     |     |     |     |     |     |     |
Loss
|     |     |     |     |     |     |     |     | φrem= | j   | ,   |     |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
j
| wherec                          | i,UKR | issigned,withnegativevaluesindicatingan |             |     |                 |     |       |     | G j                |     |      |         |     |          |
| ------------------------------- | ----- | --------------------------------------- | ----------- | --- | --------------- | --- | ----- | --- | ------------------ | --- | ---- | ------- | --- | -------- |
| increase                        | in    | flows, as                               | is the case | for | EU institutions | and |       |     |                    |     |      |         |     |          |
|                                 |       |                                         |             |     |                 |     | where | G   | is the mobilisable |     | gap. | A value | of  | φ rem =1 |
| severalEuropeanbilateraldonors. |       |                                         |             |     |                 |     |       |     | j                  |     |      |         |     | j        |
impliesthatthefullactivationofcurrentlynon-remitting
| Forallotherrecipients |     |     | j̸=Ukraine,theprojected2025 |     |         |     |                                           |      |             |             |     |        |          |         |
| --------------------- | --- | --- | --------------------------- | --- | ------- | --- | ----------------------------------------- | ---- | ----------- | ----------- | --- | ------ | -------- | ------- |
| transferis:           |     |     |                             |     |         |     | migrantswouldexactlycompensatetheaidloss. |      |             |             |     |        |          | Aswith  |
|                       |     |     |                             |     |         |     | the                                       | debt | ratio, 100% | constitutes |     | a hard | ceiling, | and the |
|                       |     |     | (cid:0)                     |     | (cid:1) |     |                                           |      |             |             |     |        |          |         |
Aid =Aid · 1−c , (2) tworatiosarethereforedirectlycomparableasmeasuresof
|     | ij,2025 |     | ij,2024 | i,non-UKR |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
feasibility.
wherec
i,non-UKR isthenon-Ukrainecutratedefinedinequa- Weclassifyrecipientcountriesintogroupsusingk-means
tion(8). DonorsnotpresentintheOECDpreliminaryta- clustering applied jointly to three dimensions: the debt
blesretaintheir2024disbursementlevelsunchangedinthe reliefcompensationratioφdebt,theremittancemobilisation
j
compensationratioφrem,andtheshareofGNIlosttoaid
| projection. |     | Theproportionalapplicationofauniformcut |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
rateacrossallnon-Ukrainerecipientsofagivendonoris cuts γ =Loss /GNI . Together, these three dimensions
|     |     |     |     |     |     |     |     | j   | j   | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
11/20

captureboththemagnitudeoftheshocksufferedbyanaid- RPC acknowledge financial support by the Asylum, Mi-
recipientcountryandthefeasibilityofoffsettingitthrough grationandIntegrationFundoftheEuropeanCommission
thetwoavailableexternalfinancechannels. together with the Federal Ministry of the Interior (grant
Priortoclustering,eachvariableislog-transformedto number2022-0.392.231). RPCisalsofundedbytheFed-
addressthepronouncedright-skewnessoftherawdistribu- eralMinistryforInnovation, MobilityandInfrastructure
tions, in which the majority of countries cluster near the (BMIMI)underthegrantnumberGZ2023-2.841.266.
originwhilealongrighttailrepresentshighlyexposedout-
liers. Formally,foreachvariablex∈{φ debt,φ rem,γ }we Competing interests
j j j
apply:
Theauthorsdeclarenocompetinginterests.
| x˜ =log(x | +ε), |     | (6) |         |           |     |     |
| --------- | ---- | --- | --- | ------- | --------- | --- | --- |
| j         | j    |     |     |         |           |     |     |
|           |      |     |     | Ethical | statement |     |     |
=10−6isasmallstabilityconstantaddedtoavoid
whereε
References
numericalissuesatzero.Thetransformedvariablesarestan-
dardisedtozeromeanandunitvariancebeforeclustering,
|     |     |     |     | 1. Marc´,Ł. | Theimpactofaidontotalgovernmentexpen- |     |     |
| --- | --- | --- | --- | ----------- | ------------------------------------- | --- | --- |
ensuringthatnosingledimensiondominatestheEuclidean ditures: Newevidenceonfungibility. Rev.Dev.Econ.
| distance | metric by virtue | of scale differences | alone. We |     |     |     |     |
| -------- | ---------------- | -------------------- | --------- | --- | --- | --- | --- |
21,627–663(2017).
selectfourclusterstoensurequalitativeinterpretabilityof
|     |     |     |     | 2. OECD. | Developmentco-operationreport2024: |     | Tack- |
| --- | --- | --- | --- | -------- | ---------------------------------- | --- | ----- |
theresults.
lingpovertyandinequalitiesthroughthegreentransi-
Wecomplementtheclusteringanalysiswithaprincipal
tion. Tech.Rep.,OECD(2024).
componentanalysisofthestandardised,log-transformed
features. The two leading components, which together 3. daSilva,A.F.etal. Impactoftwodecadesofhuman-
itariananddevelopmentassistanceandtheprojected
explain95.1%ofthetotalvariance,areusedtovisualise
theclusteringstructureandinterpretthedimensionsalong mortalityconsequencesofcurrentdefundingto2030:
whichthefourvulnerabilitytiersareseparated. Thefirst retrospectiveevaluationandforecastinganalysis. The
componentcapturestheoverallmagnitudeoftheburden LancetGlob.Heal.(2026).
acrossallthreedimensions,whilethesecondcapturesthe
4. Mbah,R.E.,Hardgrave,C.M.,Mbah,D.E.,Nutt,A.
contrastbetweentheavailabilityofcompensationthrough &Russell,J.G. TheimpactofUSAIDbudgetcutson
debtrelieforremittancesmobilisation,andistheprimary
|     |     |     |     | globaldevelopmentinitiatives: |     | areviewofchallenges, |     |
| --- | --- | --- | --- | ----------------------------- | --- | -------------------- | --- |
axisdistinguishingamongthemoreseverelyaffectedtiers.
|     |     |     |     | responses,andimplications. |     | Adv.Soc.Sci.Res.J.12, |     |
| --- | --- | --- | --- | -------------------------- | --- | --------------------- | --- |
219232(2025).
Data availability
5. Clemens,M.A.,Radelet,S.,Bhavnani,R.R.&Bazzi,
S. Countingchickenswhentheyhatch:Timingandthe
TheanalysisusespubliclyavailabledatafromtheOECD
TheEcon.J.122,590–617
CreditorReportingSystem,OECDPreliminaryaidStatis- effectsofaidongrowth.
(2012).
tics,theWorldBankInternationalDebtStatistics,andthe
United Nations International Migrant Stock dataset. Bi- 6. Panizza, U., Sturzenegger, F. &Zettelmeyer, J. The
lateral remittance estimates are publicly available42. All J.
economicsandlawofsovereigndebtanddefault.
derived datasets and code necessary to reproduce the economicliterature47,651–698(2009).
| main analyses | are available | in a permanent | repository |     |     |     |     |
| ------------- | ------------- | -------------- | ---------- | --- | --- | --- | --- |
7. Ratha,D.etal.Workers’remittances:animportantand
| on Zenodo | (https://doi.org/10.5281/zenodo. |     |     |                                           |     |     |        |
| --------- | -------------------------------- | --- | --- | ----------------------------------------- | --- | --- | ------ |
|           |                                  |     |     | stablesourceofexternaldevelopmentfinance. |     |     | Remit. |
22054992)
developmentimpactfutureprospects9,19–51(2005).
|         |                   |           |                  | 8. Miliband,D.          | Wecanrestructuredebtforhumanitarian |                          |             |
| ------- | ----------------- | --------- | ---------------- | ----------------------- | ----------------------------------- | ------------------------ | ----------- |
| Author  | contributions     |           |                  |                         |                                     |                          |             |
|         |                   |           |                  | ends.                   | FinancialTimes(2025).               | Accessed:                | 2026-07-01. |
| AV, RH, | and RPC conceived | the study | and designed the |                         |                                     |                          |             |
|         |                   |           |                  | 9. Huckstep,S.&Helen,D. |                                     | Afteraidcuts,here’showto |             |
analyses. AV and RH collected the data. AV performed makethemostoutofremittances.CGDEVBlog(2025).
| theanalyses. | AV,RH,andRPCwrotethemanuscript. |     | All |                               |     |             |     |
| ------------ | ------------------------------- | --- | --- | ----------------------------- | --- | ----------- | --- |
|              |                                 |     |     | UpdatedonMay22,2025.Accessed: |     | 2026-07-01. |     |
authorsreviewedandapprovedthefinalversion.
|     |     |     |     | 10. Addison, | T., Mavrotas, | G. & McGillivray, | M. Aid, |
| --- | --- | --- | --- | ------------ | ------------- | ----------------- | ------- |
debtreliefandnewsourcesoffinanceformeetingthe
Acknowledgements
|     |     |     |     | MillenniumDevelopmentGoals. |     | J.Int.Aff.113–127 |     |
| --- | --- | --- | --- | --------------------------- | --- | ----------------- | --- |
(2005).
OnbehalfoftheSupplyChainIntelligenceInstituteAustria
(ASCII),RHacknowledgesfinancialsupportfromtheAus- 11. Cordella,T.&Missale,A. Togiveortoforgive? Aid
trianFederalMinistryforEconomy,EnergyandTourism versusdebtrelief. J.Int.MoneyFinance37,504–528
| (BMWET)andtheFederalStateofUpperAustria. |     |     | AVand | (2013). |     |     |     |
| ---------------------------------------- | --- | --- | ----- | ------- | --- | --- | --- |
12/20

12. Bertram, G. “Sustainable development” in Pacific 28. Menkhaus, K. Governance without government in
micro-economies. WorldDev.14,809–822(1986). Somalia: Spoilers, statebuilding, andthepoliticsof
|              |     |        |         |         |        |     | coping. | Int.security31,74–106(2006). |     |     |     |     |     |
| ------------ | --- | ------ | ------- | ------- | ------ | --- | ------- | ---------------------------- | --- | --- | --- | --- | --- |
| 13. Poirine, | B.  | Should | we hate | or love | MIRAB? | The |         |                              |     |     |     |     |     |
Contemp.Pac.65–105(1998). 29. Mohapatra, S., Ratha, D. & Silwal, A. Remittances
|                |     |                                     |     |     |     |     | slowedin2023,expectedtogrowfasterin2024. |     |     |     |     |     | Mi- |
| -------------- | --- | ----------------------------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| 14. Krugman,P. |     | Financingvs.forgivingadebtoverhang. |     |     |     |     |                                          |     |     |     |     |     |     |
grationanddevelopmentBrief40,WorldBank(2024).
J.developmentEcon.29,253–268(1988).
|                |     |                                    |     |     |     |     | 30. Frankel,J. |     | Arebilateralremittancescountercyclical? |     |     |     |     |
| -------------- | --- | ---------------------------------- | --- | --- | --- | --- | -------------- | --- | --------------------------------------- | --- | --- | --- | --- |
| 15. Sachs,J.D. |     | Resolvingthedebtcrisisoflow-income |     |     |     |     |                |     |                                         |     |     |     |     |
OpenEcon.Rev.22,1–16(2011).
countries.Brookingspapersoneconomicactivity2002,
257–286(2002). 31. Burnside,C.&Dollar,D. Aid,policies,andgrowth.
Am.economicreview90,847–868(2000).
| 16. Boyce, | J. K. | & Ndikumana, |     | L. Africa’s | debt: | Who |     |     |     |     |     |     |     |
| ---------- | ----- | ------------ | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
oweswhom? Cap.flightcapitalcontrolsdeveloping 32. OECD. CreditorReportingSystem(CRS)Database.
countries334(2005). https://stats.oecd.org/Index.aspx?DataSetCode=CRS1
|             |     |         |          |        |       |        | (2026).                             | OfficialDevelopmentAssistance(ODA)sec- |     |     |     |             |     |
| ----------- | --- | ------- | -------- | ------ | ----- | ------ | ----------------------------------- | -------------------------------------- | --- | --- | --- | ----------- | --- |
| 17. UNCTAD. |     | A world | of debt. | Report | 2025, | United |                                     |                                        |     |     |     |             |     |
|             |     |         |          |        |       |        | toralandgeographicalflows.Accessed: |                                        |     |     |     | 2026-04-20. |     |
Nations(2026).
|           |     |            |           |      |           |     | 33. Hayward, | R., | Klimek, | P.&Naqvi, | A.  | UnitedStates |     |
| --------- | --- | ---------- | --------- | ---- | --------- | --- | ------------ | --- | ------- | --------- | --- | ------------ | --- |
| 18. Kose, | A., | Nagle, P., | Ohnsorge, | F. & | Sugawara, | N.  |              |     |         |           |     |              |     |
andEuropeanUnionaidcutsriskexacerbatinglinksbe-
| Global | waves | of debt: | Causes | and | consequences |     |     |     |     |     |     |     |     |
| ------ | ----- | -------- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tweenaid,trade,andhumanandenvironmentalcrises.
(WorldBankPublications,2021).
Commun.Sustain.1,12(2026).
| 19. Le Goff, | M.          | & Kpodar, | K.      | Do remittances |            | reduce |                  |     |                                 |            |             |     |         |
| ------------ | ----------- | --------- | ------- | -------------- | ---------- | ------ | ---------------- | --- | ------------------------------- | ---------- | ----------- | --- | ------- |
|              |             |           |         |                |            |        | 34. WorldBank.   |     | Fragility,conflict,andviolence: |            |             |     | Country |
| aid          | dependency? | IMF       | Working | Paper          | WP/11/246, |        |                  |     |                                 |            |             |     |         |
|              |             |           |         |                |            |        | classifications. |     | Brief,                          | WorldBank, | Washington, |     | DC      |
InternationalMonetaryFund(2011).
(2026).
| 20. Carling,J. |     | Remittances: | Eightanalyticalperspectives. |     |     |     |           |             |     |          |             |            |     |
| -------------- | --- | ------------ | ---------------------------- | --- | --- | --- | --------- | ----------- | --- | -------- | ----------- | ---------- | --- |
|                |     |              |                              |     |     |     | 35. OECD. | Preliminary |     | official | development | assistance |     |
InRoutledgehandbookofmigrationanddevelopment,
|     |     |     |     |     |     |     | levelsin2025. |     | DevelopmentCo-operationDirectorate |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------------------------- | --- | --- | --- | --- |
114–124(Routledge,2020).
reportDCD(2026)8,OECDPublishing,Paris(2026).
21. Aggarwal,S.,Aker,J.C.,Jeong,D.,Kumar,N.,Park,
|                             |     |     |     |                   |     |     | 36. Riddell, | R.  | Does | foreign aid | really work? |     | (Oxford |
| --------------------------- | --- | --- | --- | ----------------- | --- | --- | ------------ | --- | ---- | ----------- | ------------ | --- | ------- |
| D.S.,Robinson,J.&Spearot,A. |     |     |     | Thedynamiceffects |     |     |              |     |      |             |              |     |         |
UniversityPress,2008).
| ofcashtransferstoagriculturalhouseholds. |                             |     |     |     | Am.Econ. |     |                |                                     |     |     |     |     |     |
| ---------------------------------------- | --------------------------- | --- | --- | --- | -------- | --- | -------------- | ----------------------------------- | --- | --- | --- | --- | --- |
|                                          |                             |     |     |     |          |     | 37. Killick,T. | IMFprogrammesindevelopingcountries: |     |     |     |     |     |
| Journal:                                 | Appl.Econ.18,254–282(2026). |     |     |     |          |     |                |                                     |     |     |     |     |     |
Designandimpact(Routledge,2003).
| 22. Pega,F.,Liu,S.Y.,Walter,S.&Lhachimi,S.K. |     |     |     |     |     | Un- |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conditional cash transfers for assistance in humani- 38. Dreher,A. IMFconditionality: theoryandevidence.
Publicchoice141,233–267(2009).
| tariandisasters: |     | Effectonuseofhealthservicesand |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
healthoutcomesinlow-andmiddle-incomecountries. 39. Kentikelenis,A.E.,Stubbs,T.H.&King,L.P. IMF
CochraneDatabaseSystRev2015,CD011247(2015).
|            |     |             |     |         |           |     | conditionality |                                      | and | development | policy | space, | 1985– |
| ---------- | --- | ----------- | --- | ------- | --------- | --- | -------------- | ------------------------------------ | --- | ----------- | ------ | ------ | ----- |
|            |     |             |     |         |           |     | 2014.          | Rev.Int.Polit.Econ.23,543–582(2016). |     |             |        |        |       |
| 23. Mbaye, | L.  | M. & Drabo, | A.  | Natural | disasters | and |                |                                      |     |             |        |        |       |
poverty reduction: do remittances matter? CESifo 40. Himmer,M.&Rod,Z. Chinesedebttrapdiplomacy:
Econ.Stud.63,481–499(2017). Realityormyth? J.IndianOcean.Reg.18,250–272
(2022).
| 24. Amuedo-Dorantes, |     |     | C. & Pozo, | S. New | evidence | on  |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ---------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
theroleofremittancesonhealthcareexpendituresby 41. Watkins,M. Underminingconditionality? Theeffect
Mexican households. Rev. Econ. Househ. 9, 69–98 ofChinesedevelopmentassistanceoncompliancewith
| (2011). |     |     |     |     |     |     | WorldBankprojectagreements. |     |     |     | TheRev.Int.Organ. |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ----------------- | --- | --- |
25. Musah-Surugu, I. J., Ahenkan, A., Bawole, J. N. & 17,667–690(2022).
Darkwah,S.A. Migrants’remittances: Acomplemen- 42. Vismara,A.,Ali,O.,Källner,C.,Prieto-Viertel,G.&
tarysourceoffinancingadaptationtoclimatechange Prieto-Curiel,R.Migrantsasfirstresponders:Aglobal
Int.J.Clim.Chang.Strateg.
atthelocallevelinGhana. estimateofdisaster-drivenremittances. arXivpreprint
| Manag.10,178–196(2018). |     |     |     |     |     |     | arXiv:2512.16373(2025). |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
26. Salas,V.B. Internationalremittancesandhumancapi- 43. Tafani,I.,Ali,O.,Prieto-Curiel,R.&Riccaboni,M.
talformation. Worlddevelopment59,224–237(2014). Moststayclose,somegofar:Understandingmigration
|                                  |     |     |     |                |     |     | distanceinwestafrica. |     |     | EPJDataSci.(2026). |     |     |     |
| -------------------------------- | --- | --- | --- | -------------- | --- | --- | --------------------- | --- | --- | ------------------ | --- | --- | --- |
| 27. Gyimah-Brempong,K.&Asiedu,E. |     |     |     | Remittancesand |     |     |                       |     |     |                    |     |     |     |
investmentineducation: EvidencefromGhana. The 44. Schewel, K. & Debray, A. Global trends in South–
journalinternationaltrade&economicdevelopment Southmigration. ThePalgravehandbookSouth–South
| 24,173–200(2015). |     |     |     |     |     |     | migrationinequality153–181(2023). |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
13/20

| 45. Hujo, | K.&Piper, | N.  | South–Southmigration: |     | Chal- |
| --------- | --------- | --- | --------------------- | --- | ----- |
lengesfordevelopmentandsocialpolicy.Development
50,19–25(2007).
| 46. Kapur, | D. Diaspora, |     | development, | and democracy: |     |
| ---------- | ------------ | --- | ------------ | -------------- | --- |
Thedomesticimpactofinternationalmigrationfrom
India(PrincetonUniversityPress,2010).
| 47. InternationalMonetaryFund&WorldBank. |     |     |     |     | IMFand |
| ---------------------------------------- | --- | --- | --- | --- | ------ |
WorldBankannounceUS$4.5billionindebtrelieffor
| Somalia.(2023). |     | PressReleaseNo.23/438. |     |     |     |
| --------------- | --- | ---------------------- | --- | --- | --- |
48. Carment,D.&Calleja,R.Diasporasandfragilestates–
beyondremittancesassessingthetheoreticalandpolicy
| linkages.                 | J.Ethn.Migr.Stud.44,1270–1288(2018). |     |     |                     |     |
| ------------------------- | ------------------------------------ | --- | --- | ------------------- | --- |
| 49. Makina,D.&Mudungwe,P. |                                      |     |     | Patternsandtrendsof |     |
InternationalMigrationwithinandoutofAfrica(Rout-
ledgeLondon,2023).
| 50. Acker,K.,Brautigam,D.&Huang,Y. |     |     |                          | Debtreliefwith |     |
| ---------------------------------- | --- | --- | ------------------------ | -------------- | --- |
| Chinesecharacteristics.            |     |     | Tech.Rep.WorkingPaperNo. |                |     |
2020/39,ChinaAfricaResearchInitiative,Schoolof
| AdvancedInternationalStudies, |     |     |     | JohnsHopkinsUni- |     |
| ----------------------------- | --- | --- | --- | ---------------- | --- |
versity,Washington,DC(2020).
| 51. Gibson, | R.M.etal. |     | Theimpactofaidsanctionson |     |     |
| ----------- | --------- | --- | ------------------------- | --- | --- |
maternalandchildmortality,1990–2019:Apanelanal-
ysis. TheLancetGlob.Heal.13,e820–e830(2025).
| 52. Bulíˇr,A.&Hamann,A.J. |                              |     | Volatilityofdevelopment |              |     |
| ------------------------- | ---------------------------- | --- | ----------------------- | ------------ | --- |
| aid:                      | Fromthefryingpanintothefire? |     |                         | WorldDev.36, |     |
2048–2066(2008).
| 53. Agénor,P.-R.&Bayraktar,N. |     |                                     |     | Aidvolatility,human |     |
| ----------------------------- | --- | ----------------------------------- | --- | ------------------- | --- |
| capital,andgrowth.            |     | J.Hum.Cap.14,401–448(2020).         |     |                     |     |
| 54. McEwan,C.                 |     | Postcolonialismanddevelopment(Rout- |     |                     |     |
ledge,2008).
| 55. Lancaster,C. |     | Foreignaid: |     | Diplomacy,development, |     |
| ---------------- | --- | ----------- | --- | ---------------------- | --- |
domesticpolitics(UniversityofChicagopress,2008).
| 56. Hanlon,J. | Howmuchdebtmustbecancelled? |     |     |     | J.Int. |
| ------------- | --------------------------- | --- | --- | --- | ------ |
Dev.TheJ.Dev.Stud.Assoc.12,877–901(2000).
57. Moss,T.,PetterssonGelander,G.&VandeWalle,N.
| An  | aid-institutions | paradox? |     | A review essay | on aid |
| --- | ---------------- | -------- | --- | -------------- | ------ |
dependencyandstatebuildinginsub-SaharanAfrica.
Cent.forGlob.Dev.workingpaper11–05(2006).
| 58. Taylor,J.E. |           | Remittancesandinequalityreconsidered: |               |          |           |
| --------------- | --------- | ------------------------------------- | ------------- | -------- | --------- |
| Direct,         | indirect, | and                                   | intertemporal | effects. | J. Policy |
modeling14,187–208(1992).
| 59. Briggs,R.C. |     | Doesforeignaidtargetthepoorest? |     |     | Int. |
| --------------- | --- | ------------------------------- | --- | --- | ---- |
Organ.71,187–206(2017).
| 60. CongressionalResearchService.    |              |                                  |                | Foreignassistance: |         |
| ------------------------------------ | ------------ | -------------------------------- | -------------- | ------------------ | ------- |
| An                                   | introduction | to U.S.                          | programs       | and policy.        | Tech.   |
| Rep.IF10261,LibraryofCongress(2024). |              |                                  |                |                    | Updated |
| January24,2024.Accessed:             |              |                                  |                | 2026-04-21.        |         |
| 61. Ratha,                           | D. &         | Shaw,                            | W. South-South | migration          | and     |
| remittances.                         |              | 102(WorldBankPublications,2007). |                |                    |         |
14/20

Supplementary results where AGE is the donor’s grant-equivalent total ODA,
i
AUKR,GE
|       |          |      |            |     |     |             | is  | the Ukraine-specific |     |              | flow converted |     | to grant- |
| ----- | -------- | ---- | ---------- | --- | --- | ----------- | --- | -------------------- | --- | ------------ | -------------- | --- | --------- |
| A Aid | data and | cuts | estimation |     |     | i           |     |                      |     |              |                |     |           |
|       |          |      |            |     |     | equivalent, |     | and AIDRC            | is  | the in-donor | refugee        |     | cost. The |
i
DataonaidflowsaredrawnfromtheOECDDevelopment
non-Ukrainecutratefordonoriisthen:
AssistanceCommittee(DAC)’sCreditorReportingSystem
Ae x c l
(CRS).In2024,theCRSdatareportatotalofcirca323bil-
|                               |     |     |     |                     |     |     | cnon-UKR=1− |     | i, 2 0 25 | .   |     |     | (8) |
| ----------------------------- | --- | --- | --- | ------------------- | --- | --- | ----------- | --- | --------- | --- | --- | --- | --- |
|                               |     |     |     |                     |     |     | i           |     | Aexcl     |     |     |     |     |
| lionUSDinnominalaidtransfers. |     |     |     | Ofthissum,17percent |     |     |             |     |           |     |     |     |     |
i,2024
wenttolowincomecountries,43percenttolowermiddle
incomecountries,and39percenttouppermiddleincome The estimated grant-equivalent cuts for all recipients
countries. The regional distribution is also uneven, with beyond Ukraine are then used to estimated the recipient-
| Sub-SaharanAfricareceivingthelargestshareofaidwith |     |     |     |     |     | sidelosses. |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
26percent,followedbyEuropeandCentralAsiawith24
percent,andSouthAsiawith14.5percent. Globally,38.5 B Remittances and migrants stocks data
percentofaidwasdestinedforgeneralgovernmentsupport,
|              |                 |     |             |     |                 | The | global | remittance | dataset | used | for | this paper | spans |
| ------------ | --------------- | --- | ----------- | --- | --------------- | --- | ------ | ---------- | ------- | ---- | --- | ---------- | ----- |
| 35.9 percent | for investments |     | in economic |     | infrastructure, |     |        |            |         |      |     |            |       |
the2010to2024periodandisbasedontheworkofVis-
15.3percentforhealthandeducation,and10.3foremer-
al.42.
gencyresponses. TheCRSdatashowasteadyincreasein mara et We decide to rely on this dataset because
traditionaldatasourcesonremittances,namelytheWorld
ODAtransfersovertheperiod2010-2024,upuntilthecuts
in2025(figure1). However,theseyearsalsowitnesseda Bank’s KNOMAD bilateral remittances matrix, present
|               |       |            |         |           |          | twokeyproblems. |     |     | Thefirstrelatestodataavailability,as |     |     |     |     |
| ------------- | ----- | ---------- | ------- | --------- | -------- | --------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
| compositional | shift | as Ukraine | started | receiving | a larger |                 |     |     |                                      |     |     |     |     |
theworkofKNOMADhasbeendiscontinuedandthelast
shareofaidtransfersafterthebeginningofthewar,now
makingUkrainethelargestaidrecipientbyawidemargin. datasetreleasedisfortheyear2023. Thesecondrelates
tothedataproductionprocessitself,asKNOMADrelies
MostoftheincreaseintransferstoUkrainecomesfromthe
UnitedStates. Aftertheimplementationofthe2025cuts on a static gravity model estimation based only on bilat-
eralmigrantstocksandGDPdifferentialsbetweenorigin
thisrolehasbeenlargelytakenupbyEUinstitutions,as
|     |     |     |     |     |     | and | destination | country. |     | As documented |     | in the | paper42, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------------- | --- | ------ | -------- |
discussedinthepaper.
Wecalibratedonor-levelaidcutratesdirectlyfromthe thisapproachassumesarigidstructurewhereallinterna-
OECDPreliminaryODAStatisticsfor202535,whichpro- tionalmigrantsremitthusfailingtocapturethedifferences
videthefirstcomprehensiverealiseddataondisbursements arisingfromeconomicanddemographicstructureofeach
|                                              |     |     |     |     |     | diaspora. | To  | overcome | these | limitations, |     | the underlying |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | -------- | ----- | ------------ | --- | -------------- | --- |
| acrossDACmembercountriesforthereferenceyear. |     |     |     |     | We  |           |     |          |       |              |     |                |     |
dataframeworkutilizesanovelmonthlypanelcompilation
| draw on | three published |     | tables, each | covering | a distinct |     |     |     |     |     |     |     |     |
| ------- | --------------- | --- | ------------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
dimensionoftheaidcontraction: i)grant-equivalentODA ofbilateralremittanceflowscoveringapproximately36,000
observationsand$668billionacross2010to2019,which
totalsbydonor;ii)totalandUkraine-specificbilateralflows
isderivedfromnationalcentralbankreportingincluding
| on a net | disbursement | basis; | iii) | in-donor | refugee costs |     |     |     |     |     |     |     |     |
| -------- | ------------ | ------ | ---- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(IDRCs)bydonoronaheadlinemeasurebasis. outflowsfromItalyandinflowsfromMexico,Guatemala,
|     |     |     |     |     |     | Nicaragua, |     | the Philippines, |     | and | Pakistan. | The | method- |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- | --------- | --- | ------- |
Thethreetablesmeasureaidonpartiallydifferentcon-
ceptual bases, grant-equivalent, net disbursements, and ologymodelsinternationalmigrantsasindividualagents
|     |     |     |     |     |     | who | make | time-dependent, |     | binary | remittance |     | choices at |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | ------ | ---------- | --- | ---------- |
headline,andmustbereconciledbeforeapplicationtothe
|                   |                     |     |     |               |     | a monthly |     | frequency | following |     | a Bernoulli | process. | An  |
| ----------------- | ------------------- | --- | --- | ------------- | --- | --------- | --- | --------- | --------- | --- | ----------- | -------- | --- |
| bilateralnetwork. | Weproceedasfollows. |     |     | Foreachdonor, |     |           |     |           |           |     |             |          |     |
wecomputeagrant-equivalenttonet-disbursementscaling individualmigrant’smonthlyprobabilityofsendingremit-
tancesisgovernedbyalogisticfunctionincorporatingfive
ratiousingthe2024and2025totalsfromTables1and2
respectively. This ratio captures the degree to which the corecomponents: age-dependentearnings-to-consumption
ratios,theprobabilityofhavingfamilyinthedestination
donor’sportfolioisdominatedbyloansrelativetogrants,
country,GDPdifferentialsandabsolutepercapitaincome
| and is used | to convert | Ukraine-specific |     | bilateral | net dis- |     |     |     |     |     |     |     |     |
| ----------- | ---------- | ---------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
bursements onto a grant-equivalent basis comparable to levelsbetweenoriginanddestinationcountries,andtheoc-
currenceandmagnitudeoforigin-countrydisasters(floods,
| total ODA. | IDRCs | from | Table 2 | are treated | as already |     |     |     |     |     |     |     |     |
| ---------- | ----- | ---- | ------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
measuredonabasisclosetogrant-equivalentforbilateral storms,earthquakes,anddroughts). Thestructuralmodelis
calibratedtomatchthepanelofbilateralremittancesflows.
| grants-dominantdonors,andarededucteddirectly. |     |     |     |     | Where |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Thecalibratedmodel,withitseightparameters,isthenused
thescalingratioisunavailableduetomissingTable2en-
tries,wedefaulttoaratioofone,implyingthatthedonor’s toextrapolateamatrixoftheunobservedglobalbilateral
remittancedata,basedonthebilateralstocksofmigrants.
portfolioiseffectivelyall-grant.
Fromthesecomponents,weconstructforeachdonoran Globally, the United Nations migrants stock dataset
recordsatotalof282.8millioninternationalmigrantswith
effectiveaidtotalonagrant-equivalentbasisthatisstripped
|     |     |     |     |     |     | identifiablecountryoforiginanddestination. |     |     |     |     |     |     | Thedistri- |
| --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- |
ofbothUkraine-specificflowsandIDRCs:
butionisslightlyskewedtowardsmales,whomakeup52
Aexcl=AGE−AUKR,GE−AIDRC, (7) percent of the total migrant population compared to 48
| i   | i   | i   | i   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15/20

SupplementaryTable1. Donor-specificaidreduction thelargestshareat17.3%,followedbyGermanyat4.8%,
ratesfornon-Ukrainerecipients(2025,OECD SaudiArabiaat4.7%,Canadaat3.1%,andtheUnitedKing-
preliminary). dom at 3.1%. Concurrently, global remittance estimates
from2010to2024totalover9.19trillionUSDincumu-
Donor Estimatedaidchange(2025) lativevolume,displayingasteadyupwardtrendinyearly
remittancesfrom487.98billionUSDin2010toapeakof
Australia -2.4%
over747.65billionUSDby2023. In2024,7%ofthetotal
Austria -9.7%
flowswenttolowincomecountries,45%tolower-middle
Azerbaijan -26.2%
incomecountries,34%toupper-middleincomecountries,
Belgium -17.9%
and13%tohighincomecountries. Moreover,weestimate
Bulgaria -13.2%
thatifeveryinternationalmigrantofworking-agewereto
Canada -27.4%
sendremittances,therewouldhavebeenatotalflowof1.54
Croatia -7.1%
trillionUSD.Thedistributionoftheseflowsdependonthe
Czechia -1.2%
socio-economiccharacteristicsofeachbilateraldiaspora.
Denmark 4.3%
EUInstitutions -35.0%
Estonia -9.2% C Robustness tests for cluster profiles
Finland -5.5%
Toassesswhetherthefour-clustersolutionisrobusttok-
France -13.3%
meansinitialization,weperformedtenindependentcluster-
Germany -15.5%
ingrunswithdifferentrandomseeds.Allrunsproducedvir-
Greece -12.0%
tuallyidenticalclusterassignments,withameanAdjusted
Hungary 46.6%
Rand Index (ARI) = 0.993 for all pairwise comparisons.
Iceland -1.1%
Thestabilityindicatesthatthesolutionhasconvergedtoa
Ireland -7.4%
globaloptimumandisnotsensitivetothestartingconfigu-
Israel -10.2%
ration,eliminatingconcernsaboutlocalminimaartefacts.
Italy 2.9%
Additionally,were-scaledthelog-transformedfeatures
Japan -7.6%
usingthreealternativemethods: (i)RobustScaler(lesssen-
Kuwait -20.1%
sitive to outliers), (ii) MinMaxScaler (bounded scaling),
Latvia -24.5%
and(iii)StandardScaler(baselinez-scorenormalization).
Liechtenstein -4.9%
TheRobustScalerandStandardScalerproducedidentical
Lithuania -27.4%
clusterassignmentsusingk-means(ARI=1.0). TheMin-
Luxembourg 6.5%
MaxScalerproducedalmostidenticalassignment,withan
Malta -23.4%
ARI = 0.93. This invariance to scaling method confirms
Monaco 10.3%
thattheclusterstructurereflectsgenuinepatternsinthedata
Netherlands -1.2%
andisnotanartefactofthestandardizationprocedure.
NewZealand -19.9%
Weproceededbytestingwhetheralternativeclustering
Norway -1.6%
methodologiesproducedifferentresults. WeusedHierar-
Poland -13.7%
chicalAgglomerativeClustering(Wardlinkage)toparti-
Portugal -19.2%
tioncountriesintofourclusters. Thisproducedamoderate
Qatar 23.4%
agreementwithk-means(ARI=0.38,NormalisedMutual
Romania -7.7%
Information=0.57). Inspectionofthemismatchesreveals
Slovakia -7.1%
thathierarchicalclusteringpreservesthebroadtypologybut
Slovenia -8.0%
reallocatessomefringecountriesbetweenclusters. These
SouthKorea 4.1%
areprimarilycountriesattheboundarybetweenlowand
Spain 2.8%
moderateexposure,andbetweenmoderateexposureand
Sweden 5.5%
theconstrainedclusters. Thecoreinterpretationofthefour-
Switzerland -8.5%
clustertypologyremainsunchanged: hierarchicalmethods
Taiwan 5.2%
identifythesameunderlyingstructuralcontrasts(aid-debt
Turkey -9.0%
constrainedvs. aid-remittanceconstrainedvulnerability),
USA -55.4%
confirmingthesereflectgenuinepropertiesofthedatarather
UnitedArabEmirates 55.5%
thanak-means-specificartefact.
UnitedKingdom -10.9%
Tofurtherassessthestabilityofindividualcountryas-
signments,weperformed50bootstrapiterations,eachtime
removing10%ofcountriesrandomlyandre-clusteringus-
percentforfemales. Destinationsharesareheavilyconcen- ing k-means. For each country, we calculated a stability
tratedinmajoreconomies,withtheUnitedStateshosting score as the proportion of bootstrap iterations in which
16/20

itremainedco-clusteredwithitsoriginalneighbours. The D Principal Component Analysis
meanstabilityscoreis0.834(±0.061),indicatingthat83.4%
|               |               |     |                |           |      | We performed | a principal | component | analysis (PCA) | on  |
| ------------- | ------------- | --- | -------------- | --------- | ---- | ------------ | ----------- | --------- | -------------- | --- |
| of co-cluster | relationships |     | persist across | bootstrap | sam- |              |             |           |                |     |
thestandardised,log-transformedvaluesofthedebt-service
ples. Fivecountriesfallbelow70%stability(Azerbaijan,
compensationratio,remittancemobilisationcompensation
Nicaragua,Zimbabwe,Kyrgyzstan,Coted’Ivoire),suggest-
|     |     |     |     |     |     | ratio, and | share of GNI | lost to aid | cuts. The first | two |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | ----------- | --------------- | --- |
ingrobustcountry-levelassignmentsforthevastmajorityof
principalcomponentsexplained78.1%and16.9%ofthe
thesample.Eightfurthercountriesshowborderlinestability
totalvariance,respectively,accountingfor95.1%jointly.
(0.70–0.80),indicatingtheysitnearclusterboundariesbut
| remainconsistentlyassignedtotheirprimarycluster.     |     |     |     |     | This |                      |     |                        |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ---- | -------------------- | --- | ---------------------- | --- | --- |
|                                                      |     |     |     |     |      | SupplementaryTable2. |     | PCAloadingsandvariance |     |     |
| patternisexpectedanddiagnosticallyusefulasthesecoun- |     |     |     |     |      | explained            |     |                        |     |     |
triesrepresentgenuinelyambiguouscaseswherealternative
policynarrativescouldapply.
|     |     |     |     |     |     | Variable |     |     | PC1 | PC2 |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
Lastly,weevaluatedclusteringqualityusingthreestan- Debt-servicecompensationratio 0.577 −0.580
|     |     |     |     |     |     | Remittancemobilisationcompensationratio |     |     | 0.532 | 0.801 |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | ----- | ----- |
dardvalidationindices(SilhouetteScore,Davies–Bouldin
Index,andCalinski–HarabaszIndex)forK=3throughK=8. GNIlossshare(%) 0.620 −0.148
|                  |     |                   |     |         |            | Explainedvariance |     |     | 78.1% | 16.9% |
| ---------------- | --- | ----------------- | --- | ------- | ---------- | ----------------- | --- | --- | ----- | ----- |
| The five-cluster |     | solution achieved | the | highest | Silhouette |                   |     |     |       |       |
Score(0.36),whilethefour-clustersolutionperformedal-
most identically (0.345), indicating only a negligible re- PC1showedpositiveloadingsonallthreedimensions,in-
dicatingthatitprimarilyrepresentstheoverallmagnitudeof
| ductioninclustercohesionandseparation. |     |     |     | Althoughthe |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Davies–BouldinandCalinski–Harabaszindicesmarginally countries’exposuretotheaidshockandthecompensation
|                                   |     |     |     |                     |     | requiredtooffsetit. | PC2showedoppositeloadingsforthe |     |     |     |
| --------------------------------- | --- | --- | --- | ------------------- | --- | ------------------- | ------------------------------- | --- | --- | --- |
| favourK=3,thedifferencesaresmall. |     |     |     | Incontrast,thefour- |     |                     |                                 |     |     |     |
debt-servicecompensationratio(−0.580)andremittance
clustersolutionprovidesaricherandmorepolicy-relevant
interpretationbydistinguishingbetweendebt-constrained mobilisationcompensationratio(0.801),whiletheloading
|     |     |     |     |     |     | onGNIlosswascomparativelysmall(−0.148). |     |     | Thisindi- |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --------- | --- |
andremittance-constrainedvulnerabilityprofilesthatare
catesthatPC2primarilyrepresentsacontrastbetweenthe
mergedunderK=3orseparatedwithoutaclearnarrative
relativefeasibilityofcompensationthroughdebt-servicere-
| underK=5. | Increasingthenumberofclustersbeyondfour |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
liefandremittancemobilisation.Countriesrequiringhigher
doesnotimproveclusteringqualityandinsteadaddscom-
plexitywhileyieldinglimitedadditionalsubstantivediffer- remittancemobilisationcompensationlieontheopposite
sideofPC2fromthoserequiringhigherdebt-servicerelief,
| entiation. | WethereforeadoptK=4asthepreferredbalance |     |     |     |     |     |     |     |     |     |
| ---------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reflectingfundamentallydifferentconstraintsoncompensa-
betweenstatisticalperformanceandinterpretability.
tioncapacity.
| The robustness |     | tests collectively |     | show that | the four- |     |     |     |     |     |
| -------------- | --- | ------------------ | --- | --------- | --------- | --- | --- | --- | --- | --- |
clustertypologyisarobustempiricalfindingratherthana
| contingentoutcomeofmethodologicalchoices. |     |     |     |     | Theclus- |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
teringisinsensitivetoinitialization,scaling,andalternative
| clusteringapproaches. |     | Whilealternativemethodsproduce |     |     |     |     |     |     |     |     |
| --------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
moderatedisagreementonfringecases,theypreservethe
coretypologicaldistinctionascountriesdivideintothose
withlowandmoderateexposureandthosecapableofoff-
settinghighaidlossesalternativeviadebtservicingrelief
| orremittancemobilisation. |            |          | Theinvarianceacrossmethods |           |      |     |     |     |     |     |
| ------------------------- | ---------- | -------- | -------------------------- | --------- | ---- | --- | --- | --- | --- | --- |
| provides                  | confidence | that the | conceptual                 | framework | cap- |     |     |     |     |     |
turesgenuine,replicablepatternsinhowexposuretoaid
shocksinteractswithembeddednessintootherexternalfi-
| nance networks. |     | The primary | policy | implication | is that |     |     |     |     |     |
| --------------- | --- | ----------- | ------ | ----------- | ------- | --- | --- | --- | --- | --- |
whileindividualcountryclassificationsforborderlinecases
couldreasonablyshiftunderalternativespecifications,the
| broad typology | is  | stable. Policy | interventions |     | can there- |     |     |     |     |     |
| -------------- | --- | -------------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- |
forebedesignedaroundcluster-levelcharacteristicswith
confidencethattheunderlyingvulnerabilitystructuresper-
sist. Table3reportsthedetailedresultsforeachofthe107
aidrecipient’sestimatedlossesinpercentageofGNIand
| the potential | for | compensation | via debt | cancellation | and |     |     |     |     |     |
| ------------- | --- | ------------ | -------- | ------------ | --- | --- | --- | --- | --- | --- |
remittancesgaputilisationalongsideclusterassignment.
17/20

A Income classification of B
recipient country
High Income
Upper-middle Income
Lower-middle Income
Low Income
SupplementaryFigure1. Timeseriesofforeignaidtransfers. PanelAshowstheevolutionovertime(2010-2024)of
aggregateaidtransfersbyincomegroupofthereceivingcountry. PanelBshowsthetop10aidrecipientovertimebyabsolute
volumeoftransfers,depictingtheshiftinprominenceofUkraine.
18/20

SupplementaryTable3. CountriesaffectedbyprojectedODAcutsin2025byvulnerabilitycluster
Country AidLoss2025 DebtCancellation RemittancesPotentialActivation Cluster
|                | (%GNI) | needed(%GNI) | needed(%GNI) |                            |
| -------------- | ------ | ------------ | ------------ | -------------------------- |
| Syria          | 5.25   | 3525.34      | 7.78         | aid-debtconstrained        |
| SouthSudan     | 4.60   | 490.71       | 64.39        | aid-debtconstrained        |
| Somalia        | 4.18   | 3093.77      | 21.52        | aid-debtconstrained        |
| Afghanistan    | 3.17   | 835.67       | 8.87         | aid-debtconstrained        |
| Burundi        | 3.17   | 192.45       | 86.00        | aid-debtconstrained        |
| Liberia        | 2.40   | 123.59       | 65.82        | aid-debtconstrained        |
| Timor-Leste    | 1.98   | 146.86       | 5.49         | aid-debtconstrained        |
| Lebanon        | 1.73   | 159.12       | 14.00        | aid-debtconstrained        |
| Eritrea        | 1.69   | 157.65       | 3.53         | aid-debtconstrained        |
| Yemen          | 1.60   | 242.23       | 8.59         | aid-debtconstrained        |
| Haiti          | 1.28   | 61.16        | 5.72         | aid-debtconstrained        |
| Moldova        | 1.26   | 48.19        | 12.63        | aid-debtconstrained        |
| Sudan          | 0.99   | 247.42       | 19.85        | aid-debtconstrained        |
| Palestine      | 0.89   | 330.89       | 4.91         | aid-debtconstrained        |
| Ethiopia       | 0.74   | 76.92        | 26.07        | aid-debtconstrained        |
| Zimbabwe       | 0.55   | 170.58       | 14.25        | aid-debtconstrained        |
| CAR            | 3.06   | 157.90       | 420.37       | aid-remittancesconstrained |
| Mozambique     | 2.95   | 65.82        | 441.07       | aid-remittancesconstrained |
| Malawi         | 2.67   | 178.07       | 1454.37      | aid-remittancesconstrained |
| Lesotho        | 2.56   | 63.19        | 226.66       | aid-remittancesconstrained |
| Jordan         | 1.80   | 57.54        | 57.57        | aid-remittancesconstrained |
| Zambia         | 1.53   | 134.41       | 1084.57      | aid-remittancesconstrained |
| Gambia         | 1.38   | 60.86        | 81.33        | aid-remittancesconstrained |
| Rwanda         | 1.24   | 71.89        | 200.27       | aid-remittancesconstrained |
| Congo,Dem.Rep. | 1.11   | 163.06       | 82.57        | aid-remittancesconstrained |
| Niger          | 1.03   | 52.66        | 329.62       | aid-remittancesconstrained |
| Madagascar     | 1.02   | 63.38        | 190.03       | aid-remittancesconstrained |
| BurkinaFaso    | 0.98   | 66.78        | 40.55        | aid-remittancesconstrained |
| Mali           | 0.97   | 68.35        | 46.50        | aid-remittancesconstrained |
| Eswatini       | 0.96   | 27.67        | 993.10       | aid-remittancesconstrained |
| Senegal        | 0.96   | 17.23        | 58.40        | aid-remittancesconstrained |
| SierraLeone    | 0.87   | 45.17        | 136.59       | aid-remittancesconstrained |
| Togo           | 0.82   | 30.39        | 52.35        | aid-remittancesconstrained |
| Uganda         | 0.77   | 34.75        | 548.49       | aid-remittancesconstrained |
| Tanzania       | 0.69   | 32.55        | 1645.17      | aid-remittancesconstrained |
| Namibia        | 0.68   | 42.24        | 376.28       | aid-remittancesconstrained |
| Benin          | 0.63   | 20.05        | 52.15        | aid-remittancesconstrained |
| Djibouti       | 0.63   | 23.23        | 1713.53      | aid-remittancesconstrained |
| Mauritania     | 0.59   | 15.84        | 235.31       | aid-remittancesconstrained |
| Kenya          | 0.49   | 20.25        | 68.37        | aid-remittancesconstrained |
| Botswana       | 0.15   | 11.08        | 248.01       | aid-remittancesconstrained |
| Honduras       | 0.72   | 28.41        | 3.56         | moderateexposure           |
| NorthMacedonia | 0.67   | 15.83        | 4.62         | moderateexposure           |
| Tunisia        | 0.61   | 11.88        | 28.97        | moderateexposure           |
| Laos           | 0.58   | 14.23        | 9.67         | moderateexposure           |
| Mongolia       | 0.58   | 9.08         | 25.33        | moderateexposure           |
| Bosnia         | 0.53   | 18.79        | 3.00         | moderateexposure           |
| ElSalvador     | 0.50   | 16.16        | 1.30         | moderateexposure           |
| Armenia        | 0.47   | 16.65        | 9.04         | moderateexposure           |
| Georgia        | 0.45   | 17.13        | 15.75        | moderateexposure           |
| Coted’Ivoire   | 0.42   | 8.87         | 40.91        | moderateexposure           |
| Guinea-Bissau  | 0.40   | 32.68        | 6.44         | moderateexposure           |
| Nepal          | 0.40   | 42.63        | 4.73         | moderateexposure           |
| Guinea         | 0.38   | 22.02        | 13.00        | moderateexposure           |
Continuedonnextpage
19/20

SupplementaryTable3(continued)
Country AidLoss2025 DebtCancellation RemittancesPotentialActivation Cluster
|                   | (%GNI) | needed(%GNI) | needed(%GNI) |                  |
| ----------------- | ------ | ------------ | ------------ | ---------------- |
| Nigeria           | 0.38   | 18.27        | 12.99        | moderateexposure |
| Cameroon          | 0.36   | 12.81        | 37.76        | moderateexposure |
| Tajikistan        | 0.35   | 26.09        | 8.77         | moderateexposure |
| Myanmar           | 0.31   | 24.41        | 7.53         | moderateexposure |
| Albania           | 0.29   | 12.53        | 2.96         | moderateexposure |
| Cambodia          | 0.29   | 24.09        | 8.10         | moderateexposure |
| Serbia            | 0.26   | 10.87        | 5.80         | moderateexposure |
| Ghana             | 0.24   | 34.86        | 7.03         | moderateexposure |
| Kyrgyzstan        | 0.23   | 9.71         | 6.26         | moderateexposure |
| Morocco           | 0.21   | 6.31         | 4.23         | moderateexposure |
| Egypt             | 0.20   | 3.01         | 5.90         | moderateexposure |
| Nicaragua         | 0.20   | 5.30         | 1.34         | moderateexposure |
| PapuaNewGuinea    | 0.19   | 9.68         | 22.19        | moderateexposure |
| Jamaica           | 0.18   | 3.86         | 1.40         | moderateexposure |
| Uzbekistan        | 0.17   | 5.71         | 6.03         | moderateexposure |
| Guatemala         | 0.16   | 24.74        | 1.93         | moderateexposure |
| Mauritius         | 0.15   | 2.33         | 8.36         | moderateexposure |
| Congo             | 0.14   | 2.09         | 5.57         | moderateexposure |
| SouthAfrica       | 0.14   | 13.34        | 27.76        | moderateexposure |
| Angola            | 0.13   | 0.99         | 11.93        | moderateexposure |
| Bangladesh        | 0.13   | 14.18        | 5.43         | moderateexposure |
| Colombia          | 0.13   | 5.41         | 4.04         | moderateexposure |
| Ecuador           | 0.13   | 3.93         | 2.52         | moderateexposure |
| Iraq              | 0.12   | 9.63         | 4.57         | moderateexposure |
| Peru              | 0.08   | 11.27        | 3.42         | moderateexposure |
| Vietnam           | 0.08   | 6.45         | 2.27         | moderateexposure |
| Turkey            | 0.06   | 7.75         | 7.43         | moderateexposure |
| CostaRica         | 0.05   | 3.07         | 39.82        | moderateexposure |
| Venezuela         | 0.03   | 254.22       | 1.03         | moderateexposure |
| Panama            | 0.09   | 1.74         | 4.21         | lowexposure      |
| SriLanka          | 0.09   | 3.36         | 2.29         | lowexposure      |
| Bolivia           | 0.07   | 2.19         | 2.63         | lowexposure      |
| DominicanRepublic | 0.07   | 5.31         | 0.78         | lowexposure      |
| Paraguay          | 0.07   | 2.96         | 2.25         | lowexposure      |
| Pakistan          | 0.06   | 1.93         | 1.36         | lowexposure      |
| Gabon             | 0.05   | 1.42         | 7.77         | lowexposure      |
| Belarus           | 0.04   | 0.96         | 2.22         | lowexposure      |
| Philippines       | 0.04   | 5.41         | 1.05         | lowexposure      |
| Azerbaijan        | 0.03   | 1.88         | 1.45         | lowexposure      |
| India             | 0.03   | 5.37         | 3.25         | lowexposure      |
| Algeria           | 0.02   | 14.95        | 1.66         | lowexposure      |
| Brazil            | 0.02   | 1.04         | 10.67        | lowexposure      |
| EquatorialGuinea  | 0.02   | 0.79         | 1.01         | lowexposure      |
| Indonesia         | 0.02   | 3.68         | 7.55         | lowexposure      |
| Iran              | 0.01   | 11.32        | 1.82         | lowexposure      |
| Kazakhstan        | 0.01   | 0.95         | 0.43         | lowexposure      |
| Mexico            | 0.01   | 3.14         | 0.24         | lowexposure      |
| Thailand          | 0.01   | 5.14         | 2.18         | lowexposure      |
| Argentina         | 0.00   | 0.14         | 1.77         | lowexposure      |
| China             | 0.00   | 1.75         | 0.25         | lowexposure      |
| Malaysia          | 0.00   | 0.02         | 0.07         | lowexposure      |
20/20
---- END DOCUMENT ----
