#Il faut toujours fairer gaffe avec les espaces dans les []
if [ $# -eq 0 ]; then
    echo Il manque un paramètre
    echo "Usage : ./pere.sh <nb_file>"
    exit 1
fi

echo Je suis $$
for i in $(seq 1 "$1"); do
    fils.sh
done