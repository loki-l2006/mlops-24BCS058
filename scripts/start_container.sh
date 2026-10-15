#!/bin/bash
set -e

cd /home/ubuntu/mlops-24BCS058/mlops-student

docker build -t student-app .
docker run -d --restart unless-stopped 
  -p 8080:5000 
  --name student-container 
  student-app
