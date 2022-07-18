#!/bin/bash

cd project-sankalp

git fetch
git reset origin/main --hard

python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
