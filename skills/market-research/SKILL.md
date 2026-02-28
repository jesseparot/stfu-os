---
name: market-research
description: >
  Recherche de marché et benchmark concurrentiel via Linkup deep search + oracle.
  Utiliser pour rechercher un marché, benchmarker des concurrents, analyser une industrie,
  dimensionner un marché, cartographier un paysage concurrentiel, ou investiguer des entreprises/tendances.
  Aussi activé AUTOMATIQUEMENT quand une tâche bénéficierait d'intelligence de marché structurée —
  ex. préparation d'une proposition, évaluation d'une nouvelle verticale, ou appui d'une recommandation
  stratégique avec des données réelles. Produit un output markdown structuré.
user_invocable: true
---

# Recherche de marché & Benchmark concurrentiel

Recherche de marché structurée propulsée par Linkup deep search (principal), oracle/Gemini (complémentaire), et WebSearch (fallback). Produit de l'intelligence actionnable en markdown local.

## Invocation

```
/market-research <sujet ou question>
```

**Exemples :**
```
/market-research marché des chatbots RH en France
/market-research competitors to Miro for collaborative whiteboarding
/market-research IA générative dans le secteur bancaire européen
/market-research company profile: Mistral AI
```

Se déclenche aussi automatiquement quand une tâche implique une analyse de marché, de l'intelligence concurrentielle, ou de la recherche sectorielle.

## Entrées

- Un sujet de recherche, une question, un marché ou un nom d'entreprise
- Optionnel : périmètre géographique, industrie, période, angles spécifiques

Si l'entrée est vague, utiliser `AskUserQuestion` pour qualifier :
- Quel est le contexte business ? (projet client, proposition, prospection, stratégie interne)
- Périmètre géographique ? (France, Europe, mondial)
- Angles spécifiques ? (concurrents, taille de marché, tendances, réglementation, profils d'entreprises)
- Profondeur ? (scan rapide vs deep dive)

## Outils de recherche

### Principal : Linkup MCP (recherche web approfondie)

Les outils Linkup sont préfixés `mcp__linkup__`. Deux outils principaux :

**`mcp__linkup__linkup-search`** — Recherche web temps réel sur des sources de confiance.
- `query` : requête en langage naturel — **les questions complètes fonctionnent mieux** (pas de keyword stuffing)
- `depth` : `"standard"` (rapide, réponses directes) ou `"deep"` (recherche complète multi-sources)

**Quand utiliser chaque profondeur :**
- **Standard** — vérifications factuelles rapides, points de données spécifiques, actualités récentes, questions à réponse unique
- **Deep** — dimensionnement de marché, paysages concurrentiels, synthèse multi-sources, analyse de tendances, tout ce qui nécessite un recoupement

**`mcp__linkup__linkup-fetch`** — Extraire le contenu complet d'une page web depuis une URL.
- `url` : URL de la page cible
- `renderJs` : `true` pour activer le rendu JavaScript sur les sites dynamiques/SPA (plus lent mais nécessaire pour les pages JS-heavy)

### Complémentaire : Oracle (recherche approfondie Gemini)

Utiliser le skill oracle pour :
- Recouper les résultats Linkup avec une intelligence web plus large
- Obtenir une analyse synthétisée de multiples sources en une fois
- Stress-tester des conclusions
- Sujets où les résultats Linkup sont minces

Invocation oracle (voir `oracle/SKILL.md` pour les détails complets) :
```bash
gemini -m gemini-2.5-pro -p "Prompt de recherche ici" 2>&1
# Fallback vers flash en cas d'erreur de capacité
```

### Complémentaire : WebSearch

Utiliser WebSearch en parallèle de Linkup pour :
- Angles de recherche différents sur le même sujet (diversifie les sources)
- Recherches ciblées rapides (stats spécifiques, dates, faits)
- Quand le quota Linkup doit être préservé

## Workflow

### Étape 1 — Qualifier le brief de recherche

Comprendre ce qui est nécessaire avant de chercher. Si invoqué manuellement avec un sujet clair, passer directement à la recherche. Si le contexte est ambigu, utiliser `AskUserQuestion` :

- **Contexte business** : pourquoi cette recherche est-elle nécessaire ? (façonne l'output)
- **Périmètre** : limites géographiques, temporelles, sectorielles
- **Questions clés** : quelles questions spécifiques l'output doit-il répondre ?
- **Type de sortie** : cartographie de paysage, profils d'entreprises, dimensionnement de marché, analyse de tendances, tableau comparatif (voir Types de sortie ci-dessous)

### Étape 2 — Concevoir la stratégie de recherche

Planifier 3-5 angles de recherche parallèles avant d'exécuter. Mapper chaque angle au meilleur outil et profondeur :

| Angle | Outil | Profondeur | Exemple de requête |
|-------|-------|------------|---------------------|
| Paysage concurrentiel | Linkup search | **deep** | `"Quelles sont les principales entreprises de chatbots IA pour les RH en Europe ? Quel est leur positionnement et leur financement ?"` |
| Taille du marché & données | Linkup search | **deep** | `"Quelle est la taille actuelle du marché des chatbots RH en Europe ? Taux de croissance et projections ?"` |
| Développements récents | Linkup search | **standard** | `"Dernières actualités et levées de fonds HR tech chatbots 2025 2026"` |
| Deep-dive entreprise spécifique | Linkup fetch | — | Extraire depuis le site web de l'entreprise, page about, ou communiqués de presse |
| Synthèse large & validation | Oracle | — | `"Rechercher le marché des chatbots RH en Europe..."` |
| Points de données rapides | WebSearch | — | Stats spécifiques, dates, info réglementaire |

**Principe clé :** Utiliser **deep** pour les questions de recherche principales (2-3 requêtes max — elles sont approfondies mais coûtent plus). Utiliser **standard** pour les lookups complémentaires.

### Étape 3 — Exécuter les recherches en parallèle

Lancer les recherches en parallèle pour maximiser la vitesse :

1. **Lancer 2-3 recherches Linkup deep** sur les questions de recherche principales
2. **Lancer 1-2 recherches Linkup standard** pour les actualités récentes / faits rapides
3. **Lancer l'oracle** en parallèle pour une synthèse indépendante sur la question principale
4. **Lancer WebSearch** pour les points de données spécifiques nécessaires

Toutes les recherches indépendantes doivent être lancées simultanément.

### Étape 4 — Lecture approfondie des sources clés

Depuis les résultats de recherche, identifier 5-10 pages à haute valeur et extraire le contenu complet :

1. Utiliser `mcp__linkup__linkup-fetch` sur les URLs les plus prometteuses des résultats de recherche
2. Mettre `renderJs: true` pour les sites dynamiques (pages d'entreprises, dashboards, rapports interactifs)
3. Lire et synthétiser — chercher : chiffres, dimensionnement de marché, positionnement concurrentiel, tendances, citations

### Étape 5 — Synthétiser et structurer

Fusionner tous les résultats dans un output structuré. Règles :

- **Dédupliquer** entre les sources — un même fait de multiples sources = confiance plus élevée
- **Tout citer** — chaque affirmation a besoin d'une URL source ou d'un nom de source
- **Signaler l'incertitude** — si des données sont contradictoires entre sources, présenter les deux avec une note
- **Quantifier quand c'est possible** — taille de marché en €/$, taux de croissance en %, métriques d'entreprises
- **Dater les données** — toujours noter la date d'une statistique (ex. "au T3 2025")
- **Séparer faits et interprétation** — présenter les données d'abord, puis l'analyse/recommandations STFU

### Étape 6 — Cross-valider les affirmations clés (optionnel mais recommandé)

Pour la recherche à forts enjeux (livrables clients, propositions), lancer un stress-test oracle :

```
Voici ma synthèse de recherche de marché sur [sujet] :
[Résumé des principaux résultats]

Recherche sur le web pour vérifier :
1. Ces chiffres de taille de marché sont-ils précis et à jour ?
2. Est-ce que je manque des acteurs majeurs ?
3. Y a-t-il des contre-tendances ou risques que je ne vois pas ?
4. Quel est le contre-argument le plus fort à [conclusion clé] ?
```

Intégrer les corrections valides. Documenter ce qui a été confirmé vs ajusté.

### Étape 7 — Rédiger l'output

Générer un fichier markdown structuré. Utiliser le template de sortie approprié (voir ci-dessous).

**Emplacement du fichier :** écrire dans le répertoire de travail actuel ou `.temp/` si pas de contexte projet.
**Convention de nommage :** `market-research-{topic-slug}_draft.md`

## Types de sortie

### A. Paysage concurrentiel

```markdown
# Étude de marché — {Sujet}

_Recherche générée par /market-research — {Date}_

## Résumé exécutif

{2-3 paragraphes : résultats clés, dynamiques de marché, implications STFU}

## Paysage concurrentiel

### Vue d'ensemble

{Description du marché, taille si disponible, trajectoire de croissance}

### Acteurs clés

| Acteur | Positionnement | Taille/Funding | Forces | Faiblesses | Source |
|--------|---------------|----------------|--------|------------|--------|
| ... | ... | ... | ... | ... | [lien] |

### Cartographie

{Analyse du positionnement : qui concurrence sur quelles dimensions, lacunes du marché}

## Tendances clés

1. **{Tendance 1}** — {Description + preuves + source}
2. **{Tendance 2}** — ...

## Implications STFU

- {Ce que cela signifie pour le positionnement/clients de STFU}
- {Opportunités identifiées}
- {Risques ou points de vigilance}

## Sources

- [{Titre}]({URL}) — {Brève note sur ce qui a été extrait}
- ...
```

### B. Profil d'entreprise

```markdown
# Profil entreprise — {Entreprise}

_Recherche générée par /market-research — {Date}_

## Fiche d'identité

| | |
|---|---|
| **Nom** | {Entreprise} |
| **Fondation** | {Année} |
| **Siège** | {Localisation} |
| **Effectif** | {Taille} |
| **Funding / CA** | {Revenus ou financement} |
| **Secteur** | {Industrie} |
| **Site** | [{URL}]({URL}) |

## Positionnement et offre

{Ce qu'ils font, comment ils se positionnent, marché cible}

## Actualités récentes

- {Date} — {Événement/actualité + source}
- ...

## Forces et faiblesses

**Forces :** {Points}
**Faiblesses :** {Points}

## Sources

- ...
```

### C. Dimensionnement de marché

```markdown
# Dimensionnement marché — {Marché}

_Recherche générée par /market-research — {Date}_

## Résumé

{Chiffres clés : TAM/SAM/SOM si applicable, taux de croissance, géographie}

## Données de marché

| Indicateur | Valeur | Source | Date |
|-----------|--------|--------|------|
| Taille du marché | {€/$ X} | [{Source}]({URL}) | {Année} |
| Croissance annuelle | {X%} | ... | ... |
| ... | ... | ... | ... |

## Segmentation

{Par géographie, segment, cas d'usage — les dimensions pertinentes}

## Dynamiques de croissance

{Ce qui tire la croissance, ce qui la freine}

## Sources

- ...
```

### D. Tableau comparatif

```markdown
# Benchmark — {Sujet}

_Recherche générée par /market-research — {Date}_

## Critères de comparaison

{Pourquoi ces critères, ce qui compte pour l'évaluation}

## Comparatif

| Critère | {Acteur 1} | {Acteur 2} | {Acteur 3} | {Acteur 4} |
|---------|------------|------------|------------|------------|
| {Critère 1} | ... | ... | ... | ... |
| {Critère 2} | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| **Verdict** | ... | ... | ... | ... |

## Analyse

{Points clés du comparatif, recommandations}

## Sources

- ...
```

## Règles

- **Toujours citer les sources** — chaque affirmation, chiffre ou fait d'entreprise a besoin d'une URL ou d'un nom de source. Pas d'assertion sans source.
- **Tout dater** — des données de marché sans date ne valent rien. Toujours noter l'année/trimestre.
- **Utiliser le mode deep pour les questions principales** — les 2-3 questions de recherche principales doivent utiliser `depth: "deep"`. Utiliser `"standard"` pour les lookups complémentaires.
- **Les questions complètes battent les mots-clés** — Linkup fonctionne mieux avec des questions en langage naturel, pas des chaînes de mots-clés. Rédiger les requêtes comme on les poserait à un analyste.
- **Exécution parallèle** — lancer toutes les recherches indépendantes simultanément. Ne pas sérialiser ce qui peut être parallélisé.
- **Français ou anglais selon le sujet** — recherche de marché client en français, technique/interne en anglais. S'aligner sur la langue de l'utilisateur.
- **Pas de données inventées** — si un chiffre de taille de marché est introuvable, écrire "non disponible" plutôt qu'estimer. Signaler ce qui manque.
- **Oracle pour la validation, pas la génération** — utiliser l'oracle pour recouper et stress-tester, pas comme source de données principale.
- **Angle STFU** — toujours conclure avec les implications pour STFU (positionnement, opportunités, pertinence client) quand la recherche est pour usage interne.

## Cas limites

| Cas | Comportement |
|-----|-------------|
| MCP Linkup indisponible | Fallback sur WebSearch + oracle. Noter la qualité réduite dans l'output. |
| Sujet très niche (peu de résultats) | Reformuler en questions plus larges, utiliser `linkup-fetch` sur toute URL pertinente trouvée, s'appuyer sur l'oracle pour la synthèse. |
| Données contradictoires entre sources | Présenter les deux valeurs avec leurs sources. Ne pas en choisir une silencieusement. |
| Pas de données de taille de marché | L'indiquer explicitement. Proposer des métriques proxy ou une méthodologie d'estimation si applicable. |
| L'utilisateur demande un scan rapide | Sauter les étapes 4-6. Faire 2-3 recherches Linkup standard, synthèse brève, pas d'extraction approfondie. |
| Recherche pour un livrable client | Workflow complet incluant le stress-test oracle. Standards de citation plus élevés. |
| Pages sources JS-heavy | Utiliser `linkup-fetch` avec `renderJs: true` pour extraire correctement le contenu. |

## Points d'extension

Quand des MCPs de recherche supplémentaires sont installés (Exa, Tavily, Brave), ils complètent Linkup :

| MCP | Meilleur pour | Ajout au workflow |
|-----|---------------|-------------------|
| Exa | Recherche sémantique/neurale, découverte d'entreprises, recherche filtrée par catégorie | Étape 3 — découverte parallèle d'entreprises/papers de recherche |
| Tavily | Résultats structurés agent-native | Étape 3 — recherche parallèle structurée |
| Brave | Recherche keyword rapide, actualités, index indépendant | Étape 3 — veille actualités, développements temps réel |

Commandes d'installation (depuis le répertoire du projet stfu) :
```bash
claude mcp add -s project -e "EXA_API_KEY=xxx" exa -- npx -y exa-mcp-server
claude mcp add -s project --transport http tavily "https://mcp.tavily.com/mcp/?tavilyApiKey=xxx"
claude mcp add -s project -e "BRAVE_API_KEY=xxx" brave-search -- npx -y brave-search-mcp
```
