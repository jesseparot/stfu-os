# Patterns de séquences email outbound

Patterns réutilisables pour les séquences de prospection STFU. Chaque séquence suit la structure 4 emails / 14 jours.

## Structure standard

| Email | Timing | Objectif | Ton |
|-------|--------|----------|-----|
| Email 1 | J0 | Ouvrir la conversation | Éducatif, pas vendeur |
| Email 2 | J3 | Approfondir + signal prix | Technique light |
| Email 3 | J7 | Prouver avec des chiffres | Case study |
| Email 4 | J12 | Dernier rappel, angle différent | Direct, assumé |

## Templates de hooks par type de cible

### Même secteur que la mission d'origine

Le prospect connaît déjà le problème. Aller droit au fait.

```
Hook : "{Problème sectoriel connu} — on l'a résolu pour {client ou "un acteur du secteur"} en {durée}."
Preuve : résultats quantifiés du case
Angle : "vous avez probablement le même problème"
```

**Exemple :**
> La conformité CSRD va coûter entre 50 et 200k€ par an aux ETI du retail. On a automatisé 70% du reporting pour un acteur du secteur en 6 semaines.

### Secteur adjacent (même problème, autre industrie)

Le prospect ne sait pas forcément que la solution existe dans son secteur. Éduquer d'abord.

```
Hook : "Les {secteur d'origine} ont trouvé une solution à {problème transverse}. Ça s'applique à {secteur du prospect}."
Preuve : analogie + chiffres
Angle : "le pattern est identique, on l'a déjà industrialisé"
```

**Exemple :**
> Les acteurs du luxe automatisent leur veille réglementaire avec de l'IA depuis 2025. Le même système s'applique aux ETI industrielles — mêmes contraintes, même ROI.

### Cible tech/plateforme (même stack, autre usage)

Le prospect utilise les mêmes outils. Parler leur langage technique.

```
Hook : "Vous utilisez {outil/plateforme} — on a construit {solution} dessus pour {client}."
Preuve : description technique light + résultat business
Angle : "vous avez déjà l'infra, il manque la couche IA/automatisation"
```

**Exemple :**
> Votre stack Salesforce + HubSpot peut générer automatiquement des propositions commerciales personnalisées. On l'a fait pour un éditeur SaaS — 3x plus de propales envoyées, même équipe.

## Templates de CTA

### CTA soft (email 1)

À utiliser au premier contact. Basse friction, pas d'engagement.

- "Je vous envoie un exemple concret de ce qu'on a livré ?"
- "15 min pour voir si ça s'applique à votre contexte ?"
- "Je vous partage le case study complet ?"
- "Ça vaut un échange rapide ?"

### CTA medium (email 2-3)

Le prospect a ouvert les emails précédents. Monter d'un cran.

- "On fait un call de 20 min pour voir ce que ça donnerait chez vous ?"
- "Je peux vous montrer le prototype en 15 min — ça parle mieux qu'un email."
- "Quand est-ce qu'on en discute ?"

### CTA direct (email 4)

Dernier email. Être direct, assumer.

- "Dernier message sur le sujet. Si {problème} n'est pas une priorité, pas de souci. Sinon, un call cette semaine ?"
- "Je ne vais pas relancer. Si le sujet vous parle, répondez à cet email et on cale un créneau."
- "Si ce n'est pas le moment, je comprends. Mon calendrier est ouvert si ça le devient : {lien}"

## Règles de signal prix

Le signal prix apparaît dans l'email 2 ou 3. Jamais l'email 1 (trop tôt) ni l'email 4 (trop tard).

**Formats recommandés :**
- Ordre de grandeur : "Projets de l'ordre de X à Y€"
- Fourchette : "À partir de X€ pour {périmètre minimal}"
- Par rapport au coût du problème : "Un investissement de X€ vs. un coût actuel de Y€/an"
- Comparaison : "3 à 5x moins cher qu'un développement interne"

**Ne jamais faire :**
- Prix exact dans un email froid (réservé au call)
- Prix sans contexte (toujours lier au périmètre ou au résultat)
- Prix sans ancrage (toujours comparer à quelque chose : coût actuel, alternative, ROI)

## Patterns A/B testing

### Variante A — Résultat business

L'email est centré sur ce que le prospect **gagne**. Le "comment" est secondaire.

```
Structure :
1. Problème du prospect (douleur)
2. Résultat obtenu ailleurs (chiffres)
3. Ce que ça changerait pour lui
4. CTA
```

Mots-clés : résultat, gain, économie, temps, ROI, impact, transformation

### Variante B — Réplication capability

L'email est centré sur ce qu'on a **construit**. La preuve technique crée la crédibilité.

```
Structure :
1. Ce qu'on a construit (description concrète)
2. Pour qui et dans quel contexte
3. Pourquoi c'est réplicable chez le prospect
4. CTA
```

Mots-clés : on a construit, prototype, système, automatisé, déployé, stack, livré

### Quand utiliser quelle variante

| Contexte | Variante recommandée |
|----------|---------------------|
| Prospect C-level / décideur business | A (résultat business) |
| Prospect technique / product / ops | B (capability) |
| Secteur très concurrentiel | A (différenciation par le résultat) |
| Secteur peu mature sur le sujet | B (éducation par la preuve technique) |
| Budget serré / sensibilité prix | A (focus ROI) |
| Innovation / early adopter | B (focus nouveauté technique) |

## Règles de rédaction

- **Objet court** : max 6-8 mots, pas de majuscule sauf début de phrase
- **Pas de "Bonjour {prénom},"** en cold email — aller directement au sujet ou commencer par une phrase d'accroche
- **Max 100 mots par email** : si c'est plus long, couper
- **1 seul CTA par email** : pas de choix, une seule action demandée
- **Pas de pièce jointe** en email 1 : proposer d'envoyer, pas envoyer directement
- **Personnalisation** : au minimum {prénom}, {entreprise}, {secteur}. Idéalement une référence à un signal spécifique (recrutement, levée, lancement produit, contrainte réglementaire)
- **Signature simple** : Prénom, rôle, STFU, lien calendrier. Pas de pavé corporate.
