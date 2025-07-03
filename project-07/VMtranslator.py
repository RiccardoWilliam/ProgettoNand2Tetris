import argparse
from pathlib import Path
from Parser import Parser, CommandType
from CodeWriter import CodeWriter

class VMtranslator:
    def __init__(self, input_file, output_dir, debug: bool = False):
        input_file = Path(input_file)
        output_dir = Path(output_dir)

        if input_file.suffix != ".vm":
            print("Input file isn't a .vm file")
            exit()

        if not input_file.exists() or not input_file.is_file():
            print("Invalid input file")
            exit()

        if not output_dir.exists() or not output_dir.is_dir():
            print("Invalid output folder")
            exit()

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

    @property
    def currentInstruction(self):
        return self.__parser.currentInstruction

    def writeInstruction(self):
        instruction_type = self.__parser.commandType
        instruction_arg1 = self.__parser.arg1
        instruction_arg2 = self.__parser.arg2

        match instruction_type:
            case CommandType.C_PUSH | CommandType.C_POP:
                self.__code_writer.writePushPop(instruction_type, instruction_arg1, instruction_arg2)
            case CommandType.C_ARITHMETIC:
                self.__code_writer.writeArithmetic(self.__parser.arg0)
            case _:
                print(f"// Istruzione non riconosciuta: {instruction_type}")

        if self.__debug:
            print(f"// {self.currentInstruction}")

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
