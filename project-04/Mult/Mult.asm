// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//inizializza sum con 0
@sum
M=0
//inizializza i con il valore di R1
@R1
D=M
@i
M=D
//while label
(WHILE)
@i
D=M
//if i==0 goto END
@END 
D;JEQ
//else
@R0
D=M
//sum = sum + R0
@sum
M=D+M
//i = i - 1
@i
M=M-1
//goto WHILE
@WHILE
0;JMP
(END)
//R2 = sum
@sum
D=M
@R2
M=D
//exit
@END
0;JMP



