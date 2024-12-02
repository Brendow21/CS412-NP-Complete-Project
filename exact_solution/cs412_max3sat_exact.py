"""
    name: Jerry Huang

    Honor Code and Acknowledgments:

    This work complies with the JMU Honor Code.
"""

import itertools  # To generate all possible truth assignments


def max_3SAT(assignments, clauses):
    """
    Count the number of satisfied clauses for a given assignment.

    :param assignments: A list of boolean values representing the truth assignment of variables.
    :param clauses: A list of clauses where each clause is a tuple of literals.
    :return: The number of clauses satisfied by the given assignment.
    """
    satisfied_count = 0  # Counter for satisfied clauses
    for clause in clauses:
        for literal in clause:
            # Convert 1-indexed variable to 0-indexed for assignments
            var_index = abs(literal) - 1
            # Retrieve the truth value of the variable
            value = assignments[var_index]
            # Check if the literal satisfies the clause
            if (literal > 0 and value) or (literal < 0 and not value):
                satisfied_count += 1  # Increment count if the clause is satisfied
                break  # Move to the next clause once satisfied
    return satisfied_count


def main():

    # Read number of variables (n) and number of clauses (m)
    n, m = map(int, input().split())

    # Read the clauses as tuples of literals
    clauses = [tuple(map(int, input().split())) for _ in range(m)]

    # Generate all possible truth assignments for n variables
    assignments = itertools.product([True, False], repeat=n)

    max_satisfied = 0  # Track the maximum number of satisfied clauses
    best_assignment = None  # Store the assignment that satisfies the most clauses

    for assignment in assignments:
        # Count how many clauses are satisfied by the current assignment
        satisfied_count = max_3SAT(assignment, clauses)
        # Update the best assignment if this one satisfies more clauses
        if satisfied_count > max_satisfied:
            max_satisfied = satisfied_count
            best_assignment = assignment

    # Print the results
    print(f"\n{max_satisfied}")
    if best_assignment:
        # Print the satisfying assignment in the format x1, x2, ..., xn
        for i, val in enumerate(best_assignment, 1):
            print(f"{i} {'T' if val else 'F'}")


if __name__ == "__main__":
    main()  # Run the main function
