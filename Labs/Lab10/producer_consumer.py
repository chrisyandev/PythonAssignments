from city_processor import *

class CityOverheadTimeQueue:
    def __init__(self):
        self.data_queue = []

    def put(self, overhead_time: CityOverheadTimes) -> None:
        self.data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        overhead_time = self.data_queue[0]
        del self.data_queue[0]
        return overhead_time

    def __len__(self) -> int:
        return len(self.data_queue)


