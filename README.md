# Project 1 - Project Proposal

## Project title: Correlation Versus Causation in the S&P 500 Performance

## Team members
- Robel
- Eyob
- Ben

## Project Description/Outline
What are the possible factors that either impact or are correlated to the returns of the S&P 500?

Possible correlations: 
- weather 
- currency valuation (USD and Crypto)
- commodity price (oil) 
- Tweets / Sentiment Analysis (pytrends would be a new library)
Stagger the tweet and price by 1 day
Compare the impact of sentiment from tweets to the next day’s price
Could potentially get data directly from the Twitter API


## Research questions to answer
How does weather in New York, NY correlate with the performance of the S&P 500? 
Can weather forecasting give us insight into future stock performance?
What is the correlation of BTC to the S&P 500?

## Datasets to be used
Yahoo Finance for Historical Financial Data, including:
- S & P 500
- Bitcoin
- Commodity (oil)
Weather API
- https://github.com/n0shake/Public-APIs#weather


## Rough breakdown of tasks

### A. Correlation Assesment
1. Collect the most recent five years of data for the assets being analyzed and populated the data into unique dataframes. 
- Clean data
- Set date as the index
2. Determine the daily returns of each asset
- e.g. `asset_df.pct_change()`
3. Use one of the APIs provided in `https://github.com/n0shake/Public-APIs#weather` to collect weather data for the same 5 year period
4. Combine all assets (plus weather data) into a new dataframe
- e.g. `combined_returns = pd.concat([asset1_df, asset2_df, asset3_df], axis="columns", join="inner")`
5. Plot the combined_returs
- e.g. `combined_returns.plot()`
6. Calculate and plot cumulative returns for each asset
- `cumulative_returns = (1 + combined_returns).cumprod()`
- `cumulative_returns.plot(figsize=(20,10), title="Cumulative Returns")`
7. Determine and plot correlation of the S&P 500 to the various assets (plus weather)
- `correlation = combined_returns.corr()`
- `sns.heatmap(corrleation)`

### B. Weather Correlation
1. Collect 5 years of weatehr data from and API
2. Clean data
3. Concatinate weather to the combined_returns dateframe
4. Calculate and plot weather correlation
5. Optional: 
- Calculate correlation for other global equities markets
- Create map using hvplot

### C. Sentiment Analysis
1. Collect data about tweets mentions of 'SP500' through the twitter API. Five years of data is ideal, but we will make use of what is available.
2. Calculate correlation of twitter sentiment for the time available (note: we plan to stager the calculation by one day to see how one day's tweets impact the next day's S&P 500 performance).
3. Option to perform sentiment analysis on other assets (i.e. BTC and Oil)
4. Option to pursue data from another source (e.g. news data)

### D. Portfolio Recommendation
1. Determine how risky the assets are
- Calculate and plot rolling standard deviation `combined_returns.rolling(window=21).std().plot(figsize=(25, 10))`
- Calculate and plot the beta for the various assets `beta = asset.cov() / asset.var()`
- Calculate and plot the Sharpe Ratios `sharpe_ratios = ((combined_returns.mean() - risk_free_rate.mean()) * 252) / (combined_returns.std() * np.sqrt(252))`
2. Create fictional portfolios of the various assets. All portfolios have the same assets but with different weights. And run Monte Carlo Simulations to determine which portfolio we would advize. 
- e.g. One may be made of 33.33% SPY (the S&P 500 etf), 33.33% BTC, and 33.33% oil etf, and another portfolio might be 50% SPY (the S&P 500 etf), 30% BTC, and 20% oil etf.
- `MCSimulation.plot_simulation()`
