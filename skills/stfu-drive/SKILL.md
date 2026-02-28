---
name: stfu-drive
description: Naviguer et gérer le Google Drive STFU Team. Utiliser SYSTÉMATIQUEMENT quand on demande de trouver, ouvrir, créer, lister ou organiser des fichiers et dossiers sur Google Drive — ou quand une tâche implique le dossier Drive d'un client, des fichiers projet, des livrables ou des documents partagés. Aussi utiliser quand l'utilisateur référence du contenu Drive implicitement (ex. "trouve la propale Vallourec", "qu'est-ce qu'il y a dans le dossier Kapsul").
---

# STFU Drive

Navigation et gestion efficaces du Google Drive partagé STFU Team via MCP.

## Configuration

- **Email** : Lire `$GOOGLE_USER_EMAIL` depuis l'environnement (`echo $GOOGLE_USER_EMAIL` via Bash). Si non défini, demander à l'utilisateur son email Google `@stfu.pro`. Toujours utiliser cette valeur pour `user_google_email`.
- **Dossier racine** : `💏 STFU Team` — ID : `1MG7LnZzAJPg7EEzbWjX4OfSMH4WL5m-L`

## Structure du Drive

```
💏 STFU Team/
├── Pro - {ClientName}/              # Dossiers clients (un par client)
│   ├── {project-name}/              # Dossiers projets
│   │   ├── STFU <> {ClientName}/    # Partagé avec le client
│   │   └── (tout le reste)          # Interne uniquement — pas visible par le client
│   └── (fichiers au niveau client)  # Docs client transverses
├── 1 - Designs, Graphismes et Logo/
├── 2 - Plaquette et Catalogue/
├── 3 - Présentations, Conférences/
├── 4 - Slides : propales, team.../
├── 5 - Méthode & templates/
├── 6 - Flash/
├── 7 - Formations et prez internes/
├── 8 - Sales/
├── 9 - Marketing/
├── 10 - Podcast/
├── 11 - Factures/
├── 12 - NDAs, Contrats & Templates/
├── 13 - Ressources/
├── 14 - Documents Competitors/
├── 15 - QUALIOPI/
├── 16 - Pole Intrapreneuriat/
├── 17 - Pole Produit / IA/
├── 21 - CHO/
├── 22 - Admin/
└── (spreadsheets, docs à la racine)
```

## Répertoire des dossiers internes

| # | Nom | ID | Contenu |
|---|-----|----|---------|
| 1 | Designs, Graphismes et Logo | `0B8Cks6tL_VP_d3RuZUkzeVNoaTg` | Logos STFU, éléments graphiques, icônes, illustrations, logos clients, assets design (.sketch) |
| 2 | Plaquette et Catalogue | `1EPtaLlq3chznobV_8mIcUnFJNvyqB8jc` | Brochures client-facing, catalogue (accel, open inno), one-sliders, présentations personnalisées client |
| 3 | Présentations, Conférences | `10VWBOBjVXb2wMvPz-O3LfLkqhdX_qEGJ` | Talks et conférences externes (open inno, prototypage, no-code, prise de parole publique), matériaux webinar |
| 4 | Slides : propales, team... | `1eh7-oNGzjzRDa-LFvK_9pFv9b963MDyu` | TOUS LES SLIDES PROPALE, TOUS LES SLIDES CASE STUDIES, TOUS LES SLIDES TEAM master decks, template de proposition, exemples de livrables anonymisés |
| 5 | Méthode & templates | `1MnrcilMvLFUUpwosflRfOrZxNb4FJOFZ` | Méthodologies STFU (open inno, strat orga innovation, biotech/medtech), exemples de structure mission, docs d'onboarding partenaire |
| 6 | Flash | `1TSIqlDklGlm-S8FfK62cnTZSNQjrNnqE` | Programme Flash (offre format court) : deck de proposition, slides programme, variante freelance, P&L, vidéos d'appels de vente, témoignages |
| 7 | Formations et prez internes | `1v-HcDKENn7WuvH_sZn5iT0Zj1D170xgU` | Lunch & learns, présentations stratégie interne, processus de recrutement, moments durabilité, soirées missions |
| 8 | Sales | `1eZTMBVwdJqK85D7plzq__H82OsJk1HBw` | Stack commerciale (listes de prospects, templates Lemlist, liste de contacts Go/No Go, cibles Next120 IA), processus outbound |
| 9 | Marketing | `1SJNRnM0w5ms33Qz2QtpQNogXAtGP4hdS` | Calendrier et stratégie marketing, nurturing, site web, événements clients, réseaux sociaux, livres/mapiful, tables rondes |
| 10 | Podcast | `1huFEznPMGr1N2K7AM194okO7v60zgsHw` | Épisodes de podcast par invité (Seald, Deuxième Avis, Storio, Underdog, Pretto, TechnoFounders, Zeffy, Jow, LDLC...) |
| 11 | Factures | `1-8xltcbrTf6HH50fmneNchd-mtOyC7bK` | Factures clients organisées par nom de client, templates de facturation |
| 12 | NDAs, Contrats & Templates | `1UUbZLbDo5--yelRZLenlGFJwTSt7v44h` | NDAs, CGV, INPI, docs cybersécurité/RGPD, templates de tarification (programme intra) |
| 13 | Ressources | `0B3kuqk-1GG3iWUVid0V4WDVSQzg` | Matériaux de référence généraux |
| 14 | Documents Competitors | `1oRqjG0aJiZm99CPcNJZ-HIXcfNgU3XBG` | Documentation et analyse des concurrents |
| 15 | QUALIOPI | `1BuiimgjN8joZatn2q_2OsInsjccFpOXz` | Certification Qualiopi : docs d'audit, suivi de formation, certificat, BPF, templates de convention |
| 16 | Pole Intrapreneuriat | `169mqNlLQMRvDs3in7VHf88MhdcYwWiSl` | Business unit intrapreneuriat : decks commerciaux, roadmap, listes outbound, livre blanc, contenu blog, decks spécifiques LVMH |
| 17 | Pole Produit / IA | `1yrLD1icUv8eSZzDm6MXoS6am0SdVBqeQ` | Business unit Produit/IA : deck offres IA, ressources & documentation |
| 21 | CHO | `1HVicBwkxzBVQXvMbS1fLW2kaYRigbFQ9` | Bien-être équipe (Chief Happiness Officer) : planning séminaire, vidéos team |
| 22 | Admin | `1bYbfoPHI-tCaDJQ8BXZIXiWP5utwLL-i` | Administratif : suivi des congés, tableurs RH |
| - | 4 - Formations, CAPS, Ateliers Makers | `1CVxqaahRgXzpUR1tG4v6IfUO3xcaJK0W` | Livraison formation : formation GenAI, master confs (innovation, exploration, prototypage), ateliers méthodologie CAPS, ateliers makers, e-learning |
| - | Pro - PUBLIC FOLDER | `1N3zdNNWqQqOzqAbN-2gwhPVVesPemEDa` | Liste de références missions publique (pour réponses AO DC2/DUME) |

## Règles clés

1. **Périmètre par défaut** : Toujours commencer les recherches depuis le dossier racine STFU Team sauf si un client ou projet spécifique est mentionné.
2. **Interne vs partagé** : Les fichiers dans les dossiers `STFU <> {ClientName}` sont partagés avec le client. Tout le reste dans un dossier projet est interne. Ne jamais mettre de contenu confidentiel dans un dossier partagé sans confirmation explicite.
3. **Nommage dossier client** : `Pro - {ClientName}` — correspondre au nommage existant (majuscules, accents) lors de la recherche. Utiliser la recherche floue si le nom exact est incertain.
4. **Nommage dossier partagé** : `STFU <> {ClientName}` — c'est la convention pour les dossiers de collaboration client-facing.

## Workflows

### 1. Trouver le dossier Drive d'un client

1. Rechercher le dossier client : `name contains 'Pro - {ClientName}' and mimeType = 'application/vnd.google-apps.folder'` dans la racine STFU Team
2. Si pas de match exact, essayer un nom partiel ou lister le contenu du dossier racine
3. Retourner le lien du dossier et lister son contenu

### 2. Trouver un fichier spécifique

1. Si le client est connu, restreindre la recherche à l'arborescence de ce client
2. Si le client est inconnu, chercher à travers la racine STFU Team : `name contains '{query}'` avec `folder_id` sur la racine
3. Utiliser `mcp__google-workspace__search_drive_files` avec les opérateurs de requête appropriés
4. Présenter les résultats avec les liens directs

### 3. Explorer un projet

1. Trouver le dossier client (workflow 1)
2. Lister son contenu pour trouver le dossier projet
3. Lister le contenu du dossier projet
4. Distinguer les fichiers internes des fichiers partagés (`STFU <> {ClientName}`) lors de la présentation des résultats

### 4. Trouver des ressources internes

Pour le contenu non-client, utiliser le répertoire des dossiers internes ci-dessus. Lookup rapide :

| Besoin | Dossier # |
|--------|-----------|
| Logos, assets design | 1 |
| Brochures clients, catalogues | 2 |
| Slides de conférences externes | 3 |
| Decks de proposition, slides case study, slides team | 4 |
| Méthodologies, templates de mission | 5 |
| Matériaux du programme Flash | 6 |
| Présentations internes, L&L, onboarding | 7 |
| Listes de prospects, outils outbound, stack commerciale | 8 |
| Calendrier marketing, événements, site web, réseaux sociaux | 9 |
| Épisodes de podcast | 10 |
| Factures clients | 11 |
| NDAs, contrats, CGV, templates juridiques | 12 |
| Matériaux de référence généraux | 13 |
| Intelligence concurrentielle | 14 |
| Certification Qualiopi & docs d'audit | 15 |
| BU intrapreneuriat (decks commerciaux, roadmap) | 16 |
| BU Produit/IA (offres, ressources) | 17 |
| Bien-être équipe, séminaire | 21 |
| RH, admin, suivi congés | 22 |
| Livraison formation (formations, CAPS, ateliers) | 4-Formations |
| Références missions publiques (pour AO/DUME) | Pro - PUBLIC FOLDER |

### 5. Créer un nouveau dossier projet

1. Trouver ou confirmer que le dossier client existe
2. Créer le sous-dossier projet avec un nom descriptif
3. Créer le sous-dossier partagé `STFU <> {ClientName}` à l'intérieur
4. Confirmer la structure avec l'utilisateur avant de partager avec des contacts externes

## Exemples d'utilisation

**"Trouve la propale Kapsul"**
→ Chercher dans le dossier `Pro - Kapsul` les présentations/documents contenant "proposition" ou "proposal"

**"Qu'est-ce qu'il y a dans le dossier Vallourec ?"**
→ Lister le contenu de `Pro - Vallourec`, montrer les projets et fichiers

**"Où sont les templates de contrats ?"**
→ Naviguer vers le dossier `12 - NDAs, Contrats & Templates`, lister le contenu

**"Crée un dossier projet pour la nouvelle mission APHP"**
→ Trouver `Pro - APHP`, créer le sous-dossier projet, créer le sous-dossier partagé `STFU <> APHP` à l'intérieur
