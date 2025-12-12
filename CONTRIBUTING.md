# Guide de Contribution

Merci de votre intérêt pour contribuer au projet ! 🎉

## Comment contribuer

### Signaler un bug

1. Vérifiez que le bug n'a pas déjà été signalé dans les [issues](https://github.com/votre-username/ape-commandes-vanille/issues)
2. Ouvrez une nouvelle issue en utilisant le template "Bug Report"
3. Incluez :
   - Description claire du problème
   - Étapes pour reproduire
   - Comportement attendu vs observé
   - Captures d'écran si pertinent
   - Version de Python utilisée

### Proposer une nouvelle fonctionnalité

1. Ouvrez une issue avec le tag "enhancement"
2. Décrivez la fonctionnalité souhaitée
3. Expliquez pourquoi elle serait utile
4. Discutez de l'implémentation avant de coder

### Soumettre une Pull Request

1. **Forkez** le repository
2. **Créez une branche** depuis `main` :
   ```bash
   git checkout -b feature/ma-super-fonctionnalite
   ```
3. **Faites vos modifications** :
   - Suivez le style de code existant
   - Ajoutez des commentaires si nécessaire
   - Testez vos changements
4. **Committez** avec un message clair :
   ```bash
   ```
5. **Poussez** vers votre fork :
   ```bash
   git push origin feature/ma-super-fonctionnalite
   ```
6. **Ouvrez une Pull Request** vers `main`

## Standards de code

### Style Python

- Suivre [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Noms de variables en `snake_case`
- Noms de constantes en `MAJUSCULES`
- Docstrings pour les fonctions

### Messages de commit

Utiliser le format :
- `feat:` pour une nouvelle fonctionnalité
- `fix:` pour une correction de bug
- `docs:` pour la documentation
- `style:` pour le formatage
- `refactor:` pour la refactorisation
- `test:` pour les tests

Exemples :
```
feat: ajout du support des paiements en ligne
fix: correction de l'encodage UTF-8
docs: mise à jour du README avec exemples
```

## Tests

Avant de soumettre :
1. Testez avec différents fichiers CSV
2. Vérifiez l'affichage HTML
3. Testez l'impression
4. Validez sur Windows et macOS si possible

## Questions

N'hésitez pas à poser des questions en ouvrant une issue avec le tag "question".

Merci pour votre contribution ! 🙏
