---
name: mission-to-outbound
description: >
  Génère un plan de prospection outbound complet à partir d'une mission STFU réplicable.
  Collecte les données mission (Airtable, Slite, Drive), identifie le pattern réplicable,
  propose des ICP/personas avec filtres Sales Navigator, rédige des séquences email,
  stress-test avec l'oracle, et publie dans Slite.
  Stack cible : Sales Navigator + Evaboot + Lemlist (ouvert à d'autres leviers si pertinent).
  Utiliser quand on veut transformer une mission existante en campagne de prospection.
user_invocable: true
---

# Plan de prospection outbound

Transforme une mission STFU existante en plan de prospection complet, prêt à exécuter sur la stack Sales Nav + Evaboot + Lemlist.

## Déclenchement

L'utilisateur invoque `/mission-to-outbound <nom-mission>`. L'argument est un nom de mission, un client, ou un mot-clé.

```
/mission-to-outbound tcheen
/mission-to-outbound totalenergies ia
/mission-to-outbound chatbot rh
```

**Input** : nom de la mission (ou mot-clé)
**Output** : note Slite avec plan de prospection complet
**Stack outbound par défaut** : Sales Nav → Evaboot → Lemlist (ouvert à d'autres stratégies si plus pertinent au cas par cas)

## Workflow

### Étape 1 — Collecter les données mission (Airtable)

1. Chercher la mission via `mcp__airtable__search_records` (base `appyJq6jZuil2VMgC`, table `tbl5qzd6zlaWBKpqs`) avec le nom/mot-clé fourni.
2. Extraire :
   - Client
   - Description / brief
   - Contexte et enjeux
   - Actions réalisées
   - Résultats et livrables
   - Tags offres, mots-clés
   - **Statut "Client autorisé en public"** (critique pour les séquences email)
3. Si plusieurs résultats : `AskUserQuestion` pour demander lequel.
4. Si aucun résultat : élargir la recherche avec des variantes du mot-clé.

### Étape 2 — Enrichir via Slite

1. Chercher `<nom-mission>` et le nom du client dans Slite via `mcp__slite__search-notes`.
2. Lire les notes pertinentes : notes projet ("Pro - X"), suivis, RETEX, all-hands mentions.
3. Extraire : détails opérationnels, retours clients, problèmes rencontrés, résultats qualitatifs.

### Étape 3 — Chercher les livrables dans le Drive

1. Chercher dans le Drive STFU via `mcp__google-workspace__search_drive_files` (email : résoudre `$GOOGLE_USER_EMAIL` via Bash ; si non défini, demander à l'utilisateur).
2. Prioriser : .docx (livrables), présentations (propales), spreadsheets (devis).
3. Extraire le contenu des livrables clés via `mcp__google-workspace__get_drive_file_content`.
4. Stocker les liens Drive des documents pertinents pour les inclure dans le plan final.

### Étape 4 — Synthétiser le pattern réplicable

À partir des données collectées, formaliser :

1. **Ce qui a été construit** : description précise du livrable/service/système
2. **Pourquoi c'est réplicable** : qu'est-ce qui change d'un client à l'autre vs. qu'est-ce qui reste identique ?
3. **Stack technique** : outils, technos, méthodologies utilisées
4. **Coûts et délais** : ordre de grandeur du projet (budget, durée, équipe)
5. **Résultats mesurables** : métriques, gains, ROI documenté
6. **Nommabilité du client** : vérifier le champ Airtable "Client autorisé en public"

### Étape 5 — Qualifier le livrable attendu avec l'utilisateur

Utiliser `AskUserQuestion` pour confirmer :
- L'angle de vente (ce qu'on pousse exactement)
- Le volume cible de prospects (par défaut ~200 bien ciblés)
- La stack outbound (par défaut Sales Nav + Evaboot + Lemlist, ou autre)
- Le budget/pricing à signaler dans les séquences
- Les verticales déjà en tête (ou exploration libre)

### Étape 6 — Identifier les verticales et ICP

1. **Verticale directe** : même secteur que la mission d'origine
2. **Verticales adjacentes** : identifier 2-3 secteurs où le même pattern s'applique (réglementation similaire, même type de problème, même maturité tech)
3. Pour chaque verticale, définir le profil entreprise : taille, CA, secteur, pression réglementaire ou concurrentielle
4. **Max 3-4 ICP en V1** : mieux vaut 200 prospects bien ciblés que 500 dilués

### Étape 7 — Définir les personas et filtres Sales Navigator

Pour chaque ICP, définir 1-2 personas :

| Champ | Contenu |
|-------|---------|
| Titre Sales Nav | Exact, tel qu'il apparaît dans les filtres |
| Douleur principale | Le problème qu'on résout |
| Déclencheur d'achat | Ce qui rend le besoin urgent maintenant |
| Argument clé | Pourquoi STFU et pas un autre |

**Déléguer la construction des filtres au skill `sales-nav`** (`.claude/skills/sales-nav/SKILL.md`). Suivre ce workflow :

1. Lire `sales-nav/references/boolean-search.md` → construire le boolean titre pour chaque persona (variantes FR/EN, genrées, abréviations, exclusions)
2. Sélectionner les filtres Lead depuis `sales-nav/references/lead-filters.md` (prioriser : Titre boolean > Effectifs > Géographie > Niveau hiérarchique)
3. Sélectionner les filtres Account depuis `sales-nav/references/account-filters.md` (secteur au niveau Account, jamais Lead)
4. Choisir les secteurs exacts depuis `sales-nav/references/industries-taxonomy.md` — utiliser les valeurs de la taxonomie, ne pas inventer de noms de secteur
5. Choisir la stratégie de recherche (Persona-Based par défaut, Account-Based si liste de comptes, Intent si trigger prioritaire)
6. Ajouter 1 spotlight par recherche pour la priorisation P1 (changement de poste, activité récente, offres d'emploi)
7. Estimer le volume avec la méthodologie entonnoir itératif du skill (cible : 200-500 résultats par recherche)
8. Produire la sortie au format template défini dans `sales-nav/SKILL.md` (filtres Lead, filtres Account, Spotlight, volume estimé, recommandation extraction)

### Étape 8 — Rédiger les séquences email

1 séquence par ICP (ou regrouper si les angles sont proches). 4 emails sur 14 jours par séquence.

**Structure :**

| Email | Timing | Contenu | CTA |
|-------|--------|---------|-----|
| Email 1 | J0 | Hook + preuve sociale ou éducatif | Soft (exemple, call 15 min) |
| Email 2 | J3 | Contenu éducatif / technique light + **signal prix** | Medium |
| Email 3 | J7 | Case study avec chiffres quantifiés | Direct (call, démo) |
| Email 4 | J12 | Dernier rappel, angle différent | Direct |

**2 variantes de pitch obligatoires :**
- **Variante A — Résultat business** : centré sur ce que le prospect gagne (ROI, temps, conformité)
- **Variante B — Réplication capability** : centré sur la preuve de ce qu'on a construit (case, chiffres, stack)

Rédiger les 2 variantes pour au moins l'email 1 de chaque séquence.

Utiliser les patterns de `references/sequence-patterns.md` comme base.

### Étape 9 — Stress-test avec l'oracle

1. Invoquer Gemini via `/Users/jesseparot/.local/bin/gemini -m gemini-2.5-flash -p "..." 2>&1` (timeout 120s).
2. Prompt : résumer le plan complet + demander les failles sur :
   - Pertinence des ICP
   - Force du pitch
   - Réalisme du volume
   - Concurrence directe
   - Qualité des CTA
   - Cohérence du pricing
3. Intégrer les retours valides dans le plan final.
4. Documenter les critiques retenues vs. écartées avec justification.

### Étape 10 — Publier dans Slite

1. Créer la note via `mcp__slite__create-note` :
   - `parentNoteId` : `4iSIsQoH4FxNM3` (Pôle expérimentation 2026)
   - `title` : `Exp {Mission} — Plan de prospection`
   - `markdown` : contenu structuré (voir template ci-dessous)

2. Communiquer à l'utilisateur :
   - Lien vers la note Slite
   - Résumé : nombre d'ICP, volume total estimé, prérequis avant lancement
   - Rappel des éléments manquants éventuels

**Template de la note Slite :**

```markdown
_Plan généré par /mission-to-outbound_

# Exp {Mission} — Plan de prospection

## Contexte mission

- **Client** : {Nom} {(nommable en public / anonymisé)}
- **Mission** : {Description courte}
- **Résultats** : {Métriques clés}
- **Sources** : [Airtable]({lien}) · [Drive]({lien}) · [Slite]({lien})

## Pattern réplicable

{Description de ce qui a été construit, pourquoi c'est transférable, ce qui change vs. ce qui reste}

**Stack** : {Outils/technos}
**Ordre de grandeur** : {Budget, durée}

---

## ICP et verticales

### ICP 1 — {Nom}

**Verticale** : {Secteur}
**Profil entreprise** : {Taille, CA, caractéristiques}
**Volume estimé** : {X prospects}

**Persona principal** : {Titre}
- Douleur : {Problème}
- Déclencheur : {Urgence}
- Argument clé : {Pourquoi STFU}

**Filtres Sales Navigator :**
| Filtre | Valeur |
|--------|--------|
| ... | ... |

### ICP 2 — {Nom}
{Même structure}

### ICP 3 — {Nom}
{Même structure}

---

## Séquences email

### Séquence ICP 1 — {Nom}

**Variante A — Résultat business**

**Email 1 (J0)**
Objet : {Objet}
{Corps}

**Email 2 (J3)**
Objet : {Objet}
{Corps}

**Email 3 (J7)**
Objet : {Objet}
{Corps}

**Email 4 (J12)**
Objet : {Objet}
{Corps}

**Variante B — Réplication capability**

**Email 1 (J0)**
Objet : {Objet}
{Corps}

{Séquences suivantes}

---

## Retour oracle

**Critiques retenues :**
- {Critique} → {Ajustement fait}

**Critiques écartées :**
- {Critique} → {Justification}

---

## Prérequis avant lancement

- [ ] {Prérequis 1}
- [ ] {Prérequis 2}
- [ ] {Prérequis 3}

## Prochaines étapes

1. {Étape 1}
2. {Étape 2}
3. {Étape 3}
```

## Règles clés

- **Max 3-4 ICP en V1** : mieux vaut 200 prospects bien ciblés que 500 dilués. On élargit après les premiers retours.
- **Toujours 2 variantes de pitch** : résultat business (Variante A) + réplication capability (Variante B). Testables en A/B dans Lemlist.
- **Signal prix obligatoire** : ordre de grandeur dans la séquence (email 2 ou 3). Pas de prix exact, mais un cadrage ("projets de l'ordre de X€", "à partir de X€").
- **Vérifier "Client autorisé en public"** avant de nommer le client dans les emails. Si non autorisé, anonymiser ("un acteur de la grande distribution", "un leader européen du...").
- **CTA basse friction en email 1** : exemple, démo, call 15 min. Pas de demande lourde au premier contact.
- **Prérequis avant lancement** : toujours lister ce qui manque (métriques à consolider, cas quantifié à préparer, landing page, assets visuels).
- **Ouverture à d'autres leviers** : si l'emailing n'est pas le meilleur canal pour un ICP donné, recommander une alternative (LinkedIn organique, partenariats, événements, contenu, etc.).

## Coordonnées MCP

| Service | Usage | Coordonnées |
|---------|-------|-------------|
| Airtable | Données mission | Base: `appyJq6jZuil2VMgC`, Table missions: `tbl5qzd6zlaWBKpqs` |
| Slite | Notes projet + publication | Parent note prospection: `4iSIsQoH4FxNM3` |
| Google Drive | Livrables, propales | Email: `$GOOGLE_USER_EMAIL` (résoudre via Bash) |
| Gemini Oracle | Stress-test | `/Users/jesseparot/.local/bin/gemini -m gemini-2.5-flash -p "..." 2>&1` |

## Gestion des cas limites

| Cas | Comportement |
|-----|-------------|
| Mission introuvable dans Airtable | Élargir la recherche, puis demander à l'utilisateur de préciser |
| Pas de livrables dans le Drive | Continuer avec Airtable + Slite, noter dans les prérequis |
| Client non autorisé en public | Anonymiser systématiquement dans les séquences email |
| Pas de résultats quantifiés | Signaler dans les prérequis, proposer des métriques à collecter |
| Oracle indisponible | Sauter l'étape 9, noter que le stress-test n'a pas été fait |
| Mission très ancienne / peu documentée | Signaler la limite, proposer un entretien interne pour compléter |

## Exemples d'invocation

```
/mission-to-outbound tcheen
→ Collecte données Airtable + Slite + Drive sur la mission Tcheen
→ Demande de confirmer l'angle et le volume
→ Propose 3 ICP avec personas et filtres Sales Nav
→ Rédige 3 séquences email (variantes A et B)
→ Stress-test avec oracle
→ Publie dans Slite sous "Pôle expérimentation 2026"

/mission-to-outbound chatbot rh
→ Cherche les missions liées aux chatbots RH
→ Identifie le pattern réplicable
→ Propose des verticales (RH, formation, services internes)
→ Même workflow complet

/mission-to-outbound totalenergies
→ Cherche les missions TotalEnergies
→ Si plusieurs, demande laquelle
→ Continue le workflow
```
