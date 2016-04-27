# File: gradient_descent.py
# Course: Boston University CS330 - Algorithms Spring 2016 Assignment 7 Question 4
# Authors: Nicholas Louie (nlouie@bu.edu), Satoe Sakuma ( ), Pauline Ramirez (pgr@bu.edu)
# Created: 4/26/16
# Due: 4/28/16 7pm
# Description: Generates an initial random solution S. For each k iterations, considers a random move
# to a neighbor S' of the current solution S. If the residue r(S') is less than r(S), sets S to S'
# returns the final and best S.
# The random move defined for gradient descent is as follows: choose random i and j from [1,n] s.t. i != j
# Set S_i to -S_i and with probability 1/2 set S_j to -S_j


import controller



def gradient_descent(A, k):
    for x in range(K):
        # Choose an i and j
        i = random.randint(0, len(A))
        j = random.randint(0, len(A))
        # Make sure they're not the same
        while (i == j):
            j = random.randint(0, len(A))
        A[i] = -1 * A[i]
        # Probability of 1/2 to set A[j] to -A[j]
        rand = random.random()
        if rand > 0.5:
            A[j] = -1 * A[j]
        else:
            pass
        
        

# eof
