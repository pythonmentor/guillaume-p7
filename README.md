# GrandPy bot
Ce site met en scène **GrandPy bot**, un robot, qui répond aux questions de l'utilisateur.
Il renseigne ce dernier sur des lieux, en lui donnant des informations tirées de wikipédia ainsi qu'une carte googlemaps.

 ## Description
 Dans le cadre du projet, le programme utilise ces différents langages:

 1. **Python**
 Python 3.6 est utilisé pour le parser. Le parser sert à normaliser la question, extraire le ou les mots importants.
 Ces mots serviront à faire des recherches googlemaps et wikipedia.

 2. **Test Driven Developpement**
 Tout au long de sa conception, les tests unitaires ont permis de répondre avec justesse au besoin du projet.
**Pytest et pylint sont des objets de développement. Ils ne sont pas utilisables dans le produit final**

 3. **html5 css3**
 Le projet est écrit en html5, css3. Ces versions de langages sont les plus récentes aujourd'hui.

 4. **Flask**
 Le framework de ce site est Flask, un framework léger.

 5. **Heroku**
 Du coté serveur, le paas (plateform as a server) est heroku.
 Le serveur en lui même est gunicorn.

 ## Installation
Simplement cloner le repository sur votre machine.
Installer pipenv (si ça n'est pas déja fait).

Vous pouvez faire les tests unitaires comme ceci:
* pipenv shell (dans votre console, pour activer l'environnement virtuel).
* pytest -v 

Pour lancer le site en local:
Créer un fichier .env définissant les variables d'environnement BACKEND_KEY et FRONT_KEY avec des clés googlemaps.
* python3 -m webapp.routes (dans l'environnement virtuel).

## librairie
Les informations concernant le back-end se trouvent dans le dossier **robot**.
Les informations liées au front-end se trouvent dans le dossier **webapp**.
Les tests unitaires se trouvent dans le dossier **tests**.

## informations diverses
Lors de l'installation de pipenv, il faut spécifier que le projet est versionné en python 3.x, comme ceci:
* pipenv --python 3.x (x étant la version installée sur votre poste de travail)
