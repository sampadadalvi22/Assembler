from symboltable import *
from literaltable import *
from sys import argv
import sys
import os

op_val=[]
ins_sym=['mov','add','sub','call','inc','dec','push','pop','not','and','or','xor','jmp','je','jne','jg','jng','jge','jnge','jl','jnl','jle','jnle','jz','jnz','loop','cmp','ret']
ins_str=['MOVSB','MOVSW','MOVSD','STOSB','STOSW','STOSD','LODSB','LODSW','LODSD','SCASB','SACSW','SACSD','CMPSB','CMPSW','CMPSD','CLD','STD','REP','REPE','REPNE','REPZ','REPNZ']
reg_sym32=['eax','ebx','ecx','edx','edi','esi','esp','ebp']
reg_sym16=['ax','bx','cx','dx','di','si','sp','bp']
reg_sym08=['al','bl','cl','dl','ah','bh','ch','dh']

if not os.path.exists(".symbol_table.txt"):
    open(".symbol_table.txt","w").close()

if not os.path.exists(".literal_table.txt"):
    open(".literal_table.txt","w").close()
    
fp2=open(".symbol_table.txt","r")
line2=(fp2.read().split())
fp4=open(".literal_table.txt","r")
line4=(fp4.read()).split()


def find_sym_num(fy):
    for i in range(len(line2)):
        if fy ==line2[i]:
            val2=(line2[i-2])
            break
    return val2

def check_sym(val2,n):
    val3=list(val2)
    val4=val3[n:-1]
    val5=','.join(val4)
    val6=val5.replace(",","")
    return val6

def find_opcode(line1,list1,l_no,addr):
    opcode_no=[]
    address=[]
    opcode_ins=[]
    orignal_ins=[]
    global cnt
    flag=0
    val=list1[1]
    val1=[]
    val2=[]
    val3=[]
    val4=[]
    temp=val.split(',')
    
    if len(temp)==2:
        ins=list1[0]
        if len(temp[0])<7 and len(temp[1])<7:
            fy=temp[0]
            sy=temp[1]
            flag=1
        if len(temp[0])<7 and len(temp[1])>=7:
            val1=temp[1]
            val2=list(val1)
            if val2[0]=='d':
                val=check_sym(val1,6)
                fy=temp[0]
                sy=val
                flag=1
            if val2[0]=='w':
                val=check_sym(val1,5)
                fy=temp[0]
                sy=val
                flag=1
            if val2[0]=='b':
                val=check_sym(val1,5)
                fy=temp[0]
                sy=val
                flag=1

        if len(temp[0])>=7 and len(temp[1])<7:
            val1=temp[0]
            val2=list(val1)
            if val2[0]=='d':
                val=check_sym(val1,6)
                fy=val
                sy=temp[1]
                flag=1
            if val2[0]=='w':
                val=check_sym(val1,5)
                fy=val
                sy=temp[1]
                flag=1
            if val2[0]=='b':
                val=check_sym(val1,5)
                fy=val
                sy=temp[1]
                flag=1
            
    if len(temp)==1:
        ins=list1[0]
        fy=temp[0]
        flag=2

    if flag==2:                                           # push | pop | inc | dec | not | jmp | loop | call | ret
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+4
        
        if ins=='push' and fy in reg_sym32:               # push reg32
            opcode_ins.append("op#46 push  reg32")
        else:
            opcode_ins.append("op#46 push  mem32")
        if ins=='push' and fy in reg_sym16:               # push reg16
            opcode_ins.append("op#47 push  reg16")
        if ins=='push' and fy in reg_sym08:               # push reg08
            opcode_ins.append("op#48 push  reg08")
        
        if ins=='pop' and fy in reg_sym32:                # pop reg32 
            opcode_ins.append("op#49 pop   reg32")
        if ins=='pop' and fy in reg_sym16:                # pop reg16
            opcode_ins.append("op#50 pop   reg16")
        if ins=='pop' and fy in reg_sym08:                # pop reg08
            opcode_ins.append("op#51 pop   reg08")
            
        if ins=='inc' and fy in reg_sym32:                # inc reg32 
            opcode_ins.append("op#52 inc   reg32")
        if ins=='inc' and fy in reg_sym16:                # inc reg16
            opcode_ins.append("op#53 inc   reg16")
        if ins=='inc' and fy in reg_sym08:                # inc reg08
            opcode_ins.append("op#54 inc   reg08")
        if ins=='inc' and fy in line2:                    # inc sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("op#55 inc   sym#%r"% int(val2))

        if ins=='dec' and fy in reg_sym32:                # dec reg32 
            opcode_ins.append("op#56 dec   reg32")
        if ins=='dec' and fy in reg_sym16:                # dec reg16
            opcode_ins.append("op#57 dec   reg16")
        if ins=='dec' and fy in reg_sym08:                # dec reg08
            opcode_ins.append("op#58 dec   reg08")
        if ins=='dec' and fy in line2:                    # dec sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("op#59 dec   sym#%r"% int(val2))

        if ins=='not' and fy in reg_sym32:                # not reg32 
            opcode_ins.append("op#75 not   reg32")
        if ins=='not' and fy in reg_sym16:                # not reg16
            opcode_ins.append("op#76 not   reg16")
        if ins=='not' and fy in reg_sym08:                # not reg08
            opcode_ins.append("op#77 not   reg08")
        if ins=='not' and fy in line2:                    # not sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("op#59 not   sym#%r"% int(val2))

      
        if ins=='jmp' and fy in line2:                    # jmp sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#109 jmp   sym#%r"% int(val2))
        if ins=='je' and fy in line2:                    # je sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#110 je    sym#%r"% int(val2))
        if ins=='jne' and fy in line2:                    # jne sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#111 jne   sym#%r"% int(val2))
        if ins=='jg' and fy in line2:                    # jg sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#112 jg    sym#%r"% int(val2))
        if ins=='jng' and fy in line2:                    # jng sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#113 jng   sym#%r"% int(val2))
        if ins=='jge' and fy in line2:                    # jge sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#114 jge   sym#%r"% int(val2))
        if ins=='jnge' and fy in line2:                    # jnge sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#115 jnge  sym#%r"% int(val2))
        if ins=='jl' and fy in line2:                    # jl sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#116 jl    sym#%r"% int(val2))
        if ins=='jnl' and fy in line2:                    # jnl sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#117 jnl   sym#%r"% int(val2))
        if ins=='jle' and fy in line2:                    # jle sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#118 jle   sym#%r"% int(val2))
        if ins=='jnle' and fy in line2:                    # jnle sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#119 jnle  sym#%r"% int(val2))
        if ins=='jz' and fy in line2:                    # jz sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#120 jz    sym#%r"% int(val2))
        if ins=='jnz' and fy in line2:                    # jnz sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#121 jnz   sym#%r"% int(val2))

        if ins=='loop' and fy in line2:                    # loop sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#122 loop sym#%r"% int(val2))

        if ins=='call' and fy in line2:                    # call sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#135 call sym#%r"% int(val2))
     
        if ins=='ret' and fy in reg_sym32:                 # ret reg32 
            opcode_ins.append("o#136 ret  reg32")
        if ins=='ret' and fy in reg_sym16:                 # ret reg16 
            opcode_ins.append("o#137 ret  reg16")
        if ins=='ret' and fy in reg_sym08:                 # ret reg08
            opcode_ins.append("o#138 ret  reg08")
        if ins=='ret' and fy in line2:                     # ret sym/mem 
            val2=find_sym_num(fy)
            opcode_ins.append("o#139 ret sym#%r"% int(val2))

            
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
        
    if flag==1 and (fy in reg_sym32) and (sy in reg_sym32): #mov | cmp | add | sub | and | or | xor  reg32,reg32
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+4
        if ins=='mov':
            opcode_ins.append("op#10 reg32 reg32")
        if ins=='add':
            opcode_ins.append("op#25 reg32 reg32")
        if ins=='sub':
            opcode_ins.append("op#40 reg32 reg32")
        if ins=='and':
            opcode_ins.append("op#69 reg32 reg32")
        if ins=='or':
            opcode_ins.append("op#88 reg32 reg32")
        if ins=='xor':
            opcode_ins.append("o#103 reg32 reg32")
        if ins=='cmp':
            opcode_ins.append("o#129 reg32 reg32")
            
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr

    if flag==1 and (fy in reg_sym16) and (sy in reg_sym16): #mov | cmp | add | sub | and | or | xor reg16,reg16
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+4
        if ins=='mov':
            opcode_ins.append("op#11 reg16 reg16")
        if ins=='add':
            opcode_ins.append("op#26 reg16 reg16")
        if ins=='sub':
            opcode_ins.append("op#41 reg16 reg16")
        if ins=='and':
            opcode_ins.append("op#70 reg16 reg16")
        if ins=='or':
            opcode_ins.append("op#89 reg16 reg16")
        if ins=='xor':
            opcode_ins.append("o#104 reg16 reg16")
        if ins=='cmp':
            opcode_ins.append("o#130 reg16 reg16")
            
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
    
    if flag==1 and (fy in reg_sym08) and (sy in reg_sym08):  #mov | cmp | add | sub | and | or | xor reg08,reg08
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+4
        if ins=='mov':
            opcode_ins.append("op#12 reg08 reg08")
        if ins=='add':
            opcode_ins.append("op#27 reg08 reg08")
        if ins=='sub':
            opcode_ins.append("op#42 reg08 reg08")
        if ins=='and':
            opcode_ins.append("op#71 reg08 reg08")
        if ins=='or':
            opcode_ins.append("op#90 reg08 reg08")
        if ins=='xor':
            opcode_ins.append("o#105 reg08 reg08")
        if ins=='cmp':
            opcode_ins.append("o#131 reg08 reg08")
 
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr



    if flag==1 and (fy in reg_sym32) and (sy in line4): #mov | cmp | add | sub | and | or | xor reg32,lis32
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line4)):
            if sy == line4[i] and ord((list(sy))[0]) in range(48,58):
                val=(line4[i-1])
                break
        if ins =='mov':
            temp=('op#07 reg32 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='add':
            temp=('op#22 reg32 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#37 reg32 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#66 reg32 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#85 reg32 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('o#100 reg32 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='cmp':
            temp=('o#126 reg32 lit#%r'% int(val))
            opcode_ins.append(temp)

        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr


    if flag==1 and (fy in reg_sym16) and (sy in line4): #mov | cmp | add | sub | and | or | xor reg16,lit16 
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line4)):
            if sy == line4[i] and ord((list(sy))[0]) in range(48,58):
                val=(line4[i-1])
                break
        if ins =='mov':
            temp=('op#08 reg16 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='add':
            temp=('op#23 reg16 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#38 reg16 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#67 reg16 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#86 reg16 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('o#101 reg16 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='cmp':
            temp=('o#127 reg16 lit#%r'% int(val))
            opcode_ins.append(temp)
            
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr

    if flag==1 and (fy in reg_sym08) and (sy in line4): #mov | cmp | add | sub | and | or | xor reg08,lit08
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line4)):
            if sy == line4[i] and ord((list(sy))[0]) in range(48,58):
                val=(line4[i-1])
                break
        if ins =='mov':
            temp=('op#09 reg08 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='add':
            temp=('op#24 reg08 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#38 reg08 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#68 reg08 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#87 reg08 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('o#102 reg08 lit#%r'% int(val))
            opcode_ins.append(temp)
        if ins=='cmp':
            temp=('o#128 reg08 lit#%r'% int(val))
            opcode_ins.append(temp)
            
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
   
    

    if flag==1 and (fy in line2) and (sy in reg_sym32):  #mov | cmp | add | sub | and | or | xor sym32,reg32
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line2)):
            if fy ==line2[i]:
                val2=(line2[i-2])
                break
        if ins=='mov':
            temp=('op#04 sym#%d reg32'% int(val2))
            opcode_ins.append(temp)
        if ins=='add':
            temp=('op#19 sym#%d reg32'% int(val2))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#34 sym#%d reg32'% int(val2))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#63 sym#%d reg32'% int(val2))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#82 sym#%d reg32'% int(val2))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('op#91 sym#%d reg32'% int(val2))
            opcode_ins.append(temp)
        if ins=='cmp':
            temp=('o#123 sym#%d reg32'% int(val2))
            opcode_ins.append(temp)
            
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr

    if flag==1 and (fy in line2) and (sy in reg_sym16):  #mov | cmp | add | sub | and | or | xor sym16,reg16
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line2)):
            if fy ==line2[i]:
                val2=(line2[i-2])
                break
        if ins=='mov':
            temp=('op#05 sym#%d reg16'% int(val2))
            opcode_ins.append(temp)
        if ins=='add':
            temp=('op#20 sym#%d reg16'% int(val2))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#35 sym#%d reg16'% int(val2))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#64 sym#%d reg16'% int(val2))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#83 sym#%d reg16'% int(val2))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('op#98 sym#%d reg16'% int(val2))
            opcode_ins.append(temp)
        if ins=='cmp':
            temp=('o#124 sym#%d reg16'% int(val2))
            opcode_ins.append(temp)

        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr

    if flag==1 and (fy in line2) and (sy in reg_sym08):  #mov | cmp | add | sub | and | or | xor sym08,reg08
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line2)):
            if fy ==line2[i]:
                val2=(line2[i-2])
                break
        if ins=='mov':
            temp=('op#06 sym#%d reg08'% int(val2))
            opcode_ins.append(temp)
        if ins=='add':
            temp=('op#21 sym#%d reg08'% int(val2))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#36 sym#%d reg08'% int(val2))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#65 sym#%d reg08'% int(val2))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#84 sym#%d reg08'% int(val2))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('op#99 sym#%d reg08'% int(val2))
            opcode_ins.append(temp)
        if ins=='cmp':
            temp=('o#125 sym#%d reg08'% int(val2))
            opcode_ins.append(temp)
            
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
   
    
        
    if flag==1 and (fy in reg_sym32) and (sy in line2):  #mov | cmp | add | sub | and | or | xor reg32,sym32
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line2)):
            if sy ==line2[i] and ord((list(sy))[0]) not in range(48,58):
                val1=(line2[i-2])
                break
        if val1==[]:
            return
        else:
            if ins=='mov':
                temp1=('op#13 reg32 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='add':
                temp1=('op#28 reg32 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='sub':
                temp1=('op#43 reg32 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='and':
                temp1=('op#72 reg32 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='or':
                temp1=('op#91 reg32 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='xor':
                temp1=('o#106 reg32 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='cmp':
                temp1=('o#132 reg32 sym#%r'% int(val1))
                opcode_ins.append(temp1)
                
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
    
    if flag==1 and (fy in reg_sym16) and (sy in line2): #mov | cmp | add | sub | and | or | xor reg16,sym16
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line2)):
            if sy ==line2[i] and ord((list(sy))[0]) not in range(48,58):
                val1=(line2[i-2])
                break
        if val1==[]:
            return
        else:
            if ins=='mov':
                temp1=('op#14 reg16 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='add':
                temp1=('op#29 reg16 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='sub':
                temp1=('op#44 reg16 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='and':
                temp1=('op#73 reg16 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='or':
                temp1=('op#92 reg16 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='xor':
                temp1=('o#107 reg16 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='cmp':
                temp1=('o#133 reg16 sym#%r'% int(val1))
                opcode_ins.append(temp1)
         
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr

    if flag==1 and (fy in reg_sym08) and (sy in line2): #mov | cmp | add | sub | and | or | xor reg08,sym08
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+6
        for i in range(len(line2)):
            if sy ==line2[i] and ord((list(sy))[0]) not in range(48,58):
                val1=(line2[i-2])
                break
        if val1==[]:
            return
        else:
            if ins=='mov':
                temp1=('op#15 reg08 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='add':
                temp1=('op#30 reg08 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='sub':
                temp1=('op#45 reg08 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='and':
                temp1=('op#74 reg08 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='or':
                temp1=('op#93 reg08 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='xor':
                temp1=('o#108 reg08 sym#%r'% int(val1))
                opcode_ins.append(temp1)
            if ins=='cmp':
                temp1=('o#134 reg08 sym#%r'% int(val1))
                opcode_ins.append(temp1)
                
        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr


    
    if flag==1 and (fy in line2):              #mov | add | sub | and | or | xor sym32,lit32
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+8
        for i in range(len(line2)):
            if fy ==line2[i]:
                val4=(line2[i-2])
                break
        for j in range(len(line4)):
            if sy == line4[j] and ord((list(sy))[0]) in range(48,58):
                val3=(line4[j-1])
                break
        if ins=='mov':
                temp=('op#01 sym#%r lit#%r'% (int(val4),int(val3)))
                opcode_ins.append(temp)
        if ins=='add':
            temp=('op#16 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#41 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#60 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#79 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('op#94 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)

        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
        
    else:
        return addr

    if flag==1 and (fy in line2):              #mov | add | sub | and | or | xor sym16,lit16
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+8
        for i in range(len(line2)):
            if fy ==line2[i]:
                val4=(line2[i-2])
                break
        for j in range(len(line4)):
            if sy == line4[j] and ord((list(sy))[0]) in range(48,58):
                val3=(line4[j-1])
                break
        if ins=='mov':
                temp=('op#02 sym#%r lit#%r'% (int(val4),int(val3)))
                opcode_ins.append(temp)
        if ins=='add':
            temp=('op#17 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#42 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#61 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#80 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('op#95 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)

        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
        
    else:
        return addr


    if flag==1 and (fy in line2):              #mov | add | sub | and | or | xor sym08,lit08
        opcode_no.append(l_no)
        add='{0:04}'.format(addr)
        address.append(add)
        addr=addr+8
        for i in range(len(line2)):
            if fy ==line2[i]:
                val4=(line2[i-2])
                break
        for j in range(len(line4)):
            if sy == line4[j] and ord((list(sy))[0]) in range(48,58):
                val3=(line4[j-1])
                break
        if ins=='mov':
                temp=('op#03 sym#%r lit#%r'% (int(val4),int(val3)))
                opcode_ins.append(temp)
        if ins=='add':
            temp=('op#18 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='sub':
            temp=('op#43 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='and':
            temp=('op#62 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='or':
            temp=('op#81 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)
        if ins=='xor':
            temp=('op#96 sym#%r lit#%r'% (int(val4),int(val3)))
            opcode_ins.append(temp)

        orignal_ins.append(list1[0]+" "+list1[1])
        op_val.append(opcode_no+address+opcode_ins+orignal_ins)
        return addr
        
    else:
        return addr

def find_opcode_str(line1,list1,l_no,addr):
    opcode_no=[]
    address=[]
    opcode_ins=[]
    orignal_ins=[]
    global cnt
    ins=list1[0]
    
    opcode_no.append(l_no)
    add='{0:04}'.format(addr)
    address.append(add)
    addr=addr+4
    if ins=='MOVSB':                                     # MOVSB
        opcode_ins.append("o#140 ES:DI DS:SI")
    if ins=='MOVSW':                                     # MOVSW
        opcode_ins.append("o#141 ES:DI DS:SI")
    if ins=='MOVSD':                                     # MOVSD
        opcode_ins.append("o#142 ES:DI DS:SI")

    if ins=='CMPSB':                                     # CMPSB
        opcode_ins.append("o#143 DS:SI ES:DI")
    if ins=='CMPSW':                                     # CMPSW
        opcode_ins.append("o#144 DS:SI ES:DI")
    if ins=='CMPSD':                                     # CMPSD
        opcode_ins.append("o#145 DS:SI ES:DI")

    if ins=='SCASB':                                     # SCASB
        opcode_ins.append("o#146 ES:DI reg08")
    if ins=='SCASW':                                     # SCASW
        opcode_ins.append("o#147 ES:DI reg16")
    if ins=='SCASD':                                     # SCASD
        opcode_ins.append("o#148 ES:DI reg32")

    if ins=='STOSB':                                     # STOSB
        opcode_ins.append("o#149 ES:DI reg08")
    if ins=='STOSW':                                     # STOSW
        opcode_ins.append("o#150 ES:DI reg16")
    if ins=='STOSD':                                     # STOSD
        opcode_ins.append("o#151 ES:DI reg32")

    if ins=='LODSB':                                     # LODSB
        opcode_ins.append("o#152 reg08 DS:SI")
    if ins=='LODSW':                                     # LODSW
        opcode_ins.append("o#153 reg16 DS:SI")
    if ins=='LODSD':                                     # LODSD
        opcode_ins.append("o#154 reg32 DS:SI")

    if ins=='CLD':                                      # CLD
        opcode_ins.append("o#155 DF=0       ")
    if ins=='STD':                                      # STD
        opcode_ins.append("o#156 DF=1       ")
    
        
    orignal_ins.append(list1[0])
    op_val.append(opcode_no+address+opcode_ins+orignal_ins)
    return addr

    
            
def opcode_table(fname):
    l_no=1
    addr=0
    fp1=open(fname,"r")
    line1=fp1.readline()
    while(line1!=""):
        list1=line1.split()
        for i in range(len(list1)):
            if list1[i] in ins_sym:
                val=find_opcode(line1,list1,l_no,addr)
                addr=val
            if list1[i] in ins_str:
                val=find_opcode_str(line1,list1,l_no,addr)
                addr=val
           
        l_no+=1        
        line1=fp1.readline()
        

def opcode_disp():
    ln=len(op_val)
    if (op_val==[]):
        print('\t'"Intermediate Code NOT Available")
    else:
        #print('\n''\t'"Line No" '\t' "Address" '\t' "Inst Symbol"  '\t' '\t' "Original " '\n')
        for i in range(ln):
            print('\t',op_val[i][0] ,'',op_val[i][1],' ' ,op_val[i][2],'  ',op_val[i][3])
        print('\n')        
        

if __name__ == '__main__':
    
    script,filename=argv
    sym_table(filename)
    write_file()
    
    lit_table(filename)
    lit_write()
    
    opcode_table(filename)
    opcode_disp()
 
