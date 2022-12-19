# Code Challenges
A new collection of my personal solutions to various code challenges.
### Setup
This repo implements solutions in Python 3.10+.  It's recommended to run and install dependencies from a virtual environment.

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
- - Challenge: [Switch the Bulb--Play game Series #10](https://www.codewars.com/kata/5a96064cfd57777828000187/train/python)
  - Location: [./src/code_wars/switch_the_bulbs.py](./src/code_wars/switch_the_bulbs.py)
  - Strategy: Create a graph and use a depth first search to find a possible route.
  - Resources:
  - - [Depth-first_search](https://en.wikipedia.org/wiki/Depth-first_search)
    - [Dijkstra's_algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
    - [Travelling_salesman_problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)




### Notes
- The [union](https://docs.python.org/3/whatsnew/3.10.html) `|` operator to merge dictionaries returning a new was introduced in Python 3.10
- The [walrus](https://docs.python.org/3/whatsnew/3.8.html) `:=` operator was introduced in Python 3.8.
