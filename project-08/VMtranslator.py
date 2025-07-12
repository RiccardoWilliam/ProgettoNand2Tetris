import argparse
from pathlib import Path
from Parser import Parser
from CodeWriter import CodeWriter
from VMexceptions import *
from VMenums import *

class VMtranslator:
    def __init__(self, source, output_dir, debug: bool = False):
        self.__source = Path(source)
        output_dir = Path(output_dir)
        self.__debug = debug

        if self.__source.suffix != ".vm" and not self.__source.is_dir():
            raise VMFileError("Input file isn't a .vm file nor a folder")

        # Nome del file .asm finale
        self.__output_path = output_dir / self.__source.with_suffix('.asm').name
        self.__code_writer = CodeWriter(self.__output_path)
    
    def translate(self):
        if self.__source.is_file():
            self.__translate_file(self.__source)
            self.__code_writer.writeEndLoop()
        else:
            self.__code_writer.writeBootstrapCode()
            vm_files = self.__source.glob("*.vm")
            for vm_file in vm_files:
                self.__translate_file(vm_file)
        

    def __translate_file(self, filepath: Path):
        parser = Parser(filepath)
        self.__code_writer.setFileName(filepath.stem) 

        while parser.hasMoreLines():
            parser.advance()
            command = CommandType(parser.commandType())

            if self.__debug:
                print(f"// {parser.currentInstruction()}")

            match command:
                case CommandType.C_PUSH | CommandType.C_POP:
                    segment = SegmentType(parser.arg1())
                    index = int(parser.arg2())
                    self.__code_writer.writePushPop(command, segment, index)

                case CommandType.C_ARITHMETIC:
                    operator = OperatorType(parser.arg1())
                    self.__code_writer.writeArithmetic(operator)

                case CommandType.C_LABEL:
                    label = parser.arg1()
                    self.__code_writer.writeLabel(label)

                case CommandType.C_GOTO:
                    label = parser.arg1()
                    self.__code_writer.writeGoto(label)

                case CommandType.C_IF:
                    label = parser.arg1()
                    self.__code_writer.writeIf(label)

                case CommandType.C_FUNCTION:
                    functionName = parser.arg1()
                    nVars = int(parser.arg2())
                    self.__code_writer.writeFunction(functionName, nVars)

                case CommandType.C_CALL:
                    functionName = parser.arg1()
                    nArgs = int(parser.arg2())
                    self.__code_writer.writeCall(functionName, nArgs)

                case CommandType.C_RETURN:
                    self.__code_writer.writeReturn()


if __name__ == "__main__":
    argParser = argparse.ArgumentParser(description="VM to Hack Assembly Translator")
    argParser.add_argument("input_file", help="Path to .vm file or folder")
    argParser.add_argument("output_dir", help="Output directory for .asm file")
    argParser.add_argument("--debug", action="store_true", help="Enable debug mode")

    args = argParser.parse_args()

    translator = VMtranslator(args.input_file, args.output_dir, args.debug)
    translator.translate()

    print("Translation completed")
