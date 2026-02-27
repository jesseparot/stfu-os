# Visual Inspection Prompt — stfu-slides v2

Prompt structuré pour le self-review visuel (Step 5). Utiliser avec `get_page_thumbnail` → `WebFetch`.

---

## Prompt d'inspection

Envoyer ce prompt à `WebFetch` avec le thumbnail de la slide :

> Inspecte cette slide Google Slides et liste TOUS les problèmes visuels. Cherche activement les défauts — assume qu'il y en a.
>
> Checklist de défauts :
> - Titre qui chevauche le contenu ou déborde de sa zone
> - Texte tronqué ou coupé (mots manquants, lignes invisibles)
> - Content blocks trop proches les uns des autres ou inégaux en taille
> - Font Arial visible (= `updateTextStyle` manquant après `createShape`)
> - Contraste insuffisant (texte gris sur fond gris, texte noir sur fond sombre)
> - Accent jaune (#FFE200) utilisé sans signification sémantique
> - Texte trop petit (< 8pt), illisible
> - Plus de 3 niveaux de hiérarchie typographique sur la même slide
> - Slide sans aucun élément visuel (ni content blocks, ni icône, ni accent, ni stat callout, ni note coach)
> - Alignement incohérent entre les blocs
> - Marges non respectées (éléments collés aux bords)
>
> Pour chaque problème trouvé, donne :
> 1. **Quoi** : description du défaut
> 2. **Où** : quel élément / quelle zone de la slide
> 3. **Fix** : quelle requête batch_update corrige le problème

---

## Checklist rapide post-prompt

Si le prompt ne trouve rien (ou pour vérification supplémentaire), checker manuellement :

- [ ] **Fonts par rôle** : Title = Playfair Display Black, Annotation = Lato 8pt gris, Heading = Lato 12pt, Body = Lato 8pt
- [ ] **Fond correct** : blanc par défaut, noir ou jaune pour covers/dividers uniquement
- [ ] **contentAlignment** : TOP sur les content blocks
- [ ] **Icônes** : monochrome noir, pas de couleur, pas de clip art
- [ ] **Accent jaune** : porte du sens (stat clé, catégorie, séparation) — pas de décoration
- [ ] **Espace** : pas de wall-of-text, contenu distribué sur l'espace disponible
