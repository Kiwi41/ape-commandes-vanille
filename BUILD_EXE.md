# 🏗️ Création d'un Exécutable Windows (.exe)

Ce guide explique comment créer un fichier `.exe` autonome qui peut être lancé sur n'importe quel PC Windows **sans avoir Python installé**.

## 📦 Méthode Automatique (Recommandée)

### Étape 1 : Préparation

Assurez-vous que PyInstaller est installé :

```bash
pip install pyinstaller
```

### Étape 2 : Lancer le script de build

Double-cliquez sur le fichier :

```
build_exe.bat
```

Ou lancez-le depuis un terminal :

```bash
build_exe.bat
```

### Étape 3 : Récupérer l'exécutable

L'exécutable sera créé dans le dossier `dist/` :

```
dist/APE_Bons_Commande.exe
```

**Taille approximative** : ~15-20 MB (contient Python embarqué)

## 📋 Méthode Manuelle

Si vous préférez créer l'exécutable manuellement :

```bash
# 1. Installer PyInstaller
pip install pyinstaller

# 2. Créer l'exécutable
pyinstaller --onefile --windowed --name "APE_Bons_Commande" generer_gui.py

# 3. Récupérer l'exe
# Il sera dans : dist/APE_Bons_Commande.exe
```

## 🚀 Utilisation de l'Exécutable

### Sur votre PC

1. L'exécutable est dans `dist/APE_Bons_Commande.exe`
2. Double-cliquez dessus pour lancer l'application
3. L'interface graphique s'ouvre immédiatement

### Sur un autre PC Windows

1. **Copiez** le fichier `APE_Bons_Commande.exe` sur une clé USB
2. **Transférez-le** sur le PC cible (n'importe quelle version de Windows 10/11)
3. **Double-cliquez** sur l'exe - ça fonctionne directement !

**Aucune installation requise** : pas besoin de Python, pas de dépendances, tout est embarqué.

## 🎯 Options Avancées

### Créer avec une icône personnalisée

Si vous avez un fichier `.ico` :

```bash
pyinstaller --onefile --windowed --icon=mon_icone.ico --name "APE_Bons_Commande" generer_gui.py
```

### Créer en mode console (pour debug)

Si vous voulez voir les messages d'erreur :

```bash
pyinstaller --onefile --name "APE_Bons_Commande" generer_gui.py
```

(Enlevez `--windowed` pour afficher une console)

### Inclure des fichiers supplémentaires

Si votre script a besoin de fichiers externes :

```bash
pyinstaller --onefile --windowed --add-data "fichier.txt;." generer_gui.py
```

## ❓ Dépannage

### PyInstaller n'est pas reconnu

```bash
# Installez PyInstaller
pip install pyinstaller

# Ou avec le chemin complet de Python
python -m PyInstaller ...
```

### L'exe ne se lance pas

1. **Essayez en mode console** (sans `--windowed`) pour voir les erreurs
2. **Vérifiez l'antivirus** : il peut bloquer l'exe (ajoutez une exception)
3. **Windows Defender** : peut mettre l'exe en quarantaine à la première exécution

### L'exe est trop gros

C'est normal ! PyInstaller embarque :
- Python complet (~5-10 MB)
- Tkinter et ses dépendances (~5-8 MB)
- Votre code et bibliothèques (~1-2 MB)

**Total** : ~15-20 MB (acceptable pour une distribution facile)

### Optimiser la taille

Pour réduire la taille :

```bash
# Utiliser UPX (compresseur)
pip install pyinstaller[encryption]
pyinstaller --onefile --windowed --upx-dir=./upx generer_gui.py
```

## 🔒 Sécurité et Antivirus

**Important** : Les exécutables PyInstaller sont parfois détectés comme suspects par certains antivirus (faux positifs).

### Solutions :

1. **Signez numériquement** l'exe (avec un certificat de signature de code)
2. **Ajoutez une exception** dans Windows Defender
3. **Distribuez avec un README** expliquant que c'est un script Python empaqueté

### Vérifier que l'exe est sain

Après compilation, scannez sur [VirusTotal](https://www.virustotal.com) pour rassurer les utilisateurs.

## 📚 Documentation PyInstaller

Pour plus d'options :
- [Documentation officielle](https://pyinstaller.org/en/stable/)
- [Options de ligne de commande](https://pyinstaller.org/en/stable/usage.html)

## ✅ Checklist de Distribution

Avant de distribuer l'exécutable :

- [ ] Testé sur votre PC Windows
- [ ] Testé sur un PC sans Python installé
- [ ] Créé un README pour les utilisateurs
- [ ] Vérifié que le CSV fonctionne
- [ ] Scanné avec antivirus (pour rassurer)
- [ ] Compressé en ZIP avec documentation

## 📦 Package de Distribution Recommandé

Créez un dossier `APE_Bons_Commande_v1.3/` avec :

```
APE_Bons_Commande_v1.3/
├── APE_Bons_Commande.exe          # L'exécutable
├── README.txt                      # Guide rapide
├── exemple_export.csv              # Fichier CSV d'exemple
└── LICENCE.txt                     # Si besoin
```

Puis créez un ZIP : `APE_Bons_Commande_v1.3.zip`

## 🎉 C'est Tout !

Votre application est maintenant distribuable sur n'importe quel PC Windows 10/11 !
