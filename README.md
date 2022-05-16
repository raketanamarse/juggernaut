# juggernaut

Джаггернаут это система удаленного визуального мониторинга объекта (подвижная платформа с веб-камерой и веб-интерфейсом управленя)
видео демонстрация https://drive.google.com/drive/folders/1pVir6T9NVAQeprB8VJB5rh41zkXT1gg4

![020220428_173745_DRO](https://user-images.githubusercontent.com/104571006/165778176-45fc84ee-3507-4098-84d8-3611110b6a02.jpg)

![изображение](https://user-images.githubusercontent.com/104571006/165775937-a71faccb-8828-4fd5-8aa3-fac9792ef6b5.png)

Прототип собирался на raspberry pi 4 
для работы нудно установить mjpg-streamer (https://github.com/jacksonliam/mjpg-streamer) и поместить в каталог с проектом


нужно дать права на исполнение \n
cd juggernaut
chmod +x *

в ~\main\templates\index.html заменить ip адреса (ы конце файла) трансляции на локальный адрес внутри сети (внутри VPN) {так же нужно задать белые ip, если робот будет находиться не в одной сети вместе с оператором}
    
   img src="http://10.0.2.3:8080/?action=stream" 
   img src="http://raspberrypi:8080/?action=stream" 
   
после вернуться в ~\jopa
и запустить веб-сервер: python main.py
зайти на ip адрес rpi4 ip:8000





