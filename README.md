# Z-Score-Statistical-Test
This test helps in statistically identifying whether a study is statistically significant upon analyzing Z-scores.
Below, you can find how to use this script, and how it can help in analyzing your data-set:

Understanding the Model:

This model represents a null model, meaning it shows what the data should look like if nothing special is happening—in other words, if the null hypothesis is true. Under this assumption, the expected value is 0 because, over the long run, we do not expect any systematic effect or deviation from the mean.
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Interpreting the Axes:

The x-axis represents the z-score, which measures how far a result is from the null mean in terms of standard deviations. The y-axis represents the frequency of those z-scores, showing how many simulated datasets produced each value. Together, the graph visualizes how likely different outcomes are under the null hypothesis.
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Using the Model for Hypothesis Testing:

This model can be used as a statistical test for the null hypothesis. For example, in a drug trial, if the observed mean falls near the center of the distribution (around a z-score of 0), the result is likely not statistically significant and can be attributed to random variation. However, if the observed mean lies in the tails of the distribution, it indicates a rare event under the null model, suggesting statistical significance and a potential real effect.
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Understanding False Positives:

An important application of this model is identifying false positives. If the null hypothesis is true (e.g., the drug has no real effect), we can ask: how often would we still observe extreme results just by chance? Any values far from zero—both positive and negative—represent outcomes that could be mistakenly interpreted as significant. Specifically, values to the right of a positive observed z-score and to the left of its negative counterpart correspond to potential false positives.
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Final Note:

The “mean” referenced here is actually the z-score of the observed dataset’s mean. This value is used to determine how extreme the observed result is compared to the null model. A high absolute z-score corresponds to a low probability of false positives, suggesting that the observed effect is unlikely due to random noise. Conversely, a z-score close to 0 corresponds to a high probability of false positives, indicating that any observed variation is likely due to chance rather than a real underlying cause.
