@echo off
setlocal enabledelayedexpansion

:: --- Usernames with simulated colors ---
set users[0]=[RED] bibida
set users[1]=[GREEN] ninje
set users[2]=[BLUE] zemil
set users[3]=[YELLOW] Thorncurry
set users[4]=[PURPLE] bandaso
set users[5]=[CYAN] jankso

:: --- Sample messages ---
set messages[0]=hi
set messages[1]=yoo dis shit awesoe asf
set messages[2]=yooo ngl dis stream fireeee
set messages[3]=omgggg
set messages[4]=LOLLOLOLOOLOLOOOL
set messages[5]=hehe
set messages[6]=ok lol
set messages[7]=streem go
set messages[8]=wtf did I miss btw
set messages[9]=I don understan

:: --- Clear previous chat ---
> chat.txt echo.

:loop
:: Pick random user
set /a useridx=%random% %%6
:: Pick random message
set /a msgidx=%random% %%10

:: Append message to temporary file
echo !users[%useridx%]!: !messages[%msgidx%]! >> temp_chat.txt

:: Keep only last 12 lines (simulate scrolling)
set count=0
for /f "delims=" %%a in (temp_chat.txt) do (
    set /a count+=1
    set "line[!count!]=%%a"
)
set /a start=count-11
if !start! lss 1 set start=1

> chat.txt (
    for /l %%i in (!start!,1,!count!) do echo !line[%%i]!
)

:: Random delay between 0.3–2.5 seconds
set /a delay=%random% %%2200 + 300
ping -n 1 -w !delay! 127.0.0.1 >nul

goto loop
