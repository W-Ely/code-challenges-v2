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

https://www.codewars.com/kata/5a96064cfd57777828000187/train/python
