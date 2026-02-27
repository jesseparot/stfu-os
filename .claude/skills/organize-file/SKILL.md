---
name: organize-file
description: Organise automatiquement les fichiers déposés dans _workspace/_inbox/. Analyse le contenu, identifie le type de document et le projet associé, puis déplace et renomme selon les conventions STFU. Utilisable manuellement ou via hook automatique.
---

# Organize file

Skill pour organiser automatiquement les fichiers déposés dans `_workspace/_inbox/`.

## Workflow

### 1. Analyse du fichier

**Lire le fichier** et identifier :

1. **Type de document** :
   - `transcript` : transcription d'appel/réunion
   - `cr` : compte-rendu de réunion
   - `note` : notes de travail
   - `proposal` : proposition commerciale
   - `rapport` : rapport ou livrable
   - `presentation` : slides, deck
   - `contrat` : document contractuel
   - `facture` : facture ou devis
   - `ao` : appel d'offres / DCE
   - `unknown` : type non identifié

2. **Client/lead associé** (si détectable) :
   - Chercher mentions de noms d'entreprises connues
   - Verifier contre la liste dans `_workspace/projects/` et `_workspace/sales/leads/`

3. **Projet associé** (si détectable) :
   - Chercher des références à des projets existants
   - Identifier des dates ou noms de projet

4. **Date du document** :
   - Extraire la date du contenu si présente
   - Utiliser la date de modification du fichier sinon

### 2. Détermination de la destination

**Règles de routage** :

| Type | Client identifié | Destination |
|------|------------------|-------------|
| transcript, cr, note | Oui, projet actif | `_workspace/projects/{project-name}/` |
| transcript, cr, note | Oui, lead | `_workspace/sales/leads/{lead}/conversations/` |
| transcript, cr, note | Non | `_workspace/_inbox/` (demander confirmation) |
| proposal | Oui, lead | `_workspace/sales/leads/{lead}/documents/` |
| proposal | Non | `_workspace/sales/` |
| rapport, presentation | Oui, projet actif | `_workspace/projects/{project-name}/` |
| ao | Identifiable | `_workspace/sales/appels-d-offres/{organisme}-{sujet}-{YY-MM}/` |
| contrat, facture | Oui | `_workspace/projects/{project-name}/` |
| unknown | - | `_workspace/_inbox/` (demander confirmation) |

**Note** : verifier aussi `_workspace/clients/` (legacy) si le projet n'est pas trouve dans `_workspace/projects/`.

### 3. Renommage selon conventions

**Appliquer les conventions de `conventions.md`** :

| Type | Format cible |
|------|--------------|
| transcript | `{YYYY-MM-DD}-transcript-{sujet}.md` |
| cr | `cr-{YYYY-MM-DD}-{sujet}.md` |
| note | `notes-{sujet}.md` |
| proposal | `proposition-{client}-{sujet}_draft.md` |
| rapport | `rapport-{sujet}_draft.md` |

### 4. Exécution

**Mode prompt (par défaut)** :

Avant de déplacer, afficher :
```
📁 Fichier : {nom_original}
📄 Type détecté : {type}
🏢 Client/Lead : {client ou "Non identifié"}
📂 Destination : {chemin_destination}
📝 Nouveau nom : {nouveau_nom}

Confirmer ? [O/n]
```

**Mode auto** (si confiance élevée) :

Déplacer directement si :
- Type clairement identifié
- Client/projet trouvé avec certitude
- Pas d'ambiguïté sur la destination

### 5. Gestion des cas ambigus

Si impossible de déterminer la destination :

1. **Laisser dans `_workspace/_inbox/`**
2. **Ajouter `[NEEDS-REVIEW]`** au début du nom de fichier
3. **Créer/mettre à jour `_workspace/_inbox/_pending.md`** :

```markdown
# Fichiers en attente de classification

## {date}

### {nom_fichier}
- **Type possible** : {type ou "inconnu"}
- **Client possible** : {suggestions}
- **Action suggérée** : {suggestion}
```

---

## Utilisation

### Invocation manuelle

```
/organize-file /chemin/vers/_workspace/_inbox/fichier.md
```

ou

```
/organize-file _workspace/_inbox/
```
(pour traiter tous les fichiers de l'inbox)

### Invocation automatique (hook)

Le hook peut être configuré pour déclencher ce skill automatiquement quand un fichier est déposé dans `_workspace/_inbox/`.

---

## Exemples

### Exemple 1 : Transcript client connu

**Fichier** : `_workspace/_inbox/transcript-call-28-01.txt`
**Contenu** : Mentionne "TotalEnergies" et "programme innovation"

**Résultat** :
```
📁 Fichier : transcript-call-28-01.txt
📄 Type détecté : transcript
🏢 Client : totalenergies
📂 Destination : _workspace/projects/totalenergies-programme-innovation/
📝 Nouveau nom : 2025-01-28-transcript-call-innovation.md
```

### Exemple 2 : Document ambigu

**Fichier** : `_workspace/_inbox/notes-reunion.md`
**Contenu** : Pas de mention de client spécifique

**Résultat** :
```
📁 Fichier : notes-reunion.md
📄 Type détecté : note
🏢 Client : Non identifié

❓ Je n'ai pas pu identifier le client associé.
   Quel est le contexte de ce document ?

   1. Client existant (préciser)
   2. Nouveau lead
   3. Interne STFU
   4. Autre
```

### Exemple 3 : Appel d'offres

**Fichier** : `_workspace/_inbox/DCE-ADEME-innovation-2026.pdf`
**Contenu** : Dossier de consultation ADEME

**Résultat** :
```
📁 Fichier : DCE-ADEME-innovation-2026.pdf
📄 Type détecté : ao (appel d'offres)
📂 Destination : _workspace/sales/appels-d-offres/ademe-innovation-26-01/
📝 Actions :
   - Créer le dossier ademe-innovation-26-01/
   - Déplacer le DCE
   - Proposer de lancer /appel-d-offres pour créer le brief
```

---

## Ressources

- Conventions de nommage : `../../conventions.md`
- Projets actifs : `../../_workspace/projects/`
- Liste des leads : `../../_workspace/sales/leads/`

---

*Dernière mise à jour : 2025-01-28*
