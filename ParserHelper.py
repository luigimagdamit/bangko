class ParserHelper:
    def add(self, n):
        self.stack.append(n)
    def getTop(self):
        return self.stack.pop()
    def printStack(self):
        for token in self.stack:
            print(token)
    def printMemory(self):
        for variable in self.memory:
            print(self.memory[variable])