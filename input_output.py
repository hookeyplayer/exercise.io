# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:16:09 2020

@author: xiaofan
"""
# =============================================================================
# pandas I/O
# =============================================================================
import pandas.io.sql as pds
# sql
data = pds.read_sql('SELECT * FROM numbers', con)
# from sql to csv
data.to_csv(filename + '.csv')
# four subplots
pd.read_csv(filename + '.csv')[['No1', 'No2', 'No3', 'No4']].hist(bins = 20)
pd.read_excel(filename + '.xlsx', 'Sheet1').cumsum().plot()

# =============================================================================
# PyTables
# =============================================================================
import tables as tb
filename = path + 'tab.h5'
data = tb.open_file(filename, 'w')
filters = tb.Filters(complevel = 0) # no compression

# PyTables can do out-of-memory computations

# =============================================================================
# parallel computing
# =============================================================================
# traditional Monte Carlo for Black Scholes Merton Euro calls
def bsm_mcs_valuation(strike):
    '''underlying asset accords SDE
    parameters:
    strike:float strike of option
    result:
    value: estimate pv of call option'''
    import numpy as np
    S0 = 100; T = 1.0; r = 0.05; vola = 0.2
    M = 50; I = 20000 # matrix
    dt = T/M
    rand = np.random.standard_normal((M+1, I))
    S = np.zeros((M+1, I)); S[0] = S0
    for t in range(1, M+1):
        S[t] = S[t-1] * np.exp((r-0.5*vola**2)*dt + vola*np.sqrt(dt)*rand[t])
        value = np.exp(-r*T)*np.sum(np.maximum(S[-1]-strike, 0))/I
    return value

# sequential calculation
# return list objects containing strikes and valuation results
def seq_value(n):
    '''sequential option valuation
    parameters:
        n:int number of options to be valued'''
    strikes = np.linspace(80, 120, num = n)
    option_values = []
    for strike in strikes:
        option_values.append(bsm_mcs_valuation(strike))
    return strikes, option_values
        
# =============================================================================
# parallel computation
# =============================================================================
from IPython.parallel import Client
c = Client(profile = 'default')
view = c.load_balanced_view() # generate a view on the cluster
def par_value(n):
    '''parallel option valuation
    parameters:
        n:int number of option valuations/strikes'''
        strikes = np.linspace(80, 120, n)
        option_values = []
        for strike in strikes:
            value = view.apply_async(bsm_msc_valuation, strike)
            option_values.append(value)
            c.wait(option_values)
        return strikes, option_values
# =============================================================================
# multiprocessing
# =============================================================================
import multiprocessing as np # parallelize code execution locally
import math
def simulate_geometric_brownian_motion(p):
    '''generate geometric brownian motion'''
    M, I = p # time steps, paths
    S0 = 100; T = 1.0; r = 0.05
    dt = T / M
    paths = np.zeros((M+1, I))
    paths[0] = S0
    for t in range(1, M+1):
        paths[t] = paths[t-1]*np.exp((r-0.5*sigma**2)*dt+
                    sigma*math.sqrt(dt)*np.random.standard_normal(I))
    return paths
paths = simulate_geometric_brownian_motion((5, 2))
        
        



