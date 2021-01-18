#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:50:56 2021

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

symbols = list(pd.read_excel('msci2019.xlsx')['Symbol'])
start = '2019-01-01'
end = '2021-01-01'
df2 = yf.download(symbols,start,end)['Adj Close'] # 518, 1339
df2.dropna()
print(df2.shape)
#%%
# =============================================================================
# 取对数
# =============================================================================

logReturns2 = pd.DataFrame()
for col in df2.columns:
    logReturns2[col] = np.log(df2[col]).diff(-1)

# =============================================================================
# edge, nodes准备
# =============================================================================

corrMatrix2 = logReturns2.corr()
edges2 = corrMatrix2.stack().reset_index()
edges2.columns = ['theOne','theOther','correlation']
# remove self correlations
# list, 含 pairwise correlation信息
edges2 = edges2.loc[edges2['theOne'] != edges2['theOther']].copy()
# undirected graph with weights corresponding to the correlation magnitude
G2 = nx.from_pandas_edgelist(edges2, 'theOne', 'theOther', edge_attr=['correlation'])

print(nx.info(G2))
# Number of nodes: 1333
# Number of edges: 887403
# Average degree: 1331.4374

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

# # 4
# nx.draw(G0, with_labels=True, node_size=50,
#         edge_color='#363847',  pos=nx.spectral_layout(G0))
# plt.title("Spectral layout")
# plt.show()

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
Gx2 = nx.from_pandas_edgelist(edges2, 'theOne', 'theOther',
                             edge_attr=['correlation'])

# list to store edges to remove
remove2 = []
# loop through edges in Gx and find correlations which are below the threshold
for theOne, theOther in Gx2.edges():
    corr2 = Gx2[theOne][theOther]['correlation']
    #add to remove node list if abs(corr) < threshold
    if abs(corr2) < threshold:
        remove2.append((theOne, theOther))

# remove edges contained in the remove list
Gx2.remove_edges_from(remove2)

print(str(len(remove2)) + " edges removed")
# 872378 edges removed
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


edge_colours2 = []
edge_width2 = []
for key, value in nx.get_edge_attributes(Gx2, 'correlation').items():
    edge_colours2.append(assign_colour(value))
    edge_width2.append(assign_thickness(value))

# 赋值 node size (degree)
node_size2 = []
for key, value in dict(Gx2.degree).items():
    node_size2.append(assign_node_size(value))
    
#%%
# 绘图
sns.set(rc={'figure.figsize': (12, 12)})
font_dict = {'fontsize': 15}

# nx.draw(Gx2, pos=nx.circular_layout(Gx2), with_labels=True,
#         node_size=node_size2, edge_color=edge_colours2,
#         width=edge_width2)
# plt.title("Корреляции цен активов (2019.1.1-2021.1.1)", fontdict=font_dict)
# plt.show()

# nx.draw(Gx2, pos=nx.fruchterman_reingold_layout(Gx2), with_labels=True,
#         node_size=node_size2, edge_color=edge_colours2,
#         width = edge_width2)
# plt.title("Корреляции цен активов (2019.1.1-2021.1.1) - Fruchterman-Reingold",
#           fontdict=font_dict)
# plt.show()

# nx.draw(Gx2, pos=nx.random_layout(Gx2), with_labels=True,
#         node_size=node_size2, edge_color=edge_colours2,
#         width=edge_width2)
# plt.title("Корреляции цен активов (2019.1.1-2021.1.1)", fontdict=font_dict)
# plt.show()
#%%
# =============================================================================
# 最小生成树 Kruskal's algos
# =============================================================================
# 在删除低相关系数低edges之后创建最小生成树
mst2 = nx.minimum_spanning_tree(Gx2)
edge_colours2 = []

# 给edges赋值颜色
for key, value in nx.get_edge_attributes(mst2, 'correlation').items():
    edge_colours2.append(assign_colour(value))

# node size 和 width 赋值 constant
# nx.draw(mst2, with_labels=True, pos=nx.fruchterman_reingold_layout(mst2),
#         node_size=200, edge_color=edge_colours2, width = 1.2)

nx.draw(mst2, with_labels=True, pos=nx.spectral_layout(mst2),
        node_size=200, edge_color=edge_colours2, width = 1.2)
plt.title("Корреляции цен активов (2019.1.1-2021.1.1) - Минимальное остовное дерево",
          fontdict=font_dict)
plt.show()