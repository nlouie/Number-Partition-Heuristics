# File: simulated_annealing.py
# Course: Boston University CS330 - Algorithms Spring 2016 Assignment 7 Question 4
# Authors: Nicholas Louie (nlouie@bu.edu), Satoe Sakuma (ssakuma@bu.edu), Pauline Ramirez ( )
# Created: 4/26/16
# Due: 4/28/16 7pm
# Description: Generates an initial random solution S. For each k iterations, considers a random move
# to a neighbor S' of the current solution S. Simulated Annealing accepts worse moves with
# Pr[r(S') > r(S)] = e^((-r(S') - r(S))/T(i)) where T(i) = (10^10)*(0.8)^(floor(i/300))
# Returns the smallest residue seen over all iterations

import random
import math


def simulated_annealing(A, k):
    import controller
    # Get random solution
    S = controller.generate_random_solution(len(A))
    # Get residue of solution
    residue_1 = controller.residue(A,S)
    # keep track of smallest_residue
    smallest_residue = residue_1

    for x in range(k):
        i = random.randint(0, len(S)-1)
        j = random.randint(0, len(S)-1)

        # make sure i and j are different
        while i == j:
            j = random.randint(0, len(S)-1)
            if i != j:
                break

        S[i] *= -1

        # change with probability half
        rand = random.uniform(0, 1)
        if rand > 0.5:
            S[j] *= -1

        residue_2 = controller.residue(A, S)

        # compare the two residues
        if abs(residue_2) > abs(residue_1):
            # take the worse residue by e() probability but smallest_residue still keeps track of smallest
            rand1 = random.uniform(0, 1)
            if rand1 < e_prob(i, residue_1, residue_2):
                residue_1 = residue_2

        return smallest_residue

# calculate eprob


def e_prob(i, residue_1, residue_2):
    temp = (10**10)*(.8**math.floor(i/300))
    temp_prob = math.exp(-1 * math.floor(residue_2 - residue_1)/temp)
    return temp_prob

# eof
