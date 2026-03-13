---
name: workshop-debrief
description: >
  Crée un debrief structuré et client-facing à partir des productions d'un workshop (photos murales,
  whiteboards, transcripts). Extrait le contenu via OCR interactif, structure par exercice, adapte
  les sections au type d'atelier, et publie dans Slite. Deux modes : présentiel (photos) et
  distanciel (screenshots/PDF + transcript). Utiliser pour débriefer, restituer ou synthétiser
  un atelier, un workshop, un sprint, une rétro, ou un exercice collaboratif.
user_invocable: true
---

# Workshop debrief

Génère un debrief structuré et client-facing à partir des productions brutes d'un workshop (photos, whiteboards, transcripts) et le publie dans Slite.

## Déclenchement

L'utilisateur invoque `/workshop-debrief` ou demande de débriefer un atelier.

```
/workshop-debrief
/workshop-debrief service blueprint decathlon
/workshop-debrief (avec des photos dans le dossier courant)
```

**Input** : photos murales, screenshots whiteboard, transcripts, slides de facilitation
**Output** : note Slite structurée, client-facing, prête à partager

## Dépendances MCP

| MCP | Niveau | Usage |
|-----|--------|-------|
| `slite` | Projet (stfu-os) | Publication du debrief |

## Workflow

### Étape 1 — Qualifier le mode et le contexte

Utiliser `AskUserQuestion` pour recueillir le contexte :

| Information | Obligatoire | Exemple |
|-------------|-------------|---------|
| Mode | Oui | Présentiel / distanciel |
| Type d'atelier | Oui | Idéation, cadrage, roadmap, design sprint, rétro, co-création, test, service blueprint / user journey |
| Client / projet | Oui | Decathlon, projet Arena |
| Date de l'atelier | Oui | 2026-03-07 |
| Sujet / titre court | Oui | Service blueprint parcours client |
| Participants | Oui | Noms + rôles |
| Qu'est-ce qui se passe après l'atelier ? | Oui | Livrables attendus, décisions à prendre |
| Slides de facilitation disponibles ? | Non | Fichier local |

**Question clé** : "Qu'est-ce qui se passe après l'atelier ?" oriente l'emphase du debrief (si le livrable suivant est un prototype, on insiste sur les décisions design ; si c'est un comité, on insiste sur les arbitrages).

**Identification projet/client :**
Même pattern que `/debrief` étape 3 :
1. Lister les dossiers actifs dans le workspace (`projects/`, `sales/leads/`)
2. Matcher par nom de client ou mots-clés
3. Chercher dans Slite via `mcp__slite__search-notes` pour identifier la note parent du projet
4. Proposer le match trouvé, avec options : le match proposé, "Autre projet", "Pas de projet associé"
5. Si "Pas de projet associé", utiliser le channel personnel (`user-8eklmPPXu58_d5`)

> **Gate — Contexte validé**
> Présenter le résumé du contexte. Attendre confirmation avant de continuer.

### Étape 2 — Collecter et extraire les inputs

#### Mode présentiel (photos)

Consulter [references/photo-extraction-protocol.md](references/photo-extraction-protocol.md) pour le protocole complet.

Traiter les photos **une par une** avec validation interactive :

Pour chaque photo :
1. Lire l'image avec le tool `Read`
2. Extraire tout le contenu visible : texte des post-its, dessins, flèches, clusters, votes (gommettes, points), titres de colonnes/zones
3. Préserver les groupements spatiaux (les clusters comptent autant que le texte)
4. Présenter l'extraction à l'utilisateur via `AskUserQuestion` :
   - Contenu extrait, organisé par zone/cluster
   - Éléments incertains signalés avec `[?]`
   - Demander confirmation ou corrections

**Pourquoi une par une** : l'OCR sur écriture manuscrite est imparfait. Le facilitateur a le contexte pour corriger les erreurs et compléter ce que l'image ne montre pas.

#### Mode distanciel

- Screenshots ou PDF de whiteboard : traiter comme les photos (même protocole)
- Transcript (Granola ou fichier) : lire et extraire les échanges clés par exercice
- Les deux sources se complètent : le whiteboard montre les productions, le transcript montre les discussions

#### Slides de facilitation (optionnel)

Si des slides de facilitation existent, les lire pour comprendre la structure des exercices (consignes, objectifs de chaque activité, timing prévu). Ça aide à structurer l'étape 3.

> **Gate — Contenu brut complet validé**
> Confirmer que toutes les photos/sources ont été traitées et que l'utilisateur n'a rien à ajouter.

### Étape 3 — Structurer les productions par exercice

Identifier les exercices/activités du workshop à partir des inputs et les structurer :

Pour chaque exercice :
- **Nom de l'exercice** : tel que nommé par le facilitateur (ou reconstitué)
- **Objectif** : ce qu'on cherchait à produire
- **Participants/groupes** : qui a participé (sous-groupes si travail en parallèle)
- **Outputs structurés** : les productions organisées (idées, parcours, blueprints, matrices...)
- **Thèmes émergents** : patterns et regroupements qui ressortent
- **Votes/prioritisation** : si des votes ou dots ont été utilisés, les préserver avec les scores

Si les slides de facilitation ont été lues, les utiliser pour nommer les exercices et comprendre leur objectif.

> **Gate — Productions structurées validées**
> Présenter les productions structurées par exercice. Attendre confirmation.

### Étape 4 — Adapter les sections au type d'atelier

Charger [references/workshop-types.md](references/workshop-types.md) pour les sections spécifiques au type identifié à l'étape 1.

Types couverts : idéation, cadrage/alignment, roadmap, design sprint, rétro, co-création, test, service blueprint / user journey.

Le type a été classifié à l'étape 1, pas de re-confirmation nécessaire. Appliquer les sections adaptées automatiquement.

### Étape 5 — Extraire insights et décisions

À partir des productions structurées, extraire :

- **Décisions prises** : ce qui a été tranché pendant l'atelier
- **Insights clés** : ce qu'on a appris, surprises, patterns forts
- **Questions ouvertes** : sujets non résolus, débats non tranchés
- **Points de vigilance** : risques, tensions, sujets sensibles

**Important — output client-facing** :
- Pas de recommandations internes STFU
- Pas de "non-dits" ni d'observations off-record
- Tout ce qui est écrit est partageable tel quel avec le client
- Ton professionnel et factuel

> **Gate — Insights validés**
> Présenter les insights extraits. Le facilitateur a du contexte off-record qu'il peut ajouter ou retirer. Attendre confirmation.

### Étape 6 — Générer la note de debrief

Utiliser le template [assets/template-debrief.md](assets/template-debrief.md) comme structure de base.

**Structure universelle :**

1. **Métadonnées** : date, participants, type, durée, facilitateur
2. **TLDR** : 3-5 phrases résumant l'essentiel (décisions, productions clés, suites)
3. **Objectif de l'atelier** : ce qu'on cherchait à accomplir
4. **Déroulé** : séquence des exercices (tableau synthétique)
5. **Productions par exercice** : contenu détaillé de chaque exercice (étape 3)
6. **Synthèse et insights** : patterns transversaux, apprentissages (étape 5)
7. **Décisions** : liste des décisions prises
8. **Questions ouvertes** : sujets à trancher
9. **Actions** : tableau (action, responsable, deadline)
10. **Prochaines étapes** : ce qui se passe après l'atelier (informé par la question clé de l'étape 1)

**Adaptations par type** : appliquer les sections spécifiques de `workshop-types.md` (étape 4). Certains types ajoutent des sections (ex. service blueprint ajoute "Parcours cartographié"), d'autres modifient des sections existantes.

**Règles de rédaction :**
- Appliquer `stfu-writing` : pas de title case, pas de em-dash, mots simples, accents corrects
- Vérifier `glossary.md` pour les noms propres
- Client-facing : ton professionnel, partageable tel quel
- Verbatims pertinents entre guillemets avec attribution
- Quantifier quand possible (votes, nombre d'idées, temps passé)
- Pas de placeholders dans l'output final

> **Gate — Draft approuvé**
> Présenter le draft complet. Attendre validation avant publication.

### Étape 7 — Publier dans Slite

1. Appeler `mcp__slite__create-note` avec :
   - `title` : `WS - {YYYY-MM-DD} - {sujet}`
   - `parentNoteId` : l'ID de la note parent du projet identifié à l'étape 1
   - `markdown` : le contenu du debrief
2. Si pas de parent trouvé, utiliser le channel personnel (`user-8eklmPPXu58_d5`)

### Étape 8 — Résumé

Afficher dans le terminal :

```
Note publiée : {lien Slite}

Résumé :
- {N} exercices documentés
- {N} décisions prises
- {N} actions identifiées
- {N} questions ouvertes

Questions ouvertes :
- {Question 1}
- {Question 2}
```

## Règles clés

| Règle | Détail |
|-------|--------|
| **Client-facing** | Tout est partageable tel quel. Pas de section interne STFU. |
| **Photos une par une** | OCR manuscrit imparfait, validation interactive obligatoire. |
| **Groupements spatiaux** | Les clusters sur les photos comptent autant que le texte. |
| **stfu-writing** | Ton direct, mots simples, pas de title case, accents corrects. |
| **Glossaire** | Vérifier `glossary.md` pour les noms propres. |
| **Naming Slite** | `WS - {YYYY-MM-DD} - {sujet}` |
| **Gate avant publication** | Le draft complet est validé avant publication. |
| **Question clé** | "Qu'est-ce qui se passe après ?" oriente l'emphase du debrief. |

## Gestion des cas limites

| Cas | Comportement |
|-----|-------------|
| Photos floues ou illisibles | Signaler les zones illisibles, demander à l'utilisateur de compléter |
| Pas de photos / pas de matière | Proposer de travailler depuis les notes du facilitateur ou le transcript |
| Atelier avec sous-groupes | Structurer les productions par groupe, puis synthèse transverse |
| Workshop multi-jours | Un debrief par jour ou un debrief consolidé (demander à l'utilisateur) |
| Type d'atelier non listé | Utiliser la structure universelle, adapter les sections manuellement |
| Pas de match projet Slite | Créer dans le channel personnel, signaler qu'il faudra peut-être déplacer |
| Mélange présentiel/distanciel | Traiter les deux types de sources avec leurs protocoles respectifs |

## Note Mural API (référence future)

L'API Mural supporte l'upload d'images et la création de widgets avec positionnement. Un skill dédié "workshop-to-mural" pourrait s'appuyer sur le debrief produit ici pour créer un board Mural structuré. Hors scope de ce skill.

## Ressources

- Protocole d'extraction photo : [references/photo-extraction-protocol.md](references/photo-extraction-protocol.md)
- Sections par type d'atelier : [references/workshop-types.md](references/workshop-types.md)
- Template debrief : [assets/template-debrief.md](assets/template-debrief.md)
- Règles d'écriture : `stfu-writing`
- Glossaire : `glossary.md`

## Exemples d'invocation

```
/workshop-debrief
→ Demande le mode, le type, le contexte, puis guide l'extraction et la publication

/workshop-debrief service blueprint decathlon
→ Pré-remplit le type (service blueprint) et le client (Decathlon)

/workshop-debrief
(depuis un dossier projet avec des photos)
→ Détecte le projet, propose de traiter les photos du dossier
```
