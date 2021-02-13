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
end = '2021-02-12'
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
#%%

def get_density(G):
    # How many possible edges?
    possible_edges = len(G.nodes) * (len(G.nodes) - 1) / 2
    actual_edges = len(G.edges)
    return actual_edges/possible_edges

print(get_density(G2)) 
print(nx.node_connectivity(G2)) 
clustering_coeffs = nx.clustering(G2).values()
average_clustering_coeff = sum(clustering_coeffs)/len(clustering_coeffs)
print(average_clustering_coeff) 
print(nx.diameter(G2))
#%%


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

nx.draw(Gx2, pos=nx.circular_layout(Gx2), with_labels=True,
        node_size=node_size2, edge_color=edge_colours2,
        width=edge_width2)
plt.title("Корреляции цен активов (2019.1.1-2021.2.1) Круговая схема, после удаления 872789 (98,65%) рёбра, корреляция < 0,5", fontdict=font_dict)
plt.show()

nx.draw(Gx2, pos=nx.fruchterman_reingold_layout(Gx2), with_labels=True,
        node_size=node_size2, edge_color=edge_colours2,
        width = edge_width2)
plt.title("Корреляции цен активов (2019.1.1-2021.2.1) Fruchterman-Reingold, после удаления 872789 (98,65%) рёбра, корреляция < 0,5",fontdict=font_dict)
plt.show()

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
plt.title("Корреляции цен активов (2019.1.1-2021.2.1) - Минимальное остовное дерево",
          fontdict=font_dict)
plt.show()

#%%
# Define find_nodes_with_highest_deg_cent()
def find_nodes_with_highest_deg_cent(G):

    deg_cent = nx.degree_centrality(G)
    # Compute the maximum degree centrality: max_dc
    max_1_dc = max(list(deg_cent.values()))
    max_2_dc = list(sorted(deg_cent.values()))[-2]
    max_3_dc = list(sorted(deg_cent.values()))[-3]
    max_4_dc = list(sorted(deg_cent.values()))[-4]
    max_5_dc = list(sorted(deg_cent.values()))[-5]
    max_6_dc = list(sorted(deg_cent.values()))[-6]
    max_7_dc = list(sorted(deg_cent.values()))[-7]
    max_8_dc = list(sorted(deg_cent.values()))[-8]
    max_9_dc = list(sorted(deg_cent.values()))[-9]
    max_10_dc = list(sorted(deg_cent.values()))[-10]
    max_11_dc = list(sorted(deg_cent.values()))[-11] 
    max_12_dc = list(sorted(deg_cent.values()))[-12]
    max_13_dc = list(sorted(deg_cent.values()))[-13] 
    max_14_dc = list(sorted(deg_cent.values()))[-14]
    max_15_dc = list(sorted(deg_cent.values()))[-15] 
    max_16_dc = list(sorted(deg_cent.values()))[-16]
    max_17_dc = list(sorted(deg_cent.values()))[-17] 
    max_18_dc = list(sorted(deg_cent.values()))[-18] 
    max_19_dc = list(sorted(deg_cent.values()))[-19]
    max_20_dc = list(sorted(deg_cent.values()))[-20]
    maxnode1 = set()
    maxnode2 = set()
    maxnode3 = set()
    maxnode4 = set()
    maxnode5 = set()
    maxnode6 = set()
    maxnode7 = set()
    maxnode8 = set()
    maxnode9 = set()
    maxnode10 = set() 
    maxnode11 = set()
    maxnode12 = set() 
    maxnode13 = set()
    maxnode14 = set() 
    maxnode15 = set()
    maxnode16 = set() 
    maxnode17 = set()
    maxnode18 = set()
    maxnode19 = set() 
    maxnode20 = set()
    # Iterate over the degree centrality dictionary
    for k, v in deg_cent.items():

        # Check if the current value has the maximum degree centrality
        if v == max_1_dc:
            # Add the current node to the set of nodes
            maxnode1.add(k)
        if v == max_2_dc:
            maxnode2.add(k)
        if v == max_3_dc:
            maxnode4.add(k)
        if v == max_4_dc:
            maxnode4.add(k)
        if v == max_5_dc:
            maxnode5.add(k)
        if v == max_6_dc:
            maxnode6.add(k)
        if v == max_7_dc:
            maxnode7.add(k)
        if v == max_8_dc:
            maxnode8.add(k)
        if v == max_9_dc:
            maxnode9.add(k)
        if v == max_10_dc:
            maxnode10.add(k)
        if v == max_11_dc:
            maxnode11.add(k)
        if v == max_12_dc:
            maxnode12.add(k)
        if v == max_13_dc:
            maxnode13.add(k)
        if v == max_14_dc:
            maxnode14.add(k)
        if v == max_15_dc:
            maxnode15.add(k)
        if v == max_16_dc:
            maxnode16.add(k)
        if v == max_17_dc:
            maxnode17.add(k)
        if v == max_18_dc:
            maxnode18.add(k)
        if v == max_19_dc:
            maxnode19.add(k)
        if v == max_20_dc:
            maxnode20.add(k)
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10,maxnode11,maxnode12,maxnode13,maxnode14,maxnode15,maxnode16,maxnode17,maxnode18,maxnode19,maxnode20

top_deg_dc,top2_deg_dc,top3_deg_dc,top4_deg_dc,top5_deg_dc,top6_deg_dc,top7_deg_dc,top8_deg_dc,top9_deg_dc,top10_deg_dc,top11_deg_dc,top12_deg_dc,top13_deg_dc,top14_deg_dc,top15_deg_dc,top16_deg_dc,top17_deg_dc,top18_deg_dc,top19_deg_dc,top20_deg_dc  = find_nodes_with_highest_deg_cent(Gx2)
print(top_deg_dc,top2_deg_dc,top3_deg_dc,top4_deg_dc,top5_deg_dc,top6_deg_dc,top7_deg_dc,top8_deg_dc,top9_deg_dc,top10_deg_dc,top11_deg_dc,top12_deg_dc,top13_deg_dc,top14_deg_dc,top15_deg_dc,top16_deg_dc,top17_deg_dc,top18_deg_dc,top19_deg_dc,top20_deg_dc)
# for node in Gx2.nodes():
#     print(node, nx.degree_centrality(Gx2)[node])

#%%
# =============================================================================
# 2.Eigenvector centrality
# =============================================================================
# Define find_nodes_with_highest_deg_cent()
def find_nodes_with_highest_eig_c(Gx):

    eig_c = nx.eigenvector_centrality(Gx, max_iter=1000)
    # Compute the maximum degree centrality: max_dc
    max_1_ec = max(list(eig_c.values()))
    max_2_ec = list(sorted(eig_c.values()))[-2]
    max_3_ec = list(sorted(eig_c.values()))[-3]
    max_4_ec = list(sorted(eig_c.values()))[-4]
    max_5_ec = list(sorted(eig_c.values()))[-5]
    max_6_ec = list(sorted(eig_c.values()))[-6]
    max_7_ec = list(sorted(eig_c.values()))[-7]
    max_8_ec = list(sorted(eig_c.values()))[-8]
    max_9_ec = list(sorted(eig_c.values()))[-9]
    max_10_ec = list(sorted(eig_c.values()))[-10]
    max_11_ec = list(sorted(eig_c.values()))[-11]
    max_12_ec = list(sorted(eig_c.values()))[-12]
    max_13_ec = list(sorted(eig_c.values()))[-13]
    max_14_ec = list(sorted(eig_c.values()))[-14]
    max_15_ec = list(sorted(eig_c.values()))[-15]
    max_16_ec = list(sorted(eig_c.values()))[-16]
    max_17_ec = list(sorted(eig_c.values()))[-17]
    max_18_ec = list(sorted(eig_c.values()))[-18]
    max_19_ec = list(sorted(eig_c.values()))[-19]
    max_20_ec = list(sorted(eig_c.values()))[-20]
    maxnode1 = set()
    maxnode2 = set()
    maxnode3 = set()
    maxnode4 = set()
    maxnode5 = set()
    maxnode6 = set()
    maxnode7 = set()
    maxnode8 = set()
    maxnode9 = set()
    maxnode10 = set()
    maxnode11 = set()
    maxnode12 = set()
    maxnode13 = set()
    maxnode14 = set()
    maxnode15 = set()
    maxnode16 = set()
    maxnode17 = set()
    maxnode18 = set()
    maxnode19 = set()
    maxnode20 = set()

    # Iterate over the degree centrality dictionary
    for k, v in eig_c.items():

        # Check if the current value has the maximum degree centrality
        if v == max_1_ec:
            maxnode1.add(k)
        if v == max_2_ec:
            maxnode2.add(k)
        if v == max_3_ec:
            maxnode4.add(k)
        if v == max_4_ec:
            maxnode4.add(k)
        if v == max_5_ec:
            maxnode5.add(k)
        if v == max_6_ec:
            maxnode6.add(k)
        if v == max_7_ec:
            maxnode7.add(k)
        if v == max_8_ec:
            maxnode8.add(k)
        if v == max_9_ec:
            maxnode9.add(k)
        if v == max_10_ec:
            maxnode10.add(k)
        if v == max_11_ec:
            maxnode11.add(k)
        if v == max_12_ec:
            maxnode12.add(k)
        if v == max_13_ec:
            maxnode13.add(k)
        if v == max_14_ec:
            maxnode14.add(k)
        if v == max_15_ec:
            maxnode15.add(k)
        if v == max_16_ec:
            maxnode16.add(k)
        if v == max_17_ec:
            maxnode17.add(k)
        if v == max_18_ec:
            maxnode18.add(k)
        if v == max_19_ec:
            maxnode19.add(k)
        if v == max_20_ec:
            maxnode20.add(k)
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10,maxnode11,maxnode12,maxnode13,maxnode14,maxnode15,maxnode16,maxnode17,maxnode18,maxnode19,maxnode20

top_eig_c,top2_eig_c,top3_eig_c,top4_eig_c,top5_eig_c,top6_eig_c,top7_eig_c,top8_eig_c,top9_eig_c,top10_eig_c,top11_eig_c,top12_eig_c,top13_eig_c,top14_eig_c,top15_eig_c,top16_eig_c,top17_eig_c,top18_eig_c,top19_eig_c,top20_eig_c  = find_nodes_with_highest_eig_c(Gx2)
print(top_eig_c,top2_eig_c,top3_eig_c,top4_eig_c,top5_eig_c,top6_eig_c,top7_eig_c,top8_eig_c,top9_eig_c,top10_eig_c,top11_eig_c,top12_eig_c,top13_eig_c,top14_eig_c,top15_eig_c,top16_eig_c,top17_eig_c,top18_eig_c,top19_eig_c,top20_eig_c)

#%%
# =============================================================================
# 3.Betweenness Centrality
# =============================================================================

def find_nodes_with_highest_bet_cent(Gx):
    bet_cent = nx.betweenness_centrality(Gx)
    max_1_bc = max(list(bet_cent.values()))
      
    max_2_bc = list(sorted(bet_cent.values()))[-2]
    max_3_bc = list(sorted(bet_cent.values()))[-3]
    max_4_bc = list(sorted(bet_cent.values()))[-4]
    max_5_bc = list(sorted(bet_cent.values()))[-5]
    max_6_bc = list(sorted(bet_cent.values()))[-6]
    max_7_bc = list(sorted(bet_cent.values()))[-7]
    max_8_bc = list(sorted(bet_cent.values()))[-8]
    max_9_bc = list(sorted(bet_cent.values()))[-9]
    max_10_bc = list(sorted(bet_cent.values()))[-10]
    max_11_bc = list(sorted(bet_cent.values()))[-11]
    max_12_bc = list(sorted(bet_cent.values()))[-12]
    max_13_bc = list(sorted(bet_cent.values()))[-13]
    max_14_bc = list(sorted(bet_cent.values()))[-14]
    max_15_bc = list(sorted(bet_cent.values()))[-15]
    max_16_bc = list(sorted(bet_cent.values()))[-16]
    max_17_bc = list(sorted(bet_cent.values()))[-17]
    max_18_bc = list(sorted(bet_cent.values()))[-18]
    max_19_bc = list(sorted(bet_cent.values()))[-19]
    max_20_bc = list(sorted(bet_cent.values()))[-20]
    maxnode1 = set()    
    maxnode2 = set()
    maxnode3 = set()
    maxnode4 = set()
    maxnode5 = set()
    maxnode6 = set()
    maxnode7 = set()
    maxnode8 = set()
    maxnode9 = set()
    maxnode10 = set()
    maxnode11 = set()    
    maxnode12 = set()
    maxnode13 = set()
    maxnode14 = set()
    maxnode15 = set()
    maxnode16 = set()
    maxnode17 = set()
    maxnode18 = set()
    maxnode19 = set()
    maxnode20 = set()
    # Iterate over the degree centrality dictionary
    for k, v in bet_cent.items():

        if v == max_1_bc:
            maxnode1.add(k)
        if v == max_2_bc:
            maxnode2.add(k)
        if v == max_3_bc:
            maxnode4.add(k)
        if v == max_4_bc:
            maxnode4.add(k)
        if v == max_5_bc:
            maxnode5.add(k)
        if v == max_6_bc:
            maxnode6.add(k)
        if v == max_7_bc:
            maxnode7.add(k)
        if v == max_8_bc:
            maxnode8.add(k)
        if v == max_9_bc:
            maxnode9.add(k)
        if v == max_10_bc:
            maxnode10.add(k)
        if v == max_11_bc:
            maxnode11.add(k)
        if v == max_12_bc:
            maxnode12.add(k)
        if v == max_13_bc:
            maxnode13.add(k)
        if v == max_14_bc:
            maxnode14.add(k)
        if v == max_15_bc:
            maxnode15.add(k)
        if v == max_16_bc:
            maxnode16.add(k)
        if v == max_17_bc:
            maxnode17.add(k)
        if v == max_18_bc:
            maxnode18.add(k)
        if v == max_19_bc:
            maxnode19.add(k)
        if v == max_20_bc:
            maxnode20.add(k)
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10,maxnode11,maxnode12,maxnode13,maxnode14,maxnode15,maxnode16,maxnode17,maxnode18,maxnode19,maxnode20

top_deg_bc,top2_deg_bc,top3_deg_bc,top4_deg_bc,top5_deg_bc,top6_deg_bc,top7_deg_bc,top8_deg_bc,top9_deg_bc,top10_deg_bc,top11_deg_bc,top12_deg_bc,top13_deg_bc,top14_deg_bc,top15_deg_bc,top16_deg_bc,top17_deg_bc,top18_deg_bc,top19_deg_bc,top20_deg_bc   = find_nodes_with_highest_bet_cent(Gx2)
print(top_deg_bc,top2_deg_bc,top3_deg_bc,top4_deg_bc,top5_deg_bc,top6_deg_bc,top7_deg_bc,top8_deg_bc,top9_deg_bc,top10_deg_bc,top11_deg_bc,top12_deg_bc,top13_deg_bc,top14_deg_bc,top15_deg_bc,top16_deg_bc,top17_deg_bc,top18_deg_bc,top19_deg_bc,top20_deg_bc)

#%%
# =============================================================================
# 4.Closeness centrality
# =============================================================================

def find_nodes_with_highest_clo_cent(Gx):
    clo_cent = nx.closeness_centrality(Gx)
    max_1_cc = max(list(clo_cent.values()))
    maxnode1 = set()          
    max_2_cc = list(sorted(clo_cent.values()))[-2]
    max_3_cc = list(sorted(clo_cent.values()))[-3]
    max_4_cc = list(sorted(clo_cent.values()))[-4]
    max_5_cc = list(sorted(clo_cent.values()))[-5]
    max_6_cc = list(sorted(clo_cent.values()))[-6]
    max_7_cc = list(sorted(clo_cent.values()))[-7]
    max_8_cc = list(sorted(clo_cent.values()))[-8]
    max_9_cc = list(sorted(clo_cent.values()))[-9]
    max_10_cc = list(sorted(clo_cent.values()))[-10] 
    max_11_cc = list(sorted(clo_cent.values()))[-11]  
    max_12_cc = list(sorted(clo_cent.values()))[-12]
    max_13_cc = list(sorted(clo_cent.values()))[-13]
    max_14_cc = list(sorted(clo_cent.values()))[-14]
    max_15_cc = list(sorted(clo_cent.values()))[-15]
    max_16_cc = list(sorted(clo_cent.values()))[-16]
    max_17_cc = list(sorted(clo_cent.values()))[-17]
    max_18_cc = list(sorted(clo_cent.values()))[-18]
    max_19_cc = list(sorted(clo_cent.values()))[-19]
    max_20_cc = list(sorted(clo_cent.values()))[-20]


    maxnode2 = set()
    maxnode3 = set()
    maxnode4 = set()
    maxnode5 = set()
    maxnode6 = set()
    maxnode7 = set()
    maxnode8 = set()
    maxnode9 = set()
    maxnode10 = set() 
    maxnode11 = set() 
    maxnode12 = set()
    maxnode13 = set()
    maxnode14 = set()
    maxnode15 = set()
    maxnode16 = set()
    maxnode17 = set()
    maxnode18 = set()
    maxnode19 = set()
    maxnode20 = set()

    for k, v in clo_cent.items():

        if v == max_1_cc:
            maxnode1.add(k)
        if v == max_2_cc:
            maxnode2.add(k)
        if v == max_3_cc:
            maxnode4.add(k)
        if v == max_4_cc:
            maxnode4.add(k)
        if v == max_5_cc:
            maxnode5.add(k)
        if v == max_6_cc:
            maxnode6.add(k)
        if v == max_7_cc:
            maxnode7.add(k)
        if v == max_8_cc:
            maxnode8.add(k)
        if v == max_9_cc:
            maxnode9.add(k)
        if v == max_10_cc:
            maxnode10.add(k)
        if v == max_11_cc:
            maxnode11.add(k)
        if v == max_12_cc:
            maxnode12.add(k)
        if v == max_13_cc:
            maxnode13.add(k)
        if v == max_14_cc:
            maxnode14.add(k)
        if v == max_15_cc:
            maxnode15.add(k)
        if v == max_16_cc:
            maxnode16.add(k)
        if v == max_17_cc:
            maxnode17.add(k)
        if v == max_18_cc:
            maxnode18.add(k)
        if v == max_19_cc:
            maxnode19.add(k)
        if v == max_20_cc:
            maxnode20.add(k)
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10,maxnode11,maxnode12,maxnode13,maxnode14,maxnode15,maxnode16,maxnode17,maxnode18,maxnode19,maxnode20

top_clo_cc,top2_clo_cc,top3_clo_cc,top4_clo_cc,top5_clo_cc,top6_clo_cc,top7_clo_cc,top8_clo_cc,top9_clo_cc,top10_clo_cc,top11_clo_cc,top12_clo_cc,top13_clo_cc,top14_clo_cc,top15_clo_cc,top16_clo_cc,top17_clo_cc,top18_clo_cc,top19_clo_cc,top20_clo_cc  = find_nodes_with_highest_clo_cent(Gx2)
print(top_clo_cc,top2_clo_cc,top3_clo_cc,top4_clo_cc,top5_clo_cc,top6_clo_cc,top7_clo_cc,top8_clo_cc,top9_clo_cc,top10_clo_cc,top11_clo_cc,top12_clo_cc,top13_clo_cc,top14_clo_cc,top15_clo_cc,top16_clo_cc,top17_clo_cc,top18_clo_cc,top19_clo_cc,top20_clo_cc)

#%%
# =============================================================================
#  Degree Distribution2
# =============================================================================

# def plot_degree_distribution(G):
#     degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
#     degreeCount = collections.Counter(degree_sequence)
#     deg, cnt = zip(*degreeCount.items())
#     fig, ax = plt.subplots()
#     plt.bar(deg, cnt)
#     plt.ylabel("Количество") 
#     plt.xlabel("Степень или валентность вершины")

# plot_degree_distribution(Gx2)
# plt.title("Распределение степеней (узлов, вершин)(2016.1.1-2019.2.1)",
#           fontdict=font_dict)
# plt.show()

#%%
degree_freq = np.array(nx.degree_histogram(Gx2))
plt.figure(figsize=(12, 8))
plt.stem(degree_freq)
plt.ylabel("Частота(Количество)")
plt.xlabel("Степень или валентность вершины")
plt.title("Распределение степеней (узлов, вершин)(2019.1.1-2021.2.1)",
          fontdict=font_dict)
plt.show()
#%%







