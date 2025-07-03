from VMexceptions import *
from pathlib import Path
from VMenums import *

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
                raise VMFileError(message="Input file doesn't contain instructions", path=path)

        
        self.__current_line = 0
    
    def advance(self):

        #check end of instructions
        if not self.hasMoreLines():
            raise VMFileError("Can't advance, no more instructions available")

        #reset args
        self.__arg1 = None
        self.__arg2 = None

        #fetch instruction
        self.__current_instruction = self.__instructions[self.__current_line]
        instruction_fragments = self.__current_instruction.lower().split()

        #check instruction length
        if len(instruction_fragments) > 3:
            raise VMInstructionError(message="Invalid instruction length", instruction=self.__current_instruction, line_number=self.__current_line)

        #check instruction type
        self.__check_instruction_type(instruction_fragments[0])
        
        #check instruction arguments 
        self.__check_instruction_args(instruction_fragments)

        #advance
        self.__current_line +=1

    #checks the instruction type
    def __check_instruction_type(self, instruction_type: str):
        if instruction_type in (operator.value for operator in OperatorType):
            self.__instruction_type = CommandType.C_ARITHMETIC
            return

        type_map = {
            "push": CommandType.C_PUSH,
            "pop": CommandType.C_POP,
            "call": CommandType.C_CALL,
            "function": CommandType.C_FUNCTION,
            "return": CommandType.C_RETURN,
            "label": CommandType.C_LABEL,
            "if-goto": CommandType.C_GOTO
        }

        if instruction_type in type_map:
            self.__instruction_type = type_map[instruction_type]
            return

        raise VMInstructionError(message="Invalid instruction type",instruction=self.__current_instruction,line_number=self.__current_line)

    #checks if the instruction arguments based on the command are correct and assigns them
    def __check_instruction_args(self, instruction: list[str]):
        
        arg_count = len(instruction)

        #checks for arithmetic compliance
        if self.__instruction_type == CommandType.C_ARITHMETIC:
            if arg_count != 1:
                raise VMInstructionError(message="Invalid instruction argument count", instruction=self.__current_instruction, line_number=self.__current_line)
            self.__arg1 = instruction[0]
            return
        
        #checks for push/pop compliance
        if self.__instruction_type in (CommandType.C_PUSH, CommandType.C_POP):

            if arg_count != 3:
                raise VMInstructionError(message="Invalid instruction argument count", instruction=self.__current_instruction, line_number=self.__current_line)            

            arg = instruction[1]
            index = int(instruction[2])

            if arg not in [segment.value for segment in SegmentType]:
                raise VMInstructionError(message="Invalid instruction segment", instruction=self.__current_instruction, line_number=self.__current_line)
            
            #illegal "pop constant x" instruction
            if self.__instruction_type == CommandType.C_POP and arg == SegmentType.S_CONSTANT.value:
                raise VMSegmentError(message="Invalid segment for pop instruction, using constant", instruction=self.__current_instruction, line_number=self.__current_line)

            if not arg.isdecimal():
                raise VMInstructionError(message="Invalid instruction index", instruction=self.__current_instruction, line_number=self.__current_line)                
        
            if not (0 <= index <= 32767):
                raise VMInstructionError(message="Invalid index value", instruction=self.__current_instruction, line_number=self.__current_line)
            
            self.__arg1 = instruction[1]
            self.__arg2 = instruction[2]
            return

    def hasMoreLines(self) -> bool:
        return self.__current_line < len(self.__instructions)

    def commandType(self) -> CommandType | None:
        return self.__instruction_type
    
    def arg1(self) -> str | None:
        return self.__arg1
    
    def arg2(self) -> str | None:
        return self.__arg2
    
    def currentInstruction(self) -> str | None:
        return self.__current_instruction

    