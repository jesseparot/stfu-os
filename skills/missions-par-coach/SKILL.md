---
name: missions-par-coach
description: >
  Recherche et score les missions pertinentes d'un coach STFU dans Airtable.
  Reçoit un coach et des critères, requête Airtable, score chaque mission sur
  3 axes (secteur, expertise, format), retourne un tableau de sélection trié.
  Peut être lancé en parallèle (1 instance par coach).
user_invocable: true
context: fork
agent: general-purpose
argument-hint: "<coach> [critères de scoring]"
---

# Missions par coach

Recherche les missions pertinentes d'un coach STFU dans Airtable, les score par pertinence tri-critère, et retourne un tableau de sélection trié.

## Airtable Coordinates

- **Base ID** : `appyJq6jZuil2VMgC`
- **Table MISSIONS** : `tbl5qzd6zlaWBKpqs`
- **Table Clients** : `tblX4SA7Urt6ZnPh5`
- **Table Coachs** : `tblkriKoMRFWgIE75`
- **Table Types de mission/Offres** : `tblUwVoM2xsbN4aQ2`
- **Table Expertises STFU** : `tblQ2vbozVFSbuOLd`
- **Table Verticales** : `tblcqrVyabchAnUhS`

## IDs coachs

| Nom | Record ID |
|-----|-----------|
| Jesse Parot | `recdIpNGOSxXjNlok` |
| Mickaël Coenca | `recmbHXTFgSNQ3GXJ` |
| Benjamin Crot | `recmr64R7Yli12fzS` |
| Béatrice d'Aunay | `recrXF6U2qDEdghzP` |
| David Baruchel | `recp0f6hXqssf5ZRb` |
| David Flak | `recp1L3nTfnFyBlKE` |
| Baptiste Lahondé | `recgCjA4FwpmucBg4` |
| Nina Ledun | `recjoGEaBKu5hkIpx` |
| Juliette Testud | `recNUDHGKVTq9fvSu` |
| Johann Arias | `recGPt3ZZoNj5DnVU` |
| Quentin Splingart | `reccenh5YGsSOQlDp` |
| Pierre Prat | `recwzv5omlgZx6NWX` |
| Victoire Guyot | `reccy8dTYqLnb1oJ4` |
| Yann Le Morvan | `recy0hLlgxZqjGHoK` |
| Grégoire Debit | `recHfbAUfbFZLdNjJ` |
| Ghizlane Harfaoui | `recOTkYAMhwoRoXaK` |
| Boukar Sall | `recmChn76ndN4qolG` |
| Romain Sabatier | `recMFuCMX5gDAzDXV` |

## Input

Ce skill reçoit en argument :
- **Coach** : prénom (obligatoire)
- **Critères de scoring** (optionnels, passés par l'orchestrateur ou l'utilisateur) :
  - `--secteur` : secteurs cibles (ex: "public, innovation")
  - `--expertise` : expertises méthodologiques (ex: "design thinking, coaching")
  - `--format` : formats de mission (ex: "programme, formation, workshop")
  - `--refs` : nombre de missions max (défaut : 10-15)
  - `--profils-cctp` : profils CCTP si contexte AO

Si aucun critère n'est fourni et que le skill est invoqué directement (pas via orchestrateur), demander le contexte à l'utilisateur.

## Workflow

### 1. Parser l'input

Identifier le coach et son record ID depuis la table ci-dessus. Extraire les critères de scoring des arguments.

### 2. Requêter Airtable

Requêter la table MISSIONS via `mcp__airtable__search_records` :
- Base ID : `appyJq6jZuil2VMgC`
- Table : `tbl5qzd6zlaWBKpqs`
- Filtrer par coach (champ lié Coachs)

**IMPORTANT** : NE PAS utiliser les vues "par coach" dans Airtable. Ces vues sont conçues pour le remplissage des fiches missions, pas pour la sélection de références. Toujours requêter la table MISSIONS directement avec un filtre sur le champ Coachs.

Champs à récupérer pour chaque mission :
- `Nom interne de la mission`
- `Nom Client` (champ lié)
- `Description du projet`
- `Contexte`
- `Actions`
- `Resultats/Livrables`
- `Année(s)`
- `Type de référence`
- `Tags Verticales Séquences` (champ lié)
- `Mots clés mission`
- `Expertises STFU` (champ lié)
- `Tags offres` (champ lié)
- `Client autorisé en public`

### 3. Gestion du volume

Si le résultat est trop gros (sauvé en fichier par Airtable MCP), extraire via `jq` (Bash) les champs clés :
- `Nom interne de la mission`
- `Nom Client`
- `Description du projet`
- `Année(s)`
- `Type de référence`
- `Mots clés mission`
- `Client autorisé en public`

### 4. Scoring sémantique via agent Haiku

Déléguer le scoring à l'agent `mission-scorer` (Haiku) en **un seul appel batch** :

1. **Préparer le payload JSON** avec :
   - `criteres` : les critères reçus (secteur, expertise, format, profils_cctp si fournis)
   - `missions` : toutes les missions récupérées, avec les champs pertinents (id, nom, client, description, contexte, actions, resultats, annees, type_reference, tags_verticales, mots_cles, expertises_stfu, tags_offres, client_public)

2. **Appeler l'agent** :
   ```
   Agent(subagent_type="mission-scorer", model="haiku", prompt=<payload JSON>)
   ```

3. **Parser la réponse JSON** : extraire le tableau `scores` avec pour chaque mission : id, scores par axe (`++`/`+`/`-`), et justifications.

**Conversion en score numérique** :
- `++` = 2 points, `+` = 1 point, `-` = 0 point
- Score total = somme des 3 axes (max 6)
- Affichage dans le tableau : `++` → ✓✓, `+` → ✓, `-` → ✗

### 6. Sélection

Sélectionner top N missions, triées par score total décroissant :
- D'abord les missions avec score ≥ 5 (au moins deux `++` et un `+`)
- Puis score 3-4
- Ignorer score ≤ 2 sauf si pas assez de résultats
- **Départage à score égal** : favoriser les missions avec plus de `++` (un `++`+`+`+`-` bat un `+`+`+`+`+`)

### 7. Output

Retourner le tableau markdown trié par score décroissant :

```
| V | Client | Mission | Description | Année | Type | Secteur | Expertise | Format | Score |
|---|--------|---------|-------------|-------|------|---------|-----------|--------|-------|
|   | IDEMIA | Innovathon Strat | 8 promos, formation DT, coaching, pitch COMEX | 2018-2025 | Programme | ✓✓ | ✓✓ | ✓✓ | 6/6 |
|   | BNP | Design Sprint | Facilitation sprint innovation équipe produit | 2022 | Workshop | ✓✓ | ✓ | ✗ | 3/6 |
```

- Colonne **V** = vide, pour validation utilisateur
- Colonne **Description** = synthèse 1 ligne (~10-15 mots) du champ `Description du projet`
- Inclure les **record IDs** Airtable dans l'output (en commentaire ou en colonne masquée) pour que les skills en aval puissent récupérer les fiches complètes

## Notes

- Ce skill est conçu pour être forkable : 1 instance par coach, lancé en parallèle par l'orchestrateur `/cv-propale`
- Peut aussi être invoqué directement pour explorer les missions d'un coach
- Les critères de scoring viennent du document de référence (DCE, brief, note Slite), PAS d'hypothèses
