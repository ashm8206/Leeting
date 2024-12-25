class Solution:
    def getSkyline(self, buildings):
        # Create events for all x-coordinates (both start and end of buildings)
        events = []
        for left, right, height in buildings:
            # Start of building: positive height
            events.append([left, -height])  # Negative height for start event
            # End of building: negative height
            events.append([right, height])  # Positive height for end event
        
        # Sort events by x-coordinate
        # If x coordinates are same:
        # 1. If both starts (negative heights), higher building first
        # 2. If both ends (positive heights), lower building first
        # 3. If mix of start and end, start comes first
        events.sort(key=lambda x: (x[0], x[1]))
        
        # Use multiset to track heights
        heights = [0]  # Initialize with ground level
        result = []
        prev_max = 0
        
        for x, h in events:
            if h < 0:  # Start of building
                heights.append(-h)  # Add height (convert back to positive)
            else:  # End of building
                heights.remove(h)  # Remove this height
                
            # Get current maximum height
            curr_max = max(heights)
            
            # If maximum height changed, add new point
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max
        
        return result