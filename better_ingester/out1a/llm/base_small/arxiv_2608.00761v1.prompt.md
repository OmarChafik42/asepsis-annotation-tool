Below is a document converted to flat markdown. Its heading hierarchy was lost in conversion.

TASK: recover the section headings and their nesting depth. Use only headings that literally appear in the text — do not invent, and do not include running heads or figure captions. Drop any leading numbering from the title itself. Level 1 is a top-level section.

Output ONLY a JSON object of the form
  {"headings": [{"title": "...", "level": 1}, ...]}
in reading order, with no commentary before or after it.

---- DOCUMENT ----
| AI and | Exchange | Rate | Predictability |
| ------ | -------- | ---- | -------------- |
Amin Izadyar
| Imperial | College Business | School, Imperial | College London |
| -------- | ---------------- | ---------------- | -------------- |
Email:a.izadyar23@imperial.ac.uk
6202 guA 1  ]NG.nif-q[  1v16700.8062:viXra
August 4, 2026

Abstract
I revisit the exchange rate disconnect puzzle, first documented by Meese and Rogoff
(1983),usinggenerativeartificialintelligence(AI)toforecastcurrencyreturnsbasedon
economic fundamentals. Using ChatGPT and DeepSeek, I analyze a comprehensive
dataset of economic data releases for major currency pairs and measure the funda-
mental strength of each currency. These AI-powered fundamentals exhibit significant
cross-sectional predictive power. A simple trading strategy that goes long currencies
with strong fundamentals and short currencies with weak fundamentals generates a
Sharpe ratio exceeding 0.7 per annum. The excess returns of this strategy remain
significant after controlling for traditional currency factors. To mitigate concerns of
look-ahead bias, I run multiple exercises to ensure that predictability stems from AI
reasoning rather than memorization. Finally, I explore the potential sources of pre-
dictability and find evidence that the Taylor rule framework, generally used by central
banks to set interest rates, is a key mechanism connecting exchange rates to economic
fundamentals.
Keywords: Foreign Exchange, Return Predictability, Large Language Models, ChatGPT,
Artificial Intelligence
JEL Classification: C53, F31, F37, G12, G15.

1 Introduction
The ability of economic fundamentals to forecast exchange rates remains elusive, since mod-
els based on fundamentals are often outperformed by a simple random walk, a phenomenon
known as the “exchange rate disconnect” puzzle (e.g., Meese and Rogoff, 1983). Although
the recent literature has identified a few economic variables that appear to have predictive
power, the answer to this empirical puzzle remains unresolved (e.g., Mark, 1995; Engel and
West, 2005; Rossi, 2013).
Against this backdrop, the emergence of artificial intelligence (AI) offers new opportunities
to re-examine this puzzle. AI’s recent advancements have enabled it to solve problems once
considered too complex or data-intensive for traditional methods. Motivated by these devel-
opments, I leverage AI’s reasoning power and proficiency in handling large datasets to study
a comprehensive dataset of economic data releases, covering over 500 indicators from 1996
to 2024 for major economies. This study aims to find a link between exchange rates and eco-
nomic fundamentals, thus enhancing our understanding of price discovery in the largest and
deepest financial market in the world. To preview my results, I find evidence that AI-derived
fundamentals can predict future exchange rate returns and the most important predictors
are Inflation data, Employment data, and Broad economic activity indicators.
Usinglargelanguagemodels(LLMs)likeGPT-4oandDeepSeek-V3, Ianalyzealargedataset
comprising realized values, previous figures, and consensus forecasts of key economic data
releases, such as GDP reports, employment statistics, inflation indices, and central bank
decisions. I interact with the AI model using a structured prompt and ask it to generate
a concise analysis and a directional signal indicating whether the data release implies the
currency would STRENGTHEN, WEAKEN, or has an INSIGNIFICANT OR UNCERTAIN
impact. Notably, the input provided to the model includes only the realized, previous, and
forecast values, along with the name of the currency associated with the data release, exclud-
inganyinformationaboutthetimeordateoftherelease. UsingAI’soutput, Ithenconstruct
a simple measure, called the AIFX index, that captures the net fundamental strength of each
currency. Specifically, for each currency, the AIFX index is defined as the difference between
the number of positive (directional signal as “STRENGTHEN”) and negative (“WEAKEN”)
1

signals, divided by the total number of signals, over a given lookback window.
The AIFX index exhibits significant cross-sectional predictive power. A simple trading strat-
egy, called the AIFX strategy, that goes long currencies with a strong AIFX index and short
currencies with a weak AIFX index produces an annualized Sharpe ratio larger than 0.7.
Moreover, after controlling for traditional currency factors like dollar, dollar carry, carry,
momentum, and value, I uncover a statistically significant alpha that accounts for 74% of
the AIFX strategy’s average return. I further validate the result through a panel regression
exercise, showing that the AIFX index effectively predicts next month exchange rate returns.
Taken together, these findings suggest that AI can help uncover previously underexplored
sources of return predictability in the FX market, thus shedding light on the role of economic
fundamentals, as advocated by the theoretical literature.
I conduct multiple robustness checks to ensure the reliability of the baseline results. First,
while the main analysis uses GPT-4o to interpret data releases, I replicate the entire exercise
using DeepSeek V3 to test the sensitivity of the core findings to the choice of AI model. The
results remain consistent, with both models exhibiting very similar performance. Second, I
construct an alternative measure, the Weighted AIFX index, which assigns a weight to each
directional signal based on its estimated level of importance. I use this weighted index as
the signal in a cross-sectional trading strategy and find that the core results remain robust.
Third, I also implement a time-series trading strategy as an alternative to the cross-sectional
strategy used in the baseline specification. The time-series strategy also generates economi-
cally meaningful Sharpe ratios, and its performance remains significant after controlling for
benchmark currency factors.
A major concern when using LLMs for prediction tasks is look-ahead bias, which occurs
when a model is trained using information not available at the time of the prediction. As a
result, the model’s performance may look better than it would be in real-time. To mitigate
this concern, I implement four different exercises. In the first one, I investigate whether the
AI model may implicitly “remember” the timing of a data release. Specifically, I use the
same data that was fed to the AI model to generate the directional signals, but this time I
ask it to indicate the year (not the exact date) when the data was released. If the AI model
can recall the timing of the release, we should expect it to correctly identify the release year
2

in a high proportion of cases. However, the distribution of years guessed by the AI model
differs markedly from the true distribution of data releases in the dataset. I show that only
5.6% of the model’s guesses are correct on average within each year. In the second exercise, I
exploit the fact that the knowledge cut-off date for GPT-4o is October 2023, while for GPT-
3.5 it is September 2021. This two-year gap provides an opportunity to examine whether
the relative performance of the two models differs significantly. Specifically, I compare their
performance during the period from 1996 to 2021, covered by both models’ training sets, to
the period from 2021 to 2023, which only GPT-4o was trained on. If look-ahead bias were
present, we would expect a sharp decline in the relative performance of GPT-3.5 after its
training period ends, compared to GPT-4o. To test this, I conduct a difference-in-differences
analysis and find that the relative performance of the two models does not differ significantly
across the two periods. In the third exercise, I test for the possibility that the AI model may
have a memory of the overall relationship between exchange rate returns and certain macro-
variables. For example, if the model was trained during a period when inflation and currency
returns were positively correlated, it might predict higher exchange rates in response to ris-
ing inflation, based on memory and not reasoning. Therefore, I investigate whether the AI
model has a memory of the realized correlation of macro variables with next month currency
returns over the sample period, but find no evidence indicating so. In the fourth exercise,
I construct a portfolio based on what the AI model can remember about monthly currency
returns during the sample period, referred to as the pure hindsight portfolio, and use it as
a control factor. I find that the return of the AIFX strategy is orthogonal to the return of
the pure hindsight portfolio. Overall, these findings collectively suggest that the AI model’s
performance is unlikely to be driven by look-ahead bias, and should reflect genuine reasoning
based on the information available at the time of prediction.
After establishing the predictive power of the AI-derived variables, I investigate the under-
lying sources of this predictability. This step is crucial from an economic standpoint, as
it sheds light on the possible mechanisms through which fundamentals influence exchange
rate movements. First, I find that Inflation data, Employment data, and Broad economic
activity indicators are the most important categories for forecasting exchange rates. These
variables are closely linked to the monetary policy framework proposed by Taylor (1993),
3

suggesting that central banks’ policy responses to economic conditions play a pivotal role
in exchange rate determination. This interpretation is supported by prior empirical stud-
ies such as Clarida and Waldman (2007), Molodtsova and Papell (2009), and Engel and
Wu (2024), which document the predictive power of Taylor-rule fundamentals for exchange
rates. Second, I find that the predictive signal is largely driven by positive news (news im-
plying currency appreciation) rather than negative news (implying depreciation). Further
analysis reveals that negative news tends to trigger a stronger immediate market reaction
than positive news, consistent with the findings of Andersen et al. (2003). As a result, neg-
ative news may leave less room for delayed exchange rate adjustments, thereby reducing
its predictive content at longer horizons. A plausible interpretation is that this asymmetry
in market reaction is partly driven by the way central banks implement monetary policy.
In particular, several studies have documented that monetary authorities tend to respond
more aggressively to negative output gaps than to positive ones, leading to a general bias
toward lower interest rates (Juan et al., 2004; Brüggemann and Riedel, 2011; Hofmann and
Bogdanova, 2012; Komlan, 2013). The political economy of monetary policy also reinforces
this asymmetric tendency. Rate hikes can be politically unpopular as they may slow the
economy or increase borrowing costs. This asymmetric policy stance can influence investors’
expectations, prompting stronger immediate reaction to negative news and contributing to
the asymmetric predictive power documented in this study. Taken together, the empirical
findings point to the importance of the Taylor rule and monetary policy in explaining ex-
change rate movements. Nonetheless, alternative explanations cannot be definitively ruled
out.
This research contributes to two strands of literature. The first involves the well-known “ex-
change rate disconnect” puzzle, first observed by Meese and Rogoff (1983). Their findings,
seen as shocking at the time, prompted a large literature that re-examined the robustness
of the results (Mark, 1995; Kilian, 1999; Cheung et al., 2005; Molodtsova and Papell, 2009).
However, the early empirical studies were inconclusive in addressing the puzzle. A notable
contribution in this context is Engel and West (2005), who offer a potential resolution. They
demonstrate analytically that exchange rates can be consistent with present value asset pric-
ing models and follow a process arbitrarily close to a random walk if certain conditions are
4

met. Following this, Engel et al. (2007) present a defense of exchange rate models by ar-
guing that a random walk model is a tough benchmark to beat and propose alternative
methods for evaluating the performance of exchange rate models. In addition, recent empiri-
cal studies suggest a connection between currency returns and countries’ external imbalances
(Gourinchas and Rey, 2007; Della Corte et al., 2012, 2016), sovereign risk (Augustin et al.,
2020; Della Corte et al., 2022, 2023), the output gap (Colacito et al., 2020), macroeconomic
uncertainty (Berg and Mark, 2018; Della Corte and Krecetovs, 2024), and unemployment
(Nucera, 2017). Notably, the pattern of predictability documented in this paper is consistent
with the findings of Dahlquist and Hasseltoft (2020), who examine how past trends in key
macroeconomic indicators, referred to as economic momentum, can predict currency returns.
This paper advances the existing literature by using a novel AI-powered methodology to an-
alyze an expanded set of economic indicators. This innovative approach helps uncover new
predictability patterns and provides new insights into exchange rate movements.
Second, this project adds to the body of literature on novel research methods in financial
economics that leverage generative AI. For example, Eisfeldt and Schubert (2024) conduct
a comprehensive survey of how this emerging technology can decrease the time and costs
associated with traditional research designs in finance while enabling novel analytical ap-
proaches. Emerging applications include generating data embeddings (Gabaix et al., 2024;
Kimetal.,2024),textclassification(Changetal.,2024;Krockenbergeretal.,2024),retrieval-
augmentedgeneration(Bartiketal.,2024;ChenandWang,2024), simulatingagentbehavior
(Horton, 2023; Fedyk et al., 2024; Hewitt et al., 2024), and hypothesis generation (Si et al.,
2024; Ludwig and Mullainathan, 2024). Specifically, the prompting technique employed in
this study is most similar to the approaches used in the following papers. Bybee (2023) uses
AI to generate economic expectations from historical news data spanning 120 years. In addi-
tion, Lopez-Lira and Tang (2024) and Chen et al. (2024) explore the ability of generative AI,
specifically ChatGPT, to predict stock price movements based on sentiments extracted from
business news headlines. In contrast to these papers, which focus on sentiment extraction
from textual data, this study does not aim to extract signals from text. Instead, it relies
on structured, numerical data, and the AI model is prompted to generate analysis based
on the numerical values of economic data releases. Overall, this paper contributes to the
5

existing literature by demonstrating AI’s capability to analyze large volumes of structured
data in the context of currency markets. In addition, it introduces new techniques to address
look-ahead bias.
Theremainderofthepaperisorganizedasfollows; Section2presentsthedata; Section3out-
lines the construction of the AI-powered variables; Section 4 evaluates the predictive power
of these variables; Section 5 investigates the issue of look-ahead bias; Section 6 explores
the underlying mechanisms driving the predictability; and Section 7 concludes. A separate
Internet Appendix provides additional results not included in the main body of this paper.
2 Data
I focus on G-10 currencies that include the United States dollar (USD), Euro (EUR),
Japanese yen (JPY), British pound sterling (GBP), Swiss franc (CHF), Canadian dollar
(CAD), Australian dollar (AUD), New Zealand dollar (NZD), Swedish krona (SEK), and
Norwegian krone (NOK). I limit my focus to these currencies because of the long history of
economic data releases available. To measure the economic fundamentals of each currency,
I have collected the economic calendar data from Investing.com. The economic calendar
aggregates key economic data releases, such as GDP reports, employment statistics, infla-
tion readings, central bank decisions, and other economic indicators (544 unique indicators),
across multiple countries. It provides, for each data release, the realized value, the previous
figure, and the consensus forecast. The dataset spans from January 1996 to October 2024
and comprises a total of 174,820 data points. Table 1 displays the number of observations
collected for each currency. In addition, I have collected end-of-day (London time) exchange
rates and one-month forward rates from Bloomberg. Notably, there are nine exchange rates
in the cross-section, and all rates are defined as the amount of U.S. dollars (USD) required to
purchaseoneunitofforeigncurrency(FCU).Table2reportssummarystatisticsforexchange
rate returns.
Table 1 and Table 2 about here
6

| 3 Analysing |                | Data | Releases |     |
| ----------- | -------------- | ---- | -------- | --- |
| 3.1 AI      | as a financial |      | Analyst  |     |
For each data release in the economic calendar data, I feed structured prompts, as in
Prompt 1, to GPT-4o using APIs. The prompt contains the title, realized value, previous
figure, and the consensus forecast of the data release and instructs the AI model to generate
a concise analysis and a directional signal indicating whether the data release implies the
currency would STRENGTHEN, WEAKEN, or has an INSIGNIFICANT OR UNCERTAIN
impact. In Prompt 1, {currency} will correspond to the currency associated with the data
release. Notably, I exclude any information about the time or date of the release.
Prompt: Forget all previous instructions. You are a financial analyst. You will be
given a news headline. Please analyze the news’s effect on {currency} and provide a brief
response. Then indicate whether this headline implies {currency} will STRENGTHEN,
WEAKEN, or have an INSIGNIFICANT OR UNCERTAIN effect. Generate the output
in this format: {(ANALYSIS: short analysis discussing the channel), (DIRECTION: one
| of STRENGTHEN, |     | WEAKEN, | INSIGNIFICANT | OR UNCERTAIN)} |
| -------------- | --- | ------- | ------------- | -------------- |
|                |     |         | Prompt        | 1              |
As illustrated in Example 1, Example 2, and Example 3, the output explains the mechanism
of how the release could affect the associated currency and indicates the potential direction
of change.
| • Currency: | AUD |     |     |     |
| ----------- | --- | --- | --- | --- |
• Input: News headline: Trade Balance (monthly), Actual: 4.502B, Forecast: 6.100B,
| Previous: | 7.180B |     |     |     |
| --------- | ------ | --- | --- | --- |
• Output: Analysis: The trade balance figure came in lower than both the forecast and
thepreviousmonth,indicatingasmallerthanexpectedsurplus. Thiscouldsuggestthat
exports have decreased or imports have increased more than anticipated, potentially
signaling weaker economic activity. A lower trade balance can negatively impact the
currency as it implies that fewer Australian dollars are demanded in international
markets to purchase Australian goods and services., Direction: WEAKEN.
|     |     |     | Example | 1   |
| --- | --- | --- | ------- | --- |
7

| • Currency: | CAD |     |     |     |
| ----------- | --- | --- | --- | --- |
• Input: News headline: GDP (MoM), Actual: 0, Forecast: 0.001, Previous: 0.006
• Output: Analysis: The Canadian GDP month-on-month growth rate is recorded
at 0%, which is below the forecast of 0.1% and significantly lower than the previ-
ous month’s 0.6%. This stagnation signals a slowdown in economic growth and may
dampen investor sentiment towards the Canadian dollar. As GDP is a key indicator
of economic health, a lower than expected performance can lead to expectations of a
more accommodative monetary policy from the Bank of Canada, potentially putting
| downward    | pressure | on the CAD., | Direction: | WEAKEN. |
| ----------- | -------- | ------------ | ---------- | ------- |
|             |          |              | Example    | 2       |
| • Currency: | GBP      |              |            |         |
• Input: News headline: CPI (MoM), Actual: 0.004, Forecast: 0.003, Previous: 0.002
• Output: Analysis: The Consumer Price Index (CPI) measures the change in the price
level of a basket of goods and services. A higher-than-expected CPI indicates increased
inflationary pressures. The actual CPI of 0.004 surpasses both the forecast of 0.003
and the previous value of 0.002. This suggests stronger inflationary trends, potentially
leading to expectations of tighter monetary policy by the Bank of England. Higher
interest rates generally lead to currency appreciation as they attract foreign investment
| seeking | higher returns., | Direction: | STRENGTHEN. |     |
| ------- | ---------------- | ---------- | ----------- | --- |
|         |                  |            | Example     | 3   |
To clarify the terminology, throughout this paper, I refer to data releases with the direction
labeled as STRENGTHEN in the output as positive news, those labeled as WEAKEN as
negative news, and those labeled as INSIGNIFICANT OR UNCERTAIN as neutral news.
Table 1 presents a detailed breakdown of the count and percentage of positive, negative,
and neutral news for each currency during the sample period, providing insights into the
| distribution | of outputs   | from the | AI model. |     |
| ------------ | ------------ | -------- | --------- | --- |
| 3.2 Variable | Construction |          |           |     |
I follow a simple and intuitive approach to construct three AI-powered variables. Suppose we
are at time t and let τ denote the lookback period. Therefore, the time interval L = (t−τ,t]
would be the lookback window at time t. Based on this, I construct the following variables
8

| for currency | c:       |       |        |             |         |         |             |        |     |
| ------------ | -------- | ----- | ------ | ----------- | ------- | ------- | ----------- | ------ | --- |
|              |          |       | Number | of positive | news    | related | to currency | c in L |     |
|              | Strength |       | =      |             |         |         |             |        | (1) |
|              |          | c,t,τ | Total  | number      | of news | related | to currency | c in L |     |
|              |          |       | Number | of negative | news    | related | to currency | c in L |     |
|              | Weakness |       | =      |             |         |         |             |        | (2) |
|              |          | c,t,τ | Total  | number      | of news | related | to currency | c in L |     |
−Weakness
|     |     |     | AIFX | = Strength |       |     |       |     | (3) |
| --- | --- | --- | ---- | ---------- | ----- | --- | ----- | --- | --- |
|     |     |     |      | c,t,τ      | c,t,τ |     | c,t,τ |     |     |
The Strength ratio captures the proportion of positive news, while the Weakness ratio mea-
sures the proportion of negative news. The AIFX index is defined as the net balance between
positive and negative news, providing a single composite metric of implied currency strength
| derived       | from AI-classified |     | data.      |     |     |     |     |     |     |
| ------------- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
| 4 Performance |                    |     | Evaluation |     |     |     |     |     |     |
In this section, I analyze the predictive power of the AI-derived variables. I begin by con-
structing cross-sectional trading strategies that use the AIFX index as the signal, evaluated
across a range of lookback periods. The performance of these strategies is then assessed
relative to common currency factors. To formally test the statistical significance of the
AIFX index in predicting future returns, I estimate panel regressions. To ensure robustness,
the entire analysis is replicated using DeepSeek-V3, a leading alternative to the baseline
model GPT-4o. Next, I introduce an alternative specification of the AI-powered variables
by weighting each data release according to its estimated economic importance. Finally,
I implement a time-series strategy based on the same signal and further decompose the
predictive component to isolate the role of U.S. dollar fundamentals.
| 4.1 Cross-sectional |     |     | Trading | Strategy |     |     |     |     |     |
| ------------------- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- |
I assess the predictive power of the AIFX index (as defined in Equation (3)), using stylized
cross-sectional trading strategies. Notably, to evaluate the sensitivity of performance to the
length of lookback window, I consider lookback periods of 1 to 60 months. Specifically,
for each choice of lookback period, currencies are sorted by their AIFX index at the end
of each month and I take long positions in the top two currencies with the highest AIFX
index and short positions in the bottom two with the lowest. I refer to this strategy as the
9

AIFX strategy. Figure 1 presents the annualized Sharpe ratios of the strategy across different
| lookback | periods. |     |     |        |     |         |      |     |     |
| -------- | -------- | --- | --- | ------ | --- | ------- | ---- | --- | --- |
|          |          |     |     | Figure |     | 1 about | here |     |     |
TheAIFX strategy consistentlyyieldspositiveSharperatiosacrossalllookbackperiods, with
economically significant performance in most cases. Predictive power appears particularly
strongforlookbackperiodsof36to60months. Additionally,Table3reportstheperformance
statistics of the AIFX strategy, including the mean, standard deviation, skewness, excess
kurtosis and first-order autocorrelation of returns. Figure 2 illustrates the dollar value of
an initial $1 investment in the AIFX strategy1. A visual inspection of the figure indicates a
generalupwardtrendinperformance, withgainsdistributedrelativelyevenlythroughoutthe
sample period. Figure 3 shows the portfolio composition over time. The strategy exhibits
moderateturnover,implyingthattransactioncostsareunlikelytosignificantlyerodereturns.
|     |     | Table |     | 3, Figure | 2   | and Figure | 3 about | here |     |
| --- | --- | ----- | --- | --------- | --- | ---------- | ------- | ---- | --- |
To further examine the performance, I run contemporaneous regressions based on:
|     |     | RX  | = α | +β Dollar |     | +β Dollar | Carry | +β Carry + |     |
| --- | --- | --- | --- | --------- | --- | --------- | ----- | ---------- | --- |
|     |     | t,τ | τ   | 1,τ       | t   | 2,τ       |       | 3,τ        |     |
t t
|     |     |     | β   | Momentum | +β  | Value | +ϵ    |     | (4) |
| --- | --- | --- | --- | -------- | --- | ----- | ----- | --- | --- |
|     |     |     | 4,τ |          | t   | 5,τ   | t t,τ |     |     |
where RX denotes the monthly excess return of the AIFX strategy with lookback period
t,τ
τ; Dollar is a long-only portfolio that takes equal-weighted long positions in all currencies;
Dollar Carry is a directional strategy that goes long (short) all currencies when the average
forward discount is positive (negative); Carry, Momentum, and Value are cross-sectional
strategies that rank currencies by their forward discount, previous month’s return, and five-
year return, respectively. The construction of currency factors is further detailed in Internet
Appendix A and their performance statistics are reported in Internet Appendix Table A.1.
| I report the | regression |     | results | of Equation |     | (4) in | Table 4. |     |     |
| ------------ | ---------- | --- | ------- | ----------- | --- | ------ | -------- | --- | --- |
1Tosavespace,Figure2alsodisplaysthecumulativereturnofastrategythatusesStrengthratio(defined
in Equation (1)) as the signal. This strategy will be discussed in Section 6.2.1.
10

Table 4 about here
ThefindingsindicatethattheAIFX strategy’sreturnsarenotfullyexplainedbythecommon
currency factors, and this conclusion holds across different lookback periods. For example,
with a 48-month lookback period, the strategy yields a statistically significant alpha that
accounts for 74% of the average return of the strategy, suggesting that only about one-
quarter of the return is subsumed by traditional currency factors. Notably, for lookback
periods of 54 and 60 months, the alpha becomes only marginally significant, as the Value
factor gains more explanatory power. Overall, the analysis presented in this section provides
strong evidence that the AIFX index possesses significant predictive power. These findings
suggest that AI can help uncover previously underexplored sources of return predictability in
theFXmarket, contributingtoarenewedconnectionbetweenexchangeratesandunderlying
economic fundamentals.
4.2 Panel Regression
To assess the statistical significance of the predictive power of the AIFX index, I estimate
the following panel regression model for each choice of lookback period:
R = α +β AIFX +ϵ (5)
c,t+1 t,τ τ c,t,τ c,t,τ
In Equation (5), R represents the monthly excess return of currency c at time t + 1,
c,t+1
and AIFX denotes the AIFX index for currency c at time t when the lookback period is
c,t,τ
set equal to τ. Observations for monthly returns are non-overlapping, and both R and
c,t+1
AIFX are measured at the end of calendar months. Accordingly, this regression examines
c,t,τ
whether the AIFX index of a currency at the end of a given month can predict the currency’s
return in the subsequent month. Time fixed effects (α ) are included to simulate a cross-
t
sectional setting where the focus is not on average returns, but rather on the cross-sectional
differences in currency returns. The primary coeﬀicient of interest is β, which captures the
predictive relationship between the AIFX index and future returns. Consistent with the
methodology in Section 4.1, I consider a range of lookback periods to investigate how the
predictive power of the AIFX index varies with the length of lookback window. Figure 4
11

presents the t-statistics associated with β from Equation (5) across different lookback peri-
ods. The results indicate that the predictive relationship is statistically significant for most
lookback periods. In addition, the t-statistic profile in Figure 4 resembles the Sharpe-ratio
pattern in Figure 1. Furthermore, Internet Appendix Figure A.1 displays the regression
results when spot returns, rather than excess returns, are used as the dependent variable.
While the coeﬀicient of AIFX is still statistically significant across a range of lookback pe-
riods, its predictive power is somewhat weaker than in the excess-return specification. The
findings of this section provide additional evidence that the AIFX index possesses predictive
ability for future exchange rate returns.
Figure 4 about here
4.3 GPT-4o vs DeepSeek-V3
The core analysis of this paper makes use of GPT-4o. As a robustness check, I also consider
DeepSeek-V3, a key competitor to GPT-4o. Figure 5 compares the Sharpe ratios of the
AIFX strategy constructed using GPT-4o and DeepSeek-V3. The results reveal similar per-
formance, with both exercises delivering comparable Sharpe ratios across different lookback
periods and exhibiting a consistent pattern. These findings provide supporting evidence that
the baseline results are robust to the choice of alternative AI models.
Figure 5 about here
4.4 Alternative ways of constructing the AIFX index
I now examine whether the results are robust to an alternative method for constructing the
AIFX index. In the core analysis, to construct the variables, I only consider the count of
positive, negative, or neutral news items. While this method is straightforward and easy
to interpret, it overlooks the heterogeneity in the economic significance of different data
releases. To address this limitation, I adopt an alternative approach that incorporates the
relative importance of each data release. Using Prompt 2, I further ask GPT-4o to assign a
numerical score from 1 to 100 indicating the magnitude of the expected impact of the data
12

release on the exchange rate. Example 4 and Example 5 illustrate this methodology in more
detail. The resulting score, scaled by 100, is then used as a weight for each data release in
| the construction | of the | variables. |     |     |
| ---------------- | ------ | ---------- | --- | --- |
Prompt: Forget all previous instructions. On a scale of 1 to 100, how big is the po-
tential impact of the data release on the currency? Provide a short explanation of your
reasoning. Generate the output in this format: {(ANALYSIS: short analysis discussing
| your reasoning), | (Score:      | a number  | between  | 1 and 100)} |
| ---------------- | ------------ | --------- | -------- | ----------- |
|                  |              |           | Prompt   | 2           |
| • Currency:      | CAD          |           |          |             |
| • Input:         | Data release | headline: | Core CPI | (YoY)       |
• Output: Analysis: The Core Consumer Price Index (CPI) is a critical indicator of
inflation, excluding volatile items like food and energy. A change in the Core CPI
can signal shifts in purchasing power and inflation trends, influencing the Bank of
Canada’s monetary policy decisions, such as interest rate adjustments. Such decisions,
in turn, can significantly impact the Canadian dollar’s strength. If the Core CPI shows
unexpected inflation, it could lead to speculation on rate hikes, strengthening CAD,
or if it suggests low inflation, it may lead to rate cuts, weakening CAD., Score: 85.
|             |     |     | Example | 4   |
| ----------- | --- | --- | ------- | --- |
| • Currency: | GBP |     |         |     |
• Input: Data release headline: U.K. Construction Output (YoY)
• Output: Analysis: The construction sector is a significant component of the U.K.
economy, but it is not the largest. A year-on-year increase or decrease in construc-
tion output can provide insights into economic health and potential future economic
conditions, which could impact investor confidence in the GBP. However, it is not
as impactful as major economic indicators like GDP, inflation, or employment data.
Thus, while it holds relevance, its direct influence on the GBP is moderate.), Score:
45.
|     |     |     | Example | 5   |
| --- | --- | --- | ------- | --- |
Similar to Section 3.2, I construct three AI-powered variables for currency c at time t and
13

| for a lookback |     | period   | of τ: |          |     |     |             |          |         |             |        |     |
| -------------- | --- | -------- | ----- | -------- | --- | --- | ----------- | -------- | ------- | ----------- | ------ | --- |
|                |     |          |       | Weighted |     | sum | of positive | news     | related | to currency | c in   | L   |
| Weighted       |     | Strength |       | =        |     |     |             |          |         |             |        |     |
|                |     |          | c,t,τ | Weighted |     | sum | of          | all news | related | to currency | c in L |     |
|                |     |          |       | Weighted |     | sum | of negative | news     | related | to currency | c in   | L   |
| Weighted       |     | Weakness |       | =        |     |     |             |          |         |             |        |     |
c,t,τ
|     |          |     |      |       | Weighted | sum      | of  | all news  | related | to currency | c in L |     |
| --- | -------- | --- | ---- | ----- | -------- | -------- | --- | --------- | ------- | ----------- | ------ | --- |
|     | Weighted |     | AIFX | =     | Weighted | Strength |     | −Weighted |         | Weakness    |        | (6) |
|     |          |     |      | c,t,τ |          |          |     | c,t,τ     |         |             | c,t,τ  |     |
Figure 6 compares the performance of the strategies based on the AIFX index and the
WeightedAIFXindex acrossarangeoflookbackperiods. Thefigureshowsthatincorporating
weights enhances the Sharpe ratios for nearly all lookback windows. This finding suggests
that the baseline strategy can be further improved by refining the specification of the input
variables. Moreover, the results demonstrate that the predictive performance of the strategy
is robust to alternative methods of constructing the AI-powered variables.
|     |             |     |            |     | Figure | 6 about |     | here |     |     |     |     |
| --- | ----------- | --- | ---------- | --- | ------ | ------- | --- | ---- | --- | --- | --- | --- |
| 4.5 | Time-Series |     | Strategies |     |        |         |     |      |     |     |     |     |
So far, I have worked with cross-sectional trading strategies based on the AIFX index. Here,
I consider time-series strategies based on the same signal to examine an alternative portfolio
formation approach. Let AIFX be the indicator for currency c and AIFX be the
|     |     |     |     | c,t,τ |     |     |     |     |     |     | US,t,τ |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ------ | --- |
corresponding value for the U.S. dollar. I then define the following variable:
|     |     |     |     | Diff AIFX |       | = AIFX |       | −AIFX |        |     |     | (7) |
| --- | --- | --- | --- | --------- | ----- | ------ | ----- | ----- | ------ | --- | --- | --- |
|     |     |     |     |           | c,t,τ |        | c,t,τ |       | US,t,τ |     |     |     |
For each choice of lookback period τ, at the end of each month t, I take a long position
in currency c if Diff AIFX is positive and a short position if negative. Thus, portfolio
c,t,τ
−1,
weights are either +1 or depending on the sign of the signal.2 Unlike the cross-sectional
strategy, which is dollar neutral, the time-series strategy may carry exposure to the dollar,
either positive or negative. Portfolios are then rebalanced every month. As in Section 4.1,
2Tomaintaincomparabilityinvolatilitywiththecross-sectionalstrategy,Iscalethesesign-basedweights
| by N, the | number | of currencies |     | included | in the | portfolio. |     |     |     |     |     |     |
| --------- | ------ | ------------- | --- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
14

I evaluate performance across lookback windows ranging from 1 to 60 months. Internet
Appendix Figure A.2 reports the Sharpe ratios of the time-series strategy that uses Diff
AIFX index as the trading signal. While the strategy exhibits somewhat lower Sharpe ratios
compared to its cross-sectional counterpart, performance remains economically meaningful
across a wide range of lookback periods. Notably, the predictive power of the signal is
stronger for longer lookback windows, particularly those between 45 and 60 months. To
further investigate the nature of time-series predictability, I decompose Diff AIFX index
into its components and examine AIFX and AIFX separately. Specifically, I follow the
c USD
same time-series portfolio formation approach, but in one case use AIFX as the trading
c
signal, and in the other, use AIFX . Internet Appendix Figure A.3 presents the Sharpe
USD
ratios of the two strategies. The results show that the strategy based on AIFX delivers
USD
economically significant Sharpe ratios, generally in the range of 0.4 to 0.5, across a wide
spectrum of lookback periods. In contrast, the strategy based on AIFX does not yield
c
Sharpe ratios significantly different from zero; moreover, the performance fluctuates in sign
across different lookback periods. These findings suggest that the time-series predictability
is primarily driven by AIFX . This may reflect either the dominant role of U.S.-related
USD
economic fundamentals relative to domestic fundamentals in forecasting currency returns,
or simply the greater availability of data related to U.S. fundamentals. In addition, Internet
Appendix B provides further insights by reporting the strategy’s cumulative returns, key
performance statistics, and the results of regressions of the strategy’s returns on benchmark
currency factors. To conclude, the findings of this section provide further evidence that the
AIFX index contains valuable predictive information, and that its predictive power is robust
across both cross-sectional and time-series settings.
5 Look-ahead Bias: Reasoning or Memorization?
A major concern when using LLMs for forecasting tasks is look-ahead bias, which occurs
when a model is trained using information not available at the time of prediction. This
can make the model’s performance appear better than it would be in real-time. To address
this concern, I design and implement four different tests to determine whether the model’s
performance reflects genuine reasoning or merely the recall of memorized information. First,
15

I investigate whether the model might implicitly “remember” the timing of a data release.
Second, I exploit the difference in knowledge cut-off dates between GPT-4o and GPT-3.5
to test for performance divergence in the post-training period of GPT-3.5. Third, I assess
whether the model has memorized the correlation between macroeconomic variables and
future currency returns. Finally, I construct a portfolio based entirely on what the AI model
remembersofcurrencyreturnsduringthesampleperiodanduseitasabenchmarktocontrol
| for predictive | signals | that are contaminated | by  | look-ahead | bias. |
| -------------- | ------- | --------------------- | --- | ---------- | ----- |
| 5.1 Guess      | the     | Year                  |     |            |       |
In the core analysis, I do not provide any information about the timing or date of the release
as part of the input. Nevertheless, there remains the possibility that the AI model could
infer the release date from the provided inputs. To test for this possibility, I conduct an
experiment using the same data that was originally fed into the AI model via Prompt 1, but
instead of asking for an economic analysis, I ask the model to identify the year (not the exact
date) in which the data release occurred. This exercise is implemented using Prompt 3.
Prompt: Forget all previous instructions. You are a financial analyst. You will be given
a news headline related to {currency}. The news headline was published sometime between
1996 and 2024 (inclusive). Based on the information available and your memory, indicate
the year this headline was published. Generate the output in this format: {(YEAR: a 4-
| digit number | indicating | the year)} |        |     |     |
| ------------ | ---------- | ---------- | ------ | --- | --- |
|              |            |            | Prompt | 3   |     |
If the AI model is indeed able to recall the timing of the release, we would expect it to
correctly identify the release year in a high proportion of cases. Figure 7 displays the number
of data releases published each year in the dataset, representing the true distribution of data
releases over time. In contrast, Figure 8 presents the distribution of GPT-4o’s year-level
guesses. It is evident that the model’s guessed distribution diverges significantly from the
| actual distribution | of  | data releases. |              |         |      |
| ------------------- | --- | -------------- | ------------ | ------- | ---- |
|                     |     | Figure         | 7 and Figure | 8 about | here |
To provide a more nuanced view of the model’s classification performance at the year level,
16

for each year y, I calculate three standard evaluation metrics commonly used in the machine
| learning | literature: |     |           |     |                 |     |          |     |     |
| -------- | ----------- | --- | --------- | --- | --------------- | --- | -------- | --- | --- |
|          |             |     |           |     | Correct guesses |     | for year | y   |     |
|          |             |     | Precision | =   |                 |     |          | ,   | (8) |
y
|     |     |     |        |     | Total instances | guessed       | as       | year y    |     |
| --- | --- | --- | ------ | --- | --------------- | ------------- | -------- | --------- | --- |
|     |     |     |        |     | Correct         | guesses       | for year | y         |     |
|     |     |     | Recall | =   |                 |               |          |           | (9) |
|     |     |     |        | y   | Total actual    | data releases |          | in year y |     |
2
|     |     |     |     | F1  | =   |     | .   |     | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | y 1 |     | 1   |     |      |
+
|     |     |     |     |     | Precisiony | Recally |     |     |     |
| --- | --- | --- | --- | --- | ---------- | ------- | --- | --- | --- |
Precision measures how accurate the model is when it predicts year y. That is, among all
y
instances the model guessed as year y, how many were actually correct. Recall measures
y
how well the model identifies instances from year y. It captures the proportion of actual data
releasesinyeary thatthemodelcorrectlyguessed. F1 istheharmonicmeanofprecisionand
y
recallforyeary, providingabalancedmeasurethataccountsforbothfalsepositivesandfalse
negatives. Internet Appendix Table A.4 reports a breakdown of the model’s classification
performance across years. On average, the model achieves a precision of 5.68%, a recall
of 4.17%, and an F1 score of 2.36%, which are all very low. Further analysis, reported in
Internet Appendix Figure A.5, investigates whether better classification performance (higher
F1 scores) coincides with stronger strategy performance and finds no evidence indicating
so. To conclude, the results of this section undermine the hypothesis that the AI model’s
predictivepowerstemsfrommemorizationbyshowingthatitssignalisnotdrivenbyimplicit
| knowledge   | of historical |       | release | dates. |            |     |     |     |     |
| ----------- | ------------- | ----- | ------- | ------ | ---------- | --- | --- | --- | --- |
| 5.2 Cut-off |               | Test: | GPT-4o  |        | vs GPT-3.5 |     |     |     |     |
Theknowledgecut-offdateforGPT-4oisOctober2023,whereasforGPT-3.5,itisSeptember
2021. This two-year gap offers a unique opportunity to examine whether the performance of
the two models diverges significantly based on their access to post-2021 data. To investigate
this, I compare the performance of GPT-4o and GPT-3.5 over two distinct subperiods: (i)
1996–2021, a period fully covered by both models’ training data, and (ii) 2021–2023, a
period included only in GPT-4o’s training set. If look-ahead bias is present, then GPT-3.5’s
performance should drop sharply after 2021, while GPT-4o maintains its predictive accuracy.
To implement this test, I feed both GPT-3.5 and GPT-4o two separate prompts: Prompt 4
17

and Prompt 5. These prompts are identical in structure to Prompt 1, but they explicitly
indicate the time period in which the data release occurred, either between January 1996
and September 2021 or between September 2021 and October 2023.
Prompt: Forget all previous instructions. You are a financial analyst. You will be given
a news headline which was published sometime between January 1996 and
September 2021. Please analyze the news’s effect on {currency} and provide a brief
response. Then indicate whether this headline implies {currency} will STRENGTHEN,
WEAKEN, or have an INSIGNIFICANT OR UNCERTAIN effect. Generate the output
in this format: {(ANALYSIS: short analysis discussing the channel), (DIRECTION: one
| of STRENGTHEN, |     | WEAKEN, |     | INSIGNIFICANT |        | OR  | UNCERTAIN)}. |     |     |
| -------------- | --- | ------- | --- | ------------- | ------ | --- | ------------ | --- | --- |
|                |     |         |     |               | Prompt | 4   |              |     |     |
Prompt: Forget all previous instructions. You are a financial analyst. You will be given
a news headline which was published sometime between September 2021 and
October 2023. Please analyze the news’s effect on {currency} and provide a brief
response. Then indicate whether this headline implies {currency} will STRENGTHEN,
WEAKEN, or have an INSIGNIFICANT OR UNCERTAIN effect. Generate the output
in this format: {(ANALYSIS: short analysis discussing the channel), (DIRECTION: one
| of STRENGTHEN, |     | WEAKEN, |     | INSIGNIFICANT |        | OR  | UNCERTAIN)} |     |     |
| -------------- | --- | ------- | --- | ------------- | ------ | --- | ----------- | --- | --- |
|                |     |         |     |               | Prompt | 5   |             |     |     |
Having obtained the outputs from both AI models across the two subperiods, I construct
the AIFX index, as defined in Section 3.2, for each currency on the last day of each calendar
month using a one-month lookback window. In the first exercise, I compute the monthly
correlation between the AIFX index values generated by GPT-3.5 and GPT-4o over the two
periods. Table 5 shows that the correlation between the two models’ outputs remains high
and largely stable across both periods, indicating no substantial shift in model behavior
after 2021. To further assess potential divergence in outputs, I implement a difference-in-
differences analysis as specified in Equation (11). In this setup, T is a treatment indicator
i
equal to 1 for GPT-4o and 0 for GPT-3.5, while After is a time indicator equal to 1 for
t
the period from September 2021 to October 2023 and 0 for the period from January 1996 to
×After
September 2021. The interaction term T captures the differential change in outputs
|             |            |      |       |           | i          | t        |         |      |      |
| ----------- | ---------- | ---- | ----- | --------- | ---------- | -------- | ------- | ---- | ---- |
| between the | two models |      | after | GPT-3.5’s | training   | cut-off. |         |      |      |
|             |            | AIFX | =     | β +β      | T +β After | +β       | T After | +ϵ   | (11) |
|             |            |      | i,t   | 0         | 1 i 2      | t        | 3 i     | t it |      |
18

If look-ahead bias were at work, we would expect the coeﬀicient β to be statistically sig-
3
nificant. However, as shown in Table 6, the interaction term is statistically insignificant
across specifications. These results suggest that GPT-3.5’s performance remains comparable
to GPT-4o even after its training window ends. That said, the relatively short length of the
two-year gap may limit the statistical power to detect small differences. Taken together, the
evidence from this analysis further supports the conclusion that the AI model’s predictive
power is not driven by look-ahead bias.
Table 5 and Table 6 about here
5.3 Correlations Between Macro Variables and Currency Returns
Another potential source of look-ahead bias may arise if the AI model has memorized general
patterns between exchange rate returns and macroeconomic variables, during its training pe-
riod. For example, suppose the model was trained on data in which inflation and currency
returns were positively correlated. In that case, it might predict higher exchange rates in
response to rising inflation, not through active reasoning, but by recalling historical associa-
tions. Therefore, I examine whether the AI model has a memory of the realized correlations
between key macroeconomic variables and future currency returns over the period from Jan-
uary 1996 to October 2023. This period spans the full sample used in this study and ends
at the knowledge cut-off date of GPT-4o. I focus on two macro variables: the monthly con-
sumer price index (CPI) and unemployment rate. Using Prompt 6, I ask the AI model to
reportthecorrelationbetweeneachmacrovariableandnext-monthcurrencyreturnsforeach
currency3. I run this prompt 1,000 times for each currency–macro variable pair to obtain a
distribution of the model’s estimated correlations.
Prompt: Forget all previous instructions. You are a financial analyst. Please indi-
cate what is the correlation between {country}’s {macro_variable} and next month {cur-
rency}USD returns over the period from January 1996 to October 2023. Do not include
any extra explanations in the output. Generate the output in this format: {(CORRELA-
TION: number indicating the correlation)}.
Prompt 6
3For this exercise, I only consider currencies with available monthly CPI and unemployment rate data.
19

Figure9andFigure10displaytheresultingdistributionsforGBP,alongsidethetruerealized
correlation values computed over the same period. If the AI model had a strong memory of
the historical co-movement between macro variables and currency returns, we would expect
its estimates to be narrowly concentrated and closely aligned with the true realized value.
However, the two figures reveal substantial variation across the model’s estimates, and the
means of the distributions are not aligned with the true realized values. Similar patterns are
observed across other currencies, although figures are not reported to save space. These find-
ings indicate that GPT-4o does not have a strong memory of the general correlation between
macroeconomic variables and future exchange rate returns, further mitigating concerns of
| look-ahead | bias.     |           |              |          |      |
| ---------- | --------- | --------- | ------------ | -------- | ---- |
|            |           | Figure    | 9 and Figure | 10 about | here |
| 5.4 Pure   | Hindsight | Portfolio |              |          |      |
In this subsection, I construct a portfolio based solely on what the AI model may remember
about historical currency returns. The aim is to isolate any performance that might arise
purely from memorization, rather than reasoning. Specifically, I use Prompt 7 to directly
ask GPT-4o whether each currency strengthened, weakened, or remained unchanged in a
| given month | of the | sample period. |     |     |     |
| ----------- | ------ | -------------- | --- | --- | --- |
Prompt: Forget all previous instructions. You are a financial analyst. Please indicate
whether the currency {currency} has STRENGTHENED, WEAKENED, or was UN-
CHANGED over the period from {start_date} to {end_date}. Do not include any extra
explanations in the output. Generate the output in this format: {(DIRECTION: one of
| STRENGTHENED, |     | WEAKENED, | UNCHANGED)}. |     |     |
| ------------- | --- | --------- | ------------ | --- | --- |
|               |     |           | Prompt       | 7   |     |
The output of this prompt reflects the model’s recollection of directional return movements,
independent of any economic analysis or reasoning. Using these outputs, I form a trading
strategy, referred to as the pure hindsight portfolio, by taking long positions in currencies
the model indicates will strengthen and short positions in those it indicates will weaken.
The portfolio is rebalanced at the end of each calendar month, same as the AIFX strategy.
Thisportfolioexhibitshighlypositivelyskewedreturns(skewnessof2.52), extremelyfattails
20

(excess kurtosis of 18.61), and delivers a Sharpe ratio of 0.914. Internet Appendix Figure A.6
displays the cumulative return of the portfolio over time. Notably, the cumulative return is
relatively flat prior to 2008, a period that is less represented in the AI model’s training data,
aswellasaftertheknowledgecut-offdatein2023. Incontrast,theportfolioperformsstrongly
between 2008 and 2023, with its best performance occurring during the 2008 financial crisis,
suggesting that the AI model is better able to recall return directions from this well-covered
period. The pure hindsight portfolio could serve as a good control for predictive signals
and the associated strategy returns that are contaminated by look-ahead bias. Therefore, I
regress the excess returns of the AIFX strategy on the excess returns of the pure hindsight
| portfolio, | as shown | in Equation    | (12):  |                          |     |      |
| ---------- | -------- | -------------- | ------ | ------------------------ | --- | ---- |
|            |          | RXAIFXstrategy |        | RXPurehindsightportfolio |     |      |
|            |          |                | = α +β |                          | +ϵ  | (12) |
|            |          | t,τ            | τ τ    | t                        | t,τ |      |
If the performance of the AIFX strategy were driven by memorized knowledge, we would
expecttoobservesignificantlypositivebetas,orstatisticallyinsignificantalphas. Inaddition,
I report the Information Ratio, defined in Equation (13), which measures the Sharpe ratio
of the component of strategy returns orthogonal to the benchmark:
α
|     |     | Information | Ratio = |                   |     | (13) |
| --- | --- | ----------- | ------- | ----------------- | --- | ---- |
|     |     |             |         | Standard error of | ϵ   |      |
t
The results, reported in Table 7, show that the intercept (α) is highly significant across
all lookback periods, while the beta (β) is negative and statistically significant. Moreover,
the reported information ratios are economically meaningful, ranging from 0.75 to 0.85.
These findings show that the AIFX strategy’s returns are not subsumed by those of the pure
hindsight portfolio. In fact, the negative beta suggests that the AIFX strategy may operate
in opposition to memorized return signals. Overall, this analysis provides further evidence
that the predictive signals identified by the AI model are not driven by look-ahead bias.
|     |     |     | Table 7 about | here |     |     |
| --- | --- | --- | ------------- | ---- | --- | --- |
4The performance statistics are for the period from January 1996 to October 2023
21

6 Mechanisms Underlying Predictability
In this section, I examine the underlying economic mechanisms. Understanding these mech-
anisms is essential, as it provides insight into how and why economic fundamentals influence
exchange rate movements. First, I study which category of fundamentals have more pre-
dictive power. Second, I explore the asymmetric predictive power of positive and negative
news. Finally, I propose and discuss a potential mechanism.
6.1 Predictive Power of Different Categories of Fundamentals
In this section, I examine which categories of economic fundamentals contribute most to ex-
change rate predictability. The dataset used in this study includes a broad array of economic
indicators, comprising 544 unique data series. Up to this point, the AI-powered variables
used to predict exchange rates have aggregated information from all these indicators. A nat-
ural next step is to assess the heterogeneous impact of economic fundamentals on currency
forecasting. To do this, I classify the data releases into eight distinct categories. This catego-
rization process can be viewed as a form of dimensionality reduction. The methodology used
to assign indicators to categories is detailed in Internet Appendix C. In addition, Table 8
presents the eight categories, along with representative examples of data releases included in
each category and the number of observations in the dataset for each group. To assess the
importance of each category, I follow a leave-one-out approach. Specifically, I re-estimate the
baseline cross-sectional strategy (AIFX strategy) multiple times, each time excluding one of
the eight categories from the construction of the AIFX index. I then compute the percentage
drop in the Sharpe ratio relative to the AIFX strategy. The intuition behind this procedure
is that a larger drop in Sharpe ratio indicates a greater contribution of that category to pre-
dictive performance5. This analysis is conducted for lookback periods ranging from 36 to 60
months, where the predictive power of the strategy is strongest. I then compute the average
percentage drop in Sharpe ratio across these lookback periods. The results are presented in
Figure 11. The figure reveals that Inflation data, Employment data, and Broad economic
5Analternativeapproachwouldbetoconstructthestrategyusingonlyonecategoryatatime. However,
this method would lead to significant variation in the number of observations across categories, making it
diﬀicult to draw meaningful comparisons. By contrast, the leave-one-out method ensures a more consistent
sample size across all exercises, thereby improving the comparability of the results.
22

activity indicators are the top three categories associated with the largest drops in Sharpe
ratio when excluded. Additionally, I find that the marginal contributions of other categories
are negative, in other words, excluding them leads to better performance. Notably, Figure 12
compares the performance of the AIFX strategy, constructed using all eight categories, with
an alternative strategy that uses only the top three categories: ‘Inflation data’, ‘Employment
data’, and ‘Broad economic activity indicators’. The figure shows a clear improvement in
performancewhenthestrategyisrestrictedtothesethreecategories. Specifically, theSharpe
ratios increase by approximately 40% on average, and in some instances, more than double.
The results provided in this section indicate the key role of ‘Inflation data’, ‘Employment
data’, and ‘Broad economic activity indicators’ in driving exchange rate predictability.
Table 8, Figure 11 and Figure 12 about here
6.2 Decomposing Predictability: Positive vs. Negative News
So far, I have examined the predictive power of the AIFX index. By construction, this
variable is composed of two components: (i) the Strength ratio (Equation (1)), which mea-
sures the proportion of positive news, and (ii) the Weakness ratio (Equation (2)), which
captures the proportion of negative news. In this section, I investigate the predictive power
of Strength ratio and Weakness ratio separately. First, I construct cross-sectional trading
strategies using each variable as the trading signal. Second, I estimate panel regressions
with future currency returns as the dependent variable and the Strength ratio and Weakness
ratio as explanatory variables. Third, I explore the reason behind the asymmetric predictive
power.
6.2.1 Cross-sectional Trading Strategies
I construct two sets of cross-sectional trading strategies, following the methodology of Sec-
tion 4.1. In the first set, I use the Strength ratio as the trading signal. For each choice of
lookback period, at the end of each month, currencies are sorted based on their Strength
ratio, and I take long positions in the top two currencies with the highest values and short
positions in the bottom two with the lowest. Portfolios are rebalanced at the end of each
calendar month. In the second set of strategies, I use the Weakness ratio as the signal and
23

follow the same procedure as before with the only difference that currencies are sorted in
reverse order. In other words, I go long the two currencies with the lowest Weakness ra-
tio and short the two with the highest. Figure 13 presents the annualized Sharpe ratios
of the two strategies across different lookback periods. The strategy based on the Strength
ratio consistently delivers economically meaningful performance, with Sharpe ratios exceed-
ing 0.5 in most cases. In contrast, the strategy based on the Weakness ratio exhibits weak
performance. Notably, for lookback periods greater than 16 months, the strategy tends to
misdirect predictions and generates slightly negative Sharpe ratios. These findings suggest
that the predictive power of the AIFX index is primarily driven by the Strength ratio. In
other words, positive news appear to possess more predictive signal than negative news in
| forecasting | exchange          | rate movements. |        |               |     |     |
| ----------- | ----------------- | --------------- | ------ | ------------- | --- | --- |
|             |                   |                 | Figure | 13 about here |     |     |
| 6.2.2       | Panel Regressions |                 |        |               |     |     |
Following a similar methodology to Section 4.2, I estimate the following panel regression
| model | for each choice | of lookback | period:     |             |             |      |
| ----- | --------------- | ----------- | ----------- | ----------- | ----------- | ---- |
|       | R               | = α         | +β Strength | +β Weakness | +ϵ          | (14) |
|       |                 | c,t+1 t,τ   | 1,τ         | c,t,τ 2,τ   | c,t,τ c,t,τ |      |
in Equation (14), R denotes the monthly excess return of currency c at time t + 1.
c,t+1
Accordingly, this regression framework examines whether the Strength ratio and Weakness
ratio of a currency at the end of a given month can predict the currency’s return in the
subsequent month. Therefore, we are interested in testing the statistical significance of β
1
and β . Figure 14 reports the t-statistics for β and β across different lookback periods. The
| 2   |     |     |     | 1 2 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
results reveal that β is statistically significant across nearly all specifications, whereas β is
|     |     | 1   |     |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- |
consistently insignificant. In other words, the Strength ratio reliably forecasts next-month
currency returns, while the Weakness ratio does not. These findings reinforce the earlier
conclusion that the predictive power of the AIFX index is primarily driven by positive news.
|     |     |     | Figure | 14 about here |     |     |
| --- | --- | --- | ------ | ------------- | --- | --- |
24

6.2.3 Further Investigation of the Asymmetric Predictive Power
In this part, I explore the answer to the question of why positive news, as captured by the
Strength ratio, carries more forward-looking information than negative news, as captured
by the Weakness ratio. A straightforward hypothesis is that the dataset may contain more
positive than negative news. A higher number of data points can increase the signal-to-noise
ratio, leadingtomorepredictivepower. Table1reportsthedistributionofpositive, negative,
and neutral news in the dataset. The table clearly shows that the news classifications are
fairly balanced, with no substantial skew toward positive or negative observations, thereby
refutingthishypothesis. Asecondhypothesisrelatestothepotentialsynchronizationofbusi-
ness cycles among G10 economies. If most countries in the sample experience downturns
or negative shocks simultaneously, then the incidence of negative news would be relatively
synchronized across currencies. As a result, the Weakness ratio would fail to generate suf-
ficient cross-sectional variation to differentiate between currencies, limiting its usefulness in
forecasting returns. Internet Appendix Figure A.7 presents the cross-sectional standard de-
viations for the AIFX index, Strength ratio, and Weakness ratio over time. The figure reveals
that all three series exhibit fairly similar levels of dispersion over time, suggesting that the
lack of cross-sectional variation in the Weakness ratio is not a plausible explanation. In the
third exercise, I compare the average realized returns on the release day6 across positive,
negative, and neutral news, as shown in Figure 15. On average, currencies appreciate by
1.92 basis points on days with positive news, depreciate by 0.28 basis points on days with
neutral news, and experience a considerably larger depreciation of 4.99 basis points on days
with negative news. Additionally, Internet Appendix Figure A.8 displays the average return
in a three-day event window that includes the day before, the day of, and the day after the
release. The results reveal a stronger immediate market reaction to negative news relative
to positive news. This asymmetry is consistent with the findings of Andersen et al. (2003),
who document stronger market reactions to negative economic surprises in the FX market
duringthe1992–1998period. Theresultsfromthesedailyreturnanalysessuggestaplausible
explanation for the asymmetry in predictive power: negative news induces a stronger and
6This analysis differs from the rest of the paper, which has focused exclusively on monthly data. More-
over, precise within-month release dates are only reliably available in the dataset from 2008 onward. As a
result, the daily analysis presented here is restricted to the post-2008 period.
25

more immediate exchange rate adjustment, thereby exhausting its informational content in
the short run. Consequently, the Weakness ratio, which aggregates negative news, carries
limited predictive power at the monthly horizon. On the other hand, positive news prompts
a more gradual adjustment, leaving room for further price (exchange rate) discovery. As a
result, the Strength ratio retains a greater degree of predictive content, helping explain why
it is the primary driver of the overall performance of the AIFX index.
Figure 15 about here
6.3 A Potential Mechanism
In this section, I propose and discuss a potential mechanism through which economic fun-
damentals influence exchange rates. The three categories found in Section 6.1 to have the
highest predictive power are Inflation data, Employment data, and Broad economic activity
indicators, all of which enter the monetary policy framework proposed by Taylor (1993). The
Taylor rule posits that central banks adjust short-term interest rates in response to devia-
tions in inflation from its target and to output gaps, measured by unemployment and broad
economic activity indicators. Under this framework, a higher inflation or a positive output
gap typically prompts monetary tightening, whereas lower inflation or a negative output gap
leads to easing. Such monetary policy adjustments affect interest rate differentials, thereby
influencing the attractiveness of holding a currency. Consistent with this, in Example 2 and
Example 3, the AI model explicitly evaluates economic news in terms of its likely effect on
monetary policy under a Taylor-type framework, and then based on that, infers the impact
onexchangerates. TheseobservationssuggestthattheAImodelincorporatesreasoningcon-
sistent with economic theory when interpreting fundamental news. In addition, empirical
evidence from previous literature supports the predictive power of Taylor-rule fundamen-
tals for exchange rates (Clarida and Waldman, 2007; Molodtsova and Papell, 2009). More
recently, Engel and Wu (2024) argue that as central banks became more independent and
credible in adhering to Taylor-type policies, exchange rates became more systematically tied
to economic fundamentals. They find that the explanatory power of exchange rate mod-
els has improved over time, particularly as inflation targeting and policy credibility have
strengthened. Taken together, these findings suggest that the Taylor rule framework is a key
26

mechanism through which economic fundamentals affect exchange rates, and that this mech-
anism is reflected both in the AI model’s reasoning and in the empirical results presented
in this paper. Furthermore, the asymmetric way central banks implement the Taylor rule
could explain the stronger market reaction to negative news, compared to positive news,
documented in Section 6.2.3. The original Taylor rule prescribes a linear and symmetric
policy response; however, various scholars have identified asymmetric tendencies in actual
monetary policy decisions (Juan et al., 2004; Brüggemann and Riedel, 2011; Komlan, 2013).
Notably, Hofmann and Bogdanova (2012) show that actual policy interest rates in both
advanced and emerging economies have often been lower than those prescribed by standard
Taylor rules. They attribute these deviations to the asymmetric tendencies of central banks.
Specifically, central banks cut rates quickly in downturns but raise them slowly or not at all
in booms. The political economy of monetary policy also reinforces this asymmetry. Rate
cuts are generally popular because they support growth and reduce unemployment, while
rate hikes can be politically unpopular as they may slow the economy or increase borrowing
costs. Even independent central banks are not immune to political pressures. For instance,
onseveraloccasions7, U.S.PresidentDonaldTrumppubliclycriticizedFederalReserveChair
Jerome Powell for not lowering interest rates, despite inflation remaining above the policy
target and no clear evidence of a negative output gap. If we accept this asymmetric tendency
in central banks’ behaviour, investors’ immediate and more pronounced reaction to negative
news, compared to positive news, could be rationalized. Specifically, investors rationally
anticipate that central banks will respond aggressively to negative news (implying an easing
of monetary policy and possible currency depreciation), prompting them to react strongly.
Conversely, they respond less strongly to positive news (implying a tightening of monetary
policy and possible currency appreciation), as they anticipate a more cautious reaction from
the central bank. To conclude, the empirical findings of this paper highlight the importance
of the Taylor rule and monetary policy in exchange rate determination. That said, I do
not rule out alternative explanations and leave a more formal investigation of competing
mechanisms to future research.
7Example of such political pressures reported by Bloomberg: www.bloomberg.com/news/articles/2025-
06-06/trump-pressures-fed-s-powell-to-cut-rates-a-full-point
27

7 Conclusions
This paper uses generative artificial intelligence (AI) to forecast currency returns from eco-
nomic fundamentals, offering fresh insights into the long-standing exchange rate disconnect
puzzle, originally documented by Meese and Rogoff (1983). Leveraging models like GPT-4o
andDeepSeek-V3,Ianalyzealargedatasetofeconomicdatareleasesformajorcurrencypairs
and construct AI-based variables that capture each currency’s underlying macroeconomic
strength. These AI-derived signals exhibit strong predictive power in both cross-sectional
and time-series settings, with performance robust to different lookback windows and alter-
native variable specifications. To ensure the reliability of these findings, I conduct a series
exercises that rule out look-ahead bias and demonstrate that the AI model’s performance
stems from genuine reasoning rather than memorized information. I also explore the mech-
anisms behind this predictability and provide evidence that monetary policy, particularly
the Taylor rule framework used by central banks to set interest rates, plays a central role
in linking economic fundamentals to exchange rate movements. Further investigating the
mechanisms driving this predictive power represents a promising avenue for future research.
In addition, this paper offers preliminary evidence that AI can act as a financial analyst.
Future work could explore this more deeply, in a spirit similar to Cao et al. (2024), who
show that an AI analyst, leveraging large-scale data and machine learning, can outperform
human analysts in forecasting stock returns.
28

References
Andersen, T. G., Bollerslev, T., Diebold, F. X., and Vega, C. (2003). Micro effects of
macro announcements: Real-time price discovery in foreign exchange. American
| Economic | Review, | 93:38–62. |     |     |     |
| -------- | ------- | --------- | --- | --- | --- |
Augustin, P., Chernov, M., and Song, D. (2020). Sovereign credit risk and exchange rates:
Evidence from CDS quanto spreads. Journal of Financial Economics, 137:129–151.
Bartik, A., Gupta, A., and Milo, D. (2024). The costs of housing regulation: Evidence from
generative regulatory measurement. Working Paper, University of Illinois at
Urbana-Champaign.
Berg, K. A. and Mark, N. C. (2018). Global macro risks in currency excess returns.
| Journal | of Empirical |     | Finance, | 45:300–315. |     |
| ------- | ------------ | --- | -------- | ----------- | --- |
Brüggemann, R. and Riedel, J. (2011). Nonlinear interest rate reaction functions for the
| U.K. Economic |     | Modelling, | 28:1174–1185. |     |     |
| ------------- | --- | ---------- | ------------- | --- | --- |
Bybee, J. L. (2023). The ghost in the machine: Generating beliefs with large language
| models. | Working | Paper, | University | of Chicago. |     |
| ------- | ------- | ------ | ---------- | ----------- | --- |
Cao, S., Jiang, W., Wang, J., and Yang, B. (2024). From man vs. machine to man +
machine: The art and AI of stock analyses. Journal of Financial Economics, 160:1–22.
Chang, A., Dong, X., Martin, X., and Zhou, C. (2024). AI (ChatGPT) democratization,
return predictability, and trading inequality. Working Paper, Washington University in
Saint Louis.
Chen, J., Tang, G., Zhou, G., and Zhu, W. (2024). ChatGPT, stock market predictability
and links to the macroeconomy. Working Paper, Washington University in Saint Louis.
Chen, M. A. and Wang, X. (2024). Displacement or augmentation? The effects of AI
innovation on workforce dynamics and firm value. Working Paper, Georgia State
University.
Chernov, M., Dahlquist, M., and Lochstoer, L. (2023). Pricing currency risks. Journal of
| Finance, | 78:693–730. |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
Cheung, Y.-W., Chinn, M. D., and Garcia Pascual, A. (2005). Empirical exchange rate
models of the nineties: Are any fit to survive? Journal of International Money and
| Finance, | 24:1150–1175. |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- |
Clarida, R. H. and Waldman, D. (2007). Is bad news about inflation good news for the
| exchange | rate? | Working | Paper, | Columbia | University. |
| -------- | ----- | ------- | ------ | -------- | ----------- |
Colacito, R., Riddiough, S. J., and Sarno, L. (2020). Business cycles and currency returns.
| Journal | of Financial |     | Economics, | 137:659–678. |     |
| ------- | ------------ | --- | ---------- | ------------ | --- |
Dahlquist, M. and Hasseltoft, H. (2020). Economic momentum and currency returns.
| Journal | of Financial |     | Economics, | 136:152–167. |     |
| ------- | ------------ | --- | ---------- | ------------ | --- |
29

Della Corte, P., Jeanneret, A., and Patelli, E. D. (2023). A credit-based theory of the
currency risk premium. Journal of Financial Economics, 149:473–496.
Della Corte, P. and Krecetovs, A. (2024). Current account uncertainty and currency
| premia. | Management | Science, | 70:5795–5815. |
| ------- | ---------- | -------- | ------------- |
Della Corte, P., Riddiough, S. J., and Sarno, L. (2016). Currency premia and global
| imbalances. | Review | of Financial | Studies, 29:2161–2193. |
| ----------- | ------ | ------------ | ---------------------- |
Della Corte, P., Sarno, L., Schmeling, M., and Wagner, C. (2022). Exchange rates and
| sovereign | risk. Management | Science, | 68:5591–5617. |
| --------- | ---------------- | -------- | ------------- |
Della Corte, P., Sarno, L., and Sestieri, G. (2012). The predictive information content of
external imbalances for exchange rate returns: How much is it worth? Review of
| Economics | and Statistics, | 94:100–115. |     |
| --------- | --------------- | ----------- | --- |
Eisfeldt, A. L. and Schubert, G. (2024). AI and finance. Working Paper, University of
| California | Los Angeles. |     |     |
| ---------- | ------------ | --- | --- |
Engel, C., Mark, N. C., West, K. D., Rogoff, K., and Rossi, B. (2007). Exchange rate
models are not as bad as you think. NBER Macroeconomics Annual, 22:381–473.
Engel, C. and West, K. (2005). Exchange rates and fundamentals. Journal of Political
| Economy, | 113:485–517. |     |     |
| -------- | ------------ | --- | --- |
Engel, C. and Wu, S. P. (2024). Exchange rate models are better than you think, and why
they didn’t work in the old days. Working Paper, University of Wisconsin.
Fedyk, A., Kakhbod, A., Li, P., and Malmendier, U. (2024). ChatGPT and perception
biases in investments: An experimental study. Working Paper, University of California
Berkeley.
Gabaix, X., Koijen, R. S. J., Richmond, R., and Yogo, M. (2024). Asset embeddings.
| Working | Paper, Harvard | University. |     |
| ------- | -------------- | ----------- | --- |
Gourinchas, P. and Rey, H. (2007). International financial adjustment. Journal of Political
| Economy, | 115:665–703. |     |     |
| -------- | ------------ | --- | --- |
Hewitt, L., Ashokkumar, A., Ghezae, I., and Willer, R. (2024). Predicting results of social
science experiments using large language models. Working Paper, Stanford University.
Hofmann, B. and Bogdanova, B. (2012). Taylor rules and monetary policy: A global ’great
| deviation’? | BIS Quarterly | Review, | September:37–49. |
| ----------- | ------------- | ------- | ---------------- |
Horton, J. J. (2023). Large language models as simulated economic agents: What can we
learn from homo silicus? Working Paper, Massachusetts Institute of Technology.
Juan, D., María-Dolores, P. R., and J., R.-M. F. (2004). Nonlinear monetary policy rules:
Some new evidence for the U.S. Studies in Nonlinear Dynamics & Econometrics, 8:1–34.
Kilian, L. (1999). Exchange rates and monetary fundamentals: What do we learn from
long-horizon regressions? Journal of Applied Econometrics, 14:491–510.
30

Kim, S., Ahn, Y.-Y., and Park, J. (2024). Labor space: A unifying representation of the
labor market via large language models. Working Paper, Indiana University.
Komlan, F. (2013). The asymmetric reaction of monetary policy to inflation and the
output gap: Evidence from Canada. Economic Modelling, 30:911–923.
Krockenberger, V., Saunders, A., Steffen, S., and Verhoff, P. (2024). CovenantAI - new
insights into covenant violations. Working Paper, New York University.
Lopez-Lira, A. and Tang, Y. (2024). Can ChatGPT forecast stock price movements?
Return predictability and large language models. Working Paper, University of Florida.
Ludwig, J. and Mullainathan, S. (2024). Machine learning as a tool for hypothesis
generation. Quarterly Journal of Economics, 139:751–827.
Mark, N. C. (1995). Exchange rates and fundamentals: Evidence on long-horizon
predictability. American Economic Review, 85:201–218.
Meese, R. A. and Rogoff, K. (1983). Empirical exchange rate models of the seventies: Do
they fit out of sample? Journal of International Economics, 14:3–24.
Molodtsova, T. and Papell, D. H. (2009). Out-of-sample exchange rate predictability with
taylor rule fundamentals. Journal of International Economics, 77:167–180.
Newey, W. K. and West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity
and autocorrelation consistent covariance matrix. Econometrica, 55:703–708.
Nucera, F. (2017). Unemployment fluctuations and the predictability of currency returns.
Journal of Banking and Finance, 84:88–106.
Rossi, B. (2013). Exchange rate predictability. Journal of Economic Literature,
51:1063–1119.
Si, C., Yang, D., and Hashimoto, T. (2024). Can LLMs generate novel research ideas? A
large-scale human study with 100+ NLP researchers. Working Paper, Stanford
University.
Taylor, J. B. (1993). Discretion versus policy rules in practice. Carnegie-Rochester
Conference Series on Public Policy, 39:195–214.
31

Figure 1. Sharpe Ratios
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
1 6 12 18 24 30 36 42 48 54 60
Lookback Period (Months)
oitaR
eprahS
dezilaunnA
This figure reports the annualized Sharpe ratios of cross-sectional strategies that use the AIFX index (defined in Equation (3)) as the
trading signal. I refer to this strategy as the AIFX strategy. For each choice of lookback period, currencies are sorted by their AIFX
index at the end of each month and I take long positions in the top two currencies with the highest AIFX index and short positions
in the bottom two with the lowest. Portfolios are rebalanced at the end of each calendar month. Lookback periods of 1 to 60 months
are considered. The sample period spans from January 1996 to October 2024, but returns start at different dates due to differences in
lookback periods.
32

|     |      |       | Figure | 2. Cumulative | Returns |     |     |
| --- | ---- | ----- | ------ | ------------- | ------- | --- | --- |
|     | AIFX | index |        |               |         |     |     |
3.5
| tnemtsevnI | Strength  | ratio  |     |     |     |     |     |
| ---------- | --------- | ------ | --- | --- | --- | --- | --- |
|            | Cut-off   | Date   |     |     |     |     |     |
|            | Recession | Period |     |     |     |     |     |
3
1$
laitinI 2.5
na
2
fo
eulaV
33
1.5
ralloD
1
|     | 0   | 5   |     | 0   | 5   | 0   | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   | 0   |     | 1   | 1   | 2   | 2   |
|     | 0   | 0   |     | 0   | 0   | 0   | 0   |
|     | 2   | 2   |     | 2   | 2   | 2   | 2   |
Date
The graph displays the Dollar value of an initial $1 investment in two cross-sectional strategies from January 2000 to October 2024. The
blue line uses the AIFX index (defined in Equation (3)) and the red line uses the Strength ratio (defined in Equation (1)) as the signal.
Both trading strategies have a lookback period of 48 months. The green shaded regions denote NBER recession periods. The vertical
dotted line marks GPT-4o’s knowledge cutoff date, October 2023, when its training data ends.

|     |     |     |     | Figure |     | 3. Portfolio |     | Composition |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | ------------ | --- | ----------- | --- | --- | --- | --- |
|     |     | AUD |     |        |     |              |     | CHF         |     |     | EUR |     |
|     | 1   |     |     |        |     | 1            |     |             |     | 1   |     |     |
noitisoP
|     | 0   |     |     |     |     | 0   |     |     |     | 0   |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     | −1  |     |     |     |     | −1  |     |     |     | −1  |     |       |
|     | 0   | 5 0 | 5   | 0 4 |     | 0   | 5 0 | 5   | 0 4 | 0   | 5 0 | 5 0 4 |
0 0 0 0 0 1 0 1 0 2 0 2 0 0 0 0 0 1 0 1 0 2 0 2 0 0 0 0 0 1 0 1 0 2 0 2
|     | 2 2 | 2   | 2 2 | 2   |     | 2 2 | 2   | 2   | 2 2 | 2 2 | 2 2 | 2 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | GBP |     |     |     |     |     | JPY |     |     | NZD |     |
|     | 1   |     |     |     |     | 1   |     |     |     | 1   |     |     |
noitisoP
|     | 0   |     |     |     |     | 0   |     |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
34
|     | −1  |     |     |     |     | −1  |     |     |     | −1  |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     | 0   | 5 0 | 5   | 0 4 |     | 0   | 5 0 | 5   | 0 4 | 0   | 5 0 | 5 0 4 |
0 0 0 0 0 1 0 1 0 2 0 2 0 0 0 0 0 1 0 1 0 2 0 2 0 0 0 0 0 1 0 1 0 2 0 2
|     | 2 2 | 2   | 2 2 | 2   |     | 2 2 | 2   | 2   | 2 2 | 2 2 | 2 2 | 2 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | SEK |     |     |     |     |     | CAD |     |     | NOK |     |
|     | 1   |     |     |     |     | 1   |     |     |     | 1   |     |     |
noitisoP
|     | 0   |     |     |     |     | 0   |     |     |     | 0   |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     | −1  |     |     |     |     | −1  |     |     |     | −1  |     |       |
|     | 0   | 5 0 | 5   | 0 4 |     | 0   | 5 0 | 5   | 0 4 | 0   | 5 0 | 5 0 4 |
|     | 0   | 0 1 | 1 2 | 2   |     | 0 0 | 1   | 1   | 2 2 | 0 0 | 1 1 | 2 2   |
2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0
|     |     | Date |     |     |     |     |     | Date |     |     | Date |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- |
This figure shows the positions taken in each currency over time for the AIFX strategy with a 48-month lookback period. A value of 1
−1
indicates a long position, 0 indicates no position, and indicates a short position. The performance is reported for the period from
| January 2000 | to October | 2024. The | green | shaded | regions | denote | NBER | recession | periods. |     |     |     |
| ------------ | ---------- | --------- | ----- | ------ | ------- | ------ | ---- | --------- | -------- | --- | --- | --- |

Figure 4. t-statistics
T-statistics
|     | 3.5 |     |     |     | (5%) | Significance | Level |
| --- | --- | --- | --- | --- | ---- | ------------ | ----- |
3
2.5
tats-T
2
1.5
35
1
0.5
0
|     |     | 1 6 | 12 18    | 24     | 30 36 42 | 48  | 54 60 |
| --- | --- | --- | -------- | ------ | -------- | --- | ----- |
|     |     |     | Lookback | Period | (Months) |     |       |
Thisfiguredisplaysthet-statisticsofβ inEquation(5). Theregressionisrepeatedfordifferentchoicesoflookbackperiod. Thisregression
examines whether the AIFX index of a currency at the end of a given month can predict the currency’s excess return in the subsequent
month. Standard errors are clustered at the currency and time level. The regression includes time fixed effects, although not reported
here. The sample period spans from January 1996 to October 2024, but returns start at different dates due to differences in lookback
| periods. The | dashed horizontal | line marks | the 5% statistical | significance | threshold. |     |     |
| ------------ | ----------------- | ---------- | ------------------ | ------------ | ---------- | --- | --- |

|     |     | Figure   | 5. Sharpe | Ratios | (GPT-4o | vs DeepSeek-V3) |     |     |
| --- | --- | -------- | --------- | ------ | ------- | --------------- | --- | --- |
|     |     | DeepSeek | V3        |        |         |                 |     |     |
|     |     | GPT      | 4o        |        |         |                 |     |     |
0.7
oitaR
0.6
eprahS
0.5
0.4
dezilaunnA
0.3
36
0.2
0.1
|     |     | 1   | 6 12 | 18 24    | 30     | 36 42    | 48 54 | 60  |
| --- | --- | --- | ---- | -------- | ------ | -------- | ----- | --- |
|     |     |     |      | Lookback | Period | (Months) |       |     |
This figure compares the Sharpe ratios of the AIFX strategy constructed using GPT-4o and DeepSeek-V3. In one strategy the AIFX
index (defined in Equation (3)) was constructed using GPT-4o’s outputs and in the other strategy, the AIFX index was constructed
using DeepSeek V3’s outputs. Both strategies are cross-sectional ones that use the AIFX index as the trading signal. For each choice of
lookback period, currencies are sorted by their AIFX index at the end of each month and I take long positions in the top two currencies
with the highest AIFX index and short positions in the bottom two with the lowest. Portfolios are rebalanced at the end of each calendar
month. Lookback periods of 1 to 60 months are considered. The sample period spans from January 1996 to October 2024, but returns
| start at different | dates due | to differences | in lookback | periods. |     |     |     |     |
| ------------------ | --------- | -------------- | ----------- | -------- | --- | --- | --- | --- |

Figure 6. Alternative Specification of the AIFX index
0.7
0.6
0.5
0.4
0.3
0.2
0.1
1 6 12 18 24 30 36 42 48 54 60
Lookback Period (Months)
oitaR
eprahS
dezilaunnA
Weighted
Unweighted
This figure reports the annualized Sharpe ratios of cross-sectional strategies that use the AIFX index (defined in Equation (3)) and
Weighted AIFX index (defined in Equation (6)) as the trading signal. For each choice of lookback period, currencies are sorted based on
the signal at the end of each month and I take long positions in the top two currencies with the highest signal value and short positions
in the bottom two with the lowest. Portfolios are rebalanced at the end of each calendar month. Lookback periods of 1 to 60 months
are considered. The sample period spans from January 1996 to October 2024, but returns start at different dates due to differences in
lookback periods.
37

Figure 7. Distribution of Data Releases
6991 7991 8991 9991 0002 1002 2002 3002 4002 5002 6002 7002 8002 9002 0102 1102 2102 3102 4102 5102 6102 7102 8102 9102 0202 1202 2202 3202 4202
5,000
4,000
3,000
2,000
1,000
0
Year
sesaeleR
ataD
cimonocE
fo
rebmuN
This figure shows the distribution of data releases in the dataset across years. The sample period spans from January 1996 to October
2024. The dataset is collected from Investing.com’s economic calendar data. The economic calendar for each currency lists the dates
and times of key economic releases, such as GDP reports, employment statistics, inflation readings, central bank decisions, and other
economic indicators.
38

|     |     |     | Figure | 8. Distribution |     | of AI’s Guesses |     |     |     |
| --- | --- | --- | ------ | --------------- | --- | --------------- | --- | --- | --- |
80,000
70,000
60,000
sesseuG
50,000
|     | fo  | 40,000 |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
rebmuN
30,000
39
20,000
10,000
0
|     |     | 6991 | 7991 8991 9991 0002 | 1002 2002 3002 4002 5002 | 6002 7002 8002 9002 | 0102 1102 2102 3102 4102 | 5102 6102 7102 8102 | 9102 0202 1202 2202 | 3202 4202 |
| --- | --- | ---- | ------------------- | ------------------------ | ------------------- | ------------------------ | ------------------- | ------------------- | --------- |
Year
This figure displays the distribution of GPT-4o’s guesses when tasked with identifying the year (not the exact date) in which each data
release occurred, using Prompt 3. This exercise serves as a test for potential look-ahead bias. In the experiment, I use the same inputs
originally provided to the AI model via Prompt 1, but instead of asking for an economic analysis, the model is asked to guess the year
| of the data | release. The | sample period | spans from | January 1996 | to October | 2024. |     |     |     |
| ----------- | ------------ | ------------- | ---------- | ------------ | ---------- | ----- | --- | --- | --- |

Figure 9. Distribution of AI’s Correlation Estimates
600
500
400
300
200
100
0
−0.25−0.2−0.15−0.1−0.05 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35
Correlation
ycneuqerF
GPT-4o Estimates
True Realized Value
Distribution of GPT-4o’s correlation estimates between the United Kingdom’s monthly CPI and next-month GBPUSD returns over the
period from January 1996 to October 2023, compared with the true realized correlation over the same period. The correlation estimates
were generated using Prompt 6, and the exercise was repeated 1,000 times to obtain the distribution.
40

| Figure | 10. Distribution |     | of AI’s | Correlation | Estimates |     |
| ------ | ---------------- | --- | ------- | ----------- | --------- | --- |
GPT-4o Estimates
600
|     |     |     |     |     | True Realized | Value |
| --- | --- | --- | --- | --- | ------------- | ----- |
500
400
ycneuqerF
300
41
200
100
0
| −0.4 | −0.3 | −0.2 | −0.1 |       |     |     |
| ---- | ---- | ---- | ---- | ----- | --- | --- |
|      |      |      |      | 0 0.1 | 0.2 | 0.3 |
Correlation
Distribution of GPT-4o’s correlation estimates between the United Kingdom’s monthly unemployment rate and next-month GBPUSD
returns over the period from January 1996 to October 2023, compared with the true realized correlation over the same period. The
correlation estimates were generated using Prompt 6, and the exercise was repeated 1,000 times to obtain the distribution.

Figure 11. Percentage Drop in Sharpe Ratio
39.79
40
35
30
25
20
15
10
5.07
5 3.92
0
−5
−7.66
−10 −9.06
−11.44
−10.84
−12.23
−15
Br A o c a t d i v E it c y o I n n o d m ic ic a C t o o r n s s u m R e e r t a S i e l n A ti c m ti e v n it t y & E U m ne p m l o p y l m o y e m nt e n & t D F a i t n a a S n p c e i c a u l l M at a i v r e ke I t n s d & ices I n P fl a ri t c i e o n I n & dices I n G te o r v e e s r t n R m a e t n e t s P & olic y I nter n a T t r i o a n d a e l M a I n n d u u f a s c t t r u i a r l i n A g ct & i vit y
Category
)tnecreP(
oitaR
eprahS
ni
porD
ThisfigurereportsthepercentagedropinSharperatiooftheAIFX strategy, followingaleave-one-outapproach. Specifically, thebaseline
strategy is re-estimated multiple times, each time excluding one of the eight categories from the construction of the AIFX index (defined
in Equation (3)). The reported values represent the average percentage drop in Sharpe ratio across lookback periods ranging from 36 to
60 months. The sample period spans from January 1996 to October 2024.
42

Figure 12. Performance of Selected Categories
1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
36 42 48 54 60
Lookback Period (Months)
oitaR
eprahS
dezilaunnA
Selected Categories
All Categories
The figures compares the performance of the AIFX strategy, constructed using all eight categories of data releases, with an alternative
strategythatusesonlythetopthreecategories: ‘Inflationdata’, ‘Employmentdata’, and‘Broadeconomicactivityindicators’. Thecross-
sectional strategy uses the AIFX index (defined in Equation (3)) as the trading signal. For each choice of lookback period, currencies are
sorted by their AIFX index at the end of each month and I take long positions in the top two currencies with the highest AIFX index
and short positions in the bottom two with the lowest. Portfolios are rebalanced at the end of each calendar month. Lookback periods
of 36 to 60 months are considered. The sample period spans from January 1996 to October 2024, but returns start at different dates due
to differences in lookback periods.
43

Figure 13. Sharpe Ratios (Strength ratio vs Weakness ratio)
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
−0.1
−0.2
−0.3
1 6 12 18 24 30 36 42 48 54 60
Lookback Period (Months)
oitaR
eprahS
dezilaunnA
Weakness ratio
Strength ratio
This figure reports the annualized Sharpe ratios of cross-sectional strategies that use the Strength ratio (defined in Equation (1)) and
Weakness ratio (defined in Equation (2)) as the trading signal. For the first strategy, for each choice of lookback period, currencies are
sorted based on their Strength ratio at the end of each month, and I take long positions in the top two currencies with the highest values
and short positions in the bottom two with the lowest. Portfolios are rebalanced at the end of each calendar month. In the second
strategy, I use the Weakness ratio as the signal but sort currencies in reverse order. Specifically, at the end of each month, I go long
the two currencies with the lowest Weakness ratio and short the two with the highest. The rebalancing schedule and lookback period
specifications remain the same as those in the strategy based on the Strength ratio. Lookback periods of 1 to 60 months are considered.
The sample period spans from January 1996 to October 2024, but returns start at different dates due to differences in lookback periods.
44

| Figure | 14.          | t-statistics | (Strength | ratio vs | Weakness | ratio) |     |
| ------ | ------------ | ------------ | --------- | -------- | -------- | ------ | --- |
| 4      | T-statistics | (Weakness    | ratio)    |          |          |        |     |
|        | T-statistics | (Strength    | ratio)    |          |          |        |     |
|        | (5%)         | Significance | Level     |          |          |        |     |
3
2
tats-T
1
0
45
−1
−2
| 1   | 6   | 12 18 | 24              | 30 36    | 42  | 48 54 | 60  |
| --- | --- | ----- | --------------- | -------- | --- | ----- | --- |
|     |     |       | Lookback Period | (Months) |     |       |     |
This figure displays the t-statistics of β and β in Equation (14). The regression is repeated for differentchoices of lookbackperiod. This
|     | 1   | 2   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
regression examines whether the Strength ratio and Weakness ratio of a currency at the end of a given month can predict the currency’s
excess return in the subsequent month. Standard errors are clustered at the currency and time level. The regression includes time fixed
effects, although not reported here. The sample period spans from January 1996 to October 2024, but returns start at different dates
due to differences in lookback periods. The dashed horizontal lines mark the 5% statistical significance threshold.

| Figure | 15. Average | Daily Returns |     |
| ------ | ----------- | ------------- | --- |
1.92
2
1
)stnioP
0
sisaB( −0.28
−1
snruteR
−2
−3
46
naeM
−4
−5
−4.99
| e   |     | al  | e   |
| --- | --- | --- | --- |
| v   |     |     | v   |
| ti  |     | t r | ti  |
| si  |     | u   | a   |
| o   |     | e   | g   |
| P   |     | N   | e   |
N
This figure compares the average realized returns on days associated with each type of news. Each of the data releases in the dataset is
labeled as positive, neutral or negative using the output of Prompt 1. Specifically, I refer to data releases with the direction labeled as
STRENGTHEN in the output as positive news, those labeled as WEAKEN as negative news, and those labeled as INSIGNIFICANT
OR UNCERTAIN as neutral news. The sample period for this exercise is from 2008 to 2024.

|     | Table | 1.  | Frequency | Table | of Data Releases |     |
| --- | ----- | --- | --------- | ----- | ---------------- | --- |
Thistabledisplaysthedistributionofdatareleasesforeachofthetenmajorcurrenciesincludedinthedataset,whichwassourcedfromInvesting.com’s
economiccalendardataspanningJanuary1996toOctober2024. ’Total’indicatestheoverallnumberofobservationsforeachcurrency,while’Positive,’
’Negative,’ and ’Neutral’ denote the classification of data releases by GPT-4o using Prompt 1, based on their impact on the currency’s returns. The
percentages in parentheses represent the proportion of each category relative to the total observations for that currency.
|     | Currency | Total   | Positive | (%) Negative | (%) Neutral | (%) |
| --- | -------- | ------- | -------- | ------------ | ----------- | --- |
|     | AUD      | 12,134  | 4,347    | 36 4,885     | 40 2,902    | 24  |
|     | CAD      | 12,652  | 4,462    | 35 4,837     | 38 3,353    | 27  |
|     | CHF      | 5,554   | 1,825    | 33 1,952     | 35 1,777    | 32  |
|     | EUR      | 13,698  | 4,097    | 30 4,550     | 33 5,051    | 37  |
|     | GBP      | 20,261  | 6,266    | 31 7,246     | 36 6,749    | 33  |
|     | JPY      | 17,846  | 5,736    | 32 6,760     | 38 5,350    | 30  |
|     | NZD      | 9,261   | 3,589    | 39 3,792     | 41 1,880    | 20  |
| 47  | NOK      | 4,864   | 1,509    | 31 1,547     | 32 1,808    | 37  |
|     | SEK      | 6,490   | 2,075    | 32 2,498     | 38 1,917    | 30  |
|     | USD      | 72,060  | 21,223   | 29 20,508    | 28 30,329   | 42  |
|     | ALL      | 174,820 | 55,129   | 32 58,575    | 33 61,116   | 35  |

|     |     |     | Table | 2. Summary |     | Statistics |     |     |     |     |
| --- | --- | --- | ----- | ---------- | --- | ---------- | --- | --- | --- | --- |
This table reports summary statistics for exchange rate returns. All rates are defined as the number of U.S. dollars (USD) required to purchase one
unit of foreign currency (FCU). Panel A presents statistics for excess returns, while Panel B shows statistics for spot returns. The reported statistics
include mean returns, standard deviation, skewness, excess kurtosis, first-order autocorrelation (AR(1)), and Sharpe ratios. All measures are based
on monthly returns, though means, standard deviations, and Sharpe ratios are annualized. The sample period spans January 1996 to October 2024,
| with the exception | of the EUR, | for which excess | return | data begin | in January | 1999.     |         |       |        |        |
| ------------------ | ----------- | ---------------- | ------ | ---------- | ---------- | --------- | ------- | ----- | ------ | ------ |
|                    |             | AUD              | CAD    | CHF        | EUR        | GBP       | JPY     | NZD   | NOK    | SEK    |
|                    |             |                  |        |            | Panel      | A. Excess | Returns |       |        |        |
|                    |             |                  | −0.141 | −0.953     | −1.105     | −0.182    | −3.873  |       | −1.325 | −2.080 |
| Mean               |             | 0.993            |        |            |            |           |         | 1.602 |        |        |
Standard deviation 11.916 8.199 9.812 9.393 8.410 10.352 12.353 11.347 10.765
|          |     | −0.379 | −0.486 |       | −0.073 | −0.337 |       | −0.265 | −0.196 |       |
| -------- | --- | ------ | ------ | ----- | ------ | ------ | ----- | ------ | ------ | ----- |
| Skewness |     |        |        | 0.186 |        |        | 0.446 |        |        | 0.024 |
Excess kurtosis 1.599 3.338 1.578 1.259 1.304 2.356 1.123 0.693 0.364
AR(1) 0.031 −0.064 −0.044 0.038 0.022 0.005 −0.014 0.010 0.036
Sharpe Ratio 0.083 −0.017 −0.097 −0.118 −0.022 −0.374 0.130 −0.117 −0.193
48
|     |     |     |     |     | Panel | B. Spot | Returns |     |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | ------- | --- | --- | --- |
Mean −0.437 −0.048 1.175 −0.603 −0.556 −1.220 −0.403 −1.825 −1.483
Standard deviation 11.864 8.193 9.779 9.257 8.399 10.344 12.337 11.308 10.722
|          |     | −0.421 | −0.501 |       | −0.126 | −0.343 |       | −0.282 | −0.216 |       |
| -------- | --- | ------ | ------ | ----- | ------ | ------ | ----- | ------ | ------ | ----- |
| Skewness |     |        |        | 0.164 |        |        | 0.492 |        |        | 0.001 |
Excess kurtosis 1.710 3.360 1.608 1.237 1.373 2.600 1.209 0.765 0.403
|        |       |        | −0.065 | −0.052 |        |        |        | −0.017 |        |        |
| ------ | ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| AR(1)  |       | 0.022  |        |        | 0.030  | 0.019  | 0.001  |        | 0.003  | 0.027  |
|        |       | −0.037 | −0.006 |        | −0.065 | −0.066 | −0.118 | −0.033 | −0.161 | −0.138 |
| Sharpe | Ratio |        |        | 0.120  |        |        |        |        |        |        |

|     |     | Table | 3. Performance | Statistics |     |     |
| --- | --- | ----- | -------------- | ---------- | --- | --- |
Thistablereportstheperformancestatisticsforthecross-sectionalstrategiesthatusetheAIFX index (definedinEquation(3))asthetradingsignal.
I refer to this strategy as the AIFX strategy. For each choice of lookback period, currencies are sorted by their AIFX index at the end of each month
and I take long positions in the top two currencies with the highest AIFX index and short positions in the bottom two with the lowest. Portfolios
are rebalanced at the end of each calendar month. Results are shown for different lookback periods. The statistics include mean returns, standard
deviation, skewness, excess kurtosis, first-order autocorrelation (AR(1)) and Sharpe Ratios. The measures are based on monthly returns, but means,
standard deviations and Sharpe ratios are annualized. The performance reported is from January 2001 to October 2024.
|          |           | 36 months | 42 months | 48 months | 54 months | 60 months |
| -------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Mean     |           | 4.060     | 4.261     | 4.354     | 3.603     | 3.197     |
| Standard | deviation | 7.031     | 7.056     | 7.335     | 7.341     | 6.840     |
|          |           | −0.086    |           | −0.152    | −0.137    | −0.480    |
| Skewness |           |           | 0.058     |           |           |           |
| Excess   | kurtosis  | 1.777     | 1.902     | 2.634     | 2.566     | 1.960     |
|          |           | −0.015    | −0.001    |           | −0.006    | −0.010    |
| AR(1)    |           |           |           | 0.008     |           |           |
| Sharpe   | Ratio     | 0.577     | 0.604     | 0.594     | 0.491     | 0.467     |
49

|     |     |     | Table |     | 4. Performance |     | Over | Benchmark |     | Factors |     |
| --- | --- | --- | ----- | --- | -------------- | --- | ---- | --------- | --- | ------- | --- |
This table presents the results from the contemporaneous regression specified in Equation (4), which examines whether the monthly returns of the
AIFX strategy can be explained by common currency factors. The results are reported for different lookback periods. Benchmark factors include
Dollar, Dollar Carry, Cross-sectional Carry, Cross-sectional One-month Momentum, and Cross-sectional Value strategies, as described in Internet
Appendix A. The performance reported is from January 2001 to October 2024. Newey and West (1987) standard errors are reported in parentheses.
| ***, **, | and * indicate | statistical | significance | at  | the 1%, | 5%, and 10% | levels, | respectively. |          |        |           |
| -------- | -------------- | ----------- | ------------ | --- | ------- | ----------- | ------- | ------------- | -------- | ------ | --------- |
|          |                |             |              |     |         | Return      | of      | the AIFX      | strategy |        |           |
|          |                |             |              | 36  | months  | 42 months   | 48      | months        | 54       | months | 60 months |
|          |                |             |              |     | 2.88**  | 2.88**      |         | 3.24**        |          | 2.40*  | 2.04*     |
Alpha
|     |     |          |       | (1.32) |         | (1.32)  |     | (1.32)  | (1.32)   |         | (1.20)   |
| --- | --- | -------- | ----- | ------ | ------- | ------- | --- | ------- | -------- | ------- | -------- |
| 50  |     |          |       |        | 0.10*   | 0.09*   |     |         |          |         |          |
|     |     | Dollar   |       |        |         |         |     | 0.09    |          | 0.06    | 0.06     |
|     |     |          |       | (0.05) |         | (0.05)  |     | (0.05)  | (0.05)   |         | (0.04)   |
|     |     | Dollar   | Carry |        | 0.14*** | 0.12*** |     | 0.16*** |          | 0.15*** | 0.17***  |
|     |     |          |       | (0.05) |         | (0.05)  |     | (0.05)  | (0.05)   |         | (0.04)   |
|     |     | Carry    |       |        | 0.29*** | 0.35*** |     | 0.33*** |          | 0.41*** | 0.41***  |
|     |     |          |       | (0.06) |         | (0.05)  |     | (0.06)  | (0.05)   |         | (0.05)   |
|     |     | Value    |       | −0.03  |         | −0.02   |     | −0.13** | −0.18*** |         | −0.18*** |
|     |     |          |       | (0.06) |         | (0.05)  |     | (0.06)  | (0.05)   |         | (0.05)   |
|     |     | Momentum |       | −0.03  |         | −0.07   |     | −0.05   | −0.06    |         | −0.02    |
|     |     |          |       | (0.05) |         | (0.05)  |     | (0.06)  | (0.05)   |         | (0.05)   |
|     |     | R2(%)    |       |        | 20.5    | 25.1    |     | 24.2    |          | 31.3    | 36.8     |
|     |     | N        |       |        | 286     | 286     |     | 286     |          | 286     | 286      |

|     | Table | 5. Correlations | of  | the AIFX | index |
| --- | ----- | --------------- | --- | -------- | ----- |
This table reports the correlation between the AIFX index (defined in Equation (3)) constructed using outputs from GPT-3.5 and GPT-4o. For each
currency,thetablepresentsthecorrelationofthesignalsacrosstwodistinctperiods: January1996toSeptember2021—whenbothmodelshadaccess
to training data—and September 2021 to October 2023—a period only included in GPT-4o’s training data.
|     | Currency | 1996 | - 2021 | 2021 - 2023 |     |
| --- | -------- | ---- | ------ | ----------- | --- |
|     | AUD      |      | 0.86   | 0.83        |     |
|     | CAD      |      | 0.81   | 0.89        |     |
|     | CHF      |      | 0.76   | 0.72        |     |
|     | EUR      |      | 0.87   | 0.94        |     |
|     | GBP      |      | 0.86   | 0.89        |     |
|     | JPY      |      | 0.81   | 0.79        |     |
|     | NZD      |      | 0.84   | 0.83        |     |
|     | NOK      |      | 0.74   | 0.67        |     |
| 51  | SEK      |      | 0.84   | 0.86        |     |

| Table | 6. Difference-in-Differences |     | Exercise |
| ----- | ---------------------------- | --- | -------- |
This table presents the results of the difference-in-differences analysis, described in Equation (11), investigating the differential output of the two
AI models GPT-3.5 and GPT-4o across two distinct periods: from January 1996 to September 2021, which is within both models’ training sets,
againsttheperiodfromSeptember2021toOctober2023,whichonlyGPT-4owastrainedon. T i representsthetreatment,whichisadummyvariable
assigned the value 1 for GPT-4o and 0 for GPT-3.5. Similarly, After t is a dummy variable that is 1 for the period from September 2021 to October
2023 and 0 from January 1996 to September 2021. T ∗After is the interaction term. The analysis uses two model specifications to check robustness.
i i
Column 1 does not cluster standard errors, while column 2 clusters standard errors on the currency level.
(1) (2)
| T   |     |     | 0.03*** 0.03*** |
| --- | --- | --- | --------------- |
i
(0.01) (0.01)
| After |     |     | −0.01 −0.01 |
| ----- | --- | --- | ----------- |
i
(0.02) (0.02)
×After
| T   |     |     | 0.01 0.01 |
| --- | --- | --- | --------- |
i i
52 (0.02) (0.01)
| Currency  | Fixed    | Effect | Y Y       |
| --------- | -------- | ------ | --------- |
| Clustered | Standard | Errors | N Y       |
| R2        | (%)      |        | 2.80 2.80 |
| #         | of Obs.  |        | 5958 5958 |

|     | Table | 7. Pure Hindsight |     | Portfolio |     | as  | Control | Factor |     |
| --- | ----- | ----------------- | --- | --------- | --- | --- | ------- | ------ | --- |
ThistablereportstheresultsforthecontemporaneousregressionspecifiedinEquation(12)whichexamineswhetherthemonthlyreturnsoftheAIFX
strategy can be explained by the pure hindsight portfolio. The pure hindsight portfolio is solely based on what the AI model may remember about
historical currency returns and uses the outputs of Prompt 7. The portfolio is rebalanced at the end of each calendar month, same as the AIFX
strategy. The results are reported for different lookback periods. The performance reported is from January 2001 to October 2024. Newey and West
(1987) standard errors are reported in parentheses. ***, **, and * indicate statistical significance at the 1%, 5%, and 10% levels, respectively.
|             |       |           | Return    |     | of the    | AIFX | strategy  |     |           |
| ----------- | ----- | --------- | --------- | --- | --------- | ---- | --------- | --- | --------- |
|             |       | 36 months | 42 months |     | 48 months |      | 54 months |     | 60 months |
| Alpha       |       | 5.52***   | 5.99***   |     | 6.06***   |      | 5.45***   |     | 5.09***   |
|             |       | (1.47)    | (1.48)    |     | (1.56)    |      | (1.57)    |     | (1.46)    |
| Beta        |       | −0.36***  | −0.44***  |     | −0.38***  |      | −0.38***  |     | −0.40***  |
|             |       | (0.09)    | (0.09)    |     | (0.10)    |      | (0.10)    |     | (0.09)    |
| Information | Ratio | 0.78      | 0.85      |     | 0.83      |      | 0.75      |     | 0.76      |
53
| R2(%) |     | 4.80 | 7.15 |     | 5.10 |     | 5.00 |     | 6.46 |
| ----- | --- | ---- | ---- | --- | ---- | --- | ---- | --- | ---- |
| N     |     | 298  | 292  |     |      | 286 | 280  |     | 274  |

Table 8. Categories Descriptive Table
The table presents the eight categories, along with representative examples of data releases included in each category and the number of observations
in the dataset for each group. The methodology used to assign data releases to categories is detailed in Internet Appendix C. The data releases are
sourced from Investing.com’s economic calendar data spanning January 1996 to October 2024.
Category Example Headlines Frequency
Unemployment Rate, Employment Change,
Employment and Unemployment
Participation Rate, Overtime Pay, Continuing Jobless 17,717
Data
Claims
Retail Sales, Westpac Consumer Sentiment, NAB
Consumer Sentiment, Retail or
Business Confidence, Michigan Consumer Sentiment, 31,129
Services Activity
Chain Store Sales
Exports, Imports, Trade Balance, Current Account,
International Trade 14,685
Terms of Trade Index
Building Approvals, HIA New Home Sales, AIG
Manufacturing, Industrial or
Manufacturing Index, Capacity Utilization Rate, 37,945
Construction Activity
Chicago PMI
PPI, CPI, Wage Price Index, Import Price Index, ISM
Inflation and Price Indices 36,753
Manufacturing Prices
Interest Rates, Monetary Policy,
Bank Lending, M2 Money Stock, Government Operating
Government Budget, or Bond 20,587
Balance, Fed’s Balance Sheet, Deposit Facility Rate
Issuance
Net Investment Flow, Mortgage Refinance Index, CFTC
Financial Markets and Speculative S&P 500 speculative net positions, Foreign Investments
21,227
Indices in Japanese Stocks, CFTC Gold speculative net
positions
Broad Economic Activity GDP, Labour Productivity, Corporate Profits, Non-farm
22,473
Indicators Productivity, Bankruptcy Filings
54

|              |     |             | Internet | Appendix |     |     |     |
| ------------ | --- | ----------- | -------- | -------- | --- | --- | --- |
| A Definition |     | of Currency |          | Factors  |     |     |     |
This section outlines the construction of benchmark FX strategies used throughout the
paper. These strategies follow standard practices in the empirical FX literature (Chernov
et al., 2023) and serve as controls to evaluate the performance of the AI-powered signals.
• Dollar: A long-only portfolio that takes equal-weighted long positions in all non-
USD currencies. This strategy captures the average performance of foreign currencies
| against | the U.S. | dollar. |     |     |     |     |     |
| ------- | -------- | ------- | --- | --- | --- | --- | --- |
• Dollar Carry: This strategy uses the average forward discount across all currencies
as the signal. It goes long (short) all currencies versus the USD when the average
| forward         | discount | is positive | (negative). |     |     |     |     |
| --------------- | -------- | ----------- | ----------- | --- | --- | --- | --- |
| Cross-sectional |          | Strategies  |             |     |     |     |     |
• Carry: This strategy uses each currency’s forward discount as an individual signal.
Currencies are ranked by their forward discount, and positions are assigned using rank-
| based weights |     | defined by: |     |     |     |     |     |
| ------------- | --- | ----------- | --- | --- | --- | --- | --- |
|               |     |             |     |     |     | !   |     |
XN
1
|     |     | wi  | = κ rank(zi | )−  | rank(zi | ) , | (A.1) |
| --- | --- | --- | ----------- | --- | ------- | --- | ----- |
|     |     |     | pt          | pt  | pt      |     |       |
N
i=1
| wi  |     |     |     | zi  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
where denotes the weight of currency i, is the forward discount signal, and κ
|     | pt  |     |     | pt  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
is a scaling constant that ensures the portfolio is USD-neutral. With N = 9, possible
| weights | are: ±0.4,±0.3,±0.2,±0.1,0.0. |     |     |     |     |     |     |
| ------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
zi
• Momentum: Constructed in the same way as Carry, but the signal is defined as
pt
| the excess | return | in the | most recent | month:  |     |     |     |
| ---------- | ------ | ------ | ----------- | ------- | --- | --- | --- |
|            |        |        |             | zi = Ri | .   |     |     |
|            |        |        |             | pt t−1  |     |     |     |
A-1

• Value: This strategy uses the five-year detrended FX rate as the signal:
|     |     |     |     | !   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | X6  | −1  |     |
1
|     |     |     | Qi e Qi | Qi        |     |       |
| --- | --- | --- | ------- | --------- | --- | ----- |
|     |     |     | =       |           | ,   | (A.2) |
|     |     |     | t t     | 13 t−60+j |     |       |
j=−6
e
where Qi denotes the FX rate. The signal Qi is then used with the rank-weighting
|             | t           |        |     | t   |     |     |
| ----------- | ----------- | ------ | --- | --- | --- | --- |
| scheme      | in Equation | (A.1). |     |     |     |     |
| Time-Series | Strategies  |        |     |     |     |     |
Time-series (TS) strategies rely on sign-based signals. At each rebalancing date, currencies
with a positive signal are held long, and those with a negative signal are held short, using
| the following | weight scheme: |     |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- | --- |
1
|     |     |     | wi = | sign(zi), |     | (A.3) |
| --- | --- | --- | ---- | --------- | --- | ----- |
|     |     |     | TS,t | t         |     |       |
N
where N is the number of currencies. This ensures that the volatility of time-series strategies
are comparable to cross-sectional strategies. The net USD exposure in not zero and varies
over time.
• TS-Carry: Uses the forward discount as the signal zi. Positions are taken according
t
| to Equation | (A.3). |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- |
• TS-Momentum: Uses the most recent monthly excess return Ri as the signal:
t−1
|     |     |     |     | zi Ri |     |     |
| --- | --- | --- | --- | ----- | --- | --- |
= .
t t−1
| Positions | are taken | according | to Equation | (A.3). |     |     |
| --------- | --------- | --------- | ----------- | ------ | --- | --- |
• TS-Value: Uses the five-year detrended FX rate defined in Equation (A.2) as the
signal:
e
zi Qi.
=
t t
| Positions | are taken | according | to Equation | (A.3). |     |     |
| --------- | --------- | --------- | ----------- | ------ | --- | --- |
All strategies are rebalanced monthly. Cross-sectional strategies are USD-neutral by con-
A-2

struction, while TS strategies may exhibit time-varying USD exposure depending on the
aggregate direction of the signals.
B Time-Series Strategy; Additional Results
This section provides further insights into the performance of the time-series strategy intro-
duced in Section 4.5. Internet Appendix Figure A.4 illustrates the cumulative returns of the
strategy over time, while Internet Appendix Table A.2 reports key performance statistics,
including the mean, standard deviation, skewness, excess kurtosis, and first-order autocor-
relation of returns. To assess whether the strategy’s returns can be explained by benchmark
time-series FX strategies, I estimate contemporaneous regressions similar to Equation (4).
The construction of the benchmark strategies is detailed in Internet Appendix A. The re-
gression results are presented in Internet Appendix Table A.3. The findings indicate that
the strategy’s returns are not fully explained by the benchmark currency factors, and this
conclusion holds across various lookback periods. For instance, with a 54-month lookback
window, the strategy generates a statistically significant alpha that accounts for approxi-
mately 69% of the average return of the strategy, implying that only about one-third of the
return is subsumed by the benchmark strategies.
C Categorization Procedure
This section outlines the methodology used to classify each data release in the dataset into
oneofeightcategories. Thesecategoriesaredesignedtorepresentdistinctgroupsofeconomic
fundamentals. The categories are: 1- Employment and Unemployment Data 2- Consumer
Sentiment, Retail, or Services Activity 3- International Trade 4- Manufacturing, Industrial,
or Construction Activity 5- Inflation and Price Indices 6- Interest Rates, Monetary Policy,
Government Budget, or Bond Issuance 7- Financial Markets and Speculative Indices 8-
Broad Economic Activity Indicators. The selection of these eight categories was made with
the assistance of GPT-4o and guided by two key criteria: (i) economic interpretability,
ensuring that each category captures a distinct dimension of economic conditions, and (ii)
data suﬀiciency, ensuring that each category contains a meaningful number of observations.
To assign each data release to its appropriate category, I interact with GPT-4o using the
A-3

prompt shown in Prompt 8. This prompt instructs the AI model to classify the headline of
each economic data release into one of the predefined categories.
Prompt: Forget all previous instructions. I will give you a headline. Please list the
category it belongs to among the following categories: ’1. Employment and Unemployment
Data; 2. Consumer Sentiment, Retail or Services Activity; 3. International Trade; 4.
Manufacturing, Industrial or Construction Activity; 5. Inflation and Price Indices; 6.
Interest Rates, Monetary Policy, Government Budget or Bond Issuance; 7. Financial
Markets and Speculative Indices; 8. Broad Economic Activity Indicators.’ Generate the
output in this format: {(CATEGORY: CATEGORY NUMBER AND NAME)}
Prompt 8
This automated classification procedure ensures consistency across a large set of headlines
and enables a systematic analysis of the heterogeneous predictive power of different types of
economic fundamentals, as discussed in Section 6.1. In addition, Table 8 presents the eight
categories, along with representative examples of headlines and the number of observations
within each category.
A-4

| Figure | A.1. | t-statistics | (spot returns) |     |     |
| ------ | ---- | ------------ | -------------- | --- | --- |
3.5
T-statistics
|     |     |     | (5%) Significance | Level |     |
| --- | --- | --- | ----------------- | ----- | --- |
3
|     |     |     | (10%) | Significance Level |     |
| --- | --- | --- | ----- | ------------------ | --- |
2.5
2
tats-T
1.5
A-5
1
0.5
0
| 1 6 | 12 18    | 24 30  | 36 42    | 48 54 | 60  |
| --- | -------- | ------ | -------- | ----- | --- |
|     | Lookback | Period | (Months) |       |     |
This figure displays the t-statistics of β in Equation (5), where the dependent variable is spot return. The regression is repeated for
different choices of lookback period. This regression examines whether the AIFX index of a currency at the end of a given month can
predict the currency’s spot return in the subsequent month. Standard errors are clustered at the currency and time level. The regression
includes time fixed effects, although not reported here. The sample period spans from January 1996 to October 2024, but returns start
at different dates due to differences in lookback periods. The dashed horizontal lines mark the 5% and 10% statistical significance
thresholds.

Figure A.2. Performance of AI-powered Time-series strategy
0.5
0.4
0.3
0.2
0.1
0
−0.1
1 6 12 18 24 30 36 42 48 54 60
Lookback Period (Months)
oitaR
eprahS
dezilaunnA
This figure reports the annualized Sharpe ratios of time-series strategies that use the Diff AIFX index (defined in Equation (7)) as the
trading signal. For each choice of lookback period τ, at the end of each month t, I take a long position in currency c if Diff AIFX
c,t,τ
is positive and a short position if negative. Thus, portfolio weights are either +1 or −1, depending on the sign of the signal. Portfolios
are rebalanced at the end of each calendar month. Lookback periods of 1 to 60 months are considered. The sample period spans from
January 1996 to October 2024, but returns start at different dates due to differences in lookback periods.
A-6

Figure A.3. Sharpe Ratios (AIFX vs AIFX )
c USD
0.6
0.5
0.4
0.3
0.2
0.1
0
−0.1
−0.2
−0.3
1 6 12 18 24 30 36 42 48 54 60
Lookback Period (Months)
oitaR
eprahS
dezilaunnA
AIFX
c
AIFX
USD
ThisfigurereportstheannualizedSharperatiosoftime-seriesstrategiesthatusetheAIFX andAIFX asthetradingsignal. Portfolios
c USD
are rebalanced at the end of each calendar month. Lookback periods of 1 to 60 months are considered. The sample period spans from
January 1996 to October 2024, but returns start at different dates due to differences in lookback periods.
A-7

|     |     |     | Figure | A.4. Cumulative | Returns |     |     |
| --- | --- | --- | ------ | --------------- | ------- | --- | --- |
2.6
Diff AIFX
| tnemtsevnI | 2.4 | AIFX |     |     |     |     |     |
| ---------- | --- | ---- | --- | --- | --- | --- | --- |
USD
|     |     | Cut-off | Date |     |     |     |     |
| --- | --- | ------- | ---- | --- | --- | --- | --- |
2.2
|     |     | Recession | Period |     |     |     |     |
| --- | --- | --------- | ------ | --- | --- | --- | --- |
| 1$  | 2   |           |        |     |     |     |     |
laitinI
1.8
na
1.6
fo
A-8
eulaV
1.4
ralloD
1.2
1
|     | 0   |     | 5   | 0   | 5   | 0   | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   |     | 0   | 1   | 1   | 2   | 2   |
|     | 0   |     | 0   | 0   | 0   | 0   | 0   |
|     | 2   |     | 2   | 2   | 2   | 2   | 2   |
Date
The graph displays the Dollar value of an initial $1 investment in two time-series strategies from January 2000 to October 2024. The
blue line uses the Diff AIFX index (defined in Equation (7)) and the red line uses the AIFX USD as the signal. Both trading strategies
have a lookback period of 48 months. The green shaded regions denote NBER recession periods. The vertical dotted line marks the
| knowledge | cutoff date | of GPT-4o | (October 2023). |     |     |     |     |
| --------- | ----------- | --------- | --------------- | --- | --- | --- | --- |

Figure A.5. Comparison of F1 Score and Strategy’s Annual Return
0002 1002 2002 3002 4002 5002 6002 7002 8002 9002 0102 1102 2102 3102 4102 5102 6102 7102 8102 9102 0202 1202 2202 3202 4202
Correlation = −0.36
20
15
10
5
0
−5
Year
)%(
ecnamrofreP
F1 Score
Annual Return
The red line displays the annual return of the AIFX strategy with a lookback period of 48 months. The blue line shows the F1 score
(defined in Equation (10)) for each year. The performance is reported from January 2000 to October 2024.
A-9

| Figure | A.6. Pure | Hindsight | Portfolio’s | Performance | Over Time |     |
| ------ | --------- | --------- | ----------- | ----------- | --------- | --- |
3
| Pure-hindsight     |      | Portfolio |     |     |     |     |
| ------------------ | ---- | --------- | --- | --- | --- | --- |
| tnemtsevnI Cut-off | Date |           |     |     |     |     |
Recession Period
2.5
1$
laitinI
2
na
fo
A-10
eulaV
1.5
ralloD
1
| 6   | 0   | 5   | 0   | 5   | 0   | 4   |
| --- | --- | --- | --- | --- | --- | --- |
| 9   | 0   | 0   | 1   | 1   | 2   | 2   |
| 9   | 0   | 0   | 0   | 0   | 0   | 0   |
| 1   | 2   | 2   | 2   | 2   | 2   | 2   |
Date
The graph displays the Dollar value of an initial $1 investment in the pure hindsight portfolio from January 1996 to October 2024. The
trading strategy’s signal is solely based on what the AI model may remember about historical currency returns and uses the outputs of
Prompt 7. The portfolio is rebalanced at the end of each calendar month, same as the AIFX strategy. The green shaded regions denote
NBER recession periods. The vertical dotted line marks the knowledge cutoff date of GPT-4o (October 2023).

|     |     |      | Figure | A.7. Cross-sectional |     | Standard | Deviation |       |
| --- | --- | ---- | ------ | -------------------- | --- | -------- | --------- | ----- |
|     |     | 0.08 |        |                      |     |          | Strength  | ratio |
|     |     |      |        |                      |     |          | Weakness  | ratio |
|     |     |      |        |                      |     |          | AIFX      | index |
0.07
|     | noitaiveD | 0.06 |     |     |     |     |     |     |
| --- | --------- | ---- | --- | --- | --- | --- | --- | --- |
0.05
dradnatS
0.04
A-11
0.03
0.02
0.01
|     |     |     | 0   | 5   | 0   | 5   | 0   | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 0   | 0   | 1   | 1   | 2   | 2   |
|     |     | 0   |     | 0   | 0   | 0   | 0   | 0   |
|     |     | 2   |     | 2   | 2   | 2   | 2   | 2   |
Date
The figure displays the monthly cross-sectional standard deviation of three AI-powered variables from January 2000 to October 2024.
The three variables include: AIFX index (defined in Equation (3)) , Strength ratio (defined in Equation (1)) and Weakness ratio (defined
| in Equation | (2)). All | the three | variables | have a lookback | period of | 48 months. |     |     |
| ----------- | --------- | --------- | --------- | --------------- | --------- | ---------- | --- | --- |

|     |     | Figure | A.8. Average | Daily Returns |     |     |
| --- | --- | ------ | ------------ | ------------- | --- | --- |
1.92
2
1
)stnioP
0.30
0.10
0
sisaB(
| −1  |     |     |     |     |     | −0.73 |
| --- | --- | --- | --- | --- | --- | ----- |
−1.24
snruteR
−2
−3
A-12
naeM
−4
|     | Positive | News |     |     |     |     |
| --- | -------- | ---- | --- | --- | --- | --- |
| −5  | Negative | News |     |     |     |     |
−4.99
|     |     | r e |     | a y |     | e r |
| --- | --- | --- | --- | --- | --- | --- |
|     |     | o   |     | D   |     | t   |
|     |     | ef  |     |     |     | Af  |
|     |     | B   |     | e   |     |     |
|     |     |     |     | m   | y   |     |
|     |     | y   |     |     | a   |     |
|     |     | a   |     | a   | D   |     |
|     | D   |     |     | S   |     |     |
This figure compares the average realized returns associated with positive and negative news on the day before, day of and the day after
the release. Each of the data releases in the dataset is labeled as positive, neutral or negative using the output of Prompt 1. Specifically,
I refer to data releases with the direction labeled as STRENGTHEN in the output as positive news, those labeled as WEAKEN as
negative news, and those labeled as INSIGNIFICANT OR UNCERTAIN as neutral news. The sample period for this exercise is from
2008 to 2024.

|     |     | Table | A.1. Performance | Statistics |     |     |
| --- | --- | ----- | ---------------- | ---------- | --- | --- |
Thistablereportstheperformancestatisticsofthebenchmarkcurrencyfactors. ThebenchmarksincludeDollar, DollarCarry, Cross-sectionalCarry,
Cross-sectional One-month Momentum, and Cross-sectional Value strategies, constructed as described in Internet Appendix A. The statistics include
mean returns, standard deviation, skewness, excess kurtosis, first-order autocorrelation (AR(1)) and Sharpe Ratios. The measures are based on
monthlyreturns,butmeans,standarddeviationsandSharperatiosareannualized. TheperformancereportedisfromJanuary2001toOctober2024.
|     |     | Dollar | DollarCarry | Carry | Value | Momentum |
| --- | --- | ------ | ----------- | ----- | ----- | -------- |
−0.374
| Mean     |           | 0.249  | 2.111  | 3.201  | 2.282 |       |
| -------- | --------- | ------ | ------ | ------ | ----- | ----- |
| Standard | deviation | 8.296  | 8.273  | 7.653  | 6.963 | 6.963 |
|          |           | −0.154 | −0.289 | −0.942 |       |       |
| Skewness |           |        |        |        | 0.024 | 0.406 |
| Excess   | kurtosis  | 0.807  | 0.896  | 3.764  | 0.077 | 4.532 |
−0.041
| AR(1)  |       | 0.028 | 0.019 | 0.044 | 0.001 |        |
| ------ | ----- | ----- | ----- | ----- | ----- | ------ |
| Sharpe | Ratio | 0.030 | 0.255 | 0.418 | 0.328 | −0.054 |
A-13

|     |     |     | Table | A.2. Performance | Statistics |     |
| --- | --- | --- | ----- | ---------------- | ---------- | --- |
This table reports the performance statistics for the time-series strategies that use the Diff AIFX index (defined in Equation (7)) as the trading
signal. For each choice of lookback period τ, at the end of each month t, I take a long position in currency c if Diff AIFX is positive and a short
c,t,τ
−1,
position if negative. Thus, portfolio weights are either +1 or depending on the sign of the signal. Portfolios are rebalanced at the end of each
calendar month. Results are shown for different lookback periods. The statistics include mean returns, standard deviation, skewness, excess kurtosis,
first-order autocorrelation (AR(1)) and Sharpe Ratios. The measures are based on monthly returns, but means, standard deviations and Sharpe
| ratios are annualized. | The performance | reported | is from   | January 2001 to October | 2024.     |           |
| ---------------------- | --------------- | -------- | --------- | ----------------------- | --------- | --------- |
|                        |                 |          |           | 48 months               | 54 months | 60 months |
|                        |                 | Mean     |           | 2.187                   | 2.252     | 2.112     |
|                        |                 | Standard | deviation | 5.883                   | 5.843     | 5.905     |
|                        |                 |          |           | −0.183                  | −0.153    | −0.184    |
Skewness
|     |     | Excess | kurtosis | 0.315  | 0.535  | 0.260  |
| --- | --- | ------ | -------- | ------ | ------ | ------ |
|     |     |        |          | −0.043 | −0.057 | −0.039 |
AR(1)
|     |     | Sharpe | Ratio | 0.372 | 0.385 | 0.358 |
| --- | --- | ------ | ----- | ----- | ----- | ----- |
A-14

| Table |     | A.3. Performance |     | Over | Benchmark |     | Factors |
| ----- | --- | ---------------- | --- | ---- | --------- | --- | ------- |
This table presents the results from a contemporaneous regression similar to the one specified in Equation (4), which examines whether the monthly
returns of the time-series strategy, using the Diff AIFX index (defined in Equation (7)) as the trading signal, can be explained by common currency
factors. The time-series benchmark strategies are described in Internet Appendix A. The performance reported is from January 2001 to October
2024. Newey and West (1987) standard errors are reported in parentheses. ***, **, and * indicate statistical significance at the 1%, 5%, and 10%
levels, respectively.
|     |     |     | Return    | of the | AI-powered | Strategy  |     |
| --- | --- | --- | --------- | ------ | ---------- | --------- | --- |
|     |     |     | 48 months | 54     | months     | 60 months |     |
|     |     |     | 1.42*     |        | 1.56**     | 1.44**    |     |
Alpha
|     |     |     | (0.84) |     | (0.72) | (0.72) |     |
| --- | --- | --- | ------ | --- | ------ | ------ | --- |
A-15
|     |     |     | −0.46*** |     | −0.52*** | −0.56*** |     |
| --- | --- | --- | -------- | --- | -------- | -------- | --- |
Dollar
|     |          |       | (0.03)  |     | (0.03)  | (0.02)  |     |
| --- | -------- | ----- | ------- | --- | ------- | ------- | --- |
|     | Dollar   | Carry | 0.24*** |     | 0.28*** | 0.26*** |     |
|     |          |       | (0.05)  |     | (0.04)  | (0.04)  |     |
|     | Carry    |       | 1.95*** |     | 0.89    | 0.99*   |     |
|     |          |       | (0.71)  |     | (0.63)  | (0.59)  |     |
|     | Value    |       | 0.02    |     | 0.42    | 0.22    |     |
|     |          |       | (0.36)  |     | (0.32)  | (0.30)  |     |
|     | Momentum |       | −0.10   |     | 0.23    | 0.33    |     |
|     |          |       | (0.34)  |     | (0.30)  | (0.28)  |     |
|     |          | R2(%) | 54.9    |     | 64.7    | 69.5    |     |
|     |          | N     | 286     |     | 286     | 286     |     |

|     | Table A.4. | Evaluation | of the Classification |     |     |     |
| --- | ---------- | ---------- | --------------------- | --- | --- | --- |
This table provides a detailed description of the classification exercise of Section 5.1. In the classification exercise, the AI model is tasked with
identifying the year (not the exact date) in which each data release occurred, using Prompt 3. This exercise serves as a test for potential look-ahead
bias. In the experiment, I use the same inputs originally provided to the AI model via Prompt 1, but instead of asking for an economic analysis, the
model is asked to guess the year of the data release. The sample period spans from January 1996 to October 2024.
Year Number of Data Releases All Guesses Correct Guesses Precision(%) Recall(%) F1-score(%)
| 1996 | 1955 | 283 | 8   | 2.83 | 0.41 | 0.72 |
| ---- | ---- | --- | --- | ---- | ---- | ---- |
| 1997 | 2053 | 123 | 7   | 5.69 | 0.34 | 0.64 |
| 1998 | 2091 | 279 | 16  | 5.73 | 0.77 | 1.35 |
| 1999 | 2171 | 426 | 18  | 4.23 | 0.83 | 1.39 |
| 2000 | 2260 | 96  | 0   | 0.00 | 0.00 | 0.00 |
| 2001 | 2393 | 131 | 8   | 6.11 | 0.33 | 0.63 |
| 2002 | 2418 | 98  | 6   | 6.12 | 0.25 | 0.48 |
| 2003 | 2460 | 144 | 7   | 4.86 | 0.28 | 0.54 |
| 2004 | 2488 | 169 | 5   | 2.96 | 0.20 | 0.38 |
A-16
| 2005 | 2517 | 139   | 4    | 2.88  | 0.16  | 0.30 |
| ---- | ---- | ----- | ---- | ----- | ----- | ---- |
| 2006 | 2559 | 137   | 7    | 5.11  | 0.27  | 0.52 |
| 2007 | 2567 | 132   | 5    | 3.79  | 0.19  | 0.37 |
| 2008 | 3610 | 353   | 28   | 7.93  | 0.78  | 1.41 |
| 2009 | 3770 | 557   | 77   | 13.82 | 2.04  | 3.56 |
| 2010 | 3822 | 353   | 21   | 5.95  | 0.55  | 1.01 |
| 2011 | 3814 | 315   | 15   | 4.76  | 0.39  | 0.73 |
| 2012 | 3845 | 362   | 30   | 8.29  | 0.78  | 1.43 |
| 2013 | 3952 | 590   | 42   | 7.12  | 1.06  | 1.85 |
| 2014 | 4385 | 834   | 49   | 5.88  | 1.12  | 1.88 |
| 2015 | 4665 | 1036  | 79   | 7.63  | 1.69  | 2.77 |
| 2016 | 4639 | 1530  | 120  | 7.84  | 2.59  | 3.89 |
| 2017 | 4604 | 799   | 45   | 5.63  | 0.98  | 1.67 |
| 2018 | 4682 | 804   | 47   | 5.85  | 1.00  | 1.71 |
| 2019 | 4842 | 1282  | 68   | 5.30  | 1.40  | 2.22 |
| 2020 | 5128 | 4883  | 487  | 9.97  | 9.50  | 9.73 |
| 2021 | 5104 | 4099  | 343  | 8.37  | 6.72  | 7.45 |
| 2022 | 4996 | 6329  | 378  | 5.97  | 7.57  | 6.67 |
| 2023 | 4996 | 73860 | 3792 | 5.13  | 75.90 | 9.61 |
| 2024 | 3946 | 2566  | 111  | 4.33  | 2.81  | 3.41 |
---- END DOCUMENT ----
