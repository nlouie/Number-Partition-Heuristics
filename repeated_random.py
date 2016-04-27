# File: repeated_random.py
# Course: Boston University CS330 - Algorithms Spring 2016 Assignment 7 Question 4
# Authors: Nicholas Louie (nlouie@bu.edu), Satoe Sakuma (ssakuma@bu.edu), Pauline Ramirez (pgr@bu.edu)
# Created: 4/26/16
# Due: 4/28/16 7pm
# Description: Generates k random solutions to the number partition problem
# and returns the one with the smallest residue





def repeated_random(A, k):
    import controller
    S = controller.generate_random_solution(len(A))
    smallest_residue = controller.residue(A, S)
    for i in range(k - 1):
        S = controller.generate_random_solution(len(A))
        r = controller.residue(A, S)
        if abs(r) < abs(smallest_residue):
            smallest_residue = r
    return smallest_residue

# eof
