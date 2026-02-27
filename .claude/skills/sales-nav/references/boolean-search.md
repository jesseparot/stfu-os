# Recherche booléenne — Sales Navigator

Syntaxe, patterns français, templates par persona et pièges à éviter.

---

## Syntaxe

### Opérateurs

| Opérateur | Usage | Exemple |
|-----------|-------|---------|
| `AND` | Les deux termes doivent être présents | `"Directeur" AND "Innovation"` |
| `OR` | Au moins un des termes | `"DSI" OR "CTO" OR "Directeur informatique"` |
| `NOT` | Exclure un terme | `"Directeur" NOT "Adjoint"` |
| `"..."` | Expression exacte | `"Chef de projet digital"` |
| `(...)` | Grouper les expressions | `("DSI" OR "CTO") AND NOT "Adjoint"` |

**Règles** :
- Les opérateurs doivent être en **MAJUSCULES** : `AND`, `OR`, `NOT`
- Les guillemets forcent la correspondance exacte
- Les parenthèses contrôlent la priorité (comme en maths)
- **Limite** : ~15 opérateurs par champ (au-delà, LinkedIn peut ignorer des termes)
- Les opérateurs fonctionnent dans les champs : **Title**, **Keywords**, **Company**

### Champs supportés

| Champ | Supporte le boolean | Recommandation |
|-------|-------------------|----------------|
| **Title** (Titre) | Oui | Le champ principal pour le ciblage. Toujours construire ici. |
| **Keywords** | Oui | Réserver aux compétences niche (SAP, Figma, Kubernetes). Ne PAS y mettre de titres. |
| **Company** (Entreprise) | Oui | Pour cibler/exclure des entreprises par nom. |
| **First Name / Last Name** | Non | Texte simple uniquement. |

---

## Patterns titres français

### Structures courantes

Les titres français suivent des patterns récurrents :

| Pattern | Exemples |
|---------|----------|
| `Directeur/Directrice de {domaine}` | Directeur de l'Innovation, Directrice des Achats |
| `Responsable {domaine}` | Responsable IT, Responsable Transformation |
| `Chef/Cheffe de {domaine}` | Chef de projet digital |
| `Head of {domaine}` | Head of Data, Head of Innovation |
| `VP {domaine}` | VP Engineering, VP Sales |
| `{Domaine} Manager` | Product Manager, IT Manager |

### Gestion du genre

Toujours inclure les variantes masculines et féminines :

```
"Directeur Innovation" OR "Directrice Innovation" OR "Directeur de l'Innovation" OR "Directrice de l'Innovation"
```

Pattern abrégé quand possible :
```
"Dir. Innovation" OR "Directeur Innovation" OR "Directrice Innovation"
```

### Abréviations françaises courantes

| Abréviation | Formes longues à inclure |
|-------------|-------------------------|
| **DSI** | Directeur des Systèmes d'Information, Directrice des Systèmes d'Information, Directeur SI |
| **DRH** | Directeur des Ressources Humaines, Directrice des Ressources Humaines |
| **DAF** | Directeur Administratif et Financier, Directrice Administrative et Financière |
| **DG** | Directeur Général, Directrice Générale |
| **PDG** | Président-Directeur Général, Présidente-Directrice Générale |
| **CMO** | Chief Marketing Officer, Directeur Marketing, Directrice Marketing |
| **CTO** | Chief Technology Officer, Directeur Technique, Directrice Technique |
| **CDO** | Chief Digital Officer, Chief Data Officer, Directeur Digital, Directeur Data |
| **CISO** | Chief Information Security Officer, RSSI, Responsable Sécurité SI |
| **COO** | Chief Operating Officer, Directeur des Opérations, Directrice des Opérations |
| **CFO** | Chief Financial Officer, DAF |
| **CPO** | Chief Product Officer, VP Product, Directeur Produit |

### Équivalents anglais

Les profils français utilisent souvent des titres anglais. **Toujours inclure les deux langues** :

```
("DSI" OR "CTO" OR "Chief Technology Officer" OR "Directeur Technique" OR "Directrice Technique" OR "Directeur des Systèmes d'Information" OR "Directrice des Systèmes d'Information" OR "VP Engineering" OR "VP Technique")
```

---

## Templates par persona type

### C-Level / Direction Générale

```
("PDG" OR "CEO" OR "DG" OR "Directeur Général" OR "Directrice Générale" OR "Président" OR "Présidente" OR "Chief Executive Officer" OR "Managing Director" OR "Gérant" OR "Gérante" OR "Fondateur" OR "Fondatrice" OR "Co-fondateur" OR "Co-fondatrice")
```

### Innovation / Transformation digitale

```
("Directeur Innovation" OR "Directrice Innovation" OR "Chief Innovation Officer" OR "Head of Innovation" OR "Responsable Innovation" OR "VP Innovation" OR "Directeur Transformation" OR "Directrice Transformation" OR "Chief Digital Officer" OR "CDO" OR "Directeur Digital" OR "Directrice Digitale" OR "Head of Digital" OR "Responsable Transformation Digitale")
```

### DSI / Tech

```
("DSI" OR "CTO" OR "Chief Technology Officer" OR "Directeur Technique" OR "Directrice Technique" OR "Directeur des Systèmes d'Information" OR "Directrice des Systèmes d'Information" OR "Directeur Informatique" OR "Directrice Informatique" OR "VP Engineering" OR "VP Technique" OR "Head of IT" OR "Head of Engineering" OR "Responsable IT" OR "Responsable Informatique")
```

### Data / IA

```
("Chief Data Officer" OR "CDO" OR "Directeur Data" OR "Directrice Data" OR "Head of Data" OR "Head of AI" OR "Responsable Data" OR "Data Director" OR "VP Data" OR "Chief AI Officer" OR "Directeur Intelligence Artificielle" OR "Directrice Intelligence Artificielle" OR "Head of Analytics" OR "Responsable IA")
```

### Ressources Humaines

```
("DRH" OR "Directeur des Ressources Humaines" OR "Directrice des Ressources Humaines" OR "Chief People Officer" OR "CPO" OR "VP RH" OR "VP HR" OR "VP People" OR "Head of HR" OR "Head of People" OR "Responsable RH" OR "HR Director" OR "People Director" OR "Directeur du Personnel" OR "Directrice du Personnel")
```

### Achats / Procurement

```
("Directeur des Achats" OR "Directrice des Achats" OR "Chief Procurement Officer" OR "CPO" OR "VP Achats" OR "VP Procurement" OR "Head of Procurement" OR "Head of Purchasing" OR "Responsable Achats" OR "Procurement Director" OR "Purchasing Director" OR "Acheteur" OR "Acheteuse" NOT "Stagiaire" NOT "Alternant")
```

### Marketing

```
("CMO" OR "Chief Marketing Officer" OR "Directeur Marketing" OR "Directrice Marketing" OR "VP Marketing" OR "Head of Marketing" OR "Responsable Marketing" OR "Directeur Communication" OR "Directrice Communication" OR "Head of Growth" OR "VP Growth" OR "Responsable Communication" OR "Marketing Director")
```

### Finance / DAF

```
("DAF" OR "CFO" OR "Chief Financial Officer" OR "Directeur Financier" OR "Directrice Financière" OR "Directeur Administratif et Financier" OR "Directrice Administrative et Financière" OR "VP Finance" OR "Head of Finance" OR "Responsable Financier" OR "Finance Director" OR "Contrôleur de Gestion")
```

### Opérations / Supply Chain

```
("COO" OR "Chief Operating Officer" OR "Directeur des Opérations" OR "Directrice des Opérations" OR "VP Operations" OR "Head of Operations" OR "Responsable Opérations" OR "Supply Chain Director" OR "Directeur Supply Chain" OR "Directrice Supply Chain" OR "Directeur Logistique" OR "Directrice Logistique" OR "Head of Supply Chain" OR "VP Supply Chain")
```

### Juridique / Compliance

```
("Directeur Juridique" OR "Directrice Juridique" OR "Chief Legal Officer" OR "CLO" OR "General Counsel" OR "VP Juridique" OR "VP Legal" OR "Head of Legal" OR "Responsable Juridique" OR "Responsable Conformité" OR "Compliance Officer" OR "Chief Compliance Officer" OR "DPO" OR "Data Protection Officer")
```

### Commercial / Ventes

```
("Directeur Commercial" OR "Directrice Commerciale" OR "Chief Revenue Officer" OR "CRO" OR "Chief Sales Officer" OR "VP Sales" OR "VP Commercial" OR "Head of Sales" OR "Responsable Commercial" OR "Sales Director" OR "Business Developer" OR "Ingénieur d'Affaires" OR "Account Executive" OR "Sales Manager" OR "Directeur des Ventes" OR "Directrice des Ventes")
```

---

## Titres piégeux

### Chef de projet
Trop générique seul. **Toujours qualifier avec le domaine** :
```
"Chef de projet digital" OR "Chef de projet SI" OR "Chef de projet innovation" OR "Chef de projet data"
```
Sans qualification → bruit massif (des milliers de résultats non pertinents).

### Consultant
Qualifier avec secteur ou spécialité. Sans ça, on attrape tous les consultants externes :
```
"Consultant transformation digitale" OR "Consultant innovation" OR "Consultant data"
```
Mieux : exclure avec `NOT Consultant` dans la recherche principale et cibler les postes internes.

### Responsable
Ambigu — peut aller du responsable de magasin au responsable stratégie. **Toujours préciser le domaine** :
```
"Responsable Innovation" OR "Responsable Digital" OR "Responsable Transformation"
```

### Commercial
Mapper toutes les variantes FR et EN :
```
"Commercial" OR "Business Developer" OR "Ingénieur d'Affaires" OR "Account Executive" OR "Sales Manager" OR "Chargé d'Affaires" OR "Responsable Développement Commercial"
```

---

## Patterns d'exclusion

Toujours ajouter des exclusions pour nettoyer les résultats :

### Exclusions standard
```
NOT "Stagiaire" NOT "Alternant" NOT "Alternance" NOT "Apprenti" NOT "Intern"
```

### Exclusions consultants/freelances (si on cible les internes)
```
NOT "Consultant" NOT "Freelance" NOT "Indépendant" NOT "Indépendante"
```

### Exclusions hiérarchiques (si on veut uniquement les N-1/N)
```
NOT "Adjoint" NOT "Adjointe" NOT "Assistant" NOT "Assistante" NOT "Junior"
```

### Exclusion de concurrents / collègues
Ajouter les noms d'entreprise concurrentes dans le champ Company avec NOT :
```
Company: NOT "Nom Concurrent 1" NOT "Nom Concurrent 2"
```

---

## Combinaison complète — Exemple

**Cible** : DSI/CTO dans les ETI industrielles en France, excluant les juniors et consultants.

**Titre** :
```
("DSI" OR "CTO" OR "Chief Technology Officer" OR "Directeur Technique" OR "Directrice Technique" OR "Directeur des Systèmes d'Information" OR "Directrice des Systèmes d'Information" OR "Directeur Informatique" OR "Directrice Informatique" OR "VP Engineering" OR "Head of IT") NOT "Adjoint" NOT "Consultant" NOT "Stagiaire" NOT "Alternant"
```

**Keywords** : *(vide ou compétence niche spécifique)*

**Résultat attendu avec filtres Account** (ETI industrielles France) : 500-1500 résultats → affiner avec spotlights ou sous-secteurs.
