# Filtres Account — Sales Navigator

Les 16 filtres disponibles sur une recherche Account (entreprise) dans Sales Navigator.

> **Principe clé** : Toujours filtrer le **secteur** et la **taille** au niveau Account, pas au niveau Lead. Le profil Lead hérite d'attributs souvent imprécis.

---

## Taille

### Effectifs de l'entreprise
- **Type** : Dropdown multi-sélection
- **Fiabilité** : fiable
- **Valeurs** :
  - Self-employed (1)
  - 1-10
  - 11-50
  - 51-200
  - 201-500
  - 501-1000
  - 1001-5000
  - 5001-10000
  - 10001+
- **Recommandation** : Le meilleur proxy de taille. Préférer systématiquement aux tranches de CA.
- **Repères France** :
  - TPE : 1-10
  - PME : 11-250 (51-200 + 201-500 partiellement)
  - ETI : 250-5000 (201-500 + 501-1000 + 1001-5000)
  - Grande entreprise : 5001+

### Chiffre d'affaires annuel
- **Type** : Range (min–max), multi-devise
- **Fiabilité** : peu fiable
- **Valeurs** : Saisie libre en EUR, USD, GBP, etc.
- **Note** : Données basées sur des estimations (Dun & Bradstreet, données publiques). **Très peu fiable pour les entreprises non cotées.** Ne pas baser un ciblage dessus.
- **Recommandation** : Utiliser uniquement en complément des effectifs, jamais seul.

---

## Secteur

### Secteur d'activité (Industry)
- **Type** : Dropdown hiérarchique multi-sélection
- **Fiabilité** : fiable
- **Valeurs** : Voir `industries-taxonomy.md` pour la taxonomie complète.
- **Recommandation** : C'est LE filtre sectoriel à utiliser (pas le secteur Lead). Sélectionner les sous-secteurs précis plutôt que les catégories parentes pour un ciblage fin.

---

## Géographie

### Siège social
- **Type** : Hiérarchique (région → pays → état/département → ville)
- **Fiabilité** : fiable
- **Valeurs courantes** :
  - Europe → France → Île-de-France → Paris
  - Europe → France → Auvergne-Rhône-Alpes → Lyon
- **Note** : Filtre le siège social déclaré. Attention : les entreprises avec des bureaux multiples ne sont localisées qu'au siège.

---

## Croissance

### Croissance des effectifs
- **Type** : Dropdown
- **Fiabilité** : moyen
- **Valeurs** :
  - Croissance négative
  - 0-3%
  - 3-10%
  - 10-20%
  - Plus de 20%
- **Note** : Basé sur l'évolution du nombre d'employés LinkedIn sur 12 mois. Signal de dynamisme. Les entreprises en forte croissance ont plus de budget et plus de besoins.
- **Recommandation** : Combiner avec effectifs pour cibler les scale-ups (ex. : 51-500 + croissance >10%).

### Croissance des effectifs par division
- **Type** : Dropdown par département
- **Fiabilité** : moyen
- **Usage** : Identifier les entreprises qui recrutent dans un département spécifique (ex. : croissance IT = investissement tech).

### Offres d'emploi
- **Type** : Toggle on/off + filtres (fonction, ancienneté, date publication)
- **Fiabilité** : fiable
- **Usage** : Signal d'achat fort. Une entreprise qui recrute un DSI a besoin de solutions IT. Filtrer par fonction pour corréler avec votre offre.
- **Recommandation** : Excellent signal d'intention. Si une entreprise recrute un poste lié à votre offre, c'est qu'elle investit dans ce domaine.

---

## Type d'entreprise

### Type
- **Type** : Dropdown multi-sélection
- **Fiabilité** : fiable
- **Valeurs** :
  - Société cotée en bourse (Public Company)
  - Société privée (Privately Held)
  - Organisation à but non lucratif (Nonprofit)
  - Institution éducative (Educational Institution)
  - Auto-entrepreneur (Self-Employed)
  - Partenariat (Partnership)
  - Agence gouvernementale (Government Agency)
- **Recommandation** : Pour le B2B classique → Société cotée + Société privée. Exclure Self-Employed et Partenariat pour éviter le bruit.

---

## Technologies

### Technologies utilisées
- **Type** : Texte libre / auto-complétion
- **Fiabilité** : peu fiable
- **Valeurs indicatives** : Salesforce, SAP, Oracle, Microsoft 365, HubSpot, Slack, AWS, etc.
- **Note** : Données basées sur des estimations (scraping de sites, offres d'emploi, sources tierces). **Très peu fiable.** Peut servir d'indice complémentaire mais jamais comme filtre principal.
- **Recommandation** : Utiliser uniquement pour enrichir une recherche déjà qualifiée. Ex. : "entreprises utilisant SAP" en complément d'un ciblage sectoriel + taille.

---

## Autres filtres

### Fortune 500
- **Type** : Toggle on/off
- **Fiabilité** : fiable
- **Usage** : Cibler uniquement les entreprises du classement Fortune 500. Peu pertinent pour le marché français, sauf pour les grands groupes internationaux.

### Nombre d'abonnés (page entreprise)
- **Type** : Range (min–max)
- **Fiabilité** : moyen
- **Usage** : Proxy indirect de la taille et de la visibilité de l'entreprise.

### Taille de division
- **Type** : Range par département
- **Fiabilité** : moyen
- **Usage** : Cibler les entreprises avec un département IT de +50 personnes, par exemple.

### Activité récente sur la page entreprise
- **Type** : Toggle
- **Fiabilité** : moyen
- **Usage** : Filtre les entreprises ayant publié récemment sur leur page LinkedIn.

### Listes de comptes
- **Type** : Sélection de liste sauvegardée
- **Usage** : Filtrer/exclure les comptes déjà dans une liste. Indispensable pour le ABM.
- **Recommandation** : Toujours exclure les comptes déjà prospectés.

---

## Résumé par fiabilité

| Fiabilité | Filtres |
|-----------|---------|
| **fiable** | Effectifs, Secteur (Industry), Siège social, Type, Offres d'emploi, Fortune 500, Listes de comptes |
| **moyen** | Croissance effectifs, Croissance par division, Nombre d'abonnés, Taille de division, Activité page |
| **peu fiable** | CA annuel, Technologies |

## Combinaisons recommandées

| Objectif | Filtres |
|----------|---------|
| PME tech en France | Effectifs 51-500 + Secteur "Développement de logiciels" + Siège France |
| ETI industrielles en croissance | Effectifs 201-5000 + Secteur "Industrie manufacturière" (sous-secteurs) + Croissance >10% |
| Grands groupes qui recrutent un CDO | Effectifs 5001+ + Offres d'emploi (fonction: IT/Digital) |
| Scale-ups SaaS | Effectifs 51-500 + Croissance >20% + Type Société privée |
| ABM sur liste | Liste de comptes spécifique + filtres Lead pour le persona |
