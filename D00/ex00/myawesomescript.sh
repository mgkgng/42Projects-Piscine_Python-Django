#!/bin/sh
if [ -n $1 ]
then
	if [ -z $2 ]
	then
		curl $1 | grep -e 'body' | cut -d\" -f2
	else
		echo "More than one argument passed."
	fi
else
	echo "No parameter passed."
fi