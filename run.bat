@echo off
title UAS KRIPTOGRAFI - KEL2
call .env\Scripts\activate
echo ===============================
echo    Aplikasi Enkripsi ROT13 dan Steganografi LSB
echo ===============================

pip install FreeSimpleGUI
pip install Pillow

python main.py
pause