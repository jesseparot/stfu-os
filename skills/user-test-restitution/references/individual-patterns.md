# Individual Test Restitution Patterns

This file provides patterns and structures for creating restitutions of individual user tests.

## Standard Structure

### 1. Header & Profile (Required)
```markdown
# Test utilisateur - [Prénom] - [Date]

## 📋 Profil
- **Âge** : [age]
- **Profession** : [job]
- **Aisance digitale** : ⭐⭐⭐⭐☆ (1-5)
- **Usage [contexte produit]** : [fréquence d'usage]
- **Contexte du test** : [lieu, moment, ambiance]
```

### 2. Tested Journeys (Required)
For each journey tested:

```markdown
### Parcours [N] : [Nom du parcours]
**Objectif** : [ce qu'on demandait au testeur]

- ✅ **Réussite** : Oui / Partiel / Non
- ⏱️ **Durée** : [X]min [Y]s
- 🧠 **Compréhension spontanée** : [a-t-il compris sans aide ?]

**🔴 Blocages**
- [Point de friction]
  - *Comportement observé* : [description détaillée]
  - *Verbatim* : "[citation exacte]"
  - *Cause hypothétique* : [analyse]

**🟢 Réussites**
- [Ce qui a bien marché]
  - *Verbatim* : "[citation]"

**💡 Comportements inattendus**
- [Ce qu'il/elle a fait différemment]
```

### 3. Key Verbatims (Required)
```markdown
## 🎙️ Verbatims clés

> "[Citation exacte révélant un insight]"
> — Contexte : [quand c'est dit]
```

### 4. Emotions & Reactions (Recommended)
```markdown
## 😊 Émotions / Réactions

- **Frustration** : Sur [écran/fonctionnalité], quand...
- **Surprise positive** : "[verbatim]"
- **Confusion** : Hésitations sur...
```

### 5. Specific Insights (Recommended)
```markdown
## 💎 Insights spécifiques

3-5 observations clés :
- Mental model différent : [description]
- Comparaisons spontanées : [app/service comparé]
- Besoins exprimés : [demandes non anticipées]
```

### 6. Weak Signals (Optional)
```markdown
## 🚨 Signaux faibles

Comportements non verbaux observés :
- [Expression faciale / geste / ton de voix]
- [Hésitations, clics répétés, etc.]
```

### 7. Quick Scoring (Optional)
```markdown
## 📊 Scoring rapide

| Critère | Note /5 | Commentaire |
|---------|---------|-------------|
| Facilité d'usage | ⭐⭐⭐ | [justification] |
| Valeur perçue | ⭐⭐⭐⭐ | [justification] |
| Fluidité | ⭐⭐ | [justification] |
| Désirabilité | ⭐⭐⭐⭐ | [justification] |
```

### 8. Validated/Invalidated Hypotheses (Recommended)
```markdown
## ✅ Validé / ❌ Invalidé

**Hypothèses de conception validées :**
- [H1] : [description hypothèse + validation observée]

**Hypothèses invalidées :**
- [H2] : On pensait que... MAIS [observation contraire]
```

### 9. Immediate Recommendations (Required)
```markdown
## 🔧 Recommandations immédiates

Issues de CE test uniquement :
1. **[Critique]** [Action prioritaire]
2. **[Important]** [Action recommandée]
3. **[Nice-to-have]** [Amélioration optionnelle]
```

### 10. Media References (Optional)
```markdown
## 🎬 Captures / Vidéos

- `[filename].png` - [description du moment]
- `[filename].mp4` (timestamp) - [description]
```

---

## Adaptation Guidelines

### For Early Prototypes
Emphasize:
- What works (validated hypotheses)
- Weak signals (non-verbal behaviors)
- Blind spots (what wasn't tested)

### For Mature Products
Emphasize:
- Comparison with previous version
- Competitive benchmarks
- Quantitative metrics

### For Specific Domains
Add domain-specific sections as needed (see project-types.md for examples).
