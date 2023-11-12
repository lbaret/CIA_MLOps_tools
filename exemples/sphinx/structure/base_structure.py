from typing import Tuple


class BaseStructure:
    """Défini les composantes principales d'une structure placée sur la map."""

    def __init__(
        self,
        health: int,
        damage: int,
        armor: int,
        magic_resist: int,
        make_super_minions_spawn: bool,
        end_game: bool,
        coordinates: Tuple[int, int]
    ) -> None:
        """Instanciate the structure with it's features.

        :param health: Points de vie de la structure
        :type health: int
        :param damage: Dégâts infligés par la structure (si applicable)
        :type damage: int
        :param armor: Armure de la structure
        :type armor: int
        :param magic_resist: Résistance magique de la structure
        :type magic_resist: int
        :param make_super_sbire_spawn: Indique si une fois la structure à 0 point de vie fait apparaître des super-sbires
        :type make_super_sbire_spawn: bool
        :param end_game: Indique si une fois la structure à 0 point vie met fin à la partie
        :type end_game: bool
        :param coordinates: Coordonnées de la structure sur la carte
        :type coordinates: Tuple[int, int]
        """        
        self.health = health
        self.damage = damage
        self.armor = armor
        self.magic_resist = magic_resist
        self.make_super_minions_spawn = make_super_minions_spawn
        self.end_game = end_game
        self.coordinates = coordinates
