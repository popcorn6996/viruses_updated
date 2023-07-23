@echo off

REM Check if the script is running with administrative privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires administrative privileges.
    echo Please run the script as an administrator.
    pause
    exit /b 1
)

set /p username=Enter the username whose password you want to change: 
net user %username% *

REM Check if the password change was successful
if %errorLevel% equ 0 (
    echo Password changed successfully for user %username%.
) else (
    echo Failed to change the password for user %username%.
)

pause
