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
import random


def gradient_descent(A, k):
    # Get a random solution
    S = controller.generate_random_solution(A)
    # Get the residue of the solution
    smallest_residue = controller.residue(A, S)
    
    for x in range(k):        
        # Choose an i and j
        i = random.randint(0, len(S))
        j = random.randint(0, len(S))
        # Make sure they're not the same
        while (i == j):
            j = random.randint(0, len(S))
        S[i] = -1 * S[i]
        # Probability of 1/2 to set A[j] to -A[j]
        rand = random.random()
        if rand > 0.5:
            S[j] = -1 * S[j]
        r = controller.residue(A, S)

        # Compare the residues
        if abs(r) < abs(smallest_residue):
            smallest_residue = r
    return smallest_residue
        

# eof
