#!/bin/bash
# Bash script that sends a request passed as argument then displays status code
curl -s -o /dev/null -w "%{http_code}" "$1"
