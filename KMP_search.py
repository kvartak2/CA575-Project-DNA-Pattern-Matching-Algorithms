
#KMP Algorithm

import pandas as pd
import numpy as np
import time


start = time.time()


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
            print("Pattern Found at Index : "+str(i-j))
            j=lps[j-1]
        elif(i<pattern_LEN and pattern_list[i]!=find_pat_list[j]):
            if(j==0):
                i=i+1
            elif(j!=0):
                j=lps[j-1]



DNA_f = open("defected_chr1_GRCh38.txt","r")
DNA_contents = DNA_f.read()
pattern=DNA_contents

lamda_virus_f = open("lamda_virus.txt","r")
lamda_virus_contents = lamda_virus_f.read()
find_pat=lamda_virus_contents


pattern_list = list(pattern)
find_pat_list=list(find_pat)

pattern_LEN=len(pattern_list)
find_pat_LEN=len(find_pat_list)
lps=[0] * find_pat_LEN



fun_lps(pattern_list,lps)

fun_pat_match(pattern_list,find_pat_list,lps)



lamda_virus_f.close()
DNA_f.close()

end = time.time()

print(f"Runtime of the program is {end - start}")
