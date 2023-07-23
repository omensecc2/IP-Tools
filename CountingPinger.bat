@ECHO OFF
chcp 65001 >nul
Title [+] Counting Pinger [+]
mode con cols=39 lines=10
ECHO                    ,
ECHO                 \  :  /
ECHO              `. __/ \__ .'
ECHO              _ _\     /_ _
ECHO                 /_   _\
ECHO               .'  \ /  `.
ECHO                 /  :  \
ECHO                    '
ECHO.
set /p IP=Enter IP Address:
Title [+] Pinging:%IP% [+]
mode con cols=39 lines=9
set /a Failure=0
set /a Success=0
set /a Status=N/A
:Reply
PING -n 1 %IP% | FIND "TTL="
cls
ECHO.
ECHO  Pinging: %IP%
ECHO.
ECHO  Status: %IP%
ECHO.
ECHO  Successful Replies: %Success%
ECHO.
ECHO  Failed Replies: %Failure%
ECHO.
IF ERRORLEVEL 1 (SET in=c & set /a Failure=%Failure% +1) else set /a Success=%Success% +1
timeout /t 1 >nul
goto Reply