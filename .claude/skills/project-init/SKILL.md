---
name: project-init
description: Initialise un projet STFU — dossier local, manifest, note Slite, dossier Drive. Utiliser pour creer, initialiser, demarrer ou setup un nouveau projet client. Aussi utilisable quand un lead est converti en mission.
---

# Project init

Initialise un nouveau projet STFU avec un dossier local, un manifest, une note Slite et un dossier Drive.

## Configuration

- **Email Drive** : Lire `$GOOGLE_USER_EMAIL` depuis l'environnement (`echo $GOOGLE_USER_EMAIL` via Bash). Si non défini, demander à l'utilisateur son email Google `@stfu.pro`.
- **Drive racine STFU** : `1MG7LnZzAJPg7EEzbWjX4OfSMH4WL5m-L`
- **Dossier local** : `_workspace/projects/`

## Workflow

### 1. Collecter les infos

Utiliser `AskUserQuestion` pour collecter :

**Requis :**
- Client (nom de l'entreprise)
- Sujet du projet (en quelques mots)

**Optionnels :**
- Contexte bref (2-3 lignes)
- Timeline (date de debut, duree estimee)
- Coach(s) (defaut : Jesse Parot)

### 2. Identifier l'equipe projet client

Reconstituer automatiquement la liste des interlocuteurs cote client (noms + emails) en croisant plusieurs sources, puis faire valider par le coach.

#### Sources (interroger en parallele)

1. **Google Calendar** — Chercher les evenements recents et a venir avec le client :
   - `mcp__claude_ai_Google_Calendar__gcal_list_events` avec `q: "{ClientName}"` et `condenseEventDetails: false` (pour avoir les attendees)
   - Fenetre : 3 mois avant -> 1 mois apres la date du jour
   - Extraire les attendees (email + displayName) de chaque evenement
   - Filtrer : exclure les emails `@stfu.pro` (equipe interne)

2. **Gmail** — Chercher les echanges recents avec le client :
   - `mcp__claude_ai_Gmail__gmail_search_messages` avec `q: "from:*@{domaine-client} OR to:*@{domaine-client}"` (deduire le domaine du nom client, ou utiliser le nom directement)
   - Variante : `q: "{ClientName}"` si le domaine n'est pas evident
   - Lire les 5-10 premiers messages via `mcp__claude_ai_Gmail__gmail_read_message` pour extraire les headers From/To/Cc
   - Filtrer : exclure les emails `@stfu.pro`

3. **Granola** (bonus) — Chercher les reunions mentionnant le client :
   - `mcp__granola__query_granola_meetings` avec query : `"{ClientName}"`
   - Si des reunions sont trouvees, recuperer les details pour extraire les attendees
   - Utile pour completer avec des noms qui n'apparaissent pas dans Calendar/Gmail

#### Deduplication et presentation

- Fusionner les resultats des sources (dedup par email)
- Presenter la liste au coach via `AskUserQuestion` :

```
Equipe projet {Client} identifiee :

- Marie Dupont <marie.dupont@client.com> (source: Calendar — 3 reunions, Gmail — 8 emails)
- Jean Martin <jean.martin@client.com> (source: Gmail — en CC sur 2 threads)
- Sophie Leroy <sophie.leroy@client.com> (source: Drive — partage dossier)

Contacts a ajouter, corriger ou supprimer ? (Entree pour valider)
```

- Le coach peut ajouter des contacts manuellement, corriger des noms, ou supprimer des faux positifs
- Si aucune source ne renvoie de resultat : demander directement au coach de lister l'equipe

### 3. Generer le nom de dossier

Proposer `{client}-{sujet}` (lowercase, tirets, pas d'espaces).

Regles :
- Le client en premier, le sujet ensuite
- Pas de dates dans le nom
- Exemples : `totalenergies-plug-charge`, `arkea-banque-conversationnelle`, `bpi-i-phd`

Le coach peut override le nom propose. Si le dossier existe deja dans `_workspace/projects/`, prevenir et proposer de mettre a jour le manifest existant.

### 4. Creer le dossier local et le manifest

Creer `_workspace/projects/{name}/README.md` avec le template ci-dessous.

#### Template manifest

```markdown
# {Sujet} -- {Client}

**Coach(s)** : {coach(s)}
**Timeline** : {start} ->

## Contexte

{2-3 lignes de contexte, ou "A completer" si non fourni}

## Equipe client

| Nom | Email | Role/notes |
|-----|-------|------------|
| {Prenom Nom} | {email} | {role si connu, sinon vide} |

## Sources

| Quoi | Lien |
|------|------|
| Slite | [note parent]({url}) |
| Drive | [dossier projet]({url}) |
| Outils client | {a completer} |

## Notes

```

Design : ~15 lignes remplies. Flat, scannable, pas de structure imposee au-dela.

### 5. Creer/trouver la note Slite

1. Chercher une note existante via `mcp__slite__search-notes` avec le nom du client + sujet
2. Si une note pertinente existe : utiliser son URL dans le manifest
3. Si rien : creer la note parent projet via `mcp__slite__create-note`
   - Titre : `{Sujet} -- {Client}`
   - Contenu : le contexte du projet
4. Creer une note enfant "Comptes rendus" sous la note parent
5. Stocker les URLs dans le manifest

### 6. Creer/trouver le dossier Drive

1. Chercher le dossier client dans le Drive STFU :
   - Utiliser `mcp__google-workspace__search_drive_files` pour chercher `Pro - {ClientName}` dans la racine `1MG7LnZzAJPg7EEzbWjX4OfSMH4WL5m-L`

2. Si pas de dossier client :
   - Creer `Pro - {ClientName}` via `mcp__google-workspace__create_drive_folder` dans la racine STFU

3. Creer le sous-dossier projet :
   - Nom : `{Sujet}` dans le dossier client
   - Creer un sous-dossier `STFU <> {ClientName}` (destine au partage client)

4. Stocker l'URL du dossier projet dans le manifest

### 7. Recap

Afficher un resume des ressources creees :

```
Projet initialise : {name}

- Dossier local : _workspace/projects/{name}/
- Slite : {url note parent}
- Drive : {url dossier projet}
- Equipe client : {N} contacts identifies

Prochaines etapes :
- Completer le manifest si besoin
- Lancer /debrief apres le premier call
```

## Idempotence

- Si `_workspace/projects/{name}/` existe deja, ne pas ecraser. Prevenir et proposer de mettre a jour le manifest.
- Si la note Slite existe deja, la lier sans creer de doublon.
- Si le dossier Drive existe deja, le lier sans creer de doublon.

## Exemples

### Exemple 1 : nouveau projet

```
User: /project-init
→ Qui est le client ? "TotalEnergies"
→ Sujet ? "Arena Sismage"
→ Contexte ? "Exploration IA generative pour la plateforme Sismage de simulation geosciences"
→ Timeline ? "Fevrier 2026"
→ Coach(s) ? "Jesse Parot"

Resultat :
- _workspace/projects/totalenergies-arena-sismage/README.md cree
- Note Slite "Arena Sismage -- TotalEnergies" creee
- Dossier Drive "Arena Sismage" cree dans "Pro - TotalEnergies"
```

### Exemple 2 : lead converti

```
User: Le lead Engie est signe, lance /project-init
→ Infos pre-remplies depuis le lead si disponible
→ Meme workflow
→ Proposer de deplacer le lead vers _workspace/_archive/
```
