# Crontab debugging 방법

<pre> */1 * * * * sh /home/pi/devel/BerePi/apps/tinyosGW/this_run_public_ip.sh > /home/pi/devel/BerePi/apps/tinyosGW/debug/debug.log 2>&1 </pre>

- 확인 방법 : tail -f -n20 /home/pi/devel/BererPi/apps/tinyosGW/debug/debug.log