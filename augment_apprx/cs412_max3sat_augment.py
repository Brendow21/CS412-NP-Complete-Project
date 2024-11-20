"""
    name:  Gillian Kelly

    Honor Code and Acknowledgments:

    This work complies with the JMU Honor Code.
"""

import time


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
  

def main():
    start_time = time.time()

    # first line is number of variables and number of clauses
    n, m = int(input().strip().split())
    
    adj_list = []
    # read in the next m clauses
    for i in range(m):
        edge_list = list(map(int, input().strip().split()))
        adj_list.append(edge_list)

    # draw edges between each clause 
    for i in range(m):
        x1, x2, x3 = int(input().strip().split())

    # draw an edge between contradicting variables across the clauses

    # run independent set on the ALL possible vertice combinations
    
    # pick one variable from each clause (as long as not contradicting)

    # print results 


    runtime = time.time() - start_time
    print(f"\n Total runtime: {runtime:.6f} seconds \n")

if __name__ == "__main__":
    main()