# Google Workspace MCP — Guide d'installation

Connecter Claude Code au Google Drive, Docs, Sheets et Slides partagés de STFU via le serveur [workspace-mcp](https://github.com/taylorwilsdon/google_workspace_mcp).

Tu n'as **pas** besoin de créer un projet Google Cloud. Les identifiants OAuth sont partagés par l'équipe.

## Prérequis

- Claude Code installé
- `uv` installé (`brew install uv`)
- Un compte `@stfu.pro` (Google Workspace)
- Le repo `stfu-os` cloné (`git clone ...` puis `cd stfu-os`)

## 1. Récupérer les identifiants

Les identifiants OAuth (`GOOGLE_OAUTH_CLIENT_ID` et `GOOGLE_OAUTH_CLIENT_SECRET`) sont dans une **note Slite privée** réservée à l'équipe :

> **[Identifiants Google Workspace MCP](https://startthefup.slite.com/app/docs/bCumEg95RnWZrh)**

Ces identifiants sont les memes pour tout le monde. Ils identifient l'app STFU, pas ton compte perso.

## 2. Configurer `.env`

```bash
# Copier le template
cp .env.example .env

# Editer .env avec tes valeurs
# Remplir au minimum :
#   GOOGLE_OAUTH_CLIENT_ID=<copié depuis Slite>
#   GOOGLE_OAUTH_CLIENT_SECRET=<copié depuis Slite>
#   GOOGLE_USER_EMAIL=prenom@stfu.pro
```

Ensuite, ajouter le sourcing automatique dans ton shell :

```bash
# Ajouter cette ligne a ~/.zshrc
echo '[ -f "$HOME/stfu-workspace/.env" ] && { set -a; source "$HOME/stfu-workspace/.env"; set +a; }' >> ~/.zshrc

# Recharger
source ~/.zshrc

# Verifier
echo $GOOGLE_OAUTH_CLIENT_ID   # doit afficher la valeur
echo $GOOGLE_USER_EMAIL         # doit afficher ton email
```

## 3. Premiere authentification

```bash
cd ~/stfu-workspace && claude --plugin-dir ~/stfu-os
```

1. Taper `/mcp` dans Claude Code — verifier que `google-workspace` apparait comme connecte
2. Demander un truc Drive (ex. "liste mes fichiers Drive")
3. Claude va retourner une **URL d'autorisation** — clique dessus
4. Connecte-toi avec ton compte `@stfu.pro` et autorise toutes les permissions
5. C'est bon. Le token est cache pour les sessions futures dans `~/.google_workspace_mcp/credentials/{ton-email}.json`

## Depannage

### Port 8000 occupe (le plus frequent)

Si l'auth OAuth echoue avec "Port 8000 is already in use", c'est parce que le serveur MCP occupe deja le port. Fix :

```bash
# Ouvrir un AUTRE terminal
export GOOGLE_OAUTH_CLIENT_ID="<ta-valeur>"
export GOOGLE_OAUTH_CLIENT_SECRET="<ta-valeur>"
export OAUTHLIB_INSECURE_TRANSPORT=1
export WORKSPACE_MCP_PORT=9000
uvx workspace-mcp --cli list
```

Ca lance l'auth OAuth sur un port different. Une fois authentifie, relance Claude Code et ca marche.

### Token expire / erreur d'auth

```bash
rm ~/.google_workspace_mcp/credentials/{ton-email}.json
```

Puis relance Claude Code — il te redemandera de t'authentifier.

### `uvx` non trouve

```bash
brew install uv
```

### Claude Code ne voit pas les variables

Verifier que le sourcing `.env` est bien dans `~/.zshrc` et que le shell a ete recharge :

```bash
source ~/.zshrc
echo $GOOGLE_OAUTH_CLIENT_ID  # doit afficher la valeur
```

Si vide : verifier que `.env` existe et contient les bonnes valeurs (pas de guillemets autour des valeurs, pas de retours a la ligne Windows).

## Comment ca marche (pour les curieux)

Le setup `.mcp.json` du repo utilise `${GOOGLE_OAUTH_CLIENT_ID}` et `${GOOGLE_OAUTH_CLIENT_SECRET}` comme variables d'environnement. Claude Code les resout depuis ton shell au lancement.

Le CLIENT_ID/SECRET est partage — il identifie l'**app** STFU, pas toi. Ton identite est determinee par le token OAuth que tu obtiens a l'etape 3. Chaque utilisateur a son propre token dans `~/.google_workspace_mcp/credentials/`.

Le package `workspace-mcp` (v1.12.0+) gere le multi-utilisateur nativement. Pas besoin de modifier `.mcp.json` ou `.claude/settings.json`.
