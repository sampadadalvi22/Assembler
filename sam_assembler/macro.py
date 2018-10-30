from sys import argv
from subprocess import call
from subprocess import *
import sys
import os

val_mnt=[]
val_mdt=[]
val_mac=[]
val_sma=[]
sta=0
end=0
tmp1=0
tmp2=0
flag=1
pflag=0
cnt=1
pcnt=0
mcnt=0

def check_val1(list1):
    val=[]
    val1=list1[0]
    val2=list1[1]
    val3=val2.split(',')
    if len(val3)==2:
        val4=val3[0]
        val5=val3[1]
        val.append(val1)
        val.append(val4)
        val.append(val5)
        return val
        
    if len(val3)==1:
        val4=val3[0]
        val5=0
        val.append(val1)
        val.append(val4)
        return val

def check_val(list1):
    val=[]
    val1=list1[0]
    val2=list1[1]
    val3=val2.split(',')
    if len(val3)==2:
        val4=val3[0]
        val5=val3[1]
        return val1 + ' ' + val4 + ',' + val5

    if len(val3)==1:
        val4=val3[0]
        val5=0
        return val1 + ' ' + val4

    
def mdt_table(list1,ln):
    mno=[]
    mval=[]
    global flag
    global pflag
    global cnt 
    global mcnt
    global pcnt

    if cnt>pcnt:
        if pflag is 1:
            mno.append(mcnt)
            mcnt+=1
            val=check_val(list1)
            mval.append(val)
            val_mdt.append(mno+mval)
            pflag+=1
            return

        if pflag is not 1:
            mno.append(mcnt)
            mcnt+=1
            val=check_val(list1)
            mval.append(val)
            val_mdt.append(mno+mval)
            pflag+=1
  
    return 


def mnt_table(line1,ln):
    mno=[]
    mname=[]
    mentry=[]
    mstart=[]
    mend=[]
    mline=[]
    global flag
    global pflag
    global cnt
    global pcnt
    global sta
    global end
    global tmp1
    global tmp2
    list1=line1.split()
    
    if list1==[] or list1[0]=='section':
        return
    
    if '%macro' in list1 and len(list1[0])==6:
        mno.append(cnt)
        mname.append(list1[1])
        mentry.append(int(list1[2]))
        tmp1=sta
        mstart.append(tmp1)
        val_mnt.append(mno+mname+mentry+mstart)
        #print(list1)
        cnt+=1
        pcnt+=1
        flag+=1
        
    if '%macro' not in list1 and '%endmacro' not in list1 and cnt>pcnt:
        mdt_table(list1,ln)
        #print(list1)
        
    if '%endmacro' in list1 and len(list1[0])==9:
        flag-=1
        sta=sta+pflag
        tmp2=pflag
        pflag=0
        mend.append(sta-1)
        mline.append(ln)
        val_mnt.append(mend+mline)
        #print(list1)

def append_other(line1,cnt,filename):
    glist=[]
    plist=[]
    data=['db','dw','dd','dq','dt','resb','resw','resd','resq','rest']
    inst=['mov','add','sub']
    secx=['section','global','extern']
    list1=line1.split()
    
    if list1==[]:
        glist.append(' ')
        val_mac.append(glist)
        val_sma.append(glist)
        return

    if list1[0] in secx:
        val=check_val(list1)
        glist.append('['+val+']')
        val_mac.append(glist)
        plist.append(val)
        val_sma.append(plist)

    if 'main:' in list1:
        glist.append(list1[0])
        val_mac.append(glist)
        val_sma.append(glist)
        
    elif list1[0] not in inst :
        strp=0
        endp=0
        v1=0
        v2=0
        if list1[1] not in data:
            if list1[0] not in secx: 
                val=check_val1(list1)
                v1=val[1]
                v2=val[2]
                for i in reversed(range(0,len(val_mnt),2)):
                    if val[0]==val_mnt[i][1]:
                        strp=val_mnt[i][3]
                        endp=val_mnt[i+1][0]+1
                        break
                    
        for i in range(strp,endp):
            glist=[]
            instn=['add','push','call']
            temp=(val_mdt[i][1]).split()
            val=check_val1(temp)
            
            if len(val)==3 and val[2]=='%1':
                ch='%line'+' '+str(cnt)+'+0'+' '+filename
                glist.append(ch)
                val_mac.append(glist)
                glist=[]
                val.pop(2)
                val.insert(2,v1)
                val1=val[0]
                val2=val[1]
                val3=val[2]
                glist.append(' '+val1+' '+val2+','+val3)
                val_mac.append(glist)
                val_sma.append(glist)
            if len(val)==3 and val[2]=='%2':
                val.pop(2)
                val.insert(2,v2)
                val1=val[0]
                val2=val[1]
                val3=val[2]
                glist.append(' '+val1+' '+val2+','+val3)
                val_mac.append(glist)
                val_sma.append(glist)

            if len(val)==3 and val[0] in instn:
                val1=val[0]
                val2=val[1]
                val3=val[2]
                glist.append(' '+val1+' '+val2+','+val3)
                val_mac.append(glist)
                val_sma.append(glist)

            if len(val)==2 and val[0] in instn:
                val1=val[0]
                val2=val[1]
                glist.append(' '+val1+' '+val2)
                val_mac.append(glist)
                val_sma.append(glist)

            if i==endp-1:
                glist=[]
                ch='%line'+' '+str(cnt)+'+1'+' '+filename
                glist.append(ch)
                val_mac.append(glist)
                  
        
                
    for i in range(len(list1)):
        if list1[i] in data:
            val1=list1[i-1]
            val2=list1[i]
            val3=list1[i+1]
            glist.append(' '+val1+' '+val2+' '+val3)
            val_mac.append(glist)
            val_sma.append(glist)

        if list1[i] in inst:
            val=check_val(list1)
            glist.append(' '+val)
            val_mac.append(glist)
            val_sma.append(glist)

    
def macro_table(fname):
    fp1=open(fname,"r")
    line1=fp1.readline()
    cnt=1
    list1=line1.split()
    while (line1!="" and 'section' not in list1):
        list1=line1.split()
        for i in range(len(line1)):
            mnt_table(line1,cnt)
            break
        cnt+=1
        line1=fp1.readline()
        
    append_other('section .data',cnt,fname)
    append_other(line1,cnt,fname)
    line1=fp1.readline()
    while (line1!=""):
        append_other(line1,cnt,fname)
        cnt+=1
        line1=fp1.readline() 
    fp1.close()

def mnt_display():
    if (val_mnt==[]):
        print('\t'"MNT Table NOT Available")
    else:
        ln=len(val_mnt)
        print("\n\t"" No" "\t" " Name" '\t' "entry" '\t' "start"  '\t' "end" '\n')
        for i in range(0,ln,2):
            printf=check_output(["echo"," \t"+str(val_mnt[i][0]) +"\t"+str(val_mnt[i][1])+"\t"+str(val_mnt[i][2])+"\t"+str(val_mnt[i][3])+"\t"+str(val_mnt[i+1][0])],universal_newlines=True)
            print(printf)
        print('\n')



def mdt_display():
    if (val_mdt==[]):
        print('\t'"MDT Table NOT Available")
    else:
        ln=len(val_mdt)
        for i in range(ln):
            printf=check_output(["echo",' \t'+str(val_mdt[i][0]) +'\t'+str(val_mdt[i][1])],universal_newlines=True)
            print(printf)
        print('\n')

def exp_display(fname):
    ll=len(val_mnt)
    for i in range(1,ll,2):
        print('%line',val_mnt[i][1],'+1',fname,'\n')

    
    ln=len(val_mac)
    for i in range(ln):
        print('',val_mac[i][0])
    
    print('\n')

def exp_write1(filename,fname):
    fo=open(fname,"w+")
    ll=len(val_mnt)
    ln=len(val_mac)
    for i in range(1,ll,2):
        fo.write('%line'+' '+str(val_mnt[i][1])+'+1'+' '+filename+'\n\n')

    for i in range(ln):
        fo.write(' '+str(val_mac[i][0])+'\n')

def exp_write():
    fo=open("sp.asm","w+")
    ln=len(val_sma)

    for i in range(ln):
        fo.write(" "+str(val_sma[i][0])+'\n')
            
    
        
if __name__ == '__main__':
    
    script,filename=argv
    macro_table(filename)
    #mnt_display()
    #mdt_display()
    exp_display(filename)
