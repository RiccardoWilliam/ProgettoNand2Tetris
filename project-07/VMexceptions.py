from pathlib import Path

#Base exception for VM-related errors
class VMError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

#Raised for errors related to file reading or file content
class VMFileError(VMError):
    def __init__(self, message: str, path: Path | None = None):
        if path:
            full_message = f"File error in '{path}': {message}"
        else:
            full_message = f"File error: {message}"
        super().__init__(full_message)

#Raised for errors in instruction format or type
class VMInstructionError(VMError):
    def __init__(self, message: str, instruction: str, line_number: int):
        full_message = f"[Line {line_number}] Instruction error: {message}\n  → {instruction}"
        super().__init__(full_message)

#Raised for segment issues in push/pop instructions
class VMSegmentError(VMError):
    def __init__(self, message: str, line_number: int, instruction: str):
        full_message = f"[Line {line_number}] Segment error: {message}\n  → {instruction}"
        super().__init__(full_message)
