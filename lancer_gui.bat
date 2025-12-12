@echo off
REM Lanceur GUI pour le Générateur de Bons de Commande APE
REM Double-cliquez sur ce fichier pour ouvrir l'interface graphique

echo.
echo ========================================
echo  Generateur de Bons de Commande - GUI
echo  APE Villebarou
echo ========================================
echo.
echo Demarrage de l'interface graphique...
echo.

python generer_gui.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Erreur lors du lancement !
    echo.
    echo Verifiez que Python est installe correctement.
    echo.
    pause
)
