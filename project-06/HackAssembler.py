<<<<<<< HEAD
from sys import argv
from pathlib import Path
from SymbolTable import SymbolTable
from Parser import Parser
from Translator import Translator

class Assembler:

    def __init__(self, sourceFile, outputPath):
    
        self.__filePath = Path(sourceFile)
        self.__outputFolder = Path(outputPath)

        if not self.__filePath.exists() or not self.__outputFolder.exists():
            print("il percorso non esiste")
            exit()

        if not self.__filePath.is_file() or not self.__outputFolder.is_dir():
            print("Il percorso non è un file")
            exit()

        if self.__filePath.suffix != ".asm":
            print("il file non è un file assembly")
            exit()
        
        self.__filename = self.__filePath.stem
        self.__outputFile = self.__outputFolder.joinpath(self.__filename + ".hack")

        # Clear old file content
        open(self.__outputFile, "w").close()


    def buildSymbolTable(self, table: SymbolTable, printTable=False):
        
        self.__symbolTable = table
        labelParser = Parser(self.__filePath)

        #adds label symbols inside the table
        address = 0
        while labelParser.hasMoreLines():
            labelParser.advance()

            instructionType = labelParser.instructionType
            symbol = labelParser.symbol

            if instructionType == labelParser.L_INSTRUCTION and not self.__symbolTable.contains(symbol):
                self.__symbolTable.addEntry(symbol, address)
                continue
            
            address+=1

        #adds variable symbols to the table
        variableParser = Parser(self.__filePath)

        varCount = 0
        while variableParser.hasMoreLines():

            variableParser.advance()

            instructionType = variableParser.instructionType
            symbol = variableParser.symbol

            if instructionType == variableParser.A_INSTRUCTION and not self.__symbolTable.contains(symbol) and not symbol.isdigit():
                self.__symbolTable.addEntry(symbol, 16 + varCount)
                varCount+=1
        
        if(printTable):
            self.__symbolTable.printTable("./table.json")
        
    def assemble(self, debug=False):

            parser = Parser(self.__filePath, debug)
            translator = Translator()

            while parser.hasMoreLines():

                instruction = ""

                parser.advance()

                instructionType = parser.instructionType

                if instructionType == parser.A_INSTRUCTION:
                    address = parser.symbol
                    if self.__symbolTable.contains(address):
                        address = self.__symbolTable.getAddress(address)

                    instruction = "0" + format(int(address), "015b")

                    with open(file = self.__outputFile, mode = "a", encoding="utf-8") as file:
                        file.write(instruction + "\n")
                    
                    continue
                
                if instructionType == parser.C_INSTRUCTION:
                    
                    instruction += "111"

                    dest = translator.dest(parser.dest)
                    comp = translator.comp(parser.comp)
                    jump = translator.jump(parser.jump)

                    if "M" in parser.comp:
                        instruction += "1"
                    else:
                        instruction += "0"

                    instruction += comp + dest + jump

                    with open(file = self.__outputFile, mode = "a", encoding="utf-8") as file:
                        file.write(instruction + "\n")
                    
                    continue
            
            print(f"{self.__filename} assembled and written in ./{self.__outputFile}")
                    
if len(argv) != 3:
    print("Numero di argomenti invalido: script.py \n path/to/source.asm path/to/output_folder/")
    exit()

source = argv[1]
output_folder = argv[2]

assembler = Assembler(source, output_folder)
symbolTable = SymbolTable()

assembler.buildSymbolTable(symbolTable)
=======
from sys import argv
from pathlib import Path
from SymbolTable import SymbolTable
from Parser import Parser
from Translator import Translator

class Assembler:

    def __init__(self, sourceFile, outputPath):
    
        self.__filePath = Path(sourceFile)
        self.__outputFolder = Path(outputPath)

        if not self.__filePath.exists() or not self.__outputFolder.exists():
            print("il percorso non esiste")
            exit()

        if not self.__filePath.is_file() or not self.__outputFolder.is_dir():
            print("Il percorso non è un file")
            exit()

        if self.__filePath.suffix != ".asm":
            print("il file non è un file assembly")
            exit()
        
        self.__filename = self.__filePath.stem
        self.__outputFile = self.__outputFolder.joinpath(self.__filename + ".hack")

        # Clear old file content
        open(self.__outputFile, "w").close()


    def buildSymbolTable(self, table: SymbolTable, printTable=False):
        
        self.__symbolTable = table
        labelParser = Parser(self.__filePath)

        #adds label symbols inside the table
        address = 0
        while labelParser.hasMoreLines():
            labelParser.advance()

            instructionType = labelParser.instructionType
            symbol = labelParser.symbol

            if instructionType == labelParser.L_INSTRUCTION and not self.__symbolTable.contains(symbol):
                self.__symbolTable.addEntry(symbol, address)
                continue
            
            address+=1

        #adds variable symbols to the table
        variableParser = Parser(self.__filePath)

        varCount = 0
        while variableParser.hasMoreLines():

            variableParser.advance()

            instructionType = variableParser.instructionType
            symbol = variableParser.symbol

            if instructionType == variableParser.A_INSTRUCTION and not self.__symbolTable.contains(symbol) and not symbol.isdigit():
                self.__symbolTable.addEntry(symbol, 16 + varCount)
                varCount+=1
        
        if(printTable):
            self.__symbolTable.printTable("./table.json")
        
    def assemble(self, debug=False):

            parser = Parser(self.__filePath, debug)
            translator = Translator()

            while parser.hasMoreLines():

                instruction = ""

                parser.advance()

                instructionType = parser.instructionType

                if instructionType == parser.A_INSTRUCTION:
                    address = parser.symbol
                    if self.__symbolTable.contains(address):
                        address = self.__symbolTable.getAddress(address)

                    instruction = "0" + format(int(address), "015b")

                    with open(file = self.__outputFile, mode = "a", encoding="utf-8") as file:
                        file.write(instruction + "\n")
                    
                    continue
                
                if instructionType == parser.C_INSTRUCTION:
                    
                    instruction += "111"

                    dest = translator.dest(parser.dest)
                    comp = translator.comp(parser.comp)
                    jump = translator.jump(parser.jump)

                    if "M" in parser.comp:
                        instruction += "1"
                    else:
                        instruction += "0"

                    instruction += comp + dest + jump

                    with open(file = self.__outputFile, mode = "a", encoding="utf-8") as file:
                        file.write(instruction + "\n")
                    
                    continue
            
            print(f"{self.__filename} assembled and written in ./{self.__outputFile}")
                    
if len(argv) != 3:
    print("Numero di argomenti invalido: script.py \n path/to/source.asm path/to/output_folder/")
    exit()

source = argv[1]
output_folder = argv[2]

assembler = Assembler(source, output_folder)
symbolTable = SymbolTable()

assembler.buildSymbolTable(symbolTable)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
assembler.assemble()