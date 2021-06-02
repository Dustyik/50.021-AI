#flight search engine
#flight - starting city + time
#city - strings and time

#1. Good choice of state - Current City

class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time

    def __str__(self):
        return str((self.start_city, self.start_time))+ "->"+ str((self.end_city, self.end_time))

flightDB = [Flight("Rome", 1, "Paris", 4),
            Flight("Rome", 3, "Madrid", 5),
            Flight("Rome", 5, "Istanbul", 10),
            Flight("Paris", 2, "London", 4),
            Flight("Paris", 5, "Oslo", 7),
            Flight("Paris", 5, "Istanbul", 9),
            Flight("Madrid", 7, "Rabat", 10),
            Flight("Madrid", 8, "London", 10),
            Flight("Istanbul", 10, "Constantinople", 10)]