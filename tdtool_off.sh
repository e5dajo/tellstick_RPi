#! /bin/bash 
echo "sleep $3;tdtool --off $2" | at $1
