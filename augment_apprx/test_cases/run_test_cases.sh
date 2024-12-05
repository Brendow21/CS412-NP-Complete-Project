#!/bin/bash

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"
UL="\e[430m"

echo -e "${BOLD}Test cases:"
echo -e "\t${BOLD}test\tresult\truntime${NC}"

PROG_TO_TEST=cs412_max3sat_augment.py

for test in test*
do 
    cd $test
    start = `python3 -c 'import time; print(time.time())'`
    python3 ../${PROG_TO_TEST} < input.txt > output.txt
    end= `python3 -c 'import time; print(time.time())'`

    if [ "$(head -n 2 expected.txt)" = "$(head -n 2 output.txt)" ]
    then
        echo -e "\t${test}\t${GREEN}passed\t${BLUE}${runtime}s${NC}"
    else
        echo -e "\t${test}\t${RED}failed\t${BLUE}${runtime}s${NC}"
    fi

    cd ../
done

exit 0