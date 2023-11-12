from typing import List

from ..champions.base_champion import BaseChampion
from .base_spell import BaseSpell


class NoxiousTrap(BaseSpell):
    """Sort ultime piège nocif (R spell) de Teemo."""
    def __init__(self, damages: List[int], damage_type: List[str], *, stun: bool, blind: bool, bump: bool) -> None:
        """Instancie la classe du sort piège nocif de Teemo.

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
    
    def apply(self, champions: List[BaseChampion]) -> None:
        """Applique les effets du sort piège nocif aux champions atteints par le sort.

        :param champion: listes d'instances de champions atteints par le sort
        :type champion: List[BaseChampion]
        :raises NotImplementedError: Méthode abstraite qui doit être implémentée par une classe enfant
        """
        pass