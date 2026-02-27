# Catalogue des skills STFU

Index des skills disponibles pour le workspace STFU.

---

## Skills disponibles

| Skill | Commande | Description |
|-------|----------|-------------|
| [appel-d-offres](./appel-d-offres/SKILL.md) | `/appel-d-offres` | Brief d'appels d'offres français - extrait les infos clés et évalue le fit STFU |
| [propale](./propale/SKILL.md) | `/propale` | Proposition commerciale STFU — framework McKinsey 8 sections, recherche missions Airtable, draft markdown prêt pour /stfu-slides |
| [stfu-writing](./stfu-writing/SKILL.md) | *(auto)* | Règles de style STFU - appliqué automatiquement à tous les contenus |
| qualify (global) | *(auto)* | Qualification du brief avant tout livrable - force l'alignement sur l'output attendu |
| [organize-file](./organize-file/SKILL.md) | `/organize-file` | Organisation automatique des fichiers de l'inbox |
| [user-test-restitution](./user-test-restitution/SKILL.md) | `/user-test-restitution` | Génère des restitutions professionnelles de tests utilisateurs |
| [methode-beta-gouv](./methode-beta-gouv/SKILL.md) | *(auto)* | Guide méthode beta.gouv pour les missions de coaching - phases, comité d'investissement, AARRI, posture coach STFU |
| [stfu-drive](./stfu-drive/SKILL.md) | *(auto)* | Navigation et gestion du Google Drive STFU Team - recherche de fichiers, dossiers clients, livrables |
| [project-init](./project-init/SKILL.md) | `/project-init` | Initialise un projet — dossier local, manifest, Slite, Drive |
| [mission-airtable](./mission-airtable/SKILL.md) | `/mission-airtable` | Crée une fiche mission Airtable à partir des fichiers d'un projet client |
| [oracle](./oracle/SKILL.md) | *(auto)* | Deep research via Gemini (web search, synthèse multi-sources) + second opinion pour challenger le raisonnement |
| [mission-to-outbound](./mission-to-outbound/SKILL.md) | `/mission-to-outbound` | Plan de prospection outbound complet à partir d'une mission STFU réplicable — ICP, personas, filtres Sales Nav, séquences email, stress-test oracle, publication Slite |
| [sales-nav](./sales-nav/SKILL.md) | *(auto)* | Expert Sales Navigator — filtres, boolean, estimation volume, best practices (FR). Mobilisé par mission-to-outbound et activable sur tout sujet Sales Nav. |
| [lemlist](./lemlist/SKILL.md) | `/lemlist` | Expert Lemlist automation — audit, stratégie, création de campagnes, sourcing leads, optimisation outreach |
| [case-study-slide](./case-study-slide/SKILL.md) | `/case-study-slide` | Génère une présentation Google Slides case study à partir d'une mission Airtable — copie le template, injecte les données |
| [list-gen](./list-gen/SKILL.md) | `/list-gen` | Génération et enrichissement de listes de prospects — brief, stratégie Sales Nav, analyse, enrichissement Dropcontact, livraison Drive/Lemlist |
| [market-research](./market-research/SKILL.md) | `/market-research` + *(auto)* | Étude de marché et benchmark concurrentiel via Linkup deep search + oracle — paysage concurrentiel, sizing, profils entreprises, tendances |
| [mermaid-stfu](./mermaid-stfu/SKILL.md) | *(auto)* | Diagrammes Mermaid brandés STFU — palette gris + accent jaune, typographie Lato, export PNG/SVG |
| [stfu-slides](./stfu-slides/SKILL.md) | `/stfu-slides` + *(auto)* | Design engine Google Slides brandées STFU — choix de layout, styling typo, compositions custom, self-review visuel via thumbnails |
| [clean-workspace](./clean-workspace/SKILL.md) | `/clean-workspace` | Scan et nettoyage du workspace — détecte brouillons anciens, scratch, artefacts, orphelins, DCE expirés, cross-check Slite/Drive |

---

## Comment utiliser un skill

### Invocation directe
```
/appel-d-offres /chemin/vers/dce.pdf
```

### Skills automatiques
Certains skills (comme `stfu-writing`) sont appliqués automatiquement à tout le contenu produit.

---

## Structure d'un skill

Chaque skill est un dossier contenant :
```
skill-name/
├── SKILL.md      # Définition du skill (front matter YAML + instructions)
└── scripts/      # Scripts additionnels si nécessaire (optionnel)
```

### Front matter requis

```yaml
---
name: skill-name
description: Description courte pour le catalogue et la détection automatique.
---
```

---

## Créer un nouveau skill

Utiliser `/skill-creator` pour créer ou modifier un skill de manière guidée.

---

*Derniere mise a jour : 2026-02-26*
