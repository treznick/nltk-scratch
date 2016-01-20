# NLTK Scratch notes

## Setup

  1. clone the repo: `git clone git@github.com:treznick/nltk-scratch.git`
  2. set up an upstream remote: `git remote add upstream git@github.com:treznick/nltk-scratch.git`
    - Periodically sync with upstream. Rebase and PR changes as necessary
  3. run the setup script: `./setup.sh`
  4. activate the virtualenv: `workon $(cat .venv)`
  5. run jupyter: `jupyter notebook`

## How to use virtualenvwrapper

`workon cc-nltk` or whatever you've named your virtualenv in your `.venv` file

This will:
  1. cd into your project directory
  2. activate your virtualenv
  3. install all of your requirements if they're not already there

When you're done working on that project, run `deactivate`

## how to run jupyter

`jupyter notebook`

## Gotchas

  * Sometimes it's hard to compile some dependencies (specifically Tk), when installing matplotlib
    * I used `brew tap homebrew/dupes/tcl-tk; brew install tcl-tk`
    * also reinstalling python3 with `--with-brewed-tk` may have done it. The `setup.sh` script runs that now
  * When in a jupyter notebook, make sure you call `% matplotlib inline` before `import matplotlib` so that plots show up inline in the notebook.
