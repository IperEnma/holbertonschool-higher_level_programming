#!/bin/bash
# get only if status code is  0

http_code=$(curl -s -w \%{http_code} -o /dev/null $1)

if [[ $http_code -eq 200 ]]
then
	curl -s $1
fi
