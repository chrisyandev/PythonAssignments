from city_processor import *
from threading import *
import time
import logging


class CityOverheadTimeQueue:
    """ Stores a queue of CityOverheadTimes to be processed. """
    def __init__(self):
        """ Initializes queue and creates a Lock to manage thread access. """
        self.data_queue = []
        self.access_queue_lock = Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """ Enqueues a CityOverheadTimes. """
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)
            print(f"element added to queue! Queue has "
                  f"{len(self.data_queue)} elements")

    def get(self) -> CityOverheadTimes:
        """ Dequeues a CityOverheadTimes. """
        with self.access_queue_lock:
            overhead_time = self.data_queue[0]
            del self.data_queue[0]
            print(f"element removed from queue! Queue has "
                  f"{len(self.data_queue)} elements left")
            return overhead_time

    def __len__(self) -> int:
        """ Gets the queue size. """
        return len(self.data_queue)


class ProducerThread(Thread):
    """ Adds the data retrieved from endpoint to the queue. """
    # For generating a unique id
    id_counter = 0

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        """
        :param cities: a list of City objects
        :param queue: a CityOverheadTimeQueue
        """
        super().__init__()
        self.city_list = cities
        self.overhead_time_queue = queue
        ProducerThread.id_counter += 1
        self.id = ProducerThread.id_counter

    def run(self) -> None:
        """ Retrieves data for each city and adds it to the queue. """
        count = 1
        for city in self.city_list:
            overhead_times = ISSDataRequest.get_overhead_pass(city)
            logging.info("Producer %d is adding to the queue", self.id)
            self.overhead_time_queue.put(overhead_times)
            count += 1
            if count % 5 == 0:
                time.sleep(1)


class ConsumerThread(Thread):
    """ Consumes data from CityOverheadTimeQueue. """
    # For generating a unique id
    id_counter = 0

    def __init__(self, queue: CityOverheadTimeQueue):
        """
        :param queue: a CityOverheadTimeQueue
        """
        super().__init__()
        self.overhead_time_queue = queue
        self.data_incoming = True
        ConsumerThread.id_counter += 1
        self.id = ConsumerThread.id_counter

    def run(self) -> None:
        """ Gets data from the queue and prints it. """
        if len(self.overhead_time_queue) == 0:
            print(f"Consumer {self.id} is sleeping since queue is empty")
            time.sleep(0.75)
        while self.data_incoming or len(self.overhead_time_queue) > 0:
            city_overhead_times = self.overhead_time_queue.get()
            print(f"The ISS will pass over {city_overhead_times.city.city_name} "
                  f"{len(city_overhead_times.passes)} times. The times are:")
            for event in city_overhead_times.passes:
                print(event)
            time.sleep(0.5)
