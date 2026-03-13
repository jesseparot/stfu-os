---
name: cv-propale
description: >
  Orchestre la production de CVs pour un AO ou une propale. Qualifie le besoin,
  extrait les critères du document de référence, lance la recherche de missions
  par coach, consolide pour validation, puis génère les CVs. Utiliser quand on
  demande de produire des CVs pour un appel d'offres ou une proposition commerciale.
user_invocable: true
---

# CV / Propale — Orchestrateur

Orchestre le pipeline complet : qualification → recherche missions → validation → génération CVs.

## Étape 1 : Qualification

Collecter les informations manquantes via le **tool** `AskUserQuestion`. NE PAS poser les questions en texte libre.

**Skip intelligent** : si le contexte est déjà fourni (plan, message utilisateur, skill amont), ne pas redemander ce qui est connu.

Informations à collecter :
1. **Coach(s)** : quel(s) coach(s) ?
2. **Contexte** : AO / propale / pitch
3. **Document de référence** : CCTP, brief, note Slite
4. **Nombre de refs par coach** : défaut 10-15

Exemple de call pattern :

```
AskUserQuestion({
  questions: [{
    question: "C'est pour quel contexte ?",
    header: "Contexte",
    options: [
      {label: "AO", description: "Appel d'offres — besoin des profils CCTP, niveaux, XP"},
      {label: "Propale", description: "Proposition commerciale"},
      {label: "Pitch", description: "Présentation courte"}
    ],
    multiSelect: false
  }]
})
```

## Étape 1b : Lecture du document de référence

Selon le contexte, aller lire le document source pour en extraire les critères de scoring :

- **AO** : lire le DCE (CCTP, RC, BPU) — y chercher les profils requis, les niveaux de formation exigés, les années d'XP, les compétences clés, les secteurs prioritaires, les types de missions attendues
- **Propale** : lire la note Slite, le brief, ou le mail du client — y chercher le besoin, le secteur, le format attendu
- **Pitch** : lire le brief ou la description de l'événement

Si l'utilisateur n'a pas fourni de document, lui demander via `AskUserQuestion` :
- "Tu as un lien vers le DCE / la note Slite / le brief ? Ca me permettra de scorer les missions sur les vrais critères."

Les critères extraits du document alimentent directement le scoring tri-critère et sont passés tels quels au cv-builder en aval (profils CCTP, niveaux, exigences).

## Étape 2 : Recherche de missions (parallélisée)

Invoquer le skill `/missions-par-coach` pour **chaque coach** via le tool `Skill`, en passant les critères dans les arguments. Lancer tous les appels en parallèle (un par coach) dans un seul message avec plusieurs tool calls.

Prompt de délégation par coach :
```
<coach> --secteur "<secteurs>" --expertise "<expertises>" --format "<formats>" --refs <N> --profils-cctp "<profils si AO>"
```

Exemple pour 3 coachs — envoyer les 3 appels `Skill` dans un seul message :
```
Skill({ skill: "missions-par-coach", args: "Mickaël --secteur \"public, innovation\" --expertise \"design thinking, coaching\" --format \"programme, formation\" --refs 12 --profils-cctp \"Chef de projet, Coach agile\"" })
Skill({ skill: "missions-par-coach", args: "Nina --secteur \"public, innovation\" --expertise \"design, UX\" --format \"projet, workshop\" --refs 12 --profils-cctp \"UX Designer\"" })
Skill({ skill: "missions-par-coach", args: "Jesse --secteur \"public\" --expertise \"stratégie, innovation\" --format \"programme\" --refs 10" })
```

## Étape 3 : Consolidation + validation

1. Récupérer les tableaux de chaque fork
2. Consolider dans un fichier `.md` unique :
   - Un tableau par coach
   - Résumé global (nombre de missions par score)
3. Écrire le fichier dans le dossier du projet ou demander le chemin via `AskUserQuestion`
4. Demander validation à l'utilisateur — l'utilisateur coche les missions retenues (colonne V)

## Étape 4 : Génération des CVs (parallélisée)

Pour chaque coach + missions validées, invoquer `/cv-builder` via le tool `Skill` en parallèle. Passer :

```
Skill({ skill: "cv-builder", args: "<coach> --objectif <AO|propale|pitch> --missions \"<record IDs>\" --profils-cctp \"<profils>\" --output <chemin>" })
```

Lancer tous les appels dans un seul message.

## Notes

- Ce skill est interactif : qualification → validation → génération
- Les critères extraits du document de référence (profils CCTP, niveaux, exigences) sont passés tels quels aux skills en aval
- Le chemin de sortie des fichiers est demandé à l'utilisateur si pas évident du contexte
