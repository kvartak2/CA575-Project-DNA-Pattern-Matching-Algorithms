import pandas as pd
import numpy as np

def fun_lps(pattern_list,lps):
    i=0
    j=1
    while(j<LEN):
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
    
    print(lps)




pattern="ABABC"
pattern_list = list(disease)



LEN=len(pattern_list)
lps=[0] * LEN
#lps=[]
#print(LEN)
#print(lps)


fun_lps(pattern_list,lps)


#lps[0]=0
