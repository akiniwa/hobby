@Echo OFF

:: By Elektro H@cker

FOR /F "Tokens=2 delims==" %%# in ('WMIC OS GET Installdate /format:list') DO (
    Call Set "full_date=%%#"
    Call Set "date=%%full_date:~0,4%%/%%full_date:~4,2%%/%%full_date:~6,2%%"
    Call Set "custom_date=%%full_date:~4,2%%/%%full_date:~6,2%%/%%full_date:~0,4%%"
)

Echo %full_date%
Echo %date%
echo %custom_date%

Pause&Exit