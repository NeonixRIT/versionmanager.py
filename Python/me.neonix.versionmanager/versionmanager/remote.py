import requests

from project import Project
from version import Version

class Remote (Project):
    '''
    Object representing a the latest project version on github.
    '''
    def __init__(self, author: str, projectName: str, separator: str, length: int):
        url = f'https://api.github.com/repos/{author}/{projectName}/releases/latest'
        version = Version(requests.get(url).json()['tag_name'], separator, length)
        super().__init__(author, projectName, version)
