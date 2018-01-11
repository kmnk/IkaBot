from type.language import Language

class Weapon:

    def __init__(self, weapon, language=Language.EN_US):
        self._language = language
        self._name = weapon['name']
        self._localized_name = weapon['localized_name']

    @property
    def name(self): return self._name

    @property
    def localized_name(self):
        return self._localized_name[self._language.value]
