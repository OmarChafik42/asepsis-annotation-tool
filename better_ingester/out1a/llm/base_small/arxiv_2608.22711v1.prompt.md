Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
General-Sum Linear Regulator Games for Positive Systems
Alba Gurpegui∗,1 , Monika Tomar∗,2 and Takashi Tanaka2
Abstract—Thispaperstudiesacontinuous-timegeneral-sum equilibria play a central role in the differential games litera-
non-cooperative game with linear costs, positive linear system ture [7], particularly in linear-quadratic LQ games [8]–[11],
dynamics, and elementwise linear input constraints. In the
including the Riccati-based formulations for positive linear
finite-horizon case, we present a verification theorem charac-
systems [12] and associated iterative solvers [13]. Positivity
terizing feedback Nash equilibria, in terms of absolutely con-
tinuoussolutionsofacoupledsystemofvector-valuedordinary of the system dynamics arises naturally in game-theoretic
differential equations, realized by time-varying feedback laws. settings such as evolutionary and population dynamics [14]
Unlikelinear-quadraticdifferentialgames,whoseRiccati-based and pollution games [15], where states (populations, pollu-
equilibria scale quadratically with the state dimension, this
tantstocks)areintrinsicallynonnegativeandcostsarelinear,
formulation scales linearly. However, the resulting piecewise-
astheprofitsfromemittingandthecostsofpollutioncontrol
constant feedback saturates between its constraint bounds
rather than varying smoothly, and additional mathematical growinproportiontotheamountinvolved.Inthispaper,we
challengesarisewhencharacterizingthesolutionsofthediffer- exploit this positivity property and build on prior work in
ential equations, which are generally discontinuous due to the zero-sum dynamic games, formulated as minimax optimal
switching nature of the feedback gains. In this work, we study control problems with linear costs, linear positive dynamics,
thecasewhereswitchingoccursonlyatisolatedtimeinstants.In
and elementwise linear input constraints, which has been
the infinite-horizon case, under stabilizability assumptions, the
equilibriumischaracterizedbycoupledvector-valuedalgebraic studied both in discrete [16] and continuous time [17]. This
equations.Forthisgame,weproposeiterativemethodstocom- class, referred to as the Minimax Linear Regulator (LR)
pute both finite and infinite-horizon equilibria. The approach problem, admits explicit solutions for all nonnegative initial
is illustrated through a large-scale pollution game.
conditions under appropriate assumptions. Inspired by these
I. INTRODUCTION results, we extend the minimax LR framework to a general-
Continuous-time dynamic game theory provides a nat- sum non-cooperative dynamic game setting and study the
ural framework for modeling interactions among strategic corresponding feedback Nash equilibria. The contributions
agents whose decisions evolve over time. This framework of this work are summarized below.
finds applications across a wide range of fields, including C1 We propose a general-sum non-cooperative dynamic
economics [1], ecology [2] and epidemiology [3]. In non- game with linear costs, positive linear dynamics and
cooperative settings, different solution concepts are avail- elementwise linear constraints on the inputs.
able, but the Nash equilibrium solution remains the most C2 We present a verification theorem characterizing feed-
prominent. This solution is defined by the property that no back Nash equilibria given by state-feedback policies
player can reduce its cost through unilateral deviation. Nash with piecewise-constant gains, in terms of absolutely
equilibria can be defined in different ways: in open-loop continuous solutions of coupled vector-valued ordinary
form, where control inputs depend only on time and initial differential equations (ODEs).
conditions, or in feedback form, where they depend on the C3 Underappropriatestabilizabilityassumptions,wepresent
current state. In general, these notions are not equivalent, the stationary feedback Nash equilibria, which are given
although they coincide for certain classes of games [4], by static state-feedback laws and characterized by cou-
[5]. Equilibria in non-cooperative games can be classified pled vector-valued algebraic equations.
according to their robustness and time-consistency. Feed- C4 We develop iterative algorithms for computing the equi-
back Nash equilibria are generally considered strongly time libriaoftheconsideredfiniteandinfinite-horizonsettings
consistent, as they allow players to react to deviations in andillustrateourresultsonalarge-scalepollutiongame.
the state trajectory regardless of past policies [6]. These
A. Notation
ThisworkispartiallyfundedbytheWallenbergAI,AutonomousSystems LetR + denotethesetofnonnegativerealnumbers,Rn the
andSoftwareProgram(WASP),theEuropeanResearchCouncil(ERC)un- n-dimensional Euclidean space and Rn the positive orthant.
dertheEuropeanUnion’sHorizon2020researchandinnovationprogramme Rm×n denotes the set of m×n real + matrices. Any vector
undergrantagreementNo101199738,DARPACOMPASSprogramunder
grant agreement HR0011-25-3-0210 and AFOSR DSCT program under is, by default, a column vector. 1 denotes the vector of
grantagreementFA9550-25-1-0347. ones of appropriate dimension, and I denotes the n×n
∗Theseauthorscontributedequally.1A.GurpeguiiswiththeDepartment n
identitymatrix.Foravectorx,diag(x)denotesthediagonal
of Automatic Control and the ELLIIT Strategic Research Area at Lund
University,Lund,Sweden.2 M.TomarandT.TanakaarewiththeSchool matrix with entries of x on the diagonal. |X| denotes the
ofIndustrialEngineering,SchoolofAeronauticsandAstronautics,Elmore matrix obtained by replacing the elements of a real matrix
Family School of Electrical and Computer Engineering, Purdue Univer-
X with their absolute values. Inequalities between matrices
sity,WestLafayette,IN,USA.Email:alba.gurpeguiramon@control.lth.se,
tomarm@purdue.edu,tanaka16@purdue.edu, or vectors are understood elementwise; in particular, X ≥0
6202
guA
42
]CO.htam[
1v11722.8062:viXra

(X ≤ 0) means that all entries of X are nonnegative exists a feedback law u = −Kx with |u| ≤ Ex such that
(nonpositive). The signum of a scalar is defined as the set- A−BK is Hurwitz.
valued map 
 {−1} ifx<0 The following Lemma characterizes the infinite-horizon
sign(x)= [−1,+1] ifx=0. optimal value of the LR problem (1) as T →∞.
{+1}
ifx>0
Lemma1. LetA∈Rn×n,B ∈Rn×m,E ∈Rm×n,s∈Rn,
+
II. PRELIMINARIES r ∈Rm. Suppose that the pair (A,B) is E-stabilizable and
Dynamical systems that leave the positive orthant of the A−|B|E isMetzler,s−E⊤|r|>0holds.Then,asT →∞,
statespaceinvariantarecalledpositivesystems(relatedcon- problem (1) has a finite minimum for every x 0 if and only if
ceptsincludecompartmentalsystemsandmonotonesystems
0=s+A⊤p−K⊤(r+B⊤p) (3)
[18]), and have attracted special attention in the control
theory literature. A linear dynamical system x˙(t) = Ax(t) holds with K ∈ diag (cid:0) sign(r+B⊤p) (cid:1) E. Moreover, the
is called positive if entry-wise nonnegativity of x(0) implies feedback law u∗(t) := −Kx is optimal and E-stabilizing
entry-wise nonnegativity of x(t) for all t ≥ 0. It is well and the optimal cost is given by J(x ,u∗)=p⊤x .
0 0
known that this holds if and only if A is a Metzler matrix
Proof: This theorem follows from [17, Cor. 7]. ■
(i.e., a square matrix with non-negative off-diagonal entries)
It is worth highlighting that the algebraic equation (3)
[19, Thm. 2.5]. Motivated by this property, we consider the
can be reformulated equivalently as a linear program [17,
Linear Regulator (LR) problem, an optimal control problem
Thm. 12], leveraging the scalability potential of this optimal
with linear nonnegative cost, positive linear dynamics and
control problem class.
elementwise linear input constraints
III. PROBLEMFORMULATION
min (cid:82)T (cid:2) s⊤x(τ)+r⊤u(τ) (cid:3) dτ
µ 0 Consider a continuous-time system with N > 1 players
s.t x˙(t)=Ax(t)+Bu(t), x(0)=x (1) described by the differential equation
0
u(t)=µ(x(t)), |u|≤Ex, x˙(t)=Ax(t)+ (cid:80)N B u (t), x(0)=x (4)
i=1 i i 0
wherethevectorx(t)denotesthetime-varyingstate,u(t)the fort∈[0,T],wherex 0 ∈Rn + ,x(t)∈Rnisthestatevariable
control input, A∈Rn×n, B ∈Rn×m, E ∈Rm + ×n, s∈Rn, ofthesystemandu i (t)∈Rmi isthecontrolinputofthei-th
and r ∈Rm. player for i = 1,...,N satisfying |u i | ≤ E i x, E i ∈ Rm + i×n.
Remarkably,explicitsolutionsforthisproblemarederived LetA∈Rn×n beaMetzlermatrix,andB i ∈Rn×mi forall
in [17] under the assumption A−|B|E is Metzler and s− i. Each player i=1,...,N has an associated cost functional
E⊤|r|>0, motivated in Remark 1. Under these conditions, C (t,x,u ,...,u )= (cid:82)T (cid:0) s⊤x(τ)+r⊤u (τ) (cid:1) dτ (5)
the explicit solution of the problem (1) is characterized by a i 1 N t i i i
vector p(t)∈Rn satisfying where x(s), t≤s≤T on the right-hand side is defined by
+ (4) with the initial condition x(t) = x ∈ Rn, the input
+
−p˙(t)=s+A⊤p(t)−E⊤|r+B⊤p(t)|, p(T)=0. (2) u
i
(t) ∈ Rmi, i = 1,...,N and s
i
∈ Rn
+
, r
i
∈ Rmi.
We formulate this setting as a non-cooperative differential
In fact, if the LR problem has a solution, by Picard-
game, where each player seeks to minimize its individual
Lindelo¨f[20]thesolutionisunique,theoptimalcostisgiven
cost functional, subject to the following assumptions.
by p(0)⊤x and the optimal control policy is, among all
0
potentially nonlinear policies, a time-varying policy u∗(t)= Assumption 1. A− (cid:80)N |B |E is Metzler.
i=1 i i
−K(t)x(t)withK(t)∈ diag(sign(r+B⊤p(t)))E.Werefer
Assumption 2. s −E⊤|r |>0 for all i.
totheentries(r+B⊤p(t))astheinputgradients.Theoptimal i i i
policy defined above is not necessarily unique. Specifically, Remark1. Assumption1ensurestheinvarianceoftheposi-
whenaninputgradientvanishesatsomeindexi,allfeedback tiveorthantunderthesystemdynamics(4)andAssumption2
gain matrices in the set guarantees that each cost functional (5) is nonnegative and
bounded from below.
K= (cid:8) DE |D ∈[−1,1],D ∈sign([r+p(t)⊤B] )forj ̸=i (cid:9)
ii jj j
Werefertotheresultingnon-cooperativedifferentialgame
lead to the same and unique solution p(t) of the ODE (2). as the Linear Regulator (LR) general-sum game. In this
Importantly,theoptimalpolicyinheritsthesparsitystructure article, we focus on feedback Nash-equilibrium solutions,
oftheEmatrix,whichisdeterminedbytheproblemdesigner as recalled in the following definition [7].
and may capture limitations in actuation and sensing.
Definition 2 (Feedback Nash equilibrium). Consider the
In the infinite-horizon case, we additionally require the
dynamic game defined by (4) and (5). The set of feedback
optimalsolutionstoensureclosed-loopstability.Anotionof
control laws (µ∗,...,µ∗ ) is a feedback Nash equilibrium if
stabilizability within the constrained input class |u| ≤ Ex, 1 N
is defined in [17] as E-stabilizability. C (t,x,µ∗,...,µ∗,...,µ∗ )≤C (t,x,µ∗,...,µ ,...,µ∗ )
i 1 i N i 1 i N
Definition 1 (E-stabilizability). Let A∈Rn×n, B ∈Rn×m for all pairs (t,x)∈[0,T]×Rn, where C is the cost func-
+ i
and E ∈ Rm×n. The pair (A,B) is E-stabilizable if there tional (5).
+

IV. MAINRESULTS for every admissible input, the system f
1
(x,u
1
) admits a
A. Finite Horizon unique Carathe´odory solution x which is AC, hence V 1 (τ,x)
is AC. By the Fundamental Theorem of Calculus for AC
In this section, we study the non-cooperative differential
functions [22, Thm. 7.18]
game over a fixed horizon [0,T], in which each player
chooses an admissible state-feedback law subject to elemen- p (T)⊤x(T)−p (t)⊤x(t)= (cid:82)T(p˙ (τ)⊤x(τ)+p (τ)⊤x˙(τ))dτ.
1 1 t 1 1
twise linear input constraints. The corresponding feedback
Since p (T) = 0, substituting the dynamics x˙ = f (x,u )
Nash equilibria are characterized by a coupled system of 1 1 1
and by definition of p˙ in (6) gives
vector-valued ordinary differential equations. 1
We recall the notion of absolutely continuous (AC) func- −p (t)⊤x(t)= (cid:82)T(cid:2) −s⊤x(τ)+(r +B⊤p (τ))⊤K x(τ)
1 t 1 1 1 1 1
tion before stating the main result of this section. +p (τ)⊤B u (τ) (cid:3) dτ.
1 1 1
Definition 3. The function γ :[a,b]→R is absolutely con-
Adding and subtracting r⊤u inside the integral yields
tinuous if, for all ϵ>0, there exists δ>0 such that for 1 1
each finite collection (cid:8) (a ,b ),...,(a ,b ) (cid:9) of disjoint open p (t)⊤x(t)= (cid:82)T(cid:2) (s⊤x(τ)+r⊤u (τ))−r⊤u (τ)
1 1 n n 1 t 1 1 1 1 1
i t n h t a e t rv (cid:80) al n sco |γ nt ( a b in ) e − d γ in (a [a ) , | b < ]w ϵ i . th (cid:80)n i=1 (b i −a i )<δ,itfollows −p 1 (τ)⊤B 1 u 1 (τ)−(r 1 +B 1 ⊤p 1 (τ))⊤K 1 (τ)x(τ) (cid:3) dτ.
i=1 i i
Equivalently,
The following theorem characterizes the feedback Nash
equilibrium in terms of absolutely continuous solutions of a C 1 (t,x,u 1 ,u∗ 2 )=p⊤ 1 (t)x(t) (8)
coupled ODE system, under the assumption that the entries + (cid:82)T[(r +B⊤p (τ))⊤(u (τ)+K (τ)x(τ))]dτ.
t 1 1 1 1 1
of the input gradients r +B⊤p , i=1,...,N are nonzero
i i i Under the admissible set −E x(t)≤u (t)≤E x(t),
almost everywhere. 1 1 1
u (t) seeks to minimize C . By Assumption 1 the
1 1
Theorem 2. Suppose that Assumption 1 and Assumption 2 closed-loop trajectory satisfies x(t) ≥ 0. Since
hold. Suppose also that there exist absolutely continuous r +B⊤p ̸=0 for almost every τ ∈[t,T], the input
1 1 1
functions p i :[0,T]→Rn, i=1,...,N satisfying u∗ 1 (t)=−diag(sign(r 1 +B 1 ⊤p 1 ))E 1 x(t) is the pointwise min-
imizer of (r +B⊤p (t))⊤u over the box [−E x(t),E x(t)]
−p˙ (t)=s +A⊤p (t)−K (t)⊤(r +B⊤p (t)) (6) 1 1 1 1 1 1
i i i i i i i where (r +B⊤p (t))⊤(u (t)+K (t)x(t))≥0. Integrating
− (cid:80) K (t)⊤B⊤p (t) 1 1 1 1 1
j̸=i j j i over [t,T] yields C 1 (t,x,u 1 ,u∗ 2 )≥p⊤ 1 (t)x(t), and equality is
almost everywhere, with p i (T)=0, K i (t)=diag(sign(r i + achieved when u 1 =u∗ 1 . The same logic applies to player
B pl i a ⊤ y p e i r (t i )) = )E 1 i ,. a .., n N d t s h a e ti e s n fy tr r ies + o B f ⊤ th p e ( i t n ) p ̸= ut 0 gr f a o d r i a e l n m ts os o t f e e v a e c r h y 2 eq . u H il e i n b c ri e u , m b . y [7, Definition 6.2] (u∗ 1 ,u∗ 2 ) is a feedback Nas ■ h
i i i
t∈[0,T]. Then the feedback laws
Remark 2. Note that the right-hand side of (6) is piecewise
u∗(t)=−K (t)x(t) (7) affine in p i , i=1,...,N. On each subinterval where every
i i
entryoftheinputgradientsr +B⊤p (t)̸=0,thematricesK
i i i i
define a feedback Nash equilibrium for the dynamic game are constant and the system reduces to an affine ODE. The
(4) and (5). Moreover, the cost incurred by player i is given right-hand sideis thenmeasurable int, continuous inp and
i
by p i (0)⊤x 0 , i=1,...,N. bounded by (cid:13) (cid:13)s i (cid:13) (cid:13)+ (cid:13) (cid:13)E i (cid:13) (cid:13) (cid:13) (cid:13)r i (cid:13) (cid:13)+( (cid:13) (cid:13)A (cid:13) (cid:13)+ (cid:80)N j=1 (cid:13) (cid:13)B j (cid:13) (cid:13) (cid:13) (cid:13)E j (cid:13) (cid:13))β
oneverycompactsetwith|p |≤β,forsomeβ >0,satisfying
Proof: We prove the result for the two-player case for i
the Carathe´odory conditions, which imply the existence of a
simplicity, the general case follows analogously. Assume
solution[21,Thm.5.1].Uniquenessineachsubintervalholds
that the coupled ODE system (6) admits a pair of AC
since the right-hand side is Lipschitz in p with constant
solutions (p (t),p (t)), t ∈ [0,T], satisfying (6) almost i
everywhere 1 and su 2 ch that every entry of r i +B i ⊤p i (t)̸=0 κ the = n ( f (cid:13) (cid:13) o A ll (cid:13) (cid:13) ow + s (cid:80) by N j= i 1 n (cid:13) (cid:13) d B uc j t (cid:13) (cid:13) i (cid:13) (cid:13) o E n j o (cid:13) (cid:13) v ) e . r G th lo e b n a o l n u -s n w iq i u tc e h n i e n s g s i o n n ter [ v 0 a , l T s. ]
for almost every t∈[0,T]. We verify that the feedback
laws defined in (7) constitute a feedback Nash equilibrium. The following example illustrates a solution that is not
Fix any pair (t,x)∈[0,T]×Rn and the second player’s coveredbyTheorem2,wherer +B⊤p (t)=0onaninterval
i i i
equilibrium strategy u∗ 2 =−K 2 (t)x. The optimization prob- I ⊆[0,T] of positive measure.
lem of Player 1 has a running cost g (x,u )=s⊤x+r⊤u ,
1 1 1 1 1 Example 1. Consider A=0, B =B =1, E =0.5,
dynamics f (x,u )=(A−B K )x+B u and an admis- 1 2 1
1 1 2 2 1 1
(cid:8) (cid:9) E =0.4, r =r =−1, s =0.6, s =0.5, T =5,
sible set U (x)= u :|u |≤E x . Define the candi- 2 1 2 1 2
1 1 1 1
p (T)=0. The set of coupled ODEs (6) becomes
date value function V (τ,x)=p (τ)⊤x. Since p is AC i
1 1 1
by assumption, the right hand side of f 1 is measur- p˙ 1 (t)=−0.6+(p 1 (t)−1)K 1 (t)+p 1 (t)K 2 (t) (9)
able in τ and continuous in x, and for every compact
p˙ (t)=−0.5+(p (t)−1)K (t)+p (t)K (t) (10)
set D⊂[0,T]×Rn×Rm with |x|≤α1, for some α>0, 2 2 2 2 1
|f |≤κα1foralltand|f (x,u )−f (y,u )|≤κ|x−y|with with K (t)∈0.5sign(p (t)−1), K (t)∈0.4sign(p (t)−1).
1 1 1 1 1 1 1 2 2
(cid:13) (cid:13) (cid:13) (cid:13)(cid:13) (cid:13) (cid:13) (cid:13)(cid:13) (cid:13)
κ=((cid:13)A(cid:13)+(cid:13)B 2(cid:13)(cid:13)E 2(cid:13)+(cid:13)B 1(cid:13)(cid:13)E 1(cid:13)). By the Carathe´odory Assume p
2
(t)=1 and p
1
(t)≥1 on an interval I ⊆[0,T] so
existenceanduniquenesstheorems[21,Thm.5.1,Thm.5.3] that the input gradient is zero on a set of positive measure.

Carathe´odory notion of solution, we assume that switching
of the active set occurs only at isolated times forming a
set of measure zero. Let S (t)=diag(sign(r +B⊤p (t))).
i i i i
Since the discrete active set S (t) depends on the implicitly
i
unknown state p (t), we employ an implicit Backward Euler
i
discretization coupled with a fixed-point active-set iteration.
Ateachtimestep,thealgorithmiteratesbetweensolvingfor
the p-vector and updating the control signs. Repeated sign
patterns detect cycling; the iterate is accepted if the discrete
residual is below tolerance, otherwise the computation is
terminated and may be repeated with a smaller time step.
B. Infinite Horizon
In the infinite-horizon setting, we restrict attention to
constant linear state-feedback strategies. This is motivated
Fig.1.PhasediagramofExample1illustratingtheswitching by the requirement of closed-loop stability to guarantee
surfaces Σ ={p =1} and Σ ={p =1}. finiteness of the cost, as well as by the fact that the single-
1 1 2 2
Recall that this case is not covered by Theorem 2, where it player LR problem admits a static optimal solution.
is assumed to be nonzero almost everywhere. From the sec- Denote u K (t)=−Kx(t), K ∈Rm×n. In this subsection
ond equation (10) p˙ (t)=0=−0.5+K (t), so K (t)=0.5. we are concerned with the dynamic game constituted by the
2 1 1
Thenp˙ =−1.1+(0.5+K (t))p .SinceK (t)∈[−0.4,0.4], dynamics (4) and the cost functions (5) as T →∞, i.e.
1 2 1 2
define β(t):=0.5+K 2 (t)∈[0.1,0.9]. Thus, any trajec- J (x ,u ,...,u )= (cid:82)∞(cid:0) s⊤x(t)+r⊤u (t) (cid:1) dt. (11)
tory satisfying p =1 and p˙ (t)=−1.1+β(t)p (t) with i 0 1 N 0 i i Ki
2 1 1
β(t)∈[0.1,0.9] is admissible. Moreover, because along under Assumptions 1 and 2.
p 2 (t)=1 the value of K 2 (t) is not uniquely defined, the In this case, a set of feedback strategies is admissible if
solutionfailstobeuniqueandthedynamicsaremoreappro- it belongs to the subset of state-feedback control laws that
priatelydescribedbyadifferentialinclusion[23],[24],which render the zero equilibrium of system (4) asymptotically
is beyond the scope of this work. Note that on I, different stable. In this context, the notion of E-stabilizability in
choices of K 2 (t) correspond to different trajectories for p 1 Definition 1, extended to the dynamic game setting, is
through the coupling term p 1 (t)K 2 (t), so non-uniqueness on relevant and necessary for the Nash equilibrium analysis.
one player’s feedback propagates to the other player’s ODE.
This behavior is illustrated in Figure 1, which shows the Assumption 3. We shall limit our set of permitted controls
phase diagram of the system. to the constant feedback strategies which are stabilizing.
(cid:110) (cid:111)
For approximating the backward ODE system, we next K := (K ,...,K ):A− (cid:80)N B K isHurwitz (12)
N 1 N i=1 i i
introduceafullyimplicitBackwardEuleractive-setscheme.
Remark 3. To verify the (E ,...,E )-stabilizability of the
1 N
Algorithm 1 Backward Euler with Active-Set Iteration tuple (A,B 1 ,...,B N ) with A being Metzler, by [17, Lem. 4]
it is necessary and sufficient to verify the feasibility of
Require: T,M,PT,ℓ ,ϵ with ∆t=T/M
max
PM ←PT, S i M ←diag(sign(r i +B i ⊤pM i )) Ax+ (cid:80)N i=1 B i u i ≤−1, −E i x≤u i ≤E i x, ∀i.
for k=M,...,1 do
P(0)←Pk, S(0)←Sk, ℓ←0 In the sequel, this stabilization constraint is imposed to
repeat Solve implicit Euler for P(ℓ+1): ensure the finiteness of the infinite-horizon integrals in (11).
(cid:16) (cid:17)
Q(ℓ)←I−∆t A⊤− (cid:80)N E⊤S(ℓ)B⊤ Note that in contrast to LQR, in the LR setting this assump-
j=1 j j j
for i=1,...,N do tion will impose restrictions on the design of the matrix E.
(cid:104) (cid:105)
p(ℓ+1)←(Q(ℓ))−1 pk+∆t(s −E⊤S(ℓ)r)
i i i i i i Definition 4 (Stationary Feedback Nash Equilibrium).
S i (ℓ+1)←diag(sign(r i +B i ⊤p( i ℓ+1))) Consider the dynamic game defined by the system (4)
end for and the cost function (11), for i = 1,...,N. An
ℓ←ℓ+1 admissible set of strategies (u K∗,...,u K∗), with
u if n S ti ( l ℓ) S ̸= (ℓ) S ∈ (ℓ− { 1 S ) (0 a ) n , d .. R ., e S s( ( P ℓ− (ℓ 1 ) ) , } S o (ℓ r )) ℓ > = ϵ, ℓ m re a t x urn Fail u st K at i ∗ io = na − ry K i ∗ f x ee a d n b d ac ( k K 1 ∗ N ,.. a ., sh K N ∗ e ) q ∈ uil K ib N ri , um 1 i c f on th st e it N u f t o es llowing a
Pk−1←P(ℓ), Sk−1←S(ℓ) inequalities hold
end for
return {Pk,Sk}M
k=0
J i (x 0 ,u K
1
∗,...,u K
i
∗,...,u K
N
∗)≤J i (x 0 ,u K
1
∗,...,u Ki ,...,u K
N
∗)
foralli,x andforeachadmissibleK ,i=1,...,N suchthat
0 i
Algorithm 1. As mentioned in Remark 2 for the (K∗,...,K ,...,K∗)∈K .
1 i N N

Theorem 3 states that the feedback Nash equilibria of real nonnegative vectors pˆ ,pˆ , satisfying the equations
1 2
theLRinfinite-horizonproblemarecharacterized,withinthe
0=s⊤+pˆ⊤A−(r⊤+pˆ⊤B )K −pˆ⊤B K∗ (14)
admissible class K by the solution of the equations 1 1 1 1 1 1 1 2 2
N
0=s⊤+pˆ⊤A−(r⊤+pˆ⊤B )K −pˆ⊤B K∗ (15)
2 2 2 2 2 2 2 1 1
0=s⊤ i +p⊤ i A−(r i ⊤+p⊤ i B i )K i ∗− (cid:80) j̸=i p⊤ i B j K j ∗, (13) suchthatbothA−B 1 K 1 −B 2 K 2 ∗ andA−B 1 K 1 ∗−B 2 K 2 are
Hurwitz.AlsobyLemma1,K ∈ diag(sign(r +B⊤pˆ))E
where K∗ ∈ diag(sign(r +B⊤p ))E . i i i i i
Definitio i n 5. A vector i tuple i ( i pˆ ,.. i .,pˆ ) with pˆ ∈Rn is a in nd (14 J ) i ( b x y 0 d ,u ia K g 1 ∗ ( , si u g K n 2 ( ∗ r ) + = B pˆ ⊤ ⊤ i pˆ x 0 ) , )E i = an 1 d , K 2. ∗ S i u n b e s q ti u t a u t t i i o n n g ( K 15 2 ∗ )
1 N i + 2 2 2 2 1
called a stabilizing solution of the coupled equations (13) by diag(sign(r +B⊤pˆ ))E , shows that (pˆ ,pˆ ) satisfies
1 1 1 1 1 2
ifeachpˆ satisfies(13)whereK ∈ diag(sign(r +B⊤pˆ))E the coupled set of algebraic equations (13). Furthermore,
i i i i i i
and the matrix A− (cid:80)N B K is Hurwitz. replacing K∗ by diag(sign(r +B⊤pˆ ))E in A−B K∗−
i=1 i i 1 1 1 1 1 1 1
B K shows that the matrix A−B K −B K is Hurwitz,
Theorem 3. Suppose Assumptions 1 and 2 hold, 2 2 1 1 2 2
which completes the proof. ■
(A,B ,...,B ) is (E ,...,E )-stabilizable in the sense of
1 N 1 N
Definition 1 and (pˆ ,...,pˆ ), pˆ ∈ Rn for all i is a set of Algorithm 2. The infinite-horizon equilibrium (13) is
1 N i +
computed via a fixed-point iteration on the sign struc-
stabilizing solutions of the algebraic equations (13) in the
T se h n e s n e ( o u f K D ∗ e , fi .. n ., i u tio K n ∗ 5 ) i w s i a th s K ta i t ∗ io ∈ na d ry iag fe ( e s d ig b n a ( c r k i N + a B sh i ⊤ e pˆ q i u )) il E ib i - . w tu e re co m ns a t t r r u ic c e t s, the in m iti a a t l r i i z x ed A( c w ℓ l ) i = th A S − i (0) (cid:80) = N j= I 1 . B A j S t j (ℓ i ) t E er j a , ti w on hic ℓ h ,
rium.Mor 1 eover,th N ecostincurredbyplayeribyplayingthis is Metzler by Ass 2. Provided it is Hurwitz (verifiable
equilibrium action is pˆ⊤x , i=1,...,N. by the linear program in Remark 3), we solve the lin-
Na C sh on e v q er u s i e li l b y r , iu if m, (u th K e 1 ∗ n i ,.. t . h 0 , e u r K e N ∗ e ) xis is ts a a s s t t a a t b io il n i a zi r n y g fe so ed lu b t a io c n k e S a i ( r ℓ+ s 1 y ) s = tem dia p g ( i (cid:0) ℓ s + ig 1 n ) ( = r i − + (A B ( c i ⊤ ℓ l ) p ) ( i − ℓ+ ⊤ 1 (cid:0) ) s ) i (cid:1) , − ro E w i ⊤ s S o i (ℓ f )r z i e (cid:1) ro an in d pu u t pd g a ra te -
(pˆ ,...,pˆ ) of the algebraic equations (13) in the sense of dient keep their sign as a selection rule (Remark 4). Over
1 N
Definition 5 such that K∗ ∈ diag(sign(r +B⊤pˆ))E . finitely many sign structures, the iteration either converges
i i i i i
to a selected stationary equilibrium or a cycle is detected.
Remark 4. The stationary feedback laws u K i ∗ = −K i ∗x V. SIMULATIONEXAMPLE:LARGE-SCALEGLOBAL
can be nonunique. Indeed, for any player i if there exists a
row j such that (r +B⊤p ) = 0, then all feedback gains
POLLUTIONGAME
i i i j
satisfying −(E ) ≤ (K ) ≤ (E ) lead to different sets To demonstrate the scalability and rich dynamic behavior
i j i j i j
of solutions (p ,...,p ) to (13), which may yield different of the proposed Linear Regulator framework, we simulate
1 N
a densely interconnected multinational pollution game. This
stabilizing solutions and hence different Nash equilibria.
game is inspired by many classical works in the literature
Proof: We provethe Theorem for thetwo-player case, the where cross-boundary pollution is modeled to capture the
general case follows analogously. effects of neighboring regions’ actions on the common
=⇒SupposethatAssumptions1,2hold,(A,B 1 ,...,B N )is resource’s pollution levels [25], [26], and recent works [27],
(E 1 ,...,E N )-stabilizable and (pˆ 1 ,pˆ 2 ) is a stabilizing solution [28]. We consider N =3 strategic players (e.g., multina-
of the algebraic system of equations (13). Fix u∗ =−K∗x tional companies) interacting over a global environment
2 2
with K 2 ∗ ∈ diag(sign(r 2 +B 2 ⊤pˆ 2 ))E 2 and consider the mini- discretized into n=30 zones, with each player managing
mization problem of player 1 m =20 industrial sectors. This game employs a dense
i
MetzlerdiffusionmatrixA(with diagonal entries of −1.0for
J
1
(x
0
,u
1
,u
K 2
∗)= (cid:82)
0
∞(cid:0) s⊤
1
x(t)+r
1
⊤u
1
(t) (cid:1) dt
localized environmental absorption and off-diagonal entries
of 0.03 capturing physical spillover) and dense input matri-
subject to x˙(t)=(A−B K∗)x(t)+B u (t), x(0) = x . By
2 2 1 1 0 ces B ∼U(0.1,1.0) (reflecting cross-border industrial foot-
assumption, the equation i
prints). A small constraint matrix E =0.0004 is chosen
i
0=s⊤+p⊤A−(r⊤+p⊤B )K −p⊤B K∗ to model regulatory standards applied to all players. The
1 1 1 1 1 1 1 2 2
players are assigned heterogeneous cost profiles where state
hasastabilizingsolutionpˆ 1 .Thus,byLemma1thisoptimal cost vectors s i >0 represent environmental cost sensitivities
control problem admits a solution. The optimal control law uniformly drawn from player specific ranges, while r <0
i
is given by u K 1 ∗ (t) ∈ −diag(sign(r 1 + B 1 ⊤pˆ 1 ))E 1 x(t) represent marginal economic profits of industrial emissions
and the corresponding minimum cost is pˆ⊤x . Hence, linearly spaced between player specific bounds. The result-
1 0
J
1
(x
0
,u
K
1
∗,u
K
2
∗)≤J
1
(x
0
,u
K1
,u
K
2
∗) for all admissible K
1
. ing finite-horizon dynamics exhibit asynchronous switching
An analogous argument applies to player 2. Therefore, between maximum emission and abatement in response to
(u K∗,u K∗) is a stationary feedback Nash equilibrium. the asymmetric global state and competitors’ actions. As
1 2
⇐=Supposethat(K∗,K∗)∈K isafeedbackNashequi- shown in Figure 3, Player 1, representing a high-yield
1 2 2
librium. By definition, J (x ,u∗ ,u∗ )≤J (x ,u ,u∗ ), economy (s ∈[1.5,2.5],r ∈[−50,−30]), prioritizes profit
1 0 K1 K2 1 0 K1 K2 1 1
J (x ,u∗ ,u∗ )≤J (x ,u∗ ,u ) for all x and for all switching to emissions in the horizon of the game. Player 2
2 0 K1 K2 2 0 K1 K2 0
admissible state feedback matrices K , K , such that modelsavulnerableregionwithsevereenvironmentalpenal-
1 2
(K∗,K )∈K and (K ,K∗)∈K . By Lemma 1 there exist ties(s ∈[2.0,4.0],r ∈[−40,−20])withmoderateeconomic
1 2 2 1 2 2 2 2

margins, which forces a delayed switching closer to end of REFERENCES
| the game. | Finally, | Player | 3   | acts as | an emerging |     | economy |                 |     |       |      |         |                 |         |
| --------- | -------- | ------ | --- | ------- | ----------- | --- | ------- | --------------- | --- | ----- | ---- | ------- | --------------- | ------- |
|           |          |        |     |         |             |     |         | [1] S. Clemhout | and | H. Y. | Wan. | Chapter | 23 Differential | games - |
with low environmental sensivity and economic margins Economicapplications. InHandbookofGameTheorywithEconomic
(s ∈[1.0,2.0],r ∈[−30,−10]), resulting in an intermediate Applications,volume2,pages801–825.Elsevier,1994.
3 3 [2] KG.Ma¨ler,A.Xepapadeas,andA.Zeeuw.Theeconomicsofshallow
| switching | regime. | Consequently, |     | the | global | pollution | state |        |                                         |     |     |     |     |     |
| --------- | ------- | ------------- | --- | --- | ------ | --------- | ----- | ------ | --------------------------------------- | --- | --- | --- | --- | --- |
|           |         |               |     |     |        |           |       | lakes. | EnvironResourceEcon26,page603–624,2003. |     |     |     |     |     |
in Figure 2 initially tracks the infinite-horizon steady-state [3] T. C. Reluga. Game theory of social distancing in response to an
decay, but exhibit a late-stage resurgence as players switch epidemic. PLoSComputationalBiology,6,2010.
|     |     |     |     |     |     |     |     | [4] C.Fershtman.Identificationofclassesofdifferentialgamesforwhich |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
to maximum emission near the terminal horizon. theopenloopisadegeneratefeedbackNashequilibrium. Journalof
OptimizationTheoryandApplications,55:217–231,1987.
50 [5] C.-Y.Chiu,J.Li,M.Bhatt,andN.Mehr.Towhatextentdoopen-loop
Finite Horizon
)x( etatS noitulloP Infinite Horizon andfeedbackNashequilibriadivergeingeneral-sumlinearquadratic
40
|     |     |     |     |     |     |     |     | dynamicgames?  |      | IEEEControlSystemsLetters,8:2583–2588,2024. |     |            |               |         |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ------------------------------------------- | --- | ---------- | ------------- | ------- |
|     |     |     |     |     |     |     |     | [6] T. Bas¸ar. | Time | consistency                                 | and | robustness | of equilibria | in non- |
30
cooperativedynamicgames.InDynamicPolicyGamesinEconomics,
20 volume 181 of Contributions to Economic Analysis, pages 9–54.
Elsevier,1989.
10
|     |     |     |     |     |     |     |     | [7] T. Bas¸ar | and G. | J. Olsder. | Dynamic | Noncooperative |     | Game Theory. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ---------- | ------- | -------------- | --- | ------------ |
SocietyforIndustrialandAppliedMathematics,Philadelphia,1999.
|     | 0.0 | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 3.0 |     |               |        |            |        |            |        |               |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------------- | ------ | ---------- | ------ | ---------- | ------ | ------------- |
|     |     |     |     |     |     |         |     | [8] T. Bas¸ar | and G. | J. Olsder. | On the | uniqueness | of the | Nash solution |
Time
|     |     |     |     |     |     |     |     | inlinear-quadraticdifferentialgames. |     |     |     | InternationalJournalofGame |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | -------------------------- | --- | --- |
Fig. 2. Trajectory of the 30 global pollution states. Theory,5:552–563,2013.
|     |     |     |     |     |     |     |     | [9] C.PossieriandM.Sassano. |     |     | Analgebraicgeometryapproachforthe |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --------------------------------- | --- | --- | --- |
computationofalllinearfeedbackNashequilibriainLQdifferential
)1u( slortnoC Finite Horizon games. In 2015 54th IEEE Conference on Decision and Control
|     | 0.50 |     |     |     |     | Infinite Horizon |     |                            |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | ---------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
|     | 0.25 |     |     |     |     |                  |     | (CDC),pages5197–5202,2015. |     |     |     |     |     |     |
0.00 [10] J. Engwerda. LQ Dynamic Optimization and Differential Games.
|     | −0.25 |     |     |     |     |     |     | Hoboken,NJ,USA:Wiley,2005. |     |              |                |     |              |        |
| --- | ----- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | ------------ | -------------- | --- | ------------ | ------ |
|     |       |     |     |     |     |     |     | [11] G. Kossioris,         | M.  | Plexousakis, | A. Xepapadeas, |     | A. de Zeeuw, | and K- |
−0.50
|     |                   |     |     |     |     |     |     | G.Ma¨ler.    | FeedbackNashequilibriafornon-lineardifferentialgames |         |             |     |          |              |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------------------------------------- | ------- | ----------- | --- | -------- | ------------ |
|     | )2u( slortnoC 0.4 |     |     |     |     |     |     |              |                                                      |         |             |     |          |              |
|     |                   |     |     |     |     |     |     | in pollution | control.                                             | Journal | of Economic |     | Dynamics | and Control, |
0.2
|     | 0.0 |     |     |     |     |     |     | 32(4):1312–1331,2008. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
T.P.Azevedo-Perdicou´lisandG.Jank.Linearquadraticnashgameson
|     | −0.2 |     |     |     |     |     |     | [12]                   |     |                                         |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --------------------------------------- | --- | --- | --- | --- |
|     |      |     |     |     |     |     |     | positivelinearsystems. |     | EuropeanJournalofControl,11(6):632–644, |     |     |     |     |
−0.4
2005.
)3u( slortnoC 0.4 [13] I. Ivanov, L. Imsland, and B. Bogdanova. Iterative algorithms for
0.2 computing the feedback nash equilibrium point for positive systems.
|     | 0.0 |     |     |     |     |     |     | InternationalJournalofSystemsScience,48(4):729–737,2017. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
−0.2 [14] J. Hofbauer and K. Sigmund. Evolutionary Games and Population
|     | −0.4 |     |     |     |     |     |     | Dynamics. | CambridgeUniversityPress,1998. |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --------- | ------------------------------ | --- | --- | --- | --- | --- |
0.0 0.5 1.0 1.5 2.0 2.5 3.0 [15] C.Yu,G.Tu,andF.Yu.Researchontransboundaryairpollutioncon-
Time trolandcooperativestrategiesbasedondifferentialgame.Atmosphere,
15(12):1528,2024.
Fig. 3. Control inputs across 20 industrial sectors for the [16] A. Gurpegui, E. Tegling, and A. Rantzer. Minimax linear optimal
three multinational players. Asymmetric rewards and envi- control of positive systems. The IEEE Control Systems Letters (L-
CSS),7:3920–3925,2023.
| ronmental | sensitivities |     | trigger | staggered, | unaligned |     | switch- |                   |     |              |             |     |             |         |
| --------- | ------------- | --- | ------- | ---------- | --------- | --- | ------- | ----------------- | --- | ------------ | ----------- | --- | ----------- | ------- |
|           |               |     |         |            |           |     |         | [17] A. Gurpegui, |     | M. Jeeninga, | E. Tegling, | and | A. Rantzer. | Minimax |
ing. linear regulator problems for positive systems. IEEE Transactions
|     |     |     |             |     |     |     |     | onAutomaticControl,pages1–14,2026. |     |               |          |     | Inpress.         |      |
| --- | --- | --- | ----------- | --- | --- | --- | --- | ---------------------------------- | --- | ------------- | -------- | --- | ---------------- | ---- |
|     |     | VI. | CONCLUSIONS |     |     |     |     |                                    |     |               |          |     |                  |      |
|     |     |     |             |     |     |     |     | [18] D. Angeli                     | and | E. D. Sontag. | Monotone |     | control systems. | IEEE |
This paper studies a class of continuous-time general- TransactionsonAutomaticControl,48(10):1684–1698,2003.
|     |     |     |     |     |     |     |     | [19] T.Kaczorek. | Positive1Dand2DSystems. |     |     |     | SpringerLondon,2012. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------------------- | --- | --- | --- | -------------------- | --- |
sum non-cooperative games with linear costs, linear dynam- [20] W.G.KelleyandA.C.Peterson.TheTheoryofDifferentialEquations:
ics, and elementwise linear input constraints. In the finite- ClassicalandQualitative. SpringerScience&BusinessMedia,2010.
horizon case, under isolated switching regimes, sufficient [21] J.K.Hale. OrdinaryDifferentialEquations. Krieger,Malabar,1980.
|            |     |          |      |            |     |       |          | [22] W.Rudin.   | RealComplexAnalysis. |     |           | McGraw-Hill,1987. |              |         |
| ---------- | --- | -------- | ---- | ---------- | --- | ----- | -------- | --------------- | -------------------- | --- | --------- | ----------------- | ------------ | ------- |
| conditions | for | feedback | Nash | equilibria | are | given | by time- |                 |                      |     |           |                   |              |         |
|            |     |          |      |            |     |       |          | [23] J. Cortes. | Discontinuous        |     | dynamical | systems.          | IEEE Control | Systems |
varying feedback policies satisfying a system of vector- Magazine,28(3):36–73,2008.
|                 |     |             |                  |     |            |            |         | [24] R.B.VinterandP.R.Wolenski. |          |           | HamiltonJacobitheoryforoptimal |     |                   |        |
| --------------- | --- | ----------- | ---------------- | --- | ---------- | ---------- | ------- | ------------------------------- | -------- | --------- | ------------------------------ | --- | ----------------- | ------ |
| valued ODEs.    |     | In the      | infinite-horizon |     | case, the  | equilibria | are     |                                 |          |           |                                |     |                   |        |
|                 |     |             |                  |     |            |            |         | control                         | problems | with data | measurable                     | in  | time. Proceedings | of the |
| static feedback |     | stabilizing | policies,        |     | determined | by         | vector- |                                 |          |           |                                |     |                   |        |
28thIEEEConferenceonDecisionandControl,,pages293–295vol.1,
valuedalgebraicequations.Thisworkuncoversaninteresting
1989.
|         |               |         |               |             |             |            |           | [25] F.VanderPloegandA.deZeeuw.Adifferentialgameofinternational |     |                                            |           |     |             |                |
| ------- | ------------- | ------- | ------------- | ----------- | ----------- | ---------- | --------- | --------------------------------------------------------------- | --- | ------------------------------------------ | --------- | --- | ----------- | -------------- |
| dynamic | game          | setting | that inherits | the         | scalability |            | potential |                                                                 |     |                                            |           |     |             |                |
|         |               |         |               |             |             |            |           | pollutioncontrol.                                               |     | Systems&ControlLetters,17(6):409–414,1991. |           |     |             |                |
| of the  | LR framework, |         | while         | introducing |             | additional | and       |                                                                 |     |                                            |           |     |             |                |
|         |               |         |               |             |             |            |           | [26] S. Jørgensen                                               | and | G. Zaccour.                                | Incentive |     | equilibrium | strategies and |
compelling mathematical challenges, such as establishing a welfareallocationinadynamicgameofpollutioncontrol.Automatica,
37(1):29–36,2001.
| priori conditions |        | for     | the existence, | uniqueness, |     | and            | isolated |                                                                |       |            |              |     |            |            |
| ----------------- | ------ | ------- | -------------- | ----------- | --- | -------------- | -------- | -------------------------------------------------------------- | ----- | ---------- | ------------ | --- | ---------- | ---------- |
|                   |        |         |                |             |     |                |          | [27] C.WeiandC.Luo.Adifferentialgamedesignofwatershedpollution |       |            |              |     |            |            |
| switching         | of the | coupled | ODE            | solutions,  | and | characterizing |          |                                                                |       |            |              |     |            |            |
|                   |        |         |                |             |     |                |          | management                                                     | under | ecological | compensation |     | criterion. | Journal of |
the non-isolated switching case, which are natural directions CleanerProduction,274:122320,2020.
for future research. Other directions of future work involve [28] J. De Frutos, P. Lo´pez-Pe´rez, and G. Mart´ın-Herra´n. Equilibrium
strategiesinamultiregionaltransboundarypollutiondifferentialgame
deriving necessary conditions for the existence of feedback withspatiallydistributedcontrols. Automatica,125:109411,2021.
| Nash equilibria |     | and | applying | this framework |     | to models | of  |     |     |     |     |     |     |     |
| --------------- | --- | --- | -------- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
opioid epidemics.
---- END DOCUMENT ----
