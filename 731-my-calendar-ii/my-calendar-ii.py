class MyCalendarTwo:
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
        for time, value in self.events.items():
            if time > end:
                break
            count += value
            if count > 2:
                # Revert the changes if there's a conflict
                self.events[start] -= 1
                self.events[end] += 1
                return False
                
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)