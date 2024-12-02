"""
    name: Brendan Hom
    Max 3-Sat Approximation Solution

    n: Number of variables.
    m: Number of clauses.
    L: Maximum iterations of the while loop in main.

    Strategy Idea: 
        1. Randomization
        Assign random Boolean values to each variable.

        2. Incremental Improvement
        Iteratively flip the truth value of each variable one at a time. 
        After each flip, compute the new number of satisfied clauses.
        Retain the flip if it improves the solution; otherwise, revert the flip.

        3. Stopping Conditions
        The algorithm attempts to improve the solution incrementally over multiple iterations.
        It stops either when no further improvement is made after 5 consecutive iterations or 
        when all clauses are satisfied (best_count == m).

    Runtime:
    1. Initial random assignment: O(n)
    2. Checking satisfaction of all clauses after a flip: O(m)
    3. Flipping each variable iteratively: O(n * m)

    Time Complexity: O(n * m)
"""
import random

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

def max_3sat_approx(n, clauses, assignments):
    """Try to improve the current assignment by flipping one variable at a time."""
    best_count = 0
    num_loops = 0
    while num_loops < 5:
        for var in range(1, n + 1):
            # Flip the variable
            assignments[var] = not assignments[var]
            current_count = calculate_satisfied_clauses(clauses, assignments)

            # If flipping improves, keep the change; otherwise, revert
            if current_count > best_count:
                best_count = current_count
                num_loops = 0  # Reset loop counter if improvement is made
            else:
                assignments[var] = not assignments[var]  # Revert flip
                num_loops += 1

    return best_count

def main():
    n, m = map(int, input().strip().split())
    clauses = [tuple(map(int, input().strip().split())) for _ in range(m)]

    # Initialize random assignments
    assignments = {var: random.choice([True, False]) for var in range(1, n + 1)}

    # Print best count
    print(max_3sat_approx(n, clauses, assignments))

    # Output the variable assignments
    for var in range(1, n + 1):
        print(f"{var} {'T' if assignments[var] else 'F'}")

if __name__ == "__main__":
    main()
