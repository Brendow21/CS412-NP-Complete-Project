"""
    name:  Gillian Kelly

    Honor Code and Acknowledgments:

    This work complies with the JMU Honor Code.
"""

import time
import matplotlib.pyplot as plot
from itertools import product

def is_indep_set(n, adj_list, independent_set):
    # check all vertices in independent set
    for v in independent_set:
        neighbors = adj_list[v]
        # retrieve adjcancy list of v, and check its neighbors
        # aren't in independent set
        for adj_node in neighbors:
            if adj_node in independent_set:
                return False
    
    return True


def max_ind_set(graph):
    if len(graph) == 0:
        return []
    
    # select a vertex from the graph
    v = next(iter(graph))
    
    # delete curr vertex from graph
    graph2 = dict(graph)
    del graph2[v]

    # current vertex NOT selected -- make graph without v
    without_v_graph = {}
    for k in graph:
        if k != v:
            without_v_graph[k] = graph[k] - {v}

    without_v = max_ind_set(without_v_graph)
    
    # Current vertex selected - make a new graph without v and its neighbors
    with_v_graph = {}
    for k in graph:
        if k != v and not k in graph[v]:
            with_v_graph[k] = graph[k] - set(graph[v])

    with_v = [v] + max_ind_set(with_v_graph)

    return max(with_v, without_v, key=len)

# helper function for determining clause satisfication 
    


def main():
    start_time = time.time()

    # first line is number of variables and number of clauses
    n, m = map(int, input().strip().split())
    
    # create adj list where each key is a variable and value is a set of connected nodes
    adj_list = {i: set() for i in range(-n, n+1) if i != 0}

    # create a list of clauses
    clauses = []
    # read in the next m clauses
    for _ in range(m):
        x1, x2, x3 = map(int, input().strip().split())
        clauses.append((x1, x2, x3))
        for x, y in [(x1, x2), (x1, x3), (x2, x3)]:
            adj_list[x].add(y)
            adj_list[y].add(x)
        # add an edge between contradicting variables (x1 and -x1)
        for x in (x1, x2, x3):
            adj_list[x].add(-x)
            adj_list[-x].add(x)

    print(f"\n Given {n} variables with {m} clauses...\n")

    print(f"The graph has the following edges:\n")
    print(f"{adj_list}")

    # run max independent set on the graph
    maxIndSet = max_ind_set(adj_list)
    formatted = ", ".join(map(str, maxIndSet))
    print(f"\n The Max Independent Set is of size '{len(maxIndSet)}' and includes vertices: {formatted}\n")

    # set vertices in independent set to its inverse value

    # determine if 3SAT problem is satisfiable ?
    
    # print num of satisfied clauses
    # print variables with their assignment


    runtime = time.time() - start_time
    print(f"\n Total runtime: {runtime:.6f} seconds \n")

if __name__ == "__main__":
    main()