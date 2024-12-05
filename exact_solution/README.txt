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
        
        Test case name
        Execution time
        Number of satisfied clauses
