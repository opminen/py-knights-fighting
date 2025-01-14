from app.knights.preparation import Knight


class Battle:

    person_battle = []

    def __init__(self, first_player: Knight, second_player: Knight) -> None:
        self.first_player = first_player
        self.second_player = second_player
        self.person_battle.extend([first_player, second_player])

    def check_loser(self) -> None:
        if self.first_player.is_no_health():
            print(f"{self.first_player.name} is dead."
                  f" Won {self.second_player.name}.")
        elif self.second_player.is_no_health():
            print(f"{self.second_player.name} is dead."
                  f" Won {self.first_player.name}.")
        else:
            print(f"{self.first_player.name} and "
                  f"{self.second_player.name} survived the battle.")

    @classmethod
    def before_battle(cls) -> None:
        for knight in cls.person_battle:
            knight.apply_preparations()

    def battle_damage(self) -> None:
        self.first_player.hp -= (
            self.second_player.power - self.first_player.protection
        )
        self.second_player.hp -= (
            self.first_player.power - self.second_player.protection)
        self.check_loser()

    @classmethod
    def battles_result(cls) -> dict:
        return {knight.name: knight.hp for knight in cls.person_battle}
