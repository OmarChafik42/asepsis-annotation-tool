Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Jointly estimating transmissibility and prior immunity
from epidemic time series
David J.D. Earn∗ Todd L. Parsons†
Abstract
Infectious disease time series are often used to estimate a pathogen’s basic repro-
duction number, R . However, fits of epidemic models to time series conflate pathogen
0
transmissibility with pre-existing population immunity, so only the effective reproduc-
tion number, R , can be inferred. This composite parameter is the product of the
eff
underlying R and the pre-epidemic susceptible fraction, x−. We show that a conser-
0
vation law associated with epidemic momentum—prevalence weighted by potential to
infect—makes it possible to disentangle transmissibility from prior immunity and to
inferR andx− separatelyfromasingleepidemictimeseries. Wetestthemethodology
0
using stochastic epidemic simulations, and illustrate the approach with a reappraisal
of influenza transmissibility during the 1918 pandemic, estimating rather than assum-
ing the degree of prior population immunity. For the autumn wave in Philadelphia,
USA, we find R ≈ 2.7 and x− ≈ 0.8, implying that about 20% of the population was
0
already immune before that wave, plausibly as a result of infection during the spring
1918 herald wave.
Keywords: epidemic momentum, prior immunity, epidemic inference, basic reproduction
number, 1918 influenza pandemic
1 Introduction
Epidemic time series are commonly used to infer how well an infection spreads, as measured
by the basic reproduction number, R —the expected number of secondary infections caused
0
by a typical infected individual in a fully susceptible population. A standard approach
estimates the initial exponential growth rate and combines it with an estimated or assumed
distribution of intrinsic generation intervals—the delays between infection of an individual
and the secondary infections caused by that individual—to obtain a reproduction number
[1, 2, 3]. More precisely, if x− is the fraction of the population that was susceptible before
the epidemic began, initial growth identifies the effective reproduction number R = R x−,
eff 0
∗Department of Mathematics & Statistics and M.G. DeGroote Institute for Infectious Disease Re-
search, McMaster University, 1280 Main Street West, Hamilton, Ontario, L8S 4K1, Canada. Email:
earn@math.mcmaster.ca. ORCID: 0000-0002-7562-1341.
†LPSM, Sorbonne Université, CNRS UMR 8001, Paris 75005, France. ORCID: 0000-0002-2599-8415.
1
6202
luJ
22
]EP.oib-q[
1v75612.7062:viXra

rather than R [4]. Early growth alone does not separate pathogen transmissibility from
0
pre-existing population immunity, because different combinations of R and x− can give the
0
same R .
eff
The fraction of the population that was already immune when the epidemic began is
z− = 1−x−. Allowing for pre-existing immunity (x− < 1) changes both the transmissibility
inferred for the pathogen and the estimated proportion infected during the focal epidemic,
z+ = x− −x+, where x+ is the fraction susceptible after the epidemic. Thus, assuming that
the population was initially fully susceptible confounds the interpretation of transmissibility,
prior immunity, and final size.
Epidemic momentum [5] provides the additional information needed to separate R from
0
x−. Conceptually, epidemic momentum measures the infectious potential carried by the
population, weighting past infections by their remaining potential to transmit. It can be
constructed from an incidence time series and the intrinsic generation-interval distribution
g(α), where α is the time since infection. The susceptible fraction and epidemic momentum
satisfy a conservation law [5, Section 3(d)]; the value of the conserved quantity is yˆ, the
maximum epidemic momentum. Together with R = R x−, an estimate of yˆ supplies the
eff 0
additional relation needed to determine R and x− separately.
0
Inthispaper, weexploitepidemicmomentumtoinferR andx− separatelyfromthesame
0
epidemic time series. We assess this momentum-based method for inferring transmissibility
and prior immunity using stochastic epidemic simulations for which both quantities are
known, andthenapplyittotheautumnwaveofthe1918influenzapandemicinPhiladelphia.
The application illustrates the biological consequences of estimating, rather than assuming,
the population immunity present before an epidemic.
The inference proceeds from an observed incidence time series, or from a time series
from which incidence can be reconstructed (e.g., mortality [6]), together with an assumed
or estimated intrinsic generation interval distribution g(α). Initial exponential growth gives
R = R x−. The incidence history and g(α) then determine the epidemic momentum
eff 0
through time, from which we extract its maximum yˆ. Combining yˆ with the early growth
estimate separates R from x−; prior immunity and final size follow from the inferred sus-
0
ceptible fractions.
We first introduce the renewal-equation formulation of epidemic models, from which we
derive the relations underlying the momentum-based method. We then assess its accuracy
using stochastic simulations, apply it to main-wave data recorded in Philadelphia in 1918,
and discuss the biological interpretation and limitations of the inferences.
2 Methods
2.1 Kermack and McKendrick’s renewal equation
We formulate the momentum-based method using the renewal equation, which represents a
broad class of epidemic models without requiring a particular compartmental structure [7,
8, 9]. This formulation is particularly convenient for inference because it is written in terms
of incidence—the quantity observed, or reconstructed, from an epidemic time series—and
the intrinsic generation-interval distribution, which must already be estimated or assumed
2

to convert an epidemic growth rate into a reproduction number [1].
We measure time in units of a convenient epidemiological timescale, often the mean
infectious period, so that τ is dimensionless and the equations can be written in terms of
R rather than separate transmission and recovery-rate parameters. We write X(τ) for the
0
susceptible fraction at time τ, and ι(τ) for the incidence, the fraction of the population
newly infected per unit time. The probability density g(α) specifies the distribution of
the intrinsic generation interval, the delay between infection of an individual and a
secondary infection caused by that individual [10, 11]. In dimensionless time, the renewal
| equation | is  |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- |
dX
|     |     |     | =   | −ι(τ), |     |     | (2.1a) |
| --- | --- | --- | --- | ------ | --- | --- | ------ |
dτ
Z τ
|     |     |     | ι(τ) = | R X(τ) | ι(s)g(τ −s)ds. |     | (2.1b) |
| --- | --- | --- | ------ | ------ | -------------- | --- | ------ |
0
−∞
The first equation identifies incidence with the rate at which susceptibles are depleted. In
the second equation, infections that occurred at time s contribute to incidence at time τ
according to the generation-interval density evaluated at their infection age, τ − s. The
| factor | R X(τ) is the | effective | reproduction | number | at time | τ.  |     |
| ------ | ------------- | --------- | ------------ | ------ | ------- | --- | --- |
0
In the framework represented by Eq. (2.1), differences in infection-age structure among
epidemic models are captured by g(α). Standard examples of generation-interval distribu-
tions, including those corresponding to the SIR and SEIR models, are given in Table 1.
Other choices of g(α) represent models with more general infection-age structure [9]. A
fuller account of the renewal equation, its initial history, and its relation to compartmental
| models | is given in | [5, Section | 2(e)]. |     |     |     |     |
| ------ | ----------- | ----------- | ------ | --- | --- | --- | --- |
The lower limit of integration in Eq. (2.1b) makes explicit that incidence at time τ de-
pends on the preceding incidence history. This history enters the inference in two ways.
First, exponentially growing incidence in the early epidemic tail yields the Euler–Lotka rela-
tion that identifies R = R x−. Second, the incidence history and g(α) determine epidemic
eff 0
momentum, which weights past infections by their remaining reproductive potential. In
practice, observations begin at a finite time, but the early exponential approximation also
allows the unobserved part of the incidence history to be included in the momentum calcula-
tion. We begin with the relationship between the asymptotic exponential growth and decay
| rates and | transmissibility. |     |                  |     |         |     |     |
| --------- | ----------------- | --- | ---------------- | --- | ------- | --- | --- |
| 2.2       | Tail exponents    |     | and reproduction |     | numbers |     |     |
In the initial (τ → −∞) and final (τ → +∞) phases of an epidemic, incidence grows and
decays exponentially,
|     |     |     |     | ι(τ) ∝ | eλ±τ, |     | (2.2) |
| --- | --- | --- | --- | ------ | ----- | --- | ----- |
where λ− > 0 applies near the start of the epidemic and λ+ < 0 applies near the end; we refer
to λ± as the tail exponents. During these early and late phases, incidence is small and
the susceptible fraction is nearly constant, at x− and x+, respectively. Substituting Eq. (2.2)
into Eq. (2.1b), rearranging, and cancelling common factors gives the Euler–Lotka equation
| [12, 13, | 14], |      |     |             |            |       |       |
| -------- | ---- | ---- | --- | ----------- | ---------- | ----- | ----- |
|          |      | 1    | Z ∞ |             |            |       |       |
|          |      |      | =   | e−λ±αg(α)dα | ≡ L[g](λ±) | ≡ L . | (2.3) |
|          |      | R x± |     |             |            | ±     |       |
|          |      | 0    | 0   |             |            |       |       |
3

For the initial growth phase, setting x− = 1 in Eq. (2.3) gives the formula of Wallinga and
Lipsitch [1, Equation (2.7)], which is often used with empirical estimates of λ− to infer R
0
[1, 2, 3]. If x− < 1, the same calculation instead yields R = R x− [4].
|     |     |     |     |     |     |     | eff | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Estimating x− empirically is sometimes possible (e.g., [15]). Computationally demanding
and/or model-specific methods that attempt to infer or constrain x− indirectly from the
observed epidemic data have also been proposed (see Section 4.1). Our approach obtains the
additional information directly from epidemic momentum, which we now define precisely.
| 2.3 | Constructing |     | epidemic |     | momentum |     | from | incidence |     |     |
| --- | ------------ | --- | -------- | --- | -------- | --- | ---- | --------- | --- | --- |
At infection age α, the upper tail of the generation-interval distribution is the fraction of an
individual’s intrinsic transmission potential that remains. Multiplying this fraction by R ,
0
| we define | the reduced |     | reproduction |     | number |     |     |     |     |     |
| --------- | ----------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- |
Z ∞
|     |     |     |     | R   | = R | g(α′)dα′. |     |     |     | (2.4) |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ----- |
|     |     |     |     |     | α   | 0         |     |     |     |       |
α
Thus R is the expected number of future secondary infections caused by an individual
α
of infection age α in a fully susceptible population, while R /R is the fraction of that
|     |     |     |     |     |     |     |     | α 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
individual’s reproductive potential that remains (which depends only on g(α), not R ).
0
At time τ, the cohort infected at time τ −α contributes ι(τ −α)dα to the infection-age
distribution. Weighting each cohort by its remaining reproductive potential we obtain the
| epidemic | momentum |     | [5], |     |     |     |     |     |     |     |
| -------- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|          |          |     |      |     | Z   |     | R   |     |     |     |
∞
|     |     |     |     | Y(τ) | =   | ι(τ −α) | α dα. |     |     | (2.5) |
| --- | --- | --- | --- | ---- | --- | ------- | ----- | --- | --- | ----- |
|     |     |     |     |      | 0   |         | R     |     |     |       |
0
For the SIR and SEIR models, epidemic momentum coincides with the total prevalence
of infection. More generally, epidemic momentum is a weighted prevalence: each currently
infectedindividualcontributesaccordingtotheirremainingpotentialtoinfect, soindividuals
| at different | infection |     | ages carry | different | weights. |     |     |     |     |     |
| ------------ | --------- | --- | ---------- | --------- | -------- | --- | --- | --- | --- | --- |
An equivalent representation is useful when epidemic observations are expressed as cu-
Rτ
mulative incidence. Writing ι(τ) = ι(s)ds and integrating Eq. (2.5) by parts, using
−∞
d
| (R   | /R ) = −g(α), |     | gives |     |     |     |     |     |     |     |
| ---- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| dα α | 0             |     |       |     |     |     |     |     |     |     |
Z ∞
|     |     |     | Y(τ) | =   | ι(τ)− | ι(τ −α)g(α)dα. |     |     |     | (2.6) |
| --- | --- | --- | ---- | --- | ----- | -------------- | --- | --- | --- | ----- |
0
Thus epidemic momentum can be computed either directly from incidence using Eq. (2.5),
or from the corresponding cumulative-incidence curve using Eq. (2.6).
Bothrepresentationsformallyinvolvethecompleteincidencehistory. Inpractice,suppose
observations begin at time τ during the initial exponential-growth phase, with ι(τ) = ι.
|     |     |     |     | i   |     |     |     |     |     | i i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ιeλ−(s−τi).
Incidence before τ can then be approximated by ι(s) ≈ Splitting Eq. (2.5) into
|                   |      | i      |            |         |        |            | i      |         |       |       |
| ----------------- | ---- | ------ | ---------- | ------- | ------ | ---------- | ------ | ------- | ----- | ----- |
| the contributions |      | before | and        | after τ | gives, | for τ ≥ τ, |        |         |       |       |
|                   |      |        |            |         | i      |            | i      |         |       |       |
|                   |      |        |            | Z       | ∞      | R          | Z τ−τi |         | R     |       |
|                   |      |        | ιeλ−(τ−τi) |         | e−λ−α  |            |        |         |       |       |
|                   | Y(τ) | ≈      |            |         |        | α dα       | +      | ι(τ −α) | α dα. | (2.7) |
|                   |      |        | i          |         |        | R          |        |         | R     |       |
|                   |      |        |            | τ−τi    |        |            | 0      |         |       |       |
|                   |      |        |            |         |        | 0          |        |         | 0     |       |
4

The first term in Eq. (2.7) reconstructs the contribution from infections that occurred be-
fore observations began, while the second is computed directly from the observed incidence
history. A Laplace-transform representation of the first term, including the explicit SEIR
| expressions | used | in our | calculations, |     | is  | derived in Section | A.  |     |     |
| ----------- | ---- | ------ | ------------- | --- | --- | ------------------ | --- | --- | --- |
Consequently, the observed incidence curve, its initial growth rate λ−, and the generation-
interval distribution g(α) determine the epidemic momentum throughout the observed epi-
demicand, inparticular, itsmaximumyˆ. WenextcombinethisinformationwithR = R x−
eff 0
| to infer | R and | x− separately. |     |     |     |     |     |     |     |
| -------- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
0
| 2.4 Inferring |     | R   | and | prior |     | population | immunity | using epidemic |     |
| ------------- | --- | --- | --- | ----- | --- | ---------- | -------- | -------------- | --- |
0
momentum
The preceding subsections provide the two quantities needed to separate R from x−. First,
0
L
the rising tail exponent λ− and the generation-interval distribution g(α) determine and
−
1/L
hence R = R x− = [Eq. (2.3)]. Second, the incidence history and g(α) determine the
|     | eff 0 |     | −   |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
epidemicmomentumY(τ)[Eq.(2.5)]andhenceitsmaximumyˆ. Wenowusetheconservation
fromyˆandL
lawpresentedinRef.[5]toinferR ,andtheninferthepre-epidemicsusceptible
|          |         |     |       |     | 0   | −   |     |     |     |
| -------- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- |
| fraction | x− from | R = | R x−. |     |     |     |     |     |     |
|          |         | eff | 0     |     |     |     |     |     |     |
The quantity that is conserved along epidemic trajectories is a function of susceptible
fraction and epidemic momentum, and can be written [5, Section 3(d)]
(cid:18)x(cid:19)
|     |     |     |     |     | C(x,y) | = y +xˆV | ,   |     | (2.8) |
| --- | --- | --- | --- | --- | ------ | -------- | --- | --- | ----- |
xˆ
1
where V(u) = u−1−lnu is the “Volterra function” [16] and xˆ = . The conserved value
R
0
| of C is the | maximum | epidemic |     | momentum,   |     |          |                   |     |       |
| ----------- | ------- | -------- | --- | ----------- | --- | -------- | ----------------- | --- | ----- |
|             |         |          |     | (cid:16)    |     | (cid:17) | (cid:16) (cid:17) |     |       |
|             |         |          |     | C X(τ),Y(τ) |     | = C      | xˆ,yˆ = yˆ.       |     | (2.9) |
At the pre- and post-epidemic endpoints, X = x± and Y = 0. Consequently, yˆ= C(x±,0) =
| 1 V(R | x±). Since | Eq. | (2.3) | gives | R x± | = 1/L , we | obtain |     |     |
| ----- | ---------- | --- | ----- | ----- | ---- | ---------- | ------ | --- | --- |
| R 0   |            |     |       |       | 0    | ±          |        |     |     |
0
|     |     |     |     |     |     | (cid:18) | (cid:19) |     |        |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ------ |
|     |     |     |     |     |     | 1 1      |          |     |        |
|     |     |     |     |     | R   | = V      | .        |     | (2.10) |
L
|     |     |     |     |     | 0   | yˆ  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
±
Thus either epidemic tail provides an exact expression for R in terms of its tail exponent,
0
λ− or λ+, the generation interval distribution g(α), and the maximum epidemic momentum
yˆ, with no dependence on the pre-epidemic susceptible fraction x−.
For inference from the initial growth phase, we use L = L in Eq. (2.10). Then Eq. (2.3)
± −
gives
|     |     |      |     | 1   |     |      |           | 1   |        |
| --- | --- | ---- | --- | --- | --- | ---- | --------- | --- | ------ |
|     |     | x− = |     |     | and | z− = | 1−x− = 1− | .   | (2.11) |
|     |     |      |     | L   |     |      |           | L   |        |
|     |     |      | R   |     |     |      | R         |     |        |
|     |     |      |     | 0 − |     |      |           | 0 − |        |
Hence estimates of λ− and yˆ, together with g(α), determine both pathogen transmissibility
| (R ) and | prior population |     | immunity |     | (z−). |     |     |     |     |
| -------- | ---------------- | --- | -------- | --- | ----- | --- | --- | --- | --- |
0
The falling tail exponent λ+ is difficult to estimate because the asymptotic decay occurs
when incidence is very low. However, it is not necessary to observe the falling tail in order
5

to estimate the final size of the epidemic. Applying Eq. (2.10) to the two endpoints gives
|              |               |        | (cid:18)      | (cid:19) (cid:18) | (cid:19) |        |
| ------------ | ------------- | ------ | ------------- | ----------------- | -------- | ------ |
|              |               |        |               | 1                 | 1        |        |
|              |               |        | V             | = V               | .        | (2.12) |
|              |               |        | L             | L                 |          |        |
|              |               |        |               | −                 | +        |        |
| The solution | corresponding | to the | post-epidemic | endpoint          | is       |        |
|              |               |        | 1             | (cid:18)          | (cid:19) |        |
1 e−1/L
|     |     |     | =   | −W − | − , | (2.13) |
| --- | --- | --- | --- | ---- | --- | ------ |
|     |     |     | L   | + L  |     |        |
−
+
where W is the principal branch of Lambert’s W function (Section C). Since x+ = 1/(R L ),
|     | +   |     |     |     |     | 0 + |
| --- | --- | --- | --- | --- | --- | --- |
the proportion infected during the focal epidemic—the final size—is therefore
|     |     |      |        |     | !   |        |
| --- | --- | ---- | ------ | --- | --- | ------ |
|     |     |      |        | 1   | 1 1 |        |
|     |     | z+ = | x− −x+ | =   | − . | (2.14) |
|     |     |      |        | R   | L L |        |
|     |     |      |        | 0   | − + |        |
Operationally, we estimate λ− from the initial exponential-growth phase, evaluate L ,
−
construct Y(τ) from the incidence history, and identify its maximum yˆ. Equations (2.10)
and (2.11) determine R , x−, and z−. Equation (2.13) then determines L , and Eq. (2.14)
0 +
gives z+; the post-epidemic susceptible fraction follows from x+ = x− − z+. Observations
must extend long enough to estimate the maximum of epidemic momentum, but need not
| extend into | the asymptotic | falling | tail. |     |     |     |
| ----------- | -------------- | ------- | ----- | --- | --- | --- |
L
The absolute scale of the incidence curve is required because yˆ, unlike λ− and , depends
−
on that scale. Multiplying incidence by a constant multiplies Y(τ) and yˆ by the same
constant, and therefore changes the value of R inferred from Eq. (2.10). Incidence must
0
therefore be expressed as a fraction of the population, or the factor connecting the observed
time series to incidence must be known or examined explicitly, as in the influenza mortality
| application | below. |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- |
3 Results
3.1 Estimates of prior immunity and R from stochastic simula-
0
tions
We assessed the momentum-based method using stochastic SEIR simulations for which R
0
and the pre-epidemic susceptible fraction x− were known. The simulations spanned a wide
range of R for several combinations of x− and population size N, allowing us to examine
0
the effects of demographic stochasticity on each stage of the inference.
Themethodfirstestimatestheinitialgrowthrateλ− fromtherisingtailandconstructsthe
epidemicmomentumfromincidencetoestimateitsmaximumyˆ. (Detailsofthecomputation,
including estimating initial conditions, are given in Section A.) Figure 1 shows the relative
errors in these two quantities. Inserting the estimated values of λ− and yˆ into Eqs. (2.10)
and (2.11) gives the corresponding estimates of R and x−, shown in Fig. 2.
0
In the upper panels of Fig. 2, grey squares show the true values of x−. The estimated
values are distributed around the corresponding true values across the simulated parameter
combinations, with greater stochastic variation in smaller populations. The lower panels
6

|        |          | λ−       | 105)  |        |          | λ−       |     | 106)  |
| ------ | -------- | -------- | ----- | ------ | -------- | -------- | --- | ----- |
|        | Relative | error in | (N =  |        | Relative | error in | (N  | =     |
| 0.10   |          |          |       | 0.10   |          |          |     |       |
| 0.05   |          |          |       | 0.05   |          |          |     |       |
| −λ/−λ∆ |          |          |       | −λ/−λ∆ |          |          |     |       |
| 0.00   |          |          |       | 0.00   |          |          |     |       |
| -0.05  |          |          |       | -0.05  |          |          |     |       |
| -0.10  |          |          |       | -0.10  |          |          |     |       |
|        | 5 10     | 15 20    | 25 30 |        | 5 10     | 15       | 20  | 25 30 |
Relative error in yˆ (N = 105) Relative error in yˆ (N = 106)
|       |     | R      |     |       |     | R    |     |     |
| ----- | --- | ------ | --- | ----- | --- | ---- | --- | --- |
| 0.015 |     | True 0 |     | 0.015 |     | True | 0   |     |
x
| 0.010        |      |       |       | 0.010        |      |     | i       |       |
| ------------ | ---- | ----- | ----- | ------------ | ---- | --- | ------- | ----- |
|              |      |       |       |              |      | 0.6 | 0.7 0.8 | 0.9   |
| ˆy/ˆy∆ 0.005 |      |       |       | ˆy/ˆy∆ 0.005 |      |     |         |       |
| 0.000        |      |       |       | 0.000        |      |     |         |       |
| -0.005       |      |       |       | -0.005       |      |     |         |       |
| -0.010       |      |       |       | -0.010       |      |     |         |       |
| -0.015       |      |       |       | -0.015       |      |     |         |       |
|              | 5 10 | 15 20 | 25 30 |              | 5 10 | 15  | 20      | 25 30 |
True basic reproduction number R 0 True basic reproduction number R 0
|     |     | True R |     |     |     | True R |     |     |
| --- | --- | ------ | --- | --- | --- | ------ | --- | --- |
|     |     | 0      |     |     |     |        | 0   |     |
Figure 1: Estimates of initial growth rate λ− and peak epidemic momentum yˆ
from stochastic SEIR simulations. The top panels show the relative error in the initial
growth rate λ− as a function of the true R specified in the simulations (with population size
0
N = 105 on the left and N = 106 on the right). The exact value of λ− is given by the SEIR
row in Table 1. Simulations were carried out with equal mean latent and infectious periods
(ℓ = 1) and incidence time series were obtained by “observing” five times per infectious
period, corresponding to daily data for a disease with a five day infectious period. Realistic
initialconditionswerechosenbyensuringapproximateagreementwiththeinitialexponential
growth phase of the SEIR ODEs. Estimates of λ− were obtained by applying the R package
epigrowthfit [2, 17, 18] to the simulated incidence time series. The second row of panels shows
the relative error in the peak epidemic momentum (yˆ, the exact value of which is given by
Y(xˆ) in [5, Eq. (2.4)]); the epidemic momentum Y(τ) was estimated by convolving the
simulated cumulative incidence ι(τ) with the generation interval distribution g(α) [Eq. (2.6)
and Table 1]. A small systematic underestimate in yˆ is evident, but the magnitude of the
relative error in yˆ is an order of magnitude smaller than the magnitude of the relative error
in λ−, so the systematic error has a negligible effect on the estimate of R .
0
7

x−
|           |     |      | Pre-epidemic |     | susceptible |           | proportion |      |     |     |       |
| --------- | --- | ---- | ------------ | --- | ----------- | --------- | ---------- | ---- | --- | --- | ----- |
|           | 1.0 |      |              | 105 |             | 1.0       |            |      |     | 106 |       |
|           |     |      | N =          |     |             |           |            |      | N = |     |       |
|           | 0.9 |      |              |     |             | 0.9       |            |      |     |     |       |
| −x        |     |      |              |     |             | −x        |            |      |     |     |       |
|           | 0.8 |      |              |     |             | 0.8       |            |      |     |     |       |
| detciderP |     |      |              |     |             | detciderP |            |      |     |     |       |
|           | 0.7 |      |              |     |             | 0.7       |            |      |     |     |       |
|           | 0.6 |      |              |     |             | 0.6       |            |      |     |     |       |
|           | 0.5 |      |              |     |             | 0.5       |            |      |     |     |       |
|           |     | 5 10 | 15           | 20  | 25 30       |           |            | 5 10 | 15  | 20  | 25 30 |
True basic reproduction number R 0 True basic reproduction number R 0
|     |     |     |     | Basic | reproduction |     | number | R   |     |     |     |
| --- | --- | --- | --- | ----- | ------------ | --- | ------ | --- | --- | --- | --- |
0
|     | 30        |            | 30  |        |            | 30  |        |            | 30  |        |            |
| --- | --------- | ---------- | --- | ------ | ---------- | --- | ------ | ---------- | --- | ------ | ---------- |
|     | N=105     |            |     | N=105  |            |     | N=105  |            |     | N=105  |            |
|     | 25 xi=0.6 |            | 25  | xi=0.7 |            | 25  | xi=0.8 |            | 25  | xi=0.9 |            |
|     | 20        |            | 20  |        |            | 20  |        |            | 20  |        |            |
|     | 15        |            | 15  |        |            | 15  |        |            | 15  |        |            |
|     | 10        |            | 10  |        |            | 10  |        |            | 10  |        |            |
| 0   | 5         | viaλ−andyˆ | 5   |        | viaλ−andyˆ | 5   |        | viaλ−andyˆ | 5   |        | viaλ−andyˆ |
| R   |           | viaλ−only  |     |        | viaλ−only  |     |        | viaλ−only  |     |        | viaλ−only  |
|     | 0         |            | 0   |        |            | 0   |        |            | 0   |        |            |
detciderP
|     | 0 5       | 10 20      | 30  | 0 5 10 | 20 30      |     | 0 5    | 10 20 30   |     | 0 5    | 10 20 30   |
| --- | --------- | ---------- | --- | ------ | ---------- | --- | ------ | ---------- | --- | ------ | ---------- |
|     | 30        |            | 30  |        |            | 30  |        |            | 30  |        |            |
|     | N=106     |            |     | N=106  |            |     | N=106  |            |     | N=106  |            |
|     | 25 xi=0.6 |            | 25  | xi=0.7 |            | 25  | xi=0.8 |            | 25  | xi=0.9 |            |
|     | 20        |            | 20  |        |            | 20  |        |            | 20  |        |            |
|     | 15        |            | 15  |        |            | 15  |        |            | 15  |        |            |
|     | 10        |            | 10  |        |            | 10  |        |            | 10  |        |            |
|     |           | viaλ−andyˆ |     |        | viaλ−andyˆ |     |        | viaλ−andyˆ |     |        | viaλ−andyˆ |
|     | 5         |            | 5   |        |            | 5   |        |            | 5   |        |            |
|     |           | viaλ−only  |     |        | viaλ−only  |     |        | viaλ−only  |     |        | viaλ−only  |
|     | 0         |            | 0   |        |            | 0   |        |            | 0   |        |            |
|     | 0 5       | 10 20      | 30  | 0 5 10 | 20 30      |     | 0 5    | 10 20 30   |     | 0 5    | 10 20 30   |
|     |           |            |     |        | True       | R   |        |            |     |        |            |
0
Figure 2: Prior population immunity (z− = 1−x−) and basic reproduction number
(R ) estimated from stochastic SEIR simulations. Exploiting the epidemic momen-
0
tum, we successfully disentangle and accurately estimate both z− and R . The top panels
0
show the predicted pre-epidemic susceptible proportion x−, so the pre-existing level of pop-
ulation immunity is z− = 1 − x− [estimated via Eq. (2.11)]. The true x− associated with
the deterministic skeleton of the model [computed via Eq. (2.11) using the exact value of
λ− from Table 1] is indicated with grey squares. Symbols and colours are associated with
the initial susceptible proportion x as in Fig. 1. The bottom panels show the predicted R
|     |     |     |     | i   |     |     |     |     |     |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
from the same simulations. The smaller symbols show the value of R estimated using the
0
uncorrected Wallinga-Lipsitch (WL) formula [1], which uses only the estimated growth rate
λ−, whereas the larger symbols show R as estimated using Eq. (2.10), which uses both λ−
0
and the estimated peak epidemic momentum yˆ. The grey line corresponds to “Predicted
8
| R   | = True | R ”. |     |     |     |     |     |     |     |     |     |
| --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |        | 0    |     |     |     |     |     |     |     |     |     |

show the estimates of R , which similarly lie close to the line of perfect agreement, with
0
| accuracy | improving |     | as population |     | size increases. |     |     |     |
| -------- | --------- | --- | ------------- | --- | --------------- | --- | --- | --- |
For comparison, the smaller symbols in the lower panels show the reproduction numbers
obtained from the initial growth rate under the assumption that the population was initially
fully susceptible (x− = 1). When pre-existing immunity is present, these values are system-
atically smaller than the true R , because the initial growth rate identifies R = R x− rather
|        |     |     |     | 0   |     |     | eff 0 |     |
| ------ | --- | --- | --- | --- | --- | --- | ----- | --- |
| than R | .   |     |     |     |     |     |       |     |
0
All simulations shown in Figs. 1 and 2 had equal mean latent and infectious periods
(ℓ = 1 in Eq.(T6)); the performance of the method was similar for other values of ℓ.
3.2 Reappraisal of the 1918 influenza pandemic in Philadelphia
Having shown that the momentum-based method recovers known values of R and x− from
0
stochastic simulations, we applied it to daily pneumonia and influenza (P&I) mortality
recorded during the main wave of the 1918 influenza pandemic in Philadelphia, which oc-
| curred | in the | autumn | of 1918 | (Fig. | 3). |     |     |     |
| ------ | ------ | ------ | ------- | ----- | --- | --- | --- | --- |
Because mortality rather than incidence was reported, we used Richardson–Lucy decon-
volution to reconstruct a curve proportional to incidence [6]. (Details of the mortality data,
the infection-to-death distribution used for deconvolution, the generation-interval assump-
tions, and the calculation of epidemic momentum are given in the caption to Fig. 3.) The
proportionality factor includes the case-fatality proportion, CFP, because only that fraction
of infections resulted in recorded deaths. This unknown scale does not affect the estimated
| initial | growth | rate | [2, 17, 18], | which | was λ− | ≃ 0.16/day. |     |     |
| ------- | ------ | ---- | ------------ | ----- | ------ | ----------- | --- | --- |
Following Mills et al. [24], we assumed mean latent and infectious periods of T =
lat
1.9days and T = 4.1days, respectively, hence ℓ ≡ T /T = 0.463. Measuring time
|     |     | inf |     |     |     |     | lat inf |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- |
in units of T gives λ− ≈ 0.655. The corresponding SEIR generation-interval distribution
inf
| [Table | 1] then | yields |     |     |     |     |     |     |
| ------ | ------- | ------ | --- | --- | --- | --- | --- | --- |
L
|     |     |     |     |     | ≈   | 0.464. |     | (3.1) |
| --- | --- | --- | --- | --- | --- | ------ | --- | ----- |
−
This estimate gives a lower bound on R that is independent of the incidence scale: since
0
| x− ≤ 1, | we have | R   | ≥ R , | so Eq. | (2.3) implies |     |     |     |
| ------- | ------- | --- | ----- | ------ | ------------- | --- | --- | --- |
0 eff
1
|     |     |     |     |     | R ≥ | ≈   | 2.16. | (3.2) |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- |
0 L
−
Convolving the reconstructed incidence curve with the remaining reproductive-potential
kernel[Eq.(2.4)]givestheepidemicmomentum[Eq.(2.5)]showninFig.3. Becauseepidemic
momentum is linearly related to incidence, the multiplicative factor CFP is retained in the
reconstructed momentum curve; its maximum is therefore CFP × yˆ, rather than yˆ. For
| mortality | data, | Eq. | (2.10) | is therefore | more | usefully | written             |       |
| --------- | ----- | --- | ------ | ------------ | ---- | -------- | ------------------- | ----- |
|           |       |     |        |              | CFP  |          | (cid:18) 1 (cid:19) |       |
|           |       |     |        |              | R =  |          | V .                 | (3.3) |
L
|     |     |     |     |     | 0 CFP×yˆ |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- |
−
| The momentum |     | curve | in Fig. | 3   | gives  |            |     |       |
| ------------ | --- | ----- | ------- | --- | ------ | ---------- | --- | ----- |
|              |     |       |         |     | CFP×yˆ | ≈ 0.00287, |     | (3.4) |
9

10-1
10-2
10-3
10-4
10-5
10-6
Sep Oct Nov Dec
atad
yliad
Pneumoniaandinfluenza
observeddeathspercapita
reconstructedincidence
epidemicmomentum
Figure 3: 1918 influenza pandemic in Philadelphia, USA. Daily deaths from pneu-
monia and influenza (P&I) were recorded from 1 September to 31 December 1918 [19]. We
deconvolved the observed mortality time series to obtain estimated daily incidence ι(t), us-
ing an empirically estimated infection to death distribution: as detailed in previous work [6]
and implemented in the fastbeta R package [20, 21], gamma distributions were fitted to an
empirical incubation period distribution [22, Figure 1] and an empirical symptom onset to
death distribution [23, Chart 2], which were then convolved to obtain the infection to death
distribution. We then convolved the estimated ι(t) with the estimated reduced reproduction
number [Eq. (2.4)] (via g(α) from Table 1 with ℓ = 0.463) to obtain the epidemic momentum
time series Y(t) [Eq. (2.5)]. The peak of the observed daily P&I mortality occurred on 11
October 1918 (with 803 P&I deaths), whereas estimated incidence peaked on 29 Septem-
ber 1918 and estimated epidemic momentum peaked on 1 October 1918 (vertical grey line).
Note that peak momentum always occurs after peak incidence (see Section B). Associated
estimates of R and population immunity are discussed in the main text in Section 3.2.
0
so that
R ≈ 135×CFP. (3.5)
0
The lower bound on R given in Eq. (3.2) therefore implies a CFP lower bound,
0
R 2.16
CFP ≈ 0 ≳ = 1.6%. (3.6)
135 135
Frost [25, p.593] estimated that the case-fatality proportion during the main wave of the
1918 pandemic ranged from 0.8% to 3.1% across US cities. For a group of northeastern com-
munities near Philadelphia, he estimated CFP = 2.05% [25, p.593], consistent with the lower
bound in Eq. (3.6). We therefore use CFP ≃ 2% as a representative value for Philadelphia.
Substitution into Eq. (3.5) implies
R ≈ 2.71. (3.7)
0
Equation (2.11) then gives
z− ≈ 0.203, (3.8)
indicating that approximately 20% of the population was immune before the main wave.
10

Mills et al. [24] also assumed CFP = 2%, based on the midpoint of Frost’s range [25],
but assumed prior population immunity z− = 30% from seasonal-influenza evidence [24,
pp.905–906] (the relevant passages are reproduced in Section D). They reported
1.7 ≤ R ≤ 2.4 (3.9)
0
for Philadelphia [24, SI p.5]. However, using the observed initial growth rate and the SEIR
generation-interval distribution assumed both here and by Mills et al., z− = 0.3 would imply
1
R = ≈ 3.08, (3.10)
0 (1−z−)L
−
which lies outside their reported range. Thus their stated assumption about prior immunity
and their reported estimate of R are not mutually consistent under Eq. (2.11).
0
Our momentum-based analysis instead estimates R and z− consistently from the ob-
0
served initial growth and reconstructed momentum curve. The estimate in Eq. (3.8) suggests
that a substantial fraction (20%) of the Philadelphia population was already immune before
the main wave, plausibly because of infection during the spring 1918 “herald wave”.
4 Discussion
Initial epidemic growth does not, by itself, distinguish pathogen transmissibility from pre-
existing population immunity. Rather, it identifies the effective reproduction number R =
eff
R x−, the product of the basic reproduction number and the fraction of the population
0
susceptible before the epidemic began [4]. Consequently, different combinations of R and
0
x− can generate the same initial growth. We have shown that epidemic momentum provides
the additional information needed to separate these quantities. Together, the initial growth
rate (tail exponent) and maximum epidemic momentum determine R and x−, from which
0
prior immunity (z−) and the proportion infected during the focal epidemic (z+) follow.
The momentum-based method successfully recovered both R and x− from stochastic
0
SEIR simulations across the parameter combinations examined (Figs. 1 and 2). As expected,
stochastic variation was greater in smaller populations, but the estimates were distributed
around the corresponding true values. By contrast, estimates obtained from the initial
growth rate while assuming x− = 1 were systematically smaller than the true R whenever
0
pre-existing immunity was present. These estimates are not intrinsically inaccurate: they
estimate R = R x−, rather than R . The error arises when R is interpreted as the basic
eff 0 0 eff
reproduction number despite uncertainty about the initial susceptible fraction.
Our reappraisal of the 1918 influenza pandemic illustrates the biological importance of
this distinction. For the main wave in Philadelphia, which occurred in the autumn of 1918,
the observed initial growth and reconstructed epidemic momentum imply R ≈ 2.71 and
0
z− ≈ 0.203. Thus, approximately 20% of the population appears to have been immune
before the main wave began. Infection during the spring 1918 “herald wave” provides a
plausible explanation for at least some of this immunity, but other sources of pre-existing
immunity are also possible.
The Philadelphia analysis also illustrates the consequences of assuming prior immunity
rather than estimating it. Mills et al. [24] assumed z− = 30%, but the observed growth rate
11

and their assumed generation-interval distribution imply R ≈ 3.08, outside the range they
0
reported. Thus, their assumed prior immunity and reported estimate of R are not mutually
0
consistent under the standard relationship between epidemic growth, prior immunity, and
reproduction number given in Eq. (2.11). The broader point is not specific to this earlier
analysis: estimates of R obtained by fixing prior immunity necessarily inherit any error in
0
that assumption.
4.1 Relation to previous approaches
Previous attempts to infer transmissibility and prior immunity from epidemic time series
have generally required additional approximations, strong model assumptions, or external
information. Caley et al. [26] estimated the time-dependent effective reproduction number
during the multi-wave 1919 influenza epidemic in Sydney from hospitalization and mortality
data. They combined these estimates with cumulative incidence and a priori assumptions
about periods in which contact behaviour had returned to normal to separate susceptible
depletion from changes in contact rates. Their analysis suggested that more than 90%
of the population was initially susceptible and gave a preferred estimate R ≈ 1.8. The
0
inference of prior immunity depended on the assumed clinical attack rate, the reconstruction
ofthetime-dependentreproductionnumber, andthecorrectidentificationofperiodswithout
behavioural change.
Cope et al. [27] used approximate Bayesian computation to fit a climate-driven stochas-
tic epidemic model to seasonal influenza surveillance data from New South Wales. Their
posterior distribution showed a strong relationship between R and the initial susceptible
0
fraction: relatively high values of R were associated with low susceptibility, while their
0
product was much more tightly constrained. Thus, even with a substantially richer model
and observation process, the data did not sharply identify the two quantities separately.
Bergström et al. [28] proved that, in an SIR model with under-reporting and prior im-
munity, the transmission rate, reporting fraction, and initial immune fraction are not jointly
identifiable from reported incidence alone. They showed that identifiability can be restored
by supplementing reported incidence with an estimate of prior immunity or infection preva-
lence. Their analysis is restricted to the SIR model and assumes the final size of the epidemic
has been observed. Our approach, which applies to all models represented by the renewal
equation, instead exploits the fact that epidemic momentum peaks at xˆ = 1 so all required
R
0
information—including an estimate of peak momentum yˆ—can be inferred much earlier.
However, an unknown reporting fraction still determines the scale of epidemic momentum
and must be estimated or constrained; in the Philadelphia analysis, the corresponding un-
known scale is the case-fatality proportion.
4.2 Data requirements and statistical challenges
The momentum-based method requires an estimate of the intrinsic generation-interval dis-
tribution. This requirement is not unique to our method: the same distribution is already
needed to convert an epidemic growth rate into an effective reproduction number [1]. Nev-
ertheless, uncertainty or misspecification in g(α) affects both R and the reconstruction of
eff
epidemic momentum, and therefore propagates into estimates of R and x−. Applications
0
12

shouldthereforebemindfulofsensitivitytotheassumedformandparametersoftheintrinsic
generation-interval distribution.
The absolute scale of incidence is also required for point estimates of R and x−. Multi-
0
plying the incidence curve by a constant leaves its exponential growth rate unchanged but
multiplies epidemic momentum and its maximum by the same constant, thereby changing
the inferred R . Incidence must therefore be expressed as a fraction of the population, or the
0
factor connecting the observed time series to incidence must be known or estimated. Even
when this scale factor cannot be estimated reliably, the initial growth rate still provides a
useful lower bound on R . For Philadelphia, Eq. (3.2) gives R ≳ 2.16, independently of the
0 0
assumed case-fatality proportion.
Mortality, hospital admissions, and other delayed observations require reconstruction of
the underlying incidence curve. This reconstruction depends on the relevant delay distri-
bution and may introduce additional uncertainty. The unobserved incidence history before
observations begin must also be approximated, although the initial exponential phase pro-
vides a natural extrapolation [Section A].
Peak epidemic momentum occurs after peak incidence [Section B], but this does not
imply that the entire rise to yˆ must be observed before a useful estimate can be made.
As an epidemic unfolds, provisional estimates of the eventual maximum yˆ, and hence of
R and x−, should become progressively more informative. Moreover, when incidence is
0
reconstructedfromadelayedobservablesuchashospitalizationormortality,ausefulestimate
of peak momentum may be available well before the observed time series reaches its peak, as
illustrated by Fig. 3. An important statistical challenge will be to develop robust confidence
intervalsforR andx− andtodeterminehowtheyimproveasmoreofanepidemicisobserved.
0
4.3 Model assumptions and extensions
The derivations in this paper assume mass-action incidence, so that susceptibility enters
incidence linearly through the susceptible fraction of the population. Individual differences
in intrinsic susceptibility, contact rate, and other mechanisms can instead produce nonlin-
ear dependence of incidence on the susceptible fraction [29, 30, 31, 32]. In that case, the
conserved quantity and inference formulae derived here must be modified.
We have extended the epidemic-momentum framework to incidence that depends non-
linearly on susceptible fraction, and derived the corresponding conserved quantity in this
more general setting [33]. This class provides one way to incorporate nonlinear effects of
susceptibility without explicitly tracking population structure [32]. More detailed forms of
host heterogeneity may instead require structured models that distinguish among host types.
The present analysis also assumes that the underlying transmissibility and intrinsic
generation-interval distribution remain fixed over the period analysed. Behavioural change,
interventions, pathogen evolution, or changes in reporting can violate these assumptions and
break the conservation law [5, Appendix J]. Applications should therefore be restricted to
periods over which these assumptions are defensible, or would require the development of
extensions that account explicitly for time-varying transmission.
Finally, the method estimates the susceptible fraction relevant to the focal epidemic
but does not identify the biological source of prior immunity. Such immunity may arise
from previous infection with the same pathogen, cross-reactive immunity to related strains,
13

vaccination, or other differences in susceptibility. In the Philadelphia application, infection
during the spring herald wave is one plausible source, but other sources of pre-existing
| immunity | are possible. |     |     |     |
| -------- | ------------- | --- | --- | --- |
4.4 Conclusions
Epidemic growth reflects both pathogen transmissibility and the immunological state of the
population in which transmission occurs. Assuming that the population was initially fully
susceptible can therefore lead to substantial underestimation of R and misinterpretation
0
of epidemic final size. Epidemic momentum provides a way to separate these effects using
information contained in the same epidemic time series. By combining the initial growth
rate with the maximum epidemic momentum, the momentum-based method yields separate
estimates of R and prior population immunity while retaining the generality of the renewal-
0
| equation | framework. |     |     |     |
| -------- | ---------- | --- | --- | --- |
Ethics
This work did not require ethical approval from a human subject or animal welfare commit-
tee.
| Data | accessibility |     |     |     |
| ---- | ------------- | --- | --- | --- |
The 1918 pneumonia and influenza mortality data shown in Fig. 3 have been published
previously [6] and are available in the fastbeta R package [21]. R code that reproduces all
the figures will be included as supplementary material to the published version.
| Declaration |     | of  | AI use |     |
| ----------- | --- | --- | ------ | --- |
We used ChatGPT and OpenAI Codex to assist with R coding, LATEX coding, and lan-
guage editing. All scientific arguments, mathematical derivations, analyses, interpretations,
and conclusions were developed by the authors, who take full responsibility for the final
manuscript.
| Author       | contributions |           |           |                      |
| ------------ | ------------- | --------- | --------- | -------------------- |
| Both authors | contributed   |           | to all    | aspects of the work. |
| Competing    |               | interests |           |                      |
| We declare   | we have       | no        | competing | interests.           |
14

Funding
We were supported by the Fields Institute for Research in Mathematical Sciences; the con-
tentsofthispaperaresolelytheresponsibilityoftheauthorsanddonotnecessarilyrepresent
the official views of the Institute. DJDE was supported by an NSERC Discovery Grant.
Acknowledgements
We are grateful to Ben Bolker, Caroline Colijn, Jonathan Dushoff, Maya Earn, Mark Lewis,
Junling Ma, David Price, and Steve Walker for comments and discussions. Deterministic
and stochastic simulations, and deconvolution of mortality to incidence, were facilitated by
convenient functions in the fastbeta R package, written by Mikael Jagan.
APPENDICES
| A Epidemic |     |     | momentum |     |     | from |     | finite |     | incidence | history |     |
| ---------- | --- | --- | -------- | --- | --- | ---- | --- | ------ | --- | --------- | ------- | --- |
For τ ≥ τ, splitting Eq. (2.5) over infections that occurred before and after observations
i
began gives
|     |     |      |     | Z    |         |     |       | Z    |         |       |     |      |
| --- | --- | ---- | --- | ---- | ------- | --- | ----- | ---- | ------- | ----- | --- | ---- |
|     |     |      |     | ∞    |         | R   |       | τ−τi |         | R     |     |      |
|     |     | Y(τ) | =   |      | ι(τ −α) |     | α dα+ |      | ι(τ −α) | α dα. |     | (A1) |
|     |     |      |     |      |         | R   |       |      |         | R     |     |      |
|     |     |      |     | τ−τi |         |     | 0     | 0    |         | 0     |     |      |
The second integral is computed directly from the observed incidence history. During the
| initial exponential-growth |     |     |     | phase, | Eq. (2.2),         | with | ι(τ) | =   | ι, gives |     |     |      |
| -------------------------- | --- | --- | --- | ------ | ------------------ | ---- | ---- | --- | -------- | --- | --- | ---- |
|                            |     |     |     |        |                    |      |      | i   | i        |     |     |      |
|                            |     |     | ι(τ | −α)    | ≈ ιeλ−(τ−τi)e−λ−α, |      |      |     | α > τ    | −τ, |     | (A2) |
|                            |     |     |     |        | i                  |      |      |     |          | i   |     |      |
where the initial growth rate λ− is also estimated from the observed incidence time series
[2, 17, 18]. The first integral in Eq. (A1) is therefore approximated by
|     |     |     |     |     |            | Z ∞ |       | R   |     |     |     |      |
| --- | --- | --- | --- | --- | ---------- | --- | ----- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | ιeλ−(τ−τi) |     | e−λ−α | α   | dα. |     |     | (A3) |
i
R
|       |                |     |     |      |            | τ−τi |        | 0   |     |     |     |     |
| ----- | -------------- | --- | --- | ---- | ---------- | ---- | ------ | --- | --- | --- | --- | --- |
| Using | the definition |     | of  | R in | Eq. (2.4), | we   | obtain |     |     |     |     |     |
α
|     | Z   | ∞     | R   |      | Z ∞ |              |     | Z ∞ |            |     |     |     |
| --- | --- | ----- | --- | ---- | --- | ------------ | --- | --- | ---------- | --- | --- | --- |
|     |     | e−λ−α |     | α dα | =   | e−λ−(α+τ−τi) |     |     | g(α′)dα′dα |     |     |     |
R
|     | τ−τi |     |     | 0   | 0            |     |       | α+τ−τi |      |             |     |     |
| --- | ---- | --- | --- | --- | ------------ | --- | ----- | ------ | ---- | ----------- | --- | --- |
|     |      |     |     |     |              | Z   |       | Z      |      |             |     |     |
|     |      |     |     |     |              |     | ∞     |        | ∞    |             |     |     |
|     |      |     |     |     | = e−λ−(τ−τi) |     | e−λ−α |        | g(α′ | +τ −τ)dα′dα |     |     |
i
|     |     |     |     |     |              |     | 0   | α           |     |           |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | ----------- | --- | --------- | --- | --- |
|     |     |     |     |     |              | Z   | ∞Z  | α′          |     |           |     |     |
|     |     |     |     |     | = e−λ−(τ−τi) |     |     | e−λ−αdαg(α′ |     | +τ −τ)dα′ |     |     |
i
0 0
e−λ−(τ−τi)
Z ∞(cid:16) 1−e−λ−α′(cid:17)
|     |     |     |     |     | =   |     |     |     | g(α′ | +τ −τ)dα′ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- | --- |
i
λ−
0
e−λ−(τ−τi)
|     |     |     |     |     | =   |     | [L[g | ](0)−L[g |     | ](λ−)], |     | (A4) |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | ------- | --- | ---- |
|     |     |     |     |     |     |     |      | τ−τi     |     | τ−τi    |     |      |
λ−
15

where
|                |                     |     | g       | (α)  | = g(α+τ |     | −τ)       |     |     |     | (A5) |
| -------------- | ------------------- | --- | ------- | ---- | ------- | --- | --------- | --- | --- | --- | ---- |
|                |                     |     | τ−τi    |      |         |     | i         |     |     |     |      |
| is the shifted | generation-interval |     | kernel, | with | Laplace |     | transform |     |     |     |      |
Z ∞
L[g
|     |     |     | ](λ) | =   | e−λαg(α+τ |     | −τ)dα. |     |     |     | (A6) |
| --- | --- | --- | ---- | --- | --------- | --- | ------ | --- | --- | --- | ---- |
|     |     |     | τ−τi |     |           |     |        | i   |     |     |      |
0
Substituting Eq. (A4) into Eqs. (A1) and (A3) gives the finite-history representation
|     |      | ι        |          |     |      |         | Z τ−τi |         | R   |     |      |
| --- | ---- | -------- | -------- | --- | ---- | ------- | ------ | ------- | --- | --- | ---- |
|     | Y(τ) | ≈ i [L[g | ](0)−L[g |     |      | ](λ−)]+ |        | ι(τ −α) | α   | dα. | (A7) |
|     |      |          | τ−τi     |     | τ−τi |         |        |         |     |     |      |
|     |      | λ−       |          |     |      |         |        |         | R   |     |      |
|     |      |          |          |     |      |         | 0      |         | 0   |     |      |
Thefirsttermreconstructsthecontributionfrominfectionsthatoccurredbeforeobservations
began, while the second is calculated directly from the observed incidence history.
For the SEIR generation-interval distribution given in Table 1, the shifted Laplace trans-
form is
|     |     |     |    |     | " e−(τ−τi) |     | ℓe−(τ−τi)/ℓ# |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | ------------ | --- | --- | --- | --- |
1
|     |     |     |  |     |     | −   |      | ,   | ℓ ̸= 1, |     |     |
| --- | --- | --- | ------ | --- | --- | --- | ---- | --- | ------- | --- | --- |
|     |     |     |        | 1−ℓ | 1+λ |     | 1+ℓλ |     |         |     |     |
L[g
|     |     | ](λ) | =   |     |     |     |     |     |     |     | (A8) |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
τ−τi
|     |     |     |  | 1+(1 | + λ )( | τ −τ | )           |     |        |     |     |
| --- | --- | --- | ------ | ---- | ------ | ---- | ----------- | --- | ------ | --- | --- |
|     |     |     |        |      |        |      | i e−(τ−τi), |     |        |     |     |
|     |     |     |        |      |        |      |             |     | ℓ = 1. |     |     |
|     |     |     |        | (1   | + λ    | ) 2  |             |     |        |     |     |
It follows that the contribution from the unobserved incidence history is
|     |     |     |     |        | "   |          | ℓ2e−(τ−τi)/ℓ# |       |     |     |         |
| --- | --- | --- | --- | ------- | --- | -------- | ------------- | ----- | --- | --- | ------- |
|     |     |     |     |         | ι   | e−(τ−τi) |               |       |     |     |         |
|     |     |     |     |  | i   |          |               |       |     |     |         |
|     |     |     |     |         |     |          | −             |       | ,   |     | ℓ ̸= 1, |
|     |     |     |     | 1−      | ℓ   | 1+λ−     |               | 1+ℓλ− |     |     |         |
ι
i
| [L[g | ](0)−L[g |      | ](λ−)] | =       |          |      |     |         |        |     |        |
| ---- | -------- | ---- | ------ | ------- | -------- | ---- | --- | ------- | ------ | --- | ------ |
|      | τ−τi     | τ−τi |        |         |          |      |     | h       |        | i   |        |
| λ−   |          |      |        |  |          | 2+(τ | −τ  | ) + λ 1 | +(τ −τ | )   |        |
|      |          |      |        |         |          |      |     | i −     |        | i   |        |
|      |          |      |        | ι       | e−(τ−τi) |      |     |         |        | ,   | ℓ = 1. |
i
|     |     |     |     |     |     |     |     | ( 1 + λ − )2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
(A9)
These expressions allow the contribution from infections that occurred before τ to be cal-
i
culated directly in the SEIR examples, without numerical integration over an unobserved
| incidence       | history. |              |      |        |        |     |          |     |     |     |     |
| --------------- | -------- | ------------ | ---- | ------ | ------ | --- | -------- | --- | --- | --- | --- |
| B Incidence     |          | always       |      | peaks  | before |     | momentum |     |     |     |     |
| Differentiating | under    | the integral | sign | in Eq. | (2.5), | we  | have     |     |     |     |     |
|                 |          |              | dY   | Z      | dι     |     | R        |     |     |     |     |
∞
|     |     |     |     | =   | (τ  | −α) | α dα. |     |     |     | (B1) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ---- |
|     |     |     | dτ  | 0   | dτ  |     | R     |     |     |     |      |
0
|     | dι  |     |     |     |     |     |     | dι  |     |     | dY  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We must have > 0 until incidence reaches its peak (where = 0), and thus > 0
|     | dτ  |     |     |     |     |     |     | dτ  |     |     | dτ  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
at peak incidence; therefore, momentum always peaks after incidence. Peak momentum (yˆ)
always occurs at xˆ [5, Section 3(a)], whereas Eq. (2.1a) shows that the fraction susceptible
is monotone decreasing. Hence the fraction susceptible at peak incidence always exceeds xˆ.
16

| C Lambert’s |     | W-function |     |     |     |     |     |
| ----------- | --- | ---------- | --- | --- | --- | --- | --- |
This appendix is identical to the corresponding appendix in [5, Appendix F] and is included
| here for | convenience. |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- |
E(z)
If = zez, Lambert’s W-function W(z) ([34]; [35, §4.13]) solves the “left-sided”
E(W(z))
inverse relation = z. This equation has countably many solutions, written W (z)
k
for solutions with argz ∈ [2πk,2π(k + 1)). Only W and W return real values for real
0 −1
[−1,0)
z; for other k, W is always complex. We use the two real branches: W maps
|     |     | k   |     |     |     | −1  | e   |
| --- | --- | --- | --- | --- | --- | --- | --- |
to (−∞,−1], and W maps [−1,∞) to [−1,∞). For these two branches, W is a partial
|     |     | 0   |     |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
e
| “right-sided” | inverse | function | for E(z): |     |     |     |     |
| ------------- | ------- | -------- | --------- | --- | --- | --- | --- |
(E(z))
|     |     |     | W   | = z | if z ≤ −1 |     | (C1a) |
| --- | --- | --- | --- | --- | --------- | --- | ----- |
−1
|     |     |     | W   | (E(z)) = z | if z ≥ −1. |     | (C1b) |
| --- | --- | --- | --- | ---------- | ---------- | --- | ----- |
0
While the standard notation W is chosen to indicate the winding number associated with
k
the given branch, for our purposes it is more convenient to write W for W and W for W ,
|     |     |     |     |     |     | −1  | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | −   |     | +   |
so we can write expressions involving W , where the ± matches the corresponding sign in x±
±
| and/or | λ± (W    | and W are | also written | Wp and Wm | [35, §4.13]). |         |     |
| ------ | -------- | --------- | ------------ | --------- | ------------- | ------- | --- |
|        | +        | −         |              |           |               |         |     |
| D      | Previous | estimates |              | of prior  | immunity      | to 1918 | in- |
fluenza
Mills et al. [24, pp.905–906] state: “The proportion of the population susceptible at
the start of the pandemic determines the relationship between R and the basic reproductive
number (R ), which is the number of secondary cases generated by a primary case in a
0
completely susceptible population2. Frost hypothesized that a 1918 pandemic-like strain
spread throughout America in the spring of 1918 (ref. 22), and recent analyses support this
‘herald wave’ hypothesis23. Anecdotal evidence suggests that those who fell ill in the spring
were protected from disease in the autumn pandemic24. Nevertheless, a large majority of
the population was probably susceptible to the A/H1N1 pandemic strain in September 1918.
In a typical epidemic transmission season, 15–25% of the population becomes infected with
influenza4.
The herald wave is believed to have arrived late in the 1917–18 transmission
season. Using 70% as a conservative lower bound for the fraction susceptible at the start of
the autumn pandemic, the medians for our initial and extreme R are 2.9 and 3.9.”
0
Frost [25, p.593] states: “The case fatality, or ratio of deaths to total cases of influenza,
varied in the localities surveyed from 3.1 per cent in New London to 0.8 per cent in San
Antonio, the variations showing no consistent relation to incidence rates. There is, however,
some relation to geographic location, namely, that the highest case-fatality rates occurred
in New London, San Francisco, Baltimore, and minor Maryland communities, in the order
named––that is, in communities representing, respectively, the northern half of the Atlantic
seaboard and the Pacific coast. In the central and southern cities the case fatality was gen-
erally notably lower. Combining the eleven localities into three groups comprising, respec-
tively––(1) San Francisco, (2) New London, Baltimore, and minor Maryland communities,
17

(3) central and southern cities, comprising all other localities, the case-fatality rates in these
three groups are, respectively, 2.33, 2.05, and 1.08 per cent. This is of interest in connection
with the observation that from the standpoint of mortality rates the epidemic was generally
more severe along the northern Atlantic Seaboard and the Pacific Coast than in the Central
States.”
18

Table 1: Standard infectious disease transmission models.
The susceptible-infectious-removed (SIR) model, first proposed by KM [7], assumes that all
infected individuals are equally infectious, and immunity upon recovery is permanent. It is
represented with two equations in standard form [(T1), with parameters β, the transmission
rate, γ, theremovalrate, andpopulationsizeN]ordimensionlessform[(T2), withparameter
R , the basic reproduction number, and time measured in units of the mean infectious
0
period, T = γ−1.]. The generation interval distribution is identical to the infectious period
inf
distribution, so the mean generation interval is µ = γ−1. In this simple model, the epidemic
momentum is equal to the prevalence.
Most infectious diseases have a non-negligible latent period, i.e., there is a delay between ini-
tial infection and becoming infectious. The susceptible-exposed-infectious-removed (SEIR)
model introduces an exposed stage (E) of mean duration γ−1, when individuals are infected
E
but not yet infectious [36]. The mean generation interval µ is the sum of the means of the
latent and infectious periods [10, 11]. In dimensionless units, we write the mean latent pe-
riod ℓ, i.e., as a proportion of the mean infectious period, so the mean generation interval is
µ = ℓ+1 in these units. The standard form is (T5) and the dimensionless form is (T6). We
denote the proportions susceptible, exposed, and infectious by X, Y , and Y, respectively,
E I
and—as in the SIR model—the epidemic momentum Y corresponds to the total proportion
infected, i.e., Y = Y + Y (see [5, Section 2(c)]), consistent with our notation for the SIR
E I
model (T2). The per capita rates at which individuals leave the exposed and infectious com-
partments are γ and γ, respectively. The basic reproduction number is R = β/γ and the
E I 0 I
mean latent period (as a proportion of the mean infectious period γ−1) is ℓ = γ/γ .
I I E
Generic epidemic models can be specified using the renewal equation, which relates the
susceptible fraction X to the force of infection F with a differential equation (T9a), and
relates F to the generation interval distribution, g(α), via a convolution [Eq. (T9b)]. If g(α)
is not known, it is common to assume it is a gamma distribution, as in (T11).
19

SIR model
Standard Dimensionless (X= S, Y = I ) Parameters Properties
N N
β = transmissionrate
dX (T3a) τ =γt (T4a)
d d S t =− N β SI (T1a) dτ =−R 0 XY (T2a) γ 1 = mean pe in ri f o e d ctious g(α)=e−α (T4b)
dY = (cid:0) R X−1 (cid:1) Y (T3b)
dI
=
(cid:0)β
S−γ
(cid:1)
I (T1b)
dτ 0
(T2b) µ= meangeneration = 1
L[g](λ)=
λ+
1
1
(T4c)
dt N interval γ
(T3c) λ± =R 0 x±−1
ι=R 0 XY (T2c) (T4d)
R = basicreproduction = β
0 number γ
(T3d)
SEIR model
Standard Dimensionless (Y =E, Y= I ) Parameters Properties
E N I N
1 τ =γ t (T8a)
= meanlatent I
dS =−β SI (T5a) d d X τ =−R 0 XY I (T6a) γ E period (T7a) ( αe−α, ℓ=1
dt N g(α)=
dY E =R XY − 1 Y 1 = meaninfectious e−α 1 − − e− ℓ α/ℓ, ℓ̸=1
dE = β SI−γE (T5b) dτ 0 I ℓ E γ I period (T8b)
dt N E (T6b) (T7b)
1 1 L[g](λ)= 1 · 1
dI dY 1 µ= + (T7c) ℓλ+1 λ+1
=γE−γI (T5c) I = Y −Y (T6c) γ γ (T8c)
dt E I dτ ℓ E I E I
ι=R 0 XY I (T6d) R ℓ 0 = = γ β I / γ I γ − E 1 ( ( T T 7 7 d e ) ) λ± = p (1−ℓ) 2 2 ( + R 0 4 x ℓ ± R − 0 x 1 ± ) +(1+ (T ℓ) 8d)
Renewal equation
Dimensionless renewal equation For general g(α) For Gamma g(α) [a= µ2 , b= µ ]
σ2 σ2
dX =−X(τ)F(τ) (T9a) Z ∞ ba
dτ µ= αg(α)dα (T10a) g(α)= αa−1e−bα (T11a)
Γ(a)
Z τ 0
F(τ)=R X(α)F(α)g(τ −α)dα L[g](λ)= (cid:0) b (cid:1)a (T11b)
0 τ =t/µ (T10b) λ+b
−∞ (T9b) λ± =b (cid:0) (R x±)1/a−1 (cid:1) (T11c)
1 0
=L[g(t)](λ±) (T10c)
ι=XF (T9c) R 0 x±
20

References
[1] Wallinga J, Lipsitch M. 2007 How generation intervals shape the relationship be-
tween growth rates and reproductive numbers. Proc. R. Soc. B 274, 599–604.
(10.1098/rspb.2006.3754)
[2] Ma J, Dushoff J, Bolker BM, Earn DJD. 2014 Estimating initial epidemic growth rates.
| Bull. Math. | Biol. 76, | 245–260. | (10.1007/s11538-013-9918-2) |     |
| ----------- | --------- | -------- | --------------------------- | --- |
[3] Ma J. 2020 Estimating epidemic exponential growth rate and basic reproduction num-
| ber. Infect. | Dis. Model. | 5,  | 129–141. | (10.1016/j.idm.2019.12.009) |
| ------------ | ----------- | --- | -------- | --------------------------- |
[4] McCaw JM, McVernon J, McBryde ES, Mathews JD. 2009 Influenza: accounting for
| prior immunity. | Science | 325, | 1071. | (10.1126/science.325_1071a) |
| --------------- | ------- | ---- | ----- | --------------------------- |
[5] Earn DJD, Parsons TL. 2025 Epidemic “momentum” and a conservation law for infec-
| tious disease | dynamics. | arXiv | preprint | arXiv:2511.01939. |
| ------------- | --------- | ----- | -------- | ----------------- |
[6] Goldstein E, Dushoff J, Ma J, Plotkin J, Earn DJD, Lipsitch M. 2009 Reconstructing
influenza incidence by deconvolution of daily mortality time series. Proc. Natl. Acad.
| Sci. U.S.A. | 106, 21825–21829. |     | (10.1073/pnas.0902958106) |     |
| ----------- | ----------------- | --- | ------------------------- | --- |
[7] Kermack WO, McKendrick AG. 1927 A contribution to the mathematical theory of
epidemics. Proc. R. Soc. Lond. A 115, 700–721. (10.1098/rspa.1927.0118)
[8] BredaD,DiekmannO,DeGraafWF,PuglieseA,VermiglioR.2012Ontheformulation
of epidemic models (an appraisal of Kermack and McKendrick). J. Biol. Dyn. 6, 103–
117. (10.1080/17513758.2012.716454)
[9] Champredon D, Dushoff J, Earn DJD. 2018 Equivalence of the Erlang SEIR epi-
demic model and the renewal equation. SIAM J. Appl. Math. 78, 3258–3278.
(10.1137/18M1186411)
[10] Svensson A. 2007 A note on generation times in epidemic models. Math. Biosci. 208,
| 300–311. | (10.1016/j.mbs.2006.10.010) |     |     |     |
| -------- | --------------------------- | --- | --- | --- |
[11] Champredon D, Dushoff J. 2015 Intrinsic and realized generation intervals in infectious-
disease transmission. Proc. R. Soc. B 282, 20152026. (10.1098/rspb.2015.2026)
[12] Dublin LI, Lotka AJ. 1925 On the True Rate of Natural Increase: As Exemplified by
the Population of the United States, 1920. J. Am. Stat. Assoc. 20, 305–339. JSTOR
| stable DOI: | 10.2307/2965517 |     | (10.1080/01621459.1925.10503498) |     |
| ----------- | --------------- | --- | -------------------------------- | --- |
[13] Feller W. 1941 On the Integral Equation of Renewal Theory. Ann. Math. Stat. 12,
| 243–267. | (10.1214/aoms/1177731708) |     |     |     |
| -------- | ------------------------- | --- | --- | --- |
[14] Keyfitz N, Caswell H. 2005 Applied Mathematical Demography. Statistics for Biol-
ogy and Health. New York, NY: Springer 3 edition. Online ISBN: 978-0-387-27409-6
(10.1007/b139042)
21

[15] Stone L, Olinky R, Huppert A. 2007 Seasonal dynamics of recurrent epidemics. Nature
446, 533–536. (10.1038/nature05638)
[16] Earn DJD, McCluskey CC. 2025 Global stability of epidemic models with uniform sus-
ceptibility. Proc. Natl. Acad. Sci. U.S.A. 122, e2510156122. (10.1073/pnas.2510156122)
[17] Earn DJD, Ma J, Poinar H, Dushoff J, Bolker BM. 2020 Acceleration of plague out-
breaks in the second pandemic. Proc. Natl. Acad. Sci. U.S.A. 117, 27703–27711.
(10.1073/pnas.2004904117)
[18] Jagan M, Bolker B. 2024 epigrowthfit: Nonlinear Mixed Effects Models of Epidemic
Growth. R package version 0.15.3 (10.32614/cran.package.epigrowthfit)
[19] Rogers SL. 1920 Special Tables of Mortality from Influenza and Pneumonia, in Indiana,
Kansas, and Philadelphia, PA. U.S. Department of Commerce, Washington, DC.
[20] Jagan M, deJonge MS, Krylova O, Earn DJD. 2020 Fast estimation of time-varying
infectious disease transmission rates. PLoS Comput. Biol. 16, e1008124. (10.1371/jour-
nal.pcbi.1008124)
[21] Jagan M. 2025 fastbeta: Fast Approximation of Time-Varying Infectious Disease Trans-
mission Rates. R package version 0.5.0 (10.32614/cran.package.fastbeta)
[22] Moser MR, Bender TR, Margolis HS, Noble GR, Kendal AP, Ritter DG. 1979 An
outbreak of influenza aboard a commercial airliner. Am. J. Epidemiol. 110, 1–6.
(10.1093/oxfordjournals.aje.a112781)
[23] Keeton RW, Cushman AB. 1918 The influenza epidemic in Chicago: The disease as a
type of toxemic shock. JAMA 71, 1962–1967. (10.1001/jama.1918.02600500012003)
[24] Mills CE, Robins JM, Lipsitch M. 2004 Transmissibility of 1918 pandemic influenza.
Nature 432, 904–906. (10.1038/nature03063)
[25] Frost WH. 1920 Statistics of influenza morbidity with special reference to certain factors
in case incidence and case fatality. Public Health Rep. 35, 584–597. (10.2307/4575511)
[26] Caley P, Philp DJ, McCracken K. 2008 Quantifying social distancing arising from pan-
demic influenza. J. R. Soc. Interface 5, 631–639. (10.1098/rsif.2007.1197)
[27] Cope RC, Ross JV, Chilver M, Stocks NP, Mitchell L. 2018 Characterising seasonal
influenza epidemiology using primary care surveillance data. PLoS Comput. Biol. 14,
e1006377. (10.1371/journal.pcbi.1006377)
[28] Bergström F, Favero M, Britton T. 2026 Identifiability in Epidemic Models with Prior
Immunity and Under-Reporting. Bull. Math. Biol. 88, 90. (10.1007/s11538-026-01656-
w)
[29] Wilson EB, Worcester J. 1945 The law of mass action in epidemiology. Proc. Natl. Acad.
Sci. U.S.A. 31, 24–34. (10.1073/pnas.31.1.24)
22

[30] LiuWM,LevinSA,IwasaY.1986Influenceofnonlinearincidenceratesuponthebehav-
ior of SIRS epidemiological models. J. Math. Biol. 23, 187–204. (10.1007/bf00276956)
[31] Finkenstädt B, Grenfell B. 2000 Time series modelling of childhood diseases: A dynam-
ical systems approach. J. R. Stat. Soc. Ser. C Appl. Stat. 49, 187–205. (10.1111/1467-
9876.00187)
[32] Novozhilov AS. 2008 On the spread of epidemics in a closed heterogeneous population.
Math. Biosci. 215, 177–185. (10.1016/j.mbs.2008.07.010)
[33] Earn DJD, Parsons TL. 2026 Epidemic Momentum with Nonlinear Incidence. In prepa-
ration.
[34] Corless RM, Gonnet GH, Hare DEG, Jeffrey DJ, Knuth DE. 1996 On the Lambert W
function. Adv. Comput. Math. 5, 329–359. (10.1007/bf02124750)
[35] DLMF. 2025 NIST Digital Library of Mathematical Functions. https://dlmf.nist.gov/,
Release 1.2.5 of 2025-12-15. F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I.
Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and
M. A. McClain, eds.
[36] Anderson RM, May RM. 1991 Infectious Diseases of Humans: Dynamics and Control.
Oxford: Oxford University Press. (10.1093/oso/9780198545996.001.0001)
23
---- END DOCUMENT ----
