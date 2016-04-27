# File: controller.py
# Course: Boston University CS330 - Algorithms Spring 2016 Assignment 7 Question 4
# Authors: Nicholas Louie (nlouie@bu.edu), Satoe Sakuma ( ), Pauline Ramirez ( )
# Created: 4/26/16
# Due: 4/28/16 7pm
# Description: controller.py controls the entire process of question 4.

# import each heuristic algorithm

import Karmarkar_Karp
import gradient_descent
import repeated_random
import simulated_annealing

# dependencies
import sys, argparse, random

# number of iterations of each heuristic
k = 25000
# number of integers chosen uniformly from [1,10^12]
n = 100
# number of test cases
m = 50

# takes a list of numbers A and a solution set S and returns
# the residue of A given the solution set.


def residue(A, S):
    # check input for empty lists or different len
    if len(A) == 0 or len(S) == 0 or len(A) != len(S):
        print("Invalid Inputs")
        return None
    r = 0
    for i in range(len(A)):
        if A[i] != -1 or A[i] != 1:
            print("Invalid Solution value")
            return None
        r += S[i] * A[i]
    return r



def main(argv):
    #create array of 100 random integers from [1,10^12]
    inst = []
    for i in range(1,n):
        inst.append(random.randint(1,10**12))

def generate_random_solution(n):
    #create an array of 100 integers of either -1 or 1
    x = [-1,1]
    randSol = []
    for i in range (1,n):
        randSol.append(x[random.randint(0,1)])

if __name__ == "__main__":
   main(sys.argv[1:])


# eof
