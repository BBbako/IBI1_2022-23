#pseudocode
# produce rabbits
# How many rabbits have been born?
#  If less than 100: keep producing
#  If more than 100: DONE!
n=4
g=2
while(n<=100):
    n=n*2
    g=g+1
print("100 rabbits have been born at "+ str(g)+" generation.")
