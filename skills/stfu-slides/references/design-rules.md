# Design Rules — stfu-slides v2

Référence complète des règles de design pour les présentations Google Slides STFU.

---

## Palette du thème

### Couleurs principales (hex + RGB API format 0-1)

| Slot | Hex | RGB API | Usage |
|------|-----|---------|-------|
| dk1 | `#000000` | `{"red": 0, "green": 0, "blue": 0}` | Texte principal, titres |
| lt1 | `#FFFFFF` | `{"red": 1, "green": 1, "blue": 1}` | Fond, texte sur fond sombre |
| dk2 / body | `#434343` | `{"red": 0.263, "green": 0.263, "blue": 0.263}` | Body text de-emphasized |
| lt2 | `#F3F3F3` | `{"red": 0.953, "green": 0.953, "blue": 0.953}` | Gris très clair |
| accent1 | `#FFF000` | `{"red": 1, "green": 0.941, "blue": 0}` | Jaune vif — carré accent layouts |
| accent2 / STFU | `#FFE200` | `{"red": 1, "green": 0.886, "blue": 0}` | Jaune STFU — accent marque |
| accent3 | `#379634` | `{"red": 0.216, "green": 0.588, "blue": 0.204}` | Vert (validation) |
| accent4 | `#D00000` | `{"red": 0.816, "green": 0, "blue": 0}` | Rouge (warning) |
| accent5 | `#AFAFAF` | `{"red": 0.686, "green": 0.686, "blue": 0.686}` | Gris moyen |
| accent6 | `#7A7A7A` | `{"red": 0.478, "green": 0.478, "blue": 0.478}` | Gris foncé |

### Règles d'usage des couleurs

- **Accent #FFE200 porte du sens** — pas de décoration. Cohérent avec mermaid-stfu.
- **Fond par défaut** : blanc (#FFFFFF). Dividers/covers : noir (#000000) ou jaune (#FFE200).
- **Pas d'autres couleurs** sauf vert/rouge pour validation/warning ponctuel.

---

## Typographie — hiérarchie 5 niveaux

### Les 5 rôles

| Rôle | Font family | Weight | Taille | Couleur | Casse |
|------|-------------|--------|--------|---------|-------|
| Title | Playfair Display | Black (900) | 24pt | #000000 | Phrase (JAMAIS tout en majuscules) |
| Subtitle | Lato | Regular (400) | 10pt | #7A7A7A | Phrase (usage rare) |
| Annotation | Lato | Regular (400) | 8pt | #7A7A7A | MAJUSCULES |
| Heading | Lato | *selon emphasis* | 12pt | *selon emphasis* | Phrase |
| Body | Lato | *selon emphasis* | 8pt | *selon emphasis* | Phrase |

### Système d'emphasis

Heading et Body ont deux modes :

| Mode | Weight | Couleur | API `bold` | API `foregroundColor` |
|------|--------|---------|------------|----------------------|
| **Emphasized** | Black (900) | #000000 (dk1) | `true` | `{"red": 0, "green": 0, "blue": 0}` |
| **De-emphasized** | Regular (400) | #434343 (dk2) | `false` | `{"red": 0.263, "green": 0.263, "blue": 0.263}` |

**Règle de décision par slide** :
- **Message-driven** (insight, recommandation, point de vue) → heading emphasized, body de-emphasized
- **Data-driven** (chiffres, métriques, comparaison) → heading de-emphasized, body emphasized
- **Par défaut** → heading emphasized, body de-emphasized

### Titre sur fond sombre

Quand la slide a un fond noir ou foncé, le titre passe en blanc :
- Font : Playfair Display Black, 24pt
- Couleur : #FFFFFF (`{"red": 1, "green": 1, "blue": 1}`)

### Font weight 900 (Black)

L'API Google Slides n'expose que `bold: true` (= weight 700). Pour obtenir Black (900), utiliser `fontFamily: "Lato Black"` ou `fontFamily: "Playfair Display Black"`. Si le rendu n'est pas correct, fallback sur `bold: true` avec le nom de famille standard.

### Point critique : fonts par défaut

Le `fontScheme` du thème dit "Arial" en fallback. Tout texte inséré via `createShape` + `insertText` SANS `updateTextStyle` explicite sera en **Arial 14pt**.

**Règle absolue** : toujours appliquer `updateTextStyle` après `insertText` sur tout élément créé via API. Seuls les placeholders hérités des layouts (titre, body) portent automatiquement la bonne font.

---

## Grille — dual margin modes

### Modes de marge

| Mode | px | EMU | usable_width (EMU) | Quand |
|------|-----|------|-------------------|-------|
| **Compact** | 16 | 152,400 | 8,839,200 | 4+ blocs, contenu dense |
| **Spacious** | 40 | 381,000 | 8,382,000 | 1-3 blocs, mise en page aérée |

Calculer les positions via `grid_calc.py --margin compact|spacious`. Les flags `--x-start`/`--x-end` overrident le mode quand spécifiés.

### Positions de référence

| Élément | x (EMU) | y (EMU) | largeur (EMU) | hauteur (EMU) |
|---------|---------|---------|---------------|----------------|
| Canvas | 0 | 0 | 9,144,000 | 5,143,500 |
| Carré jaune accent | 0 | 379,215 | 228,600 | 205,800 |
| Ligne séparatrice | 0 | 584,955 | 9,151,500 | 0 |
| Zone titre | 228,600 | 205,740 | 8,686,800 | 572,700 |
| Zone body | 228,600 | 915,570 | 8,686,800 | 4,022,100 |
| N° de page | 8,595,308 | 4,838,672 | 548,700 | 338,700 |

### Zones verticales

| Zone | Début (EMU) | Fin (EMU) | Utile (EMU) |
|------|-------------|-----------|-------------|
| Sous titre | 915,570 | 4,738,000 | 3,822,430 |
| Pleine page | 205,740 | 4,738,000 | 4,532,260 |

### Clearance titre / contenu

Le titre Playfair Display Black à 24pt a une hauteur de ligne d'environ 380,000 EMU.

| Lignes titre | Bottom titre (y=300,000) | Body start min |
|-------------|--------------------------|----------------|
| 1 ligne | 680,000 | 830,000 |
| 2 lignes | 1,060,000 | 1,210,000 |
| 3 lignes | INTERDIT — reformuler | — |

Pour les layouts avec placeholder : le placeholder gère la clearance automatiquement.

### Conversions utiles

- 1 pt = 12,700 EMU
- 1 cm = 360,000 EMU

---

## Styles de tables

### Table style 1 — standard (fond blanc)

- Header : fond #000000, texte #FFFFFF, Lato Bold 11pt
- Lignes : fond alternant #FFFFFF / #F3F3F3, texte #434343, Lato Regular 10pt
- Bordures : #E0E0E0, 0.5pt

### Table style 2 — sombre (fond noir)

- Header : fond #FFE200, texte #000000, Lato Bold 11pt
- Lignes : fond alternant #1A1A1A / #2A2A2A, texte #FFFFFF, Lato Regular 10pt
- Bordures : #434343, 0.5pt

### Table style 3 — accent (highlight une ligne)

- Comme style 1, mais la ligne à mettre en avant a fond #FFE200, texte #000000

### Table style 4 — minimal (sans bordures visibles)

- Pas de header visuel distinct
- Lignes : fond transparent, texte #434343, Lato Regular 11pt
- Séparateurs : ligne horizontale #E0E0E0, 0.5pt entre chaque ligne

---

## Limitations API Google Slides

### autofit (TEXT_AUTOFIT / SHAPE_AUTOFIT)

L'API Slides **ne supporte PAS** l'écriture de `autofitType` autre que `NONE`. `TEXT_AUTOFIT` et `SHAPE_AUTOFIT` sont en **lecture seule** — ils ne peuvent être activés que manuellement dans l'UI Google Slides.

**Conséquence** : quand un titre ou un body risque de déborder, on ne peut pas compter sur l'API pour réduire la police automatiquement. Stratégies de contournement :

1. **Réduire la police manuellement** via `updateTextStyle` si le texte est long
2. **Agrandir la box** via `updatePageElementTransform` (scaleY) pour contenir le texte
3. **Utiliser des layouts avec placeholders** : les placeholders hérités des layouts ont le autofit configuré par défaut dans le template
4. **Éviter les titres longs** (max ~60 caractères en Playfair 24pt)

### contentAlignment

`contentAlignment` (TOP, MIDDLE, BOTTOM) **est writable** via `updateShapeProperties` :

```json
{
  "updateShapeProperties": {
    "objectId": "<ID>",
    "shapeProperties": {"contentAlignment": "TOP"},
    "fields": "contentAlignment"
  }
}
```

Usage recommandé : TOP pour les bodies, MIDDLE pour les blocs courts.

---

## Anti-patterns

- Rainbow colors — jamais
- Icônes décoratives sans fonction — les icônes fonctionnelles (différencier des catégories, marquer des blocs) sont OK en monochrome noir. Pas de clip art, pas d'icônes colorées.
- Accent (#FFE200) sans signification sémantique
- Wall-of-text (> 8 lignes de body sur une slide)
- Plus de 3 niveaux de hiérarchie typographique sur une même slide
- Texte < 8pt
- Images en couleur (toujours N&B)
- Ombres portées, gradients, effets 3D
- Calcul mental des positions EMU — toujours utiliser `grid_calc.py`
- Slide sans élément visuel (pas de content blocks, pas d'icône, pas d'accent, pas de stat callout, pas de note coach)
