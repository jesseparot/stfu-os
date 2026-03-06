---
name: propale
description: >
  Guide la rédaction de propositions commerciales STFU. Framework McKinsey 8 sections
  adapté au positionnement STFU. Détecte le contexte (lead/projet), collecte le brief,
  recherche les missions passées (Airtable), enrichit via Drive/Slite/oracle, qualifie
  le livrable, design l'approche, rédige la propale complète, et propose le handoff
  vers /stfu-slides. Utiliser pour rédiger, créer, préparer ou structurer une proposition
  commerciale, une propale, ou une offre commerciale.
user_invocable: true
---

# Proposition commerciale

Rédige des propositions commerciales structurées selon le framework McKinsey 8 sections adapté STFU, enrichies par les missions passées Airtable et le contexte client.

## Déclenchement

L'utilisateur invoque `/propale` ou demande de rédiger une proposition commerciale.

```
/propale
/propale totalenergies arena
/propale (depuis un dossier lead)
```

**Input** : contexte client (brief, notes de découverte, transcript Granola)
**Output** : markdown structuré 8 sections, prêt pour `/stfu-slides`

## Workflow

### Étape 1 — Détecter le contexte

Identifier automatiquement le contexte selon le répertoire courant :

- **Dossier lead** (`sales/leads/`) : lire le README.md, pré-remplir client, contacts, contexte
- **Dossier projet** (`projects/`) : lire le manifest ou README, extraire client et historique
- **Argument fourni** : utiliser le nom client/sujet passé en argument
- **Sinon** : demander client + sujet via `AskUserQuestion`

Si des fichiers de brief existent dans le dossier (type `brief-propale-*.md`), les lire pour pré-remplir le contexte.

### Étape 2 — Collecter le brief

Utiliser `AskUserQuestion` pour recueillir les informations manquantes :

| Information | Obligatoire | Exemple |
|-------------|-------------|---------|
| Client et interlocuteurs | Oui | TotalEnergies, Cyril Ronot (PM) |
| Sujet / besoin exprimé | Oui | Roadmap innovation Arena x Sismage |
| Audience de la propale | Oui | COPIL / CODIR / COMEX |
| Budget estimé (si connu) | Non | 30-50 k euros |
| Notes de découverte / transcript | Non | Fichier local ou réf. Granola |
| Contraintes (délai, format, équipe) | Non | Livraison sous 10 jours, max 15 slides |
| Concurrents / alternatives | Non | Cabinet X en short-list |

**Si transcript Granola référencé** : récupérer via `mcp__claude_ai_Granola__query_granola_meetings` + `mcp__claude_ai_Granola__get_meeting_transcript` pour extraire les verbatims clés et le contexte de découverte.

> **Gate — Brief validé**
> Présenter la synthèse du brief. Attendre confirmation avant de continuer.

### Étape 3 — Rechercher les missions passées (Airtable)

Même pattern que `/analyse-ao` :

**Coordonnées Airtable :**
- Base ID : `appyJq6jZuil2VMgC`
- Table ID : `tbl5qzd6zlaWBKpqs`
- Recherche via `mcp__airtable__search_records` (cherche dans le Search Field)

**Processus :**
1. Extraire 3-5 mots-clés pertinents du brief (secteur, type de mission, méthodologie, compétences)
2. Lancer plusieurs recherches avec des mots-clés différents pour maximiser la couverture
3. Dédupliquer les résultats
4. Sélectionner 3-5 missions les plus pertinentes pour la section "Pourquoi STFU"
5. Pour chaque mission : ID, client, description courte, résultats quantifiés
6. **Vérifier `Client autorise en public`** avant de nommer un client. Si non autorisé, anonymiser ("un acteur majeur de l'énergie", "un leader européen du...")

### Étape 4 — Rechercher le contexte client (en parallèle)

Lancer en parallèle :

| Source | Action | Données recherchées |
|--------|--------|---------------------|
| **Drive** | `mcp__google-workspace__search_drive_files` | Docs existants sur ce client, propales précédentes, livrables |
| **Slite** | `mcp__slite__search-notes` | Notes internes, CR de meetings, briefs d'AO |
| **Oracle** (si nouveau client ou secteur inconnu) | Gemini via `gemini` | Recherche company, enjeux sectoriels, actualités récentes |

Email Google : résoudre `$GOOGLE_USER_EMAIL` via Bash. Si non défini, demander à l'utilisateur.

### Étape 5 — Qualifier le livrable

Présenter un brief structuré pour validation via `AskUserQuestion` :

```
Qualification du livrable :
- Output : proposition commerciale 12-16 slides equivalent
- Audience : [COPIL/CODIR/COMEX]
- Format : markdown structuré (prêt pour /stfu-slides)
- Registre : [exécutif / opérationnel / technique]
- Contraintes : [budget, délai, format...]
- Angle stratégique : [l'axe principal de la propale]
- Missions de référence : [X missions Airtable identifiées]
```

Calibrer le ton selon l'audience :
- **COMEX** : executive summary lourd, approche synthétique, ROI en avant
- **CODIR** : équilibre stratégie/opérationnel
- **COPIL / opérationnel** : approche détaillée, livrables précis, planning granulaire

> **Gate — Qualification validée**
> Présenter le brief structuré. Attendre confirmation avant de continuer.

### Étape 6 — Designer l'approche

#### 6a — Table de l'approche (5 colonnes)

Construire la table de l'approche au format 5 colonnes. Consulter [references/chiffrage.md](references/chiffrage.md) pour les heuristiques de durée et le vocabulaire emoji.

| Colonne | Contenu |
|---------|---------|
| Phase | Nom de la phase : verbe d'action + objet (ex. "Cartographier les parcours") |
| Étape | Emoji + nom de l'étape (vocabulaire emoji fixe, voir `references/chiffrage.md`) |
| Description | Bullets décrivant l'activité concrète |
| Détail du calcul | Raisonnement explicite (ex. "5 entretiens × 3h ÷ 8h = 1,9 j → 2 j") |
| Durée (j) | Format numérique européen (virgule : 1,5 j), granularité 0,5 j minimum |

**Règles de la table :**
- Sous-totaux par phase + total général
- Marge coordination explicite par phase (10-20%)
- 3-5 phases, chaque phase avec 2-5 étapes

**Informer par les missions passées** : reprendre les approches qui ont fonctionné sur des missions similaires (étape 3).

> **Gate — Approche validée**
> Présenter la table 5 colonnes. Attendre confirmation.
> Une fois validée, les colonnes Phase, Étape et Durée sont verrouillées.
> Seule la colonne Description reste modifiable dans les itérations suivantes.

#### 6b — GANTT

Construire le GANTT au format tableau markdown :
- Semaines en colonnes (S1, S2...)
- `y` pour les lignes de phase (durée globale de la phase)
- `x` pour les lignes d'étape (positionnement précis)
- Étapes indentées sous leur phase
- Adapter le nombre de colonnes à la durée réelle du projet

> **Gate — Planning validé**
> Présenter le GANTT. Attendre confirmation avant de passer à la rédaction.

### Étape 7 — Rédiger la propale complète

Suivre le framework McKinsey 8 sections adapté STFU. Consulter [references/framework.md](references/framework.md) pour la guidance détaillée par section.

Utiliser le template [assets/template.md](assets/template.md) comme structure de base.

| # | Section | Slides equiv. | Contenu clé |
|---|---------|---------------|-------------|
| 1 | Executive summary (SCR) | 1 | Situation, complication, résolution en 3 paragraphes max |
| 2 | Contexte et enjeux | 1-2 | Reformulation empathique du problème client |
| 3 | Pourquoi agir maintenant | 1 | Urgence, coût de l'inaction, fenêtre d'opportunité |
| 4 | Objectifs et convictions | 1-2 | Ce qu'on vise + les partis pris STFU sur le sujet |
| 5 | Notre approche | 3-5 | Phases, timeline, équipe, gouvernance, gates |
| 6 | Investissement | 1 | Budget détaillé par phase + conditions |
| 7 | Pourquoi STFU | 1-2 | Missions de référence Airtable + positionnement |
| 8 | Prochaines étapes | 1 | Actions concrètes avec dates et responsables |
| **Total** | | **12-16** | |

**Règles de rédaction :**
- `stfu-writing` appliqué (pas de title case, mots simples, accents corrects)
- Vérifier `glossary.md` pour l'orthographe des noms propres
- Perspective client-first (jamais "STFU est ravi de...", toujours "Vous faites face à...")
- Pyramid Principle : conclusion d'abord, détails ensuite
- Impact quantifié partout (euros, %, jours, utilisateurs)
- Pas de placeholders dans l'output final. Si une info est inconnue, écrire "A discuter" ou "A définir ensemble"
- Max 20-25 slides equivalent

### Étape 8 — Sauvegarder le draft

**Convention de nommage** : `propale-{sujet}_draft.md`

**Emplacement** (par ordre de priorité) :
1. Dossier lead courant (`sales/leads/{lead}/`)
2. Dossier projet courant (`projects/{projet}/`)
3. `_inbox/` si aucun contexte

### Étape 9 — Proposer les next steps

Après sauvegarde, communiquer :

1. **Chemin du fichier** créé
2. **Résumé** : client, sujet, nombre de phases, budget total, nombre de missions de référence
3. **Next steps proposés** :
   - Relecture et itérations sur le draft
   - `/stfu-slides` pour créer la version Google Slides
   - Upload Drive dans le dossier client (si dossier Drive identifié)
   - Envoi au client (hors scope)

### Étape 10 — (Optionnel) Upload Drive

Si l'utilisateur valide, uploader le draft sur le Drive :
1. Identifier le dossier Drive client via `mcp__google-workspace__search_drive_files`
2. Créer le fichier via `mcp__google-workspace__create_drive_file`
3. Communiquer le lien

## Règles clés

| Règle | Détail |
|-------|--------|
| **Client-first** | Écrire du point de vue du client, pas de STFU. "Vous" avant "nous". |
| **Pyramid Principle** | Conclusion d'abord. Chaque section commence par sa synthèse. |
| **Impact quantifié** | Chaque affirmation forte est appuyée par un chiffre ou un exemple. |
| **Pas de placeholders** | "A discuter" si inconnu, jamais "[MONTANT]" ou "[A COMPLÉTER]". |
| **Calibrer par audience** | COMEX = synthétique. Opérationnel = détaillé. |
| **Max 20-25 slides** | Discipline de concision. Couper le superflu. |
| **Anonymiser si nécessaire** | Vérifier Airtable "Client autorisé en public" systématiquement. |
| **stfu-writing** | Ton direct, mots simples, pas de title case, accents corrects. |
| **Glossaire** | Vérifier `glossary.md` pour les noms propres avant de rédiger. |
| **Format européen** | Virgule décimale pour les durées (1,5 j), pas de point. |
| **Emoji obligatoire** | Chaque nom d'étape dans la table de l'approche commence par un emoji du vocabulaire fixe. |
| **Verrouillage post-gate** | Après gate "Approche validée", Phase/Étape/Durée sont figées. Seule Description est modifiable. |

## Coordonnées MCP

| Service | Usage | Coordonnées |
|---------|-------|-------------|
| Airtable | Missions passées | Base: `appyJq6jZuil2VMgC`, Table: `tbl5qzd6zlaWBKpqs` |
| Slite | Notes internes, CR | Recherche via `mcp__slite__search-notes` |
| Google Drive | Docs client, propales | Email: `$GOOGLE_USER_EMAIL` (résoudre via Bash) |
| Granola | Transcripts meetings | `mcp__claude_ai_Granola__query_granola_meetings` |
| Gemini Oracle | Recherche secteur/client | `gemini -m gemini-2.5-flash -p "..." 2>&1` (timeout 120s) |

## Gestion des cas limites

| Cas | Comportement |
|-----|-------------|
| Pas de missions de référence | Section 7 centrée sur le positionnement STFU sans case studies |
| Pas de budget connu | Section 6 avec fourchette ou "A définir ensemble" |
| Client inconnu (pas d'historique) | Recherche oracle renforcée, pas de Drive/Slite |
| Brief très léger | Poser plus de questions à l'étape 2 |
| Propale urgente | Sections réduites, signaler les zones à compléter |
| Secteur hors expertise STFU | Signaler le risque, proposer un angle "approche transverse" |

## Ressources

- Framework détaillé : [references/framework.md](references/framework.md)
- Chiffrage et heuristiques : [references/chiffrage.md](references/chiffrage.md)
- Template : [assets/template.md](assets/template.md)
- Profil entreprise : `../../stfu-context.md`
- Exemple réel : `projects/totalenergies-arena/brief-propale-arena-sismage.md`

## Exemples d'invocation

**Exemple 1 : depuis un dossier lead**
```
User: (dans sales/leads/acme-dupont-innovation/)
User: /propale

Claude: [Lit README.md du lead, pré-remplit client/contexte]
Claude: [AskUserQuestion pour compléter le brief]
Claude: [Recherche Airtable + Drive + Slite en parallèle]
Claude: [Qualifie le livrable, propose two-pass]
Claude: [Présente l'outline des phases pour validation]
Claude: [Rédige la propale complète]
Claude: "Propale créée : propale-innovation_draft.md
        Client : Acme, 4 phases sur 12 semaines, budget 45-60 k euros.
        3 missions de référence identifiées.

        Next steps :
        - Relecture du draft
        - /stfu-slides pour la version slides
        - Upload Drive"
```

**Exemple 2 : one-shot avec brief fourni**
```
User: /propale
User: "On a un lead chez Decathlon, ils veulent un POC chatbot interne.
       Budget ~20k, décision dans 2 semaines. Audience : direction digitale."

Claude: [Crée le brief, recherche missions chatbot dans Airtable]
Claude: [Mode one-shot vu l'urgence]
Claude: [Rédige directement la propale complète]
Claude: "Propale créée : propale-chatbot-interne_draft.md (dans _inbox/)
        ..."
```

**Exemple 3 : avec transcript Granola**
```
User: /propale — on a eu un call de découverte avec BNP ce matin

Claude: [Récupère le transcript Granola du call BNP]
Claude: [Extrait les insights clés, pré-remplit le brief]
Claude: [Continue le workflow normal]
```
