// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//screen is composed of 256 rows of 512 pixels each and so each row is 
//composed of 32 DWORDs, meaning that the screen totals to 255*32=8192 DWORDs 

(MAIN)
    @KBD
    D=M
    //if
    @ELSE
    D;JNE
    //function call
    @parameter
    M=-1
    @FILL
    0;JMP
//else
(ELSE)
    //function call
    @parameter
    M=0
    @FILL
    0;JMP
    
//fill function
(FILL)
    @i
    M=0
(FOR)
    @i
    D=M
    @SCREEN
    D=D+A //saves row_address in D
    @row_address
    M=D //saves row_address in a variable
    @parameter 
    D=M //select parameter 
    @row_address
    A=M //goes to row_address
    M=D //change row's value
    @i  
    MD=M+1 //increments i
    @8192
    D=A-D  //8192-i
    @MAIN
    D;JEQ
    @FOR
    0;JMP

    





