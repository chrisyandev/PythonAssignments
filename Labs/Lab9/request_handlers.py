from abc import *
from pathlib import Path
from des import DesKey
from crypto import CryptoMode
import ast


class BaseRequestHandler(ABC):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, request, **kwargs):
        pass

    def set_handler(self, handler):
        self.next_handler = handler


class ValidateDataHandler(BaseRequestHandler):
    """ Checks if data can be processed. """

    def handle_request(self, request, **kwargs):
        """
        If file exists and is a text file, this can be processed.
        Or if data input isn't an empty string, this can be processed.
        :param request: a Request
        :param kwargs: empty
        :return: None
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
        if request.data_input is not None:
            pass



class EncryptDataHandler(BaseRequestHandler):
    def handle_request(self, request, **kwargs):
        print("encrypting data")
        key = DesKey(bytes(request.key, 'utf-8'))
        if request.data_input is not None:
            encrypted = key.encrypt(bytes(request.data_input, 'utf-8'), padding=True)
            print(request.data_input)
            print(encrypted)
        else:
            with open(request.input_file, mode="rb") as text_file:
                data = text_file.read()
                encrypted = key.encrypt(data, padding=True)
                print(data)
                print(encrypted)
        self.next_handler.handle_request(request)


class DecryptDataHandler(BaseRequestHandler):
    def handle_request(self, request, **kwargs):
        print("decrypting data")
        key = DesKey(bytes(request.key, 'utf-8'))
        if request.data_input is not None:
            data = r"%s" % request.data_input
            data = ast.literal_eval(data)
            print(data)
            decrypted = key.decrypt(data, padding=True)
            print(decrypted)
        else:
            with open(request.input_file, mode="r") as text_file:
                data = r"%s" % text_file.read()
                data = ast.literal_eval(data)
                print(data)
                decrypted = key.decrypt(data, padding=True)
                print(decrypted)
        self.next_handler.handle_request(request)


class OutputResultHandler(BaseRequestHandler):
    def handle_request(self, request, **kwargs):
        print("outputting result")
