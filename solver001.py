#!/usr/bin/python
# -*- coding: utf-8 -*-


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
            
    #print('002', edges)
    #print('003', table)
    #print('004', neighbor_count)

    # sort nodes according to number of linked neighbors
    neighbor_count = sorted(neighbor_count.items(), key= lambda x: x[1], reverse= True )
    #print('004 order', neighbor_count)
    assment = [None] * len(neighbor_count)
    index, colors, explored = 0, 0, set()
    for N in neighbor_count: # (node, count)  [('10', 10), ('4', 9), ('2', 9), ('11', 9), ('9', 9),]
        c_nodes = [x for x in edges if int(N[0]) in x] # get all adjacent neighbors from edge
        #print('005',c_nodes, table, N[0])

        if (None in table[N[0]]): # 1st pass will always have None
            i = table[N[0]].index(None)
            table[N[0]].insert(i, i) # replace with index, push everything by +1
            #explored.add(table[N[0]])
            #print('----', table, i, N[0])
            assment[int(N[0])] = i 
            # propergate the constraint
            for x in c_nodes:
                if x[0] != N[0] : 
                    if len(table[str(x[0])]) <= i:
                        #padding to allow indexing
                        table[str(x[0])] = table[str(x[0])] + [None] * (i-(len(table[str(x[0])])-1))
                    
                    
                    if table[str(x[0])][i] == None: # replace with o
                        table[str(x[0])][i] = '_'
                        table[str(x[0])].append(None)
                    
                    #print('--A--', table[str(x[0])], N,x,i )

                    
                if x[1] != N[0] : 
                    if len(table[str(x[1])]) <= i:
                        #padding to allow indexing
                        table[str(x[1])] = table[str(x[1])] + [None] * (i-(len(table[str(x[1])])-1))

                   
                    if table[str(x[1])][i] == None: # replace with 0
                        table[str(x[1])][i] = '_'
                        table[str(x[1])].append(None)

                    #print('--B--', table[str(x[1])], N , x, i)

        colors = max(i, colors)
        index += 1
        

    #print('final', assment  )

    # build a trivial solution
    # every node has its own color
    #solution = range(0, node_count)

    # prepare the solution in the specified output format
    output_data = str(colors+1) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, assment))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    file_location = "C:/Users/paul kuria/Documents/coloring/data/gc_20_9" #gc_20_1, gc_4_1, gc_20_3, gc_20_7, gc_50_7,gc_50_9, gc_1000_7
    with open(file_location, 'r') as input_data_file: #gc_70_1
            input_data = input_data_file.read()
            print('----final---',solve_it(input_data))

