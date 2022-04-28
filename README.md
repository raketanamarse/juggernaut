# juggernaut
remote monitoring system

Джаггернаут это система удаленного визуального мониторинга объекта (подвижная платформа с вебкамерой и вебинтерфейсом управленя)

Прототип собирался на raspberry pi 4 
для работы нудно установить mjpg-streamer (https://github.com/jacksonliam/mjpg-streamer) и поместить в каталог с проектом

в ~\jopa\templates\index.html заменить ip адреса трансляции на локальный адрес внутри сети (внутри VPN) {так же нужно задать белые ip, если робот будет находиться не в одной сети вместе с оператором}

   <!--<h1>THIS IS VIDEO</h1>-->   
   <img src="http://10.0.2.3:8080/?action=stream" />  
   <img src="http://raspberrypi:8080/?action=stream" />
   <img src-"http://10.0.2.3:8080/?action=stream" /> 

после вернуться в ~\jopa
и запустить веб-сервер: python main.py
зайти на ip адрес rpi4 ip:8000
