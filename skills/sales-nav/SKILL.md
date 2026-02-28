---
name: sales-nav
description: >
  Expert Sales Navigator — co-pilote pour la construction de filtres, boolean search,
  estimation de volume et best practices (FR). Encode les 3 stratégies de recherche
  (Persona, Account-Based, Intent/Trigger), les 50+ filtres Lead et Account,
  la taxonomie sectorielle LinkedIn, et les pièges courants.
  Mobilisé automatiquement par mission-to-outbound et activable directement via /sales-nav.
user_invocable: true
---

# Co-pilote Sales Navigator

Expert Sales Navigator pour la prospection outbound STFU. Construit des recherches précises, estime les volumes, et évite les pièges classiques.

## Déclenchement

Invoqué automatiquement par `/mission-to-outbound` (étape 7) ou directement :

```
/sales-nav directeurs achats agroalimentaire france
/sales-nav DSI ETI industrielles île-de-france
/sales-nav account-based liste de 50 comptes tech
```

**Input** : description du persona cible, du secteur, de la géographie, ou d'une liste de comptes.
**Output** : filtres Sales Nav structurés, boolean search, volume estimé, recommandations.

---

## Fichiers de référence

| Fichier | Contenu |
|---------|---------|
| `references/lead-filters.md` | 34 filtres Lead avec valeurs valides, type et fiabilité |
| `references/account-filters.md` | 16 filtres Account avec valeurs valides et combinaisons recommandées |
| `references/industries-taxonomy.md` | Taxonomie sectorielle LinkedIn hiérarchique (FR) — valeurs exactes |
| `references/boolean-search.md` | Syntaxe booléenne, patterns titres FR, templates par persona, exclusions |

**Consulter ces fichiers systématiquement** avant de proposer des filtres. Ne jamais inventer de valeurs — utiliser uniquement les valeurs listées dans les références.

---

## Étape 0 — Choisir la stratégie de recherche

Trois stratégies, combinables. Identifier laquelle s'applique avant de construire les filtres.

### Persona-Based (défaut)

**Quand** : "Je cherche tous les DSI des ETI en France."
**Logique** : Définir le persona → filtres Lead → filtres Account → affiner.
**Usage** : La majorité des recherches. Point de départ par défaut.

### Account-Based (ABM)

**Quand** : "Je cible ces 50 entreprises, qui contacter dedans ?"
**Logique** : Liste de comptes → recherche Lead dans la liste → mapping multi-niveaux (décideur, influenceur, acheteur).
**Usage** : Quand on a déjà identifié les entreprises cibles. Plus précis mais volume plus faible.
**Spécificité** : Créer une liste de comptes dans Sales Nav, puis chercher des Leads dans cette liste. Prévoir 3 recherches par compte (décideur / influenceur-utilisateur / acheteur).

### Intent/Trigger-Based

**Quand** : "Qui est en phase d'achat maintenant ?"
**Logique** : Spotlights + signaux d'intention → filtrer par persona ICP → prioriser par "chaleur".
**Usage** : Pour maximiser les taux de réponse. Volume faible mais conversion élevée.
**Spécificité** : Combiner filtres ICP + 1 seul spotlight (changement de poste OU publication récente OU offres d'emploi). Sauvegarder la recherche pour monitoring régulier.

### Priorisation par chaleur

Combiner les 3 stratégies pour segmenter les prospects :

| Priorité | Définition | Taux de réponse attendu |
|----------|-----------|------------------------|
| **P1 — Chaud** | ICP match + signal d'intention (changement de poste, activité récente, suit l'entreprise) | 15-25% |
| **P2 — Tiède** | ICP match + 2e degré de connexion (intro possible) | 8-15% |
| **P3 — Froid** | ICP match seul (persona + account corrects, aucun signal) | 3-8% |

---

## Workflow en 8 étapes

### Étape 1 — Choisir la stratégie

Identifier la stratégie principale (Persona / Account / Intent) à partir du brief. En cas de doute → Persona-Based par défaut.

Si le contexte fournit une liste d'entreprises nommées → Account-Based.
Si l'objectif est de maximiser la conversion immédiate → Intent/Trigger-Based.

### Étape 2 — Partir du persona

Définir le persona cible :
- **Titre** : la forme exacte telle qu'elle apparaît sur les profils LinkedIn français
- **Séniorité** : niveau hiérarchique (CxO, VP, Directeur, Manager)
- **Fonction** : département (IT, RH, Finance, Achats, etc.)

**Construire le boolean titre** en consultant `references/boolean-search.md` :
1. Partir du template persona le plus proche
2. Ajouter les variantes FR + EN + abréviations + formes genrées
3. Ajouter les exclusions standard (Stagiaire, Alternant, etc.)
4. Vérifier qu'on ne dépasse pas ~15 opérateurs

### Étape 3 — Cadrer l'entreprise

Définir le profil entreprise cible :
- **Taille** : tranches d'effectifs (voir `references/account-filters.md`)
- **Secteur** : sous-secteurs exacts de la taxonomie LinkedIn (voir `references/industries-taxonomy.md`)
- **Géographie** : pays / région / ville
- **Signaux** : croissance effectifs, offres d'emploi

**Règle** : Toujours filtrer le secteur au niveau Account, jamais au niveau Lead.

### Étape 4 — Construire le boolean titre

En utilisant `references/boolean-search.md` :
1. Choisir le template persona approprié
2. Adapter au contexte spécifique (domaine, spécialité)
3. Inclure : variantes genrées (Directeur/Directrice), abréviations (DSI), anglicismes (CTO)
4. Exclure : Stagiaire, Alternant, Adjoint, Consultant (si ciblage interne)
5. Tester la lisibilité — un boolean illisible sera mal maintenu

### Étape 5 — Choisir les filtres structurels

En consultant `references/lead-filters.md` et `references/account-filters.md` :
1. Sélectionner les filtres par ordre de fiabilité (fiable → moyen → éviter peu fiable)
2. Prioriser : Effectifs > Secteur Account > Géographie > Niveau hiérarchique > Fonction
3. Éviter : CA annuel, Technologies, Secteur Lead, Années d'expérience

### Étape 6 — Sélectionner les secteurs précis

En consultant `references/industries-taxonomy.md` :
1. Identifier la catégorie parente pertinente
2. Sélectionner les sous-secteurs spécifiques (pas la catégorie entière sauf si tout est pertinent)
3. **Toujours utiliser les valeurs exactes de la taxonomie** — ne pas inventer de noms de secteur
4. Vérifier les secteurs adjacents qui pourraient être pertinents

### Étape 7 — Ajouter les spotlights et signaux d'intention

Sélectionner **1 seul spotlight par recherche** (le stacking réduit trop le volume) :

| Spotlight | Signal | Bon pour |
|-----------|--------|----------|
| Changement de poste | Nouveau en poste, veut faire ses preuves | P1 — meilleur signal d'achat |
| Activité LinkedIn | Publie/commente, profil actif | P1 — réceptif aux messages |
| Offres d'emploi (Account) | L'entreprise recrute dans le domaine | P1 — investit dans le sujet |
| Suit votre entreprise | Connaît déjà STFU | P2 — notoriété existante |
| Connexions partagées (2e degré) | Intro possible | P2 — levier social |

**Stratégie** : Créer une recherche cœur sans spotlight (P3), puis dupliquer avec chaque spotlight pour les P1/P2.

### Étape 8 — Qualifier et segmenter le volume

#### Méthode entonnoir itératif

1. **Commencer large (TAM)** : 2-3 filtres non-négociables uniquement (géographie + effectifs + boolean titre simple)
2. **Mesurer le volume brut** → c'est le plafond théorique
3. **Ajouter les filtres un par un** et noter l'impact de chacun sur le volume
4. **Cible idéale** : 200-500 résultats pour le cœur de cible
5. **Recherche accordéon** : si trop restreint, retirer le filtre le plus restrictif ; si trop large, ajouter un filtre

#### Ordres de grandeur France

| Base | Volume estimé |
|------|--------------|
| Tous les profils LinkedIn France | ~25 millions |
| Avec titre C-level/VP/Dir | ~500 000 |
| + Secteur spécifique (ex. industrie) | ~50 000-100 000 |
| + Effectifs ETI (201-5000) | ~10 000-30 000 |
| + Boolean titre précis (ex. DSI) | ~2 000-8 000 |
| + Région (ex. Île-de-France) | ~800-3 000 |
| + Spotlight (ex. changement poste) | ~50-300 |

#### Facteurs de réduction typiques par filtre

| Filtre ajouté | Réduction estimée |
|---------------|-------------------|
| Géographie (France) | Base |
| Effectifs (1 tranche) | ÷ 3 à 5 |
| Secteur (1 sous-secteur) | ÷ 5 à 15 |
| Boolean titre précis | ÷ 3 à 10 |
| Niveau hiérarchique | ÷ 2 à 4 |
| Spotlight | ÷ 10 à 50 |

#### Limite extraction

- **Evaboot** : qualité dégradée au-delà de ~1000 résultats par extraction. Si le volume dépasse 1000, segmenter en plusieurs recherches (par région, par sous-secteur, par tranche d'effectifs).
- **Recommandation** : viser 200-500 par recherche pour une qualité optimale.

---

## Pièges courants (anti-patterns)

### Mots-clés dans la barre Keywords
Ne PAS mettre de titres de poste dans Keywords. Ce champ cherche dans tout le profil (bio, compétences, expériences passées). Réserver aux compétences niche : SAP, Figma, Kubernetes, Power BI, etc.

### Fonction seule sans boolean
Le filtre Fonction est auto-attribué par LinkedIn et souvent imprécis. Toujours construire un boolean titre en complément. La Fonction sert de pré-filtre, pas de filtre principal.

### Secteur lead au lieu de secteur account
Le secteur au niveau Lead est auto-attribué et hérite parfois de l'entreprise précédente. **Toujours filtrer le secteur au niveau Account** via Industry.

### Titres fourre-tout sans qualification
"Chef de projet", "Consultant", "Responsable" seuls → bruit massif. Toujours qualifier avec le domaine. Voir la section "Titres piégeux" dans `references/boolean-search.md`.

### Oublier les exclusions
Toujours exclure : Stagiaire, Alternant, Apprenti, Intern. Si ciblage interne : exclure Consultant, Freelance, Indépendant. Exclure les concurrents et ses propres collègues dans le champ Company.

### CA annuel comme filtre de taille
Peu fiable hors entreprises cotées. **Toujours utiliser les effectifs** comme proxy de taille.

### Technologies comme filtre principal
Données estimées, non déclarées. Ne baser un ciblage dessus que si c'est un critère non-négociable, et toujours vérifier manuellement les premiers résultats.

### Variantes genrées oubliées
Toujours inclure Directeur/Directrice, Chef/Cheffe, Responsable (invariable), Président/Présidente dans le boolean.

### Spotlight stacking
Un seul spotlight par recherche. Empiler "changement de poste" + "activité récente" réduit le volume à quasi-zéro. Créer des recherches séparées par spotlight.

### Années d'expérience comme filtre
Calculé automatiquement par LinkedIn à partir de l'historique. Trous de carrière, études longues, profils incomplets → résultats très imprécis. Éviter.

---

## Techniques avancées (power users)

### Trigger-based search (recherches sauvegardées)

1. Créer une recherche ICP de base (boolean + account filters)
2. Ajouter 1 spotlight (changement de poste OU publication récente)
3. Sauvegarder la recherche
4. Vérifier chaque semaine les nouveaux résultats
5. Contacter avec le contexte du trigger ("Félicitations pour votre prise de poste...")

### Account mapping multi-niveaux

Pour un même compte cible, créer 3 recherches Lead :

| Niveau | Cible | Rôle dans l'achat |
|--------|-------|-------------------|
| Décideur | C-level, VP | Valide le budget, signe |
| Influenceur / Utilisateur | Directeur, Manager métier | Recommande, utilise au quotidien |
| Acheteur | Achats, Procurement | Process achat, négociation |

Contacter les 3 niveaux avec des angles différents.

### Multi-recherche par verticale

Quand on cible plusieurs secteurs, créer une recherche séparée par verticale plutôt qu'une recherche unique avec 10 secteurs. Permet :
- Un boolean titre adapté par verticale (les titres diffèrent)
- Un volume maîtrisé par segment
- Un message personnalisé par secteur

---

## Template de sortie

Quand ce skill produit un résultat, utiliser ce format structuré :

```markdown
## Filtres Sales Navigator — {Nom du persona}

**Stratégie** : {Persona-Based / Account-Based / Intent-Based}

### Filtres Lead

| Filtre | Valeur |
|--------|--------|
| Boolean titre | `{boolean complet}` |
| Fonction | {valeurs sélectionnées ou "—"} |
| Niveau hiérarchique | {valeurs} |
| Géographie | {pays / région / ville} |
| Keywords | {compétences niche ou "—"} |

### Filtres Account

| Filtre | Valeur |
|--------|--------|
| Effectifs | {tranches sélectionnées} |
| Secteur (Industry) | {sous-secteurs exacts de la taxonomie} |
| Siège social | {géographie} |
| Type | {Société privée, Cotée, etc.} |
| Croissance | {tranche ou "—"} |
| Offres d'emploi | {oui/non + fonction si oui} |

### Spotlight

| Spotlight | Recherche |
|-----------|-----------|
| {Nom du spotlight} | {Recherche P1 — description} |

### Volume estimé

| Segment | Volume estimé | Usage |
|---------|--------------|-------|
| Cœur de cible (sans spotlight) | {X} | Base de prospection P3 |
| Avec spotlight {nom} | {X} | Priorisation P1 |
| Total exploitable | {X} | Après dédoublonnage |

### Recommandation extraction

- **Volume par extraction Evaboot** : {X} (max recommandé : 1000)
- **Segmentation suggérée** : {par région / par secteur / par tranche si >1000}
- **Fréquence de refresh** : {hebdo si trigger-based / mensuel si persona-based}

### Exclusions appliquées

- Boolean : {NOT terms}
- Company : {entreprises exclues}
```

---

## Règles clés

1. **Toujours consulter les fichiers de référence** — ne jamais inventer de valeurs de filtres ou de noms de secteur.
2. **Fiabilité first** — privilégier les filtres fiables (Titre boolean, Effectifs, Secteur Account, Géographie) aux filtres approximatifs.
3. **200-500 résultats = sweet spot** — en-dessous c'est trop restreint, au-dessus c'est dilué.
4. **Un spotlight max par recherche** — dupliquer plutôt qu'empiler.
5. **Boolean titre > Fonction** — toujours construire le boolean, ne jamais se fier à la Fonction seule.
6. **Secteur Account > Secteur Lead** — le secteur Lead est auto-attribué et peu fiable.
7. **Effectifs > CA** — les effectifs sont déclaratifs et vérifiables, le CA est estimé.
8. **Toujours exclure** — Stagiaires, Alternants, et si pertinent : Consultants, Freelances, Concurrents.
