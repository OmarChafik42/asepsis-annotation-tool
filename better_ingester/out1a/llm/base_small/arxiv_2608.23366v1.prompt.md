Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
TRANSFORM-BASED MULTILINEAR ALGEBRA VIA
TENSOR DECOMPOSITION∗
YIDAN MEI†, SHENGHAN MEI‡, ZIQIN HE§, AND CAN CHEN¶
Abstract. Transform-based tensor products, including the T-product and its more general
form,namelythehigher-ordertensor-tensorproduct,havebecomefundamentaltoolsformultilinear
data analysis in applications such as image processing, signal reconstruction, and robotics. While
invertibletransformsenabletensorcomputationstobecarriedoutviamatrixoperationsinthetrans-
formdomain,theresultingstorageandcomputationalcostsremainprohibitiveforhigh-dimensional,
higher-order tensors. To address this challenge, we integrate low-rank tensor decomposition tech-
niques,specificallytensortraindecomposition(TTD)andhierarchicalTuckerdecomposition(HTD),
into transform-based multilinear algebra to improve computational and memory efficiency. In par-
ticular, we develop TTD- and HTD-based formulations for the T-product and its associated key
algebra,suchasblockdiagonalizationandtensorsingularvaluedecomposition,byoperatingdirectly
onthefactormatricesortensorsofthedecompositions. Theframeworkisfurthergeneralizedtothe
higher-order tensor-tensor product and appliedto multilinear model order reduction problems. We
demonstratetheeffectiveness andefficiencyofourframeworkwithnumericalexamples.
Key words. transform-basedmultilinear algebra, low-ranktensor decomposition, tensor train
decomposition, hierarchicalTuckerdecomposition, tensorsingularvaluedecomposition
MSC codes. 15A18, 15A23,15A69,65F55
1. Introduction. Multidimensionaldatahavebecomeubiquitousinmodernsci-
entific and engineering applications, including image and video processing [1, 53, 55],
biomedical measurement analysis [2, 46], robotics [48, 52], and networked dynamical
systems[10,12,47]. Intheseapplications,thedataareinherentlymultiway,withspa-
tial, temporal, spectral, or modal relationships encoded across multiple indices. For
example,videosequencescontaincoupledspatialandtemporalcorrelations,whilenet-
worked and biomedical systems often exhibit interactions across multiple functional
or physical modes. Traditional approaches frequently reshape tensors into vectors or
matrices through unfolding in order to apply classical linear algebra techniques. Al-
though this may simplify computations, it often destroys intrinsic multilinear struc-
ture, weakens correlations across modes, and leads to redundant high-dimensional
representations [13, 33, 44]. These limitations become increasingly pronounced as
the size and order of the data grow. Multilinear algebra therefore provides a natural
framework for modeling and processing such data while preserving their underlying
multiway structure, enabling more compact representations and more effective ex-
ploitation of correlations across multiple dimensions simultaneously.
Among existing tensor frameworks, transform-based tensor algebra, particularly
theT-product,providesaneffectiveoperator-basedframeworkforthird-ordertensors
[7, 8, 25, 26, 30, 39]. By combining block-circulant representations with invertible
transforms, the T-product induces tensor analogues of many classical matrix oper-
∗SubmittedtotheeditorsAugust25,2026.
Funding: Fundinginformationgoeshere.
†Department of Statistics and Data Science, Yale University, New Haven, CT 06511, USA (yi-
dan.mei@yale.edu).
‡DepartmentofMathematics,UniversityofNorthCarolinaatChapelHill,ChapelHill,NC27599,
USA(shmei@unc.edu).
§DepartmentofMathematics,UniversityofNorthCarolinaatChapelHill,ChapelHill,NC27599,
USA(zhe21@unc.edu).
¶SchoolofDataandInformationSciences,DepartmentofMathematics,andDepartmentofBio-
statistics,UniversityofNorthCarolinaatChapelHill,ChapelHill,NC27599,USA(canc@unc.edu).
1
6202
guA
42
]AN.htam[
1v66332.8062:viXra

ations, including inversion, eigendecomposition, and tensor singular value decompo-
sition (T-SVD), while enabling these operations to be computed through decoupled
matrix problems in the transform domain. Owing to its elegant algebraic structure
and computational efficiency, the T-product framework has been successfully applied
toawiderangeofproblems,includingposeestimationandrecognition[17,21],tensor
completion and robust principal component analysis [18, 28, 58], multi-view learning
[50, 54, 56], signal processing [19, 43, 45], tensor linear systems [31], and multilinear
systemsandcontrol[15,20,22,32,35,37,38]. Motivatedbytheincreasingprevalence
of higher-order data, several generalizations of transform-based tensor algebra have
beendevelopedbeyondthethird-ordersetting. Inparticular,thehigher-ordertensor-
tensor product framework generalizes the T-product to tensors of arbitrary order by
applying separable transforms along multiple modes, thereby reducing tensor oper-
ations to collections of independent matrix computations in the transform domain
while preserving the underlying multiway structure [24, 36, 42, 51].
AlthoughtheT-productandrelatedtransform-basedtensoralgebrahaveenabled
a broad range of applications, they do not fully eliminate the underlying compu-
tational bottleneck. For large-scale problems, both storage and runtime can still
become prohibitive because the computations rely on full tensor representations,
block-circulant embeddings, and repeated dense matrix factorizations in the trans-
form domain. These costs grow further as either the tensor order or individual mode
dimensions increase, making scalability a critical concern. The issue is particularly
pronounced in high-dimensional multilinear systems analysis and control, where ten-
sorproducts,spectralcomputations,anddecomposition-basedroutinesmustoftenbe
performed repeatedly within iterative algorithms [20, 35, 37]. Similar challenges also
arise in high-dimensional imaging and scientific computing, where large mode sizes
lead to substantial memory demands and computational overhead [3, 5, 9].
To address this challenge, it is natural to combine transform-based multilin-
ear algebra with low-rank tensor decompositions. A substantial body of work has
shown that tensor decompositions, including CANDECOMP/PARAFAC decomposi-
tion [4, 27], higher-order singular value decomposition [6, 14], tensor train decompo-
sition (TTD) [40, 41], and hierarchical Tucker decomposition (HTD) [16], can repre-
senthigh-dimensionaltensorsinacompactformwhilepreservingessentialmultilinear
structure [49]. In this work, we focus on TTD and HTD, which are particularly well
suited for higher-order problems due to their numerically stable and storage-efficient
representations and their ability to support key numerical operations, such as or-
thogonalization,truncation,andlinear-system-relatedcomputations,directly onlow-
dimensionalcoretensorsorhierarchicalfactorsratherthanonfulltensors. Moreover,
bothformatshavedemonstratedstrongperformanceinlarge-scalecomputationalset-
tings and have been successfully employed in dynamical low-rank approximation for
time-dependent tensor problems [29, 34]. These characteristics make TTD and HTD
particularly attractive for accelerating transform-based tensor operations in regimes
where both dimensionality and computational cost are substantial.
The primary contribution of this work is a tensor decomposition-based compu-
tational framework for transform-based multilinear algebra. We reformulate the T-
product and related operations directly within TTD and HTD formats, so that the
dominant computations are performed on compressed core tensors or factors with-
out explicitly forming or reconstructing full tensors. In particular, we derive TTD-
and HTD-based formulations for block diagonalization, the T-product, and T-SVD,
andprovideadetailedcomputationalcomplexityanalysisofthe resultingalgorithms.
We further extend these constructions from the third-order setting to the higher-
2

ordertensor-tensorproductframework. Finally,wedemonstratetheeffectivenessand
efficiency ofthe proposedapproachthroughnumericalexamples andillustrateits ap-
plicability to model order reduction in multilinear dynamical systems. To support
reproducibility and practical use, we also provide MATLAB codes implementing the
main decomposition-based tensor operations developed in this work.
Theremainderofthisarticleisorganizedasfollows. Section2reviewstensorpre-
liminaries, including the T-product, the higher-order tensor-tensor product, and the
fundamentals of TTD and HTD. Section 3 develops TTD- and HTD-based formula-
tions for third-order transform-basedtensor algebra,including block diagonalization,
the T-product, and T-SVD. Section 4 extends these constructions to higher-order
tensor-tensorproducts. Section5presentsnumericalexperimentsillustratingtheper-
formance of the proposed methods and their application to multilinear model order
reduction. Section 6 concludes with future research directions.
2. Preliminaries. Tensors provide a natural representation for multidimen-
sional data, extending vector and matrix algebrato higher orders[11, 27]. The order
of a tensor refers to the number of its dimensions, with eachdimension referredto as
a mode. A kth-order tensor is typically denoted by T Rn1×n2×···×nk. Many matrix
∈
operations and decompositions can be extended to the tensor setting in a consistent
manner. Forconvenience,weadoptMATLAB colonnotation“:”todenoteallentries
alongagiventensordimension. Forexample,thefrontalslices,whicharematricesob-
tainedbyfixingallindicesexceptthefirsttwo,ofathird-ordertensorT Rn1×n2×n3
∈
can be written as T(:,:,j ) for j =1,2,...,n .
3 3 3
2.1. T-product. The T-product extends matrix multiplication to third-order
tensors by enabling tensor multiplication through circular convolution operations [7,
25, 26]. A key component of this framework is the use of block-circulant operators,
which represent a tensor as a structured block matrix whose multiplication can be
performed using standard matrix operations. Complementing this construction, the
unfoldingoperatorreshapesatensorintoablockcolumnmatrix,establishingabridge
between tensor representations and classical matrix multiplication. Given a third-
order tensor T Rn1×n2×n3, the two operators are defined as
∈
T(:,:,1) T(:,:,n ) T(:,:,2)
3
···
T(:,:,2) T(:,:,1) T(:,:,3)
bcirc(T)=
. . . . . .
·
.
·
.
·
. . . .

∈
Rn1n3×n2n3,
 
T(:,:,n ) T(:,:,n 1) T(:,:,1)
 3 3 − ··· 
unfold(T)=

T(:,:,1)⊤ T(:,:,2)⊤ T(:,:,n )⊤
⊤
Rn1n3×n2.
3
··· ∈
The reverse operatio (cid:2) n fold() satisfies fold(unfold(T)) = T(cid:3) . With these operators,
·
the third-order T-product is defined as follows.
Definition 2.1 (T-product). The T-product between two third-order tensors
T Rn1×l×n3 and S Rl×n2×n3, denoted by T⋆S, is defined as
∈ ∈
T⋆S=fold bcirc(T)unfold(S) Rn1×n2×n3.
∈
(cid:0) (cid:1)
The T-product naturally induces tensor analogues of standard matrix concepts.
A tensor I Rn×n×n3 is said to be the T-identity tensor if its first frontal slice
∈
I(:,:,1) is an identity matrix, and the following slices I(:,:,j ), j = 2,3,...,n are
3 3 3
all zeros. The T-transpose of a tensor T Rn1×n2×n3, denoted by T⊤, is defined as
∈
3

transposingeachfrontalsliceT(:,:,j )andthenreversingthe orderofthe transposed
3
slices from 2 to n
3
. The T-inverse of a tensor T Rn×n×n3, denoted by T−1, is
∈
defined such that T⋆T−1 = T−1⋆T = I, where I is the identity tensor. The tensor
T Rn×n×n3 issaidtobeT-orthogonalifT⋆T⊤ =T⊤⋆T =I. AtensorT Rn×n×n3
∈ ∈
is called F-diagonal if each frontal slice T(:,:,j ) is a diagonal matrix. Note that we
3
use the same notations for matrix and T-productoperations(e.g., transpose,inverse,
etc.) whenever no ambiguity arises. More importantly, the classical singular value
decomposition (SVD) admits a natural extension to tensors within the T-product
framework, known as tensor singular value decomposition (T-SVD) [57, 58].
Definition 2.2 (T-SVD). The T-SVD of a tensor T Rn1×n2×n3 is defined as
∈
(2.1) T =U⋆S⋆V⊤,
where U Rn1×n1×n3 and V Rn2×n2×n3 are T-orthogonal, and S Rn1×n2×n3 is
an F-rect ∈ angular diagonal tens ∈ or. The tubes S
jj:
Rn3 are referred to ∈ as the singular
∈
tubes of T for j =1,2,...,min n ,n .
1 2
{ }
T-SVD can be computed by exploiting the discrete Fourier transform together
with the classical matrix SVD. In particular, a block-circulant matrix can be block-
diagonalized through left and right multiplication by block Fourier matrices. For a
third-order tensor T Rn1×n2×n3, the Fourier transform of its block-circulant repre-
∈
sentation, denoted by bcirc(T) , is expressed as
F{ }
(2.2) bcirc(T) =(F I )bcirc(T)(F∗ I )=blkdiag(T ,T ,...,T ),
F{ } n3 ⊗ n1 n3 ⊗ n2 1 2 n3
where blkdiag() denotes the MATLAB block diagonal operator, represents the
m
Kr
a
o
t
n
ri
e
x
c
,
k
a
e
n
r
d
pr
F
o
n
d
3
u · c
∈
t, C∗
n3
d
×
e
n
n
3
ot
is
es
th
t
e
he
di
c
s
o
c
n
re
ju
te
ga
F
t
o
e
u
t
r
r
i
a
er
ns
t
p
ra
o
n
se
s
,
fo
I
r
n
m
1 ∈
ma
R
tr
n
i
1
x
×n
d
⊗ 1
efi
i
n
s
e
t
d
he
as
identity
1 1 1 1
···
1 ω ω2 ω−1
1
F n3 = √n 3 . . . . . . . . . · . · . · . . . . ,
 
1 ωn3−1 ω2(n3−1) ω(n3−1)2
 ··· 
 
with ω =exp( 2πi)(i is the imaginarynumber here). Next, the matrix SVD of each
−n3
diagonalblock matrix is computed as T =U S V∗ for j =1,2,...,n . Finally,
j3 j3 j3 j3 3 3
the factor tensors U, S, and V are obtained by applying the inverse discrete Fourier
transform to the collections of matrices U , S , and V , respectively. It is worth
j3 j3 j3
noting that the T-SVD of T differs from the matrix SVD of bcirc(T) since the block
circulant matrix bcirc(S) is not diagonal.
2.2. Higher-order tensor-tensor product. The higher-order tensor-tensor
product, introduced in [42], generalizes the T-product to tensors of arbitrary order,
enabling transform-based tensor operations to be performed in the higher-order set-
ting. To define the higher-ordertensor-tensorproduct, we firstintroduce two notions
of tensor multiplication.
Definition 2.3 (Tensor-matrix multiplication). The mode-p tensor-matrix mul-
tiplicationforakth-ordertensorT Rn1×n2×···×nk andamatrixA Rm×np,denoted
by T
p
A Rn1×n2×···×np−1×m×np ∈ +1×···×nk, is defined as ∈
× ∈
np
(T A)(j ,j ,...,j ,i,j ,...,j )= A(i,j )T(j ,j ,...,j ,j ,j ,...,j ).
p 1 2 p−1 p+1 k p 1 2 p−1 p p+1 k
×
j Xp=1
4

Definition 2.4 (Facewise product). For kth-order tensors T Rn1×ℓ×n3×···×nk
and S Rℓ×n2×n3×···×nk, the facewise product between the two te ∈ nsors, denoted by
T ∆ S ∈ Rn1×n2×n3×n4×···×nk, is defined as
∈
(T ∆ S)(:,:,j ,j ,...,j )=T(:,:,j ,j ,...,j )S(:,:,j ,j ,...,j ),
3 4 k 3 4 k 3 4 k
for every index tuple j ,j ,...,j .
3 4 k
Definition 2.5 (Higher-ordertensor-tensorproduct). For two kth-order tensors
T Rn1×ℓ×n3×···×nk and S Rℓ×n2×n3×···×nk, the higher-order tensor-tensor product
bet ∈ ween the two tensors, den ∈ oted by T⋆
H
S Rn1×n2×n3×n4×···×nk, is defined as
∈
(2.3) T⋆ S= T ∆ S F−1 F−1 F−1,
H × 3 n3 × 4 n4 × 5 ···× k nk
(cid:0) (cid:1)
where T =T
×
3 F n3× 4 F n4× e5
···
e
×
k F nk and S=S
×
3 F n3× 4 F n4× 5
···×
k F nk are
obtained by applying the discrete Fourier transform matrices along modes 3 through
k via teensor-matrix multiplication. e
Applying the discrete Fourier transform along modes 3 through k decouples the
computation into n n n independent matrix computations in the Fourier do-
3 4 k
···
main,therebyextendingT-product-basedalgebraicstructuressuchasT-SVDtokth-
ordertensors. Moregenerally,anyinvertiblelineartransformcanreplacethe discrete
Fouriertransform,yieldingabroaderclassoftransform-basedtensor-tensorproducts.
2.3. Tensordecomposition. Tensordecompositionisafundamentaltechnique
for representing high-dimensional tensors using lower dimensional components [27].
Among the many tensor decomposition formats, this work focuses on tensor train
decomposition(TTD)[40]andhierarchicalTuckerdecomposition(HTD)[16]because
of their favorable numerical stability and strong compression capability.
Definition 2.6 (TTD). Let T Rn1×n2×···×nk be a kth-order tensor. The TTD
∈
of T is defined as
r0 r1 rk
T(j ,j ,...,j )= G (α ,j ,α )G (α ,j ,α ) G (α ,j ,α ),
1 2 k 1 0 1 1 2 1 2 2 k k−1 k k
··· ···
α X0=1α X1=1 α Xk=1
whereG
t ∈
Rrt−1×nt×rt,t=1,2,...,k,arereferredtoasthecoretensors,and
{
r
t }
k
t=0
are called the TT-ranks with r =r =1.
0 k
Definition 2.7 (HTD). Let T Rn1×n2×···×nk be a kth-order tensor, and let
∈ T
be a dimension tree associated with the index set D = 1,2,...,k . The HTD of T is
{ }
defined recursively on as
T
rt1 rt2
U (:,α )= B (α ,α ,α )U (:,α ) U (:,α ),
t t t t1 t2 t t1 t1
⊗
t2 t2
α Xt1 =1α Xt2 =1
where t and t denote the two child nodes of node t in the dimension tree , B
1 2 t
Rrt1 ×rt2 ×rt is the transfer tensor associated with node t, and r
t
is the corres T pondin ∈ g
hierarchical rank. For each leaf node t 1,2,...,k , the factor matrices satisfy
U
t
Rnt×rt. Theoriginal tensorT isreco ∈ ver { edrecursiv } elybycontractingthetransfer
∈
tensors and factor matrices from the leaf nodes to the root of the dimension tree.
It is worth noting that for third-order tensors, HTD can be equivalently written
as the standard Tucker decomposition (TD), up to a reparameterization of the core
5

tensor. Specifically, given a third-order tensor T Rn1×n2×n3, its TD is defined as
∈
T =G U U U ,
1 1 2 2 3 3
× × ×
where G Rr1×r2×r3 is referred to as the core tensor, and U
t
Rnt×rt, t = 1,2,3,
∈ ∈
arethefactormatrices. Inthiscase,theHTDofT reducestoasingle-leveldimension
tree,anditstransfertensorscanbeabsorbedintoasingleTuckercoretensor,thereby
yielding an equivalent representation. We will adopt the standard Tucker format in
place of HTD for the development of the T-product algebra.
3. TTD- and HTD-based T-product algebra. In this section, we develop
decomposition-based formulations for the fundamental operations of the T-product
algebra,includingblockdiagonalization,theT-product,andT-SVD,byexploitingthe
low-rankstructuresprovidedbyTTDandHTD.Specifically,wereformulatetheseop-
erationsdirectlyintermsofthedecompositionfactors,enablingefficientcomputation
without reconstructing the full tensors.
3.1. Block diagonalization. Block diagonalization plays a central role in T-
productalgebra,as it transformsthe block-circulantstructure of a third-ordertensor
into a collection of independent matrices in the Fourier domain. Specifically, given
a Cn t 1 h × ir n d 2 - , o j r 3 de = r t 1 e , n 2 s , o . r . T .,n ∈ 3 , R a n s 1× d n e 2 fi × n n e 3 d , w in e ( c 2 o . m 2) p . u A te lt i h ts ou d g ia h g t o h n e al fa b s l t oc F k ou m r a ie t r ric tr e a s n T sf j o 3 rm ∈
provides a direct and efficient way to perform this operation, the computation can
become expensive for large-scale tensors. Notably, if a low-rank TTD or HTD of T
is available, the diagonal block matrices T can be constructed more efficiently by
j3
exploiting the factorized structure of the tensor.
Proposition 3.1 (TTD-based block diagonalization). Let T Rn1×n2×n3 be
a third-order tensor in the TTD format with core tensors G
1
R∈
1×n1×r1, G
2
Rr1×n2×r2, and G
3
Rr2×n3×1. Then the diagonal block matrices ∈ of T in the Fourie ∈ r
∈
domain are computed as
r1 r2
(3.1) T (j ,j )= G (j ,α )G (α ,j ,α )G (α ,j ),
j3 1 2 1 1 1 2 1 2 2 3 2 3
α X1=1α X2=1
e
where G =G F , for j =1,2,...,n .
3 3
×
2 n3 3 3
Proof. FromthedefinitionofblockdiagonalizationintheFourierdomain,thejth
e
block diagonal matrix is obtained by applying the discrete Fourier transform along
the third mode, equivalently, by multiplying the discrete Fourier matrix F along
n3
the third mode of T. Substituting the TTD of T into this transformation yields
r1 r2 n3
T (j ,j )= G (j ,α )G (α ,j ,α ) G (α ,j)F (j,j ) .
j3 1 2 1 1 1 2 1 2 2 3 2 n3 3
!
α X1=1α X2=1
X
j=1
Define G =G F , and the desired result then follows immediately.
3 3
×
2 n3
Proposition 3.2 (HTD/TD-based block diagonalization). Let T Rn1×n2×n3
be a thi e rd-order tensor in the HTD/TD format with core tensor G Rr ∈ 1×r2×r3, and
factor matrices U
1
Rn1×r1, U
2
Rn2×r2, and U
3
Rn3×r3. T ∈ hen the diagonal
∈ ∈ ∈
block matrices of T in the Fourier domain are computed as
r1 r2 r3
(3.2) T (j ,j )= G(α ,α ,α )U (j ,α )U (j ,α )U (j ,α ),
j3 1 2 1 2 3 1 1 1 2 2 2 3 3 3
α X1=1α X2=1α X3=1
e
6

where U =F U , for j =1,2,...,n .
3 n3 3 3 3
Proof. TheprooffollowsimmediatelyfromtheobservationthatmultiplyingT by
e
F alongthe thirdmodeisequivalenttoreplacingthe factormatrixU withF U
n3 3 n3 3
in the HTD/TD of T.
Bothpropositionsprovideefficientproceduresforconstructingthediagonalblocks
when the TT- or hierarchical ranks are small relative to the tensor dimensions. The
computationscanbefurtheracceleratedbymatricizingintermediatecontractions. For
theTTD-basedapproach,reshapingthecoretensorsallowsthecontractionstobeper-
formed using matrix-vector and matrix-matrix multiplications rather than entrywise
tensor contractions. The same strategy applies to the HTD/TD-based approach.
Remark 3.3. Assume n =n =n =n and let r denote the maximum TT-rank
1 2 3
or hierarchical rank. The computational costs of TTD-based and HTD/TD-based
block diagonalization are estimated as (rnlogn+n(r2n+rn2)) and (rnlogn+
O O
n(r3+r2n+rn2)), respectively. In contrast, the definition-based approachfirst con-
structs the full tensor and then applies the fast Fourier transform along the third
mode, which costs (n3logn) and requires storing the entire tensor.
O
3.2. T-product. Using the block-diagonal representation, the T-product can
be computedbyperformingindependentmatrixmultiplicationsonthecorresponding
diagonal blocks in the Fourier domain, followed by the inverse Fourier transform to
recover the resulting tensor.
Corollary 3.4. Given two third-order tensors T Rn1×l×n3 and S Rl×n2×n3
∈ ∈
in the TTD format with core tensors G , G , G and H , H , H , respectively, their
1 2 3 1 2 3
T-product T⋆S Rn1×n2×n3 is computed as
∈
T⋆S=bcirc−1 −1(blkdiag T S ,T S ,...,T S ) ,
F
1 1 2 2 n3 n3
where T and S denote th (cid:16) e j th diagonal(cid:0)blocks of T and S in the F(cid:1)o (cid:17) urier domain,
j3 j3 3
respectively, computed from their TTD representations according to (3.1).
Proof. The proof follows immediately from the property of the T-product under
the Fourier domain and Proposition 3.1.
Similarly, for tensors represented in the HTD/TD format, the T-product can
be computed using the block-diagonal representation established in Proposition 3.2.
However, this approach does not fully exploit the underlying low-rank TTD or HT-
D/TDstructure,asit requiresthe explicitformationofintermediatediagonalblocks.
A more efficient formulation can be obtained by expressing the T-product directly in
terms of the TTD or HTD/TD factors of the input tensors, thereby preserving the
compressed structure throughout the computation.
Proposition 3.5 (TTD-based T-product). Given two third-order tensors T
Rn1×l×n3 and S Rl×n2×n3 in the TTD format with core tensors G
1
, G
2
, G
3
and H
1
∈ ,
∈
H , H , and TT-ranks 1,r ,r ,1 and 1,s ,s ,1 , respectively, their T-product
2 3 1 2 1 2
T⋆S Rn1×n2×n3 admits { a TTD re } presen { tation with } core tensors
∈
P (1,j ,φ(α ,β ))=G (1,j ,α ),
1 1 1 1 1 1 1
l
P (φ(α ,β ),j ,φ(α ,β ))= G (α ,j,α )H (1,j,β )H (β ,j ,β ),
2 1 1 2 2 2 2 1 2 1 1 2 1 2 2
j=1
X
P =P F−1 with P (φ(α ,β ),j ,1)=G (α ,j ,1)H (β ,j ,1),
3 3 × 2 n3 3 2 2 3 3 2 3 3 2 3
7
e e e e

where φ(α ,β )=α +(β 1)r for t=1,2, G =G F , and H =H F ,
t t t t
−
t 3 3
×
2 n3 3 3
×
2 n3
and with TT-ranks 1,r s ,r s ,1 .
1 1 2 2
{ }
e e
Proof. Denote by C = T ⋆S the T-product and by C its representation in the
Fourier domain. Since C(j ,j ,j ) = l T (j ,j)S (j,j ) for j = 1,2,...,n ,
1 2 3 j=1 j3 1 j3 2 3 3
substituting T (j ,j) and S (j,j ) with the correspondieng core representations ac-
j3 1 j3 2
P
cording to (3.1) yields e
l r1 r2 s1 s2
C(j ,j ,j )= G (1,j ,α )G (α ,j,α )G (α ,j ,1)
1 2 3 1 1 1 2 1 2 3 2 3
X
j=1α X1=1α X2=1β X1=1β X2=1
e H (1,j,β )H (β ,j ,β )H (β ,j ,1) e
1 1 2 1 2 2 3 2 3
×
Rearranging the terms according to the output indices, we obtain
e
r1 r2 s1 s2 l
C(j ,j ,j )= G (1,j ,α ) G (α ,j,α )H (1,j,β )
1 2 3 1 1 1 2 1 2 1 1
α X1=1α X2=1β X1=1β X2=1
X
j=1
e
H (β ,j ,β ) G (α ,j ,1)H (β ,j ,1).
2 1 2 2 3 2 3 3 2 3
× !
Introducing the combined indices eγ = φ(α ,βe) and γ = φ(α ,β ) and using the
1 1 1 2 2 2
definitions of P , P , and P , we obtain
1 2 3
r1s1 r2s2
e
C(j ,j ,j )= P (1,j ,γ )P (γ ,j ,γ )P (γ ,j ,1).
1 2 3 1 1 1 2 1 2 2 3 2 3
γ X1=1γ X2=1
e e
Applying the inverse Fourier transform to the third core P = P F−1 yields the
3 3 × 2 n3
TTD representation of C.
e
Proposition 3.6 (HTD/TD-based T-product). Given two third-order tensors
T Rn1×l×n3 and S Rl×n2×n3 in the HTD/TD format with core tensors G
Rr1 ∈ ×r2×r3 and H Rs1 ∈ ×s2×s3 and factor matrices U
t
andV
t
, t=1,2,3,respectively ∈ ,
theirT-productT⋆ ∈ S Rn1×n2×n3 admitsanHTD/TDrepresentationwithcoretensor
∈
P=P
× 3
F−
n3
1
∈
Rr1×s2×n3 where
r2 s1 r3 s3
e
P(α ,β ,γ )= G(α ,α ,α )M(α ,β )H(β ,β ,β )U (γ ,α )V (γ ,β ),
1 2 3 1 2 3 2 1 1 2 3 3 3 3 3 3 3
α X2=1β X1=1α X3=1β X3=1
e e e
with M=U⊤
2
V
1 ∈
Rr2×s1, U
3
=F
n3
U
3 ∈
Cn3×r3, and V
3
=F
n3
V
3 ∈
Cn3×s3, and
with factor matrices U , V , and I .
1 2 n3
e e
Proof. TheproofproceedssimilarlytothatfortheTTD-basedT-product. Denote
by C = T ⋆ S the T-product and by C its representation in the Fourier domain.
According to (3.2), it follows that
e
l r1 r2 r3 s1 s2 s3
C(j ,j ,j )= G(α ,α ,α )H(β ,β ,β )
1 2 3 1 2 3 1 2 3
X
j=1α X1=1α X2=1α X3=1β X1=1β X2=1β X3=1
e
U (j ,α )U (j,α )V (j,β )V (j ,β )U (j ,α )V (j ,β )
1 1 1 2 2 1 1 2 2 2 3 3 3 3 3 3
×
r1 s2
= P(α ,β ,j )U (j ,α )V (j ,βe ). e
1 2 3 1 1 1 2 2 2
α X1=1β X2=1
e
8

Finally, applying the inverse Fourier transform to the third mode of P yields the
HTD/TD representation of C.
e
Remark 3.7. Assumen =n =n =n,andletrandsdenotethemaximumTT-
1 2 3
ranks or hierarchicalranks of T and S. The computational complexities of the TTD-
basedand HTD/TD-basedT-productare about ((r+s+rs)nlogn+r2sl+r2s2n)
O
and ((r+s+rs)nlogn+rsl+(r3+s3+r2s+rs2)n), respectively. By comparison,
O
thestandardblock-circulantimplementationoftheT-productrequiresapproximately
(ln4) operations and the explicit storage of the full block-circulant matrix.
O
The TTD-based and HTD/TD-based formulations compute the T-product en-
tirely in compressed form, avoiding full tensors and their block-circulant representa-
tions and thereby reducing computational cost and memory requirements when the
decomposition ranks are small relative to the tensor dimensions.
3.3. T-SVD. SimilartoCorollary3.4forthe T-product,wecanleveragetensor
decomposition-based block diagonalization to compute T-SVD.
Corollary 3.8. Given a third-order tensor T Rn1×n2×n3 in the TTD format
with core tensors G , G , and G , let T = U S ∈ V∗ be the matrix SVDs of the
1 2 3 j3 j3 j3 j3
diagonal blocks T ,T ,...,T computed from the TTD representation according to
1 2 n3
(3.1). Then the T-SVD of T is obtained by assembling these matrix SVD factors and
applying the inverse Fourier transform.
Proof. The result follows directly from the definition of T-SVD and the block
diagonalization established in Proposition 3.1.
Analogously, T-SVD can also be computed using the block-diagonal represen-
tation associated with HTD/TD as presented in Proposition 3.2. Furthermore, the
factortensorsoftheT-SVDcanbeconstructeddirectlywithintheTTDorHTD/TD
formatsby operatingonthe correspondingcorerepresentations,thereby avoidingthe
explicit formation of the full dense tensors in either the original or transform do-
mains. For convenience, we permit the TTD and HTD/TD representations of the
factor tensors of T-SVD to be complex-valued, even though equivalent real-valued
representations can be readily obtained via suitable transformations.
Proposition 3.9 (TTD-basedT-SVD). Forathird-order tensorT Rn1×n2×n3
∈
in the TTD format with core tensors G , G , and G and TT-ranks 1,r ,r ,1 , let
1 2 3 1 2
{ }
G = Q R and G = Q R be the QR factorizations of the matricization G
Rn 1 1×r1 o 1 f G 1
1
and the 2 mode- 2 2 m 2 atricization G
2
Rn2×r1r2 of G
2
, respectively. Defi 1 n ∈ e
∈
M =R B with
β 1 β
r2
B (α ,η)= R (η,φ(α ,α ))G (α ,β,1),
β 1 2 1 2 3 2
α X2=1
e
where φ(α ,α )=α +(α 1)r and G =G F . Then the TTDs of the T-SVD
1 2 1 2
−
1 3 3
×
2 n3
factor tensors U, S, and V are computed as
e
U: P (1,j ,α)=Q (j ,α), P (α,ξ,β)=U (α,ξ), P (β,j ,1)=F−1(j ,β),
1 1 1 1 2 β 3 3 n3 3
S: Q (1,ξ,µ)=I (ξ,µ), Q (µ,ζ,β)=S (µ,ζ), Q (β,j ,1)=F−1(j ,β),
1 s 2 β 3 3 n3 3
V: R (1,j ,η)=Q (j ,η), R (η,ζ,β)=V (η,ζ), R (β,j ,1)=F−1(j ,β),
1 2 2 2 2 β 3 3 n3 3
where U , S , and V are derived from the compact matrix SVD of M , i.e.,
β β β β
M =U S V∗, and s=max rank(M ), for α=1,2,...,r , β =1,2,...,n ,
β β β β 1≤β≤n3 β 1 3
9

ξ,ζ,µ = 1,2,...,s, and η = 1,2,...,min n ,r r . If some M has rank smaller
2 1 2 β
{ }
than s, we extend its SVD factors to size s by adding extra columns and setting the
corresponding singular values to zero.
Proof. According to Proposition 3.1, the βth Fourier block diagonal matrix of T
canbewrittenasT (j ,j )= r1 r2 G (j ,α )G (α ,j ,α )G (α ,β,1).The
QRfactorizationof
β
G
1
giv
2
esG (α
α1
,
=
j
1
,α
α
)
2=
=
1 1
q
1
Q
1
(j
2
,η)R
1 2
(η,α
2
+
3
(α
2
1)r ).By
2 2P1 2P2 η=1 2 2 2 1 2 − 1
the definition of B , it follows that T = G B Q⊤. Applying the Q e R factorization
β β P1 β 2
G =Q R yields
1 1 1
T =Q (R B )Q⊤ =Q M Q⊤.
β 1 1 β 2 1 β 2
Taking the compact SVD of the reduced matrix M =U S V∗ yields
β β β β
T =(Q U )S (Q V )∗.
β 1 β β 2 β
Since Q , Q , U , and V have orthonormal columns, Q U and Q V also have
1 2 β β 1 β 2 β
orthonormal columns. Therefore, this yields a valid compact SVD of the Fourier
block diagonal matrix T . Stacking these factorizations over β = 1,2,...,n yields
β 3
the Fourier-domaintensors whose slices are (Q U ), S , and (Q V ). Applying the
1 β β 2 β
inverse Fourier transform along the third mode reconstructs the corresponding TT
core tensors. For example, for U, we obtain
n3
U(j ,ξ,j )= (Q U )(j ,ξ)F−1(j ,β).
1 3 1 β 1 n3 3
β=1
X
This is equivalently written in TTD form as
n3 r1
U(j ,ξ,j )= P (1,j ,α)P (α,ξ,β)P (β,j ,1),
1 3 1 1 2 3 3
β=1α=1
XX
with TT-ranks 1,r ,n ,1 . The constructions for S and V follow identically by
1 3
{ }
replacing Q U with S and Q V , respectively.
1 β β 2 β
Proposition 3.10 (HTD/TD-based T-SVD). Let T Rn1×n2×n3 be a third-
order tensor in the HTD/TD format with core tensor G
R∈
r1×r2×r3 and factor ma-
tricesU
t
Rnt×rt,t=1,2,3. AssumeU
1
andU
2
haveo ∈ rthonormalcolumns. Define
∈
U =F U and
3 n3 3
r3
e G = G(:,:,α )U (j ,α ) Cr1×r2
j3 3 3 3 3
∈
α X3=1
e
forj =1,2,...,n . SupposethatthecompactmatrixSVDsofG aregivenbyG =
3 3 j3 j3
P Q R∗ with s = max rank(G ). Then the HTD/TD representations of
j3 j3 j3 1≤j3≤n3 j3
the T-SVD factor tensors U, S, and V are computed as
U=P U I F−1, S=Q I I F−1,
× 1 1 × 2 s × 3 n3 × 1 s × 2 s × 3 n3
V=R U I F−1,
e × 1 2 × 2 s × 3 n3 e
where P(:,:,j
3
) = Pej3 , Q(:,:,j
3
) = Q
j3
, and R(:,:,j
3
) = R
j3
. If some G
j3
has rank
smaller than s, we extend its SVD factors to size s by adding extra columns and
settingethe correspondingesingular values to zeero.
10

Proof. According to Proposition3.2, the j th Fourier block diagonalmatrix of T
3
can be written as T =U G U⊤. Substituting the compact SVD of G yields
j3 1 j3 2 j3
T =U P Q R∗ U⊤ =(U P )Q (U R )∗.
j3 1 j3 j3 j3 2 1 j3 j3 2 j3
Since U and U have orthonormal columns, the factor matrices U P and U R
1 2 1 j3 2 j3
haveorthonormalcolumns. Therefore,thisdefinesavalidmatrixSVDofT . Bythe
j3
definition of the T-SVD, the Fourier-domain frontal slices of the factor tensors U, S,
andVarerespectivelygivenbyU P ,Q ,andU R forj =1,2,...,n . Stacking
1 j3 j3 2 j3 3 3
theseslicesyieldsthe Fourier-domaintensorsP U , Q,andR U . Applying the
1 1 1 2
× ×
inverseFouriertransformalongthe thirdmode givesthe HTD/TDrepresentationsof
the T-SVD factor tensors. e e e
The factor tensors/matrices in Proposition 3.9 and Proposition 3.10 may be
complex-valued,butequivalentreal-valuedrepresentationscanbeobtainedbygroup-
ing conjugate frequency pairs. The Fourier-domain frontal slices of T satisfy T ¯j3 =
T , where ¯j =1 for j =1 and ¯j =n j +2 otherwise. Thus, the left and right
sin
j3
gularfacto
3
rsat¯j ca
3
nbe chosen
3
as th
3
e − co
3
mplexconjugates ofthose atj with the
3 3
same singular values. In the inverse Fourier transform, each conjugate pair can be
transformed into real and imaginary linear combinations, yielding real-valued cores
without changing the T-SVD factor tensors or the stated ranks. The self-conjugate
frequencies j = 1 and, when n is even, j = n /2+1, are real-valued by the same
3 3 3 3
symmetryrelation. Therefore,theT-SVDfactortensorsadmitequivalentreal-valued
TTD or HTD/TD representations after grouping all conjugate frequency pairs.
Remark 3.11. Assume n = n = n = n, and let r denote the maximum TT-
1 2 3
rankorhierarchicalrank. FortheTTD-basedT-SVD,themaincomputationsconsist
of three parts, namely transforming the third core tensor, computing the QR factor-
ization of the reshaped first core tensor, and performing compact SVDs of M for
j3
j =1,2,...,n . The resulting cost is thus approximately (rnlogn+nr2+nr2q+
3 3
O
nmin r,q 2max r,q ), where q min r2,n . For the HTD/TD-based T-SVD, the
2
{ } { } ≤ { }
dominant computations consist of transforming U , constructing the reduced ma-
3
trices G , and performing compact SVDs of G for j = 1,2,...,n , yielding an
j3 j3 3 3
overallcomplexityof (rnlogn+nr3).Bycomparison,thecomputationalcostofthe
O
definition-based T-SVD is dominated by the Fourier transform of T and the matrix
SVDsoftheFourier-domainfrontalslices,whichcostapproximately (n3logn+n4).
O
In summary, the proposed TTD- and HTD/TD-based formulations compute the
T-SVDdirectlyfromthecorrespondingdecompositionfactorsandobtaintheresulting
factortensorsintheTTDorHTD/TDformat,withoutexplicitlyreconstructingeither
thefulltensororitsblock-diagonalrepresentation. WhentheTT-ranksorhierarchical
ranks are small relative to the tensor dimensions, the proposed formulations achieve
substantial computational savings over the definition-based T-SVD.
4. Generalization to higher-order tensors. Thissectiongeneralizesthepre-
ceding results to the higher-order setting. For a kth-order tensor T Rn1×n2×···×nk,
∈
the definition-basedhigher-orderblockdiagonalizationfirstappliesseparablediscrete
Fourier transforms along modes 3,4,...,k, i.e.,
T =T F F F .
×
3 n3
×
4 n4
×
5
···×
k nk
Foreachfrequencytuple j =(j ,j ,...,j ),wherej =1,2,...,n fort=3,4,...,k,
e 3 4 k t t
the corresponding Fourier-domain block is T
j
= T(:,:,j
3
,j
4
,...,j
k
) Cn1×n2. In-
∈
11
e

steadofexplicitlyconstructingthefulltensoranditsFouriertransform,thefollowing
propositionsderive higher-orderblock diagonalization,the higher-ordertensor-tensor
product, and higher-order SVD directly from the TTD and HTD representations by
operating on their core tensors, transfer tensors, or factor matrices.
Proposition 4.1 (TTD-based higher-order block diagonalization). Let T
Rn1×n2×n3×···×nk be a tensor in the TTD format with core tensors G
t
Rrt−1×nt×rt ∈ ,
t fre = qu 1 e , n 2 c , y .. t . u , p k le . j D = efin (j e 3 , G j t 4 , = ... G , t j k × ) 2 , F th n e t F ∈ ou C r r ie t− r 1 -d × o n m t× a r i t n fo d r iag t o = na 3 l , b 4 lo ,. c . k ∈ ., T k j . Fo C r n1 e × ac n h 2
∈
is then computed as e
r1 r2 rk k
T (j ,j )= G (1,j ,α )G (α ,j ,α ) G (α ,j ,α ).
j 1 2 1 1 1 2 1 2 2 t t−1 t t
···
α X1=1α X2=1 α Xk=1 t
Y
=3
e
Proof. TheprooffollowsthesameargumentasProposition3.1. Thehigher-order
block diagonalization applies the discrete Fourier transforms along modes 3,4,...,k.
Since mode-t multiplication acts only on the physical index of the tth core tensor,
the transformed tensor is represented by the original core tensors G ,G and the
1 2
transformed core tensors G for t = 3,4,...,k. Evaluating this TTD representation
t
at the frequency tuple j gives the stated expression for T .
j
Proposition 4.2 (HT e D-based higher-order block diagonalization). Let T
Rn1×n2×n3×···×nk be a tensor in the HTD format with respect to a dimension tre ∈ e
on D = 1,2,...,k with 1,2 . Let U
t
Rnt×rt denote the leaf factor matri-
T { } { }∈T ∈
ces and B the transfer tensor associated with each internal node τ . DefineU =
τ t
F
nt
U
t
∈
Cnt×rt for t = 3,4,...,k. For a fixed frequency tuple j ∈ = T (j
3
,j
4
,...,j
k
),
evaluate the transformed leaf factor U at the row U (j ,:), while leaving U andeU
t t t 1 2
unevaluated. Contracting all transfer tensors and the selected leaf rows over the di-
mension tree, with the indices associaeted with modese1 and 2 left open, gives a reduced
matrix G
j
Cr1×r2. Then the Fourier-domain diagonal block corresponding to each
∈
frequency tuple j is computed as
T =U G U⊤ Cn1×n2.
j 1 j 2 ∈
Proof. Theargumentisanalogoustothethird-orderHTDconstructioninPropo-
sition 3.2, but the remaining contractions are carried out along the dimension tree.
Applying the discrete Fourier transforms along modes 3,4,...,k is equivalent to re-
placing the leaf factor matrices U by U = F U , t = 3,4,...,k. For a fixed
t t nt t
frequency tuple j, selecting the rows U (j ,:) fixes all transformed modes. Contract-
t t
ing the remaining HTD network gives T e=U G U⊤.
j 1 j 2
e
Proposition 4.3 (TTD-based higher-order tensor-tensor product). Given two
tensors T Rn1×l×n3×···×nk and S Rl×n2×n3×···×nk in TTD format with core ten-
∈ ∈
sors G , H and TT-ranks 1,r ,...,r ,1 , 1,s ,...,s ,1 , respectively, define
t t 1 k−1 1 k−1
{ } { }
G = G F and H = H F for t = 3,4,...,k. Then the higher-order
t t
×
2 nt t t
×
2 nt
tensor-tensor product T⋆ S admits a TTD representation with core tensors
H
e e
P (1,j ,φ(α ,β ))=G (1,j ,α ),
1 1 1 1 1 1 1
l

P (φ(α ,β ),j ,φ(α ,β ))= G (α ,j,α )H (1,j,β )H (β ,j ,β ),
 2 1 1 2 2 2
X
j=1
2 1 2 1 1 2 1 2 2
P =P F−1 for t=3,4, ,k,
 t
e
t × 2 nt ···
12

where φ(α ,β )=α +(β 1)r , and for α =1,2,...,r and β =1,2,...,s ,
t t t t t t t t t
−
P φ(α ,β ),j ,φ(α ,β ) =G (α ,j ,α )H (β ,j ,β ),
t t−1 t−1 t t t t t−1 t t t t−1 t t
and with TT-(cid:0)ranks 1,r 1 s 1 ,r 2 s 2 ,...,r k−(cid:1)1 s k−1 ,1 .
e { e } e
Proof. The proof follows the same argument as Proposition 3.5. After applying
the discrete Fourier transform along modes 3,4,...,k, the higher-ordertensor-tensor
product reduces to matrix multiplication at each frequency tuple j. By Proposi-
tion 4.1, the Fourier-domain blocks of T and S are obtained from the core tensors
G ,G ,G and H ,H ,H , respectively. Multiplying these two blocks and contracting
1 2 t 1 2 t
over the shared index j =1,2,...,l gives the first two core tensors P and P , while
1 2
theremeainingfrequencey-modecoretensorsareobtainedbypairingthecorresponding
entries of G and H , t=3,4,...,k. Applying F−1 to these paired core tensors along
t t nt
their second indices gives the stated core tensors.
Propoesitione
4.4 (HTD-based higher-order tensor-tensor product). Given two
tensors T Rn1×l×n3×···×nk and S Rl×n2×n3×···×nk in the HTD format with respect
∈ ∈
tothe samedimension tree on D = 1,2,...,k with 1,2 , let U and G and
t τ
T { } { }∈T
V andH denotetheleaffactormatricesandtransfertensorsofT andS,respectively.
t τ
Define φ(a,b) = a+(b 1)p, where a = 1,2,...,p. Let W = U , W = V , and
1 1 2 2
−
define U =F U , V =F V , W (j ,φ(α ,β ))=U (j ,α )V (j ,β ), and W =
t nt t t nt t t t t t t t t t t t t
F−
nt
1W
t
for t=3,4,...,k. At the node
{
1,2
}
, let M=U⊤
2
V
1 ∈
Rr2×s1 and define
e e f e e
r2 s1
fP (α ,β ,φ(γ,δ))= G (α ,α ,γ)M(α ,β )H (β ,β ,δ).
{1,2} 1 2 {1,2} 1 2 2 1 {1,2} 1 2
α X2=1β X1=1
For any other internal node τ with children τ and τ , define
1 2
∈T
P φ(α ,β ),φ(α ,β ),φ(α ,β ) =G (α ,α ,α )H (β ,β ,β ).
τ τ1 τ1 τ2 τ2 τ τ τ τ1 τ2 τ τ τ1 τ2 τ
Then the(cid:0)higher-order tensor-tensor produ(cid:1)ct T ⋆
H
S admits an HTD representation
with leaf factors W and transfer tensors P , whose hierarchical ranks are bounded by
t τ
the products of the corresponding input ranks.
Proof. The argument is similar to the third-order HTD construction in Proposi-
tion 3.6. After applying the discrete Fourier transform along modes 3,4,...,k, the
tensor-tensor product reduces to matrix multiplication at each frequency tuple. The
transformed leaf factors U and V , t = 3,4,...,k, therefore give the paired out-
t t
put leaf factors W . The shared dimension of size l is contracted at the node 1,2
t
throughM=U⊤V ,whicehgivestehe statedtransfer tensorP . Allother int { erna } l
2 1 {1,2}
nodes are obtainfed by pairing the corresponding transfer tensors of the two input
HTD representations. Applying the inverse discrete Fourier transform to the paired
leaf factors along modes 3,4,...,k gives the stated HTD representation.
Proposition 4.5 (TTD-based higher-order SVD). Let T Rn1×n2×···×nk be a
tensor in the TTD format with core tensors G
t
Rrt−1×nt×rt, t ∈ =1,2,...,k. Define
∈
G = G F for t = 3,4,...,k, and let G = Q R and G = Q R be the QR
fa t ctoriz t a × tio 2 ns n o t f the matricization G
1
Rn1× 1 r1 of 1 G
1
1 and the 2 mode-2 2 m 2 atricization
Ge
2
Rn2×r1r2 of G
2
, respectively. Fo ∈ r each frequency tuple β = (β
3
,β
4
,...,β
k
),
∈
where β =1,2,...,n ,
t t
r2 r3 rk k
B (α ,η)= R (η,α +(α 1)r ) G (α ,β ,α ).
β 1 2 1 2 1 t t−1 t t
··· −
α X2=1α X3=1 α Xk=1 t
Y
=3
e
13

DefineM =R B , s=max rank(M ),andletM =U S (V )∗ bethecompact
β 1 β β β β β β β
SVDpadded with zerosingular values if necessary. Let ρ =φ(β ,ρ )=β +(ρ
t t t+1 t t+1
−
1)n denote the combined frequency index and set ρ = 1. Then the TTDs of the
t k+1
higher-order SVD factor tensors U, S, and V are computed as
U:P (1,j ,α)=Q (j ,α), P (α,ξ,ρ )=U (α,ξ), P (ρ ,j ,ρ )=F−1(j ,β ),
1 1 1 1 2 3 β t t t t+1 nt t t
S:Q (1,ξ,µ)=I (ξ,µ), Q (µ,ζ,ρ )=S (µ,ζ), Q (ρ ,j ,ρ )=F−1(j ,β ),
1 s 2 3 β t t t t+1 nt t t
V:R (1,j ,η)=Q (j ,η), R (η,ζ,ρ )=V (η,ζ), R (ρ ,j ,ρ )=F−1(j ,β ),
1 2 2 2 2 3 β t t t t+1 nt t t
for t=3,4,...,k, where η =1,2,...,min n ,r r and all unspecified entries of the
2 1 2
{ }
transform-mode core tensors equal to zero.
Proof. The proof follows the same argument as Proposition 3.9. For each fre-
quencytupleβ,Proposition4.1andtheQRfactorizationofthemode-2matricization
of G give T(:,:,β) = G B Q⊤. Using G = Q R , we have T(:,:,β) = Q M Q⊤.
2 1 β 2 1 1 1 1 β 2
Taking the SVD of M gives T(:,:,β) = (Q U )S (Q V )∗. Thus, the Fourier-
β 1 β β 2 β
domain higeher-order SVD factors are obtained from Q U , Se , and Q V for all
1 β β 2 β
frequency tuples. The stated TTecore tensors collect these factors over the combined
frequency indices ρ , while the core tensors P , Q , and R , t = 3,4,...,k, apply the
t t t t
inverseFouriertransformsalongmodes 3,4,...,k. Hence,they define TTD represen-
tations of the higher-order SVD factor tensors U, S, and V.
Proposition 4.6 (HTD-basedhigher-orderSVD). Let T Rn1×n2×n3×···×nk be
∈
a tensor in the HTD format with leaf factor matrices U and transfer tensors B
t τ
with respect to a dimension tree on D = 1,2,...,k , where U and U have
1 2
T { }
orthonormal columns. Assumethat 1,2 and that themodes 3,4,...,k form the
{ }∈T
complementary subtree. For t = 3,4,...,k, define U = F U . For each frequency
t nt t
tuple j, let G
j
Cr1×r2 be obtained by contracting the transformed HTD network
∈
with the rows U (j ,:), while leaving the rank indicees associated with modes 1 and 2
t t
open. Set s=max rank(G ) and let G =U S (V )∗ be the compact SVD, padded
j j j j j j
with zero singuelar values if necessary. Let U, S, and V be the HTD trees whose
T T T
root D has children 1,2 and f = 3,4,...,k , and which share the same subtree
f
{ } { } T
on f. The leaf factors of U, S, and V are computed as
L U =U , L U =I , L U =F−1,
L { S 1} =I 1 , L { S 2} =I s , L { S t} =F n − t 1, t=3,4,...,k.
L { V 1} =U s , L { V 2} =I s , L { V t} =F n − t 1,
{1} 2 {2} s {t} nt
Let φ(a,b)=a+(b 1)p, a=1,2,...,p. The transfer tensors at the node 1,2 are
− { }
BU
(α ,ξ,φ(α ,ξ))=1,
BS
(ξ,ζ,φ(ξ,ζ)) =1,
BV
(α ,ζ,φ(α ,ζ))=1,
{1,2} 1 1 {1,2} {1,2} 2 2
For each leaf node t f, let ρ =j . For each internal node τ f with children
{t} t
{ }⊆ ⊆
τ and τ , define ρ =φ(ρ ,ρ )=ρ +( n )(ρ 1). Therefore, the transfer
1 2 τ τ1 τ2 τ1 ℓ∈τ1 ℓ τ2−
tensors at τ satisfy BX(ρ ,ρ ,ρ ) = 1, where X U,S,V . Finally, the root
τ τ1 τ2 τ Q ∈ { }
transfer tensors are computed as
BU
(φ(α ,ξ),ρ ,1)=U (α ,ξ),
BS
(φ(ξ,ζ),ρ ,1)=S (ξ,ζ),
D 1 f j 1 D f j
BV (φ(α ,ζ),ρ ,1)=V (α ,ζ).
D 2 f j 2
These factor matrices and transfer tensors define HTD representations of the higher-
order SVD factor tensors U, S, and V, with all unspecified entries of the transfer
tensors equal to zero.
14

Proof. The argument is similar to the third-order HTD construction in Proposi-
tion 3.10. For each j, Proposition 4.2 gives T(:,:,j) = U G U⊤. Substituting the
1 j 2
compact SVD of G yields T(:,:,j)=(U U )S (U V )∗. Thus, the Fourier-domain
|     |     |     | j   |     |     | 1 j | j 2 | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
higher-order SVD factors are U U , S , andeU V . The proposed HTD leaf factors
|     |     |     |     |     | 1 j | j   | 2 j |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and transfer tensors reproduece these factors at each frequency tuple: the node 1,2
{ }
pairs the rank and singular-vectorindices, the subtree combines the frequency in-
T f
dicesj ,j ,...,j andappliesthe inversediscreteFouriertransformsthroughtheleaf
|     | 3 4 | k   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F−1,
factors and the root transfer tensor stores U , S , or V . Since the transform-
|     | nt  |     |     |     |     |     | j   | j   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F−1,
mode leaf factors are nt t = 3,4,...,k, the HTD contraction applies the inverse
discrete Fourier transforms along all transform modes. Therefore, the constructed
| HTD | representations |     | give | U, S, | and V | satisfying | T =U⋆ | S⋆  | V⊤. |     |
| --- | --------------- | --- | ---- | ----- | ----- | ---------- | ----- | --- | --- | --- |
|     |                 |     |      |       |       |            |       | H   | H   |     |
Remark 4.7. Assume n 1 =n 2 = =n k =n. Let r and s denote the maximum
···
TT-ranks or hierarchical ranks. For the TTD-based framework, the computational
complexities are ((k 2)r2nlogn+nk−2((k 2)r2 +nr2 +rn2)) for higher-order
|     |     | O   | −   | (r2sl+r2s2n+(k |     |     | 2)n((r2 − | +s2)logn+r2s2(1+logn))) |     |     |
| --- | --- | --- | --- | -------------- | --- | --- | --------- | ----------------------- | --- | --- |
block diagonalization,
|     |     |     | O   |     |     | −   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for the higher-order tensor-tensor product, and ((k 2)r2nlogn+nr2 +nr2q +
| nk−2((k | 2)r2+r2q+min |     |     |     | 2max |        | O     | −     | r2,n               |     |
| ------- | ------------ | --- | --- | --- | ---- | ------ | ----- | ----- | ------------------ | --- |
|         |              |     |     | r,q |      | r,q )) | where | q min | 2 for higher-order |     |
|         | −            |     |     | {   | }    | { }    |       | ≤     | { }                |     |
SVD. For the HTD-based framework, the corresponding computational complexities
are ((k 2)nrlogn+nk−2(kr3+r2n+rn2)) forhigher-orderblockdiagonalization,
O 2)n(r+s+rs)logn+lrs+kr3s3) −
| ((k |     |     |     |     |     |     | for the | higher-order | tensor-tensor | prod- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ------------- | ----- |
O −
uct, and ((k 2)nrlogn+nk−2(kr3+r3)) for higher-order SVD. In contrast, the
|     | O   | −   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
definition-basedapproachexplicitlyformsthefulltensorsandperformscomputations
on all nk−2 block-diagonalmatrices in the transformdomain. Consequently, its com-
putational complexities are (nk(k 2)logn) for higher-orderblock diagonalization,
| (nk−2((2ln+n2)(k |                |     | 2)logn+ln2))forthehigher-ordertensor-tensorproduct,and | O   | −            |     |      |     |     |     |
| ---------------- | -------------- | --- | ------------------------------------------------------ | --- | ------------ | --- | ---- | --- | --- | --- |
| O                |                |     | −                                                      |     |              |     |      |     |     |     |
| (nk(k            | 2)logn+nk−2n3) |     |                                                        | for | higher-order |     | SVD. |     |     |     |
O −
Byformulatinghigher-orderblockdiagonalization,thetensor-tensorproduct,and
higher-order SVD directly in terms of the TTD and HTD factors, the proposed al-
gorithms avoid constructing full tensors and their transform-domain representations
while preservingthe underlyinglow-rankdecompositionstructure. This reducesstor-
age requirements and computational cost when the decomposition ranks are small
relative to the tensor dimensions, providing an efficient framework for higher-order
| transform-based |     | multilinear |     | algebra. |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
5. Numerical Examples. We evaluatedthe proposedframeworkthroughase-
riesofnumericalexperiments. Allcomputationswereperformedonauniversityhigh-
performancecomputingcluster,witheachexperimentallocated200GBofmemoryon
a compute node. The source code for the experiments is available at https://github.
| com/usernamemydusername/decomp |     |     |     |     |     | based tensoralg. |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
5.1. Third-order T-product. We evaluated the computational efficiency of
the proposedTTD-andHTD-basedT-productusingrandomlygeneratedthird-order
tensors T Rn1×l×n3 and S Rl×n2×n3 under three data generation strategies: (a)
|     | ∈   |     |     | ∈   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
randomsparse tensors,(b) tensors with low TT-ranks,and (c) tensors with low hier-
archicalranks. We excluded the computationaltime for constructing TTD andHTD
formats. Throughoutthe experiments, we fixed n =6 and varied n , n , and l from
|     |     |     |     |     |     |     | 3   |     | 1 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
23to213.
Forthelow-rankcases,thecorrespondingTTDorHTDfactorsareprovided
asinputs. We comparedthefollowingthreeimplementations: (i)the definition-based
T-product;(ii)theproposedTTD-basedT-productaccordingtoProposition3.5;and
(iii)theproposedHTD-basedT-productframeworkaccordingtoProposition3.6. For
15

|     | Random Sparse |     |     | Low TT-Ranks |     |     | Low Hierarchical Ranks |     |     |
| --- | ------------- | --- | --- | ------------ | --- | --- | ---------------------- | --- | --- |
104
|     | Definition-based |     |     | Definition-based |     |     | Definition-based |     |     |
| --- | ---------------- | --- | --- | ---------------- | --- | --- | ---------------- | --- | --- |
|     | HTD-based        |     |     | HTD-based        |     |     | HTD-based        |     |     |
102
|     | TTD-based |     |     | TTD-based |     |     | TTD-based |     |     |
| --- | --------- | --- | --- | --------- | --- | --- | --------- | --- | --- |
)s( emiT
100
10-2
10-4
| 23  | 25 27       | 29  | 211 213 23 | 25 27       | 29  | 211 213 | 23 25 | 27 29 211   | 213 |
| --- | ----------- | --- | ---------- | ----------- | --- | ------- | ----- | ----------- | --- |
|     | Dimension n |     |            | Dimension n |     |         |       | Dimension n |     |
Fig. 1. Log-log plots of the average runtime for the definition-based, TTD-based, and HTD-
basedT-productunderthreedatagenerationstrategies: randomsparsetensors,randomtensorswith
| low TT-rank, | and | random | tensors with | low hierarchical | rank. |     |     |     |     |
| ------------ | --- | ------ | ------------ | ---------------- | ----- | --- | --- | --- | --- |
each problem size, the experiment was repeated five times, and the average runtime
was recorded. The results in Figure 1 show that the proposed TTD- and HTD-based
methodsconsistentlyoutperformthe definition-basedimplementationacrossallthree
data generationstrategies. The performanceadvantagebecomesmore pronouncedas
thetensordimensionsincrease,especiallyfortensorswithlowTT-rankorhierarchical
rank,wherecomputationsareperformeddirectlyoncompressedrepresentations. The
HTD-based method is generally faster than the TTD-based method across all three
data generation strategies because it first contracts the shared physical mode in the
reducedrepresentation,whereastheTTD-basedconstructionmultipliestheTT-ranks
| in the | corresponding | output | core. |     |     |     |     |     |     |
| ------ | ------------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
5.2. Fourth-orderSVD. Weevaluatedthecomputationalefficiencyofthepro-
posed TTD- and HTD-based frameworks for computing the fourth-order SVD. We
considered fourth-order tensors T Rn1×n2×n3×n4 generated using the same three
∈
data generation strategies as in the previous experiment. The spatial dimensions
were varied as n = n = 2p, p = 3,4,...,13, while the transform-mode dimensions
|     |     | 1 2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
were fixed at n = n = 4. We compared three implementations: (i) the definition-
|     |     | 3 4 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
based higher-order SVD; (ii) the proposed TTD-based higher-order SVD according
to Proposition4.5; and (iii) the proposedHTD-based higher-orderSVD accordingto
Proposition 4.6. For each problem size, the experiment was repeated five times, and
the average runtime was recorded. As shown in Figure 2, both the proposed TTD-
and HTD-based methods consistently outperform the definition-based implementa-
tion across all three data generationstrategies. The performance advantage becomes
morepronouncedasthetensordimensionsincrease,particularlywhenthetensorsad-
mit low TT-rank or HTD representations. Moreover, in additional tests beyond the
rangeshowninFigure2,wefoundthatthedefinition-basedmethodfailedtocomplete
the test cases for p 15 due to its substantially higher memory and computational
≥
requirements, whereas the proposed methods remained computationally feasible.
| 5.3. | T-eigensystem |     | realization | algorithm. |     |     |          |           |         |
| ---- | ------------- | --- | ----------- | ---------- | --- | --- | -------- | --------- | ------- |
|      |               |     |             |            |     | The | proposed | framework | is par- |
ticularly beneficial for large-scale applications in which the T-SVD constitutes the
dominant computational kernel. As an example, we considered the tensor eigensys-
tem realization algorithm (T-ERA) [37], which identifies reduced-order multilinear
systemsfrommeasureddatausingtheT-productandT-SVD.T-ERAgeneralizesthe
classicaleigensystemrealizationalgorithm(ERA)[23]tomultilinearsystemsthrough
transform-basedtensoralgebra. SincethecomputationalcostofT-ERAisdominated
16

|     | Random Sparse |     |     | Low TT-Ranks |     |     | Low Hierarchical Ranks |     |
| --- | ------------- | --- | --- | ------------ | --- | --- | ---------------------- | --- |
104
|     | Definition-based |     |     | Definition-based |     |     | Definition-based |     |
| --- | ---------------- | --- | --- | ---------------- | --- | --- | ---------------- | --- |
|     | HTD-based        |     |     | HTD-based        |     |     | HTD-based        |     |
102
|     | TTD-based |     |     | TTD-based |     |     | TTD-based |     |
| --- | --------- | --- | --- | --------- | --- | --- | --------- | --- |
)s( emiT
100
10-2
10-4
| 23  | 25          | 27 29 211 | 213 23 | 25 27       | 29  | 211 213 | 23 25 27    | 29 211 213 |
| --- | ----------- | --------- | ------ | ----------- | --- | ------- | ----------- | ---------- |
|     | Dimension n |           |        | Dimension n |     |         | Dimension n |            |
Fig. 2. Log-log plots of the average runtime for the definition-based, TTD-based, and HTD-
based higher-order SVD methods under three data generation strategies: random sparse tensors,
| random | tensorswith   | low TT-rank, | and | random       | tensorswith | low hierarchical |                        | rank. |
| ------ | ------------- | ------------ | --- | ------------ | ----------- | ---------------- | ---------------------- | ----- |
|        | Random Sparse |              |     | Low TT-Ranks |             |                  | Low Hierarchical Ranks |       |
104
103
)s( emiT
102
101
100
|     | TERA | TTD HTD |     | TERA | TTD HTD |     | TERA | TTD HTD |
| --- | ---- | ------- | --- | ---- | ------- | --- | ---- | ------- |
Fig.3. Logplotsoftheaverageruntimeofthebaseline,TTD-based,andHTD-basedT-ERAfor
generalized Hankeltensors with random sparse, low TT-rank, and low hierarchical rank structures.
by the T-SVD of a large generalized Hankel tensor, it provides a natural benchmark
| for evaluating |     | the proposed | framework. |     |     |     |     |     |
| -------------- | --- | ------------ | ---------- | --- | --- | --- | --- | --- |
We replacedthe definition-basedT-SVD in T-ERAwith the proposedTTD- and
HTD-based formulations and compared their computational performance. Specifi-
cally, we benchmarked T-ERA using synthetic generalized Hankel tensors with one
of three prescribed structures: (a) random sparse, (b) low TT-rank, or (c) low hi-
erarchical rank, following the framework in [37], and the Hankel dimensions satisfy
ℓ(L+1)=m(T+1)=H,wherewefixedH =10,000. Wecomparedthreeimplemen-
tations of T-ERA that differ only in the computation of the Hankel T-SVD: (i) the
baseline T-ERA using the definition-based T-SVD; (ii) T-ERA with the TTD-based
T-SVD; and (iii) T-ERA with the HTD-based T-SVD. For each configuration, the
experiment was repeated ten times, and the average runtime for reduced model con-
struction was recorded. As shown in Figure 3, replacing the definition-based Hankel
T-SVD with the proposed TTD- or HTD-based formulations substantially reduces
theoverallruntimeofT-ERAacrossallthreedatagenerationstrategies. Therelative
errors between the reduced systems generated by the TTD-/HTD-based meth-
∞
| H   |     |     |     |     |     | 10−14 |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- |
ods and the definition-based method remain below 2 for all three test cases
×
(see Table 1). These results confirm that the proposed T-SVD methods effectively
| alleviate | the dominant | computational |     | bottleneck |     | in large-scale | T-ERA. |     |
| --------- | ------------ | ------------- | --- | ---------- | --- | -------------- | ------ | --- |
6. Conclusion.
|     |     | In  | this article, | we  | developed | decomposition-based |     | computa- |
| --- | --- | --- | ------------- | --- | --------- | ------------------- | --- | -------- |
tionalframeworksfortransform-basedmultilinearalgebrausingTTDandHTD.They
17

|     |     |     |     |     | Table 1 |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- |
Relative H errors ofthe reduced systemsobtainedbythe TTD-and HTD-basedT-ERAwith
∞
| respect | to the definition-based |                      | T-ERA | model | for the three testcases. |           |       |     |
| ------- | ----------------------- | -------------------- | ----- | ----- | ------------------------ | --------- | ----- | --- |
|         |                         | Case                 |       |       | TTD-based                | HTD-based |       |     |
|         |                         | Randomsparse         |       |       | 5.77 10−15               | 5.97      | 10−15 |     |
|         |                         |                      |       |       | × 10−15                  | ×         | 10−15 |     |
|         |                         | LowTT-ranks          |       |       | 9.05                     | 9.16      |       |     |
|         |                         |                      |       |       | ×                        | ×         |       |     |
|         |                         | Lowhierarchicalranks |       |       | 1.67 10−14               | 1.58      | 10−14 |     |
|         |                         |                      |       |       | ×                        | ×         |       |     |
formulate block diagonalization, the T-product, and T-SVD directly in compressed
representations, so that the computations are performed on TTD core tensors or
HTD factorswithout full-tensorreconstruction. We further extendedthe frameworks
to higher-order tensors and demonstrated their effectiveness numerically, including
in multilinear system model reduction. The results show that the proposed TTD-
based and HTD-based methods can substantially reduce computational cost while
preserving the operator-based structure of transform tensor algebra, especially when
| the | tensors have | low TT- | or hierarchicalranks. |     |     |     |     |     |
| --- | ------------ | ------- | --------------------- | --- | --- | --- | --- | --- |
Severaldirectionsmeritfurtherinvestigation. Theproposeddecomposition-based
framework can be extended to other transform-basedtensor operations,including T-
QR, tensor inverse computations, and additional tensor factorizations. It would also
be valuable to move beyond the discrete Fourier transform by incorporating more
general invertible transforms together with a broader class of tensor decompositions,
enabling the computational representation to better adapt to the underlying data
and operators. This includes the development of transform-dependent compressed
formulations as well as practical strategies for selecting appropriate decomposition
formats for different applications. More broadly, the proposed framework can be
integrated into computational pipelines in which transform-based tensor operations
arise repeatedly as fundamental computational kernels, including multilinear system
identificationandmodel reduction,multidimensional imagingandvideo analysis,hy-
perspectraldata processing,parametricpartialdifferentialequations anduncertainty
quantification, and scientific machine learning. We expect that these directions will
further expand the scope of scalable transform-based multilinear algebra and its ap-
| plications | to large-scaletensor |     |     | computation. |     |     |     |     |
| ---------- | -------------------- | --- | --- | ------------ | --- | --- | --- | --- |
REFERENCES
[1] S. Ahmadi-Asl, M. G. Asante-Mensah, A. Cichocki, A. H. Phan, I. Oseledets, and
|     | J. Wang,           | Fast | cross tensor | approximation | for image | and video | completion, | Signal Pro- |
| --- | ------------------ | ---- | ------------ | ------------- | --------- | --------- | ----------- | ----------- |
|     | cessing,213(2023), |      | p.109121.    |               |           |           |             |             |
[2] K. S. F. Azam, O. Ryabchykov,and T. Bocklitz, A review on data fusion of multidimen-
|     | sional medical | and | biomedical | data,Molecules,27(2022), |     | p.7448. |     |     |
| --- | -------------- | --- | ---------- | ------------------------ | --- | ------- | --- | --- |
[3] M.Bachmayr,A.Cohen,andW.Dahmen,Parametricpdes: sparse orlow-rank approxima-
|     | tions?,IMAJournalofNumericalAnalysis,38(2018), |     |     |     |     | pp.1661–1708. |     |     |
| --- | ---------------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- |
[4] B. W. Bader and T. G. Kolda, Efficient matlab computations with sparse and factored
|     | tensors,SIAMJournalonScientificComputing, |     |     |     | 30(2008), | pp.205–231. |     |     |
| --- | ----------------------------------------- | --- | --- | --- | --------- | ----------- | --- | --- |
[5] J.A.Bengua,H.N.Phien,H.D.Tuan,andM.N.Do,Efficienttensorcompletionforcolor
|     | imageandvideorecovery: |               |     | Low-ranktensortrain,IEEETransactionsonImageProcessing, |     |     |     |     |
| --- | ---------------------- | ------------- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
|     | 26(2017),              | pp.2466–2479. |     |                                                        |     |     |     |     |
[6] G.BergqvistandE.G.Larsson,Thehigher-ordersingularvaluedecomposition: Theoryand
|     | an application | [lecture | notes], | IEEE | Signal ProcessingMagazine, |     | 27 (2010), | pp. 151–154, |
| --- | -------------- | -------- | ------- | ---- | -------------------------- | --- | ---------- | ------------ |
https://doi.org/10.1109/MSP.2010.936030.
[7] K. Braman, Third-order tensors as linear operators on a space of matrices, Linear Algebra
|     | anditsApplications,433(2010), |     |     | pp.1241–1253. |     |     |     |     |
| --- | ----------------------------- | --- | --- | ------------- | --- | --- | --- | --- |
18

[8] Z.CaoandP.Xie,Onsometensorinequalitiesbasedonthet-product,LinearandMultilinear
| Algebra,71(2023), | pp.377–390. |     |     |     |     |     |     |     |
| ----------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
[9] Y.Chang,L.Yan,X.-L.Zhao,H.Fang,Z.Zhang,andS.Zhong,Weightedlow-ranktensor
| recovery | forhyperspectral | image | restoration,IEEEtransactionsoncybernetics,50(2020), |     |     |     |     |     |
| -------- | ---------------- | ----- | --------------------------------------------------- | --- | --- | --- | --- | --- |
pp.4558–4572.
C.Chen,Explicitsolutionsandstabilitypropertiesofhomogeneous
| [10]                  |     |                              |     |     |     | polynomialdynamicalsys- |     |     |
| --------------------- | --- | ---------------------------- | --- | --- | --- | ----------------------- | --- | --- |
| tems,IEEETransactions |     | onAutomaticControl,68(2022), |     |     |     | pp.4962–4969.           |     |     |
[11] C. Chen,Tensor-Based Dynamical Systems,Synthesis Lectures onMathematics &Statistics,
Springer,Cham,2024,https://doi.org/10.1007/978-3-031-54505-4.
[12] C.Chen,A.Surana,A.M.Bloch,andI.Rajapakse,Controllability of hypergraphs, IEEE
| Transactions | onNetworkScienceandEngineering,8(2021), |     |     |     |     | pp.1646–1657. |     |     |
| ------------ | --------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- |
[13] C. Chen, A. Surana, A. M. Bloch, and I. Rajapakse, Multilinear control systems theory,
| SIAMJournalonControlandOptimization,59(2021), |     |     |     |     |     | pp.749–776. |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
[14] L. De Lathauwer, B. De Moor, and J. Vandewalle, A multilinear singular value decom-
| position, | SIAMjournalonMatrixAnalysisandApplications,21(2000), |     |     |     |     |     | pp.1253–1278. |     |
| --------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- |
[15] J. Ding, H. Choi, Y. Wei, and P. Xie, The tensor phase under a tensor–tensor product,
| Computational | andAppliedMathematics, |     |     | 44(2025), | p.121. |     |     |     |
| ------------- | ---------------------- | --- | --- | --------- | ------ | --- | --- | --- |
[16] L.Grasedyck,Hierarchicalsingularvaluedecompositionoftensors,SIAMJournalonMatrix
| AnalysisandApplications,31(2010), |     |     |     | pp.2029–2054, | https://doi.org/10.1137/090764189. |     |     |     |
| --------------------------------- | --- | --- | --- | ------------- | ---------------------------------- | --- | --- | --- |
[17] N.Hao,M.E.Kilmer,K.Braman,andR.C.Hoover,Facialrecognitionusingtensor-tensor
| decompositions, | SIAMJournalonImagingSciences, |     |     |     | 6(2013), | pp.437–463. |     |     |
| --------------- | ----------------------------- | --- | --- | --- | -------- | ----------- | --- | --- |
[18] H.He,C.Ling,andW.Xie,Tensorcompletionviaageneralizedtransformedtensort-product
| decomposition | without | t-svd,JournalofScientificComputing,93(2022), |     |     |     |     | p.47. |     |
| ------------- | ------- | -------------------------------------------- | --- | --- | --- | --- | ----- | --- |
[19] Z. He, M. Hu, Y. Lou, and C. Chen, Tensor dynamic mode decomposition, IEEE Signal
| ProcessingLetters,33(2026), |     |     | pp.1225–1229, | https://doi.org/10.1109/LSP.2026.3673197. |     |     |     |     |
| --------------------------- | --- | --- | ------------- | ----------------------------------------- | --- | --- | --- | --- |
[20] Z. He, Y. Mei, S. Mei, X. Mao, A. Dong, R. Wang, and C. Chen, Data-driven control of
| t-product-based | dynamical | systems, |     | IEEE Transactions |     | on Automatic | Control, | 71 (2026), |
| --------------- | --------- | -------- | --- | ----------------- | --- | ------------ | -------- | ---------- |
pp.5486–5493.
[21] R.C.Hoover,K.S.Braman,andN.Hao,Poseestimationfromasingleimageusingtensor
| decomposition | and an | algebra | of circulants, | in  | 2011 IEEE/RSJ | International |     | Conference |
| ------------- | ------ | ------- | -------------- | --- | ------------- | ------------- | --- | ---------- |
onIntelligentRobotsandSystems,IEEE,2011,pp.2928–2934.
[22] R.C.Hoover,K.Caudle,andK.Braman,Anewapproachtomultilineardynamicalsystems
| and control, | arXivpreprintarXiv:2108.13583, |     |     | (2021). |     |     |     |     |
| ------------ | ------------------------------ | --- | --- | ------- | --- | --- | --- | --- |
J.JuangandR.Pappa,Aneigensystemrealizationalgorithmformodal
| [23]     |                                                              |     |     |     |     |     | parameteridentifica- |         |
| -------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | -------------------- | ------- |
| tion and | model reduction,JournalofGuidanceControlandDynamics,8(1985), |     |     |     |     |     |                      | pp.620– |
627,https://doi.org/10.2514/3.20031.
[24] E.Kernfeld,M.Kilmer,andS.Aeron,Tensor–tensorproductswithinvertiblelineartrans-
| forms,LinearAlgebraanditsApplications,485(2015), |     |     |     |     |     | pp.545–570. |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ----------- | --- | --- |
[25] M.E.Kilmer,K.Braman,N.Hao,andR.C.Hoover,Third-ordertensorsasoperatorson
| matrices:                                        | Atheoreticalandcomputational |     |     | framework | withapplications |             | inimaging,SIAM |     |
| ------------------------------------------------ | ---------------------------- | --- | --- | --------- | ---------------- | ----------- | -------------- | --- |
| JournalonMatrixAnalysisandApplications,34(2013), |                              |     |     |           |                  | pp.148–172. |                |     |
[26] M. E. Kilmer and C. D. Martin, Factorization strategies for third-order tensors, Linear
| AlgebraanditsApplications,435(2011), |     |     |     | pp.641–658. |     |     |     |     |
| ------------------------------------ | --- | --- | --- | ----------- | --- | --- | --- | --- |
[27] T. G. Kolda and B. W. Bader, Tensor decompositions and applications, SIAM review, 51
| (2009), pp.455–500. |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[28] C. Lu, J. Feng, Y. Chen, W. Liu, Z. Lin, and S. Yan, Tensor robust principal compo-
nentanalysiswithanewtensornuclearnorm,IEEEtransactionsonpatternanalysisand
| machineintelligence,42(2019), |     |     | pp.925–938. |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- |
[29] C.Lubich,T.Rohwedder,R.Schneider,andB.Vandereycken,Dynamicalapproximation
| by hierarchical        | tucker | and tensor-train |     | tensors,                           | SIAM | Journal | on Matrix | Analysis and |
| ---------------------- | ------ | ---------------- | --- | ---------------------------------- | ---- | ------- | --------- | ------------ |
| Applications,34(2013), |        | pp.470–494,      |     | https://doi.org/10.1137/120885723. |      |         |           |              |
[30] K. Lund, The tensor t-function: A definition for functions of third-order tensors, Numerical
| LinearAlgebrawithApplications,27(2020), |     |     |     | p.e2288. |     |     |     |     |
| --------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- |
[31] A. Ma and D. Molitor, Randomized kaczmarz for tensor linear systems, BIT Numerical
| Mathematics, | 62(2022), | pp.171–194, |     | https://doi.org/10.1007/s10543-021-00877-w. |     |     |     |     |
| ------------ | --------- | ----------- | --- | ------------------------------------------- | --- | --- | --- | --- |
[32] W. Ma, C. Liu, and Y. Wei, Multilinear time-invariant descriptor systems, Computational
| andAppliedMathematics, |     | 44(2025), |     | p.277. |     |     |     |     |
| ---------------------- | --- | --------- | --- | ------ | --- | --- | --- | --- |
[33] W. Ma, C. Liu, and Y. Wei, Online tensor-based dynamic mode decomposition for time-
| varying system,JournalofScientificComputing,108(2026), |     |     |     |     |     | p.3. |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | ---- | --- | --- |
[34] X.Mao,A.Dong,Z.He,Y.Mei,S.Mei,andC.Chen,Tensor-basedhomogeneous polyno-
| mial dynamical | systemanalysis |         | from | data,arXivpreprintarXiv:2503.17774,(2025). |     |          |             |          |
| -------------- | -------------- | ------- | ---- | ------------------------------------------ | --- | -------- | ----------- | -------- |
| X. Mao, A.     | Dong, Z. He,   | Y. Mei, | S.   | Mei, R. Wang,                              | and | C. Chen, |             |          |
| [35]           |                |         |      |                                            |     |          | Data-driven | analysis |
19

of t-product-based dynamical systems,IEEEControl SystemsLetters, 8(2025), pp.3356–
3361.
[36] C. D. Martin,R. Shafer,andB. LaRue,An order-p tensor factorization with applications
in imaging,SIAMJournalonScientificComputing,35(2013), pp.A474–A490.
[37] S.Mei,Z.He,Y.Mei,X.Mao,A.Dong,R.Wang,andC.Chen,Data-drivenmodel order
reduction via t-svd,Automatica, 186(2026), p.112862.
[38] Y.Mei,S.Mei,Z.He,X.Mao,A.Dong,andC.Chen,Controllability and observability of
t-product-based time-varying systems, in 2025 Proceedings of the Conference on Control
anditsApplications(CT),SIAM,2025, pp.62–67.
[39] Y. Miao, L. Qi, and Y. Wei, T-jordan canonical form and t-drazin inverse based on the
t-product,CommunicationsonAppliedMathematicsandComputation,3(2021),pp.201–
220.
[40] I. V. Oseledets, Tensor-train decomposition, SIAM Journal on Scientific Computing, 33
(2011), pp.2295–2317, https://doi.org/10.1137/090752286.
[41] I. V. Oseledets and E. E. Tyrtyshnikov, Breaking the Curse of Dimensionality, Or How
to Use SVD in Many Dimensions, SIAM Journal on Scientific Computing, 31 (2009),
pp.3744–3759.
[42] C.Ozdemir,R.C.Hoover,K.Caudle,andK.Braman,High-ordermultilineardiscriminant
analysis via order-n tensor eigendecomposition, arXivpreprintarXiv:2205.09191, (2022).
[43] K. Pena-Pena, D. L. Lau, and G. R. Arce, T-hgsp: Hypergraph signal processing using t-
product tensor decompositions, IEEE Transactions on Signal and Information Processing
overNetworks,9(2023), pp.329–345.
[44] M. Rogers, L. Li, and S. J. Russell, Multilinear dynamical systems for tensor time series,
Advances inNeuralInformationProcessingSystems,26(2013).
[45] A. K. Saibaba, M. E. Kilmer, K. Hall-Hooper, F. Tian, and A. Mize, A tensor-based
dynamic mode decomposition based on the m-product, arXiv preprint arXiv:2508.10126,
(2025).
[46] F.Sedighin,Tensormethods inbiomedical image analysis,JournalofMedicalSignals&Sen-
sors,14(2024), p.16.
[47] Y.Shen,B.Baingana,andG.B.Giannakis,Tensordecompositions foridentifyingdirected
graph topologiesandtrackingdynamicnetworks,IEEETransactionsonSignalProcessing,
65(2017), pp.3675–3687.
[48] S. Shetty, T. Lembono, T. Loew, and S. Calinon, Tensor train for global optimization
problems in robotics,TheInternational JournalofRoboticsResearch,43(2024), pp.811–
839.
[49] N.Tokcan,S.S.Sofi,V.T.Pham,C.Pr´evost,S.Kharbech,B.Magnier,T.P.Nguyen,
Y. Zniyed, and L. De Lathauwer, Tensor decompositions for signal processing: The-
ory,advances,andapplications,SignalProcessing,238(2026),p.110191,https://doi.org/
https://doi.org/10.1016/j.sigpro.2025.110191.
[50] A. Wang, Y. Qiu, H. Huang, Z. Jin, G. Zhou, and Q. Zhao, Towards a geometric under-
standing of tensor learning via the t-product, Advances inNeural Information Processing
Systems,38(2026), pp.141360–141382.
[51] Y.WangandY.Yang,Hot-svd: higherordert-singularvaluedecompositionfortensorsbased
on tensor–tensor product, Computational andAppliedMathematics,41(2022), p.394.
[52] W. S. Wijesoma, L. L. Perera, and M. D. Adams, Toward multidimensional assignment
data association in robot localization and mapping, IEEE Transactions on Robotics, 22
(2006), pp.350–365.
[53] J. W. Woods, Multidimensional signal, image, and video processing and coding, Academic
press,2011.
[54] J.Wu,Z.Lin,andH.Zha,Essentialtensorlearningformulti-viewspectralclustering,IEEE
Transactions onImageProcessing,28(2019), pp.5910–5922.
[55] S. Xia, D. Qiu, and X. Zhang, Tensor factorization via transformed tensor-tensor product
for image alignment,NumericalAlgorithms,95(2024), pp.1251–1289.
[56] M. Yin, J. Gao, S. Xie, and Y. Guo, Multiview subspace clustering via tensorial t-product
representation, IEEE Transactions onNeuralNetworks andLearningSystems, 30(2018),
pp.851–864.
[57] J.Zhang,A.K.Saibaba,M.E.Kilmer,andS.Aeron,Arandomized tensorsingularvalue
decomposition based on the t-product, Numerical Linear Algebra with Applications, 25
(2018), p.e2179.
[58] Z. Zhang and S. Aeron, Exact tensor completion using t-svd, IEEE Transactions on Signal
Processing,65(2016), pp.1511–1526.
20
---- END DOCUMENT ----
