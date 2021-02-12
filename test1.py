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
import collections
#%%

# =============================================================================
# 数据处理
# =============================================================================

symbols = list(pd.read_excel('msci2017.xlsx')['Symbol'])
start = '2016-01-01'
end = '2018-01-01'
df = yf.download(symbols,start,end)['Adj Close'] # 30 Failed downloads
df.dropna()
print(df.shape)# (627, 802)
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
# sns.clustermap(corrMatrix1, cmap="RdYlGn")
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
# Number of edges: 317112
# Average degree: 795.7641
#%%
# =============================================================================
# Density
# =============================================================================
def get_density(G):
    # How many possible edges?
    possible_edges = len(G.nodes) * (len(G.nodes) - 1) / 2
    actual_edges = len(G.edges)
    return actual_edges/possible_edges
print(get_density(G0)) #0.9997036626041121
print(nx.node_connectivity(G0)) #779
clustering_coeffs = nx.clustering(G0).values()
average_clustering_coeff = sum(clustering_coeffs)/len(clustering_coeffs)
print(average_clustering_coeff) #0.9997095641879765
print(nx.diameter(G0))
#%%
# =============================================================================
# 原始图
# =============================================================================

# plt.figure(figsize=(7,7))
# 1
# nx.draw(G0, with_labels=True, node_size=200, node_color="#e1575c",
#         edge_color='#363847',  pos=nx.circular_layout(G0))
# plt.title("Circular layout")

# 2
# nx.draw(G0, with_labels=True, node_size=100, node_color="#e1575c",
#         edge_color='#363847',  pos=nx.random_layout(G0))
# plt.title("Random layout")

# # 3
# nx.draw(G0, with_labels=True, node_size=8, alpha=1,
#         edge_color='#363847',arrows=False, pos=nx.spring_layout(G0))
# plt.title("Spring layout")

# # 4
# nx.draw(G0, with_labels=True, node_size=50,
#         edge_color='#363847',  pos=nx.spectral_layout(G0))
# plt.title("Spectral layout")
# plt.show()
#%%


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
# 删除了315764条
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
#%%
# 绘图
sns.set(rc={'figure.figsize': (12, 12)})
font_dict = {'fontsize': 15}

nx.draw(Gx, pos=nx.circular_layout(Gx), with_labels=True,
        node_size=node_size, edge_color=edge_colours,
        width=edge_width)
plt.title("Корреляции цен активов (2016.1.1-2018.1.1) Круговая схема, после удаления 315764 (99,57%) рёбра, корреляция < 0,5", fontdict=font_dict)
plt.show()

nx.draw(Gx, pos=nx.fruchterman_reingold_layout(Gx), with_labels=True,
        node_size=node_size, edge_color=edge_colours,
        width = edge_width)
plt.title("Корреляции цен активов (2016.1.1-2018.1.1) - Fruchterman-Reingold, после удаления 315764 (99,57%) рёбра, корреляция < 0,5",
          fontdict=font_dict)
plt.show()

# nx.draw(Gx, pos=nx.random_layout(Gx), with_labels=True,
#         node_size=node_size, edge_color=edge_colours,
#         width=edge_width)
# plt.title("Корреляции цен активов (2016.1.1-2018.1.1)", fontdict=font_dict)
# plt.show()
#%%
# =============================================================================
# 最小生成树 Kruskal's algos
# =============================================================================
# 在删除低相关系数低edges之后创建最小生成树
mst = nx.minimum_spanning_tree(Gx)
edge_colours = []

# 给edges赋值颜色
for key, value in nx.get_edge_attributes(mst, 'correlation').items():
    edge_colours.append(assign_colour(value))

# # node size 和 width 赋值 constant
# nx.draw(mst, with_labels=True, pos=nx.fruchterman_reingold_layout(mst),
#         node_size=200, edge_color=edge_colours, width = 1.2)
nx.draw(mst, with_labels=True, pos=nx.spectral_layout(mst),
        node_size=200, edge_color=edge_colours, width = 1.2)
plt.title("Корреляции цен активов (2016.1.1-2018.1.1) - Минимальное остовное дерево",
          fontdict=font_dict)
plt.show()
#%%
# =============================================================================
# Partition & Community
# =============================================================================
# partitions = nx.community.girvan_newman(Gx)
# communities = set(partitions.values())
# communities_dict = {c: [k for k, v in partitions.items() if v == c] for c in communities}

# # Filter that dictionary to map community to the node of highest degree within the community
# highest_degree = {k: max(v, key=lambda x: G.degree(x)) for k, v in communities_dict.items()}
# print(partitions)

# modularity = nx.community.quality.modularity(Gx, partitions)
#%%
# partitions = nx.community.greedy_modularity_communities(Gx)
# partitions = nx.community.asyn_lpa_communities(Gx)
# G = nx.karate_club_graph()
# =============================================================================
# 1.Degree centrality
# =============================================================================

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
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10

top_deg_dc,top2_deg_dc,top3_deg_dc,top4_deg_dc,top5_deg_dc,top6_deg_dc,top7_deg_dc,top8_deg_dc,top9_deg_dc,top10_deg_dc  = find_nodes_with_highest_deg_cent(Gx)
print(top_deg_dc,top2_deg_dc,top3_deg_dc,top4_deg_dc,top5_deg_dc,top6_deg_dc,top7_deg_dc,top8_deg_dc,top9_deg_dc,top10_deg_dc)
for node in Gx.nodes():
    print(node, nx.degree_centrality(Gx)[node])

#%%
# =============================================================================
# 2.Eigenvector centrality
# =============================================================================
# Define find_nodes_with_highest_deg_cent()
def find_nodes_with_highest_eig_c(G):

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

    # Iterate over the degree centrality dictionary
    for k, v in eig_c.items():

        # Check if the current value has the maximum degree centrality
        if v == max_1_ec:
            # Add the current node to the set of nodes
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
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10

top_eig_c,top2_eig_c,top3_eig_c,top4_eig_c,top5_eig_c,top6_eig_c,top7_eig_c,top8_eig_c,top9_eig_c,top10_eig_c  = find_nodes_with_highest_eig_c(Gx)
print(top_eig_c,top2_eig_c,top3_eig_c,top4_eig_c,top5_eig_c,top6_eig_c,top7_eig_c,top8_eig_c,top9_eig_c,top10_eig_c)

#%%
# =============================================================================
# 3.Betweenness Centrality
# =============================================================================

def find_nodes_with_highest_bet_cent(G):
    bet_cent = nx.betweenness_centrality(Gx)
    max_1_bc = max(list(bet_cent.values()))
    maxnode1 = set()          
    max_2_bc = list(sorted(bet_cent.values()))[-2]
    max_3_bc = list(sorted(bet_cent.values()))[-3]
    max_4_bc = list(sorted(bet_cent.values()))[-4]
    max_5_bc = list(sorted(bet_cent.values()))[-5]
    max_6_bc = list(sorted(bet_cent.values()))[-6]
    max_7_bc = list(sorted(bet_cent.values()))[-7]
    max_8_bc = list(sorted(bet_cent.values()))[-8]
    max_9_bc = list(sorted(bet_cent.values()))[-9]
    max_10_bc = list(sorted(bet_cent.values()))[-10]

    maxnode2 = set()
    maxnode3 = set()
    maxnode4 = set()
    maxnode5 = set()
    maxnode6 = set()
    maxnode7 = set()
    maxnode8 = set()
    maxnode9 = set()
    maxnode10 = set()

    # Iterate over the degree centrality dictionary
    for k, v in bet_cent.items():

        # Check if the current value has the maximum degree centrality
        if v == max_1_bc:
            # Add the current node to the set of nodes
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
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10

top_deg_bc,top2_deg_bc,top3_deg_bc,top4_deg_bc,top5_deg_bc,top6_deg_bc,top7_deg_bc,top8_deg_bc,top9_deg_bc,top10_deg_bc  = find_nodes_with_highest_bet_cent(G)
print(top_deg_bc,top2_deg_bc,top3_deg_bc,top4_deg_bc,top5_deg_bc,top6_deg_bc,top7_deg_bc,top8_deg_bc,top9_deg_bc,top10_deg_bc)

#%%
# =============================================================================
# 4.Closeness centrality
# =============================================================================

def find_nodes_with_highest_clo_cent(G):
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

    maxnode2 = set()
    maxnode3 = set()
    maxnode4 = set()
    maxnode5 = set()
    maxnode6 = set()
    maxnode7 = set()
    maxnode8 = set()
    maxnode9 = set()
    maxnode10 = set()

    for k, v in clo_cent.items():

        if v == max_1_cc:
            # Add the current node to the set of nodes
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
        if v == max_7_bc:
            maxnode7.add(k)
        if v == max_8_cc:
            maxnode8.add(k)
        if v == max_9_cc:
            maxnode9.add(k)
        if v == max_10_cc:
            maxnode10.add(k)
    return maxnode1,maxnode2,maxnode3,maxnode4,maxnode5,maxnode6,maxnode7,maxnode8,maxnode9,maxnode10

top_clo_cc,top2_clo_cc,top3_clo_cc,top4_clo_cc,top5_clo_cc,top6_clo_cc,top7_clo_cc,top8_clo_cc,top9_clo_cc,top10_clo_cc  = find_nodes_with_highest_bet_cent(G)
print(top_clo_cc,top2_clo_cc,top3_clo_cc,top4_clo_cc,top5_clo_cc,top6_clo_cc,top7_clo_cc,top8_clo_cc,top9_clo_cc,top10_clo_cc)

#%%
# =============================================================================
#  Degree Distribution2
# =============================================================================

def plot_degree_distribution(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    fig, ax = plt.subplots()
    plt.bar(deg, cnt)
    plt.ylabel("Количество") 
    plt.xlabel("Степень или валентность вершины")

plot_degree_distribution(Gx)
plt.title("Распределение степеней (узлов, вершин)(2016.1.1-2018.1.1)",
          fontdict=font_dict)
plt.show()
#%%
G0.degree()
degree_sequence = list(G0.degree())
nb_nodes = n
nb_arr = len(G0.edges())
avg_degree = np.mean(np.array(degree_sequence)[:,1])
med_degree = np.median(np.array(degree_sequence)[:,1])
max_degree = max(np.array(degree_sequence)[:,1])
min_degree = np.min(np.array(degree_sequence)[:,1])
print("Number of nodes : " + str(nb_nodes))
print("Number of edges : " + str(nb_arr))
print("Maximum degree : " + str(max_degree))
print("Minimum degree : " + str(min_degree))
print("Average degree : " + str(avg_degree))
print("Median degree : " + str(med_degree))
#%%
degree_freq = np.array(nx.degree_histogram(G0))
plt.figure(figsize=(12, 8))
plt.stem(degree_freq)
plt.ylabel("Частота")
plt.xlabel("Степень или валентность вершины")
plt.show()
