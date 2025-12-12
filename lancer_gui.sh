#!/bin/bash
# Lanceur GUI pour le Générateur de Bons de Commande APE
# Exécutez ce script pour ouvrir l'interface graphique

echo ""
echo "========================================"
echo " Générateur de Bons de Commande - GUI"
echo " APE Villebarou"
echo "========================================"
echo ""
echo "Démarrage de l'interface graphique..."
echo ""

python3 generer_gui.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Erreur lors du lancement !"
    echo ""
    echo "Vérifiez que Python 3 est installé correctement."
    echo ""
    read -p "Appuyez sur Entrée pour continuer..."
fi
