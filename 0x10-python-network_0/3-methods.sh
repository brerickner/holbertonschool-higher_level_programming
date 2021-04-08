#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods acceptable.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
