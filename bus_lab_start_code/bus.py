class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, input_person):
        self.passengers.append(input_person)
    
    def drop_off(self, input_person):
        self.passengers.remove(input_person)
    
    def empty_bus(self):
        self.passengers.clear()
    
    def pick_up_from_stop(self, input_bus_stop):
        for person in input_bus_stop.queue:
            self.pick_up(person)
        input_bus_stop.clear()