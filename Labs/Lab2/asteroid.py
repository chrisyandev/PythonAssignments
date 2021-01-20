class Vector:
    def __init__(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]

    def add(self, vector):
        self.x += vector.get_x()
        self.y += vector.get_y()
        self.z += vector.get_z()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_vector(self):
        return self.get_x(), self.get_y(), self.get_z()

    def __str__(self):
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
        return self._position.add(self._velocity)

    def get_circumference(self):
        return self._circumference

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def get_id(self):
        return self._id

    @classmethod
    def __generate_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    def __str__(self):
        return 'ID: {0} | Circumference: {1} | Position: {2} | Velocity: {3}'\
            .format(self.get_id(), self.get_circumference(), self.get_position(), self.get_velocity())


def main():
    ast = Asteroid(10, Vector((1, 1, 1)), Vector((3, 2, 4)))
    print(ast)
    ast.move()
    print(ast)


if __name__ == '__main__':
    main()
