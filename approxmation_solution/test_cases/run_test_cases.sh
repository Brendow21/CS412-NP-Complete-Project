#!/bin/bash

# Program to test
PROGRAM="../cs412_max3sat_approx.py"

# List of test case files
TEST_CASES=("test100" "test1000" "test10000" "test100000")

# Loop over all test cases
for TEST_CASE in "${TEST_CASES[@]}"
do
    INPUT_FILE="${TEST_CASE}.txt"
    RESULTS_FILE="${TEST_CASE}_results.txt"

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
    SATISFIED_CLAUSES=$(head "$OUTPUT")

    # Append results to the file
    {
        echo "Test case: $TEST_CASE"
        echo "Satisfied Clauses: $SATISFIED_CLAUSES"
        echo "-----------------------------"
    } >> "$RESULTS_FILE"

    # Cleanup temporary output file
    rm "$OUTPUT"
done
