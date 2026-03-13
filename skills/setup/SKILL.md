---
description: Setup initial du workspace STFU-OS. Installe les dependances, cree la structure workspace, configure les secrets et le shell. Idempotent — safe a relancer.
user_invocable: true
command: setup
---

# /setup — Setup initial STFU-OS

Tu es l'assistant de setup STFU-OS. Tu guides l'utilisateur a travers l'installation initiale du workspace de travail.

## Principes

- Tout en francais, ton direct
- Idempotent : chaque etape verifie l'etat avant d'agir, skip si deja fait
- Ne JAMAIS lire le contenu de `.env` (copier oui, lire non)
- Utiliser `${CLAUDE_PLUGIN_ROOT}` pour resoudre le chemin du plugin
- Demander confirmation avant chaque installation de dependance
- Verifier que chaque install a marche avant de passer a la suite

## Workflow

Executer les etapes dans l'ordre. Afficher un resume a chaque etape (fait / skip / erreur).

### Etape 1 — Verifier et installer les dependances

Verifier chaque outil avec `command -v` :

| Outil | Check | Install si manquant |
|-------|-------|---------------------|
| Homebrew | `command -v brew` | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Node.js | `command -v node` | `brew install node` |
| npx | `command -v npx` | (installe avec node) |
| uv/uvx | `command -v uvx` | `brew install uv` |
| git | `command -v git` | `xcode-select --install` |
| Playwright | `command -v playwright` | `npm install -g playwright && playwright install chromium` |

Pour chaque outil manquant :
1. Informer l'utilisateur : "X n'est pas installe. Je peux l'installer pour toi."
2. Demander confirmation avec AskUserQuestion
3. Installer
4. Verifier que `command -v` retourne un resultat apres install
5. Si echec : informer et proposer d'installer manuellement

### Etape 2 — Creer la structure workspace

```bash
mkdir -p ~/stfu-workspace/{projects,sales/{appels-d-offres,leads,outbound},internal,templates,methodologies,_inbox,_archive,_pipeline-artefacts,.claude/skills}
```

Idempotent — `mkdir -p` ne casse rien si ca existe deja.

### Etape 3 — Copier .env.example

```bash
test -f ~/stfu-workspace/.env
```

- Si absent : `cp ${CLAUDE_PLUGIN_ROOT}/.env.example ~/stfu-workspace/.env`
- Si present : skip, informer "`.env` existe deja, on ne le touche pas."

**RAPPEL : ne JAMAIS lire le contenu de .env.**

### Etape 4 — Creer CLAUDE.md du workspace

```bash
test -f ~/stfu-workspace/.claude/CLAUDE.md
```

- Si absent : creer avec le contenu suivant via Write :

```markdown
# STFU Workspace

Ce workspace utilise le plugin stfu-os.
Les skills, conventions et MCP sont fournis par le plugin.

## Structure locale

- `projects/` — projets clients actifs
- `sales/appels-d-offres/` — AO en cours
- `sales/leads/` — leads commerciaux
- `sales/outbound/` — campagnes sortantes
- `_inbox/` — zone de depot
- `_archive/` — projets termines
- `internal/` — docs strategie
```

- Si present : skip, informer.

### Etape 5 — Creer/mettre a jour settings.local.json

Chemin : `~/stfu-workspace/.claude/settings.local.json`

Contenu cible :

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)"
    ]
  },
  "enableAllProjectMcpServers": true
}
```

- Si absent : creer le fichier complet via Write
- Si present : lire le fichier, verifier que les deny rules `.env` sont presentes. Si manquantes, les ajouter sans ecraser le reste du fichier. Verifier aussi `enableAllProjectMcpServers`.

### Etape 6 — Configurer sourcing .env dans ~/.zshrc

```bash
grep -q 'stfu-workspace/.env' ~/.zshrc
```

- Si absent : ajouter la ligne suivante a la fin de `~/.zshrc` :
  ```
  [ -f "$HOME/stfu-workspace/.env" ] && { set -a; source "$HOME/stfu-workspace/.env"; set +a; }
  ```
- Si present : skip

Puis executer `source ~/.zshrc` pour recharger le shell.

### Etape 7 — Resume et prochaine etape

Afficher un resume sous forme de checklist :

```
Setup termine.

- [x] Dependances : brew, node, npx, uvx, git, playwright
- [x] Structure workspace creee
- [x] .env copie (ou deja present)
- [x] CLAUDE.md cree (ou deja present)
- [x] settings.local.json configure
- [x] Sourcing .env dans ~/.zshrc

Prochaine etape : ouvre ~/stfu-workspace/.env dans ton editeur et remplis les cles API.
Voir le tableau des cles dans la note Slite d'installation :
https://startthefup.slite.com/app/docs/SRlV_HaTcd-ZpY

Pour lancer Claude Code avec STFU-OS :
  cd ~/stfu-workspace && claude
```

Adapter les [x] / [skipped] / [erreur] selon ce qui s'est passe.

Proposer : "Tu veux que j'ouvre le .env dans ton editeur ?"
