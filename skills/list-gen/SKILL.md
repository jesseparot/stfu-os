---
name: list-gen
description: >
  Génère et enrichit des listes de prospects pour des campagnes outbound ou de l'exploration.
  Workflow de bout en bout : brief, stratégie Sales Navigator (via /sales-nav),
  recherche manuelle + export Evaboot, analyse et nettoyage de la liste, enrichissement
  Dropcontact, livraison (Google Drive ou campagne Lemlist via MCP).
  Utiliser pour construire une liste de prospects, générer des leads, créer une liste
  outbound, nettoyer/analyser une liste exportée, enrichir des contacts, ou préparer
  une liste pour une campagne. Aussi déclenché par /list-gen. Diffère de /mission-to-outbound
  qui part d'une mission passée. Ce skill est le workflow autonome de construction de liste
  utilisable dans tout contexte (exploration, expérimentation outbound, prospection classique).
---

# Workflow de génération de listes

Processus en 6 étapes du brief à la liste livrable. Les étapes 1-2 et 4-6 sont automatisées. L'étape 3 est un handoff humain.

## Étape 1 : Brief

Clarifier l'objectif et les paramètres de la liste. Demander :

- **Objectif** : exploration pour un projet, expérimentation outbound, ou campagne outbound classique ?
- **Cible** : qui cherche-t-on ? (persona, industrie, taille d'entreprise, géographie)
- **Volume** : combien de contacts nécessaires ?
- **Destination** : Google Drive (pour usage manuel) ou Lemlist (pour campagne automatisée) ?
- **Contexte** : un projet client existant, une mission, ou une liste précédente sur laquelle s'appuyer ?

Résumer le brief. Obtenir la validation de l'utilisateur avant de continuer.

## Étape 2 : Stratégie Sales Navigator

Invoquer `/sales-nav` pour co-construire la stratégie de recherche :
- Choisir le type de stratégie (Persona / Account-Based / Intent)
- Définir la boolean search, les filtres, les objectifs de volume
- Sortie : paramètres de recherche Sales Navigator prêts à exécuter

## Étape 3 : Recherche manuelle + Export Evaboot (handoff humain)

Mettre en pause et instruire l'utilisateur :

> Exécute la recherche Sales Navigator avec les filtres de l'étape 2.
> Exporte les résultats via Evaboot.
> Dépose le fichier CSV dans le dossier du projet ou partage le chemin.

Attendre que l'utilisateur fournisse le chemin du fichier exporté.

## Étape 4 : Analyse et nettoyage de la liste

Lire le CSV (utiliser le skill `/xlsx` si .xlsx). Analyser chaque contact par rapport au brief.

### Gestion des colonnes

À la réception d'un export Evaboot/Sales Navigator, le CSV contient typiquement 60+ colonnes. Pour la qualification et l'enrichissement, ne garder que ces colonnes essentielles :

**À garder (19 colonnes) :**

| Colonne | Usage |
|---------|-------|
| First Name | Identité + Dropcontact |
| Last Name | Identité + Dropcontact |
| Current Job | Qualification de titre (critère principal) |
| LinkedIn URL Public | Enrichissement Dropcontact + outreach |
| Sales Navigator URL | Référence |
| Is Open Profile | Stratégie InMail |
| Company Name | Qualification entreprise |
| Company Domain | Dropcontact + vérification |
| Company Employee Exact Count | Filtre taille |
| Company Employee Range | Filtre taille (backup) |
| Company Industry | Filtre secteur |
| Company Description | Comprendre l'activité de l'entreprise — clé pour qualifier les cas limites |
| Company Specialities | Mots-clés, complète la description |
| Company Location | Géographie |
| Profile Headline | Contexte rapide de la personne |
| Profile Summary | Personnalisation + qualification des cas limites |
| Job Description | Qualification — révèle l'activité événementielle/sectorielle même quand le tag industrie est faux |
| Location (person) | Géographie |
| Has New Position | Priorisation P1 (nouveau poste = plus ouvert au changement) |

**À supprimer (34+ colonnes) :** Email/Email Status (généralement vides depuis SN), toutes les URLs de photos, LinkedIn Unique IDs, Connections, Is Premium, Is Open To Work, Education, Skills, Languages, Volunteer, Follower Count, Technologies, Posting Frequency, InMail Restriction, Profile Timezone, Months/Years in Position/Company, Revenue Currency, Funding Stage, Company Type Detailed, Company Website URL (redondant avec Domain), Matches Filters, No Match Reasons.

### Méthodologie de qualification

**Ne PAS faire confiance aveuglément à la colonne "Matches Filters" d'Evaboot.** Lancer une qualification indépendante en utilisant :

1. **Score de titre** (0-3) :
   - 3 = Niveau directeur : Directeur/trice Commercial(e), Head of Sales, Sales Director, Directeur du Développement
   - 2 = Niveau manager : Responsable Commercial, Responsable Développement Commercial
   - 1 = IC/Connexe : Business Developer, Chargé de développement
   - 0 = Exclu : Stagiaire, Intern, Alternant, Assistant, Junior, Retraité, "Work Study"

2. **Match secteur entreprise** (0-3) : Vérifier TOUS les champs textuels — Company Industry seul n'est pas fiable. Les tags industrie LinkedIn sont souvent faux.
   - Chercher dans Company Description + Company Specialities + Company Name + Profile Summary + Job Description + Profile Headline les mots-clés sectoriels
   - Un contact tagué "Software Development" peut travailler dans une entreprise event tech (ex. Eventmaker, AppCraft EVENTS)
   - Une entreprise "Business Consulting" peut en réalité être une agence événementielle

3. **Taille entreprise** (0-2) :
   - 2 = Dans la fourchette (dépend de l'ICP, typiquement 11-500)
   - 1 = Limite ou inconnu (ne pas auto-rejeter les tailles inconnues)
   - 0 = Hors fourchette (solopreneur, ou 10001+)

4. **Vérification de séniorité** : Après qualification, vérifier la distribution hiérarchique :
   - Director (44%) + Manager (45%) = niveau décideur -> cible
   - IC/Business Developer (~10%) = potentiellement trop junior pour un outreach décideur
   - Signaler et demander à l'utilisateur s'il faut inclure les contacts niveau IC

5. **Drapeaux de priorisation** :
   - P1 : Has New Position = Yes (nouveau poste = plus réceptif à l'outreach)
   - P2 : Is Open Profile = True (possibilité de contacter directement)

### Catégories de sortie

- **KEEP_A** : Bon score titre + match secteur + match taille
- **KEEP_B** : Bon globalement mais un critère légèrement plus faible
- **REVIEW** : Bon titre mais secteur incertain — vérifier Profile Summary + Job Description pour les mots-clés sectoriels
- **DROP** : Mismatch clair sur titre, secteur ou taille

Présenter un résumé avec les comptages par catégorie, puis demander à l'utilisateur ses décisions de volume/format avant de générer le CSV de sortie.

## Étape 5 : Enrichissement Dropcontact

Enrichir les contacts restants via le MCP Dropcontact.

### Choix de l'outil

| Données disponibles | Outil MCP | Fiabilité |
|---------------------|-----------|-----------|
| Prénom + nom + entreprise | `enrich_contact_with_first_last_company` | **Meilleure** — retourne email, téléphone, SIRET, NAF, CA, adresse |
| Nom complet + entreprise | `enrich_contact_with_full_name_company` | Bonne — même sortie, utiliser quand les noms ne sont pas séparés |
| URL LinkedIn | `enrich_contact_with_linkedin_url` | **Faible** — retourne souvent uniquement l'URL, pas de données d'enrichissement |

**Toujours préférer `enrich_contact_with_first_last_company`** à la méthode URL LinkedIn. Malgré l'apparente précision de la méthode URL LinkedIn, la méthode prénom/nom/entreprise retourne des données significativement plus riches.

### Données d'enrichissement retournées

Un enrichissement réussi ajoute : email (avec qualification + validité), company_phone, company_website, company_siret, company_naf5_code, company_naf5_description, company_turnover, company_address (rue + CP + ville), company_country.

### Workflow

**> 80 contacts : générer un CSV pour upload web Dropcontact.** L'enrichissement MCP est trop lent pour les grandes listes (~10s par contact). Générer un CSV avec les colonnes `first_name`, `last_name`, `company`, `linkedin`, `website` et instruire l'utilisateur de l'uploader sur dropcontact.com pour un enrichissement en masse. Une fois le fichier enrichi récupéré, le fusionner avec le CSV qualifié.

**<= 80 contacts : enrichir directement via MCP.** Traiter par lots parallèles de 10. Tracker le succès/échec pour chaque contact. Ajouter les colonnes d'enrichissement : enriched_email, email_qualification, email_is_valid, company_phone, company_website_dc, company_siret, company_naf_code, company_naf_description, company_turnover, company_address, company_zip, company_city, enrichment_status.

Utiliser `validate_email_address` sur les résultats où email_is_valid est false ou manquant.

### Rapport

Présenter : total traité, emails trouvés (nombre + %), emails valides, emails invalides, échecs d'enrichissement, et tout pattern notable (ex. "les petites entreprises <10 employés ont un taux de hit email plus bas").

## Étape 6 : Livraison

Selon la destination définie dans le brief :

### Option A : Google Drive
Utiliser le skill `stfu-drive` pour naviguer vers le dossier cible. Uploader la liste enrichie via le MCP Google Workspace.

### Option B : Campagne Lemlist
Utiliser le skill `/lemlist` pour créer ou mettre à jour la campagne. Importer les contacts enrichis comme leads. Confirmer le nombre de leads et la déduplication.

### Option C : Fichier local
Sauvegarder le CSV nettoyé + enrichi dans le dossier du projet.

## Dépendances de skills

| Skill | Quand |
|-------|-------|
| `/sales-nav` | Étape 2 — construction des filtres |
| `/xlsx` | Étape 4 — si l'export est en .xlsx |
| `/lemlist` | Étape 6 Option B — création de campagne |
| `stfu-drive` | Étape 6 Option A — livraison Drive |
