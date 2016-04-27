#  Boston Univerisity CS330 - Algorithms Spring 2016 [Assignment 7](https://www.evernote.com/shard/s184/sh/e477ea53-445f-45fb-a48a-142369fbe4cb/a6cb8dd3cd6ea97080efd1811485c1cf) Question 4
### Nicholas Louie (nlouie@bu.edu), Satoe Sakuma (ssakuma@bu.edu), Pauline Ramirez (pgr@bu.edu) 
### 4/26/16

#### Running the package
------------------------------
`python3 controller.py`

#### Dependencies
------------------------------
Python 3.4

#### Package Contents
------------------------------
- controller.py
- gradient_descent.py
- Karmarkar_Karp.py
- repeated_random.py
- simulated_annealing.py

#### Functionality
------------------------------
`controller.py` runs various heuristics for the *NUMBER PARTITION* problem. 
The controller runs `m = 50` random instances of `n = 100` integers using `k = 25000` iterations

#### Results
------------------------------
#####Average Exec Times
- Karmarkar Karp Avg Exec Time: `0.000459990501404`
- Repeated Random Avg Exec Time: `5.07450001717`
- Gradient Descent Avg Exec Time: `1.9392400074`
- Simulated Annealing Avg Exec Time: `1.06476000786`
#####Average Residues
-Karmarkar Karp Avg Residue: `230107`
-Repeated Random Avg Residue: `235445680`
-Gradient Descent Avg Residue: `233291618`
-Simulated Annealing Residue: `350839537`

######Total Execution Time: 403.976000071
