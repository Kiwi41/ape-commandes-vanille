# 🚀 Quick Start - Test rapide du générateur

Ce fichier vous permet de tester rapidement le générateur avec vos propres données.

## 📋 Utilisation rapide

### 1. Génération HTML simple

```bash
python generer_bons_commande.py
```
*Appuyez sur Entrée pour auto-détecter le fichier CSV dans Downloads*

### 2. Test avec le fichier d'exemple

```bash
python generer_bons_commande.py exemple_export_template.csv
```

```bash
# HTML + PDF
python generer_bons_commande.py 
# Uniquement PDF
python generer_bons_commande.py ```

## 🎯 Exemples de commandes

### Cas d'usage typiques

```bash
# Auto-détection + HTML
python generer_bons_commande.py

# Fichier spécifique + PDF
python generer_bons_commande.py mon_export.csv 
# Plusieurs fichiers à traiter
python generer_bons_commande.py export1.csv
python generer_bons_commande.py export2.csv python generer_bons_commande.py export3.csv ```

## ⚡ Raccourcis PowerShell (Windows)

Créez un alias pour simplifier :

```powershell
# Ajoutez dans votre profil PowerShell
Set-Alias genbon "python C:\chemin\vers\generer_bons_commande.py"

# Utilisation
genbon
genbon genbon mon_fichier.csv ```

## 🐧 Raccourcis Bash (Linux/macOS)

```bash
# Ajoutez dans votre .bashrc ou .zshrc
alias genbon='python /chemin/vers/generer_bons_commande.py'

# Utilisation
genbon
genbon genbon mon_fichier.csv ```

## 📊 Résultat attendu

Après exécution, vous obtiendrez :

- ✅ Un fichier `bons_commande_[nom_csv].html` 
- ✅ Optionnel : Un fichier `bons_commande_[nom_csv].pdf`
- 📱 Ouverture automatique dans le navigateur/lecteur PDF
- 📊 Statistiques affichées dans la console

## ❓ Aide

```bash
python generer_bons_commande.py --help
```

## 🐛 Dépannage rapide

### Le script ne trouve pas mon CSV
- Vérifiez que le fichier contient "vanille" dans son nom
- Ou spécifiez le chemin complet : `python generer_bons_commande.py C:\chemin\vers\fichier.csv`

### Génération PDF

### Le fichier ne s'ouvre pas automatiquement
- Ouvrez manuellement le fichier HTML/PDF généré
- Il se trouve dans le même dossier que votre CSV source

## 💡 Astuce

Pour traiter plusieurs ventes dans l'année, créez un dossier par campagne :

```
Ventes_APE/
├── 2025_Vanille/
│   ├── export.csv
│   └── bons_commande_export.html
├── 2025_Chocolats/
│   ├── export.csv
│   └── bons_commande_export.html
└── 2025_Calendriers/
    ├── export.csv
    └── bons_commande_export.html
```

---

🎉 **Prêt à générer vos bons de commande !**
