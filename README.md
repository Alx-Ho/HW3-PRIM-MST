# HW 3: Prim's algorithm

Notes: I used code LLMs to nicely comment and format my code.

In this assignment, you'll implement Prim's algorithm, a non-trivial greedy algorithm used to construct minimum spanning trees. 

## Tasks

### Coding

* [DONE] `construct_mst` implemented with Prim’s algorithm using a min-heap and outputs the MST adjacency matrix in `self.mst`.

### Development

* [DONE] `check_mst` now asserts shape, symmetry, edge subset, edge count (n−1), connectivity, and total weight.
* [DONE] Added a third unit test on a 4‑node cycle with tied weights to validate correctness under multiple valid MSTs.
* [Optional] Make your package `pip` installable. (Refer to prevous assignments for more in-depth information.)
* [Optional] Automate testing with `pytest` and GitHub Actions, and add a status badge to this README file. (Refer to previous assignments for more in-depth information.)

## Getting started

Fork this repository to your own GitHub account. Work on the codebase locally and commit changes to your forked repository. 

You will need following packages:

- [numpy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/)
- [pytest](https://docs.pytest.org/en/7.2.x/)

We also strongly recommend you use the built-in [heapq](https://docs.python.org/3/library/heapq.html) module.

## Completing the assignment

Push your code to GitHub with passing unit tests, and submit a link to your repository through this [google form link]([https://forms.gle/guyuWE6hsTiz34WTA](https://docs.google.com/forms/d/e/1FAIpQLSdA3xmIjLZ5_eq9SvC3DHczAdYr6tuRGCHwmFTslspwzboI8A/viewform))

## Grading

### Code (6 points)

* Minimum spanning tree construction works correctly (6)
    * Correct implementation of Prim's algorithm (4)
    * Produces expected output on small graph (1) 
    * Produces expected output on single cell data (1) 

### Unit tests (3 points)

* Complete function "check_mst" (1)
* Write at least two unit tests for MST construction (2)

### Style (1 points)

* Readable code with clear comments and method descriptions (1)

### Extra credit (0.5)

* Github actions/workflow (0.5)
