from VMexceptions import *
from pathlib import Path
from VMenums import *
from re import fullmatch

class Parser:

    label_pattern = r'^(?!\d)[\w.:]+$'

    def __init__(self, source: Path):

        with open(source, encoding="utf-8") as file:
            ## removes all comments and empty lines
            self.__instructions: list[str] = []
            for line in file:
                # Remove trailing and leading whitespace
                stripped_line = line.strip()
                
                # Skip if the line is empty or a full-line comment
                if not stripped_line or stripped_line.startswith("//"):
                    continue

                # Remove inline comments
                code_part = stripped_line.split("//", 1)[0].strip()
                
                # Skip if removing the inline comment results in an empty line
                if code_part:
                    self.__instructions.append(code_part)
            
            if len(self.__instructions) == 0:
                raise VMFileError(message="Input file doesn't contain instructions", path=source)

        # initialize instance variables
        self.__current_line = -1
    
    def advance(self):

        #check end of instructions
        if not self.hasMoreLines():
            raise VMFileError("Can't advance, no more instructions available")
        
        #advance
        self.__current_line +=1

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

    #checks the instruction type
    def __check_instruction_type(self, instruction_type: str):
        if instruction_type in (operator.value for operator in OperatorType):
            self.__instruction_type = CommandType.C_ARITHMETIC.value
            return

        type_map = {
            "push": CommandType.C_PUSH,
            "pop": CommandType.C_POP,
            "call": CommandType.C_CALL,
            "function": CommandType.C_FUNCTION,
            "return": CommandType.C_RETURN,
            "label": CommandType.C_LABEL,
            "if-goto": CommandType.C_IF,
            "goto": CommandType.C_GOTO
        }

        if instruction_type in type_map:
            self.__instruction_type = type_map[instruction_type].value
            return

        raise VMInstructionError(message="Invalid instruction type",instruction=self.__current_instruction,line_number=self.__current_line)

    #checks if the instruction arguments based on the command are correct and assigns them
    def __check_instruction_args(self, instruction: list[str]):
        
        arg_count = len(instruction)
        command = self.__instruction_type

        if command == CommandType.C_ARITHMETIC.value:
            if arg_count != 1:
                raise VMInstructionError(message="Invalid instruction argument count", instruction=self.__current_instruction, line_number=self.__current_line)
            self.__arg1 = instruction[0]
            return
        
        if command in (CommandType.C_PUSH.value, CommandType.C_POP.value):

            if arg_count != 3:
                raise VMInstructionError(message="Invalid instruction argument count", instruction=self.__current_instruction, line_number=self.__current_line)            

            segment = instruction[1]
            index = instruction[2]

            #unknown segment
            if segment not in [segment.value for segment in SegmentType]:
                raise VMInstructionError(message="Invalid instruction segment", instruction=self.__current_instruction, line_number=self.__current_line)
            
            #illegal "pop constant x" instruction
            if command == CommandType.C_POP.value and segment == SegmentType.S_CONSTANT.value:
                raise VMSegmentError(message="Invalid segment for pop instruction, using constant", instruction=self.__current_instruction, line_number=self.__current_line)

            #invalid index type
            if not index.isdecimal():
                raise VMInstructionError(message="Invalid instruction index, is not decimal", instruction=self.__current_instruction, line_number=self.__current_line)                
        
            #invalid index value
            if not (0 <= int(index) <= 32767):
                raise VMInstructionError(message="Invalid index value, must be between 0 and 32767", instruction=self.__current_instruction, line_number=self.__current_line)
            
            #illegal "push/pop temp x" instruction where x not in [0..7]
            if segment == SegmentType.S_TEMP.value and int(index) not in [i for i in range(8)]:
                raise VMInstructionError(message="Invalid index for TEMP segment, range not in between [0..7]", instruction=self.__current_instruction, line_number=self.__current_line)
            
            #illegal "push/pop pointer x" instruction where x not in [0.7]
            if segment == SegmentType.S_POINTER.value and int(index) not in (0,1):
                raise VMInstructionError(message="Invalid index for POINTER segment, range not in between [0,1]", instruction=self.__current_instruction, line_number=self.__current_line)

            self.__arg1 = segment
            self.__arg2 = index
            return

        if command == CommandType.C_RETURN.value:
            if arg_count != 1:
                raise VMInstructionError(message="Invalid instruction argument count", instruction=self.__current_instruction, line_number=self.__current_line)            
            self.__arg1 = None
            self.__arg2 = None
            return
        
        if command in (CommandType.C_LABEL.value, CommandType.C_GOTO.value, CommandType.C_IF.value):
            if arg_count != 2:
                raise VMInstructionError(message="Invalid instruction argument count", instruction=self.__current_instruction, line_number=self.__current_line)

            label = instruction[1]
            
            if not fullmatch(Parser.label_pattern,label):
                raise VMInstructionError(message="Invalid instruction label format", instruction=self.__current_instruction, line_number=self.__current_line)
            self.__arg1 = label
            self.__arg2 = None
            return

        if command in (CommandType.C_FUNCTION.value, CommandType.C_CALL.value):
            if arg_count != 3:
                raise VMInstructionError(message="Invalid instruction argument count", instruction=self.__current_instruction, line_number=self.__current_line)

            label = instruction[1]
            nVars = instruction[2]   #nVars is considered the same as nArgs

            if not fullmatch(Parser.label_pattern, label):
                raise VMInstructionError(message="Invalid instruction label format", instruction=self.__current_instruction, line_number=self.__current_line)

            if not nVars.isdecimal():
                raise VMInstructionError(message="Invalid instruction index", instruction=self.__current_instruction, line_number=self.__current_line)                

            self.__arg1 = label
            self.__arg2 = nVars
            return 

    def hasMoreLines(self) -> bool:
        return self.__current_line < len(self.__instructions) - 1

    def commandType(self) -> str:
        if self.__current_line == -1:
            raise VMFileError(message="No instruction parsed yet, call Parser.advance() first")
        
        return self.__instruction_type
    
    def arg1(self) -> str:
        if self.__current_line == -1:
            raise VMFileError(message="No instruction parsed yet, call Parser.advance() first")

        if self.__arg1 is None:
            raise VMInstructionError(message="Can't call 1st argument, is None", instruction=self.__current_instruction, line_number=self.__current_line)
        
        return self.__arg1
    
    def arg2(self) -> str:
        if self.__current_line == -1:
            raise VMFileError(message="No instruction parsed yet, call Parser.advance() first")

        if self.__arg2 is None:
            raise VMInstructionError(message="Can't call 2nd argument, is None", instruction=self.__current_instruction, line_number=self.__current_line)
        
        return self.__arg2
    
    def currentInstruction(self) -> str:
        if self.__current_line == -1:
            raise VMFileError(message="No instruction parsed yet, call Parser.advance() first")
        
        return self.__current_instruction

    