#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de Bons de Commande pour Ventes de Vanille
======================================================

Script pour générer automatiquement des bons de commande imprimables
à partir d'un export CSV de commandes de produits vanille.

Auteur: APE Villebarou
Licence: MIT
"""

import csv
from collections import defaultdict
from datetime import datetime
import os
import sys
import webbrowser
import argparse

# ============================================================================
# CONFIGURATION - Modifier ces paramètres selon vos besoins
# ============================================================================

# Parser d'arguments
parser = argparse.ArgumentParser(description='Générateur de bons de commande pour ventes APE')
parser.add_argument('csv_file', nargs='?', help='Chemin du fichier CSV d\'export')
parser.add_argument('--pdf', action='store_true', help='Générer aussi un fichier PDF')
parser.add_argument('--pdf-only', action='store_true', help='Générer uniquement le PDF (pas de HTML)')
args = parser.parse_args()

# Fichier CSV d'entrée
if args.csv_file:
    csv_file = args.csv_file
else:
    # Par défaut, demander le fichier
    csv_file = input("Chemin du fichier CSV d'export (ou Entrée pour utiliser le dernier fichier vanille du dossier Downloads) : ").strip()
    
    if not csv_file:
        # Chercher le dernier fichier CSV contenant "vanille" dans Downloads
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        csv_files = [f for f in os.listdir(downloads_dir) 
                     if f.lower().endswith(".csv") and "vanille" in f.lower()]
        
        if not csv_files:
            # Sinon chercher les fichiers commençant par "export-"
            csv_files = [f for f in os.listdir(downloads_dir) 
                        if f.startswith("export-") and f.endswith(".csv")]
        
        if csv_files:
            csv_files.sort(reverse=True)  # Trier par nom (date dans le nom)
            csv_file = os.path.join(downloads_dir, csv_files[0])
            print(f"✓ Fichier détecté : {csv_files[0]}")
        else:
            print("❌ Aucun fichier d'export trouvé dans Downloads")
            sys.exit(1)

# Vérifier que le fichier existe
if not os.path.exists(csv_file):
    print(f"❌ Erreur : Le fichier '{csv_file}' n'existe pas")
    sys.exit(1)

# Nom du produit (peut être personnalisé)
PRODUIT_NOM = "Gousses de Vanille Bourbon de Madagascar"

# Association/Organisation
ORGANISATION = "APE Villebarou"
ORGANISATION_COMPLET = "APE Villebarou • Association de Parents d'Élèves"

# ============================================================================
# TRAITEMENT DES DONNÉES
# ============================================================================

# Dictionnaire pour stocker les commandes regroupées par payeur
commandes_par_payeur = defaultdict(lambda: {
    'nom_complet': '',
    'telephone': '',
    'email': '',
    'enfants': {},  # enfants avec leurs classes
    'produits': defaultdict(int),
    'total': 0,
    'avec_classe': False,
    'moyen_paiement': ''
})

# Variables pour les statistiques et dates
dates_commandes = []

print("\n" + "=" * 70)
print("📊 ANALYSE DU FICHIER CSV")
print("=" * 70)

# Lecture du fichier CSV
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';')
    
    for row in reader:
        row = {k.strip(): v for k, v in row.items()}
        
        ref_commande = row['Référence commande'].strip()
        classe = row["Classe de l'enfant"].strip()
        prenom_enfant = row["Prénom de l'enfant"].strip()
        nom_enfant = row["Nom de l'enfant"].strip()
        prenom_payeur = row['Prénom payeur'].strip()
        nom_payeur = row['Nom payeur'].strip()
        tarif = row['Tarif'].strip()
        montant_str = row['Montant tarif'].strip()
        date_commande = row['Date de la commande'].strip()
        moyen_paiement = row['Moyen de paiement'].strip()
        
        # Collecter les dates pour déterminer la période
        if date_commande:
            try:
                date_obj = datetime.strptime(date_commande.split()[0], '%d/%m/%Y')
                dates_commandes.append(date_obj)
            except:
                pass
        
        # Créer une clé unique pour le payeur
        payeur_key = f"{prenom_payeur} {nom_payeur}".strip()
        if not payeur_key:
            payeur_key = row['Email payeur'].strip()
        
        # Initialiser les infos du payeur
        if not commandes_par_payeur[payeur_key]['nom_complet']:
            commandes_par_payeur[payeur_key]['nom_complet'] = payeur_key
            commandes_par_payeur[payeur_key]['telephone'] = row['n° de téléphone'].strip()
            commandes_par_payeur[payeur_key]['email'] = row['Email payeur'].strip()
            commandes_par_payeur[payeur_key]['moyen_paiement'] = moyen_paiement
        
        # Ajouter l'enfant et sa classe
        if prenom_enfant or nom_enfant:
            nom_enfant_complet = f"{prenom_enfant} {nom_enfant}".strip()
            if nom_enfant_complet:
                commandes_par_payeur[payeur_key]['enfants'][nom_enfant_complet] = classe if classe else "Sans classe"
        
        # Vérifier si le payeur a au moins une commande avec classe
        if classe:
            commandes_par_payeur[payeur_key]['avec_classe'] = True
        
        # Ajouter les produits
        if montant_str and montant_str != '0,00':
            montant = float(montant_str.replace(',', '.'))
            if montant > 0:
                commandes_par_payeur[payeur_key]['produits'][tarif] += 1
                commandes_par_payeur[payeur_key]['total'] += montant

# Filtrer les payeurs sans produits
commandes_finales = {k: v for k, v in commandes_par_payeur.items() if v['produits']}

# Déterminer la période des commandes
if dates_commandes:
    date_debut = min(dates_commandes)
    date_fin = max(dates_commandes)
    periode_text = f"Période du {date_debut.strftime('%d/%m/%Y')} au {date_fin.strftime('%d/%m/%Y')}"
    print(f"✓ Période détectée : {periode_text}")
else:
    periode_text = f"Année {datetime.now().year}"
    print(f"⚠ Période non détectée, utilisation par défaut : {periode_text}")

# Afficher les statistiques
print(f"✓ {len(commandes_finales)} payeur(s) avec commandes")
total_montant = sum(info['total'] for info in commandes_finales.values())
print(f"✓ Montant total : {total_montant:.2f} €")

# Générer le nom du fichier de sortie
base_name = os.path.splitext(os.path.basename(csv_file))[0]
output_dir = os.path.dirname(csv_file)
if not output_dir:
    output_dir = os.path.join(os.path.expanduser("~"), "Downloads")

output_file = os.path.join(output_dir, f"bons_commande_{base_name}.html")
print(f"✓ Fichier de sortie : {os.path.basename(output_file)}")
print("=" * 70 + "\n")

# ============================================================================
# GÉNÉRATION DU FICHIER HTML
# ============================================================================

# Créer le contenu HTML (sans f-string pour le CSS)
html_header = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bons de Commande - {PRODUIT_NOM}</title>
    <style>
"""

html_css = """        @media print {
            .bon-commande {
                page-break-inside: avoid;
                page-break-after: always;
            }
            .no-print {
                display: none;
            }
        }
        
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        .no-print {
            text-align: center;
            margin-bottom: 20px;
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .no-print button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin: 5px;
        }
        
        .no-print button:hover {
            background-color: #45a049;
        }
        
        .bon-commande {
            background: white;
            border: 3px dashed #333;
            border-radius: 10px;
            padding: 25px;
            margin: 20px auto;
            max-width: 800px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            position: relative;
        }
        
        .bon-commande.avec-classe {
            border-color: #4CAF50;
        }
        
        .bon-commande.sans-classe {
            border-color: #FF9800;
            background-color: #FFFBF5;
        }
        
        .header {
            text-align: center;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }
        
        .bon-commande.sans-classe .header {
            border-bottom-color: #FF9800;
        }
        
        .header h1 {
            color: #4CAF50;
            margin: 0 0 5px 0;
            font-size: 24px;
        }
        
        .bon-commande.sans-classe .header h1 {
            color: #FF9800;
        }
        
        .header h2 {
            color: #666;
            margin: 5px 0;
            font-size: 18px;
            font-weight: normal;
        }
        
        .badge-statut {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: bold;
            margin-left: 10px;
        }
        
        .badge-avec-classe {
            background-color: #4CAF50;
            color: white;
        }
        
        .badge-sans-classe {
            background-color: #FF9800;
            color: white;
        }
        
        .payeur-nom {
            font-size: 24px;
            font-weight: bold;
            color: white;
            margin: 15px 0;
            text-align: center;
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            padding: 15px;
            border-radius: 8px;
        }
        
        .bon-commande.sans-classe .payeur-nom {
            background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        }
        
        .info-section {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 2px solid #e0e0e0;
        }
        
        .bon-commande.sans-classe .info-section {
            background-color: #FFF3E0;
            border-color: #FFE0B2;
        }
        
        .info-row {
            display: flex;
            margin: 8px 0;
            align-items: center;
        }
        
        .info-label {
            font-weight: bold;
            color: #333;
            min-width: 140px;
        }
        
        .info-value {
            color: #666;
        }
        
        .warning-badge {
            background-color: #ff5252;
            color: white;
            padding: 8px 12px;
            border-radius: 5px;
            display: inline-block;
            margin: 10px 0;
            font-size: 13px;
            font-weight: bold;
        }
        
        .enfants-section {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 5px solid #4CAF50;
        }
        
        .bon-commande.sans-classe .enfants-section {
            border-left-color: #FF9800;
        }
        
        .enfants-section h3 {
            color: #4CAF50;
            margin-top: 0;
            margin-bottom: 10px;
        }
        
        .bon-commande.sans-classe .enfants-section h3 {
            color: #FF9800;
        }
        
        .enfant-item {
            padding: 8px;
            margin: 5px 0;
            background: white;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
        }
        
        .enfant-nom {
            font-weight: bold;
            color: #333;
        }
        
        .enfant-classe {
            color: #666;
            font-style: italic;
        }
        
        .enfant-classe.sans-classe-text {
            color: #FF5722;
            font-weight: bold;
        }
        
        .produits-section {
            margin: 20px 0;
        }
        
        .produits-section h3 {
            color: #4CAF50;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 8px;
            margin-bottom: 15px;
        }
        
        .bon-commande.sans-classe .produits-section h3 {
            color: #FF9800;
            border-bottom-color: #FF9800;
        }
        
        .produit-item {
            background-color: #fff;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding: 12px 15px;
            margin: 10px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .produit-item:hover {
            border-color: #4CAF50;
            box-shadow: 0 2px 5px rgba(76, 175, 80, 0.2);
        }
        
        .bon-commande.sans-classe .produit-item:hover {
            border-color: #FF9800;
            box-shadow: 0 2px 5px rgba(255, 152, 0, 0.2);
        }
        
        .produit-quantite {
            background-color: #4CAF50;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 16px;
        }
        
        .bon-commande.sans-classe .produit-quantite {
            background-color: #FF9800;
        }
        
        .produit-nom {
            flex-grow: 1;
            margin: 0 15px;
            font-size: 16px;
            color: #333;
        }
        
        .footer {
            margin-top: 25px;
            padding-top: 15px;
            border-top: 2px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .total {
            font-size: 22px;
            font-weight: bold;
            color: #4CAF50;
        }
        
        .bon-commande.sans-classe .total {
            color: #FF9800;
        }
        
        .total-label {
            color: #666;
            margin-right: 10px;
        }
        
        .signature-box {
            border: 2px dashed #ccc;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            color: #999;
            font-size: 12px;
            min-width: 200px;
        }
        
        .scissors {
            position: absolute;
            right: -15px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 30px;
            color: #999;
        }
        
        .ape-logo {
            text-align: center;
            color: #999;
            font-size: 12px;
            margin-top: 15px;
        }
"""

html_body_start = f"""    </style>
</head>
<body>
    <div class="no-print">
        <h2>📋 Bons de Commande - {PRODUIT_NOM}</h2>
        <p>{ORGANISATION} - {periode_text}</p>
        <button onclick="window.print()">🖨️ Imprimer tous les bons</button>
    </div>
"""

html_content = html_header + html_css + html_body_start

bon_numero = 1
nb_avec_classe = 0
nb_sans_classe = 0

# Fonction pour déterminer l'icône de paiement
def get_icone_paiement(moyen):
    """
    Retourne l'emoji approprié selon le moyen de paiement.
    
    Args:
        moyen (str): Le moyen de paiement (ex: "Carte bancaire", "Espèces", "Chèque")
    
    Returns:
        str: L'emoji correspondant au moyen de paiement
    """
    moyen_lower = moyen.lower()
    if 'carte' in moyen_lower or 'bancaire' in moyen_lower or 'cb' in moyen_lower:
        return '💳'
    elif 'espèce' in moyen_lower or 'liquide' in moyen_lower or 'cash' in moyen_lower:
        return '💵'
    elif 'chèque' in moyen_lower or 'cheque' in moyen_lower:
        return '📝'
    elif 'virement' in moyen_lower:
        return '🏦'
    elif 'paypal' in moyen_lower:
        return '🅿️'
    else:
        return '💰'

for payeur, info in sorted(commandes_finales.items()):
    classe_css = "avec-classe" if info['avec_classe'] else "sans-classe"
    badge_text = "✓ AVEC CLASSE" if info['avec_classe'] else "⚠ SANS CLASSE"
    badge_css = "badge-avec-classe" if info['avec_classe'] else "badge-sans-classe"
    
    if info['avec_classe']:
        nb_avec_classe += 1
    else:
        nb_sans_classe += 1
    
    # Déterminer l'icône de paiement
    icone_paiement = get_icone_paiement(info['moyen_paiement'])
    
    html_content += f"""
    <div class="bon-commande {classe_css}">
        <div class="scissors">✂️</div>
        <div class="header">
            <h1>🌿 BON DE COMMANDE N°{bon_numero:03d} <span class="{badge_css} badge-statut">{badge_text}</span></h1>
            <h2>{PRODUIT_NOM}</h2>
        </div>
        
        <div class="payeur-nom">{icone_paiement} {info['nom_complet']}</div>
"""
    
    if not info['avec_classe']:
        html_content += """
        <div class="warning-badge">⚠️ Attention : Vérifier la classe avant livraison</div>
"""
    
    html_content += """
        <div class="info-section">
"""
    
    if info['moyen_paiement']:
        html_content += f"""
            <div class="info-row">
                <span class="info-label">{icone_paiement} Paiement :</span>
                <span class="info-value">{info['moyen_paiement']}</span>
            </div>
"""
    
    if info['telephone']:
        html_content += f"""
            <div class="info-row">
                <span class="info-label">📞 Téléphone :</span>
                <span class="info-value">{info['telephone']}</span>
            </div>
"""
    
    if info['email']:
        html_content += f"""
            <div class="info-row">
                <span class="info-label">📧 Email :</span>
                <span class="info-value">{info['email']}</span>
            </div>
"""
    
    html_content += """
        </div>
"""
    
    # Afficher les enfants et leurs classes
    if info['enfants']:
        html_content += """
        <div class="enfants-section">
            <h3>👨‍👩‍👧‍👦 Enfant(s) concerné(s) :</h3>
"""
        for enfant, classe in sorted(info['enfants'].items()):
            classe_css_text = "sans-classe-text" if classe == "Sans classe" else ""
            html_content += f"""
            <div class="enfant-item">
                <span class="enfant-nom">{enfant}</span>
                <span class="enfant-classe {classe_css_text}">{classe}</span>
            </div>
"""
        html_content += """
        </div>
"""
    
    html_content += """
        <div class="produits-section">
            <h3>📦 PRODUITS COMMANDÉS</h3>
"""
    
    for produit, quantite in sorted(info['produits'].items()):
        html_content += f"""
            <div class="produit-item">
                <span class="produit-quantite">{quantite}x</span>
                <span class="produit-nom">{produit}</span>
            </div>
"""
    
    html_content += f"""
        </div>
        
        <div class="footer">
            <div class="total">
                <span class="total-label">TOTAL :</span>
                <span>{info['total']:.2f} €</span>
            </div>
            <div class="signature-box">
                Signature / Date<br>
                <br>
                <br>
            </div>
        </div>
        
        <div class="ape-logo">
            {ORGANISATION_COMPLET}
        </div>
    </div>
"""
    bon_numero += 1

html_content += f"""
    <div class="no-print" style="margin-top: 30px; text-align: center; background: white; padding: 20px; border-radius: 8px;">
        <h3>📊 Récapitulatif</h3>
        <p><strong>Total : {bon_numero - 1} bon(s) de commande</strong></p>
        <p>✅ Avec classe : {nb_avec_classe} | ⚠️ Sans classe : {nb_sans_classe}</p>
        <p>💰 Montant total : {total_montant:.2f} €</p>
        <button onclick="window.print()">🖨️ Imprimer tous les bons</button>
    </div>
</body>
</html>
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("=" * 70)
print("✅ BONS DE COMMANDE GÉNÉRÉS")
print("=" * 70)
print(f"\n📄 Fichier HTML créé : {os.path.basename(output_file)}")
print(f"📂 Emplacement : {output_dir}")
print(f"\n📊 Récapitulatif :")
print(f"   • Total de bons : {bon_numero - 1}")
print(f"   • Avec classe (vert) : {nb_avec_classe}")
print(f"   • Sans classe (orange) : {nb_sans_classe}")
print(f"   • Montant total : {total_montant:.2f} €")
print(f"   • Période : {periode_text}")

# ============================================================================
# GÉNÉRATION DU PDF (si demandé)
# ============================================================================

pdf_file = None
if args.pdf or args.pdf_only:
    print("\n" + "=" * 70)
    print("� GÉNÉRATION DU PDF")
    print("=" * 70)
    
    try:
        from weasyprint import HTML, CSS
        
        pdf_file = os.path.join(output_dir, f"bons_commande_{base_name}.pdf")
        
        # CSS spécifique pour le PDF (optimisation impression)
        pdf_css = CSS(string="""
            @page {
                size: A4;
                margin: 1cm;
            }
            .bon-commande {
                page-break-after: always;
                page-break-inside: avoid;
            }
            .no-print {
                display: none;
            }
        """)
        
        # Générer le PDF depuis le HTML
        print("⏳ Conversion HTML → PDF en cours...")
        HTML(string=html_content).write_pdf(pdf_file, stylesheets=[pdf_css])
        
        print(f"✓ Fichier PDF créé : {os.path.basename(pdf_file)}")
        print(f"📂 Emplacement : {output_dir}")
        
    except ImportError:
        print("\n⚠️  ERREUR : La bibliothèque 'weasyprint' n'est pas installée")
        print("\n💡 Pour installer weasyprint, exécutez :")
        print("   pip install weasyprint")
        print("\n📝 Note : weasyprint nécessite aussi GTK+ sur Windows")
        print("   Téléchargez-le depuis : https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases")
        print("\n   Alternative simple : utilisez l'impression PDF de votre navigateur")
        pdf_file = None
    except Exception as e:
        print(f"\n❌ Erreur lors de la génération du PDF : {e}")
        print("💡 Vous pouvez utiliser l'impression PDF de votre navigateur à la place")
        pdf_file = None

print("\n" + "=" * 70)

# Ouvrir automatiquement le fichier
if not args.pdf_only:
    print("💡 Ouverture du fichier HTML dans le navigateur...")
    try:
        webbrowser.open(output_file)
        print("✓ Fichier HTML ouvert dans le navigateur")
    except:
        print("⚠ Impossible d'ouvrir automatiquement le fichier")
        print(f"   Ouvrez manuellement : {output_file}")
elif pdf_file:
    print("💡 Ouverture du fichier PDF...")
    try:
        webbrowser.open(pdf_file)
        print("✓ Fichier PDF ouvert")
    except:
        print("⚠ Impossible d'ouvrir automatiquement le fichier")
        print(f"   Ouvrez manuellement : {pdf_file}")

print("=" * 70)
print("\n✨ Génération terminée avec succès !")
if not args.pdf_only:
    print(f"📄 HTML : {output_file}")
if pdf_file:
    print(f"📄 PDF  : {pdf_file}")
print()
