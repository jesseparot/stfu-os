# CLAUDE.md

Ce fichier guide Claude Code (claude.ai/code) dans ce dépôt.

## Contexte

Workspace de **Start The F*** Up (STFU)**, studio de conseil en innovation. Lire `stfu-context.md` pour le contexte complet.

**Philosophie centrale — La Soute vs Le Pont** (cf. `_workspace/internal/studio-os-roadmap.md`) :
- **La Soute** (territoire IA) : productions commoditisées (recherche, rapports, slides, analyse de données). Cible : 90% de réduction du temps.
- **Le Pont** (territoire humain) : jugement à haute valeur (stratégie, influence des parties prenantes, go/no-go). Cible : 80%+ du temps humain ici.

Quand tu produis un livrable, demande-toi : Soute (automatiser) ou Pont (appuyer le jugement humain) ?

## Ton et style

- Direct, sans bullshit — fidèle à la marque STFU
- Business-first : toujours rattacher les recommandations à la valeur/ROI
- Orienté action : biais pour l'exécution plutôt que la planification
- Français pour tous les contenus et les livrables clients, sauf si anglais spécifié
- **Règles d'écriture** : skill `stfu-writing` appliqué automatiquement — voir `skills/stfu-writing/SKILL.md`
- **Noms propres** : toujours vérifier `glossary.md` pour les orthographes exactes (TotalEnergies, IDEMIA, CHANEL, etc.)

## Emplacements clés

| Fonction | Chemin |
|----------|--------|
| Contexte entreprise | `stfu-context.md` |
| **Conventions (source de vérité)** | `conventions.md` |
| Glossaire / noms propres | `glossary.md` |
| Guides partenaires | `tuto/` |
| Configuration secrets | `tuto/secrets-setup.md` |
| Catalogue de skills | `.claude/skills/_index.md` |
| Projets (local) | `_workspace/projects/{client}-{sujet}/` |
| AO en cours | `_workspace/sales/appels-d-offres/{organisme}-{sujet}-{YY-MM}/` |
| Leads | `_workspace/sales/leads/{entreprise}-{contact}-{sujet}/` |
| Outbound | `_workspace/sales/outbound/` |
| Templates (migration vers Slite) | `_workspace/templates/` |
| Méthodologies (migration vers Slite) | `_workspace/methodologies/` |
| Docs stratégie OS | `_workspace/internal/` |
| Inbox (zone de dépôt) | `_workspace/_inbox/` |
| Archive | `_workspace/_archive/` |

## Conventions de nommage

Source de vérité : `conventions.md`. Référence rapide :

- **Dossiers** : minuscules, tirets, pas d'espaces
- **Projets** : `{client}-{sujet}` (recommande)
- **Documents brouillon** : `type-sujet_draft.md`
- **Documents finaux** : `type-sujet_final.md`
- **Transcripts** : `YYYY-MM-DD-type-sujet.md`
- **CR** : `cr-YYYY-MM-DD-sujet.md`
- **AO** : `{organisme}-{sujet}-{YY-MM}`

## Sources de données et intégrations MCP

Ce workspace utilise des outils cloud comme sources de vérité pour le contenu, accessibles via MCP :

| Outil | Usage | Utilisé par |
|-------|-------|-------------|
| **Slite** | Docs internes, méthodologies, playbooks | `/debrief`, methode-beta-gouv, référence générale |
| **Airtable** | Base de missions, références passées, pipeline | `/appel-d-offres` (recherche de missions passées) |
| **Granola** | Transcripts et notes de réunion | `debrief` (skill user-level — récupère les transcripts, génère les CR) |
| **Google Drive** | Fichiers clients, livrables, propositions, docs partagés | `stfu-drive` (navigation du Drive STFU Team) |

Quand un skill a besoin de méthodologie ou de données de référence, interroger le MCP concerné plutôt que de chercher des copies locales. Le repo contient la **couche outil** (skills, config, conventions) ; les outils cloud contiennent la **couche contenu** (docs, données, travail client).

## Skills disponibles

| Skill | Déclenchement | Description |
|-------|---------------|-------------|
| `/project-init` | Manuel | Initialiser un projet (dossier local, manifest, Slite, Drive) |
| `/appel-d-offres` | Manuel | Analyser et briefer un appel d'offres |
| `/propale` | Manuel | Rédiger une proposition commerciale (framework McKinsey 8 sections) |
| `/organize-file` | Manuel | Organiser les fichiers depuis l'inbox |
| `/user-test-restitution` | Manuel | Générer des documents de restitution de tests utilisateurs |
| `stfu-writing` | Auto | Règles de style d'écriture appliquées à tout le contenu |
| `methode-beta-gouv` | Auto | Méthodologie de coaching beta.gouv (phases, AARRI, posture) |
| `qualify` | Auto | Impose la qualification du livrable avant toute production substantielle |
| `stfu-drive` | Auto | Naviguer et gérer le Google Drive STFU Team |
| `oracle` | Auto | Recherche approfondie via Gemini + stress-test en second avis |
| `mermaid-stfu` | Auto | Diagrammes Mermaid brandés — palette grise + accent #FFE200, Lato, commandes d'export |
| `/mission-to-outbound` | Manuel | Générer un plan de prospection outbound à partir d'une mission STFU |
| `/case-study-slide` | Manuel | Générer une présentation Google Slides case study à partir d'une mission Airtable |
| `/list-gen` | Manuel | Générer et enrichir des listes de prospects — brief, Sales Nav, Evaboot, Dropcontact, Drive/Lemlist |
| `stfu-slides` | Auto + `/stfu-slides` | Design engine Google Slides brandées — layout, typo, compositions custom, self-review visuel |
| `/clean-workspace` | Manuel | Scan et nettoyage du workspace — brouillons anciens, scratch, orphelins, cross-check Slite/Drive |

Catalogue complet : `.claude/skills/_index.md`

## Workflows

### Nouvel appel d'offres

1. Déposer le DCE dans `_workspace/_inbox/` ou `_workspace/sales/appels-d-offres/{organisme}-{sujet}-{YY-MM}/`
2. Lancer `/appel-d-offres` pour générer le brief (recherche de missions de référence dans Airtable)
3. Décision : go/no-go noté dans le README

### Nouveau lead

1. Créer `_workspace/sales/leads/{entreprise}-{contact}-{sujet}/`
2. Créer un README.md avec les infos du lead (contexte, contacts, prochaines étapes)

### Lead converti en client

1. Lancer `/project-init` (cree dossier local, manifest, Slite, Drive)
2. Deplacer le lead vers `_workspace/_archive/` ou supprimer

### Après fin de mission

1. Capitaliser dans Airtable (via `/mission-airtable`)
2. Deplacer `_workspace/projects/{name}/` vers `_workspace/_archive/`

### Debrief de réunion

1. Lancer `/debrief` après une réunion (skill user-level — nécessite Granola + Apple Reminders)
2. Le skill récupère le transcript depuis Granola, identifie le contexte projet
3. Génère un CR structuré et le publie sur Slite

### Proposition commerciale

1. S'assurer que le contexte existe (dossier lead ou projet)
2. Lancer `/propale` — collecte le brief, recherche les missions Airtable, qualifie le livrable
3. Valider l'outline de l'approche (mode two-pass recommandé)
4. Draft produit dans `propale-{sujet}_draft.md`
5. `/stfu-slides` pour la version Google Slides
6. Upload Drive dans le dossier client

### Organisation des fichiers

`/organize-file` sur les fichiers dans `_workspace/_inbox/` :
- Détecte le type et le client/projet associé
- Renomme selon les conventions
- Déplace vers l'emplacement approprié

## Production de livrables

- Vérifier `_workspace/templates/` d'abord pour les structures existantes (migration vers Slite)
- Référencer les projets similaires passés dans Airtable
- Vérifier `glossary.md` pour l'orthographe des noms propres
- Inclure des résultats quantifiés quand c'est possible (€, %, utilisateurs, temps économisé)
- Garder les résumés exécutifs sous 3 paragraphes

## Direction architecturale (v2)

Le workspace est un repo Git partagé (`stfu-os`) pour la couche outil, avec le contenu dans les outils cloud. Principe clé : Git = comment on travaille (skills, config, conventions). Cloud = sur quoi on travaille (docs, données, livrables clients). `_workspace/` est la zone de transition locale — le contenu migre vers le cloud au fur et à mesure que les outils mûrissent.
