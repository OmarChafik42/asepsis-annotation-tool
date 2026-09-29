Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Removing Population Size, World Cities Leave on
Land a Footprint of Wealth
Victor Vignolles1 and R´emi Lemoy1*
1*Geography Department, University of Rouen, IDEES Laboratory,
UMR 6266 CNRS, Rue Lavoisier, Mont-Saint-Aignan, 76821, France.
*Corresponding author(s). E-mail(s): remi.lemoy@univ-rouen.fr;
Contributing authors: victorvignolles@gmail.com;
Abstract
Urban expansion builds on precious arable land [1, 2], affecting ecosystems and
health [3–7], despite worldwide measures to alleviate its impacts, in small and
large cities. Nonetheless, the link between urban extent and population size is
still unclear [8, 9]. Here we uncover a scaling law governing built-up land in
1800+ global urban areas. We observe that world cities have homothetic (or
isometric) radial land use profiles, and that built-up footprint is proportional
to total population. This spatial scaling law is important for the understanding
and the definition of urban areas, to help build a science of cities and make
themmoresustainable.Itimpliesthatsmallandlargecitieshavesimilarinternal
structures, and that built-up area per capita is constant across city sizes. The
remaining variations are very strongly correlated to wealth measured by gross
domestic product per capita, suggesting a pick between economic development
and sustainabiliy.
Keywords:landuse,urbanscalinglaws,radialanalysis,globalcities
Human societies are increasingly urban at the global scale. Urbanization is associated
with economic, scientific, and societal progress [10] for humanity, and also important
consequences on the environment, such as climate change or losses of biodiversity
and arable land, which are linked to urban land use [1–7]. Cities participate in the
biodiversity crisis in particular through animal habitat fragmentation. Indeed, urban
forms follow fractal patterns [11], which means that they affect vast areas, although
urban land represents only around 1.47% of global land area in 2015 (1.05% in 1990)
1
6202
guA
91
]hp-cos.scisyhp[
1v29781.8062:viXra

[12]. Climate change is also linked to cities as they concentrate human activities and
associated pollutions, for instance the emissions of greenhouse gases. These affect
deeplytheglobalclimate,whiletheurbanheatislandeffect,linkedtourbanlanduse,
changes the local intra-urban climate [13]. Actually, soil sealing is an issue probably
first of all because land which is taken by urbanization is usually rich and easily
accessible arable land [2]. Its loss affects agricultural opportunities and can be linked
with deforestation and zoonoses. Arable land is one of many finite, non-renewable (in
reasonable time scales) planetary resources which need to be used sparingly [14, 15].
Indeed, once a piece of land has been urbanized, covered e.g. by a building or road,
thesoildiesquickly.Ifitisthenunsealed,itcanbecomefertileagainonlyafteravery
long time, through natural processes. Soil sealing is also a major driver of flood risk
[16]. In this context, the spatial aspects of urban land use elude a precise quantitative
description, despite a huge body of literature on the statics and dynamics of cities.
Citydefinitionitselfisstillaratheropenproblem,especiallyattheglobalscale.Hence,
thereisaneedforrobustempiricalstylizedfactstoguidetheemergingurbanscience.
Herewestudythedistributionofurbanlandusewithinglobalcities,anditsevolution
with city size. We show that it can guide us for defining cities, and help us determine
whether smaller or larger cities are more parsimonious in their use of land.
Wenotefirstthatthegenericshapeofcitiesiscircular.Theyareusuallyorganized
aroundacitycenter,wherehumanactivitiesareespeciallyconcentrated.Thisisasso-
ciated with higher buildings, high levels of built up and artificial land, of residential
population density, employment and urban amenities. It is the reason why quantita-
tivespatialmodelsofurbanstructurestartedwitharadialapproachtocities[17,18].
Here, in order to find a generic urban structure, we focus only on the most essen-
tial spatial characteristics of cities, which might be observed for very different entities
worldwide. We observe that the urban radial structure has such a generic character.
Second, we know that cities exist in a wide variety of scales. The distribution of
theirsizehasbeenmuchstudiedandlinkedtoZipf’slaw[19].Manyattributesofcities,
suchasaverageincomeorairpollutionalsoevolvewithsize,andtheirstudyconstitutes
the domain of urban scaling laws [20–22]. This study actually started in biology,
wherescalinglawsfororganismslinktheirmasstootherattributes,suchasheartrate
or bone section [23]. Scaling laws in biology are grounded on the obvious definition
of mass, which is a good measure of organisms’ size. For urban scaling laws, total
populationN isusuallyconsideredanequivalent,althoughitisdimensionless.Itisthe
sizeparameterofcitieswhichisbestdefined,becausemostoftheurbanpopulationis
concentrated near the city center, and the total population is not too sensitive to city
definition. One of the important differences between biological organisms and cities
is indeed that humans who animate cities are largely independent, which means that
the city does not have as much coherence, as a whole, as a biological organism. This
explains why the question of city definition is still open after decades of research on
the subject.
Hence we study here how center-periphery profiles of urban land use evolve with
city size measured by population N. This links intra-urban study (radial analysis) to
inter-urbanstudy(scalinglaws)andcanbeseenasastudyof“citiesassystemswithin
systems of cities” [24]. More precisely, we study the radial profiles of urban built-up
2

landinthe1800largesturbanareasoftheworld,withmorethan300,000inhabitants
each. And we find that these center-periphery profiles present striking regularities,
within cities and across city sizes and countries of the world. This provides a new
robust stylized fact, much needed for the advancement of urban science.
Uniformity of land use in world cities
Fig. 1 Urbanradialstructureofbuilt-uplandin2020.Shareofbuilt-uplandforthe1800+largest
globalcitiesasafunctionofthea)non-rescaleddistancerandb)rescaleddistancer′ tothecenter.
c)Statisticsontherescaledprofiles,showinga√clearcommontrend.d)CharacteristicradiuslN asa
function of population N, with a line lN =l1 N, where l1 =6 m, used as a guide to the eye (see
Supp.Table1andSupp.Fig.11).
Using radial (center-periphery) profiles allows us to project (or average) the two-
dimensional urban land on only one dimension, the distance r to the city center (Fig.
1a)), which is convenient to assess how the share of built-up land s(r) decreases when
thedistancetothecenterrincreases.Thenweusetwomethodstoremovetheeffectof
sizeandidentifythescalinglawgoverningtheseurbanlanduseprofiles.Thefirstone,
3

illustratedonFig.1b)-c),consistsinrescalingthedistancetothecenterproportionally
√
to the square root of city population N. The rescaled distance r′ is given by r′ =
(cid:112)
r.k , with k = N /N the rescaling factor, where we use Tokyo, the largest
N N Tokyo
city in the world with population N ≃3.107 inhabitants, as a reference (without
Tokyo
loss of generality). For a city 4 times smaller than Tokyo such as London, (N =
√London
N /4), the distance is multiplied by a rescaling parameter k = 4 = 2. In
Tokyo London
otherwords,theareaofeachcityisstretchedproportionallytoitspopulationN.This
providesadatacollapseofthebuilt-uplandprofilesofglobalcities,andagenericradial
profileappears(Fig.1b)-c)).Thisprofilehasanexponentialformandacharacterestic
scale (it is not scale-free). Our second method consists then in an exponential fit of
the radial built-up land profile s (r) of each city, following s (r) = a exp(−r/l ).
N N N N
We find that the share of built-up land in the city center a is rather constant,
N
around 35% (see Supp. Info.). And the characteristic distance (scale) l of these
N √
exponentially decreasing profiles scales like the square root of population l ∼l . N
N 1
(Fig.1(d)),wherel ≃6misthecharacteristicradiusofatheoreticalcitywithN =1
1
inhabitant (see Supp. Info.). The results of both methods are clearly consistent and
robust.Built-uplandisstrikinglysimilarinworldcities,oncetheeffectofsizeistaken
off. And this effect is simple and geometrical. As the characteristic radius l of a city
√ N
is proportionalto the square root of its population l ∼ N, the built-up area S of a
N
city is proportional to its population S ∼l2 ∼N. This means that the built-up area
N
per capita is constant, and that inhabitants of small or large cities use just as much
built-uplandonaverage.Italsomeansthateffortstocurburbansprawlandpreserve
arable and natural land are needed equally in small and large cities. We note that the
relation between area S and population N of cities has already been studied rather
extensively, but without a conclusive result. The exponents coined in the literature
[8,9,21]rangebetween2/3and1,thevaluewefindhere.Itisafundamentalrelation,
which is the starting point of different modelling approaches [9, 22]. Here we reach a
definite conclusion, at the global scale, for two reasons. First, we focus on land use
only, which is probably the most regular morphological aspect of cities. Second, our
radialscalingmethodsallowustoexploitthegenericallycircularstructureofcitiesand
extract the size effect efficiently. Furthermore, we obtain a simple universal formula
√
governing built-up land in world cities s (r) = aexp(−r/(l N)), with a ≃ 35%
N 1
and l ≃ 6m. This is a precious stylized fact which can be a guide for city definition
1
regarding environmental impacts such as losses of biodiversity, land take or urban
heat island, which are all linked to the urbanized area of cities [1, 4, 5, 13]. We note
that very similar results can likely be obtained for artificial or impervious urban land
[25–28], even though datasets at the global scale are not as reliable yet.
We note also that water bodies and polycentric urban regions have some influence
on the radial profiles of built-up land studied here. We first need to state that water
bodies have been removed from our analyses. Since land under water is not built-
up, the share of built-up land is computed over emerged land only, which is a rather
effective way to treat coastal cities. Indeed, to put it simply, cities which include a
largeareaofwaterbodies,suchascoastalcities,presentradialprofileswhicharequite
similar to more continental cities, once water bodies are removed from the analysis.
This can be seen on Figure 1d), where waterfront cities follow the general trend, and
4

|                                             | 6   |     |     |     |     | 6                                           |        |         |
| ------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------------- | ------ | ------- |
| )%( eliforp naem eht ot ecnereffid etulosbA |     |     |     |     |     | )%( eliforp naem eht ot ecnereffid etulosbA | 5−25 % | 45−65 % |
Overlap
|     | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))) |     |     |     |     |     | 25−45 % | 65−85 % |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | ------- | ------- |
|     | 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |     |     |     |     | 4   |         |         |
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
|     | 2   |     |        |     |         | 2   |     |     |
| --- | --- | --- | ------ | --- | ------- | --- | --- | --- |
|     | 0   |     |        |     |         | 0   |     |     |
|     | −2  |     | 5−25 % |     | 45−65 % | −2  |     |     |
Water
|     |     |                                         | 25−45 %  |     | 65−85 % |                                         |          |          |
| --- | --- | --------------------------------------- | -------- | --- | ------- | --------------------------------------- | -------- | -------- |
|     | 0   | 10                                      | 20 30 40 | 50  | 60      | 70 0 10                                 | 20 30 40 | 50 60 70 |
|     |     | Rescaled distance to the center r' (km) |          |     |         | Rescaled distance to the center r' (km) |          |          |
)%( eliforp naem eht ot ecnereffid etulosbA )%( eliforp naem eht ot ecnereffid etulosbA Brazil Congo DR. Nigeria
|     | 10  |     |     |     |     | 10  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
|     |     |     |     |     |     |     | China India | Pakistan |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- |
|     | 8   |     |     |     |     | 8   |             |          |
|     | 6   |     |     |     |     | 6   |             |          |
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
|     | 4   |                                         |          |       |     | 4                                       |          |          |
| --- | --- | --------------------------------------- | -------- | ----- | --- | --------------------------------------- | -------- | -------- |
|     | 2   |                                         |          |       |     | 2                                       |          |          |
|     | 0   |                                         |          |       |     | 0                                       |          |          |
|     | −2  |                                         |          |       |     | −2                                      |          |          |
|     | −4  |                                         | France   | Japan | USA | −4                                      |          |          |
|     |     |                                         | Germany  | U.K   |     |                                         |          |          |
|     | −6  |                                         |          |       |     | −6                                      |          |          |
|     | 0   | 10                                      | 20 30 40 | 50    | 60  | 70 0 10                                 | 20 30 40 | 50 60 70 |
|     |     | Rescaled distance to the center r' (km) |          |       |     | Rescaled distance to the center r' (km) |          |          |
Fig. 2 Deviation from the mean rescaled built up land profile, depending on geographical and
economicfactors.a)Waterfrontcities,b)Polycentricareas,c)5countrieswithhighGDPpercapita,
d)3oftheBRICScountries(Brazil,China,India)and3developingcountries(CongoDR.,Nigeria,
Pakistan).
onFigure2a),wheredeviationsduetowaterbodiesarerathersmall(afewpercentage
points, even for cities having most of their area covered by water). We note however
that there is a trend in these deviations as cities with more water bodies have more
built-up land in their periphery, on average. On the other hand, polycentric urban
regions introduce more fluctuations on Figure 1d), and an understandably higher
characteristic distance on average, although the deviations they introduce in radial
| profiles | on  | Figure | 2b) are | also rather | small. |            |         |     |
| -------- | --- | ------ | ------- | ----------- | ------ | ---------- | ------- | --- |
| Wealth,  |     | hidden | behind  |             | the    | uniformity | of land | use |
patterns
Ourscalinganalysesalsosuggesttodefineasize-independentindicatorofurbanextent
percapita,whichwecallUrbanBuiltLandIndex(UBLI),asUBLI=a .l2 /N.Since
N N
5

the share of built-up land in the city center a is roughly constant (see Supp. Info.),
N
this index is closely related to the residual of the regression on Fig. 1d) (see Supp.
Fig. 14a)). We note also that this UBLI has a value which is on average l2 ≃ 34 m2
1
if we forget a (roughly constant). This distance l ≃ 6 m (the characteristic length
N 1
of a theoretical city with N = 1 inhabitant) is a new fundamental constant of cities,
and l−2 ≃ 29,000 inhabitants/km2 gives a characteristic scale of population density.
1
Contrary to studies of scaling laws in physics or biology, this UBLI indicator is not
dimensionless. This is linked to the fact that total population N, the size parameter,
is a dimensionless measure of human life in a city (an ”urban mass”), which actu-
ally measures many different phenomena studied in urban scaling analysis, related
to economic and social activity, living conditions or pollution for instance. There is
no equivalent in physics or biology, which also relates to our discussion above on the
correspondence between city population and mass of organisms.
Fig.3 GlobalmapoftheUrbanBuiltLandIndex(UBLI),whichindicatescities’extentirrespective
oftheirsize.SeeSupp.Info.forzoomsandacomparisonwithwealth.
This Urban Built Land Index allows us to characterize per capita urban land
use independently of the size of cities. What is left of global per capita urban land
variations, then, when the size effect is taken off? The answer is wealth, measured by
the gross domestic product per capita (GDP pc), as shown on Figures 3 and 4. When
mapping the UBLI (Fig. 3), we observe a map very reminiscent of the global map of
theGDPpc(seeSupp.Fig.14).Andwhenwerelatethetwovariablestogether(GDP
pc and median UBLI) for the countries with the largest number of cities, we observe
indeedasurprisinglyhighlinearcorrelationR=0.95(Fig.4a).Thislevelofcorrelation
(see Supp. Fig. 13) means that the relationship between wealth and urban land use is
extremely direct. Actually, it is probably two-way, since more wealth allows people to
consumelargerbuildingspacespercapita,andtheconstruction,maintenance,heating
6

|     | 40  |     | Germany |               | Germany       |     |     |     |
| --- | --- | --- | ------- | ------------- | ------------- | --- | --- | --- |
|     |     |     |         | United States | United States |     |     |     |
bbbbbbbbbbbbbbbbbbbbbb))))))))))))))))))))))
|     | aaaaaaaaaaaaaaaaaaaaaaaa)))))))))))))))))))))))) |     |     |     | 30  |     |     |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Japan
Canada
| ).bahni/²m( ILBU naideM | 30  |     |       |                         | France Italy   |     |     |     |
| ----------------------- | --- | --- | ----- | ----------------------- | -------------- | --- | --- | --- |
|                         |     |     | Japan | ).bahni/²m( ILBU naideM | United Kingdom |     |     |     |
Canada
ItalyFranceUnited Kingdom
Russian Federation
|     | 20  |     |     |     |       | Brazil Indonesia |         |     |
| --- | --- | --- | --- | --- | ----- | ---------------- | ------- | --- |
|     |     |     |     |     | China | Mexico           |         |     |
|     |     |     |     |     | 10    |                  | Nigeria |     |
Thailand
IndonesiaBraziAlrgReunstsiniaan Federation
|     | T hailandMexico China |     | Philippines |     |     |     |     |     |
| --- | --------------------- | --- | ----------- | --- | --- | --- | --- | --- |
10 Niger ia
|     |                 |     | I                | r a n , Islamic Rep. |                    | Ph i lip p ines |                  |           |
| --- | --------------- | --- | ---------------- | -------------------- | ------------------ | --------------- | ---------------- | --------- |
|     | Iraq            |     | I                | n d ia               | Iran, Islamic Rep. |                 |                  | I raq     |
|     | Colombia Turkey |     |                  |                      |                    | Turkey I n d ia |                  | Pakista n |
|     |                 |     | Pakistan         |                      | 5                  |                 |                  |           |
|     |                 |     | Congo, Dem. Rep. |                      |                    | Colombia        | Congo, Dem. Rep. |           |
0
|     | 0 16,000 | 32,000       | 48,000 | 64,000 | 2   | 3                   | 5   |     |
| --- | -------- | ------------ | ------ | ------ | --- | ------------------- | --- | --- |
|     |          | GDP pc (US$) |        |        |     | Mean household size |     |     |
Fig.4 RelationshipbetweenthemediannationalurbanbuiltlandindexUBLIanda)grossdomestic
productpercapitaandb)meanhouseholdsize(log-loggraph).
and cooling of these larger buildings generates economic activity and wealth which
| contributes | to  | higher GDP | pc. |     |     |     |     |     |
| ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
We also note that wealth is a multi-faceted variable, correlated to many others
such as household size (negatively, see Fig. 4 for the link between household size and
UBLI) or car ownership (positively). These variables can in turn influence urban land
per capita.
Turning back to rescaled radial profiles of urban land use, we can observe the
influenceofthosevariablesontheintra-urbanstructureofcities.WeseeonFigure2c)
and d) that economic development and wealth are indeed expressed in urban radial
profiles,oncethesizeeffectisremoved.Citiesinwealthiercountrieshavemorebuilt-up
| land, | in particular | in their | periphery, | where most | urban | land is located. |     |     |
| ----- | ------------- | -------- | ---------- | ---------- | ----- | ---------------- | --- | --- |
Our findings suggest that on the one hand, efforts to mitigate urbanisation and
soil sealing by buildings are needed equally for small and large cities, anywhere in
the world. On the other hand, efforts should be all the more important as countries
and people are wealthier. As for other variables and other scales (such as carbon
footprint [29, 30]), we find indeed an extremely direct link here between wealth and
environmentalimpacts.Inordertopreservelandonearthfromurbanisationandmeet
sustainability challenges, a general conclusion is that the goal of human economic
activity and policy needs to change. The objective of increasing wealth per se (mea-
suredbyGDP)iswrong,becauseitincreasesclimatechange,environmentalpollution
andthetollonplanetaryressourcesandbiodiversity.Actually,weseeherethatdevel-
opment, taken in the sense of economic growth, goes exactly against sustainability
challenges. On the contrary, the aim of economic activity should be less individualis-
tic, competitive and materialistic, and more collective, collaborative and immaterial
(theenjoymentoflife[31]).Inthisendeavor,educationandresearchcouldclearlyplay
an important role. However, this is not really the orientation which human societies
| are | choosing now. |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
7

Methods
Data
Thisworkreliesonremotelysenseddataforobservinglanduse,whichprovidesmany
opportunitiesforurbanandenvironmentalstudies,forinstanceregardingurbanforms
[32]. We use mainly the GHSL Built-up surface dataset (GHSL BUILT-S R2022A),
developed by the Global Human Settlement Layer (GHSL) project of the European
Commission (which is illustrated on Supp. Figs 5 and 6). This raster spatial dataset
providestheglobaldistributionofbuilt-upareas,i.eareascoveredbybuildings,using
a spatial generalization [33]. We choose here a dataset with a resolution of 100 m,
which is sufficiently precise considering the 200m width of rings used in this study.
The second main component of our data is the total population of cities, which we
use as a scale factor. We select the database of Cities with 300,000 inhabitants or
more from the World Urbanization Prospects of the United Nations. This represents
1860 cities and above 2.5 billion people, more than 32% of the world population. The
population for each year presents collected data (national censuses, sample surveys,
civilregisters),anddemographicprojectionstofilldatagaps[34].Waterbodiesneedto
beconsideredsincetheycanhaveasignificantimpactonurbanlandusedistribution,
and urban areas are often adjacent to rivers and coastlines [35]. Consequently, we
mask the GHSL built-up surface raster values by the ESRI - Garmin World Water
Bodies, which contain the major oceans, seas, rivers, lakes and salt flats at a global
scale. Through this process, all the pixels that intersect with any body of water are
not considered in our analysis. We also use economic and demographic data at the
scale of world countries, namely GDP per capita data in 2020 provided by the World
Bank, and mean househod size provided by the United Nations. The full reference of
these datasets is given in the Supplemental Information.
Statistical and spatial analysis
The determination of the city centers’ location is an important point for our radial
analysis.Wefocushereoncityhalls,duetotheirconsistentlycentrallocation.Incases
where the city hall is not referenced on any reliable website, we use the location of a
centralstructuringbuilding,suchasacentralpostoffice,amajorcentralmarketplace
orbazaar,amayoralhouse,acentralsquareoracentralreligiousmonument,withthe
precioushelp ofthe GlobalUrban Centres database [36].To guaranteethe robustness
of this key data, all 1860 centers are returned one by one using this method. Then
we perform a radial analysis for each city in our sample. We first define a maximal
urban extent as a disc around each city center. This disc is of radius D =150 km for
the urban area of Tokyo (the largest city in the sample, whose population is denoted
N ).Theradiusissmallerforothercities,accordingtothescalinglawweuncover
Tokyo
in our analysis. For a city of population N, this maximal extent is r = D/k ,
max N
(cid:112)
where k = N /N, with r the Euclidean distance to the center. For London,
N Tokyo
whose population is roughly 4 times smaller than Tokyo’s, k = 2 and the maximal
extent is 150/2=75km (see Supp. Fig. 6). Within each city’s disc, we then extract
concentricringsof200mwidth,inwhichtheshareofbuilt-uplandiscomputed.Thus
8

we obtain our object of study, the share of built-up land s(r) at any distance r from
thecitycenter.InordertomakeallcitiescomparabletoTokyo(chosenasareference,
without loss of generality), we rescale on Fig. 1b)-c) the distance r of all cities’ radial
profiles s(r) using the rescaling factors k , thus defining a rescaled distance r′ to
N
the center . We check that the exponent 1/2=0.5, corresponding to the square root
of population, provides an optimal rescaling and data collapse in terms of signal-to-
noise ratio (Supp. Fig. 7). Since rescaling factors k have different real values, we use
N
linearinterpolationbetweentheclosestdatapointsinordertoobtaindataatcommon
rescaleddistancesandcomputestatisticsonrescaledprofiless(r′)(Fig.1c)).Sincethe
generic shape of those radial profiles of land use s (r) is exponential, we perform an
N
exponential regression for all cities’ radial profiles, following s (r)=a exp(−r/l ),
N N N
where a is the share of built-up land in the city center and l the characteristic
N N
decreasedistance,foracityofpopulationN.Notethatthischaracteristicdistancel
N
is defined up to a multiplicative constant. Here it gives the distance at which built-up
land is exp(−1) ≃ 37% of its value in the center, and also the distance at which the
highest quantity of land is built (see Supp. Info.). These regressions give a median R2
of 0.9 on all cities (see Supp. Table 1), a very high value which confirms their quality.
We single out waterfront cities and polycentric areas in our analysis. We consider a
city as waterfront if more than 60% of its maximal urban extent disc (of radius r
max
around the center) is covered by water bodies, and as interconnected (polycentric)
if more than 75% of its disc overlaps with other cities’ maximal extents. The clear
scalingbehaviourobservedheresuggeststodefineanUrbanBuiltLandIndex(UBLI)
to capture size-independant variations, as UBLI = a l2 /N, which is closely related
N N
totheresidualsofFigure1d)(asillustratedonSupp.Fig.11a)).Itgivesameasureof
the characteristic built-up area per inhabitant (defined, as the characteristic distance
l ,uptoamultiplicativeconstant),whichisonaveragehere21m2(median12m2,see
N
Fig. 3), and of a characteristic population density (”net” density, with respect to the
built-up area only), on average 47,000 inhabitants/km2 (median 84,000 inhab./km2).
We note that the analyses are conducted using the R programming language,
v4.2.2.AddingtoR-base,Rpackagesareusedforspatialanalysis(rgdal,rgeos,raster,
sp, sf and terra), data manipulation (tidyverse, stringr, purrr, plyr, dplyr, tidyr,
data.table, tibble and vctrs), import and export (openxlsx), regressions (minpack.lm,
nls2), visualization (ggplot2, plotly, leaflet, mapsf, cowplot, ggthemes, viridis, and
ggsn)andmoremiscellaneoususes(str2str,gdata,corrplotandggpubr).Theprocess-
ingusesthenationalsharedacademiccloudserveroftheFrenchVeryLargeResearch
Infrastructure for Social Sciences and Humanities, Huma-Num.
Supplementary information. This manuscript has an accompanying supplemen-
tary file.
Acknowledgements. The authors acknowledge comments by M. Barth´el´emy, A.
Litvine,G.Caruso,R.LeGoixandA.P´echeric,dataprovidedbyP.Kilgarriffaswell
as funding by ANR GreenLand and RIN SUCHIES.
Author Contributions. R.L. designed the study. V.V. acquired the data and per-
formed the analyses under supervision by R.L. V.V. and R.L. interpreted the results
and wrote the manuscript.
9

| Competing | Interests. |     | The | authors | declare | no competing | interests. |
| --------- | ---------- | --- | --- | ------- | ------- | ------------ | ---------- |
References
[1] Seto, K.C., Fragkias, M., Gu¨neralp, B., Reilly, M.K.: A meta-analysis of global
| urban | land | expansion. | PloS | one | 6(8), | 23777 (2011) |     |
| ----- | ---- | ---------- | ---- | --- | ----- | ------------ | --- |
[2] Bren d’Amour, C., Reitsma, F., Baiocchi, G., Barthel, S., Gu¨neralp, B., Erb,
K.-H., Haberl, H., Creutzig, F., Seto, K.C.: Future urban land expansion and
implications for global croplands. Proceedings of the National Academy of
| Sciences | 114(34), |     | 8939–8944 | (2017) |     |     |     |
| -------- | -------- | --- | --------- | ------ | --- | --- | --- |
[3] McDonald, R.I., Mansur, A.V., Ascens˜ao, F., Colbert, M., Crossman, K.,
Elmqvist, T., Gonzalez, A., Gu¨neralp, B., Haase, D., Hamann, M., et al.:
Researchgapsinknowledgeoftheimpactofurbangrowthonbiodiversity.Nature
| Sustainability |     | 3(1), | 16–24 | (2020) |     |     |     |
| -------------- | --- | ----- | ----- | ------ | --- | --- | --- |
[4] Simkin, R.D., Seto, K.C., McDonald, R.I., Jetz, W.: Biodiversity impacts and
conservationimplicationsofurbanlandexpansionprojectedto2050.Proceedings
| of the | National | Academy |     | of Sciences | 119(12), | 2117297119 | (2022) |
| ------ | -------- | ------- | --- | ----------- | -------- | ---------- | ------ |
[5] Seto, K.C., Gu¨neralp, B., Hutyra, L.R.: Global forecasts of urban expansion to
2030 and direct impacts on biodiversity and carbon pools. Proceedings of the
| National | Academy |     | of Sciences |     | 109(40), | 16083–16088 | (2012) |
| -------- | ------- | --- | ----------- | --- | -------- | ----------- | ------ |
[6] Schwela, D.: Air pollution and health in urban areas. Reviews on environmental
| health | 15(1-2), | 13–42 | (2000) |     |     |     |     |
| ------ | -------- | ----- | ------ | --- | --- | --- | --- |
[7] World Health Organization: Integrating Health in Urban and Territorial Plan-
ning:aSourcebook.UN-HabitatandWorldHealthOrganization,Geneva(2020)
[8] Batty,M.,Ferguson,P.:Definingcitysize.SAGEPublicationsSageUK:London,
| England | (2011) |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --- | --- |
[9] Ribeiro, F.L., Rybski, D.: Mathematical models to explain the origin of urban
| scaling | laws. | Physics | Reports |     | 1012, 1–39 | (2023) |     |
| ------- | ----- | ------- | ------- | --- | ---------- | ------ | --- |
[10] Glaeser, E.: Triumph of the City: How Our Greatest Invention Makes Us Richer,
Smarter, Greener,Healthier, andHappier.PenguinPublishingGroup, NewYork
(2008)
[11] White, R., Engelen, G.: Cellular automata and fractal urban form: a cellular
modelling approach to the evolution of urban land-use patterns. Environment
| and | planning | A 25(8), | 1175–1199 |     | (1993) |     |     |
| --- | -------- | -------- | --------- | --- | ------ | --- | --- |
[12] Center for International Earth Science Information Network / Columbia Uni-
versity: Urban-Rural Population and Land Area Estimates Version 2. NASA
10

Socioeconomic Data and Applications Center, Palisades, NY (2013)
[13] Zhou, B., Rybski, D., Kropp, J.P.: The role of city size and urban form in the
surface urban heat island. Scientific reports 7(1), 4791 (2017)
[14] Meadows, D.H., Club of Rome: The Limits to Growth; a Report for the Club
of Rome’s Project on the Predicament of Mankind. Universe Books, New York
(1972)
[15] IEA International Energy Agency: World Energy Outlook 2023, Paris, France
(2023)
[16] Wheater,H.,Evans,E.:Landuse,watermanagementandfuturefloodrisk.Land
use policy 26, 251–264 (2009)
[17] Von Thu¨nen, J.H.: Der isolierte staat in beziehung auf national¨okonomie und
landwirtschaft. Gustav Fischer, Stuttgart (reprinted 1966) (1826)
[18] Alonso, W.: Location and Land Use. Harvard University Press, Cambridge, MA
and London, England (1964). https://doi.org/10.4159/harvard.9780674730854
[19] Nitsch, V.: Zipf zipped. Journal of Urban Economics 57(1), 86–100 (2005)
[20] Pumain, D.: Scaling Laws and Urban Systems. SFI Working Paper 2004-02-002,
Santa Fe Institute, Santa-Fe, NM, United-States (2004)
[21] Batty,M.:Thesize,scale,andshapeofcities.science319(5864),769–771(2008)
[22] Bettencourt, L.M.: The origins of scaling in cities. Science 340(6139), 1438–1441
(2013)
[23] Brown, J.H., West, G.B.: Scaling in Biology. Oxford University Press, Oxford,
UK (2000)
[24] Berry, B.J.: Cities as systems within systems of cities. Papers in regional science
13(1), 147–163 (1964)
[25] Tobler, W.R.: Satellite confirmation of settlement size coefficients. Area 1(3),
30–34 (1969)
[26] Gu´erois, M., Pumain, D.: Built-up encroachment and the urban field: a com-
parison of forty European cities. Environment and Planning A 40(9), 2186–2203
(2008)
[27] Lemoy, R., Caruso, G.: Evidence for the homothetic scaling of urban forms.
Environment and Planning B: Urban Analytics and City Science 47(5), 870–888
(2020)
11

[28] Lemoy, R., Caruso, G.: Radial analysis and scaling of urban land use. Scientific
| reports | 11(1), | 1–8 (2021) |     |     |     |     |     |
| ------- | ------ | ---------- | --- | --- | --- | --- | --- |
[29] Hertwich, E.G., Peters, G.P.: Carbon footprint of nations: a global, trade-linked
| analysis. | Environmental |     | science | & technology |     | 43(16), 6414–6420 | (2009) |
| --------- | ------------- | --- | ------- | ------------ | --- | ----------------- | ------ |
[30] Moran,D.,Kanemoto,K.,Jiborn,M.,Wood,R.,T¨obben,J.,Seto,K.C.:Carbon
footprintsof13000cities.EnvironmentalResearchLetters13(6),064041(2018)
[31] Georgescu-Roegen, N.: Energy analysis and economic valuation. Southern Eco-
| nomic | Journal, | 1023–1058 | (1979) |     |     |     |     |
| ----- | -------- | --------- | ------ | --- | --- | --- | --- |
[32] Zhu,Z.,Zhou,Y.,Seto,K.C.,Stokes,E.C.,Deng,C.,Pickett,S.T.,Taubenb¨ock,
H.: Understanding an urbanizing planet: Strategic directions for remote sensing.
| Remote | Sensing | of Environment |     | 228, | 164–182 | (2019) |     |
| ------ | ------- | -------------- | --- | ---- | ------- | ------ | --- |
[33] European Commission, Joint Research Centre, Schiavina M., Melchiorri M.,
Pesaresi M. et al.: GHSL Data Package 2022 – Public release GHS P2022.
| Publications |     | Office of | the European |     | Union | (2022) |     |
| ------------ | --- | --------- | ------------ | --- | ----- | ------ | --- |
[34] UnitedNations,DepartmentofEconomicandSocialAffairs,PopulationDivision:
WorldUrbanizationProspects:The2018Revision-Methodology,OnlineEdition
(2018)
[35] Grimm, N.B., Faeth, S.H., Golubiewski, N.E., Redman, C.L., Wu, J., Bai, X.,
Briggs,J.M.:Globalchangeandtheecologyofcities.science319(5864),756–760
(2008)
[36] Kilgarriff, P.: Global Urban Centres (GUC). https://doi.org/10.5281/zenodo.
18705750
[37] Louf, R., Barthelemy, M.: Scaling: lost in the smog. Environment and Planning
| B: Planning   |       | and Design | 41(5),      | 767–769 | (2014) |     |     |
| ------------- | ----- | ---------- | ----------- | ------- | ------ | --- | --- |
| Supplementary |       |            | Information |         |        |     |     |
| The GHSL      | built | surface    |             | data    |        |     |     |
The main dataset used in this study, the GHS-BUILT-S dataset, is presented here on
figures5and6.Thisglobalrasterdatasetprovidesthebuilt-uparea(insquaremeters)
within square cells of 100m side length. The value is encoded as a 4 digit integer,
between0and10,000(whichcorrespondstoa100%built-upcell).Theremote-sensing
and processing of this dataset [33] ensures that the urban footprints correspond to
reality, even in specific areas such as industrial zones, ports or slums. In this way, the
| entire urban | area | can be | taken into | account | in  | this work. |     |
| ------------ | ---- | ------ | ---------- | ------- | --- | ---------- | --- |
12

Fig. 5 TheGHSLbuiltsurfacedatasetfortheSeineValleyinFrance(Rouen-Parisaxis).Apixel
withvalue10,000isfullybuilt,whileapixelwithvalue0isnotbuiltatall.
Comparison of urban extents for cities of different sizes
We propose to visualize on Figure 6 the maximal urban extents used in this study,
in order to understand the chosen definition of cities’ buffers. We compare Tokyo’s
r =150kmradiusbufferwithitsequivalentr inothercitiesofgivenpopulation
max Nmax
(cid:112)
N, using the formula r =r /k =r N/N .
Nmax max N max Tokyo
Thismethodallowsustocircumventonemajorprobleminthestudyoftheurban
environment, which concerns the definition of the city. There is no consensus on how
theyshouldbedefined,eitherbyresearchersorbyotherorganizations.Andthisclearly
influences the results of comparative urban studies [37]. Taking or not taking into
accountspecificzoneswillleadtodifferentresults,sinceperimetersarenotanalogous.
Thereisalackofauniformdefinitionofcitiesacrosstheworld,whichmakesitdifficult
to compare urban areas [1]. In this work, we manage to use this global database
becauseourbufferdefinitionisbasedonthepopulationofcities,whichisdefinedhere
by the World Urbanization Prospects of the United Nations. We note that in this
population dataset each year’s population includes collected data (national censuses,
sample surveys, civil registers, etc.), and demographic projections to make up for the
fact that harvesting dates can vary from one country to another, and for data gaps.
13

Fig.6 Comparisonofbuffersizes,withareferencetothepopulationofTokyousingarNmax=150km
radiuswithaα=1/2scalingexponent.Comparisonofbuffersizesforcitiesofdifferentsizes:Tokyo
(Japan),LosAngeles(USA),Madrid(Spain),Rabat(Morocco),Jeonju(RepublicofKorea).Wekeep
the same scale on all maps of the first and third lines, but the maps of the 2nd and 4th lines are
rescaled.
Signal over noise ratio
Asignal-to-noiseratioSNRcanbecomputedonthe(rescaled)built-upradialprofiles
s (r′) to determine the most appropriate scaling exponent [27]. To compute this
N
quantity, we rescale the profiles with different exponent values α ranging from 0 to 1,
meaningthattherescaleddistanceisr′ =r(N /N)α.Thenwecomputeameasure
Tokyo
of the efficiency of this rescaling. We start with the mean value < s (r′) > (over all
N
cities)ofthebuilt-uplandshareateach(rescaled)distancer′,whichweconsiderasour
(cid:112)
signal. The corresponding standard deviation σ (r′) = <(s (r′)−<s (r′)>)2 >
s N N
is the noise. We compute the SNR as the ratio of both quantities, averaged over all
14

distances SNR = <s (r′)>/σ (r′). This averaging over rescaled distances (which
N s
we denote with an overline) starts in the center (r′ = r = 0) and stops when the
meanbuilt-uplandshare<s (r′)>reachesagiventhresholdt(forinstance,t=0.1
N
or 0.175). We then represent the variations of this SNR as a function of the values
of the rescaling exponent α and the threshold on Figure 7, which helps us find the
best rescaling exponent. Indeed, the highest point on the curves corresponds to the
strongest signal over noise ratio and therefore to the most relevant value, for each
threshold. Here it corresponds to the scaling exponent 1/2.
3.5
3.0
2.5
2.0
0.00 0.25 0.50 0.75 1.00
Rescaling exponent a
RNS
oitar
esion−ot−langiS
t=
0.05
0.075
0.1
0.125
0.15
0.175
0.2
Fig. 7 VariationofthesignaltonoiseratioSNRasafunctionoftherescalingexponentαused,for
differentthresholdvaluest.Theblackverticallinerepresentsexponentα=1/2.Thelinearbehavior
forlargevaluesofαislinkedtothemaximalurbanextentrmax beingreached.
Impact of considering water bodies
Some cities have a large amount of water bodies around them. This clearly has an
impact on their built-up area in the sense that the presence of water is a constraint
for building construction and artificialization. In order to illustrate this, we show on
thefirstlineofFigure8howwaterbodiesimpactbuilt-uplandprofilesfortwocoastal
cities.Whenwaterisconsidered,thatis,landcoveredbywaterbodiesisremovedfrom
our analysis, built-up land shares are higher, since they are computed on incomplete
rings. On the second line, we show that this does not affect the scaling law and the
general picture much, since not all cities are coastal.
Characteristic decrease distance and models
We perform non-linear regressions of the built-up land share s (r) as a function of
N
the distance r to the center, following s (r) = a exp(−r/l ). The first parameter
N N N
15

|                            | 45  |     |               |     | 45                         |     |     |               |
| -------------------------- | --- | --- | ------------- | --- | -------------------------- | --- | --- | ------------- |
|                            |     |     |               |     | 40                         |     |     | Water kept    |
|                            | 40  |     | Water kept    |     |                            |     |     |               |
|                            | 35  |     | Water removed |     | 35                         |     |     | Water removed |
| )%( dnal pu−tliub fo erahS |     |     |               |     | )%( dnal pu−tliub fo erahS |     |     |               |
|                            | 30  |     |               |     | 30                         |     |     |               |
25
25
|     | 20  |     |     |     | 20  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 15  |     |     |     | 15  |     |     |     |
10
10
|     | 5                                       |       |       |       | 5   |      |                                         |          |
| --- | --------------------------------------- | ----- | ----- | ----- | --- | ---- | --------------------------------------- | -------- |
|     | 0                                       |       |       |       | 0   |      |                                         |          |
|     | 0 10                                    | 20 30 | 40 50 | 60 70 |     | 0 10 | 20 30 40                                | 50 60 70 |
|     | Rescaled distance to the center r' (km) |       |       |       |     |      | Rescaled distance to the center r' (km) |          |
0.5
10−90% quantiles
25−75% quantiles
|     |     | )%( dnal pu−tliub fo erahS |     |     | Mean   |     |     |     |
| --- | --- | -------------------------- | --- | --- | ------ | --- | --- | --- |
|     |     |                            | 0.4 |     | Median |     |     |     |
WR 10−90% quantiles
WR 25−75% quantiles
|     |     |     | 0.3 |     | WR Mean |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- |
WR Median
0.2
0.1
0.0
|     |     |     | 0   | 10 20 30 40 | 50 60 | 70 80 | 90 100 |     |
| --- | --- | --- | --- | ----------- | ----- | ----- | ------ | --- |
Rescaled distance to the center r' (km)
Fig. 8 Effectofconsideringwateronbuilt-uplandshares.Top:fortwocitiespresentingmorethan
60%ofwaterbodieswithintheirmaximalextent,DaNang(Vietnam,left)andLasPalmasdeGran
Canaria(Spain,right).Bottom:statisticsonthestudied1800+rescaledradialprofilesofurbanbuilt-
up land use. The graph compares profiles where water bodies are kept in the analysis, and where
waterbodiesareremoved(WR)fromtheanalysis,withconsequentlyslightlyhighersharesofbuilt-
upland.
a N gives a measure of the built-up land share in the city center. We note here that
the second parameter, the characteristic distance l , is the distance at which built-
N
up land is at exp(−1) ≃ 37% of its value in the center. It is also the distance from
the center at which the highest (absolute) amount of land is built, according to our
exponential model. Indeed, the total length of built-up land in each ring (considered
| here | of infinitesimal | width) | is 2πrs | N (r), which | is  | maximum | at l N . |     |
| ---- | ---------------- | ------ | ------- | ------------ | --- | ------- | -------- | --- |
In Table 1, we present the results of the estimated scaling law l ∼ l Nα, using
|     |     |     |     |     |     |     |     | N 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
log-log fits on the characteristic distance l against population N. We either keep or
N
removewaterbodiesfromtheanalysis,useone-ortwo-parametermodelsandkeepor
removeverypolycentricurbanareasfromtheanalysis.Theone-parametermodeluses
a N = 35% and fits only l N . This is associated with only a very small loss in median
R2, which shows that this hypothesis is very reasonable. Cities are considered to be
16

| Model        |     |     | NL1w NL2w | NL1*w NL2*w |      | NL1 NL2   | NL1* NL2* |
| ------------ | --- | --- | --------- | ----------- | ---- | --------- | --------- |
| Observations |     |     | 1860 1860 | 1747        | 1747 | 1860 1860 | 1747 1747 |
Scalingexponentα 0.480 0.484 0.484 0.506 0.526 0.526 0.531 0.520
| Constantl1 | (m) |     | 7.38 7.44 | 6.70 | 5.08 | 4.52 4.74 | 4.10 4.70 |
| ---------- | --- | --- | --------- | ---- | ---- | --------- | --------- |
MedianR2 (allprofiles) 0.88 0.89 0.89 0.91 0.88 0.93 0.88 0.93
| Scalinglaw’sR2 |     |     | 0.41 0.22 | 0.45 | 0.48 | 0.46 0.19 | 0.50 0.47 |
| -------------- | --- | --- | --------- | ---- | ---- | --------- | --------- |
Table 1 Resultsofa(log-log)linearregressiononcharacteristicdistancelN againstcity
populationN,loglN ∼logl1+αlogN fordifferentmodelsandsamples.Rows:thenumberof
observationsisthenumberofcitiesconsideredinthemodel.Thescalingexponentisdenotedα.
Theconstantl1 isgiveninmeters.ThetwomeasuredR2 correspondtothemedianR2 ofthe
correspondingnon-linearfitoverallprofiles,andtheR2 ofour(log-log)linearregressionofthe
scalinglaw.Columns:eachnon-linearmodelprocessedonthe1800+citieswithoneparameter
(NL1,whereaN isfixedto35%)andtwoparameters(NL2),andonasampleof1747citieswith
oneandtwoparameters(NL1*andNL2*).Inthefirst4models,whichhaveaw indexintheir
names,waterisnotconsidered(thatis,waterbodiesarekeptinthecomputationofradialprofiles).
in very polycentric urban areas here if the overlap rate of their buffer by other cities’
| buffers exceeds | 75% | (113 | cities are | in this situation). |     |     |     |
| --------------- | --- | ---- | ---------- | ------------------- | --- | --- | --- |
We can observe on Table 1 that the fitted scaling exponent α is very close to 1/2,
the constant l around 6m, the median R2 over all profiles around 0.9 and the scaling
1
law’s R2 around 0.45 in most cases (slightly higher for one-parameter models).
| Distribution     |     | of the | 1860 studied | cities,         | and | of peculiar |     |
| ---------------- | --- | ------ | ------------ | --------------- | --- | ----------- | --- |
| characteristics: |     | water  | bodies       | and polycentric |     | regions     |     |
We identify two important factors influencing urban land use, whose variations at the
global scale are represented on Figure 9. The first one is the presence of water bodies,
which is mostly associated with coastal cities. And the second one is the existenc of
polycentric urban regions, which we measure by the overlap rate of a city’s maximal
extent buffer of radius r with other cities’ extents. This is associated with the
Nmax
| most populated | areas | of   | the world. |     |     |     |     |
| -------------- | ----- | ---- | ---------- | --- | --- | --- | --- |
| Urban          | Built | Land | Index UBLI |     |     |     |     |
We note here that the Urban Built Land Index defined in the main text UBLI=
l2
a N /N is very closely linked to the residual of the power-law relationship presented √
N
on Fig. 10 (and Fig. 1d)). Indeed this relation can be written as l = l N, or
|     |     |     |     |     |     |     | N 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
logl = logl +1/2logN. The residual of this relation can be written as logl −
| N   | 1   |     |     |     |     |     | N   |
| --- | --- | --- | --- | --- | --- | --- | --- |
(logl +1/2logN),while1/2logUBLI=1/2loga +logl −1/2logN.Thedifference
| 1   |     |     |     |     | N   | N   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
betweenbothquantitiesisthenonlylogl ,whichisaconstant,and1/2loga ,which
|           |           |         |         | 1   |     |     | N   |
| --------- | --------- | ------- | ------- | --- | --- | --- | --- |
| is almost | constant, | as seen | before. |     |     |     |     |
We show on Figures 10, 11 and 12 that the fitted share of built-up land in the
center a is indeed roughly constant, around 35%. It is quite independant of the
N
characteristic distance l (and hence population size N), and does not show a clear
N
| relationship | with | polycentric | urban | areas either. |     |     |     |
| ------------ | ---- | ----------- | ----- | ------------- | --- | --- | --- |
17

Fig. 9 Geographical distribution of urban areas with 300,000 or more inhabitants in 2020. We
identifytwomaintypesofdeterminingcharacteristics:toppanel,thepresenceofanimportantwater
body,bottompanel,theproximitywithothercities.
| Relating | national  | observations | of the Urban | Built Land | Index |
| -------- | --------- | ------------ | ------------ | ---------- | ----- |
| to other | variables |              |              |            |       |
In the main text, we map the UBLI at the global scale (Figure 3). Zooms on different
continents are provided here on Figures 15, 16 and 17. We also describe in the main
text the variations of the UBLI between countries, observed via the median UBLI
at national scale. We relate the median UBLI (UBLI ) to national economic and
m
| demographic | variables | on Figure 4. |     |     |     |
| ----------- | --------- | ------------ | --- | --- | --- |
On Figure 4a), we relate it to the GDP pc of countries, obtaining a relationship
UBLI =5.74+5.28×10−4GDPpc, which yields a R2 of 0.906 (R=0.952) for the 24
m
18

)mk( Nl ecnatsid citsiretcarahC
| )mk( Nl ecnatsid citsiretcarahC 30 |     |     | 30  |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- |
| 10                                 |     |     | 10  |     |     |
| 3                                  |     |     | 3   |     |     |
<0.94 11.48 − 16.4
|     | 0.94 − 5.12 | 16.4 − 27.85 |     | aN   |           |
| --- | ----------- | ------------ | --- | ---- | --------- |
|     | 5.12 − 7.82 | >27.85       |     | 0.25 | 0.50 0.75 |
7.82 − 11.48 NA
| 1     |                   |       | 1           |              |       |
| ----- | ----------------- | ----- | ----------- | ------------ | ----- |
| 3e+05 | 1e+06 3e+06 1e+07 | 3e+07 | 3e+05 1e+06 | 3e+06 1e+07  | 3e+07 |
|       | Population N      |       |             | Population N |       |
Fig.10 CharacteristicdistancecomputedwiththeNL2*model.ThecolorsindicatetheUrbanBuilt
LandIndexUBLI=aNl 2 /N inm2/inhabitant(leftpanel),whichisdirectlyrelatedtotheresidual
N
oftheregressio√n,andtheshareofbuilt-uplandinthecenteraN (rightpanel).Ontheleftpanel,the
| lineislN =l1 | N,wherel1=6m,whileontherightpanelitislN |     |     | =0.0047N0.52. |     |
| ------------ | --------------------------------------- | --- | --- | ------------- | --- |
Fig. 11 Relationshipbetweentheshareofbuilt-upsurfaceinthecenteraN andthecharacteristic
distance lN computed with the SNL2* model. The colors indicate the percentage of overlap with
| neighboringcities(leftpanel)andthetotalpopulationN |     |     | (rightpanel). |     |     |
| -------------------------------------------------- | --- | --- | ------------- | --- | --- |
countries having the highest numbers of cities. Figure 13 shows that the correlation
between both variable is even higher if less countries are considered in this analysis.
Indeed, we obtain R=0.963 when considering only the 14 countries having the high-
est numbers of cities, R=0.984 with only 10 countries, and R=0.99987 with only 3
countries. In our view, this shows that the relationship between UBLI and GDPpc
at national scale is extremely strong, and that including more countries (with lower
19

Fig. 12 Built-upsurfaceinthecenteraN forthe1800+cities.
0 10 20 30 40
00.1
59.0
09.0
58.0
08.0
Sample size n
R
noitalerroc
raeniL
Fig. 13 Variation of the correlation R between median UBLI and GDP pc as a function of the
number n of countries included in the analysis. Countries are included in the sample in order of
decreasingnumberofcities.
numbers of cities) in this analysis introduces more noise and weakens the correlation.
Figure 14 provides a global map of the GPDpc to be compared with the global map
of the UBLI (Figure 3 of the main text). The same colors and discretization are used,
and the national GDPpc is applied to all cities of the database. We know that this is
not a correct geographical representation of this variable, but we provide it just for
this comparison, which shows that both maps are very similar.
20

Fig.14 MapofthenationalGrossDomesticProductGDPpercapita,wherethecolorsareapplied
tothestudiedcities,forcomparisonwiththemapoftheUBLI(Fig.3ofthemaintext).
On Figure 4b), we relate UBLI to mean household size (HHS), obtaining
m
UBLI =58×HHS−1.4, with R2=0.5 (R=-0.72).
m
The GDP per capita is provided by the World Bank national
accounts data, and OECD National Accounts data files, available at
https://data.worldbank.org/indicator/NY.GDP.PCAP.CD (last visited November
2024). The mean household size is provided by the United Nations Population
Division, within the Database on Household Size and Composition 2022, available
at https://www.un.org/development/desa/pd/data/household-size-and-composition
(last visited November 2024). For the mean household size, the country data is col-
lected and sorted according to the different sources which provide it. Then for each
source, an autoregressive integrated moving average (ARIMA) is used to project the
mean number of people per household in 2020 in each country. This methodology
enables us to model and forecast this time series without being constrained by the
disparities in data collection across different countries. Note also that Saudi Arabia
has no data for the household size indicator in our sources.
21

Fig. 15 ZoomingondifferentpartsoftheglobalmapoftheUrbanBuiltLandIndexUBLI(Fig.3
ofthemaintext):WestAfrica,CentralAmerica,NorthAmerica.
22

Fig. 16 ZoomingondifferentpartsoftheglobalmapoftheUrbanBuiltLandIndexUBLI(Fig.3
ofthemaintext):SouthAmerica,EastAsia,SouthEastAsia.
23

Fig. 17 ZoomingondifferentpartsoftheglobalmapoftheUrbanBuiltLandIndexUBLI(Fig.3
ofthemaintext):SouthAsia,Europe,MiddleEast.
24
---- END DOCUMENT ----
