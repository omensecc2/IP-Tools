@ECHO OFF
Title [+] Timed Pinger [+]
set /p IP=Enter IP Address:
set /p time=Set Timelimit:
set time=%time%
set %time%=%time1%                                                       
:Reply                                                                            
title [+] PINGING %IP% [+] Remaining Time:%time%
PING -n 1 %IP% | FIND "TTL="
IF ERRORLEVEL 1 (SET in=c & ECHO Request Timed Out...)
ping -t 2 0 10 127.0.0.1 >nul
set /a time=%time% -1
if %time%==0 Goto timeend
Goto Reply
:timeend
ECHO Pinging Has Stopped...
timeout /t 2 >nul
ECHO Closing Application
timeout /t 3 >nul
exit