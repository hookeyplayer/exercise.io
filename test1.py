#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:55:54 2021

@author: xiaofan
"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import math
#%%

# =============================================================================
# data preparation
# =============================================================================

symbols = list(pd.read_excel('msci2017.xlsx')['Symbol'])
start = '2017-01-01'
end = '2017-12-31'
df = yf.download(symbols,start,end)['Adj Close'] # 30 Failed downloads
df.dropna()
print(df.shape)

# =============================================================================
# convert to log returns
# =============================================================================

logReturns = pd.DataFrame()
for col in df.columns:
    logReturns[col] = np.log(df[col]).diff(-1)

# =============================================================================
# Heat map
# =============================================================================

corrMatrix = logReturns.corr()
print(corrMatrix.head())
# sns.clustermap(corrMatrix, cmap="RdYlGn")
# plt.show()

# =============================================================================
# edge and nodes preparation
# =============================================================================

edges = corrMatrix.stack().reset_index()
edges.columns = ['theOne','theOther','correlation']
# remove self correlations
# list, containing pairwise correlation information
edges = edges.loc[edges['theOne'] != edges['theOther']].copy()
# undirected graph with weights corresponding to the correlation magnitude
G0 = nx.from_pandas_edgelist(edges, 'theOne', 'theOther', edge_attr=['correlation'])

#print out the graph info
print(nx.info(G0))
# Number of nodes: 797
# Number of edges: 316985
# Average degree: 795.4454

# =============================================================================
# un-weighted graph, one-size nodes
# =============================================================================

plt.figure(figsize=(7,7))
# 1
# nx.draw(G0, with_labels=True, node_size=200, node_color="#e1575c",
#         edge_color='#363847',  pos=nx.circular_layout(G0))
# plt.title("Circular layout")

# 2
# nx.draw(G0, with_labels=True, node_size=100, node_color="#e1575c",
#         edge_color='#363847',  pos=nx.random_layout(G0))
# plt.title("Random layout")

# # 3
# nx.draw(G0, with_labels=True, node_size=200,
#         edge_color='#363847',  pos=nx.spring_layout(G0))
# plt.title("Sprint layout")

# 4
nx.draw(G0, with_labels=True, node_size=50,
        edge_color='#363847',  pos=nx.spectral_layout(G0))
plt.title("Spectral layout")
plt.show()

# =============================================================================
# improved graph 1--threshold 
# =============================================================================

# unsystematic risk assesment
# (1)which assets show strong/meaningful correlations (i.e. >0.5) with each other
# (2)are these correlations positive or negative?
# (3)which are the most/least ‘connected’ assets. 
# (i.e. which assets share the most/least strong correlations with others)

# (4)which groups of assets behave similarly 
# (i.e. which assets are correlated with the same type of other assets)

# =============================================================================
# improved graph 2--node size (degree)
# =============================================================================

# =============================================================================
# improved graph 3--edge thickness(correlation magnitude)
# =============================================================================
