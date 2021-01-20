import datetime
import math
import random

from asteroid import *


class Controller:

    asteroids = []

    def __init__(self, num_of_asteroids, min_radius, max_radius, cube_length, max_speed):
        for x in range(num_of_asteroids):
            new_asteroid = Asteroid(self.__random_circumference(min_radius, max_radius),
                                    self.__random_vector(-(cube_length/2), cube_length/2),
                                    self.__random_vector(-max_speed, max_speed))
            self.asteroids.append(new_asteroid)

    @classmethod
    def simulate(cls, seconds):
        target_time = datetime.datetime.now().second + 1
        while datetime.datetime.now().second < target_time:
            pass
        print('Simulation Start Time: ', datetime.datetime.now())
        target_time += 1
        for s in range(seconds):
            for a in cls.asteroids:
                a.move()
            while datetime.datetime.now().second < target_time:
                pass
            target_time += 1

    @staticmethod
    def __random_vector(min, max):
        x = random.randint(min, max)
        y = random.randint(min, max)
        z = random.randint(min, max)
        return Vector((x, y, z))

    @staticmethod
    def __random_circumference(min_radius, max_radius):
        radius = random.randint(min_radius, max_radius)
        return 2 * math.pi * radius


def main():
    controller = Controller(100, 1, 4, 100, 5)

    controller.simulate(20)
    print('finished simulation')


if __name__ == '__main__':
    main()
