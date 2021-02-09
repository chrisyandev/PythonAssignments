from enum import Enum
from pathlib import Path
import json


class FileExtensions(Enum):
    TXT = ".txt"
    JSON = ".json"


class FileHandler:

    @staticmethod
    def load_data(path, file_extension):
        my_file = Path(path)
        if my_file.is_file():
            if file_extension.lower() == FileExtensions.TXT.value:
                with open(path, mode="r") as my_text_file:
                    data = my_text_file.read()
                    return data
            elif file_extension.lower() == FileExtensions.JSON.value:
                with open(path, mode="r", encoding="utf-8") as data_file:
                    data = json.load(data_file)
                    return data

    @staticmethod
    def write_lines(path, lines):
        with open(path, mode='a') as my_text_file:
            for line in lines:
                my_text_file.write(line)


