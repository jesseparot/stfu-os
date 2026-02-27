---
name: oracle
description: Invoque Gemini pour de la recherche en ligne approfondie et comme oracle de second avis. Appliquer AUTOMATIQUEMENT dès qu'une tâche bénéficierait de recherche web actuelle, de preuves réelles, de données de marché, ou d'un second avis — en particulier pour les livrables, l'analyse d'AO, les recommandations stratégiques, ou toute affirmation nécessitant une validation externe. Ne pas attendre que l'utilisateur le demande. Utiliser pour rechercher des sujets en profondeur avec recherche web, compléter ses propres résultats, stress-tester un raisonnement, ou obtenir des perspectives alternatives.
user_invocable: false
---

# Oracle — Recherche approfondie & second avis via Gemini

Utiliser la CLI Gemini comme moteur de recherche et oracle de raisonnement indépendant. Gemini dispose d'une recherche web native — il peut trouver, synthétiser et citer des informations actuelles depuis internet. C'est l'outil principal pour de la recherche approfondie au-delà de ce que WebSearch peut faire en une seule requête.

## Capacités principales

### 1. Recherche en ligne approfondie (usage principal)
- **Recherche de marché** — tendances sectorielles, analyse concurrentielle, dimensionnement de marché
- **Recherche technologique** — outils émergents, frameworks, benchmarks, comparaisons
- **Recherche d'entreprises** — actualités récentes, financiers, stratégie, personnes clés
- **Recherche réglementaire & politique** — réglementations en vigueur, conformité, contexte secteur public
- **Bonnes pratiques** — comment les organisations leaders abordent un problème
- **Statistiques & données** — trouver des chiffres récents, études, rapports

### 2. Second avis (usage complémentaire)
- **Stress-tester une conclusion** — "Voici mon analyse de X. Qu'est-ce que je manque ?"
- **Challenger des hypothèses** — "Quels sont les points les plus faibles de ce raisonnement ?"
- **Débloquer une impasse** — quand on hésite entre deux approches
- **Cross-valider des faits** — "Cette affirmation est-elle exacte ? Cherche sur le web pour vérifier."

## Quand utiliser

**Utiliser pour la recherche quand :**
- L'utilisateur a besoin d'informations actuelles et détaillées sur un sujet (marché, entreprise, tech, réglementation)
- WebSearch donne des résultats superficiels et une synthèse plus profonde est nécessaire
- Besoin de multiples angles sur une question de recherche (combiner ses résultats + ceux de Gemini)
- Le sujet requiert un recoupement de multiples sources pour la précision
- Besoin de données récentes, statistiques ou case studies pour appuyer un livrable
- Préparation d'une réponse d'AO, analyse concurrentielle ou briefing client nécessitant des preuves réelles

**Utiliser pour le second avis quand :**
- Décisions stratégiques complexes où une deuxième perspective ajoute de la valeur
- Quand on suspecte que son raisonnement est biaisé ou circulaire
- Quand l'utilisateur demande explicitement un second avis

**Ne PAS utiliser pour :**
- Génération ou édition de code simple
- Tâches où on est confiant dans la réponse et qu'on a déjà l'info
- Questions triviales qui ne bénéficient pas de recherche web ou d'un second modèle
- Informations trouvables plus rapidement avec ses propres outils (fichiers locaux, sources MCP)

## Comment invoquer

Utiliser Bash pour appeler la CLI Gemini en mode non-interactif :

```bash
/Users/jesseparot/.local/bin/gemini -m gemini-2.5-pro -p "Votre prompt ici" 2>&1
```

**Important :**
- **Toujours utiliser `2>&1`** (jamais `2>/dev/null`) pour que les erreurs soient visibles et qu'on puisse détecter les erreurs de capacité et basculer.
- **Essayer pro d'abord, basculer sur flash.** Si la sortie contient `MODEL_CAPACITY_EXHAUSTED` ou `429`, retenter immédiatement le même prompt avec `-m gemini-2.5-flash`. Le faire silencieusement — pas besoin de demander à l'utilisateur.

Pour les tâches de recherche nécessitant une recherche web extensive, utiliser un timeout plus long (jusqu'à 120s) :

```bash
# Utiliser l'outil Bash avec timeout: 120000
/Users/jesseparot/.local/bin/gemini -m gemini-2.5-pro -p "Votre prompt de recherche ici" 2>&1
# Si erreur de capacité → retenter avec flash
/Users/jesseparot/.local/bin/gemini -m gemini-2.5-flash -p "Votre prompt de recherche ici" 2>&1
```

### Règles de construction des prompts

1. **Donner le contexte complet** — Expliquer pourquoi on recherche cela. Inclure le contexte client, projet ou décision en cours.
2. **Être spécifique sur ce qu'on veut** — "Trouver des case studies récents de X dans l'industrie Y avec des résultats quantifiés" bat "Parle-moi de X."
3. **Demander des sources** — Toujours demander à Gemini de citer des URLs ou noms de sources pour pouvoir vérifier.
4. **Demander un output structuré** — Demander des bullet points, tableaux ou listes numérotées pour faciliter le parsing.
5. **Spécifier la récence** — Si la fraîcheur compte, dire "focus sur les sources 2025-2026" ou "données les plus récentes disponibles."
6. **Une question de recherche par appel** — Garder les prompts focalisés. Lancer plusieurs appels en parallèle pour différents angles.
7. **Limiter la longueur du prompt** — Garder sous ~2000 mots.

### Templates de prompts

**Recherche marché/industrie approfondie :**
```
Recherche l'état actuel de [sujet/industrie] dans [géographie/contexte].
J'ai besoin de :
- Tendances et évolutions clés (2025-2026)
- Acteurs majeurs et leur positionnement
- Taille de marché ou données de croissance si disponibles
- Case studies ou exemples notables
Cite tes sources (URLs ou noms de rapports). Structure en bullet points.
```

**Recherche entreprise/concurrents :**
```
Recherche [nom d'entreprise] — j'ai besoin d'informations actuelles :
- Mouvements stratégiques récents, partenariats ou lancements produit
- Indicateurs financiers clés ou levées de fonds
- Changements de leadership et d'organisation
- Positionnement marché vs concurrents
Focus sur les informations 2025-2026. Cite les sources.
```

**Recherche technologie/outil :**
```
J'évalue [technologie/outil/approche] pour [cas d'usage].
Recherche :
- Maturité et adoption actuelles (qui l'utilise, à quelle échelle)
- Forces, limites et pièges connus
- Alternatives et comparaison
- Benchmarks ou case studies récents
Cite les sources. Sois précis avec les numéros de version et dates.
```

**Recherche réglementaire/politique :**
```
Recherche le paysage réglementaire actuel pour [sujet] dans [pays/région].
J'ai besoin de :
- Réglementations et cadres clés en vigueur
- Changements récents ou législation à venir
- Exigences de conformité pour [type d'organisation]
- Tendances d'application ou cas notables
Cite les sources officielles quand c'est possible.
```

**Preuves pour un livrable :**
```
Je prépare [type de livrable] pour [contexte client].
J'ai besoin de preuves réelles pour appuyer [affirmation ou recommandation spécifique] :
- Case studies d'organisations qui [ont fait X] avec des résultats quantifiés
- Statistiques ou benchmarks sectoriels
- Avis d'experts ou rapports d'analystes
Cite toutes les sources. Priorise les sources crédibles et récentes.
```

**Stress-test de raisonnement :**
```
Je conseille sur [sujet]. Ma conclusion est [X] parce que [raisons].
Cherche sur le web des contre-preuves ou perspectives alternatives.
Quels sont les contre-arguments les plus forts ? Qu'est-ce que je manque potentiellement ?
Réponds en 5-10 bullet points avec sources.
```

**Vérification factuelle avec sources :**
```
Vérifie l'affirmation suivante en cherchant sur le web : [affirmation]
Est-ce exact ? Quelle est l'information actuelle et correcte ?
Cite les sources spécifiques.
```

## Workflow de recherche

### Pattern de recherche parallèle

Pour une recherche complète, lancer sa propre recherche WebSearch ET l'oracle en parallèle :

1. **Toi** cherches avec WebSearch pour des résultats rapides et ciblés
2. **L'oracle** fait une synthèse plus profonde via Gemini (qui cherche et recoupe de multiples sources)
3. **Toi** fusionnes les deux ensembles de résultats, dédupliques, et synthétises pour l'utilisateur

Cela donne une couverture plus large que chaque outil seul.

### Recherche multi-angles

Pour les sujets complexes, faire plusieurs appels Gemini en parallèle avec des angles différents :

```
# Appel 1 : Vue d'ensemble du marché
# Appel 2 : Concurrents clés
# Appel 3 : Contexte réglementaire
```

Puis synthétiser à travers tous les résultats.

## Comment utiliser la réponse

1. **Recouper** — Comparer les résultats de Gemini avec ses propres résultats WebSearch. Les résultats convergents sont plus fiables.
2. **Vérifier les affirmations clés** — Si une statistique ou un fait est critique pour un livrable, vérifier que la source citée existe.
3. **Synthétiser, ne pas copier** — Intégrer les insights dans sa propre analyse. Ne pas coller la sortie de Gemini directement.
4. **Citer les sources** — Quand Gemini fournit des URLs ou noms de sources, les inclure dans l'output à l'utilisateur.
5. **Signaler l'incertitude** — Si Gemini et sa propre recherche divergent, présenter les deux perspectives à l'utilisateur.
6. **Attribuer quand c'est pertinent** — Pour des contributions de recherche substantielles, mentionner l'utilisation d'outils de recherche approfondie.

## Sélection de modèle et fallback

**Essayer pro d'abord, basculer sur flash automatiquement.** Le endpoint free-tier sature fréquemment sa capacité sur gemini-2.5-pro — quand ça arrive, retenter le même prompt avec flash.

- **`gemini-2.5-pro`** (essayer d'abord) : Meilleur pour la recherche approfondie, la synthèse complexe, l'analyse multi-sources.
- **`gemini-2.5-flash`** (fallback) : Rapide, fiable, suffisant pour la plupart des tâches. Toujours disponible en fallback.

**Pattern de fallback :** Toujours tenter pro d'abord. Si la sortie contient `MODEL_CAPACITY_EXHAUSTED`, `429`, ou `RESOURCE_EXHAUSTED`, retenter immédiatement le même prompt avec flash. Ne pas demander à l'utilisateur — le faire silencieusement.

```bash
# Étape 1 : Essayer pro
/Users/jesseparot/.local/bin/gemini -m gemini-2.5-pro -p "Votre prompt" 2>&1

# Étape 2 : Si pro échoue avec erreur de capacité → retenter avec flash (même prompt)
/Users/jesseparot/.local/bin/gemini -m gemini-2.5-flash -p "Votre prompt" 2>&1
```

## Timeout

- **Requêtes de recherche** : Utiliser un timeout de 120s sur l'outil Bash (`timeout: 120000`) — la recherche web + synthèse prend du temps
- **Vérifications factuelles rapides** : Le timeout par défaut de 30s suffit
- Si un appel bloque, le timeout de l'outil Bash le rattrapera

## Gestion des erreurs

Puisqu'on utilise `2>&1`, les erreurs seront visibles dans la sortie. Les gérer intelligemment :

- **`MODEL_CAPACITY_EXHAUSTED` / 429 sur gemini-2.5-pro** — Retenter avec `-m gemini-2.5-flash`. C'est l'erreur la plus fréquente (limites de capacité free-tier). Ne PAS retenter avec le même modèle.
- **`MODEL_CAPACITY_EXHAUSTED` / 429 sur flash** — Attendre et retenter une fois (flash récupère généralement en 1-2s). Si ça échoue encore, basculer sur WebSearch.
- **Erreurs d'auth** — Informer l'utilisateur qu'il doit se ré-authentifier en lançant `gemini` dans le terminal.
- **Réponse vide ou timeout** — Basculer sur WebSearch. Ne pas bloquer sur un échec de l'oracle.
- **Warnings de dépréciation `punycode`** — Les ignorer, ce sont des warnings Node.js inoffensifs.
- **Résultats semblent minces** — Reformuler la requête ou décomposer en sous-questions plus spécifiques.
