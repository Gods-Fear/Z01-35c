@echo off 

ffmpeg -i test.mp4 -r 0.0033 -vcodec png miniatura-%002d.png

pause 



:: -i nazwa_pliku - ścieżka pliku źródłowego wideo

::-r fps (ustawia liczbę klatek na sekundę przy zapisie; 
::fps jest wyrażane w hercach (1 / sekundę); używamy 1, abyśmy pobierali tylko jedną klatkę)

::-vf scale=-1:120 - rozmiar 

::ffmpeg -i test.mp4 -r 0.0033 -vf scale=-1:120 -vcodec png capture-%002d.png