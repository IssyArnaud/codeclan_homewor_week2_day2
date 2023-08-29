class BusStop:
    def __init__(self, input_name):
        self.name = input_name
        self.queue = []
    
    def queue_length(self):
        return len(self.queue)
    
    def add_to_queue(self, input_person):
        self.queue.append(input_person)
    
    def clear(self):
        self.queue.clear()