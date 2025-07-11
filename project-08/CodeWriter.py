from pathlib import Path
from VMenums import *
from VMexceptions import *

#TODO   manage multiple source .vm files,
#       write init sequence

class CodeWriter:

    __ASM_POP_UPDATE_SP = "\n".join([
        "@SP",
        "AM=M-1",
        "D=M"
    ])

    __ASM_PUSH_UPDATE_SP = "\n".join([
        "@SP", 
        "A=M", 
        "M=D", 
        "@SP", 
        "M=M+1"])

    def __init__(self, path: Path):
        self.__output_path = path
        self.__filename = path.stem
        self.__current_function = path.stem
        self.__label_map = {
            "frame": 0,  
            "call": 0, 
            "return": 0, 
            "math": 0}

        # Clear old file content
        open(self.__output_path, "w").close()

    def writePushPop(self, instruction_type: CommandType, segment: SegmentType, index: int):

        #hashmap for VM segments to assembly segments correspondance
        VM_TO_ASM_SEGMENT = {
            SegmentType.S_THIS: "THIS",
            SegmentType.S_THAT: "THAT",
            SegmentType.S_LOCAL: "LCL",
            SegmentType.S_ARGUMENT: "ARG"
        }

        assembly = ""

        if instruction_type == CommandType.C_PUSH:

            #adds a debugging comment
            assembly = f"// push {segment.value} {index}\n"

            match segment:
                case SegmentType.S_CONSTANT:
                    assembly += "\n".join([
                        f"@{index}",
                        "D=A"
                    ])

                case SegmentType.S_TEMP:
                    assembly += "\n".join([
                        f"@R{5 + index}",
                        "D=M"
                    ])

                case SegmentType.S_POINTER:
                    segment_name = "THIS" if index == 0 else "THAT"
                    assembly += "\n".join([
                        f"@{segment_name}",
                        "D=M"
                    ])

                case SegmentType.S_STATIC:
                    assembly += "\n".join([
                        f"@{self.__filename}.{index}",
                        "D=M"
                    ])

                case SegmentType.S_LOCAL | SegmentType.S_ARGUMENT | SegmentType.S_THIS | SegmentType.S_THAT:
                    asm_segment = VM_TO_ASM_SEGMENT[segment]
                    assembly += "\n".join([
                        f"@{index}",
                        "D=A",
                        f"@{asm_segment}",
                        "A=D+M",
                        "D=M"
                    ])

            #adds a newline to separate instructions
            assembly += "\n"

            #common push assembly sequence for updating and then incrementing the stack pointer
            assembly += CodeWriter.__ASM_PUSH_UPDATE_SP

        elif instruction_type == CommandType.C_POP:
            
            #adds a debugging comment
            assembly = f"// pop {segment.value} {index}\n"

            match segment:
                case SegmentType.S_TEMP:
                    assembly += "\n".join([
                        CodeWriter.__ASM_POP_UPDATE_SP,
                        f"@R{5 + index}",
                        "M=D"
                    ])

                case SegmentType.S_POINTER:
                    segment_name = "THIS" if index == 0 else "THAT"
                    assembly += "\n".join([
                        CodeWriter.__ASM_POP_UPDATE_SP,
                        f"@{segment_name}",
                        "M=D",
                    ])

                case SegmentType.S_STATIC:
                    assembly += "\n".join([
                        CodeWriter.__ASM_POP_UPDATE_SP,
                        f"@{self.__filename}.{index}",
                        "M=D",
                    ])

                case SegmentType.S_LOCAL | SegmentType.S_ARGUMENT | SegmentType.S_THIS | SegmentType.S_THAT:
                    asm_segment = VM_TO_ASM_SEGMENT[segment]
                    assembly += "\n".join([
                        f"@{index}",
                        "D=A",
                        f"@{asm_segment}",
                        "D=D+M",
                        "@R13",
                        "M=D",
                        CodeWriter.__ASM_POP_UPDATE_SP,
                        "@R13",
                        "A=M",
                        "M=D"
                    ])

        # adds a newline to separate instructions
        assembly += "\n"

        # writes the translated instruction
        self.__saveInstruction(assembly)        
    
    def writeArithmetic(self, operator: OperatorType):

        assembly = f"// {operator.value}\n"

        ASM_MATH_UPDATE_SP = "\n".join([
            CodeWriter.__ASM_POP_UPDATE_SP,
            "A=A-1"
        ])

        match operator:
            case OperatorType.O_ADD:
                assembly += "\n".join([
                    ASM_MATH_UPDATE_SP,
                    "M=D+M"
                ])
            case OperatorType.O_SUB:
                assembly += "\n".join([
                    ASM_MATH_UPDATE_SP,
                    "M=M-D"
                ])
            case OperatorType.O_AND:
                assembly += "\n".join([
                    ASM_MATH_UPDATE_SP,
                    "M=D&M"
                ])
            case OperatorType.O_OR:
                assembly += "\n".join([
                    ASM_MATH_UPDATE_SP,
                    "M=D|M"
                ])
            case OperatorType.O_NEG:
                assembly += "\n".join([
                    "@SP",
                    "A=M-1",
                    "M=-M"
                ])
            case OperatorType.O_NOT:
                assembly += "\n".join([
                    "@SP",
                    "A=M-1",
                    "M=!M"
                ])
            case OperatorType.O_EQ | OperatorType.O_LT | OperatorType.O_GT:

                OPERATOR_JUMP_MATCH = { 
                    "eq": "D;JNE",
                    "lt": "D;JGE",
                    "gt": "D;JLE"
                }

                assembly += "\n".join([
                    ASM_MATH_UPDATE_SP,
                    "D=M-D",
                    "M=0",
                    f"@END_{operator.value.upper()}_{self.__filename}.{self.__label_map["math"]}",
                    OPERATOR_JUMP_MATCH[operator.value],
                    "@SP",
                    "A=M-1",
                    "M=-1",
                    f"(END_{operator.value.upper()}_{self.__filename}.{self.__label_map["math"]})"
                ])

                self.__label_map["math"] += 1

        # adds newline to separate instructions
        assembly += "\n"

        self.__saveInstruction(assembly)       

    def writeLabel(self, label: str):

        label = f"{self.__filename}.{self.__current_function}${label}"

        assembly = f"// label {label}\n"
        assembly += f"({label})"
        assembly += "\n"

        self.__saveInstruction(assembly)

    def writeGoto(self, label: str):

        label = f"{self.__filename}.{self.__current_function}${label}"        

        assembly= f"// goto {label}\n"
        assembly += "\n".join([
            f"@{label}",
            "0;JMP"
        ])
        assembly += "\n"

        self.__saveInstruction(assembly)

    def writeIf(self, label: str):

        label = f"{self.__filename}.{self.__current_function}${label}"

        ASM_IF_UPDATE_SP = CodeWriter.__ASM_POP_UPDATE_SP
        assembly = f"// if-goto {label}\n"
        assembly += "\n".join([
            ASM_IF_UPDATE_SP,
            f"@{label}",
            "D;JNE"
        ])
        assembly += "\n"

        self.__saveInstruction(assembly)

    def writeFunction(self, functionName: str, nVars: int):

        # checks whether the current function context has changed 
        if functionName != self.__current_function:
            self.__current_function = functionName

        ASM_FUNCTION_PUSH_CONST = "\n".join([
            "@0",
            "D=A",
            CodeWriter.__ASM_PUSH_UPDATE_SP
        ])
        assembly = f"// function {functionName} {nVars}\n"
        assembly += "\n".join([
            f"({functionName})",
            "\n".join([ASM_FUNCTION_PUSH_CONST for _ in range(nVars)])
        ])
        assembly += "\n"

        self.__saveInstruction(assembly)
    
    def writeCall(self, functionName: str, nArgs: int):
        
        function_return_label = f"{functionName}$ret.{self.__label_map["call"]}"
        self.__label_map["call"] += 1

        args= [
            function_return_label, "LCL", "ARG", "THIS", "THAT"
        ]

        assembly = f"// call {functionName} {nArgs}\n"
        # push each argument onto the stack
        for arg in args:
            assembly += "\n".join([
                f"@{arg}",
                "D=M",
                CodeWriter.__ASM_PUSH_UPDATE_SP
            ])
            assembly += "\n"
        # move ARG to the first passed argument's position
        assembly += "\n".join([
            "@5",
            "D=A",
            f"@{nArgs}",
            "D=D-A",
            "@SP",
            "D=M-D",
            "@ARG",
            "M=D",
            "@SP",
            "D=M",
            "@LCL",
            "M=D",
            f"@{functionName}",
            "0;JMP",
            f"({function_return_label})"
        ])
        assembly += "\n"

        self.__saveInstruction(assembly)
    
    def writeReturn(self):

        frame_label = f"@frame_{self.__filename}.{self.__current_function}_{self.__label_map["frame"]}"
        return_label = f"@retAddr_{self.__filename}.{self.__current_function}_{self.__label_map["return"]}"

        # pop argument 0
        assembly = "\n".join([
            "// return",
            "@LCL",
            "D=M",
            frame_label,
            "M=D",
            "@5",
            "A=D-A",
            "D=M",
            return_label,
            "M=D",
            "@0",
            "D=A",
            "@ARG",
            "D=D+M",
            "@R13",
            "M=D",
            CodeWriter.__ASM_POP_UPDATE_SP,
            "@R13",
            "A=M",
            "M=D",
        ])
        assembly += "\n"

        # SP = RAM[ARG] + 1
        assembly += "\n".join([
            "@ARG",
            "D=M",
            "@SP",
            "M=D+1",
        ])
        assembly += "\n"
        
        # THIS/THAT/ARG/LCL = RAM[--FRAME]
        args = ["THAT", "THIS", "ARG", "LCL"]
        for arg in args:
            assembly+="\n".join([
                frame_label,
                "AM=M-1",
                "D=M",
                f"@{arg}",
                "M=D",
            ])
            assembly += "\n"

        # GOTO RAM[RETADDR]
        assembly += "\n".join([
            return_label,
            "A=M",
            "0;JMP"
        ])
        assembly += "\n"

        self.__label_map["frame"] += 1
        self.__label_map["return"] += 1

        self.__saveInstruction(assembly)
    
    #writes common end loop for Hack Machine assembly program
    def writeEndLoop(self):
        endLoop =  "\n".join([
                    "(END)",
                    "@END", 
                    "0;JMP"
                    ])
    
        self.__saveInstruction(assembly=endLoop)
            
    #appends the assembly instruction at the end of the file
    def __saveInstruction(self, assembly):
        with open(self.__output_path, "a", encoding="utf-8") as file:
            file.write(assembly)