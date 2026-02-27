---
name: user-test-restitution
description: Crée des documents de restitution de tests utilisateurs professionnels à partir de notes d'analyse. Utiliser quand l'utilisateur demande de créer, rédiger ou générer une restitution/rapport/synthèse de tests utilisateurs, tests d'utilisabilité ou de recherche UX. Supporte les restitutions individuelles (un seul utilisateur) et les synthèses (plusieurs utilisateurs). Gère différents types de projets (apps mobiles, interfaces conversationnelles, bancaire, e-commerce, SaaS, tests d'accessibilité). Utiliser quand l'utilisateur a des données de test (fichiers d'analyse, notes, observations) et a besoin d'un livrable structuré.
---

# Restitution de tests utilisateurs

Crée des documents de restitution professionnels et structurés à partir de données de tests utilisateurs.

## Vue d'ensemble

Ce skill génère deux types de documents de restitution :
1. **Restitution individuelle** : Analyse détaillée d'un seul test utilisateur
2. **Restitution synthèse** : Insights transversaux issus de plusieurs tests

Les deux suivent les bonnes pratiques de recherche UX et sont adaptables à différents types de projets (mobile, web, conversationnel, bancaire, etc.).

## Arbre de décision

```
Demande utilisateur
    │
    ├─ "Crée une restitution pour [un utilisateur]"
    │   → Workflow Restitution Individuelle
    │
    ├─ "Crée une synthèse de [plusieurs utilisateurs]"
    │   → Workflow Restitution Synthèse
    │
    └─ "J'ai besoin d'un template pour les tests utilisateurs"
        → Fournir le template vierge (voir section Templates)
```

## Workflow Restitution Individuelle

Utiliser quand l'utilisateur veut analyser un seul test utilisateur.

### Étape 1 : Collecter les données d'entrée

Lire les matériaux sources fournis :
- Fichier d'analyse (si existant) : observations détaillées
- Notes brutes : notes non structurées de la session de test
- Contexte additionnel : brief projet, protocole de test, etc.

**Poser des questions de clarification si nécessaire :**
- Type de projet ? (app mobile, web, conversationnel, bancaire, etc.)
- Phase de test ? (prototype early, beta, produit mature)
- Axes de focus spécifiques ? (accessibilité, IA conversationnelle, etc.)

### Étape 2 : Déterminer les adaptations par type de projet

Consulter [references/project-types.md](references/project-types.md) pour les sections spécifiques au domaine à ajouter :
- Apps mobiles : ajouter les observations touch/gestes
- Interfaces conversationnelles : ajouter l'analyse NLU/NLG
- Bancaire : ajouter la perception de sécurité, compréhension du jargon
- E-commerce : ajouter l'analyse du funnel de conversion
- SaaS/B2B : ajouter les barrières à l'adoption
- Accessibilité : ajouter la conformité WCAG

**N'ajouter que les sections pertinentes** — ne pas inclure toutes les adaptations pour chaque projet.

### Étape 3 : Structurer le document

Suivre la structure standard de [references/individual-patterns.md](references/individual-patterns.md) :

**Sections obligatoires :**
1. En-tête & Profil
2. Parcours testés (résultats par parcours)
3. Verbatims clés
4. Recommandations immédiates

**Sections recommandées :**
5. Émotions & Réactions
6. Insights spécifiques
7. Hypothèses validées/invalidées

**Sections optionnelles :**
8. Signaux faibles (comportements non-verbaux)
9. Scoring rapide
10. Références média

### Étape 4 : Rédiger avec les bonnes pratiques

**Quantifier quand c'est possible :**
- "Complété en 3min 12s" (pas "rapidement")
- "A hésité 8 secondes avant de cliquer" (pas "a hésité")

**Utiliser des verbatims directs :**
- Inclure les citations exactes dans la langue de l'utilisateur
- Fournir le contexte du moment où c'a été dit
- Sélectionner les citations qui révèlent les modèles mentaux

**Prioriser les recommandations :**
- **[Critique]** : Bloque l'usage
- **[Important]** : Dégrade l'expérience
- **[Nice-to-have]** : Amélioration mineure

**Convention de nommage :**
Suivre les conventions STFU dans jesse-os :
- Brouillon : `YYYY-MM-DD-test-[prenom]_draft.md`
- Final : `YYYY-MM-DD-test-[prenom]_final.md`

### Étape 5 : Sauvegarder et itérer

Sauvegarder à l'emplacement approprié (demander à l'utilisateur si c'est pas clair).

Proposer :
> "Restitution créée. Souhaites-tu que j'ajuste le ton, que j'ajoute du détail à certaines sections, ou que je crée une synthèse à travers plusieurs tests ?"

---

## Workflow Restitution Synthèse

Utiliser quand l'utilisateur veut synthétiser les insights de plusieurs tests utilisateurs.

### Étape 1 : Collecter les données d'entrée

Lire tous les matériaux sources :
- Fichiers d'analyse individuels (s'ils existent)
- Notes brutes de plusieurs sessions de test
- Contexte projet et protocole de test

**Requis :** Au moins 3 utilisateurs pour créer une synthèse significative.

### Étape 2 : Identifier le contexte projet

Demander si ce n'est pas clair :
- Type et phase du projet
- Nombre de participants
- Hypothèses clés testées
- Axes de focus spécifiques

Consulter [references/project-types.md](references/project-types.md) pour les adaptations par domaine.

### Étape 3 : Structurer le document

Suivre [references/synthesis-patterns.md](references/synthesis-patterns.md) :

**Sections obligatoires :**
1. **Résumé exécutif** (1 page max)
   - Verdict global
   - 3-5 insights clés
   - Top 3 bloqueurs critiques
   - Quick wins
2. **Méthodologie** (bref)
3. **Résultats par parcours/fonctionnalité**
   - Taux de réussite (X/N utilisateurs)
   - Points de friction avec nombre d'utilisateurs
   - Ce qui fonctionne
4. **Insights thématiques** (transversaux)
   - Compréhension/modèles mentaux
   - Navigation
   - Valeur perçue
   - Émotions
5. **Recommandations priorisées**
   - Matrice impact/effort
   - Roadmap suggérée

**Sections recommandées :**
6. Hypothèses validées/invalidées

**Sections optionnelles :**
7. Annexes (liens vers les fichiers individuels)

### Étape 4 : Agréger les données

**Compter les patterns à travers les utilisateurs :**
- "3/5 utilisateurs bloqués sur [fonctionnalité]"
- "4/5 utilisateurs ont apprécié [élément]"

**Sélectionner des verbatims représentatifs :**
- Choisir les citations qui reflètent les expériences partagées
- Inclure l'attribution (quel utilisateur l'a dit)

**Quantifier l'impact :**
- Taux de réussite : pourcentage + nombre d'utilisateurs
- Métriques temporelles : moyenne + fourchette
- Sévérité : > 50% impactés = bloqueur critique

### Étape 5 : Prioriser les recommandations

Utiliser la matrice Impact/Effort :

| Priorité | Critères | Notation |
|----------|----------|----------|
| 🔴 Critique | Bloque l'adoption + >50% utilisateurs | Impact : 🔥🔥🔥 |
| 🟠 Important | Dégrade l'expérience | Impact : 🔥🔥 |
| 🟢 Nice-to-have | Amélioration mineure | Impact : 🔥 |

**Estimation d'effort :**
- ⚡ Faible : Fix rapide, pas de changement d'architecture
- ⚡⚡ Moyen : Développement modéré
- ⚡⚡⚡ Élevé : Refonte majeure ou nouveau système

### Étape 6 : Créer la roadmap

Suggérer une implémentation par sprint :

```markdown
**Sprint 1** (Bloqueurs critiques) :
- [ ] [Action 1]
- [ ] [Action 2]

**Sprint 2** (Quick wins + Important) :
- [ ] [Quick win]
- [ ] [Amélioration importante]

**Backlog** (Nice-to-have) :
- [ ] [Amélioration future]
```

### Étape 7 : Sauvegarder et itérer

**Convention de nommage (STFU) :**
- Brouillon : `YYYY-MM-DD-restitution-[projet]_draft.md`
- Final : `YYYY-MM-DD-restitution-[projet]_final.md`

Proposer des suites :
> "Synthèse créée. Souhaites-tu que je crée un résumé en slides, que j'approfondisse certaines sections, ou que je génère des templates pour le prochain round de tests ?"

---

## Templates

Fournir des templates vierges quand demandé.

### Template test individuel
Situé dans : [assets/template-individual.md](assets/template-individual.md)

Utiliser quand l'utilisateur demande :
- "Donne-moi un template pour un test utilisateur individuel"
- "J'ai besoin d'une structure pour mon prochain test"

### Template synthèse
Situé dans : [assets/template-synthesis.md](assets/template-synthesis.md)

Utiliser quand l'utilisateur demande :
- "Donne-moi un template pour une synthèse multi-utilisateurs"
- "J'ai besoin d'une structure de restitution"

### Exemple : Bancaire conversationnel
Situé dans : [assets/example-banking-conversational.md](assets/example-banking-conversational.md)

Utiliser comme référence pour montrer :
- Structure de synthèse complète
- Adaptations spécifiques au domaine (conversationnel + bancaire)
- Ton professionnel et quantification

**Quand montrer les exemples :**
- L'utilisateur demande "Tu peux me montrer un exemple ?"
- L'utilisateur hésite sur la structure
- L'utilisateur est dans un contexte bancaire/conversationnel

---

## Adaptation par type de projet

Différents types de projets nécessitent des sections spécialisées. Consulter [references/project-types.md](references/project-types.md) pour les adaptations détaillées :

- **Apps mobiles** : Accessibilité tactile, confusion de gestes, problèmes de taille d'écran
- **Conversationnel/Chat/Voix** : Compréhension NLU, ton NLG, confiance dans l'IA
- **Bancaire/Financier** : Compréhension du jargon, perception de sécurité, validation des montants
- **E-commerce** : Découverte, filtres, funnel de conversion, points d'abandon
- **SaaS/B2B** : Intégration au workflow, adoption par l'équipe, perception du ROI
- **Accessibilité** : Conformité WCAG, support des technologies d'assistance

**Important :** N'ajouter que les sections pertinentes — ne pas alourdir le document avec du contenu non applicable.

---

## Directives de rédaction

### Ton
- **Professionnel mais lisible** : éviter le jargon académique
- **Orienté business** : lier les insights à l'impact (adoption, satisfaction, tickets support)
- **Basé sur les preuves** : citer des comportements, pas des opinions

### Quantification
- Toujours utiliser le format "X/N utilisateurs"
- Inclure des pourcentages quand c'est significatif
- Fournir les métriques temporelles quand disponibles
- Spécifier la sévérité selon l'impact utilisateur

### Verbatims
- Utiliser des citations exactes dans la langue originale
- Fournir le contexte (quand/où ça a été dit)
- Sélectionner les citations qui révèlent les modèles mentaux
- Ne pas sur-citer — être sélectif

### Recommandations
- Commencer par un verbe (forme impérative) : "Ajouter X", "Supprimer Y", "Repenser Z"
- Lier au comportement observé
- Estimer l'effort qualitativement
- Quantifier l'impact attendu quand c'est possible

### Résumé exécutif (synthèse uniquement)
- 1 page max (3-4 paragraphes)
- Verdict clair : validé / à retravailler / à repenser
- Uniquement des insights actionnables
- Pas de détails techniques

---

## Contextes spéciaux

### Prototypes early
Mettre l'accent sur :
- Ce qui fonctionne (consolider la confiance dans les hypothèses validées)
- Les angles morts (ce qui n'a pas été testé)
- Pivots stratégiques vs ajustements mineurs

### Produits matures
Mettre l'accent sur :
- Comparaison avec la version précédente
- Benchmarks concurrentiels
- ROI quantifié des changements proposés

### Projets confidentiels/sensibles
- Demander à l'utilisateur les exigences de confidentialité
- Anonymiser les noms d'utilisateurs si nécessaire
- Éviter les captures d'écran avec des données personnelles

---

## Ressources

Ce skill inclut :

### references/
- **individual-patterns.md** : Structure complète et directives pour les restitutions individuelles
- **synthesis-patterns.md** : Structure complète et directives pour les restitutions multi-utilisateurs
- **project-types.md** : Adaptations spécifiques au domaine (mobile, conversationnel, bancaire, e-commerce, SaaS, accessibilité)

### assets/
- **template-individual.md** : Template vierge pour restitution de test individuel
- **template-synthesis.md** : Template vierge pour synthèse multi-utilisateurs
- **example-banking-conversational.md** : Exemple complet montrant la synthèse de 5 utilisateurs pour une app bancaire mobile conversationnelle

---

## Demandes courantes

**"Rédige une restitution pour le test de Nina"**
→ Workflow Restitution Individuelle

**"Synthétise les 5 tests de cette semaine"**
→ Workflow Restitution Synthèse

**"J'ai besoin d'un template pour mon prochain round de tests"**
→ Fournir template-individual.md ou template-synthesis.md

**"Comment structurerais-tu une restitution pour une app bancaire conversationnelle ?"**
→ Montrer example-banking-conversational.md + expliquer les adaptations de project-types.md

**"La restitution est trop longue"**
→ Réduire les verbatims, fusionner les points de friction similaires, supprimer les sections optionnelles

**"Ajoute plus de détail à la section recommandations"**
→ Lire references/synthesis-patterns.md pour le format de recommandation, ajouter les estimations d'effort et la roadmap

**"Adapte ça pour des tests d'accessibilité"**
→ Lire references/project-types.md (section Accessibilité), ajouter les critères WCAG, notes sur les technologies d'assistance
