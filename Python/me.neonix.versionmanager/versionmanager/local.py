from project import Project
from version import Version

class Local(Project):
    '''
    Object representing a the current project installed by the user.
    '''
    def __init__(self, author: str, projectName: str, version: str, separator: str, length: int):
        version = Version(version, separator, length)
        super().__init__(author, projectName, version)
