class BaseChampion:  # noqa: D100
    """Classe parente des champions."""

    def __init__(
        self,
        health: int,
        mana: int,
        base_damage: int,
        base_ap: int,
        armor: int,
        magic_resist: int,
    ) -> None:
        """Instanciation de la classe parente des divers champions.
        On s'attend à recevoir les caractéristiques de bases de chacun,
        comme la santé, le mana, les dégâts et les résistances.

        :param health: Points de vie (santé) du champion
        :type health: int
        :param mana: Points de mana du champion
        :type mana: int
        :param base_damage: Les dégâts physiques (autos-attaques) de base du champion
        :type base_damage: int
        :param base_ap: Les dégâts magiques de base du champion
        :type base_ap: int
        :param armor: Resistance aux dégâts physiques de base du champion
        :type armor: int
        :param magic_resist: Resistance aux dégâts magiques de base du champion
        :type magic_resist: int
        """  # noqa: D205
        self.health = health
        self.mana = mana
        self.base_damage = base_damage
        self.base_ap = base_ap
        self.armor = armor
        self.magic_resist = magic_resist

        self._stunned = False
        self._bumped = False
        self._blinded = False
