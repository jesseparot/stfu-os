# Todo — STFU OS

Backlog des chantiers d'amélioration du plugin. Séquençage : chantier 1 d'abord (socle), puis 2 (skills), puis 3-5 en parallèle.

---

## Chantier 1 — Refondre le socle de contexte

**Pourquoi** : `stfu-context.md` est descriptif mais pas opératoire. Un concurrent pourrait copier 80% du doc. Il manque le savoir-faire distinctif, les partis-pris, les anti-patterns.

**Méthode** : interviews structurées Jesse → rédaction → validation.

### Docs à créer/réécrire

- [ ] **stfu-context.md** — Enrichir : profils types de l'équipe (pas noms), ADN entrepreneurial, ce qu'on ne fait PAS, positionnement vs ESN/Big4/agences
- [ ] **stfu-methodologies.md** (nouveau) — Design Thinking version STFU, formats de sprint réels, outils terrain, séquençage type d'une mission
- [ ] **stfu-differentiators.md** (nouveau) — Partis-pris explicites : pourquoi terrain > desk research, pourquoi ex-entrepreneurs, pourquoi bout-en-bout, anti-patterns qu'on refuse
- [ ] **stfu-missions-types.md** (nouveau) — Typologie des missions (exploration, programme intra, accélération, coaching, formation) avec durée, livrables attendus, KPIs, pricing indicatif
- [ ] **glossary.md** — Étoffer à 50+ termes, corrections fréquentes, vocabulaire interne vs client

### Interviews à mener

1. STFU en 5 partis-pris : qu'est-ce qu'on refuse ? Qu'est-ce qui différencie *vraiment* ?
2. Typologie des missions : 4-5 types avec exemples concrets
3. Méthodo réelle : sprint type, outils utilisés, livrables réels
4. Anti-patterns : erreurs de junior consultant corrigées le plus souvent

---

## Chantier 2 — Remplir les références manquantes des skills

**Pourquoi** : propale, stfu-slides, user-test-restitution, workshop-debrief pointent vers des `references/` et `assets/` qui n'existent pas. Sans ça, Claude improvise au lieu d'appliquer la méthode STFU.

**Méthode** : partir de vrais livrables passés, extraire le pattern, formaliser.

- [ ] **propale** — `references/framework.md`, `references/chiffrage.md`, `assets/template.md` (partir de 2-3 vraies propales livrées)
- [ ] **stfu-slides** — `references/design-rules.md`, `references/slide-types.md` (formaliser à partir de vrais decks)
- [ ] **user-test-restitution** — `references/individual-patterns.md`, `references/synthesis-patterns.md` (partir de vrais rapports)
- [ ] **workshop-debrief** — `references/photo-extraction-protocol.md`, `references/workshop-types.md` (formaliser la méthode réelle)

---

## Chantier 3 — Back pressure & qualité

**Pourquoi** : aucun mécanisme de qualité systématique. Pas de critères de validation, pas de checklist, pas de "definition of done".

- [ ] **Critères de qualité par livrable** — Checklist "definition of done" intégrée dans chaque skill (ex: une propale doit avoir X sections, des chiffres, une timeline)
- [ ] **Agent `quality-review`** — Remplacer l'usage de `/verify` (générique, même contexte) par un agent STFU dédié. Subagent = contexte frais, pas de biais de confirmation. Reçoit le livrable + type, charge les critères STFU spécifiques, vérifie ton/structure/complétude/anti-patterns, retourne verdict structuré (pass/fix). Prérequis : avoir les critères de qualité par livrable (item ci-dessus)
- [ ] **Exemples gold standard** — 1 exemple anonymisé par skill livrable, servant de benchmark
- [ ] **Anti-patterns explicites** — Par skill : "ne jamais faire X, Y, Z" — erreurs courantes de junior

---

## Chantier 4 — Granularité des skills

**Pourquoi** : certains skills font trop ou pas assez. D'autres manquent pour des tâches récurrentes.

### Skills à retravailler

- [ ] **propale** — Découper : brief/qualification (amont) vs rédaction (aval) vs chiffrage (spécifique)
- [ ] **case-study-slide** — Enrichir : multi-slides, choix de format, vrais exemples visuels
- [ ] **mission-airtable** — Réécrire : moins spec-sheet, plus guidé et contextuel
- [ ] **setup** — Étoffer : validation plus poussée, onboarding progressif

### Skills à créer

- [ ] **interview-guide** — Préparer des guides d'entretien terrain (récurrent dans les missions STFU)
- [ ] **benchmark** — Matrices de benchmark structurées (format réel STFU, pas générique)
- [ ] **business-case** — P&L, sizing, hypothèses — format distinct de la propale

---

## Chantier 5 — Détailler les approches méthodologiques

**Pourquoi** : les skills utilisent "Design Thinking" comme un label sans détailler les formats concrets.

- [ ] **Formats de sprint** — Demi-journée, journée, semaine — avec séquençage réel
- [ ] **Outils terrain** — Quels outils pour quels exercices (pas juste "Design Thinking")
- [ ] **Templates d'atelier** — Ice-breakers, exercices divergence/convergence, formats de restitution
- [ ] **Séquençage type par mission** — Exploration (8 sem), accélération (12 sem), etc.

---

## Ancien backlog (MVP)

### Templates à refondre

- [ ] **Rapport d'exploration** — Repartir d'un vrai rapport livré vs squelette textbook actuel
- [ ] **Brief projet** — Comparer avec les vrais briefs utilisés en mission
- [ ] **Proposition commerciale** — Aligner sur le format réel (subsumé par chantier 2 / propale)
- [ ] **Contracts** — Dossier vide. Décider : template contrat-cadre/bon de commande, ou supprimer

### Décisions en attente

- [ ] **Local vs Slite** — Les docs de référence restent dans le repo ou migrent vers Slite ? (Si Slite, les skills doivent interroger Slite MCP plutôt que lire des fichiers locaux)

---

## Chantier 6 — Migration Google Workspace : MCP → gws CLI

**Pourquoi** : le serveur MCP communautaire (`workspace-mcp` via `uvx`) dépend d'un mainteneur unique, nécessite un runtime Python, et inscrit 62 outils dans le contexte. La CLI `gws` (Rust, Google officieux) offre une découverte dynamique des APIs, du JSON structuré, et zéro coût de contexte baseline.

**Statut** : en pause. La CLI est installée et fonctionnelle localement (Jesse), mais le setup équipe est trop lourd vs le MCP actuel. On attend que le bug d'encryption keyring macOS soit résolu (issue #360).

**Ce qui est fait** :
- [x] `gws` CLI v0.9.1 installé (`npm install -g @googleworkspace/cli`)
- [x] Projet GCP dédié créé (`stfu-gws-cli`)
- [x] APIs activées (Drive, Docs, Sheets, Slides, Gmail, Calendar)
- [x] Auth fonctionnelle via workaround ADC (`gcloud auth application-default login`)
- [x] Validé : Drive search, Slides get/thumbnail — OK

**Ce qui reste** :
- [ ] **Attendre fix encryption macOS** — issue googleworkspace/cli#360. Quand résolu, le setup devient `npm install -g @googleworkspace/cli && gws auth login` (2 commandes)
- [ ] **Réécrire 7 skills STFU** — Remplacer les appels `mcp__google-workspace__*` par `gws` CLI via Bash (stfu-drive, stfu-slides, case-study-slide, propale, analyse-ao, mission-to-outbound, batch-update-patterns)
- [ ] **Retirer le serveur MCP** — Supprimer l'entrée `google-workspace` de `.mcp.json`
- [ ] **Mettre à jour le tuto setup** — `tuto/google-workspace-mcp-setup.md` → gws auth
- [ ] **Script setup équipe** — Automatiser l'install + auth pour les collègues

**Rollback** : `git checkout -- .` + re-add MCP dans `.mcp.json`. Le MCP ne nécessite aucune installation (`uvx` tourne à la volée).

---

*Créé le 2026-02-23 · Refondu le 2026-03-10*
