from typing import Tuple

from ..spells.blinding_dart import BlindingDart
from ..spells.noxious_trap import NoxiousTrap
from .base_champion import BaseChampion


class Teemo(BaseChampion):  # noqa: D101
    """Classe représentant Teemo, le p'tit criss.

    :param BaseChampion: Classe mère des champions
    """

    def __init__(
        self,
        health: int,
        mana: int,
        base_damage: int,
        base_ap: int,
        armor: int,
        magic_resist: int,
        spells: Tuple[BlindingDart, NoxiousTrap],
    ) -> None:
        """Instanciate Teemo character.

        :param health: Points de vie (santé) de Teemo
        :type health: int
        :param mana: Points de mana de Teemo
        :type mana: int
        :param base_damage: Les dégâts physiques (autos-attaques) de base de Teemo
        :type base_damage: int
        :param base_ap: Les dégâts magiques de base de Teemo
        :type base_ap: int
        :param armor: Resistance aux dégâts physiques de base de Teemo
        :type armor: int
        :param magic_resist: Resistance aux dégâts magiques de base de Teemo
        :type magic_resist: int
        :param spells: Les sorts de Teemo
        :type spells: Tuple[BlindingDart, NoxiousTrap]
        """
        super().__init__(health, mana, base_damage, base_ap, armor, magic_resist, spells)
