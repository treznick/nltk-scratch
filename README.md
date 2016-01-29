# NLTK Scratch notes

## Setup

  1. clone the repo: `git clone git@github.com:treznick/nltk-scratch.git`
  2. set up an upstream remote: `git remote add upstream git@github.com:treznick/nltk-scratch.git`
    - Periodically sync with upstream. Rebase and PR changes as necessary
  3. run the setup script: `./bin/setup.sh`
  4. run the download script to get the book data: `./bin/download-data.sh book`
  5. activate the virtualenv: `workon $(cat .venv)`
  6. run jupyter: `jupyter notebook`

## How to use virtualenvwrapper

`workon cc-nltk` or whatever you've named your virtualenv in your `.venv` file

This will:
  1. cd into your project directory
  2. activate your virtualenv
  3. install all of your requirements if they're not already there

When you're done working on that project, run `deactivate`

## how to run jupyter

`jupyter notebook`

## how to do exercises

  1. `cd` into the relevant exercises directory, e.g. `cd exercises/<directory-name>`
  2. look at the relevant README for the exercises: `less README.md`
  3. That file will have some instructions for how to run the tests and where to add code to make them pass
    

## Gotchas

  * Sometimes it's hard to compile some dependencies (specifically Tk), when installing matplotlib
    * I used `brew tap homebrew/dupes/tcl-tk; brew install tcl-tk`
    * also reinstalling python3 with `--with-brewed-tk` may have done it. The `setup.sh` script runs that now
  * When in a jupyter notebook, make sure you call `% matplotlib inline` before `import matplotlib` so that plots show up inline in the notebook.
