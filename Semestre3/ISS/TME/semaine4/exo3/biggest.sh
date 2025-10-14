#Validation argument et repo
[ $# -eq 0 ] && echo "Il faut un répertoire" && exit 1
[ ! -d "$1" ] && echo "T'es sûr que t'as bien écrit?" && exit 1

#Trouve le plus gros fichier
max=0
biggest=""
for fichier in "$1"/*; do 
    taille=$(wc -c < "$fichier")
    if [ "$taille" -gt "$max" ]; then
        max=$taille
        biggest=$fichier
    fi
done
echo "$biggest"