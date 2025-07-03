from enum import Enum

class CommandType(Enum):
    C_ARITHMETIC = "C_ARITHMETIC" #mono
    C_PUSH = "C_PUSH" #triple
    C_POP = "C_POP" #triple
    C_LABEL = "C_LABEL" #double
    C_GOTO = "C_GOTO" #double
    C_IF = "C_IF" #double
    C_FUNCTION = "C_FUNCTION" #triple
    C_RETURN = "C_RETURN" #mono
    C_CALL = "C_CALL" #triple

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
