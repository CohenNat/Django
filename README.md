# Multilang Site

## Description
`multilang_site` est un projet Django qui prend en charge l'internationalisation (i18n) et permet de gérer des articles de blog avec des champs `title`, `content`, et `publication_date`. Le projet supporte au moins deux langues : français et anglais.

## Prérequis

- Python 3.x
- pip (Python package installer)
- Virtualenv (optionnel mais recommandé)

## Installation

1. **Cloner le dépôt :**

    ```bash
    git clone https://github.com/CohenNat/Django.git
    cd Django
    ```

2. **Configurer l'environnement virtuel :**

    ```bash
    python -m venv venv
    source venv/bin/activate # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. **Installer les dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

4. Créez le fichier `settings.py` en utilisant `settings.py.example` comme modèle et configurez vos paramètres (comme `DATABASES`, `SECRET_KEY`, etc.).

5. Appliquez les migrations :

    ```bash
    python manage.py migrate
    ```

6. Créez un superutilisateur pour accéder à l'interface d'administration :

    ```bash
    python manage.py createsuperuser
    ```

## Utilisation

1. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

2. Accédez à l'interface d'administration à `http://127.0.0.1:8000/admin/` et connectez-vous avec le superutilisateur que vous avez créé.

3. Ajoutez des articles de blog via l'interface d'administration.

4. Pour voir la liste des articles en Français de blog, accédez à `http://127.0.0.1:8000/fr/articles/`.

5. Pour voir la liste des articles en English de blog, accédez à `http://127.0.0.1:8000/en/articles/`.

6. Accédez à `http://127.0.0.1:8000/chatbot/` pour utiliser le chatbot.

7. Accédez à `http://127.0.0.1:8000/search/` pour utiliser la recherche augmentée par IA.

## Internationalisation

Le projet supporte le changement de langue entre le français et l'anglais. Pour changer la langue, utilisez les boutons de langue sur la page de liste des articles.

### Ajouter des traductions

1. Marquez les chaînes à traduire dans les templates et les fichiers Python en utilisant `{% trans %}` dans les templates et `gettext` dans les fichiers Python.

2. Créez des fichiers de traduction pour les langues supportées :

    ```bash
    django-admin makemessages -l fr
    django-admin makemessages -l en
    ```

3. Traduisez les chaînes dans les fichiers `.po` générés dans le répertoire `locale`.

4. Compilez les fichiers de traduction :

    ```bash
    django-admin compilemessages
    ```
