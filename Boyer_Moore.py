"""
Created on Wed Mar 18 03:05:41 2020
@author: kasturivartak
"""
import time


start = time.time()

def fullSuffixMatch_case1(shiftArray, borderArray, DNA_pattern, patLen): 
    i = patLen 
    j = patLen + 1
    borderArray[i] = j
    
    while(i > 0): 
        while ((j <= patLen) and (DNA_pattern[i - 1] != DNA_pattern[j - 1])):
            if(shiftArray[j]==0):
                shiftArray[j] = j - i 
            j = borderArray[j] 
        i = i- 1
        j =j-1
        borderArray[i] = j 
    

def fullSuffixMatch_case2(shiftArray, borderArray, DNA_pattern, patLen): 
    j=borderArray[0]
    for i in range(patLen+1):
        if(shiftArray[i]==0):
            shiftArray[i]=j
        if(i==j):
            j=borderArray[j]
            

DNA_f = open("defected_chr1_GRCh38.txt","r")
DNA_contents = DNA_f.read()
DNA_seq=DNA_contents

lamda_virus_f = open("lamda_virus.txt","r")
lamda_virus_contents = lamda_virus_f.read()
DNA_pattern=lamda_virus_contents

i=0
count=0
patLen=len(DNA_pattern)
DNALen=len(DNA_seq)
    

borderArray = [0] * (patLen + 1) 
shiftArray = [0] * (patLen + 1) 
    
fullSuffixMatch_case1(shiftArray, borderArray, DNA_pattern, patLen)
fullSuffixMatch_case2(shiftArray, borderArray, DNA_pattern, patLen)
    
    
while(i <= DNALen - patLen):
    j=patLen -1
    while(j>=0 and DNA_pattern[j] == DNA_seq[i+j]):
        j=j-1
    if(j<0):
        print("\npattern found at position : ",i)
        count=count+1
        i = i +shiftArray[0]
    else:
        i = i + shiftArray[j+1]


print("\nNo. of occurrences=",count)
lamda_virus_f.close()
DNA_f.close()

end = time.time()

print(f"Runtime of the program is {end - start}")
