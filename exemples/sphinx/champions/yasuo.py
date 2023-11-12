from typing import Tuple

from ..spells.steel_tempest import SteelTempest
from .base_champion import BaseChampion


class Yasuo(BaseChampion):  # noqa: D101
    """Classe représentant Yasuo, le machin qui va dans tous les sens.

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
        spells: Tuple[SteelTempest],
    ) -> None:
        """Instanciate Yasuo character.

        :param health: Points de vie (santé) de Yasuo
        :type health: int
        :param mana: Points de mana de Yasuo
        :type mana: int
        :param base_damage: Les dégâts physiques (autos-attaques) de base de Yasuo
        :type base_damage: int
        :param base_ap: Les dégâts magiques de base de Yasuo
        :type base_ap: int
        :param armor: Resistance aux dégâts physiques de base de Yasuo
        :type armor: int
        :param magic_resist: Resistance aux dégâts magiques de base de Yasuo
        :type magic_resist: int
        :param spells: Les sorts de Yasuo
        :type spells: Tuple[SteelTempest]
        """
        super().__init__(health, mana, base_damage, base_ap, armor, magic_resist, spells)
