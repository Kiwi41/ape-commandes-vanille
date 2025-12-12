# Guide d'installation pour l'export PDF

Ce guide vous aidera à installer `weasyprint` pour activer l'export PDF direct.

## 🪟 Windows

### Étape 1 : Installer GTK+ (requis)

1. Téléchargez **GTK+ for Windows** :
   - 📥 [Télécharger ici](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)
   - Prenez la dernière version (ex: `gtk3-runtime-x.x.x-x-ts-win64.exe`)

2. Exécutez l'installateur
3. Redémarrez votre terminal PowerShell

### Étape 2 : Installer weasyprint

```powershell
pip install weasyprint
```

### Étape 3 : Tester

```powershell
python generer_bons_commande.py --pdf
```

## 🐧 Linux (Ubuntu/Debian)

```bash
# Installer les dépendances système
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# Installer weasyprint
pip install weasyprint
```

## 🍎 macOS

```bash
# Installer les dépendances avec Homebrew
brew install python3 cairo pango gdk-pixbuf libffi

# Installer weasyprint
pip install weasyprint
```

## ❓ Problèmes courants

### Windows : "cairo.dll not found"

**Solution** : GTK+ n'est pas correctement installé ou pas dans le PATH.
1. Réinstallez GTK+
2. Vérifiez que le dossier `C:\Program Files\GTK3-Runtime Win64\bin` est dans votre PATH
3. Redémarrez votre terminal

### "No module named 'weasyprint'"

**Solution** : weasyprint n'est pas installé dans le bon environnement Python.
```bash
# Vérifiez votre Python
python --version

# Réinstallez weasyprint
pip install --upgrade weasyprint
```

### Erreur de compilation

**Solution** : Installez les dépendances système d'abord (voir sections Linux/macOS ci-dessus).

## 🎯 Alternative : Impression PDF depuis le navigateur

Si l'installation de weasyprint pose problème, vous pouvez simplement :

1. Générer le HTML normalement :
   ```bash
   python generer_bons_commande.py
   ```

2. Dans le navigateur ouvert, utilisez `Ctrl+P` (ou `Cmd+P` sur Mac)

3. Sélectionnez "Enregistrer au format PDF"

Cette méthode fonctionne sur tous les systèmes sans installation supplémentaire ! ✨

## 📚 Ressources

- [Documentation weasyprint](https://doc.courtbouillon.org/weasyprint/)
- [GTK+ for Windows](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)
- [Problèmes connus weasyprint](https://github.com/Kozea/WeasyPrint/issues)
