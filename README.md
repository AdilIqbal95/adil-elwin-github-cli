# Github repo CLI interface

## User Instructions

_Note: make sure you have [pipenv installed](https://github.com/getfutureproof/fp_guides_wiki/wiki/Virtual-Environment) before continuing._

- Fork/clone this repository
- `pipenv shell` to activate your virtual environment for the project
- `pipenv install` to install dependencies
- `pipenv run start` or `python index.py` to run program

## Task list

- [ ] Create a CLI with an Object Oriented design
  - [ ] On starting the app, User is asked for their GitHub username
  - [ ] A request is made to `https://api.github.com/users/<username>/repos`
  - [ ] API data is turned into instances of Repository class
  - [ ] User is shown a numbered list their repos by name
  - [ ] User can input a number to see more details on the corresponding repository


### Study Notes

This app was created with the help of the study note below:
[OO Python](https://github.com/getfutureproof/fp_guides_wiki/wiki/OO-Python)