# File: simulated_annealing.py
# Course: Boston University CS330 - Algorithms Spring 2016 Assignment 7 Question 4
# Authors: Nicholas Louie (nlouie@bu.edu), Satoe Sakuma ( ), Pauline Ramirez ( )
# Created: 4/26/16
# Due: 4/28/16 7pm
# Description: Generates an initial random solution S. For each k iterations, considers a random move
# to a neighbor S' of the current solution S. Simulated Annealing accepts worse moves with
# Pr[r(S') > r(S)] = e^((-r(S') - r(S))/T(i)) where T(i) = (10^10)*(0.8)^(floor(i/300))
# Returns the smallest residue seen over all iterations

import controller


def simulated_annealing(A, k):
    pass

# eof
