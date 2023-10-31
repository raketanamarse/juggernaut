# juggernaut

Джаггернаут это система удаленного визуального мониторинга объекта (подвижная платформа с веб-камерой и веб-интерфейсом управленя)
видео демонстрация смотри видео vidoe1-vidoe3
![020220428_173745_DRO](https://user-images.githubusercontent.com/104571006/165778176-45fc84ee-3507-4098-84d8-3611110b6a02.jpg)

![изображение](https://user-images.githubusercontent.com/104571006/165775937-a71faccb-8828-4fd5-8aa3-fac9792ef6b5.png)

Прототип собирался на raspberry pi 4 
для работы нудно установить mjpg-streamer (https://github.com/jacksonliam/mjpg-streamer) и поместить в каталог с проектом


нужно дать права на исполнение, зайти в дирректорию cd juggernaut и дать права chmod +x *

---------------------------------------------
после нужно добавить в автозагрузку startgpio.sh командой: sudo mv autorun.service /lib/systemd/system/autorunJuggernaut.service

и выдаем права: sudo chmod 644 /lib/systemd/system/autorunJuggernaut.service

sudo systemctl daemon-reload

sudo systemctl enable autorunJuggernaut.service

---------------------------------------------
сделать автозапуск веб-сервера

crontab -e

добавить в конец файла строку:
@reboot python3 /home/pi/juggernaut/main/main.py

![изображение](https://user-images.githubusercontent.com/104571006/168795973-6473a2f9-bc89-47e9-9263-a185131c7d4b.png)


---------------------------------------------
в ~\main\templates\index.html заменить ip адреса (ы конце файла) трансляции на локальный адрес внутри сети (внутри VPN) {так же нужно задать белые ip, если робот будет находиться не в одной сети вместе с оператором}
    
   img src="http://10.0.2.3:8080/?action=stream" 
   img src="http://raspberrypi:8080/?action=stream" 
   
   ![изображение](https://user-images.githubusercontent.com/104571006/168796173-72521a09-4463-4031-af23-9e6f8dc8cfd1.png)

   
---------------------------------------------
после вернуться в ~\main
и запустить веб-сервер: python main.py
зайти на ip адрес rpi4 ip:8000
или sudo reboot если все правильно добавленно в автозагрузку




