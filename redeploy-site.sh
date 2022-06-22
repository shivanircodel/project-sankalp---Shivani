#!/bin/bash

tmux kill-server

cd project-sankalp

git fetch
git reset origin/main --hard

python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux
tmux detach
flask run --host=0.0.0.0
