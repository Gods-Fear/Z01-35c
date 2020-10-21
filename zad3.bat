@echo off

echo Detecting permissions...

net session >nul 2>&1

if %ERRORLEVEL% == 0 (
    echo Hello Admin.
) else (
    echo Sorry, you are only user.
)

::pause
