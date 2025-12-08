sleep 30 &
PID_Child=$!
echo  $PID_Child

#Compare PPID
ps -p o "$PID_Child" o pid,ppid,state
#Run at terminal ps -p (the pid that cames from echo $1) o pid,ppid,state