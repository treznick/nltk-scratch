brew install python3
pip install virtualenvwrapper
mkvirtualenv -a . -r requirements.txt -p $(which python3) $(cat .venv)
