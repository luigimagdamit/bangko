from Token import Token
class Variable():
    def __init__(self, name, value, type) -> None:
        self.name = name
        self.value = value
        self.type = type
    def __str__(self) -> str:
        return (
                    "VAR_NAME " 
                    + str(self.name) 
                    + " VAR_VALUE " 
                    + str(self.value) 
                    + " VAR_TYPE " 
                    + str(self.type)
        )
    def toToken(self):
        return Token(self.name, self.value, self.type)