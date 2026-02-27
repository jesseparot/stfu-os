---
name: case-study-slide
description: Génère une présentation Google Slides case study à partir d'une mission Airtable. Copie le template case study, remplit avec les données de la mission (titre, contexte, réalisations). Utiliser pour créer une slide case study, un deck case study, ou générer une présentation à partir d'une mission.
---

# Générateur de slides Case Study

## Vue d'ensemble

Crée une présentation Google Slides case study brandée à partir d'un enregistrement mission Airtable. Copie le template case study (qui contient le bon thème, les polices et la mise en page), puis remplit les zones de texte avec les données de la mission.

## Workflow

### 1. Identifier la mission

**Si un nom de mission/client est fourni :**
- Rechercher dans la table Airtable MISSIONS via `mcp__airtable__search_records`
- Si plusieurs résultats, présenter les meilleurs matchs et laisser l'utilisateur choisir

**Si aucune mission n'est spécifiée :**
- Demander à l'utilisateur quelle mission utiliser

### 2. Extraire les données de la mission

Depuis l'enregistrement Airtable, extraire :

| Champ | Colonne Airtable | Usage |
|-------|-----------------|-------|
| Nom client | `Nom Client` | Titre |
| Nom de la mission | `Nom interne de la mission` | Titre |
| Contexte | `Contexte` | Section Contexte |
| Description | `Description du projet` | Fallback si Contexte est vide |
| Résultats | `Resultats/Livrables` | Section Réalisations |
| Actions | `Actions` | Peut compléter Réalisations si Résultats est léger |
| Année(s) | `Année(s)` | Métadonnées |
| Industrie | `Tags Verticales Séquences` | Métadonnées |
| Type | `Type de référence` | Métadonnées |
| Tags | `Tags offres` | Métadonnées |
| Public OK | `Client autorisé en public` | Signaler si non autorisé |

**Règles de contenu :**
- Pour le **titre** : `{NOM CLIENT} — {Nom de la mission}`
- Pour le **Contexte** : utiliser le champ `Contexte`. Si vide, utiliser `Description du projet` en fallback
- Pour les **Réalisations** : utiliser le champ `Resultats/Livrables`. Formater en bullet points (préfixer chaque ligne avec `• ` si pas déjà en puces). Si vide, utiliser le champ `Actions` à la place
- Nettoyer les artéfacts markdown (`\-`, `\\-`, etc.) du texte Airtable
- Supprimer les espaces en début/fin de chaque champ

### 3. Copier le template

Copier la présentation template case study pour créer un nouveau fichier.

**Coordonnées du template :**
- Template ID : `1lTiuH1X-X4XyMta0aHsqAV2vrhYbAgEyK4G-_hX4ptY`
- Email utilisateur : Lire `$GOOGLE_USER_EMAIL` depuis l'environnement (`echo $GOOGLE_USER_EMAIL` via Bash). Si non défini, demander à l'utilisateur son email Google `@stfu.pro`.

**Paramètres de copie :**
- Nouveau nom : `Case Study — {Client} — {Nom de la mission}`
- Destination : Drive racine de l'utilisateur (par défaut) sauf indication contraire

```
mcp__google-workspace__copy_drive_file(
  user_google_email=<GOOGLE_USER_EMAIL>,
  file_id="1lTiuH1X-X4XyMta0aHsqAV2vrhYbAgEyK4G-_hX4ptY",
  new_name="Case Study — {Client} — {Nom de la mission}"
)
```

### 4. Remplir les zones de texte

Le template a une slide avec 3 zones de texte. Insérer le contenu via `batch_update_presentation`.

**Mapping des zones de texte (IDs stables du template) :**

| ID de la zone | Rôle | Contenu |
|---------------|------|---------|
| `g3c7bb67f70e_0_237` | Titre | `{CLIENT} — {Nom de la mission}` |
| `g3c7bb67f70e_0_4` | Contexte | Texte de contexte ou description |
| `g3c7bb67f70e_0_5` | Réalisations | Résultats/livrables en bullet points |

**Requêtes batch update :**
```json
[
  {"insertText": {"objectId": "g3c7bb67f70e_0_237", "text": "..."}},
  {"insertText": {"objectId": "g3c7bb67f70e_0_4", "text": "..."}},
  {"insertText": {"objectId": "g3c7bb67f70e_0_5", "text": "..."}}
]
```

Pas de styling nécessaire — le thème du template applique automatiquement les polices, tailles et couleurs.

### 5. Signaler la confidentialité

Si `Client autorisé en public` n'est PAS "Autorisé", avertir l'utilisateur :
> "Ce client n'est pas autorisé en public. Cette case study est à usage interne uniquement."

### 6. Retourner le résultat

Communiquer à l'utilisateur :
1. Lien vers la présentation créée
2. Nom du client et de la mission
3. Avertissement de confidentialité si applicable
4. Rappel que le design du template est en cours d'amélioration (TODO : améliorer la mise en page, ajouter une colonne droite pour actions/métadonnées)

## Ressources

- **Airtable MISSIONS** : base `appyJq6jZuil2VMgC`, table `tbl5qzd6zlaWBKpqs`
- **Template** : `1lTiuH1X-X4XyMta0aHsqAV2vrhYbAgEyK4G-_hX4ptY`
- **Email utilisateur** : `$GOOGLE_USER_EMAIL` (résoudre via Bash)

## Relation avec stfu-slides

Ce skill gère les **case studies simples (1 slide)** à partir d'un template dédié. Pour des présentations multi-slides (decks complets, propositions, restitutions), utiliser le skill `stfu-slides` qui gère le design engine complet avec choix de layout, compositions custom et self-review visuel.

## Notes d'amélioration du template

Le template actuel (v1) est minimal — fond blanc, accent jaune, deux sections en colonne gauche. Améliorations futures :
- Ajouter une colonne droite pour les métadonnées client (année, industrie, type de mission)
- Ajouter une zone pour la section Actions
- Ajouter un emplacement pour le logo client
- Mieux utiliser l'espace horizontal (actuellement les 40% droits sont vides)
- Envisager une variante multi-slides pour les case studies plus riches

Quand le template est mis à jour, re-sonder les IDs des zones de texte en insérant des marqueurs de test (`[BOX-{id}]`) et en vérifiant la miniature. Mettre à jour le mapping dans ce skill en conséquence.

## Exemples d'utilisation

```
User: "Fais une case study slide pour la mission Bayer Clinique du Futur"

Claude: [Recherche dans Airtable "Bayer Clinique"]
Claude: [Copie le template, remplit avec les données de la mission]
Claude: "Case study créée : https://docs.google.com/presentation/d/...
        Mission : Bayer — Clinique du Futur Onco (2026)
        ⚠️ Client non autorisé en public — usage interne uniquement."
```

```
User: "/case-study-slide Stellantis Wheel Protection"

Claude: [Recherche, trouve la mission, copie le template, remplit]
Claude: "Case study créée : https://docs.google.com/presentation/d/...
        Mission : Stellantis — Star Up Wheel Protection (2025-2026)"
```
