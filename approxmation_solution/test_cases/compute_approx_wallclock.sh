#!/bin/bash

# Program to test
# PROGRAM="../../exact_solution/cs412_max3sat_exact.py"
PROGRAM="../cs412_max3sat_approx.py"


# Output results file
RESULTS_FILE="wall_clock_tests/approx_results.txt"

# Initialize the results file
> "$RESULTS_FILE"
echo "Test Results" >> "$RESULTS_FILE"
echo "-----------------------------" >> "$RESULTS_FILE"

# List of test case files
TEST_CASES=("test3" "test5" "test8" "test10" "test12" "test15" "test17"
            "test20" "test21" "test22" "test23" "test24" "test25" "test26" "test28" "test29" "test30")

# Loop over all test cases
for TEST_CASE in "${TEST_CASES[@]}"
do
    INPUT_FILE="wall_clock_tests/${TEST_CASE}.txt"

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
    python3 "$PROGRAM" < "$INPUT_FILE" > "$OUTPUT"
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
