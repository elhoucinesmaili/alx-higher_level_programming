#!/bin/bash
# Bash script that makes reuest that causes the server to respond with message
curl -s -L -X PUT -H "Origin: AlxSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
