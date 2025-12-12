#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Graphique pour le Générateur de Bons de Commande
===========================================================

Interface utilisateur graphique (GUI) pour faciliter l'utilisation
du générateur de bons de commande APE.

Auteur: APE Villebarou
Licence: MIT
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import subprocess
import threading
from pathlib import Path

class GenerateurGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🌿 Générateur de Bons de Commande APE")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Variables
        self.csv_file = tk.StringVar()
        self.generate_pdf = tk.BooleanVar(value=False)
        self.pdf_only = tk.BooleanVar(value=False)
        self.auto_open = tk.BooleanVar(value=True)
        
        # Chemin du script principal
        self.script_path = Path(__file__).parent / "generer_bons_commande.py"
        
        self.create_widgets()
        self.check_script_exists()
    
    def create_widgets(self):
        """Créer tous les widgets de l'interface"""
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # === EN-TÊTE ===
        header_frame = tk.Frame(self.root, bg='#4CAF50', height=100)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🌿 Générateur de Bons de Commande",
            font=('Arial', 20, 'bold'),
            bg='#4CAF50',
            fg='white'
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            header_frame,
            text="APE Villebarou - Ventes de Produits",
            font=('Arial', 12),
            bg='#4CAF50',
            fg='white'
        )
        subtitle_label.pack()
        
        # === CONTENU PRINCIPAL ===
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill='both', expand=True)
        
        # Section Fichier CSV
        csv_frame = ttk.LabelFrame(main_frame, text="📁 Fichier CSV", padding="15")
        csv_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Label(csv_frame, text="Sélectionnez le fichier d'export CSV :").pack(anchor='w', pady=(0, 5))
        
        csv_select_frame = ttk.Frame(csv_frame)
        csv_select_frame.pack(fill='x')
        
        self.csv_entry = ttk.Entry(csv_select_frame, textvariable=self.csv_file, width=50)
        self.csv_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        browse_btn = ttk.Button(csv_select_frame, text="📂 Parcourir", command=self.browse_csv)
        browse_btn.pack(side='left')
        
        auto_detect_btn = ttk.Button(csv_select_frame, text="🔍 Auto-détection", command=self.auto_detect_csv)
        auto_detect_btn.pack(side='left', padx=(5, 0))
        
        # Section Options
        options_frame = ttk.LabelFrame(main_frame, text="⚙️ Options de Génération", padding="15")
        options_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Checkbutton(
            options_frame,
            text="📄 Générer aussi un fichier PDF (nécessite weasyprint)",
            variable=self.generate_pdf,
            command=self.update_pdf_options
        ).pack(anchor='w', pady=5)
        
        self.pdf_only_check = ttk.Checkbutton(
            options_frame,
            text="📄 Générer uniquement le PDF (pas de HTML)",
            variable=self.pdf_only,
            state='disabled'
        )
        self.pdf_only_check.pack(anchor='w', pady=5)
        
        ttk.Checkbutton(
            options_frame,
            text="🌐 Ouvrir automatiquement le fichier généré",
            variable=self.auto_open
        ).pack(anchor='w', pady=5)
        
        # Informations
        info_frame = ttk.LabelFrame(main_frame, text="ℹ️ Informations", padding="15")
        info_frame.pack(fill='x', pady=(0, 15))
        
        info_text = """Le générateur va :
• Analyser le fichier CSV d'export
• Regrouper les commandes par payeur
• Générer des bons imprimables avec code couleur
• Afficher les statistiques par classe"""
        
        ttk.Label(info_frame, text=info_text, justify='left').pack(anchor='w')
        
        # Bouton Générer
        generate_btn = tk.Button(
            main_frame,
            text="🚀 GÉNÉRER LES BONS DE COMMANDE",
            command=self.generate,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 14, 'bold'),
            height=2,
            cursor='hand2'
        )
        generate_btn.pack(fill='x', pady=(0, 15))
        
        # Console de sortie
        output_frame = ttk.LabelFrame(main_frame, text="📊 Résultat de la Génération", padding="10")
        output_frame.pack(fill='both', expand=True)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=15,
            wrap='word',
            font=('Consolas', 9)
        )
        self.output_text.pack(fill='both', expand=True)
        
        # Barre de progression
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        
    def check_script_exists(self):
        """Vérifier que le script principal existe"""
        if not self.script_path.exists():
            messagebox.showerror(
                "Erreur",
                f"Le script 'generer_bons_commande.py' est introuvable.\n\n"
                f"Chemin recherché : {self.script_path}\n\n"
                f"Assurez-vous que ce fichier GUI est dans le même dossier que le script principal."
            )
    
    def browse_csv(self):
        """Ouvrir un dialogue pour sélectionner un fichier CSV"""
        filename = filedialog.askopenfilename(
            title="Sélectionner le fichier CSV d'export",
            filetypes=[
                ("Fichiers CSV", "*.csv"),
                ("Tous les fichiers", "*.*")
            ],
            initialdir=os.path.expanduser("~/Downloads")
        )
        if filename:
            self.csv_file.set(filename)
            self.log(f"✓ Fichier sélectionné : {os.path.basename(filename)}")
    
    def auto_detect_csv(self):
        """Auto-détecter le dernier fichier vanille dans Downloads"""
        downloads_dir = os.path.expanduser("~/Downloads")
        
        try:
            csv_files = [
                f for f in os.listdir(downloads_dir)
                if f.lower().endswith(".csv") and "vanille" in f.lower()
            ]
            
            if not csv_files:
                csv_files = [
                    f for f in os.listdir(downloads_dir)
                    if f.startswith("export-") and f.endswith(".csv")
                ]
            
            if csv_files:
                csv_files.sort(reverse=True)
                detected_file = os.path.join(downloads_dir, csv_files[0])
                self.csv_file.set(detected_file)
                self.log(f"✓ Fichier détecté automatiquement : {csv_files[0]}")
                messagebox.showinfo("Fichier détecté", f"Fichier trouvé :\n{csv_files[0]}")
            else:
                messagebox.showwarning(
                    "Aucun fichier trouvé",
                    "Aucun fichier CSV trouvé dans le dossier Téléchargements.\n\n"
                    "Utilisez le bouton 'Parcourir' pour sélectionner manuellement."
                )
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la détection : {e}")
    
    def update_pdf_options(self):
        """Activer/désactiver l'option PDF uniquement"""
        if self.generate_pdf.get():
            self.pdf_only_check.config(state='normal')
        else:
            self.pdf_only.set(False)
            self.pdf_only_check.config(state='disabled')
    
    def log(self, message):
        """Ajouter un message dans la console de sortie"""
        self.output_text.insert('end', message + '\n')
        self.output_text.see('end')
        self.output_text.update()
    
    def clear_log(self):
        """Effacer la console de sortie"""
        self.output_text.delete('1.0', 'end')
    
    def generate(self):
        """Lancer la génération des bons de commande"""
        # Validation
        if not self.csv_file.get():
            messagebox.showwarning(
                "Fichier manquant",
                "Veuillez sélectionner un fichier CSV ou utiliser l'auto-détection."
            )
            return
        
        if not os.path.exists(self.csv_file.get()):
            messagebox.showerror(
                "Fichier introuvable",
                f"Le fichier sélectionné n'existe pas :\n{self.csv_file.get()}"
            )
            return
        
        # Lancer la génération dans un thread séparé
        thread = threading.Thread(target=self._run_generation, daemon=True)
        thread.start()
    
    def _run_generation(self):
        """Exécuter le script de génération (dans un thread)"""
        self.root.after(0, self.clear_log)
        self.root.after(0, self.log, "🚀 Démarrage de la génération...")
        self.root.after(0, self.progress.pack, {'fill': 'x', 'pady': (10, 0)})
        self.root.after(0, self.progress.start)
        
        try:
            # Construire la commande
            cmd = [sys.executable, str(self.script_path), self.csv_file.get()]
            
            if self.generate_pdf.get():
                if self.pdf_only.get():
                    cmd.append('--pdf-only')
                else:
                    cmd.append('--pdf')
            
            # Exécuter le script
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                bufsize=1
            )
            
            # Lire la sortie en temps réel
            for line in process.stdout:
                self.root.after(0, self.log, line.rstrip())
            
            process.wait()
            
            # Vérifier le résultat
            if process.returncode == 0:
                self.root.after(0, self.log, "\n" + "="*60)
                self.root.after(0, self.log, "✅ GÉNÉRATION TERMINÉE AVEC SUCCÈS !")
                self.root.after(0, self.log, "="*60)
                
                self.root.after(0, lambda: messagebox.showinfo("Succès", 
                    "Les bons de commande ont été générés avec succès !\n\n"
                    "Consultez la fenêtre de résultat pour plus de détails."))
            else:
                self.root.after(0, self.log, "\n❌ Erreur lors de la génération")
                self.root.after(0, lambda: messagebox.showerror("Erreur",
                    "Une erreur s'est produite lors de la génération.\n\n"
                    "Consultez la fenêtre de résultat pour plus de détails."))
        
        except Exception as e:
            self.root.after(0, self.log, f"\n❌ Erreur : {e}")
            self.root.after(0, lambda: messagebox.showerror("Erreur", f"Erreur inattendue :\n{e}"))
        
        finally:
            self.root.after(0, self.progress.stop)
            self.root.after(0, self.progress.pack_forget)

def main():
    """Point d'entrée principal"""
    root = tk.Tk()
    app = GenerateurGUI(root)
    
    # Centrer la fenêtre
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()
