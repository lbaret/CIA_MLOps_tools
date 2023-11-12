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

Pytorch Lightning est un framework qui va encapsuler vos modèles dans des LightningModule, vous offrant un composant de base pour pouvoir entrainer optimalement vos modèles, comme on pourrait le faire via un simple appel à la méthode `fit()` comme pour `scikit-learn` et `tensorflow`.

Le framework est très permissif et vous permet de gérer tous les comportements de votre boucle d'entrainement, sans que vous aillez à l'implémenter entièrement. De plus, il vous permet de logger vos métriques durant les exécutions, que ce soit en entrainement, en validation ou en test. Il enregistre vos poids selon vos directives (seulement garder la meilleure itération en validation ou bien conserver uniquement le modèle en dernière époque, etc...). Les données enregistrées sont facilements accessibles avec le `Tensorboard` offert par `tensorflow`. Vous pouvez également très simplement coupler `MLflow` et `Pytorch-Lightning` afin de faire un suivi optimal de vos expérimentations.

[Pour en savoir plus sur pytorch-lightning](https://lightning.ai/docs/pytorch/stable/)

### Tensorboard

Le `tensorboard` est un excellent outil si vous avez besoin de visualiser rapmidement et efficaceent vos données, que ce soit des embeddings, des images, des simples graphiques, des histogrammes, etc... Pour la visualisation, `tensorboard` vous offre des options afin de lisser vos graphes ou simplement de les peaufiner.

[Pour en savoir plus sur les tensorboards](https://www.tensorflow.org/tensorboard?hl=fr)

### Data Version Control

On parle souvent de la gestion des versions d'un code. Or, dans le cas du MLOps, il peut être également essentiel de devoir sauvegarder les divers versions de vos données. Git pourrait être une option, mais ce ne serait pas l'idéal car un dépôt est limité en taille et enregistre toutes les données de façon binaire.

Imaginez vous réalisez plusieurs expérimentations durant votre projet, mais qu'au fil du temps vous retravaillez votre traitement de données afin de créer de nouveaux modèles. Il vous faudra sûrement garder en mémoire les versions ultérieures de votre jeu de données afin de pouvoir efficacement récupérer et refaire tourner de nouvelles expérimentations afin de procéder à des comparaisons. Cela peut vous sauver la mise lors de vos travaux de recherche.

[Pour en savoir plus sur DVC](https://dvc.org/)

### Docstring et Sphinx

Pour commencer, docstring est une façon de documenter ses fonctions/méthodes directement dans le code entre les triples chevrons """docstring""". Cela permet aux développeurs d'indiquer quels sont les informations à savoir sur les arguments (type, valeurs, exemples, etc...), et les valeurs en sortie. Coupler docstring avec la librairie sphinx permet de générer automatiquement et rapidement une documentation en format HTML sans trop se casser la tête. Ces pages HTML peuvent ensuite être publiés en ligne simplement (exemple en lien github.io).
[Pour en savoir plus sur sphinx](https://www.sphinx-doc.org/en/master/index.html)

## Les bonus

### WSL 2.0

Pour de quelconques raisons, vous pourriez avoir envie de passer sous Linux, mais vous ne voulez ou ne pouvez pas vous défaire de Windows, notamment pour le *gaming* ou car votre projet/entreprise vous contraint à son utilisation. Vous seriez tenter d'installer une machine virtuelle et d'y coller Linux dedans ou de simplement configurer un *dual boot*. Or si je vous parle de Windows Subsystem for Linux vous pourriez avoir la l'une des meilleures alternatives selon votre besoin !

WSL est un sous-système qui va être intégré à votre environement Windows, ainsi Windows va partager les ressources efficacement pour pouvoir faire rouler votre Linux. Vous pouvez alors jouer dans Linux comme si l'aviez réellement installé sur votre machine, sans avoir la contrainte de lancer une machine virtuelle ou de redémarrer votre ordinateur pour pouvoir y accéder.

Ainsi, à l'aide d'un IDE tel que VS Code ou PyCharm, vous serez en mesure de développer comme si vous étiez sur Windows mais en travaillant dans votre sous-système ! Je le conseille vivement dans le cas où les outils comme `pyenv` et `poetry` sont conçus pour fonctionner nativement sur Linux.

[Pour en savoir plus sur WSL](https://learn.microsoft.com/en-us/windows/wsl/)

### Kubernetes

Je ne le présenterai pas en démo car c'est un outil très spécifique dont je n'ai pas cherché à réellement comprendre les mécanismes. Retenez qu'il vous sera (sûrement) indispensable lorsque vous travaillerez dans une entreprise. \
En effet, c'est un *framework* fort utile qui va vous permettre de lancer et de surveiller des exécutions de programmes sur un serveur distant. Son avantage est de découper et d'organiser les ressources afin de lancer vos programmes, qui plus est, les exécutions doivent être encapsulées dans un containeur docker.

[Pour en savoir plus sur Kubernetes](https://kubernetes.io/)

### Docker et les .devcontainer avec Visual Studio Code

Les *containers* de Docker sont un indispensable du développement ! C'est un outil avec lequel il est préférable de se familiariser. Que vous voulez travailler dans la recherche ou dans l'ingénierie, il vous donne la chance d'avoir un environnement reproductible à 100% car il construit à l'aide d'une image un environnement de développement que vous pouvez contrôler. L'image en question peut être n'importe quel système d'exploitation (Windows, Ubuntu, Debian, Kali, etc...), dont des versions allégées pour n'installer que ce dont vous avez besoin !

Le `devcontainer` proposé par VS Code vous permet de développer depuis votre IDE (VS Code oblige) dans un container, ainsi, fini les problèmes de packages ou de versions non compatibles ! Couplez cela avec `pyenv` et `poetry` et vous êtes équipé(e)s pour développer et livrer votre code sans vous inquiéter !

[Pour en savoir plus sur Docker](https://www.docker.com/)
[Pour en savoir plus sur le développement sous .devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)

### black

[Deprecated -> ruff](#ruff)

Outil développé en Python pour pouvoir vérifier le formatage mais également formater automatiquement le code.

[Pour en savoir plus sur Black](https://black.readthedocs.io/en/stable/)

### pylint

[Deprecated -> ruff](#ruff)

Pylint est un analyseur de code, comme `Black` c'est un outil qui peut vous faire gagner du temps, car sans avoir besoin d'exécuter le code il peut rapidement évaluer le flux dans votre code et cibler des erreurs avant que vous ne l'exécutiez.

[Pour en savoir plus sur pylint](https://pylint.readthedocs.io/en/latest/user_guide/installation/index.html)

### click

Click est une alternative plus évoluée et plus simple d'usage que `argparse` pour gérer les exécutions de programme Python. Mais dans notre cas, nous nous focaliserons sur `hydra` qui est spécifiquement adapté aux usages du scientifique et du chercheur en apprentissage automatique.

[Pour en savoir plus sur click](https://click.palletsprojects.com/en/8.1.x/)

### Ruff

Ruff est un outil optimisé pour le linting et le code formatting, c'est un tout-en-un. Cela vous évite d'utiliser plusieurs outils différents comme pylint, flake8 ou autoflake pour le linting et Black ou mypy pour le formatting de code.

[Pour en savoir plus sur ruff](https://docs.astral.sh/ruff/)

### Security

Chercher le package pour trouver les CVEs (ou vulnérabilités), autrement dit les problèmes de sécurité que peuvent induire l'utilisation des packages mis en cause. Très pratique lorsque vous travaillez en mode CI/CD.

[Pour en savoir plus sur safety](https://github.com/pyupio/safety)
