# Chiffrage et estimation des durées

Référence pour le calcul des durées dans la table de l'approche (section 5 de la propale).

## Unité de base

- **1 jour = 8 heures**
- **Format** : virgule décimale (1,5 j), granularité minimale 0,5 j dans la table
- **Marge coordination** : 10-20% par phase, explicité dans le détail du calcul

## Heuristiques par type d'activité

| Type d'activité | Durée unitaire | Justification |
|-----------------|----------------|---------------|
| Interview facile (interne, contact existant) | 1h | Prépa + entretien + notes |
| Interview difficile (externe, prise de contact) | 3h | Sourcing + relances + entretien + notes |
| Atelier court (2-4h) | 0,5 j | Prépa + animation + restitution flash |
| Atelier demi-journée avec livrable | 1 j | Prépa + animation + rédaction livrable |
| Rapport court (< 10 pages) | 1 j | Rédaction + mise en forme + 1 passe de relecture |
| Rapport long (> 10 pages) | 2-3 j | Rédaction + structuration + relecture + itération |
| Kickoff call | 0,5 j | Prépa support + animation + CR |
| Analyse de données | 2-4 j | Collecte + nettoyage + analyse + synthèse |
| Itération/révisions client | 0,5-1 j | Intégration retours + ajustement + renvoi |
| Présentation (prépa + animation) | 1 j | Création support + répétition + animation |

## Vocabulaire emoji

Chaque étape dans la table de l'approche commence par un emoji du vocabulaire fixe :

| Emoji | Type d'activité |
|-------|-----------------|
| 🛠 | Atelier |
| 📞 | Call |
| 📊 | Analyse |
| ✍️ | Rédaction |
| 🧪 | Test |
| 🎯 | Présentation |
| 👥 | Interview |
| 📋 | Livrable |
| 🔍 | Recherche |
| 📦 | Livraison |

## Exemples de calcul annotés

### Exemple 1 — Phase de cadrage

| Phase | Étape | Description | Détail du calcul | Durée (j) |
|-------|-------|-------------|------------------|-----------|
| Phase 1 — Cadrer | 📞 Kickoff | - Alignement équipes <br> - Validation périmètre | Prépa 2h + call 2h + CR 1h = 5h ÷ 8h = 0,6 j → 1 j | 1 |
| | 👥 Interviews internes | - 6 entretiens stakeholders <br> - Grille d'analyse | 6 interviews × 1h = 6h ÷ 8h = 0,8 j → 1 j | 1 |
| | ✍️ Synthèse de cadrage | - Rapport de cadrage <br> - Matrice enjeux | Rédaction rapport court = 1 j | 1 |
| | 🎯 Restitution cadrage | - Présentation COPIL | Prépa 4h + animation 2h = 6h ÷ 8h = 0,8 j → 1 j | 1 |
| | | | Marge coordination 15% : 4 j × 0,15 = 0,6 j → 0,5 j | 0,5 |
| **Sous-total Phase 1** | | | | **4,5** |

### Exemple 2 — Phase terrain avec interviews externes

| Phase | Étape | Description | Détail du calcul | Durée (j) |
|-------|-------|-------------|------------------|-----------|
| Phase 2 — Explorer | 👥 Interviews externes | - 8 entretiens utilisateurs <br> - Guide d'entretien | 8 interviews × 3h = 24h ÷ 8h = 3 j | 3 |
| | 📊 Analyse des verbatims | - Codage thématique <br> - Matrice insights | Analyse données = 2 j | 2 |
| | 🛠 Atelier co-conception | - Idéation avec équipe client <br> - Priorisation | Atelier demi-journée avec livrable = 1 j | 1 |
| | | | Marge coordination 15% : 6 j × 0,15 = 0,9 j → 1 j | 1 |
| **Sous-total Phase 2** | | | | **7** |

### Exemple 3 — Phase de livraison

| Phase | Étape | Description | Détail du calcul | Durée (j) |
|-------|-------|-------------|------------------|-----------|
| Phase 3 — Livrer | ✍️ Rédaction rapport final | - Rapport > 10 pages <br> - Recommandations | Rapport long = 3 j | 3 |
| | 🧪 Revue interne | - Relecture croisée <br> - Ajustements | Itération = 0,5 j | 0,5 |
| | 📦 Livraison client | - Envoi + call de présentation | Présentation 1 j | 1 |
| | | | Marge coordination 10% : 4,5 j × 0,1 = 0,5 j | 0,5 |
| **Sous-total Phase 3** | | | | **5** |
| **TOTAL** | | | | **16,5** |

## Règles d'arrondi

- Arrondir au 0,5 j supérieur dans la table
- Ne jamais afficher de durée < 0,5 j dans la table (regrouper les micro-tâches)
- La marge coordination est une ligne explicite par phase, pas un arrondi silencieux
