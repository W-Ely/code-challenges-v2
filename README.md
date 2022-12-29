# Code Challenges
A new collection of my personal solutions to various code challenges.
### Setup
This repo implements solutions in Python 3.8+.  It's recommended to run and install dependencies from a virtual environment.

After cloning this repo:
```sh
python -m venv .venv
```
or if Python 3 is not your default.
```sh
python3 -m venv .venv
```

Then activate the virtual environment.
```sh
. ./.venv/bin/activate
```
Next install the dependencies:
```sh
pip install -r requirements.txt
```
### Testing
Tests are setup to run with Pythons builtin unittest library.
```sh
python -m unittest
```

### Linting
- Autoformating is handled with [black](https://pypi.org/project/black/)
```sh
black src tests
```
- Linting by [pylint](https://pypi.org/project/pylint/)
```sh
pylint src tests
```
- Import arrangment by [isort](https://pypi.org/project/isort/)
```sh
isort src tests
```

### Challenges
#### Code Wars
- - Challenge: [Next bigger number with the same digits](https://www.codewars.com/kata/55983863da40caa2c900004e/train/python)
  - Location: [./src/code_wars/next_bigger_number.py](./src/code_wars/next_bigger_number.py)
  - Strategy:
    1. Moving from right to left find first number with a larger number to the right.
    1. Next find the smallest number to the right of this number that is also large than this number.
    1. Then switch these two numbers.
    1. Sort all the numbers to the right of the left number.
- - Challenge: [Stargate SG-1: Cute and Fuzzy](https://www.codewars.com/kata/59669eba1b229e32a300001a/train/python)
  - Location: [./src/code_wars/sg1.py](./src/code_wars/sg1.py)
  - Strategy: Create a graph and use a breadth first search to find a possible route.
  - Resources:
  - - [Breadth-first_search](https://en.wikipedia.org/wiki/Breadth-first_search)
    - [Dijkstra's_algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
#### Codecademy
- - Challenge: [The Knapsack Problem](https://www.codecademy.com/code-challenges/code-challenge-knapsack-problem-python)
  - Location: [./src/codecademy/the_knapsack_problem.py](./src/codecademy/the_knapsack_problem.py)
  - Resources:
  - - [Wikipedia - Dynamic Programming](https://en.wikipedia.org//wiki/Dynamic_programming)
    - [Wikipedia - Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem)
    - [Geeks for Geeks - Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/)
    - [Grokking Algorithms: An Illustrated Guide for Programmers and Other Curious People, Chapter 9](https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230)