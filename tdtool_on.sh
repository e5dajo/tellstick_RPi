#! /bin/bash 
echo "sleep $3;tdtool --on $2" | at $1
