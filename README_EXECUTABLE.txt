====================================================
   APE BONS DE COMMANDE - VENTE DE VANILLE
====================================================

Version : 1.3.0
Date    : Décembre 2025

====================================================
   UTILISATION RAPIDE
====================================================

1. Double-cliquez sur "APE_Bons_Commande.exe"

2. Dans l'interface :
   - Cliquez sur "Parcourir" pour sélectionner votre fichier CSV
   - Cochez "Afficher les statistiques" si vous voulez le résumé
   - Cochez "Ouvrir dans le navigateur" pour voir le résultat
   - Cliquez sur "Générer"

3. Les bons de commande sont créés dans le dossier :
   bons_commande_YYYYMMDD_HHMMSS/

4. Pour générer un PDF :
   - Ouvrez le fichier HTML dans votre navigateur
   - Appuyez sur Ctrl+P
   - Choisissez "Enregistrer en PDF"

====================================================
   FORMAT DU FICHIER CSV
====================================================

Votre fichier CSV doit contenir ces colonnes :

- Nom du payeur
- Prénom de l'enfant
- Nom de l'enfant
- Classe
- Produit
- Quantité
- Prix unitaire
- Moyen de paiement

Exemple :
"Dupont","Marie","Dupont","CE1","Vanille 50g","2","5.00","Espèces"

====================================================
   CONFIGURATION REQUISE
====================================================

✅ Windows 10 ou 11 (64-bit)
✅ Aucune installation nécessaire !
✅ Pas besoin de Python
✅ Fonctionne directement

====================================================
   SUPPORT & DOCUMENTATION
====================================================

📚 Guide complet : https://github.com/Kiwi41/ape-commandes-vanille
📧 Questions : kevin.favry@worldline.com

====================================================
   NOTES
====================================================

- L'exécutable contient Python embarqué (c'est normal qu'il fasse ~10 MB)
- Au premier lancement, Windows peut afficher un avertissement de sécurité
  (cliquez sur "Plus d'infos" puis "Exécuter quand même")
- Tous les fichiers générés sont créés dans le même dossier que l'exe

====================================================
   LICENCE
====================================================

Open Source - Libre d'utilisation pour l'APE de Villebarou

© 2025 - APE Villebarou
