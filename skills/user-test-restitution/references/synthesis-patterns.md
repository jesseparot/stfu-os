# Multi-Test Synthesis Restitution Patterns

This file provides patterns and structures for creating synthesis restitutions across multiple user tests.

## Standard Structure

### 1. Executive Summary (Required)
```markdown
# Restitution Tests Utilisateurs - [Nom du projet]
**Date** : [date]
**Nombre de participants** : [N]
**Phase** : [Prototype/Beta/etc.]

## 🎯 Executive Summary

### Verdict global
[2-3 phrases : Le prototype est-il validé, à retravailler, ou à repenser ? Quel est le niveau de confiance ?]

### Insights clés (3-5 maximum)
1. **[Titre insight]** : [Description comportementale factuelle]
2. **[Titre insight]** : [Description avec quantification si possible]
3. **[Titre insight]** : [Description]

### Top 3 blockers critiques
1. **[Blocker]** : [Impact] - [X/N utilisateurs bloqués]
2. **[Blocker]** : [Impact] - [X/N utilisateurs]
3. **[Blocker]** : [Impact] - [X/N utilisateurs]

### Quick Wins
Actions faciles à fort impact :
- [ ] [Action 1] - Impact : [description]
- [ ] [Action 2] - Impact : [description]
- [ ] [Action 3] - Impact : [description]
```

### 2. Methodology (Required, Brief)
```markdown
## 📋 Méthodologie

### Participants
| Profil | Âge | Usage [produit] | Aisance digitale |
|--------|-----|-----------------|------------------|
| [Prénom] | [age] | [fréquence] | ⭐⭐⭐⭐☆ |
| [Prénom] | [age] | [fréquence] | ⭐⭐⭐☆☆ |

**Échantillon** : [Description de la diversité/représentativité]

### Protocole
- **Durée moyenne** : [X] minutes par test
- **Format** : [Présentiel/Distanciel/Hybride]
- **Scénarios testés** : [Liste courte]
- **Périmètre** : [Fonctionnalités/parcours couverts]
```

### 3. Results by Journey/Feature (Required)
```markdown
## 📊 Résultats par parcours

### Parcours 1 : [Nom]
**Objectif utilisateur** : [Description]

#### Métriques
- ✅ **Taux de réussite** : [X/N] utilisateurs ([%])
- ⏱️ **Temps moyen** : [X] min [Y] s
- 🔄 **Retours en arrière** : [X/N] utilisateurs

#### Points de friction majeurs
**1. [Nom du friction point]** - [X/N utilisateurs]
- *Observation* : [Description comportement]
- *Verbatims représentatifs* :
  > "[Citation utilisateur 1]"
  > "[Citation utilisateur 2]"
- *Cause identifiée* : [Analyse]
- *Recommandation* : [Action]

**2. [Autre friction point]** - [X/N utilisateurs]
[Même structure]

#### Ce qui fonctionne
- ✅ [Élément positif] - [X/N utilisateurs satisfaits]
  > "[Verbatim]"

---

### Parcours 2 : [Nom]
[Même structure]
```

### 4. Cross-Cutting Thematic Insights (Required)
```markdown
## 💡 Insights thématiques transverses

### Compréhension / Mental Model
**Constat** : [Observation générale sur X/N utilisateurs]

*Exemples* :
- [Utilisateur A] : [comportement]
- [Utilisateur B] : [comportement différent mais même cause]

**Impact** : [Conséquence sur l'usage]

**Recommandation** : [Action structurante]

---

### Navigation / Architecture d'information
[Même structure]

---

### Valeur perçue
[Même structure]

---

### Émotions / Satisfaction
[Même structure]
```

### 5. Prioritized Recommendations (Required)
```markdown
## 🎯 Recommandations priorisées

### Matrice Impact / Effort

#### 🔴 Critiques (Bloquent l'adoption)
| Recommandation | Parcours affecté | Impact | Effort | Utilisateurs impactés |
|----------------|------------------|--------|--------|-----------------------|
| [Action] | [Parcours] | 🔥🔥🔥 | ⚡⚡ | [X/N] |

#### 🟠 Importantes (Dégradent l'expérience)
| Recommandation | Parcours affecté | Impact | Effort | Utilisateurs impactés |
|----------------|------------------|--------|--------|-----------------------|
| [Action] | [Parcours] | 🔥🔥 | ⚡ | [X/N] |

#### 🟢 Nice-to-have (Améliorations)
| Recommandation | Parcours affecté | Impact | Effort | Utilisateurs impactés |
|----------------|------------------|--------|--------|-----------------------|
| [Action] | [Parcours] | 🔥 | ⚡ | [X/N] |

### Roadmap suggérée
**Sprint 1** (Blockers critiques) :
- [ ] [Action prioritaire 1]
- [ ] [Action prioritaire 2]

**Sprint 2** (Quick wins + importantes) :
- [ ] [Action importante 1]
- [ ] [Quick win]

**Backlog** (Nice-to-have) :
- [ ] [Amélioration future]
```

### 6. Validated/Invalidated Hypotheses (Recommended)
```markdown
## ✅ Hypothèses validées / ❌ Hypothèses invalidées

### Validées
| Hypothèse | Validation | Force |
|-----------|------------|-------|
| [H1] : [Description] | [X/N utilisateurs confirment] | ✅✅✅ |
| [H2] : [Description] | [X/N utilisateurs confirment] | ✅✅ |

### Invalidées
| Hypothèse | Réalité observée | Impact |
|-----------|------------------|--------|
| [H3] : On pensait que... | MAIS les utilisateurs... | 🔴 Revoir le design |

### Nouvelles hypothèses émergentes
- [Nouvelle hypothèse à tester] - Observé chez [X/N] utilisateurs
```

### 7. Annexes (Optional)
```markdown
## 📎 Annexes

### A. Grilles d'observation détaillées
[Lien vers fichiers individuels]

### B. Verbatims complets par utilisateur
[Lien vers fichiers individuels]

### C. Captures d'écran annotées
[Dossier assets]

### D. Métriques brutes
[Tableaux de données si pertinent]
```

---

## Quantification Guidelines

Always quantify when possible:
- **Taux de réussite** : X/N utilisateurs ([%])
- **Patterns comportementaux** : "X utilisateurs sur N..."
- **Verbatims multiples** : Indiquer combien d'utilisateurs ont exprimé l'idée
- **Sévérité** : Blocker critique si > 50% des utilisateurs impactés

## Writing Guidelines

### Executive Summary
- Max 1 page (3-4 paragraphs)
- Business-focused language
- Actionable verdict
- No technical jargon

### Verbatims
- Always include attribution context (when it was said)
- Select representative quotes, not all quotes
- Prefer quotes that reveal mental models over feature feedback

### Recommendations
- Tie to business impact when possible (adoption rate, completion rate, support tickets)
- Separate "must fix" from "nice to have"
- Include effort estimates (qualitative: ⚡ low, ⚡⚡ medium, ⚡⚡⚡ high)

## Adaptation by Context

For early prototypes:
- Emphasize what works (build confidence)
- Highlight blind spots (what wasn't tested)
- Focus on strategic pivots vs minor tweaks

For mature products:
- Compare metrics to previous versions
- Benchmark against competitors
- Quantify ROI of changes
