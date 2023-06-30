# Password Generator

Ce projet est un générateur de mots de passe basé sur différentes variations de mots et d'informations de date. Le générateur utilise plusieurs concepts de programmation orientée objet pour organiser le code et faciliter la maintenance et l'extension.

## Utilisation du polymorphisme

Lien dans le code : [PasswordGenerator](https://github.com/SP4RT49/passwordGuesser/blob/main/passwordGuesser.py)

Définition : Le polymorphisme est la capacité d'un objet à prendre différentes formes et à se comporter de manière différente en fonction du contexte. Dans ce projet, le polymorphisme est utilisé pour générer différentes variations de mots en fonction des options sélectionnées par l'utilisateur.

## Utilisation de l'encapsulation

Lien dans le code : [PasswordGenerator](https://github.com/SP4RT49/passwordGuesser/blob/main/passwordGuesser.py)

Définition : L'encapsulation est le mécanisme qui permet de regrouper les données et les méthodes connexes en une seule entité, appelée classe. Dans ce projet, l'encapsulation est utilisée pour encapsuler les fonctionnalités de génération de mots de passe dans la classe `PasswordGenerator`.

## Utilisation de la composition

Lien dans le code : [CustomPasswordGenerator](https://github.com/SP4RT49/passwordGuesser/blob/main/passwordGuesser.py)

Définition : La composition est un mécanisme qui permet de combiner plusieurs objets pour former un nouvel objet. Dans ce projet, la composition est utilisée pour créer une instance de `PasswordGenerator` en utilisant un objet `DynamicFields` contenant des mots et des dates dynamiques. Cela permet de personnaliser le générateur de mots de passe en fonction des champs ajoutés par l'utilisateur.

## Utilisation de l'héritage

Lien dans le code : [CustomPasswordGenerator](https://github.com/SP4RT49/passwordGuesser/blob/main/passwordGuesser.py)

Définition : L'héritage est un mécanisme de la programmation orientée objet qui permet à une classe d'hériter des attributs et des méthodes d'une autre classe. Dans ce projet, la classe `CustomPasswordGenerator` hérite de la classe de base `PasswordGenerator` pour ajouter des fonctionnalités supplémentaires spécifiques à la génération de mots de passe personnalisés.

## Utilisation d'interface

Lien dans le code : N/A

Définition : Une interface est un ensemble de méthodes abstraites définies dans une classe ou un objet. Elle définit le contrat que chaque classe ou objet implémentant l'interface doit respecter. Dans ce projet, aucune interface spécifique n'est utilisée.

## Utilisation de méthodes et attributs d'objets

Lien dans le code : [PasswordGenerator](https://github.com/SP4RT49/passwordGuesser/blob/main/passwordGuesser.py)

Définition : Les méthodes sont des fonctions définies à l'intérieur d'une classe qui agissent sur les objets de cette classe. Les attributs sont des variables liées à un objet spécifique. Dans ce projet, différentes méthodes sont définies dans la classe `PasswordGenerator` pour générer des mots de passe et effectuer des opérations sur les mots et les dates. Les attributs tels que `options`, `passwords`, `words` et `dates` sont utilisés pour stocker les données nécessaires au processus de génération de mots de passe.

## Utilisation de méthodes et attributs statiques

Lien dans le code : N/A

Définition : Les méthodes et attributs statiques appartiennent à une classe plutôt qu'à une instance spécifique de la classe. Ils peuvent être appelés sur la classe elle-même, plutôt que sur une instance de la classe. Dans ce projet, aucune méthode ou attribut statique n'est utilisé.

## Utilisation de méthodes et attributs de classe

Lien dans le code : N/A

Définition : Les méthodes et attributs de classe sont associés à la classe elle-même plutôt qu'à une instance spécifique de la classe. Ils peuvent être appelés sur la classe et partagés par toutes les instances de la classe. Dans ce projet, aucune méthode ou attribut de classe n'est utilisé.
