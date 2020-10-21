@echo off

set /p extension=Please put file extension 
set /p PATH=Please put a path 

if exist "%PATH%\*.%extension%" (
		for %%a in (%PATH%\*.%extension%) do echo %%a
) else (
    echo file does not exist - do something else
)



::pause 
