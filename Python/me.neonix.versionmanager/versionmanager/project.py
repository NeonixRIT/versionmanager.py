class Project:
    '''
    Base class for a project.
    '''
    __slots__ = ['__author', '__name', '__version']

    def __init__(self, author, name, version):
        self.__author = author
        self.__name = name
        self.__version = version


    def __repr__(self):
        return f'Project[{self.__author}, {self.__name}, {self.__version}]'


    def set_version(self, version):
        self.__version = version


    def verison(self):
        return self.__version
