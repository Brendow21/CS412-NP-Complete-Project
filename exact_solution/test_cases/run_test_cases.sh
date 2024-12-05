#!/bin/bash

# Program to test
PROGRAM="../cs412_max3sat_exact.py"

# Output results file
RESULTS_FILE="results.txt"

# Initialize the results file
> "$RESULTS_FILE"
echo "Test Results" >> "$RESULTS_FILE"
echo "-----------------------------" >> "$RESULTS_FILE"

# List of test cases

# Quick Test Set (Average Time: >3 Minutes)
 TEST_CASES=("test20" "test21" "test22" "test23" "test24")

# Short Length Test (Average Time: ~3 Minutes )
# TEST_CASES=("test25")

# Medium Length Test (Average Time: ~6 Minutes )
# TEST_CASES=("test26")

# Long Length Test (Average Time: ~10 Minutes )
# TEST_CASES=("test28")

# -----TEST CASES BELOW WILL TAKE OVER 20 MINUTES EACH-----
# TEST_CASES=("test29")
# TEST_CASES=("test30")

# Loop over all test cases
for TEST_CASE in "${TEST_CASES[@]}"
do
    INPUT_FILE="${TEST_CASE}.txt"

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
    START_TIME=$(date +%s%N)
    OUTPUT=$(mktemp)
    python "$PROGRAM" < "$INPUT_FILE" > "$OUTPUT"
    END_TIME=$(date +%s%N)
    EXECUTION_TIME_MS=$(( (END_TIME - START_TIME) / 1000000 ))
    EXECUTION_TIME_SECONDS=$(awk "BEGIN {printf \"%.3f\", $EXECUTION_TIME_MS / 1000}")
    SATISFIED_CLAUSES=$(head -n 1 "$OUTPUT")

    # Append results to the file
    {
        echo "Test case: $TEST_CASE"
        echo "Execution time: $EXECUTION_TIME_SECONDS seconds"
        echo "Satisfied clauses: $SATISFIED_CLAUSES"
        echo "-----------------------------"
    } >> "$RESULTS_FILE"

    # Cleanup temporary output file
    rm "$OUTPUT"
done

echo "Results written to $RESULTS_FILE" >> "$RESULTS_FILE"