#!/bin/bash

[ $# -eq 0 ] && echo il manque un parametre && exit 1
n=$1

if [ $n -gt 0 ]; then
    n=$((n - 1))
    echo "Ola : 0"
    ./ola.sh $n
fi
