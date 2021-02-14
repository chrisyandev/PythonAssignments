class NotificationHandler:
    """ Handles printing any type of notification. """

    @staticmethod
    def warn(message):
        """ Prints a warning. """
        print(f"WARNING: {message}")

    @staticmethod
    def notify(message):
        """ Prints a notification. """
        print(f"Note: {message}")
