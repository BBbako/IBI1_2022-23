class Triathlon:
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time, total_time ):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = total_time
    def print_all(self):
        print(self.first_name , self.last_name , self.location , self.swim_time , self.cycle_time , self.run_time , self.total_time)
# example
s1 = Triathlon('Xiao', 'Ming', 'Beijing', 2, 2, 2, 6)
s1.print_all()
