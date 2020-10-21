@echo off
	set /p PATH=Pleas put the path:
	cd %PATH%
	set s=-
	call :fun s
	exit /b
	
	:fun
		for /d %%a in ("*") do (
			set s=%s%--
			echo %s% %%a
			cd %%a
			call :fun s
			cd ..
		)
		
exit /b

:: cd.. Change to the parent director