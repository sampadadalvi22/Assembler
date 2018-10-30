from sys import argv
import sys

redf_flag=[]
ubdf_flag=[]
temp_sym=[]
lab_sym=[]
sym_val=[]
sym_def=['db','dw','dd','dq','dt','resb','resw','resd','resq','rest']
sym_udf=['global','extern','jmp','je','jne','jg','lge','lnge','jng','jl','jle','lnle','jnl','jz','jnz','loop']
sym_equ=['equ']
sym_err=[['1','symbol %r redefined']]
cnt=1
symb=[]
filename="sampadaassembler"

def constr(val2):
    val3=','.join(val2)
    val4=val3.split(',')
    val5=[]
    
    for i in range(len(val4)):
        if(val4[i]=='0'):
            for j in range(i):
                val5.append(val4[j])

    val6=','.join(val5)
    val7=val6.replace(","," ")
    val8=val7.replace('"','')
    return val8


def find_size(val1,n):
    ss=val1.split(',')
    sn=len(ss)
    return(sn*n)

def count_len(val1):
    val2=val1.split('-')
    temp=val2[1]
    for i in range(len(sym_val)):
        if temp in sym_val[i][1]:
            return sym_val[i][5]
            

def check_size(val1,n,s):
    val2=list(val1)
    val3=ord(val2[0])
    if val3 in range(48,58):
        return ((int(val1))*s)

def find_val(val):
    for i in range(len(sym_val)):
        if val[i] in sym_val[i][1]:
            return sym_val[i][6]

    

def find_sym(list2,n):
    sym_num=[]
    symbol=[]
    values=[]
    size  =[]
    line_no=[]
    sym_type=[]
    define_un=[]
    section=[]
    global cnt
    
    for i in range(len(list2)):
        if list2[i] in sym_def:
            symbol.append(list2[i-1])                                 #append symbol name in symbol list
            sym_num.append(cnt)
            cnt+=1
            if list2[i] in sym_def[:4]:
                section.append('dat')
            if list2[i] in sym_def[5:]:
                section.append('bss')
            if (list2[i]=='db'):
                val1=[]
                for j in range(i+1,len(list2)):
                    if(list2[j]!='0'):
                        val1.append(list2[j])
                val2=constr(val1)
                values.append(val2)
                
            if (list2[i]=='dw' or list2[i]=='dd' or list2[i]=='dq' or list2[i]=='dt'):
                values.append(list2[i+1])

            if (list2[i]=='resb' or list2[i]=='resw' or list2[i]=='resd' or list2[i]=='resq' or list2[i]=='rest'):
                values.append('-')     
                
                        
            if list2[i] in sym_def:
                define_un.append('D')
            else:
                define_un.append('U')

            if list2[i]=='db':
                size.append(len(val2))
            if list2[i]=='dw':
                siz=find_size(list2[i+1],2)
                size.append(siz)
            if list2[i]=='dd':
                siz=find_size(list2[i+1],4)
                size.append(siz)
            if list2[i]=='dq':
                siz=find_size(list2[i+1],8)
                size.append(siz)
            if list2[i]=='dt':
                siz=find_size(list2[i+1],10)
                size.append(siz)
            if list2[i]=='resb':
                siz=check_size(list2[i+1],n,1)
                size.append(siz)
            if list2[i]=='resw':
                siz=check_size(list2[i+1],n,2)
                size.append(siz)
            if list2[i]=='resd':
                siz=check_size(list2[i+1],n,4)
                size.append(siz)
            if list2[i]=='resq':
                siz=check_size(list2[i+1],n,8)
                size.append(siz)
            if list2[i]=='rest':
                siz=check_size(list2[i+1],n,10)
                size.append(siz)

            line_no.append(n)
            sym_type.append(list2[i])
            sym_val.append(line_no+symbol+define_un+sym_num+section+size+values+sym_type)

        if list2[i] in sym_udf and len(list2)==2:
            line_no.append(n)
            section.append('txt')
            if list2[i]=='global' or list2[i]=='extern':
                symbol.append(list2[i+1])
                sym_num.append(cnt)
                cnt+=1
            if list2[i] in sym_udf[2:]:
                symbol.append(list2[i+1])
                sym_num.append(cnt)
                cnt+=1
            if list2[i] in sym_udf:
                define_un.append('U')
            else:
                define_un.append('D')
            size.append('-')
            values.append('-')
            sym_type.append('-')
            sym_val.append(line_no+symbol+define_un+sym_num+section+size+values+sym_type)
            
        if list2[i] in sym_equ:
            line_no.append(n)
            section.append('dat')
            symbol.append(list2[i-1])
            sym_num.append(cnt)
            cnt+=1
            if list2[i] in sym_udf:
                define_un.append('U')
            else:
                define_un.append('D')
            temp=count_len(list2[i+1])
            size.append(temp)
            val1=list2[i+1].split('-')
            val2=find_val(val1[1])
            values.append(val2)
            sym_type.append('-')
            sym_val.append(line_no+symbol+define_un+sym_num+section+size+values+sym_type)


        if list2[i] in sym_udf and len(list2)>=2:
            temp=list2[i+1]
            lab_sym.append(temp)
    
    if list2==[]:
        return
    else:
        val1=list2[0]
        val2=list(val1)
        for i in range(len(val2)):
            if val2[i]==':':
                val3=''.join(val2[:i])
                temp_sym.append(val3)


def disp_error(n,sym,l):
    for i in range(len(sym_err)):
        if 'n' in sym_err[i][0]:
            print(sym_err)
            

            
def sym_err_redef(list1,n):
    for i in range(len(list1)):
        if list1[i] in sym_def:
            temp=list1[i-1]
            for j in range(len(sym_val)):
                if temp in sym_val[j][1]:
                    # disp_error(1,temp,l)
                    print(filename,':',n, "errror",':',"symbol",temp,"redefined")
                    return 0
                    
        if list1[i] in sym_def:
            if list1[i-1]=='main':
                 print(filename,':',n, "errror",':',"symbol",list1[i-1],"redefined")
                 return 0
               
       
    
def sym_err_undef(list1,n):              
    for i in range(len(list1)):
   
        if list1[i]=='equ':
            val1=list1[i+1]
            val2=val1.split('-')
            val3=val2[1]
            for j in range(len(sym_val)):
                if val3 in sym_val[j][1]:
                    return 1 
                else:
                    print(filename,':',n, "errror",':',"symbol",val3,"undefined")
                    return 0

        if len(list1)==1:
            if list1[i]=='global':
                print(filename,':',n, "warning",':'," macro `global' exists, but not taking 0 parameters")
                print(filename,':',n, "warning",':',"label alone on a line without a colon might be in error")
                return 0
            
        if list1[i] in sym_def:
            if list1[i-1]=='main':
                print(filename,':',n, "warning",':',"symbol",list1[i-1],"GLOBAL directive after symbol definition is an experimental feature")
                return 0

        if list1[i] in sym_def[5:]:
            val1=list1[i+1]
            val2=list(val1)
            val3=ord(val2[0])
            if val3 not in range(48,58):
                print(filename,':',n, "errror",':',"symbol",val1,"undefined")
                return 0

            
        if list1[i] in sym_udf[2:]:
            temp=list1[i+1]
            if temp not in temp_sym:
                print(filename,':',n, "errror",':',"symbol",temp,"undefined")
                return 0
    
    if list1==[]:
        return
    else:
        val1=list1[0]
        val2=list(val1)
        for i in range(len(val2)):
            if val2[i]==':':
                val3=''.join(val2[:i])
                if val3 not in lab_sym:
                    print(filename,':',n, "errror",':',"symbol",val3,"undefined")
                    return 0        

    
def sym_table(f_name):
    global filename
    filename=f_name
    op=open(f_name,"r")
    l=op.read()
    ll=l.split('\n')
    ln=len(ll)
    
    of=open(f_name,"r+")
    for i in range(1,ln):
        line1=of.readline()
        list1=line1.split()
        cnt1=sym_err_redef(list1,i)
        redf_flag.append(cnt1)
        find_sym(list1,i)

    if 0 in redf_flag:
        sys.exit()
        
    pf=open(f_name,"r+")
    for j in range(1,ln):
        line2=pf.readline()
        list2=line2.split()
        cnt2=sym_err_undef(list2,j)
        ubdf_flag.append(cnt2)
    if 0 in ubdf_flag:
        sys.exit()

    k=0
    for k in range(len(sym_val)):
        symb.append(sym_val[k][1])


  
        
def sym_tab_disp():
    if (sym_val==[]):
        print('\t'"Symbol NOT Available")
    else:
        ln=len(sym_val)
        print('\n'"    line Number" '\t' "Sym_No" '\t' "Symbol" '\t' "Define/Undefine"  '\t' "section" '\t' "Size" '\t' "Values" '\n')
        for i in range(ln):
            print('\t',sym_val[i][0] ,'\t',sym_val[i][3],'\t',sym_val[i][1],'\t''\t',sym_val[i][2],'\t',sym_val[i][4],'\t',sym_val[i][5],'\t',sym_val[i][6])
        print('\n')

def write_file():
    fo=open(".symbol_table.txt","w+")
    for i in range(len(sym_val)):
        fo.write(str(sym_val[i][3])+'\t'+str(sym_val[i][0])+'\t'+sym_val[i][1]+'\t'+str(sym_val[i][4])+'\t'+str(sym_val[i][5])+'\t'+sym_val[i][6]+'\n')
    
         
if __name__ == '__main__':
    filename=argv[1]
    
    sym_table(filename)
    sym_tab_disp()
    write_file()
