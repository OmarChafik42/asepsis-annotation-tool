Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
1
Flow Matching-Based
PET Image Reconstruction
Fumio Hashimoto, Ziqian Huang, Tatsuya Yokota, and Kuang Gong
Abstract—Generative models have shown strong potential smoothness and anatomical information, to further improve
for positron emission tomography (PET) image reconstruction. PET image quality [3]–[7].
Although diffusion model-based reconstruction methods have
Recent advances in deep learning have led to growing
demonstrated promising performance, they often require many
interest in data-driven approaches for PET image reconstruc- reverse sampling steps with data-consistency updates incor-
porated into the sampling process. Flow matching offers an tion [8]–[10]. Early deep learning-based methods mainly used
attractivealternativebecauseitcandirectlyestimatecleanimages convolutionalneuralnetworks(CNNs)aslearnedimagepriors
from intermediate states, allowing data-consistency refinement within PET image reconstruction. For example, CNNs have
to be separated from flow propagation. In this work, we pro- been used to parameterize PET images within iterative re-
posed flow matching-based PET image reconstruction methods.
construction frameworks [11] and to provide learned regular-
We first established PET-FlowDPS by incorporating Poisson
likelihood guidance with an expectation-maximization (EM)- ization in unrolled reconstruction frameworks [12]. Although
based preconditioner into the FlowDPS framework. We then these approaches demonstrate the potential of CNN-based
proposed a model-based PET reconstruction method that used priorstoimprovePETimagequality,theyrelyondeterministic
a pretrained flow matching model as a prior, in which the flow-
mappingsratherthanexplicitlymodelingtheunderlyingimage
based prior, PET data refinement, and stochastic propagation distribution. When multiple plausible high-quality solutions
were interpreted within an approximate Bayesian framework.
Experimentalresultsusing[18F]FDGbrainPETdatasetsshowed exist, such deterministic mappings may produce averaged
thattheproposedmethodachievedbetterbias-variancetrade-offs estimates, potentially suppressing fine structural details and
acrossdifferentdoselevelscomparedwithotherreferencemeth- leading to oversmoothed images [13], [14].
ods. These results demonstrated the potential of flow matching
Diffusion models [15], [16], which can learn image distri-
asagenerativepriorforquantitativePETimagereconstruction.
butionsandactasgenerativepriors,havebeeninvestigatedfor
various PET imaging tasks, including image denoising [17]–
Index Terms—Positron emission tomography (PET), Image
[20],synthesis[21],[22],andattenuationcorrection[23],[24].
reconstruction, Flow matching
For PET image reconstruction, Singh et al. [25] demonstrated
the potential of score-based reconstruction using diffusion
posteriorsampling(DPS)[26]anddecomposeddiffusionsam-
I. INTRODUCTION
pling(DDS)[27].Subsequentstudiesextendeddiffusion-based
POSITRON emission tomography (PET) enables quanti- PET reconstruction to fully 3D imaging [28], joint activity
tative in vivo imaging of radiotracer distributions, mak- and attenuation estimation [29], [30], and out-of-distribution
ing it a valuable molecular imaging modality in oncol- adaptation [31], [32].
ogy, cardiology, and neurology. However, PET image qual- Despite these advances, diffusion-based PET image recon-
ity is fundamentally constrained by limited counting statis- struction remains computationally demanding because both
tics and various physical degradation effects, which com- neural network evaluations and data-consistency updates must
promises its lesion detectability and quantitative accuracy. berepeatedovermanyreversesamplingsteps.Itsperformance
Althoughiterativereconstructionmethods,suchasmaximum- can also be sensitive to the noise schedule, the number of
likelihood expectation-maximization (MLEM) and ordered- reverse sampling steps, and the strength and timing of the
subsets expectation-maximization (OSEM), have been widely data-consistency updates. In DPS, computing the likelihood
used for PET image reconstruction with explicit modeling gradient with respect to an intermediate noisy image requires
of Poisson noise statistics and the PET system response [1], differentiating through the denoised estimate and thus back-
[2], the resulting images often exhibit excessive noise under propagatingthroughtheneuralnetworkateachsamplingstep.
low-count conditions. To address this limitation, maximum Thisincreasescomputationalandmemorycostsandmayresult
a posteriori (MAP)-based reconstruction methods have been innumericallysensitiveupdates[27].AlthoughPET-DDS[25]
developed to incorporate prior information, such as spatial and likelihood scheduling [28] improve the efficiency and
robustness of data-consistency updates, the generative prior
ThisworkwassupportedbyNIHgrantsR01EB034692andR01AG078250. and data-consistency refinement remain coupled within the
(Correspondingauthor:KuangGong)
prescribed reverse diffusion process.
F.Hashimoto,Z.HuangandK.GongarewiththeJ.CraytonPruittFamily
Department of Biomedical Engineering, University of Florida, FL, USA (e- Flow matching offers an attractive alternative to diffu-
mail:fumio.hashimo@ufl.edu;ziqian.huang@ufl.edu;kgong@bme.ufl.edu). sion models by learning a time-dependent velocity field that
T. Yokota is with the Department of Computer Science, Nagoya Institute
transports samples from a source distribution to the target
of Technology, Aichi, Japan and with the RIKEN Center for Advanced
IntelligenceProject,Tokyo,Japan(e-mail:t.yokota@nitech.ac.jp). distribution along a prescribed probability path [33]. Its rela-
6202
guA
02
]VI.ssee[
1v21102.8062:viXra

2
tively straight transport trajectories can reduce the number of B. Flow matching
sampling steps required for image generation. Under a linear
Flow matching learns a continuous-time velocity field that
probability path, the velocity predicted at an intermediate
transports samples from a simple source distribution to a
point can be used to directly estimate the destination image.
target image distribution [33], [38]. Let x ∼ p (x ) denote
0 0 0
This property provides a flexible framework for incorporating
a sample from the source distribution, typically a standard
data consistency into inverse problems [34]–[37]. Recently,
Gaussian distribution, and let x ∼ p (x ) denote a sample
1 1 1
Flower[35]providesanapproximateBayesianframeworkthat
from the target image distribution. Using a linear probability
separates destination estimation, data-consistency refinement,
path, an intermediate sample at time t∈[0,1] is defined as
and stochastic propagation. However, its data-consistency re-
finementassumesaGaussianobservationmodelandtherefore x t =(1−t)x 0 +tx 1 , (4)
does not directly account for the Poisson statistics of PET
and the corresponding conditional velocity along this path is
measurements.
dx
In this study, we present flow matching-based PET image v (x |x ,x )= t =x −x . (5)
reconstruction methods. First, we establish PET-FlowDPS t t 0 1 dt 1 0
as a baseline by extending flow-driven posterior sampling Aneuralnetworkv (x ,t)parameterizedbyθ istrainedto
θ t
(FlowDPS) [34] to PET reconstruction using Poisson likeli- approximate the velocity field by minimizing the conditional
hoodguidancewithpreconditionedgradients.Second,inspired flow-matching loss
bytheFlowerframework[35],weproposeamodel-basedPET (cid:104) (cid:105)
reconstruction method that uses a pretrained flow-matching L CFM (θ)=E t,x0,x1 ∥v θ (x t ,t)−(x 1 −x 0 )∥2 2 , (6)
model as a learned image prior. The proposed algorithm
where x = (1−t)x +tx , t ∼ U(0,1), x ∼ p (x ), and
iteratively performs three steps: (1) flow-based destination t 0 1 0 0 0
x ∼ p (x ). After training, samples from the target distri-
estimationtoobtainacleanimageestimate,(2)penalizedPET 1 1 1
bution can be generated by solving the ordinary differential
image reconstruction refinement to enforce data consistency,
equation (ODE)
and (3) flow-based propagation to update the image to the
next time step. These three steps can be interpreted within an dx t =v (x ,t), x ∼p (x ), (7)
approximateBayesianframework.Separatingdata-consistency dt θ t 0 0 0
refinement from flow propagation allows established model- from t=0 to t=1 using a numerical ODE solver.
based PET reconstruction algorithms to be directly incorpo- Under the linear probability path in (4), an estimate of
ratedintotherefinementstepwithoutmodifyingthepretrained the destination image x can be obtained directly from an
1
flow model, thereby enabling stable data-consistency enforce- intermediate state x as
t
ment for quantitative PET reconstruction.
xˆ (x ,t)=x +(1−t)v (x ,t). (8)
1 t t θ t
II. BACKGROUND This explicit destination-image estimate enables data-
consistency refinement to be applied before advancing the
A. PET image reconstruction
intermediate state along the flow trajectory.
PETimageacquisitioncanbedescribedusingthefollowing
linear model
III. METHODOLOGY
y¯=Ax+b, (1)
A schematic overview of PET-FlowDPS and the proposed
where y¯∈RM denotes the expected projection data, x∈RN model-based PET reconstruction with a flow-based prior is
represents the unknown radiotracer distribution, A ∈ RM×N shown in Fig. 1. Both methods refine the flow-based desti-
is the system matrix, and b ∈ RM represents mean of the nation estimate using the measured PET data. PET-FlowDPS
random and scatter events. M and N denote the number applies a data-consistency update using the gradient of the
of lines of response (LOR) and image voxels, respectively. log-likelihood,whereastheproposedmethodperformsaMAP
Assuming the measured projection data y ∈ RM follows the reconstruction that balances data fidelity and the flow-based
Poisson distribution with mean y¯, the log-likelihood function prior.
can be written as
M A. FlowDPS for PET reconstruction
(cid:88)
L(y |x)= {y log([Ax] +b )−([Ax] +b )}. (2)
i i i i i FlowDPSisaposteriorsamplingsolverforinverseproblems
i=1
thatintegratesthelikelihoodgradientandstochasticnoiseinto
TheMLEMalgorithmestimatesxbymaximizing(2)using a flow matching framework [34]. For the linear conditional
the following iterative update for voxel j flow, the marginal velocity is
x( j n+1) = x S ( j n) (cid:88) M A ij [Ax(n y ) i ] +b , S j = (cid:88) M A ij . (3) v t (x t )= x t t + 1− t t ∇ xt logp t (x t ). (9)
j i i
i=1 i=1 The corresponding posterior marginal velocity is
This update rule is stable because it always satisfies
x 1−t
L(y|x(n+1))≥L(y|x(n)). v
t
(x
t
|y)=
t
t +
t
∇
xt
logp
t
(x
t
|y). (10)

3
𝝐 # 𝒙" 𝒙
!,# 𝒙"
!,#
%!"#
𝒙#
!,#
𝒙
𝒙
%!
%!
𝒙"
$,#
𝒙 𝒙 𝒙 𝒙 𝒙
$ ! ! $ !
𝝐
# 𝒙"
!,# 𝒙"
!,# 𝒙
𝒙# %!"#
!,#
𝒙
%!
𝒙 𝒙 𝒙 𝒙 𝒙
$ ! ! $ !
SPDwolF-TEP
)a(
desoporP
)b(
𝒙" !,#
𝒙#
𝒙# !,#
$,#&!
𝒙#
!,#
(1) Destination estimation (2) PET-data refinement (3) Propagation
Fig.1. Overviewof(a)PET-FlowDPSand(b)theproposedmodel-basedPETreconstructionwithaflow-basedprior.Instep(1),bothmethodsestimatea
destinationimageusingthepretrainedflowmodel.Instep(2),(a)PET-FlowDPSappliesadata-consistencyupdateusingthegradientofthelog-likelihood,
and(b)theproposedmethodperformsaMAPreconstructionthatbalancesdatafidelityandtheconditionalflow-basedprior.Instep(3),therefineddestination
estimate is propagated to the next flow time point using the respective stochastic propagation rules. The purple contours in step (2) represent the PET log-
likelihood,andthebluecontoursin(b-2)representtheconditionalflow-basedpriorapproximatedbyaGaussiandistribution.
Using Bayes’ rule, (10) can be rewritten as where λ is the time-dependent guidance strength with the
tk
factor 1/t in (12) absorbed into λ . After this correction,
1−t k tk
v (x |y)=v (x )+ ∇ logp (y |x ) the sample at the next time point is obtained as
t t t t t xt t t
(11)
1−t x˜ = (cid:112) t ϵ + (cid:112) 1−t xˆ , (16)
≈v (x ,t)+ ∇ logp (y |x ). 0,k+1 k+1 k k+1 0,k
θ t t xt t t
x =(1−t )x˜ +t x˜ , (17)
tk+1 k+1 0,k+1 k+1 1,k
Since p (y |x ) is not tractable, DPS [26] and FlowDPS [34]
t t
where ϵ ∼N(0,I).
apply the following approximations k
For PET reconstruction, the preconditioned gradient of the
∇ logp (y |x )≈∇ logp(y |xˆ (x ,t)), (DPS) log-likelihood is calculated by
xt t t xt 1 t
1 (cid:26) (cid:20) (cid:21) (cid:27)
≈ t ∇ xˆ1 logp(y |xˆ 1 (x t ,t)). (FlowD (1 P 2 S ) ) ∇˜ x L(y |x)= S x AT Ax y +b −S , (18)
Thus, the unconditional flow can be guided toward the
where x/S is a preconditioning term for stability. Using this
posterior distribution by incorporating the likelihood gradient.
gradient, (15) becomes
Although DPS requires backpropagation through the flow
model to compute the Jacobian of the destination estimator, x˜ 1,k =xˆ 1,k +λ∇˜ xˆ1,k L(y |xˆ 1,k ), (19)
FlowDPS approximates this gradient to bypass the Jacobian
where λ is the constant guidance strength. The overall al-
computationandappliesthelikelihoodgradientdirectlytothe
gorithm of the PET-FlowDPS reconstruction is shown in
destination image estimate.
Algorithm 1.
To apply the likelihood approximation in (12), FlowDPS
Although FlowDPS derives an additional likelihood-
usestheflow-basedsourceanddestinationestimates.Using(4)
gradient term for the posterior velocity field, its practical
and(5),theseestimatesateachtimepointt canbeexpressed
k
implementation differs from this theoretical formulation. In
by the flow-version of Tweedie’s formula [34] as
practice, the guidance coefficient is typically chosen to be
xˆ =x −t v (x ,t ), (13) a relatively small value, and multiple gradient updates are
0,k tk k θ tk k
performed [34]. In addition, the stochastic propagation step is
xˆ =x +(1−t )v (x ,t ). (14)
1,k tk k θ tk k inherited from the sampling strategy of DPS [26], rather than
Thedestinationestimateisthencorrectedusingthelikelihood beingdirectlyderivedfromtheflow-basedprobabilisticformu-
gradient as lation.Asaconsequence,theprobabilisticinterpretationofthe
trade-offbetweenthepretrainedflow-basedpriorandthedata-
x˜ =xˆ +λ ∇ logp(y |xˆ ), (15) consistency term becomes less explicit. The PET-FlowDPS
1,k 1,k tk xˆ1,k 1,k

4
Algorithm 1 PET-FlowDPS reconstruction rithm. The PET data observation process is defined by the
Require: Flowtimepoints0=t 0 <t 1 <···<t K =1,flow following probabilistic forward model
model v , measured data y, background b, and guidance
θ
strength λ x 0 ∼p 0 (x 0 )=N(0,I), (20)
1: x t0 ∼N(0,I) x 1 =Φ 1 (x 0 )∼p 1 (x 1 ), (21)
2: for k =0 to K−1 do y ∼P(y|Ax +b), (22)
1
3: xˆ 0,k =x tk −t k v θ (x tk ,t k )
4: xˆ 1,k =x tk +(1−t k )v θ (x (cid:26) tk ,t k (cid:20) ) (cid:21) (cid:27) where Φ 1 is a transportation function from the source domain
5: ∇˜ xˆ1,k L(y |xˆ 1,k )= xˆ S 1,k AT Axˆ 1 y ,k +b −S t T o he th v e ar t i a a r b g l e e t s d a o re ma g i e n ne a r n a d ted P se s q ta u n e d n s tia f l o ly r P as oi x ss 0 o → n d x is 1 tr → ibu y tio . n.
6: x˜ 1,k =xˆ 1,k +λ∇˜ xˆ1,k L(y |xˆ 1,k ) Our goal is to sample PET images from the posterior dis-
7: ϵ k ∼N(0 √ ,I) √ tribution p(x 1 |y). We discretize the continuous time interval
8: x˜ 0,k+1 = t k+1 ϵ k + 1−t k+1 xˆ 0,k t ∈ [0,1] into K + 1 time points and perform sequential
9: x tk+1 =(1−t k+1 )x˜ 0,k+1 +t k+1 x˜ 1,k sampling as follows:
10: end for
11: return xˆ =x tK x t0 ∼p(x t0 ), (23)
x ∼p(x |x ,y), (24)
t1 t1 t0
Algorithm 2 Model-based PET reconstruction using flow .
.
.
matching
Require: Flow time points 0 = t
0
< t
1
< ··· < t
K
= 1, x tK ∼p(x tK |x tK−1 ,y), (25)
flow model v , measured data y, background b, penalty
θ where 0 = t < t < ··· < t < t = 1. Since x can
strength β, and inner iteration number N 0 1 K−1 K 0
be sampled directly from N(0,I), the remaining task is to
1: x t0 ∼N(0,I) sample
2: for k =0 to K−1 do
4
3
:
:
x
xˆ
(
1
0
,k
) =
=
[
x
xˆ
t
1
k
,k
+
] +
(1−t k )v θ (x tk ,t k ) x tk+1 ∼p(x tk+1 |x tk ,y), (26)
5: for n=0 to N −1 do foranyk ∈{0,1,...,K−1}.Directsamplingfromthiscondi-
6: xˆ( E n M + , 1 j ) = x S ( j n (cid:18)j ) (cid:80) i A ij[Ax (cid:19) (n y ) i ]i+bi t m io o n d a e l l d f i o s r tr p ib ( u x tion i | s x dif , fi y c ) u . lt, so we introduce an approximate
x( j n+1) = 2 1 xˆ 1,j,k − S β j 2) Approxim tk a + te 1 pr t o k babilistic models and sampling decom-
7: (cid:115) position: FollowingFlower[35],weusethefollowingapprox-
+ 1
(cid:18)
xˆ − S j
(cid:19)2
+4xˆ(n+1) S j imations to decompose the conditional sampling process:
2 1,j,k β EM,j β
8: end for p˜(x 1 |x tk )=N(xˆ 1 (x tk ,t k ),β−1I), (27)
9: x˜ 1,k =x(N) p˜(x tk+1 |x 1 ,x tk )=p(x tk+1 |x 1 )
10: ϵ k ∼N(0,I) =N(t x ,(1−t )2I). (28)
k+1 1 k+1
11: x tk+1 =(1−t k+1 )ϵ k +t k+1 x˜ 1,k
12: end for Thefirstapproximationin(27)assumesthat,givenx ,the
13: return xˆ =x tK destination image x 1 follows a Gaussian distribution ce t n k tered
attheflow-basedestimatexˆ (x ,t ).Theparameterβ repre-
1 tk k
sentstheprecisionofthisdistributionandcontrolsthestrength
algorithmimprovesthestabilityofthedata-consistencyupdate of the regularization imposed by flow matching. The second
by incorporating an EM-based preconditioner. As a result, approximation in (28) replaces the transition conditioned on
likelihood refinement can be performed stably using a single both x tk and x 1 with a stochastic transition conditioned only
update. However, this modification still does not provide a onx 1 .Thisformulationprovidesaprobabilisticinterpretation
probabilisticformulationoftheoverallreconstructionprocess. of the stochastic propagation step.
Next, we consider the conditional distribution p(x |
tk+1
x ,y) in (26). By marginalizing over x , applying the
B. Model-based PET reconstruction using flow matching
tk 1
conditional independence implied by the Markov property,
In this section, inspired by the Flower framework, we i.e. p(x tk+1 |x 1 ,x tk ,y)=p(x tk+1 |x 1 ,x tk ), and subsequently
proposeamodel-basedPETreconstructionalgorithmdesigned applying the approximations in (27) and (28), we obtain
to improve stability and interpretability compared with PET-
p(x |x ,y)
FlowDPS.Theproposedreconstructionmethodformulatesthe tk+1 tk
(cid:90)
flow-based prior, PET-data refinement, and stochastic propa- = p(x |x ,x ,y)p(x |x ,y)dx , (29)
gation within an approximate Bayesian framework.
tk+1 1 tk 1 tk 1
(cid:90)
1) Theoretical background: We first describe the proba-
≈ p˜(x |x ,x )p˜(x |x ,y)dx , (30)
bilistic modeling structure used to derive the proposed algo-
tk+1 1 tk 1 tk 1

5
where, by Bayes’ rule and conditional independence implied
by the Markov property, i.e. p(y|x ,x )=p(y|x ), 28.0
1 tk 1
p˜(x |x ,y)∝p(y|x ,x )p˜(x |x )=p(y|x )p˜(x |x )
1 tk 1 tk 1 tk 1 1 tk
=P(y|Ax +b)N(x |xˆ (x ,t ),β−1I). (31) 27.5
1 1 1 tk k
Equation(30)representstheapproximateconditionaldistri-
bution of x as a marginal distribution over x . Therefore, 27.0
tk+1 1
rather than sampling directly from this marginal distribution,
we employ a hierarchical sampling. We first draw x˜ from its
1
conditionalposteriorandthendrawx fromtheconditional 26.5
tk+1
distribution given x˜ . Specifically, it is given by
1
x˜ ∼p˜(x |x ,y), (32) 26.0
1 1 tk
x tk+1 ∼N(t k+1 x˜ 1 ,(1−t k+1 )2I). (33) 5 1025 50 75 100 125 150 175 200
Sampling steps
In Flower [35], under a Gaussian likelihood, this sampling
stepwasreplacedbytheexpectedvalue(oranequivalentMAP
solution) plus a stochastic perturbation. Although a Laplace
approximation could be used for approximate sampling from
the Poisson posterior in PET, Flower reported better recon-
struction performance when this perturbation was omitted.
Basedonthisfinding,ourproposedmethodreplacesstep(32)
with the MAP solution:
x˜ =argmaxlogp˜(x |x ,y). (34) 1
x1
1 tk
This MAP approximation converts the posterior refinement
intoapenalizedlikelihoodoptimizationproblem,whichiswell
suitedtoPETreconstructionbecauseefficientoptimizational-
gorithms,suchaspenalizedEMmethods,arereadilyavailable.
Therefore,theproposedmethodusestheMAPestimateinstead
of directly sampling from p˜(x |x ,y) at each flow step.
1 tk
3) Update rules: The proposed algorithm consists of three
steps: (1) flow-based destination estimation to obtain a clean
image estimate, (2) penalized PET image reconstruction re-
finement to enforce data consistency, and (3) flow-based
propagation to update the image at the next time step.
1) Based on the conditional prior in (27), the destination
image is estimated as the mean of the conditional prior
p˜(x |x )=N(xˆ (x ,t ),β−1I): 1 tk 1 tk k
xˆ (x ,t )=x +(1−t )v (x ,t ). (35)
1 tk k tk k θ tk k
2) Based on the conditional posterior in (31), the destina-
tion image estimate xˆ is refined using the measured
1,k
PET data y by solving the following penalized PET
reconstruction problem:
(cid:26) (cid:27) β
x˜ =argmax L(y|x)− ∥x−xˆ (x ,t )∥2 , 1,k x 2 1 tk k 2
=prox [xˆ (x ,t )], (36)
−β−1L(y|x) 1 tk k
whereβ controlsthestrengthoftheflow-basedprior.To
solve(36),weusetheoptimizationtransfermethod[39],
[40]. The voxel-wise update rule for (36) is
(cid:20) (cid:21) 1 S
x˜(n+1) = xˆ − j
1,j 2 1,j β
(cid:115)
1
(cid:18)
S
(cid:19)2
S
+ xˆ − j +4x(n+1) j, (37)
2 1,j β EM,j β
)Bd(
RNSP
Proposed
Proposed(5)
0.345
0.344
0.343
0.342
0.341
0.340
0.339
0.338
0.337
0.16 0.17 0.18 0.19
White matter CoV
).u.a(
ekatpu
nematuP
200
200
Proposed
Proposed(5)
Full dose
5
5
Fig.2. ImpactofthenumberofsamplingstepsKonPSNR(top)andonthe
putamen uptake–white matter CoV tradeoff curves (bottom). Filled markers
correspondtotheimagesasshowninFig.4.
where x(n+1) is obtained by MLEM (3) from x˜(n).
EM 1
3) Based on the stochastic propagation model in (33), the
refined destination estimate is propagated to the next
time point as
x =(1−t )ϵ +t x˜ , (38)
tk+1 k+1 k k+1 1
where ϵ ∼N(0,I) is sampled at each time step.
k
The overall algorithm of the proposed model-based PET
image reconstruction method is shown in Algorithm 2. To
further improve reconstruction stability, we used an ensemble
average of five independently reconstructed images, denoted
as Proposed(5).
IV. EXPERIMENTALSETUP
We evaluated flow matching-based reconstruction methods
usingclinicalbrain[18F]FDGPETdata.Theexperimentswere
run on an NVIDIA B200 GPU with 192 GB of memory.
A. Brain PET data
For the clinical data experiment, we used pretrained un-
conditional flow models trained on early 0-10 min frames

6
0.345
0.344
0.343
0.342
0.341
0.340
0.339
0.338
0.337
0.16 0.17 0.18 0.19 0.20 0.21 0.22 0.23
White matter CoV
).u.a(
ekatpu
nematuP
penalty[44],decomposeddiffusionsampling(DDS)[25],and
Proposed PET-FlowDPS. For a fair comparison, the diffusion model
Proposed(5)
used in DDS was trained using the same training datasets and
Full dose
14 employed the same network architecture as the corresponding
14 1 flow model.
For the MAPEM method, we used the relative difference
penalty defined as
1
R(x)= (cid:88) (cid:88) (x j −x k )2 , (39)
(x +x )+γ|x −x | j k j k
j k∈Nj
whereN standsforasetofneighborhoodindicesofjthvoxel
j
andγ controlstheshapeofthefunction.Followingthedefault
setting for clinical PET scanners, we set γ =2 [45].
For DDS reconstruction, we used the following iterative
update:
xˆ(n+1) =xˆ(n)+
Fig. 3. Impact of the number of inner EM iterations N on the putamen 0 0
(cid:34) (cid:35)
uptake–whitematterCoVtrade-offcurvesacrossthe10subjectsatthe10% xˆ(n) y (cid:16) (cid:17)
count level. Markers were plotted for N = 1,2,...,14. Filled markers 0 AT −S−2λ xˆ(n)−xˆ(0) ,
indicate N = 10, which was used for the representative images shown in S Axˆ(n)+b DDS 0 0
0
Fig.4. (40)
where xˆ(0) =xˆ , n=0,1,...,N −1 denotes the number
of [18F]MK-6240 tau scans [17], with an injected dose of of iterat 0 ions, xˆ 0 (n)/S is a preco D n D d S itioning term and λ
0 DDS
approximately 185 MBq. These early-time-frame PET images
controls the strength of the regularization. We set the number
mainly reflected cerebral blood flow information. The PET
of diffusion sampling steps to 200 and N = 5 in the
DDS
images were reconstructed using the ordered subsets EM
experiments.
algorithm with 3 iterations and 17 subsets, including point
For the proposed method, the flow interval was discretized
spread function modeling and time-of-flight information. The
into 50 sampling steps, and 10 penalized EM iterations were
reconstructed images had a matrix size of 256×256×89 and
performed at each time point. The penalty strength was set to
avoxelsizeof1.17×1.17×2.79mm3.ThePETimageswere
β =0.1. Unless otherwise specified, these settings were used
subsequently downsampled and centrally cropped, resulting
for all reported results.
in a matrix size of 128 × 128 × 80 and a voxel size of
Mean uptake was calculated in the putamen region and
2.34×2.34×2.79mm3.Themodelwasimplementedusinga
background noise was evaluated using the coefficient of vari-
3D U-Net backbone and trained on 116 PET datasets. Among
ation (CoV) in the white matter region as
thesedatasets,110wereusedfortrainingand6forvalidation.
During testing, we used 10 clinical [18F]FDG data from CoV= SD WM , (41)
the Monash DaCRA fPET–fMRI dataset [41]. Dynamic PET Mean
WM
scans were acquired over 90 min following an injection of where Mean and SD are the mean and standard devi-
WM WM
approximately 238 MBq of [18F]FDG, and the data acquired ation values of the white matter regions, respectively. These
duringthe80–90minintervalwereusedfortesting.Lowdose regions were derived from FreeSurfer [46]. Peak signal-to-
PET data were simulated by downsampling the original list- noise ratio (PSNR) was also calculated using the full dose
mode data to 10% and 5% of the original counts. The 10% image as the reference as
dose level was used for the primary evaluation, and the 5%
(cid:34) (cid:35)
dose level was evaluated to assess reconstruction performance max(X )2
PSNR=10log full , (42)
u d n o d se er d m at o a re w s e e r v e er u e se lo d w t - o do g s e e n c e o ra n t d e it r i e o f n e s r . e T n h ce ec im or a re g s e p s o . n T d h i e ng P f E u T ll 10 N 1 vox (cid:13) (cid:13)X full −X′ (cid:13) (cid:13) 2 2
images were reconstructed on a 128×128×80 voxel grid where max(·) indicates the maximum value of the image,
with a voxel size of 2.34×2.34×2.79 mm3. Scatter and ran- X and X′ denote the full dose and target reconstructed
full
dom corrections were performed using a voxel-driven scatter images, respectively, and N is the number of voxels.
vox
model and a maximum-likelihood method, respectively, and For the variability analysis, 10 independent low-dose re-
magnetic resonance-derived µ maps were used for attenuation alizations were generated by randomly sampling 10% of
correction [42]. The system matrix was implemented using the events from the original listmode data. Each realization
Parallelproj [43]. was independently reconstructed using all evaluated methods.
Voxel-wise mean and standard-deviation images were calcu-
lated across the 10 reconstructed images. The bias image
B. Evaluation
was calculated as the voxel-wise difference between the mean
Wecomparedtheproposedmodel-basedPETreconstruction reconstructedimageandthecorrespondingfull-dosereference
method with MLEM, MAPEM using the relative difference image.

7
| MLEM (Full dose) |     | MLEM |     | MAPEM |     | DDS | FlowDPS |     |     | Proposed |     | Proposed(5) |     |
| ---------------- | --- | ---- | --- | ----- | --- | --- | ------- | --- | --- | -------- | --- | ----------- | --- |
Fig.4. Reconstructionresultsofthreeorthogonalslicesoftheclinical[18F]FDGdataat10%dose.
|      |     |     |     |     |     | provided                                        | putamen | uptake        | closest   | to         | the full     | dose   | reference |
| ---- | --- | --- | --- | --- | --- | ----------------------------------------------- | ------- | ------------- | --------- | ---------- | ------------ | ------ | --------- |
|      |     |     |     |     |     | whilemaintaininglowerwhitematterCoV.Therefore,K |         |               |           |            |              |        | =50       |
| 0.34 |     |     |     |     |     | and N =10                                       | were    | used          | in the    | subsequent | experiments. |        |           |
|      |     |     |     |     |     | Figure                                          | 4 shows | reconstructed |           |            | images       | of one | clinical  |
|      |     |     |     |     |     | [18F]FDG                                        | data    | using         | different | methods.   | PET-FlowDPS  |        | and       |
).u.a( ekatpU nematuP 0.33 theproposedmethodproducedimageswithlowernoiselevels
|     |     |     |     |     |     | than MLEM, | MAPEM,   |          | and DDS. | In    | particular, | the | proposed  |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | -------- | ----- | ----------- | --- | --------- |
|     |     |     |     |     |     | method     | provided | visually | higher   | image | contrast    |     | than PET- |
0.32
|     |     |     |     |     |     | FlowDPS,      | consistent |        | with the | putamen | uptake–white |             | matter |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | ------ | -------- | ------- | ------------ | ----------- | ------ |
|     |     |     |     |     |     | CoV trade-off |            | curves | shown    | in Fig. | 5. DDS,      | PET-FlowDPS |        |
andtheproposedmethodrecoveredputamenuptakecompara-
| 0.31 |     |     |     |     | Full dose |                                                          |         |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --------- | -------------------------------------------------------- | ------- | --- | --- | --- | --- | --- | --- |
|      |     |     |     |     | MLEM      | bletothatofthefulldosereference.However,DDSandPET-       |         |     |     |     |     |     |     |
|      |     |     |     |     | MAPEM     | FlowDPSexhibitedlessfavorablenoisecharacteristicsthanthe |         |     |     |     |     |     |     |
| 0.30 |     |     |     |     | DDS       | proposed                                                 | method. |     |     |     |     |     |     |
FlowDPS
|     |     |     |     |     |     | Figure | 6 shows | the | voxel-wise | mean, | bias, | and | standard- |
| --- | --- | --- | --- | --- | --- | ------ | ------- | --- | ---------- | ----- | ----- | --- | --------- |
Proposed
|     |     |     |     |     | Proposed(5) | deviation | maps | for | the different |     | reconstruction |     | methods. |
| --- | --- | --- | --- | --- | ----------- | --------- | ---- | --- | ------------- | --- | -------------- | --- | -------- |
0.29
|     |      |      |      |      |           | MLEM, | MAPEM, | and | DDS | exhibited | relatively |     | high spa- |
| --- | ---- | ---- | ---- | ---- | --------- | ----- | ------ | --- | --- | --------- | ---------- | --- | --------- |
|     | 0.15 | 0.20 | 0.25 | 0.30 | 0.35 0.40 |       |        |     |     |           |            |     |           |
White matter CoV
|         |              |              |        |     |                  | tial standard | deviations, |            | whereas | PET-FlowDPS |          | and           | the pro- |
| ------- | ------------ | ------------ | ------ | --- | ---------------- | ------------- | ----------- | ---------- | ------- | ----------- | -------- | ------------- | -------- |
|         |              |              |        |     |                  | posed method  |             | showed     | lower   | spatial     | standard | deviations.   | PET-     |
|         |              |              |        |     |                  | FlowDPS       | exhibited   | relatively |         | high        | spatial  | bias, whereas | the      |
| Fig. 5. | Mean putamen | uptake–white | matter | CoV | trade-off curves | across        |             |            |         |             |          |               |          |
the10subjectsatthe10%countlevel.Markerswereplottedat10-iteration proposed method maintained bias levels comparable to those
intervalsfrom10to100forMLEM,at20-iterationintervalsfrom20to200 ofMLEMandMAPEMwhileprovidinglowerspatialstandard
| forMAPEM(βMAPEM=30,γ=2),atλ |     |     |     | DDSof0,10,100,500,and1000 |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deviations.Overall,theproposedmethodprovidedafavorable
| for DDS, | at λ of 0.8, 0.9, | 1.0, 1.2, | and 1.4 | for PET-FlowDPS, | and at | β of |     |     |     |     |     |     |     |
| -------- | ----------------- | --------- | ------- | ---------------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
0.05,0.06,0.08,0.1,and0.25forProposedandProposed(5).Filledmarkers balance between spatial bias and variability.
correspondtotherepresentativeimagesshowninFig.4.
|     |     |     |     |     |     | To further       | evaluate |             | reconstruction |          | performance | under             | more    |
| --- | --- | --- | --- | --- | --- | ---------------- | -------- | ----------- | -------------- | -------- | ----------- | ----------------- | ------- |
|     |     |     |     |     |     | severe low-count |          | conditions, |                | Fig. 7   | shows       | the reconstructed |         |
|     |     |     |     |     |     | images           | at the   | 5% count    | level.         | Compared |             | with              | the 10% |
V. RESULTS
doseresults,PET-FlowDPSproducedblurredimages,whereas
Figure 2 shows the impact of the number of sampling the proposed method preserved image contrast and structural
steps K on PSNR and on the putamen uptake–white matter details.Consistentwiththereconstructedimages,theputamen
CoV tradeoffs. The PSNR peaked at K = 50 and decreased uptake–whitematterCoVtradeoffcurvesinFig.8showedthat
thereafter. Favorable tradeoffs were observed with both 50 the proposed method recovered putamen uptake comparable
and 75 sampling steps. Figure 3 presents the impact of the to that of the full dose reference, whereas PET-FlowDPS
number of penalized EM iterations on the putamen uptake– underestimated putamen uptake. These quantitative results
whitematterCoVtradeoffcurves.TenEMiterations(N =10) demonstrate that the proposed model-based flow matching

8
| MLEM (Full dose) |     |     | MLEM |     | MAPEM |     | DDS | FlowDPS |     | Proposed |     |     | Proposed(5) |     |
| ---------------- | --- | --- | ---- | --- | ----- | --- | --- | ------- | --- | -------- | --- | --- | ----------- | --- |
0.9
0.6
naeM
0.3
0.0
0.2
0.1
saiB
0.0
−0.1
−0.2
0.05
noitaived dradnatS
0.04
0.03
0.02
0.01
0.00
Fig.6. Voxel-wisemean,bias,andstandard-deviationmapscalculatedfrom10independent10%lowdoserealizationsforthedifferentreconstructionmethods.
reconstruction outperformed both conventional iterative and the proposed method replaces this gradient-based refinement
generative model-based reconstruction methods. with MAP reconstruction. This formulation provides an ex-
The computation times for DDS, PET-FlowDPS, and the plicit balance between the flow-based prior and the PET log-
proposed method were 3.93, 0.40, and 1.85 minutes, respec- likelihood through the penalty parameter β, making the rela-
tively. tive contributions of the learned prior and measured PET data
|     |     |     |     |     |     |     | more directly |     | interpretable. | This | modification |     | may | stabilize |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | ---- | ------------ | --- | --- | --------- |
VI. DISCUSSION the PET-data refinement step in the proposed method, which
|                    |        |              |          |                     |           |        | may explain | its    | higher   | image contrast, |              | lower | spatial | bias, and |
| ------------------ | ------ | ------------ | -------- | ------------------- | --------- | ------ | ----------- | ------ | -------- | --------------- | ------------ | ----- | ------- | --------- |
| In this            | study, | we presented |          | flow matching-based |           | PET    | im-         |        |          |                 |              |       |         |           |
|                    |        |              |          |                     |           |        | lower noise | levels | compared | with            | PET-FlowDPS. |       |         |           |
| age reconstruction |        | methods.     | Although |                     | diffusion | models | have        |        |          |                 |              |       |         |           |
Weinvestigatedtheeffectsofthenumberofsamplingsteps
| shown promising |     | performance |     | for PET | reconstruction, |     | in- |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
corporating data consistency into the reverse sampling pro- and the number of EM iterations. The results suggest that
|              |             |     |     |          |                    |     | increasing | the | number | of sampling | steps | does | not necessarily |     |
| ------------ | ----------- | --- | --- | -------- | ------------------ | --- | ---------- | --- | ------ | ----------- | ----- | ---- | --------------- | --- |
| cess remains | challenging |     | and | can lead | to computationally |     |            |     |        |             |       |      |                 |     |
intensive and numerically sensitive updates. In addition, the lead to improved reconstruction performance. As shown in
|            |          |     |                  |         |           |          | Fig. 3,        | increasing | the number   |        | of EM | iterations   | was   | important |
| ---------- | -------- | --- | ---------------- | ------- | --------- | -------- | -------------- | ---------- | ------------ | ------ | ----- | ------------ | ----- | --------- |
| generative | sampling | and | data-consistency |         | updates   | are      | closely        |            |              |        |       |              |       |           |
|            |          |     |                  |         |           |          | for recovering |            | quantitative | uptake |       | and reducing | bias. | This      |
| coupled    | through  | the | prescribed       | reverse | diffusion | process. |                |            |              |        |       |              |       |           |
Flow matching provides a flexible framework for addressing findingsuggeststhatsufficientoptimizationofthesubproblem
|                   |     |          |       |     |                    |     | in (36) | is important | for | quantitative | PET | reconstruction. |     | With |
| ----------------- | --- | -------- | ----- | --- | ------------------ | --- | ------- | ------------ | --- | ------------ | --- | --------------- | --- | ---- |
| these limitations |     | because, | under | a   | linear probability |     | path,   |              |     |              |     |                 |     |      |
the destination image can be directly estimated from an few EM iterations, the refined image may remain influenced
|     |     |     |     |     |     |     | by the | flow-based | prior | and may | not | sufficiently | reflect | the |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ----- | ------- | --- | ------------ | ------- | --- |
intermediatestate.Thispropertyallowsdestinationestimation,
|          |             |     |      |             |     |            | likelihood | term. | However, | the | effects | of these | two parameters |     |
| -------- | ----------- | --- | ---- | ----------- | --- | ---------- | ---------- | ----- | -------- | --- | ------- | -------- | -------------- | --- |
| PET-data | refinement, | and | flow | propagation | to  | be treated | as         |       |          |     |         |          |                |     |
separate steps. Based on this framework, we first developed arenotindependentbecausethetotalnumberofEMiterations
|             |         |               |     |                |                |          | increases | with | the number | of sampling |           | steps. | In the  | proposed |
| ----------- | ------- | ------------- | --- | -------------- | -------------- | -------- | --------- | ---- | ---------- | ----------- | --------- | ------ | ------- | -------- |
| PET-FlowDPS | by      | incorporating |     | PET likelihood |                | guidance | into      |      |            |             |           |        |         |          |
|             |         |               |     |                |                |          | method,   | N EM | iterations | are         | performed |        | at each | of the K |
| FlowDPS.    | We then | proposed      |     | a model-based  | reconstruction |          |           |      |            |             |           |        |         |          |
method in which the PET-data refinement step is formulated sampling steps, resulting in a total of K ×N EM iterations.
Therefore,thedecreaseinPSNRobservedbeyond50sampling
as MAP reconstruction.
A key difference between PET-FlowDPS and the proposed steps may not be solely due to the increased number of sam-
plingsteps,butmayalsoreflecttheeffectoftheincreasedtotal
| method              | lies in | the PET-data |          | refinement | step               | (2) shown | in     |       |             |        |      |      |                     |     |
| ------------------- | ------- | ------------ | -------- | ---------- | ------------------ | --------- | ------ | ----- | ----------- | ------ | ---- | ---- | ------------------- | --- |
|                     |         |              |          |            |                    |           | number | of EM | iterations. | Future | work | will | further investigate |     |
| Fig. 1. PET-FlowDPS |         |              | directly | applies    | a likelihood-based |           | cor-   |       |             |        |      |      |                     |     |
rection to the flow-based destination estimate. Although the the individual and combined effects of these parameters.
PET-specific preconditioning term improves the stability of At the 10% count level, DDS, PET-FlowDPS, and the pro-
thisupdate,itsbehaviorstilldependsontheselectedguidance posed method recovered putamen uptake comparable to that
strength λ and the local log-likelihood gradient. In contrast, ofthefull-dosereference,indicatingthatgenerativepriorscan

9
| MLEM (Full dose) |     | MLEM |     |     | MAPEM |     |     | DDS | FlowDPS |     |     | Proposed |     | Proposed(5) |     |
| ---------------- | --- | ---- | --- | --- | ----- | --- | --- | --- | ------- | --- | --- | -------- | --- | ----------- | --- |
Fig.7. Reconstructionresultsofthreeorthogonalslicesoftheclinical[18F]FDGdataat5%dose.
|     |     |     |     |     |     |     |     | quantitative | accuracy. |     | At the 5% | count | level, | PET-FlowDPS |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | --------- | ----- | ------ | ----------- | --- |
underestimatedputamenuptake,whereastheproposedmethod
0.34 ma0in.3t4a4ined uptake comparable to that of the full0-d.2o5se ref-
|                            |     |     |     |     |     |     |     | erence.                        | This result | suggests    |              | that the | M0A.2P5-based   |            | PET-data |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | ----------- | ----------- | ------------ | -------- | --------------- | ---------- | -------- |
|                            |     |     |     |     |     |     |     | refinement                     | is more     | robust      | 0u.1nder     | noisier  | conditions      |            | than the |
| ).u.a( ekatpu nematuP 0.33 |     |     |     |     |     |     |     |                                |             |             |              |          | 0.1             |            |          |
|                            |     |     |     |     |     |     |     | dir0e.c3t42likelihood-guidance |             |             | update       | used     | in PET-FlowDPS. |            |          |
|                            |     |     |     |     |     |     |     | This                           | study has   | several     | limitations. |          | First, the      | evaluation | was      |
|                            |     |     |     |     |     |     |     | performed                      | using       | 10 clinical | brain        | PET      | datasets        | at         | two low- |
0.32
|     |     |     |     |     |     |     |     | cou0n.3t40levels | (10% | and | 5%). Further |     | evaluation | using | larger |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | --- | ------------ | --- | ---------- | ----- | ------ |
cohorts,differentscanners,andotherradiotracersisneededto
0.31 evaluate the generalizability of the proposed method. Second,
Full dose
|     |     |     |     |     |     |     |     | the0.f3u3l8l | dose reconstructed |     | images | were | used | as references. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------ | --- | ------ | ---- | ---- | -------------- | --- |
MLEM
|     |     |     |     |     |     | MAPEM |     | Thesereferenceimagescontainstatisticalnoiseandcorrection |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
0.30
|     |     |     |     |     |     | DDS |     | errors, which | should |     | be considered |     | when interpreting |     | these |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | ------------- | --- | ----------------- | --- | ----- |
0.005
|     |     |     |     |     |     | FlowDPS     |     | quantitative | measures.   |        | Third, | hyperparameters, |          | such | as 0.005 the |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | ----------- | ------ | ------ | ---------------- | -------- | ---- | ------------ |
|     |     |     |     |     |     | Proposed    |     | 0.336        |             |        |        |                  |          |      |              |
|     |     |     |     |     |     | Proposed(5) |     | number       | of sampling | steps, | the    | number           | of inner | EM   | iterations,  |
0.29
|     |     |     |     |     |     |     |     | and the | penalty | strength, | may | require | adjustment | for | different |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --------- | --- | ------- | ---------- | --- | --------- |
0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.16 0.18 0.20 0.22 0.24
|              |         |              | White matter CoV |            |           |        |        | conditions.Fourth,theformulationoftheproposedmethodre- |                   |     | White matter CoV |          |               |                |         |
| ------------ | ------- | ------------ | ---------------- | ---------- | --------- | ------ | ------ | ------------------------------------------------------ | ----------------- | --- | ---------------- | -------- | ------------- | -------------- | ------- |
|              |         |              |                  |            |           |        |        | lies on several                                        | approximations    |     |                  | for some | probabilistic |                | models. |
|              |         |              |                  |            |           |        |        | Therefore,                                             | the reconstructed |     | images           | should   | not           | be interpreted |         |
| Fig. 8. Mean | putamen | uptake–white |                  | matter CoV | trade-off | curves | across |                                                        |                   |     |                  |          |               |                |         |
the 10 subjects at the 5% count level. Markers were plotted at 10-iteration as exact samples from the PET posterior distribution.
intervalsfrom10to100forMLEM,at10-iterationintervalsfrom10to200
|                | λ         |           |           |         |              |         | λ       |     |     |      |            |     |     |     |     |
| -------------- | --------- | --------- | --------- | ------- | ------------ | ------- | ------- | --- | --- | ---- | ---------- | --- | --- | --- | --- |
| for MAPEM,     | at DDS    | of 0, 10, | 100, 500, | and     | 1000 for     | DDS, at | of 0.8, |     |     |      |            |     |     |     |     |
| 0.9, 1.0, 1.2, | 1.4, 1.6, | 1.8, 2.0, | 2.2, and  | 2.5 for | PET-FlowDPS, | and     | at β    | of  |     |      |            |     |     |     |     |
|                |           |           |           |         |              |         |         |     |     | VII. | CONCLUSION |     |     |     |     |
0.005,0.01,0.02,0.03,0.04,0.05,0.06,0.08,0.1,and0.25forProposedand
Proposed(5).FilledmarkerscorrespondtotheimagesasshowninFig.7. In this work, we proposed flow matching-based PET image
reconstructionmethods.Evaluationsshowedthattheproposed
|          |              |             |     |       |          |             |     | flow-based | method | improved |      | PET image       | quality |     | compared |
| -------- | ------------ | ----------- | --- | ----- | -------- | ----------- | --- | ---------- | ------ | -------- | ---- | --------------- | ------- | --- | -------- |
|          |              |             |     |       |          |             |     | with MLEM, | MAPEM, |          | DDS, | and PET-FlowDPS |         |     | methods. |
| preserve | quantitative | information |     | under | low-dose | conditions. |     |            |        |          |      |                 |         |     |          |
As shown in Fig. 6, DDS exhibited higher spatial standard The results demonstrate that flow matching is a promising
|            |          |            |     |          |             |     |      | generative | prior | for | PET image | reconstruction, |     | offering | a   |
| ---------- | -------- | ---------- | --- | -------- | ----------- | --- | ---- | ---------- | ----- | --- | --------- | --------------- | --- | -------- | --- |
| deviations | than the | flow-based |     | methods. | PET-FlowDPS |     | pro- |            |       |     |           |                 |     |          |     |
favorablebalancebetweenquantitativeaccuracyanddenoising
videdlowerspatialvariabilityatthecostofrelativelyincreased
performance.
| spatial bias. | In         | contrast, | the      | proposed | method      | maintained |       |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --------- | -------- | -------- | ----------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| bias levels   | comparable |           | to those | of MLEM, |             | MAPEM,     | and   |     |     |     |     |     |     |     |     |
| DDS while     | achieving  | lower     | spatial  | standard | deviations. |            | These |     |     |     |     |     |     |     |     |
REFERENCES
| results show | that             | the proposed |             | method       | provides | a           | more fa- |               |              |        |                 |      |            |                |            |
| ------------ | ---------------- | ------------ | ----------- | ------------ | -------- | ----------- | -------- | ------------- | ------------ | ------ | --------------- | ---- | ---------- | -------------- | ---------- |
|              |                  |              |             |              |          |             |          | [1] L. A.     | Shepp        | and Y. | Vardi, “Maximum |      | likelihood | reconstruction | for        |
| vorable      | bias–variability | balance      |             | than the     | other    | methods,    | with     |               |              |        |                 |      |            |                |            |
|              |                  |              |             |              |          |             |          | emission      | tomography,” |        | IEEE Trans.     | Med. | Imaging,   | vol. 1,        | no. 2, pp. |
| both low     | bias and         | low          | variability | contributing |          | to improved |          | 113–122,1982. |              |        |                 |      |            |                |            |

10
[2] H.M.HudsonandR.S.Larkin,“Acceleratedimagereconstructionusing [26] H.Chung,J.Kim,M.T.Mccann,M.L.Klasky,andJ.C.Ye,“Diffusion
orderedsubsetsofprojectiondata,”IEEETrans.Med.Imaging,vol.13, Posterior Sampling for General Noisy Inverse Problems,” in Proc. Int.
| no.4,pp.601–609,1994. |     |     |     |     |     |     |     | Conf.Learn.Represent.(ICLR),2023. |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[3] P.J.Green,“Bayesianreconstructionsfromemissiontomographydata [27] H. Chung, S. Lee, and J. C. Ye, “Decomposed Diffusion Sampler for
using a modified EM algorithm,” IEEE Trans. Med. Imaging, vol. 9, AcceleratingLarge-ScaleInverseProblems,”inProc.Int.Conf.Learn.
| no.1,pp.84–93,1990. |            |     |          |             |              |     |               | Represent.(ICLR),2024. |     |         |       |        |             |     |                 |
| ------------------- | ---------- | --- | -------- | ----------- | ------------ | --- | ------------- | ---------------------- | --- | ------- | ----- | ------ | ----------- | --- | --------------- |
|                     |            |     |          |             |              |     |               | [28] G. Webber,        | Y.  | Mizuno, | O. D. | Howes, | A. Hammers, |     | A. P. King, and |
| [4] A. R.           | D. Pierro, | “A  | modified | expectation | maximization |     | algorithm for |                        |     |         |       |        |             |     |                 |
penalized likelihood estimation in emission tomography,” IEEE Trans. A.J.Reader,“Likelihood-ScheduledScore-BasedGenerativeModeling
Med.Imaging,vol.14,no.1,pp.132–137,1995. for Fully 3D PET Image Reconstruction,” IEEE Trans. Med. Imaging,
[5] J.NuytsandJ.A.Fessler,“Apenalized-likelihoodimagereconstruction vol.44,no.11,pp.4445–4456,2025.
methodforemissiontomography,comparedtopostsmoothedmaximum- [29] S. Bae, J. S. Lee, and K. Gong, “Joint reconstruction of activity and
|     |     |     |     |     |     |     |     | attenuation | for | pet imaging | with | diffusion | prior,” | in 2025 | IEEE 22nd |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ---- | --------- | ------- | ------- | --------- |
likelihoodwithmatchedspatialresolution,”IEEETrans.Med.Imaging,
vol.22,no.9,pp.1042–1052,2003. InternationalSymposiumonBiomedicalImaging(ISBI). IEEE,2025,
| [6] J.QiandR.M.Leahy,“Iterativereconstructiontechniquesinemission |     |     |     |     |     |     |     | pp.1–4. |     |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
computed tomography,” Phys. Med. Biol., vol. 51, no. 15, pp. R541– [30] C.Phung-Ngocetal.,“JointReconstructionofActivityandAttenuation
R578,2006. inPETbyDiffusionPosteriorSamplinginWaveletCoefficientSpace,”
|           |        |        |             |     |                  |     |               | IEEE | Trans. | Radiat. | Plasma | Med. Sci., | 2026. | [Online]. | Available: |
| --------- | ------ | ------ | ----------- | --- | ---------------- | --- | ------------- | ---- | ------ | ------- | ------ | ---------- | ----- | --------- | ---------- |
| [7] J. Qi | and R. | Leahy, | “Resolution | and | noise properties |     | of MAP recon- |      |        |         |        |            |       |           |            |
structionforfully3-DPET,”IEEETrans.Med.Imaging,vol.19,no.5, https://doi.org/10.1109/TRPMS.2026.3706239
pp.493–506,2000. [31] F. Hashimoto and K. Gong, “PET image reconstruction using deep
[8] A.J.Reader,G.Corda,A.Mehranian,C.daCosta-Luis,S.Ellis,and diffusion image prior,” IEEE Trans. Med. Imaging, vol. 45, no. 6, pp.
| J. A. | Schnabel, | “Deep | learning | for PET | image | reconstruction,” | IEEE | 2628–2638,2026. |     |        |            |     |            |               |       |
| ----- | --------- | ----- | -------- | ------- | ----- | ---------------- | ---- | --------------- | --- | ------ | ---------- | --- | ---------- | ------------- | ----- |
|       |           |       |          |         |       |                  |      | [32] R. Yilmaz, | Y.  | Wu, J. | Stegmaier, | and | V. Schulz, | “PET-Adapter: | Test- |
Trans.Radiat.PlasmaMed.Sci.,vol.5,no.1,pp.1–25,2021.
|     |     |     |     |     |     |     |     | Time | Domain | Adaptation | for | Full and | Limited-Angle |     | PET Image |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ---------- | --- | -------- | ------------- | --- | --------- |
[9] F.Hashimoto,Y.Onishi,K.Ote,H.Tashima,A.J.Reader,andT.Ya-
maya,“Deeplearning-basedpetimagedenoisingandreconstruction:a Reconstruction,”2026,arXiv:2605.08030.
review,”Radiol.Phys.Technol.,vol.17,no.1,pp.24–46,2024. [33] X. Liu, C. Gong, and Q. Liu, “Flow Straight and Fast: Learning to
|              |     |                   |     |             |     |       |                 | Generate | and | Transfer | Data with | Rectified | Flow,” | in  | Proc. Int. Conf. |
| ------------ | --- | ----------------- | --- | ----------- | --- | ----- | --------------- | -------- | --- | -------- | --------- | --------- | ------ | --- | ---------------- |
| [10] K. Miwa | et  | al., “Innovations |     | in clinical | PET | image | reconstruction: |          |     |          |           |           |        |     |                  |
Learn.Represent.(ICLR),2023.
advancesinBayesianpenalizedlikelihoodalgorithmanddeeplearning,”
|     |     |     |     |     |     |     |     | [34] J. Kim, | B. S. | Kim, and | J. C. | Ye, “FlowDPS: |     | Flow-Driven | Posterior |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | -------- | ----- | ------------- | --- | ----------- | --------- |
Ann.Nucl.Med.,vol.39,no.9,pp.875–898,2025.
SamplingforInverseProblems,”inProc.IEEE/CVFInt.Conf.Comput.
| [11] K. Gong | et  | al., “Iterative | PET | Image | Reconstruction |     | Using Convo- |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --- | ----- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
lutional Neural Network Representation,” IEEE Trans. Med. Imaging, Vis.(ICCV),2025,pp.12328–12337.
|     |     |     |     |     |     |     |     | [35] M. | Pourya, B. | E. Rawas, | and | M. Unser, | “Flower: | A   | Flow-Matching |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --------- | --- | --------- | -------- | --- | ------------- |
vol.38,no.3,pp.675–685,2019.
|                   |     |        |            |              |     |      |              | Solver | for Inverse | Problems,” |     | in Proc. | Int. Conf. | Learn. | Represent. |
| ----------------- | --- | ------ | ---------- | ------------ | --- | ---- | ------------ | ------ | ----------- | ---------- | --- | -------- | ---------- | ------ | ---------- |
| [12] A. Mehranian |     | and A. | J. Reader, | “Model-Based |     | Deep | Learning PET |        |             |            |     |          |            |        |            |
(ICLR),2026.
| Image | Reconstruction |     | Using | Forward–Backward |     | Splitting | Expecta- |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | ----- | ---------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[36] S.T.Martin,A.Gagneux,P.Hagemann,andG.Steidl,“PnP-Flow:Plug-
tion–Maximization,”IEEETrans.Radiat.PlasmaMed.Sci.,vol.5,no.1,
pp.54–64,2021. and-Play Image Restoration with Flow Matching,” in Proc. Int. Conf.
Learn.Represent.(ICLR),2025.
| [13] J. Whang, |     | M. Delbracio, | H.  | Talebi, | C. Saharia, | A. G. | Dimakis, and |              |         |        |       |                       |     |     |              |
| -------------- | --- | ------------- | --- | ------- | ----------- | ----- | ------------ | ------------ | ------- | ------ | ----- | --------------------- | --- | --- | ------------ |
|                |     |               |     |         |             |       |              | [37] H. Ran, | H. Liu, | and B. | Zhao, | “Manifold-constrained |     | pet | image recon- |
P.Milanfar,“DeblurringviaStochasticRefinement,”inProc.IEEE/CVF
structionwithflow-matchingpriorsviaadmm,”inIEEEConf.Comput.
Conf.Comput.Vis.PatternRecognit.(CVPR),2022,pp.16293–16303.
ImagingUsingSynth.Apertures(CISA),2026,pp.1–5.
[14] C.Saharia,J.Ho,W.Chan,T.Salimans,D.J.Fleet,andM.Norouzi,
“ImageSuper-ResolutionviaIterativeRefinement,”IEEETrans.Pattern [38] Y.Lipman,R.T.Q.Chen,H.Ben-Hamu,M.Nickel,andM.Le,“Flow
matchingforgenerativemodeling,”inProc.Int.Conf.Learn.Represent.
Anal.Mach.Intell.,vol.45,no.4,pp.4713–4726,2023.
(ICLR),2023.
[15] J.Ho,A.Jain,andP.Abbeel,“Denoisingdiffusionprobabilisticmodels,”
|     |     |     |     |     |     |     |     | [39] K. Lange, | A.  | R. Hunter, | and | I. Yang, | “Optimization |     | Transfer Using |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | -------- | ------------- | --- | -------------- |
inAdv.NeuralInf.Process.Syst.,2020.
SurrogateObjectiveFunctions,”J.Comput.Graph.Stat.,vol.9,no.1,
| [16] Y. Song, | J.  | Sohl-Dickstein, | D.  | P. Kingma, | A.  | Kumar, | S. Ermon, and |     |     |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ---------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.1–20,2000.
B. Poole, “Score-based generative modeling through stochastic differ- [40] G. Wang and J. Qi, “Penalized likelihood PET image reconstruction
entialequations,”inProc.Int.Conf.Learn.Represent.(ICLR),2020.
|               |     |          |       |         |            |         |            | using | patch-based | edge-preserving |     | regularization,” |     | IEEE | Trans.Med. |
| ------------- | --- | -------- | ----- | ------- | ---------- | ------- | ---------- | ----- | ----------- | --------------- | --- | ---------------- | --- | ---- | ---------- |
| [17] K. Gong, | K.  | Johnson, | G. E. | Fakhri, | Q. Li, and | T. Pan, | “PET image |       |             |                 |     |                  |     |      |            |
Imaging,vol.31,no.12,pp.2194–2204,2012.
| denoising | based | on  | denoising | diffusion | probabilistic | model,” | Eur. | J.         |         |         |         |       |            |     |               |
| --------- | ----- | --- | --------- | --------- | ------------- | ------- | ---- | ---------- | ------- | ------- | ------- | ----- | ---------- | --- | ------------- |
|           |       |     |           |           |               |         |      | [41] S. D. | Jamadar | et al., | “Monash | DaCRA | fPET-fMRI: |     | A dataset for |
Nucl.Med.Mol.Imaging,vol.51,pp.358–368,2024.
|     |     |     |     |     |     |     |     | comparison | of  | radiotracer | administration |     | for high | temporal | resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | -------------- | --- | -------- | -------- | ---------- |
[18] S. Pan et al., “Full-dose whole-body PET synthesis from low-dose functionalFDG-PET,”GigaScience,vol.11,pp.1–12,2022.
PETusinghigh-efficiencydenoisingdiffusionprobabilisticmodel:PET [42] P. J. Markiewicz et al., “NiftyPET: a High-throughput Software Plat-
consistencymodel,”Med.Phys.,vol.51,no.8,pp.5468–5478,2024.
|            |         |         |            |     |           |           |          | form | for High | Quantitative | Accuracy |     | and Precision | PET | Imaging and |
| ---------- | ------- | ------- | ---------- | --- | --------- | --------- | -------- | ---- | -------- | ------------ | -------- | --- | ------------- | --- | ----------- |
| [19] B. Yu | et al., | “Robust | whole-body |     | PET image | denoising | using 3D |      |          |              |          |     |               |     |             |
Analysis,”Neuroinform.,vol.16,no.1,pp.95–115,2018.
diffusion models: evaluation across various scanners, tracers, and dose [43] G. Schramm and K. Thielemans, “PARALLELPROJ—an open-source
levels,”Eur.J.Nucl.Med.Mol.Imaging,vol.52,pp.2549–2562,2025. framework for fast calculation of projections in tomography,” Front.
[20] H.Xieetal.,“Dose-awarediffusionmodelfor3DPETimagedenoising: Nucl.Med.,vol.3,2024.
Multi-institutionalvalidationwithreaderstudyandreallow-dosedata,”
|     |     |     |     |     |     |     |     | [44] J. Nuyts, | D. Beque´, | P.  | Dupont, | and L. | Mortelmans, | “A  | concave prior |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | --- | ------- | ------ | ----------- | --- | ------------- |
Med.ImageAnal.,vol.111,2026,art.no.104039.
penalizingrelativedifferencesformaximum-a-posteriorireconstruction
[21] T.Xieetal.,“SynthesizingPETimagesfromhigh-fieldandultra-high- in emission tomography,” IEEE Trans. Nucl. Sci., vol. 49, no. 1, pp.
| field | MR images | using | joint | diffusion | attention | model,” | Med. Phys., | 56–60,2002. |     |     |     |     |     |     |     |
| ----- | --------- | ----- | ----- | --------- | --------- | ------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
vol.51,no.8,pp.5250–5269,2024. [45] K.Miwaetal.,“Impactofγ factorinthepenaltyfunctionofBayesian
[22] Y. Gong, S.-i. Jang, W. Shao, Y. Su, and K. Gong, “TauGenNet: penalizedlikelihoodreconstruction(Q.Clear)toachievehigh-resolution
Plasma-DrivenTauPETImageSynthesisviaText-Guided3DDiffusion
PETimages,”EJNMMIPhys.,vol.10,2023,art.no.3.
Models,” IEEE Trans. Radiat. Plasma Med. Sci., 2026. [Online]. [46] B.Fischl,“FreeSurfer,”NeuroImage,vol.62,no.2,pp.774–781,2012.
Available:https://doi.org/10.1109/TRPMS.2026.3688162
| [23] T. Chen | et  | al., “2.5D | Multi-View | Averaging |     | Diffusion | Model for 3D |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ---------- | --------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
MedicalImageTranslation:ApplicationtoLow-CountPETReconstruc-
tionWithCT-LessAttenuationCorrection,”IEEETrans.Med.Imaging,
vol.44,no.11,pp.4239–4250,2025.
[24] M.J.Cho,H.S.Shim,S.Kim,andJ.S.Lee,“GPDM:generation-prior
diffusionmodelforaccelerateddirectattenuationandscattercorrection
ofwhole-body18F-FDGPET,”Phys.Med.Biol.,vol.71,no.12,2026,
art.no.125011.
| [25] I. R.       | Singh | et al., “Score-Based |        | Generative  |          | Models | for PET Image |     |     |     |     |     |     |     |     |
| ---------------- | ----- | -------------------- | ------ | ----------- | -------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reconstruction,” |       | Mach.                | Learn. | for Biomed. | Imaging, | vol.   | 2, pp. 547–   |     |     |     |     |     |     |     |     |
585,2024.
---- END DOCUMENT ----
