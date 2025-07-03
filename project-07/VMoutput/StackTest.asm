// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
<<<<<<< HEAD
@END_EQ_StackTest.0
=======
@END_EQ_0
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JNE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_EQ_StackTest.0)
=======
(END_EQ_0)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
<<<<<<< HEAD
@END_EQ_StackTest.1
=======
@END_EQ_1
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JNE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_EQ_StackTest.1)
=======
(END_EQ_1)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
<<<<<<< HEAD
@END_EQ_StackTest.2
=======
@END_EQ_2
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JNE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_EQ_StackTest.2)
=======
(END_EQ_2)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
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
<<<<<<< HEAD
@END_LT_StackTest.3
=======
@END_LT_3
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JGE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_LT_StackTest.3)
=======
(END_LT_3)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
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
<<<<<<< HEAD
@END_LT_StackTest.4
=======
@END_LT_4
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JGE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_LT_StackTest.4)
=======
(END_LT_4)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
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
<<<<<<< HEAD
@END_LT_StackTest.5
=======
@END_LT_5
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JGE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_LT_StackTest.5)
=======
(END_LT_5)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
<<<<<<< HEAD
@END_GT_StackTest.6
=======
@END_GT_6
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JLE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_GT_StackTest.6)
=======
(END_GT_6)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
<<<<<<< HEAD
@END_GT_StackTest.7
=======
@END_GT_7
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JLE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_GT_StackTest.7)
=======
(END_GT_7)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
<<<<<<< HEAD
@END_GT_StackTest.8
=======
@END_GT_8
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
D;JLE
@SP
A=M-1
M=-1
<<<<<<< HEAD
(END_GT_StackTest.8)
=======
(END_GT_8)
>>>>>>> 9f2a03e89405598df3b5d1d8f38781e2e5895217
// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 53
@53
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
// push constant 112
@112
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
// neg
@SP
A=M-1
M=-M
// and
@SP
AM=M-1
D=M
A=A-1
M=D&M
// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
AM=M-1
D=M
A=A-1
M=D|M
// not
@SP
A=M-1
M=!M
(END)
@END
0;JMP