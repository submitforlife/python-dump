@echo off
set outputFile="bpm_output.txt"
:loop
set /a bpm=%random% %% 150 + 212
echo %bpm% > %outputFile%
timeout /t 1 >nul
goto loop
