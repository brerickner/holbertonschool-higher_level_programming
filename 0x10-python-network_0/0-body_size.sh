#!/bin/bash
# Bash script that takes in a URL, sends request and displays size of body
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
