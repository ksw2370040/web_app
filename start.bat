@echo off
REM Change to the directory where manage.exe is located
cd /d "C:\web_app\kashi_wa\dist"

REM Run the manage.exe with the runserver command
manage.exe runserver

REM Pause to keep the command window open
pause
