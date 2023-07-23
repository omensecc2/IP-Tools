@ECHO OFF
Title [+] Red Pinger [+]
mode con cols=56 lines=17
set /p IP=Enter IP Address:
cls
title [+] Pinging:%IP% [+]                                                       
:Reply                                                                            
PING -n 1 %IP% | FIND "TTL="
IF ERRORLEVEL 1 (SET in=c & ECHO Request Timed Out...)
ping -t 2 0 10 127.0.0.1 >nul
goto Reply