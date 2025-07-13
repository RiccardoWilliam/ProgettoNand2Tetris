// function Sys.init 0
(Sys.init)
// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// call Sys.main 0
// push Sys.main$ret.0
@Sys.main$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = RAM[SP] - 5 - nArgs
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto Sys.main
@Sys.main
0;JMP
(Sys.main$ret.0)
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// label Sys.init$LOOP
(Sys.init$LOOP)
// goto Sys.init$LOOP
@Sys.init$LOOP
0;JMP
// function Sys.main 5
(Sys.main)
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 1
@1
D=A
@LCL
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 2
@2
D=A
@LCL
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 3
@3
D=A
@LCL
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Sys.add12 1
// push Sys.add12$ret.1
@Sys.add12$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = RAM[SP] - 5 - nArgs
@5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto Sys.add12
@Sys.add12
0;JMP
(Sys.add12$ret.1)
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 4
@4
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// return
// RAM[FRAME] = LCL
@LCL
D=M
@FRAME_Sys.main_0
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Sys.main_0
M=D
// pop argument 0
@ARG
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = RAM[--FRAME]
@FRAME_Sys.main_0
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Sys.main_0
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Sys.main_0
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Sys.main_0
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Sys.main_0
A=M
0;JMP
// function Sys.add12 0
(Sys.add12)
// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 12
@12
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// return
// RAM[FRAME] = LCL
@LCL
D=M
@FRAME_Sys.add12_1
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Sys.add12_1
M=D
// pop argument 0
@ARG
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = RAM[--FRAME]
@FRAME_Sys.add12_1
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Sys.add12_1
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Sys.add12_1
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Sys.add12_1
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Sys.add12_1
A=M
0;JMP
(END)
@END
0;JMP
