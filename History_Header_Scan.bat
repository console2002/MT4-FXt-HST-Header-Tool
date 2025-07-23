@echo off
cd /d "%~dp0"

echo Scanning .hst and .fxt files for header information...
python History_Header_Scan.py

pause
