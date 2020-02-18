import pandas as pd
import numpy as np

def fun_lps(pattern_list,lps):
    i=0
    j=1
    while(j<find_pat_LEN):
        if(pattern_list[i]!=pattern_list[j]):
            if(i==0):
                lps[j]=0
                j=j+1
            else:
                i=lps[i-1]
        else:
            lps[j]=i+1
            i=i+1
            j=j+1
    
def fun_pat_match(pattern_list,find_pat_list,lps):   
    i=0
    j=0
    while(i<pattern_LEN):
        if(pattern_list[i]==find_pat_list[j]):
            i=i+1
            j=j+1
        if(j==find_pat_LEN):
            print("Pattern Found Index="+str(i-j))
            j=lps[j-1]
        elif(pattern_list[i]!=find_pat_list[j]):
            if(j==0):
                i=i+1
            elif(j!=0):
                j=lps[j-1]



pattern="ABABC"
pattern_list = list(disease)
find_pat="ABC"
find_pat_list=list(find_pat)



pattern_LEN=len(pattern_list)
find_pat_LEN=len(find_pat_list)
lps=[0] * find_pat_LEN
#lps=[]
#print(LEN)
#print(lps)


fun_lps(pattern_list,lps)
print(lps)
fun_pat_match(pattern_list,find_pat_list,lps)


#lps[0]=0
