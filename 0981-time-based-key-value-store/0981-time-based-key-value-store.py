class TimeMap:
    def bisect_left(self, timestamp, values, low, high):

        while low < high:
            mid = (low + high) // 2

            if timestamp <= values[mid][0]:
                high = mid
            else:
                low = mid + 1
        
        return low

    def __init__(self):
        self.timestamp_val = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp_val:
            self.timestamp_val[key] = [(timestamp, value)]
        else:
            self.timestamp_val[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_val:
            return ""

        values = self.timestamp_val[key]

        index = self.bisect_left(timestamp, values, 0, len(values))

        if index == len(values):
            return values[index-1][1]

        if values[index][0] == timestamp:
            return values[index][1]
        
        if index == 0:
            return ""
       
        return values[index-1][1]

       


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)