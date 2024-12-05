#!/bin/bash

# Program to test
PROGRAM="../cs412_max3sat_approx.py"
# PROGRAM="../../exact_solution/cs412_max3sat_exact.py"


# List of test case files
TEST_CASES=("test100" "test200" "test400" "test600" "test800")

# Loop over all test cases
for TEST_CASE in "${TEST_CASES[@]}"
do
    INPUT_FILE="lower_bound_tests/${TEST_CASE}_clauses.txt"
    # Results for Approx
    RESULTS_FILE="lower_bound_tests/${TEST_CASE}_clauses_approx_results.txt"
    # Results for Exact
    # RESULTS_FILE="lower_bound_tests/${TEST_CASE}_clauses_exact_results.txt"


    # Initialize the results file for each test case
    > "$RESULTS_FILE"
    echo "Test Results for $TEST_CASE" >> "$RESULTS_FILE"
    echo "-----------------------------" >> "$RESULTS_FILE"

    # Check if input file exists
    if [ ! -f "$INPUT_FILE" ]; then
        echo "Input file $INPUT_FILE not found. Skipping test case." >> "$RESULTS_FILE"
        echo "-----------------------------" >> "$RESULTS_FILE"
        continue
    fi

    # Check if the program exists
    if [ ! -f "$PROGRAM" ]; then
        echo "Program $PROGRAM not found. Exiting." >> "$RESULTS_FILE"
        exit 1
    fi

    # Measure execution time and run the program
    OUTPUT=$(mktemp)
    python "$PROGRAM" < "$INPUT_FILE" > "$OUTPUT"
    SATISFIED_CLAUSES=$(head -n 1 "$OUTPUT")
    REMAINING_OUTPUT=$(tail -n +2 "$OUTPUT")

    # Append results to the file
    {
        echo "Test case: $TEST_CASE"
        echo "Satisfied Clauses: $SATISFIED_CLAUSES"
        echo "$REMAINING_OUTPUT"
        echo "-----------------------------"
    } >> "$RESULTS_FILE"

    # Cleanup temporary output file
    rm "$OUTPUT"
done
