#!/bin/bash
# search content length

curl -sI $1 | grep -i "Content-Length"  | cut -d ' ' -f2
