#!/bin/sh
echo 22 >> /sys/class/gpio/export ; echo out >> /sys/class/gpio/gpio22/direction
echo '22 done'

echo 27 >> /sys/class/gpio/export ; echo out >> /sys/class/gpio/gpio27/direction
echo '27 done'
echo 24 >> /sys/class/gpio/export ; echo out >> /sys/class/gpio/gpio24/direction
echo '24 done'
echo 23 >> /sys/class/gpio/export ; echo out >> /sys/class/gpio/gpio23/direction
echo '23 done'
