"""


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
        print(current_count)
        if current_count > best_count:
            best_count = current_count
            num_loops = 0
        if (best_count == m):
            break
        num_loops += 1

    # Output the number of satisfied clauses
    print()
    print(best_count)
    # Output the variable assignments
    for var in range(1, n + 1):
        print(f"{var} {'T' if assignments[var] else 'F'}")

if __name__ == "__main__":
    main()
