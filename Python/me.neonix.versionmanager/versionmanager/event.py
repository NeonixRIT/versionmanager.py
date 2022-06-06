class Event:
    __slots__ = ['__funcs']


    def __init__(self):
        self.__funcs = []


    def __call__(self) -> list:
        for func in self.__funcs:
            func()


    def __iadd__(self, func):
        self.__funcs.append(func)
        return self
