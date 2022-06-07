from enum import Enum
from event import Event
from local import Local
from remote import Remote

class Result(Enum):
    OUTDATED = -1,
    CURRENT = 0,
    DEV = 1


class VersionManager:
    __slots__ = ['__local', '__remote', '__status', '__author', '__projectName', '__separator', 'outdated_event', 'current_event', 'dev_event']


    def __init__(self, author: str, projectName: str, version: str, separator='.'):
        self.__author = author
        self.__projectName = projectName
        self.__separator = separator

        self.__local = Local(author, projectName, version, separator)
        self.__remote = None

        self.outdated_event = Event()
        self.current_event = Event()
        self.dev_event = Event()


    def check_status(self):
        if self.__remote is None:
            self.__remote = Remote(self.__author, self.__projectName, self.__separator)
        else:
            self.__remote.update_version()

        if self.__local.verison() == self.__remote.verison():
            self.current_event()
            return Result.CURRENT
        elif self.__local.verison() < self.__remote.verison():
            self.outdated_event()
            return Result.OUTDATED
        else:
            self.dev_event()
            return Result.DEV



vm = VersionManager('Aquatic-Labs', 'Umbra-Mod-Menu', '2.0.5')
vm.dev_event += lambda: print('Dev version')
vm.outdated_event += lambda: print('Outdated version')
vm.current_event += lambda: print('Current version')
vm.check_status()
