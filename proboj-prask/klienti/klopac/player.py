import random
from probojPlayer import ProbojPlayer
from constants import *
from unit import Unit

OBRANASTAGE = 0
INF = 10**9 - 1
MIN_SAFE_DIST = 2
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

            
        
        

        
    
    
    def make_turn(self) -> Command:
        """
        Túto funkciu máte naprogramovať
        """        
        stratoska = 2
        max = 5
        pocet_nepriatelov = 0
        zoznwm = self.world
        for i in range(0, len(zoznwm)-1):
            jednotka = zoznwm[i]
            if jednotka is not None:
                if not jednotka.owner == self.name:
                    pocet_nepriatelov += 1
                    if i < 10:
                        stratoska = 2
                    elif pocet_nepriatelov > 0:
                        stratoska = 4
                    else:
                        stratoska = 1

        if stratoska == 1:
            return Command.INCOME    
        elif stratoska == 2:
            return Command.DVIHAK       
        elif stratoska == 3:
            return Command.BAGER  
        elif stratoska == 4:
            ##self.Rudko_je_najsamsuper()
            return Command.VALEC
        pass
           
        
        
        
        
        

        

if __name__ == "__main__":
    p = MyPlayer()
    p.run()