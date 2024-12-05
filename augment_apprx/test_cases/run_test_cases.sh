#!/bin/bash

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"
UL="\e[430m"

echo -e "${BOLD}Test cases:"
echo -e "\t${BOLD}test\tresult\truntime${NC}"

PROGRAM="../cs412_max3sat_augment.py"

RESULTS_FILE="results.txt"

> "$RESULTS_FILE"
echo "Test Results" >> "$RESULTS_FILE"
echo "-----------------------------" >> "$RESULTS_FILE"

TEST_CASES=("test1", "test2", "test3", "test4", "test5", "test6")

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
exit 0
