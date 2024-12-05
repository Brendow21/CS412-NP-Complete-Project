Exact solution Instructions

Before Use:
    1. Open Git Bash Terminal (Unless already open)
    Change directory to ../exact_solution/test_cases

Modify Test Cases:

    The script uses the TEST_CASES array to determine which test files to process.
    Uncomment the desired set of test cases (Quick Test, Short Length, Medium Length, etc.) by removing the # character from the appropriate line.
    Only have one line of test cases uncommented at a time.
    Example:

        To run the short-length test, update the script as follows:

        TEST_CASES=("test25")

Execute the script by running:

    ./run_test_script.sh
    
Check the Results:

    The script writes the results to a file named results.txt in the current directory.
    
    Open results.txt to view:
        
        Test Case Name
        Execution Time
        Number of Satisfied clauses
        The Best Assignments


Importance of the NP-hard Problem:

    Max 3-SAT is an NP-hard optimization problem, meaning it has no known polynomial-time solution unless 𝑃=𝑁𝑃. 
    This makes it a critical benchmark for testing optimization algorithms, heuristics, and approximation techniques.

Applications:
    Artificial Intelligence and Machine Learning:

        Reasoning and Inference:
            Max 3-SAT is often used in AI systems for logical reasoning and decision-making, such as designing systems that infer conclusions from a large number of rules.
        
        Feature Selection:
            In machine learning, Boolean formulas can model the relationship between features and outcomes. Max 3-SAT optimizations are used to select a subset of features that satisfy the most constraints.
    
    Circuit Design and Verification:

        Logic Circuit Optimization:
            Circuit design involves ensuring that logical components operate as intended. Max 3-SAT helps in minimizing unsatisfied logical constraints during optimization.
