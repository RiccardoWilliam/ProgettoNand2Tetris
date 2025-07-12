import argparse
from pathlib import Path
from Parser import Parser
from CodeWriter import CodeWriter
from VMexceptions import *
from VMenums import *

# add multi-file translation
class VMtranslator:
    def __init__(self, source, output_dir, debug: bool = False):
        source = Path(source)
        output_dir = Path(output_dir)

        if source.suffix != ".vm" and not source.is_dir():
            raise VMFileError("Input file isn't a .vm file nor a folder")

        # makes an output .asm file's name the same as the source's
        output_path = output_dir / source.with_suffix('.asm').name

        self.__parser = Parser(source)
        self.__code_writer = CodeWriter(output_path)

        self.__debug = debug

    def next(self):
        self.__parser.advance()

    def hasMoreLines(self):
        return self.__parser.hasMoreLines()

    def writeEndLoop(self):
        self.__code_writer.writeEndLoop()
    
    def writeBootstrapCode(self):
        self.__code_writer.writeBootstrapCode()

    def __currentInstruction(self):
        return self.__parser.currentInstruction()
    
    def __arg1(self):
        return self.__parser.arg1()
    
    def __arg2(self):
        return self.__parser.arg2()

    def writeInstruction(self):
        command = CommandType(self.__parser.commandType())

        match command:
            case CommandType.C_PUSH | CommandType.C_POP:

                segment = SegmentType(self.__arg1())
                index = int(self.__arg2())
                self.__code_writer.writePushPop(command, segment, index)

            case CommandType.C_ARITHMETIC:
                
                operator = OperatorType(self.__arg1())
                self.__code_writer.writeArithmetic(operator)

            case CommandType.C_LABEL:

                label = self.__arg1()
                self.__code_writer.writeLabel(label)
            
            case CommandType.C_GOTO:

                label = self.__arg1()
                self.__code_writer.writeGoto(label)
            
            case CommandType.C_IF:

                label = self.__arg1()
                self.__code_writer.writeIf(label)
            
            case CommandType.C_FUNCTION:

                functionName = self.__arg1()
                nVars = int(self.__arg2())

                self.__code_writer.writeFunction(functionName, nVars)

            case CommandType.C_CALL:

                functionName = self.__arg1()
                nArgs = int(self.__arg2())

                self.__code_writer.writeCall(functionName, nArgs)
            
            case CommandType.C_RETURN:

                self.__code_writer.writeReturn()

        if self.__debug:
            print(f"// {self.__currentInstruction()}")

if __name__ == "__main__":
    argParser = argparse.ArgumentParser(description="VM to Hack Assembly Translator")
    argParser.add_argument("input_file", help="Path to .vm input file")
    argParser.add_argument("output_dir", help="Output directory for .asm file")
    argParser.add_argument("--debug", action="store_true", help="Enable debug mode")

    args = argParser.parse_args()

    translator = VMtranslator(args.input_file, args.output_dir, args.debug)

    # translator.writeBootstrapCode()
    while translator.hasMoreLines():
        translator.next()
        translator.writeInstruction()
    translator.writeEndLoop()

    print("Translation completed")
