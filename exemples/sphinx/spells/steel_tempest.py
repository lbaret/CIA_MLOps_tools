from typing import Any, List

from .base_spell import BaseSpell


class SteelTempest(BaseSpell):
    """Sort tempête d'acier (Q spell) de Yasuo."""

    def __init__(
        self,
        damages: List[int],
        damage_type: List[str],
        *,
        stun: bool,
        blind: bool,
        bump: bool,
    ) -> None:
        """Instancie la classe du sort tempête d'acier de Yasuo.

        :param damages: Les valeurs des dégâts infligés par le sort.
        :type damages: List[int]
        :param damage_type: Les types des dégâts infligés par le sort.
        :type damage_type: List[str]
        :param stun: Indique si le sort a un effet paralysant
        :type stun: bool
        :param blind: indique si le sort aveugle le champion
        :type blind: bool
        :param bump: indique si le sort propulse un champion dans les airs
        :type bump: bool
        """
        super().__init__(damages, damage_type, stun=stun, blind=blind, bump=bump)

    def apply(self, hitted: List[Any]) -> None:
        """Applique les effets du sort tempête d'acier aux champions atteints par le sort.

        :param champion: listes d'instances d'objets atteints par le sort
        :type champion: List[Any]
        :raises NotImplementedError: Méthode abstraite qui doit être implémentée par une classe enfant
        """
        pass
