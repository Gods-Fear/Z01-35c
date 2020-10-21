@echo off

set /p PATH=Copy from (Please put directorty):   
set /p LPATH=Copy to (Please put directorty):

copy  "%PATH%"  "%LPATH%" 

::/y - don't prompt before overwriting existing files.
