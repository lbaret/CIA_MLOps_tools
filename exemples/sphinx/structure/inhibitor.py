from typing import Tuple
from .base_structure import BaseStructure


class Inhibitor(BaseStructure):
    """Classe enfant de la structure représentant l'inhibiteur d'une équipe.

    :param BaseStructure: Informations principales de la structure
    :type BaseStructure: _type_
    """
    def __init__(
        self,
        health: int,
        armor: int,
        magic_resist: int,
        coordinates: Tuple[int, int],
    ) -> None:
        """Instancie la classe de l'inhibiteur.

        :param health: Points de vie de l'inhibiteur
        :type health: int
        :param armor: Armure de l'inhibiteur
        :type armor: int
        :param magic_resist: Résistance magique de l'inhibiteur
        :type magic_resist: int
        :param coordinates: Coordonnées de l'inhibiteur sur la carte
        :type coordinates: Tuple[int, int]
        """
        super().__init__(
            health=health,
            damage=0,
            armor=armor,
            magic_resist=magic_resist,
            make_super_minions_spawn=True,
            end_game=False,
            coordinates=coordinates,
        )