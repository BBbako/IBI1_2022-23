seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
#Set a variable to record the number of sequences and a variable to record the lenth of seq
num=0
lenth=len(seq)
#to calculate the number, we only need to calculate the number of TGA and TAA
for i in range(3,lenth-2,1):
    if seq[i:i+3]=='TGA'or seq[i:i+3]=='TAA':
        num=num+1
print(num)
