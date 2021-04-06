from city_processor import *
from threading import *
import time


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


class ProducerThread(Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.city_list = cities
        self.overhead_time_queue = queue

    def run(self) -> None:
        print("producer running")
        count = 1
        for city in self.city_list:
            print(city)
            overhead_times = ISSDataRequest.get_overhead_pass(city)
            self.overhead_time_queue.put(overhead_times)
            count += 1
            if count % 5 == 0:
                print("producer sleeping for 1")
                time.sleep(1)


class ConsumerThread(Thread):
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.overhead_time_queue = queue
        self.data_incoming = True

    def run(self) -> None:
        print("consumer running")
        if len(self.overhead_time_queue) == 0:
            print("consumer sleeping for 0.75")
            time.sleep(0.75)
        while self.data_incoming or len(self.overhead_time_queue) > 0:
            city_overhead_times = self.overhead_time_queue.get()
            for event in city_overhead_times.passes:
                print(event)
                print("consumer sleeping for 0.5")
                time.sleep(0.5)
