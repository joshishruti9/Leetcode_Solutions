class TimeMap:
    def bisect_right(self, timestamp, values, low, high):

        while low < high:
            mid = (low + high) // 2

            if timestamp < values[mid][0]:
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

        index = self.bisect_right(timestamp, values, 0, len(values))

        # 1,2,3,4,15,16,17,18

        #if index < len(values) and values[index][0] == timestamp:
            #return values[index][1]
        
        if index > 0:
            return values[index-1][1]

        return ""

       


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)