"""
Created on Tue Feb 18 06:55:05 2020

@author: kasturivartak
"""
import time


start = time.time()


def fun_lps(DNA_pattern_list,lps):
    i=0
    j=1
    while(j < DNA_pattern_LEN):
        if(DNA_pattern_list[i] != DNA_pattern_list[j]):
            if(i==0):
                lps[j]=0
                j=j+1
            else:
                i=lps[i-1]
        else:
            lps[j]=i+1
            i=i+1
            j=j+1
    


DNA_f = open("defected_chr1_GRCh38.txt","r")
DNA_contents = DNA_f.read()
DNA_seq = DNA_contents

lamda_virus_f = open("lamda_virus.txt","r")
lamda_virus_contents = lamda_virus_f.read()
DNA_pattern=lamda_virus_contents


DNA_seq_list = list(DNA_seq)
DNA_pattern_list=list(DNA_pattern)

DNA_seq_LEN=len(DNA_seq_list)
DNA_pattern_LEN=len(DNA_pattern_list)
lps=[0] * DNA_pattern_LEN



fun_lps(DNA_pattern_list,lps)

i=0
j=0
count=0
while(i < DNA_seq_LEN):
    if(DNA_seq_list[i]==DNA_pattern_list[j]):
        i=i+1
        j=j+1
    if(j==DNA_pattern_LEN):
        print("Pattern Found at Index : "+str(i-j))
        count=count+1
        j=lps[j-1]
    elif(i<DNA_seq_LEN and DNA_seq_list[i]!=DNA_pattern_list[j]):
        if(j==0):
            i=i+1
        elif(j!=0):
            j=lps[j-1]


print("\nNo. of occurrences=",count) 

lamda_virus_f.close()
DNA_f.close()

end = time.time()

print(f"Runtime of the program is {end - start}")
