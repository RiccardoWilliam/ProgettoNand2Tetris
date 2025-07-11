from pathlib import Path
from enum import Enum

class CommandType(Enum):
    C_ARITHMETIC = "C_ARITHMETIC"
    C_PUSH = "C_PUSH"
    C_POP = "C_POP"
    C_LABEL = "C_LABEL"
    C_GOTO = "C_GOTO"
    C_IF = "C_IF"
    C_FUNCTION = "C_FUNCTION"
    C_RETURN = "C_RETURN"
    C_CALL = "C_CALL"

class SegmentType(Enum):
    S_CONSTANT = "constant"
    S_POINTER = "pointer"
    S_THAT = "that"
    S_THIS = "this"
    S_LOCAL = "local"
    S_TEMP = "temp"
    S_ARGUMENT = "argument"
    S_STATIC = "static"

class OperatorType(Enum):
    O_ADD = "add"
    O_SUB = "sub"
    O_AND = "and"
    O_OR = "or"
    O_NEG = "neg"
    O_NOT = "not"
    O_GT = "gt"
    O_LT = "lt"
    O_EQ = "eq"

class Parser:

    def __init__(self, path: Path):

        with open(path, encoding = "utf-8") as file:
            ##removes all comments and empty lines
            self.__instructions: list[str] = []
            for line in file:
                #remove trailing and leading whitespace
                stripped_line = line.strip()
                #if line is empty or is a comment, ignore it
                if not stripped_line or stripped_line.startswith("//"):
                    continue 
                self.__instructions.append(stripped_line)
            
            if len(self.__instructions) == 0:
                print("Input file doesn't contain instructions")
                exit()

        
        self.__current_line = 0
        self.__current_instruction = None 
        self.__instruction_type = None
        self.__arg0 = None
        self.__arg1 = None 
        self.__arg2 = None
    
    def advance(self):

        #check end of instructions
        if not self.hasMoreLines():
            print("Can't advance, no more instruction available")
            exit()

        #reset args
        self.__arg0 = None
        self.__arg1 = None
        self.__arg2 = None

        #fetch instruction
        self.__current_instruction = self.__instructions[self.__current_line]
        current_instruction = self.__current_instruction.lower().split(" ")

        #check instruction length
        if len(current_instruction) > 3:
            print(f"Invalid instruction length at line {self.__current_line}")
            print(f"instruction: {self.__current_instruction}")
            exit()

        #check instruction type
        self.__instruction_type_check(current_instruction[0])
        
        #check instruction arguments 
        self.__instruction_args_check(current_instruction)

        #advance
        self.__current_line +=1

    #checks if the first instruction operand corresponds to a known instruction type
    def __instruction_type_check(self, instruction_type):
        
        for operator in OperatorType:
            if instruction_type == operator.value:
                self.__instruction_type = CommandType.C_ARITHMETIC
                self.__arg0 = operator
                return
        
        if instruction_type ==  "pop":
            self.__instruction_type = CommandType.C_POP
            return
        
        if instruction_type == "push":
            self.__instruction_type = CommandType.C_PUSH
            return
        
        if instruction_type == "call":
            self.__instruction_type = CommandType.C_CALL
            return
        
        if instruction_type == "function":
            self.__instruction_type = CommandType.C_FUNCTION
            return
        
        if instruction_type == "return":
            self.__instruction_type = CommandType.C_RETURN
            return
        
        if instruction_type == "label":
            self.__instruction_type = CommandType.C_LABEL
            return
        
        if instruction_type == "if-goto":
            self.__instruction_type = CommandType.C_GOTO
            return

        print(f"Invalid instruction type at line {self.__current_line}")
        print(f"instruction: {self.__current_instruction}")
        exit()
    
    #checks if the instruction arguments are correct and assigns them
    def __instruction_args_check(self, instruction: list[str]):
        
        #if it's an arithmetic instruction, check length and set args as empty
        if self.__instruction_type == CommandType.C_ARITHMETIC:
            if len(instruction) == 1:
                self.__arg1 = None
                self.__arg2 = None
                return

            print(f"Invalid instruction argument count at line {self.__current_line}")
            print(f"instruction: {self.__current_instruction}")
            exit()
        
        #if its a push/pop, check length, segment and index, then assign args
        if self.__instruction_type in (CommandType.C_PUSH, CommandType.C_POP):
            #check PUSH/POP arg length
            if len(instruction) != 3:
                print(f"Invalid instruction argument count at line {self.__current_line}")
                print(f"instruction: {self.__current_instruction}")
                exit()
            
            #check PUSH/POP segment existance
            for segment in SegmentType:
                if instruction[1] == segment.value:
                    break
            else:
                print(f"Invalid instruction segment at line {self.__current_line}")
                print(f"instruction: {self.__current_instruction}")
                exit()
            
            #check for index type correctness
            if not instruction[2].isdecimal():
                print(f"Invalid instruction index at line {self.__current_line}")
                print(f"instruction: {self.__current_instruction}")
                exit()
            
            #check for index value correctness
            if int(instruction[2]) > 32767 or int(instruction[2]) < 0:
                print(f"Invalid index value at line {self.__current_line}")
                print(f"instruction: {self.__current_instruction}")
                exit()
            
            self.__arg1 = SegmentType(instruction[1])
            self.__arg2 = int(instruction[2])
            return

    def hasMoreLines(self) -> bool:
        return self.__current_line < len(self.__instructions)

    @property
    def commandType(self) -> CommandType | None:
        return self.__instruction_type
    
    @property
    def arg0(self) -> OperatorType | None:
        return self.__arg0

    @property
    def arg1(self) -> SegmentType | None:
        return self.__arg1
    
    @property
    def arg2(self) -> int | None:
        return self.__arg2
    
    @property
    def currentInstruction(self) -> str | None:
        return self.__current_instruction

    