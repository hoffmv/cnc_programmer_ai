@echo off
echo Installing cnc_programmer_ai (alpha)...
powershell -command "Expand-Archive -Path cnc_programmer_ai-alpha-package.zip -DestinationPath $env:USERPROFILE\Desktop\cnc_programmer_ai-alpha"
echo Installed to Desktop\cnc_programmer_ai-alpha
pause