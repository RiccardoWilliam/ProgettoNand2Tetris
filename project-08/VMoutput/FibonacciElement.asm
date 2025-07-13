// bootstrap code
@256
D=A
@SP
M=D
// call Sys.init 0
// push Sys.init$ret.0
@Sys.init$ret.0
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
// goto Sys.init
@Sys.init
0;JMP
(Sys.init$ret.0)
// function Main.fibonacci 0
(Main.fibonacci)
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
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@END_LT_Main.fibonacci.0
D;JGE
@SP
A=M-1
M=-1
(END_LT_Main.fibonacci.0)
// if-goto Main.fibonacci$N_LT_2
@SP
AM=M-1
D=M
@Main.fibonacci$N_LT_2
D;JNE
// goto Main.fibonacci$N_GE_2
@Main.fibonacci$N_GE_2
0;JMP
// label Main.fibonacci$N_LT_2
(Main.fibonacci$N_LT_2)
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
// return
// RAM[FRAME] = LCL
@LCL
D=M
@FRAME_Main.fibonacci_0
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Main.fibonacci_0
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
@FRAME_Main.fibonacci_0
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Main.fibonacci_0
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Main.fibonacci_0
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Main.fibonacci_0
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Main.fibonacci_0
A=M
0;JMP
// label Main.fibonacci$N_GE_2
(Main.fibonacci$N_GE_2)
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
// push constant 2
@2
D=A
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
// call Main.fibonacci 1
// push Main.fibonacci$ret.1
@Main.fibonacci$ret.1
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
// goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)
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
// push constant 1
@1
D=A
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
// call Main.fibonacci 1
// push Main.fibonacci$ret.2
@Main.fibonacci$ret.2
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
// goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)
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
@FRAME_Main.fibonacci_1
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Main.fibonacci_1
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
@FRAME_Main.fibonacci_1
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Main.fibonacci_1
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Main.fibonacci_1
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Main.fibonacci_1
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Main.fibonacci_1
A=M
0;JMP
// function Sys.init 0
(Sys.init)
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
// push Main.fibonacci$ret.3
@Main.fibonacci$ret.3
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
// goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)
// label Sys.init$END
(Sys.init$END)
// goto Sys.init$END
@Sys.init$END
0;JMP
