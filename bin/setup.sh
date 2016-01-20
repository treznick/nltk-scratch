brew install python3 --with-brewed-tk
pip install virtualenvwrapper
mkvirtualenv -a .. -r requirements.txt -p $(which python3) $(cat .venv)
