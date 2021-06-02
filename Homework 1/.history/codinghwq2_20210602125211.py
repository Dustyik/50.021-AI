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
return str((self.start_city, self.start_time))+’ -> ’
+ str((self.end_