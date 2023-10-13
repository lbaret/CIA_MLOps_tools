# {{ cookiecutter.nom_projet }}

Aujourd'hui {{ cookiecutter.auteur }} a décidé de vous présenter un tutoriel sur les outils qui vont vous rendre plus efficace en entreprise.  


{%- if cookiecutter.prefere == "chat" -%}

## Voici un petit chat

![Le chaton](images/chat.jpg)

{%- elif cookiecutter.prefere == "chien" -%}

## Voici un chien

![Le chien](images/chien.jpg)

{%- elif cookiecutter.prefere == "justin bieber" -%}

## Le p'tit canadien tannant

![Le beau gosse](images/justin_bieber.jpg)

{%- elif cookiecutter.prefere == "aucun" -%}

## VOID

.

{% endif %}
