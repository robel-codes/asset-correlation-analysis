# Asset Correlation Analysis

## User Story

## Table of Contents

1. [Project Links](#Project-Links)
1. [Questions](#Questions)
1. [Instructions](#Instructions)
1. [Project Team](#Project-Team)
1. [Contribution Guidelines](#Contribution-Guidelines)
1. [Contanct](#Contact)
1. [License](#License)

## Project Links

[Repo Link](https://github.com/robel-codes/asset-correlation-analysis) <br>
![Repo Image](./images/output.png)

## Questions

### What programming tools can potentially be used to validate that a portfolio is diversified?
- pandas
- alpaca_trade_api
- hvplot
- MCForecastTools
- seaborn

### Is there a measurable correlation between the weather in NYC and the performance of the market?
- Our analysis and graphs indicate there is no correlation during the timeframe investigated.
- ![Weather Correlation Graph](./images/weather_corr_1.png)

### Which of the factors in our initial data set is most correlated with the S&P 500?
- The price of BTC has the highest correlation with the S&P 500.
- ![All Correlation Graph](./images/all_corr.png)

### Does a relationship exist between the overall market performance and the sentiment of people's Google searches?
- It depends on the search query.
-[Google Sentiment Correlation Graph 1](./images/sp500_sentiment_1.png)
-[Google Sentiment Correlation Graph 2](./images/sp500_sentiment_2.png)

### Would a portfolio made up of SP500 index fund, BTC and Oil perform well over time?
- Our analysis indicate that this would not be an advisable investment strategy.
![Portfolio Simulation](./images/simulation_1.png)

## Code and Dependencies
This code is to be run on 
`Python 3.7.13`

The following Python Libraries were also imported and used

`import pandas as pd`

`import os`

`import requests`

`from dotenv import load_dotenv`

`import alpaca_trade_api as tradeapi`

`from MCForecastTools import MCSimulation`

`import alpaca_trade_api as tradeapi`

`import numpy as np`

`import datetime as dt`

`import seaborn as sns`

`from pathlib import Path`

`import pandas_datareader as web`

`from pytrends.request import TrendReq`

`import matplotlib.pyplot as plt`

## Instructions

Add a .env file and add this code with your Alpaca credintals to make an API call via Alpaca SDK

```
 * ALPACA_API_KEY = "your-alpaca-api-key"
 * ALPACA_SECRET_KEY='your-alpaca-secret-key'
```

## Project Team

[Ben Eilers](https://github.com/bweilers) <br>
[Eyob](https://github.com/dobinhom) <br>
[Robel Gebremeskel](https://github.com/robel-codes) <br>

## Contribution Guidelines:

```
Feel free to contribute to this repo by creating issues or sending an email to any of the contributors in the list below.
```

## Contact

<details>
    <summary>Contact</summary>
    ben.eilers@gmail.com <br>
    dobinhom@gmail.com <br>
    rofikre@yahoo.com <br>

</details>

## License

#### Distributed under the MIT License. See [Choose A License](https://choosealicense.com/) for more details.
