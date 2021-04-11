import argparse


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


def main(request: Request):
    """ Drives the program. """
    pass


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
