#Typeethon o TyPython

from tokens import Token

def getType(lexeme):

    if (lexeme[0] >= "0" and lexeme[0] <= "9"):
        return "value"
    elif (lexeme[0] == "\""):
        return "value"

    match lexeme:
        case "int" | "float" | "bool" | "string":
            return "data type"
        case "=":
            return "equal"
        case ":":
            return "colon"
        case "True" | "False":
            return "value"
        case _:
            return"identifier"
    
    

def matches(suspect, criminals):
    for criminal in criminals:
        if (suspect == criminal):
            return True
    return False


    
sourcePath = "./main.tpy"
sourceFile = open(sourcePath)

# source = sourceFile.read()

source = "num : int = 0\n a : float = 0.0"

tokens = []


lastRound = False
lexeme = ""

for i in range(0, len(source)):

    try:
        if(source[i+1]):
            pass
    except IndexError:
        lastRound = True
            
    if (matches(source[i], [" ", "\n", "#"])): 

        if (lexeme != ""):
            type = getType(lexeme)

            tokens.append(Token(lexeme, type))
            lexeme=""
    else:
        lexeme += source[i]

    if (lastRound):
        if (lexeme != ""):
            type = getType(lexeme)

            tokens.append(Token(lexeme, type))
            lexeme=""


print("type List:")
for type in tokens:
    print(f"\t{type}")



