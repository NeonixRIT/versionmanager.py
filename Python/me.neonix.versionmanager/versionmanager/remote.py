import requests

from project import Project
from version import Version

class Remote (Project):
    '''
    Object representing a the latest project version on github.
    '''
    __slots__ = ['__url', '__separator']


    def __init__(self, author: str, projectName: str, separator: str):
        self.__url = f'https://api.github.com/repos/{author}/{projectName}/releases/latest'
        self.__separator = separator

        version = Version(requests.get(self.__url).json()['tag_name'], self.__separator)
        super().__init__(author, projectName, version)


    def update_version(self):
        version = Version(requests.get(self.__url).json()['tag_name'], self.__separator)
        super().set_version(version)
