#!/bin/sh
curl $1 2>/dev/null| grep -e 'body' | cut -d\" -f2