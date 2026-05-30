class TimeMap:

    def __init__(self):
        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = [(timestamp, value)]
        else:
            self.time_dict[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""
        
        search_list = self.time_dict.get(key)
        low = 0
        high = len(search_list)
        
        while low < high:
            mid = (low + high) // 2

            if timestamp < search_list[mid][0]:
                high = mid
            else:
                low = mid + 1
            
        return search_list[low-1][1] if low >= 1 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)