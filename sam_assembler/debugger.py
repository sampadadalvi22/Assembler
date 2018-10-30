#!/usr/bin/env python3
from symboltable import *
from literaltable import *
from finalLst import *
from finalObj import *
from smaco import *
from sys import argv
import sys

display=[]
pcnt=1

if not os.path.exists(".symbol_table.txt"):
    open(".symbol_table.txt","w").close()

if not os.path.exists(".literal_table.txt"):
    open(".literal_table.txt","w").close()

def help_call():
    print("List of classes of commands:")
    print("'h' or 'hlep'  --help for debugger instructions")
    print("'ni' or 'next' --execute the next instruction")
    print("'q' or 'quit'  --quit out of gdb ")
    print("'list'         --display source code")
    print("'info reg'     --display all register information")
    print("'display $reg' --display always $reg  information")
    print("'print/d $reg' --display $reg  values in decimal")
    print("'print/h $reg' --display $reg  values in hexdecimal")
    print("'print/b $reg' --display $reg  values in binary")
    print("'run'          --start the debugging program \n")
    return
    

def quit_call():
    q=input("You Want Quit it ? (y or n)")
    if q=='y':
        exit()
    if q=='n':
        return
    if q not in ['y','n']:
        print("Please answer y or n.")
        quit_call()
    
def list_call():
    for i in range(len(op_val)):
        print(op_val[i][0],'\t',op_val[i][3])

    return

def display_call(reg):
    rval=0
    val=reg.replace('$','')
    display.append(str(val))
    for j in range(len(final)):
        if final[j]==val:
            rval=(final[j-1])
    for i in range(len(display)):
        if display[i]==val:
            print(i+1,": ",reg,"=",rval)
    return

def print_decimal(reg):
    global pcnt
    rval=0
    val=reg.replace('$','')
    for i in range(len(final)):
        if final[i]==val:
            print("$",pcnt,":",val,"=",final[i-1])
            pcnt+=1

def print_hex(reg):
    global pcnt
    rval=0
    val=reg.replace('$','')
    for i in range(len(final)):
        if final[i]==val:
            print("$",pcnt,":",val,"=",hex(int(final[i-1])))
            pcnt+=1

def print_binary(reg):
    global pcnt
    rval=0
    val=reg.replace('$','')
    for i in range(len(final)):
        if final[i]==val:
            print("$",pcnt,":",val,"=",bin(int(final[i-1])))
            pcnt+=1
            
def display_reg():
    if display!=[]:
        for i in range(len(display)):
            reg=display[i]
            for j in range(len(final)):
                if final[j]==reg:
                    print(i+1,":",reg,"=",final[j-1])
                   

def info_reg_call():
    cnt=1
    for i in range(33,len(final),2):
        print(cnt,":",final[i],"= ",final[i-1])
        cnt+=1
    return


def start_deb():
    cnt=0
    n=len(op_txt)
    print("Breakpoint 1, 0x08048400 in main ()")
    while cnt<n:
       
        sp=input("(gdb)")
        sk=sp.split()
        
        if sp=='ni' or sp=='next' or sp=='n':
            decode_opcode(op_txt[cnt][2])
            print(op_txt[cnt][0],":",op_txt[cnt][3])
            display_reg()
            cnt+=1

        if sp=='run':
            print("The program being debugged has been started already.")
            e=input("Start it from the beginning? (y or n)")
            if e=='y':
                start_deb()
            if e=='n':
                return
                           
        if sp=='q' or sp=='quit':
            quit_call()

        if sp=='list':
            list_call()

        if sk[0]=='display':
            display_call(sk[1])

        if sp=='info reg':
            info_reg_call()

        if sp=='help' or sp=='h':
            help_call()

        if sk[0]=='display':
            display_call(sk[1])

        if sk[0]=='print/d':
            print_decimal(sk[1])

        if sk[0]=='print/h':
            print_hex(sk[1])

        if sk[0]=='print/b':
            print_binary(sk[1])

        if sp not in ['n','ni','next','q','quit','list','help','h','info reg','run','display $eax','display $ebx','display $ecx','display $edx','display $esp','display $ebp','display $esi','display $edi','print/d $eax','print/d $ebx','print/d $ecx','print/d $edx','print/d $esp','print/d $ebp','print/d $esi','print/d $edi','print/h $eax','print/h $ebx','print/h $ecx','print/h $edx','print/h $esp','print/h $ebp','print/h $esi','print/h $edi','print/b $eax','print/b $ebx','print/b $ecx','print/b $edx','print/b $esp','print/b $ebp','print/b $esi','print/b $edi']:
            print("Undefined command: %r.  Try 'help' or 'h'." % (sp))

            
    else:
        print("which has no line number information, end program")


        
if __name__ == '__main__':
        
    script,filename=argv
    f1=filename.split('.')
    if f1[1]!='asm':
        print("nasm: fatal: unable to open input file",filename)
        sys.exit()
        
    sym_table(filename)
    write_file()
     
    lit_table(filename)
    lit_write()
    
    obj_code(filename)
   
        

    print("< pudebugger -v1.0")
    print("< copyright@ Sagar Dahatonde")
    print("< Pune University Computer Science Department")
    print("For help, type 'help' or 'h'")
    print("Reading symbols from ./a.out...done.")
    while True:
        sp=input("(gdb)")
        sk=sp.split()
        
        if sp=='q' or sp=='quit':
            quit_call()

        if sp=='list':
            list_call()

        if sp=='info reg':
            print("The program is not being run.")

        if sp=='help' or sp=='h':
            help_call()

        if sp=='run':
            start_deb()
            
        if sk[0]=='display':
            display_call(sk[1])

        if sk[0]=='print/d':
            print_decimal(sk[1])

        if sk[0]=='print/h':
            print_hex(sk[1])

        if sk[0]=='print/b':
            print_binary(sk[1])

        if sp=='n' or sp=='ni' or sp=='next':
            print("The program is not being run.")
            
        if sp not in ['n','q','quit','list','help','h','info reg','run','display $eax','display $ebx','display $ecx','display $edx','display $esp','display $ebp','display $esi','display $edi','print/d $eax','print/d $ebx','print/d $ecx','print/d $edx','print/d $esp','print/d $ebp','print/d $esi','print/d $edi','print/h $eax','print/h $ebx','print/h $ecx','print/h $edx','print/h $esp','print/h $ebp','print/h $esi','print/h $edi','print/b $eax','print/b $ebx','print/b $ecx','print/b $edx','print/b $esp','print/b $ebp','print/b $esi','print/b $edi']:
            print("Undefined command: %r.  Try 'help' or 'h'." % (sp))
            
           
