#!/bin/bash

echo "🚀 Launching GAMA simulation..."

docker-compose -f docker/docker-compose.yml run gama \
  bash -c "echo 'Run GAMA model here' && ls models/"