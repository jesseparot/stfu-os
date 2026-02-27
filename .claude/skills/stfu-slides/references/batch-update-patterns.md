# Batch Update Patterns — stfu-slides v2

Patterns JSON pour l'API Google Slides via `mcp__google-workspace__batch_update_presentation`.

> **Limitation API** : `TEXT_AUTOFIT` et `SHAPE_AUTOFIT` ne sont PAS writable via l'API.
> Seul `NONE` est supporté. Ne JAMAIS inclure `autofitType` dans les batch_update requests.

---

## createSlide — les 5 layouts

### Layout 1 — Titre + contenu (g386b92f88e9_0_24)

```json
{
  "createSlide": {
    "objectId": "slide_001",
    "slideLayoutReference": {"layoutId": "g386b92f88e9_0_24"},
    "placeholderIdMappings": [
      {"layoutPlaceholder": {"type": "TITLE"}, "objectId": "slide_001_title"},
      {"layoutPlaceholder": {"type": "BODY"}, "objectId": "slide_001_body"}
    ]
  }
}
```

### Layout 2 — Titre carré jaune (g386b92f88e9_0_73)

```json
{
  "createSlide": {
    "objectId": "slide_002",
    "slideLayoutReference": {"layoutId": "g386b92f88e9_0_73"},
    "placeholderIdMappings": [
      {"layoutPlaceholder": {"type": "TITLE"}, "objectId": "slide_002_title"}
    ]
  }
}
```

### Layout 3 — Titre ligne (g386b92f88e9_0_84)

```json
{
  "createSlide": {
    "objectId": "slide_003",
    "slideLayoutReference": {"layoutId": "g386b92f88e9_0_84"},
    "placeholderIdMappings": [
      {"layoutPlaceholder": {"type": "TITLE"}, "objectId": "slide_003_title"}
    ]
  }
}
```

### Layout 4 — Titre (g386b92f88e9_0_93)

```json
{
  "createSlide": {
    "objectId": "slide_004",
    "slideLayoutReference": {"layoutId": "g386b92f88e9_0_93"},
    "placeholderIdMappings": [
      {"layoutPlaceholder": {"type": "TITLE"}, "objectId": "slide_004_title"}
    ]
  }
}
```

### Layout 5 — Vide (g386b92f88e9_0_46)

```json
{
  "createSlide": {
    "objectId": "slide_005",
    "slideLayoutReference": {"layoutId": "g386b92f88e9_0_46"}
  }
}
```

---

## insertText

### Dans un placeholder

```json
{"insertText": {"objectId": "slide_001_title", "text": "Le texte du titre"}}
```

### Body avec bullet points

```json
{"insertText": {"objectId": "slide_001_body", "text": "Premier point\nDeuxième point\nTroisième point"}}
```

---

## createShape — text box

```json
{
  "createShape": {
    "objectId": "textbox_001",
    "shapeType": "TEXT_BOX",
    "elementProperties": {
      "pageObjectId": "slide_005",
      "size": {
        "width": {"magnitude": 8382000, "unit": "EMU"},
        "height": {"magnitude": 500000, "unit": "EMU"}
      },
      "transform": {
        "scaleX": 1,
        "scaleY": 1,
        "translateX": 381000,
        "translateY": 2000000,
        "unit": "EMU"
      }
    }
  }
}
```

**CRITIQUE** : après `createShape` + `insertText`, toujours enchaîner avec `updateTextStyle` pour éviter le fallback Arial 14pt.

---

## updateTextStyle — les 8 patterns v2

### Title — Playfair Display Black (fond clair)

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "ALL"},
    "style": {
      "fontFamily": "Playfair Display",
      "fontSize": {"magnitude": 24, "unit": "PT"},
      "bold": true,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

### Title — sur fond sombre (blanc)

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "ALL"},
    "style": {
      "fontFamily": "Playfair Display",
      "fontSize": {"magnitude": 24, "unit": "PT"},
      "bold": true,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 1, "green": 1, "blue": 1}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

### Subtitle — Lato Regular gris

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "ALL"},
    "style": {
      "fontFamily": "Lato",
      "fontSize": {"magnitude": 10, "unit": "PT"},
      "bold": false,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0.478, "green": 0.478, "blue": 0.478}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

### Annotation — Lato Regular 8pt gris (MAJUSCULES côté texte)

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "FIXED_RANGE", "startIndex": 0, "endIndex": 10},
    "style": {
      "fontFamily": "Lato",
      "fontSize": {"magnitude": 8, "unit": "PT"},
      "bold": false,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0.478, "green": 0.478, "blue": 0.478}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

Note : les MAJUSCULES sont gérées côté texte (insérer en uppercase), pas via l'API.

### Heading — emphasized (Black, noir)

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "FIXED_RANGE", "startIndex": 11, "endIndex": 30},
    "style": {
      "fontFamily": "Lato",
      "fontSize": {"magnitude": 12, "unit": "PT"},
      "bold": true,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

### Heading — de-emphasized (Regular, dk2)

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "FIXED_RANGE", "startIndex": 11, "endIndex": 30},
    "style": {
      "fontFamily": "Lato",
      "fontSize": {"magnitude": 12, "unit": "PT"},
      "bold": false,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0.263, "green": 0.263, "blue": 0.263}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

### Body — emphasized (Black, noir)

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "FIXED_RANGE", "startIndex": 31, "endIndex": 100},
    "style": {
      "fontFamily": "Lato",
      "fontSize": {"magnitude": 8, "unit": "PT"},
      "bold": true,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

### Body — de-emphasized (Regular, dk2)

```json
{
  "updateTextStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "FIXED_RANGE", "startIndex": 31, "endIndex": 100},
    "style": {
      "fontFamily": "Lato",
      "fontSize": {"magnitude": 8, "unit": "PT"},
      "bold": false,
      "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0.263, "green": 0.263, "blue": 0.263}}}
    },
    "fields": "fontFamily,fontSize,bold,foregroundColor"
  }
}
```

---

## Content block — pattern complet

Un content block = annotation + heading + body dans un TEXT_BOX unique, stylé par segments FIXED_RANGE.

Exemple pour un bloc avec annotation "CONTEXTE", heading emphasized, body de-emphasized :

```json
[
  {
    "createShape": {
      "objectId": "block_001",
      "shapeType": "TEXT_BOX",
      "elementProperties": {
        "pageObjectId": "<SLIDE_ID>",
        "size": {
          "width": {"magnitude": 2504440, "unit": "EMU"},
          "height": {"magnitude": 3822430, "unit": "EMU"}
        },
        "transform": {
          "scaleX": 1, "scaleY": 1,
          "translateX": 152400, "translateY": 915570,
          "unit": "EMU"
        }
      }
    }
  },
  {
    "insertText": {
      "objectId": "block_001",
      "text": "CONTEXTE\nLe heading du bloc\nBody text avec les détails et les données du bloc."
    }
  },
  {
    "updateTextStyle": {
      "objectId": "block_001",
      "textRange": {"type": "FIXED_RANGE", "startIndex": 0, "endIndex": 9},
      "style": {
        "fontFamily": "Lato",
        "fontSize": {"magnitude": 8, "unit": "PT"},
        "bold": false,
        "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0.478, "green": 0.478, "blue": 0.478}}}
      },
      "fields": "fontFamily,fontSize,bold,foregroundColor"
    }
  },
  {
    "updateTextStyle": {
      "objectId": "block_001",
      "textRange": {"type": "FIXED_RANGE", "startIndex": 10, "endIndex": 28},
      "style": {
        "fontFamily": "Lato",
        "fontSize": {"magnitude": 12, "unit": "PT"},
        "bold": true,
        "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}
      },
      "fields": "fontFamily,fontSize,bold,foregroundColor"
    }
  },
  {
    "updateTextStyle": {
      "objectId": "block_001",
      "textRange": {"type": "FIXED_RANGE", "startIndex": 29, "endIndex": 75},
      "style": {
        "fontFamily": "Lato",
        "fontSize": {"magnitude": 8, "unit": "PT"},
        "bold": false,
        "foregroundColor": {"opaqueColor": {"rgbColor": {"red": 0.263, "green": 0.263, "blue": 0.263}}}
      },
      "fields": "fontFamily,fontSize,bold,foregroundColor"
    }
  },
  {
    "updateShapeProperties": {
      "objectId": "block_001",
      "shapeProperties": {"contentAlignment": "TOP"},
      "fields": "contentAlignment"
    }
  }
]
```

**Calcul des indices** : compter les caractères du texte inséré. `\n` = 1 caractère. Le startIndex de chaque segment = endIndex du précédent + 1 (pour le `\n`).

---

## createImage — icône fonctionnelle

Icônes Material Icons en PNG monochrome noir. Usage : différencier des catégories dans les content blocks, marquer des blocs thématiques.

### URL format

```
https://raw.githubusercontent.com/material-icons/material-icons-png/master/png/black/{icon_name}/baseline-2x.png
```

### Icônes utiles

| Icône | Nom | Usage type |
|-------|-----|------------|
| check_circle | Validation, acquis | `check_circle` |
| trending_up | Croissance, résultat | `trending_up` |
| lightbulb | Insight, idée | `lightbulb` |
| warning | Risque, attention | `warning` |
| groups | Équipe, utilisateurs | `groups` |
| timeline | Process, roadmap | `timeline` |
| insights | Analyse, données | `insights` |
| rocket_launch | Lancement, ambition | `rocket_launch` |
| target | Objectif | `target` |
| build | Méthode, outil | `build` |

### Pattern JSON

```json
{
  "createImage": {
    "objectId": "icon_block_001",
    "url": "https://raw.githubusercontent.com/material-icons/material-icons-png/master/png/black/check_circle/baseline-2x.png",
    "elementProperties": {
      "pageObjectId": "<SLIDE_ID>",
      "size": {
        "width": {"magnitude": 228600, "unit": "EMU"},
        "height": {"magnitude": 228600, "unit": "EMU"}
      },
      "transform": {
        "scaleX": 1, "scaleY": 1,
        "translateX": 152400,
        "translateY": 700000,
        "unit": "EMU"
      }
    }
  }
}
```

228,600 EMU = 24px. Positionner l'icône au-dessus de l'annotation du content block.

**Règle** : icône fonctionnelle uniquement — si on peut la retirer sans perte d'information, elle est décorative → ne pas ajouter.

---

## updatePageProperties — fond de slide

### Fond noir

```json
{
  "updatePageProperties": {
    "objectId": "<SLIDE_ID>",
    "pageProperties": {
      "pageBackgroundFill": {
        "solidFill": {
          "color": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}
        }
      }
    },
    "fields": "pageBackgroundFill.solidFill.color"
  }
}
```

### Fond jaune STFU

```json
{
  "updatePageProperties": {
    "objectId": "<SLIDE_ID>",
    "pageProperties": {
      "pageBackgroundFill": {
        "solidFill": {
          "color": {"rgbColor": {"red": 1, "green": 0.886, "blue": 0}}
        }
      }
    },
    "fields": "pageBackgroundFill.solidFill.color"
  }
}
```

---

## deleteObject

```json
{"deleteObject": {"objectId": "<OBJECT_ID>"}}
```

---

## updateParagraphStyle

### Centré

```json
{
  "updateParagraphStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "ALL"},
    "style": {"alignment": "CENTER"},
    "fields": "alignment"
  }
}
```

### Espacement entre paragraphes

```json
{
  "updateParagraphStyle": {
    "objectId": "<ID>",
    "textRange": {"type": "ALL"},
    "style": {
      "spaceAbove": {"magnitude": 6, "unit": "PT"},
      "spaceBelow": {"magnitude": 6, "unit": "PT"},
      "lineSpacing": 120
    },
    "fields": "spaceAbove,spaceBelow,lineSpacing"
  }
}
```

---

## replaceAllText

```json
{
  "replaceAllText": {
    "containsText": {"text": "{{PLACEHOLDER}}", "matchCase": true},
    "replaceText": "Valeur réelle"
  }
}
```
