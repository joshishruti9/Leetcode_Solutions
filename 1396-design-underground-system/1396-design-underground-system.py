class UndergroundSystem:
    #We can use dictionary to store intime for a particular id
    #when we call checkout we will pop out that value and we will calculate average of start and end and store in another dictonary
    #when we are calling getAverageTime we will get the vvalue from dictionary2 and return it.

    def __init__(self):

        self.travelMap = {}
        self.avgTimeMap = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.travelMap:
            self.travelMap[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.travelMap:
            start_station_name, start_time = self.travelMap.pop(id)
            time_difference = t - start_time

            if (start_station_name, stationName) in self.avgTimeMap:
                curr_avg_time, count = self.avgTimeMap.pop((start_station_name, stationName))
                #curr_total_time += time_difference
                curr_avg_time = (((curr_avg_time * count) + time_difference) / (count+1))
                self.avgTimeMap[((start_station_name, stationName))] = (curr_avg_time, count+1)
            else:
                self.avgTimeMap[((start_station_name, stationName))] = (time_difference, 1)



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        curr_avg_time, count = self.avgTimeMap.get((startStation, endStation))
        return curr_avg_time
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)