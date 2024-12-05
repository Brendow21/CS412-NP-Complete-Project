"""
    name:  Gillian Kelly

    Honor Code and Acknowledgments:

    This work complies with the JMU Honor Code.
"""

import collections
import random
import time


# helper function for determining clause satisfication -- BY BRENDAN!
def calculate_satisfied_clauses(clauses, assignments):
    """Calculate the number of satisfied clauses given the assignments."""
    satisfied_count = 0
    for clause in clauses:
        # Check if the clause is satisfied
        for literal in clause:
            if ((literal > 0 and assignments[abs(literal)]) or
            (literal < 0 and not assignments[abs(literal)])):
                satisfied_count += 1
                break
    return satisfied_count


"""Exponential version of Max Independent Set. This was used to validate my approximation solutions"""
def max_ind_set(graph):
    if len(graph) == 0:
        return []
    
    # select a random vertex from the graph to start
    # v = random.choice(list(graph.keys()))
    # select the first vertex from the graph to start
    v = next(iter(graph))

    # current vertex NOT selected -- make graph without v
    without_v_graph = {k: neighbors - {v} for k, neighbors in graph.items() if k != v}

    without_v = max_ind_set(without_v_graph)
    
    # Current vertex selected - make a new graph without v and its neighbors
    with_v_graph = {k: neighbors - graph[v] for k, neighbors in graph.items() if k != v and k not in graph[v]}

    with_v = [v] + max_ind_set(with_v_graph)

    return max(with_v, without_v, key=len)    


"""Approximation of Max Independent Set that utilized randomization"""
def max_ind_set_random(graph):
    remaining_graph = {k: set(neighbors) for k, neighbors in graph.items()}
    ind_set = []

    while remaining_graph:
        # select random vertex from remaining graph
        v = random.choice(list(remaining_graph.keys()))
        
        # add selected vertex to independent set 
        ind_set.append(v)

        # get all neighbors of v before removing it from the graph
        to_remove = set(remaining_graph[v])
        to_remove.add(v) # include v itself in the removal set

        # remove selected vertex and its neighbors from graph
        for u in to_remove:
            if u in remaining_graph:
                remaining_graph.pop(u)

    return ind_set

""" attempts to add non-conflicting vertices to the MIS and updates solution if it leads to a
    more optimal result """
def mis_local_search(graph, mis, clauses, assignments):
    curr_mis = mis[:]
    improvement = True
    while improvement:
        improvement = False
        for v in list(graph.keys()):
            if v not in curr_mis and all(u not in curr_mis for u in graph[v]):
                improved_mis = curr_mis + [v]
                improved_assgn = update_assignments(improved_mis, assignments.copy())
                if calculate_satisfied_clauses(clauses, improved_assgn) > calculate_satisfied_clauses(clauses, assignments):
                    assignments = improved_assgn
                    curr_mis = improved_mis
                    improvement = True
                    break

    return curr_mis



"""Updates the variables that are in the independent set"""
def update_assignments(maxIndSet, assignments):
    for (i, var) in maxIndSet:
        if var > 0:
            assignments[abs(var)] = True
        else:
            assignments[abs(var)] = False
    return assignments


"""Initialize assignments with the original values of each clause"""
def initialize_assignments(n, m):
    clauses = []
    assignments = {}
    for _ in range(m):
        clause = tuple(map(int, input().strip().split()))
        clauses.append(clause)
        for var in clause:
            var_idx = abs(var)
            var_val = var > 0
            if var_idx not in assignments:
                assignments[var_idx] = var_val
    return clauses, assignments


""" Builds the adjacency list, moved to separate function for cleanliness"""
def build_graph(clauses):
    # read in the next m clauses, and built adj_list with 
    # unqiue vertex name that includes the clause it corresponds to
    adj_list = {}
    for i, (x1, x2, x3) in enumerate(clauses):
        # vertices represented as tuples with (clause #, variable)
        vertices = [(i, x) for x in (x1, x2, x3)]
        for j, v1 in enumerate(vertices):
            if v1 not in adj_list:
                adj_list[v1] = set()
            for k in range(3):
                if j != k:
                    v2 = vertices[k]
                    adj_list[v1].add(v2)

    # add edges between contradicting variables across clauses
    for i, (x1, x2, x3) in enumerate(clauses):
        for x in (x1, x2, x3):
            opp = (i, -x)
            # check if opp in any other clauses
            for j, (y1, y2, y3) in enumerate(clauses):
                if i != j and -x in (y1, y2, y3):
                    adj_list[(i, x)].add((j, -x))
                    adj_list[(j, -x)].add((i, x))

    return adj_list


def main():
    # first line is number of variables and number of clauses
    n, m = map(int, input().strip().split())
    
    clauses = [tuple(map(int, input().strip().split())) for _ in range(m)]

    # clauses, assignments = initialize_assignments(n, m)
    adj_list = build_graph(clauses)

    assignments = {var: False for var in range(1, n + 1)}

    mis = max_ind_set_random(adj_list)

    refined_mis = mis_local_search(adj_list, mis, clauses, assignments)
    update_assignments(refined_mis, assignments)
    satisifed_clauses = calculate_satisfied_clauses(clauses, assignments)

    # print num of satisfied clauses
    formatted = ", ".join(map(str, refined_mis))
    print(f"{satisifed_clauses}")

    # print variables with their assignment
    for var in range(1, n + 1):
        print(f"{var} {'T' if assignments[var] else 'F'}")

if __name__ == "__main__":
    main()