#!/bin/bash
# Bash script that makes reuest that causes the server to respond with message
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
