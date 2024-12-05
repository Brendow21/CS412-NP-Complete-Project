import re
import matplotlib.pyplot as plt

# Function to read the file and extract the number of clauses and execution time
def parse_test_results(file_path):
    clauses = []
    runtimes = []

    with open(file_path, 'r') as file:
        data = file.read()

        # Regular expressions to match the relevant data
        test_case_pattern = re.compile(r'Test case: (\S+)')
        time_pattern = re.compile(r'Execution time: (\d+\.\d+) seconds')
        clauses_pattern = re.compile(r'Satisfied clauses: (\d+)')

        # Find all matches
        test_cases = test_case_pattern.findall(data)
        times = time_pattern.findall(data)
        clauses_found = clauses_pattern.findall(data)

        # Convert strings to appropriate types
        for time, clause in zip(times, clauses_found):
            clauses.append(int(clause))
            runtimes.append(float(time))

    return clauses, runtimes

# Function to plot the graph
def plot_results(clauses, runtimes):
    plt.figure(figsize=(10, 6))
    plt.plot(clauses, runtimes, marker='o', linestyle='-', color='b')
    plt.title('Execution Time vs Number of Clauses')
    plt.xlabel('Number of Clauses')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main function
if __name__ == "__main__":
    # Replace 'test_results.txt' with the path to your input file
    file_path = 'test_cases/results.txt'
    clauses, runtimes = parse_test_results(file_path)
    
    # Plot the results
    plot_results(clauses, runtimes)
