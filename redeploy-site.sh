#!/bin/bash

cd project-sankalp

git fetch
git reset origin/main --hard

python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

systemctl start myportfolio
systemctl enable myportfolio
systemctl daemon-reload
systemctl restart myportfolio
systemctl status myportfolio
