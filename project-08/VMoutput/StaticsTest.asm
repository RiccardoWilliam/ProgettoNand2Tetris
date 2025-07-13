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
// function Class1.set 0
(Class1.set)
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
// pop static 0
@SP
AM=M-1
D=M
@Class1.0
M=D
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
// pop static 1
@SP
AM=M-1
D=M
@Class1.1
M=D
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// return
// RAM[FRAME] = LCL
@LCL
D=M
@FRAME_Class1.set_0
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Class1.set_0
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
@FRAME_Class1.set_0
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Class1.set_0
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Class1.set_0
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Class1.set_0
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Class1.set_0
A=M
0;JMP
// function Class1.get 0
(Class1.get)
// push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@Class1.1
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
@FRAME_Class1.get_1
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Class1.get_1
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
@FRAME_Class1.get_1
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Class1.get_1
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Class1.get_1
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Class1.get_1
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Class1.get_1
A=M
0;JMP
// function Class2.set 0
(Class2.set)
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
// pop static 0
@SP
AM=M-1
D=M
@Class2.0
M=D
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
// pop static 1
@SP
AM=M-1
D=M
@Class2.1
M=D
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// return
// RAM[FRAME] = LCL
@LCL
D=M
@FRAME_Class2.set_2
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Class2.set_2
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
@FRAME_Class2.set_2
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Class2.set_2
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Class2.set_2
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Class2.set_2
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Class2.set_2
A=M
0;JMP
// function Class2.get 0
(Class2.get)
// push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@Class2.1
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
@FRAME_Class2.get_3
M=D
// RETADDR = LCL - 5
@5
A=D-A
D=M
@RETADDR_Class2.get_3
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
@FRAME_Class2.get_3
AM=M-1
D=M
@THAT
M=D
// THIS = RAM[--FRAME]
@FRAME_Class2.get_3
AM=M-1
D=M
@THIS
M=D
// ARG = RAM[--FRAME]
@FRAME_Class2.get_3
AM=M-1
D=M
@ARG
M=D
// LCL = RAM[--FRAME]
@FRAME_Class2.get_3
AM=M-1
D=M
@LCL
M=D
// goto RAM[RETADDR]
@RETADDR_Class2.get_3
A=M
0;JMP
// function Sys.init 0
(Sys.init)
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class1.set 2
// push Class1.set$ret.1
@Class1.set$ret.1
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
@2
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
// goto Class1.set
@Class1.set
0;JMP
(Class1.set$ret.1)
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class2.set 2
// push Class2.set$ret.2
@Class2.set$ret.2
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
@2
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
// goto Class2.set
@Class2.set
0;JMP
(Class2.set$ret.2)
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// call Class1.get 0
// push Class1.get$ret.3
@Class1.get$ret.3
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
// goto Class1.get
@Class1.get
0;JMP
(Class1.get$ret.3)
// call Class2.get 0
// push Class2.get$ret.4
@Class2.get$ret.4
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
// goto Class2.get
@Class2.get
0;JMP
(Class2.get$ret.4)
// label Sys.init$END
(Sys.init$END)
// goto Sys.init$END
@Sys.init$END
0;JMP
