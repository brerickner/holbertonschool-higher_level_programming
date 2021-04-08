#!/bin/bash
# Bash script that takes in a URL as an argument and displays the body
curl "$1" -sX GET -d "X-HolbertonSchool-User-Id=98"
