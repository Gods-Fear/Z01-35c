@echo off

call:factorial "%~1"
echo result: %ErrorLevel%
exit /b 0

:factorial
    if "%~1" LEQ "2" (
        set ErrorLevel=%~1
        exit /b 0
    )
    set /a next=%~1 - 1
    call:factorial %next%
    set /a ErrorLevel=%~1 * %ErrorLevel%
exit /b 0