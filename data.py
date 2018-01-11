import json

import model.weapons

class Data:
    def __init__(self, env):
        self._env = env
        self._token = None
        self._weapons_arr = []

    @property
    def token(self):
        if not self._token:
            with open('TOKEN', 'r') as f:
                arr = [line.rstrip() for line in f]
                self._token = arr[0]
        return self._token

    @property
    def weapons(self):
        if len(self._weapons_arr) <= 0: self._load_weapons()
        return self._weapons_arr

    @property
    def all_weapons(self):
        if len(self._weapons_arr) <= 0: self._load_weapons()
        all_weapons = []
        for weapons in self._weapons_arr: all_weapons.extend(weapons.list)
        return all_weapons

    def _load_weapons(self):
        if len(self._weapons_arr) <= 0:
            with open('data/weapons.json', 'r') as f:
                arr = json.load(f)

            self._weapons_arr = [model.weapons.Weapons(ws, self._env.language) for ws in arr]
