# stfu-os — Plugin Claude Code

Plugin Claude Code pour **Start The F*** Up**, studio de conseil en innovation.

Fournit les skills, conventions, MCP et workflows du studio.

## Prerequis

- [Claude Code](https://claude.ai/claude-code) installe
- Node.js / npx (pour les serveurs MCP)
- uv / uvx (`brew install uv`) — pour le MCP Google Workspace
- Gemini CLI (`gemini`) en PATH — pour le skill oracle

## Installation

### Depuis le source (mainteneur)

```bash
cd ~/stfu-workspace
claude --plugin-dir ~/stfu-os
```

### Marketplace (equipe)

```bash
# A venir — pour l'instant utiliser --plugin-dir
```

## Setup initial

### 1. Creer le workspace

```bash
mkdir -p ~/stfu-workspace/{projects,sales/{appels-d-offres,leads,outbound},internal,templates,methodologies,_inbox,_archive,_pipeline-artefacts,.claude/skills}
```

### 2. Configurer les secrets

```bash
# Copier le template
cp ~/stfu-os/.env.example ~/stfu-workspace/.env
# Editer avec vos vraies valeurs

# Ajouter le sourcing dans ~/.zshrc :
echo '[ -f "$HOME/stfu-workspace/.env" ] && { set -a; source "$HOME/stfu-workspace/.env"; set +a; }' >> ~/.zshrc
source ~/.zshrc
```

### 3. Proteger les fichiers .env

Ajouter ces regles dans `~/stfu-workspace/.claude/settings.json` pour empecher Claude de lire les secrets :

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)"
    ]
  }
}
```

Voir `tuto/secrets-setup.md` pour le detail des cles API.

### 4. Authentification Google

Voir `tuto/google-workspace-mcp-setup.md` pour le guide complet.

## Skills disponibles

### Plugin (fournis par stfu-os)

| Skill | Commande | Description |
|-------|----------|-------------|
| stfu-core | *(auto)* | Instructions fondamentales, contexte, conventions, workflows |
| stfu-writing | *(auto)* | Regles de style appliquees a tout contenu |
| methode-beta-gouv | *(auto)* | Methodologie coaching beta.gouv |
| stfu-drive | *(auto)* | Navigation Google Drive STFU Team |
| oracle | *(auto)* | Recherche approfondie via Gemini + second avis |
| mermaid-stfu | *(auto)* | Diagrammes Mermaid brandes |
| stfu-slides | `/stfu-slides` | Design engine Google Slides |
| market-research | `/market-research` | Etude de marche et benchmark |
| appel-d-offres | `/appel-d-offres` | Brief d'appels d'offres |
| propale | `/propale` | Proposition commerciale |
| mission-airtable | `/mission-airtable` | Capitalisation mission dans Airtable |
| mission-to-outbound | `/mission-to-outbound` | Plan de prospection outbound |
| case-study-slide | `/case-study-slide` | Slide case study depuis Airtable |
| list-gen | `/list-gen` | Listes de prospects enrichies |
| sales-nav | *(auto)* | Expert Sales Navigator |
| lemlist | `/lemlist` | Automation Lemlist |
| user-test-restitution | `/user-test-restitution` | Restitution tests utilisateurs |

### Workspace (dans ~/stfu-workspace/.claude/skills/)

| Skill | Commande | Description |
|-------|----------|-------------|
| organize-file | `/organize-file` | Organiser les fichiers de l'inbox |
| project-init | `/project-init` | Initialiser un projet |
| clean-workspace | `/clean-workspace` | Scan et nettoyage du workspace |

## Guides

- [Configuration des secrets](tuto/secrets-setup.md)
- [Google Workspace MCP](tuto/google-workspace-mcp-setup.md)
- [Setup Claude Code](tuto/claude-code-setup.md)

## Architecture

```
stfu-os/ (plugin)           stfu-workspace/ (workspace)
├── .claude-plugin/         ├── .claude/
│   └── plugin.json         │   ├── CLAUDE.md
├── skills/                 │   ├── settings.local.json
│   ├── stfu-core/          │   └── skills/
│   ├── appel-d-offres/     │       ├── organize-file/
│   ├── propale/            │       ├── project-init/
│   ├── stfu-slides/        │       └── clean-workspace/
│   ├── oracle/             ├── projects/
│   └── ...                 ├── sales/
├── .mcp.json               ├── _inbox/
├── conventions.md          ├── _archive/
├── glossary.md             └── .env
├── stfu-context.md
└── tuto/
```

**Plugin (Git)** = comment on travaille — skills, config, conventions.
**Workspace (local)** = sur quoi on travaille — projets, sales, livrables.
**Cloud (Slite, Drive, Airtable)** = source de verite du contenu.
