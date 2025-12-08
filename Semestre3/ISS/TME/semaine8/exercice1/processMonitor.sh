PID_Child=$1
echo  $PID_Child

for i in {1..60}; do
    ps -p o "$PID_Child" o pid,ppid,state
done
