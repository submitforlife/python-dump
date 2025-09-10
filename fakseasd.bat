@echo off
:loop
set /a bpm=%RANDOM% %% 190 + 200
echo %bpm% > heart_rate.txt
timeout /t 1 >nul
goto loop