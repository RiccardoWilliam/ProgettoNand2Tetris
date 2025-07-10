import argparse
from pathlib import Path
from Parser import Parser
from CodeWriter import CodeWriter
from VMexceptions import *
from VMenums import *

class VMtranslator:
    def __init__(self, input_file, output_dir, debug: bool = False):
        input_file = Path(input_file)
        output_dir = Path(output_dir)

        if input_file.suffix != ".vm":
            raise VMFileError("Input file isn't a .vm file")

        if not input_file.exists() or not input_file.is_file():
            raise VMFileError("Invalid input file")
        
        if not output_dir.exists() or not output_dir.is_dir():
            raise VMFileError("Invalid output folder")

        output_path = output_dir / input_file.with_suffix('.asm').name
        self.__parser = Parser(input_file)
        self.__code_writer = CodeWriter(output_path)
        self.__debug = debug

    def next(self):
        self.__parser.advance()

    def hasMoreLines(self):
        return self.__parser.hasMoreLines()

    def writeEndLoop(self):
        self.__code_writer.writeEndLoop()

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

            case _:
                raise VMFileError("Invalid instruction")

        if self.__debug:
            print(f"// {self.__currentInstruction()}")

if __name__ == "__main__":
    argParser = argparse.ArgumentParser(description="VM to Hack Assembly Translator")
    argParser.add_argument("input_file", help="Path to .vm input file")
    argParser.add_argument("output_dir", help="Output directory for .asm file")
    argParser.add_argument("--debug", action="store_true", help="Enable debug mode")

    args = argParser.parse_args()

    translator = VMtranslator(args.input_file, args.output_dir, args.debug)

    while translator.hasMoreLines():
        translator.next()
        translator.writeInstruction()
    translator.writeEndLoop()

    print("Translation completed")
