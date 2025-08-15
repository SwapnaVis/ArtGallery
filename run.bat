@echo off
echo Starting MySQL Service...
net start MySQL80

echo Running ArtGallery Backend...
python backend\main.py
pause