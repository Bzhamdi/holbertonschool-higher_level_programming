#!/bin/bash
#start with curl -x put 0.0.0.0:5000/catch_me
curl -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -s
