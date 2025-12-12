#  Démarrage Rapide

Ce guide vous permet de commencer rapidement avec le générateur de bons de commande.

##  Utilisation Basique

### 1. Interface Graphique (Recommandé)

**La méthode la plus simple** :
```bash
# Windows : double-cliquez sur lancer_gui.bat
# Ou :
python generer_gui.py
```

Voir le [Guide GUI complet](GUI_GUIDE.md) pour plus de détails.

### 2. Ligne de commande (pour utilisateurs avancés)

```bash
# Lancement basique (auto-détection du CSV dans Downloads)
python generer_bons_commande.py

# Avec un fichier spécifique
python generer_bons_commande.py chemin/vers/export-vanille.csv
```

##  Exemples d'utilisation

### Génération standard

```bash
# Le script cherche automatiquement dans Downloads
python generer_bons_commande.py

# Ou avec un fichier spécifique
python generer_bons_commande.py mon_export.csv
```

### Batch processing

```bash
# Traiter plusieurs fichiers
python generer_bons_commande.py export1.csv
python generer_bons_commande.py export2.csv
python generer_bons_commande.py export3.csv
```

##  Alias pratiques (optionnel)

### PowerShell (Windows)
```powershell
# Ajouter dans votre profil PowerShell
function genbon { python C:\chemin\vers\generer_bons_commande.py $args }

# Utilisation
genbon
genbon mon_fichier.csv
```

### Bash (Linux/macOS)
```bash
# Ajouter dans ~/.bashrc ou ~/.zshrc
alias genbon='python3 /chemin/vers/generer_bons_commande.py'

# Utilisation
genbon
genbon mon_fichier.csv
```

##  Fichiers générés

À la fin de l'exécution, vous aurez :
-  Un fichier `bons_commande_[nom_csv].html`
-  Dans le même dossier que le fichier CSV source

**Pour obtenir un PDF** :
1. Ouvrez le HTML dans votre navigateur
2. Appuyez sur `Ctrl+P` (Windows/Linux) ou `Cmd+P` (macOS)
3. Sélectionnez "Enregistrer au format PDF"

##  Ce que fait le script

1.  Trouve le fichier CSV (auto ou manuel)
2.  Analyse les données
3.  Regroupe par payeur
4.  Génère les bons de commande HTML
5.  Calcule les statistiques par classe
6.  Ouvre automatiquement le résultat

##  Résolution de problèmes

### Fichier CSV non trouvé
- Placez votre CSV dans le dossier Downloads
- Ou spécifiez le chemin complet : `python generer_bons_commande.py C:\chemin\complet\fichier.csv`

### Problème d'encodage
- Le script gère automatiquement l'UTF-8
- Si problème : vérifiez que votre CSV est en UTF-8

### Le fichier ne s'ouvre pas
- Ouvrez manuellement le fichier HTML généré
- Le chemin est affiché dans la console

##  Pour aller plus loin

- [ Guide Interface Graphique](GUI_GUIDE.md) - Mode d'emploi du GUI
- [ README complet](README.md) - Documentation complète
- [ Personnalisation](README.md#personnalisation) - Adapter à vos besoins
