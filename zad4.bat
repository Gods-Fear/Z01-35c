@echo off
 
    if %1 leq 0 (
      echo The number must be greater than 'null'.
      goto:eof
    )
	
    set /a a=0
    set /a b=1
    set /a c=0
    set /a i=0
	
   
    :loop
      if %i% == %1 goto:result
      set /a c=%a% + %b%
      set /a a=%b%
      set /a b=%c%
	  echo %b%
      set /a i+=1
      goto:loop
	:result 
		echo Result: %b%
		

::pause



:: leq = Less Than or Equal To
::goto = go to ..