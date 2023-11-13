from typing import Tuple
from .base_structure import BaseStructure


class Nexus(BaseStructure):
    """Classe enfant de la structure représentant le Nexus d'une équipe.

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
        """Instancie la classe du Nexus.

        :param health: Points de vie du Nexus
        :type health: int
        :param armor: Armure du Nexus
        :type armor: int
        :param magic_resist: Résistance magique du Nexus
        :type magic_resist: int
        :param coordinates: Coordonnées du Nexus sur la carte
        :type coordinates: Tuple[int, int]
        """
        super().__init__(
            health=health,
            damage=0,
            armor=armor,
            magic_resist=magic_resist,
            make_super_minions_spawn=False,
            end_game=True,
            coordinates=coordinates,
        )
