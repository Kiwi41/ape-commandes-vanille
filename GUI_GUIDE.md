#  Guide d'utilisation de l'Interface Graphique (GUI)

L'interface graphique permet d'utiliser le générateur de bons de commande sans avoir à taper de commandes.

##  Lancement rapide

### Windows
1. Double-cliquez sur `lancer_gui.bat`
2. Ou dans PowerShell : `python generer_gui.py`

### Linux / macOS
1. Dans le terminal : `./lancer_gui.sh` (donnez les permissions : `chmod +x lancer_gui.sh`)
2. Ou : `python3 generer_gui.py`

##  Utilisation

### 1. Sélection du fichier CSV

**Option A : Parcourir manuellement**
- Cliquez sur le bouton ` Parcourir`
- Naviguez vers votre fichier CSV
- Sélectionnez-le

**Option B : Auto-détection**
- Cliquez sur le bouton ` Auto-détection`
- Le programme cherchera automatiquement le dernier fichier CSV contenant "vanille" dans vos Téléchargements

### 2. Options de génération

- ** Ouvrir automatiquement le fichier généré**
  - Ouvre le fichier HTML dans votre navigateur par défaut

** Pour obtenir un PDF** : 
- Ouvrez le HTML généré dans votre navigateur
- Appuyez sur `Ctrl+P` (Windows/Linux) ou `Cmd+P` (macOS)
- Sélectionnez "Enregistrer au format PDF"

### 3. Génération

- Cliquez sur le gros bouton vert ` GÉNÉRER LES BONS DE COMMANDE`
- La console affiche la progression en temps réel
- Une barre de progression apparaît pendant le traitement
- Un message confirme le succès ou signale les erreurs

### 4. Résultat

La fenêtre de résultat affiche :
-  Fichier CSV détecté
-  Statistiques (période, nombre de payeurs, montant total)
-  Statistiques par classe
-  Chemin du fichier généré
-  Confirmation de succès

##  Aperçu de l'interface

```

   Générateur de Bons de Commande          
  APE Villebarou - Ventes de Produits       

                                             
   Fichier CSV                             
     
   chemin/vers/fichier.csv                
     
  [ Parcourir] [ Auto-détection]        
                                             
   Options de Génération                  
    Ouvrir automatiquement le fichier    
   Pour PDF : Ctrl+P dans le navigateur   
                                             
  ℹ Informations                            
  Le générateur va :                         
   Analyser le fichier CSV d'export        
   Regrouper les commandes par payeur      
   Générer des bons imprimables            
   Afficher les statistiques par classe    
                                             
     
     GÉNÉRER LES BONS DE COMMANDE       
     
                                             
   Résultat de la Génération              
     
    Démarrage de la génération...       
    Fichier détecté: export.csv         
    31 payeur(s) avec commandes          
    Montant total : 1025.00 €            
    GÉNÉRATION TERMINÉE !                
     

```

##  Dépannage

### L'interface ne se lance pas

**Vérifiez que Python est installé :**
```bash
python --version
```

**Vérifiez que tkinter est installé :**
```bash
python -c "import tkinter"
```

Si erreur, installez tkinter :
- **Windows** : Inclus avec Python (réinstallez Python en cochant "tcl/tk")
- **Ubuntu/Debian** : `sudo apt-get install python3-tk`
- **macOS** : Inclus avec Python

### "Aucun fichier trouvé" avec auto-détection

- Vérifiez que le fichier CSV est bien dans le dossier **Téléchargements**
- Le nom du fichier doit contenir "**vanille**" ou commencer par "**export-**"
- Sinon, utilisez le bouton **Parcourir**

### Le fichier ne s'ouvre pas automatiquement

- Décochez "Ouvrir automatiquement"
- Ouvrez manuellement le fichier HTML généré (affiché dans la console)

##  Avantages de l'interface graphique

-  **Pas de ligne de commande** : Tout en quelques clics
-  **Feedback visuel** : Progression en temps réel
-  **Auto-détection** : Trouve automatiquement votre fichier
-  **Messages clairs** : Erreurs et succès bien expliqués
-  **Simple** : Parfait pour les bénévoles non techniques

##  Conseils

- **Utilisez l'auto-détection** pour gagner du temps
- **Consultez la console** pour voir les détails de la génération
- **Le HTML est prêt à imprimer** : Utilisez Ctrl+P pour un PDF
- **Les fichiers sont au même endroit** que le CSV source
