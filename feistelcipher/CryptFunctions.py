class CryptFunctions():
    class CryptFunctionBlock():
        def __init__(self, func, key = None) -> None:
            self.func = func
            self.key = [] if key is None else key

        def execute(self, num: int) -> int:
            return self.func(num, *self.key)

    def __init__(self):
        self.cryptFuncs = []

    def __iter__(self):
        return iter(self.cryptFuncs)

    def __getitem__(self, index):
        return self.cryptFuncs[index]

    def __str__(self) -> str:
        s: str = f"\n{'Function':32}Keys\n\n"
        for funcBlock in self:
            s += f"{funcBlock.func.__name__:32}{funcBlock.key}\n"

        return s

    def addFunc(self, func, key = None) -> None:
        self.cryptFuncs += [self.CryptFunctionBlock(func, key)]

