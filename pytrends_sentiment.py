import pandas as pd
import numpy as np
from pytrends.request import TrendReq
from pytrends import dailydata
import pandas_datareader as web
import matplotlib.pyplot as plt

# takes a string as an argument
# + dataframe
def generate_trends_analysis(key_word):

    trends1 = dailydata.get_daily_data(key_word, 2022, 9, 2022, 11, geo='US')
    trends2 = dailydata.get_daily_data(key_word, 2022, 6, 2022, 8, geo='US')
    trends3 = dailydata.get_daily_data(key_word, 2022, 3, 2022, 5, geo='US')


    trends_combined = pd.concat([trends1, trends2, trends3], axis='rows', join='inner')
    trends_combined.sort_index(ascending=True, inplace=True)
    trends_combined.drop(columns=[f'{key_word}_unscaled', f'{key_word}_monthly', 'isPartial', 'scale'], inplace=True)
    trends_combined.columns = [f'sentiment_score_{key_word}']

    # return trends_combined


    # Gets the historical abs value of the asset
    asset_historical_df = web.get_data_yahoo([key_word], '10/31/2017', interval='d')
    asset_historical_df = asset_historical_df.iloc[:, [0,1,2]]
    asset_historical_df = asset_historical_df['Close']
    asset_historical_df.columns = [' '.join(col).strip() for col in asset_historical_df.columns.values]

    # concat and plot correlation ABS
    absolute_price_correlation_df = pd.concat([asset_historical_df, trends_combined], axis="columns", join="inner")
    absolute_price_correlation_df.columns = [key_word, f'sentiment_score_{key_word}']
    
    # return absolute_price_correlation_df

    plot1 = absolute_price_correlation_df.plot(x=key_word, y=f'sentiment_score_{key_word}', style= 'o')
    plot2 = plt.xlabel(key_word)
    plot3 = plt.ylabel(f'sentiment_score_{key_word}')
    plt.title(f"{key_word} Correlation Plot")
    # return plot1


    # concat and plot correlation daily returns
    daily_return_correlation = absolute_price_correlation_df.copy()
    daily_return_correlation['Daily_Return'] = daily_return_correlation[key_word].pct_change()
    daily_return_correlation.drop(columns=[key_word], inplace=True)
    daily_return_correlation.dropna(inplace=True)
    plot4 = daily_return_correlation.plot(x='Daily_Return', y=f'sentiment_score_{key_word}', style= 'o')
    plot5 = plt.xlabel("Daily_Return")
    plot6 = plt.ylabel(f'sentiment_score_{key_word}')
    plt.title(f"{key_word} Daily Return Correlation with Sentiment Plot")




