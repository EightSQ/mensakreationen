#!/bin/bash

docker run --rm -d -e PORT=8081 -p 8081:8081 --name "mensakreationen" mensakreationen:latest
