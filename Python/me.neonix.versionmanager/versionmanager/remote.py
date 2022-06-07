import requests

from project import Project
from version import Version

class Remote (Project):
    '''
    Object representing a the latest project version on github.
    '''
    __slots__ = ['__url', '__separator', '__data']


    def __init__(self, author: str, projectName: str, separator: str):
        self.__url = f'https://api.github.com/repos/{author}/{projectName}/releases/latest'
        self.__separator = separator
        self.__data = requests.get(self.__url).json()

        version = Version(self.__data['tag_name'], self.__separator)
        super().__init__(author, projectName, version)


    def refresh(self):
        self.__data = requests.get(self.__url).json()
        version = Version(self.__data['tag_name'], self.__separator)
        super().set_version(version)


    def get_data(self):
        return self.__data
