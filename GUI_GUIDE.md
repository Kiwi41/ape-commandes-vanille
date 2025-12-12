# 🖥️ Guide d'utilisation de l'Interface Graphique (GUI)

L'interface graphique permet d'utiliser le générateur de bons de commande sans avoir à taper de commandes.

## 🚀 Lancement rapide

### Windows
1. Double-cliquez sur `lancer_gui.bat`
2. Ou dans PowerShell : `python generer_gui.py`

### Linux / macOS
1. Dans le terminal : `./lancer_gui.sh` (donnez les permissions : `chmod +x lancer_gui.sh`)
2. Ou : `python3 generer_gui.py`

## 📋 Utilisation

### 1. Sélection du fichier CSV

**Option A : Parcourir manuellement**
- Cliquez sur le bouton `📂 Parcourir`
- Naviguez vers votre fichier CSV
- Sélectionnez-le

**Option B : Auto-détection**
- Cliquez sur le bouton `🔍 Auto-détection`
- Le programme cherchera automatiquement le dernier fichier CSV contenant "vanille" dans vos Téléchargements

### 2. Options de génération

Cochez les options souhaitées :

      
      
- **🌐 Ouvrir automatiquement le fichier généré**
  
### 3. Génération

- Cliquez sur le gros bouton vert `🚀 GÉNÉRER LES BONS DE COMMANDE`
- La console affiche la progression en temps réel
- Une barre de progression apparaît pendant le traitement
- Un message confirme le succès ou signale les erreurs

### 4. Résultat

La fenêtre de résultat affiche :
- ✓ Fichier CSV détecté
- 📊 Statistiques (période, nombre de payeurs, montant total)
- 📈 Statistiques par classe
- 📄 Chemin du fichier généré
- ✅ Confirmation de succès

## 🎨 Aperçu de l'interface

```
┌─────────────────────────────────────────────┐
│  🌿 Générateur de Bons de Commande          │
│  APE Villebarou - Ventes de Produits       │
├─────────────────────────────────────────────┤
│                                             │
│  📁 Fichier CSV                             │
│  ┌─────────────────────────────────────┐   │
│  │ chemin/vers/fichier.csv             │   │
│  └─────────────────────────────────────┘   │
│  [📂 Parcourir] [🔍 Auto-détection]        │
│                                             │
│  ⚙️ Options de Génération                  │
│  ☐ 📄 Générer aussi un fichier PDF         │
│  ☐ 📄 Générer uniquement le PDF            │
│  ☑ 🌐 Ouvrir automatiquement le fichier    │
│                                             │
│  ℹ️ Informations                            │
│  Le générateur va :                         │
│  • Analyser le fichier CSV d'export        │
│  • Regrouper les commandes par payeur      │
│  • Générer des bons imprimables            │
│  • Afficher les statistiques par classe    │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │ 🚀 GÉNÉRER LES BONS DE COMMANDE       │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  📊 Résultat de la Génération              │
│  ┌─────────────────────────────────────┐   │
│  │ ✓ Fichier détecté : export.csv     │   │
│  │ 📊 ANALYSE DU FICHIER CSV           │   │
│  │ ✓ Période détectée : 17/11 au 08/12│   │
│  │ ✓ 31 payeur(s) avec commandes       │   │
│  │ ...                                  │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

## ⚡ Raccourcis clavier

- `Ctrl+O` : Ouvrir le dialogue de sélection de fichier (pas encore implémenté)
- `Ctrl+Q` : Quitter l'application (standard)

## ❓ Dépannage

### L'interface ne se lance pas

**Problème** : `ModuleNotFoundError: No module named 'tkinter'`

**Solution Windows** :
```bash
# Réinstallez Python en cochant "tcl/tk and IDLE"
# Ou installez via :
pip install tk
```

**Solution Linux (Ubuntu/Debian)** :
```bash
sudo apt-get install python3-tk
```

**Solution macOS** :
```bash
# tkinter est inclus avec Python de python.org
# Si problème avec Homebrew Python :
brew install python-tk
```

### Le bouton "Générer" ne fait rien

- Vérifiez que `generer_bons_commande.py` est dans le même dossier
- Consultez la console de résultat pour les messages d'erreur
- Vérifiez que le fichier CSV sélectionné existe

### L'auto-détection ne trouve rien

- Vérifiez que votre fichier CSV contient "vanille" dans le nom
- Ou commence par "export-"
- Utilisez le bouton "Parcourir" pour sélectionner manuellement

### Le PDF ne se génère pas


## 🎯 Avantages de l'interface graphique

✅ **Plus simple** : Pas besoin de taper des commandes  
✅ **Visuel** : Sélection de fichiers par dialogue  
✅ **Feedback** : Console en temps réel  
✅ **Accessible** : Utilisable par tous, même sans connaissances techniques  
✅ **Options claires** : Cases à cocher pour les options  

## 💡 Astuces

1. **Glisser-déposer** : Vous pouvez glisser un fichier CSV dans le champ de saisie (sur certains systèmes)

2. **Historique** : Le dernier fichier utilisé est mémorisé (fonctionnalité à venir)

3. **Multi-génération** : Vous pouvez générer plusieurs bons successivement sans fermer l'application

## 🔙 Revenir à la ligne de commande

Si vous préférez la ligne de commande :
```bash
python generer_bons_commande.py
```

Voir [QUICKSTART.md](QUICKSTART.md) pour plus d'exemples en ligne de commande.

---

💚 **L'interface graphique rend le générateur accessible à tous les bénévoles APE !**
