class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passagers = []

    def add_passagers(self, name):
        if not self.open_seats():
            return False
        self.passagers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passagers)

flight = Flight(3)

people = ["João", "Joana", "Pedro", "Joaquin"]
for person in people:
    #sucess = flight.add_passagers(person)
    #if sucess:
    if flight.add_passagers(person):
        print(f"Added {person} to flight sucessfully!")
    else:
        print(f"No available seats for {person}")


#p = Point(2, 3)
#print(p.x,' \n',p.y)

