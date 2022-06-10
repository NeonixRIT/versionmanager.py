'''
A GitHub Project Version Manager that polls latest version data from GitHub repo release tag

author: Kamron Cole (kjc8084@rit.edu)
'''
from enum import Enum
from .event import Event
from .local import Local
from .remote import Remote

class Status(Enum):
    OUTDATED = -1,
    CURRENT = 0,
    DEV = 1


class VersionManager:
    '''
    The main class to compare a local project to the latest Github release and perform actions based on the result
    '''
    __slots__ = ['__local', '__remote', '__author', '__projectName', '__separator', 'outdated_event', 'current_event', 'dev_event']


    def __init__(self, author: str, projectName: str, version: str, separator='.'):
        '''
        Instantiate the VersionManager for a project
        author: the owner of the project's repo
        projectName: the name of the project's repo
        version: the semantic version of the project as a string
        separator: the separator used to separate the version categories
        '''
        self.__author = author
        self.__projectName = projectName
        self.__separator = separator

        self.__local = Local(author, projectName, version, separator)
        self.__remote = None

        self.outdated_event = Event()
        self.current_event = Event()
        self.dev_event = Event()


    def check_status(self) -> Status:
        '''
        Compare local project version to the latest GitHub release version. Trigger events based on comparison result
        returns: Result of version comparison in form of values from the Status Enum
        '''
        if self.__remote is None:
            self.__remote = Remote(self.__author, self.__projectName, self.__separator)
        else:
            self.__remote.refresh()

        if self.__local.verison() == self.__remote.verison():
            self.current_event()
            return Status.CURRENT
        elif self.__local.verison() < self.__remote.verison():
            self.outdated_event()
            return Status.OUTDATED
        else:
            self.dev_event()
            return Status.DEV


    def get_data(self) -> dict:
        '''
        Get various other information about the latest GitHub release from the parsed JSON
        returns: A dictionary representation of the JSON
        '''
        if self.__remote is None:
            self.__remote = Remote(self.__author, self.__projectName, self.__separator)
        return self.__remote.get_data()
