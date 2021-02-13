import json
from enum import Enum
from pathlib import Path
from json import *


class FileExtensions(Enum):
    """ Contains the types of accepted file extensions. """
    TXT = ".txt"
    JSON = ".json"


class FileHandler:
    """ Handles operations to do with files. """

    @staticmethod
    def load_data(path, file_extension):
        """
        Converts JSON-formatted text into a dictionary.
        :param path: a string
        :param file_extension: a string
        :return: a dict
        """
        my_file = Path(path)
        if my_file.is_file():
            if file_extension.lower() == FileExtensions.TXT.value:
                with open(path, mode="r") as my_text_file:
                    text = my_text_file.read()
                    try:
                        data = json.loads(text)
                    except JSONDecodeError:
                        raise InvalidFileTypeError()
                    else:
                        return data
            elif file_extension.lower() == FileExtensions.JSON.value:
                with open(path, mode="r", encoding="utf-8") as data_file:
                    return json.load(data_file)
            else:
                raise InvalidFileTypeError()
        else:
            raise FileNotExistError()

    @staticmethod
    def write_lines(path, lines):
        """
        Appends strings to a text file.
        :param path: a string
        :param lines: a string
        :return: none
        """
        with open(path, mode='a') as my_text_file:
            for line in lines:
                my_text_file.write(line)


class InvalidFileTypeError(Exception):
    """ Raised when a file is not in JSON format. """
    def __init__(self):
        super().__init__("Error! File contents need to be in JSON format!")


class FileNotExistError(Exception):
    """ Raised when a file does not exist. """
    def __init__(self):
        super().__init__("Error! File does not exist!")
