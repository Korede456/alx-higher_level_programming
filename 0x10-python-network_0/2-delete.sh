#!/bin/bash
# A script that senda a delete request to the url passed as the first
# argument and displays the body of the response

curl -sX DELETE "$1"
