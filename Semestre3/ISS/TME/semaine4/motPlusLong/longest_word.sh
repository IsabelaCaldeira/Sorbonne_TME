while read line ; do   
    list ="$list $(./longest_param.sh $line)"
done < $1

./longest_param.sh $list