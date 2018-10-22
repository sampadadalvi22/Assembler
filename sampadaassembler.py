from sys import argv
from subprocess import call
from subprocess import *
from symboltable import *
from literaltable import *



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

  

def disp_option(x):
    if x=='-s':
        print("\n\t\t\t\t SYMBOL TABLE")
        call(["python3","symboltable.py",filename])
        print('\n')

    if x=='-l':
        print("\n\t\t\t\t LITERAL TABLE")
        call(["python3","literaltable.py",filename])
        print('\n')

    
      
if __name__ == "__main__":

    if len(argv)==1:
        printf=check_output(["echo", "Place enter input .asm file name"], universal_newlines=True)
        print(printf)
        options()
        exit()

    
    filename=argv[1]
    f=filename.split('.')
    
   

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

      
                
            
                
        if len(list1)<2:
            for i in list1:
                if i not in ['-s','-l','-i','-lst','-o']:
                    pp=check_output(["echo", "Place enter options[-s/-l/-i/-lst/-obj]"], universal_newlines=True)
                    print(pp)
                    options()
                    exit()

            for i in list1:
                disp_option(i)
                exit()
        
    
