class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = []

        for (first, last, seats) in bookings:
            events.append((first-1,seats))
            events.append((last,-seats))
        events.sort()
        res = [0] * n
        for event in events:
            if event[0] >= n:
                continue
            res[event[0]] += event[1] 
        
        for i in range(1,n):
            res[i] += res[i-1] 
        return res
