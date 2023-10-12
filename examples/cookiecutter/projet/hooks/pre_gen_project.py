import os
import sys

REMOVE_PATHS = [
    '{% if cookiecutter.prefere != "aucun" %} images {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

ADD_PATHS = [
    '{{ cookiecutter.bayesien_ou_frequentiste }}'
]

for path in ADD_PATHS:
    path = path.strip()
    os.mkdir(path)
