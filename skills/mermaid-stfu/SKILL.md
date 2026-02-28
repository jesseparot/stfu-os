---
name: mermaid-stfu
description: Génère des diagrammes Mermaid brandés avec l'identité visuelle STFU. Appliqué automatiquement lors de la création de tout diagramme Mermaid. Gère le theming, la palette de couleurs, la typographie, les commandes d'export. Couvre flowcharts, diagrammes de séquence, journey maps et tous les types de diagrammes Mermaid.
---

# Diagrammes Mermaid STFU

Appliquer ces règles lors de la génération de tout diagramme Mermaid pour le travail STFU.

## Palette de la marque

### Échelle de gris (90-95% de tous les éléments du diagramme)

| Token | Hex | Usage |
|-------|-----|-------|
| `black` | `#1A1A1A` | Texte principal, headers d'acteurs, éléments critiques/bloquants |
| `dark` | `#333333` | Bordures, éléments secondaires forts, labels de sous-groupes |
| `mid` | `#555555` | Couleur des flèches/lignes, labels d'arêtes |
| `light-mid` | `#999999` | Éléments dé-emphasisés, éléments futurs/spéculatifs |
| `light` | `#E0E0E0` | Remplissage de nœud standard (défaut pour la majorité des boîtes) |
| `near-white` | `#F0F0F0` | Arrière-plans de sous-groupes/clusters |
| `white` | `#FFFFFF` | Canvas, texte sur fonds sombres |

### Accent (5-10% des éléments du diagramme, maximum)

| Token | Hex | Usage |
|-------|-----|-------|
| `accent` | `#FFE200` | L'UN insight clé, point de décision, ou élément focal par section du diagramme. Jamais en décoration. |
| `accent-light` | `#FFF3B0` | Accent secondaire quand un deuxième niveau de mise en avant est nécessaire. Rare. |

### Règles d'utilisation des couleurs

1. **L'accent doit porter du sens.** Le jaune n'est pas de la décoration. Chaque élément jaune doit appartenir au même fil narratif : le chemin critique, les points de douleur, les acteurs qui comptent le plus, les décisions. Le lecteur doit pouvoir ne suivre que le jaune et comprendre l'histoire.
2. **Le gris est le défaut.** La plupart des nœuds sont en gris clair (#E0E0E0). C'est le canvas. Le jaune ressort parce qu'il est entouré de gris.
3. **Remplissages sombres (#1A1A1A) pour la sévérité/finalité.** Erreurs, bloqueurs, échecs critiques. Texte blanc sur fond sombre.
4. **Bordures en pointillés + light-mid (#999999)** pour les éléments spéculatifs/futurs/concurrents.
5. **Pas d'autres couleurs.** Pas de bleu, pas de rouge, pas de vert. La palette gris + jaune est l'identité.

### Appliquer l'accent — cadre de décision

Avant d'assigner du jaune, décider : **quelle est l'histoire que raconte ce diagramme ?** Puis colorer les éléments qui portent cette histoire. Ce peut être 2 nœuds ou 8 — le nombre n'importe pas. Ce qui importe c'est la cohérence : tous les éléments jaunes doivent répondre à la même question.

Exemples d'utilisation cohérente de l'accent :
- Chaîne de valeur : jaune sur les acteurs qui intéressent le client (leur rôle + leurs partenaires directs)
- Carte de points de douleur : jaune sur les problèmes prioritaires à résoudre en premier
- Flux technique : jaune sur les étapes où ça casse
- Parcours utilisateur : jaune sur les moments qui définissent l'adoption vs l'abandon

## Typographie

- **Police** : Lato (tous les graisses)
- **Fichiers de police** : `.claude/skills/mermaid-stfu/fonts/` (copier dans `~/Library/Fonts/` si non installée)
- **Variable de thème Mermaid** : `'fontFamily': 'Lato'`

## Bloc de thème

Coller ceci en haut de chaque fichier `.mmd`. Ajuster les variables spécifiques au type de diagramme selon le besoin.

### Flowcharts (graph LR/TB)

```
%%{init: {'theme': 'base', 'themeVariables': {
  'fontFamily': 'Lato',
  'fontSize': '14px',
  'primaryColor': '#E0E0E0',
  'primaryTextColor': '#1A1A1A',
  'primaryBorderColor': '#333333',
  'secondaryColor': '#F0F0F0',
  'tertiaryColor': '#FFFFFF',
  'lineColor': '#555555',
  'textColor': '#1A1A1A',
  'clusterBkg': '#F0F0F0',
  'clusterBorder': '#CCCCCC'
}}}%%
```

### Diagrammes de séquence

```
%%{init: {'theme': 'base', 'themeVariables': {
  'fontFamily': 'Lato',
  'fontSize': '13px',
  'actorBkg': '#1A1A1A',
  'actorBorder': '#1A1A1A',
  'actorTextColor': '#FFFFFF',
  'actorLineColor': '#CCCCCC',
  'signalColor': '#333333',
  'signalTextColor': '#1A1A1A',
  'noteBkgColor': '#FFE200',
  'noteTextColor': '#1A1A1A',
  'noteBorderColor': '#D4BD00',
  'activationBkgColor': '#F0F0F0',
  'activationBorderColor': '#333333',
  'labelBoxBkgColor': '#F0F0F0',
  'labelBoxBorderColor': '#333333',
  'labelTextColor': '#1A1A1A',
  'altSectionBkgColor': '#F8F8F8',
  'loopTextColor': '#1A1A1A',
  'textColor': '#1A1A1A'
}}}%%
```

Note : dans les diagrammes de séquence, `noteBkgColor: #FFE200` est intentionnel. Les notes sont le mécanisme de callout et doivent attirer l'attention. C'est l'usage correct de l'accent.

### Diagrammes journey

```
%%{init: {'theme': 'base', 'themeVariables': {
  'fontFamily': 'Lato',
  'fontSize': '13px',
  'textColor': '#1A1A1A',
  'titleColor': '#1A1A1A'
}}}%%
```

**Limitation connue** : Le type `journey` de Mermaid utilise une échelle de couleurs codée en dur basée sur le score (rouge → vert) qui ne peut pas être surchargée. Les couleurs des barres de tâches NE correspondront PAS à la palette STFU. Accepter cela ou convertir en layout flowchart si le branding complet est requis.

## Patterns de styling des nœuds

### Nœud par défaut (majorité des éléments)
```
style NODE fill:#E0E0E0,stroke:#333333,color:#1A1A1A,stroke-width:1px
```

### Nœud accent (point focal, 1 par section max)
```
style NODE fill:#FFE200,stroke:#1A1A1A,color:#1A1A1A,stroke-width:2px
```

### Accent secondaire (rare)
```
style NODE fill:#FFF3B0,stroke:#333333,color:#1A1A1A,stroke-width:1px
```

### Nœud critique/erreur/bloqueur
```
style NODE fill:#1A1A1A,stroke:#000000,color:#FFFFFF,stroke-width:2px
```

### Nœud sombre principal (acteurs clés, utilisateurs finaux)
```
style NODE fill:#333333,stroke:#1A1A1A,color:#FFFFFF,stroke-width:2px
```

### Nœud spéculatif/futur
```
style NODE fill:#FFFFFF,stroke:#999999,color:#888888,stroke-width:1px,stroke-dasharray: 5 5
```

## Légendes

Quand la couleur accent porte du sens, ajouter une légende pour que le lecteur sache ce que le jaune (et les autres traitements visuels) représentent.

### Flowcharts — nœud texte inline (PAS un subgraph)

**Ne jamais utiliser un `subgraph` pour les légendes dans les flowcharts.** Mermaid traite les subgraphs comme des participants du layout — un subgraph légende va occuper une colonne/ligne entière et casser la mise en page du diagramme.

À la place, utiliser un nœud stylé autonome sans connexions :

```
LEGEND["🟡 Jaune = Signification clé  ·  ⬜ Gris = Par défaut  ·  ┈ Pointillé = Autre signification"]
style LEGEND fill:none,stroke:none,color:#555555,font-size:12px
```

Cela flotte au bord du diagramme sans affecter le flux.

### Diagrammes de séquence — note d'ouverture

Utiliser une `Note` sur le participant le plus à gauche :

```
Note left of FirstActor: Jaune = points de friction<br/>et problèmes connus
```

Les notes de diagrammes de séquence sont natives au format et ne perturbent pas le layout.

### Diagrammes groupés (points de douleur, matrices) — subgraph légende classDef

Pour les diagrammes `graph TB` avec des groupes subgraph (pas des diagrammes de flux LR), un petit subgraph légende en haut peut fonctionner car le layout est vertical et la légende ne vole pas une colonne de flux :

```
subgraph LEG [" "]
    direction LR
    L1[" "]:::accent
    L1T["Élément critique"]:::legendText
    L2[" "]:::dark
    L2T["Problème structurel"]:::legendText
end

classDef legendText fill:none,stroke:none,color:#555555,font-size:12px
style LEG fill:none,stroke:none
```

**Règle d'or** : si le diagramme est `graph LR`, ne jamais utiliser un subgraph légende. Si `graph TB` avec des subgraphs groupés, un subgraph légende en haut est acceptable.

### Toujours vérifier le rendu

Après l'export, **lire le PNG** pour vérifier que la légende n'a pas cassé le layout. L'auto-layout de Mermaid est imprévisible avec des éléments supplémentaires.

## Commandes d'export

Toujours exporter depuis la racine du repo ou le répertoire contenant les fichiers `.mmd`.

### PNG (pour partage, haute résolution)
```bash
mmdc -i diagram.mmd -o diagram.png -s 3
```

### SVG (pour import Figma et édition ultérieure)
```bash
mmdc -i diagram.mmd -o diagram.svg
```

### Prérequis

1. Installer mmdc : `npm install -g @mermaid-js/mermaid-cli`
2. Installer Lato : copier les fichiers `.ttf` depuis le dossier `fonts/` du skill mermaid-stfu (`skills/mermaid-stfu/fonts/`) dans `~/Library/Fonts/`

## Workflow

1. Générer le fichier `.mmd` avec le bloc de thème et le contenu
2. Appliquer les styles de nœuds — gris clair par défaut, accent uniquement quand c'est justifié
3. Exporter en PNG à 3x pour le partage
4. Exporter en SVG si un rendu client-facing est nécessaire (Figma → restyle → Slides/deck)

## Ce qu'il ne faut PAS faire

- Ne pas utiliser l'accent sur plus de ~10% des nœuds
- Ne pas utiliser de couleurs hors de la palette (pas de bleu, rouge, vert, violet)
- Ne pas utiliser le type de diagramme `journey` si la cohérence de marque est critique — convertir en flowchart
- Ne pas utiliser le flag `--cssFile` pour les exports PNG — le Lato système gère le rendu. Le CSS n'est nécessaire que pour l'embedding de police SVG si Lato n'est pas installé.
