import itertools
import time


def evaluate_3sat_incomplete(assignments, clauses):
    """
    Evaluate the 3-SAT formula for a given assignment of variables and clauses.

    :param assignments: A list of boolean values representing the truth assignment of variables.
    :param clauses: A list of clauses where each clause is a tuple of literals.
    :return: True if all clauses are satisfied, otherwise False.
    """
    for clause in clauses:
        clause_satisfied = False
        for literal in clause:
            var_index = abs(literal) - 1  # Variables are 1-indexed
            # Get the variable's value from assignments
            value = assignments[var_index]
            if (literal > 0 and value) or (literal < 0 and not value):
                clause_satisfied = True
                break
        if not clause_satisfied:
            return False
    return True


def main():
    # Record the start time
    start_time = time.time()

    n, m = map(int, input().split())

    clauses = [tuple(map(int, input().split())) for _ in range(m)]

    # Generate all possible truth assignments for n variables
    assignments = itertools.product([True, False], repeat=n)

    # Check the 3-SAT formula for satisfiability
    print("\nChecking 3-SAT formula:")
    unsatisfiable = True
    for assignment in assignments:
        if evaluate_3sat_incomplete(assignment, clauses):
            print("Found satisfying assignment:")
            for i, val in enumerate(assignment, 1):
                print(f"x{i}={'T' if val else 'F'}")
            unsatisfiable = False
            break

    if unsatisfiable:
        print("The 3-SAT formula is unsatisfiable.")

    # Record the end time
    end_time = time.time()

    # Calculate the total runtime
    runtime = end_time - start_time
    print(f"\nTotal runtime: {runtime:.6f} seconds")


if __name__ == "__main__":
    main()
