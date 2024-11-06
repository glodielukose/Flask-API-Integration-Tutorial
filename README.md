# Flask-API-Integration-Tutorial

**Description:**

Ce repository contient un tutoriel détaillé sur l'utilisation des données d'une API externe avec une application Flask. Vous y trouverez les étapes nécessaires pour configurer votre environnement, effectuer des requêtes à une API externe, traiter les données reçues et les intégrer dans votre application Flask.

**Contenu:**
- [Flask-API-Integration-Tutorial](#flask-api-integration-tutorial)
  - [Introduction à Flask](#introduction-à-flask)
  - [Configuration de l'environnement](#configuration-de-lenvironnement)
  - [Requêtes à une API externe](#requêtes-à-une-api-externe)
    - [Introduction à l'API OpenWeatherMap](#introduction-à-lapi-openweathermap)
    - [Créer un compte OpenWeatherMap](#créer-un-compte-openweathermap)
      - [Étape 1 :](#étape-1-)
      - [Étape 2 :](#étape-2-)
      - [Étape 3 :](#étape-3-)
      - [Étape 4 :](#étape-4-)
      - [Étape 5 :](#étape-5-)
      - [Étape 6 :](#étape-6-)
    - [Analyser les fichiers JSON avec Python](#analyser-les-fichiers-json-avec-python)
      - [Introduction au JSON](#introduction-au-json)
      - [Extraire les informations de l'URL](#extraire-les-informations-de-lurl)
  - [Affichage des données dans l'application](#affichage-des-données-dans-lapplication)
    - [Étape 1](#étape-1)
    - [Étape 2](#étape-2)
    - [Étape 3](#étape-3)
  - [Aller Plus loin](#aller-plus-loin)

**Prérequis:**
- Connaissances de base en Python
- Environnement de développement configuré

## Introduction à Flask
Flask est un micro-framework web en Python qui permet de développer des applications web de manière rapide et flexible. Il est conçu pour être léger et minimaliste, offrant les fonctionnalités essentielles pour créer des applications, comme le routage d'URL et la gestion des requêtes, tout en permettant aux développeurs de choisir leurs propres outils et bibliothèques pour des fonctionnalités avancées. Flask utilise le langage Python et est apprécié pour sa simplicité et sa modularité, ce qui le rend particulièrement adapté aux projets de petite à moyenne échelle ou aux prototypes.

## Configuration de l'environnement
Pour commencer, nous allons devoir initialiser le projet sur notre machine et configurer notre environnement. Pour ce faire, je vous invite à suivre les étapes suivantes :

1. Création du dossier qui va contenir notre application Flask :
   ```bash
   mkdir Flask-API-Integration-Tutorial
   ```
2. Initialisation d'un environnement virtuel Python :
   ```bash
   python -m venv venv
   ```

   Pour ensuite activer l'environnement virtuel, il faut taper la commande suivante :
   ```bash
   source venv/bin/activate
   ```

   Une fois que l'environnement virtuel a été configuré, nous allons pouvoir installer les différentes dépendances de notre projet.

3. Installation des différentes dépendances et librairies :
   Premièrement, nous aurons à installer notre dépendance principale, dans notre cas il s'agit de Flask :
   ```bash 
   pip install flask
   ```

4. Vérification des différentes fonctionnalités :
   Nous allons créer un fichier `app.py` dans lequel nous allons mettre le contenu suivant :
   ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def index():
      return "Hello World !"
   ```

   * `from flask import Flask` : Cette ligne permet d'importer `Flask`, qui est une instance contenue dans Flask, permettant de créer une instance de Flask qui gère les routes et les requêtes web.
   * `app = Flask(__name__)` : On initialise `app` comme étant une instance de Flask. `Flask(__name__)` permet à l'application de se repérer dans le dossier de notre projet.
   * `@app.route("/")` : Ce décorateur indique à Flask quelle fonction il doit appeler lorsque la route `/` est activée.

   Ensuite, pour vérifier si tout fonctionne correctement, le mieux serait de tester avec la commande suivante :
   ```bash
   flask run
   ```

## Requêtes à une API externe
### Introduction à l'API OpenWeatherMap
Il y a très peu d'APIs qui sont disponibles gratuitement, mais heureusement pour nous, il y a une API qui nous propose un plan gratuit : il s'agit de l'`OpenWeatherMap API`. Cette API nous permet d'avoir accès à des données météo de certaines régions de notre planète, et c'est celle-ci que nous allons utiliser pour notre exemple.

Malgré le fait qu'elle soit gratuite, cette API a quelques restrictions :
* Elle ne permet que 60 appels API par minute et 5000 par jour dans son plan gratuit.
* Pour l'utiliser, il va nécessairement falloir créer un compte sur leur site web.
  
### Créer un compte OpenWeatherMap
Pour créer un compte, il va d'abord falloir se rendre sur le site web de OpenWeatherMap, qui se trouve à l'adresse suivante : [https://openweathermap.org/](https://openweathermap.org/).

#### Étape 1 :
Une fois que vous êtes sur le site, cela devrait se présenter comme ceci. Ensuite, cliquez sur le bouton `Sign In`.

<img src='./assets/etape1.png' alt='première étape' width='820'>

#### Étape 2 :
Ensuite, vous devriez être redirigé sur une page qui ressemble un peu à ça. Si vous avez déjà un compte, vous n'avez qu'à remplir vos identifiants dans le formulaire. Sinon, cliquez sur le bouton `Create an Account` pour créer un nouveau compte.

<img src='./assets/etape2.png' alt='deuxième étape' width='820'>

#### Étape 3 :
Si vous avez cliqué sur ce bouton, vous tomberez sur cette page. Il faut ensuite remplir ce formulaire pour créer un nouveau compte :

<img src='./assets/etape3.png' alt='troisième étape' width='820'>

#### Étape 4 :
Une fois que vous vous êtes connecté ou que vous avez terminé tout ce qui concerne l'inscription, vous devriez être redirigé vers cette page. Pour avoir accès aux données d'une API, nous avons besoin d'une clé, et c'est grâce à cette clé que l'on peut accéder aux données servies par cette API. Pour obtenir votre clé, il faut cliquer sur le bouton `API Key`.

<img src='./assets/etape4.png' alt='quatrième étape' width='820'>

#### Étape 5 :
Copiez cette clé API, nous en aurons besoin pour la suite.

<img src='./assets/etape5.png' alt='cinquième étape' width='820'>

#### Étape 6 :
Essayez de taper l'URL suivante `http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid=<API Key>` dans la barre de recherche de votre navigateur, en remplaçant `<API Key>` par votre clé API. Vous devriez normalement obtenir le résultat suivant :

<div style="display:flex; max-width:100%;">
  <img src='./assets/etape6-1.png' alt='cinquième étape' width='50%'>
  <img src='./assets/etape6-2.png' alt='cinquième étape' width='50%'>
</div>

### Analyser les fichiers JSON avec Python
Nous avons maintenant la possibilité d'accéder aux données via le protocole HTTP via l'URL d'une API. Maintenant, le mieux serait de pouvoir utiliser ces données dans du code Python pour notre application.

#### Introduction au JSON
Le JSON est une structure de données qui ressemble beaucoup au dictionnaire Python, même s'il peut y avoir des petites différences. Cela nous facilitera encore plus l'utilisation si nous sommes déjà à l'aise avec les dictionnaires Python. Python met à notre disposition quelques librairies pour extraire du JSON à partir d'une URL :
* `urllib` : Cette librairie va nous permettre de télécharger les données contenues dans l'URL.
* `JSON` : C'est une autre librairie Python qui nous permet de parser les données pour pouvoir ensuite les utiliser comme un dictionnaire Python.

#### Extraire les informations de l'URL
Pour commencer, nous allons d'abord devoir importer nos librairies :
```python
import json
import urllib
```

Ensuite, créez la fonction qui va nous permettre de gérer la récupération des données :
```python
def get_weather(query):
  api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=<API Key>"
  query = urllib.parse.quote(query)
  url = api_url.format(query)
  data = urllib.request.urlopen(url).read()
  parsed = json.loads(data)
  weather = None
  
  if parsed['weather']:
    weather = {
      'description': parsed['weather'][0]['description'],
      'temperature': parsed['main']['temp'],
      'city': parsed['name'],
      'country': parsed['sys']['country']
    }
  
  return weather
```
N'oubliez surtout pas de remplacer `<API Key>` par votre clé API.

## Affichage des données dans l'application

Maintenant que nous sommes capables de récupérer les données de l'API sous forme de dictionnaire Python, nous devrions pouvoir les afficher dans une page web HTML. Pour cela, nous allons utiliser le moteur de template Jinja. Ce moteur, directement intégré dans Flask, nous permet d'afficher des données dynamiques sur une page web.

Jinja est déjà intégré dans Flask, donc nous n'avons pas besoin de l'installer dans notre environnement. Les étapes suivantes vous montreront comment utiliser Jinja pour notre projet.

### Étape 1
Pour commencer, créez un dossier dans notre projet nommé `templates`, puis, dans ce dossier, créez un fichier `.html` nommé `home.html` qui contiendra le code suivant :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Weather</title>
</head>
<body>
  
</body>
</html>
```

**NB** : Il est important que le dossier contenant nos fichiers `.html` s'appelle `templates` pour qu'il soit reconnu par Jinja.

### Étape 2
Ensuite, nous devons faire en sorte qu'à chaque lancement du serveur, notre page web soit affichée. Rendez-vous dans le fichier `app.py` et importez une fonction de Flask qui nous permettra de le faire :

```python
from flask import Flask, render_template
```

Modifiez ensuite la fonction `index` pour qu'elle renvoie notre page HTML :

```python
def index():
  return render_template("home.html")
```

Une fois le serveur lancé, vous devriez obtenir le résultat suivant :
<img src='./assets/resultat1.png' alt='quatrième étape' width='820'>

Ceci étant fait, notre objectif reste tout de même de pouvoir visualiser nos données sur notre page. Pour cela, passons à la dernière étape :

### Étape 3
Pour que nos données soient accessibles sur notre page, nous devons les passer comme arguments à la fonction `render_template` :

```python
def index():
  return render_template(
    "home.html",
    weather=get_weather("London,Uk")
    )
```

Nous pourrons alors accéder à nos données sur notre page web. Il ne reste plus qu'à bien les organiser :

```html
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Weather</title>
</head>
<body>
  <h1>Headlines</h1>
  <h2>Current Weather</h2>
  <p>
    City : 
    <b>{{ weather.city }} | {{ weather.country }}</b>
  </p>
  <p>{{ weather.description }} | {{ weather.temperature }}&#8451;</p>
</body>
</html>
```

Si vous redémarrez le serveur, votre page web devrait ressembler à ceci :
<img src='./assets/resultat2.png' alt='quatrième étape' width='820'>

## Aller Plus loin

Pour aller plus loin, vous pouvez permettre aux utilisateurs de rechercher une ville spécifique :

Dans `app.py` :
```python
from flask import Flask, render_template, request
```

Dans `home.html` :
```html
<form>
  <input type="text" name="city" id="city" placeholder="search">
  <input type="submit" value="Submit">
</form>
```

Dans `app.py` :
```python
def index():
  city = request.args.get('city')
  if not city:
    city = "London,Uk"

  return render_template(
    "home.html",
    weather=get_weather(city)
    )
```