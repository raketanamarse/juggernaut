sudo killall -9 mjpg_streamer 
screen -Sdm webca /usr/local/bin/mjpg_streamer -i "input_uvc.so -f 15 -r 640x480"  -o "output_http.so -w /usr/local/share/mjpg-streamer/www"
