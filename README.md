# STFU - Start The F*** Up

Studio d'innovation - Workspace AI-augmented

## Structure

```
stfu-os/
├── .claude/                 # Instructions Claude et skills
│   ├── CLAUDE.md
│   └── skills/
│
├── tuto/                    # Guides partenaires
│   └── secrets-setup.md
│
├── .mcp.json                # Config MCP (secrets via ${VAR})
├── .env.example             # Template des secrets
├── .gitignore               # Exclut _workspace/, .env, binaires
│
├── conventions.md           # Regles de nommage et structure
├── glossary.md              # Noms propres
├── stfu-context.md          # Contexte entreprise
│
└── _workspace/              # Travail local (GITIGNORED)
    ├── projects/            # Projets actifs (flat)
    ├── sales/               # Pipeline commercial
    │   ├── appels-d-offres/
    │   ├── leads/
    │   └── outbound/
    ├── templates/           # Structures reutilisables (migration Slite)
    ├── methodologies/       # Process, frameworks (migration Slite)
    ├── internal/            # Docs strategie OS
    ├── _inbox/              # Zone de depot
    └── _archive/            # Termine
```

**Tracked (git)** : tool layer — skills, config, conventions, guides partenaires.
**`_workspace/` (gitignored)** : content layer — tout le travail actif. Migre progressivement vers Slite/Drive.

## Conventions de nommage

Voir `conventions.md` pour le detail. En bref :

- **Projets** : `{client}-{sujet}` (ex: `totalenergies-plug-charge`)
- **Documents draft** : `type-sujet_draft.md`
- **Documents final** : `type-sujet_final.md`
- **CR** : `cr-YYYY-MM-DD-sujet.md`

## Workflows

### Nouvel appel d'offres

1. Deposer le DCE dans `_workspace/_inbox/` ou `_workspace/sales/appels-d-offres/{organisme}-{sujet}-{YY-MM}/`
2. Lancer `/appel-d-offres` pour generer le brief
3. Go/no-go note dans le README du dossier

### Nouveau lead

1. Creer `_workspace/sales/leads/{entreprise}-{contact}-{sujet}/`
2. Creer README.md avec infos lead

### Lead converti en client

1. Lancer `/project-init` (dossier local, manifest, Slite, Drive)
2. Archiver le lead

### Fin de mission

1. Capitaliser dans Airtable (via `/mission-airtable`)
2. Archiver dans `_workspace/_archive/`

## Skills disponibles

| Skill | Usage |
|-------|-------|
| `/project-init` | Initialiser un projet |
| `/appel-d-offres` | Brief d'un appel d'offres |
| `/organize-file` | Organiser un fichier de l'inbox |
| `/debrief` | Debrief reunion depuis Granola |
| `/mission-to-outbound` | Plan prospection depuis une mission |
| `/case-study-slide` | Slide case study depuis Airtable |
| `/list-gen` | Listes de prospection enrichies |

## AI-ready

- Chaque dossier projet contient un `README.md` manifest
- Les conventions sont dans `conventions.md` (source de verite)
- Les instructions Claude sont dans `.claude/CLAUDE.md`
- Les secrets sont dans `.env` (gitignored), pas dans `.mcp.json`
