from .version import Version
from .project import Project

class Local(Project):
    '''
    Object representing a the current project installed by the user.
    '''
    def __init__(self, author: str, projectName: str, version: str, separator: str):
        version = Version(version, separator)
        super().__init__(author, projectName, version)
