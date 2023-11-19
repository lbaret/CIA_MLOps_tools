from typing import List

from .champions.base_champion import BaseChampion
from .structures.inhibitor import Inhibitor
from .structures.nexus import Nexus
from .structures.tower import Tower

def function_test(
    towers: List[Tower]
) -> float:
    """Test de la fonction

    :param towers: _description_
    :type towers: List[Tower]
    :return: _description_
    :rtype: float
    """


def load_map(
    towers: List[Tower], inhibitors: List[Inhibitor], nexus: List[Nexus]
) -> None:
    """Charge les éléments présents sur la carte.

    :param towers: Les tours présentes sur la carte
    :type towers: List[Tower]
    :param inhibitors: Les inhibiteurs présents sur la carte
    :type inhibitors: List[Inhibitor]
    :param nexus: Les deux nexus de chacune des équipes.
    :type nexus: List[Nexus]
    """
    pass


def load_champions(blue_team: List[BaseChampion], red_team: List[BaseChampion]) -> None:
    """Charge les champions choisis par les joueurs.

    :param blue_team: Les champions séléctionnés par l'équipe du côté bleu (gauche de la map)
    :type blue_team: List[BaseChampion]
    :param red_team: Les champions séléctionnés par l'équipe du côté rouge (droite de la map)
    :type red_team: List[BaseChampion]
    """
    pass
