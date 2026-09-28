#Typeethon o TyPython
sourcePath = "./main.py"

sourceFile = open(sourcePath)

source = sourceFile.read()

# source = "int num = 0\nfloat a = 0.0"

tokens = []

# print(tokens[len(source) - 1])

# print(source[3])

word = ""
TYPE =""
for i in range(0, len(source)):
    
    if (source[i] == " " or source[i] == "\n" or source[i]=="#"): 

        if (word != ""):
            token = ""

            match word:
                case "int" | "float" | "bool" | "string":
                    token = "data type"
                case "=":
                    token = "equal"
                case "True" | "False":
                    token = "value"
                case _:
                    token="identifier"
            
            if (word[0] >= "0" and word[0] <= "9"):
                token="value"
            elif (word[0] == "\""):
                token="value"

            tokens.append(f" {word} : {token} ")
            word=""
        
    else:
        word += source[i]

        
    if (i > (len(source) - 2)):
        if (word != ""):
            tokens.append(f"{word}")
        

print("Token List:")
for token in tokens:
    print(f"\t[{token}]")


