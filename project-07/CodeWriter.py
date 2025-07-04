from pathlib import Path
from VMenums import *

class CodeWriter:

    __VM_TO_ASM_SEGMENT = {
        SegmentType.S_THIS: "THIS",
        SegmentType.S_THAT: "THAT",
        SegmentType.S_LOCAL: "LCL",
        SegmentType.S_ARGUMENT: "ARG"
    }

    __PUSH_STORE_ASM_INST = "\n".join(["@SP", "A=M", "M=D", "@SP", "M=M+1"])
    __POP_LOAD_ASM_INST = "\n".join(["@SP","AM=M-1","D=M"])

    def __init__(self, path: Path):
        self.__output_path = path
        self.__filename = path.stem
        self.__label_count = 0

        # Clear old file content
        open(self.__output_path, "w").close()

    def writePushPop(self, instruction_type: str, segment: SegmentType, index: int):

        assembly = ""

        if instruction_type == CommandType.C_PUSH:
            assembly = f"// push {segment.value} {index}\n"
            assembly += self.__pushFetchString(segment, index) + "\n"
            assembly += CodeWriter.__PUSH_STORE_ASM_INST

        elif instruction_type == CommandType.C_POP:
            assembly = f"// pop {segment.value} {index}\n"
            assembly += self.__popFetchString(segment, index)

        assembly += "\n"

        with open(self.__output_path, "a", encoding="utf-8") as file:
            file.write(assembly)
    
    def writeArithmetic(self, operator: OperatorType):

        assembly = f"// {operator.value}\n"

        match operator:
            case OperatorType.O_ADD:
                assembly += "\n".join([
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "A=A-1",
                    "M=D+M"
                ])
            case OperatorType.O_SUB:
                assembly += "\n".join([
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "A=A-1",
                    "M=M-D"
                ])
            case OperatorType.O_AND:
                assembly += "\n".join([
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "A=A-1",
                    "M=D&M"
                ])
            case OperatorType.O_OR:
                assembly += "\n".join([
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "A=A-1",
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
            case OperatorType.O_EQ:
                assembly += "\n".join([
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "A=A-1",
                    "D=M-D",
                    "M=0",
                    f"@END_EQ_{self.__filename}.{self.__label_count}",
                    "D;JNE",
                    "@SP",
                    "A=M-1",
                    "M=-1",
                    f"(END_EQ_{self.__filename}.{self.__label_count})"
                ])
            case OperatorType.O_LT:
                assembly += "\n".join([
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "A=A-1",
                    "D=M-D",
                    "M=0",
                    f"@END_LT_{self.__filename}.{self.__label_count}",
                    "D;JGE",
                    "@SP",
                    "A=M-1",
                    "M=-1",
                    f"(END_LT_{self.__filename}.{self.__label_count})"
                ])
            case OperatorType.O_GT:
                assembly += "\n".join([
                    "@SP",
                    "AM=M-1",
                    "D=M",
                    "A=A-1",
                    "D=M-D",
                    "M=0",
                    f"@END_GT_{self.__filename}.{self.__label_count}",
                    "D;JLE",
                    "@SP",
                    "A=M-1",
                    "M=-1",
                    f"(END_GT_{self.__filename}.{self.__label_count})"
                ])
        self.__label_count += 1
        assembly += "\n"

        with open(self.__output_path, "a", encoding="utf-8") as file:
            file.write(assembly)

    def __pushFetchString(self, segment, index):
        match segment:
            case SegmentType.S_CONSTANT:
                return "\n".join([
                    f"@{index}",
                    "D=A"
                ])

            case SegmentType.S_TEMP:
                if index > 7:
                    print("Invalid temp segment index")
                    exit()
                return "\n".join([
                    f"@R{5 + index}",
                    "D=M"
                ])

            case SegmentType.S_POINTER:
                if index > 1:
                    print("Invalid pointer index")
                    exit()
                segment_name = "THIS" if index == 0 else "THAT"
                return "\n".join([
                    f"@{segment_name}",
                    "D=M"
                ])

            case SegmentType.S_STATIC:
                return "\n".join([
                    f"@{self.__filename}.{index}",
                    "D=M"
                ])

            case SegmentType.S_LOCAL | SegmentType.S_ARGUMENT | SegmentType.S_THIS | SegmentType.S_THAT:
                asm_segment = CodeWriter.__VM_TO_ASM_SEGMENT[segment]
                return "\n".join([
                    f"@{index}",
                    "D=A",
                    f"@{asm_segment}",
                    "A=D+M",
                    "D=M"
                ])

            case _:
                print(f"Invalid segment: {segment} for push instruction")
                print(f"Instruction: push {segment} {index}")
                exit()
    
    def __popFetchString(self, segment, index):
        
        match segment:
            case SegmentType.S_TEMP:
                if index > 7:
                    print("Invalid temp segment index")
                    exit()
                return "\n".join([
                    CodeWriter.__POP_LOAD_ASM_INST,
                    f"@R{5 + index}",
                    "M=D"
                ])

            case SegmentType.S_POINTER:
                if index > 1:
                    print("Invalid pointer index")
                    exit()
                segment_name = "THIS" if index == 0 else "THAT"
                return "\n".join([
                    CodeWriter.__POP_LOAD_ASM_INST,
                    f"@{segment_name}",
                    "M=D",
                ])

            case SegmentType.S_STATIC:
                return "\n".join([
                    CodeWriter.__POP_LOAD_ASM_INST,
                    f"@{self.__filename}.{index}",
                    "M=D",
                ])

            case SegmentType.S_LOCAL | SegmentType.S_ARGUMENT | SegmentType.S_THIS | SegmentType.S_THAT:
                asm_segment = CodeWriter.__VM_TO_ASM_SEGMENT[segment]
                return "\n".join([
                    f"@{index}",
                    "D=A",
                    f"@{asm_segment}",
                    "D=D+M",
                    "@R13",
                    "M=D",
                    CodeWriter.__POP_LOAD_ASM_INST,
                    "@R13",
                    "A=M",
                    "M=D"
                ])

            case _:
                print(f"Invalid segment: {segment} for pop instruction")
                print(f"Instruction: pop {segment} {index}")
                exit()

    def writeEndLoop(self):
        with open(self.__output_path, "a", encoding="utf-8") as file:
            file.write("\n".join([
                    "(END)",
                    "@END", 
                    "0;JMP"
                    ]))
    