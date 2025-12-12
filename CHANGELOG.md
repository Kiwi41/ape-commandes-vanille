# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.3.0] - 2025-12-12

###  Ajouté
- **Interface Graphique (GUI)** avec tkinter pour utilisateurs non techniques
- Application `generer_gui.py` avec fonctionnalités complètes :
  - Sélection de fichier CSV via bouton "Parcourir"
  - Auto-détection intelligente dans le dossier Téléchargements
  - Console de sortie en temps réel avec scrolling
  - Ouverture automatique optionnelle des résultats
  - Note explicative pour générer des PDF via navigateur (Ctrl+P)
- Scripts de lancement faciles :
  - `lancer_gui.bat` pour Windows (double-clic)
  - `lancer_gui.sh` pour Linux/macOS
- Guide complet `GUI_GUIDE.md` avec :
  - Instructions de lancement multi-plateformes
  - Aperçu ASCII de l'interface
  - Guide pas à pas d'utilisation
  - Section de dépannage (installation tkinter)
  - Conseils et raccourcis clavier

###  Améliorations
- Threading pour exécution non-bloquante de la génération
- Gestion d'erreurs avec messages clairs dans la console GUI
- Header vert APE (#4CAF50) pour identité visuelle
- Redirection subprocess pour affichage temps réel
- Vérification de disponibilité Python dans les lanceurs

###  Corrections
- **Fix threading Tkinter** : Correction des appels messagebox depuis thread avec lambda
- **Fix encodage Windows** : Configuration UTF-8 forcée pour stdout/stderr (résout UnicodeEncodeError avec émojis)
- **Simplification PDF** : Retrait des options PDF (weasyprint trop complexe sur Windows), remplacé par note Ctrl+P
- **Fix doublon** : Suppression du label PDF en double dans l'interface

###  Documentation
- README mis à jour avec section GUI en tête
- Guide GUI ajouté aux liens de documentation
- Instructions différenciées débutants/ligne de commande
- Retrait des références à l'export PDF automatique

