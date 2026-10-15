#!/bin/bash
set -e

if docker ps -a --format '{{.Names}}' | grep -q '^student-container$'; then
    docker rm -f student-container
fi
