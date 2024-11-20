import random

# Number of variables (n) and clauses (m)
n = 10
m = 100

# Generate m clauses, each with 3 random literals
clauses = []
for _ in range(m):
    clause = [random.choice([i, -i]) for i in random.sample(range(1, n+1), 3)]
    clauses.append(clause)

# Print the input in the required format
print(f"{n} {m}")
for clause in clauses:
    print(" ".join(map(str, clause)))
