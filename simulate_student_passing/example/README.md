# Example Simulation Tutorial

## Purpose
To test the durability of test cases as a way of combatting possible "cheap" solutions to STAT 430 questions.

## How to Use Files

(001) To run your own simulations, create the following files in any directory:
- NOT PROVIDED IN REPO
  - `dummy_solution.py` : possible student solution for a given question
  - `largest_odd.py` : approved solution for a given question
- PROVIDED IN REPO
  - `master_test.py` : file for storing all test cases
  - `master_report.py` : file for testing cases, simulating student submissions, and generating distribution of student scores

(002a) After creating these files, ensure they are in the same directory. The main file to run is `master_report.py`. This file will call `master_test.py` using the `subprocess` module.

(002b) `master_report.py` accepts two parameters:
- `num_students` : the number of students attempting this problem with the provided `dummy_solution`
- `num_attempts` : the number of times a student will submit their `dummy_solution` for the given problem

(003) At the end of the simulations but still while the script is executing, the user will be prompted twice more:
- `Entering Test Weights`: for each test case, enter the number of points the test case rewards for being solved
- `Selecting Test Distribution` : select the test case whose score distribution you would like to see (unfortunately, only one can be accessed per execution)

## Desired Output

![Screen Shot 2021-08-27 at 16 35 35](https://user-images.githubusercontent.com/78045025/131191021-b99b30a8-0a59-4cb2-ad4d-c8b1f6f510f5.png)
