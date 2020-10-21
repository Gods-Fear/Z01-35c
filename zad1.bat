@echo off

set /p extension=Please put file extension 
set /p PATH=Please put a path 

if exist "%PATH%\*.%extension%" (
		for %%a in (%PATH%\*.%extension%) do echo %%a
) else (
    echo file does not exist - do something else
)



::pause C:\Users\1\Desktop\PWR\2semestr\AISD\wyklad 
:: C:\Users\1\Desktop\PWR\5semestr\Web\Lab_1 
::C:\Users\1\Desktop\PWR\5semestr\JSkryp