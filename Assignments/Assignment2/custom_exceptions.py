class OrderProcessError(Exception):
    def __init__(self):
        super().__init__(f"Order could not be processed")


class InvalidVarietyError(OrderProcessError):
    def __init__(self, variety):
        super().__init__(f"{variety} is not a valid variety")


class InvalidColourError(OrderProcessError):
    def __init__(self, colour):
        super().__init__(f"{colour} is not a valid colour")


class InvalidSizeError(OrderProcessError):
    def __init__(self, size):
        super().__init__(f"{size} is not a valid size")


class InvalidSpiderTypeError(OrderProcessError):
    def __init__(self, spider_type):
        super().__init__(f"{spider_type} is not a valid spider type")
