#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
SCORE OF 38/60. 63.3 %
TRY NEIGHBOHOOD SWAPING
'''
from collections import Counter


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    #print('001 start. \n Node & Vertice \n', input_data)
    lines = input_data.split('\n') # ['4 3', '0 1', '1 2', '1 3', '']
   
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
        table[parts[0]] = [None]
        table[parts[1]] = [None]

        if parts[0] not in node_nei: 
            
            node_nei[parts[0]] = [parts[1]]
        else : 
            
            node_nei[parts[0]] = node_nei[parts[0]] + [parts[1]]

        # there are instances where node is not in the first part, hence count
        if parts[1] not in node_nei: 
            
            node_nei[parts[1]] = [parts[0]]

        else : 
            
            node_nei[parts[1]] = node_nei[parts[1]] + [parts[0]]

    count_nodes = dict()
    for k,v_ in node_nei.items():
        v = str(len(v_))
        if v in count_nodes:
            count_nodes[v] = count_nodes[v] + [k]
        
        else:
            count_nodes[v] = [k]

               
    node_order = sorted(list(count_nodes.keys()), reverse= True)
    #print('004 order', node_order)
    assment = [None] * node_count
    index, colors, explored = 0, 0, set(())
    order = []

    for x in node_order: # order ['19', '18', '17', '16', '15', '14', '12']
        n_list = count_nodes[x] # node list with x neightbors
        count, next_ = int(x), None
        
        iter_ = len(n_list)
        for y in range(iter_ ):# there's an item that will be skipped if you use n_list
            n_list_2 = [x for x in n_list if x not in explored]
            cvb = {x:len(v) for x, v in table.items() if x in n_list_2}
            #print('cvb',cvb)
            cvb = min(cvb.items(), key= lambda x : x[1] )
            #print('cvb',cvb)
            
            next_ = cvb[0] 
            explored.add(next_)
            # assign color to x
            # min size of table
            i = table[next_].index(None)
            table[next_].insert(i, i) # replace with index, push everything by +1
            #explored.add(table[N[0]])
            #print('----', table, i, N[0])
            assment[int(next_)] = i 
            # get neighbors of next_
            c_nodes = node_nei[next_] #['16'] 16 ['0', '2', '4', '5', '6', '8', '9', '10', '11', '13', '15', '18']
            #print('--inner--', next_, c_nodes, table ) 
            order.append(next_)
            # propergate the constraint
            for x in c_nodes:
                #print('c_node 00', i, (i- len(table[x])),table[x] , any(list(range(0, y))) not in table[x])
                if len(table[x]) <= i: # padding
                    table[x] = table[x] + [None] + [None] * abs(i- len(table[x]))
                    #print('c_node 001', table[x])
                        
                    #print('c_node 003', i ,table[x] )

                if table[x][i] == None: # replace with -
                    table[x][i] = '_'
                    table[x].append(None)
                    #print('c_node 002', table[x])
                
            colors = max(i, colors)

    #print(table)               
    output_data = str(colors+1) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, assment))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    file_location = "C:/Users/paul kuria/Documents/coloring/data/gc_50_9" #gc_20_1, gc_4_1, gc_20_3, gc_20_7, gc_50_7,gc_50_9, gc_1000_7
    with open(file_location, 'r') as input_data_file: #gc_70_1
            input_data = input_data_file.read()
            print('----final---',solve_it(input_data))

