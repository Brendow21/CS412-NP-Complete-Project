#!/bin/bash

# Shell script for running tests cases for approximation augmentation

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"
UL="\e[430m"

echo -e "${BOLD}Test cases:"
echo -e "\t${BOLD}test\t\taugment\t\truntime\t\tapprox${NC}"


PROG_TO_TEST=../cs412_max3sat_augment.py

for test in test*
do
    cd $test
    start=`python3 -c 'import time; print(time.time())'`
    python3 ../${PROG_TO_TEST} < input.txt > output.txt
    end=`python3 -c 'import time; print(time.time())'`
    runtime=$( echo "$end - $start" | bc -l )


    if [ "$(head -n 1 expected.txt)" = "$(head -n 1 output.txt)" ]
    then
        echo -e "\t${test}\t\t$(head -n 1 output.txt)\t\t${BLUE}${runtime}s${NC}\t\t$(head -n 1 expected.txt)"
    else
        echo -e "\t${test}\t\t$(head -n 1 output.txt)\t\t${BLUE}${runtime}s${NC}\t\t$(head -n 1 expected.txt)"
    fi

    cd ../

done

exit 0


