Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
Construction and Design of MPAC Codes
Fangbo Yi, Zuoxin Cai, Zhongjun Yang, Student Member, IEEE, Li Chen, Senior
Member, IEEE, Huazi Zhang, Senior Member, IEEE, Wenxin Liu, and Yuan Li
Abstract
This paper proposes modified polarization-adjusted convolutional (MPAC) codes and their hybrid
decodingthatachievesanimprovedperformance-complexitytradeoff.ForMPACcodes,onlyasubsetof
theinformationbitsundergotheconvolutionaltransform.Theoutputisthencombinedwiththeremaining
informationbitsfortheinnerpolartransform.Correspondingly,theconvolutionallytransformedbitsare
recovered by Fano decoding, while the remaining information bits are recovered by the successive
cancellation (SC) decoding, constitutingthe hybrid Fano-successive cancellation (HFSC) decoding. The
MPAC codes are further designed by the coset-wise analysis that characterizes the number of minimum
weight codewords (MWCs). It is discovered that a partially convolutional transform can improve the
codeword through utilizing the row combinations of the frozen set efficiently. This property enables the
MPAC codes to outperform their prototype polarization-adjusted convolutional (PAC) codes and cyclic
redundancy check (CRC)-polar codes. Furthermore, MPAC codes can be optimized by reducing the
number of MWCs. Our numerical results demonstrate that, with a similar decoding complexity budget,
the MPAC codes offer competent decoding performance when compared with PAC codes using Fano
decoding and CRC-polar codes using SC list (SCL) decoding.
Index Terms
Fanodecoding,minimumweightdistribution,polarcodes,polarization-adjustedconvolutionalcodes.
This article was presented in part at the 2023 IEEE International Symposium on Information Theory (ISIT)
[DOI:10.1109/ISIT54713.2023.10206642].
Fangbo Yi, Zuoxin Cai, Zhongjun Yang and Wenxin Liu are with the School of Electronics and Information Tech-
nology, Sun Yat-sen University, Guangzhou 510006, China (e-mail: yifb@mail2.sysu.edu.cn; caizx7@mail2.sysu.edu.cn;
yangzhj59@mail2.sysu.edu.cn; liuwx6@mail2.sysu.edu.cn).
Li Chen is with the School of Electronics and Information Technology, Sun Yat-sen University, Guangzhou 510006, China,
and also with Guangdong Province Key Laboratory of Information Security Technology, Guangzhou, 510006, China (e-mail:
chenli55@mail.sysu.edu.cn).
Huazi Zhang and Yuan Li are with Hangzhou Research Center, Huawei Technologies Co., Ltd., Hangzhou 310052, China
(e-mail: zhanghuazi@huawei.com; liyuan299@huawei.com).
6202
guA
62
]TI.sc[
2v75712.8062:viXra

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 1
I. INTRODUCTION
Polar codes have been proven to achieve capacity of the binary input discrete memoryless
channel (BI-DMC), under the prerequisites of approaching infinite codeword length and the
successive cancellation (SC) decoding [1]. However, for short-to-medium length polar codes,
the SC decoding performances remain limited. A notable improvement can be achieved through
the SC list (SCL) decoding [2] [3], which keeps L distinct instances of the SC decoding paths.
The SCL decoding can approach the maximum likelihood (ML) decoding performance with a
sufficiently large list size L. Further improvement can be obtained by concatenating polar codes
with the cyclic redundancy check (CRC) codes [2] [3], the parity check (PC) codes [4] [5] or
the convolutional codes [6] [7].
The polarization-adjusted convolutional (PAC) codes [7] concatenate an outer rate-1 convo-
lutional code with an inner polar code. It is shown that the normal approximation (NA) bound
can be approached by PAC codes using Fano decoding [7]. However, PAC codes are usually
constructed through the Reed-Muller (RM) rate profiling [7], which yields limited code rates.
Addressing this, the existing polar code rate profiling schemes [1] [8]–[11] can be utilized for
selecting the reliable subchannels, while the RM-polar rate profiling [12] [13] can yield both
a flexible rate choice and improved codeword weight distribution. By further considering the
effect of convolutional transform, performances of PAC codes can be improved. By considering
subchannel utilizations, Liu et al. [14] proposed the weighted sum (WS) metric for a more
flexible rate profiling. It generalizes the RM rate profiling to design PAC code for any desired
rate. Several rate profiling designs have also been proposed in order to optimize the decoding
error probability [15] [16], reducing the Fano decoding complexity [17] [18]. The minimum
weight distribution (MWD) contains knowledge of the code’s minimum Hamming distance and
the number of its minimum weight codewords (MWCs). Moreover, by considering the transpose
of the convolutional transform matrix [19] and formation of MWCs [20], the MWD of PAC
codes can also be improved. It leads to an enhanced ML decoding performance for the codes.
Fano decoding [21] is an efficient algorithm in terms of its required hardware implementation
resources, including memory and computation resources. However, when the received informa-
tion is unreliable, Fano decoding may suffer from a high decoding latency and complexity. To
reduce the Fano decoding complexity, Moradi et al. [22] proposed the path metric function that is
parameterized by the subchannel cutoff rates. Meanwhile, Rowshan et al. [13] proposed several

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 2
tree search strategies to reduce the decoding complexity. They both enable the Fano decoding to
achieve a better performance-complexity tradeoff. To further curb worst-case decoding latency
and complexity, Fano decoding can be performed with a computational threshold [22]–[24].
But it inevitably leads to a decoding performance degradation. So far, limited efforts have been
deployed through redesigning PAC codes in achieving a better performance-complexity tradeoff.
It is known that a code’s ML decoding performance is determined by its weight distribution.
Both polar codes and PAC codes can be designed through optimizing their weight distributions
[19], [20], [25]–[27]. With an exhaustive search, weight distribution of both polar codes and PAC
codes can be computed, but only up to the length of 64 bits [25] [27]. Utilizing the recursive
structure of polar codes, the probabilistic methods [28] [29] can estimate the codes’ weight
distribution. With a similar approach, Li et al. [30] analyzed the average weight distribution of
the pre-transformed polar codes which include PAC codes. Overall, it remains challenging to
compute a code’s entire weight distribution. Consequently, the MWD becomes a predominant
metric in asymptotic performance analysis, as it dictates the error probability floor at high signal-
to-noise ratio (SNR) regimes [31]. For a family of polar codes that are defined by the partial
order property, Bardet et al. [32] provided an explicit formula for computing the number of
MWCs. For the same family of codes, Rowshan et al. [20] characterized the row combinations
of the MWCs under the coset-wise framework using a set-theoretic approach. It can be further
generalized for analyzing the MWD of PAC codes [33]. Besides the above mentioned theoretical
analysis, the MWD of both polar codes and PAC codes can also be numerically estimated. Li
et al. [34] proposed the SCL-based enumeration method to evaluate the number of MWCs. But
it requires a huge memory and complexity since the decoding output list size L needs to be
sufficiently large.
This paper proposes the modified PAC (MPAC) codes and their hybrid Fano-SC (HFSC)
decoding. This coding scheme was first proposed in our previous work of [35], which performs
convolutional transform only for a portion of information bits. It limits the number of nodes that
are allowed for backtracking, yielding a better performance-complexity tradeoff than the relevant
coding schemes. In this work, the MPAC code design is further proposed based on the coset-wise
analysis of its MWD, leading to the approximated union bound (AUB)-optimal MPAC codes
that have a better MWD than PAC codes and CRC-polar codes. It also shows the effectiveness
of the partially convolutional transform design for improving the MWD. Major contributions of
this work are summarized as follows:

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 3
The MPAC codes are proposed. In the coding scheme, only a subset of information bits
•
undergotheconvolutionaltransform.Itsoutputbitsarethenconcatenatedwiththeremaining
| information | bits for | the inner | polar transform. |     |     |     |     |
| ----------- | -------- | --------- | ---------------- | --- | --- | --- | --- |
The HFSC decoding is further proposed to decode information bits. It recovers the con-
•
volutionally transformed information bits and the remaining information bits through Fano
decoding and SC decoding, respectively. Our numerical results show that with a budgeted
complexity, the proposed scheme yields a better performance-complexity tradeoff than Fano
| decoding | of PAC codes | and | SCL decoding | of CRC-polar | codes. |     |     |
| -------- | ------------ | --- | ------------ | ------------ | ------ | --- | --- |
• The coset-wise analysis of the MWD of MPAC codes is presented, which leads to design
the AUB-optimal MPAC codes. By considering the impact of frozen bits in MPAC codes,
it characterizes the row combinations of the MWCs. By further validating generation of the
characterized codewords, the exact volume of MWCs in MPAC codes can be obtained. For
a wide range of code parameters, the designed MPAC codes yield a better MWD than PAC
| codes | and CRC-polar | codes. |     |     |     |     |     |
| ----- | ------------- | ------ | --- | --- | --- | --- | --- |
The rest of this paper is organized as follows. Section II provides the background knowledge
on polar codes and PAC codes. Section III proposes the MPAC codes and their HFSC decod-
ing. Section IV analyzes the MWD of MPAC codes in the coset-wise framework. Section V
presents the design of AUB-optimal MPAC codes and their numerical results. Finally, Section
VI concludes this paper. Ahead of the rest sections, we first state our notation fashion as follows.
| F   | = {0,1} | ⊕   |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
Let 2 and denote the binary field and its addition operator, respectively. We
also let ⊕ denote the addition operator between the binary vectors. Let [l,u] denote the set
{l,l + 1,...,u}, where l < u. For a set A ⊆ [0,N − 1], its cardinality and complementary
aj,
set are denoted by |A| and Ac, respectively. Further let where i < j, denote the vector
i
(a ,a ,...,a ). Given a vector aN−1 and a set A ⊆ [0,N − 1], we use a to denote its
| i i+1 | j   |     | 0   |     |     | A   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
subvector (a | i ∈ A). Note when A = [0,N −1], aN−1 = a . The binary representation of an
|     | i   |     |     |     | A   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0
integer i ∈ [0,2n −1] is defined as bin(i) = i ...i i , where i is the most significant bit
|     |                  |     |     | n−1 1 0 | n−1 |     |     |
| --- | ---------------- | --- | --- | ------- | --- | --- | --- |
|     | (cid:80)n−1i 2b. |     |     | aN−1    |     |     |     |
and i = The support of a vector is the index set of its non-zero coordinates,
|            | b=0 b |     |     | 0   |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- |
| supp(aN−1) | ≜     |     |     |     |     |     | ≜   |
i.e., {i ∈ [0,N −1] | a ̸= 0}. Let S denote the support of bin(i), i.e., S {b ∈
|     | 0   |     | i   | i   |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- |
[0,n−1] | i ̸= 0}. Furthermore, let S \S denote all elements in the support of bin(j) but are not
|     | b   |     | j i |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
in the support of bin(i). The Hamming weight of a vector cN−1 ∈ FN is denoted as w(cN−1) ≜
|     |     |     |     |     | 0 2 |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|supp(cN−1)|. Given two vectors c = (c ,c ,...,c ) ∈ FN and c′ = (c′,c′,...,c′ ) ∈ FN,
|     | 0   |     | 0 1 | N−1 | 2   | 0 1 | N−1 2 |
| --- | --- | --- | --- | --- | --- | --- | ----- |
the Hamming distance between them is defined as d(c,c′) = |{i ∈ [0,N −1] | c ̸= c′}|.
i
i

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |           |     |       |     |     |       |     |     |     | 4   |
| ----------------------------------------------- | --- | --- | --- | --------- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- |
|                                                 |     |     |     | II. POLAR |     | CODES |     | PAC | CODES |     |     |     |     |
AND
Thissectionprovidestheprerequisitesforthiswork,includingpolarcodesanditsSCdecoding,
| PAC             | codes | and its Fano | decoding. |       |     |     |     |     |     |     |     |     |     |
| --------------- | ----- | ------------ | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. Approximated |       | Union        | Bound     | (AUB) |     |     |     |     |     |     |     |     |     |
A K-dimensional subspace C of FN is called an (N,K,d ) binary linear block code, where
min
2
N and K are the length and dimension of the code, respectively, and the minimum distance
| d   | of the | code is defined |     | as  |     |     |     |     |     |     |     |     |     |
| --- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
min
d(c,c′).
|     |     |     |     |     | d   | =   | min |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
min
c,c′∈C,c̸=c′
For a binary input additive white Gaussian noise (BI-AWGN) channel, union bound [31] on
the ML decoding frame error rate (FER), denoted as P , of a binary linear block code is
e
N
|     |     |     |     |     |     |     | (cid:16)(cid:112) |     | (cid:17) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --- | --- | --- | --- |
(cid:88)
|     |     |     |     | P ≤ |     | A Q | 2d·R·E |     | /N  | ,   |     |     | (1) |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
|     |     |     |     | e   |     | d   |        |     | b 0 |     |     |     |     |
d=dmin
|     |     |     |     |     |     |     |     |     |     |     | (cid:82) 2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
where A denotes the number of weight-d codewords, Q(y) = 1 ∞ e−ϑ dϑ is the tail
|     | d   |     |     |     |     |     |     |     |     | √   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | 2π  | y   |     |     |
distribution function of the standard normal distribution, R = K/N is the code rate and E /N
|     |     |     |     |     |     |     |     |     |     |     |     |     | b 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is the SNR per information bit. The MWD is defined by both d and A . As SNR increases,
|     |     |     |     |     |     |     |     |     | min |     | dmin |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
MWD becomes dominant for (1). Hence, the union bound can be approximated by
|     |     |     |     |     |      | (cid:16)(cid:112) |     |      | (cid:17) |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ----------------- | --- | ---- | -------- | --- | --- | --- | --- |
|     |     |     |     | P ≈ | A    | Q                 | 2d  | ·R·E | /N       | .   |     |     | (2) |
|     |     |     |     | e   | dmin |                   | min |      | b 0      |     |     |     |     |
The above AUB is often utilized to assess the operational performance of a designed binary
| linear   | block | code. |             |     |     |     |     |     |     |     |     |     |     |
| -------- | ----- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B. Polar | Codes | and   | SC Decoding |     |     |     |     |     |     |     |     |     |     |
Polar codes are founded on channel capacity polarization which is the consequence of channel
combining and splitting [1]. Given a BI-DMC W : X → Y, with X ∈ F and Y ∈ R, a set of N
2
polarized subchannels W(i) : X → YN ×Xi−1 can be obtained through the channel polarization
N
|          |       | N = 2n, | n   | ∈ N+ | i   | ∈ [0,N−1]. |     | I(W) |     | I(W(i)) |        |               |     |
| -------- | ----- | ------- | --- | ---- | --- | ---------- | --- | ---- | --- | ------- | ------ | ------------- | --- |
| process, | where |         |     | and  |     |            |     | Let  | and |         | denote | the symmetric |     |
N
W(i)
capacity of channel W and subchannel , respectively. Channel polarization results in most
N
|     |     | W(i) |     |     |     |     |     |     | I(W(i)) |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
of the subchannels becoming either noiseless with → 1, or heavily noisy with
|     |     |     | N   |     |     |     |     |     | N   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I(W(i))
→ 0.
N

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     | 5   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
An (N,K) polar code is constructed by the rate profiling and polar transform G = F⊗n,
p
|     | ((1,0),(1,1))T |     | F2×2 |     |     |     |     |     |     |     |
| --- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
where F = ∈ is the kernel matrix and ⊗ denotes the Kronecker product.
2
|     |     |     |     |     |     |     |     |     | mK−1 FK |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
Rate profiling with parameters (N,K,I) embeds the information vector ∈ into a
|     |     |     |     |     |     |     |     |     | 0 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
FN.
carrier vector uN−1 ∈ It is defined by the information set I ⊆ [0,N − 1] and the frozen
|     | 0   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
set Ic = [0,N −1]\I, such that u = mK−1 and u = 0. After rate profiling, the codeword
|     |     |     |     | I   | 0   |     | Ic  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cN−1 ∈ FN can be generated by polar transform as cN−1 = uN−1G . By denoting the polar
| 0 2 |     |     |     |     |     |     | 0   | 0   | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transform matrix G as G = [gT,gT,...,gT ]T, the polar codeword can be defined as
|     | p   | p     |     |     |      |          |     |         |     |     |
| --- | --- | ----- | --- | --- | ---- | -------- | --- | ------- | --- | --- |
|     |     |       | 0   | 1   | N−1  |          |     |         |     |     |
|     |     | uN−1G |     | = u | g ⊕u | g ⊕···⊕u |     | g       | .   | (3) |
|     |     |       | 0 p | 0   | 0    | 1 1      |     | N−1 N−1 |     |     |
With rate profiling that sets u = 0, {g | i ∈ I} forms a basis of the polar codebook, denoted
|     |     |     | Ic  |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as C(I).
Polar codes are decoded by the SC algorithm in which the information bits are estimated
successively based on their decision log-likelihood ratios (LLRs). Let us assume that codeword
cN−1 is transmitted through a noisy channel using binary phase shift keying (BPSK) modulation.
0
Let yN−1 = (y ,y ,...,y ) ∈ RN and uˆN−1 = (uˆ ,uˆ ,...,uˆ ) ∈ FN denote the received
|     | 0 1 | N−1 |     |     | 0   |     | 0 1 | N−1 | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
symbol vector and the estimated carrier vector, respectively. Over the SC decoding trellis, the
| decision LLR | of the estimated |     | bit | uˆ is | defined | as  |     |     |     |     |
| ------------ | ---------------- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     | P(yN−1,uˆi−1 |     | | uˆ = | 0)  |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | --- | --- |
i
|     |     |     | L(i) | = ln | 0            | 0   |        | ,   |     | (4) |
| --- | --- | --- | ---- | ---- | ------------ | --- | ------ | --- | --- | --- |
|     |     |     | N    |      | P(yN−1,uˆi−1 |     | | uˆ = | 1)  |     |     |
|     |     |     |      |      |              | 0   | i      |     |     |     |
0
where P(yN−1,uˆi−1 | uˆ ) is the transition probability of W(i) . Estimation uˆ can be successively
|     | 0   | i   |     |     |     |     | N   |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
made based on the decision LLR of (4). For i ∈ Ic, uˆ = 0 as they are frozen. For i ∈ I, u is
|     |     |     |     |     |     |     | i   |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
an information bit which can be estimated based on a bitwise ML decision rule as

|     |     |     |      |         |  0, |     | if L(i)    | ≥ 0 ; |     |     |
| --- | --- | --- | ---- | ------- | ----- | --- | ---------- | ----- | --- | --- |
|     |     |     |      | Υ(L(i)) |       |     | N          |       |     |     |
|     |     |     | uˆ = |         | =     |     |            |       |     | (5) |
|     |     |     | i    |         | N     |     |            |       |     |     |
|     |     |     |      |         |  1, |     | otherwise. |       |     |     |
The SC decoding complexity is measured as the number of LLR computations, i.e., N log N.
2
| C. PAC Codes | and Fano | Decoding |     |     |     |     |     |     |     |     |
| ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
APACcodeconcatenatesanouterrate-1convolutionaltransformwithaninnerpolartransform,
as shown in Fig. 1. This concatenation protects the message bits in the inner code through
utilizingtheircorrelationprovidedbytheconvolutionaltransform,yieldinganimproveddecoding
performance.

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |          |         |     |            |               |           |     |           |     |     |     | 6   |
| ----------------------------------------------- | -------- | ------- | --- | ---------- | ------------- | --------- | --- | --------- | --- | --- | --- | --- |
|                                                 |          |         |     | Rate       | Convolutional |           |     | Polar     |     |     |     |     |
|                                                 |          |         |     | Profiling  |               | Transform |     | Transform |     |     |     |     |
| Fig.                                            | 1. Block | diagram | of  | PAC codes. |               |           |     |           |     |     |     |     |
Algorithm 1: Generation of a single convolutional output bit, conv1b(·)
|     | Input: | v, S, | gt; |     |     |     |     |     |     |     |     |     |
| --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     | Output:    | u,  | S;     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | Initialize | u   | = v ·g | ;   |     |     |     |     |     |     |     |     |
0
|     | For | j = 1 → | |S| | do  |     |     |     | // |S| | previous |     | inputs |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | ------ | -------- | --- | ------ | --- |
2
|     | If  | g = 1 | then    |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3   |     | j     |         |     |     |     |     |     |     |     |     |     |
|     |     | u =   | u⊕S[j]; |     |     |     |     |     |     |     |     |     |
4
| 5   | S =    | (v,S[1],··· | ,S[t−1]); |     |     |     | // update | shift | register |     | state |     |
| --- | ------ | ----------- | --------- | --- | --- | --- | --------- | ----- | -------- | --- | ----- | --- |
|     | Return | [u,S];      |           |     |     |     |           |       |          |     |       |     |
6
|     | sN−1 |     | FN  | uN−1 FN |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Let ∈ and ∈ denote the input and output vectors of the convolutional
|     |     | 0   | 2   | 0 2 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transform,respectively.To encodean(N,K) PACcode,informationvectormK isfirstembedded
1
into sN−1 under the rate profiling with parameters (N,K,I), such that s = mK−1 and s = 0.
|     | 0    |            |           |        |               |     |           |     | I   | 0   | Ic  |     |
| --- | ---- | ---------- | --------- | ------ | ------------- | --- | --------- | --- | --- | --- | --- | --- |
|     | uN−1 | is further | generated | by the | convolutional |     | transform | as  |     |     |     |     |
0
t
(cid:88)
|     |     |     |     |     | u   | =   | g s , |     |     |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     | i   |     | j i−j |     |     |     |     |     |
j=0
where gt = (g ,g ,...,g ) ∈ Ft+1 are coefficients of the convolutional generator polynomial.
|     |     |     | 0 1 | t 2 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
Let S = (S[1],S[2],··· ,S[t]) denote state of the convolutional shift registers. Algorithm 1
(conv1b(·)) describes the generation of a convolutional output bit u based on the current state
S and the input bit v. Equivalently, the convolutional transform can be represented in an upper-
|     |     |     |     | FN×N, |     |     |     |     |     |     | gt. |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
triangular Toeplitz matrix G ∈ whose rows are formed by shifting the vector Hence,
|     |     |     |     | c 2 |     |     |     |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
uN−1 = sN−1G . Finally, the PAC codeword cN−1 is further generated by cN−1 = uN−1G .
| 0   |     | 0   | c   |     |     |     | 0   |     |     | 0   | 0   | p   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore, convolutional coded bits uN−1 are transmitted through the polarized subchannels.
0
Fano decoding was first adopted to decode PAC codes, in which the constraints of the
convolutional transform is imposed [7]. It can be seen as a depth-first search algorithm with
the path metrics serving as the reliability indicators. In this paper, we use the optimal path
| metric | function |     | [22],  | which can be       | computed | layer-by-layer |                      | as  |           |     |     |     |
| ------ | -------- | --- | ------ | ------------------ | -------- | -------------- | -------------------- | --- | --------- | --- | --- | --- |
|        |          |     | M(uˆi) | = M(uˆi−1)+1.0+log |          |                | P(uˆ | yN−1,uˆi−1)−E |     | (1,W(i)), |     |     | (7) |
|        |          |     |        | 0 0                |          | 2              | i                    | 0   | 0         |     |     |     |
|        |          |     |        |                    |          |                | 0                    |     |           | N   |     |     |

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     |     |     | 7   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where P(uˆ | yN−1,uˆi−1) and E (1,W(i)) are the a posteriori probability of uˆ and the cutoff
|     | i   |     |      | 0   |     |     |     |     |     |          | i   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
|     |     | 0   | 0    |     | N   |     |     |     |     |          |     |     |
|     |     |     | W(i) |     |     |     |     |     |     | (1,W(i)) |     |     |
rate of subchannel , respectively. For the BI-AWGN channel, E can be obtained
|     |     |     | N   |     |     |     |     |     | 0   |     | N   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by [36]
|     |         |     | (1,W(i)) |     |         | (1+exp(−1/(2(σ(i))2))), |      |     |     |     |     |     |
| --- | ------- | --- | -------- | --- | ------- | ----------------------- | ---- | --- | --- | --- | --- | --- |
|     |         |     | E        |     | = 1−log |                         |      |     |     |     |     | (8) |
|     |         |     | 0        | N   |         | 2                       |      |     | N   |     |     |     |
|     | (σ(i))2 |     |          |     |         |                         | W(i) |     |     |     |     |     |
where is the simulated noise variance of . It can be estimated via the Gaussian
|     | N   |     |     |     |     |     |     | N   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
approximation (GA) [10]. By adjusting threshold T dynamically with a step size ∆ [21], Fano
M(uˆi)
| decoding | compares |     |     | in controlling |     | the decoding |     | moves | as: |     |     |     |
| -------- | -------- | --- | --- | -------------- | --- | ------------ | --- | ----- | --- | --- | --- | --- |
0
| 1) If | {M(uˆi)} |       | ≥ T, move | forward |     | to path | {uˆi} | ;   |     |     |     |     |
| ----- | -------- | ----- | --------- | ------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
|       |          | 0 max |           |         |     |         | 0     | max |     |     |     |     |
2) If {M(uˆi)} < T, move backward to the root node of the tree, or the ancestor node uˆ
|     |     | 0 max |     |     |     |     |     |     |     |     |     | i′  |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which satisfies {M(uˆi′ )} > T, where i′ ≤ i, and the path {uˆi′ } has not been visited.
|     |     |     | min |     |     |     |     |     | min |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 0   |     |     |     |     |     | 0   |     |     |     |
At the beginning of the decoding, state of the shift registers and the path metric are initialized
(cid:0) uˆ−1(cid:1)
as S = 0 and M = 0, respectively. Assuming that bit uˆ (i ∈ I) has been explored by Fano
|     |     | 0   |     |     |     |     |     | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
decoding and the current state of shift registers is S, the information bit sˆ can be determined
i
| by the | convolutional |     | constraint | as  |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |  1, | if conv1b(1,S,gt) |     |     | = [uˆ | ,S′] ; |     |     |
| --- | --- | --- | --- | --- | ----- | ----------------- | --- | --- | ----- | ------ | --- | --- |
i
|     |     |     | sˆ = λ(uˆ | ,S) = |       |            |     |     | 0   |     |     |     |
| --- | --- | --- | --------- | ----- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
|     |     |     | i         | i     |       |            |     |     |     |     |     | (9) |
|     |     |     |           |       |  0, | otherwise, |     |     |     |     |     |     |
where S′ means the next shift registers corresponding to the output estimation uˆ . Furthermore,
i
the next state S is updated by S′. Once the decoding reaches a leaf of the tree, the complete
|             |     | uˆN−1 | sˆN−1 |      |           |     |      |          |     |     |     |     |
| ----------- | --- | ----- | ----- | ---- | --------- | --- | ---- | -------- | --- | --- | --- | --- |
| estimations | of  |       | and   | are  | obtained. |     |      |          |     |     |     |     |
|             |     | 0     | 0     |      |           |     |      |          |     |     |     |     |
|             |     |       | III.  | MPAC | CODES     | AND | HFSC | DECODING |     |     |     |     |
This section introduces the MPAC codes and their HFSC decoding, which can yield a good
performance-complexity tradeoff. Construction of the MPAC encoding includes two rate profil-
ings which are defined by the proposed improved RM-polar (iRMP) orderings and the Gaussian
approximation (GA), respectively. The HFSC decoding integrates Fano decoding and SC decod-
| ing to recover  |     | the information |            | bits. |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. Construction |     | of              | MPAC Codes |       |     |     |     |     |     |     |     |     |
For an (N,K) MPAC code, it needs to be further specified by the convolutional parameters
| (N ,K | ),  | N   |     |     |     |     |     |     |     | G′  | ∈ FNc×Nc | K   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
c c where c is the dimension of the convolutional transform as and c
c 2

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |             |     |     |               |             |       |           |     | 8   |
| ----------------------------------------------- | --- | --- | ----------- | --- | --- | ------------- | ----------- | ----- | --------- | --- | --- |
|                                                 |     |     | Rate        |     |     | Convolutional |             |       |           |     |     |
|                                                 |     |     | Profiling Ⅰ |     |     | Transform     |             |       |           |     |     |
|                                                 |     |     |             |     |     |               |             | Rate  | Polar     |     |     |
|                                                 |     |     |             |     |     |               | Profiling Ⅱ |       | Transform |     |     |
Information bits
Remaining information bits:
| Fig. 2. | Block diagram | of  | the (N,K)-(N | ,K  | ) MPAC | codes. |     |     |     |     |     |
| ------- | ------------- | --- | ------------ | --- | ------ | ------ | --- | --- | --- | --- | --- |
|         |               |     |              | c   | c      |        |     |     |     |     |     |
is the number of information bits that undergo the transform. Fig. 2 shows the encoding block
diagram of an (N,K)-(N ,K ) MPAC code. The convolutional parameters should satisfy
|     |     |     | c   | c   |     |       |       |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | ---- |
|     |     |     |     |     | K   | −K +N | ≤ N.  |     |     |     | (10) |
|     |     |     |     |     |     | c     | c     |     |     |     |      |
|     |     |     |     |     |     |       | (N,K) |     |     | K   | = K  |
The equality holds when the MPAC code becomes the PAC code, i.e., when c
and N = N. Hence, the MPAC codes can be considered as a more general case of PAC codes
c
where the convolutional transform is performed on a portion of the information bits.
To encode an (N,K)-(N ,K ) MPAC code, the information bits mK−1 is partitioned into
|     |     |     |     | c c |     |     |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mK−1 = (mKc−1,mK−1), where mKc−1 and mK−1 denote the information bits that will undergo
| 0   | 0   |     | Kc  |     | 0   | Kc  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the convolutional transform and the remaining information bits, respectively. Furthermore, rate
profiling I and II are utilized to construct the input vectors of the convolutional transform and
|     |     |     |     | sNc−1 |     | uN−1, |     |     |     | mKc−1 |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | ----- | --- |
the polar transform, denoted as and respectively. The information bits will
|     |     |     |     | 0   |     | 0   |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sNc−1
first be embedded into the vector under the rate profiling I with parameter (N ,K ,D),
|     |     |     |     |     | 0   |     |     |     |     | c   | c   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where D ⊆ [0,N ] and |D| = K . sNc−1 is constructed as sNc−1 = (s ,s ), where s =
|     |     | c   |     |     | c 0 |     |     | 0   | D Dc |     | D   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
mKc−1 and s = 0. The convolutional codeword is further generated by vNc−1 = sNc−1G′. It
| 0   | Dc  |     |     |     |     |     |     |     | 0   | 0   | c   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
will be concatenated with the remaining information bits mK−1 to be transmitted through the
Kc
polarized subchannels. The subchannels are chosen for transmitting information bits based on
their reliabilities. Let A ⊆ [0,N − 1] denote the index set of the K − K + N most reliable
c c
subchannels. Among set A, the N least reliable subchannels are indexed by set P. Consequently,
c
| under | rate profiling |     | II, the vector |     | uN−1 | is partitioned | into |     |     |     |     |
| ----- | -------------- | --- | -------------- | --- | ---- | -------------- | ---- | --- | --- | --- | --- |
0
|     |     |     |     |     | uN−1 | = (u | ,u ,u ), |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | -------- | --- | --- | --- | --- |
(11)
|     |     |     |     |     | 0   | A\P | P Ac |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
where u = mK−1, u = vNc−1 and u = 0 are the remaining information bits, the convolu-
|     | A\P | Kc  | P   | 0   |     | Ac  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     | 9   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tional codeword and the frozen bits, respectively. Finally, the MPAC codeword is generated by
cN−1 uN−1G
| =   | , where | again | G   | is the | polar transform | matrix. |     |     |
| --- | ------- | ----- | --- | ------ | --------------- | ------- | --- | --- |
| 0   | 0 p     |       | p   |        |                 |         |     |     |
With the above description, it can be seen that the two rate profilings that are specified
by the index sets A, P and D, and the convolutional parameters (N ,K ) determine an MPAC
c c
code. They also interplay in determining the MPAC codes’ optimal and practical error-correction
performances. In particular, rate profiling II assigns the convolutional output and the remaining
information bits based on the polarized subchannels reliabilities, while rate profiling I is further
designed to provide a good weight distribution of MPAC codes. This effect will be revealed in
Section IV. To realize this design, GA [10] and an iRMP ordering [13] are utilized. Selection
of the convolutional parameters (N ,K ) will be further discussed in Sections III-C V.
c c
Ascending mean LLRs
Index set
Ascending iRMP orderings
Index set
| Fig. 3. Construction | of index | sets. |     |     |     |     |     |     |
| -------------------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
Fig. 3 shows the construction of index sets in the two rate profilings. It begins with the
A P
construction of index sets and of the rate profiling II using GA. By assuming an all-zero
W(i)
codeword, GA estimates the mean LLR value of all polarized subchannels , which are
N
|     | L(W(i)) |     |     |     |     |     | W(i) | L(W(i)) |
| --- | ------- | --- | --- | --- | --- | --- | ---- | ------- |
denoted as and i ∈ [0,N −1]. Note that the subchannel with a greater
|     | N   |     |     |     |     |     | N   | N   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
is more reliable, and vice versa. Hence, the N subchannels can be ordered by their reliabilities,
yielding a refreshed subchannel index tuple (j ,j ,...,j ) , which implies
|     |     |          |     |          | 0 1   | N−1 GA |     |     |
| --- | --- | -------- | --- | -------- | ----- | ------ | --- | --- |
|     |     | L(W(j0)) |     | L(W(j1)) |       | (jN−1) |     |     |
|     |     |          |     | >        | > ··· | > L(W  | ).  |     |
|     |     |          | N   |          | N     | N      |     |     |
Since A is the sorted index set of the K −K +N most reliable subchannels, we have
|     |     |     |     |      | c c           |     |     |      |
| --- | --- | --- | --- | ---- | ------------- | --- | --- | ---- |
|     |     |     | A   | = {j | ,j ,...,j     | }.  |     | (12) |
|     |     |     |     |      | 0 1 K−Kc+Nc−1 |     |     |      |

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |              |     |        |     |       |          |             |     |     |     |     |     | 10  |
| ----------------------------------------------- | --- | ------------ | --- | ------ | --- | ----- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
| Among                                           |     | A, the index | set | of the | N   | least | reliable | subchannels |     | is  |     |     |     |     |
c
|     |     |     |     | P   | = {j | ,j   |        | ,...,j |           |     | }.  |     |     | (13) |
| --- | --- | --- | --- | --- | ---- | ---- | ------ | ------ | --------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |      | K−Kc | K−Kc+1 |        | K−Kc+Nc−1 |     |     |     |     |      |
When considering the design of rate profiling I, we also use I and F to denote the general
information set and general frozen set w.r.t. the information set and the frozen set of the inner
polar code, respectively. For simplicity, subscripts ∗ and ∗ are used to denote those that will
|     |     |     |     |     |     |     |     |     | c   | p   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
undergo the convolutional transform and those that will not, respectively. Hence, I = I ∪I and
|     |     |     |     |     |     |     |     |     |     |     |     |     | c p |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F = F ∪F . Consequently, rate profiling II constructs I = A\P, F = Ac and P = I ∪F
|     | c   | p   |     |     |     |     |     |     |     | p   | p   |     | c   | c   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
under the GA ordering, while rate profiling I only constructs I and F . Selecting the indices that
|     |     |     |     |     |     |     |     |     |     | c   | c   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
indicate rows of higher weights in G in forming I would result in a better weight distribution
p
2|Si|
for the code [12] [13]. For simplicity, let r(i) = = w(g ) denote the weight of row g ,
|     |     |     |     |     |     |     |     |     |     |     | i   |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where i ∈ [0,N −1] and S denotes the support of bin(i). To improve the weight distribution of
i
an MPAC code, a feasible approach is to construct I by selecting the indices with higher r(i)
c
values from the set P. It can be realized by the iRMP rate profiling [13], as it can often result
| in a | better | weight | distribution |     | than | the RM-polar |     | rate | profiling |     | [12]. |     |     |     |
| ---- | ------ | ------ | ------------ | --- | ---- | ------------ | --- | ---- | --------- | --- | ----- | --- | --- | --- |
Definition I (iRMP Ordering). Given indices i,j ∈ [0,N − 1], we define iRMP ordering
| (i,j) |     | if they | satisfy | either | of  | the following |     | conditions: |     |     |     |     |     |     |
| ----- | --- | ------- | ------- | ------ | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
iRMP
| •   | r(i) | > r(j); |         |     |          |     |      |     |          |     |     |     |     |     |
| --- | ---- | ------- | ------- | --- | -------- | --- | ---- | --- | -------- | --- | --- | --- | --- | --- |
|     |      |         | L(W(i)) |     | L(W(j)). |     |      |     |          |     |     |     |     |     |
|     | r(i) | = r(j)  | and     |     | ≥        |     |      |     |          |     |     |     |     |     |
| •   |      |         |         | N   |          | N   |      |     |          |     |     |     |     |     |
|     |      |         |         |     |          |     | W(i) |     | L(W(i)), |     |     |     |     |     |
Note that the mean LLR of subchannel , i.e., can be estimated by GA for i ∈
|     |     |     |     |     |     |     | N   |     |     | N   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[0,N −1].
|       |     | L(W(i)) | ̸= L(W(j)) |     |         | i,j | ∈ [0,N | −1] |     | i ̸= | j,                    |     |           |     |
| ----- | --- | ------- | ---------- | --- | ------- | --- | ------ | --- | --- | ---- | --------------------- | --- | --------- | --- |
| Since |     |         |            |     | for any |     |        |     | and |      | it is straightforward |     | to verify |     |
|       |     | N       |            | N   |         |     |        |     |     |      |                       |     |           |     |
that the iRMP ordering is a total order. Note that any two indices belonging to [0,N −1] are
| comparable |     | under | the | iRMP | ordering. |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ----- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Under the iRMP ordering, the indices in set P are ordered, yielding an N -tuple (j ,j ,...,
|     |     |     |     |     |     |     |     |     |     |     |     | c   | [0] [1] |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
j ) and [ ∗ ] is a mapping of [0,N − 1] → [K − K ,K − K + N − 1]. The tuple
| [Nc−1] | iRMP |     |     |     |     |     | c   |     |     |     | c c | c   |     |     |
| ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
implies that for any a′,b′ ∈ [0,N −1] and a′ < b′, we have (j ,j ) . Indices with the K
|         |      |           |     |              | c             |              |     |        |        | [a′] | [b′] iRMP |     |     | c    |
| ------- | ---- | --------- | --- | ------------ | ------------- | ------------ | --- | ------ | ------ | ---- | --------- | --- | --- | ---- |
| highest | iRMP | orderings |     | are selected |               | to construct |     | set    | B as   |      |           |     |     |      |
|         |      |           |     |              |               | B = {j       | ,j  | ,...,j |        | },   |           |     |     | (14) |
|         |      |           |     |              |               |              | [0] | [1]    | [Kc−1] |      |           |     |     |      |
| where   | B    | ⊆ P and   | |B| | = K .        | Consequently, |              | I   | = B    | and F  | =    | P \B.     |     |     |      |
|         |      |           |     | c            |               |              |     | c      |        | c    |           |     |     |      |

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     | 11  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Index set D characterizes rate profiling I in disposing information bits mKc−1, which is
0
constructed based on sets B and P as follows. Elements of B are first represented in an ascending
bKc−1
order over a vector, yielding = (b ,b ,...,b ), where b < b < ··· < b . A
|     |     |     | 0   |     | 0 1 | Kc−1 |     | 0 1 |     | Kc−1 |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
𭟋
mapping (∗) is further defined as B = {b |i ∈ [0,K −1]} → [0,K −1]. This implies that
|     | B   |     |     |     | i   | c   |     | c   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the index of the coordinate b is determined by i = 𭟋 (b ). Similarly, mapping 𭟋 (∗) is defined
|     |     |     | i   |     |     | B i |     |     | P   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as P → [0,N −1]. Subsequently, index set D can be further constructed as
c
𭟋
|     |     |     | D = {k | ∈ [0,N | −1] | | k = (b),b | ∈ B}, |     |     | (15) |
| --- | --- | --- | ------ | ------ | ----- | --------- | ----- | --- | --- | ---- |
|     |     |     |        |        | c     | P         |       |     |     |      |
where |D| = K . Since P = I ∪F and B = I , mapping functions 𭟋 (∗) and 𭟋 (∗) are
|     | c   |     | c   | c   | c   |     |     | Ic∪Fc |     | Ic  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
also defined, respectively. They are utilized to determine indices of the convolutional codeword
| vNc−1 |     |     | mKc−1 |     |     |     |     |     |     |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
and the information bits in the following HFSC decoding. Note that the above
| 0   |     |     |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mentioned index sets and mapping functions are computed once offline for a particular (N,K)-
| (N ,K | ) MPAC code. |     |     |     |     |     |     |     |     |     |
| ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c c
| B. HFSC | Decoding |     |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fano
Decoding
Message
Extraction
SC
Decoding
| Fig. 4. Block | diagram of | the HFSC | decoding. |     |     |     |     |     |     |     |
| ------------- | ---------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Fig. 4 shows block diagram of the HFSC decoding. This is a successive information recovery,
where the Fano decoding and the SC decoding are deployed for estimating the message bits,
based on the above mentioned index sets I , F , I , and F . In an MPAC code, only partial
|     |     |     |     |     | c c | p   | p   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
information bits undergo the convolutional transform. The HFSC decoding can subsequently
limit the number of nodes that allow backward computation in Fano decoding, and rationalize
the decoding complexity. It deploys the SC decoding to estimate the information bits mK−1 that
Kc
are transmitted through the most reliable subchannels, i.e., those indexed by I . Fano decoding
p
will only be deployed to estimate the convolutional codeword vNc−1 that are transmitted through
0

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 12
the subchannels indexed by I ∪F . Meanwhile, it further estimates the information bits mKc−1
c c 0
that undergo the convolutional transform. Note that during the decoding, the decision LLRs are
computed by the SC decoding rule [37]. The HFSC decoding operates as follows.
• For bits u i that are indexed by i ∈ I c ∪ F c , Fano decoding requests the SC rules for
computing the decision LLRs L(i) and further determines the path metrics {M(uˆi)} and
N 0 max
{M(uˆi)} . Following a node visit as described in Section II-C, it estimates uˆ , where
0 min i′
i′ ≤ i. This indicates that the decoder can potentially correct the previously decoded bits
through backward computation. Furthermore, if i′ ∈ I , the information bit mˆ can be
c j
determined by the convolutional constraint of (9), where the index j = 𭟋 (i′). The Fano
Ic
decoder feeds back the estimated bits uˆ to the SC decoder and continues the decoding.
i′
• For bits u i that are indexed by i ∈ I p ∪ F p , the SC decoding estimates them based on
its decision LLR L(i) as in (5). In particular, when i ∈ F , it directly sets the frozen bits
N p
uˆ = 0. It also updates the path metric M(uˆi) based on the estimated bit uˆ .
i 0 i
Once uˆ is estimated, or equivalently, when i = N, the information bits mˆK−1 can be
N−1 0
retrieved from both mˆKc−1 and uˆN−1. Algorithm 2 summarizes the HFSC decoding, where the
0 0
input index sets I , F , I and F are determined by the rate profilings I and II.
c c p p
Note that the decoding computation threshold can also be utilized for the HFSC decoding to
limit the decoding latency and complexity, which will be introduced in the following subsection.
C. Simulation Results
We first study the performance-complexity tradeoff of the proposed MPAC codes numerically.
Its theoretical insights and improved design will be presented in Sections IV. In this paper, all
codes and decoding performances are evaluated over the AWGN channel using BPSK mod-
ulation. The proposed schemes are compared with relevant coding schemes, including polar
codes under SC decoding, PAC codes under Fano decoding, and CRC-polar codes under SCL
decoding. Both the MPAC codes and PAC codes employ the convolutional generator sequence
(1,0,1,1,0,1,1). MPAC codes are designed using GA at an SNR per codeword symbol of
E /N = 0 dB, while PAC codes are constructed using the RM rate profiling [7]. For both
s 0
the HFSC decoding and Fano decoding, the step size ∆ = 2 which is numerically chosen in
optimizing performance-complexity tradeoff [22]. Both the CRC-polar codes and polar codes are
designed using the reliability sequence in 5G standard [38]. Given N and K, an (N,K)-(N ,K )
c c
MPAC code is alternatively denoted as MPAC-(N ,K ). The convolutional parameters (N ,K )
c c c c

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 13
| Algorithm |        | 2:    |     |       |          |     |     |     |     |     |     |
| --------- | ------ | ----- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
|           |        |       | The | HFSC  | Decoding |     |     |     |     |     |     |
|           | Input: | yN−1, | I , | F , I | , F ;    |     |     |     |     |     |     |
|           |        |       | c   | c p   | p        |     |     |     |     |     |     |
0
|     | Output: | mˆK−1; |     |     |     |     |     |     |     |     |     |
| --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
| 1   | Initialize | i =    | 0 and | j = | 0;  |     |     |     |     |     |     |
| --- | ---------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2   | While      | i ̸= N | do    |     |     |     |     |     |     |     |     |
L(i)
|     | Compute |       | decision | LLR  |     | as  | in (4); |     |     |         |         |
| --- | ------- | ----- | -------- | ---- | --- | --- | ------- | --- | --- | ------- | ------- |
| 3   |         |       |          |      |     | N   |         |     |     |         |         |
| 4   | If      | i ∈ I | ∪F       | then |     |     |         |     |     | // Fano | decoder |
|     |         | c     | c        |      |     |     |         |     |     |         |         |
M(uˆi)
| 5   |     | Compute | path | metrics |     |     | as in | (7); |     |     |     |
| --- | --- | ------- | ---- | ------- | --- | --- | ----- | ---- | --- | --- | --- |
1
|     |     | Perform | a   | node visit | of  | Fano | decoding; |     |     |     |     |
| --- | --- | ------- | --- | ---------- | --- | ---- | --------- | --- | --- | --- | --- |
6
|     |     | Estimate | uˆ  | with | i′ ≤ | i and | let i = | i′ +1; |     |     |     |
| --- | --- | -------- | --- | ---- | ---- | ----- | ------- | ------ | --- | --- | --- |
| 7   |     |          |     | i′   |      |       |         |        |     |     |     |
|     |     | If i′    | ∈ I | then |      |       |         |        |     |     |     |
| 8   |     |          | c   |      |      |       |         |        |     |     |     |
𭟋 (i′)
9 Let j = and determine mˆ by convolutional constraint as in (9);
|     |      |     |     | Ic  |     |     |     | j   |     |       |         |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- |
|     | Else |     |     |     |     |     |     |     |     | // SC | decoder |
10
|     |          | If i     | ∈ F      | then set | uˆ    | = 0;    |       |          |     |       |          |
| --- | -------- | -------- | -------- | -------- | ----- | ------- | ----- | -------- | --- | ----- | -------- |
| 11  |          |          | p        |          | i     |         |       |          |     |       |          |
|     |          | If i     | ∈ I then |          |       |         |       |          |     | // SC | decoding |
| 12  |          |          | p        |          |       |         |       |          |     |       |          |
|     |          | Estimate |          | uˆ based |       | on L(i) | as in | (5)      |     |       |          |
| 13  |          |          |          | i        |       |         | N     |          |     |       |          |
|     |          | Compute  | M(uˆi)   |          | as in | (7) and | let   | i = i+1; |     |       |          |
| 14  |          |          |          | 0        |       |         |       |          |     |       |          |
|     |          | mˆK      | −1       | mˆK      | c−1   | uˆN     | −1;   |          |     |       |          |
| 15  | Retrieve |          | from     |          | and   |         |       |          |     |       |          |
|     |          | 0        |          | 0        |       |         | 0     |          |     |       |          |
mˆK−1
16 Return
0
will be determined by maximizing the HFSC decoding performance, which helps further verify
| the | performance-complexity |     |     |     | tradeoff |     | advantage | of the MPAC | codes. |     |     |
| --- | ---------------------- | --- | --- | --- | -------- | --- | --------- | ----------- | ------ | --- | --- |
Decoding complexity is measured as the average number of LLR computations required
Φ
to decode a codeword. A decoding LLR computation threshold is introduced to bound
the decoding complexity and latency of both the HFSC decoding and Fano decoding. It is a
N+
multiplicity of the SC decoding complexity, i.e., Φ = ηN log N, where η ∈ is referred
2
as the normalized complexity factor. For both the HFSC decoding and Fano decoding, once Φ
is reached, the SC decoding will be switched to in estimating the remaining information bits.
This prevents the decoding from lingering over the decoding tree, rationalizing the otherwise
| unlimited |     | decoding |     | computation. |     |     |     |     |     |     |     |
| --------- | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Fig. 5 shows the decoding frame error rate (FER) and complexity performance of different
coding schemes with N = 128 and K = 64. For yielding a good FER performance under the
HFSC decoding, optional parameters (N ,K ) = (96,48), (64,32) and (32,16) are chosen for
|     |     |     |     |     |     |     | c   | c   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MPAC codes, which are obtained from our numerical study in [35]. A decoding computation
threshold of η = 128 is also provided for the HFSC decoding and Fano decoding as in [35].

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 14
|     | 100 |     |     | 35  |     |     |
| --- | --- | --- | --- | --- | --- | --- |
30
10−1
 ytixelpmoC dezilamroN 25
10−2
20
REF
15
10−3
10
10−4
5
|     | 10−5 |                          |          | 0                        |          |            |
| --- | ---- | ------------------------ | -------- | ------------------------ | -------- | ---------- |
|     |      | 1 2                      | 3 4      | 5 1                      | 2 3      | 4 5        |
|     |      |                          | SNR (dB) |                          | SNR (dB) |            |
|     |      |    MPAC-(96, 48), HFSC   |          |        PAC, Fano         |          |            |
|     |      |    MPAC-(64, 32), HFSC   |          |         CRC-polar, SCL   |          |            |
|     |      |    MPAC-(32, 16), HFSC   |          |       polar, SC          |          |            |
Fig.5. PerformancecomparisonofMPACcodes,PACcodes,polarcodesandCRC-polarcodes,whereN =128andK =64.
It can be seen that the MPAC-(96,48) code can slightly outperform the (128,64) PAC code.
Furthermore, when compared with the CRC-polar code, the MPAC-(96,48) code achieves 0.25
dB power gain at the FER of 10−4 with a smaller complexity. It can also be seen that the MPAC-
(64,32) code performs nearly the same as the (128,64) PAC code, but with a lower decoding
complexity. Moreover, both the MPAC-(96,48) code and MPAC-(64,32) code can outperform
the MPAC-(32,16) code, validating the effectiveness of the convolutional parameters which are
listedin[35].Itimplysthatasufficientportionofinformationbitsneedstoundergoconvolutional
| transform | to achieve | a good | decoding performance. |          |     |     |
| --------- | ---------- | ------ | --------------------- | -------- | --- | --- |
|           |            |        | IV. MWD               | ANALYSIS |     |     |
This section analyzes the MWD of MPAC codes, including the formation of the MWCs and
their coset-wise enumeration. Compared with the existing SCL-based enumeration [34], it has
a much lower computational complexity. More importantly, this analysis provides a new metric
for designing MPAC codes, especially in determining the convolutional transform parameters
(N ,K ). We first revisit the formation of MWCs for polar codes. By considering the impact
c c
of convolutional transform and frozen bits, we present the general characterization of row

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     | 15  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
combinations of the MWCs in MPAC codes together with the validation approach. Based on
this, an efficient algorithm is proposed to determine the number of MWCs.
| A. Formation |     | of the MWCs | for Polar | Codes |     |     |     |     |     |
| ------------ | --- | ----------- | --------- | ----- | --- | --- | --- | --- | --- |
The set theoretical approach [20] in analyzing the MWD of polar codes is applied to show
the intrinsic structure to the proposed MPAC codes. By enumerating all the combinations, the
formation and the number of MWCs can be obtained. The approach can be used to analyze
polar like codes with the partial order property, which will be defined as follows.
Definition II (Partial Order [39]). Given subchannel indices i,j ∈ [0,N−1], the partial order
| i ⪯ j holds | if     | they satisfy | one of     | the three | conditions: |          |       |      |     |
| ----------- | ------ | ------------ | ---------- | --------- | ----------- | -------- | ----- | ---- | --- |
| S           | ⊆ S ;  |              |            |           |             |          |       |      |     |
| • i         | j      |              |            |           |             |          |       |      |     |
| • S         | = (S   | \{a})∪{b}    | for a pair | of a      | ∈ S ,b      | ∈/ S and | a <   | b;   |     |
| j           | i      |              |            |           | i           | i        |       |      |     |
| • There     | exists | an index     | k ∈ [0,N   | −1]       | satisfying  | i ⪯ k    | and k | ⪯ j. |     |
Note that there may exist some pairs of indices that neither of the index precedes the other
under the partial order. For this, the following Definition III is needed.
Definition III (Partial Order Property [20]). A set I ⊆ [0,N −1] is said to satisfy the partial
|     |     |     |     |     |     | ic Ic |     |     | ic. |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
order property if none of the index pair i ∈ I, ∈ satisfies the partial order i ⪯ Or
|               |     |      | ⪯̸ ic     |         |     | ic    | Ic. |     |     |
| ------------- | --- | ---- | --------- | ------- | --- | ----- | --- | --- | --- |
| equivalently, | we  | have | i for any | indices | i ∈ | I and | ∈   |     |     |
I
With the above definition, if a set satisfies the partial order property, it can be found that
all the indices in I compose a chain of partial orders. Moreover, for every pair of indices i ∈ I
| and j ∈ | [0,N | −1], if | i ⪯ j, j ∈ I. |     |     |     |     |     |     |
| ------- | ---- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
Given a polar code C(I) with information set I that satisfies the partial order property, the
analysis of its MWCs starts from dividing the code C(I) into |I| disjoint cosets.
Definition IV (Polar Coset [20]). Given an N-dimensional polar transform G and an infor-
p
| mation | set I ∈ | [0,N −1], | the coset | is defined | by  |     |     |          |     |
| ------ | ------- | --------- | --------- | ---------- | --- | --- | --- | -------- | --- |
|        |         |           |           | (cid:40)   |     |     |     | (cid:41) |     |
(cid:77)
|     |     |     | C (I) = | g ⊕ | g   | | H ⊆ | I \[0,i] | ,   | (16) |
| --- | --- | --- | ------- | --- | --- | ----- | -------- | --- | ---- |
|     |     |     | i       | i   | h   |       |          |     |      |
h∈H
|           | i-th |        | G g         |          |               |     |     |     |     |
| --------- | ---- | ------ | ----------- | -------- | ------------- | --- | --- | --- | --- |
| where the |      | row of | p , i.e., i | , is the | coset leader. |     |     |     |     |
In other words, coset C (I) is the set of codewords generated by C(I \ [0,i − 1]), where
i
C(I \ [0,i − 1]) is the subcode of polar code C(I). The following Lemma 1 indicates that

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     |     | 16  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the Hamming weight of coset leader g , where i ∈ I is a lower bound for the weight of any
i
| codeword | in the | coset | C (I). |     |     |     |     |     |     |     |     |
| -------- | ------ | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
i
Lemma 1 ([20], [40]). For any i ∈ [0,N −1] and H ⊆ [i+1,N −1], we have
(cid:77)
|     |     |     |     |     | w(g | ⊕   | g ) ≥ w(g | ).  |     |     | (17) |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ---- |
|     |     |     |     |     | i   |     | h         | i   |     |     |      |
h∈H
By comparing the row weights of all coset leaders, the minimum distance of the polar code
| C(I) can | be obtained | by  |     |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|          |             |     |     | d   | =   | ω   |     |     |     |     |     |
|          |             |     |     |     | min | min |     |     |     |     |     |
(18)
|     |     |     |     |     | =   | min({w(g | ) | i | ∈ I}). |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | ------ | --- | --- | --- |
i
Note that the weight of row g can be easily calculated by w(g ) = 2|Si|, where i ∈ [0,N−1].
|     |     |     |     | i   |     |     |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Further let A (I) and A (I) denote the number of MWCs in polar code C(I) and coset
|     | ωmin |     | i,ωmin |     |     |     |     |     |     |     |     |
| --- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
C (I), respectively. Based on Lemma 1, we have A (I) = 0 for every index i ∈ {j ∈ I |
| i   |     |     |     |     |     |     | i,ωmin |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
w(g ) > ω }. Consequently, only the cosets with their leaders’ weight being equal to ω
| j   | min |     |     |     |     |     |     |     |     |     | min |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
need to be considered. All linear combinations that form the MWCs in coset C (I), where i ∈ I
i
and w(g ) = ω , can be explicitly characterized by the following Lemma 2.
i min
Lemma 2 ([20], [32]). Given an information set I ⊆ [0,N −1] that satisfies the partial order
|     |     |     |     | i   | ∈ I | w(g | ) = ω |     |     | C   | (I) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
property and coset leader index with i min , the MWCs in polar coset i can
| be formed | by  | rows as |     |     |          |     |          |       |     |     |      |
| --------- | --- | ------- | --- | --- | -------- | --- | -------- | ----- | --- | --- | ---- |
|           |     |         |     |     | (cid:77) |     | (cid:77) |       |     |     |      |
|           |     |         |     | w(g | ⊕        | g ⊕ | g        | ) = ω | ,   |     | (19) |
|           |     |         |     | i   |          | j   |          | m     | min |     |      |
|           |     |         |     |     | j∈J      |     | m∈M(J)   |       |     |     |      |
where the rows with index defined in sets J ⊆ K and M(J) are called the core rows and the
i
balancing rows, respectively. Moreover, the sets K and M(J) can be constructed by the index
i
| of i and | the so | called | M-construction, |     | respectively. |     |     |     |     |     |     |
| -------- | ------ | ------ | --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
For an index i ∈ [0,N −1], the set K captures every index j ∈ [i+1,N −1] that satisfies
i
| w(g ) | ≥ w(g | ⊕g ) = | w(g ). | Equivalently, |          | set | K is defined | as   |       |     |      |
| ----- | ----- | ------ | ------ | ------------- | -------- | --- | ------------ | ---- | ----- | --- | ---- |
| j     | i     | j      | i      |               |          |     | i            |      |       |     |      |
|       |       |        | K      | ≜ {j          | ∈ [i+1,N |     | −1] | |S     | \S | | = 1}. |     | (20) |
|       |       |        |        | i             |          |     |              | j i  |       |     |      |
This set can be determined by applying the addition operation and the left swap operation on
| binary | vector bin(i) | as  | in [20]. |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Given a set J ⊆ K , the corresponding balancing set M(J) can be constructed using the
i

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     | 17  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
M-construction [20]. However, the M-construction is only conducted when all the indices of
set J are known. It is more efficient to construct set M(J) through an ongoing approach [41]
| which enlists | the indices | of set | J one-by-one. |     |     |     |
| ------------- | ----------- | ------ | ------------- | --- | --- | --- |
The partial order property of information set I promises both sets K and M(J) are disjoint
i
subsets of I∩[i+1,N −1]. That says K ⊆ I∩[i+1,N −1], M(J) ⊆ I∩[i+1,N −1] and
i
| K ∩M(J) | = ∅. |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- |
i
| As a | result, the value | of uN−1 | can be controlled | based | on  |     |
| ---- | ----------------- | ------- | ----------------- | ----- | --- | --- |
0

|     |     |  1, | if x ∈ {i}∪J | ∪M(J); |     |      |
| --- | --- | ----- | ------------ | ------ | --- | ---- |
|     |     | u =   |              |        |     | (21) |
x
|     |     |  0, | if x ∈ [0,N | −1]\({i}∪J | ∪M(J)). |     |
| --- | --- | ----- | ----------- | ---------- | ------- | --- |
The corresponding MWCs can be further obtained by polar encoding as in (3). Consequently,
the number of MWCs in C(I) can be calculated as defined by the following Corollary 3.
Corollary 3 ([20]). Given an information set I ⊆ [0,N − 1] that satisfies the partial order
| property, | the number | of MWCs | of C (I) is |     |     |     |
| --------- | ---------- | ------- | ----------- | --- | --- | --- |
i
(cid:88)
|     |     |     | A (I) = |     | 2|Ki|. | (22) |
| --- | --- | --- | ------- | --- | ------ | ---- |
ωmin
i∈I: w(gi)=ωmin
| B. Formation | of the | MWCs for | MPAC Codes |     |     |     |
| ------------ | ------ | -------- | ---------- | --- | --- | --- |
The above mentioned characterization of row combinations of MWCs for polar codes shows
that it is important to define the index sets that correspond to the support of vector uN−1.
0
Therefore, in forming the MWCs of MPAC codes, the index sets I , F , I and F . shall be
c c p p
characterized. For our description convenience, they are also illustrated in Fig. 6.
The general information set I = I ∪ I and frozen set F = F ∪F are further obtained.
c p c p
The rate profiling I ensures the subchannel indexes i with higher w(g ) are chosen, yielding a
i
higher minimum row weights, i.e., min({w(g ) | i ∈ I}, for MPAC codes.
i
Ascending mean LLRs
AscendingiRMPorderings
| Fig. 6. Index | sets of N subchannels | under | MPAC coding. |     |     |     |
| ------------- | --------------------- | ----- | ------------ | --- | --- | --- |

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     |     | 18  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
It is worth mentioning that the method proposed for MWCs enumeration of MPAC code can
be realized through checking the legality of every MWC enumeration. As a result, their MWCs
can be formed by (19) and further be enumerated by the row combination manner as (21). In
other words, we need to set u = 1 for every x ∈ {i}∪J∪M(J). However, it has been observed
x
in [33] that the outer convolutional transform with the frozen bits as inputs generates constraint
on the values of some u . In the proposed MPAC codes, uN−1 = (u , u , u ), where the
|     |     |     |     | x   |     |     |     | 0   |     | Ic∪Fc Ip Fp |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
values of u , u and u are the output vector of convolutional transform, information bits
|     |     | Ic∪Fc | Ip  |     | Fp  |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and frozen bits, respectively. In the following, we will discuss the influence of convolutional
transform and the frozen bits on the value of u , which are characterized in three cases.
x
Case I: When x ∈ I ∪ F , u is the convolutional output, which is determined by u =
|     |     |     |     | c   | c   | x   |     |     |     |     | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:76)t
g s , or equivalently, by applying conv1b(·), where k = 𭟋 (x). Considering the
| j=0 | j   | k−j |     |     |     |     |     |     |     | Ic∪Fc |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
(cid:76)t
constraint of t previous convolutional inputs, we have u = V ⊕s , where V = g s .
|     |     |     |     |     |     |     |     | x   |     | k   | j k−j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
j=1
Since the value of s is determined by either an information bit or a frozen bit, we consider the
k
| corresponding |     |     | subcases | of  | x ∈ I | and x ∈ F . |     |     |     |     |     |
| ------------- | --- | --- | -------- | --- | ----- | ----------- | --- | --- | --- | --- | --- |
|               |     |     |          |     |       | c c         |     |     |     |     |     |
Case I-A: When x ∈ I , s = 0 or 1. Hence, we can obtain u = 1 by choosing s
|               |     |      |      |     | c   | k   |     |     |     | x   | k   |
| ------------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| appropriately |     | such | that |     |     |     |     |     |     |     |     |

|     |     |     |     |     |     |  1, | if V | = 0; |     |     |      |
| --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | --- | --- | ---- |
|     |     |     |     |     |     | s =  |      |      |     |     | (23) |
k
|              |     |     |      |        |      |  0,          | if V     | = 1. |     |     |     |
| ------------ | --- | --- | ---- | ------ | ---- | ------------- | -------- | ---- | --- | --- | --- |
| In obtaining |     | u   | = 0, | we can | take | the opposites | of (23). |      |     |     |     |
x
Case I-B: When x ∈ F , s is determined by a frozen bit, and let s = 0. Consequently, u
|     |     |     |     |     | c k |     |     |     |     | k   | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is only determined by the previous input constraint, i.e., u = V. If the previous inputs cause
x
| V = | 1,  |      | u   | = 1.       |     | u = 0. |     |     |     |     |     |
| --- | --- | ---- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
|     | we  | have | x   | Otherwise, |     | x      |     |     |     |     |     |
Case II: When x ∈ I , u is determined by an information bit, u = 0 or 1.
|     |     |     |     | p   | x   |     |     |     |     | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Case III: When x ∈ F , u is directly determined by a frozen bit and u = 0.
|     |     |     |     |     | p x |     |     |     |     | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
It can be seen that in Case I-A and Case I-B, we have no control on the value of u . Based
x
on the setting of uN−1 in obtaining the MWCs as in (21), we focus on the value of u that is
|     |     |     | 0   |     |     |     |     |     |     |     | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
only determined by convolutional operation, where x ∈ (F ∪F )∩[i+1,N−1]. Since in Case
|       |     |     |     |     |     |           |     | c   | p   |     |     |
| ----- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
| III u | =   | 0,  |     |     |     | Case I-B. |     |     |     | F ˜ |     |
x we turn to focus on Consequently, the index set c is defined as
˜
|     |     |     |     |     | F ≜ | {f ∈ F ∩[i+1,N |     | −1]|u | = 1}. |     | (24) |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ----- | --- | ---- |
|     |     |     |     |     | c   | c              |     | f     |       |     |      |
|     |     |     | ˜   |     |     | (cid:76)       |     |       |       |     |      |
ThegenerationofF impliesthatanotherterm g willbeincludedintherowcombination
|     |     |     | c   |     |     |     | f∈F˜ c | f   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |          |     |        |                 |     |     |     |     | 19  |
| ----------------------------------------------- | -------- | --- | ------ | --------------- | --- | --- | --- | --- | --- |
| of (19).                                        | A subset | of  | F ˜ is | further defined | as  |     |     |     |     |
c
˜
|     |     |     |     | F = | {f ∈ F | | |S \S | | = 1}. |     | (25) |
| --- | --- | --- | --- | --- | -------- | ----- | ------- | --- | ---- |
|     |     |     |     | J   | c        | f     | i       |     |      |
(cid:76)
Remark 4. The inclusion of the additional term g in the MWC row combination of
f∈F˜ c f
(19) does not reduce the minimum distance of an MPAC code. This is due to the fact that for any
˜
f ∈ F , the enlisted row g is not the coset leader of any coset in the code. Based on Lemma
| c   |     |     |     | f   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1, since the general information set I = I ∪I remains unchanged, the minimum distance of
c p
| the MPAC | code | is maintained |     | as      |     |     |     |     |     |
| -------- | ---- | ------------- | --- | ------- | --- | --- | --- | --- | --- |
|          |      |               | d   | = ω     |     |     |     |     |     |
|          |      |               |     | min min |     |     |     |     |     |
(26)
|     |     |     |     | = min({w(g | ) | i ∈ | I and | I = | I ∪I }). |     |
| --- | --- | --- | --- | ---------- | ------- | ----- | --- | -------- | --- |
|     |     |     |     |            | i       |       |     | c p      |     |
Please note that the above property does not always hold for all MPAC codes. But in this
work, we only consider the MPAC codes that yield (26). Theorem 5 further characterizes the
more general row combination in obtaining the MWCs of an MPAC code.
Theorem 5. Given an MPAC code that is defined by the subchannel index sets I , F , I and
c c p
F where index i is chosen such that w(g ) = ω , the minimum weight codewords in coset
| p   |     |     |     |     | i   | min |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C (I)
| i can | be  | further | redefined | based    | on (25) as |          |     |       |      |
| ----- | --- | ------- | --------- | -------- | ---------- | -------- | --- | ----- | ---- |
|       |     |         |           | (cid:77) |            | (cid:77) |     |       |      |
|       |     |         |           | w(g ⊕    | g ⊕        |          | g ) | = ω , | (27) |
|       |     |         |           | i        | j          |          | m   | min   |      |
j∈J∪FJ
m∈M(J∪FJ)
where J ⊆ K and M(J) are constructed as in Lemma 2. The set F can be represented based
|         |          | i   |      |             |     |     |         | J             |     |
| ------- | -------- | --- | ---- | ----------- | --- | --- | ------- | ------------- | --- |
| on (24) | and (25) | as  |      |             |     |     |         |               |     |
|         |          | F   | = {f | ∈ F ∩[i+1,N | −1] | | u | = 1 and | |S \S | = 1}. |     |
|         |          | J   |      | c           |     | f   |         | f i           |     |
Proof: It is a generalization of Lemma 2. The main difference between MWC generation of
polar codes and that of MPAC codes lies in the index set F . It is caused by the convolutional
J
constraints and the frozen bits as in Case I-B. Furthermore, since the indices of set F have
J
the same property as those of the set J ⊆ K , we can replace the sets J and M(J) of (19)
i
by J ∪ F and M(J ∪ F ), respectively. This immediately leads to (27). In the following
|     | J   |     |     | J   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
subsection IV-C, we will propose an efficient approach to yield sets J and F , which can be
J
| enumerated | one | by one | as  | in Algorithm | 3   |     |     |     |     |
| ---------- | --- | ------ | --- | ------------ | --- | --- | --- | --- | --- |
Fig. 7 illustrates Venn diagram of the associated index sets in characterizing the MWCs of

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     | 20  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MPAC codes. In particular, the index sets of rows that form the MWCs are denoted by the red
| boxes.    | We further   | combine | these | index | sets   | into | the set |       |     |      |
| --------- | ------------ | ------- | ----- | ----- | ------ | ---- | ------- | ----- | --- | ---- |
|           |              |         | U (J) | =     | {i}∪(J | ∪F   | )∪M(J   | ∪F ), |     | (28) |
|           |              |         | i     |       |        |      | J       | J     |     |      |
| such that | in obtaining | the     | MWC,  | it    | should | be   |         |       |     |      |

|     |     |     |     |  1 | if  | x ∈ | U (J); |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ------ | --- | --- | --- |
i
|     |     |     | u   | =   |     |     |     |     |     | (29) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
x
|     |     |     |     |  0 | if  | x ∈ | [0,N −1]\U | (J). |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---------- | ---- | --- | --- |
i
| Fig. 7. Venn | diagram of | the associated |     | index sets | for | indices | [i+1,N −1]. |     |     |     |
| ------------ | ---------- | -------------- | --- | ---------- | --- | ------- | ----------- | --- | --- | --- |
Therefore, the number of MWCs of the proposed MPAC codes can be determined. However,
as discussed in Case I-B and Case III, for f ∈ F ∪F , we have no control on the value of
|     |     |     |     |     |     |     | c p |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
u . If eq. (29) cannot be ensured, the corresponding MWC cannot be formed. The following
f
subsection introduces the verification of the MWCs for MPAC codes and determines their exact
number.
| C. Verification | of  | the MWCs | for | MPAC | Codes |     |     |     |     |     |
| --------------- | --- | -------- | --- | ---- | ----- | --- | --- | --- | --- | --- |
Based on Corollary 3, the number of MWCs characterized in (27) can be obtained by enumer-
ating all the possible index sets U (J) that are defined as in (28). Since the index set M(J∪F )
|     |     |     |     | i   |     |     |     |     |     | J   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is constructed based on set J ∪F , all possible index sets J ∪F need to be found [33].
|     |     |     |     | J   |     |     |     | J   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma 6. The number of all possible index sets J ∪F is equal to 2|Ki|.
J
is2|Ki|.SincesetF
| Proof: | ThenumberofallpossibleindexsetsJ |     |     |     |     |     | ⊆ K |     | isgeneratedbased |     |
| ------ | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
|        |                                  |     |     |     |     |     | i   |     | J                |     |
on the convolutional outputs, it is related to the previous convolutional inputs. When obtaining

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     |     | 21  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the MWCs of an MPAC code, the convolutional inputs are determined by (29). In other words,
F depends on set J. Therefore, the number of all possible sets J ∪F is equal to that of all
| J        |      |          |        |     |     |     |     |     |     | J   |     |
| -------- | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| possible | sets | J, i.e., | 2|Ki|. |     |     |     |     |     |     |     |     |
(cid:76)t
Combining both Case I-B and Case III of Section IV-B, u = g s = V and
|     |     |     |     |     |     |     |     |     |     | x j=1 j k−j |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
k = 𭟋 (x) for x ∈ F and u = 0 for x ∈ F , respectively. Consequently, for some
|     | Ic∪Fc |     |     | c   | x   |     |     | p   |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
J ⊆ K , the value of u and x ∈ F ∪F , cannot be chosen to ensure supp(uN−1) = U (J).
|     | i   |     |     | x   | c   | p   |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
This results in some codewords that are formed as (27) cannot be generated by the MPAC
| encoding. |     | For better | representation, |          | let   | us further |     | define   |     |         |     |
| --------- | --- | ---------- | --------------- | -------- | ----- | ---------- | --- | -------- | --- | ------- | --- |
|           |     |            | E1 =            | {(F ˜ \F | )\((F | ∩[i+1,N    |     | −1])∩M(J |     | ∪F ))}, |     |
|           |     |            |                 | c        | J     | c          |     |          |     | J       |     |
J
˜
|     |     |     | E2  | = {((F | ∩[i+1,N     |     | −1])∩M(J |     | ∪F  | ))\F |     |
| --- | --- | --- | --- | ------ | ----------- | --- | -------- | --- | --- | ---- | --- |
|     |     |     | J   |        | c           |     |          |     |     | J c  |     |
|     |     |     |     | E3 =   | {(F ∩[i+1,N |     | −1])∩M(J |     | ∪F  | )}.  |     |
|     |     |     |     |        | p           |     |          |     |     | J    |     |
J
For a more illustrative presentation, the index sets E1, E2 and E3 are marked by the green,
|     |     |     |     |     |     |     |     | J   | J   | J   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
yellow and blue shades in Fig 7, respectively. Considering the contradiction of supp(uN−1) ̸=
0
U (J), there are three criteria that can be utilized to validate the case in which the characterized
i
codewords cannot be generated. For every J ⊆ K , when x ∈ F ∪F , the value of u needs
|           |         |         |          |          |     |     |     | i   |     | c p | x   |
| --------- | ------- | ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| to be     | checked | as      | follows. |          |     |     |     |     |     |     |     |
| Criterion |         | 1 (C1): | u        | = 1, but | x ∈ | E1; |     |     |     |     |     |
|           |         |         | x        |          |     | J   |     |     |     |     |     |
| Criterion |         | 2 (C2): | u        | = 0, but | x ∈ | E2; |     |     |     |     |     |
|           |         |         | x        |          |     | J   |     |     |     |     |     |
| Criterion |         | 3 (C3): | u        | = 0, but | x ∈ | E3. |     |     |     |     |     |
|           |         |         | x        |          |     | J   |     |     |     |     |     |
In C1, since x ∈ E1, u should be set as 0 such that (29) is met. However, we get u = 1
|     |     |     |     | x   |     |     |     |     |     |     | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
J
under the constraints of Case I-B, which implies the undesired row g has been included in
x
the row combinations of (27). It prevents formation of the corresponding MWC. In C2, since
x ∈ E2, u should be set as 1. However, under the same constraints in Case I-B, we get u = 0,
|     | J   | x   |     |     |     |     |     |     |     |     | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resulting in the desired row g being excluded from the row combinations of (27). C3 also
x
checks the case in which the characterized MWCs cannot be generated due to the absence of
some specific rows. Note that a missing row is caused by the constraint of the corresponding
x ∈ E3.
frozen bit in Case III and its index With the above three criteria, the exact number of
J
| the | MWCs | of an | MPAC | code | is characterized |     | as in | Theorem | 7.  |     |     |
| --- | ---- | ----- | ---- | ---- | ---------------- | --- | ----- | ------- | --- | --- | --- |
Theorem 7. With the subchannel index sets I , F , I and F of MPAC codes, the number
|     |     |     |     |     |     |     | c   | c   | p   | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |      |          |       |     |          |      |     |     |     |     |     | 22  |
| ----------------------------------------------- | ---- | -------- | ----- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
| of                                              | MWCs | in coset | C (I) | of  | the MPAC | code | is  |     |     |     |     |     |
i
|     |     |     |     |     |     | AMPAC | =   | 2|Ki| | −X, |     |     | (30) |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | ---- |
i,ωmin
where X is the number of the MWCs that are characterized in Theorem 5, but cannot be formed.
| It  | is called | the | MWC | number | deficit. |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
Proof: Based on Lemma 6, the number of MWCs in C (I) of an MPAC code has an upper
i
boundof2|Ki|.TheupperboundisachievedonlyifforallJ ⊆ K ,thecorrespondingvectoruN−1
|     |     |     |     |     |     |     |     |     |     | i   |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
satisfiessupp(uN−1) = U (J).AssumeX isthenumberofthesetsJ thatsupp(uN−1) ̸= U (J),
|     |     |       |          | i   |     |     |            |     |     |     |     | i   |
| --- | --- | ----- | -------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|     |     |       | 0        |     |     |     |            |     |     |     | 0   |     |
|     |     | AMPAC | 2|Ki|−X, |     |     |     | [0,2|Ki|]. |     |     |     |     |     |
we have = where X ∈ The value of X is obtained by assessing the
i,ωmin
| above | mentioned |     | criteria | C1, | C2  | and C3. |     |     |     |     |     |     |
| ----- | --------- | --- | -------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Recalling (24), (25) and the M-construction, for every index f ∈ F ˜ \F , M(J ∪F ) has
|     |      |          |     |       |        |             |         |        |       | c             | J   | J   |
| --- | ---- | -------- | --- | ----- | ------ | ----------- | ------- | ------ | ----- | ------------- | --- | --- |
| the | same | property | of  | |S \S | | > 1. | Let us      | further | define | set   |               |     |     |
|     |      |          |     | f     | i      |             |         |        |       |               |     |     |
|     |      |          | F∗  | = {f  | ∈ (F   | ∪F )∩[i+1,N |         |        | −1] | | |S \S | > 1}, |     |     |
|     |      |          |     |       |        | c p         |         |        |       | f i           |     |     |
where E1 ∪E2 ∪E3 ⊆ F∗. The following Remark 8 reveals that if F∗ = ∅, the value of X can
|     |     | J J | J   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2|Ki|
| be  | set as | 0 without | enumerating |     | the |     | characterized |     | MWCs. |     |     |     |
| --- | ------ | --------- | ----------- | --- | --- | --- | ------------- | --- | ----- | --- | --- | --- |
Remark 8. Since E1 ∪E2 ∪E3 ⊆ F∗, if one of the criteria C1, C2 and C3 is met, there exists
|     |     |     | J   | J   | J   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | F∗. | F∗  |     |     |     |     |     |
at least an index f that satisfies f ∈ If = ∅, none of the three criteria can be met and
F∗
X = 0. Note that = ∅ if and only if {(F ∪F )∩[i+1,N −1]} = ∅ or |S \S | = 1 for
|     |     |     |     |     |     |     | c   | p   |     |     | f i |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
all f ∈ {(F ∪F )∩[i+1,N −1]}. The former case implies that every set U (J) is a subset
|     |     | c   | p   |     |     |     |     |     |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of {(I ∪I )∩[i,N −1]}, which is attainable. For the latter, E1 = E2 = E3 = ∅. None of the
|       | c     | p   |            |      |     |        |     |        |     | J J | J   |     |
| ----- | ----- | --- | ---------- | ---- | --- | ------ | --- | ------ | --- | --- | --- | --- |
| above | cases | is  | consistent | with | C1, | C2 and | C3. | Hence, | X = | 0.  |     |     |
Except the above mentioned case, counting the number of MWCs in coset C (I), i.e., AMPAC,
|     |     |     |     |     |     |     |     |     |     |     | i   | i,ωmin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
can be performed through enumerating all the 2|Ki| index sets U (J) and checking the three
i
criteria for related vectors uN−1. Based on Theorem 7, we have AMPAC = 2|Ki|−X. An ongoing
|     |     |     |     | 0   |     |     |     |     |     | i,ωmin |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
approach is applied to construct U (J). The values of u with x ∈ [i,N−1] can then be checked
|     |     |     |     |     | i   |     |     |     | x   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AMPAC
such that the values of X and can be determined. This is summarized as in Algorithm
i,ωmin
3, which evolves from Algorithm 1 of [41]. However, when focusing on the MPAC codes, the
additional cases should be taken into account. During the bit-by-bit acquisition of u for each
x
J ⊆ K , we only record the updates of the shift register states S. Notably, state S is updated
i

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 23
only at bits u such that x ∈ I ∪F . The ongoing approach initializes X = 0 and proceeds to
|     | x   | c   | c   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
enumerate u for x = i to N − 1. According to the reached index of x, there are three cases
x
| summarized | as follows. |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
When reaching an index x ∈ I or x ∈ I , if x ∈ J, let u = 1 and partially construct
| •   |       |     | c   | p   |     |     | x         |     |
| --- | ----- | --- | --- | --- | --- | --- | --------- | --- |
| M(J | ∪ F ) |     | M   | ˜   |     |     | addToM(·) |     |
J that is denoted as , using the subroutine that was defined in
Algorithm 2 of [41]. Index x is also needed to add to the partially formed J, which is
˜
denoted as J. In particular, when x ∈ I , the value of u can be determined based on
|     |     |     |     | c   |     |     | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(29). Furthermore, the input bit s is determined by (9) and the state S is updated by
k
| conv1b(s | ,S,gt), | where | k = 𭟋 | (x). |     |     |     |     |
| -------- | ------- | ----- | ----- | ---- | --- | --- | --- | --- |
|          | k       |       | Ic∪Fc |      |     |     |     |     |
0
When reaching an index x ∈ F as in Case I-B, u is determined by the previous
| •   |     |     |     | c   |     | x   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
convolutionalinputs,i.e.,[u ,S] ← conv1b(0,S,gt).IfeithercriteriaC1orC2issatisfied,
x
0
X is increased by one. In particular, if x ∈ F , the operations for index x ∈ J will be
J
also taken.
It should be mentioned that the subroutine addToM(·) does not distinguish the indices in
| sets J | and F . |     |     |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
J
When reaching an index x ∈ F as in Case III, u is frozen as 0. If criterion C3 is satisfied,
| •         |           |         | p   |     | x   |     |     |     |
| --------- | --------- | ------- | --- | --- | --- | --- | --- | --- |
| X is also | increased | by one. |     |     |     |     |     |     |
With the above mentioned procedure, X can be determined and so can AMPAC be obtained.
i,ωmin
For every C (I), complexity of the coset-wise enumeration is O(2|Ki| ·(N −i)). Moreover, by
i
introducing a factor ζ = max{F∗}, the computational complexity can be reduced to O(2|K ζ| ·
i
(ζ−i)). It follows a similar strategy that was introduced in [41]. Based on Algorithm 3, the set
uN−1
K (in line 4 of Algorithm 3) and the vector (in line 10 of Algorithm 3) degenerate into
| i   |     |     |     | i   |     |     |     |               |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
| ζ   |     |     | uζ  |     |     |     |     | ζ|(2|K ζ|−X). |
set K = {j ∈ K | j < ζ} and vector , respectively. As a result, AM P A C = 2|Ki\K i i
| i   | i   |     |     | i   |     |     | i,ω |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
m in
Alternatively, we can also employ an SCL decoder with a sufficiently large decoding output
list size L, which exhibits a computational complexity of O(L·N log N) for enumerating the
2
MWCs [34]. But the SCL-based enumeration method is conducted when the all-zero codeword is
transmitted at a very high SNR, e.g., 20 dB. Recalling Theorem 7, the list size should satisfy L ≥
2|Ki|
for enumerating all the MWCs in the coset C (I). Hence, computational complexity of this
i
|     | O(2|Ki|·N |     |     | 2|K ζ|·(ζ−i) |     | 2|Ki|·N |     |     |
| --- | --------- | --- | --- | ------------ | --- | ------- | --- | --- |
method is at least log N). Since i ≪ log N, the proposed coset-
|     |     |     | 2   |     |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
wise enumeration method is much simpler than the existing SCL-based enumeration method.

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |     |     |     |     |     |     |     |     |     | 24  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Algorithm 3: Enumeration of MWCs in coset C (I) of MPAC Code, i.e. AMPAC
|        |     |     |         |      |     |     |     | i   |     |     | i,ωmin |     |
| ------ | --- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | ------ | --- |
|        | i,  | I F | I       | F S, | gt; |     |     |     |     |     |        |     |
| Input: |     | c , | c , p , | p ,  |     |     |     |     |     |     |        |     |
0
AMPAC;
Output:
i,ωmin
| Initialize |     | X =  | 0 and | construct | sets | K   | and | F∗; |     |     |        |     |
| ---------- | --- | ---- | ----- | --------- | ---- | --- | --- | --- | --- | --- | ------ | --- |
| 1          |     |      |       |           |      |     | i   |     |     |     |        |     |
| If F∗      | = ∅ | then |       |           |      |     |     |     |     | //  | Remark | 8   |
2
|     | Return | AM  | P A C = | 2|Ki|; |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| 3   |        | i,ω |         |        |     |     |     |     |     |     |     |     |
m in
| 4 For | every | J ⊆ | K do |     |     |     |     |     |     |     |     |     |
| ----- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
˜ ˜
| 5   | Set J,M | ←      | ∅;       |     |     |     |     |        |     |     |     |     |
| --- | ------- | ------ | -------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
|     | uN      | −1     | 0N −1,sN | c−1 | 0N  | c−1 |     | 0t −1; |     |     |     |     |
| 6   | Set     | =      |          |     | =   | and | S   | =      |     |     |     |     |
|     |         | 0      | 0        | 0   | 0   |     |     | 0      |     |     |     |     |
| 7   | If i ∈  | I then |          |     |     |     |     |        |     |     |     |     |
c
|     | Compute |       | k =      | 𭟋     | (i) and | set | s = | 1;  |     |     |     |     |
| --- | ------- | ----- | -------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
| 8   |         |       |          | Ic∪Fc |         |     | k   |     |     |     |     |     |
|     | [u      | ,S] ← | conv1b(s |       | ,S,gt); |     |     |     |     |     |     |     |
| 9   |         | i     |          |       | k       |     |     |     |     |     |     |     |
0
|     | For x | = i+1 | to  | N −1 | do  |     |     |     |     |     |     |     |
| --- | ----- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
10
| 11  | If  | x ∈ I | or x | ∈ I | then |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |       | c    | p   |      |     |     |     |     |     |     |     |
// for
| 12  |     | If x | ∈ J then |              |       |      |     |     |     |      | x ∈ I | ∪I  |
| --- | --- | ---- | -------- | ------------ | ----- | ---- | --- | --- | --- | ---- | ----- | --- |
|     |     |      |          |              |       |      |     |     |     |      |       | c p |
|     |     |      | ˜        | addToM(i,x,J |       | ˜    | ˜   |     | //  | [41, | Alg.  | 2]  |
| 13  |     |      | M ←      |              |       | ,M   | );  |     |     |      |       |     |
|     |     |      | ˜        | ˜            |       |      |     |     |     |      |       |     |
| 14  |     |      | J ← J    | ∪{x};        |       |      |     |     |     |      |       |     |
|     |     | If x | ∈ I      | then         |       |      |     |     |     |      |       |     |
| 15  |     |      | c        |              |       |      |     |     |     |      |       |     |
|     |     |      | Compute  | k =          | 𭟋     | (x); |     |     |     |      |       |     |
| 16  |     |      |          |              | Ic∪Fc |      |     |     |     |      |       |     |
|     |     |      | If x ∈   | J then       |       |      |     |     |     |      |       |     |
17
| 18  |     |     | Set | u = | 1;  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x
Else
19
|     |     |     | If      | x ∈ M ˜  | then     | set  | u =     | 1;  |     |     |     |     |
| --- | --- | --- | ------- | -------- | -------- | ---- | ------- | --- | --- | --- | --- | --- |
| 20  |     |     |         |          |          |      | x       |     |     |     |     |     |
|     |     |     | If      | x ∈/ M ˜ | then     | set  | u =     | 0;  |     |     |     |     |
| 21  |     |     |         |          |          |      | x       |     |     |     |     |     |
|     |     |     | Compute | s        | = λ(u    | ,S); |         |     |     |     |     |     |
| 22  |     |     |         | k        |          | x    |         |     |     |     |     |     |
|     |     |     | Update  | S ←      | conv1b(s |      | ,S,gt); |     |     |     |     |     |
| 23  |     |     |         |          |          |      | k       |     |     |     |     |     |
0
|     | Else | if  | x ∈ F | then |     |     |     |     |     |     |     |     |
| --- | ---- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24  |      |     | c     |      |     |     |     |     |     |     |     |     |
𭟋
| 25  |     | Compute | k   | =   | (x); |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Ic∪Fc
|     |     | Compute | [u  | ,S] | ← conv1b(0,S,gt); |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| 26  |     |         |     | x   |                   |     |     |     |     |     |     |     |
0
|     |     | If x | ∈ F∗ | then |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
27
|     |     |     | If u = | 1 and   | x ∈/   | M ˜ then |     |     |     |     |     |     |
| --- | --- | --- | ------ | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- |
| 28  |     |     | x      |         |        |          |     |     |     |     |     |     |
|     |     |     | X      | = X +1, | break; |          |     |     |     |     | //  | C1  |
29
|     |     |     | If u = | 0 and   | x ∈    | M ˜ then |     |     |     |     |     |     |
| --- | --- | --- | ------ | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- |
| 30  |     |     | x      |         |        |          |     |     |     |     |     |     |
|     |     |     | X      | = X +1, | break; |          |     |     |     |     | //  | C2  |
31
| 32  |     | Else |        |                |     |     |        |     |     |     |       |     |
| --- | --- | ---- | ------ | -------------- | --- | --- | ------ | --- | --- | --- | ----- | --- |
|     |     |      | If u = | 1 then         |     |     |        |     |     | //  | for x | ∈ F |
| 33  |     |      | x      |                |     |     |        |     |     |     |       | J   |
|     |     |      | M ˜    | ← addToM(i,x,J |     |     | ˜ ,M ˜ | );  |     |     |       |     |
34
|     |     |     | J ˜ | ← J ˜ | ∪{x}; |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
35
|     | Else |      |       |      |     |     |     |     |     | //  | for x | ∈ F |
| --- | ---- | ---- | ----- | ---- | --- | --- | --- | --- | --- | --- | ----- | --- |
| 36  |      |      |       |      |     |     |     |     |     |     |       | p   |
|     |      | If x | ∈ M ˜ | then |     |     |     |     |     |     |       |     |
37
|     |     |     | X = X | +1, | break; |     |     |     |     |     | //  | C3  |
| --- | --- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
38
|           | AM  | P A C | 2|Ki| |     |     |     |     |     |     |     |     |     |
| --------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 39 Return |     |       | =     | −X; |     |     |     |     |     |     |     |     |
i,ω m in

| IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED |     |     |             |            |     |     | 25  |
| ----------------------------------------------- | --- | --- | ----------- | ---------- | --- | --- | --- |
|                                                 |     | V.  | AUB-OPTIMAL | MPAC CODES |     |     |     |
This sectiondesigns theAUB-optimal MPAC codesthrough searchingfor the optimalconvolu-
(N∗,K∗).
tional parameters This design approach shows a partially convolutional transformation
c c
can improve the minimum weight distribution for an MPAC code over its prototype PAC code,
attributed to utilizing the row combinations of the frozen set more efficiently. The AUB-optimal
MPAC code outperforms a PAC code and a CRC-polar code in terms of both MWD and decoding
performance.
| A. Design | of AUB-Optimal | MPAC | Codes |     |     |     |     |
| --------- | -------------- | ---- | ----- | --- | --- | --- | --- |
With the proposed coset-wise analysis of the MWD for MPAC codes, the minimum distance
d and the number of MWCs A can be determined. Furthermore, eq. (2) implies that both
| min |     |     | dmin |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
maximizing d and minimizing A can optimize the AUB P . The asymptotic ML decoding
|     | min |     | dmin |     | e   |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
performance of different MPAC codes that are specified by their convolutional parameters
(N ,K ) can be evaluated by their corresponding AUBs P . It guides the design of MPAC
| c c |     |     |     |     | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
codes, especially in determining (N ,K ) in optimizing the code’s AUB performance. We call
c c
| them the | AUB-optimal | MPAC codes. |     |     |     |     |     |
| -------- | ----------- | ----------- | --- | --- | --- | --- | --- |
Given N and K, let (N∗,K∗) denote the pair that optimizes the code’s AUB performance.
c c
| Considering | the parameter | constraint | of (10), | we have |     |     |      |
| ----------- | ------------- | ---------- | -------- | ------- | --- | --- | ---- |
|             |               |            | 0 ≤ N −K | ≤ N −K, |     |     |      |
|             |               |            | c        | c       |     |     |      |
|             |               |            | 0 < K    | ≤ K,    |     |     | (31) |
c
|     |     |     | 0 < N | ≤ N. |     |     |     |
| --- | --- | --- | ----- | ---- | --- | --- | --- |
c
The above inequalities imply that K ∈ [1,K] and N ∈ [K ,N − K + K ]. There are
|     |     |     | c   | c   | c   | c   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
K(N −K +1) pairs of (N ,K ). With the coset-wise analysis of MWD, this parameter search
c c
becomespractical.Sincethetworateprofilingsandthechoiceof(N ,K )jointlydetermined ,
|     |     |     |     |     | c c |     | min |
| --- | --- | --- | --- | --- | --- | --- | --- |
maximizing d can be realized by choosing specific pairs of (N ,K ). This helps rationalize
|               | min        |        |          |     | c c |     |     |
| ------------- | ---------- | ------ | -------- | --- | --- | --- | --- |
| the otherwise | exhaustive | search | process. |     |     |     |     |
Fig. 8 shows how the AUB performances P of MPAC codes are affected by K and N
|     |     |     |     | e   |     | c   | c   |
| --- | --- | --- | --- | --- | --- | --- | --- |
under the SNR per information bit of E /N = 3.5 dB. We consider the MPAC codes with
|     |     |     | b   | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
length N = 128, dimension K = 64 and the convolutional generator polynomial coefficients of
(1,0,1,1,0,1,1). The rate profiling is conducted by GA at an SNR of 0 dB. We compare the
AUB performances of MPAC codes with the prototype (128,64) PAC code of [7]. The PAC code

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 26
Fig. 8. AUB performances of the MPAC codes and PAC codes versus parameters (N ,K ), where N = 128, K = 64 and
c c
E /N =3.5 dB.
b 0
is constructed by the RM rate profiling. Its MWD is d = 16 and A = 3120. The AUB
min dmin
performances are measured versus parameters (N ,K ), yielding the blue and the red meshes that
c c
correspond to the MPAC codes and the PAC code, respectively. In particular, the AUB-optimal
MPAC code with parameter (N∗,K∗) = (65,45) is marked by a red ‘×’ symbol. The code has
c c
d = 16 and A = 2633. It can be seen that there exist numerous (N ,K ) that can enable
min dmin c c
an MPAC code to outperform the prototype PAC code. This is due to a better weight distribution
is produced by the partially convolutional transform in the MPAC codes. Furthermore, Fig. 8
also suggests that a larger K is more likely to yield a better weight distribution for the MPAC
c
codes. It helps maximize d and yields a greater MWC number deficit X. With a large K ,
min c
reducing N within the scope that keeps d being maximized generally achieves a better AUB
c min
performance. This indicates that assigning elements from set F to set F can lead to a better
c p
MWD for the MPAC codes. An extreme case to the opposite is when K = 0, the MPAC codes
c
become polar codes with no improvement on its weight distribution.
B. Simulation Results
ThissubsectionpresentstheMWDresultsandperformancesoftheAUB-optimalMPACcodes.
The AUB-optimal MPAC codes are also compared with the relevant coding schemes, especially

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 27
the MPAC codes designed in Section III. Note that the parameters of the relevant coding schemes
that are applied in this subsection are the same as those in Section III-C.
|     |     |     |     | TABLE | I   |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
THEMWDOFAUB-OPTIMALMPACCODES,PACCODES,ENSEMBLEAVERAGEANDCRC-POLARCODESWITH
DIFFERENTCODEPARAMETERS
|     |     | PAC |     | MPAC |     | Ensemble | Average | CRC-polar |
| --- | --- | --- | --- | ---- | --- | -------- | ------- | --------- |
N K
(N∗,K∗)
|        | d   | A     |          | d     | A     | d   | A       | d A      |
| ------ | --- | ----- | -------- | ----- | ----- | --- | ------- | -------- |
|        | min | dmin  | c        | c min | dmin  | min | dmin    | min dmin |
| 29     | 32  | 820   | (61,29)  | 32    | 436   | 32  | 422.1   | 24 53    |
| 128 64 | 16  | 3120  | (65,45)  | 16    | 2633  | 16  | 2766.9  | 12 224   |
| 99     | 8   | 16080 | (89,71)  | 8     | 15264 | 8   | 15936.0 | 6 152    |
| 93     | 32  | 5092  | (145,86) | 32    | 2788  | 32  | 2766.9  | 16 6     |
256
| 163     | 16  | 18896  | (169,132) | 16  | 15622  | 16  | 15936.3  | 8 4    |
| ------- | --- | ------ | --------- | --- | ------ | --- | -------- | ------ |
| 130     | 64  | 17092  | (252,110) | 64  | 3466   | 64  | 2766.9   | 32 256 |
| 512 256 | 32  | 35900  | (342,222) | 32  | 17108  | 32  | 15936.3  | 16 966 |
| 382     | 16  | 128704 | (314,216) | 16  | 104209 | 16  | 101280.0 | 8 2307 |
TableIprovidestheMWDofPACcodes,theAUB-optimalMPACcodes,theensembleaverage
of pre-transformed polar codes [30] and CRC-polar codes. The average MWD of pre-transformed
polar codes is analyzed by the probabilistic method that calculates the weight spectrum of
the pre-transformed polar codes with randomly generated pre-transformed matrix and the RM
rate profiling. The detailed procedure of this method can be found in [30]. MPAC codes are
constructed by the proposed iRMP construction, while PAC codes are constructed by the RM rate
profiling. The convolutional generator polynomial coefficients (1,0,1,1,0,1,1) are employed.
The CRC-polar codes are constructed by the 5G reliability sequence.
It can be seen that for a wide range of code parameters, the AUB-optimal MPAC codes yield
a better MWD than the respective PAC codes and CRC-polar codes. In particular, the AUB-
optimal MPAC codes yield the same minimum distance d as the PAC codes, but they contain
min
less MWCs. Meanwhile, it can also be observed that the minimum distance of the AUB-optimal
MPAC codes are greater than that of the CRC-polar codes. Furthermore, the AUB-optimal MPAC
codesyieldacloseA comparedtotheaveragepre-transformedpolarcodes.Theydemonstrate
dmin
that the AUB-optimal MPAC codes have the MWD advantage over both the PAC codes and the
| CRC-polar | codes. |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
With code parameters of N and K concerned in Table I, MPAC codes have the same

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 28
information set I as the corresponding PAC codes. Their main difference is reflected in pre-
transformed design. By defining d as bits before polar transformation, the pre-transformed matrix
dN−1.
G can be utilized to represent the constraint relationship between bits in Note that
| pre |     |     |     |     |     |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- |
cN−1 = dN−1G G . In particular, for PAC codes, we have G = G . For MPAC codes, the
| 0 0 | pre p |     |     |     | pre | c   |     |
| --- | ----- | --- | --- | --- | --- | --- | --- |
submatrix of G with rows and columns selected in P is G′. G is further obtained with
|                   | pre          |       |          |           | c   | pre |     |
| ----------------- | ------------ | ----- | -------- | --------- | --- | --- | --- |
| diagonal elements | set to 1 and | other | elements | set to 0. |     |     |     |
|                   | 100          |       |          | 25        |     |     |     |
|                   | 10−1         |       |          | 20        |     |     |     |
 ytixelpmoC dezilamroN
10−2
15
REF
|     | 10−3                      |     |       | 10                  |       |                       |     |
| --- | ------------------------- | --- | ----- | ------------------- | ----- | --------------------- | --- |
|     | 10−4                      |     |       | 5                   |       |                       |     |
|     | 10−5                      |     |       | 0                   |       |                       |     |
|     | 1 2                       | 3   |       | 4 1.0 1.5           | 2.0   | 2.5 3.0 3.5           | 4.0 |
|     |                           | SNR |       |                     | SNR   |                       |     |
|     |    MPAC-(65, 45)*, HFSC   |     |       |    PAC, Fano        |       |  MPAC-(65, 45)*, AUB  |     |
|     |    MPAC-(96, 48), HFSC    |     |       |    CRC-Polar, SCL   |       |  PAC, AUB             |     |
|     |    MPAC-(64, 32), HFSC    |     |       |    Polar, SC        |       |  CRC-Polar, AUB       |     |
Fig. 9. Performance comparison of the AUB-optimal MPAC codes and other relevant codes, where N =128 and K =64.
Therefore, the G of an MPAC code is sparser than that of a PAC code and generally not a
pre
Toeplitz matrix. Consequently, some bits of an MPAC code in d can influence other bits with a
Ic
more distant index in d than the case in PAC code. For low rate polar-like codes, the continuous
Fc
length of the frozen set is large. With short convolutional generator polynomials employed, PAC
codes can only utilize a portion of d to reduce the number of MWCs sufficiently. However, the
Fc
MPAC codes can utilize the sparser pre-transformed matrix to involve more rows in F in row
c
combinations. This results in a better effect on the MWC number deficit X increasing especially
for low code rates. As a result, the MPAC codes not only inherit the advantage of PAC codes,
but also incorporate the row combinations of the frozen set. After selecting the convolutional

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 29
parameters, this leads to a better MWD for the AUB-optimal MPAC codes than the PAC codes
| and the CRC-polar | codes. |     |     |     |     |
| ----------------- | ------ | --- | --- | --- | --- |
Note that as the code rate increases, the MWD improvement margin of MPAC codes becomes
less significant. This is because in such situation, some MWCs in the specific cosets cannot be
reduced. The proportion of these irreducible MWCs increases with the code rate. On the other
hand, higher rate restricts the size of F for MPAC codes, which leads to less improvement of
p
| MWD in comparison | with PAC | codes. |      |     |     |
| ----------------- | -------- | ------ | ---- | --- | --- |
|                   | 100      |        | 10.0 |     |     |
10−1
7.5
 ytixelpmoC dezilamroN
10−2
REF
10−3
5.0
10−4
2.5
10−5
|     | 10−6                     |         | 0.0                        |                  |     |
| --- | ------------------------ | ------- | -------------------------- | ---------------- | --- |
|     | 1 2                      | 3       | 4 1.0 1.5                  | 2.0 2.5 3.0 3.5  | 4.0 |
|     |                          | SNR     |                            | SNR              |     |
|     |   MPAC-(61, 29)*, HFSC   |         |   CRC-Polar, SCL           |         PAC, AUB |     |
|     |   MPAC-(33, 14), HFSC    |         |   Polar, SC                |  CRC-Polar, AUB  |     |
|     |   PAC, Fano              |         |  MPAC-(61, 29)*, AUB       |                  |     |
|     |  MPAC-(61, 29)*, SCL     |         |                            |                  |     |
Fig. 10. Performance comparison of the AUB-optimal MPAC codes and other relevant codes, where N =128 and K =29.
Finally, Fig. 9 shows the HFSC decoding FER, normalized complexity and AUB of the
optimizedMPACcodewithN = 128andK = 64.Adecodingcomputationthresholdofη = 128
is applied. The decoding FER and complexity performances of different coding schemes are also
provided, including the MPAC-(96,48) and the MPAC-(64,32) codes. Note that the MWD of
the MPAC-(96,48) code and the MPAC-(64,32) code are {d = 16,A = 2900} and
|     |     |     |     | min | dmin |
| --- | --- | --- | --- | --- | ---- |
{d = 16,A = 3121}, respectively. It can be seen that the AUB-optimal MPAC code
| min | dmin |     |     |     |     |
| --- | ---- | --- | --- | --- | --- |
indicated by ∗ as MPAC-(65,45)∗ can slightly outperform the MPAC-(96,48) code and the
MPAC-(64,32) code with an increased complexity. Fig. 10 shows the same coding schemes
with N = 128 and K = 29. It can be seen that the AUB-optimal MPAC code with HFSC

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 30
decoding outperforms the MPAC-(33,14) code, the PAC code and the CRC-polar code in both
the decoding FER and the AUB.
VI. CONCLUSION
This paper has proposed the MPAC codes and their HFSC decoding. Realized by two rate
profiling steps with convolutional parameters, a subset of the information bits first undergo the
convolutional transform. The convolutional output then together with the remaining information
bits undergo the polar transform. Consequently, the HFSC decoding deploys the Fano decoding
and SC decoding to recover the information bits that have undergone the convolutional transform
and those that have not, respectively. The MWD analysis of the MPAC codes has been provided
in the coset-wise framework, which can be further utilized to optimize the design of MPAC
codes, especially in selecting the convolutional parameters. Consequently, the AUB-optimal
MPAC codes can be designed, achieving a better MWD than the PAC codes and CRC-polar
codes. The implication of the MWD improvement is examined by effectively exploiting the row
combinations of the frozen set, which originates from the sparser pre-transformed matrix of
MPAC codes. Simulation results of the proposed schemes and the relevant schemes have been
presented to verify the decoding performance and complexity advantages of the proposed MPAC
coding schemes.
ACKNOWLEDGEMENT
This work was sponsored by the National Natural Science Foundation of China (NSFC) with
project ID 62471503 and Guangdong National Science Foundation (GDNSF) with project ID
2024A1515010213.
REFERENCES
[1] E. Arıkan, “Channel polarization: A method for constructing capacity-achieving codes for symmetric binary-input
memoryless channels,” IEEE Trans. Inform. Theory, vol. 55, no. 7, pp. 3051–3073, Jul. 2009.
[2] I.TalandA.Vardy,“Listdecodingofpolarcodes,”IEEETrans.Inform.Theory,vol.61,no.5,pp.2213–2226,Jul.2015.
[3] K. Niu and K. Chen, “CRC-aided decoding of polar codes,” IEEE Commun. Lett., vol. 16, no. 10, pp. 1668–1671, Oct.
2012.
[4] T. Wang, D. Qu, and T. Jiang, “Parity-check-concatenated polar codes,” IEEE Commun. Lett., vol. 20, no. 12, pp. 2342–
2345, Dec. 2016.
[5] H. Zhang, R. Li, J. Wang, S. Dai, G. Zhang, Y. Chen, H. Luo, and J. Wang, “Parity-check polar coding for 5G and
beyond,” in Proc. 2018 IEEE Int. Conf. Commun. (ICC), Kansas City, MO, USA., May 2018.

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 31
[6] A. Fazeli, K. Tian, and A. Vardy, “Viterbi-aided successive-cancellation decoding of polar codes,” in Proc. 2017 IEEE
Glob. Commun. Conf. (GLOBECOM), Singapore, Singapore, Dec. 2017.
[7] E. Arıkan, “From sequential decoding to channel polarization and back again,” preprint available as arXiv:1908.09594,
Aug. 2019.
[8] R.MoriandT.Tanaka,“Performanceofpolarcodeswiththeconstructionusingdensityevolution,”IEEECommun.Lett.,
vol. 13, no. 7, pp. 519–521, Jul. 2009.
[9] I. Tal and A. Vardy, “How to construct polar codes,” IEEE Trans. Inform. Theory, vol. 59, no. 10, pp. 6562–6582, Oct.
2013.
[10] P. Trifonov, “Efficient design and decoding of polar codes,” IEEE Trans. Commun., vol. 60, no. 11, pp. 3221–3227, Nov.
2012.
[11] G.He,J.-C.Belfiore,I.Land,G.Yang,X.Liu,Y.Chen,R.Li,J.Wang,Y.Ge,R.Zhang,andW.Tong,“Beta-expansion:
A theoretical framework for fast and recursive construction of polar codes,” in Proc. 2017 IEEE Glob. Commun. Conf.
(GLOBECOM), Singapore, Singapore, Dec. 2017, pp. 1–6.
[12] B. Li, H. Shen, and D. Tse, “A RM-polar codes,” preprint available as arXiv:1407.5483, Jul. 2014.
[13] M. Rowshan, A. Burg, and E. Viterbo, “Polarization-adjusted convolutional (PAC) codes: sequential decoding vs list
decoding,” IEEE Trans. Veh. Technol., vol. 70, no. 2, pp. 1434–1447, Feb. 2021.
[14] W. Liu, L. Chen, and X. Liu, “A weighted sum based construction of PAC codes,” IEEE Commun. Lett., vol. 27, no. 1,
pp. 28–31, Jan. 2023.
[15] M. Moradi and A. Mozammel, “A Monte-Carlo based construction of polarization-adjusted convolutional (PAC) codes,”
preprint available as arXiv:2106.08118, Jun. 2021.
[16] M.-C. Chiu and Y.-S. Su, “Design of polar codes and PAC codes for SCL decoding,” IEEE Trans. Commun., vol. 71,
no. 5, pp. 2587–2601, May 2023.
[17] M. Moradi and D. G. M. Mitchell, “PAC code rate-profile design using search-constrained optimization algorithms,”
preprint available as arXiv:2401.10376, Jan. 2024.
[18] S.Jiang,J.Wang,C.Xia,andX.Li,“ConstructionofPACcodeswithlist-searchandpath-splittingcriticalsets,”preprint
available as arXiv:2304.11554, Apr. 2023.
[19] X.Gu,M.Rowshan,andJ.Yuan,“ImprovedconvolutionalprecoderforPACcodes,”inProc.2023IEEEGlob.Commun.
Conf. (GLOBECOM), Kuala Lumpur, Malaysia, Dec. 2023.
[20] M. Rowshan, S. H. Dau, and E. Viterbo, “On the formation of min-weight codewords of polar/PAC codes and its
applications,” IEEE Trans. Inform. Theory, vol. 69, no. 12, pp. 7627–7649, Dec. 2023.
[21] R. Fano, “A heuristic discussion of probabilistic decoding,” IEEE Trans. Inform. Theory, vol. 9, no. 2, pp. 64–74, Apr.
1963.
[22] M. Moradi, “On sequential decoding metric function of polarization-adjusted convolutional (PAC) codes,” IEEE Trans.
Commun., vol. 69, no. 12, pp. 7913–7922, Dec. 2021.
[23] M. Moradi, A. Mozammel, K. Qin, and E. Arıkan, “Performance and complexity of sequential decoding of PAC codes,”
preprint available as arXiv:2012.04990, Dec. 2020.
[24] W. Liu, L. Chen, and X. Liu, “Hybrid decoding of CRC-polar codes,” in Proc. 13th Int. Conf. Wirel. Commun. Signal
Process. (WCSP), Virtual, Online, China, Oct. 2021.
[25] M. Abdullah and W. H. Mow, “New search for the polarization-adjusted convolutional codes with respect to the AFER-
optimality criterion,” in Proc. 2023 IEEE Int. Symp. Inform. Theory (ISIT), Taipei, Taiwan, China, 2023.
[26] S.Gelincik,P.Mary,A.Savard,andJ.-Y.Baudais,“Preservingtheminimumdistanceofpolar-likecodeswhileincreasing
the information length,” in Proc. 2022 IEEE Int. Symp. Inform. Theory (ISIT), Espoo, Finland, Jun. 2022.

IEEETRANSACTIONSONINFORMATIONTHEORY,RESUBMITTED 32
[27] M.Xu,P.Chen,B.Bai,andS.Tong,“Distancespectrumandoptimizeddesignofconcatenatedpolarcodes,”inProc.9th
| Int. Conf. | Wirel. Commun. | Signal Process. | (WCSP), | Nanjing, | China, Oct. 2017. |
| ---------- | -------------- | --------------- | ------- | -------- | ----------------- |
[28] M. Valipour and S. Yousefi, “On probabilistic weight distribution of polar codes,” IEEE Commun. Lett., vol. 17, no. 11,
| pp. 2120–2123, | Nov. 2013. |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- |
[29] Q.Zhang,A.Liu,andX.Pan,“Anenhancedprobabilisticcomputationmethodfortheweightdistributionofpolarcodes,”
| IEEE Commun. | Lett., vol. | 21, no. 12, pp. | 2562–2565, | Dec. 2017. |     |
| ------------ | ----------- | --------------- | ---------- | ---------- | --- |
[30] Y. Li, H. Zhang, R. Li, J. Wang, G. Yan, and Z. Ma, “On the weight spectrum of pre-transformed polar codes,” in Proc.
2021 IEEE Int. Symp. Inform. Theory (ISIT), Virtual, Melbourne, VIC, Australia, Jul. 2021.
[31] S. Lin and D. J. Costello, Error Control Coding, 2nd ed. Pearson Prentice Hall, Upper Saddle River, May 2004.
[32] M.Bardet,V.Dragoi,A.Otmani,andJ.-P.Tillich,“Algebraicpropertiesofpolarcodesfromanewpolynomialformalism,”
| in Proc. | 2016 IEEE Int. Symp. | Inform. Theory | (ISIT), | Barcelona, | Spain, Jul. 2016. |
| -------- | -------------------- | -------------- | ------- | ---------- | ----------------- |
[33] M. Rowshan and J. Yuan, “On the minimum weight codewords of PAC codes: The impact of pre-transformation,” IEEE
| J. Select. | Areas. Inform. | Theory, vol. 4, pp. | 487 – | 498, Sep. | 2023. |
| ---------- | -------------- | ------------------- | ----- | --------- | ----- |
[34] B. Li, H. Shen, and D. Tse, “An adaptive successive cancellation list decoder for polar codes with cyclic redundancy
| check,” IEEE | Commun. Lett., | vol. 16, no. | 12, pp. | 2044–2047, | Dec. 2012. |
| ------------ | -------------- | ------------ | ------- | ---------- | ---------- |
[35] Z. Cai, L. Chen, W. Liu, and H. Zhang, “Modified PAC codes,” in Proc. 2023 IEEE Int. Symp. Inform. Theory (ISIT),
| Taipei, Taiwan, | China, Jun. | 2023. |     |     |     |
| --------------- | ----------- | ----- | --- | --- | --- |
[36] R. G. Gallager, Information Theory and Reliable Communication. New York, NY, USA: Wiley, Dec. 1968.
[37] A. Balatsoukas-Stimming, M. B. Parizi, and A. Burg, “LLR-based successive cancellation list decoding of polar codes,”
| IEEE Trans. | Signal Process., | vol. 63, no. | 19, pp. | 5165–5179, | Oct. 2015. |
| ----------- | ---------------- | ------------ | ------- | ---------- | ---------- |
[38] 3GPP,“5GNR:MultiplexingandChannelCoding,”3rdGenerationPartnershipProject(3GPP),TS38.212version15.2.0,
Jul. 2018.
[39] C.Schurch,“Apartialorderforthesynthesizedchannelsofapolarcode,”inProc.2016IEEEInt.Symp.Inform.Theory
| (ISIT), Barcelona, | Spain, | Jul. 2016. |     |     |     |
| ------------------ | ------ | ---------- | --- | --- | --- |
[40] B. Li, H. Zhang, and J. Gu, “On pre-transformed polar codes,” preprint available as arXiv:1912.06359, Dec. 2019.
[41] M. Rowshan and J. Yuan, “Fast enumeration of minimum weight codewords of PAC codes,” in Proc. 2022 IEEE Inform.
| Theory Workshop | (ITW), | Mumbai, India, | Nov. 2022. |     |     |
| --------------- | ------ | -------------- | ---------- | --- | --- |
---- END DOCUMENT ----
