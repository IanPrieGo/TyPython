class Token:
    def __init__(self, lexeme, type):
        self.lexeme = lexeme
        self.type = type

    def __str__(self):
        return f"Token [ < {self.lexeme} >, {self.type} ]"