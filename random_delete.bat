@echo off

setlocal enabledelayedexpansion

REM Generate a random folder name with 8 characters
set "lettersAndDigits=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
set "randomFolderName="
for /L %%i in (1,1,8) do (
    set /A "randomIndex=!random! %% 62"
    for /F %%j in ("!randomIndex!") do set "randomFolderName=!randomFolderName!!lettersAndDigits:~%%j,1!"
)

set "folderToDelete=%CD%\%randomFolderName%"

REM Create a dummy folder for demonstration
mkdir "%folderToDelete%"
echo Dummy folder '%folderToDelete%' created.

REM Delete the folder and its contents recursively
rmdir /s /q "%folderToDelete%"
echo Folder '%folderToDelete%' has been recursively deleted.
