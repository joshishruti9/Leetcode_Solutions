class UndergroundSystem:

    def __init__(self):
        self.stationMap = {}
        self.timeMap = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        if id not in self.stationMap:
            self.stationMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        if id in self.stationMap:
            start_station, start_time = self.stationMap.pop(id)

            time_diff = t - start_time

            if (start_station, stationName) in self.timeMap:
                curr_time_diff, curr_count = self.timeMap.pop((start_station, stationName))
                self.timeMap[(start_station, stationName)] = (curr_time_diff + time_diff, curr_count + 1)
            else:
                self.timeMap[(start_station, stationName)] = (time_diff, 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        time, count = self.timeMap[(startStation, endStation)]
        return time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)