from city_processor import *


def main():
    city_database = CityDatabase("city_locations_test.xlsx")
    print(city_database.city_db[0])
    ISSDataRequest.get_overhead_pass(city_database.city_db[0])

if __name__ == "__main__":
    main()
