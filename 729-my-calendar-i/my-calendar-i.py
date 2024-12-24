class MyCalendar:

    def __init__(self):
        # self.events = {}
        self.events = SortedDict()
    
    def book(self, start: int, end: int) -> bool:
        """
        Book an event from start time to end time.
        
        Args:
            start (int): Start time of the event
            end (int): End time of the event
            
        Returns:
            bool: True if the event can be booked, False if there's a conflict
        """
        # Increment count at start time, decrement at end time
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1
        
        # Check for conflicts by scanning through all times
        count = 0
        for value in self.events.values():
            count += value
            if count > 1:
                # Revert the changes if there's a conflict
                self.events[start] -= 1
                self.events[end] += 1
                return False
                
        return True

    # def __init__(self):

    #     self.calendar = []
        

    # def book(self, start: int, end: int) -> bool:
    #     # self.calendar.sort(key = lambda x: x[1], reverse = True)
    #     # 10  20
    #     # .   15(start) < end
    #     for s, e in self.calendar:
    #         if  start < e and end > s:
    #             return False
    #     self.calendar.append((start,end))
    #     return True

#      47 50
# 33 41 --> ok ending before next start
# .  39  45

# 10 20
#.   15 25
        

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)