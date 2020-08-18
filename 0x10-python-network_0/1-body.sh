#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
# -S option to disable the progression display
# -L option to follow all redirects
curl -s -L "$1"
