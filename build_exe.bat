@echo off
REM Script pour créer un exécutable Windows du GUI

echo.
echo ========================================
echo   CREATION EXECUTABLE WINDOWS
echo ========================================
echo.

REM Nettoyage des anciens builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /q *.spec

echo [1/3] Nettoyage effectue...
echo.

REM Création de l'exécutable avec PyInstaller
echo [2/3] Creation de l'executable (cela peut prendre 1-2 minutes)...
echo.

python -m PyInstaller ^
    --onefile ^
    --windowed ^
    --name "APE_Bons_Commande" ^
    --icon=NONE ^
    --add-data "generer_bons_commande.py;." ^
    --hidden-import tkinter ^
    --hidden-import tkinter.filedialog ^
    --hidden-import tkinter.messagebox ^
    generer_gui.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERREUR] La creation a echoue !
    echo Verifiez que PyInstaller est installe : pip install pyinstaller
    pause
    exit /b 1
)

echo.
echo [3/3] Nettoyage des fichiers temporaires...
rmdir /s /q build
del /q *.spec

echo.
echo ========================================
echo   SUCCES !
echo ========================================
echo.
echo L'executable a ete cree :
echo   dist\APE_Bons_Commande.exe
echo.
echo Vous pouvez le copier sur n'importe quel PC Windows
echo et le lancer sans avoir Python installe.
echo.
pause
