from city_processor import *
from threading import *
import time


class CityOverheadTimeQueue:
    def __init__(self):
        self.data_queue = []
        self.access_queue_lock = Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        with self.access_queue_lock:
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
        count = 1
        for city in self.city_list:
            print(city)
            overhead_times = ISSDataRequest.get_overhead_pass(city)
            self.overhead_time_queue.put(overhead_times)
            count += 1
            if count % 5 == 0:
                time.sleep(1)


class ConsumerThread(Thread):
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.overhead_time_queue = queue
        self.data_incoming = True

    def run(self) -> None:
        if len(self.overhead_time_queue) == 0:
            print("queue empty, consumer sleeping")
            time.sleep(0.75)
        while self.data_incoming or len(self.overhead_time_queue) > 0:
            city_overhead_times = self.overhead_time_queue.get()
            for event in city_overhead_times.passes:
                print(event)
                time.sleep(0.5)
