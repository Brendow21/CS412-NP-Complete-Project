"""
    name:  Gillian Kelly

    Honor Code and Acknowledgments:

    This work complies with the JMU Honor Code.
"""

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
    # first line contains vertex count
    n = int(input().strip())

    adj_list = []
    # next n lines has vertices and its neighbors
    for i in range(n):
        edge_list = list(map(int, input().strip().split()))
        adj_list.append(edge_list)

    # save the proposed independent set
    independent_set = list(map(int, input().strip().split()))
    # check if given list of verticces is an independent set
    if is_indep_set(n, adj_list, independent_set):
        print("TRUE")
    else:
        print("FALSE")

if __name__ == "__main__":
    main()