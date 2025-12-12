# ðŸŒ¿ GÃ©nÃ©rateur de Bons de Commande - Vente de Vanille APE

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub release](https://img.shields.io/badge/release-v1.3.0-brightgreen.svg)](https://github.com/Kiwi41/ape-commandes-vanille/releases)

Script Python pour gÃ©nÃ©rer automatiquement des bons de commande imprimables Ã  partir d'un export CSV de commandes de produits vanille (ou tout autre produit).

## ðŸš€ DÃ©marrage rapide

### Interface Graphique (RecommandÃ© pour dÃ©butants)

```bash
# Windows : double-cliquez sur lancer_gui.bat
# Ou :
python generer_gui.py
```

### Ligne de commande

```bash
# Clone et utilisation basique
git clone https://github.com/Kiwi41/ape-commandes-vanille.git
cd ape-commandes-vanille
python generer_bons_commande.py


```

ðŸ“– **Guides disponibles** :
- [ðŸ–¥ï¸ Guide Interface Graphique](GUI_GUIDE.md) - Utilisation de l'interface visuelle (recommandÃ©)
- [âš¡ DÃ©marrage rapide](QUICKSTART.md) - Premiers pas et exemples en ligne de commande
- [ðŸ“„ Installation PDF](INSTALL_PDF.md) - Installer weasyprint pour l'export PDF
- [ðŸ¤ Contribution](CONTRIBUTING.md) - Comment contribuer au projet
- [ðŸ“ Changelog](CHANGELOG.md) - Historique des versions

## ðŸ“‹ Table des matiÃ¨res

- [FonctionnalitÃ©s](#-fonctionnalitÃ©s)
- [PrÃ©requis](#-prÃ©requis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Format du CSV](#-format-du-csv)
- [Personnalisation](#-personnalisation)
- [Exemples](#-exemples)
- [Captures d'Ã©cran](#-captures-dÃ©cran)
- [Contribution](#-contribution)
- [Licence](#-licence)

## âœ¨ FonctionnalitÃ©s

- **ï¿½ï¸ Interface Graphique** : Application conviviale pour utilisateurs non techniques
- **ï¿½ðŸ“Š Analyse automatique** : DÃ©tection automatique du fichier CSV et extraction de la pÃ©riode de commandes
- **ðŸ‘¥ Regroupement par payeur** : Consolidation de toutes les commandes d'une mÃªme famille sur un seul bon
- **ðŸŽ¨ Code couleur visuel** :
  - ðŸŸ¢ **Vert** : Commandes avec classe assignÃ©e (livraison facilitÃ©e)
  - ðŸŸ  **Orange** : Commandes sans classe (nÃ©cessite vÃ©rification)
- **ï¿½ Statistiques par classe** :
  - Nombre d'enfants par classe
  - Nombre de familles par classe
  - Montant total par classe
  - Tableau rÃ©capitulatif interactif dans le HTML
- **ï¿½ðŸ’³ IcÃ´nes de paiement** :
  - ðŸ’³ Carte bancaire
  - ðŸ’µ EspÃ¨ces
  - ðŸ“ ChÃ¨que
  - ðŸ¦ Virement
  - ðŸ…¿ï¸ PayPal
  - ðŸ’° Autre
- **ï¿½ Export PDF** : GÃ©nÃ©ration directe de PDF prÃªts Ã  imprimer (optionnel)
- **ï¿½ðŸ–¨ï¸ OptimisÃ© pour l'impression** : DÃ©coupe facile avec bordures en pointillÃ©s
- **ðŸ“± Responsive** : Affichage adaptÃ© Ã  tous les Ã©crans
- **ðŸ”„ RÃ©utilisable** : Configuration simple pour de futures campagnes de vente

## ðŸ”§ PrÃ©requis

- **Python 3.7+** (aucune dÃ©pendance externe requise pour la gÃ©nÃ©ration HTML)
- Un fichier CSV d'export de commandes (format dÃ©taillÃ© ci-dessous)
- **Optionnel pour PDF** : `weasyprint` (voir installation ci-dessous)

## ðŸ“¥ Installation

### Option 1 : Clone du repository

```bash
git clone https://github.com/Kiwi41/ape-commandes-vanille.git
cd ape-commandes-vanille
```

### Option 2 : Installation avec support PDF

```bash
# Clone du repository
git clone https://github.com/Kiwi41/ape-commandes-vanille.git
cd ape-commandes-vanille

# Installation des dÃ©pendances pour le PDF
pip install -r requirements.txt
```

**Note Windows** : `weasyprint` nÃ©cessite GTK+ sur Windows.  
ðŸ“¥ TÃ©lÃ©chargez-le depuis : [GTK+ for Windows](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

### Option 3 : TÃ©lÃ©chargement direct (sans Git)

1. TÃ©lÃ©chargez `generer_bons_commande.py`
2. Placez-le dans le dossier de votre choix

## ðŸš€ Utilisation

### Mode 1 : GÃ©nÃ©ration HTML simple (recommandÃ©)

Placez votre fichier CSV dans le dossier **Downloads** avec "vanille" dans le nom, puis lancez :

```bash
python generer_bons_commande.py
```

Appuyez sur **EntrÃ©e** pour que le script dÃ©tecte automatiquement le dernier fichier.

### Mode 2 : GÃ©nÃ©ration avec export PDF

```bash
# GÃ©nÃ©rer HTML + PDF
python generer_bons_commande.py --pdf

# GÃ©nÃ©rer uniquement le PDF (pas de HTML)
python generer_bons_commande.py --pdf-only
```

### Mode 3 : Avec chemin de fichier spÃ©cifique

```bash
# HTML seulement
python generer_bons_commande.py chemin/vers/votre/fichier.csv

# HTML + PDF
python generer_bons_commande.py chemin/vers/votre/fichier.csv --pdf
```

### Options disponibles

| Option | Description |
|--------|-------------|
| (aucune) | GÃ©nÃ¨re uniquement le HTML et l'ouvre dans le navigateur |
| `--pdf` | GÃ©nÃ¨re HTML + PDF |
| `--pdf-only` | GÃ©nÃ¨re uniquement le PDF (pas de HTML) |
| `-h, --help` | Affiche l'aide complÃ¨te |

### Mode 2 : Avec argument

```bash
python generer_bons_commande.py chemin/vers/votre/fichier.csv
```

### Mode 3 : Saisie manuelle

```bash
python generer_bons_commande.py
# Puis entrez le chemin du fichier CSV lorsque demandÃ©
```

### RÃ©sultat

Le script gÃ©nÃ¨re un fichier HTML nommÃ© `bons_commande_[nom_du_csv].html` qui s'ouvre automatiquement dans votre navigateur par dÃ©faut.

## ðŸ“„ Format du CSV

Le fichier CSV doit contenir les colonnes suivantes (sÃ©parateur `;`, encodage UTF-8) :

| Colonne | Description | Obligatoire |
|---------|-------------|-------------|
| `RÃ©fÃ©rence commande` | Identifiant unique de la commande | âœ… |
| `Classe de l'enfant` | Classe de l'enfant (ex: CE2 A) | âŒ |
| `PrÃ©nom de l'enfant` | PrÃ©nom de l'enfant | âœ… |
| `Nom de l'enfant` | Nom de l'enfant | âœ… |
| `PrÃ©nom payeur` | PrÃ©nom du parent/payeur | âœ… |
| `Nom payeur` | Nom du parent/payeur | âœ… |
| `Email payeur` | Email du payeur | âŒ |
| `nÂ° de tÃ©lÃ©phone` | TÃ©lÃ©phone du payeur | âŒ |
| `Tarif` | Nom du produit commandÃ© | âœ… |
| `Montant tarif` | Prix unitaire (format: `10,00`) | âœ… |
| `Date de la commande` | Date au format `DD/MM/YYYY` | âœ… |
| `Moyen de paiement` | Mode de paiement (ex: "Carte bancaire") | âŒ |

### Exemple de fichier CSV

```csv
RÃ©fÃ©rence commande;Classe de l'enfant;PrÃ©nom de l'enfant;Nom de l'enfant;PrÃ©nom payeur;Nom payeur;Email payeur;nÂ° de tÃ©lÃ©phone;Tarif;Montant tarif;Date de la commande;Moyen de paiement
CMD001;CE2 A;Marie;Dupont;Sophie;Dupont;sophie.dupont@email.com;0612345678;12 gousses 14cm;10,00;17/11/2025;Carte bancaire
CMD002;CE2 A;Marie;Dupont;Sophie;Dupont;sophie.dupont@email.com;0612345678;Poudre de vanille 25g;5,00;17/11/2025;Carte bancaire
```

## âš™ï¸ Personnalisation

Modifiez la section **CONFIGURATION** dans le script (lignes 12-50) :

```python
# Nom du produit
PRODUIT_NOM = "Gousses de Vanille Bourbon de Madagascar"

# Association/Organisation
ORGANISATION = "APE Villebarou"
ORGANISATION_COMPLET = "APE Villebarou â€¢ Association de Parents d'Ã‰lÃ¨ves"
```

### Adaptation pour d'autres produits

Ce script est facilement adaptable pour :
- Ventes de chocolats
- Ventes de fromages
- Ventes de calendriers
- Ventes de fleurs
- Tout autre produit vendu par une APE/association

Il suffit de modifier `PRODUIT_NOM` et `ORGANISATION` !

## ðŸ“Š Exemples

### Sortie console

```
======================================================================
ðŸ“Š ANALYSE DU FICHIER CSV
======================================================================
âœ“ PÃ©riode dÃ©tectÃ©e : PÃ©riode du 17/11/2025 au 08/12/2025
âœ“ 31 payeur(s) avec commandes
âœ“ Montant total : 1025.00 â‚¬
âœ“ Fichier de sortie : bons_commande_export-vanille.html
======================================================================

======================================================================
âœ… BONS DE COMMANDE GÃ‰NÃ‰RÃ‰S
======================================================================

ðŸ“„ Fichier crÃ©Ã© : bons_commande_export-vanille.html
ðŸ“‚ Emplacement : C:\Users\...\Downloads

ðŸ“Š RÃ©capitulatif :
   â€¢ Total de bons : 31
   â€¢ Avec classe (vert) : 24
   â€¢ Sans classe (orange) : 7
   â€¢ Montant total : 1025.00 â‚¬
   â€¢ PÃ©riode : PÃ©riode du 17/11/2025 au 08/12/2025

ðŸ’¡ Ouverture automatique du fichier dans le navigateur...
======================================================================

âœ“ Fichier ouvert dans le navigateur
```

### Structure d'un bon de commande

Chaque bon contient :
- âœ‚ï¸ **Marques de dÃ©coupe** (bordures en pointillÃ©s)
- ðŸ“‹ **NumÃ©ro de bon** et badge de statut (avec/sans classe)
- ðŸ’³ **Nom du payeur** avec icÃ´ne de paiement
- ðŸ“ž **CoordonnÃ©es** (tÃ©lÃ©phone, email)
- ðŸ‘¨â€ðŸ‘©â€ðŸ‘§â€ðŸ‘¦ **Liste des enfants** avec leurs classes
- ðŸ“¦ **Produits commandÃ©s** avec quantitÃ©s
- ðŸ’° **Total** de la commande
- âœï¸ **Zone de signature**

## ðŸ“¸ Captures d'Ã©cran

### Bon avec classe (vert)
![Bon avec classe](docs/images/bon-avec-classe.png)

### Bon sans classe (orange)
![Bon sans classe](docs/images/bon-sans-classe.png)

### Vue d'impression
![Vue d'impression](docs/images/impression.png)

## ðŸ¤ Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. CrÃ©ez une branche pour votre fonctionnalitÃ© (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### IdÃ©es d'amÃ©liorations

- [ ] Export en PDF directement
- [ ] Statistiques par classe
- [ ] Filtrage par moyen de paiement
- [ ] Support des remises/rÃ©ductions
- [ ] Interface graphique (GUI)
- [ ] Envoi automatique par email

## ðŸ“ Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de dÃ©tails.

## ðŸ‘¥ Auteurs

- **APE Villebarou** - Association de Parents d'Ã‰lÃ¨ves

## ðŸ™ Remerciements

- Toutes les familles qui participent aux ventes APE
- Les bÃ©nÃ©voles qui organisent ces campagnes
- La communautÃ© Python pour les excellents outils

## ðŸ“ž Support

Pour toute question ou problÃ¨me :
- Ouvrez une [issue](https://github.com/votre-username/ape-commandes-vanille/issues)
- Contactez l'APE via [email@ape-villebarou.fr](mailto:email@ape-villebarou.fr)

---

â­ Si ce projet vous a aidÃ©, n'hÃ©sitez pas Ã  lui donner une Ã©toile sur GitHub !

ðŸŒ¿ *Fait avec â¤ï¸ pour faciliter le travail des associations de parents d'Ã©lÃ¨ves*


