class OrderProcessError(Exception):
    """ Called when something prevents an order from being filled. """
    def __init__(self):
        super().__init__(f"Order could not be processed")


class InvalidVarietyError(OrderProcessError):
    """ Called when a requested candy variety doesn't exist. """
    def __init__(self, variety):
        super().__init__(f"{variety} is not a valid variety")


class InvalidColourError(OrderProcessError):
    """ Called when a requested colour doesn't exist. """
    def __init__(self, colour):
        super().__init__(f"{colour} is not a valid colour")


class InvalidSizeError(OrderProcessError):
    """ Called when a requested size doesn't exist. """
    def __init__(self, size):
        super().__init__(f"{size} is not a valid size")


class InvalidSpiderTypeError(OrderProcessError):
    """ Called when a requested spider type doesn't exist. """
    def __init__(self, spider_type):
        super().__init__(f"{spider_type} is not a valid spider type")
