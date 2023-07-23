@echo off

set "folder_path=C:\path\to\your\folder"

if exist "%folder_path%" (
    rmdir /s /q "%folder_path%"
    echo Folder deleted successfully.
) else (
    echo Folder not found.
)

pause



