
'''
loding your dotenv file, setting keys, and calling the 
alpcaca api object, and their imports needed
'''

import os
import pandas as pd
import alpaca_trade_api as tradeapi

# Load .env enviroment variables
from dotenv import load_dotenv
load_dotenv()

# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# create the alpaca API object
api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version = "v2"
)



''' gets tickers from alpaca api
    do note, it's the old style API used for class,
    not the updated one. So newer dates wont work

    ticker = [list]
    timeframe = str of time, e.g. "1Day"

    start_date = pd.Timestamp("2018-08-04", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2021-08-04", tz="America/New_York").isoformat()
'''

df_ticker = api.get_bars(
    ticker,
    timeframe,
    start = start_date,
    end = end_date
).df


'''
ignore warnings from the MCSimulator Class
'''
import warnings

# Suppress the specific PerformanceWarning
warnings.filterwarnings('ignore', message='DataFrame is highly fragmented', category=pd.errors.PerformanceWarning)


'''
reorganizing and concatenating a dataframe delivered from 
old-style alpaca api
'''

# Reorganize the DataFrame
# Separate ticker data
T = df_ticker[df_ticker["symbol"]=="T"].drop("symbol", axis=1)
NKE = df_ticker[df_ticker["symbol"]=="NKE"].drop("symbol", axis=1)
XOM = df_ticker[df_ticker["symbol"]=="XOM"].drop("symbol", axis=1)

# Concatenate the ticker DataFrames
df_ticker = pd.concat([T, NKE, XOM], axis=1, keys=["T","NKE","XOM"])


# Pick AGG and SPY close prices
agg_close_price = df_ticker["AGG"]["close"].values[0]
spy_close_price = df_ticker["SPY"]["close"].values[0]

'''
example instantiation and configuration of the MCSimulator Class
'''
from MCForecastTools import MCSimulation

# Set number of simulations
num_sims = 1000
years = 3

# Configure a Monte Carlo simulation to forecast three years daily returns
MC_tsla = MCSimulation(df_ticker, weights=[1/3,1/3,1/3], num_simulation=num_sims, num_trading_days=252*years)