#!/bin/bash
# Bash script that takes in a URL as an argument and displays the body
curl -sX "$1" GET -H "X-HolbertonSchool-User-Id: 98"
