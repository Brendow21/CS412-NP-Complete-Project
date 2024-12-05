#!/bin/bash

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"
UL="\e[430m"

# echo -e "${BOLD}Test cases:"
# echo -e "\t${BOLD}test\tresult\truntime${NC}"

PROGRAM="../cs412_max3sat_augment.py"


TEST_CASES=("test1", "test2", "test3", "test4", "test5", "test6")

for TEST_CASE in "${TEST_CASES[@]}"
do
    INPUT_FILE="${TEST_CASE}.txt"
    RESULTS_FILE="${TEST_CASE}_results.txt"

    #initialize result file
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
        echo "Satisfied clauses: $SATISFIED_CLAUSES"
        echo "$REMAINING_OUTPUT"
        echo "-----------------------------"
    } >> "$RESULTS_FILE"

    # Cleanup temporary output file
    rm "$OUTPUT"
done

