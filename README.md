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
    1. From right to left find first number with larger number to the left.
    1. Find the smallest number to the right of this numebr that is large than this number.
    1. Switch the two numbers.
    1. Sort the numbers to the right of the first.
