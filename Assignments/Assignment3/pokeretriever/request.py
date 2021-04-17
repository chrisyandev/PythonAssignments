import datetime
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
    async def handle_request(self, request: Request, **kwargs):
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
            return await self.next_handler.handle_request(request, **kwargs)
        else:
            print("Data input error. File does not exist or string is empty.")
            return


class PrepareDataHandler(BaseRequestHandler):
    """ Prepares the data in order to be processed. """
    async def handle_request(self, request: Request, **kwargs):
        """ Converts string from file or Request into bytes. """
        print("preparing data")
        if request.input_data is not None:
            kwargs["ids"] = [request.input_data]
        else:
            with open(request.input_file, mode='r', encoding='utf-8') as text_file:
                ids = text_file.readlines()
                ids = [w.rstrip("\n") for w in ids]
                kwargs["ids"] = ids
        return await self.next_handler.handle_request(request, **kwargs)


class GetResponseHandler(BaseRequestHandler):
    async def handle_request(self, request: Request, **kwargs):
        print("getting response")
        kwargs["response"] = await PokeRetriever.process_requests(request.mode, kwargs.get("ids"))
        return await self.next_handler.handle_request(request, **kwargs)


class PokedexObjectHandler(BaseRequestHandler):
    async def handle_request(self, request: Request, **kwargs):
        print("getting pokedex objects")
        factory = FactoryTypes.factory_types[request.mode]()
        async_coroutines = [factory.create_object(**json_obj, expanded=request.expanded)
                            for json_obj in kwargs["response"]]
        poke_objects = await asyncio.gather(*async_coroutines)
        kwargs["poke_objects"] = poke_objects
        return self.next_handler.handle_request(request, **kwargs)


class OutputHandler(BaseRequestHandler):
    def handle_request(self, request: Request, **kwargs):
        poke_objects = kwargs["poke_objects"]
        print("Timestamp: " + str(datetime.datetime.now()))
        print("Number of requests: " + str(len(poke_objects)))
        for po in poke_objects:
            print("==============================================")
            print(po)
            print("==============================================")
        return "success", poke_objects
