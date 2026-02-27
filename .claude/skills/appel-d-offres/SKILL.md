---
name: appel-d-offres
description: Analyse les appels d'offres pour Start The F*** Up. Extrait les informations clés, vérifie la pertinence par rapport au profil STFU, recherche les missions passées dans Airtable, et crée un brief structuré comme note Slite dans la BDD Appels d'offres. Utiliser pour briefer, résumer, analyser ou examiner un appel d'offres, un marché public ou privé.
---

# Brief d'Appels d'Offres

## Vue d'ensemble

Analyse les appels d'offres et crée des briefs structurés sous forme de notes Slite dans la BDD Appels d'offres. Le workflow extrait les informations clés, filtre sur la pertinence, enrichit avec des références de missions passées depuis Airtable, et publie directement dans Slite.

## Workflow

### 1. Extraction du document

**Pour les fichiers PDF :**
- Utiliser l'outil Read pour extraire le texte du PDF
- Si le PDF est basé sur des images ou mal formaté, noter les problèmes d'extraction

**Pour les fichiers DOCX :**
- Utiliser le skill `/docx` pour extraire le contenu des documents Word
- Préserver la structure du document et les marqueurs de formatage

**Pour les formats mixtes :**
- Traiter chaque document séparément
- Consolider les informations issues de plusieurs fichiers

### 2. Extraction des informations

Extraire et organiser les informations suivantes du document de l'appel d'offres :

#### A. Contexte du projet
- Organisme émetteur
- Contexte et enjeux
- Objectifs du projet
- Périmètre

#### B. Contenu attendu de l'offre
**Critique — ce qui doit figurer dans la réponse :**
- Structure de la réponse attendue
- Documents à fournir
- Format et présentation
- Nombre de pages / limites de volume
- Langue(s) requise(s)

#### C. Livrables attendus
**Ce qui sera livré si le marché est attribué :**
- Liste des livrables
- Format des livrables
- Échéances de livraison
- Critères de validation

#### D. Attentes spécifiques
**Ce que l'acheteur recherche dans l'offre :**
- Méthodologie attendue
- Compétences clés recherchées
- Expérience/références requises
- Composition de l'équipe
- Modalités de travail (remote, présentiel, fréquence)

#### E. Éléments financiers
- Budget estimé ou plafond
- Type de marché (forfait, régie, etc.)
- Modalités de paiement
- Durée du contrat

#### F. Critères d'évaluation
**Comment l'offre sera jugée :**
- Critères techniques et pondération
- Critère prix et pondération
- Critères éliminatoires
- Grille de notation si disponible

#### G. Informations pratiques
- Date limite de candidature
- Date de notification
- Date de démarrage prévue
- Localisation et contraintes de présence
- Contacts et modalités de questions

### 3. Filtre de pertinence

**Charger le profil de l'entreprise :**
Lire le profil depuis `../../stfu-context.md` (relatif au répertoire du skill) pour comprendre les services, expertises et positionnement de STFU.

**Évaluer l'alignement avec STFU :**
- Vérifier si l'AO entre dans les domaines d'expertise de STFU (innovation, design thinking, intrapreneuriat, développement produit, go-to-market, etc.)
- Identifier les signaux d'alerte (voir section Signaux d'alerte ci-dessous)

**Logique de décision :**
- **Si clairement hors sujet** (infrastructure IT pure, body shopping, domaines entièrement hors du périmètre STFU) : utiliser `AskUserQuestion` pour signaler le désalignement et demander à l'utilisateur s'il souhaite continuer ou s'arrêter. Exemple : "Cet AO porte sur [sujet] qui semble hors du positionnement STFU. Souhaites-tu quand même que je crée le brief ?"
- **Si au moins partiellement pertinent** (un certain chevauchement avec les services STFU, même partiel) : continuer sans demander.

### 4. Recherche de références Airtable

Rechercher les missions passées STFU pertinentes dans la table Airtable MISSIONS pour les inclure comme références dans le brief.

**Coordonnées Airtable :**
- Base ID : `appyJq6jZuil2VMgC`
- Table ID : `tbl5qzd6zlaWBKpqs`
- La recherche se fait via `mcp__airtable__search_records` qui cherche dans le Search Field (concatène client, description, tags, expertises, mots-clés)

**Processus :**
1. Extraire 3-5 mots-clés pertinents de l'AO (secteur, type de mission, méthodologie, compétences clés, industrie)
2. Lancer plusieurs recherches avec des mots-clés différents pour maximiser la couverture (ex. une recherche par secteur, une par méthodologie, une par type de mission)
3. Dédupliquer les résultats entre les recherches
4. Pour chaque mission pertinente, extraire : ID Mission, Nom Client, Description (Brief ou Description du projet), Type de référence
5. Inclure toutes les références pertinentes — pas de limite artificielle
6. Si plus de 10 références trouvées, sélectionner les plus pertinentes et ajouter une note dans le brief indiquant qu'il en existe davantage

### 5. Upload Google Drive

Uploader les fichiers DCE sur le Google Drive STFU Team dans le dossier "Pro - Appels d'Offres".

**Coordonnées Drive :**
- Dossier parent : `Pro - Appels d'Offres` — ID : `10op7qXqihbb0-gxc51ACiF02OExPEuZz`
- Email utilisateur : Lire `$GOOGLE_USER_EMAIL` depuis l'environnement (`echo $GOOGLE_USER_EMAIL` via Bash). Si non défini, demander à l'utilisateur son email Google `@stfu.pro`.

**Processus :**
1. Dériver le nom du dossier à partir des informations extraites en utilisant la convention de nommage AO : `{organisme}-{sujet}-{YY-MM}` (minuscules, tirets, année et mois à 2 chiffres)
2. Créer le dossier parent de l'AO dans "Pro - Appels d'Offres" via `mcp__google-workspace__create_drive_file` avec `mimeType: application/vnd.google-apps.folder`
3. Créer un sous-dossier `DCE` dans le dossier parent
4. Uploader chaque fichier DCE dans le sous-dossier `DCE` via `mcp__google-workspace__create_drive_file`
5. Stocker le lien du dossier parent (`https://drive.google.com/drive/folders/{folder_id}`) pour usage dans la note Slite

**Exemples de nommage :**
- `kedge-formation-strategie-25-11`
- `ministere-culture-oppic-ia-26-01`
- `montpellier-metropole-25-01`

### 6. Création de la note Slite

**IMPORTANT : Créer une note Slite, PAS un fichier local.**

Utiliser `mcp__slite__create-note` pour créer le brief comme note enfant sous "BDD Appels d'offres".

**Paramètres Slite :**
- Parent note ID : `8wtWoitjnRLYHD`
- Format du titre : `{Organisation} - {Sujet}` (ex. "OPCO Santé - Études IA")
- Format du contenu : markdown

**Template du contenu de la note :**

```markdown
_Brief généré automatiquement par /appel-d-offres_

# 1-liner

[Description courte en 1-2 phrases : type de marché + objet + périmètre]

---

# Infos générales

- **Acheteur** : [Organisation]
- **Valeur totale** : [Budget ou "Non communiqué"]
- **Date limite de candidature** : [Date] → [X jours/semaines restants]
- **Durée du contrat** : [Durée]
- **Type de marché** : [Forfait, régie, accord-cadre...]
- **Lien de l'annonce** : [URL si disponible]
- **Lien du dépôt de réponse** : [URL si disponible]
- **Lien du DCE** : [Lien Drive du dossier DCE — issu de l'étape 5]

## Lot(s) intéressant(s)

- LOT X - [sujet] - [valeur]

---

# Éléments intéressants

## OBJET DU MARCHÉ

[Description détaillée : contexte, enjeux, objectifs, périmètre. 2-3 paragraphes.]

## CONTENU ATTENDU DE L'OFFRE

[Ce qui doit figurer dans la réponse :]
- Structure de la réponse attendue
- Documents à fournir
- Format et contraintes (pages, langue...)

## LIVRABLES

| Livrable | Format | Échéance | Notes |
|----------|--------|----------|-------|
| ... | ... | ... | ... |

## ATTENTES SPÉCIFIQUES

**Méthodologie :** [Méthodologie attendue]
**Compétences clés :** [Compétences recherchées]
**Expérience/Références :** [Exigences d'expérience]
**Équipe :** [Composition attendue]
**Modalités de travail :** [Présentiel, remote, fréquence, localisation]

## CRITÈRES DE SÉLECTION

| Critère | Pondération | Détails |
|---------|-------------|---------|
| Technique | XX% | [Sous-critères si disponibles] |
| Prix | XX% | |
| ... | ... | ... |

**Critères éliminatoires :**
- [Critère 1]
- [Critère 2]

## ÉLÉMENTS FINANCIERS

- **Budget :** [Montant ou "Non communiqué"]
- **Type de marché :** [Forfait, régie, etc.]
- **Modalités de paiement :** [Conditions]
- **Reconduction :** [Si applicable]

---

# Calendrier

- **Date limite de candidature :** [Date] → [X jours/semaines restants]
- **Date de notification :** [Date]
- **Démarrage prévu :** [Date]
- **Contacts / modalités de questions :** [Info]

---

# Références missions STFU

[Missions passées trouvées dans la base Airtable]

- **[ID Mission]** — [Client] : [Description courte] — _[Type de référence]_
- **[ID Mission]** — [Client] : [Description courte] — _[Type de référence]_
- ...

[Si 10+ références : "Plus de X missions potentiellement pertinentes identifiées. Les plus proches sont listées ci-dessus."]

[Si aucune référence : "Aucune mission de référence identifiée dans la base STFU."]

---

# Première impression STFU

**Alignement évident :**
- [Point fort 1]
- [Point fort 2]

**Points d'attention :**
- [Risque/contrainte 1]
- [Risque/contrainte 2]

**Blockers potentiels :**
- [Blocker ou "Aucun identifié"]

---

# Questions & remarques

## Questions pour l'acheteur

_A soumettre rapidement car il y a souvent un long délai de réponse_

- [Question 1]

## Remarques générales

- [Remarque 1]
```

**Après la création de la note :**
Les outils MCP Slite ne permettent pas de définir les propriétés de collection. Informer l'utilisateur de passer manuellement le Status à "Analyse" dans Slite.

### 7. Résumé

Après la création de la note, communiquer à l'utilisateur :
1. L'URL de la note Slite créée
2. L'URL du dossier Drive créé
3. Un rappel de passer le Status à "Analyse" dans Slite
4. Un résumé en 2-3 phrases : sujet, date limite, évaluation de pertinence, nombre de références Airtable trouvées

## Points importants

**Style de communication :**
- Clair et factuel
- Ton direct et orienté action de STFU
- Focus sur l'aide à l'évaluation par les équipes
- Mettre en évidence les informations critiques

**Standards de qualité :**
- Toutes les dates clairement identifiées
- Signaler les ambiguïtés ou informations manquantes dans l'AO
- Utiliser des tableaux pour la clarté des données structurées
- Ne pas laisser de placeholders dans la note finale — si une information n'est pas disponible, écrire "Non communiqué" ou "Non précisé"
- Supprimer les sections du template sans contenu plutôt que de laisser des placeholders vides

**Signaux d'alerte à noter :**
- Demandes de type ESN/body shopping (pas le positionnement STFU)
- Missions purement techniques sans dimension innovation/business
- Consulting théorique sans POC ni test terrain
- Secteurs hors des domaines d'expertise STFU
- Critères obligatoires potentiellement problématiques
- Contraintes de localisation incompatibles

## Ressources

- Profil entreprise : `../../stfu-context.md` (deux niveaux au-dessus du répertoire du skill)
- Table Airtable MISSIONS : base `appyJq6jZuil2VMgC`, table `tbl5qzd6zlaWBKpqs`
- Slite BDD Appels d'offres : note parent `8wtWoitjnRLYHD`
- Dossier Google Drive "Pro - Appels d'Offres" : ID `10op7qXqihbb0-gxc51ACiF02OExPEuZz`

## Exemples d'utilisation

**Exemple 1 : Brief basique**
```
User: "Peux-tu faire un brief de cet AO ? /path/to/appels-offres/ao-innovation/dossier.pdf"

Claude: [Lit le PDF, extrait les informations, évalue la pertinence, recherche dans Airtable]
Claude: [Crée le dossier Drive region-idf-programme-innovation-26-02 avec sous-dossier DCE, uploade le PDF]
Claude: [Crée la note Slite sous BDD Appels d'offres avec le titre "Région IDF - Programme Innovation", inclut le lien Drive]
Claude: "J'ai créé le brief dans Slite : https://startthefup.slite.com/app/docs/XXXXX
        DCE uploadé dans le Drive : https://drive.google.com/drive/folders/XXXXX

        Pense à passer le status à 'Analyse' dans Slite.

        Il s'agit d'un programme d'accompagnement à l'innovation sur 6 mois pour la Région IDF.
        Date limite : 15 février 2026 (26 jours).
        Bon alignement avec STFU — 4 missions de référence identifiées dans la base."
```

**Exemple 2 : AO hors sujet**
```
User: "Brief cet AO : /path/to/ao/infra-reseau.pdf"

Claude: [Lit le PDF, extrait les infos, évalue la pertinence]
Claude: [Utilise AskUserQuestion] "Cet AO porte sur la maintenance d'infrastructure réseau,
        ce qui semble hors du positionnement STFU (pas de dimension innovation/conseil).
        Souhaites-tu quand même que je crée le brief ?"

User: "Non, laisse tomber"
Claude: "OK, AO ignoré."
```

**Exemple 3 : Documents multiples**
```
User: "Brief cet AO : /path/to/ao/reglement.pdf et /path/to/ao/annexe-technique.pdf"

Claude: [Traite les deux documents, consolide les informations, suit le workflow complet]
```
