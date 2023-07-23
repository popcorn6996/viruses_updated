@echo off

set /a counter=1

:loop

    echo This loop will run 10 times.
    ::Let's make a while loop
    

    set /a counter+=1
    @echo off
    start explorer.exe "C:\Users\USER\Desktop\images"

    if %counter% LSS 11 goto loop