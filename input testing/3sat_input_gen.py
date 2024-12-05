import random

# Number of variables (n) and clauses (m)
n = 3
m = 20

# Generate m clauses, each with 3 random literals
clauses = []
for _ in range(m):
    clause = [random.choice([i, -i]) for i in random.sample(range(1, n+1), 3)]
    clauses.append(clause)

# Save to file
file = open("test1.txt", "w")

# Print the input in the required format
file.write(f"{n} {m}\n")
for clause in clauses:
    file.write(" ".join(map(str, clause)))
    file.write("\n")

file.close()