---
name: mission-airtable
description: Crée une fiche mission dans la base Airtable MISSIONS à partir des fichiers d'un projet client. Lit les documents du projet (notes, CR, restitutions, README), extrait les informations clés, résout les références (client, coachs, tags, verticales, expertises), et crée l'enregistrement Airtable. Utilisable quand on demande de capitaliser, référencer, ou ajouter une mission dans Airtable.
---

# Mission Airtable

## Overview

Crée un enregistrement dans la table MISSIONS de la base Airtable à partir des fichiers locaux d'un projet client. Extrait les informations, résout les références vers les tables liées, et crée la fiche.

## Airtable Coordinates

- **Base ID** : `appyJq6jZuil2VMgC` (Marketing: Base Missions)
- **Table MISSIONS** : `tbl5qzd6zlaWBKpqs`
- **Table Clients** : `tblX4SA7Urt6ZnPh5`
- **Table Coachs** : `tblkriKoMRFWgIE75`
- **Table Types de mission/Offres** : `tblUwVoM2xsbN4aQ2`
- **Table Expertises STFU** : `tblQ2vbozVFSbuOLd`
- **Table Verticales** : `tblcqrVyabchAnUhS`

## Workflow

### 1. Identifier les fichiers source

L'utilisateur fournit soit :
- Un chemin vers un dossier projet (`_workspace/projects/{project-name}/`)
- Des chemins vers des fichiers specifiques
- Le nom d'un projet/client (le skill cherche dans `_workspace/projects/`)

**Fichiers à chercher en priorité :**
- `README.md` ou tout fichier de contexte projet
- `note-*.md` (notes d'état, notes internes)
- `cr-*.md` (comptes-rendus)
- `*restitution*.md` (restitutions)
- `*_draft.md` ou `*_final.md` (livrables)
- Tout fichier `.md` pertinent dans le dossier projet

**Ne pas lire :**
- Les fichiers `.pptx`, `.xlsx` (trop volumineux, peu de texte exploitable)
- Les fichiers de `tests-utilisateurs/` individuels (trop granulaire, lire plutôt la restitution)
- Les dossiers `partage/` (fichiers client, pas de contexte mission)

### 2. Lire et extraire les informations

Lire les fichiers identifiés et extraire :

| Information | Source typique | Champ Airtable |
|-------------|---------------|----------------|
| Nom du client | Nom du dossier client ou contenu | Client (linked) |
| Nom interne de la mission | Nom du dossier projet ou contenu | Nom interne de la mission |
| Contexte et enjeux | Notes, README, propale | Brief + Contexte |
| Ce qui a été fait | CR, notes, restitutions | Brief + Actions |
| Résultats et livrables | Notes, restitutions | Brief + Resultats/Livrables |
| Description synthétique | Synthétiser depuis le tout | Description du projet |
| Participants STFU | CR, notes | Coachs |
| Années de la mission | Dates dans les fichiers | Année(s) |
| Pays | Contenu ou défaut France | Pays |

### 3. Construire le Brief

Le champ **Brief** est le plus important car il alimente les champs IA auto-générés (Description IA, Contexte IA, Actions IA, Resultats/livrables IA, Mots Clés AI).

**Format du Brief :**
```
Contexte - [résumé du contexte en 1-2 phrases]

[Paragraphe de contexte détaillé : situation initiale du client, enjeux, contraintes, éléments déclencheurs. 3-5 lignes.]

Accomplissements :

> [Action 1]
> [Action 2]
> [Action 3]
> [Action 4]
> [Action 5]

[Paragraphe de description des actions, détaillant ce que STFU a fait. Suffisamment riche pour que les champs IA puissent en extraire de la matière.]

Résultats et livrables :

- [Livrable/résultat 1]
- [Livrable/résultat 2]
- [Livrable/résultat 3]
```

Le Brief doit être factuel, riche en détails concrets, et fidèle au contenu des fichiers source. Ne rien inventer.

### 4. Résoudre les références (tables liées)

Pour chaque champ lié, chercher les enregistrements correspondants :

#### Client
Chercher dans la table Clients (`tblX4SA7Urt6ZnPh5`) via `mcp__airtable__search_records` avec le nom du client.
Si le client n'existe pas, signaler à l'utilisateur et proposer de créer l'enregistrement dans la table Clients d'abord.

#### Coachs
Chercher dans la table Coachs (`tblkriKoMRFWgIE75`) via `mcp__airtable__search_records` avec les noms des participants STFU identifiés dans les fichiers.

**Mapping noms courants → record IDs :**

| Nom | Record ID |
|-----|-----------|
| Jesse Parot | `recdIpNGOSxXjNlok` ou `reczQP0JsElzULBgf` |
| Ghizlane Harfaoui | `recOTkYAMhwoRoXaK` |
| Mickaël Coenca | `recmbHXTFgSNQ3GXJ` |
| David Baruchel | `recp0f6hXqssf5ZRb` |
| David Flak | `recp1L3nTfnFyBlKE` |
| Baptiste Lahondé | `recgCjA4FwpmucBg4` |
| Benjamin Crot | `recmr64R7Yli12fzS` |
| Nina Ledun | `recjoGEaBKu5hkIpx` |
| Juliette Testud | `recNUDHGKVTq9fvSu` |
| Johann Arias | `recGPt3ZZoNj5DnVU` |
| Quentin Splingart | `reccenh5YGsSOQlDp` |
| Pierre Prat | `recwzv5omlgZx6NWX` |
| Victoire Guyot | `reccy8dTYqLnb1oJ4` |
| Yann Le Morvan | `recy0hLlgxZqjGHoK` |
| Béatrice D'Aunay | `recrXF6U2qDEdghzP` |
| Grégoire Debit | `recHfbAUfbFZLdNjJ` |
| Boukar Sall | `recmChn76ndN4qolG` |
| Romain Sabatier | `recMFuCMX5gDAzDXV` |

Utiliser `recdIpNGOSxXjNlok` pour Jesse Parot (c'est le record avec le plus de missions).

#### Tags offres (Type de mission)
Mapper depuis le contenu de la mission vers les valeurs existantes :

| Tag offre | Record ID | Quand utiliser |
|-----------|-----------|----------------|
| Métier - Projet | `recxtiI8q7D1NLopY` | Conception, exploration, prototypage, production de livrables |
| Métier - Explo strat | `recuVPVSREuww1vi8` | Exploration stratégique menée conjointement |
| Programme d'innovation | `recn59myGgrz2OnjS` | Conception et opérationnalisation d'un programme |
| Projet d'intrapreneuriat | `recGikpzEcbJOBiqU` | Coaching de porteurs de projets internes |
| Stratégie organisation inno | `recY6if47N2WQxgKd` | Conseil stratégique, cadrage, organisation |
| Formation / conférence | `recEQPzYMcOGlCTO8` | Transmission, acculturation, pédagogie |
| Workshop / hackathon | `recbT1DhS9d0fwz5U` | Animation de dispositifs collectifs |
| Autres | `rec4XC4NABR009ZTk` | Missions hors catégories |

#### Tags Verticales Séquences (Secteur)
Mapper depuis le secteur du client :

| Verticale | Record ID |
|-----------|-----------|
| Banque & Assurances | `recwJf65ZVtLbkjfH` |
| Energie | `recPI57Mdn6yapmYL` |
| Automobile | `recAP9Bl4vdOqNsgr` |
| Luxe | `reclIW0OZali2cA3n` |
| Cosmétique | `recrFBD197A1wpw2S` |
| Santé | `recPqUbmGtydfawCk` |
| Retail & ecommerce | `recsLURlr2VsTYMsZ` |
| Construction & ingénierie | `recFz0rd8eEdQrmGd` |
| Mobilité & Transports de personnes | `recM7UsvPI16nReuS` |
| Logistique & Transport de biens | `recGZNL3QApStoKtm` |
| Agroalimentaire, Vins & spiritueux | `recNeZH34Ob4IGE62` |
| Tourisme & hotellerie | `rec4mf9XSFA0A0zaq` |
| Défense sécurité aéronautique | `rec4hUPV02aK2kWra` |
| Secteur public | `recgNFmDjRU2LGXuK` |
| Education | `recuVBfQw4DcdLgUk` |
| Conseil | `recUQeTT2Hmq7Ojoa` |
| Industrie | `rece8MEr2EBo9jUKk` |

#### Expertises STFU
Mapper depuis les compétences mobilisées dans la mission :

| Expertise | Record ID | Quand utiliser |
|-----------|-----------|----------------|
| Méthodologie d'innovation | `rec3FrgL5BZOvvmUj` | Design thinking, workshops, sprints |
| UX Design | `recaKcdvrE076cVQi` | Tests utilisateurs, prototypage UX, recherche utilisateur |
| Prototypage | `recRfW10WJyxPsdzJ` | Prototypes, maquettes, POC |
| Etudes & analyses de marchés | `recVBWsHVW2KqyMZs` | Benchmarks, études concurrentielles |
| Product-market fit & value proposition testing | `recPHVNZnfDze3QQr` | Validation produit, tests de valeur |
| Go-to-market & Business development | `reco3QY7WOTP1ZMjt` | Stratégie commerciale, lancement |
| Marketing & branding | `recJk91luEAhgP5ap` | Identité, communication, branding |
| Elaboration du business model | `recspzPyL2deqAbWz` | Business model canvas, modèle économique |
| Maitrise du pitch & storytelling | `recqhmyNjQjJbBfuI` | Présentation, storytelling |
| MVP build - No-code & low-code | `recjooCvnc7bKz4VS` | Construction MVP |
| Beta-test | `recyl4EpzLbX9Rf0i` | Tests en conditions réelles |
| Scrum Master & Project management | `recSDA4uaduoWBQcd` | Gestion de projet agile |
| Financial stratégies & budgeting | `reccEed9HlG0NXUg7` | Stratégie financière |
| Scaling strategies: Sales et opérations | `recr12IGEAy22dXCv` | Passage à l'échelle |
| Partnerships: startup & innovation policy | `recRWrkG4n2LhpU1t` | Partenariats, politique innovation |
| Technology assessment and maturation, IP | `recqbbcSmpgpbA5OZ` | Évaluation technologique |
| Valorisation et stratégies de cessions | `rec6Q7yOWtIqacmpg` | M&A, cessions |
| Planification et implémentation des opérations business | `recbom4qH1pHEGGWr` | Opérations |

### 5. Remplir les champs directs

#### Type de référence (singleSelect)
Inférer depuis le contenu :
- `Programme` : programme récurrent multi-projets
- `Saison` : 1 édition d'un programme récurrent (ex: Idemia Innovathon #4)
- `Projet d'intra` : projet porté par des intrapreneurs
- `Mission métier` : mission de conseil/accompagnement classique
- `Workshop` : intervention ponctuelle type workshop
- `Formation` : formation ou conférence
- `Conférence` : conférence ou keynote
- `Stratégie` : mission de cadrage stratégique

#### Client autorisé en public (singleSelect)
- `Autorisé` : le nom du client peut être cité publiquement
- `Secret` : ne pas citer le nom du client
- `Ne sais pas` : en cas de doute

En cas de doute, mettre `Ne sais pas` et demander à l'utilisateur.

#### Année(s) (multipleSelects)
Valeurs possibles : `2017`, `2018`, `2019`, `2020`, `2021`, `2022`, `2023`, `2024`, `2025`, `2026`
Extraire depuis les dates dans les fichiers. Plusieurs années possibles si la mission s'étend.

#### Pays (multipleSelects)
Défaut : `🇫🇷 France`
Valeurs possibles : `🇿🇦 Afrique du Sud`, `🇩🇪 Allemagne`, `🇰🇭 Cambodge`, `🇫🇷 France`, `🇮🇳 Inde`, `🇮🇹 Italie`, `🇳🇱 Pays-Bas`, `🇩🇴 République Dominicaine`, `🇹🇳 Tunisie`, `🇺🇸 USA`, `🇬🇧 Royaume-Uni`, `🇲🇦 Maroc`, `Singapour`, `Brésil`, `Espagne`

#### Status (singleSelect)
Toujours `To-do` pour une nouvelle fiche.

#### Descriptif client anonyme
Générer une description courte et sobre du client sans le nommer.
Style : "Leader mondial de l'énergie", "Acteur majeur de la banque et de l'assurance", "Néobanque française".

#### Description du projet
3 lignes max. Ce qu'est le projet et son objectif principal. Mettre en avant la valeur apportée au client.

#### Contexte
3 lignes max. Situation initiale du client, enjeux, éléments déclencheurs. Répondre à "pourquoi ce projet a été lancé". Ne pas décrire les actions menées.

#### Actions
Liste de 4 à 8 puces. Verbes d'action concrets. Logique chronologique ou structurée. Exclure résultats et livrables.

#### Resultats/Livrables
3-4 puces max. Livrables produits et résultats obtenus. Impact concret et observable.

#### Mots clés mission
Liste de mots-clés séparés par des virgules. Mots-clés actionnables, métiers ou sectoriels. 1 à 3 mots max par mot-clé.

### 6. Posture rédactionnelle

La posture dépend du Tag offres :

| Tag offres | Posture | Formulation |
|------------|---------|-------------|
| Stratégie organisation inno | Consultant | Conseil stratégique, cadrage, recommandations. Ne pas écrire que STFU exécute. |
| Métier - Projet | Faisant | Implication directe dans conception, exploration, prototypage. |
| Métier - Explo strat | Faisant | Exploration stratégique menée conjointement. |
| Programme d'innovation | Faisant | Conception et opérationnalisation du programme. |
| Projet d'intrapreneuriat | Coach | Accompagnement et coaching. Ne jamais écrire que STFU a réalisé le projet. |
| Formation / conférence | Formateur | Transmission, acculturation, pédagogie. |
| Workshop / hackathon | Formateur | Conception et animation de dispositifs collectifs. |

### 7. Présenter le draft à l'utilisateur

Avant de créer l'enregistrement, présenter un résumé structuré :

```
## Draft fiche mission

**Client** : [Nom client]
**Nom interne** : [Nom mission]
**Type** : [Type de référence]
**Tag offres** : [Tag]
**Verticale** : [Verticale]
**Année(s)** : [Année(s)]
**Pays** : [Pays]
**Coachs** : [Noms]
**Client autorisé** : [Autorisé/Secret/Ne sais pas]

### Brief
[Brief complet]

### Description du projet
[3 lignes]

### Contexte
[3 lignes]

### Actions
- [Action 1]
- ...

### Résultats/Livrables
- [Livrable 1]
- ...

### Mots clés
[mots-clés]

### Expertises STFU
[Liste]
```

Demander confirmation ou ajustements avec `AskUserQuestion`.

### 8. Créer l'enregistrement

Utiliser `mcp__airtable__create_record` avec :

```json
{
  "baseId": "appyJq6jZuil2VMgC",
  "tableId": "tbl5qzd6zlaWBKpqs",
  "fields": {
    "Client": ["<client_record_id>"],
    "Nom interne de la mission": "<nom>",
    "Brief": "<brief_complet>",
    "Description du projet": "<description>",
    "Contexte": "<contexte>",
    "Actions": "<actions>",
    "Resultats/Livrables": "<resultats>",
    "Mots clés mission": "<mots_cles>",
    "Type de référence": "<type>",
    "Client autorisé en public": "<statut>",
    "Descriptif client anonyme": "<descriptif>",
    "Status": "To-do",
    "Année(s)": ["<annee1>", "<annee2>"],
    "Pays": ["🇫🇷 France"],
    "Coachs": ["<coach_record_id_1>", "<coach_record_id_2>"],
    "Tags offres": ["<tag_offre_record_id>"],
    "Tags Verticales Séquences": ["<verticale_record_id>"],
    "Expertises STFU": ["<expertise_record_id_1>", "<expertise_record_id_2>"]
  }
}
```

**Important sur les linked records** : les champs liés (Client, Coachs, Tags offres, Tags Verticales Séquences, Expertises STFU) prennent des **arrays de record IDs**, pas des noms.

### 9. Confirmation

Après création, communiquer :
1. Confirmation que la fiche a été créée
2. Le record ID de la nouvelle fiche
3. Le status de la fiche (normalement `🟠 A compléter` avec la liste des champs manquants, ou `🟢 Validé` si tout est rempli)
4. Rappeler que les champs IA (Description IA, Contexte IA, Actions IA, etc.) se rempliront automatiquement depuis le Brief dans Airtable
5. Si des champs n'ont pas pu être remplis (ex: Propale, Restitution, Cover Image), les lister

## Champs optionnels (URLs)

Ces champs ne peuvent être remplis que si l'utilisateur fournit les liens :
- **Propale** : lien Google Slides de la propale
- **Restitution** : lien slides de restitution ou doc principal ou Drive
- **Cover Image** : URL d'une image quali style Unsplash
- **Lien Slide Case Study Existant** : si un case study existe déjà

## Cas particuliers

### Client n'existe pas dans Airtable
Si la recherche dans la table Clients ne retourne rien :
1. Informer l'utilisateur
2. Proposer de créer le client d'abord (via `mcp__airtable__create_record` dans la table Clients)
3. Utiliser le record ID du nouveau client pour la mission

### Mission déjà existante
Avant de créer, faire une recherche dans MISSIONS avec le nom du client + nom de la mission pour éviter les doublons.

### Fichiers insuffisants
Si les fichiers ne contiennent pas assez d'informations pour remplir les champs requis :
1. Remplir ce qui est possible
2. Lister les champs manquants
3. Proposer à l'utilisateur de compléter oralement ou de pointer vers d'autres fichiers

## Example Usage

```
User: "Ajoute la mission Arkea banque conversationnelle dans Airtable"
→ Le skill cherche dans _workspace/projects/arkea-banque-conversationnelle/
→ Lit les fichiers clés (note d'état, CR, restitution)
→ Extrait les infos, résout les références
→ Présente le draft
→ Crée l'enregistrement après validation
```
