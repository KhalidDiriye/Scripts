@echo off
color C
echo !!!!!THIS WILL DO THE FOLLOWING!!!!! 
echo Disable Diagnostics Service, DWM Push Service, Background Intelligent Transfer Service, Superfetch, Windows Search
pause
cls
color 9
sc config DiagTrack start= disabled
sc config dmwappushservice start= disabled
sc config BITS start= disabled
sc config SysMain start= disabled
sc config WSearch start= disabled
color A
echo Done! Press any key to exit
pause >nul