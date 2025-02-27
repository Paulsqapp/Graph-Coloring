#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
GRAPH COLORING USING NETWORKX
'''
from collections import Counter
import networkx as nx
#import matplotlib.pyplot as plt
import random

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    #print('001 start. \n Node & Vertice \n', input_data)
    random.seed(20)
    lines = input_data.split('\n') # ['4 3', '0 1', '1 2', '1 3', '']
    G = nx.Graph()  
    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    
    edges = []
    table = dict()
    node_nei = dict()
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        G.add_nodes_from((int(parts[0]), int(parts[1])))
        G.add_edge(int(parts[0]), int(parts[1]))
        
    #color_list = ["gold", "violet", "violet", "violet","limegreen", "limegreen", "darkorange"]
    #print('002', G.edges(), '\n', G.nodes())
    
    #equitable_color(G, num_colors=3) , greedy_color(G, strategy='random_sequential')
    #independent_set , saturation_largest_first , connected_sequential_bfs
    coloring = nx.coloring.greedy_color(G, strategy='random_sequential', interchange=True)
    #coloring= nx.coloring.strategy_random_sequential(G, color_list, seed=10)

    #print('graph',coloring)
   

    order  = [None] * len(coloring)
    #count = 0
    for k,v in coloring.items():
        order[k] = v
                
    #print('003', table)
    #print('003 b', order)
    
    # sort nodes according to number of linked neighbors  
    colors = max(order) +1
    
    #nx.draw_networkx(G,)
    #plt.show()
    
    output_data = str(colors) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, order))

    return output_data

if __name__ == '__main__':
    import sys
    file_location = "data\gc_100_7" #gc_20_1, gc_4_1, gc_20_3, gc_20_7, gc_50_7,gc_50_9, gc_1000_7
    with open(file_location, 'r') as input_data_file: #gc_70_1
            input_data = input_data_file.read()
            print('----final---',solve_it(input_data))

