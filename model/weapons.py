import model.weapon

from type.language import Language
from type.weapon import Weapon

class Weapons:

    def __init__(self, weapons, language=Language.EN_US):
        self._language = language
        self._type = Weapon.from_str(weapons['type'])
        self._localized_name = weapons['localized_name']
        self._weapons = [model.weapon.Weapon(w, language) for w in weapons['weapons']]

    @property
    def type(self): return self._type

    @property
    def localized_name(self):
        return self._localized_name[self._language.value]

    @property
    def list(self): return self._weapons

    @classmethod
    def pick(cls, types):
        return self._weapons
