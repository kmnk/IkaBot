from enum import Enum
from typing import List

class Weapon(Enum):
    SHOOTERS   = 'Shooters'
    DUALIES    = 'Dualies'
    ROLLERS    = 'Rollers'
    BRUSHES    = 'Brushes'
    BLASTERS   = 'Blasters'
    BRELLAS    = 'Brellas'
    SLOSHERS   = 'Sloshers'
    CHARGERS   = 'Chargers'
    SPLATLINGS = 'Splatlings'

    @classmethod
    def from_str(cls, val:str):
        for member in cls:
            if member.value.upper() == val.upper():
                return member
        return None

    @classmethod
    def from_str_arr(cls, vals:List[str]):
        return [cls.from_str(val) for val in vals]

