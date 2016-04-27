### Controller

```python
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

    controller_start_time = time.time()

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

        controller_end_time = time.time()
        controller_exec_time = controller_end_time - controller_start_time

        # Compute and print Total Stats

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

        f.write("\n Total Execution Time: " + str(controller_exec_time))

main()

# eof
```

### Karmarkar Karp

```python
# File: Karmarkar_Karp.py
# Author: Nicholas Louie (nlouie@bu.edu), Jennifer Tsui (jgtsui@bu.edu),  Benjamin Owens (bsowens@bu.edu)
# Date: 3/30/16
# Boston University Computer Science Spring 2016
# CS330 Assignment 5 Question 4 (b)
# Description: Solves the number partition problem with the Karmarkar-Karp Algorithm
# Resources: https://en.wikipedia.org/wiki/Partition_problem
# https://docs.python.org/3.0/library/heapq.html
# Adapted for HW7 Question 4 - Nicholas Louie, Satoe Sakuma, Pauline Ramirez
# 4/26/16

import heapq

# INPUT
test_list = [10, 8, 7, 6, 5]

# partition takes a list of integers and performs KK number partitioning algorithm


def karmarkar_karp(l):
    n = len(l)
    K = sum(l)

    # init heap, but since heappop only pops the min value, we will multiply each input value by -1
    heap = []
    for item in l:
        heapq.heappush(heap, item * -1)
    heapq.heapify(heap)

    while len(heap) > 1:
        i = heapq.heappop(heap)
        j = heapq.heappop(heap)
        heapq.heappush(heap, abs(i - j) * -1)

    # the result should be the residue. Switch negative sign back.
    r = heapq.heappop(heap) * -1

    return abs(r)

# eof
```

### Repeated Random

```python
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
        if r < smallest_residue:
            smallest_residue = r
    return smallest_residue

# eof

```

### Gradient Descent
```python
# File: gradient_descent.py
# Course: Boston University CS330 - Algorithms Spring 2016 Assignment 7 Question 4
# Authors: Nicholas Louie (nlouie@bu.edu), Satoe Sakuma (ssakuma@bu.edu), Pauline Ramirez (pgr@bu.edu)
# Created: 4/26/16
# Due: 4/28/16 7pm
# Description: Generates an initial random solution S. For each k iterations, considers a random move
# to a neighbor S' of the current solution S. If the residue r(S') is less than r(S), sets S to S'
# returns the final and best S.
# The random move defined for gradient descent is as follows: choose random i and j from [1,n] s.t. i != j
# Set S_i to -S_i and with probability 1/2 set S_j to -S_j

import random


def gradient_descent(A, k):
    import controller
    # Get a random solution
    S = controller.generate_random_solution(len(A))
    # Get the residue of the solution
    smallest_residue = controller.residue(A, S)
    for x in range(k):
        sTemp = S
        # Choose an i and j
        i = random.randint(0, len(S) - 1)
        j = random.randint(0, len(S) - 1)
        # Make sure they're not the same
        while i == j:
            j = random.randint(0, len(S) - 1)
        sTemp[i] *= -1
        # Probability of 1/2 to set A[j] to -A[j]
        rand = random.random()
        if rand > 0.5:
            sTemp[j] *= -1
        r1 = controller.residue(A, S)
        r2 = controller.residue(A, sTemp)
        # Compare the residues
        if r2 < r1:
            # set new state
            S = sTemp
        # keep track of smallest
        if r2 < smallest_residue:
            smallest_residue = r2
    return S, smallest_residue
        

# eof

```

### Simulated Annealing

```python
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
    residue_1 = controller.residue(A, S)
    # keep track of smallest_residue
    smallest_residue = residue_1

    for x in range(k):
        sTemp = S
        i = random.randint(0, len(S)-1)
        j = random.randint(0, len(S)-1)

        # make sure i and j are different
        while i == j:
            j = random.randint(0, len(S)-1)
            if i != j:
                break

        sTemp[i] *= -1

        # change with probability half
        rand = random.uniform(0, 1)
        if rand > 0.5:
            sTemp[j] *= -1

        residue_2 = controller.residue(A, sTemp)

        # compare the two residues
        if residue_2 > residue_1:
            # take the worse residue by e() probability but smallest_residue still keeps track of smallest
            rand1 = random.uniform(0, 1)
            if rand1 < e_prob(x, residue_1, residue_2):
                # accept new state
                S = sTemp
        # new residue is smaller than old
        else:
            S = sTemp

        if residue_2 < smallest_residue:
            smallest_residue = residue_2
        
    return S, smallest_residue

# calculate eprob


def e_prob(i, residue_1, residue_2):
    temp = (10**10)*(.8**math.floor(i/300))
    temp_prob = math.exp((-1 * (residue_2 - residue_1)/temp))
    return temp_prob

# eof

```