#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me prints You got me!
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "catch_me=You got me\!&user_id=98" -H "Origin: HolbertonSchool"
