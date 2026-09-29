Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Building A CSFQ-Inspired Transport for Switched CXL Memory Pooling
ZeruiGuo1,EmilyShriver2,andMingLiu1
1UniversityofWisconsin-Madison 2Intel
Abstract beingdeveloped,evaluated,andsampled.
EmergingswitchedCXLmemorypoolingsystems,albeit However,memorypooling,especiallyunderswitchedde-
promising,sufferfromsignificantperformanceinterference ployment,suffersfromsignificantperformanceinterference.
due to the shared but performance-uncontrolled data path Unlikelocalmemoryconnectedviadedicatedmemorybuses,
amongconcurrentmemorystreamsbetweenahostcoreand thedatapathbetweenahostcoreandaremoteCXLDIMM
aremoteDIMM.Wesystematicallycharacterizeamemory under switched pooling is shared among concurrent intra-
poolingappliancebasedontheXConn’sApolloCXLswitch, /inter-hostmemorystreamswithoutexplicitperformancecon-
andidentifythreeissues:intra-hostcontention,in-fabriccon- trol. We systematically characterize the problem using the
gestion,andunmanagedhost-remoteDIMMinteraction. XConn’sApolloCXLswitchandTitanevaluationplatform
Thispaperpresentsanewtransportlayer,MemChannel, andidentifythreeissues(§2.3).First,attheserverhost,taking
whichprovidesthemchannelabstractiontomanageend-to- the Intel EMR (Emerald Rapids) processoras an example,
endfabricbandwidthamongcompetingmemoryflowsand accesscontentionshappenatboth(a)theCHA(cachingand
enableapplication-specifictrafficforswitchedCXLmemory homeagent)andM2PCIemodulesofthehostuncore;and
pooling.Underthehood,ourkeyideaistobuildaSender- (b) the virtual lane inside a CXL host adapter, increasing
DrivenFabric-Informedtransportprotocol–inspiredbyCore- theCXLmemoryaccesslatencybyupto13.4×with82.6%
Stateless Fair Queueing (CSFQ)–that admits just the right bandwidthdrops.Second,withintheswitchfabric,thelink-
amountofCXLrequeststoeachmchannelbasedontheesti- layercredit-basedflowcontrolisworkload-agnostic,causing
matedCore↔DIMM bandwidthavailability.Tograpple head-of-linkblockingandunfairbandwidthpartitionatthe
CXL
withtheramificationsofCXL-inducedidiosyncrasies,Mem- egressport.Assuch,whenacacheline-sizedmemorystream
Channelintroducesacoupleoftechniques:time-basedrate interleaveswitha4KB-sizedone,itexperiences6.9×/3.8×
control,host-sideadmissioncontrol,cross-hostbookkeeping, higherread/writelatencies,with97.8%linkbandwidthbeing
new congestion signals,rate estimation based on the fluid taken(eventhoughbothhavethesameamountofoutstanding
model,anddelay-basedlinkcapacityadjustment.Webuild bytes). Third,the hardware prefetching implicitly induces
MemChannelfromscratchandsupportunmodifiedapplica- manymoreloadsintothetargetadapterunderregularaccess
tions.Ourevaluationsoverswitchedmemorypoolingdemon- patterns and predictable data locality,which is completely
strate the effectiveness ofMemChannelfrom performance transparent to the CXL fabric. We observed that while the
isolation,scalability,andmulti-tenancyperspectives. switchdownstreamportisnotcongested,thetargetadapter
seestwiceasmuchtraffic,causingdramaticqueuebuild-up.
1 Introduction
Therefore, the switched CXL memory pooling lacks a
Load-Store interconnects–such as Compute Express Link transportlayerthatcan effectively manage end-to-endfab-
(CXL)–andtheresultingmemorypoolinghavegainedsignifi- ricbandwidthamongcompetingmemoryflowsandenable
canttractionrecently.Theytransparentlyextendacommodity application-specific traffic control. However,realizing this
server’s memory capacity,enable elastic memory resource isnon-trivial. First,CXLpackets(FLITs)traversethrough
sharing, and allow applications to access remote memory theCPUpipeline,systembus,switchingfabric,andremote
usingload/storeinstructions.Suchcomposablememorytech- DIMM, whose transmissions are implicit. Specifically, a
nologyholds greatpotentialto remedythe DRAM scaling load/storeinstructionisissueddependingondatalocalityand
issue,amelioratehardwareresourceutilization,andboostthe theexecutionconditionofmicro-architecturalcomponents,
costefficiencyofrack/cluster-scalecomputing.Thelastfew anditsresponsedirectlyresumesthestalledprocessorexecu-
yearshaveseenseveralindustrialprototypes[6,11,15,16,18] tionwithoutsignaling.Second,CXLadaptersandswitches
6202
guA
22
]IN.sc[
1v13712.8062:viXra

employanultra-fastdataplanewithlimitedin-networkcom- UPs DPs
Host Servers (1…n) CXL Memory Chassis (1…n)
putingcapabilities,whosehardwarearchitectureisopaque,
Processors RP CXL Endpoint Adapter (EA)
eludinganyactivetrafficcontrolmechanisms.Third,monitor-
CXL Host CXL Memory ingthedatatransmissionperformancerequiresustobridge Adatper (HA) Controller
the gapbetween high-levelmemory streams andlow-level
hop-by-hoplink-layercredits.Theproblemisfurtherexacer-
batedbytheinherentnatureofthelosslessnetworkandthe
massiveamountofapplication-inducedmemoryrequests.
Wedesignandimplementanewtransportlayer(dubbed
MemChannel) atop today’s CXL.mem protocol stack, in-
spiredbyaseminaltechnique–Core-StatelessFairQueueing
(CSFQ) [75]. It achieves max-min bandwidth in the Inter-
netforcompetingflowswithoutmaintainingper-flowstates.
We find that CSFQ is promising to tackle the above chal-
lengesinourcontextbecause(a)itishighlyscalable,where
coreswitchesonlymaintainafewaggregatedvariables(e.g.,
arrivalrate,acceptedrate,andfairsharerate)withfixedcom-
puting complexity; (b) edge-driven, requiring minimal in-
network support; (c) lightweight on the data plane,whose
traffic manipulation primitives (e.g.,statistic bookkeeping,
labeling,andpacketdropping)arecompute-efficient.
MemChannel comprises three pieces: (a) host program-
minginterfacesthatcenteraroundthemchannelsystemob-
jectwithAPIstosupportunmodifiedapplications;(b)thehost
runtimethatrunstheprotocolstack,interactswithCXLfab-
riccomponents,andperformsratecontrol;and(c)in-fabric
system extensionsattheswitch,adapter,andCXLDIMM,
participatingintheprotocolexecution.MemChannelprobes
theend-to-endbandwidthcapabilityatruntimeonthedata
plane, introduces new fabric congestion signals, and com-
putestheper-mchanneltransmissionrate.KeytoMemChan-
nelisaSender-DrivenFabric-Informedtransportprotocol
that admits just the right amount of CXL requests to each
mchannelbasedontheestimatedCore↔DIMM band-
CXL
widthavailability.Specifically,wefirstapplythefluidmodel
to the entire CXL fabric,figure outhow to tailorCSFQ to
ourcontext,andderivethetheoreticalbound.Next,tohan-
dletheimplicittransmissionissue,MemChannelappliesthe
time-basedratecontrolthattranslatestheend-to-endband-
widthusageandavailabilitytotheavailablerunningtime.To
avoidin-networkdata-planeoperations,wepushratecalcula-
tiontotheedge,reserveadesignatedremotememoryregion
forbookkeepingcross-hoststatistics,andtranslatein-network
packetdroppingtoendhostadmissioncontrol.Wethenfollow
thefluidmodeltodeterminetheper-mchannelaccessspeed
andfairsharerateanduseadelay-basedapproachtoprobethe
linkbandwidthcapacity.Further,weextendtheMemChannel
tosupportweightandmulti-layerCXLswitching.
WeprototypedtheMemChannel,portedseveralapplica-
tions[26,27,44,49]atop,andperformedend-to-endevalu-
ationoverarealswitchedmemorypoolingsetup.Oureval-
uations show that MemChannel fully uses the underlying
link bandwidth, mitigates intra-host and cross-host perfor-
manceinterference,providesCSFQ-likefairness,adaptsto
……
LXC hctiwS
……
Local DIMMs rrDrDDIIMIMMMMMsss
(a). Memory pooling architecture
V…L .1.
vPPB VL n
(b). Evaluated hardware testbed (c). CXL switch architecture
Arbiter Crossbar Switching 1
troP
V…L .1. vPPB VL n n troP Arbiter
CXL HA CXL CXL EA
Switch
CEngine
OICM
CXL DIMMs
OICM
CXL HA
Figure1:Thearchitectureandhardwaretestbedofaswitched
CXLmemorypool.(c)showsthearchitectureofaCXLswitch.
VL=VirtualLane.vPPB=VirtualPCI-to-PCIBridge.
thefabricbandwidthavailability,andscaleswiththeapplica-
tiondemands.Applicationsrunningovermchannelsreceive
efficientmulti-tenancyandachieve2–3.5×improvements.
2 UnderstandingSwitchedCXLMEMPooling
2.1 SwitchedCXLMemoryPooling
CXL[3]isanemerginghigh-speedclusterinterconnectbuilt
atopthe physicallayerofPCIe Express [10]. Itprovides a
load/storeinterfaceforCPU,memory,anddevicecommunica-
tions.TheinterconnectusestheFlexBusI/Oarchitecture[4],
andisorganizedintophysical,datalink,andtransactionlayers.
CXLsupportsthreetypesofchannels:CXL.cache,CXL.mem,
andCXL.io.MemorypoolingisconstructedusingCXL.mem
andthecorrespondingmemoryexpanders(Type-3device).
SinceCXL2.0,CXLfabricsallowresourcepoolingviasingle-
levelandmulti-tieredswitching[4].Figure1depictsthesys-
temarchitectureofaswitchedCXLmemorypool.
• CXLHostAdapter.Itexposesaccessrootports(RPs)and
cooperateswiththehostmemorysubsystem.Theadapter
convertsload/storeinstructionsintofabric-routableFLITs
andtransmitsthemoverthewire.Uponresponses,itparses
thepackets,obtainsfetchedreaddataorwritecompletions,
anddeliversthemtotheprocessorpipeline.
• CXL Switch. A CXL switchconsists ofupstream ports
(UPs) for host adapters’ connectivity,downstream ports
(DPs)forremotememory,andinternalforwardingtables
fortraffic orchestration. Upon initialization,it discovers
allconnectedcomponents,configurestheroutingstructure,
andfillstableentriesbasedonthetopology.Theswitchcar-
riesCXLtransactionsonthedataplaneandemployssome
schedulingpolicies.CXLsupportsahybridofPort-Based
Routing(PBR)andHierarchy-BasedRouting(HBR).
• CXLEndpointAdapter.Itstaysclosetotargetmemory
devices,operatingasaresponderforremotememory.The
adapter processes CXL protocols and converts between
FLITsandmemorycommands.Italsoperformsintegrity
checking,requeststeering(whenmultiplelogicdevicesare
used),andtransmissionspeedsynchronization.

• CXLAttachedMemory.TheremoteDIMMs(rDIMMs) 1 Intra-host 2 In-fabric 3 In-rDIMM
Stream1
arehousedinastandalonechassisorappliance,including Core 1 Local DIMM
LLC Stream2 CXL Memory
anSoCbackplane,memorycontrollers,andapowersup- Core n CXL Host Adapter CXL CXL End. Adapter (rDIMM)
ply.EachmoduleusesaDDR-compatiblePHYinterface, Core 1 Local DIMM Switch
supportingdifferentkindsofmemorymedia. Core n LLC CXL Host Adapter Stream4 CXL E S n tr d ea . m A 3 dapter CX ( L rD M IM e M mo ) ry
Stream 5 (prefetch)
Evaluation Target. Several memory appliances [6,11,14,
17,18]havebeendeveloped,sampled,andtestedinthepast
fewyears.WetaketherecentTitanplatform[18]fromthe
XConnTechastheevaluationtarget(Figure1-b).Itconsists
of(1)ASIC-basedhostandendpointadapters;(2)anXConn
B2ApolloCXLswitchwith14upstream anddownstream
ports,2 CEM [1] slots,and 128 CXL2.0 lanes,supporting
×2,×4,and×8bifurcations;(3)amemorychassisusingan
MCIO/EDSFFbackplanethatholdsupto12vendor-agnostic
CXLDIMMs[8,12]underthecompactEDSFFE1.S,E3.S,
andE3.Lformfactors[7];and(4)anMX8boardoperating
asthemanagementhostandfabricmanager.
SoftwareStack.AswitchedCXLmemorypoolingplatform
hasthreesoftwarecomponents:(1)afabricmanagerrunning
on a dedicated host,which interacts with each fabric hard-
ware,discoversthesystemtopology,enumerateshostsand
targetmemorynodes,andmonitorstheirlivingstatus;(2)the
memorycontrollerfirmwarefortheremoteDIMMs,which
configuresthecommunicationID,initializesitsaddressspace,
andprocessestraverseddata;(3)adevicedriverthatmakes
remotememoryashost-manageddevicememory(HDM)and
exposesitasaCPUlessNUMAnode.ThehostOSfabricates
anattachedCXLDIMMasamemorynode,managesitwith
objectortieredmemorysystems[34,46,52,61,74,78,82,87],
andrunsapplicationsatop.AfteraCXLDIMMismapped
to the host memory subsystem, applications can access it
via load/store instructions. Take the Intelx86 processoras
an example. A memory read, missed from the last-level
cache (LLC), fetches the corresponding cache line from
the CXL memory. Memory writes hitthe store bufferfirst,
thenareissuedtotheremotememoryundereviction.Hard-
ware/Softwareprefetchandcachecoherence-inducedevents
(likeread-for-ownership)alsocausedataloads[47,50].
2.2 CXLSwitchingArchitecture
ACXLswitchprovideshigh-performanceandlosslesscon-
nectivitybetweenupstreamanddownstreamports(Figure1-
c).DataistransmittedattheFLITgranularity,afixed-sized
amountofdatatraversedovertheunderlyinglink,suchas68B
and256B.AnincomingFLITarrivesatonevirtuallane(VL)
andisthenforwardedtoanarbiter(multiplexer).Next,the
FLITisdeliveredtoavPPB(virtualPCI-to-PCIbridge)mod-
ule,actingasalogicalconnectionpointtoaccommodatedif-
ferenttypesofCXLdevicesandfacilitatetherouting.vPPBs
can also be organized hierarchically to construct multiple
VCS(virtualCXLSwitch)withinaphysicalswitch.Thereis
acreditengine(CEngine)interactingwithallvPPBsandrun-
ning(1)ahop-by-hopcredit-basedflowcontrol[42,43];(2)
acreditupdateprotocol(likeN23)forreliabledevice-switch
1
tsoH
2
tsoH
Figure2:DifferentaccesscontentionpointsalongtheCXLdata
pathunderswitchedCXLmemorypooling.
andswitch-switchcoordination[42];and(3)anadaptiveand
statisticalcreditallocationschemetomaximizebandwidth
usage[43].Last,mostoftoday’sCXLswitches(likeXConn
ApolloXC50256[18]andOmegaFabric[6])employacross-
bartopology,where the routing logic is determinedby the
fabricmanagerduringthememorypoolinitialization.Note
that(1)theCXLswitchisnearlybufferlessbutstillincurs
transmissionstallwhencreditstarvationhappens;(2)thereis
littleprogrammabilityontheswitchdata-plane,unlikeEth-
ernetonesofferingsomein-networkprimitivesinthetraffic
manager;(3)hostandendpointadaptersusuallyadoptasimi-
larswitchingarchitecture,justwithmuchfewerports.
2.3 CharacterizingSwitchedCXLMemoryPooling
Researchershavestudiedextensivelyaboutadirect-attached
CXL Type-3 memory expander [34,45,47,50,55,71,76].
ThissectioncharacterizestheperformanceofswitchedCXL
memorypoolingwithafocusonanalyzingtheperformance
interference.Figure2presentshowintra-andinter-hostmem-
oryrequestswouldinterleaveatdifferentlocationsalongthe
CXL data path in a switched memory pool. We configure
experiments to locate the contention points, quantify how
performanceisolationisaffected,andexploretherootcauses.
Experimental Methodology. We use 2U Intel Emerald
Rapidsserversashosts,whereeachcontainstwoXeonGold
6530 CPUs, 1536GB DDR5 memory, and two Samsung
9MA3 960GB NVMe drives. Eachprocessorhas 32 cores
runningat2.1GHzand160MBLLC.AllthehostsrunUbuntu
24.04. EachserverisequippedwithoneCXLhostadapter
enclosingtwo×8CXLports.UsingIntelMLC[5],weob-
serve that the serverachieves 220.5ns and 47.2GB/s when
accessing the switched CXL memory pool. We developed
a micro-benchmark (similar to [9,51,76]) that can launch
anynumberofmemorystreamsbetweenhostcoresandlo-
cal/CXLDIMMswithdifferentaccesspatterns.Itsupports
variousconfigurations,suchasenabling/disablingprefetching,
issuingtemporalread/writeandnon-temporalwrite,injecting
NOPinstructions,andperformingrandom/sequential/strided
accesses.Thebenchmarkusesdataandinstructionsynchro-
nization barriers to complete pending reads and writes in
theCPUpipelinebeforestartingthetest.Whenrunning,it
spawnsseveralpinnedthreads,initiatesmemorystreams,is-
suesreads/writes,andcollectsexecutionstatistics.
Issue#1:Intra-hostContention.HostuncoreandCXLhost
adapterarethefirsttwocontendinglocations.InanIntelX86
processor,the uncore–enclosing LLC,CHA (Caching and

|                         |     |     |  1800     |            |  25 |           |     |
| ----------------------- | --- | --- | --------- | ---------- | --- | --------- | --- |
|  700 Local-Affect-Local |     |     | Read-Read | Read-Write |     | Read-Read |     |
C X L - A ff e c t- L oc a l  1600 Write-Read Write-Write )s/BG( htdiwdnaB Write-Read
|  600 Lo           | c a l -A f fe c t -C X L |     | )sn( ycnetaL  1400 |     |  20 |             |     |
| ----------------- | ------------------------ | --- | ------------------ | --- | --- | ----------- | --- |
| )sn( ycnetaL  500 | CXL-Affect-CXL           |     |  1200              |     |     | Read-Write  |     |
|  400              |                          |     |  1000              |     |  15 | Write-Write |     |
 800
|  300 |     |     |  600 |     |  10 |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
 200
|      |     |     |  400 |     |  5  |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
|  100 |     |     |  200 |     |     |     |     |
|  0   |     |     |  0   |     |  0  |     |     |
 0  20  40  60  80  100  0  20  40  60  80  100  0  20  40  60  80  100
Contending Traffic Load (%) Contending Traffic Load (%) Contending Traffic Load (%)
(a)Uncorecontention. (b)Hostadaptercontention(latency). (c)Hostadaptercontention(bandwidth).
Figure3:(a)runsbackgroundthreadsononesocket,issuessequentialaccesses,andmaxesoutitsmemorybandwidth.Wereport
randomaccesslatency.The“Local-Affect-Local”and“CXL-Affect-Local”casesareaddedforcomparisons.(b)/(c)presentthehost
contentionissue.X–Yshowsthatthevictimstream(X)isimpactedbyco-locatedstreams(Y).Allexperimentsuseone×8CXLport.
|  2500 |     |     |  2500 |     |     |     |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- |
Read-Read Write-Read Local-CXL-rnd local-CXL-seq  25 Memory Stream1 Memory Stream2
|  2000 Read-Write |           | Write-Write |  2000 CXL1-CXL2-rnd | CXL1-CXL2-seq       | )s/BG( htdiwdnaB |     |     |
| ---------------- | --------- | ----------- | ------------------- | ------------------- | ---------------- | --- | --- |
| )sn( ycnetaL     | 20.7 GB/s |             | )sn( ycnetaL        |                     |  20              |     |     |
|  1500            |           |             |  1500               |                     |                  |     |     |
|                  |           | 22.1 GB/s   |                     | 20.4 GB/s 20.7 GB/s |  15              |     |     |
|  1000            |           |             |  1000               |                     |                  |     |     |
|                  | 20.6 GB/s | 22.0 GB/s   |                     |                     |  10              |     |     |
|  500             |           |             |  500                |                     |                  |     |     |
 5
|  0  |     |     |  0  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
64B 128B 256B 512B 1KB 2KB 4KB 8KB 16KB 64B 128B 256B 512B 1KB 2KB 4KB 8KB 16KB  0 R(4K)-R( R (4 R (4 R ( R ( W W
Data Block Size of the Throughput Stream Data Block Size of the Throughput Stream 4K K)-R( 64 K)-W( 4 K 4 K)-W( 6 4 6 4)-W( 4K (4 K)-W (4 ( K 4 K)-W(64)
|     |     |     |     |     |     | ) ) ) ) ) ) |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- |
(a)Host-rDIMMinterference. (b)rDIMM-rDIMMinterference. (c)Bandwidthpartition.
Figure4:In(a),X–YdescribesthecasethatalatencystreamXisco-locatedwiththroughputstreams(Y),wherewereporttheaverage
latencyofX.(b)presentsthelatencyresultsoffourdatamovements.Weaddthelocal-rDIMMscenarioforcomparison.rnd=Random.
seq=Sequential.In(c),weruntwothroughputstreamseachoverfourcores,issuing64B/4KBread/writerequests.
HomeAgent),andFlexBus,connectedviaameshNoC[66]– Issue#2:In-fabricCongestion.TheCXLswitchisthesec-
issharedbylocalandCXLmemoryrequests,e.g.,stream1 ond interference point (stream3 and stream4 in Figure 2).
andstream2inFigure2.Weconfiguretwokindsofthreads: SincetheCXLswitchingreliesonahop-by-hopcredit-based
T1,whoseworkingsetfitsintotheLLC,accessinglocalor flowcontrol[38,42,43],theamountofcreditsthatadown-
CXL memory and measuring latency; and T2, which gen- streamentityreceivesisproportionaltoitsbandwidthusage
erates competing traffic with gradually increased loads by and the contention degree at the upstream device. Hence,
addingthenumberofthreadswithoutoverwhelmingthehost whenasmall-sizedrequeststreamcompeteswithalargeone
adapter’sbandwidthcapacity.AsshowninFigure3-a,when thatcausescreditover-subscription,itwouldexperiencestalls
the FlexBus is congested,accessing the CXL memory ex- due to delayed credit replenishment. To quantify this, we
periencesupto13.4×latencyincreases,risingfrom50.1ns configuretwokindsofrandomaccessmemorystreams:the
to 669.4ns. Using the recent PathFinder tool [47],we find latencystreamthatissuesonememoryread/writeatatime,
outthatthisisbecausesignificantqueueinghappensatthe andthethroughputone,whichgenerateslargerdatablocks,
M2PCIeingress,whichslowsdownCXLrequesttransmis- yieldingmultipleoutstandingmemorytransactions.
sion.WhencontentionsoccurattheLLC/CHAundermixed We intermix small and large memory requests and de-
local and CXL traffic,we observe that both the LLC miss ploymemorystreamsintwodirections:host→rDIMMand
rateandthetotalamountofcachesnoopingrequestsgreatly rDIMM→rDIMM. Regarding the host→rDIMM case, as
increase,yieldingatmost2.9×CXLaccesslatencyincreases.
|     |     |     |     | shown in Figure | 4-a, when | the fabric is under-utilized, | a   |
| --- | --- | --- | --- | --------------- | --------- | ----------------------------- | --- |
Next,we analyze the hostadaptercontention by issuing 64Breadmixedwith128Breadsandwritescausesa7.5%
|     |     |     |     | and 54.2% latency | increase, | respectively. In the case | of a |
| --- | --- | --- | --- | ----------------- | --------- | ------------------------- | ---- |
cache-bypassedCXLrequests(stream2andstream3inFig-
ure 2). We set up two memory streams: T1 accesses CXL 64B write contending with throughput streams, when the
memorywithoneoutstandingload/store(i.e.,victimmemory datablocksizeis256B,itslatencyisincreasedby6.2%and
stream);T2reads/writestoremotememory,withthenumber 98.6%.Thisisduetothehead-of-line(HoL)blockingeffect
ofoutstandingaccessesgraduallyincreased.AsshowninFig- attheupstreamport.Whenbandwidthover-subscriptionhap-
pens,onewouldexperienceconsiderableperformancedrops.
ures3-b/c,T1startstoexperienceaperformancedropeven
whenthetotaltrafficonlyreaches30%,farbelowtheadapter’s Forexample,wheninterleavedwitha4KBmemoryrequest,
bandwidthcapacity. By discussing withthe device vendor, a 64B read/write experiences a 6.9×/3.8× slowdown. The
rDIMM→rDIMMscenariopresentssimilarbehaviors(Fig-
welearnthatthisisbecausethehostadapterschedulesCXL
FLITs over several VLs of the virtual lane in a best-effort ure4-b),wherethe64BCXLmemoryaccesslatencystarts
fashion,completelyagnosticofhowrequestsareissuedfrom torisewhenthedatablocksizeisabove256B.
hostcores,whichcausesskewedcross-laneFLITdistribution. Next,wedeploytwocompetingthroughputstreams,vary
Whentheadapterisnearlysaturated,weobservethatinthe theirrequestconfigurations,andexplorehowbandwidthis
Read(T1)-Read(T2)case,thevictimstream’sbandwidthis allocatedindifferentcases.AsshowninFigure4-c,wefind
reducedby82.6%,withlatenciesincreasedfrom230.2nsto thatthebandwidthamemorystreamreceivesismainlypro-
1624.2ns.Theotherthreecasesaresimilar. portionaltoitsdatablocksize,regardlessofrequesttype.For

| StrideLen. | RDLat. |     | RDTh. | WRLat. |     | WRTh. |  40        |     |  50        |             |
| ---------- | ------ | --- | ----- | ------ | --- | ----- | ---------- | --- | ---------- | ----------- |
|            |        |     |       |        |     |       | Local-Read |     | Local-Read | Remote-Read |
1 1 0 . 9 n s 2 1 . 9 G B / s 1 0 . 8 n s 2 2 . 0 G B / s   3 5 L o c a l - W r i t e Local-Write Remote-Write
|     |     |         |             |     |             |                 |   3 0 R R e e m m o o t t e e - - R W e r | a i t d e | )s/BG( htdiwdnaB  40 |     |
| --- | --- | ------- | ----------- | --- | ----------- | --------------- | ----------------------------------------- | --------- | -------------------- | --- |
| 2   | 1 5 | . 6 n s | 1 5 . 3 G B | / s | 1 3 . 2 n s | 1 8 . 0 G B / s | )sn( ycnetaL   2 5                        |           |                      |     |
 30
| 4   | 18.7ns |     | 12.7GB/s |     | 13.3ns | 17.9GB/s |  20 |     |     |     |
| --- | ------ | --- | -------- | --- | ------ | -------- | --- | --- | --- | --- |
| 6   | 18.2ns |     | 13.1GB/s |     | 12.3ns | 19.4GB/s |  15 |     |  20 |     |
 10
| 8   | 18.6ns |     | 12.8GB/s |     | 12.4ns | 19.2GB/s |     |     |  10 |     |
| --- | ------ | --- | -------- | --- | ------ | -------- | --- | --- | --- | --- |
 5
| Table1:CXLmemoryperformanceunderafixedstridesizeX. |     |     |     |     |     |     |  0  |          |  0      |              |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------------ |
|                                                    |     |     |     |     |     |     | 0 8 | 16 32 64 | 128 0 8 | 16 32 64 128 |
ThedistancebetweentwoconsecutiverequestsisX×64bytes. NOP Instructions (#) NOP Instructions (#)
|     |     |     |     |     |     |     | (a)Latency. |     | (b)Bandwidth. |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- |
example,whentwo4KBread(write)streamsinterleave,each
Figure5:Performancewhenperturbinginstructionprefetching.
| wouldachieve10.6(11.0)GB/s. |     |     |     | However,ifa4KBstream |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
thedatapathbetweenahostcoreandaremoteCXLDIMM
| is interleaved | with | a 64B | one,it | can take | nearly | 97.8% of |     |     |     |     |
| -------------- | ---- | ----- | ------ | -------- | ------ | -------- | --- | --- | --- | --- |
issharedamongconcurrentmemoryrequestswithoutexplicit
| the total | bandwidth. | These | results | make | sense | fortwo rea- |     |     |     |     |
| --------- | ---------- | ----- | ------- | ---- | ----- | ----------- | --- | --- | --- | --- |
performancecontrol.Assuch,anyon-pathentities,likethe
sons. First,memoryrequestsfromonememorystreamare
hostmemorysubsystem,switch,andhost/endpointadapter,
synchronouslyservedonebyone.Thenumberofoutstanding
|     |     |     |     |     |     |     | couldbecomeacommunication |     | chokepoint,whichwould |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --------------------- | --- |
cacheline-sizedreads/writesdependsonthedatablocksize.
breakthetargetlatencyandbandwidthofamemorystream.
Second,whenmultipleconcurrentstreamscompeteforthe
Thiscallsforanewtransportlayerforswitchedmemorypool-
fabric,theCXLswitch/adaptermainlyperformsround-robin
ingthateffectivelyallocatescommunicationresourcesbased
schedulingtodecidethenextissuingrequest.Thus,thestream
|     |     |     |     |     |     |     | on the application | requirements. | Realizing | this incurs the |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ------------- | --------- | --------------- |
withmorependingtransactionshasmoreopportunitiestobe
followingthreechallengesthathavenotbeentackledbefore.
scheduled,yieldinghigherbandwidth.
Issue#3:UnmanagedHost-rDIMMInteraction.Theend- • #1:Implicittransmission.Underswitchedmemorypool-
pointadapterprovisionsenoughbandwidthforCXLDIMMs.
ing,aCXLrequesttraversesacrosstheCPUpipeline,cache
Sinceitconnectsdirectlytotheswitch,accesscongestionis hierarchy,systembus,adapters,switchingfabric,andre-
firstresolvedatthedownstreamport,whichshouldleavethe moteDIMM.WhetherandwhentoissueaCXLload/store
adapterandrDIMMfreefromcontendingtraffic.However,
transactionisaffectedbyseveralfactors,suchasdatalocal-
wefindoutthisissometimesnotthecase.Eventhoughwe ity(L1D,L2,andLLC),queueingoccupancyatdifferent
controltheaggregatedtrafficacrossallhoststobelowerthan
micro-architecturalcomponents(suchasstorebufferand
thelink/portbandwidth,contentionstillhappens.Thisisbe- linefillbuffer),andhardwareprefetching.Similarly,adata
causehostprefetching,underregularaccesspatterns,implic- response returns to the host memory subsystem and di-
itlygeneratesmorememoryrequests,whicharetransparent
rectlyresumestheprocessorexecution.Therefore,tracking
totheCXLfabricbutcausebandwidthover-subscription. CXLrequests,measuringtheper-flowperformance,and
Weconfigureourmicrobenchmarktoissuestridedmemory
controllingthetransmissionratebecomenon-trivial.
readsandwrites.Table1presentsthelatencyandthroughput
• #2:Hardwarenon-programmabilityandopaqueness.
| as the stride | lengthincreases |     | from | 1 to | 8. When | the stride |            |                    |         |                 |
| ------------- | --------------- | --- | ---- | ---- | ------- | ---------- | ---------- | ------------------ | ------- | --------------- |
|               |                 |     |      |      |         |            | To sustain | at sub-microsecond | latency | and hundreds of |
lengthis1,comparedwiththerandomaccess,remotememory
Gigabytespersecondofbandwidth(CXL3.2[4]),CXL
readandwriteachieve10.9nsand10.8ns(hittingintheL1and
adaptersandswitchesstreamlinetheirdataplaneandoffer
L2cache),sustainingat21.9GB/sand22.0GB/sbandwidth.
nearlynoreconfigurabilityandtelemetrycapability,mak-
Apparently,theaccesslocalityresultsinmultiplecacheline
ingourconventionalin-networktransportdesign[21,22,39,
readsandwritesissuingconcurrentlytohidelatency.When
48,92]impractical.Further,thereisnoconsensussystem
thestridelengthincreasesto8,thereadandwritebandwidth
modeloropenimplementationstandard(likePISA[29]).
| dropsto12.8GB/sand19.2GB/s. |     |     |     | Further,weperturbthe |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
• #3:Fine-grainedcross-layertrafficmonitoring.Measur-
CPUprefetchingeffectbyissuingNOPinstructionsbetween
ingend-to-endbandwidthavailabilityisalreadychalleng-
| two consecutive |     | memory | accesses | and | measure | its perfor- |     |     |     |     |
| --------------- | --- | ------ | -------- | --- | ------- | ----------- | --- | --- | --- | --- |
ingenoughsincethisrequirestrackinghowmanylink-layer
| mance impact. | We  | find | that both | local | and | CXL memory |     |     |     |     |
| ------------- | --- | ---- | --------- | ----- | --- | ---------- | --- | --- | --- | --- |
creditsareallocatedacrosstheentiredatapath.However,
performancedropssignificantlywheninsertingmoreNOP
inaswitchedpool,thetransportlayerhastofurtherbreak
| instructions | (Figure | 5). When | prefetching |     | helps | little,a re- |     |     |     |     |
| ------------ | ------- | -------- | ----------- | --- | ----- | ------------ | --- | --- | --- | --- |
downthisinformationatafinergranularitytoindividual
| motememoryread/writematchesthelocalone. |     |     |     |     |     | Therefore, |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
hostprefetchingcausesunmanagedhost-rDIMMinteraction, hostcores/threads.Asdescribedabove,theround-tripde-
layisimpracticaltoobtain,giventheintegratedpipeline.
whichwouldintroducemuchmoretrafficthanexpectedand
Theinherentnatureoflosslessfabric(back-pressureand
causecontentionwithinthetargetmemorypool.
creditstarvation)furtherexacerbatestheissue.
2.4 ProblemandChallenges
Ourcharacterizationstudyunearthsandquantifiesthreeis- 3 MemChannel:aDesignatedMemoryLane
sues(i.e.,intra-hostcontention,in-fabriccongestion,andhost-
rDIMMinteraction)thatcauseperformanceinterferenceina ThissectionintroducestheMemChanneltransport,including
switchedCXLmemorypool.Thefundamentalproblemisthat semantics,APIs,andsystemmodel.Oursystemdesigngoals:

• HighUtilization.MemChannelshouldfullyusetheband-
| widthatanyvantage |     |     | pointandlink. |     | Itshouldbe | ableto |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ------------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
rampuptheCXLmemoryaccessspeedforotherneeded
applicationswhensomebandwidthbecomesavailable.
| • Efficient | Multi-tenancy. |     | MemChannel |     | should | mitigate |     |     |     |     |     |     |     |
| ----------- | -------------- | --- | ---------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
theperformanceinterferenceacrosstheend-to-endCXL
| datapath(§2.3). |     |     | Itshouldachievelow(tail)latencyand |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
approximateMax-Minfairnessundercontention.
• Lowoverheads.MemChannelshouldhavelittleimpact
onthedefactoCXLloadandstoreaccess.Itshouldincur
Figure6:ThesystemmodelofMemChannel.
fewmemoryfootprintsandconsumetolerablehostCPU
cycleswhenholdingexistingapplications. • PerformanceAttributes,likebandwidthenvelopeandinter-
ferencedegree.Developersspecifythemuponregistration
oratruntime.Whenomitted,themchannelislabeledas
3.1 Overview
best-effortanduseswhatbandwidthisavailable.
| MemChannel |     | is a transport | layer | that | orchestrates | remote |     |     |     |     |     |     |     |
| ---------- | --- | -------------- | ----- | ---- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
memory accesses between host cores and CXL DIMMs 3.3 ThemchannelInterface
| in a switched |     | CXL | memory pool. | It offers | a   | performance- |            |          |     |              |     |               |     |
| ------------- | --- | --- | ------------ | --------- | --- | ------------ | ---------- | -------- | --- | ------------ | --- | ------------- | --- |
|               |     |     |              |           |     |              | MemChannel | provides |     | a user-space | CLI | (Command-Line |     |
controlleddatapipe(mchannel),provisionspropercommu-
Interface),similartonumactl,whichonboardstheunmod-
nicationresourcesbasedonworkloaddemandsandremote
ifiedapplicationsandcontrolstheirexecutionbehaviorsto
DIMM’sfreebandwidth,andmitigatesinterferencefromcon-
achievetheperformancetarget.MemChannelruntimeoffers
tendingmemorystreams.Amchannel,establishedbetween
fourlightweightAPIstocontroltheremotememoryaccess:
| ahostcore(C)andaCXLDIMM(rDIMM |           |             |          |     | ),isassociated |            |                 |                 |         |           |          |              |       |
| ----------------------------- | --------- | ----------- | -------- | --- | -------------- | ---------- | --------------- | --------------- | ------- | --------- | -------- | ------------ | ----- |
|                               |           | i           |          |     | j              |            |                 |                 |         |           |          |              |       |
|                               |           |             |          |     |                |            | • mchannel_init |                 | creates | mchannels |          | and takes    | user- |
| with a                        | dedicated | application | process. |     | One can        | also group |                 |                 |         |           |          |              |       |
|                               |           |             |          |     |                |            | specified       | configurations, |         | such      | as which | applications | to    |
multiplemchannelsforeachapplication(discussedin§4.4).
run,hostcoremappings,remotememorynodes,andper-
KeytoMemChannelisaSender-DrivenFabric-Informed
|     |     |     |     |     |     |     | formanceattributes. |     |     | ItthenidentifiestheCXLdatapath |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------------------------ | --- | --- | --- |
transportprotocolthatadmitsjustenoughCXLrequeststothe
foreachmchannel,allocateslocalmemoryformchannel
| switchedmemorypoolbasedontheestimatedC |     |     |     |     |     | ↔rDIMM |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|                                        |     |     |     |     |     | i j    |     |     |     |     |     |     |     |
metadata,mapssharedCXLmemoryforinter-hostcoordi-
bandwidthavailability.Essentially,itprobestheend-to-end
nation,andlaunchestheapplicationsassubprocesses.
bandwidthcapabilityatruntimeonthedataplane,introduces
|     |     |     |     |     |     |     | • mchannel_open |     | opens | a mchannel |     | to a rDIMM | in the |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | ---------- | --- | ---------- | ------ |
newfabriccongestionsignals,computestheper-mchannel
transmission rate and admits an adequate amount of CXL pool,invokedwhenanewapplicationthreadislaunched.
load/storecommandstothememorypool.MemChannelen- Itallocatestheper-threadmchannelstatesandresources,
andthenarmsaPOSIXtimerwithaschedulingwindow
compassesthreemajorpieces.Oneistheprogramminginter-
facethatallowsportingunmodifiedapplications.Thesecond T W .Whenthetimerexpires,itinvokesmchannel_sched
asthesignalhandlerandreadjuststhebandwidthallocation.
isthehostruntimethatrunstheprotocolstack,interactswith
Italsousesthem_bindsystemcalltoensuretheapplica-
otherCXLfabriccomponents,andperformsratecontrol.The
thirdisin-fabricsystemextensionsattheswitch,adapter,and tionplacesitsdataontheremoteDIMMspecifiedbythe
mchannel,setsthethread’scoreaffinitybasedonthehost
CXLDIMM,whichparticipateintheprotocolprocessing.
coremappings,andopensaswellasmapstheperformance
| 3.2 ThemchannelSemantics |     |     |     |     |     |     | countersforCXLbandwidthmonitoring. |     |        |     |          |        |        |
| ------------------------ | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | ------ | --- | -------- | ------ | ------ |
|                          |     |     |     |     |     |     | • mchannel_close                   |     | closes | the | mchannel | to the | remote |
MemChannelexposesthemchannelasasystemobjectfrom
thehostOSperspective,consistingofthefollowingattributes: DIMM,cleansupallocatedresources,andunsetsthetimer
signalhandler.Itiscalledwhentheapplicationthreadexits.
• Host/CoreIDandRegisteredMemoryNode,specifyingthe
• mchannel_schedenforcesapplication-specificbandwidth
requester(source)andresponder(destination)ofaMem-
allocationviaourtransportprotocol(§4),whichmonitors
Channel.Akintocommoditysystems[6,11,17],wesupport
|     |     |     |     |     |     |     | the remote | pool | access | bandwidth | and | then controls | ap- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------ | --------- | --- | ------------- | --- |
DAXmemory,mountedasaCPUlessNUMAnode.
|     |     |     |     |     |     |     | plication | execution | to  | meet the | application | performance |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------- | ----------- | ----------- | --- |
• CXL Data Path,describing the end-to-end data path be- needs. For bandwidth measurement,we use off-core re-
| tweenC | and | rDIMM | ,provided | by  | the fabric | manager, |                                                   |     |     |     |     |     |     |
| ------ | --- | ----- | --------- | --- | ---------- | -------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|        | i   |       | j         |     |            |          | sponse(OCR)architecturaleventcounterstotrackthree |     |     |     |     |     |     |
includinghostadapter,switches,andendpointadapter. typesofCXLrequests[47,50]: demandreads,readsfor
• ChannelRepresentation,like struct sock,instantiated ownership,andhardwareprefetches.Theresultsarecol-
byourhostruntime,servingasanintermediateconnection lectedviardpmccommandsandaggregatedastheremote
pointbetweenapplicationsandthetransportprotocol. bandwidth.Forbandwidthcontrol,duringaschedulingwin-

dowT ,weadjustthePOSIXtimerexpirationsuchthat However, naively applying CSFQ and its successor
W
theapplicationthreadrunsforT andsleepsforT −T . HCSFQ[84]isstillnotfeasibleforthreereasons.First,these
|     |     |     | R   |     | W R |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MemChannelreliesoncodeinjectiontechniques[2],such approachestakepacketdropsasacongestionsignal,butCXL
|     |     |     |     |     |     | fabric | is a | lossless | network. | Second,core |     | switches |     | require |
| --- | --- | --- | --- | --- | --- | ------ | ---- | -------- | -------- | ----------- | --- | -------- | --- | ------- |
asLD_PRELOADandptrace,tosupportunmodifiedapplica-
thepacket-droppingprimitivefortrafficregulation,whichis
tions.Specifically,MemChannelinjectsadynamiclinklibrary
|     |     |     |     |     |     | not | supported | on  | CXL | switches. | Third,CSFQ |     | needs | accu- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --------- | ---------- | --- | ----- | ----- |
(DLL)intoapplicationswhenlaunchingthem.InsidetheDLL
rateflowrateandlinkbandwidthavailabilityestimations,but
constructorandpthread_createinterposedbyDLL,Mem-
Channelcallsmchannel_open.Themchannelinterfacesin- CXL switching lacks such capabilities. Therefore,akin to
CSFQandHCSFQ,wefirstapplythefluidmodeltotheCXL
curlowoverheads,becausemchannel_schedisinvokedonly
switching,derivethetheoreticalguaranteeswhenachieving
| once perscheduling | window | T   | and halts | application | exe- |     |     |     |     |     |     |     |     |     |
| ------------------ | ------ | --- | --------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
W
cutiononlyonceduringthatwindow.Inaddition,weutilize themax-minfairness(§4.2),andredesignthetransportalgo-
rithm(§4.3).Tohandletheimplicittransmissionissue,Mem-
locklessdatastructurestosynchronizebetweenmchannels
andtherdpmccommandtoreadperformancecountersinside Channel applies the time-based rate control that translates
theend-to-endbandwidthusageandavailabilitytotheavail-
mchannel_schedinsteadofsystemcalls.
ablerunningtime.Toavoidin-networkdata-planeoperations,
3.4 SystemModel
|     |     |     |     |     |     | we  | push rate | calculation |     | to the | edge,reserve |     | a designated |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------ | ------------ | --- | ------------ | --- |
remotememoryregionforbookkeepingcross-hoststatistics,
Wedivideourrunningenvironmentintosixlayers(Figure6):
andtranslatein-networkpacketdroppingtoendhostadmis-
applications,mchannels,hostadapters,CXLswitches,end-
|                    |     |        |               |     |       | sion | control. | We  | then follow |     | the fluid | model | to determine |     |
| ------------------ | --- | ------ | ------------- | --- | ----- | ---- | -------- | --- | ----------- | --- | --------- | ----- | ------------ | --- |
| point adapters,and | CXL | DIMMs. | OurMemChannel |     | layer |      |          |     |             |     |           |       |              |     |
theper-mchannelaccessspeedandfairsharerateandusea
| carries application-induced |     | CXL | memory | requests | and de- |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
liversthemtothehostadapter.TheCXLFLITtraversesthe delay-basedapproachtoprobethelinkbandwidthcapacity.
underlyingfabricasitis.FollowingtherecentCXLspecifi- 4.2 ApplyingFluidModeltoCXLSwitching
cation[4],thememorydevicecontinuouslyreportsservice
loads,reflectingitsinternalqueueingstatus.Therearetwo WeapplythefluidmodeltoformalizeswitchedCXLmemory
poolingsystems.Thesystemisviewedasadirectedacyclic
| ways: (a) piggyback | in  | memory | responses | (red | line in Fig- |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------ | --------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ure 6),where the memory transaction response reserves 2 graphG(V,E),whereV representssystemcomponents(e.g.,
|     |     |     |     |     |     | theonesinFigure6),andE |     |     |     | representsthetrafficflowsbe- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
bitstoindicatefourlevelsofloads:lightload,optimalload,
tweencomponents.Weassumetheflowsarecontinuousmem-
moderateoverload,andserveroverload;(b)QoStelemetry
messages(bluelineinFigure6),i.e.,thehostissuesexplicit orystreamsfromahostcoretoaremoteCXLDIMM.We
considerasinglelayerofswitchinginthefollowingdiscus-
QoSstatusqueriesthroughtheCXLComponentCommand
Interface(CCI),whereasthememoryexpander(rDIMM)re- sion,butouranalysisappliestomultiplelayers.Aflowstarts
fromamemorychannel,goesthroughabridgeandaswitch,
turnstheaverageloadofthelastprofilingepoch.
|     |     |     |     |     |     | and | reaches | the CXL | DIMM. |     | Therefore,graph |     | G(V,E) | is  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----- | --- | --------------- | --- | ------ | --- |
4 AnCSFQ-InspiredTransport
acompletemultipartitegraph,wherethevertexsetisparti-
|                                                      |     |     |     |     |     | tionedintofourdisjointsubsets{V |     |     |     |     | ,V  | ,V ,V | }forchannels, |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ----- | ------------- | --- |
| Thissectiondescribesourcoretransportprotocolandshows |     |     |     |     |     |                                 |     |     |     |     | C   | H S E |               |     |
howweaddresstheabovechallenges(§2.4). hostadapters,switches,andendpointadapters,respectively.
EachCXLhardwarecomponenthasamaximumlinktrans-
4.1 WhyCore-StatelessFairQueueing mission capacityC . Let α be the fairshare rate a node v
|     |     |     |     |     |     |     |     |     | v   | v   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allocatedtoitssuccessors.Weknowtheapplicationaccessde-
Core-StatelessFairQueueing(CSFQ)[75],aseminalwork
|                                                     |     |     |     |     |     | mandD | forchannelv |     |     | ∈V viaourmechanism(§4.3).For |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --- | ---------------------------- | --- | --- | --- | --- |
| incomputernetworks,introducedafairqueueingalgorithm |     |     |     |     |     |       | c           |     | c   | C                            |     |     |     |     |
for the Internet several decades ago. It achieves max-min theedgebetweenachannelandahostadapter,theaggregated
|     |     |     |     |     |     | demandisthechannel’sdemand,e.g.,D |     |     |     |     |     | =D  | ;v ∈V | .The |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | ----- | ---- |
fair bandwidth allocation among competing flows without ch c h H
demandforotheredgescanbecalculatedrecursively.
maintainingper-flowstates.Thealgorithmdividestherate
controllogicbetweenthenetworkingedgeandcore,where D = ∑ min(α ,D ) (1)
|                     |     |              |      |           |           |     |     | vw  |     |     |     | v uv |     |     |
| ------------------- | --- | ------------ | ---- | --------- | --------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
| (1) edges calculate | the | flow arrival | rate | and label | the rates |     |     |     |     |     |     |      |     |     |
euv∈p;∀p∈Pvw
intopackets;(2)thecoreestimatesthefairrateiterativelyand
|     |     |     |     |     |     | p=(e | ,e  | ,e );e | ,e  | ,e ∈Edescribesaflowpath.P |     |     |     | =   |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------ | --- | ------------------------- | --- | --- | --- | --- |
probabilisticallydropspacketstoachievethefairsharerate. ch hs se ch hs se vw
{p|e ∈ p}isalltheflowsgoingthroughedgee
CSFQis(a)scalable,wherecoreroutersonlymaintainafew vw vw .There-
aggregatedvariables(e.g.,arrivalrate,acceptedrate,andfair fore,undercontention,wheretheaggregatedmemorydemand
|     |     |     |     |     |     | D   | = ∑ | D   | >C , | one can | achieve | the | max-min | fair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ------- | --- | ------- | ---- |
sharerate)withfixedcomputingcomplexity;(b)edge-driven, v euv∈E uv v
requiringminimalin-networksupport;(c)lightweightonthe bandwidth allocation among competing flows when α v is
theuniquesolutiontothefollowingequation.
dataplane,thetrafficmanipulationprimitives(e.g.,statistic
| bookkeeping,labeling,and                        |     | packet | dropping) |     | are compute- |     |     |     |     |         |     |     |     |     |
| ----------------------------------------------- | --- | ------ | --------- | --- | ------------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
|                                                 |     |        |           |     |              |     |     |     | C = | ∑ min(α | ,D  | )   |     | (2) |
| efficient,makingitpromisingtoaddressourproblem. |     |        |           |     |              |     |     |     | v   |         | v   | uv  |     |     |
euv∈E

Algorithm1TransportAlgorithm. oversubscribed.FollowingthedefinitionofCSFQ,wethen
estimatethememoryaccessrateasthefollowingequation,
1: procedureMCHANNEL_SCHED(mchannelc)
2: n=read_perf_counters() ▷CXLmemoryaccesscount whereK isaconstantforadjustingthesamplingwindow.
| 3:  | c.demand=estimate_rate(c.demand,n,c.TW); |     |     |     |     | ▷Eq.3 |     |                              |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | ----- | --- | ---------------------------- | --- | --- | --- | --- | --- |
|     |                                          |     |     |     |     |       |     | rnew=(1−e−TW/K)r′+e−TW/Krold |     |     |     |     | (3) |
|     | c.rate=estimate_rate(c.rate,n,c.TR);     |     |     |     |     | ▷Eq.3 |     | c                            |     | c   |     | c   |     |
4:
5: forOn_Path_Device dev inc.pathdo We estimate the access demand D by substituting r′ with
|     |                                    |                    |     |                        |     |        |            |                  |                        | c        |         |         | c      |
| --- | ---------------------------------- | ------------------ | --- | ---------------------- | --- | ------ | ---------- | ---------------- | ---------------------- | -------- | ------- | ------- | ------ |
| 6:  |                                    | α=estimate_α(dev); |     |                        |     |        | D′.        |                  |                        |          |         |         |        |
|     |                                    |                    |     |                        |     |        | Hence,     | hosts update     | r c                    | and D c  | of each | channel | at the |
| 7:  |                                    | c.α=min(α,c.α);    |     |                        |     |        | c          |                  |                        |          |         |         |        |
|     |                                    |                    |     |                        |     |        | beginning  | ofthe scheduling |                        | function | (ALG1   | L2–4).  | Since  |
|     | c.TR=estimate_TR(c.demand,c.α,TW); |                    |     |                        |     | ▷ Eq.5 |            |                  |                        |          |         |         |        |
| 8:  |                                    |                    |     |                        |     |        | CXL fabric | is lossless,the  | aggregatedmemoryaccess |          |         |         | rate   |
| 9:  | sleep(c.TW−c.TR)                   |                    |     | ▷Yieldtoothermchannels |     |        |            |                  |                        |          |         |         |        |
canbecalculateddirectly,ratherthanusingEq.3asinCSFQ.
10: procedureESTIMATE_α(On_Path_Devicedev)
FairShareRateEstimation.MemChannelthencalculates
ifcur_time≥start_time+Kthen
11:
thefairsharerateαonthehostandissuestherightamount
| 12: |     | F,D=0,0; | ▷localrateF,localdemandD |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofload/storeinstructionstoavoidcongestion.However,us-
| 13: |     | formchannel | c indev.mchannelsdo |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ingEq.2tocomputeαdirectlyrequiresahosttoknowthe
| 14: |     | F+=c.rate; |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15: D=max(D,c.demand); aggregatedmemorydemandsonedges(D )acrossallon-
uv
pathhardwareittraverses.UnlikeEthernet,wherethearrival
| 16: |     | dev.F,dev.D=agg_rate(F,D); |     |     | ▷viasharedmemory |     |     |     |     |     |     |     |     |
| --- | --- | -------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
17: iflocalhostisdev.hostthen rate (i.e., demand) can be directly measured at the switch
18: dev.α=min(dev.α×dev.C,dev.D); ▷Eq.4 port,hereitmustbeobtainedthroughrecursivecalculations
dev.F
(Eq.1).Specifically,thememorydemandofaCXLendpoint
| 19: |     | start_time=cur_time; |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
returndev.α; adapterdependsonincomingmemorystreamsfromallcorre-
20:
spondingupstreamCXLswitchports,whichinturndepend
21: procedureADJUST_CAPACITY(On_Path_Devicedev)
22: ifdev.F<dev.Canddev.l>δthen onincomingstreamsfromupstreamhostadapters.Thisrecur-
23: dev.C=dev.C×(1−dev.l−δ)▷MultiplicativeDecrease sivedependencycaneasilyleadtoanaccumulationoferror
2(1−δ)
margins.Furthermore,bothdemandsandfairshareratesmust
24: elseifdev.l≤δthen
25: dev.C=dev.C+λ×(δ−dev.l)×K▷AdditiveIncrease besharedacrosshosts,makingthealgorithmdifficulttoscale.
|     |     |     |     |     |     |     | Instead,weestimatethefairshareratebasedon |     |     |     |     |     | theaggre- |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --------- |
26: dev.C=max(dev.C,dev.max_capacity)
|                          |     |     |     |                         |     |     | gatedremotememoryaccessrateF                       |     |     | v onthehostforhardware |     |     |     |
| ------------------------ | --- | --- | --- | ----------------------- | --- | --- | -------------------------------------------------- | --- | --- | ---------------------- | --- | --- | --- |
| Withoutcontention(e.g.,D |     |     | ≤C  | ),alldemandscanbesatis- |     |     |                                                    |     |     |                        |     |     |     |
|                          |     |     | v v |                         |     |     | nodev,definedasthenumberofload/storecommandstrans- |     |     |                        |     |     |     |
|                          |     |     |     | =max                    |     | D   |                                                    |     |     |                        |     |     |     |
fiedbysettingα v tothemax,i.e.,α v euv∈E uv .There mittedthroughv.Thisapproachisstraightforwardtocompute
| are | two key | differences | when applying |     | the fluid | model in |     |     |     |     |     |     |     |
| --- | ------- | ----------- | ------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
andcanbecalibratedusinghardwarebandwidthtelemetry.
| ourcasecomparedwithCSFQ. |     |            | First,memoryaccessrates |          |             |      |                                     |     |     |     |     |     |            |
| ------------------------ | --- | ---------- | ----------------------- | -------- | ----------- | ---- | ----------------------------------- | --- | --- | --- | --- | --- | ---------- |
|                          |     |            |                         |          |             |      | WenextdescribehowMemChannelperforms |     |     |     |     |     | fair-share |
| remain                   | the | same along | the flow                | path. As | a result,we | com- |                                     |     |     |     |     |     |            |
rateestimation(Algorithm1L10–20).Wedefinetheaggre-
| pute | memory | access demand | instead | of  | using | flow arrival |                          |     |     |     |     |        |         |
| ---- | ------ | ------------- | ------- | --- | ----- | ------------ | ------------------------ | --- | --- | --- | --- | ------ | ------- |
|      |        |               |         |     |       |              | gatedmemoryaccessrateasF |     |     | =∑  | f   | ,where | f isthe |
ratesforedgesandvertices.Second,weusethelinktransmis- v euv∈E uv uv
|     |     |     |     |     |     |     | flowonedgee | and | f =r | for∀v | ∈V ,∀v | ∈V  | .Since |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | ----- | ------ | --- | ------ |
|     |     |     |     |     |     |     |             | uv  | cb   | c     | c C    | h   | H      |
sioncapacityateachnoderatherthanthedefaultmaximum
|     |     |     |     |     |     |     | the access | rate is the | same within | a   | flow p,the | aggregated |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------- | --- | ---------- | ---------- | --- |
bandwidthspecifiedinthehardwaredocumentation.Thisis
|         |     |               |     |              |     |           | rateF isexpressedas∑ |     |             | r   | ,whereP | denotesall |     |
| ------- | --- | ------------- | --- | ------------ | --- | --------- | -------------------- | --- | ----------- | --- | ------- | ---------- | --- |
|         |     |               |     |              |     |           | v                    |     | ecb∈p,∀p∈Pv |     | c       | v          |     |
| because | the | numberofFLITs | a   | CXL portofan |     | adapteror |                      |     |             |     |         |            |     |
flowspassingthroughnodev.Undercongestion(Eq.2),we
switchcanhandleandtransmitisnotstaticbutdependson
estimateαiterativelyusingthecurrentcongestioncondition
thequeuingconditionsandinternalexecutionstatus.
Cv.Iftheestimatedfairsharerateexceedsthelargestlocalde-
Fv
4.3 TheTransportAlgorithm mandmax c∈VL D c ,thereisnocongestionwithinthelocalhost,
|     |     |     |     |     |     |     | andthusαissettothemaximumdemand,i.e.,max |     |     |     |     |     | D .      |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | -------- |
|     |     |     |     |     |     |     |                                          |     |     |     |     |     | euv∈E uv |
AccessRateandDemandEstimation.Wemeasurethenum-
C v
berofremotecachelineaccessesnduringaschedulingwin- α =min(α , max D ) (4)
|     |     |     |     |     |     |     |     | new | old | F   |     | c   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dowT byreadingperformancecounters(§3.3).Themea- v ecb∈p,∀p∈Pv
W
| suredCXL |     | memoryaccess | rate | formchannel | c   | is r ′ = n S, |            |                 |     |        |         |           |     |
| -------- | --- | ------------ | ---- | ----------- | --- | ------------- | ---------- | --------------- | --- | ------ | ------- | --------- | --- |
|          |     |              |      |             |     | c T           | At the end | of the sampling |     | window | K,hosts | calculate | the |
W
whereSdenotesthecachelinesize.r ′ reflectstheamountof fair share rates of all hardware components used by their
c
| CXLbandwidthconsumedbymchannelcoverT |     |     |     |     |            | .Similarly, |                                                    |                |     |        |        |      |            |
| ------------------------------------ | --- | --- | --- | --- | ---------- | ----------- | -------------------------------------------------- | -------------- | --- | ------ | ------ | ---- | ---------- |
|                                      |     |     |     |     |            | W           | mchannels.                                         | The aggregated |     | memory | access | rate | F v is the |
| themeasuredmemorydemandisD′          |     |     |     |     | n S,whereT |             |                                                    |                |     |        |        |      |            |
|                                      |     |     |     | =   |            | R isthe     | onlyvariablesharedacrosshoststocomputethefairshare |                |     |        |        |      |            |
|                                      |     |     |     | c   | T R        |             |                                                    |                |     |        |        |      |            |
application’srunningtimewithinT .D′ indicatesthemem- ratesforsharedCXLhardware(e.g.,switchesandexpanders).
|     |     |     |     | W c |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orybandwidththatmchannelcwouldgenerateifitwerenot To disseminate this information,eachhostwrites the local
throttledbythetransportalgorithm.Measuringapplication sumofthememoryaccessratesforeachhardwarecomponent
demand in this manneris possible because the application toasmall,dedicatedsharedmemoryaddress.Theaggregated
runsatfullspeedwithoutinterruptionsorslowdownsduring rate F can then be obtained by summing these local rates.
v
T ,asouralgorithmensuresthatCXLcomponentsarenot Themchannelfairsharerateα istheminimumvaluealong
| R   |     |     |     |     |     |     |     |     |     | c   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

path p(i.e.,α =min α ),whichisthentranslatedinto pacityisdifficulttomeasureandmaychangedynamically.
|     | c   | euv∈p | v   |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
therunningtimetocontrolapplicationexecution. Inspiredbythedelay-basedcongestioncontrol[24,30,65],
Time-basedRateControl.MemChannelcontrolstheFLIT wemaintainloadfactorslbasedonthecongestionsignals.
transmissionratebyadjustingtheapplicationthreadrunning
|        |        |                 |     |        |     |               |     | l =(1−g)×l |     | +g×L | (6) |
| ------ | ------ | --------------- | --- | ------ | --- | ------------- | --- | ---------- | --- | ---- | --- |
| T      |        |                 |     |        | T   |               |     | new        |     | old  |     |
| time R | within | each scheduling |     | window | W   | (§3.3). After |     |            |     |      |     |
runningforT ,theapplicationthreadyieldstoanotherandre- Lrepresentsthepercentageofresponsesmarkedashaving
R
mainsinthewaitingqueueuntilthenextschedulingwindow moderate or severe overload in the device load field. For
begins.AshortschedulingwindowT W enablesfine-grained telemetrycases,thebackpressureaveragepercentageinthe
control over application execution but incurs high context- QoSresponseisdirectlyusedasL.gisaconfigurableparam-
| switching | overhead | due | to frequent | timer-expiration |     | inter- |     |     |     |     |     |
| --------- | -------- | --- | ----------- | ---------------- | --- | ------ | --- | --- | --- | --- | --- |
eter.Usingthem,wethendividetheoperationregionintothe
rupts.Conversely,alargerT reducesschedulingoverhead followingcategoriesandapplydifferentscalingstrategies:
W
| but causes | tail | latency | increases | because | requests | are less |     |     |     |     |     |
| ---------- | ---- | ------- | --------- | ------- | -------- | -------- | --- | --- | --- | --- | --- |
• CongestionAvoidance,occurringwhenfairsharerateis
tightlycoordinated.WechooseT W =100µsinourprototype, increasingandl isrelativelylarge.Thismeansthatsome
whichstrikesabalancebetweenthesetwotrade-offs.
remotememoryaccesseshaveexperiencedhighdelays.We
SimilartoTCP,aflowcannottransmitbyteswhenthere performamultiplicativedecreaseandscalethereducing
| is nofree | spacein | the congestion |     | window. | Bytemporarily |     |     |     |     |     |     |
| --------- | ------- | -------------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
factorbasedontheloadfactorl(ALG1L22–23).
stallingapplicationexecution,wecanregulatethememoryac-
|     |     |     |     |     |     |     | • Congestion | Free, where | l < | δ. This indicates | that the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ----------------- | -------- |
cessratetopreventcongestion.Toavoidtemporalcontention,
rDIMMisabletodeliverpredefinedbandwidth.Depend-
applicationthreadsandtheirmchannelsrunasynchronously,
ingonhowmuchidlenessthechannelhasobserved,our
| even though | they | may | have the | same | scheduling | window. |                             |     |     |               |     |
| ----------- | ---- | --- | -------- | ---- | ---------- | ------- | --------------------------- | --- | --- | ------------- | --- |
|             |      |     |          |      |            |         | algorithmwilladdλ×(δ−h.l)×K |     |     | (ALG1L24–25). |     |
MemChannelestimatestheCXLmemoryaccesssizeBdur-
ingoneschedulingwindowasD T .Toensurefairsharing 4.4 AlgorithmExtensions
c R
| ofCXLmemory,themax-minfairremotememorysizeB |     |     |     |     |     | fair |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
WeightSupport.MemChannelcanbeextendedtosupport
| thatanapplicationcanaccessduringT |     |     |     |     | ismin(α | ,D )×T . |                                |     |     |                     |     |
| --------------------------------- | --- | --- | --- | --- | ------- | -------- | ------------------------------ | --- | --- | ------------------- | --- |
|                                   |     |     |     | W   |         | c c W    | mchannelswithdifferentweightsw |     |     | ,meaningthatallcon- |     |
c
Thegoalofourtransportistoachievemax-minfairresource gestionchannelswillreceiveafairsharerateofw .The
c α c
allocationwithoutwastingCXLmemorybandwidth.There-
onlymodificationrequiredistoupdateEq.5accordingly.
| fore,wesetB=B |     | .Rearranginggivesafairrunningtime |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fair
|                            |     |     |     |     |     |     |     | min(w |     | α ,D )T |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- |
| duringoneschedulingwindow: |     |     |     |     |     |     |     |       | c   | c c W   |     |
|                            |     |     |     |     |     |     |     | T R = |     |         | (7) |
D
|     |     |     | min(α | ,D )T |     |     |     |     |     | c   |     |
| --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
c c W
T R = (5) HCSFQ Support. Our algorithm achieves the fair share
D
c
amongmchannels,equivalenttoasingle-layerHCSFQ.How-
New Congestion Signals. In Ethernet, congestion can be ever,inpractice,anapplicationmayusemultiplemchannels
readilyinferredfromexplicitsignalslikepacketloss.How-
(two-layerHCSFQ),andatenantmayrunmultipleapplica-
| ever, such | signals | are largely |     | unavailable | in the | CXL fab- |     |     |     |     |     |
| ---------- | ------- | ----------- | --- | ----------- | ------ | -------- | --- | --- | --- | --- | --- |
tions(three-layerHCSFQ).SupportingHCSFQisstraightfor-
ric. Instead, the CXL 3.2 specification [4] mandates that wardinMemChannel.In§4.3,weknow(a)thetransmission
| memory | expanders | include | a   | 2-bit device-internal |     | load in- |     |     |     |     |     |
| ------ | --------- | ------- | --- | --------------------- | --- | -------- | --- | --- | --- | --- | --- |
capacityofthehardware,whichcorrespondstotherootnode
| dication | in memory | responses |     | (S2M),which | encodes | four |     |     |     |     |     |
| -------- | --------- | --------- | --- | ----------- | ------- | ---- | --- | --- | --- | --- | --- |
ofthetree,and(b)memoryaccessdemandandaccessrateof
levelsofcongestiontypicallyderivedfromtheexpander’sin- themchannel,whichcorrespondtotheleafnodesofthetree.
ternalqueueoccupancy.Inaddition,thespecificationstrongly
Theaggregateddemand/rateoftheparentnodeisthesumof
recommendsthatmemorydevicesexposeaQoStelemetry itschildren’s(i.e.,D =∑D ).ByapplyingEq.4recursively
|     |     |     |     |     |     |     |     | v   | u   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mechanismthatperiodicallyreports(1)egress-portbackpres-
fromtheroottotheleaves,wecandeterminethefairshare
sure,indicatingthatoneormoreupstreamqueuesbetween
rate,α,foreachlayer.Wethentranslatetheαofthelastlayer
the expanderandthe hostare saturated,and(2) temporary into the mchannel running time using Eq. 5. Note thatthe
throughputreductionsduringDRAMrefreshoperations.
treeisusedforallhardwarecomponents(adapters,switches,
Congestionattheadaptercanbequeriedatthehostsince andDIMMs)asshowninoursystemmodel(§3.4).
| the device | is attached | locally. |     | ForCXL | DIMMs,we | lever- |     |     |     |     |     |
| ---------- | ----------- | -------- | --- | ------ | -------- | ------ | --- | --- | --- | --- | --- |
4.5 BoundAnalysis
| age the device-loadfieldto |     |     | capture | boththe | device’s | inter- |     |     |     |     |     |
| -------------------------- | --- | --- | ------- | ------- | -------- | ------ | --- | --- | --- | --- | --- |
nalqueueingpressureandtemporarythroughputreductions, Wepresentthefollowingtheoremtoshowthatouralgorithm
whiledisablingtheegress-portbackpressuresignal.Theback- provides performance bounds for applications. Consider a
pressureinformationisconveyedthroughtelemetrymessages memorychannelwithafixedfairsharerateα andweightw
|     |     |     |     |     |     |     |     |     |     | c   | c   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andistreatedasacongestionsignalforCXLswitches,since duringasamplingwindowK.Intheidealcase,thememory
switchesexposenoexplicitcongestionnotifications. channelshouldnotissueload/storetrafficexceedingw c α c K.
TransmissionCapacityEstimation.Duetotheinternalcom- We can prove that no matter how the application tries to
plexityofCXLhardwarecomponents,thetransmissionca- game the system,ourmechanism ensures thatthe bytes of

load/storetrafficfromamemorychannelarenomorethan: Avg w/o MC Tail w/o MC )SPOM( tuphguorhT  140 w/o MC w/ MC
|     |                   |     |                        |     |     |     |                   | Avg w/ MC |     | Tail w/ MC |      |     |     |     |
| --- | ----------------- | --- | ---------------------- | --- | --- | --- | ----------------- | --------- | --- | ---------- | ---- | --- | --- | --- |
| w   | α K(1+2TW),whereT |     | istheschedulingwindow. |     |     |     |  700              |           |     |            |  120 |     |     |     |
| c   | c                 | K   | W                      |     |     |     | )sn( ycnetaL  600 |           |     |            |  100 |     |     |     |
|     |                   |     |                        |     |     | K   |   5               | 0 0       |     |            |      |     |     |     |
Proof.ConsideranyintervalK=[t′,t′′),andleth=⌊ ⌋.In   4 0 0  80
|                                                     |     |     |     |     |     | T W |   3  | 0 0  |                |     |  60 |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | ---- | -------------- | --- | --- | --- | --- | --- |
| aninterval,therewillbehfullschedulingwindows,atmost |     |     |     |     |     |     |  200 |      |                |     |  40 |     |     |     |
| oneschedulingwindowbeforet′,andatmostoneschedul-    |     |     |     |     |     |     |  100 |      |                |     |  20 |     |     |     |
|                                                     |     |     |     |     |     |     |      |  0 A | B C            | D F |  0  |     |     |     |
|                                                     |     |     |     |     |     |     |      |      | YCSB Workloads |     |     | A   | B C | D F |
ing window aftert′′. Thus,the maximum number of bytes YCSB Workloads
transmittedduringK is∑ h + 1B .BasedonEq.7,wehave: (a)MICAlatency. (b)MICAthroughput.
i= 0 i
|     |     |     |     |     |     |     |     | Avg w/o MC | Tail w/o MC |     |  16 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | --- | --- | --- |
B i ≤B fair =min(w c α c ,D c )T W ≤w c α c T W . (8) Avg w/ MC Tail w/ MC )SPOM( tuphguorhT  14 w/o MC w/ MC
 1200
|                                         |     |     |     |     |     |     | )sn( ycnetaL  1000 |     |     |     |  12 |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
| Therefore,wecanderivetheboundasfollows: |     |     |     |     |     |     |                    |     |     |     |  10 |     |     |     |
|                                         |     |     |     |     |     |     |  800               |     |     |     |  8  |     |     |     |
 600
|     | h+1 |     |     | (cid:18) K | (cid:19) |     |  400 |     |     |     |  6  |     |     |     |
| --- | --- | --- | --- | ---------- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
 4
|     | ∑B  | ≤(h+2)w | α T | ≤ +2       | w α | T        |  200 |                 |                |     |  2  |                    |     |     |
| --- | --- | ------- | --- | ---------- | --- | -------- | ---- | --------------- | -------------- | --- | --- | ------------------ | --- | --- |
|     |     | i       | c c | W T        | c   | c W      |      |  0 A            | B C            | D F |  0  |                    |     |     |
|     | i=0 |         |     | W          |     |          |      |                 | YCSB Workloads |     |     | A                  | B C | D F |
|     |     |         |     |            |     | (9)      |      |                 |                |     |     | YCSB Workloads     |     |     |
|     |     |         |     | (cid:18)   | T   | (cid:19) |      |                 |                |     |     |                    |     |     |
|     |     |         |     |            | W   |          |      | (c)Silolatency. |                |     |     | (d)Silothroughput. |     |     |
|     |     |         |     | =w α K 1+2 |     | .        |      |                 |                |     |     |                    |     |     |
|     |     |         |     | c c        | K   |          |      |                 |                |     |     |                    |     |     |
Figure7:ThroughputandlatencyofMICAandSilooverone
Thisboundindicatesthattheapplicationcanissueatmost ×8adaptertothememorypool,comparingbetweenw/andw/o
| 2TW |     |     |     |     |     |     | MemChannelscenarios.Weuse32threadsinthisexperiment. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
fractionalmorerequestsintheshortrun,ensuringthat
K
ouralgorithmachievesamax-minfairbandwidthallocation. Avg w/o MC Tail w/o MC  300
|     |     |     |     |     |     |     |     | Avg w/ MC |     | Tail w/ MC | )SPOM( tuphguorhT  250 | w/o MC | w/ MC |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | ---------------------- | ------ | ----- | --- |
 700
| 5   | Evaluation |     |     |     |     |     | )sn( ycnetaL  600 |     |     |     |  200 |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | ---- | --- | --- | --- |
|     |            |     |     |     |     |     |  500              |     |     |     |  150 |     |     |     |
 400
| 5.1 | ExperimentalMethodology |     |     |     |     |     |  300 |     |     |     |  100 |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- |
 200
|     |     |     |     |     |     |     |  100 |      |     |     |  50 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |      |  0 A | B C | D F |  0  |     |     |     |
Testbeds and Workloads. We use the same experimental A B C D F
|     |     |     |     |     |     |     |     |     | YCSB Workloads |     |     | YCSB Workloads |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | -------------- | --- | --- |
setupas§2.3.Ourevaluationsuseadiversesetofmemory-
|     |     |     |     |     |     |     |     | (a)MICAlatency. |     |     |     | (b)MICAthroughput. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ------------------ | --- | --- |
intensiveworkloadsaspriorstudies[53,79,82,91].(a).In-
|     |     |     |     |     |     |     |     | Avg w/o MC | Tail w/o MC |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | --- | --- | --- |
memory databases. We run a hashtable-based in-memory Avg w/ MC Tail w/ MC )SPOM( tuphguorhT  30 w/o MC w/ MC
 1200
| key-valuestore,MICA[49],configuredwith8-bytekeysand |     |     |     |     |     |     |                    |     |     |     |  25 |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
|                                                     |     |     |     |     |     |     | )sn( ycnetaL  1000 |     |     |     |  20 |     |     |     |
 800
| 100-bytevalues,andwefocusonitsin-memorycomponents: |     |     |     |     |     |     |  600 |     |     |     |  15 |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
 10
| circularlogs,lossyconcurrenthashindexes,andbulkchain- |     |             |             |                 |     |       |  400 |     |                |     |     |                |     |     |
| ----------------------------------------------------- | --- | ----------- | ----------- | --------------- | --- | ----- | ---- | --- | -------------- | --- | --- | -------------- | --- | --- |
|                                                       |     |             |             |                 |     |       |  200 |     |                |     |  5  |                |     |     |
| ing.WealsoevaluateaB-tree–baseddatabase,Silo[77],de-  |     |             |             |                 |     |       |      |  0  |                |     |     |                |     |     |
|                                                       |     |             |             |                 |     |       |      | A   | B C            | D F |  0  | A              | B C | D F |
|                                                       |     |             |             |                 |     |       |      |     | YCSB Workloads |     |     | YCSB Workloads |     |     |
| signed                                                | for | low-latency | transaction | processing,with |     | a 1KB |      |     |                |     |     |                |     |     |
valuesize.TheclienttrafficisgeneratedviaYCSB[33].(b). (c)Silolatency. (d)Silothroughput.
Graphanalytics.WedeploytheGAP[27]benchmarksuite, Figure8:ThroughputandlatencyofMICAandSiloovertwo
×8adapterstothememorypool,comparingbetweenw/andw/o
includingseveralgraphkernels:Breadth-FirstSearch(BFS),
Single-SourceShortestPaths(SSSP),PageRank(PR),Con- MemChannelscenarios.Weuse64threadsinthisexperiment.
bandwidthtotheremotememorypool.However,MemChan-
nectedComponents(CC),andBetweenessCentrality(BC),
whichuseaKroneckergraphandauniformrandomgraph. nelreducesthein-fabriccongestionandyieldslatencysav-
(c).High-performancecomputing(HPC).WealsouseSPEC ings.Forexample,asshowninFigure7-b/d,MemChannel
CPU2017[13]andPARSEC[28],includingscientificand reduces the average CXL memory access latency of Silo
numericalapplicationsthatstressmemoryaccess. by 28.6%/38.0%/38.4%/38.3%/28.8%, and tail latency by
8.7%/28.0%/27.7%/29.3%/5.8%acrossfiveworkloadscom-
| Performance |     | Metrics. | We  | report application |     | throughput, |     |     |     |     |     |     |     |     |
| ----------- | --- | -------- | --- | ------------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
latency,andperformanceslowdown. MemChannelobtains pared with the cases when disabling MemChannel. MICA
per-mchannelbandwidthusingperformancecounters(§3.3) shows similar results. We then use two CXL adapters and
andaggregatesthemtoderivebothapplication-levelandhost- run64threads.Theaveragethroughputoverfiveapplications
levelmemorybandwidth.WemeasureCXLmemoryaccess reaches225.3MOPSundermchannel(Figure8),achieving
|     |     |     |     |     |     |     | 41.0GB/s | CXL | bandwidth |     | to the | remote memory |     | pool. In |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | --- | ------ | ------------- | --- | -------- |
latencyviaCHAqueues,i.e.,dividingoccupancybythenum-
berofCXLrequests,followingtheColloid’sapproach[79]. termsoflatency,similarly,MemChannelmitigatesthefabric
contentionandachieves23.9%and19.6%loweraverageand
5.2 ApplicationPerformanceoverMemChannel
taillatenciescomparedtothecaseswithoutMemChannel.
WefirstexaminehowmuchperformanceMemChanneldeliv-
5.3 Intra-HostPerformanceIsolation
erstoapplicationswhenaccessingtheswitchedCXLmem-
ory pool. In this experiment, we use MICA and Silo and Wecreateintra-hostcontentionbysharingthehostadapter
reportthethroughputandlatency.Withone×8CXLport,as between an application and competing background traffic.
showninFigure7-a/c,applicationsshownearlynothrough- WeuseBwavesandRomsfromCPUSPECasourapplica-
put degradation,and MemChannel can provide 19.6 GB/s tions.AsshowninFigure9-a/b,applicationsrunningwithout

|     |     |  10 |     |  8  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
 7 w/o mchannel w/o mchannel w/o mchannel App w/o MC App w/ MC
oitaR nwodwolS  6 w/ mchannel oitaR nwodwolS  8 w/ mchannel oitaR nwodwolS  7 w/ mchannel Ttl w/o MC Ttl w/ MC
|     |     |     |     |  6  |     | )s/BG( htdiwdnaB  25 |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- |
|  5  |     |  6  |     |  5  |     |  20                  |     |
|  4  |     |     |     |  4  |     |                      |     |
|  3  |     |  4  |     |     |     |  15                  |     |
|     |     |     |     |  3  |     |  10                  |     |
|  2  |     |     |     |  2  |     |                      |     |
|  1  |     |  2  |     |  1  |     |  5                   |     |
 0  0  20  40  60  80  100  0  0  20  40  60  80  100  0  0  20  40  60  80  100  0  0  20  40  60  80  100
Contending Traffic Load (%) Contending Traffic Load (%) Contending Traffic Load (%) Contending Traffic Load (%)
(a)BwaresSlowdown. (b)RomsSlowdown. (a)BCSlowdown. (b)BCBandwidth.
App w/o MC App w/ MC App w/o MC App w/ MC  4.5 App w/o MC App w/ MC
Ttl w/o MC Ttl w/ MC Ttl w/o MC Ttl w/ MC oitaR nwodwolS  4 w/o mchannel Ttl w/o MC Ttl w/ MC
)s/BG( htdiwdnaB  25 )s/BG( htdiwdnaB  25  3.5 w/ mchannel )s/BG( htdiwdnaB  25
|  20 |     |  20 |     |  3  |     |  20 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
 2.5
|  15 |     |  15 |     |  2  |     |  15 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
 1.5
|  10 |     |  10 |     |     |     |  10 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  5  |     |  5  |     |  1  |     |  5  |     |
 0.5
|  0  |     |  0  |     |  0  |     |  0  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
 0 Contending Traffic Load (%)  20  40  60  80  100  0 Contending Traffic Load (%)  20  40  60  80  100  0 Contending Traffic Load (%)  20  40  60  80  100  0 Contending Traffic Load (%)  20  40  60  80  100
(c)BwaresBandwidth. (d)RomsBandwidth. (c)PRSlowdown. (d)PRBandwidth.
Avg w/o MC Avg w/ MC Avg w/o MC Avg w/ MC Figure 10: Application slowdown andCXL bandwidthwhen
| Tail w/o MC | Tail w/ MC | Tail w/o MC | Tail w/ MC |                                                   |     |     |     |
| ----------- | ---------- | ----------- | ---------- | ------------------------------------------------- | --- | --- | --- |
|             |            |  2000       |            | varyingcontendingtrafficunderin-fabriccongestion. |     |     |     |
 2000
| )sn( ycnetaL |     | )sn( ycnetaL  1500 |     |     |     |     |     |
| ------------ | --- | ------------------ | --- | --- | --- | --- | --- |
 1500 switching point. Under heavy contention (e.g., more than
|  1000 |     |  1000 |     |     |     |     |     |
| ----- | --- | ----- | --- | --- | --- | --- | --- |
80%trafficload),MemChannelachievesanaverageof97.2%
|  500                        |             |  500                        |                      |                                            |     |     |     |
| --------------------------- | ----------- | --------------------------- | -------------------- | ------------------------------------------ | --- | --- | --- |
|  0                          |             |  0                          |                      | bandwidthutilizationacrosstwoapplications. |     |     |     |
|  0  20                      |  40  60  80 |  100  0                     |  20  40  60  80  100 |                                            |     |     |     |
| Contending Traffic Load (%) |             | Contending Traffic Load (%) |                      |                                            |     |     |     |
5.5 Fairness
| (e)BwaresLatency. |     | (f)RomsLatency. |     |     |     |     |     |
| ----------------- | --- | --------------- | --- | --- | --- | --- | --- |
Figure9:Applicationslowdown,CXLbandwidth,andlatency We achieve a fair bandwidth share by calculating the
whenvaryingcontendingtrafficunderhostadaptercontention. mchannel rate, and MemChannel enforces it via the rate
MemChannelexperience7.0×and8.8×slowdownsasthe control algorithm. To measure effectiveness, we co-locate
pairsofSPECCPU,MICA,andSiloapplications,gradually
| contending | traffic load increases | to 100% | for bwaves and |     |     |     |     |
| ---------- | ---------------------- | ------- | -------------- | --- | --- | --- | --- |
increasingthenumberofthreadsforbothapplicationstoin-
| roms,respectively. | In contrast,applications |     | running under |     |     |     |     |
| ------------------ | ------------------------ | --- | ------------- | --- | --- | --- | --- |
MemChannelonlyseea2.5×slowdown.Thisimprovement ducecontentionintheCXLfabric,andreporttheresulting
memorybandwidthforeach.AsshowninFigure11,under
occursbecauseMemChannelprovidesperformanceisolation
among co-locatedchannels throughits transportalgorithm lightcontention(e.g.,onethread),MemChannelmatchesthe
|     |     |     |     | baseline | by allocating bandwidth | according | to application |
| --- | --- | --- | --- | -------- | ----------------------- | --------- | -------------- |
(§4.3).Tobetterunderstandthiseffect,wefurthermeasure
demand.Underheavycontention(e.g.,15threads),compared
theCXLaccessbandwidthoftheapplicationsandthetotal
bandwidth,asshowninFigure9-c/d.MemChannelallocates with the case without MemChannel, MemChannel signifi-
cantlyreducesthebandwidthgapbetweentwoapplications:
morebandwidthtoapplicationsbasedonmax-minfairness.
Under heavy contention (e.g.,when the contending traffic from8.9GB/sto1.3GB/sforBwaves+Silo,from11.5GB/sto
loadis≥80%),MemChannelachievesanaverageof96.1% 1.8GB/sforBwaves+MICA,andfrom3.1GB/sto0.1GB/sfor
MICA+Silo.Ourtransportcontrolstheapplication’sremote
bandwidthutilizationacrosstwoapplications,whilereducing
averagelatencyby51.6%and35.1%andtaillatencyby25.8% accessbandwidth,ensuringafairshareofhardwareresources.
|     |     |     |     | We compare | our runtime | with TPP [61] | under different |
| --- | --- | --- | --- | ---------- | ----------- | ------------- | --------------- |
and26.3%forBwavesandRoms,asshowninFigure9-e/f.
backgroundtrafficgeneratedbythesameSPECapplication
5.4 Inter-HostPerformanceIsolation
asabove(Figure12).WerunfivetypesofYCSBworkloads
Wethensetupin-fabriccongestionas§2.3andevaluatehow overMICA,withthelocal-to-remotememorycapacityratio
MemChannelmitigatestheissue.Weusetwographapplica- settoeight.Withoutbackgroundtraffic,TPPslightlyoutper-
tions,i.e.,BetweenessCentrality(BC)andPageRank(PR), formsoursystemby1.2×intermsofthroughputandreduces
inthisexperiment.AsshowninFigure10-a/c,applications latency by 16% across all five workloads. This is because
running without MemChannel experience 7.2× and 4.2× sufficientremotememorybandwidthisavailabletosupport
slowdownsasthecontendingtrafficloadincreasesto100% pagedemotionandpromotion.However,undermoderatecon-
forBCandPR,respectively.Incontrast,applicationsrunning tention,ourruntimematchestheperformanceofTPP.Under
underMemChannelonlysee3.1×and2.1×slowdown,re- heavy contention,ourruntime achieves a 1.5× throughput
| spectively. | The performance | improvementcomes | from the |     |     |     |     |
| ----------- | --------------- | ---------------- | -------- | --- | --- | --- | --- |
improvementandreduceslatencyby43%.Thisisduetothe
factthatMemChannelallocatesbandwidthacrosscompeting performanceisolationcapabilityprovidedbyMemChannel.
applicationsbasedontheirperformancerequirements.Again,
5.6 SystemOverheads
wemeasuretheapplicationCXLaccessbandwidthandthe
total bandwidth,as shown in Figure 10-b/d. MemChannel MemChannelincursmarginaloverheadstotheapplication.
allocatesbandwidthinamax-minfairnessmannerattheCXL Fair-shareratecalculationandassignmentareperformedonly

 18
 20 Bwaves w/o MC Bwaves w/ MC Bw a v e s  w / o   M C Bw a v e s  w /   M C MICA w/o MC MICA w/ MC
)s/BG( htdiwdnaB Silo w/o MC Silo w/ MC )s/BG( htdiwdnaB  20 M I C A   w / o   M C M I C A   w /   M C )s/BG( htdiwdnaB  16 Silo w/o MC Silo w/ MC
|  15 |     |     |     |     |     |     |     |     |  14 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |  15 |     |     |     |  12 |     |     |     |     |
 10
|  10 |     |     |     |     |  10 |     |     |     |  8  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 6
 5
|     |     |     |     |     |  5  |     |     |     |  4  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 2
|     |  0  |     |         |     |  0  |     |             |     |  0  |     |     |      |       |
| --- | --- | --- | ------- | --- | --- | --- | ----------- | --- | --- | --- | --- | ---- | ----- |
|     | 1 3 | 5 7 | 9 11 13 | 15  |     | 1 3 | 5 7 9 11 13 | 15  |     | 1 3 | 5 7 | 9 11 | 13 15 |
Per-application Thread Number (#) Per-application Thread Number (#) Per-application Thread Number (#)
|     | (a)Bwaves+SILO. |     |     |     |     | (b)Bwaves+MICA. |     |     |     |     | (c)MICA+Silo. |     |     |
| --- | --------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | ------------- | --- | --- |
Figure11:ComparetheCXLmemorybandwidthwhenrunningtwoapplicationswithandwithoutMemChannelsupportonahost.
Wegraduallyincreasethethreadnumberforbothapplicationstocreatecontentionthememoryfabric.
 1  4 )SPOM( tuphguorhT  3 )SPOM( tuphguorhT  2.5  2.5 )SPOM( tuphguorhT
MC latency MC throughput  3.5   1 . 4 M C   l at e n cy M C   t h r o u g h p u t MC latency MC throughput
)su( ycnetaL  0.8 TPP latency TPP throughput  3 )su( ycnetaL   1 . 2 T P P  l a t en c y T P P   t h r o u g h p u t  2.5 )su( ycnetaL  2 TPP latency TPP throughput  2
|      |     |     |     |  2.5 |  1   |     |     |  2   |      |     |     |     |      |
| ---- | --- | --- | --- | ---- | ---- | --- | --- | ---- | ---- | --- | --- | --- | ---- |
|  0.6 |     |     |     |      |  0.8 |     |     |      |  1.5 |     |     |     |  1.5 |
|      |     |     |     |  2   |      |     |     |  1.5 |      |     |     |     |      |
|  0.4 |     |     |     |  1.5 |  0.6 |     |     |  1   |  1   |     |     |     |  1   |
|  0.2 |     |     |     |  1   |  0.4 |     |     |      |  0.5 |     |     |     |  0.5 |
|      |     |     |     |  0.5 |  0.2 |     |     |  0.5 |      |     |     |     |      |
|      |  0  |     |     |  0   |  0   |     |     |  0   |  0   |     |     |     |  0   |
YCSB-AYCSB-BYCSB-CYCSB-DYCSB-F YCSB-AYCSB-BYCSB-CYCSB-DYCSB-F YCSB-AYCSB-BYCSB-CYCSB-DYCSB-F
|     |                  | Workload |     |     |     |                        | Workload |     |     |                     | Workload |     |     |
| --- | ---------------- | -------- | --- | --- | --- | ---------------------- | -------- | --- | --- | ------------------- | -------- | --- | --- |
|     | (a)NoContention. |          |     |     |     | (b)ModerateContention. |          |     |     | (c)HeavyContention. |          |     |     |
Figure12:LatencyandthroughputforMICArunninginMemChannelandTPPunderfiveYCSBworkloads.Y-1axisislatency,and
Y-2axisisthroughput.WSapplicationisusedtogeneratebackgroundtraffic.
onceperschedulingwindowforallon-pathdevices,basedon tion [36,40,41,57,62–64,83,85,88],but are mostly used
sharedaggregatedapplicationdemandsandrates.Eachcore in an exclusive deployment. As it moves to multi-tenant
needstoreadonlyonesingleperformancecounterviardpmc. cases,similartransporttechniqueslikeMemChannelwould
The primary overhead introduced by MemChannel comes beneeded.Webelieveourpastexplorationonprogrammable
from POSIX timer timeout interruptions, used to suspend networks[32,35,72,73,81,86,89,90]andin-networkcom-
application execution. Based on our testing,this overhead puting[37,54,56,58–60,67–70]canshedgreatlighton.
amountsto1.7%whentheschedulingwindowissetto100
CongestionControlinHostNetworks.Researchershave
us,enablingfine-grainedcontrolofCXLmemoryaccess. built models to understand congestion happening within a
|     |     |     |     |     |     |     | single host | [23,25,31,80]. |     | HostCC | [23] | locates | and iden- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | ------ | ---- | ------- | --------- |
5.7 Discussion
tifiesbothhost-internalandnetworkfabriccongestion,sig-
CXLecosystemsareundersignificantdevelopment.Webe- nificantlyreducinghostqueueingandpacketlosswhileim-
lievethatMemChannelcanstillbeapplied,butrequiressev- provingthroughputandtaillatency.MidhulVuppalapatietal.
eral changes. First, MemChannel currently advocates the developadomain-by-domaincredit-basedflowcontrolmodel
device-internalloadtoindicatethetrafficconditionofeach tocapturethesubtleinterplaythatleadstolatencyinflation
remoteDIMMandusesend-to-enddelaytoestimatethefab- andhostresourceunderutilization[80].MemChannelcoor-
ric bandwidth capacity. With in-fabric explicit congestion dinatestenantsinaload–storememorypoolingsettingand
notification,ourtransportcanbefurtherimproved.Second, enablesfairsharingofmemorybandwidth.
| MemChannel |     | is evaluated | at rack | scale | ratherthan | at  | clus-        |     |     |     |     |     |     |
| ---------- | --- | ------------ | ------- | ----- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
|            |     |              |         |       |            |     | 7 Conclusion |     |     |     |     |     |     |
terscale.ItwillbeinterestingtoexplorehowMemChannel
operatesinascale-outCXLfabricwithPBR.Third,there- This paper presents MemChannel, a transport layer for
centCXLspecificationintroducestheCXLbundledportto switched CXL memory pooling. MemChannel introduces
supportdeviceswithhigherbandwidthrequirements.Since
|     |     |     |     |     |     |     | the mchannel | abstraction |     | for | end-to-end | fabric | bandwidth |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --- | ---------- | ------ | --------- |
itenableslogicalaggregationofmultipleCXLports,Mem- managementamongcompetingmemorystreamsandenables
Channelshouldaccountfortheintra-bundletrafficcondition application-specifictrafficcontrol.KeytoMemChannelisa
anddevelopanewdevice-loadestimationtechnique. Sender-DrivenFabric-Informedtransportprotocol–inspired
|     |     |     |     |     |     |     | by Core-Stateless |     | Fair | Queueing | (CSFQ)–that |     | admits just |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | -------- | ----------- | --- | ----------- |
6 RelatedWork
|     |     |     |     |     |     |     | enough | CXL requests | to  | each | mchannel | based | on the esti- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ---- | -------- | ----- | ------------ |
CXLMemorySystem.Researchershaveexploredhowto matedCore↔DIMM bandwidthavailability.Oureval-
remote
uationsdemonstratethatMemChannelachieveshighutiliza-
buildCXL-basedremotememorysystemsextensively[34,46,
47,50,55,61,76,82,91].Forexample,Pond[46]analyzesthe tion,performanceisolation,scalability,andmulti-tenancy.
memorystrandingissuewithinAzureandproposesaCXL-
Acknowledgement
basedsmallpooledsystemarchitecture.Melody[50]develops
aframeworktocharacterizeCXLmemoryperformance. We would like to thank the anonymous reviewers and our
Load-Store InterconnectandProgrammable Networks. shepherd,PaoloCosta,fortheircommentsandfeedback.This
Load-storefabrics[3,19,20,38]havegainedgreatinterest workissupportedinpartbyNSFgrantsCNS-2106199,CNS-
recentlytobuildscale-upnetworksforresourcedisaggrega- 2212192,CAREER-2339755,andIntelfacultyawards.

| References |     |     |     |     | [16] The Leo | CXL™ | Memory | Connectivity |     | Platform. |
| ---------- | --- | --- | --- | --- | ------------ | ---- | ------ | ------------ | --- | --------- |
https://www.asteralabs.com/products/cxl-m
| [1] An Introduction |     | to  | Form | Factors for PCI Ex- |     |     |     |     |     |     |
| ------------------- | --- | --- | ---- | ------------------- | --- | --- | --- | --- | --- | --- |
emory-platform/leo-cxl-memory-connectivit
https://pcisig.com/introduction-for
press.
y-platform/,2025.
m-factors-pci-express,2025.
|          |            |                              |     |     | [17] UnifabriXMAX. |     | https://www.unifabrix.com/te |     |     |     |
| -------- | ---------- | ---------------------------- | --- | --- | ------------------ | --- | ---------------------------- | --- | --- | --- |
| [2] Code | Injection. | https://en.wikipedia.org/wik |     |     |                    |     |                              |     |     |     |
chnology,2025.
i/Code_injection,2025.
https://www.xconn-t
|     |     |     |     | https://computee | [18] XConnTitanEvaluationKit. |     |     |     |     |     |
| --- | --- | --- | --- | ---------------- | ----------------------------- | --- | --- | --- | --- | --- |
[3] ComputeExpressLink(CXL).
ech.com/products,2025.
xpresslink.org,2025.
|             |         |      |       |                | [19] The NVIDIA | NVLink. |     | https://www.nvidia.com |     |     |
| ----------- | ------- | ---- | ----- | -------------- | --------------- | ------- | --- | ---------------------- | --- | --- |
| [4] Compute | Express | Link | (CXL) | Specification. |                 |         |     |                        |     |     |
/en-us/data-center/nvlink/,2026.
https://www.computeexpresslink.org/downloa
d-the-specification,2025. [20] UltraAcceleratorLink(UALink). https://www.ua
linkconsortium.org,2026.
| [5] Intel Memory |     | Latency | Checker. | https://www.in |     |     |     |     |     |     |
| ---------------- | --- | ------- | -------- | -------------- | --- | --- | --- | --- | --- | --- |
tel.com/content/www/us/en/developer/articl
[21] VamsiAddanki,MariaApostolaki,ManyaGhobadi,Ste-
es/tool/intelr-memory-latency-checker.html, fanSchmid,andLaurentVanbever. ABM:Activebuffer
2025.
|                               |     |     |                      |     | managementindatacenters. |      |            | InProceedingsoftheACM |     |     |
| ----------------------------- | --- | --- | -------------------- | --- | ------------------------ | ---- | ---------- | --------------------- | --- | --- |
|                               |     |     |                      |     | SIGCOMM                  | 2022 | Conference | (SIGCOMM’22),pages    |     |     |
| [6] IntelliProp’sOmegaFabric. |     |     | https://www.intellip |     |                          |      |            |                       |     |     |
36–52,2022.
rop.com/products-page,2025.
[22] SakshamAgarwal,QizheCai,RachitAgarwal,David
[7] JEDECMemoryModuleReferenceBaseStandard–for
|                          |     |     |     |                    | Shmoys,andAmin               |     | Vahdat. | Harmony: | A      | congestion- |
| ------------------------ | --- | --- | --- | ------------------ | ---------------------------- | --- | ------- | -------- | ------ | ----------- |
| ComputeExpressLink(CXL). |     |     |     | https://www.jedec. |                              |     |         |          |        |             |
|                          |     |     |     |                    | free datacenterarchitecture. |     |         | In 21st  | USENIX | Sympo-      |
org/standards-documents/docs/jesd317a,2025.
siumonNetworkedSystemsDesignandImplementation
|            |        |           |       | https:// | (NSDI’24),pages329–343,2024. |     |     |     |     |     |
| ---------- | ------ | --------- | ----- | -------- | ---------------------------- | --- | --- | --- | --- | --- |
| [8] Micron | Memory | Expansion | Using | CXL.     |                              |     |     |     |     |     |
www.micron.com/products/memory/cxl-memory,
[23] SakshamAgarwal,ArvindKrishnamurthy,andRachit
2025.
|     |     |     |     |     | Agarwal. | Hostcongestioncontrol. |     |     | InProceedingsof |     |
| --- | --- | --- | --- | --- | -------- | ---------------------- | --- | --- | --------------- | --- |
[9] pChase:APointerChasingBenchmark. https://gi theACMSIGCOMM2023Conference,pages275–287,
2023.
thub.com/maleadt/pChase,2025.
|     |     |     |     |     | [24] Mohammad | Alizadeh, |     | Albert Greenberg, |     | David A |
| --- | --- | --- | --- | --- | ------------- | --------- | --- | ----------------- | --- | ------- |
[10] PCIExpress(PeripheralComponentInterconnectEx-
press). https://pcisig.com,2025. Maltz,JitendraPadhye,ParveenPatel,BalajiPrabhakar,
|     |     |     |     |     | SudiptaSengupta,andMurariSridharan. |     |     |     |     | Datacenter |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ---------- |
[11] Samsung CXL Memory Module - Box (CMM-B). Proceedings of the ACM SIGCOMM
|     |     |     |     |     | tcp (dctcp). | In  |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
https://semiconductor.samsung.com/news-eve 2010Conference,pages63–74,2010.
nts/tech-blog/cxl-memory-module-box-cmm-b/,
|     |     |     |     |     | [25] Seunghyun | An, | Joontaek | Oh, and | Ming Liu. | Server |
| --- | --- | --- | --- | --- | -------------- | --- | -------- | ------- | --------- | ------ |
2025.
|     |     |     |     |     | ChipletNetworking. |     | InProceedingsofthe24thACM |     |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | ------------------------- | --- | --- | --- |
[12] SMART CXL Memory Modules. https: WorkshoponHotTopicsinNetworks(HotNets’25),page
| //www.smartm.com/product/list/cxl-memor |     |     |     |     | 289–299,2025. |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
y?utm_source=CXL&utm_medium=Website&utm_ter
|     |     |     |     |     | [26] NikolasAskitisandRanjanSinha. |     |     |     | HAT-trie:acache- |     |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ---------------- | --- |
m=CXL-Website-TR&utm_content=CXL-Website-L
ink&utm_campaign=CXL-Website,2025. conscioustrie-baseddatastructureforstrings. InPro-
|     |     |     |     |     | ceedings | of the | thirtieth | Australasian | conference | on  |
| --- | --- | --- | --- | --- | -------- | ------ | --------- | ------------ | ---------- | --- |
[13] SPEC CPU 2017. https://www.spec.org/cpu Computerscience-Volume62,pages97–105,2007.
2017,2025.
[27] ScottBeamer,KrsteAsanovic´,andDavidPatterson.The
[14] TheFalconC5022. https://www.h3platform.com/ GAPBenchmarkSuite,2017.
product-detail/overview/35,2025.
[28] ChristianBienia,SanjeevKumar,JaswinderPalSingh,
[15] TheIntel®Agilex™7FPGAI-SeriesDevelopmentKit. andKaiLi. Theparsecbenchmarksuite:Characteriza-
https://www.intel.com/content/www/us/en/pr tionandarchitecturalimplications. InProceedingsof
oducts/details/fpga/development-kits/agil the17thinternationalconferenceonParallelarchitec-
ex/i-series/dev-agi027.html,2025. turesandcompilationtechniques,pages72–81,2008.

[29] PatBosshart,GlenGibb,Hun-SeokKim,GeorgeVargh- [38] WentaoHou,JieZhang,ZekeWang,andMingLiu. Un-
ese,NickMcKeown,MartinIzzard,FernandoMujica, derstandingRoutablePCIePerformanceforCompos-
andMarkHorowitz. Forwardingmetamorphosis:fast ableInfrastructures.In21stUSENIXSymposiumonNet-
programmablematch-actionprocessinginhardwarefor workedSystemsDesignandImplementation(NSDI’24),
| SDN. | In Proceedings |     | of the | ACM | SIGCOMM | 2013 | 2024. |     |     |     |     |     |
| ---- | -------------- | --- | ------ | --- | ------- | ---- | ----- | --- | --- | --- | --- | --- |
ConferenceonSIGCOMM,page99–110,2013.
|                        |                                     |     |                           |              |     |         | [39] Shuihai                          | Hu, Wei                                    | Bai, | Gaoxiong | Zeng, Zilong | Wang, |
| ---------------------- | ----------------------------------- | --- | ------------------------- | ------------ | --- | ------- | ------------------------------------- | ------------------------------------------ | ---- | -------- | ------------ | ----- |
| [30] Lawrence          | S Brakmo,Sean                       |     | W                         | O’malley,and |     | Larry L |                                       |                                            |      |          |              |       |
|                        |                                     |     |                           |              |     |         | BaochenQiao,KaiChen,KunTan,andYiWang. |                                            |      |          |              | Ae-   |
| Peterson.              | TCPVegas:Newtechniquesforcongestion |     |                           |              |     |         |                                       |                                            |      |          |              |       |
|                        |                                     |     |                           |              |     |         | olus:                                 | Abuildingblockforproactivetransportindata- |      |          |              |       |
| detectionandavoidance. |                                     |     | InProceedingsoftheconfer- |              |     |         |                                       |                                            |      |          |              |       |
|                        |                                     |     |                           |              |     |         | centers.                              | InProceedingsoftheAnnualconferenceofthe    |      |          |              |       |
enceonCommunicationsarchitectures,protocolsand
ACMSpecialInterestGrouponDataCommunicationon
applications,pages24–35,1994.
theapplications,technologies,architectures,andpro-
|     |     |     |     |     |     |     | tocols | for computer | communication |     | (SIGCOMM’20), |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | ------------- | --- | ------------- | --- |
[31] QizheCai,ShubhamChaudhary,MidhulVuppalapati,
JaehyunHwang,andRachitAgarwal. Understanding pages422–434,2020.
|              |       |            |     | Proceedings |     | of the |                            |     |     |                        |     |     |
| ------------ | ----- | ---------- | --- | ----------- | --- | ------ | -------------------------- | --- | --- | ---------------------- | --- | --- |
| host network | stack | overheads. |     | In          |     |        |                            |     |     |                        |     |     |
|              |       |            |     |             |     |        | [40] ShengJiangandMingLiu. |     |     | BuildinganElasticBlock |     |     |
2021ACMSIGCOMM2021Conference,pages65–77,
| 2021. |     |     |     |     |     |     | Storage | over EBOFs | Using | Shadow | Views. | In 22nd |
| ----- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----- | ------ | ------ | ------- |
USENIXSymposiumonNetworkedSystemsDesignand
[32] XuzhengChen,JieZhang,TingFu,YifanShen,ShuMa, Implementation(NSDI’25),pages1137–1153,2025.
| Kun Qian,Lingjun |     | Zhu,Chao |     | Shi,Yin | Zhang,Ming |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Liu,etal. Demystifyingdatapathacceleratorenhanced [41] YuyuanKangandMingLiu. UnderstandingandProfil-
off-path smartnic. In 2024 IEEE 32nd International ingNVMe-over-TCPUsingntprof. In22ndUSENIX
ConferenceonNetworkProtocols(ICNP’24),pages1– SymposiumonNetworkedSystemsDesignandImple-
| 12,2024. |     |     |     |     |     |     | mentation(NSDI’25),pages1117–1136,2025. |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
[33] BrianFCooper,AdamSilberstein,ErwinTam,Raghu
[42] HTKung,TrevorBlackwell,andAlanChapman.Credit-
| Ramakrishnan,andRussellSears. |     |     |     | Benchmarkingcloud     |     |     |       |              |     |               |        |        |
| ----------------------------- | --- | --- | --- | --------------------- | --- | --- | ----- | ------------ | --- | ------------- | ------ | ------ |
|                               |     |     |     |                       |     |     | based | flow control | for | ATM networks: | Credit | update |
| servingsystemswithYCSB.       |     |     |     | InProceedingsofthe1st |     |     |       |              |     |               |        |        |
protocol,adaptivecreditallocationandstatisticalmul-
ACMsymposiumonCloudcomputing,pages143–154,
|     |     |     |     |     |     |     | tiplexing. | In Proceedings |     | of the | conference | on Com- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------ | ---------- | ------- |
2010.
municationsarchitectures,protocolsandapplications,
| [34] DonghyunGouk,SangwonLee,MiryeongKwon,and |                |                                 |      |              |     |     | 1994.                       |     |     |                         |     |     |
| --------------------------------------------- | -------------- | ------------------------------- | ---- | ------------ | --- | --- | --------------------------- | --- | --- | ----------------------- | --- | --- |
| MyoungsooJung.                                |                | Directaccess,{High-Performance} |      |              |     |     |                             |     |     |                         |     |     |
|                                               |                |                                 |      |              |     |     | [43] NTKungandRobertMorris. |     |     | Credit-basedflowcontrol |     |     |
| memory                                        | disaggregation |                                 | with | {DirectCXL}. |     | In  |                             |     |     |                         |     |     |
2022USENIXAnnualTechnicalConference(USENIX foratmnetworks. IEEEnetwork,9(2):40–48,1995.
ATC’22),pages287–294,2022.
|            |             |      |        |      |          |      | [44] Nhat               | Minh Lê, | Antoniu | Pop,                     | Albert | Cohen, and |
| ---------- | ----------- | ---- | ------ | ---- | -------- | ---- | ----------------------- | -------- | ------- | ------------------------ | ------ | ---------- |
| [35] Zerui | Guo, Jiaxin | Lin, | Yuebin | Bai, | Daehyeok | Kim, |                         |          |         |                          |        |            |
|            |             |      |        |      |          |      | FrancescoZappaNardelli. |          |         | CorrectandEfficientWork- |        |            |
Michael Swift, Aditya Akella, and Ming Liu. Log- StealingforWeakMemoryModels. InProceedingsof
NIC:AHigh-LevelPerformanceModelforSmartNICs.
the18thACMSIGPLANSymposiumonPrinciplesand
InProceedingsofthe56thAnnualIEEE/ACMInterna-
PracticeofParallelProgramming,2013.
tionalSymposiumonMicroarchitecture(MICRO’23),
page916–929,2023.
|     |     |     |     |     |     |     | [45] PhilipLevis,KunLin,andAmyTai. |     |     |     | ACaseAgainst |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ------------ | --- |
CXLMemoryPooling.InProceedingsofthe22ndACM
[36] ZeruiGuo,HuaZhang,ChenxingyuZhao,YuebinBai,
WorkshoponHotTopicsinNetworks(HotNets’23),page
| MichaelSwift,andMingLiu. |     |     |     | LEED: | ALow-Power, |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
18–24,2023.
FastPersistentKey-ValueStoreonSmartNICJBOFs.In
ProceedingsoftheACMSIGCOMM2023Conference
[46] HuaichengLi,DanielS.Berger,LisaHsu,DanielErnst,
(SIGCOMM’23),page1012–1027,2023.
|     |     |     |     |     |     |     | Pantea | Zardoshti, | Stanko | Novakovic, | Monish | Shah, |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------ | ---------- | ------ | ----- |
[37] YongchaoHe,WenfeiWu,YanfangLe,MingLiu,and SamirRajadnya,ScottLee,IshwarAgarwal,MarkD.
ChonLam Lao. A Generic Service to Provide In- Hill,MarcusFontoura,andRicardoBianchini. Pond:
NetworkAggregationforKey-ValueStreams. InPro- CXL-BasedMemoryPoolingSystemsforCloudPlat-
ceedingsofthe28thACMInternationalConferenceon forms. InProceedingsofthe28thACMInternational
ArchitecturalSupportforProgrammingLanguagesand ConferenceonArchitecturalSupportforProgramming
OperatingSystems(ASPLOS’23),Volume2,page33–47, LanguagesandOperatingSystems(ASPLOS’23),Vol-
| 2023. |     |     |     |     |     |     | ume2,page574–587,2023. |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |

[47] XiaoLi,ZeruiGuo,YuebinBai,MehashKetkar,Hugh [57] Ming Liu, Arvind Krishnamurthy, Harsha V. Mad-
Willkinson,andMingLiu. UnderstandingandProfiling hyastha,Rishi Bhardwaj,Karan Gupta,Chinmay Ka-
CXL.mem Using PathFinder. In Proceedings of the mat,HuapengYuan,AdityaJaltade,RogerLiao,Pavan
ACM SIGCOMM 2025 Conference (SIGCOMM’25), Konka,andAnoopJawahar. Fine-GrainedReplicated
| 2025. |     |     |     |     |     |     | StateMachinesforaClusterStorageSystem. |     |     |     |     |     | In17th |
| ----- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | ------ |
USENIXSymposiumonNetworkedSystemsDesignand
| [48] Yuliang | Li, | Rui Miao, | Hongqiang |     | Harry Liu, | Yan |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Implementation(NSDI’20),pages305–323,2020.
| Zhuang,                                 | Fei | Feng, | Lingbo Tang, | Zheng | Cao, | Ming  |     |     |     |     |     |     |     |
| --------------------------------------- | --- | ----- | ------------ | ----- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Zhang,FrankKelly,MohammadAlizadeh,etal. |     |       |              |       |      | HPCC: |     |     |     |     |     |     |     |
[58] MingLiu,LiangLuo,JacobNelson,LuisCeze,Arvind
Highprecisioncongestioncontrol. InProceedingsof Krishnamurthy, and Kishore Atreya. IncBricks: To-
theACMspecialinterestgroupondatacommunication
|     |     |     |     |     |     |     | ward | In-Network | Computation |     | with | an In-Network |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ----------- | --- | ---- | ------------- | --- |
(SIGCOMM’19),pages44–58.2019.
|     |     |     |     |     |     |     | Cache. | InProceedingsoftheTwenty-SecondInterna- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------------------------------- | --- | --- | --- | --- | --- |
tionalConferenceonArchitecturalSupportforProgram-
[49] HyeontaekLim,DongsuHan,DavidG.Andersen,and
mingLanguagesandOperatingSystems(ASPLOS’17),
| MichaelKaminsky. |     | MICA:Aholisticapproachtofast |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
page795–809,2017.
| In-MemoryKey-Valuestorage. |     |     |     | In11thUSENIXSympo- |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
siumonNetworkedSystemsDesignandImplementation
|     |     |     |     |     |     |     | [59] Ming | Liu, Simon |     | Peter, Arvind | Krishnamurthy, |     | and |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------------- | -------------- | --- | --- |
(NSDI14),2014.
|             |       |         |         |       |              |     | Phitchaya | Mangpo        |             | Phothilimthana. |                      | E3: | Energy- |
| ----------- | ----- | ------- | ------- | ----- | ------------ | --- | --------- | ------------- | ----------- | --------------- | -------------------- | --- | ------- |
|             |       |         |         |       |              |     | Efficient | Microservices |             | on              | SmartNIC-Accelerated |     |         |
| [50] Jinshu | Liu,  | Hamid   | Hadian, | Yuyue | Wang, Daniel | S   |           |               |             |                 |                      |     |         |
|             |       |         |         |       |              |     | Servers.  | In            | 2019 USENIX | Annual          | Technical            |     | Confer- |
| Berger,     | Marie | Nguyen, | Xun     | Jian, | Sam H Noh,   | and |           |               |             |                 |                      |     |         |
ence(USENIXATC’19),pages363–378,2019.
| HuaichengLi.                   |     | Systematiccxlmemorycharacterization |     |                    |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | ----------------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| andperformanceanalysisatscale. |     |                                     |     | InProceedingsofthe |     |     |     |     |     |     |     |     |     |
[60] LiangLuo,MingLiu,JacobNelson,LuisCeze,Amar
| 30th    | ACM | International | Conference |     | on Architectural |     |                                     |     |     |     |     |            |     |
| ------- | --- | ------------- | ---------- | --- | ---------------- | --- | ----------------------------------- | --- | --- | --- | --- | ---------- | --- |
|         |     |               |            |     |                  |     | Phanishayee,andArvindKrishnamurthy. |     |     |     |     | Motivating |     |
| Support | for | Programming   | Languages  |     | and Operating    |     |                                     |     |     |     |     |            |     |
Systems,Volume2,pages1203–1217,2025. in-networkaggregationfordistributeddeepneuralnet-
|     |     |     |     |     |     |     | worktraining. |     | InWorkshoponApproximateComputing |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------------------------- | --- | --- | --- | --- |
AcrosstheStack,2017.
| [51] Jinshu | Liu,  | Hamid   | Hadian, | Yuyue | Wang, Daniel | S   |     |     |     |     |     |     |     |
| ----------- | ----- | ------- | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Berger,     | Marie | Nguyen, | Xun     | Jian, | Sam H Noh,   | and |     |     |     |     |     |     |     |
HuaichengLi. Systematiccxlmemorycharacterization [61] Hasan Al Maruf,Hao Wang,Abhishek Dhanotia,Jo-
|                                |     |     |     |                    |     |     | hannes | Weiner, | Niket | Agarwal, | Pallab | Bhattacharya, |     |
| ------------------------------ | --- | --- | --- | ------------------ | --- | --- | ------ | ------- | ----- | -------- | ------ | ------------- | --- |
| andperformanceanalysisatscale. |     |     |     | InProceedingsofthe |     |     |        |         |       |          |        |               |     |
30th ACM International Conference on Architectural ChrisPetersen,MosharafChowdhury,ShobhitKanaujia,
|         |     |             |           |     |               |     | andPrakashChauhan.               |     |     | TPP: | Transparent | Page          | Place- |
| ------- | --- | ----------- | --------- | --- | ------------- | --- | -------------------------------- | --- | --- | ---- | ----------- | ------------- | ------ |
| Support | for | Programming | Languages |     | and Operating |     |                                  |     |     |      |             |               |        |
|         |     |             |           |     |               |     | mentforCXL-EnabledTiered-Memory. |     |     |      |             | InProceedings |        |
Systems,Volume2,pages1203–1217,2025.
ofthe28thACMInternationalConferenceonArchitec-
[52] JinshuLiu,HamidHadian,HanchenXu,andHuaicheng turalSupportforProgrammingLanguagesandOper-
| Li. | TieredMemoryManagementBeyondHotness. |     |     |     |     | In  |     |     |     |     |     |     |     |
| --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
atingSystems(ASPLOS’23),Volume3,page742–755,
| 19thUSENIXSymposiumonOperatingSystemsDesign |     |     |     |     |     |     | 2023. |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
andImplementation(OSDI’25),pages731–747,2025.
|     |     |     |     |     |     |     | [62] Jaehong | Min, | Ming | Liu, Tapan | Chugh, | Chenxingyu |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---- | ---------- | ------ | ---------- | --- |
[53] JinshuLiu,HamidHadian,HanchenXu,andHuaicheng
Zhao,AndrewWei,InHwanDoh,andArvindKrishna-
Li. Tiered memory management beyond hotness. In murthy. Gimbal:enablingmulti-tenantstoragedisaggre-
19thUSENIXSymposiumonOperatingSystemsDesign
|     |     |     |     |     |     |     | gationonSmartNICJBOFs. |     |     | InProceedingsofthe2021 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ---------------------- | --- | --- | --- |
andImplementation(OSDI25),pages731–747,2025.
|                    |      |          |                              |         |       |      | ACM               | SIGCOMM | 2021 | Conference |     | (SIGCOMM’21), |     |
| ------------------ | ---- | -------- | ---------------------------- | ------- | ----- | ---- | ----------------- | ------- | ---- | ---------- | --- | ------------- | --- |
|                    |      | Building | Distributed                  | Systems | Using | Pro- | page106–122,2021. |         |      |            |     |               |     |
| [54] Ming          | Liu. |          |                              |         |       |      |                   |         |      |            |     |               |     |
| grammableNetworks. |      |          | UniversityofWashington,2020. |         |       |      |                   |         |      |            |     |               |     |
[63] JaehongMin,ChenxingyuZhao,MingLiu,andArvind
[55] MingLiu.Fabric-CentricComputing.InProceedingsof Krishnamurthy. eZNS: An elastic zoned namespace
the19thWorkshoponHotTopicsinOperatingSystems for commodity ZNS SSDs. In 17th USENIX Sympo-
siumonOperatingSystemsDesignandImplementation
(HotOS’23),page118–126,2023.
(OSDI’23),pages461–477,2023.
| [56] Ming | Liu,Tianyi | Cui,Henry |     | Schuh,ArvindKrishna- |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
murthy,SimonPeter,andKaranGupta. Offloadingdis- [64] JaehongMin,ChenxingyuZhao,MingLiu,andArvind
tributed applications onto smartNICs using iPipe. In Krishnamurthy. eZNS:ElasticZonedNamespacefor
ProceedingsoftheACMSpecialInterestGrouponData EnhancedPerformanceIsolationandDeviceUtilization.
Communication(SIGCOMM’19),page318–333,2019. ACMTrans.Storage,20(3),June2024.

[65] Radhika Mittal, Vinh The Lam, Nandita Dukkipati, murthy,andAnirudhSivaraman. ProgrammableCalen-
Emily Blem, Hassan Wassel, Monia Ghobadi, Amin darQueuesforHigh-speedPacketScheduling. In17th
Vahdat, Yaogong Wang, David Wetherall, and David USENIXSymposiumonNetworkedSystemsDesignand
Zats. TIMELY:RTT-basedCongestionControlforthe Implementation(NSDI’20),pages685–699,2020.
| Datacenter. |     | InProceedingsofthe2015ACMConfer- |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[74] KevinSong,JiachengYang,ZixuanWang,JishenZhao,
enceonSpecialInterestGrouponDataCommunication
|     |     |     |     |     |     |     | SihangLiu,andGennadyPekhimenko. |     |     |     |     | HybridTier:an |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ------------- | --- |
(SIGCOMM’15),page537–550,2015.
AdaptiveandLightweightCXL-MemoryTieringSys-
[66] NevineNassif,AshleyO.Munch,CarletonL.Molnar, tem. In Proceedings of the 30th ACM International
GeraldPasdast,SitaramanV.Lyer,ZibingYang,Oscar ConferenceonArchitecturalSupportforProgramming
Mendoza, Mark Huddart, Srikrishnan Venkataraman, LanguagesandOperatingSystems,Volume3,pages112–
| Sireesha | Kandula, |     | Rafi Marom, | Alexandra |     | M. Kern, | 128,2025. |     |     |     |     |     |     |
| -------- | -------- | --- | ----------- | --------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- |
BillBowhill,DavidR.Mulvihill,SrikanthNimmagadda,
[75] IonStoica,ScottShenker,andHuiZhang.Core-stateless
VarmaKalidindi,JonathanKrause,MohammadM.Haq,
fairqueueing:Achievingapproximatelyfairbandwidth
| Roopali                                       | Sharma,and |               | Kevin       | Duda. | Sapphire | Rapids: |                                 |            |            |     |                 |               |     |
| --------------------------------------------- | ---------- | ------------- | ----------- | ----- | -------- | ------- | ------------------------------- | ---------- | ---------- | --- | --------------- | ------------- | --- |
|                                               |            |               |             |       |          |         | allocationsinhighspeednetworks. |            |            |     | InProceedingsof |               |     |
| TheNext-GenerationIntelXeonScalableProcessor. |            |               |             |       |          | In      |                                 |            |            |     |                 |               |     |
|                                               |            |               |             |       |          |         | the ACM                         | SIGCOMM’98 | conference |     | on              | Applications, |     |
| 2022                                          | IEEE       | International | Solid-State |       | Circuits | Confer- |                                 |            |            |     |                 |               |     |
technologies,architectures,andprotocolsforcomputer
ence(ISSCC’22),volume65,pages44–46,2022.
communication,pages118–130,1998.
[67] PhitchayaMangpoPhothilimthana,MingLiu,Antoine
|     |     |     |     |     |     |     | [76] Yan | Sun, Yifan Yuan, | Zeduo | Yu, | Reese | Kuper, | Chi- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | ----- | --- | ----- | ------ | ---- |
Kaufmann,SimonPeter,RastislavBodik,andThomas
Anderson. Floem: A Programming System for NIC- hunSong,JinghanHuang,HouxiangJi,SiddharthAgar-
wal,JiaqiLou,IpoomJeong,RenWang,JungHoAhn,
| Accelerated |     | Network      | Applications. |     | In 13th | USENIX     |                          |              |           |     |                 |     |         |
| ----------- | --- | ------------ | ------------- | --- | ------- | ---------- | ------------------------ | ------------ | --------- | --- | --------------- | --- | ------- |
|             |     |              |               |     |         |            | TianyinXu,andNamSungKim. |              |           |     | DemystifyingCXL |     |         |
| Symposium   |     | on Operating | Systems       |     | Design  | and Imple- |                          |              |           |     |                 |     |         |
|             |     |              |               |     |         |            | Memory                   | with Genuine | CXL-Ready |     | Systems         |     | and De- |
mentation(OSDI’18),pages663–679,2018.
|     |     |     |     |     |     |     | vices. | InProceedingsofthe56thAnnualIEEE/ACM |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------------------------------ | --- | --- | --- | --- | --- |
[68] Yiming Qiu, Qiao Kang, Ming Liu, and Ang Chen. International Symposium on Microarchitecture (MI-
Clara:PerformanceClarityforSmartNICOffloading.In CRO’23),page105–121,2023.
Proceedingsofthe19thACMWorkshoponHotTopics
|     |     |     |     |     |     |     | [77] Stephen | Tu, Wenting | Zheng, | Eddie | Kohler, |     | Barbara |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------ | ----- | ------- | --- | ------- |
inNetworks(HotNets’20),page16–22,2020.
|     |     |     |     |     |     |     | Liskov,and | Samuel | Madden. | Speedy |     | transactions | in  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------- | ------ | --- | ------------ | --- |
[69] YimingQiu,JiarongXing,Kuo-FengHsu,QiaoKang, multicorein-memorydatabases. InProceedingsofthe
Ming Liu, Srinivas Narayana, and Ang Chen. Auto- Twenty-FourthACMSymposiumonOperatingSystems
matedSmartNICOffloadingInsightsforNetworkFunc- Principles,pages18–32,2013.
| tions. | InProceedingsoftheACMSIGOPS28thSympo- |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
siumonOperatingSystemsPrinciples(SOSP’21),page [78] MidhulVuppalapatiandRachitAgarwal. TieredMem-
|     |     |     |     |     |     |     | oryManagement:AccessLatencyistheKey! |     |     |     |     |     | InPro- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | ------ |
772–787,2021.
ceedingsoftheACMSIGOPS30thSymposiumonOp-
[70] HenryN.Schuh,WeihaoLiang,MingLiu,JacobNel- eratingSystemsPrinciples,pages79–94,2024.
| son, | and Arvind |     | Krishnamurthy. |     | Xenic:        | SmartNIC- |                                         |     |     |     |     |            |     |
| ---- | ---------- | --- | -------------- | --- | ------------- | --------- | --------------------------------------- | --- | --- | --- | --- | ---------- | --- |
|      |            |     |                |     | InProceedings |           | [79] MidhulVuppalapatiandRachitAgarwal. |     |     |     |     | TieredMem- |     |
AcceleratedDistributedTransactions.
|        |     |        |                |     |     |           | oryManagement:AccessLatencyistheKey! |     |     |     |     |     | InPro- |
| ------ | --- | ------ | -------------- | --- | --- | --------- | ------------------------------------ | --- | --- | --- | --- | --- | ------ |
| of the | ACM | SIGOPS | 28th Symposium |     | on  | Operating |                                      |     |     |     |     |     |        |
ceedingsoftheACMSIGOPS30thSymposiumonOp-
SystemsPrinciples(SOSP’21),page740–755,2021.
eratingSystemsPrinciples,pages79–94,2024.
| [71] Debendra |     | Das | Sharma, Robert |     | Blankenship, | and |     |     |     |     |     |     |     |
| ------------- | --- | --- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[80] MidhulVuppalapati,SakshamAgarwal,HenrySchuh,
| Daniel | S   | Berger. | An introduction |     | to  | the com- |     |     |     |     |     |     |     |
| ------ | --- | ------- | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
BarisKasikci,ArvindKrishnamurthy,andRachitAgar-
| pute | express | link | (cxl) interconnect. |     | arXiv | preprint |     |     |     |     |     |     |     |
| ---- | ------- | ---- | ------------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
arXiv:2306.11227,2023. wal. Understandingthehostnetwork. InProceedingsof
theACMSIGCOMM2024Conference,pages581–594,
| [72] Naveen               | Kr. | Sharma, | Ming Liu,                 | Kishore            |     | Atreya, and | 2024.         |       |          |     |          |      |     |
| ------------------------- | --- | ------- | ------------------------- | ------------------ | --- | ----------- | ------------- | ----- | -------- | --- | -------- | ---- | --- |
| ArvindKrishnamurthy.      |     |         | ApproximatingFairQueueing |                    |     |             |               |       |          |     |          |      |     |
|                           |     |         |                           |                    |     |             | [81] Chendong | Wang, | Joontaek | Oh, | and Ming | Liu. | Co- |
| onReconfigurableSwitches. |     |         |                           | In15thUSENIXSympo- |     |             |               |       |          |     |          |      |     |
DesigningtrafficcontrolwithNVMe-oFfordisaggre-
siumonNetworkedSystemsDesignandImplementation
|     |     |     |     |     |     |     | gated | storage: A | comparative | study | of  | switched | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ----------- | ----- | --- | -------- | --- |
(NSDI’18),pages1–16,2018.
|     |     |     |     |     |     |     | switchlessSANarchitectures. |     |     | In23rdUSENIXSympo- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ------------------ | --- | --- | --- |
[73] Naveen Kr. Sharma, Chenxingyu Zhao, Ming Liu, siumonNetworkedSystemsDesignandImplementation
PraveinGKannan,ChanghoonKim,ArvindKrishna- (NSDI’26),pages2651–2669,2026.

[82] Lingfeng Xiang, Zhen Lin, Weishu Deng, Hui Lu, Languages and Operating Systems, Volume 2, pages
| Jia Rao, | Yifan Yuan, | and | Ren Wang. | Nomad:{Non- |     | 1727–1748,2026. |     |     |     |
| -------- | ----------- | --- | --------- | ----------- | --- | --------------- | --- | --- | --- |
Exclusive}MemoryTieringviaTransactionalPageMi-
|          |         |        |           |     |           | [91] Yuhong | Zhong, Daniel | S. Berger, Carl | Waldspurger, |
| -------- | ------- | ------ | --------- | --- | --------- | ----------- | ------------- | --------------- | ------------ |
| gration. | In 18th | USENIX | Symposium | on  | Operating |             |               |                 |              |
SystemsDesignandImplementation(OSDI’24),pages RyanWee,IshwarAgarwal,RajatAgarwal,FrankHady,
|     |     |     |     |     |     | Karthik | Kumar,Mark | D. Hill,Mosharaf | Chowdhury, |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | ---------------- | ---------- |
19–35,2024.
|     |     |     |     |     |     | andAsafCidon. | ManagingMemoryTierswithCXL |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | -------------------------- | --- | --- |
[83] XinchengXie,WentaoHou,ZeruiGuo,andMingLiu. inVirtualizedEnvironments. In18thUSENIXSympo-
Building massive MIMO baseband processing on a siumonOperatingSystemsDesignandImplementation
Single-Nodesupercomputer. In22ndUSENIXSympo- (OSDI’24),pages37–56,2024.
siumonNetworkedSystemsDesignandImplementation
(NSDI’25),pages1221–1242,2025. [92] YiboZhu,HaggaiEran,DanielFirestone,Chuanxiong
Guo,MarinaLipshteyn,YehonatanLiron,JitendraPad-
[84] ZhuolongYu,JingfengWu,VladimirBraverman,Ion hye,ShacharRaindel,MohamadHajYahia,andMing
Stoica,andXin Jin. Twentyyearsafter: Hierarchical Zhang. Congestion Control for Large-Scale RDMA
{Core-Stateless}fairqueueing.In18thUSENIXSympo- Deployments. InProceedingsofthe2015ACMConfer-
siumonNetworkedSystemsDesignandImplementation enceonSpecialInterestGrouponDataCommunication
| (NSDI’21),pages29–45,2021.                 |     |     |     |     |        | (SIGCOMM’15),page523–536,2015. |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ------ | ------------------------------ | --- | --- | --- |
| [85] HuaZhang,XiaoLi,YuebinBai,andMingLiu. |     |     |     |     | Under- |                                |     |     |     |
standingandOptimizingDatabasePushdownonDis-
| aggregatedStorage. |     | In  | Proceedings | ofthe | 31stACM |     |     |     |     |
| ------------------ | --- | --- | ----------- | ----- | ------- | --- | --- | --- | --- |
InternationalConferenceonArchitecturalSupportfor
ProgrammingLanguagesandOperatingSystems,Vol-
ume2,pages2141–2158,2026.
[86] JieZhang,HongjingHuang,XuzhengChen,XiangLi,
| Jieru Zhao,Ming    |         | Liu,andZeke                 |          | Wang. RpcNIC: | En-      |     |     |     |     |
| ------------------ | ------- | --------------------------- | -------- | ------------- | -------- | --- | --- | --- | --- |
| abling Efficient   |         | Datacenter                  | RPC      | Offloading    | on PCIe- |     |     |     |     |
| attachedSmartNICs. |         | In2025IEEEInternationalSym- |          |               |          |     |     |     |     |
| posium             | on High | Performance                 | Computer | Architecture  |          |     |     |     |     |
(HPCA’25),pages1379–1394,2025.
[87] MingxingZhang,TengMa,JinqiHua,ZhengLiu,Kang
| Chen, Ning | Ding,                                | Fan | Du, Jinlei | Jiang, Tao | Ma, and |     |     |     |     |
| ---------- | ------------------------------------ | --- | ---------- | ---------- | ------- | --- | --- | --- | --- |
| YongweiWu. | Partialfailureresilientmemorymanage- |     |            |            |         |     |     |     |     |
mentsystemfor(cxl-based)distributedsharedmemory.
| In Proceedings | of  | the 29th | Symposium | on  | Operating |     |     |     |     |
| -------------- | --- | -------- | --------- | --- | --------- | --- | --- | --- | --- |
SystemsPrinciples(SOSP’23),pages658–674,2023.
[88] ChenxingyuZhao,TapanChugh,JaehongMin,Ming
| Liu,andArvindKrishnamurthy. |     |     | Dremel:AdaptiveCon- |     |     |     |     |     |     |
| --------------------------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Proc.ACM
figurationTuningofRocksDBKV-Store.
Meas.Anal.Comput.Syst.,6(2),June2022.
[89] ChenxingyuZhao,JaehongMin,MingLiu,andArvind
| Krishnamurthy.           |     | White-Boxing |                    | RDMA with | Packet- |     |     |     |     |
| ------------------------ | --- | ------------ | ------------------ | --------- | ------- | --- | --- | --- | --- |
| GranularSoftwareControl. |     |              | In22ndUSENIXSympo- |           |         |     |     |     |     |
siumonNetworkedSystemsDesignandImplementation
(NSDI’25),pages427–449,2025.
| [90] Chenxingyu | Zhao, | Hongtao | Zhang, | Jaehong | Min, |     |     |     |     |
| --------------- | ----- | ------- | ------ | ------- | ---- | --- | --- | --- | --- |
ShengkaiLin,WeiZhang,KaiyuanZhang,MingLiu,
| andArvindKrishnamurthy. |     |     | SG-IOV:Socket-Granular |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
I/OVirtualizationforSmartNIC-BasedContainerNet-
| works. | InProceedingsofthe31stACMInternational |     |     |     |     |     |     |     |     |
| ------ | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ConferenceonArchitecturalSupportforProgramming

Figure13:Channelbandwidthwhenaddingfourchannelscom-
paredbetweenwithandwithoutMemChannelcases.
A Appendix
A.1 MemChannelAdaptiveness
Wefurtherexaminehowthechannelbandwidthadjustswhen
addingmoremchannelsatruntime.Wefirstrunasynthetic
workloadwithandwithoutMemChannel.Then,at2.5s,7.5s,
12.5s,and17.5s,wegraduallyaddonemoresyntheticwork-
loadandmeasuretheaveragechannelbandwidtheveryhalf
second.Whenamchannelisaddedtothesystem,MemChan-
nelupdatesthefairsharerateandregulatestheremotemem-
oryaccessrate(Figure13),causingabandwidthdropat3s,
8s,13s,and18s.Subsequently,thetransportalgorithmrecal-
culatesthehardwareprocessingcapacitybasedoncongestion
signals,increasingtheaveragebandwidth.
---- END DOCUMENT ----
