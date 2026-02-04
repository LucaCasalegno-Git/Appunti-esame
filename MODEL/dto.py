from datetime import datetime
from dataclasses import dataclass, field
from arts_mia.model.object import Object

@dataclass
class State:
    o1: Object  # Approccio ORM
    o2: Object
    id: str
    name: str
    lat: float
    lng: float
    neighbors: list = field(default_factory=list)
    date_posted: datetime

    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id
    def __repr__(self):
        return f'<State id={self.id} name={self.name}>'
    def __str__(self):
        return f"{self.team_code} ({self.name})"