# swami.py – Room Selector Logic

class TaskMemoryRoom:
    def __init__(self, room_id):
        self.room_id = room_id
        self.memory = []

    def train(self, data, shared_core):
        processed = shared_core.forward(data)
        self.memory.append(processed)
        return processed

    def predict(self, data):
        return self.memory[-1] if self.memory else "No memory yet"

class RoomSelector:
    def __init__(self):
        self.task_to_room = {}
        self.next_id = 0

    def get_or_create(self, task_name):
        if task_name not in self.task_to_room:
            self.task_to_room[task_name] = TaskMemoryRoom(f"room_{self.next_id}")
            self.next_id += 1
        return self.task_to_room[task_name]

    def get(self, task_name):
        return self.task_to_room[task_name]
