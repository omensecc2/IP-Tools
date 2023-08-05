@ECHO off
Title [+] RGB Pinger [+]
mode con cols=56 lines=17
set /a num= (%Random%%%9)+1
color %num%
set /p IP=Enter IP Address:
cls
color %in%
Title [+] Pinging: %IP% [+]                                                       
:Reply                                                                            
set /a num= (%Random%%%9)+1
color %num%
PING -n 1 %IP% | FIND "TTL="
IF ERRORLEVEL 1 (SET in=c & ECHO Request Timed Out...)
goto Reply
