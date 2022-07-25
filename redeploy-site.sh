#!/bin/bash

chmod +x redeploy-site.sh

cd project-sankalp---Shivani

git fetch
git reset origin/main --hard

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

docker-compose ps
