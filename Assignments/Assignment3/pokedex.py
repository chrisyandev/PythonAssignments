import argparse
import datetime

from pokeretriever.request import *
from pokeretriever.pokedex_object import *


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("pokemon", "ability", "move"), help="The mode the app will open in")
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument("--inputfile", help="Name of file containing the data")
    input_group.add_argument("--inputdata", help="Data input directly into the console")
    parser.add_argument("--expanded", action="store_true", help="Outputs additional information")
    parser.add_argument("--output", default="console", help="Prints the output to this file")

    try:
        args = parser.parse_args()
        request = Request()
        print(vars(args))
        request.mode = args.mode
        request.input_file = args.inputfile
        request.input_data = args.inputdata
        request.expanded = args.expanded
        request.output = args.output
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


def execute_request(request: Request) -> list:
    validate_data_handler = ValidateDataHandler()
    prepare_data_handler = PrepareDataHandler()
    get_response_handler = GetResponseHandler()
    pokedex_object_handler = PokedexObjectHandler()
    validate_data_handler.set_handler(prepare_data_handler)
    prepare_data_handler.set_handler(get_response_handler)
    get_response_handler.set_handler(pokedex_object_handler)

    starting_handler = validate_data_handler
    result = starting_handler.handle_request(request)
    return result


def main(request: Request):
    """ Drives the program. """
    poke_objs = execute_request(request)
    print("Timestamp: " + str(datetime.datetime.now()))
    print("Number of requests: " + str(len(poke_objs)))
    for po in poke_objs:
        print(po)


if __name__ == '__main__':
    request_ = setup_request_commandline()
    main(request_)
