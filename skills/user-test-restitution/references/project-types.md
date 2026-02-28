# Project Type Adaptations

This file provides domain-specific adaptations for different types of projects and products.

## Usage
When creating a restitution, check if the project matches one of these types. If yes, add the corresponding specialized sections to the standard structure.

---

## Mobile App Testing

### Additional Profile Questions
```markdown
## 📋 Profil
[...standard profile fields...]
- **Device utilisé** : [iPhone/Android] [modèle]
- **Taille d'écran** : [pouces]
- **Habitudes mobiles** : [apps les plus utilisées]
```

### Additional Friction Points to Watch
- Thumb reachability issues
- Text input difficulties
- Gesture confusion (tap vs long press vs swipe)
- Touch target size problems
- Keyboard behavior

### Mobile-Specific Scoring
```markdown
| Critère | Note /5 | Commentaire |
|---------|---------|-------------|
| Accessibilité tactile | ⭐⭐⭐ | Zones difficiles à atteindre |
| Lisibilité | ⭐⭐⭐⭐ | Taille de police OK |
| Réactivité | ⭐⭐⭐ | Lag sur [action] |
```

---

## Conversational / Chat / Voice Interfaces

### Additional Profile Questions
```markdown
## 📋 Profil
[...standard profile fields...]
- **Usage assistants vocaux** : Siri/Alexa/Google/Aucun
- **Aisance conversation écrite** : ⭐⭐⭐⭐☆
- **Attentes interface conversationnelle** : [description]
```

### Conversational-Specific Section
Add after "Résultats par parcours" :

```markdown
## 🗣️ Interaction conversationnelle

### Langage utilisé spontanément
**Formulations naturelles observées** :
- [Utilisateur] : "[phrase exacte tapée/dite]"
- [Utilisateur] : "[autre formulation]"

**Écart avec formulations "système"** :
- Utilisateur dit : "[formulation naturelle]"
- Système attend : "[formulation technique]"
- **Impact** : [compréhension / frustration]

### Compréhension des réponses
**Ton perçu** :
- [X/N] utilisateurs : "Trop formel"
- [X/N] utilisateurs : "Juste bien"
- [X/N] utilisateurs : "Trop familier"

**Longueur des réponses** :
- [X/N] utilisateurs : "Trop verbeux"
- [X/N] utilisateurs : "Juste bien"
- [X/N] utilisateurs : "Trop court / manque de contexte"

**Verbatims représentatifs** :
> "[Citation sur le ton]"
> "[Citation sur la clarté]"

### Confiance dans l'IA
**Comportements de vérification** :
- [X/N] utilisateurs vérifient la réponse ailleurs avant de valider
- [X/N] utilisateurs hésitent à valider une action suggérée
- [X/N] utilisateurs font confiance immédiatement

**Signaux d'anxiété** :
- [Description comportements : hésitation, re-lecture multiple, etc.]

**Verbatims sur la confiance** :
> "[Citation révélant confiance/méfiance]"

### Gestion des erreurs conversationnelles
**Reformulations spontanées** :
- Quand l'IA ne comprend pas, [X/N] utilisateurs reformulent
- [X/N] utilisateurs abandonnent
- [X/N] utilisateurs essaient un autre canal

**Attentes de continuité** :
- [X/N] utilisateurs s'attendent à ce que l'IA se souvienne du contexte
- Verbatim : "[citation sur mémoire conversationnelle]"
```

### Conversational-Specific Recommendations
```markdown
## 🔧 Recommandations spécifiques conversationnel

### Compréhension du langage naturel (NLU)
- [ ] Enrichir les synonymes pour : [liste termes]
- [ ] Gérer les formulations : [exemples]

### Génération de réponse (NLG)
- [ ] Ajuster le ton : [direction]
- [ ] Raccourcir/Allonger les réponses sur : [contextes]

### Gestion d'erreur
- [ ] Améliorer la reformulation quand incompréhension
- [ ] Suggérer des alternatives quand échec
```

---

## Banking / Financial Services

### Additional Profile Questions
```markdown
## 📋 Profil
[...standard profile fields...]
- **Usage banque en ligne** : quotidien / hebdo / mensuel / rare
- **Services utilisés** : [virements, consultation, épargne, etc.]
- **Niveau d'aisance financière** : ⭐⭐⭐⭐☆
```

### Banking-Specific Section
```markdown
## 💳 Spécificités bancaires

### Compréhension du jargon
**Termes mal compris** :
- "[Terme technique]" → [X/N] utilisateurs ne comprennent pas
  > Verbatim : "[citation]"

**Préférences de formulation** :
- Préfèrent : "[formulation grand public]"
- Au lieu de : "[jargon bancaire]"

### Perception de sécurité
**Signaux de confiance** :
- [X/N] utilisateurs vérifient les icônes de sécurité
- [X/N] utilisateurs hésitent sur validation finale
- [X/N] utilisateurs expriment des préoccupations de sécurité
  > Verbatim : "[citation sur sécurité]"

**Attentes de confirmation** :
- [X/N] utilisateurs s'attendent à une confirmation [email/SMS/push]
- [X/N] utilisateurs voudraient pouvoir annuler après validation

### Gestion des montants
**Saisie des montants** :
- Préfèrent : [clavier numérique / texte / slider]
- Erreurs observées : [description]

**Vérification des montants** :
- [X/N] utilisateurs vérifient plusieurs fois avant validation
- Comportement : [description hésitations]
```

---

## E-commerce / Marketplace

### E-commerce-Specific Section
```markdown
## 🛒 Parcours d'achat

### Découverte produit
**Navigation** :
- [X/N] utilisateurs trouvent le produit via [méthode]
- Points de friction : [description]

**Filtres / Recherche** :
- Filtres utilisés : [liste]
- Filtres manquants demandés : [liste]

### Décision d'achat
**Éléments consultés avant achat** :
- [X/N] consultent les avis clients
- [X/N] comparent avec d'autres produits
- [X/N] vérifient les frais de livraison

**Freins à l'achat** :
- [Description hésitations observées]
- Verbatims : "[citations]"

### Tunnel de conversion
**Points d'abandon** :
- [X/N] abandonnent à l'étape : [nom étape]
- Raison : [description]

**Temps de complétion** :
- De l'ajout au panier à la validation : [X] min
- Points de ralentissement : [description]
```

---

## SaaS / B2B Tools

### B2B-Specific Section
```markdown
## 💼 Adoption et usage professionnel

### Intégration dans le workflow
**Usage projeté** :
- [X/N] utilisateurs l'intégreraient dans leur routine quotidienne
- [X/N] l'utiliseraient occasionnellement
- [X/N] ne voient pas de cas d'usage clair

**Comparaison avec outils actuels** :
- Outils actuellement utilisés : [liste]
- Avantages perçus vs outil actuel : [description]
- Manques par rapport à l'outil actuel : [description]

### Valeur business perçue
**ROI attendu** :
- Gain de temps estimé : [description]
- Amélioration de qualité : [description]
- Réduction d'erreurs : [description]

**Verbatims sur la valeur** :
> "[Citation sur l'utilité business]"

### Adoption team
**Barrières à l'adoption** :
- [X/N] pensent que leurs collègues auraient du mal avec [aspect]
- Formation nécessaire : [description]

**Champions potentiels** :
- [X/N] seraient prêts à évangéliser l'outil en interne
```

---

## Accessibility Testing

### Accessibility-Specific Section
```markdown
## ♿ Accessibilité

### Profil accessibilité
- **Type de handicap testé** : [visuel/moteur/auditif/cognitif]
- **Technologies assistives utilisées** : [lecteur d'écran/navigation clavier/etc.]
- **Niveau d'expertise** : [débutant/intermédiaire/expert]

### Résultats accessibilité
**Parcours réussis avec technologie assistive** :
- ✅ [Parcours A] : [X/N] utilisateurs
- ❌ [Parcours B] : [X/N] utilisateurs bloqués

**Blockers spécifiques** :
- [Description blocker] - Norme WCAG : [critère]
- [Description blocker] - Norme WCAG : [critère]

**Verbatims** :
> "[Citation sur expérience accessibilité]"

### Recommandations WCAG
| Critère WCAG | Niveau | Parcours | Action |
|--------------|--------|----------|--------|
| [1.4.3 Contraste] | AA | [Parcours] | [Action corrective] |
| [2.1.1 Clavier] | A | [Parcours] | [Action corrective] |
```

---

## Usage Notes

1. **Don't add all sections**: Only include sections relevant to the specific project type being tested
2. **Combine as needed**: A mobile banking app would combine "Mobile App" + "Banking" sections
3. **Adapt language**: Use the terminology natural to the domain (e.g., "patient" for healthcare, "user" for SaaS)
4. **Custom sections**: If the project doesn't fit these types, create custom sections following the same pattern
