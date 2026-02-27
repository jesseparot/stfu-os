---
name: clean-workspace
description: >
  Scan et nettoyage du workspace _workspace/. Detecte brouillons anciens,
  dossiers scratch, artefacts orphelins, backlog inbox, projets archivables,
  fichiers orphelins, DCE d'AO expires. Cross-check Slite pour identifier
  les drafts locaux deja pousses. Detection par pattern et contexte
  (age, contenu, conventions). Non-destructif par defaut.
  Utiliser pour nettoyer, ranger, auditer le workspace.
user_invocable: true
---

# clean-workspace

Scan, categorise et propose des actions de nettoyage pour `_workspace/`. Non-destructif par defaut.

## Principes

- **Pattern-based** : detection par suffixes (`_draft`, `_final`), dossiers (`_scratch/`), conventions de nommage -- pas par structure hardcodee
- **Context-aware** : age du fichier, contenu (mentions client, type de doc), taille
- **Non-destructif** : scan et rapport d'abord, actions sur confirmation uniquement
- **Universel** : fonctionne quel que soit le workspace du coach

## Workflow

### 1. Scan du workspace

Verifier la date courante (`date +%Y-%m-%d`). Scanner `_workspace/` recursivement pour collecter chemin, date de derniere modification, taille.

### 2. Classifier chaque element

| Categorie | Detection | Seuil |
|-----------|-----------|-------|
| `[scratch]` | Dossier `_scratch/` ou fichiers dedans | > 14 jours |
| `[artefact]` | Fichier JSON/CSV dans `_pipeline-artefacts/` | > 7 jours |
| `[inbox]` | Fichier dans `_inbox/` (sauf `_pending.md`) | Immediat |
| `[brouillon]` | Fichier `*_draft.*` hors `_scratch/` | > 30 jours (45j si projet actif*) |
| `[dce-expire]` | PDF/docs dans dossier AO `{org}-{sujet}-{YY-MM}` | YY-MM + 1 mois depasse |
| `[archivable]` | Dossier projet dont TOUS les fichiers sont anciens | > 30 jours sur tous fichiers |
| `[orphelin]` | Fichier a la racine de `_workspace/` (hors dossiers standard) | Immediat |
| `[doublon]` | `_draft` avec `_final` existant a cote | Immediat |
| `[convention]` | Nom avec espaces, majuscules, type manquant, suffixe manquant | Immediat |

*Projet actif = au moins un fichier modifie < 14 jours dans le dossier projet.

Regles complementaires :
- **AO** : parser `YY-MM` du nom de dossier. Si mois courant > YY-MM + 1, DCE expire (le brief vit dans Slite/Airtable)
- **Fichiers > 10 Mo** : mention explicite de la taille
- **Orphelins** : lire le contenu des fichiers orphelins pour tenter d'identifier leur type/client

### 3. Cross-check Slite et Drive

Pour chaque fichier `_draft` et chaque CR local :
- Chercher dans **Slite** via `search-notes` (par titre sans le suffixe `_draft`)
- Chercher dans **Google Drive** via `search_drive_files` (par nom de fichier)

Si un equivalent cloud existe, marquer `[deja cloud]` avec lien vers la note Slite ou le fichier Drive. Action recommandee : supprimer le local.

Note : le check Drive n'est pertinent que si le projet utilise Drive (verifier dans le manifest README.md du projet si un lien Drive est renseigne).

### 4. Generer le rapport

Presenter un tableau par categorie. Chaque ligne : chemin relatif, age, taille (si > 1 Mo), action recommandee.

Resume en fin avec :
- Compteurs par categorie
- Espace total recuperable
- Nombre de fichiers proteges (non flagges)

### 5. Demander quoi faire

Options a proposer :
1. Tout appliquer (avec confirmation globale)
2. Choisir par categorie
3. Fichier par fichier
4. Juste noter (aucune action)

### 6. Executer les actions approuvees

| Action | Cible | Comportement |
|--------|-------|-------------|
| Supprimer | Scratch anciens, artefacts, DCE expires, doublons | Double confirmation |
| Archiver local | Projets inactifs | Deplacer vers `_archive/` |
| Organiser | Items inbox | Deleguer a `/organize-file` |
| Deplacer | Orphelins identifies | Vers le bon dossier projet |
| Renommer | Violations de convention | Proposer le nom correct |
| Finaliser | Draft pousse au cloud | Renommer `_draft` vers `_final` ou supprimer |

## Chemins proteges (jamais flagges)

- `README.md` dans tout dossier projet
- `_pending.md` dans inbox

## Interactions avec les skills existants

- `/organize-file` : clean-workspace delegue l'inbox a ce skill
- `/mission-airtable` : avant archivage projet, suggerer la capitalisation Airtable
