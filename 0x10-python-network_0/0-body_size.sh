#!/bin/bash
#result Content-Length: 10 so 
#awk -F : field separator. OR  cut -d
curl -sI "$1" | grep 'Content-Length:' | awk -F " " '{print $2}'
