class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            raise IndexError("ERROR: The queue is empty!")

    def peek(self):
        if len(self.items) != 0:
            return self.items[len(self.items)-1]
        else:
            raise IndexError("ERROR: The queue is empty!")
    def clear(self):
        self.items = []

    def __str__(self):
        new_list = []
        for item in self.items:
            new_list.append(str(item))
        items_str = ", ".join(new_list)
        return f"-> |{items_str}| ->"


def musical_chairs(player, music_duration):
    m = Queue()
    for name in player:
        m.enqueue(name)

    while m.size() > 1:
        for i in range(music_duration):
            temp = m.dequeue()
            m.enqueue(temp)
        print(f"{m.dequeue()} is eliminated!")
    winner = m.peek()
    return winner

names = ["Peter","Jane","Kathy","Mark"]
winner = musical_chairs(names, 3)
print(f"The winner is {winner}")




