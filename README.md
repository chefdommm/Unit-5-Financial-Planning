# Unit-5-Financial-Planning

![Financial Planner](https://www.aegonlife.com/insurance-investment-knowledge/wp-content/uploads/2017/01/financial-planning-660x330-1.jpg)



## OVERVIEW

We were directed to start a FinTech consultancy firm, and try to make a difference by working on projects with high social impact in local communities. The first contract was  to help one of the biggest credit unions in the area. They wanted a tool that helps their members enhance their financial health. The Chief Technology Officer (CTO) of the credit union asked  to develop a prototype application to demo in the next credit union assembly.



The first task was to create a personal finance planner that will allow users to visualize their savings composed by investments in shares and cryptocurrencies to assess if they have enough money as an emergency fund.

The second tool was to create a retirement planning tool that will use the Alpaca API to fetch historical closing prices for a retirement portfolio composed of stocks and bonds, then run Monte Carlo simulations to project the portfolio performance at 30 years. Then the Monte Carlo data was used to calculate the expected portfolio returns given a specific initial investment amount.

---


## *STEPS*

### Part 1 - Personal Finance Planner

In this section of the challenge, was to create a personal finance planner application. To develop the personal finance planner prototype,

* The average household income for each member of the credit union is `$12,000`.

* Every union member has a savings portfolio composed of cryptocurrencies, stocks and bonds:

 1.  The first step was to assume the amount of crypto currency tha the members had.
 * The crypto currencies we dealt with were `Bitcoin` and `Ethereum`

 ![Bitcoin](https://i.ebayimg.com/images/g/THsAAOSwLsBZWjws/s-l300.jpg)

 ![Ethereum](https://mining-cryptocurrency.ru/wp-content/uploads/Ethereum-1.jpg)



# Crypto Portfolio

1. I had create two variables called `my_btc` and `my_eth`. Set them equal to `1.2` and `5.3`, respectively.

2. I then `requests` library to fetch the current price in Canadian dollars (`CAD`) of bitcoin (`BTC`) and ethereum (`ETH`) using the **Alternative Free Crypto API** endpoints provided in the starter notebook.

3. I then had to parse the API JSON response to select only the crypto prices and store each price in a variable.

4.I Computed the portfolio value of cryptocurrencies and print the results.

# Bonds Portfolio

1. I  had to create two variables named `my_agg` and `my_spy` and set them equal to `200` and `50`, respectively.

2. I then got  the Alpaca API key and secret key variables, then create the Alpaca API object using the `tradeapi.REST` function from the Alpaca SDK.

3. I Formated the current date as ISO format. You may change the date set in the starter code to the current date.

4. I retrieved  current closing prices for `SPY` and `AGG` using Alpaca's `get_bars()` function. Transform the function's response to a Pandas DataFrame and preview the data.

5. I then picked the `SPY` and `AGG` close prices from the Alpaca's `get_bars()` DataFrame response and store them as Python variables. Print the closing values for validation.

6. I Computed the value in dollars of the current amount of shares and print the results.

# Savings Health Analysis

In this section, I assessed the financial health of the credit union's members.

1. Create a variable called `monthly_income` and set its value to `12000`.

2. I analyzed the current savings health, created a DataFrame called `df_savings` with two rows. Store the total value in dollars of the crypto assets in the first row and the total value of the shares in the second row.


3. I then used the `df_savings` DataFrame to plot a pie chart to visualize the composition of personal savings.

4. Use an `if` conditional statements to validate if the current savings are enough for an emergency fund. An ideal emergency fund should be equal to three times your monthly income.

    * If total savings are greater (>) than the emergency fund, display a message congratulating the person for having enough money in this fund.
---


# Part 2 - Retirement Planning

In this section I used the Alpaca API to fetch historical closing prices for a retirement portfolio and then Use the MCForecastTools toolkit to create Monte Carlo simulations to project the portfolio performance at `30` years. I then used the Monte Carlo data to answer questions about the portfolio.


## Monte Carlo Simulation
![Monte Carlo Sim](https://pmstudycircle.com/wp-content/uploads/2015/02/Monte-Carlo-Simulation.png)

1. I used the Alpaca API to fetch five years historical closing prices for a traditional `40/60` portfolio using the `SPY` and `AGG` tickers to represent the `60%` stocks (`SPY`) and `40%` bonds (`AGG`) composition of the portfolio. 

2. I configure and executed a Monte Carlo Simulation of `100` runs (`MY COMPUTER COULD NOT HANDLE 500 RUNS`) and `30` years for the `40/60` portfolio.

3. I then plotted the simulation results and the probability distribution/confidence intervals.



## Retirement Analysis

1. I fetched the summary statistics from the Monte Carlo simulation results.

1. Given an initial investment of `$20,000`, I calculated the expected portfolio return in dollars at the `95%` lower and upper confidence intervals.

2. I also calculated the expected portfolio return at the `95%` lower and upper confidence intervals.



---

