from producer_consumer import *
import math


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO)

    city_database = CityDatabase("city_locations.xlsx")
    city_overhead_time_queue = CityOverheadTimeQueue()

    sub_database_size = math.floor((len(city_database.city_db) / 3))
    sub_database_1 = [city_database.city_db[x]
                      for x in range(sub_database_size)]
    sub_database_2 = [city_database.city_db[x]
                      for x in range(sub_database_size, sub_database_size * 2)]
    sub_database_3 = [city_database.city_db[x]
                      for x in range(sub_database_size * 2, len(city_database.city_db))]

    producers = [
        ProducerThread(sub_database_1, city_overhead_time_queue),
        ProducerThread(sub_database_2, city_overhead_time_queue),
        ProducerThread(sub_database_3, city_overhead_time_queue)
    ]
    for p in producers:
        p.start()
    for p in producers:
        p.join()

    consumer = ConsumerThread(city_overhead_time_queue)
    consumer.data_incoming = False
    consumer.start()
    consumer.join()


if __name__ == "__main__":
    main()
