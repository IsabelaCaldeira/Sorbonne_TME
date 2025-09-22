echo Mon PID est $$

#On appele la fonction fils pour regarder l'evolution de comment ça marche le vincule des pid et ppid
for i in {1..10} ; do
    ./fils.sh
done