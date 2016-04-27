# File: controller.py
# Course: Boston University CS330 - Algorithms Spring 2016 Assignment 7 Question 4
# Authors: Nicholas Louie (nlouie@bu.edu), Satoe Sakuma (ssakuma@bu.edu), Pauline Ramirez (pgr@bu.edu)
# Created: 4/26/16
# Due: 4/28/16 7pm
# Description: controller.py controls the entire process of question 4.

# import each heuristic algorithm

import Karmarkar_Karp
import gradient_descent
import repeated_random
import simulated_annealing

# dependencies
import random
import time

# takes a list of numbers A and a solution set S and returns
# the residue of A given the solution set.


def residue(A, S):
    # check input for empty lists or different len
    if len(A) == 0 or len(S) == 0 or len(A) != len(S):
        print("Invalid Inputs")
        return None
    r = 0
    for i in range(len(A)):
        if not (A[i] != -1 or A[i] != 1):
            print("Invalid Solution value")
            return None
        r += S[i] * A[i]
    return abs(r)


def generate_random_ints(n):
    # create array of 100 random integers from [1,10^12]
    inst = []
    for i in range(1,n):
        inst.append(random.randint(1, pow(10, 12)))
    return inst


def generate_random_solution(n):
    # create an array of 100 integers of either -1 or 1
    x = [-1, 1]
    rand_sol = []
    for i in range(n):
        rand_sol.append(x[random.randint(0, 1)])
    return rand_sol


def main():
    # number of iterations of each heuristic
    k = 25000
    # number of integers chosen uniformly from [1,10^12]
    n = 100
    # number of test cases
    m = 50

    # keep for statistics

    kk_exec_times = []
    rr_exec_times = []
    gd_exec_times = []
    sa_exec_times = []

    kk_residues = []
    rr_residues = []
    gd_residues = []
    sa_residues = []

    # write errthang to output file
    with open('output.txt', 'w') as f:
        # for each number of test cases
        f.write("Running controller.py...\nk = " + str(k) + ", n = " + str(n) + ", m = " + str(m) + "\n")
        for i in range(m):
            A = generate_random_ints(n)
            f.write("---------------------- Test case " + str(i) + "--------------------" +
                    "\n**Statistics**\n")
            f.write("A : " + str(A) + "\n")

            # Kamarkar Karp

            kk_start_time = time.time()
            kk_out = Karmarkar_Karp.karmarkar_karp(A)
            kk_end_time = time.time()
            kk_exec_time = kk_end_time - kk_start_time
            kk_exec_times.append(kk_exec_time)
            kk_residues.append(kk_out)
            f.write("Karmarkar Karp Residue: " + str(kk_out) +
                    "\nKarmarkar Karp Exec Time: " + str(kk_exec_time) + "\n")

            # Repeated Random

            rr_start_time = time.time()
            rr_out = repeated_random.repeated_random(A, k)
            rr_end_time = time.time()
            rr_exec_time = rr_end_time - rr_start_time
            rr_exec_times.append(rr_exec_time)
            rr_residues.append(rr_out)
            f.write("Repeated Random Residue: " + str(rr_out) +
                    "\nRepeated Random Exec Time: " + str(rr_exec_time) + "\n")

            # Gradient Descent

            gd_start_time = time.time()
            gd_out_a, gd_out_r = gradient_descent.gradient_descent(A, k)
            gd_out = str(gd_out_a)
            gd_end_time = time.time()
            gd_exec_time = gd_end_time - gd_start_time
            gd_exec_times.append(gd_exec_time)
            gd_residues.append(gd_out_r)
            f.write("Gradient Descent Solution: " + gd_out + "Residue = " + str(gd_out_r) +
                    "\nGradient Descent Exec Time: " + str(gd_exec_time) + "\n")

            # Simulated Annealing

            sa_start_time = time.time()
            sa_out_a, sa_out_r = simulated_annealing.simulated_annealing(A, k)
            # sa_out = str(sa_out_a)
            sa_end_time = time.time()
            sa_exec_time = sa_end_time - sa_start_time
            sa_exec_times.append(sa_exec_time)
            sa_residues.append(sa_out_r)
            f.write("Simulated Annealing Best Residue: " + str(sa_out_r) +
                    "\nSimulated Annealing Exec Time: " + str(sa_exec_time) + "\n")

            f.write("--------------------- End Test case " + str(i) + "-----------------------\n")

        # Comupute and print Total Stats

        kk_avg_exec_time = sum(kk_exec_times) / m
        rr_avg_exec_time = sum(rr_exec_times) / m
        gd_avg_exec_time = sum(gd_exec_times) / m
        sa_avg_exec_time = sum(sa_exec_times) / m

        kk_avg_residue = sum(kk_residues) / m
        rr_avg_residue = sum(rr_residues) / m
        gd_avg_residue = sum(gd_residues) / m
        sa_avg_residue = sum(sa_residues) / m

        f.write("\nAverage Exec Times\nKarmarkar Karp Avg Exec Time: " + str(kk_avg_exec_time) +
                "\nRepeated Random Avg Exec Time: " + str(rr_avg_exec_time) +
                "\nGradient Descent Avg Exec Time: " + str(gd_avg_exec_time) +
                "\nSimulated Annealing Avg Exec Time: " + str(sa_avg_exec_time)
                )

        f.write("\nAverage Residues\nKarmarkar Karp Avg Residue: " + str(kk_avg_residue) +
                "\nRepeated Random Avg Residue: " + str(rr_avg_residue) +
                "\nGradient Descent Avg Residue: " + str(gd_avg_residue) +
                "\nSimulated Annealing Residue: " + str(sa_avg_residue)
                )

main()

# eof
