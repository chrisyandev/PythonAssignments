from producer_consumer import *
import math


def main():
    """ Creates and starts producer and consumer threads. """
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO)
    start_time = datetime.datetime.now()

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
    consumer = ConsumerThread(city_overhead_time_queue)
    consumer.start()
    for p in producers:
        p.start()
    for p in producers:
        p.join()
    consumer.data_incoming = False
    consumer.join()

    end_time = datetime.datetime.now()
    print(f"Total duration {(end_time - start_time).total_seconds()} seconds")


if __name__ == "__main__":
    main()
