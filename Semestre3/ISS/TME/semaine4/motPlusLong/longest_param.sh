 #! /bin/bash

 max_size=0

 for param in "$@" ; do
    if [ ${#param} -gt $max_size ] ; then
        max_size=${#param}
        longest_param="$param"
    fi
 done

 if [ $max_size -gt 0 ] ; then
    echo $longest_param
 fi