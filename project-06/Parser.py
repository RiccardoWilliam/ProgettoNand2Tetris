<<<<<<< HEAD
class Parser:

    A_INSTRUCTION = "A_INSTRUCTION"
    C_INSTRUCTION = "C_INSTRUCTION"
    L_INSTRUCTION = "L_INSTRUCTION"

    def __init__(self, path, debug=False):
        
        with open(file = path, encoding = "utf-8") as file:
            ##removes all comments and empty lines
            self.__instructions = [
                line.strip() for line in file
                if line.strip() and not line.strip().startswith("//")
            ]

        self.__debug = debug
        self.__current_line = 0
        self.__current_instruction = None
        self.__instructionType = None
        self.__symbol = None
        self.__dest = None
        self.__comp = None
        self.__jump = None

    #parses the instruction and fetches its composing fields: dest, comp, jump and var/label symbol
    def advance(self) -> None:

        #removes leading and trailing whitespace
        self.__current_instruction = self.__instructions[self.__current_line].strip()

        if self.__current_instruction.startswith("@"):

            self.__instructionType = self.A_INSTRUCTION
            self.__symbol = self.__current_instruction.removeprefix("@")

        elif self.__current_instruction.startswith("("):

            self.__instructionType = self.L_INSTRUCTION
            self.__symbol = self.__current_instruction.removeprefix("(").removesuffix(")")
        else:
            self.__instructionType = self.C_INSTRUCTION
            inst = self.__current_instruction
            self.__symbol = "none"

            if "=" in inst:
                self.__dest = inst[:inst.index("=")]
                inst = inst.replace(self.__dest + "=", "")
            else:
                self.__dest = "null"
            
            if ";" in inst:
                self.__jump = inst[inst.index(";")+1:]
                inst = inst.replace( ";" + self.__jump, "")
            else:
                self.__jump = "null"

            self.__comp = inst
        
        if(self.__debug):
            print(f"""
line: {self.__current_line}
instruction: {self.__current_instruction}
instruction type: {self.__instructionType}
symbol: {self.__symbol}
dest: {self.__dest}
comp: {self.__comp}
jump: {self.__jump}
            """)

        self.__current_line += 1
    
    @property
    def instructionType(self) -> str:
        return self.__instructionType

    @property
    def symbol(self) -> str:
        return self.__symbol
    
    @property
    def dest(self) -> str:
        return self.__dest
    
    @property
    def comp(self) -> str:
        return self.__comp
    
    @property
    def jump(self) -> str:
        return self.__jump
    
    def hasMoreLines(self) -> bool:
=======
class Parser:

    A_INSTRUCTION = "A_INSTRUCTION"
    C_INSTRUCTION = "C_INSTRUCTION"
    L_INSTRUCTION = "L_INSTRUCTION"

    def __init__(self, path, debug=False):
        
        with open(file = path, encoding = "utf-8") as file:
            ##removes all comments and empty lines
            self.__instructions = [
                line.strip() for line in file
                if line.strip() and not line.strip().startswith("//")
            ]

        self.__debug = debug
        self.__current_line = 0
        self.__current_instruction = None
        self.__instructionType = None
        self.__symbol = None
        self.__dest = None
        self.__comp = None
        self.__jump = None

    #parses the instruction and fetches its composing fields: dest, comp, jump and var/label symbol
    def advance(self) -> None:

        #removes leading and trailing whitespace
        self.__current_instruction = self.__instructions[self.__current_line].strip()

        if self.__current_instruction.startswith("@"):

            self.__instructionType = self.A_INSTRUCTION
            self.__symbol = self.__current_instruction.removeprefix("@")

        elif self.__current_instruction.startswith("("):

            self.__instructionType = self.L_INSTRUCTION
            self.__symbol = self.__current_instruction.removeprefix("(").removesuffix(")")
        else:
            self.__instructionType = self.C_INSTRUCTION
            inst = self.__current_instruction
            self.__symbol = "none"

            if "=" in inst:
                self.__dest = inst[:inst.index("=")]
                inst = inst.replace(self.__dest + "=", "")
            else:
                self.__dest = "null"
            
            if ";" in inst:
                self.__jump = inst[inst.index(";")+1:]
                inst = inst.replace( ";" + self.__jump, "")
            else:
                self.__jump = "null"

            self.__comp = inst
        
        if(self.__debug):
            print(f"""
line: {self.__current_line}
instruction: {self.__current_instruction}
instruction type: {self.__instructionType}
symbol: {self.__symbol}
dest: {self.__dest}
comp: {self.__comp}
jump: {self.__jump}
            """)

        self.__current_line += 1
    
    @property
    def instructionType(self) -> str:
        return self.__instructionType

    @property
    def symbol(self) -> str:
        return self.__symbol
    
    @property
    def dest(self) -> str:
        return self.__dest
    
    @property
    def comp(self) -> str:
        return self.__comp
    
    @property
    def jump(self) -> str:
        return self.__jump
    
    def hasMoreLines(self) -> bool:
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
        return self.__current_line != len(self.__instructions)