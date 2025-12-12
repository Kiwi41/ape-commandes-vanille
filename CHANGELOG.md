# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.1.0] - 2025-12-12

### ✨ Ajouté
- **Export PDF direct** avec l'option `--pdf` ou `--pdf-only`
- Support de `argparse` pour une meilleure gestion des arguments
- Fichier `requirements.txt` pour les dépendances optionnelles
- Guide d'installation PDF (`INSTALL_PDF.md`)
- Gestion d'erreur gracieuse si weasyprint n'est pas installé
- CSS spécifique pour optimiser le rendu PDF

### 🔧 Modifié
- Arguments en ligne de commande refactorisés avec argparse
- README mis à jour avec les nouvelles options d'utilisation
- Messages de sortie plus clairs et informatifs

### 📚 Documentation
- Ajout de la section "Export PDF" dans le README
- Instructions d'installation détaillées pour Windows/Linux/macOS
- Alternative avec impression navigateur documentée

## [1.0.0] - 2025-12-12

### ✨ Ajouté
- Script principal `generer_bons_commande.py`
- Auto-détection des fichiers CSV contenant "vanille"
- Regroupement automatique des commandes par payeur
- Génération HTML responsive optimisée pour l'impression
- Code couleur visuel (vert = avec classe, orange = sans classe)
- Icônes de paiement selon le moyen (carte, espèces, chèque, virement, PayPal)
- Extraction automatique de la période de commandes
- Affichage des informations enfant/classe
- Calcul automatique des totaux
- Ouverture automatique dans le navigateur
- Documentation complète (README, CONTRIBUTING, LICENSE)
- Fichier d'exemple CSV

### 🎨 Design
- Bordures en pointillés pour faciliter la découpe
- Zones de signature pour validation
- Badges de statut (avec/sans classe)
- Gradients de couleur pour les en-têtes
- Style print-friendly sans éléments superflus

### 📊 Statistiques
- Nombre total de bons générés
- Répartition avec/sans classe
- Montant total des commandes
- Période des commandes

## [Future] - À venir

### 🔮 Prévu
- ✅ ~~Export PDF direct~~ (Ajouté en v1.1.0)
- Interface graphique (GUI)
- Statistiques par classe
- Filtrage par moyen de paiement
- Envoi automatique par email
- Support des réductions/remises
- Multi-langues (anglais)
- Mode batch pour plusieurs campagnes

---

[1.1.0]: https://github.com/Kiwi41/ape-commandes-vanille/releases/tag/v1.1.0
[1.0.0]: https://github.com/Kiwi41/ape-commandes-vanille/releases/tag/v1.0.0
