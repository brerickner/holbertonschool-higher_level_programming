#!/bin/bash
# Bash script to post and validate JSON from file
curl -sL "$1" -X POST -H "Content-Type: application/json" -d @"$2" 
