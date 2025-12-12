# 🌿 Générateur de Bons de Commande - Vente de Vanille APE

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Script Python pour générer automatiquement des bons de commande imprimables à partir d'un export CSV de commandes de produits vanille (ou tout autre produit).

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Format du CSV](#-format-du-csv)
- [Personnalisation](#-personnalisation)
- [Exemples](#-exemples)
- [Captures d'écran](#-captures-décran)
- [Contribution](#-contribution)
- [Licence](#-licence)

## ✨ Fonctionnalités

- **📊 Analyse automatique** : Détection automatique du fichier CSV et extraction de la période de commandes
- **👥 Regroupement par payeur** : Consolidation de toutes les commandes d'une même famille sur un seul bon
- **🎨 Code couleur visuel** :
  - 🟢 **Vert** : Commandes avec classe assignée (livraison facilitée)
  - 🟠 **Orange** : Commandes sans classe (nécessite vérification)
- **💳 Icônes de paiement** :
  - 💳 Carte bancaire
  - 💵 Espèces
  - 📝 Chèque
  - 🏦 Virement
  - 🅿️ PayPal
  - 💰 Autre
- **🖨️ Optimisé pour l'impression** : Découpe facile avec bordures en pointillés
- **📱 Responsive** : Affichage adapté à tous les écrans
- **🔄 Réutilisable** : Configuration simple pour de futures campagnes de vente

## 🔧 Prérequis

- **Python 3.7+** (aucune dépendance externe requise)
- Un fichier CSV d'export de commandes (format détaillé ci-dessous)

## 📥 Installation

### Option 1 : Clone du repository

```bash
git clone https://github.com/votre-username/ape-commandes-vanille.git
cd ape-commandes-vanille
```

### Option 2 : Téléchargement direct

1. Téléchargez `generer_bons_commande.py`
2. Placez-le dans le dossier de votre choix

## 🚀 Utilisation

### Mode 1 : Auto-détection (recommandé)

Placez votre fichier CSV dans le dossier **Downloads** avec "vanille" dans le nom, puis lancez :

```bash
python generer_bons_commande.py
```

Appuyez sur **Entrée** pour que le script détecte automatiquement le dernier fichier.

### Mode 2 : Avec argument

```bash
python generer_bons_commande.py chemin/vers/votre/fichier.csv
```

### Mode 3 : Saisie manuelle

```bash
python generer_bons_commande.py
# Puis entrez le chemin du fichier CSV lorsque demandé
```

### Résultat

Le script génère un fichier HTML nommé `bons_commande_[nom_du_csv].html` qui s'ouvre automatiquement dans votre navigateur par défaut.

## 📄 Format du CSV

Le fichier CSV doit contenir les colonnes suivantes (séparateur `;`, encodage UTF-8) :

| Colonne | Description | Obligatoire |
|---------|-------------|-------------|
| `Référence commande` | Identifiant unique de la commande | ✅ |
| `Classe de l'enfant` | Classe de l'enfant (ex: CE2 A) | ❌ |
| `Prénom de l'enfant` | Prénom de l'enfant | ✅ |
| `Nom de l'enfant` | Nom de l'enfant | ✅ |
| `Prénom payeur` | Prénom du parent/payeur | ✅ |
| `Nom payeur` | Nom du parent/payeur | ✅ |
| `Email payeur` | Email du payeur | ❌ |
| `n° de téléphone` | Téléphone du payeur | ❌ |
| `Tarif` | Nom du produit commandé | ✅ |
| `Montant tarif` | Prix unitaire (format: `10,00`) | ✅ |
| `Date de la commande` | Date au format `DD/MM/YYYY` | ✅ |
| `Moyen de paiement` | Mode de paiement (ex: "Carte bancaire") | ❌ |

### Exemple de fichier CSV

```csv
Référence commande;Classe de l'enfant;Prénom de l'enfant;Nom de l'enfant;Prénom payeur;Nom payeur;Email payeur;n° de téléphone;Tarif;Montant tarif;Date de la commande;Moyen de paiement
CMD001;CE2 A;Marie;Dupont;Sophie;Dupont;sophie.dupont@email.com;0612345678;12 gousses 14cm;10,00;17/11/2025;Carte bancaire
CMD002;CE2 A;Marie;Dupont;Sophie;Dupont;sophie.dupont@email.com;0612345678;Poudre de vanille 25g;5,00;17/11/2025;Carte bancaire
```

## ⚙️ Personnalisation

Modifiez la section **CONFIGURATION** dans le script (lignes 12-50) :

```python
# Nom du produit
PRODUIT_NOM = "Gousses de Vanille Bourbon de Madagascar"

# Association/Organisation
ORGANISATION = "APE Villebarou"
ORGANISATION_COMPLET = "APE Villebarou • Association de Parents d'Élèves"
```

### Adaptation pour d'autres produits

Ce script est facilement adaptable pour :
- Ventes de chocolats
- Ventes de fromages
- Ventes de calendriers
- Ventes de fleurs
- Tout autre produit vendu par une APE/association

Il suffit de modifier `PRODUIT_NOM` et `ORGANISATION` !

## 📊 Exemples

### Sortie console

```
======================================================================
📊 ANALYSE DU FICHIER CSV
======================================================================
✓ Période détectée : Période du 17/11/2025 au 08/12/2025
✓ 31 payeur(s) avec commandes
✓ Montant total : 1025.00 €
✓ Fichier de sortie : bons_commande_export-vanille.html
======================================================================

======================================================================
✅ BONS DE COMMANDE GÉNÉRÉS
======================================================================

📄 Fichier créé : bons_commande_export-vanille.html
📂 Emplacement : C:\Users\...\Downloads

📊 Récapitulatif :
   • Total de bons : 31
   • Avec classe (vert) : 24
   • Sans classe (orange) : 7
   • Montant total : 1025.00 €
   • Période : Période du 17/11/2025 au 08/12/2025

💡 Ouverture automatique du fichier dans le navigateur...
======================================================================

✓ Fichier ouvert dans le navigateur
```

### Structure d'un bon de commande

Chaque bon contient :
- ✂️ **Marques de découpe** (bordures en pointillés)
- 📋 **Numéro de bon** et badge de statut (avec/sans classe)
- 💳 **Nom du payeur** avec icône de paiement
- 📞 **Coordonnées** (téléphone, email)
- 👨‍👩‍👧‍👦 **Liste des enfants** avec leurs classes
- 📦 **Produits commandés** avec quantités
- 💰 **Total** de la commande
- ✍️ **Zone de signature**

## 📸 Captures d'écran

### Bon avec classe (vert)
![Bon avec classe](docs/images/bon-avec-classe.png)

### Bon sans classe (orange)
![Bon sans classe](docs/images/bon-sans-classe.png)

### Vue d'impression
![Vue d'impression](docs/images/impression.png)

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Idées d'améliorations

- [ ] Export en PDF directement
- [ ] Statistiques par classe
- [ ] Filtrage par moyen de paiement
- [ ] Support des remises/réductions
- [ ] Interface graphique (GUI)
- [ ] Envoi automatique par email

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs

- **APE Villebarou** - Association de Parents d'Élèves

## 🙏 Remerciements

- Toutes les familles qui participent aux ventes APE
- Les bénévoles qui organisent ces campagnes
- La communauté Python pour les excellents outils

## 📞 Support

Pour toute question ou problème :
- Ouvrez une [issue](https://github.com/votre-username/ape-commandes-vanille/issues)
- Contactez l'APE via [email@ape-villebarou.fr](mailto:email@ape-villebarou.fr)

---

⭐ Si ce projet vous a aidé, n'hésitez pas à lui donner une étoile sur GitHub !

🌿 *Fait avec ❤️ pour faciliter le travail des associations de parents d'élèves*
