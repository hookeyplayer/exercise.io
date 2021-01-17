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
# 数据处理
# =============================================================================

symbols = list(pd.read_excel('msci2017.xlsx')['Symbol'])
start = '2017-01-01'
end = '2017-12-31'
df = yf.download(symbols,start,end)['Adj Close'] # 30 Failed downloads
df.dropna()
print(df.shape)
#%%
# =============================================================================
# 取对数
# =============================================================================

logReturns = pd.DataFrame()
for col in df.columns:
    logReturns[col] = np.log(df[col]).diff(-1)

# =============================================================================
# Heat map*
# =============================================================================

corrMatrix = logReturns.corr()
print(corrMatrix.head())
# sns.clustermap(corrMatrix, cmap="RdYlGn")
# plt.show()

# =============================================================================
# edge, nodes准备
# =============================================================================

edges = corrMatrix.stack().reset_index()
edges.columns = ['theOne','theOther','correlation']
# remove self correlations
# list, 含 pairwise correlation信息
edges = edges.loc[edges['theOne'] != edges['theOther']].copy()
# undirected graph with weights corresponding to the correlation magnitude
G0 = nx.from_pandas_edgelist(edges, 'theOne', 'theOther', edge_attr=['correlation'])

print(nx.info(G0))
# Number of nodes: 797
# Number of edges: 316985
# Average degree: 795.4454

# =============================================================================
# 原始图
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
# plt.title("Spring layout")

# 4
nx.draw(G0, with_labels=True, node_size=50,
        edge_color='#363847',  pos=nx.spectral_layout(G0))
plt.title("Spectral layout")
plt.show()

# =============================================================================
# 非系统风险的相关问题
# =============================================================================
    
# (1)which assets show strong/meaningful correlations (i.e. >0.5) with each other?

# (2)are these correlations positive or negative?

# (3)which are the most/least ‘connected’ assets?
# (i.e. which assets share the most/least strong correlations with others)

# (4)which groups of assets behave similarly?
# (i.e. which assets are correlated with the same type of other assets)

# =============================================================================
# 对原始图的优化--threshold 
# =============================================================================

# 'winner takes all' method - set minium correlation threshold to remove some edges
threshold = 0.5

# create a new graph from edge list
Gx = nx.from_pandas_edgelist(edges, 'theOne', 'theOther',
                             edge_attr=['correlation'])

# list to store edges to remove
remove = []
# loop through edges in Gx and find correlations which are below the threshold
for theOne, theOther in Gx.edges():
    corr = Gx[theOne][theOther]['correlation']
    #add to remove node list if abs(corr) < threshold
    if abs(corr) < threshold:
        remove.append((theOne, theOther))

# remove edges contained in the remove list
Gx.remove_edges_from(remove)

print(str(len(remove)) + " edges removed")
# 原来有318580条
# 删除了317708条
#%%

# =============================================================================
# improved graph 2--node(颜色+degree)，edge粗细
# =============================================================================

# 根据correlation的正负赋值颜色
def assign_colour(correlation):
    if correlation <= 0:
        return "#ffa09b"  # red
    else:
        return "#9eccb7"  # green
    
# 根据correlation标量大小赋值粗细
def assign_thickness(correlation, benchmark_thickness=2, scaling_factor=3):
    return benchmark_thickness * abs(correlation)**scaling_factor

def assign_node_size(degree, scaling_factor=50):
    return degree * scaling_factor


edge_colours = []
edge_width = []
for key, value in nx.get_edge_attributes(Gx, 'correlation').items():
    edge_colours.append(assign_colour(value))
    edge_width.append(assign_thickness(value))

# 赋值 node size (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))

# 绘图
sns.set(rc={'figure.figsize': (12, 12)})
font_dict = {'fontsize': 15}

# nx.draw(Gx, pos=nx.circular_layout(Gx), with_labels=True,
#         node_size=node_size, edge_color=edge_colours,
#         width=edge_width)
# plt.title("Корреляции цен активов (круговой)", fontdict=font_dict)
# plt.show()

nx.draw(Gx, pos=nx.fruchterman_reingold_layout(Gx), with_labels=True,
        node_size=node_size, edge_color=edge_colours,
       width = edge_width)
plt.title("Корреляции цен активов - Fruchterman-Reingold layout",
          fontdict=font_dict)
plt.show()

# nx.draw(Gx, pos=nx.circular_layout(Gx), with_labels=True,
#         node_size=node_size, edge_color=edge_colours,
#         width=edge_width)
# plt.title("Корреляции цен активов (случайный)", fontdict=font_dict)
# plt.show()
