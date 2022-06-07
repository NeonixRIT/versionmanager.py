class Version:
    '''
    Object representing a version number used to make handling Project versions easier
    '''
    __slots__ = ['__version_list', '__version_str']


    def __init__(self, version='0.0.0', separator='.'):
        self.__version_str = version
        self.__version_list = list(version.split(separator))


    def __str__(self):
        return self.__version_str


    def __repr__(self):
        return f'Version[{self.__version_str}, {self.__version_list}]'


    def __lt__(self, other):
        for i in range(len(self.__version_list)):
            version_number = int(self.__version_list[i])
            latest_version_number = int(other.__version_list[i])
            if version_number < latest_version_number:
                return True
            elif version_number > latest_version_number:
                return False
        return False


    def __eq__(self, other):
        if type(other) != Version:
            return False

        return repr(self) == repr(other)
