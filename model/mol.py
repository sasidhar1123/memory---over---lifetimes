# mol.py – Main Memory Controller

from .swami import RoomSelector
from .shared_core import SharedCore

class MoL:
    def __init__(self):
        self.rooms = {}
        self.shared_core = SharedCore()
        self.selector = RoomSelector()

    def learn(self, task_name, data):
        room = self.selector.get_or_create(task_name)
        out = room.train(data, self.shared_core)
        return out

    def recall(self, task_name, data):
        room = self.selector.get(task_name)
        return room.predict(data)
