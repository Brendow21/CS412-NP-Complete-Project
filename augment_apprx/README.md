# Augmentation Approximation Part E and F 
# Gillian Kelly

## Class 11/18
Decided I will be reducing the Max3SAT problem to the Independent Set and write an approximation for Independent Set. 
Delevoped my approach to the problem with includes:
- I will be starting by editing the input for the Lab 17, and perform conversion from 3Sat sentence to a graph.
- I will draw edges between contradicting variables (like 1 and -1)
- I will run independent set on ALL possible vertice combinations and save the best result 
- I will also be keeping track of the runtime to make sure my solution runs in polynomial time 

## Class 11/20:
Worked on implementing the Max-3SAT reduction to independent set. I have got it working, but I just want to make sure that my logic
is correct, so I still need to do some more testing.
- NOTE: after looking over the textbook again, I think I may want to change the way I am interpretting MaxIndSet. In the textbook it mentions
comparing the size of the largest independent set to the number of clauses. I will possibly be adding some more code for these comparisons 

## Class 12/4:
- update graph representation so that vertices have unique names that indicate their clauses, I was going to use letters to represent clauses, but there is a chance that I 
could receive an input that has over 26 clauses, and the English alphabet doesn't have more than 26 letters. So instead I decided to use a tuple representation with the clause number and variable number. 
- Now that I have a graph with no repeating vertices, I was able to run independent set on the graph