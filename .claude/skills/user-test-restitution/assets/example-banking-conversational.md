# Restitution Tests Utilisateurs - Banque Mobile Conversationnelle
**Date** : 2026-02-02
**Nombre de participants** : 5
**Phase** : Premier prototype

## 🎯 Executive Summary

### Verdict global
Le prototype conversationnel est **validé dans son concept** mais nécessite des **ajustements majeurs sur la compréhension du langage naturel**. 4 utilisateurs sur 5 ont exprimé un intérêt fort pour une banque conversationnelle, mais 3 sur 5 ont été bloqués par des incompréhensions de leurs formulations naturelles.

### Insights clés
1. **Mental model "messagerie" vs "formulaire"** : Les utilisateurs s'attendent à une conversation fluide comme WhatsApp, pas à un questionnaire guidé étape par étape
2. **Confiance limitée sur les montants** : 5/5 utilisateurs vérifient plusieurs fois avant de valider un virement, même avec confirmation conversationnelle
3. **Langage bancaire vs langage quotidien** : "Bénéficiaire" n'est pas compris (4/5), les utilisateurs disent "la personne à qui j'envoie de l'argent"

### Top 3 blockers critiques
1. **Incompréhension formulations naturelles** : 3/5 utilisateurs bloqués - L'IA ne reconnaît pas "virer 50€ à Marie" et demande de reformuler en langage formel
2. **Absence de historique conversationnel** : 5/5 utilisateurs frustrés - Doivent répéter le contexte à chaque nouvelle demande
3. **Validation des montants ambiguë** : 4/5 utilisateurs confus - Ne comprennent pas si le montant est validé ou s'il faut encore confirmer

### Quick Wins
- [ ] Enrichir les synonymes NLU : "virer/envoyer/transférer", "personne/ami/contact" → Impact : déblocage de 3/5 utilisateurs
- [ ] Ajouter récapitulatif visuel avant validation finale → Impact : réduction de l'anxiété sur 5/5 utilisateurs
- [ ] Reformuler "Bénéficiaire" → "À qui voulez-vous envoyer de l'argent ?" → Impact : compréhension immédiate

---

## 📋 Méthodologie

### Participants
| Profil | Âge | Usage banque mobile | Aisance digitale | Usage assistants vocaux |
|--------|-----|---------------------|------------------|-------------------------|
| Nina | 32 | Quotidien | ⭐⭐⭐⭐☆ | Siri (occasionnel) |
| Marc | 45 | Hebdomadaire | ⭐⭐⭐☆☆ | Aucun |
| Sophie | 28 | Quotidien | ⭐⭐⭐⭐⭐ | Alexa (fréquent) |
| Thomas | 38 | Mensuel | ⭐⭐☆☆☆ | Google (rare) |
| Léa | 25 | Quotidien | ⭐⭐⭐⭐⭐ | Tous (power user) |

**Échantillon** : Diversité d'âge (25-45 ans), d'aisance digitale, et d'usage d'interfaces conversationnelles

### Protocole
- **Durée moyenne** : 25 minutes par test
- **Format** : Présentiel, mobile personnel
- **Scénarios testés** :
  1. Virement à un proche (50€)
  2. Consultation de solde et dernières opérations
  3. Question ouverte sur un débit inconnu
- **Périmètre** : Interface conversationnelle uniquement (pas de fallback formulaire classique)

---

## 📊 Résultats par parcours

### Parcours 1 : Virement conversationnel
**Objectif utilisateur** : Envoyer 50€ à un proche en discutant avec l'assistant

#### Métriques
- ✅ **Taux de réussite** : 2/5 utilisateurs (40%)
- ⏱️ **Temps moyen** : 3min 45s (vs 1min attendu)
- 🔄 **Reformulations nécessaires** : 5/5 utilisateurs ont dû reformuler au moins une fois

#### Points de friction majeurs
**1. Incompréhension du langage naturel** - 3/5 utilisateurs bloqués
- *Observation* : L'utilisateur tape "Je veux virer 50€ à Marie", l'IA répond "Je n'ai pas compris, voulez-vous effectuer un virement ?"
- *Verbatims représentatifs* :
  > "Mais je viens de dire que je veux virer de l'argent, pourquoi elle ne comprend pas ?" — Nina
  > "C'est censé être conversationnel mais ça comprend rien..." — Marc
- *Cause identifiée* : Modèle NLU trop restrictif, entraîné sur langage bancaire formel
- *Recommandation* : Enrichir le corpus NLU avec formulations grand public (virer/envoyer/transférer, personne/ami/contact)

**2. Absence de mémoire conversationnelle** - 5/5 utilisateurs frustrés
- *Observation* : Après avoir complété le virement, l'utilisateur demande "C'est bien parti ?", l'IA demande "De quel virement parlez-vous ?"
- *Verbatims* :
  > "Euh... le virement dont on parle depuis 3 minutes ??!" — Sophie
  > "Elle devrait se souvenir de ce qu'on vient de faire non ?" — Léa
- *Cause* : Pas de contexte conversationnel maintenu entre les messages
- *Recommandation* : Implémenter mémoire de session (minimum 5 derniers messages)

**3. Validation finale ambiguë** - 4/5 utilisateurs confus
- *Observation* : Message "Le virement de 50€ à Marie est prêt" → utilisateurs ne savent pas si c'est validé ou s'il faut encore cliquer quelque part
- *Verbatims* :
  > "Prêt ça veut dire fait ou pas fait ?" — Thomas
  > "Je dois faire quoi maintenant ?" — Marc
- *Cause* : Formulation passive, pas de Call-to-Action clair
- *Recommandation* : Ajouter bouton explicite "Valider le virement" + récapitulatif visuel

#### Ce qui fonctionne
- ✅ **Ton conversationnel apprécié** - 5/5 utilisateurs
  > "J'aime bien le fait que ça parle normalement, c'est moins froid qu'une banque" — Nina
- ✅ **Guidage par questions** - 3/5 utilisateurs trouvent ça rassurant
  > "Elle me demande étape par étape, je suis pas perdu" — Thomas

---

### Parcours 2 : Consultation de solde
**Objectif utilisateur** : Demander son solde et voir les dernières opérations

#### Métriques
- ✅ **Taux de réussite** : 5/5 utilisateurs (100%)
- ⏱️ **Temps moyen** : 45s

#### Points de friction majeurs
**1. Verbosité de la réponse** - 3/5 utilisateurs
- *Observation* : L'IA donne le solde + explique le calcul + liste les 3 dernières opérations = 8 lignes de texte
- *Verbatims* :
  > "Trop de blabla, je veux juste le chiffre" — Léa
  > "J'ai arrêté de lire après la deuxième ligne" — Sophie
- *Recommandation* : Réponse courte par défaut, proposer "En savoir plus" si besoin de détails

#### Ce qui fonctionne
- ✅ **Compréhension parfaite** - 5/5 utilisateurs avec formulations variées ("C'est quoi mon solde ?", "Combien j'ai ?", "Mon compte ?")
- ✅ **Affichage visuel du solde** - 5/5 utilisateurs apprécient la carte visuelle en complément du texte

---

### Parcours 3 : Question sur débit inconnu
**Objectif utilisateur** : Demander "C'est quoi ce débit de 23,50€ ?"

#### Métriques
- ✅ **Taux de réussite** : 4/5 utilisateurs (80%)
- ⏱️ **Temps moyen** : 1min 20s

#### Points de friction majeurs
**1. Reformulation imprécise** - 2/5 utilisateurs
- *Observation* : Utilisateur dit "C'est quoi ce truc à 23€", l'IA ne trouve pas l'opération (montant exact : 23,50€)
- *Recommandation* : Tolérance sur les montants arrondis (±1€)

#### Ce qui fonctionne
- ✅ **Détection des débits inhabituels** - 4/5 utilisateurs impressionnés que l'IA identifie les opérations suspectes
  > "Ah c'est pratique qu'elle me dise direct si c'est bizarre" — Nina

---

## 💡 Insights thématiques transverses

### Compréhension / Mental Model
**Constat** : Les utilisateurs s'attendent à une conversation **fluide et contextuelle** comme avec un humain, pas à un chatbot qui oublie tout entre chaque message (5/5 utilisateurs)

*Exemples* :
- Nina : "Je peux lui parler comme à un ami ?" puis déçue quand l'IA ne comprend pas ses formulations naturelles
- Léa : Compare à ChatGPT et s'étonne que l'IA ne se souvienne pas du contexte

**Impact** : Frustration élevée, impression de "faux conversationnel"

**Recommandation** :
1. Communiquer clairement les limites ("Je me souviens des 5 derniers messages")
2. Améliorer la NLU pour accepter le langage quotidien
3. Maintenir le contexte conversationnel sur toute la session

---

### Navigation / Architecture d'information
**Constat** : La navigation conversationnelle pure (sans boutons/menu) désoriente 3/5 utilisateurs quand ils ne savent pas quoi demander

*Exemples* :
- Marc : "Je peux faire quoi d'autre avec cette app ?" - ne sait pas comment découvrir les fonctionnalités
- Thomas : Cherche un menu, ne trouve pas, abandonne l'exploration

**Impact** : Utilisation limitée aux fonctionnalités explicitement connues

**Recommandation** :
1. Ajouter des suggestions contextuelles ("Vous pouvez aussi : Voir vos dépenses, Faire un virement, etc.")
2. Bouton "Que puis-je faire ?" accessible en permanence
3. Onboarding pour montrer les commandes principales

---

### Valeur perçue
**Constat** : 4/5 utilisateurs voient la valeur pour des **tâches simples et récurrentes** (solde, dernier virement), mais pas pour des opérations complexes

*Exemples* :
- Sophie : "Pour virer 50€ à un pote oui, mais pour un virement SEPA international je préfère le formulaire classique"
- Léa : "C'est rapide pour les trucs que je fais souvent, mais je m'inquiéterais de me tromper sur un gros montant"

**Impact** : Adoption conditionnelle au type d'opération

**Recommandation** :
1. Positionner le conversationnel comme **canal complémentaire** (pas remplacement)
2. Proposer fallback vers formulaire classique pour opérations sensibles/complexes
3. Communiquer les use cases idéaux (virements rapides, consultation, questions)

---

### Émotions / Satisfaction
**Constat** : Forte **anxiété sur les montants** même avec conversationnel (5/5 utilisateurs vérifient plusieurs fois avant validation)

*Exemples* :
- Nina : Vérifie 3 fois le montant et le destinataire avant de valider
- Marc : "Je préfère quand même voir un récap clair avant de valider, juste au cas où"

**Impact** : Le conversationnel ne réduit PAS l'anxiété financière (contrairement à l'hypothèse initiale)

**Recommandation** :
1. Toujours afficher récapitulatif **visuel** avant validation (pas juste texte)
2. Possibilité d'annuler immédiatement après validation
3. Confirmation SMS/push pour rassurer

---

## 🗣️ Interaction conversationnelle

### Langage utilisé spontanément
**Formulations naturelles observées** :
- Nina : "Je veux virer 50€ à Marie"
- Marc : "Envoie 50 balles à Marie"
- Sophie : "Transfère 50€ sur le compte de Marie"
- Thomas : "Faire un virement de 50€"
- Léa : "Peux-tu envoyer 50€ à Marie ?"

**Écart avec formulations système** :
- Système attend : "Effectuer un virement" / "Bénéficiaire" / "Montant"
- Utilisateurs disent : "Virer/envoyer" / "La personne/mon ami(e)" / "50 balles/euros"
- **Impact** : 3/5 utilisateurs ne sont pas compris du premier coup

### Compréhension des réponses
**Ton perçu** :
- 4/5 utilisateurs : "Juste bien, professionnel mais pas trop formel"
- 1/5 utilisateur (Léa) : "Un peu trop poli, on dirait un robot banquier"

**Longueur des réponses** :
- 3/5 utilisateurs : "Trop verbeux sur consultation solde et historique"
- 2/5 utilisateurs : "OK, ça donne le contexte"

**Verbatims représentatifs** :
> "J'aime bien le ton, c'est comme parler à quelqu'un de la banque mais en sympa" — Nina
> "Des fois elle parle trop, je veux juste l'info rapide" — Sophie

### Confiance dans l'IA
**Comportements de vérification** :
- 5/5 utilisateurs vérifient le récapitulatif plusieurs fois avant validation
- 2/5 utilisateurs ont demandé "T'es sûre que c'est le bon compte ?"
- 0/5 utilisateurs ne font confiance immédiatement sans vérifier

**Signaux d'anxiété** :
- Hésitations longues (5-10s) avant de cliquer "Valider"
- Re-lecture multiple du récapitulatif
- Questions de confirmation ("C'est bien 50€ ?", "Marie Dupont c'est bien ça ?")

**Verbatims sur la confiance** :
> "Je sais que c'est une machine donc je vérifie bien, on sait jamais" — Marc
> "J'ai un peu peur qu'elle se trompe de compte" — Thomas

### Gestion des erreurs conversationnelles
**Reformulations spontanées** :
- Quand l'IA ne comprend pas, 4/5 utilisateurs reformulent (généralement en langage plus formel)
- 1/5 utilisateur (Marc) abandonne après 2 incompréhensions

**Attentes de continuité** :
- 5/5 utilisateurs s'attendent à ce que l'IA se souvienne du contexte de conversation
- Verbatim :
  > "Pourquoi je dois tout répéter ? Elle devrait se rappeler qu'on parle du virement à Marie" — Sophie

---

## 🎯 Recommandations priorisées

### Matrice Impact / Effort

#### 🔴 Critiques (Bloquent l'adoption)
| Recommandation | Parcours affecté | Impact | Effort | Utilisateurs impactés |
|----------------|------------------|--------|--------|-----------------------|
| Enrichir NLU avec langage quotidien (virer/envoyer, personne/ami) | Virement | 🔥🔥🔥 | ⚡⚡⚡ | 3/5 |
| Implémenter mémoire conversationnelle (session) | Tous | 🔥🔥🔥 | ⚡⚡⚡ | 5/5 |
| Ajouter récapitulatif visuel + CTA clair avant validation | Virement | 🔥🔥🔥 | ⚡ | 4/5 |

#### 🟠 Importantes (Dégradent l'expérience)
| Recommandation | Parcours affecté | Impact | Effort | Utilisateurs impactés |
|----------------|------------------|--------|--------|-----------------------|
| Réduire verbosité des réponses (consultation) | Consultation | 🔥🔥 | ⚡ | 3/5 |
| Ajouter suggestions contextuelles ("Vous pouvez aussi...") | Navigation | 🔥🔥 | ⚡⚡ | 3/5 |
| Tolérance montants arrondis (±1€) | Question débit | 🔥 | ⚡ | 2/5 |
| Proposer fallback formulaire classique pour opérations complexes | Virement | 🔥🔥 | ⚡⚡ | 4/5 |

#### 🟢 Nice-to-have (Améliorations)
| Recommandation | Parcours affecté | Impact | Effort | Utilisateurs impactés |
|----------------|------------------|--------|--------|-----------------------|
| Possibilité annulation immédiate post-validation | Virement | 🔥 | ⚡⚡ | 5/5 |
| Onboarding des commandes principales | Découverte | 🔥 | ⚡ | 3/5 |
| Ajuster ton (moins "poli robot") | Tous | 🔥 | ⚡ | 1/5 |

### Roadmap suggérée
**Sprint 1** (Blockers critiques - 2 semaines) :
- [ ] Enrichir corpus NLU avec 50+ formulations quotidiennes
- [ ] Implémenter mémoire conversationnelle (5 derniers messages minimum)
- [ ] Redesign validation : récapitulatif visuel + bouton CTA explicite

**Sprint 2** (Quick wins + importantes - 1 semaine) :
- [ ] Réduire verbosité réponses (mode "court" par défaut)
- [ ] Ajouter suggestions contextuelles
- [ ] Tolérance montants arrondis dans recherche

**Backlog** (Nice-to-have) :
- [ ] Fallback formulaire classique
- [ ] Annulation post-validation
- [ ] Onboarding interactif

---

## ✅ Hypothèses validées / ❌ Hypothèses invalidées

### Validées
| Hypothèse | Validation | Force |
|-----------|------------|-------|
| H1 : Les utilisateurs préfèrent un ton conversationnel à un ton bancaire formel | 4/5 utilisateurs apprécient le ton | ✅✅✅ |
| H2 : La consultation de solde est un use case idéal pour le conversationnel | 5/5 réussissent rapidement et facilement | ✅✅✅ |
| H3 : Les utilisateurs acceptent de "parler" à leur banque via texte | 4/5 utilisateurs à l'aise avec le concept | ✅✅ |

### Invalidées
| Hypothèse | Réalité observée | Impact |
|-----------|------------------|--------|
| H4 : Le conversationnel réduit l'anxiété financière | 5/5 utilisateurs vérifient autant (voire plus) qu'avec formulaire classique | 🔴 Revoir la promesse de valeur |
| H5 : Les utilisateurs comprennent intuitivement comment interagir avec l'IA | 3/5 bloqués par incompréhensions NLU, 3/5 ne savent pas comment découvrir les fonctionnalités | 🔴 Revoir l'onboarding + NLU |
| H6 : Le conversationnel peut remplacer le formulaire classique pour tous types de virements | 4/5 utilisateurs veulent un fallback formulaire pour virements complexes | 🟠 Positionner comme canal complémentaire |

### Nouvelles hypothèses émergentes
- **H7** : Les utilisateurs accepteraient mieux les limitations de l'IA si elles étaient explicites - Observé chez 3/5 utilisateurs qui disent "Si elle me dit qu'elle se souvient que de 5 messages, OK, mais là je sais pas"
- **H8** : Le conversationnel est idéal pour les opérations **récurrentes et simples**, pas pour les nouvelles opérations complexes - Observé chez 4/5 utilisateurs

---

## 📎 Annexes

### A. Grilles d'observation détaillées
- [2026-02-02-test-nina.md](2026-02-02-test-nina.md)
- [2026-02-02-test-marc.md](2026-02-02-test-marc.md)
- [2026-02-02-test-sophie.md](2026-02-02-test-sophie.md)
- [2026-02-02-test-thomas.md](2026-02-02-test-thomas.md)
- [2026-02-02-test-lea.md](2026-02-02-test-lea.md)

### B. Captures d'écran annotées
- `assets/nina-blocage-nlp.png` - Nina bloquée sur "virer 50€"
- `assets/marc-confusion-validation.png` - Marc ne sait pas si c'est validé
- `assets/sophie-verbeux.mp4` - Réaction de Sophie face à la réponse longue

### C. Métriques brutes
| Utilisateur | Virement (réussi) | Consultation (réussi) | Question débit (réussi) | Reformulations nécessaires |
|-------------|-------------------|----------------------|-------------------------|----------------------------|
| Nina | ✅ (3min 12s) | ✅ (42s) | ✅ (1min 05s) | 2 |
| Marc | ❌ (abandonné) | ✅ (38s) | ❌ (montant imprécis) | 4 |
| Sophie | ✅ (2min 58s) | ✅ (51s) | ✅ (1min 48s) | 1 |
| Thomas | ❌ (bloqué validation) | ✅ (1min 02s) | ✅ (1min 22s) | 3 |
| Léa | ✅ (4min 22s) | ✅ (35s) | ✅ (58s) | 2 |
