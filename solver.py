#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from copy import deepcopy

### if this fails, back tracking search

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
    neighbor_count = dict()
    neighbor_node_count = dict()
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        table[parts[0]] = [None]
        table[parts[1]] = [None]

        if parts[0] not in neighbor_count: neighbor_count[parts[0]] = 1
        else : neighbor_count[parts[0]] += 1
        # there are instances where node is not in the first part, hence count
        if parts[1] not in neighbor_count: neighbor_count[parts[1]] = 1
        else : neighbor_count[parts[1]] += 1
    
    table_2 = deepcopy(table)
    #print('002', edges)
    #print('003', table)
    #print('004a', neighbor_count, edges)

    # sort nodes according to number of linked neighbors
    neighbor_count = sorted(neighbor_count.items(), key= lambda x: x[1], reverse= True )
    iterations = neighbor_count[0][1]//2
    #print('004 order', neighbor_count, iterations, )

    neighbor_node_count = dict()
    for x in neighbor_count: #[('1', 3), ('0', 1), ('2', 1), ('3', 1)]
        if str(x[1]) not in neighbor_node_count: neighbor_node_count[str(x[1])] = [x[0]]
        else:
            neighbor_node_count[str(x[1])] = neighbor_node_count[str(x[1])] + [x[0]]

    #print('005', neighbor_node_count)

    # develop an sequence of how the nodes will be explored.
    order = []
    explored = {}
    chromatic_no = 10**10
    assment_final = []

    print('iterations',iterations)
    while iterations > 1:
        #random.seed()
        for y in neighbor_node_count.values():
            random.shuffle(y)
            order += y 

        # dont repeat the same order

        #print('006 shuffled', neighbor_node_count)
        #print('007 ordering', order)
        
        assment = [None] * len(neighbor_count)
        index, colors, explored = 0, 0, set()
        for N in order: # (node, count)   ['18', '1', '11', '0', '15', '2', '17', '16', '12', '19', '4', '5', '13', '14', '9', '3', '6', '10', '7', '8']
            c_nodes = [x for x in edges if int(N) in x] # get all adjacent neighbors from edge
            #print('005',c_nodes, table, N)

            if (None in table[N]): # 1st pass will always have None
                i = table[N].index(None)
                table[N][i] =  i # replace with index, push everything by +1
                table[N] += [None]
                #explored.add(table[N])
                #print('----', table, i, N)
                assment[int(N)] = i 
                # propergate the constraint
                for x in c_nodes:
                    if x[0] != N : 
                        if len(table[str(x[0])]) <= i:
                            #padding to allow indexing
                            table[str(x[0])] = table[str(x[0])] + [None] * (i-(len(table[str(x[0])])-1))
                        
                        
                        if table[str(x[0])][i] == None: # replace with o
                            table[str(x[0])][i] = '_'
                            table[str(x[0])].append(None)
                        
                        #print('--A--', table[str(x[0])], N,x,i )

                        
                    if x[1] != N : 
                        if len(table[str(x[1])]) <= i:
                            #padding to allow indexing
                            table[str(x[1])] = table[str(x[1])] + [None] * (i-(len(table[str(x[1])])-1))

                    
                        if table[str(x[1])][i] == None: # replace with 0
                            table[str(x[1])][i] = '_'
                            table[str(x[1])].append(None)

                        #print('--B--', table[str(x[1])], N , x, i)

            colors = max(i, colors) 
            index += 1
        #print('hello a', chromatic_no, colors)
        if chromatic_no > colors:
            #print('hello', chromatic_no, colors)
            chromatic_no = colors
            assment_final = assment
        else:
            chromatic_no = min(colors, chromatic_no) 
        #print(table)
        order = []
        index, colors  = 0, 0
        table = table_2
        iterations -= 1
               

    print('final', assment_final, chromatic_no  )

    # build a trivial solution
    # every node has its own color
    #solution = range(0, node_count)

    # prepare the solution in the specified output format
    output_data = str(chromatic_no +1) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, assment_final))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    file_location = "path_to_files" #gc_20_1, gc_4_1, gc_20_3, gc_20_7, gc_50_7,gc_50_9, gc_1000_7
    with open(file_location, 'r') as input_data_file: #gc_70_1
            input_data = input_data_file.read()
            print('----final---',solve_it(input_data))

