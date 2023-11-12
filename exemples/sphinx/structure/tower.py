from typing import Tuple
from .base_structure import BaseStructure


class Tower(BaseStructure):
    """Classe enfant de la structure représentant la tour d'une équipe.

    :param BaseStructure: Informations principales de la structure
    :type BaseStructure: _type_
    """
    def __init__(
        self,
        health: int,
        damage: int,
        armor: int,
        magic_resist: int,
        coordinates: Tuple[int, int],
    ) -> None:
        """Instancie la classe du tour.

        :param health: Points de vie de la tour
        :type health: int
        :param damage: Dégâts infligés par la tour
        :type damage: int
        :param armor: Armure de la tour
        :type armor: int
        :param magic_resist: Résistance magique de la tour
        :type magic_resist: int
        :param coordinates: Coordonnées de la tour sur la carte
        :type coordinates: Tuple[int, int]
        """
        super().__init__(
            health=health,
            damage=damage,
            armor=armor,
            magic_resist=magic_resist,
            make_super_minions_spawn=False,
            end_game=False,
            coordinates=coordinates,
        )
