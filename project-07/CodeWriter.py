from pathlib import Path
from VMenums import *
from VMexceptions import *

class CodeWriter:

    ASM_POP_UPDATE_SP = "\n".join([
        "@SP",
        "AM=M-1",
        "D=M"
    ])

    #hashmap for VM segments to assembly segments correspondance
    __VM_TO_ASM_SEGMENT = {
        SegmentType.S_THIS: "THIS",
        SegmentType.S_THAT: "THAT",
        SegmentType.S_LOCAL: "LCL",
        SegmentType.S_ARGUMENT: "ARG"
    }

    def __init__(self, path: Path):
        self.__output_path = path
        self.__filename = path.stem
        self.__label_count = 0

        # Clear old file content
        open(self.__output_path, "w").close()

    def writePushPop(self, instruction_type: CommandType, segment: SegmentType, index: int):

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
                    asm_segment = CodeWriter.__VM_TO_ASM_SEGMENT[segment]
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
            assembly += "\n".join(["@SP", "A=M", "M=D", "@SP", "M=M+1"])

        elif instruction_type == CommandType.C_POP:
            
            #adds a debugging comment
            assembly = f"// pop {segment.value} {index}\n"

            match segment:
                case SegmentType.S_TEMP:
                    assembly += "\n".join([
                        CodeWriter.ASM_POP_UPDATE_SP,
                        f"@R{5 + index}",
                        "M=D"
                    ])

                case SegmentType.S_POINTER:
                    segment_name = "THIS" if index == 0 else "THAT"
                    assembly += "\n".join([
                        CodeWriter.ASM_POP_UPDATE_SP,
                        f"@{segment_name}",
                        "M=D",
                    ])

                case SegmentType.S_STATIC:
                    assembly += "\n".join([
                        CodeWriter.ASM_POP_UPDATE_SP,
                        f"@{self.__filename}.{index}",
                        "M=D",
                    ])

                case SegmentType.S_LOCAL | SegmentType.S_ARGUMENT | SegmentType.S_THIS | SegmentType.S_THAT:
                    asm_segment = CodeWriter.__VM_TO_ASM_SEGMENT[segment]
                    assembly += "\n".join([
                        f"@{index}",
                        "D=A",
                        f"@{asm_segment}",
                        "D=D+M",
                        "@R13",
                        "M=D",
                        CodeWriter.ASM_POP_UPDATE_SP,
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
            CodeWriter.ASM_POP_UPDATE_SP,
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
                assembly += "\n".join([
                    ASM_MATH_UPDATE_SP,
                    "D=M-D",
                    "M=0",
                    f"@END_{operator.value.upper()}_{self.__filename}.{self.__label_count}",
                    "D;JNE",
                    "@SP",
                    "A=M-1",
                    "M=-1",
                    f"(END_{operator.value.upper()}_{self.__filename}.{self.__label_count})"
                ])

                self.__label_count += 1

        # adds newline to separate instructions
        assembly += "\n"

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