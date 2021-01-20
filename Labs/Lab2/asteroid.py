class Vector:
    """This class represents a 3D vector."""
    def __init__(self, vector):
        """
        Initializes the state.
        :param vector: a tuple holding the vector coordinates
        """
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]

    def add(self, vector):
        """
        Adds another vector to this one.
        :param vector: another vector
        :return: result of adding the vectors
        """
        self.x += vector.get_x()
        self.y += vector.get_y()
        self.z += vector.get_z()

    def get_x(self):
        """
        Gets the x coordinate.
        :return: the x coordinate
        """
        return self.x

    def get_y(self):
        """
        Gets the y coordinate.
        :return: the y coordinate
        """
        return self.y

    def get_z(self):
        """
        Gets the z coordinate.
        :return: the z coordinate
        """
        return self.z

    def get_vector(self):
        """
        Gets the vector coordinates as a tuple.
        :return: a tuple containing the vector coordinates
        """
        return self.get_x(), self.get_y(), self.get_z()

    def __str__(self):
        """
        Changes the vector as a tuple into a string.
        :return: a string representing the vector coordinates
        """
        return str(self.get_vector())


class Asteroid:
    """This class represents an asteroid."""
    id_counter = 0

    def __init__(self, circumference, position, velocity):
        """
        Initializes properties of the asteroid.
        :param circumference: in metres
        :param position: a 3D vector
        :param velocity: a 3D vector
        """
        self._circumference = circumference
        self._position = position
        self._velocity = velocity
        self._id = self.__generate_id()

    def move(self):
        """
        Changes the asteroid position based on its velocity.
        Prints the asteroid's old and new positions.
        :return: none
        """
        print('Asteroid {0} moved! Old Pos: {1} '
              .format(self.get_id(), self.get_position()), end="")
        self._position.add(self._velocity)
        print('-> New Pos: {0}'.format(self.get_position()))

    def get_circumference(self):
        """
        Gets the asteroid's circumference.
        :return: the asteroid's circumference
        """
        return self._circumference

    def get_position(self):
        """
        Gets the asteroid's position.
        :return: the asteroid's position
        """
        return self._position

    def get_velocity(self):
        """
        Gets the asteroid's velocity.
        :return: the asteroid's velocity
        """
        return self._velocity

    def get_id(self):
        """
        Gets the asteroid's unique id.
        :return: the asteroid's unique id
        """
        return self._id

    @classmethod
    def __generate_id(cls):
        # Returns a new id
        cls.id_counter += 1
        return cls.id_counter

    def __str__(self):
        """
        Returns a formatted string containing information about the asteroid.
        :return: a formatted string
        """
        return 'Asteroid: {0} is currently at {2} and moving at {3} ' \
               'meters per second. It has a circumference of {1}.'\
            .format(self.get_id(), self.get_circumference(),
                    self.get_position(), self.get_velocity())

