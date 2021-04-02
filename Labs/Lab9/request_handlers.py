from abc import *
from pathlib import Path
from des import DesKey
from crypto import CryptoMode
import ast


class BaseRequestHandler(ABC):
    """ All handlers must inherit from this. """
    def __init__(self, next_handler=None):
        """
        :param next_handler: a BaseRequestHandler
        """
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, request, **kwargs):
        """ Handles a specific task. """
        pass

    def set_handler(self, handler):
        """ Sets the next handler. """
        self.next_handler = handler


class CheckKeyHandler(BaseRequestHandler):
    """ Checks if key is of valid length. """
    def handle_request(self, request, **kwargs):
        """ If key is length 8, 16, or 24, converts to bytes. """
        print("checking key")
        key_length = (8, 16, 24)
        if len(request.key) not in key_length:
            print("Key length must be 8, 16, or 24")
        else:
            kwargs["key"] = bytes(request.key, 'utf-8')
            self.next_handler.handle_request(request, **kwargs)


class ValidateDataHandler(BaseRequestHandler):
    """ Checks if data can be processed. """
    def handle_request(self, request, **kwargs):
        """
        If file exists and is a text file, this can be processed.
        Or if data input isn't an empty string, this can be processed.
        """
        print("validating input")

        is_valid_request = False

        if request.input_file is not None:
            my_file = Path(request.input_file)
            if not my_file.is_file():
                print("File does not exist")
            elif not request.input_file.endswith(".txt"):
                print("Must be a text file")
            else:
                is_valid_request = True

        if request.data_input is not None:
            if request.data_input.strip() == "":
                print("String is empty")
            else:
                is_valid_request = True

        if is_valid_request:
            self.next_handler.handle_request(request, **kwargs)
        else:
            print("Cannot process data")
            return


class PrepareDataHandler(BaseRequestHandler):
    """ Prepares the data in order to be processed. """
    def handle_request(self, request, **kwargs):
        """ Converts string from file or Request into bytes. """
        print("preparing data")
        if request.encryption_state.value == CryptoMode.EN.value:
            if request.data_input is not None:
                kwargs["data"] = bytes(request.data_input, 'utf-8')
            else:
                with open(request.input_file, mode="rb") as text_file:
                    kwargs["data"] = text_file.read()
        if request.encryption_state.value == CryptoMode.DE.value:
            if request.data_input is not None:
                data = r"%s" % request.data_input
                kwargs["data"] = ast.literal_eval(data)
            else:
                with open(request.input_file, mode="r") as text_file:
                    data = r"%s" % text_file.read()
                    kwargs["data"] = ast.literal_eval(data)
        self.next_handler.handle_request(request, **kwargs)


class EncryptDataHandler(BaseRequestHandler):
    """ Encrypts the data. """
    def handle_request(self, request, **kwargs):
        """ Encrypts the data. """
        print("encrypting data")
        key = DesKey(kwargs.pop("key"))
        kwargs["result"] = key.encrypt(kwargs.pop("data"), padding=True)
        self.next_handler.handle_request(request, **kwargs)


class DecryptDataHandler(BaseRequestHandler):
    """ Decrypts the data. """
    def handle_request(self, request, **kwargs):
        """ Decrypts the data. """
        print("decrypting data")
        key = DesKey(kwargs.pop("key"))
        kwargs["result"] = key.decrypt(kwargs.pop("data"), padding=True)
        self.next_handler.handle_request(request, **kwargs)


class OutputResultHandler(BaseRequestHandler):
    """ Outputs the result. """
    def handle_request(self, request, **kwargs):
        """ Either prints the result or writes it to a file. """
        print("outputting result")
        result = kwargs.pop("result")
        if request.output == "print":
            print(result)
        else:
            with open(request.output, mode="w") as text_file:
                text_file.write(str(result))
