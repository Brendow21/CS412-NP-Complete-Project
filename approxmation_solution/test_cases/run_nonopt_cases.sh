#!/bin/bash

# Programs to test
PROGRAM_APPROX="../cs412_max3sat_approx.py"
PROGRAM_EXACT="../../exact_solution/cs412_max3sat_exact.py"

# Output results file
RESULTS_FILE="non_optimal/nonopt_results.txt"

# Initialize the results file
> "$RESULTS_FILE"
echo "Test Results" >> "$RESULTS_FILE"
echo "-----------------------------" >> "$RESULTS_FILE"

# List of test case files
TEST_CASES=("non_optimal/test_nonopt")

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

    # Check if both programs exist
    if [ ! -f "$PROGRAM_APPROX" ] || [ ! -f "$PROGRAM_EXACT" ]; then
        echo "One or both programs not found. Exiting." >> "$RESULTS_FILE"
        exit 1
    fi

    # Run the approximate solution program
    OUTPUT_APPROX=$(mktemp)
    python3 "$PROGRAM_APPROX" < "$INPUT_FILE" > "$OUTPUT_APPROX"
    SATISFIED_CLAUSES_APPROX=$(head "$OUTPUT_APPROX")

    # Run the exact solution program
    OUTPUT_EXACT=$(mktemp)
    python3 "$PROGRAM_EXACT" < "$INPUT_FILE" > "$OUTPUT_EXACT"
    SATISFIED_CLAUSES_EXACT=$(head "$OUTPUT_EXACT")

    # Append results to the file for both programs
    {
        echo "Test case: $TEST_CASE"
        echo "Approximate solution:"
        echo "Satisfied clauses: $SATISFIED_CLAUSES_APPROX"
        echo "Exact solution:"
        echo "Satisfied clauses: $SATISFIED_CLAUSES_EXACT"
        echo "-----------------------------"
    } >> "$RESULTS_FILE"

    # Cleanup temporary output files
    rm "$OUTPUT_APPROX" "$OUTPUT_EXACT"
done

echo "Results written to $RESULTS_FILE"
