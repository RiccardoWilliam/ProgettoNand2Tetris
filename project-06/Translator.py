<<<<<<< HEAD
class Translator:

    def __init__(self):
        pass

    def dest(self, destination: str) -> str:
        
        match(destination):
            case "null":
                return "000"
            case "M":
                return "001"
            case "D":
                return "010"
            case "DM":
                return "011"
            case "MD":
                return "011"
            case "A":
                return "100"
            case "AM":
                return "101"
            case "MA":
                return "101"
            case "AD":
                return "110"
            case "DA":
                return "110"
            case "ADM":
                return "111"

    def comp(self, computation: str) -> str:
        
        match(computation):
            case "0": 
                return "101010"
            case "1":
                return "111111"
            case "-1":
                return "111010"
            case "D":
                return "001100"
            case "A":
                return "110000"            
            case "M":
                return "110000"
            case "!D":
                return "001101"
            case "!A":
                return "110001"
            case "!M":
                return "110001"
            case "-D":
                return "001111"
            case "-A":
                return "110011"
            case "-M":
                return "110011"
            case "D+1":
                return "011111"
            case "A+1":
                return "110111"
            case "M+1":
                return "110111"
            case "D-1":
                return "001110"
            case "A-1":
                return "110010"
            case "M-1":
                return "110010"
            case "D+A":
                return "000010"
            case "D+M":
                return "000010"
            case "D-A":
                return "010011"
            case "D-M":
                return "010011"
            case "A-D":
                return "000111"
            case "M-D":
                return "000111"
            case "D&A":
                return "000000"
            case "D&M":
                return "000000"
            case "D|A":
                return "010101"
            case "D|M":
                return "010101"


    def jump(self, jump: str) -> str:
        
        match(jump):
            case "null":
                return "000"
            case "JGT":
                return "001"
            case "JEQ":
                return "010"
            case "JGE":
                return "011"
            case "JLT":
                return "100"
            case "JNE":
                return "101"
            case "JLE":
                return "110"
            case "JMP":
=======
class Translator:

    def __init__(self):
        pass

    def dest(self, destination: str) -> str:
        
        match(destination):
            case "null":
                return "000"
            case "M":
                return "001"
            case "D":
                return "010"
            case "DM":
                return "011"
            case "MD":
                return "011"
            case "A":
                return "100"
            case "AM":
                return "101"
            case "MA":
                return "101"
            case "AD":
                return "110"
            case "DA":
                return "110"
            case "ADM":
                return "111"

    def comp(self, computation: str) -> str:
        
        match(computation):
            case "0": 
                return "101010"
            case "1":
                return "111111"
            case "-1":
                return "111010"
            case "D":
                return "001100"
            case "A":
                return "110000"            
            case "M":
                return "110000"
            case "!D":
                return "001101"
            case "!A":
                return "110001"
            case "!M":
                return "110001"
            case "-D":
                return "001111"
            case "-A":
                return "110011"
            case "-M":
                return "110011"
            case "D+1":
                return "011111"
            case "A+1":
                return "110111"
            case "M+1":
                return "110111"
            case "D-1":
                return "001110"
            case "A-1":
                return "110010"
            case "M-1":
                return "110010"
            case "D+A":
                return "000010"
            case "D+M":
                return "000010"
            case "D-A":
                return "010011"
            case "D-M":
                return "010011"
            case "A-D":
                return "000111"
            case "M-D":
                return "000111"
            case "D&A":
                return "000000"
            case "D&M":
                return "000000"
            case "D|A":
                return "010101"
            case "D|M":
                return "010101"


    def jump(self, jump: str) -> str:
        
        match(jump):
            case "null":
                return "000"
            case "JGT":
                return "001"
            case "JEQ":
                return "010"
            case "JGE":
                return "011"
            case "JLT":
                return "100"
            case "JNE":
                return "101"
            case "JLE":
                return "110"
            case "JMP":
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
                return "111"