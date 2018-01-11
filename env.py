import os

from type.language import Language

class Env:
    def __init__(self):
        self._debug = None
        self._language = None
        self._prefix = None

    @property
    def debug(self):
        if not self._debug:
            self._debug = os.getenv('DEBUG', 'FALSE').upper() == 'TRUE'
        return self._debug

    @property
    def language(self):
        if not self._language:
            l = os.getenv('LANGUAGE', 'en_US')
            if l == Language.EN_US.value:   self._language = Language.EN_US
            elif l == Language.JA_JP.value: self._language = Language.JA_JP
            else:                           self._language = Language.EN_US
        return self._language

    @property
    def prefix(self):
        if not self._prefix:
            self._prefix = os.getenv('PREFIX', '?')
        return self._prefix
