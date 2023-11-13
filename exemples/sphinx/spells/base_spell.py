from abc import abstractmethod
from typing import Any, List


class BaseSpell:
    """Classe modélisant la base du comportement d'un sort."""

    def __init__(
        self,
        damages: List[int],
        damage_type: List[str],
        *,
        stun: bool,
        blind: bool,
        bump: bool,
    ) -> None:
        """Instanciation de la classe parent représentant un sort.

        :param damages: Les dégats de base du sort.
        :type damages: List[int]
        :param damage_type: Les éléments des dégâts appliqués de de chacun du sort
        :type damage_type: List[str]
        :param stun: Indique si le sort a un effet paralysant
        :type stun: bool
        :param blind: indique si le sort aveugle le champion
        :type blind: bool
        :param bump: indique si le sort propulse un champion dans les airs
        :type bump: bool
        """
        self.damages = damages
        self.damage_type = damage_type
        self.stun = stun
        self.blind = blind
        self.bump = bump

    def __call__(self, hitted: List[Any]) -> None:
        """Voir la méthode apply().

        :param champion: listes d'instances d'objets atteints par le sort
        :type champion: List[Any]
        """
        self.apply(hitted)

    @abstractmethod
    def apply(self, hitted: List[Any]) -> None:
        """Applique les effets aux objets atteints par le sort.

        :param champion: listes d'instances d'objets atteints par le sort
        :type champion: List[Any]
        :raises NotImplementedError: Méthode abstraite qui doit être implémentée par une classe enfant
        """
        raise NotImplementedError("This method must be implemented by a child class")

    def apply_damages(self, hitted: List[Any]) -> None:
        """Applique les dégâts aux objets atteints par le sort.

        :param champion: listes d'instances d'objets atteints par le sort
        :type champion: List[Any]
        :raises NotImplementedError: Méthode abstraite qui doit être implémentée par une classe enfant
        """
        raise NotImplementedError("This method must be implemented by a child class")

    def apply_state(self, hitted: List[Any]) -> None:
        """Applique les effets de contrôle aux objets atteints par le sort.

        :param champion: listes d'instances d'objets atteints par le sort
        :type champion: List[BaseChampion]
        :raises NotImplementedError: Méthode abstraite qui doit être implémentée par une classe enfant
        """
        raise NotImplementedError("This method must be implemented by a child class")
