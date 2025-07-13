// function SimpleFunction.test 2
(SimpleFunction.test)
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
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// not
@SP
A=M-1
M=!M
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
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// push argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// return
// RAM[FRAME] = LCL
@LCL
D=M
@FRAME_SimpleFunction.test_0
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_SimpleFunction.test_0
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
@FRAME_SimpleFunction.test_0
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_SimpleFunction.test_0
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_SimpleFunction.test_0
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_SimpleFunction.test_0
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_SimpleFunction.test_0
A=M
0;JMP
(END)
@END
0;JMP
