# Les outils essentiels pour la construction d'un projet d'apprentissage automatique

Vous retrouverez dans ce tutoriel la présentation des principaux **outils** pour le bon **développement** d'un projet incluant des modèles d'**apprentissage automatique**.

## Installer le projet et faire rouler le code

Insérer ici les directives.

## Les outils

### Cookiecutter

Ce premier outil n'est pas un indispensable dans vos études, mais il peut être essentiel et efficace dans vos projets en entreprise. \
C'est un réel compagnon qui vous permettra d'accélérer la mise en place de votre projet et la construction de l'arborescence de votre dossier contenant votre code. Vous l'aurez sûrement compris, mais c'est un outil qui vous permet de créer des *templates* de projets et ainsi d'y inclure tous les fichiers initiaux dans votre nouveau dossier de projet.

[Pour en savoir plus sur les cookiecutters](https://cookiecutter.readthedocs.io/en/stable/)

### Pyenv + Poetry

Ces deux outils vont de pairs et vous seront redoutablement utiles pour le développement. \
Du côté pyenv, l'outil vous offre la possibilité de gérer plusieurs versions python d'un coup. Autrement dit, vous pouvez installez plusieurs versions python sur votre machine. \
Quant à poetry, l'outil vous permet de gérer des environnements python. Il gère les conflits de dépendances, les versions et construit un environnement reproductible via un fichier nommé `poetry.lock`. Si vous mettez les fichiers `pyproject.toml` et `poetry.lock` dans votre dépôt *github*, tout le monde peut installer le même environnement, sans avoir de problème de version de package python.

[Pour en savoir plus sur pyenv](https://github.com/pyenv/pyenv) \
[Pour en savoir plus sur poetry](https://python-poetry.org/)

### Hydra

Hydra est le compagnon typique pour le scientifique/chercheur. Il permet de gérer les configurations tout en permettant de lancer les exécutions d'un programme Python. \
Les configurations sont basées sur une arborescence de fichiers au format *yaml*.

[Pour en savoir plus sur hydra](https://hydra.cc/)

### MLflow

Outil phare pour la gestion des expérimentations en apprentissage automatique. Grâve à une application web en local (ou déployé sur un serveur), vous aurez accès à tous vos entrainements de modèles, les méta-données et les métriques que vous avez choisi de *tracker*. De plus, il est simple de récupérer les poids du modèle que vous voulez ré-utiliser par la suite, tout en vous fiant aux informations que vous avez collecté.

[Pour en savoir plus sur MLflow](https://mlflow.org/)

### Pytorch-Lightning

À compléter 

[Pour en savoir plus sur pytorch-lightning](https://lightning.ai/docs/pytorch/stable/)

### Tensorboard

À compléter

[Pour en savoir plus sur les tensorboards](https://www.tensorflow.org/tensorboard?hl=fr)

### Data Version Control

À compléter

[Pour en savoir plus sur DVC](https://dvc.org/)

## Les bonus

### WSL 2.0

À compléter
[Pour en savoir plus sur WSL](https://learn.microsoft.com/en-us/windows/wsl/)

### Kubernetes

Je ne le présenterai pas en démo car c'est un outil très spécifique dont je n'ai pas cherché à réellement comprendre les mécanismes. Retenez qu'il vous sera (sûrement) indispensable lorsque vous travaillerez dans une entreprise. \
En effet, c'est un *framework* fort utile qui va vous permettre de lancer et de surveiller des exécutions de programmes sur un serveur distant. Son avantage est de découper et d'organiser les ressources afin de lancer vos programmes, qui plus est, les exécutions doivent être encapsulés dans un containeur docker.

[Pour en savoir plus sur Kubernetes](https://kubernetes.io/)

### .devcontainer avec Visual Studio Code

À compléter

[Pour en savoir plus sur le développement sous .devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)

### black

À compléter

[Pour en savoir plus sur Black](https://black.readthedocs.io/en/stable/)

### pylint

À compléter

[Pour en savoir plus sur pylint](https://pylint.readthedocs.io/en/latest/user_guide/installation/index.html)

### click

À compléter

[Pour en savoir plus sur click](https://click.palletsprojects.com/en/8.1.x/)