#!/usr/bin/env python
# coding: utf-8

# In[2]:


# My Initial Imports
import os
import requests
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Load .env environment variiables
from dotenv import load_dotenv
load_dotenv('C:/Users/chefd/OneDrive/Desktop/keys/.env.txt')


# In[4]:


alpaca_api_key = os.getenv('ALPACA_API_KEY')
alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

# CREATE THE ALPACA API OBJECT
alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2"
)


# In[5]:


timeframe = '1Day'


# In[6]:


# Set start and end dates of five years back from today.
start_date = pd.Timestamp("2017-06-22", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2022-06-22", tz="America/New_York").isoformat()


# In[9]:


# Set the tickers
ticker = ["AGG", "SPY"]


# In[11]:


# Get 5 years' worth of historical data for SPY and AGG
df_ticker = alpaca.get_bars(
    ticker,
    timeframe,
    start=start_date,
    end=end_date
).df
df_ticker.head()


# In[12]:


df_ticker.tail()


# In[14]:


# Reorganize the DataFrame
# Separate ticker data
MSFT = df_ticker[df_ticker['symbol']=='AGG'].drop('symbol', axis=1)
KO = df_ticker[df_ticker['symbol']=='SPY'].drop('symbol', axis=1)


# In[15]:


df_ticker = pd.concat([MSFT, KO],axis=1, keys=['AGG','SPY'])
df_ticker.head()


# In[16]:


get_ipython().run_line_magic('pinfo', 'MCSimulation')


# In[17]:


MC_thirtyyear = MCSimulation(
    portfolio_data = df_ticker,
    weights = [.60,.40],
    num_simulation = 100,
    num_trading_days = 252*30
)

# could only do 100 sinulations computer could not do 500


# In[18]:


MC_thirtyyear.portfolio_data.head()


# In[19]:


MC_thirtyyear.calc_cumulative_return()


# In[20]:


line_plot = MC_thirtyyear.plot_simulation()


# In[21]:


line_plot = MC_thirtyyear.plot_distribution()


# In[22]:


tbl = MC_thirtyyear.summarize_cumulative_return()


# In[23]:


print(tbl)


# In[26]:


# Set initial investment
initial_investment = 20000
# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $20,000

ci_lower = round(tbl[8]*20000,2)
ci_upper = round(tbl[9]*20000,2)

# Print results
print(f"There is a 95% chance that an initial investment of ${initial_investment} in the portfolio"
      f" over the next 30 years will end within in the range of"
      f" ${ci_lower} and ${ci_upper}")


# In[33]:


# Calculate the expected portfolio return at the 95% lower and upper confidence intervals based on a 50% increase in the initial investment.
# Set initial investment
initial_investment = 20000 * 1.5
print(f"the initial investment is, ${initial_investment}")


# In[34]:


# Set initial investment
initial_investment = 20000
# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $20,000

ci_lower = round(tbl[8]*30000,2)
ci_upper = round(tbl[9]*30000,2)

# Print results
print(f"There is a 95% chance that an initial investment of ${initial_investment} in the portfolio"
      f" over the next 30 years will end within in the range of"
      f" ${ci_lower} and ${ci_upper}")


# In[ ]:




