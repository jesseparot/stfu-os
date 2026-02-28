# Guide de configuration des secrets

Comment configurer les clés API et identifiants MCP pour stfu-os.

## Principe

`.mcp.json` référence des variables d'environnement via la syntaxe `${VAR}`. Claude Code résout ces variables depuis l'**environnement shell du processus** au lancement — pas depuis un fichier, un keychain ou un settings interne.

C'est une limitation connue de Claude Code : la section `env` de `settings.json` ne nourrit **pas** la résolution `${VAR}` dans `.mcp.json` ([issue #4276](https://github.com/anthropics/claude-code/issues/4276), [issue #11927](https://github.com/anthropics/claude-code/issues/11927)). L'approche `.env` + sourcing shell est donc la méthode recommandée.

## Démarrage rapide

```bash
# 1. Créer le fichier .env à partir du template
cp .env.example .env
# Éditer .env avec vos vraies valeurs

# 2. Exporter les variables dans votre shell
# Ajouter cette ligne à votre ~/.zshrc (ou ~/.bashrc) :
[ -f "$HOME/stfu-workspace/.env" ] && { set -a; source "$HOME/stfu-workspace/.env"; set +a; }

# 3. Recharger le shell et lancer Claude Code
source ~/.zshrc
cd ~/stfu-workspace && claude --plugin-dir ~/stfu-os
```

## Sécurité

### Protection contre la lecture par Claude

`.claudeignore` ne bloque pas fiablement l'accès aux fichiers secrets. On utilise `permissions.deny` dans `settings.json` (at repo root) (commité dans le repo) :

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

Cela empêche Claude Code de lire le contenu de `.env`, même s'il est présent sur le disque. Les variables restent accessibles via l'environnement shell (c'est le comportement voulu).

### `.env` est gitignored

Le fichier `.env` ne quitte jamais votre machine. Seul `.env.example` (sans valeurs) est commité.

### Alternative plus sécurisée : 1Password

Pour éviter les secrets en clair sur le disque, vous pouvez utiliser 1Password CLI :

```bash
# Lancer Claude Code avec injection des secrets depuis 1Password
op run --env-file=.env.op -- claude
```

Où `.env.op` contient des références 1Password :
```
AIRTABLE_API_KEY=op://Vault/Airtable/token
LINKUP_API_KEY=op://Vault/Linkup/api-key
```

Les secrets sont résolus à la volée, jamais écrits sur le disque.

## Secrets requis

| Variable | Serveur MCP | Où l'obtenir |
|----------|-------------|--------------|
| `AIRTABLE_API_KEY` | airtable | [airtable.com/create/tokens](https://airtable.com/create/tokens) — créer un personal access token avec les scopes lecture/écriture sur la Base Missions |
| `GOOGLE_OAUTH_CLIENT_ID` | google-workspace | Identifiants partagés par l'équipe — voir [note Slite privée](https://startthefup.slite.com/app/docs/bCumEg95RnWZrh). Guide complet : [tuto/google-workspace-mcp-setup.md](google-workspace-mcp-setup.md) |
| `GOOGLE_OAUTH_CLIENT_SECRET` | google-workspace | Même note Slite que ci-dessus |
| `GOOGLE_USER_EMAIL` | google-workspace (skills) | Votre email `@stfu.pro` — utilisé par les skills pour les appels Drive/Docs/Sheets/Slides |
| `LEMLIST_API_KEY` | lemlist | Lemlist > Settings > Integrations > API |
| `DROPCONTACT_ACCESS_TOKEN` | dropcontact | Dashboard Dropcontact > section API |
| `LINKUP_API_KEY` | linkup | [app.linkup.so/account](https://app.linkup.so/account) |

## Services sans clé nécessaire

Ces services s'authentifient via login navigateur (HTTP MCP) — pas de variable d'environnement :

- **Slite** — `api.slite.com/mcp`
- **beta.gouv** — public, aucune authentification

## Notes de configuration par service

### Airtable

1. Aller sur [airtable.com/create/tokens](https://airtable.com/create/tokens)
2. Créer un nouveau personal access token
3. Scopes nécessaires : `data.records:read`, `data.records:write`, `schema.bases:read`
4. Accorder l'accès à la base "Marketing: Base Missions"
5. Copier le token (commence par `pat...`)

### Google Workspace

Les identifiants OAuth (`CLIENT_ID` et `CLIENT_SECRET`) sont **partagés par l'équipe** — pas besoin de créer un projet Google Cloud. Recuperer les valeurs depuis la note Slite privée.

Pour le guide complet d'installation et de dépannage, voir **[tuto/google-workspace-mcp-setup.md](google-workspace-mcp-setup.md)**.

1. Copier `GOOGLE_OAUTH_CLIENT_ID` et `GOOGLE_OAUTH_CLIENT_SECRET` depuis la note Slite
2. Ajouter `GOOGLE_USER_EMAIL=prenom@stfu.pro` dans `.env`
3. À la première utilisation, Claude Code ouvrira un navigateur pour le consentement OAuth
4. Token sauvegardé dans `~/.google_workspace_mcp/credentials/{votre-email}.json`

### Lemlist

1. Ouvrir l'app Lemlist
2. Aller dans Settings > Integrations > API
3. Copier la clé API

### Dropcontact

1. Se connecter à Dropcontact
2. Aller dans la section API du dashboard
3. Copier le access token

### Linkup

1. Se connecter sur [app.linkup.so](https://app.linkup.so)
2. Aller dans les paramètres du compte
3. Copier la clé API

## Rotation des secrets

1. Générer une nouvelle clé/token dans le dashboard du service
2. Mettre à jour la valeur dans `.env`
3. Recharger le shell (`source ~/.zshrc`) puis relancer Claude Code

## Dépannage

**Les variables ne sont pas reconnues par Claude Code** : Claude Code résout `${VAR}` depuis l'environnement shell, pas depuis `.env` directement. Vérifier que la ligne `source .env` est bien dans `~/.zshrc` et que le shell a été rechargé. Tester avec `echo $AIRTABLE_API_KEY` dans le terminal.

**Le fichier `.env` a des retours à la ligne Windows** : Si le fichier a été édité sous Windows ou copié depuis un outil web, les `\r\n` peuvent corrompre les valeurs. Corriger avec `sed -i '' 's/\r$//' .env` (macOS) ou `sed -i 's/\r$//' .env` (Linux).

**Le serveur MCP ne démarre pas** : Vérifier que le nom de variable dans `.env` correspond exactement à ce qui est dans `.env.example`. Pas de guillemets autour des valeurs.

**Erreurs "unauthorized" ou "403"** : La clé a peut-être expiré ou été révoquée. Regénérer et mettre à jour `.env`, puis recharger le shell.

**Le prompt OAuth Google réapparaît** : Le refresh token OAuth a peut-être expiré. Supprimer `~/.google_workspace_mcp/credentials/{votre-email}.json` et se ré-authentifier.
