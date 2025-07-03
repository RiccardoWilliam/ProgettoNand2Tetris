<<<<<<< HEAD
import json

class SymbolTable:
    
    def __init__(self):
        self.__table: dict[str, int] = {}
        
        for i in range(16):
            self.addEntry(f"R{i}", i)
        
        self.addEntry("SP", 0)
        self.addEntry("LCL",1)
        self.addEntry("ARG",2)
        self.addEntry("THIS",3)
        self.addEntry("THAT",4)
        self.addEntry("SCREEN",16384)
        self.addEntry("KBD",24576)
    
    def addEntry(self, symbol: str, address: int) -> None:
        self.__table[symbol] = address
    
    def contains(self, symbol: str) -> bool:
        return symbol in self.__table
    
    def getAddress(self, symbol: str) -> int:
        return self.__table[symbol]
    
    #utilities

    def printTable(self, path):
        with open(path, "wt", encoding="utf-8") as file:
=======
import json

class SymbolTable:
    
    def __init__(self):
        self.__table: dict[str, int] = {}
        
        for i in range(16):
            self.addEntry(f"R{i}", i)
        
        self.addEntry("SP", 0)
        self.addEntry("LCL",1)
        self.addEntry("ARG",2)
        self.addEntry("THIS",3)
        self.addEntry("THAT",4)
        self.addEntry("SCREEN",16384)
        self.addEntry("KBD",24576)
    
    def addEntry(self, symbol: str, address: int) -> None:
        self.__table[symbol] = address
    
    def contains(self, symbol: str) -> bool:
        return symbol in self.__table
    
    def getAddress(self, symbol: str) -> int:
        return self.__table[symbol]
    
    #utilities

    def printTable(self, path):
        with open(path, "wt", encoding="utf-8") as file:
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
            json.dump(self.__table, file, indent=4)