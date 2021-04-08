#!/bin/bash
# Bash script that takes in a URL as an argument and displays the body
curl -sX "$1" GET -d "X-HolbertonSchool-User-Id=98"
