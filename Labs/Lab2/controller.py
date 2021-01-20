import datetime
import math
import random

from asteroid import *


class Controller:
    """This class controls the simulation of asteroids in space."""
    asteroids = []

    def __init__(self, num_of_asteroids, min_radius, max_radius, cube_length, max_speed):
        """
        Creates Asteroid instances with randomized properties
        limited by this method's arguments.
        :param num_of_asteroids: the number of asteroids to create
        :param min_radius: an asteroid's minimum possible radius
        :param max_radius: an asteroid's maximum possible radius
        :param cube_length: the length of the space containing the asteroids
        :param max_speed: max value for an asteroid's velocity vector
        """
        for x in range(num_of_asteroids):
            new_asteroid = Asteroid(self.__random_circumference(min_radius, max_radius),
                                    self.__random_vector(-(cube_length/2), cube_length/2),
                                    self.__random_vector(-max_speed, max_speed))
            self.asteroids.append(new_asteroid)

    @classmethod
    def simulate(cls, seconds):
        """
        Moves all asteroids once every second, on the second.
        If the time is partway through a second, execution is paused.
        :param seconds: the duration of the simulation
        :return: none
        """
        target_time = datetime.datetime.now().second + 1
        while datetime.datetime.now().second < target_time:
            pass
        print('Simulation Start Time: ', datetime.datetime.now())
        print('\nMoving Asteroids!\n-----------------')
        target_time += 1
        for s in range(seconds):
            for a in cls.asteroids:
                a.move()
                print(a)
            while datetime.datetime.now().second < target_time:
                pass
            target_time += 1

    @staticmethod
    def __random_vector(min, max):
        # Returns a Vector with random coordinates
        x = random.randint(min, max)
        y = random.randint(min, max)
        z = random.randint(min, max)
        return Vector((x, y, z))

    @staticmethod
    def __random_circumference(min_radius, max_radius):
        # Calculates the circumference based on a random radius
        radius = random.randint(min_radius, max_radius)
        return 2 * math.pi * radius


def main():
    """
    Drives the program.
    :return: none
    """
    controller = Controller(100, 1, 4, 100, 5)
    controller.simulate(5)
    print('finished simulation')


if __name__ == '__main__':
    main()
