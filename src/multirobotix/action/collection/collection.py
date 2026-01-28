from typing import List

from robotix.structure.kind.mind.action.composite.component import Component


class Collection:
    def __init__(self, members:List[Component]):
        self._members = members