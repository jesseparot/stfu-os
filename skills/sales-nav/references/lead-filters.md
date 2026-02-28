# Filtres Lead — Sales Navigator

Les 34 filtres disponibles sur une recherche Lead dans Sales Navigator, organisés par catégorie.

> **Légende fiabilité** : fiable / moyen / peu fiable

---

## Poste

### Titre de poste (boolean)
- **Type** : Texte libre avec opérateurs booléens
- **Fiabilité** : fiable
- **Usage** : Le filtre le plus fiable pour le ciblage. Supporte AND, OR, NOT, guillemets, parenthèses. Voir `boolean-search.md` pour les patterns.
- **Limite** : ~15 opérateurs par champ.
- **Recommandation** : Toujours construire un boolean titre plutôt que de se fier à Fonction seule.

### Fonction
- **Type** : Dropdown multi-sélection
- **Fiabilité** : moyen
- **Valeurs** :
  - Comptabilité
  - Administration
  - Arts et design
  - Développement commercial
  - Conseil
  - Éducation
  - Ingénierie
  - Entrepreneuriat
  - Finance
  - Soins de santé
  - Ressources humaines
  - Technologies de l'information
  - Juridique
  - Marketing
  - Médias et communication
  - Opérations
  - Achats
  - Gestion de produit
  - Gestion de programmes et de projets
  - Gestion de la qualité
  - Immobilier
  - Recherche
  - Commercial (Ventes)
  - Support
  - Formation et développement
  - Militaire et services de protection
- **Note** : Auto-attribuée par l'algorithme LinkedIn à partir du titre. Peut être inexacte. Utiliser en complément du boolean titre, jamais seule.

### Niveau hiérarchique
- **Type** : Dropdown multi-sélection
- **Fiabilité** : moyen
- **Valeurs** :
  - Non renseigné
  - Débutant (Entry)
  - Formé (Training)
  - Expérimenté (Senior)
  - Gestionnaire (Manager)
  - Directeur (Director)
  - Vice-président (VP)
  - CxO
  - Associé (Partner)
  - Propriétaire (Owner)
  - Stratégique (Strategic)
  - Senior partner
  - Non managérial
- **Note** : Auto-attribuée par LinkedIn. Utile en pré-filtre, mais toujours affiner avec le boolean titre. Les valeurs "Stratégique", "Senior partner" et "Non managérial" ont été ajoutées en 2025.
- **Recommandation** : Pour cibler des décideurs → CxO + VP + Directeur. Pour managers opérationnels → Gestionnaire + Directeur.

### Années dans le poste actuel
- **Type** : Range (min–max)
- **Fiabilité** : moyen
- **Valeurs** : 1-2, 3-5, 6-10, Plus de 10
- **Note** : Utile pour cibler les personnes récemment en poste (plus ouvertes au changement) ou installées (plus de pouvoir de décision).

### Années dans l'entreprise actuelle
- **Type** : Range (min–max)
- **Fiabilité** : moyen
- **Valeurs** : 1-2, 3-5, 6-10, Plus de 10

---

## Entreprise du lead

### Entreprise actuelle
- **Type** : Texte libre / auto-complétion
- **Fiabilité** : fiable
- **Usage** : Pour du ciblage ABM (Account-Based). Saisir le nom exact de l'entreprise. Plusieurs entreprises possibles.
- **Recommandation** : Préférer les listes de comptes pour du ABM massif.

### Ancienne entreprise
- **Type** : Texte libre / auto-complétion
- **Fiabilité** : fiable
- **Usage** : Cibler les anciens de certaines entreprises (alumni targeting). Ex. : anciens de McKinsey maintenant en entreprise.

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
- **Note** : Un des filtres les plus fiables. Préférer aux tranches de CA.

### Type d'entreprise
- **Type** : Dropdown multi-sélection
- **Fiabilité** : fiable
- **Valeurs** :
  - Société cotée en bourse
  - Société privée
  - Organisation à but non lucratif
  - Institution éducative
  - Auto-entrepreneur
  - Partenariat
  - Agence gouvernementale

### Siège social de l'entreprise
- **Type** : Géographie (pays / région / ville)
- **Fiabilité** : fiable
- **Note** : Filtre le siège social déclaré. Attention : un salarié à Lyon dans une entreprise dont le siège est à Paris sera exclu si on filtre siège = Lyon.

---

## Personnel

### Géographie
- **Type** : Hiérarchique (région → pays → état/département → ville)
- **Fiabilité** : fiable
- **Valeurs courantes France** :
  - France (pays)
  - Île-de-France, Auvergne-Rhône-Alpes, Nouvelle-Aquitaine, Occitanie, etc. (régions)
  - Paris, Lyon, Marseille, Toulouse, Nantes, etc. (villes)
- **Note** : Basé sur la localisation du profil. Peut ne pas correspondre au lieu de travail réel (télétravail).
- **Recommandation** : Pour la France entière, sélectionner "France". Pour l'Île-de-France, sélectionner la région.

### Secteur du lead
- **Type** : Dropdown hiérarchique
- **Fiabilité** : peu fiable
- **Note** : Auto-attribué par LinkedIn. **Ne pas utiliser pour le ciblage sectoriel.** Toujours préférer le filtre Industry au niveau Account (voir `account-filters.md`).

### Code postal
- **Type** : Texte + rayon
- **Fiabilité** : moyen
- **Usage** : Ciblage très local (rayon autour d'un code postal).

### Groupes
- **Type** : Texte libre / auto-complétion
- **Fiabilité** : fiable
- **Usage** : Cibler les membres de groupes LinkedIn spécifiques. Utile pour les communautés métier.

### École
- **Type** : Texte libre / auto-complétion
- **Fiabilité** : fiable
- **Usage** : Ciblage par formation. Ex. : anciens de HEC, Polytechnique, ESSEC.

### Langues du profil
- **Type** : Dropdown
- **Fiabilité** : moyen
- **Valeurs courantes** : Français, Anglais, Espagnol, Allemand, Italien, Portugais, etc.
- **Note** : Basé sur les langues déclarées dans le profil.

### Années d'expérience
- **Type** : Range (min–max)
- **Fiabilité** : peu fiable
- **Valeurs** : 1-2, 3-5, 6-10, Plus de 10
- **Note** : Calculé automatiquement par LinkedIn à partir de l'historique. Souvent imprécis (trous de carrière, études, etc.). **Éviter comme filtre principal.**

### Prénom
- **Type** : Texte libre
- **Fiabilité** : fiable
- **Usage** : Très rarement utile sauf ciblage nominal.

### Nom de famille
- **Type** : Texte libre
- **Fiabilité** : fiable
- **Usage** : Très rarement utile sauf ciblage nominal.

---

## Spotlight

### Changement de poste récent
- **Type** : Toggle on/off
- **Fiabilité** : fiable
- **Note** : Personnes ayant changé de poste dans les 90 derniers jours. **Signal d'achat fort** — les nouveaux arrivants cherchent à faire leurs preuves et sont plus ouverts.
- **Recommandation** : Excellent pour du trigger-based prospecting. Limite le volume mais augmente les taux de réponse.

### Activité LinkedIn récente
- **Type** : Toggle on/off
- **Fiabilité** : fiable
- **Note** : Publication ou commentaire dans les 30 derniers jours. Indique un profil actif, plus susceptible de voir/répondre aux InMails.

### Connexions partagées
- **Type** : Dropdown (1er degré, 2e degré, 3e degré+)
- **Fiabilité** : fiable
- **Note** : 2e degré = connexions de vos connexions. Idéal pour les introductions. 3e degré = réseau élargi.

### Suit votre entreprise
- **Type** : Toggle on/off
- **Fiabilité** : fiable
- **Note** : Personnes qui suivent la page LinkedIn de STFU. Signal d'intérêt faible mais utile.

### A consulté votre profil
- **Type** : Toggle on/off
- **Fiabilité** : fiable
- **Note** : Disponible avec compte Sales Nav. Signal d'intérêt.

### Mentionné dans les actualités
- **Type** : Toggle on/off
- **Fiabilité** : moyen
- **Note** : Couverture presse récente. Utile mais volume faible.

---

## Workflow et listes

### Listes de leads
- **Type** : Sélection de liste sauvegardée
- **Usage** : Filtrer/exclure les leads déjà dans une liste.
- **Recommandation** : Exclure les leads déjà contactés pour éviter les doublons.

### Recherches enregistrées
- **Type** : Sélection de recherche sauvegardée
- **Usage** : Réutiliser une recherche existante comme base.

### Leads sauvegardés
- **Type** : Toggle
- **Usage** : N'afficher que les leads sauvegardés.

### Leads du CRM
- **Type** : Toggle
- **Usage** : Filtrer selon les leads synchronisés avec le CRM (si intégration active).

### Personas
- **Type** : Sélection de persona sauvegardé
- **Usage** : Appliquer un profil de recherche pré-configuré.
- **Note** : Les personas Sales Nav sauvegardent une combinaison de filtres. Utile pour les recherches récurrentes.

---

## Résumé des filtres par fiabilité

| Fiabilité | Filtres |
|-----------|---------|
| **fiable** | Titre (boolean), Entreprise actuelle/ancienne, Effectifs, Type entreprise, Siège social, Géographie, Groupes, École, Spotlights |
| **moyen** | Fonction, Niveau hiérarchique, Années dans poste/entreprise, Langues, Code postal |
| **peu fiable** | Secteur lead, Années d'expérience |
