trap "echo il ne doit en rester qu'un" SIGINT

while True; do
    echo still here
done

#Pour le tuer on va envoyer un signaux sigkill (-9) par le terminal avec son PID