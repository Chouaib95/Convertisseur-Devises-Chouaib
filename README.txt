Convertisseur de Devises
Ce script Python utilise la bibliothèque PySide6 pour créer une application graphique de conversion de devises. L'application utilise le module currency_converter pour effectuer les conversions entre différentes devises.

Fonctionnalités :
Interface Graphique Intuitive : L'application offre une interface utilisateur conviviale avec des composants tels que des menus déroulants pour la sélection des devises, des zones de saisie pour les montants, et un bouton pour inverser les devises.

Conversion en Temps Réel : Les conversions sont effectuées en temps réel dès que l'utilisateur modifie les paramètres de conversion, fournissant ainsi des résultats instantanés.

Gestion des Erreurs : En cas de données non disponibles pour la conversion, l'application affiche un message d'erreur pour informer l'utilisateur.

Personnalisation du Style : L'interface graphique est stylisée avec une feuille de style CSS, offrant un aspect moderne et attrayant.

Utilisation
Sélection des Devises : Choisissez les devises de départ et d'arrivée dans les menus déroulants correspondants.

Saisie du Montant : Entrez le montant que vous souhaitez convertir dans la zone de saisie.

Inversion des Devises : Utilisez le bouton "Inverser devises" pour échanger les devises de départ et d'arrivée.

Résultats en Temps Réel : Les résultats de la conversion sont affichés instantanément, avec une précision de deux chiffres après la virgule.

Prérequis
Assurez-vous d'avoir Python installé sur votre système. Vous pouvez également utiliser un environnement virtuel pour isoler les dépendances.

bash
Copy code
pip install PySide6 currency_converter
Exécution
Exécutez le script en utilisant la commande suivante :

bash
Copy code
python votre_script.py
Personnalisation du Style
L'interface graphique est stylisée avec une feuille de style CSS. Vous pouvez personnaliser les couleurs et les styles en modifiant la méthode setup_css dans le script.

Auteur
C.EDDARBALI

Note : Assurez-vous de respecter les licences des bibliothèques utilisées et d'inclure toute attribution nécessaire dans votre projet.
