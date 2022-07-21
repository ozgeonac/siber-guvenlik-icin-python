#!/bin/sh
case "$1" in
  start)
    echo "Servis basladi"
    python /home/a/PycharmProjects/calismalar/icerikKontrol.py &
    ;;
  stop)
    echo "Servis durduruluyor"
    PID=`ps x |grep 'python /home/a/PycharmProjects/calismalar/icerikKontrol.py' | head -1 | awk '{print $1}'`
    echo "Durdurulan Uygulama PID: " $PID
    kill -9 $PID
    ;;
  status)
    echo "Status:"
    PID=`ps x |grep 'python /home/a/PycharmProjects/calismalar/icerikKontrol.py' | head -1 | awk '{print $1}'`
    echo $PID "nolu uygulamada calisiyor"
    ;;
  *)
    echo "Usage: /etc/init.d/icerikKontrol {start|stop}"
    exit 1
;;
esac

exit 0
