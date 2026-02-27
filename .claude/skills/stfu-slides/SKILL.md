---
name: stfu-slides
description: Design engine pour Google Slides brandées STFU. Appliqué automatiquement quand on crée des slides ou des présentations multi-slides. Gère le choix de layout, l'insertion de contenu, le styling typographique, les compositions custom, et le self-review visuel via thumbnails. Utiliser pour créer un deck, une présentation, des slides stratégiques, une proposition, une restitution. Ne couvre PAS les case studies simples (1 slide) — déléguer à /case-study-slide.
---

# stfu-slides v2 — Content-first draft engine

## Philosophie

**Content-first draft** : Claude produit le contenu et le layout. Le coach finit le design, les diagrammes, les images, et ajuste la copy.

- Pas de pixel-perfect automation — un brouillon structuré que le coach complète
- Priorité au contenu lisible et bien organisé
- Diagrammes, images, et layouts complexes : laisser au coach
- 4 compositions dynamiques au lieu de 11 types rigides
- Self-review adversarial : le premier rendu n'est jamais correct. Chercher les bugs, pas confirmer le succès.

## Quand ce skill s'active

- Création de présentations multi-slides (decks, propositions, restitutions, ateliers)
- Toute demande de slides stratégiques brandées STFU
- Quand un autre skill a besoin de produire des slides (sauf case study simple)

## Quand NE PAS utiliser

- **Case study simple (1 slide)** : utiliser `/case-study-slide`
- **Diagrammes complexes** : utiliser `mermaid-stfu` pour générer un PNG, puis l'insérer manuellement
- **Arc narratif** : ce skill gère le design, pas la structure narrative

---

## Configuration

| Paramètre | Valeur |
|-----------|--------|
| Template ID | `1ZyT0oZMRaI9HRg1kcluh1rgWWBhywvfJCJPPTogFsUg` |
| Template nom | Template4Claude Slides STFU |
| Dossier slides Drive | `1eh7-oNGzjzRDa-LFvK_9pFv9b963MDyu` |
| Email utilisateur | `$GOOGLE_USER_EMAIL` (résoudre via `echo $GOOGLE_USER_EMAIL` en Bash) |
| Page size | 9,144,000 x 5,143,500 EMU (16:9) |

---

## Process

### Step 0 — Content analysis

Avant de toucher à l'API, identifier pour chaque slide :
- Le message principal (1 phrase)
- Le nombre de blocs de contenu
- Le type de composition (voir layout decision tree)
- L'emphasis : message-driven (heading emph) ou data-driven (body emph)
- L'élément visuel : quel élément différencie cette slide du texte brut ? (content blocks structurés, icône fonctionnelle, accent jaune sémantique, stat callout, ou note coach pour image/diagramme)

### Step 1 — Source decision

Pour chaque slide, décider :
1. **Slide existante à modifier** → `get_presentation`, identifier la slide, modifier via batch_update
2. **Nouveau layout depuis template** → continuer au step 2
3. **Slide from scratch** → continuer au step 2

### Step 2 — Copy template (si nouveau deck)

```
mcp__google-workspace__copy_drive_file(
  user_google_email=<EMAIL>,
  file_id="1ZyT0oZMRaI9HRg1kcluh1rgWWBhywvfJCJPPTogFsUg",
  new_name="<Nom de la présentation>",
  parent_folder_id="1eh7-oNGzjzRDa-LFvK_9pFv9b963MDyu"
)
```

Puis supprimer les slides placeholder via `get_presentation` + `deleteObject`.

### Step 3 — Create slides

Pour chaque slide :

1. **Margin mode** : `compact` (4+ blocs) ou `spacious` (1-3 blocs)
2. **Positions** : `python3 grid_calc.py columns N --margin <mode>` — TOUJOURS calculer, jamais deviner les EMU
3. **Layout** : choisir via le layout decision tree ci-dessous
4. **Contenu** : `createSlide` → `insertText` → `updateTextStyle` (si éléments custom)

**CRITIQUE** : toujours appliquer `updateTextStyle` sur tout texte créé via `createShape`. Sans styling explicite, le texte sera en Arial 14pt.

### Step 4 — Emphasis decision

Par slide, décider du mode d'emphasis :

| Slide type | Heading | Body |
|-----------|---------|------|
| Message-driven (insight, recommandation) | **Emphasized** (Black #000) | De-emphasized (Regular #434343) |
| Data-driven (chiffres, métriques) | De-emphasized (Regular #434343) | **Emphasized** (Black #000) |
| Par défaut | **Emphasized** | De-emphasized |

### Step 5 — Self-review (fix-and-verify)

**Assume qu'il y a des problèmes. Ton job est de les trouver.**

Après chaque slide ou max 2 slides :

1. `get_page_thumbnail` (LARGE) → `WebFetch` avec le **prompt d'inspection structuré** de `references/visual-inspection-prompt.md`
2. **Lister les problèmes trouvés** — si aucun trouvé, re-inspecter plus critiquement (un premier passage propre est suspect)
3. **Fix** chaque problème via batch_update
4. **Re-vérifier les slides affectées** — un fix crée souvent un nouveau problème (décalage d'indices, chevauchement, font reset)
5. Répéter jusqu'à un passage complet sans nouveau problème
6. **Ne pas déclarer le succès avant au moins un cycle fix-and-verify**

Max 3 itérations par slide. Fallback si thumbnails KO : export PDF via `get_drive_file_download_url` + `Read`.

### Step 6 — Deliver

**Pré-condition** : toutes les slides ont passé au moins un cycle fix-and-verify (Step 5).

Communiquer :
- Lien vers la présentation
- Nombre de slides créées
- Résumé du contenu par slide
- Problèmes trouvés et corrigés pendant le QA (transparence)
- Points à finaliser par le coach (images, diagrammes, ajustements)

---

## Layout decision tree

```
├── Titre + texte structuré (paragraphes, bullets) ?
│   → Content standard (layout 1) — body placeholder inclus
│
├── Titre + N blocs côte à côte (colonnes, comparaison, métriques) ?
│   → Title + N blocks (layout 3) — titre placeholder + colonnes via grid_calc.py
│
├── Statement / accroche / insight clé, peu ou pas de body ?
│   → Statement (layout 2 ou 4) — titre seul, proéminent
│
└── Cover / section divider / slide d'impact ?
    → Cover (layout 5) — fond custom + titre via API
```

---

## Design rules (résumé)

Détails complets dans `references/design-rules.md`.

### Typographie — 5 niveaux

| Rôle | Font | Size | Couleur | Casse |
|------|------|------|---------|-------|
| Title | Playfair Display Black | 24pt | #000000 | Phrase (JAMAIS majuscules) |
| Subtitle | Lato Regular | 10pt | #7A7A7A | Phrase |
| Annotation | Lato Regular | 8pt | #7A7A7A | MAJUSCULES |
| Heading | Lato (emphasis) | 12pt | (emphasis) | Phrase |
| Body | Lato (emphasis) | 8pt | (emphasis) | Phrase |

### Emphasis

- **Emphasized** : Bold/Black + #000000
- **De-emphasized** : Regular + #434343

### Marges

| Mode | EMU | Usage |
|------|-----|-------|
| Compact | 152,400 | 4+ blocs, dense |
| Spacious | 381,000 | 1-3 blocs, aéré |

---

## Content block structure

Un content block = annotation + heading + body dans un TEXT_BOX unique.

```
ANNOTATION\n          → Lato 8pt #7A7A7A, MAJUSCULES
Heading text\n        → Lato 12pt, emphasis selon décision slide
Body details here.    → Lato 8pt, emphasis inverse du heading
```

Styler par segments via `updateTextStyle` avec `FIXED_RANGE`. Voir `references/batch-update-patterns.md` pour le pattern complet.

### Variante avec icône

Pour les slides Title + N blocks où les blocs représentent des catégories distinctes, ajouter une icône fonctionnelle monochrome au-dessus de l'annotation via `createImage`. Voir `references/batch-update-patterns.md` § createImage pour le pattern et la liste d'icônes disponibles.

---

## Content limits

| Métrique | Idéal | Max |
|----------|-------|-----|
| Blocs par slide | 3 | 6 |
| Bullets par bloc | 3 | 5 |
| Lignes de body par slide | 6 | 8 |
| Lignes de titre | 1 | 2 (reformuler si 3+) |

Si ça déborde → couper en 2 slides.

---

## Visual element par slide

Chaque slide doit contenir au moins un élément visuel qui la distingue du texte brut.

| Élément | Quand | Comment |
|---------|-------|---------|
| Content blocks structurés | Slide avec 2+ points distincts | `createShape` en colonnes via `grid_calc.py` |
| Icône fonctionnelle | Blocs = catégories à différencier | `createImage` monochrome noir (voir batch-update-patterns.md) |
| Accent jaune sémantique | Stat clé, donnée saillante | Rectangle #FFE200 ou fond highlight |
| Stat callout | Chiffre d'impact à mettre en avant | Texte large (18-24pt) + annotation contexte |
| Note coach | Image, diagramme, ou visuel attendu | `[COACH : insérer ici — description du visuel attendu]` |

**Règle** : si aucun élément visuel identifié au Step 0 → ajouter une note coach `[COACH : insérer ici — description du visuel attendu]` dans un text box gris lt2.

---

## Layouts disponibles

| Layout | layoutId | Nom | Composition |
|--------|----------|-----|-------------|
| 1 | `g386b92f88e9_0_24` | Titre + contenu | Content standard |
| 2 | `g386b92f88e9_0_73` | Titre carré jaune | Statement |
| 3 | `g386b92f88e9_0_84` | Titre ligne | Title + N blocks |
| 4 | `g386b92f88e9_0_93` | Titre | Statement (alt) |
| 5 | `g386b92f88e9_0_46` | Vide | Cover / divider |

Les layout IDs sont stables entre le template original et ses copies.

---

## Outils

### `tools/grid_calc.py`

Calculateur de positions EMU. **Toujours lancer AVANT de construire les batch_update requests.** Jamais de calcul mental des EMU.

```bash
# Colonnes avec margin mode
python3 tools/grid_calc.py columns 3 --margin compact
python3 tools/grid_calc.py columns 2 --margin spacious

# Lignes (sous titre ou pleine page)
python3 tools/grid_calc.py rows 4
python3 tools/grid_calc.py rows 3 --full-page

# Grille NxM
python3 tools/grid_calc.py grid 3x2 --margin compact

# Body start (clearance titre sur layout Vide)
python3 tools/grid_calc.py body-start 55 --font-size 24

# Override marges (valeurs absolues)
python3 tools/grid_calc.py columns 2 --x-start 228600 --x-end 8915400
```

Chemin : `.claude/skills/stfu-slides/tools/grid_calc.py`

---

## Registre de templates

| Template | ID | Usage |
|----------|----|----|
| Template4Claude Slides STFU | `1ZyT0oZMRaI9HRg1kcluh1rgWWBhywvfJCJPPTogFsUg` | Decks multi-slides (ce skill) |
| Case Study template | `1lTiuH1X-X4XyMta0aHsqAV2vrhYbAgEyK4G-_hX4ptY` | Case study 1 slide (`/case-study-slide`) |

---

## Interaction avec d'autres skills

| Skill | Relation |
|-------|----------|
| `/case-study-slide` | Case studies simples (1 slide). Indépendant de ce skill. |
| `mermaid-stfu` | Partage la philosophie d'accent (#FFE200 = sens). Exports PNG/SVG insérables manuellement. |
| `stfu-writing` | Appliqué au contenu textuel des slides |
| `stfu-drive` | Navigation Drive pour fichiers existants |
| `glossary.md` | Vérifier les noms propres avant insertion |

---

## Fichiers de référence

| Fichier | Contenu |
|---------|---------|
| `references/design-rules.md` | Palette, typo 5 niveaux, emphasis, marges, anti-patterns |
| `references/slide-types.md` | 4 compositions dynamiques avec process et patterns |
| `references/batch-update-patterns.md` | Patterns JSON pour l'API (layouts, texte, content blocks, icônes, fonds) |
| `references/visual-inspection-prompt.md` | Prompt structuré pour le self-review visuel (Step 5) |
| `tools/grid_calc.py` | Calculateur de positions (colonnes, lignes, grilles, body-start, margin modes) |
