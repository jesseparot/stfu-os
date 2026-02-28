# Slide Types — stfu-slides v2

4 compositions dynamiques. Les positions sont calculées via `grid_calc.py`, pas codées en dur.

---

## 1. Content standard (titre + texte)

**Layout** : `g386b92f88e9_0_24` (Titre + contenu) — carré jaune + ligne + body placeholder
**Usage** : slide avec titre et texte structuré (paragraphes ou bullets)

### Process

1. `createSlide` avec layout 1, mapper TITLE et BODY placeholders
2. `insertText` dans le titre et le body
3. Pas de `updateTextStyle` nécessaire — les placeholders héritent les fonts du layout

### Pattern

```json
[
  {
    "createSlide": {
      "objectId": "slide_content_001",
      "slideLayoutReference": {"layoutId": "g386b92f88e9_0_24"},
      "placeholderIdMappings": [
        {"layoutPlaceholder": {"type": "TITLE"}, "objectId": "title_001"},
        {"layoutPlaceholder": {"type": "BODY"}, "objectId": "body_001"}
      ]
    }
  },
  {"insertText": {"objectId": "title_001", "text": "Titre de la slide"}},
  {"insertText": {"objectId": "body_001", "text": "Contenu body ici..."}}
]
```

---

## 2. Title + N blocks (colonnes)

**Layout** : `g386b92f88e9_0_84` (Titre ligne) — titre placeholder + zone libre pour contenu
**Usage** : comparaison, arguments, métriques, blocs structurés côte à côte

### Process

1. `createSlide` avec layout 3 (Titre ligne), mapper TITLE placeholder
2. `insertText` dans le titre
3. Choisir le margin mode : `compact` (4+ blocs) ou `spacious` (1-3 blocs)
4. Calculer les colonnes : `python3 grid_calc.py columns N --margin <mode>`
5. Pour chaque bloc, créer un TEXT_BOX avec le contenu structuré (annotation + heading + body)
6. Appliquer le styling via `updateTextStyle` avec FIXED_RANGE pour chaque segment

### Structure d'un content block

Chaque bloc suit la structure annotation → heading → body dans un seul TEXT_BOX :

```
ANNOTATION\n
Heading text\n
Body text avec les détails, les bullets, les données.
```

Styler avec FIXED_RANGE :
- Annotation (première ligne) : Lato Regular 8pt #7A7A7A, MAJUSCULES côté texte
- Heading (deuxième ligne) : Lato 12pt, emphasis selon la décision slide
- Body (reste) : Lato 8pt, emphasis inverse du heading

### Positionnement

Les positions x et largeurs viennent de `grid_calc.py columns N`. La hauteur des text boxes = zone body utile (y_start = 915,570, y_end = 4,738,000 → h = 3,822,430 EMU). Le texte se place naturellement en haut de la box avec `contentAlignment: TOP`.

---

## 3. Statement / key insight

**Layout** : `g386b92f88e9_0_73` (Titre carré jaune) ou `g386b92f88e9_0_93` (Titre nu)
**Usage** : phrase d'accroche, insight clé, citation stratégique, recommandation

### Process

1. `createSlide` avec layout 2 (Titre carré jaune) ou layout 4 (Titre nu), mapper TITLE
2. `insertText` dans le titre
3. Optionnel : ajouter un subtitle via `createShape` TEXT_BOX, style Subtitle (Lato Regular 10pt #7A7A7A)

### Pattern

```json
[
  {
    "createSlide": {
      "objectId": "slide_statement_001",
      "slideLayoutReference": {"layoutId": "g386b92f88e9_0_73"},
      "placeholderIdMappings": [
        {"layoutPlaceholder": {"type": "TITLE"}, "objectId": "title_statement_001"}
      ]
    }
  },
  {"insertText": {"objectId": "title_statement_001", "text": "L'insight clé qui change tout."}}
]
```

---

## 4. Cover / section divider

**Layout** : `g386b92f88e9_0_46` (Vide) — tout via API
**Usage** : page de garde, séparation de section, slide d'impact

### Process

1. `createSlide` avec layout 5 (Vide)
2. `updatePageProperties` pour le fond (noir, jaune, ou garder blanc)
3. Créer le titre via `createShape` TEXT_BOX, centré
4. Appliquer le style Title (Playfair Display Black 24pt), blanc si fond sombre
5. Optionnel : subtitle, date/contexte

### Variantes de fond

| Variante | Background | Titre couleur | Subtitle couleur |
|----------|-----------|---------------|-----------------|
| Cover noir | #000000 | #FFFFFF | #AFAFAF |
| Cover jaune | #FFE200 | #000000 | #434343 |
| Section divider blanc | (défaut) | #000000 | #7A7A7A |

### Positionnement titre (cover)

- Title text box : x = marge spacious (381,000), y = centré vertical (~2,000,000), largeur = 8,382,000
- Subtitle : sous le titre, ~500,000 EMU plus bas
- Pas de grid_calc.py nécessaire pour les covers — positionnement centré simple

---

## Récapitulatif des layouts

| Layout | layoutId | Nom | Décoration | Body placeholder | Compositions |
|--------|----------|-----|------------|-----------------|--------------|
| 1 | `g386b92f88e9_0_24` | Titre + contenu | Carré jaune + ligne | Oui | Content standard |
| 2 | `g386b92f88e9_0_73` | Titre carré jaune | Carré jaune + ligne | Non | Statement |
| 3 | `g386b92f88e9_0_84` | Titre ligne | Ligne seule | Non | Title + N blocks |
| 4 | `g386b92f88e9_0_93` | Titre | Aucune | Non | Statement (alt) |
| 5 | `g386b92f88e9_0_46` | Vide | Aucune | Non | Cover / divider |
