# Claude Code — Guide d'installation

Installer Claude Code sur macOS et configurer l'environnement pour `stfu-os`.

## Prerequis

- macOS (Catalina ou plus recent)
- Node.js 18+ (`brew install node`)
- Le repo `stfu-os` clone

## 1. Verifier ton shell

macOS utilise **zsh** par defaut depuis Catalina (2019). Verifie que c'est bien le cas :

```bash
echo $SHELL
```

- Si ca affiche `/bin/zsh` — tout est bon, passe a l'etape 2.
- Si ca affiche `/bin/bash` — il faut changer (voir section ci-dessous).

### Passer de bash a zsh

Le shell bash sur macOS cause des problemes :
- Les outils modernes (Claude Code, Cursor, etc.) configurent le PATH dans `~/.zshrc` — bash ne lit pas ce fichier
- La version de bash livree avec macOS est ancienne (3.2, de 2007) pour des raisons de licence
- Les tutos de ce repo supposent zsh

Pour changer :

```bash
# Changer le shell par defaut
chsh -s /bin/zsh

# Fermer et rouvrir le terminal
```

Si tu avais des customisations dans `~/.bash_profile` ou `~/.bashrc`, migre-les dans `~/.zshrc`.

## 2. Installer Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Verifier l'installation :

```bash
claude --version
```

Si `claude: command not found` apres l'installation, le PATH npm n'est probablement pas configure. Ajouter dans `~/.zshrc` :

```bash
export PATH="$(npm config get prefix)/bin:$PATH"
```

Puis `source ~/.zshrc`.

## 3. Installer Playwright

Playwright permet a Claude Code de prendre des screenshots, tester des pages web et interagir avec des sites.

```bash
npm install -g playwright
playwright install chromium
```

Verifier :

```bash
playwright --version
```

## 4. Configurer stfu-os

```bash
# Copier le template de secrets dans le workspace
cp ~/stfu-os/.env.example ~/stfu-workspace/.env
# Editer ~/stfu-workspace/.env avec tes valeurs
# Voir tuto/secrets-setup.md pour le guide complet

# Ajouter le sourcing auto dans ton shell
echo '[ -f "$HOME/stfu-workspace/.env" ] && { set -a; source "$HOME/stfu-workspace/.env"; set +a; }' >> ~/.zshrc
source ~/.zshrc

# Lancer Claude Code (marketplace)
cd ~/stfu-workspace
claude
```

## 5. Utilisation dans Cursor

Claude Code s'integre dans le terminal de Cursor. Si le terminal Cursor n'est pas en zsh :

1. Ouvrir Cursor > Settings > Terminal
2. Verifier que le shell par defaut est `/bin/zsh`
3. Ou ajouter dans `settings.json` de Cursor :

```json
{
  "terminal.integrated.defaultProfile.osx": "zsh"
}
```

Si `claude` n'est pas reconnu dans le terminal Cursor mais fonctionne dans le terminal systeme, redemarrer Cursor pour qu'il recharge le PATH.

## Depannage

### `claude: command not found`

**Cause probable** : le shell est en bash au lieu de zsh, ou le PATH n'inclut pas le dossier npm global.

```bash
# Verifier le shell
echo $SHELL

# Si bash, changer vers zsh (voir etape 1)
chsh -s /bin/zsh

# Si deja zsh, verifier le PATH
which claude
npm config get prefix
# Ajouter le prefix npm au PATH dans ~/.zshrc si absent
```

### Claude Code fonctionne dans le terminal mais pas dans Cursor

Le terminal integre de Cursor peut utiliser un shell different du terminal systeme.

1. Verifier le shell dans le terminal Cursor : `echo $SHELL`
2. Si c'est bash, configurer Cursor pour utiliser zsh (voir etape 4)
3. Redemarrer Cursor completement (pas juste le terminal)

### Les serveurs MCP ne demarrent pas

Voir [secrets-setup.md](secrets-setup.md) pour la configuration des cles API et le depannage MCP.

### Erreur de permissions npm

Si `npm install -g` echoue avec `EACCES` :

```bash
# Fix propre — changer le dossier global npm
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Puis reinstaller
npm install -g @anthropic-ai/claude-code
```
