Max 3-Sat Approximation
n = number of variables
m = number of clauses

Running Program:
python cs412_max3sat_approx.py

Input:
n m
m clauses

Sample Input:
3 3
3 2 -1
2 -3 -1
3 -2 -1

Sample Output:
3
1 T
2 T
3 T

Class 1: For the approximation, I will be greedy by selecting the best choice at that time by selecting a variable in the current valuse to be True of False in order to satisfy the clause, and if there is more than one variable available, I will randomly pick one of the variables to make True or False to satisfy the clause.

Class 2: Wrote the approximation by randomly assigning True or False to each variable and looping through each clause checking if the caluse is valid. 

Class 3: Reworking approximation to not randomly reassign all variables when looking for a better solution.

Class 4: Worked on writing shell script to write test cases and start making slides for presentation