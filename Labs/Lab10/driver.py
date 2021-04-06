from city_processor import *
from producer_consumer import *


def main():
    city_database = CityDatabase("city_locations_test.xlsx")
    # print(city_database.city_db[0])
    # city_overhead_times = ISSDataRequest.get_overhead_pass(city_database.city_db[0])
    city_overhead_time_queue = CityOverheadTimeQueue()
    # city_overhead_time_queue.put(city_overhead_times)
    # print(len(city_overhead_time_queue))

    producer = ProducerThread(city_database.city_db, city_overhead_time_queue)
    producer.start()
    producer.join()

    consumer = ConsumerThread(city_overhead_time_queue)
    consumer.start()
    consumer.join()
    print("setting data_incoming to False")
    consumer.data_incoming = False


if __name__ == "__main__":
    main()
