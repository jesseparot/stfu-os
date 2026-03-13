---
name: cv-builder
description: >
  Construit un CV structuré pour un coach STFU à partir de missions Airtable,
  pour les réponses AO et propositions commerciales. Utiliser quand on demande
  de rédiger un CV, une fiche intervenant, ou des références par coach.
user_invocable: true
context: fork
agent: general-purpose
argument-hint: "<coach> <objectif: AO|propale|pitch>"
---

# cv-builder

Tu construis des CVs structurés pour les coachs STFU à partir de leurs bios (dossier `team/`) et de missions Airtable.

## Input attendu

Tu reçois en input :
- **Objectif** : AO / propale / pitch / autre
- **Contexte de l'AO** (si AO) : profils CCTP requis, niveaux, exigences
- **Coach(s)** : nom(s)
- **Missions sélectionnées** : liste (record IDs, noms, ou output de `/missions-par-coach`)
- **Chemin de sortie** : où écrire le fichier

Arguments CLI (quand invoqué par l'orchestrateur) :
- `--objectif` : AO / propale / pitch
- `--missions` : record IDs séparés par virgules
- `--profils-cctp` : profils CCTP (si AO)
- `--output` : chemin du fichier de sortie

## Airtable Coordinates

- **Base ID** : `appyJq6jZuil2VMgC`
- **Table MISSIONS** : `tbl5qzd6zlaWBKpqs`

## Workflow

### 1. Lire la bio du coach

Lire le fichier `team/{prenom-nom}.md` dans le plugin directory. Ce fichier contient :
- Nom complet, rôle STFU
- Formation (diplômes, écoles, niveaux)
- Parcours pro (startups, postes, dates)
- Enseignement le cas échéant
- Compétences clés

**IMPORTANT - dates du parcours pro** : si la bio ne contient pas de dates pour un poste, NE PAS en inventer. Laisser le champ date vide ou omettre la date. La règle "pas de contenu inventé" s'applique aussi au parcours pro.

### 2. Récupérer les fiches missions complètes

Pour chaque mission sélectionnée, utiliser `mcp__airtable__get_record` (base `appyJq6jZuil2VMgC`, table `tbl5qzd6zlaWBKpqs`) pour obtenir la fiche complète.

**NE PAS** se contenter du preview tronqué de `list_records` ou `search_records`. Toujours lire la fiche complète.

Champs à utiliser :
- `Description du projet`
- `Contexte`
- `Actions`
- `Resultats/Livrables`
- `Mots clés mission`
- `Année(s)`
- `Nom Client`
- `Nom interne de la mission`
- `Client autorisé en public`

### 3. Choisir le template selon l'objectif

Trois templates disponibles : AO, propale, pitch.

### 4. Rédiger et écrire le fichier

## Templates

### Template AO (appel d'offres)

```markdown
# [NOM Prénom]

**Profil(s) CCTP** : [Liste des profils visés par le CCTP - UNIQUEMENT ceux explicitement fournis en input. NE PAS inventer de profils CCTP.]

## Formation
- [Diplôme] - [École] - Niveau [X]

## Parcours professionnel
(ordre antéchronologique - du plus récent au plus ancien)
- **[Rôle]** - [Entreprise] - [Dates si connues]
  [1-2 lignes de description]

## Compétences clés
- [Compétence alignée avec profils CCTP]

## Expériences opérationnelles pertinentes

### [Client] - [Nom mission] ([Année])
- **Contexte** : [1-2 phrases depuis Airtable]
- **Rôle** : [Depuis Airtable Actions]
- **Livrables** : [Depuis Airtable Résultats/Livrables]
- **Adéquation profil** : [En quoi cette mission démontre les compétences attendues par le CCTP - utiliser le même intitulé de section dans tous les CVs]
```

### Template propale (proposition commerciale)

```markdown
## [Prénom Nom] - [Rôle STFU]

[Bio 2-3 lignes : parcours, expertise principale, ce qui le/la rend pertinent(e) pour cette mission]

### Missions pertinentes

- **[Client] - [Mission]** ([Année]) : [1 phrase résultat/impact]
- **[Client] - [Mission]** ([Année]) : [1 phrase résultat/impact]
[...]
```

### Template pitch (présentation courte)

```markdown
**[Prénom Nom]** - [Formation courte] - [Rôle STFU]
- [Client] : [impact en 5 mots]
- [Client] : [impact en 5 mots]
[...]
```

## Règles de rédaction

Ces règles s'appliquent à tous les formats :

1. **Source unique** : données Airtable pour Contexte/Rôle/Livrables. NE PAS inventer de contenu. Chaque phrase doit être traçable vers un champ Airtable.
2. **Clients nommés par défaut** sauf si `Client autorisé en public` = Secret ET le contexte l'exige :
   - Propale : anonymiser les secrets (ex: "un acteur majeur du secteur bancaire")
   - AO : souvent tout en clair car réponse officielle - demander si pas clair
   - Pitch : anonymiser les secrets
3. **Style STFU** :
   - Pas de title case (sauf noms propres)
   - Pas d'em-dash (utiliser " - ")
   - Mots simples, phrases courtes
   - Accents français corrects
4. **Pas de padding** : ne pas gonfler le contenu. Si une mission a peu de détail dans Airtable, le bloc sera court. C'est normal.
5. **Ordre antéchronologique** : parcours pro ET expériences opérationnelles doivent être en ordre antéchronologique (du plus récent au plus ancien).
6. **Profils CCTP** : ne jamais inventer de profils CCTP. Utiliser uniquement ceux fournis explicitement en input. Si aucun profil n'est fourni, omettre la ligne.
7. **Cohérence multi-CVs** : quand plusieurs CVs sont produits pour le même AO, utiliser exactement les mêmes intitulés de sections et le même format de présentation de l'adéquation profil. L'intitulé standard est "Adéquation profil".

## Vérifications avant écriture

Avant d'écrire le fichier final, vérifier :

- [ ] Si AO : formation >= niveau requis pour les profils visés, XP >= années requises
- [ ] Chaque mission listée existe dans Airtable (pas de mission inventée)
- [ ] Pas de contenu inventé (chaque phrase traçable vers un champ Airtable ou la bio team/)
- [ ] Pas de dates inventées dans le parcours pro (si la bio n'a pas de date, ne pas en mettre)
- [ ] Ordre antéchronologique respecté (parcours pro + expériences)
- [ ] Profils CCTP = uniquement ceux fournis en input
- [ ] Style STFU respecté (pas de title case, pas d'em-dash)
- [ ] Clients secrets anonymisés si nécessaire selon le contexte
