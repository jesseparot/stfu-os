# Protocole d'extraction photo

Guide pour extraire le contenu des photos murales de workshop (post-its, whiteboards, paperboards).

## Principes

1. **Une photo à la fois** : traiter chaque photo séparément avec validation interactive
2. **L'espace compte** : les groupements spatiaux (clusters, colonnes, proximité) portent du sens
3. **OCR manuscrit imparfait** : toujours signaler les éléments incertains
4. **Le facilitateur complète** : il a le contexte que la photo ne montre pas

## Étapes par photo

### 1. Lire l'image

Utiliser le tool `Read` sur le fichier image. Observer :
- Type de support (post-its sur mur, whiteboard, paperboard, tableau)
- Structure visible (colonnes, zones, cadrants, axes)
- Éléments non textuels (flèches, dessins, votes, gommettes)

### 2. Extraire le contenu

Organiser l'extraction par zone spatiale :

```
Zone : {nom ou position - ex. "colonne gauche", "cluster haut-droite"}
- Post-it 1 : "{texte}"
- Post-it 2 : "{texte}"
- Post-it 3 : "{texte}" [?] (lecture incertaine)

Éléments visuels :
- Flèche de {zone A} vers {zone B}
- 3 gommettes rouges sur post-it "{texte}"
- Dessin : {description}
```

### 3. Signaler les incertitudes

Marquer avec `[?]` tout élément dont la lecture est incertaine :
- Écriture illisible : `"{mot?} quelque chose {mot?}"` [?]
- Post-it partiellement caché : `"{texte visible}..."` [?] (partiellement caché)
- Ambiguïté de groupement : signaler si un post-it pourrait appartenir à deux clusters

### 4. Présenter pour validation

Présenter l'extraction à l'utilisateur via `AskUserQuestion` :

```
Photo : {nom du fichier}

{Extraction organisée par zone}

Éléments incertains :
- {Liste des [?] avec contexte}

Questions :
- {Questions spécifiques si nécessaire}

Cette extraction est-elle correcte ? Des corrections ou ajouts ?
```

### 5. Intégrer les corrections

Mettre à jour l'extraction avec les corrections de l'utilisateur avant de passer à la photo suivante.

## Éléments à capturer

| Élément | Comment le noter |
|---------|-----------------|
| Texte post-it | Citation entre guillemets |
| Clusters/groupes | Nommer la zone, lister les post-its |
| Titres de colonnes/zones | En gras, comme organisateur |
| Votes (gommettes, dots) | Nombre + couleur + sur quel post-it |
| Flèches/connexions | De → vers, avec direction |
| Dessins/schémas | Description textuelle de ce qui est représenté |
| Annotations | Texte ajouté au feutre sur le support |
| Numérotation | Préserver l'ordre si des numéros sont visibles |

## Pièges courants

- **Post-its superposés** : demander à l'utilisateur s'il y a du contenu caché
- **Écriture en miroir** : les photos prises avec flash sur un whiteboard peuvent inverser
- **Couleur des post-its** : la couleur porte souvent du sens (catégories, priorités), la noter
- **Contexte hors-cadre** : demander si d'autres éléments étaient visibles mais pas photographiés
