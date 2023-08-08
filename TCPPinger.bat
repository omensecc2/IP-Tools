@ECHO OFF
Title [+] TCP Pinger [+]
mode con cols=70 lines=32
set /p IP=Enter IP Address:
set /p PORT=Enter Port:
Title [+] Pinging:%IP%:%PORT% [+]
cls
mode con cols=70 lines=32
PAPING  %IP% -p %PORT%