from sys import argv
from subprocess import call
from subprocess import *
from symboltable import *
from literaltable import *
from intermediatecode import *
from finalLst import *
from finalObj import *
from debugger import *
from macro import *

if not os.path.exists(".symbol_table.txt"):
    open(".symbol_table.txt","w").close()

if not os.path.exists(".literal_table.txt"):
    open(".literal_table.txt","w").close()

def options():
    p1=check_output(["echo","SYNOPSIS \n \t ./sampadaassembler.py asm_filename [options]\t=> Get Outpuet asm file "], universal_newlines=True)
    print(p1)
    p2=check_output(["echo", "COMMAND LINE OPTIONS"], universal_newlines=True)
    print(p2)
    p3=check_output(["echo", "\t -s \t=> Display Symbol Table"], universal_newlines=True)
    print(p3)
    p4=check_output(["echo", "\t -l \t=> Display Literal Table"], universal_newlines=True)
    print(p4)
    p5=check_output(["echo", "\t -i \t=> Display Intermediate Code"], universal_newlines=True)
    print(p5)
    p6=check_output(["echo", "\t -lst   => Display lst Code"], universal_newlines=True)
    print(p6)
    p7=check_output(["echo", "\t -o   \t=> Display Object Code"], universal_newlines=True)
    print(p7)
    p7=check_output(["echo", "\t -gdb   => Debugging Source Code"], universal_newlines=True)
    print(p7)
    p8=check_output(["echo", "\t -lst I output_filename.lst \t=> Write lst Code"], universal_newlines=True)
    print(p8)
    p9=check_output(["echo", "\t -o   I output_filename.txt \t=> Write Object Code"], universal_newlines=True)
    print(p9)
    
    p1=check_output(["echo","\nSYNOPSIS MACRO \n \t\t  ./puasm.py macro_asm_filename [options]\t=> Get Output macro_asm file"], universal_newlines=True)
    print(p1)
    p2=check_output(["echo", "COMMAND LINE OPTIONS MACRO"], universal_newlines=True)
    print(p2)
    p3=check_output(["echo", "\t -e  \t=> Display Macro Expansion Code"], universal_newlines=True)
    print(p3)
    p3=check_output(["echo", "\t -mt \t=> Display Macro Table(MNT & MDT)"], universal_newlines=True)
    print(p3)
    p3=check_output(["echo", "\t -ms \t=> Display Symbol Table"], universal_newlines=True)
    print(p3)
    p3=check_output(["echo", "\t -ml \t=> Display Literal Table"], universal_newlines=True)
    print(p3)
    p3=check_output(["echo", "\t -mi \t=> Display Intermediate Code"], universal_newlines=True)
    print(p3)
    p3=check_output(["echo", "\t -mlst  => Display lst Code"], universal_newlines=True)
    print(p3)
    p3=check_output(["echo", "\t -mo \t=> Display Object Code"], universal_newlines=True)
    print(p3)
    p3=check_output(["echo", "\t -mgdb  => Debugging Source Code"], universal_newlines=True)
    print(p3)
    p10=check_output(["echo", "\t -e    I output_filename.txt \t=> Write Macro Expansion Code"], universal_newlines=True)
    print(p10)
    p10=check_output(["echo", "\t -eo   I output_filename.txt \t=> Write Object Code"], universal_newlines=True)
    print(p10)
    p10=check_output(["echo", "\t -elst I output_filename.txt \t=> Write lst Code"], universal_newlines=True)
    print(p10)

   
   
    
def disp_option(x):
    if x=='-s':
        print("\n\t\t\t\t SYMBOL TABLE")
        call(["python3","symboltable.py",filename])
        print('\n')

    if x=='-l':
        print("\n\t\t\t\t LITERAL TABLE")
        call(["python3","literaltable.py",filename])
        print('\n')

    if x=='-i':
        print("\n\t\t\t\t Intermediate Code\n")
        call(["python3","intermediatecode.py",filename])
        print('\n')

    if x=='-lst':
        print("\n\t\t\t\t lst)\n")
        call(["python3","finalLst.py",filename])

    if x=='-o':
        print("\n\t\t\t\t Object Code\n")
        call(["python3","finalObj.py",filename])

    if x=='-gdb':
        call(["python3","debugger.py",filename])

    if x=='-e':
        call(["python3","macro.py",filename])

    if x=='-mt':
         macro_table(filename)
         print("\n\t\t\t\tMNT Table\n")
         mnt_display()
         print("\n\t\t\t\tMDT Table\n")
         mdt_display()

    if x=='-ms':
        macro_table(filename)
        exp_write()
        print("\n\t\t\tMacro SYMBOL TABLE")
        call(["python3","symboltable.py","sp.asm"])
        exit()

    if x=='-ml':
        macro_table(filename)
        exp_write()
        print("\n\t\t\tMacro LITERAL TABLE")
        call(["python3","literaltable.py","sp.asm"])
        print('\n')
    
    if x=='-mi':
        macro_table(filename)
        exp_write()
        print("\n\t\t\tMacro Intermediate Code\n")
        call(["python3","intermediatecode.py","sp.asm"])
        print('\n')

    if x=='-mlst':
        macro_table(filename)
        exp_write()
        print("\n\t\t\t\tMacro lst)\n")
        call(["python3","finalLst.py","sp.asm"])

    if x=='-mo':
        macro_table(filename)
        exp_write()
        print("\n\t\t\t\tMacro Object Code\n")
        call(["python3","finalObj.py","sp.asm"])

    if x=='-mgdb':
        macro_table(filename)
        exp_write()
        call(["python3","debugger.py","sp.asm"])
    
      
if __name__ == "__main__":

    if len(argv)==1:
        printf=check_output(["echo", "Place enter input .asm file name"], universal_newlines=True)
        print(printf)
        options()
        exit()

    
    filename=argv[1]
    f=filename.split('.')
    
    if len(argv)==2:
        fp=open(filename,"r")
        line=fp.read().split()
        if line[0]=='section':
            call(["python3","smaco.py",filename])
            exit()
        if line[0]=='%macro':
            macro_table(filename)
            exp_write()
            call(["python3","smaco.py","sp.asm"])
            exit()
    
            
    if len(argv)> 2:
        list1=argv[2:]

        
      
        filename1=argv[2]
        f1=filename1.split('.')

        if len(argv)==4 and list1[2=='-o']:
            print("\n\t\t\t\t Object Code\n")
            call(["python3","concatObj.py",filename])

    if len(argv)== 3:
        list1=argv[2:]

            
        if len(list1)>3:
            if list1[1]=='I' and list1[0]=='-lst':
                lst_table(filename)
                fname=str(list1[2])
                lst_write(fname)
                exit()

            if list1[1]=='I' and list1[0]=='-o':
                obj_code(filename)
                fname=str(list1[2])
                sym_table(filename)
                lit_table(filename)   
                obj_write(fname)
                exit()

            if list1[1]=='I' and list1[0]=='-e':
                macro_table(filename)
                fname=str(list1[2])
                exp_write1(filename,fname)
                exit()

            if list1[1]=='I' and list1[0]=='-mlst':
                macro_table(filename)
                exp_write()
                lst_table("sp.asm")
                fname=str(list1[2])
                lst_write(fname)
                exit()

            if list1[1]=='I' and list1[0]=='-mo':
                macro_table(filename)
                exp_write()
                obj_code("sp.asm")
                fname=str(list1[2])
                sym_table("sp.asm")
                lit_table("sp.asm")   
                obj_write(fname)
                exit()

                
            if list1[1]=='-o':
                print("\n\t\t\t\tConcat  Object Code\n")
                call(["python3","concatObj.py",filename])
                #obj_code(filename)
                #fname=str(list1[2])
                #sym_table(filename)
                #lit_table(filename)   
                #obj_write(fname)
                exit()
                
            
                
        if len(list1)<2:
            for i in list1:
                if i not in ['-s','-l','-i','-lst','-o','I','-gdb','-e','-mt','-ms','-ml','-mi','-mlst','-mo','-mgdb']:
                    pp=check_output(["echo", "Place enter options[-s/-l/-i/-lst/-obj]"], universal_newlines=True)
                    print(pp)
                    options()
                    exit()

            for i in list1:
                disp_option(i)
                exit()
        
    
