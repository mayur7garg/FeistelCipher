class CryptFunctions():
    class CryptFunctionBlock():
        def __init__(self, func, key: int) -> None:
            self.func = func
            self.key = key

        def execute(self, num: int) -> int:
            return self.func(self.key, num)

    def __init__(self):
        self.cryptFuncs = []

    def __iter__(self):
        return iter(self.cryptFuncs)

    def __getitem__(self, index):
        return self.cryptFuncs[index]

    def addFunc(self, func, key: int) -> None:
        self.cryptFuncs += [self.CryptFunctionBlock(func, key)]
