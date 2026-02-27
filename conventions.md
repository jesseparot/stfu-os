# Conventions STFU

Ce document est la **source de verite** pour les conventions de nommage et de structure du workspace STFU. Il est lu par les humains et par Claude.

---

## 1. Structure des dossiers

Le workspace separe le **tool layer** (tracked dans git) du **content layer** (local dans `_workspace/`, gitignored).

### Tracked (git) — tool layer

```
stfu-os/
├── .claude/
│   ├── CLAUDE.md                # Instructions pour Claude
│   └── skills/                  # Un dossier par skill (flat)
│       └── _index.md            # Catalogue des skills
│
├── .mcp.json                    # Config MCP (secrets via ${VAR})
├── .env.example                 # Template des secrets
├── .gitignore                   # Exclut _workspace/, .env, binaires
│
├── tuto/                        # Guides partenaires
│   └── secrets-setup.md
│
├── README.md                    # Vue d'ensemble, onboarding
├── conventions.md               # Ce fichier
├── stfu-context.md              # Contexte entreprise
└── glossary.md                  # Noms propres
```

### `_workspace/` (gitignored) — content layer

**Core (tout coach)** :

```
_workspace/
├── projects/           # Projets actifs
│   └── {client}-{sujet}/
│       ├── README.md   # Manifest (seul fichier requis)
│       └── _scratch/   # Docs ephemeres, reflexion locale (reco)
├── _inbox/             # Zone de depot par defaut
└── _archive/           # Projets et leads termines
```

**Optionnel (selon le coach/workflow)** :

```
├── sales/              # Si suivi local d'AO (sinon tout dans Slite/Salesforce)
│   └── appels-d-offres/
├── internal/           # Docs de reflexion strategie personnels
├── templates/          # En cours de migration vers Slite
├── methodologies/      # En cours de migration vers Slite
└── _pipeline-artefacts/  # Intermediaires de workflows automatises
```

Le contenu dans `_workspace/` migre progressivement vers les outils cloud (Slite, Drive). L'objectif : zero contenu local a terme.

---

## 2. Conventions de nommage

### 2.1 Dossiers

| Type | Convention | Exemple |
|------|------------|---------|
| Projet | `{client}-{sujet}` (recommande, pas impose) | `totalenergies-plug-charge`, `arkea-banque-conversationnelle` |
| Lead | `{entreprise}-{sujet}` ou `{entreprise}-{contact}-{sujet}` | `totalenergies-arena`, `bnp-dupont-innovation-lab` |
| Appel d'offres | `{organisme}-{sujet}-{YY-MM}` | `ademe-produits-num-26-01` |

### 2.2 Fichiers

| Type | Convention | Exemple |
|------|------------|---------|
| Document draft | `{type}-{sujet}_draft.md` | `rapport-explo_draft.md` |
| Document valide | `{type}-{sujet}_final.md` | `rapport-explo_final.md` |
| Document versionne | `{type}-{sujet}-v{X.Y}.md` | `rapport-explo-v1.0.md` |
| Transcript | `{YYYY-MM-DD}-{type}-{sujet}.md` | `2025-01-28-call-kickoff.md` |
| CR reunion | `cr-{YYYY-MM-DD}-{sujet}.md` | `cr-2025-01-28-copil.md` |
| Scratch (ephemere) | `_scratch/` dans un dossier projet | Docs jetables, reflexion locale, jamais pousse vers le cloud |

### 2.3 Statuts (suffixes)

| Suffixe | Signification |
|---------|---------------|
| `_draft` | Travail en cours, non valide |
| `_final` | Valide, livrable |
| `_archive` | Obsolete, garde pour reference |

### 2.4 Fichiers locaux : transit vs ephemere

| Type | Convention | Destination cloud | Nettoyage |
|------|-----------|-------------------|-----------|
| Draft (transit) | `{type}-{sujet}_draft.md` | Sera pousse vers Slite/Drive | Supprimer apres push |
| Final (valide) | `{type}-{sujet}_final.md` | Pousse ou pret | Supprimer apres push |
| Scratch (ephemere) | Fichiers dans `_scratch/` | Jamais pousse | Supprimer librement |
| CR | `cr-YYYY-MM-DD-sujet.md` | Slite via /debrief | Supprimer apres push |

`_scratch/` peut exister dans tout dossier projet. Pas de convention de nommage
a l'interieur -- c'est du brouillon jetable par definition.

---

## 3. Projets et missions

### 3.1 Principe

Chaque projet a un **dossier local** dans `_workspace/projects/` avec un manifest README qui pointe vers les espaces cloud. Le contenu (notes, CRs, livrables) vit dans Slite, Drive, etc. Pas de duplication. Pas de structure tracked dans git pour les projets.

### 3.2 Dossier local (_workspace/projects/)

```
_workspace/projects/{client}-{sujet}/
├── README.md          # Manifest projet — seul fichier requis
└── ...                # Fichiers de travail locaux
```

Le README.md sert de **carte** pour que Claude et les humains sachent ou trouver les choses.

#### Template manifest

```markdown
# {Sujet} -- {Client}

**Coach(s)** : {coach(s)}
**Timeline** : {start} ->

## Contexte

{2-3 lignes}

## Sources

| Quoi | Lien |
|------|------|
| Slite | [note parent]({url}) |
| Drive | [dossier projet]({url}) |
| Outils client | {a completer} |

## Notes

```

**Pourquoi local** : iterer avec Claude Code est plus rapide que modifier Slite ou Drive directement. Le fichier local permet des allers-retours rapides avant un commit cloud.

**Regles** :
- Les fichiers dans `_workspace/` suivent les conventions de nommage standard (section 2)
- Une fois publie dans l'outil cloud, le fichier local peut etre supprime
- `_workspace/` ne doit jamais devenir un stockage permanent — migrer vers Slite/Drive

### 3.3 Structure cloud — Slite

Chaque projet actif a un espace structure dans Slite :

```
[Note parent projet]                    # Contexte, brief, liens
├── Comptes rendus                      # Note parent des CRs
│   ├── cr-YYYY-MM-DD-sujet            # Chaque CR = une note enfant
│   ├── cr-YYYY-MM-DD-sujet
│   └── ...
└── [Notes de travail au cas par cas]   # Analyse, exploration, etc.
```

**Note "Comptes rendus"** : c'est une note parent dont les enfants sont les CRs. Elle peut contenir un bloc `<database>` (format collection Slite) pour afficher les CRs en tableau avec colonnes Date, Sujet, Participants.

**Convention de nommage des CRs dans Slite** : `cr-YYYY-MM-DD-sujet` (meme convention que les fichiers locaux).

Le skill `/debrief` publie directement dans cette structure : il identifie la note parent projet et cree le CR comme note enfant de "Comptes rendus".

### 3.4 Workflow de setup projet

Lancer `/project-init`. Le skill cree automatiquement :
1. Le dossier local + manifest dans `_workspace/projects/`
2. La note parent Slite + sous-note "Comptes rendus"
3. Le dossier Drive (dans le dossier client existant ou nouveau)
4. Les liens dans le manifest

---

## 4. Structure d'un lead

```
_workspace/sales/leads/{entreprise}-{contact}-{sujet}/
│
├── README.md                    # Fiche lead
│   # Contexte, besoin identifie
│   # Contacts, decideurs
│   # Historique des echanges
│   # Prochaines etapes
│   # Statut (qualification, proposition, negociation...)
│
├── conversations/               # Transcripts, notes de calls
└── documents/                   # Docs recus, envoyes
```

---

## 5. Lifecycle lead → client → archive

```
1. RDV de vente organise
   → Creer _workspace/sales/leads/{entreprise}-{contact}-{sujet}/
   → Remplir README.md (fiche lead)

2. Mission signee
   → Lancer /project-init (cree dossier local, Slite, Drive, manifest)
   → Deplacer lead vers _workspace/_archive/ ou supprimer

3. Mission en cours
   → CRs publies dans Slite (via /debrief ou manuellement)
   → Iteration locale dans _workspace/ si besoin, puis commit cloud
   → Livrables dans Drive ou outil client

4. Mission terminee
   → Capitaliser dans Airtable (via /mission-airtable)
   → Deplacer _workspace/projects/{name}/ vers _workspace/_archive/
   → Archiver la note Slite (si fonctionnalite dispo)
```

---

## 6. Inbox et organisation automatique

### 6.1 Principe

Le dossier `_workspace/_inbox/` est la zone de depot par defaut. Les fichiers peuvent etre organises automatiquement via le skill `organize-file`.

### 6.2 Comportement

1. Fichier depose dans `_workspace/_inbox/`
2. Skill `organize-file` analyse :
   - Type de fichier (transcript, note, CR, proposal, etc.)
   - Client/lead associe (si detectable)
   - Projet/mission associe (si detectable)
3. Action :
   - Renommage selon conventions
   - Deplacement vers le bon dossier
   - Creation de dossier si necessaire
   - Demande de confirmation si ambiguite

### 6.3 Cas ambigus

Si le skill ne peut pas determiner la destination :
- Le fichier reste dans `_workspace/_inbox/`
- Un tag `[NEEDS-REVIEW]` est ajoute
- Une entree est ajoutee dans `_workspace/_inbox/_pending.md`

---

## 7. Style d'ecriture

Voir `.claude/skills/stfu-writing/SKILL.md` pour les regles detaillees :
- Pas de title case
- Pas de em-dash
- Mots simples, pas de jargon inutile

---

*Derniere mise a jour : 2026-02-24*
