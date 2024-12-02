"""
    name: Brendan Hom
    Max 3-Sat Approximation Solution

    n: Number of variables.
    m: Number of clauses.
    L: Maximum iterations of the while loop in main.

    Strategy Idea: 
        1. Randomized Approximation
        Assign random Boolean values to each variable.
        Each iteration computes how many clauses are satisfied under the current assignment.
        
        2. Repeated Attempts
        The algorithm repeats the random assignment process up to 10.
        It retains the "best count" of satisfied clauses across all iterations.
        
        3. Stopping Conditions
        Stops if all cluases are satisfied (best_count == m) or
        It completes L iterations without improvement.

    Runtime: 
    1. Assignment of truth values to each variable: O(n)
    2. Checking each cluase to see if it is satisfied: O(m)
    
    Time Complexity: O(n + m)
"""
import random

def max_3sat_approx(n, clauses):
    # Assign random truth values to each variable
    assignments = {var: random.choice([True, False]) for var in range(1, n + 1)}
    satisfied_count = 0

    for clause in clauses:
        # Check if the clause is satisfied
        for literal in clause:
            if ((literal > 0 and assignments[abs(literal)]) or
            (literal < 0 and not assignments[abs(literal)])):
                satisfied_count += 1
                break

    return satisfied_count, assignments

def main():
    n, m = map(int, input().strip().split())
    clauses = [tuple(map(int, input().strip().split())) for _ in range(m)]
    best_count = 0
    num_loops = 0

    while (num_loops < 10):
        current_count, assignments = max_3sat_approx(n, clauses)
        if current_count > best_count:
            best_count = current_count
            num_loops = 0
        if (best_count == m):
            break
        num_loops += 1

    # Print Best count
    print(best_count)
    # Output the variable assignments
    for var in range(1, n + 1):
        print(f"{var} {'T' if assignments[var] else 'F'}")

if __name__ == "__main__":
    main()
