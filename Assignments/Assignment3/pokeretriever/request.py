from abc import *
from pathlib import Path
from .poke_retriever import *
from .pokedex_object_factory import *


class Request:
    def __init__(self):
        self.mode = None
        self.input_file = None
        self.input_data = None
        self.expanded = None
        self.output = None

    def __str__(self):
        return f"Request -> Mode: {self.mode}, Input file: {self.input_file}, " \
               f"Data: {self.input_data}, Expanded: {self.expanded}, " \
               f"Output: {self.output}"


class BaseRequestHandler(ABC):
    """ All handlers must inherit from this. """
    def __init__(self, next_handler=None):
        """
        :param next_handler: a BaseRequestHandler
        """
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, request: Request, **kwargs):
        """ Handles a specific task. """
        pass

    def set_handler(self, handler):
        """ Sets the next handler. """
        self.next_handler = handler


class ValidateDataHandler(BaseRequestHandler):
    """ Checks if data can be processed. """
    def handle_request(self, request: Request, **kwargs):
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

        if request.input_data is not None:
            if request.input_data.strip() == "":
                print("String is empty")
            else:
                is_valid_request = True

        if is_valid_request:
            return self.next_handler.handle_request(request, **kwargs)
        else:
            print("Cannot process data")
            return


class PrepareDataHandler(BaseRequestHandler):
    """ Prepares the data in order to be processed. """
    def handle_request(self, request: Request, **kwargs):
        """ Converts string from file or Request into bytes. """
        print("preparing data")
        if request.input_data is not None:
            kwargs["ids"] = [request.input_data]
        else:
            with open(request.input_file, mode='r', encoding='utf-8') as text_file:
                ids = text_file.readlines()
                ids = [w.rstrip("\n") for w in ids]
                kwargs["ids"] = ids
        return self.next_handler.handle_request(request, **kwargs)


class GetResponseHandler(BaseRequestHandler):
    def handle_request(self, request: Request, **kwargs):
        print("getting response")
        kwargs["response"] = PokeRetriever.retrieve(request.mode, kwargs.get("ids"))
        print(kwargs["response"][2]["abilities"])
        return self.next_handler.handle_request(request, **kwargs)


class PokedexObjectHandler(BaseRequestHandler):
    def handle_request(self, request: Request, **kwargs):
        print("getting pokedex objects")
        poke_objects = []
        factory = FactoryTypes.factory_types[request.mode]()
        for x in kwargs.get("response"):
            poke_objects.append(factory.create_object(x, request))
        return poke_objects

        # print(poke_objects[0].id)
        # print(poke_objects[0].name)
        # print(poke_objects[0].height)
        # print(poke_objects[0].weight)
        # print(poke_objects[0].expanded)


class OutputPokedexObjectHandler(BaseRequestHandler):
    pass

