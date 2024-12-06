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


"""Updates the variables that are in the independent set"""
def update_assignments(maxIndSet, assignments):
    for (i, var) in maxIndSet:
        assignments[abs(var)] = var > 0
    return assignments


""" Builds the adjacency list, moved to separate function for cleanliness"""
def build_graph(clauses):
    adj_list = collections.defaultdict(set)
    clause_map = collections.defaultdict(list)

    for i, (x1, x2, x3) in enumerate(clauses):
        vertices = [(i, x) for x in (x1, x2, x3)]
        for j, v1 in enumerate(vertices):
            adj_list[v1].update(vertices[:j] + vertices[j+1:])

        # Map literals to their clause indices
        for x in (x1, x2, x3):
            clause_map[x].append(i)

    # Add contradicting edges
    for x, clause_indices in clause_map.items():
        for i in clause_indices:
            for j in clause_map[-x]:
                if i != j:
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
    
    i = 0
    best_results = 0
    while i < 5:
        mis = max_ind_set_random(adj_list)

        # refined_mis = local_search_mis(adj_list, mis, clauses, assignments)
        update_assignments(mis, assignments)
        satisifed_clauses = calculate_satisfied_clauses(clauses, assignments)
        if satisifed_clauses > best_results:
            best_results = satisifed_clauses
        
        i += 1

    # print num of satisfied clauses
    formatted = ", ".join(map(str, mis))
    print(f"{satisifed_clauses}")

    # print variables with their assignment
    for var in range(1, n + 1):
        print(f"{var} {'T' if assignments[var] else 'F'}")

if __name__ == "__main__":
    main()