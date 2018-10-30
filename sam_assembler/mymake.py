from sys import argv
from subprocess import call


def make_call(list1,cnt):
    # print(list1,cnt)
    """
    if len(list1)==1:
        ll=list1[0]
        ln=ll+":"
        fp1=open("make","r")
        line1=fp1.readline()
        while(line1!=""):
            list1=line1.split()
            if list1!=[] and list1[0]==ln:
                cnt=0
                while(len(line1)!=1 and line1!=""):
                    list1=line1.split()
                    if cnt>0:
                        make_call(list1,cnt)
                        cnt+=1
                        line1=fp1.readline()
                        
                    line1=fp1.readline()
    
    """
    if len(list1)==3:
        call([list1[0],list1[1],list1[2]])

    
    

if __name__ == "__main__":

    if len(argv)==1:
        cnt=0
        fp1=open("make","r")
        line1=fp1.readline()
        while(len(line1)!=1):
            list1=line1.split()
            if cnt>0:
                make_call(list1,cnt)
            cnt+=1
            line1=fp1.readline()
    
       
    
    if len(argv)==2:
        inst=argv[1]
        insc=inst+':'
        fp2=open("make","r")
        line2=(fp2.read().split())
        
        if insc not in line2:
            print("pz enter valid entry")

        if insc in line2:
            fp1=open("make","r")
            line1=fp1.readline()
            while(line1!=""):
                list1=line1.split()
                if list1!=[] and list1[0]==insc:
                    cnt=0
                    while(len(line1)!=1 and line1!=""):
                        list1=line1.split()
                        if cnt>0:
                            make_call(list1,cnt)
                        cnt+=1
                        line1=fp1.readline()
                        
                line1=fp1.readline()
    
