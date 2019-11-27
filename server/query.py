from random import choice

import numpy as np
from pandas import DataFrame


class QueryList(list):
    def first(self) -> object:
        if not self:
            return {}
        return self[0]

    def random(self) -> object:
        return choice(self)


class QueryDataFrame(DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fillna("", inplace=True)

    def _and(self, conditions: list):
        return QueryDataFrame(self[np.logical_and.reduce(conditions)])

    def search(self, **kwargs):
        conditions = list()
        for key, value in kwargs.items():
            if key not in self.keys():
                raise KeyError(key)
            conditions.append(self[key].str.contains(value))

        return self._and(conditions)

    def to_query_list(self) -> QueryList:
        return QueryList(self.to_dict("records"))
