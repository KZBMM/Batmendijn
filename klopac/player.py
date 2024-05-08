import random
from probojPlayer import ProbojPlayer
from constants import *



INF = 10**9 - 1
MIN_SAFE_DIST = 1
UPGRADE_FORMATION = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)] # NOT USED
ATTACK_FORMATION = [(0,)] * 5 + [(0, 1)] * 5 + [(2, 1, 2, 1, 1)] * 100
DESIRED_LEVEL_INCOME = 3
DESIRED_LEVEL_TURRET = 2
BAGER_SAFETY_NET = unit_cost[UnitType.BAGER.value] // 2
ID_TO_UNIT = [UnitType.BAGER, UnitType.DVIHAK, UnitType.VALEC]
ID_TO_COMMAND = [Command.BAGER, Command.DVIHAK, Command.VALEC]

class MyPlayer(ProbojPlayer):
    """
    self.name: str
    self.money: int
    self.income_lvl: int
    self.turret_lvl: int
    self.world: list[Optional[Unit]] = []
    """
    moje_jednotky: list[tuple[int, Unit]]
    jeho_jednotky: list[tuple[int, Unit]]
    buy_queue = []
    attack_stage = 0
    
    
    def zivoty_jednotiek(self):
        self.log(self.moje_jednotky, self.jeho_jednotky)

        def sucet(jednotky):
            return sum(jednotka.hp for _, jednotka in jednotky)

        return sucet(self.moje_jednotky), sucet(self.jeho_jednotky)

    def kolko_kol_protivnik_pride_k_nasemu_domceku(self):
        hp_moje, hp_jeho = self.zivoty_jednotiek()
        if hp_jeho == 0:
            return INF
        vzdialenost = min(i - u.attack_range for i, u in self.jeho_jednotky)
        maximalny_utok = max(unit_attack_dmg)
        cas = hp_moje / maximalny_utok + vzdialenost
        debug(
            "kolko_kol",
            hp_moje,
            hp_jeho,
            vzdialenost,
            maximalny_utok,
            cas,
        )
        return cas

    def kolko_mozem_minut_bez_ohrozenia_domceka(self):
        cas = self.kolko_kol_protivnik_pride_k_nasemu_domceku()
        if cas == INF:
            return INF
        if cas <= MIN_SAFE_DIST:
            return -1
        debug("kolko_mozem", cas, self.money, self.income_lvl)
        peniaze = self.money + income[self.income_lvl] * cas
        mozem_minut = max(0, peniaze - unit_cost[UnitType.BAGER.value])
        return mozem_minut
    
    
    def kde_su():
        pass
    
    
    def Obrana():
        pass


    def Utok():
        pass


    def Risky_Strategia():
        pass
    
    
    
    
    
    def make_turn(self) -> Command:
        """
        Túto funkciu máte naprogramovať
        """        
        return

if __name__ == "__main__":
    p = MyPlayer()
    p.run()